# 获取请求数据

假设有这样一个请求：http://localhost:8080/springmvc/register?name=zhangsan&password=123&email=zhangsan@jkweilai.com

在SpringMVC中应该如何获取请求提交的数据呢？

在SpringMVC中又应该如何获取请求头信息呢？

在SpringMVC中又应该如何获取客户端提交的Cookie数据呢？

**创建新的模块：**`springmvc-003`

---

## 准备工作

### 创建UserController

```java

package com.jkweilai.springmvc.controller;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;

@Controller
public class UserController {
    @RequestMapping("/")
    public String toRegisterPage(){
        return "register";
    }
}

```

### 提供一个注册页面

```html

<!DOCTYPE html>
<html lang="en" xmlns:th="http://www.thymeleaf.org">
<head>
    <meta charset="UTF-8">
    <title>用户注册</title>
</head>
<body>
<h3>用户注册</h3>
<hr>
<form th:action="@{/register}" method="post">
    用户名：<input type="text" name="username"><br>
    密码：<input type="password" name="password"><br>
    性别：
        男 <input type="radio" name="sex" value="1">
        女 <input type="radio" name="sex" value="0">
        <br>
    爱好：
        跑步 <input type="checkbox" name="hobby" value="1">
        唱歌 <input type="checkbox" name="hobby" value="2">
        跳舞 <input type="checkbox" name="hobby" value="3">
        <br>
    简介：<textarea rows="10" cols="60" name="intro"></textarea><br>
    <input type="submit" value="注册">
</form>
</body>
</html>

```

---

## 使用原生的Servlet API进行获取

****知识点列表：****

1. **什么是原生 Servlet API？**HttpServletRequest、HttpServletResponse 等
2. **Servlet 原生 API 如何注入？直接方法参数即可注入。**
3. **开发中是否推荐？不推荐。因为这种方式会导致 Controller 无法脱离 web 容器进行单元测试。**
4. **什么时候使用这种方式？比如需要手动设置响应头的场景就必须使用这种方式了。**

**原生的Servlet API指的是：**HttpServletRequest、HttpServletResponse 等。

在SpringMVC当中，一个Controller类中的方法参数上如果有HttpServletRequest，SpringMVC会自动将`****当前请求对象****`传递给这个参数，因此我们可以通过这个参数来获取请求提交的数据。

```java

@PostMapping(value="/register")
public String register(HttpServletRequest request){
    // 通过当前请求对象获取提交的数据
    String username = request.getParameter("username");
    String password = request.getParameter("password");
    String sex = request.getParameter("sex");
    String[] hobbies = request.getParameterValues("hobby");
    String intro = request.getParameter("intro");
    System.out.println(username + "," + password + "," + sex + "," + Arrays.toString(hobbies) + "," + intro);
    return "success";
}

```

**以下代码是完成一个文件下载的功能，这种情况下就需要使用原生的 Servlet API 了：**

```java

@GetMapping("/down")
public void downloadJpg(HttpServletRequest request, HttpServletResponse response) {
    try {
        // 获取ServletContext对象。
        ServletContext application = request.getServletContext();
        // 通过ServletContext获取文件绝对路径。
        String realPath = application.getRealPath("/img/image.jpg");
        File file = new File(realPath);

        // 设置图片相关的响应头
        response.setContentType("image/jpeg");
        // 设置文件下载行为：attachment 强制下载，不直接在浏览器中显示
        response.setHeader("Content-Disposition", "attachment; filename=\"image.jpg\"");
        response.setHeader("Content-Length", String.valueOf(file.length()));

        // 写入响应流
        Files.copy(file.toPath(), response.getOutputStream());
        response.flushBuffer();

    } catch (IOException e) {
        // 处理异常
        response.setStatus(HttpServletResponse.SC_NOT_FOUND);
    }
}

```

---

## 使用RequestParam注解标注

**知识点列表：**

