面试题

```java
package com.powernode.javase.thread03;  

/**
 * 关于sleep的面试题：以下程序中，是main线程休眠5秒，还是分支线程休眠5秒？
 */
public class ThreadTest {
  public static void main(String[] args) {
    MyThread t = new MyThread();
    t.setName("t");
    t.start();

    try {
      // 这行代码并不是让t线程睡眠，而是让当前线程睡眠。
      // 当前线程是main线程。
      t.sleep(100); // 等同于：Thread.sleep(100);
    } catch (InterruptedException e) {
      throw new RuntimeException(e);
    }

    for (int i = 0; i < 5; i++) {
      System.out.println(Thread.currentThread().getName() + "===>" + i);
    }
  }
}

class MyThread extends Thread {
  @Override
  public void run(){
    for (int i = 0; i < 5; i++) {
      System.out.println(Thread.currentThread().getName() + "===>" + i);
    }
  }
}
```