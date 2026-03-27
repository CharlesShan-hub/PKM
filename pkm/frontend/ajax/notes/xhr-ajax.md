# **XHR 实现 AJAX**

---

## XMLHttpRequest 概述

1. **浏览器原生 API，1999 年 IE5 引入。**
2. **XMLHttpRequest对象是传统 AJAX 的核心对象，通过它可以发送请求以及接收服务器数据的返回。**
3. **XMLHttpRequest对象，现代浏览器都是支持的，都内置了该对象。直接用即可。**
4. **创建XMLHttpRequest对象**

```javascript
const xhr = new XMLHttpRequest();
```

---

## **XMLHttpRequest对象的方法**

| ****方法**** | ****描述**** |
| --- | --- |
| **abort()** | **取消当前请求** |
| **getAllResponseHeaders()** | **返回头部信息** |
| **getResponseHeader()** | **返回特定的头部信息** |
| ****open(****_****method****_****,****_****url****_****,****_****async****_****,****_****user****_****,****_****psw****_****)**** | **method：请求类型 GET 或 POST**<br/>**url：请求路径**<br/>**async：true（异步）或 false（同步）**<br/>**user：可选的用户名称**<br/>**psw：可选的密码** |
| ****send()**** | **发送请求，适合 GET 请求。** |
| ****send(****_****string****_****)**** | **发送请求，并携带数据，适合 POST 请求，数据将在请求体当中发送。** |
| ****setRequestHeader()**** | **设置请求头** |

---

## **XMLHttpRequest对象的属性**

| ****属性**** | ****描述**** |
| --- | --- |
| onreadystatechange | **定义当 readyState 属性发生变化时被调用的函数** |
| ****onload**** | **请求成功完成时触发。但这个响应的结果可能是 200，可能是 404，也可能是 500 等。只要这一次请求完整的结束了，不管报错不报错，onload 会触发。** |
| ****onerror**** | **onerror 只在网络层面的请求失败时触发（如无法连接服务器、DNS解析失败、CORS错误等），而不会在HTTP状态码错误（如404、500）时触发。** |
| ontimeout | **请求超时时触发，需要先设置超时时间：xhr.timeout = 5000; // 5 秒超时**<br/>**超时后请求会自动终止，触发ontimeout后不会再触发onload或onerror** |
| readyState | **保存 XMLHttpRequest 的状态：**<br/>**0：请求未初始化**<br/>**1：服务器连接已建立**<br/>**2：请求已收到**<br/>**3：正在处理请求**<br/>**4：请求已完成且响应已就绪** |
| ****responseText**** | **以字符串返回响应数据** |
| responseXML | **以 XML 数据返回响应数据** |
| ****status**** | **返回请求的状态号**<br/>**200: "OK"**<br/>**403: "Forbidden"**<br/>**404: "Not Found"**<br/>**500："服务器内部错误"** |
| **statusText** | **返回状态文本（比如 "OK" 或 "Not Found"）** |

