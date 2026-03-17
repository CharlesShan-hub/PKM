* 方法重载：<u>同一个类中，多个同名方法存在，单要求形参不同</u>。

  ```java
  public class Program{
    public static void main(String[] args){
      T t = new T();
      // 调用了 public int plus(int a, int b)
      System.out.println(t.plus(1,2)); // 3
      // 调用了 public double plus(double a, double b)
      System.out.println(t.plus(1.1,2.2)); // 3.3
      // 调用了 public double plus(double a, double b)
      // 1隐形转换成了1.0
      System.out.println(t.plus(1,2.0)); // 3.0
    }
  }
  
  class T{
    public int plus(int a, int b){
      return a+b;
    }
    public double plus(double a, double b){
      return a+b;
    }
  }
  ```

* 要求：方法名必须相同，参数列表必须不同，对返回类型无要求

    ```java
    // 与下边构成方法重载的
    void show(int a, char b, double c){}
    
    void show(int x, char y, double z){} // 不是
    int show(int a, double c, char b){}  // 是
    void show(int a, double c, char b){} // 是
    boolean show(int c, char b){}        // 是
    void show(double c){}                // 是
    double show(int x, char y, double z){}//不是
    void shows(){}                       // 不是
    ```

* 构造器也可以进行方法重载

    ```java
    class Cat{
     int age;
     String name;
     Cat(){
       this(0,"Default");
     }
     Cat(int age){
       this(age,"Default");
     }
     Cat(String name){
       this(0,name);
     }
     Cat(int age, String name){
       this.age = age;
       this.name = name;
     }
    }
    ```

