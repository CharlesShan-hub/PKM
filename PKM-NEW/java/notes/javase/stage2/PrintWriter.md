# PrintWriter

`PrintWriter` 是 Java I/O 体系中的**字符打印流**，功能与 `PrintStream` 非常相似，但它是基于**字符流（Writer）**实现的，因此更适合处理文本数据的输出，尤其是涉及国际化字符集时。

## 介绍
1. 🏅核心特性

	| 特性       | 说明                                              |
	| :------- | :---------------------------------------------- |
	| **继承关系** | `java.io.Writer` → `java.io.PrintWriter`        |
	| **主要作用** | 方便地打印各种数据类型的字符形式                                |
	| **构造灵活** | 既可以包装 `OutputStream`（字节流），也可以包装 `Writer`（字符流）   |
	| **异常处理** | **永远不会抛出 IOException**（需调用 `checkError()` 检查错误） |


2. 🔑核心API

   | 分类 | API | 说明 |
   | :--- | :--- | :--- |
   | **构造器** | `PrintWriter(Writer out)` | 包装一个字符输出流 |
   | | `PrintWriter(OutputStream out)` | 包装一个字节输出流 |
   | | `PrintWriter(String fileName)` | 直接写入指定文件 |
   | **常用方法** | `print(Any data)` | 打印数据 |
   | | `println(Any data)` | 打印数据并换行 |
   | | `printf(String format, Object... args)` | 格式化输出 |

3. ✅ 适用场景
   4. **Web 开发**：Servlet 中的 `response.getWriter()` 返回的就是 `PrintWriter`。
   5. **文本文件生成**：生成 HTML、XML、JSON 等纯文本文件。

## 代码示例

### 1. 基本打印示例
```java
// PrintWriter 示例（字符流）
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.PrintWriter;

public class PrintStreamAndPrintWriterExample {
  public static void main(String[] args) {
    // Using try-with-resources for auto-close
    try (PrintWriter ps = new PrintWriter(System.out)) {
      ps.println(64);
      ps.write((char)64);
      ps.write("\nHello, PrintWriter!");

      // Check for errors if needed
      if (ps.checkError()) {
        System.err.println("An error occurred during writing");
      }
    }
    // No catch block needed since PrintWriter doesn't throw IOExceptions
  }
}
```

### 2. 构造与刷新测试
```java
package com.powernode.javase.io;  

import java.io.FileWriter;  
import java.io.PrintWriter;  

/**  
 * java.io.PrintWriter：专门负责打印的流。（字符形式）  
 * 需要手动刷新flush。  
 * PrintWriter比PrintStream多一个构造方法：  
 *      PrintStream构造方法：  
 *          PrintStream(OutputStream)  
 *      PrintWriter构造方法：  
 *          PrintWriter(OutputStream)  
 *          PrintWriter(Writer) 
 */
public class PrintWriterTest {  
  public static void main(String[] args) throws Exception{  
    // 创建字符打印流  
    //PrintWriter pw = new PrintWriter(new FileOutputStream("log2"));  

    PrintWriter pw = new PrintWriter(new FileWriter("log2"), true);  

    // 打印  
    pw.println("world hello!!!");  
    pw.println("zhangsan hello!!!");  

    // 刷新  
    //pw.flush();  

    // 关闭  
    pw.close();  
  }  
}
```

参考 [PrintStream](PrintStream.md)
