super案例

```java
// A类
class A {
    public A() {
        System.out.println("我是A类");
    }
}

// B类继承自A类
class B extends A {
    public B() {
        System.out.println("我是B类的无参构造");
    }

    public B(String name) {
        System.out.println(name + "我是B类的有参构造");
    }
}

// C类继承自B类
class C extends B {
    public C() {
        this("hello");
        System.out.println("我是c类的无参构造");
    }

    public C(String name) {
        super("hahah");
        System.out.println("我是c类的有参构造");
    }
}

// main方法中创建C类的实例
public class ExtendsExercise02 {
    public static void main(String[] args) {
        C c = new C();
        // 我是A类
        // hahah我是B类的有参构造
        // 我是c类的有参构造
        // 我是c类的无参构造
    }
}
```
