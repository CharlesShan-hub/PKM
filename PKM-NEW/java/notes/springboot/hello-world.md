# Springboot Hello World

* 创建 springboot 项目: https://www.bilibili.com/video/BV14z4y1N7pg/?p=3
* 先创建 maven 项目然后手动配置 springboot: https://www.bilibili.com/video/BV14z4y1N7pg/?p=4

---
## 环境与配置

* springboot 采用 3.n
* java 版本需要≥17
* 采用 maven 进行配置
* 需要的依赖只要选择springweb就可以了

---
## 代码

* 导入的依赖已经默认写好：其中`org.springframework.boot`就是工程的 id，以后每一个子工程都要继承这个工程的配置
```XML
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 https://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>
    <parent>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-parent</artifactId>
        <version>3.5.3</version>
        <relativePath/> <!-- lookup parent from repository -->
    </parent>
    <groupId>com.charlesshan</groupId>
    <artifactId>hello-world</artifactId>
    <version>0.0.1-SNAPSHOT</version>
    <name>hello-world</name>
    <description>hello-world</description>
    <url/>
    <licenses>
        <license/>
    </licenses>
    <developers>
        <developer/>
    </developers>
    <scm>
        <connection/>
        <developerConnection/>
        <tag/>
        <url/>
    </scm>
    <properties>
        <java.version>21</java.version>
    </properties>
    <dependencies>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-web</artifactId>
        </dependency>

        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-test</artifactId>
            <scope>test</scope>
        </dependency>
    </dependencies>

    <build>
        <plugins>
            <plugin>
                <groupId>org.springframework.boot</groupId>
                <artifactId>spring-boot-maven-plugin</artifactId>
            </plugin>
        </plugins>
    </build>

</project>
```
* 启动类已经默认写好
```Java
package com.charlesshan.helloworld;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class HelloWorldApplication {
    public static void main(String[] args) {
        SpringApplication.run(HelloWorldApplication.class, args);
    }
}
```
* 编写 Controller
```java
package com.charlesshan.helloworld.controller;

import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class HelloController {
    @RequestMapping("/hello")
    public String hello() {
        return "Hello World!";
    }
}
```
* 最后去浏览器访问: http://localhost:8080/hello

---
## 打包

只需要使用maven的package打包

运行只需：`java -jar ./springboot-0.0.1-SNAPSHOT.jar`

面试题：**Spring Boot的JAR包与普通JAR包的区别**

* Spring Boot打包成的JAR文件与传统的Java应用程序中的JAR文件的区别，主要体现在**依赖管理**和**可执行性**上。
* 在**依赖管理**方面，Spring Boot的JAR包通常**包含了应用程序运行所需的所有依赖项**，也就是说它是一个"fat jar"（胖JAR包）。这种打包方式使得应用可以独立运行，而不需要外部的类路径或应用服务器上的其他依赖。相比之下，普通的JAR文件**一般只包含一个类库的功能**，并且需要依赖于特定的类路径来找到其他的类库或者框架，这些依赖项通常在部署环境中已经存在，比如在一个应用服务器中。
* 就**可执行性**而言，Spring Boot的JAR文件可以通过直接执行这个JAR文件来启动应用程序，也就是说它是一个可执行的JAR文件。通过简单的`java -jar your-application.jar`命令就可以直接运行应用程序。而**普通的JAR**文件通常是不可直接执行的，**需要通过指定主类**（main class）的方式或者其他方式来启动一个应用程序，例如使用`-cp`或`-classpath`加上类路径以及主类名来执行。
* Spring Boot的这些特性使得部署和运行变得更加简单和方便，特别是在微服务架构中，每个服务都可以被打包成独立的JAR文件并部署到任何支持Java的地方。这种设计大大简化了应用程序的部署流程，降低了环境配置的复杂度，为开发者和运维人员提供了极大的便利。

---
## 脚手架

**Spring Boot 脚手架​**​是一套预配置的项目模板和代码生成工具，用于快速创建基于 Spring Boot 的标准项目结构。它就像建筑的"脚手架"一样，为你搭建好项目的基础框架。

```bash
my-project/
├── src/
│   ├── main/
│   │   ├── java/com/example/
│   │   │   └── MyApplication.java
│   │   └── resources/
│   │       ├── application.properties
│   │       └── static/
│   └── test/
├── pom.xml
└── README.md
```

所以，上面的helloworld例子我们只需要自己写一个controller就可以了。当然不同的工具支持不同的脚手架，比如官方的，idea的，阿里巴巴的，我们也可以自定义脚手架。

