
```java
package ex_thread;

import java.util.concurrent.Callable;
import java.util.concurrent.ExecutionException;
import java.util.concurrent.FutureTask;

public class Master {
  public static void main(String[] args) throws ExecutionException, InterruptedException {
    //Callable<String> callable = new Cat();
    //FutureTask<String> futureTask = new FutureTask<>(callable);
    FutureTask<String> futureTask = new FutureTask<>(new Cat());
    Thread cat = new Thread(futureTask);
    cat.start();
    System.out.println(futureTask.get()); // 获取返回值
  }
}

class Cat implements Callable {
  @Override
  public String call() {
    for(int i=0; i<5; i++) {
      System.out.println("喵喵 "+Thread.currentThread().getName());
      ThraadUtils.sleep(100);
    }
    return "小猫跑走了";
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

//喵喵 Thread-0
//喵喵 Thread-0
//喵喵 Thread-0
//喵喵 Thread-0
//喵喵 Thread-0
//小猫跑走了
```
