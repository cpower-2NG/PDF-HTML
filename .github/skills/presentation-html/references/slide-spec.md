# Slide Spec

## Deck Model
- One deck = one theme = one typographic system.
- One slide = one primary idea.
- Keep the content linear enough that a future PPT conversion remains practical.

## Recommended Slide Types
- Title or opening
- Problem statement
- Agenda or roadmap
- Core content slides
- Evidence or demo slides
- Summary
- Call to action or closing

## Layout Rules
- Default canvas ratio: 16:9.
- Use a single page grid system with generous spacing.
- Keep large headings short.
- Keep body text scannable and avoid dense paragraphs.
- Prefer consistent alignment across the whole deck.

## Export Rules
- Prepare `@page` and `@media print` styles.
- Avoid layout effects that rely on scrolling, sticky positioning, or hover.
- Keep text as text, not baked into images.
- Use local fonts or broadly available system fallbacks when export reliability matters.
- When PPTX is a target, keep each slide export-safe: no overflow, no absolute-position dependency for core content, and no content that only appears on hover or after script timing.
- Prefer a linear DOM order that matches slide reading order, because most PPT conversion tools flatten or sample the page rather than understand layout intent.
- Use SVG or simple vector shapes for charts and diagrams so they survive conversion better than raster screenshots.
- Avoid background-only information; if something is important, repeat it as visible text.

## Validation Checklist
- No clipped content at the bottom or right edge.
- No hidden elements that only appear on one screen size.
- Backgrounds still read well when printed.
- Each slide has a clear hierarchy.
- The deck still works if animations are disabled.
- Every slide can be converted independently without needing cross-slide state.
