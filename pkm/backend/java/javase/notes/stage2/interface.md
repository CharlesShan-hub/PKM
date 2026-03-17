# 接口

---

## 接口的定义

* 接口使用`interface`关键字定义。
* 接口的修饰符，只能是 `public` 和默认

* jdk8之前，接口中只能定义**常量**和**抽象方法**。
  * 属性：只能是 `final` 的，而且是 `public static final` （是有的属性都是常量）。
  * 接口中属性的访问形式：`接口名.属性名`。
  * 抽象方法：可以省略`abstract`关键字，只能是`public`方法，并且可以省略`public`关键字。
* jdk8之后，加入了三种新的方法
  * **默认（实例）方法**：需要用`default`修饰，只能是`public`方法，并且可以省略`public`关键字。
  * **私有（实例）方法**：只能由接口中的其他实例方法调用。
  * **静态方法**

```java
public interface AInterface {
    // 属性
  public int n1 = 10;
  public static final String n2 = "Hello";

  // 方法
  // 在接口中，抽象方法，可以省略abstract关键字
  void hi(); // 等价于 public abstract void hi();

  // 在jdk8后，可以有默认实现方法，需要使用 default 关键字修饰
  default public void ok() {
    System.out.println("ok");
    System.out.println(ha());
  }
  // 在 jdk8后，可以有私有方法
  private int ha(){
    return 1;
  }
  // 在 jdk8后，可以有静态方法
  public static void say(){
    System.out.println(AInterface.n2);
  }
}
```

---

## 接口的继承与实现

* 接口不能被实例化，需要被实现后才能实例化

- 普通类实现接口，需要实现所有接口的方法
- 抽象类实现接口，可以不用实现接口的方法
- 一个类可以同时实现多个接口
- 一个接口不能继承其他的类，但是可以继承多个别的接口

```java
package ex_interface;  
  
public class Test {  
  public static void main(String[] args){ 
    // 接口不能被实例化，需要被实现后才能实例化
    // UsbInterface usb = new UsbInterface(); ❌
    Phone phone = new Phone();  
    Camera camera = new Camera();  
    Computer computer = new Computer();  
    computer.work(phone);  
    //Phone Start  
    //Phone Stop        
    computer.work(camera);  
    //Camera Start  
    //Camera Stop    
  }  
}  
  
interface UsbInterface{  
  public void start();  
  public void stop();  
}  
  
class Phone implements UsbInterface{  
  @Override  
  public void start() {  
    System.out.println("Phone Start");  
  }  
  @Override  
  public void stop() {  
    System.out.println("Phone Stop");  
  }
}  
  
class Camera implements UsbInterface{  
  @Override  
  public void start() {  
    System.out.println("Camera Start");  
  }  
  @Override  
  public void stop() {  
    System.out.println("Camera Stop");  
  }
}  
  
class Computer{  
    // 通过接口调用方法
  public void work(UsbInterface usbInterface){ 
    usbInterface.start();  
    usbInterface.stop();  
  }
}
```

---

## 接口继承特殊情况

* 一个接口继承多个接口，如果多个接口中存在方法签名冲突，则此时不支持多继承，也不支持多实现

```java
interface A(){
  int a(); // 方法签名冲突
}
interface B(){
  String a();// 方法签名冲突
}
interface C extends A,B{}// 不可以❌
class D implements A,B{}// 不可以❌
```

* 一个类继承了父类，又同时实现了接口，如果父类和接口有同名方法，实现类优先使用父类的

```java
class A{
  public void f(){
    System.out.println('A');
  }
}   
interface B{
  default void f(){
    System.out.println('B');
  }
}
class C extends A implements B{
  public void f1(){
    f(); // A 优先使用父类的
  }
  public void f2(){
    super.f();// A 优先使用父类的
  }
  public void f3(){
    B.super.f(); // B 指定了接口的名字
  }
}
```

