# IELTS Learning · Design System v1.0

> All current and future GitHub Pages HTML must follow this specification. The actual CSS source of truth is `assets/css/site.css`. Visual examples: https://zane4j.github.io/ielts-learning/design-system/

## Purpose

This is a **reading-first** site for IELTS speaking notes, writing reviews and annotated essays. Optimize for long-form readability, not dashboard density or decoration. Keep one consistent design language for all site pages.

## Required files and layout

- Shared CSS: `assets/css/site.css`
- Shared interactions: `assets/js/site.js`
- Design examples: `design-system/index.html`
- New page starter: `templates/page.html.example`
- Validation: `scripts/check-design.mjs`
- CI enforcement: `.github/workflows/design-system-check.yml`

Every HTML page must reference the shared CSS and JS with **working relative paths**, contain `lang="zh-CN"` (or the actual dominant page language), a `viewport` meta tag, exactly one `<h1>`, and a `<main>`. HTML pages must not define page-specific `<style>` blocks, `style="..."` attributes or style-related event handlers. Add reusable rules to the shared stylesheet instead. Inline highlighting must use documented semantic CSS classes.

## Visual foundations

- Background: `--color-page: #f7f8fa`; surfaces: `--color-surface: #ffffff`.
- Main text: `--color-text: #243247`; headings: `--color-text-strong: #172438`; secondary text: `--color-muted: #53647a`.
- Links and primary action: `--color-link: #225588`, `--color-brand: #224b74`.
- Borders: `--color-border: #dce3eb`; use thin borders and very subtle shadows.
- Font: system sans-serif for UI/CN explanation; Georgia/Times-style serif fallback for full English essay reading.
- Default body: 16px, line-height 1.75; IELTS essay: approximately 17.5px, line-height 1.98.
- Comfortable long-form line width: `max-width: 69ch`; page container up to `70rem` for comparison/table layout.
- H1: 26–38px, H2: 21–25px, logical heading levels.
- Spacing: use shared `--space-*` tokens, not arbitrary custom values. Maintain paragraph breaks; do not insert manual line breaks inside a natural paragraph.
- Focus ring visible to keyboard users; honor reduced motion. Target WCAG 2.2 AA text contrast (4.5:1 normal, 3:1 large). Test browser zoom and mobile layout.
- Use calm white card surfaces; avoid loud saturated gradients and badge-heavy designs.

## Semantic highlighting

**In side-by-side original-versus-correction comparisons:** highlight only the changed portion in the *corrected* column using `<mark class="diff">` (soft yellow `#fff0b3`). Never modify the user's original in the left column.

**Only in complete corrected essays and Band 7.5 model essays:** use five soft background categories with deep text:
- `hl-logic`: pale red `#fce2e2`, bold + underline: connectors
- `hl-trend`: pale blue `#deecff`, bold: changes and trend verbs
- `hl-degree`: pale orange `#fff0c9`, bold: degree adverbs
- `hl-data`: pale green `#e2f3dd`, underline: data, ranges, comparisons
- `hl-structure`: pale purple `#f1e2ff`, bold + underline: reusable grammar/complex syntax

Never convey meaning by color alone: labels, boldness and underlining distinguish categories. Do not stack conflicting color classes on the same span.

## IELTS Task 1 review page structure (required)

1. Four-dimensional assessment (TA / CC / LR / GRA) and overall estimate.
2. Four side-by-side sections: Introduction / Overview / Body 1 / Body 2, **original left, minimally corrected right**, actual changes yellow, short explanation below each.
3. Complete corrected essay with four natural paragraphs, **no P1/P2/Intro/Body labels within the essay**, five background highlights, re-score.
4. Band 7.5 model answer, same four-paragraph reading format and five highlights.
5. Error patterns, reusable expressions and optionally data verification. Never confuse percentage and percentage points.

Use `.compare-section`, `.compare-grid`, `.paper.original`, `.paper.revised`, `.annotation`, `.essay-card`, `.score` from shared CSS. Desktop dual columns; under 850px stack into one column. The full essay must not add artificial line breaks inside paragraphs.

## UX navigation and interactions

- Every new page must have a path back to its directory and the site home.
- Keep the home/directory indexes updated: `index.html` for the site, `writing/index.html`, `writing/task1/index.html`, as applicable.
- Keep `README.md` as a **single stable link to the GitHub Pages HTML homepage** (`https://zane4j.github.io/ielts-learning/`). Maintain all directory navigation in HTML indexes only. Do not maintain parallel Markdown catalogs. Preserve existing Markdown study notes without deleting or migrating them unless specifically requested.
- Use shared JS controls with `data-copy="id"`, `data-action="toggle-highlight"`, `data-action="toggle-size"`, `data-action="print"` rather than inline JS. Rich-copy attempts HTML + plain text but Feishu may still handle pasting differently.
- Links must have readable labels, keyboard operation must work, and printing should preserve background highlighters where supported.

