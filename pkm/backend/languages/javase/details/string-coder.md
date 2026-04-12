# String 的 coder 字段
---
## 第一步：`char[]`变成`byte[]`
1. java9之前：String 内部实现仍然是 `char[]`，字符串的字符使用 **Unicode** 字符编码，**一个字符（不区分字母还是汉字）占两个字节**。
2. java9 开始：使用`byte[]`保存字符串，的目的是**节省字符串占用的内存空间**。内存占用减少带来的另外一个好处，就是 [GC](https://javabetter.cn/jvm/gc.html) 次数也会减少。

---
## 第二步：编码方式选择
[jdk9为何要将String的底层实现由char[]改成了byte[]?](https://www.zhihu.com/question/447224628)

针对 JDK 9 的 String 源码里，为了区别编码方式，追加了一个 coder 字段来区分。Java 会根据字符串的内容自动设置为相应的编码，要么 Latin-1 要么 UTF16。
```java
/**
 * The identifier of the encoding used to encode the bytes in
 * {@code value}. The supported values in this implementation are
 *
 * LATIN1
 * UTF16
 *
 * @implNote This field is trusted by the VM, and is a subject to
 * constant folding if String instance is constant. Overwriting this
 * field after construction will cause problems.
 */
private final byte coder;
```
