---

---
# Java 解析 json
> 按照老杜网课内容整理

---

## JSON 概述

### 什么是JSON

* **JSON**（JavaScript Object Notation）是一种轻量级的数据交换格式，它基于 **ECMAScript** 的一个子集，采用完全独立于编程语言的文本格式来存储和表示数据。
* JSON的特点
    + 易于人阅读和编写
    + 易于机器解析和生成
    + 比XML更小、更快、更易解析

### JSON的语法格式

1. 数据以键值对形式存在 `"key": value`（注意：合法的 JSON 字符串中的 key 必须使用双引号括起来）
2. 数据由逗号分隔 `,`
3. 大括号 `{}` 保存对象（无序的键值对集合）
4. 中括号 `[]` 保存数组（有序的值集合）

### JSON支持的数据类型

+ 字符串（必须用双引号）
+ 数字（整数或浮点数）
+ 布尔值（true/false）
+ 数组（在方括号中）
+ 对象（在花括号中）
+ null

### JSON 示例

```json
{
  "name": "张三",
  "age": 20,
  "isStudent": false,
  "hobbies": ["读书", "游泳", "编程"],
  "address": {
    "street": "人民路123号",
    "city": "北京",
    "postalCode": "100000"
  },
  "languages": [
    {"name": "中文", "level": "母语"},
    {"name": "英语", "level": "流利"}
  ],
  "hasCar": null
}
```

### JSON的应用场景

1. **Web API数据传输**：大多数现代Web API使用JSON作为数据交换格式
2. **配置文件**：许多应用程序使用JSON格式存储配置
3. **NoSQL数据库**：如MongoDB使用类似JSON的BSON格式存储数据
4. **前后端数据交互**：前端JavaScript与后端服务之间的数据交换
5. **移动应用开发**：移动APP与服务器之间的通信
6. **日志存储**：结构化日志常以JSON格式存储
7. **序列化和反序列化**：在不同系统间传递对象数据

JSON由于其简洁性和易用性，已成为现代Web开发中最流行的数据交换格式之一。

---

## XML 与 JSON 优缺点

### XML的优点

1. **格式统一，标准完善**：XML格式统一，符合W3C标准，被广泛接受和采用。
2. **强大的数据描述能力**：XML具有极强的数据描述能力，易于理解和验证，特别适合描述复杂的数据结构。
3. **扩展性强**：支持自定义标签和命名空间，具有极强的扩展性，可以通过定义新的标签和命名空间来适应不同的需求。
4. **支持混合内容**：能够记录混合内容（mixed content），例如在XML中处理包含结构化标记的字符串时非常方便。
5. **成熟的生态系统**：有丰富的标准支持，包括XML Schema、DTD、XPath、XQuery、XSLT等，以及DOM、SAX、StAX等解析标准。
6. **命名空间支持**：允许在同一文档中混合由多个源读取或写入的数据，适合复杂的企业级应用。
7. **行业广泛应用**：在文档处理（如Microsoft Word）、Web服务（如SOAP）等领域仍是主要格式。

### XML的缺点

1. **冗余度高**：XML文件庞大，格式复杂，包含大量冗余标签，传输占用带宽较多。
2. **解析复杂**：服务器端和客户端都需要花费大量代码来解析XML，代码复杂且不易维护。
3. **资源消耗大**：解析XML花费较多的计算资源和时间，特别是在处理大型文档时。
4. **浏览器兼容性问题**：不同浏览器之间解析XML的方式可能不一致，需要额外的兼容性处理。
5. **学习曲线陡峭**：完整的XML技术栈（Schema、XPath、XSLT等）学习成本较高。

### JSON的优点

1. **轻量简洁**：数据格式简单，冗余少，占用带宽小，传输效率高。
2. **易于解析**：解析JSON非常简单快速，特别是在JavaScript中可以直接转换为对象。
3. **与JavaScript无缝集成**：作为JavaScript的子集，在Web开发中处理非常自然。
4. **数据类型支持**：天然支持常见的数据类型（字符串、数字、布尔值、数组、对象等），无需额外定义。
5. **开发效率高**：大大简化了服务器端和客户端的代码开发量，易于维护。
6. **性能优势**：序列化和反序列化速度显著优于XML，CPU和内存资源消耗更少。
7. **适合现代Web应用**：特别适合前后端分离架构和RESTful API设计。

### JSON的缺点

1. **缺乏某些高级特性**：不支持注释、命名空间、属性等XML具有的特性。
2. **模式支持有限**：虽然JSON Schema存在，但不如XML Schema成熟和强大。
3. **不适合复杂文档**：对复杂数据结构（如嵌套多层的数据）可能不够直观和易读。
4. **安全性问题**：直接使用eval()解析JSON可能存在安全风险（虽然可以用JSON.parse()避免）。
5. **企业级支持不足**：在某些企业环境和传统系统中支持不如XML广泛。

