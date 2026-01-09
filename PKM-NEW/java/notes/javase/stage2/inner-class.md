# 内部类

---
## 类的五大成分

1. 成员变量：[attributes-and-methods](../stage1/attributes-and-methods.md)
2. 构造器：[constructor-and-this](../stage1/constructor-and-this.md)
3. 方法：[attributes-and-methods](../stage1/attributes-and-methods.md)
4. 代码块：[code-block](code-block.md)
5. 内部类：本文
---
## 概述

内部类最大的特点就是可以**直接访问私有属性**。

内部类的分类

➢ 定义在外部类局部位置上（比如方法内）：
  1) 局部内部类（有类名）
  2) 匿名内部类（没有类名，重点!!!!!!!!!）

➢ 定义在外部类的成员位置上：
  1) 成员内部类（没用static修饰）
  2) 静态内部类（使用static修饰）

---
## 局部内部类

1. 可以直接访问外部类的所有成员，包含私有的
	```java
	package ex_innerclass;  
	public class Test {  
	    public static void main(String[] args){  
	        Outer outer = new Outer();  
	        outer.m(); // 100  
	    }  
	}  
	  
	class Outer {  
	    private int a = 100;  
	    public void m(){  
	        //局部内部类通常定义在方法里边
	        class Inner{  
	            public void f(){  
	                System.out.println(a); // 这里可以访问 private a            
	            }  
	        }        
	        Inner inner = new Inner();  
	        inner.f();  
	    }
	}
	```
2. 不能添加访问修饰符，因为**它的地位就是一个局部变量**。局部变量是不能使用修饰符的。但是可以使用final修饰，因为局部变量也可以使用final
	```java
	package ex_innerclass;  
	public class Test {  
	    public static void main(String[] args){  
	        Outer outer = new Outer();  
	        outer.m(); // 100  
	    }  
	}  
	  
	class Outer {  
	    private int a = 100;  
	    public void m(){  
	        final class Inner{  
	            public void f(){  
	                System.out.println(a); // 这里可以访问 private a            }  
	        }        
	        Inner inner = new Inner();  
	        inner.f();  
	    }
	}
	```
3. 作用域：仅仅在定义它的**方法**或**代码块**中。
	```java
	package ex_innerclass;  
    
	public class Test {  
	    public static void main(String[] args){  
	        Outer outer = new Outer(); // 100  
	    }  
	}  
	  
	class Outer {  
	    private int a = 100;  
	    {        
		    final class Inner{  
	            public void f(){  
	                System.out.println(a);  
	            }        
	        }        
	        Inner inner = new Inner();  
	        inner.f();  
	    }
	}
	```
4. 局部内部类---访问---->外部类的成员。局部内部类可以直接访问外部类的成员，比如刚才的用 private。
5. 外部类---访问---->局部内部类的成员。访问方式：创建对象，再访问（注意：必须在作用域内）：要在局部内部类的作用域内创建对象，然后调用方法，就像上边的 `Inner inner = new Inner();`
6. 外部其他类---不能访问----->局部内部类（因为局部内部类地位是一个局部变量）
7. 如果外部类和局部内部类的成员重名时，默认遵循就近原则，如果想访问外部类的成员，则可以使用（外部类名.this.成员）去访问
	```java
	package ex_innerclass;  
	  
	public class Test {  
	    public static void main(String[] args){  
	        Outer outer = new Outer(); // 100  
	        System.out.println(outer); // ex_innerclass.Outer@3feba861  
	    }  
	}  
	  
	class Outer {  
	    private int a = 100;  
	    {        
		    final class Inner{  
	            public void f(){  
	                int a = 10;  
	                System.out.println(a); // 10  
	                System.out.println(Outer.this.a); // 100  
	                // Outer.this是一个对象，哪个调用了f()，this 就指向谁  
	                System.out.println(Outer.this); // ex_innerclass.Outer@3feba861  
	            }  
	        }        
	        Inner inner = new Inner();  
	        inner.f();  
	    }
	}
	```

---
## 匿名内部类(非常重要)

本质：
1. 匿名内部类的本质是“类”
2. 匿名内部类是“内部类”（仍然定义在方法或者代码块中）
3. 匿名内部类没有用户定义的名字，但是有系统取的名字
4. 匿名内部类同时是一个对象

```java
new 类或接口(参数列表){
	类体
}
```

案例

```java
package ex_innerclass;  
  
public class AnonymousInnerClass {  
    public static void main(String[] args){  
        Outer outer = new Outer();  
        outer.method();  
    }
}  
  
class Outer{  
    public void method(){  
        // 基于接口的匿名内部类  
        // 1, 需求: 像是用 IA 接口，并创建对象  
        // 2. 传统方法 写一个类，创建该接口，并创建对象  
        IA baby = new Baby();  
        baby.cry(); // wor~  
  
        // 3. 现在的需求，这个 Baby 类只会用一次，以后再也不用了  
        // 4. 可以用匿名内部类，简化代码  
        // 5. baby2 的编译类型是 IA（就是接口的类型，等号左边）
        // 6. baby2 的运行类型是 匿名内部类!
        /*
	        我们看底层
	        class 底层会分配 implements IA{
			    @Override
			    public void cry(){  
	                System.out.println("WOR~");  
	            }      
	        }
		    如何分配：底层会分配“外部类名$1”
        */
        IA baby2 = new IA(){  
            @Override  
            public void cry(){  
                System.out.println("WOR~");  
            }        
        };        
        baby2.cry(); // WOR~  
        System.out.println(baby2.getClass()); // class ex_innerclass.Outer$1
	    // 7. jdk 在底层创建匿名内部类Outer$1，立即创建了它的实例，并把地址返回给 baby2
	    // 8. 匿名内部类Outer$1使用后就没有了，以后也不能用Outer$1了
	    
		IA baby3 = new IA(){  
		    @Override  
		    public void cry(){  
		        System.out.println("WOR~");  
		    }
		};  
		baby3.cry(); // WOR~  
		System.out.println(baby3.getClass()); // class ex_innerclass.Outer$2
    }  
}  
  
interface IA{  
    public void cry();  
}  
  
class Baby implements IA{  
    @Override  
    public void cry() {  
        System.out.println("wor~");  
    }
}
```

