
# json5 syntax

## Links

* json5 2018标准：[https://spec.json5.org/](https://spec.json5.org/)
* json5 官网：[https://json5.org/](https://json5.org/)
* 中文的简洁易懂的 blog：[https://blog.csdn.net/github\_38727595/article/details/137816175](https://blog.csdn.net/github\_38727595/article/details/137816175)
* 另一个blog：[http://wxnacy.com/2018/02/18/json5/](http://wxnacy.com/2018/02/18/json5/)
* json5 在线解析：[https://www.json.cn/json5/](https://www.json.cn/json5/)

> 个人感觉 Json5 更适合搭配 js 使用，它把 json 改造的更像 js 的对象了。

## comment：注释

{% hint style="info" %}
JSON5**允许**在数据中添加注释。
{% endhint %}

```json5
{
    // 单行注释
    /*
        多行注释
    */
}
```

## whitespace：空白

{% hint style="info" %}
更多的空白

[https://spec.json5.org/#white-space](https://spec.json5.org/#white-space)
{% endhint %}

<table><thead><tr><th width="139">Code Points</th><th width="62" data-type="checkbox">json</th><th width="72" data-type="checkbox">json5</th><th width="464">Description</th></tr></thead><tbody><tr><td>U+0009</td><td>true</td><td>true</td><td>Horizontal tab</td></tr><tr><td>U+000A</td><td>true</td><td>true</td><td>Line feed</td></tr><tr><td>U+000B</td><td>false</td><td>true</td><td>Vertical tab</td></tr><tr><td>U+000C</td><td>false</td><td>true</td><td>Form feed</td></tr><tr><td>U+000D</td><td>true</td><td>true</td><td>Carriage return</td></tr><tr><td>U+0020</td><td>true</td><td>true</td><td>Space</td></tr><tr><td>U+00A0</td><td>false</td><td>true</td><td>Non-breaking space</td></tr><tr><td>U+2028</td><td>false</td><td>true</td><td>Line separator</td></tr><tr><td>U+2029</td><td>false</td><td>true</td><td>Paragraph separator</td></tr><tr><td>U+FEFF</td><td>false</td><td>true</td><td>Byte order mark</td></tr><tr><td>Unicode Zs category</td><td>false</td><td>true</td><td>Any other character in the Space Separator Unicode category</td></tr></tbody></table>

## string：字符串

{% hint style="info" %}
1. 字符串可以用单引号了
2. 字符串可以多行了
{% endhint %}

```json5
{
  // 字符串值允许使用单引号括起来
  singleQuotes: 'I can use "double quotes" here',

  // 字符串值允许包含字符转义序列
  lineBreaks: "Look, Mom!\
  No \n's!",
}
```

## number：数值

{% hint style="info" %}
1. 支持 16 进制，但是 8 进制和 2 进制不行
2. 可以表示无穷和 Nan
{% endhint %}

```json5
{
  keya: 0xFF, // 十六进制数字
  //keyb: 0o377, // 八进制数字
  //keyc: 0b1111, // 二进制数字
  positiveInfinity: Infinity,
  negativeInfinity: -Infinity,
  notANumber: NaN,
}
```

## value：值

{% hint style="danger" %}
1. 可以直接表示日期，不用写成字符串了（**这个应该只能在 js 里边这样写**）
2. 其他的都和 json 一样
{% endhint %}

```json5
{
    birthdate: new Date("1990-01-01"), // 日期对象
}
```

## object：对象

{% hint style="info" %}
1. 尾随逗号
{% endhint %}

```json5
{
    year: 2000,
}
```

## Demo

```json5
{
  // 单行注释:
  // "key1": "str",

  // 多行注释:
  /* "key2": "str",
    "key3": "str" */

  // key 可以不使用引号
  key1: "str",

  // key 允许使用单引号
  key2: "str",

  // 字符串值允许使用单引号括起来
  singleQuotes: 'I can use "double quotes" here',

  // 字符串值允许包含字符转义序列
  lineBreaks: "Look, Mom!\
  No \n's!",

  arr1: [1, 2], // 可以有尾随逗号
  arr2: { a: "str", b: "str" }, // 对象也可以有尾随逗号

  // 数字可以是十六进制，注意是 0xff5643 不是 #ff5643
  hexadecimal: 0xff5643,

  // 数字可以带有 前导小数点 后导小数点：
  leadingDecimalPoint: .35, andTrailing: 35.,

  // 允许正负号
  income: +3000.0, amount: -500.0,

  // 允许使用 NaN 和 Infinity
  positiveInfinity: Infinity,
  negativeInfinity: -Infinity,
  notANumber: NaN,

  // Unicode 字符可以在标识符中使用
  π: 3.141592653589793,
  "ლ(ಠ益ಠლ)": "为什么我们不能成为朋友？",

  // 键名允许重复，后面的会覆盖前面的
  重复键: "第一个值",
  重复键: "第二个值", // 这将覆盖第一个值
}
```
