# SpringBoot 异步方法

---

## 异步方法的作用

**异步方法的作用是将耗时操作放到后台线程执行，避免阻塞主线程，提高系统吞吐量和响应速度。本质是让方法调用立即返回，实际执行交给线程池异步完成。**

1. **邮件/短信发送**→ “发邮件时不阻塞用户注册流程”**
2. **文件处理**→ “上传大文件后台处理，用户无需等待”**
3. **日志记录**→ “日志异步保存，不影响主业务性能”**
4. **数据同步**→ “跨系统数据同步在后台悄悄完成”**
5. **缓存预热**→ “启动时异步预热缓存，服务立即可用”核心就一句：任何“不需要立即知道结果”的耗时任务，都可以用异步方法优化体验。**

---

## 异步方法的实现步骤

### 启用异步支持

在主入口类上添加注解：`@EnableAsync`，这一步非常关键，这样异步方法注解 `@Async`才会生效。

```java
package com.jkweilai.demo;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.scheduling.annotation.EnableAsync;

@SpringBootApplication
@EnableAsync // 启用异步支持
public class SpringAsyncApplication {

    public static void main(String[] args) {
        SpringApplication.run(SpringAsyncApplication.class, args);
    }

}

```

### 配置线程池

执行异步方法时，需要新的线程，springboot 默认提供了一个简单的线程池，在实际开发中，我们通常手动配置线程池。

```java
package com.jkweilai.demo.config;

import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.scheduling.concurrent.ThreadPoolTaskExecutor;

import java.util.concurrent.Executor;
import java.util.concurrent.ThreadPoolExecutor;

@Configuration
public class AsyncConfig {

    /**
     * 默认线程池 - 用于通用异步任务
     */
    @Bean("taskExecutor")
    public Executor taskExecutor() {
        ThreadPoolTaskExecutor executor = new ThreadPoolTaskExecutor();
        // 核心线程数：线程池创建时初始化的线程数
        executor.setCorePoolSize(10);
        // 最大线程数：线程池最大的线程数，只有在缓冲队列满了之后才会申请超过核心线程数的线程
        executor.setMaxPoolSize(50);
        // 缓冲队列：用来缓冲执行任务的队列
        executor.setQueueCapacity(200);
        // 允许线程的空闲时间：当超过了核心线程之外的线程在空闲时间到达之后会被销毁
        executor.setKeepAliveSeconds(60);
        // 线程池名的前缀：设置好了之后可以方便我们定位处理任务所在的线程池
        executor.setThreadNamePrefix("async-task-");

        // 线程池对拒绝任务的处理策略
        // 当线程池"满了"（队列也满了）的时候，新来的任务怎么处理?
        // CallerRunsPolicy 表示“调用者运行”策略，让提交任务的线程（比如Tomcat的HTTP线程）自己去执行这个任务
        executor.setRejectedExecutionHandler(new ThreadPoolExecutor.CallerRunsPolicy());

        // 等待所有任务结束后再关闭线程池
        executor.setWaitForTasksToCompleteOnShutdown(true);
        // 等待时间：如果60秒了任务还没有完成，也会关闭线程池，避免一直等。等待时间可调整。
        executor.setAwaitTerminationSeconds(60);

        // 初始化线程池
        executor.initialize();
        return executor;
    }

    /**
     * 专用线程池 - 用于IO密集型任务
     */
    @Bean("ioTaskExecutor")
    public Executor iOTaskExecutor() {
        ThreadPoolTaskExecutor executor = new ThreadPoolTaskExecutor();
        // IO密集型任务大部分时间在等待（CPU空闲），多开线程可以让CPU在等待期间处理其他任务，提高总体利用率。
        executor.setCorePoolSize(20);      // IO密集型可设置更多线程
        executor.setMaxPoolSize(100);
        executor.setQueueCapacity(500);
        executor.setKeepAliveSeconds(30);
        executor.setThreadNamePrefix("async-io-");
        executor.setRejectedExecutionHandler(new ThreadPoolExecutor.CallerRunsPolicy());
        executor.initialize();
        return executor;
    }

    /**
     * 专用线程池 - 用于CPU密集型任务
     */
    @Bean("cpuTaskExecutor")
    public Executor cpuTaskExecutor() {
        ThreadPoolTaskExecutor executor = new ThreadPoolTaskExecutor();
        // CPU密集型线程数不宜过多，通常为CPU核数+1 （需要记住，为什么？有兴趣的可以查阅资料）
        int cpuCores = Runtime.getRuntime().availableProcessors();
        executor.setCorePoolSize(cpuCores + 1);
        executor.setMaxPoolSize(cpuCores * 2);
        executor.setQueueCapacity(100);
        executor.setThreadNamePrefix("async-cpu-");
        executor.setRejectedExecutionHandler(new ThreadPoolExecutor.AbortPolicy());
        executor.initialize();
        return executor;
    }
}
```

### 编写异步方法

```java
package com.jkweilai.demo.async;

import org.springframework.scheduling.annotation.Async;
import org.springframework.stereotype.Service;

import java.time.LocalDateTime;
import java.util.concurrent.TimeUnit;

@Service
public class AsyncService {

    // 指定异步方法，并且指定使用哪个线程池。
    @Async("taskExecutor")
    public void doTask(){
        System.out.println(Thread.currentThread().getName() + "开始处理任务：" + LocalDateTime.now());
        try {
            TimeUnit.SECONDS.sleep(10);
        } catch (InterruptedException e) {
            throw new RuntimeException(e);
        }
        System.out.println(Thread.currentThread().getName() + "处理任务完成：" + LocalDateTime.now());
    }
}
```

### 编写测试程序

```java
package com.jkweilai.demo;

import com.jkweilai.demo.async.AsyncService;
import jakarta.annotation.Resource;
import org.junit.jupiter.api.Test;
import org.springframework.boot.test.context.SpringBootTest;

@SpringBootTest
class SpringAsyncApplicationTests {

    @Resource
    private AsyncService asyncService;

    @Test
    void test() {
        asyncService.doTask();
        System.out.println("test end....");
    }

}

```

执行效果如下：

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1765200075661-99116326-9d77-44b7-91a3-a3fba8c413d7.png" width="471.2" title="" crop="0,0,1,1" id="ue4dc41cd" class="ne-image">

---

## 注意事项

1. **异步方法必须是 public 方法**
2. **同类内部调用异步方法不会生效**（因为基于代理）**
3. **建议为不同业务类型配置不同的线程池**
4. **生产环境一定要配置合理的线程池参数和拒绝策略**

