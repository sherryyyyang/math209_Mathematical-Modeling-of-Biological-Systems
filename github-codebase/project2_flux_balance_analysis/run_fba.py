"""Project 2 — Run FBA: baseline and knockouts."""
from fba import simple_network, fba_maximize_flux

def main():
    S, lb, ub = simple_network()
    opt, _ = fba_maximize_flux(S, lb, ub, 7)
    ub4 = ub.copy(); ub4[3] = 0
    opt4, _ = fba_maximize_flux(S, lb, ub4, 7)
    ub3 = ub.copy(); ub3[2] = 0
    opt3, _ = fba_maximize_flux(S, lb, ub3, 7)
    print("Project 2 — Baseline:", round(opt, 6), "Knockout v4:", round(opt4, 6), "Knockout v3:", round(opt3, 6))

if __name__ == "__main__":
    main()
