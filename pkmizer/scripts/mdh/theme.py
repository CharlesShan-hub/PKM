"""
主题系统：Typora 主题 CSS 适配、主题目录准备与扫描、相对路径计算
"""

import os
import re
import shutil
from pathlib import Path
from typing import List

# Typora 主题目录（用于自动复制到站点根）
TYPORA_THEMES_DIR = Path(os.environ.get('APPDATA', '')) / 'Typora' / 'themes'

# Typora CSS 适配规则：把 Typora 预览 DOM 的选择器映射到标准 HTML 元素
# 注意：
#  - 规则有顺序依赖（pre.md-fences 先于 .md-fences，避免拼成无效的 prepre）
#  - 子目录 CSS（皮肤 @import 的样式文件）同样会被适配
#  - 以正则词边界匹配，避免误伤复合类名（如 .md-focus-container）
#  - 规则更新后把 ADAPT_MARKER 版本号 +1，旧文件会自动重新适配
THEME_ADAPT_RULES = [
    (r'pre\.md-fences', 'pre'),      # 代码块容器（pre.md-fences → pre）
    (r'#write', 'body'),             # 正文容器（宽度、内边距等）
    (r'\.md-fences', 'pre'),         # 代码块（孤立 .md-fences → pre）
    (r'\.md-fenced-code', 'pre'),    # 代码块（部分主题用）
    (r'\.md-task-list-item', 'li'),  # 任务列表项
    (r'\.md-list-item', 'li'),       # 列表项（phycat 等主题用）
    (r'\.md-heading', ''),           # 标题装饰类（h3.md-heading:after → h3:after）
    (r'\.md-focus', ':focus'),       # 聚焦标题（md-focus → :focus，保持 :not() 有效）
    (r'\.typora-export body', 'body'),  # Typora 导出专用容器（深色主题背景在此定义）
    (r'content>body', 'body'),       # vlook 主题的导出容器
]
# 说明：.md-meta-block（YAML frontmatter 块）不参与适配。frontmatter 在导出时被剥离，
# 页面里不存在该元素；若把 pre.md-meta-block 适配成 pre，会导致主题里 frontmatter 专属的
# ::after 徽章 / hover 动画泄漏到所有普通代码块上（如 phycat 的 "YAML" 徽章）。
# 适配标记：带版本号。规则更新后把版本号 +1，旧文件会自动重新适配（幂等）。
ADAPT_MARKER = '/* adapted by pkmizer v4 */'
# 旧版本适配标记（用于识别需要从 Typora 源恢复后再重适配的文件）
ANY_ADAPT_MARKER = 'adapted by pkmizer'

# CodeMirror token 类名 -> Pygments token 类名（语法高亮配色翻译表）
# Typora 主题用 .cm-* 定义代码配色，PyGments 输出用 .k/.s/.m 等短类名。
# 适配时把主题里已有的 cm 配色翻译成 PyGments 类，代码块颜色与 Typora 一致。
CM_TO_PYGMENTS = {
    'keyword':    ['k', 'kd', 'kn', 'kp', 'kr'],
    'builtin':    ['nb', 'bp'],
    'type':       ['kt'],
    'variable':   ['n', 'nx', 'nv', 'nc', 'nn', 'nl', 'ni'],
    'variable-2': ['n', 'nx', 'nv'],
    'variable-3': ['n', 'nx', 'nv'],
    'def':        ['nf', 'na'],
    'attribute':  ['na', 'nd'],
    'property':   ['py'],
    'operator':   ['o', 'ow'],
    'string':     ['s', 's1', 's2', 'sb', 'sc', 'se', 'sh', 'si', 'sr', 'ss', 'sx', 'sd'],
    'number':     ['m', 'mi', 'mf', 'mh', 'mb', 'mo', 'il'],
    'comment':    ['c', 'c1', 'cm', 'cp', 'cs'],
    'atom':       ['kc'],
    'tag':        ['nt'],
    'meta':       ['ni'],
    'link':       ['sr'],
    'error':      ['err'],
}


def _extract_cm_colors(css: str) -> dict:
    """
    从主题 CSS 提取 CodeMirror token 配色（类名 -> "color: ...; font-weight: ..." 声明）

    用花括号配对遍历，跳过 @media 等嵌套块，只收集顶层规则里 .cm-* 类的颜色声明。

    Args:
        css: CSS 内容

    Returns:
        dict: cm 类名 -> 样式声明串
    """
    colors = {}
    i, n = 0, len(css)
    while i < n:
        start = css.find('{', i)
        if start < 0:
            break
        depth = 1
        j = start + 1
        while j < n and depth:
            if css[j] == '{':
                depth += 1
            elif css[j] == '}':
                depth -= 1
            j += 1
        selector = css[i:start]
        if '.cm-' in selector and not selector.strip().startswith('@'):
            decl = css[start:j]
            color = re.search(r'color\s*:\s*([^;}]+)', decl)
            if color:
                style = 'color: ' + color.group(1).strip()
                weight = re.search(r'font-weight\s*:\s*([^;}]+)', decl)
                if weight:
                    style += '; font-weight: ' + weight.group(1).strip()
                for cm in set(re.findall(r'\.cm-([A-Za-z0-9_-]+)', selector)):
                    colors[cm] = style
        i = j
    return colors


