# Production Website

The approved November 2026 redesign is the main website implementation. See the repository README for content editing, build, preview, and deployment instructions.

`build.py` renders static pages from canonical publication data and the curated CV. `check.py` audits local links, fragment targets, duplicate IDs, unrendered template tokens outside citations, and exact resume/headshot copies. The GitHub Pages workflow runs this audit and the regression tests before deployment.

Both themes use local fonts/assets only. Search, filters, citation copy controls, and tabs are progressive enhancements. All publications and CV sections stay readable without JavaScript. Printing expands every CV section.
