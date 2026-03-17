# 抽象类

## 引出

当父类的某些方法，需要声明，但是又不确定如何实现，就是用抽象类

```java
class Animal{  
    public void eat(){  
        System.out.println("这是一个动物，但是不知道吃什么🤔");  
    }
}
```

可以改成下边的样子

```java
abstract class Animal{  
    public abstract void eat();  
}  
  
class Dog extends Animal{  
    public void eat(){  
        System.out.println("大棒骨🦴");  
    }
}  
  
class Cat extends Animal{  
    public void eat(){  
        System.out.println("小鱼干🐟");  
    }
}
```

## 细节

1) **抽象类不能被实例化**
2) 抽象类不一定要包含abstract方法。也就是说，抽象类可以没有abstract方法
3) 一旦类包含了abstract方法，则这个类必须声明为abstract 
4) abstract 只能修饰**类**和**方法**，不能修饰属性和其它的
5) 抽象类可以有任意成员【**因为抽象类还是类**】，比如：非抽象方法、构造器、静态属性等等
6) 抽象方法不能有主体，即不能实现：❌`abstract void aaa(){ };`
7) 如果一个类继承了抽象类，则它必须实现抽象类的所有抽象方法，除非它自己也声明为 abstract 类。
8) 抽象方法不能用 `private` 、 `final` 和 `static` 来修饰，因为他们是和重写相违背的

## 练习

1) 题1，思考：abstract final class A{} 能编译通过吗，why?❌
2) 题2，思考：abstract public static void test2(); 能编译通过吗，why?❌
3) 题3，思考：abstract private void test3(); 能编译通过吗，why?❌
4) 编写一个Employee类，声明为抽象类，包含如下三个属性：name，id，salary。提供必要的构造器和抽象方法：work()。对于Manager类来说，他既是员工，还具有奖金(bonus)的属性。请使用继承的思想，设计CommonEmployee类和Manager类，要求类中提供必要的方法进行属性访问，实现work()，提示 “经理/普通员工 名字 工作中.....”
    ```java
    package ex_abstract;  
      
    public class Main {  
        public static void main(String[] args){  
            Employee[] p = new Employee[2];  
            p[0] = new Manager("Jack","01",20000);  
            p[1] = new Manager("Joker","01",2000);  
            for(int i=0; i<p.length; i++)  
                p[i].work();  
            // 经理Jack工作中  
            // 经理Joker工作中  
        }  
    }  
      
    abstract class Employee{  
        private String name;  
        private String id;  
        private double salary;  
      
        public String getName() {  
            return name;  
        }  
        public String getId() {  
            return id;  
        }  
        public double getSalary() {  
            return salary;  
        }  
        public Employee(String name, String id, double salary) {  
            this.name = name;  
            this.id = id;  
            this.salary = salary;  
        }  
        public abstract void work();  
    }  
      
    class CommonEmployee extends Employee{  
        public CommonEmployee(String name, String id, double salary) {  
            super(name, id, salary);  
        }  
        @Override  
        public void work(){  
            System.out.println("普通员工"+getName()+"工作中");  
        }
    }  
      
    class Manager extends Employee{  
        public Manager(String name, String id, double salary) {  
            super(name, id, salary);  
        }  
        @Override  
        public void work(){  
            System.out.println("经理"+getName()+"工作中");  
        }
    }  
    ```

## 模板设计模式

👉 [template-pattern](../../../design-pattern/template-pattern.md)