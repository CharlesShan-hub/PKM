# bleach

`Bleach` 是一个 Python 库，用于清理 HTML 文本，并防止跨站脚本攻击（XSS）。它通过剥离或转义 HTML 中潜在的危险内容来实现这一目的。`Bleach` 通常用于需要处理用户输入的 Web 应用程序，以确保这些输入在显示给其他用户之前是安全的。 以下是 `Bleach` 的一些关键特点和用法：

#### 关键特点

1. **HTML 清理**：移除 HTML 标签和属性，留下纯文本内容。
2. **白名单过滤**：允许开发者定义一个白名单，只允许特定的 HTML 标签和属性。
3. **链接转换**：将 URL 和邮箱地址转换为链接。
4. **跨站脚本攻击防护**：防止 XSS 攻击，通过清理潜在的 JavaScript 代码和其他危险内容。
5. **灵活性**：可以很容易地集成到现有的 Web 应用程序中。

#### 安装

可以通过pip安装`Bleach`：

```bash
pip install bleach
```

#### 基本用法

以下是一些使用 `Bleach` 的基本示例：

**清理 HTML**

```python
import bleach
dirty_html = "<script>alert('xss');</script><p>Safe content</p>"
clean_html = bleach.clean(dirty_html)
print(clean_html)
```

这个例子中，`bleach.clean` 函数会移除 `<script>` 标签并返回安全的 HTML 内容。

**使用白名单**

```python
allowed_tags = ['p', 'b', 'i', 'u']
allowed_attrs = {'p': ['class'], 'a': ['href', 'title']}
clean_html = bleach.clean(dirty_html, tags=allowed_tags, attributes=allowed_attrs)
print(clean_html)
```

在这个例子中，`bleach.clean` 函数只允许指定的标签和属性，其他所有内容都会被清理掉。

**转换链接**

```python
linkified_html = bleach.linkify(dirty_html)
print(linkified_html)
```

这个例子中，`bleach.linkify` 函数会将文本中的 URL 和邮箱地址转换为 HTML 链接。

#### 使用场景

* **Web 应用程序**：在处理用户提交的 HTML 内容时，使用 `Bleach` 来清理并防止 XSS 攻击。
* **内容管理系统**：在 CMS 中，`Bleach` 可以用来清理用户生成的内容，同时保留必要的 HTML 标签。
* **论坛和评论系统**：在论坛和评论系统中，`Bleach` 可以确保用户输入的内容不会包含恶意代码。 `Bleach` 是一个强大的工具，用于在 Web 应用程序中处理和显示用户生成的 HTML 内容，同时保护应用程序免受 XSS 攻击。
