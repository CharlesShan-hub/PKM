"""
图片双击放大控件：全屏遮罩展示大图（页面内嵌 style/script 模板）

用法与 theme_ui / nav_ui 一致：返回 <style> + <script> 字符串，
由 html.py 注入到每个页面。双击正文 <img> 打开，点击遮罩 / Esc 关闭。
"""


def build_lightbox_script() -> str:
    """
    构建图片双击放大控件（lightbox）

    双击页面正文的图片弹出全屏遮罩并居中展示大图；
    点击遮罩任意处或按 Esc 关闭。UI 控件区（导航面板/主题按钮）内的
    图标不受影响。

    Returns:
        str: <style> + <script> 内容
    """
    return """<style>
#pkm-lightbox {
  position: fixed; inset: 0; z-index: 9999;
  background: rgba(0, 0, 0, .85);
  display: none; align-items: center; justify-content: center;
  cursor: zoom-out; padding: 4vh 4vw;
}
#pkm-lightbox.open {
  display: flex;
}
#pkm-lightbox img {
  max-width: 92vw; max-height: 92vh;
  box-shadow: 0 8px 48px rgba(0, 0, 0, .55);
  border-radius: 4px;
  background: #fff;
}
</style>
<script>
(function () {
  var box = document.createElement('div');
  box.id = 'pkm-lightbox';
  var boxImg = document.createElement('img');
  box.appendChild(boxImg);
  document.body.appendChild(box);

  function open(src, alt) {
    boxImg.src = src;
    boxImg.alt = alt || '';
    box.classList.add('open');
  }
  function close() {
    box.classList.remove('open');
  }

  box.addEventListener('click', close);
  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape') close();
  });
  document.addEventListener('dblclick', function (e) {
    var t = e.target;
    if (t && t.tagName === 'IMG' && !t.closest('nav, #nav-btn, #theme-btn, #theme-menu, #pkm-lightbox')) {
      e.preventDefault();
      open(t.currentSrc || t.src, t.alt);
    }
  });
})();
</script>
"""
