#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys

def analyze_bytes(file_path):
    """分析文件字节"""
    print(f"分析文件: {file_path}")
    
    with open(file_path, 'rb') as f:
        data = f.read(100)
        
    print(f"前100字节: {data}")
    print(f"十六进制: {data.hex()}")
    
    # 尝试UTF-8解码
    try:
        utf8_text = data.decode('utf-8')
        print(f"UTF-8解码成功: {repr(utf8_text[:30])}")
    except UnicodeDecodeError as e:
        print(f"UTF-8解码失败: {e}")
        
    # 尝试GBK解码
    try:
        gbk_text = data.decode('gbk')
        print(f"GBK解码成功: {repr(gbk_text[:30])}")
    except UnicodeDecodeError as e:
        print(f"GBK解码失败: {e}")

if __name__ == "__main__":
    analyze_bytes("D:/BaiduNetdiskDownload/laodu/25-RabbitMQ/document/temp.md")