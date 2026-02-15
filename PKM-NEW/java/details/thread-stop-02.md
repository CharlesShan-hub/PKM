
```java
package com.powernode.javase.thread06;  

/**  
 * 如何合理的，正常的方式终止一个线程的执行？  
 *      一般我们在实际开发中会使用打标记的方式，来终止一个线程的执行。  
 */  
public class ThreadTest {  
  public static void main(String[] args) {  
    // 创建线程  
    MyRunnable mr = new MyRunnable();  
    Thread t = new Thread(mr);  
    t.setName("t");  
    // 启动线程  
    t.start();  

    // 5秒之后终止线程t的执行  
    try {  
      Thread.sleep(5000);  
    } catch (InterruptedException e) {  
      throw new RuntimeException(e);  
    }  

    //终止线程t的执行。  
    mr.run = false;  
  }  
}  

class MyRunnable implements Runnable {  
  /**  
     * 是否继续执行的标记。  
     * true表示：继续执行。  
     * false表示：停止执行。  
     */  
  boolean run = true;  

  @Override  
  public void run() {  
    for (int i = 0; i < 10; i++) {  
      if(run){  
        System.out.println(Thread.currentThread().getName() + "==>" + i);  
        try {  
          Thread.sleep(1000);  
        } catch (InterruptedException e) {  
          throw new RuntimeException(e);  
        }  
      }else{  
        return;  
      }  
    }  
  }  
}
```
