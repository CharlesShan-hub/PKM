# enum

> 官方api文档： https://docs.python.org/3/library/enum.html
> 官网教程： https://docs.python.org/3/howto/enum.html
> 网友教程： https://blog.csdn.net/tekin_cn/article/details/145955099

## Enum Methods

### Define Enum and Visit item & attributes

定义

```python
from enum import Enum

class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

class Weekday(Enum):
	MONDAY = 1
	TUESDAY = 2
	WEDNESDAY = 3
	THURSDAY = 4
	FRIDAY = 5
	SATURDAY = 6
	SUNDAY = 7
```

访问

```python
print(Color(1))         # Color.RED
print(Color.RED)        # Color.RED
print(Color["RED"])     # Color.RED
print(Color.RED.name)   # 'RED'
print(Color.RED.value)  # 1
```

```python
print(type(Weekday.MONDAY)) # <enum 'Weekday'>
print(isinstance(Weekday.FRIDAY, Weekday)) # True
```

### Ensuring unique enumeration values

没有 `@unique`: 默认每个 name 对应的 value 可以是一样的

```python
class Direction(Enum):
	UP = 1
	DOWN = 2
	LEFT = 3
	RIGHT = 4
	Front = 1
	Back = 2

print(Direction.UP == Direction.Front) # True
```

有 `@unique` 修饰：每个 value 必须是独一无二的

```python
from enum import unique

@unique
class Direction(Enum):
	UP = 1
	DOWN = 2
	LEFT = 3
	RIGHT = 4
	# Front = 1 # <-- can't do this!
	# Back = 2
```

### Using automatic values

使用`auto`得到默认递增的 value

```python
from enum import auto

class Color(Enum):
	RED = auto()
	GREEN = auto()
	BLUE = auto()

for member in Color: 
	print(member.value) # 1 2 3
```

可以通过`_generate_next_value_()`改变 value 赋值方式

```python
class ChineseHour(Enum):

	def _generate_next_value_(name, start, count, last_values):
		hour = (count - 1) * 2 - 1
		return (hour % 24, (hour + 2) % 24 or 24)
	
	子时 = auto()
	丑时 = auto()
	寅时 = auto()
	卯时 = auto()
	辰时 = auto()
	巳时 = auto()
	午时 = auto()
	未时 = auto()
	申时 = auto()
	酉时 = auto()
	戌时 = auto()
	亥时 = auto()
	
	@property
	def start_hour(self):
		assert isinstance(self.value, tuple), "Value must be a tuple"
		return self.value[0]
	
	@property
	def end_hour(self):
		assert isinstance(self.value, tuple), "Value must be a tuple"
		return self.value[1]
	
	def contains(self, hour):
		assert isinstance(self.value, tuple), "Value must be a tuple"
		start, end = self.value
		if start < end:
			return start <= hour < end
		return hour >= start or hour < end

for hour in ChineseHour:
	print(f"{hour.name}: {hour.start_hour}:00-{hour.end_hour}:00")

# 丑时: 23:00-1:00
# 寅时: 1:00-3:00
# 卯时: 3:00-5:00
# 辰时: 5:00-7:00
# 巳时: 7:00-9:00
# 午时: 9:00-11:00
# 未时: 11:00-13:00
# 申时: 13:00-15:00
# 酉时: 15:00-17:00
# 戌时: 17:00-19:00
# 亥时: 19:00-21:00
```

### Iteration

默认不会提供别名的项，所以下面没有Alias这个name

```python
class ColorWithAliases(Enum):
	RED = 1
	GREEN = 2
	BLUE = 3
	ALIAS = 1

print(list(ColorWithAliases))
# [<ColorWithAliases.RED: 1>, <ColorWithAliases.GREEN: 2>, <ColorWithAliases.BLUE: 3>]
```

使用 `__members__` 同时得到 name 和 value，这种方式可以访问别名成员

```python
for key, value in ColorWithAliases.__members__.items():
	print(key, value)

# RED ColorWithAliases.RED
# GREEN ColorWithAliases.GREEN
# BLUE ColorWithAliases.BLUE
# ALIAS ColorWithAliases.RED
```

### Comparisons

使用 `is` 或 `is not`

