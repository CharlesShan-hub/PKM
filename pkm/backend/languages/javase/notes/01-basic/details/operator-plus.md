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

```bash
11
56
567
513
137
567
567
```