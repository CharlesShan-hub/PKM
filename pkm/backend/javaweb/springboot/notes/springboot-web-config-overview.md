# Web 中的核心配置类概述

---

## 共 27 个自动配置类

**如果是 web 开发，最终会留下 27 个自动配置类：**

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1765028276659-f02e9956-37a7-4f5f-8f1c-443808c3a385.png" width="399.2" title="" crop="0,0,1,1" id="uf26504a6" class="ne-image">

**分别是：**

```plain
0 = "org.springframework.boot.autoconfigure.admin.SpringApplicationAdminJmxAutoConfiguration"
1 = "org.springframework.boot.autoconfigure.aop.AopAutoConfiguration"
2 = "org.springframework.boot.autoconfigure.availability.ApplicationAvailabilityAutoConfiguration"
3 = "org.springframework.boot.autoconfigure.cache.CacheAutoConfiguration"
4 = "org.springframework.boot.autoconfigure.context.ConfigurationPropertiesAutoConfiguration"
5 = "org.springframework.boot.autoconfigure.context.LifecycleAutoConfiguration"
6 = "org.springframework.boot.autoconfigure.context.MessageSourceAutoConfiguration"
7 = "org.springframework.boot.autoconfigure.context.PropertyPlaceholderAutoConfiguration"
8 = "org.springframework.boot.autoconfigure.http.HttpMessageConvertersAutoConfiguration"
9 = "org.springframework.boot.autoconfigure.http.client.HttpClientAutoConfiguration"
10 = "org.springframework.boot.autoconfigure.info.ProjectInfoAutoConfiguration"
11 = "org.springframework.boot.autoconfigure.jackson.JacksonAutoConfiguration"
12 = "org.springframework.boot.autoconfigure.jmx.JmxAutoConfiguration"
13 = "org.springframework.boot.autoconfigure.sql.init.SqlInitializationAutoConfiguration"
14 = "org.springframework.boot.autoconfigure.ssl.SslAutoConfiguration"
15 = "org.springframework.boot.autoconfigure.task.TaskExecutionAutoConfiguration"
16 = "org.springframework.boot.autoconfigure.task.TaskSchedulingAutoConfiguration"
17 = "org.springframework.boot.autoconfigure.web.client.RestClientAutoConfiguration"
18 = "org.springframework.boot.autoconfigure.web.client.RestTemplateAutoConfiguration"
19 = "org.springframework.boot.autoconfigure.web.embedded.EmbeddedWebServerFactoryCustomizerAutoConfiguration"
20 = "org.springframework.boot.autoconfigure.web.servlet.DispatcherServletAutoConfiguration"
21 = "org.springframework.boot.autoconfigure.web.servlet.HttpEncodingAutoConfiguration"
22 = "org.springframework.boot.autoconfigure.web.servlet.MultipartAutoConfiguration"
23 = "org.springframework.boot.autoconfigure.web.servlet.ServletWebServerFactoryAutoConfiguration"
24 = "org.springframework.boot.autoconfigure.web.servlet.WebMvcAutoConfiguration"
25 = "org.springframework.boot.autoconfigure.web.servlet.error.ErrorMvcAutoConfiguration"
26 = "org.springframework.boot.autoconfigure.websocket.servlet.WebSocketServletAutoConfiguration"
```

---

## 服务器启动（2个）

**19. EmbeddedWebServerFactoryCustomizerAutoConfiguration**

+ **作用**：Web服务器专有配置器（Tomcat/Jetty专有配置）
+ **配置**：`server.tomcat.*`, `server.jetty.*`, `server.undertow.*`

**23. ServletWebServerFactoryAutoConfiguration**

+ **作用**：Web服务器通用配置
+ **配置**：`server.*`（通用：端口、SSL、上下文路径）

---

## Spring MVC核心（3个）

**20. DispatcherServletAutoConfiguration**

+ **作用**：创建Spring MVC核心DispatcherServlet
+ **配置**：`spring.mvc.servlet.*`

**24. WebMvcAutoConfiguration**

+ **作用**：配置完整Spring MVC框架
+ **配置**：`spring.mvc.*`（静态资源、视图解析等）

**25. ErrorMvcAutoConfiguration**

+ **作用**：全局错误处理
+ **配置**：`server.error.*`

---

## 数据处理（2个）

**11. JacksonAutoConfiguration**

+ **作用**：JSON处理（REST API必需），它是 SpringBoot 处理 JSON 时默认采用 Jackson 库。
+ **配置**：`spring.jackson.*`

**8. HttpMessageConvertersAutoConfiguration**

+ **作用**：HTTP消息转换器（JSON/XML转换）
+ **配置**：自动配置
+ **它会自动配置多个消息转换器**，其中 **MappingJackson2HttpMessageConverter** 使用的是**JacksonAutoConfiguration**

---

## Web增强功能（3个）

**21. HttpEncodingAutoConfiguration**

+ **作用**：字符编码过滤器（强制UTF-8）
+ **配置**：`server.servlet.encoding.*`

**22. MultipartAutoConfiguration**

+ **作用**：文件上传支持
+ **配置**：`spring.servlet.multipart.*`

**14. SslAutoConfiguration**

+ **作用**：SSL/TLS安全配置
+ **配置**：`server.ssl.*`

