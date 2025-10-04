import numpy as np
from orbit_boost import OrbitBoostClassifier

def test_seed_reproducibility():
    rng = np.random.default_rng(42)
    X = rng.normal(size=(300, 12)).astype(np.float32)
    y = rng.integers(0, 4, size=300)

    m1 = OrbitBoostClassifier(n_estimators=12, random_state=123, verbose=0).fit(X, y)
    m2 = OrbitBoostClassifier(n_estimators=12, random_state=123, verbose=0).fit(X, y)
    p1 = m1.predict(X)
    p2 = m2.predict(X)
    assert (p1 == p2).mean() > 0.98
