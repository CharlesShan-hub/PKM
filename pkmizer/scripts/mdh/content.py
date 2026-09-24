"""
正文内容处理：frontmatter 解析、标题提取、Markdown 文件发现、内部链接修复
"""

import posixpath
import re
import shutil
from pathlib import Path
from typing import List, Optional, Tuple

# YAML frontmatter（--- 包裹的头部元数据）
FRONTMATTER_START = '---'

# 导出时排除的目录（Obsidian 配置、git 等）
EXCLUDED_DIRS = {'.git', '.obsidian', '.trash', '.idea', '__pycache__'}

# Excalidraw 画布标记（frontmatter 里出现即视为画布资源，不导出为页面）
EXCALIDRAW_MARKERS = ('excalidraw-plugin: parsed', 'excalidraw-plugin: Parsed', 'tags: [excalidraw]')


def is_excalidraw_file(path: Path) -> bool:
    """
    判断文件是否为 Excalidraw 画布（按 frontmatter 标记，兼容 .excalidraw.md 与普通 .md 两种命名）

    Args:
        path: 待判断的文件

    Returns:
        bool: 是画布返回 True
    """
    try:
        with open(path, 'r', encoding='utf-8', errors='ignore') as f:
            head = f.read(1000)
        return any(m in head for m in EXCALIDRAW_MARKERS)
    except OSError:
        return False


def parse_frontmatter(content: str) -> Tuple[Optional[str], str]:
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
    递归查找所有 Markdown 页面文件，排除隐藏/无关目录与 Excalidraw 画布

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
        # Excalidraw 画布是资源（渲染成 SVG 被页面引用），不导出为页面
        if is_excalidraw_file(path):
            continue
        files.append(path)
    return sorted(files)


def find_excalidraw_files(input_dir: Path) -> List[Path]:
    """
    递归查找所有 Excalidraw 画布资源文件，排除隐藏/无关目录

    按 frontmatter 标记识别，兼容 .excalidraw.md 与 xxx-drawing.md 两种命名。

    Args:
        input_dir: 笔记根目录

    Returns:
        List[Path]: 画布资源文件路径列表
    """
    files = []
    for path in input_dir.rglob('*.md'):
        if any(part in EXCLUDED_DIRS for part in path.relative_to(input_dir).parts[:-1]):
            continue
        if is_excalidraw_file(path):
            files.append(path)
    return sorted(files)


# 匹配 <a ... href="..."> 的 href 值（保留原引号）
LINK_HREF_RE = re.compile(r'(<a\b[^>]*?\bhref=)(["\'])(.*?)\2')


def fix_internal_links(body: str) -> str:
    """
    把笔记内部链接的后缀 .md 改为 .html（仅相对路径链接）

    只处理 <a> 标签的 href；带协议前缀的外部链接（http/https/mailto 等）
    不动，锚点链接（.md#xxx 会正确变为 .html#xxx）。图片、代码块不受影响。

    Args:
        body: 渲染后的 HTML 正文

    Returns:
        str: 修正链接后的 HTML
    """
    def _repl(m):
        href = m.group(3)
        # 有协议前缀的是外部链接，跳过
        if re.match(r'^[a-zA-Z][a-zA-Z0-9+.\-]*:', href):
            return m.group(0)
        # 仅替换末尾的 .md 后缀（后面跟 # ? 或结束），避免误伤路径中的 .md
        new_href = re.sub(r'\.md(?=[#?]|$)', '.html', href)
        return m.group(1) + m.group(2) + new_href + m.group(2)

    return LINK_HREF_RE.sub(_repl, body)


# Obsidian wiki 语法：![[嵌入]]（画布嵌入保留处理；普通 [[链接]] 已由迁移工具改写为标准 Markdown）
WIKI_EMBED_RE = re.compile(r'!\[\[([^\]|]+)(?:\|([^\]]+))?\]\]')


