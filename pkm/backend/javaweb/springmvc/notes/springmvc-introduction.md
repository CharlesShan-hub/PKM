# 初识 SpringMVC 

---

## 回顾MVC 架构模式

MVC是一种软件架构模式（是一种软件架构设计思想，不止Java开发中用到，其它语言也需要用到），它将应用分为三块：

+ M：Model（模型）
+ V：View（视图）
+ C：Controller（控制器）

MVC将应用分为三块，每一块各司其职，都有自己专注的事情要做，他们属于分工协作，互相配合：

+ Model：负责业务处理及数据的收集。
+ View：负责数据的展示
+ Controller：负责调度。它是一个调度中心，它来决定什么时候调用Model来处理业务，什么时候调用View视图来展示数据。

MVC架构模式如下所示：

<img src="https://cdn.nlark.com/yuque/0/2024/png/21376908/1710142469881-5dee11e1-80e8-4cbc-8f0c-726d4e42bbfa.png" width="1378" title="" crop="0,0,1,1" id="u4dd05c22" class="ne-image" style="font-size: 16px">

MVC架构模式的描述：前端浏览器发送请求给web服务器，web服务器中的Controller接收到用户的请求，Controller负责将前端提交的数据进行封装，然后Controller调用Model来处理业务，当Model处理完业务后会返回处理之后的数据给Controller，Controller再调用View来完成数据的展示，最终将结果响应给浏览器，浏览器进行渲染展示页面。

**面试题：什么是三层模型，并说一说MVC架构模式与三层模型的区别？**

+ **三层架构是系统整体的纵向分层，解决的是表现、业务、数据访问之间的职责分离；**
+ **而MVC是表现层内部的横向解耦，解决的是用户交互中数据、视图、控制逻辑的关系。**
+ **它们不是二选一，通常会在项目中协同工作——在三层架构的‘表现层’里使用MVC模式。**
+ **比如Spring MVC项目，就是用MVC模式实现了三层架构里的表现层。**

****

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1764331586696-acdd037f-01b1-45ab-a711-15115ed4f728.png" width="220" title="" crop="0,0,1,1" id="ueb153103" class="ne-image" style="font-size: 16px">

---

## SpringMVC概述

SpringMVC是一个实现了MVC架构模式的Web框架，底层基于Servlet实现。全称：`Spring Web MVC`，是 `Spring`框架的七大模块之一。

SpringMVC已经将MVC架构模式实现了，因此只要我们是基于SpringMVC框架写代码，编写的程序就是符合MVC架构模式的。（****MVC的架子搭好了，我们只需要添添补补****）

使用SpringMVC框架的时候同样也可以使用IoC和AOP。

---

## SpringMVC帮我们做了什么

SpringMVC框架帮我们做了什么，与纯粹的Servlet开发有什么区别？

1.  入口控制：SpringMVC框架通过DispatcherServlet作为入口控制器，负责接收请求和分发请求。而在Servlet开发中，需要自己编写Servlet程序，并在web.xml中进行配置，才能接受和处理请求。 
2. 在SpringMVC中，表单提交时可以自动将表单数据绑定到相应的Java对象中，只需要在控制器方法的参数列表中声明该Java对象即可，无需手动获取和赋值表单数据。而在纯粹的Servlet开发中，这些都是需要自己手动完成的。
3.  IoC容器：SpringMVC框架通过IoC容器管理对象，只需要在配置文件中进行相应的配置即可获取实例对象，而在Servlet开发中需要手动创建对象实例。 
4.  统一处理请求：SpringMVC框架提供了拦截器、异常处理器等统一处理请求的机制，并且可以灵活地配置这些处理器。而在Servlet开发中，需要自行编写过滤器、异常处理器等，增加了代码的复杂度和开发难度。 
5.  视图解析：SpringMVC框架提供了多种视图模板，如JSP、Freemarker、Velocity、Thymeleaf 等，并且支持国际化、主题等特性。而在Servlet开发中需要手动处理视图层，增加了代码的复杂度。 

总之，与Servlet开发相比，SpringMVC框架可以帮我们节省很多时间和精力，减少代码的复杂度，更加专注于业务开发。同时，也提供了更多的功能和扩展性，可以更好地满足企业级应用的开发需求。

---

## SpringMVC框架的特点

1.  轻量级：相对于其他Web框架，Spring MVC框架比较小巧轻便。（只有几个几百KB左右的Jar包文件） 
2.  模块化：请求处理过程被分成多个模块，以模块化的方式进行处理。 
    1. 控制器模块：Controller
    2. 业务逻辑模块：Model
    3. 视图模块：View
