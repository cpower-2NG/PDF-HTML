---
name: presentation-html
description: "Generate HTML presentation decks from a topic, and prepare them for PDF or PPT export. Use for slide structure, visual theme design, semantic HTML, print layout, and export-ready decks."
argument-hint: "主题 / 受众 / 页数 / 风格 / 导出格式"
user-invocable: true
disable-model-invocation: false
---

# HTML Presentation Deck Skill

## When to Use
- User asks for a presentation, keynote, demo deck, report slides, workshop slides, or pitch deck.
- User wants AI to write the HTML/CSS for the deck.
- User wants the result to be exported to PDF or converted into PPT.

## Workflow
1. Gather only the essential inputs: topic, audience, language, page count or duration, output format, style direction, and any brand constraints.
2. Build the narrative first: opening, core sections, supporting evidence, and ending.
3. Generate a deck structure that is easy to print and easy to split into slides.
4. Write semantic HTML with a clear per-slide structure.
5. Add theme tokens with CSS variables, and keep the layout stable in 16:9 and print modes.
6. Check export safety: selectable text, local assets, no layout that depends on hover or scrolling.
7. If PPT output is requested, keep each slide self-contained and avoid visual tricks that are hard to convert.
8. If an editable PPTX is requested, explicitly plan the conversion path and keep the deck compatible with the chosen converter before writing the final HTML.

## Default Rules
- Prefer semantic HTML over canvas-heavy or framework-heavy solutions.
- Prefer one visual idea per deck.
- Prefer local assets or embedded data URIs.
- Keep the code easy to edit by hand.
- Avoid unnecessary dependencies unless the user asks for them.
- Use accessible contrast and clear typographic hierarchy.
- Prefer conversion-friendly layouts: one dominant block per slide, predictable flow, and limited overlap.
- Prefer PDF as the stable intermediate artifact when fidelity matters more than editability.
- Prefer PPTX conversion only after the HTML passes print preview and overflow checks.

## Quality Checklist
- Each slide has one main point.
- Spacing and typography are consistent across the deck.
- No text overlaps, clipping, or overflow in common viewport sizes.
- Print styles preserve background, page breaks, and margins.
- The deck remains understandable if animations are disabled.
- All images or charts have fallbacks if they are essential.

## Deliverables
Return these in order when generating a deck:
1. A short concept summary.
2. A slide outline.
3. The HTML or HTML plus asset structure.
4. Export notes for PDF and PPT.
5. Optional next-step commands for local preview or conversion.
6. If PPTX is requested, include the conversion route, the expected converter, and any limits on editability.

## References
- [Slide spec](./references/slide-spec.md)
- [Starter template](./assets/starter.html)
