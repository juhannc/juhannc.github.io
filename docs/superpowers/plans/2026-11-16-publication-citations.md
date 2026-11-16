# Publication citation tabs

**Goal:** Every publication detail page offers source-based BibLaTeX and traditional BibTeX citations in compact switchable tabs.

**Approach:** Export only public bibliographic fields from the local library into committed Jekyll data. A progressive-enhancement component renders both citations without JavaScript; with JavaScript it provides accessible tabs, keyboard navigation, and copying. Keep existing publication URLs and descriptions. No publishing requested: changes remain local with the preview available.

- [x] Test journal/date conversion, thesis types, software/status preservation, field filtering, and round-trip parsing before implementing the exporter.
- [x] Export both formats for all 23 works, including the two supervised theses.
- [x] Add the tab component, scoped styles, copy action, and optional maintenance documentation.
- [x] Validate source coverage, parsing, traditional BibTeX compilation, production build, browser interactions, clipboard, keyboard use, mobile/dark mode, and no-JavaScript fallback.

**Verification:** Four exporter unit tests pass. All 46 generated snippets round-trip and match source authors and conference titles; private fields are absent. Traditional BibTeX processes all 23 entries with plain.bst without warnings. The production Jekyll build includes the citation widget on all 23 pages. Browser checks verified exact text, switching, arrow/Home/End keys, clipboard content, clipboard-denied fallback, 320–1440px layouts, dark mode, and JavaScript-disabled rendering, with no JavaScript errors. Independent review found no material issues. GitHub master remains at fbaeedb: the work is only in the local preview.
