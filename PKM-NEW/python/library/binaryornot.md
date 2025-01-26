# binaryornot

`binaryornot` 是一个简单的Python库，用于检查文件是否为二进制文件。在处理文件时，区分文本文件和二进制文件是很重要的，因为它们需要不同的处理方式。`binaryornot` 通过检查文件内容来确定文件是否可能是二进制文件。 以下是 `binaryornot` 的一些关键特点和用法：

#### 关键特点

1. **快速检测**：通过读取文件的前几个字节来快速判断文件是否为二进制。
2. **简单易用**：提供了一个简单的API，易于集成到其他应用程序中。
3. **容错性**：即使文件开头包含了一些不可打印的字符，`binaryornot` 也能正确判断。

#### 安装

可以通过pip安装`binaryornot`：

```bash
pip install binaryornot
```

#### 基本用法

以下是一个使用 `binaryornot` 的基本示例：

```python
import binaryornot
# 检查文件是否为二进制
is_binary = binaryornot.is_binary('example.txt')
print('Is binary:', is_binary)
# 你也可以直接使用命令行工具
# binaryornot example.txt
```

在这个例子中，`is_binary` 函数会返回一个布尔值，指示传入的文件路径对应的文件是否为二进制文件。

#### API

* `is_binary(file_path, block_size=1024)`: 这是 `binaryornot` 提供的主要函数，用于检查文件是否为二进制文件。`file_path` 是要检查的文件的路径，`block_size` 是要读取的文件块的大小，默认为 1024 字节。

#### 使用场景

* **文件处理**：在需要区分文本文件和二进制文件的应用程序中使用，例如文件同步工具、备份软件或文件管理系统。
* **数据导入**：在导入数据到数据库或其他系统之前，检查文件类型。
* **自动化脚本**：在自动化脚本中，根据文件类型执行不同的操作。 `binaryornot` 是一个轻量级的库，适用于需要快速确定文件类型的场景。它的实现原理是基于一些常见的二进制文件特征，如控制字符的存在，但这并不是一个完全可靠的检测方法，因为有些文本文件也可能包含少量的二进制数据。因此，`binaryornot` 更适合作为一个初步的检查工具。
