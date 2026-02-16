# DataOutputStream

`DataOutputStream` 是 Java I/O 体系中的**数据输出流**，它允许应用程序以与机器无关的方式将 Java 基本数据类型写入输出流。

## 介绍
1. 🏅核心特性

   | 特性 | 说明 |
   | :--- | :--- |
   | **继承关系** | `java.io.OutputStream` → `java.io.FilterOutputStream` → `java.io.DataOutputStream` |
   | **主要作用** | 将 Java 基本数据类型（int, double 等）写入文件 |
   | **二进制格式** | 写入的数据是二进制格式，不是文本，无法直接用文本编辑器查看 |
   | **效率** | 写入过程无需进行字符编码转换，效率较高 |

2. 🔑核心API

   | 分类 | API | 说明 |
   | :--- | :--- | :--- |
   | **构造器** | `DataOutputStream(OutputStream out)` | 包装一个字节输出流 |
   | **常用方法** | `void writeInt(int v)` | 写入 int 值（4字节） |
   | | `void writeDouble(double v)` | 写入 double 值（8字节） |
   | | `void writeBoolean(boolean v)` | 写入 boolean 值（1字节） |
   | | `void writeUTF(String str)` | 写入 UTF-8 编码的字符串 |
   | | `void flush()` | 刷新缓冲区 |

3. ✅ 适用场景
   1. **数据持久化**：需要保存程序中的变量值，以便后续读取。
   2. **网络传输**：在网络协议中发送结构化的二进制数据。

4. ⚠️ 注意事项
   * 写入的数据只能由 `DataInputStream` 读取，且**读取顺序必须与写入顺序完全一致**。

## 代码示例

### 1. 写入基本数据类型
```java
package com.powernode.javase.io;  
  
import java.io.DataOutputStream;  
import java.io.FileOutputStream;  
  
/**  
 * java.io.DataOutputStream：数据流（数据字节输出流）  
 * 作用：将java程序中的数据直接写入到文件，写到文件中就是二进制。  
 * DataOutputStream写的效率很高，原因是：写的过程不需要转码。  
 * DataOutputStream写到文件中的数据，只能由DataInputStream来读取。
 */
public class DataOutputStreamTest {  
    public static void main(String[] args) throws Exception{  
        // 节点流  
        //OutputStream os = new FileOutputStream("data");  
        // 包装流  
        //DataOutputStream dos = new DataOutputStream(os);  
  
        DataOutputStream dos = new DataOutputStream(new FileOutputStream("data"));  
  
        // 准备数据  
        byte b = -127;  
        short s = 32767;  
        int i = 2147483647;  
        long l = 1111111111L;  
        float f = 3.0F;  
        double d = 3.14;  
        boolean flag = false;  
        char c = '国';  
        String str = "动力节点";  
  
        // 开始写  
        dos.writeByte(b);  
        dos.writeShort(s);  
        dos.writeInt(i);  
        dos.writeLong(l);  
        dos.writeFloat(f);  
        dos.writeDouble(d);  
        dos.writeBoolean(flag);  
        dos.writeChar(c);  
        dos.writeUTF(str);  
  
        dos.flush();  
        dos.close();  
    }  
}
```

参考 [DataInputStream](DataInputStream.md)
