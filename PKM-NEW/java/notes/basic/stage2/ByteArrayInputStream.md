# ByteArrayInputStream

[[ByteArrayOutputStream]]

* ByteArrayInputStream和ByteArrayOutputStream都是内存操作流，不需要打开和关闭文件等操作。这些流是非常常用的，可以将它们看作开发中的常用工具，能够方便地读写字节数组、图像数据等内存中的数据。
* ByteArrayInputStream和ByteArrayOutputStream都是节点流。
* ByteArrayOutputStream，将数据写入到内存中的字节数组当中。
* ByteArrayInputStream，读取内存中某个字节数组中的数据。

```java
package com.powernode.javase.io;  
  
import java.io.ByteArrayOutputStream;  
  
/**  
 * java.io.ByteArrayOutputStream：向内存中的字节数组写数据。  
 */  
public class ByteArrayOutputStreamTest01 {  
    public static void main(String[] args) {  
  
        // ByteArrayOutputStream的基本用法。  
        ByteArrayOutputStream baos = new ByteArrayOutputStream(); //节点流  
  
        // 开始写  
        baos.write(1);  
        baos.write(2);  
        baos.write(3);  
  
        // 怎么获取内存中的哪个byte[]数组呢？  
        byte[] byteArray = baos.toByteArray();  
        for (byte b : byteArray){  
            System.out.println(b);  
        }  
    }  
}
```

根据装饰器原理，我们可以进行自由的组合，多个包装流可以叠加使用

```java
package com.powernode.javase.io;  
  
import java.io.ByteArrayInputStream;  
import java.io.ByteArrayOutputStream;  
import java.io.ObjectInputStream;  
import java.io.ObjectOutputStream;  
import java.util.Date;  
  
/**  
 * 了解了装饰器设计模式之后，我们就知道了，包装流和节点流是可以随意组合的。  
 * ObjectOutputStream（包装流）和ByteArrayOutputStream（节点流）进行组合。  
 */  
public class ByteArrayOutputStreamTest02 {  
    public static void main(String[] args) throws Exception{  
  
        // 节点流  
        ByteArrayOutputStream baos = new ByteArrayOutputStream();  
        // 包装流  
        ObjectOutputStream oos = new ObjectOutputStream(baos);  
  
        // 开始写  
        oos.writeInt(100);  
        oos.writeBoolean(false);  
        oos.writeDouble(3.14);  
        oos.writeUTF("动力节点");  
        oos.writeObject(new Date());  
  
        // 使用了包装流就需要手动刷新一下。  
        oos.flush();  
  
        // 获取内存中的大byte数组  
        byte[] byteArray = baos.toByteArray();  
        /*for(byte b : byteArray){  
            System.out.println(b);        }*/  
        // 使用ByteArrayInputStream将上面这个byte数组恢复。  
        // 读的过程，读内存中的大byte数组。  
        // 节点流  
        ByteArrayInputStream bais = new ByteArrayInputStream(byteArray);  
        // 包装流  
        ObjectInputStream ois = new ObjectInputStream(bais);  
  
        // 开始读  
        System.out.println(ois.readInt());  
        System.out.println(ois.readBoolean());  
        System.out.println(ois.readDouble());  
        System.out.println(ois.readUTF());  
        System.out.println(ois.readObject());  
    }  
}
```

可以使用ByteArrayOutputStream进行对象的深克隆

```java
package com.powernode.javase.io.clone;  
  
import java.io.Serial;  
import java.io.Serializable;  
  
public class User implements Serializable {  
  
    @Serial  
    private static final long serialVersionUID = -4947432823777553977L;  
  
    private String name;  
    private int age;  
    private Address addr;  
  
    public User() {  
    }  
  
    public User(String name, int age, Address addr) {  
        this.name = name;  
        this.age = age;  
        this.addr = addr;  
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
  
    public Address getAddr() {  
        return addr;  
    }  
  
    public void setAddr(Address addr) {  
        this.addr = addr;  
    }  
  
    @Override  
    public String toString() {  
        return "User{" +  
                "name='" + name + '\'' +  
                ", age=" + age +  
                ", addr=" + addr +  
                '}';  
    }  
}
```

```java
package com.powernode.javase.io.clone;  
  
import java.io.Serial;  
import java.io.Serializable;  
  
public class Address implements Serializable {  
  
    @Serial  
    private static final long serialVersionUID = -4947432823777553978L;  
  
    private String city;  
    private String street;  
  
    public Address() {  
    }  
  
    public Address(String city, String street) {  
        this.city = city;  
        this.street = street;  
    }  
  
    public String getCity() {  
        return city;  
    }  
  
    public void setCity(String city) {  
        this.city = city;  
    }  
  
    public String getStreet() {  
        return street;  
    }  
  
    public void setStreet(String street) {  
        this.street = street;  
    }  
  
    @Override  
    public String toString() {  
        return "Address{" +  
                "city='" + city + '\'' +  
                ", street='" + street + '\'' +  
                '}';  
    }  
}
```

```java
package com.powernode.javase.io.clone;  
  
import java.io.ByteArrayInputStream;  
import java.io.ByteArrayOutputStream;  
import java.io.ObjectInputStream;  
import java.io.ObjectOutputStream;  
  
/**  
 * 使用ByteArrayOutputStream和ByteArrayInputStream直接复制的对象就是一个深克隆。  
 */  
public class DeepCloneTest {  
    public static void main(String[] args) throws Exception{  
        // 准备对象  
        Address addr = new Address("北京", "朝阳");  
        User user = new User("zhangsan", 20, addr);  
  
        // 将Java对象写到一个byte数组中。  
        ByteArrayOutputStream baos = new ByteArrayOutputStream();  
        ObjectOutputStream oos = new ObjectOutputStream(baos);  
  
        oos.writeObject(user);  
  
        oos.flush();  
  
        // 从byte数组中读取数据恢复java对象  
        ByteArrayInputStream bais = new ByteArrayInputStream(baos.toByteArray());  
        ObjectInputStream ois = new ObjectInputStream(bais);  
  
        // 这就是哪个经过深拷贝之后的新对象  
        User user2 = (User) ois.readObject();  
  
        user2.getAddr().setCity("南京");  
  
        System.out.println(user);  
        System.out.println(user2);  
    }  
}
```

目前深拷贝的方案

* 调用Object的clone方法，默认是浅克隆，需要深克隆的话，就需要重写clone方法。
* 可以通过序列化和反序列化完成对象的克隆。
* 也可以通过ByteArrayInputStream和ByteArrayOutputStream完成深克隆。
