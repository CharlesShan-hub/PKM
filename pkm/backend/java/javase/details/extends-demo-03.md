this案例

```java
class A{
    public A(){
        System.out.println("A");
    }
}

class B{
    public B(){
        this("ABC");
        System.out.println("B");
    }
    public B(String name){
        System.out.println("B "+name);
    }
}

public class Test{
    public static void main(String[] args){
        B b = new B(); // 会输出什么
        // A 
        // B ABC 
        // B
    }
}
```
