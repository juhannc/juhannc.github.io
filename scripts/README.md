# scripts/

Utility scripts for the Academic Pages template.

## `make-og-image.py`

Generates the default Open Graph / social preview image at
`images/og-image.png` (1200x630 PNG) used by `_includes/seo.html` when a page
does not define its own header image.

```
python3 scripts/make-og-image.py
```

Requirements:

- Python 3 with [Pillow](https://python-pillow.org) (`pip install Pillow`)
- A TrueType font; defaults to DejaVu Sans (`/usr/share/fonts/truetype/dejavu`),
  override with the `FONT_DIR` environment variable
- The site favicon at `images/favicon-512x512.png` (already in the template);
  it is composited as the card logo

The output is byte-reproducible for a given Pillow/font version and is committed
to the repo, so the build itself does not need Pillow.

## `export_citations.py`

Updates `_data/citations.json` from the source BibLaTeX library, selecting only
entries referenced by `bibkey` in `_publications/`. Both citation formats are
committed, so normal Jekyll builds do not need Python or access to the library.
Private fields such as local file paths, groups, notes, and abstracts are omitted.

```sh
python -m pip install -r scripts/requirements-citations.txt
python scripts/export_citations.py /path/to/literature.bib
python -m unittest discover -s tests -v
```

BibLaTeX retains the source entry types and modern fields. Traditional BibTeX
uses `year`/`month`, `journal`, and `school`; theses use `@mastersthesis` or
`@phdthesis`, while online works and software use `@misc`. Publication status
and software versions are retained in the BibTeX `note` field. Titles retain their source text without an added capitalization-protection
brace layer. Existing source braces, including those used for accented names,
are preserved.
