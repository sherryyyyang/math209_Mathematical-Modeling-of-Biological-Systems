"""Generate all figures; save to each project's outputs/ subfolder and optionally showcase-website/assets/."""
import sys
from pathlib import Path
import matplotlib.pyplot as plt

REPO = Path(__file__).resolve().parent.parent  # github-codebase
ASSETS_DIR = REPO.parent / "showcase-website" / "assets"  # 209/showcase-website/assets

ASSETS_DIR.mkdir(parents=True, exist_ok=True)

PROJECT_NAMES = [
    "project1_regression",
    "project2_flux_balance_analysis",
    "project3_tumor_growth_ode",
    "project4_covid19",
    "project5_tumor_microenvironment",
]
for name in PROJECT_NAMES:
    sys.path.insert(0, str(REPO / name))

def _save(project_name, fig_name):
    out_dir = REPO / project_name / "outputs"
    out_dir.mkdir(parents=True, exist_ok=True)
    plt.savefig(out_dir / fig_name, dpi=150, bbox_inches="tight")
    if ASSETS_DIR.exists():
        plt.savefig(ASSETS_DIR / fig_name, dpi=150, bbox_inches="tight")
    plt.close()

def main():
    import numpy as np

    # Project 1
    from regression import fit_linear, fit_quadratic, fit_exponential, predict_linear, predict_quadratic, predict_exponential
    np.random.seed(42)
    t = np.linspace(0, 100, 50)
    y = 2.0 + 0.08*t + 0.001*t**2 + np.random.normal(0, 1.5, size=t.shape)
    coef_lin, _, _ = fit_linear(t, y)
    coef_quad, _, _ = fit_quadratic(t, y)
    coef_exp, _, _ = fit_exponential(t, y)
    t_plot = np.linspace(t.min(), t.max(), 200)
    plt.figure(figsize=(7,4))
    plt.scatter(t, y, color="red", marker="x", label="Data")
    plt.plot(t_plot, predict_linear(coef_lin, t_plot), "k--", label="Linear")
    plt.plot(t_plot, predict_quadratic(coef_quad, t_plot), "b-", label="Quadratic")
    plt.plot(t_plot, predict_exponential(coef_exp, t_plot), "g-", label="Exponential")
    plt.xlabel("t"); plt.ylabel("y"); plt.legend(); plt.grid(True); plt.title("Project 1 — Regression")
    _save("project1_regression", "fig_regression.png")
    plt.figure(figsize=(6,4)); plt.scatter(t, y, color="red", marker="x"); plt.plot(t_plot, predict_linear(coef_lin, t_plot), "k--"); plt.xlabel("t"); plt.ylabel("y"); plt.grid(True); plt.title("Linear"); _save("project1_regression", "fig_regression_linear.png")
    plt.figure(figsize=(6,4)); plt.scatter(t, y, color="red", marker="x"); plt.plot(t_plot, predict_quadratic(coef_quad, t_plot), "b-"); plt.xlabel("t"); plt.ylabel("y"); plt.grid(True); plt.title("Quadratic"); _save("project1_regression", "fig_regression_quadratic.png")
    plt.figure(figsize=(6,4)); plt.scatter(t, y, color="red", marker="x"); plt.plot(t_plot, predict_exponential(coef_exp, t_plot), "g-"); plt.xlabel("t"); plt.ylabel("y"); plt.grid(True); plt.title("Exponential"); _save("project1_regression", "fig_regression_exponential.png")

    # Project 2
    from fba import simple_network, fba_maximize_flux
    S, lb, ub = simple_network()
    opt, _ = fba_maximize_flux(S, lb, ub, 7)
    ub4 = ub.copy(); ub4[3] = 0; opt4, _ = fba_maximize_flux(S, lb, ub4, 7)
    ub3 = ub.copy(); ub3[2] = 0; opt3, _ = fba_maximize_flux(S, lb, ub3, 7)
    plt.figure(figsize=(5,4))
    plt.bar(["Baseline", "KO v4", "KO v3"], [opt, opt4, opt3], color=["#2ecc71", "#e74c3c", "#e74c3c"])
    plt.ylabel("Optimal biomass flux"); plt.title("Project 2 — FBA"); _save("project2_flux_balance_analysis", "fig_fba.png")

    # Project 3
    from tumor_ode import simulate_tumor_growth
    t, w0 = simulate_tumor_growth(0, t_span=(0,40))
    _, w45 = simulate_tumor_growth(45, t_span=(0,40))
    _, w60 = simulate_tumor_growth(60, t_span=(0,40))
    plt.figure(figsize=(7,4))
    plt.plot(t, w0, label="D=0"); plt.plot(t, w45, label="D=45"); plt.plot(t, w60, label="D=60")
    plt.xlabel("time"); plt.ylabel("tumor weight"); plt.legend(); plt.grid(True); plt.title("Project 3 — Tumor growth")
    _save("project3_tumor_growth_ode", "fig_tumor_growth.png")

    # Project 4
    from covid19 import simulate_covid19
    t_max = 200
    t, Y = simulate_covid19(delta=1.0, R0=5.7, t_max=t_max)
    S, E, A, I, H, R, D = Y
    plt.figure(figsize=(7,4))
    plt.plot(t, S, label="S"); plt.plot(t, E, label="E"); plt.plot(t, A+I+H, label="A+I+H"); plt.plot(t, R+D, label="R+D")
    plt.xlabel("time"); plt.ylabel("fraction"); plt.legend(); plt.grid(True); plt.title("Project 4 — COVID-19")
    _save("project4_covid19", "fig_covid19.png")
    fig, axes = plt.subplots(2, 2, figsize=(10,8))
    axes[0,0].plot(t, S, label="S"); axes[0,0].plot(t, E, label="E"); axes[0,0].plot(t, A+I+H, label="A+I+H"); axes[0,0].plot(t, R+D, label="R+D"); axes[0,0].legend(); axes[0,0].set_title("Compartments")
    axes[0,1].plot(t, D); axes[0,1].set_title("Cumulative deaths")
    axes[1,0].plot(t, np.concatenate([[0], np.diff(S)])); axes[1,0].set_title("Daily new cases")
    axes[1,1].plot(t, H*1e5); axes[1,1].set_title("Hospitalizations per 100k")
    plt.suptitle("Project 4 — COVID-19 baseline"); plt.tight_layout()
    _save("project4_covid19", "fig_covid19_baseline.png")
    plt.figure(figsize=(7,4))
    for d, label in [(1,"δ=1"), (0.8,"δ=0.8"), (0.6,"δ=0.6"), (0.4,"δ=0.4")]:
        _, Yd = simulate_covid19(delta=d, R0=5.7, t_max=t_max)
        plt.plot(t, Yd[6], label=label)
    plt.xlabel("time"); plt.ylabel("Cumulative deaths"); plt.legend(); plt.title("Project 4 — Effect of delta"); plt.grid(True)
    _save("project4_covid19", "fig_covid19_delta.png")

    # Project 5
    from tme_visualize import draw_tme
    fig, axes = plt.subplots(1, 3, figsize=(12,4))
    np.random.seed(42)
    for ax, R2 in zip(axes, [400, 500, 600]):
        draw_tme(ax, R1=30, R2=100*(R2/500), n_immune=50)
        ax.set_title(f"R2 = {R2}")
    plt.suptitle("Project 5 — TME: effect of R2"); plt.tight_layout()
    _save("project5_tumor_microenvironment", "fig_tme.png")
    plt.figure(figsize=(5,5)); ax = plt.gca(); np.random.seed(42); draw_tme(ax, R1=30, R2=80, n_immune=60)
    plt.title("Project 5 — TME single"); _save("project5_tumor_microenvironment", "fig_tme_single.png")

    print("Figures saved to each project's outputs/ subfolder")
    if ASSETS_DIR.exists():
        print("Figures for website:", ASSETS_DIR)

if __name__ == "__main__":
    main()
