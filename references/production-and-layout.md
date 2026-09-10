# Production Mode and Adaptive Layout

## Set the Route Before Production

Record one mode in both the outline metadata and style prompt:

- `可编辑`: required copy is native text; specify whether diagrams and structures also need editing. Generate illustrations/backgrounds without copy, then compose text separately.
- `整页图片`: the full slide, including the exact approved copy, is rasterized/generated. State that text is not independently editable. Do not apply editable-page bans on text inside the full-slide image.
- `混合`: identify page ranges and their modes; state which elements remain editable within any composite page. Unlisted pages inherit a named default, never an ambiguous guess.

PPTX can contain full-page images; PDF can be exported from editable slides. Neither extension nor a screenshot source determines the route. If a later request changes the route, update conflicting text, font, and asset instructions across all three planning files before handoff. Do not silently switch routes to conceal quality problems.

## Plan Constraints, Not Every Coordinate

Lock the topic, required copy and facts, content hierarchy, audience, visual direction, production route, and any user-fixed page count or layout. Distinguish required display text from optional supporting text and speaker notes. Mark verbatim material such as textbook passages explicitly; do not rewrite it for visual convenience.

Suggest a small set of layout families based on communication needs, not a compulsory template count. Describe each family's dominant visual, text/illustration relationship, alignment, whitespace, and suitable density. Identify repeat pages. Keep exact coordinates, mandatory line breaks, and fixed per-page font sizes optional unless requested or required for precise matching.

Allow production to adjust text-box dimensions, line breaks, spacing, illustration scale/crop, image-to-text ratio, and composition. Preserve useful image subjects and the reading order. Consistency means coordinated hierarchy and rhythm, not forcing every page into one layout or filling every blank area. Once representative pages work, reuse their established styles for comparable pages; deliberate exceptions must serve the content.

## Typography Boundaries

In `字体说明.txt`, define project-specific starting size bands, a reading-size floor, and upper bounds by role: cover, page title, key question, body, supporting label, folio. Consider the actual canvas dimensions, audience, viewing context, script, and selected font's visible glyph size. Do not impose one universal point-size table across decks.

Per-line mappings may refer to these role tokens instead of fixing a separate size for every sentence. At production, select a coherent working size per role and adjust within the bands after rendering. Do not shrink text simply to fit, enlarge body copy just to consume whitespace, or let equal-level titles drift across pages. A floor is a rejection threshold, not the default size. Teaching content must not be demoted to tiny annotation text.

When crowded: adjust line breaks and usable space, reduce decorative competition, change layout, then shorten only explicitly optional copy or split/rebalance pages if permitted. Preserve required wording and facts. A fixed page count cannot be increased silently; if layout changes cannot solve it, ask which constraint may change.

## Mode-Specific Repair

Editable pages: inspect actual rendered text, not just calculated boxes. Repair wrapping, clipping, font substitution, line spacing, margins, overlap, and visual weight using native elements. Check glyph coverage, including pinyin, before relying on a font.

Full-image pages: local font names and point sizes express a visual target, not a guarantee that the image model used that font or achieved exact metrics. Give the generator exact page copy and clear hierarchy, text area, density, and whitespace instructions. Judge actual letter size at intended display scale. Compare all generated text with the approved copy, including punctuation, pinyin, numbers, and omissions; OCR may assist but does not replace visual inspection. Regenerate or edit the affected image for wrong text or bad layout. Enlarging the same whole image does not repair the relative font size. Adding native overlay text changes the page to a composite workflow and needs the route updated, not an undisclosed substitution.

Mixed decks: apply each repair method to its own pages and compare both groups together for consistent apparent typography, color, and margins.

## Required Handoff, Not Work to Execute Now

Write the following project-adapted requirements into `风格提示词.txt`:

1. Before batch production, render representative pages covering the cover, the densest content, and a typical activity/diagram where present. A short deck can use fewer samples; mixed decks need coverage of both routes. Review actual images and fix the sample styles before expanding them. This internal check need not add user approvals unless requested by the user or production workflow.
2. Inspect every completed slide at readable display scale for correct copy, hierarchy, balanced whitespace, uncropped subjects, and absence of clipping/overlap. Review a whole-deck contact sheet for inconsistent apparent sizes, palette drift, and monotonous composition.
3. Repair and re-render affected pages, recheck neighbors using the same layout, and reconcile any approved copy/page-count changes with the outline and font mappings. Do not loop indefinitely: after two failed repair rounds for the same issue, report it and propose a route/layout/content tradeoff for confirmation.
4. Report what was actually inspected. If rendering or inspection is unavailable, disclose the unverified visual quality; never mark the design accepted based only on prompt text or structural checks.

Planning-stage self-checks validate these handoff instructions and their consistency only. Actual rendered quality is verified in the production stage.
