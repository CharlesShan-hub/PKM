# RESTful编程风格

---

## RESTful是什么

RESTful是`WEB服务接口`的一种设计风格。

RESTful定义了一组约束条件和规范，可以让`WEB服务接口`更加简洁、易于理解、易于扩展、安全可靠。

RESTful对一个`WEB服务接口`都规定了哪些东西？

+ 对请求的URL格式有约束和规范
+ 对HTTP的请求方式有约束和规范
+ 对请求和响应的数据格式有约束和规范
+ 对HTTP状态码有约束和规范
+ 等 ......

REST对请求方式的约束是这样的：

+ 查询必须发送GET请求
+ 新增必须发送POST请求
+ 修改必须发送PUT请求
+ 删除必须发送DELETE请求

REST对URL的约束是这样的：

+ 传统的URL：get请求，/springmvc/getUserById?id=1
+ REST风格的URL：**get请求**，/springmvc/user/1

+ 传统的URL：get请求，/springmvc/deleteUserById?id=1
+ REST风格的URL：**delete请求**, /springmvc/user/1

RESTful对URL的约束和规范的核心是：****通过采用****`****不同的请求方式****`****+****`****URL****`****来确定WEB服务中的资源。****

---

## RESTful风格与传统方式对比

传统的 URL 与 RESTful URL 的区别是传统的 URL 是基于方法名进行资源访问和操作，而 RESTful URL 是基于资源的结构和状态进行操作的。下面是一张表格，展示两者之间的具体区别：

| **传统的 URL** | **RESTful URL** |
| --- | --- |
| GET /getUserById?id=1 | GET /user/1 |
| GET /getAllUser | GET /user |
| POST /addUser | POST /user |
| POST /modifyUser | PUT /user |
| GET /deleteUserById?id=1 | DELETE /user/1 |

从上表中我们可以看出，传统的URL是基于动作的，而 RESTful URL 是基于资源和状态的，因此 RESTful URL 更加清晰和易于理解，这也是 REST 架构风格被广泛使用的主要原因之一。

---

## RESTful方式演示查询

RESTful规范中规定，如果要查询数据，需要发送GET请求。

### 根据id查询(GET /api/user/1)

```xml

<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
       xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
       xmlns:context="http://www.springframework.org/schema/context"
       xmlns:mvc="http://www.springframework.org/schema/mvc"
       xsi:schemaLocation="http://www.springframework.org/schema/beans http://www.springframework.org/schema/beans/spring-beans.xsd http://www.springframework.org/schema/context https://www.springframework.org/schema/context/spring-context.xsd http://www.springframework.org/schema/mvc https://www.springframework.org/schema/mvc/spring-mvc.xsd">

    <!--组件扫描-->
    <context:component-scan base-package="com.jkweilai.springmvc.controller"/>

    <!--视图解析器-->
    <bean id="thymeleafViewResolver" class="org.thymeleaf.spring6.view.ThymeleafViewResolver">
        <property name="characterEncoding" value="UTF-8"/>
        <property name="order" value="1"/>
        <property name="templateEngine">
            <bean class="org.thymeleaf.spring6.SpringTemplateEngine">
                <property name="templateResolver">
                    <bean class="org.thymeleaf.spring6.templateresolver.SpringResourceTemplateResolver">
                        <property name="prefix" value="/WEB-INF/thymeleaf/"/>
                        <property name="suffix" value=".html"/>
                        <property name="templateMode" value="HTML"/>
                        <property name="characterEncoding" value="UTF-8"/>
                    </bean>
                </property>
            </bean>
        </property>
    </bean>

    <!--启用注解-->
    <mvc:annotation-driven/>

    <!--视图控制器映射-->
    <mvc:view-controller path="/" view-name="index"/>
</beans>

```

首页index.html

```html

<!DOCTYPE html>
<html lang="en" xmlns:th="http://www.thymeleaf.org">
<head>
    <meta charset="UTF-8">
    <title>index</title>
</head>
<body>
<h1>index page</h1>
<hr>
<!--根据id查询：GET /api/user/1 -->
<a th:href="@{/api/user/1}">根据id查询用户信息</a><br>

</body>
</html>

```

控制器Controller：

```java

package com.jkweilai.springmvc.controller;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;

@Controller
public class UserController {

    @RequestMapping(value = "/api/user/{id}", method = RequestMethod.GET)
    public String getById(@PathVariable("id") Integer id){
        System.out.println("根据用户id查询用户信息，用户id是" + id);
        return "ok";
    }

}

```

视图页面：

```html

<!DOCTYPE html>
<html lang="en" xmlns:th="http://www.thymeleaf.org">
<head>
    <meta charset="UTF-8">
    <title>ok</title>
</head>
<body>
<h1>ok</h1>
</body>
</html>

```

启动服务器，测试：http://localhost:8080/springmvc

### 查询所有(GET /api/user)

