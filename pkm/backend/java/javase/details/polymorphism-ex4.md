
```java
public class Test{
    public static void main(String[] args){
        A a = new B();
        System.out.println(a.sum());
        System.out.println(a.sum1());
    }
}

class A{
    public int i = 10;
    public int sum(){
        return getI() + 10; // 方法有动态绑定机制，所以 getI 是 B 的 getI
    }
    public int sum1(){
        return i+10; // 属性没有动态绑定机制，所以 i 是 A 的 i
    }
    public int getI(){
        return i;
    }
}

class B extends A{
    public int i = 20;
    // public int sum(){
    //   return getI() + 20;
    // }
    // public int sum1(){
    //   return i+10;
    // }
    public int getI(){
        return i;
    }
}
```

```
>>> 30
>>> 20
```

