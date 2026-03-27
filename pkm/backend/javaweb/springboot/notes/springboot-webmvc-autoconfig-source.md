# **WebMvcAutoConfiguration 源码解释**

---

## WebMvc自动配置是否生效的条件

```java
// 先加载这几个类，然后再加载WebMvcAutoConfiguration
@AutoConfiguration(after = { DispatcherServletAutoConfiguration.class, TaskExecutionAutoConfiguration.class,ValidationAutoConfiguration.class })
// 必须是一个web应用，WebMvcAutoConfiguration才会生效
@ConditionalOnWebApplication(type = Type.SERVLET)
// 类路径中必须存在这几个类，WebMvcAutoConfiguration才会生效
@ConditionalOnClass({ Servlet.class, DispatcherServlet.class, WebMvcConfigurer.class })
// 如果有这样一个Bean，WebMvcAutoConfiguration不生效
// 针对这个可以看一下@EnableWebMvc注解，你会发现它导入了DelegatingWebMvcConfiguration，而它继承了WebMvcConfigurationSupport
// 因此当我们使用 @EnableWebMvc注解时，默认配置会全部失效
@ConditionalOnMissingBean(WebMvcConfigurationSupport.class)
// 以下这两个不重要
@AutoConfigureOrder(Ordered.HIGHEST_PRECEDENCE + 10)
@ImportRuntimeHints(WebResourcesRuntimeHints.class)
public class WebMvcAutoConfiguration {}
```

---

## WebMvc自动配置生效后引入了两个Filter Bean

### 引入了**HiddenHttpMethodFilter Bean**

```java
@Bean
@ConditionalOnMissingBean(HiddenHttpMethodFilter.class)
@ConditionalOnProperty(prefix = "spring.mvc.hiddenmethod.filter", name = "enabled")
public OrderedHiddenHttpMethodFilter hiddenHttpMethodFilter() {
    return new OrderedHiddenHttpMethodFilter();
}
```

提供对浏览器表单支持PUT、DELETE等HTTP方法的兼容处理

### 引入了**FormContentFilter Bean**

```java
@Bean
@ConditionalOnMissingBean(FormContentFilter.class)
@ConditionalOnProperty(prefix = "spring.mvc.formcontent.filter", name = "enabled", matchIfMissing = true)
public OrderedFormContentFilter formContentFilter() {
    return new OrderedFormContentFilter();
}
```

**解析并处理**`**application/x-www-form-urlencoded**`**格式的PUT、DELETE请求体数据。**

---

## WebMvc自动配置生效后引入了WebMvcConfigurer接口的实现类

**知识点清单：**

1. `**WebMvcAutoConfiguration**`**类中的静态内部类**`**WebMvcAutoConfigurationAdapter**`**实现了WebMvcConfigurer 接口。**
2. **这个接口的实现我们之前写过，在 SpringMVC 全注解开发时写过。因此 SpringBoot 对 MVC 的默认配置都在这个内部类中。**
3. **想修改默认配置：在 application.yml 文件中配置**`**spring.mvc**`**、**`**spring.web**`
4. **想对默认配置进行扩展，例如添加拦截器：编写类实现**`**WebMvcConfigurer**`**接口+**`**@Configuration**`

在SpringBoot框架的`WebMvcAutoConfiguration`类中提供了一个内部类：`WebMvcAutoConfigurationAdapter`

<img src="https://cdn.nlark.com/yuque/0/2024/png/21376908/1730345630650-62e11666-3e95-4c64-9787-c0b18d083c91.png" width="1080" title="" crop="0,0,1,1" id="ue6dbe412" class="ne-image">

SpringBoot在这个类`WebMvcAutoConfigurationAdapter`中进行了一系列的Spring MVC相关配置。

### 关于`WebMvcConfigurer`接口

这个接口我们以前就用过。在 SpringMVC 中进行全注解式开发时就用了。在这个接口中提供了很多方法，需要改变Spring MVC的哪个行为，则重写对应的方法即可，下面是这个接口中所有的方法，以及每个方法对应的Spring MVC行为的解释：

