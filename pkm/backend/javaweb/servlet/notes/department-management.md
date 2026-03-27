# 实现部门管理

在项目的开发过程中会融入新知识点的讲解，请务必注意新知识点的吸收。（****以项目驱动教学。****）

---

## 环境搭建

1. 使用之前的静态网站页面：index.html、list.html、add.html、edit.html、detail.html。完成部门信息的 CRUD 操作。
2. 使用学习 mysql 时的表：dept
3. IDEA 中创建 dept 项目模块，创建 web 目录，添加 web 支持，创建构件。
4. 创建 `WEB-INF/lib`目录，添加 mysql 驱动 jar 包。
5. 创建 lib 目录，添加 servlet-api.jar 包，并将其添加到 classpath。
6. 将构件部署到 Tomcat 服务器。

JDBC 工具类使用之前的：

```java
package com.jkweilai.dept.utils;

import java.sql.*;
import java.util.ResourceBundle;

public class DbUtils {
    private static String url;
    private static String user;
    private static String password;

    static {
        // 读取属性资源文件
        ResourceBundle bundle = ResourceBundle.getBundle("jdbc");
        String driver = bundle.getString("driver");
        url = bundle.getString("url");
        user = bundle.getString("user");
        password = bundle.getString("password");
        // 注册驱动
        try {
            Class.forName(driver);
        } catch (ClassNotFoundException e) {
            throw new RuntimeException(e);
        }
    }

    public static Connection getConnection() throws SQLException {
        Connection conn = DriverManager.getConnection(url, user, password);
        return conn;
    }

    public static void close(Connection conn, Statement stmt, ResultSet rs){
        if (rs != null) {
            try {
                rs.close();
            } catch (SQLException e) {
                throw new RuntimeException(e);
            }
        }
        if (stmt != null) {
            try {
                stmt.close();
            } catch (SQLException e) {
                throw new RuntimeException(e);
            }
        }
        if (conn != null) {
            try {
                conn.close();
            } catch (SQLException e) {
                throw new RuntimeException(e);
            }
        }
    }
}
```

在 src 目录下新建 jdbc.properties 文件，提供以下配置：

```properties
driver=com.mysql.cj.jdbc.Driver
url=jdbc:mysql://localhost:3306/servlet
user=root
password=123456
```

---

## 部门列表

编写 `DeptListServlet`，连接数据库，动态打印表格的 tr。

