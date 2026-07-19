# 布尔类型

## 基本特性
* **大小**：占用1字节
* **取值**：只能是 `true` 或 `false`
* **与C的区别**：不能用0或非零整数代替 `boolean`

```java
boolean isReady = true;
boolean isFinished = false;

// 错误：Java不支持数值到boolean的转换
// int flag = 1;
// boolean b = flag;
```


## 面试题：boolean占用多少字节
对于单独的boolean变量，理论上是1字节，但是JVM会对内存进行补齐，所以后边增加了三字节的空白。如果再加上对象头，一共占用了32 字节。

```bash
Size of boolean array: [Z object internals:
 OFFSET  SIZE      TYPE DESCRIPTION                               VALUE
      0     4           (object header)                           01 00 00 00 (00000001 00000000 00000000 00000000) (1)
      4     4           (object header)                           00 00 00 00 (00000000 00000000 00000000 00000000) (0)
      8     4           (object header)                           00 63 17 00 (00000000 01100011 00010111 00000000) (1532672)
     12     4           (object header)                           06 00 00 00 (00000110 00000000 00000000 00000000) (6)
     16     6   boolean [Z.<elements>                             N/A
     22     2           (loss due to the next object alignment)
Instance size: 24 bytes
Space losses: 0 bytes internal + 2 bytes external = 2 bytes total
```

对于boolean类型的数组（比如长度为6），也是会补齐4字节为单位的一行，所以也是会有一定的冗余，但数组内部每个boolean都是1字节。

```bash
Size of boolean array: [Z object internals:
 OFFSET  SIZE      TYPE DESCRIPTION                               VALUE
      0     4           (object header)                           01 00 00 00 (00000001 00000000 00000000 00000000) (1)
      4     4           (object header)                           00 00 00 00 (00000000 00000000 00000000 00000000) (0)
      8     4           (object header)                           00 63 17 00 (00000000 01100011 00010111 00000000) (1532672)
     12     4           (object header)                           06 00 00 00 (00000110 00000000 00000000 00000000) (6)
     16     6   boolean [Z.<elements>                             N/A
     22     2           (loss due to the next object alignment)
Instance size: 24 bytes
Space losses: 0 bytes internal + 2 bytes external = 2 bytes total
```
