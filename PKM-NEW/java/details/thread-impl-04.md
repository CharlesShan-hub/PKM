
```java
package com.powernode.javase.thread25;  

import java.util.concurrent.ExecutorService;  
import java.util.concurrent.Executors;  

/**  
 * 创建线程的第四种方式：使用线程池技术。  
 * 线程池本质上就是一个缓存：cache  
 * 一般都是服务器在启动的时候，初始化线程池，  
 * 也就是说服务器在启动的时候，创建N多个线程对象，  
 * 直接放到线程池中，需要使用线程对象的时候，直接从线程池中获取。  
 */  
public class ThreadTest {  
  public static void main(String[] args) {  

    // 创建一个线程池对象（线程池中有3个线程）  
    ExecutorService executorService = Executors.newFixedThreadPool(3);

    // 将任务交给线程池（你不需要触碰到这个线程对象，你只需要将要处理的任务交给线程池即可。）  
    executorService.submit(new Runnable() {
      @Override
      public void run() {
        for (int i = 0; i < 10; i++) {
          System.out.println(Thread.currentThread().getName() + "--->" + i);
        }
      }
    });
    executorService.submit(new Runnable() {
      @Override
      public void run() {
        for (int i = 0; i < 10; i++) {
          System.out.println(Thread.currentThread().getName() + "--->" + i);
        }
      }
    });

    // 最后记得关闭线程池
    executorService.shutdown();
  }  
}
```
