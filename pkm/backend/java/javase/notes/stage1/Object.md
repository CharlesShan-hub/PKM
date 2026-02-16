# Object

---
## equals方法

### equals方法和==

1. 使用方法：`==`，比较运算符
2. 既可以判断基本类型，也可以判断引用类型
3. 判断基本类型的时候判断的是值是否相等
4. 判断引用类型的时候判断的是地址是否相等

5. 案例1

   ```java
   class A{}
   ```

   ```java
   // main
   A a = new A();
   A b = a;
   A c = b;
   System.out.println(a==c); // true
   ```

6. 案例2

   ```java
   class B extends A{}
   class A{}
   ```

   ```java
   // main
   B b = new B();
   A a = b;
   System.out.println(a==b); // true
   ```

### 一些类的equals源码
1. .equals()源码(JDK 17)

   ```java
   // Object.java
   public boolean equals(Object obj) {
     return (this == obj);
   }
	```
	
	```java
   // Integer.java
   public boolean equals(Object obj) {
     if (obj instanceof Integer) {
       return value == ((Integer)obj).intValue();
     }
     return false;
   }
	```
	
	```java
   // String.java(jdk17)
   public boolean equals(Object anObject) {
     if (this == anObject) {
       return true;
     }
     return (anObject instanceof String aString)
       && (!COMPACT_STRINGS || this.coder == aString.coder)
       && StringLatin1.equals(value, aString.value);
   }
	```
	
	```java
   // String.java(jdk8)
   public boolean equals(Object anObject) {
     if (this == anObject) {//如果是同一个对象
       return true;//返回 true 
     }
     if (anObject instanceof String) {//判断类型
       String anotherString = (String)anObject;//向下转型 int n = value.length;
       if (n == anotherString.value.length) {//如果长度相同
         char v1[] = value;
         char v2[] = anotherString.value;
         int i = 0;
         while (n-- != 0) {//然后一个一个的比较字符
           if (v1[i] != v2[i]) return false;
           i++; 
         }
         return true;//如果两个字符串的所有字符都相等，则返回 true
   	}
   	return false;//如果比较的不是字符串，则直接返回 false 
   }
   ```

2. int 比较
	```java
	Integer i1 = new Integer(1000);
	Integer i2 = new Integer(1000);
	System.out.println(i1 == i2);
	System.out.println(i1.equals(i2));
	```

	```bash
	false
	true
	```
3. 字符串比较案例

   ```java
   String str1 = new String("abc");
   String str2 = new String("abc");
   System.out.println(str1 == str2);
   System.out.println(str1.equals(str2));
   ```

	```bash
	false
	true
	```

4. 重写.equal方法

	```java
	class Person{
	 private String name; 
	 private int age; 
	 private char gender;
	 
	//重写 Object 的 equals 方法 
	 @Override
	 public boolean equals(Object obj) {
	   //判断如果比较的两个对象是同一个对象，则直接返回 true 
	   if(this == obj) {
		 return true; 
	   }
	   //类型判断
	   if(obj instanceof Person) {//是 Person，我们才比较
		 Person p = (Person)obj;
		 return this.name.equals(p.name) && this.age == p.age && this.gender == p.gender;
	   }
	   //如果不是 Person ，则直接返回 false 
	   return false;
	}
	 
	 public Person(String name, int age, char gender) { 
	   this.name = name;
	   this.age = age;
	   this.gender = gender; 
	 }
	 public String getName() {return name;}
	 public void setName(String name) {this.name = name;}
	 public int getAge() {return age;}
	 public void setAge(int age) { this.age = age;}
	 public char getGender() {return gender;}
	 public void setGender(char gender) {this.gender = gender;} 
	}
	```

### 自己重写equals
1. 练习

    ```java
    Person p1 = new Person(); 
    p1.name = "A";
    Person p2 = new Person(); 
    p2.name = "A";
    System.out.println(p1==p2);
    System.out.println(p1.name.equals(p2.name));
    System.out.println(p1.equals(p2));
    String s1 = new String("asdf");
    String s2 = new String("asdf"); 
    System.out.println(s1.equals(s2));
    System.out.println(s1==s2);
    ```

    ```java
    Person p1 = new Person(); 
    p1.name = "A";
    Person p2 = new Person(); 
    p2.name = "A";
    System.out.println(p1==p2); //False 
    System.out.println(p1.name.equals(p2.name));//True
    System.out.println(p1.equals(p2));//False,Person类重写后是True
    String s1 = new String("asdf");
    String s2 = new String("asdf"); 
    System.out.println(s1.equals(s2));//T 
    System.out.println(s1==s2); //F
    ```

