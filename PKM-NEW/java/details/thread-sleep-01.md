
```java
package com.powernode.javase.thread02;  

/**  
 * 关于线程的sleep方法：  
 *      1. static void sleep(long millis)
 *          静态方法，没有返回值，参数是一个毫秒。1秒 = 1000毫秒  
 *      2. 这个方法作用是：  
 *          让当前线程进入休眠，也就是让当前线程放弃占有的CPU时间片，让其进入阻塞状态。  
 *          意思：你别再占用CPU了，让给其他线程吧。  
 *          阻塞多久呢？参数毫秒为准。在指定的时间范围内，当前线程没有权利抢夺CPU时间片了。  
 *      3. 怎么理解“当前线程”呢？  
 *          Thread.sleep(1000); 这个代码出现在哪个线程中，当前线程就是这个线程。  
 *      4. run方法在方法重写的时候，不能在方法声明位置使用 throws 抛出异常。  
 *      5. sleep方法可以模拟每隔固定的时间调用一次程序。  
 */  
public class ThreadTest {  
  public static void main(String[] args) {  
    try {  
      // 让当前线程睡眠5秒  
      // 这段代码出现在主线程中，所以当前线程就是主线程  
      // 让主线程睡眠5秒  
      Thread.sleep(1000 * 5);  
    } catch (InterruptedException e) {  
      throw new RuntimeException(e);  
    }  

    for (int i = 0; i < 10; i++) {  
      System.out.println(Thread.currentThread().getName() + "->" + i);  
    }  

    // 启动线程  
    Thread t = new Thread(new MyRunnable());  
    t.setName("t");  
    t.start();  
  }  
}  

class MyRunnable implements Runnable {  

  @Override  
  public void run(){  
    for (int i = 0; i < 10; i++) {  
      System.out.println(Thread.currentThread().getName() + "->" + i);  
      try {  
        Thread.sleep(1000);  
      } catch (InterruptedException e) {  
        throw new RuntimeException(e);  
      }  
    }  
  }  
}
```
