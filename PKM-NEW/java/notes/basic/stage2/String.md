# String

![[../../../assets/String-drawing| 1000]]

---
## String

### 基本概念

1. **String 对象用于保存字符串，也就是一组字符序列**
2. 字符串常量对象是用双引号括起的字符序列。例如："你好"、"12.97"、"boy"等
3. **字符串的字符使用 Unicode 字符编码，一个字符（不区分字母还是汉字）占两个字节。**
4. **String 类较常用构造器（其它看手册）：**
    
    - `String s1 = new String();` // 默认构造器，创建一个空字符串
    - `String s2 = new String(String original);` // 通过另一个字符串对象创建
    - `String s3 = new String(char[] a);` // 通过字符数组创建
    - `String s4 = new String(char[] a, int startindex, int count)` // 通过字符数组的一部分创建
    - `String s5 = new String(bytes[] b)`
    - 还有很多其他的
5. String 继承了 `Serializable` 接口：String 可以通过网络传输
6. String 继承了 `Comparable` 接口：String 可以相互比较
7. String 是一个 final 类：不能被其他的类继承

### String 的内存分析

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

练习 1。以下语句创建了几个对象？画出内存布局图。

```java
String s1 = "hello";
s1 = "haha";
```

```json
{
	'栈':{
		s1: Ox88,//第一句
		s1: 0x22//第二句后变成了这样
	},
	'堆':{
		0x88: {
			value: 0x11,
		}
	},
	'常量池':{
		0x11: "Hello",(第一个对象)
		0x22: "haha"（第二个对象，都是字符串常量对象）
	}
}
```

练习 2。创建了几个对象？

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

练习 3。创建了几个对象

```java
String a = "Hello";
String b = "abv";
String c = a + b;
```

这样三个对象，但是注意，c 是指向堆的。
具体创建的过程如下：
1. 先创建一个 StringBuilder sb = StringBuilder()
2. 执行 sb.append("hello");
3. sb.append("abc");
4. String c = sb.toString();
5. 最后其实是 c 指向堆中的对象(String) value[] -> 池中 "helloabc"

```json
{
	'栈':{
		a: 0x11,
		b: 0x22,
		c: 0x88
	},
	'堆':{
		0x88: {
			value: 0x33,
		}
	},
	'常量池':{
		0x11: "Hello",
		0x22: "haha",
		0x33: "Hellohaha"
	}
}
```

如果后边继续

```java
String d = "Helloabc";
System.out.println(c == d); // false，因为 c 指向 0x88，d 直接指向了常量池
```

**❗️重要总结：常量相加，找常量池。变量相加，找堆。**

练习 4。下面代码输出什么，并说明原因。

```java
String s1 = "hsped";
String s2 = "java";
String s5 = "hspedjava";
String s6 = (s1 + s2).intern();    // intern代表放到了常量池里边
System.out.println(s5 == s6);      // true，因为 intern 了，所以又指向常量池了
System.out.println(s5.equals(s6)); // true
```

练习 5。下列程序运行的结果是什么，尝试画出内存布局图？

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


### String不能修改

1. String 内部的内容保存在了：`private final byte[] value;`，**所以 String 不可修改，注意，他的不可修改不是值不可修改，而是地址不能修改（value 不能指向新的地址，但是单独字符的内容是可以变换的）**【面试会问】
	```java
	// String.java
	public final class String  
		implements java.io.Serializable, Comparable<String>, CharSequence,  
				   Constable, ConstantDesc {
		private final byte[] value;
		...
	}
	```

2. 相比之下，后边的`StringBuilder`就把内容保存在了非`final`的`Byte`数组中。
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

3. Java8之前保存在`private final char[] value;`，Java9 开始保存在`private final byte[] value;`了因为可以**节省空间**。

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

### 两种创建方式

在Java中，创建`String`对象有两种主要方式，每种方式在内存管理和性能上有不同的表现。

#### 方式一：直接赋值

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

#### 方式二：调用构造器

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

String 常用的构造方法

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

#### 练习

Demo

```java
public class StringCreationExample {
    public static void main(String[] args) {
        // 方式一：直接赋值
        String s = "hsp";
        System.out.println("s: " + s);

        // 方式二：调用构造器
        String s2 = new String("hsp");
        System.out.println("s2: " + s2);
    }
}
```

```
s: hsp
s2: hsp
```

练习

