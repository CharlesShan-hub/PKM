# 构造器与this

[toc]

## 构造器

* 构造器案例

  ```java
  public class program{
    public static void main(String args[]){
      // 构造器可以进行方法重载
      // 构造器不能有返回值
      Person p1 = new Person();
      Person p2 = new Person(18,"Carl");
      Person p3 = new Person(22);
      System.out.println(p1.age);
      System.out.println(p2.age);
      System.out.println(p3.age);
    }
  }
  class Person{
    int age;
    String name;
    public Person(){
      age = 1;
    }
    public Person(int _age, String _name){
      age = _age;
      name = _name;
    }
    
    public Person(int _age){
      age = _age;
    }
  }
  ```

* 不写构造器的时候，一个类在编译的时候也会有构造器！

  ```java
  public Person{}
  
  // 但是编译的时候会生成默认的构造器：
  public Person{
    Person(){} // <- 默认构造器
  }
  
  // 但是当用户写了构造器之后，默认构造器就没了，就不能再直接new Person();了
  ```

* 对象创建流程的分析（面试题）

  ```java
  class Person{
    int age = 90;
    String name;
    Person(String n, int a){
      name = n;
      age = a;
    }
  }
  ```

  1. 下面是执行`Person p = new Person("小倩",20);`的流程
  2. 在「方法区」加载「类信息(Person类)」
  3. 在「堆」开辟空间，比如「0x1122」，里边有age和name两个字段，
  4. age默认是0，name默认是null，这一步是「隐式初始化」
  5. 进行「显式初始化」，age赋值成90
  6. 运行「构造函数」，age赋值成20，name赋值成0x1133，0x1133是常量池中保存name的位置的地址，该地址保存名字“小倩”
  7. 最后把0x1122赋值到「栈」里边的p变量，p是对象的引用

## this

* 引入this

  ```java
  public Dog{
    String name;
    int age;
    /*
    public Dog(String _name, int _age){
      name = _name;
      age = _age;
    }*/
    // 有没有另一种方法，让代码更好读
    public Dog(String name, int age){
      this.name = name;
      this.age = age;
    }
  }
  ```

* this本质：其实this和name、age一样，都是成员变量，不过this被隐藏起来了，this存放的是对象自己的地址！

* 构造器与this

  ```java
  class T{
    String name;
    int age;
    public T(){
      this("Jack",80);// 必须放在第一句
      System.out.println("this来访问构造器");
    }
    public T(String name,int age){
      this.name = name;
      this.age = age;
    }
  }
  ```
