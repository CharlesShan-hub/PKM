"""
Wiki 链接迁移工具：把 Obsidian wiki 语法转换为标准 Markdown

- [[xxx]] / [[xxx|别名]]       ->  [文本](相对路径.md)（含 #锚点 保留）
- ![[xxx.png|尺寸]]            ->  ![文本](相对路径)（尺寸转 attr_list）
- ![[xxx.excalidraw|尺寸]]     ->  保留 wiki 语法（画布嵌入供导出转 SVG），目标名补全为 .excalidraw
- 混合语法 ![[a](b.png)]      ->  ![](b.png)
- 代码块内的 [[...]] 不受影响；无法解析的引用保留原样并在报告中列出
"""

import posixpath
import re
import sys
from pathlib import Path
from typing import List, Optional, Tuple

sys.path.insert(0, str(Path(__file__).resolve().parent))

from mdh.content import EXCLUDED_DIRS, is_excalidraw_file

DESCRIPTION = "Wiki 链接迁移 - 把 Obsidian [[...]] 语法转换为标准 Markdown（画布嵌入保留）"

PARAM_PROMPTS = {
    'input_dir': {
        'label': '笔记根目录（基础文件夹）',
        'type': 'path',
        'default': '',
    },
    'dry_run': {
        'label': '仅预览（不写文件）',
        'type': 'bool',
        'default': True,
    },
}

# wiki 语法（画布嵌入先替换，避免被普通链接正则吃掉）
WIKI_EMBED_RE = re.compile(r'!\[\[([^\]|]+)(?:\|([^\]]+))?\]\]')
WIKI_LINK_RE = re.compile(r'(?<!!)\[\[([^\]|]+)(?:\|([^\]]+))?\]\]')
# 混合语法：![[name](../assets/x.png)]
WIKI_HYBRID_RE = re.compile(r'!\[\[([^\]|]+)\]\(([^)]+)\)\]')
# 围栏代码块（跳过其中内容）
FENCE_RE = re.compile(r'```.*?```', re.DOTALL)
# 图片扩展名
IMAGE_EXT_RE = re.compile(r'\.(png|jpe?g|gif|bmp|webp|svg)$', re.I)


def build_vault_index(files: List[Path], input_path: Path) -> dict:
    """
    构建全库文件索引（文件名/完整路径 -> 相对输入根的 posix 路径）

    覆盖 vault 内全部文件（含图片等非 .md），使 ![[assets/x.png]] 图片嵌入可解析；
    .md 文件额外注册去后缀键（如 xxx / xxx.excalidraw）。

    Args:
        files: vault 内全部文件
        input_path: 笔记根目录

    Returns:
        dict: 引用名 -> 相对路径（posix，含后缀）
    """
    index = {}
    for f in files:
        rel = f.relative_to(input_path)
        name = f.name
        p = rel.as_posix()
        index[name] = p
        index[p] = p
        if name.endswith('.md'):
            if name.endswith('.excalidraw.md'):
                index[name[:-3]] = p                 # xxx.excalidraw
                index[name[:-len('.excalidraw.md')]] = p  # xxx
            else:
                index[name[:-3]] = p                 # xxx（去 .md）
    return index


def resolve_target(target: str, md_rel: Path, index: dict) -> Optional[Tuple[str, str]]:
    """
    解析 wiki 引用目标，返回 (相对输入根的路径, 锚点)

    带路径前缀的相对当前 md 目录解析（试补 .md / .excalidraw / .excalidraw.md 后缀）；
    纯文件名按全库 basename 匹配。

    Args:
        target: wiki 引用名（可能带 #锚点）
        md_rel: 当前文件相对输入根的路径
        index: 全库索引

    Returns:
        Optional[tuple]: (相对输入根路径, 锚点)；找不到返回 None
    """
    t = target.strip()
    path_part, anchor = t, ''
    if '#' in t:
        path_part, anchor = t.split('#', 1)
    if '/' not in path_part:
        for cand in (path_part, path_part + '.md', path_part + '.excalidraw', path_part + '.excalidraw.md'):
            if cand in index:
                return index[cand], anchor
        return None, anchor
    md_dir = md_rel.parent.as_posix()
    base = posixpath.normpath(posixpath.join(md_dir, path_part))
    for cand in (base, base + '.md', base + '.excalidraw', base + '.excalidraw.md'):
        if cand in index:
            return index[cand], anchor
    # Obsidian 语义兜底：相对路径解析失败时按全库文件名（basename）匹配
    bname = posixpath.basename(path_part)
    if bname in index:
        return index[bname], anchor
    return None, anchor


def vault_rel_from(md_rel: Path, target_rel: str) -> str:
    """
    计算从当前文件所在目录到目标的相对路径

    Args:
        md_rel: 当前文件相对输入根的路径
        target_rel: 目标相对输入根的路径

    Returns:
        str: 相对路径（posix）
    """
    md_dir = md_rel.parent.as_posix()
    return posixpath.relpath(target_rel, md_dir)


def display_name(target: str) -> str:
    """
    生成显示名：去目录前缀与 .excalidraw.md / .excalidraw / .md 后缀

    Args:
        target: wiki 引用名

    Returns:
        str: 显示名
    """
    name = target.rsplit('/', 1)[-1].split('#', 1)[0]
    for suffix in ('.excalidraw.md', '.excalidraw', '.md'):
        if name.endswith(suffix):
            return name[:-len(suffix)]
    return name


