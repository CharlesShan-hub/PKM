# 多线程

---
## 基本概念

### 概述
1. 进程：进程是指操作系统中的**一段程序**，它是一个正在执行中的程序实例，**具有独立的内存空间和系统资源**，如文件、网络端口等。在计算机程序执行时，先创建进程，再在进程中进行程序的执行。一般来说，一个进程可以包含多个线程。（简单理解，一个程序就是一个进程。）
2. 线程：线程是指进程中的**一个执行单元**，**是进程的一部分**，它负责在进程中执行程序代码。每个线程都有自己的**栈和程序计数器，并且可以共享进程的资源**。多个线程可以在同一时刻执行不同的操作，从而提高了程序的执行效率。
3. JVM规范中规定：堆内存、方法区 是线程共享的。虚拟机栈、本地方法栈、程序计数器 是每个线程私有的。
4. 关于Java程序的运行原理
	1. “java HelloWorld”执行后，会启动JVM，JVM的启动表示一个进程启动了。
	2. JVM进程会首先启动一个主线程（main-thread），主线程负责调用main方法。因此main方法是在主线程中运行的。
	3. 除了主线程之外，还启动了一个垃圾回收线程。因此启动JVM，至少启动了两个线程。
	4. 在main方法的执行过程中，程序员可以手动创建其他线程对象并启动。

### 并行并发
1. 并行：比如，多个 CPU 彼此就是并行
2. 并发：比如，一个 CPU 轮转处理不同的任务，就是并发

查看本电脑可用的CPU数
```java
package ex_thread;  
  
public class CPUNumber {  
    public static void main(String[] args) {  
        System.out.println(Runtime.getRuntime().availableProcessors());  
    }
}
```


---
## 线程创建

> 1. 继承`Thread`类，重写`run`方法。
> 2. 实现`Runable`接口，重写`run`方法，`Thread t = new Thread(new MyRunnable());`
> 3. 实现`Callable`接口，重写`call`方法并返回数据，`Thread t = new Thread(new FutureTask(new MyCallable()));`
> 4. 线程池，`executorService.submit(new MyRunnable());`

### 继承`Thread`类
👉 [thread-impl-01](../../../details/thread-impl-01.md)
1. 编写一个类继承`Thread`，重写`run()`。
2. 创建线程对象：`Thread t = new MyThread();`
3. 启动线程：`t.start();`

### 实现`Runable`接口

👉 [thread-impl-02](../../../details/thread-impl-02.md)，如果一个类已经继承了其他的类，不能再继承 `Thread` 类了。这里底层使用了**静态代理模式**。

1. 编写一个类实现`Runnable`接口，实现`run()`。
2. 创建线程对象：`Thread t = new Thread(new MyRunnable());`
3. 启动线程：`t.start();`

### 实现`Callable`接口

👉 [thread-impl-03](../../../details/thread-impl-03.md)，继承`Thread`类和实现`Runable`接口都无法内容，而实现`Callable`接口可以实现这种需求。

1. 定义一个类实现`Callable`接口，重写`call()`，封装要做的事情，和要放回的数据。
2. 把`Callable`类型的对象封装成`FutureTask`（线程任务对象）。
3. `futureTask.get()`会等待线程执行完再获取返回值。

### 线程池

👉 [thread-impl-04](../../../details/thread-impl-04.md)

### 为什么是 start 不是 run

因为 run 就是一个普通的方法。直接调用 run 并没有启用多线程

```java
// Thread.java

public synchronized void start() {  
  /**  
     * This method is not invoked for the main method thread or "system"     
     * group threads created/set up by the VM. Any new functionality added     
     * to this method in the future may have to also be added to the VM.     
     *     
     * A zero status value corresponds to state "NEW".     
     */    
  if (threadStatus != 0)  
    throw new IllegalThreadStateException();  

  /* Notify the group that this thread is about to be started  
     * so that it can be added to the group's list of threads     
     * and the group's unstarted count can be decremented. */    
  group.add(this);  

  boolean started = false;  
  try {  
    start0();  
    started = true;  
  } finally {  
    try {  
      if (!started) {  
        group.threadStartFailed(this);  
      }        
    } catch (Throwable ignore) {  
      /* do nothing. If start0 threw a Throwable then  
              it will be passed up the call stack */        
    }  
  }
}
```

`start0()`才是真正的实现了多线程的方法！

---

## 线程方法

### 常用api

| 方法/构造器                                   | 说明                                                   |
| --------------------------------------------- | ------------------------------------------------------ |
| **常用方法**                                  |                                                        |
| `public void run()`                           | 线程的任务方法                                         |
| `public void start()`                         | 启动线程                                               |
| `public String getName()`                     | 获取当前线程的名称，线程名称默认是 Thread-索引         |
| `public void setName(String name)`            | 为线程设置名称                                         |
| `public static Thread currentThread()`        | 获取当前执行的线程对象                                 |
| `public static void sleep(long time)`         | 让当前执行的线程休眠多少毫秒后，再继续执行             |
| `public final void join()`                    | 让调用当前这个方法的线程先执行完                       |
| **常见构造器**                                |                                                        |
| `public Thread()`                             | 创建新线程对象                                         |
| `public Thread(String name)`                  | 创建新线程对象，并指定线程名称                         |
| `public Thread(Runnable target)`              | 创建新线程对象，使用指定的 Runnable 对象               |
| `public Thread(Runnable target, String name)` | 创建新线程对象，使用指定的 Runnable 对象并指定线程名称 |

### 名称管理

* **`setName(String name)`**  ：设置线程名称，与参数`name`相同。  
* **`getName()`**  ：功能：返回当前线程的名称。  
👉 [thread-name](../../../details/thread-name.md)

### jconsole工具

终端输入 jconsole，可以查看进程

---
## 用户线程与守护线程

### 概念

| 特性 | 用户线程（User Thread） | 守护线程（Daemon Thread） |
| :--- | :--- | :--- |
| **别名** | 工作线程 | - |
| **核心作用** | 执行业务逻辑 | 为用户线程提供辅助服务 |
| **生命周期** | 当线程任务执行完成时终止，或可通过通知方式主动结束 | 随用户线程终止而自动结束，当所有用户线程结束时立即销毁 |
| **JVM退出影响** | JVM会等待所有用户线程执行完毕才退出 | 不会阻止JVM退出 |
| **设置方法** | - | `thread.setDaemon(true)` |
| **典型应用** | 业务逻辑处理 | 垃圾回收线程（GC Thread）、日志监控等后台服务 |

3. 典型守护线程示例
	- **垃圾回收线程（GC Thread）​**
		- 持续监控内存状态
		- 用户线程运行时在后台自动回收资源

4. 关键区别对比

| 特性        | 用户线程               | 守护线程               |
|------------|-----------------------|-----------------------|
| 终止条件    | 任务完成/主动通知      | 随用户线程结束自动终止 |
| JVM退出影响 | 会阻止JVM退出          | 不会阻止JVM退出        |
| 典型应用    | 业务逻辑处理           | GC/日志监控等后台服务  |

### 案例

案例1

