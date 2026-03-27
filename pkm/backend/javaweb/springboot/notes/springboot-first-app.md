# First Spring Boot

需求：在浏览器上输入请求路径 http://localhost:8080/hello，在浏览器上显示 HelloWorld!

使用**Spring Boot3 开发web应用**，实现步骤如下：

---

## 第一步：创建一个空的工程，并设置JDK版本21

Spring Boot 3要求JDK最低版本是17

---

## 第二步：设置maven

---

## 第三步：创建一个Maven模块 sb3-01-first-web

---

## 第四步：打开Spring Boot 3官方文档，按照文档一步一步进行

<img src="https://cdn.nlark.com/yuque/0/2024/png/21376908/1726111379585-fd90758d-f6bd-4a71-9ba9-b1549dd18c84.png" width="1435" title="" crop="0,0,1,1" id="u20fe7d93" class="ne-image">

<img src="https://cdn.nlark.com/yuque/0/2024/png/21376908/1726111411632-0a5cfc79-f222-4395-ae19-35b8d3868f3d.png" width="1397" title="" crop="0,0,1,1" id="ua754be37" class="ne-image">

---

## 第五步：要使用Spring Boot 3，需要继承这个开源项目。从官方指导文档中复制以下内容：

<img src="https://cdn.nlark.com/yuque/0/2024/png/21376908/1726111736067-221c85d6-e3ce-4d41-9b20-2893705b11de.png" width="1193" title="" crop="0,0,1,1" id="uc8da12ee" class="ne-image">

```xml
<!--继承Spring Boot 3.5.8开源项目-->
<parent>
  <groupId>org.springframework.boot</groupId>
  <artifactId>spring-boot-starter-parent</artifactId>
  <version>3.5.8</version>
</parent>
```

我们开发的每一个项目其实可以看做是 Spring Boot 项目下的子项目。

**思考：使用 springboot 框架为什么和之前框架感觉不一样，以前我们学习框架的的时候，用它就引入它的依赖，但 springboot 这里是继承方式，而不是直接引入它的依赖。为什么呢？**

---

## 第六步：添加Spring Boot的web starter

<img src="https://cdn.nlark.com/yuque/0/2024/png/21376908/1726112199621-1d90cda6-1bb5-4c66-ac9f-b0f2bedb87b3.png" width="1205" title="" crop="0,0,1,1" id="u50bdf0fc" class="ne-image">

在parent下立即添加如下配置，让Spring Boot项目具备开发web应用的依赖：

```xml
<dependencies>
    <!--引入Spring Boot web启动器依赖-->
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-web</artifactId>
    </dependency>
</dependencies>
```

关联的依赖也被引入进来，如下：

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1764847827355-3257c228-5568-4680-8495-fd4321ac4f2f.png" width="444" title="" crop="0,0,1,1" id="u3eec3d7c" class="ne-image">

可以看到spring mvc被引入了，tomcat服务器也被引入了。

---

## 第七步：编写Spring Boot主入口程序

```java
package com.jkweilai.springboot;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class MyApplication {
    public static void main(String[] args) {
        SpringApplication.run(MyApplication.class, args);
    }
}

```

---

## 第八步：编写controller

```java
package com.jkweilai.springboot.controller;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class HelloController {
    
    @GetMapping("/hello")
    public String hello(){
        return "Hello World!";
    }
}

```

---

## 第九步：运行main方法就是启动web容器

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1764848081916-20d5b937-ce54-405c-8205-3ec8ee9afdda.png" width="1195.2" title="" crop="0,0,1,1" id="u7dc77bce" class="ne-image">

---

## 第十步：打开浏览器访问

[http://localhost:8080/hello](http://localhost:8080/hello)

<img src="https://cdn.nlark.com/yuque/0/2024/png/21376908/1726113139402-b64d1c16-9055-495c-aa3d-1ef13baf9816.png" width="376" title="" crop="0,0,1,1" id="uf6009535" class="ne-image">

