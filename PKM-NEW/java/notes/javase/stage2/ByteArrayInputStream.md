# ByteArrayInputStream

`ByteArrayInputStream` 是 Java I/O 体系中**字节输入流（InputStream）**的子类，专门用于从内存中的**字节数组**读取数据。

## 介绍
1. 🏅核心特性

   | 特性 | 说明 |
   | :--- | :--- |
   | **继承关系** | `java.io.InputStream` → `java.io.ByteArrayInputStream` |
   | **数据来源** | 内存中的**字节数组（byte array）** |
   | **资源管理** | `close()` 方法无效（空实现），调用后仍可继续使用，无需关闭 |
   | **线程安全** | 主要是同步的 |

2. 🔑核心API

   | 分类 | API | 说明 |
   | :--- | :--- | :--- |
   | **构造器** | `ByteArrayInputStream(byte[] buf)` | 使用整个数组作为数据源 |
   | | `ByteArrayInputStream(byte[] buf, int offset, int length)` | 使用数组的一部分 |
   | **常用方法** | `int read()` | 读取下一个字节 |
   | | `int read(byte[] b, int off, int len)` | 读取多个字节到目标数组 |
   | | `int available()` | 返回剩余可读字节数 |
   | | `void reset()` | 重置到流的起始位置（支持重复读取） |

3. ✅ 适用场景
   1. **数据回放**：多次读取同一段内存数据（支持 `mark/reset`）。
   2. **测试驱动**：在单元测试中模拟 `InputStream` 输入源，无需依赖真实文件。
   3. **反序列化**：从网络或数据库获取的字节数据中恢复对象（配合 `ObjectInputStream`）。

4. ❌ 不适用场景
   1. **大文件处理**：需将文件全量加载到内存数组才能创建流，消耗大量内存。

5. `ByteArrayInputStream`和`FileInputStream`的区别
	
	| 特性/维度 | **ByteArrayInputStream** | **FileInputStream** |
	|-----------|-------------------------|----------------------|
	| **继承关系** | `ByteArrayInputStream` → `InputStream` | `FileInputStream` → `InputStream` |
	| **数据源** | 内存中的字节数组 | 磁盘上的文件 |
	| **物理位置** | 内存 | 磁盘文件系统 |
	| **性能** | ⚡ **极快**（内存操作，纳米级） | ⏳ **较慢**（I/O操作，毫秒级） |
	| **线程安全** | ❌ 非线程安全 | ✅ 通常是线程安全的 |
	| **可重复读取** | ✅ 支持（通过 `reset()`） | ❌ 不支持（需重新打开） |
	| **标记支持** | ✅ 支持 `mark()`/`reset()` | ❌ 通常不支持 |
	| **资源管理** | 🔄 可关闭但非必需 | 🔐 **必须关闭**（系统资源） |
	| **异常处理** | 较少I/O异常 | 较多I/O异常（文件不存在、权限等） |

## 代码示例

### 1. 基本读取
从内存数组中读取数据。

```java
import java.io.ByteArrayInputStream;

public class BasicRead {
    public static void main(String[] args) {
        byte[] source = "Hello World".getBytes();
        
        // 创建内存输入流
        ByteArrayInputStream bais = new ByteArrayInputStream(source);
        
        int data;
        while ((data = bais.read()) != -1) {
            System.out.print((char) data);
        }
        // close() 无效，无需调用
    }
}
```

### 2. 重复读取 (Mark/Reset)
演示 `ByteArrayInputStream` 支持的重置功能。

```java
import java.io.ByteArrayInputStream;

public class RepeatRead {
    public static void main(String[] args) {
        byte[] source = {10, 20, 30};
        ByteArrayInputStream bais = new ByteArrayInputStream(source);

        // 第一次读取
        System.out.println("First read: " + bais.read()); // 10
        System.out.println("Second read: " + bais.read()); // 20

        // 重置到开头
        bais.reset(); 
        
        // 再次读取
        System.out.println("Read after reset: " + bais.read()); // 10
    }
}
```

### 3. 结合对象流
参见 [ByteArrayOutputStream.md](ByteArrayOutputStream.md) 中的“对象深克隆”示例，`ByteArrayInputStream` 常作为反序列化的输入源。