```java
package com.jkweilai.dept.servlets;

import com.jkweilai.dept.utils.DbUtils;
import jakarta.servlet.ServletException;
import jakarta.servlet.annotation.WebServlet;
import jakarta.servlet.http.HttpServlet;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.io.IOException;
import java.io.PrintWriter;
import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;

@WebServlet("/list")
public class DeptListServlet extends HttpServlet {
    @Override
    protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        response.setContentType("text/html;charset=UTF-8");
        PrintWriter out = response.getWriter();
        out.print("""
                <!DOCTYPE html>
                <html lang="zh-CN">
                <head>
                    <meta charset="UTF-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1.0">
                    <title>部门管理系统 - 部门列表</title>
                    <style>
                        * {
                            margin: 0;
                            padding: 0;
                            box-sizing: border-box;
                            font-family: 'Arial', sans-serif;
                        }
                        body {
                            background-color: #f5f5f5;
                        }
                        .container {
                            max-width: 1200px;
                            margin: 0 auto;
                            padding: 20px;
                        }
                        .header {
                            display: flex;
                            justify-content: space-between;
                            align-items: center;
                            margin-bottom: 30px;
                        }
                        .header h1 {
                            color: #333;
                            font-size: 24px;
                        }
                        .add-btn {
                            padding: 10px 20px;
                            background-color: #4a90e2;
                            color: white;
                            border: none;
                            border-radius: 4px;
                            cursor: pointer;
                            text-decoration: none;
                            font-size: 14px;
                            transition: background-color 0.3s;
                        }
                        .add-btn:hover {
                            background-color: #3a7bc8;
                        }
                        .department-table {
                            width: 100%;
                            border-collapse: collapse;
                            background-color: white;
                            box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
                            border-radius: 4px;
                            overflow: hidden;
                        }
                        .department-table th, .department-table td {
                            padding: 15px;
                            text-align: left;
                            border-bottom: 1px solid #eee;
                        }
                        .department-table th {
                            background-color: #f8f9fa;
                            font-weight: 600;
                            color: #555;
                        }
                        .department-table tr:hover {
                            background-color: #f8f9fa;
                        }
                        .action-btn {
                            padding: 6px 12px;
                            margin-right: 5px;
                            border: none;
                            border-radius: 4px;
                            cursor: pointer;
                            font-size: 13px;
                            transition: all 0.3s;
                            text-decoration: none;
                            display: inline-block;
                        }
                        .view-btn {
                            background-color: #5cb85c;
                            color: white;
                        }
                        .view-btn:hover {
                            background-color: #4cae4c;
                        }
                        .edit-btn {
                            background-color: #f0ad4e;
                            color: white;
                        }
                        .edit-btn:hover {
                            background-color: #eea236;
                        }
                        .delete-btn {
                            background-color: #d9534f;
                            color: white;
                        }
                        .delete-btn:hover {
                            background-color: #d43f3a;
                        }
                        .logout {
                            text-align: right;
                            margin-top: 20px;
                        }
                        .logout a {
                            color: #777;
                            text-decoration: none;
                            font-size: 14px;
                        }
                        .logout a:hover {
                            color: #333;
                        }
                    </style>
                </head>
                <body>
                    <div class="container">
                        <div class="header">
                            <h1>部门列表</h1>
                            <a href="" class="add-btn">添加部门</a>
                        </div>
                        <table class="department-table">
                            <thead>
                                <tr>
                                    <th>部门编号</th>
                                    <th>部门名称</th>
                                    <th>部门地理位置</th>
                                    <th>操作</th>
                                </tr>
                            </thead>
                            <tbody>
                """);
        // 连接数据库，动态打印表格的行tr
        Connection conn = null;
        PreparedStatement pst = null;
        ResultSet rs = null;
        try {
            conn = DbUtils.getConnection();
            String sql = "select deptno,dname,loc from dept";
            pst = conn.prepareStatement(sql);
            rs = pst.executeQuery();
            while(rs.next()){
                String deptno = rs.getString("deptno");
                String dname = rs.getString("dname");
                String loc = rs.getString("loc");
                out.print("<tr>");
                out.print("    <td>" + deptno + "</td>");
                out.print("    <td>" + dname + "</td>");
                out.print("    <td>" + loc + "</td>");
                out.print("    <td>");
                out.print("        <a href='' class='action-btn view-btn'>查看</a>");
                out.print("        <a href='' class='action-btn edit-btn'>修改</a>");
                out.print("        <a href='' class='action-btn delete-btn' onclick=''>删除</a>");
                out.print("    </td>");
                out.print("</tr>");
            }
        } catch (Exception e) {
            e.printStackTrace();
        } finally {
            DbUtils.close(conn, pst, rs);
        }
        out.print("""
                </tbody>
                        </table>
                        <div class="logout">
                            <a href="">退出登录</a>
                        </div>
                    </div>
                </body>
                </html>
                """);
    }
}
```

执行结果如下：

