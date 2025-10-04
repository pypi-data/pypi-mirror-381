import numpy as np
from sklearn.neighbors import NearestNeighbors

def compute_rarity(X, rare_k=24):
    Xf = np.asarray(X, dtype=np.float32)
    if not np.isfinite(Xf).all():
        col_means = np.nanmean(Xf, axis=0)
        col_means = np.nan_to_num(col_means, nan=0.0, posinf=0.0, neginf=0.0)
        bad = ~np.isfinite(Xf)
        Xf[bad] = np.take(col_means, np.where(bad)[1])
    k = min(rare_k, max(2, Xf.shape[0] - 1))
    nn = NearestNeighbors(n_neighbors=k).fit(Xf)
    dists, _ = nn.kneighbors(Xf, return_distance=True)
    kth = dists[:, -1]
    return np.nan_to_num(kth, nan=0.0, posinf=0.0, neginf=0.0) + 1e-6

def boss_sample(rng, grad_norm, rarity, subsample_top=0.20, subsample_rare=0.25):
    n = grad_norm.shape[0]
    top_n  = int(np.ceil(subsample_top  * n))
    rare_n = int(np.ceil(subsample_rare * n))

    g = np.nan_to_num(grad_norm, nan=0.0, posinf=0.0, neginf=0.0)
    top_idx = np.argpartition(-g, kth=max(0, top_n - 1))[:top_n]
    mask_top = np.zeros(n, dtype=bool)
    mask_top[top_idx] = True

    rem_idx = np.flatnonzero(~mask_top)
    rare_idx = np.array([], dtype=int)
    if rare_n > 0 and rem_idx.size > 0:
        rar = np.nan_to_num(rarity[rem_idx], nan=0.0, posinf=0.0, neginf=0.0)
        s = rar.sum()
        p = rar / s if (s > 0 and np.isfinite(s)) else None
        if (p is not None) and (not np.isfinite(p).all() or p.sum() <= 0):
            p = None
        rare_idx = rng.choice(rem_idx, size=min(rare_n, rem_idx.size), replace=False, p=p)

    S = np.unique(np.concatenate([top_idx, rare_idx], axis=0))
    w = np.ones(n, dtype=np.float32)
    if rare_idx.size > 0:
        w[rare_idx] = (1.0 - subsample_top) / (subsample_rare + 1e-12)
    return S, w
