# JWT
**<font style="color:rgb(15, 17, 21);">JWT 是一个完全独立的技术标准（RFC 7519）</font>**<font style="color:rgb(15, 17, 21);">，它本身并不隶属于 OAuth2 或 Spring Security，但三者经常一起使用。</font>

## Spring Security 的默认会话机制
**Spring Security 默认使用的是 Session 机制。**

**具体解释：**

在现在的 GitHub OAuth2 项目中，Spring Security 的默认工作流程是这样的：

**登录成功后**

+ Spring Security 会将认证信息（包括从 GitHub 获取的用户信息 `OAuth2User`）存储在 **HttpSession** 中
+ 同时在浏览器端设置一个名为 `JSESSIONID` 的 Cookie

**后续请求中**

+ 浏览器自动携带 `JSESSIONID` Cookie
+ Spring Security 根据这个 ID 找到对应的 Session
+ 从 Session 中恢复认证信息，让你能在 Controller 中通过 `@AuthenticationPrincipal` 获取用户信息

**代码证明**

在 Controller 中：

```java
@GetMapping("/")
public String index(Model model, @AuthenticationPrincipal OAuth2User oauth2User) {
    // 这个 oauth2User 就是从 Session 中取出来的
    // 不需要每次请求都去 GitHub 重新获取
    model.addAttribute("userName", oauth2User.getName());
    return "index";
}
```

**Session 有效期**

+ 默认情况下，Session 在用户关闭浏览器后失效
+ 也可以在 `application.yml` 中配置：

```yaml
server:
  servlet:
    session:
      timeout: 1800 # 30分钟（以秒为单位）
```

## 用 JWT 和不用 JWT 的区别
用了JWT，前端可以直接从 JWT 令牌中读取用户信息而不用问后端；没用JWT，前端每次需要用户信息时都必须请求后端接口。

+ **用JWT**：用户基本信息「写在身份证上」，谁都能看，前端自给自足
+ **不用JWT**：用户基本信息「锁在服务器保险柜里」，前端每次都要敲门问

最核心的区别——**信息存储位置和访问方式**不同。



**想象一下，你经常去一个****健身房****。**

**没用 JWT 的时候（传统 Session）：**

你第一次去，前台给你一张**磁卡**（Session ID）。这张卡本身没信息，只是健身房电脑系统里的一个编号。

每次你进健身房，都要**刷卡**（发送请求）。  
前台要**打电话问后台**（查询数据库/Session）：“卡号 888 是谁？他有啥权限？”  
后台查完告诉前台：“是张三，可以进器械区。”  
然后才放你进去。

**缺点**：前台每次都要问后台，很麻烦。如果健身房开了连锁店（多个服务器），信息可能不同步。

****

**用了 JWT 的时候：**

你第一次去，前台给你一张**高级防伪会员卡**（JWT）。

这张卡很神奇，上面用**特殊防伪技术**（签名）写着你的所有信息：

> “姓名：张三，会员等级：金卡，有效期至：2024年底...”（**Payload - 有效信息**）  
这些信息被**特殊编码**过（Base64 编码：只是为了防止网络传输中乱码），但谁都能看懂（信息是明文形式）。
>

现在你进任何一家连锁店，前台只需要：

1. 用专门的**验钞灯**（签名验证算法）照一下卡的**防伪标记**（Signature）。
2. 如果防伪标记是真的，他就**直接相信卡上写的所有信息**，不再打电话问总部。

**优点**：速度快（不用每次查数据库），去哪家店都行（无状态、扩展性好）。



**总结一下 JWT 的核心特点：**

1. **自包含**：信息就写在卡上（令牌里），不用去后台查。
2. **可验证**：通过防伪签名（Signature）确保信息没人篡改。
3. **有期限**：卡上写着有效期，过期就作废。

所以，**JWT 就是一个自带防伪标识、写着用户信息的数字身份证**。验证方只要验证身份证真伪，就可以直接相信上面的信息，省去了每次查询中央数据库的麻烦。

## 什么是 JWT
**<font style="color:rgb(15, 17, 21);">JWT 是 JSON Web Token 的缩写。</font>**

