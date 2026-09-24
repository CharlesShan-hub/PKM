"""
Markdown to HTML Exporter
将 Markdown 笔记导出为 HTML（保留相对路径结构到站点根目录），支持动态切换 Typora 主题
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

import os
import re
import html
import json
import shutil
from pathlib import Path
from typing import List, Optional

import markdown as md_lib


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
__PKM_OUTLINE__
__PKM_THEME_SELECT__
__PKM_THEME_SCRIPT__
</body>
</html>"""

# YAML frontmatter（--- 包裹的头部元数据）
FRONTMATTER_START = '---'

# 导出时排除的目录（Obsidian 配置、git 等）
EXCLUDED_DIRS = {'.git', '.obsidian', '.trash', '.idea', '__pycache__'}

# Typora 主题目录（用于自动复制到站点根）
TYPORA_THEMES_DIR = Path(os.environ.get('APPDATA', '')) / 'Typora' / 'themes'

# Typora CSS 适配规则：把 Typora 预览 DOM 的选择器映射到标准 HTML 元素
# 注意：
#  - 规则有顺序依赖（.md-fences 先于 .md-focus，避免并列类被拆散）
#  - 子目录 CSS（皮肤 @import 的样式文件）同样会被适配
#  - 以正则词边界匹配，避免误伤复合类名（如 .md-focus-container）
#  - 规则更新后把 ADAPT_MARKER 版本号 +1，旧文件会自动重新适配
THEME_ADAPT_RULES = [
    (r'#write', 'body'),           # 正文容器（宽度、内边距等）
    (r'\.md-fences', 'pre'),       # 代码块
    (r'\.md-fenced-code', 'pre'),  # 代码块（部分主题用）
    (r'\.md-task-list-item', 'li'),  # 任务列表项
    (r'\.md-list-item', 'li'),     # 列表项（phycat 等主题用）
    (r'\.md-meta-block', ''),      # frontmatter 代码块（pre.md-meta-block → pre）
    (r'\.md-heading', ''),         # 标题装饰类（h3.md-heading:after → h3:after）
    (r'\.md-focus', ':focus'),     # 聚焦标题（md-focus → :focus，保持 :not() 有效）
    (r'\.typora-export body', 'body'),  # Typora 导出专用容器（深色主题背景在此定义）
    (r'content>body', 'body'),     # vlook 主题的导出容器
]
# 适配标记：带版本号。规则更新后把版本号 +1，旧文件会自动重新适配（幂等）。
ADAPT_MARKER = '/* adapted by pkmizer v2 */'


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

    return ADAPT_MARKER + '\n' + css


def adapt_themes_dir(themes_dir: Path) -> int:
    """
    适配 themes 目录下所有 CSS 文件

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
            new_content = adapt_theme_css(content)
            if new_content != content:
                with open(css_file, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                adapted += 1
                print(f"已适配主题: {css_file.relative_to(themes_dir)}")
        except Exception as e:
            print(f"适配主题失败 {css_file.relative_to(themes_dir)}: {e}")
    return adapted


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


def build_theme_script(themes_rel: str, themes: List[str], default_theme: str) -> str:
    """
    构建主题切换控件：半透明图标按钮 + 弹出主题菜单
    （按钮半透明，悬浮/点击时不透明；图标始终不透明）

    Args:
        themes_rel: 到 themes/ 目录的相对路径
        themes: 主题名列表
        default_theme: 默认主题名

    Returns:
        str: <style> + <script> 内容
    """
    themes_json = json.dumps(themes)
    return f"""<style>
