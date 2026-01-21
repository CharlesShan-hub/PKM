# InputStreamReader

`InputStreamReader` 是 Java I/O 体系中的**转换流**，它是**字节流通向字符流的桥梁**。它读取字节，并使用指定的字符集将其解码为字符。

## 介绍
1. 🏅核心特性
   | 特性 | 说明 |
   | :--- | :--- |
   | **继承关系** | `java.io.Reader` → `java.io.InputStreamReader` |
   | **主要作用** | 将 `InputStream`（字节流）转换为 `Reader`（字符流） |
   | **编码支持** | 支持显式指定字符集（Charset），解决乱码问题的关键 |
   | **设计模式** | **适配器模式（Adapter）**，将字节流接口适配为字符流接口 |

2. 🔑核心API
   | 分类 | API | 说明 |
   | :--- | :--- | :--- |
   | **构造器** | `InputStreamReader(InputStream in)` | 使用默认字符集创建 |
   | | `InputStreamReader(InputStream in, String charsetName)` | 使用指定字符集名称创建（如 "UTF-8"） |
   | | `InputStreamReader(InputStream in, Charset cs)` | 使用指定 Charset 对象创建 |
   | **常用方法** | `int read()` | 读取单个字符 |
   | | `int read(char[] cbuf, int offset, int length)` | 读取字符到数组 |
   | | `String getEncoding()` | 获取当前使用的字符编码名称 |
   | | `void close()` | 关闭流 |

3. ✅ 适用场景
   1. **解决乱码**：读取非 UTF-8 编码的文件（如 GBK 编码的旧文件）。
   2. **流转换**：获取了字节流（如 `System.in`, `Socket.getInputStream()`），但需要按字符处理。

## 代码示例

### 1. 指定编码读取
读取一个 GBK 编码的文件（假设系统默认是 UTF-8），必须指定编码否则会乱码。

```java
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.nio.charset.StandardCharsets;

public class ReadWithEncoding {
    public static void main(String[] args) {
        String path = "assets/gbk_file.txt";
        
        // 显式指定编码为 GBK (或使用 StandardCharsets.UTF_8 等)
        try (InputStreamReader isr = new InputStreamReader(new FileInputStream(path), "GBK")) {
            System.out.println("当前编码: " + isr.getEncoding());
            
            int c;
            while ((c = isr.read()) != -1) {
                System.out.print((char) c);
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
```

### 2. 读取标准输入
将 `System.in`（字节流）转换为字符流，以便按行读取控制台输入。

```java
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class SystemInDemo {
    public static void main(String[] args) throws IOException {
        // System.in 是 InputStream，无法直接 readLine()
        // 需要通过 InputStreamReader 转换为 Reader，再包装为 BufferedReader
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        System.out.print("请输入内容: ");
        String line = br.readLine();
        System.out.println("你输入了: " + line);
    }
}
```

## 💡 提示
* JDK 11+ 的 `FileReader` 已经支持指定编码：`new FileReader("path", StandardCharsets.UTF_8)`，在读取文件场景下可直接替代 `InputStreamReader`。
