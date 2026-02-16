# 单例模式

---
### 简介

1. 是什么：采取一定方法保证整个软件系统中，对后一个类只能存在一个对象实例，并且该类只提供一个取得对象实例的方法
2. 两种：饿汉式、懒汉式

---
### 饿汉式

1. 将构造器私有化
2. 在类的内部创建实例，设置为 static（如果不是 static，就有需要调用构造器了，就矛盾了）

```java
package ex_single;  
  
// 一个男生只能有一个女朋友  
public class Main {  
    public static void main(String[] args){  
        GirlFriend girlFriend1 = GirlFriend.getGrilFriend();  
        GirlFriend girlFriend2 = GirlFriend.getGrilFriend();  
        System.out.println(girlFriend1); // 小红  
        System.out.println(girlFriend2); // 小红  
        System.out.println(girlFriend1 == girlFriend2); // true  
    }  
}  
  
class GirlFriend{  
    private String name;
		// 使用private static创建静态变量，这样保证所有的类只有一个GirlFriend实例
    private static GirlFriend grilFriend = new GirlFriend("小红");  

    private GirlFriend(String name) {  
      this.name = name;  
    }  
    public static GirlFriend getGrilFriend() {  
      return grilFriend;  
    }  
    @Override  
    public String toString(){  
      return name;  
    }
}
```

为什么叫“饿汉”，因为女朋友的在类里边就实例化好了，可能程序不会用到，但是已经先实例化了。

---
### 懒汉式

1. 仍然将构造器私有化
2. 在返回对象的函数中，动态的判断是否创建过对象

```java
package ex_single;  
  
// 一个男生只能有一个女朋友  
public class Main {  
    public static void main(String[] args){  
        GirlFriend girlFriend1 = GirlFriend.getGrilFriend();  
        GirlFriend girlFriend2 = GirlFriend.getGrilFriend();  
        System.out.println(girlFriend1); // 小红  
        System.out.println(girlFriend2); // 小红  
        System.out.println(girlFriend1 == girlFriend2); // true  
    }  
}  
  
class GirlFriend{  
    private String name;  
    private static GirlFriend grilFriend = null;  
  
    private GirlFriend(String name) {  
        this.name = name;  
    }  
    public static GirlFriend getGrilFriend() {  
        if(grilFriend == null)  
            grilFriend = new GirlFriend("小红");  
        return grilFriend;  
    }  
    @Override  
    public String toString(){  
        return name;  
    }
}
```

1. 二者最主要的区别在于创建对象的时机不同：**饿汉式**是在**类加载就创建了对象实例**，而**懒汉式**是在**使用时才创建**。
2. 饿汉式不存在线程安全问题，**懒汉式**存在**线程安全问题**。（后面学习线程后，会完善一把）
3. **饿汉式**存在**浪费资源**的可能。因为如果程序员一个对象实例都没有使用，那么饿汉式创建的对象就浪费了，懒汉式是使用时才创建，就不存在这个问题。
4. 在我们javaSE标准类中，java.lang.Runtime就是经典的单例模式。