上边的是继承了接口的匿名内部类，下边是继承了类的匿名内部类

```java 
package ex_innerclass;  
  
public class AnonymousInnerClass {  
    public static void main(String[] args){  
        Outer outer = new Outer();  
        outer.method();  
    }
}  
  
abstract class People{  
    public abstract void say();  
}  
  
class Coder extends People{  
    @Override  
    public void say() {  
        System.out.println("我爱 Python!");  
    }
}  
  
class Outer{  
    public void method(){  
        new Coder().say();  
        // 我爱 Python!        
        new Coder(){}.say();  
        // 我爱 Python!        
        new Coder(){  
            @Override  
            public void say(){  
                System.out.println("我爱 Java!");  
            }        
        }.say();  
        // 我爱 Java!    
    }  
}
```

应用场景 1：当做实参直接传递

```java
package ex_innerclass;  
  
public class AnonymousInnerClass {  
    public static void main(String[] args){  
        Laboratory laboratory = new Laboratory();  
        laboratory.push(new Student());  
        // I work from 10AM to 5PM, 5 days a week~  
        laboratory.push(new Student(){  
            @Override  
            public void work(){  
                System.out.println("In bridge, I work from 8AM to 9PM, 6 days a week!!");  
            }        
        });        
        // In bridge, I work from 8AM to 9PM, 6 days a week!!  
    }  
}  
  
class Student{  
    public void work(){  
        System.out.println("I work from 10AM to 5PM, 5 days a week~");  
    }
}  
  
class Laboratory{  
    public void push(Student student){  
        student.work();  
    }
}
```

应用场景 2：
1. 有一个铃声接口 Bell，里面有个 ring 方法。（右图）
2. 有一个手机类 Cellphone，具有闹钟功能 alarmclock，参数是 Bell 类型（右图）
3. 测试手机类的闹钟功能，通过匿名内部类（对象）作为参数，打印：懒猪起床了
4. 再传入另一个匿名内部类（对象），打印：小伙伴上课了
```java
package ex_innerclass;  
  
public class AnonymousInnerClass {  
    public static void main(String[] args){  
        CellPhone p = new CellPhone();  
        p.alarmclock(new Bell() {  
            @Override  
            public void ring() {  
                System.out.println("懒猪起床了");  
            }        
        });  
        p.alarmclock(new Bell() {  
            @Override  
            public void ring() {  
                System.out.println("小伙伴上课了");  
            }        
        });    
    }
}  
  
interface Bell{  
    void ring();  
}  
  
class CellPhone{  
    public void alarmclock(Bell bell){  
        bell.ring();  
    }
}
```

---
## 成员内部类（实例内部类）

> 妙计：成员内部类是外部类的一个成员，所以叫成员内部类。

1. 定义的位置：外部类的成员位置
2. 没有`static`修饰

3. 两种其他外部类获得内部类实例的方法
   1. `Outer.Inner inner = outer.new Inner();  `
   2. `Outer.Inner inner = outer.get();  `（get是自己的写的方法）

```java
package ex_innerclass;  
  
public class AnonymousInnerClass {  
    public static void main(String[] args){  
        Outer outer = new Outer();  
  
        // 1. 通过类的对象调用  
        Outer.Inner inner = outer.new Inner();  
        inner.say();  
        // 要用实例去 new        
        Outer.Inner i2 = new Outer().new Inner();  
        new Outer().new Inner().say();  
  
        // 2. 通过方法返回  
        Outer.Inner i3 = outer.get();  
    }
}  
  
class Outer{ 
    private int n = 10;  
    public String name = "张三";  
  
    // public class Inner  
    // protected class Inner    
    // private class Inner    
    class Inner {   // 成员内部类可以用各种访问修饰符
        public void say() {  
            System.out.println(n);   // 10  
            System.out.println(name);//张三  
        }  
    }    
    public Inner get(){  
        return new Inner();  
    }    
    public void use(){  
        Inner i = new Inner();  
        i.say();  
    }
}
```

## 静态内部类

```java
package ex_innerclass;  
  
public class AnonymousInnerClass {  
    public static void main(String[] args){  
        Outer.Inner inner = new Outer.Inner();   // <--重点
        inner.say(); // 19  
    }  
}  
  
class Outer{  
    private static int a = 19;  
    private int b = 20;  
    public static class Inner{  
        public static void say(){  
            System.out.println(a);  
            //System.out.println(b); 错 静态类只能访问静态成员  
        }  
    }
}
```