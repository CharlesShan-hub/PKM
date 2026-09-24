/**
 * Excalidraw .excalidraw.md -> SVG renderer
 *
 * 把 Obsidian Excalidraw 插件保存的 .excalidraw.md 渲染为静态 SVG：
 *  1. 提取正文中的 ```compressed-json 块，用 lz-string 解压出 Excalidraw JSON
 *  2. 通过 @aldinokemal2104/excalidraw-to-svg 无头渲染成 SVG（自动嵌入手绘字体）
 *  3. 按输入相对路径写出 .svg 到站点根目录（与 .excalidraw.md 同位置）
 *
 * 用法:
 *   node svg.mjs <site_root> <input_root> <excalidraw.md 路径>...
 */
import { readFileSync, writeFileSync, mkdirSync } from 'node:fs';
import { dirname, relative, resolve, join } from 'node:path';
import lzString from 'lz-string';
import excalidrawToSvg from '@aldinokemal2104/excalidraw-to-svg';

const [siteRoot, inputRoot, ...files] = process.argv.slice(2);

/** 从 .excalidraw.md 文本中提取 Excalidraw JSON 字符串 */
function extractJson(text) {
  // 去掉 frontmatter
  const body = text.replace(/^---[\s\S]*?---\s*/, '').trim();
  // 标准压缩格式：```compressed-json 块
  // 注意：插件把压缩串按 256 字符分块、以空行分隔（便于 Git 对比），
  // decompressFromBase64 对换行敏感，需先移除所有空白
  const m = body.match(/```compressed-json\s*\n([\s\S]*?)```/);
  if (m) {
    const json = lzString.decompressFromBase64(m[1].replace(/\s+/g, ''));
    if (json) return json;
  }
  // 兼容未压缩格式：正文整体就是 JSON
  try {
    JSON.parse(body);
    return body;
  } catch (_) {
    return '';
  }
}

const results = { ok: 0, fail: 0 };
for (const file of files) {
  try {
    const text = readFileSync(file, 'utf8');
    const json = extractJson(text);
    if (!json) {
      console.error(`[SKIP] 无法提取 JSON: ${file}`);
      results.fail += 1;
      continue;
    }
    const svgEl = await excalidrawToSvg(json);
    const svg = svgEl.outerHTML;
    // 目标路径：站点根 + 输入相对路径，扩展名 .excalidraw.md -> .svg
    const rel = relative(inputRoot, file);
    const target = resolve(siteRoot, rel).replace(/\.excalidraw\.md$/i, '.excalidraw.svg');
    mkdirSync(dirname(target), { recursive: true });
    writeFileSync(target, svg, 'utf8');
    console.log(`[OK] ${rel}`);
    results.ok += 1;
  } catch (e) {
    console.error(`[FAIL] ${file}: ${e.message}`);
    results.fail += 1;
  }
}
console.log(`DONE ok=${results.ok} fail=${results.fail}`);
// 渲染库的 warm worker 会让进程保持存活，subprocess 调用方需要确定性退出
process.exit(0);
