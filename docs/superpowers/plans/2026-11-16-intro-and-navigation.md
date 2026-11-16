# Intro, CV section navigation, and sitemap

**Goal:** Introduce Johann by first name with his AI expertise, improve navigation through the expanded CV, and remove broken/template entries and blog references from the sitemap.

**Approach:** Update the homepage lead; use ordinary section anchors on the CV so the complete career history stays visible and printable. Replace the generic site.pages/posts sitemap with the main navigation, useful resources, and actual publication collection. Hide the unused blog feed link in the footer and document head.

- [x] Update the homepage lead and add accessible CV section links with heading offsets and print handling.
- [x] Replace the sitemap with a page matching the profile layout, omitting error pages, redirects, assets, and blog scaffolding.
- [x] Hide the unused feed links.
- [x] Verify production build, main text, human/XML sitemap targets, CV anchors, responsive layout, and dark mode.

**Verification:** Jekyll production build and whitespace checks passed. Human and XML sitemap targets resolve to generated content; browser requests to all human sitemap content links returned HTTP 200. All 23 publications remain listed. No blog, 404, redirect-data, or stylesheet entries are shown. Homepage, CV, and sitemap passed browser layout checks at 320, 390, 768, and 1440 pixels. CV section anchors land below the masthead, all content remains visible, dark mode works, and no JavaScript errors occurred. The local preview was restarted to load the feed configuration.
