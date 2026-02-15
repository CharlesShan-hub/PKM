# astunparse

`astunparse` 是一个用于 Python 的库，专门用于解析和操作抽象语法树（AST）。这个库是从 Python 源代码分发中的 `unparse` 分解出来的版本，用于将 AST 转换回源代码。它主要与 Python 2.6 到 Python 3.5 版本兼容。

这个库的主要特点包括：

1. **AST 解析和操作**：`astunparse` 能够解析 Python 代码的 AST，并提供操作这些节点的功能。
2. **源代码转换**：它能够将 AST 转换回原始的源代码，这对于理解和操作代码非常有用。
3. **兼容性**：与 Python 2.6 到 Python 3.5 版本兼容，适用于多个版本的 Python。

例如，你可以使用 `astunparse.unparse(ast.parse(inspect.getsource(ast)))` 来将 AST 转换回源代码，或者使用 `astunparse.dump(ast.parse(inspect.getsource(ast)))` 来获取 AST 的漂亮打印输出。

要安装 `astunparse`，你可以使用 pip 命令：

```bash
pip install astunparse
```

更多信息和文档可以在 `astunparse` 的官方文档页面中找到。
