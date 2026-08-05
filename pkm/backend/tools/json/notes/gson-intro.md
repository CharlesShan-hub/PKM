## Part 1：快速上手

> 目标：5 分钟跑通 Gson 基本流程，知道怎么用，不深入原理。

---

### 1.1 引入依赖

**Maven**：

```xml
<dependency>
    <groupId>com.google.code.gson</groupId>
    <artifactId>gson</artifactId>
    <version>2.10.1</version>
</dependency>
```

**Gradle**：

```groovy
implementation 'com.google.code.gson:gson:2.10.1'
```

---

### 1.2 最简示例：对象 ↔ JSON

```java
// 定义一个简单的 POJO
public class User {
    private String name;
    private int age;
    // 必须有默认构造器（无参构造）
    // getter/setter 可省略，Gson 通过反射直接访问字段
}

// 使用
Gson gson = new Gson();

// 对象 → JSON
User user = new User("张三", 25);
String json = gson.toJson(user);
// 输出: {"name":"张三","age":25}

// JSON → 对象
User user2 = gson.fromJson(json, User.class);
```

> 💡 注意：Gson 不强制要求 getter/setter，直接通过反射读取字段值。但**必须有默认构造器**（无参构造），否则反序列化会失败。

---

### 1.3 常见场景速览

#### 1.3.1 List / Map 转换

```java
// List → JSON
List<String> list = Arrays.asList("a", "b", "c");
String json = gson.toJson(list);  // ["a","b","c"]

// JSON → List（注意泛型）
List<String> list2 = gson.fromJson(json, new TypeToken<List<String>>(){}.getType());

// Map → JSON
Map<String, Object> map = new HashMap<>();
map.put("name", "张三");
map.put("age", 25);
String json2 = gson.toJson(map);  // {"name":"张三","age":25}
```

#### 1.3.2 复杂嵌套对象

```java
public class Order {
    private int id;
    private User user;          // 嵌套对象
    private List<Item> items;   // 嵌套 List
}
public class Item {
    private String name;
    private double price;
}

// 直接互转，Gson 自动递归处理嵌套
Order order = gson.fromJson(json, Order.class);
String json = gson.toJson(order);
```

#### 1.3.3 `TypeToken` 解决泛型问题

```java
// 错误写法：泛型被擦除，无法拿到 List<User> 的类型
// List<User> users = gson.fromJson(json, List.class);  // ❌ 会得到 List<LinkedTreeMap>

// 正确写法：使用 TypeToken
List<User> users = gson.fromJson(json, new TypeToken<List<User>>(){}.getType());
```

> ⚠️ 原理放第二部分，这里记住：**凡是泛型类型（List、Map、自定义泛型类），必须用 `TypeToken` 包装**。

---

### 1.4 常见误区速览（详细分析放后续）

| 误区 | 简要说明 |
|------|---------|
| `null` 字段丢失 | 默认不序列化 `null` 字段，需 `serializeNulls()` |
| 日期格式奇怪 | 默认输出 `"Jun 8, 2021"` 这种格式，需 `setDateFormat()` |
| 循环引用栈溢出 | 对象互相引用会无限递归，需 `@JsonIgnore` 或自定义策略 |
| 接口/抽象类失败 | 反序列化时不知道具体子类型，需要自定义处理 |
| 大整数精度丢失 | 超过 2^53 的 Long 可能变 Double，需 `setLongSerializationPolicy()` |

---

### 1.5 小结

到这里你已经能完成 90% 的日常 JSON 转换需求。接下来进入第二部分，深入 Gson 的核心类和机制，理解它为什么这么设计，以及如何避开那些坑。