## How ChatGPT / other code agents must work

1. **Read `AGENTS.md` and this file before changing or adding a page.**
2. Read relevant existing pages and shared CSS before editing; preserve original user writing and existing links.
3. Make semantic, minimal changes. Never copy/paste independent CSS into HTML or override styles per page.
4. If a new component/token is genuinely necessary, update shared CSS, document it here, and update `design-system/index.html` with a visible example.
5. When adding or removing content, update the correct **HTML directory index only** (and any relevant HTML back-navigation). Do not append or sync individual study entries into README or Markdown directory files.
6. Run `node scripts/check-design.mjs` and address failures **before** committing.
7. Confirm the site at https://zane4j.github.io/ielts-learning/ and test the relevant subpage navigation and mobile reading (manual check or browser test).
8. If automatic validation reports failure, do not describe the page as fully compliant.
9. Preserve users' data; do not overwrite unrelated speaking/IELTS files.

## Enforcement and limitations

`scripts/check-design.mjs` is automatically run via GitHub Actions for every push and PR. It covers enforceable HTML structure, shared asset usage, relative asset validity, styling violations, and navigation files. It does **not** prove full WCAG compliance, visual quality, or correct reading flow. For stronger enforcement, repository admin should enable **branch protection/ruleset** on `main` requiring the design check to pass before merging (and restrict direct pushes). Without that rule, GitHub can report a failure but cannot block all pushes.

**Note:** GitHub's native rendering of `.md` files uses GitHub's styles and cannot load this site's CSS. The design system applies to HTML pages served on GitHub Pages. The existing Markdown study notes remain as historical/source resources; the HTML homepage and HTML indexes are the **only navigational source of truth**. The root README is just a pointer to the HTML homepage.

## References

- W3C WCAG 2.2 (Contrast Minimum): https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html
- USWDS Typography: https://designsystem.digital.gov/components/typography/
- GitHub Primer Typography: https://primer.style/foundations/typography
- GOV.UK Design System Layout: https://design-system.service.gov.uk/styles/layout/

## Speaking Part 2 · Zoe 人物模板与关键词（2026-11）

- 人物模板、使用说明：`speaking/part2/people/zoe-template.html`；目录：`speaking/part2/people/index.html`；16 道题均有独立 HTML 页面。
- 统一五段：INTRO、WHAT、STORY、WHY / FEELING、ENDING；每部分以小标题及**一个自然段**呈现，段内不强行换行。
- 仅固定模板语言加粗（`<strong>`）；每题 1 分钟准备关键词用 `<mark class="speaking-keyword">` 在完整原文与关键词清单同时标注。样式为浅绿色 + 加粗 + 下划线，和写作批改专用 `diff`、五色批注区分。
- 使用 `.speaking-answer` 控制框架段落样式，用 `.keyword-list` 在宽屏双栏显示关键词、窄屏单栏。隐藏高亮、放大字号和富文本复制复用 `assets/js/site.js`。
- 姓名、年龄、职业身份和具体经历属于口语训练设定；不能把“仅看视频”代替真实朋友关系或“看运动视频”代替运动员成就。

## Speaking 紧凑阅读布局（v1.1，2026-11）

针对 `speaking/part2/people/` 中的 Zoe 模板、目录及 16 道题启用 `<body class="speaking-compact">`，其他 Speaking 页面可选择复用。通过共享 `assets/css/site.css` 的同名前缀规则实施，不影响 Writing 布局。

- **默认阅读顺序：**短页头 → 1 分钟关键词 → 五段完整英文稿 → 可展开 Cue Card → 可展开改动说明；文章和关键词始终默认可见。
- **减少留白、不压缩字体：**缩减 hero、卡片、导航和模块间距，保持英文 16–17px 左右和 1.7 以上行距，限制行宽。五段框架各为一个自然段，段内不人为换行。
- **关键词与框架：**关键词以自动换行的短标签列出，并在正文以 `.speaking-keyword` 背景标注；固定框架保留粗体，两种语义明确区分。
- **辅助内容折叠：**使用原生 `details/summary`，折叠题卡及附加说明。要提供明确 summary，支持键盘与触屏；不要隐藏主要回答。
- **紧凑目录：**`.speaking-topic-grid` 双栏 Topic 链接，窄屏切为单栏；保留完整题号和可访问链接。
- **交互和一致性：**复制、放大、隐藏高亮沿用共享 JS；不允许页面内 CSS 和内联事件。保留目录与首页回链。
- **检查范围：**手机、放大阅读、键盘、打印。页面布局结构示例见 `design-system/index.html`。
