# OutputStreamWriter

`OutputStreamWriter` 是 Java I/O 体系中的**转换流**，它是**字符流通向字节流的桥梁**。它接收字符，并使用指定的字符集将其编码为字节写入到底层输出流中。

## 介绍
1. 🏅核心特性
   | 特性 | 说明 |
   | :--- | :--- |
   | **继承关系** | `java.io.Writer` → `java.io.OutputStreamWriter` |
   | **主要作用** | 将 `Writer`（字符流）转换为 `OutputStream`（字节流） |
   | **编码支持** | 支持显式指定字符集，控制写入文件的编码格式 |
   | **设计模式** | **适配器模式（Adapter）** |

2. 🔑核心API
   | 分类 | API | 说明 |
   | :--- | :--- | :--- |
   | **构造器** | `OutputStreamWriter(OutputStream out)` | 使用默认字符集创建 |
   | | `OutputStreamWriter(OutputStream out, String charsetName)` | 使用指定字符集名称创建 |
   | | `OutputStreamWriter(OutputStream out, Charset cs)` | 使用指定 Charset 对象创建 |
   | **常用方法** | `void write(String str)` | 写入字符串 |
   | | `void write(char[] cbuf)` | 写入字符数组 |
   | | `String getEncoding()` | 获取当前使用的字符编码名称 |
   | | `void flush()` | 刷新缓冲区（转换流有内部缓冲） |
   | | `void close()` | 关闭流 |

3. ✅ 适用场景
   1. **指定编码写入**：强制以特定编码（如 UTF-8, GBK）保存文件。
   2. **流转换**：将字符数据写入到字节流中（如 `System.out`, `Socket.getOutputStream()`）。

## 代码示例

### 1. 指定编码写入
将字符串以 UTF-8 编码写入文件。

```java
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.OutputStreamWriter;
import java.nio.charset.StandardCharsets;

public class WriteWithEncoding {
    public static void main(String[] args) {
        String path = "assets/utf8_file.txt";
        
        // 指定使用 UTF-8 编码写入
        try (OutputStreamWriter osw = new OutputStreamWriter(new FileOutputStream(path), StandardCharsets.UTF_8)) {
            System.out.println("写入编码: " + osw.getEncoding());
            
            osw.write("Hello, 世界!");
            osw.write("\n这是一个测试。");
            
            // 转换流内部有缓冲区，建议手动 flush 或依赖 try-with-resources 自动 close
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
```

### 2. 写入标准输出
将字符直接写入控制台（`System.out` 是字节流）。

```java
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.OutputStreamWriter;

public class SystemOutDemo {
    public static void main(String[] args) throws IOException {
        // 获取标准输出流的字符包装器
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        
        bw.write("Hello from OutputStreamWriter!");
        bw.newLine();
        
        // 必须刷新，否则无法显示在控制台
        bw.flush();
    }
}
```

## 💡 提示
* JDK 11+ 的 `FileWriter` 已经支持指定编码：`new FileWriter("path", StandardCharsets.UTF_8)`，在写入文件场景下可直接替代 `OutputStreamWriter`。
