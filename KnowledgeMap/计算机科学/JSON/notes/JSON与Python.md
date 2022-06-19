# JSON与Python

2022.6.16

[toc]

## Overview

本条目主要介绍python的标准库，JSON

> [python官网网站介绍](https://docs.python.org/3/library/json.html)

## 数据类型转换

python转换成json

| Python                                 | JSON   |
| :------------------------------------- | :----- |
| dict                                   | object |
| list, tuple                            | array  |
| str                                    | string |
| int, float, int- & float-derived Enums | number |
| True                                   | true   |
| False                                  | false  |
| None                                   | null   |

json转换成python

| JSON          | Python |
| :------------ | :----- |
| object        | dict   |
| array         | list   |
| string        | str    |
| number (int)  | int    |
| number (real) | float  |
| true          | True   |
| false         | False  |
| null          | None   |

## 主要使用方法

| 方法              | 功能                                         |
| ----------------- | -------------------------------------------- |
| json.dump(obj,fp) | 将python数据类型转换并保存到json格式的文件内 |
| json.dumps(obj)   | 将python数据类型转换为json格式的字符串       |
| json.load(fp)     | 从json文件读取数据并转换成python类型         |
| json.loads(s)     | 将json字符串转换为python类型                 |

案例1

```python
import json
print(json.dumps(['foo', {'bar': ('baz', None, 1.0, 2, True)}]))
# ["foo", {"bar": ["baz", null, 1.0, 2, true]}]

print(json.dumps({"c": 0, "b": 0, "a": 0}, sort_keys=True))
# {"a": 0, "b": 0, "c": 0}

print(json.dumps({'bar': ('baz', None, 1.0, 2, True)}, indent=4))
#{
#    "bar": [
#        "baz",
#        null,
#        1.0,
#        2,
#        true
#    ]
#}
```

案例2

```python
import json
from io import StringIO
io = StringIO()
json.dump(['streaming API'], io)
io.getvalue()
# '["streaming API"]'
# 写入文件：
# json.dump(['streaming API'], open('data.json','w'))
# json.dump(['streaming API'], open('data.json','w'), indent=4)
```

案例3

```python
import json
s = '''["foo", {"bar": ["baz", null, 1.0, 2, true]}]'''
print(json.loads(s))
# ['foo', {'bar': ['baz', None, 1.0, 2, True]}]
```

案例4

```python
import json
obj = json.load(open('data.json','r'))
```