```java
package ex_thread;  
  
public class Deamon {  
    public static void main(String[] args) throws InterruptedException {  
        MyDeamon myDeamon = new MyDeamon();  
        myDeamon.setDaemon(true);  
        myDeamon.start();  
        for(int i=0; i<5; i++){  
            System.out.println("宝强在工作...");  
            Thread.sleep(100);  
        }   
    }
}
  
class MyDeamon extends Thread{  
    @Override  
    public void run() {  
        while(true){  
            System.out.println("马蓉和宋喆在开心聊天~~");  
            try{  
                Thread.sleep(50);  
            }catch(InterruptedException e){  
                e.printStackTrace();  
            }        
        }    
    }
}  
 
//马蓉和宋喆在开心聊天~~  
//宝强在工作...  
//马蓉和宋喆在开心聊天~~  
//马蓉和宋喆在开心聊天~~  
//宝强在工作...  
//马蓉和宋喆在开心聊天~~  
//宝强在工作...  
//马蓉和宋喆在开心聊天~~  
//马蓉和宋喆在开心聊天~~  
//宝强在工作...  
//马蓉和宋喆在开心聊天~~  
//马蓉和宋喆在开心聊天~~  
//宝强在工作...  
//马蓉和宋喆在开心聊天~~  
//马蓉和宋喆在开心聊天~~  
//  
//Process finished with exit code 0
```

案例2

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

### 定时器

```java
package com.powernode.javase.thread08;  
  
import java.text.SimpleDateFormat;  
import java.util.Date;  
import java.util.Timer;  
import java.util.TimerTask;  
  
/**  
 * 1. JDK中提供的定时任务：  
 *      java.util.Timer         定时器  
 *      java.util.TimerTask     定时任务  
 * 2. 定时器 + 定时任务：可以帮我们在程序中完成：每间隔多久执行一次某段程序。  
 * 3. Timer的构造方法：  
 *      Timer()  
 *      Timer(boolean isDaemon) isDaemon是true表示该定时器是一个守护线程。  
 */  
public class ThreadTest {  
    public static void main(String[] args) throws Exception{  
        // 创建定时器对象（本质上就是一个线程）  
        // 如果这个定时器执行的任务是一个后台任务，是一个守护任务，建议将其定义为守护线程。  
        Timer timer = new Timer(true);  
  
        // 指定定时任务  
        SimpleDateFormat sdf = new SimpleDateFormat("yyyy-MM-dd HH:mm:ss");  
        Date firstTime = sdf.parse("2024-01-27 10:22:00");  
        //timer.schedule(new LogTimerTask(), firstTime, 1000);  
  
  
        // 匿名内部类的方式  
        timer.schedule(new TimerTask() {  
            int count = 0;  
            @Override  
            public void run() {  
                // 执行任务  
                Date now = new Date();  
                String strTime = sdf.format(now);  
                System.out.println(strTime + ": " + count++);  
            }  
        }, firstTime, 1000 * 5);  
  
  
        for (int i = 0; i < 10; i++) {  
            Thread.sleep(1000);  
        }  
    }  
}

/**  
 * 定时任务类：专门记录日期的定时任务类。  
 */  
class LogTimerTask extends TimerTask {  
  
    SimpleDateFormat sdf = new SimpleDateFormat("yyyy-MM-dd HH:mm:ss SSS");  
    int count = 0;  
  
    @Override  
    public void run() {  
        // 执行任务  
        Date now = new Date();  
        String strTime = sdf.format(now);  
        System.out.println(strTime + ": " + count++);  
    }  
}
```


---

 ## 线程的生命周期

### 六种状态

![[../../../assets/threading-drawing|1000]]
* 新建状态（NEW）
* 就绪状态（RUNNABLE）
* 运行状态（RUNNABLE）
* 超时等待状态（TIMED_WAITING）：有时长限定的等待
* 等待状态（WAITING）：无期限的等待，没有时长限定
* 阻塞状态（BLOCKED）：遇到锁之后变成阻塞状态
* 死亡状态（TERMINATED）

| 方法            | 作用场景                         | 备注                          |  
|-----------------|----------------------------------|-------------------------------|  
| `start()`       | 启动新线程                       | 异步执行`run()`中的逻辑       |  
| `run()`         | 定义线程任务                     | 直接调用相当于普通方法        |  
| `sleep()`       | 线程暂停                         | 不释放锁，可能抛`InterruptedException` |  
| `interrupt()`   | 请求终止线程                     | 需线程自身检查中断标志        |  

一个查看 java 线程状态的案例

```java
package ex_thread;  
  
public class State {  
    public static void main(String[] args) throws InterruptedException {  
        T t = new T();  
        System.out.println(t.getName()+"  "+t.getState()); // NEW
        t.start();  
        while(Thread.State.TERMINATED != t.getState()) {  
            System.out.println(t.getName()+"  "+t.getState());  
            Thread.sleep(10);  
        }  
        System.out.println(t.getName()+"  "+t.getState());  
    }
}  
  
class T extends Thread{  
    @Override  
    public void run() {  
        for(int i=0; i<5; i++){  
            System.out.println(Thread.currentThread().getName()+i);  
            try {  
                Thread.sleep(5);  
            } catch (InterruptedException e) {  
                throw new RuntimeException(e);  
            }        
        }    
    }
}
```

### sleep(静态方法)

sleep的使用案例和介绍，注意：休眠时**不释放锁**。  

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

### interrupt(实例方法)

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

```java
package ex_thread;  
  
public class Int {  
    public static void main(String[] args) {  
        People people = new People();  
        people.setName("Charles");  
        people.setPriority(Thread.MIN_PRIORITY);  
        people.start();  
        try {  
            Thread.sleep(5000);  
        } catch (InterruptedException e) {  
            throw new RuntimeException(e);  
        }        
        people.interrupt();  
    }
}  
  
class People extends Thread {  
    @Override  
    public void run() {  
        for (int i = 0; i < 10; i++) {  
            System.out.println(Thread.currentThread().getName()+"在吃包子"+i);  
        }        
        System.out.println(Thread.currentThread().getName()+"开始休息");  
        try {  
            Thread.sleep(20000);  
        } catch (InterruptedException e) {  
            System.out.println(Thread.currentThread().getName()+"的休息被中断");  
        }        
        for (int i = 0; i < 10; i++) {  
            System.out.println(Thread.currentThread().getName()+"在继续吃包子"+i);  
        }    
    }
}
```

### stop

stop是不能成功终止线程

```java
package com.powernode.javase.thread05;  
  
/**  
 * 一个线程 t 一直在正常的运行，如何终止 t 线程的执行！！！！  
 */  
public class ThreadTest {  
    public static void main(String[] args) {  
        Thread t = new Thread(new MyRunnable());  
        t.setName("t");  
        t.start();  
  
        // 5秒之后，t线程停止！  
        try {  
            Thread.sleep(5000);  
        } catch (InterruptedException e) {  
            throw new RuntimeException(e);  
        }  
        // 终止线程t的执行。  
        // 从java2开始就不建议使用了，因为这种方式是强行终止线程。容易导致数据丢失。  
        // 没有保存的数据，在内存中的数据一定会因为此方式导致丢失。  
        t.stop();  
    }  
}  
  
class MyRunnable implements Runnable {  
  
    @Override  
    public void run() {  
        for (int i = 0; i < 10; i++) {  
            try {  
                Thread.sleep(1000);  
            } catch (InterruptedException e) {  
                throw new RuntimeException(e);  
            }  
            System.out.println(Thread.currentThread().getName() + "===>" + i);  
        }  
    }  
}
```

正确的方法需要我们手动使用flag进行判断

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

### join(实例方法)
- **作用**：强制优先执行插队线程
- **特点**：
	- 插队线程必须完全执行完毕
	- 调用线程会等待插队线程完成
