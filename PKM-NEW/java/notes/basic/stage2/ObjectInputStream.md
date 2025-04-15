# ObjectInputStream

👉 接[[ObjectOutputStream]]

• ObjectInputStream是Java对象反序列化的输入流，用于从字节流读取对象
• 继承体系：
    • java.lang.Object
    • java.io.InputStream
    • java.io.ObjectInputStream
• 主要特点：
    - 实现对象的反序列化(Deserialization)
    - 可以读取基本数据类型和对象
    - 必须与写入时的ObjectOutputStream配对使用

• 常用构造方法：
    - `ObjectInputStream(InputStream in)`：创建从指定输入流读取的ObjectInputStream

• 常用方法：
    - `readObject()`：读取一个对象
    - `readInt()`：读取一个int值
    - `readUTF()`：读取UTF-8格式字符串
    - `close()`：关闭流

• 示例代码：读取之前序列化的Person对象
```java
import java.io.*;

public class ObjectInputExample {
    public static void main(String[] args) {
        String filePath = "/Users/kimshan/Public/project/javanote/out/production/javanote/assets/object.dat";
        
        try (ObjectInputStream ois = new ObjectInputStream(
                new FileInputStream(filePath))) {
            
            // 读取基本数据类型
            int number = ois.readInt();
            String text = ois.readUTF();
            
            // 读取Person对象
            Person person = (Person) ois.readObject();
            
            System.out.println("Number: " + number);
            System.out.println("Text: " + text);
            System.out.println("Person: " + person.name + ", " + person.age);
            
        } catch (IOException | ClassNotFoundException e) {
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