```java
String a = "hsp"; // a 指向 常量池的 "hsp"
String b = new String("hsp"); // b 指向堆中对象
System.out.println(a.equals(b)); // T
System.out.println(a == b); // F
System.out.println(a == b.intern()); // intern方法自己先查看API, T
System.out.println(b == b.intern()); // F
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

### 常用方法

Java 中的 `String` 类提供了许多用于字符串操作的方法。以下是一些常用的方法及其案例：

1. `length()`

	**描述**：返回字符串的长度。
	
	**案例**：
	```java
	String str = "Hello, World!";
	int length = str.length();
	System.out.println("Length of the string: " + length);
	```

2. `charAt(int index)`

	**描述**：返回指定索引处的字符。
	
	**案例**：
	```java
	String str = "Hello";
	char firstChar = str.charAt(0);
	System.out.println("First character: " + firstChar);
	```

3. `substring(int beginIndex, int endIndex)`

	**描述**：返回一个新字符串，它是此字符串的一个子字符串。
	
	**案例**：
	```java
	String str = "Hello, World!";
	String subStr = str.substring(0, 5);
	System.out.println("Substring: " + subStr);
	```

4. `indexOf(String str)` 和 `lastIndexOf(String str)`

	**描述**：返回指定子字符串在此字符串中第一次出现的索引。
	
	**案例**：
	```java
	String str = "Hello, World!";
	int index = str.indexOf("World");
	System.out.println("Index of 'World': " + index);
	```

5. `replace(CharSequence target, CharSequence replacement)`

	**描述**：返回一个新的字符串，它是通过用新子字符串替换此字符串中所有出现的给定目标子字符串得到的。
	
	**案例**：
	```java
	String str = "Hello, World!";
	String newStr = str.replace("World", "Java");
	System.out.println("Replaced string: " + newStr);
	```

6. `toUpperCase()` 和 `toLowerCase()`

	**描述**：将此字符串转换为大写或小写。
	
	**案例**：
	```java
	String str = "Hello, World!";
	String upperStr = str.toUpperCase();
	String lowerStr = str.toLowerCase();
	System.out.println("Uppercase: " + upperStr);
	System.out.println("Lowercase: " + lowerStr);
	```

7. `trim()`

	**描述**：去除字符串两端的空白字符。
	
	**案例**：
	```java
	String str = "   Hello, World!   ";
	String trimmedStr = str.trim();
	System.out.println("Trimmed string: " + trimmedStr);
	```

8. `split(String regex)`

	**描述**：根据给定正则表达式的匹配拆分此字符串。
	
	**案例**：
	```java
	String str = "one,two,three";
	String[] parts = str.split(",");
	System.out.println("Split strings:");
	for (String part : parts) {
	    System.out.println(part);
	}
	```

9. `equals(Object anObject)` 和 `equalsIgnoreCase(String anotherString)`

	**描述**：比较两个字符串是否相等。
	
	**案例**：
	```java
	String str1 = "Hello";
	String str2 = "hello";
	boolean isEqual = str1.equals(str2);
	boolean isEqualIgnoreCase = str1.equalsIgnoreCase(str2);
	System.out.println("Equal: " + isEqual);
	System.out.println("Equal ignoring case: " + isEqualIgnoreCase);
	```

	这些方法涵盖了字符串的基本操作，包括长度获取、字符访问、子字符串提取、字符串替换、大小写转换、空白去除、字符串分割以及字符串比较等。通过这些方法，可以方便地对字符串进行各种操作。
	
	确实，`String.format()` 是 Java 中处理字符串格式化的一个非常有用的工具。它允许你按照指定的格式来构造字符串，类似于 C 语言中的 `printf` 函数。

### `String.format()` 方法

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

### String与正则表达式

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

### 面试题

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

---
## StringBuffer

### stringbuffer 是什么

* `StringBuffer`是可变长度的字符序列。可以理解成长度可变的 String
* `StringBuffer`是一个**容器**
	```java
	public final class StringBuffer  
	    extends AbstractStringBuilder  
	    implements Appendable, Serializable, Comparable<StringBuffer>, CharSequence  
	{}
	```
* `StringBuffer`的父类`AbstractStringBuilder`里边有一个`char[] value;`这里存放字符串内容。⚠️不是 final 的。另外存放在堆里边而不是常量池了（因为数组在堆里边）。

### stringbuffer 和 string 的对比

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
	    // char[] value; // 这个放在堆中
	    ```
    
* 使用场景
	- `String` 类适合于不需要修改字符串内容的场景，因为其不可变性保证了字符串的安全性。
	- `StringBuffer` 类适合于需要频繁修改字符串内容的场景，因为它提供了更高的效率。

### 四种构造器

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

### StringBuffer 与 String 的转换

在 Java 开发中，经常需要在 `String` 和 `StringBuffer` 之间进行转换。以下是如何实现这些转换的详细说明和示例代码。

1. String 转换为 StringBuffer

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

2. StringBuffer 转换为 String

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

### StringBuffer 的常用方法

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

---
## StringBuilder

### 基本介绍

1. **描述**：
   - `StringBuilder` 是一个可变的字符序列类。
   - 提供了与 `StringBuffer` 兼容的 API，但不保证同步。
   - 设计为 `StringBuffer` 的一个简易替换，用于字符串缓冲区被单个线程使用时。
   - 在大多数实现中，`StringBuilder` 比 `StringBuffer` 更快，因为它不需要同步。

2. **主要操作**：
   - 主要操作是 `append` 和 `insert` 方法。
   - 这些方法可以重载，以接受任意类型的数据。

### 使用场景

- 当需要在单个线程中频繁修改字符串内容时，推荐使用 `StringBuilder`。
- 由于 `StringBuilder` 不是线程安全的，因此在多线程环境中应使用 `StringBuffer`。

### 示例代码

```java
public class StringBuilderExample {
    public static void main(String[] args) {
        StringBuilder sb = new StringBuilder("Hello");
        sb.append(", World!"); // 使用 append 方法添加字符串
        System.out.println(sb.toString()); // 输出: Hello, World!

        sb.insert(7, "Java"); // 在索引 7 处插入字符串 "Java"
        System.out.println(sb.toString()); // 输出: Hello, JavaWorld!

        // 重载 append 方法，接受任意类型的数据
        sb.append(123).append(true).append(45.67);
        System.out.println(sb.toString()); // 输出: Hello, JavaWorld!123true45.67
    }
}
```

```
Hello, World!
Hello, JavaWorld!
Hello, JavaWorld!123true45.67
```


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
