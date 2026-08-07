# Gson

* 简介：Google 出品，API 简洁，支持对象与 JSON 的直接转换。
    - Gson Github：https://github.com/google/gson
    - 王二博客：https://javabetter.cn/gongju/gson.html
* [第一部分：Gson常见使用场景](gson-intro.md)：Gson 忠实还原 JSON，把 Java 与 JSON 的鸿沟暴露给你，提供 `GsonBuilder`（全局）和注解（局部）两把手术刀，但填坑还得靠你自己。
    - Gson 忠实还原 JSON，把 Java 与 JSON 的鸿沟暴露给你，提供 `GsonBuilder`（全局）和注解（局部）两把手术刀，但填坑还得靠你自己。
    - **对象转换**：`toJson` / `fromJson` 基本用法，必须有默认构造器
    - **美观输出**：`setPrettyPrinting()` 只影响序列化
    - **集合与列表**：List / Map 必须用 `TypeToken` 解决泛型擦除
    - **null 字段**：默认不输出 null，`serializeNulls()` 可开启
    - **日期格式**：`setDateFormat("yyyy-MM-dd HH:mm:ss")` 自定义格式
    - **字段重命名**：`@SerializedName` 指定 JSON 字段名，`alternate` 支持反序列化别名
    - **字段过滤**：`transient` 完全不序列化；`@Expose` 精准控制双向
    - **循环引用**：Gson 不自动处理，需要开发者主动切断引用链
    - **大整数精度**：默认转 double 会丢精度，需自定义 TypeAdapter
* [第二部分：Gson API解析](gson-syn.md)




---

## 第一部分：快速上手（使用角度）

[gson-intro](gson-intro.md)
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