"""Project 1 — Regression: linear, quadratic, exponential. Self-contained."""
import numpy as np
from typing import Tuple


def r_squared(y_true: np.ndarray, y_pred: np.ndarray) -> float:
    ss_res = np.sum((y_true - y_pred) ** 2)
    ss_tot = np.sum((y_true - np.mean(y_true)) ** 2)
    return 0.0 if ss_tot == 0 else 1.0 - ss_res / ss_tot


def fit_linear(t: np.ndarray, y: np.ndarray) -> Tuple[np.ndarray, np.ndarray, float]:
    A = np.column_stack((np.ones_like(t), t))
    coef = np.linalg.lstsq(A, y, rcond=None)[0]
    pred = A @ coef
    return coef, pred, r_squared(y, pred)


def fit_quadratic(t: np.ndarray, y: np.ndarray) -> Tuple[np.ndarray, np.ndarray, float]:
    A = np.column_stack((np.ones_like(t), t, t**2))
    coef = np.linalg.lstsq(A, y, rcond=None)[0]
    pred = A @ coef
    return coef, pred, r_squared(y, pred)


def fit_exponential(t: np.ndarray, y: np.ndarray) -> Tuple[np.ndarray, np.ndarray, float]:
    y_pos = np.maximum(y, 1e-10)
    z = np.log(y_pos)
    A = np.column_stack((np.ones_like(t), t))
    coef = np.linalg.lstsq(A, z, rcond=None)[0]
    pred_y = np.exp(A @ coef)
    return coef, pred_y, r_squared(z, A @ coef)


def predict_linear(coef: np.ndarray, t: np.ndarray) -> np.ndarray:
    return coef[0] + coef[1] * t


def predict_quadratic(coef: np.ndarray, t: np.ndarray) -> np.ndarray:
    return coef[0] + coef[1] * t + coef[2] * t**2


def predict_exponential(coef: np.ndarray, t: np.ndarray) -> np.ndarray:
    return np.exp(coef[0] + coef[1] * t)
