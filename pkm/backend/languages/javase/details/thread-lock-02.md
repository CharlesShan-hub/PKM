
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
