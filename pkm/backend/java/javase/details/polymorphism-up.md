
```java
class Animal{
 public void say(){
   System.out.println("...");
 }
}
class Cat extends Animal{
 public void say(){
   System.out.println("Miao~");
 }
 protected void secret(){
   System.out.println("不能说的秘密");
 }
}
```

```java
public class Program{
 public static void main(String[] args){
   Animal a = new Cat();
   a.say();
   System.out.println(a instanceof Cat);
   //a.secret(); // 不能调用，因为secret是Cat的方法，不是Animal的方法
 }
}
```

```
>>> Miao~
>>> true
```
