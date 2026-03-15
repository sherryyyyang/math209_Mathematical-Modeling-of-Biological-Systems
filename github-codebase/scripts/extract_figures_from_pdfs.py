"""
Extract figures from project1.pdf through project7.pdf into each project's outputs/ folder.
Use these original report figures when generated figures are wrong or data is missing.
Requires: poppler-utils (pdfimages) on PATH.
"""
import subprocess
import shutil
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
PDF_DIR = REPO.parent  # MATH209 folder with project1.pdf, project2.pdf, ...
TEMP_DIR = REPO / ".pdf_extract_temp"

# Map project number -> (output folder name, optional list of canonical names for first N figures)
PROJECTS = {
    1: ("project1_regression", ["fig_regression.png", "fig_regression_linear.png", "fig_regression_quadratic.png", "fig_regression_exponential.png"]),
    2: ("project2_flux_balance_analysis", ["fig_fba.png"]),
    3: ("project3_tumor_growth_ode", ["fig_tumor_growth.png"]),
    4: ("project4_covid19", ["fig_covid19.png", "fig_covid19_baseline.png", "fig_covid19_delta.png"]),
    5: ("project5_tumor_microenvironment", ["fig_tme.png", "fig_tme_single.png"]),
    6: ("project6", None),
    7: ("project7", None),
}


def min_size_for_figure(width: int, height: int) -> bool:
    """Skip tiny images (banners, icons). Keep plot-sized images."""
    return width >= 200 and height >= 150


def extract_pdf(pdf_path: Path, out_dir: Path, canonical_names: list | None) -> int:
    if not pdf_path.exists():
        print(f"  Skip (not found): {pdf_path.name}")
        return 0
    out_dir.mkdir(parents=True, exist_ok=True)
    prefix = TEMP_DIR / pdf_path.stem
    TEMP_DIR.mkdir(parents=True, exist_ok=True)
    try:
        subprocess.run(
            ["pdfimages", "-png", str(pdf_path), str(prefix)],
            check=True,
            capture_output=True,
            cwd=str(PDF_DIR),
        )
    except FileNotFoundError:
        print("  Error: pdfimages not found. Install poppler-utils (e.g. brew install poppler).")
        return 0
    except subprocess.CalledProcessError as e:
        print(f"  Error running pdfimages: {e}")
        return 0

    # Collect extracted images (pdfimages names them prefix-000.png, prefix-001.png, ...)
    extracted = sorted(prefix.parent.glob(f"{prefix.name}-*.png"))
    if not extracted:
        return 0

    # Optional: get dimensions to skip tiny images (would need PIL or identify)
    kept = []
    for i, f in enumerate(extracted):
        try:
            import struct
            with open(f, "rb") as fp:
                fp.seek(16)
                w, h = struct.unpack(">II", fp.read(8))
            if min_size_for_figure(w, h):
                kept.append(f)
            else:
                f.unlink()
        except Exception:
            kept.append(f)

    count = 0
    for i, src in enumerate(kept):
        fig_name = f"fig_{i+1:02d}.png"
        dst = out_dir / fig_name
        shutil.copy2(src, dst)
        count += 1
        if canonical_names and i < len(canonical_names):
            canonical = out_dir / canonical_names[i]
            shutil.copy2(src, canonical)

    # Clean temp files
    for f in prefix.parent.glob(f"{prefix.name}-*.png"):
        try:
            f.unlink()
        except Exception:
            pass
    return count


def main():
    print("Extracting figures from report PDFs into project outputs/...")
    for num, (folder_name, canonical_names) in PROJECTS.items():
        pdf_path = PDF_DIR / f"project{num}.pdf"
        out_dir = REPO / folder_name / "outputs"
        n = extract_pdf(pdf_path, out_dir, canonical_names)
        print(f"  Project {num} ({folder_name}): {n} figures -> {out_dir}")
    if TEMP_DIR.exists():
        try:
            TEMP_DIR.rmdir()
        except OSError:
            pass
    print("Done.")


if __name__ == "__main__":
    main()
