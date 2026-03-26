# Java 解析 XML

Java 解析 XML 指的是：Java 读取 XML。

---

## Java 解析 XML 的抽象规范

|**名称**​|**类型**​|**定义内容**​|**归属组织**​|
|---|---|---|---|
|**JAXP**​|统一工厂接口|提供 **SAXParserFactory**, **DocumentBuilderFactory**, **TransformerFactory**  <br>是 **抽象工厂**，不包含具体实现，通过 SPI 加载底层解析器。  <br>**SPI（Service Provider Interface）**​ 是 Java 提供的一种**服务发现机制**，用于解耦接口与实现，让第三方可以为标准接口提供具体实现，并由 Java 自动加载。它在 XML 解析（如 JAXP）、JDBC 驱动等场景中广泛使用。  <br>**SPI 与 API 的区别**：SPI 的接口由标准库定义，实现由第三方提供，典型场景JAXP、JDBC 驱动、日志框架（SLF4J）。 API 的接口和实现均由同一方提供，典型场景Java 集合类、IO 流等标准库。|Oracle (Java 标准库)|
|**DOM**​|树形结构解析规范|定义 **Document**, **Element**, **Node**​ 等 W3C 标准接口|W3C|
|**SAX**​|事件驱动解析规范|定义 **ContentHandler**, **ErrorHandler**​ 等回调接口|SAX 开源社区|
|**StAX**​|流式推拉模型规范|定义 **XMLStreamReader**（拉模式）, **XMLEventReader**（推模式）|JSR-173 (Java 标准)|
|**XPath**​|查询语言规范|定义 **XPathExpression**, **XPathNodes**​ 等查询接口  <br>**注意：只有 DOM 解析中才需要 XPath**​|W3C|

---

## Java 解析 XML 的具体库

| **实现库名称**​            | **实现的规范**​     | **支持解析方式**​    | **开发团队**​             | **JDK 内置**​ | **特点**​                               |
| --------------------- | -------------- | -------------- | --------------------- | ----------- | ------------------------------------- |
| **DOM4J**​            | DOM (扩展)       | DOM + XPath    | MetaStuff             | 否           | API 更友好，性能优于 W3C DOM，Hibernate 等框架曾使用 |
| **JDOM**​             | DOM (简化版)      | DOM            | Jason Hunter 等        | 否           | 专为 Java 优化，使用 **List**​ 等集合类简化操作      |
| **XOM**​              | DOM (严格规范)     | DOM            | Elliotte Rusty Harold | 否           | 严格遵循 XML 规范，轻量级                       |
| **Woodstox**​         | StAX           | StAX（推拉模型）     | FasterXML             | 否           | 高性能 StAX 实现，适合大数据流式解析                 |
| **Xerces**​           | SAX, DOM       | SAX, DOM       | Apache                | 否           | 历史最久，JDK 早期默认实现                       |
| **JDK 内置解析器（JDK9+）**​ | SAX, DOM, StAX | SAX, DOM, StAX | Oracle                | 是           | 包名前缀：**jdk.xml.internal**​            |

---

## DOM4J 解析 XML(DOM+XPath)

以第三方库 DOM4J（DOM for java） 来演示 DOM 解析。解析时采用 DOM+XPath 方式。

### XPath

XPath（XML Path Language）是一种用于在XML文档中定位节点的查询语言。在DOM4J解析XML时，XPath提供了一种简洁高效的方式来查找和选择XML文档中的特定节点或节点集，而不需要手动遍历整个DOM树。

常见XPath表达式

1. 基本路径表达
    - `//book`：选择文档中所有的book元素
    - `/bookstore/book`：选择根元素bookstore下的所有book子元素
    - `book/title`：选择当前节点下book元素的title子元素
2. 条件筛选
    - `//book[1]`：选择第一个book元素
    - `//book[last()]`：选择最后一个book元素
    - `//book[price>35]`：选择price大于35的book元素
    - `//book[@category='WEB']`：选择category属性为WEB的book元素
3. 通配符
    - `//*`：选择文档中的所有元素
    - `//book/*`：选择book元素的所有子元素
    - `//@*`：选择所有的属性