- **使用场景**：需要确保某个线程优先完成时

join也可以指定join的时间，就是只把CPU让给某个进程最多一段时间

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

练习
1. **主线程任务**：
   - 每隔1秒输出"hi"
   - 共输出10次
2. **子线程触发条件**：
   - 当主线程输出到第5次"hi"时
   - 启动一个实现`Runnable`接口的子线程
3. **子线程任务**：
   - 每隔1秒输出"hello"
   - 输出满10次后自动退出
4. **线程后续**：
   - 子线程结束后继续输出剩余"hi"
   - 直到完成10次输出

```java
package ex_thread;  
  
public class Ex02 {  
    public static void main(String[] args) throws InterruptedException {  
        Thread thread = new Thread(new Child());  
  
        for(int i = 0;i < 10;i++){  
            System.out.println("hi"+i);  
            Thread.sleep(1000);  
            if(i == 5){  
                thread.start();  
                thread.join();  
            }        
        }  
    }
}  
  
class Child implements Runnable {  
    @Override  
    public void run(){  
        for(int i=0;i<10;i++){  
            System.out.println("hello"+i);  
            try{  
                Thread.sleep(50);  
            }catch(InterruptedException e){  
                e.printStackTrace();  
            }        
        }    
    }
}  
  
//hi0  
//hi1  
//hi2  
//hi3  
//hi4  
//hi5  
//hello0  
//hello1  
//hello2  
//hello3  
//hello4  
//hello5  
//hello6  
//hello7  
//hello8  
//hello9  
//hi6  
//hi7  
//hi8  
//hi9
```

---
## 虚拟机调度

### 调度模型
* 分时调度模型：所有线程轮流使用CPU的执行权，并且平均的分配每个线程占用的CPU的时间。
* 抢占式调度模型：让优先级高的线程以较大的概率优先获得CPU的执行权，如果线程的优先级相同，那么就会随机选择一个线程获得CPU的执行权，而**Java采用的就是抢占式调用**。

### 线程优先级
* ***`setPriority(int priority)`**  
	* 功能：设置线程优先级（范围：1~10）。  
* ***`getPriority()`**  
	* 功能：获取线程优先级。  
* 线程优先级默认是5

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

### yield(让位)
- **作用**：让出CPU资源，允许其他线程执行
- **特点**：
	- 礼让时间不确定
	- 不保证礼让一定成功
- **使用场景**：当线程不需要占用全部CPU资源时

```java
package ex_thread;  
  
public class Yield{  
    public static void main(String[] args) throws InterruptedException{  
        T1 t1 = new T1();  
        t1.start();  
        for(int i=0;i<10;i++){  
            System.out.println(Thread.currentThread().getName()+i);  
            Thread.sleep(100);  
            if(i == 5){  
                t1.join();  
            }        
        }    
    }
}  
  
class T1 extends Thread{  
    @Override  
    public void run() {  
        for(int i=0;i<10;i++){  
            System.out.println(Thread.currentThread().getName()+i);  
            try{  
                Thread.sleep(100);  
            }catch(InterruptedException e){  
                throw new RuntimeException(e);  
            }        
        }    
    }
}
```

```txt
main0
Thread-00
main1
Thread-01
main2
Thread-02
main3
Thread-03
Thread-04
main4
Thread-05
main5
Thread-06
Thread-07
Thread-08
Thread-09
main6
main7
main8
main9
```

如果把`t2.join();`改成了`Thread.yield();`，那就是根据 CPU 资源去礼让，如果资源充足，那么就不会礼让。

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

---

## 锁

我们使用下边的售票案例中的方法名称：

| 特性   | 类锁                                             | 实例锁                                     |
| ------ | ------------------------------------------------ | ------------------------------------------ |
| 方法   | `static synchronized`                            | `synchronized`                             |
|        | `public static synchronized boolean sell(){...}` | `public synchronized boolean sell() {...}` |
| 代码块 | `synchronized(ClassName.class)`                  | `synchronized(this)`                       |
|        | `synchronized(ThreadTicket.class){...}`          | `synchronized(this){...}`                  |

### 没有加锁

我们使用一个卖票的案例，引出锁的应用。假设有一个售票系统，三个售票窗口同时出售300张票。如果没有适当的同步机制，多个线程（窗口）可能会同时访问和修改剩余的票数，导致数据不一致的问题。

```java
package ex_thread;

public class Ticket {
  public static void main(String[] args) {
    new ThreadTicket("窗口1").start();
    new ThreadTicket("窗口2").start();
    new ThreadTicket("窗口3").start();
  }
}

class ThreadTicket extends Thread {
  private static int ticket = 300; // 让多个线程共享票数  

  public ThreadTicket(String name) {
    super(name);
  }

  // 没有使用锁
  public boolean sell() {
    if (ticket <= 0) {
      System.out.println("已卖完");
      return false;
    } else {
      ThraadUtils.sleep(50);
      System.out.println(Thread.currentThread().getName() + "售出一张票, 还剩余" + --ticket);
      return true;
    }
  }

  @Override
  public void run() {
    System.out.println(getName() + "开始售票");
    while (true) {
      if (!sell()) {
        break;
      }
    }
  }
}

class ThraadUtils{
  public static void sleep(long millis) {
    try {
      Thread.sleep(millis);
    } catch (InterruptedException e) {
      throw new RuntimeException(e);
    }
  }
}
```

```txt
....
窗口1售出一张票, 还剩余3 
窗口2售出一张票, 还剩余2 
窗口3售出一张票, 还剩余1 
窗口1售出一张票, 还剩余0 
已卖完 
窗口2售出一张票, 还剩余-1 
已卖完 
窗口3售出一张票, 还剩余-2 
已卖完
```

### 类锁

线程同步：一些敏感数据在同一时刻不能被多个线程同时访问。也就是说，当有一个线程进行访存时，其他线程不能同时进行访存。
我们需要引入`synchronized`来对卖票的方法进行同步。

**​类锁的两种实现方式​**​

- `static synchronized`方法
- `synchronized(ClassName.class)`代码块

下边案例唯一的改变就是 `public boolean sell()` 变成了 `public static synchronized boolean sell()`

```java
package ex_thread;

public class Ticket {
  public static void main(String[] args) {
    new ThreadTicket("窗口1").start();
    new ThreadTicket("窗口2").start();
    new ThreadTicket("窗口3").start();
  }
}

class ThreadTicket extends Thread {
  private static int ticket = 300; // 让多个线程共享票数  

  public ThreadTicket(String name) {
    super(name);
  }

  // 使用静态同步方法，使用类锁
  public static synchronized boolean sell() {
    if (ticket <= 0) {
      System.out.println("已卖完");
      return false;
    } else {
      ThraadUtils.sleep(50);
      System.out.println(Thread.currentThread().getName() + "售出一张票, 还剩余" + --ticket);
      return true;
    }
  }

  @Override
  public void run() {
    System.out.println(getName() + "开始售票");
    while (true) {
      if (!sell()) {
        break;
      }
    }
  }
}

class ThraadUtils{
  public static void sleep(long millis) {
    try {
      Thread.sleep(millis);
    } catch (InterruptedException e) {
      throw new RuntimeException(e);
    }
  }
}
```

这个案例使用`synchronized(ClassName.class)`对代码块进行上锁。

