---

---
# Java 解析 json
> 按照老杜网课内容整理

## Java 解析 JSON 的常用库

在Java语言中，常用的JSON解析库有以下几种，每种都有其特点和适用场景：

### Jackson

+ **特点**：高性能、功能全面、社区活跃，支持流式解析（`Streaming API`）、数据绑定（`ObjectMapper`）和树模型。
+ **优点**：速度快，适合处理大规模数据；支持注解配置；与Spring框架深度集成。<font style="color:#DF2A3F;">（Spring 生态默认集成）</font>
+ **缺点**：API略复杂。
+ **示例**：[jackson](jackson.md)

```java
ObjectMapper mapper = new ObjectMapper();
User user = mapper.readValue(jsonString, User.class); // JSON转对象
String json = mapper.writeValueAsString(user); // 对象转JSON
```

### Gson

+ **特点**：Google出品，API简洁，支持对象与JSON的直接转换。
+ **优点**：易用性强，适合简单场景；支持泛型、自定义序列化/反序列化。
+ **缺点**：性能略低于Jackson。
+ **示例**：[gson](gson.md)

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

