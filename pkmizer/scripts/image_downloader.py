"""
Markdown Image Downloader Tool
Downloads online images referenced in markdown files and replaces with local references
"""

DESCRIPTION = "Downloads online images from markdown files and replaces URLs with local file references."

PARAM_PROMPTS = {
    'input_dir': {
        'label': 'Input Directory (contains markdown files)',
        'type': 'path',
        'default': '',
    },
    'output_dir': {
        'label': 'Output Directory (optional, defaults to ../assets)',
        'type': 'path',
        'default': '',
    },
}


import os
import re
import urllib.request
import urllib.error
from urllib.parse import urlparse, unquote
from pathlib import Path
import time


def download_image(url, output_dir, timeout=15, retry_count=3):
    """
    下载图片到指定目录
    
    Args:
        url: 图片URL
        output_dir: 输出目录
        timeout: 超时时间（秒）
        retry_count: 重试次数
    
    Returns:
        tuple: (成功与否, 本地文件名, 错误信息)
    """
    # 从URL提取文件名
    parsed = urlparse(url)
    basename = os.path.basename(unquote(parsed.path))
    
    # 如果没有扩展名，尝试从Content-Type推断
    if not basename or '.' not in basename:
        basename = f"image_{int(time.time())}.jpg"
    
    # 确保文件名唯一
    local_name = basename
    counter = 1
    while os.path.exists(os.path.join(output_dir, local_name)):
        name, ext = os.path.splitext(basename)
        local_name = f"{name}_{counter}{ext}"
        counter += 1
    
    local_path = os.path.join(output_dir, local_name)
    
    # 重试机制
    for attempt in range(retry_count):
        try:
            req = urllib.request.Request(url, headers={
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
            })
            
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                # 检查Content-Type
                content_type = resp.headers.get('Content-Type', '')
                if not local_name.lower().endswith(('.jpg', '.jpeg', '.png', '.gif', '.webp', '.svg')):
                    # 根据Content-Type添加扩展名
                    if 'jpeg' in content_type or 'jpg' in content_type:
                        local_name += '.jpg'
                    elif 'png' in content_type:
                        local_name += '.png'
                    elif 'gif' in content_type:
                        local_name += '.gif'
                    elif 'webp' in content_type:
                        local_name += '.webp'
                    elif 'svg' in content_type:
                        local_name += '.svg'
                    else:
                        local_name += '.jpg'
                
                local_path = os.path.join(output_dir, local_name)
                
                with open(local_path, 'wb') as out:
                    out.write(resp.read())
            
            return True, local_name, None
            
        except urllib.error.HTTPError as e:
            if attempt == retry_count - 1:
                return False, None, f"HTTP错误 {e.code}: {e.reason}"
            time.sleep(1)  # 等待后重试
            
        except urllib.error.URLError as e:
            if attempt == retry_count - 1:
                return False, None, f"URL错误: {e.reason}"
            time.sleep(1)
            
        except Exception as e:
            if attempt == retry_count - 1:
                return False, None, f"下载错误: {str(e)}"
            time.sleep(1)
    
    return False, None, "下载失败"


def find_markdown_images(input_dir):
    """
    查找Markdown文件中的图片引用
    
    Args:
        input_dir: 输入目录
    
    Returns:
        dict: {文件名: [(行内容, 图片URL), ...]}
    """
    # 支持多种图片引用格式的正则表达式
    patterns = [
        # HTML img标签
        re.compile(r'<img\s+[^>]*src="(https?://[^"]+)"[^>]*>', re.IGNORECASE),
        # Markdown图片语法
        re.compile(r'!\[[^\]]*\]\((https?://[^)]+)\)'),
        # 带标题的Markdown图片
        re.compile(r'!\[[^\]]*\]\((https?://[^)]+)\s+"[^"]+"\)'),
    ]
    
    files_images = {}
    input_path = Path(input_dir)
    
    # 递归查找所有markdown文件
    for md_file in input_path.rglob("*.md"):
        try:
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # 获取相对于输入目录的路径（用于显示）
            rel_path = md_file.relative_to(input_path)
            
            # 找出所有图片引用
            image_refs = []
            lines = content.split('\n')
            
            for line_num, line in enumerate(lines, 1):
                for pattern in patterns:
                    matches = pattern.findall(line)
                    for url in matches:
                        image_refs.append((line, url, line_num))
            
            if image_refs:
                files_images[str(rel_path)] = image_refs
                
        except Exception as e:
            print(f"读取文件 {md_file} 时出错: {str(e)}")
    
    return files_images


