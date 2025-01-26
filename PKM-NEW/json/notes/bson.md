
# BSON

## Links

* 官网：[https://bsonspec.org/](https://bsonspec.org/)
* mongodb：[https://www.mongodb.com/resources/languages/bson](https://www.mongodb.com/resources/languages/bson)
* wiki：[https://en.wikipedia.org/wiki/BSON](https://en.wikipedia.org/wiki/BSON)
* youtube demo：[https://www.youtube.com/watch?v=pYbBRRJkwc0](https://www.youtube.com/watch?v=pYbBRRJkwc0)

## Wiki Notes

* BSON起源于2009年的[MongoDB](https://en.wikipedia.org/wiki/MongoDB)
* 与JSON相比，BSON在存储空间和扫描速度方面都很高效。
* JSON的一个重要区别是BSON包含JSON中不存在的类型（例如日期时间，字节数组和适当的IEEE 754浮点数），并为几个数字类型提供严格的类型处理，而不是通用的“数字”类型。

## Demo

* 每一个对象，首先要写它的大小，然后写内部的元素。
* 每一个元素，首先要写它的键的类型（具体见：[https://bsonspec.org/spec.html](https://bsonspec.org/spec.html)）然后是键的名字的二进制，然后是值。
* 键和值和对象，都用0x00作为结尾。

<figure><img src="../../.gitbook/assets/image (112).png" alt=""><figcaption></figcaption></figure>
