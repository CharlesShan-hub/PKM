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
