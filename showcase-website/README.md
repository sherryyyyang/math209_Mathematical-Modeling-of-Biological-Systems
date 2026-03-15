# Showcase website — Quantitative Biology & Systems Modeling

A single-page portfolio for **Sherry Yang** with **all project figures** (Projects 1–5) from the codebase.

## Quick start

1. **Figures are already in the repo** under `assets/project1/` through `assets/project5/`. No setup needed to view the site.

2. **Open the site:** open `index.html` in a browser, or serve the folder:
   ```bash
   cd showcase-website
   python3 -m http.server 8080
   ```
   Then visit `http://localhost:8080`.

## Contents

- **Hero:** Tumor growth figure (Project 3).
- **Project cards (1–5):** One main figure per project, then **all** generated figures:
  - **Scrollable strip** when a project has many figures (5+): vertical scroll within the card.
  - **Panel** when a project has 2–4 figures: small grid.
- **All figures:** Scrollable gallery at the bottom with captions.

## Refreshing figures

Figures are kept in both each project’s `github-codebase/<project>/outputs/` and here in `assets/project1/` … `project5/`. From the repo root run:

```bash
cd github-codebase && python scripts/generate_figures.py
```

That script writes to both the codebase `outputs/` dirs and this folder’s assets. No separate copy step.

## Deployment

Upload the entire `showcase-website` folder (including `assets/project1/`–`assets/project5/`) to GitHub Pages, Netlify, Vercel, or any static host. The GitHub link in the footer points to `sherryyyyang/math209_Mathematical-Modeling-of-Biological-Systems`.
