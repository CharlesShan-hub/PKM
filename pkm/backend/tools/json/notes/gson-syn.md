
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

