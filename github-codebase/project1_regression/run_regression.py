"""Project 1 — Run regression: linear, quadratic, exponential."""
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
from regression import (
    fit_linear, fit_quadratic, fit_exponential,
    predict_linear, predict_quadratic, predict_exponential,
)

def main():
    data_path = Path(__file__).parent / "hw1_data.csv"
    if data_path.exists():
        import pandas as pd
        data = pd.read_csv(data_path, header=None)
        t = data.iloc[0:65, 0].values
        y = data.iloc[0:65, 1].values
    else:
        np.random.seed(42)
        t = np.linspace(0, 100, 50)
        y = 2.0 + 0.08 * t + 0.001 * t**2 + np.random.normal(0, 1.5, size=t.shape)

    coef_lin, _, r2_lin = fit_linear(t, y)
    coef_quad, _, r2_quad = fit_quadratic(t, y)
    coef_exp, _, r2_exp = fit_exponential(t, y)
    print("Project 1 — R² linear:", round(r2_lin, 4), "quadratic:", round(r2_quad, 4), "exponential:", round(r2_exp, 4))

    t_plot = np.linspace(t.min(), t.max(), 200)
    plt.figure(figsize=(8, 5))
    plt.scatter(t, y, color="red", marker="x", label="Data")
    plt.plot(t_plot, predict_linear(coef_lin, t_plot), "k--", label="Linear")
    plt.plot(t_plot, predict_quadratic(coef_quad, t_plot), "b-", label="Quadratic")
    plt.plot(t_plot, predict_exponential(coef_exp, t_plot), "g-", label="Exponential")
    plt.xlabel("t"); plt.ylabel("y"); plt.legend(); plt.grid(True)
    plt.title("Project 1 — Regression fits")
    out = Path(__file__).parent / "output"
    out.mkdir(exist_ok=True)
    plt.savefig(out / "regression_fits.png", dpi=150, bbox_inches="tight")
    plt.show()

if __name__ == "__main__":
    main()