<font style="color:rgb(15, 17, 21);">把它拆开理解就非常简单：</font>

+ **<font style="color:rgb(15, 17, 21);">JSON</font>**<font style="color:rgb(15, 17, 21);">：说明它使用</font><font style="color:rgb(15, 17, 21);"> </font>**<font style="color:rgb(15, 17, 21);">JSON 格式</font>**<font style="color:rgb(15, 17, 21);"> </font><font style="color:rgb(15, 17, 21);">来存储信息。就像你平时写的</font><font style="color:rgb(15, 17, 21);"> </font>`<font style="color:rgb(15, 17, 21);background-color:rgb(235, 238, 242);">{"name": "张三", "age": 25}</font>`<font style="color:rgb(15, 17, 21);"> </font><font style="color:rgb(15, 17, 21);">这种键值对。</font>
+ **<font style="color:rgb(15, 17, 21);">Web</font>**<font style="color:rgb(15, 17, 21);">：说明它是为</font><font style="color:rgb(15, 17, 21);"> </font>**<font style="color:rgb(15, 17, 21);">网络应用</font>**<font style="color:rgb(15, 17, 21);"> </font><font style="color:rgb(15, 17, 21);">设计的，专门用于在网站、API 之间安全地传递信息。</font>
+ **<font style="color:rgb(15, 17, 21);">Token</font>**<font style="color:rgb(15, 17, 21);">：意思是 </font>**<font style="color:rgb(15, 17, 21);">“令牌”</font>**<font style="color:rgb(15, 17, 21);"> 或 </font>**<font style="color:rgb(15, 17, 21);">“凭证”</font>**<font style="color:rgb(15, 17, 21);">。就像开门用的钥匙、进入游乐园的门票。</font>

<font style="color:rgb(15, 17, 21);">如果是前后端分离的系统，那就不能使用 HttpSession 技术了，就需要使用 JWT 了。</font>

## JWT 底层机制
我们回到健身房的例子，但这次我们来看看这张“防伪会员卡”到底是怎么从无到有制作出来的。

### 第一幕：准备材料（签发 JWT）
想象你是一家健身房的老板，要给自己制作一张高级防伪会员卡。

**第一步：写下核心信息（创建 Payload）**  
你拿出一张卡片，写上你的基本信息：

```json
{
  "姓名": "张三",
  "等级": "金卡会员", 
  "发卡时间": "2024-01-01",
  "有效期至": "2024-12-31"
}
```

这就是 **Payload（有效载荷）**，即卡里要存储的核心信息。

**第二步：写明防伪技术（创建 Header）**  
为了防止别人伪造，你决定采用一种复杂的防伪技术。你在卡片角落注明：

```json
{
  "防伪技术": "健身房独家秘方V1",
  "卡片类型": "JWT会员卡"
}
```

这就是 **Header（头部）**，说明了使用的签名算法(**HS256 算法**)和类型。

### 第二幕：制作防伪标识（生成 Signature）
这是最关键的一步，决定了卡片的真伪。

**第三步：混合编码（Base64Url 编码）**

1. 你把 **Header** 这张小纸条的内容，用一种**通用翻译器**（Base64Url 编码）转成一串看似乱码的文字：`aaaa`
2. 你把 **Payload** 这张卡片的内容，也用同样的**通用翻译器**转成另一串乱码：`bbbb`
3. 你把这两串乱码用点号连接起来：`aaaa.bbbb`

**第四步：核心加密（生成签名）**  
现在到了最核心的步骤：

+ 你有一个只有健身房经理才知道的 **“绝密配方”**（Secret Key）。
+ 你把这个 **“绝密配方”** 和刚才那串 `aaaa.bbbb` 放进一个**特殊的机器**（签名算法，如 HS256）里进行加工。
+ 机器吐出一串全新的、独一无二的**防伪码**（Signature）：`cccc`

**最终成品：**  
你把所有部分用点号连接起来，最终得到了一张完整的、带有防伪标识的会员卡：  
`aaaa.bbbb.cccc`

这就是一个完整的 **JWT**。

