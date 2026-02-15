# asttokens

`asttokens` 是一个用于 Python 的库，它能够为抽象语法树（AST）添加源代码的位置信息，包括标记和文本。这个库的主要目的是让那些处理逻辑 AST 节点的工具能够找到导致这些节点的特定文本。例如，它可用于自动化重构或突出显示。 `asttokens` 的主要特点包括：

1. **源代码位置信息**：它为 AST 添加了源代码的位置信息，包括标记和文本，使得处理 AST 的工具能够更准确地定位和操作代码。
2. **兼容性**：`asttokens` 兼容 Python 2 和 Python 3，并能够为由 `ast` 和 `astroid` 库构建的 AST 树添加标记。
3. **使用方式**：你可以通过导入 `asttokens` 和 `ast` 库来使用它。一旦树被标记，节点将获得 `.firsttoken` 和 `.lasttoken` 属性，并提供一些有用的方法来操作它们。 例如，你可以使用 `asttokens.ASTTokens(source, parseTrue)` 来标记树，然后使用 `atok.gettext(attrnode)` 来获取节点的源文本，以及 `attrnode.lasttoken.startpos` 和 `attrnode.lasttoken.endpos` 来获取节点的开始和结束位置。 要安装 `asttokens`，你可以使用 pip 命令：

```bash
pip install asttokens
```

更多信息和文档可以在 `asttokens` 的官方文档页面中找到。
