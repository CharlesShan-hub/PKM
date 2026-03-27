# springboot bean 管理

## 资源

* bean扫描: https://www.bilibili.com/video/BV14z4y1N7pg/?p=8
* bean注册: https://www.bilibili.com/video/BV14z4y1N7pg/?p=9
* 注册条件: https://www.bilibili.com/video/BV14z4y1N7pg/?p=10
* 自动配置: https://www.bilibili.com/video/BV14z4y1N7pg/?p=11

---
## @SpringBootApplication

### 源码分析

```java
@SpringBootApplication  
public class SpringbootApplication {  
    public static void main(String[] args) {  
       SpringApplication.run(SpringbootApplication.class, args);  
    }  
}
```

其对应的源码是

```java
	@Target({ElementType.TYPE})  
	@Retention(RetentionPolicy.RUNTIME)  
@Documented  
@Inherited  
@SpringBootConfiguration  
@EnableAutoConfiguration  
@ComponentScan(  
	    excludeFilters = {@Filter(  
	    type = FilterType.CUSTOM,  
	    classes = {TypeExcludeFilter.class}  
	), @Filter(  
	    type = FilterType.CUSTOM,  
	    classes = {AutoConfigurationExcludeFilter.class}  
	)}  
)  
public @interface SpringBootApplication {
	 // ....
}
```

可以看到，其中有三个重要功能：
* `@SpringBootConfiguration`
	* 被@Configuration标注，是一个配置类
	* 只有@SpringBootConfiguration 的里边的@Bean标注方法，才能进行IOC 容器管理
	* SpringbootApplication.class又被称为源，Springboot 就是从这里开始加载整个容器的 bean 的
* `@EnableAutoConfiguration`
	* 启用自动配置（默认启用）
	* Spring Boot 的自动配置机制是其核心特性之一，它通过智能地检测类路径和配置文件，自动完成组件的初始化和管理。具体来说，当 Spring Boot 应用启动时，它会扫描类路径下存在的类以及 `application.properties`（或 `application.yml`）中的配置项。例如，如果检测到类路径中有 `SqlSessionFactory`类，或者配置文件中设置了数据源相关信息，Spring Boot 就会认为当前项目使用了 MyBatis 框架，并自动初始化 MyBatis 相关的 Bean（如 `SqlSessionFactoryBean`、`MapperScannerConfigurer`等），然后将这些 Bean 注册到 IoC 容器中进行统一管理。这种机制极大地减少了开发人员手动编写 XML 或 Java 配置的工作，真正实现了“约定优于配置”的开发理念，让开发者更专注于业务逻辑而非环境搭建。
	* 通过SpringApplication.run可以返回上下文对象：`ConfigurableBootstrapContext context = (ConfigurableBootstrapContext) SpringApplication.run(SpringbootApplication.class, args);`
* `@ComponentScan`

### 主要参数

`@ComponentScan` 有几个重要的参数可以配置：

1. ​**​basePackages / value​**​: 指定要扫描的基础包
    
    ```
    @ComponentScan(basePackages = "com.example")
    @ComponentScan({"com.example", "com.other"}) // value 的简写
    ```
    
2. ​**​basePackageClasses​**​: 通过类来指定扫描的基础包
    
    ```
    @ComponentScan(basePackageClasses = {SomeClass.class, AnotherClass.class})
    ```
    
3. ​**​includeFilters​**​: 包含特定的组件类型
    
    ```
    @ComponentScan(includeFilters = @Filter(type = FilterType.ANNOTATION, classes = CustomAnnotation.class))
    ```
    
4. ​**​excludeFilters​**​: 排除特定的组件类型
    
    ```
    @ComponentScan(excludeFilters = @Filter(type = FilterType.ANNOTATION, classes = Controller.class))
    ```
    
5. ​**​useDefaultFilters​**​: 是否使用默认过滤器（默认为 true）
    
    ```
    @ComponentScan(useDefaultFilters = false)
    ```
    
### 使用场景示例

1. 扫描多个包

```java
@SpringBootApplication
@ComponentScan(basePackages = {"com.example.main", "com.example.utils"})
public class MyApplication {
    // ...
}
```

2. 排除特定组件

```java
@SpringBootApplication
@ComponentScan(excludeFilters = @Filter(type = FilterType.ANNOTATION, classes = {Service.class}))
public class MyApplication {
    // ...
}
```

3. 自定义过滤器

