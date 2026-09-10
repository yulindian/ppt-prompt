# Material Roles and Usage Scale

Use this reference before choosing a work mode whenever the user provides multiple materials or mixed instructions.

The skill should not force all requests into a fixed set of modes. Instead, treat each request as:

```text
main goal + material roles + usage scale + target constraints + delivery stage
```

## Main Goal

Identify what the user wants now:

- Generate a PPT planning package only
- Convert source content into a PPT outline
- Recreate or transform a reference style
- Combine multiple content sources
- Fit an existing target audience, brand, curriculum, product, or scenario
- Prepare a handoff for later PPT production

If the main goal is unclear and affects the output, ask before creating files.

## Material Roles

Assign every source material one or more roles:

- **Main content source:** primary facts, arguments, outline, lesson content, data, script, or narrative. It may be preserved, condensed, reorganized, and lightly expanded according to the user's permission.
- **Secondary content source:** supplemental examples, cases, data, quotes, or explanations. Use it to enrich the main content without changing the main goal.
- **Content recreation source:** source to be二创. Extract topic angle, content modules, logic, and useful ideas, but rewrite wording, examples, order, and structure enough to avoid copying.
- **Style reference:** learn broad color, mood, illustration style, typography direction, visual density, and overall feel.
- **Layout reference:** learn page types, grid rhythm, information hierarchy, module arrangement, title placement, and visual pacing. Redesign the final layout unless the user explicitly asks to copy and has rights to do so.
- **Content module reference:** borrow module types such as目录、知识卡、案例页、互动页、复盘页、练习页, while rewriting specific text and recomposing pages.
- **Asset source:** source contains concrete visuals that should be packaged, referenced, generated from, or rebuilt later, such as charts, tables, diagrams, maps, portraits, product photos, real photos, screenshots, or evidence images.
- **Target constraint:** source defines audience, use scenario, brand tone, curriculum standard, platform style, buyer persona, course objective, or difficulty level. Target constraints override style/content sources when they conflict.
- **Factual source:** source supports factual claims, dates, policy details, product specs, data, or technical statements. Preserve accuracy and cite or record provenance when needed.

Record the role mapping in `PPT内容大纲.txt` when multiple materials are used differently.

## Usage Scale

For each material, decide and record the allowed usage scale:

- **Full use:** preserve core facts, structure, claims, cases, and data; rewrite into PPT language and improve sequencing. Use when the user owns the material or explicitly says it can be fully used.
- **Organize and expand:** preserve the main line while adding explanations, transitions, examples, summaries, teaching/reporting pages, or audience-specific framing.
- **Condense:** keep only the important points, conclusions, data, and examples needed for the target page count.
- **Recreate:** extract topic, module logic, information design, and broad style; rewrite wording, examples, order, and page logic. Use for二创 or platform/reference materials where copying is not desired.
- **Style-only:** use only visual mood, palette, typography direction, information density, and layout rhythm.
- **Asset-only:** use only specific visuals as packaged images, visual references, or rebuild references.
- **Constraint-only:** use only to guide fit, tone, difficulty, audience, brand, or scenario.

If the user says content can be completely used, do not over-sanitize it into a loose inspiration source. If the user asks for二创 or gives public/reference content without reuse permission, do not fully copy it.

## Mixed-Source Pattern

For requests like `参考A材料风格内容排版，用B内容资料，贴合C`, use this pattern:

```text
A: style reference + layout reference + content module reference
B: main content source, full use or organize-and-expand
C: target constraint
```

Execution priorities:

1. C controls audience, scenario, language difficulty, tone, and final usefulness.
2. B controls factual content, teaching/reporting substance, and slide messages.
3. A controls visual direction and reusable module inspiration, but not exact wording or copied layout unless explicitly allowed.

If B and C conflict, adapt B to C. If A and C conflict, adapt A's style to C. If A and B conflict, use B for content and A only for presentation strategy.

## Questions to Ask Before Execution

Ask a concise clarification before creating files when any of these are unclear and material:

- Which material is the main content source?
- Whether a source can be fully used or should be二创.
- Whether a reference is for style, layout, content modules, or direct asset use.
- Whether a provided output path is the target folder or the parent folder.
- Whether official, brand, IP, product, portrait, or real-photo assets may be used.
- Whether web research or factual expansion is expected for a topic that could be outdated or sensitive.

Do not ask when the role is obvious from the user's wording and proceeding will not materially harm the result.
