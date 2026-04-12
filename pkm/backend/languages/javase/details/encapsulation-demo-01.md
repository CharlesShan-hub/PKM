封装的案例：getter和setter（与构造器结合）

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
