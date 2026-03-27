# **AJAX跨域问题**

---

## 跨域

+ **跨域是指从一个域名的网页去请求另一个域名的资源。比如从百度(https://baidu.com)页面去请求京东(**https://www.jd.com**)的资源。**
+ **通过超链接或者form表单提交或者window.location.href的方式进行跨域是不存在问题的（******大家可以编写程序测试一下******）。但在一个域名的网页中的一段js代码发送ajax请求去访问另一个域名中的资源，由于同源策略的存在导致无法跨域访问，那么ajax就存在这种跨域问题。**
+ **同源策略是指一段脚本只能读取来自同一来源的窗口和文档的属性（例如： A 站点的一段 JS 脚本去读取 B 站点的 Cookie，这是不允许的，这就是同源策略在起作用），****同源就是协议、域名和端口都相同。**
+ **有一些情况下，我们是需要使用ajax进行跨域访问的。比如某公司的A页面(a.domain.com)有可能需要获取B页面(b.domain.com)。**

---

## **同源还是不同源**

+ 区分同源和不同源的三要素
    - 协议
    - 域名
    - 端口
+ 协议一致，域名一致，端口号一致，三个要素都一致，才是同源，其它一律都是不同源

| **URL1** | ** URL2** | **是否同源** | 描述 |
| --- | --- | --- | --- |
| http://localhost:8080/a/index.html | http://localhost:8080/a/first | 同源 | 协议 域名 端口一致 |
| http://localhost:8080/a/index.html | http://localhost:8080/b/first | 同源 | 协议 域名 端口一致 |
| http://www.myweb.com:8080/a.js | https://www.myweb.com:8080/b.js | 不同源 | 协议不同 |
| http://www.myweb.com:8080/a.js | http://www.myweb.com:8081/b.js | 不同源 | 端口不同 |
| http://www.myweb.com/a.js | http://www.myweb2.com/b.js | 不同源 | 域名不同 |
| http://www.myweb.com/a.js | http://crm.myweb.com/b.js | 不同源 | 子域名不同 |

---

## 复现AJAX跨域问题

+ 部署两个tomcat服务器，1号服务器和2号服务器，两个服务器设置的端口不同，1号服务器如下所示：

![](https://cdn.nlark.com/yuque/0/2022/png/21376908/1654049493291-95fc4c8c-881b-477e-83c9-5506c4488297.png)

+ 2号服务器如下所示，注意端口是不同的：

![](https://cdn.nlark.com/yuque/0/2022/png/21376908/1654049601618-483007b4-8493-45e5-b27b-c5812c7d14d8.png)

+ 访问两台服务器的地址如下：
    - 1号服务器：http://localhost:8080
    - 2号服务器：http://localhost:8081
+ 提供两个webapp，一个是a应用，一个是b应用。将来a应用部署到1号服务器上。b应用部署到2号服务器上。
+ a应用的前端代码如下：

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>a应用发送ajax请求，访问b应用的servlet</title>
</head>
<body>
<script type="text/javascript">
    window.onload = function(){
        document.getElementById("btn").onclick = function (){
            // 1.创建ajax核心对象
            let xmlHttpRequest = new XMLHttpRequest();
            // 2.注册回调函数
            xmlHttpRequest.onreadystatechange = function (){
                // 我们只是为了测试ajax请求默认情况下是否可以跨域，所以这里不需要写代码，只要保证请求发过去即可。
            }
            // 3.打开通道（这一步重的请求路径很关键）
            xmlHttpRequest.open("GET", "http://localhost:8081/b/hello", true)
            // 4.发送请求
            xmlHttpRequest.send()
        }
    }
</script>
<button id="btn">a应用发送ajax请求，访问b应用的servlet</button>
</body>
</html>
```

+ b应用的后端代码如下：

```java
import jakarta.servlet.ServletException;
import jakarta.servlet.annotation.WebServlet;
import jakarta.servlet.http.HttpServlet;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

import java.io.IOException;

@WebServlet("/hello")
public class HelloServlet extends HttpServlet {
    @Override
    protected void doGet(HttpServletRequest req, HttpServletResponse resp) 
            throws ServletException, IOException {
        System.out.println("hello servlet");
    }
}
```

+ a应用部署到1号服务器，b应用部署到2号服务器，将1号和2号服务器都启动。
+ 服务器启动成功后，打开浏览器，在地址栏上输入请求地址：http://localhost:8080/a/index.html

![](https://cdn.nlark.com/yuque/0/2022/png/21376908/1655278866144-5cdc939d-369b-4970-9e12-b52bbe9ec3c4.png)

+ F12，打开谷歌浏览器的控制台窗口，然后点击上图中的按钮，发送ajax请求，结果如下图：

![](https://cdn.nlark.com/yuque/0/2022/png/21376908/1655278984925-ead6c98a-dfad-45cf-83d4-4b0556283612.png)

报错了，错误信息中描述了：从 `http://localhost:8080` 上访问 `http://localhost:8081/b/hello` 被同源策略阻止：请求的资源上不存在“Access Control Allow Origin”标头。这就是ajax跨域问题。

---

## AJAX跨域解决方案

### 方案一：后端 CORS（生产/开发）

（核心原理：被访问的资源允许你跨域访问时才可以访问。）

+ a站点客户端代码：

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>a应用发送ajax请求，访问b应用的servlet</title>
</head>
<body>
<script src="https://cdn.bootcdn.net/ajax/libs/axios/1.6.7/axios.min.js"></script>
<script>
    document.addEventListener("DOMContentLoaded", function (){
        document.getElementById("btn").addEventListener("click", async function (){
            let response = await axios.get("http://localhost:8081/b/hello");
            document.getElementById("mydiv").innerHTML = response.data;
        });
    });
</script>
<button id="btn">a应用发送ajax请求，访问b应用的servlet</button>
<div id="mydiv"></div>
</body>
</html>
```

+ b站点服务端代码：

```java
import jakarta.servlet.ServletException;
import jakarta.servlet.annotation.WebServlet;
import jakarta.servlet.http.HttpServlet;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

import java.io.IOException;
import java.io.PrintWriter;

@WebServlet("/hello")
public class HelloServlet extends HttpServlet {
    @Override
    protected void doGet(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        // 设置响应头：以下这是表示该资源任何人都能用
        response.setHeader("Access-Control-Allow-Origin", "*");
        // 设置相应内容类型
        response.setContentType("text/html;charset=UTF-8");
        PrintWriter out = response.getWriter();
        out.print("<h1>hello ajax!!</h1>");
    }
}
```

+ 将a应用部署到1号服务器，将b应用部署到2号服务器，将两台服务器都启动起来，打开浏览器，输入地址：http://localhost:8080/a/index.html，如下图：

![](https://cdn.nlark.com/yuque/0/2022/png/21376908/1655283835672-ba311028-ae93-4ca1-9291-0bc9e4c1ed32.png)

+ 点击上图的按钮，发送ajax请求，结果如下图所示：

![](https://cdn.nlark.com/yuque/0/2022/png/21376908/1655284013139-78c8c9d5-7b9f-4bc0-bb09-dd498fe91091.png)

**对于 SpringBoot 项目来说可以做以下的全局配置**：

```java
@Configuration
public class CorsConfig implements WebMvcConfigurer {
    @Override
    public void addCorsMappings(CorsRegistry registry) {
        registry.addMapping("/**")
                .allowedOrigins("https://your-frontend.com")
                .allowedMethods("GET", "POST", "PUT", "DELETE");
    }
}
```

### 方案二：后端 HttpClient 代理（生产/开发）

这种方式主要是通过后端java程序来完成跨域访问。因为跨域的限制只针对XMLHttpRequest对象，java程序是可以跨域访问的，原理如下图：

![](https://cdn.nlark.com/yuque/0/2022/png/21376908/1655476145124-153a35c4-f336-4342-a35f-d4e90fb122a9.png)

****核心原理：a站点中的按钮无法直接发送ajax请求访问b站点中的TargetServlet，但是可以发送ajax请求访问当前站点中的ProxyServlet，将它当作一个代理，然后通过代理发送get/post请求访问b站点中的TargetServlet。****

通过 Java 程序发送 get 或 post 请求可以使用 jdk 内置的 api（java.net.URLConnection，java.net.URL等类库），也可以使用 Apache 的 httpclient 开源组件完成。

这里着重看一下 httpclient 如何发送 get 或 post 请求。

首选需要引入 httpclient 的 jar 包：

![](https://cdn.nlark.com/yuque/0/2025/png/21376908/1750401194695-8febc260-5a0a-418f-bd3e-d4c32d842c4f.png)

使用 httpclient 发送 get 请求：

```java
package com.jkweilai.httpclient;

import org.apache.http.HttpEntity;
import org.apache.http.client.methods.CloseableHttpResponse;
import org.apache.http.client.methods.HttpGet;
import org.apache.http.client.utils.URIBuilder;
import org.apache.http.impl.client.CloseableHttpClient;
import org.apache.http.impl.client.HttpClients;
import org.apache.http.util.EntityUtils;

import java.io.IOException;
import java.net.URI;
import java.net.URISyntaxException;

public class HttpClientGetWithParams {
    public static void main(String[] args) {
        try (CloseableHttpClient httpClient = HttpClients.createDefault()) {
            // 使用URIBuilder构建带参数的URL
            URI uri = new URIBuilder("https://example.com/api/search").addParameter("q", "httpclient").addParameter("page", "1").addParameter("size", "10").build();

            HttpGet httpGet = new HttpGet(uri);

            try (CloseableHttpResponse response = httpClient.execute(httpGet)) {
                System.out.println("Status Code: " + response.getStatusLine().getStatusCode());

                HttpEntity entity = response.getEntity();
                if (entity != null) {
                    System.out.println("Response: " + EntityUtils.toString(entity));
                    EntityUtils.consume(entity);
                }
            }
        } catch (IOException | URISyntaxException e) {
            throw new RuntimeException(e);
        }
    }
}
```

使用 httpclient 发送 post 请求：

```java
package com.jkweilai.httpclient;

import org.apache.http.HttpEntity;
import org.apache.http.NameValuePair;
import org.apache.http.client.entity.UrlEncodedFormEntity;
import org.apache.http.client.methods.CloseableHttpResponse;
import org.apache.http.client.methods.HttpPost;
import org.apache.http.impl.client.CloseableHttpClient;
import org.apache.http.impl.client.HttpClients;
import org.apache.http.message.BasicNameValuePair;
import org.apache.http.util.EntityUtils;

import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

public class HttpClientPostForm {
    public static void main(String[] args) {
        try (CloseableHttpClient httpClient = HttpClients.createDefault()) {
            HttpPost httpPost = new HttpPost("https://example.com/api/login");

            // 设置表单数据
            List<NameValuePair> params = new ArrayList<>();
            params.add(new BasicNameValuePair("username", "user123"));
            params.add(new BasicNameValuePair("password", "pass123"));

            httpPost.setEntity(new UrlEncodedFormEntity(params));

            try (CloseableHttpResponse response = httpClient.execute(httpPost)) {
                System.out.println("Status Code: " + response.getStatusLine().getStatusCode());

                HttpEntity entity = response.getEntity();
                if (entity != null) {
                    System.out.println("Response: " + EntityUtils.toString(entity));
                    EntityUtils.consume(entity);
                }
            }
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }
}
```

### 方案三：****Nginx 反向代理（生产）****

****原理******：通过 Nginx 将前端和后端请求统一转发到同源域名下。（******和 HttpClient 是完全一样的思想。******）**  
****配置示例******：**

```nginx
server {
    listen 80;
    server_name your-domain.com;

    location /api {
        proxy_pass http://backend-server.com;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }

    location / {
        root /path/to/frontend;
        try_files $uri /index.html;
    }
}
```

****优点******：隐藏后端地址，统一入口，避免跨域问题。**

### **方案四：开发环境代理（开发）**

这是通过前端构建工具（如 Vite 或 Webpack）的开发服务器实现的 本地请求转发，****仅在开发阶段生效****，与生产环境的 Nginx/CORS 是分离的。

****Vite 项目（****`****vite.config.js****`****）****

```javascript
export default defineConfig({
  server: {
    proxy: {
      '/api': {
        target: 'http://backend-server.com', // 后端真实地址
        changeOrigin: true,                  // 修改请求头中的 Origin
        rewrite: path => path.replace(/^\/api/, '') // 路径重写
      }
    }
  }
})
```

前端项目运行在前端服务器中（我们叫做 Vite 开发服务器），前端服务器的代理过程如下：

```plain
浏览器请求: http://localhost:3000/api/users
↓
Vite开发服务器拦截到 /api 请求
↓
转发到: http://backend-server.com/users  (去掉/api)
↓
后端返回数据给Vite
↓
Vite把数据返回给浏览器
```

**几种方案的对比：**

| ****方案**** | ****适用环境**** | ****配置位置**** | ****是否需要后端配合**** |
| --- | --- | --- | --- |
| **Vue 配置文件代理** | **开发环境** | **前端构建工具配置** | **否** |
| **Nginx 反向代理（******如果项目最终部署不使用 Nginx，可以使用 Spring Cloud Gateway 来完成******）** | **生产环境** | **服务器配置文件** | **否** |
| **后端 CORS** | **生产/开发** | **后端代码** | **是** |
| **后端 HttpClient 代理** | **生产/开发** | **后端代码** | **是** |
