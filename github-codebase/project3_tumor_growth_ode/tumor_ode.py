"""Project 3 — Tumor growth ODE with drug PK."""
import numpy as np
from scipy.integrate import solve_ivp
from typing import Tuple, Optional

PARAMS = {"lambda0": 0.146, "lambda1": 0.334, "w0": 0.085, "V": 4.85, "phi": 20.0, "k1": 0.469, "k2": 0.842, "k21": 1.4784, "alpha": 13.582, "beta": 1.445, "t0_dose": 13.0}

def drug_concentration(t: float, D: float, V: float, alpha: float, beta: float, k21: float, t0: float) -> float:
    if t <= t0: return 0.0
    A = (D / V) * (alpha - k21) / (alpha - beta)
    B = -(D / V) * (beta - k21) / (alpha - beta)
    tau = t - t0
    return A * np.exp(-alpha * tau) + B * np.exp(-beta * tau)

def tumor_ode(t: float, x: np.ndarray, D: float, p: dict) -> np.ndarray:
    x1, x2, x3, x4 = x
    w = x1 + x2 + x3 + x4
    c = drug_concentration(t, D, p["V"], p["alpha"], p["beta"], p["k21"], p["t0_dose"])
    denom = (1 + (p["lambda0"] / p["lambda1"] * w) ** p["phi"]) ** (1 / p["phi"])
    dx1 = (p["lambda0"] * x1) / denom - p["k2"] * c * x1
    dx2 = p["k2"] * c * x1 - p["k1"] * x2
    dx3 = p["k1"] * (x2 - x3)
    dx4 = p["k1"] * (x3 - x4)
    return np.array([dx1, dx2, dx3, dx4])

def simulate_tumor_growth(D: float, t_span: Tuple[float, float] = (0, 40), t_eval: Optional[np.ndarray] = None, x0: Optional[np.ndarray] = None, params: Optional[dict] = None) -> Tuple[np.ndarray, np.ndarray]:
    p = {**PARAMS} if params is None else {**PARAMS, **params}
    if x0 is None: x0 = np.array([p["w0"], 0.0, 0.0, 0.0])
    def rhs(t, x): return tumor_ode(t, x, D, p)
    if t_eval is None: t_eval = np.linspace(t_span[0], t_span[1], 500)
    sol = solve_ivp(rhs, t_span, x0, t_eval=t_eval, method="RK45")
    return sol.t, np.sum(sol.y, axis=0)
