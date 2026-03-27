# Servlet中的三个域对象

---

## 回顾域对象

请求域：request

会话域：session

应用域：application

三个域都有以下三个方法：

```java

// 向域中存储数据
void setAttribute(String name, Object obj);

// 从域中读取数据
Object getAttribute(String name);

// 删除域中的数据
void removeAttribute(String name);

```

主要是通过：setAttribute + getAttribute方法来完成在域中数据的传递和共享。

**request**

接口名：HttpServletRequest

简称：request

request对象代表了一次请求。一次请求一个request。

使用请求域的业务场景：在A资源中通过转发的方式跳转到B资源，因为是转发，因此从A到B是一次请求，如果想让A资源和B资源共享同一个数据，可以将数据存储到request域中。

**session**

接口名：HttpSession

简称：session

session对象代表了一次会话。从打开浏览器开始访问，到最终浏览器关闭，这是一次完整的会话。每个会话session对象都对应一个JSESSIONID，而JSESSIONID生成后以cookie的方式存储在浏览器客户端。浏览器关闭，JSESSIONID失效，会话结束。

使用会话域的业务场景：

1. 在A资源中通过重定向的方式跳转到B资源，因为是重定向，因此从A到B是两次请求，如果想让A资源和B资源共享同一个数据，可以将数据存储到session域中。
2. 登录成功后保存用户的登录状态。

**application**

接口名：ServletContext

简称：application

application对象代表了整个web应用，服务器启动时创建，服务器关闭时销毁。对于一个web应用来说，application对象只有一个。

使用应用域的业务场景：记录网站的在线人数。

---

## request域对象

在SpringMVC中，在request域中共享数据有以下几种方式：

1. 使用原生Servlet API方式。
2. 使用Model接口。
3. 使用Map接口。
4. 使用ModelMap类。
5. 使用ModelAndView类。

### 使用原生Servlet API方式

在Controller的方法上使用HttpServletRequest：

```java

@Controller
public class RequestScopeTestController {

    @RequestMapping("/testServletAPI")
    public String testServletAPI(HttpServletRequest request){
        // 向request域中存储数据
        request.setAttribute("testRequestScope", "在SpringMVC中使用原生Servlet API实现request域数据共享");
        return "view";
    }
}

```

页面：

```html

<!DOCTYPE html>
<html lang="en" xmlns:th="http://www.thymeleaf.org">
<head>
    <meta charset="UTF-8">
    <title>view</title>
</head>
<body>
<div th:text="${testRequestScope}"></div>
</body>
</html>

```

超链接：

```html

<!DOCTYPE html>
<html lang="en" xmlns:th="http://www.thymeleaf.org">
<head>
    <meta charset="UTF-8">
    <title>index</title>
</head>
<body>
<h1>Index Page</h1>
<a th:href="@{/testServletAPI}">在SpringMVC中使用原生Servlet API实现request域数据共享</a><br>
</body>
</html>

```

测试结果：

<img src="https://cdn.nlark.com/yuque/0/2024/png/21376908/1710747192867-9c718af0-41ad-4be9-8d48-c2ecdbd90789.png" width="489" title="" crop="0,0,1,1" id="u50ed1ef3" class="ne-image" style="font-size: 16px">

这种方式当然可以，用SpringMVC框架，不建议使用原生Servlet API。

### 使用Model接口

```java

@RequestMapping("/testModel")
public String testModel(Model model){
    // 向request域中存储数据
    model.addAttribute("testRequestScope", "在SpringMVC中使用Model接口实现request域数据共享");
    return "view";
}

```

### 使用Map接口

```java

@RequestMapping("/testMap")
public String testMap(Map<String, Object> map){
    // 向request域中存储数据
    map.put("testRequestScope", "在SpringMVC中使用Map接口实现request域数据共享");
    return "view";
}

```

### 使用ModelMap类

```java

@RequestMapping("/testModelMap")
public String testModelMap(ModelMap modelMap){
    // 向request域中存储数据
    modelMap.addAttribute("testRequestScope", "在SpringMVC中使用ModelMap实现request域数据共享");
    return "view";
}

```

### Model、Map、ModelMap的关系

可以在以上Model、Map、ModelMap的测试程序中将其输出，看看输出什么：

<img src="https://cdn.nlark.com/yuque/0/2024/png/21376908/1710748328132-7ec71a48-8879-4758-824a-a9d669f1594a.png" width="845" title="" crop="0,0,1,1" id="u85bdc93d" class="ne-image" style="font-size: 16px">

看不出来什么区别，从输出结果上可以看到都是一样的。

可以将其运行时类名输出：

<img src="https://cdn.nlark.com/yuque/0/2024/png/21376908/1710748490407-0ab2044c-0261-498d-b55d-ce563afda27d.png" width="788" title="" crop="0,0,1,1" id="u0cb00398" class="ne-image" style="font-size: 16px">

通过输出结果可以看出，无论是Model、Map还是ModelMap，底层实例化的对象都是：BindingAwareModelMap。

可以查看BindingAwareModelMap的继承结构：

<img src="https://cdn.nlark.com/yuque/0/2024/png/21376908/1710748694354-caf9941e-9ce9-4215-bfe7-2d2a759ef206.png" width="511" title="" crop="0,0,1,1" id="u6b7fdd17" class="ne-image" style="font-size: 16px">

通过继承结构可以看出：BindingAwareModelMap继承了ModelMap，而ModelMap又实现了Map接口。

另外，请看以下源码：