def replace_image_references(input_dir, output_dir, url_to_filename):
    """
    替换Markdown文件中的图片引用
    
    Args:
        input_dir: 输入目录
        output_dir: 输出目录（assets目录）
        url_to_filename: URL到本地文件名的映射
    
    Returns:
        tuple: (更新的文件数, 错误列表)
    """
    updated_files = 0
    errors = []
    
    input_path = Path(input_dir)
    assets_dir = Path(output_dir)  # output_dir就是assets目录
    
    # 计算assets目录相对于markdown文件的路径
    assets_relative_path = os.path.relpath(assets_dir, input_path)
    
    # 调试：打印原始相对路径
    print(f"调试[replace] - assets_relative_path原始值: {repr(assets_relative_path)}")
    print(f"调试[replace] - assets_relative_path长度: {len(assets_relative_path)}")
    
    # 清理路径中的特殊字符
    assets_relative_path = ''.join(c for c in assets_relative_path if ord(c) >= 32)
    
    print(f"调试[replace] - assets_relative_path清理后: {assets_relative_path}")
    
    for md_file in input_path.rglob("*.md"):
        try:
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            new_content = content
            
            # 替换所有图片引用
            for url, local_name in url_to_filename.items():
                # 确保路径使用正斜杠（Markdown标准）
                clean_relative_path = assets_relative_path.replace('\\', '/')
                
                # 替换HTML img标签
                img_pattern = re.compile(fr'<img\s+[^>]*src="{re.escape(url)}"[^>]*>', re.IGNORECASE)
                new_content = img_pattern.sub(f'![{local_name}]({clean_relative_path}/{local_name})', new_content)
                
                # 替换Markdown图片语法
                md_pattern = re.compile(fr'!\[[^\]]*\]\({re.escape(url)}\)')
                new_content = md_pattern.sub(f'![{local_name}]({clean_relative_path}/{local_name})', new_content)
                
                # 替换带标题的Markdown图片
                md_title_pattern = re.compile(fr'!\[[^\]]*\]\({re.escape(url)}\s+"[^"]+"\)')
                new_content = md_title_pattern.sub(f'![{local_name}]({clean_relative_path}/{local_name})', new_content)
            
            if new_content != content:
                with open(md_file, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                updated_files += 1
                
        except Exception as e:
            errors.append(f"更新文件 {md_file} 时出错: {str(e)}")
    
    return updated_files, errors


def run(input_dir=None, output_dir=None):
    """
    运行图片下载器工具
    
    Args:
        input_dir: 包含markdown文件的输入目录
        output_dir: 输出目录（可选，默认使用输入目录的父目录下的assets文件夹）
    
    Returns:
        str: 执行结果摘要
    """
    if not input_dir:
        return "错误: 需要提供输入目录参数"
    
    input_path = Path(input_dir)
    
    if not input_path.exists():
        return f"错误: 输入目录不存在: {input_dir}"
    
    # 如果未提供输出目录，使用输入目录的父目录下的assets文件夹
    if not output_dir:
        output_dir = str(input_path.parent / "assets")
    
    output_path = Path(output_dir)
    
    # 创建输出目录
    output_path.mkdir(parents=True, exist_ok=True)
    
    # assets目录就是输出目录本身
    assets_dir = output_path
    assets_dir.mkdir(exist_ok=True)
    
    # 计算assets目录相对于markdown文件的路径
    assets_relative_path = os.path.relpath(assets_dir, input_path)
    
    # 调试：打印原始相对路径
    print(f"调试 - assets_relative_path原始值: {repr(assets_relative_path)}")
    print(f"调试 - assets_relative_path长度: {len(assets_relative_path)}")
    print(f"调试 - assets_relative_path字符: {[ord(c) for c in assets_relative_path]}")
    
    # 清理路径中的特殊字符
    assets_relative_path = ''.join(c for c in assets_relative_path if ord(c) >= 32)
    
    print(f"输入目录: {input_dir}")
    print(f"输出目录: {output_dir}")
    print(f"Assets目录: {assets_dir}")
    print(f"相对路径: {assets_relative_path}")
    print("-" * 50)
    
    # 1. 查找所有图片引用
    print("正在查找Markdown文件中的图片引用...")
    files_images = find_markdown_images(input_dir)
    
    if not files_images:
        return f"在 {input_dir} 中未找到包含在线图片的Markdown文件"
    
    total_images = sum(len(refs) for refs in files_images.values())
    print(f"发现 {len(files_images)} 个文件包含 {total_images} 张在线图片")
    
    # 2. 收集所有唯一的URL
    all_urls = set()
    for refs in files_images.values():
        for _, url, _ in refs:
            all_urls.add(url)
    
    print(f"发现 {len(all_urls)} 个唯一的图片URL")
    print("-" * 50)
    
    # 3. 下载图片
    print("开始下载图片...")
    url_to_filename = {}
    download_stats = {
        'success': 0,
        'skipped': 0,
        'failed': 0,
        'errors': []
    }
    
    for i, url in enumerate(all_urls, 1):
        # 检查是否已存在同名文件
        parsed = urlparse(url)
        basename = os.path.basename(unquote(parsed.path))
        if basename:
            # 检查文件是否已存在
            existing_files = list(assets_dir.glob(f"{os.path.splitext(basename)[0]}*"))
            if existing_files:
                # 使用已存在的文件
                local_name = existing_files[0].name
                url_to_filename[url] = local_name
                download_stats['skipped'] += 1
                print(f"  [{i}/{len(all_urls)}] [跳过] {local_name} (已存在)")
                continue
        
        success, local_name, error = download_image(url, assets_dir)
        
        if success:
            url_to_filename[url] = local_name
            download_stats['success'] += 1
            print(f"  [{i}/{len(all_urls)}] [成功] {local_name}")
        else:
            download_stats['failed'] += 1
            download_stats['errors'].append(f"URL: {url}, 错误: {error}")
            print(f"  [{i}/{len(all_urls)}] [失败] {url} -> {error}")
    
    print("-" * 50)
    
    # 4. 替换文件引用
    print("开始替换Markdown文件中的图片引用...")
    updated_files, update_errors = replace_image_references(input_dir, output_dir, url_to_filename)
    
    if update_errors:
        download_stats['errors'].extend(update_errors)
    
    print("-" * 50)
    
    # 5. 生成结果摘要
    result = [
        "=" * 60,
        "Markdown图片下载器 - 执行结果",
        "=" * 60,
        f"输入目录: {input_dir}",
        f"输出目录: {output_dir}",
        f"Assets目录: {assets_dir}",
        f"相对路径: {assets_relative_path}",
        "",
        "统计信息:",
        f"  扫描文件数: {len(files_images)} 个Markdown文件",
        f"  发现图片数: {total_images} 张在线图片",
        f"  唯一URL数: {len(all_urls)} 个",
        "",
        "下载结果:",
        f"  成功下载: {download_stats['success']} 张",
        f"  跳过(已存在): {download_stats['skipped']} 张",
        f"  下载失败: {download_stats['failed']} 张",
        "",
        "文件更新:",
        f"  更新文件: {updated_files} 个",
    ]
    
    if download_stats['errors']:
        result.append("")
        result.append("错误信息:")
        for error in download_stats['errors'][:10]:  # 只显示前10个错误
            result.append(f"  - {error}")
        if len(download_stats['errors']) > 10:
            result.append(f"  ... 还有 {len(download_stats['errors']) - 10} 个错误未显示")
    
    result.append("=" * 60)
    
    return "\n".join(result)


if __name__ == "__main__":
    # 测试代码
    test_input = r"D:\project\PKM\pkm\backend\javaweb\xxl-job\notes"
    test_output = r"D:\project\PKM\pkm\backend\javaweb\xxl-job"
    
    if os.path.exists(test_input):
        result = run(test_input, test_output)
        print(result)
    else:
        print("测试目录不存在，请手动指定参数运行")
        print("用法: python image_downloader.py <input_dir> <output_dir>")