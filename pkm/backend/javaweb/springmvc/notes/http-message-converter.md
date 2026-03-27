# Http 消息转换器

---

## 什么是 HTTP 消息转换器

1. **HTTP 消息**指的是**请求协议的内容**和**响应协议的内容**。
2. HTTP 消息转换器是：**它******将HTTP请求和响应中的原始数据（如JSON/XML/String）与Java对象之间进行智能双向转换******，让开发者能够直接处理业务对象，不需要手动解析和组装数据格式。**
3. **比如，前端提交一个 json 字符串，后端通过消息转换器直接将 json 字符串转换成 java 对象**
4. **或者后端生成了 java 对象，消息转换器也可以自动将 java 对象转换成 json 格式的字符串响应给前端。**

---

## **HTTP 消息转换器需要我们写吗**

不需要，SpringMVC 框架已经内置了很多消息转换器，可以满足日常开发，除非极特殊情况，内置的消息转换器无法完成时，我们可以自己定制。

---

## 内置常用的 HTTP 消息转换器有哪些

1. 所有的 HTTP 消息转换器都有一个公共的接口：`HttpMessageConverter`
2. 该接口下常见的消息转换器包括：
    1. `StringHttpMessageConverter`（**请求和响应阶段**都有用）
    2. `MappingJackson2HttpMessageConverter`（**请求和响应阶段**都有用）
    3. `FormHttpMessageConverter`（主要在**请求阶段**起作用）

---

## 怎么指定使用哪个 HTTP 消息转换器

在程序当中通过编写不同的注解，来选择不同的 HTTP 消息转换器。

**在响应阶段：（******使用@ResponseBody 来启用消息转换器******）**

1. 使用 `@ResponseBody`注解来启用`StringHttpMessageConverter`和`MappingJackson2HttpMessageConverter`
2. 当使用 `@ResponseBody`并且 `Controller#method()`返回一个**普通的字符串**时：`StringHttpMessageConverter`启用。它会把字符串直接写入响应体，假设方法返回 `hello`字符串，最终浏览器页面上就显示一个 `hello` 字符串。
3. 当使用 `@ResponseBody`并且 `Controller#method()`返回一个** Java 对象**时：`MappingJackson2HttpMessageConverter`启用（底层优先使用 jackson 来解析 json）。它会将 Java 对象转换成 JSON 格式的字符串响应给前端。
4. 在响应阶段如果没有使用 `@ResponseBody`注解标注，则默认会走 `ModelAndView`机制，不走消息转换器机制。
5. **总结一句话：**如果需要响应 JSON 给前端，就需要在 `Controller#method()`上添加`@ResponseBody`注解，并返回一个 Java 对象（一般是返回一个统一的 R 对象。）。

**在请求阶段：（******@RequestBody 来启用消息转换器******）**

1. 当请求头的 `Content-Type: application/json`，并且 `Controller#method()`方法的参数上使用了 `@RequestBody`，那么前端提交的 JSON 字符串将被转换成 Java 对象，底层使用的消息转换器是：`MappingJackson2HttpMessageConverter`
2. 当请求头的 `Content-Type`是 `text/plain`，并且 `Controller#method()`方法的参数上使用了 `@RequestBody`，后端会使用`StringHttpMessageConverter`
3. 当请求头的 `Content-Type`是 `application/x-www-form-urlencoded`或 `multipart/form-data`，并且 `Controller#method()`方法的参数上使用了 `@RequestBody`，后端会使用`FormHttpMessageConverter`。
4. 如果 `Controller#method()`方法的参数上没有添加 `@RequestBody`注解，是不会走任何消息转换器的。
5. **总结一句话：**前端如果提交 JSON 字符串，后端 `Controller#method()`参数设置为 Java 对象，并让参数使用 `@RequestBody`注解进行标注。底层会自动将 JSON 字符串转换成 Java 对象。

---

## 对于**响应**来说 mv 不是 null 时不会使用消息转换器

**对于响应来说**，如果 DispatcherServlet 的 doDispatch 方法中的 `mv`不是 null，则响应时不会走任何消息转换器。

****ModelAndView******和******消息转换器******是 Spring MVC 中两条完全不同的响应处理路径，******它们互斥******。**

****ModelAndView 机制中******，当请求提交数据，后端进行数据绑定时使用的机制是：******WebDataBinder 机制******。**

---

## **@ResponseBody 的使用**

### **@ResponseBody 可以出现的位置**

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1764666381864-bafe3e4c-545c-4216-acac-416ddb313800.png" width="435.2" title="" crop="0,0,1,1" id="u61904f2e" class="ne-image" style="font-size: 16px">

1. 出现在方法上：只作用于当前方法。
2. 出现在类上：作用于当前类中所有的方法。

