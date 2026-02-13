
```java
package com.powernode.javase.thread23;  

import java.util.concurrent.locks.ReentrantLock;  

class SingletonTest {  

  // 静态变量  
  private static Singleton s1;  
  private static Singleton s2;  

  public static void main(String[] args) {  

    // 创建线程对象t1  
    Thread t1 = new Thread(new Runnable() {  
      @Override  
      public void run() {  
        s1 = Singleton.getSingleton();  
      }  
    });  

    // 创建线程对象t2  
    Thread t2 = new Thread(new Runnable() {  
      @Override  
      public void run() {  
        s2 = Singleton.getSingleton();  
      }  
    });  

    // 启动线程  
    t1.start();  
    t2.start();  

    try {  
      t1.join();  
    } catch (InterruptedException e) {  
      throw new RuntimeException(e);  
    }  
    try {  
      t2.join();  
    } catch (InterruptedException e) {  
      throw new RuntimeException(e);  
    }  

    // 判断这两个Singleton对象是否一样。  
    System.out.println(s1);  
    System.out.println(s2);  
    System.out.println(s1 == s2);  

  }  
}  

/**  
 * 懒汉式单例模式  
 */  
public class Singleton {  
  private static Singleton singleton;  

  private Singleton() {  
    System.out.println("构造方法执行了！");  
  }  

  // 使用Lock来实现线程安全  
  // Lock是接口，从JDK5开始引入的。  
  // Lock接口下有一个实现类：可重入锁（ReentrantLock）  
  // 注意：要想使用ReentrantLock达到线程安全，假设要让t1 t2 t3线程同步，就需要让t1 t2 t3共享同一个lock。  
  // Lock 和 synchronized 哪个好？Lock更好。为什么？因为更加灵活。  
  private static final ReentrantLock lock = new ReentrantLock();  

  public static Singleton getSingleton() {  
    if(singleton == null){  

      try {  
        // 加锁  
        lock.lock();  
        if (singleton == null) {  
          try {  
            Thread.sleep(2000);  
          } catch (InterruptedException e) {  
            throw new RuntimeException(e);  
          }  
          singleton = new Singleton();  
        }  
      } finally {  
        // 解锁（需要100%保证解锁，怎么办？finally）  
        lock.unlock();  
      }  

    }  
    return singleton;  
  }  
}
```
