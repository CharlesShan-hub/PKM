# 前后端分离
在前后端分离的系统中，用户认证成功或者失败不应该渲染页面，应该返回 JSON 给前端系统。

**<font style="color:#DF2A3F;">注意：本章节内容不是完全的前后端分离，只是演示后端如何返回 JSON，如果纯前后端分离，需要 JWT。</font>**

## 用户认证流程
<img src="assets/usernamepasswordauthenticationfilter-16822329079281.png" title="null" crop="0,0,1,1" id="hueEG" class="ne-image" style="font-size: 16px">

**我们来描述一下，在前后端分离系统中，用户认证的流程：**

1. **用户提交登录**
    - 前端 POST 发送 JSON 【`{"username": "admin", "password": "password"}`】到登录接口（如 `/login`）：
2. **认证过滤器拦截**
    - `UsernamePasswordAuthenticationFilter` 拦截请求
    - 将用户名密码封装为 `UsernamePasswordAuthenticationToken`
3. **AuthenticationManager 认证**
    - **调用 **`UserDetailsService.loadUserByUsername(username)` 
    - **使用 **`PasswordEncoder` 校验密码
4. **认证成功**
    - 生成 `Authentication` 对象（**凭证对象**）
    - 存入 `SecurityContextHolder`
    - **调用 **`AuthenticationSuccessHandler` → 返回成功JSON
5. **认证失败**
    - **调用 **`AuthenticationFailureHandler` → 返回错误JSON



**核心是：**

1. 认证成功自动调用：`AuthenticationSuccessHandler`
2. 认证失败自动调用：`AuthenticationFailureHandler`



接下来我们来一步一步实现一下。

## 引入 `fastjson2`
我们肯定是需要对 JSON 进行处理的，因此要引入 `fastjson2`依赖：

```xml
<dependency>
    <groupId>com.alibaba.fastjson2</groupId>
    <artifactId>fastjson2</artifactId>
    <version>2.0.59</version>
</dependency>
```

## 认证成功的响应
编写 `AuthenticationSuccessHandler`接口的实现类，认证成功后，这个接口的 `onAuthenticationSuccess()`方法自动被调用。在该方法中向前端系统响应 JSON。

### 成功结果处理
```java
package com.jkweilai.spring.security.demo.config;

import com.alibaba.fastjson2.JSON;
import jakarta.servlet.ServletException;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.security.core.Authentication;
import org.springframework.security.web.authentication.AuthenticationSuccessHandler;

import java.io.IOException;
import java.util.HashMap;
import java.util.Map;

public class MyAuthenticationSuccessHandler implements AuthenticationSuccessHandler {
    // 认证成功时的回调
    @Override
    public void onAuthenticationSuccess(HttpServletRequest request, HttpServletResponse response, Authentication authentication) throws IOException, ServletException {
        // 获取认证主体（通常是用户标识，如用户名、UserDetails对象）
        Object principal = authentication.getPrincipal();
        // 获取用户权限列表（角色和权限信息）
        //Collection<? extends GrantedAuthority> authorities = authentication.getAuthorities();
        // 获取用户凭证（通常是密码，认证成功后出于安全考虑会清除）
        //Object credentials = authentication.getCredentials();

        // 封装数据
        Map<String, Object> map = new HashMap<>();
        map.put("code", "1");
        map.put("msg", "登录成功");
        map.put("data", principal);

        // 转换JSON
        String json = JSON.toJSONString(map);

        // 响应JSON
        response.setContentType("application/json;charset=UTF-8");
        response.getWriter().print(json);
    }
}

```

### SecurityFilterChain配置
如何让 `Spring Security`找到你这个回调呢？你需要在 `SecurityFilterChain`中进行如下的配置：

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1759319758338-d9f6b0aa-fab9-4feb-919e-a197e5979585.png" width="1000" title="" crop="0,0,1,1" id="u6a76fa44" class="ne-image" style="font-size: 16px">

```java
form.successHandler(new MyAuthenticationSuccessHandler())
```



**测试如下：**

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1759320811494-ffecb514-cf45-4f49-80c5-cd42cdaba161.png" width="488" title="" crop="0,0,1,1" id="u4876a273" class="ne-image" style="font-size: 16px">

## 认证失败的响应
编写 `AuthenticationFailureHandler` 接口的实现类，认证失败后，这个接口的 `onAuthenticationFailure()`方法自动被调用。在该方法中向前端系统响应 JSON。

