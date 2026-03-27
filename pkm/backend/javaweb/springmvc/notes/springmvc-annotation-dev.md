# **SpringMVC 全注解开发**

---

## web.xml文件的替代

### Servlet3.0新特性

Servlet3.0新特性：web.xml文件可以不写了。

在Servlet3.0的时候，规范中提供了一个接口：

<img src="https://cdn.nlark.com/yuque/0/2024/png/21376908/1711700341492-8c9a85d9-bca5-484f-8d5d-c3939f48db95.png" width="921" title="" crop="0,0,1,1" id="u141ebb8e" class="ne-image">

服务器在启动的时候会自动从容器中找 `ServletContainerInitializer`接口的实现类，自动调用它的`onStartup`方法来完成Servlet上下文的初始化。

在Spring3.1版本的时候，提供了这样一个类，实现以上的接口：

<img src="https://cdn.nlark.com/yuque/0/2024/png/21376908/1711700544729-77092224-626d-4b76-8408-f3744fe2ad72.png" width="939" title="" crop="0,0,1,1" id="ua7872bf7" class="ne-image">

它的核心方法如下：

<img src="https://cdn.nlark.com/yuque/0/2024/png/21376908/1711700669446-3bcc469c-71d3-423a-86f7-52e95b73f344.png" width="1149" title="" crop="0,0,1,1" id="uf4b1d92d" class="ne-image">

可以看到在服务器启动的时候，它会去加载所有实现`WebApplicationInitializer`接口的类：

<img src="https://cdn.nlark.com/yuque/0/2024/png/21376908/1711700736674-05682c42-1904-4311-aede-b2e7994bfabf.png" width="803" title="" crop="0,0,1,1" id="ub1510e11" class="ne-image">

这个接口下有一个子类是我们需要的：`AbstractAnnotationConfigDispatcherServletInitializer`

<img src="https://cdn.nlark.com/yuque/0/2024/png/21376908/1711700804612-90b68082-5b55-4084-90fb-c230f6aed3a9.png" width="681" title="" crop="0,0,1,1" id="u1135318a" class="ne-image">

当我们编写类继承`AbstractAnnotationConfigDispatcherServletInitializer`之后，web服务器在启动的时候会根据它来初始化Servlet上下文。

<img src="https://cdn.nlark.com/yuque/0/2024/png/21376908/1711701535524-d2635ca6-3bae-4613-9dbb-ed6cb0b7dca6.png" width="813" title="" crop="0,0,1,1" id="uc2f1acbd" class="ne-image">

### 编写WebAppInitializer

以下这个类就是用来代替web.xml文件的：

```java

package com.jkweilai.springmvc.config;

import jakarta.servlet.Filter;
import org.springframework.web.filter.CharacterEncodingFilter;
import org.springframework.web.filter.HiddenHttpMethodFilter;
import org.springframework.web.servlet.support.AbstractAnnotationConfigDispatcherServletInitializer;

// 以下配置是代替 web.xml 的。
// 等同于在web.xml文件中配置DispatcherServlet
// 1.指定springmvc.xml文件的位置。
// 2.指定在服务器启动时加载。（不需要指定，指定扫描包的时候，能扫描到即可）
// 3.配置映射路径url-pattern
// 4.字符编码过滤器
// 5.HiddenHttpMethodFilter

// 本身是一个 Servlet容器初始化器，它的生命周期由 Servlet容器（如Tomcat）管理，而不是由Spring容器管理。
// WebConfig 类的作用是：配置DispatcherServlet本身，它会在Spring容器启动之前就被Servlet容器调用。
// @Configuration  // 不能添加 @Configuration 注解
public class WebConfig extends AbstractAnnotationConfigDispatcherServletInitializer {

    // 我们之前写的springmvc.xml文件中的配置，既有spring的配置，又有springmvc的配置
    // 中大型项目一般都将这两个配置分开，我们这里将springmvc.xml拆分为两个配置类。
    // 1. SpringConfig 类编写Spring配置。
    // 2. SpringMvcConfig 类编写SpringMVC配置。

    // 指定Spring的配置
    @Override
    protected Class<?>[] getRootConfigClasses() {
        return new Class[]{SpringConfig.class};
    }

    // 指定SpringMVC的配置
    @Override
    protected Class<?>[] getServletConfigClasses() {
        return new Class[]{SpringMvcConfig.class};
    }

    // 配置DispatcherServlet的 url-pattern
    @Override
    protected String[] getServletMappings() {
        return new String[]{"/"};
    }

    // 配置字符编码过滤器以及RESTful过滤器
    @Override
    protected Filter[] getServletFilters() {
        CharacterEncodingFilter characterEncodingFilter = new CharacterEncodingFilter();
        characterEncodingFilter.setEncoding("UTF-8");
        characterEncodingFilter.setForceRequestEncoding(true);
        characterEncodingFilter.setForceResponseEncoding(true);
        HiddenHttpMethodFilter hiddenHttpMethodFilter = new HiddenHttpMethodFilter();
        return new Filter[]{characterEncodingFilter, hiddenHttpMethodFilter};
    }
}

```

