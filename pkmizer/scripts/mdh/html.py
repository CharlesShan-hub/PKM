"""
页面组装：HTML 模板、Markdown 渲染 + 组件拼接、代码块语法高亮、保存
"""

import html as html_lib
import re
import textwrap
from pathlib import Path
from typing import List

import markdown as md_lib

from .content import fix_internal_links
from .lightbox_ui import build_lightbox_script
from .nav_ui import build_nav_panel
from .theme_ui import build_theme_script
from .toc_ui import build_toc_panel

# 代码块正则：<pre><code ...>...</code></pre>（fenced_code 扩展的产物）
CODE_BLOCK_RE = re.compile(r'<pre><code(?P<attrs>[^>]*?)>(?P<code>.*?)</code></pre>', re.DOTALL)

# Obsidian/Typora 常见语言别名 -> PyGments lexer 名（空串表示不参与高亮）
LEXER_ALIASES = {
    'js': 'javascript', 'ts': 'typescript', 'py': 'python', 'sh': 'shell',
    'yml': 'yaml', 'md': 'markdown', 'latex': 'tex', 'c++': 'cpp', 'c#': 'csharp',
    'text': '', 'txt': '', 'plain': '', 'mermaid': '',
}


def _lift_indented_fences(md_text: str) -> str:
    """
    把列表项内缩进的围栏代码块提升为顶格围栏

    python-markdown 的 fenced_code 不识别列表内缩进（Tab/空格）的围栏，
    缩进围栏会退化成普通文本，块内 # 开头的行还会被误解析为标题
    （如 `\t#include <stdio.h>` 变成 <h1>）。Typora 笔记里这种写法很常见，
    转换前把缩进围栏块统一 dedent 为顶格，交给 fenced_code 正常处理。

    Args:
        md_text: 原始 Markdown 文本

    Returns:
        str: 处理后的文本（顶格围栏不变；未闭合的缩进围栏保持原样）
    """
    lines = md_text.split('\n')
    out, i, n = [], 0, len(lines)
    while i < n:
        line = lines[i]
        m = re.match(r'^([ \t]+)([`~]{3,})', line)
        if not m:
            out.append(line)
            i += 1
            continue
        fence_ch = m.group(2)[0]
        open_len = len(m.group(2))
        j = i + 1
        while j < n:
            cm = re.match(r'^[ \t]*([`~]{3,})\s*$', lines[j])
            if cm and cm.group(1)[0] == fence_ch and len(cm.group(1)) >= open_len:
                break
            j += 1
        if j >= n:
            out.append(line)
            i += 1
            continue
        block = '\n'.join(lines[i:j + 1]).expandtabs(4)
        out.append(textwrap.dedent(block))
        i = j + 1
    return '\n'.join(out)


def highlight_code_blocks(body: str) -> str:
    """
    代码块语法高亮 + 补齐 Typora 语义类

    - <pre><code class="language-x"> → <pre lang="x"><code class="language-x md-fencescode">+PyGments spans
    - md-fencescode 类让主题里 code:not(.md-fencescode)（行内代码样式）正确排除代码块
    - lang 属性让主题里 pre::before/::after（语言标签/装饰）按 Typora 语义生效
    - mermaid / 无语言 / 未知语言：仅补类与 lang，不做高亮
    - PyGments 未安装时自动降级为仅补类

    Args:
        body: 渲染后的 HTML 正文

    Returns:
        str: 处理后的 HTML
    """
    try:
        from pygments import highlight as _pyg_highlight
        from pygments.formatters import HtmlFormatter
        from pygments.lexers import TextLexer, get_lexer_by_name
        from pygments.util import ClassNotFound
        _fmt = HtmlFormatter(nowrap=True)
    except ImportError:
        _pyg_highlight, _fmt = None, None

    def _lexer(lang):
        alias = LEXER_ALIASES.get(lang, lang)
        if not alias:
            return None
        try:
            return get_lexer_by_name(alias)
        except ClassNotFound:
            return None

    def _repl(m):
        attrs, code = m.group('attrs'), m.group('code')
        lang = ''
        m_lang = re.search(r'class="language-([A-Za-z0-9_+-]+)"', attrs)
        if m_lang:
            lang = m_lang.group(1)
        # 内层 code 补 md-fencescode（Typora 语义：代码块内层类名）
        if 'class=' in attrs:
            code_attrs = re.sub(r'class="([^"]*)"', r'class="\1 md-fencescode"', attrs, count=1)
        else:
            code_attrs = ' class="md-fencescode"' + attrs
        pre_attrs = f' lang="{lang}"' if lang else ''
        if not lang or lang in ('text', 'txt', 'plain', 'mermaid') or not _pyg_highlight:
            return f'<pre{pre_attrs}><code{code_attrs}>{code}</code></pre>'
        lexer = _lexer(lang)
        if lexer is None:
            return f'<pre{pre_attrs}><code{code_attrs}>{code}</code></pre>'
        spans = _pyg_highlight(html_lib.unescape(code), lexer, _fmt)
        return f'<pre{pre_attrs}><code{code_attrs}>{spans}</code></pre>'

    return CODE_BLOCK_RE.sub(_repl, body)


