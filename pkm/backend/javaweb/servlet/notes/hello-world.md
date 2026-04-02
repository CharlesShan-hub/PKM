# Hello World

---

## 目录结构

```plain
webapproot
    |-------html
    |-------css
    |-------javascript
    |-------其它静态资源
    |-------WEB-INF
        |-------classes
        |-------lib
        |-------web.xml
```

1. 静态资源直接放在 web 应用的根目录下即可。这里的静态资源包括但不限于：html css javascript images 等。
2. WEB-INF 名字必须是全部大写的 `WEB-INF`
3. 放在 `WEB-INF`目录下的资源**是受保护**的，不可在浏览器地址栏上通过地址直接访问。例如在 `WEB-INF`放一个 `index.html`，在浏览器地址栏上访问 `http://localhost:8080/webapproot/WEB-INF/index.html`会出现 `404`错误。（404 是 HTTP 状态码，表示访问的资源找不到。）
4. `WEB-INF\classes`目录下放字节码。
5. `WEB-INF\lib`目录下放第三方的 `jar`包。如连接数据库的驱动 jar 包。当然也可以放到 `CATALINA_HOME/lib`目录下也是可以的，`CATALINA_HOME/lib`是全局的，`WEB-INF/lib`是局部的。
6. `WEB-INF\web.xml`文件中编写请求路径和 Servlet 全限定类名的映射关系。

Servlet 规范中规定了 web 应用的配置文件不能随意编写，因为 Tomcat 服务器是按照这个规范去找这个文件，去解析这个文件的：

1. 文件名必须叫做 `web.xml`。
2. 文件必须存放到 `webapproot/WEB-INF/web.xml`这个位置。
3. web.xml 文件中的具体配置信息也不能随便写，例如要配置一个请求路径和 Servlet 全限定类名之间的映射关系，必须按照以下配置进行：

```xml
<!--servlet配置信息-->
<servlet>
  <!--servlet的名字随便写一个，但是要保证和servlet mapping中的servlet名字一致。-->
  <servlet-name>loginServlet</servlet-name>
  <!--这里必须填写Servlet类的全限定类名-->
  <servlet-class>com.jkweilai.servlet.LoginServlet</servlet-class>
</servlet>
<!--servlet映射信息-->
<servlet-mapping>
  <servlet-name>loginServlet</servlet-name>
  <!--请求路径必须以 / 开始，不要添加项目名。-->
  <url-pattern>/login</url-pattern>
  <!--支持编写多个-->
  <url-pattern>/a/b/c</url-pattern>
</servlet-mapping>
```

---

## Hello World

具体内容参考：[first-servlet](../details/first-servlet.md)，这里仅记录核心内容

首先是创建目录

```plain
web01
    |-------WEB-INF
        |-------classes
        |-------web.xml
```

在任意位置编写实现类，需要实现五个方法

```java
package com.jkweilai.servlet;

import jakarta.servlet.Servlet;
import jakarta.servlet.ServletException;
import jakarta.servlet.ServletRequest;
import jakarta.servlet.ServletResponse;
import jakarta.servlet.ServletConfig;
import java.io.PrintWriter;
import java.io.IOException;

public class HelloServlet implements Servlet{

    public void init(ServletConfig config) throws ServletException{}

    public void service(ServletRequest request,ServletResponse response)
        throws ServletException, IOException{
        // 向控制台打印
        System.out.println("Hello Servlet!");
        
        // 向浏览器上响应HTML
        response.setContentType("text/html"); // 设置响应的内容类型，这个对解决响应时的中文乱码问题没有作用。
        response.setCharacterEncoding("UTF-8"); // 设置响应时采用的字符编码方式。这个是解决响应时中文乱码问题的关键。
        
        PrintWriter out = response.getWriter();
        out.print("<h1>Hello Servlet!</h1>");
        out.print("<h1>你好，服务器端的小程序！</h1>");
    }

    public void destroy(){}

    public String getServletInfo(){
        return "";
    }

    public ServletConfig getServletConfig(){
        return null;
    }

}
```

编译需要确保 javac 能找到 `servlet-api.jar`，然后把生成的 `.class` 文件放到指定位置

```plain
web01
    |---WEB-INF
        |---classes
            |---com (要注意一定要带着包粘贴)
                |---jkweilai
                    |---HelloServlet
```

编写 web.xml

```xml
<?xml version="1.0" encoding="UTF-8"?>
<web-app xmlns="https://jakarta.ee/xml/ns/jakartaee"
  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xsi:schemaLocation="https://jakarta.ee/xml/ns/jakartaee
                      https://jakarta.ee/xml/ns/jakartaee/web-app_6_0.xsd"
  version="6.0"
  metadata-complete="true">

  <servlet>
      <servlet-name>firstServlet</servlet-name>
      <servlet-class>com.jkweilai.servlet.HelloServlet</servlet-class>
  </servlet>
  <servlet-mapping>
      <servlet-name>firstServlet</servlet-name>
      <url-pattern>/hello</url-pattern>
  </servlet-mapping>
  
</web-app>
```

最后把编写好的 web01 放到 WEBAPPs 下边。

---

## 静态网站案例

后边很多案例会基于这个静态网站进行进一步开发，这个案例就是在servlet上搭建一个部门管理系统的最初的雏形。详细内容：[static-website-development](../details/static-website-development.md)