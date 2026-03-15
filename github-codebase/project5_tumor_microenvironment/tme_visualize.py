"""Project 5 — TME: cancer core + immune annulus. R2 = outer radius."""
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

def draw_tme(ax, R1: float = 30, R2: float = 80, n_immune: int = 40):
    theta = np.linspace(0, 2 * np.pi, 100)
    ax.fill(R1 * np.cos(theta), R1 * np.sin(theta), color="red", alpha=0.8, label="Cancer")
    ax.plot(R2 * np.cos(theta), R2 * np.sin(theta), color="steelblue", linewidth=2, label="R2")
    r_immune = R1 + (R2 - R1) * np.random.uniform(0.3, 1.0, n_immune)
    th_immune = np.random.uniform(0, 2 * np.pi, n_immune)
    ax.scatter(r_immune * np.cos(th_immune), r_immune * np.sin(th_immune), c="steelblue", s=25, alpha=0.8, label="Immune")
    ax.set_aspect("equal"); ax.set_xlim(-R2*1.2, R2*1.2); ax.set_ylim(-R2*1.2, R2*1.2); ax.legend(loc="upper right", fontsize=8)

def main():
    np.random.seed(42)
    fig, axes = plt.subplots(1, 3, figsize=(12, 4))
    for ax, R2 in zip(axes, [400, 500, 600]):
        r2_plot = 100 * (R2 / 500)
        draw_tme(ax, R1=30, R2=r2_plot, n_immune=50)
        ax.set_title(f"R2 = {R2}")
    plt.suptitle("Project 5 — TME: effect of R2"); plt.tight_layout()
    out = Path(__file__).parent / "output"; out.mkdir(exist_ok=True)
    plt.savefig(out / "tme_R2.png", dpi=150, bbox_inches="tight"); plt.show()
    plt.figure(figsize=(5,5)); ax = plt.gca(); np.random.seed(42); draw_tme(ax, R1=30, R2=80, n_immune=60)
    plt.title("Project 5 — TME single"); plt.savefig(out / "tme_single.png", dpi=150, bbox_inches="tight"); plt.show()

if __name__ == "__main__":
    main()
