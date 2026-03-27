# 使用RESTful实现用户管理系统

---

## 静态页面准备

文件包括：user.css、user_index.html、user_list.html、user_add.html、user_edit.html。代码如下：

### user.css

```css

.header {
  background-color: #f2f2f2;
  padding: 20px;
  text-align: center;
}

ul {
  list-style-type: none;
  margin: 0;
  padding: 0;
  overflow: hidden;
  background-color: #333;
}

li {
  float: left;
}

li a {
  display: block;
  color: white;
  text-align: center;
  padding: 14px 16px;
  text-decoration: none;
}

li a:hover:not(.active) {
  background-color: #111;
}

.active {
  background-color: #4CAF50;
}

form {
  width: 50%;
  margin: 0 auto;
  padding: 20px;
  border: 1px solid #ddd;
  border-radius: 4px;
}

label {
  display: block;
  margin-bottom: 8px;
}

input[type="text"], input[type="email"], select {
  width: 100%;
  padding: 6px 10px;
  margin: 8px 0;
  box-sizing: border-box;
  border: 1px solid #555;
  border-radius: 4px;
  font-size: 16px;
}

button[type="submit"] {
  padding: 10px;
  background-color: #4CAF50;
  color: #fff;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

button[type="submit"]:hover {
  background-color: #3e8e41;
}

table {
  border-collapse: collapse;
  width: 100%;
}

th, td {
  border: 1px solid #ddd;
  padding: 8px;
  text-align: left;
}

th {
  background-color: #f2f2f2;
}

tr:nth-child(even) {
  background-color: #f2f2f2;
}

.header {
  background-color: #f2f2f2;
  padding: 20px;
  text-align: center;
}

a {
  text-decoration: none;
  color: #333;
}

.add-button {
  margin-bottom: 20px;
  padding: 10px;
  background-color: #4CAF50;
  color: #fff;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

.add-button:hover {
  background-color: #3e8e41;
}

```

### user_index.html

```html

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>用户管理系统</title>
  <link rel="stylesheet" href="user.css" type="text/css"></link>
</head>
<body>
  <div class="header">
    <h1>用户管理系统</h1>
  </div>
  <ul>
    <li><a class="active" href="user_list.html">用户列表</a></li>
  </ul>
</body>
</html>

```

### user_list.html

```html

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>用户列表</title>
  <link rel="stylesheet" href="user.css" type="text/css"></link>
</head>
<body>
  <div class="header">
    <h1>用户列表</h1>
  </div>
  <div class="add-button-wrapper">
    <a class="add-button" href="user_add.html">新增用户</a>
  </div>
  <table>
    <thead>
      <tr>
        <th>编号</th>
        <th>用户名</th>
        <th>性别</th>
        <th>邮箱</th>
        <th>操作</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>1</td>
        <td>张三</td>
        <td>男</td>
        <td>zhangsan@jkweilai.com</td>
        <td>
          修改
          删除
        </td>
      </tr>
      <tr>
        <td>2</td>
        <td>李四</td>
        <td>女</td>
        <td>lisi@jkweilai.com</td>
        <td>
          修改
          删除
        </td>
      </tr>
    </tbody>
  </table>
</body>
</html>

```

### user_add.html

```html

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>新增用户</title>
  <link rel="stylesheet" href="user.css" type="text/css"></link>
</head>
<body>
  <h1>新增用户</h1>
  <form>
    <label>用户名:</label>
    <input type="text" name="username" required>

    <label>性别:</label>
    <select name="gender" required>
      <option value="">-- 请选择 --</option>
      <option value="1">男</option>
      <option value="0">女</option>
    </select>

    <label>邮箱:</label>
    <input type="email" name="email" required>

    <button type="submit">保存</button>
  </form>
</body>
</html>

```

### user_edit.html

```html

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>修改用户</title>
  <link rel="stylesheet" href="user.css" type="text/css"></link>
</head>
<body>
  <h1>修改用户</h1>
  <form>
    <label>用户名:</label>
    <input type="text" name="username" value="张三" required>

    <label>性别:</label>
    <select name="gender" required>
      <option value="">-- 请选择 --</option>
      <option value="1" selected>男</option>
      <option value="0">女</option>
    </select>

    <label>邮箱:</label>
    <input type="email" name="email" value="zhangsan@jkweilai.com" required>

    <button type="submit">修改</button>
  </form>
</body>
</html>

```

