"""
Markdown File Splitter Tool V2
只读取输入并打印
"""

DESCRIPTION = "Markdown文件分割工具V2 - 只读取输入并打印"

PARAM_PROMPTS = {
    'input_file': {
        'label': '输入Markdown文件',
        'type': 'file',
        'default': '',
    },
    'output_dir': {
        'label': '输出目录（将创建/notes子文件夹）',
        'type': 'path',
        'default': '',
    },
    'api_key': {
        'label': 'DeepSeek API密钥（可选）',
        'type': 'text',
        'default': '',
    }
}

import os
import re
import json
import requests
import time
from pathlib import Path
from typing import Optional, List, Tuple


def find_level1_headings_with_positions(content: str) -> List[Tuple[str, int]]:
    """
    寻找所有的一级标题及其位置
    
    查找所有开头是# 的行，处理代码块逻辑，返回标题和位置
    
    Args:
        content: Markdown文件内容
        
    Returns:
        List[Tuple[str, int]]: 所有一级标题的列表，每个元素是(标题文本, 位置)
    """
    headings = []
    
    # 按行处理，但需要跳过代码块中的行
    lines = content.split('\n')
    in_code_block = False
    current_pos = 0
    
    for i, line in enumerate(lines):
        line_start_pos = current_pos
        
        # 检查是否进入或退出代码块
        if line.strip().startswith('```'):
            in_code_block = not in_code_block
        
        # 如果不在代码块中，检查是否是一级标题
        if not in_code_block:
            # 检查是否是一级标题（# 开头，且不是 ## 或 ###）
            if line.startswith('# ') and not line.startswith('##'):
                # 去掉 "# " 前缀，得到标题文本
                heading_text = line[2:].strip()
                headings.append((heading_text, line_start_pos))
        
        # 更新当前位置（包括换行符）
        current_pos += len(line) + 1
    
    return headings


def split_content_by_headings(content: str, headings_with_positions: List[Tuple[str, int]]) -> List[Tuple[str, str]]:
    """
    根据标题位置分割内容
    
    Args:
        content: 原始内容
        headings_with_positions: 标题和位置列表
        
    Returns:
        List[Tuple[str, str]]: 分割后的章节列表，每个元素是(标题, 内容)
    """
    sections = []
    
    for i, (heading, start_pos) in enumerate(headings_with_positions):
        # 计算本节内容的结束位置（下一个标题开始或文件结束）
        if i + 1 < len(headings_with_positions):
            end_pos = headings_with_positions[i + 1][1]
        else:
            end_pos = len(content)
        
        # 提取本节内容
        section_content = content[start_pos:end_pos]
        
        sections.append((heading, section_content))
    
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


