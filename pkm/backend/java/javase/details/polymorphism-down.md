
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
   ((Child)a).secret();
 }
}
```

```
>>> 不能说的秘密
```