### 第三幕：验卡过程（验证 JWT）
现在，你拿着这张卡 `aaaa.bbbb.cccc` 去健身房前台。

前台小哥的验卡流程如下：

**第一步：拆解**  
他把卡片拆成三部分：`aaaa`、`bbbb` 和 `cccc`。

**第二步：重现防伪码**

1. 前台小哥也有一台同样的**特殊机器**（验证算法）。
2. 他知道健身房通用的 **“绝密配方”**（Secret Key）。
3. 他把 `aaaa` 和 `bbbb` 重新组合成 `aaaa.bbbb`，然后和 **“绝密配方”** 一起放进机器。
4. 机器也吐出一串防伪码，我们称之为 `cccc2`。

**第三步：比对**  
现在，他开始比对他自己算出来的 `cccc2` 和卡片上印着的 `cccc`。

+ **情况A（验卡通过）**：如果 `cccc2` 和 `cccc` **完全一样**。
    - 结论：“卡是真的！信息有效！”
    - 前台小哥信任卡片上的所有信息，直接为你服务。
+ **情况B（验卡失败）**：如果 `cccc2` 和 `cccc` **对不上**。
    - 结论：“卡是假的！信息被篡改过！”
    - 立即拒绝服务。

### 底层机制的核心要点总结
1. **三部分组成**：`Header.Payload.Signature`，用点连接。
2. **信息透明**：Header 和 Payload 只是做了 Base64 编码，**谁都能解码看清内容**，所以不能存放密码等敏感信息。
3. **安全全靠签名**：整个 JWT 的安全性和可信度，100% 依赖于 **Signature**。Signature 是由 Header、Payload 和 Secret Key 共同通过加密算法计算得出的。
4. **验证原理**：验证方用同样的算法和 Secret Key，对收到的 Header 和 Payload 重新计算一次签名，然后与 JWT 自带的 Signature 进行比对。一致则可信。
5. **密钥是关键**：那个 **Secret Key** 至关重要，如果泄露，任何人都可以伪造合法的 JWT。它必须被严格保护在服务器端。

简单说，JWT 的底层就是一个 **“信息 + 防伪码”** 的结构，它的安全性不在于隐藏信息，而在于通过密码学手段确保信息**无法被篡改**。



<font style="color:rgb(15, 17, 21);">站在 Web 前端角度来说，首次登录成功后从后端接收到 JWT，可以将其存储在浏览器本地（如 LocalStorage 或 Cookie）。之后需要获取用户基本信息（如用户名、头像）时，前端</font>**<font style="color:rgb(15, 17, 21);">无需再请求后端接口</font>**<font style="color:rgb(15, 17, 21);">，只需直接解析 JWT 的 Payload 部分即可读取这些信息。</font>

<font style="color:rgb(15, 17, 21);"></font>

<font style="color:rgb(15, 17, 21);">不过要注意：JWT 虽然自带有效期，但</font>**<font style="color:rgb(15, 17, 21);">无法在有效期内主动失效</font>**<font style="color:rgb(15, 17, 21);">。也就是说，就算用户已经主动退出系统了，JWT 只要还没有过期，该 Token 还是有效的。这是 JWT “无状态”特性带来的权衡，在实际应用中通常需要借助黑名单、设置较短有效期等策略来弥补这一点。</font>



## OAuth2 GitHub登录项目集成JWT
### <font style="color:rgb(15, 17, 21);">添加依赖</font>
<font style="color:rgb(15, 17, 21);">首先在 </font>`<font style="color:rgb(15, 17, 21);">pom.xml</font>`<font style="color:rgb(15, 17, 21);"> 中添加JWT相关依赖：JJWT（</font>**<font style="color:rgb(15, 17, 21);">Java JWT 的库</font>**<font style="color:rgb(15, 17, 21);">）</font>

