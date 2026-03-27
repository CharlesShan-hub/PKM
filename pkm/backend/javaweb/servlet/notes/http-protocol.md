# HTTP协议

---

## 什么是HTTP协议

**HTTP（HyperText Transfer Protocol，超文本传输协议）** 是一种用于分布式、协作式超媒体信息系统的应用层协议。它是万维网（WWW）数据通信的基础，基于**客户端-服务器模型**，通过请求-响应模式工作。  

**核心特点**：  

+ **无状态**：默认不保留之前的请求/响应信息（可通过Cookie/Session实现状态管理）。  
+ **基于TCP/IP**：默认端口80（HTTPS为443）。  
+ **灵活可扩展**：支持自定义头部、多种数据格式（JSON、XML等）。

**HTTP 协议版本：**

+ HTTP/1.0：短连接。**每次浏览器向服务器发起一个请求，都会建立一个全新的 TCP 连接。**
+ HTTP/1.1：持久连接。**浏览器和服务器建立一次 TCP 连接后，可以在这个连接上连续进行多次请求和响应。**

**HTTP1.1 连接是可复用的：**

+ 对同一域名的请求，可以复用同一个连接
+ 例如有这样一个网页：**在 HTTP/1.1 时代，浏览器通常为每个域名开启******6******个左右的并行连接，以下页面在加载的时候就会有连接复用的情况。（底层弄了个 TCP 连接池，连接池最高支持 6 个 TCP 连接并发，下面这个 HTML 页面需要 9 个 TCP 连接，1 个加载 HTML，8 个加载图片。因此有连接复用的情况）**

```html
<body>
  <img src="http://localhost:8080/app/1.jpg">
  <img src="http://localhost:8080/app/2.jpg">
  <img src="http://localhost:8080/app/3.jpg">
  <img src="http://localhost:8080/app/4.jpg">
  <img src="http://localhost:8080/app/5.jpg">
  <img src="http://localhost:8080/app/6.jpg">
  <img src="http://localhost:8080/app/7.jpg">
  <img src="http://localhost:8080/app/8.jpg">
</body>
```

****HTTP/1.1 是有状态的吗？****

+ 无状态。尽管从 1.0 的短连接升级成了 1.1 的持久连接，但 HTTP 协议仍然是无状态的。无状态主要体现在：默认不保留之前的请求/响应信息。

---

## HTTP请求报文详解

HTTP请求报文由以下部分组成：  

```http
GET /index.html HTTP/1.1          # 请求行（方法 + URI + 协议版本）
Host: www.example.com             # 请求头部（键值对）
User-Agent: Mozilla/5.0          
Accept: text/html,application/xhtml+xml
Accept-Language: en-US           
Connection: keep-alive
Content-Type: application/x-www-form-urlencoded
Cookie: sessionId=abc123; userId=admin
                                  # 空行（分隔头部和体）
name=John&age=30                  # 请求体（GET通常无体，POST/PUT等有）
```

**关键字段说明**：  

+ **请求行**：  
    - **方法**：GET（获取资源）、POST（提交数据）、PUT（更新）、DELETE（删除）等。  
    - **URI**：请求的资源路径（如`/index.html`）。  
    - **协议版本**：HTTP/1.1 或 HTTP/2。
+ **请求头部**：  
    - `Host`：目标服务器域名（必填）。  
    - `User-Agent`：客户端标识（如浏览器类型）。  
    - `Content-Type`：请求体的数据类型（`application/x-www-form-urlencoded`表示普通表单提交，`application/json`表示以 JSON 格式提交数据）。  
    - `Cookie`：客户端携带的会话信息。
+ **请求体**：仅POST/PUT等方法携带数据（如表单、JSON）。

---

## HTTP响应报文详解

HTTP响应报文结构：  

```http
HTTP/1.1 200 OK                  # 状态行（协议版本 + 状态码 + 描述）
Server: nginx/1.18.0             # 响应头部
Date: Mon, 01 Jun 2025 12:00:00 GMT
Content-Type: text/html; charset=UTF-8          
Content-Length: 1234             
Connection: keep-alive          
Set-Cookie: session_id=abc123; HttpOnly; SameSite=Strict
                                 # 空行
<!DOCTYPE html>                  # 响应体（实际数据）
<html>...</html>
```

**关键字段说明**：  

+ **状态行**：  
    - **状态码**：  
        * `****200 OK****`****：成功。****
        * `****404 Not Found****`****：资源不存在。****
        * `****405****`****：请求方式和服务器端的处理方式不一致。（例如：前端请求方式为 POST，服务器端处理方式是 GET，则发生 405 错误。）****
        * `****500 Internal Server Error****`****：服务器错误。****
