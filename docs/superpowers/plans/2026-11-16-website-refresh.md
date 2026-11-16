# Website refresh implementation plan

**Goal:** Refresh the existing Academic Pages website from upstream, the local bibliography, and the current resume.

**Architecture:** Keep Jekyll and the upstream theme. Preserve personal content and stable publication URLs. Render the CV with semantic HTML and theme-aware responsive CSS; keep the PDF at its existing URL.

**Sources:** `/home/johann/Obsidian/References/Literature/literature.bib`; `/home/johann/Documents/Arbeit/Bewerbungen/Resume.tex` and `Resume.pdf`.

- [x] Merge Academic Pages commit `94c90b9`, preserving personalized settings and deleted template examples.
- [x] Update Ruby and npm dependencies, retain lockfiles, rebuild JavaScript, and align the deployment workflow with the locked build.
- [x] Reconcile authored publications (including the former name Lange), add short original summaries and an overview, preserve existing supervised theses, and label forthcoming work accurately.
- [x] Replace the CV content with current resume information, style experience/education and skill groups for desktop, mobile, dark mode, and print, and replace `files/CV.pdf` byte for byte.
- [x] Build Jekyll and JavaScript; inspect generated pages, publication coverage and links, PDF identity, responsive layout, and merge state.

**Review focus:** Personal settings must survive the merge; no dummy publications; no duplicate article URLs; future work must not be labeled published; CV download must retain the old URL; no private bibliography metadata may enter public output.

**Verification:** Jekyll 4.4.1 build and JavaScript build passed. npm audit reported zero vulnerabilities. Browser checks passed at 320, 390, 768, and 1440 pixels, with working dark-mode toggle and no JavaScript errors. Content checks verified 21 bibliography entries plus two supervised theses, unique publication URLs, all 13 existing URLs retained, and identical source/destination PDF bytes. Upstream Sass emits deprecation warnings.
