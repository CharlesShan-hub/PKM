# PrintStreams

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

参考[[PrintWriter]]