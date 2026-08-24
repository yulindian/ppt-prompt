#!/usr/bin/env python3
"""Validate a ppt-prompt planning package."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


REQUIRED_PAGE_FIELDS = (
    "页面类型：",
    "页面标题：",
    "本页目标：",
    "核心内容：",
    "建议版式：",
    "视觉重点：",
    "备注：",
)

REQUIRED_OUTLINE_HEADER_FIELDS = (
    "PPT名称：",
    "目标主题：",
    "目标受众：",
    "使用场景：",
    "目标页数：",
    "内容使用模式：",
    "内容对标文件：",
    "风格对标文件：",
    "素材权限：",
    "明确禁止：",
    "内容对标映射：",
)


def read_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except UnicodeDecodeError as exc:
        raise ValueError(f"{path.name} must be UTF-8: {exc}") from exc


def page_blocks(outline: str) -> list[tuple[int, str]]:
    matches = list(re.finditer(r"(?m)^第(\d{2,3})页\s*$", outline))
    blocks: list[tuple[int, str]] = []
    for index, match in enumerate(matches):
        end = matches[index + 1].start() if index + 1 < len(matches) else len(outline)
        blocks.append((int(match.group(1)), outline[match.start():end]))
    return blocks


def validate(folder: Path, expected_pages: int | None) -> list[str]:
    errors: list[str] = []
    outline_path = folder / "PPT内容大纲.txt"
    style_path = folder / "风格提示词.txt"

    if not outline_path.is_file():
        errors.append("Missing PPT内容大纲.txt")
    if not style_path.is_file():
        errors.append("Missing 风格提示词.txt")
    if errors:
        return errors

    try:
        outline = read_text(outline_path)
        style = read_text(style_path)
    except ValueError as exc:
        return [str(exc)]

    for field in REQUIRED_OUTLINE_HEADER_FIELDS:
        if field not in outline:
            errors.append(f"Outline missing header field: {field}")

    pages = page_blocks(outline)
    if not pages:
        errors.append("No page blocks found")
    if expected_pages is not None and len(pages) != expected_pages:
        errors.append(f"Expected {expected_pages} pages, found {len(pages)}")

    expected_numbers = list(range(1, len(pages) + 1))
    actual_numbers = [number for number, _ in pages]
    if actual_numbers != expected_numbers:
        errors.append(f"Page numbering is not contiguous: {actual_numbers}")

    for number, block in pages:
        for field in REQUIRED_PAGE_FIELDS:
            if field not in block:
                errors.append(f"Page {number:02d} missing field: {field}")

    images_dir = folder / "images"
    if images_dir.exists() and not images_dir.is_dir():
        errors.append("images exists but is not a directory")
    elif images_dir.is_dir():
        files = sorted(path for path in images_dir.iterdir() if path.is_file())
        if not files:
            errors.append("images directory is empty; remove it when no assets are packaged")
        for asset in files:
            if asset.name not in outline and asset.name not in style:
                errors.append(f"Unreferenced packaged asset: {asset.name}")
        if "权限" not in style and "permission" not in style.lower():
            errors.append("Style file does not record asset permission information")

    if "内容对标映射：" in outline:
        mapping = outline.split("内容对标映射：", 1)[1].split("\n", 1)[0].strip()
        if not mapping:
            errors.append("内容对标映射 is empty")

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("folder", type=Path, help="Planning package folder")
    parser.add_argument("--expected-pages", type=int)
    args = parser.parse_args()

    folder = args.folder.resolve()
    if not folder.is_dir():
        print(f"ERROR: folder does not exist: {folder}")
        return 2

    errors = validate(folder, args.expected_pages)
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1

    print("Package is valid")
    return 0


if __name__ == "__main__":
    sys.exit(main())