3.  依赖注入：Spring MVC框架利用Spring框架的依赖注入功能实现对象的管理，实现松散耦合。 
4.  易于扩展：提供了很多口子，允许开发者根据需要插入自己的代码，以扩展实现应用程序的特殊需求。 
    1. Spring MVC框架允许开发人员通过自定义模块和组件来扩展和增强框架的功能。
    2. Spring MVC框架与其他Spring框架及第三方框架集成得非常紧密，这使得开发人员可以非常方便地集成其他框架，以获得更好的功能。
5.  易于测试：支持单元测试框架，提高代码质量和可维护性。 （对SpringMVC中的Controller测试时，不需要依靠Web服务器。）
6.  自动化配置：提供自动化配置，减少配置细节。 
    1. Spring MVC框架基于约定大于配置的原则，对常用的配置约定进行自动化配置。
7.  灵活性：Spring MVC框架支持多种视图技术，如JSP、FreeMarker、Thymeleaf等，针对不同的视图配置不同的视图解析器即可。 

---

## 第一个SpringMVC程序

### 创建Maven模块

第一步：创建Empty Project，起名：springmvc。

第二步：设置springmvc工程的JDK版本：Java21。

第三步：设置maven、设置字符编码方式 UTF-8。

第四步：创建Maven模块 `springmvc-001`

第五步：将pom.xml文件中的打包方式修改为war

```xml

<!-- 打包方式设置为war方式 -->
<packaging>war</packaging>

```

第六步：添加以下依赖

```xml

<dependencies>
    <!--Spring MVC依赖-->
    <dependency>
        <groupId>org.springframework</groupId>
        <artifactId>spring-webmvc</artifactId>
        <version>6.2.13</version>
    </dependency>
    <!--logback日志框架依赖-->
    <dependency>
        <groupId>ch.qos.logback</groupId>
        <artifactId>logback-classic</artifactId>
        <version>1.5.21</version>
        <scope>compile</scope>
    </dependency>
    <!--servlet规范依赖-->
    <dependency>
        <groupId>jakarta.servlet</groupId>
        <artifactId>jakarta.servlet-api</artifactId>
        <version>6.1.0</version>
        <scope>provided</scope>
    </dependency>
    <!--thymeleaf与spring6整合依赖-->
    <dependency>
        <groupId>org.thymeleaf</groupId>
        <artifactId>thymeleaf-spring6</artifactId>
        <version>3.1.2.RELEASE</version>
    </dependency>
</dependencies>

```

### 添加web支持

**第一步：**在main目录下创建一个webapp目录

**第二步：**添加web.xml配置文件

+ 注意 web.xml 文件的位置：E:\Spring MVC\code\springmvc\springmvc-001\****src\main\webapp\WEB-INF\web.xml****
+ 注意版本选择：6.0

添加web支持后的目录结构：

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1764332865455-5135bf3b-bfd1-4265-a8d1-d8e326c88b28.png" width="285" title="" crop="0,0,1,1" id="uc568c006" class="ne-image" style="font-size: 16px">

### 配置web.xml文件

Spring MVC是一个web框架，在javaweb中谁来负责接收请求，处理请求，以及响应呢？当然是Servlet。

在SpringMVC框架中已经为我们写好了一个Servlet，它的名字叫做：DispatcherServlet，我们称其为前端控制器。既然是Servlet，那么它就需要在web.xml文件中进行配置：

```xml

<?xml version="1.0" encoding="UTF-8"?>
<web-app xmlns="https://jakarta.ee/xml/ns/jakartaee"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="https://jakarta.ee/xml/ns/jakartaee https://jakarta.ee/xml/ns/jakartaee/web-app_6_0.xsd"
         version="6.0">

    <!--前端控制器-->
    <servlet>
        <servlet-name>springmvc</servlet-name>
        <servlet-class>org.springframework.web.servlet.DispatcherServlet</servlet-class>
    </servlet>

    <servlet-mapping>
        <servlet-name>springmvc</servlet-name>
        <!--
            1. / 是 Spring MVC 官方推荐写法。
            2. /* 会拦截所有路径，包括 xx.jsp，jsp应该交由Web容器内置的JspServlet自动处理，Spring MVC不应该拦截。因此不建议写 /*
            3. / 到底拦截的是什么？拦截的是所有其他Servlet不要的请求，不过在spring mvc开发中我们只编写一个 DispatcherServlet，不需要
            编写其他的Servlet，在这种情况下，我们可以等同的认为 / 拦截了除jsp之外的所有请求。
            4. / 会拦截所有的静态资源。看似是一个缺点。实则是优点。
            5. / 的优点有三个：
                第一：支持 RESTful URL
                第二：放行 JSP 给容器
                第三：促使使用更优的静态资源方案（web容器自带Servlet处理静态资源效率低。Spring框架处理静态资源效率高：例如spring提供了缓存控制等高级功能）
        -->
        <url-pattern>/</url-pattern>
    </servlet-mapping>

</web-app>

```

