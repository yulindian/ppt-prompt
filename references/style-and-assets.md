# Style, Assets, and Editable Text

## Audience-Facing Copy

Distinguish internal planning metadata from slide text that the end audience will see.

- `目标受众`, `使用场景`, `使用者`, and similar context fields belong in outline metadata, not audience-facing slide copy.
- Do not write product-introduction phrases on slides, such as `小学主题班课`, `开学第一课`, `适用于...`, `20页PPT+教学设计`, `通用模板`, unless the user explicitly asks.
- On cover pages and section dividers, write the actual usable lesson/report/training theme directly.
- If the user gives a broad scenario, convert it into a concrete classroom-facing or audience-facing topic instead of displaying the scenario as a selling point.

## Layout Consistency

Apply [production-and-layout.md](production-and-layout.md) first. The consistency rules below describe reusable layout families, not a requirement to freeze coordinates before rendering. Production may adjust the family after representative-page review and apply the change consistently.

When several pages belong to the same section, module, activity group, or repeated page type, keep their layout style consistent:

- Same master layout, grid, title position, content block position, margin system, color role, decorative corner elements, and visual hierarchy.
- Change mainly slide text, page number, section label, and page-specific illustration subject.
- Section dividers should share chapter title treatment, illustration scale, background complexity, and decorative rhythm.
- Repeated activity, comparison, case, data, quote, exercise, or summary pages should use reusable template families.
- Change layout only when the page's communication need genuinely changes.

Record this in `风格提示词.txt`, especially under `三、版式布局` and `八、可复用 AI 设计提示词`.

For repeated content pages that should look like one coherent set, explicitly state when the same background or master page should be reused and only the central content area should change. In the prompt, define:

- Shared background/master name or group, such as `知识讲解页共用背景A`.
- Fixed elements: background image, decorative corners, title area, page number, side ornaments, color blocks, and safe margins.
- Variable elements: the middle content text, table, example, chart, activity prompt, or image placeholder.
- Alignment and spacing relationships for the variable content area; exact position, width, height, and padding are optional and can be calibrated during production.
- Which pages belong to the group.

Use this pattern when it improves consistency:

```text
第05-08页为同一内容页模板组：共用背景与标题层级，替换中间内容。先渲染代表页校准间距、图文比例和字号，再沿用到同组页面；过密页可换同风格版式，不强行缩字。
```

## Editable Text and Visual Separation

Use these principles for editable pages. For full-image pages, include the exact approved text in the full-slide generation prompt, with dedicated readable text areas and mode-specific review/repair. For mixed mode, apply the appropriate rules by page. Full-image text is not independently editable.

- Keep illustrations, backgrounds, decorative elements, icons, book covers, posters, UI screens, signs, badges, cards, charts, and image areas text-free whenever possible.
- Keep those same image/decorative areas free of numbers whenever possible.
- Put required titles, body text, labels, chart values, figure captions, notes, and callouts in the outline as separate editable PPT text.
- Cover, section divider, and transition pages may use richer full-scene visuals.
- Body/content pages must keep text and visuals in clearly separated zones.
- Avoid placing dense text over complex images, strong textures, gradients, photos, or illustrations.
- Data/chart pages should not generate fake embedded chart text or numbers inside images; chart titles, axis labels, legends, and values should be editable.
- If a page needs a short readable label inside an image, state it clearly and keep it minimal.

## Image Asset Packaging

Create `images/` only when specific image assets are needed for later PPT production.

Images can be packaged for several legitimate reasons:

- The PPT needs a data chart, table, map, process, diagram, or report figure as a source or rebuild reference.
- The PPT needs a portrait,人物画像, real person photo, product photo, real shooting photo, classroom/event/site photo, or factual scene image.
- The PPT needs screenshots, UI images, evidence captures, official visuals, brand/product/IP visuals, or other factual assets.
- The user explicitly provides images to use as source assets rather than only style inspiration.

When adding images:

- Use stable filenames, such as `page05_data_chart.png`, `page12_product_photo.jpg`, `style_reference_01.png`, or `source_diagram_customer_journey.png`.
- Prefer copying or extracting only the necessary visual region, not full-page screenshots with irrelevant surroundings.
- Preserve original file quality when possible.
- Do not alter source images destructively.
- Do not include watermarked, account-marked, QR-coded, or platform UI images unless explicitly required.
- For web or official images, record source and usage notes in `风格提示词.txt` or page `备注：`.
- Reference every packaged image from at least one page `备注：` or from the style prompt.
- If copyright or permission is unclear, mark the image as `visual reference only` and recommend replacing it with an authorized asset during final production.

For each packaged image, explicitly mark one usage type:

- `直接使用`
- `视觉参考`
- `可编辑重建参考`
- `生成参考`

When an image contains data, tables, flowcharts, diagrams, or maps that should be editable later, prefer `可编辑重建参考` and instruct the later PPT stage to rebuild the content as editable chart/shape/text when possible.

For web-sourced real images, prefer stable original files over search-result thumbnails. Record the source page URL, image URL when available, license/permission note when discoverable, and intended slide usage.

## Brand, IP, and Copyright

Clarify how reference materials should be used:

- Style reference: learn broad color, layout, mood, typography direction, information density.
- Content reference: extract and restructure information only when requested.
- Asset use: use official/brand/IP/film materials only when the user explicitly permits or requests it, or when factual visual identification is necessary and usage is documented.

Even when permitted:

- Do not include watermarks, account names, QR codes, platform UI, or source screenshots unless explicitly requested.
- In editable mode, do not generate body text inside illustration assets. In full-image mode, render only the approved page copy in dedicated readable areas; do not invent text or reproduce source poster layouts.
- Avoid reproducing a full official poster, screenshot, or copyrighted page layout as a slide background unless the user explicitly asks and has rights to use it.

## Mandatory Negative Constraints

Include relevant negative constraints in `风格提示词.txt`, conditioned on the production mode. The bans below on text/numbers inside decorative assets must not become a ban on required page copy inside an intentionally full-image slide. Do not send contradictory editable-only requirements to the full-image route.

- 不要水印
- 不要账号名
- 不要二维码
- 不要平台元素
- 不要原作者标识
- 不要店铺标识
- 不要直接复制参考图原文案
- 不要照搬原页面顺序
- 不要复刻完全一致页面布局
- 不要使用原视频截图或表情包拼贴
- 不要把产品包装词写进面向观众的页面文案，除非用户明确要求展示
- 不要把实景照片里的屏幕外环境、设备边框、翻页 UI 识别为 PPT 设计
- 不要在插图、背景、图标、书本封面、海报、路牌、票据、徽章、气泡或装饰元素里生成大段文字
- 不要在插图、背景、图标、书本封面、海报、路牌、票据、徽章、气泡或装饰元素里生成数字，除非确实需要且后期无法用可编辑 PPT 文本替代
- 正文页不要把文字压在复杂插图、照片或强纹理背景上
- 正文页不要让文字和插图混在同一视觉区域里难以编辑
- 不要文字过小或拥挤
- 不要中英文乱码

Add topic-specific negative constraints when needed:

- Brands/IP/films: do not include unauthorized logos, watermarks, platform UI, poster layouts, or official screenshots unless explicitly permitted.
- Data/report PPTs: do not invent precise data unless provided or sourced.
- Medical/legal/financial content: avoid unsupported claims and cite reliable sources when browsing.
