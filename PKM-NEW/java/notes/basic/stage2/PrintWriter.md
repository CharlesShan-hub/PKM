# PrintWriter

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

参考[[PrintStream]]