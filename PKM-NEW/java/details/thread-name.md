
```java
package com.powernode.javase.thread01;  

/**  
 * 关于线程中常用方法：  
 *      实例方法：  
 *          String getName();  获取线程对象的名字  
 *          void setName(String threadName); 修改线程的名字  
 *      静态方法：  
 *          static Thread currentThread(); 获取当前线程对象的引用。  
 */  
public class ThreadTest {  
  public static void main(String[] args) {  

    // 获取当前线程对象  
    Thread mainThread = Thread.currentThread();  

    // 获取当前线程的名字  
    System.out.println("主线程的名字：" + mainThread.getName()); // 主线程的名字：main  

    // 默认的名字  
    Thread t1 = new MyThread();  
    t1.start();  //分支线程的名字：Thread-0

    // 创建线程时指定名字  
    Thread t2 = new MyThread("tt");  
    t2.start();  // 分支线程的名字：tt 

    // 后期修改名字
    Thread t3 = new MyThread("tt1");  
    t3.setName("t1");  
    t3.start();  // 分支线程的名字：t1
  }  
}  

class MyThread extends Thread{  

  public MyThread(String threadName){  
    super(threadName);  
  }

  public MyThread(){  
    super();  
  }  

  @Override  
  public void run() {  
    // 获取当前线程对象  
    Thread t = Thread.currentThread();  
    // 获取当前线程对象的名字  
    System.out.println("分支线程的名字：" + t.getName()); 
  }  
}
```
