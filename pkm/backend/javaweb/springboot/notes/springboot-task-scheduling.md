# Spring Task 定时任务

---

## 定时任务技术概述

**Spring Task 是 Spring 框架内置的轻量级定时任务工具，配置简单，适合中小型项目或对定时任务需求不复杂的场景，Spring Boot 的自动配置进一步简化了使用。若任务调度需求较为复杂，可选用以下专业框架：**

+ **Quartz**：功能全面，支持复杂调度策略和高可用性，适用于大型企业级应用。**
+ **XXL-JOB**：提供友好的 Web 管理界面和丰富的告警机制，适合需要可视化调度与高可用的中小型企业。**
+ **Elastic-Job**：支持任务分片与弹性伸缩，适用于需高度扩展和分布式调度的大型分布式系统。选择建议**

+ **需复杂调度和高可用时，选**Quartz**。**
+ **需要易用的管理界面和分布式调度支持，选**XXL-JOB**。**
+ **若已基于 ZooKeeper 且需弹性扩缩容与分片，选**Elastic-Job**。**

---

## 什么是定时任务

**定时任务（Scheduled Task）指在预先设定的时间或按指定周期自动执行的任务。它广泛应用于各类系统中，用于自动化完成重复性或定期维护性工作，例如**数据备份、日志清理、生成报表、定时发送邮件、系统监控**等。主要特点**

+ **自动化**：无需人工干预，降低操作负担与出错风险。**
+ **周期性**：可按固定间隔（如每小时）或在特定时刻（如每日凌晨）执行。**
+ **可配置性**：执行时间和频率可通过配置或代码灵活调整。**
+ **高可用性**（分布式场景）：支持集群与故障转移，保障任务可靠执行。**

---

## Spring Task实现定时任务

**不需要引入任何依赖，只要是 springboot 项目即可。**第一步：编写定时任务类**

```java
package com.jkweilai.demo.task;

import org.springframework.scheduling.annotation.Scheduled;
import org.springframework.stereotype.Component;

import java.time.LocalDateTime;

// 定时任务类纳入IoC容器的管理。
@Component
public class MyTask {

    // 指定定时任务：每隔5秒执行一次任务，以固定周期方式执行。
    @Scheduled(fixedRate = 5000)
    public void doTask() {
        System.out.println(LocalDateTime.now());
    }
}

```

**第二步：在定时任务类上或主入口类上添加注解**

```java
package com.jkweilai.demo;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.scheduling.annotation.EnableScheduling;

@SpringBootApplication
// 主入口类上添加该注解，或在定时任务类上添加，表示启用定时任务。
@EnableScheduling
public class SpringTaskApplication {

    public static void main(String[] args) {
        SpringApplication.run(SpringTaskApplication.class, args);
    }

}

```

---

## 定时规则详解

通过这个注解`@Scheduled`的属性来指定定时规则，主要包括：

+ **fixedRate 与 fixedRateString：周期性执行任务。如果上一次任务执行时长超过了设定的周期时间，上次任务结束后，下次任务立即开始。**
+ **fixedDelay 与 fixedDelayString：周期性执行任务。不管上一次任务耗时多久，任务结束后都会经过一个固定的时间周期，再开启下一次任务。**
+ **initialDelay 与 initialDelayString：第一次执行任务时的延迟时间。**
+ **timeUnit：用来指定时间单位。**
+ **zone：用来指定时区。**
+ **cron：**Cron 表达式**### **fixedRate 与 fixedRateString**
按照固定周期执行任务。

注意： fixedRate：如果上一次任务的执行时间已经超过了设置的间隔时间，则在上一次任务结束之后立即开启下一次任务

```java
import org.springframework.scheduling.annotation.Scheduled;
import org.springframework.stereotype.Component;

import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;
import java.util.concurrent.TimeUnit;

@Component
public class MyTask {

    // 如果任务的执行总时长超过5秒，则当前任务结束后，下次任务立即开始。
    @Scheduled(fixedRate = 5000)
    public void doTask() {
        LocalDateTime begin = LocalDateTime.now();
        DateTimeFormatter dtf = DateTimeFormatter.ofPattern("HH:mm:ss");
        System.out.println("任务开始：" + dtf.format(begin));
        try {
            TimeUnit.SECONDS.sleep(10);
        } catch (InterruptedException e) {
            throw new RuntimeException(e);
        }
        LocalDateTime end = LocalDateTime.now();
        System.out.println("任务结束：" + dtf.format(end));
    }
}

```

fixedRateString属性支持字符串类型的属性值，这种方式主要便于在配置文件中达到可配置的效果：

```properties
task.fixed-rate-string=5000
```

在java程序中这样取出配置：

```java
import org.springframework.scheduling.annotation.Scheduled;
import org.springframework.stereotype.Component;

import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;
import java.util.concurrent.TimeUnit;

@Component
public class MyTask {

    @Scheduled(fixedRateString = "${task.fixed-rate-string}")
    public void doTask() {
        LocalDateTime begin = LocalDateTime.now();
        DateTimeFormatter dtf = DateTimeFormatter.ofPattern("HH:mm:ss");
        System.out.println("任务开始：" + dtf.format(begin));
        try {
            TimeUnit.SECONDS.sleep(10);
        } catch (InterruptedException e) {
            throw new RuntimeException(e);
        }
        LocalDateTime end = LocalDateTime.now();
        System.out.println("任务结束：" + dtf.format(end));
    }
}

```

### fixedDelay 与 fixedDelayString

`fixedDelay`也是用来设置周期性的执行任务。

但要注意：这个配置的效果是，不管上一次任务耗时多久，下一次任务一定是在上一次任务结束之后再经过一个固定的时间才开启。

