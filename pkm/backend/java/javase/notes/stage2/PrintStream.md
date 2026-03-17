# PrintStream

`PrintStream` 是 Java I/O 体系中的**字节打印流**，它为其他输出流添加了功能，使它们能够方便地打印各种数据值表示形式。我们最熟悉的 `System.out` 就是一个 `PrintStream` 实例。

## 介绍
1. 🏅核心特性

    | 特性 | 说明 |
    | :--- | :--- |
    | **继承关系** | `java.io.OutputStream` → `java.io.FilterOutputStream` → `java.io.PrintStream` |
    | **主要作用** | 方便地打印各种数据类型（int, boolean, String 等） |
    | **异常处理** | **永远不会抛出 IOException**（需调用 `checkError()` 检查错误） |
    | **自动刷新** | 可配置自动刷新（遇到换行符或 `println` 时刷新） |

2. 🔑核心API

   | 分类 | API | 说明 |
   | :--- | :--- | :--- |
   | **构造器** | `PrintStream(OutputStream out)` | 包装一个输出流 |
   | | `PrintStream(String fileName)` | 直接写入指定文件 |
   | | `PrintStream(File file)` | 直接写入指定文件对象 |
   | **常用方法** | `print(Any data)` | 打印数据（不换行） |
   | | `println(Any data)` | 打印数据并换行 |
   | | `printf(String format, Object... args)` | 格式化输出（类似 C 语言） |
   | | `System.setOut(PrintStream out)` | 重定向标准输出流 |

3. ✅ 适用场景
   1. **日志输出**：向控制台或日志文件打印调试信息。
   2. **格式化输出**：需要生成特定格式的文本报告。

## 代码示例

### 1. 基本打印示例
```java
// PrintStream 示例（字节流）
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.PrintStream;

public class PrintStreamAndPrintWriterExample {
  public static void main(String[] args) {
    try{
      // PrintStream ps = new PrintStream(new FileOutputStream(filePath));
      PrintStream ps = new PrintStream(System.out);
      ps.println(64);
      ps.write((byte)64);
      ps.write("\nHello, PrintStream!".getBytes());
      ps.close();
    }catch(IOException e) {
      e.printStackTrace();
    }
  }
}
```

### 2. 详细功能测试
```java
package com.powernode.javase.io;  

import java.io.FileOutputStream;  
import java.io.FileWriter;  
import java.io.PrintStream;  

/**  
 * 1. java.io.PrintStream：打印流（专业的负责打印的流，字节形式。）  
 * 2. PrintStream不需要手动刷新，自动刷新。  
 */  
public class PrintStreamTest {  
  public static void main(String[] args) throws Exception{  
    // 创建一个打印流对象  
    // 构造方法：PrintStream(OutputStream out)  
    // 构造方法：PrintStream(String fileName)  
    PrintStream ps = new PrintStream("log1");  

    // 没有这样的构造方法，PrintWriter可以
    //PrintStream ps2 = new PrintStream(new FileWriter(""));  

    //PrintStream ps2 = new PrintStream(new FileOutputStream("log1"));  
    // 打印流可以打印各种数据类型数据。  
    ps.print(100);  
    ps.println(false);  
    ps.println("abc");  
    ps.println('T');  
    ps.println(3.14);  
    ps.println("hell world");  
    ps.println(200);  

    ps.println("\"hello world!\"");  

    String name = "张三";  
    double score = 95.5;  

    ps.printf("姓名：%s，考试成绩：%.2f", name, score);  // 这里格式化的内容很多

    // 关闭  
    ps.close();  
  }  
}
```

参考 [PrintWriter](PrintWriter.md)
