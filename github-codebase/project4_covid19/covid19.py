"""Project 4 — COVID-19: S, E, A, I, H, R, D."""
import numpy as np
from scipy.integrate import solve_ivp
from typing import Tuple, Optional

def covid19_rhs(t: float, state: np.ndarray, delta: float, pc: float, pca: float, R0: float, h0: float, r0: float) -> np.ndarray:
    S, E, A, I, H, R, D = state
    N = S + E + A + I + H + R + D
    if N <= 0: return np.zeros(7)
    beta, gamma, sigma, eta, mu = R0 * delta * 0.1, 0.1, 0.2, 0.3, 0.01
    dS = -beta * S * (A + I) / N
    dE = beta * S * (A + I) / N - sigma * E
    dA = sigma * E * (1 - pc) - gamma * A
    dI = sigma * E * pc - eta * I
    dH = eta * I * h0 - r0 * H - mu * H
    dR = gamma * A + eta * I * (1 - h0) + r0 * H
    dD = mu * H
    return np.array([dS, dE, dA, dI, dH, dR, dD])

def simulate_covid19(delta: float = 1.0, pc: float = 0.0, pca: float = 0.0, R0: float = 5.7, h0: float = 0.01, r0: float = 0.1, t_max: int = 200, y0: Optional[np.ndarray] = None) -> Tuple[np.ndarray, np.ndarray]:
    if y0 is None: y0 = np.array([1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
    def rhs(t, y): return covid19_rhs(t, y, delta, pc, pca, R0, h0, r0)
    t_eval = np.linspace(0, t_max, max(500, t_max))
    sol = solve_ivp(rhs, (0, t_max), y0, t_eval=t_eval, method="RK45")
    return sol.t, sol.y
