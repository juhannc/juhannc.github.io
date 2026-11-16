# Johann Christensen’s Website

Personal research website at https://www.chrstnsn.de, built as static HTML with Python/Jinja, local CSS, and small JavaScript enhancements. GitHub Actions builds and deploys to GitHub Pages when `master` changes.

## Build and Preview

Python 3.13:

```sh
python -m venv .venv
.venv/bin/python -m pip install -r website/requirements.txt
.venv/bin/python website/build.py --output _site
.venv/bin/python website/check.py _site
.venv/bin/python -m http.server 4173 --directory _site --bind 127.0.0.1
```

Open http://127.0.0.1:4173/. Run regression checks with `.venv/bin/python -m unittest discover -s tests -v`.

## Editing Content

- `website/templates/`: page layouts and shared publication/reviewing components.
- `website/assets/`: CSS, interaction scripts, and organization logos (with source attribution).
- `_publications/`: canonical publication metadata, short summaries, abstracts, links, and status. `handouturl` adds a Talk Handout action on the paper and publication cards.
- `_data/citations.json`: public BibLaTeX and BibTeX citations. Regenerate from the reference library with `python scripts/export_citations.py /path/to/literature.bib`.
- `_pages/cv.md`: curated career, education, skills, and teaching sections. The production builder extracts these sections; selected publications and reviewing/supervision panels use shared templates and canonical data.
- `_data/service.yml`: peer reviewing. `_data/academic_service.yml`: conference service and recognition.
- `_config.yml`: identity/profile links used in the LLM profile. `llms.txt`: detailed machine-readable profile (source with a few legacy Liquid substitutions handled by the builder).
- `files/`: resume and conference handout PDFs. `Johann_Christensen_Headshot.jpg`: exact full-resolution headshot, available at the domain root.
- `CNAME`: canonical domain, copied into the published artifact. The build also emits `.nojekyll`, canonical metadata, structured profile data, sitemap, robots.txt, and legacy URL redirects.

The old Academic Pages/Jekyll layouts and styles are retained as historical source for now. They are not built, installed, or published by the production workflow. Only explicitly selected static assets and generated pages enter `_site`; no local bibliography, resume source, presentation source, speaker notes, or repository files are published.

## Conference Handouts

The DASC 2024 SafetyNet and ICTAI 2024 pyCASX handouts are hosted locally beside their papers. They were taken from the author's presentation release `release/c900ec6`. Broader internal/status presentations and speaker-note versions are not included. Add a handout to a publication only after its content is matched to that paper.
