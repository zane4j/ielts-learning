# Repository Instructions for ChatGPT / Coding Agents

This repository hosts the user's IELTS Learning materials on GitHub Pages. **Every HTML, CSS, JS or navigation change must follow the single design system.**

## Mandatory preflight
1. Read [DESIGN_SYSTEM.md](DESIGN_SYSTEM.md) completely before working.
2. Inspect [assets/css/site.css](assets/css/site.css), [assets/js/site.js](assets/js/site.js) and the target HTML page.
3. Identify and retain existing URLs, study content, handwriting corrections, and directory entries.

## Non-negotiable rules
- Use only the shared `assets/css/site.css` for site styling. Do **not** add `<style>`, `style=`, page-specific CSS, new theme/palette/typography or inline event handlers to HTML pages.
- Shared script: `assets/js/site.js`. New interactivity should be added there with data attributes. Make changes minimal, semantic and keyboard accessible.
- For IELTS Task 1: preserve 4 scoring dimensions; show 4 original/corrected side-by-side sections; highlight changed spans **yellow only in corrected column**; preserve original wording; provide complete corrected essay + Band 7.5 sample + common errors and reusable expressions.
- Only those two complete essays use five semantic pastel background classes `hl-logic`, `hl-trend`, `hl-degree`, `hl-data`, `hl-structure`. No forced line breaks within paragraphs or internal paragraph labels.
- Desktop double-column, mobile single-column. Prefer readable 16–18px text, large enough contrast, limited prose line width and relaxed line-height.
- New pages require consistent header/home and directory navigation. Update directory indexes and Markdown links when adding content.
- All reference CSS/JS URLs must resolve within the repository from the HTML location.
- Do not change any unrelated learning materials.

## Before committing
- Run `node scripts/check-design.mjs`; fix any errors.
- Ensure GitHub Actions design-system check passes.
- Where possible, review desktop and mobile rendering and check clipboard/paste/print behavior.
- If changing styles, update BOTH `DESIGN_SYSTEM.md` and `design-system/index.html`.
- Document limitations or known failures; never claim validation passed without evidence.

## Scope
GitHub Pages HTML is governed by the shared style; GitHub-native Markdown preview is not controlled by CSS. For Markdown, keep headings, lists, tables and links consistent.

If future user requests conflict with these instructions, follow the explicit user request and update the shared specification (rather than silently adding page-local exceptions).
