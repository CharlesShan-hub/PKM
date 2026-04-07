import re
from pathlib import Path

def split_markdown_by_headings_debug(file_path: str):
    """
    调试版本的分割函数，打印详细的分割信息
    """
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    print(f"文件总长度: {len(content)} 字符")
    print(f"文件内容前200字符: {content[:200]}")
    print("-" * 80)
    
    # 预处理：标记代码区域，避免将代码中的#识别为标题
    # 1. 匹配代码块（三个反引号包围的内容）
    code_block_pattern = re.compile(r'```[\s\S]*?```', re.MULTILINE)
    # 2. 匹配行内代码（单个反引号包围的内容）
    inline_code_pattern = re.compile(r'`[^`]*`')
    
    # 创建一个标记版本的内容，将代码区域替换为占位符
    code_regions = []
    
    def replace_code_region(match):
        code_regions.append(match.group(0))
        return f'__CODE_REGION_{len(code_regions)-1}__'
    
    # 先替换代码块（三个反引号）
    processed_content = code_block_pattern.sub(replace_code_region, content)
    # 再替换行内代码（单个反引号）
    processed_content = inline_code_pattern.sub(replace_code_region, processed_content)
    
    print(f"处理后内容长度: {len(processed_content)} 字符")
    print(f"找到的代码区域数量: {len(code_regions)}")
    for i, code in enumerate(code_regions[:3]):  # 只显示前3个
        print(f"代码区域 {i}: {code[:100]}...")
    print("-" * 80)
    
    # 使用正则表达式查找所有一级标题
    # 匹配格式: # 标题（注意：## 标题是二级标题，### 标题是三级标题）
    # 使用负向先行断言确保后面没有紧跟着另一个#
    heading_pattern = re.compile(r'^#(?!#)\s+(.+)$', re.MULTILINE)
    
    # 找到所有标题的位置
    headings = []
    for match in heading_pattern.finditer(processed_content):
        # 检查这个位置是否在原始内容中也是有效的（不在代码块中）
        original_pos = match.start()
        # 由于我们只替换了代码块，位置映射是保持的
        headings.append((original_pos, match.group(1)))
        print(f"找到标题: '{match.group(1)}' 在位置 {original_pos}")
    
    if not headings:
        print("未找到一级标题")
        return []
    
    print(f"总共找到 {len(headings)} 个标题")
    print("-" * 80)
    
    # 分割内容
    sections = []
    for i, (start_pos, heading) in enumerate(headings):
        # 计算本节内容的结束位置（下一个标题开始或文件结束）
        end_pos = headings[i + 1][0] if i + 1 < len(headings) else len(content)
        
        print(f"章节 {i+1}: '{heading}'")
        print(f"  开始位置: {start_pos}, 结束位置: {end_pos}")
        print(f"  内容长度: {end_pos - start_pos} 字符")
        
        # 提取本节内容（包含标题行）
        section_content = content[start_pos:end_pos].strip()
        
        # 检查内容是否包含代码块
        if '```' in section_content:
            print(f"  包含代码块")
        
        # 检查内容开头
        print(f"  内容开头50字符: {section_content[:50]}")
        
        # 检查内容结尾
        print(f"  内容结尾50字符: {section_content[-50:]}")
        
        # 还原代码块占位符
        for idx, code_region in enumerate(code_regions):
            placeholder = f'__CODE_REGION_{idx}__'
            if placeholder in section_content:
                section_content = section_content.replace(placeholder, code_region)
        
        # 清理标题中的占位符
        for idx, code_region in enumerate(code_regions):
            placeholder = f'__CODE_REGION_{idx}__'
            if placeholder in heading:
                heading = heading.replace(placeholder, '')
                heading = heading.strip()
        
        sections.append((heading, section_content))
        print("-" * 80)
    
    return sections

if __name__ == "__main__":
    # 测试分割逻辑
    test_file = "test_split_issue.md"
    sections = split_markdown_by_headings_debug(test_file)
    
    print("\n" + "=" * 80)
    print("分割结果摘要:")
    for i, (heading, content) in enumerate(sections):
        print(f"章节 {i+1}: {heading}")
        print(f"  内容长度: {len(content)} 字符")
        
        # 检查是否有截断的代码
        if 'public void createOrder' in content:
            print(f"  包含完整的 createOrder 方法")
        elif 'createOrder' in content:
            print(f"  包含 createOrder 但不完整")
            
        # 查找代码块
        code_blocks = re.findall(r'```[\s\S]*?```', content)
        print(f"  包含 {len(code_blocks)} 个代码块")