
# JSONL

## Links

* \[1]官网：[https://jsonlines.org/](https://jsonlines.org/)
* \[2][https://manifold.net/doc/mfd9/jsonl.htm](https://manifold.net/doc/mfd9/jsonl.htm)

## Notes

1. jsonl syntax\[2]
   1. JSONL是一种基于文本的格式，使用.jsonl文件扩展名，基本上与[JSON](https://manifold.net/doc/mfd9/json.htm)格式相同，但使用换行符来分隔JSON值。也称为_**JSON Lines**_。
   2. jsonl 每一行是一个 json，一次解析一行，每一行不超过 2G，这对于在内存有限的机器上处理非常大的文件非常有用。
2. JSON vs  JSONL\[2]
   1. JSONL使用UTF-8编码。这与JSON不同，JSON允许使用ASCII转义序列编码Unicode字符串。
   2. 每一行都是有效的JSON值。
   3. 每一行都用一个换行符"\n“分隔。这意味着还支持回车、换行符序列“\r\n”，因为在解析JSON值时会隐式忽略周围的白色空格。文件中的最后一个字符可能是行分隔符，它将被视为没有行分隔符。
3. JSONL 有时比 CSV 更好，因为CSV 损坏了很难处理。

## Demo

JSONL better than csv\[1]

```json
["Name", "Session", "Score", "Completed"]
["Gilbert", "2013", 24, true]
["Alexa", "2013", 29, true]
["May", "2012B", 14, false]
["Deloise", "2012A", 19, true] 
```

JSONL with nested structure\[1]

```json
{"name": "Gilbert", "wins": [["straight", "7♣"], ["one pair", "10♥"]]}
{"name": "Alexa", "wins": [["two pair", "4♠"], ["two pair", "9♠"]]}
{"name": "May", "wins": []}
{"name": "Deloise", "wins": [["three of a kind", "5♣"]]}
```

