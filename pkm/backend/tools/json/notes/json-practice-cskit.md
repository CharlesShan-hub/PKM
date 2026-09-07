# JSON 实战：从 YshJson 到自研框架 cskit

> 对应 [README 学习计划](../README.md) 第一阶段 + 第四阶段的**超越版**：
> 不只是"读懂 YshJson"，而是基于对它的理解，**造出了自己的 JSON 框架**。

## 🎯 一句话总结

用「用 → 看 → 懂 → 复现 → 超越」的学习法，把公司工具类 `YshJson` 吃透，
然后设计并实现了个人框架 **cskit**（https://github.com/CharlesShan-hub/cskit）：
统一门面 + 可插拔适配器（Gson / Fastjson2 / Jackson），支持自定义适配器扩展。

---

## 一、读源码：YshJson 的精髓（264 行）

公司内部包 `ysh-java-kit` 里的 `com.ysh.common.json.YshJson`，基于 Gson 的薄封装：

| 设计点 | 说明 |
|---|---|
| `DEFAULT_GSON` 静态缓存 | Gson 线程安全、构建成本高 → 默认路径复用单例 |
| `GsonInitOperation` 函数式接口 | 需要定制时传 lambda 配 GsonBuilder，默认快、定制灵活 |
| 非泛型/可泛型双轨重载 | 泛型擦除 → List/Map 必须用 `TypeToken` |
| `TypeToken.getParameterized` | 内部动态拼泛型，免匿名内部类 |

**本质**：把"创建 Gson"收编成默认单例 + 静态便捷方法。少 new 是表象，**统一入口 + 线程安全复用**是本质。

### 源码里暴露的坑（Javadoc 明示）

1. 默认 Gson 日期格式是美式 `"Mar 10, 2024"`，没配 `setDateFormat`
2. `fromJsonStringToMap` 值全是 Object：数值→Double、嵌套→LinkedTreeMap
3. **大整数精度**：`Map<String,Object>` 反序列化 long 会变 Double 丢精度（如雪花 ID！）
4. 定制路径每次 `new GsonBuilder().create()`，不缓存 → 高频调用性能坑

---

## 二、复现 + 超越：自研框架 cskit

### 架构：接口 + 注册表（对标 JDBC / slf4j）

```
业务代码 → JsonAdapter 接口（唯一依赖）
              ↓
  JsonAdapterRegistry 单例注册表（开放扩展）
   ├── gson / fastjson / jackson（官方适配器）
   └── company / 任何自研库（用户实现接口 + 注册一行即用）
```

### 关键设计决策

| 决策 | 理由 |
|---|---|
| `JsonAdapter` 接口 5 方法 | toJson / fromJson / fromJson(Type) / fromJsonList / fromJsonMap |
| 注册表用**单例** | 注册中心全局唯一，避免多处 new 各注册各的 |
| 注册表用 `ConcurrentHashMap` | 全局共享必须线程安全（16 线程并发测试验证） |
| `json-core` 零第三方依赖 | 依赖隔离：用谁引谁的适配器模块 |
| 模块拆分（core/gson/fastjson/jackson） | 解决"只想用 gson 却要装全部"的问题 |
| `@JsonField` 统一注解 | value/name 重命名 + serialize/deserialize 开关，各适配器翻译 |

### 各适配器的注解翻译层（扩展点不同）

- **Gson**：手写 `TypeAdapterFactory`（Gson 没有注解内省扩展）
- **Jackson**：原生 `AnnotationIntrospector`（优雅得多！）
- **Fastjson2**：未接注解层（README 标注为扩展点）

### 性能实测（1000 条记录，预热 2000 + 测量 20000，JDK 21）

| 实现 | 序列化 | 反序列化 |
|---|---|---|
| Gson | ~288 μs | ~106 μs |
| Fastjson2 | **~21 μs** 🏆 | **~28 μs** 🏆 |
| Jackson | ~50 μs | ~99 μs |

正确性：三库 1000 条往返全部无丢失，业务代码完全一致。

---

## 三、实战踩坑记录（最值钱的资产）

