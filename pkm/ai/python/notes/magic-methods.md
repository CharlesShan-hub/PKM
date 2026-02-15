# Magic Methods

> https://zhuanlan.zhihu.com/p/344951719

## 字符串表示

| 特性           | `__repr__`                      | `__str__`               |
| ------------ | ------------------------------- | ----------------------- |
| ​**​目标用户​**​ | 开发者（调试用）                        | 终端用户（友好显示）              |
| ​**​调用场景​**​ | REPL、日志、`repr(obj)`             | `print(obj)`、`str(obj)` |
| ​**​要求​**​   | 明确无歧义                           | 可读性好                    |
| ​**​默认行为​**​ | 返回 `<ClassName object at 内存地址>` | 默认回退到 `__repr__`        |

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __repr__(self):
        return f"Person(name='{self.name}', age={self.age})"
    
    def __str__(self):
        return f"{self.name} ({self.age}岁)"

p = Person("Alice", 30)

# 直接输出对象（调用 __repr__）
print(repr(p))  # 输出: Person(name='Alice', age=30)

# print() 优先调用 __str__
print(p)        # 输出: Alice (30岁)
```