```java
@SpringBootApplication
@ComponentScan(
    includeFilters = @Filter(type = FilterType.CUSTOM, classes = MyTypeFilter.class),
    useDefaultFilters = false
)
public class MyApplication {
    // ...
}
```

---
## Bean注册

### 自己的类

对于我们自己写的类，可以使用下边的注解注入到程序中。

|     注解      |       说明        |             位置              |
| :---------: | :-------------: | :-------------------------: |
| @Component  |   声明bean的基础注解   |        不属于以下三类时，用此注解        |
| @Controller | @Component的衍生注解 |          标注在控制器类上           |
|  @Service   | @Component的衍生注解 |           标注在业务类上           |
| @Repository | @Component的衍生注解 | 标注在数据访问类上（由于与mybatis整合，用的少） |

### 第三方的类：`@Bean`

对于第三方的类，代码是只读的，我们不能对其进行修改，对此我们可以使用@Bean和@Import进行注入

首先我们新建一个工程 demoBean，里边仅包含一个文件 Movie.java

```java
package com.charles;  
  
public class Movie {  
    String title;  
    String year;  
}
```

使用maven打包成demoBean-1.0-SNAPSHOT.jar

再新建一个springboot工程，在其终端中，安装该包
```bash
charles@Charless-MacBook-Pro ~/w/p/p/j/s/bean (master)> mvn install:install-file -Dfile=/Users/charles/workspace/project/playground/java/springboot/demoBean/target/demoBean-1.0-SNAPSHOT.jar -DgroupId=org.charles -DartifactId=common-pojo -Dversion=1.0 -Dpackaging=jar
[INFO] Scanning for projects...
[INFO] 
[INFO] --------------------------< com.charles:bean >--------------------------
[INFO] Building bean 0.0.1-SNAPSHOT
[INFO]   from pom.xml
[INFO] --------------------------------[ jar ]---------------------------------
[INFO] 
[INFO] --- install:3.1.4:install-file (default-cli) @ bean ---
[INFO] Installing /Users/charles/workspace/project/playground/java/springboot/demoBean/target/demoBean-1.0-SNAPSHOT.jar to /Users/charles/.m2/repository/org/charles/common-pojo/1.0/common-pojo-1.0.jar
[INFO] Installing /var/folders/n7/t8br89y558n8dkpg4gkw10g00000gn/T/demoBean-1.0-SNAPSHOT9326471047283854776.pom to /Users/charles/.m2/repository/org/charles/common-pojo/1.0/common-pojo-1.0.pom
[INFO] ------------------------------------------------------------------------
[INFO] BUILD SUCCESS
[INFO] ------------------------------------------------------------------------
[INFO] Total time:  0.194 s
[INFO] Finished at: 2025-12-25T13:58:47+08:00
[INFO] ------------------------------------------------------------------------
charles@Charless-MacBook-Pro ~/w/p/p/j/s/bean (master)> 

```

这时候我们可以去springboot工程里边使用引入坐标了
```xml
<dependency>  
    <groupId>org.charles</groupId>  
    <artifactId>common-pojo</artifactId>  
    <version>1.0</version>  
</dependency>
```

修改主程序类，使用@Bean就可以注入这个对象了。SpringApplication.run会返回一个ApplicationContext对象，我们使用getBean可以获取到这个注入的Movie。

```java
@SpringBootApplication  
public class BeanApplication {  
  
    public static void main(String[] args) {  
  
        ApplicationContext context = SpringApplication.run(BeanApplication.class, args);  
  
        Movie movie = context.getBean(Movie.class);  
        System.out.println(movie);  // com.charles.Movie@250b236d
    }  
    @Bean  
    public Movie Movie(){  
        return new Movie();  
    }}
```

### 第三方的类：`@Bean` + config包

因为启动程序最好还是自用来启动，不要加入引入包的功能，所以更推荐第二种方案：在controller同级创建config包，里边创建配置类比如`config/CommonConfig.java`

```java
package com.charles.bean.config;  
  
import com.charles.Movie;  
import org.springframework.context.annotation.Bean;  
import org.springframework.context.annotation.Configuration;  
  
@Configuration  
public class CommonConfig {  
    @Bean  
    public Movie CharlesMovie(){  
        return new Movie();  
    }
}
```

在使用的时候可以去获取类，也可以使用方法名（本案例中就是CharlesMovie）

