"""
Markdown File Splitter Tool
Splits a markdown file by # headings, generates meaningful filenames using AI,
and creates organized notes structure.
"""

DESCRIPTION = "Splits a markdown file by # headings, generates meaningful filenames using AI, and creates organized notes structure."

PARAM_PROMPTS = {
    'input_file': {
        'label': 'Input Markdown File',
        'type': 'file',  # 改为file类型，以便选择文件
        'default': '',
    },
    'output_dir': {
        'label': 'Output Directory (will create /notes subfolder)',
        'type': 'path',
        'default': '',
    },
    'api_key': {
        'label': 'DeepSeek API Key (optional, can use DEEPSEEK_API_KEY env var)',
        'type': 'text',
        'default': '',
    }
}


import os
import re
import json
import requests
import time
import sys
from pathlib import Path
from typing import List, Tuple, Optional
import hashlib


def split_markdown_by_headings(file_path: str) -> List[Tuple[str, str]]:
    """
    按一级标题分割Markdown文件，直接查找# 标题模式
    
    Args:
        file_path: Markdown文件路径
        
    Returns:
        List[Tuple[str, str]]: 列表，每个元素是(标题, 内容)
    """
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 简单直接的方法：按行查找 # 开头的标题
    lines = content.split('\n')
    sections = []
    current_heading = None
    current_content = []
    
    for line in lines:
        # 检查是否是一级标题（# 开头，后面有空格，且不是 ## 或 ###）
        if line.startswith('# ') and not line.startswith('##'):
            # 如果已经有收集的内容，保存前一个章节
            if current_heading is not None:
                section_content = '\n'.join(current_content).strip()
                if section_content:
                    sections.append((current_heading, section_content))
            
            # 开始新的章节
            current_heading = line[2:].strip()  # 去掉 "# " 前缀
            current_content = [line]  # 包含标题行
        else:
            # 添加到当前章节内容
            if current_heading is not None:
                current_content.append(line)
    
    # 添加最后一个章节
    if current_heading is not None:
        section_content = '\n'.join(current_content).strip()
        if section_content:
            sections.append((current_heading, section_content))
    
    if not sections:
        raise ValueError("No level-1 headings (#) found in the markdown file")
    
    return sections


def generate_filename_with_ai(heading: str, content: str, api_key: str) -> str:
    """
    使用DeepSeek API生成文件名
    
    Args:
        heading: 章节标题
        content: 章节内容（前500字符）
        api_key: DeepSeek API密钥
        
    Returns:
        str: 生成的文件名
    """
    # 提取内容的前500个字符作为上下文
    context = content[:500]
    
    # 构建提示词
    prompt = f"""You are a helpful assistant that generates concise, descriptive filenames for markdown documents.

Given a section of markdown content (starting with a heading), generate a suitable filename that:
1. Is in English only
2. Uses lowercase letters
3. Separates words with hyphens (-)
4. Is concise (3-5 words maximum)
5. Accurately reflects the content
6. Ends with .md extension

Original heading: {heading}
Content to analyze: {context}

Generate only the filename, nothing else.
Example format: understanding-deepseek-api-integration.md"""
    
    try:
        # 调用DeepSeek API
        headers = {
            'Authorization': f'Bearer {api_key}',
            'Content-Type': 'application/json'
        }
        
        payload = {
            'model': 'deepseek-chat',
            'messages': [
                {'role': 'system', 'content': 'You are a helpful assistant that generates concise, descriptive filenames.'},
                {'role': 'user', 'content': prompt}
            ],
            'max_tokens': 50,
            'temperature': 0.3
        }
        
        response = requests.post(
            'https://api.deepseek.com/chat/completions',
            headers=headers,
            json=payload,
            timeout=30
        )
        
        if response.status_code == 200:
            result = response.json()
            filename = result['choices'][0]['message']['content'].strip()
            
            # 清理文件名：移除可能的引号、确保以.md结尾
            filename = filename.strip('"\'')
            if not filename.endswith('.md'):
                filename += '.md'
            
            # 确保只包含允许的字符
            filename = re.sub(r'[^a-zA-Z0-9\-\.]', '-', filename)
            filename = filename.lower()
            
            return filename
        else:
            print(f"API调用失败: {response.status_code} - {response.text}")
            return generate_fallback_filename(heading)
            
    except Exception as e:
        print(f"API调用异常: {e}")
        return generate_fallback_filename(heading)


