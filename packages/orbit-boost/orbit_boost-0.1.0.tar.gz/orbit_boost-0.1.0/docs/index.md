# Orbit Boost

Orbit Boost is a gradient boosting classifier for tabular data featuring:
- **Oblique projections** per round (tiny linear combos of features)
- **BOSS sampling** (gradient- & rarity-based subsampling)
- **Ridge-multinomial warm-start** of logits
- **Global Newton line search** per round
- **Early stopping** on QWK

## Installation

### From PyPI
```
pip install orbit-boost
```

### From source
```
git clone https://github.com/abdulvahapmutlu/orbit-boost.git
cd orbit-boost
pip install -e .[dev]
```

## Basic usage
```
from orbit_boost import OrbitBoostClassifier

clf = OrbitBoostClassifier(
    n_estimators=256,
    learning_rate=0.05,
    random_state=42,
)
clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)
```
