
# 默认 Servlet

## 18.1. 什么是默认 Servlet

JavaWeb 开发中，任何一个 Web 服务器都会内置一个默认的 Servlet

在 Tomcat 中，默认的 Servlet 类名是：`org.apache.catalina.servlets.DefaultServlet`，它是服务器内置的，专门用来处理静态资源（HTML,CSS,JS,图片等静态资源）和兜底返回 404 的默认处理器。

它被配置在服务器的 web.xml 文件中：`%CATALINA_HOME%/conf/web.xml`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<web-app xmlns="urn:jakarta:jsf:default">
    <servlet>
    <servlet-name>default</servlet-name>
    <servlet-class>org.apache.catalina.servlets.DefaultServlet</servlet-class>
    <init-param>
    <param-name>debug</param-name>
    <param-value>0</param-value>
    </init-param>
    <init-param>
    <param-name>listings</param-name>
    <param-value>false</param-value>
    </init-param>
    </servlet>
    <servlet-mapping>
    <servlet-name>default</servlet-name>
    <url-pattern>/</url-pattern>
    </servlet-mapping>
</web-app>
```

通过配置可以看到，默认 Servlet 的映射路径是 `/`

### 这个 `/` 会自动拦截以下的请求：

1. 访问所有静态资源时，会走默认的 Servlet，默认的 Servlet 负责给你找静态资源并响应给浏览器。如果找不到这个静态资源，默认 Servlet 会直接响应 404 给前端。
2. 访问的资源不存在时，会走默认的 Servlet，默认 Servlet 会直接响应 404 给前端。

**注意：默认 Servlet 又叫做兜底处理器。**


## 18.2. 自定义默认 Servlet 会怎样

如果自定义默认 Servlet，如下：

```xml
1    <servlet>
2    <servlet-name>defaultServlet</servlet-name>
3    <servlet-class>com.jkweilai.servlet.DefaultServlet</servlet-class>
4    </servlet>
5    <servlet-mapping>
6    <servlet-name>defaultServlet</servlet-name>
7    <url-pattern>/</url-pattern>
8    </servlet-mapping>
```

如果你的 `com.jkweilai.servlet.DefaultServlet` 中什么也没写，就会导致无法正常访问静态资源，以及就算访问的资源不存在，也不会报 404 的提示信息了。

**结论：尽量不要自定义默认 Servlet，也就是说定义资源时不要占用 `<url-pattern></url-pattern>` 请求路径。**