def generate_fallback_filename(heading: str) -> str:
    """
    备选文件名生成方案（当API不可用时使用）
    
    Args:
        heading: 章节标题
        
    Returns:
        str: 生成的文件名
    """
    # 简单规则：将中文标题转换为拼音风格的英文文件名
    # 这里使用简单的翻译映射（实际应用中可能需要更复杂的处理）
    translations = {
        '项目': 'project',
        '概述': 'overview',
        '指南': 'guide',
        '使用': 'usage',
        '基础': 'basics',
        '编程': 'programming',
        '语法': 'syntax',
        '标题': 'headings',
        '列表': 'lists',
        '认证': 'authentication',
        '请求': 'request',
        '格式': 'format',
        '变量': 'variables',
        '数据': 'data',
        '类型': 'types',
        '控制': 'control',
        '流': 'flow',
        'Python': 'python',
        'Markdown': 'markdown',
        'DeepSeek': 'deepseek',
        'API': 'api'
    }
    
    # 简单的转换逻辑
    filename = heading.lower()
    for chinese, english in translations.items():
        filename = filename.replace(chinese.lower(), english)
    
    # 移除特殊字符，用连字符替换空格和标点
    filename = re.sub(r'[^\w\s-]', '', filename)
    filename = re.sub(r'[\s_]+', '-', filename)
    filename = filename.strip('-')
    
    # 确保以.md结尾
    if not filename.endswith('.md'):
        filename += '.md'
    
    return filename


def save_chapter(heading: str, content: str, output_path: Path, index: int, existing_filenames: set) -> str:
    """
    保存章节到文件，确保文件名唯一
    
    Args:
        heading: 章节标题
        content: 章节内容
        output_path: 输出目录
        index: 章节索引
        existing_filenames: 已存在的文件名集合
        
    Returns:
        str: 实际保存的文件名
    """
    # 生成基础文件名
    base_filename = f"chapter-{index:02d}.md"
    
    # 尝试使用更描述性的文件名
    try:
        # 从标题生成简单文件名
        safe_heading = re.sub(r'[^\w\s-]', '', heading)
        safe_heading = re.sub(r'[\s_]+', '-', safe_heading)
        safe_heading = safe_heading.strip('-').lower()
        
        if safe_heading and len(safe_heading) > 3:
            descriptive_name = safe_heading[:50] + '.md'
            if descriptive_name not in existing_filenames:
                base_filename = descriptive_name
    except:
        pass
    
    # 确保文件名唯一
    filename = base_filename
    counter = 1
    while filename in existing_filenames:
        name_part, ext = os.path.splitext(base_filename)
        filename = f"{name_part}-{counter}{ext}"
        counter += 1
    
    # 保存文件
    file_path = output_path / filename
    try:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"文件已保存: {file_path} (大小: {len(content)} 字符)")
    except Exception as e:
        print(f"保存文件失败 {file_path}: {e}")
        raise
    
    existing_filenames.add(filename)
    return filename


def save_chapter_with_filename(heading: str, content: str, output_path: Path, suggested_filename: str, existing_filenames: set) -> str:
    """
    使用指定的文件名保存章节
    
    Args:
        heading: 章节标题
        content: 章节内容
        output_path: 输出目录
        suggested_filename: 建议的文件名
        existing_filenames: 已存在的文件名集合
        
    Returns:
        str: 实际保存的文件名
    """
    # 确保文件名唯一
    filename = suggested_filename
    counter = 1
    while filename in existing_filenames:
        name_part, ext = os.path.splitext(suggested_filename)
        filename = f"{name_part}-{counter}{ext}"
        counter += 1
    
    # 保存文件
    file_path = output_path / filename
    try:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"文件已保存: {file_path} (大小: {len(content)} 字符)")
    except Exception as e:
        print(f"保存文件失败 {file_path}: {e}")
        raise
    
    existing_filenames.add(filename)
    return filename


