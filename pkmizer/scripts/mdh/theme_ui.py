"""
主题切换控件：半透明图标按钮 + 弹出主题菜单（页面内嵌 style/script 模板）
"""

import json
from typing import List


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
    link.onload = function () {{
      try {{ window.dispatchEvent(new Event("pkm-theme-applied")); }} catch (e) {{}}
    }};
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
