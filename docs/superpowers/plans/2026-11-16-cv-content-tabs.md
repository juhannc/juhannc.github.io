# CV content tabs

**Goal:** Replace the CV's jump links with actual switching tabs, as explicitly requested, and remove the bachelor's thesis and Airbus internship entries from the CV.

**Approach:** Reuse the six existing navigation categories as progressively enhanced tabs. Keep the hero and PDF download, with one readable content panel at a time; place Languages under Technical skills. Experience is the default. Support arrow/Home/End keys, existing section deep links, complete print output, and visible content without JavaScript. Keep the Airbus working-student role, bachelor’s degree, publication records, and source PDF.

- [x] Establish a failing browser check for six switching CV tabs.
- [x] Restructure the CV into six panels and remove the two requested experience entries.
- [x] Add scoped tab styles and keyboard/deep-link handling, with print and no-JavaScript fallbacks.
- [x] Verify all tabs, retained/removed content, PDF identity, mobile/dark mode, keyboard navigation, deep links, print output, and production build.

**Verification:** The browser test first failed because the old CV had no tabs. After implementation, production build and browser checks passed for six switching panels, five retained experience roles, arrow/Home/End navigation, Education/Languages deep links, 320–1440px layouts, dark mode, and full print/no-JavaScript content. No JavaScript errors. Static checks confirm both requested entries are absent while the working-student role and bachelor’s degree remain; source PDF, publication records, and llms.txt are unchanged. Independent review found no material issues.