### 应用场景选择建议

选择XML
1. 需要严格的数据验证和行业标准XSD支持时
2. 处理文档型数据（如Office文档）或需要混合内容时
3. 在企业级系统集成中，特别是使用SOAP等传统Web服务时
4. 需要利用XSLT进行数据转换时
5. 在需要命名空间支持的多源数据集成场景中

选择JSON
1. 开发Web或移动应用，特别是前后端数据交互时
2. 需要轻量级解决方案，追求性能和简洁性时
3. 使用JavaScript或与JavaScript生态系统紧密集成的技术栈时
4. 在NoSQL数据库（如MongoDB）中存储数据时
5. 开发RESTful API或微服务架构时

### 未来趋势

从搜索结果来看，JSON在Web开发领域已经取得了明显优势，特别是在前后端分离、移动应用和API设计方面。随着JavaScript全栈开发（如Node.js）和NoSQL数据库（如MongoDB）的流行，JSON的使用场景还在不断扩大。

然而，XML在文档处理、企业级应用和某些特定行业（如金融、医疗）中仍占据重要地位。两者的关系更多是互补而非替代，开发者应根据具体需求选择合适的工具。

---

## JavaScript 解析 JSON

### JavaScript 对象转换为 JSON

```javascript
const myObject = {
  name: "张三",
  age: 30,
  city: "北京"
};

// 将对象转换为 JSON 字符串
const jsonString = JSON.stringify(myObject);

console.log(jsonString);
// 输出: {"name":"张三","age":30,"city":"北京"}
```

### JSON 转换为 JavaScript 对象

```javascript
const jsonString = '{"name":"张三","age":30,"city":"北京"}';

// 将 JSON 字符串转换为 JavaScript 对象
const jsObject = JSON.parse(jsonString);

console.log(jsObject.name); // 输出: "张三"
console.log(jsObject.age);  // 输出: 30
```

---

## Java 解析 JSON 的常用库

在Java语言中，常用的JSON解析库有以下几种，每种都有其特点和适用场景：

### Jackson

+ **特点**：高性能、功能全面、社区活跃，支持流式解析（`Streaming API`）、数据绑定（`ObjectMapper`）和树模型。
+ **优点**：速度快，适合处理大规模数据；支持注解配置；与Spring框架深度集成。<font style="color:#DF2A3F;">（Spring 生态默认集成）</font>
+ **缺点**：API略复杂。
+ **示例**：

```java
ObjectMapper mapper = new ObjectMapper();
User user = mapper.readValue(jsonString, User.class); // JSON转对象
String json = mapper.writeValueAsString(user); // 对象转JSON
```

### Gson

+ **特点**：Google出品，API简洁，支持对象与JSON的直接转换。
+ **优点**：易用性强，适合简单场景；支持泛型、自定义序列化/反序列化。
+ **缺点**：性能略低于Jackson。
+ **示例**：

```java
Gson gson = new Gson();
User user = gson.fromJson(jsonString, User.class); // JSON转对象
String json = gson.toJson(user); // 对象转JSON
```

### org.json (JSON-Java)

+ **特点**：Java官方提供的轻量级库，API简单。
+ **优点**：无需额外依赖，适合小型项目。
+ **缺点**：功能较少，不支持对象直接映射；性能一般。
+ **示例**：

```java
JSONObject obj = new JSONObject(jsonString);
String name = obj.getString("name");
```

### JSON.simple

+ **特点**：轻量级，符合JSON规范，适合简单读写。
+ **优点**：体积小，学习成本低。
+ **缺点**：功能有限，不支持复杂对象映射。
+ **示例**：

```java
JSONObject obj = (JSONObject) JSONValue.parse(jsonString);
String name = (String) obj.get("name");
```

### Fastjson

+ **特点**：阿里巴巴开源，号称最快的JSON库。（Fastjson曾多次曝出漏洞，生产环境建议用Jackson或Gson）
+ **优点**：性能极佳，支持对象直接映射。
+ **缺点**：安全性曾曝出漏洞（需及时更新版本）；社区活跃度下降。
+ **示例**：

```java
User user = JSON.parseObject(jsonString, User.class); // JSON转对象
String json = JSON.toJSONString(user); // 对象转JSON
```

### JSON-B (Java EE标准)

+ **特点**：Java EE的JSON绑定标准（JSR 367），类似JAXB for XML。
+ **优点**：标准化，与Java EE生态集成好（如Jakarta EE）。
+ **缺点**：依赖容器，灵活性较低。
+ **示例**：

