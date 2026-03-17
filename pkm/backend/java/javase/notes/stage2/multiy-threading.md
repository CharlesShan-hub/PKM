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
👉 [thread-impl-01](../../details/thread-impl-01.md)
1. 编写一个类继承`Thread`，重写`run()`。
2. 创建线程对象：`Thread t = new MyThread();`
3. 启动线程：`t.start();`

### 实现`Runable`接口

👉 [thread-impl-02](../../details/thread-impl-02.md)，如果一个类已经继承了其他的类，不能再继承 `Thread` 类了。这里底层使用了**静态代理模式**。

1. 编写一个类实现`Runnable`接口，实现`run()`。
2. 创建线程对象：`Thread t = new Thread(new MyRunnable());`
3. 启动线程：`t.start();`

### 实现`Callable`接口

👉 [thread-impl-03](../../details/thread-impl-03.md)，继承`Thread`类和实现`Runable`接口都无法内容，而实现`Callable`接口可以实现这种需求。

1. 定义一个类实现`Callable`接口，重写`call()`，封装要做的事情，和要放回的数据。
2. 把`Callable`类型的对象封装成`FutureTask`（线程任务对象）。
3. `futureTask.get()`会等待线程执行完再获取返回值。

### 线程池

👉 [thread-impl-04](../../details/thread-impl-04.md)，线程池本质上就是一个缓存：cache 。一般都是服务器在启动的时候，初始化线程池，也就是说服务器在启动的时候，创建N多个线程对象，直接放到线程池中，需要使用线程对象的时候，直接从线程池中获取。 
### 为什么是 start 不是 run

在[Thread.java 源码](../../details/thread-start-source.md)中， run 就是一个普通的方法。直接调用 run 并没有启用多线程，`start0()`才是真正的实现了多线程的方法！

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
👉 [thread-name](../../details/thread-name.md)

### jconsole工具

终端输入 jconsole，可以查看进程

---
## 锁

> 我们使用一个卖票的案例，引出锁的应用。

线程同步：一些敏感数据在同一时刻不能被多个线程同时访问。也就是说，当有一个线程进行访存时，其他线程不能同时进行访存。我们需要引入`synchronized`来对卖票的方法进行同步。

|                | 类锁                                             | 实例锁                                     |
| -------------- | ------------------------------------------------ | ------------------------------------------ |
| **同步方法**   | `static synchronized`                            | `synchronized`                             |
|                | `public static synchronized boolean sell(){...}` | `public synchronized boolean sell() {...}` |
| **同步代码块** | `synchronized(ClassName.class)`                  | `synchronized(this)`                       |
|                | `synchronized(ThreadTicket.class){...}`          | `synchronized(this){...}`                  |
| 作用范围​​       | 全局，所有实例共享                               | 仅当前实例有效                             |
| 适用场景       | 静态变量/静态方法                                | 实例变量/实例方法                          |
| 线程安全​​       | ✅ 所有线程同一把锁                               | ❌ 每个线程不同锁                           |

### 没有加锁

假设有一个售票系统，三个售票窗口同时出售5张票。如果没有适当的同步机制，多个线程（窗口）可能会同时访问和修改剩余的票数，导致数据不一致的问题。

👉 [thread-lock-01](../../details/thread-lock-01.md)
### 类锁

**​类锁的两种实现方式​**：如果整个方法都需要同步，用第一种；如果只需要同步方法中的部分代码，用第二种。​

- `static synchronized`方法
    -  `public boolean sell()` 变成了 `public static synchronized boolean sell()`（唯一的改变）
    - 👉 [thread-lock-02](../../details/thread-lock-02.md)
- `synchronized(ClassName.class)`代码块
    - 使用`synchronized(ClassName.class)`对代码块
    - 👉 [thread-lock-03](../../details/thread-lock-03.md)

### 实例锁

1. 语法
    ```java
    synchronized(需要排队的线程共享的对象){
        // 需要同步的代码
    }
    ```
2. 原理：假设`obj`是`t1`, `t2`两个线程共享的。`t1`和`t2`执行这个代码的时候，一定是有一个先抢到了CPU时间片。假设`t1`先抢到了CPU时间片。`t1`线程找共享对象`obj`的对象锁，找到之后，则占有这把锁。只要能够占有`obj`对象的对象锁，就有权利进入同步代码块执行代码。 当`t1`线程执行完同步代码块之后，会释放之前占有的对象锁（归还锁）。 同样，`t2`线程抢到CPU时间片之后，也开始执行，也会去找共享对象`obj`的对象锁，但由于`t1`线程占有这把锁，`t2`线程只能在同步代码块之外等待。
    ```java
    synchronized(obj){
        // 同步代码块
    }
    ```
3. 注意同步代码块的范围，不要无故扩大同步的范围，同步代码块范围越小，效率越高。
4. `obj`需要是线程共享的对象，如果不是就会失效，👉 [thread-lock-04](../../details/thread-lock-04.md)
5. 重新改成同一个对象上锁，👉 [thread-lock-05](../../details/thread-lock-05.md)

### 死锁问题

两个线程互相等待对方释放锁，结果谁都动不了。👉 [thread-lock-dead](../../details/thread-lock-dead.md)

| 操作              | 是否释放锁 | 线程状态          | 风险等级   |
| --------------- | ----- | ------------- | ------ |
| sleep()/yield() | ❌     | TIMED_WAITING | ⭐⭐     |
| suspend()       | ❌     | SUSPENDED     | ⚠️⚠️⚠️ |
| wait()          | ✅     | WAITING       | ⭐      |

### 懒汉式单例模式安全问题

