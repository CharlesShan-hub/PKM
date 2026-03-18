# static

---

## 类变量（静态变量）

有一个游乐场，有很多小孩，不停的有小孩进来，求小孩个数。

没有类变量的版本（bad example）

```java
public class Test{
    public static void main(String[] args){
        int count = 0;
        Child c1 = new Child("A");
        count++;
        Child c2 = new Child("B");
        count++;
        Child c3 = new Child("C");
        count++;
        System.out.println(count); // 3
    }
}
class Child{
    private String name;
    public Child(String name){
        this.name = name;
        join();
    }
    public void join(){
        System.out.println(name + "加入了游戏");
    }
} 
```

有类变量的版本：**不同的对象的变量共享一个数据空间**，static 修饰

```java
public class Test{
    public static void main(String[] args){
        Child c1 = new Child("A");
        Child c2 = new Child("B");
        Child c3 = new Child("C");
        System.out.println(Child.count); // 3, 类变量可以用类名直接访问
        System.out.println(c1.count);    // 3, 不同的对象共享同一个空间
    }
}
class Child{
    private String name;
    public static int count = 0; // 类变量(静态变量)
    public Child(String name){
        this.name = name;
        join();
        count++; // 这里修改的是类变量
    }
    public void join(){
        System.out.println(name + "加入了游戏");
    }
} 
```

内存布局

总的来讲，所有对象共享静态变量，静态变量在类加载的时候就生成了

```json
{
    'stack':{
        c1_pointer,c2_pointer,c3_pointer,
    },
    'heap':{
        c1_content,c2_content,c3_content,
        count(有的 jdk 版本静态变量在这里)
    },
    'constant pool':{
        '静态域':{
            count(有的 jdk 版本静态变量在这里)
        }
    }
}
```

实例变量不能通过类名.方法名访问，只有静态变量可以

类变量的生命周期随着类的加载开始，随着类的消亡结束

---

## 类方法（静态方法）

类方法（静态方法）：也是 static 修饰，注意 **里边不能用 this 和 super**，静态方法只能访问静态成员

非静态成员，既可以访问静态成员也可以访问非静态成员

类方法常用于工具类，比如 Math.sprt()

```java
class People{  
    public int n1;  
    public static int n2;  
    public void m1(){}  
    public static void m2(){}  
  
    public static void method1(){  
        // System.out.println(n1);  
        System.out.println(n2);  
        // m1();  
        // this.m1();
        m2();
        People.m2();  
    }    
    public void method2(){  
        System.out.println(n1);  
        System.out.println(n2);  
        m1();  
        m2();  
    }
}
```

练习1

```java
// 题1(评讲), 输出什么?
public class Test {
    static int count = 9;
    public void count() {
        System.out.println("count=" + (count++));
    }
    public static void main(String args[]) {
        new Test().count();
        new Test().count();
        System.out.println(Test.count)
    }
}
```

```java
public class Test {
    static int count = 9;
    public void count() {
        System.out.println("count=" + (count++));
    }
    public static void main(String args[]) {
        new Test().count();
        // count=9
        new Test().count();
        // count=10
        System.out.println(Test.count)
        // 11
    }
}
```

练习 2

```java
//题2(评讲)，看看下面代码有没有错误，如果有错误，就修改，看看输出什么？

class Person { //StaticExercise02.java
    private int id;
    private static int total = 0;
    public static int getTotalPerson() {
        id++;
        return total;
    }
    public Person() {
        total++;
        id = total;
    }
}

public class TestPerson {
    public static void main(String[] args) {
        System.out.println("Number of total is " + Person.getTotalPerson());
        Person p1 = new Person();
        System.out.println("Number of total is " + Person.getTotalPerson());
    }
}
```

```java
class Person { //StaticExercise02.java
    private int id;
    private static int total = 0;
    public static int getTotalPerson() {
        // id++;  // 不行
        return total;
    }
    public Person() {
        total++;
        id = total;
    }
}

public class TestPerson {
    public static void main(String[] args) {
        System.out.println("Number of total is " + Person.getTotalPerson()); // 0
        Person p1 = new Person();
        System.out.println("Number of total is " + Person.getTotalPerson()); // 1
    }
}
```

练习 3

```java
// 题3(评讲)，看看下面代码有没有错误，如果有错误，就修改，看看total等于多少？

class Person { //StaticExercise03.java
    private int id;
    private static int total = 0;
    public static void setTotalPerson(int total) {
        this.total = total;
        Person.total = total;
    }
    public Person() {
        total++;
        id = total;
    }
}

public class TestPerson {
    public static void main(String[] args) {
        Person.setTotalPerson(3);
        new Person();
    }
}
```

```java
// 题3(评讲)，看看下面代码有没有错误，如果有错误，就修改，看看total等于多少？

class Person { //StaticExercise03.java
    private int id;
    private static int total = 0;
    public static void setTotalPerson(int total) {
        // this.total = total;
        Person.total = total;
    }
    public Person() {
        total++;
        id = total;
    }
}

public class TestPerson {
    public static void main(String[] args) {
        Person.setTotalPerson(3); 
        new Person();
        // 这里 total=4
    }
}
```

---

## main

为什么是`public static void main(String[] args)`

* `public`：main 函数是虚拟机调用的，JVM 和 main 不在一个包，也不是继承关系
* `static`：JVM 调用 main 并不需要创建对象
* `String[] args`：传入的参数列表

因为 main 是 static 的，所以只能调用自己的类的 static 的成员。如果要调用非静态的，就要实例化一个新对象

```java
public Test{
    static int i=1;
    int j=2;
    public static void main(String[] args){
        System.out.println(i);
        Test t = new Test(); 
        System.out.println(t.j);
    }
}
```

## 面试题

* 简述一下static
  * 变量：静态变量，类级别变量，所有实例共享同⼀份数据。
  * ⽅法：静态⽅法，类级别⽅法，与实例⽆关。
  * 代码块：在类加载时初始化⼀些数据，只执⾏⼀次。[code-block](code-block.md)
  * 内部类：与外部类绑定但独⽴于外部类实例。[inner-class](inner-class.md)
  * 导⼊：可以直接访问静态成员，⽆需通过类名引⽤，简化代码书写，但会降低代码可读性

* 关于加载顺序

    ```java
      static int a = method();  
      
      static int b = 10;  
      
      public static int method(){  
        return b;  
      }  
      
      @Test  
      public void test3(){  
        System.out.println(a); // 0  
      }
    ```

  答案：0。因为调用 method 的时候是 a 调用的，这时候 b 还没被初始化，所以是 0。

