# Expanded website CV and LLM profile

**Goal:** Keep the CV design while presenting a fuller career history than the concise resume PDF. Remove the award from web content and enrich the LLM-readable profile with supported skills and experience.

**Sources:** Current Resume.tex, the longer CV.tex, the original website CV in commit fbaeedb, and current publication metadata. Use the current resume for current role/PhD and language proficiency; use the longer CV and original site for earlier experience. Distinguish the Berkeley visiting appointment from the thesis period and earlier TUHH doctoral research from the current Bochum PhD. Keep the PDF unchanged.

- [x] Restore Airbus working-student work, Berkeley research, the REXUS/BEXUS experiment, undergraduate robotics research, the Airbus internship, and teaching.
- [x] Expand education, contextual technical skills, and project leadership while keeping the existing visual structure.
- [x] Remove the award block, dead award styles, and LLM-profile award references.
- [x] Expand llms.txt with career history, research focus, skills in context, and qualifications.
- [x] Verify rendered content, source fidelity, PDF identity, mobile/desktop layout, dark mode, and build.

**Verification:** Production Jekyll build passed. Rendered CV and llms.txt include the restored roles and contextual skills, omit the award, and retain canonical links and forthcoming research status. Browser checks passed at 320, 390, 768, 1024, and 1440 pixels, with seven experience entries, two teaching roles, four selected publications, no horizontal overflow, working dark mode, and no JavaScript errors. PDF bytes remain unchanged. Independent source-fidelity review found no material issues.
