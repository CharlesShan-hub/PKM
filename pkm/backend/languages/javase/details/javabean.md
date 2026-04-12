# Java Bean (实体类)

要求

* 类中所有的成员变量全部私有，并提供`public`修饰的`getter/setter`方法
* 类中需要提供一个无参数构造器，有参数构造器可选

案例（主要是这个思想）

```java
package javabean;  
  
public class Main {  
    public static void main(String[] args) {  
        StudentOperator sp = new StudentOperator();  
        Student student = new Student("Charles", 2000);  
        sp.setStudent(student);  
        sp.print();  
    }  
}
```

```java
package javabean;  
  
public class Student {  
    private String name;  
    private int year;  
    public String getName() {  
        return name;  
    }  
    public void setName(String name) {  
        this.name = name;  
    }  
    public int getYear() {  
        return year;  
    }  
    public void setYear(int year) {  
        this.year = year;  
    }  
    public Student(String name, int year) {  
        this.name = name;  
        this.year = year;  
    }  
    public Student() {}  
}
```

```java
package javabean;  
  
public class StudentOperator {  
    private Student student;  
  
    public StudentOperator() {}  
  
    public StudentOperator(Student student) {  
        this.student = student;  
    }  
  
    public void setStudent(Student student) {  
        this.student = student;  
    }  
  
    public void print(){  
        if(student != null){  
            System.out.println(student.getName() + " birth in " + student.getYear());  
        }else{  
            System.out.println("Student is null");  
        }  
    }  
}
```