DispatcherServlet是SpringMVC框架为我们提供的最核心的类，它是整个SpringMVC框架的前端控制器，负责接收HTTP请求、将请求路由到处理程序、处理响应信息，最终将响应返回给客户端。DispatcherServlet是Web应用程序的主要入口点之一，它的职责包括：

1.  接收客户端的HTTP请求：DispatcherServlet监听来自Web浏览器的HTTP请求，然后根据请求的URL将请求数据解析为Request对象。 
2.  处理请求的URL：DispatcherServlet将请求的URL与处理程序进行匹配，确定要调用哪个控制器（Controller）来处理此请求。 
3.  调用相应的控制器：DispatcherServlet将请求发送给找到的控制器处理，控制器将执行业务逻辑，然后返回一个模型对象（Model）。 
4.  渲染视图：DispatcherServlet将调用视图引擎，将模型对象呈现为用户可以查看的HTML页面。 
5.  返回响应给客户端：DispatcherServlet将生成的响应发送回浏览器，响应可以包括JSON、XML、HTML以及其它类型的数据

### 编写控制器FirstController

DispatcherServlet接收到请求之后，会根据请求路径分发到对应的Controller，Controller来负责处理请求的核心业务。在SpringMVC框架中Controller是一个普通的Java类（一个普通的POJO类，不需要继承任何类或实现任何接口），需要注意的是：POJO类要纳入IoC容器来管理，POJO类的生命周期由Spring来管理，因此要使用注解标注：

```java

package com.jkweilai.springmvc.controller;

import org.springframework.stereotype.Controller;

@Controller
public class FirstController {
    
}

```

### 配置springmvc-servlet.xml文件

SpringMVC框架有它自己的配置文件，该配置文件的名字默认为：<servlet-name>-servlet.xml，****默认存放的位置是WEB-INF 目录下****：

```xml

<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
       xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
       xmlns:context="http://www.springframework.org/schema/context"
       xsi:schemaLocation="http://www.springframework.org/schema/beans http://www.springframework.org/schema/beans/spring-beans.xsd http://www.springframework.org/schema/context https://www.springframework.org/schema/context/spring-context.xsd">
    <!--组件扫描-->
    <context:component-scan base-package="com.jkweilai.springmvc.controller"/>
    <!--视图解析器-->
    <bean id="thymeleafViewResolver" class="org.thymeleaf.spring6.view.ThymeleafViewResolver">
        <!--作用于视图渲染的过程中，可以设置视图渲染后输出时采用的编码字符集-->
        <property name="characterEncoding" value="UTF-8"/>
        <!--如果配置多个视图解析器，它来决定优先使用哪个视图解析器，它的值越小优先级越高-->
        <property name="order" value="1"/>
        <!--当 ThymeleafViewResolver 渲染模板时，会使用该模板引擎来解析、编译和渲染模板-->
        <property name="templateEngine">
            <bean class="org.thymeleaf.spring6.SpringTemplateEngine">
                <!--用于指定 Thymeleaf 模板引擎使用的模板解析器。模板解析器负责根据模板位置、模板资源名称、文件编码等信息，加载模板并对其进行解析-->
                <property name="templateResolver">
                    <bean class="org.thymeleaf.spring6.templateresolver.SpringResourceTemplateResolver">
                        <!--设置模板文件的位置（前缀）-->
                        <property name="prefix" value="/WEB-INF/templates/"/>
                        <!--设置模板文件后缀（后缀），Thymeleaf文件扩展名不一定是html，也可以是其他，例如txt，大部分都是html-->
                        <property name="suffix" value=".html"/>
                        <!--设置模板类型，例如：HTML,TEXT,JAVASCRIPT,CSS等-->
                        <property name="templateMode" value="HTML"/>
                        <!--用于模板文件在读取和解析过程中采用的编码字符集-->
                        <property name="characterEncoding" value="UTF-8"/>
                    </bean>
                </property>
            </bean>
        </property>
    </bean>
</beans>

```