---

## SpringMVC环境搭建

### 创建module：usermgt

打包方式 `war`

### 引入相关依赖

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
    <!--lombok-->
    <dependency>
        <groupId>org.projectlombok</groupId>
        <artifactId>lombok</artifactId>
        <version>1.18.42</version>
    </dependency>
</dependencies>

```

### 添加web支持，配置web.xml文件

```xml

<?xml version="1.0" encoding="UTF-8"?>
<web-app xmlns="https://jakarta.ee/xml/ns/jakartaee"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="https://jakarta.ee/xml/ns/jakartaee https://jakarta.ee/xml/ns/jakartaee/web-app_6_0.xsd"
         version="6.0">

    <!--字符编码过滤器-->
    <filter>
        <filter-name>characterEncodingFilter</filter-name>
        <filter-class>org.springframework.web.filter.CharacterEncodingFilter</filter-class>
        <init-param>
            <param-name>encoding</param-name>
            <param-value>UTF-8</param-value>
        </init-param>
        <init-param>
            <param-name>forceRequestEncoding</param-name>
            <param-value>true</param-value>
        </init-param>
        <init-param>
            <param-name>forceResponseEncoding</param-name>
            <param-value>true</param-value>
        </init-param>
    </filter>
    <filter-mapping>
        <filter-name>characterEncodingFilter</filter-name>
        <url-pattern>/*</url-pattern>
    </filter-mapping>
    
    <!--HTTP请求方式过滤器-->
    <filter>
        <filter-name>hiddenHttpMethodFilter</filter-name>
        <filter-class>org.springframework.web.filter.HiddenHttpMethodFilter</filter-class>
    </filter>
    <filter-mapping>
        <filter-name>hiddenHttpMethodFilter</filter-name>
        <url-pattern>/*</url-pattern>
    </filter-mapping>
    
    <!--前端控制器-->
    <servlet>
        <servlet-name>springmvc</servlet-name>
        <servlet-class>org.springframework.web.servlet.DispatcherServlet</servlet-class>
        <init-param>
            <param-name>contextConfigLocation</param-name>
            <param-value>classpath:springmvc.xml</param-value>
        </init-param>
        <load-on-startup>1</load-on-startup>
    </servlet>
    <servlet-mapping>
        <servlet-name>springmvc</servlet-name>
        <url-pattern>/</url-pattern>
    </servlet-mapping>

</web-app>

```

注意两个过滤器Filter的配置顺序：

+ 先配置 CharacterEncodingFilter
+ 再配置 HiddenHttpMethodFilter

### 配置springmvc.xml文件

```xml

<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
       xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:mvc="http://www.springframework.org/schema/mvc"
       xmlns:context="http://www.springframework.org/schema/context"
       xsi:schemaLocation="http://www.springframework.org/schema/beans http://www.springframework.org/schema/beans/spring-beans.xsd http://www.springframework.org/schema/mvc https://www.springframework.org/schema/mvc/spring-mvc.xsd http://www.springframework.org/schema/context https://www.springframework.org/schema/context/spring-context.xsd">

    <!--组件扫描-->
    <context:component-scan base-package="com.jkweilai.usermgt.controller,com.jkweilai.usermgt.dao"/>

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

    <!--开启注解-->
    <mvc:annotation-driven/>

    <!--静态资源处理-->
    <!--告诉 Spring MVC 对于匹配特定 URL 模式的请求，直接从文件系统提供静态文件，而不需要经过控制器处理-->
    <mvc:resources mapping="/static/**" location="/static/" />

    <!--静态资源处理-->
    <!--Spring MVC 会将所有未匹配到 Controller 的请求，转发给 Web 容器（Tomcat）的默认 Servlet 处理，性能较低。-->
    <!--<mvc:default-servlet-handler/>-->

</beans>

```

在WEB-INF目录下新建：thymeleaf目录

创建package。

---

## 显示首页

在应用的根下新建目录：static，将user.css文件拷贝进去。

<img src="https://cdn.nlark.com/yuque/0/2024/png/21376908/1710922471241-f7ec47fc-9106-4d52-bd88-24b1005e99c6.png" width="303" title="" crop="0,0,1,1" id="u19a749a5" class="ne-image" style="font-size: 16px">

将user_index.html拷贝到WEB-INF/thymeleaf目录下：

<img src="https://cdn.nlark.com/yuque/0/2024/png/21376908/1710922711285-f6d7e3ea-ee9f-4b95-a454-0f1b41204a46.png" width="309" title="" crop="0,0,1,1" id="u413f67b2" class="ne-image" style="font-size: 16px">

代码有两处需要修改：

<img src="https://cdn.nlark.com/yuque/0/2024/png/21376908/1710922744668-a8863a20-0635-4c69-b461-a182949678d6.png" width="828" title="" crop="0,0,1,1" id="u16a044a8" class="ne-image" style="font-size: 16px">

重要：在springmvc.xml文件中配置视图控制器映射：

```xml

<!--视图控制器映射-->
<mvc:view-controller path="/" view-name="user_index"/>

```

部署，启动服务器，测试：

<img src="https://cdn.nlark.com/yuque/0/2024/png/21376908/1710922946129-cfb0cded-a7de-4b37-9f89-38b01b642655.png" width="1915" title="" crop="0,0,1,1" id="u63e0b047" class="ne-image" style="font-size: 16px">

---

## 实现用户列表

修改user_index.html中的超链接：

```html

<!DOCTYPE html>
<html lang="en" xmlns:th="http://www.thymeleaf.org">
<head>
  <meta charset="UTF-8">
  <title>用户管理系统</title>
  <link rel="stylesheet" th:href="@{/static/user.css}" type="text/css"></link>
</head>
<body>
  <div class="header">
    <h1>用户管理系统</h1>
  </div>
  <ul>
    <li><a class="active" th:href="@{/user}">用户列表</a></li>
  </ul>
</body>
</html>

```

编写 entity：User

```java

package com.jkweilai.usermgt.entity;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

@Data
@AllArgsConstructor
@NoArgsConstructor
public class User {
    private Long id;
    private String name;
    private String email;
    private Integer gender;
}

```

编写UserDao，提供selectAll方法：

```java

package com.jkweilai.usermgt.dao;

import com.jkweilai.usermgt.entity.User;
import org.springframework.stereotype.Repository;

import java.util.ArrayList;
import java.util.List;

@Repository
public class UserDao {
    private static List<User> users = new ArrayList<>();
    static {
        User user1 = new User(10001L, "张三", "zhangsan@jkweilai.com", 1);
        User user2 = new User(10002L, "李四", "lisi@jkweilai.com", 1);
        User user3 = new User(10003L, "王五", "wangwu@jkweilai.com", 1);
        User user4 = new User(10004L, "赵六", "zhaoliu@jkweilai.com", 0);
        User user5 = new User(10005L, "钱七", "qianqi@jkweilai.com", 0);
        users.add(user1);
        users.add(user2);
        users.add(user3);
        users.add(user4);
        users.add(user5);
    }

    public List<User> selectAll(){
        return users;
    }
}

```

编写控制器UserController：

```java

package com.jkweilai.usermgt.controller;

import com.jkweilai.usermgt.entity.User;
import com.jkweilai.usermgt.dao.UserDao;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;

import java.util.List;

@Controller
public class UserController {

    @Autowired
    private UserDao userDao;

    @GetMapping("/user")
    public String list(Model model){
        // 获取所有的用户
        List<User> users = userDao.selectAll();
        // 存储到request域
        model.addAttribute("users", users);
        // 跳转视图
        return "user_list";
    }
}

```

将user_list.html拷贝到thymeleaf目录下，并进行代码修改，显示用户列表：

```html

<!DOCTYPE html>
<html lang="en" xmlns:th="http://www.thymeleaf.org">
<head>
  <meta charset="UTF-8">
  <title>用户列表</title>
  <link rel="stylesheet" th:href="@{/static/user.css}" type="text/css"></link>
</head>
<body>
  <div class="header">
    <h1>用户列表</h1>
  </div>
  <div class="add-button-wrapper">
    <a class="add-button" href="user_add.html">新增用户</a>
  </div>
  <table>
    <thead>
      <tr>
        <th>编号</th>
        <th>用户名</th>
        <th>性别</th>
        <th>邮箱</th>
        <th>操作</th>
      </tr>
    </thead>
    <tbody>

      <tr th:each="user : ${users}">
        <td th:text="${user.id}"></td>
        <td th:text="${user.name}"></td>
        <td th:text="${user.gender == 1 ? '男' : '女'}"></td>
        <td th:text="${user.email}"></td>
        <td>
          <a href="">修改</a>
          <a href="">删除</a>
        </td>
      </tr>

    </tbody>
  </table>
</body>
</html>

```

---

## 实现新增功能

### 跳转到新增页面

在用户列表页面，修改`新增用户`的超链接：

<img src="https://cdn.nlark.com/yuque/0/2024/png/21376908/1710924492210-29f6afb3-551b-478e-adda-4b1952ba2971.png" width="690" title="" crop="0,0,1,1" id="u596104c4" class="ne-image" style="font-size: 16px">

将user_add.html拷贝到thymeleaf目录下，并进行代码修改如下：

```html

<!DOCTYPE html>
<html lang="en" xmlns:th="http:www.thymeleaf.org">
<head>
  <meta charset="UTF-8">
  <title>新增用户</title>
  <link rel="stylesheet" th:href="@{/static/user.css}" type="text/css"></link>
</head>
<body>
  <h1>新增用户</h1>
  <form>
    <label>用户名:</label>
    <input type="text" name="username" required>

    <label>性别:</label>
    <select name="gender" required>
      <option value="">-- 请选择 --</option>
      <option value="1">男</option>
      <option value="0">女</option>
    </select>

    <label>邮箱:</label>
    <input type="email" name="email" required>

    <button type="submit">保存</button>
  </form>
</body>
</html>

```

在springmvc.xml文件中配置`视图控制器映射`：

```xml

<mvc:view-controller path="/toSave" view-name="user_add"/>

```

启动服务器测试：

<img src="https://cdn.nlark.com/yuque/0/2024/png/21376908/1710924719699-451900a1-ead4-463f-8536-8db72ac56b0b.png" width="1589" title="" crop="0,0,1,1" id="u4c32fb33" class="ne-image" style="font-size: 16px">

### 实现新增功能

前端页面发送POST请求，提交表单，user_add.html代码如下：

```html

<!DOCTYPE html>
<html lang="en" xmlns:th="http:www.thymeleaf.org">
<head>
  <meta charset="UTF-8">
  <title>新增用户</title>
  <link rel="stylesheet" th:href="@{/static/user.css}" type="text/css"></link>
</head>
<body>
  <h1>新增用户</h1>
  <form th:action="@{/user}" method="post">
    <label>用户名:</label>
    <input type="text" name="name" required>

    <label>性别:</label>
    <select name="gender" required>
      <option value="">-- 请选择 --</option>
      <option value="1">男</option>
      <option value="0">女</option>
    </select>

    <label>邮箱:</label>
    <input type="email" name="email" required>

    <button type="submit">保存</button>
  </form>
</body>
</html>

```

编写控制器UserController：

```java

@PostMapping("/user")
public String save(User user){
    // 保存用户
    userDao.save(user);
    // 重定向到列表
    return "redirect:/user";
}

```

****注意：保存成功后，采用重定向的方式跳转到用户列表。****

编写UserDao：

```java

public static Long generateId(){
    // Stream API
    Long maxId = users.stream().map(user -> user.getId()).reduce((id1, id2) -> id1 > id2 ? id1 : id2).get();
    return maxId + 1;
}

public void save(User user){
    // 设置id
    user.setId(generateId());
    // 保存
    users.add(user);
}

```

****注意：单独写了一个方法生成id，内部使用了Stream API。****

---

## 跳转到修改页面

修改user_list.html中`修改`超链接：

```html

<a th:href="@{'/user/' + ${user.id}}">修改</a>

```

编写Controller：

```java

@GetMapping("/user/{id}")
public String toUpdate(@PathVariable("id") Long id, Model model){
    // 根据id查询用户信息
    User user = userDao.selectById(id);
    // 将对象存储到request域
    model.addAttribute("user", user);
    // 跳转视图
    return "user_edit";
}

```

编写UserDao：

```java

public User selectById(Long id){
    return users.stream().filter(user -> user.getId().equals(id)).findFirst().get();
}

```

将user_edit.html拷贝thymeleaf目录下，并修改代码如下：

```html

<!DOCTYPE html>
<html lang="en" xmlns:th="http://www.thymeleaf.org">
<head>
    <meta charset="UTF-8">
    <title>修改用户</title>
    <link rel="stylesheet" th:href="@{/static/user.css}" type="text/css"></link>
</head>
<body>
<h1>修改用户</h1>
<form th:object="${user}">
    <label>用户名:</label>
    <input type="text" name="username" th:value="*{name}" required>

    <label>性别:</label>
    <!--th:field会自动选中下拉列表的选项-->
    <select name="gender" th:field="*{gender}" required>
        <option value="">-- 请选择 --</option>
        <option value="1">男</option>
        <option value="0">女</option>
    </select>

    <label>邮箱:</label>
    <input type="email" name="email" th:value="*{email}" required>

    <button type="submit">修改</button>
</form>
</body>
</html>

```

---

## 实现修改功能

将user_edit.html页面中的form表单修改一下，添加action，添加method，隐藏域的方式提交请求方式put，隐藏域的方式提交id：

```html

<form th:action="@{/user}" method="post"  th:object="${user}">
  <!--隐藏域的方式设置请求方式为put请求-->
  <input type="hidden" name="_method" value="put">
  <!--隐藏域的方式提交id-->
  <input type="hidden" name="id" th:value="*{id}">

  <label>用户名:</label>
  <input type="text" name="name" th:value="*{name}" required>

  <label>性别:</label>
  <select name="gender" th:field="*{gender}" required>
    <option value="">-- 请选择 --</option>
    <option value="1">男</option>
    <option value="0">女</option>
  </select>

  <label>邮箱:</label>
  <input type="email" name="email" th:value="*{email}" required>

  <button type="submit">修改</button>
</form>

```

编写Controller：

```java

@PutMapping("/user")
public String modify(User user){
    // 更新数据
    userDao.update(user);
    // 重定向
    return "redirect:/user";
}

```

编写UserDao：

```java

public void update(User user){
    for (int i = 0; i < users.size(); i++) {
        if(user.getId().equals(users.get(i).getId())){
            users.set(i, user);
            break;
        }
    }
}

```

---

## 实现删除功能

删除应该发送DELETE请求，要模拟DELETE请求，就需要使用表单方式提交。因此我们点击`删除`超链接时需要采用表单方式提交。

在user_list.html页面添加form表单，并且点击超链接时应该提交表单，代码如下：

```html

<!DOCTYPE html>
<html lang="en" xmlns:th="http://www.thymeleaf.org">
<head>
  <meta charset="UTF-8">
  <title>用户列表</title>
  <link rel="stylesheet" th:href="@{/static/user.css}" type="text/css"></link>
</head>
<body>
  <div class="header">
    <h1>用户列表</h1>
  </div>
  <div class="add-button-wrapper">
    <a class="add-button" th:href="@{/toSave}">新增用户</a>
  </div>
  <table>
    <thead>
      <tr>
        <th>编号</th>
        <th>用户名</th>
        <th>性别</th>
        <th>邮箱</th>
        <th>操作</th>
      </tr>
    </thead>
    <tbody>

      <tr th:each="user : ${users}">
        <td th:text="${user.id}"></td>
        <td th:text="${user.name}"></td>
        <td th:text="${user.gender == 1 ? '男' : '女'}"></td>
        <td th:text="${user.email}"></td>
        <td>
          <a th:href="@{'/user/' + ${user.id}}">修改</a>
          <!--为删除提供一个鼠标单击事件-->
          <a th:href="@{'/user/' + ${user.id}}" onclick="del(event)">删除</a>
        </td>
      </tr>

    </tbody>
  </table>

  <!--为删除操作准备一个form表单，点击删除时提交form表单-->
  <div style="display: none">
  <form method="post" id="delForm">
    <input type="hidden" name="_method" value="delete"/>
  </form>
  </div>

  <script>
    function del(event){
      // 获取表单
      let delForm = document.getElementById("delForm");
      // 设置表单action
      delForm.action = event.target.href;
      if(window.confirm("您确定要删除吗？")){
        // 提交表单
        delForm.submit();
      }
      // 阻止超链接默认行为
      event.preventDefault();
    }
  </script>
</body>
</html>

```

编写Controller:

```java

@DeleteMapping("/user/{id}")
public String del(@PathVariable("id") Long id){
    // 删除
    userDao.deleteById(id);
    // 重定向
    return "redirect:/user";
}

```

编写UserDao:

```java

public void deleteById(Long id){
    for (int i = 0; i < users.size(); i++) {
        if(id.equals(users.get(i).getId())){
            users.remove(i);
            break;
        }
    }
}

```
