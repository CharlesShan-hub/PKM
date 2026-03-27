# Java中实现任务调度的主要方式

---

## Timer和TimerTask（单线程本质）

```java
import java.util.Timer;
import java.util.TimerTask;

public class BasicScheduler {
    public static void main(String[] args) {
        Timer timer = new Timer();
        
        // 延迟1秒后执行，只执行一次
        timer.schedule(new TimerTask() {
            @Override
            public void run() {
                System.out.println("执行一次任务 - " + new Date());
            }
        }, 1000);
        
        // 延迟2秒后执行，之后每隔3秒重复执行
        timer.scheduleAtFixedRate(new TimerTask() {
            @Override
            public void run() {
                System.out.println("重复执行任务 - " + new Date());
            }
        }, 2000, 3000);
    }
}
```

**缺点**：功能简单，不适合复杂调度需求，并且Timer底层执行任务是单线程的本质。

**Timer的单线程本质：**

1. 内部只有一个线程（名为"Timer-0"的线程）
2. 所有任务放入优先队列，按执行时间排序
3. 执行流程：

```java
while (true) {
    TimerTask task = queue.poll(); // 取最早的任务
    if (task != null) {
        task.run(); // 同步执行（阻塞后续任务）
    }
}
```

可以编写程序测试一下，给排在前面的任务添加阻塞代码，观察执行结果：

```java
// 一个Timer对象
Timer timer = new Timer();
// 任务1
timer.schedule(new TimerTask() {
    @Override
    public void run() {
        System.out.println("阻塞开始" + new Date());
        // 阻塞
        try {
            Thread.sleep(3000);
        } catch (InterruptedException e) {
            throw new RuntimeException(e);
        }
        System.out.println("阻塞结束" + new Date());
    }
}, 1000);
// 任务2
timer.schedule(new TimerTask() {
    @Override
    public void run() {
        System.out.println("普通任务" + new Date());
    }
}, 1000);
```

执行结果说明了Timer本质上是单线程的方式：

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1744637909072-461d28c0-c910-4276-826f-31ba411150b8.png" width="441" title="" crop="0,0,1,1" id="ua4e6b97e" class="ne-image" style="font-size: 16px">

---

## ScheduledExecutorService（并发方式）

```java
import java.util.concurrent.Executors;
import java.util.concurrent.ScheduledExecutorService;
import java.util.concurrent.TimeUnit;

public class ExecutorScheduler {
    public static void main(String[] args) {
        // ExecutorService 是JUC包提供的线程池
        // ScheduledExecutorService 是JUC包提供的专门负责任务调度的线程池（ScheduledExecutorService 是 ExecutorService的子类。）
        ScheduledExecutorService executor = Executors.newScheduledThreadPool(2);
        
        // 延迟3秒后执行
        executor.schedule(() -> {
            System.out.println("延迟执行任务 - " + new Date());
        }, 3, TimeUnit.SECONDS);
        
        // 延迟5秒后执行，之后每隔2秒重复执行
        executor.scheduleAtFixedRate(() -> {
            System.out.println("定期执行任务 - " + new Date());
        }, 5, 2, TimeUnit.SECONDS);
    }
}
```

**优点**：线程池管理，更灵活，功能更强大。

编写程序测试一下，看看`ScheduleExecutorService`多任务处理时是不是真正的异步：

```java
ScheduledExecutorService executor = Executors.newScheduledThreadPool(2);

// 任务1
executor.schedule(() -> {
    System.out.println("阻塞任务开始：" + new Date());
    try {
        Thread.sleep(3000);
    } catch (InterruptedException e) {
        throw new RuntimeException(e);
    }
    System.out.println("阻塞任务结束：" + new Date());
}, 1, TimeUnit.SECONDS);

// 任务2
executor.schedule(() -> {
    System.out.println("普通任务：" + new Date());
}, 1, TimeUnit.SECONDS);
```

执行结果如下：

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1744638342122-740e935c-6468-495d-b5d5-01e2574c074e.png" width="503" title="" crop="0,0,1,1" id="u734c191e" class="ne-image" style="font-size: 16px">

`**Timer**`**和**`**ScheduledExecutorService**`**的区别：**

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1744638024854-6f57fdaf-1696-42cc-a3a1-47a102a8d067.png" width="615" title="" crop="0,0,1,1" id="ueebaa57d" class="ne-image" style="font-size: 16px">

---

## Spring框架的@Scheduled注解（Spring项目常用）

```java
import org.springframework.scheduling.annotation.EnableScheduling;
import org.springframework.scheduling.annotation.Scheduled;
import org.springframework.stereotype.Component;

import java.util.Date;

@Component
@EnableScheduling
public class SpringScheduler {
    
    // 每5秒执行一次
    @Scheduled(fixedRate = 5000)
    public void fixedRateTask() {
        System.out.println("固定频率任务 - " + new Date());
    }
    
    // 每天上午10:15执行
    @Scheduled(cron = "0 15 10 * * ?") // cron表达式：定义任务执行时间规则的字符串格式
    public void cronTask() {
        System.out.println("Cron表达式任务 - " + new Date());
    }
}
```

需要在Spring配置类上添加`@EnableScheduling`注解启用调度功能。

`@Scheduled`默认是同步执行，如果要异步执行需要额外添加 `@Async`注解。

---

## Quartz框架（企业级调度）

Quartz是一个功能强大的开源作业调度库，支持复杂的调度需求。但在近些年的统计数据来看，Quartz框架使用的越来越少了。

**使用量下降的原因：**

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1744639792374-9e4470e7-f384-4d11-bd25-e9bf4d4f777a.png" width="765" title="" crop="0,0,1,1" id="u35f21fff" class="ne-image" style="font-size: 16px">

