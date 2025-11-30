# getopt

## Basic

getopt的函数原型

```python
import getopt 
getopt.getopt(args, shortopts, longopts=[])
```
- `args`: 要解析的参数列表（通常是 `sys.argv[1:]`）
- `shortopts`: 短选项字符串（类似 C 的 `optstring`）
- `longopts`: 长选项列表（可选）

首先查看python里调用参数是如何传递进去的，第一个参数是文件路径，后边的是传入的命令和参数

```python
# basic.py
print(f"sys.argv: {sys.argv}")
```

```bash
(playground) kimshan@ROBINMBP ~/P/p/playground (master)> uv run -m exp.getopt.basic -a 1 -b 2
sys.argv: ['/Users/kimshan/Public/project/playground/exp/getopt/basic.py', '-a', '1', '-b', '2']
```

1. 基本语法：`getopt.getopt(args, shortopts, longopts=[])`
   - args: 要解析的命令行参数列表
   - shortopts: 短选项字符串，如'ab:c'
   - longopts: 长选项列表，如['help', 'output=']
2. 选项字符串规则：
   - 单个字符表示选项，如 'a' 表示 -a 选项
   - 字符后跟冒号 ':' 表示选项需要参数，如 'b:' 表示 -b 需要参数
   - 自Python 3.14版本起，getopt支持双冒号 '::' 表示可选参数
3. 使用示例：
   - 命令行: `python script.py -a -b value -c`
   - 解析结果: `opts = [('-a', ''), ('-b', 'value'), ('-c', '')], args = []`
4. 错误处理：
   - 未知选项: 抛出 GetoptError，消息包含未知选项
   - 缺少必需参数: 抛出 GetoptError，消息包含缺少参数的选项
5. 与GNU getopt的主要区别：
   - 自Python 3.14起，支持可选参数(::)扩展
   - 错误处理方式不同，Python版本会抛出异常

对应c语言的getopt [[unistd]]，python版的可以实现类似的效果

```python
#!/usr/bin/env python3
import getopt
import sys

def main():
    """
    使用Python标准库的getopt模块解析命令行参数
    
    在Python 3.14版本中，getopt模块开始支持可选参数功能
    本示例中：
    - 'a' 表示选项 -a 不需要参数
    - 'b:' 表示选项 -b 需要参数（冒号表示必需参数）
    - 'c::' 表示选项 -c 接受可选参数（双冒号表示可选参数）
    """
    
    try:
        # 使用getopt.getopt函数解析命令行参数
        # 第一个参数：要解析的参数列表（排除程序名）
        # 第二个参数：选项字符串，定义了选项及其是否需要参数
        # 返回值：opts是(选项, 参数)元组的列表，args是非选项参数的列表
        opts, args = getopt.getopt(sys.argv[1:], 'ab:c::')
        
        # 处理解析出的选项
        for opt, arg in opts:
            if opt == '-a':
                # -a 选项不需要参数
                print("选项 -a 被指定")
            elif opt == '-b':
                # -b 选项需要参数，参数值存储在arg中
                print(f"选项 -b 被指定，参数为: {arg}")
            elif opt == '-c':
                # 在Python 3.14+中，-c 是可选参数选项
                if arg:
                    print(f"选项 -c 被指定，带有参数: {arg}")
                else:
                    print("选项 -c 被指定，没有参数")
        
        # 处理非选项参数
        for arg in args:
            print(f"非选项参数: {arg}")
            
    except getopt.GetoptError as e:
        # 处理错误情况
        # 常见错误：未知选项、缺少必需参数
        print(f"getopt错误: {e}")
        sys.exit(1)

# 测试示例说明
'''
# 编译命令
# 无需编译，直接运行Python脚本

# 测试示例1: python basic.py -a -b Hello -c New -d World
# 预期输出:
# 选项 -a 被指定
# 选项 -b 被指定，参数为: Hello
# 选项 -c 被指定，带有参数: New
# 未知选项: d
# 非选项参数: World

# 测试示例2: python basic.py -a -b Hello -c
# 预期输出:
# 选项 -a 被指定
# 选项 -b 被指定，参数为: Hello
# 选项 -c 被指定，没有参数

# 测试示例3: python basic.py -a -b Hello
# 预期输出:
# 选项 -a 被指定
# 选项 -b 被指定，参数为: Hello
'''


if __name__ == "__main__":
    main()
```

```bash
(playground)~/P/p/p/e/getopt [0] $ uv run -m exp.getopt.basic -a -b Hello -cWorld
选项 -a 被指定
选项 -b 被指定，参数为: Hello
选项 -c 被指定，带有参数: World

(playground)~/P/p/p/e/getopt [0] $ uv run -m exp.getopt.basic -a -b Hello -c
选项 -a 被指定
选项 -b 被指定，参数为: Hello
选项 -c 被指定，没有参数

(playground) ~/P/p/p/e/getopt [0] $ uv run -m exp.getopt.basic -a -b Hello
选项 -a 被指定
选项 -b 被指定，参数为: Hello
```

## Long Params



```bash
>>>s = '--condition=foo --testing --output-file abc.def -x a1 a2'
>>>args = s.split()
>>>args
['--condition=foo', '--testing', '--output-file', 'abc.def', '-x', 'a1', 'a2']
>>>optlist, args = getopt.getopt(args, 'x', [
    'condition=', 'output-file=', 'testing'])
>>>optlist
[('--condition', 'foo'), ('--testing', ''), ('--output-file', 'abc.def'), ('-x', '')]
>>>args
['a1', 'a2']
```





* https://docs.python.org/zh-cn/3/library/getopt.html