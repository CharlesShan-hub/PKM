# 封装

浏览顺序：本文 👉 [extends](extends.md) 👉 [polymorphism](polymorphism.md)
 
1. encapsulation

2. 封装：把抽象出来的数据【属性】和对数据的操作【方法】封装在一起，数据被保护在内部，程序的其他部分只有通过被授权的操作【方法】，才能对数据进行访问

3. 好处：可以对赋值进行规则判断

4. 实现：getter和setter（与构造器结合）

   ```java
   public class Person{
     private int age; // 1. 将属性变成 private
     public boolean setName(int age){
       if(age>130 || age<0) return false;
       this.age = age;
       return true;
     }
     public int getAge(){ // 2. public 的 setter 和 getter 
       return this.age;
     }
     public Person(){
       setName(0);
     }
     public Person(int age){
       if(setName(age)==false)setName(0);
     }
   }
   ```

5. 案例

在 Java 中如何实现对类属性的控制呢？以下是一个简单的示例程序 `Encapsulation01.java`，演示了如何对年龄进行合理的验证，并控制对敏感信息（如年龄、工资）的访问。
- 不能随便查看人的年龄、工资等隐私信息。
- 对设置的年龄进行合理的验证：
  - 年龄必须在 1-120 之间。
  - 年龄、工资不能被直接查看。
  - `name` 的长度必须在 2-6 个字符之间。

```java
public class Person {
    public String name;
    private int age;
    private double salary;
    private String job;

    // 构造函数
    public Person(String name, int age, double salary, String job) {
        setName(name);
        setAge(age);
        setSalary(salary);
        this.job = job;
    }

    // name 的 getter 和 setter
    public String getName() {
        return name;
    }

    public void setName(String name) {
        if (name.length() >= 2 && name.length() <= 6) {
            this.name = name;
        } else {
            System.out.println("Name must be between 2 and 6 characters.");
        }
    }

    // age 的 getter 和 setter
    public int getAge() {
        return age;
    }

    public void setAge(int age) {
        if (age >= 1 && age <= 120) {
            this.age = age;
        } else {
            System.out.println("Age must be between 1 and 120.");
            this.age = 0; // 默认年龄
        }
    }

    // salary 的 getter 和 setter
    public double getSalary() {
        return salary;
    }

    public void setSalary(double salary) {
        this.salary = salary;
    }

    // job 的 getter 和 setter
    public String getJob() {
        return job;
    }

    public void setJob(String job) {
        this.job = job;
    }
}