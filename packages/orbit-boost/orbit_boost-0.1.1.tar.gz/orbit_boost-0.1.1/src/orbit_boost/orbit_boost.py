# ====================== Orbit Boost ======================
import time
import numpy as np

from sklearn.tree import DecisionTreeRegressor
from sklearn.utils import check_random_state
from sklearn.base import BaseEstimator, ClassifierMixin
from sklearn.utils.validation import check_is_fitted
from joblib import Parallel, delayed

from ._oblique import _ObliqueProjector
from ._linear_warmstart import ridge_multinomial_logits as _ridge_multinomial_logits
from ._sampling import compute_rarity as _compute_rarity, boss_sample as _boss_sample

# ---------- core utils ----------
def _softmax(Z: np.ndarray) -> np.ndarray:
    """Row-wise softmax with numerical stability."""
    Z = Z - Z.max(axis=1, keepdims=True)
    np.exp(Z, out=Z)
    Z_sum = Z.sum(axis=1, keepdims=True)
    Z /= (Z_sum + 1e-12)
    return Z


class OrbitBoostClassifier(BaseEstimator, ClassifierMixin):
    """
    Orbit Boost:
      • Multiclass gradient boosting (softmax, argmax decode)
      • BOSS sampling (top-|g| + rarity-weighted remainder)
      • Oblique projections per boosting round (tiny k-feature linear combos)
      • Newton-style per-class weights + global scalar line search
      • Early stopping on validation QWK (incremental update)
      • Parallel per-class regression trees

      NEW (lightweight):
      • Ridge-multinomial warm-start logits (closed-form, optional subsample)
      • Mild class reweighting in the Newton step (e.g., slight focus on classes B/C)

      Removed/avoided:
      • No calibration, no threshold sweep, no ordinal/double heads, no linear leaves

    Notes
    -----
    * Input X must be numerical and finite; the code attempts to heal NaNs/Inf in rarity calc.
    * Validation arrays (X_val, y_val) may be provided via constructor for early stopping.
    """

    def __init__(
        self,
        n_estimators=320,
        learning_rate=0.05,
        max_depth=8,
        min_samples_leaf=24,
        subsample_top=0.20,
        subsample_rare=0.25,
        rare_k=24,
        n_oblique=16,
        oblique_k=3,
        n_jobs=-1,
        random_state=42,
        verbose=1,
        # early stopping
        early_stopping_rounds=40,
        eval_every=10,
        X_val=None,
        y_val=None,
        # warm start (linear)
        warm_start_linear=True,
        warm_l2=1e-2,
        warm_sample_n=120_000,   # subset size for ridge; None -> use all
        # class reweight (per-class multipliers on the Newton sample_weight)
        class_weights=None,      # default: [1.00, 1.06, 1.03, 1.00, 1.00] if K>=5
    ):
        self.n_estimators = int(n_estimators)
        self.learning_rate = float(learning_rate)
        self.max_depth = int(max_depth)
        self.min_samples_leaf = int(min_samples_leaf)
        self.subsample_top = float(subsample_top)
        self.subsample_rare = float(subsample_rare)
        self.rare_k = int(rare_k)
        self.n_oblique = int(n_oblique)
        self.oblique_k = int(oblique_k)
        self.n_jobs = int(n_jobs)
        self.random_state = random_state
        self.verbose = int(verbose)
        self.early_stopping_rounds = int(early_stopping_rounds) if early_stopping_rounds else 0
        self.eval_every = int(eval_every)
        self._X_val = None if X_val is None else np.asarray(X_val, dtype=np.float32)
        self._y_val = None if y_val is None else np.asarray(y_val)

        self.warm_start_linear = bool(warm_start_linear)
        self.warm_l2 = float(warm_l2)
        self.warm_sample_n = None if warm_sample_n is None else int(warm_sample_n)

        self.class_weights = class_weights  # can be None -> default set in fit()

    # ----- helpers -----
    def _one_hot(self, y):
        classes = np.unique(y)
        class_to_index = {c: i for i, c in enumerate(classes)}
        K = len(classes)
        Y = np.zeros((y.shape[0], K), dtype=np.float32)
        for i, label in enumerate(y):
            Y[i, class_to_index[label]] = 1.0
        return Y, classes

    # ----- API -----
    def fit(self, X, y):
        X = np.asarray(X, dtype=np.float32)
        y = np.asarray(y)
        self._rng = check_random_state(self.random_state)

        Y_onehot, classes = self._one_hot(y)
        self.classes_ = classes
        K = Y_onehot.shape[1]
        n, d = X.shape

        # set default class weights if none provided (slight extra focus on B/C)
        if self.class_weights is None:
            cw = np.ones(K, dtype=np.float32)
            # assume labels 0..4 map to A..E; give B (+6%) and C (+3%) tiny boosts
            if K >= 5:
                if 1 < K:
                    cw[1] = 1.06
                if 2 < K:
                    cw[2] = 1.03
            self.class_weights_ = cw
        else:
            cw = np.asarray(self.class_weights, dtype=np.float32)
            if cw.shape[0] != K:
                raise ValueError("class_weights must have length equal to number of classes (K)")
            self.class_weights_ = cw

        # rarity (once)
        rarity = _compute_rarity(X)

        # init logits
        have_val = (self._X_val is not None) and (self._y_val is not None)
        F = np.zeros((n, K), dtype=np.float32)

        # ------- warm-start linear logits (closed-form ridge on a subsample) -------
        if self.warm_start_linear:
            W = _ridge_multinomial_logits(
                X, y, K=K, l2=self.warm_l2, rng=self._rng, sample_n=self.warm_sample_n
            )  # (d+1, K)
            Xb = np.concatenate([np.ones((n, 1), dtype=np.float32), X], axis=1)
            F = Xb @ W
            if have_val:
                Xvb = np.concatenate(
                    [np.ones((self._X_val.shape[0], 1), dtype=np.float32), self._X_val],
                    axis=1
                )
                F_val = Xvb @ W
        else:
            if have_val:
                F_val = np.zeros((self._X_val.shape[0], K), dtype=np.float32)

        self.trees_ = []
        self.proj_ = _ObliqueProjector(
            n_oblique=self.n_oblique, k=self.oblique_k, random_state=self._rng
        )

        best_kappa = -np.inf
        best_iter = 0
        rounds_since_improve = 0

        t0 = time.time()
        for t in range(self.n_estimators):
            # gradient & Hessian at current F
            P = _softmax(F.copy())
            G = Y_onehot - P
            H = P * (1.0 - P)
            grad_norm = np.sqrt((G ** 2).sum(axis=1))

            # BOSS sampling
            S, w_boss = _boss_sample(self._rng, grad_norm, rarity, self.subsample_top, self.subsample_rare)
            X_S = X[S]

            # projections for this round
            proj_defs = self.proj_.new_round(d)
            Z_S   = _ObliqueProjector._apply_once(X_S, proj_defs)
            Z_all = _ObliqueProjector._apply_once(X,  proj_defs)
            Xaug_S   = np.hstack([X_S, Z_S])
            Xaug_all = np.hstack([X,   Z_all])

            if have_val:
                Z_val = _ObliqueProjector._apply_once(self._X_val, proj_defs)
                Xaug_val = np.hstack([self._X_val, Z_val])

            # --- fit K regressors in parallel (threads) ---
            cw = self.class_weights_

            def _fit_and_predict(k):
                target = G[S, k]
                sw = cw[k] * w_boss[S] * np.clip(H[S, k], 1e-6, 1.0).astype(np.float32)
                tree = DecisionTreeRegressor(
                    max_depth=self.max_depth,
                    min_samples_leaf=self.min_samples_leaf,
                    random_state=self._rng.randint(0, 1_000_000)
                )
                tree.fit(Xaug_S, target, sample_weight=sw)
                pred_train = tree.predict(Xaug_all)
                pred_val   = tree.predict(Xaug_val) if have_val else None
                return tree, pred_train.astype(np.float32), (
                    None if pred_val is None else pred_val.astype(np.float32)
                )

            results = Parallel(n_jobs=self.n_jobs, prefer="threads")(
                delayed(_fit_and_predict)(k) for k in range(K)
            )
            round_trees, preds_train_list, preds_val_list = zip(*results)
            self.trees_.append(list(round_trees))

            # stack preds to shape (n, K)
            F_add = np.stack(preds_train_list, axis=1) * self.learning_rate

            # --- scalar Newton line search: η = (Σ G*f)/(Σ H*f^2) ---
            num = float((G * F_add).sum())
            den = float((H * (F_add ** 2)).sum())
            eta = 1.0 if den <= 1e-12 else np.clip(num / den, 0.0, 2.0)  # clip for stability

            # apply to train logits
            F += eta * F_add

            # incremental val update
            if have_val:
                F_add_val = np.stack(preds_val_list, axis=1) * (self.learning_rate * eta)
                F_val += F_add_val

            # logging
            if self.verbose and ((t + 1) % max(1, self.n_estimators // 10) == 0 or (t + 1) == self.n_estimators):
                elapsed = time.time() - t0
                it_done = t + 1
                it_left = self.n_estimators - it_done
                eta_time = elapsed / it_done * it_left if it_done > 0 else 0.0
                print(f"[OrbitBoost] iter {it_done}/{self.n_estimators} | η={eta:.3f} | elapsed {elapsed:,.1f}s | ETA {eta_time:,.1f}s")

            # early stopping on QWK every eval_every rounds
            if have_val and (self.early_stopping_rounds > 0) and ((t + 1) % self.eval_every == 0 or (t + 1) == self.n_estimators):
                # Compute QWK on argmax decode
                from sklearn.metrics import cohen_kappa_score
                y_pred_val = np.argmax(_softmax(F_val.copy()), axis=1)
                kappa = cohen_kappa_score(self._y_val, y_pred_val, weights='quadratic')
                if self.verbose:
                    print(f"[OrbitBoost][val] iter {t+1}  kappa={kappa:.6f}  best={best_kappa:.6f}")
                if kappa > best_kappa + 1e-6:
                    best_kappa = kappa
                    best_iter = t + 1
                    rounds_since_improve = 0
                else:
                    rounds_since_improve += self.eval_every
                    if rounds_since_improve >= self.early_stopping_rounds:
                        if self.verbose:
                            print(f"[OrbitBoost] Early stopping at iter {t+1} (best @ {best_iter}, kappa={best_kappa:.6f})")
                        break

        # finalize best iteration (truncate)
        last_iter = t + 1
        self.best_iteration_ = best_iter if have_val and best_iter > 0 else last_iter
        self.best_score_ = best_kappa if have_val else None
        self.trees_ = self.trees_[:self.best_iteration_]
        self.proj_.defs_ = self.proj_.defs_[:self.best_iteration_]
        return self

    def _decision_function(self, X):
        check_is_fitted(self, ("trees_", "classes_", "proj_"))
        X = np.asarray(X, dtype=np.float32)
        n = X.shape[0]
        K = len(self.classes_)
        F = np.zeros((n, K), dtype=np.float32)
        for t, round_trees in enumerate(self.trees_):
            Z = self.proj_.transform_round(X, t)
            Xaug = np.hstack([X, Z])
            for k, tree in enumerate(round_trees):
                F[:, k] += self.learning_rate * tree.predict(Xaug)
        return F

    def predict_proba(self, X):
        F = self._decision_function(X)
        return _softmax(F)

    def predict(self, X):
        P = self.predict_proba(X)
        idx = np.argmax(P, axis=1)
        return self.classes_[idx]