```java
package ex_thread;

public class Ticket {
  public static void main(String[] args) {
    new ThreadTicket("窗口1").start();
    new ThreadTicket("窗口2").start();
    new ThreadTicket("窗口3").start();
  }
}

class ThreadTicket extends Thread {
  private static int ticket = 300; // 让多个线程共享票数  

  public ThreadTicket(String name) {
    super(name);
  }

  public boolean sell() {
    // `static`只能修饰方法，不能修饰代码块
    synchronized(ThreadTicket.class){
      if (ticket <= 0) {
        System.out.println("已卖完");
        return false;
      } else {
        ThraadUtils.sleep(50);
        System.out.println(Thread.currentThread().getName() + "售出一张票, 还剩余" + --ticket);
        return true;
      }
    }
  }

  @Override
  public void run() {
    System.out.println(getName() + "开始售票");
    while (true) {
      if (!sell()) {
        break;
      }
    }
  }
}

class ThraadUtils{
  public static void sleep(long millis) {
    try {
      Thread.sleep(millis);
    } catch (InterruptedException e) {
      throw new RuntimeException(e);
    }
  }
}
```

```txt
窗口3售出一张票, 还剩余4 
窗口3售出一张票, 还剩余3 
窗口3售出一张票, 还剩余2 
窗口3售出一张票, 还剩余1 
窗口3售出一张票, 还剩余0 
已卖完 
已卖完 
已卖完
```

选择哪种方式取决于你的具体需求：如果整个方法都需要同步，用第一种；如果只需要同步方法中的部分代码，用第二种。

### 实例锁

使用线程同步机制，来保证多线程并发环境下的数据安全问题：  
 1. 线程同步的本质是：线程排队执行就是同步机制。  
 2. 语法格式： 

     ```java
     synchronized(必须是需要排队的这几个线程共享的对象){
       // 需要同步的代码
     }
     ```

     “必须是需要排队的这几个线程共享的对象” 这个必须选对了。这个如果选错了，可能会无故增加同步的线程数量，导致效率降低。
 3. 原理是什么？

     ```java
     synchronized(obj){
       // 同步代码块
     }
     ```
 4. 假设obj是t1 t2两个线程共享的。  
     t1和t2执行这个代码的时候，一定是有一个先抢到了CPU时间片。一定是有先后顺序的。  
     假设t1先抢到了CPU时间片。t1线程找共享对象obj的对象锁，找到之后，则占有这把锁。只要能够占有obj对象的对象锁，就有权利进入同步代码块执行代码。  
     当t1线程执行完同步代码块之后，会释放之前占有的对象锁（归还锁）。  
     同样，t2线程抢到CPU时间片之后，也开始执行，也会去找共享对象obj的对象锁，但由于t1线程占有这把锁，t2线程只能在同步代码块之外等待。  
 5. 注意同步代码块的范围，不要无故扩大同步的范围，同步代码块范围越小，效率越高。

| 特性           | `static synchronized`(类锁) | `synchronized`(实例锁) |
| ------------ | ------------------------- | ------------------- |
| ​**​锁对象​**​  | `ClassName.class`         | `this`(当前对象实例)      |
| ​**​作用范围​**​ | 全局，所有实例共享                 | 仅当前实例有效             |
| ​**​适用场景​**​ | 静态变量/静态方法                 | 实例变量/实例方法           |
| ​**​线程安全​**​ | ✅ 所有线程同一把锁                | ❌ 每个线程不同锁           |

我们发现，使用实例锁对`sell`方法或者售卖的代码块进行上锁，程序又失效了。

```java
package ex_thread;

public class Ticket {
  public static void main(String[] args) {
    new ThreadTicket("窗口1").start();
    new ThreadTicket("窗口2").start();
    new ThreadTicket("窗口3").start();
  }
}

class ThreadTicket extends Thread {
  private static int ticket = 300; // 让多个线程共享票数  

  public ThreadTicket(String name) {
    super(name);
  }

  public synchronized boolean sell() {
    if (ticket <= 0) {
      System.out.println("已卖完");
      return false;
    } else {
      try {
        Thread.sleep(50);
      } catch (InterruptedException e) {
        e.printStackTrace();
      }
      System.out.println(Thread.currentThread().getName() + "售出一张票, 还剩余" + --ticket);
      return true;
    }
  }

  @Override
  public void run() {
    System.out.println(getName() + "开始售票");
    while (true) {
      if (!sell()) {
        break;
      }
    }
  }
}
```

```txt
窗口2售出一张票, 还剩余3 
窗口3售出一张票, 还剩余2 
窗口1售出一张票, 还剩余1 
窗口2售出一张票, 还剩余0 
已卖完 
窗口3售出一张票, 还剩余-1 
已卖完 
窗口1售出一张票, 还剩余-2 
已卖完
```

```java
package ex_thread;

public class Ticket {
  public static void main(String[] args) {
    new ThreadTicket("窗口1").start();
    new ThreadTicket("窗口2").start();
    new ThreadTicket("窗口3").start();
  }
}

class ThreadTicket extends Thread {
  private static int ticket = 300; // 让多个线程共享票数  

  public ThreadTicket(String name) {
    super(name);
  }

  public boolean sell() {
    synchronized(this){
      if (ticket <= 0) {
        System.out.println("已卖完");
        return false;
      } else {
        try {
          Thread.sleep(50);
        } catch (InterruptedException e) {
          e.printStackTrace();
        }
        System.out.println(Thread.currentThread().getName() + "售出一张票, 还剩余" + --ticket);
        return true;
      }
    }
  }

  @Override
  public void run() {
    System.out.println(getName() + "开始售票");
    while (true) {
      if (!sell()) {
        break;
      }
    }
  }
}
```

```txt
窗口1售出一张票, 还剩余2 
窗口2售出一张票, 还剩余2 
窗口3售出一张票, 还剩余1 
窗口1售出一张票, 还剩余0 
窗口2售出一张票, 还剩余-1 
已卖完 
已卖完 
窗口3售出一张票, 还剩余-2 
已卖完
```

所以我们需要对同一个对象上锁才可以成功！

注意下边的调用方法进行了更换，要使用
```java
ThreadTicket ticket = new ThreadTicket("窗口");  
new Thread(ticket, "窗口1").start(); 
new Thread(ticket, "窗口2").start(); 
new Thread(ticket, "窗口3").start();
```

完整代码如下

```java
public class Ticket {
  public static void main(String[] args) {
    ThreadTicket ticket = new ThreadTicket();  
    new Thread(ticket, "窗口1").start(); 
    new Thread(ticket, "窗口2").start(); 
    new Thread(ticket, "窗口3").start();
  }
}

class ThreadTicket extends Thread {  
  private static int ticket = 300; // 让多个线程共享票数  

  public boolean sell(){  
    synchronized(this) {
      if (ticket <= 0) {  
        System.out.println("已卖完");  
        return false;  
      }else{  
        try{  
          Thread.sleep(50);  
        }catch (InterruptedException e){  
          e.printStackTrace();  
        }            
        System.out.println(Thread.currentThread().getName()+"售出一张票, 还剩余"+ --ticket);  
        return true;  
      }   
    } 
  }    
  @Override  
  public void run() {  
    System.out.println("Start");  
    while (true) {  
      if(!sell()){  
        break;  
      }        
    }    
  }
}
```

**三个 Thread 操作的是同一个对象！这样才能成功的锁上**，所以就算传入的是别的，比如 object，也可以，只要他们是一个对象