### 功能一：响应普通字符串到前端

**第一步：前端 axios 发送 ajax post 请求**

```html

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>test</title>
</head>
<body>
<button id="loadMsgBtn">获取消息</button>
<div id="msg"></div>
<script src="https://unpkg.com/axios/dist/axios.min.js"></script>
<script>
    document.addEventListener("DOMContentLoaded", function(){
        let loadMsgBtn = document.querySelector("#loadMsgBtn");
        let msgDiv = document.querySelector("#msg");
        loadMsgBtn.addEventListener("click", async function (){
            try{
                // 发送ajax post请求
                let response = await axios.post("msg");
                msgDiv.textContent = response.data;
            }catch (e) {
               console.log(e);
            }
        });
    });
</script>
</body>
</html>

```

**第二步：编写 Controller，使用@ResponseBody注解，响应普通字符串**

```java

package com.jkweilai.usermgt.controller;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.ResponseBody;

@Controller
public class ResponseBodyController {
    
    @PostMapping("/msg")
    @ResponseBody
    public String hello(){
        // 重点是这里：由于使用@ResponseBody注解，因此返回值不再被当做逻辑视图名
        // 底层会使用消息转换器StringHttpMessageConverter，将该字符串直接写入响应体
        return "hello";
    }
}

```

**第三步：测试**

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1764667149639-b1911edf-23d9-4935-ac1f-eb154e6f48c9.png" width="104.8" title="" crop="0,0,1,1" id="u36a44e72" class="ne-image" style="font-size: 16px">

**总结：**使用@ResponseBody，`return "hello";`不再是逻辑视图名了，是一个普通的字符串，底层将自动使用 `StringHttpMessageConverter`转换器，将字符串直接写入响应体。

### 功能二：响应 json 字符串到前端

**第一步：引入解析 JSON 的库：**`**jackson**`**的依赖**

```xml

<dependency>
  <groupId>com.fasterxml.jackson.core</groupId>
  <artifactId>jackson-databind</artifactId>
  <version>2.17.0</version>
</dependency>

```

**第二步：编写实体类**

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

**第三步：编写 Controller**

```java

package com.jkweilai.usermgt.controller;

import com.jkweilai.usermgt.entity.User;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.ResponseBody;

@Controller
public class ResponseBodyController {

    @PostMapping("/msg")
    @ResponseBody
    public User hello() {
        User user = new User(100L, "张三", "zhangsan@123.com", 1);
        return user;
    }
    
}

```

**第四步：编写 axios 发送 ajax post 请求**

```html

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>test</title>
</head>
<body>
<button id="loadMsgBtn">获取消息</button>
<div id="msg"></div>
<script src="https://unpkg.com/axios/dist/axios.min.js"></script>
<script>
    document.addEventListener("DOMContentLoaded", function(){
        let loadMsgBtn = document.querySelector("#loadMsgBtn");
        let msgDiv = document.querySelector("#msg");
        loadMsgBtn.addEventListener("click", async function (){
            try{
                // 发送ajax post请求
                let response = await axios.post("msg");
                msgDiv.textContent = JSON.stringify(response.data); // 返回了一个对象，将对象转换成json字符串
            }catch (e) {
               console.log(e);
            }
        });
    });
</script>
</body>
</html>

```

**第五步：测试**

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1764668498115-0cb02a8c-5752-417e-bf13-22243d8554c7.png" width="476" title="" crop="0,0,1,1" id="u3b483f43" class="ne-image" style="font-size: 16px">

**总结：使用@ResponseBody注解标注，并且**`**return obj;**`**时，另外也引入了解析 json 的 java 库之后，会自动使用**`**MappingJackson2HttpMessageConverter**`**消息转换器。**

---

## @RestController 的使用

1. 现代开发中，一般 `Controller`中每一个方法上都需要添加 `@ResponseBody`注解，因为大部分情况下都是返回 JSON 字符串给前端，为了注解复用，`@ResponseBody`最好写在类上面，如下：

```java

@Controller
@ResponseBody
public class ResponseBodyController {
    @PostMapping("/msg1")
    public String hello1() {
        return "hello";
    }
    @PostMapping("/msg2")
    public User hello2() {
        User user = new User(100L, "张三", "zhangsan@123.com", 1);
        return user;
    }
}

```

2. 以上代码可以继续再简化，SpringMVC 提供了 `@RestController`，`@RestController = @Controller + @ResponseBody`，因此代码直接这样写即可：

```java

@RestController
public class ResponseBodyController {
    @PostMapping("/msg1")
    public String hello1() {
        return "hello";
    }
    @PostMapping("/msg2")
    public User hello2() {
        User user = new User(100L, "张三", "zhangsan@123.com", 1);
        return user;
    }
}

```

---

## @RequestBody 的使用

