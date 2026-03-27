# Spring的入门程序

---

## Spring 的官方地址

官网地址：[https://spring.io/](https://spring.io/)，从这里你可以找到官方指南。

打开Spring官网后，可以看到Spring Framework，以及通过Spring Framework衍生的其它框架：

![](https://cdn.nlark.com/yuque/0/2022/png/21376908/1663749081947-b895cb4e-b7f6-4120-a1fe-a14651044847.png)

---

## Spring的jar文件

![](https://cdn.nlark.com/yuque/0/2025/png/21376908/1763645880150-75b14f50-e64f-4260-8267-12050cfb0de5.png)

以上是 Spring Framework 的 jar 包，可以看到有 20+个。以前的开发是需要下载这些 jar 包的，需要什么功能就下载对应的 jar 包，放到项目当中，现在有 Maven，方便多了，不需要下载 jar 包了。只需要引入 GAV 坐标即可。

**了解一下重点 jar 包：**

| **模块 JAR 包** | **主要职责** | **概括** |
| --- | --- | --- |
| **spring-core** | IoC 容器基础实现 | 框架的**心脏**，提供最基础的依赖注入功能 |
| **spring-beans** | Bean 工厂与装配 | 负责**创建和管理**应用中的所有对象（Bean） |
| **spring-context** | 应用上下文与企业服务 | 在核心容器之上，提供**事件、国际化**等企业级功能 |
| **spring-aop** | 面向切面编程 | 将**事务、日志**等横切关注点从业务代码中分离出来 |
| **spring-jdbc** | JDBC 抽象与简化 | **大幅简化**传统的 JDBC 冗长编码 |
| **spring-tx** | 事务管理 | 提供**声明式事务**控制，保证数据操作的原子性 |
| **spring-orm** | ORM 框架集成 | 无缝集成 **Hibernate、JPA** 等主流持久层框架 |
| **spring-web** | Web 开发基础 | 为 **Web MVC 和 WebFlux** 提供共用的底层支持 |
| **spring-webmvc** | 同步 Web 框架 | **基于 Servlet API** 的传统 MVC 模式 Web 框架 |
| **spring-webflux** | 异步 Web 框架 | **响应式、非阻塞**的现代 Web 框架，适合高并发场景 |
| **spring-test** | 测试框架支持 | 提供对 **Spring 环境集成测试**的强大支持 |

---

## 第一个Spring程序

**前期准备**：

+ 打开IDEA创建Empty Project：spring
+ 设置JDK 版本及编译器版本
+ 设置IDEA的Maven：关联自己的maven
+ 在空的工程spring中创建第一个模块（普通的 Java Maven 模块）：spring-001-first

### 添加spring context依赖

```xml
<dependency>
    <groupId>org.springframework</groupId>
    <artifactId>spring-context</artifactId>
    <version>6.2.13</version>
</dependency>
```

****注意：打包方式jar。****

当加入spring context的依赖之后，会关联引入其他依赖：

![](https://cdn.nlark.com/yuque/0/2025/png/21376908/1763649527180-d0d3dc0c-3b6a-428c-92a1-2c579820ba1c.png)

### 添加junit5依赖

```xml
<dependency>
    <groupId>org.junit.jupiter</groupId>
    <artifactId>junit-jupiter-api</artifactId>
    <version>5.11.0</version>
    <scope>test</scope>
</dependency>
```

### 定义bean

```java
package com.jkweilai.spring.bean;

public class User {
}
```

### 编写spring的配置文件

beans.xml。**该文件放在类的根路径下**。

![](https://cdn.nlark.com/yuque/0/2022/png/21376908/1663816617460-ee35243c-fddc-4771-af28-0017f8af2ab5.png)

配置文件中进行bean的配置。

```xml
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
       xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
       xsi:schemaLocation="http://www.springframework.org/schema/beans http://www.springframework.org/schema/beans/spring-beans.xsd">
    
  <bean id="userBean" class="com.jkweilai.spring.bean.User"></bean>
  
</beans>
```

bean的id和class属性：

+ ****id属性：代表对象的唯一标识。可以看做一个人的身份证号。****
+ ****class属性：用来指定要创建的java对象的类名，这个类名必须是全限定类名（带包名）。****

### 编写测试程序

```java
package com.jkweilai.spring.test;

import org.junit.jupiter.api.Test;
import org.springframework.context.ApplicationContext;
import org.springframework.context.support.ClassPathXmlApplicationContext;

public class SpringTest {

    @Test
    public void testFirst(){
        // 初始化Spring容器上下文（解析beans.xml文件，创建所有的bean对象）
        ApplicationContext applicationContext = new ClassPathXmlApplicationContext("beans.xml");
        // 根据id获取bean对象
        Object userBean = applicationContext.getBean("userBean");
        System.out.println(userBean);
    }
}

```

运行结果：

![](https://cdn.nlark.com/yuque/0/2025/png/21376908/1763650025240-e128f903-3ae4-4ee8-8b78-6b28565bf228.png)

---

## 第一个Spring程序详细剖析

### bean标签的id属性可以重复吗？

```java
package com.jkweilai.spring.bean;

public class Vip {
}

```

```xml
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
       xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
       xsi:schemaLocation="http://www.springframework.org/schema/beans http://www.springframework.org/schema/beans/spring-beans.xsd">

    <bean id="userBean" class="com.jkweilai.spring.bean.User"/>
    <bean id="userBean" class="com.jkweilai.spring.bean.Vip"/>
</beans>
```

****通过测试得出：在spring的配置文件中id是不能重名。****

### 底层是怎么创建对象的，是通过反射机制调用无参数构造方法吗？

```java
package com.jkweilai.spring.bean;

public class User {
    public User() {
        System.out.println("User的无参数构造方法执行");
    }
}

```

在User类中添加无参数构造方法。

****通过测试得知：创建对象时确实调用了无参数构造方法。****

如果提供一个有参数构造方法，不提供无参数构造方法会怎样呢？

```java
package com.jkweilai.spring.bean;

public class User {
    /*public User() {
        System.out.println("User的无参数构造方法执行");
    }*/

    public User(String name){
        System.out.println("User的有参数构造方法执行");
    }
}

```

****通过测试得知：spring是通过调用类的无参数构造方法来创建对象的，所以要想让spring给你创建对象，必须保证无参数构造方法是存在的。****

Spring是如何创建对象的呢？原理是什么？

```java
// dom4j解析beans.xml文件，从中获取class的全限定类名
// 通过反射机制调用无参数构造方法创建对象
Class clazz = Class.forName("com.jkweilai.spring.bean.User");
Object obj = clazz.newInstance();
```

### 把创建好的对象存储到一个什么样的数据结构当中了呢？

![](https://cdn.nlark.com/yuque/0/2022/png/21376908/1663829973365-59ca2f4c-4d81-471f-8e4c-aa272f8c2b81.png)

### spring配置文件的名字必须叫做beans.xml吗？

```java
ApplicationContext applicationContext = new ClassPathXmlApplicationContext("beans.xml");
```

通过以上的java代码可以看出，这个spring配置文件名字是我们负责提供的，显然spring配置文件的名字是随意的。

### 像这样的beans.xml文件可以有多个吗？

再创建一个spring配置文件，起名：spring.xml

```xml
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
       xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
       xsi:schemaLocation="http://www.springframework.org/schema/beans http://www.springframework.org/schema/beans/spring-beans.xsd">
    <bean id="vipBean" class="com.jkweilai.spring.bean.Vip"/>
</beans>
```

```java
package com.jkweilai.spring.test;

import org.junit.jupiter.api.Test;
import org.springframework.context.ApplicationContext;
import org.springframework.context.support.ClassPathXmlApplicationContext;

public class SpringTest {

    @Test
    public void testFirst(){
        // 初始化Spring容器上下文（解析beans.xml文件，创建所有的bean对象）
        ApplicationContext applicationContext = new ClassPathXmlApplicationContext("beans.xml","spring.xml");

        // 根据id获取bean对象
        Object userBean = applicationContext.getBean("userBean");
        Object vipBean = applicationContext.getBean("vipBean");

        System.out.println(userBean);
        System.out.println(vipBean);
    }
}

```

通过测试得知，spring的配置文件可以有多个，在ClassPathXmlApplicationContext构造方法的参数上传递文件路径即可。这是为什么呢？通过源码可以看到：

![](https://cdn.nlark.com/yuque/0/2022/png/21376908/1663830614508-d00ecc07-5b51-4d2d-bc1d-8f2cb4f0c785.png)

### 在配置文件中配置的类必须是自定义的吗，可以使用JDK中的类吗，例如：java.util.Date？

```xml
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
       xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
       xsi:schemaLocation="http://www.springframework.org/schema/beans http://www.springframework.org/schema/beans/spring-beans.xsd">

    <bean id="userBean" class="com.jkweilai.spring.bean.User"/>
    <!--<bean id="userBean" class="com.jkweilai.spring.bean.Vip"/>-->

    <bean id="dateBean" class="java.util.Date"/>
</beans>
```

通过测试得知，在spring配置文件中配置的bean可以任意类，只要这个类不是抽象的，并且提供了无参数构造方法。

### getBean()方法调用时，如果指定的id不存在会怎样？

![](https://cdn.nlark.com/yuque/0/2022/png/21376908/1663831841228-eda809d8-3e51-4b08-913c-76ff78efae1f.png)

运行测试程序：

![](https://cdn.nlark.com/yuque/0/2025/png/21376908/1763650804850-03cc33c1-dcf0-40eb-b07a-d816d6dad4b8.png)

通过测试得知，当id不存在的时候，会出现异常。

### getBean()方法返回的类型是Object，如果访问子类的特有属性和方法时，还需要向下转型，有其它办法可以解决这个问题吗？

```java
User user = applicationContext.getBean("userBean", User.class);
```

### ClassPathXmlApplicationContext是从类路径中加载配置文件，如果没有在类路径当中，又应该如何加载配置文件呢？

```xml
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
       xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
       xsi:schemaLocation="http://www.springframework.org/schema/beans http://www.springframework.org/schema/beans/spring-beans.xsd">
    <bean id="vipBean2" class="com.jkweilai.spring.bean.Vip"/>
</beans>
```

```java
ApplicationContext applicationContext2 = new FileSystemXmlApplicationContext("d:/spring.xml");
Vip vip = applicationContext2.getBean("vipBean2", Vip.class);
System.out.println(vip);
```

没有在类路径中的话，需要使用FileSystemXmlApplicationContext类进行加载配置文件。

这种方式较少用。一般都是将配置文件放到类路径当中，这样可移植性更强。

### ApplicationContext的超级父接口BeanFactory。

```java
BeanFactory beanFactory = new ClassPathXmlApplicationContext("spring.xml");
Object vipBean = beanFactory.getBean("vipBean");
System.out.println(vipBean);
```

BeanFactory是Spring容器的超级接口。ApplicationContext是BeanFactory的子接口。

---

## Spring 集成 logback 日志框架

SpringBoot 框架默认集成的是 logback 日志框架。但单纯只用 Spring 框架的时候，它是没有集成任何日志框架的，只是集成了日志门面。因此我们需要手动提供日志门面的实现，我们这里选择 logback 。

第一步：引入 logback 依赖

```xml
<dependency>
    <groupId>ch.qos.logback</groupId>
    <artifactId>logback-classic</artifactId>
    <version>1.4.14</version>
</dependency>
```

第二步：在类的根路径下提供 logback.xml 配置文件（文件名固定为：logback.xml，文件必须放到类根路径下。）

```xml
<?xml version="1.0" encoding="UTF-8"?>
<configuration>
    <!-- 定义日志输出格式 -->
    <property name="CONSOLE_LOG_PATTERN" value="%d{yyyy-MM-dd HH:mm:ss.SSS} [%thread] %-5level %logger{36} - %msg%n"/>
    <property name="FILE_LOG_PATTERN" value="%d{yyyy-MM-dd HH:mm:ss.SSS} [%thread] %-5level %logger{36} - %msg%n"/>

    <!-- 控制台输出 Appender -->
    <appender name="CONSOLE" class="ch.qos.logback.core.ConsoleAppender">
        <encoder>
            <pattern>${CONSOLE_LOG_PATTERN}</pattern>
            <charset>UTF-8</charset>
        </encoder>
    </appender>

    <!-- 文件输出 Appender -->
    <appender name="FILE" class="ch.qos.logback.core.rolling.RollingFileAppender">
        <!-- 日志文件路径 -->
        <file>logs/application.log</file>
        <encoder>
            <pattern>${FILE_LOG_PATTERN}</pattern>
            <charset>UTF-8</charset>
        </encoder>
        <!-- 滚动策略 -->
        <rollingPolicy class="ch.qos.logback.core.rolling.TimeBasedRollingPolicy">
            <!-- 按天归档 -->
            <fileNamePattern>logs/application.%d{yyyy-MM-dd}.%i.log</fileNamePattern>
            <timeBasedFileNamingAndTriggeringPolicy class="ch.qos.logback.core.rolling.SizeAndTimeBasedFNATP">
                <!-- 单个文件最大 100MB -->
                <maxFileSize>100MB</maxFileSize>
            </timeBasedFileNamingAndTriggeringPolicy>
            <!-- 保留 30 天的历史 -->
            <maxHistory>30</maxHistory>
        </rollingPolicy>
    </appender>

    <!-- 设置日志级别 -->
    <!-- Spring Framework 的日志级别 -->
    <logger name="org.springframework" level="INFO"/>
    <!-- 项目的包路径，设置为 DEBUG 以便调试 -->
    <logger name="com.jkweilai" level="DEBUG"/>

    <!-- 根日志配置 -->
    <root level="INFO">
        <appender-ref ref="CONSOLE"/>
        <appender-ref ref="FILE"/>
    </root>
</configuration>
```

日志级别

1. TRACE：最低级别，用于记录所有日志信息。
2. DEBUG：用于记录调试信息，便于开发人员进行调试，但不适用于生产环境。
3. INFO：用于记录生产环境下的信息，如启动信息、用户登录信息等。
4. WARN：用于记录警告信息，表示程序可能出现潜在问题。
5. ERROR：用于记录错误信息，表示程序已经出现错误，需要进行处理。
6. FATAL：最高级别，用于记录致命错误信息，表示程序已经无法继续执行，需要进行紧急处理。
7. OFF：关闭所有的日志记录。

第三步：使用日志框架

```java
Logger logger = LoggerFactory.getLogger(FirstSpringTest.class);
logger.info("我是一条日志消息");
```