```java
public class Ticket {
    public static void main(String[] args) {
	    ThreadTicket ticket = new ThreadTicket();  
        new Thread(ticket, "窗口1").start(); 
        new Thread(ticket, "窗口2").start(); 
        new Thread(ticket, "窗口3").start();
    }
}

class ThreadTicket extends Thread {  
    private static int ticket = 300; // 让多个线程共享票数  
    private Object obj = new Object(); // <- 这样
  
    public boolean sell(){  
        synchronized(obj) { // <- 这样
	        if (ticket <= 0) {  
	            System.out.println("已卖完");  
	            return false;  
	        }else{  
	            try{  
	                Thread.sleep(50);  
	            }catch (InterruptedException e){  
	                e.printStackTrace();  
	            }            
	            System.out.println(Thread.currentThread().getName()+"售出一张票, 还剩余"+ --ticket);  
	            return true;  
	        }   
        } 
    }
    @Override  
    public void run() {  
        System.out.println("Start");  
        while (true) {  
            if(!sell()){  
                break;  
            }        
        }    
    }
}
```

最后，我们的`synchronized(this)`如果是对一个方法整体进行同步，那么就可以等价于对方法进行`synchronized`并且共享对象就是`this`

### 死锁

```java
package ex_thread;  

public class DeadClock {  
  public static void main(String[] args) {  
    new DeadClockThread(true).start();  
    new DeadClockThread(false).start();  
    // Thread-12  
    // Thread-01    
  }  
}  

class DeadClockThread extends Thread{  
  static Object o1 = new Object();  
  static Object o2 = new Object();  
  boolean flag = true;  

  public DeadClockThread(boolean flag){  
    this.flag = flag;  
  }  

  @Override  
  public void run() {  
    if(flag){  
      synchronized (o1) {  
        System.out.println(Thread.currentThread().getName()+"1");  
        try {  
          Thread.sleep(10000);  
        } catch (InterruptedException e) {  
          throw new RuntimeException(e);  
        }                
        synchronized (o2) {  
          System.out.println(Thread.currentThread().getName()+"2");  
        }            
      }        
    }else{  
      synchronized (o2) {  
        System.out.println(Thread.currentThread().getName()+"2");  
        try {  
          Thread.sleep(10000);  
        } catch (InterruptedException e) {  
          throw new RuntimeException(e);  
        }                
        synchronized (o1) {  
          System.out.println(Thread.currentThread().getName()+"1");  
        }            
      }        
    }   
  }
}
```

| 操作              | 是否释放锁 | 线程状态          | 风险等级   |
| --------------- | ----- | ------------- | ------ |
| sleep()/yield() | ❌     | TIMED_WAITING | ⭐⭐     |
| suspend()       | ❌     | SUSPENDED     | ⚠️⚠️⚠️ |
| wait()          | ✅     | WAITING       | ⭐      |

---
## 线程通信

* wait
* notify
* notifyAll

```java
package com.powernode.javase.thread21;  

/*  
题目描述：两个线程交替输出  
t1-->1  
t2-->2  
t1-->3  
t2-->4  
t1-->5  
t2-->6  
t1-->7  
t2-->8  
t1-->9  
t2-->10  
t1-->11  
t2-->12  
t1-->13  
t2-->14  
....  
 */  
/**  
 * 1. 内容是关于：线程通信。  
 *  
 * 2. 线程通信涉及到三个方法：  
 *      wait()、notify()、notifyAll()  
 * 
 * 3. 以上三个方法都是Object类的方法。  
 * 
 * 4. 其中wait()方法重载了三个：  
 *      wait():调用此方法，线程进入“等待状态”  
 *      wait(毫秒)：调用此方法，线程进入“超时等待状态”  
 *      wait(毫秒, 纳秒)：调用此方法，线程进入“超时等待状态”  
 * 
 * 5. 调用wait方法和notify相关方法的，不是通过线程对象去调用，而是通过共享对象去调用。  
 *  
 * 6. 例如调用了：obj.wait()，什么效果？  
 *      obj是多线程共享的对象。  
 *      当调用了obj.wait()之后，在obj对象上活跃的所有线程进入无期限等待。直到调用了该共享对象的 obj.notify() 方法进行了唤醒。  
 *      而且唤醒后，会接着上一次调用wait()方法的位置继续向下执行。  
 *  
 * 7. obj.wait()方法调用之后，会释放之前占用的对象锁。  
 *  
 * 8. 关于notify和notifyAll方法：  
 *      共享对象.notify(); 调用之后效果是什么？唤醒优先级最高的等待线程。如果优先级一样，则随机唤醒一个。  
 *      共享对象.notifyAll(); 调用之后效果是什么？唤醒所有在该共享对象上等待的线程。  
 */  

public class ThreadTest {  
  public static void main(String[] args) {  
    // 共享对象  
    MyRunnable mr = new MyRunnable();  

    // 两个线程  
    Thread t1 = new Thread(mr);  
    Thread t2 = new Thread(mr);  

    t1.setName("t1");  
    t2.setName("t2");  

    t1.start();  
    t2.start();  
  }  
}  

class MyRunnable implements Runnable {  

  // 实例变量，多线程共享的。  
  private int count = 0;  

  //private Object obj = new Object();  

  @Override  
  public void run() {  
    while(true){  
      synchronized (this){  
        //synchronized (obj) {  

        // 记得唤醒t1线程  
        // t2线程执行过程中把t1唤醒了。但是由于t2仍然占用对象锁，所以即使t1醒了，也不会往下执行。  
        this.notify();  
        //obj.notify();  

        if(count >= 100) break;  
        // 模拟延迟  
        try {  
          Thread.sleep(50);  
        } catch (InterruptedException e) {  
          e.printStackTrace();  
        }  
        // 程序执行到这里count一定是小于100  
        System.out.println(Thread.currentThread().getName() + "-->" + (++count));  

        try {  
          // 让其中一个线程等待，这个等待的线程可能是t1，也可能是t2  
          // 假设是t1线程等待。  
          // t1线程进入无期限的等待，并且等待的时候，不占用对象锁。  
          this.wait();  
          //obj.wait();  
        } catch (InterruptedException e) {  
          e.printStackTrace();  
        }  
      }  
    }  
  }  
}
```

进阶练习：三个线程轮流输出10轮