1. **RequestParam注解作用：将**`**请求参数**`**与方法上的**`**形参**`**映射。**
2. **对于@RequestParam注解来说，属性有value和name，这两个属性的作用相同，都是用来指定提交数据的name。**
3. **@RequestParam(value="name2") 中value一定不要写错，写错就会出现 400 错误。**
4. **出现 400 错误的本质原因是：**`**@RequestParam**`**注解有一个 **`**required**`**属性，该属性未指定时，默认为 **`**true**`**，表示前端提交数据时必须提交该参数，如果不提交，则出现 400 错误。想避免该错误的发生，可以将 **`**required**`**属性值设置为 **`**false**`**。**
5. `**@RequestParam**`**注解有一个 **`**defaultValue**`**属性，用来指定参数的默认值，当没有提交该参数或提交的是空字符串时，**`**defaultValue**`**属性起作用。**

### RequestParam注解的基本使用

RequestParam注解作用：将`请求参数`与方法上的`形参`映射。

```java

@PostMapping(value = "/register")
public String register(
        @RequestParam(value="username")
        String a,
        @RequestParam(value="password")
        String b,
        @RequestParam(value="sex")
        String c,
        @RequestParam(value="hobby")
        String[] d,
        @RequestParam(name="intro")
        String e) {
    System.out.println(a);
    System.out.println(b);
    System.out.println(c);
    System.out.println(Arrays.toString(d));
    System.out.println(e);
    return "success";
}

```

注意：对于@RequestParam注解来说，属性有value和name，这两个属性的作用相同，都是用来指定提交数据的name。

<img src="https://cdn.nlark.com/yuque/0/2024/png/21376908/1710428008416-73b3a547-46ab-47bb-922c-b3d090e0cfc9.png" width="494" title="" crop="0,0,1,1" id="uaf3c3ba7" class="ne-image" style="font-size: 16px">

例如：发送请求时提交的数据是：name1=value1&name2=value2，则这个注解应该这样写：@RequestParam(value="name1")、@RequestParam(value="name2")

一定要注意： @RequestParam(value="name2") 中value一定不要写错，写错就会出现以下问题：

<img src="https://cdn.nlark.com/yuque/0/2024/png/21376908/1710428081389-9ac88bba-c37c-4fb8-9b9d-f7a9091b97ab.png" width="608" title="" crop="0,0,1,1" id="ua16f46af" class="ne-image" style="font-size: 16px">

测试结果：

<img src="https://cdn.nlark.com/yuque/0/2024/png/21376908/1710428139767-d3888c35-e2f8-407f-accb-f744a7098148.png" width="741" title="" crop="0,0,1,1" id="u1fdff3b9" class="ne-image" style="font-size: 16px">

### RequestParam注解的required属性

<img src="https://cdn.nlark.com/yuque/0/2024/png/21376908/1710465027479-caeb1d78-c92d-4fca-b9fa-80e6bcf06c7a.png" width="670" title="" crop="0,0,1,1" id="u05ce0a11" class="ne-image" style="font-size: 16px">

required属性用来设置该方法参数是否为必须的。

默认情况下，这个参数为 `true`，表示方法参数是必需的。如果请求中缺少对应的参数，则会抛出异常。

可以将其设置为`false`，false表示不是必须的，如果请求中缺少对应的参数，则方法的参数为null。

测试，修改register方法，如下：

<img src="https://cdn.nlark.com/yuque/0/2024/png/21376908/1710468078605-3c6a2dd2-e9c4-4450-9712-02f11b5543d3.png" width="610" title="" crop="0,0,1,1" id="ue64914c9" class="ne-image" style="font-size: 16px">

添加了一个 age 形参，没有指定 required 属性时，默认是true，表示必需的，但前端表单中没有年龄age，我们来看报错信息：

<img src="https://cdn.nlark.com/yuque/0/2024/png/21376908/1710468194109-56b8df42-2110-4b2b-9e73-064884f2e04b.png" width="807" title="" crop="0,0,1,1" id="u1a3fb4dc" class="ne-image" style="font-size: 16px">

错误信息告诉我们：参数age是必需的。没有提供这个请求参数，HTTP状态码 400

如果将 required 属性设置为 false。则该参数则不是必须的，如果请求参数仍然未提供时，我们来看结果：

<img src="https://cdn.nlark.com/yuque/0/2024/png/21376908/1710468402437-7395c6e2-6ab4-4bdc-a66e-cb82811be4e4.png" width="685" title="" crop="0,0,1,1" id="u3168e498" class="ne-image" style="font-size: 16px">

