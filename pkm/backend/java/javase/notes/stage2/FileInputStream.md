# FileInputStream

`FileInputStream` 是 Java I/O 体系中**字节输入流（InputStream）**的子类，专门用于从文件系统中读取原始字节数据（8位字节流）。

## 介绍
1. 🏅核心特性

    | 特性 | 说明 |
    | :--- | :--- |
    | **继承关系** | `java.io.InputStream` → `java.io.FileInputStream` |
    | **数据单位** | 以**字节（byte）**为单位读取（适合二进制数据） |
    | **读取方式** | 顺序读取（不可随机访问，需用 `RandomAccessFile`） |
    | **资源管理** | 必须显式调用 `close()` 关闭流（推荐 try-with-resources） |


2. 🔑核心API

    | 分类 | API | 说明 |
    | :--- | :--- | :--- |
    | **构造器** | `FileInputStream(String name)` | 通过文件路径创建 |
    | | `FileInputStream(File file)` | 通过 File 对象创建 |
    | **常用方法** | `int read()` | 读取一个字节，返回 -1 表示结束 |
    | | `int read(byte[] b)` | 读取多个字节到数组 |
    | | `void close()` | 关闭流释放资源 |

3. ✅ 适用场景
   1. **读取二进制文件**：图片（`.jpg`）、音频（`.mp3`）、视频（`.mp4`）、压缩包等。
   1. **低层级文本读取**：需手动处理编码（建议配合 `InputStreamReader`）。
   1. **流链构建**：作为 `BufferedInputStream`、`ObjectInputStream` 等装饰流的基础。


4. ❌ 不适用场景
   1. **直接读取文本**：建议用 `FileReader` 避免乱码。
   2. **随机访问**：建议用 `RandomAccessFile`。

## 代码示例

### 1. 单字节读取
逐个字节读取，效率较低，适合演示或极小文件。**如果读中文会乱码**。

```java
import java.io.FileInputStream;
import java.io.IOException;

public class ReadByte {
    public static void main(String[] args) {
        String path = "assets/a.txt";
        try {
            FileInputStream fis = new FileInputStream(path);
            int num;
            // read() 返回 -1 代表结束，否则返回字节的 int 值
            while ((num = fis.read()) != -1) {
                System.out.print((char) num);
            }
            System.out.println();
            fis.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
```

### 2. 一次性读取
将文件内容一次性读入字节数组（慎用于大文件）。性能得到了提升，因为减少了与硬盘和内存交互的次数。

```java
import java.io.File;
import java.io.FileInputStream;
import java.io.IOException;

public class ReadAll {
    public static void main(String[] args) {
        String path = "assets/a.txt";
        try {
            File file = new File(path);
            FileInputStream fis = new FileInputStream(path);
            byte[] content = new byte[(int) file.length()];
            
            fis.read(content); // 返回实际读取字节数
            System.out.println(new String(content));
            
            fis.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
```

### 3. 分批读取（推荐）
使用缓冲区（Buffer）循环读取，兼顾效率与内存。但依然无法避免中文乱码问题，因为会截断汉字字节的可能性。

```java
import java.io.FileInputStream;
import java.io.IOException;

public class ReadBuffer {
    public static void main(String[] args) {
        String path = "assets/a.txt";
        try {
            FileInputStream fis = new FileInputStream(path);
            byte[] buffer = new byte[8]; // 实际开发通常用 1024 或 4096
            int len;
            
            // read(buffer) 返回读取到的字节数，-1 表示结束
            while ((len = fis.read(buffer)) != -1) {
                System.out.print(new String(buffer, 0, len));
            }
            System.out.println();
            fis.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
```