```xml
<!--提供JWT创建和解析的接口和抽象类，是开发时的主要编程接口。-->
<dependency>
    <groupId>io.jsonwebtoken</groupId>
    <artifactId>jjwt-api</artifactId>
    <version>0.13.0</version>
</dependency>
<!--提供JJWT接口的具体实现，在运行时负责实际的JWT令牌处理逻辑。-->
<dependency>
    <groupId>io.jsonwebtoken</groupId>
    <artifactId>jjwt-impl</artifactId>
    <version>0.13.0</version>
    <scope>runtime</scope>
</dependency>
<!--使用Jackson库来处理JWT的JSON序列化和反序列化操作。-->
<dependency>
    <groupId>io.jsonwebtoken</groupId>
    <artifactId>jjwt-jackson</artifactId>
    <version>0.13.0</version>
    <scope>runtime</scope>
</dependency>
```

### <font style="color:rgb(15, 17, 21);">配置JWT属性</font>
<font style="color:rgb(15, 17, 21);">在 </font>`<font style="color:rgb(15, 17, 21);">application.yml</font>`<font style="color:rgb(15, 17, 21);"> 中添加JWT配置：</font>

```yaml
app:
  jwt:
    secret: "oauth2-login-demo-jwt-secret-2024@Secure!Key#256Bits$MinLengthRequired" # 一定是强秘钥
    expiration: 86400000 # 24小时
    issuer: "oauth2-login-demo" # 标明这个 JWT 是由哪个应用颁发的，在验证 token 时可以检查发行者是否匹配
```

### <font style="color:rgb(15, 17, 21);">创建JWT工具类</font>
```java
package com.jkweilai.oauth2.logindemo.config.jwt;

import io.jsonwebtoken.Claims;
import io.jsonwebtoken.JwtException;
import io.jsonwebtoken.Jwts;
import io.jsonwebtoken.SignatureAlgorithm;
import io.jsonwebtoken.security.Keys;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.security.core.Authentication;
import org.springframework.security.core.GrantedAuthority;
import org.springframework.stereotype.Component;

import javax.crypto.SecretKey;
import java.util.ArrayList;
import java.util.Date;
import java.util.List;
import java.util.stream.Collectors;

@Component
public class JwtTokenProvider {

    @Value("${app.jwt.secret}")
    private String jwtSecret;

    @Value("${app.jwt.expiration}")
    private long jwtExpiration;

    @Value("${app.jwt.issuer}")
    private String jwtIssuer;

    /**
     * 根据配置的密钥字符串生成JWT签名所需的SecretKey对象。
     *
     * @return
     */
    private SecretKey getSigningKey() {
        return Keys.hmacShaKeyFor(jwtSecret.getBytes());
    }

    /**
     * 使用用户认证信息生成包含用户名、角色和过期时间的JWT令牌。
     *
     * @param authentication
     * @return
     */
    public String generateToken(Authentication authentication) {
        String username = authentication.getName();
        List<String> roles = authentication.getAuthorities().stream().map(GrantedAuthority::getAuthority).collect(Collectors.toList());
        
        // 每个角色名前添加 ROLE_ 前缀。
        List<String> normalizedRoles = normalizeRoles(roles);

        // 系统当前时间
        Date now = new Date();
        // 过期时间
        Date expiryDate = new Date(now.getTime() + jwtExpiration);

        return Jwts.builder()
                .setSubject(username)           // 设置JWT主题，存储用户名作为用户唯一标识
                .setIssuer(jwtIssuer)            // 设置JWT签发者，标识token来自哪个应用
                .setIssuedAt(now)                // 设置JWT签发时间，用于计算token年龄
                .setExpiration(expiryDate)       // 设置JWT过期时间，到达此时间后token失效
                .claim("roles", normalizedRoles) // 添加自定义声明，存储用户标准化后的角色列表
                .signWith(getSigningKey(), SignatureAlgorithm.HS256) // 使用 HS256算法和密钥 对JWT进行签名，防止篡改
                .compact();                       // 将以上所有设置组装成最终的JWT字符串
    }

    /**
     * 标准化角色列表，确保包含 ROLE_USER 并正确处理各种角色格式
     * @PreAuthorize("hasRole('ADMIN')")  在检查的时候会判断用户是否有ROLE_ADMIN角色
     * 因此，下面的方法是给所有的角色统一添加 ROLE_ 前缀。
     */
    private List<String> normalizeRoles(List<String> roles) {
        List<String> normalizedRoles = new ArrayList<>();

        // 这不是必须的，是业务需求，不是技术必须：让所有登录用户都拥有一个基础角色（ROLE_USER），确保每个人在应用内都有最基本的权限
        normalizedRoles.add("ROLE_USER");

        for (String role : roles) {
            if (role.startsWith("SCOPE_")) {
                // SCOPE_ 开头的是 GitHub 的 OAuth2 授权范围，和我应用自身的业务角色无关，不需要混入我的角色体系
                // SCOPE_ 开头是 Spring Security 在处理 OAuth2 登录时，自动将 GitHub 返回的授权范围（scope）加上前缀后转换成的 GrantedAuthority
                continue;
            } else if (!role.startsWith("ROLE_")) {
                normalizedRoles.add("ROLE_" + role);
            } else {
                normalizedRoles.add(role);
            }
        }

        return normalizedRoles;
    }

    /**
     * 从JWT令牌中解析并提取用户名主题(subject)。
     *
     * @param token
     * @return
     */
    public String getUsernameFromToken(String token) {
        Claims claims = Jwts.parser().setSigningKey(getSigningKey()).build().parseClaimsJws(token).getBody();
        return claims.getSubject();
    }

    /**
     * 验证JWT令牌的签名有效性和格式正确性。
     *
     * @param token
     * @return
     */
    public boolean validateToken(String token) {
        try {
            Jwts.parser().setSigningKey(getSigningKey()).build().parseClaimsJws(token);
            return true;
        } catch (JwtException | IllegalArgumentException e) {
            return false;
        }
    }

    /**
     * 从JWT令牌中提取用户角色权限列表。
     *
     * @param token
     * @return
     */
    public List<String> getRolesFromToken(String token) {
        Claims claims = Jwts.parser().setSigningKey(getSigningKey()).build().parseClaimsJws(token).getBody();

        return claims.get("roles", List.class);
    }
}
```