<img src="https://cdn.nlark.com/yuque/0/2024/png/21376908/1710468358266-82e27b39-b24a-4aca-902e-9a69c5630ca7.png" width="488" title="" crop="0,0,1,1" id="u0b40f7d7" class="ne-image" style="font-size: 16px">

<img src="https://cdn.nlark.com/yuque/0/2024/png/21376908/1710468442095-a0aa03e0-390e-440c-b9db-61139b8098cb.png" width="290" title="" crop="0,0,1,1" id="uf8a54914" class="ne-image" style="font-size: 16px">

通过测试得知，如果一个参数被设置为`不是必需的`，当没有提交对应的请求参数时，形参默认值null。

### 安装接口测试工具 Apipost

它是一个**国产的**接口测试工具，目前在国内使用较多。把它安装一下。咱们接下来使用一下：

**使用 Apipost 发送 get 请求，携带查询参数：**

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1764495647856-59d7c579-1696-4426-92d9-05a655fb3333.png" width="553.6" title="" crop="0,0,1,1" id="uc3431823" class="ne-image" style="font-size: 16px">

**使用 Apipost 发送 post 请求，以普通文本形式提交表单数据：**

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1764495789233-7daadea7-40f2-4dc5-a5c0-f3701794a167.png" width="547.2" title="" crop="0,0,1,1" id="u085eb63f" class="ne-image" style="font-size: 16px">

**使用 Apipost 发送 post 请求，以二进制的方式提交表单数据：（适合文件上传）**

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1764495917686-99311377-3e74-4b25-988e-0a4bfd9a4f37.png" width="593.6" title="" crop="0,0,1,1" id="u4e78698a" class="ne-image" style="font-size: 16px">

**使用 Apipost 发送 post 请求，并且提交 JSON 字符串到服务器：**

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1764496082736-acc6506c-f8b4-4197-8892-b95cd4b12db4.png" width="650.4" title="" crop="0,0,1,1" id="u072e2fb2" class="ne-image" style="font-size: 16px">

**使用 Apipost 工具发送请求时，设置请求头：**

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1764496187497-29597aed-7976-4807-a66b-880656ea95e9.png" width="650.4" title="" crop="0,0,1,1" id="u3101b1bf" class="ne-image" style="font-size: 16px">

**使用 Apipost 工作提交纯二进制数据，例如做单文件上传：**

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1764496419092-5687f07c-4d95-44c7-8621-af888667dfce.png" width="720" title="" crop="0,0,1,1" id="u55d8dfc6" class="ne-image" style="font-size: 16px">

### RequestParam注解的defaultValue属性

defaultValue属性用来设置形参的默认值，当`没有提供对应的请求参数`或者`请求参数的值是空字符串""`的时候，方法的形参会采用默认值。

**当前端页面没有提交email的时候：**

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1764496959630-5ca32659-fda5-4544-8438-23435d293a3b.png" width="677.6" title="" crop="0,0,1,1" id="u3ce279cc" class="ne-image" style="font-size: 16px">

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1764496981766-b5dc6d20-aec2-4fb2-974c-3fa170c2504e.png" width="200" title="" crop="0,0,1,1" id="UodRn" class="ne-image" style="font-size: 16px">

**当前端页面提交的email是空字符串的时候：**

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1764497016535-d8e10530-4012-4fe5-8884-c1d7a298b1da.png" width="638.4" title="" crop="0,0,1,1" id="u33cba45d" class="ne-image" style="font-size: 16px">

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1764496981766-b5dc6d20-aec2-4fb2-974c-3fa170c2504e.png" width="200" title="" crop="0,0,1,1" id="nMmHO" class="ne-image" style="font-size: 16px">

**当前端提交的email不是空字符串的时候：**

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1764497068703-6a9e6352-92f9-4fdd-8c21-5916c1d3f099.png" width="553.6" title="" crop="0,0,1,1" id="u766b6549" class="ne-image" style="font-size: 16px">

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1764497048835-480702a7-7869-4344-a4f5-cca96e8c584f.png" width="185.6" title="" crop="0,0,1,1" id="u2d8acedd" class="ne-image" style="font-size: 16px">

