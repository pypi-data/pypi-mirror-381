import numpy as np
from orbit_boost import OrbitBoostClassifier

def test_best_iteration_set():
    rng = np.random.default_rng(0)
    X = rng.normal(size=(400, 8)).astype(np.float32)
    y = rng.integers(0, 3, size=400)
    Xv, yv = X[:120], y[:120]
    Xt, yt = X[120:], y[120:]
    clf = OrbitBoostClassifier(n_estimators=20, eval_every=5, early_stopping_rounds=5, X_val=Xv, y_val=yv, verbose=0)
    clf.fit(Xt, yt)
    assert hasattr(clf, "best_iteration_")
    assert len(clf.trees_) == clf.best_iteration_
