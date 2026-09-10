# Output Contract

## Folder Naming

Use a polished, presentation-ready Chinese or requested-language topic name. Use the content topic as the folder name, not the package type.

Avoid copying platform titles, blogger titles, account names, trendy punctuation, dates, or source identifiers unless essential to the user's topic.

The PPT name and output folder name are related but not identical:

- `PPT名称` is the polished final title used in the outline.
- The output folder is named `<PPT名称>_提示词阶段`.

If the user provides a target output address, create the child folder under that address:

```text
<target-output-address>/<PPT名称>_提示词阶段/
```

If the user gives a path that might be either a parent folder or the exact desired output folder, ask before creating files. If no target address is provided, create `<PPT名称>_提示词阶段` in the current working directory or another clearly appropriate local workspace.

Good examples:

- `从牛来到我来新学期我准备好了_提示词阶段`
- `AI工具赋能教学实践_提示词阶段`
- `年度项目复盘与增长计划_提示词阶段`
- `校园安全第一课_提示词阶段`
- `产品发布会核心叙事_提示词阶段`

## PPT内容大纲.txt

Use this structure:

```text
PPT名称：
目标主题：
使用者：
目标受众：
使用场景：
目标页数：
制作模式：可编辑 / 整页图片 / 混合（注明用户指定或本次假设；混合注明页段）
设计调整边界：必留文案、可简化内容、是否允许拆页；具体位置与字号留待制作时校准
内容来源：
材料角色与使用尺度：
整体叙事节奏：
视觉风格方向：

第01页
页面类型：
页面标题：
本页目标：
核心内容：
1.
2.
3.
建议版式：
视觉重点：
备注：
```

Each page must include:

- 页码
- 页面类型
- 页面标题
- 本页目标
- 核心内容, sized to the page's communication need; distinguish exact audience-facing copy from optional support and teacher notes rather than forcing a fixed bullet count
- 建议版式
- 视觉重点
- 备注

Use `备注：` to record page-specific production notes:

- Required image asset filename from `images/`
- Whether a chart, table, process, diagram, or map should be rebuilt as editable PPT elements
- Special font treatment, with exact line mapping kept in `字体说明.txt`
- Source, permission, citation, official/brand/IP, or web usage notes
- Material role notes when a page uses one source for content and another for layout/style
- Reusable page-template notes, especially when several content pages should share the same background/master and only replace the middle content area
- Any later PPT production requirement that should not be lost

Common page types:

- 封面页
- 目录页
- 背景页
- 问题引入页
- 核心观点页
- 概念解释页
- 数据图表页
- 流程说明页
- 时间线页
- 案例分析页
- 对比分析页
- 方法模型页
- 方案页
- 互动讨论页
- 练习任务页
- 行动计划页
- 总结页
- Q&A页
- 结束页

Education/courseware page types may also include:

- 课堂导入页
- 知识讲解页
- 情境判断页
- 小组任务页
- 学生输出页
- 课堂练习页
- 成长承诺页

## 风格提示词.txt

Use this structure:

```text
一、整体风格总结

二、色彩体系

三、版式布局

四、字体风格

五、图形元素

六、图片处理

七、图片素材清单

八、可复用 AI 设计提示词

九、负面约束

十、自检记录
```

If `images/` is created, `七、图片素材清单` must list:

- Filename
- Used on which page(s)
- Purpose: source chart, data figure, product photo, character image, style reference, etc.
- Source: user-provided, extracted from material, official source, web source, etc.
- Usage note: rebuild as editable chart, use as visual reference only, allowed official/IP asset, etc.

If no images are packaged, write:

```text
本项目无需额外图片素材文件夹。
```

The reusable AI design prompt must support 16:9 full-slide generation and include:

- Overall art direction
- Palette with approximate HEX values when possible
- Typography direction and pointer to `字体说明.txt`
- Layout rhythm and master-page consistency
- Reusable background/master-page groups, including fixed elements and variable middle content zones
- Illustration/image treatment
- Image asset usage and packaging rules
- Information density
- Decorative elements
- Visual complexity levels for cover/divider/body/data pages
- Production mode and corresponding text treatment: editable text/image separation or full-image exact-copy generation; mixed mode includes page ranges
- Flexible layout families, typography limits, permitted production adjustments, and sample/render/review/repair handoff from production-and-layout.md
- Negative constraints

## 字体说明.txt

Use this structure:

```text
一、字体选择原则

二、本机字体检查结果

三、本项目使用字体清单

四、字体文件打包清单

五、逐页逐句字体标注

六、替代字体方案

七、授权与使用说明

八、自检记录
```

For `五、逐页逐句字体标注`, use a repeatable structure:

```text
第01页
1. 文案：...
   字体：...
   字重/样式：...
   字号层级：封面主标题 / 副标题 / 正文 / 注释 / 标签 / 页码 / 数字
   用途说明：...
```

Every audience-facing line planned in the outline should be covered. If repeated list items share one font rule, list each sentence and then apply one shared rule.

Mappings may reference shared role size bands rather than rigid per-line sizes. For full-image pages, label font selections as visual targets, not verified raster font identities. Keep the production mode and adjustment boundaries consistent across all three files.

## Optional Folders

Create `images/` only for necessary assets that should travel with the package:

- Data charts, tables, diagrams, maps, screenshots, or figures extracted from source materials
- User-provided reference images needed as concrete source assets
- Official, brand, IP, product, film, or event images when the user permits or requests their use
- Portraits, real photos, product photos, classroom/event photos, evidence screenshots, UI screenshots, or scene photos when the PPT content genuinely needs them
- Web-sourced real images when necessary and permitted, with source and usage notes recorded

Do not create `images/` when assets are only style inspiration and can be described in the prompt.

For every image, record whether it is:

- Direct PPT image material
- Visual reference only
- Rebuild reference for an editable chart, table, map, process, or diagram
- Generation reference for a new illustration, portrait, product scene, or real-photo style image

Create `fonts/` only when selected local font files should travel with the package and can be located. Do not package unused fonts. If redistribution rights are unclear, mark `授权需自行确认`.

`字体说明.txt` is always required even when `fonts/` is not created. It must explain every page's audience-facing text font usage.
