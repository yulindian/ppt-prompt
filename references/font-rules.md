# Font Rules

Always create `字体说明.txt` for every PPT planning package.

## Font Selection

Select fonts according to topic, audience, tone, and visual style:

- Children's, storybook, playful, or classroom decks may use local rounded, handwritten, or friendly fonts when available.
- Formal reports, business decks, policy decks, and academic decks should use clean sans-serif or serif fonts with strong readability.
- Traditional culture, literature, ceremony, or heritage decks may use Song, Kai, Li, or calligraphic-style fonts when appropriate.
- Technology, product, and dashboard decks should use modern sans-serif fonts with stable numeric rendering.

Use a broader range of verified local fonts when the deck benefits from it. Do not default only to Microsoft YaHei, SimHei, or generic black fonts.

## Local Font Inspection

For size bands, permitted production adjustments, and full-image limitations, follow [production-and-layout.md](production-and-layout.md). Per-line coverage remains required, but role-based sizing is sufficient; do not require exact point sizes for each sentence before rendering. In full-image mode, checked local fonts are visual references or future editable substitutes, not proof the generated image uses them. Package fonts only when genuinely needed; explain omissions normally.

Before finalizing font choices, inspect local fonts when feasible. Useful Windows sources:

```text
C:\Windows\Fonts
C:\Users\<user>\AppData\Local\Microsoft\Windows\Fonts
HKLM:\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Fonts
HKCU:\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Fonts
```

Use fonts actually available on the machine. Do not invent or casually recommend unverified font names. If an ideal font is missing, choose the closest local substitute and record the substitution.

## 字体说明.txt Requirements

Include:

- Font selection principles for this deck
- Local font inspection result
- Project font list: display name, role, weight/style, local file name or path when found, fallback font
- Font packaging list: which files were copied into `fonts/`, or why no font files were packaged
- Per-page and per-sentence font mapping for every audience-facing line in `PPT内容大纲.txt`
- License/permission notes, especially for system or third-party fonts

The per-page mapping must be explicit enough for a later PPT maker to implement without guessing:

```text
第01页
页面标题《...》：字体 / 字重 / 字号层级 / 用途说明
副标题《...》：字体 / 字重 / 字号层级 / 用途说明
正文《...》：字体 / 字重 / 字号层级 / 用途说明
标签《...》：字体 / 字重 / 字号层级 / 用途说明
页码/数字：字体 / 字重 / 字号层级 / 用途说明
```

If a page has repeated bullet items or table cells using the same treatment, list all audience-facing text and state the shared font rule. Do not merely say "正文统一使用某字体" without tying it back to each page's text.

## Fonts Folder

When creating `fonts/`:

- Copy only fonts actually used by the deck.
- Use stable filenames matching the original file where possible.
- Do not package unused fonts.
- If redistribution rights are unclear, avoid packaging unless needed and clearly mark `授权需自行确认`.
- If a selected font cannot be copied, record its local name and fallback instead of silently omitting it.

In `风格提示词.txt`, describe the font strategy by text role and point to `字体说明.txt` for exact line-level mapping.

In the final response, explicitly state whether `fonts/` was created. If it was not created, explain whether the reason is system font usage, licensing uncertainty, unavailable files, or no need to package font files.
