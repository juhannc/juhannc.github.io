# CV profile layout and education cleanup

**Goal:** Share the publications page's profile sidebar on the CV; restore a rounded rectangular portrait; update the sidebar bio and remove XING; simplify CV tabs and education.

**Approach:** Nest the CV layout inside the shared profile layout, preserving accessible content-switching tabs, print output, and no-JavaScript fallback. Use five tabs, with languages under Skills. Education entries follow title → institution → dates, with the Berkeley thesis nested as an M.Sc. component. Change the earlier research heading to External Researcher · Reinforcement Learning, and retain a single unqualified TUHH institution line. Drop the Leadership panel and B.Sc. from the web CV. Keep source PDFs and publication records intact.

- [x] Establish a failing browser check for the shared sidebar, five tabs, and education structure.
- [x] Update the CV layout and content, shared portrait styling, and sidebar configuration.
- [x] Verify source content, production build, CV tabs and education, all shared sidebars, 320–1440px layouts, dark mode, print/no-JS behavior, and PDF identity.

**Verification:** The initial browser check failed because the CV lacked the profile sidebar. Production build/static checks then passed for the shared sidebar, five tabs, updated education and global bio, XING removal, and unchanged PDF. Browser checks passed at 320, 390, 768, 1024, and 1440 pixels on homepage/publications/CV, verifying natural portrait aspect ratio, rounded-rectangle shape, no horizontal overflow or desktop sidebar overlap, all five switching tabs, keyboard behavior, languages, dark mode, complete print output, and no-JavaScript fallback. No JavaScript errors. The browser run skipped the unrelated external MathJax download after an external-load timeout. Independent review found no material issues.
