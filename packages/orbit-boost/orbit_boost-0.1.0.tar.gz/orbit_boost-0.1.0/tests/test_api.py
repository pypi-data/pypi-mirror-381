import numpy as np
from orbit_boost import OrbitBoostClassifier

def test_fit_predict_shapes():
    rng = np.random.default_rng(0)
    X = rng.normal(size=(200, 10)).astype(np.float32)
    y = rng.integers(0, 3, size=200)
    clf = OrbitBoostClassifier(n_estimators=8, eval_every=2, early_stopping_rounds=4, verbose=0)
    clf.fit(X, y)
    proba = clf.predict_proba(X)
    assert proba.shape == (200, len(np.unique(y)))
    assert np.allclose(proba.sum(axis=1), 1.0, atol=1e-5)
