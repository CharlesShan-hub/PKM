# 会话管理

---

## 项目存在的问题

部门管理系统现在任何人都可以访问，只要知道请求路径，假设知道部门列表页面的请求路径 `http://localhost:8080/dept/list`

![](https://cdn.nlark.com/yuque/0/2025/png/21376908/1749450392879-651f3ccc-912e-447f-9bd5-ec503377281f.png)

如果知道删除部门的请求路径 `http://localhost:8080/dept/delete?deptno=20`，这个部门将会删除。

因此系统应该提供登录功能，只有登录的人（管理员：有权限的人）才能够进行相关的操作。用户登录功能也是一个系统最基本的功能。

登录功能实现的关键点：

1. 正确的用户名和密码，才能登录成功。
2. 登录成功后应该将用户登录的状态保存住。

---

## 登录功能的实现

分析实现步骤：

1. 需要一张用户表 `t_user`存储用户名和密码。
2. 密码需要以 `Argon2（阿尔戈恩）`加密方式存储。
3. 需要提供一个登录页面。
4. 用户登录页面上填写用户名和密码，提交表单，后端 Servlet 获取用户名和密码，验证是否正确，如果正确登录成功，跳转到部门列表页面。如果错误登录失败，重新跳转到登录页面，并提示登录失败。

### 用户表创建

`t_user`表：

![](https://cdn.nlark.com/yuque/0/2025/png/21376908/1749453368431-dc296051-f4eb-4207-a9b4-29f1a8e81252.png)

```sql
DROP TABLE IF EXISTS `t_user`;
CREATE TABLE `t_user`  (
  `id` int NOT NULL AUTO_INCREMENT COMMENT '主键自增',
  `username` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '用户名',
  `password` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT 'hash加密',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = DYNAMIC;
```

### Argon2 加密算法

**Argon2 是一种抗 GPU/ASIC 破解的现代密码哈希算法，通过可调内存和计算成本抵御暴力攻击，被公认为当前最安全的密码存储方案之一。**（核心特点：内存困难型、抗硬件加速破解、密码哈希大赛冠军）

提供一个工具 `Argon2PasswordUtil`，将这个工具类放到 dept 项目中：

```java
package com.jkweilai.dept.utils;

import org.bouncycastle.crypto.generators.Argon2BytesGenerator;
import org.bouncycastle.crypto.params.Argon2Parameters;

import java.nio.charset.StandardCharsets;
import java.security.SecureRandom;
import java.util.Base64;

public class Argon2PasswordUtil {

    // Argon2 参数配置（可根据需求调整）
    private static final int ITERATIONS = 3;          // 迭代次数
    private static final int MEMORY_COST = 65536;     // 内存成本（64MB）
    private static final int PARALLELISM = 4;         // 并行度
    private static final int SALT_LENGTH = 16;        // 盐值长度（16字节）
    private static final int HASH_LENGTH = 32;        // 哈希输出长度（32字节）

    /**
     * 生成 Argon2 哈希密码（含盐值）
     */
    public static String hashPassword(String password) {
        // 1. 生成随机盐值
        byte[] salt = generateSalt();

        // 2. 配置 Argon2 参数
        Argon2Parameters.Builder builder = new Argon2Parameters.Builder(Argon2Parameters.ARGON2_id)
                .withSalt(salt)
                .withIterations(ITERATIONS)
                .withMemoryAsKB(MEMORY_COST)
                .withParallelism(PARALLELISM);

        // 3. 生成哈希
        Argon2BytesGenerator generator = new Argon2BytesGenerator();
        generator.init(builder.build());
        byte[] hash = new byte[HASH_LENGTH];
        generator.generateBytes(password.getBytes(StandardCharsets.UTF_8), hash);

        // 4. 返回格式：算法$版本$参数$盐$哈希（Base64编码）
        return "argon2id" +
                "$v=19" +
                "$m=" + MEMORY_COST + ",t=" + ITERATIONS + ",p=" + PARALLELISM +
                "$" + Base64.getEncoder().encodeToString(salt) +
                "$" + Base64.getEncoder().encodeToString(hash);
    }

    /**
     * 验证密码是否正确
     */
    public static boolean verifyPassword(String password, String hashedPassword) {
        // 1. 解析存储的哈希字符串
        String[] parts = hashedPassword.split("\\$");
        if (parts.length != 5 || !parts[0].equals("argon2id")) {
            throw new IllegalArgumentException("Invalid Argon2 hash format");
        }

        // 2. 提取参数
        byte[] salt = Base64.getDecoder().decode(parts[3]);
        byte[] storedHash = Base64.getDecoder().decode(parts[4]);

        // 3. 重新计算哈希
        Argon2Parameters.Builder builder = new Argon2Parameters.Builder(Argon2Parameters.ARGON2_id)
                .withSalt(salt)
                .withIterations(ITERATIONS)
                .withMemoryAsKB(MEMORY_COST)
                .withParallelism(PARALLELISM);

        Argon2BytesGenerator generator = new Argon2BytesGenerator();
        generator.init(builder.build());
        byte[] computedHash = new byte[storedHash.length];
        generator.generateBytes(password.getBytes(StandardCharsets.UTF_8), computedHash);

        // 4. 比较哈希值
        return constantTimeEquals(storedHash, computedHash);
    }

    /**
     * 生成随机盐值
     */
    private static byte[] generateSalt() {
        SecureRandom random = new SecureRandom();
        byte[] salt = new byte[SALT_LENGTH];
        random.nextBytes(salt);
        return salt;
    }

    /**
     * 安全比较字节数组（防止时序攻击）
     */
    private static boolean constantTimeEquals(byte[] a, byte[] b) {
        if (a.length != b.length) {
            return false;
        }
        int result = 0;
        for (int i = 0; i < a.length; i++) {
            result |= a[i] ^ b[i];
        }
        return result == 0;
    }
}
```

说明：

1. `hashPassword`方法的作用是：将明文经过 Argon2 算法加密生成密文。
2. `verifyPassword`方法的作用是：验证密码是否正确。

提示：如果需要使用 Argon2 加密算法，需要引入相关的 java jar 包，如下：

![](https://cdn.nlark.com/yuque/0/2025/png/21376908/1749454867679-ad1eccf2-bbaa-4018-b2e0-a12022b4df1a.png)

将这个 jar 包拷贝到 `WEB-INF/lib`目录下，并且将其添加到 classpath 当中。

### 生成密文存储到数据库

在 `Argon2PasswordUtil`中临时添加一个 main 方法，在该方法中为密码 `Abc_%*123-dEf`加密：

```java
// 临时生成密文
public static void main(String[] args) {
    String s = hashPassword("Abc_%*123-dEf");
    System.out.println(s);
}
```

执行这个 main 方法，在控制台上会打印密文，将密文插入的数据库表当中。

dept 项目的管理员用户名是：`admin`，密码是：`Abc_%*123-dEf`

### 登录页面的开发

把之前开发静态网站时的 `index.html`代码拷贝过来放到 `WEB-INF/templates/index.html`文件中：记得把 css 单独写到 `css/index.css`文件中。

```html
<!DOCTYPE html>
<html lang="zh-CN" xmlns:th="http://www.thymeleaf.org">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>部门管理系统 - 登录</title>
  <link rel="stylesheet" th:href="@{/css/index.css}">
</head>
<body>
<div class="login-container">
  <div class="login-header">
    <h1>部门管理系统</h1>
    <p>请输入您的凭据以继续</p>
  </div>
  <form th:action="@{/login}" method="post">
    <div class="form-group">
      <label for="username">用户名</label>
      <input type="text" id="username" name="username" placeholder="请输入用户名" required>
    </div>
    <div class="form-group">
      <label for="password">密码</label>
      <input type="password" id="password" name="password" placeholder="请输入密码" required>
    </div>
    <button type="submit" class="login-btn">登录</button>
  </form>
  <div class="footer">
    <p>© 2025 部门管理系统 - 版权所有</p>
  </div>
</div>
</body>
</html>
```

### 登录页面的展示

编写 `IndexServlet`跳转到 `WEB-INF/templates/index.html`页面，完成登录页面的展示：

```java
package com.jkweilai.dept.servlets;

import jakarta.servlet.ServletException;
import jakarta.servlet.annotation.WebServlet;
import jakarta.servlet.http.HttpServlet;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

import java.io.IOException;

@WebServlet("/index")
public class IndexServlet extends HttpServlet {
    @Override
    protected void doGet(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
        req.setAttribute("template", "index");
        req.getRequestDispatcher("/view").forward(req, resp);
    }
}
```

### 登录请求处理

用户在登录页面输入用户名和密码，点击登录按钮，提交表单数据，后端 `LoginServlet`接收登录信息，连接数据库验证用户名密码是否正确，如果正确，则重定向到部门列表页面，如果登录失败，则将失败信息存储到 request 域中，重新跳回登录页面。在登录页面展示登录失败的信息。

```java
package com.jkweilai.dept.servlets;

import com.jkweilai.dept.utils.Argon2PasswordUtil;
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

@WebServlet("/login")
public class LoginServlet extends HttpServlet {
    @Override
    protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        // 获取用户名和密码
        String username = request.getParameter("username");
        String password = request.getParameter("password");
        // 连接数据库校验用户名和密码
        Connection conn = null;
        PreparedStatement ps = null;
        ResultSet rs = null;
        boolean loginSuccess = false;
        try {
            conn = DbUtils.getConnection();
            String sql = "select password from t_user where username = ?";
            ps = conn.prepareStatement(sql);
            ps.setString(1, username);
            rs = ps.executeQuery();
            if(rs.next()) {
                String hashPassword = rs.getString("password");
                if(Argon2PasswordUtil.verifyPassword(password, hashPassword)) {
                    // 登录成功
                    loginSuccess = true;
                    // 重定向到部门列表
                    response.sendRedirect(request.getContextPath() + "/list");
                }
            }
        } catch (Exception e) {
            e.printStackTrace();
        } finally {
            DbUtils.close(conn, ps, rs);
        }
        // 登录失败，转发到登录页面
        if(!loginSuccess) {
            request.setAttribute("errorMsg", "用户名不存在或密码错误！");
            request.setAttribute("template", "index");
            request.getRequestDispatcher("/view").forward(request, response);
        }
    }
}
```

当登录失败时，页面显示的效果如下：

![](https://cdn.nlark.com/yuque/0/2025/png/21376908/1749515601938-27efefc2-7ea2-4efb-ad54-49c353d91b82.png)

当登录成功时，会跳转到部门列表页面：

![](https://cdn.nlark.com/yuque/0/2025/png/21376908/1749515657512-aabcfec2-b91d-4f2f-bba3-66ecea8ffa91.png)

到此为止，登录功能基本的逻辑已经实现了。

### 当前登录功能有用吗

虽然登录功能已经实现，但是这个登录功能起作用了吗？

测试一下，可以把浏览器关闭，重新打开浏览器，在不登录的情况下，直接访问部门列表页面，看看能不能访问。

经过测试，大家应该看到了，部门列表页面在没有登录的情况下，仍然是可以访问的，可见目前的登录功能没有起到作用。

我们要达到的效果是：要想使用系统中的部门维护相关功能，必须是在已经登录的状态下。如果已经登录了，可以继续访问，如果没有登录则需要跳转到登录页面要求用户登录。

那我们应该怎么判断用户是已经登录了还是没有登录呢？也就是说，我们怎么判断用户当前的登录状态呢？

再换句话说，在 web 项目中我们应该怎么保存用户的登录状态呢？这就需要使用 session 机制了。

---

## session 机制

### **HTTP 协议的无状态性**

**HTTP 协议在设计之初是******无状态的******：**

1. ****每个请求相互独立******：服务器默认不会记住之前的请求（例如：第一次请求登录，第二次请求查看购物车时，服务器不知道这两个请求来自同一用户）**
2. ****简单高效******：无状态设计降低了服务器资源消耗，符合早期 Web 的静态页面需求**

****但现实业务需要状态！******例如：用户登录后，后续操作（如加购商品、支付）都需要知道是谁在操作。**

**session 机制在 HTTP 无状态的基础上******模拟出"有状态"。****

### 什么是 session

****session（会话） 并不是 JavaWeb 独有的机制******，是一种广泛应用于 Web 开发的******会话管理技术******，几乎所有服务端技术（如 PHP、ASP.NET、Python Django/Flask等）都实现了类似的 session 机制。**

**session是服务器端用来跟踪用户状态的一种机制。在 JavaWeb 开发中，session 指的是**`****HttpSession****`**对象，它代表了服务器与客户端（通常是浏览器）之间的一次会话。**

****"一次会话"******指的是******从用户首次访问服务器到结束交互的完整过程******。**

**session 是存储在 web 服务器端的，在 JavaWeb 开发中，在 Tomcat 服务器中会自动维护一个 session 列表，session 对象存储在 session 列表中，每一个 session 对象都会对应一个 sessionId。**

### session 的获取

在 JavaWeb 开发中，通过以下代码来获取服务器端的 session 对象：

第一种方式：获取该请求对应的 session 对象，如果没有该请求关联的 session 对象，则创建一个新的 session 对象与当前请求关联。

```java
HttpSession session = request.getSession();
```

第二种方式：获取该请求对应的 session 对象，如果没有该请求关联的 session 对象，则返回 null。

```java
HttpSession session = request.getSession(false);
```

### session 的工作原理

1. **当客户端第一次访问服务器时，执行到**`**HttpSession session = request.getSession();**`**代码时，服务器会创建该用户所属的 session 对象，并且为该 session 对象生成一个 sessionId。**
2. **这个 sessionId 会通过 Cookie 返回给客户端**
    1. **如果浏览器禁用 Cookie 的话，可以通过******URL 重写的方式******将 sessionId 响应给客户端，不过 URL 重写机制会导致开发繁琐，因此大多数网站是要求客户不要禁用 Cookie 的**
3. **客户端在******后续******请求中会携带这个 sessionId**
4. **服务器通过 sessionId 识别并返回该用户所属的 session 对象**

**编写程序，可以测试一下，发送请求时打开浏览器的网络面板，查看具体的请求报文和响应报文：**

**第一次发送请求时，客户端不会携带 sessionId，因为客户端中没有 sessionId，但是服务器端会响应 sessionId，因此在请求报文中没有 sessionId，但是在响应报文中应该存在 sessionId**

**请求头：**

![](https://cdn.nlark.com/yuque/0/2025/png/21376908/1749521891896-01187993-9e7b-43bf-aa47-467a2fe794e0.png)

响应头：

![](https://cdn.nlark.com/yuque/0/2025/png/21376908/1749521935384-77267fb4-55f9-43aa-aab0-07110bf82933.png)

**第二次发送请求时，客户端会携带 sessionId，因为客户端中已经存在 sessionId 了，服务器不会再生成新的 session 对象，进而不会生成新的 sessionId，因此响应报文中不应该存在 sessionId**

**请求头：**

![](https://cdn.nlark.com/yuque/0/2025/png/21376908/1749521974147-43eb3b46-c1e8-4573-ad40-dd27c2180e6c.png)

**响应头：**

![](https://cdn.nlark.com/yuque/0/2025/png/21376908/1749521983614-28d4f20a-93af-483e-abf3-899fdc248481.png)

### **session 的主要用途**

1. ****用户身份认证******：存储登录状态，记录用户是否已登录**
2. ****数据共享******：在同一用户的不同请求间共享数据**
3. ****购物车功能******：电商网站中存储用户选择的商品**
4. ****用户偏好设置******：保存用户的个性化设置**

### session 作用域

在 JavaWeb 开发中 session 对象也提供了以下三个方法：

```java
// 向会话域中存储数据
void setAttribute(String name, Object data);

// 从会话域中取数据
Object getAttribute(String name);

// 删除会话域中的数据
void removeAttribute(String name);
```

****request、session、application******是 JavaWeb 开发中三个不同作用域的存储对象，它们的主要区别在于******生命周期******和******数据共享范围******。以下是详细对比：**

| ****作用域**** | ****实现类/接口**** | ****生命周期**** | ****数据共享范围**** | ****典型应用场景**** |
| --- | --- | --- | --- | --- |
| ****request**** | `****HttpServletRequest****` | **一次请求内有效** | **当前请求的转发链（forward）** | **页面间跳转时传递临时数据** |
| ****session**** | `****HttpSession****` | **用户会话期间（默认30分钟无活动失效）** | **同一用户的所有请求** | **存储登录状态、购物车数据** |
| ****application**** | `****ServletContext****` | **Web应用启动到停止** | **所有用户共享** | **全局配置、计数器、缓存数据** |

三个作用域中 `application`应用域因所有用户共享，如果共享数据涉及到修改操作，需要考虑线程安全问题。session 和 request 则不存在这个问题。

三个作用域的选择原则：尽可能使用小的作用域对象。

### session 的超时机制

默认情况下，服务器是不知道用户关闭浏览器这个行为的，因此 session 需要引入超时机制，以免失效的 session 一直停留在服务器内存当中。

session 一直停留在服务器中的问题：

1. 耗费内存。
2. session 对象被劫持的话，存在安全问题。

在 Tomcat 服务器中，默认情况下 session 的超时时间设置的是 30 分钟，在 `CATALINA_HOME/confi/web.xml`中有默认配置，如下：

![](https://cdn.nlark.com/yuque/0/2025/png/21376908/1749521047119-4cc75f0b-4e60-4757-93df-6699ce0e8eb7.png)

这是一个全局的配置，我们也可以在自己项目的 web.xml 文件中进行局部配置，局部优先生效。

### 手动销毁 session

session 除了依靠 session 超时机制来销毁之外，也支持手动销毁 session，调用以下方法可以销毁 session：

```java
session.invalidate(); // 手动销毁
```

例如，用户如果在浏览器上主动点击了 `安全退出`或者 `退出登录`等按钮，表示用户主动退出系统，后端应该执行以上代码来主动销毁 session 对象。

### session 中数据的持久化

session 对象销毁时，session 中可能保留了用户会话时的数据，例如用户登录后往购物车中存放的商品。（为什么要这样做？这是为了保证用户下一次登录成功后，购物车未结算的商品可以正常展示。）

如何持久化，可以使用监听器来完成，例如以下示例代码：

```java
import javax.servlet.annotation.WebListener;
import javax.servlet.http.HttpSessionEvent;
import javax.servlet.http.HttpSessionAttributeListener;
import javax.servlet.http.HttpSessionBindingEvent;

@WebListener
public class SessionPersistenceListener implements HttpSessionListener {

    @Override
    public void sessionDestroyed(HttpSessionEvent se) {
        // Session超时或调用invalidate()时触发
        HttpSession session = se.getSession();
        
        // 获取需要持久化的数据
        User user = (User) session.getAttribute("user");
        ShoppingCart cart = (ShoppingCart) session.getAttribute("cart");
        
        // 执行持久化操作
        if (user != null) {
            UserDao.saveLastActivityTime(user.getId(), new Date());
        }
        if (cart != null && !cart.isEmpty()) {
            CartService.saveTemporaryCart(user.getId(), cart);
        }
    }
}
```

---

## 完善登录功能

我们应该在用户登录成功后，创建该用户对应的 session 对象，然后将用户登录信息，存储到 session 域当中。以后就可以通过 session 对象中是否存在登录信息来判定用户是否登录了。

`LoginServlet`代码修改如下：

![](https://cdn.nlark.com/yuque/0/2025/png/21376908/1749522198381-d6ab2758-6d6b-4bd4-b6bd-204bc48bd7b2.png)

---

## 登录验证过滤器

怎么能让已经登录的用户才能访问部门列表页面？

这就需要在 `DeptListServlet`类中添加拦截逻辑了：获取 session，判断 session 中是否存在用户名，如果不存在则跳转到登录页面，如果存在则表示已登录，可以继续访问。

这个拦截逻辑不仅需要在 `DeptListServlet`类中添加，在其它 Servlet 中也需要添加，因此有必要编写一个过滤器来进行拦截。

思考：这个过滤器应该拦截什么请求路径，什么路径不应该拦截？

1. 如果用户是显示登录页面，不应该拦截。`/dept/index`不能拦截。
2. 如果用户是登录请求，不应该拦截。`/dept/login`不能拦截。
3. 如果请求路径以 `/css`开始，不应该拦截。（当然项目中也可能存在 js 文件，jpg 或 png 等图片，也不应该拦截）
4. 其它的请求路径一律拦截。

编写过滤器 `CheckLoginFilter`：

```java
package com.jkweilai.dept.filters;

import jakarta.servlet.*;
import jakarta.servlet.annotation.WebFilter;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.servlet.http.HttpSession;

import java.io.IOException;

// 所有请求路径都经过这个过滤器
@WebFilter("/*")
public class CheckLoginFilter implements Filter {

    @Override
    public void doFilter(ServletRequest req, ServletResponse resp, FilterChain chain) throws IOException, ServletException {
        HttpServletRequest request = (HttpServletRequest) req;
        HttpServletResponse response = (HttpServletResponse) resp;
        HttpSession session = request.getSession(false);
        String servletPath = request.getServletPath();
        if ("/index".equals(servletPath) || "/login".equals(servletPath) || servletPath.startsWith("/css") || (session != null && session.getAttribute("username") != null)) {
            chain.doFilter(req, resp);
        } else {
            response.sendRedirect(request.getContextPath() + "/index");
        }
    }
}
```

到此为止，登录功能就完全起作用了。

---

## 关于 web 站点欢迎页

在 `CATALINA_HOME/conf/web.xml`文件中对欢迎页进行了全局配置，如下：

![](https://cdn.nlark.com/yuque/0/2025/png/21376908/1749524091859-be8f6d06-1f98-4ac9-b074-f9cc5132e215.png)

因此默认情况下，这几个页面被当做欢迎页。

设置了欢迎页之后的效果是：访问 web 项目的根时，如果没有指定具体的资源路径，默认走欢迎页，例如访问 `http://localhost:8080/dept`时，默认会访问 `http://localhost:8080/dept/index.html`。

我们也可以在自己项目的 web.xml 文件中配置局部的欢迎页，局部优先。

如果我希望把 `http://localhost:8080/dept/index`作为欢迎页的话，应该这样配置：

```xml
<?xml version="1.0" encoding="UTF-8"?>
<web-app xmlns="https://jakarta.ee/xml/ns/jakartaee"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="https://jakarta.ee/xml/ns/jakartaee https://jakarta.ee/xml/ns/jakartaee/web-app_6_0.xsd"
         version="6.0">
    
    <welcome-file-list>
        <welcome-file>index</welcome-file>
    </welcome-file-list>
</web-app>
```

需要注意的是：欢迎页路径在设置的时候，不需要添加项目名，也不需要以 `/`开头。

到此为止，我们启动服务器之后，直接在浏览器地址栏上输入 `http://localhost:8080/dept`即可访问部门管理系统了。

---

## 每个操作页显示用户名

添加 `common.css`文件到 `/css`目录下：

```css
.user-info {
    display: flex;
    justify-content: flex-end;
    align-items: center;
    padding: 10px 0;
    margin-bottom: 10px;
    border-bottom: 1px solid #ddd;
}
.user-name {
    margin-right: 15px;
    color: #555;
    font-weight: 600;
}
.user-actions a {
    color: #777;
    text-decoration: none;
    font-size: 14px;
    margin-left: 10px;
}
.user-actions a:hover {
    color: #333;
    text-decoration: underline;
}
```

在 `add.html`、`list.html`、`edit.html`、`detail.html`的 `<div class="container">`和 `<div class="header">`之间添加以下代码：

```html
<!-- 新增的用户信息栏 -->
<div class="user-info">
  <span class="user-name">当前用户：管理员</span>
  <div class="user-actions">
    <a href="#">退出登录</a>
  </div>
</div>
```

在 `add.html`、`list.html`、`edit.html`、`detail.html`中添加 `common.css`样式：

```html
<link rel="stylesheet" th:href="@{/css/common.css}">
```

效果如下：

![](https://cdn.nlark.com/yuque/0/2025/png/21376908/1749525110958-94f1914a-070c-4cac-a5ad-8f7c872080b4.png)

用户登录成功后，将用户名存储到 session 作用域中了，因此在 html 页面中使用 `${session.username}`取出当前登录的用户名，替换掉页面中的 `管理员`：

```html
<span class="user-name" th:text="|当前用户：${session.username}|"></span>
```

最终效果如下：

![](https://cdn.nlark.com/yuque/0/2025/png/21376908/1749525457096-16dd2be4-c0ee-465a-aae7-a01bfb818c32.png)

---

## 退出系统

用户点击退出系统时，后端应该销毁 session。

修改 退出系统 链接的请求路径：

```html
<a th:href="@{/logout}">退出登录</a>
```

编写 Servlet 销毁 session，重定向到登录页面：

```java
package com.jkweilai.dept.servlets;

import jakarta.servlet.ServletException;
import jakarta.servlet.annotation.WebServlet;
import jakarta.servlet.http.HttpServlet;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.servlet.http.HttpSession;

import java.io.IOException;

@WebServlet("/logout")
public class LogoutServlet extends HttpServlet {
    @Override
    protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        HttpSession session = request.getSession(false);
        if (session != null) {
            session.invalidate();
        }
        response.sendRedirect(request.getContextPath() + "/index");
    }
}

```

测试一下，用户点击退出系统后，是否还可以在浏览器地址栏上直接输入 `http://localhost:8080/dept/list`访问部门列表页面，如果跳转到登录页面则表示正常。

---

## Cookie&Token 机制

### cookie机制及其作用

**cookie**是Web开发中用于在客户端存储少量数据的一种机制，由服务器发送到用户浏览器并保存在本地，当浏览器再次访问同一服务器时会将Cookie数据回传给服务器。

**cookie的特点**：

+ 存储在客户端（浏览器）
+ 大小限制（通常4KB左右）
+ 每个域名下的 cookie 数量有限制（通常20-50个）
+ 可以设置过期时间（不设置有效期时，默认 cookie 保存在浏览器缓存中，浏览器关闭后 cookie 消失，设置有效期 > 0 时 cookie 会被保存在客户端硬盘文件中）
+ 可以被用户禁用（浏览器可以设置禁止接收 cookie，服务器还是会响应 cookie，但浏览器可以拒绝接收）

### cookie的应用场景

1. **用户登录状态保持**：记住登录状态，避免频繁登录
2. **购物车功能**：存储用户选择的商品信息
3. **个性化设置**：保存用户的语言、主题等偏好
4. **广告定向投放**：根据用户兴趣展示相关广告
    1. 当用户访问网站时，你可以设置一个或多个 cookies来存储用户的兴趣信息。例如，如果网站是关于时尚的，你可以设置一个名为interest_fashion的 cookie
5. **跨页面数据传递**：在多个页面间共享数据
    1. 假设创建了一个 cookie 存储了一些共享数据 data，并且让 cookie 关联请求路径，假设关联的请求路径是 `/dept`，那么 `/dept/list`、`/dept/save`等请求路径浏览器都会发送 cookie 数据给服务器，这样多个 Servlet 之间可以共享数据，进而完成跨页面数据传递

### session 和 cookie 的区别

| ****特性**** | ****cookie**** | ****session**** |
| --- | --- | --- |
| **存储位置** | **客户端** | **服务器端** |
| **安全性** | **较低** | **较高** |
| **存储大小** | **有限（约4KB）** | **较大（取决于服务器）** |
| **生命周期** | **可设置长期有效** | **通常较短（会话期间）** |
| **性能影响** | **每次请求都会携带** | **只在服务器端查找** |

### 在JavaWeb中创建和响应Cookie

#### 创建Cookie

```java
// 创建一个名为"username"，值为"john"的Cookie
Cookie cookie = new Cookie("username", "john");
```

cookie 的 name 和 value 要求必须是 String 类型。

#### 设置Cookie属性

```java
// 设置过期时间（秒），不设置则默认为会话Cookie（浏览器关闭即删除）
cookie.setMaxAge(60 * 60 * 24 * 7); // 一周后过期

// 设置路径，以下代码的作用是：当浏览器发送的请求路径是/myapp或者/myapp下的子路径时，都会发送该cookie给服务器。
cookie.setPath("/myapp"); 

// 设置域名（可以跨子域共享）
// 主域名：example.com
// 子域名：api.example.com、shop.example.com
// 不设置域名时，Cookie 仅对 当前完整域名 生效，不包括子域名。
// 显式设置域名时，只能设置为 当前域名或其父级主域名，不能是其他无关域名。
// 一句话：Cookie 永远被限制在它的主域名及子域名下，无法“越狱”！
// cookie.setDomain(".example.com");

// 如果网站使用的协议是HTTPS协议，应该执行以下代码，这样的话，只有发送HTTPS请求时，cookie才会提交给服务器。
// cookie.setSecure(true);

// 设置HttpOnly属性，有效减少XSS攻击
// HttpOnly 标记的 Cookie 只能由浏览器通过 HTTP(S) 请求发送到服务器，JavaScript 无法访问它，因此即使存在 XSS，攻击者也无法直接窃取这类 Cookie。
cookie.setHttpOnly(true);
```

#### 响应Cookie到客户端

```java
response.addCookie(cookie);
```

### 服务器端获取客户端提交的 Cookie

```java
// 从请求中获取所有Cookie
Cookie[] cookies = request.getCookies();

if (cookies != null) {
    for (Cookie cookie : cookies) {
        String name = cookie.getName(); // 获取Cookie的名字
        String value = cookie.getValue(); // 获取Cookie的值
        // 处理Cookie数据
        if ("username".equals(name)) {
            System.out.println("用户名: " + value);
        }
    }
}
```

### cookie的注意事项

1. **安全性问题**：
    - 敏感信息不应存储在Cookie中，即使密码是经过加密的也不要存储在 Cookie 中
    - 使用HttpOnly和Secure标志增强安全性
    - 考虑对Cookie值进行加密
2. **编码问题**：Cookie的值不能包含****空格、分号、逗号****等特殊字符，需要对特殊字符进行URL编码

```java
Cookie cookie = new Cookie("test", URLEncoder.encode("含有特殊字符的值", "UTF-8"));
```

3. **用 Java 程序删除Cookie**：

```java
Cookie cookie = new Cookie("username", "");
cookie.setMaxAge(0); // 立即过期
cookie.setPath("/"); // 必须与要删除的Cookie的路径一致
response.addCookie(cookie);
```

4. **跨域问题**：Cookie不能跨域共享，可以通过设置domain属性实现子域共享。

### 实现"记住我"功能

实现思路：登录成功后，应该创建 Cookie，Cookie 中保存登录的用户名，然后将 Cookie 响应给浏览器。下一次浏览器发送请求时就会携带 Cookie，服务器接收浏览器提交的 Cookie 后，获取 Cookie 中是否有登录的用户名，如果存在则表示已登录，如果不存在则跳转到登录页面。另外，实现了“记住我”这个功能后，用户关闭浏览器，再打开浏览器访问系统时就不需要登录了，所以 IndexServlet 程序也需要改动。因此要编写三部分代码：

1. `LoginServlet`中登录成功后，创建 Cookie，Cookie 中保存登录的用户名，然后响应 Cookie 到浏览器。
2. `CheckLoginFilter`中，获取浏览器提交的 Cookie，并且查看 Cookie 中是否保存了登录的用户名，如果有则创建 session，将登录名存储到 session 中，如果没有则跳转到登录页面。
3. `IndexServlet`中，获取浏览器提交的 Cookie，并且查看 Cookie 中是否保存了登录的用户名，如果有则创建 session，将登录名存储到 session 中，如果没有则跳转到登录页面。

```java
package com.jkweilai.dept.servlets;

import com.jkweilai.dept.utils.Argon2PasswordUtil;
import com.jkweilai.dept.utils.DbUtils;
import jakarta.servlet.ServletException;
import jakarta.servlet.annotation.WebServlet;
import jakarta.servlet.http.*;

import java.io.IOException;
import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;

@WebServlet("/login")
public class LoginServlet extends HttpServlet {
    @Override
    protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        // 获取用户名和密码
        String username = request.getParameter("username");
        String password = request.getParameter("password");
        // 连接数据库校验用户名和密码
        Connection conn = null;
        PreparedStatement ps = null;
        ResultSet rs = null;
        boolean loginSuccess = false;
        try {
            conn = DbUtils.getConnection();
            String sql = "select password from t_user where username = ?";
            ps = conn.prepareStatement(sql);
            ps.setString(1, username);
            rs = ps.executeQuery();
            if(rs.next()) {
                String hashPassword = rs.getString("password");
                if(Argon2PasswordUtil.verifyPassword(password, hashPassword)) {
                    // 登录成功
                    loginSuccess = true;
                    // 创建session对象，存储用户登录的信息
                    HttpSession session = request.getSession();
                    session.setAttribute("username", username);
                    
                    // 创建Cookie，将登录名存储到Cookie中，响应到浏览器
                    Cookie cookie = new Cookie("username", username);
                    cookie.setMaxAge(60 * 60 * 24 * 30); // 30天有效
                    cookie.setPath(request.getContextPath());
                    cookie.setHttpOnly(true);
                    if(request.isSecure()){
                        cookie.setSecure(true);
                    }
                    response.addCookie(cookie);
                    
                    // 重定向到部门列表
                    response.sendRedirect(request.getContextPath() + "/list");
                }
            }
        } catch (Exception e) {
            e.printStackTrace();
        } finally {
            DbUtils.close(conn, ps, rs);
        }
        // 登录失败，转发到登录页面
        if(!loginSuccess) {
            request.setAttribute("errorMsg", "用户名不存在或密码错误！");
            request.setAttribute("template", "index");
            request.getRequestDispatcher("/view").forward(request, response);
        }
    }
}
```

在 `LoginServlet`中添加的代码是：

![](https://cdn.nlark.com/yuque/0/2025/png/21376908/1749689769680-72e0f8df-7e65-41a3-adea-4bb11ad98430.png)

```java
package com.jkweilai.dept.filters;

import jakarta.servlet.*;
import jakarta.servlet.annotation.WebFilter;
import jakarta.servlet.http.Cookie;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.servlet.http.HttpSession;

import java.io.IOException;

// 所有请求路径都经过这个过滤器
@WebFilter("/*")
public class CheckLoginFilter implements Filter {

    @Override
    public void doFilter(ServletRequest req, ServletResponse resp, FilterChain chain) throws IOException, ServletException {
        HttpServletRequest request = (HttpServletRequest) req;
        HttpServletResponse response = (HttpServletResponse) resp;

        // 获取客户端的Cookie，如果有名字为 username 的Cookie
        // 将该Cookie的value取出（用户的登录名），存储到session中
        // 表示该用户已登录
        Cookie[] cookies = request.getCookies();
        if(cookies != null) {
            for(Cookie cookie : cookies) {
                if(cookie.getName().equals("username")) {
                    String username = cookie.getValue();
                    request.getSession().setAttribute("username", username);
                    chain.doFilter(request, response);
                    return;
                }
            }
        }

        HttpSession session = request.getSession(false);
        String servletPath = request.getServletPath();
        if ("/index".equals(servletPath) || "/login".equals(servletPath) || servletPath.startsWith("/css") || (session != null && session.getAttribute("username") != null)) {
            chain.doFilter(req, resp);
        } else {
            response.sendRedirect(request.getContextPath() + "/index");
        }
    }
}
```

`CheckLoginFilter`过滤器中添加的代码如下：

![](https://cdn.nlark.com/yuque/0/2025/png/21376908/1749690017973-06ecca62-c95f-4396-bc1d-824f27a6ab59.png)

`IndexServlet`程序修改如下：

```java
package com.jkweilai.dept.servlets;

import jakarta.servlet.ServletException;
import jakarta.servlet.annotation.WebServlet;
import jakarta.servlet.http.Cookie;
import jakarta.servlet.http.HttpServlet;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

import java.io.IOException;

@WebServlet("/index")
public class IndexServlet extends HttpServlet {
    @Override
    protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {

        boolean isLogin = false;
        Cookie[] cookies = request.getCookies();
        if(cookies != null) {
            for(Cookie cookie : cookies) {
                if(cookie.getName().equals("username")) {
                    isLogin = true;
                    String username = cookie.getValue();
                    request.getSession().setAttribute("username", username);
                    request.setAttribute("template", "list");
                    response.sendRedirect(request.getContextPath() + "/list");
                }
            }
        }

        if(!isLogin) {
            request.setAttribute("template", "index");
            request.getRequestDispatcher("/view").forward(request, response);
        }
        
    }
}

```

到此“记住我”功能基本上实现了。大家可以自行测试一下。

以上“记住我”功能存在的问题包括：

1. ****安全性问题******：直接存储用户名在Cookie中，容易被窃取或伪造。一旦被窃取或伪造，对于后端系统来说，用户名是长期有效且不可变的，攻击者可以长期冒充用户。**
2. ****容易导致越权访问******：如果系统仅依赖 Cookie 中的用户名做身份认证，攻击者******伪造 Cookie 即可登录任意账号******。而且还可以把**`****username=admin****`**改成**`****username=root****`**，可能直接获得管理员权限。**
3. ****敏感信息暴露******：将明文用户名存储在客户端Cookie中，可能违反隐私保护原则。**
4. ****密码未参与验证******：记住我功能通常应该重新验证密码，而不仅仅是依赖Cookie。**
5. ****无法应对数据泄露******：如果数据库泄露，攻击者拿到所有用户名，可以直接构造恶意 Cookie，而******服务器无法区分合法和非法请求******。**
6. ****CSRF防护不足******：虽然设置了HttpOnly，但没有其他CSRF防护措施。**

**更安全的做法是生成一个随机令牌（token）存储在数据库（或者存储在 redis 缓存中），并与用户关联，同时在Cookie中只存储这个令牌值。**

****因此，你需要将之前实现的“记住我”功能添加的所有代码全部删除。我们将使用 Token 令牌来实现“记住我”功能。****

### Token 令牌

实现“记住我”功能，采用 Cookie 中存储 Token 令牌要比直接存储用户名安全的多。

#### 什么是 Token 令牌
**Token是一种代表用户身份和权限的凭证，它是在用户成功登录后由服务器生成并返回给客户端的一串随机字符串。客户端在后续请求中携带这个Token来证明自己的身份，而无需每次都发送用户名和密码。**

#### Token 的工作流程
1. **客户端发送登录请求**
2. **服务器验证用户名和密码，生成Token，Token 和用户 id 关联存储到数据库表中，然后将 Token 响应给客户端**
3. **客户端存储Token（通常在localStorage或cookie中）**
4. **后续请求携带Token**
5. **服务器验证Token并处理请求**

#### Token 为什么更安全
| ****方案**** | ****直接存储用户名**** | ****存储 Token**** |
| --- | --- | --- |
| ****是否可伪造**** | **✅****是（直接改 Cookie）** | **❌****否（需猜中随机 Token）** |
| ****是否可撤销**** | **❌****否（除非改用户名）** | **✅****是（服务器可删除 Token）** |
| ****有效期控制**** | **❌****永久有效** | **✅****可设置过期时间** |
| ****泄露风险**** | **🔴****高风险（用户名固定）** | **🟢****低风险（Token 无意义）** |
| ****适用场景**** | **❌****不推荐** | **✅****推荐（行业标准）** |

+ ****直接存用户名******：相当于把家门钥匙放在门口地毯下，谁找到都能用。**
+ ****存 Token******：相当于使用一次性密码锁，钥匙可随时更换，即使被拿到也很快失效。**

#### Token 的生成算法

```java
package com.jkweilai.dept.utils;

import java.security.SecureRandom;
import java.util.Base64;

public class TokenGenerator {

    // 生成一个安全的随机 Token（Base64 编码）
    public static String generateSecureToken() {
        SecureRandom secureRandom = new SecureRandom();
        byte[] tokenBytes = new byte[32]; // 32字节 = 256位（足够安全）
        secureRandom.nextBytes(tokenBytes); // 填充随机字节
        return Base64.getUrlEncoder().withoutPadding().encodeToString(tokenBytes);
    }

}
```

+ **使用******256 位随机数******（32字节），暴力破解几乎不可能。**
+ `****Base64****`**编码后无**`****+/=****`**等特殊字符。**

### 用 Token 实现“记住我”功能

#### Token 表的设计

```sql
CREATE TABLE `user_remember_tokens` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` bigint NOT NULL COMMENT '关联的用户ID',
  `token` varchar(64) NOT NULL COMMENT '随机生成的token',
  `series` varchar(64) NOT NULL COMMENT '序列标识(安全增强)',
  `fingerprint` varchar(255) DEFAULT NULL COMMENT '客户端指纹(IP+UserAgent哈希)',
  `created_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `expires_at` datetime NOT NULL COMMENT '过期时间',
  `revoked` tinyint(1) NOT NULL DEFAULT '0' COMMENT '是否已撤销',
  PRIMARY KEY (`id`),
  UNIQUE KEY `uniq_series` (`series`),
  KEY `idx_user_token` (`user_id`,`token`),
  KEY `idx_expires` (`expires_at`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='用户持久登录token表';
```

+ **series 机制**：**每个浏览器生成唯一的series标识，每次更新token时保留series但更换token，如果发现相同series但不同token，可能是token被盗。**

```java
String series = UUID.randomUUID().toString();
```

+ **fingerprint 机制（客户端指纹）**：

```java
String ip = request.getRemoteAddr();
String userAgent = request.getHeader("User-Agent");
String fingerprint = DigestUtils.sha256Hex(ip + userAgent + "salt");
```

以上代码需要这个 jar 包：![](https://cdn.nlark.com/yuque/0/2025/png/21376908/1749699237786-870af075-9760-4644-aa7b-0543bbf1100a.png)，添加到 WEB-INF/lib 目录下，并且添加到 classpath 中。

**Apache Commons Codec 是一个用于编码和解码的Java库，提供常用的编码器如Base64、Hex、URL等**

#### 代码的实现
实现思路：

1. 用户登录成功后：【在 LoginServlet 中编写代码】
    1. 生成 Token，Token 关联用户 id 存储到 user_remember_tokens 表。
    2. 将 Token 放到 Cookie 中响应给浏览器。
    3. 将用户名存储到 session 中 。
2. 验证 Token：【在 CheckLoginFilter 中编写代码】
    1. 获取客户端提交的 Cookie，从 Cookie 中获取 Token
    2. 连接数据库验证 Token 是否有效：
        1. 有效，登录成功，将用户名存储到 session 中，展示部门列表
        2. 无效，删除客户端 Token，将数据库 Token 的 revoked 设置为 1， 跳转到登录页面
3. 当用户登录过之后，用户再次发送 `http://localhost:8080/dept`请求时，应该展示部门列表页面：【在 IndexServlet 中编写代码】
    1. 先看 session 中有没有用户名，如果有则直接显示部门列表。
    2. 如果 session 中没有用户名，则获取客户端提交的 Token。
    3. 连接数据库验证 Token 是否有效：
        1. 有效，登录成功，将用户名存储到 session 中，展示部门列表
        2. 无效，删除客户端 Token，将数据库 Token 的 revoked 设置为 1，跳转到登录页面

`LoginServlet`的代码：

```java
package com.jkweilai.dept.servlets;

import com.jkweilai.dept.utils.Argon2PasswordUtil;
import com.jkweilai.dept.utils.DbUtils;
import com.jkweilai.dept.utils.TokenGenerator;
import jakarta.servlet.ServletException;
import jakarta.servlet.annotation.WebServlet;
import jakarta.servlet.http.*;
import org.apache.commons.codec.digest.DigestUtils;

import java.io.IOException;
import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.Timestamp;
import java.time.LocalDateTime;
import java.util.UUID;

@WebServlet("/login")
public class LoginServlet extends HttpServlet {
    @Override
    protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        // 获取用户名和密码
        String username = request.getParameter("username");
        String password = request.getParameter("password");
        // 连接数据库校验用户名和密码
        Connection conn = null;
        PreparedStatement ps = null;
        ResultSet rs = null;
        PreparedStatement ps2 = null;
        boolean loginSuccess = false;
        try {
            conn = DbUtils.getConnection();
            String sql = "select id,password from t_user where username = ?";
            ps = conn.prepareStatement(sql);
            ps.setString(1, username);
            rs = ps.executeQuery();
            if(rs.next()) {
                String hashPassword = rs.getString("password");
                if(Argon2PasswordUtil.verifyPassword(password, hashPassword)) {
                    // 登录成功
                    loginSuccess = true;

                    // ===============================================================================================
                    // 生成Token
                    String token = TokenGenerator.generateSecureToken();
                    // 保存Token到数据库
                    String insertTokenSql = "insert into user_remember_tokens(id,user_id,token,series,fingerprint,expires_at) values(null,?,?,?,?,?)";
                    ps2 = conn.prepareStatement(insertTokenSql);
                    ps2.setString(1, rs.getString("id"));
                    ps2.setString(2, token);
                    String series = UUID.randomUUID().toString();
                    ps2.setString(3, series);
                    String ip = request.getRemoteAddr();
                    String userAgent = request.getHeader("User-Agent");
                    String fingerprint = DigestUtils.sha256Hex(ip + userAgent + "salt");
                    ps2.setString(4, fingerprint);
                    LocalDateTime expiresAt = LocalDateTime.now().plusDays(30);
                    ps2.setTimestamp(5, Timestamp.valueOf(expiresAt)); // 30天有效
                    ps2.executeUpdate();
                    // 响应Token到浏览器
                    Cookie cookie = new Cookie("token", token);
                    cookie.setMaxAge(60 * 60 * 24 * 30); // 30天有效
                    cookie.setPath(request.getContextPath());
                    cookie.setHttpOnly(true);
                    if(request.isSecure()){
                        cookie.setSecure(true);
                    }
                    response.addCookie(cookie);
                    // ===============================================================================================

                    // 创建session对象，存储用户登录的信息
                    HttpSession session = request.getSession();
                    session.setAttribute("username", username);
                    // 重定向到部门列表
                    response.sendRedirect(request.getContextPath() + "/list");
                }
            }
        } catch (Exception e) {
            e.printStackTrace();
        } finally {
            DbUtils.close(null, ps2, null);
            DbUtils.close(conn, ps, rs);
        }
        // 登录失败，转发到登录页面
        if(!loginSuccess) {
            request.setAttribute("errorMsg", "用户名不存在或密码错误！");
            request.setAttribute("template", "index");
            request.getRequestDispatcher("/view").forward(request, response);
        }
    }
}
```

`CheckLoginFilter`代码的实现：

```java
package com.jkweilai.dept.filters;

import com.jkweilai.dept.utils.DbUtils;
import jakarta.servlet.*;
import jakarta.servlet.annotation.WebFilter;
import jakarta.servlet.http.Cookie;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.servlet.http.HttpSession;
import org.apache.commons.codec.digest.DigestUtils;

import java.io.IOException;
import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;

// 所有请求路径都经过这个过滤器
@WebFilter("/*")
public class CheckLoginFilter implements Filter {

    @Override
    public void doFilter(ServletRequest req, ServletResponse resp, FilterChain chain) throws IOException, ServletException {
        HttpServletRequest request = (HttpServletRequest) req;
        HttpServletResponse response = (HttpServletResponse) resp;
        HttpSession session = request.getSession(false);
        String servletPath = request.getServletPath();
        if ("/index".equals(servletPath) || "/login".equals(servletPath) || servletPath.startsWith("/css") || (session != null && session.getAttribute("username") != null)) {
            chain.doFilter(req, resp);
        } else {
            // 看看客户端是否提交Token，并且Token是否有效，如果有效登录成功，创建session存储用户名，无效则删除客户端Token并跳转到登录页面
            boolean isLogin = false;
            Cookie[] cookies = request.getCookies();
            if (cookies != null) {
                for (Cookie cookie : cookies) {
                    if ("token".equals(cookie.getName())) {
                        String token = cookie.getValue();
                        // 验证token是否有效
                        Connection conn = null;
                        PreparedStatement ps = null;
                        PreparedStatement ps2 = null;
                        ResultSet rs = null;
                        try {
                            conn = DbUtils.getConnection();
                            String sql = "select u.username from user_remember_tokens urt join t_user u on urt.user_id=u.id where urt.token=? and urt.fingerprint=? and urt.expires_at > now() and urt.revoked = '0'";
                            ps = conn.prepareStatement(sql);
                            ps.setString(1, token);
                            String ip = request.getRemoteAddr();
                            String userAgent = request.getHeader("User-Agent");
                            String fingerprint = DigestUtils.sha256Hex(ip + userAgent + "salt");
                            ps.setString(2, fingerprint);
                            rs = ps.executeQuery();
                            if (rs.next()) {
                                isLogin = true;
                                HttpSession newSession = request.getSession(true);
                                newSession.setAttribute("username", rs.getString("username"));
                                chain.doFilter(request, response);
                            } else {
                                // 将数据库中token的revoked设置为1
                                String sql2 = "update user_remember_tokens set revoked=1 where token=?";
                                ps2 = conn.prepareStatement(sql2);
                                ps2.setString(1, token);
                                ps2.executeUpdate();
                                // 删除客户端Token
                                Cookie deletedCookie = new Cookie("token", token);
                                deletedCookie.setMaxAge(0);
                                response.addCookie(deletedCookie);
                            }
                        } catch (Exception e) {
                            e.printStackTrace();
                        } finally {
                            DbUtils.close(null, ps2, null);
                            DbUtils.close(conn, ps, rs);
                        }
                    }
                }
            }
            if (!isLogin) {
                response.sendRedirect(request.getContextPath() + "/index");
            }
        }
    }
}
```

`IndexServlet`的代码：

```java
package com.jkweilai.dept.servlets;

import com.jkweilai.dept.utils.DbUtils;
import jakarta.servlet.ServletException;
import jakarta.servlet.annotation.WebServlet;
import jakarta.servlet.http.*;
import org.apache.commons.codec.digest.DigestUtils;

import java.io.IOException;
import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;

@WebServlet("/index")
public class IndexServlet extends HttpServlet {
    @Override
    protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        HttpSession session = request.getSession(false);
        if (session != null && session.getAttribute("username") != null) {
            response.sendRedirect(request.getContextPath() + "/list");
        } else {
            // 看看客户端是否提交Token，并且Token是否有效，如果有效登录成功，创建session存储用户名，无效则删除客户端Token并跳转到登录页面
            boolean isLogin = false;
            Cookie[] cookies = request.getCookies();
            if (cookies != null) {
                for (Cookie cookie : cookies) {
                    if ("token".equals(cookie.getName())) {
                        String token = cookie.getValue();
                        // 验证token是否有效
                        Connection conn = null;
                        PreparedStatement ps = null;
                        PreparedStatement ps2 = null;
                        ResultSet rs = null;
                        try {
                            conn = DbUtils.getConnection();
                            String sql = "select u.username from user_remember_tokens urt join t_user u on urt.user_id=u.id where urt.token=? and urt.fingerprint=? and urt.expires_at > now() and urt.revoked = '0'";
                            ps = conn.prepareStatement(sql);
                            ps.setString(1, token);
                            String ip = request.getRemoteAddr();
                            String userAgent = request.getHeader("User-Agent");
                            String fingerprint = DigestUtils.sha256Hex(ip + userAgent + "salt");
                            ps.setString(2, fingerprint);
                            rs = ps.executeQuery();
                            if (rs.next()) {
                                isLogin = true;
                                HttpSession newSession = request.getSession(true);
                                newSession.setAttribute("username", rs.getString("username"));
                                response.sendRedirect(request.getContextPath() + "/list");
                            } else {
                                // 将数据库中token的revoked设置为1
                                String sql2 = "update user_remember_tokens set revoked=1 where token=?";
                                ps2 = conn.prepareStatement(sql2);
                                ps2.setString(1, token);
                                ps2.executeUpdate();
                                // 删除客户端Token
                                Cookie deletedCookie = new Cookie("token", token);
                                deletedCookie.setMaxAge(0);
                                response.addCookie(deletedCookie);
                            }
                        } catch (Exception e) {
                            e.printStackTrace();
                        } finally {
                            DbUtils.close(null, ps2, null);
                            DbUtils.close(conn, ps, rs);
                        }
                    }
                }
            }
            if (!isLogin) {
                request.setAttribute("template", "index");
                request.getRequestDispatcher("/view").forward(request, response);
            }
        }
    }
}

```

### 退出系统清除 Token 

退出系统时，应该删除客户端的 token，并且将数据库中的 token 撤销掉（revoked 设置为 1）。

`LogoutServlet`的代码修改如下：

```java
package com.jkweilai.dept.servlets;

import com.jkweilai.dept.utils.DbUtils;
import jakarta.servlet.ServletException;
import jakarta.servlet.annotation.WebServlet;
import jakarta.servlet.http.*;

import java.io.IOException;
import java.sql.Connection;
import java.sql.PreparedStatement;

@WebServlet("/logout")
public class LogoutServlet extends HttpServlet {
    @Override
    protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        HttpSession session = request.getSession(false);
        if (session != null) {
            session.invalidate();
        }

        Cookie[] cookies = request.getCookies();
        if (cookies != null) {
            for (Cookie cookie : cookies) {
                if (cookie.getName().equals("token")) {
                    String token = cookie.getValue();
                    // 将数据库表中token的revoked设置为1
                    Connection conn = null;
                    PreparedStatement ps = null;
                    try {
                        conn = DbUtils.getConnection();
                        String sql = "update user_remember_tokens set revoked = 1 where token=?";
                        ps = conn.prepareStatement(sql);
                        ps.setString(1, token);
                        ps.executeUpdate();
                    } catch (Exception e) {
                        e.printStackTrace();
                    } finally {
                        DbUtils.close(conn, ps, null);
                    }
                    // 删除客户端Token
                    Cookie newCookie = new Cookie("token", token);
                    newCookie.setMaxAge(0);
                    response.addCookie(newCookie);
                }
            }
        }

        response.sendRedirect(request.getContextPath() + "/index");
    }
}
```

### 最佳实践建议

1. ****限制每个用户的token数量******：实际上就是控制登录的设备**

```sql
-- 创建token前检查
SELECT COUNT(*) FROM user_remember_tokens WHERE user_id = ? AND revoked = 0 AND expires_at > NOW();
```

2. ****定期维护******：定期清理已撤销或已过期的 token**

```sql
-- 清理过期token（可设置定时任务）
DELETE FROM user_remember_tokens WHERE expires_at < NOW() OR revoked = 1;
```

3. ****敏感操作保护******：**
+ **修改密码/邮箱等敏感操作后立即撤销所有remember token**
+ **重要操作（如支付）要求重新输入密码**