```python
print(Color.RED is Color.GREEN) # True
```

使用 `==` 或 `!=`

```python
print(Color.RED == Color.RED) # True
```

不可以将 enum 和 value 比较

```python
print(Color.RED is == 1) # TypeError ❌
```

不可以使用 `>` or `<`

```python
print(Color.RED is < Color.GREEN) # TypeError ❌
```

### Extend

only if parent enum class has no enum items, it can has a child class

```python
class BaseColor(Enum):
	def __str__(self):
		return f"{self.name}: {self.value}"

class Color(BaseColor):
	RED = 1
	GREEN = 2
	BLUE = 3
	YELLOW = 4

print(Color.YELLOW) # YELLOW: 4
```

```python
class MoreColor(Color): # You can't do this!
	...
```

### dataclasses & enum

假设我们正在开发一个游戏，需要定义不同的角色类型（`Enum`），每个角色类型有特定的属性（通过 `dataclass` 定义）

```python
from dataclasses import dataclass
from enum import Enum

@dataclass
class RoleAttributes:
	health: int # 生命值
	attack: int # 攻击力
	speed: float # 移动速度
	description: str = "" # 可选描述

class CharacterType(RoleAttributes, Enum):
	# 格式: 枚举成员 = (health, attack, speed, description)
	WARRIOR = 100, 15, 1.2, "近战战士，高攻击"
	ARCHER = 70, 20, 1.5, "远程射手，高爆发"
	MAGE = 60, 25, 1.0, "法术法师，群体伤害"
  
# 获取枚举成员及其属性
archer = CharacterType.ARCHER
print(archer) # 输出: CharacterType.ARCHER
print(archer.health) # 输出: 70
print(archer.description) # 输出: "远程射手，高爆发"
  
# 类型安全的比较
if archer == CharacterType.ARCHER:
	print("这是射手角色") # 会执行
```

[[dataclasses]] 和enum的`__repr__`会冲突，所以不可以直接对继承了enum的类使用dataclass

```python
@dataclass  # ❌ 不要这样做！
class BadCharacter(Enum):
    WARRIOR = 100, 10
    ARCHER = 70, 15

# 问题1: 成员比较错误
print(BadCharacter.WARRIOR == BadCharacter.ARCHER)  # 输出: True（应为 False）

# 问题2: 无法直接访问字段
print(BadCharacter.WARRIOR.health)  # 报错！没有 health 属性
```

### Pickling

枚举可以被序列化和反序列化

```python
from pickle import dumps, loads

class Fruit(Enum):
	apple = 1
	banana = 2
	cherry = 3

print(loads(dumps(Fruit.apple)))
# Fruit.apple
```

```python
import json
from json import JSONEncoder
from enum import Enum

class Fruit(Enum):
    apple = 1
    banana = 2
    cherry = 3

# 序列化
class EnumEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Enum):
            return {
	            "__enum__": True, 
	            "type": type(obj).__name__, 
	            "value": obj.value
	        }
        return super().default(obj)
        
json_str = json.dumps(Fruit.apple, cls=EnumEncoder)
print(json_str)  # 输出: {"__enum__": true, "type": "Fruit", "value": 1}

# 反序列化
def enum_hook(d):
    if d.get("__enum__"):
        return globals()[d["type"]](d["value"])
    return d

restored_fruit = json.loads(json_str, object_hook=enum_hook)
print(restored_fruit)  # 输出: Fruit.apple
```

## Enum Classes

![[assets/enum-drawing|1000]]
### IntEnum

当我们需要知道每一个name对应的整数，甚至需要运算的时候，就要用到`IntEnum`

```python
from enum import IntEnum

class HTTPStatus(IntEnum):
    CONTINUE = 100
    OK = 200
    CREATED = 201
    BAD_REQUEST = 400
    UNAUTHORIZED = 401
    FORBIDDEN = 403
    NOT_FOUND = 404
    INTERNAL_SERVER_ERROR = 500

# 可以直接与整数比较
response = 404
if response == HTTPStatus.NOT_FOUND:
    print("Page not found")

# 也可以作为整数使用，但整数运算后，结果不再是枚举类型
print(HTTPStatus.OK + 100)  # 300
```



