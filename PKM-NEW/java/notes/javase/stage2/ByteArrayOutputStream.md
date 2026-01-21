# ByteArrayOutputStream

`ByteArrayOutputStream` 是 Java I/O 体系中**字节输出流（OutputStream）**的子类，专门用于在内存中创建一个可以增长的缓冲区，并将数据写入其中。

## 介绍
1. 🏅核心特性
   | 特性 | 说明 |
   | :--- | :--- |
   | **继承关系** | `java.io.OutputStream` → `java.io.ByteArrayOutputStream` |
   | **数据去向** | 写入内部的**字节数组（byte array）**（自动扩容） |
   | **资源管理** | `close()` 方法无效（空实现），调用后仍可继续使用，无需关闭 |
   | **线程安全** | 部分方法是同步的（synchronized） |

2. 🔑核心API
   | 分类 | API | 说明 |
   | :--- | :--- | :--- |
   | **构造器** | `ByteArrayOutputStream()` | 创建默认大小（32字节）的缓冲区 |
   | | `ByteArrayOutputStream(int size)` | 创建指定初始大小的缓冲区 |
   | **常用方法** | `void write(int b)` | 写入一个字节 |
   | | `void write(byte[] b, int off, int len)` | 写入字节数组的一部分 |
   | | `void writeTo(OutputStream out)` | 将缓冲区内容写入另一个输出流 |
   | | `byte[] toByteArray()` | 获取缓冲区数据的副本（核心方法） |
   | | `String toString()` | 将缓冲区内容转为字符串（使用默认编码） |

3. ✅ 适用场景
   1. **内存缓存**：需要临时存储数据，最后一次性获取。
   2. **数据转换**：将图片、对象序列化结果转为字节数组。
   3. **深克隆**：配合 `ObjectOutputStream` 和 `ByteArrayInputStream` 实现对象深拷贝。

4. ❌ 不适用场景
   1. **海量数据**：数据全在内存中，数据量过大会导致 `OutOfMemoryError`。

## 代码示例

### 1. 基本用法
写入数据并获取字节数组。

```java
import java.io.ByteArrayOutputStream;
import java.io.IOException;

public class BasicUsage {
    public static void main(String[] args) {
        // 创建内存输出流（不需要文件路径）
        ByteArrayOutputStream baos = new ByteArrayOutputStream();

        // 写入数据到内存
        baos.write(97); // 'a'
        baos.write(98); // 'b'
        baos.write(99); // 'c'
        
        try {
            baos.write("Hello".getBytes());
        } catch (IOException e) {
            e.printStackTrace();
        }

        // 获取内存中的数据
        byte[] result = baos.toByteArray();
        System.out.println(new String(result)); // abcHello
        
        // close() 无效，无需调用，但调用也没错
    }
}
```

### 2. 组合使用（对象序列化）
结合 `ObjectOutputStream` 将对象转为字节数组。

```java
import java.io.ByteArrayOutputStream;
import java.io.ObjectOutputStream;
import java.util.Date;

public class ObjectToBytes {
  public static void main(String[] args) throws Exception {
    ByteArrayOutputStream baos = new ByteArrayOutputStream();
    ObjectOutputStream oos = new ObjectOutputStream(baos);

    // 将数据写入 baos 的缓冲区
    oos.writeInt(100);
    oos.writeBoolean(false);
    oos.writeUTF("动力节点");
    oos.writeObject(new Date());

    oos.flush(); // 刷新包装流

    // 获取结果
    byte[] data = baos.toByteArray();
    System.out.println("数据长度: " + data.length);
  }
}
```

### 3. 对象深克隆（Deep Clone）
利用内存流实现对象的深拷贝（完全独立的副本）。

**实体类 (需实现 Serializable，使用 Lombok 简化)**：
```java
import java.io.Serializable;
import lombok.AllArgsConstructor;
import lombok.Data;

@Data
@AllArgsConstructor
class Address implements Serializable {
    private static final long serialVersionUID = 1L;
    private String city;
}

@Data
@AllArgsConstructor
class User implements Serializable {
    private static final long serialVersionUID = 1L;
    private String name;
    private Address addr;
}
```

**克隆测试**：
```java
import java.io.*;

public class DeepCloneTest {
  public static void main(String[] args) throws Exception {
    // 1. 准备源对象
    User srcUser = new User("ZhangSan", new Address("Beijing"));

    // 2. 序列化：Object -> byte[] (写入 ByteArrayOutputStream)
    ByteArrayOutputStream baos = new ByteArrayOutputStream();
    ObjectOutputStream oos = new ObjectOutputStream(baos);
    oos.writeObject(srcUser);
    oos.flush();
    byte[] bytes = baos.toByteArray();

    // 3. 反序列化：byte[] -> Object (从 ByteArrayInputStream 读取)
    ByteArrayInputStream bais = new ByteArrayInputStream(bytes);
    ObjectInputStream ois = new ObjectInputStream(bais);
    User clonedUser = (User) ois.readObject();

    // 4. 验证深拷贝（修改副本不影响原件）
    clonedUser.getAddr().setCity("Nanjing");

    System.out.println("原对象: " + srcUser);      // Beijing
    System.out.println("克隆对象: " + clonedUser); // Nanjing
  }
}
```
