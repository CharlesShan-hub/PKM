# 代码块

---
## 类的五大成分

1. 成员变量：[attributes-and-methods](../stage1/attributes-and-methods.md)
2. 构造器：[attributes-and-methods](../stage1/attributes-and-methods.md)
3. 方法：[attributes-and-methods](../stage1/attributes-and-methods.md)
4. 代码块：本文
5. 内部类：[inner-class](inner-class.md)

---
## 基本语法

```java
[修饰符]{ // 修饰符只能是 static 或者省略
	代码
}
```

常用情况：对构造器的补充（代码块在构造器之前进行，可以把不同构造器的共同部分先放在代码块里边提前执行）

代码块的种类

1. 普通代码块/**实例代码块**：每次实例化都要执行一次，如果用类的静态属性和方法，并不会执行普通代码块
2. static代码块/**静态代码块**：用于对类进行初始化。
   - **执行时机**：随着类的加载而执行，**并且只会执行一次**。
   - **对比**：如果是普通代码块，每创建一个对象，就执行一次。
3. 类什么时候被加载
   - **创建对象实例时**：使用`new`关键字创建对象时，类会被加载。
   - **创建子类对象实例**：父类也会被加载。
   - **使用类的静态成员时**：包括静态属性和静态方法。

```java
package ex_block;  

public class Test {  
  public static void main(String[] args){  
    PeopleA p1 = new PeopleA(); // Initializing A
    PeopleA p2 = new PeopleA("Jack"); // Initializing A
    PeopleB p3 = new PeopleB();  // Initializing B
    PeopleB p4 = new PeopleB("Jack");  // 不会再输出了
  }
}

class PeopleA{  
  private String name;  
  // 初始化块，用于在构造器执行之前初始化代码  
  {  
    System.out.println("Initializing A");  
  }    
  public PeopleA(){}  
  public PeopleA(String name){  
    this.name = name;  
  }
}

class PeopleB{  
  private String name;  
  // 初始化块，用于在构造器执行之前初始化代码  
  static {  
    System.out.println("Initializing B");  
  }    
  public PeopleB(){}  
  public PeopleB(String name){  
    this.name = name;  
  }
}
```

```java
package ex_block;  

public class Test {  
  public static void main(String[] args){  
    System.out.println("Run Parent static m: ");  
    Parent.m();  
    //static block of Parent  
    //static method of Parent        
    System.out.println("New Parent: ");  
    Parent p = new Parent();  
    // 没有 static block of Parent, 因为在 Parent.m()时就已经执行了静态代码块  
    //normal block of Parent  
    System.out.println("Run Parent m2: ");  
    p.m2();  
    //method of Parent  

    System.out.println("Run Child static m: ");  
    Child.m();  
    //static block of Child  
    //static method of Child        
    System.out.println("New Child: ");  
    Child c = new Child();  
    //normal block of Parent  
    //normal block of Child        
    System.out.println("Run Child m2: ");  
    c.m2();  
    //method of Child  

  }  
}  

class Parent{  
  static {  
    System.out.println("static block of Parent");  
  }  
  { 
    System.out.println("normal block of Parent");  
  }  
  static void m(){  
    System.out.println("static method of Parent");  
  } 
  void m2(){  
    System.out.println("method of Parent");  
  }
}  

class Child extends Parent{  
  static {  
    System.out.println("static block of Child");  
  }  
  {
    System.out.println("normal block of Child");  
  }
  static void m(){  
    System.out.println("static method of Child");  
  }
  void m2(){  
    System.out.println("method of Child");  
  }
}
```

> 我的理解：
> 静态函数执行没有对应的构造器，所以用静态代码块。
> 对应着没有 static 的普通代码快，就变成了构造器的补充。

---
## 执行顺序

创建一个对象时，在 **一个类**（没有继承关系） 调用顺序是:(重点，难点)：
① 调用静态代码块和静态属性初始化(注意：静态代码块和静态属性初始化调用的优先级一样，如果有多个静态代码块和多个静态变量初始化，**则按他们定义的顺序调用**)
```java
class A {
    // 静态属性的初始化
    private static int n1 = getN1();
    
    // 静态代码块
    static {
        System.out.println("A 静态代码块01");
    }

    public static int getN1() {
        System.out.println("getN1被调用...");
        return 100;
    }
    
    public static void main(String[] args) {
        A a = new A();
        // getN1被调用...
        // A 静态代码块01
    }
}
```

```java
class A {
    // 静态代码块
    static {
        System.out.println("A 静态代码块01");
    }
    
	// 静态属性的初始化
    private static int n1 = getN1();

    public static int getN1() {
        System.out.println("getN1被调用...");
        return 100;
    }
    
    public static void main(String[] args) {
        A a = new A();
        // A 静态代码块01
        // getN1被调用...
    }
}
```
② 调用普通代码块和普通属性的初始化(注意：普通代码块和普通属性初始化调用的优先级一样，如果有多个普通代码块和多个普通属性初始化，则按定义顺序调用)
③ 调用构造方法。


构造方法（构造器）的最前边其实隐藏了 super()和调用普通代码块：
```java
package ex_block;  
  
class AAA {  
    // 普通代码块  
    {  
        System.out.println("AAA的普通代码块...");  
    }  
    public AAA() {  
        // (1) 调用父类的构造方法（如果有的话）  
        // super();  
  
        // (2) 调用本类的普通代码块  
        System.out.println("AAA() 构造器被调用...");  
    }
}  
  
class BBB extends AAA {  
    // 普通代码块  
    {  
        System.out.println("BBB的普通代码块...");  
    }  
    public BBB() {  
        // (1) 调用父类的构造方法（如果有的话）  
        // super();  
  
        // (2) 调用本类的普通代码块  
        System.out.println("BBB() 构造器被调用...");  
    }
}  
  
public class Main {  
    public static void main(String[] args) {  
        // 创建 BBB 类的对象，这将触发普通代码块和构造方法的调用  
        System.out.println("创建 BBB 对象");  
        new BBB();  
        //创建 BBB 对象  
        //AAA的普通代码块...  
        //AAA() 构造器被调用...  
        //BBB的普通代码块...  
        //BBB() 构造器被调用...  
    }  
}
```

下边看一下有继承关系的情况（最难的情况）

写一个例子：创建一个子类时(继承关系)，他们的静态代码块，静态属性初始化，普通代码块，普通属性初始化，构造方法的调用顺序如下：
① 父类的静态代码块和静态属性(优先级一样，按定义顺序执行)
② 子类的静态代码块和静态属性(优先级一样，按定义顺序执行)
③ 父类的普通代码块和普通属性初始化(优先级一样，按定义顺序执行)
④ 父类的构造方法
⑤ 子类的普通代码块和普通属性初始化(优先级一样，按定义顺序执行)
⑥ 子类的构造方法 // 面试题

```java
package ex_block;  
  
// 父类 A
class A {  
    // 父类静态属性  
    static int staticVarA;  
    // 父类普通属性  
    int instanceVarA;  
  
    // 父类静态代码块  
    static {  
        System.out.println("父类A的静态代码块执行");  
        staticVarA = 1;  
    }  
    // 父类普通代码块  
    {  
        System.out.println("父类A的普通代码块执行");  
        instanceVarA = 100;  
    }  
    // 父类构造方法  
    public A() {  
        System.out.println("父类A的构造方法执行");  
    }
}  
  
// 子类 B 继承自 A
class B extends A {  
    // 子类静态属性  
    static int staticVarB;  
    // 子类普通属性  
    int instanceVarB;  
  
    // 子类静态代码块  
    static {  
        System.out.println("子类B的静态代码块执行");  
        staticVarB = 2;  
    }  
    // 子类普通代码块  
    {  
        System.out.println("子类B的普通代码块执行");  
        instanceVarB = 200;  
    }  
    // 子类构造方法  
    public B() {  
        System.out.println("子类B的构造方法执行");  
    }
}  
  
// 测试类  
public class Tester {  
    public static void main(String[] args) {  
        // 创建子类B的对象，触发各类初始化和构造方法的调用  
        System.out.println("创建子类B的对象");  
        new B();  
        //创建子类B的对象  
        //父类A的静态代码块执行  
        //子类B的静态代码块执行  
        //父类A的普通代码块执行  
        //父类A的构造方法执行  
        //子类B的普通代码块执行  
        //子类B的构造方法执行  
    }  
}
```


静态代码块只能直接调用静态成员(静态属性和静态方法)，普通代码块可以调用任意成员。

练习 1：

```java
//课堂练习题 CodeBlockExercise01.java
//题1：下面的代码输出什么？
class Person {
    public static int total;
    static {
        total = 100;
        System.out.println("in static block!"); // 1
    }
}

public class Test {
    public static void main(String[] args) {
        System.out.println("total = " + Person.total);
        System.out.println("total = " + Person.total);
    }
}
```

```txt
in static block!
total = 100
total = 100
```

练习 2：

```java
//题2：下面的代码输出什么？
//CodeBlockExercise02.java

class Sample {
    Sample(String s) {
        System.out.println(s);
    }
    Sample() {
        System.out.println("Sample默认构造函数被调用");
    }
}

class Test {
    Sample sam1 = new Sample("sam1成员初始化");
    static Sample sam = new Sample("静态成员sam初始化");
    static {
        System.out.println("static块执行");
        if (sam == null) System.out.println("sam is null");
    }
    Test() {
        System.out.println("Test默认构造函数被调用");
    }
	// 主方法
	public static void main(String str[]) {
	    Test a = new Test(); // 无参构造器
	}
}
```

```txt
静态成员sam初始化 // 静态的第一个
static块执行     // 静态的第二个
sam1成员初始化    // 非静态的第一个
Test默认构造函数被调用 // 构造器
```