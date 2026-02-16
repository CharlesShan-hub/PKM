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
    - `transient`关键字修饰的属性不会参与序列化。  

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

完整案例

```java
package com.powernode.javase.io;  
  
import java.io.FileInputStream;  
import java.io.ObjectInputStream;  
  
/**  
 * 反序列化过程：将文件中的Student字节序列恢复到内存中，变成Student对象。  
 */  
public class ObjectInputStreamTest03 {  
  
    public static void main(String[] args) throws Exception{  
  
        ObjectInputStream ois = new ObjectInputStream(new FileInputStream("student"));  
  
        System.out.println(ois.readObject());  
  
        ois.close();  
    }  
}
```

```java
package com.powernode.javase.io;  
  
import java.io.Serializable;  
import java.io.Serial;  
  
/**  
 * 1. 重点：凡是参与序列化和反序列化的对象必须实现 java.io.Serializable 可序列化的接口。  
 * 2. 这个接口是一个标志接口，没有任何方法。只是起到一个标记的作用。  
 * 3. 它到底是标记什么呢？？？？？？  
 * 4. 当java程序中类实现了Serializable接口，编译器会自动给该类添加一个“序列化版本号”。  
 *      序列化版本号：serialVersionUID  
 * 5. 序列化版本号有什么用？  
 *      在Java语言中是如何区分class版本的？  
 *      首先通过类的名字，然后再通过序列化版本号进行区分的。  
 *      在java语言中，不能仅仅通过一个类的名字来进行类的区分，这样太危险了。  
 * 6. 为了保证序列化的安全，只有同一个class才能进行序列化和反序列化。在java中是如何保证同一个class的？  
 *      类名 + 序列化版本号：serialVersionUID  
 * 
 * java.io.InvalidClassException: com.powernode.javase.io.Student; 
 * local class incompatible: 
 *      stream classdesc serialVersionUID = -4936871645261081394,  （三年前的学生对象，是三年前的Student.class创建的学生对象。）  
 *      local class serialVersionUID = 5009257763737485728  （三年后，Student.class升级了。导致了版本发生了变化。）  
 */  
public class Student implements Serializable {  
  
    // 建议：不是必须的。  
    // 如果你确定这个类确实还是以前的那个类。类本身是合法的。没有问题。  
    // 建议你将序列化版本号写死！  
    @Serial  
    private static final long serialVersionUID = -7005027670916214239L;  
  
    private String name;  
    private transient int age; // transient关键字修饰的属性不会参与序列化。  
  
    private String addr;  
  
    public String getAddr() {  
        return addr;  
    }  
  
    public void setAddr(String addr) {  
        this.addr = addr;  
    }  
  
    @Override  
    public String toString() {  
        return "Student{" +  
                "name='" + name + '\'' +  
                ", age=" + age +  
                '}';  
    }  
  
    public Student() {  
    }  
  
    public Student(String name, int age) {  
        this.name = name;  
        this.age = age;  
    }  
  
    public String getName() {  
        return name;  
    }  
  
    public void setName(String name) {  
        this.name = name;  
    }  
  
    public int getAge() {  
        return age;  
    }  
  
    public void setAge(int age) {  
        this.age = age;  
    }  
}
```