def find_level1_headings(content: str) -> List[str]:
    """
    寻找所有的一级标题（兼容旧版本）
    
    Args:
        content: Markdown文件内容
        
    Returns:
        List[str]: 所有一级标题的列表
    """
    headings_with_positions = find_level1_headings_with_positions(content)
    return [heading for heading, _ in headings_with_positions]


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
        f.write("# 生成的笔记\n\n")
        f.write("此目录包含从Markdown文件生成的笔记。\n\n")
        
        f.write("## 文件列表\n\n")
        for filename in filenames:
            # 创建相对路径链接
            rel_path = notes_dir.name + "/" + filename
            # 获取文件标题（从文件名推断）
            title = os.path.splitext(filename)[0].replace('-', ' ').title()
            f.write(f"- [{title}]({rel_path})\n")
        
        f.write("\n## 使用说明\n\n")
        f.write("这些笔记是由PKMizer Markdown分割工具自动生成的。\n")
        f.write(f"生成时间: {time.strftime('%Y-%m-%d %H:%M:%S')}\n")
    
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
        result.append("=" * 60)
        result.append("只读取输入并打印")
        result.append("=" * 60)
        result.append("")
        
        # 读取输入参数
        result.append(f"输入文件: {input_file}")
        result.append(f"输出目录: {output_dir}")
        if api_key:
            result.append(f"API密钥: {api_key[:10]}...")
        result.append("")
        
        # 验证输入文件
        input_path = Path(input_file)
        if not input_path.exists():
            result.append(f"错误: 输入文件不存在: {input_file}")
            return "\n".join(result)
        
        if input_path.suffix.lower() != '.md':
            result.append(f"错误: 输入文件不是Markdown文件: {input_file}")
            return "\n".join(result)
        
        result.append(f"文件大小: {input_path.stat().st_size} 字节")
        result.append("")
        
        # 读取文件内容
        with open(input_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        result.append(f"文件内容长度: {len(content)} 字符")
        result.append("")
        
        # 显示文件前500个字符
        result.append("文件内容前500字符:")
        result.append("-" * 40)
        if len(content) > 500:
            result.append(content[:500] + "...")
        else:
            result.append(content)
        result.append("-" * 40)
        result.append("")
        
        # 第二个功能：寻找所有一级标题
        result.append("=" * 60)
        result.append("第二个功能：寻找所有一级标题")
        result.append("=" * 60)
        result.append("")
        
        headings = find_level1_headings(content)
        
        if not headings:
            result.append("未找到一级标题")
        else:
            result.append(f"找到 {len(headings)} 个一级标题:")
            for i, heading in enumerate(headings):
                result.append(f"  {i+1}. {heading}")
        
        result.append("")
        result.append("功能完成：返回标题列表")
        
        # 第三个功能：找到标题的index并打印位置
        result.append("")
        result.append("=" * 60)
        result.append("第三个功能：找到标题的index并打印位置")
        result.append("=" * 60)
        result.append("")
        
        # 获取标题和位置
        headings_with_positions = find_level1_headings_with_positions(content)
        
        if not headings_with_positions:
            result.append("未找到一级标题")
        else:
            result.append(f"找到 {len(headings_with_positions)} 个一级标题及其位置:")
            for i, (heading, position) in enumerate(headings_with_positions):
                result.append(f"")
                result.append(f"标题 {i+1}: {heading}")
                result.append(f"  位置: {position}")
                
                # 显示该位置前后的内容（用于验证）
                start = max(0, position - 20)
                end = min(len(content), position + 80)
                context = content[start:end]
                
                # 标记标题位置
                if start <= position < end:
                    marker_pos = position - start
                    marked_context = context[:marker_pos] + "【标题开始】" + context[marker_pos:]
                    result.append(f"  上下文: {marked_context}")
                else:
                    result.append(f"  上下文: {context}")
                
                # 显示标题行的完整内容
                lines = content[position:].split('\n')
                if lines:
                    title_line = lines[0]
                    result.append(f"  标题行: {title_line}")
            
            result.append("")
            result.append("功能完成：已找到所有标题的位置")
        
        # 第四个功能：根据位置分割内容
        result.append("")
        result.append("=" * 60)
        result.append("第四个功能：根据位置分割内容")
        result.append("=" * 60)
        result.append("")
        
        # 获取标题和位置
        headings_with_positions = find_level1_headings_with_positions(content)
        
        if not headings_with_positions:
            result.append("未找到一级标题，无法分割文件")
        else:
            # 分割内容
            sections = split_content_by_headings(content, headings_with_positions)
            
            result.append(f"成功分割为 {len(sections)} 个章节:")
            for i, (heading, section_content) in enumerate(sections):
                result.append(f"")
                result.append(f"章节 {i+1}: {heading}")
                result.append(f"  内容长度: {len(section_content)} 字符")
                
                # 检查内容是否包含完整的代码块
                code_blocks = re.findall(r'```[\s\S]*?```', section_content)
                result.append(f"  包含 {len(code_blocks)} 个代码块")
                
                # 显示内容前100个字符
                preview = section_content[:100].replace('\n', ' ')
                if len(section_content) > 100:
                    preview += "..."
                result.append(f"  内容预览: {preview}")
            
            result.append("")
            result.append("分割完成：所有章节已正确分割")
            
            # 第五个功能：使用AI生成文件名并保存章节
            result.append("")
            result.append("=" * 60)
            result.append("第五个功能：使用AI生成文件名并保存章节")
            result.append("=" * 60)
            result.append("")
            
            # 验证输出目录
            output_path = Path(output_dir)
            if not output_path.exists():
                output_path.mkdir(parents=True, exist_ok=True)
                result.append(f"创建输出目录: {output_path}")
            
            # 创建notes子目录
            notes_dir = output_path / "notes"
            notes_dir.mkdir(exist_ok=True)
            
            result.append(f"输出目录: {output_path}")
            result.append(f"Notes子目录: {notes_dir}")
            result.append("")
            
            # 准备保存章节
            existing_filenames = set()
            saved_files = []
            
            for i, (heading, section_content) in enumerate(sections):
                result.append(f"处理章节 {i+1}: {heading}")
                
                # 生成文件名
                if api_key:
                    result.append(f"  使用AI生成文件名...")
                    try:
                        filename = generate_filename_with_ai(heading, section_content, api_key)
                        result.append(f"  AI生成的文件名: {filename}")
                    except Exception as e:
                        result.append(f"  AI生成文件名失败: {e}")
                        filename = generate_fallback_filename(heading)
                        result.append(f"  使用备选文件名: {filename}")
                else:
                    filename = generate_fallback_filename(heading)
                    result.append(f"  使用备选文件名: {filename}")
                
                # 保存文件到notes子目录
                try:
                    saved_filename = save_chapter_with_filename(
                        heading, section_content, notes_dir, filename, existing_filenames
                    )
                    saved_files.append(saved_filename)
                    result.append(f"  文件已保存: {saved_filename}")
                except Exception as e:
                    result.append(f"  保存文件失败: {e}")
                
                result.append("")
            
            result.append(f"保存完成：共保存 {len(saved_files)} 个文件")
            result.append("")
            result.append(f"文件保存在: {notes_dir}")
            result.append("保存的文件列表:")
            for i, filename in enumerate(saved_files):
                result.append(f"  {i+1}. {filename}")
            
            # 生成README.md文件
            result.append("")
            result.append("正在生成README.md文件...")
            try:
                readme_path = generate_readme(output_path, notes_dir, saved_files)
                result.append(f"README.md已生成: {readme_path}")
                result.append("")
                result.append("README内容预览:")
                result.append("-" * 40)
                
                # 读取并显示README的前几行
                with open(readme_path, 'r', encoding='utf-8') as f:
                    readme_content = f.read()
                    lines = readme_content.split('\n')
                    for line in lines[:10]:  # 显示前10行
                        if line.strip():
                            result.append(f"  {line}")
                
                result.append("-" * 40)
                result.append("")
                result.append("处理完成！")
            except Exception as e:
                result.append(f"生成README失败: {e}")
        
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
