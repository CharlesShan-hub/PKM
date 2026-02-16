# BufferedReader

`BufferedReader` 是 Java I/O 体系中**带缓冲的字符输入流（Reader）**，用于提高字符读取效率，特别是按行读取文本数据。

## 介绍
1. 🏅核心特性
   | 特性 | 说明 |
   | :--- | :--- |
   | **继承关系** | `java.io.Reader` → `java.io.BufferedReader` |
   | **缓冲机制** | 内置 **8KB (8192)** 字符缓冲区，减少磁盘 I/O 次数 |
   | **数据单位** | 字符（char）或字符串（String） |
   | **设计模式** | **装饰者模式（Decorator）**，通常包装 `FileReader` 或 `InputStreamReader` |

2. 🔑核心API
   | 分类 | API | 说明 |
   | :--- | :--- | :--- |
   | **构造器** | `BufferedReader(Reader in)` | 创建默认缓冲区（8KB）的缓冲流 |
   | | `BufferedReader(Reader in, int sz)` | 创建指定缓冲区大小的缓冲流 |
   | **常用方法** | `String readLine()` | 读取一行文本（不含换行符），返回 `null` 表示结束 |
   | | `int read()` | 读取单个字符 |
   | | `int read(char[] cbuf)` | 读取多个字符到数组 |
   | | `Stream<String> lines()` | 返回行的流（JDK 8+） |
   | | `void mark(int readAheadLimit)` | 标记当前位置（支持回退） |
   | | `void reset()` | 回退到标记位置 |
   | | `void close()` | 关闭流（会自动关闭被包装的 Reader） |

3. ✅ 适用场景
   1. **按行读取**：解析日志、配置文件、CSV 等文本数据。
   2. **高性能读取**：读取大文件时，缓冲机制能显著提升性能。
   3. **网络通信**：读取 Socket 传输的文本指令。

4. ❌ 不适用场景
   1. **读取二进制文件**：请使用 `BufferedInputStream`。

## 代码示例

### 1. 逐行读取（推荐）
最常用的读取方式，使用 `readLine()` 遍历文件。

```java
import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

public class ReadLines {
    public static void main(String[] args) {
        String path = "assets/a.txt";
        
        try (BufferedReader br = new BufferedReader(new FileReader(path))) {
            String line;
            // readLine() 返回 null 表示读到末尾
            while ((line = br.readLine()) != null) {
                System.out.println(line);
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
```

### 2. 使用 Stream API (JDK 8+)
更现代的函数式写法，代码更简洁。

```java
import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

public class ReadLinesStream {
    public static void main(String[] args) {
        String path = "assets/a.txt";
        
        try (BufferedReader br = new BufferedReader(new FileReader(path))) {
            // lines() 返回 Stream<String>，可直接进行 filter, map 等操作
            br.lines()
              .filter(s -> !s.isEmpty()) // 过滤空行
              .forEach(System.out::println);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
```

### 3. Mark 和 Reset
`BufferedReader` 支持标记和重置，可用于重复读取某段内容。

```java
import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

public class MarkResetDemo {
    public static void main(String[] args) {
        String path = "assets/bib.txt";
        
        try (BufferedReader br = new BufferedReader(new FileReader(path))) {
            if (!br.markSupported()) {
                System.out.println("当前流不支持 mark/reset");
                return;
            }

            // 1. 读取第一行
            System.out.println("Line 1: " + br.readLine());

            // 2. 标记当前位置（参数：保留标记的字符数限制）
            br.mark(1024);

            // 3. 继续读取后续两行
            System.out.println("Line 2: " + br.readLine());
            System.out.println("Line 3: " + br.readLine());

            // 4. 重置回标记位置（即回到 Line 1 之后，Line 2 之前）
            System.out.println("--- 执行 reset ---");
            br.reset();

            // 5. 重新读取（将再次读到 Line 2 和 Line 3）
            System.out.println("Re-read Line 2: " + br.readLine());
            System.out.println("Re-read Line 3: " + br.readLine());
            
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
```

## 源码解析
`BufferedReader` 内部维护了一个 `char[]` 数组作为缓冲区，默认大小为 8192。

```java
public class BufferedReader extends Reader {
    private Reader in;
    private char cb[];
    private static int defaultCharBufferSize = 8192; // 默认 8KB

    public BufferedReader(Reader in) {
        this(in, defaultCharBufferSize);
    }

    public BufferedReader(Reader in, int sz) {
        super(in);
        if (sz <= 0)
            throw new IllegalArgumentException("Buffer size <= 0");
        this.in = in;
        cb = new char[sz]; // 初始化缓冲区
        // ...
    }
    // ...
}
```
