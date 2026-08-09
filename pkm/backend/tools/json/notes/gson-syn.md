# Part 2：源码级理解（从外到内）

> 目标：不追求逐行读懂源码，而是带着问题看 —— **这个类解决了什么问题？设计决策是什么？边界情况怎么处理？**

## 核心类清单（按阅读顺序）

| 类                              | 重点关注                            |
| ------------------------------ | ------------------------------- |
| `Gson`                         | `toJson()` / `fromJson()` 的入口流程 |
| `GsonBuilder`                  | 各种配置如何影响内部组件                    |
| `TypeAdapter`                  | 序列化/反序列化的核心接口                   |
| `ReflectiveTypeAdapterFactory` | 反射怎么读写字段（**核心！**）               |
| `TypeToken`                    | 泛型捕获的原理                         |
| `JsonReader` / `JsonWriter`    | 流式解析的实现                         |
## `Gson`

### 准备

还是这个动物的案例，继续序列化和反序列化：

```java
package top.charles;  
  
import lombok.AllArgsConstructor;  
import lombok.NoArgsConstructor;  
import lombok.ToString;  

@AllArgsConstructor  
@NoArgsConstructor // 必须有默认构造器（无参构造）  
@ToString  
public class Animal {  
    private String name;  
    private int birthYear;  
}
```

### 序列化

#### 第一步：`Gson.java`的工作

```java
Animal a1 = new Animal("Tom", 1938);  
String json = gson.toJson(a1);
```

```java
// Gosn.java
public String toJson(Object src) {  
  if (src == null) {  
    return toJson(JsonNull.INSTANCE);    // <-
  }  return toJson(src, src.getClass()); // <-
}
```

如果对象真的是空，会输出`"null"`

```java
@Test  
public void testNullObject(){  
    Animal a1 = null;  
    String json1 = gson.toJson(a1);  
    // togo: return toJson(JsonNull.INSTANCE);
    System.out.println(json1); // null  
    System.out.println(json1.equals("null")); // true  
    System.out.println(json1.length()); // 4  
}
```

如果对象不是空则会默认先找到运行时类型，然后再传入一个`StringWriter`：

```java
// Gosn.java
// return toJson(src, src.getClass());
public String toJson(Object src, Type typeOfSrc) {  
  StringWriter writer = new StringWriter();  
  toJson(src, typeOfSrc, writer);  // <-
  return writer.toString();  
}
```

`StringWriter` 是 Java 标准库里的一个**字符输出流**，比直接用 `String` 拼接高效（避免了大量不可变字符串的创建）。

```java
// Gosn.java
// toJson(src, typeOfSrc, writer);
public void toJson(Object src, Type typeOfSrc, Appendable writer) throws JsonIOException {  
  try {  
    JsonWriter jsonWriter = newJsonWriter(Streams.writerForAppendable(writer));  
    toJson(src, typeOfSrc, jsonWriter);  // <-
  } catch (IOException e) {  
    throw new JsonIOException(e);  
  }  
}
```

`JsonWriter` 是 Gson 自己的流式写入器
1. **`Appendable` 是宽泛的接口** —— 不止 `StringWriter`，`StringBuilder`、`Writer` 等都实现了它。Gson 对外暴露的是 `Appendable`，调用方可以传任何实现。
2. **但 Gson 内部需要的是 `JsonWriter`** —— 它提供了 `name()`、`value()`、`beginObject()` 等 JSON 语法方法。

```java
// Gosn.java
// toJson(src, typeOfSrc, jsonWriter);
public void toJson(JsonElement jsonElement, JsonWriter writer) throws JsonIOException {  
  boolean oldLenient = writer.isLenient();  
  writer.setLenient(true);  
  boolean oldHtmlSafe = writer.isHtmlSafe();  
  writer.setHtmlSafe(htmlSafe);  
  boolean oldSerializeNulls = writer.getSerializeNulls();  
  writer.setSerializeNulls(serializeNulls);  
  try {
    Streams.write(jsonElement, writer);  // <-
  } catch (IOException e) {  
    throw new JsonIOException(e);  
  } catch (AssertionError e) {  
    throw new AssertionError("AssertionError (GSON " + GsonBuildConfig.VERSION + "): " + e.getMessage(), e);  
  } finally {  
    writer.setLenient(oldLenient);  
    writer.setHtmlSafe(oldHtmlSafe);  
    writer.setSerializeNulls(oldSerializeNulls);  
  }  
}
```

