# 设置静态资源的请求路径的前缀

spring.mvc.static-path-pattern=/static/**

```

要修改`静态资源的存放位置`，这样配置：

```properties

spring.web.resources.static-locations=classpath:/static1/,classpath:/static2/

```

进行以上配置之后：

1. 访问静态资源的请求路径应该是这样的：http://localhost:8080/static/....
2. 静态资源的存放位置也应该放到`classpath:/static1/,classpath:/static2/`下面，其他位置无效。

**访问静态资源测试结果如下：**

<img src="https://cdn.nlark.com/yuque/0/2024/png/21376908/1730433000967-37e76b55-5715-4387-a135-5daacd53a755.png" width="229" title="" crop="0,0,1,1" id="ubdb65472" class="ne-image">

<img src="https://cdn.nlark.com/yuque/0/2024/png/21376908/1730433110267-b2f84e91-6b95-48d3-88d6-acff3dca26cc.png" width="410" title="" crop="0,0,1,1" id="u1a2b2598" class="ne-image">

<img src="https://cdn.nlark.com/yuque/0/2024/png/21376908/1730433134598-5ac4583f-e7c1-4a8e-a3bb-77e2a3a33ac7.png" width="331" title="" crop="0,0,1,1" id="ub90c36bc" class="ne-image">

如果访问`dog2.jpg`，就无法访问了：

<img src="https://cdn.nlark.com/yuque/0/2024/png/21376908/1730433508569-ce398096-8cae-42e3-b6a2-5fe94e2a007a.png" width="528" title="" crop="0,0,1,1" id="ue129b260" class="ne-image">

但是，存储在`classpath:/META-INF/resources/`目录下的`dog1.jpg`仍然是可以访问的：

<img src="https://cdn.nlark.com/yuque/0/2024/png/21376908/1730433537233-e7fe1330-22d3-4b36-8c43-bbdc9a578f99.png" width="326" title="" crop="0,0,1,1" id="u13abe56d" class="ne-image">

因此，存储在`classpath:/META-INF/resources/`位置的静态资源会被默认加载，不受手动配置的影响。

---

## 编写代码方式

编写代码方式又包括两种方式：

+ 第一种：编写类实现`WebMvcConfigurer`接口+`@Configuration`，重写对应的方法。
+ 第二种：编写一个方法，用`@Bean`注解标注。

### 第一种方式

因此在SpringBoot主入口程序同级目录下新建`config`包，在`config`包下新建`WebConfig`类：

```java

package com.jkweilai.springboot.config;

import org.springframework.context.annotation.Configuration;
import org.springframework.web.servlet.config.annotation.ResourceHandlerRegistry;
import org.springframework.web.servlet.config.annotation.WebMvcConfigurer;

// 使用该注解标注，表示该类为配置类。
@Configuration
public class WebConfig implements WebMvcConfigurer {
    @Override
    public void addResourceHandlers(ResourceHandlerRegistry registry) {
        registry.addResourceHandler("/static/**")
                .addResourceLocations("classpath:/static1/", "classpath:/static2/");
    }
}

```

注意：将`application.properties`文件中之前的所有配置全部注释掉。让其恢复到最原始的默认配置。

<img src="https://cdn.nlark.com/yuque/0/2024/png/21376908/1730444156893-d646065e-96dc-449c-a8cc-eff70e23594c.png" width="261" title="" crop="0,0,1,1" id="ueff091e5" class="ne-image">

启动服务器进行测试：

<img src="https://cdn.nlark.com/yuque/0/2024/png/21376908/1730444208880-ca582b52-a68f-4918-9ead-f342c5ebbf38.png" width="275" title="" crop="0,0,1,1" id="u1eeb495d" class="ne-image">

<img src="https://cdn.nlark.com/yuque/0/2024/png/21376908/1730444226844-d1e40613-8c6c-43a5-95a1-1c0d34d101bb.png" width="239" title="" crop="0,0,1,1" id="ueb89442c" class="ne-image">

通过测试，我们的配置是生效的。

我们再来看看，默认的配置是否还生效？

<img src="https://cdn.nlark.com/yuque/0/2024/png/21376908/1730444289901-3304e315-67e2-4d6c-93b8-0db5f48a24a7.png" width="313" title="" crop="0,0,1,1" id="ua9846b46" class="ne-image">

我们可以看到，Spring Boot对Spring MVC的默认自动配置是生效的。

**因此，以上的方式只是在Spring MVC默认行为之外扩展行为。**

### 第二种方式

采用`@Bean`注解提供一个`WebMvcConfigurer`组件，代码如下：

```java

package com.jkweilai.springboot.config;

import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.web.servlet.config.annotation.ResourceHandlerRegistry;
import org.springframework.web.servlet.config.annotation.WebMvcConfigurer;

@Configuration
public class WebConfig2 {

    @Bean
    public WebMvcConfigurer addResourceHandlers(){
        return new WebMvcConfigurer() {
            @Override
            public void addResourceHandlers(ResourceHandlerRegistry registry) {
                registry.addResourceHandler("/static/**")
                        .addResourceLocations("classpath:/static1/", "classpath:/static2/");
            }
        };
    }
}

```

测试结果如下：

<img src="https://cdn.nlark.com/yuque/0/2024/png/21376908/1730444971338-0aca22a6-ff00-4644-9e21-2d08765b62e4.png" width="352" title="" crop="0,0,1,1" id="ub73538be" class="ne-image">

<img src="https://cdn.nlark.com/yuque/0/2024/png/21376908/1730444986018-554aeccd-a0fd-43d2-9b92-7846fea2415c.png" width="318" title="" crop="0,0,1,1" id="u86c7b340" class="ne-image">

<img src="https://cdn.nlark.com/yuque/0/2024/png/21376908/1730445003557-89783ce1-fdf7-4b22-873b-0fafdc07ecd2.png" width="325" title="" crop="0,0,1,1" id="u8827d14f" class="ne-image">

通过了测试，并且以上代码也是在原有配置基础上进行扩展。

### 其他配置实现方式相同

以上对`静态资源处理`进行了手动配置，也可以做其他配置，例如拦截器：

```java

package com.jkweilai.springboot.config;

import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.web.servlet.HandlerInterceptor;
import org.springframework.web.servlet.ModelAndView;
import org.springframework.web.servlet.config.annotation.InterceptorRegistry;
import org.springframework.web.servlet.config.annotation.ResourceHandlerRegistry;
import org.springframework.web.servlet.config.annotation.WebMvcConfigurer;

@Configuration
public class WebConfig2 {

    @Bean
    public WebMvcConfigurer addResourceHandlers(){
        return new WebMvcConfigurer() {
            @Override
            public void addResourceHandlers(ResourceHandlerRegistry registry) {
                registry.addResourceHandler("/static/**")
                        .addResourceLocations("classpath:/static1/", "classpath:/static2/");
            }
        };
    }

    // 拦截器配置。
    @Bean
    public WebMvcConfigurer addInterceptor(){
        return new WebMvcConfigurer() {
            @Override
            public void addInterceptors(InterceptorRegistry registry) {
                registry.addInterceptor(new HandlerInterceptor() {
                    @Override
                    public boolean preHandle(HttpServletRequest request, HttpServletResponse response, Object handler) throws Exception {
                        System.out.println("Interceptor's preHandle......");
                        return true;
                    }

                    @Override
                    public void postHandle(HttpServletRequest request, HttpServletResponse response, Object handler, ModelAndView modelAndView) throws Exception {
                        System.out.println("Interceptor's postHandle......");
                    }

                    @Override
                    public void afterCompletion(HttpServletRequest request, HttpServletResponse response, Object handler, Exception ex) throws Exception {
                        System.out.println("Interceptor's afterCompletion......");
                    }
                });
            }
        };
    }
}

```

启动服务器，打开浏览器，发送请求[http://localhost:8080/static/dog5.jpg](http://localhost:8080/static/dog5.jpg)，后台执行结果如下：

<img src="https://cdn.nlark.com/yuque/0/2024/png/21376908/1730445490551-7c8fbe3f-a792-4307-8c46-21a365e0b25d.png" width="409" title="" crop="0,0,1,1" id="u9c5870cc" class="ne-image">

这说明拦截器生效。

