
```java
class Animal{
 int age = 1;
}
class Cat extends Animal{
 int age = 2;
}
public class Program{
 public static void main(String[] args){
   Animal a = new Cat();
   System.out.println(a.age);
 }
}
```

```
>>> 1
```
