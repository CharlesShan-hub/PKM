"""
Markdown to HTML Exporter
将 Markdown 笔记导出为 HTML（保留相对路径结构到 dist 目录）
"""

DESCRIPTION = "Markdown 转 HTML 导出工具 - 将指定文件夹下的 .md 文件全量导出为 .html 到 dist 目录"

PARAM_PROMPTS = {
    'input_dir': {
        'label': '笔记根目录（基础文件夹）',
        'type': 'path',
        'default': '',
    },
    'output_dir': {
        'label': '输出目录（默认 dist）',
        'type': 'path',
        'default': '',
    },
}

import re
import html
from pathlib import Path
from typing import List, Optional

import markdown as md_lib


# 最简 HTML 模板：能显示标题和正文，样式后续再加
HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
</head>
<body>
{content}
</body>
</html>"""

# YAML frontmatter（--- 包裹的头部元数据）
FRONTMATTER_START = '---'

# 导出时排除的目录（Obsidian 配置、git 等）
EXCLUDED_DIRS = {'.git', '.obsidian', '.trash', '.idea', '__pycache__'}


def parse_frontmatter(content: str):
    """
    解析开头的 YAML frontmatter，返回 (title, 正文)

    逐行解析，只认文件开头的 --- 到下一个 --- 行，避免误吞正文。

    Args:
        content: 原始 Markdown 内容

    Returns:
        tuple: (title 字段或 None, 去掉 frontmatter 后的正文)
    """
    if not content.startswith(FRONTMATTER_START):
        return None, content

    lines = content.split('\n')
    for i in range(1, len(lines)):
        if lines[i].strip() == FRONTMATTER_START:
            title = None
            for line in lines[1:i]:
                m = re.match(r'^title:\s*(.+)$', line.strip())
                if m:
                    title = m.group(1).strip().strip('"\'')
                    break
            return title, '\n'.join(lines[i + 1:])

    return None, content


def strip_frontmatter(content: str) -> str:
    """
    过滤掉 YAML frontmatter 头部，返回正文内容

    Args:
        content: 原始 Markdown 内容

    Returns:
        str: 去掉 frontmatter 后的正文
    """
    _, body = parse_frontmatter(content)
    return body


def extract_title(content: str, fallback: str) -> str:
    """
    提取页面标题：优先取 frontmatter 的 title 字段，否则用文件名

    Args:
        content: 原始 Markdown 内容
        fallback: 备选标题（文件名）

    Returns:
        str: 页面标题
    """
    title, _ = parse_frontmatter(content)
    return title if title else fallback


def find_markdown_files(input_dir: Path) -> List[Path]:
    """
    递归查找所有 Markdown 文件，排除隐藏/无关目录

    Args:
        input_dir: 笔记根目录

    Returns:
        List[Path]: Markdown 文件路径列表
    """
    files = []
    for path in input_dir.rglob("*.md"):
        # 跳过排除目录下的文件
        if any(part in EXCLUDED_DIRS for part in path.relative_to(input_dir).parts[:-1]):
            continue
        files.append(path)
    return sorted(files)


def convert_to_html(md_content: str, title: str) -> str:
    """
    将 Markdown 内容转换为完整的 HTML 页面

    Args:
        md_content: 过滤 frontmatter 后的 Markdown 正文
        title: 页面标题

    Returns:
        str: 完整 HTML 内容
    """
    body = md_lib.markdown(md_content, extensions=['extra'])
    return HTML_TEMPLATE.format(title=html.escape(title), content=body)


def save_html(html_content: str, output_path: Path) -> None:
    """
    保存 HTML 文件到指定路径（自动创建父目录）

    Args:
        html_content: HTML 内容
        output_path: 输出文件路径
    """
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html_content)


def run(input_dir: Optional[str] = None, output_dir: Optional[str] = None) -> str:
    """
    主运行函数：全量导出

    扫描输入目录下所有 .md 文件，转换为 HTML 并写入输出目录（默认 dist），
    保留相对路径结构。

    Args:
        input_dir: 笔记根目录
        output_dir: 输出目录（默认 dist）

    Returns:
        str: 执行结果摘要
    """
    if not input_dir:
        return "错误: 需要提供输入目录参数"

    input_path = Path(input_dir)
    if not input_path.exists():
        return f"错误: 输入目录不存在: {input_dir}"
    if not input_path.is_dir():
        return f"错误: 输入路径不是目录: {input_dir}"

    # 输出目录默认 dist
    output_path = Path(output_dir) if output_dir else Path.cwd() / "dist"

    md_files = find_markdown_files(input_path)
    if not md_files:
        return f"未找到 Markdown 文件: {input_dir}"

    exported = []
    errors = []

    for md_file in md_files:
        try:
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()

            # 过滤 frontmatter 并确定标题
            body = strip_frontmatter(content)
            title = extract_title(content, md_file.stem)

            # 转换并保存，保留相对路径结构
            html_content = convert_to_html(body, title)
            rel_path = md_file.relative_to(input_path).with_suffix('.html')
            save_html(html_content, output_path / rel_path)

            exported.append(rel_path)
            print(f"[{len(exported)}/{len(md_files)}] {rel_path}")
        except Exception as e:
            errors.append(f"{md_file.name}: {str(e)}")

    # 汇总结果
    result = [
        "=" * 60,
        "Markdown 导出完成（全量）",
        "=" * 60,
        f"输入目录: {input_path}",
        f"输出目录: {output_path}",
        f"导出文件: {len(exported)} / {len(md_files)} 个",
    ]
    if errors:
        result.append("")
        result.append("错误列表:")
        for error in errors:
            result.append(f"  - {error}")
    result.append("=" * 60)

    return "\n".join(result)


if __name__ == "__main__":
    import sys

    if len(sys.argv) >= 2:
        input_dir = sys.argv[1]
        output_dir = sys.argv[2] if len(sys.argv) > 2 else None
        print(run(input_dir, output_dir))
    else:
        print("用法: python markdown_to_html.py <input_dir> [output_dir]")
        print("示例: python markdown_to_html.py D:/path/to/notes ./dist")
