"""
DeepSeek Markdown Optimizer
使用 DeepSeek API 批量优化 Markdown 文件（保留内容，仅优化语法）
"""

DESCRIPTION = "使用 DeepSeek API 批量优化 Markdown 文件 - 转换 font 标签为加粗，优化 Markdown 语法"

PARAM_PROMPTS = {
    'input_dir': {
        'label': '输入目录（包含 Markdown 文件）',
        'type': 'path',
        'default': '',
    },
    'prompt_name': {
        'label': '提示词模板',
        'type': 'select',
        'options': {
            'font_to_bold': 'Font标签转加粗',
            'markdown_format': 'Markdown格式化',
            'content_summary': '内容摘要',
        },
        'default': 'font_to_bold',
    },
    'api_key': {
        'label': 'DeepSeek API 密钥',
        'type': 'text',
        'default': '',
    },
}


import os
import re
import time
import json
import shutil
import requests
from pathlib import Path
from typing import Optional, List, Tuple


# 提示词模板
SYSTEM_PROMPT = """你是一个 Markdown 语法优化专家。

你的任务是：
1. 将 HTML 中的 <font> 标签转换为标准 Markdown 加粗语法（**文字**）
2. 保持原始内容完全不变，只优化 Markdown 语法
3. 修复明显的 Markdown 语法错误
4. 保持原有格式结构

重要规则：
- 只修改 Markdown 语法，不要修改实际内容
- <font> 标签要转换为 **加粗**
- 保留代码块、链接、图片等原有格式
- 输出只包含优化后的 Markdown 内容，不要添加任何解释
"""



def backup_directory(input_dir: str) -> Tuple[bool, str]:
    """
    备份输入目录

    Args:
        input_dir: 输入目录路径

    Returns:
        Tuple[成功与否, 备份路径或错误信息]
    """
    input_path = Path(input_dir)
    backup_path = input_path.parent / f"{input_path.name}_backup"

    # 如果备份目录已存在，先删除
    if backup_path.exists():
        shutil.rmtree(backup_path)

    try:
        shutil.copytree(input_path, backup_path)
        return True, str(backup_path)
    except Exception as e:
        return False, f"备份失败: {str(e)}"


def find_markdown_files(input_dir: str) -> List[Path]:
    """
    查找目录下所有 Markdown 文件

    Args:
        input_dir: 输入目录

    Returns:
        List[Path]: Markdown 文件路径列表
    """
    input_path = Path(input_dir)
    md_files = list(input_path.rglob("*.md")) + list(input_path.rglob("*.markdown"))
    return sorted(md_files)


def optimize_with_api(content: str, api_key: str, model: str, system_prompt: str, user_prompt_template: str) -> Tuple[bool, str]:
    """
    使用 DeepSeek API 优化 Markdown 内容

    Args:
        content: 原始内容
        api_key: API 密钥
        model: 模型名称
        system_prompt: 系统提示词
        user_prompt_template: 用户提示词模板

    Returns:
        Tuple[成功与否, 优化后的内容或错误信息]
    """
    headers = {
        'Authorization': f'Bearer {api_key}',
        'Content-Type': 'application/json'
    }

    payload = {
        'model': model,
        'messages': [
            {'role': 'system', 'content': system_prompt},
            {'role': 'user', 'content': user_prompt_template.format(content=content)}
        ],
        'max_tokens': 4096,
        'temperature': 0.1
    }

    try:
        response = requests.post(
            'https://api.deepseek.com/chat/completions',
            headers=headers,
            json=payload,
            timeout=120
        )

        if response.status_code == 200:
            result = response.json()
            optimized_content = result['choices'][0]['message']['content'].strip()
            return True, optimized_content
        else:
            return False, f"API 错误: {response.status_code} - {response.text}"

    except requests.exceptions.Timeout:
        return False, "API 请求超时"
    except Exception as e:
        return False, f"请求异常: {str(e)}"


