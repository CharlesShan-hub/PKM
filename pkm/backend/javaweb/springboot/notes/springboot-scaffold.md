# Spring Boot脚手架

---

## 什么是脚手架

### 建筑工程中的脚手架

在建筑工程领域，“脚手架”指的是临时性的结构，用于支撑建筑物以及建筑材料，同时为建筑工人提供工作平台。这种脚手架通常是由钢管、扣件、木板和其他配件组成的，可以根据施工需要搭建不同高度和形状的结构。

<img src="https://cdn.nlark.com/yuque/0/2024/png/21376908/1728552516494-a4239fdd-4ac0-4dbc-b55c-94eb742a950a.png" width="390" title="" crop="0,0,1,1" id="u6e13660b" class="ne-image">

### 软件开发中的脚手架

在软件开发领域，“脚手架”指的是用于快速创建项目基本结构的工具或模板。它帮助开发者初始化项目，设置必要的目录结构、文件模板以及依赖项。 

**脚手架 = 预设好的项目模板**

### Spring Boot脚手架

Spring Boot 脚手架（Scaffold）可以帮助开发者快速搭建一个Spring Boot项目结构，让开发者只专注于业务逻辑的开发，而不是在项目的初始阶段花费大量时间来配置环境或者解决依赖关系。

Spring Boot 脚手架工具存在多种形式，以下是一些常见的 Spring Boot 脚手架工具和方法：

+ **Spring Initializr：**

