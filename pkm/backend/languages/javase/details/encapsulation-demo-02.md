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