def extract_markdown_from_response(response: str) -> Optional[str]:
    """
    从 API 响应中提取 Markdown 内容（处理可能的代码块包裹）

    Args:
        response: API 响应内容

    Returns:
        提取的 Markdown 内容或原内容
    """
    # 如果响应被 ```markdown 或 ``` 包裹，提取内部内容
    code_block_pattern = r'^```(?:markdown)?\s*\n(.*?)\n```$'
    match = re.match(code_block_pattern, response, re.DOTALL)
    if match:
        return match.group(1)

    return response


def process_markdown_file(file_path: Path, api_key: str, model: str, total: int, index: int,
                          prompt_name: str, system_prompt: str, user_prompt_template: str) -> Tuple[bool, str]:
    """
    处理单个 Markdown 文件

    Args:
        file_path: 文件路径
        api_key: API 密钥
        model: 模型名称
        total: 总文件数
        index: 当前索引
        prompt_name: 提示词名称
        system_prompt: 系统提示词
        user_prompt_template: 用户提示词模板

    Returns:
        Tuple[成功与否, 结果信息]
    """
    print(f"[{index}/{total}] 开始处理: {file_path.name}")

    try:
        # 读取原始内容
        with open(file_path, 'r', encoding='utf-8') as f:
            original_content = f.read()

        # 检查是否包含 font 标签
        has_font_tags = '<font' in original_content

        print(f"  文件大小: {len(original_content)} 字符, 包含 font 标签: {'是' if has_font_tags else '否'}")

        # 调用 API 优化
        print(f"  正在调用 DeepSeek API (prompt: {prompt_name})...")
        success, result = optimize_with_api(original_content, api_key, model, system_prompt, user_prompt_template)

        if not success:
            print(f"  API 调用失败: {result}")
            return False, f"API 调用失败: {result}"

        # 提取 Markdown 内容
        optimized_content = extract_markdown_from_response(result)

        # 保存优化后的内容
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(optimized_content)

        # 检查 font 标签是否被移除
        still_has_font = '<font' in optimized_content

        print(f"  [OK] 优化完成 (优化后: {len(optimized_content)} 字符, font 标签: {'残留' if still_has_font else '已清除'})")

        return True, "优化成功"

    except Exception as e:
        print(f"  [FAIL] 处理失败: {str(e)}")
        return False, f"处理失败: {str(e)}"


