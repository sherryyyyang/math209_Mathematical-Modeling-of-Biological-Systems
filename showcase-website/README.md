# Showcase website — Quantitative Biology & Systems Modeling

A single-page portfolio for **Sherry Yang** with **all project figures** from the codebase displayed on the site.

## Quick start

1. **Generate figures** (required so the site has images to show):
   ```bash
   cd github-codebase
   python scripts/generate_figures.py
   ```
   This writes figures into `showcase-website/assets/` (and `github-codebase/outputs/`).

2. **Open the site:** open `index.html` in a browser, or serve the folder:
   ```bash
   cd showcase-website
   python3 -m http.server 8080
   ```
   Then visit `http://localhost:8080`.

## Contents

- **Hero:** Tumor growth figure (Project 3).
- **Project cards:** One main figure per project, plus extra panels where relevant (e.g. regression linear/quad/exp, COVID baseline & delta, TME single & R2 comparison).
- **All figures:** Gallery at the bottom showing every generated figure with captions.

## Customization

- **GitHub link:** Edit the footer `<a href="https://github.com">` to your repo.
- **Regenerate figures:** Run `python scripts/generate_figures.py` from `github-codebase` anytime; figures are saved into `showcase-website/assets/` automatically.

## Deployment

Upload the entire `showcase-website` folder (including `assets/` with the PNGs) to GitHub Pages, Netlify, Vercel, or any static host.