---

## 依靠控制器方法上的形参名来接收

**知识点列表：**

1. **@RequestParam 这个注解是可以省略的，如果方法形参的名字和提交数据时的name相同，则 @RequestParam 可以省略。**
2. **但有一个前提：如果你采用的是Spring6+版本，你需要在pom.xml文件中指定编译参数'-parameter'**
3. **形参名必须和提交数据的 name 一致。如果不一致，则形参值为 null。**
4. **如果前端提交的数组，后端也可以用 String 来接收，不一定使用数组。**

配置如下：

```xml

<build>
    <plugins>
        <plugin>
            <groupId>org.apache.maven.plugins</groupId>
            <artifactId>maven-compiler-plugin</artifactId>
            <version>3.12.1</version>
            <configuration>
                <source>21</source>
                <target>21</target>
                <compilerArgs>
                    <arg>-parameters</arg>
                </compilerArgs>
            </configuration>
        </plugin>
    </plugins>
</build>

```

****注意：如果你使用的是Spring5的版本，以上的配置是不需要的。****

Controller中的方法只需要这样写：****形参的名字必须和提交的数据的name一致！！！！！****

```java

@PostMapping(value="/register")
public String register(String username, String password, String sex, String[] hobby, String intro){
    System.out.println(username + "," + password + "," + sex + "," + Arrays.toString(hobby) + "," + intro);
    return "success";
}

```

如果形参名和提交的数据的name不一致时：

<img src="https://cdn.nlark.com/yuque/0/2024/png/21376908/1710428636791-b1c4eb79-ce31-4ecf-9ee5-4db8e6ffb0d6.png" width="1252" title="" crop="0,0,1,1" id="u3d867463" class="ne-image" style="font-size: 16px">

<img src="https://cdn.nlark.com/yuque/0/2024/png/21376908/1710428682813-4c2440c7-0500-4d02-a66a-7a3852ebd981.png" width="465" title="" crop="0,0,1,1" id="u4de014af" class="ne-image" style="font-size: 16px">

另外，还有一点，对于提交的hobby数据，也可以采用String来接收，不一定使用数组方式：

```java

@PostMapping(value="/register")
public String register(String username, String password, String sex, String hobby, String intro){
    System.out.println(username + "," + password + "," + sex + "," + hobby + "," + intro);
    return "success";
}

```

根据输出结果可以看到多个hobby是采用“,”进行连接的。

---

## 使用 JavaBean 接收请求参数

**知识点列表：**

1. **使用 JavaBean 接收数据更方便。**
2. **前提条件是提交的参数 name 必须和 JavaBean 的属性名保持一致。**
3. **底层实现原理是：通过反射机制调用 setter 方法给属性赋值的。**

以上方式大家可以看到，当提交的数据非常多时，方法的形参个数会非常多，这不是很好的设计。在SpringMVC中也可以使用POJO类/JavaBean来接收请求参数。不过有一个非常重要的要求：`POJO类的属性名`必须和`请求参数的参数名`保持一致。

**提供以下的 javabean 类：**

```java

package com.jkweilai.springmvc.pojo;

import java.util.Arrays;

public class User {
    private Long id;
    private String username;
    private String password;
    private String sex;
    private String[] hobby;
    private String intro;

    // setter and getter

    @Override
    public String toString() {
        return "User{" +
                "id=" + id +
                ", username='" + username + '\'' +
                ", password='" + password + '\'' +
                ", sex='" + sex + '\'' +
                ", hobby=" + Arrays.toString(hobby) +
                ", intro='" + intro + '\'' +
                '}';
    }
}

```

在控制器方法的形参位置上使用javabean来接收请求参数：

```java

@PostMapping("/register")
public String register(User user){
    System.out.println(user);
    return "success";
}

```

****底层的实现原理：反射机制。先获取请求参数的名字，因为请求参数的名字就是JavaBean的属性名，通过这种方式给对应的属性赋值****。

我们来测试一下：当JavaBean的属性名和请求参数的参数名不一致时，会出现什么问题？（注意：****getter和setter的方法名不修改，只修改属性名****）