#theme-btn {{
  position: fixed; top: 10px; right: 10px; z-index: 1000;
  width: 38px; height: 38px; border-radius: 50%;
  background: rgba(127,127,127,.3);
  -webkit-backdrop-filter: blur(4px); backdrop-filter: blur(4px);
  display: flex; align-items: center; justify-content: center;
  cursor: pointer; transition: background .2s ease;
  border: 1px solid rgba(255,255,255,.25);
}}
#theme-btn:hover, #theme-btn.open {{
  background: rgba(0,0,0,.7); border-color: rgba(255,255,255,.5);
}}
#theme-btn svg {{
  width: 20px; height: 20px; fill: none; stroke: #fff; stroke-width: 1.8;
  stroke-linecap: round; stroke-linejoin: round;
  filter: drop-shadow(0 1px 2px rgba(0,0,0,.6));
}}
#theme-menu {{
  position: fixed; top: 56px; right: 10px; z-index: 1000;
  display: none; min-width: 160px; max-height: 70vh; overflow-y: auto;
  background: rgba(255,255,255,.95);
  -webkit-backdrop-filter: blur(8px); backdrop-filter: blur(8px);
  border-radius: 10px; box-shadow: 0 4px 20px rgba(0,0,0,.2);
  padding: 6px; font-size: 13px; font-family: Arial, sans-serif;
}}
#theme-menu.open {{ display: block; }}
.theme-item {{
  padding: 6px 10px; border-radius: 6px; cursor: pointer;
  color: #333; white-space: nowrap;
}}
.theme-item:hover {{ background: rgba(0,0,0,.08); }}
.theme-item.active {{ background: rgba(0,0,0,.15); font-weight: 600; }}
</style>
<script>
(function () {{
  var themes = {themes_json};
  var base = "{themes_rel}/";
  var link = document.getElementById("theme-css");
  var btn = document.getElementById("theme-btn");
  var menu = document.getElementById("theme-menu");
  var saved = null;
  try {{ saved = localStorage.getItem("pkm-theme"); }} catch (e) {{}}
  var current = (saved && themes.indexOf(saved) > -1) ? saved : "{default_theme}";
  themes.forEach(function (name) {{
    var item = document.createElement("div");
    item.className = "theme-item";
    item.textContent = name;
    item.addEventListener("click", function () {{ apply(name); hide(); }});
    menu.appendChild(item);
  }});
  var apply = function (name) {{
    current = name;
    link.href = base + name + ".css";
    try {{ localStorage.setItem("pkm-theme", name); }} catch (e) {{}}
    refreshActive();
  }};
  var refreshActive = function () {{
    var items = menu.querySelectorAll(".theme-item");
    for (var i = 0; i < items.length; i++) {{
      items[i].classList.toggle("active", items[i].textContent === current);
    }}
  }};
  var show = function () {{ menu.classList.add("open"); btn.classList.add("open"); }};
  var hide = function () {{ menu.classList.remove("open"); btn.classList.remove("open"); }};
  btn.addEventListener("click", function () {{
    if (menu.classList.contains("open")) {{ hide(); }} else {{ show(); }}
  }});
  document.addEventListener("click", function (e) {{
    if (!btn.contains(e.target) && !menu.contains(e.target)) {{ hide(); }}
  }});
  apply(current);
}})();
</script>"""


def build_outline_tree(tokens: List[dict]) -> str:
    """
    递归生成大纲树 HTML（嵌套 ul/li，有子级的项带折叠箭头）

    Args:
        tokens: markdown toc 扩展输出的标题树（含 level/id/name/children）

    Returns:
        str: 嵌套列表 HTML
    """
    if not tokens:
        return ''
    items = []
    for tok in tokens:
        name = html.escape(tok.get('name', ''))
        tid = tok.get('id', '')
        children = build_outline_tree(tok.get('children', []))
        if children:
            items.append(
                f'<li class="has-sub" data-id="{tid}">'
                f'<span class="outline-toggle" title="折叠/展开"></span>'
                f'<a href="#{tid}">{name}</a><ul>{children}</ul></li>'
            )
        else:
            items.append(f'<li data-id="{tid}"><a href="#{tid}">{name}</a></li>')
    return ''.join(items)


def build_outline_panel(toc_tokens: List[dict]) -> str:
    """
    构建左侧大纲面板：半透明图标按钮 + 可折叠标题树 + 滚动高亮当前章节

    面板默认收起，点左上角按钮展开；点标题平滑滚动到对应章节。

    Args:
        toc_tokens: markdown toc 扩展输出的标题树

    Returns:
        str: 完整面板 HTML（含样式与脚本）；无标题时返回空串
    """
    tree = build_outline_tree(toc_tokens)
    if not tree:
        return ''
    return f"""<style>