4. 轴选择
    - `//book/title | //book/price`：选择所有book的title和price元素
    - `//title/../@category`：选择title父元素的category属性
5. 函数
    - `//book[contains(title, 'XML')]`：选择 title 元素的文本内容包含"XML"的book元素
    - `//book[starts-with(title, 'Java')]`：选择title 元素的文本内容以"Java"开头的book元素
    - `//book[string-length(title) > 10]`：选择title 元素的文本内容长度大于10的book元素

### DOM+XPath 解析

要使用 DOM4J，需要引入它的 jar 包，Maven坐标如下

```xml
<!-- DOM4J 核心 -->
<dependency>
    <groupId>org.dom4j</groupId>
    <artifactId>dom4j</artifactId>
    <version>2.1.4</version>
</dependency>

<!-- XPath 支持（必须，否则无法使用XPath） -->
<!-- 从 DOM4J 2.0.0 开始，XPath 功能被拆分到了单独的模块。 -->
<dependency>
    <groupId>jaxen</groupId>
    <artifactId>jaxen</artifactId>
    <version>1.2.0</version>
</dependency>
```

XML 文件

```xml
<?xml version="1.0" encoding="UTF-8"?>
<bookstore>
    <book category="COOKING">
        <title lang="en">Everyday Italian</title>
        <author>Giada De Laurentiis</author>
        <year>2005</year>
        <price>30.00</price>
    </book>
    <book category="CHILDREN">
        <title lang="en">Harry Potter</title>
        <author>J.K. Rowling</author>
        <year>2005</year>
        <price>29.99</price>
    </book>
    <book category="WEB">
        <title lang="en">Learning XML</title>
        <author>Erik T. Ray</author>
        <year>2003</year>
        <price>39.95</price>
    </book>
    <book category="WEB">
        <title lang="en">XQuery Kick Start</title>
        <author>James McGovern</author>
        <year>2003</year>
        <price>49.99</price>
    </book>
</bookstore>
```

Java 代码：

```java
package top.charles;
  
import org.dom4j.Document;
import org.dom4j.DocumentException;  
import org.dom4j.Node;  
import org.dom4j.io.SAXReader;  
import java.io.InputStream;  
import java.util.List;  

public class Dom4jXpathExample {  
    public static void main(String[] args) {  
        try {  
            // 1. 获取类加载器  
            ClassLoader classLoader = Dom4jXpathExample.class.getClassLoader();  
  
            // 2. 获取 resources 目录下的 XML 文件流  
            InputStream inputStream = classLoader.getResourceAsStream("Book.xml");
  
            if (inputStream == null) {
                System.out.println("错误: 在 classpath/resources 目录下找不到 Book.xml 文件");
                System.out.println("请确保 Book.xml 文件在 src/main/resources/ 目录下");
                return;
            }

            // 3. 创建 SAXReader 对象
            // 注意：DOM4J 的 SAXReader 不是纯 SAX 解析，而是 SAX + DOM 混合模式。
            // 它底层用 SAX 高效读取 XML，但最终构建 DOM4J 的 Document 对象，支持 XPath 查询。
            SAXReader reader = new SAXReader();
            
            // 4. 从 InputStream 加载 XML 文件
            Document document = reader.read(inputStream);
            
            // 5. 关闭输入流
            inputStream.close();
  
            System.out.println("=== 所有书籍标题 ===");  
  
            // 6. 使用 XPath 选择所有 title 元素  
            List<Node> titleNodes = document.selectNodes("//book/title");  
            for (Node node : titleNodes) {  
                System.out.println(node.getText());  
            }  
  
            System.out.println("\n=== 价格超过 35 的书籍 ===");  
  
            // 7. 使用 XPath 选择价格 > 35 的书籍  
            List<Node> expensiveBooks = document.selectNodes("//book[price>35]");  
            for (Node book : expensiveBooks) {  
                String title = book.selectSingleNode("title").getText();  
                String price = book.selectSingleNode("price").getText();  
                System.out.println(title + " - 价格: " + price);  
            }  
  
            System.out.println("\n=== WEB 类别的书籍 ===");  
  
            // 8. 使用属性选择  
            List<Node> webBooks = document.selectNodes("//book[@category='WEB']");  
            for (Node book : webBooks) {  
                String title = book.selectSingleNode("title").getText();  
                String author = book.selectSingleNode("author").getText();  
                System.out.println(title + " - 作者: " + author);  
            }  
  
            // 9. 获取单个节点  
            Node firstBook = document.selectSingleNode("//book[1]");  
            System.out.println("\n第一本书的类别: " + firstBook.valueOf("@category"));  
  
        } catch (Exception e) {
            e.printStackTrace();  
        }  
    }  
}
```

