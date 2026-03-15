"""Project 3 — Simulate tumor growth for D = 0, 45, 60."""
import matplotlib.pyplot as plt
from pathlib import Path
from tumor_ode import simulate_tumor_growth

def main():
    t, w0 = simulate_tumor_growth(0, t_span=(0, 40))
    _, w45 = simulate_tumor_growth(45, t_span=(0, 40))
    _, w60 = simulate_tumor_growth(60, t_span=(0, 40))
    plt.figure(figsize=(8, 5))
    plt.plot(t, w0, label="D=0"); plt.plot(t, w45, label="D=45"); plt.plot(t, w60, label="D=60")
    plt.xlabel("time"); plt.ylabel("tumor weight"); plt.legend(); plt.grid(True)
    plt.title("Project 3 — Tumor growth")
    out = Path(__file__).parent / "output"
    out.mkdir(exist_ok=True)
    plt.savefig(out / "tumor_growth.png", dpi=150, bbox_inches="tight")
    plt.show()

if __name__ == "__main__":
    main()
