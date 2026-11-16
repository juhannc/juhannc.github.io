# Profile pages refresh

**Goal:** Apply the approved CV design direction to the homepage and publications while retaining the profile sidebar; remove unused template content and provide an LLM-readable profile.

**Approach:** A shared profile layout and CSS use the CV's typography, spacing, rules, and theme colors. Reuse the existing author sidebar and publication data. Compact publication entries link to full citations on unchanged detail-page URLs. Keep publication status explicit and sort by metadata date.

- [x] Create the shared profile layout and publication entry include; restyle homepage and publication index.
- [x] Add `/llms.txt` with profile facts, primary pages, identity aliases, and generated selected research/status links; advertise it in the document head.
- [x] Remove unused template demo content and tooling; retain personal content, PDFs, build configuration, and shared theme dependencies. Replace template README with site-specific instructions.
- [x] Build and verify rendered text, sidebar layout, mobile navigation, dark mode, publication links/order, cleanup, and LLM profile output.

**Verification:** Production Jekyll build passed. Browser checks passed for homepage and publications at 320, 390, 768, 1023, 1024, and 1440 pixels; sidebar has no desktop overlap, mobile menus and dark mode work, 23 publications remain present, and no JavaScript errors occurred. All generated internal page and asset links resolve; canonical llms.txt contains rendered metadata and the correct forthcoming status. All three PDFs are unchanged. Corrected a pre-existing slides URL typo. Used relative URLs for core CSS and JavaScript to avoid preview hostname/CORS problems. Independent review found no material issues. Upstream Sass deprecation warnings remain.