---

## JDK 内置解析器 SAX 解析

以 JDK 内置解析器为例，演示 SAX 解析。XML 文件

```xml
<?xml version="1.0" encoding="UTF-8"?>
<bookstore>
    <book category="COOKING">
        <title lang="en">Everyday Italian</title>
        <author>Giada De Laurentiis</author>
        <year>2005</year>
        <price>30.00</price>
    </book>
    <book category="CHILDREN">
        <title lang="en">Harry Potter</title>
        <author>J.K. Rowling</author>
        <year>2005</year>
        <price>29.99</price>
    </book>
    <book category="WEB">
        <title lang="en">Learning XML</title>
        <author>Erik T. Ray</author>
        <year>2003</year>
        <price>39.95</price>
    </book>
</bookstore>
```

Java 代码。要自己重写Handler，在回调函数里边处理内容。

```java
package top.charles;  
  
import org.xml.sax.Attributes;  
import org.xml.sax.SAXException;  
import org.xml.sax.helpers.DefaultHandler;  
  
import javax.xml.parsers.SAXParser;  
import javax.xml.parsers.SAXParserFactory;  
import java.io.InputStream;  
  
public class SAXParserExample {  
  
    public static void main(String[] args) {  
        try {  
            // 1. 创建SAXParserFactory实例  
            SAXParserFactory factory = SAXParserFactory.newInstance();  
  
            // 2. 创建SAXParser实例  
            SAXParser saxParser = factory.newSAXParser();  
  
            // 3. 创建自定义的Handler  
            BookHandler handler = new BookHandler();  
  
            // 4. 从 resources 目录获取 XML 文件流  
            ClassLoader classLoader = SAXParserExample.class.getClassLoader();  
            InputStream inputStream = classLoader.getResourceAsStream("Book.xml");  
  
            if (inputStream == null) {  
                System.out.println("错误: 在 classpath/resources 目录下找不到 books.xml 文件");  
                System.out.println("请确保 books.xml 文件在 src/main/resources/ 目录下");  
                return;  
            }  
  
            // 5. 解析XML文件（从 InputStream）  
            saxParser.parse(inputStream, handler);  
  
            // 6. 关闭流  
            inputStream.close();  
  
        } catch (Exception e) {  
            e.printStackTrace();  
        }  
    }  
}  
  
// 自定义Handler类，继承DefaultHandler  
class BookHandler extends DefaultHandler {
  
    private String currentElement;  
    private StringBuilder currentText;  
  
    @Override  
    public void startDocument() throws SAXException {  
        System.out.println("开始解析文档");  
        currentText = new StringBuilder();  
    }  
  
    @Override  
    public void endDocument() throws SAXException {  
        System.out.println("文档解析结束");  
    }  
  
    @Override  
    public void startElement(String uri, String localName, String qName, Attributes attributes) throws SAXException {  
  
        currentElement = qName;  
        currentText.setLength(0);  
  
        if ("book".equals(qName)) {  
            String category = attributes.getValue("category");  
            System.out.println("\nBook Category: " + category);  
        } else if ("title".equals(qName) && attributes.getLength() > 0) {  
            String lang = attributes.getValue("lang");  
            System.out.println("Title Language: " + lang);  
        }  
    }  
  
    @Override  
    public void endElement(String uri, String localName, String qName) throws SAXException {  
  
        if ("title".equals(qName)) {  
            System.out.println("Title: " + currentText.toString().trim());  
        } else if ("author".equals(qName)) {  
            System.out.println("Author: " + currentText.toString().trim());  
        } else if ("year".equals(qName)) {  
            System.out.println("Year: " + currentText.toString().trim());  
        } else if ("price".equals(qName)) {  
            System.out.println("Price: " + currentText.toString().trim());  
        }  
    }  
  
    @Override  
    public void characters(char[] ch, int start, int length) throws SAXException {  
        currentText.append(ch, start, length);  
    }  
}
```

