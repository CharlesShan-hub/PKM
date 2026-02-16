
```java
package com.powernode.javase.thread09;  

/**  
 * 线程合并  
 *      1. 调用join()方法完成线程合并。  
 *  
 *      2. join()方法是一个实例方法。（不是静态方法） t.join  
 * *      3. 假设在main方法（main线程）中调用了 t.join()，后果是什么？  
 *          t线程合并到主线程中。主线程进入阻塞状态。直到 t 线程执行结束。主线程阻塞解除。  
 *  
 *      4. t.join()方法其实是让当前线程进入阻塞状态，直到t线程结束，当前线程阻塞解除。  
 *  
 *      5. 和sleep方法有点类似，但不一样：  
 *          第一：sleep方法是静态方法，join是实例方法。  
 *          第二：sleep方法可以指定睡眠的时长，join方法不能保证阻塞的时长。  
 *          第三：sleep和join方法都是让当前线程进入阻塞状态。  
 *          第四：sleep方法的阻塞解除条件？时间过去了。 join方法的阻塞解除条件？调用join方法的那个线程结束了。  
 */  
public class ThreadTest {  
  public static void main(String[] args) throws InterruptedException {  
    Thread t = new MyThread();  
    t.setName("t");  
    t.start();  

    System.out.println("main begin");  

    // 合并线程  
    // t合并到main线程中。  
    // main线程受到阻塞（当前线程受到阻塞）  
    // t线程继续执行，直到t线程结束。main线程阻塞解除（当前线程阻塞解除）。  
    //t.join();  

    // join方法也可以有参数，参数是毫秒。  
    // 以下代码表示 t 线程合并到 当前线程，合并时长 10 毫秒  
    // 阻塞当前线程 10 毫秒  
    //t.join(10);  

    // 调用这个方法，是想让当前线程受阻10秒  
    // 但不一定，如果在指定的阻塞时间内，t线程结束了。当前线程阻塞也会解除。  
    t.join(1000 * 10);  

    // 当前线程休眠10秒。  
    //Thread.sleep(1000 * 10);  

    // 主线程  
    for (int i = 0; i < 10; i++) {  
      System.out.println(Thread.currentThread().getName() + "==>" + i);  
    }  

    System.out.println("main over");  
  }  
}  

class MyThread extends Thread {  
  @Override  
  public void run() {  
    for (int i = 0; i < 10; i++) {  
      System.out.println(Thread.currentThread().getName() + "==>" + i);  
    }  
  }  
}
```
