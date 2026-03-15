# MATH209 — Mathematical Modeling of Biological Systems

Coursework from **Quantitative Biology & Systems Modeling**, organized by project. Each project is self-contained with code (where applicable), figures, and report PDFs.

## Repository structure

| Folder | Contents |
|--------|----------|
| **`github-codebase/`** | Seven projects (1–7): Python code, scripts, and generated figures. See [github-codebase/README.md](github-codebase/README.md) for project list and run instructions. |
| **`showcase-website/`** | Single-page site that displays project figures. Open `index.html` or run `python3 -m http.server 8080` inside it. |
| **`project1.pdf`–`project7.pdf`** | Report PDFs for each project (at repo root). |

## Projects (in `github-codebase/`)

| Project | Topic |
|---------|--------|
| 1 — Regression | Linear, quadratic, exponential fits; R² |
| 2 — Flux balance analysis | Metabolic networks, biomass maximization |
| 3 — Tumor growth ODE | Tumor weight + drug PK, Runge–Kutta |
| 4 — COVID-19 model | S/E/A/I/H/R/D epidemic dynamics, R₀, interventions |
| 5 — Tumor microenvironment | Effector T cells, macrophages, spatial R2 |
| 6 & 7 | Report PDFs and figures in `outputs/` |

## Figures

- **From code (Projects 1–5):** From repo root, `cd github-codebase && python scripts/generate_figures.py`
- **From PDFs (all 7):** `cd github-codebase && python scripts/extract_figures_from_pdfs.py` (requires [poppler](https://poppler.freedesktop.org/); on macOS: `brew install poppler`). Expects `project1.pdf`–`project7.pdf` in the parent folder (this repo root).

## Setup and run

```bash
pip install -r github-codebase/requirements.txt
cd github-codebase/project1_regression && python run_regression.py
# etc.
```

## License

MIT.
