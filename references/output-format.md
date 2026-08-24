# Output Format

## `PPT内容大纲.txt`

Begin with:

```text
PPT名称：
目标主题：
使用者：
目标受众：
使用场景：
目标页数：
输出语言：
内容使用模式：严格对标 / 启发参考 / 原材料拆解 / 主题研究 / 图片二创
内容来源：
内容对标文件：
风格对标文件：
素材权限：
明确禁止：
必须保留的核心模块：
允许重构的部分：
新增内容范围：
内容对标映射：
整体叙事节奏：
视觉风格方向：
```

Each page must include:

```text
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

Use `备注：` for timing, audience adaptation, citations, asset filenames, editable rebuilding, and permission notes.

When duration is specified, distribute approximate timing across sections or pages and check that the total is realistic.

## `风格提示词.txt`

Use:

```text
一、整体风格总结
二、参考角色与使用边界
三、色彩体系
四、版式布局
五、字体风格
六、图形元素
七、图片处理
八、图片素材清单
九、可复用AI设计提示词
十、负面约束
十一、自检记录
```

Under `二、参考角色与使用边界`, state which files control content, style, and assets and which uses are forbidden.

If no `images/` folder is created, write:

```text
本项目没有获得或不需要额外素材打包权限，因此不创建images文件夹。
```

If `images/` exists, list each real file and its permission basis. Do not list hypothetical assets as packaged files.

## Reusable Visual Prompt

Include:

- 16:9 canvas,
- art direction,
- palette and approximate HEX values where useful,
- typography direction,
- layout rhythm,
- illustration/photo treatment,
- cover/divider/body/data-page complexity,
- information density,
- editable text zones,
- image asset roles,
- negative constraints.

## Editable Text And Visual Separation

- Keep required titles, body text, labels, values, captions, notes, and calls to action as separate editable PPT elements.
- Keep backgrounds, illustrations, icons, posters, screens, signs, books, badges, cards, and decoration text-free whenever possible.
- Rebuild charts, diagrams, tables, and timelines as editable elements when later editability matters.
- Do not put dense text on complex photos, textures, or illustrations.

## Negative Constraints

Include relevant constraints:

- no watermark, account name, QR code, platform UI, or unrelated branding,
- no copying reference wording or full layouts,
- no extraction or packaging from sources without permission,
- no fake precise data,
- no pseudo-writing or garbled text inside images,
- no tiny or overcrowded text,
- no invented signatures, institutions, or credits,
- no unauthorized logo, character, poster, screenshot, or IP asset,
- no mislabeling fan material as official.
