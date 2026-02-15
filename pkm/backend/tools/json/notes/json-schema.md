
# JSON Schema

## Links

* \[1] [https://json-schema.apifox.cn/](https://json-schema.apifox.cn/)
* \[2] [https://json-schema.org/](https://json-schema.org/)
* \[3] API 清单：[https://www.learnjsonschema.com/](https://www.learnjsonschema.com/)

***

## Notes

### Type-specific keywords

> [https://json-schema.org/understanding-json-schema/reference/type](https://json-schema.org/understanding-json-schema/reference/type)

* type：<mark style="color:green;">**string**</mark>、<mark style="color:green;">**number**</mark>、<mark style="color:green;">**integer**</mark>、<mark style="color:green;">**object**</mark>、<mark style="color:green;">**array**</mark>、<mark style="color:green;">**boolean**</mark>、<mark style="color:green;">**null**</mark>
* <mark style="color:orange;">**with type string**</mark>
  * Length：<mark style="color:green;">**minLength**</mark>、<mark style="color:green;">**maxLength**</mark>
  * <mark style="color:green;">**pattern**</mark>(正则表达式)
  * Dates and times
    * <mark style="color:green;">**date-time**</mark>：`2018-11-13T20:20:39+00:00`
    * <mark style="color:green;">**time**</mark>：`20:20:39+00:00`
    * <mark style="color:green;">**date**</mark>：`2018-11-13`
    * <mark style="color:green;">**duration**</mark>：`P3D`（3 天）
  * Hostnames：<mark style="color:green;">**hostname**</mark>、<mark style="color:green;">**idn-hostname**</mark>
  * IP Addresses：<mark style="color:green;">**ipv4**</mark>、<mark style="color:green;">**ipv6**</mark>
  * Resource identifiers：<mark style="color:green;">**uuid**</mark>、<mark style="color:green;">**uri**</mark>、<mark style="color:green;">**uri-reference**</mark>、<mark style="color:green;">**iri**</mark>、<mark style="color:green;">**iri-reference**</mark>
  * URI template：<mark style="color:green;">**uri-template**</mark>
  * JSON Pointer：<mark style="color:green;">**json-pointer**</mark>、<mark style="color:green;">**relative-json-pointer**</mark>
  * Regular Expressions：<mark style="color:green;">**regex**</mark>
* <mark style="color:orange;">**with type number**</mark>
  * multiples：<mark style="color:green;">**multipleOf**</mark>（倍数，可以设置成任何正数）
  * range：<mark style="color:green;">**minimum**</mark>、<mark style="color:green;">**exclusiveMinimum**</mark>、<mark style="color:green;">**exclusiveMinimum**</mark>、<mark style="color:green;">**maximum**</mark>、<mark style="color:green;">**exclusiveMaximum**</mark>
* <mark style="color:orange;">**with type object**</mark>
  * <mark style="color:green;">**properties**</mark>
  * <mark style="color:green;">**patternProperties**</mark>：正则表达式用于 key
  * <mark style="color:green;">**additionalProperties**</mark>：如果为 false，那么不允许有其他的 propertites
  * <mark style="color:green;">**unevaluatedProperties**</mark>：类似于`additionalProperties`，只是它可以识别在子架构中声明的属性。
  * <mark style="color:green;">**required**</mark>：必须包含的properties，是一个array
  * <mark style="color:green;">**propertyNames**</mark>：属性名称。如果您不想强制使用特定的属性，但又想确保这些属性的名称遵循特定的约定，那么这会很有用。
  * 属性的数量：<mark style="color:green;">**minProperties**</mark>、<mark style="color:green;">**maxProperties**</mark>

例如：

```scheme
{
  "type": "object",
  "properties": {
    "number": { "type": "number" },
    "street_name": { "type": "string" },
    "street_type": { "enum": ["Street", "Avenue", "Boulevard"] }
  },
  "patternProperties": {
    "^S_": { "type": "string" }, <- 任何 S_ 开头的key 对应的 value 都必须是 string
  }
  "additionalProperties": false,
  // "additionalProperties": { "type": "string" } <- 这样就可以允许 string 的属性
}
```

* <mark style="color:orange;">**with type array**</mark>
  * <mark style="color:green;">**prefixItems**</mark>：元组验证（一个固定长度的序列，其中每个项目可能具有不同的模式）
  * <mark style="color:green;">**unevaluatedItems**</mark>：数组中添加或禁止额外项时有用和 items 有点像
  * <mark style="color:green;">**items**</mark>：列表验证（一个任意长度的序列，其中每个项目匹配相同的模式）。items用来验证超出`prefixItems`中定义的元素是否有效，如果为 false 则不能包含其他项目
  * <mark style="color:green;">**minItems**</mark>、<mark style="color:green;">**maxItems**</mark>：数组长度
  * <mark style="color:green;">**contains**</mark>：有一个满足就行
  * <mark style="color:green;">**minContains**</mark>、<mark style="color:green;">**maxContains**</mark>：进一步控制 contains 达标的数量
  * <mark style="color:green;">**uniqueItems**</mark>：确保数组中的每个项都是唯一的

```scheme
{
  "type": "array",
  "prefixItems": [
    { "type": "number" },
    { "type": "string" },
    { "enum": ["Street", "Avenue", "Boulevard"] },
    { "enum": ["NW", "NE", "SW", "SE"] }
  ],
  "items": false
}
```

```scheme
{
  "prefixItems": [
    { "type": "string" }, { "type": "number" }
  ],
  "unevaluatedItems": false
}
```

* <mark style="color:orange;">**with type boolean**</mark>（只能是 true 或 false）
* <mark style="color:orange;">**with type null**</mark>（只能是 null，其他的比如 false，0，"" 都不可以）

## Schema Composition <a href="#schema-composition" id="schema-composition"></a>

> [https://json-schema.org/understanding-json-schema/reference/combining#schema-composition](https://json-schema.org/understanding-json-schema/reference/combining#schema-composition)

* `allOf`: (AND) Must be valid against _all_ of the [subschemas](https://json-schema.org/learn/glossary#subschema)
* `anyOf`: (OR) Must be valid against _any_ of the subschemas
* `oneOf`: (XOR) Must be valid against _exactly one_ of the subschemas
* `not`：非

Examples：

需要同时满足

```scheme
{
  "allOf": [
    { "type": "string" },
    { "maxLength": 5 }
  ]
}
```

满足其一就行

```scheme
{
  "anyOf": [
    { "type": "string", "maxLength": 5 },
    { "type": "number", "minimum": 0 }
  ]
}
```

满足一个

```scheme
{
  "oneOf": [
    { "type": "number", "multipleOf": 5 },
    { "type": "number", "multipleOf": 3 }
  ]
}
```

非

```scheme
{ "not": { "type": "string" } }
```