```html

<!--查询所有-->
<a th:href="@{/api/user}">查询所有</a><br>

```

```java

@RequestMapping(value = "/api/user", method = RequestMethod.GET)
public String getAll(){
    System.out.println("查询所有用户信息");
    return "ok";
}

```

---

## RESTful方式演示增加(POST /api/user)

RESTful规范中规定，如果要进行保存操作，需要发送POST请求。

```html

<!--保存用户-->
<form th:action="@{/api/user}" method="post">
    <input type="submit" th:value="保存">
</form>

```

```java

@RequestMapping(value = "/api/user", method = RequestMethod.POST)
public String save(){
    System.out.println("保存用户信息");
    return "ok";
}

```

---

## RESTful方式演示修改

RESTful规范中规定，如果要进行保存操作，需要发送PUT请求。

****如何发送PUT请求？****

****第一步：首先你必须是一个POST请求。****

****第二步：在发送POST请求的时候，提交这样的数据：****`****_method=PUT****`

****第三步：在web.xml文件配置SpringMVC提供的过滤器：HiddenHttpMethodFilter****

实践一下：

```html

<!--修改用户-->
<hr>
<form th:action="@{/api/user}" method="post">
    <!--隐藏域的方式提交 _method=put -->
    <input type="hidden" name="_method" value="put">
    用户名：<input type="text" name="username"><br>
    <input type="submit" th:value="修改">
</form>

```

```xml

<!--隐藏的HTTP请求方式过滤器-->
<filter>
    <filter-name>hiddenHttpMethodFilter</filter-name>
    <filter-class>org.springframework.web.filter.HiddenHttpMethodFilter</filter-class>
</filter>
<filter-mapping>
    <filter-name>hiddenHttpMethodFilter</filter-name>
    <url-pattern>/*</url-pattern>
</filter-mapping>

```

```java

@RequestMapping(value = "/api/user", method = RequestMethod.PUT)
public String update(@RequestParam("username") String username){
    System.out.println("修改用户信息，用户名：" + username);
    return "ok";
}

```

---

## **HiddenHttpMethodFilter**

HiddenHttpMethodFilter是Spring MVC框架提供的，专门用于RESTful编程风格。

实现原理可以通过源码查看：

<img src="https://cdn.nlark.com/yuque/0/2024/png/21376908/1710981996209-5c66441b-0aa9-41a7-b71d-26b2ffb0f4f5.png" width="1291" title="" crop="0,0,1,1" id="u35d657b9" class="ne-image" style="font-size: 16px">

<img src="https://cdn.nlark.com/yuque/0/2024/png/21376908/1710982160559-ffe20024-a10a-4aa2-b39e-44bebd0d3945.png" width="699" title="" crop="0,0,1,1" id="u4b2501ea" class="ne-image" style="font-size: 16px">

<img src="https://cdn.nlark.com/yuque/0/2024/png/21376908/1710982194265-720a0b49-aa95-475f-900b-7234280f5c9c.png" width="925" title="" crop="0,0,1,1" id="u4e856ede" class="ne-image" style="font-size: 16px">

通过源码可以看到，if语句中，首先判断是否为POST请求，如果是POST请求，调用`request.getParameter(this.methodParam)`。可以看到`this.methodParam`是`_method`，这样就要求我们在提交请求方式的时候必须采用这个格式：`_method=put`。获取到请求方式之后，调用了toUpperCase转换成大写了。因此前端页面中小写的put或者大写的PUT都是可以的。if语句中嵌套的if语句说的是，只有请求方式是 PUT,DELETE,PATCH的时候会创建HttpMethodRequestWrapper对象。而HttpMethodRequestWrapper对象的构造方法是这样的：

<img src="https://cdn.nlark.com/yuque/0/2024/png/21376908/1710984179119-96331e0b-ae39-45b0-bba1-b8db3ec7107f.png" width="905" title="" crop="0,0,1,1" id="udaf4f43c" class="ne-image" style="font-size: 16px">

这样method就从POST变成了：PUT/DELETE/PATCH。

****重点注意事项：CharacterEncodingFilter和********HiddenHttpMethodFilter的顺序****

细心的同学应该注意到了，在**HiddenHttpMethodFilter源码中有这样一行代码：**

<img src="https://cdn.nlark.com/yuque/0/2024/png/21376908/1710984264334-7df83331-ddbb-4ead-a58c-cb4dc6c19ef6.png" width="614" title="" crop="0,0,1,1" id="ue805f02f" class="ne-image" style="font-size: 16px">

大家是否还记得，字符编码过滤器执行之前不能调用 request.getParameter方法，如果提前调用了，乱码问题就无法解决了。因为request.setCharacterEncoding()方法的执行必须在所有request.getParameter()方法之前执行。因此这两个过滤器就有先后顺序的要求，在web.xml文件中，应该先配置CharacterEncodingFilter，然后再配置HiddenHttpMethodFilter。
