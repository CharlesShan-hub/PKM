# 深入理解 Servlet

---

## BS 系统涉及的角色与协议

****详细图：****

![](https://cdn.nlark.com/yuque/0/2025/png/21376908/1748698438324-7379061b-2b64-4a15-b633-8be0a994a1d3.png)

****简略图：****

![](https://cdn.nlark.com/yuque/0/2025/png/21376908/1748591918933-62254fe4-fd52-4fd3-a83f-76da1d33a44e.png)

****

**4 个角色：**

+ 浏览器开发者（开发谷歌浏览器的那些人）
+ Web 服务器开发者（开发 Tomcat 服务器的那些人）
+ Web 应用开发者（JavaWeb 程序员，说的是我们）
+ 数据库服务器开发者（开发 MySQL 数据库的那些人）

**3 个协议：**

+ 浏览器和 Web 服务器之间的通信协议 HTTP。
+ Web 服务器和 Web 应用之间都必须遵循 Servlet 规范。这样 Web 服务器和 Web 应用才可以解耦合。****（怎么理解解耦合：Web 应用开发完成后不一定非要部署到 Tomcat 中，可以部署到任何一个实现了 Servlet 规范的容器中）****
+ Web 应用中的 Java 程序和数据库服务器之间必须遵循 JDBC 规范。这样 Java 程序和具体的数据库产品就解耦合了。****（怎么理解解耦合：Java 程序不一定非要连接 MySQL 数据库，不改任何代码的前提下，还可以连接 Oracle 数据库）****

---

## 模拟 Servlet 接口

我们来模拟一下 Servlet 接口，帮助大家理解 Servlet 的本质及实现原理。不需要那么复杂，我们模拟两个角色，一个规范即可。

**两个角色：**

+ Tomcat 服务器开发者。
+ Web 应用的开发者。（JavaWeb 程序员）

**一个规范：**

+ Servlet 规范。

**创建一个目录用来存储代码：**

![](https://cdn.nlark.com/yuque/0/2025/png/21376908/1748699596162-cbf178a8-a0e7-42ea-a3b1-ff6cba0d8d79.png)

### 制定 Servlet 规范

Servlet 规范中规范了很多东西，我们这里只编写一个 `Servlet`接口即可。`Tomcat 服务器开发者 `和 `Web 应用开发者 `都面向该接口编程，才可以做到解耦合。

打开 ` 模拟 Servlet 本质 `目录，编写 `Servlet`接口，代码如下：

```java
package jakarta.servlet;

public interface Servlet{
    // 处理请求的核心方法
    void service();
}
```

### Web 应用的开发者

Web 应用的开发者应该完全面向 Servlet 接口编写具体的 Servlet。我们这里编写两个 Servlet。一个是处理用户登录的 LoginServlet。一个是删除部门信息的 DeptDeleteServlet。任何一个 Servlet 类都要实现 Servlet 接口，这样开发出的 Web 应用才不会依赖具体的 Web 服务器。

```java
package com.jkweilai.servlet;

import jakarta.servlet.Servlet;

public class LoginServlet implements Servlet{
    public void service(){
        System.out.println("正在处理用户的登录请求...");
    }
}
```

```java
package com.jkweilai.servlet;

import jakarta.servlet.Servlet;

public class DeptDeleteServlet implements Servlet{
    public void service(){
        System.out.println("正在删除部门信息...");
    }
}
```

重要的一步：请求路径和 Servlet 之间的映射关系需要 web.xml 配置文件。这里为了简单，使用 `web.properties`来代替 `web.xml`，新建 `web.properties`，提供以下配置：

```properties
/login=com.jkweilai.servlet.LoginServlet
/del=com.jkweilai.servlet.DeptDeleteServlet
```

这个配置文件的创建和编写都需要 Web 应用的开发者来提供。在这个配置文件中主要配置了请求路径和 Servlet 全限定类名之间的对应关系。当用户的请求路径是 `/login`时执行 `LoginServlet`来处理请求。当用户的请求路径是 `/del`时执行 `DeptDeleteServlet`来处理请求。

### Tomcat 服务器开发者

Tomcat 服务器开发者也要完全面向 Servlet 接口去调用，因为 Tomcat 服务器根本就不知道具体的 Servlet 是哪个，它只知道 Web 应用开发者提供的 Servlet 类都实现了 Servlet 接口。

Tomcat 服务器启动就是执行 main 方法，当服务器启动之后，开始接收用户的请求，当用户请求发送后，Tomcat 获取到用户的请求路径，然后读取 Web 应用开发者编写的 `web.properties`配置文件，通过这个配置文件找到要处理这次请求的 Servlet 类的全限定类名，通过反射机制创建 Servlet 对象，调用 service 方法来处理当前的请求。

大家思考一个问题：为什么这个配置文件的名字以及配置文件所放的位置都是 Servlet 规范中规定好的，不能随便写？

```java
package org.apache.catalina.startup;

import java.util.Scanner;
import java.util.ResourceBundle;
import jakarta.servlet.Servlet;

public class Bootstrap{

    public static void main(String[] args) throws Exception{
        System.out.println("Tomcat服务器启动成功，开始接收用户请求...");
        ResourceBundle bundle = ResourceBundle.getBundle("web");
        Scanner s = new Scanner(System.in);
        while(true){
            System.out.print("请输入请求路径：");
            String url = s.next();
            String servletClassName = bundle.getString(url);
            Class clazz = Class.forName(servletClassName);
            Servlet servlet = (Servlet)clazz.newInstance();
            servlet.service();
        }
    }
}
```

### 测试

编译以上程序：

![](https://cdn.nlark.com/yuque/0/2025/png/21376908/1748702315777-7936f7fa-32cd-403a-a846-fcf8b5599942.png)

如果编译时提示字符集的问题，如下：

![](https://cdn.nlark.com/yuque/0/2025/png/21376908/1748701998763-6cb2db7b-d815-4df8-9edd-909bb2f2341b.png)

这是因为 EditPlus 编辑器默认的字符编码方式为 ANSI。将 EditPlus 的字符编码方式修改为 UTF-8，如下：

![](https://cdn.nlark.com/yuque/0/2025/png/21376908/1748702089356-864b0c5b-7dfc-4086-a418-10dfe3616ca4.png)

然后将我们之前编写的每个文件的字符集修改为 UTF-8：

![](https://cdn.nlark.com/yuque/0/2025/png/21376908/1748702135913-59347664-6e4b-4db8-b437-7aaa6c896b2a.png)

操作完成后一定要重新保存文件哦。

再次编译，结果如下：

![](https://cdn.nlark.com/yuque/0/2025/png/21376908/1748702266074-0389b564-f7f8-422d-8f07-92d90cb80ff9.png)

运行 Bootstrap 类，启动 Tomcat 服务器，开始接收用户的请求：

![](https://cdn.nlark.com/yuque/0/2025/png/21376908/1748702391882-77e32431-ee75-41d8-8203-e817347ac75f.png)

发送`/login`请求，再发送 `/del`请求，观察 Tomcat 服务器是否可以调用到对应的 Servlet：

![](https://cdn.nlark.com/yuque/0/2025/png/21376908/1748702414510-153c54cf-be8c-419d-ac86-664cbc2c92d8.png)

---

## Servlet 规范规定了什么

只有遵守了 Servlet 规范，web 应用才能够运行在不同的符合规范的 web 服务器中。你需要永远记住这句话。

### 定义了一些接口和类

Servlet 规范定义了一些接口和类，例如接口 `jakarta.servlet.Servlet`、`jakarta.servlet.ServletRequest`、`jakarta.servlet.ServletResponse`。Tomcat 服务器面向接口调用和实现。JavaWeb 程序员也面向这些接口调用和实现。这样 Web 服务器和 Web 应用就达到了解耦合。

### 规定了 JavaWeb 应用的目录结构

JavaWeb 应用的目录结构不能随便写，也是 Servlet 规范中规定的，这样我的项目就可以不依赖具体的 Web 服务器了。只要这个服务器是一个符合 Servlet 规范的服务器，都可以运行我的项目。

为了保证 web 应用的可移植性（可以运行在不同的 web 服务器中），Servlet 规范中规定了 web 应用的目录结构，一个标准的 JavaWeb 应用目录结构必须遵守以下规范：

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
3. 放在 `WEB-INF`目录下的资源是****受保护的****，不可在浏览器地址栏上通过地址直接访问。例如在 `WEB-INF`放一个 `index.html`，在浏览器地址栏上访问 `http://localhost:8080/webapproot/WEB-INF/index.html`会出现 `404`错误。（404 是 HTTP 状态码，表示访问的资源找不到。）
4. `WEB-INF\classes`目录下放字节码。
5. `WEB-INF\lib`目录下放第三方的 `jar`包。如连接数据库的驱动 jar 包。当然也可以放到 `CATALINA_HOME/lib`目录下也是可以的，`CATALINA_HOME/lib`是全局的，`WEB-INF/lib`是局部的。
6. `WEB-INF\web.xml`文件中编写请求路径和 Servlet 全限定类名的映射关系。

### 规定的配置文件不能随便写

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