### <font style="color:rgb(15, 17, 21);">创建JWT认证过滤器</font>
**<font style="color:rgb(15, 17, 21);">表单登录（Form Login）的认证过滤器大家都知道：</font>**`**<font style="color:rgb(15, 17, 21);background-color:rgb(235, 238, 242);">UsernamePasswordAuthenticationFilter</font>**`

<font style="color:rgb(15, 17, 21);background-color:rgb(235, 238, 242);"></font>

<font style="color:rgb(15, 17, 21);">如果使用 JWT，Spring Security </font>**<font style="color:rgb(15, 17, 21);">没有内置的默认认证过滤器</font>**<font style="color:rgb(15, 17, 21);">，需要</font>**<font style="color:rgb(15, 17, 21);">自定义过滤器</font>**<font style="color:rgb(15, 17, 21);">来完成 JWT 的认证工作</font>

<font style="color:rgb(15, 17, 21);"></font>

<font style="color:rgb(15, 17, 21);">自定义过滤器，继承 </font>`<font style="color:rgb(15, 17, 21);background-color:rgb(235, 238, 242);">OncePerRequestFilter</font>`<font style="color:rgb(15, 17, 21);">，在过滤器中：</font>

1. <font style="color:rgb(15, 17, 21);">从请求头中提取 JWT（一般是</font><font style="color:rgb(15, 17, 21);"> </font>`<font style="color:rgb(15, 17, 21);background-color:rgb(235, 238, 242);">Authorization: Bearer <token></font>`<font style="color:rgb(15, 17, 21);">）</font>
2. <font style="color:rgb(15, 17, 21);">验证 JWT 的签名和有效性</font>
3. <font style="color:rgb(15, 17, 21);">从 JWT 中解析用户信息（用户名、角色等）</font>
4. <font style="color:rgb(15, 17, 21);">创建 </font>`<font style="color:rgb(15, 17, 21);background-color:rgb(235, 238, 242);">UsernamePasswordAuthenticationToken</font>`<font style="color:rgb(15, 17, 21);"> 并设置到 </font>`<font style="color:rgb(15, 17, 21);background-color:rgb(235, 238, 242);">SecurityContextHolder</font>`<font style="color:rgb(15, 17, 21);"> 中</font>

