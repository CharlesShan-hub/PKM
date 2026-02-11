# 继承

浏览顺序：[encapsulation](encapsulation.md) 👉 本文 👉 [polymorphism](polymorphism.md)

1. 好处：提高代码的复用性
2. 语法：`class 子类 extends 父类`
3. 子类会调用父类的构造器
	```java
	// Test.java
	package ex_extend;  
	import ex_extend.Parent;  
	import ex_extend.Child;  
	  
	public class Test {  
	    public static void main(String[] args){  
	        Parent p = new Parent();  
	        // Constructor of Parent.  
	        Child c = new Child();  
	        // Constructor of Parent.  
	        // Constructor of Child.        
	        Parent p2 = new Parent("P");  
	        // Constructor of Parent P  
	        Child c2 = new Child("C");  
	        // Constructor of Parent C  
	        // Constructor of Child C    
	    }  
	}
	```

	```java
	// Parent.java
	package ex_extend;  
	  
	class Parent {  
	    public Parent(){  
	        System.out.println("Constructor of Parent.");  
	    } 
		public Parent(String name){  
	        System.out.println("Constructor of Parent "+name);  
	    }
	}  
	  
	class Child extends Parent{  
	    public Child(){  
	        // super();  默认调用父类无参构造器
	        System.out.println("Constructor of Child.");  
	    }
	    public Child(String name){
		    super(name); // 调用父类有参构造器需要手动调用
		    System.out.println("Constructor of Child "+name);  
	    }
	}
	```

4. `super`和`this`一样，也需要在第一行，所以和两个只能二选一
5. java 所有的类都是 Object 的子类
6. java 只能继承一个父类
7. 案例

```java
class A{
	public A(){
		System.out.println("A");
	}
}

class B{
	public B(){
		this("ABC");
		System.out.println("B");
	}
	public B(String name){
		System.out.println("B "+name);
	}
}

public class Test{
	public static void main(String[] args){
		B b = new B(); // 会输出什么
		// A 
		// B ABC 
		// B
	}
}
```

9. 案例

```java
// A类
class A {
    public A() {
        System.out.println("我是A类");
    }
}

// B类继承自A类
class B extends A {
    public B() {
        System.out.println("我是B类的无参构造");
    }

    public B(String name) {
        System.out.println(name + "我是B类的有参构造");
    }
}

// C类继承自B类
class C extends B {
    public C() {
        this("hello");
        System.out.println("我是c类的无参构造");
    }

    public C(String name) {
        super("hahah");
        System.out.println("我是c类的有参构造");
    }
}

// main方法中创建C类的实例
public class ExtendsExercise02 {
    public static void main(String[] args) {
        C c = new C();
        // 我是A类
        // hahah我是B类的有参构造
        // 我是c类的有参构造
        // 我是c类的无参构造
    }
}
```

10. 小案例

   ```java
   package com.charles.extends_;
   class Country{
       String country = "中国";
       @Override
       public String toString(){
           return "这里是"+this.country;
       }
   }
   class Province extends Country{
       String province = "台湾省";
       @Override
       public String toString(){
           return "这里是"+this.country+this.province;
       }
   }
   public class AiGuo{
       public static void main(String[] args){
           Province p = new Province();
           System.out.println(p.toString());
       }
   }
   // print:
   // 这里是中国台湾省
   ```

   
