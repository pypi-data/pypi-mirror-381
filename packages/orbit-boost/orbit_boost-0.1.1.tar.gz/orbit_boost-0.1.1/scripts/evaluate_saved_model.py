import os
import argparse
import joblib
import pandas as pd
from sklearn.metrics import classification_report, cohen_kappa_score, f1_score, confusion_matrix

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--data-dir", required=True)
    ap.add_argument("--model",    required=True)
    ap.add_argument("--scaler",   required=True)
    args = ap.parse_args()

    Xte = pd.read_csv(os.path.join(args.data_dir, "X_test_step2.csv"))
    yte = pd.read_csv(os.path.join(args.data_dir, "y_test_step2.csv")).squeeze().values - 1

    model  = joblib.load(args.model)
    scaler = joblib.load(args.scaler)
    Xte = scaler.transform(Xte)

    preds = model.predict(Xte)
    print(classification_report(yte, preds, target_names=['A','B','C','D','E']))
    print("Quadratic Kappa:", cohen_kappa_score(yte, preds, weights='quadratic'))
    print("F1-macro:      ", f1_score(yte, preds, average='macro'))
    print("Confusion Matrix:\n", confusion_matrix(yte, preds, labels=[0,1,2,3,4]))

if __name__ == "__main__":
    main()