`@RequestBody`经常使用在：前端提交一个 JSON 字符串。后端要将 JSON 字符串转换成 Java 对象。

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1764669597129-7308113b-2153-4a11-a0e6-f4f9add26571.png" width="392" title="" crop="0,0,1,1" id="uf93a8b3b" class="ne-image" style="font-size: 16px">

**第一步：引入 jackson 依赖**

**第二步：编写 User 类**

**第三步：编写 Controller**

```java

@RestController
public class ResponseBodyController {
    @PostMapping("/msg")
    public User hello(@RequestBody User user) {
        return user;
    }
}

```

**第四步：编写 axios 发送 ajax post 请求**

```html

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>test</title>
</head>
<body>
<button id="loadMsgBtn">获取消息</button>
<div id="msg"></div>
<script src="https://unpkg.com/axios/dist/axios.min.js"></script>
<script>
    document.addEventListener("DOMContentLoaded", function(){
        let loadMsgBtn = document.querySelector("#loadMsgBtn");
        let msgDiv = document.querySelector("#msg");
        loadMsgBtn.addEventListener("click", async function (){
            try{
                // 前端准备好数据
                let data = {
                    id: 1,
                    name: "admin",
                    gender: 1,
                    email: "admin@123.com"
                };
                // 发送ajax post请求
                let response = await axios.post("msg", data);
                msgDiv.textContent = JSON.stringify(response.data); // 返回了一个对象，将对象转换成json字符串
            }catch (e) {
               console.log(e);
            }
        });
    });
</script>
</body>
</html>

```

**第五步：测试**

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1764669405713-b9607dc0-7cdc-436d-9e49-626036a8cae2.png" width="464" title="" crop="0,0,1,1" id="ub62c0df9" class="ne-image" style="font-size: 16px">

---

## RequestEntity

RequestEntity不是一个注解，是一个普通的类。这个类的实例封装了整个请求协议：**包括请求行、请求头、请求体所有信息**。

出现在控制器方法的参数上：

```java

@RequestMapping("/send")
@ResponseBody
public String send(RequestEntity<User> requestEntity){
    System.out.println("请求方式：" + requestEntity.getMethod());
    System.out.println("请求URL：" + requestEntity.getUrl());
    HttpHeaders headers = requestEntity.getHeaders();
    System.out.println("请求的内容类型：" + headers.getContentType());
    System.out.println("请求头：" + headers);

    User user = requestEntity.getBody();
    System.out.println(user);
    System.out.println(user.getUsername());
    System.out.println(user.getPassword());
    return "success";
}

```

在实际的开发中，如果你需要获取更详细的请求协议中的信息。可以使用`RequestEntity`

---

## ResponseEntity

ResponseEntity不是注解，是一个类。用该类的实例可以封装响应协议，包括：状态行、响应头、响应体。也就是说：如果你想定制属于自己的响应协议，可以使用该类。

假如我要完成这样一个需求：前端提交一个id，后端根据id进行查询，如果返回null，请在前端显示404错误。如果返回不是null，则输出返回的user。

```java

@Controller
public class UserController {
     
    @GetMapping("/users/{id}")
    public ResponseEntity<User> getUserById(@PathVariable Long id) {
        User user = userService.getUserById(id);
        if (user == null) {
            return ResponseEntity.status(HttpStatus.NOT_FOUND).body(null); // 404
        } else {
            return ResponseEntity.ok(user); // 200
        }
    }
}

```

测试：当用户不存在时

<img src="https://cdn.nlark.com/yuque/0/2024/png/21376908/1711032765280-343794d6-b262-460b-8c03-e14bd8946850.png" width="1159" title="" crop="0,0,1,1" id="i4wT6" class="ne-image" style="font-size: 16px">

测试：当用户存在时

<img src="https://cdn.nlark.com/yuque/0/2024/png/21376908/1711032830325-866fe36b-cc47-4493-b9bb-8ebd34c7a86c.png" width="515" title="" crop="0,0,1,1" id="llYjP" class="ne-image" style="font-size: 16px">

---

## RESTful 的 AJAX 请求总结

1. 发送 get 请求：`axios.get(url,config)`，如果需要提交多个参数，则在 `config`对象中配置 `params`属性，例如以下代码：

```javascript

axios.get('/api/users', {
  params: {
    id: 1,
    name: "zhangsan"
  }
});

```

2. 发送 post 请求：`axios.post(url,data,config)`
3. 发送 put 请求：`axios.put(url,data,config)`
4. 发送 delete 请求：`axios.delete(url,config)`，删除多条数据时，则在 `config`对象中配置 `params`属性，例如以下代码：

```javascript

axios.delete('/api/users', {
  params: {
    ids: [2, 3]  // 使用数组
  }
});

```
