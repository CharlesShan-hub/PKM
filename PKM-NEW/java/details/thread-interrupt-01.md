
```java
package com.powernode.javase.thread04;  

/**  
 * 怎么中断一个线程的睡眠。（怎么解除线程因sleep导致的阻塞，让其开始抢夺CPU时间片。）  
 */  
public class ThreadTest {  
  public static void main(String[] args) {  
    // 创建线程对象并启动  
    Thread t = new Thread(new Runnable() {  
      @Override  
      public void run() {  
        System.out.println(Thread.currentThread().getName() + "===> begin");  
        try {  
          // 睡眠一年  
          Thread.sleep(1000 * 60 * 60 * 24 * 365);  
        } catch (InterruptedException e) {  
          // 打印异常信息  
          //e.printStackTrace();  
          System.out.println("知道了，这就起床！");  
        }  
        // 睡眠一年之后，起来干活了  
        System.out.println(Thread.currentThread().getName() + " do some!");  
      }  
    });  

    // 启动线程  
    t.start();  

    // 主线程  
    // 要求：5秒之后，睡眠的Thread-0线程起来干活  
    try {  
      Thread.sleep(5 * 1000);  
    } catch (InterruptedException e) {  
      throw new RuntimeException(e);  
    }  
    // Thread-0起来干活了。  
    // 这行代码的作用是终止 t 线程的睡眠。  
    // interrupt方法是一个实例方法。  
    // 以下代码含义：t线程别睡了。  
    // 底层实现原理是利用了：异常处理机制。  
    // 当调用这个方法的时候，如果t线程正在睡眠，必然会抛出：InterruptedException，然后捕捉异常，终止睡眠。  
    t.interrupt();  

  }  
}
```
