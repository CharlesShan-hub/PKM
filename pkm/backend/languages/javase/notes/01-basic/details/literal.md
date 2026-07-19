# 字面量

## 什么是字面量
Java 中，字面量指的是在程序中直接使用的数据，字面量是 Java 中最基本的表达式，不需要进行计算或转换，直接使用即可。


## Java 中都有哪些字面量
- 整数型：10、-5、0、100
- 浮点型：3.14、-0.5、1.0
- 布尔型：true、false
- 字符型：'a'、'b'、'c'、'1'、'2'、'国'
- 字符串型："Hello"、"World"、"Java"、"你好呀"


## 加号运算符
1. 加号“+”在 Java 中是一种运算符，有两个作用：
    1. 求和
    2. 字符串拼接：+ 的任意一边只要是字符串类型，做字符串拼接操作，拼接之后的结果还是一个字符串。其它情况一律是求和操作。
2. 判断以下程序的输出结果

```java
System.out.println(5 + 6);
System.out.println("5" + "6");
System.out.println("5" + 6 + 7);
System.out.println("5" + (6 + 7));
System.out.println(5 + 6 + "7");
System.out.println(5 + "6" + 7);
System.out.println(5 + (6 + "7")); // 添加小括号优先级较高
```
