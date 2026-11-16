# Website Redesign PoC

The user explicitly requested a new design PoC for review, on desktop and mobile, with no push or publication. Treat this as a reviewable prototype, not an approved production migration.

Use a distinct warm off-white/navy/orange design with generous space, strong typographic hierarchy, a compact identity sidebar, and consistent navigation: Overview, Research, CV, Service. Keep a naturally proportioned rounded-rectangle portrait, the AI expert bio, first-name introduction, no XING, Title Case headings, and a prominent resume download. Provide a dark theme and an effective mobile navigation.

Research should be discoverable through search, category/year filters, selected work, and complete detail pages retaining human citations plus switchable BibLaTeX/BibTeX. Distinguish accepted/forthcoming work, supervised work, and authored publications. No software publications. The CV keeps the current curated history and content-switching tabs; do not restore previously removed CV entries or the best-session paper award. Add the explicitly requested 2026 reviewing activities and ICML Silver Reviewer Award, plus Mina Randolf's supervised thesis from literature.bib.

Implement as a standalone static site generated from existing repository content, using Jinja templates, local CSS, and small dependency-free browser scripts. This provides a full working PoC without changing the production stack or requiring framework maintenance. The live site's local preview stays on port 4000; the new PoC uses port 4173. Preserve the custom domain's source and existing PDFs/headshot bytes. No push.

The homepage should explain the research and connect it to concrete publications, career background, mentoring, and service. Give every publication its own page. Include a useful sitemap, LLM profile, accessible states, print/no-JavaScript fallbacks, and no empty controls. Validate navigation, filtering, citations, all data coverage, responsive layouts, keyboard behavior, dark mode, and source privacy before handoff.

## Follow-Up Approval

The user approved the preview and requested switching the main website to this variant, with landing-page organization logos, handouts, additional academic service, and publication cards in the CV. The production implementation is now in `website/`; the migration plan records the follow-up scope. The earlier no-push instruction applied to the PoC review stage and is superseded by the instruction to switch to the approved design.
