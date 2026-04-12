# FileReader

`FileReader` 是 Java I/O 体系中**字符输入流（Reader）**的子类，专门用于从文件系统中读取字符数据（文本）。

## 介绍

1. 🏅核心特性

   | 特性 | 说明 |
   | :--- | :--- |
   | **继承关系** | `java.io.Reader` → `java.io.InputStreamReader` → `java.io.FileReader` |
   | **数据单位** | 以**字符（char）**为单位读取（适合文本数据） |
   | **读取方式** | 顺序读取（默认使用系统默认编码，JDK 11+ 可指定编码） |
   | **资源管理** | 必须显式调用 `close()` 关闭流（推荐 try-with-resources） |

2. 🔑核心API

   | 分类 | API | 说明 |
   | :--- | :--- | :--- |
   | **构造器** | `FileReader(String fileName)` | 通过文件路径创建 |
   | | `FileReader(File file)` | 通过 File 对象创建 |
   | **常用方法** | `int read()` | 读取一个字符，返回字符的 int 值（-1 表示结束） |
   | | `int read(char[] cbuf)` | 读取多个字符到数组 |
   | | `void close()` | 关闭流释放资源 |

3. ✅ 适用场景
   1. **读取纯文本文件**：`.txt`, `.java`, `.json`, `.xml` 等。
   2. **字符流处理**：不需要关心底层字节编码转换（使用默认编码）的简单场景。

4. ❌ 不适用场景
   1. **读取二进制文件**：图片、音频、视频等（请使用 `FileInputStream`）。
   2. **复杂编码处理**：如果文件编码与系统默认不一致，建议使用 `InputStreamReader` 显式指定编码。

## 代码示例

### 1. 单字符读取

逐个字符读取，效率较低。

```java
import java.io.FileReader;
import java.io.IOException;

public class ReadChar {
    public static void main(String[] args) {
        String path = "assets/a.txt";
        try (FileReader fr = new FileReader(path)) {
            int ch;
            // read() 返回 -1 代表结束
            while ((ch = fr.read()) != -1) {
                System.out.print((char) ch);
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
```

### 2. 分批读取（推荐）

使用字符数组缓冲区（Buffer）读取，效率更高。

```java
import java.io.FileReader;
import java.io.IOException;

public class ReadBuffer {
    public static void main(String[] args) {
        String path = "assets/a.txt";
        try (FileReader fr = new FileReader(path)) {
            char[] buffer = new char[1024]; // 1KB 字符缓冲区
            int len;
            
            // read(buffer) 返回实际读取的字符数
            while ((len = fr.read(buffer)) != -1) {
                // 将字符数组转为字符串，注意指定有效长度
                System.out.print(new String(buffer, 0, len));
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
```