Spring配置如下：

```java

package com.jkweilai.springmvc.config;

import org.springframework.context.annotation.Configuration;

@Configuration
public class SpringConfig {
}

```

SpringMVC配置如下：

```java

package com.jkweilai.springmvc.config;

import org.springframework.context.annotation.Configuration;

@Configuration
public class SpringMvcConfig {
}

```

---

## Spring 配置

组件扫描我们归纳到 Spring 的配置下：

```java

package com.jkweilai.springmvc.config;

import org.springframework.context.annotation.Configuration;

// 以后这这里配置Spring相关的配置，例如：数据源、事务管理器等。
@Configuration
public class SpringConfig {
}

```

---

## Spring MVC的配置

重点注意事项：SpringMVC 的配置类需要实现一个固定的接口 `**WebMvcConfigurer**`

### 开启注解驱动及扫描 controller

```java

package com.jkweilai.springmvc.config;

import org.springframework.context.annotation.Configuration;
import org.springframework.web.servlet.config.annotation.EnableWebMvc;
import org.springframework.web.servlet.config.annotation.WebMvcConfigurer;

@Configuration
@EnableWebMvc // 代替：<mvc:annotation-driven/>
// 注意：所有controller的扫描需要放到 SpringMvcConfig中，如果只放到 SpringConfig 中进行扫描是不行的。
@ComponentScan(basePackages = {"com.jkweilai.springmvc.controller"}) 
public class SpringMvcConfig implements WebMvcConfigurer {
}

```

**使用了**`**@EnableWebMvc**`**，你的类******必须实现****`****WebMvcConfigurer****`****接口******来配置静态资源处理，否则所有静态资源（CSS、JS、图片）都无法访问。**

### 视图解析器

```java

// 配置Thymeleaf视图解析器
@Bean
public ThymeleafViewResolver thymeleafViewResolver() {
    ThymeleafViewResolver viewResolver = new ThymeleafViewResolver();
    viewResolver.setTemplateEngine(templateEngine());
    viewResolver.setCharacterEncoding("UTF-8");
    viewResolver.setOrder(1);
    return viewResolver;
}

private SpringTemplateEngine templateEngine() {
    SpringTemplateEngine engine = new SpringTemplateEngine();
    engine.setTemplateResolver(templateResolver());
    return engine;
}

@Bean
public SpringResourceTemplateResolver templateResolver() {
    SpringResourceTemplateResolver resolver = new SpringResourceTemplateResolver();
    resolver.setPrefix("/WEB-INF/templates/");
    resolver.setSuffix(".html");
    resolver.setTemplateMode(TemplateMode.HTML);
    resolver.setCharacterEncoding("UTF-8");
    resolver.setCacheable(false);
    return resolver;
}

```