关于 `XMLHttpRequest`对象的使用，可参考官方文档：[**MDN Web Docs**](https://developer.mozilla.org/en-US/docs/Web/API/XMLHttpRequest)

---

## **XHR 发送 GET 请求**

功能描述：用户在注册页面上输入用户名 ，失去焦点后发送 AJAX 请求，验证用户名是否可用。

### 准备页面

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>用户名验证</title>
    <style>
        body {
            font-family: 'Roboto', 'Microsoft YaHei', sans-serif;
            background-color: #f5f5f5;
            margin: 0;
            padding: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            color: #333;
        }

        .container {
            background-color: white;
            border-radius: 10px;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
            padding: 30px;
            width: 100%;
            max-width: 400px;
            transition: all 0.3s ease;
        }

        h1 {
            text-align: center;
            color: #2c3e50;
            margin-bottom: 30px;
        }

        .form-group {
            margin-bottom: 20px;
        }

        label {
            display: block;
            margin-bottom: 8px;
            font-weight: 500;
            color: #2c3e50;
        }

        input[type="text"] {
            width: 100%;
            padding: 12px 15px;
            border: 1px solid #ddd;
            border-radius: 6px;
            font-size: 16px;
            transition: border 0.3s, box-shadow 0.3s;
            box-sizing: border-box;
        }

        input[type="text"]:focus {
            border-color: #3498db;
            box-shadow: 0 0 0 3px rgba(52, 152, 219, 0.2);
            outline: none;
        }

        .feedback {
            margin-top: 8px;
            padding: 10px;
            border-radius: 4px;
            font-size: 14px;
            opacity: 0;
            transition: opacity 0.3s ease;
        }

        .feedback.show {
            opacity: 1;
        }

        .feedback.success {
            background-color: #d4edda;
            color: #155724;
        }

        .feedback.error {
            background-color: #f8d7da;
            color: #721c24;
        }

        .loading {
            color: #17a2b8;
            display: flex;
            align-items: center;
        }

        .loading::after {
            content: "";
            display: inline-block;
            width: 16px;
            height: 16px;
            margin-left: 8px;
            border: 2px solid #17a2b8;
            border-radius: 50%;
            border-top-color: transparent;
            animation: spin 0.8s linear infinite;
        }

        @keyframes spin {
            to { transform: rotate(360deg); }
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>用户注册</h1>
        <div class="form-group">
            <label for="username">用户名：</label>
            <input type="text" id="username" name="username" placeholder="请输入用户名" autocomplete="off">
            <div id="username-feedback" class="feedback"></div>
        </div>
    </div>

    <script>
        document.addEventListener('DOMContentLoaded', function() {
            const usernameInput = document.getElementById('username');
            const feedbackElement = document.getElementById('username-feedback');
            
            // 模拟已存在的用户名数据库
            const existingUsernames = ['admin', 'test', 'user', 'guest', 'demo'];
            
            usernameInput.addEventListener('blur', function() {
                const username = usernameInput.value.trim();
                
                if (!username) {
                    return; // 如果用户名为空，不做任何操作
                }
                
                // 显示加载状态
                showLoading();
                
                // 模拟网络请求延迟
                setTimeout(() => {
                    // 模拟服务器响应 - 检查用户名是否已存在
                    if (existingUsernames.includes(username.toLowerCase())) {
                        showFeedback('error', '您的名字太受欢迎，需要重新填写。');
                    } else {
                        showFeedback('success', '恭喜你，您的用户名可用。');
                    }
                }, 800); // 800毫秒延迟模拟网络请求
            });
            
            function showLoading() {
                feedbackElement.textContent = '正在检查用户名...';
                feedbackElement.className = 'feedback loading show';
            }
            
            function showFeedback(type, message) {
                feedbackElement.textContent = message;
                feedbackElement.className = `feedback ${type} show`;
            }
            
            // 输入时隐藏反馈信息
            usernameInput.addEventListener('input', function() {
                feedbackElement.className = 'feedback';
            });
        });
    </script>
</body>
</html>
```

页面效果如下：

![](https://cdn.nlark.com/yuque/0/2025/png/21376908/1750209811297-4cbeb3cc-71a9-4672-9425-cd20dda9027a.png)

![](https://cdn.nlark.com/yuque/0/2025/png/21376908/1750209825223-5a0189f6-3d34-4482-ab3b-d0ee0e8fa7e2.png)

### 准备数据库表

创建 `t_user`表，准备几条数据：

```sql
SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

DROP TABLE IF EXISTS `t_user`;
CREATE TABLE `t_user`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `username` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 3 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

INSERT INTO `t_user` VALUES (1, 'admin');
INSERT INTO `t_user` VALUES (2, 'test');

SET FOREIGN_KEY_CHECKS = 1;
```

![](https://cdn.nlark.com/yuque/0/2025/png/21376908/1750211064304-5655b731-2f8c-4aad-b431-b73e85e8ab31.png)

### 编写后端 Servlet

编写后端 Servlet 程序，连接数据库，验证用户名是否存在，如果存在表示用户名不可用返回：`{"success":false}`，如果不存在表示用户名可用返回：`{"success":true}`

这里为了快速开发，没有使用三层架构，直接将所有代码编写到 Servlet 中了：

```java
package com.jkweilai.ajax.servlet;

import jakarta.servlet.ServletException;
import jakarta.servlet.annotation.WebServlet;
import jakarta.servlet.http.HttpServlet;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

import java.io.IOException;
import java.sql.*;

@WebServlet("/check")
public class CheckUsernameServlet extends HttpServlet {
    @Override
    protected void service(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        // 获取用户名
        String username = request.getParameter("username");
        // 连接数据库验证用户名是否可用
        Connection conn = null;
        PreparedStatement ps = null;
        ResultSet rs = null;
        boolean success = true;
        try {
            Class.forName("com.mysql.cj.jdbc.Driver");
            conn = DriverManager.getConnection("jdbc:mysql://localhost:3306/ajax", "root", "123456");
            String sql = "select * from t_user where username = ?";
            ps = conn.prepareStatement(sql);
            ps.setString(1, username);
            rs = ps.executeQuery();
            if (rs.next()) {
                success = false;
            }
        } catch (Exception e) {
            throw new RuntimeException(e);
        } finally {
            if (rs != null) {
                try {
                    rs.close();
                } catch (SQLException e) {
                    throw new RuntimeException(e);
                }
            }
            if (ps != null) {
                try {
                    ps.close();
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
        // 响应
        // 设置响应的内容类型以及响应时采用的字符编码方式
        response.setContentType("application/json;charset=UTF-8");
        response.getWriter().print("{\"success\" : " + success + "}");
    }
}
```

编写完后端程序之后，测试后端接口是否正常。

### 发送 GET 请求

将之前编写的页面中的以下代码注释掉：

![](https://cdn.nlark.com/yuque/0/2025/png/21376908/1750212594949-3986de9c-0e66-45a2-8b24-81efbf3836d2.png)

然后在注释掉的代码位置上编写使用 xhr 发送 ajax get 请求的代码，如下：

```javascript
// 1. 创建xhr对象
const xhr = new XMLHttpRequest();
// 2. 开启通道
xhr.open('GET', `check?username=${encodeURIComponent(username)}&_=${Date.now()}`, true);
// 3. 注册回调函数
xhr.onload = function(){
    if(xhr.status >= 200 && xhr.status < 300){
        try{
            const result = JSON.parse(xhr.responseText);
            if(result.success){
                showFeedback('success', '恭喜你，您的用户名可用。');
            }else{
                showFeedback('error', '您的名字太受欢迎，需要重新填写。');
            }
        }catch(e){
            showFeedback('error', '解析响应时出错，请重试。');
        }
    }else{
        showFeedback("error", "请求失败，请稍后重试。");
    }
}
xhr.onerror = function(){
    showFeedback("error", "网络错误，请检查您的连接。");
}
// 4. 发送请求
xhr.send();
```

注意：

1. 以上代码中的 `encodeURIComponent`是对提交的数据进行编码，防止 GET 请求提交的数据乱码问题。（比如表单提交数据的时候采用 GET 请求，提交的数据是：`**张三%/**`  此时这个函数就起作用了。）
2. 以上代码中 `Date.now()`是给 URL 后面添加时间戳，解决 GET 请求缓存问题。（旧版浏览器可能存在 GET 缓存问题。）

---

## XHR 发送 POST 请求

和 GET 请求的代码区别在于：

1. 需要设置请求头的内容类型。模拟表单提交数据。
2. 请求数据编写在 send 方法的参数上，模拟在请求体中提交数据。

代码如下：

```javascript
// 1. 创建xhr对象
const xhr = new XMLHttpRequest();
// 2. 开启通道
xhr.open('POST', 'check', true);
// 3. 注册回调函数
xhr.onload = function(){
  if(xhr.status >= 200 && xhr.status < 300){
    try{
      const result = JSON.parse(xhr.responseText);
      if(result.success){
        showFeedback('success', '恭喜你，您的用户名可用。');
      }else{
        showFeedback('error', '您的名字太受欢迎，需要重新填写。');
      }
    }catch(e){
      showFeedback('error', '解析响应时出错，请重试。');
    }
  }else{
    showFeedback("error", "请求失败，请稍后重试。");
  }
}
xhr.onerror = function(){
  showFeedback("error", "网络错误，请检查您的连接。");
}
// 4. 发送请求
// 设置请求头内容类型（模拟form表单提交数据）以及采用哪一种字符编码方式。必须放在open方法后面。
xhr.setRequestHeader("Content-type", "application/x-www-form-urlencoded; charset=UTF-8");
// 在请求体中提交数据
xhr.send(`username=${encodeURIComponent(username)}`);
```
