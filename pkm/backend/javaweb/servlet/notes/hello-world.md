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

1. 静态资源：直接放在 web 应用的根目录下即可。这里的静态资源包括但不限于：html css、javascript、images 等。
2. WEB-INF
    1. 名字必须是全部大写的 `WEB-INF`
    2. 放在 `WEB-INF`目录下的资源**是受保护**的，不可在浏览器地址栏上通过地址直接访问。例如在 `WEB-INF`放一个 `index.html`，在浏览器地址栏上访问 `http://localhost:8080/webapproot/WEB-INF/index.html`会出现 `404`错误。
3. `WEB-INF\classes`：放字节码
4. `WEB-INF\lib`：放第三方的 `jar`包。如连接数据库的驱动 `jar` 包。当然也可以放到 `CATALINA_HOME/lib`目录下也是可以的，`CATALINA_HOME/lib`是全局的，`WEB-INF/lib`是局部的。
5. `WEB-INF\web.xml`文件：
    1. 编写请求路径和 Servlet 全限定类名的映射关系。
    2. Servlet 规范中规定了 web 应用的配置文件不能随意编写，因为 Tomcat 服务器是按照这个规范去找这个文件，去解析这个文件的：
    3. 文件必须存放到 `webapproot/WEB-INF/web.xml`这个位置。
    4. `web.xml` 文件中的具体配置信息也不能随便写，例如要配置一个请求路径和 Servlet 全限定类名之间的映射关系，必须按照以下配置进行：
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

## 案例分析

1. 静态网站案例（这个只是前端内容）：后边很多案例会基于这个静态网站进行进一步开发，这个案例就是在servlet上搭建一个部门管理系统的最初的雏形。详细内容：[static-website-development](../details/static-website-development.md)
2. Hello World：[first-servlet](../details/first-servlet.md)
3. java程序里边可以使用jdbc访问数据库：[database-connection](database-connection.md)

---

## 使用IDEA编写servlet

* [servlet-with-idea](../details/servlet-with-idea.md)