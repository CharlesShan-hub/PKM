# enum

> https://docs.python.org/3/library/enum.html

## Enum Methods

### Define Enum and Visit item & attributes

Define

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

Visit

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

Without `@unique`: Value of items can be the same

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

With `@unique`

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

We can auto define values of items: Default index applies increasing.

```python
from enum import auto

class Color(Enum):
	RED = auto()
	GREEN = auto()
	BLUE = auto()

for member in Color: 
	print(member.value) # 1 2 3
```

We can change index method.

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

does not provide the aliases

```python
class ColorWithAliases(Enum):
	RED = 1
	GREEN = 2
	BLUE = 3
	Alias = 1

print(list(ColorWithAliases))
# [<ColorWithAliases.RED: 1>, <ColorWithAliases.GREEN: 2>, <ColorWithAliases.BLUE: 3>]
```

use `__members__` to get key and value，it can visit aliases members

```python
for key, value in ColorWithAliases.__members__.items():
	print(key, value)

# RED ColorWithAliases.RED
# GREEN ColorWithAliases.GREEN
# BLUE ColorWithAliases.BLUE
# ALIAS ColorWithAliases.RED
```

### Comparisons

use `is` or `is not`

```python
print(Color.RED is Color.GREEN) # True
```

use `==` or `!=`

```python
print(Color.RED == Color.RED) # True
```

can not compare enum with values

```python
print(Color.RED is == 1) # TypeError ❌
```

can not compare enum with `>` or `<`

```python
print(Color.RED is < Color.GREEN) # TypeError ❌
```

## Enum Classes



