# DataInputStream

`DataInputStream` 是 Java I/O 体系中的**数据输入流**，它允许应用程序以与机器无关的方式从底层输入流中读取基本的 Java 数据类型。

## 介绍
1. 🏅核心特性

   | 特性 | 说明 |
   | :--- | :--- |
   | **继承关系** | `java.io.InputStream` → `java.io.FilterInputStream` → `java.io.DataInputStream` |
   | **主要作用** | 读取 `DataOutputStream` 写入的二进制数据 |
   | **数据恢复** | 能将二进制流准确还原为 int, double, boolean 等 Java 类型 |
   | **强顺序性** | **读取顺序必须与写入顺序严格一致**，否则会读取到错误数据 |

2. 🔑核心API

   | 分类 | API | 说明 |
   | :--- | :--- | :--- |
   | **构造器** | `DataInputStream(InputStream in)` | 包装一个字节输入流 |
   | **常用方法** | `int readInt()` | 读取 int 值 |
   | | `double readDouble()` | 读取 double 值 |
   | | `boolean readBoolean()` | 读取 boolean 值 |
   | | `String readUTF()` | 读取 UTF-8 编码的字符串 |

3. ✅ 适用场景
   1. **读取数据文件**：解析由 `DataOutputStream` 生成的二进制数据文件。
   2. **网络通信**：解析网络协议包中的字段。

## 代码示例

### 1. 读取基本数据类型
```java
package com.powernode.javase.io;  
  
import java.io.DataInputStream;  
import java.io.FileInputStream;  
  
/**  
 * java.io.DataInputStream：数据流（数据字节输入流）  
 * 作用：专门用来读取使用DataOutputStream流写入的文件。  
 * 注意：读取的顺序要和写入的顺序一致。（要不然无法恢复原样。）  
 */  
public class DataInputStreamTest {  
    public static void main(String[] args) throws Exception{  
        // 创建数据字节输入流对象  
        DataInputStream dis = new DataInputStream(new FileInputStream("data"));  
  
        //System.out.println(dis.readBoolean());  
  
        // 开始读  
        byte b = dis.readByte();  
        short s = dis.readShort();  
        int i = dis.readInt();  
        long l = dis.readLong();  
        float f = dis.readFloat();  
        double d = dis.readDouble();  
        boolean flag = dis.readBoolean();  
        char c = dis.readChar();  
        String str = dis.readUTF();  
  
        System.out.println(b);  
        System.out.println(s);  
        System.out.println(i);  
        System.out.println(l);  
        System.out.println(f);  
        System.out.println(d);  
        System.out.println(flag);  
        System.out.println(c);  
        System.out.println(str);  
  
        // 关闭流  
        dis.close();  
  
        /*
        FileInputStream fis = new FileInputStream("data");  
  
        System.out.println(fis.read());        
        System.out.println(fis.read());        
        System.out.println(fis.read());        
        System.out.println(fis.read());  
        fis.close();
        */  
  
    }  
}
```

参考 [DataOutputStream](DataOutputStream.md)
