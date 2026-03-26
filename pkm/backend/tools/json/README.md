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
