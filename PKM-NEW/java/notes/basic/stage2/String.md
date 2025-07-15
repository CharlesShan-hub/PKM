# String

![[../../../assets/String-drawing| 1000]]

---
## String

### 🍭 基本概念

1. String 对象用于保存字符串，也就是一组字符序列
2. 字符串常量对象是用双引号括起的字符序列。例如："你好"、"12.97"、"boy"
3. String 类较常用构造器（其它看手册）：
    - `String s1 = new String();` // 默认构造器，创建一个空字符串
    - `String s2 = new String(String original);` // 通过另一个字符串对象创建
    - `String s3 = new String(char[] a);` // 通过字符数组创建
    - `String s4 = new String(char[] a, int startindex, int count)` // 通过字符数组的一部分创建
    - `String s5 = new String(bytes[] b)`
    - 还有很多其他的

### ✏️ 源码分析

```java
// String.java, java8
public final class String  
	implements java.io.Serializable, Comparable<String>, CharSequence,  
			   Constable, ConstantDesc {
	private final char[] value;
	...
}
```

```java
// String.java, java9开始
public final class String  
	implements java.io.Serializable, Comparable<String>, CharSequence,  
			   Constable, ConstantDesc {
	private final byte[] value;
	private final byte coder;
	...
}
```

1. 内部字符数组的保存
	1. java9之前：String 内部实现仍然是 `char[]`，字符串的字符使用 **Unicode** 字符编码，**一个字符（不区分字母还是汉字）占两个字节**。
	2. java9 开始：使用`byte[]`保存字符串，针对 JDK 9 的 String 源码里，为了区别编码方式，追加了一个 coder 字段来区分。Java 会根据字符串的内容自动设置为相应的编码，要么 Latin-1 要么 UTF16。
	3. 从 `char[]` 到 `byte[]`，最主要的目的是**节省字符串占用的内存空间**。内存占用减少带来的另外一个好处，就是 [GC](https://javabetter.cn/jvm/gc.html) 次数也会减少。
2. String 继承了 `Serializable` 接口：String 可以通过网络传输
3. String 继承了 `Comparable` 接口：String 可以相互比较
4. **String 是一个 final 类**： String 不能被其他的类继承
5. String 内部存放 **byte/char 数组的对象也是 final**：对象不能被修改，但是对象内部的内容可以被修改（value 不能指向新的地址，但是单独字符的内容是可以变换的）
	```java
	public class StringAndCharArrayExample {
		public static void main(String[] args) {
			// 字符串的重新赋值
			String name = "jack";
			System.out.println("Before changing name: " + name);
			name = "tom";
			System.out.println("After changing name: " + name);
	
			// final 关键字和字符数组的操作
			final char[] value = {'a', 'b', 'c'};
			char[] v2 = {'t', 'u', 'm'};
	
			// 修改字符数组中的元素
			value[0] = 'H';
			System.out.println("Modified value array: " + new String(value));
	
			// 尝试重新赋值给 final 关键字修饰的数组（编译错误）
			// value = v2; // 这行代码会导致编译错误，因为 final 关键字修饰的数组不能被重新赋值
	
			// 输出结果
			System.out.println("v2 array: " + new String(v2));
		}
	}
	```
6. 相比之下，后边的`StringBuilder`就把内容保存在了非`final`的`Byte`数组中。
	```java
	// AbstractStringBuilder.java
	abstract sealed class AbstractStringBuilder implements Appendable, CharSequence  
	    permits StringBuilder, StringBuffer {  
	    /**  
	     * The value is used for character storage.     
	     */    
	     byte[] value;
	     ...
	     }
	}
	```

### 常用方法

#### 🍭方法总结

1. `substring(int beginIndex, int endIndex)`
	1. **描述**：返回一个新字符串，它是此字符串的一个子字符串。
	2. **案例**
		```java
		String str = "Hello, World!";
		String subStr = str.substring(0, 5);
		System.out.println("Substring: " + subStr);
		```
	3. **源码**
		```java
		public String substring(int beginIndex) {
		    // 检查起始索引是否小于 0，如果是，则抛出 StringIndexOutOfBoundsException 异常
		    if (beginIndex < 0) {
		        throw new StringIndexOutOfBoundsException(beginIndex);
		    }
		    // 计算子字符串的长度
		    int subLen = value.length - beginIndex;
		    // 检查子字符串长度是否为负数，如果是，则抛出 StringIndexOutOfBoundsException 异常
		    if (subLen < 0) {
		        throw new StringIndexOutOfBoundsException(subLen);
		    }
		    // 如果起始索引为 0，则返回原字符串；否则，创建并返回新的字符串
		    return (beginIndex == 0) ? this : new String(value, beginIndex, subLen);
		}
		```
2. `length()`
	1. **描述**：返回字符串的长度。
	2. **案例**
		```java
		String str = "Hello, World!";
		int length = str.length();
		System.out.println("Length of the string: " + length);
		```
3. `charAt(int index)`
	1. **描述**：返回指定索引处的字符。
	2. **案例**
		```java
		String str = "Hello";
		char firstChar = str.charAt(0);
		System.out.println("First character: " + firstChar);
		```
4. `indexOf(String str)` 和 `lastIndexOf(String str)`
	1. **描述**：返回指定子字符串在此字符串中第一次出现的索引。
	2. **案例**：
		```java
		String str = "Hello, World!";
		int index = str.indexOf("World");
		System.out.println("Index of 'World': " + index);
		```
5. `replace(CharSequence target, CharSequence replacement)`
	1. **描述**：返回一个新的字符串，它是通过用新子字符串替换此字符串中所有出现的给定目标子字符串得到的。
	2. **案例**
		```java
		String str = "Hello, World!";
		String newStr = str.replace("World", "Java");
		System.out.println("Replaced string: " + newStr);
		```
6. `toUpperCase()` 和 `toLowerCase()`
	1. **描述**：将此字符串转换为大写或小写。
	2. **案例**：
		```java
		String str = "Hello, World!";
		String upperStr = str.toUpperCase();
		String lowerStr = str.toLowerCase();
		System.out.println("Uppercase: " + upperStr);
		System.out.println("Lowercase: " + lowerStr);
		```
7. `trim()`
	1. **描述**：去除字符串两端的空白字符。
	2. **案例**：
		```java
		String str = "   Hello, World!   ";
		String trimmedStr = str.trim();
		System.out.println("Trimmed string: " + trimmedStr);
		```
8. `split(String regex)`
	1. **描述**：根据给定正则表达式的匹配拆分此字符串。
	2. **案例**
		```java
		String str = "one,two,three";
		String[] parts = str.split(",");
		System.out.println("Split strings:");
		for (String part : parts) {
			System.out.println(part);
		}
		```
9. `equals(Object anObject)` 和 `equalsIgnoreCase(String anotherString)`
	1. **描述**：比较两个字符串是否相等。
	2. **案例**
		```java
		String str1 = "Hello";
		String str2 = "hello";
		boolean isEqual = str1.equals(str2);
		boolean isEqualIgnoreCase = str1.equalsIgnoreCase(str2);
		System.out.println("Equal: " + isEqual);
		System.out.println("Equal ignoring case: " + isEqualIgnoreCase);
		```

#### 🍭 `format()` 

**描述**：根据格式字符串（format string）和后续参数来格式化字符串。
**语法**：
```java
String.format(String format, Object... args)
```

- `format`：格式字符串，其中可以包含普通文本和格式说明符（如 `%d`、`%s` 等）。
- `args`：一个或多个参数，用于替换格式字符串中的格式说明符。
- `%s`：字符串
- `%d` 或 `%i`：十进制整数
- `%f`：浮点数（默认小数点后6位）
- `%.2f`：浮点数，保留两位小数
- `%x` 或 `%X`：十六进制整数
- `%b` 或 `%B`：二进制整数
- `%c`：字符
- `%h`：十六进制哈希码

```java
public class FormatExample {
    public static void main(String[] args) {
        // 格式化字符串
        String name = "Kimi";
        int age = 30;
        double pi = Math.PI;

        // 使用 String.format() 格式化字符串
        String info = String.format("Name: %s, Age: %d, PI: %.2f", name, age, pi);
        System.out.println(info);

        // 更多格式化示例
        String hex = String.format("Hexadecimal: %x", 255);
        String binary = String.format("Binary: %b", 9);
        String hash = String.format("Hash code: %h", "example");

        System.out.println(hex);
        System.out.println(binary);
        System.out.println(hash);
    }
}
```

```
Name: Kimi, Age: 30, PI: 3.14
Hexadecimal: ff
Binary: 1001
Hash code: 6c657874
```

- `String.format()` 方法非常灵活，可以用于各种复杂的格式化需求。
- 除了基本的数据类型格式化，还可以通过 `%` 后跟字母（如 `%+`、`%-`、`%,` 等）来控制格式化的细节，例如正负号显示、对齐方式、千位分隔符等。
- 从 Java 7 开始，`String.format()` 支持 `Locale` 参数，可以用于实现本地化格式化。

通过这些示例和说明，你应该能够更好地理解和使用 `String.format()` 方法来处理字符串格式化。

#### ✏️ [hashCode()](https://javabetter.cn/string/string-source.html#string-%E7%B1%BB%E7%9A%84-hashcode-%E6%96%B9%E6%B3%95)

每一个字符串都会有一个 hash 值，这个哈希值在很大概率是不会重复的，因此 String 很适合来作为 [HashMap](https://javabetter.cn/collection/hashmap.html)（后面会细讲）的键值。

```java
// String.java
private int hash; // 缓存字符串的哈希码

public int hashCode() {
    int h = hash; // 从缓存中获取哈希码
    // 如果哈希码未被计算过（即为 0）且字符串不为空，则计算哈希码
    if (h == 0 && value.length > 0) {
        char val[] = value; // 获取字符串的字符数组

        // 遍历字符串的每个字符来计算哈希码
        for (int i = 0; i < value.length; i++) {
            h = 31 * h + val[i]; // 使用 31 作为乘法因子
        }
        hash = h; // 缓存计算后的哈希码
    }
    return h; // 返回哈希码
}
```

hashCode 方法首先检查是否已经计算过哈希码，如果已经计算过，则直接返回缓存的哈希码。否则，方法将使用一个循环遍历字符串的所有字符，并使用一个乘法和加法的组合计算哈希码。

这种计算方法被称为“31 倍哈希法”。计算完成后，将得到的哈希值存储在 hash 成员变量中，以便下次调用 hashCode 方法时直接返回该值，而不需要重新计算。这是一种缓存优化，称为“惰性计算”。31 倍哈希法的优点在于简单易实现，计算速度快，同时也比较均匀地分布在哈希表中。

**31 倍哈希法（31-Hash）** 是一种简单有效的字符串哈希算法，常用于对字符串进行哈希处理。该算法的基本思想是将字符串中的每个字符乘以一个固定的质数 31 的幂次方，并将它们相加得到哈希值。具体地，假设字符串为 s，长度为 n，则 31 倍哈希值计算公式如下：

```java
H(s) = (s[0] * 31^(n-1)) + (s[1] * 31^(n-2)) + ... + (s[n-1] * 31^0)
```

模拟计算Hash
```java
public class HashCodeExample {
    public static void main(String[] args) {
        String text = "沉默王二";
        int hashCode = computeHashCode(text);
        System.out.println("字符串 \"" + text + "\" 的哈希码是: " + hashCode);

        System.out.println("String 的 hashCode " + text.hashCode());
    }

    public static int computeHashCode(String text) {
        int h = 0;
        for (int i = 0; i < text.length(); i++) {
            h = 31 * h + text.charAt(i);
        }
        return h;
    }
}
```

### 内存分析

#### ✏️ 常量池

Java专门在堆中为字符串准备了一个**字符串常量池**。因为字符串使用比较频繁，放在字符串常量池中省去了对象的创建过程，从而提高程序的执行效率。（常量池属于一种缓存技术，缓存技术是提高程序执行效率的重要手段。）

```java
// s1是一个引用。保存了对象的内存地址。  
String s1 = "hello";  
// s2是一个引用。保存了对象的内存地址。  
String s2 = "hello";  
  
System.out.println(s1 == s2); // true  
// 因为运行的时候，两个 hello 也因为都是字符串常量所有在内存中其实是同一个内容
  
String s3 = "test";  
String s4 = new String("test");  
System.out.println(s3 == s4); // false  
  
// 比较两个字符串是否相等，靠谱一点的，还是equals方法。别用 ==
System.out.println(s3.equals(s4)); // true
```

#### 🍭 常用的构造方法

* `String(char[] value)`：根据字符数组创建一个新的字符串对象。
* `String(char[] value, int offset, int count)`：根据字符数组的指定部分创建一个新的字符串对象。
* `String(byte[] bytes)`：根据字节数组创建一个新的字符串对象，默认使用平台默认的字符集进行解码。
* `String(byte[] bytes, int offset, int length)`：根据字节数组的指定部分创建一个新的字符串对象，默认使用平台默认的字符集进行**解码**。
* `String(byte[] bytes, Charset charset)`：
	* 根据字节数组和指定的字符集创建一个新的字符串对象。
	* new String(bytes, Charset.defaultCharset());
* `String(byte[] bytes, String charsetName)`：
	* 根据字节数组和指定的字符集名称创建一个新的字符串对象。
	* 这是一个解码的过程。你需要提前知道“byte[] bytes”是通过哪个编码方式进行编码得到的。
	* 如果通过GBK的方式进行编码得到的“byte[] bytes”，调用以上构造方法时采用UTF-8的方式进行解码。就会出现乱码。
* `String(String original)`：
	* 通过复制现有字符串创建一个新的字符串对象。
	* 这个方法被@IntrinsicCandidate标注，这个注解的作用是告诉编译器,该方法或构造函数是一个内在的候选方法,可以被优化和替换为更高效的代码。因此它是**不建议使用**的。
	* new String(“hello”); 这个代码会让常量池中有一个 “hello”，并且在堆中也有有一个String对象。

```java
package com.powernode.javase.stringtest;  
  
import java.io.UnsupportedEncodingException;  
import java.nio.charset.Charset;  
import java.nio.charset.StandardCharsets;  
  
/**  
 * 关于String类的构造方法  
 */  
public class StringTest03 {  
    public static void main(String[] args) throws UnsupportedEncodingException {  
  
        // 有一个char[]数组，可以将char[]数组转换成字符串  
        char[] chars = new char[]{'动','力','节','点'};  
        // 转换成字符串  
        String s1 = new String(chars);  
        System.out.println(s1);  
  
        // 将char[]数组的一部分转换成字符串  
        String s2 = new String(chars, 0, 2);  
        System.out.println(s2);  
  
        // 有一个byte[]数组，可以将byte[]数组转换成字符串  
        byte[] bytes = {97,98,99,100};  
        // 将byte[]数组转换成字符串String，是一个解码的过程。（采用的是平台默认的字符编码方式进行的解码。）  
        String s3 = new String(bytes);  
        System.out.println(s3);  
  
        // 将byte[]数组的一部分转换成字符串（解码的过程，也是采用平台默认的字符集。）  
        String s4 = new String(bytes, 0, 2);  
        System.out.println(s4);  
  
        // 乱码的本质：在进行编码和解码的时候没有使用同一个字符编码方式。  
        // 先将字符串转换成byte[]数组（这个过程是一个编码的过程）  
        // 这里先按照GBK的字符集进行编码。（GBK是简体中文）  
        //byte[] bs = "动力节点，一家只教授Java的培训机构".getBytes("UTF-8");  
        byte[] bs = "动力节点，一家只教授Java的培训机构".getBytes(StandardCharsets.UTF_8);  
  
        // 将以上的byte[]数组转换成字符串（这个过程是一个解码的过程）  
        //String s5 = new String(bs, "UTF-8");  
        String s5 = new String(bs, StandardCharsets.UTF_8);  
  
        System.out.println(s5);  
  
        // 在不知道字符编码方式的时候，可以动态获取平台的编码方式。（使用平台默认的字符集进行编码）  
        byte[] bs2 = "动力节点".getBytes(Charset.defaultCharset());  
  
        // 使用平台默认的字符集进行解码。  
        String s6 = new String(bs2, Charset.defaultCharset());  
  
        System.out.println(s6);  
  
        // 创建一个字符串对象，也是可以这样做的。但不建议了。  
        // 内在的候选方法，不建议使用了。  
        // 被@IntrinsicCandidate注解标注了。这个注解是Java16引入的。  
        //String s7 = new String("STRING"); 
        // 底层会有两个对象，一个是"STRING"在字符串常量池中。一个是在堆内存中。浪费内存。  
        String s8 = "STRING";  
    }  
}
```

#### ✏️ 创建方式1：直接赋值

```java
String s = "hsp";
```
- **描述**：这种方式直接将字符串字面量赋值给变量`s`。
- **内存管理**：
  - Java虚拟机（JVM）会在常量池中查找是否存在相同的字符串字面量。
  - 如果常量池中已经存在"hsp"，则直接让变量`s`指向常量池中的这个字符串，不会创建新的对象。
  - 如果常量池中不存在，则创建一个新的字符串对象，并将其放入常量池，然后让变量`s`指向这个新创建的对象。
- **性能**：这种方式通常更高效，因为它利用了常量池来避免重复创建相同的字符串对象。

```java
String a = "java";
String b = "java";
System.out.println(a.equals(b)); // true
System.out.println(a == b); // true
```

#### ✏️ 创建方式2：构造器

```java
String s2 = new String("hsp");
```

- **描述**：通过调用`String`类的构造器来创建一个新的字符串对象。
- **内存管理**：
  - **无论常量池中是否存在相同的字符串，都会在堆内存中创建一个新的字符串对象。**
  - 这种方式会维护`String`对象的`value`属性，指向新创建的字符数组。
  - 如果常量池中不存在"hsp"，则创建新对象；如果存在，也会创建新对象，但新对象的内容与常量池中的对象相同。
- **性能**：这种方式通常不如直接赋值高效，因为它总是创建新的对象，增加了内存的使用和垃圾回收的负担。

- **直接赋值**（方式一）**更高效**，因为它利用了常量池来避免重复创建相同的字符串对象，减少了内存的使用。
- **调用构造器**（方式二）在需要修改字符串内容或需要新对象时使用，但通常不推荐用于创建字符串常量，因为它会增加内存的使用和垃圾回收的负担。

练习：以下语句创建了几个对象？画出内存布局图。（两个）

```java
String s1 = "hello";
s1 = "haha";
```

```json
{
	'栈':{
		s1: Ox11,//第一句
		s1: 0x22//第二句后变成了这样
	},
	'常量池':{
		0x11: "Hello",//(第一个对象)
		0x22: "haha"//（第二个对象，都是字符串常量对象）
	}
}
```

练习

```java
String s1 = "hsped"; // 指向常量池 hsped
String s2 = "java"; // 指向常量池 java
String s4 = "java"; // 指向常量池 java
String s3 = new String("java");//指向堆，堆变量的 value 再指向常量池java
System.out.println(s2 == s3);      // f
System.out.println(s2 == s4);      // t
System.out.println(s2.equals(s3)); // t
System.out.println(s1 == s2);      // f 
```

练习

```java
Person p1 = new Person();
p1.name = "hsped";
Person p2 = new Person();
p2.name = "hsped";

System.out.println(p1.name.equals(p2.name)); // t
System.out.println(p1.name == p2.name); // t
System.out.println(p1.name == "hsped"); // t

String s1 = new String("bcde");
String s2 = new String("bcde");
System.out.println(s1 == s2); // f
```

#### ✏️ 字符串相加

练习：创建了几个对象？

```java
String a = "hello" + "abc";
```

```json
{
	'栈':{
		a: 0x33;
	},
	'堆':{
	},
	'常量池':{
		// 0x11: "Hello",
		// 0x22: "haha",
		// 上边两个被编译器优化没了，因为他们没有引用指向，不要把编译器当成傻子
		0x33: "Hellohaha"（只有 1 个对象）
	}
}
```

练习：创建了几个对象

```java
String a = "Hello";
String b = "abv";
String c = a + b;
```

创建了 5 个对象，其中常量池中有 3 个
具体创建的过程如下：
1. 先创建一个 StringBuilder sb = StringBuilder(); // 堆中创建一个 StringBuilder 对象
2. 执行 sb.append("hello");
3. sb.append("abc");
4. String c = sb.toString(); // 这里会创建一个 String 对象
5. 最后其实是 c 指向堆中的对象(String) value[] -> 池中 "helloabc"

```json
{
	'栈':{
		a: 0x11,
		b: 0x22,
		c: 0x88
	},
	'堆':{
		0x88: { // 5
			value: 0x33,
		}
		0x99: StringBuilder sb // 4
	},
	'常量池':{
		0x11: "Hello", // 1
		0x22: "haha", // 2
		0x33: "Hellohaha" // 3
	}
}
```

如果后边继续

```java
String d = "Helloabc";
System.out.println(c == d); // false，因为 c 指向 0x88，d 直接指向了常量池
```

练习：创建了几个对象？

```java
final String s2 = "b";  
String s3 = "a" + s2;  
```

还是一个！直接是"ab"，因为 s2 是final 了，所以编译器又可以优化了。

**❗️重要总结：常量相加，找常量池。变量相加，找堆。**

#### ✏️ intern

练习

```java
String a = "hsp"; // a 指向 常量池的 "hsp"
String b = new String("hsp"); // b 指向堆中对象
System.out.println(a.equals(b)); // T
System.out.println(a == b); // F
System.out.println(a == b.intern()); // intern方法自己先查看API, T
System.out.println(b == b.intern()); // F
```

练习：下面代码输出什么，并说明原因。

```java
String s1 = "hsped";
String s2 = "java";
String s5 = "hspedjava";
String s6 = (s1 + s2).intern();    // intern代表放到了常量池里边
System.out.println(s5 == s6);      // true，因为 intern 了，所以又指向常量池了
System.out.println(s5.equals(s6)); // true
```

练习：下列程序运行的结果是什么，尝试画出内存布局图？

```java
public class Test1 {
    String str = new String("hsp");
    final char[] ch = { 'j', 'a', 'v', 'a' };
    public void change(String str, char ch[]) {
        str = "java";
        ch[0] = 'h';
    }
    public static void main(String[] args) {
        Test1 ex = new Test1();
        ex.change(ex.str, ex.ch);
        System.out.print(ex.str + " and ");
        System.out.println(ex.ch);
    }
} // 思考，认真看，仔细想
```

change函数拿到 str，一开始指向 ex.str。后来因为 String 不能变，所以修改的是 change 的函数指向了常量池中的 “java”并不会更不会影响到 main 栈里边的 ex.str。所以结果为 hsp，hava

为什么 hava 变了呢，因为原来的数组存在堆里边，j 变成了 h。

为什么 hsp 没变，因为新的字符串在方法区，原来堆里边的引用对象没有变化。

综合面试题

```java
package com.powernode.javase.stringtest;  
  
import org.junit.jupiter.api.Test;  
  
/**  
 * String类常见的面试题。  
 */  
public class StringExam {  
    @Test  
    public void test1(){  
        String s1 = "abc";  
        String s2 = new String("abc");  
        System.out.println(s1 == s2); // false  
        System.out.println(s1.equals(s2)); // true  
    }  
  
    @Test  
    public void test2(){  
        // 这种拼接会在编译阶段完成。编译器优化策略。  
        String s1 = "a" + "b" + "c";  
        String s2 = "abc";  
        System.out.println(s1 == s2); // true  
    }  
  
    @Test  
    public void test3(){  
        String s1 = "abc";  
        String s2 = "ab";  
        String s3 = s2 + "c";  
        System.out.println(s1 == s3); // false  
        System.out.println(s1.equals(s3)); // true  
    }  
  
    @Test  
    public void test4(){  
        // 问题：创建了几个对象？  
        // 字符串常量池中1个  
        String s1 = "a";  
        // 字符串常量池中1个 ，堆1个。  
        String s2 = new String("b");  
        // 堆中2个。（StringBuilder对象，String对象）  
        String s3 = s1 + s2;  
    }  
  
    @Test  
    public void test5(){  
        // 问题：创建了几个对象？  
        // 6个对象  
        // 字符串常量池中2个  
        // StringBuilder1个  
        // 堆中的String 3个。  
        String s = new String("a") + new String("b");  
    }  
  
    @Test  
    public void test6(){  
        // 这个程序会出现异常吗？如果没有异常，结果是什么？  
        // 不会出现异常，结果是：nullnull  
        String s1 = null;  
        String s2 = s1 + null;  
        System.out.println(s2);  
    }  
  
    @Test  
    public void test7(){  
  
        String s1 = "ab";  
  
        final String s2 = "b";  
        String s3 = "a" + s2;  
  
        // 和这个一样了。  
        //String s3 = "a" + "b";  
  
        System.out.println(s1 == s3);  
        // 因为final String s2，所以编译阶段还是把"a"和 s2 拼接了
    }  
  
    @Test  
    public void test8(){  
  
        String s1 = "ab";  
  
        final String s2 = getB();  
        String s3 = "a" + s2;  
  
        System.out.println(s1 == s3); // false  
    }  

    @Test  
    public void test9(){  
        String s1 = "a1";  
        String s2 = "a" + 1;  
        System.out.println(s1 == s2); // true  
    }  
  
    @Test  
    public void test10(){  
        String s1 = new String("abc");  
        System.out.println(s1);  
  
        StringBuilder s2 = new StringBuilder("abc");  
        System.out.println(s2);  
  
        // 类型不一样，没有比较的意义。  
        // 类型不一样，结果一定是false。  
        System.out.println(s1.equals(s2)); // false  
    }  
}
```

### 🍭 String与正则表达式

* [[re]]
* [[史上最全正则表达式]]

* String replace(CharSequence target, CharSequence replacement);
	* 将当前字符串中所有的target替换成replacement，返回一个新的字符串。
* String replaceAll(String regex, String replacement);
	* 将当前字符串中所有符合正则表达式的regex替换成replacement。
* String[] split(String regex);
	* 将当前字符串以某个正则表达式表示的子字符串进行分割，返回一个字符串数组。
* boolean matches(String regex);
	* 判断当前字符串是否符合正则表达式regex。

```java
package com.powernode.javase.stringtest;  
  
import org.junit.jupiter.api.Test;  
  
import java.util.ArrayList;  
import java.util.List;  
  
/**  
 * 测试用例  
 */  
public class StringMethodTest {  
  
    @Test  
    public void testMatches(){  
        // 邮箱地址的正则表达式  
        String emailRegExp = "^\\w+([-+.]\\w+)*@\\w+([-.]\\w+)*\\.\\w+([-.]\\w+)*$";  
        String email = "dujubin@126.com";  
  
        System.out.println(email.matches(emailRegExp));  
  
    }  
  
    @Test  
    public void testSplit(){  
        // 根据正则表达式进行字符串的拆分  
        // 拆分后返回一个字符串数组  
        String[] strs = "动1力2节3点4。".split("\\d");  
        System.out.println(strs.length);  
        for(String s : strs){  
            System.out.println(s);  
        }  
  
        String[] ymd = "1970-10-11".split("-");  
        for(String s : ymd){  
            System.out.println(s);  
        }  
  
        String data = "name=zhangsan&password=123&email=zhangsan@123.com&gender=男";  
        String[] params = data.split("&");  
        for(String param : params) {  
            //System.out.println(param);  
            String[] nameAndValue = param.split("=");  
            for(String s : nameAndValue){  
                System.out.println(s);  
            }  
        }  
    }  
}
```

---
## StringBuffer & StringBuilder

### 🍭 StringBuffer 基本概念

由于[字符串是不可变的](https://javabetter.cn/string/immutable.html)，所以当遇到[字符串拼接](https://javabetter.cn/string/join.html)（尤其是使用`+`号操作符）的时候，就需要考量性能的问题，你不能毫无顾虑地生产太多 String 对象，对珍贵的内存造成不必要的压力。于是 Java 就设计了一个专门用来解决此问题的 StringBuffer 类。

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

### ✏️ StringBuilder

由于 StringBuffer 操作字符串的方法加了 [`synchronized` 关键字](https://javabetter.cn/thread/synchronized-1.html)进行了同步，主要是考虑到多线程环境下的安全问题，所以如果在非多线程环境下，执行效率就会比较低，因为加了没必要的锁。

于是 Java 就给 StringBuffer “生了个兄弟”，名叫 StringBuilder，说，“孩子，你别管线程安全了，你就在单线程环境下使用，这样效率会高得多，如果要在多线程环境下修改字符串，你到时候可以使用 [`ThreadLocal`](https://javabetter.cn/thread/ThreadLocal.html) 来避免多线程冲突。”

- 当需要在单个线程中频繁修改字符串内容时，推荐使用 `StringBuilder`。
- 由于 `StringBuilder` 不是线程安全的，因此在多线程环境中应使用 `StringBuffer`。

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

### ✏️ AbstractStringBuilder 扩容机制（重点）

> 重点是扩容规则要记住，初始化大小要记住。

1. 初始大小：默认是 **16**，也可以指定初始大小。
2. 扩容大小：$$space_{new} = space_{old} + \max{(space_{old}+2, need)}$$

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
// 最少需要扩容：34 = max(0, 50 - 16)
// 16 + max(16+2, 34) = 50 (用了 50)
stringBuilder.append("abcdef");
// 最少需要扩容：6 = max(0, 56 - 50) 
// 50 + max(50+2, 6) = 102 (用了 56)
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

如果添加的字符串不是 null，那么就会去查看容量了

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
 1.  初始化：默认 16，也可以指定
 2. append：默认新容量为旧容量的两倍加上 2，如果不够，就是原长度+要加的长度

### 🍭 StringBuffer 和 String 的对比

* String 类
	- **特性**：`String` 保存的是字符串常量，其值不可更改。
	- **内存管理**：每次对 `String` 类的更新实际上是在内存中创建一个新的字符串对象，这意味着原字符串对象的地址会改变。
	- **性能**：由于每次更新都涉及到内存地址的更改，因此效率相对较低。
	- **示例代码**：
	    ```java
	    private final char value[];
	    ```
	    
* StringBuffer 类
	- **特性**：`StringBuffer` 保存的是字符串变量，其值可以更改。
	- **内存管理**：`StringBuffer` 的更新实际上可以在原有对象上进行，不需要每次都创建新的对象，因此不需要更新内存地址。
	- **性能**：由于不需要频繁地创建新对象和更改内存地址，因此效率较高。
	- **示例代码**：
	    ```java
	    char[] value; // 这个放在堆中
	    ```
    
* 使用场景
	- `String` 类适合于不需要修改字符串内容的场景，因为其不可变性保证了字符串的安全性。
	- `StringBuffer` 类适合于需要频繁修改字符串内容的场景，因为它提供了更高的效率。

### 🍭 四种构造器

1. `StringBuffer()`
	- **描述**：构造一个不带字符的字符串缓冲区，其初始容量为 16 个字符。
	- **用途**：当你需要一个空的 `StringBuffer` 实例，并且初始容量不是问题时使用。

2. `StringBuffer(CharSequence seq)`
	- **描述**：构造一个字符串缓冲区，它包含与指定的 `CharSequence` 相同的字符。
	- **用途**：当你需要一个 `StringBuffer` 实例，并且已经有一个 `CharSequence`（如 `String`）作为内容时使用。

3. `StringBuffer(int capacity)`
	- **描述**：构造一个不带字符，但具有指定初始容量的字符串缓冲区。即对 `char[]` 大小进行指定。
	- **用途**：当你需要一个 `StringBuffer` 实例，并且知道所需的初始容量时使用，这可以避免后续的容量调整。

4. `StringBuffer(String str)`
	- **描述**：构造一个字符串缓冲区，并将其内容初始化为指定的字符串内容。
	- **用途**：当你需要一个 `StringBuffer` 实例，并且已经有一个 `String` 作为初始内容时使用。

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

```
Hello
World
Java
Kimi
```

- `StringBuffer` 是一个可变的字符序列，适用于需要频繁修改字符串内容的场景。
- 选择合适的构造器可以提高程序的效率，特别是在需要大量字符串操作的情况下。
- 通过指定初始容量，可以避免多次扩容操作，从而提高性能。

### 🍭 StringBuffer 与 String 的转换

在 Java 开发中，经常需要在 `String` 和 `StringBuffer` 之间进行转换。以下是如何实现这些转换的详细说明和示例代码。

1. `String` 转换为 `StringBuffer`

**方法1**：
- 使用 `StringBuffer` 的构造器直接将 `String` 转换为 `StringBuffer`。
- 示例代码：
  ```java
  String s = "hello";
  StringBuffer b1 = new StringBuffer(s);
  ```

**方法2**：
- 创建一个空的 `StringBuffer` 对象，然后使用 `append` 方法添加字符串。
- 示例代码：
  ```java
  StringBuffer b2 = new StringBuffer();
  b2.append(s);
  ```

2. `StringBuffer` 转换为 `String`

**方法1**：
- 使用 `StringBuffer` 的 `toString()` 方法将 `StringBuffer` 转换为 `String`。
- 示例代码：
  ```java
  String s2 = b1.toString();
  ```

**方法2**：
- 使用 `String` 的构造器，将 `StringBuffer` 作为参数传递。
- 示例代码：
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

```
String from b1: hello
String from b1: hello
```

- `String` 是不可变的，每次修改都会创建新的对象。
- `StringBuffer` 是可变的，可以在原有对象上进行修改，适合频繁修改的场景。
- 通过上述方法，可以在 `String` 和 `StringBuffer` 之间灵活转换，以满足不同的编程需求。

### 🍭 StringBuffer 的常用方法

`StringBuffer` 类提供了多种方法来操作字符串缓冲区。以下是一些常用方法的笔记：

1. 增加内容 (`append`)
	- **描述**：在缓冲区的末尾追加新的字符串。
	- **示例**：
	  ```java
	  StringBuffer s = new StringBuffer("hello");
	  s.append(", ");
	  s.append("张三丰");
	  System.out.println(s); // 输出: hello, 张三丰
	  ```

2. 删除内容 (`delete`)
	- **描述**：删除缓冲区中从 `start` 到 `end`（不包括 `end`）的字符。
	- **示例**：
	  ```java
	  s.delete(11, 14);
	  System.out.println(s); // 输出: hello, 张三丰
	  ```

3. 修改内容 (`replace`)
	- **描述**：将缓冲区中从 `start` 到 `end`（不包括 `end`）的内容替换为新的字符串。
	- **示例**：
	  ```java
	  s.replace(9, 11, "周芷若");
	  System.out.println(s); // 输出: hello, 周芷若
	  ```

4. 查找索引 (`indexOf`)
	- **描述**：查找子串在字符串中第一次出现的索引，如果找不到返回 -1。
	- **示例**：
	  ```java
	  int index = s.indexOf("张三丰");
	  System.out.println(index); // 输出: -1
	  ```

5. 插入内容 (`insert`)
	- **描述**：在指定位置插入字符串。
	- **示例**：
	  ```java
	  s.insert(9, "赵敏");
	  System.out.println(s); // 输出: hello, 赵敏, 周芷若
	  ```

6. 获取长度 (`length`)
	- **描述**：获取缓冲区中字符串的长度。
	- **示例**：
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

```
hello, 张三丰
hello, 张三丰
hello, 周芷若
-1
hello, 赵敏, 周芷若
18
```

- `StringBuffer` 是一个可变的字符序列，适合在需要频繁修改字符串内容的场景中使用。
- 通过这些方法，可以方便地对字符串缓冲区进行增删改查等操作。

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