1. **保存旧状态**（`oldLenient`、`oldHtmlSafe`、`oldSerializeNulls`）
2. **临时覆盖成 Gson 实例自己的配置**（`lenient`、`htmlSafe`、`serializeNulls`）
3. **真正干活**（`Streams.write`）
4. **finally 恢复旧状态** —— 不管成功还是失败，都不污染外部的 `JsonWriter`

```java
// Streams.java
//Streams.write(jsonElement, writer);
public static void write(JsonElement element, JsonWriter writer) throws IOException {  
  TypeAdapters.JSON_ELEMENT.write(writer, element);  
}
```

#### 第二步：`Stream.java`的工作



---

1. **`Gson` + `GsonBuilder`**：先看入口，理解 Gson 实例里装了什么
    
2. **`TypeAdapter` + `TypeAdapterFactory`**：核心机制，理解了这两个，Gson 的 80% 就懂了
    
3. **`JsonReader` + `JsonWriter`**：底层 IO，看 Gson 如何流式处理 JSON
    
4. **`ReflectiveTypeAdapterFactory`**：Gson 最“魔法”的部分，反射 + 缓存
    
5. **`TypeToken`**：理解 Gson 如何处理泛型
    
6. **`Excluder` + `FieldNamingStrategy`**：配置相关的细节
    
7. **`JsonSerializer` / `JsonDeserializer`**：了解历史遗留接口，便于维护旧代码

---

## 二、源码阅读策略：跟踪一个案例

**不要从头读到尾**，用"跟踪一个案例"的方式：

1. 写一个最简单的对象（如 `User`）
2. 在 `gson.toJson()` 入口打断点
3. 一步步跟进去，看它：
   - 怎么获取 `TypeAdapter`
   - 怎么拿到字段列表
   - 怎么处理每个字段（`@SerializedName`、`transient`、`@Expose`）
4. 记录每一步的**关键类名和方法名**

> 一次跟踪 30-60 分钟，比读三天文档都有用。

---

## 三、笔记形式：源码路径 + 核心逻辑

```markdown
## 场景：Xxx

> 背景：xxx

💡 源码位置：`Gson.toJson()` → `getAdapter()` → `ReflectiveTypeAdapterFactory.create()`

核心逻辑：
1. xxx
2. xxx
3. xxx

关键代码片段（截取核心几行，不要大段贴）：
```

> 以后忘了细节，看一眼源码路径就能快速定位，不用重新搜索。

---

## 四、笔记结构（从外到内）

1. **入口篇**：`Gson.toJson()` / `fromJson()` —— 整体流程骨架
2. **适配器篇**：`TypeAdapter` 体系 —— 为什么要有适配器？怎么获取？
3. **反射篇**：`ReflectiveTypeAdapterFactory` —— 怎么读写字段（核心）
4. **类型篇**：`TypeToken` —— 泛型捕获原理（相对独立，可单独一章）
5. **流式篇**：`JsonReader` / `JsonWriter` —— 怎么解析/生成 JSON

每个篇章目标：**能用自己的话讲清楚这个模块的职责和核心逻辑**。

---

## 五、费曼检验标准

学完一个模块，问自己：

> "如果现在有人问我 Gson 怎么把 JSON 变成 Java 对象的，我能用 3 句话讲清楚吗？"

**3 句版本参考**：

1. Gson 通过 `TypeToken` 获取目标类型的完整信息（包括泛型）
2. 根据类型查找或创建对应的 `TypeAdapter`（反射适配器是兜底方案）
3. `TypeAdapter` 用 `JsonReader` 逐个读取 JSON 令牌，用反射填充 Java 对象字段

---

## 六、Part 1 的亮点，Part 2 继续保持

- ✅ 每个场景都有"为什么需要"的背景
- ✅ 每个用法标注"本质"
- ✅ 有"错误示例"和"为什么错"
- ✅ 最后总结，提炼设计哲学



