```java
import org.springframework.scheduling.annotation.Scheduled;
import org.springframework.stereotype.Component;

import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;
import java.util.concurrent.TimeUnit;

@Component
public class MyTask {

    @Scheduled(fixedDelay = 5000)
    public void doTask() {
        LocalDateTime begin = LocalDateTime.now();
        DateTimeFormatter dtf = DateTimeFormatter.ofPattern("HH:mm:ss");
        System.out.println("任务开始：" + dtf.format(begin));
        try {
            TimeUnit.SECONDS.sleep(10);
        } catch (InterruptedException e) {
            throw new RuntimeException(e);
        }
        LocalDateTime end = LocalDateTime.now();
        System.out.println("任务结束：" + dtf.format(end));
    }
}

```

`fixedDelayString`同样是为了支持可配置。

### **initialDelay 与 initialDelayString**

指定任务首次执行前的初始延迟时间（以毫秒为单位）

如果你希望在应用启动之后过 10 秒开始执行某个任务，并且要求每隔 1 秒执行一次，则需要这样配置：

```java
import org.springframework.scheduling.annotation.Scheduled;
import org.springframework.stereotype.Component;

import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;

@Component
public class MyTask {

    @Scheduled(initialDelay = 10 * 1000, fixedRate = 1000)
    public void doTask() {
        LocalDateTime begin = LocalDateTime.now();
        DateTimeFormatter dtf = DateTimeFormatter.ofPattern("HH:mm:ss");
        System.out.println("任务执行：" + dtf.format(begin));
    }
}

```

### timeUnit

用来指定时间单位。

```java
import org.springframework.scheduling.annotation.Scheduled;
import org.springframework.stereotype.Component;

import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;
import java.util.concurrent.TimeUnit;

@Component
public class MyTask {

    @Scheduled(initialDelay = 10, fixedRate = 1, timeUnit = TimeUnit.SECONDS)
    public void doTask() {
        LocalDateTime begin = LocalDateTime.now();
        DateTimeFormatter dtf = DateTimeFormatter.ofPattern("HH:mm:ss");
        System.out.println("任务执行：" + dtf.format(begin));
    }
}

```

以上表示以**秒**为单位，第一次任务执行是在应用启动 10 秒之后开始，然后每间隔1 秒执行一次。

### zone

用来指定时区。默认使用服务器所在时区。

通过以下代码可以获取时区列表：

```java
ZoneId.getAvailableZoneIds().forEach(System.out::println);
```

**中国的常用时区：**

+ **Asia/Chongqing**
+ **Asia/Shanghai如何使用：zone 一般在使用 cron 表达式的时候才能看出效果。**

```java
@Scheduled(zone = "Asia/Shanghai")
```

### cron表达式

cron 表达式用来定义了任务的执行时间规则。

cron 表达式由**六个**或**七个**字段组成，每个字段之间用**空格分隔**。格式如下：

```plain
秒 分 时 日 月 星期几 [年]
```

**字段说明：**

+ 秒：0-59
+ 分：0-59
+ 时：0-23
+ 日：1-31
+ 月：1-12 或 JAN-DEC
+ 星期几：0-7 或 SUN-SAT（其中 0 和 7 都表示星期日）
+ 年（可选）：1970-2099

**常见通配符：**

+**   表示所有可能的值。
+ **,**   表示列出的值。
+ **-**   表示一个值的范围。
+ **/**   表示增量。
+ **?**   表示不指定值（只能用于日期和星期几字段）。
+ **L**   表示最后一天（日期字段）或最后一个（星期几字段）。
    - 日字段上：表示月的最后一天
    - 周字段上：`5L`表示月的最后一个星期五
+ **W**   表示离指定日期最近的工作日。
+ **#**表示每月的第几个星期几。（用在星期几字段上）
    - `6#3`表示每月第 3 个星期六

**请理解下列的cron表达式：**

+ `30 * * * * ?`       每分钟的第30秒执行
+ `0 0 14 * * ?`      每天的14:00执行
+ `0 0 14 ? * MON`      每周一的14:00执行
+ `59 59 23 L * ?`        每月的最后一天的23:59:59执行
+ `0 30 * * * ?`      每小时的第30分钟执行
+ `0 0 0,12 * * ?`     每天的00:00和12:00执行
+ `0 0 0-3 * * ?`       每天的00:00到03:00之间的每小时执行
+ `0 0/5 * * * ?`        每天的00:00开始，每隔5分钟执行一次
+ `0 0 9 1W * ?`       每月的第一个工作日的09:00执行
+ `0 0 17 ? * 5L`       每月的最后一个星期五的17:00执行
+ `0 0 12 ? * WED#2`      每月的第二个星期三的12:00执行
+ `0 0 10 15 * ?`      每月的第15天的10:00执行
+ `0 0 14 ? * MON-FRI`     每周的星期一到星期五的14:00执行
+ `0 0 12 1,15 * ?`      每月的1号和15号的12:00执行
+ `0 0 0 1 1 ?`      每年的1月1日的00:00执行
+ `0 0 17 LW * ?`       每月的最后一个工作日的17:00执行
+ `0 0 10 ? * MON#3`     每月的第三个星期一的10:00执行
+ `0 0 9 10 * ?`      每月的第10天的09:00执行
+ `0 0 16 ? * TUE#L`    每月的最后一个星期二的16:00执行
+ `0 0 12-14 15 * ?`    每月的第15天的12:00到14:00之间的每小时执行

**下面的 Cron 表达式效果是：每周一凌晨 3 点执行。并指定上海时区。**

```java
@Scheduled(cron = "0 0 3 * * 1", zone = "Asia/Shanghai")
```