### 失败结果处理
```java
package com.jkweilai.spring.security.demo.config;

import com.alibaba.fastjson2.JSON;
import jakarta.servlet.ServletException;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.security.core.AuthenticationException;
import org.springframework.security.web.authentication.AuthenticationFailureHandler;

import java.io.IOException;
import java.util.HashMap;
import java.util.Map;

public class MyAuthenticationFailureHandler implements AuthenticationFailureHandler {
    @Override
    public void onAuthenticationFailure(HttpServletRequest request, HttpServletResponse response, AuthenticationException exception) throws IOException, ServletException {
        // 获取异常信息
        String localizedMessage = exception.getLocalizedMessage();

        // 封装数据
        Map<String, Object> map = new HashMap<>();
        map.put("code", "-1");
        map.put("msg", "用户名或密码错误");

        // 转换JSON
        String json = JSON.toJSONString(map);

        // 响应JSON
        response.setContentType("application/json;charset=UTF-8");
        response.getWriter().print(json);
    }
}

```

### SecurityFilterChain配置
如何让 `Spring Security`找到你这个回调呢？你需要在 `SecurityFilterChain`中进行如下的配置：

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1759321148994-cdcebc42-8d9e-40a6-89c7-d07a4fcf2309.png" width="1016" title="" crop="0,0,1,1" id="u860ee54e" class="ne-image" style="font-size: 16px">

```java
form.failureHandler(new MyAuthenticationFailureHandler())
```



**测试如下：**

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1759321197341-f391d8cf-7623-470d-99c8-78d2c17c6a24.png" width="376" title="" crop="0,0,1,1" id="u07afda8e" class="ne-image" style="font-size: 16px">

## 注销的响应
之前注销的时候，会给一个确认页，然后注销之后会自动跳转到登录页。我们如果注销之后希望返回 JSON 字符串给前端系统，那就需要再编写一个回调。编写类实现 `LogoutSuccessHandler`接口，实现该接口中的 `onLogoutSuccess()`方法，在该方法中响应 JSON 到前端系统。

### 首先保证当前注销功能可用
你需要将 csrf 攻击防御功能关闭，这样之前的注销功能才可用：之前的注释去掉即可。

```java
http.csrf(csrf -> {
   csrf.disable();
});
```

### 注销结果处理
```java
package com.jkweilai.spring.security.demo.config;

import com.alibaba.fastjson2.JSON;
import jakarta.servlet.ServletException;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.security.core.Authentication;
import org.springframework.security.web.authentication.logout.LogoutSuccessHandler;

import java.io.IOException;
import java.util.HashMap;
import java.util.Map;

public class MyLogoutSuccessHandler implements LogoutSuccessHandler {
    @Override
    public void onLogoutSuccess(HttpServletRequest request, HttpServletResponse response, Authentication authentication) throws IOException, ServletException {
        // 封装数据
        Map<String,Object> map = new HashMap<>();
        map.put("code", "0");
        map.put("msg", "注销成功");

        // 转换JSON
        String json = JSON.toJSONString(map);

        // 响应JSON
        response.setContentType("application/json;charset=UTF-8");
        response.getWriter().print(json);
    }
}

```

### SecurityFilterChain配置
你仍然需要通过配置来告诉 `Spring Security`，它在哪里。但这一次的配置需要配置在 `http`之下，而不是 `form`之下：

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1759321733366-90093a8a-f892-490c-8cf5-6a3ff4d4c96e.png" width="838" title="" crop="0,0,1,1" id="u85f7fb94" class="ne-image" style="font-size: 16px">

```java
// 也可以不用链式调用，直接使用 http. 调用。
http.logout(logout -> {
    logout.logoutSuccessHandler(new MyLogoutSuccessHandler());
});
```



**测试如下：**

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1759322161331-cc5224f1-c681-4631-af9e-abfc670252fb.png" width="313" title="" crop="0,0,1,1" id="u7d42e66e" class="ne-image" style="font-size: 16px">

## 请求未认证的接口
### 实现AuthenticationEntryPoint接口
当访问一个需要认证之后才能访问的接口的时候，Spring Security会使用`AuthenticationEntryPoint`将用户请求跳转到登录页面。这里我们也希望系统返回一个 JSON，不要跳转到登录页。因此我们又需要编写一个回调。编写类实现 `AuthenticationEntryPoint`接口，实现 `commence()`方法：

