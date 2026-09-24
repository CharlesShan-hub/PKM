"""
全站文件树：构建 site-tree.json 数据、保存与相对路径计算
"""

import json
from pathlib import Path

from .content import EXCLUDED_DIRS


def build_site_tree(input_dir: Path) -> dict:
    """
    递归扫描笔记目录，构建全局文件树（目录 + .md 转 .html 的文件）

    Args:
        input_dir: 笔记根目录

    Returns:
        dict: 嵌套结构，目录 {'type','name','rel','children'}，文件 {'type','name','rel'}
    """
    def walk(d: Path, rel: str) -> dict:
        node = {'type': 'dir', 'name': d.name, 'rel': rel, 'children': []}
        entries = []
        for p in sorted(d.iterdir(), key=lambda x: x.name.lower()):
            if p.name in EXCLUDED_DIRS:
                continue
            rel_child = f"{rel}/{p.name}" if rel else p.name
            if p.is_dir():
                entries.append(walk(p, rel_child))
            elif p.suffix.lower() == '.md' and not p.name.endswith('.excalidraw.md'):
                # .excalidraw.md 是画布资源（渲染成 SVG 被引用），不进入文件树
                entries.append({'type': 'file', 'name': p.stem + '.html', 'rel': rel_child[:-3] + '.html'})
        node['children'] = entries
        return node

    return walk(input_dir, '')


def save_site_tree(site_root: Path, tree: dict) -> Path:
    """
    把全局文件树写入站点根的 site-tree.json（全站页面共用，加载一次即缓存）

    Args:
        site_root: 站点根目录
        tree: 文件树字典

    Returns:
        Path: site-tree.json 路径
    """
    target = site_root / 'site-tree.json'
    with open(target, 'w', encoding='utf-8') as f:
        json.dump(tree, f, ensure_ascii=False)
    return target


def site_tree_rel_path(rel_path: Path) -> str:
    """
    计算从当前页面到 site-tree.json 的相对路径（与 themes 同规则）

    Args:
        rel_path: 页面相对站点根的路径

    Returns:
        str: 相对路径（如 site-tree.json、../site-tree.json）
    """
    depth = len(rel_path.parts) - 1
    prefix = '/'.join(['..'] * depth)
    return f"{prefix}/site-tree.json" if prefix else "site-tree.json"