2. 练习
	```java
	//代码如下 EqualsExercise03.java
	int it = 65;
	float fl = 65.0f;
	System.out.println("65和65.0f是否相等？ " + (it == fl));
	char ch1 = 'A'; char ch2 = 12;
	System.out.println("65和 'A' 是否相等？ " + (it == ch1));
	System.out.println("12和ch2是否相等？ " + (12 == ch2));
	
	String str1 = new String("hello");
	String str2 = new String("hello");
	System.out.println("str1和str2是否相等？ " + (str1 == str2));
	
	System.out.println("str1是否equals str2? " + (str1.equals(str2)));
	System.out.println("hello" == new java.sql.Date());
	```

	```java
	//代码如下 EqualsExercise03.java
	int it = 65;
	float fl = 65.0f;
	System.out.println("65和65.0f是否相等？ " + (it == fl)); // true
	char ch1 = 'A'; char ch2 = 12;
	System.out.println("65和 'A' 是否相等？ " + (it == ch1)); // true
	System.out.println("12和ch2是否相等？ " + (12 == ch2)); // true
	
	String str1 = new String("hello");
	String str2 = new String("hello");
	System.out.println("str1和str2是否相等？ " + (str1 == str2)); // false
	
	System.out.println("str1是否equals str2? " + (str1.equals(str2))); // true
	System.out.println("hello" == new java.sql.Date()); // false
	```

### (面试题)为什么重写 equals 时必须重写 hashCode ⽅法？

因为基于哈希的集合类（如 HashMap）需要基于这⼀点来正确存储和查找对象。

具体地说，HashMap 通过对象的哈希码将其存储在不同的“桶”中，当查找对象时，它需要使⽤ key 的哈希码来确定对象在哪个桶中，然后再通过 equals() ⽅法找到对应的对象。

如果重写了 equals() ⽅法⽽没有重写 hashCode() ⽅法，那么被认为相等的对象可能会有不同的哈希码，从⽽导致⽆法在 HashMap 中正确处理这些对象。

具体内容参考[集合](../stage2/集合.md)中的hashmap部分

---
## Hashcode方法

1. 提高具有哈希结构的容器的效率!（比如 HashMap，HashSet 等等）
2. 两个引用，如果指向的是同一个对象，则哈希值肯定是一样的!
3. 两个引用，如果指向的是不同对象，则哈希值是不一样的（除非发生哈希碰撞）
4. 哈希值主要根据地址号来的，不能完全将哈希值等价于地址。
5. 集合中hashCode如果需要的话，也会重写,在讲解集合时，老韩在说如何重写hashCode() 代码

```java
public class Program {
  public static void main(String[] args) {
    AA aa = new AA();
    AA aa2 = new AA();
    AA aa3 = aa;
    System.out.println("aa.hashCode()=" + aa.hashCode());
    System.out.println("aa2.hashCode()=" + aa2.hashCode());
    System.out.println("aa3.hashCode()=" + aa3.hashCode()); // aa3 和 aa 的一样
  } 
}
class AA {}
```

```
aa.hashCode()=112810359
aa2.hashCode()=205029188
aa3.hashCode()=112810359
```

---
## toString方法

1. 默认返回:**全类名**+@+哈希值的十六进制（**全类名 = 包名+类名**）
	```java
	package ex_objects;  
	  
	public class Test {  
	    public static void main(String[] args){  
	        Cat c = new Cat();  
	        Dog d = new Dog();  
	        System.out.println(c.toString());  
	        System.out.println(c); // 等价于
	        // ex_objects.Cat@3feba861  
	        System.out.println(d.toString()); 
	        System.out.println(d);  // 等价于
	        // I'm not a people, but you are a true dog!  
	    }  
	}  
	  
	class Cat{}  
	class Dog{  
	    @Override  
	    public String toString(){  
	        return "I'm not a people, but you are a true dog!";  
	    }
	}
	```
2. 子类往往重写 toString 方法，用于返回对象的属性信息
	```java
	class Person{
	  String name;
	  public Person(String name){
	    this.name = name;
	  }
	  @Override
	  public String toString(){
	    return "name="+name;
	  }
	}
	```
3. Object 的 toString
	```java
	public String toString() {  
	    return getClass().getName() + "@" + Integer.toHexString(hashCode());  
	}
	```

---
## finalize方法

当垃圾回收器确定不存在该对象的更多引用时，由对象的垃圾回收器调用此方法

```java
class People{
  protected void finalize() throws Throwable{
    System.out.println("删掉了");
  }
}
public class Program{
  public static void main(String[] args){
    // main
    People p = new People();
    p = null;
  }
}
```

> 什么都不输出

垃圾回收机制的调用，是由系统来决定(即有自己的GC算法),也可以通过`System.gc()`主动触发垃圾回收机制

```java
class People{
  protected void finalize() throws Throwable{
    System.out.println("删掉了");
  }
}
public class Program{
  public static void main(String[] args){
    // main
    People p = new People();
    p = null;
    System.gc();
  }
}
```

> 删掉了

但注意，这个方法 java9 开始就不能用了。

---
## clone 方法

在 Java 中，对象克隆是通过实现 `Cloneable` 接口并重写 `Object.clone()` 方法来实现的。下面我将通过一个完整的案例来展示深浅克隆的实现方式。（下面内容是 AI 生成）

### 1. 浅克隆（Shallow Clone）示例

浅克隆只复制对象本身和其基本类型字段，引用类型的字段仍指向原对象的引用。

