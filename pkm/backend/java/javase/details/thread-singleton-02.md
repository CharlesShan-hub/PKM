
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

  // 线程安全的：第一种方案（同步方法），找类锁。  
  // 构造方法执行了！  
  // com.powernode.javase.thread23.Singleton@5b480cf9  
  // com.powernode.javase.thread23.Singleton@5b480cf9    
  // true    
  public static synchronized Singleton getSingleton() {        
	     if (singleton == null) {            
		    try {                
			     Thread.sleep(2000);            
			} catch (InterruptedException e) {                
				throw new RuntimeException(e);            
			}            
			singleton = new Singleton();        
		}        
		return singleton;    
	}
}
```
