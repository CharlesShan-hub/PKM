
**案例说明**：创建一个守护线程定时器，从指定时间开始，每5秒打印一次当前时间和计数。
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