这是 Spring 官方提供的工具，可以在 [https://start.spring.io](https://start.spring.io) 上找到。它允许开发者选择所需的依赖、Java 版本、构建工具（Maven 或 Gradle）以及其他配置选项来生成一个新的 Spring Boot 项目。

+ **IntelliJ IDEA 内置支持：**

IntelliJ IDEA 集成了 Spring Initializr 的功能，可以在 IDE 内直接创建 Spring Boot 项目。

+ **Start Alibaba Cloud：**

阿里云提供的 Start Alibaba Cloud 增强版工具，除了基本的 Spring Boot 模块外，还集成了阿里云服务和中间件的支持。

+ **JHipster：**

JHipster 是一个流行的脚手架工具，用于生成完整的 Spring Boot 应用程序，包括前端（Angular, React 或 Vue.js）和后端。它还包括用户管理和认证等功能。

+ **Yeoman Generators：**

Yeoman 是一个通用的脚手架工具，它有一个庞大的插件生态系统，其中包括用于生成 Spring Boot 项目的插件。

+ **Bootify：**

Bootify 是另一个用于生成 Spring Boot 应用程序的脚手架工具，提供了一些预定义的应用模板。

+ **Spring Boot CLI：**

Spring Boot CLI 是一个命令行工具，允许用户通过命令行来编写和运行 Spring Boot 应用。

+ **Visual Studio Code 插件：**

Visual Studio Code 社区提供了多个插件，如 Spring Boot Extension Pack，可以帮助开发者生成 Spring Boot 项目的基本结构。

+ **GitHub Gist 和 Bitbucket Templates：**

在 GitHub 和 Bitbucket 上，有很多开发者分享了用于生成 Spring Boot 项目的脚本或模板。

+ **自定义脚手架：**

很多开发者也会根据自己的需求定制自己的脚手架工具，比如使用 Bash 脚本、Gradle 或 Maven 插件等。

---

## 使用官方提供的

### 使用官方脚手架生成Spring Boot项目

Spring Initializr：[https://start.spring.io](https://start.spring.io)

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1764849320501-e61a3471-b6b5-4e64-be6d-d1ed3840a325.png" width="1366.4" title="" crop="0,0,1,1" id="u64f14c09" class="ne-image">

点击“GENERATE”后，生成zip压缩包：

<img src="https://cdn.nlark.com/yuque/0/2024/png/21376908/1728609413133-c4914cdd-0c38-4c71-ab86-7ba13e3c4dd8.png" width="244" title="" crop="0,0,1,1" id="KHgLI" class="ne-image">

将其解压后的目录结构是一个标准的maven 工程：

<img src="https://cdn.nlark.com/yuque/0/2024/png/21376908/1728609603462-7f1dd559-7b10-4200-9503-08d76df40ebe.png" width="214" title="" crop="0,0,1,1" id="uc3ca0f71" class="ne-image">

### 将项目放到IDEA当中

接下来将其导入到IDEA当中：直接将解压后的`sb3-02-use-spring-initializr`拷贝到我们新建的空工程`SpringBoot3`下，如图：

<img src="https://cdn.nlark.com/yuque/0/2024/png/21376908/1728636406330-1f5945e3-d3d7-4c2c-b9e8-dea3be89ccbf.png" width="330" title="" crop="0,0,1,1" id="u6daadf94" class="ne-image">

打开IDEA工具，你会看到如下图：

<img src="https://cdn.nlark.com/yuque/0/2024/png/21376908/1728637409850-6f7b13f1-b98d-4b11-9f17-ba5fac3112f3.png" width="373" title="" crop="0,0,1,1" id="u0f814737" class="ne-image">

注意：如果`pom.xml`文件的图标颜色不是蓝色，而是橘色，需要在`pom.xml`文件上右键，选择：add as maven project。这样`pom.xml`文件的图标就会变为蓝色了。

<img src="https://cdn.nlark.com/yuque/0/2024/png/21376908/1728643539990-d4e9061c-1e9e-4b3c-a21a-b2604f165f5b.png" width="425" title="" crop="0,0,1,1" id="u24955417" class="ne-image">

### 脚手架生成的pom.xml文件

```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 https://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>
    <parent>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-parent</artifactId>
        <version>3.5.8</version>
        <relativePath/> <!-- lookup parent from repository -->
    </parent>
    <groupId>com.jkweilai</groupId>
    <artifactId>sb3-02-use-spring-initializr</artifactId>
    <version>0.0.1-SNAPSHOT</version>
    <name>sb3-02-use-spring-initializr</name>
    <description>使用springboot官方提供的脚手架</description>
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

可以看到脚手架生成的`pom.xml`文件的内容和我们手动创建Spring Boot项目的`pom.xml`文件是一样的。

### 脚手架生成的Spring Boot项目的结构

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1764849763329-254ba947-63ce-492a-a5c3-2ebaf9e30762.png" width="711.2" title="" crop="0,0,1,1" id="u4b2e4615" class="ne-image">

请仔细阅读上图来学习Spring Boot项目结构。

### 编写controller并测试

新建controller包，并新建HelloController类，如下图：

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1764850088811-df79e223-3ce4-45a0-abb6-551ecb03d1e6.png" width="384" title="" crop="0,0,1,1" id="u298d7488" class="ne-image">

**重点：默认情况下，SpringBoot项目只扫描主入口程序所在目录以及子目录，因此创建的Controller类要求放在主入口程序的同级目录下或子目录下。其他位置默认情况下扫描不到。**

启动应用并访问：

<img src="https://cdn.nlark.com/yuque/0/2024/png/21376908/1728644098279-12a20878-eb1f-4203-b051-d01b95f79c21.png" width="350" title="" crop="0,0,1,1" id="u8175466e" class="ne-image">

---

## 使用IDEA工具的脚手架插件

 IDEA工具自带了Spring Boot脚手架的插件，使用它会更加的方便，让我们来操作一下：

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1764850264085-fef23e31-9422-487c-b978-bcc84c110bf7.png" width="780" title="" crop="0,0,1,1" id="u29d97cfe" class="ne-image">

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1764850311614-a10e39bc-7c91-45e4-b0f5-1478b5c0f8c9.png" width="773.6" title="" crop="0,0,1,1" id="u1e9a3ad9" class="ne-image">

编写控制器，启动服务器测试：

<img src="https://cdn.nlark.com/yuque/0/2024/png/21376908/1728716401724-8808d893-408c-4b1e-9e14-70d96ff461fe.png" width="435" title="" crop="0,0,1,1" id="u22bdf23d" class="ne-image"> 

