# Spring Security快速入门

**官方文档：**[https://docs.spring.io/spring-security/reference/index.html](https://docs.spring.io/spring-security/reference/index.html)

**先来记住几个单词：**

1. `authenticate`**：动词，认证。（登录的动作）**
2. `authentication`**：名词，凭证。（登录成功得到的入场券，凭证中含有**权限列表**）**
3. `authority`**：名词，权限。**
4. `authorize`**：动词，授权。**

## Spring Security 能做什么

+ 身份认证：身份认证是验证`谁正在访问系统资源`，判断用户是否为合法用户。认证用户的常见方式是要求用户输入用户名和密码。
+ 授权：用户进行身份认证后，系统会控制`谁能访问哪些资源`，这个过程叫做授权。用户无法访问没有权限的资源。

**防御常见攻击**

## 身份认证（authentication）
**官方代码示例：**[https://github.com/spring-projects/spring-security-samples/tree/main](https://github.com/spring-projects/spring-security-samples/tree/main)

### 创建Spring Boot项目
创建 Spring Boot 项目，项目名为：`spring-security-demo`

JDK 版本采用：`21`

SpringBoot 版本采用：`3.5.6`，它自动依赖的 `Spring Security`版本是 `6.5.5`

创建项目过程中选择这些依赖：`web`、`security`、`thymeleaf`

### 创建IndexController
```java
package com.jkweilai.spring.security.demo.controller;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;

@Controller
public class IndexController {

    @GetMapping("/")
    public String index(){
        return "home";
    }
}

```

### 创建 home.html
在 `templates`目录下新建 `home.html`，并编写以下代码：

```html
<!DOCTYPE html>
<html lang="en" xmlns:th="https://www.thymeleaf.org">
<head>
  <meta charset="UTF-8">
  <title>这是一个受Spring Security保护的资源</title>
</head>
<body>
<h1>你好，Spring Security！</h1>
<!-- 注意:Spring Security中自动为我们提供了 /logout 请求的默认处理流程-->
<a th:href="@{/logout}">退出系统</a>
</body>
</html>
```

### 启动项目测试
访问地址：[http://localhost:8080/](http://localhost:8080/)，浏览器自动跳转到登录页面：[http://localhost:8080/login](http://localhost:8080/login)

**Spring Security 默认提供了一个用户：**`user`

密码在启动项目时的控制台上可以查看，如下图所示：

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1758891473687-e95e00f3-e8b8-42d2-b9fc-b64fa114a65f.png" width="865.3333333333334" title="" crop="0,0,1,1" id="u92ff864f" class="ne-image" style="font-size: 16px">

输入用户名和密码之后，点击 `Sign in`，登录成功，**才会执行受保护的 **`IndexController`，最终跳转到`home.html`，如下图：

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1758891544329-8598fecb-0b23-4355-a986-0edb2a65d6d6.png" width="395.3333333333333" title="" crop="0,0,1,1" id="ue791eb1c" class="ne-image" style="font-size: 16px">

点击退出系统时，会自动跳转到提示页面：

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1758891604109-2496bcdb-29ff-4450-9c21-2b4e4321f55d.png" width="360.6666666666667" title="" crop="0,0,1,1" id="uc82cad9b" class="ne-image" style="font-size: 16px">

点击 `Log Out`后退出系统：

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1758891634303-2b58a95c-7fbc-4ce6-8dee-6e1bff0c015a.png" width="370.6666666666667" title="" crop="0,0,1,1" id="u0ed70ec7" class="ne-image" style="font-size: 16px">

### Spring Security 帮我们做了什么
1. **保护应用程序URL，要求对应用程序的任何交互进行身份验证**
**只要你项目中引入 SpringSecurity 的依赖**。 Spring Security 默认会把你整个网站的所有页面和接口都“锁起来”。任何人想访问，都必须先登录（证明自己是合法用户）。除了少数几个默认的端点（如 /login, /error），其他所有请求路径默认都需要认证。你可以通过配置来改变哪些路径需要认证，哪些可以公开访问。

2. **程序启动时生成一个默认用户：user**

为了方便你第一次启动项目就能登录测试，Spring Security 会自动创建一个临时账户，用户名就叫 user。只要你没有在配置文件（如 application.properties）中指定自己的用户名和密码，这个默认用户就会被创建。

3. **生成一个默认的随机密码，并将此密码记录在控制台上**

每次启动应用密码都会变，所以你必须在程序启动时，去 IDE 的控制台日志里找到它才能登录。

4. **生成默认的登录表单，提供了基于表单的登录，以及注销流程**

它自动给你做了一个非常简单的登录页面（你访问任何受保护的页面都会跳转到这个页面）和一个处理退出的功能。你不需要自己写这两个页面的 HTML 代码。它帮你把“用户输入用户名密码提交登录”和“用户点击退出”这一整套逻辑都做好了。你只需要用就行了。

5. **对于Web请求，重定向到登录页面；对于服务请求，返回401未经授权**

Web请求：比如你在浏览器里直接输入网站地址。如果没登录，它会友好地跳转到登录页面，让你去登录。

服务请求：比如前端 JavaScript 用 Ajax 调用一个后端 API 接口。如果没登录，它不会返回一个 HTML 登录页面（因为前端程序看不懂），而是直接返回一个标准的 HTTP 401 状态码，告诉前端“你未经授权，请先认证”。

6. **防止 CSRF 攻击（跨站请求伪造攻击）（**默认开启**）**

**CSRF 攻击：**

1. 你登录了网银系统，网银系统给你颁发了令牌，令牌存储在浏览器的 cookie 中。
2. 你没有关闭浏览器，在同一个浏览器中，你浏览了其他网站，黑客诱导你点击了某个链接。
3. 这个链接自动向网银发起转账请求，只要请求路径是网银系统的路径，那么请求路径关联的 Cookie 就会自动提交，这是浏览器的默认行为。
4. 因为网银收到了合法 Cookie，网银会认为这是合法的请求，完成向黑客账户的转账。

**Spring Security 的做法**：

1. 它会为**每个表单**生成一个唯一的、随机的“令牌”（Token）。
2. 当提交表单时，必须把这个令牌也一起提交上来。服务器会验证令牌是否正确。

**核心原理：**

1. **Cookie**：浏览器自动带，黑客能用
2. **Spring Security 为表单生成的 Token**：藏在表单里，每次不同，黑客拿不到（**同源策略保护**）
3. **提供了多种安全机制来防御会话相关的攻击（**HttpOnly 默认开启,Secure 非默认开启**）**

**安全的 Cookie 标志**：它会在你的登录凭证 Cookie 上设置 HttpOnly 和 Secure 属性。HttpOnly 能防止 JavaScript 窃取 Cookie，Secure 要求 Cookie 只能在 HTTPS 连接下传输。

8. **写入Strict-Transport-Security以确保HTTPS（**非默认开启的**）**

Spring Security 默认是不开启自动写入Strict-Transport-Security 到响应头的。如果我们在 Spring Security 框架中开启了自动写入Strict-Transport-Security 到响应头。用户通过HTTPS成功访问网站一次，浏览器就会记住"此站点必须使用HTTPS"的规则，后续所有访问（包括HTTP链接）都会自动升级为HTTPS请求。

9. **写入X-Content-Type-Options以处理嗅探攻击（**默认开启**）**

有些浏览器很“热心”，会主动猜测服务器返回内容的类型（比如一个文本文件，浏览器可能会猜它是 HTML 或 JavaScript）。这就有安全风险，攻击者可能利用这个特性执行恶意代码。

**Spring Security 的做法**：通过设置 `X-Content-Type-Options: nosniff` 这个响应头，直接命令浏览器：“别瞎猜！我说这个文件是什么类型，它就是什么类型。” 这样就关闭了浏览器的内容类型猜测行为。

10. **写入Cache Control头来保护经过身份验证的资源（**默认开启**）**

登录后的一些敏感页面**可能被浏览器或中间代理服务器缓存下来**。Spring Security 默认会对这些需要认证的请求加上 `Cache-Control` 头，告诉浏览器和缓存服务器“不要缓存这个页面的内容”。

11. **写入X-Frame-Options以处理**点击劫持**攻击（**默认开启**）**

**点击劫持**就是攻击者把一个透明的、你已登录的网站（如邮箱）用 `<iframe>` 嵌入到他的恶意网页上，然后诱骗你去点击网页上的某个按钮（比如“抽大奖”），实际上你点的是邮箱里的“删除所有邮件”按钮。

1. 你先正常登录了126（有Cookie）
2. 你不关浏览器，点开黑客发给你的链接（比如抽奖活动）
3. 黑客的网页里**偷偷藏了一个透明的126 iframe**
4. 你点"抽奖"按钮，实际点的是iframe里126的"删除邮件"按钮

**Spring Security 的做法**：通过设置 `X-Frame-Options: DENY` 这个响应头，告诉浏览器：“不允许任何网站用 iframe 把我嵌入进去。” 这样就从根本上防止了这种攻击。

## Spring Security 的底层原理
**官方文档：**[**https://docs.spring.io/spring-security/reference/servlet/architecture.html**](https://docs.spring.io/spring-security/reference/servlet/architecture.html)

Spring Security 底层的原理是使用传统的 **Servlet 过滤器**完成的。

### 核心架构：过滤器链(Filter Chain)
<img src="assets/filterchain.png" title="null" crop="0,0,1,1" id="ue5q4" class="ne-image" style="font-size: 16px">

Spring Security 的本质就是一个精心编排的过滤器链，每个过滤器负责特定的安全任务：

```plain
// 简化版的过滤器链顺序
HttpServletRequest
    ↓
→ SecurityContextPersistenceFilter (恢复SecurityContext，作用：避免每次请求都重新认证)
→ WebAsyncManagerIntegrationFilter (集成异步管理，解决异步请求中如何访问SecurityContext)
→ HeaderWriterFilter (写入安全头，如HSTS、X-Frame-Options)
→ CorsFilter (处理跨域)
→ CsrfFilter (CSRF防护)
→ LogoutFilter (处理注销：如果请求是 /logout 则执行注销逻辑)
→ UsernamePasswordAuthenticationFilter (如果请求是 /login 则执行登录认证)
→ AuthorizationFilter (授权检查)
→ ... 其他自定义过滤器 ...
→ 你的业务Controller
    ↓
HttpServletResponse
```

**一个过滤器，一个安全任务，排队执行，就像工厂的流水线一样，每个过滤器只负责自己的"工序"。**

**这种设计的好处：**

1. **单一职责**：每个过滤器只做一件事，代码清晰
2. **灵活组合**：可以根据需要启用/禁用特定过滤器
3. **可插拔**：可以自定义过滤器插入到链中任意位置
4. **灵活控制顺序**：过滤器的执行顺序很关键（比如先认证后授权）

### 核心过滤器 DelegatingFilterProxy
DelegatingFilterProxy：

1. 它本身是一个过滤器，**完全符合 Servlet 规范的过滤器**
2. 它的作用是：负责**“委托”**任务的过滤器。
3. 它是 `**Spring 框架**`提供的，`Spring Security`中使用了它。
4. 它在 Servlet 容器和 Spring 容器之间建立一个桥梁。
5. 它将**后续 Filter 对象的生命周期**交给 Spring 管理，**Servlet 容器不再管理**。

DelegatingFilterProxy 本身不是 Spring Bean，由 Servlet 容器直接实例化和管理的。

<img src="assets/delegatingfilterproxy.png" title="null" crop="0,0,1,1" id="kQHzf" class="ne-image" style="font-size: 16px">

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1758779076411-2c38102d-6014-4123-8296-e003c1f06342.png" width="213.33333333333334" title="" crop="0,0,1,1" id="u5f63c6f9" class="ne-image" style="font-size: 16px">

### 过滤器链的**代理管理器** FilterChainProxy
<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1758779110765-8c1eeacc-78d7-4e09-a0ab-17e0a870fab6.png" width="437.3333333333333" title="" crop="0,0,1,1" id="r8RBy" class="ne-image" style="font-size: 16px">

1. DelegatingFilterProxy 将任务委托给了 Spring 应用程序上下文中的`FilterChainProxy` 类型的 Bean。
2. 它不是一个普通的过滤器，它是Spring Security 自动创建的、非常复杂的 **过滤器链的代理管理器。**



**FilterChainProxy 的两大核心职责：**

**路由选择（Routing）**

+ 根据请求的URL路径、参数等特征选择一个最匹配的`SecurityFilterChain`

**链式执行（Chained Execution）**

+ 获取选中过滤器链中的所有Filter
+ 按配置顺序依次调用每个Filter的`doFilter()`方法
+ 确保整个安全过滤流程的完整执行

**总结 **`FilterChainProxy`**的作用是：**

+ 作为 `Spring Security` 的统一入口，`FilterChainProxy` **根据 URL** **路由**到对应的** 安全过滤器链 **上，然后将这个安全过滤器链上所有的 Filter 按照配置顺序调用一遍。

<img src="https://cdn.nlark.com/yuque/0/2026/png/21376908/1770782598241-ff825215-a1d2-4571-9225-208bfffb0253.png" width="522.7999877929688" title="" crop="0,0,1,1" id="lXFiK" class="ne-image" style="font-size: 16px">

### 过滤器链 SecurityFilterChain
`FilterChainProxy`根据请求的 URL 找到对应的 `SecurityFilterChain`，通过 `SecurityFilterChain`中的 `getFilters()`方法获取一个过滤器列表 `List<Filter>`，然后执行 `List<Filter>`中每一个 `Filter`的 `doFilter()`方法。

<img src="assets/securityfilterchain.png" title="null" crop="0,0,1,1" id="kIkGV" class="ne-image" style="font-size: 16px">

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1758779129742-5f7ee14e-60b7-4b6d-8e8c-ed0eead8a9f5.png" width="457.3333333333333" title="" crop="0,0,1,1" id="uc57635a7" class="ne-image" style="font-size: 16px">



**番外篇**：原理深入（可以选择理解）：`Spring Security`中的安全过滤器链上的每一个过滤器都是符合 Servlet 规范的吗？

答案是：不完全是！ Spring Security 过滤器链上的过滤器**不全是**标准的 Servlet Filter。（有的是，有的不是）



那它底层是怎么执行每一个过滤器的呢？底层是通过它 `VirtualFilterChain`实现的，源码如下：

```java
private static final class VirtualFilterChain implements FilterChain {
    
    private final FilterChain originalChain;          // 原生Servlet过滤器链
    private final List<Filter> additionalFilters;     // Spring Security的过滤器列表
    private final int size;                           // 过滤器数量
    private int currentPosition = 0;                  // 当前执行位置

    // 构造函数：传入原生链和Security过滤器
    private VirtualFilterChain(FilterChain chain, List<Filter> additionalFilters) {
        this.originalChain = chain;
        this.additionalFilters = additionalFilters;
        this.size = additionalFilters.size();         // 缓存大小
    }

    @Override
    public void doFilter(ServletRequest request, ServletResponse response) throws IOException, ServletException {
        // 1. 如果Security过滤器都执行完了 → 执行原生链
        if (this.currentPosition == this.size) {
            this.originalChain.doFilter(request, response);
            return;
        }
        
        // 2. 执行下一个Security过滤器
        this.currentPosition++;
        Filter nextFilter = this.additionalFilters.get(this.currentPosition - 1);
        
        // 日志：正在执行第几个过滤器
        if (logger.isTraceEnabled()) {
            String name = nextFilter.getClass().getSimpleName();
            logger.trace(LogMessage.format("Invoking %s (%d/%d)", name, this.currentPosition, this.size));
        }
        
        // 关键：执行过滤器，并传入this（让过滤器能调用链的下一个）
        nextFilter.doFilter(request, response, this);
    }
}
```

<img src="assets/multi-securityfilterchain-17016804731631.png" title="null" crop="0,0,1,1" id="kjS33" class="ne-image" style="font-size: 16px">

### 总结 Security 底层实现原理
`Security`工作流程如下：

```plain
HTTP请求
    ↓
DelegatingFilterProxy (委托代理)
    ↓
FilterChainProxy (过滤器链代理) ← 选择匹配的过滤器链
    ↓
[SecurityFilterChain1] 或 [SecurityFilterChain2] 或 ... (具体的过滤器链)
    ↓  
[Filter1, Filter2, Filter3, ...] (具体的过滤器序列)
    ↓
业务Servlet
```

## 默认过滤器链
`Spring Security`默认只提供了**一条安全过滤器链**，通过**配置日志**或**断点调试**都可以查看这个**默认的过滤器链**。



`Spring Security`的版本迭代非常快，不同的版本查看效果不同，当前文档中的版本号是：**6.5.5**

### 配置日志
在 `application.properties`中添加以下配置（**实际开发中要去掉，要不然打印日志太多**）：

```yaml
logging.level.org.springframework.security=DEBUG
logging.level.org.springframework.security.web.FilterChainProxy=TRACE
logging.level.org.springframework.security.config=DEBUG
```

然后启动服务器，**复制密码**，清空控制台，访问首页：[http://localhost:8080/](http://localhost:8080/)，查看控制台信息如下（部分截图）：

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1759029451564-41210e49-31aa-4f0d-afea-2a69f288f75d.png" width="726" title="" crop="0,0,1,1" id="uc923deec" class="ne-image" style="font-size: 16px">

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1759029484975-af6bf40a-5791-4f36-9018-b520bbc2d355.png" width="690" title="" crop="0,0,1,1" id="u7585af2c" class="ne-image" style="font-size: 16px">

通过日志信息可以看到 `Spring Security`默认提供的安全过滤器链是 **16 个过滤器**。

另外，可以看到当发送的请求是：`GET /`的时候，`Invoking`了 `16`个过滤器，这说明这 16 个过滤器都被调用了。

但这里需要注意的是：有的过滤器很快就执行结束了，并不会执行过滤器的核心逻辑。

例如`LogoutFilter`虽然被调用了，但由于请求路径不是 `/logout`，因此 `LogoutFilter`会立即执行结束，因此大家不需要担心效率问题。



**另外，**为什么有的请求是执行一个完整的过滤器链，有的则执行部分过滤器链，这个可以提前了解一下：这就是Spring Security的**过滤器链短路机制** - 当某个过滤器能够完全处理请求时（**白话文：经过某个过滤器时请求就处理完了。没必要再往下走了**），后续过滤器不再执行。



控制台中有这样一段日志，我们可以来解析一下这部分日志，初步了解一下这个安全框架：

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1759029985294-18bef568-83a8-4544-87dd-cc98f7cbbe21.png" width="1355" title="" crop="0,0,1,1" id="u745b36bd" class="ne-image" style="font-size: 16px">

### 断点调试
通过断点调试的方式，也可以看到。找到 `DefaultSecurityFilterChain`类，在下图位置添加断点：

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1759030220943-f36e4a18-54d2-478a-b24c-00da10b31c78.png" width="1247" title="" crop="0,0,1,1" id="u498e890e" class="ne-image" style="font-size: 16px">



直接启动项目，启动项目的时候自动就会走到这个断点上，可以清楚的看到默认有 16 个过滤器，如下图：

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1759030275483-fcddcd24-1350-4304-ab4e-cadc38c170e9.png" width="1015" title="" crop="0,0,1,1" id="u8a3575cf" class="ne-image" style="font-size: 16px">

### 16 个过滤器简单说明
:::info
1. DisableEncodeUrlFilter - 禁用URL编码
2. WebAsyncManagerIntegrationFilter - 异步请求支持
3. SecurityContextHolderFilter - 安全上下文管理
4. HeaderWriterFilter - HTTP头信息处理
5. CsrfFilter - CSRF防护
6. LogoutFilter - 退出登录处理
7. UsernamePasswordAuthenticationFilter - 表单登录认证
8. DefaultResourcesFilter - 默认资源处理
9. DefaultLoginPageGeneratingFilter - 默认登录页生成
10. DefaultLogoutPageGeneratingFilter - 默认退出页生成
11. BasicAuthenticationFilter - HTTP基本认证
12. RequestCacheAwareFilter - 请求缓存
13. SecurityContextHolderAwareRequestFilter - 请求包装
14. AnonymousAuthenticationFilter - 匿名用户认证
15. ExceptionTranslationFilter - 异常转换
16. AuthorizationFilter - 授权检查

:::

## SecurityProperties
默认情况下 `Spring Security` 将初始的用户名和密码存到了 `SecurityProperties` 类中。这个类中有一个静态内部类 `User`，配置了默认的用户名（name = "user"）和密码（password = uuid）

<img src="https://cdn.nlark.com/yuque/0/2026/png/21376908/1770784452156-925620f4-bb99-498e-ba02-aa7cf9ccede9.png" width="563.2" title="" crop="0,0,1,1" id="u8f7886f2" class="ne-image" style="font-size: 16px">

我们也可以将用户名、密码配置在SpringBoot的配置文件中：在application.properties中配置自定义用户名和密码

<img src="https://cdn.nlark.com/yuque/0/2026/png/21376908/1770784483444-b9c2ea23-1de2-4f53-ab95-cc9e4ab8aad5.png" width="408" title="" crop="0,0,1,1" id="u34c09cd2" class="ne-image" style="font-size: 16px">

<img src="https://cdn.nlark.com/yuque/0/2026/png/21376908/1770784499814-101c756e-76ca-4616-a142-7a60341c5a25.png" width="506.4" title="" crop="0,0,1,1" id="u61c9011b" class="ne-image" style="font-size: 16px">

```properties
spring.security.user.name=user
spring.security.user.password=123
```

