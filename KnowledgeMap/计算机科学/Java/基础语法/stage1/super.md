# super

## 使用用法

super代表父类的引用，用于访问父类的【属性】、【方法】、【构造器】

注意⚠️：访问父类构造器，super只能放在构造器的第一句！this也只能放在构造器第一句，所以this和super只能二选一。

```java
class People{
  public age;
  public People(int age){
    this.age = age;
  }
  public String sleep(int time){
    return "Sleep for "+time+" minutes.";
  }
}
```

```java
class Student extends People{
  public int grade;
  // 访问父类的构造器
  public Student(int age,int grade){
    super(age);
    this.grade = grade;
  }
  // 使用父类的方法
  public String study(int time){
    return "Study for "+time+" minutes. "+super.sleep(time*2);
  }
  // 使用父类的方法
  public int getAge(int age){
    return super.age;
  }
}
```

```java
public class Program{
  public static void main(String[] args){
    Student s = new Student(19,);
  }
}
```

## 执行原理

1. this：查找本类，本类没有找父类，再找父类的父类，找到为止
2. super：直接找父类，没有找再找父类的父类，找到为止
3. 没有找到，或者找到了但是不能访问，会报错
4. 多个父类都能找到，服从就近原则