def _build_syntax_css(css: str) -> str:
    """
    生成语法高亮 CSS：把主题的 CodeMirror 配色翻译成 PyGments token 类

    主题没有 cm 配色规则时返回空串（代码块保持主题默认文字色）。

    Args:
        css: 适配后的主题 CSS

    Returns:
        str: 追加到主题文件末尾的语法高亮 CSS 段（无配色时为空串）
    """
    emitted = {}
    for cm_name, pyg_classes in CM_TO_PYGMENTS.items():
        style = _extract_cm_colors(css).get(cm_name)
        if not style:
            continue
        for c in pyg_classes:
            if c not in emitted:
                emitted[c] = style
    if not emitted:
        return ''
    lines = ['/* pkmizer syntax highlight: 颜色取自本主题 CodeMirror 配色 */']
    for c in sorted(emitted):
        lines.append(f'pre code .{c} {{ {emitted[c]} }}')
    return '\n'.join(lines) + '\n'


def adapt_theme_css(css: str) -> str:
    """
    适配单份 Typora 主题 CSS，幂等（已适配的跳过）

    Args:
        css: 原始 CSS 内容

    Returns:
        str: 适配后的 CSS 内容
    """
    if ADAPT_MARKER in css:
        return css

    # 词边界匹配：.md-focus 后跟 [-A-Za-z0-9] 时视为复合类名（如 .md-focus-container），不替换
    for old, new in THEME_ADAPT_RULES:
        css = re.sub(old + r'(?![-A-Za-z0-9])', new, css)

    # 深色主题整页背景同步：正文背景用 var(--bg-color) 时，html 也应用同色
    # （Typora 导出样式的 body 是居中卡片，两侧页面背景需要一起变深色）
    if re.search(r'body\s*\{[^}]*background(?:-color)?\s*:\s*var\(--bg-color\)', css):
        css = 'html { background-color: var(--bg-color); }\n' + css

    # 追加语法高亮配色（翻译主题自带 CodeMirror 配色 -> PyGments token 类）
    syntax_css = _build_syntax_css(css)
    if syntax_css:
        css = css.rstrip() + '\n\n' + syntax_css

    return ADAPT_MARKER + '\n' + css


def _restore_from_typora(themes_dir: Path, css_file: Path) -> str:
    """
    从 Typora 原始主题目录恢复某个主题文件的原始内容

    pkm-out/themes 是 Typora themes 的完整副本，旧版本适配产物（如 v2 的
    prepre）无法通过叠加适配修复，需先还原原始文件再按新规则重适配。

    Args:
        themes_dir: 站点 themes 目录
        css_file: 待恢复的主题文件

    Returns:
        str: 原始内容；Typora 源中没有该文件（用户手动放入）时返回空串
    """
    rel = css_file.relative_to(themes_dir)
    src = TYPORA_THEMES_DIR / rel
    if src.exists() and src.is_file():
        return src.read_text(encoding='utf-8')
    return ''


def adapt_themes_dir(themes_dir: Path) -> int:
    """
    适配 themes 目录下所有 CSS 文件

    带旧版本适配标记的文件（说明是 pkmizer 的产物）会先从 Typora 源恢复
    原始内容再按当前规则重新适配，保证规则升级后能彻底修复。

    Args:
        themes_dir: themes 目录

    Returns:
        int: 本次适配的文件数
    """
    adapted = 0
    for css_file in themes_dir.rglob('*.css'):
        try:
            with open(css_file, 'r', encoding='utf-8') as f:
                content = f.read()
            # 旧版本适配标记的文件：先恢复原始内容，再按新规则重新适配
            if ADAPT_MARKER not in content and ANY_ADAPT_MARKER in content:
                restored = _restore_from_typora(themes_dir, css_file)
                if restored:
                    content = restored
                    print(f"已从 Typora 恢复原始主题: {css_file.relative_to(themes_dir)}")
            new_content = adapt_theme_css(content)
            if new_content != content:
                with open(css_file, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                adapted += 1
                print(f"已适配主题: {css_file.relative_to(themes_dir)}")
        except Exception as e:
            print(f"适配主题失败 {css_file.relative_to(themes_dir)}: {e}")
    return adapted


def ensure_themes_dir(site_root: Path) -> Path:
    """
    确保站点根目录下有 themes/ 目录

    目录不存在时，优先从 Typora 主题目录自动复制；复制不到则创建空目录。

    Args:
        site_root: 站点根目录

    Returns:
        Path: themes 目录路径
    """
    themes_dir = site_root / 'themes'
    if themes_dir.exists():
        return themes_dir

    if TYPORA_THEMES_DIR.exists() and TYPORA_THEMES_DIR.is_dir():
        shutil.copytree(TYPORA_THEMES_DIR, themes_dir)
        print(f"已从 Typora 复制主题: {TYPORA_THEMES_DIR} -> {themes_dir}")
    else:
        themes_dir.mkdir(parents=True, exist_ok=True)
        print(f"未找到 Typora 主题目录，已创建空 themes/（可手动放入 .css 主题文件）")

    return themes_dir


def scan_themes(themes_dir: Path) -> List[str]:
    """
    扫描 themes 目录下的主题名（不含 .css 后缀）

    Args:
        themes_dir: themes 目录

    Returns:
        List[str]: 排序后的主题名列表
    """
    if not themes_dir.exists():
        return []
    return sorted(p.stem for p in themes_dir.glob("*.css"))


def themes_relative_path(rel_path: Path) -> str:
    """
    计算从导出 HTML 文件位置到 themes/ 目录的相对路径

    Args:
        rel_path: HTML 文件相对于站点根目录的路径

    Returns:
        str: 相对路径（如 themes、../themes）
    """
    depth = len(rel_path.parts) - 1
    prefix = '/'.join(['..'] * depth)
    return f"{prefix}/themes" if prefix else "themes"
