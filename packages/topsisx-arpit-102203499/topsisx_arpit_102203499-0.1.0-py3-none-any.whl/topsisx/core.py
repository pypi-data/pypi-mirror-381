from __future__ import annotations
from typing import Iterable, Tuple, Sequence
import numpy as np
import pandas as pd

def _to_numeric_matrix(df_or_arr) -> Tuple[np.ndarray, Sequence[str] | None]:
    if isinstance(df_or_arr, pd.DataFrame):
        df = df_or_arr.copy()
        id_col = None
        if not np.issubdtype(df.dtypes.iloc[0], np.number):
            id_col = df.columns[0]
            df = df.drop(columns=[id_col])
        numeric_df = df.select_dtypes(include=[np.number])
        if numeric_df.shape[1] != df.shape[1]:
            raise ValueError("All criteria columns must be numeric.")
        return numeric_df.to_numpy(dtype=float), (df_or_arr[id_col].tolist() if id_col else None)
    else:
        arr = np.asarray(df_or_arr, dtype=float)
        return arr, None

def topsis(
    data: pd.DataFrame | np.ndarray,
    weights: Iterable[float],
    impacts: Iterable[str],
) -> Tuple[np.ndarray, np.ndarray]:
    X, _ = _to_numeric_matrix(data)
    m, n = X.shape
    w = np.asarray(list(weights), dtype=float)
    s = np.asarray([1 if str(x).strip() in ['+','benefit','b'] else -1 for x in impacts], dtype=int)

    if w.size != n or s.size != n:
        raise ValueError(f"weights/impacts length must be {n}.")
    if np.any(w <= 0):
        raise ValueError("All weights must be positive.")

    norms = np.linalg.norm(X, axis=0)
    if np.any(norms == 0):
        raise ValueError("A criterion column has zero norm; cannot normalize.")
    X_norm = X / norms

    w = w / w.sum()
    V = X_norm * w

    ideal_best = np.where(s == 1, V.max(axis=0), V.min(axis=0))
    ideal_worst = np.where(s == 1, V.min(axis=0), V.max(axis=0))

    d_plus = np.linalg.norm(V - ideal_best, axis=1)
    d_minus = np.linalg.norm(V - ideal_worst, axis=1)

    scores = d_minus / (d_plus + d_minus)
    order = np.argsort(-scores, kind="stable")
    ranks = np.empty_like(order)
    ranks[order] = np.arange(1, m + 1)
    return scores, ranks
