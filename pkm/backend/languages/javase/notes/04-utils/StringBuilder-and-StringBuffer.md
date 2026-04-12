# StringBuffer & StringBuilder

![StringBuilder-StringBuffer-drawing.excalidraw|1000](../../assets/StringBuilder-StringBuffer-drawing.excalidraw.md)
字符串专题阅读顺序：[String](../04-utils/String.md)  👉 本文

---

## String的缺点

* String 类的对象是**不可变**的。也就是说，⼀旦⼀个 String 对象被创建，它所包含的字符串内容是不可改变的。
* 每次对 String 对象进⾏修改**操作**（如拼接、替换等，尤其是使用`+`号操作符）实际上都会**⽣成⼀个新的 String 对象**，⽽不是修改原有对象。这可能会导致内存和**性能开销**，尤其是在⼤量字符串操作的情况下。

## 🍭 StringBuffer 基本概念

为了对珍贵的内存造成不必要的压力，Java 设计了一个专门用来解决此问题的 `StringBuffer` 类。

```java
public final class StringBuffer extends AbstractStringBuilder implements Serializable, CharSequence {

    public StringBuffer() {
        super(16);
    }
    
    public synchronized StringBuffer append(String str) {
        super.append(str);
        return this;
    }

    public synchronized String toString() {
        return new String(value, 0, count);
    }

    // 其他方法
}
```

* `StringBuffer`是可变长度的字符序列。可以理解成长度可变的 String
* `StringBuffer`是一个**容器**
* `StringBuffer`的父类`AbstractStringBuilder`里边有一个`char[] value;`这里存放字符串内容。⚠️不是 final 的。另外存放在堆里边而不是常量池了（因为数组在堆里边）。

---

## ✏️ StringBuilder

