# Spring Security自定义配置


**官方文档：**[**https://docs.spring.io/spring-security/reference/servlet/configuration/java.html**](https://docs.spring.io/spring-security/reference/servlet/configuration/java.html)

## 基于内存的用户认证
### 创建用户信息查询器
要完成**用户认证**，需要为 IoC 容器注入一个`**<font style="color:rgb(15, 17, 21);background-color:rgb(235, 238, 242);">UserDetailsService</font>**`**<font style="color:rgb(15, 17, 21);"> 类型的对象。（内存认证和数据库认证都需要这个接口）</font>**

`**<font style="color:rgb(15, 17, 21);background-color:rgb(235, 238, 242);">UserDetailsService</font>**`**<font style="color:rgb(15, 17, 21);"> 是 Spring Security 的"用户信息查询器"</font>**

`**InMemoryUserDetailsManager**`** **是 `UserDetailsService` 的一个实现，用来管理**基于内存**的用户信息。



**编写以下配置：**

```java
package com.jkweilai.spring.security.demo.config;

import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.security.config.annotation.web.configuration.EnableWebSecurity;
import org.springframework.security.core.userdetails.User;
import org.springframework.security.core.userdetails.UserDetailsService;
import org.springframework.security.provisioning.InMemoryUserDetailsManager;

@Configuration
//@EnableWebSecurity  // Spring Security的开关。（不添加这个注解也可以，因为SpringBoot进行了自动配置，根据依赖自动启用Spring Security）
public class WebSecurityConfig {

    @Bean
    public UserDetailsService userDetailsService(){
        InMemoryUserDetailsManager manager = new InMemoryUserDetailsManager();
        manager.createUser( // 该行添加断点可查看user对象信息
                User
                        .withDefaultPasswordEncoder() // 使用默认的密码编码器（使用默认的bcrypt进行加密）
                        .username("user") // 自定义用户名
                        .password("123456") // 自定义密码
                        .roles("USER") // 自定义角色
                        .build()
        );
        return manager;
    }
}
```

测试：使用用户名 `user`，密码 `123456`进行登录。

**一旦使用了自定义配置，那么之前在 **`**application.properties**`**文件中配置的用户名密码就没用了。**

### 基于内存的用户认证流程
**一、启动阶段（准备用户数据）**

1. **加载配置**：Spring 启动时，看到 `@EnableWebSecurity` 注解，启用安全框架。
2. **创建用户服务**：执行 `userDetailsService()` 方法，创建一个内存版的用户管理器（`InMemoryUserDetailsManager`）。
3. **存储用户**：使用 `User.build()` 创建用户对象（用户名、**加密的密码**、角色），并将其存入内存管理器的内部 Map 中（key 是用户名，value 是 UserDetails 对象）。

**结果**：框架现在知道有一个合法的用户 `user`，密码是 `123456`。

**二、认证阶段（验证用户登录）**

1. **拦截请求**：当访问受保护页面时，过滤器链发现用户未登录，将其重定向到登录页。
2. **提交凭证**：用户在登录页输入用户名和密码，点击登录。
3. **核心验证**：
    - **查用户**：认证管理器调用 `InMemoryUserDetailsManager.loadUserByUsername("user")`，根据用户名 `user` 从内存Map里查找对应的用户信息（`UserDetails`）。
    - **比密码**：认证器将用户提交的明文密码（`123456`）进行**编码**，然后与查出来的用户信息中存储的**已编码密码**进行比对。
4. **成功/失败**：
    - **成功**：密码一致，认证通过。用户信息被存入本次会话的安全上下文中（SecurityContext），然后跳转到最初想访问的页面。
    - **失败**：密码不一致，返回登录错误页。

**三、核心总结**

+ **启动时**：把定义好的用户信息（密码已编码）加载到内存中的一个“字典”里。
+ **登录时**：用你输入的用户名去“字典”里查找，再比对密码的编码是否一致。

**四、****<font style="color:#DF2A3F;">了解一下核心代码</font>**

用户名密码认证过滤器`UsernamePasswordAuthenticationFilter`中有一个方法 `attemptAuthentication`，代码如下：**获取用户提交的用户名和密码信息，并进入认证流程**

```java
@Override
public Authentication attemptAuthentication(HttpServletRequest request, HttpServletResponse response)
        throws AuthenticationException {
    // 检查请求方法：如果配置为只允许POST请求（默认true），且当前请求不是POST，则抛出异常
    if (this.postOnly && !request.getMethod().equals("POST")) {
        throw new AuthenticationServiceException("Authentication method not supported: " + request.getMethod());
    }
    // 从请求中获取用户名参数（默认从名为"username"的参数获取）
    String username = obtainUsername(request);
    // 处理用户名：如果不为null则去除首尾空格，如果为null则设为空字符串
    username = (username != null) ? username.trim() : "";
    // 从请求中获取密码参数（默认从名为"password"的参数获取）
    String password = obtainPassword(request);
    // 处理密码：如果不为null则保持原样，如果为null则设为空字符串
    password = (password != null) ? password : "";
    // 创建一个未认证的认证令牌对象，包含用户名和密码凭证
    UsernamePasswordAuthenticationToken authRequest = UsernamePasswordAuthenticationToken.unauthenticated(username,
            password);
    // 设置详细信息（details），通常包括远程IP地址、会话ID等请求相关信息
    setDetails(request, authRequest);
    // 将认证令牌委托给AuthenticationManager进行实际的认证处理，并返回认证结果
    return this.getAuthenticationManager().authenticate(authRequest);
}
```

`InMemoryUserDetailsManager`中的 `loadUserByUsername`方法，代码如下：**根据用户名找到内存中存储的用户。**

```java
@Override
public UserDetails loadUserByUsername(String username) throws UsernameNotFoundException {
    // 1. 根据用户名（转换为小写）从内存中的用户Map里查找对应的UserDetails对象
    UserDetails user = this.users.get(username.toLowerCase(Locale.ROOT));
    // 2. 如果找不到用户，抛出异常（这是认证失败的最常见原因）
    if (user == null) {
        throw new UsernameNotFoundException("user '" + username + "' not found");
    }
    // 3. 检查找到的用户对象是否实现了CredentialsContainer接口，如果已经实现了该接口，直接返回原用户对象
    // 如果 UserDetails 对象实现了 CredentialsContainer 接口，就表示它支持在认证完成后主动“擦除”其内部的敏感凭据（主要是密码）
    if (user instanceof CredentialsContainer) {
        return user;
    }
    // 4.如果不支持可擦除，就通过 new User()来创建一个可擦除敏感信息的 User对象。
    return new User(user.getUsername(), user.getPassword(), user.isEnabled(), user.isAccountNonExpired(),
            user.isCredentialsNonExpired(), user.isAccountNonLocked(), user.getAuthorities());
}
```

`DaoAuthenticationProvider`中的 `additionalAuthenticationChecks`方法，代码如下：**拿着内存中的密码和用户提交的密码对比，如果密码一致，认证成功**

```java
protected void additionalAuthenticationChecks(UserDetails userDetails,
        UsernamePasswordAuthenticationToken authentication) throws AuthenticationException {
    if (authentication.getCredentials() == null) {
        this.logger.debug("Failed to authenticate since no credentials provided");
        throw new BadCredentialsException(this.messages
            .getMessage("AbstractUserDetailsAuthenticationProvider.badCredentials", "Bad credentials"));
    }
    String presentedPassword = authentication.getCredentials().toString();
    if (!this.passwordEncoder.get().matches(presentedPassword, userDetails.getPassword())) {
        this.logger.debug("Failed to authenticate since password does not match stored value");
        throw new BadCredentialsException(this.messages
            .getMessage("AbstractUserDetailsAuthenticationProvider.badCredentials", "Bad credentials"));
    }
}
```

## 为数据库的用户认证准备环境
### 准备表和数据
```sql
-- 创建数据库
CREATE DATABASE `spring-security`;
USE `spring-security`;

-- 创建用户表
CREATE TABLE `user`(
    `id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `username` VARCHAR(50) DEFAULT NULL ,
    `password` VARCHAR(500) DEFAULT NULL,
    `enabled` BOOLEAN NOT NULL
);
-- 唯一索引
CREATE UNIQUE INDEX `user_username_unique_index` ON `user`(`username`); 

