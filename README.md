# Johann Christensen’s website

Personal research website at [chrstnsn.de](https://www.chrstnsn.de), built with Jekyll and the [Academic Pages](https://github.com/academicpages/academicpages.github.io) theme.

## Local preview

Use Ruby 3.4, Bundler 2.7, and Node.js 22 or newer:

```sh
bundle install
npm ci
npm run build:js
bundle exec jekyll serve --config _config.yml,_config_local.yml
```

Open http://127.0.0.1:4000. The local configuration ensures that styles and scripts load from your local build.

## Content

- `_pages/about.md`: homepage.
- `_pages/publications.html`: publication index, grouped by category and sorted newest first.
- `_data/citations.json`: generated BibLaTeX and traditional BibTeX snippets for each publication’s citation tabs; regenerate with `scripts/export_citations.py` (see `scripts/README.md`).
- `_publications/`: publication metadata, short summaries, abstracts, and citations. Keep existing permalinks when updating entries. Label accepted and forthcoming work explicitly.
- `_pages/cv.md`: CV, with selected publications drawn from the publication collection by `bibkey`.
- `files/CV.pdf`: downloadable resume; keep this URL stable.
- `llms.txt`: concise profile for language models; selected research links and status labels are generated from the same publication metadata.
- `_config.yml` and `_data/navigation.yml`: profile information, site settings, and navigation.
- `assets/css/profile.css` and `assets/css/resume.css`: custom page styles using the active theme’s colors.

The homepage, publications, sitemap, and CV share `_layouts/profile.html` and retain the author sidebar. Individual papers retain their citations and existing URLs. The CV adds `_layouts/resume.html` for its content styles and accessible section tabs.

Template demo posts, talks, teaching pages, sample images, notebook generators, and talk-map tooling have been removed. Shared theme layouts, includes, and assets remain available for the site and future upstream updates.

## Build and deployment

```sh
npm run build:js
bundle exec jekyll build
```

The GitHub Actions workflow in `.github/workflows/jekyll.yml` builds and deploys pushes to `master` with the committed Ruby and npm lockfiles. No Python tooling is required to build the site.