```java
class Person implements Cloneable {
    private String name;
    private int age;
    private Address address; // 引用类型字段

    // 构造方法、getter/setter 省略...

    @Override
    public Object clone() throws CloneNotSupportedException {
        return super.clone(); // 调用Object的clone()方法
    }
}

class Address {
    private String city;
    private String street;
    // 构造方法、getter/setter 省略...
}

public class ShallowCloneDemo {
    public static void main(String[] args) throws CloneNotSupportedException {
        Address address = new Address("北京", "长安街");
        Person original = new Person("张三", 25, address);
        
        // 浅克隆
        Person cloned = (Person) original.clone();
        
        System.out.println("原始对象: " + original.getName() + ", " + original.getAddress().getCity());
        System.out.println("克隆对象: " + cloned.getName() + ", " + cloned.getAddress().getCity());
        
        // 修改克隆对象的引用类型字段
        cloned.getAddress().setCity("上海");
        
        System.out.println("修改后原始对象地址: " + original.getAddress().getCity()); // 输出"上海"
        System.out.println("修改后克隆对象地址: " + cloned.getAddress().getCity());   // 输出"上海"
    }
}
```

​**​输出结果​**​：

```
原始对象: 张三, 北京
克隆对象: 张三, 北京
修改后原始对象地址: 上海
修改后克隆对象地址: 上海
```

### 2. 深克隆（Deep Clone）示例

深克隆会复制对象及其所有引用类型字段指向的对象。

👉：[面试题：创建对象有哪⼏种⽅式](../mianshi/new-class.md)

#### 实现方式一：递归调用clone()

```java
class Person implements Cloneable {
    private String name;
    private int age;
    private Address address;

    // 构造方法、getter/setter 省略...

    @Override
    public Object clone() throws CloneNotSupportedException {
        Person cloned = (Person) super.clone();
        cloned.address = (Address) address.clone(); // 克隆引用类型字段
        return cloned;
    }
}

class Address implements Cloneable {
    private String city;
    private String street;
    
    // 构造方法、getter/setter 省略...
    
    @Override
    public Object clone() throws CloneNotSupportedException {
        return super.clone();
    }
}

public class DeepCloneDemo {
    public static void main(String[] args) throws CloneNotSupportedException {
        Address address = new Address("北京", "长安街");
        Person original = new Person("张三", 25, address);
        
        // 深克隆
        Person cloned = (Person) original.clone();
        
        System.out.println("原始对象: " + original.getName() + ", " + original.getAddress().getCity());
        System.out.println("克隆对象: " + cloned.getName() + ", " + cloned.getAddress().getCity());
        
        // 修改克隆对象的引用类型字段
        cloned.getAddress().setCity("上海");
        
        System.out.println("修改后原始对象地址: " + original.getAddress().getCity()); // 仍为"北京"
        System.out.println("修改后克隆对象地址: " + cloned.getAddress().getCity());   // 输出"上海"
    }
}
```

#### 实现方式二：通过序列化实现深克隆

```java
import java.io.*;

class Address implements Serializable {
    private static final long serialVersionUID = 1L;
    String city;
    
    public Address(String city) {
        this.city = city;
    }
}

class Person implements Serializable {
    private static final long serialVersionUID = 1L;
    String name;
    int age;
    Address address;
    
    public Person(String name, int age, Address address) {
        this.name = name;
        this.age = age;
        this.address = address;
    }
    
    public Person deepClone() throws IOException, ClassNotFoundException {
        try (ByteArrayOutputStream bos = new ByteArrayOutputStream();
             ObjectOutputStream oos = new ObjectOutputStream(bos)) {
            
            oos.writeObject(this);
            
            try (ByteArrayInputStream bis = new ByteArrayInputStream(bos.toByteArray());
                 ObjectInputStream ois = new ObjectInputStream(bis)) {
                
                return (Person) ois.readObject();
            }
        }
    }
}

public class Main {
    public static void main(String[] args) throws IOException, ClassNotFoundException {
        Address address = new Address("河南省洛阳市");
        Person person1 = new Person("沉默王二", 18, address);
        Person person2 = person1.deepClone();
        
        System.out.println(person1.address == person2.address); // false
    }
}
```

### 3. 克隆最佳实践

1. ​**​实现Cloneable接口​**​：虽然不实现也能编译通过，但运行时调用clone()会抛出CloneNotSupportedException
2. ​**​重写clone()方法​**​：将访问修饰符从protected改为public
3. ​**​深克隆选择​**​：
    - 简单对象结构：递归调用clone()
    - 复杂对象结构：序列化方式
    - 考虑使用第三方库如Apache Commons Lang的SerializationUtils
4. ​**​替代方案​**​：考虑使用拷贝构造器或静态工厂方法
    
```java
// 拷贝构造器示例
public Person(Person original) {
    this.name = original.name;
    this.age = original.age;
    this.address = new Address(original.address); // Address也需要有拷贝构造器
}
```

克隆是创建对象副本的一种方式，但需要谨慎使用，特别是在涉及复杂对象图时。在大多数情况下，拷贝构造器或工厂方法可能是更清晰和安全的选择。