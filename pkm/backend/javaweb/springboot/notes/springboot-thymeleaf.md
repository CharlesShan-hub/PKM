# SpringBoot整合Thymeleaf

---

## 传统web应用和前后端分离

如果你是做前后端分离的项目，这一章节的内容将用不上。

现代开发大部分应用都会采用前后端分离的方式进行开发，前端是一个独立的系统，后端也是一个独立的系统，后端系统只给前端系统提供数据（JSON数据），不需要后端解析模板页面，前端系统拿到后端提供的数据之后，前端负责填充数据即可。因此这一章节内容作为了解。

传统的WEB应用（非前后端分离）：浏览器页面上展示成什么效果，后端服务器说了算，这是传统web应用最大的特点。

<img src="https://cdn.nlark.com/yuque/0/2024/png/21376908/1730789733440-1dc2d749-19c5-4363-b35d-bf6e6008265c.png" width="1168" title="" crop="0,0,1,1" id="u46582415" class="ne-image">

前后端分离的应用：前端是一个独立的系统，后端也是一个独立的系统，后端系统不再负责页面的渲染，后端系统只负责给前端系统提供开放的API接口，后端系统只负责数据的收集，然后将数据以JSON/XML等格式响应给前端系统。前端系统拿到接口返回的数据后，将数据填充到页面上。

<img src="https://cdn.nlark.com/yuque/0/2024/png/21376908/1730790760614-212e3911-eb37-4dca-88a4-eca6ecd26dba.png" width="1127" title="" crop="0,0,1,1" id="u6f6e55ce" class="ne-image">

前后端分离的好处：

+ 职责清晰：前端专注于用户界面和用户体验，后端专注于业务逻辑和数据处理。
+ 开发效率高：前后端可以并行开发，互不影响，提高开发速度。
+ 可维护性强：代码结构更清晰，便于维护和扩展。
+ 技术栈灵活：前后端可以独立选择最适合的技术栈。
+ 响应式设计：前端可以更好地处理不同设备和屏幕尺寸。
+ 性能优化：前后端可以独立优化，提升整体性能。
+ 易于测试：前后端接口明确，便于单元测试和集成测试。

---

## SpringBoot整合Thymeleaf

**提醒：SpringBoot内嵌了Servlet容器（例如：Tomcat、Jetty等），使用SpringBoot不太适合使用JSP模板技术，因为SpringBoot项目最终打成jar包之后，放在jar包中的jsp文件不能被Servlet容器解析。**

要在SpringBoot中整合Thymeleaf，按照以下步骤操作：

**第一步：**引入thymeleaf启动器

```xml
<dependency>
  <groupId>org.springframework.boot</groupId>
  <artifactId>spring-boot-starter-thymeleaf</artifactId>
</dependency>
```

**第二步：**编写配置文件，指定前缀和后缀（**默认不配置就是以下配置**）

```properties
spring.thymeleaf.prefix=classpath:/templates/
spring.thymeleaf.suffix=.html
```

**第三步：**编写控制器

```java
package com.jkweilai.springboot.controller;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;

// 不能使用 @RestController
@Controller
public class HelloController {

    @GetMapping("/h")
    public String helloThymeleaf(@RequestParam("name") String name, Model model) {
        // 将接收到的name数据存储到域对象中
        model.addAttribute("name", name);
        // 逻辑视图名
        return "hello"; // 最终的物理视图名：classpath:/templates/hello.html
    }
}
```

**第四步：**编写thymeleaf模板页面

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>hello, thymeleaf</title>
</head>
<body>
<h1>hello,<span th:text="${name}"></span></h1>
</body>
</html>
```

启动服务器，测试地址为：http://localhost:8080/h

<img src="https://cdn.nlark.com/yuque/0/2024/png/21376908/1730792132534-7b9358f0-98ff-43dc-8624-1717683b15aa.png" width="407" title="" crop="0,0,1,1" id="uc5daf1e9" class="ne-image">

---

## 将路径直接映射到视图

**在springboot中如何实现：直接将请求路径映射到特定的视图，而不需要编写controller？**

使用`ViewControllerRegistry`进行视图与控制器的注册

```java
package com.jkweilai.springboot.config;

import org.springframework.context.annotation.Configuration;
import org.springframework.web.servlet.config.annotation.ViewControllerRegistry;
import org.springframework.web.servlet.config.annotation.WebMvcConfigurer;

@Configuration
public class WebMvcConfig implements WebMvcConfigurer {

    @Override
    public void addViewControllers(ViewControllerRegistry registry) {
        registry.addViewController("/a").setViewName("a");
        registry.addViewController("/b").setViewName("b");
    }
}

```

**前提：**你需要将 `a.html`放到 `classpath:/templates/`目录下。

