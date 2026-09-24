"""
Markdown to HTML Exporter
将 Markdown 笔记导出为 HTML（保留相对路径结构到站点根目录），支持动态切换 Typora 主题

本文件是入口（供 GUI 与命令行加载），具体实现拆在 mdh/ 子包：
  content.py    - 正文处理（frontmatter/标题/链接修复）
  theme.py      - 主题适配与发现
  ui_bundle.py  - 站点级 UI（主题切换/文件树/TOC/图片放大，合成 ui.css/ui.js）
  nav.py        - 全站文件树数据
  html.py       - 页面组装与保存
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
import shutil
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
from mdh.ui_bundle import build_ui_css, build_ui_js

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

    # 站点级 UI 资源（主题切换/文件树/TOC/图片放大），页面引用外部文件避免重复内联
    (output_path / 'ui.css').write_text(build_ui_css(), encoding='utf-8')
    (output_path / 'ui.js').write_text(build_ui_js(), encoding='utf-8')

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

    # 站点首页：仓库根 README.md（若有）生成 index.html 作为入口
    readme_path = input_path.parent / 'README.md'
    if readme_path.exists():
        try:
            readme_body = strip_frontmatter(readme_path.read_text(encoding='utf-8'))
            readme_body = convert_wikilinks(readme_body, link_index, Path('index.md'))
            readme_title = extract_title(readme_body, 'README')
            readme_html = convert_to_html(readme_body, readme_title, 'themes/', themes, 'site-tree.json')
            # README 链接带仓库根前缀 pkm/，在站点根需去掉（.md 后缀转换时已改为 .html）
            readme_html = re.sub(r'(<a[^>]*?href=")pkm/', r'\1', readme_html)
            # 首页所有链接新标签页打开，主页播放的歌曲不因跳转中断
            readme_html = re.sub(r'<a([^>]*?)href="', r'<a\1target="_blank" href="', readme_html)
            # 背景音乐播放器（右下角悬浮）：主按钮播放/暂停，歌单按钮选曲，默认单曲循环
            # 歌单自动扫描站点 assets/ 目录的音频文件，后续往 assets 丢歌即可自动出现在列表
            assets_dir = output_path / 'assets'
            bgm_files = []
            if assets_dir.exists():
                bgm_files = sorted(
                    (p for p in assets_dir.iterdir() if p.is_file() and p.suffix.lower() in ('.mp3', '.m4a', '.ogg', '.wav')),
                    key=lambda p: p.name.lower(),
                )
            bgm_items = ''.join(
                f'<div class="bgm-item" data-src="assets/{p.name}">{p.stem}</div>' for p in bgm_files
            )
            music_box = '''
<div id="bgm-box">
<audio id="bgm" preload="none" loop></audio>
<button id="bgm-btn" type="button" aria-label="背景音乐" title="背景音乐">
  <svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path d="M12 3v10.55A4 4 0 1 0 14 17V7h4V3h-6z"/></svg>
</button>
<button id="bgm-list-btn" type="button" aria-label="选择歌曲" title="选择歌曲">
  <svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path d="M4 6h16v2H4zM4 11h16v2H4zM4 16h10v2H4z"/></svg>
</button>
<div id="bgm-menu">
__BGM_ITEMS__
</div>
<style>
#bgm-btn,#bgm-list-btn{position:fixed;bottom:26px;width:46px;height:46px;border-radius:50%;border:none;cursor:pointer;background:rgba(0,0,0,.35);backdrop-filter:blur(6px);display:flex;align-items:center;justify-content:center;transition:background .2s,transform .15s;z-index:999;box-shadow:0 2px 10px rgba(0,0,0,.15)}
#bgm-btn{right:26px}
#bgm-list-btn{right:82px}
#bgm-btn:hover,#bgm-list-btn:hover{background:rgba(0,0,0,.6);transform:scale(1.06)}
#bgm-btn svg{fill:#fff;width:22px;height:22px}
#bgm-list-btn svg{fill:#fff;width:20px;height:20px}
#bgm-btn.playing svg{animation:bgm-spin 4s linear infinite}
@keyframes bgm-spin{from{transform:rotate(0)}to{transform:rotate(360deg)}}
#bgm-menu{position:fixed;right:82px;bottom:80px;z-index:999;display:none;min-width:160px;max-height:56vh;overflow-y:auto;background:rgba(0,0,0,.55);backdrop-filter:blur(8px);border-radius:10px;box-shadow:0 4px 20px rgba(0,0,0,.25);padding:6px;font-size:13px;font-family:Arial,sans-serif;color:#eee}
#bgm-menu.open{display:block}
#bgm-menu .bgm-item{padding:6px 10px;border-radius:6px;cursor:pointer;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
#bgm-menu .bgm-item:hover{background:rgba(255,255,255,.12)}
#bgm-menu .bgm-item.active{background:rgba(255,255,255,.22);font-weight:600}
#bgm-menu .bgm-empty{padding:6px 10px;color:rgba(255,255,255,.6)}
</style>
<script>
(function(){var a=document.getElementById('bgm'),b=document.getElementById('bgm-btn'),lb=document.getElementById('bgm-list-btn'),m=document.getElementById('bgm-menu'),items=m.querySelectorAll('.bgm-item'),p=false,cur=null;
a.loop=true;
if(!items.length){b.style.display='none';lb.style.display='none';return;}
var pick=function(src){cur=src;a.src=src;for(var i=0;i<items.length;i++){items[i].classList.toggle('active',items[i].getAttribute('data-src')===src);}};
pick(items[0].getAttribute('data-src'));
b.addEventListener('click',function(){if(p){a.pause();b.classList.remove('playing')}else{var q=a.play();if(q!==undefined){q.catch(function(){})}b.classList.add('playing')}p=!p});
lb.addEventListener('click',function(e){e.stopPropagation();m.classList.toggle('open');lb.classList.toggle('open')});
document.addEventListener('click',function(e){if(m.classList.contains('open')&&!m.contains(e.target)&&e.target!==lb){m.classList.remove('open');lb.classList.remove('open')}});
for(var i=0;i<items.length;i++){items[i].addEventListener('click',function(){var s=this.getAttribute('data-src');if(cur!==s){pick(s);if(p){var q=a.play();if(q!==undefined){q.catch(function(){})}}}m.classList.remove('open');lb.classList.remove('open')});}
})();
</script>
</div>'''.replace('__BGM_ITEMS__', bgm_items)
            readme_html = re.sub(r'(<body[^>]*>)', r'\1' + music_box, readme_html, count=1)
            # 复制 README 引用的本地图片（相对仓库根 input_path.parent）到站点根
            for src in re.findall(r'<img[^>]*?src="([^"]+)"', readme_html):
                if src.startswith(('http:', 'https:', 'data:')):
                    continue
                src_path = (input_path.parent / src.lstrip('./')).resolve()
                if src_path.exists():
                    dest = output_path / src.lstrip('./')
                    dest.parent.mkdir(parents=True, exist_ok=True)
                    shutil.copy2(src_path, dest)
            save_html(readme_html, output_path / 'index.html')
            exported.append(Path('index.html'))
            print("站点首页: README.md -> index.html")
        except Exception as e:
            errors.append(f"README.md: {str(e)}")

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
