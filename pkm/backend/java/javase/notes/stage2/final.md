# final

---

## 基本使用

1. 使用了 final 的类，就不能继承了

    ```java
    final class A{}  
    //class B extends A{} // 不可以了
    ```

2. 使用了 final 的方法，子类不能重写

    ```java
    class A{  
        final void hi(){  
            System.out.println("A");  
        }
    }  
      
    class B extends A{  
        //final void hi(){}  
    }
    ```

3. 使用了 final 的属性，不能改变

    ```java
    class A{  
        void hi(){  
            final double TAX_TATE = 0.04;  
            //TAX_TATE = 0.05;  
        }
    }
    ```

---

## 细节

1. final修饰的属性又叫常量，一般用 XX_XX_XX 来命名。比如`TAX_TATE`
2. final修饰的属性在定义时必须赋初值，并且以后不能再修改，赋值可以在如下位置之一【选择一个位置赋初值即可】：
   ① 定义时：如 `public final double TAX_RATE = 0.08;`
   ② 在构造器中
   ③ 在代码块中。

    ```java
    class A{
        public final double TAX_RATE1 = 0.8;
        public final double TAX_RATE2;
        public final double TAX_RATE3;
        public A(){
            TAX_RATE2 = 1.1;
        }
        {
            TAX_RATE3 = 2.2;
        }
    }
    ```

3. 如果final修饰的属性是静态的，则初始化的位置只能是
     ① 定义时
     ② 在静态代码块（**不能在构造器中赋值**）。

    ```java
    class B{
        public static final double TAX_RATE1 = 0.8;
        public static final double TAX_RATE2;
        public static final double TAX_RATE3;
        public B(){
            // TAX_RATE2 = 1.1;//错❌
        }
        static {
            TAX_RATE3 = 2.2;
        }
    }
    ```

4. final类不能继承，但是可以实例化对象。
5. 如果类不是final类，但是含有final方法，则该方法虽然不能重写，但是可以被继承。
6. 一般来说，如果一个类已经是final类了，就没有必要再将方法修饰成final方法。（final类没有子类，自然没有重写其方法之说）
7. final不能修饰构造方法(即构造器)
8. （重点）`final` 和 `static` 往往搭配使用，叫做常量，效率更高，底层编译器做了优化处理——进行**宏替换**。

    ```java
    package ex_final;  
      
    public class Test {  
        public static void main(String[] args){  
            System.out.println(A.n);  
            // 1  
            System.out.println(B.n);  
            // B 被加载  
            // 1  
        }  
    }  
      
    class A{  
        public static final int n = 1;  
        static {  
            System.out.println("A 被加载");  
        }
    }  
      
    class B{  
        public static int n = 1;  
        static {  
            System.out.println("B 被加载");  
        }
    }
    ```

9. 包装类(`Integer`,`Double`, `Float`, `Boolean`等都是`final`), `String`也是`final`类。

---

## 练习

请编写一个程序，能够计算圆形的面积。要求圆周率为 3.14。赋值的位置3个方式都写一下

```java
class Circle1{
    private double r;
    // 定义
    private final double PI = 3.14;
    public Circle(double r){
        this.r = r;
    }
    public double area(){
        return PI * r * r;
    }
}

class Circle2{
    private double r;
    private final double PI;
    // 构造器
    public Circle(double r){
        PI = 3.14;
        this.r = r;
    }
    public double area(){
        return PI * r * r;
    }
}

class Circle3{
    private double r;
    private final double PI = 3.14;
    // 代码块
    {
        PI = 3.14;
    }
    public Circle(double r){
        this.r = r;
    }
    public double area(){
        return PI * r * r;
    }
}
```

找错误

```java
public class Something{
    public int addOne(final int x){ // final int x 允许✅
        ++x; // ❌ 修改了 x
        return x+1;
    }
}
```

