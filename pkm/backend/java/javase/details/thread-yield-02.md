
如果把`t2.join();`改成了`Thread.yield();`，那就是根据 CPU 资源去礼让，如果资源充足，那么就不会礼让。

下边是yield的例子


```java
package com.powernode.javase.thread11;  

/**  
 * 关于JVM的调度：  
 *      1. 让位  
 *      2. 静态方法：Thread.yield()  
 *      3. 让当前线程让位。  
 *      4. 注意：让位不会让其进入阻塞状态。只是放弃目前占有的CPU时间片，进入就绪状态，继续抢夺CPU时间片。  
 *      5. 只能保证大方向上的，大概率，到了某个点让位一次。  
 */  
public class ThreadTest {  
  public static void main(String[] args) {  
    Thread t1 = new MyThread();  
    t1.setName("t1");  

    Thread t2 = new MyThread();  
    t2.setName("t2");  

    t1.start();  
    t2.start();  
  }  
}  

class MyThread extends Thread {  
  @Override  
  public void run() {  
    for (int i = 0; i < 500; i++) {  
      if(Thread.currentThread().getName().equals("t1") && i % 10 == 0){  
        System.out.println(Thread.currentThread().getName() + "让位了，此时的i下标是：" + i);  
        // 当前线程让位，这个当前线程一定是t1  
        // t1会让位一次  
        Thread.yield();  
      }  
      System.out.println(Thread.currentThread().getName() + "==>" + i);  
    }  
  }  
}
```

这个是join的

```java
package com.powernode.javase.thread11;  

/**  
 * 关于JVM的调度：  
 *      1. 让位  
 *      2. 静态方法：Thread.yield()  
 *      3. 让当前线程让位。  
 *      4. 注意：让位不会让其进入阻塞状态。只是放弃目前占有的CPU时间片，进入就绪状态，继续抢夺CPU时间片。  
 *      5. 只能保证大方向上的，大概率，到了某个点让位一次。  
 */  
public class ThreadTest {  
  public static void main(String[] args) {  
    MyThread t1 = new MyThread();  
    t1.setName("t1");  

    MyThread t2 = new MyThread();  
    t2.setName("t2");
    t1.otherThread = t2;

    t1.start();  
    t2.start();  
  }  
}  

class MyThread extends Thread {  
  Thread otherThread;
  @Override  
  public void run() {
    for (int i = 0; i < 500; i++) {  
      if(Thread.currentThread().getName().equals("t1") && i % 10 == 0){  
        System.out.println(Thread.currentThread().getName() + "让位了，此时的i下标是：" + i);  
        // 当前线程让位，这个当前线程一定是t1  
        // t1会让位一次  
        //Thread.yield();  
        try{
            otherThread.join(1);
        }catch (InterruptedException e) {  
            throw new RuntimeException(e);  
        }
      }  
      System.out.println(Thread.currentThread().getName() + "==>" + i);  
    }  
  }  
}
```