由于 StringBuffer 操作字符串的方法加了 [`synchronized` 关键字](https://javabetter.cn/thread/synchronized-1.html)进行了同步，主要是考虑到多线程环境下的安全问题，所以如果在非多线程环境下，执行效率就会比较低，因为加了没必要的锁。

于是 Java 就给 StringBuffer “生了个兄弟”，名叫 StringBuilder，说，“孩子，你别管线程安全了，你就在单线程环境下使用，这样效率会高得多，如果要在多线程环境下修改字符串，你到时候可以使用 [`ThreadLocal`](https://javabetter.cn/thread/ThreadLocal.html) 来避免多线程冲突。”

* 当需要在**单个线程**中频繁修改字符串内容时，推荐使用 `StringBuilder`。
* 由于 `StringBuilder` 不是线程安全的，因此在**多线程环境**中应使用 `StringBuffer`。

```java
public final class StringBuilder extends AbstractStringBuilder
   implements java.io.Serializable, CharSequence
{
   // ...

   public StringBuilder append(String str) {
      super.append(str);
      return this;
   }

   public String toString() {
      // Create a copy, don't share the array
      return new String(value, 0, count);
   }

   // ...
}
```

**除了类名不同，方法没有加 synchronized，基本上完全一样。**

实际开发中，StringBuilder 的使用频率也是远高于 StringBuffer，甚至可以这么说，StringBuilder 完全取代了 StringBuffer。

最后看一下他们三个的比较

```java
public class StringBuilderVsString {
    public static void main(String[] args) {
        String text = "";
        long startTime = 0L;
        long endTime = 0L;

        // 使用 StringBuffer
        StringBuffer buffer = new StringBuffer("");
        startTime = System.currentTimeMillis();
        for (int i = 0; i < 20000; i++) {
            buffer.append(String.valueOf(i));
        }
        endTime = System.currentTimeMillis();
        System.out.println("StringBuffer的执行时间: " + (endTime - startTime));

        // 使用 StringBuilder
        startTime = System.currentTimeMillis();
        StringBuilder builder = new StringBuilder("");
        for (int i = 0; i < 20000; i++) {
            builder.append(String.valueOf(i));
        }
        endTime = System.currentTimeMillis();
        System.out.println("StringBuilder的执行时间: " + (endTime - startTime));

        // 使用 String 进行连接
        startTime = System.currentTimeMillis();
        for (int i = 0; i < 20000; i++) {
            text = text + i;
        }
        endTime = System.currentTimeMillis();
        System.out.println("String的执行时间: " + (endTime - startTime));
    }
}
```

```bash
StringBuffer的执行时间: 1
StringBuilder的执行时间: 0
String的执行时间: 73
```

1. 如果字符串存在大量的修改操作，一般使用 StringBuffer 或 StringBuilder
2. 如果字符串存在大量的修改操作，并在单线程的情况，使用 StringBuilder
3. 如果字符串存在大量的修改操作，并在多线程的情况，使用 StringBuffer
4. 如果我们字符串很少修改，被多个对象引用，使用 String，比如配置信息等

---

## ✏️ AbstractStringBuilder 扩容机制（重点）

> 重点是扩容规则要记住，初始化大小要记住。

1. 初始大小：默认是 **16**，也可以指定初始大小。
2. 扩容大小：$$ space_{new} = space_{old} + \max{(space_{old}+2, need)} $$

案例一

```java
// 创建一个初始化容量是16的StringBuilder对象  
StringBuilder stringBuilder = new StringBuilder();   // 16
  
// 进行字符串的拼接操作  
stringBuilder.append("hello");  // 16 （用了 5）
stringBuilder.append("world");  // 16 （用了 10）
stringBuilder.append(100);      // 16 （用了 13）
stringBuilder.append(false);    // 16 + max(16+2, 2) = 34 （用了 18）
```

案例二（重点）

```java
// 创建一个初始化容量是16的StringBuilder对象  
StringBuilder stringBuilder = new StringBuilder(); // 16

stringBuilder.append("12345678910000000000000000000000000000000000000000");
// 需要扩容：34 = max(old space + 2, need) = max(16 + 2, 50 - 16)
// new = 16 + max(18, 34) = 50 (用了 50, 还剩 0)
stringBuilder.append("abcdef");
// 需要扩容：52 = max(50 + 2, 56 - 50) 
// new = 50 + max(52, 6) = 102 (用了 56)
```

下面是具体的分析

StringBuilder 初始创建过程会创建大小为 16 的空字符串

```java
/**
 * Constructs a string builder with no characters in it and an
 * initial capacity of 16 characters.
 */
public StringBuilder() {
    super(16);
}
```

在调用字符串变量相加的时候结束时，系统会默认调用 StringBuilder 的 toString()

```java
public String toString() { 
    return new String(value, 0, count); 
}
```

在调用字符串变量相加的时候，会把要相加的内容通过 append() 进行拼接

```java
public StringBuilder append(String str) {
    super.append(str);
    return this;
}
```

```java
public AbstractStringBuilder append(String str) {
    if (str == null)
        return appendNull();
    int len = str.length();
    // count + len就是 ensureCapacityInternal传入的minimumCapacity
    ensureCapacityInternal(count + len);
    str.getChars(0, len, value, count);
    count += len;
    return this;
}
```

注意如果添加的是null 就真的会添加"null"字符串进去！

```java
private AbstractStringBuilder appendNull() {  
    ensureCapacityInternal(count + 4);  
    int count = this.count;  
    byte[] val = this.value;  
    if (isLatin1()) {  
        val[count++] = 'n';  
        val[count++] = 'u';  
        val[count++] = 'l';  
        val[count++] = 'l';  
    } else {  
        count = StringUTF16.putCharsAt(val, count, 'n', 'u', 'l', 'l');  
    }  
    this.count = count;  
    return this;  
}
```

查看容量的具体代码如下

```java
private void ensureCapacityInternal(int minimumCapacity) {
    // minimumCapacity = append()的 count + len
    if (minimumCapacity - value.length > 0)
        // 不够用了，扩容
        expandCapacity(minimumCapacity);
}

void expandCapacity(int minimumCapacity) {
    // 扩容策略：新容量为旧容量的两倍加上 2
    int newCapacity = value.length * 2 + 2;
    // 如果新容量小于指定的最小容量，则新容量为指定的最小容量
    if (newCapacity - minimumCapacity < 0)
        newCapacity = minimumCapacity;
    // 如果新容量小于 0，则新容量为 Integer.MAX_VALUE
    if (newCapacity < 0) {
        if (minimumCapacity < 0) // overflow
            throw new OutOfMemoryError();
        newCapacity = Integer.MAX_VALUE;
    }
    // 将字符序列的容量扩容到新容量的大小
    value = Arrays.copyOf(value, newCapacity);
}
```

 快速记忆

 1. 初始化：默认 16，也可以指定
 2. append：默认新容量为旧容量的两倍加上 2，如果不够，就是原长度+要加的长度

---

## 🍭StringBuffer 和 String 的对比

* String 类
  * **特性**：`String` 保存的是字符串常量，其值不可更改。
  * **内存管理**：每次对 `String` 类的更新实际上是在内存中创建一个新的字符串对象，这意味着原字符串对象的地址会改变。
  * **性能**：由于每次更新都涉及到内存地址的更改，因此效率相对较低。
  * **示例代码**：

    ```java
    private final char value[];
    ```

* StringBuffer 类
  * **特性**：`StringBuffer` 保存的是字符串变量，其值可以更改。
  * **内存管理**：`StringBuffer` 的更新实际上可以在原有对象上进行，不需要每次都创建新的对象，因此不需要更新内存地址。
  * **性能**：由于不需要频繁地创建新对象和更改内存地址，因此效率较高。
  * **示例代码**：

    ```java
    char[] value; // 这个放在堆中
    ```
  
* 使用场景
  * `String` 类适合于不需要修改字符串内容的场景，因为其不可变性保证了字符串的安全性。
  * `StringBuffer` 类适合于需要频繁修改字符串内容的场景，因为它提供了更高的效率。

---

## 🍭 四种构造器

1. `StringBuffer()`
    * **描述**：构造一个不带字符的字符串缓冲区，其初始容量为 16 个字符。
    * **用途**：当你需要一个空的 `StringBuffer` 实例，并且初始容量不是问题时使用。

2. `StringBuffer(CharSequence seq)`
    * **描述**：构造一个字符串缓冲区，它包含与指定的 `CharSequence` 相同的字符。
    * **用途**：当你需要一个 `StringBuffer` 实例，并且已经有一个 `CharSequence`（如 `String`）作为内容时使用。

3. `StringBuffer(int capacity)`
    * **描述**：构造一个不带字符，但具有指定初始容量的字符串缓冲区。即对 `char[]` 大小进行指定。
    * **用途**：当你需要一个 `StringBuffer` 实例，并且知道所需的初始容量时使用，这可以避免后续的容量调整。

4. `StringBuffer(String str)`
    * **描述**：构造一个字符串缓冲区，并将其内容初始化为指定的字符串内容。
    * **用途**：当你需要一个 `StringBuffer` 实例，并且已经有一个 `String` 作为初始内容时使用。

```java
public class StringBufferExample {
  public static void main(String[] args) {
    // 使用默认构造器
    StringBuffer sb1 = new StringBuffer();
    sb1.append("Hello");
    System.out.println(sb1.toString()); // 输出: Hello

    // 使用 CharSequence 构造器
    CharSequence charSequence = "World";
    StringBuffer sb2 = new StringBuffer(charSequence);
    System.out.println(sb2.toString()); // 输出: World

    // 使用指定容量构造器
    StringBuffer sb3 = new StringBuffer(10); // 初始容量为 10
    sb3.append("Java");
    System.out.println(sb3.toString()); // 输出: Java

    // 使用 String 构造器
    StringBuffer sb4 = new StringBuffer("Kimi");
    System.out.println(sb4.toString()); // 输出: Kimi
  }
}
```

```bash
Hello
World
Java
Kimi
```

* `StringBuffer` 是一个可变的字符序列，适用于需要频繁修改字符串内容的场景。
* 选择合适的构造器可以提高程序的效率，特别是在需要大量字符串操作的情况下。
* 通过指定初始容量，可以避免多次扩容操作，从而提高性能。

---

## 🍭 StringBuffer 与 String 的转换

在 Java 开发中，经常需要在 `String` 和 `StringBuffer` 之间进行转换。以下是如何实现这些转换的详细说明和示例代码。

1. `String` 转换为 `StringBuffer`

    **方法1**：
    * 使用 `StringBuffer` 的构造器直接将 `String` 转换为 `StringBuffer`。
    * 示例代码：

    ```java
        String s = "hello";
        StringBuffer b1 = new StringBuffer(s);
    ```

    **方法2**：
    * 创建一个空的 `StringBuffer` 对象，然后使用 `append` 方法添加字符串。
    * 示例代码：

    ```java
        StringBuffer b2 = new StringBuffer();
        b2.append(s);
    ```

2. `StringBuffer` 转换为 `String`

    **方法1**：

    * 使用 `StringBuffer` 的 `toString()` 方法将 `StringBuffer` 转换为 `String`。
    * 示例代码：

      ```java
      String s2 = b1.toString();
      ```

    **方法2**：

    * 使用 `String` 的构造器，将 `StringBuffer` 作为参数传递。
    * 示例代码：

      ```java
      String s3 = new String(b1);
      ```

示例代码

```java
public class StringAndStringBuffer {
    public static void main(String[] args) {
        // String 转换为 StringBuffer
        String s = "hello";
        // 方式1: 使用构造器
        StringBuffer b1 = new StringBuffer(s);
        // 方式2: 使用 append 方法
        StringBuffer b2 = new StringBuffer();
        b2.append(s);

        // StringBuffer 转换为 String
        // 方式1: 使用 toString 方法
        String s2 = b1.toString();
        // 方式2: 使用 String 构造器
        String s3 = new String(b1);

        System.out.println("String from b1: " + s2);
        System.out.println("String from b1: " + s3);
    }
}
```

```bash
String from b1: hello
String from b1: hello
```

* `String` 是不可变的，每次修改都会创建新的对象。
* `StringBuffer` 是可变的，可以在原有对象上进行修改，适合频繁修改的场景。
* 通过上述方法，可以在 `String` 和 `StringBuffer` 之间灵活转换，以满足不同的编程需求。

---

## 🍭 StringBuffer 的常用方法

`StringBuffer` 类提供了多种方法来操作字符串缓冲区。以下是一些常用方法的笔记：

1. 增加内容 (`append`)
    * **描述**：在缓冲区的末尾追加新的字符串。
    * **示例**：

      ```java
      StringBuffer s = new StringBuffer("hello");
      s.append(", ");
      s.append("张三丰");
      System.out.println(s); // 输出: hello, 张三丰
      ```

2. 删除内容 (`delete`)
    * **描述**：删除缓冲区中从 `start` 到 `end`（不包括 `end`）的字符。
    * **示例**：

      ```java
      s.delete(11, 14);
      System.out.println(s); // 输出: hello, 张三丰
      ```

3. 修改内容 (`replace`)
    * **描述**：将缓冲区中从 `start` 到 `end`（不包括 `end`）的内容替换为新的字符串。
    * **示例**：

      ```java
      s.replace(9, 11, "周芷若");
      System.out.println(s); // 输出: hello, 周芷若
      ```

4. 查找索引 (`indexOf`)
    * **描述**：查找子串在字符串中第一次出现的索引，如果找不到返回 -1。
    * **示例**：

      ```java
      int index = s.indexOf("张三丰");
      System.out.println(index); // 输出: -1
      ```

5. 插入内容 (`insert`)
    * **描述**：在指定位置插入字符串。
    * **示例**：

      ```java
      s.insert(9, "赵敏");
      System.out.println(s); // 输出: hello, 赵敏, 周芷若
      ```

6. 获取长度 (`length`)
    * **描述**：获取缓冲区中字符串的长度。
    * **示例**：

      ```java
      System.out.println(s.length()); // 输出: 18
      ```

```java
public class StringBufferMethods {
    public static void main(String[] args) {
        StringBuffer s = new StringBuffer("hello");

        // 增加内容
        s.append(", ");
        s.append("张三丰");
        System.out.println(s); // hello, 张三丰

        // 删除内容
        s.delete(11, 14);
        System.out.println(s); // hello, 张三丰

        // 修改内容
        s.replace(9, 11, "周芷若");
        System.out.println(s); // hello, 周芷若

        // 查找索引
        int index = s.indexOf("张三丰");
        System.out.println(index); // -1

        // 插入内容
        s.insert(9, "赵敏");
        System.out.println(s); // hello, 赵敏, 周芷若

        // 获取长度
        System.out.println(s.length()); // 18
    }
}
```

```bash
hello, 张三丰
hello, 张三丰
hello, 周芷若
-1
hello, 赵敏, 周芷若
18
```

* `StringBuffer` 是一个可变的字符序列，适合在需要频繁修改字符串内容的场景中使用。
* 通过这些方法，可以方便地对字符串缓冲区进行增删改查等操作。

练习（有点坑，请留意）

```java
String str = null;
StringBuffer sb = new StringBuffer();
sb.append(str);  // append 如果插入的是空，就是加入了“null”字符串！！！⚠️
System.out.println(sb.length()); // 4

System.out.println(sb); // null
StringBuffer sb1 = new StringBuffer(str); // 构造器不能插入null，报错！空指针异常
System.out.println(sb1);
```

练习

输入商品名称和商品价格，要求打印效果示例，使用前面学习的方法完成：
商品名 商品价格
手机 123,564.59

要求：**价格的小数点前面每三位用逗号隔开**。

```java
package ex_commom;  
  
import java.util.Scanner;  
  
public class StringBufferEx {  
    public static void main(String[] args){  
        Scanner scanner = new Scanner(System.in);  
        System.out.print("请输入商品名:");  
        String name = new String(scanner.next());  
        System.out.print("请输入商品价格:");  
        // StringBuffer sb = new StringBuffer(scanner.nextDouble()+"");  
        StringBuffer sb = new StringBuffer("123456789.0");  
        int index = sb.indexOf(".");  
        for(int i=index-3; i>0; i-=3)  
            sb.insert(i, ",");  
        System.out.print("商品\t商品价格");  
        System.out.print(name+"\t"+sb);  
    }  
}
```