#outline-btn {{
  position: fixed; top: 10px; left: 10px; z-index: 1000;
  width: 38px; height: 38px; border-radius: 50%;
  background: rgba(127,127,127,.3);
  -webkit-backdrop-filter: blur(4px); backdrop-filter: blur(4px);
  display: flex; align-items: center; justify-content: center;
  cursor: pointer; transition: background .2s ease;
  border: 1px solid rgba(255,255,255,.25);
}}
#outline-btn:hover, #outline-btn.open {{
  background: rgba(0,0,0,.7); border-color: rgba(255,255,255,.5);
}}
#outline-btn svg {{
  width: 20px; height: 20px; fill: none; stroke: #fff; stroke-width: 1.8;
  stroke-linecap: round; stroke-linejoin: round;
  filter: drop-shadow(0 1px 2px rgba(0,0,0,.6));
}}
#outline-panel {{
  position: fixed; top: 0; left: 0; bottom: 0; z-index: 999;
  width: 260px; transform: translateX(-100%);
  transition: transform .25s ease;
  background: rgba(255,255,255,.95);
  -webkit-backdrop-filter: blur(8px); backdrop-filter: blur(8px);
  box-shadow: 2px 0 16px rgba(0,0,0,.18);
  display: flex; flex-direction: column;
  font-size: 13px; font-family: Arial, sans-serif;
}}
#outline-panel.open {{ transform: translateX(0); }}
#outline-panel .outline-head {{
  padding: 14px 16px 10px; font-size: 14px; font-weight: 600;
  color: #555; border-bottom: 1px solid rgba(0,0,0,.08);
}}
#outline-panel .outline-tree {{
  flex: 1; overflow-y: auto; padding: 8px 8px 24px; margin: 0;
  list-style: none; box-sizing: border-box;
}}
#outline-panel ul {{ list-style: none; margin: 0; padding: 0; }}
#outline-panel li {{ position: relative; padding-left: 14px; }}
#outline-panel li a {{
  display: block; padding: 4px 6px; margin: 1px 0;
  border-radius: 5px; color: #444; text-decoration: none;
  white-space: nowrap; overflow: hidden; text-overflow: ellipsis;
  line-height: 1.45;
}}
#outline-panel li a:hover {{ background: rgba(0,0,0,.06); }}
#outline-panel li a.active {{
  background: rgba(0,0,0,.1); color: #111; font-weight: 600;
}}
.outline-toggle {{
  position: absolute; left: 0; top: 5px; width: 14px; height: 14px;
  cursor: pointer; color: #888; text-align: center; line-height: 14px;
  font-size: 10px; user-select: none;
}}
.outline-toggle::before {{ content: "▾"; }}
li.collapsed > ul {{ display: none; }}
li.collapsed > .outline-toggle::before {{ content: "▸"; }}
</style>
<button id="outline-btn" type="button" aria-label="大纲" title="大纲">
<svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
<path d="M4 5h16v2H4zM4 11h16v2H4zM4 17h10v2H4z"/>
</svg>
</button>
<div id="outline-panel">
<div class="outline-head">大纲</div>
<ul class="outline-tree">{tree}</ul>
</div>
<script>
(function () {{
  var btn = document.getElementById("outline-btn");
  var panel = document.getElementById("outline-panel");
  if (!btn || !panel) return;
  var toggle = function () {{
    panel.classList.toggle("open");
    btn.classList.toggle("open");
  }};
  btn.addEventListener("click", function (e) {{ e.stopPropagation(); toggle(); }});
  document.addEventListener("click", function (e) {{
    if (panel.classList.contains("open") &&
        !panel.contains(e.target) && e.target !== btn) toggle();
  }});
  var setActive = function (id) {{
    var items = panel.querySelectorAll("li");
    for (var i = 0; i < items.length; i++) {{
      var a = items[i].querySelector("a");
      if (!a) continue;
      if (items[i].getAttribute("data-id") === id) {{
        a.classList.add("active");
        var p = items[i].parentElement;
        while (p && p.closest) {{
          p = p.closest("li");
          if (p) p.classList.remove("collapsed");
        }}
      }} else {{
        a.classList.remove("active");
      }}
    }}
  }};
  panel.querySelectorAll("li.has-sub > .outline-toggle").forEach(function (t) {{
    t.addEventListener("click", function (e) {{
      e.stopPropagation();
      t.parentElement.classList.toggle("collapsed");
    }});
  }});
  panel.querySelectorAll("li a").forEach(function (a) {{
    a.addEventListener("click", function (e) {{
      var id = a.getAttribute("href").slice(1);
      var el = document.getElementById(decodeURIComponent(id));
      if (el) {{
        e.preventDefault();
        el.scrollIntoView({{ behavior: "smooth", block: "start" }});
        setActive(id);
      }}
    }});
  }});
  if ("IntersectionObserver" in window) {{
    var heads = document.querySelectorAll("h1[id],h2[id],h3[id],h4[id],h5[id],h6[id]");
    var io = new IntersectionObserver(function (entries) {{
      entries.forEach(function (en) {{
        if (en.isIntersecting) setActive(en.target.id);
      }});
    }}, {{ rootMargin: "-15% 0px -75% 0px" }});
    heads.forEach(function (h) {{ io.observe(h); }});
  }}
}})();
</script>"""


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


def convert_to_html(md_content: str, title: str, themes_rel: str, themes: List[str]) -> str:
    """
    将 Markdown 内容转换为完整的 HTML 页面（含主题切换控件、左侧大纲）

    Args:
        md_content: 过滤 frontmatter 后的 Markdown 正文
        title: 页面标题
        themes_rel: 到 themes/ 目录的相对路径
        themes: 主题名列表

    Returns:
        str: 完整 HTML 内容
    """
    # toc 扩展同时负责给标题生成 id（供大纲锚点跳转）并输出标题树
    md = md_lib.Markdown(extensions=['extra', 'toc'])
    body = md.convert(md_content)
    toc_tokens = md.toc_tokens

    # 渲染后修正内部链接：.md -> .html（外部链接/图片/代码块不受影响）
    body = fix_internal_links(body)

    html_out = HTML_TEMPLATE
    html_out = html_out.replace('__PKM_TITLE__', html.escape(title))
    html_out = html_out.replace('__PKM_CONTENT__', body)
    html_out = html_out.replace('__PKM_OUTLINE__', build_outline_panel(toc_tokens))

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


def run(input_dir: Optional[str] = None, output_dir: Optional[str] = None) -> str:
    """
    主运行函数：全量导出

    扫描输入目录下所有 .md 文件，转换为 HTML 并写入站点根目录（默认 dist），
    保留相对路径结构。站点根下自动准备 themes/（优先从 Typora 复制），
    每个页面内置主题切换控件。

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

            # 计算到 themes/ 的相对路径，转换并保存
            rel_path = md_file.relative_to(input_path).with_suffix('.html')
            themes_rel = themes_relative_path(rel_path)
            html_content = convert_to_html(body, title, themes_rel, themes)
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
        f"站点根目录: {output_path}",
        f"主题目录: {themes_dir}",
        f"可用主题: {len(themes)} 个（{', '.join(themes[:5])}{'...' if len(themes) > 5 else ''}）",
        f"适配主题: {adapted_count} 个（Typora 选择器已映射到标准 HTML）",
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