```java
package com.jkweilai.spring.security.demo.config;

import com.alibaba.fastjson2.JSON;
import jakarta.servlet.ServletException;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.security.core.AuthenticationException;
import org.springframework.security.web.AuthenticationEntryPoint;

import java.io.IOException;
import java.util.HashMap;
import java.util.Map;

public class MyAuthenticationEntryPoint implements AuthenticationEntryPoint {
    @Override
    public void commence(HttpServletRequest request, HttpServletResponse response, AuthenticationException authException) throws IOException, ServletException {
        // 通过它也可以获取错误信息
        String localizedMessage = authException.getLocalizedMessage();

        // 封装数据
        Map<String,Object> map = new HashMap<>();
        map.put("code", -1);
        map.put("msg", "没有登录");
        map.put("localizedMessage", localizedMessage);

        // 转换JSON
        String json = JSON.toJSONString(map);

        // 响应JSON
        response.setContentType("application/json;charset=UTF-8");
        response.getWriter().print(json);
    }
}

```

### SecurityFilterChain配置
同样，你也需要将这个回调告诉 `Spring Security`在哪里。

```java
http.exceptionHandling(exception -> {
    exception.authenticationEntryPoint(new MyAuthenticationEntryPoint()); // 请求需要认证的接口时
});
```



**测试如下：**

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1759322761231-46d5319e-5705-4d4a-aa91-056f0d731f30.png" width="912" title="" crop="0,0,1,1" id="u1ee64feb" class="ne-image" style="font-size: 16px">

## 跨域
在 `WebSecurityConfig`配置类中添加如下 Bean：

```java
@Bean
public CorsConfigurationSource corsConfigurationSource() {
    CorsConfiguration config = new CorsConfiguration();
    
    // 允许的前端地址（协议+域名+端口）
    config.setAllowedOrigins(Arrays.asList("http://localhost:5173"));
    
    // 允许的HTTP请求方法（必须包含OPTIONS）
    config.setAllowedMethods(Arrays.asList("GET", "POST", "PUT", "DELETE", "OPTIONS"));
    
    // 允许的请求头（*表示全部允许）
    config.setAllowedHeaders(Arrays.asList("*"));
    
    // 允许携带凭证（Cookie等），开启时allowedOrigins不能为*
    config.setAllowCredentials(true);
    
    // 将配置应用到所有接口
    UrlBasedCorsConfigurationSource source = new UrlBasedCorsConfigurationSource();
    source.registerCorsConfiguration("/**", config);
    return source;
}
```

重要的一步（**在安全过滤器链中进行配置**）：启用 CORS 功能，并指定配置源

```java
http.cors(cors -> cors.configurationSource(corsConfigurationSource()))
```

<font style="color:rgb(15, 17, 21);">在 Spring Security 中配置 CORS 后，它会</font>**<font style="color:rgb(15, 17, 21);">在过滤器链的最前端处理跨域请求，优先级高于其他安全过滤器，因此无需再配置 WebMvc 的 CORS</font>**<font style="color:rgb(15, 17, 21);">。</font>

## Controller 中获取用户认证信息
### 身份验证核心概念
<img src="assets/securitycontextholder.png" title="null" crop="0,0,1,1" id="TS30O" class="ne-image" style="font-size: 16px">

Spring Security 框架中，`SecurityContextHolder`、`SecurityContext`、`Authentication`、`Principal` 和 `Credentials` 是与身份验证和授权相关的核心概念。它们之间的关系如下：

1. **SecurityContextHolder**：安全上下文持有者，是安全模型的基石，存储在 ThreadLocal 中，线程安全的。
2. **SecurityContext**：安全上下文。主要作用是包含并管理当前用户的 `Authentication` 对象。
3. **Authentication**：该对象在安全上下文中扮演两个角色：
    - 在**身份验证之前**，它代表用户提交的登录请求，其中包含 `Principal`（通常是用户名）和 `Credentials`（通常是密码）。
    - 在**身份验证之后**，它代表已认证的用户，此时 `Principal` 通常是一个包含更多详细信息的用户对象（如 `UserDetails` 实例），而 `Credentials` 出于安全原因会被清除（通常为 `null`）。此外，它还包含用户的权限信息（`GrantedAuthority` 集合）。
4. **Principal**：通过 `Authentication` 对象的 `getPrincipal()` 方法获取。代表主体的身份标识。认证成功后， 它是一个能够识别用户的实体对象。
5. **Credentials**：代表证明主体身份的凭证，最常见的是密码。**在认证流程完成后，为了安全起见，这个凭证信息通常会被框架从 **`Authentication`** 对象中清除掉**，调用 `getCredentials()` 方法通常返回 `null`。（密码可以被存储，可以被用于比较，不可用于返回前端）
6. **GrantedAuthority**：表示授予主体的权限。这些权限信息在认证成功后，可以从`Authentication` 对象的 `getAuthorities()` 方法获取。

****

**总结关系链**：

`SecurityContextHolder` -> 持有 -> `SecurityContext` -> 持有 -> `Authentication` 对象 -> 包含：

+ `Principal` (身份标识)
+ `Credentials` (凭证，认证后通常为 `null`)
+ `GrantedAuthority` (权限集合)

