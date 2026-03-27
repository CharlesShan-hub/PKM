# 异常处理器

---

## 什么是异常处理器

Spring MVC在`处理器方法`执行过程中出现了异常，可以采用`异常处理器`进行应对。

**一句话概括异常处理器作用：处理器方法（Controller）执行过程中出现了异常，跳转到对应的视图，在视图上展示友好信息。**

SpringMVC为异常处理提供了一个接口：HandlerExceptionResolver

<img src="https://cdn.nlark.com/yuque/0/2024/png/21376908/1711683439894-1af197f8-20d1-401b-8704-11d51b131670.png" width="1165" title="" crop="0,0,1,1" id="uf9c002eb" class="ne-image" style="font-size: 16px">

核心方法是：resolveException。

该方法用来编写具体的异常处理方案。返回值ModelAndView，表示异常处理完之后跳转到哪个视图。

HandlerExceptionResolver 接口有两个常用的默认实现：

+ DefaultHandlerExceptionResolver
+ SimpleMappingExceptionResolver

---

## 默认的异常处理器

DefaultHandlerExceptionResolver 是默认的异常处理器。

核心方法：

<img src="https://cdn.nlark.com/yuque/0/2024/png/21376908/1711683759071-a2b84ecf-92c8-46e2-a040-8b5c113446f2.png" width="1115" title="" crop="0,0,1,1" id="u1bc95b7f" class="ne-image" style="font-size: 16px">

当请求方式和处理方式不同时，DefaultHandlerExceptionResolver的默认处理态度是：

<img src="https://cdn.nlark.com/yuque/0/2024/png/21376908/1711683899955-8f7b2a54-716a-4b36-8550-e4630f695bca.png" width="557" title="" crop="0,0,1,1" id="uf6787e7a" class="ne-image" style="font-size: 16px">

---

## 自定义的异常处理器

自定义异常处理器需要使用：SimpleMappingExceptionResolver

自定义异常处理机制有两种语法：

+ 通过XML配置文件
+ 通过注解

### 配置文件方式

```xml

<bean class="org.springframework.web.servlet.handler.SimpleMappingExceptionResolver">
    <property name="exceptionMappings">
        <props>
            <!--用来指定出现异常后，跳转的视图-->
            <prop key="java.lang.Exception">tip</prop>
        </props>
    </property>
    <!--将异常信息存储到request域，value属性用来指定存储时的key。-->
    <property name="exceptionAttribute" value="e"/>
</bean>

```

在视图页面上展示异常信息：

```html

<!DOCTYPE html>
<html lang="en" xmlns:th="http://www.thymeleaf.org">
<head>
    <meta charset="UTF-8">
    <title>出错了</title>
</head>
<body>
<h1>出错了，请联系管理员！</h1>
<div th:text="${e}"></div>
</body>
</html>

```

<img src="https://cdn.nlark.com/yuque/0/2024/png/21376908/1711684183329-eb0e9b03-4d1d-442e-9d6b-22384e3bd776.png" width="977" title="" crop="0,0,1,1" id="u1cc798bf" class="ne-image" style="font-size: 16px">

### 注解方式

```java

@ControllerAdvice
public class ExceptionController {

    @ExceptionHandler
    public String tip(Exception e, Model model){
        model.addAttribute("e", e);
        return "tip";
    }
    
}

```

### 实际开发中的全局异常处理器

全局异常处理器的作用：****统一处理应用中的异常，将异常信息转换为用户友好的响应，避免异常直接暴露给用户。****

****全局体现在：它能处理整个Spring MVC应用中所有控制器（Controller）抛出的异常，无需在每个控制器中单独编写异常处理代码。****

********

**第一步：自定义业务异常：**

```java

/**
 * 自定义业务异常类
 */
public class BusinessException extends RuntimeException {
    
    private String code;    // 错误码
    private String message; // 错误信息
    
    // 构造方法
    public BusinessException(String code, String message) {
        super(message);
        this.code = code;
        this.message = message;
    }
    
    public BusinessException(String code, String message, Throwable cause) {
        super(message, cause);
        this.code = code;
        this.message = message;
    }
    
    // Getter 方法
    public String getCode() {
        return code;
    }
    
    public String getMessage() {
        return message;
    }
}

```

**第二步：编写全局异常处理器**

```java

import jakarta.servlet.http.HttpServletRequest;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.ControllerAdvice;
import org.springframework.web.bind.annotation.ExceptionHandler;
import org.springframework.web.servlet.NoHandlerFoundException;

@ControllerAdvice
public class GlobalExceptionHandler{

    // 处理业务异常 - 页面跳转
    @ExceptionHandler(BusinessException.class)
    public String handleBusinessException(BusinessException e, Model model) {
        // 使用标准输出记录日志（生产环境建议使用日志框架）
        System.err.println("业务异常: code=" + e.getCode() + ", message=" + e.getMessage());
        e.printStackTrace();

        model.addAttribute("errorCode", e.getCode());
        model.addAttribute("errorMsg", e.getMessage());
        model.addAttribute("timestamp", java.time.LocalDateTime.now());

        return "error/business";
    }

    // 处理空指针异常
    @ExceptionHandler(NullPointerException.class)
    public String handleNullPointer(NullPointerException e, Model model) {
        System.err.println("空指针异常:");
        e.printStackTrace();

        model.addAttribute("error", "系统内部错误，请联系管理员");
        return "error/500";
    }

    // 处理所有其他异常（兜底）
    @ExceptionHandler(Exception.class)
    public String handleAllExceptions(Exception e, Model model, HttpServletRequest request) {
        System.err.println("未捕获异常: URI=" + request.getRequestURI());
        e.printStackTrace();

        model.addAttribute("error", "系统繁忙，请稍后重试");
        model.addAttribute("timestamp", java.time.LocalDateTime.now());
        model.addAttribute("path", request.getRequestURI());

        return "error/500";
    }

    // 处理404异常（需要配置）
    @ExceptionHandler(NoHandlerFoundException.class)
    public String handleNotFound(NoHandlerFoundException e, Model model) {
        System.err.println("404 - 页面未找到: " + e.getRequestURL());

        model.addAttribute("error", "请求的页面不存在");
        model.addAttribute("path", e.getRequestURL());
        return "error/404";
    }
}

```
