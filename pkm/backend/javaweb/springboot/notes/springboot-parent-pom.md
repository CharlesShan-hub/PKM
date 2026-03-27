# 为何以继承方式引入SpringBoot

---

## 提出疑问

以前我们在开发项目时，需要什么，引入对应的依赖就行，比如我们需要连接mysql数据，则引入mysql驱动的依赖，如下：

```xml
<dependency>
  <groupId>com.mysql</groupId>
  <artifactId>mysql-connector-j</artifactId>
  <version>8.3.0</version>
</dependency>
```

现在我们要使用SpringBoot框架，按说也应该采用依赖的方式将SpringBoot框架引入，如下：

```xml
<dependency>
  <groupId>org.springframework.boot</groupId>
  <artifactId>spring-boot-starter-parent</artifactId>
  <version>3.5.8</version>
</dependency>
```

但是SpringBoot官方推荐的不是直接引入依赖，而是采用继承的方式实现，如下：

```xml
<parent>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-parent</artifactId>
    <version>3.5.8</version>
</parent>
```

**为什么？**

---

## 作为父项目和作为依赖的区别

**继承父工程的优势**

+ 依赖管理：可以在父工程中定义依赖的版本，子模块可以直接引用而不必指定版本号。
+ 插件管理：可以在父工程中配置常用的插件及其版本，子模块可以直接使用这些配置。
+ 属性设置：可以在父工程中定义一些通用的属性，如项目编码、Java 版本等。
+ 统一配置：可以统一多个子模块的构建配置，确保一致性。

**直接引入依赖的局限性**（如果你不使用继承父工程的方式，而是通过直接引入依赖的方式来管理项目，那么你将失去上述的一些优势）

+ 依赖版本管理：每个子模块都需要单独指定依赖的版本，这会导致大量的重复配置，并且难以维护。
+ 插件配置：每个子模块都需要单独配置插件及其版本，无法共享父工程中的插件配置。
+ 属性设置：每个子模块都需要单独设置通用的属性，如项目编码、Java 版本等。
+ 构建配置：每个子模块的构建配置需要单独维护，难以保证一致性。

**总结：选择哪种方式取决于你的具体需求。**

+ **如果你希望多个项目之间共享构建配置，那么使用父项目是一个好的选择；**
+ **如果你只是想在项目之间共享代码，那么应该使用依赖关系。## 原理揭晓
通过源码来分析一下：

<img src="https://cdn.nlark.com/yuque/0/2024/png/21376908/1729322787542-83e28268-e350-4a0d-878d-b14d556588d8.png" width="721" title="" crop="0,0,1,1" id="u4f5fc831" class="ne-image">

<img src="https://cdn.nlark.com/yuque/0/2024/png/21376908/1729322856005-03b2b68d-b933-4fd2-ad79-dd7c98b3c47f.png" width="727" title="" crop="0,0,1,1" id="u05c02455" class="ne-image">

<img src="https://cdn.nlark.com/yuque/0/2024/png/21376908/1729322894485-d1bbdc9e-b225-4aa7-aee1-05b357e56777.png" width="847" title="" crop="0,0,1,1" id="u346581a6" class="ne-image">

通过上图源码可以看到Spring Boot预先对开发中需要用到的依赖进行了版本的统一管理。我们需要和SpringBoot框架共享这个构建配置。因此官方推荐使用继承的方式引入SpringBoot框架。**也就是说：每个 SpringBoot 版本都为我们提前打包好了一套兼容的、稳定的依赖库。我们使用 springboot，不需要手动指定某个依赖的版本，除非这个依赖没有被打包进 SpringBoot（SpringBoot 瞧不上它：嘿嘿）。

---

## 依赖统一管理的好处

Spring Boot 框架的一个重要特性就是简化了项目依赖管理。它通过提供一个叫做“依赖管理”的功能来帮助开发者更容易地管理和使用第三方库和其他 Spring 组件。具体来说，Spring Boot 提供了一个包含多个 Spring 和其他常用库的依赖版本配置文件（通常是在 `spring-boot-dependencies` 文件中），这使得开发者不需要在自己的项目中显式指定这些依赖的版本号。

这样做有以下几个好处：

1. **简化依赖声明**：  
开发者只需要在 `pom.xml` 文件中声明需要的依赖而不需要指定其版本号，因为 Spring Boot 已经为这些依赖指定了版本。例如，如果你需要使用mysql驱动，你只需要添加相应的依赖声明而不需要关心版本。

```xml
<dependency>
    <groupId>com.mysql</groupId>
    <artifactId>mysql-connector-j</artifactId>
</dependency>
```

2. **避免版本冲突**：  
当多个库之间存在依赖关系的时候，如果手动管理版本可能会导致版本之间的冲突（即“依赖地狱”）。Spring Boot 提供的统一版本管理可以减少这种冲突的可能性。
3. **易于升级**：  
当 Spring Boot 发布新版本时，通常会更新其依赖库到最新稳定版。因此，当你升级 Spring Boot 版本时，它所管理的所有依赖也会随之更新到兼容的版本。
4. **减少配置错误**：  
由于 Spring Boot 自动处理了依赖的版本，减少了手动输入版本号可能引入的拼写或格式错误。
5. **提高开发效率**：  
开发者可以专注于业务逻辑的编写，而不是花费时间在解决依赖问题上。

总的来说，Spring Boot 的依赖管理功能使得开发者可以更加专注于业务逻辑的实现，同时减少了因依赖版本不一致而引发的问题，提高了项目的可维护性和开发效率。

当然，如果你在项目中需要更改某个依赖的版本号，不想使用SpringBoot框架指定的版本号，只需要在引入依赖时强行执行版本号即可，maven是支持就近原则的：

这样做就是采用SpringBoot指定版本的依赖：

```xml
<dependency>
    <groupId>com.mysql</groupId>
    <artifactId>mysql-connector-j</artifactId>
</dependency>
```

<img src="https://cdn.nlark.com/yuque/0/2024/png/21376908/1729325886312-d3c4456c-5703-4982-9fc6-d3cd652ed1b9.png" width="421" title="" crop="0,0,1,1" id="u2408e6a6" class="ne-image">

这样做就是不采用SpringBoot指定版本的依赖：

```xml
<dependency>
    <groupId>com.mysql</groupId>
    <artifactId>mysql-connector-j</artifactId>
    <version>8.2.0</version>
</dependency>
```

<img src="https://cdn.nlark.com/yuque/0/2024/png/21376908/1729325956226-6f579f96-4e12-4c6b-99bc-dab8c044b9d4.png" width="430" title="" crop="0,0,1,1" id="u6a2c13df" class="ne-image">