+ **响应头部**：  
    - `Content-Type`：响应体类型（如`text/html`、`application/json`）。  
    - `Content-Length`：响应体大小（字节）。  
    - `Set-Cookie`：服务器设置的会话标识。【HttpOnly设置在浏览器不能使用 document.cookie 读取，防止 XSS 攻击。 SameSite=Lax允许部分安全的跨站请求（如导航链接），SameSite=Strict最严格，完全禁止在跨站请求中发送Cookie】
+ **响应体**：返回的实际数据（HTML、JSON等）。

---

## GET与POST的区别及选择

### 区别

| **特性** | **GET请求** | **POST请求** |
| --- | --- | --- |
| **数据位置** | URL查询参数（如`?name=John`） | 请求体中（不可见） |
| **数据长度限制** | 受URL长度限制（约2048字符） | 无限制（服务器可配置） |
| **安全性** | 参数暴露在URL，不适合敏感数据 | 相对更安全（HTTPS下加密） |
| **幂等性** | 幂等（多次请求结果相同） | 非幂等（可能修改数据） |
| **缓存** | 可被缓存 | 默认不缓存 |
| **浏览器历史记录** | 保留参数 | 不保留 |

**幂等性 **就是：同一个操作，你执行1次和执行N次，结果都一样。

**幂等 **操作：**你按电梯的“关门”按钮，按1次和疯狂按10次，效果都一样——门只会关一次。**

****非幂等******操作：你喝奶茶，每点一次“加珍珠”按钮，杯子里就多一份珍珠（点10次就爆炸了）。**

****提示：GET 和 POST 请求提交数据时的格式都是****`****name=value&name=value&name=value...****`****。只是提交数据的位置不同，GET 在请求行上提交数据。POST 在请求体中提交数据。****

### 如何选择

+ **用GET**：  
    - 获取数据（如搜索、页面加载）。  
    - 参数简单且非敏感（如分页`?page=2`）。
+ **用POST**：  
    - 提交敏感数据（如登录表单、支付信息）。  
    - 上传文件或大量数据（如JSON body）。  
    - 修改服务器状态（如创建/更新资源）。

### 怎么发送 POST 请求

到目前为止，浏览器向服务器发送请求时，我们所掌握的所有的方式包括：

1. 用户在浏览器地址栏上直接输入 URL
2. 用户点击超链接
3. 使用 window.location.href 或 document.location.href
4. 使用 window.open
5. 用户提交 form 表单

以上所有的方式中，只有当使用 `form`表单提交数据，并且 `form`标签的 `method`属性设置为 `post`时，才是 `POST`请求，其它都是 `GET` 请求。

---

## URL编码

URL编码（也称为百分号编码）是HTTP协议和Web开发中一个非常重要的概念，特别是在Servlet开发中。

不过大家不需要担心，大部分的请求发送都已经自动对 URL 进行了编码，只有少数情况需要手动编码。（例如：自己通过代码进行重定向的时候，重定向的 URL 中含有特殊符号就需要手动编码。）

### URL编码的作用

URL编码主要用于：

1. **解决特殊字符问题**：URL中某些字符有特殊含义（如?、&、/等），当这些字符需要作为普通字符使用时必须编码
2. **支持非ASCII字符**：URL只能使用ASCII字符集，非ASCII字符（如中文）必须编码
3. **确保数据完整性**：防止数据在传输过程中被错误解析

### 在Servlet中的主要应用场景

1. **查询字符串(Query String)**：

```java
// 例如：name=张三&age=20 需要编码为 name=%E5%BC%A0%E4%B8%89&age=20
String encodedName = URLEncoder.encode("张三", "UTF-8");
```

2. **表单提交**：
    - GET方法：参数会自动进行URL编码
    - POST方法：取决于enctype属性，application/x-www-form-urlencoded会进行编码
3. **重定向(Redirect)**：

```java
String redirectUrl = "/search?q=" + URLEncoder.encode(userInput, "UTF-8");
response.sendRedirect(redirectUrl);
```

4. **Cookie值**：Cookie的值也需要进行URL编码（对 cookie 的 value 进行编码。cookie 由 name 和 value 组成。）

### 重要性

URL编码**非常重要**，因为：

+ 不正确的编码会导致数据损坏或安全漏洞（如XSS攻击）
+ 是Web开发的基础知识，几乎所有涉及URL参数传递的场景都需要考虑
+ 现代框架虽然大多自动处理，但理解原理对调试和解决特殊问题很有帮助

### Java中的相关API

+ **编码**：`java.net.URLEncoder.encode(String s, String enc)`
+ **解码**：`java.net.URLDecoder.decode(String s, String enc)`
+ Servlet容器通常会自动解码请求参数

### 示例

```java
// 编码示例
String original = "搜索 关键词&特殊字符";
String encoded = URLEncoder.encode(original, "UTF-8");
// 结果为 "搜索+关键词%26特殊字符"

// 解码示例
String decoded = URLDecoder.decode(encoded, "UTF-8");
```

理解URL编码对于开发安全、健壮的Web应用至关重要，是Servlet开发的基础知识之一。