def generate_readme(output_dir: Path, notes_dir: Path, filenames: List[str]) -> str:
    """
    生成README.md文件
    
    Args:
        output_dir: 输出目录
        notes_dir: notes子目录
        filenames: 所有生成的文件名列表
        
    Returns:
        str: README文件路径
    """
    readme_path = output_dir / "README.md"
    
    with open(readme_path, 'w', encoding='utf-8') as f:
        f.write("# Generated Notes\n\n")
        f.write("This directory contains notes generated from the markdown file.\n\n")
        
        f.write("## Files\n\n")
        for filename in filenames:
            # 创建相对路径链接
            rel_path = notes_dir.name + "/" + filename
            # 获取文件标题（从文件名推断）
            title = os.path.splitext(filename)[0].replace('-', ' ').title()
            f.write(f"- [{title}]({rel_path})\n")
        
        f.write("\n## Usage\n\n")
        f.write("These notes were automatically generated by the PKMizer Markdown Splitter tool.\n")
    
    return str(readme_path)


def run(input_file: str, output_dir: str, api_key: Optional[str] = None) -> str:
    """
    主运行函数
    
    Args:
        input_file: 输入的Markdown文件路径
        output_dir: 输出目录路径
        api_key: DeepSeek API密钥（可选）
        
    Returns:
        str: 执行结果摘要
    """
    result = []
    
    try:
        # 验证输入文件
        input_path = Path(input_file)
        if not input_path.exists():
            return f"错误: 输入文件不存在: {input_file}"
        
        if input_path.suffix.lower() != '.md':
            return f"错误: 输入文件不是Markdown文件: {input_file}"
        
        # 创建输出目录
        output_path = Path(output_dir)
        print(f"创建输出目录: {output_path}")
        output_path.mkdir(parents=True, exist_ok=True)
        print(f"输出目录已创建: {output_path.exists()}")
        
        # 创建notes子目录
        notes_dir = output_path / "notes"
        print(f"创建notes子目录: {notes_dir}")
        notes_dir.mkdir(exist_ok=True)
        print(f"notes子目录已创建: {notes_dir.exists()}")
        
        result.append(f"输入文件: {input_file}")
        result.append(f"输出目录: {output_dir}")
        result.append(f"Notes子目录: {notes_dir}")
        result.append("")
        
        # 分割Markdown文件
        result.append("正在分割Markdown文件...")
        sections = split_markdown_by_headings(input_file)
        result.append(f"找到 {len(sections)} 个章节")
        result.append("")
        
        # 保存每个章节
        saved_filenames = []
        existing_filenames = set()
        
        for i, (heading, content) in enumerate(sections):
            result.append(f"处理章节 {i+1}: {heading}")
            
            # 生成文件名
            if api_key:
                try:
                    filename = generate_filename_with_ai(heading, content, api_key)
                    result.append(f"  AI生成文件名: {filename}")
                    # 使用AI生成的文件名保存章节
                    filename = save_chapter_with_filename(heading, content, notes_dir, filename, existing_filenames)
                except Exception as e:
                    result.append(f"  AI生成失败，使用备选方案: {e}")
                    filename = save_chapter(heading, content, notes_dir, i+1, existing_filenames)
            else:
                filename = save_chapter(heading, content, notes_dir, i+1, existing_filenames)
            
            saved_filenames.append(filename)
            result.append(f"  保存为: {filename}")
        
        result.append("")
        
        # 生成README
        result.append("正在生成README.md...")
        readme_path = generate_readme(output_path, notes_dir, saved_filenames)
        result.append(f"README生成完成: {readme_path}")
        
        result.append("")
        result.append("=" * 50)
        result.append("处理完成!")
        result.append(f"共处理 {len(sections)} 个章节")
        result.append(f"文件保存在: {notes_dir}")
        result.append(f"README文件: {readme_path}")
        result.append("=" * 50)
        
    except Exception as e:
        result.append(f"错误: {str(e)}")
        import traceback
        result.append(f"详细错误信息: {traceback.format_exc()}")
    
    return "\n".join(result)


if __name__ == "__main__":
    # 测试代码
    import sys
    
    if len(sys.argv) >= 3:
        input_file = sys.argv[1]
        output_dir = sys.argv[2]
        api_key = sys.argv[3] if len(sys.argv) > 3 else None
        
        result = run(input_file, output_dir, api_key)
        print(result)
    else:
        print("用法: python markdown_splitter.py <input_file> <output_dir> [api_key]")
        print("示例: python markdown_splitter.py input.md ./output")