-- 插入用户数据(密码是 password )
INSERT INTO `user` (`username`, `password`, `enabled`) VALUES
('admin', '{bcrypt}$2a$10$.GyF8EJtw4xeX/MrYTp6xOA2Sz1gC.jj7Hv7v5o8j/B4.rvtlwvKW', TRUE),
('jack', '{bcrypt}$2a$10$bsuU4Bxx9ks3jFmp5GKymOvZKGeXsgGJR.acmIqELyVRN3VjLQkIq', TRUE),
('lucy', '{bcrypt}$2a$10$UUpDXTOLhFUEBCAcuHKQjOnPWKcCt4n893aMDInjVZveR1xWlsO9G', TRUE);
```

### 引入依赖
```xml
<dependency>
    <groupId>mysql</groupId>
    <artifactId>mysql-connector-java</artifactId>
    <version>8.0.24</version>
    <scope>runtime</scope>
</dependency>
<dependency>
    <groupId>org.projectlombok</groupId>
    <artifactId>lombok</artifactId>
    <scope>annotationProcessor</scope>
</dependency>
<dependency>
    <groupId>com.baomidou</groupId>
    <artifactId>mybatis-plus-boot-starter</artifactId>
    <version>3.5.14</version>
    <exclusions>
        <exclusion>
            <groupId>org.mybatis</groupId>
            <artifactId>mybatis-spring</artifactId>
        </exclusion>
    </exclusions>
</dependency>
<dependency>
    <groupId>org.mybatis</groupId>
    <artifactId>mybatis-spring</artifactId>
    <version>3.0.5</version>
</dependency>
```

### 配置数据源
```properties
#MySQL数据源
spring.datasource.driver-class-name=com.mysql.cj.jdbc.Driver
spring.datasource.url=jdbc:mysql://localhost:3306/spring-security
spring.datasource.username=root
spring.datasource.password=123456

#SQL日志
mybatis-plus.configuration.log-impl=org.apache.ibatis.logging.stdout.StdOutImpl
```

### 编写 pojo 类
```java
package com.jkweilai.spring.security.demo.pojo;

import com.baomidou.mybatisplus.annotation.IdType;
import com.baomidou.mybatisplus.annotation.TableId;
import lombok.Data;

@Data
public class User {
    @TableId(value = "id", type = IdType.AUTO)
    private Integer id;
    private String username;
    private String password;
    private Boolean enabled;
}

```

### 编写 Mapper 接口
```java
package com.jkweilai.spring.security.demo.mapper;

import com.baomidou.mybatisplus.core.mapper.BaseMapper;
import com.jkweilai.spring.security.demo.pojo.User;
import org.apache.ibatis.annotations.Mapper;

@Mapper
public interface UserMapper extends BaseMapper<User> {
}

```

### 编写 Mapper XML 文件
`resources/mapper/UserMapper.xml`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE mapper PUBLIC "-//mybatis.org//DTD Mapper 3.0//EN" 
        "http://mybatis.org/dtd/mybatis-3-mapper.dtd">

<mapper namespace="com.jkweilai.spring.security.demo.mapper.UserMapper">
</mapper>
```

### 编写 Service 接口和实现类
接口

```java
package com.jkweilai.spring.security.demo.service;

import com.baomidou.mybatisplus.extension.service.IService;
import com.jkweilai.spring.security.demo.pojo.User;

public interface UserService extends IService<User> {
}
```

实现类

```java
package com.jkweilai.spring.security.demo.service.impl;

import com.baomidou.mybatisplus.extension.service.impl.ServiceImpl;
import com.jkweilai.spring.security.demo.mapper.UserMapper;
import com.jkweilai.spring.security.demo.pojo.User;
import com.jkweilai.spring.security.demo.service.UserService;
import org.springframework.stereotype.Service;

@Service
public class UserServiceImpl extends ServiceImpl<UserMapper, User> implements UserService {
}

```

### 编写 Controller
```java
package com.jkweilai.spring.security.demo.controller;

import com.jkweilai.spring.security.demo.pojo.User;
import com.jkweilai.spring.security.demo.service.UserService;
import lombok.RequiredArgsConstructor;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;

@RestController
@RequiredArgsConstructor
@RequestMapping("/user")
public class UserController {

    private final UserService userService;

    @GetMapping("/list")
    public List<User> listUser(){
        return userService.list();
    }
}

```