```java
Jsonb jsonb = JsonbBuilder.create();
User user = jsonb.fromJson(jsonString, User.class);
```

### Moshi

+ **特点**：Square公司出品，专注于JSON绑定，支持Kotlin。
+ **优点**：轻量、模块化设计，适合Android或Kotlin项目。
+ **缺点**：Java生态中不如Jackson/Gson流行。
+ **示例**：

```java
Moshi moshi = new Moshi.Builder().build();
JsonAdapter<User> adapter = moshi.adapter(User.class);
User user = adapter.fromJson(jsonString);
```

---

## Jackson 解析 JSON

Jackson 库解析 JSON 需要引入以下 jar 包：

```xml
<!-- Jackson 核心：必须的 -->
<dependency>
    <groupId>com.fasterxml.jackson.core</groupId>
    <artifactId>jackson-core</artifactId>
    <version>2.16.1</version>
</dependency>

<!-- Jackson 数据绑定：将 JSON 与对象互转 -->
<dependency>
    <groupId>com.fasterxml.jackson.core</groupId>
    <artifactId>jackson-databind</artifactId>
    <version>2.16.1</version>
</dependency>

<!-- Jackson 注解支持 -->
<dependency>
    <groupId>com.fasterxml.jackson.core</groupId>
    <artifactId>jackson-annotations</artifactId>
    <version>2.16.1</version>
</dependency>
```

**简化写法**：`jackson-databind`会自动引入 `jackson-core`和 `jackson-annotations`，所以通常只需要：

```xml
<dependency>
    <groupId>com.fasterxml.jackson.core</groupId>
    <artifactId>jackson-databind</artifactId>
    <version>2.16.1</version>
</dependency>
```

### 实体类的定义

```java
package com.laodu.jackson;

import java.util.List;

public class Person {
    private String name;
    private int age;
    private String email;
    private Address address;
    private List<String> hobbies;

    // 必须有无参构造函数
    public Person() {}

    // setter and getter
}

```

```java
package com.laodu.jackson;

public class Address {
    private String street;
    private String city;

    public Address() {}

    // setter and getter
}
```

### Java 对象转换为 JSON

```java
package com.laodu.jackson;

import com.fasterxml.jackson.databind.ObjectMapper;

import java.util.List;

public class JavaToJsonExample {
    public static void main(String[] args) throws Exception {
        // 1. 创建 Person 对象
        Address address = new Address();
        address.setStreet("123 Main St");
        address.setCity("New York");

        Person person = new Person();
        person.setName("Alice");
        person.setAge(30);
        person.setEmail("alice@example.com");
        person.setAddress(address);
        person.setHobbies(List.of("Reading", "Hiking"));

        // 2. 使用 Jackson 转换为 JSON 字符串
        ObjectMapper mapper = new ObjectMapper();
        String jsonString = mapper.writerWithDefaultPrettyPrinter().writeValueAsString(person);

        // 3. 打印结果
        System.out.println("JSON 字符串：\n" + jsonString);
    }
}

```

### JSON 转换为 Java 对象

```java
package com.laodu.jackson;

import com.fasterxml.jackson.databind.ObjectMapper;

public class JsonToJavaExample {
    public static void main(String[] args) throws Exception {
        // 1. 模拟 JSON 字符串
        String jsonString = """
                {
                  "name" : "Bob",
                  "age" : 25,
                  "email" : "bob@example.com",
                  "address" : {
                    "street" : "456 Oak Ave",
                    "city" : "Los Angeles"
                  },
                  "hobbies" : [ "Gaming", "Swimming" ]
                }
                """;

        // 2. 使用 Jackson 解析为 Java 对象
        ObjectMapper mapper = new ObjectMapper();
        // 这里需要注意的是：Person 需要保证存在无参数构造方法。
        Person person = mapper.readValue(jsonString, Person.class);

        // 3. 验证结果
        System.out.println("Person 对象：");
        System.out.println("Name: " + person.getName());
        System.out.println("Age: " + person.getAge());
        System.out.println("Address: " + person.getAddress().getStreet() + ", " + person.getAddress().getCity());
        System.out.println("Hobbies: " + person.getHobbies());
    }
}
```

---

## Gson 解析 JSON

Google出品，API简洁，支持对象与JSON的直接转换。

需要引入坐标

```xml
<dependency>
    <groupId>com.google.code.gson</groupId>
    <artifactId>gson</artifactId>
    <version>2.10.1</version>
</dependency>
```

API 超级简单

```java
Gson gson = new Gson();
User user = gson.fromJson(jsonString, User.class); // JSON转对象
String json = gson.toJson(user); // 对象转JSON
```

到此为止，XML 与 JSON 的课程内容就结束了。