```java
@SpringBootApplication  
public class BeanApplication {  
  
    public static void main(String[] args) {  
  
        ApplicationContext context = SpringApplication.run(BeanApplication.class, args);  
  
        Movie movie1 = context.getBean(Movie.class);  
        System.out.println(movie1); //com.charles.Movie@61f3fbb8  
  
        Movie movie2 = (Movie) context.getBean("CharlesMovie");  
        System.out.println(movie2); //com.charles.Movie@61f3fbb8  
    }  
}
```

我们也可以修改默认的类名

```java
@Configuration  
public class CommonConfig {  
    @Bean("GoodMovie")
    public Movie CharlesMovie(){  
        return new Movie();  
    }
}
```

### 第三方的类：`@Import`

如果我们的config并不在controller统计目录，比如可能在上一级目录，这样的话springboot自动扫码就加载不到这个CommonConfig类。比如(工程名字叫做bean)：

```bash
charles@Charless-MacBook-Pro ~/w/p/p/j/s/b/src (master)> tree
.
├── main
│   ├── java
│   │   └── com
│   │       └── charles
│   │           ├── bean
│   │           │   └── BeanApplication.java
│   │           └── config
│   │               └── CommonConfig.java
│   └── resources
│       └── application.properties
└── test
    └── java
        └── com
            └── charles
                └── bean
                    └── BeanApplicationTests.java

13 directories, 4 files
```

我们就需要手动的添加`@Import`

```java
@SpringBootApplication  
@Import(CommonConfig.class)  
public class BeanApplication {  
  
    public static void main(String[] args) {  
  
        ApplicationContext context = SpringApplication.run(BeanApplication.class, args);  
  
        Movie movie1 = context.getBean(Movie.class);  
        System.out.println(movie1); //com.charles.Movie@61f3fbb8  
  
        Movie movie2 = (Movie) context.getBean("CharlesMovie");  
        System.out.println(movie2); //com.charles.Movie@61f3fbb8  
    }  
}
```

* 添加一个-直接写类名：`@Import(CommonConfig.class)`
* 添加多个-传入数组：`@Import({A.class, B.class, C.class})`

### 第三方的类：`@Import` + `ImportSelector`

如果只有一个要引入的类，那还好办，如果我们有很多很多的配置类，数组的长度就会很长，代码不优雅。我们可以导入`ImportSelector`实现类，比如创建`config/CommonImportSelector.java`

```java
package com.charles.config;  
  
import org.springframework.context.annotation.ImportSelector;  
import org.springframework.core.type.AnnotationMetadata;  
  
public class CommonImportSelector implements ImportSelector {  
    @Override  
    public String[] selectImports(AnnotationMetadata importingClassMetadata) {  
        return new String[]{"com.charles.Movie"};  
    }
}
```

对应的只要把刚才的`@Import(CommonConfig.class)`修改成`@Import(CommonImportSelector.class)`就好了

### 第三方的类：`@Import` + `ImportSelector` + 配置文件

最后只需要优化一点了，可以把写死的类名，提取到配置文件中，比如在resources文件夹中，创建`common.imports`

common.imports
```txt
com.charles.Movie
```

CommonImportSelector.java
```java
package com.charles.config;  
  
import org.springframework.context.annotation.ImportSelector;  
import org.springframework.core.type.AnnotationMetadata;  
  
import java.io.BufferedReader;  
import java.io.InputStream;  
import java.io.InputStreamReader;  
import java.util.ArrayList;  
import java.util.List;  
  
public class CommonImportSelector implements ImportSelector {  
    @Override  
    public String[] selectImports(AnnotationMetadata importingClassMetadata) {  
        List<String> imports = new ArrayList<>();  
        InputStream is = CommonImportSelector.class.getClassLoader().getResourceAsStream("common.imports");  
        BufferedReader br = new BufferedReader(new InputStreamReader(is));  
        String line;  
        try{  
            while((line = br.readLine())!=null){  
                imports.add(line);  
            }        
        }catch (Exception e){  
            throw new RuntimeException(e);  
        }finally {  
            try{  
                if(br!=null){  
                    br.close();  
                }            
            }catch (Exception e){  
                throw new RuntimeException(e);  
            }        
        }        
        return imports.toArray(new String[0]);  
    }
}
```

