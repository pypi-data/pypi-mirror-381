# 🚀 Orbit Boost

[![PyPI version](https://img.shields.io/pypi/v/orbit-boost?color=blue&logo=pypi)](https://pypi.org/project/orbit-boost/)
[![Python Versions](https://img.shields.io/pypi/pyversions/orbit-boost?logo=python&logoColor=yellow)](https://pypi.org/project/orbit-boost/)
[![License](https://img.shields.io/github/license/abdulvahapmutlu/orbit-boost?color=green)](LICENSE)
[![CI](https://github.com/abdulvahapmutlu/orbit-boost/actions/workflows/ci.yml/badge.svg)](https://github.com/abdulvahapmutlu/orbit-boost/actions/workflows/ci.yml)

---

**Orbit Boost** is a research-oriented gradient boosting library built from scratch in Python, designed as an experimental alternative to LightGBM, XGBoost, and CatBoost.  
It introduces **oblique projections**, **BOSS sampling**, **Newton-style updates**, and a **ridge-based warm start** for improved performance.

---

## ✨ Features
- 🔥 **Custom Boosting Core**
  - Oblique feature projections per round
  - BOSS sampling strategy (gradient + rarity-driven)
  - Newton-style updates with global line search
  - Mild class reweighting for improved balance
- 🏎 **Warm Start**
  - Closed-form ridge multinomial initialization
- ⚡ **Parallelization**
  - Trees for each class are fit in parallel
- 🛑 **Early Stopping**
  - Based on validation Quadratic Weighted Kappa (QWK)
- 🎯 Compatible with **scikit-learn API** (`fit`, `predict`, `predict_proba`)

---

## 📦 Installation

From PyPI:
```
pip install orbit-boost
````

From source:

```
git clone https://github.com/abdulvahapmutlu/orbit-boost.git
cd orbit-boost
pip install -e .
```

---

## 🛠 Usage

```
from orbit_boost import OrbitBoostClassifier
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

X, y = load_digits(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = OrbitBoostClassifier(n_estimators=320, learning_rate=0.05, verbose=1)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
print(classification_report(y_test, y_pred))
```

---

## 📊 Benchmarking

Orbit Boost was compared against **LightGBM**, **XGBoost**, and **Random Forest** on the private **NutriScore** dataset (balanced training) on a 5-class NutriScore Dataset. 
Under-sampling applied to the whole dataset for each model, and the balanced training count for each class is (A, B, C, D, E) 103451.

### Quadratic Weighted Kappa (QWK) – Validation

| Model           | QWK (Validation) | F1-Macro | Accuracy |
| --------------- | ---------------- | -------- | -------- |
| **Orbit Boost** | **0.9549**       | 0.9161   | 0.93     |
| LightGBM        | 0.9545           | 0.9157   | 0.93     |
| XGBoost         | 0.9523           | 0.9080   | 0.92     |
| RandomForest    | 0.9504           | 0.9065   | 0.92     |

### Quadratic Weighted Kappa (QWK) – Test

| Model           | QWK (Test) | F1-Macro | Accuracy |
| --------------- | ---------- | -------- | -------- |
| **Orbit Boost** | **0.9549** | 0.9168   | 0.93     |
| LightGBM        | 0.9547     | 0.9167   | 0.93     |
| XGBoost         | 0.9527     | 0.9080   | 0.92     |
| RandomForest    | 0.9508     | 0.9069   | 0.92     |

📌 Orbit Boost achieves **state-of-the-art parity** with LightGBM on NutriScore, outperforming XGBoost and Random Forest. However, with pure Python loops, it's slower than its optimized rivals. Optimization for Orbit-Boost is a must.

---

## 🤝 Contributing

Contributions are welcome! Please read [CONTRIBUTING.md](CONTRIBUTING.md) and follow the [Code of Conduct](CODE_OF_CONDUCT.md).

---

## 📜 Citation

If you use **Orbit Boost** in academic work, please cite:

```
@software{orbit_boost2025,
  author = {Abdulvahap Mutlu},
  title = {Orbit Boost: Oblique Projection Gradient Boosting},
  year = {2025},
  url = {https://github.com/abdulvahapmutlu/orbit-boost},
}
```
---

## 📄 License

MIT License © 2025 [Abdulvahap Mutlu](https://github.com/abdulvahapmutlu)

---