1. **fastjson 1.x 在 JDK 21 直接废** → 序列化输出 `{}` → 换 fastjson2（官方接班人）
2. **不同库对实体类要求不同**：Gson 反射读字段、fastjson2 要 getter/setter → 适配器抹平差异
3. **循环依赖**：gson 测试依赖 jackson 做评测、jackson 又依赖 gson 对比 → Maven cycle
   → 正确解法：评测套件放"能看见所有适配器"的模块（json-jackson）
4. **IDEA 对 `file://${basedir}/repo` 本地仓库支持差**：公司私有 jar 模块在 IDEA 里标红，命令行正常
5. **Maven 镜像配置只能放 settings.xml**：写在 pom.xml 是非法标签，会导致解析失败

---

## 四、学习法沉淀：用 → 看 → 懂 → 复现 → 超越

```
用    先跑起来，知道 API 怎么用（写了 YshJsonDemoTest 验证各种坑）
看    读源码，理解设计意图（静态单例、双轨重载、TypeToken）
懂    追问"为什么这么设计"（线程安全？泛型擦除？性能？）
复现  自己实现一遍核心逻辑（命名注册表 HashMap 缓存）
超越  设计出更好的方案（适配器模式 + 模块化 + 单例注册中心）
```

**关键心态**：每次用别人的库，都问一句"如果我来设计，我会怎么做"。
今天问出"为什么不用 HashMap 缓存定制"的那一刻，就是超越的开始。

---

## 五、进阶特性（后续追加）

1. **三库注解翻译层全部完成**：
   - Gson → `JsonFieldAdapterFactory`（TypeAdapterFactory）
   - Jackson → `JsonFieldAnnotationIntrospector`（AnnotationIntrospector）
   - Fastjson → `JsonFieldFastJsonCodec`（JSONObject 中转 + 数字类型适配 BigDecimal 坑）
   - 实测：同一套 `@JsonField`，三库行为完全一致 ✅

2. **使用模式三态**（对齐并超越 YshJson）：
   - 长期复用：`register` + `get`
   - 一次性：`useOnce`（取出即删）/ `use`（作用域封闭）
   - 即用即弃：`JsonKit` 静态入口（直接传适配器 / Supplier 工厂）

3. **JsonKit 统一方法名 + 四种重载**（一个名字，四种用法，避免命名爆炸）：
   ```java
   JsonKit.toJson(obj)                                       // ① 默认适配器
   JsonKit.toJson("gson", obj)                               // ② 模板名（注册表）
   JsonKit.toJson(new GsonJsonAdapter(), obj)                // ③ 实例（一次性）
   JsonKit.toJson(() -> new GsonJsonAdapter(b -> ...), obj)  // ④ 工厂（一次性+定制）
   ```
   - `configureDefault()` 可切换默认适配器（超越 YshJson 固定 DEFAULT_GSON）
   - fromJson 同样四种重载，完全对称

4. **工程化打磨**：
   - `GsonJsonAdapter` 支持定制构造（Consumer&lt;GsonBuilder&gt;）
   - 共享测试实体模块 `json-testkit`（Animal/Employee/Tourist，DRY）
   - 测试 100% 吃自己的狗粮（移除手搓 GsonRegistry）
   - 跨库对比测试统一收拢 json-jackson 模块（打破循环依赖）

## 六、我的设计哲学（提炼）

> **底层交给最专业的人，上层我只做一件事——让使用变得简单。**

| 理念 | 落地 |
|---|---|
| 代码简洁 | 重载代替命名（一个 toJson 四种用法）、共享实体 DRY、一套注解三库通用 |
| 内存安全且轻量 | ConcurrentHashMap 线程安全、json-core 零第三方依赖、依赖隔离按需引入 |
| 不重复造轮子，在上层封装 | 适配器模式 + 门面模式（对标 JDBC / slf4j），底层用最强库、上层统一入口 |

## 七、下一步 TODO

- [x] cskit 接入 GitHub Actions CI（push 自动 mvn test）
- [x] fastjson 适配器补 `@JsonField` 注解翻译层
- [ ] 增加 yaml / xml 子框架
- [ ] cskit 发布到 Maven Central
- [ ] 项目代码实战：把 cskit 用到真实项目里验证

## 参考

- [cskit 仓库](https://github.com/CharlesShan-hub/cskit)
- [Gson 入门笔记](gson-intro.md)（查尔斯动物园系列）