```java
package com.jkweilai.oauth2.logindemo.config.jwt;

import jakarta.servlet.FilterChain;
import jakarta.servlet.ServletException;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.security.authentication.UsernamePasswordAuthenticationToken;
import org.springframework.security.core.authority.SimpleGrantedAuthority;
import org.springframework.security.core.context.SecurityContextHolder;
import org.springframework.web.filter.OncePerRequestFilter;

import java.io.IOException;
import java.util.List;
import java.util.stream.Collectors;

// OncePerRequestFilter 的核心作用是：在一个请求的完整生命周期中，不管它经过了多少次内部跳转，这个过滤器都只执行一次。
// 他是springmvc中提供的，不是security中提供的。
public class JwtAuthenticationFilter extends OncePerRequestFilter {

    private final JwtTokenProvider jwtTokenProvider;

    // 构造函数注入JWT令牌提供者用于后续的令牌验证和解析
    public JwtAuthenticationFilter(JwtTokenProvider jwtTokenProvider) {
        this.jwtTokenProvider = jwtTokenProvider;
    }

    // 拦截每个HTTP请求，验证JWT令牌并设置用户认证信息到安全上下文。
    @Override
    protected void doFilterInternal(HttpServletRequest request, HttpServletResponse response, FilterChain filterChain) throws ServletException, IOException {

        String token = getTokenFromRequest(request);

        if (token != null && jwtTokenProvider.validateToken(token)) {
            String username = jwtTokenProvider.getUsernameFromToken(token);
            List<String> roles = jwtTokenProvider.getRolesFromToken(token);

            List<SimpleGrantedAuthority> authorities = roles.stream().map(SimpleGrantedAuthority::new).collect(Collectors.toList());

            UsernamePasswordAuthenticationToken authentication = new UsernamePasswordAuthenticationToken(username, null, authorities);

            SecurityContextHolder.getContext().setAuthentication(authentication);
        }

        filterChain.doFilter(request, response);
    }

    // 从请求的Authorization头部提取Bearer令牌字符串。
    private String getTokenFromRequest(HttpServletRequest request) {
        String bearerToken = request.getHeader("Authorization");
        if (bearerToken != null && bearerToken.startsWith("Bearer ")) {
            return bearerToken.substring(7);
        }
        return null;
    }
}
```

### <font style="color:rgb(15, 17, 21);">修改Security配置</font>
<font style="color:rgb(15, 17, 21);">更新你的Security配置类：</font>

```java
package com.jkweilai.oauth2.logindemo.config;

import com.jkweilai.oauth2.logindemo.config.jwt.JwtAuthenticationFilter;
import com.jkweilai.oauth2.logindemo.config.jwt.JwtTokenProvider;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.security.config.annotation.web.builders.HttpSecurity;
import org.springframework.security.config.annotation.web.configuration.EnableWebSecurity;
import org.springframework.security.config.http.SessionCreationPolicy;
import org.springframework.security.web.SecurityFilterChain;

@Configuration
@EnableWebSecurity // 启用Spring Security的Web安全支持。
public class SecurityConfig {

    private final JwtTokenProvider jwtTokenProvider;

    public SecurityConfig(JwtTokenProvider jwtTokenProvider) {
        this.jwtTokenProvider = jwtTokenProvider;
    }

    // 定义HTTP安全过滤链的主配置方法。
    @Bean
    public SecurityFilterChain filterChain(HttpSecurity http) throws Exception {
        http
                // 配置CORS跨域支持使用默认设置。
                .cors(cors -> cors.configure(http))
                // 禁用CSRF防护因为使用无状态的JWT认证。
                .csrf(csrf -> csrf.disable())
                // 设置会话管理为无状态，不创建服务器端Session。
                .sessionManagement(session -> session.sessionCreationPolicy(SessionCreationPolicy.STATELESS))
                // 配置请求授权规则。
                .authorizeHttpRequests(authz -> authz
                        // 允许这些路径无需认证即可访问。实际上当引入oauth2的client依赖后，/login/** 和 /oauth2/** 会被默认放行。
                        .requestMatchers("/", "/login", "/oauth2/**", "/auth/**", "/api/public")
                        .permitAll()
                        .requestMatchers("/api/protected")
                        .hasRole("USER")
                        .anyRequest()
                        .authenticated() // 其他所有请求都需要认证后才能访问。
                )
                //  配置OAuth2登录功能。
                .oauth2Login(oauth2 -> oauth2
                        // 设置OAuth2登录成功后的自定义处理器。
                        .successHandler(oauth2AuthenticationSuccessHandler()))
                //在OAuth2登录过滤器前添加JWT认证过滤器。
                // 如果请求已经携带有效 JWT 时，直接认证通过，不再走 OAuth2 登录流程
                .addFilterBefore(new JwtAuthenticationFilter(jwtTokenProvider), org.springframework.security.oauth2.client.web.OAuth2LoginAuthenticationFilter.class);

        return http.build();
    }

    @Bean
    public OAuth2AuthenticationSuccessHandler oauth2AuthenticationSuccessHandler() {
        return new OAuth2AuthenticationSuccessHandler(jwtTokenProvider);
    }
}
```

