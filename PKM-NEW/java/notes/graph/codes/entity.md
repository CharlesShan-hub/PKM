```java
// Main.java
public class Main {  
    public static void main(String[] args) {  
        Student s = new Student("张三", 100);  
        StudentOperator so = new StudentOperator(s);  
        so.showPassed(); // 张三 passed    
    }  
}
```

```java
// Student.java
package itheima;  
  
public class Student {  
    private String name;  
    private int score;  
  
    public Student(String name, int score) {  
        this.name = name;  
        this.score = score;  
    }  
  
    public String getName() {  
        return name;  
    }  
  
    public void setName(String name) {  
        this.name = name;  
    }  
  
    public int getScore() {  
        return score;  
    }  
  
    public void setScore(int score) {  
        this.score = score;  
    }  
}
```

```java
// StudentOperator.java
package itheima;  
  
public class StudentOperator {  
    private Student s;  
    public StudentOperator(Student s) {  
        this.s = s;  
    }  
    public void showPassed(){  
        if(s.getScore()>=60)  
            System.out.println(s.getName() + " passed");  
        else  
            System.out.println(s.getName() + " failed");  
    }  
}
```