import numpy as np
from sklearn.utils import check_random_state

def ridge_multinomial_logits(X, y, K, l2=1e-2, rng=None, sample_n=None):
    """Closed-form ridge for multinomial logits, bias unregularized."""
    n, d = X.shape
    if sample_n is not None and sample_n < n:
        rng = check_random_state(rng)
        idx = rng.choice(n, size=sample_n, replace=False)
        Xs = X[idx].astype(np.float32, copy=False)
        ys = y[idx]
    else:
        Xs = X.astype(np.float32, copy=False)
        ys = y

    Y = np.zeros((Xs.shape[0], K), dtype=np.float32)
    for i, t in enumerate(ys):
        Y[i, int(t)] = 1.0

    Xb = np.concatenate([np.ones((Xs.shape[0], 1), dtype=np.float32), Xs], axis=1)
    XtX = Xb.T @ Xb
    if XtX.shape[0] > 1:
        XtX[1:, 1:] += np.eye(d, dtype=np.float32) * float(l2)
    XtY = Xb.T @ Y
    try:
        W = np.linalg.solve(XtX, XtY).astype(np.float32)
    except np.linalg.LinAlgError:
        W = (np.linalg.pinv(XtX) @ XtY).astype(np.float32)
    return W  # (d+1, K)
