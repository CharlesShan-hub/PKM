# dataclasses

> https://docs.python.org/3/library/dataclasses.html#dataclasses.dataclass

以下内容由deepseek生成：

`dataclasses` 是 Python 3.7+ 引入的一个内置模块（通过 `@dataclass` 装饰器），用于**简化类的定义**，特别适合用来存储数据（类似传统的数据结构或 POJO）。它自动生成常见方法（如 `__init__`、`__repr__`、`__eq__` 等），减少样板代码。

---

### **核心功能**
1. **自动生成方法**  
   只需用 `@dataclass` 装饰类并定义字段，它会自动生成：
   • `__init__()`：构造函数
   • `__repr__()`：可读的字符串表示
   • `__eq__()`：基于字段的相等性比较
   • 其他可选方法（如 `__hash__`、`__lt__` 等）

2. **类型注解驱动**  
   字段通过类型注解定义（如 `name: str`），无需手动写 `__init__`。

---

### **基础示例**
```python
from dataclasses import dataclass

@dataclass
class Person:
    name: str
    age: int
    is_active: bool = True  # 默认值

# 自动生成__init__和__repr__
p = Person("Alice", 30)
print(p)  # 输出: Person(name='Alice', age=30, is_active=True)
```

---

### **关键特性**
1. **默认值**  
   可以直接为字段赋默认值（如 `is_active: bool = True`）。

2. **不可变对象**  
   通过 `@dataclass(frozen=True)` 创建不可变实例（类似元组）：
   ```python
   @dataclass(frozen=True)
   class Point:
       x: int
       y: int

   p = Point(1, 2)
   p.x = 3  # 报错：frozen 实例不可修改
   ```

3. **后初始化处理**  
   用 `__post_init__` 方法在构造后执行逻辑：
   ```python
   @dataclass
   class Rectangle:
       width: float
       height: float
       area: float = None  # 不包含在__init__中

       def __post_init__(self):
           self.area = self.width * self.height
   ```

4. **字段控制**  
   • `field(init=False)`：排除字段从 `__init__` 中  
   • `field(repr=False)`：隐藏字段的 `__repr__`  
   ```python
   from dataclasses import field

   @dataclass
   class User:
       name: str
       password: str = field(repr=False)  # 打印时隐藏密码
   ```

---

### **与普通类的对比**
| 特性               | 普通类                          | `@dataclass`                     |
|--------------------|--------------------------------|----------------------------------|
| **定义字段**       | 需在 `__init__` 中手动声明      | 直接通过类型注解                 |
| **构造方法**       | 必须手动写 `__init__`          | 自动生成                         |
| **字符串表示**     | 需手动实现 `__repr__`          | 自动生成                         |
| **相等性比较**     | 需手动实现 `__eq__`            | 自动基于字段比较                 |
| **默认值**         | 需在 `__init__` 中处理         | 直接赋值                         |

---

### **适用场景**
• **数据容器**：如配置、DTO、数据库模型等。
• **快速原型**：避免重复写 `__init__` 和 `__repr__`。
• **不可变数据**：通过 `frozen=True` 保证数据安全。

---

### **进阶用法**
1. **继承**  
   ```python
   @dataclass
   class Base:
       x: int

   @dataclass
   class Child(Base):
       y: str
   ```

2. **与 `typing` 结合**  
   ```python
   from typing import List

   @dataclass
   class Team:
       members: List[Person]  # 使用复杂类型
   ```

3. **性能优化**  
   使用 `@dataclass(slots=True)` 生成 `__slots__` 减少内存占用。

---

### **总结**
`dataclasses` 通过自动化常见方法，让开发者更专注于数据逻辑而非样板代码，是 Python 中处理结构化数据的现代工具。对于更复杂的需求（如ORM），可结合 `pydantic` 或 `attrs` 库使用。