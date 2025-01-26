# debugpy

`debugpy` 是一个 Python 库，用于调试远程 Python 应用程序。它允许你从远程主机或容器中调试 Python 应用程序，而不需要将应用程序复制到本地机器。`debugpy` 支持多种调试模式，包括交互式调试、断点设置、变量检查和代码执行控制。 以下是 `debugpy` 的关键特点和用法：

#### 关键特点

1. **远程调试**：允许你从远程主机或容器中调试 Python 应用程序。
2. **多种调试模式**：支持交互式调试、断点设置、变量检查和代码执行控制。
3. **兼容性**：与 Python 的其他调试库（如 `pdb` 和 `pydevd`）兼容。
4. **简单易用**：提供简单的 API，易于集成到现有代码中。

#### 安装

可以通过pip安装`debugpy`：

```bash
pip install debugpy
```

#### 基本用法

以下是一些使用 `debugpy` 的基本示例：

**启动调试服务器**

```python
import debugpy
# 启动调试服务器
debugpy.listen(5678)
```

在这个例子中，我们使用 `debugpy.listen` 函数来启动一个调试服务器，监听端口 5678。

**连接到调试服务器**

```python
import debugpy
# 连接到调试服务器
debugpy.connect(5678)
```

在这个例子中，我们使用 `debugpy.connect` 函数来连接到一个已启动的调试服务器，指定端口 5678。

#### 使用场景

* **远程调试**：在需要远程调试 Python 应用程序时使用 `debugpy`。
* **容器调试**：在需要调试运行在容器中的 Python 应用程序时使用 `debugpy`。
* **团队协作**：在团队协作中，使用 `debugpy` 来远程调试和协作。 `debugpy` 是一个非常实用的库，它可以帮助 Python 开发者远程调试应用程序。由于其简单性和远程调试能力，`debugpy` 在需要远程协作和调试的场景中非常有用。
