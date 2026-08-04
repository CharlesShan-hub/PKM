@ -1,33 +0,0 @@
# JSON

---
## JSON and variations

* Humanized
	* [json](notes/json.md)：最原始的 json，用于替代 XML
	* [jsonl](notes/jsonl.md)：一行一个 json，提高读写性能
	* [json5](notes/json5.md)：扩展了 json 的数据
	* [jsonc](notes/jsonc.md)：是 json5 的子集
	* [hjson](notes/hjson.md)：扩展了 json 的数据，加入了人性化 “human” 的优化
* Application
	* [geojson](notes/geojson.md)：json 用于地理
	* [topojson](notes/topojson.md)：GeoJSON 的扩展
	* [在线转换GeoJSON和TopoJSON](http://mapshaper.org)：mapshaper.org
* Binary
	* [bson](notes/bson.md)：mongodb 推出二进制 JSON，支持更多类型
	* [smile](notes/smile.md)：1:1 对应 json 的二进制版本（复杂的规则）
	* [cbor](notes/cbor.md)：1:1 对应 json 的二进制版本（类似报文段）
	* [ubjson](notes/ubjson.md)：1:1 对应 json 的二进制版本（类型+长度+内容）
* JSON 的二进制版本总结
	* [Comparison of data-serialization formats](https://en.wikipedia.org/wiki/Comparison\_of\_data-serialization\_formats)
	* [A Survey of JSON-compatible Binary Serialization Specifications](https://arxiv.org/abs/2201.02089)
	* [A Benchmark of JSON-compatible Binary Serialization Specifications](https://arxiv.org/abs/2201.03051)
* JSON解析
	* Python：[json](../../../ai/python/library/json.md)
	* JS：[json-js](notes/json-js.md)
	* Java：[json-java](notes/json-java.md)

---
## Schema

* [[notes/json-schema|json-schema]]


---
# JSON 处理库学习计划

## 学习目标
掌握 Java 生态中三个主流 JSON 处理库（Gson、Jackson、Fastjson）的核心 API 和使用场景，能够在日常开发中根据需求选择合适的工具。

**预计总耗时**：1 周（每天 1-2 小时）

---

## 📅 学习路线

### 第一阶段：Gson（Google 官方库）
**时间**：Day 1-2  
**重点**：掌握基础序列化/反序列化，理解泛型擦除问题

- [ ] 了解 Gson 的 Maven 依赖和基本用法
- [ ] 掌握 `toJson()` / `fromJson()` 基础方法
- [ ] 理解 `TypeToken` 的作用（解决 List/Map 泛型问题）
- [ ] 学会使用 `@SerializedName` 处理字段名映射
- [ ] 了解 `GsonBuilder` 配置（日期格式、null 处理）
- [ ] 阅读公司项目中的 `YshJson` 工具类源码

---

### 第二阶段：Jackson（Spring Boot 默认）
**时间**：Day 3-4  
**重点**：掌握 ObjectMapper 核心 API，理解注解和树模型

- [ ] 了解 Jackson 的三个核心包（databind、core、annotations）
- [ ] 掌握 `ObjectMapper` 的 `writeValueAsString()` / `readValue()`
- [ ] 学习常用注解：`@JsonProperty`、`@JsonIgnore`、`@JsonFormat`
- [ ] 理解 `JsonNode` 树模型（动态解析 JSON 结构）
- [ ] 掌握配置项：日期格式化、驼峰/下划线转换、忽略未知字段
- [ ] 了解 Jackson 在 Spring Boot 中的自动配置

---

### 第三阶段：Fastjson（Alibaba 高性能够）
**时间**：Day 5  
**重点**：了解 API 差异和应用场景

- [ ] 掌握 `JSON.toJSONString()` / `JSON.parseObject()`
- [ ] 理解 `TypeReference` 处理泛型（对比 Gson 的 TypeToken）
- [ ] 了解 Fastjson 的性能优势和已知安全风险
- [ ] 对比三个库的 API 设计差异

---

### 第四阶段：综合实战
**时间**：Day 6-7  
**重点**：在真实项目中应用和对比

- [ ] 用 Gson 重写 `YshJson` 工具类的核心方法
- [ ] 在 `jcms-app` 中配置 Jackson 作为 Spring Boot 默认序列化器
- [ ] 对比三个库处理复杂嵌套对象时的代码量差异
- [ ] 整理一份个人速查表（常用 API 对照）

---

## 📚 学习资源

| 库 | 官方文档 | 推荐教程 |
|-----|---------|---------|
| Gson | https://github.com/google/gson | B站/YouTube 搜索 "Gson 教程" |
| Jackson | https://github.com/FasterXML/jackson | Baeldung 的 Jackson 系列 |
| Fastjson | https://github.com/alibaba/fastjson | 官方 Wiki（注意版本） |

---

## ✅ 验收标准

完成以下任务即视为学习达标：

- [ ] 能用 Gson 序列化/反序列化带泛型的 List/Map
- [ ] 能用 Jackson 处理下划线命名的 JSON 字段
- [ ] 能用 Fastjson 解析嵌套 JSON 对象
- [ ] 能在 `jcms-core` 中熟练使用至少一种 JSON 库处理日志

---

## 💡 建议

1. **以用带学**：直接在你的 `jcms` 项目中边写边学，比纯看文档高效 3 倍
2. **对比记忆**：把三个库的同类 API 写在 Excel 里，横向对比差异
3. **不必面面俱到**：掌握 80% 的高频用法即可，剩下的用到再查