1. 两个线程同时创建单例，结果创建了**两个不同的对象**，破坏了单例。👉 [thread-singleton-01](../../details/thread-singleton-01.md)
2. 采用类锁：👉 [thread-singleton-02](../../details/thread-singleton-02.md)
3. 采用实例锁：👉 [thread-singleton-03](../../details/thread-singleton-03.md)
### Lock

1. `Lock`是接口，从JDK5开始引入的。  
2. `Lock`接口下有一个实现类：可重入锁（`ReentrantLock`）  
3. `Lock` 和 `synchronized` 哪个好？`Lock`更好。为什么？因为更加灵活。  
4. 使用`Lock`解决懒汉式单例模式安全问题：👉 [thread-lock-lock](../../details/thread-lock-lock.md)

---
## 用户线程与守护线程

### 概念与案例

| 特性 | 用户线程（User Thread） | 守护线程（Daemon Thread） |
| :--- | :--- | :--- |
| **别名** | 工作线程 | - |
| **核心作用** | 执行业务逻辑 | 为用户线程提供辅助服务 |
| **生命周期** | 当线程任务执行完成时终止，或可通过通知方式主动结束 | 随用户线程终止而自动结束，当所有用户线程结束时立即销毁 |
| **JVM退出影响** | JVM会等待所有用户线程执行完毕才退出 | 不会阻止JVM退出 |
| **设置方法** | - | `thread.setDaemon(true)` |
| **典型应用** | 业务逻辑处理 | 垃圾回收线程（GC Thread）、日志监控等后台服务 |

* 典型守护线程示例——**垃圾回收线程（GC Thread）​**，持续监控内存状态，用户线程运行时在后台自动回收资源。
* 案例1：堂吉诃德的冒险 [thread-deamon-01](../../details/thread-deamon-01.md)
* 案例2：王宝强和马蓉的故事 [thread-deamon-02](../../details/thread-deamon-02.md)
* 案例3：没有故事背景的简单案例 [thread-deamon-03](../../details/thread-deamon-03.md)

### 定时器

- `java.util.Timer`：定时器，本质是一个线程
    - `Timer()`：创建用户线程定时器
    * `Timer(boolean isDaemon)`：`isDaemon=true`创建守护线程定时器
    * `timer.schedule(task, firstTime, interval)`：安排定时任务
        - `task`：要执行的任务（TimerTask子类）
        - `firstTime`：首次执行时间
        - `interval`：重复执行间隔（毫秒）
- `java.util.TimerTask`：定时任务，需要继承并实现`run()`方法
* 👉 [thread-timer](../../details/thread-timer.md)

---
## 线程的生命周期

### 六种状态

![[../../assets/threading-drawing|1000]]
* 新建状态（NEW）
* 就绪状态（RUNNABLE）
* 运行状态（RUNNABLE）
* 超时等待状态（TIMED_WAITING）：有时长限定的等待
* 等待状态（WAITING）：无期限的等待，没有时长限定
* 阻塞状态（BLOCKED）：遇到锁之后变成阻塞状态
* 死亡状态（TERMINATED）

| 方法            | 作用场景   | 备注                             |
| ------------- | ------ | ------------------------------ |
| `start()`     | 启动新线程  | 异步执行`run()`中的逻辑                |
| `run()`       | 定义线程任务 | 直接调用相当于普通方法                    |
| `sleep()`     | 线程暂停   | 不释放锁，可能抛`InterruptedException` |
| `interrupt()` | 请求终止线程 | 需线程自身检查中断标志                    |

使用`getState()`一个查看 java 线程状态的案例：👉 [thread-state](../../details/thread-state.md)

### sleep(静态方法)

* `static void sleep(long millis)`：静态方法，没有返回值，参数是一个毫秒。1秒 = 1000毫秒
* `sleep`让当前线程进入休眠，也就是让当前线程**放弃占有的CPU**时间片，让其进入阻塞状态。
* `sleep`休眠时**不释放锁**。
* `run`方法在方法重写的时候，不能在方法声明位置使用 `throws` 抛出异常！
* 简单的案例：👉 [thread-sleep-01](../../details/thread-sleep-01.md)
* (🌟面试题) 创建的线程对象执行sleep，是创建的线程去sleep还是当前线程sleep：👉 [thread-sleep-02](../../details/thread-sleep-02.md)

### interrupt(实例方法)

* 中断一个线程的睡眠：👉 [thread-interrupt-01](../../details/thread-interrupt-01.md)
* 👉 [thread-interrupt-02](../../details/thread-interrupt-02.md)
### stop(已经废弃)

* `stop`不能成功终止线程：👉 [thread-stop-01](../../details/thread-stop-01.md)
* 正确的方法需要我们手动使用flag进行判断：👉 [thread-stop-02](../../details/thread-stop-02.md)

### join(实例方法)
- **作用**：强制优先执行插队线程
- **特点**：插队线程必须完全执行完毕；调用线程会等待插队线程完成
- **使用场景**：需要确保某个线程优先完成时
* 🌟join也可以指定join的时间，就是只把CPU让给某个进程最多一段时间：👉 [thread-join-01](../../details/thread-join-01.md)
* 练习：👉 [thread-join-02](../../details/thread-join-02.md)

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
* 线程优先级默认是5，最低是1，最高是10。
* 👉 [thread-priority](../../details/thread-priority.md)

### yield(让位)
- **作用**：让出CPU资源，允许其他线程执行
- **特点**：礼让时间不确定；不保证礼让一定成功
- **使用场景**：当线程不需要占用全部CPU资源时
- [thread-yield-01](../../details/thread-yield-01.md)
- [thread-yield-02](../../details/thread-yield-02.md)

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
    //  System.out.println(Thread.currentThread().getName() + "启动");  
    while(true){  
      synchronized(obj){  
        while(currentThreadId != threadId){  
          // System.out.println(Thread.currentThread().getName() + "等待");  
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