---

## JDK 内置解析器 StAX 解析

以 JDK 内置解析器为例，演示 StAX 解析。

XML 文件：

```xml
<?xml version="1.0" encoding="UTF-8"?>
<library>
    <book id="101">
        <title>Java Programming</title>
        <author>James Gosling</author>
        <published>2020</published>
        <price>49.99</price>
    </book>
    <book id="102">
        <title>Effective Java</title>
        <author>Joshua Bloch</author>
        <published>2018</published>
        <price>39.95</price>
    </book>
    <book id="103">
        <title>Head First Design Patterns</title>
        <author>Eric Freeman</author>
        <published>2021</published>
        <price>45.50</price>
    </book>
</library>
```

Java 代码：

```java
import javax.xml.stream.XMLInputFactory;
import javax.xml.stream.XMLStreamConstants;
import javax.xml.stream.XMLStreamException;
import javax.xml.stream.XMLStreamReader;
import java.io.InputStream;

public class StAXParserExample {

    public static void main(String[] args) {
        InputStream inputStream = null;
        XMLStreamReader reader = null;
        
        try {
            // 1. 创建XMLInputFactory实例
            XMLInputFactory factory = XMLInputFactory.newInstance();
            
            // 可选：配置工厂
            factory.setProperty(XMLInputFactory.IS_COALESCING, true);  // 合并连续文本
            factory.setProperty(XMLInputFactory.IS_NAMESPACE_AWARE, false);  // 不启用命名空间

            // 2. 从 resources 目录获取 XML 文件流
            ClassLoader classLoader = StAXParserExample.class.getClassLoader();
            inputStream = classLoader.getResourceAsStream("books.xml");
            
            if (inputStream == null) {
                System.out.println("错误: 在 classpath/resources 目录下找不到 books.xml 文件");
                System.out.println("请确保 books.xml 文件在 src/main/resources/ 目录下");
                return;
            }

            // 3. 创建XMLStreamReader（拉模式）（如果是EventReader，那就是推模式）
            reader = factory.createXMLStreamReader(inputStream);

            // 4. 解析XML
            parseXML(reader);

        } catch (Exception e) {
            e.printStackTrace();
        } finally {
            // 5. 关闭资源
            try {
                if (reader != null) {
                    reader.close();
                }
                if (inputStream != null) {
                    inputStream.close();
                }
            } catch (Exception e) {
                e.printStackTrace();
            }
        }
    }

    private static void parseXML(XMLStreamReader reader) throws XMLStreamException {
        String currentElement = null;
        StringBuilder textContent = new StringBuilder();

        while (reader.hasNext()) {
            int event = reader.next();

            switch (event) {
                case XMLStreamConstants.START_ELEMENT:
                    currentElement = reader.getLocalName();
                    System.out.println("Start Element: " + currentElement);

                    // 处理所有属性
                    int attributeCount = reader.getAttributeCount();
                    for (int i = 0; i < attributeCount; i++) {
                        String attrName = reader.getAttributeLocalName(i);
                        String attrValue = reader.getAttributeValue(i);
                        System.out.println("  Attribute: " + attrName + " = '" + attrValue + "'");
                    }
                    break;

                case XMLStreamConstants.CHARACTERS:
                    // 注意：这里不直接trim，因为可能有空白字符
                    textContent.append(reader.getText());
                    break;

                case XMLStreamConstants.END_ELEMENT:
                    String elementName = reader.getLocalName();
                    String text = textContent.toString().trim();

                    if (!text.isEmpty()) {
                        System.out.println("  " + elementName + ": " + text);
                    }
                    System.out.println("End Element: " + elementName);

                    textContent.setLength(0); // 清空内容缓存
                    break;

                case XMLStreamConstants.START_DOCUMENT:
                    System.out.println("开始解析文档...");
                    break;

                case XMLStreamConstants.END_DOCUMENT:
                    System.out.println("文档解析结束。");
                    break;
            }
        }
    }
}
```