在WEB-INF目录下新建springmvc-servlet.xml文件，并且提供以上配置信息。

<img src="https://cdn.nlark.com/yuque/0/2024/png/21376908/1710309679329-4454ce41-d80a-42dc-abb7-683bd9397856.png" width="296" title="" crop="0,0,1,1" id="ueec9abf4" class="ne-image" style="font-size: 16px">

以上配置主要两项：

+ 第一项：组件扫描。spring扫描这个包中的类，将这个包中的类实例化并纳入IoC容器的管理。
+ 第二项：视图解析器。视图解析器（View Resolver）的作用主要是将Controller方法返回的逻辑视图名称解析成实际的视图对象。视图解析器将解析出的视图对象返回给DispatcherServlet，并最终由DispatcherServlet将该视图对象转化为响应结果，呈现给用户。

注意：如果采用了其它视图，请配置对应的视图解析器，例如：

+ JSP的视图解析器：InternalResourceViewResolver
+ FreeMarker视图解析器：FreeMarkerViewResolver
+ Velocity视图解析器：VelocityViewResolver

### 提供视图

在WEB-INF目录下新建templates目录，在templates目录中新建html文件，例如：first.html，并提供以下代码：

```html

<!DOCTYPE html>
<!--指定 th 命名空间，让 Thymeleaf 标准表达式可以被解析和执行-->
<html lang="en" xmlns:th="http://www.thymeleaf.org">
<head>
    <meta charset="UTF-8">
    <title>first springmvc</title>
</head>
<body>
<h1>我的第一个Spring MVC程序</h1>
</body>
</html>

```

