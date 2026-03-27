# Spring Boot核心注解

创建一个新的模块，来学习Spring Boot核心注解：

<img src="https://cdn.nlark.com/yuque/0/2024/png/21376908/1729564104331-5d4976ae-092d-405e-a94b-e69daaae31e6.png" width="252" title="" crop="0,0,1,1" id="ua417a324" class="ne-image">

只加入web启动器。

---

## @SpringBootApplication注解

Spring Boot的主入口程序被`@SpringBootApplication`注解标注，可见这个注解的重要性，查看它的源码：

<img src="https://cdn.nlark.com/yuque/0/2024/png/21376908/1729563192417-c03008ef-81f9-4741-ad09-42d49a4b2cc9.png" width="790" title="" crop="0,0,1,1" id="ufc9180ba" class="ne-image">

可以看出这个注解属于`组合注解`。拥有`@SpringBootConfiguration`、`@EnableAutoConfiguration`、`@ComponentScan`的功能。

---

## @SpringBootConfiguration注解

@SpringBootConfiguration注解的源码如下：

<img src="https://cdn.nlark.com/yuque/0/2024/png/21376908/1729563436496-752f56df-52aa-404b-bf83-c122a06f1312.png" width="611" title="" crop="0,0,1,1" id="u48b891e1" class="ne-image">

可以看到这个注解的被`@Configuration`标注，说明`主入口`程序是一个配置类。也就是说主入口中的方法可以被`@Bean`注解标注，被`@Bean`注解的标注的方法会被Spring容器自动调用，并且将该方法的返回对象纳入IoC容器的管理。测试一下：

```java
@SpringBootApplication
public class Sb305CoreApplication {
    @Bean
    public Date getNowDate(){ // 方法名作为bean的id
        return new Date();
    }
    public static void main(String[] args) {
        ConfigurableApplicationContext applicationContext = SpringApplication.run(Sb305CoreApplication.class, args);
        Date dateBean1 = applicationContext.getBean(Date.class);
        System.out.println(dateBean1);
        Date dateBean2 = applicationContext.getBean("getNowDate", Date.class);
        System.out.println(dateBean2);
    }
}
```

执行结果：

<img src="https://cdn.nlark.com/yuque/0/2024/png/21376908/1729564458157-1d953623-9405-4577-8fa4-ed955038be77.png" width="729" title="" crop="0,0,1,1" id="u3f0b40f5" class="ne-image">

通过测试我们也认证了这一点：`SpringBoot主入口类实际上就是一个配置类`。

这个`配置类`也可以称为`源`，起源的意思，SpringBoot从这个配置类开始加载项目中所有的bean。

---

## @EnableAutoConfiguration注解

该注解表示`启用自动配置`。

Spring Boot 会根据你引入的依赖自动为你配置好一系列的 Bean，无需手动编写复杂的配置代码。

例如：如果你在SpringBoot项目中进行了如下配置：

```properties
spring.datasource.driver-class-name=com.mysql.cj.jdbc.Driver
spring.datasource.url=jdbc:mysql://localhost:3306/springboot
spring.datasource.username=root
spring.datasource.password=123456
```

并且在依赖中引入了`mybatis依赖`/`mybatis启动器`，那么SpringBoot框架将为你自动化配置以下bean：

+ **SqlSessionFactory**: MyBatis的核心工厂SqlSessionFactory会被自动配置。这个工厂负责创建SqlSession实例，后者用来执行映射文件中的SQL语句。
+ **TransactionManager**: DataSourceTransactionManager会被自动配置来管理与数据源相关的事务。

---

## @ComponentScan注解

这个注解的作用是：启动组件扫描功能，代替spring框架xml文件中这个配置：

```xml
<context:component-scan base-package="com.jkweilai.sb305core"/>
```

因此被`@SpringBootApplication`注解标注之后，会启动组件扫描功能，扫描的包是`主入口程序所在包及子包`，因此如果一个bean要纳入IoC容器的管理则必须放到主入口程序所在包及子包下。放到主入口程序所在包之外的话，扫描不到。测试一下：

### 扫描到

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1764858589593-bb48fb45-9a27-4e14-9f48-a52218db3661.png" width="256.8" title="" crop="0,0,1,1" id="u56ca5320" class="ne-image">

`HelloController`代码如下：

```java
@RestController
public class HelloController {
    @GetMapping("/hello")
    public String hello(){
        return "hello world!";
    }
}
```

启动服务器测试：

<img src="https://cdn.nlark.com/yuque/0/2024/png/21376908/1729566015788-bfbce42f-90b2-48cf-b583-4490db6da625.png" width="323" title="" crop="0,0,1,1" id="u96014dfb" class="ne-image">

### 扫描不到

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1764858605501-aa8f51c9-f79c-4957-a569-6f61242b5710.png" width="332.8" title="" crop="0,0,1,1" id="u2d8e0c38" class="ne-image">

可以看到`UserController`没有在`sb305core`包下。

`UserController`代码如下：

```java
@RestController
public class UserController {
    @GetMapping("/list")
    public String list(){
        return "user list!";
    }
}
```

启动服务器测试：

<img src="https://cdn.nlark.com/yuque/0/2024/png/21376908/1729566187896-1d4053bd-d5da-4fd4-a243-ebd80388ac17.png" width="832" title="" crop="0,0,1,1" id="u5707540d" class="ne-image">

通过测试得知`UserController`没有被纳入IoC容器的管理。

最终结论：要让bean纳入IoC容器的管理，必须将类放到主入口程序同级目录下，或者子目录下。

### 怎么改变默认的扫描行为

可以通过以下方式来指定扫描的范围，这样就会改变默认的扫描规则：

`@SpringBootApplication(scanBasePackages = "com")`

