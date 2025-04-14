# dataclasses

> 官网： https://docs.python.org/3/library/dataclasses.html
> 科普视频： https://www.bilibili.com/video/BV1TR4y1V7NV

## 介绍

### 入门案例

> 根据科普视频总结

一开始，我们有一个很简单的类，用来记录某一条评论

```python
class ManualComment:
	def __init__(self, id: int, text: str):
		self.id: int = id
		self.text: str = text
```

接下来我们开始丰富它，我们加入了property，然后把属性加上下划线，这样变成了只读的，我们写入了获取字符串、相等、哈希等魔法函数。但这一切都是机械的工作，另外如果我要改一个地方，我需要把所有内容都修改。

```python
class ManualComment:
    def __init__(self, id: int, text: str):
        self.__id: int = id
        self.__text: str = text

    @property
    def text(self):
        return self.__text
    
    @property
    def id(self):
        return self.__id
    
    def to_dict(self):
        return {
            "id": self.id,
            "text": self.text
        }

    def __repr__(self):
        return f"ManualComment(id={self.id}, text={self.text})"
    
    def __str__(self):
        return self.text
    
    def __eq__(self, other):
        if isinstance(other, ManualComment):
            return self.id == other.id and self.text == other.text
        return False
    
    def __hash__(self):
        return hash((self.id, self.text))
    
```

我们可以用dataclasses来完成这种机械的工作

```python
from dataclasses import dataclass, asdict, astuple
@dataclass(frozen=True, order=True)
class ManualComment:
    id: int
    text: str

if __name__ == "__main__":
    comment = ManualComment(id=1, text="示例评论")
    print(asdict(comment))
    print(astuple(comment))
```

dataclasses为我们实现了很多的函数

```python
import inspect
print(inspect.getmembers(ManualComment, inspect.isfunction))
```

### Deepseek 介绍

`dataclasses` 是 Python 3.7+ 引入的一个内置模块（通过 `@dataclass` 装饰器），用于**简化类的定义**，特别适合用来存储数据（类似传统的数据结构或 POJO）。它自动生成常见方法（如 `__init__`、`__repr__`、`__eq__` 等），减少样板代码。

1. **自动生成方法**  
   只需用 `@dataclass` 装饰类并定义字段，它会自动生成：
   • `__init__()`：构造函数
   • `__repr__()`：可读的字符串表示
   • `__eq__()`：基于字段的相等性比较
   • 其他可选方法（如 `__hash__`、`__lt__` 等）

2. **类型注解驱动**  
   字段通过类型注解定义（如 `name: str`），无需手动写 `__init__`。

3. **默认值**  
   可以直接为字段赋默认值（如 `is_active: bool = True`）。

4. **不可变对象**  
   通过 `@dataclass(frozen=True)` 创建不可变实例（类似元组）：
   ```python
   @dataclass(frozen=True)
   class Point:
       x: int
       y: int

   p = Point(1, 2)
   p.x = 3  # 报错：frozen 实例不可修改
   ```

5. **后初始化处理**  
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

6. **字段控制**  
   • `field(init=False)`：排除字段从 `__init__` 中  
   • `field(repr=False)`：隐藏字段的 `__repr__`  
   ```python
   from dataclasses import field

   @dataclass
   class User:
       name: str
       password: str = field(repr=False)  # 打印时隐藏密码
   ```

7. **继承**  
   ```python
   @dataclass
   class Base:
       x: int

   @dataclass
   class Child(Base):
       y: str
   ```

8.  **与 `typing` 结合**  
	```python
	from typing import List
	
	@dataclass
	class Team:
	   members: List[Person]  # 使用复杂类型
	```

9. **性能优化**  
   使用 `@dataclass(slots=True)` 生成 `__slots__` 减少内存占用。

## API速通

### @dataclass
```python
@dataclasses.dataclass(_*_, _init=True_, _repr=True_, _eq=True_, _order=False_, _unsafe_hash=False_, _frozen=False_, _match_args=True_, _kw_only=False_, _slots=False_, _weakref_slot=False_)
```

