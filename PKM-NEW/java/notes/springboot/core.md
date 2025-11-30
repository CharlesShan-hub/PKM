# Springboot 核心机制

---
## 继承父工程

> https://blog.csdn.net/lzylzy57/article/details/144293461

继承父工程的优势

* 依赖管理：可以在父工程中定义依赖的版本，子模块可以直接引用而不必指定版本号。
* 插件管理：可以在父工程中配置常用的插件及其版本，子模块可以直接使用这些配置。
* 属性设置：可以在父工程中定义一些通用的属性，如项目编码、Java 版本等。
* 统一配置：可以统一多个子模块的构建配置，确保一致性。

直接引入依赖的局限性（如果你不使用继承父工程的方式，而是通过直接引入依赖的方式来管理项目，那么你将失去上述的一些优势）

* 依赖版本管理：每个子模块都需要单独指定依赖的版本，这会导致大量的重复配置，并且难以维护。
* 插件配置：每个子模块都需要单独配置插件及其版本，无法共享父工程中的插件配置。
* 属性设置：每个子模块都需要单独设置通用的属性，如项目编码、Java 版本等。
* 构建配置：每个子模块的构建配置需要单独维护，难以保证一致性。

总结：选择哪种方式取决于你的具体需求。

如果你希望多个项目之间共享构建配置，那么使用父项目是一个好的选择；
如果你只是想在项目之间共享代码，那么应该使用依赖关系。

---
## 启动器

> https://www.51cto.com/article/747431.html

有很多官方启动器，也有很多第三方启动器，用来导入特定的依赖的组合

---
## 核心注解

### @SpringBootApplication

```java
@SpringBootApplication  
public class SpringbootApplication {  
    public static void main(String[] args) {  
       SpringApplication.run(SpringbootApplication.class, args);  
    }  
}
```

是一个复合注解，同时拥有三个功能：
* @SpringBootConfiguration 
	* 被@Configuration标注，是一个配置类
	* 只有@SpringBootConfiguration 的里边的@Bean标注方法，才能进行IOC 容器管理
	* SpringbootApplication.class又被称为源，Springboot 就是从这里开始加载整个容器的 bean 的
* @EnableAutoConfiguration 
	* 启用自动配置（默认启用）
	* Spring Boot 的自动配置机制是其核心特性之一，它通过智能地检测类路径和配置文件，自动完成组件的初始化和管理。具体来说，当 Spring Boot 应用启动时，它会扫描类路径下存在的类以及 `application.properties`（或 `application.yml`）中的配置项。例如，如果检测到类路径中有 `SqlSessionFactory`类，或者配置文件中设置了数据源相关信息，Spring Boot 就会认为当前项目使用了 MyBatis 框架，并自动初始化 MyBatis 相关的 Bean（如 `SqlSessionFactoryBean`、`MapperScannerConfigurer`等），然后将这些 Bean 注册到 IoC 容器中进行统一管理。这种机制极大地减少了开发人员手动编写 XML 或 Java 配置的工作，真正实现了“约定优于配置”的开发理念，让开发者更专注于业务逻辑而非环境搭建。
	* 通过SpringApplication.run可以返回上下文对象：`ConfigurableBootstrapContext context = (ConfigurableBootstrapContext) SpringApplication.run(SpringbootApplication.class, args);`
	* 

@ComponentScan