### <font style="color:rgb(15, 17, 21);">创建OAuth2成功处理器</font>
**<font style="color:rgb(15, 17, 21);">在用户通过 GitHub 认证成功后，生成 JWT 并直接以 JSON 格式返回给前端，而不是重定向到页面。</font>**

**<font style="color:rgb(15, 17, 21);">这样前端系统收到后，可以将 token 存储到 storage 中。</font>**

```java
package com.jkweilai.oauth2.logindemo.config;

import com.jkweilai.oauth2.logindemo.config.jwt.JwtTokenProvider;
import jakarta.servlet.ServletException;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.security.core.Authentication;
import org.springframework.security.oauth2.core.user.OAuth2User;
import org.springframework.security.web.authentication.SimpleUrlAuthenticationSuccessHandler;
import org.springframework.stereotype.Component;

import java.io.IOException;

@Component
public class OAuth2AuthenticationSuccessHandler extends SimpleUrlAuthenticationSuccessHandler {

    private final JwtTokenProvider jwtTokenProvider;

    public OAuth2AuthenticationSuccessHandler(JwtTokenProvider jwtTokenProvider) {
        this.jwtTokenProvider = jwtTokenProvider;
    }

    @Override
    public void onAuthenticationSuccess(HttpServletRequest request, HttpServletResponse response, Authentication authentication) throws IOException, ServletException {

        OAuth2User oAuth2User = (OAuth2User) authentication.getPrincipal();

        // 生成JWT token
        String jwtToken = jwtTokenProvider.generateToken(authentication);

        String username = getUsernameFromOAuth2User(oAuth2User);

        // 将token返回给前端
        response.setContentType("application/json");
        response.setCharacterEncoding("UTF-8");

        String jsonResponse = String.format("{\"token\": \"%s\", \"username\": \"%s\"}", jwtToken, username);

        response.getWriter().write(jsonResponse);
        response.getWriter().flush();
    }

    private String getUsernameFromOAuth2User(OAuth2User oAuth2User) {
        if (oAuth2User.getAttribute("login") != null) {
            return oAuth2User.getAttribute("login");
        }
        return oAuth2User.getName();
    }
}
```

### <font style="color:rgb(15, 17, 21);">创建测试控制器</font>
```java
package com.jkweilai.oauth2.logindemo.controller;

import org.springframework.http.ResponseEntity;
import org.springframework.security.access.prepost.PreAuthorize;
import org.springframework.security.core.Authentication;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.HashMap;
import java.util.Map;

@RestController
@RequestMapping("/api")
public class TestController {

    @GetMapping("/public")
    public ResponseEntity<?> publicEndpoint() {
        Map<String, String> response = new HashMap<>();
        response.put("message", "这是一个公开的端点");
        return ResponseEntity.ok(response);
    }

    @GetMapping("/protected")
    @PreAuthorize("hasRole('USER')")
    public ResponseEntity<?> protectedEndpoint(Authentication authentication) {
        Map<String, Object> response = new HashMap<>();
        response.put("message", "这是一个受保护的端点");
        response.put("username", authentication.getName());
        response.put("authorities", authentication.getAuthorities());
        return ResponseEntity.ok(response);
    }
}

```