<img src="https://cdn.nlark.com/yuque/0/2024/png/21376908/1710748884799-5bad9d0f-9926-4ef0-a29e-7f9e5d6bd383.png" width="757" title="" crop="0,0,1,1" id="ubf08d967" class="ne-image" style="font-size: 16px">

可以看出ModelMap又实现了Model接口。因此表面上是采用了不同方式，底层本质上是相同的。

SpringMVC之所以提供了这些方式，目的就是方便程序员的使用，提供了多样化的方式，可见它的重要性。

### 使用ModelAndView类

在SpringMVC框架中为了更好的体现MVC架构模式，提供了一个类：ModelAndView。这个类的实例封装了Model和View。也就是说这个类既封装业务处理之后的数据，也体现了跳转到哪个视图。使用它也可以完成request域数据共享。

```java

@RequestMapping("/testModelAndView")
public ModelAndView testModelAndView(){
    // 创建“模型与视图对象”
    ModelAndView modelAndView = new ModelAndView();
    // 绑定数据
    modelAndView.addObject("testRequestScope", "在SpringMVC中使用ModelAndView实现request域数据共享");
    // 绑定视图
    modelAndView.setViewName("view");
    // 返回
    return modelAndView;
}

```

这种方式需要注意的是：

1. 方法的返回值类型不是String，而是ModelAndView对象。
2. ModelAndView不是出现在方法的参数位置，而是在方法体中new的。
3. 需要调用addObject向域中存储数据。
4. 需要调用setViewName设置视图的名字。

### ModelAndView源码分析

以上我们通过了五种方式完成了request域数据共享，包括：原生Servlet API，Model、Map、ModelMap、ModelAndView

其中后四种：Model、Map、ModelMap、ModelAndView。这四种方式在底层DispatcherServlet调用我们的Controller之后，返回的对象都是ModelAndView，这个可以通过源码进行分析。

在以上四种方式中，拿Model举例，添加断点进行调试：

<img src="https://cdn.nlark.com/yuque/0/2024/png/21376908/1710750710855-53e8ffdd-b563-453e-afb4-70648684e619.png" width="749" title="" crop="0,0,1,1" id="u579b6322" class="ne-image" style="font-size: 16px">

启动服务器，发送请求，走到断点：

<img src="https://cdn.nlark.com/yuque/0/2024/png/21376908/1710750795816-555dfc56-ccf2-43b4-b516-a737336d1e4f.png" width="591" title="" crop="0,0,1,1" id="u38449060" class="ne-image" style="font-size: 16px">

查看VM Stack信息：

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1764502506969-7d415950-4424-4c95-989c-02838aa265b8.png" width="604.8" title="" crop="0,0,1,1" id="u878d6b36" class="ne-image" style="font-size: 16px">

查看DispatcherServlet的1089行，源码如下：

<img src="https://cdn.nlark.com/yuque/0/2024/png/21376908/1710750933440-8254f738-2716-4f56-8610-4814e6fdecbf.png" width="1123" title="" crop="0,0,1,1" id="u56c3d766" class="ne-image" style="font-size: 16px">

可以看到这里，无论你使用哪种方式，最终都要返回一个ModelAndView对象。

提醒：大家可以通过以下断点调试方式，采用一级一级返回，最终可以看到都会返回ModelAndView对象。

<img src="https://cdn.nlark.com/yuque/0/2024/png/21376908/1710751055879-078ad592-a894-45fe-8d4d-1a74d9c8db79.png" width="357" title="" crop="0,0,1,1" id="u09e6abc5" class="ne-image" style="font-size: 16px">

---

## session域对象

在SpringMVC中使用session域共享数据，实现方式有多种，其中比较常见的两种方式：

1. 使用原生Servlet API
2. 使用SessionAttributes注解

### 使用原生Servlet API

```java

@Controller
public class SessionScopeTestController {

    @RequestMapping("/testSessionScope1")
    public String testServletAPI(HttpSession session) {
        // 向会话域中存储数据
        session.setAttribute("testSessionScope1", "使用原生Servlet API实现session域共享数据");
        return "view";
    }

}

```

视图页面：

```html

<div th:text="${session.testSessionScope1}"></div>

```

超链接：

```html

<a th:href="@{/testSessionScope1}">在SpringMVC中使用原生Servlet API实现session域共享数据</a><br>

```

### 使用SessionAttributes注解

使用SessionAttributes注解标注Controller：

```java

@Controller
@SessionAttributes(value = {"x", "y"})
public class SessionScopeTestController {

    @RequestMapping("/testSessionScope2")
    public String testSessionAttributes(ModelMap modelMap){
        // 向session域中存储数据
        modelMap.addAttribute("x", "我是埃克斯");
        modelMap.addAttribute("y", "我是歪");

        return "view";
    }
}

```

注意：SessionAttributes注解使用在Controller类上。标注了当key是 x 或者 y 时，数据将被存储到会话session中。如果没有 SessionAttributes注解，默认存储到request域中。

---

## application域对象

在SpringMVC实现application域数据共享，最常见的方案就是直接使用Servlet API了：

```java

@Controller
public class ApplicationScopeTestController {

    @RequestMapping("/testApplicationScope")
    public String testApplicationScope(HttpServletRequest request){
        
        // 获取ServletContext对象
        ServletContext application = request.getServletContext();

        // 向应用域中存储数据
        application.setAttribute("applicationScope", "我是应用域当中的一条数据");

        return "view";
    }
}

```

视图页面：

```html

<div th:text="${application.applicationScope}"></div>

```

超链接：

```html

<a th:href="@{/testApplicationScope}">在SpringMVC中使用ServletAPI实现application域共享数据</a><br>

```
