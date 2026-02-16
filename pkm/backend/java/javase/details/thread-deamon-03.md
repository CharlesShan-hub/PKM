
```java
package com.powernode.javase.thread07;  

/**  
 * 1. 在Java语言中，线程被分为两大类：  
 *      第一类：用户线程（非守护线程）  
 *      第二类：守护线程（后台线程）  
 *  
 * 2. 在JVM当中，有一个隐藏的守护线程一直在守护者，它就是GC线程。  
 *  
 * 3. 守护线程的特点：所有的用户线程结束之后，守护线程自动退出/结束。  
 *  
 * 4. 如何将一个线程设置为守护线程？  
 *      t.setDaemon(true);  
 */
public class ThreadTest {  
  public static void main(String[] args) {  
    MyThread myThread = new MyThread();  
    myThread.setName("t");  

    // 在启动线程之前，设置线程为守护线程  
    myThread.setDaemon(true);  

    myThread.start();  

    // 10s结束！  
    // main线程中，main线程是一个用户线程。  
    for (int i = 0; i < 10; i++) {  
      System.out.println(Thread.currentThread().getName() + "===>" + i);  
      try {  
        Thread.sleep(1000);  
      } catch (InterruptedException e) {  
        throw new RuntimeException(e);  
      }  
    }  

  }  
}  

class MyThread extends Thread {  
  @Override  
  public void run() {  
    int i = 0;  
    while(true){  
      System.out.println(Thread.currentThread().getName() + "===>" + (++i));  
      try {  
        Thread.sleep(1000);  
      } catch (InterruptedException e) {  
        throw new RuntimeException(e);  
      }  
    }  
  }  
}
```

