# PDF Generator

## Description
A compact Python tool that generates structured PDF pages from a CSV of topics and per-topic page counts. For each topic, the script creates one or more A4 pages containing:

- a bold header displaying the topic name,
- a grid of horizontal ruled lines for writing,
- a footer with the topic name aligned to the right.

The project focuses on predictable layout generation using simple primitives and a CSV-driven workflow. Content and structure remain separated, making the generator easy to extend or adapt for other document formats.

Key files: [main.py](main.py), [topics.csv](topics.csv), [output.pdf](output.pdf).

---

## Interesting techniques & references

### Page layout using coordinate positioning
The script constructs page content using explicit positioning and measurements. Horizontal lines are drawn using coordinate math to create a consistent ruled layout across pages. This approach provides deterministic layout control without relying on HTML rendering engines.

---

### Direct PDF primitives with FPDF
The generator uses FPDF primitives such as page creation, text cells, and vector lines to build the document structure programmatically.

FPDF documentation:  
https://py-pdf.github.io/fpdf2/Tutorial.html  
https://www.fpdf.org/en/doc/index.php

---

### Explicit page break control
Automatic page breaking is disabled using:

```python
set_auto_page_break(auto=False, margin=0)
```

This allows manual control over margins and ensures identical spacing across all generated pages.

---

### CSV-driven content model
Topics and page counts are read from [`topics.csv`](topics.csv) using `pandas.read_csv()`. This separates document content from layout logic and allows bulk generation driven by spreadsheet data.

Pandas documentation:  
https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html

---

### Procedural template pattern
Each page follows a repeatable structure:

- header
- ruled lines
- footer

The template is implemented using loops and consistent spacing rules, making it easy to adjust layout parameters or introduce additional elements such as page numbers or branding.

---

### Font and style control
Fonts and styles are applied through the FPDF API using built-in fonts (`Times`) and style flags for headers and footers. This demonstrates lightweight typographic control without external rendering dependencies.

---

## Non-obvious technologies & libraries

### FPDF / fpdf2
A lightweight, pure-Python PDF generation library that provides direct control over layout primitives such as text placement and vector drawing.

- Project: https://pypi.org/project/fpdf/
- Documentation: https://py-pdf.github.io/fpdf2/

This approach avoids browser-based rendering while maintaining precise output control.

---

### Pandas
Used as a robust CSV reader to simplify parsing and iteration over structured topic data.

Documentation:  
https://pandas.pydata.org/docs/

---

## External libraries & assets

- **fpdf / fpdf2** — PDF generation primitives  
  https://py-pdf.github.io/fpdf2/  
  https://pypi.org/project/fpdf/

- **pandas** — CSV parsing and data handling  
  https://pandas.pydata.org/

### Fonts
The script uses the built-in `Times` font family (Times / Times New Roman).

Reference:  
https://en.wikipedia.org/wiki/Times_New_Roman

If portability across systems is required, fonts can be embedded using FPDF’s `AddFont` functionality.

---

## Project structure (directories only)

```
/
```

### Notes
The repository is intentionally minimal and keeps scripts and data in the root directory:

- `main.py` — core PDF generation logic
- `topics.csv` — input data defining topics and page counts
- `output.pdf` — example generated output
- `README.md`, `.gitignore` — project metadata

If the project expands, consider introducing:

- `assets/` — embedded fonts, logos, or images
- `templates/` — alternate page layouts or configuration files
- `docs/` — design notes and extended documentation

---

## Files to review

- [`main.py`](main.py) — PDF generation logic and layout construction
- [`topics.csv`](topics.csv) — input dataset
- [`output.pdf`](output.pdf) — generated example output

---
