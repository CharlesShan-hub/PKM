# Starter-启动器

在 Spring Boot 中，启动器（Starter）本质上是一个简化依赖管理的概念。

Spring Boot 的启动器本质上就是一组预定义的依赖集合，它们被组织成一个个 Maven的依赖，以方便开发者快速集成特定的功能模块。

如果你想做web开发，只需要引入web启动器。web启动器会自动引入web开发所需要的子依赖。

**启动器 starter 的引入是会引入具体依赖的。**`**<dependencyManagement>**`**只声明/锁定依赖的版本，但它不会引入具体的依赖。引入一个启动器，就是引入这个开发场景下对应的一套依赖。**

---

## 启动器实现原理

1. **依赖聚合**：  
每个启动器通常对应一个特定的功能集或者一个完整的应用模块，如 `spring-boot-starter-web` 就包含了构建 Web 应用所需的所有基本依赖项，如 Spring MVC, Tomcat 嵌入式容器等。
2. **依赖传递**：  
当你在项目中引入一个启动器时，它不仅会把自身作为依赖加入到你的项目中，还会把它的所有直接依赖项（transitive dependencies）也加入进来。这意味着你不需要单独声明这些依赖项，它们会自动成为项目的一部分。
3. **自动配置**：  
许多启动器还提供了自动配置（Auto-configuration），这是一种机制，允许 Spring Boot 根据类路径上的可用组件自动设置你的应用程序。例如，如果类路径上有 DispatcherServlet 和嵌入式 Tomcat，则 Spring Boot 会自动配置它们，并准备好一个 web 应用程序。

**使用启动器的示例**

假设你想创建一个基于 Spring MVC 的 RESTful Web 应用，你可以简单地将 `spring-boot-starter-web` 添加到你的项目中：

```xml
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-web</artifactId>
</dependency>
```

当你添加这个依赖时，Spring Boot 会处理所有必要的细节，包括添加 Spring MVC 和 Tomcat 作为嵌入式 Servlet 容器，并且根据类路径上的内容进行适当的自动配置。如下图所示：

<img src="https://cdn.nlark.com/yuque/0/2024/png/21376908/1729327501374-2bf74e3a-cbc8-4c66-b206-dd38fec8a251.png" width="465" title="" crop="0,0,1,1" id="ua61ea1ce" class="ne-image">

这就是 Spring Boot 启动器的基本实现原理，它简化了依赖管理，让开发者能够更专注于业务逻辑的实现。

---

## 每个 Starter 是一个独立的 Maven 项目

1. 启动器是独立的 Maven 项目（有的启动器是 springboot 官方提供的，有的启动器是第三方的）。
2. 在非 SpringBoot 项目中也可以使用。在普通的 Spring 项目中也可以使用启动器。
3. 启动器是独立的 Maven 项目，**它没有继承 springboot**。每个启动器中的子依赖的版本都是启动器自己管理的（自己管理的意思是：程序员人工管理的，人工保证依赖的版本）。但启动器本身的版本是由 springboot 项目管理的。可以通过下图看到每个启动器管理自己子依赖版本。

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1764854194840-c0179cd0-1f0a-456f-be29-72da44212570.png" width="632" title="" crop="0,0,1,1" id="u91e05917" class="ne-image">

4. 当然，一个启动器，可以关联依赖其他启动器。不要把它想的太高端，就把一个启动器当做一个依赖就行了。和引入 mysql 驱动没啥区别。
5. 启动器中的子依赖的每一个版本是人工管理的，这个怎么理解？
    1. 启动器的开发人员在指定该启动器**子依赖**的版本时，参照 SpringBoot 的 BOM（**物料清单（Bill of Materials）**）。
    2. 什么是 BOM？**如果一个POM文件中主要包含**`**dependencyManagement**`**，并且被设计为供其他项目**`**import**`**使用，那么它就可以被称为BOM。**
        1. **一个真正的BOM应该具备：**
            1. `**<packaging>pom</packaging>**`**- 声明这是一个POM类型项目**
            2. **主要/唯一内容是**`**dependencyManagement**`**- 定义版本**
            3. **很少或没有**`**<dependencies>**`**- 不直接引入依赖**
            4. **被其他项目**`**import**`**- 设计目的就是被引用**
    3. **SpringBoot 的 BOM 是：**`**spring-boot-dependencies-3.5.8.pom**`

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1764856415812-4fe0aa55-158d-4d13-8cc3-6b39aba3a347.png" width="559.2" title="" crop="0,0,1,1" id="ufef4fcc7" class="ne-image">

    4. **启动器开发者是如何进行人工管理子依赖版本的？**
        1. **比如启动器的开发人员正在开发的 web 启动器的版本是：**`**spring-boot-starter-web-3.5.8**`
        2. **那么他们就会去**`**spring-boot-dependencies-3.5.8.pom**`**中找子依赖的版本。**

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1764857180195-efc3654a-5132-4995-8139-a065cb58caec.png" width="540.8" title="" crop="0,0,1,1" id="u6bc6e8c4" class="ne-image">

6. 启动器中子依赖的版本如果和 SpringBoot 的 BOM 中的依赖版本不一致，**以 BOM 中的版本为准**。
7. 启动器中子依赖不一定在 SpringBoot 的 BOM 中都存在！！

---

## SpringBoot 保证版本一致性的核心机制

1. **✅**我们的项目继承Spring Boot父项目，决定使用哪个大版本，例如（3.5.8）**
2. **✅**引入启动器时**不写版本**，自动使用父项目定义的版本（因此启动器使用的也是 3.5.8）**
3. **✅**启动器内部依赖的版本**应该**按BOM标准写（程序员编写启动器的子依赖时，自己写，但要参考 SpringBoot 的 BOM，和它一样。）**
4. **✅**即使启动器写错版本（**程序员手滑写错了**），**最终以BOM为准这就是Spring Boot保证版本一致性的核心机制。大家必须要掌握的内容是：你写的项目、Spring Boot 父项目、启动器 三者的关系！！！**

---

## 都有哪些启动器

启动器通常包括：

+ SpringBoot官方提供的启动器
+ 非官方提供的启动器

### 官方提供的启动器

启动器命名特点：spring-boot-starter-*

<img src="https://cdn.nlark.com/yuque/0/2024/png/21376908/1729328350698-5231f924-4ae0-447b-a1af-f2c25e4f8440.png" width="922" title="" crop="0,0,1,1" id="ua9ae9cd4" class="ne-image">

### 非官方的启动器

启动器命名特点：*-spring-boot-starter

<img src="https://cdn.nlark.com/yuque/0/2024/png/21376908/1729328504925-f0aa6730-ee7f-4a1d-85f9-3d2c9075318f.png" width="491" title="" crop="0,0,1,1" id="ued5b2680" class="ne-image">

