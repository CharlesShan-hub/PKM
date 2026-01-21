# BufferedWriter

`BufferedWriter` 是 Java I/O 体系中**带缓冲的字符输出流（Writer）**，用于提高字符写入效率，特别是频繁写入文本数据时。

## 介绍
1. 🏅核心特性
   | 特性 | 说明 |
   | :--- | :--- |
   | **继承关系** | `java.io.Writer` → `java.io.BufferedWriter` |
   | **缓冲机制** | 内置 **8KB (8192)** 字符缓冲区，减少磁盘 I/O 次数 |
   | **数据单位** | 字符（char）或字符串（String） |
   | **设计模式** | **装饰者模式（Decorator）**，通常包装 `FileWriter` 或 `OutputStreamWriter` |

2. 🔑核心API
   | 分类 | API | 说明 |
   | :--- | :--- | :--- |
   | **构造器** | `BufferedWriter(Writer out)` | 创建默认缓冲区（8KB）的缓冲流 |
   | | `BufferedWriter(Writer out, int sz)` | 创建指定缓冲区大小的缓冲流 |
   | **常用方法** | `void write(String s)` | 写入字符串 |
   | | `void newLine()` | 写入一个系统相关的换行符（推荐） |
   | | `void flush()` | 刷新缓冲区（强制写入磁盘） |
   | | `void close()` | 关闭流（自动刷新并关闭被包装的 Writer） |

3. ✅ 适用场景
   1. **文本写入**：生成日志文件、导出报表、写入配置文件等。
   2. **高性能写入**：相比 `FileWriter` 逐字写入，缓冲机制能大幅提升性能。
   3. **跨平台换行**：`newLine()` 自动适配 Windows (`\r\n`)、Linux (`\n`) 等系统。

4. ❌ 不适用场景
   1. **二进制文件**：图片、视频等二进制数据请使用 `BufferedOutputStream`。

## 代码示例

### 1. 基本写入
演示如何使用 `BufferedWriter` 写入文本并换行。

```java
import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;

public class WriteText {
    public static void main(String[] args) {
        String path = "assets/output.txt";
        
        // 使用 try-with-resources 自动关闭流
        try (BufferedWriter bw = new BufferedWriter(new FileWriter(path))) { // 默认覆盖模式
            bw.write("Hello, BufferedWriter!");
            bw.newLine(); // 写入系统适配的换行符
            bw.write("This is a new line.");
            
            // 写入部分字符串
            bw.newLine();
            bw.write("Test substring", 0, 4); // "Test"
            
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
```

### 2. 追加模式
通过 `FileWriter` 的构造参数开启追加模式。

```java
import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;

public class AppendText {
    public static void main(String[] args) {
        String path = "assets/output.txt";
        
        // FileWriter 第二个参数 true 表示追加
        try (BufferedWriter bw = new BufferedWriter(new FileWriter(path, true))) {
            bw.newLine();
            bw.write("--- Appended Content ---");
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
```

### 3. 文件拷贝 (文本)
结合 `BufferedReader` 实现高效的文本文件拷贝。

> ⚠️ 注意：不要用字符流拷贝图片、视频等二进制文件，会导致文件损坏。

```java
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;

public class FileCopyText {
    public static void main(String[] args) {
        String sourceFile = "assets/a.txt";
        String targetFile = "assets/a_copy.txt";
        
        try (
            BufferedReader br = new BufferedReader(new FileReader(sourceFile));
            BufferedWriter bw = new BufferedWriter(new FileWriter(targetFile))
        ) {
            String line;
            while ((line = br.readLine()) != null) {
                bw.write(line);
                bw.newLine(); // 补上换行符（readLine 不包含换行符）
            }
            System.out.println("文件拷贝完成！");
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
```
