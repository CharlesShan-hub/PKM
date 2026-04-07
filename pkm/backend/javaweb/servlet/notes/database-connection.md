# Servlet 连接数据库

继续在 `web01`项目中实现连接数据库的效果。实现功能：以列表形式显示部门名称。

> 这个案例时使用JDBC连接的数据库。

---

## 添加 mysql 驱动

在 `WEB-INF`目录下新建 `lib`目录，将 `mysql.jar`驱动放到 `lib`目录中。

![](../assets/1748911994986-fe9bc878-f3db-4fd8-8df1-0ce33086aa7a.png)

---

## 编写 DeptListServlet

```java
package com.jkweilai.servlet;

import jakarta.servlet.Servlet;
import jakarta.servlet.ServletException;
import jakarta.servlet.ServletRequest;
import jakarta.servlet.ServletResponse;
import jakarta.servlet.ServletConfig;
import java.io.PrintWriter;
import java.io.IOException;
import java.sql.*;

public class DeptListServlet implements Servlet{

    public void init(ServletConfig config) throws ServletException{}

    public void service(ServletRequest request,ServletResponse response)
        throws ServletException, IOException{
        response.setContentType("text/html;charset=UTF-8");
        PrintWriter out = response.getWriter();

        Connection conn = null;
        PreparedStatement ps = null;
        ResultSet rs = null;
        try{
            // 1.注册驱动
            Class.forName("com.mysql.cj.jdbc.Driver");
            // 2.获取连接
            String url = "jdbc:mysql://localhost:3306/servlet";
            String user = "root";
            String password = "123456";
            conn = DriverManager.getConnection(url, user, password);
            // 3.获取预编译的数据库操作对象
            String sql = "select dname from dept";
            ps = conn.prepareStatement(sql);
            // 4.执行SQL
            rs = ps.executeQuery();
            // 5.处理查询结果集
            while(rs.next()){
                String dname = rs.getString("dname");
                out.print(dname);
                out.print("<br>");
            }
        }catch(Exception e){
            e.printStackTrace();
        }finally{
            // 6.释放资源
            if(rs != null){
                try{
                    rs.close();
                }catch(Exception e){
                    e.printStackTrace();
                }
            }
            if(ps != null){
                try{
                    ps.close();
                }catch(Exception e){
                    e.printStackTrace();
                }
            }
            if(conn != null){
                try{
                    conn.close();
                }catch(Exception e){
                    e.printStackTrace();
                }
            }
        }
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

编译后，将编译后的字节码拷贝到 `WEB-INF/classes`目录下，这里不再赘述。

---

## 编写 web.xml

```xml
<servlet>
    <servlet-name>dListServlet</servlet-name>
    <servlet-class>com.jkweilai.servlet.DeptListServlet</servlet-class>
</servlet>
<servlet-mapping>
    <servlet-name>dListServlet</servlet-name>
    <url-pattern>/list</url-pattern>
</servlet-mapping>
```

---

## 提供超链接

在 `index.html`文件中添加超链接：

```html
<!--对于前端请求路径目前以 / 开始，带项目名。web.xml文件中的路径不带项目名。-->
<a href="/web01/list">部门列表</a>
```

---

## 部署测试

将项目部署到 Tomcat 的 webapps 目录下，启动 Tomcat 服务器，打开浏览器输入地址：<http://localhost:8080/web01/index.html>

![](../assets/1748912894420-6557f035-2495-4439-821d-8ccf778fae53.png)

点击部门列表超链接发送请求：

![](../assets/1748912917558-644e7f88-c10f-4aa1-b75d-74d341eb00b5.png)
