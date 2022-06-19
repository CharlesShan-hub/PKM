# JSON语法

2022.6.16

[toc]

## 主要用法

* 数组（Array）用方括号表示

* 对象（Object）用圆括号表示

* 键值对（Name/Value）组合成数组和对象

* 名称（Name）置于双引号中，

* 值（Value）：注意不能有函数和`undefined`

  * 字符串：注意使用双引号，不能使用单引号

  * 数值：注意

    <img src="https://www.json.org/img/number.png" style="zoom: 33%;" />

  * null

  * 对象

  * 数组

* 并列的数据用逗号分隔

* ```json
  {
    "string":"Chalres Shan",
    "array":[100,1e-4,
             true,false,
             ["nested"],
             {"test":null}
            ]
  }
  ```

## 外部链接

* [JSON - Wiki](https://zh.wikipedia.org/wiki/JSON)
* [JSON在线解析器](https://www.json.cn/)
* [JSON Community](http://json.com/)
* [JSON 官方简介](https://www.json.org/json-en.html)
* [JSON ECMA标准](https://www.ecma-international.org/wp-content/uploads/ECMA-404_2nd_edition_december_2017.pdf)