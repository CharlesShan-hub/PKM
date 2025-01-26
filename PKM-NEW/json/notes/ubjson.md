
# UBJSON

## Links

* \[1] Wiki：[https://en.wikipedia.org/wiki/UBJSON](https://en.wikipedia.org/wiki/UBJSON)
* \[2] 官网：[https://ubjson.org/](https://ubjson.org/)

## Notes

1. Overview
   1. JSON规范本身完全兼容
   2. 数据结构（平均）比压缩JSON小30%
2.  数据类型

    ```
    [type, 1-byte char]([integer numeric length])([data])
    ```

    具体的数据类型请看：[https://ubjson.org/type-reference/](https://ubjson.org/type-reference/)
3. 案例

```json
[
    null,
    true,
    false,
    4782345193,
    153.132,
    "ham"
]
[[]
    [Z]
    [T]
    [F]
    [l][4782345193]
    [d][153.132]
    [S][i][3][ham]
[]]
```

```json
{
    "post": {
        "id": 1137,
        "author": "rkalla",
        "timestamp": 1364482090592,
        "body": "I totally agree!"
    }
}
[{]
    [i][4][post][{]
        [i][2][id][I][1137]
        [i][6][author][S][i][5][rkalla]
        [i][9][timestamp][L][1364482090592]
        [i][4][body][S][i][16][I totally agree!]
    [}]
[}]
```

{% hint style="info" %}
我的感觉是，就是把一些常见的类型，比如 null，true，false编码一下，字符串的话，就是长度+字符，其实变化不大。
{% endhint %}
