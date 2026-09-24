"""
页面内目录控件：导航按钮旁的 TOC 按钮 + 大纲浮层（内嵌 style/script 模板）

与 nav_ui / theme_ui 相同模式：返回完整 HTML（按钮 + 面板 + 样式 + 脚本），
由 html.py 注入。点击 TOC 按钮展开当前页面的标题大纲，点击条目平滑跳转，
滚动时自动高亮当前章节；无标题的页面按钮自动隐藏。
"""


def build_toc_panel() -> str:
    """
    构建页面内目录（TOC）控件

    按钮并排在左侧文件树按钮旁；大纲面板按 h1-h6 层级缩进，
    点击条目平滑滚动到对应标题并高亮，滚动时跟随当前章节。

    Returns:
        str: 按钮 + 大纲面板 + <style> + <script> 内容
    """
    return """<style>
#toc-btn {
  position: fixed; top: 10px; left: 56px; z-index: 1000;
  width: 38px; height: 38px; border-radius: 50%;
  background: rgba(127,127,127,.3);
  -webkit-backdrop-filter: blur(4px); backdrop-filter: blur(4px);
  display: flex; align-items: center; justify-content: center;
  cursor: pointer; transition: background .2s ease;
  border: 1px solid rgba(255,255,255,.25);
}
#toc-btn:hover, #toc-btn.open {
  background: rgba(0,0,0,.7); border-color: rgba(255,255,255,.5);
}
#toc-btn svg {
  width: 20px; height: 20px; fill: none; stroke: #fff; stroke-width: 1.8;
  stroke-linecap: round; stroke-linejoin: round;
  filter: drop-shadow(0 1px 2px rgba(0,0,0,.6));
}
#toc-panel {
  position: fixed; top: 58px; left: 10px; z-index: 1000;
  width: 240px; max-height: 60vh; overflow-y: auto;
  background: var(--nav-bg, rgba(255,255,255,.95));
  color: var(--nav-fg, #555);
  -webkit-backdrop-filter: blur(8px); backdrop-filter: blur(8px);
  box-shadow: 0 4px 24px rgba(0,0,0,.18);
  border-radius: 10px; padding: 6px;
  display: none; font-size: 13px; font-family: Arial, sans-serif;
}
#toc-panel.open { display: block; }
#toc-panel .toc-list {
  list-style: none; margin: 0; padding: 0;
}
#toc-panel ul { list-style: none; margin: 0; padding: 0 0 0 12px; }
#toc-panel li { margin: 1px 0; }
#toc-panel a {
  display: block; padding: 3px 8px; border-radius: 5px;
  color: var(--nav-fg, #444); text-decoration: none;
  white-space: nowrap; overflow: hidden; text-overflow: ellipsis;
}
#toc-panel a:hover {
  background: color-mix(in srgb, var(--nav-fg, #555) 9%, transparent);
}
#toc-panel a.active {
  background: color-mix(in srgb, var(--nav-fg, #555) 16%, transparent);
  color: var(--nav-fg, #111); font-weight: 600;
}
#toc-panel .toc-empty {
  padding: 8px; color: color-mix(in srgb, var(--nav-fg, #888) 70%, transparent);
}
</style>
<button id="toc-btn" type="button" aria-label="页面目录" title="页面目录">
<svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
<path d="M3 6h12M3 12h12M3 18h12"/>
<path d="M17 4l3 3-3 3M17 10l3 3-3 3M17 16l3 3-3 3"/>
</svg>
</button>
<div id="toc-panel"></div>
<script>
(function () {
  var btn = document.getElementById("toc-btn");
  var panel = document.getElementById("toc-panel");
  if (!btn || !panel) return;

  // 复用当前主题背景色给大纲面板配色（与导航面板同一套变量名）
  var hexToRgb = function (hex) {
    var h = String(hex).trim().replace("#", "");
    if (h.length === 3) { h = h[0] + h[0] + h[1] + h[1] + h[2] + h[2]; }
    if (!/^[0-9a-fA-F]{6}$/.test(h)) return null;
    var n = parseInt(h, 16);
    return (n >> 16 & 255) + "," + (n >> 8 & 255) + "," + (n & 255);
  };
  var refreshTocTheme = function () {
    var cs = getComputedStyle(document.body);
    var bg = cs.getPropertyValue("--bg-color").trim();
    var fg = cs.getPropertyValue("--text-color").trim();
    var rgb = hexToRgb(bg);
    if (rgb) panel.style.setProperty("--nav-bg", "rgba(" + rgb + ",.92)");
    if (fg) panel.style.setProperty("--nav-fg", fg);
  };
  refreshTocTheme();
  window.addEventListener("pkm-theme-applied", refreshTocTheme);

  var headings = Array.prototype.slice.call(
    document.querySelectorAll("h1,h2,h3,h4,h5,h6")
  ).filter(function (el) { return el.id; });
  if (!headings.length) {
    btn.style.display = "none";
    return;
  }

  var open = function () { panel.classList.add("open"); btn.classList.add("open"); };
  var close = function () { panel.classList.remove("open"); btn.classList.remove("open"); };
  btn.addEventListener("click", function (e) {
    e.stopPropagation();
    if (panel.classList.contains("open")) close(); else open();
  });
  document.addEventListener("click", function (e) {
    if (panel.classList.contains("open") &&
        !panel.contains(e.target) && e.target !== btn) close();
  });
  document.addEventListener("keydown", function (e) {
    if (e.key === "Escape") close();
  });

  // 按标题级别构建嵌套目录（栈式算法：h1 > h2 > h3 层级缩进）
  var root = document.createElement("ul");
  root.className = "toc-list";
  var stack = [{ level: 0, ul: root }];
  headings.forEach(function (h) {
    var level = parseInt(h.tagName.slice(1), 10);
    var li = document.createElement("li");
    var a = document.createElement("a");
    a.href = "#" + h.id;
    a.textContent = h.textContent;
    li.appendChild(a);
    while (stack.length && stack[stack.length - 1].level >= level) stack.pop();
    var parent = stack[stack.length - 1] || { ul: root };
    parent.ul.appendChild(li);
    var sub = document.createElement("ul");
    li.appendChild(sub);
    stack.push({ level: level, ul: sub });
  });
  panel.appendChild(root);

  // 点击目录项平滑滚动到标题，并更新高亮
  var cur = null;
  var setActive = function (a) {
    if (cur) cur.classList.remove("active");
    cur = a;
    if (cur) cur.classList.add("active");
  };
  panel.addEventListener("click", function (e) {
    var a = e.target.closest("a");
    if (!a) return;
    e.preventDefault();
    var el = document.getElementById(decodeURIComponent(a.getAttribute("href").slice(1)));
    if (!el) return;
    el.scrollIntoView({ behavior: "smooth", block: "start" });
    setActive(a);
  });
  // 滚动时跟随当前章节高亮
  var updateActive = function () {
    var pos = window.scrollY + 80;
    var idx = -1;
    for (var i = 0; i < headings.length; i++) {
      if (headings[i].offsetTop <= pos) idx = i; else break;
    }
    var target = idx >= 0 ? root.querySelector('a[href="#' + headings[idx].id + '"]') : null;
    if (target && target !== cur) setActive(target);
  };
  window.addEventListener("scroll", updateActive, { passive: true });
  updateActive();
})();
</script>"""