def load_prompts(prompts_file: str = None) -> dict:
    """
    加载提示词配置文件

    Args:
        prompts_file: 提示词配置文件路径，默认使用项目根目录的 prompts.json

    Returns:
        dict: 提示词配置字典
    """
    if prompts_file is None:
        prompts_file = Path(__file__).parent.parent / "prompts.json"
    else:
        prompts_file = Path(prompts_file)

    try:
        with open(prompts_file, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        print(f"加载提示词配置文件失败: {e}")
        return {}


def run(input_dir: Optional[str] = None, api_key: Optional[str] = None, prompt_name: Optional[str] = None,
        system_prompt: Optional[str] = None, user_prompt_template: Optional[str] = None) -> str:
    """
    主运行函数

    Args:
        input_dir: 输入目录
        api_key: DeepSeek API 密钥
        prompt_name: 提示词模板名称
        system_prompt: 自定义系统提示词（可选，优先使用）
        user_prompt_template: 自定义用户提示词模板（可选，优先使用）

    Returns:
        str: 执行结果摘要
    """
    # 使用默认模型
    model = "deepseek-chat"

    # 如果没有传入自定义提示词，从配置文件加载
    if system_prompt is None or user_prompt_template is None:
        prompts = load_prompts()
        if not prompts:
            return "错误: 无法加载提示词配置文件"

        # 获取选中的提示词，默认使用第一个
        if prompt_name and prompt_name in prompts:
            selected_prompt = prompts[prompt_name]
        else:
            first_key = next(iter(prompts.keys()))
            selected_prompt = prompts[first_key]
            prompt_name = first_key

        if system_prompt is None:
            system_prompt = selected_prompt.get('system_prompt', '')
        if user_prompt_template is None:
            user_prompt_template = selected_prompt.get('user_prompt_template', '')

    result = []

    # 验证参数
    if not input_dir:
        return "错误: 需要提供输入目录参数"

    if not api_key:
        return "错误: 需要提供 DeepSeek API 密钥"

    input_path = Path(input_dir)
    if not input_path.exists():
        return f"错误: 输入目录不存在: {input_dir}"

    if not input_path.is_dir():
        return f"错误: 输入路径不是目录: {input_dir}"

    result.append("=" * 60)
    result.append("DeepSeek Markdown 优化工具")
    result.append("=" * 60)
    result.append("")
    result.append(f"输入目录: {input_dir}")
    result.append(f"模型: {model}")
    result.append("")

    # Step 1: 备份
    result.append("-" * 40)
    result.append("Step 1: 备份原文件")
    result.append("-" * 40)

    backup_success, backup_path = backup_directory(input_dir)
    if not backup_success:
        result.append(f"备份失败: {backup_path}")
        return "\n".join(result)

    result.append(f"备份成功: {backup_path}")
    result.append("")

    # Step 2: 查找 Markdown 文件
    result.append("-" * 40)
    result.append("Step 2: 扫描 Markdown 文件")
    result.append("-" * 40)

    md_files = find_markdown_files(input_dir)
    result.append(f"找到 {len(md_files)} 个 Markdown 文件")
    result.append("")

    if not md_files:
        result.append("未找到 Markdown 文件，任务结束")
        return "\n".join(result)

    # 列出所有文件
    for i, f in enumerate(md_files, 1):
        rel_path = f.relative_to(input_path)
        result.append(f"  {i}. {rel_path}")
    result.append("")

    # Step 3: 逐个处理文件
    result.append("-" * 40)
    result.append("Step 3: 调用 DeepSeek API 优化")
    result.append("-" * 40)
    result.append("")

    stats = {
        'total': len(md_files),
        'success': 0,
        'failed': 0,
        'errors': []
    }

    for i, file_path in enumerate(md_files, 1):
        success, message = process_markdown_file(
            file_path, api_key, model, len(md_files), i,
            prompt_name, system_prompt, user_prompt_template
        )

        if success:
            stats['success'] += 1
        else:
            stats['failed'] += 1
            stats['errors'].append(f"{file_path.name}: {message}")

        # API 限流保护：每个文件处理后等待 1 秒
        if i < len(md_files):
            print(f"  [WAIT] 等待 1 秒后继续下一个文件...")
            time.sleep(1)

    result.append("")

    # Step 4: 结果汇总
    result.append("-" * 40)
    result.append("Step 4: 处理结果汇总")
    result.append("-" * 40)
    result.append("")
    result.append(f"总计文件: {stats['total']}")
    result.append(f"成功: {stats['success']}")
    result.append(f"失败: {stats['failed']}")
    result.append("")

    if stats['errors']:
        result.append("错误列表:")
        for error in stats['errors']:
            result.append(f"  - {error}")
        result.append("")
        result.append("提示: 失败的文件已保留原始内容，可从备份目录恢复")

    result.append("")
    result.append(f"备份目录: {backup_path}")
    result.append("=" * 60)
    result.append("处理完成！")
    result.append("=" * 60)

    return "\n".join(result)


if __name__ == "__main__":
    # 测试代码
    import sys

    if len(sys.argv) >= 3:
        input_dir = sys.argv[1]
        api_key = sys.argv[2]
        model = sys.argv[3] if len(sys.argv) > 3 else "deepseek-chat"

        result = run(input_dir, api_key, model)
        print(result)
    else:
        print("用法: python markdown_optimizer.py <input_dir> <api_key> [model]")
        print("示例: python markdown_optimizer.py ./notes sk-xxxxx")
