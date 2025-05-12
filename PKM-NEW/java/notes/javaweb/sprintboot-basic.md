# Web基础知识

## SpringBoot Web入门

写一个Controller类
```java
package com.charles.server;  
  
import org.springframework.web.bind.annotation.RequestMapping;  
import org.springframework.web.bind.annotation.RestController;  
  
@RestController  
public class HelloController {  
    @RequestMapping("/hello")  
    public String hello(String name) {  
        System.out.println("HelloController.hello()");  
        return "Hello " + name;  
    }
}
```

然后在浏览器访问：http://localhost:8081/hello?name=heima，就会返回 Hello heima

指定接口的方法： https://www.cnblogs.com/baby123/p/11381171.html

## HTTP协议

1. 不需要手动去解析HTTP协议，SpringBoot已经帮我们解析好了
2. HttpServletRequest类可以获取请求信息，包括请求方式、请求路径、请求协议、请求参数、请求头等，内容。

```java
package com.charles.server;  
  
import jakarta.servlet.http.HttpServletRequest;  
import org.springframework.web.bind.annotation.RequestMapping;  
import org.springframework.web.bind.annotation.RestController;  
  
@RestController  
public class RequestController {  
    @RequestMapping("/request")  
    public String request(HttpServletRequest request) {  
        // 1. 获取请求方式  
        System.out.println("请求方式: "+request.getMethod());  
  
        // 2. 获取请求路径  
        System.out.println("URL: "+request.getRequestURL());  
        System.out.println("URI: "+request.getRequestURI());  
  
        // 3. 获取请求协议  
        System.out.println("协议: "+request.getProtocol());  
  
        // 4. 获取请求参数  
        System.out.println("请求参数name: "+request.getParameter("name"));  
        System.out.println("请求参数age: "+request.getParameter("age"));  
  
        // 5. 获取请求头  
        System.out.println("请求头Accept: "+request.getHeader("Accept"));  
  
        return "OK";  
  
        // http://localhost:8081/request?name=charles&age=18  
  
        // 请求方式: GET  
        // URL: http://localhost:8081/request        
        // URI: /request        
        // 协议: HTTP/1.1  
        // 请求参数name: charles  
        // 请求参数age: 18  
        // 请求头Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7  
    }  
}
```

状态码举例

1. 1xx：信息性状态码，表示请求已被接受，需要继续处理
2. 2xx：成功状态码，表示请求已成功被服务器接收、理解、并接受
   1. 200 OK：请求成功
3. 3xx：重定向状态码，表示需要进行附加操作以完成请求
   1. 307：临时重定向，请求的资源临时从不同的URI响应请求（比如http://www.baidu.com会被重定向到https://www.baidu.com）
4. 4xx：客户端错误状态码，表示请求包含语法错误或无法实现
5. 5xx：服务器错误状态码，表示服务器在处理请求的过程中发生了错误

HttpServletResponse类可以设置响应信息，包括响应状态码、响应头、响应体等内容。


## SpringBoot Web案例


## 分层解耦