### 配置静态资源

```java

// 静态资源配置
@Override
public void addResourceHandlers(ResourceHandlerRegistry registry) {
    registry.addResourceHandler("/static/**")
            .addResourceLocations("/static/")
            .setCachePeriod(3600);
}

```

### 配置 view-controller

```java

// 配置视图控制器（对于没有业务的Controller可以直接配置，不需要写）
@Override
public void addViewControllers(ViewControllerRegistry registry) {
    registry.addViewController("/").setViewName("index");
}

```

### 配置拦截器

**编写拦截器：**

```java

package com.jkweilai.springmvc.interceptor;

import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.servlet.HandlerInterceptor;

public class SecurityInterceptor implements HandlerInterceptor {

    @Override
    public boolean preHandle(HttpServletRequest request, HttpServletResponse response, Object handler) throws Exception {
        System.out.println("拦截器执行，检查你有没有权限...");
        return true;
    }
}

```

```java

package com.jkweilai.springmvc.interceptor;

import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.servlet.HandlerInterceptor;

public class LogInterceptor implements HandlerInterceptor {
    @Override
    public boolean preHandle(HttpServletRequest request, HttpServletResponse response, Object handler) throws Exception {
        System.out.println("拦截器执行，我用来记录操作日志...");
        return true;
    }
}

```

**配置拦截器：**

```java

// 配置拦截器
@Override
public void addInterceptors(InterceptorRegistry registry) {
    // 安全拦截器
    SecurityInterceptor securityInterceptor = new SecurityInterceptor();
    // 指定哪些路径拦截，哪些不拦截
    registry.addInterceptor(securityInterceptor).addPathPatterns("/**").excludePathPatterns("/test");
    // 日志拦截器
    LogInterceptor logInterceptor = new LogInterceptor();
    // 指定哪些路径拦截，哪些不拦截
    registry.addInterceptor(logInterceptor).addPathPatterns("/**").excludePathPatterns("/test");
}

```

---

## 编写测试程序进行测试

**创建好对应的文件、目录及程序：**

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1764837321272-9f6fb38a-7d7c-4aad-a627-fb8d38efdba9.png" width="326.4" title="" crop="0,0,1,1" id="u28e32141" class="ne-image">

`**index.html**`

```html

<!DOCTYPE html>
<html lang="en" xmlns:th="http://www.thymeleaf.org">
<head>
    <meta charset="UTF-8">
    <title>index page</title>
</head>
<body>
<h1>测试SpringMVC全注解开发</h1>
<h3><a th:href="@{/test}"><img width="100px" th:src="@{/static/1.jpg}"/></a></h3>
</body>
</html>

```

****

`**success.html**`

```html

<!DOCTYPE html>
<html lang="en" xmlns:th="http://www.thymeleaf.org">
<head>
    <meta charset="UTF-8">
    <title>index page</title>
</head>
<body>
<h1>success</h1>
</body>
</html>

```

`**TestController**`

```java

package com.jkweilai.springmvc.controller;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;

@Controller
public class TestController {

    @GetMapping("/test")
    public String test(){
        return "success";
    }
}

```

**访问首页面：**[**http://localhost:8080/springmvc/**](http://localhost:8080/springmvc/)

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1764837484207-1688c52b-0046-4d91-8fe6-a0dbde5268df.png" width="467.2" title="" crop="0,0,1,1" id="u038812f9" class="ne-image">

**观察后端，拦截器是否执行：**

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1764837513997-59b144e7-a8a6-45cb-97c3-b2538052daf6.png" width="341.6" title="" crop="0,0,1,1" id="u361a425a" class="ne-image">

**再发送 **`**/test**`**请求：**[**http://localhost:8080/springmvc/test**](http://localhost:8080/springmvc/test)

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1764837543320-be1f1649-4b13-47d7-be8d-475a98739f3d.png" width="415.2" title="" crop="0,0,1,1" id="uc8f30306" class="ne-image">
