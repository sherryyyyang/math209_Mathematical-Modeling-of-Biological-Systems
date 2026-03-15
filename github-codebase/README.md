# Quantitative Biology & Systems Modeling — Sherry Yang

Coursework from a quantitative/systems biology class, organized **by project**. Each folder is a separate, self-contained project you can run and showcase independently.

## Projects

| Project | Topic | Key methods |
|---------|--------|-------------|
| [**Project 1** — Regression](project1_regression/) | Linear, quadratic, exponential fits; R² | Least squares, model selection |
| [**Project 2** — Flux balance analysis](project2_flux_balance_analysis/) | Metabolic networks, maximize biomass | Linear programming, stoichiometric matrix S·v = 0 |
| [**Project 3** — Tumor growth ODE](project3_tumor_growth_ode/) | Tumor weight + drug PK | Runge–Kutta, multi-compartment ODEs |
| [**Project 4** — COVID-19 model](project4_covid19/) | S, E, A, I, H, R, D epidemic dynamics | ODE integration, R₀, intervention (δ) |
| [**Project 5** — Tumor microenvironment](project5_tumor_microenvironment/) | Effector T cells, macrophages, spatial R2 | Parameterized geometry, visualization |
| [**Project 6**](project6/) | Report PDF only (no code in repo) | `project6.pdf` in folder |
| [**Project 7**](project7/) | Report PDF only (no code in repo) | `project7.pdf` in folder |

## Repository structure

```
├── README.md
├── requirements.txt
├── project1_regression/
│   └── outputs/          # figures (same set as ../showcase-website/assets/project1/)
├── project2_flux_balance_analysis/
│   └── outputs/
├── project3_tumor_growth_ode/
│   └── outputs/
├── project4_covid19/
│   └── outputs/
├── project5_tumor_microenvironment/
│   └── outputs/
├── project6/
│   └── project6.pdf      # report only (no outputs/)
├── project7/
│   └── project7.pdf      # report only (no outputs/)
└── scripts/
    ├── generate_figures.py      # regenerate from code (Projects 1–5)
    └── extract_figures_from_pdfs.py  # extract from PDFs (Projects 1–5; PDFs not in repo)
```

**Figures:** Figures are kept in both **`<project>/outputs/`** and **`../showcase-website/assets/project1/` … `project5/`**. Run:
```bash
python scripts/generate_figures.py
```
That writes to each project’s `outputs/` and to the showcase assets. For PDF extraction, run `extract_figures_from_pdfs.py` (expects `project1.pdf`–`project5.pdf` in parent folder). Requires `poppler-utils` (e.g. `brew install poppler`).


## Setup and run

```bash
pip install -r requirements.txt
cd project1_regression && python run_regression.py
# etc.
```

## License

MIT.