```java

package com.jkweilai.springmvc.pojo;

import java.util.Arrays;

public class User {
    private Long id;
    private String uname;
    private String upwd;
    private String usex;
    private String[] uhobby;
    private String uintro;

    public User() {
    }

    public User(Long id, String username, String password, String sex, String[] hobby, String intro) {
        this.id = id;
        this.uname = username;
        this.upwd = password;
        this.usex = sex;
        this.uhobby = hobby;
        this.uintro = intro;
    }

    public Long getId() {
        return id;
    }

    public void setId(Long id) {
        this.id = id;
    }

    public String getUsername() {
        return uname;
    }

    public void setUsername(String username) {
        this.uname = username;
    }

    public String getPassword() {
        return upwd;
    }

    public void setPassword(String password) {
        this.upwd = password;
    }

    public String getSex() {
        return usex;
    }

    public void setSex(String sex) {
        this.usex = sex;
    }

    public String[] getHobby() {
        return uhobby;
    }

    public void setHobby(String[] hobby) {
        this.uhobby = hobby;
    }

    public String getIntro() {
        return uintro;
    }

    public void setIntro(String intro) {
        this.uintro = intro;
    }

    @Override
    public String toString() {
        return "User{" +
                "id=" + id +
                ", username='" + uname + '\'' +
                ", password='" + upwd + '\'' +
                ", sex='" + usex + '\'' +
                ", hobby=" + Arrays.toString(uhobby) +
                ", intro='" + uintro + '\'' +
                '}';
    }
}

```

测试结果：

<img src="https://cdn.nlark.com/yuque/0/2024/png/21376908/1710471772183-af36c134-1f73-4cb4-afc6-4a6a827aacbd.png" width="1139" title="" crop="0,0,1,1" id="u0d56b9d1" class="ne-image" style="font-size: 16px">

通过测试，我们得知：`请求参数名`可以和`JavaBean的属性名`不一致。

我们继续将其中一个属性的setter和getter方法名修改一下：

<img src="https://cdn.nlark.com/yuque/0/2024/png/21376908/1710471908862-89d1b430-cff1-43e2-9678-49017f49d663.png" width="455" title="" crop="0,0,1,1" id="u86492b81" class="ne-image" style="font-size: 16px">

再次测试：

<img src="https://cdn.nlark.com/yuque/0/2024/png/21376908/1710471961917-33f50796-7f73-4d40-a0ef-2befe83d5ebf.png" width="1179" title="" crop="0,0,1,1" id="u358b10f2" class="ne-image" style="font-size: 16px">

****通过测试可以看到：username属性没有赋上值。可见请求参数是否可以赋值到JavaBean对应的属性上，不是取决于属性名，而是setter方法名****。

---

## **RequestHeader注解**

**知识点列表：**

1. **该注解的作用是：将**`**请求头信息**`**映射到**`**方法的形参上**`**。**
2. **和RequestParam注解功能相似，RequestParam注解的作用：将**`**请求参数**`**映射到**`**方法的形参**`**上。**
3. **对于RequestHeader注解来说，也有三个属性：value、required、defaultValue，和RequestParam一样。**

测试：

```java

@PostMapping("/register")
public String register(User user, 
                       @RequestHeader(value="Referer", required = false, defaultValue = "") 
                       String referer){
    System.out.println(user);
    System.out.println(referer);
    return "success";
}

```

执行结果：

<img src="https://cdn.nlark.com/yuque/0/2024/png/21376908/1710472685320-fa79ddc4-04e0-4f8e-b97e-56f3f28ee60f.png" width="1131" title="" crop="0,0,1,1" id="u968684d7" class="ne-image" style="font-size: 16px">

---

## **CookieValue注解**

**知识点列表：**

1. **该注解的作用：将**`**请求提交的Cookie数据**`**映射到**`**方法形参**`**上**
2. **同样是有三个属性：value、required、defaultValue**

前端页面中编写发送cookie的代码：

```html

<script type="text/javascript">
    function sendCookie(){
        document.cookie = "id=123456789; expires=Thu, 18 Dec 2025 12:00:00 UTC; path=/";
        document.location = "/springmvc/register";
    }
</script>
<button onclick="sendCookie()">向服务器端发送Cookie</button>

```

后端UserController代码：