## Part 2：深度源码与核心类（语法 + 坑）

> 目标：理解 Gson 内部机制，掌握容易踩坑的点。

---

### 2.1 `Gson` 类：核心 API 原理

```java
Gson gson = new Gson();
```

- `Gson` 是线程安全的，可以全局复用（不要每次 new）
- 内部维护了一个 **TypeAdapterFactory 注册表**，用于查找类型的适配器
- `toJson()` 内部流程：
  1. 根据对象类型查找对应的 `TypeAdapter`
  2. 调用 `adapter.write(jsonWriter, obj)` 写出 JSON
- `fromJson()` 内部流程：
  1. 根据目标类型查找对应的 `TypeAdapter`
  2. 调用 `adapter.read(jsonReader)` 读取 JSON

```java
// 源码简化示意
public String toJson(Object src) {
    TypeAdapter<Object> adapter = (TypeAdapter<Object>) getAdapter(src.getClass());
    // ...
}
```

---

### 2.2 `GsonBuilder`：配置项逐一深入

```java
Gson gson = new GsonBuilder()
    .serializeNulls()                    // 序列化 null 字段
    .setPrettyPrinting()                 // 格式化输出
    .setDateFormat("yyyy-MM-dd")         // 自定义日期格式
    .setFieldNamingPolicy(FieldNamingPolicy.LOWER_CASE_WITH_UNDERSCORES)  // 字段命名策略
    .excludeFieldsWithoutExposeAnnotation()  // 只序列化 @Expose 注解的字段
    .setVersion(1.0)                     // 版本控制（与 @Since/@Until 配合）
    .setLongSerializationPolicy(LongSerializationPolicy.STRING)  // Long 转 String
    .disableInnerClassSerialization()    // 禁止序列化内部类
    .disableHtmlEscaping()               // 禁止 HTML 转义（默认会把 `<` 转成 `\u003c`）
    .create();
```

#### 常见配置详解

| 配置 | 作用 | 典型坑 |
|------|------|--------|
| `serializeNulls()` | 默认不输出 null 字段，开启后输出 `"field":null` | 默认行为容易导致字段丢失 |
| `setDateFormat()` | 默认日期格式是 `"Jun 8, 2021 10:00:00 AM"`，不符合大多数业务需求 | 不设置的话前后端解析会失败 |
| `setLongSerializationPolicy(STRING)` | 防止 JS 解析大整数丢失精度（超过 2^53） | 不设置时 Long 会转成 Double 或丢失精度 |
| `disableHtmlEscaping()` | 默认会把 `<`、`>`、`&` 转成 Unicode 转义 | 不关闭的话，HTML 标签会被转义成 `\u003c` |
| `excludeFieldsWithoutExposeAnnotation()` | 配合 `@Expose` 控制字段白名单 | 开了之后没有 `@Expose` 的字段全部丢失 |
| `setVersion()` | 配合 `@Since` / `@Until` 做版本兼容 | 不设置版本时 `@Since`/`@Until` 无效 |

---

### 2.3 注解体系

| 注解 | 作用 | 示例 |
|------|------|------|
| `@SerializedName` | 指定 JSON 字段名（应对命名不一致、字段重名） | `@SerializedName("user_name") private String userName;` |
| `@Expose` | 配合 `serializeNulls()` 或 `excludeFieldsWithoutExposeAnnotation()` 控制序列化范围 | `@Expose(serialize = false, deserialize = false)` |
| `@Since` / `@Until` | 版本控制，结合 `setVersion()` 使用 | `@Since(1.0)` 表示版本 >= 1.0 才生效 |
| `@JsonAdapter` | 指定自定义类型适配器（Part 3 详述） | `@JsonAdapter(UserAdapter.class)` |

#### `@SerializedName` 高级用法：字段重名（多备选名）

```java
public class User {
    @SerializedName(value = "name", alternate = {"userName", "username"})
    private String name;
}
// 反序列化时，JSON 中 "name"、"userName"、"username" 都能映射到 name
// 但序列化时只会输出 "name"
```

---

### 2.4 `TypeToken` 原理：泛型擦除 + Type 体系

#### 为什么需要 TypeToken？

