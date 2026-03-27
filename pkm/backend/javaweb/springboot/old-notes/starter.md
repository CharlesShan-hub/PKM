# 自定义starter

在实际开发中，经常会定义一些公共组建，提供给各个团队使用。而在SpringBoot项目中，一般会将这些公共组建封装为SpringBoot的starter。

我们引入mybatis的时候，会引入`mybatis-spring-boot-starter`，现在我们做一个自己的起步依赖，就叫`dmybatis-spring-boot-starter`，提供自动配置功能，并提供META-INF/xxx.imports

我们首先创建两个空的maven项目。一个叫`dmybatis-spring-boot-starter`，一个叫`dmybatis-spring-boot-autoconfigure`。然后ArcheType选那个quickstart！

然后去看看引入`org.mybatis.spring.boot:mybatis-spring-boot-starter`的`maven`里边包含了什么内容：
* `org.springframework.boot:spring-boot-starter`
* `org.springframework.boot:spring-boot-starter-jdbc`
* `org.mybatis.spring.boot:mybatis-spring-boot-autoconfigure`
* `org.mybatis:mybatis`
* `org.mybatis:mybatis-spring`

因为我们要自己提供autoconfigure，所以我们引入除了这个以外的别的所有内容

`dmybatis-spring-boot-start`的`pom.xml`
```xml
<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"  
  xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">  
  <modelVersion>4.0.0</modelVersion>  
  
  <groupId>com.charles</groupId>  
  <artifactId>dmybatis-spring-boot-starter</artifactId>  
  <version>1.0-SNAPSHOT</version>  
  <packaging>jar</packaging>  
  
  <name>dmybatis-spring-boot-starter</name>  
  <url>http://maven.apache.org</url>  
  
  <properties>  
    <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>  
  </properties>  
  
  <dependencies>  
    <dependency>  
      <groupId>junit</groupId>  
      <artifactId>junit</artifactId>  
      <version>3.8.1</version>  
      <scope>test</scope>  
    </dependency>  
    <dependency>  
      <groupId>org.springframework.boot</groupId>  
      <artifactId>spring-boot-starter</artifactId>  
      <version>4.0.1</version>  
    </dependency>  
    <dependency>  
      <groupId>org.springframework.boot</groupId>  
      <artifactId>spring-boot-starter-jdbc</artifactId>  
      <version>4.0.1</version>  
    </dependency>  
    <dependency>  
      <groupId>org.mybatis</groupId>  
      <artifactId>mybatis</artifactId>  
      <version>3.5.19</version>  
    </dependency>  
    <dependency>  
      <groupId>org.mybatis</groupId>  
      <artifactId>mybatis-spring</artifactId>  
      <version>4.0.0</version>  
    </dependency>  
  </dependencies>  
</project>
```

然后我们开始写自己的自动配置类，在`dmybatis-spring-boot-autoconfigure`里边创建

```java

```