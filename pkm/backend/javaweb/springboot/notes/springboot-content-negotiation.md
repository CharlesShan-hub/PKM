# 内容协商

---

## 对内容协商的理解

内容协商机制是指服务器根据客户端的请求来决定返回资源的最佳表示形式。

白话文描述：客户端要什么格式的数据，咱后端就应该返回什么格式的数据。

+ 客户端要JSON，咱就响应JSON。
+ 客户端要XML，咱就响应XML。
+ 客户端要YAML，咱就响应YAML。

你可能会有疑问：客户端接收数据时统一采用一种格式，例如JSON，不就行了吗。哪那么多事儿呀！！！

但在实际的开发中，不是这样的，例如：

+ 遗留的老客户端系统，仍然处理的是XML格式的数据。
+ 要求处理速度快的这种客户端系统，一般要求返回JSON格式的数据。
+ 要求安全性高的客户端系统，一般要求返回XML格式的数据。

因此，在现代的开发中，不同的客户端可能需要后端系统返回不同格式的数据。总之后端应该满足这种多样化的需求。

---

## 实现内容协商的两种方式

通常通过HTTP请求头（如 Accept）或请求参数（如 format）来指定客户端偏好接收的内容类型（如JSON、XML等）。服务器会根据这些信息选择最合适的格式进行响应。

### 通过HTTP请求头（如 Accept）

SpringBoot框架中，在程序员不做任何配置的情况下，优先考虑的是这种方式。

服务器会根据客户端发送请求时提交的请求头中的"Accept: application/json" 或 "Accept: application/xml" 或 "Accept: text/html"来决定响应什么格式的数据。

客户端发送请求给服务器的时候，如何设置请求头的`Accept`？有以下几种常见实现方式：

+ 写代码
    - ajax的XMLHttpRequest
    - fetch API
    - axios库....
+ 用工具
    - 接口测试工具，例如：Postman、Apifox、Apipost 等。
    - 命令行工具：curl

对于我们编写的以下Controller来说：

```java
package com.jkweilai.springboot.controller;

import com.jkweilai.springboot.bean.User;
import com.jkweilai.springboot.service.UserService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class UserController {

    @Autowired
    private UserService userService;

    @GetMapping(value = "/detail")
    public User detail(){
        return userService.getUser();
    }
}
```

我们使用了`@RestController`，也就是使用了`@ResponseBody`。因此默认支持的是返回JSON数据。怎么才能支持返回XML格式的数据呢？需要做以下两步：

第一步：引入一个依赖（这个是必须的。）

```xml
<dependency>
  <groupId>com.fasterxml.jackson.dataformat</groupId>
  <artifactId>jackson-dataformat-xml</artifactId>
</dependency>
```

第二步：在实体类上添加一个注解：不是必须的，如果要定制 XML 根节点的名字，可以使用它。

```java
package com.jkweilai.springboot.bean;

import com.fasterxml.jackson.dataformat.xml.annotation.JacksonXmlRootElement;
import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

// 通过该注解可以定制XML根节点的名字，如果不需要定制，这个注解可以去掉。
@JacksonXmlRootElement(localName = "User")
@Data
@NoArgsConstructor
@AllArgsConstructor
public class User {
    private String name;
    private String password;
}
```

**测试：**

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1765110123829-ecd2c8ca-4445-43f4-96c0-2ce8eba59f8d.png" width="664" title="" crop="0,0,1,1" id="u8b85db29" class="ne-image">

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1765110157978-4af936e5-611a-4725-8d55-12d22ef090b1.png" width="568" title="" crop="0,0,1,1" id="uf47ba325" class="ne-image">

### **通过请求参数（如**`**format**`**）**

接下来我们使用请求参数的方式，`SpringBoot优先考虑的不是通过请求参数format方式`。如何优先考虑使用`format`方式呢？做如下配置：

```properties