* 一个类或者接口实现或者继承了多个接口，如果有冲突的方法，需要手动进行重载。

```java
interface A{
  default void f(){
    System.out.println('A');
  }
}
interface B{
  default void f(){
    System.out.println('B');
  }
}
class C implements A,B{
  @Override
  public void f() {
    A.super.f(); // 使用A的
    // 或者
    B.super.f(); // 使用B的
    // 或者
    // ...
  }
}
interface D extends A,B{
  @Override
  default void f() {
    A.super.f(); // 使用A的
    // 或者
    B.super.f(); // 使用B的
    // 或者
    // ...
  }
}
```

---

## 接口的多态

多态参数：从刚才的代码中可以看到

```java
class Computer{  
    // 通过接口调用方法
    public void work(UsbInterface usbInterface){ 
        usbInterface.start();  
        usbInterface.stop();  
    }
}
```

函数可以接受实现了接口的对象。

换句话说，接口类型的对象可以接受实现了接口的类型的对象。

```java
UsbInterface usbDevice1 = new Camera();
UsbInterface usbDevice2 = new Phone();
```

向下转型

```java
UsbInterface[] usbDevices = new UsbInterface[2]; // 多态数组
usbDevices[0] = new Camera();
usbDevices[1] = new Phone();
for(int i=0; i<usbDevices.lenght; i++)
    usbDevices[i].work();
    if(usbDevices[i] instnaceof Phone)
        ((Phone)usbDevice[i]).call(); // 向下转型
```

多态传递（需要继承父接口的方法）

```java
interface IParent{
    void m(){}
}
interface IChild extends IParent{}
class C implements IChild{
    public void m(){}
}
```

## 练习

### 练习1

```java
interface A{
    int a = 23;
}

class B implements A{
}

//main函数中:
B b = new B();
System.out.println(b.a);
System.out.println(A.a);
System.out.println(B.a);
```

语法是否正确，如果正确，输出什么？

```txt
23,23,23
```

### 程序改错题

```java
interface A{
    int x = 0; 
}
class B{
    int x = 1; 
}
class C extends B implements A {
    public void pX(){
        System.out.println(x);
    }
    public static void main(String[] args) {
        new C().pX();
    }
}
```

```java
interface A{
    int x = 0;  // public static int x = 0;
}
class B{
    int x = 1; 
}
class C extends B implements A {
    public void pX(){
        // System.out.println(x); // 错误 不明确 x 是谁
        System.out.println(super.x); // 使用父类的 x
        System.out.println(A.x); // 使用接口的 x
    }
    public static void main(String[] args) {
        new C().pX();
    }
}
```

### (面试题)抽象类和接口的区别

|      |      抽象类      |      接口      |
| :--: | :-----------: | :----------: |
| 构造方法 |   可以，抽象类也是类   |      不行      |
| 多继承  |      不行       |  可以，接口本身是规范  |
| 抽象方法 | 需要abstract关键字 |   默认就是抽象方法   |
| 具体方法 |   默认就是具体方法    | 需要default关键字 |

1. 相同点
   1. 都是抽象形式，都可以有抽象方法，都不能创建对象。
   2. 都是派生子类形式：抽象类是被子类继承使用，接口是被实现类实现。
   3. 一个类继承抽象类，或者实现接口，都必须重写完他们的抽象方法，否则自己要成为抽象类或者报错！
   4. 都能支持多态，都能够实现解耦合。
2. 不同点
   1. 抽象类中可以定义类的全部普通成员，接口只能定义常量、抽象方法（JDK8新增的三种方式）。
   2. 抽象类只能被类单继承，接口可以被类多实现。
   3. 一个类继承抽象类就不能再继承其他类，一个类实现了接口（还可以继承其他类或者实现其他接口）。
   4. 抽象类体现模板思想：更利于做父类，实现代码的复用性。
   5. 接口更适合做功能的解耦合：解耦合性更强更灵活。