def size_attr(size: str) -> str:
    """
    尺寸参数转 attr_list 属性（Obsidian 的 |1000 或 |500x300）

    紧贴语法（![...](...){: width=1000}）是 python-markdown attr_list 的生效形式，
    前导空格会导致 {: ...} 被渲染为纯文本。

    Args:
        size: 尺寸字符串

    Returns:
        str: '{: width=1000}' 等；无法解析时空串
    """
    s = size.strip()
    m = re.match(r'^(\d+)$', s)
    if m:
        return '{: width=' + m.group(1) + '}'
    m = re.match(r'^(\d+)[xX](\d+)$', s)
    if m:
        return '{: width=' + m.group(1) + ' height=' + m.group(2) + '}'
    return ''


def convert_text(body: str, md_rel: Path, index: dict, input_path: Path, stats: dict) -> str:
    """
    转换正文中的 wiki 语法（跳过围栏代码块）

    Args:
        body: 文件正文
        md_rel: 当前文件相对输入根的路径
        index: 全库索引
        input_path: 笔记根目录
        stats: 统计字典（含已转换/保留画布/未解析/未解析清单）

    Returns:
        str: 转换后的正文
    """
    def _convert(seg: str) -> str:
        # 混合语法 ![[a](b.png)] -> ![](b.png)
        seg = WIKI_HYBRID_RE.sub(lambda m: f'![{display_name(m.group(1))}]({m.group(2)})', seg)

        def _embed_repl(m):
            target = m.group(1)
            resolved, anchor = resolve_target(target, md_rel, index)
            if not resolved:
                stats['未解析'] += 1
                stats['未解析清单'].append((md_rel, m.group(0)))
                return m.group(0)
            rel_path = vault_rel_from(md_rel, resolved)
            size = m.group(2) or ''
            if is_excalidraw_file(input_path / resolved):
                # 画布嵌入保留 wiki 语法，目标名规范为 .excalidraw（供 Obsidian 与导出共用）
                stats['保留画布'] += 1
                target_name = Path(resolved).stem  # 例如 vector-drawing.excalidraw
                ref_target = posixpath.join(posixpath.dirname(rel_path), target_name)
                if anchor:
                    ref_target += '#' + anchor
                return f'![[{ref_target}{"|" + size.strip() if size.strip() else ""}]]'
            stats['已转换'] += 1
            if IMAGE_EXT_RE.search(resolved):
                # 图片嵌入 -> 标准图片语法
                return f'![{display_name(target)}]({rel_path}){size_attr(size)}'
            # 普通笔记嵌入 -> 转链接
            text = display_name(target)
            if anchor:
                rel_path += '#' + anchor
            return f'[{text}]({rel_path})'

        def _link_repl(m):
            target, alias = m.group(1), m.group(2)
            resolved, anchor = resolve_target(target, md_rel, index)
            if not resolved:
                stats['未解析'] += 1
                stats['未解析清单'].append((md_rel, m.group(0)))
                return m.group(0)
            rel_path = vault_rel_from(md_rel, resolved)
            text = alias.strip() if alias and alias.strip() else display_name(target)
            if anchor:
                rel_path += '#' + anchor
            return f'[{text}]({rel_path})'

        seg = WIKI_EMBED_RE.sub(_embed_repl, seg)
        seg = WIKI_LINK_RE.sub(_link_repl, seg)
        return seg

    # 按围栏代码块切分，只转换代码块外的片段
    parts = FENCE_RE.split(body)
    fence = FENCE_RE.findall(body)
    out = []
    for i, seg in enumerate(parts):
        out.append(_convert(seg))
        if i < len(fence):
            out.append(fence[i])
    return ''.join(out)


def run(input_dir: Optional[str] = None, dry_run: bool = True) -> str:
    """
    主运行函数：迁移全部 Markdown 文件的 wiki 链接

    Args:
        input_dir: 笔记根目录
        dry_run: 仅预览不写文件

    Returns:
        str: 迁移结果报告
    """
    if not input_dir:
        return "错误: 需要提供输入目录参数"
    input_path = Path(input_dir)
    if not input_path.exists():
        return f"错误: 输入目录不存在: {input_dir}"

    all_files = sorted(
        p for p in input_path.rglob('*')
        if p.is_file()
        and not any(part in EXCLUDED_DIRS for part in p.relative_to(input_path).parts[:-1])
    )
    md_files = [p for p in all_files if p.suffix == '.md']
    if not md_files:
        return f"未找到 Markdown 文件: {input_dir}"

    index = build_vault_index(all_files, input_path)
    stats = {'已转换': 0, '保留画布': 0, '未解析': 0, '未解析清单': []}
    changed = []
    for f in md_files:
        text = f.read_text(encoding='utf-8')
        new_text = convert_text(text, f.relative_to(input_path), index, input_path, stats)
        if new_text != text:
            changed.append(f)
            if not dry_run:
                f.write_text(new_text, encoding='utf-8')

    result = [
        "=" * 60,
        "Wiki 链接迁移" + ("（预览，未写文件）" if dry_run else "完成"),
        "=" * 60,
        f"输入目录: {input_path}",
        f"扫描文件: {len(md_files)} 个",
        f"转换链接: {stats['已转换']} 处",
        f"保留画布嵌入: {stats['保留画布']} 处",
        f"未解析引用: {stats['未解析']} 处（保留原样，需人工确认）",
        f"改动文件: {len(changed)} 个",
    ]
    result.append("-" * 60)
    for f in changed:
        result.append(f"  {f.relative_to(input_path)}")
    if stats['未解析清单']:
        result.append("-" * 60)
        result.append("以下引用未找到目标文件（保留原样）:")
        for md_rel, ref in stats['未解析清单']:
            result.append(f"  {md_rel}: {ref}")
    result.append("=" * 60)
    return "\n".join(result)


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description=DESCRIPTION)
    parser.add_argument('input_dir', help='笔记根目录')
    parser.add_argument('--apply', action='store_true', help='实际写文件（默认仅预览）')
    args = parser.parse_args()
    print(run(args.input_dir, dry_run=not args.apply))