def build_link_index(md_files: List[Path], excalidraw_files: List[Path], input_path: Path) -> dict:
    """
    构建 Obsidian 文件名 -> 站点相对路径 的索引，供 wiki 语法解析

    支持三种写法匹配：带路径前缀（assets/xxx）、纯文件名（xxx.md）、
    去后缀文件名（xxx）。excalidraw 画布映射到渲染出的 .svg。

    Args:
        md_files: 普通 Markdown 页面文件列表
        excalidraw_files: .excalidraw.md 画布资源文件列表
        input_path: 笔记根目录

    Returns:
        dict: key 为 Obsidian 引用名，value 为站点相对路径（html/svg）
    """
    index = {}
    for f in md_files:
        rel = f.relative_to(input_path)
        site = rel.with_suffix('.html').as_posix()
        index[f.name] = site          # xxx.md
        index[f.stem] = site          # xxx
        index[rel.as_posix()] = site  # 完整路径 a/b/c.md（供相对路径引用解析）
    for f in excalidraw_files:
        rel = f.relative_to(input_path)
        site = rel.with_suffix('.svg').as_posix()
        name = f.name
        index[name] = site                     # xxx.excalidraw.md
        if name.endswith('.excalidraw.md'):
            index[name[:-3]] = site            # xxx.excalidraw（去 .md）
            index[name[:-len('.excalidraw.md')]] = site  # xxx（去整个后缀）
        else:
            index[name[:-3]] = site            # xxx-drawing（去 .md）
        index[rel.as_posix()] = site           # 完整路径 a/b/x.excalidraw.md
        if rel.name.endswith('.excalidraw.md'):
            index[rel.with_name(rel.name[:-len('.excalidraw.md')]).as_posix()] = site  # a/b/xxx（去后缀）
            index[rel.with_name(rel.name[:-3]).as_posix()] = site                       # a/b/xxx.excalidraw
        else:
            index[rel.with_name(rel.name[:-3]).as_posix()] = site                       # a/b/xxx-drawing
    return index


def _resolve_wikilink_target(target: str, index: dict, md_rel: Path) -> Optional[str]:
    """
    按引用名解析 wiki 链接目标，返回站点相对路径（html/svg）

    - 带路径前缀（assets/x、../assets/x）：相对当前 md 所在目录解析
    - 纯文件名：按 Obsidian 语义全库同名匹配
    - 找不到返回 None，引用保留原样

    Args:
        target: wiki 引用名
        index: build_link_index 生成的索引
        md_rel: 当前 Markdown 文件相对输入根的路径

    Returns:
        Optional[str]: 站点相对路径
    """
    t = target.strip()
    if '/' not in t:
        # 纯文件名：basename 匹配（index 已含 xxx/xxx.md/xxx.excalidraw/xxx.excalidraw.md 等）
        return index.get(t)
    # 相对路径：从当前 md 所在目录解析出输入内路径
    # 试补 .md / .excalidraw / .excalidraw.md 后缀（笔记引用画布时常省略扩展名）
    md_dir = md_rel.parent.as_posix()
    base = posixpath.normpath(posixpath.join(md_dir, t))
    for cand in (base, base + '.md', base + '.excalidraw', base + '.excalidraw.md'):
        if cand in index:
            return index[cand]
    return None


def _rel_from_page(target_site_rel: str, page_rel: Path) -> str:
    """
    计算从当前页面到目标的相对路径（页面与目标均在站点根下）

    Args:
        target_site_rel: 目标相对站点根的路径（正斜杠）
        page_rel: 当前页面（即当前 md）相对输入根的路径

    Returns:
        str: 页面相对目标路径（如 ../assets/x.svg）
    """
    page_dir = list(page_rel.parent.parts)
    target = target_site_rel.split('/')
    i = 0
    while i < len(page_dir) and i < len(target) and page_dir[i] == target[i]:
        i += 1
    up = ['..'] * (len(page_dir) - i)
    parts = up + target[i:]
    return '/'.join(parts) or '.'


