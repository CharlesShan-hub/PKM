
```java
package ex_thread;

public class Master {
  public static void main(String[] args) {
    //Cat cat = new Cat();
    //Thread thread = new Thread(cat);
    //thread.start();
    Thread cat = new Thread(new Cat());
    cat.start();
  }
}

class Cat implements Runnable {
  @Override
  public void run() {
    for(int i=0; i<5; i++) {
      System.out.println("喵喵 "+Thread.currentThread().getName());
      ThraadUtils.sleep(100);
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
