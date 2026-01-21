# FileWriter

`FileWriter` 是 Java I/O 体系中**字符输出流（Writer）**的子类，专门用于将字符数据写入文件。

## 介绍
1. 🏅核心特性
   | 特性 | 说明 |
   | :--- | :--- |
   | **继承关系** | `java.io.Writer` → `java.io.OutputStreamWriter` → `java.io.FileWriter` |
   | **数据单位** | 以**字符（char）**或**字符串（String）**为单位写入 |
   | **写入方式** | 顺序写入（默认覆盖，可开启追加模式） |
   | **资源管理** | 必须显式调用 `close()` 或 `flush()` 才能将缓冲区数据写入文件 |

2. 🔑核心API
   | 分类 | API | 说明 |
   | :--- | :--- | :--- |
   | **构造器** | `FileWriter(String fileName)` | 创建覆盖写模式的流 |
   | | `FileWriter(String fileName, boolean append)` | `append=true` 开启追加模式 |
   | **常用方法** | `void write(int c)` | 写入单个字符 |
   | | `void write(char[] cbuf)` | 写入字符数组 |
   | | `void write(String str)` | 写入字符串 |
   | | `void flush()` | 刷新缓冲区（强制写入磁盘） |
   | | `void close()` | 关闭流（关闭前会自动刷新） |

3. ✅ 适用场景
   1. **写入纯文本文件**：日志记录、文本导出等。
   2. **便捷写入**：直接写入字符串，无需手动转换为字节。

4. ❌ 不适用场景
   1. **写入二进制文件**：请使用 `FileOutputStream`。
   2. **指定编码写入**：`FileWriter` 默认使用系统编码，若需指定编码（如 UTF-8），请使用 `OutputStreamWriter`。

## 代码示例

### 1. 覆盖写入
演示写入字符、字符数组和字符串。

```java
import java.io.FileWriter;
import java.io.IOException;

public class WriteFile {
    public static void main(String[] args) {
        String path = "assets/a.txt";
        try (FileWriter fw = new FileWriter(path)) {
            // 1. 写入单个字符
            fw.write('A');
            
            // 2. 写入字符数组
            char[] chars = {'H', 'e', 'l', 'l', 'o'};
            fw.write(chars);
            
            // 3. 写入字符串
            fw.write("\nWorld");
            
            // try-with-resources 会自动调用 close()，从而触发 flush()
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
```

### 2. 追加写入
构造函数传入 `true` 开启追加模式。

```java
import java.io.FileWriter;
import java.io.IOException;

public class WriteAppend {
    public static void main(String[] args) {
        String path = "assets/a.txt";
        try (FileWriter fw = new FileWriter(path, true)) { // true 表示追加
            fw.write("\nThis is appended text.");
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
```

### 3. ⚠️ 注意事项：Flush与Close
`FileWriter` 内部有缓冲区，如果不关闭流也不刷新，数据可能丢失。

```java
import java.io.FileWriter;
import java.io.IOException;

public class FlushDemo {
    public static void main(String[] args) {
        String path = "assets/flush_test.txt";
        try {
            FileWriter fw = new FileWriter(path);
            fw.write("Data in buffer");
            
            // fw.flush(); // 手动刷新，数据写入文件，流继续有效
            
            // 如果忘记 close() 且未 flush()，程序结束时数据可能未写入文件
            fw.close(); // 关闭流，先刷新后关闭
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
```