def _display_name(target: str) -> str:
    """
    从 wiki 引用名生成显示名：去掉目录前缀与 .md/.excalidraw 后缀

    Args:
        target: wiki 引用名（如 assets/xxx.excalidraw）

    Returns:
        str: 显示名（如 xxx）
    """
    name = target.rsplit('/', 1)[-1]
    for suffix in ('.excalidraw.md', '.excalidraw', '.md'):
        if name.endswith(suffix):
            return name[:-len(suffix)]
    return name


def convert_wikilinks(body: str, index: dict, md_rel: Path) -> str:
    """
    处理 Obsidian 画布嵌入（![[xxx.excalidraw|宽度]] -> SVG 图）

    普通 [[链接]] 已停用：源 markdown 由迁移工具改写为标准 Markdown，
    残留的 [[...]] 原样保留（渲染为纯文本），不做任何转换。

    Args:
        body: Markdown 正文（渲染前）
        index: build_link_index 生成的索引
        md_rel: 当前 Markdown 文件相对输入根的路径

    Returns:
        str: 转换后的 Markdown 正文
    """
    def _embed_repl(m):
        target = m.group(1)
        site_rel = _resolve_wikilink_target(target, index, md_rel)
        if not site_rel:
            return m.group(0)
        rel = _rel_from_page(site_rel, md_rel)
        name = _display_name(target)
        if site_rel.endswith('.svg'):
            img = f'![{name}]({rel})'
            if m.group(2):
                img += _attr_size(m.group(2).strip())
            return img
        if site_rel.endswith('.html'):
            return f'[{name}]({rel})'
        return m.group(0)

    body = WIKI_EMBED_RE.sub(_embed_repl, body)
    return body


def _attr_size(size: str) -> str:
    """
    把 Obsidian 嵌入尺寸（1000 或 500x300）转成 markdown attr_list 属性

    紧贴语法（![...](...){: width=1000}）是 python-markdown attr_list 的生效形式，
    前导空格会导致 {: ...} 被渲染为纯文本。

    Args:
        size: 尺寸字符串

    Returns:
        str: attr_list 属性片段（如 '{: width=1000}'）；无法解析时返回空串
    """
    m = re.match(r'^(\d+)$', size)
    if m:
        return '{: width=' + m.group(1) + '}'
    m = re.match(r'^(\d+)[xX](\d+)$', size)
    if m:
        return '{: width=' + m.group(1) + ' height=' + m.group(2) + '}'
    return ''


# 匹配 <img ... src="..."> 的 src 值（保留原引号）
IMG_SRC_RE = re.compile(r'<img\b[^>]*?\bsrc=(["\'])(.*?)\1')


def collect_assets(html_content: str, md_file: Path, input_path: Path, output_path: Path) -> List[Path]:
    """
    按需复制页面引用的本地资源（图片等）到站点对应位置

    只复制当前页面 <img src> 引用到的、位于输入目录内的相对路径资源，
    不整目录搬运 assets/、resources/。多个页面引用同一资源只复制一次。

    Args:
        html_content: 渲染后的 HTML（含 <img> 标签）
        md_file: 当前 Markdown 文件路径（src 相对它解析）
        input_path: 笔记根目录
        output_path: 站点根目录

    Returns:
        List[Path]: 本次新复制的站点目标路径列表
    """
    copied = []
    seen = set()
    for m in IMG_SRC_RE.finditer(html_content):
        src = m.group(2)
        # 协议前缀（http/https/data 等）或站点绝对路径不处理
        if re.match(r'^[a-zA-Z][a-zA-Z0-9+.\-]*:', src) or src.startswith('/'):
            continue
        clean = re.split(r'[?#]', src)[0]
        if not clean:
            continue
        src_path = (md_file.parent / clean).resolve()
        # 必须在输入目录内，且存在才复制
        try:
            rel = src_path.relative_to(input_path.resolve())
        except ValueError:
            continue
        if not src_path.is_file() or src_path in seen:
            continue
        seen.add(src_path)
        target = output_path / rel
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src_path, target)
        copied.append(target)
    return copied