最后我们用流继续简化一下代码：CommonImportSelector.java
```java
package com.charles.config;  
  
import org.springframework.context.annotation.ImportSelector;  
import org.springframework.core.type.AnnotationMetadata;  
  
import java.io.BufferedReader;  
import java.io.IOException;  
import java.io.InputStream;  
import java.io.InputStreamReader;  
  
public class CommonImportSelector implements ImportSelector {  
    @Override  
    public String[] selectImports(AnnotationMetadata importingClassMetadata) {  
        try (
			InputStream is = CommonImportSelector.class.getClassLoader().getResourceAsStream("common.imports");
			BufferedReader br = new BufferedReader(new InputStreamReader(is))  
        ) {
			return br.lines()
				.map(String::trim)
				.filter(line -> !line.isEmpty() && !line.startsWith("#"))
				.toArray(String[]::new);  
        } catch (IOException e) {  
            throw new RuntimeException("Failed to read common.imports", e);  
        }
    }
}
```

### 组合注解

最后的最后，可以添加自己的组合注解，让调用看起来更简洁，很多java的工具都是这么做的。

anno/EnableCommonConfig.java
```java
package com.charles.anno;  
  
import com.charles.config.CommonImportSelector;  
import org.springframework.context.annotation.Import;  
  
import java.lang.annotation.ElementType;  
import java.lang.annotation.Retention;  
import java.lang.annotation.RetentionPolicy;  
import java.lang.annotation.Target;  
  
@Target({ElementType.TYPE})  
@Retention(RetentionPolicy.RUNTIME)  
@Import(CommonImportSelector.class)  
public @interface EnableCommonConfig {  
}
```

调用的位置就可以很精简啦
```java
@SpringBootApplication  
@EnableCommonConfig  
public class BeanApplication {  
  
    public static void main(String[] args) {  
  
        ApplicationContext context = SpringApplication.run(BeanApplication.class, args);  
  
        Movie movie = context.getBean(Movie.class);  
        System.out.println(movie); //com.charles.Movie@61f3fbb8  
    }  
}
```

看一下目录结构
```bash
charles@Charless-MacBook-Pro ~/w/p/p/j/s/b/src (master)> tree
.
├── main
│   ├── java
│   │   └── com
│   │       └── charles
│   │           ├── anno
│   │           │   └── EnableCommonConfig.java
│   │           ├── bean
│   │           │   └── BeanApplication.java
│   │           └── config
│   │               ├── CommonConfig.java
│   │               └── CommonImportSelector.java
│   └── resources
│       ├── application.properties
│       └── common.imports
└── test
    └── java
        └── com
            └── charles
                └── bean
                    └── BeanApplicationTests.java

14 directories, 7 files
```

---
## 注册条件

我们上边的注册都是没有参数传入的，但如果我们有一些默认的值，下边是通过@Value从配置文件读取参数的方法

首先修改一下我们的包
```java
package com.charles;  
  
public class Movie {  
    public String title;  
    public String year;  
  
    public Movie(String title, String year) {  
        this.title = title;  
        this.year = year;  
    }  
    public Movie(){}  
}
```

重新安装后，这样我们的CommonConfig里边就可以用@Value传入参数并调用Movie的有参构造器了
```java
@Configuration  
public class CommonConfig {  
  
    //@Bean  
    //public Movie Movie(){  
    //    return new Movie();  
    //}  
    @Bean  
    public Movie Movie(  
            @Value("$system.title")String title,  
            @Value("$system.title")String year  
    ) {  
        return new Movie(title, year);  
    }
}
```

我们有三个对应的注解

|            注解             |           说明           |
| :-----------------------: | :--------------------: |
|  @ConditionalOnProperty   | 配置文件中存在对应的属性，才声明该Bean  |
| @ConditionalOnMissingBean | 不存在当前类型的Bean时，才声明该Bean |
|    @ConditionalOnClass    | 当前环境存在指定的这个类时，才声明该Bean |

现在我们可以在CommonConfig.java里边判断是否有配置

```java
@Configuration  
public class CommonConfig {  
  
    @Bean  
    @ConditionalOnProperty(prefix = "system", name = {"title", "year"})  
    public Movie configuredMovie(  
            @Value("${system.title}") String title,  
            @Value("${system.year}") String year) {
        return new Movie(title, year);  
    }  
    @Bean  
    @ConditionalOnMissingBean(Movie.class)  
    public Movie defaultMovie() {  
        return new Movie();  
    }
}
```

要注意现在的开始文件需要是`@Import(CommonConfig.class)`

```java
@SpringBootApplication  
@Import(CommonConfig.class)  
public class BeanApplication {  
    public static void main(String[] args) {  
        ApplicationContext context = SpringApplication.run(BeanApplication.class, args);  
        Movie movie = context.getBean(Movie.class);  
        System.out.println(movie.title);  
    }
}
```

