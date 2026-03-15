# MATH209 — Mathematical Modeling of Biological Systems

Coursework from **Quantitative Biology & Systems Modeling**, organized by project. Each project is self-contained with code (where applicable), figures, and report PDFs.

## Repository structure

| Folder | Contents |
|--------|----------|
| **`github-codebase/`** | Seven projects (1–7): Python code, scripts, and generated figures. See [github-codebase/README.md](github-codebase/README.md) for project list and run instructions. |
| **`showcase-website/`** | Single-page site that displays project figures. Open `index.html` or run `python3 -m http.server 8080` inside it. |
| **Project 6 & 7 PDFs** | In `github-codebase/project6/project6.pdf` and `github-codebase/project7/project7.pdf`. Project 1–5 report PDFs are not in the repo. |

## Projects (in `github-codebase/`)

| Project | Topic |
|---------|--------|
| 1 — Regression | Linear, quadratic, exponential fits; R² |
| 2 — Flux balance analysis | Metabolic networks, biomass maximization |
| 3 — Tumor growth ODE | Tumor weight + drug PK, Runge–Kutta |
| 4 — COVID-19 model | S/E/A/I/H/R/D epidemic dynamics, R₀, interventions |
| 5 — Tumor microenvironment | Effector T cells, macrophages, spatial R2 |
| 6 & 7 | Report PDF only in each project folder (no `outputs/`). |

## Figures

- **From code (Projects 1–5):** `cd github-codebase && python scripts/generate_figures.py`
- **From PDFs (Projects 1–5 only, if you have the PDFs locally):** `cd github-codebase && python scripts/extract_figures_from_pdfs.py` (requires [poppler](https://poppler.freedesktop.org/); on macOS: `brew install poppler`). Expects `project1.pdf`–`project5.pdf` in the parent folder; those PDFs are not published in this repo.

## Setup and run

```bash
pip install -r github-codebase/requirements.txt
cd github-codebase/project1_regression && python run_regression.py
# etc.
```

## License

MIT.
