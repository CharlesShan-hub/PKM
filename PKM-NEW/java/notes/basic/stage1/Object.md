# Object

## equals方法

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

7. .equals()源码(JDK 17)

   ```java
   // Object.java
   public boolean equals(Object obj) {
     return (this == obj);
   }
   // Integer.java
   public boolean equals(Object obj) {
     if (obj instanceof Integer) {
       return value == ((Integer)obj).intValue();
     }
     return false;
   }
   // String.java(jdk17)
   public boolean equals(Object anObject) {
     if (this == anObject) {
       return true;
     }
     return (anObject instanceof String aString)
       && (!COMPACT_STRINGS || this.coder == aString.coder)
       && StringLatin1.equals(value, aString.value);
   }
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
   	}
   	return false;//如果比较的不是字符串，则直接返回 false 
   }
   ```

8. int 比较
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
9. 字符串比较案例

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

10. 重写.equal方法

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

11. 练习

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

12. 练习
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
3. Object的 toString
	```java
	public static String toString(Object o, String nullDefault) {  
	    return (o != null) ? o.toString() : nullDefault;  
	}
	```
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