```java

    @GetMapping("/register")
    public String register(User user,
                           @RequestHeader(value="Referer", required = false, defaultValue = "")
                           String referer,
                           @CookieValue(value="id", required = false, defaultValue = "2222222222")
                           String id){
        System.out.println(user);
        System.out.println(referer);
        System.out.println(id);
        return "success";
    }

```

测试结果：

<img src="https://cdn.nlark.com/yuque/0/2024/png/21376908/1710473271244-7a95563a-fff4-458e-914f-25b314c78bd1.png" width="989" title="" crop="0,0,1,1" id="ue186aba0" class="ne-image" style="font-size: 16px">

---

## 请求的中文乱码问题

**知识点列表：**

1. **get 请求乱码如何解决？**
2. **post 请求乱码如何解决？**
3. **Tomcat10+版本已经默认将 GET/POST 字符编码方式设置为 UTF-8 了，因此多数情况下是不存在乱码问题的。**
4. **在 Controller 中编写 **`**request.setCharacterEncoding("UTF-8");**`**可以解决请求体的乱码问题吗？**
5. **SpringMVC 中内置了一个字符编码过滤器，它解决了乱码问题。直接配置它就行了。**

有可能很多同学使用的不是Tomcat10，如果不是Tomcat10，则会出现乱码问题，我们来模拟一下乱码的产生，将apache-tomcat-10.1.19\conf\web.xml文件中的UTF-8配置修改为ISO-8859-1：

<img src="https://cdn.nlark.com/yuque/0/2024/png/21376908/1710732413713-0f034192-e4d4-4c33-aeb3-169726468251.png" width="1076" title="" crop="0,0,1,1" id="u2e406be6" class="ne-image" style="font-size: 16px">

****一定要重启Tomcat10****，新的配置才能生效，来测试一下是否存在乱码：

<img src="https://cdn.nlark.com/yuque/0/2024/png/21376908/1710732483068-b356942a-9183-4734-812d-041a151df48d.png" width="1261" title="" crop="0,0,1,1" id="u6f629e75" class="ne-image" style="font-size: 16px">

那么，在SpringMVC中如何解决请求体的中文乱码问题呢？当然，还是使用`request.setCharacterEncoding("UTF-8")`

使用它有一个前提条件，要想解决请求体乱码问题，以上代码必须在 `request.getParameter("username")`执行之前执行才有效。

也就是说以上代码如果放在Controller的相关方法中执行是无效的，因为Controller的方法在执行之前 DispatcherServlet已经调用了 `request.getParameter("username")`方法。因此在Controller方法中使用`request.setCharacterEncoding("UTF-8");`无效我们来测试一下：

```html

<form th:action="@{/register}" method="post">
    用户名：<input type="text" name="username"><br>
    密码：<input type="password" name="password"><br>
    性别：
        男 <input type="radio" name="sex" value="1">
        女 <input type="radio" name="sex" value="0">
        <br>
    爱好：
        抽烟 <input type="checkbox" name="hobby" value="smoke">
        喝酒 <input type="checkbox" name="hobby" value="drink">
        烫头 <input type="checkbox" name="hobby" value="perm">
        <br>
    简介：<textarea rows="10" cols="60" name="intro"></textarea><br>
    <input type="submit" value="注册">
</form>

```

注意：以上表单已经修改为post请求

```java

@PostMapping("/register")
public String register(User user, HttpServletRequest request) throws UnsupportedEncodingException {
    request.setCharacterEncoding("UTF-8");
    System.out.println(user);
    return "success";
}

```

测试结果：

<img src="https://cdn.nlark.com/yuque/0/2024/png/21376908/1710732483068-b356942a-9183-4734-812d-041a151df48d.png" width="1261" title="" crop="0,0,1,1" id="prLSj" class="ne-image" style="font-size: 16px">

通过测试可以看到：在Controller当中调用`request.setCharacterEncoding("UTF-8")`是无法解决POST乱码问题的。

