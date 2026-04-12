继承`Thread`类
```java
package ex_thread;

public class Master {
  public static void main(String[] args) {
    Cat cat = new Cat();
    cat.start();
    for(int i=0; i<5; i++) {
      System.out.println("主人在撸猫");
      ThraadUtils.sleep(100);
    }
  }
}

class Cat extends Thread {
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

//主人在撸猫
//喵喵 Thread-0
//喵喵 Thread-0
//主人在撸猫
//喵喵 Thread-0
//主人在撸猫
//主人在撸猫
//喵喵 Thread-0
//喵喵 Thread-0
//主人在撸猫
```
