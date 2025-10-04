import numpy as np
from sklearn.utils import check_random_state

class _ObliqueProjector:
    """Per-round tiny oblique projections (k features)."""
    def __init__(self, n_oblique=16, k=3, random_state=None):
        self.n_oblique = int(n_oblique)
        self.k = int(k)
        self.random_state = check_random_state(random_state)
        self.defs_ = []  # list of proj_defs per boosting round

    def new_round(self, n_features):
        rng = self.random_state
        proj_defs = []
        for _ in range(self.n_oblique):
            idxs = rng.choice(n_features, size=self.k, replace=False)
            w = rng.normal(size=self.k).astype(np.float32)
            w /= (np.linalg.norm(w) + 1e-12)
            proj_defs.append((idxs, w))
        self.defs_.append(proj_defs)
        return proj_defs

    @staticmethod
    def _apply_once(X, proj_defs):
        Z = np.empty((X.shape[0], len(proj_defs)), dtype=np.float32)
        for j, (idxs, w) in enumerate(proj_defs):
            Z[:, j] = X[:, idxs].dot(w)
        return Z

    def transform_round(self, X, round_idx):
        return self._apply_once(X, self.defs_[round_idx])