对于每一个Thymeleaf文件来说 xmlns:th="[http://www.thymeleaf.org"](http://www.thymeleaf.org") 是必须要写的，为了方便后续开发，可以将其添加到html模板文件中：

<img src="https://cdn.nlark.com/yuque/0/2024/png/21376908/1710310831388-377e7bc4-f5b2-4fa3-9410-d90bfdd894b8.png" width="1159" title="" crop="0,0,1,1" id="u0d2806df" class="ne-image" style="font-size: 16px">

### 控制器FirstController处理请求返回逻辑视图名称

```java

package com.jkweilai.springmvc.controller;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;

@Controller
public class FirstController {
    @RequestMapping(value="/haha")
    public String 名字随意(){
        System.out.println("正在处理请求....");
        // 返回逻辑视图名称（决定跳转到哪个页面）
        return "first";
    }
}

```

### 测试

第一步：配置Tomcat服务器

第二步：部署web模块到Tomcat服务器

第三步：启动Tomcat服务器。

第四步：打开浏览器，在浏览器地址栏上输入地址：http://localhost:8080/springmvc/haha

<img src="https://cdn.nlark.com/yuque/0/2024/png/21376908/1710312173540-4e975a51-c0df-47a3-8bdd-f2fbdb8ad831.png" width="482" title="" crop="0,0,1,1" id="u8c054553" class="ne-image" style="font-size: 16px">

后端控制台输出：

<img src="https://cdn.nlark.com/yuque/0/2024/png/21376908/1710312475793-dfb94231-5efe-4a72-840f-63d72143d47f.png" width="297" title="" crop="0,0,1,1" id="ude4fd229" class="ne-image" style="font-size: 16px">

### 执行流程总结

1. 浏览器发送请求：http://localhost:8080/springmvc/haha
2. SpringMVC的前端控制器DispatcherServlet接收到请求
3. DispatcherServlet根据请求路径 `/haha` 映射到 `**FirstController#******名字随意()****`**，调用该方法**
4. **FirstController#名字随意() 处理请求**
5. **FirstController#名字随意() 返回逻辑视图名称 first 给视图解析器**
6. **视图解析器找到 /WEB-INF/templates/first.html 文件，并进行解析，生成视图解析对象返回给前端控制器DispatcherServlet**
7. **前端控制器DispatcherServlet响应结果到浏览器。**

### **一个Controller可以编写多个方法**

一个Controller可以提供多个方法，每个方法通常是处理对应的请求，例如：

```java

@Controller
public class FirstController {
    @RequestMapping(value="/haha")
    public String 名字随意(){
        System.out.println("正在处理请求....");
        // 返回逻辑视图名称（决定跳转到哪个页面）
        return "first";
    }
    
    @RequestMapping("/other")
    public String other(){
        System.out.println("正在处理其它请求...");
        return "other";
    }
}

```

提供 other.html 文件

```html

<!DOCTYPE html>
<html lang="en" xmlns:th="http://www.thymeleaf.org">
<head>
    <meta charset="UTF-8">
    <title>other</title>
</head>
<body>
<h1>other ...</h1>
</body>
</html>

```

在 first.html 文件中，添加超链接，用超链接发送 /other 请求：

```html

<!DOCTYPE html>
<html lang="en" xmlns:th="http://www.thymeleaf.org">
<head>
    <meta charset="UTF-8">
    <title>first springmvc</title>
</head>
<body>
<h1>我的第一个Spring MVC程序</h1>
<a th:href="@{/other}">other请求</a>
</body>
</html>

```

启动Tomcat，打开浏览器，输入请求路径：http://localhost:8080/springmvc/haha

<img src="https://cdn.nlark.com/yuque/0/2024/png/21376908/1710313350020-eaecbfaf-c1ba-44d1-9422-3371248f69a2.png" width="470" title="" crop="0,0,1,1" id="u5a81f52c" class="ne-image" style="font-size: 16px">

点击超链接：other请求

<img src="https://cdn.nlark.com/yuque/0/2024/png/21376908/1710313367394-acfcdb9e-576c-4cc2-8d08-2858854a947e.png" width="416" title="" crop="0,0,1,1" id="u773a31a3" class="ne-image" style="font-size: 16px">

---

## 访问首页面效果

模块名称：`springmvc-002`

### 配置web.xml文件

重点：SpringMVC配置文件的名字和路径是可以手动设置的，如下：

```xml

<?xml version="1.0" encoding="UTF-8"?>
<web-app xmlns="http://xmlns.jcp.org/xml/ns/javaee"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://xmlns.jcp.org/xml/ns/javaee http://xmlns.jcp.org/xml/ns/javaee/web-app_4_0.xsd"
         version="4.0">
    <!--配置前端控制器-->
    <servlet>
        <servlet-name>springmvc</servlet-name>
        <servlet-class>org.springframework.web.servlet.DispatcherServlet</servlet-class>
        <!--手动设置springmvc配置文件的路径及名字-->
        <init-param>
            <param-name>contextConfigLocation</param-name>
            <param-value>classpath:springmvc.xml</param-value>
        </init-param>
        <!--为了提高用户的第一次访问效率，建议在web服务器启动时初始化前端控制器-->
        <load-on-startup>1</load-on-startup>
    </servlet>
    <servlet-mapping>
        <servlet-name>springmvc</servlet-name>
        <url-pattern>/</url-pattern>
    </servlet-mapping>
</web-app>

```

****通过<init-param>来设置SpringMVC配置文件的路径和名字。在DispatcherServlet的init方法执行时设置的。****

****<load-on-startup>1</load-on-startup>建议加上，这样可以提高用户第一次访问的效率。表示在web服务器启动时初始化DispatcherServlet。****

### 编写IndexController

```java

package com.jkweilai.springmvc.controller;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;

@Controller
public class IndexController {
    @RequestMapping("/")
    public String toIndex(){
        return "index";
    }
}

```

表示请求路径如果是：[http://localhost:8080/springmvc/](http://localhost:8080/springmvc/) ，则进入 /WEB-INF/templates/index.html 页面。

****这就是项目的首页效果！！！！！****

### 编写 springmvc.xml 配置

注意位置：在 `resources` 目录下配置 `springmvc.xml`文件

配置内容和之前一样，一个是视图解析器，一个是组件扫描。

### 提供视图

<img src="https://cdn.nlark.com/yuque/0/2024/png/21376908/1710316353838-aac1cd57-12e3-47e4-8b73-2ea2a07a0954.png" width="289" title="" crop="0,0,1,1" id="u9a159361" class="ne-image" style="font-size: 16px">

```html

<!DOCTYPE html>
<html lang="en" xmlns:th="http://www.thymeleaf.org">
<head>
    <meta charset="UTF-8">
    <title>index page</title>
</head>
<body>
<h1>index page</h1>
</body>
</html>

```

### 测试

部署到web服务器，启动web服务器，打开浏览器，在地址栏上输入：[http://localhost:8080/springmvc/](http://localhost:8080/springmvc/)

<img src="https://cdn.nlark.com/yuque/0/2024/png/21376908/1710317491301-4104920d-3537-40d1-b950-2ad1f3398a2d.png" width="421" title="" crop="0,0,1,1" id="uc8b7b484" class="ne-image" style="font-size: 16px">
