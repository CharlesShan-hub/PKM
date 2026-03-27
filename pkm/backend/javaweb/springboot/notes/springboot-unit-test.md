# Spring Boot的单元测试

---

## 不使用单元测试怎么调用service

### 创建模块

使用脚手架创建sb3-06-test模块，不添加任何启动器：

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1764858731937-5eeb3907-ce7b-4144-8ef0-ab6893b79e81.png" width="334.4" title="" crop="0,0,1,1" id="ufff0d565" class="ne-image">

### 编写service

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1764858745928-2be537af-fd1c-4ddd-8392-e49fd0579dd9.png" width="225.6" title="" crop="0,0,1,1" id="u13581b5e" class="ne-image">

```java
package com.jkweilai.sb306test.service.impl;

import com.jkweilai.sb306test.service.UserService;
import org.springframework.stereotype.Service;

@Service("userService")
public class UserServiceImpl implements UserService {
    @Override
    public void save() {
        System.out.println("保存用户信息");
    }
}
```

### 直接在入口程序中调用service

```java
@SpringBootApplication
public class Sb306TestApplication {
    public static void main(String[] args) {
        ConfigurableApplicationContext applicationContext = SpringApplication.run(Sb306TestApplication.class, args);
        UserService userService = applicationContext.getBean("userService", UserService.class);
        userService.save();
    }
}
```

执行结果：

<img src="https://cdn.nlark.com/yuque/0/2024/png/21376908/1729581624703-aa5dfd5f-1a61-48a9-bce3-9d3d615913e5.png" width="252" title="" crop="0,0,1,1" id="ubd3998a7" class="ne-image">

这种方式就是手动获取Spring上下文对象`ConfigurableApplicationContext`，然后调用getBean方法从Spring容器中获取service对象，然后调用方法。

---

## 使用单元测试怎么调用service

### test-starter引入以及测试类编写

使用单元测试应该如何调用service对象上的方法呢？

在使用脚手架创建Spring Boot项目时，为我们生成了单元测试类，如下：

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1764858829335-de2fae33-630c-4d81-8a34-071382d88988.png" width="432" title="" crop="0,0,1,1" id="ue4d348db" class="ne-image">

当然，如果要使用单元测试，需要引入单元测试启动器，如果使用脚手架创建SpringBoot项目，这个test启动器会自动引入：

```xml
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-test</artifactId>
    <scope>test</scope>
</dependency>
```

### @SpringBootTest注解

`@SpringBootTest` 会创建一个完整的 Spring 应用程序上下文（Application Context），这个上下文包含了应用程序的所有组件和服务。以下是 `@SpringBootTest` 做的一些主要工作：

1. **创建 ApplicationContext**：
    - `@SpringBootTest` 使用 `SpringApplication` 的 `run()` 方法来启动一个 Spring Boot 应用程序上下文。这意味着它会加载应用程序的主配置类和其他相关的配置类。
2. **加载配置文件**：
    - 它会查找并加载默认的配置文件，如 `application.properties`
3. **自动配置**：
    - 如果应用程序依赖于 Spring Boot 的自动配置特性，`@SpringBootTest` 会确保这些自动配置生效。这意味着它会根据可用的类和bean来自动配置一些组件，如数据库连接、消息队列等。
4. **注入依赖**：
    - 使用 `@SpringBootTest` 创建的应用程序上下文允许你在测试类中使用 `@Autowired` 注入需要的 bean，就像在一个真实的 Spring Boot 应用程序中一样。

总的来说，`@SpringBootTest` 为你的测试提供了尽可能接近实际运行时环境的条件，这对于验证应用程序的行为非常有用。

### 注入service并调用

```java
@SpringBootTest
class Sb306TestApplicationTests {

    @Autowired
    private UserService userService;
    
    @Test
    void contextLoads() {
        userService.save();
    }

}
```

测试结果如下：

<img src="https://cdn.nlark.com/yuque/0/2024/png/21376908/1729582782987-88067365-fba6-4240-b704-b2f710a96647.png" width="274" title="" crop="0,0,1,1" id="u0febe674" class="ne-image">