* `_unsafe_hash`：默认不生成哈希`__hash__`，因为这个哈希是不安全的。
* `kw_only`：传参的时候必须使用关键字参数
	```python
	from dataclasses import dataclass
	
	@dataclass(kw_only=True)
	class Person:
	    name: str
	    age: int
	
	# 正确：使用关键字参数
	p = Person(name="Alice", age=30)
	
	# 错误：尝试用位置参数传值
	p = Person("Alice", 30)  # 触发 TypeError
	```
* `frozen`：只读
	注意frozen只能保证属性不能被重新赋值，但是不能保证属性内部不变
	```python
	from dataclasses import dataclass
	
	@dataclass(frozen=True)
	class MutableData:
	    items: list  # 可变字段（列表）
	    config: dict  # 可变字段（字典）
	
	# 创建实例
	data = MutableData(items=[1, 2], config={"key": "value"})
	
	# 1. 直接重新赋值字段 → 触发 FrozenInstanceError（符合预期）
	# data.items = [3, 4]  # 报错！无法修改字段本身
	
	# 2. 修改字段的内容 → 成功！（问题所在）
	data.items.append(3)       # 列表被修改！
	data.config["new"] = 123   # 字典被修改！
	
	print(data)  # 输出: MutableData(items=[1, 2, 3], config={'key': 'value', 'new': 123})
	```

	解决方案1，使用`typing.Final`递归冻结，会进行pyright错误提示，但是强行运行还可以通过

	```python
	from dataclasses import dataclass
	from typing import Final, List, Dict
	
	@dataclass(frozen=True)
	class ImmutableData:
	    items: Final[List[int]]     # 用 Final 标记（需配合类型检查工具如 mypy）
	    config: Final[Dict[str, str]]
	
	# 创建实例
	data = ImmutableData(items=[1, 2], config={"key": "value"})
	
	# 静态类型检查会捕获以下错误（但运行时仍可能修改）：
	data.items.append(3)     # mypy 报错: "Final" list 不可修改
	data.config["new"] = 123 # mypy 报错: "Final" dict 不可修改
	```

	解决方案2 递归冻结（运行时深度不可变）
	
	```python
	from dataclasses import dataclass
	from typing import Any
	import json
	
	def deep_freeze(obj: Any) -> Any:
	    """递归冻结对象（转换为元组或冻结字典）"""
	    if isinstance(obj, dict):
	        return frozenset((k, deep_freeze(v)) for k, v in obj.items())
	    elif isinstance(obj, list):
	        return tuple(deep_freeze(x) for x in obj)
	    return obj
	
	@dataclass(frozen=True)
	class DeepFrozenData:
	    items: tuple  # 直接使用不可变类型（tuple）
	    config: frozenset  # 使用 frozenset 存储字典
	
	    def __init__(self, items: list, config: dict):
	        # 在 __init__ 中手动递归冻结
	        object.__setattr__(self, 'items', deep_freeze(items))
	        object.__setattr__(self, 'config', deep_freeze(config))
	
	# 创建实例
	data = DeepFrozenData(items=[1, 2], config={"key": "value"})
	
	# 尝试修改内容 → 全部报错！
	data.items[0] = 3          # 报错！tuple 不可修改
	next(iter(data.config))[1] = "new"  # 报错！frozenset 不可修改
	```

### field()

```python
dataclasses.field(_*_, _default=MISSING_, _default_factory=MISSING_, _init=True_, _repr=True_, _hash=None_, _compare=True_, _metadata=None_, _kw_only=MISSING_)
```

进一步限制字段信息

```python
from dataclasses import dataclass, field

@dataclass
class C:
    mylist: list[int] = field(default_factory=list)

c = C()
c.mylist += [1, 2, 3]
```

* default适用于静态的值：`x: int = field(default=0)`
* default_factory适用于动态的值：`items: list = field(default_factory=list)`
* repr：是否需要被打印（其他类的同理，是否要被包含在对应的魔法函数里边）

### _class_ Field


### _class_ InitVar

### fields()

### asdict()

### astuple()

### replace()

### is_dataclass()

### MISSING

### KW_ONLY