# HTML 模板：占位符由 convert_to_html 用 replace 填充（避免 format 与内容里的花括号冲突）
HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>__PKM_TITLE__</title>
__PKM_THEME_LINK__
</head>
<body class="done">
__PKM_CONTENT__
__PKM_NAV__
__PKM_TOC__
__PKM_THEME_SELECT__
__PKM_THEME_SCRIPT__
__PKM_LIGHTBOX__
</body>
</html>"""


def convert_to_html(md_content: str, title: str, themes_rel: str, themes: List[str], site_tree_rel: str) -> str:
    """
    将 Markdown 内容转换为完整的 HTML 页面（含主题切换控件、全局文件树）

    Args:
        md_content: 过滤 frontmatter 后的 Markdown 正文
        title: 页面标题
        themes_rel: 到 themes/ 目录的相对路径
        themes: 主题名列表
        site_tree_rel: 到 site-tree.json 的相对路径

    Returns:
        str: 完整 HTML 内容
    """
    # toc 扩展同时负责给标题生成 id（供页面内锚点跳转）
    md = md_lib.Markdown(extensions=['extra', 'toc'])
    # 先提升列表内缩进围栏（python-markdown 不识别缩进围栏，#include 等会被误当标题）
    body = md.convert(_lift_indented_fences(md_content))

    # 代码块语法高亮（PyGments 静态着色）+ 补齐 Typora 语义类（md-fencescode / lang）
    body = highlight_code_blocks(body)

    # 渲染后修正内部链接：.md -> .html（外部链接/图片/代码块不受影响）
    body = fix_internal_links(body)

    html_out = HTML_TEMPLATE
    html_out = html_out.replace('__PKM_TITLE__', html_lib.escape(title))
    html_out = html_out.replace('__PKM_CONTENT__', body)
    html_out = html_out.replace('__PKM_NAV__', build_nav_panel(site_tree_rel))
    html_out = html_out.replace('__PKM_TOC__', build_toc_panel())

    if themes:
        default_theme = themes[0]
        theme_link = f'<link id="theme-css" rel="stylesheet" href="{themes_rel}/{default_theme}.css">'
        # 半透明圆形按钮（悬浮/点击时不透明），内置不透明 SVG 主题图标；菜单项由 JS 动态填充
        theme_select = (
            '<button id="theme-btn" type="button" aria-label="切换主题" title="切换主题">'
            '<svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">'
            '<path d="M12 3a9 9 0 1 0 0 18c1.1 0 1.5-.8 1.5-1.5S13 18 13.5 18H15a3 3 0 0 0 3-3c0-4.5-3.6-12-6-12z"/>'
            '<circle cx="7.5" cy="10.5" r="1.2"/>'
            '<circle cx="12" cy="7.5" r="1.2"/>'
            '<circle cx="16.5" cy="10.5" r="1.2"/>'
            '</svg>'
            '</button>'
            '<div id="theme-menu"></div>'
        )
        theme_script = build_theme_script(themes_rel, themes, default_theme)
    else:
        theme_link, theme_select, theme_script = '', '', ''

    html_out = html_out.replace('__PKM_THEME_LINK__', theme_link)
    html_out = html_out.replace('__PKM_THEME_SELECT__', theme_select)
    html_out = html_out.replace('__PKM_THEME_SCRIPT__', theme_script)
    html_out = html_out.replace('__PKM_LIGHTBOX__', build_lightbox_script())

    return html_out


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
