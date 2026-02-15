# decorator

`decorator` 是一个 Python 库，用于创建装饰器。装饰器是一种特殊类型的 Python 函数，它可以修改其他函数的行为，而无需修改其源代码。`decorator` 库提供了一种更简单、更灵活的方式来创建装饰器，尤其是当装饰器的参数化或递归使用时。 以下是 `decorator` 的关键特点和用法：

#### 关键特点

1. **参数化装饰器**：允许你创建参数化的装饰器，这使得装饰器的使用更加灵活。
2. **递归装饰器**：允许你创建递归的装饰器，这使得装饰器的组合更加容易。
3. **简单易用**：提供简单的 API，易于集成到现有代码中。
4. **兼容性**：与 Python 的其他装饰器库（如 `functools.wraps`）兼容。

#### 安装

可以通过pip安装`decorator`：

```bash
pip install decorator
```

#### 基本用法

以下是一些使用 `decorator` 的基本示例：

**参数化装饰器**

```python
from decorator import decorator
def log(func, *args, **kwargs):
    print(f"Calling {func.__name__} with {args} and {kwargs}")
    return func(*args, **kwargs)
@decorator
def memoize(func, *args, **kwargs):
    if not hasattr(func, '_memoize_cache'):
        func._memoize_cache = {}
    key = str(args) + str(kwargs)
    if key not in func._memoize_cache:
        func._memoize_cache[key] = func(*args, **kwargs)
    return func._memoize_cache[key]
@memoize
def add(a, b):
    return a + b
print(add(3, 4))  # 输出: 7
print(add(3, 4))  # 输出: 7
```

在这个例子中，我们定义了一个名为 `log` 的装饰器，它接受一个函数 `func` 作为参数，并打印调用信息。我们使用 `decorator` 库来参数化 `log` 装饰器，使其可以应用于任何函数。然后，我们定义了一个名为 `memoize` 的装饰器，它使用缓存来存储函数的结果，以避免重复计算。

**递归装饰器**

```python
from decorator import decorator
@decorator
def wrapper(func, *args, **kwargs):
    print("Before function")
    result = func(*args, **kwargs)
    print("After function")
    return result
@wrapper
def decorated_function():
    print("Inside function")
decorated_function()  # 输出: Before function, Inside function, After function
```

在这个例子中，我们定义了一个名为 `wrapper` 的装饰器，它打印调用信息并返回函数的结果。我们使用 `decorator` 库来递归地应用 `wrapper` 装饰器，使其可以应用于任何函数。然后，我们定义了一个名为 `decorated_function` 的函数，它被 `wrapper` 装饰器装饰。

#### 使用场景

* **函数修饰**：在需要修改函数行为时使用 `decorator`。
* **日志记录**：在需要记录函数调用信息时使用 `decorator`。
* **缓存**：在需要缓存函数结果时使用 `decorator`。 `decorator` 是一个非常实用的库，它可以帮助 Python 开发者创建参数化和递归的装饰器。由于其简单性和灵活性，`decorator` 在需要修改函数行为的场景中非常有用。
