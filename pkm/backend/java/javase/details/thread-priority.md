
```java
package com.powernode.javase.thread10;  

/**  
 * 关于线程生命周期中的JVM调度：  
 *      1. 优先级  
 *      2. 线程是可以设置优先级的，优先级较高的，获得CPU时间片的总体概率高一些。  
 *      3. JVM采用的是抢占式调度模型。谁的优先级高，获取CPU时间片的总体概率就高。  
 *      4. 默认情况下，一个线程的优先级是 5.  
 *      5. 最低是1，最高是10.  
 */
public class ThreadTest {  
  public static void main(String[] args) {  

    System.out.println("最低优先级：" + Thread.MIN_PRIORITY);  
    System.out.println("最高优先级：" + Thread.MAX_PRIORITY);  
    System.out.println("默认优先级：" + Thread.NORM_PRIORITY);  

    // 获取main线程的优先级  
    Thread mainThread = Thread.currentThread();  
    System.out.println("main线程的优先级：" + mainThread.getPriority()); // 5  

    // 设置优先级  
    mainThread.setPriority(Thread.MAX_PRIORITY);  
    System.out.println("main线程的优先级：" + mainThread.getPriority()); // 10


    // 创建两个线程  
    Thread t1 = new MyThread();  
    t1.setName("biiiiiiiiig");  

    Thread t2 = new MyThread();  
    t2.setName("small");  

    t1.setPriority(Thread.MAX_PRIORITY);  
    t2.setPriority(Thread.MIN_PRIORITY);  

    t1.start();  
    t2.start();  
  }  
} 

class MyThread extends Thread {  
  @Override  
  public void run() {  
    for (int i = 0; i < 1000; i++) {  
      System.out.println(Thread.currentThread().getName() + "==>" + i);  

    }  
  }  
}
```
