"""
左侧全局文件树导航面板：半透明图标按钮 + 可折叠全站文件树（内嵌 style/script 模板）
"""


def build_nav_panel(site_tree_rel: str) -> str:
    """
    构建左侧全局文件树导航：半透明图标按钮 + 可折叠全站文件树

    文件树数据来自导出时生成的 site-tree.json（全站共用一份），
    页面加载时异步拉取，浏览器缓存后切换页面零重复下载。

    Args:
        site_tree_rel: 当前页面到 site-tree.json 的相对路径

    Returns:
        str: 完整导航面板 HTML（含样式与脚本）
    """
    return f"""<style>
#nav-btn {{
  position: fixed; top: 10px; left: 10px; z-index: 1000;
  width: 38px; height: 38px; border-radius: 50%;
  background: rgba(127,127,127,.3);
  -webkit-backdrop-filter: blur(4px); backdrop-filter: blur(4px);
  display: flex; align-items: center; justify-content: center;
  cursor: pointer; transition: background .2s ease;
  border: 1px solid rgba(255,255,255,.25);
}}
#nav-btn:hover, #nav-btn.open {{
  background: rgba(0,0,0,.7); border-color: rgba(255,255,255,.5);
}}
#nav-btn svg {{
  width: 20px; height: 20px; fill: none; stroke: #fff; stroke-width: 1.8;
  stroke-linecap: round; stroke-linejoin: round;
  filter: drop-shadow(0 1px 2px rgba(0,0,0,.6));
}}
#nav-panel {{
  position: fixed; top: 0; left: 0; bottom: 0; z-index: 999;
  width: 260px; transform: translateX(-100%);
  visibility: hidden;
  /* 收回时 transform 动画结束后再隐藏，避免移出后边缘残留 1px 竖线 */
  transition: transform .25s ease, visibility 0s .25s;
  background: var(--nav-bg, rgba(255,255,255,.95));
  color: var(--nav-fg, #555);
  -webkit-backdrop-filter: blur(8px); backdrop-filter: blur(8px);
  box-shadow: 2px 0 16px rgba(0,0,0,.18);
  display: flex; flex-direction: column;
  font-size: 13px; font-family: Arial, sans-serif;
}}
#nav-panel.open {{
  transform: translateX(0);
  visibility: visible;
  transition: transform .25s ease, visibility 0s;
}}
#nav-panel .nav-head {{
  padding: 14px 16px 10px; font-size: 14px; font-weight: 600;
  color: var(--nav-fg, #555);
  border-bottom: 1px solid color-mix(in srgb, var(--nav-fg, #555) 14%, transparent);
}}
#nav-panel .nav-tree {{
  flex: 1; overflow-y: auto; padding: 8px 8px 24px; margin: 0;
  list-style: none; box-sizing: border-box;
}}
#nav-panel ul {{ list-style: none; margin: 0; padding: 0 0 0 14px; }}
#nav-panel .nav-dir {{
  padding: 2px 0; cursor: pointer; color: var(--nav-fg, #555);
  white-space: nowrap; overflow: hidden; text-overflow: ellipsis;
}}
#nav-panel .nav-dir-label::before {{
  content: "▾"; display: inline-block; width: 14px;
  color: color-mix(in srgb, var(--nav-fg, #555) 60%, transparent);
  font-size: 10px; vertical-align: 1px;
}}
#nav-panel .nav-dir.collapsed > .nav-dir-label::before {{ content: "▸"; }}
#nav-panel .nav-dir.collapsed > ul {{ display: none; }}
#nav-panel .nav-dir-label:hover {{ color: var(--nav-fg, #111); }}
#nav-panel .nav-file {{
  display: block; padding: 3px 6px; margin: 1px 0;
  border-radius: 5px; color: var(--nav-fg, #444); text-decoration: none;
  white-space: nowrap; overflow: hidden; text-overflow: ellipsis;
  line-height: 1.45;
}}
#nav-panel .nav-file:hover {{
  background: color-mix(in srgb, var(--nav-fg, #555) 9%, transparent);
}}
#nav-panel .nav-file.active {{
  background: color-mix(in srgb, var(--nav-fg, #555) 16%, transparent);
  color: var(--nav-fg, #111); font-weight: 600;
}}
#nav-panel .nav-empty {{
  padding: 8px; color: color-mix(in srgb, var(--nav-fg, #888) 70%, transparent);
}}
</style>
<button id="nav-btn" type="button" aria-label="文件树" title="文件树">
<svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
<path d="M3 6a2 2 0 0 1 2-2h3l2 2h9a2 2 0 0 1 2 2v9a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/>
</svg>
</button>
<div id="nav-panel">
<div class="nav-head">&nbsp;</div>
<ul class="nav-tree"><li class="nav-empty">加载中...</li></ul>
</div>
<script>
(function () {{
  var btn = document.getElementById("nav-btn");
  var panel = document.getElementById("nav-panel");
  if (!btn || !panel) return;
  // 复用当前主题的 --bg-color / --text-color 给面板配色（没有则回退默认浅色）
  var hexToRgb = function (hex) {{
    var h = String(hex).trim().replace("#", "");
    if (h.length === 3) {{ h = h[0] + h[0] + h[1] + h[1] + h[2] + h[2]; }}
    if (!/^[0-9a-fA-F]{{6}}$/.test(h)) return null;
    var n = parseInt(h, 16);
    return (n >> 16 & 255) + "," + (n >> 8 & 255) + "," + (n & 255);
  }};
  var refreshNavTheme = function () {{
    var cs = getComputedStyle(document.body);
    var bg = cs.getPropertyValue("--bg-color").trim();
    var fg = cs.getPropertyValue("--text-color").trim();
    var rgb = hexToRgb(bg);
    if (rgb) panel.style.setProperty("--nav-bg", "rgba(" + rgb + ",.92)");
    if (fg) panel.style.setProperty("--nav-fg", fg);
  }};
  refreshNavTheme();
  window.addEventListener("pkm-theme-applied", refreshNavTheme);
  var toggle = function () {{
    panel.classList.toggle("open");
    btn.classList.toggle("open");
  }};
  btn.addEventListener("click", function (e) {{ e.stopPropagation(); toggle(); }});
  document.addEventListener("click", function (e) {{
    if (panel.classList.contains("open") &&
        !panel.contains(e.target) && e.target !== btn) toggle();
  }});
  // 当前页面到站点根的相对前缀（由 site-tree.json 的相对路径反推）
  var base = "{site_tree_rel}".replace(/site-tree\\.json$/, "");
  // 当前页面相对站点根的路径（用于高亮）
  var curRel = decodeURIComponent(location.pathname).replace(/^\\//, "");
  fetch("{site_tree_rel}")
    .then(function (r) {{ return r.json(); }})
    .then(function (root) {{
      var box = panel.querySelector(".nav-tree");
      box.innerHTML = "";
      if (!root.children || !root.children.length) {{
        box.innerHTML = '<li class="nav-empty">暂无文件</li>';
        return;
      }}
      (root.children || []).forEach(function (c) {{ box.appendChild(buildNode(c, 0)); }});
      expandActive(box);
    }})
    .catch(function () {{
      panel.querySelector(".nav-tree").innerHTML =
        '<li class="nav-empty">文件树加载失败</li>';
    }});
  function buildNode(node, depth) {{
    var li = document.createElement("li");
    if (node.type === "dir") {{
      li.className = "nav-dir" + (depth > 0 ? " collapsed" : "");
      var label = document.createElement("span");
      label.className = "nav-dir-label";
      label.textContent = node.name;
      label.addEventListener("click", function () {{
        li.classList.toggle("collapsed");
      }});
      li.appendChild(label);
      var ul = document.createElement("ul");
      (node.children || []).forEach(function (c) {{ ul.appendChild(buildNode(c, depth + 1)); }});
      li.appendChild(ul);
    }} else {{
      var a = document.createElement("a");
      a.className = "nav-file";
      a.href = base + node.rel;
      a.textContent = node.name;
      if (node.rel === curRel) a.classList.add("active");
      li.appendChild(a);
    }}
    return li;
  }}
  function expandActive(box) {{
    var a = box.querySelector("a.active");
    if (!a) return;
    var p = a.parentElement;
    while (p && p !== box) {{
      if (p.classList && p.classList.contains("nav-dir")) {{
        p.classList.remove("collapsed");
      }}
      p = p.parentElement;
    }}
  }}
}})();
</script>"""
