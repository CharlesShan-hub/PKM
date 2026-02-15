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

`Field`类是`field()`工厂函数返回的内容。不要自己去调用这个类。

```python
# 源码
class Field:
    __slots__ = ('name',
                 'type',
                 'default',
                 'default_factory',
                 'repr',
                 'hash',
                 'init',
                 'compare',
                 'metadata',
                 'kw_only',
                 '_field_type',  # Private: not to be used by user code.
                 )
```
### _class_ InitVar

用于一些临时的字段，可以在`__init__`和`__post_init__`里边参与计算，但是并不会最终保存

```python
from dataclasses import dataclass, InitVar

@dataclass
class Person:
    name: str
    birth_year: InitVar[int]  # 仅用于初始化的临时字段
    age: int = 0             # 计算得出的字段
    
    def __post_init__(self, birth_year):
        # 使用InitVar参数计算age
        self.age = 2023 - birth_year

# 使用示例
p = Person("张三", 1990)
print(p)          # 输出: Person(name='张三', age=33)
print(p.age)      # 输出: 33
# print(p.birth_year)  # 报错！InitVar字段不会成为实例属性
```

### fields()

一个辅助函数，用来一个包含数据类所有字段的元组，每个字段都是 Field 类型的对象，包含字段的元数据（如类型、默认值等）

```python
from dataclasses import dataclass, fields
from pprint import pprint

@dataclass
class Example:
    name: str
    age: int = 18

# 获取字段信息
field_list = fields(Example)
pprint(field_list, indent=2) 

# ( Field(name='name',type=<class 'str'>,default=<dataclasses._MISSING_TYPE object at 0x10350d070>,default_factory=<dataclasses._MISSING_TYPE object at 0x10350d070>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),kw_only=False,_field_type=_FIELD),
#   Field(name='age',type=<class 'int'>,default=18,default_factory=<dataclasses._MISSING_TYPE object at 0x10350d070>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),kw_only=False,_field_type=_FIELD))

```

### asdict()

* 将dataclass对象转换为字典
* 可以自定义字典工厂函数（默认调用内置的dict）
* 使用深拷贝得到字典

```python
from dataclasses import dataclass, asdict

@dataclass
class Category:
    name: str
    code: str

@dataclass 
class Product:
    id: int
    name: str
    price: float
    category: Category  # 嵌套数据类

def custom_factory(items):
    # 添加额外元数据的自定义字典
    d = dict(items)
    d['_meta'] = {'version': '1.0', 'timestamp': '2023-01-01'}
    return d

# 创建嵌套对象
original_category = Category("电子产品", "ELEC")
original_product = Product(1, "笔记本电脑", 5999.0, original_category)

# 转换为字典并验证深拷贝
product_dict = asdict(original_product, dict_factory=custom_factory)

# 修改原始对象
original_category.name = "家电"
original_product.price = 4999.0

print("转换后的字典(不受原始对象修改影响):")
print(product_dict)
# 输出包含原始category.name和price值

print("\n原始对象修改后:")
print(f"原始category.name: {original_category.name}")  # 家电
print(f"字典中的category.name: {product_dict['category']['name']}")  # 仍为"电子产品"
```
### astuple()

```python
dataclasses.astuple(_obj_, _*_, _tuple_factory=tuple_)
```

* 将dataclass对象转换为元组
* 同样使用深拷贝

### make_dataclass()

```python
dataclasses.make_dataclass(_cls_name_, _fields_, _*_, _bases=()_, _namespace=None_, _init=True_, _repr=True_, _eq=True_, _order=False_, _unsafe_hash=False_, _frozen=False_, _match_args=True_, _kw_only=False_, _slots=False_, _weakref_slot=False_, _module=None_)
```

用于 动态创建数据类 。它的主要作用是：

1. 运行时创建数据类 ：不需要预先用 @dataclass 装饰器定义类
2. 编程式构建类结构 ：通过参数指定字段名、类型和字段选项
3. 与装饰器等效 ：生成的类与用 @dataclass 创建的类功能完全相同

```python
from dataclasses import make_dataclass

# 动态创建一个Point数据类
Point = make_dataclass('Point', ['x', 'y'])

# 等效于：
# @dataclass
# class Point:
#     x: Any
#     y: Any

p = Point(1, 2)
print(p)  # 输出: Point(x=1, y=2)
```

### replace()

```python
dataclasses.replace(_obj_, _/_, _**changes_)
```

主要用于 创建数据类实例的修改副本

- 不可变对象友好 ：特别适合 frozen=True 的不可变数据类
- 非破坏性更新 ：返回新对象而不是修改原对象
- 字段选择性替换 ：只修改指定的字段，其余保持原值

```python
from dataclasses import dataclass, replace

@dataclass(frozen=True)  # 特别适合不可变类
class Point:
    x: int
    y: int

p1 = Point(1, 2)
p2 = replace(p1, x=3)  # 创建新对象，只修改x

print(p1)  # Point(x=1, y=2)
print(p2)  # Point(x=3, y=2)
```

### is_dataclass()

如果其参数是数据类（包括数据类的子类）或其实例，则返回 `True` ，否则返回 `False` 。

如果你需要知道一个类是否是数据类的实例（而不是数据类本身），则还需要检查 `not isinstance(obj, type)`

```python
def is_dataclass_instance(obj):
    return is_dataclass(obj) and not isinstance(obj, type)
```

### MISSING

一个表示缺失默认值或默认工厂的哨兵值。

注意：普通用户代码通常不需要直接使用 MISSING ，除非你在深度定制数据类行为。

### KW_ONLY

一个用于类型注解的哨兵值。任何伪字段之后的字段（其类型为 `KW_ONLY` ）都被标记为关键字**只读字段**。

在本例中，字段 `y` 和 `z` 将被标记为kw-only 字段：

```python
@dataclass
class Point:
    x: float
    _: KW_ONLY
    y: float
    z: float

p = Point(0, y=1.5, z=2.0)
```

### 初始化后处理

`__post_init__` 是 `dataclass` 特有的魔法方法，但它的设计遵循 Python 常规魔法方法的模式。以下是关键点分析：

1. **dataclass 专属特性**：
   - 专门由 `@dataclass` 装饰器触发调用
   - 在自动生成的 `__init__` 方法末尾被调用
   - 用于处理初始化后的额外操作

2. **与普通魔法方法的区别**：
   ```python
   class RegularClass:
       def __post_init__(self):  # 普通类中不会自动调用
           print("不会被自动调用")
   ```

3. **典型使用场景**：
   ```python
   from dataclasses import dataclass

   @dataclass
   class Point:
       x: float
       y: float
       distance: float = 0.0  # 派生字段

       def __post_init__(self):
           # 初始化后自动计算
           self.distance = (self.x**2 + self.y**2)**0.5

   p = Point(3.0, 4.0)
   print(p.distance)  # 输出: 5.0
   ```

4. **与普通魔法方法的相似性**：
   - 命名遵循 `__xxx__` 的双下划线约定
   - 作为类生命周期中的特殊钩子存在