那怎么办呢？怎么样才能在DispatcherServlet之前执行`request.setCharacterEncoding("UTF-8")`呢？没错，我相信大家想到了：过滤器Filter。过滤器Filter可以在Servlet执行之前执行。有同学又说了：监听器不行吗？不行。因为我们需要对每一次请求解决乱码，而监听器只在服务器启动阶段执行一次。因此这里解决每一次请求的乱码问题，应该使用过滤器Filter。并且，告诉大家一个好消息，SpringMVC已经将这个字符编码的过滤器提前写好了，我们直接配置好即可：`CharacterEncodingFilter`，我们一起看一下它的源码：

```java

/*
 * Copyright 2002-2018 the original author or authors.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *      https://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

package org.springframework.web.filter;

import java.io.IOException;

import jakarta.servlet.FilterChain;
import jakarta.servlet.ServletException;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

import org.springframework.lang.Nullable;
import org.springframework.util.Assert;

/**
 * Servlet Filter that allows one to specify a character encoding for requests.
 * This is useful because current browsers typically do not set a character
 * encoding even if specified in the HTML page or form.
 *
 * <p>This filter can either apply its encoding if the request does not already
 * specify an encoding, or enforce this filter's encoding in any case
 * ("forceEncoding"="true"). In the latter case, the encoding will also be
 * applied as default response encoding (although this will usually be overridden
 * by a full content type set in the view).
 *
 * @author Juergen Hoeller
 * @since 15.03.2004
 * @see #setEncoding
 * @see #setForceEncoding
 * @see jakarta.servlet.http.HttpServletRequest#setCharacterEncoding
 * @see jakarta.servlet.http.HttpServletResponse#setCharacterEncoding
 */
public class CharacterEncodingFilter extends OncePerRequestFilter {

    @Nullable
    private String encoding;

    private boolean forceRequestEncoding = false;

    private boolean forceResponseEncoding = false;

    /**
     * Create a default {@code CharacterEncodingFilter},
     * with the encoding to be set via {@link #setEncoding}.
     * @see #setEncoding
     */
    public CharacterEncodingFilter() {
    }

    /**
     * Create a {@code CharacterEncodingFilter} for the given encoding.
     * @param encoding the encoding to apply
     * @since 4.2.3
     * @see #setEncoding
     */
    public CharacterEncodingFilter(String encoding) {
        this(encoding, false);
    }

    /**
     * Create a {@code CharacterEncodingFilter} for the given encoding.
     * @param encoding the encoding to apply
     * @param forceEncoding whether the specified encoding is supposed to
     * override existing request and response encodings
     * @since 4.2.3
     * @see #setEncoding
     * @see #setForceEncoding
     */
    public CharacterEncodingFilter(String encoding, boolean forceEncoding) {
        this(encoding, forceEncoding, forceEncoding);
    }

    /**
     * Create a {@code CharacterEncodingFilter} for the given encoding.
     * @param encoding the encoding to apply
     * @param forceRequestEncoding whether the specified encoding is supposed to
     * override existing request encodings
     * @param forceResponseEncoding whether the specified encoding is supposed to
     * override existing response encodings
     * @since 4.3
     * @see #setEncoding
     * @see #setForceRequestEncoding(boolean)
     * @see #setForceResponseEncoding(boolean)
     */
    public CharacterEncodingFilter(String encoding, boolean forceRequestEncoding, boolean forceResponseEncoding) {
        Assert.hasLength(encoding, "Encoding must not be empty");
        this.encoding = encoding;
        this.forceRequestEncoding = forceRequestEncoding;
        this.forceResponseEncoding = forceResponseEncoding;
    }

    /**
     * Set the encoding to use for requests. This encoding will be passed into a
     * {@link jakarta.servlet.http.HttpServletRequest#setCharacterEncoding} call.
     * <p>Whether this encoding will override existing request encodings
     * (and whether it will be applied as default response encoding as well)
     * depends on the {@link #setForceEncoding "forceEncoding"} flag.
     */
    public void setEncoding(@Nullable String encoding) {
        this.encoding = encoding;
    }

    /**
     * Return the configured encoding for requests and/or responses.
     * @since 4.3
     */
    @Nullable
    public String getEncoding() {
        return this.encoding;
    }

    /**
     * Set whether the configured {@link #setEncoding encoding} of this filter
     * is supposed to override existing request and response encodings.
     * <p>Default is "false", i.e. do not modify the encoding if
     * {@link jakarta.servlet.http.HttpServletRequest#getCharacterEncoding()}
     * returns a non-null value. Switch this to "true" to enforce the specified
     * encoding in any case, applying it as default response encoding as well.
     * <p>This is the equivalent to setting both {@link #setForceRequestEncoding(boolean)}
     * and {@link #setForceResponseEncoding(boolean)}.
     * @see #setForceRequestEncoding(boolean)
     * @see #setForceResponseEncoding(boolean)
     */
    public void setForceEncoding(boolean forceEncoding) {
        this.forceRequestEncoding = forceEncoding;
        this.forceResponseEncoding = forceEncoding;
    }

    /**
     * Set whether the configured {@link #setEncoding encoding} of this filter
     * is supposed to override existing request encodings.
     * <p>Default is "false", i.e. do not modify the encoding if
     * {@link jakarta.servlet.http.HttpServletRequest#getCharacterEncoding()}
     * returns a non-null value. Switch this to "true" to enforce the specified
     * encoding in any case.
     * @since 4.3
     */
    public void setForceRequestEncoding(boolean forceRequestEncoding) {
        this.forceRequestEncoding = forceRequestEncoding;
    }

    /**
     * Return whether the encoding should be forced on requests.
     * @since 4.3
     */
    public boolean isForceRequestEncoding() {
        return this.forceRequestEncoding;
    }

    /**
     * Set whether the configured {@link #setEncoding encoding} of this filter
     * is supposed to override existing response encodings.
     * <p>Default is "false", i.e. do not modify the encoding.
     * Switch this to "true" to enforce the specified encoding
     * for responses in any case.
     * @since 4.3
     */
    public void setForceResponseEncoding(boolean forceResponseEncoding) {
        this.forceResponseEncoding = forceResponseEncoding;
    }

    /**
     * Return whether the encoding should be forced on responses.
     * @since 4.3
     */
    public boolean isForceResponseEncoding() {
        return this.forceResponseEncoding;
    }

    @Override
    protected void doFilterInternal(
            HttpServletRequest request, HttpServletResponse response, FilterChain filterChain)
            throws ServletException, IOException {

        String encoding = getEncoding();
        if (encoding != null) {
            if (isForceRequestEncoding() || request.getCharacterEncoding() == null) {
                request.setCharacterEncoding(encoding);
            }
            if (isForceResponseEncoding()) {
                response.setCharacterEncoding(encoding);
            }
        }
        filterChain.doFilter(request, response);
    }

}

```

