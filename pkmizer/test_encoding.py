#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
from pathlib import Path

def test_file_encoding(file_path):
    """测试文件编码"""
    print(f"测试文件: {file_path}")
    print(f"文件大小: {os.path.getsize(file_path)} 字节")
    
    # 尝试不同编码读取
    encodings = ['utf-8', 'gbk', 'gb2312', 'utf-16', 'latin-1']
    
    for encoding in encodings:
        try:
            with open(file_path, 'r', encoding=encoding) as f:
                content = f.read(200)
                print(f"\n使用 {encoding} 编码读取前200字符:")
                print("-" * 50)
                print(repr(content))
                print("-" * 50)
                # 检查是否有乱码
                if '\\x' in repr(content) or '\\u' in repr(content):
                    print(f"警告: {encoding} 编码可能有乱码")
                else:
                    print(f"OK: {encoding} 编码看起来正常")
                break
        except UnicodeDecodeError as e:
            print(f"ERROR: {encoding} 编码失败: {e}")
        except Exception as e:
            print(f"ERROR: {encoding} 编码错误: {e}")

if __name__ == "__main__":
    # 测试原始文件
    original_file = "D:/BaiduNetdiskDownload/laodu/25-RabbitMQ/document/temp.md"
    if os.path.exists(original_file):
        print("=== 测试原始文件 ===")
        test_file_encoding(original_file)
    else:
        print(f"原始文件不存在: {original_file}")
    
    # 测试生成的文件
    generated_file = "d:\\project\\PKM\\pkmizer\\rabbitmq_output2\\notes\\why-use-rabbitmq.md"
    if os.path.exists(generated_file):
        print("\n=== 测试生成的文件 ===")
        test_file_encoding(generated_file)
    else:
        print(f"生成的文件不存在: {generated_file}")