## 自动配置

为什么我的引入mybatis不需要手动的写这么多@Bean呢，因为这些包用了自动配置。下边我们分析一下springboot如何进行自动配置的。

### 源码解析

首先我们进入`@SpringBootApplication`，可以看到其中组合了`@EnableAutoConfiguration`，再点进去可以看到熟悉的`@Import`，`@Import({AutoConfigurationImportSelector.class})`。

`AutoConfigurationImportSelector.class`可以看到是实现了`DeferredImportSelector`，`DeferredImportSelector`又继承了`ImportSelector`，所以`AutoConfigurationImportSelector`也是一个配置了。

在`AutoConfigurationImportSelector`中有一个方法，虽然不会执行，但是开发者写了这个方法帮助我们了解自动配置原理。
```java
public String[] selectImports(AnnotationMetadata annotationMetadata) {  
    if (!this.isEnabled(annotationMetadata)) {  
        return NO_IMPORTS;  
    } else {  
        AutoConfigurationEntry autoConfigurationEntry = this.getAutoConfigurationEntry(annotationMetadata);  
        return StringUtils.toStringArray(autoConfigurationEntry.getConfigurations());  
    }
}
```

`autoConfigurationEntry`是通过`getAutoConfigurationEntry()`得到的，我们进入它。
```java
protected AutoConfigurationEntry getAutoConfigurationEntry(AnnotationMetadata annotationMetadata) {  
    if (!this.isEnabled(annotationMetadata)) {  
        return EMPTY_ENTRY;  
    } else {  
        AnnotationAttributes attributes = this.getAttributes(annotationMetadata);  
        List<String> configurations = this.getCandidateConfigurations(annotationMetadata, attributes);  
        configurations = this.<String>removeDuplicates(configurations);  
        Set<String> exclusions = this.getExclusions(annotationMetadata, attributes);  
        this.checkExcludedClasses(configurations, exclusions);  
        configurations.removeAll(exclusions);  
        configurations = this.getConfigurationClassFilter().filter(configurations);  
        this.fireAutoConfigurationImportEvents(configurations, exclusions);  
        return new AutoConfigurationEntry(configurations, exclusions);  
    }
}
```

显然配置是`configurations`，它是通过`getCandidateConfigurations()`得到的。
```java
protected List<String> getCandidateConfigurations(AnnotationMetadata metadata, @Nullable AnnotationAttributes attributes) {  
    ImportCandidates importCandidates = ImportCandidates.load(
		    this.autoConfigurationAnnotation, 
		    this.getBeanClassLoader()
		);  
    List<String> configurations = importCandidates.getCandidates();  
    Assert.state(!CollectionUtils.isEmpty(configurations), \
	    "No auto configuration classes found in META-INF/spring/" +
	    this.autoConfigurationAnnotation.getName() + 
	    ".imports. If you are using a custom packaging, make sure that file is correct.");  
    return configurations;  
}
```

然后中间那个名字是这样得到的，理论上就是`org.springframework.boot.autoconfigure.AutoConfiguration.class`。
```java
private final Class<?> autoConfigurationAnnotation;

public AutoConfigurationImportSelector() {  
    this((Class)null);  
}  
  
AutoConfigurationImportSelector(@Nullable Class<?> autoConfigurationAnnotation) {  
    this.autoConfigurationAnnotation = autoConfigurationAnnotation != null ? autoConfigurationAnnotation : AutoConfiguration.class;  
}
```

所以上边的字符串拼接后应该是：`META-INF/spring/org.springframework.boot.autoconfigure.AutoConfiguration.imports`，我们maven的蹭库里边找到spring-boot-autoconfigure，在`META-INF`文件夹下就可以找到这个文件。里边保存了很多很多的配置类。下边是前五行。
```txt
org.springframework.boot.autoconfigure.admin.SpringApplicationAdminJmxAutoConfiguration  
org.springframework.boot.autoconfigure.amqp.RabbitAutoConfiguration  
org.springframework.boot.autoconfigure.aop.AopAutoConfiguration  
org.springframework.boot.autoconfigure.availability.ApplicationAvailabilityAutoConfiguration  
org.springframework.boot.autoconfigure.batch.BatchAutoConfiguration
....
```

