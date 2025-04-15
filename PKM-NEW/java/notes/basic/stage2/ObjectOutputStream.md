# ObjectOutputStream

* ObjectOutputStream是Java对象序列化的输出流，用于将对象写入字节流

* 继承体系：
    * java.lang.Object
    * java.io.OutputStream
    * java.io.ObjectOutputStream

* 主要特点：
    * **实现对象的序列化(Serialization)**【常用】
    * 也可以实现Enternalizable接口（不常用）
    * 可以写入基本数据类型和对象
    * 通常与ObjectInputStream配合使用

* 常用构造方法：
    * `ObjectOutputStream(OutputStream out)`：创建写入指定输出流的ObjectOutputStream

* 常用方法：
    * `writeObject(Object obj)`：写入一个对象
    * `writeInt(int val)`：写入一个int值
    * `writeUTF(String str)`：写入UTF-8格式字符串
    * `flush()`：刷新缓冲区
    * `close()`：关闭流

* 示例代码：

```java
import java.io.*;

public class ObjectOutputExample {
    public static void main(String[] args) {
        String filePath = "/Users/kimshan/Public/project/javanote/out/production/javanote/assets/object.dat";
        
        try (ObjectOutputStream oos = new ObjectOutputStream(
                new FileOutputStream(filePath))) {
            
            // 写入基本数据类型
            oos.writeInt(123);
            oos.writeUTF("Hello World");
            
            // 写入自定义对象
            Person person = new Person("张三", 25);
            oos.writeObject(person);
            
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}

// 需要实现Serializable接口才能被序列化
class Person implements Serializable {
    public String name;
    public int age;
    
    public Person(String name, int age) {
        this.name = name;
        this.age = age;
    }
}
```

👉 [[ObjectInputStream]]