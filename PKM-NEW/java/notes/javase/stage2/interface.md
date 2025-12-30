# 接口

## 入门

```java
package ex_interface;  
  
public class Test {  
    public static void main(String[] args){  
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

## 基本介绍

三种方法

```java
public interface AInterface {
    // 写属性
    public int n1 = 10;

    // 写方法
    // 在接口中，[1]抽象方法，可以省略abstract关键字
    public void hi();
    
    // 在jdk8后，可以有[2]默认实现方法，需要使用 default 关键字修饰
    default public void ok() {
        System.out.println("ok");
    }
    // 在 jdk8后，可以有[3]静态方法
    public static void cry(){
	    System.out.println("cry");
    }
}
```

## 细节

- 接口不能被实例化
- 接口中所有的方法默认是 public 的，接口中的抽象方法可以不用 abstract 修饰（默认 public abstract）
- 普通类实现接口，需要实现所有接口的方法
- 抽象类实现接口，可以不用实现接口的方法
- 一个类可以同时实现多个接口
- 接口的属性，只能是 final 的，而且是 public static final 。
- 接口中属性的访问形式：接口名.属性名
- 一个接口不能继承其他的类，但是可以继承多个别的接口
- 接口的修饰符，只能是 public 和默认

## 接口的多态

1. 多态参数：从刚才的代码中可以看到
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
	
2. 多态数组 & 向下转型
	```java
	UsbInterface[] usbDevices = new UsbInterface[2]; // 多态数组
	usbDevices[0] = new Camera();
	usbDevices[1] = new Phone();
	for(int i=0; i<usbDevices.lenght; i++)
		usbDevices[i].work();
		if(usbDevices[i] instnaceof Phone)
			((Phone)usbDevice[i]).call(); // 向下转型
	```

3. 多态传递（需要继承父接口的方法）
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

程序改错题

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

## (面试题)抽象类和接口的区别

|      |      抽象类      |      接口      |
| :--: | :-----------: | :----------: |
| 构造方法 |   可以，抽象类也是类   |      不行      |
| 多继承  |      不行       |  可以，接口本身是规范  |
| 抽象方法 | 需要abstract关键字 |   默认就是抽象方法   |
| 具体方法 |   默认就是具体方法    | 需要default关键字 |