```java
package com.powernode.javase.thread22;  

/* 新题目：  
 * t1-->A 
 * t2-->B 
 * t3-->C 
 * t1-->A 
 * t2-->B 
 * t3-->C 
 * .... 
 * t1-->A 
 * t2-->B 
 * t3-->C  
 */  
public class ThreadTest {  

  // 共享对象（t1 t2 t3线程共享的一个对象，都去争夺这一把锁）  
  private static final Object lock = new Object();  
  // 给一个初始值，这个初始值表示第一次输出的时候，t1先输出。  
  private static boolean t1Output = true;  
  private static boolean t2Output = false;  
  private static boolean t3Output = false;  

  public static void main(String[] args) {  
    // 创建三个线程  

    // t1线程：负责输出A  
    new Thread(new Runnable() {  
      @Override  
      public void run() {  
        synchronized (lock){  
          for (int i = 0; i < 10; i++) {  
            while(!t1Output){ // 只要不是t1线程输出  
              try {  
                lock.wait();  
              } catch (InterruptedException e) {  
                throw new RuntimeException(e);  
              }  
            }  
            // 程序到这里说明：该t1线程输出了，并且t1线程被唤醒了。  
            System.out.println(Thread.currentThread().getName() + " ---> A");  
            // 该布尔标记的值  
            t1Output = false;  
            t2Output = true;  
            t3Output = false;  
            // 唤醒所有线程  
            lock.notifyAll();  
          }  
        }  
      }  
    }).start();  

    // t2线程：负责输出B  
    new Thread(new Runnable() {  
      @Override  
      public void run() {  
        synchronized (lock){  
          for (int i = 0; i < 10; i++) {  
            while(!t2Output){  
              try {  
                lock.wait();  
              } catch (InterruptedException e) {  
                throw new RuntimeException(e);  
              }  
            }  
            System.out.println(Thread.currentThread().getName() + " ---> B");  
            // 该布尔标记的值  
            t1Output = false;  
            t2Output = false;  
            t3Output = true;  
            // 唤醒所有线程  
            lock.notifyAll();  
          }  
        }  
      }  
    }).start();  

    // t3线程：负责输出C  
    new Thread(new Runnable() {  
      @Override  
      public void run() {  
        synchronized (lock){  
          for (int i = 0; i < 10; i++) {  
            while(!t3Output){  
              try {  
                lock.wait();  
              } catch (InterruptedException e) {  
                throw new RuntimeException(e);  
              }  
            }  
            System.out.println(Thread.currentThread().getName() + " ---> C");  
            // 该布尔标记的值  
            t1Output = true;  
            t2Output = false;  
            t3Output = false;  
            // 唤醒所有线程  
            lock.notifyAll();  
          }  
        }  
      }  
    }).start();  

  }  
}
```

我也实现了一下

```java
package com.powernode.javase.thread2_2;  

public class ThreadTest {  
  public static void main(String[] args) {  
    new Thread(new MyThread(0,1, false),"A").start();  
    new Thread(new MyThread(1,2, false),"B").start();  
    new Thread(new MyThread(2,0, true),"C").start();  
  }  
}  

class MyThread implements Runnable{  
  private static final Object obj = new Object();  
  public static int maxCount = 10;  
  public static int count = 1;  
  public static int currentThreadId = 0;  
  public int nextThreadId = 1;  
  public boolean isLast = false;  
  public int threadId;  
  public MyThread(int threadId, int nextThreadId, boolean isLast){  
    this.threadId = threadId;  
    this.nextThreadId = nextThreadId;  
    this.isLast = isLast;  
  }  
  @Override  
  public void run() {  
    //        System.out.println(Thread.currentThread().getName() + "启动");  
    while(true){  
      synchronized(obj){  
        while(currentThreadId != threadId){  
          //                    System.out.println(Thread.currentThread().getName() + "等待");  
          try {  
            obj.wait();  
          } catch (InterruptedException e) {  
            e.printStackTrace();  
          }  
        }  
        currentThreadId = nextThreadId;  
        if(isLast){  
          count++;  
        }  
        obj.notifyAll();  
        if(count <= maxCount){  
          System.out.println(Thread.currentThread().getName() + " -> " + count);  
        }else{  
          break;  
        }  
      }  
    }  
  }  
}
```

然后gpt的帮助下，进一步封装了一下
```java
package com.powernode.javase.thread2_2;  

import java.util.ArrayList;  
import java.util.List;  

public class ThreadTest {  
  public static void main(String[] args) {  
    ThreadFactory factory = new ThreadFactory(3, 10); // 3个线程，打印到10  
    factory.startThreads();  
  }  
}  

class ThreadFactory {  
  private final Object lock = new Object();  
  private final List<OrderedThread> threads = new ArrayList<>();  
  private final int maxCount;  
  private int count = 1;  
  private int currentThreadId = 0;  

  public ThreadFactory(int threadCount, int maxCount) {  
    this.maxCount = maxCount;  
    initializeThreads(threadCount);  
  }  

  private void initializeThreads(int threadCount) {  
    // 创建线程并设置执行顺序  
    for (int i = 0; i < threadCount; i++) {  
      int nextThreadId = (i + 1) % threadCount;  
      boolean isLast = (i == threadCount - 1);  
      threads.add(new OrderedThread(i, nextThreadId, isLast));  
    }  
  }  

  public void startThreads() {  
    // 启动所有线程  
    for (int i = 0; i < threads.size(); i++) {  
      new Thread(threads.get(i), String.valueOf((char)('A' + i))).start();  
    }  
  }  

  class OrderedThread implements Runnable {  
    private final int threadId;  
    private final int nextThreadId;  
    private final boolean isLast;  

    public OrderedThread(int threadId, int nextThreadId, boolean isLast) {  
      this.threadId = threadId;  
      this.nextThreadId = nextThreadId;  
      this.isLast = isLast;  
    }  

    @Override  
    public void run() {  
      while (true) {  
        synchronized (lock) {  
          // 检查是否完成所有打印  
          if (count > maxCount) {  
            lock.notifyAll();  
            break;  
          }  

          // 等待轮到当前线程执行  
          while (currentThreadId != threadId) {  
            try {  
              lock.wait();  
              // 被唤醒后再次检查是否完成  
              if (count > maxCount) {  
                return;  
              }  
            } catch (InterruptedException e) {  
              Thread.currentThread().interrupt();  
              return;  
            }  
          }  

          // 执行打印  
          System.out.println(Thread.currentThread().getName() + " -> " + count);  

          // 更新状态  
          currentThreadId = nextThreadId;  
          if (isLast) {  
            count++;  
          }  

          // 唤醒其他线程  
          lock.notifyAll();  
        }  
      }  
    }  
  }  
}
```

---
## 懒汉式单例模式安全问题

### synchronized

```java
package com.powernode.javase.thread23;  

import java.util.concurrent.locks.ReentrantLock;  

class SingletonTest {  

  // 静态变量  
  private static Singleton s1;  
  private static Singleton s2;  

  public static void main(String[] args) {  

    // 获取某个类。这是反射机制中的内容。  
    /*
      Class stringClass = String.class;
      Class singletonClass = Singleton.class;
      Class dateClass = java.util.Date.class;
    */  
    // 创建线程对象t1  
    Thread t1 = new Thread(new Runnable() {  
      @Override  
      public void run() {  
        s1 = Singleton.getSingleton();  
      }  
    });  

    // 创建线程对象t2  
    Thread t2 = new Thread(new Runnable() {  
      @Override  
      public void run() {  
        s2 = Singleton.getSingleton();  
      }  
    });  

    // 启动线程  
    t1.start();  
    t2.start();  

    try {  
      t1.join();  
    } catch (InterruptedException e) {  
      throw new RuntimeException(e);  
    }  
    try {  
      t2.join();  
    } catch (InterruptedException e) {  
      throw new RuntimeException(e);  
    }  

    // 判断这两个Singleton对象是否一样。  
    System.out.println(s1);  
    System.out.println(s2);  
    System.out.println(s1 == s2);  

  }  
}  

/**  
 * 懒汉式单例模式  
 */  
public class Singleton {  
  private static Singleton singleton;  

  private Singleton() {  
    System.out.println("构造方法执行了！");  
  }  

  // 非线程安全的。  
  // 构造方法执行了！  
  // 构造方法执行了！  
  // com.powernode.javase.thread23.Singleton@5b480cf9  
  // com.powernode.javase.thread23.Singleton@6f496d9f    
  // false    
  /*public static Singleton getSingleton() {        
	    if (singleton == null) {            
		    try {                
			    Thread.sleep(2000);            
			} catch (InterruptedException e) {                
				throw new RuntimeException(e);            
			}            
			singleton = new Singleton();        
		}        
		return singleton;    
	}*/  

  // 线程安全的：第一种方案（同步方法），找类锁。  
  // 构造方法执行了！  
  // com.powernode.javase.thread23.Singleton@5b480cf9  
  // com.powernode.javase.thread23.Singleton@5b480cf9    
  // true    
  /*public static synchronized Singleton getSingleton() {        
	     if (singleton == null) {            
		    try {                
			     Thread.sleep(2000);            
			} catch (InterruptedException e) {                
				throw new RuntimeException(e);            
			}            
			singleton = new Singleton();        
		}        
		return singleton;    
	}*/  

  // 线程安全的：第二种方案（同步代码块），找的类锁  
  // 构造方法执行了！  
  //com.powernode.javase.thread23.Singleton@5b480cf9  
  //com.powernode.javase.thread23.Singleton@5b480cf9    
  //true    
  /*public static Singleton getSingleton() {        
	    // 这里有一个知识点是反射机制中的内容。可以获取某个类。  
        synchronized (Singleton.class){            
        if (singleton == null) {               
	        try {                    
		        Thread.sleep(2000);                
		    } catch (InterruptedException e) {                    
			    throw new RuntimeException(e);                
			}                
				singleton = new Singleton();            
			}        
		}        
		return singleton;    
	}*/  

  // 线程安全的：这个方案对上一个方案进行优化，提升效率。  
  public static Singleton getSingleton() {  
    if(singleton == null){            
      synchronized (Singleton.class){                
        if (singleton == null) {                    
          try {                        
            Thread.sleep(2000);                    
          } catch (InterruptedException e) {                        
            throw new RuntimeException(e);                    
          }                    
          singleton = new Singleton();                
        }            
      }        
    }        
    return singleton;    
  }
}
```

