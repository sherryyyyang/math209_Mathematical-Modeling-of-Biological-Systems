"""Project 2 — FBA: maximize flux subject to S·v = 0."""
import numpy as np
from scipy.optimize import linprog
from typing import Tuple

def fba_maximize_flux(S: np.ndarray, lb: np.ndarray, ub: np.ndarray, objective_flux_index: int) -> Tuple[float, np.ndarray]:
    n = S.shape[1]
    c = np.zeros(n)
    c[objective_flux_index] = -1.0
    result = linprog(c, A_ub=None, b_ub=None, A_eq=S, b_eq=np.zeros(S.shape[0]), bounds=list(zip(lb, ub)), method="highs")
    if not result.success:
        return np.nan, result.x if result.x is not None else np.full(n, np.nan)
    return float(result.x[objective_flux_index]), result.x

def simple_network() -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
    S = np.array([
        [1, -1,  0,  0,  0,  0,  0,  0],
        [0,  1, -1, -1,  0,  0,  0,  0],
        [0,  0,  1,  0, -1,  0,  0, -1],
        [0,  0,  0,  1,  0, -1, -1, -1],
        [0,  0,  0,  0,  1,  1,  0, -1],
    ], dtype=float)
    return S, np.zeros(8), np.ones(8)
