
```java
package com.powernode.javase.thread23;  

import java.util.concurrent.locks.ReentrantLock;  

class SingletonTest {  

  // 静态变量  
  private static Singleton s1;  
  private static Singleton s2;  

  public static void main(String[] args) {  

    // 获取某个类。这是反射机制中的内容。  
    /*
      Class stringClass = String.class;
      Class singletonClass = Singleton.class;
      Class dateClass = java.util.Date.class;
    */  
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
    
    // t1.join() 和 t2.join() 的作用是
    // 等两个线程都执行完，再往下执行
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

  // 线程安全的：第二种方案（同步代码块），找的类锁  
  // 构造方法执行了！  
  //com.powernode.javase.thread23.Singleton@5b480cf9  
  //com.powernode.javase.thread23.Singleton@5b480cf9    
  //true    
  /*public static Singleton getSingleton() {        
        // 这里有一个知识点是反射机制中的内容。可以获取某个类。  
        synchronized (Singleton.class){            
        if (singleton == null) {               
            try {                    
                Thread.sleep(2000);                
            } catch (InterruptedException e) {                    
                throw new RuntimeException(e);                
            }                
                singleton = new Singleton();            
            }        
        }        
        return singleton;    
    }*/  

  // 线程安全的：这个方案对上一个方案进行优化，提升效率。  
  public static Singleton getSingleton() {  
    if(singleton == null){            
      synchronized (Singleton.class){                
        if (singleton == null) {                    
          try {                        
            Thread.sleep(2000);                    
          } catch (InterruptedException e) {                        
            throw new RuntimeException(e);                    
          }                    
          singleton = new Singleton();                
        }            
      }        
    }        
    return singleton;    
  }
}
```
* **第一次判断**（外层）：**提升效率，避免每次调用都加锁**
    - 如果 singleton 已经创建，直接返回，不用进同步块
- **第二次判断**（内层）：防止创建多个实例
    - 两个线程可能同时通过外层判断（都看到 null）
    - 第一个线程加锁创建后，第二个线程进入同步块
    - 如果没有内层判断，第二个线程会再创建一个，破坏单例