### Lock

```java
package com.powernode.javase.thread23;  

import java.util.concurrent.locks.ReentrantLock;  

class SingletonTest {  

  // 静态变量  
  private static Singleton s1;  
  private static Singleton s2;  

  public static void main(String[] args) {  

    // 获取某个类。这是反射机制中的内容。  
    /*
      Class stringClass = String.class;
      Class singletonClass = Singleton.class;
      Class dateClass = java.util.Date.class;
    */  
    // 创建线程对象t1  
    Thread t1 = new Thread(new Runnable() {  
      @Override  
      public void run() {  
        s1 = Singleton.getSingleton();  
      }  
    });  

    // 创建线程对象t2  
    Thread t2 = new Thread(new Runnable() {  
      @Override  
      public void run() {  
        s2 = Singleton.getSingleton();  
      }  
    });  

    // 启动线程  
    t1.start();  
    t2.start();  

    try {  
      t1.join();  
    } catch (InterruptedException e) {  
      throw new RuntimeException(e);  
    }  
    try {  
      t2.join();  
    } catch (InterruptedException e) {  
      throw new RuntimeException(e);  
    }  

    // 判断这两个Singleton对象是否一样。  
    System.out.println(s1);  
    System.out.println(s2);  
    System.out.println(s1 == s2);  

  }  
}  

/**  
 * 懒汉式单例模式  
 */  
public class Singleton {  
  private static Singleton singleton;  

  private Singleton() {  
    System.out.println("构造方法执行了！");  
  }  

  // 使用Lock来实现线程安全  
  // Lock是接口，从JDK5开始引入的。  
  // Lock接口下有一个实现类：可重入锁（ReentrantLock）  
  // 注意：要想使用ReentrantLock达到线程安全，假设要让t1 t2 t3线程同步，就需要让t1 t2 t3共享同一个lock。  
  // Lock 和 synchronized 哪个好？Lock更好。为什么？因为更加灵活。  
  private static final ReentrantLock lock = new ReentrantLock();  

  public static Singleton getSingleton() {  
    if(singleton == null){  

      try {  
        // 加锁  
        lock.lock();  
        if (singleton == null) {  
          try {  
            Thread.sleep(2000);  
          } catch (InterruptedException e) {  
            throw new RuntimeException(e);  
          }  
          singleton = new Singleton();  
        }  
      } finally {  
        // 解锁（需要100%保证解锁，怎么办？finally）  
        lock.unlock();  
      }  

    }  
    return singleton;  
  }  
}
```

---
## 练习

### 练习一
1. **线程启动**  
	- 在`main`方法中同时启动两个线程
2. **线程1任务**  
	   - 循环生成并打印0-100的随机整数  
	   - 输出格式示例：`Thread-1: 42`
3. **线程2任务**  
	   - 监听键盘输入  
	   - 当检测到输入字符`Q`时（不区分大小写）  
	   - 立即终止线程1的执行
	```java
	package ex_chapter16;  
	
	import java.util.Scanner;  
	
	public class Ex01 {  
	  public static void main(String[] args){  
	    T1 t1 = new T1();  
	    t1.start();  
	    new T2(t1).start();  
	  }
	}  
	
	class T1 extends Thread{  
	  private boolean loop = true;  
	
	  @Override  
	  public void run() {  
	    while(loop){  
	      System.out.println((int)(Math.random()*100+1));  
	      try {  
	        Thread.sleep(1000);  
	      } catch (InterruptedException e) {  
	        throw new RuntimeException(e);  
	      }        
	    }    
	  }  
	  public void setLoop(boolean loop) {  
	    this.loop = loop;  
	  }
	}  
	
	class T2 extends Thread{  
	  T1 t1;  
	
	  public T2(T1 t){  
	    this.t1 = t;  
	  }  
	  @Override  
	  public void run() {  
	    Scanner scanner = new Scanner(System.in);  
	    while(true){  
	      System.out.println("请输入指令，q 表示退出");  
	      if(scanner.nextLine().charAt(0) == 'q'){  
	        t1.setLoop(false);  
	        System.out.println("结束");  
	        break;  
	      }        
	    }    
	  }
	}
	```

### 练习二
1. **初始条件**  
   - 共享银行卡余额：`10000`元  
   - 两个用户线程同时操作该账户  
1. **取款规则**  
   - 每次固定取款：`1000`元  
   - 当余额 `< 1000` 时停止取款  
1. **同步要求**  
   - 必须保证线程安全  
   - 禁止出现超额取款（余额不能为负）  
	```java
	package ex_chapter16;  
	
	public class Ex02 {  
	  public static void main(String[] args) {  
	    Bank bank = new Bank();  
	    new Thread(bank).start();  
	    new Thread(bank).start();  
	  }
	}  
	
	class Bank extends Thread{  
	  private static int balance = 10000;  
	
	  @Override  
	  public void run() {  
	    while(true) {  
	      synchronized (this) {  
	        if (balance <= 0)  
	          break;  
	        balance -= 1000;  
	        System.out.println(Thread.currentThread().getName() + "取钱后，余额=" + balance);  
	      }            
	      try {  
	        Thread.sleep(100);  
	      } catch (InterruptedException e) {  
	        throw new RuntimeException(e);  
	      }        
	    }    
	  }
	}
	```
	```txt
	Thread-1取钱后，余额=9000
	Thread-2取钱后，余额=8000
	Thread-1取钱后，余额=7000
	Thread-2取钱后，余额=6000
	Thread-1取钱后，余额=5000
	Thread-2取钱后，余额=4000
	Thread-1取钱后，余额=3000
	Thread-2取钱后，余额=2000
	Thread-1取钱后，余额=1000
	Thread-2取钱后，余额=0
	```

