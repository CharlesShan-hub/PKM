# this

---

## this本质

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

## 构造器与this

可以让代码更好读：

```java
public Dog{
    String name;
    int age;
    /*
    public Dog(String _name, int _age){
      name = _name;
      age = _age;
    }
    */
    // 有没有另一种方法，让代码更好读
    public Dog(String name, int age){
      this.name = name;
      this.age = age;
    }
}
```

`this`在构造器中必须放在第一句：

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

## 面试题：this的作用

1. this是⾃身的⼀个对象，代表对象本身，可以理解为：指向对象本身的⼀个指针。
2. 用法一：普通的直接引⽤，this 相当于是指向当前对象本身
3. 用法二：形参与成员变量名字重名，⽤ this 来区分
4. 用法三：引⽤本类的构造⽅法
