# 构造器与this

---

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
      System.out.println(p1.age); // 1
      System.out.println(p2.age); // 18
      System.out.println(p3.age); // 22
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

* （重要‼️）不写构造器的时候，一个类在编译的时候也会有构造器！（可以用 javap 指令反编译看）

  ```java
  public Person{}
  
  // 但是编译的时候会生成默认的构造器：
  public Person{
    Person(){} // <- 默认构造器
  }
  
  // 但是当用户写了构造器之后，默认构造器就没了，就不能再直接new Person();了，除非显示的写出来Person(){}
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

---

## this

### 引入this

有没有另一种方法，让代码更好读
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

### this本质
其实this和name、age一样，都是成员变量，不过this被隐藏起来了，this存放的是对象自己的地址！

```java
public class Demo{
	public static void main(String[] args){
		Dog d1 = new Dog("One", 20);
		Dog d2 = new Dog("Two", 30);
		System.out.println(d1.hashCode()); // 1933863327
		d1.info();// 1933863327
		System.out.println(d2.hashCode()); // 112810359
		d2.info();// 112810359
	}
}
class Dog{
	public String name;
	public int age;
	public Dog(String name, int age){
		this.name = name;
		this.age = age;
	}
	public void info(){
		System.out.println(this.hashCode());
	}
}
```



```java
public class Main {
    public static void main(String[] args) {
        Test t = new Test();
        System.out.println(t.test() == t); // true
    }
}
class Test{
    public Test test(){
        return this;
    }
}
```

### 构造器与this

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

### 面试题：this的作用

1. this是⾃身的⼀个对象，代表对象本身，可以理解为：指向对象本身的⼀个指针。
2. 用法一：普通的直接引⽤，this 相当于是指向当前对象本身
3. 用法二：形参与成员变量名字重名，⽤ this 来区分
4. 用法三：引⽤本类的构造⽅法