### 面试题1

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
      t.sleep(1000 * 5); // 等同于：Thread.sleep(1000 * 5);  
    } catch (InterruptedException e) {  
      throw new RuntimeException(e);  
    }  

    for (int i = 0; i < 100; i++) {  
      System.out.println(Thread.currentThread().getName() + "===>" + i);  
    }  
  }  
}  

class MyThread extends Thread {  
  @Override  
  public void run(){  
    for (int i = 0; i < 100; i++) {  
      System.out.println(Thread.currentThread().getName() + "===>" + i);  
    }  
  }  
}
```

### 面试题2.1

```java
package com.powernode.javase.thread16;  

/**  
 * 线程同步机制的面试题：分析以下程序 m2 方法在执行的时候，需要等待 m1 方法的结束吗？  
 *      不需要。因为m2没有上锁
 * https://www.bilibili.com/video/BV1p7421N7XT?p=76
 */  
public class ThreadTest {  
  public static void main(String[] args) {  
    MyClass mc = new MyClass();  
    Thread t1 = new Thread(new MyRunnable(mc));  
    Thread t2 = new Thread(new MyRunnable(mc));  

    t1.setName("t1");  
    t2.setName("t2");  

    t1.start();  
    try {  
      Thread.sleep(1000);  
    } catch (InterruptedException e) {  
      throw new RuntimeException(e);  
    }  
    t2.start();  
  }  
}  

class MyRunnable implements Runnable {  

  private MyClass mc;  

  public MyRunnable(MyClass mc) {  
    this.mc = mc;  
  }  

  @Override  
  public void run() {  
    if("t1".equals(Thread.currentThread().getName())){  
      mc.m1();  
    }  
    if("t2".equals(Thread.currentThread().getName())){  
      mc.m2();  
    }  
  }  
}  

class MyClass {  
  public synchronized void m1(){  
    System.out.println("m1 begin");  
    try {  
      Thread.sleep(1000 * 5);  
    } catch (InterruptedException e) {  
      throw new RuntimeException(e);  
    }  
    System.out.println("m1 over");  
  }  

  public void m2(){  
    System.out.println("m2 begin");  
    System.out.println("m2 over");  
  }  
}
```

### 面试题2.2

```java
package com.powernode.javase.thread15;  

/**  
 * 线程同步机制的面试题：分析以下程序 m2 方法在执行的时候，需要等待 m1 方法的结束吗？  
 *      需要。  
 * https://www.bilibili.com/video/BV1p7421N7XT?p=77
 */  
public class ThreadTest {  
  public static void main(String[] args) {  
    MyClass mc = new MyClass();  
    Thread t1 = new Thread(new MyRunnable(mc));  
    Thread t2 = new Thread(new MyRunnable(mc));  

    t1.setName("t1");  
    t2.setName("t2");  

    t1.start();  
    try {  
      Thread.sleep(1000);  
    } catch (InterruptedException e) {  
      throw new RuntimeException(e);  
    }  
    t2.start();  
  }  
}  

class MyRunnable implements Runnable {  

  private MyClass mc;  

  public MyRunnable(MyClass mc) {  
    this.mc = mc;  
  }  

  @Override  
  public void run() {  
    if("t1".equals(Thread.currentThread().getName())){  
      mc.m1();  
    }  
    if("t2".equals(Thread.currentThread().getName())){  
      mc.m2();  
    }  
  }  
}  

class MyClass {  
  public synchronized void m1(){  
    System.out.println("m1 begin");  
    try {  
      Thread.sleep(1000 * 5);  
    } catch (InterruptedException e) {  
      throw new RuntimeException(e);  
    }  
    System.out.println("m1 over");  
  }  

  public synchronized void m2(){  
    System.out.println("m2 begin");  
    System.out.println("m2 over");  
  }  
}
```

### 面试题2.3

```java
package com.powernode.javase.thread17;  

/**  
 * 线程同步机制的面试题：分析以下程序 m2 方法在执行的时候，需要等待 m1 方法的结束吗？  
 *      不需要，因为对象锁是两个对象
 */  
public class ThreadTest {  
  public static void main(String[] args) {  
    MyClass mc1 = new MyClass();  
    MyClass mc2 = new MyClass();  
    Thread t1 = new Thread(new MyRunnable(mc1));  
    Thread t2 = new Thread(new MyRunnable(mc2));  

    t1.setName("t1");  
    t2.setName("t2");  

    t1.start();  
    try {  
      Thread.sleep(1000);  
    } catch (InterruptedException e) {  
      throw new RuntimeException(e);  
    }  
    t2.start();  
  }  
}  

class MyRunnable implements Runnable {  

  private MyClass mc;  

  public MyRunnable(MyClass mc) {  
    this.mc = mc;  
  }  

  @Override  
  public void run() {  
    if("t1".equals(Thread.currentThread().getName())){  
      mc.m1();  
    }  
    if("t2".equals(Thread.currentThread().getName())){  
      mc.m2();  
    }  
  }  
}  

class MyClass {  
  public synchronized void m1(){  
    System.out.println("m1 begin");  
    try {  
      Thread.sleep(1000 * 5);  
    } catch (InterruptedException e) {  
      throw new RuntimeException(e);  
    }  
    System.out.println("m1 over");  
  }  

  public synchronized void m2(){  
    System.out.println("m2 begin");  
    System.out.println("m2 over");  
  }  
}
```

### 面试题2.4

```java
package com.powernode.javase.thread18;  

/**  
 * 线程同步机制的面试题：分析以下程序 m2 方法在执行的时候，需要等待 m1 方法的结束吗？  
 *      需要等待。因为是类锁。
 *  
 * 在静态方法上添加synchronized之后，线程会占有类锁。  
 * 类锁是，对于一个类来说，只有一把锁。不管创建了多少个对象，类锁只有一把。  
 *  
 * 静态方法上添加synchronized，实际上是为了保证静态变量的安全。  
 * 实例方法上添加synchronized，实际上是为了保证实例变量的安全。  
 */  
public class ThreadTest {  
  public static void main(String[] args) {  
    MyClass mc1 = new MyClass();  
    MyClass mc2 = new MyClass();  
    Thread t1 = new Thread(new MyRunnable(mc1));  
    Thread t2 = new Thread(new MyRunnable(mc2));  

    t1.setName("t1");  
    t2.setName("t2");  

    t1.start();  
    try {  
      Thread.sleep(1000);  
    } catch (InterruptedException e) {  
      throw new RuntimeException(e);  
    }  
    t2.start();  
  }  
}  

class MyRunnable implements Runnable {  

  private MyClass mc;  

  public MyRunnable(MyClass mc) {  
    this.mc = mc;  
  }  

  @Override  
  public void run() {  
    if("t1".equals(Thread.currentThread().getName())){  
      mc.m1();  
    }  
    if("t2".equals(Thread.currentThread().getName())){  
      mc.m2();  
    }  
  }  
}  

class MyClass {  
  public static synchronized void m1(){  
    System.out.println("m1 begin");  
    try {  
      Thread.sleep(1000 * 5);  
    } catch (InterruptedException e) {  
      throw new RuntimeException(e);  
    }  
    System.out.println("m1 over");  
  }  

  public static synchronized void m2(){  
    System.out.println("m2 begin");  
    System.out.println("m2 over");  
  }  
}
```