随便找一个比如DispatcherServletAutoConfiguration，点击进入，可以看到我们熟悉的手动配置的内容注解了。
```java
@AutoConfigureOrder(Ordered.HIGHEST_PRECEDENCE)  
@AutoConfiguration(after = ServletWebServerFactoryAutoConfiguration.class)  
@ConditionalOnWebApplication(type = Type.SERVLET)  
@ConditionalOnClass(DispatcherServlet.class)  
public class DispatcherServletAutoConfiguration {  
  
    /**  
     * The bean name for a DispatcherServlet that will be mapped to the root URL "/".     
     */    
     public static final String DEFAULT_DISPATCHER_SERVLET_BEAN_NAME = "dispatcherServlet";  
  
    /**  
     * The bean name for a ServletRegistrationBean for the DispatcherServlet "/".     
     */    
     public static final String DEFAULT_DISPATCHER_SERVLET_REGISTRATION_BEAN_NAME = "dispatcherServletRegistration";  
  
    @Configuration(proxyBeanMethods = false)  
    @Conditional(DefaultDispatcherServletCondition.class)  
    @ConditionalOnClass(ServletRegistration.class)  
    @EnableConfigurationProperties(WebMvcProperties.class)  
    protected static class DispatcherServletConfiguration {  
  
       @Bean(name = DEFAULT_DISPATCHER_SERVLET_BEAN_NAME)  
       public DispatcherServlet dispatcherServlet(WebMvcProperties webMvcProperties) {  
          DispatcherServlet dispatcherServlet = new DispatcherServlet();  
          dispatcherServlet.setDispatchOptionsRequest(webMvcProperties.isDispatchOptionsRequest());  
          dispatcherServlet.setDispatchTraceRequest(webMvcProperties.isDispatchTraceRequest());  
          dispatcherServlet.setPublishEvents(webMvcProperties.isPublishRequestHandledEvents());  
          dispatcherServlet.setEnableLoggingRequestDetails(webMvcProperties.isLogRequestDetails());  
          return dispatcherServlet;  
       }
    ...
    }
    ...
}
```

### 手动实践

最后我们模仿springboot自动配置的样子，把刚才的包也改造一下

```bash
charles@Charless-MacBook-Pro ~/w/p/p/j/s/d/src (master)> tree
.
├── main
│   ├── java
│   │   └── org
│   │       └── charles
│   │           ├── CommonAutoConfig.java
│   │           ├── CommonConfig.java
│   │           └── Movie.java
│   └── resources
│       └── META-INF
│           └── spring
│               └── org.springframework.boot.autoconfigure.AutoConfiguration.imports
└── test
    └── java

11 directories, 4 files
```

CommonAutoConfig.java
```java
package org.charles;  
  
import org.springframework.boot.autoconfigure.AutoConfiguration;  
import org.springframework.context.annotation.Import;  
  
@AutoConfiguration  
@Import(CommonConfig.class)  
public class CommonAutoConfig {  
}
```

CommonConfig.java
```java
package org.charles;  
  
import org.springframework.beans.factory.annotation.Value;  
import org.springframework.boot.autoconfigure.condition.ConditionalOnMissingBean;  
import org.springframework.boot.autoconfigure.condition.ConditionalOnProperty;  
import org.springframework.context.annotation.Bean;  
  
public class CommonConfig {  
    @Bean  
    @ConditionalOnProperty(prefix = "system", name = {"title", "year"})  
    public Movie configuredMovie(  
            @Value("${system.title}") String title,  
            @Value("${system.year}") String year) {  
        return new Movie(title, year);  
    }  
    @Bean  
    @ConditionalOnMissingBean(Movie.class)  
    public Movie defaultMovie() {  
        return new Movie();  
    }
}
```

org.springframework.boot.autoconfigure.AutoConfiguration.imports
```txt
org.charles.CommonConfig
```

### 面试题：自动配置原理
1. 在主启动类上添加了`StringBootApplication`注解，这个注解组合了`EnableAutoConfiguration`注解。
2. `EnableAutoConfiguration`注解又组合了`Import`注解，导入了`AutoConfigurationImportSelector`类。
3. 这个类是`ImportSelector`接口的实现类，实现了`selectImports`方法，这个方法经过层层调用，最终会读取`EMTA-INF`目录下边的`.imports`文件。在`springboot 2.7`以前是`spring.factories`文件
4. 这个文件里边是所有的配置类的全类名，读到全类名后会解析注册条件也就是`@Conditional`及其衍生注解，把班组条件的`Bean`对象自动注入到`IOC`容器里。
