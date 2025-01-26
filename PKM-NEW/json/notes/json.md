
# JSON

## Links

* wiki：[https://en.wikipedia.org/wiki/JSON](https://en.wikipedia.org/wiki/JSON)
* 工具箱：[https://www.json.cn/](https://www.json.cn/)
* json语法介绍与每个语言调用 json 的工具链接：[https://www.json.org/json-en.html](https://www.json.org/json-en.html)

## Standards

[ECMA](https://en.wikipedia.org/wiki/Ecma\_International)和[ISO](https://en.wikipedia.org/wiki/International\_Organization\_for\_Standardization)/[IEC](https://en.wikipedia.org/wiki/International\_Electrotechnical\_Commission)标准只描述了允许的语法，而RFC涵盖了一些安全和互操作性考虑。

* ECMA标准：[https://ecma-international.org/publications-and-standards/standards/ecma-404/](https://ecma-international.org/publications-and-standards/standards/ecma-404/)
* ECMA标准翻译：[https://blog.csdn.net/qq\_41554403/article/details/125481411](https://blog.csdn.net/qq\_41554403/article/details/125481411)
* RFC标准：[https://datatracker.ietf.org/doc/html/rfc8259](https://datatracker.ietf.org/doc/html/rfc8259)
* RFC标准翻译：[https://rfc2cn.com/rfc8259.html](https://rfc2cn.com/rfc8259.html)

## comment：注释

{% hint style="info" %}
json 不允许注释，单行多行都不行！
{% endhint %}

## whitespace：空白

{% hint style="info" %}
空格，空行，换行符，制表符都被解释成空白。
{% endhint %}

<figure><img src="../../.gitbook/assets/image (18).png" alt="" width="563"><figcaption></figcaption></figure>

## string：字符串

{% hint style="info" %}
字符串是零个或多个Unicode字符的序列。字符串必须用双引号，不能用单引号。
{% endhint %}

```json
{"a": 123} 正确
{"message": "\u4f60\u597d"} 正确
{'a': 123} 错误，不能用单引号
```

<figure><img src="../../.gitbook/assets/image (16).png" alt="" width="563"><figcaption></figcaption></figure>

## number：数值

{% hint style="info" %}
浮点数采用 IEEE754 标准。另外 JSON 标准本身不直接支持十六进制、八进制和二进制的字面量表示，实在想用，可以用字符串模拟。
{% endhint %}

```json
{
    "integer": 42,
    "negative_integer": -1234567890,
    "float": 3.14159,
    "negative_float": -2.71828,
    "scientific_notation": 5e+22, // 相当于 50000000000000000000000
    "negative_scientific_notation": -1.234e-10 // 相当于 -0.0000000001234
    "hexadecimal": "0x1A", // 十六进制
    "octal": "0o12",      // 八进制
    "binary": "0b101"     // 二进制
}
```

<figure><img src="../../.gitbook/assets/image (17).png" alt="" width="563"><figcaption></figcaption></figure>

## value：值

{% hint style="info" %}
json有六种值：空白，数字，字符串，数组，对象，真，假
{% endhint %}

```json
{
  "string_value": "这是一个字符串",
  "number_value": 42,
  "object_value": {"inner_string": "对象内的字符串"},
  "array_value": ["元素1", "元素2", "元素3"],
  "boolean_value": true,
  "null_value": null
}
```

<figure><img src="../../.gitbook/assets/image (19).png" alt="" width="563"><figcaption></figcaption></figure>

## object：对象

{% hint style="info" %}
可以是空，也可以包含任意个键值对，键必须是字符串。
{% endhint %}

```json
{} 正确
{  } 正确
{   "a":2} 正确
{   "a"   :2} 正确，键前后可以有空
{"a"} 错误，必须是键值对
{1:2} 错误，键须是字符串
```

<figure><img src="../../.gitbook/assets/image (21).png" alt="" width="563"><figcaption></figcaption></figure>

## array： 数组

{% hint style="info" %}
可以是空，也可以包含任意个值。
{% endhint %}

<figure><img src="../../.gitbook/assets/image (20).png" alt="" width="563"><figcaption></figcaption></figure>
