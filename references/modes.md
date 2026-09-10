# Work Mode Guidance

Modes are common starting points, not a closed list. Before selecting a mode, first read [material-roles.md](material-roles.md) when multiple materials or mixed requirements are present.

The most reliable execution model is:

```text
main goal + material roles + usage scale + target constraints
```

Use the mode that best describes the main goal, then combine it with the material role map. If a request does not fit the three common modes below, define a clear custom primary mode in the outline metadata and still follow the output contract.

## Image-Based Recreation Mode

Use when the user provides PPT screenshots, slide images, posters, long images, Xiaohongshu-style references, or visual examples and asks for 二创 / 仿制 / 风格学习 / 内容重构 / 根据图片内容做一套.

Goal:

- Extract theme, topic angle, content structure, page types, information hierarchy, and reusable visual direction.
- Recreate as a differentiated, reusable PPT planning package.

Required inputs:

- Reference images
- Target audience
- Target page count
- Use scenario

If the user mixes this with another main content source, treat the images as style/layout/content-module references unless the user says their text content is the main content source.

Extract from images:

- Topic and likely intent
- Content modules
- Page sequence logic
- Page types
- Information density
- Visual mood
- Color system
- Typography direction
- Layout patterns
- Image/text separation
- Interactions or tasks, if relevant

Do not copy:

- Original wording
- Original examples
- Original page order exactly
- Original role names or activity names when distinctive
- Account marks, watermarks, QR codes, platform identifiers
- Unique source visuals, screenshots, UI frames, device frames, or source-specific marks

Differentiation requirements:

- Rebuild the topic angle when the source has a distinctive title or platform-style hook.
- Do not keep three consecutive pages with the same logic as the reference.
- Replace at least 40% of page types with new formats when the task is a true recreation.
- Target content similarity below 40%.
- Target page-structure similarity below 50%.
- Preserve only about 60%-70% of the broad visual mood.

If a source image contains a data chart, diagram, map, table image, product image, or other visual that must be reused or redrawn later, save the needed asset into `images/` and reference its filename in the relevant page's `备注：`.

## Topic Research and Synthesis Mode

Use when the user gives a topic, hot topic, person, film, book, product, policy, event, concept, course theme, or business/report theme and asks to create a PPT outline.

Goal:

- Research or synthesize reliable information.
- Turn the topic into a structured PPT narrative.
- Match or infer an appropriate visual style, optionally using user-provided style references.

Required inputs:

- Topic
- Target audience
- Target page count
- Use scenario

Web research:

- Browse before generating when the topic depends on recent, factual, niche, or external information.
- Prefer primary or reliable sources when factual accuracy matters.
- Use official sources for specific brands, products, films, books, policies, institutions, or current events.
- Summarize sources; do not copy long passages.
- Cite sources in the final response when web research was used.

Hot topic handling:

- Hot topics are entry points, not the whole PPT.
- Keep the user's actual use scenario dominant.
- For education/classroom themes, use roughly `Hot topic 30% / educational or presentation goal 70%`.

Style handling:

- If the user provides reference images, use them as style references unless they ask for image-based recreation.
- If no style reference is provided, infer a style appropriate to topic, audience, and use scenario.
- Record the inferred style direction in `风格提示词.txt`.

## Material Decomposition Mode

Use when the user provides PPT report materials, meeting notes, course outlines, training notes, research notes, documents, transcripts, tables, or raw content and asks to turn them into a PPT outline and style prompt.

Goal:

- Break provided materials into a clear slide sequence.
- Preserve the user's content intent.
- Improve structure, narrative flow, page types, and visual expression.

Required inputs:

- Source materials or outline
- Target audience
- Target page count
- Use scenario

Process:

- Identify the source material type: report, lesson/course outline, training content, proposal, project summary, product intro, activity plan, speech notes, etc.
- Extract core messages, supporting points, data, cases, and required conclusions.
- Group content into sections.
- Decide what should become a title page, overview page, content page, data/chart page, case page, summary page, action page, or Q&A page.
- Keep the original meaning, but rewrite page titles and slide structure for clarity.

If materials are too large, prioritize:

- User-stated goal
- Executive summary or conclusion
- Section headings
- Repeated key terms
- Data and examples supporting the main message
- Required teaching/reporting outputs

If source materials contain required data charts, diagrams, tables, screenshots, or figures, place needed image assets in `images/` when feasible and note filenames in `PPT内容大纲.txt`.

## Mixed-Source Composition Mode

Use when the user gives several materials with different purposes, such as:

```text
参考A材料风格内容排版，用B内容资料，整体贴合C
```

Goal:

- Combine sources according to their roles instead of treating every source the same way.
- Preserve the main content source at the allowed usage scale.
- Use reference materials for style, layout, and module inspiration without copying protected or distinctive content.
- Make the final PPT fit the target audience, use scenario, tone, brand, curriculum, or platform requirement.

Process:

1. Build a material role map using [material-roles.md](material-roles.md).
2. Choose the main content source and usage scale.
3. Choose which references affect visual style, layout rhythm, information hierarchy, page types, or modules.
4. Apply target constraints to language difficulty, narrative depth, tone, and visual appropriateness.
5. Record the role map in `PPT内容大纲.txt`.

Priority:

- Target constraints decide fit and should override conflicting style/content references.
- Main content source decides factual substance and slide messages.
- Style/layout references decide presentation strategy but should be redesigned unless direct copying is explicitly allowed.
