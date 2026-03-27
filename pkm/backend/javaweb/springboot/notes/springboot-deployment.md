# 便捷的部署方式

---

## 打jar包运行

Spring Boot提供了打包插件，可以将Spring Boot项目打包为**可执行 jar 包**。Web服务器（Tomcat）也会连同一块打入jar包中。只要电脑上安装了Java的运行环境（JDK），就可以启动Spring Boot项目。

<img src="https://cdn.nlark.com/yuque/0/2024/png/21376908/1726199029529-6ffc59e1-3d92-4d4e-ab44-31f24cba9585.png" width="993" title="" crop="0,0,1,1" id="u943f6236" class="ne-image">

根据官方文档指导，使用打包功能需要引入以下的插件：

```xml
<build>
    <plugins>
        <plugin>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-maven-plugin</artifactId>
        </plugin>
    </plugins>
</build>
```

执行打包命令，生成可执行jar包：

<img src="https://cdn.nlark.com/yuque/0/2024/png/21376908/1726199412578-3892d163-9341-401d-83b5-a4412a1f7bdf.png" width="429" title="" crop="0,0,1,1" id="u3a9aabf5" class="ne-image">

<img src="https://cdn.nlark.com/yuque/0/2024/png/21376908/1726199440187-2e04d480-92c7-44e2-afb4-17c495fdc415.png" width="388" title="" crop="0,0,1,1" id="u5be0028f" class="ne-image">

<img src="https://cdn.nlark.com/yuque/0/2024/png/21376908/1726199497215-d3080065-f6dc-4c1d-b37c-4af2393faf58.png" width="476" title="" crop="0,0,1,1" id="ue80f36db" class="ne-image">

单独的将这个 jar 包可以拷贝到任何位置运行，通过`java -jar sb3-01-first-web-1.0-SNAPSHOT.jar`命令来启动 Spring Boot 项目：

<img src="https://cdn.nlark.com/yuque/0/2024/png/21376908/1726199690515-f22a7212-d34a-4644-a6cd-141a58ed490c.png" width="1498" title="" crop="0,0,1,1" id="u5a0f7f0a" class="ne-image">

打开浏览器访问：

<img src="https://cdn.nlark.com/yuque/0/2024/png/21376908/1726199728479-c1365c32-65d1-428f-b4fa-3d10f20df2e0.png" width="344" title="" crop="0,0,1,1" id="u57f97959" class="ne-image">

另外，Spring Boot框架为我们提供了非常灵活的配置，在可执行jar包的同级目录下新建配置文件：application.properties，并配置以下信息：

```properties
server.port=8888
```

重新启动服务器，然后使用新的端口号访问：

<img src="https://cdn.nlark.com/yuque/0/2024/png/21376908/1727503630959-3bcc152d-e57d-4723-8630-bc576582e215.png" width="323" title="" crop="0,0,1,1" id="u8b891f28" class="ne-image">

---

## SpringBoot的jar包和普通jar包的区别

Spring Boot 打包成的 JAR 文件与传统的 Java 应用程序中的 JAR 文件相比确实有一些显著的区别，主要体现在`依赖管理`和`可执行性`上。

**依赖管理**：

+ Spring Boot 的 JAR 包通常包含了应用程序运行所需的所有依赖项，也就是说它是一个“fat jar”（胖 JAR 包），这种打包方式使得应用可以独立运行，而不需要外部的类路径或应用服务器上的其他依赖。
+ 普通的 JAR 文件一般只包含一个类库的功能，并且需要依赖于特定的类路径来找到其他的类库或者框架，这些依赖项通常在部署环境中已经存在，比如在一个应用服务器中。

**可执行性**：

+ Spring Boot 的 JAR 文件可以通过直接执行这个 JAR 文件来启动应用程序，也就是说它是一个可执行的 JAR 文件。通过 `java -jar your-application.jar` 命令就可以直接运行应用程序。
+ 而普通的 JAR 文件通常是不可直接执行的，需要通过指定主类（main class）的方式或者其他方式来启动一个应用程序，例如使用 `-cp` 或 `-classpath` 加上类路径以及主类名来执行。

Spring Boot 的这些特性使得部署和运行变得更加简单和方便，特别是在微服务架构中，每个服务都可以被打包成独立的 JAR 文件并部署到任何支持 Java 的地方。

SpringBoot的可执行jar包目录结构：

<img src="https://cdn.nlark.com/yuque/0/2024/png/21376908/1729577060207-7c7bbf86-12ee-4ea4-9f0a-fb2d44d5774c.png" width="800" title="" crop="0,0,1,1" id="ud2b62745" class="ne-image">

普通jar包的目录结构：

<img src="https://cdn.nlark.com/yuque/0/2024/png/21376908/1729576629470-76daa653-7d27-4e33-a1c1-05191c529e6a.png" width="132" title="" crop="0,0,1,1" id="u8dde5a8e" class="ne-image">