```java
// ❌ 泛型被擦除，运行时不知道 List<User> 的泛型参数
Type type = List.class;  // 只知道是 List，不知道元素是 User

// ✅ TypeToken 通过匿名内部类捕获泛型参数
Type type = new TypeToken<List<User>>(){}.getType();
```

#### 背后的 Type 体系

| 接口/类 | 作用 |
|---------|------|
| `Type` | 所有类型的父接口（`Class`、`ParameterizedType` 等都实现它） |
| `Class<?>` | 具体类类型，如 `User.class` |
| `ParameterizedType` | 参数化类型，如 `List<User>`，能拿到原始类型 + 泛型参数 |
| `GenericArrayType` | 泛型数组，如 `T[]` |
| `WildcardType` | 通配符类型，如 `? extends Number` |

```java
// TypeToken 的核心是内部的匿名类
new TypeToken<List<User>>(){}.getType();
// 通过 getGenericSuperclass() 拿到 TypeToken<T> 的泛型参数
```

---

### 2.5 序列化/反序列化内部流程

#### 反射 + `FieldAttributes`

```java
// 默认的 ReflectiveTypeAdapterFactory 会：
// 1. 遍历类的所有字段（包括父类）
// 2. 通过反射读取/写入字段值（不调用 getter/setter）
```

#### 类型适配器查找机制

```
Gson 内部有一个 TypeAdapterFactory 链：

1. 用户通过 registerTypeAdapter() 注册的 → 优先匹配
2. 注解 @JsonAdapter 指定的 → 其次
3. 内置的基础类型（String、int、boolean 等）→ 再次
4. 集合/Map 类型 → 再次
5. 最后才是反射默认适配器
```

---

### 2.6 常见坑（重点）

#### 坑 1：`null` 字段丢失

```java
User user = new User();
user.setName(null);
user.setAge(25);

gson.toJson(user);  // {"age":25}  name 字段直接消失了！
// 解决：gson = new GsonBuilder().serializeNulls().create();
```

#### 坑 2：默认日期格式奇怪

```java
Date date = new Date();
gson.toJson(date);  // "Jun 8, 2021 10:00:00 AM"  ← 美国人格式
// 解决：new GsonBuilder().setDateFormat("yyyy-MM-dd HH:mm:ss").create();
```

#### 坑 3：循环引用无限递归 → 栈溢出

```java
public class User {
    private String name;
    private User friend;  // 互相引用
}
// user.friend = user;  直接死循环！
// 解决：@JsonIgnore 或自定义序列化策略
```

#### 坑 4：接口/抽象类无法确定子类型

```java
public interface Animal { }
public class Dog implements Animal { }

// gson.fromJson(json, Animal.class);
// 报错：Cannot construct instance of Animal (no default constructor)
// 解决：自定义 JsonDeserializer 或使用 @JsonAdapter
```

#### 坑 5：大整数精度丢失

```java
Long bigNum = 1234567890123456789L;
gson.toJson(bigNum);  // 1234567890123456789  ← JSON 里没问题

// 但 JS 解析时会丢失精度（JS 最大安全整数 2^53 - 1）
// 解决：new GsonBuilder().setLongSerializationPolicy(LongSerializationPolicy.STRING).create();
// 输出： "1234567890123456789"
```

#### 坑 6：无默认构造器的类无法反序列化

```java
public class User {
    private String name;
    public User(String name) { this.name = name; }  // 没有无参构造！
}
// gson.fromJson(json, User.class);  // 报错
// 解决：使用 Unsafe 绕过构造器（Gson 默认会尝试），但不可靠
// 更推荐：自定义 InstanceCreator 或 JsonDeserializer
```

#### 坑 7：内部类序列化问题

```java
public class Outer {
    private String name;
    public class Inner {   // 非 static 内部类
        private String value;
    }
}
// 序列化内部类时，会带上隐式的外部类引用 outer
// 解决：new GsonBuilder().disableInnerClassSerialization().create();
// 或者把内部类改成 static
```

---

### 2.7 小结

掌握这些核心机制和坑点，你就能在项目里放心使用 Gson 了。接下来进入第三部分，看看如何通过自定义 `TypeAdapter` / `JsonDeserializer` 解决更复杂的场景。