### 修改 IndexController
```java
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;

@Controller
public class IndexController {

    @GetMapping("/")
    public String index() {
        return "index";
    }
}
```

### 修改 index.html
```html
<!DOCTYPE html>
<html>
<head>
    <title>Spring Security - OAuth 2 Login</title>
    <meta charset="utf-8"/>
</head>
<body>
<h1>OAuth 2 Login with Spring Security</h1>

<div>
    <p>请使用以下方式登录获取 JWT Token：</p>
    <a href="/oauth2/authorization/github">使用GitHub登录</a>
</div>

<div>
    <p>登录成功后，请在响应中获取 JWT token，然后使用以下命令测试API：</p>
    <pre>
# 测试公开端点
curl http://localhost:8080/api/public

# 测试受保护端点（需要JWT token）
curl -H "Authorization: Bearer YOUR_TOKEN" http://localhost:8080/api/protected
    </pre>
</div>

</body>
</html>
```

### <font style="color:rgb(15, 17, 21);">测试步骤</font>
**<font style="color:rgb(15, 17, 21);">步骤1: 测试GitHub登录</font>**

<font style="color:rgb(15, 17, 21);">访问你的应用，使用GitHub登录，成功后应该返回JWT token。</font>

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1759556680293-b2f7bb94-7214-47ec-bee9-573705ddd2cf.png" width="607.4285714285714" title="" crop="0,0,1,1" id="u3a316e80" class="ne-image" style="font-size: 16px">

<font style="color:rgb(15, 17, 21);"></font>

**<font style="color:rgb(15, 17, 21);">步骤2: 访问公开的端点</font>**

```bash
curl http://localhost:8080/api/public
```

**<font style="color:rgb(15, 17, 21);">步骤 3: 使用JWT访问受保护端点</font>**

```bash
# 使用返回的token访问受保护端点
curl -H "Authorization: Bearer YOUR_JWT_TOKEN" http://localhost:8080/api/protected
```

### <font style="color:rgb(15, 17, 21);">完整的工作流程</font>
1. <font style="color:rgb(15, 17, 21);">用户访问应用，点击GitHub登录</font>
2. <font style="color:rgb(15, 17, 21);">GitHub认证成功后，调用成功处理器</font>
3. <font style="color:rgb(15, 17, 21);">成功处理器生成JWT token并返回给前端</font>
4. <font style="color:rgb(15, 17, 21);">前端在后续请求中在Header中携带JWT token</font>
5. <font style="color:rgb(15, 17, 21);">JWT过滤器验证token并设置认证信息</font>
6. <font style="color:rgb(15, 17, 21);">用户访问受保护的API端点</font>

### <font style="color:rgb(15, 17, 21);">注意事项</font>
1. **密钥安全**<font style="color:rgb(15, 17, 21);">: 生产环境请使用其他无规律的密钥，并将密钥配置到环境变量中，而不是放到 </font>`<font style="color:rgb(15, 17, 21);">application.yml</font>`<font style="color:rgb(15, 17, 21);">中。</font>
2. **Token存储**<font style="color:rgb(15, 17, 21);">: 前端需要安全地存储JWT token（建议使用httpOnly cookie）</font>
3. **过期时间**<font style="color:rgb(15, 17, 21);">: 根据安全需求调整token过期时间</font>
4. **刷新Token**<font style="color:rgb(15, 17, 21);">: </font>**<font style="color:rgb(15, 17, 21);">JWT 的 Refresh Token 实现原理：在 access token 过期后通过专用接口申请新的 access token，实现用户无感知的自动续期。</font>**

<font style="color:rgb(15, 17, 21);">这样你就成功在Spring Boot OAuth2 GitHub登录项目中集成了JWT功能！</font>

