# XSLT

XSLT（Extensible Stylesheet Language Transformations）是一种用于将 XML 文档转换为其他格式（如 HTML、XML 或纯文本）的语言。

---

## XSLT 主要用途

1. 将 XML 转换为 HTML 用于网页显示
2. 将 XML 转换为其他 XML 格式
3. 提取和过滤 XML 数据
4. 对 XML 数据进行排序和重组

## 简单 XSLT 示例

### 输入 XML (books.xml)

```xml
<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="transform.xsl"?>
<books>
    <book category="technology">
        <title>XML Basics</title>
        <author>John Doe</author>
        <price>39.95</price>
    </book>
    <book category="fiction">
        <title>XML Adventures</title>
        <author>Jane Smith</author>
        <price>29.99</price>
    </book>
</books>
```

### XSLT 样式表 (transform.xsl)

```xml
<?xml version="1.0"?>
<xsl:stylesheet version="1.0" 
                xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

  <xsl:template match="/">
    <html>
      <head>
        <title>Book List</title>
      </head>
      <body>
        <h1>Book Collection</h1>
        <table border="1">
          <tr>
            <th>Title</th>
            <th>Author</th>
            <th>Price</th>
            <th>Category</th>
          </tr>
          <xsl:for-each select="books/book">
            <tr>
              <td><xsl:value-of select="title"/></td>
              <td><xsl:value-of select="author"/></td>
              <td>$<xsl:value-of select="price"/></td>
              <td><xsl:value-of select="@category"/></td>
            </tr>
          </xsl:for-each>
        </table>
      </body>
    </html>
  </xsl:template>
</xsl:stylesheet>
```

### 转换后的 HTML 输出

```html
<html>
  <head>
    <title>Book List</title>
  </head>
  <body>
    <h1>Book Collection</h1>
    <table border="1">
      <tr>
        <th>Title</th>
        <th>Author</th>
        <th>Price</th>
        <th>Category</th>
      </tr>
      <tr>
        <td>XML Basics</td>
        <td>John Doe</td>
        <td>$39.95</td>
        <td>technology</td>
      </tr>
      <tr>
        <td>XML Adventures</td>
        <td>Jane Smith</td>
        <td>$29.99</td>
        <td>fiction</td>
      </tr>
    </table>
  </body>
</html>

```