```java
public interface WebMvcConfigurer {
    // 用于定制 Spring MVC 如何匹配请求路径到控制器
    default void configurePathMatch(PathMatchConfigurer configurer) {}
    // 用于定制 Spring MVC 的内容协商策略，以确定如何根据请求的内容类型来选择合适的处理方法或返回数据格式
    default void configureContentNegotiation(ContentNegotiationConfigurer configurer) {}
    // 用于定制 Spring MVC 处理异步请求的方式
    default void configureAsyncSupport(AsyncSupportConfigurer configurer) {}
    // 用于定制是否将某些静态资源请求转发WEB容器默认的Servlet处理
    default void configureDefaultServletHandling(DefaultServletHandlerConfigurer configurer) {}
    // 用于定制 Spring MVC 解析视图的方式，以确定如何将控制器返回的视图名称转换为实际的视图资源。
    default void configureViewResolvers(ViewResolverRegistry registry) {}
    // 用于定制 Spring MVC 如何处理 HTTP 请求和响应的数据格式，包括 JSON、XML 等内容类型的转换
    default void configureMessageConverters(List<HttpMessageConverter<?>> converters) {}
    // 用于定制 Spring MVC 如何处理控制器方法中发生的异常，并提供相应的错误处理逻辑。
    default void configureHandlerExceptionResolvers(List<HandlerExceptionResolver> resolvers) {}

    // 用于定制 Spring MVC 如何处理数据的格式化和解析，例如日期、数值等类型的对象的输入和输出格式。
    default void addFormatters(FormatterRegistry registry) {}
    // 用于定制 Spring MVC 如何使用拦截器来处理请求和响应，包括在请求进入控制器之前和之后执行特定的操作。
    default void addInterceptors(InterceptorRegistry registry) {}
    // 用于定制 Spring MVC 如何处理静态资源（如 CSS、JavaScript、图片等文件）的请求。
    default void addResourceHandlers(ResourceHandlerRegistry registry) {}
    // 用于定制 Spring MVC 如何处理跨域请求，确保应用程序可以正确地响应来自不同域名的 AJAX 请求或其他跨域请求。
    default void addCorsMappings(CorsRegistry registry) {}
    // 用于快速定义简单的 URL 到视图的映射，而无需编写完整的控制器类和方法。
    default void addViewControllers(ViewControllerRegistry registry) {}
    // 用于定制 Spring MVC 如何解析控制器方法中的参数，包括如何从请求中获取并转换参数值。
    default void addArgumentResolvers(List<HandlerMethodArgumentResolver> resolvers) {}
    // 用于定制 Spring MVC 如何处理控制器方法的返回值，包括如何将返回值转换为实际的 HTTP 响应。
    default void addReturnValueHandlers(List<HandlerMethodReturnValueHandler> handlers) {}

    // 用于定制 Spring MVC 如何处理 HTTP 请求和响应的数据格式，允许你添加或调整默认的消息转换器，以支持特定的数据格式。
    default void extendMessageConverters(List<HttpMessageConverter<?>> converters) {}
    // 用于定制 Spring MVC 如何处理控制器方法中抛出的异常，允许你添加额外的异常处理逻辑。
    default void extendHandlerExceptionResolvers(List<HandlerExceptionResolver> resolvers) {}
}
```

### `WebMvcConfigurer`接口的实现类`WebMvcAutoConfigurationAdapter`

`WebMvcAutoConfigurationAdapter`是Spring Boot框架提供的，实现了Spring MVC中的`WebMvcConfigurer`接口，对Spring MVC的所有行为进行了默认的配置。

如果想要改变这些默认配置，应该怎么办呢？看源码：

<img src="https://cdn.nlark.com/yuque/0/2024/png/21376908/1730353008999-076f3b3f-2a0b-4936-a9f2-5d6cfe88b346.png" width="1010" title="" crop="0,0,1,1" id="u0962da1b" class="ne-image">

可以看到，该类上有一个注解`@EnableConfigurationProperties({ WebMvcProperties.class, WebProperties.class })`，该注解负责启用配置属性。会将配置文件`application.properties`或`application.yml`中的配置传递到该类中。因此可以通过`application.properties`或`application.yml`配置文件来改变Spring Boot对SpringMVC的默认配置。`WebMvcProperties`和`WebProperties`源码如下： 

<img src="https://cdn.nlark.com/yuque/0/2024/png/21376908/1730354494823-2adf83a4-aa2a-4fed-a5df-66b156de15c5.png" width="565" title="" crop="0,0,1,1" id="ua84cb938" class="ne-image">

<img src="https://cdn.nlark.com/yuque/0/2024/png/21376908/1730354507221-6424a72a-0728-478b-92eb-e52d3d5a6f38.png" width="425" title="" crop="0,0,1,1" id="ue279b932" class="ne-image">

通过以上源码得知要改变SpringBoot对SpringMVC的默认配置，需要在配置文件中使用以下前缀的配置：

+ spring.mvc：**主要用于配置 Spring MVC 的相关行为，例如路径匹配、视图解析、静态资源处理等**
+ spring.web：通常用于配置一些通用的 Web 层设置，如资源处理、安全性配置等。

---

## 一个小小的疑惑

我们来看一下`WebMvcAutoConfiguration`的生效条件：

<img src="https://cdn.nlark.com/yuque/0/2024/png/21376908/1730424986145-0d76b7da-06c5-4942-a5f2-3e55f0249c89.png" width="1130" title="" crop="0,0,1,1" id="iBmex" class="ne-image">

上图红框内表示，要求Spring容器中缺失`WebMvcConfigurationSupport`这个Bean，`WebMvcAutoConfiguration`才会生效。

但是我们来看一下`EnableWebMvcConfiguration`的继承结构：

<img src="https://cdn.nlark.com/yuque/0/2024/png/21376908/1730425120392-dda2febe-d932-452c-9599-6df5859a2062.png" width="376" title="" crop="0,0,1,1" id="f94jB" class="ne-image">

很明显，`EnableWebMvcConfiguration`就是一个`WebMvcConfigurationSupport`这样的Bean。

那疑问就有了：既然容器中存在`WebMvcConfigurationSupport`这样的Bean，`WebMvcAutoConfiguration`为什么还会生效呢？

原因是因为：`EnableWebMvcConfiguration`是`WebMvcAutoConfiguration`类的内部类。在`WebMvcAutoConfiguration`进行加载的时候，`EnableWebMvcConfiguration`这个内部类还没有加载。因此这个时候在容器中还不存在`WebMvcConfigurationSupport`的Bean，所以`WebMvcAutoConfiguration`仍然会生效。

**以上所说的**`**WebMvcAutoConfiguration**`**类中的内部类**`**EnableWebMvcConfiguration**`**，是用来启用Web MVC默认配置的。**注意区分：WebMvcAutoConfiguration的两个内部类：

+ `WebMvcAutoConfigurationAdapter`作用是用来：**配置 MVC 的**。
+ `EnableWebMvcConfiguration`作用是用来：**启用 MVC 配置的**。

