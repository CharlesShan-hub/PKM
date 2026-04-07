# Java中实现任务调度的主要方式

---

## Timer和TimerTask（单线程本质）

```java
package top.charles;  
  
import java.util.Date;  
import java.util.Timer;  
import java.util.TimerTask;  
  
public class TimerDemo {  
    public static void main(String[] args) {  
        Timer timer = new Timer();  
  
        // 延迟5秒后执行，只执行一次  
        timer.schedule(new TimerTask() {  
            @Override  
            public void run() {  
                System.out.println("执行一次任务 - " + new Date());  
            }  
        }, 5000);  
  
        // 延迟3秒后执行，之后每隔3秒重复执行  
        timer.scheduleAtFixedRate(new TimerTask() {  
            @Override  
            public void run() {  
                System.out.println("重复执行任务 - " + new Date());  
            }  
        }, 3000, 3000);  
    }  
}
```

```plaintext
定期执行任务 - Tue Apr 07 10:21:19 CST 2026
延迟执行任务 - Tue Apr 07 10:21:21 CST 2026
定期执行任务 - Tue Apr 07 10:21:22 CST 2026
```

**缺点**：功能简单，不适合复杂调度需求，并且`Timer`底层执行任务是**单线程**。

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

执行结果说明了Timer本质上是单线程的方式，可以看到阻塞开始后，重复执行的任务并没有如期执行：

```plaintext
重复执行任务 - Tue Apr 07 10:28:57 CST 2026
阻塞开始Tue Apr 07 10:28:59 CST 2026
阻塞结束Tue Apr 07 10:29:09 CST 2026
重复执行任务 - Tue Apr 07 10:29:09 CST 2026
重复执行任务 - Tue Apr 07 10:29:09 CST 2026
重复执行任务 - Tue Apr 07 10:29:09 CST 2026
重复执行任务 - Tue Apr 07 10:29:09 CST 2026
重复执行任务 - Tue Apr 07 10:29:12 CST 2026
```

---

## ScheduledExecutorService（并发方式）

```java
package top.charles;  
  
import java.util.Date;  
import java.util.concurrent.Executors;  
import java.util.concurrent.ScheduledExecutorService;  
import java.util.concurrent.TimeUnit;  
  
public class ScheduledExecutorServiceDemo {  
    public static void main(String[] args) {  
        // ExecutorService 是JUC包提供的线程池  
        // ScheduledExecutorService 是JUC包提供的专门负责任务调度的线程池（ScheduledExecutorService 是 ExecutorService的子类。）  
        ScheduledExecutorService executor = Executors.newScheduledThreadPool(2);  
  
        // 延迟5秒后执行  
        executor.schedule(() -> {  
            System.out.println("延迟执行任务 - " + new Date());  
        }, 5, TimeUnit.SECONDS);  
  
        // 延迟3秒后执行，之后每隔3秒重复执行  
        executor.scheduleAtFixedRate(() -> {  
            System.out.println("定期执行任务 - " + new Date());  
        }, 3, 3, TimeUnit.SECONDS);  
    }  
}
```

```plaintext
定期执行任务 - Tue Apr 07 10:30:26 CST 2026
延迟执行任务 - Tue Apr 07 10:30:28 CST 2026
定期执行任务 - Tue Apr 07 10:30:29 CST 2026
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

```plaintext
定期执行任务 - Tue Apr 07 10:32:09 CST 2026
阻塞任务开始：Tue Apr 07 10:32:11 CST 2026
定期执行任务 - Tue Apr 07 10:32:12 CST 2026
定期执行任务 - Tue Apr 07 10:32:15 CST 2026
定期执行任务 - Tue Apr 07 10:32:18 CST 2026
定期执行任务 - Tue Apr 07 10:32:21 CST 2026
阻塞任务结束：Tue Apr 07 10:32:21 CST 2026
定期执行任务 - Tue Apr 07 10:32:24 CST 2026
```

`Timer`和`ScheduledExecutorService`的区别：

|  特性   |      Timer      | ScheduledExecutorService |
| :---: | :-------------: | :----------------------: |
| 线程模型  |       单线程       |       线程池（真正的多线程）        |
| 阻塞影响  | 一个任务阻塞会延迟所有后续任务 |         各任务独立执行          |
| 时间准确性 |     受前序任务影响     |       严格准时（线程充足时）        |
| 异常影响  |   导致整个Timer崩溃   |         仅影响当前任务          |
| 任务隔离性 |        无        |           完全隔离           |

---

## Spring框架的@Scheduled注解（Spring项目常用）

```java
package com.example.demo;  
  
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
  
    // 每天上午11:10执行  
    @Scheduled(cron = "0 10 11 * * ?") // cron表达式：定义任务执行时间规则的字符串格式  
    public void cronTask() {  
        System.out.println("Cron表达式任务 - " + new Date());  
    }  
}
```

需要在Spring配置类上添加`@EnableScheduling`注解启用调度功能。

```plaintext
固定频率任务 - Tue Apr 07 11:09:55 CST 2026
Cron表达式任务 - Tue Apr 07 11:10:00 CST 2026
固定频率任务 - Tue Apr 07 11:10:00 CST 2026
```

`@Scheduled`默认是同步执行，如果要异步执行需要额外添加 `@Async`注解。

```java
@Async
@Scheduled(fixedRate = 5000)  
public void fixedRateTask() {  
    System.out.println("固定频率任务 - " + new Date());  
}
// 或者在内部的方法上加Async也可以
```

---

## Quartz框架（企业级调度）

Quartz是一个功能强大的开源作业调度库，支持复杂的调度需求。但在近些年的统计数据来看，Quartz框架使用的越来越少了。

使用量下降的原因：

| 因素 | 说明 | 替代方案 |
|------|------|----------|
| 轻量级需求增加 | 80%的定时任务场景变得简单 | Spring `@Scheduled`、ScheduledExecutorService |
| 云原生普及 | 云平台提供托管调度服务 | AWS EventBridge、Azure Scheduler、Kubernetes CronJob |
| 分布式需求 | 原生Quartz需要额外开发分布式支持 | Elastic-Job、XXL-JOB、PowerJob |
| 开发便捷性 | 配置复杂度较高 | 注解驱动的轻量级方案 |


