# Gson

* Gson Github：https://github.com/google/gson
* 王二博客：https://javabetter.cn/gongju/gson.html
* 第一部分：[gson-intro](gson-intro.md)

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

---

下边是ai的
非常好，这个结构很清晰！我帮你细化一下三个部分的内容规划：

---

## 第一部分：快速上手（使用角度）
> 目标：让读者 5 分钟能用起来，跑通基本流程

- 引入依赖（Maven / Gradle）
- 最简示例：对象 → JSON → 对象
- 常见场景速览：
  - List / Map 转换
  - 复杂嵌套对象的序列化/反序列化
  - `TypeToken` 解决泛型问题（此处只提用法，原理放第二部分）
- 常见误区速览（只点名，详细分析放第二/三部分）

---

## 第二部分：深度源码与核心类（语法 + 坑）
> 目标：理解 Gson 内部机制，掌握容易踩坑的点

- `Gson` 类：核心 API 原理（`toJson` / `fromJson` 的内部流程）
- `GsonBuilder`：配置项逐一深入
  - `serializeNulls()` / `excludeFieldsWithoutExposeAnnotation()`
  - `setLongSerializationPolicy()`（长整型精度问题，必坑）
  - `setFieldNamingPolicy()` / `setFieldNamingStrategy()`
- 注解体系：
  - `@SerializedName`、`@Expose`、`@Since`、`@Until`（版本控制）
- `TypeToken` 原理：泛型擦除 + `Type` 接口体系（`ParameterizedType` 等）
- 序列化/反序列化内部流程：
  - 反射 + `FieldAttributes`
  - 类型适配器查找机制（`TypeAdapterFactory` 注册表）
- 常见坑：
  - `null` 丢失字段
  - 默认日期格式奇怪
  - 循环引用无限递归
  - 接口/抽象类无法确定子类型
  - 大整数精度丢失（`Long` 变 `Double`？）
  - 不可变类 / 无默认构造器的类

---

## 第三部分：高级场景与二次开发
> 目标：解决真实项目中 Gson 不够用的场景

- 自定义 `TypeAdapter` / `JsonSerializer` / `JsonDeserializer`
  - 什么时候用哪个？
  - 注册方式：`@JsonAdapter` + `registerTypeAdapter()`
- 自定义 `TypeAdapterFactory`：拦截指定类型
- `JsonReader` / `JsonWriter` 流式解析：超大 JSON 内存优化
- 与框架集成：
  - Spring Boot 中替换默认 Jackson 为 Gson
  - Retrofit 中 GsonConverter
- 性能对比与优化：
  - Gson vs Jackson vs Fastjson（各自适用场景）
  - 反射缓存、`setReflectiveAccess()` 等
- 实战场景设计：
  - 处理低版本兼容（`@Since` / `@Until` + `setVersion()`）
  - 字段别名处理（前后端命名不一致）
  - 日志脱敏 / 字段过滤

---

## 建议的笔记目录树

```
Gson 学习笔记/
├── 01-快速上手.md          # 第一部分
├── 02-核心机制与坑.md      # 第二部分
└── 03-高级场景与实践.md    # 第三部分
```

---

这样三个部分从"会用 → 懂原理 → 能扩展"层层递进，覆盖了学习 Gson 的全部关键维度。你觉得这个划分如何？需要我帮你开始写第一部分的具体内容吗？