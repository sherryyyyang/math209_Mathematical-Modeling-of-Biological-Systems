"""Project 4 — Run COVID-19: baseline and delta comparison."""
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
from covid19 import simulate_covid19

def main():
    t_max = 200
    t, Y = simulate_covid19(delta=1.0, R0=5.7, t_max=t_max)
    S, E, A, I, H, R, D = Y
    fig, axes = plt.subplots(2, 2, figsize=(10, 8))
    axes[0,0].plot(t, S, label="S"); axes[0,0].plot(t, E, label="E"); axes[0,0].plot(t, A+I+H, label="A+I+H"); axes[0,0].plot(t, R+D, label="R+D"); axes[0,0].legend(); axes[0,0].set_title("Compartments")
    axes[0,1].plot(t, D); axes[0,1].set_title("Cumulative deaths")
    axes[1,0].plot(t, np.concatenate([[0], np.diff(S)])); axes[1,0].set_title("Daily new cases")
    axes[1,1].plot(t, H*1e5); axes[1,1].set_title("Hospitalizations per 100k")
    plt.suptitle("Project 4 — COVID-19 baseline"); plt.tight_layout()
    out = Path(__file__).parent / "output"; out.mkdir(exist_ok=True)
    plt.savefig(out / "covid19_baseline.png", dpi=150, bbox_inches="tight"); plt.show()
    plt.figure(figsize=(7,4))
    for d, label in [(1,"δ=1"), (0.8,"δ=0.8"), (0.6,"δ=0.6"), (0.4,"δ=0.4")]:
        _, Yd = simulate_covid19(delta=d, R0=5.7, t_max=t_max)
        plt.plot(t, Yd[6], label=label)
    plt.xlabel("time"); plt.ylabel("Cumulative deaths"); plt.legend(); plt.title("Effect of delta"); plt.grid(True)
    plt.savefig(out / "covid19_delta.png", dpi=150, bbox_inches="tight"); plt.show()

if __name__ == "__main__":
    main()