![](https://cdn.nlark.com/yuque/0/2025/png/21376908/1749023316765-9d58231e-7472-4bf6-ac18-69146a386a84.png)

****Java 15 新特性：文本块****

Java 15 正式引入了文本块（Text Blocks），使用 三个双引号 """ 作为定界符（而非反向单引号），用于简化多行字符串的编写：

```java
String json = """
    {
        "name": "Java",
        "version": 17
    }
""";
```

---

## 查看部门

在部门列表页面找到 `查看`按钮，点击查看按钮，显示该部门详细信息。

实现功能的关键步骤：在查看按钮上添加请求路径，并且携带部门编号。例如：/dept/detail?deptno=10

### 添加请求路径

在 DeptListServlet 类中找到查看按钮所在位置：

![](https://cdn.nlark.com/yuque/0/2025/png/21376908/1749023870252-a4318cce-18c7-437b-bc94-a3b8611079af.png)

在 href 属性上添加请求路径，并且携带部门编号，代码修改为：

```java
out.print("        <a href='" + contextPath + "/detail?deptno=" + deptno + "' class='action-btn view-btn'>查看</a>");
```

****说明：****`****contextPath****`****是通过****`****String contextPath = request.getContextPath();****`****获取的。前端发送请求时以****`****/****`****开头，添加项目名，项目名不要写死****`****/dept****`****，应该通过这行代码动态获取。****

启动服务器测试，点击查看按钮，出现以下 404 错误是正常的，因为 Servlet 还没写，重点看浏览器地址栏上的请求地址是否正确：

![](https://cdn.nlark.com/yuque/0/2025/png/21376908/1749024200525-c31167fb-324d-4127-a04c-99205d151a68.png)

### 显示部门详细信息

编写 `DeptDetailServlet`，重写 `doGet`方法，连接数据库，根据部门编号查询部门信息，动态打印详情页：

```java
package com.jkweilai.dept.servlets;

import com.jkweilai.dept.utils.DbUtils;
import jakarta.servlet.ServletException;
import jakarta.servlet.annotation.WebServlet;
import jakarta.servlet.http.HttpServlet;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

import java.io.IOException;
import java.io.PrintWriter;
import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;

@WebServlet("/detail")
public class DeptDetailServlet extends HttpServlet {
    @Override
    protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        response.setContentType("text/html;charset=UTF-8");
        PrintWriter out = response.getWriter();

        // 重点新知识：获取用户发送请求时提交的数据。
        // 用户发送请求时提交的数据自动被Tomcat封装到request对象中了，因此要通过request对象来获取用户提交的数据。
        String deptno = request.getParameter("deptno");

        out.print("""
                <!DOCTYPE html>
                <html lang='zh-CN'>
                <head>
                    <meta charset='UTF-8'>
                    <meta name='viewport' content='width=device-width, initial-scale=1.0'>
                    <title>部门管理系统 - 部门详情</title>
                    <style>
                        * {
                            margin: 0;
                            padding: 0;
                            box-sizing: border-box;
                            font-family: 'Arial', sans-serif;
                        }
                        body {
                            background-color: #f5f5f5;
                        }
                        .container {
                            max-width: 800px;
                            margin: 30px auto;
                            padding: 30px;
                            background-color: white;
                            border-radius: 8px;
                            box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
                        }
                        .header {
                            display: flex;
                            justify-content: space-between;
                            align-items: center;
                            margin-bottom: 30px;
                            padding-bottom: 15px;
                            border-bottom: 1px solid #eee;
                        }
                        .header h1 {
                            color: #333;
                            font-size: 24px;
                        }
                        .back-btn {
                            padding: 8px 16px;
                            background-color: #6c757d;
                            color: white;
                            border: none;
                            border-radius: 4px;
                            cursor: pointer;
                            text-decoration: none;
                            font-size: 14px;
                            transition: background-color 0.3s;
                        }
                        .back-btn:hover {
                            background-color: #5a6268;
                        }
                        .detail-card {
                            padding: 20px;
                            border-radius: 6px;
                            background-color: #f8f9fa;
                        }
                        .detail-row {
                            display: flex;
                            margin-bottom: 15px;
                            padding-bottom: 15px;
                            border-bottom: 1px solid #e9ecef;
                        }
                        .detail-row:last-child {
                            margin-bottom: 0;
                            padding-bottom: 0;
                            border-bottom: none;
                        }
                        .detail-label {
                            width: 150px;
                            font-weight: 600;
                            color: #495057;
                        }
                        .detail-value {
                            flex: 1;
                            color: #212529;
                        }
                        .action-btns {
                            margin-top: 30px;
                            text-align: right;
                        }
                        .edit-btn {
                            padding: 10px 20px;
                            background-color: #f0ad4e;
                            color: white;
                            border: none;
                            border-radius: 4px;
                            cursor: pointer;
                            text-decoration: none;
                            font-size: 14px;
                            transition: background-color 0.3s;
                        }
                        .edit-btn:hover {
                            background-color: #eea236;
                        }
                    </style>
                </head>
                <body>
                """);

        Connection conn = null;
        PreparedStatement ps = null;
        ResultSet rs = null;
        try {
            conn = DbUtils.getConnection();
            String sql = "select * from dept where deptno = ?";
            ps = conn.prepareStatement(sql);
            ps.setString(1, deptno);
            rs = ps.executeQuery();
            if(rs.next()) {
                String dname = rs.getString("dname");
                String loc = rs.getString("loc");
                out.print("<div class='container'>");
                out.print("    <div class='header'>");
                out.print("        <h1>部门详细信息</h1>");
                out.print("        <a href='' class='back-btn'>返回列表</a>");
                out.print("    </div>");
                out.print("    <div class='detail-card'>");
                out.print("        <div class='detail-row'>");
                out.print("            <div class='detail-label'>部门编号</div>");
                out.print("            <div class='detail-value'>" + deptno + "</div>");
                out.print("        </div>");
                out.print("        <div class='detail-row'>");
                out.print("            <div class='detail-label'>部门名称</div>");
                out.print("            <div class='detail-value'>" + dname + "</div>");
                out.print("        </div>");
                out.print("        <div class='detail-row'>");
                out.print("            <div class='detail-label'>部门地理位置</div>");
                out.print("            <div class='detail-value'>" + loc + "</div>");
                out.print("        </div>");
                out.print("    </div>");
                out.print("    <div class='action-btns'>");
                out.print("        <a href='' class='edit-btn'>编辑部门信息</a>");
                out.print("    </div>");
                out.print("</div>");
            }
        } catch (Exception e) {
            e.printStackTrace();
        } finally {
            DbUtils.close(conn, ps, rs);
        }
        out.print("""        
                </body>
                </html>
                """);
    }
}

```

运行结果：

![](https://cdn.nlark.com/yuque/0/2025/png/21376908/1749025994506-ce2e7413-c23b-4e83-a7f1-138b7001af4b.png)

****重点内容：****

实现本功能时，使用了一个新的知识点：通过 request 对象获取用户提交的数据。

HTTP 协议中规定，无论是 get 还是 post 请求，提交数据的格式为：name=value&name=value&name=value

要获取 value，可以通过 request 对象 getParameter()方法来获取：

```java
String value = request.getParameter("name");
```

需要注意的是 `name`必须要写正确了，尽量采用复制粘贴方式。

另外需要注意的是，该方法的返回值类型永远都是字符串形式。

---

## 删除部门

### 添加请求路径

发送 `/dept/delete?deptno=10`的请求，根据部门编号删除部门信息。

DeptListServlet 中找到删除按钮：

![](https://cdn.nlark.com/yuque/0/2025/png/21376908/1749026829298-97cab244-2f26-4ada-a673-98d9b5520328.png)

添加删除的请求路径：

```java
out.print("        <a href='javascript:void(0)' class='action-btn delete-btn' onclick='if(window.confirm(\"您确定删除吗？\"))document.location.href=\"" + contextPath + "/delete?deptno=" + deptno + "\"'>删除</a>");
```

### 实现删除

编写 DeptDeleteServlet，获取部门编号，连接数据库，根据部门编号删除数据。删除成功后再跳转到部门列表页面。

```java
package com.jkweilai.dept.servlets;

import com.jkweilai.dept.utils.DbUtils;
import jakarta.servlet.ServletException;
import jakarta.servlet.annotation.WebServlet;
import jakarta.servlet.http.HttpServlet;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

import java.io.IOException;
import java.sql.Connection;
import java.sql.PreparedStatement;

@WebServlet("/delete")
public class DeptDeleteServlet extends HttpServlet {
    @Override
    protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        // 获取部门编号
        String deptno = request.getParameter("deptno");
        // 连接数据库删除部门
        Connection conn = null;
        PreparedStatement ps = null;
        try {
            conn = DbUtils.getConnection();
            String sql = "delete from dept where deptno = ?";
            ps = conn.prepareStatement(sql);
            ps.setString(1, deptno);
            ps.executeUpdate();
        } catch (Exception e) {
            e.printStackTrace();
        } finally {
            DbUtils.close(conn, ps, null);
        }
    }
}
```

### 再跳转到部门列表

删除之后，需要展示一个全新的列表，因此需要让浏览器重新发一次全新的 `/dept/list`请求，只有浏览器发送这个请求，Tomcat 才会执行 DeptListServlet，再查一次数据库，展示新的列表，在 JavaWeb 开发中如何使用 Java 代码让浏览器自动再发一次全新的请求呢？使用重定向机制。代码如下：

****重点内容：****

```java
response.sendRedirect("/dept/list");
```

需要注意的是：重定向时的路径写法和前端超链接的写法一致，都以 `/` 开始，并且带项目名。

在 `DeptDeleteServlet`的末尾添加以下代码：

```java
response.sendRedirect(request.getContextPath() + "/list");
```

---

## 跳转到修改页面

### 添加请求路径

找到 DeptListServlet 中的修改按钮，添加请求路径 `/dept/edit?deptno=10`，代码如下：

```java
out.print("        <a href='" + contextPath + "/edit?deptno=" + deptno + "' class='action-btn edit-btn'>修改</a>");
```

### 展示修改页面

编写 DeptEditServlet，获取部门编号，根据部门编号查询部门信息，动态展示修改页面：

```java
package com.jkweilai.dept.servlets;

import com.jkweilai.dept.utils.DbUtils;
import jakarta.servlet.ServletException;
import jakarta.servlet.annotation.WebServlet;
import jakarta.servlet.http.HttpServlet;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

import java.io.IOException;
import java.io.PrintWriter;
import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;

@WebServlet("/edit")
public class DeptEditServlet extends HttpServlet {
    @Override
    protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        response.setContentType("text/html;charset=UTF-8");
        PrintWriter out = response.getWriter();

        // 获取部门编号
        String deptno = request.getParameter("deptno");

        out.print("""
                <!DOCTYPE html>
                <html lang="zh-CN">
                <head>
                    <meta charset="UTF-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1.0">
                    <title>部门管理系统 - 修改部门</title>
                    <style>
                        * {
                            margin: 0;
                            padding: 0;
                            box-sizing: border-box;
                            font-family: 'Arial', sans-serif;
                        }
                        body {
                            background-color: #f5f5f5;
                        }
                        .container {
                            max-width: 800px;
                            margin: 30px auto;
                            padding: 30px;
                            background-color: white;
                            border-radius: 8px;
                            box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
                        }
                        .header {
                            display: flex;
                            justify-content: space-between;
                            align-items: center;
                            margin-bottom: 30px;
                            padding-bottom: 15px;
                            border-bottom: 1px solid #eee;
                        }
                        .header h1 {
                            color: #333;
                            font-size: 24px;
                        }
                        .back-btn {
                            padding: 8px 16px;
                            background-color: #6c757d;
                            color: white;
                            border: none;
                            border-radius: 4px;
                            cursor: pointer;
                            text-decoration: none;
                            font-size: 14px;
                            transition: background-color 0.3s;
                        }
                        .back-btn:hover {
                            background-color: #5a6268;
                        }
                        .form-group {
                            margin-bottom: 20px;
                        }
                        .form-group label {
                            display: block;
                            margin-bottom: 8px;
                            color: #555;
                            font-weight: 500;
                        }
                        .form-group input, .form-group select {
                            width: 100%;
                            padding: 12px;
                            border: 1px solid #ddd;
                            border-radius: 4px;
                            font-size: 16px;
                            transition: border-color 0.3s;
                        }
                        .form-group input:focus, .form-group select:focus {
                            border-color: #4a90e2;
                            outline: none;
                        }
                        .form-group input[readonly] {
                            background-color: #f8f9fa;
                            color: #6c757d;
                        }
                        .btn-group {
                            display: flex;
                            justify-content: space-between;
                            margin-top: 30px;
                            padding-top: 15px;
                            border-top: 1px solid #eee;
                        }
                        .submit-btn {
                            padding: 12px 24px;
                            background-color: #4a90e2;
                            color: white;
                            border: none;
                            border-radius: 4px;
                            cursor: pointer;
                            font-size: 16px;
                            transition: background-color 0.3s;
                        }
                        .submit-btn:hover {
                            background-color: #3a7bc8;
                        }
                        .cancel-btn {
                            padding: 12px 24px;
                            background-color: #6c757d;
                            color: white;
                            border: none;
                            border-radius: 4px;
                            cursor: pointer;
                            font-size: 16px;
                            transition: background-color 0.3s;
                            text-decoration: none;
                        }
                        .cancel-btn:hover {
                            background-color: #5a6268;
                        }
                    </style>
                </head>
                <body>
                """);

        Connection conn = null;
        PreparedStatement ps = null;
        ResultSet rs = null;
        try {
            conn = DbUtils.getConnection();
            String sql = "select * from dept where deptno = ?";
            ps = conn.prepareStatement(sql);
            ps.setString(1, deptno);
            rs = ps.executeQuery();
            if(rs.next()){
                String dname = rs.getString("dname");
                String loc = rs.getString("loc");
                out.print("<div class='container'>");
                out.print("    <div class='header'>");
                out.print("    <h1>修改部门信息</h1>");
                out.print("    <a href='' class='back-btn'>返回列表</a>");
                out.print("    </div>");
                out.print("    <form action='#' method='post'>");
                out.print("    <div class='form-group'>");
                out.print("        <label for='deptId'>部门编号</label>");
                out.print("        <input type='text' id='deptId' name='deptId' value='" + deptno + "' readonly>");
                out.print("    </div>");
                out.print("    <div class='form-group'>");
                out.print("        <label for='deptName'>部门名称</label>");
                out.print("        <input type='text' id='deptName' name='deptName' value='" + dname + "' required>");
                out.print("    </div>");
                out.print("    <div class='form-group'>");
                out.print("        <label for='location'>部门地理位置</label>");
                out.print("        <input type='text' id='location' name='location' value='" + loc + "' required>");
                out.print("    </div>");
                out.print("    <div class='btn-group'>");
                out.print("        <a href='' class='cancel-btn'>取消</a>");
                out.print("        <button type='submit' class='submit-btn'>保存更改</button>");
                out.print("    </div>");
                out.print("    </form>");
                out.print("</div>");
            }
        } catch (Exception e) {
            e.printStackTrace();
        } finally {
            DbUtils.close(conn, ps, rs);
        }

        out.print("""        
                </body>
                </html>
                """);
    }
}

```

运行效果如下：

![](https://cdn.nlark.com/yuque/0/2025/png/21376908/1749028828789-378c8320-abbc-4ccc-a406-7a71841cb4f0.png)

---

## 修改部门

### 提交表单

在修改页面 （DeptEditServlet），点击保存更改，发送请求，提交 form 表单。部门编号不支持修改。

![](https://cdn.nlark.com/yuque/0/2025/png/21376908/1749031578308-0ec990fd-98d4-42d3-b417-457aa3d12e62.png)

修改后的代码如下：

```java
out.print("<div class='container'>");
out.print("    <div class='header'>");
out.print("    <h1>修改部门信息</h1>");
out.print("    <a href='" + request.getContextPath() + "/list' class='back-btn'>返回列表</a>");
out.print("    </div>");
out.print("    <form action='" + request.getContextPath() + "/update' method='post'>");
out.print("    <div class='form-group'>");
out.print("        <label for='deptId'>部门编号</label>");
out.print("        <input type='text' id='deptId' name='deptno' value='" + deptno + "' readonly>");
out.print("    </div>");
out.print("    <div class='form-group'>");
out.print("        <label for='deptName'>部门名称</label>");
out.print("        <input type='text' id='deptName' name='dname' value='" + dname + "' required>");
out.print("    </div>");
out.print("    <div class='form-group'>");
out.print("        <label for='location'>部门地理位置</label>");
out.print("        <input type='text' id='location' name='loc' value='" + loc + "' required>");
out.print("    </div>");
out.print("    <div class='btn-group'>");
out.print("        <a href='" + request.getContextPath() + "/list' class='cancel-btn'>取消</a>");
out.print("        <button type='submit' class='submit-btn'>保存更改</button>");
out.print("    </div>");
out.print("    </form>");
out.print("</div>");
```

### 修改部门

编写 DeptUpdateServlet，获取表单提交的数据，更新数据库，更新成功后重定向到列表页面：

```java
package com.jkweilai.dept.servlets;

import com.jkweilai.dept.utils.DbUtils;
import jakarta.servlet.ServletException;
import jakarta.servlet.annotation.WebServlet;
import jakarta.servlet.http.HttpServlet;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

import java.io.IOException;
import java.sql.Connection;
import java.sql.PreparedStatement;

@WebServlet("/update")
public class DeptUpdateServlet extends HttpServlet {
    @Override
    protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        // 解决请求体中文乱码问题
        request.setCharacterEncoding("UTF-8");
        // 获取表单提交的数据
        String deptno = request.getParameter("deptno");
        String dname = request.getParameter("dname");
        String loc = request.getParameter("loc");
        // 连接数据库更新部门
        Connection conn = null;
        PreparedStatement ps = null;
        try {
            conn = DbUtils.getConnection();
            String sql = "update dept set dname = ?, loc = ? where deptno = ?";
            ps = conn.prepareStatement(sql);
            ps.setString(1, dname);
            ps.setString(2, loc);
            ps.setString(3, deptno);
            ps.executeUpdate();
        } catch (Exception e) {
            e.printStackTrace();
        } finally {
            DbUtils.close(conn, ps, null);
        }
        // 重定向到列表页面
        response.sendRedirect(request.getContextPath() + "/list");
    }
}
```

### 关于请求数据的乱码问题

#### post 请求乱码
`Tomcat 7`及之前的版本，请求体默认字符集采用的是 ISO-8859-1 。当使用以下代码获取请求体的数据时，会出现中文乱码问题：

```java
String value = request.getParameter("name");
```

怎么解决请求体的乱码问题呢，只需要在 `request.getParameter("name");`之前执行以下代码即可：

```java
request.setCharacterEncoding("UTF-8");
```

从 `Tomcat8.0`开始，请求体默认字符编码方式已改为 UTF-8，**大部分情况下不需要手动处理乱码问题。除非浏览器客户端提交数据时采用 GBK 的方式，我们仍然需要执行以下代码来解决中文乱码问题：**

```java
request.setCharacterEncoding("GBK");
```

#### get 请求乱码
get 请求数据在请求行上提交，格式：uri?name=value&name=value

如果 get 请求提交中文数据，在 Tomcat7 及之前的版本中通过 `request.getParameter("name")`取数据时也会出现中文乱码问题。怎么解决 get 请求乱码问题呢？修改 `conf/server.xml`配置文件：

![](https://cdn.nlark.com/yuque/0/2025/png/21376908/1749035321888-761af397-ea18-40e2-8d7d-ad2d560b9f2b.png)

在以上 `<Connector>` 标签中添加 `URIEncoding="UTF-8"`属性。

Tomcat8 之后的版本中 `URIEncoding`属性的默认值就是 UTF-8，因此 get 请求乱码问题基本上也不需要考虑了。

怎么能够知道 `<Connector>`标签都支持哪些属性呢？可以参照 Tomcat 内部帮助文档：`CATALINA_HOME/webapps/docs/config/http.html`

![](https://cdn.nlark.com/yuque/0/2025/png/21376908/1749035530854-627f9e3c-57df-491f-845a-a3915d8c9303.png)

---

## 添加部门

### 跳转到添加部门页面

在部门列表页面点击添加部门按钮：

![](https://cdn.nlark.com/yuque/0/2025/png/21376908/1749035831501-cdecc603-bfa8-427a-b449-8a5ecc9b44a0.png)

在 DeptListServlet 中找到这个按钮，设置超链接地址为：http://localhost:8080/dept/add.html

![](https://cdn.nlark.com/yuque/0/2025/png/21376908/1749036126696-3b601ee6-7e01-4673-b287-2f216206ba47.png)

大家可能在想，为什么跳转到添加部门页面不需要经过 Servlet？这是因为添加部门页面是一个纯静态页面。不需要动态网页技术。

在项目的根下创建 `add.html`文件，将之前的 add.html 文件中的代码拷贝粘贴进来。测试效果如下：

![](https://cdn.nlark.com/yuque/0/2025/png/21376908/1749036189624-492b40a9-cbea-46b8-a865-b47d21a9f8d2.png)

将表单中的部门编号删除，因为部门编号可以在后台 Java 程序中动态生成。最终效果如下：

![](https://cdn.nlark.com/yuque/0/2025/png/21376908/1749036252161-b674a181-7428-41ec-9b0e-df55fc3f01dc.png)

### 设置 form 表单

表单的 action 属性设置，method 设置，表单项的 name 设置等。

```html
<form action="/dept/save" method="post">
  <div class="form-group">
    <label for="deptName">部门名称</label>
    <input type="text" id="deptName" name="dname" placeholder="请输入部门名称" required>
  </div>
  <div class="form-group">
    <label for="location">部门地理位置</label>
    <input type="text" id="location" name="loc" placeholder="请输入部门地理位置" required>
  </div>
  <div class="footer">
    <button type="submit" class="submit-btn">保存</button>
  </div>
</form>
```

### 保存部门

编写 DeptSaveServlet，重写 doPost 方法，获取表单提交的数据，连接数据库保存部门信息，然后重定向到列表页面。

注意：部门编号生成算法：当前最大部门编号 + 1。另外要注意多线程并发的问题，使用线程同步机制保证安全。

```java
package com.jkweilai.dept.servlets;

import com.jkweilai.dept.utils.DbUtils;
import jakarta.servlet.ServletException;
import jakarta.servlet.annotation.WebServlet;
import jakarta.servlet.http.HttpServlet;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

import java.io.IOException;
import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;

@WebServlet("/save")
public class DeptSaveServlet extends HttpServlet {
    @Override
    protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        // 解决请求体乱码问题
        request.setCharacterEncoding("UTF-8");
        // 获取部门信息
        String dname = request.getParameter("dname");
        String loc = request.getParameter("loc");
        // 连接数据库保存数据
        // 查询当前最大的部门编号，新部门编号在当前最大部门编号基础上 + 1
        Connection conn = null;
        PreparedStatement ps = null;
        PreparedStatement ps1 = null;
        ResultSet rs = null;
        try {
            conn = DbUtils.getConnection();
            String sql = "select max(deptno) as maxDeptno from dept";
            ps = conn.prepareStatement(sql);
            rs = ps.executeQuery();
            if (rs.next()) {
                int maxDeptno = rs.getInt("maxDeptno");
                synchronized (this){
                    int deptno = maxDeptno + 1;
                    String insertSql = "insert into dept values(?,?,?)";
                    ps1 = conn.prepareStatement(insertSql);
                    ps1.setInt(1, deptno);
                    ps1.setString(2, dname);
                    ps1.setString(3, loc);
                    ps1.executeUpdate();
                }
            }
        } catch (Exception e) {
            e.printStackTrace();
        } finally {
            DbUtils.close(null, ps1, null);
            DbUtils.close(conn, ps, rs);
        }

        response.sendRedirect(request.getContextPath() + "/list");
    }
}

```

到此为止，我们已经完成了基本的 CRUD 操作。
