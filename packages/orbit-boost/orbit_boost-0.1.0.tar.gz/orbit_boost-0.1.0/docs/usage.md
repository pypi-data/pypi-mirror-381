# Usage

## Python API (quickstart)
```
from orbit_boost import OrbitBoostClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

# X, y: numpy arrays or pandas values
Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.2, random_state=42)
scaler = StandardScaler().fit(Xtr)
Xtr_s, Xte_s = scaler.transform(Xtr), scaler.transform(Xte)

clf = OrbitBoostClassifier(
  n_estimators=256,
  learning_rate=0.05,
  max_depth=8,
  min_samples_leaf=24,
  random_state=42,
  # Optional: early stopping if you pass validation
  X_val=Xte_s, y_val=yte,
)
clf.fit(Xtr_s, ytr)
proba = clf.predict_proba(Xte_s)
pred  = clf.predict(Xte_s)
```

## CLI scripts

### Train & save model
```
python scripts/train_orbit_boost.py --data-dir PATH/TO/DATA --out-dir artifacts/orbit_boost
```
Expected CSVs inside `--data-dir`:
- `X_train_step2.csv`, `y_train_step2.csv`
- `X_val_step2.csv`,   `y_val_step2.csv`
- `X_test_step2.csv`,  `y_test_step2.csv`
Labels should be integers (0…K-1).

### Evaluate a saved model
```
python scripts/evaluate_saved_model.py \
  --data-dir PATH/TO/DATA \
  --model artifacts/orbit_boost/orbit_boost_classifier.pkl \
  --scaler artifacts/orbit_boost/scaler.pkl
```

## Parameters (common)
- `n_estimators` (int): boosting rounds.
- `learning_rate` (float): shrinkage on tree outputs.
- `max_depth` (int), `min_samples_leaf` (int): tree complexity.
- `subsample_top`, `subsample_rare`, `rare_k`: BOSS sampling knobs.
- `n_oblique`, `oblique_k`: number/size of oblique projections per round.
- `warm_start_linear`, `warm_l2`, `warm_sample_n`: ridge warm-start controls.
- `early_stopping_rounds`, `eval_every`, `X_val`, `y_val`: early stopping.
- `class_weights`: per-class multipliers for the Newton sample weights.
