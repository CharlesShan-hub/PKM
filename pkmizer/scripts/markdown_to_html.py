"""
Markdown to HTML Exporter
将 Markdown 笔记导出为 HTML（保留相对路径结构到站点根目录），支持动态切换 Typora 主题

本文件是入口（供 GUI 与命令行加载），具体实现拆在 mdh/ 子包：
  content.py  - 正文处理（frontmatter/标题/链接修复）
  theme.py    - 主题适配与发现
  theme_ui.py - 主题切换按钮
  nav.py      - 全站文件树数据
  nav_ui.py   - 左侧文件树导航面板
  html.py     - 页面组装与保存
"""

DESCRIPTION = "Markdown 转 HTML 导出工具 - 全量导出 .md 为 .html，支持 Typora 主题动态切换"

PARAM_PROMPTS = {
    'input_dir': {
        'label': '笔记根目录（基础文件夹）',
        'type': 'path',
        'default': '',
    },
    'output_dir': {
        'label': '站点根目录（默认 dist，含 themes/）',
        'type': 'path',
        'default': '',
    },
}

import re
import subprocess
import sys
from pathlib import Path
from typing import List, Optional

# GUI 通过 importlib 加载本文件时 scripts 目录不一定在 sys.path，手动加入以导入 mdh 子包
sys.path.insert(0, str(Path(__file__).resolve().parent))

from mdh.content import (
    build_link_index,
    collect_assets,
    convert_wikilinks,
    extract_title,
    find_excalidraw_files,
    find_markdown_files,
    strip_frontmatter,
)
from mdh.html import convert_to_html, save_html
from mdh.nav import build_site_tree, save_site_tree, site_tree_rel_path
from mdh.theme import adapt_themes_dir, ensure_themes_dir, scan_themes, themes_relative_path

# Excalidraw 渲染脚本（Node）：把 .excalidraw.md 转成站点内的 SVG
EXCALIDRAW_SCRIPT = Path(__file__).resolve().parent.parent / 'excalidraw' / 'svg.mjs'


def render_excalidraw(files: List[Path], input_path: Path, output_path: Path) -> int:
    """
    调用 Node 脚本把 .excalidraw.md 画布渲染为 SVG，写入站点对应位置

    Args:
        files: .excalidraw.md 文件列表
        input_path: 笔记根目录
        output_path: 站点根目录

    Returns:
        int: 成功渲染的画布数
    """
    if not files:
        return 0
    try:
        proc = subprocess.run(
            ['node', str(EXCALIDRAW_SCRIPT), str(output_path), str(input_path), *(str(f) for f in files)],
            capture_output=True, text=True, timeout=600,
        )
        if proc.stdout:
            print(proc.stdout.strip())
        if proc.returncode != 0 and proc.stderr:
            print(proc.stderr.strip())
        m = re.search(r'DONE ok=(\d+)', proc.stdout or '')
        return int(m.group(1)) if m else 0
    except Exception as e:
        print(f"Excalidraw 渲染失败: {e}")
        return 0


def run(input_dir: Optional[str] = None, output_dir: Optional[str] = None) -> str:
    """
    主运行函数：全量导出

    扫描输入目录下所有 .md 文件，转换为 HTML 并写入站点根目录（默认 dist），
    保留相对路径结构。站点根下自动准备 themes/（优先从 Typora 复制），
    每个页面内置主题切换控件与全局文件树导航。

    Args:
        input_dir: 笔记根目录
        output_dir: 站点根目录（默认 dist）

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

    # 站点根目录默认 dist
    output_path = Path(output_dir) if output_dir else Path.cwd() / "dist"
    output_path.mkdir(parents=True, exist_ok=True)

    # 准备 themes 目录并扫描主题
    themes_dir = ensure_themes_dir(output_path)
    adapted_count = adapt_themes_dir(themes_dir)
    themes = scan_themes(themes_dir)

    # 生成全站文件树（供左侧导航共用，独立一份 JSON 加载快）
    save_site_tree(output_path, build_site_tree(input_path))

    md_files = find_markdown_files(input_path)
    if not md_files:
        return f"未找到 Markdown 文件: {input_dir}"

    # 渲染 Excalidraw 画布为 SVG（供页面 ![[...]] 嵌入引用）
    excalidraw_files = find_excalidraw_files(input_path)
    excalidraw_ok = render_excalidraw(excalidraw_files, input_path, output_path)

    # 构建 wiki 链接索引（Obsidian 文件名 -> 站点路径），供 ![[...]] / [[...]] 解析
    link_index = build_link_index(md_files, excalidraw_files, input_path)

    exported = []
    errors = []
    copied_assets = set()

    for md_file in md_files:
        try:
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()

            # 过滤 frontmatter、转换 wiki 语法（渲染前）、确定标题
            body = strip_frontmatter(content)
            body = convert_wikilinks(body, link_index, md_file.relative_to(input_path))
            title = extract_title(content, md_file.stem)

            # 计算到 themes/ 与 site-tree.json 的相对路径，转换并保存
            rel_path = md_file.relative_to(input_path).with_suffix('.html')
            themes_rel = themes_relative_path(rel_path)
            site_tree_rel = site_tree_rel_path(rel_path)
            html_content = convert_to_html(body, title, themes_rel, themes, site_tree_rel)
            save_html(html_content, output_path / rel_path)

            # 按需复制页面引用的本地图片资源（只复制被引用的，不整目录搬运）
            copied_assets.update(collect_assets(html_content, md_file, input_path, output_path))

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
        f"站点根目录: {output_path}",
        f"主题目录: {themes_dir}",
        f"可用主题: {len(themes)} 个（{', '.join(themes[:5])}{'...' if len(themes) > 5 else ''}）",
        f"适配主题: {adapted_count} 个（Typora 选择器已映射到标准 HTML）",
        f"导出文件: {len(exported)} / {len(md_files)} 个",
        f"复制资源: {len(copied_assets)} 个（页面引用的图片按需复制）",
        f"Excalidraw 画布: {excalidraw_ok} 个渲染为 SVG（{len(excalidraw_files)} 个发现）",
    ]
    if errors:
        result.append("")
        result.append("错误列表:")
        for error in errors:
            result.append(f"  - {error}")
    result.append("=" * 60)

    return "\n".join(result)


if __name__ == "__main__":
    if len(sys.argv) >= 2:
        input_dir = sys.argv[1]
        output_dir = sys.argv[2] if len(sys.argv) > 2 else None
        print(run(input_dir, output_dir))
    else:
        print("用法: python markdown_to_html.py <input_dir> [output_dir]")
        print("示例: python markdown_to_html.py D:/path/to/notes ./dist")
