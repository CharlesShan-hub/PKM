在这个案例中，我们定义了一个名为 `Color` 的枚举类型，并演示了如何使用枚举的各种方法，包括 `valueOf`、`toString`、`equals`、`hashCode`、`getDeclaringClass`、`name`、`ordinal` 和 `compareTo`。此外，我们还尝试克隆一个枚举常量，以展示 `CloneNotSupportedException` 的异常。

练习，声明 Week 枚举类，定义周一到周日，用增强 for 循环
```java
package ex_enum;  

enum Week{  
  MONDAY("星期一"),TUESDAY("星期二"),WEDNESDAY("星期三"),
  THURSDAY("星期四"),FRIDAY("星期五"),SATURDAY("星期六"),
  SUNDAY("星期日");  
  private String name;  
  Week(String name){  
    this.name = name;  
  }    
  @Override  
  public String toString(){  
    return name;  
  }
}  

public class TestWeek {  
  public static void main(String[] args){  
    for(Week weekday: Week.values())  
      System.out.println(weekday);  
    //星期一  
    //星期二  
    //星期三  
    //星期四  
    //星期五  
    //星期六  
    //星期日  
  }  
}
```
