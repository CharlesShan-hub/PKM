# FileOutputStream

`FileOutputStream` 是 Java I/O 体系中**字节输出流（OutputStream）**的子类，专门用于将原始字节数据（8位字节流）写入文件系统。

## 介绍
1. 🏅核心特性

   | 特性 | 说明 |
   | :--- | :--- |
   | **继承关系** | `java.io.OutputStream` → `java.io.FileOutputStream` |
   | **数据单位** | 以**字节（byte）**为单位写入（适合二进制数据） |
   | **写入方式** | 顺序写入（默认覆盖，可开启追加模式） |
   | **资源管理** | 必须显式调用 `close()` 关闭流（推荐 try-with-resources） |

2. 🔑核心API

   | 分类 | API | 说明 |
   | :--- | :--- | :--- |
   | **构造器** | `FileOutputStream(String name)` | 创建覆盖写模式的流（文件不存在则自动创建） |
   | | `FileOutputStream(String name, boolean append)` | `append=true` 开启追加模式 |
   | | `FileOutputStream(File file)` | 通过 File 对象创建 |
   | | `FileOutputStream(File file, boolean append)` | `append=true` 开启追加模式 |
   | **常用方法** | `void write(int b)` | 写入一个字节 |
   | | `void write(byte[] b)` | 写入字节数组 |
   | | `void write(byte[] b, int off, int len)` | 写入字节数组的一部分 |
   | | `void close()` | 关闭流释放资源 |

3. ✅ 适用场景
   1. **写入二进制文件**：保存图片（`.jpg`）、音频（`.mp3`）、视频（`.mp4`）等。
   2. **持久化数据**：将程序中的数据保存到磁盘。
   3. **流链构建**：作为 `BufferedOutputStream`、`ObjectOutputStream` 等装饰流的底层输出流。

4. ❌ 不适用场景
   1. **直接写入文本**：建议用 `FileWriter` 或 `BufferedWriter` 以避免手动处理字符编码。

## 代码示例

### 1. 单字节写入
逐个字节写入，效率较低。

```java
package ex_file;

import java.io.FileOutputStream;
import java.io.IOException;

public class WriteByte {
  public static void main(String[] args) {
    String path = "assets/a.txt";
    try {
      FileOutputStream fos = new FileOutputStream(path);
      fos.write('a'); // 写入字符 'a'
      fos.close();
    } catch (IOException e) {
      e.printStackTrace();
    }
  }
}
```

### 2. 写入字节数组
将字符串转换为字节数组一次性写入，或写入数组的一部分。

```java
package ex_file;

import java.io.FileOutputStream;
import java.io.IOException;

public class WriteString {
  public static void main(String[] args) {
    String path = "assets/a.txt";
    try {
      FileOutputStream fos = new FileOutputStream(path);

      // 1. 写入完整字符串
      String str = "Hello World";
      fos.write(str.getBytes());

      // 2. 写入部分内容 (例如前 5 个字节)
      // fos.write(str.getBytes(), 0, 5);
      
      // 3. 写入一个中文
      // String str2 = "我爱你中国";
      // fos.write(str2.getBytes(), 0, 3); //会写入'我'

      fos.close();
    } catch (IOException e) {
      e.printStackTrace();
    }
  }
}
```



### 3. 追加写入
构造函数第二个参数传入 `true`，即可在文件末尾追加内容。

```java
package ex_file;

import java.io.FileOutputStream;
import java.io.IOException;

public class WriteAppend {
  public static void main(String[] args) {
    String path = "assets/a.txt";
    try {
      // true 表示追加模式
      FileOutputStream fos = new FileOutputStream(path, true);
      fos.write("Append content".getBytes());
      fos.close();
    } catch (IOException e) {
      e.printStackTrace();
    }
  }
}
```

### 4. 文件拷贝案例
使用缓冲区（Buffer）配合 `read(buffer)` 和 `write(buffer, off, len)` 实现高效拷贝。

```java
package ex_file;

import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.IOException;

public class FileCopy {
    public static void main(String[] args) {
        String srcPath = "assets/c.txt";
        String distPath = "assets/d.txt";
        
        // 使用 try-with-resources 自动关闭资源
        try (FileInputStream srcFis = new FileInputStream(srcPath);
             FileOutputStream distFos = new FileOutputStream(distPath)) {  // 默认覆盖
            
            byte[] buffer = new byte[1024]; // 1KB 缓冲区
            int len;
            
            // 边读边写
            while ((len = srcFis.read(buffer)) != -1) {
                // ⚠️ 注意：一定要指定长度 len，否则最后一次可能写入多余的旧数据
                distFos.write(buffer, 0, len);
            }
            
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
```