**测试：**[**http://localhost:8080/user/list**](http://localhost:8080/user/list)

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1759059041371-2d6a2bb6-28f6-42d3-8b83-a8f24539c86b.png" width="714.6666666666666" title="" crop="0,0,1,1" id="u6425e06d" class="ne-image" style="font-size: 16px">

## 基于数据库的用户认证
### 基于数据库的用户认证流程
编写`DBUserDetailsManager`（**类名随意**）实现的两个接口是 `UserDetailsManager`和 `UserDetailsPasswordService`。



**参考的是内存用户认证：不管是基于内存还是基于数据库的，都要实现这两个接口。**

<img src="https://cdn.nlark.com/yuque/0/2026/png/21376908/1770790820150-f9fd6dae-7b29-4e8c-b417-4b8cd981145b.png" width="883.2" title="" crop="0,0,1,1" id="u8e3fab96" class="ne-image" style="font-size: 16px">



**程序启动时：**

+ 实例化 `DBUserDetailsManager`对象。

**校验用户时：**

+ Spring Security 自动调用`DBUserDetailsManager`的`loadUserByUsername`方法从数据库中获取User对象。
+ 只要获取到 User 对象，后续的过程就和基于内存的用户认证流程一样了。

### 定义DBUserDetailsManager
```java
package com.jkweilai.spring.security.demo.config;

import com.baomidou.mybatisplus.core.conditions.query.QueryWrapper;
import com.jkweilai.spring.security.demo.mapper.UserMapper;
import com.jkweilai.spring.security.demo.pojo.User;
import jakarta.annotation.Resource;
import org.springframework.security.core.GrantedAuthority;
import org.springframework.security.core.userdetails.UserDetails;
import org.springframework.security.core.userdetails.UserDetailsPasswordService;
import org.springframework.security.core.userdetails.UsernameNotFoundException;
import org.springframework.security.provisioning.UserDetailsManager;

import java.util.ArrayList;
import java.util.Collection;

public class DBUserDetailsManager implements UserDetailsManager, UserDetailsPasswordService {
    @Override
    public UserDetails updatePassword(UserDetails user, String newPassword) {
        return null;
    }

    @Override
    public void createUser(UserDetails user) {

    }

    @Override
    public void updateUser(UserDetails user) {

    }

    @Override
    public void deleteUser(String username) {

    }

    @Override
    public void changePassword(String oldPassword, String newPassword) {

    }

    @Override
    public boolean userExists(String username) {
        return false;
    }

    @Resource
    private UserMapper userMapper;

    @Override
    public UserDetails loadUserByUsername(String username) throws UsernameNotFoundException {
        QueryWrapper<User> queryWrapper = new QueryWrapper<>();
        queryWrapper.eq("username", username);
        User user = userMapper.selectOne(queryWrapper);
        if(user == null){
            throw new UsernameNotFoundException(username);
        }else{
            
            // 查询数据库获取这个用户所关联的权限（现在给一个空的List集合）
            Collection<GrantedAuthority> authorities = new ArrayList<>();
            
            return new org.springframework.security.core.userdetails.User(
                    user.getUsername(),
                    user.getPassword(),
                    user.getEnabled(),
                    // 账号是否未过期
                    true,
                    // 凭证是否未过期
                    true,
                    // 用户是否未被锁定
                    true,
                    authorities // 权限列表
            );
        }
    }
}

```

### 将 UserDetailsService 纳入 IoC 容器的管理
修改WebSecurityConfig中的userDetailsService方法如下

```java
package com.jkweilai.spring.security.demo.config;

import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.security.config.annotation.web.configuration.EnableWebSecurity;
import org.springframework.security.core.userdetails.UserDetailsService;

@Configuration
@EnableWebSecurity
public class WebSecurityConfig {

    @Bean
    public UserDetailsService userDetailsService() {
        /*InMemoryUserDetailsManager manager = new InMemoryUserDetailsManager();
        manager.createUser(
                User
                        .withDefaultPasswordEncoder()
                        .username("user")
                        .password("123456")
                        .roles("USER")
                        .build());
        return manager;*/

        DBUserDetailsManager manager = new DBUserDetailsManager();
        return manager;
    }
}

```

**或者直接在DBUserDetailsManager类上添加****<font style="color:#DF2A3F;">@Component</font>****注解，只要纳入 IoC 容器的管理即可。**



测试：输入用户名 `admin`，密码 `password`，查看是否登录成功。

## 安全过滤器链的配置
### 默认配置
我们之前就说过：框架自带了一个**默认的安全过滤器链**。我们可以了解一下他的默认配置。

可以从官方手册中看到这个默认的配置：[https://docs.spring.io/spring-security/reference/servlet/configuration/java.html](https://docs.spring.io/spring-security/reference/servlet/configuration/java.html)



**以下这段配置就是默认的过滤器链，就是它的配置让程序走了 16 个过滤器：**



<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1759066562121-5332bb4a-0f0f-4240-9255-fbb6afc758c5.png" width="819.3333333333334" title="" crop="0,0,1,1" id="u29a3c329" class="ne-image" style="font-size: 16px">



把这段代码加入到 `WebSecurityConfig`中，然后我们来研究一下，默认的过滤器链都干了什么？**代码我改造了一下，可读性更好一些**。

```java
package com.jkweilai.spring.security.demo.config;

import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.security.config.Customizer;
import org.springframework.security.config.annotation.web.builders.HttpSecurity;
import org.springframework.security.config.annotation.web.configuration.EnableWebSecurity;
import org.springframework.security.web.SecurityFilterChain;

@Configuration
@EnableWebSecurity
public class WebSecurityConfig {
    @Bean
    public SecurityFilterChain securityWebFilterChain(HttpSecurity http) throws Exception{

        // 配置所有HTTP请求都需要登录才能访问
        http.authorizeHttpRequests(authorizeHttpRequestsCustomizer -> {
            authorizeHttpRequestsCustomizer.anyRequest().authenticated();
        });

        // 开启默认的表单登录页面（/login）
        http.formLogin(Customizer.withDefaults());

        // 开启HTTP Basic认证（浏览器弹窗登录）
        http.httpBasic(Customizer.withDefaults());

        // 构建并返回配置好的 SecurityFilterChain 对象
        return http.build();
    }
}

```



**默认的过滤器链拦截的是所有请求，官方文档有这样一段描述：**

<img src="https://cdn.nlark.com/yuque/0/2026/png/21376908/1770793789991-abbd675f-0733-403e-b29e-fffc5f3774a8.png" width="632" title="" crop="0,0,1,1" id="uee73981a" class="ne-image" style="font-size: 16px">



**如果要配置多个不同的安全过滤器链，可以参考官方文档，如下：****<font style="color:#DF2A3F;">不过一般一个项目只需要配置一个过滤器链即可</font>**

<img src="https://cdn.nlark.com/yuque/0/2026/png/21376908/1770793868551-d6daf421-dcce-4ed9-8b03-87f4fa5d36a2.png" width="834.4" title="" crop="0,0,1,1" id="u9f3b72ac" class="ne-image" style="font-size: 16px">



### 修改配置
**修改上面配置类中的代码就可以定制过滤器链。例如：**

`.formLogin(Customizer.withDefaults())`代码注释掉，则不再自动生成登录和登出页

当你再次访问时，浏览器会自动弹出****登录页来接收用户的输入，如下图：



<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1759103436632-799b127c-1722-48d6-9211-a9e790fe99f3.png" width="1273.3333333333333" title="" crop="0,0,1,1" id="u1602eeb0" class="ne-image" style="font-size: 16px">



**当你登录成功后，点击退出时，由于没有退出页，会出现以下的错误：**

****

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1759103509893-40385556-22cc-463d-b180-6e8db1c3b747.png" width="676.6666666666666" title="" crop="0,0,1,1" id="uabd70cf4" class="ne-image" style="font-size: 16px">



**我们之前的课程中提到过，默认情况下安全过滤器链上有 16 个过滤器，在 **`**DefaultSecurityFilterChain**`**中可以查看， 如下图所示：**

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1759030275483-fcddcd24-1350-4304-ab4e-cadc38c170e9.png" width="1015" title="" crop="0,0,1,1" id="wmEgL" class="ne-image" style="font-size: 16px">

当我们把 `.formLogin(Customizer.withDefaults())`注释掉之后，再次查看，过滤器链上只剩下 12 个过滤器了，如下图所示：

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1759103872853-6d987dc9-557b-47cb-8390-560a2dbf79ae.png" width="891.3333333333334" title="" crop="0,0,1,1" id="uaa8c1146" class="ne-image" style="font-size: 16px">

对比之后，你会发现少了这 4 个过滤器：

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1759104005840-e339f92f-fa85-45fc-b741-2cba598f1845.png" width="356" title="" crop="0,0,1,1" id="u05f102b6" class="ne-image" style="font-size: 16px">

这 4 个过滤器都是干啥的？

+ `**UsernamePasswordAuthenticationFilter**`：表单登录核心过滤器，处理表单登录的POST请求（默认 /login）
+ `**DefaultLoginPageGeneratingFilter**`：自动生成默认登录页面
+ `**DefaultLogoutPageGeneratingFilter**`：自动生成注销确认页面
+ `**DefaultResourcesFilter**`：这个过滤器负责提供一些默认的静态资源，在自动生成的登录页面中可能用到的一些基本样式或资源

当你注释掉 `.formLogin(Customizer.withDefaults())`就代表你告诉 `Spring Security`：我不再需要表单登录功能了，因此这 4 个过滤器就不需要再干活了。



另外，如果你将 `.httpBasic(Customizer.withDefaults());` 注释掉，过滤器 `BasicAuthenticationFilter` 将不再工作。

## 实现用户添加
**为什么还需要演示用户添加功能呢？**

+ **因为用户添加涉及到用户密码的加密，这个加密操作肯定要交给 Spring Security 框架来完成。**
+ **用户认证的时候（登录的时候）底层会自动调用 **`**<font style="color:#080808;background-color:#ffffff;">DBUserDetailsManager</font>**`**<font style="color:#080808;background-color:#ffffff;">的 </font>**`**<font style="color:#080808;background-color:#ffffff;">loadUserByUsername</font>**`**<font style="color:#080808;background-color:#ffffff;">方法。</font>**
+ **<font style="color:#080808;background-color:#ffffff;">用户添加的时候底层会自动调用 </font>**`**<font style="color:#080808;background-color:#ffffff;">DBUserDetailsManager</font>**`**<font style="color:#080808;background-color:#ffffff;">的 </font>**`**<font style="color:#080808;background-color:#ffffff;">createUser</font>**`**<font style="color:#080808;background-color:#ffffff;">方法。</font>**

### 编写 Controller
在 UserController 中添加以下代码：

```java
@PostMapping("/add")
public void add(@RequestBody User user){
    userService.saveUserDetails(user);
}
```

### 编写 Service
UserService 接口中添加以下方法：

```java
void saveUserDetails(User user);
```

UserServiceImpl 实现类中添加方法实现：

```java
@Resource
private DBUserDetailsManager manager;

@Override
public void saveUserDetails(User user) {
    // 密码加密
    UserDetails userDetails = org.springframework.security.core.userdetails.User
            .withDefaultPasswordEncoder()
            .username(user.getUsername())
            .password(user.getPassword())
            .build();
    manager.createUser(userDetails);
}
```

这里有个坑你要注意，以上代码要求 Spring 的 IoC 容器中必须要有 `DBUserDetailsManager`类型的 `bean`，但是 IoC 容器中没有这个 Bean，因为我们之前在配置类中编写的代码是这样的：

```java
@Bean
public UserDetailsService userDetailsService(){
    DBUserDetailsManager manager = new DBUserDetailsManager();
    return manager;
}
```

以上代码表示 IoC 容器中有一个类型叫做 `UserDetailsService`的 Bean，而不是 `DBUserDetailsManager`类型的 Bean。针对这种情况我们有两种解决方案：

+ **第一种：**修改以上代码的返回值类型为 `DBUserDetailsManager`
+ **第二种：**在 `DBUserDetailsManager`类上添加 `@Component` 注解。

这两种方式都可以。我们这里选择使用`@Component`注解，如下图：

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1759159124098-aa37be87-dbdb-4ea8-96bc-f65d653339d2.png" width="435" title="" crop="0,0,1,1" id="ud48f8697" class="ne-image" style="font-size: 16px">

把这个代码注释掉：

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1759159183995-1b50bf3b-54d0-44c3-8750-4d8b199224b8.png" width="785" title="" crop="0,0,1,1" id="ue8f25ec7" class="ne-image" style="font-size: 16px">

### 实现 createUser 方法
去实现 DBUserDetailsManager 中的 `createUser`方法：

```java
@Override
public void createUser(UserDetails userDetails) {
    User user = new User();
    user.setUsername(userDetails.getUsername());
    user.setPassword(userDetails.getPassword());
    user.setEnabled(true);
    userMapper.insert(user);
}
```

### 使用Swagger测试
添加依赖：

```xml
<!--swagger-->
<dependency>
    <groupId>com.github.xiaoymin</groupId>
    <artifactId>knife4j-openapi3-jakarta-spring-boot-starter</artifactId>
    <version>4.5.0</version>
</dependency>
```



**测试地址：**[http://localhost:8080/doc.html](http://localhost:8080/doc.html)

<img src="assets/image-20231206022701725.png" title="null" crop="0,0,1,1" id="wuly7" class="ne-image" style="font-size: 16px">



测试结果如下：显示没有权限（**要测试出这个效果还需要将之前注释掉的表单登录方式再打开**）

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1759190328439-71b084c5-4dc0-4f82-ba4a-71d1e84107e5.png" width="591" title="" crop="0,0,1,1" id="ub2a95a1e" class="ne-image" style="font-size: 16px">

什么原因？这是因为默认情况下，`Spring Security`开启了 `csrf`攻击防御功能。

### 关闭csrf攻击防御
**<font style="color:rgb(15, 17, 21);">Spring Security 默认开启了 csrf 攻击防御</font>**<font style="color:rgb(15, 17, 21);">：它会为每个表单生成一个唯一的、随机的“令牌”（Token）。当你提交表单（比如修改密码、转账）时，必须把这个令牌也一起提交上来。服务器会验证令牌是否正确。恶意网站 B 无法知道这个令牌是什么（</font>**<font style="color:rgb(15, 17, 21);">网站B无法知道令牌，是因为浏览器基于“同源策略”的安全限制，阻止了网站B的脚本读取网站A的Cookie或页面内容</font>**<font style="color:rgb(15, 17, 21);">），所以它伪造的请求就会失败。默认情况下，CSRF 防护是</font>**<font style="color:rgb(15, 17, 21);">开启</font>**<font style="color:rgb(15, 17, 21);">的，主要保护的是会改变服务器状态的请求（如 POST, PUT, DELETE）。</font>

<font style="color:rgb(15, 17, 21);"></font>

<font style="color:rgb(15, 17, 21);">我们可以看一下登录页的 HTML 源码，看看表单中有没有提交随机的“令牌”，源码如下：</font>

[http://localhost:8080/login](http://localhost:8080/login)

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1759190912126-547114d3-ec3b-4456-8221-22be0e0d790a.png" width="470" title="" crop="0,0,1,1" id="u464b9a97" class="ne-image" style="font-size: 16px">

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1759190946813-2911490f-0656-4d76-830d-4f3e50312b22.png" width="1625" title="" crop="0,0,1,1" id="ucc599c14" class="ne-image" style="font-size: 16px">

可以清楚的看到，`Spring Security`会为页面的 form 表单自动生成一个隐藏的 `_csrf`。



我们之前在实现添加用户功能的时候，由于没有编写前端页面，自然就没有把这个 `_csrf`字段的值提交给服务器，因此服务器判定没有权限。

当前我们解决这个问题的最快方式就是将默认的 `csrf`攻击防御功能关闭，可以在 `WebSecurityConfig`类的 `filterChain`方法中修改过滤规则，添加一下代码来关闭攻击防御功能：

```java
// 关闭csrf攻击防御功能（生产环境需要删除的代码）
http.csrf(csrf -> {
    csrf.disable();
});
```



再次重启服务器，测试添加用户的功能：

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1759191359141-ce26f7e0-e7f0-44bd-8040-bac2cb96d369.png" width="1351" title="" crop="0,0,1,1" id="ueb6cf79b" class="ne-image" style="font-size: 16px">

测试结果没有响应内容，这是正常的，因为 `UserController`的对应方法返回值类型是 void。

查看数据库表中的数据是否添加成功，很明显，我们已经成功了：

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1759191456965-5f8d2f62-bf25-4dcc-852b-eb45f16934ef.png" width="1529" title="" crop="0,0,1,1" id="u4874b709" class="ne-image" style="font-size: 16px">



再使用新添加的用户 `lisi/123456`进行登录，你会发现这个用户是可用的。

## 密码加密算法
**参考文档：**[**https://docs.spring.io/spring-security/reference/features/authentication/password-storage.html**](https://docs.spring.io/spring-security/reference/features/authentication/password-storage.html)

### 密码加密方式
#### 明文密码
密码以明文形式存储的问题：

+ 恶意用户通过SQL注入等手段获取到明文密码
+ 数据库管理员可能会将密码泄露

#### Hash算法
安全起见，加密技术一般都是单向转换，不可逆（只能加密不能解密），密码单向转换就必须用 Hash 算法，像常见的加密技术有 MD5、SHA-256、SHA-512 等，它们都使用了 Hash 算法。



只能加密不能解密，那 `Spring Security`是如何进行密码验证的呢？

1. 假设数据库表中保存的是通过 BCrypt 方式 Hash 后的密码。
2. 用户登录时会提交密码，`Spring Security`仍然使用 BCrypt 方式对密码进行 Hash。
3. 然后比对两个密文是否相等。



<font style="color:rgb(15, 17, 21);">Spring Security 的 PasswordEncoder 是一个专门用于</font>**<font style="color:rgb(15, 17, 21);">密码加密</font>**<font style="color:rgb(15, 17, 21);">和</font>**<font style="color:rgb(15, 17, 21);">验证</font>**<font style="color:rgb(15, 17, 21);">的接口。它提供了多种实现类，不同的实现采用了不同的</font>**<font style="color:rgb(15, 17, 21);">密码哈希算法</font>**<font style="color:rgb(15, 17, 21);">，如 BCrypt、PBKDF2 等，用于安全地存储和验证用户密码。</font>

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1759210202996-ef98ab70-50ff-4d64-999f-894a79d8180f.png" width="308.8" title="" crop="0,0,1,1" id="u6443fde7" class="ne-image" style="font-size: 16px">

PasswordEncoder 接口的源码如下：

```java
public interface PasswordEncoder {
    
    // 将明文密码编码为加密后的密码字符串
    String encode(CharSequence rawPassword);
    
    // 验证原始密码是否与加密后的密码匹配
    // rawPassword 是原始密码
    // encodedPassword 加密后的密码
    boolean matches(CharSequence rawPassword, String encodedPassword);

    default boolean upgradeEncoding(String encodedPassword) {
        return false;
    }
}
```



加密后的密文可以破解吗？单向转换，只能加密，不能解密。通常的破解方式是**采用猜测的方式进行暴力破解**。

#### 彩虹表（暴力破解）
彩虹表就像「电话号码反查手册」

普通电话簿（正常哈希）：

+ **姓名** → **电话号码**
+ 比如：张三 → 13800138000
+ 这就像：密码"123456" → 哈希"e10adc..."

彩虹表（反向查询）：

+ **电话号码** → **姓名**
+ 比如：13800138000 → 张三
+ 这就像：哈希"e10adc..." → 密码"123456"

为什么彩虹表很危险？想象一下：

+ 小偷提前编了一本超厚的《所有可能密码对应的哈希值大全》
+ 当他偷到你的哈希值时，就像查字典一样：
    - 输入：`e10adc...`
    - 一翻书：哦！原来密码是`123456`

彩虹表就是黑客提前准备好的「密码-哈希值反向查询字典」！

恶意用户使用称为彩虹表的预计算攻击工具。能够快速破解使用简单哈希算法（如MD5、SHA1）的密码。然而，现代密码存储通过**加盐**和**慢哈希函数**（如bcrypt、Argon2）有效防御彩虹表攻击。**加盐确保相同密码产生不同哈希值**，使预计算的彩虹表失效；**慢哈希函数大幅增加计算成本**，使得生成彩虹表变得不切实际。

#### 如何防御彩虹表
**加盐（Salt）** - 就像给每个人的密码加「独特调料」：

```plain
不加盐： "123456" → 哈希"e10adc..."  
加盐后： "123456+用户专属随机码" → 哈希"f82b9e..."（完全不同！）
```

这样小偷的那本「大全」就完全没用了，因为每个人的「调料」都不一样！



**大家可能会有一个疑问**，加盐之后最终还是一个字符串呀，只要是字符串应该就可以暴力破解呀？？？？

它确实还是个字符串。但问题在于规模和可行性。

**情景 1：不加盐（黑客轻松破解）**

```plain
黑客预先计算：
"123456" → 哈希A
"password" → 哈希B  
"abc123" → 哈希C
...
【一本通用字典，可攻击所有用户】
```

**情景 2：加盐后（黑客崩溃了）**

```plain
用户1：盐 = "x7!p2"
"123456x7!p2" → 哈希X

用户2：盐 = "k9$m4"  
"123456k9$m4" → 哈希Y

用户3：盐 = "r1@t8"
"123456r1@t8" → 哈希Z
...
【每个用户都需要一本新字典！】
```

<font style="color:rgb(15, 17, 21);">假设：</font>

+ <font style="color:rgb(15, 17, 21);">常用密码：1亿种组合</font>
+ <font style="color:rgb(15, 17, 21);">盐的长度：32位随机字符</font>

<font style="color:rgb(15, 17, 21);">那么需要预计算的组合：</font>

```plain
1亿个常用密码 × 43亿种可能的盐 = 43万亿亿个组合
```

<font style="color:rgb(15, 17, 21);">存储这些彩虹表需要：</font>

+ <font style="color:rgb(15, 17, 21);">不是100GB</font>
+ <font style="color:rgb(15, 17, 21);">不是100TB</font>
+ <font style="color:rgb(15, 17, 21);">而是</font>**<font style="color:rgb(15, 17, 21);">数百万个地球大小的硬盘</font>**<font style="color:rgb(15, 17, 21);">！</font>

<font style="color:rgb(15, 17, 21);">加盐的魔法不在于让密码「看不见」，而在于让黑客的</font>**<font style="color:rgb(15, 17, 21);">攻击成本从「买瓶可乐」变成「买下整个银河系」</font>**<font style="color:rgb(15, 17, 21);">！</font>

<font style="color:rgb(15, 17, 21);">所以你的直觉是对的——技术上还是能破解，但经济上完全不可行，这就是安全的本质！</font>

<font style="color:rgb(15, 17, 21);"></font>

**<font style="color:rgb(15, 17, 21);">加盐之后，数据库是如何存储的？后期又是如何进行认证的？</font>**

**<font style="color:rgb(15, 17, 21);">注册</font>**<font style="color:rgb(15, 17, 21);">：密码 → 生成随机盐 → 计算加盐哈希 → 存储(哈希+盐【盐值以明文存储，盐值公开也没关系：盐值的目的不是保密，而是确保唯一性】)  
</font>**<font style="color:rgb(15, 17, 21);">登录</font>**<font style="color:rgb(15, 17, 21);">：输入用户名和密码 → 根据用户名去数据库中查询对应的存储密码 → 从存储密码中读取盐值 → 计算 用户输入的密码+盐值 的哈希 → 比较数据库哈希</font>

#### 自适应单向函数（慢哈希函数）
**<font style="color:rgb(15, 17, 21);">可调节计算成本</font>**<font style="color:rgb(15, 17, 21);">的哈希函数，通过</font>**<font style="color:rgb(15, 17, 21);">增加计算时间</font>**<font style="color:rgb(15, 17, 21);">来防御暴力破解。</font>

随着硬件的不断发展，加盐哈希也不再安全。原因是，计算机可以每秒执行数十亿次哈希计算。这意味着我们可以轻松地破解每个密码。现在，开发人员开始使用自适应单向函数来存储密码。使用自适应单向函数验证密码时，故意占用资源（故意使用大量的CPU、内存或其他资源）。自适应单向函数允许配置一个"**工作因子**"，随着硬件的改进而增加，我们建议将“工作因子”调整到系统中验证密码需要约**一秒钟**的时间。这种权衡是为了让攻击者难以破解密码。自适应单向函数包括`bcrypt、PBKDF2、scrypt和argon2`。



**<font style="color:#DF2A3F;">防破解的核心原理是：让哈希计算变慢。</font>**

**<font style="color:#DF2A3F;">假设我生成密码的时候采用了 bcrypt 慢哈希，那么黑客在生成彩虹表的时候，自然也需要 bcrypt 进行生成。生成的速度放慢了，自然破解的时间就长了。</font>**

<font style="color:rgb(15, 17, 21);"></font>

**<font style="color:rgb(15, 17, 21);">传统快哈希（不安全）：</font>**

```java
MD5("password")    // 瞬间完成
SHA1("password")   // 瞬间完成
```

**自适应慢哈希（安全）：**

```java
bcrypt("password", cost=12)    // 需要约0.3秒
argon2("password", iterations=3) // 需要约0.5秒
```

**常见实现：**

```java
// BCrypt - 可调节工作因子
BCryptPasswordEncoder encoder = new BCryptPasswordEncoder(12);

// Argon2 - 可调节时间、内存、并行度参数
Argon2PasswordEncoder encoder = new Argon2PasswordEncoder(16, 32, 1, 65536, 3);
```

这个「慢」是精心设计的安全特性，不是性能缺陷！

### PasswordEncoder
#### BCryptPasswordEncoder
`BCrypt`是什么？BCrypt = 哈希函数 + 慢速特性。

使用 bcrypt 对密码进行哈希。该算法专为减缓计算速度而设计，能有效抵抗暴力破解。

建议将工作因子参数调整至密码验证耗时约 1 秒。BCryptPasswordEncoder 默认为强度 10，请根据实际系统性能测试并调整该参数。

#### Argon2PasswordEncoder
使用 Argon2 对密码进行哈希。该算法计算慢、占用内存大，能有效抵抗硬件破解。建议调整参数使验证耗时约 1 秒，当前实现需依赖 BouncyCastle 库。

#### Pbkdf2PasswordEncoder
使用 PBKDF2 对密码进行哈希。该算法通过多次迭代实现缓慢计算，能有效抵抗暴力破解。建议调整迭代次数，使密码验证耗时约 1 秒。

PBKDF2 已通过 FIPS（美国联邦信息处理标准）认证，适用于有合规性要求的安全场景。

FIPS 认证：美国联邦政府制定的安全标准，部分项目（如政府、金融、医疗系统）强制要求使用通过该认证的算法。

#### SCryptPasswordEncoder 
使用 Scrypt 对密码进行哈希。该算法通过大量内存占用和高计算成本，有效抵抗硬件破解。建议在实际运行环境中调整参数，使单次密码验证耗时约1秒。

#### 对比
| **<font style="color:rgb(15, 17, 21);">编码器</font>** | **<font style="color:rgb(15, 17, 21);">安全性</font>** | **<font style="color:rgb(15, 17, 21);">性能特点</font>** | **<font style="color:rgb(15, 17, 21);">适用场景</font>** | **<font style="color:rgb(15, 17, 21);">备注</font>** |
| --- | --- | --- | --- | --- |
| **<font style="color:rgb(15, 17, 21);">BCryptPasswordEncoder</font>** | <font style="color:rgb(15, 17, 21);">高</font> | <font style="color:rgb(15, 17, 21);">CPU密集型，计算慢</font> | <font style="color:rgb(15, 17, 21);">通用场景，Web应用</font> | <font style="color:rgb(15, 17, 21);">当前最广泛使用</font> |
| **<font style="color:rgb(15, 17, 21);">Argon2PasswordEncoder</font>** | <font style="color:rgb(15, 17, 21);">最高</font> | <font style="color:rgb(15, 17, 21);">CPU+内存密集型，抗硬件破解</font> | <font style="color:rgb(15, 17, 21);">高安全要求系统</font> | <font style="color:rgb(15, 17, 21);">密码哈希竞赛冠军</font> |
| **<font style="color:rgb(15, 17, 21);">Pbkdf2PasswordEncoder</font>** | <font style="color:rgb(15, 17, 21);">中高</font> | <font style="color:rgb(15, 17, 21);">CPU密集型，可调迭代次数</font> | <font style="color:rgb(15, 17, 21);">需要合规认证的项目</font> | <font style="color:rgb(15, 17, 21);">通过FIPS认证</font> |
| **<font style="color:rgb(15, 17, 21);">SCryptPasswordEncoder</font>** | <font style="color:rgb(15, 17, 21);">高</font> | <font style="color:rgb(15, 17, 21);">内存密集型，高内存占用</font> | <font style="color:rgb(15, 17, 21);">抵抗硬件破解场景</font> | <font style="color:rgb(15, 17, 21);">需要大量内存资源</font> |


### 测试 BCryptPasswordEncoder
编写测试程序测试BCryptPasswordEncoder，代码如下：

```java
package com.jkweilai.spring.security.demo;

import org.junit.jupiter.api.Test;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.security.crypto.bcrypt.BCryptPasswordEncoder;

@SpringBootTest
class SpringSecurityDemoApplicationTests {

    @Test
    void testBcrypt() {
        BCryptPasswordEncoder encoder = new BCryptPasswordEncoder();
        String password = encoder.encode("password");

        // 每一次执行输出结果都是不同的。
        // $2a$10$.GyF8EJtw4xeX/MrYTp6xOA2Sz1gC.jj7Hv7v5o8j/B4.rvtlwvKW
        // $2a$ ：算法标识,这表示使用的是 BCrypt 算法
        // 10$：工作因子,默认10，最小4，最大31。这里的 10 意思是 2¹⁰ 次迭代（即 1024 轮）
        // .GyF8EJtw4xeX/MrYTp6xO ：盐。这是一个 22 个字符（16字节）的随机值
        // A2Sz1gC.jj7Hv7v5o8j/B4.rvtlwvKW ：最终的哈希结果，经过 1024 轮计算后得到的 24 字节 的最终密文
        System.out.println(password);

        // 虽然每一次密码都是不一样的，但是这个结果是true？为什么？
        // 不一样是因为盐值不同导致的不同，matches方法每一次都会从密文中提取最新盐值。然后将最新盐值和密码结合之后再重新哈希。
        // 整个过程用户是无感知的。
        System.out.println(encoder.matches("password", password));
    }

}

```

### DelegatingPasswordEncoder
#### 存储的密码为什么会有一个前缀
数据库表中实际存储的密码形式为：`{bcrypt}$2a$10$UUpDXTOLhFUEBCAcuHKQjOnPWKcCt4n893aMDInjVZveR1xWlsO9G`

为什么前面会多一个 `{bcrypt}`？

简单直接的回答是：`{bcrypt}`** 这个前缀是一个密码编码标识符，它的主要作用是告诉 Spring Security：“这个密码是使用 BCrypt 算法进行哈希处理的”。**



**为什么需要这个前缀？—— 核心原因：支持多种密码编码方案**

在现代应用中，你可能会遇到多种不同方式编码的密码：

+ **新用户**：使用当前最推荐的 `BCrypt` 算法进行编码。
+ **老系统迁移来的用户**：他们的密码可能是用 `PBKDF2`、`SCrypt` 甚至是不安全的 `MD5` 或 `SHA-256`（无盐）编码的。
+ **未来**：你可能希望将算法升级到更强大的，比如 `Argon2`。

如果密码字符串没有标识符，认证系统在验证用户输入的密码时，会遇到一个难题：**我该用哪种算法来验证这个密码？**

`{bcrypt}` 前缀就是为了解决这个问题而生的。它解耦了密码存储和验证逻辑。



**格式规范：DelegatingPasswordEncoder**

Spring Security 5 引入了一个核心类叫做 `DelegatingPasswordEncoder`（委托密码编码器）。它就是实现这套带标识符密码体系的“大脑”。

它的工作流程如下：

1. **存储密码（编码）：**
    - 当你调用 `passwordEncoder.encode(rawPassword)` 时，`DelegatingPasswordEncoder` 会委托给当前配置的默认编码器（例如 `BCryptPasswordEncoder`）去生成哈希值。
    - 在最终的存储字符串前，它会**自动加上对应的标识符**，格式为 `{id}encodedPassword`。
2. **验证密码（匹配）：**
    - 当需要验证密码时，`DelegatingPasswordEncoder` 会从存储的密码字符串开头**提取 **`{id}`。
    - 根据这个 `id`，它找到一个对应的、专门处理这种算法的 `PasswordEncoder`。
    - 然后，它把用户输入的明文密码和存储的哈希值（去掉 `{id}` 的部分）交给这个特定的 `PasswordEncoder` 去验证。



#### 存储密码时的源码分析
<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1759244656341-26c8cfbe-9d5a-45b2-b87d-8f84f59050a0.png" width="833.6" title="" crop="0,0,1,1" id="uc5289b21" class="ne-image" style="font-size: 16px">

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1759244701210-48996c2a-56d4-4eeb-a93e-a026f241144f.png" width="901.6" title="" crop="0,0,1,1" id="u686b9839" class="ne-image" style="font-size: 16px">

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1759244771438-e5bad77d-a0cf-4d81-b891-aeabaa972add.png" width="684.8" title="" crop="0,0,1,1" id="u52b8e266" class="ne-image" style="font-size: 16px">

#### 匹配密码时的源码分析
启动服务器，访问登录页，输入用户名和密码之后，会走到下面这个代码的断点上：

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1759245130649-8b402b1c-12cf-4284-9bd2-a6513da46fe4.png" width="1059.2" title="" crop="0,0,1,1" id="u301ba828" class="ne-image" style="font-size: 16px">

可以针对这个代码每一行进行调试，通过它来理解在哪个位置去掉的前缀，最终是怎么进行的比较！

## 自定义登录页面
`Spring Security`中执行安全过滤器链的时候，其中一个过滤器为我们生成了默认的登录页，如果不想使用默认的登录页，也可以定制。

我们先来看看登录页的显示对应的请求 URL 是什么？

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1759246246462-42a9a92e-a917-4b29-99bb-8c9a1388d79a.png" width="495.2" title="" crop="0,0,1,1" id="ucd69d532" class="ne-image" style="font-size: 16px">

很显然登录页对应的 URL 是：[http://localhost:8080/login](http://localhost:8080/login)

那我们首先第一件事应该做的是：编写一个 `/login`对应的 `Controller`，让请求路径 `/login`走我们的控制器逻辑。

### 编写 LoginController
```java
package com.jkweilai.spring.security.demo.controller;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;

@Controller
public class LoginController {

    @GetMapping("/login")
    public String login(){
        return "login";
    }
    
}

```

接下来，我们肯定是需要在 `template`目录下编写一个 `login.html`。

### 编写登录页
resources/templates/login.html

```html
<!DOCTYPE html>
<html lang="en" xml:ns="https://www.thymeleaf.org">
<head>
    <meta charset="UTF-8">
    <title>自定义登录页</title>
</head>
<body>
<h1>自定义登录页</h1>
</body>
</html>
```

内容先不要写全，先简单测试一下，看看能不能跳转到我们自定义的登录页。启动服务器测试：[http://localhost:8080/login](http://localhost:8080/login)

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1759246572066-66c2ca97-ae96-45d6-b52b-85e3da519de3.png" width="518.4" title="" crop="0,0,1,1" id="u0e6ea089" class="ne-image" style="font-size: 16px">

测试结果是：并没有像我们预期的那样，直接跳转到我们自定义的登录页了。这是为什么呢？

主要原因是因为：安全过滤器链没有重新定制，仍然走的是 `Spring Security`默认生成的 `form`表单登录页。压根没走我们自定义的 `LoginController`。

因此我们需要重新定义安全过滤器链中的自动生成登录表单的环节。

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1759246763877-23ad1423-3cd2-4c8c-b2c9-f3d00ed5d355.png" width="956" title="" crop="0,0,1,1" id="u524ca6fd" class="ne-image" style="font-size: 16px">



### 配置SecurityFilterChain
将 `WebSecurityConfig`中的 `.formLogin`部分的代码进行修改，如下：

```java
.formLogin(form -> {
    form.loginPage("/login");
})
```

再次测试，结果如下：

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1759246967445-ccfb02e4-dbaa-4219-b8cc-e9035733cfe5.png" width="293.6" title="" crop="0,0,1,1" id="u4108af74" class="ne-image" style="font-size: 16px">

什么原因导致的？

主要是因为默认的安全过滤器链对所有的请求都进行身份认证，包括我们现在 `/login`请求也会拦截，导致递归重定向。

怎么办？继续添加以下配置，让 `/login`请求不需要身份认证就能访问：

```java
.formLogin(form -> {
    form.loginPage("/login").permitAll(); // 登录页不需要认证就可以访问
})
```

再次测试：成功了！！

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1759247112226-37977cd3-be8a-4885-82e7-5b59f4efcbf8.png" width="297.6" title="" crop="0,0,1,1" id="u4fcb5884" class="ne-image" style="font-size: 16px">

### 完善登录页
在`login.html`添加登录表单，保证能够提交登录的用户名和密码：

```html
<!DOCTYPE html>
<html lang="en" xml:ns="https://www.thymeleaf.org">
<head>
    <meta charset="UTF-8">
    <title>自定义登录页</title>
</head>
<body>
<h1>自定义登录页</h1>
<form th:action="@{/login}" method="post">
用户名：<input type="text" name="username"><br>
密码：<input type="password" name="password"><br>
<input type="submit" value="登录">
</form>
</body>
</html>
```

重启服务器，测试如下：

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1759247574084-013f058a-6918-450c-941a-d8f79084a171.png" width="274.4" title="" crop="0,0,1,1" id="ued29d90d" class="ne-image" style="font-size: 16px">

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1759247585445-193e9b15-af62-49cf-987a-f0b1e9700574.png" width="302.4" title="" crop="0,0,1,1" id="u15c0f22f" class="ne-image" style="font-size: 16px">

### 定制登录失败的返回地址
测试一下，登录失败之后，默认的返回地址是什么？故意输错用户名和密码

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1759247776779-d836b89e-4156-4c08-b0d8-0e51275697c4.png" width="188.8" title="" crop="0,0,1,1" id="ua0448ee4" class="ne-image" style="font-size: 16px">

返回地址是：[http://localhost:8080/login?error](http://localhost:8080/login?error)



如果你需要定制出错之后的返回地址。可以进行以下配置：

```java
.formLogin(form -> {
    form.loginPage("/login").permitAll()
        .failureUrl("/login?err"); // 自定义登录失败后的返回地址
})
```

再次测试，故意输错用户名密码，看看地址栏上的地址，可以看到自定义配置生效了：

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1759247963711-fb780b1e-8de7-4a48-a26a-3bf3ded90562.png" width="200" title="" crop="0,0,1,1" id="uc864ff72" class="ne-image" style="font-size: 16px">



你可能会问？定制这个干啥？有什么用？答案是：在页面上能够用到。如下：

在 `login.html`中添加错误处理代码

```html
<!DOCTYPE html>
<html lang="en" xml:ns="https://www.thymeleaf.org">
<head>
    <meta charset="UTF-8">
    <title>自定义登录页</title>
</head>
<body>
<h1>自定义登录页</h1>
<form th:action="@{/login}" method="post">
用户名：<input type="text" name="username"><br>
密码：<input type="password" name="password"><br>
<input type="submit" value="登录">
</form>

<div th:if="${param.err}">用户名不存在或者密码错误</div>

</body>
</html>
```

当登录失败的时候，测试结果如下：

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1759248168796-94cfbc2e-b75f-4f34-b5f1-c13963aa9b9b.png" width="292" title="" crop="0,0,1,1" id="u0f036543" class="ne-image" style="font-size: 16px">

### 定制登录表单的参数名
默认要求在登录表单提交时，提交的参数名必须是：<font style="color:#DF2A3F;">username</font>=xxx&<font style="color:#DF2A3F;">password</font>=yyy

这是 `Spring Security`固定死的，可以通过 `UsernamePasswordAuthenticationFilter`的源码来查看：

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1759248288428-0ccf0a99-2681-442c-8a59-4dffc6c72a40.png" width="960" title="" crop="0,0,1,1" id="ufd39f7d8" class="ne-image" style="font-size: 16px">

如果你想定制，可以添加以下配置：

```java
.formLogin(form -> {
    form.loginPage("/login").permitAll()
        .failureUrl("/login?err")
        .usernameParameter("name") // 自定义表单参数名
        .passwordParameter("pwd"); // 自定义表单参数名
})
```

配置修改了，那你的登录表单的参数名就需要跟着修改，代码如下：

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1759248452450-5b7633ea-2b2c-49cb-b894-d6f5c474143d.png" width="535.2" title="" crop="0,0,1,1" id="u9e46b93e" class="ne-image" style="font-size: 16px">

再次测试，看看是否能够正常登录。经过测试，是可以的。

### 关于登录表单是否自动生成 csrf 隐藏字段
之前我们把 `csrf`攻击防御功能关闭了，现在把它打开，将代码注释掉：

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1759248735015-f4033c40-6619-4168-984d-e609a138e278.png" width="446.4" title="" crop="0,0,1,1" id="u23795366" class="ne-image" style="font-size: 16px">

访问登录页，看看有没有 csrf 隐藏字段，可以看到是有的：

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1759248790509-8c3a4f50-1f78-4c62-8d47-f87ba9a36b69.png" width="1020" title="" crop="0,0,1,1" id="u8f646425" class="ne-image" style="font-size: 16px">

我们把 `login.html`中的动态参数代码修改一下：

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1759248849004-2a19f63c-bc0f-45c5-9b5d-3a8c86210c5c.png" width="555.2" title="" crop="0,0,1,1" id="u37dc3718" class="ne-image" style="font-size: 16px">

上图代码修改为：

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1759248902302-7dbe05fa-39ad-4773-8521-5f632dba4c46.png" width="508" title="" crop="0,0,1,1" id="u06a8ea92" class="ne-image" style="font-size: 16px">

再次访问登录页，查看源码，如下：

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1759248931496-096f49af-96e3-4f67-91bd-88c3731ef981.png" width="336.8" title="" crop="0,0,1,1" id="uc206c6ae" class="ne-image" style="font-size: 16px">

可以看到隐藏的 csrf 字段没有了。因此要注意：登录表单需要使用动态参数语法。也就是以下代码：

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1759248994168-a58e330b-bb10-4096-8d9b-81a0781349c9.png" width="517.6" title="" crop="0,0,1,1" id="ubc3ba356" class="ne-image" style="font-size: 16px">