最核心的方法是：

```java

@Override
protected void doFilterInternal(
        HttpServletRequest request, HttpServletResponse response, FilterChain filterChain)
        throws ServletException, IOException {

    String encoding = getEncoding();
    if (encoding != null) {
        if (isForceRequestEncoding() || request.getCharacterEncoding() == null) {
            request.setCharacterEncoding(encoding);
        }
        if (isForceResponseEncoding()) {
            response.setCharacterEncoding(encoding);
        }
    }
    filterChain.doFilter(request, response);
}

```

分析以上核心方法得知该过滤器对请求和响应都设置了字符编码方式。

+ 当`**强行使用请求字符编码方式为true**`时，或者`**请求对象的字符编码方式为null**`时，设置请求的字符编码方式。
+ 当`**强行使用响应字符编码方式为true**`时，设置响应的字符编码方式。

根据以上代码，可以得出以下配置信息，在web.xml文件中对过滤器进行如下配置：

```xml

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

```

我们再来测试，重启Tomcat10，看看乱码是否能够解决？

<img src="https://cdn.nlark.com/yuque/0/2024/png/21376908/1710733643651-29370350-6188-4ada-a8b0-99c6264f3b7a.png" width="1166" title="" crop="0,0,1,1" id="ubacc784a" class="ne-image" style="font-size: 16px">

注意：针对于我们当前的Tomcat10的配置来说，它有默认的字符集ISO-8859-1，因此以下在web.xml文件中的配置是不能缺少的：

```xml

<init-param>
    <param-name>forceRequestEncoding</param-name>
    <param-value>true</param-value>
</init-param>

```

如果缺少它，仍然是会存在乱码问题的。自行测试一下！！！！
