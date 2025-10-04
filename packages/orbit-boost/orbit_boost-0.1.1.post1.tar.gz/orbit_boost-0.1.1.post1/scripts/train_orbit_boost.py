import os
import argparse
import json
import pandas as pd
import joblib
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report, cohen_kappa_score, f1_score, confusion_matrix
from orbit_boost import OrbitBoostClassifier

def load_csvs(data_dir):
    Xtr = pd.read_csv(os.path.join(data_dir, "X_train_step2.csv"))
    ytr = pd.read_csv(os.path.join(data_dir, "y_train_step2.csv")).squeeze().values - 1
    Xva = pd.read_csv(os.path.join(data_dir, "X_val_step2.csv"))
    yva = pd.read_csv(os.path.join(data_dir, "y_val_step2.csv")).squeeze().values - 1
    Xte = pd.read_csv(os.path.join(data_dir, "X_test_step2.csv"))
    yte = pd.read_csv(os.path.join(data_dir, "y_test_step2.csv")).squeeze().values - 1
    return Xtr, ytr, Xva, yva, Xte, yte

def undersample_to(y, X, target_class):
    ref = int((y == target_class).sum())
    df = pd.DataFrame(X)
    df["target"] = y
    bal = df.groupby("target", group_keys=False).apply(
        lambda g: g.sample(n=ref, random_state=42)
    ).reset_index(drop=True)
    Xb = bal.drop(columns="target").values
    yb = bal["target"].values
    return Xb, yb

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--data-dir", required=True)
    ap.add_argument("--out-dir",  required=True)
    ap.add_argument("--params",   default=None, help="JSON file with OrbitBoost defaults")
    args = ap.parse_args()

    os.makedirs(args.out_dir, exist_ok=True)

    Xtr, ytr, Xva, yva, Xte, yte = load_csvs(args.data_dir)
    scaler = StandardScaler().fit(Xtr)
    Xtr, Xva, Xte = scaler.transform(Xtr), scaler.transform(Xva), scaler.transform(Xte)

    # Balance to class '1' count (as in your script)
    Xb, yb = undersample_to(ytr, Xtr, target_class=1)

    params = {
        "n_estimators": 512,
        "learning_rate": 0.05,
        "max_depth": 8,
        "min_samples_leaf": 24,
        "subsample_top": 0.20,
        "subsample_rare": 0.25,
        "rare_k": 24,
        "n_oblique": 16,
        "oblique_k": 3,
        "n_jobs": -1,
        "random_state": 42,
        "verbose": 1,
        "early_stopping_rounds": 40,
        "eval_every": 10,
        # validation for early stopping
        "X_val": Xva, "y_val": yva,
        # warm-start
        "warm_start_linear": True,
        "warm_l2": 1e-2,
        "warm_sample_n": 120_000,
        # mild class weights default handled in estimator
    }
    if args.params:
        with open(args.params) as f:
            params.update(json.load(f))

    model = OrbitBoostClassifier(**params).fit(Xb, yb)

    def eval_split(name, Xs, ys):
        preds = model.predict(Xs)
        print(f"\n-- {name} --")
        print(classification_report(ys, preds, target_names=['A','B','C','D','E']))
        print("Quadratic Kappa:", cohen_kappa_score(ys, preds, weights='quadratic'))
        print("F1-macro:      ", f1_score(ys, preds, average='macro'))
        print("Confusion Matrix:\n", confusion_matrix(ys, preds, labels=[0,1,2,3,4]))

    eval_split("Validation", Xva, yva)
    eval_split("Test",       Xte, yte)

    joblib.dump(model,  os.path.join(args.out_dir, "orbit_boost_classifier.pkl"))
    joblib.dump(scaler, os.path.join(args.out_dir, "scaler.pkl"))
    print("\nSaved model and scaler.")

if __name__ == "__main__":
    main()
