# Web自动配置都默认配置了什么

**查看官方文档：**

<img src="https://cdn.nlark.com/yuque/0/2024/png/21376908/1731383415638-90d102e9-1fd0-4f31-9736-9e3bef3936d3.png" width="1555" title="" crop="0,0,1,1" id="ub2ad605c" class="ne-image">

**翻译如下：## 视图解析器
+ **包括 ContentNegotiatingViewResolver 和 BeanNameViewResolver 的 Bean。**
    - **ContentNegotiatingViewResolver**：自动根据 HTTP 请求头中 Accept 字段来选择合适的视图技术渲染响应。
    - **BeanNameViewResolver**：根据视图名称找到视图 View 对象。

---

## 静态资源支持

+ **支持提供静态资源，包括对 WebJars 的支持。**
    - 静态资源路径默认已经配置好了。默认会去 static 目录下找。

---

## 数据转换与格式化

+ **自动注册 Converter 和 Formatter 的 Bean。**
    - **Converter**：转换器，做类型转换的，例如表单提交了用户数据，将表单数据转换成 User 对象。
    - **Formatter**：格式化器，做数据格式化的，例如将 Java 中的日期类型对象格式化为特定格式的日期字符串。或者将用户提交的日期字符串，转换为 Java 中的日期对象。

---

## HTTP 消息转换

+ **支持 HttpMessageConverters。**
    - 内置了很多的 HTTP 消息转换器。例如：MappingJackson2HttpMessageConverter 可以将 json 转换成 java 对象，也可以将 java 对象转换为 json 字符串。

---

## 消息代码解析

+ **自动注册 MessageCodesResolver。**
    - SpringBoot 会自动注册一个默认的消息代码解析器。
    - 帮助你在表单验证出错时生成一些特殊的代码。这些代码让你能够更精确地定位问题，并提供更友好的错误提示。

---

## 默认主页支持

+ **静态 index.html 文件支持。**
    - Spring Boot 会自动处理位于项目静态资源目录下的 index.html 文件，使其成为应用程序的默认主页。

---

## 数据绑定初始化

+ **自动使用 ConfigurableWebBindingInitializer Bean。**
    - 用它来指定默认使用哪个转换器，默认使用哪个格式化器。在这个类当中都已经配好了。

---

## 自定义配置说明

+ 自己想完全控制 Spring MVC，使用 `@EnableWebMvc`+`@Configuration`，自己写一个配置类。（**不推荐！！！）
+ 如果你希望保留默认配置并进行扩展（如拦截器、格式化程序、视图控制器等其他功能），编写类实现`WebMvcConfigurer`接口+`@Configuration` 类。**但不能使用 **`@EnableWebMvc`** 注解。**