### 在Controller中获取用户信息
当用户登录成功后，我们在 `IndexController`中尝试获取用户信息，代码如下：

```java
package com.jkweilai.spring.security.demo.controller;

import org.springframework.security.core.Authentication;
import org.springframework.security.core.GrantedAuthority;
import org.springframework.security.core.context.SecurityContext;
import org.springframework.security.core.context.SecurityContextHolder;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.Collection;
import java.util.HashMap;
import java.util.Map;

/*@Controller
public class IndexController {
    @GetMapping("/")
    public String index(){
        return "index";
    }
}*/

@RestController
public class IndexController {

    @GetMapping("/")
    public Map<String, Object> index() {

        // 1. 从SecurityContextHolder中获取当前线程的安全上下文
        SecurityContext context = SecurityContextHolder.getContext();
        // 2. 从安全上下文中获取当前用户的认证信息
        Authentication authentication = context.getAuthentication();
        // 3. 获取当前登录用户的标识（通常是用户名）
        String name = authentication.getName();
        // 4. 获取代表用户身份的主体对象（认证前通常是用户名，认证后是UserDetails等对象）
        Object principal = authentication.getPrincipal();
        // 5. 获取用户的凭证（如密码，认证成功后通常返回null）
        Object credentials = authentication.getCredentials();
        // 6. 获取当前用户被授予的所有权限（角色和权限列表）
        Collection<? extends GrantedAuthority> authorities = authentication.getAuthorities();

        System.out.println(name);
        System.out.println(principal);
        System.out.println(credentials);
        System.out.println(authorities);

        // 封装数据
        Map<String, Object> map = new HashMap<>();
        map.put("code", 0);
        map.put("data", name);

        // 响应JSON
        return map;
    }
}

```



测试如下：[http://localhost:8080/login](http://localhost:8080/login)，先发送这个请求，填写用户名和密码登录。登录成功后，再发送请求：[http://localhost:8080/](http://localhost:8080/)

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1759324314484-abc7070e-9e16-48a4-bfe6-bfcf83792156.png" width="289" title="" crop="0,0,1,1" id="u92726525" class="ne-image" style="font-size: 16px">

后端打印的信息：

```plain
admin
org.springframework.security.core.userdetails.User [Username=admin, Password=[PROTECTED], Enabled=true, AccountNonExpired=true, CredentialsNonExpired=true, AccountNonLocked=true, Granted Authorities=[]]
null
[]
```

## 会话并发处理
一个账号能在多台终端上使用叫做会话并发，如果你希望控制这个会话并发的数量，假设你希望一个账号同一个时间只能在一台设备上使用。

### 编写会话过期策略接口的实现
`Spring Security`提供了会话过期策略接口：`SessionInformationExpiredStrategy`，我们只需要编写这个接口的实现类，实现其中的 `onExpiredSessionDetected`方法，当多个会话并发时，如果当前会话被挤掉，这个回调会自动执行，响应给掉线的前端用户一个提示信息：

```java
package com.jkweilai.spring.security.demo.config;

import com.alibaba.fastjson2.JSON;
import jakarta.servlet.ServletException;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.security.web.session.SessionInformationExpiredEvent;
import org.springframework.security.web.session.SessionInformationExpiredStrategy;

import java.io.IOException;
import java.util.HashMap;
import java.util.Map;

public class MySessionInformationExpiredStrategy implements SessionInformationExpiredStrategy {
    @Override
    public void onExpiredSessionDetected(SessionInformationExpiredEvent event) throws IOException, ServletException {
        // 封装数据
        Map<String, Object> map = new HashMap<>();
        map.put("code", -1);
        map.put("msg", "该账号已从其他设备登录");

        // 转换JSON
        String json = JSON.toJSONString(map);

        // 响应JSON
        HttpServletResponse response = event.getResponse();
        response.setContentType("application/json;charset=UTF-8");
        response.getWriter().print(json);
    }
}

```

### SecurityFilterChain配置
你同样需要告诉 `Spring Security`，这个回调在哪里。

```java
// 配置会话并发管理
http.sessionManagement(session -> {
    // 1 表示一个账号只能在一个设备上使用
    session.maximumSessions(1).expiredSessionStrategy(new MySessionInformationExpiredStrategy());
});
```

  
测试：打开两个浏览器测试。一个先登录上去，另一个也登录上去。然后在第一个浏览器上再访问其他资源。

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1759325039434-95247421-f04c-46de-aa66-e92415460ae3.png" width="454" title="" crop="0,0,1,1" id="ub520acb2" class="ne-image" style="font-size: 16px">

