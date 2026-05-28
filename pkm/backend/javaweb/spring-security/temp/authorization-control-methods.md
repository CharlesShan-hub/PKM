# 授权
## 两种常见的权限控制方式
在 Spring Security 中，授权管理非常灵活，可以帮我们实现两种常见的权限控制需求：

**第一种：用户 → 权限 → 资源**  
这种方式比较直接，每个用户都有哪些具体的操作权限。比如：

+ 张三拥有“添加用户”和“查看用户列表”的权限
+ 李四只有“查看用户列表”的权限

**第二种：用户 → 角色 → 权限 → 资源**  
这种方式更加常用，通过角色来管理权限分组。比如：

+ 张三的角色是“管理员”，拥有所有操作权限
+ 李四的角色是“普通用户”，只能查看信息，不能修改

简单来说，第一种是直接给用户分配具体权限，第二种是先给角色分配权限，再把角色分配给用户，这样管理起来更加方便和规范。



这里提到的**资源**是什么？资源就是权限控制所要保护的具体对象。它可以是：

+ 一个URL地址
+ 一个页面元素（如按钮、菜单）
+ 一条数据或一个数据字段

## 授权策略
`Spring Security`中提供了两种授权策略：

+ 基于 Request 的授权
+ 基于方法的授权

| **方面** | **基于 Request 的授权** | **基于方法的授权** |
| --- | --- | --- |
| **控制层面** | **全局层面**（过滤器） | **业务方法层面**（AOP） |
| **控制粒度** | **粗粒度**（按URL分组控制） | **细粒度**（按具体操作控制） |
| **好比** | **大楼保安** | **部门经理** |
| **常用场景** | 控制页面/菜单访问 | 控制具体业务操作、数据权限 |


**最佳实践**：两者通常结合使用。

+ 先用**基于Request的授权**把守大门，阻止非法用户进入敏感区域。
+ 再用**基于方法的授权**在内部进行精细控制，确保用户只能执行被允许的具体操作。

## 基于 Request 授权的代码实现
### 用户-权限-资源
**需求：**

+ 具有 `USER_LIST` 权限的用户可以访问 `/user/list` 接口
+ 具有 `USER_ADD` 权限的用户可以访问 `/user/add` 接口

#### 第一步：配置 哪个权限可以访问哪个资源
先在 `SecurityFilterChain`中配好规则：**<font style="color:#DF2A3F;">哪个权限</font>****可以访问****<font style="color:#DF2A3F;">哪个资源</font>**

```java
http.authorizeHttpRequests(
        // authorize 是 AuthorizeHttpRequestsConfigurer 对象，用于定义具体的授权规则
        authorize -> authorize
                // 有 USER_LIST 权限的用户可以访问 /user/list
                .requestMatchers("/user/list").hasAuthority("USER_LIST")
                // 有 USER_ADD 权限的用户可以访问 /user/add
                .requestMatchers("/user/add").hasAuthority("USER_ADD")
                // 匹配所有传入的 HTTP 请求
                .anyRequest()
                // 要求所有请求都必须经过身份认证（用户必须已登录）
                .authenticated()
)
```

**<font style="color:#DF2A3F;">配置权限的代码必须放到 </font>**`**<font style="color:#DF2A3F;">anyRequest()</font>**`**<font style="color:#DF2A3F;">之前。（实际开发中应该从数据库中加载权限规则，不应该在程序中硬编码）</font>**

#### 第二步：授予 哪个用户拥有哪些权限
第一步中我们只是配置好哪个权限可以访问哪个资源。还没有给**具体的用户**授予**具体的权限**。这一步我们来给具体的用户授予具体的权限。用户拥有哪一个权限，这个**数据**其实已经在数据库表中保存好了。我们只需要将数据库表中这个用户对应的权限列表查询出来，执行下面代码的 `add`方法来完成最终的授权。这段代码需要在登录阶段的 `loadUserByUsername`方法中进行，因为在这个方法中，它会根据用户名获取用户信息，而这个用户信息中包含了从数据库表中动态查询的权限列表。我们学习阶段就不再查询数据库了，直接写死了。

在`DBUserDetailsManager` 中的 `loadUserByUsername()`方法上编写代码：

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1759373495502-f61cb7ba-31bd-461a-aa8b-bd14c5d5d1be.png" width="676.4444444444445" title="" crop="0,0,1,1" id="u2b0dddf1" class="ne-image" style="font-size: 16px">

具体代码如下：

```java
Collection<GrantedAuthority> authorities = new ArrayList<>();
// 匿名内部类方式可以
authorities.add(new GrantedAuthority() {
    @Override
    public String getAuthority() {
        return "USER_LIST";
    }
});
// lambda表达式也可以
authorities.add(() -> "USER_ADD");
```



**测试如下：**

**第一步：先登录系统**

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1759374877289-ddea0619-4b84-4b46-af97-b294e932d756.png" width="372.8888888888889" title="" crop="0,0,1,1" id="u1e839552" class="ne-image" style="font-size: 16px">

通过结果看到用户确实有这两个权限。

**第二步：看看用户是否可以正常访问 **`**/user/list**`**和 **`**/user/add**`

`/user/list`

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1759374129348-cb0ba34c-e7d4-47de-b8c2-4b766d535e6b.png" width="668.8888888888889" title="" crop="0,0,1,1" id="u93884b8d" class="ne-image" style="font-size: 16px">

`/user/add`

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1759374268238-0f5c1e67-3746-42e9-8f47-5294a96ceaa4.png" width="757.7777777777778" title="" crop="0,0,1,1" id="uffa7edd5" class="ne-image" style="font-size: 16px">

查看数据库表有没有添加成功：

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1759374384613-cc0c0991-be61-4604-91d7-225b629e9963.png" width="675.1111111111111" title="" crop="0,0,1,1" id="u8ebaf6a3" class="ne-image" style="font-size: 16px">



**第三步：收回一个 **`**/user/list**`**权限，看看结果是怎么样的**

将 `/user/list`权限注释掉，如下：

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1759374498099-b829eca6-1673-45d7-a74e-9a25f0939864.png" width="633.3333333333334" title="" crop="0,0,1,1" id="u5369d162" class="ne-image" style="font-size: 16px">



再次测试 `/user/list`请求：

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1759374575426-9293f060-b760-4b16-a554-c793a0d471cb.png" width="655.1111111111111" title="" crop="0,0,1,1" id="u3715f962" class="ne-image" style="font-size: 16px">

当访问了一个没有授权的接口，应该给前端系统返回一个 JSON 。

#### 第三步：请求未授权的接口返回 JSON
**第一步：编写权限不足的回调处理器：编写 **`**AccessDeniedHandler**`**接口的实现类**

```java
package com.jkweilai.spring.security.demo.config;

import com.alibaba.fastjson2.JSON;
import jakarta.servlet.ServletException;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.security.access.AccessDeniedException;
import org.springframework.security.web.access.AccessDeniedHandler;

import java.io.IOException;
import java.util.HashMap;
import java.util.Map;

public class MyAccessDeniedHandler implements AccessDeniedHandler {

    @Override
    public void handle(HttpServletRequest request, HttpServletResponse response, AccessDeniedException accessDeniedException) throws IOException, ServletException {
        // 封装数据
        Map<String, Object> map = new HashMap<>();
        map.put("code", -1);
        map.put("msg", "没有权限");
        // 转换JSON
        String json = JSON.toJSONString(map);
        // 响应JSON
        response.setContentType("application/json;charset=utf-8");
        response.getWriter().write(json);
    }
}

```



**第二步：在**`**SecurityFilterChain**`**中进行如下的配置：**

```java
http.exceptionHandling(exception -> {
    exception.authenticationEntryPoint(new MyAuthenticationEntryPoint()); 
    // 这是新增的代码
    exception.accessDeniedHandler(new MyAccessDeniedHandler()); // 请求未授权的接口时
});
```



测试如下：当用户没有 `USER_LIST`权限时，访问 `/user/list`请求，就会出现下面的效果

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1759375481575-9804bf7f-d4be-41b6-821d-7868f2d9df69.png" width="363.1111111111111" title="" crop="0,0,1,1" id="u116d2aaa" class="ne-image" style="font-size: 16px">



**另外，这里需要说一下，以上两步代码，也可以合并成一步，采用 lambda 表达式来实现，代码如下：**

```java
http.exceptionHandling(exception -> {
    exception.authenticationEntryPoint(new MyAuthenticationEntryPoint()); // 请求未认证的接口时
    // 新增的代码
    // 请求未授权的接口时
    exception.accessDeniedHandler((request, response, e) -> {
        // 封装数据
        Map<String, Object> map = new HashMap<>();
        map.put("code", -1);
        map.put("msg", "没有权限");
        // 转换JSON
        String json = JSON.toJSONString(map);
        // 响应JSON
        response.setContentType("application/json;charset=utf-8");
        response.getWriter().write(json);
    });
});
```

实际上之前编写的所有回调，都可以采用 lambda 表达式来完成。

### 用户-角色-资源
需求：角色为 `ADMIN` 的用户才可以访问 `/user/**` 路径下的资源

#### 配置哪个角色可以访问哪些资源
在 `SecurityFilterChain`中进行配置，先将之前的权限配置注释掉，进行角色配置：

```java
http.authorizeHttpRequests(
        // authorize 是 AuthorizeHttpRequestsConfigurer 对象，用于定义具体的授权规则
        authorize -> authorize
                // 有 USER_LIST 权限的用户可以访问 /user/list
                //.requestMatchers("/user/list").hasAuthority("USER_LIST")
                // 有 USER_ADD 权限的用户可以访问 /user/add
                //.requestMatchers("/user/add").hasAuthority("USER_ADD")
                // 角色ADMIN可以访问/user/**
                .requestMatchers("/user/**").hasRole("ADMIN")
                // 匹配所有传入的 HTTP 请求
                .anyRequest()
                // 要求所有请求都必须经过身份认证（用户必须已登录）
                .authenticated()
)
```

#### 授予 哪个用户拥有哪些角色
在实际开发中，用户对应的角色信息同样是存储到数据库表当中的，应该查询数据库，动态获取该用户拥有哪些角色。学习阶段就硬编码了。**<font style="color:#DF2A3F;">把之前授予权限的代码注释掉</font>**。编写以下代码来完成授予角色：

在 `DBUserDetailsManager` 中的 `loadUserByUsername` 方法中编写代码：

```java
// 不是 return new 了。
// 是通过调用 User类的静态方法了。
return org.springframework.security.core.userdetails.User
        .withUsername(user.getUsername())
        .password(user.getPassword())
        .accountLocked(false) // 用户未锁定
        .credentialsExpired(false) // 凭证未过期
        .disabled(false) // 账户启用
        .roles("ADMIN") // 授予角色（可以授予多个角色） .roles("ADMIN", "USER")
        .build();
```



**测试：**

**第一步：先登录，看看用户的角色是不是：**`**ROLE_ADMIN**`

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1759378487125-9bfdd381-33ad-4615-b213-ae1396744a49.png" width="361.3333333333333" title="" crop="0,0,1,1" id="u58a78699" class="ne-image" style="font-size: 16px">



**第二步：看看用户是否可以访问 **`**/user/list**`**和 **`**/user/add**`

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1759378521802-694d3dfc-037d-4263-b96f-d7c10569ced0.png" width="704" title="" crop="0,0,1,1" id="ud75204b5" class="ne-image" style="font-size: 16px">



**第三步：将用户授予的角色修改为 **`**USER**`

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1759378571794-912257af-3eae-4210-bfcb-84a77119a8cb.png" width="622.6666666666666" title="" crop="0,0,1,1" id="u3eb8a907" class="ne-image" style="font-size: 16px">



**第四步：重启服务器，再看看用户是否可以访问 **`**/user/list**`**和 **`**/user/add**`

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1759378659102-4e17c4f6-b803-4388-9e0e-a90254e57cbe.png" width="392" title="" crop="0,0,1,1" id="u0292b496" class="ne-image" style="font-size: 16px">

### 用户-角色-权限-资源
RBAC（Role-Based Access Control，基于角色的访问控制）是一种常用的数据库设计方案，它将用户的权限分配和管理与角色相关联。以下是一个基本的 `RBAC` 数据库设计方案的示例：

1. 用户表（User table）：包含用户的基本信息，例如用户名、密码和其他身份验证信息。

| 列名 | 数据类型 | 描述 |
| --- | --- | --- |
| user_id | int | 用户ID |
| username | varchar | 用户名 |
| password | varchar | 密码 |
| email | varchar | 电子邮件地址 |
| ... | ... | ... |


2. 角色表（Role table）：存储所有可能的角色及其描述。

| 列名 | 数据类型 | 描述 |
| --- | --- | --- |
| role_id | int | 角色ID |
| role_name | varchar | 角色名称 |
| description | varchar | 角色描述 |
| ... | ... | ... |


3. 权限表（Permission table）：定义系统中所有可能的权限。

| 列名 | 数据类型 | 描述 |
| --- | --- | --- |
| permission_id | int | 权限ID |
| permission_name | varchar | 权限名称 |
| description | varchar | 权限描述 |
| ... | ... | ... |


4. 用户角色关联表（User-Role table）：将用户与角色关联起来。

| 列名 | 数据类型 | 描述 |
| --- | --- | --- |
| user_role_id | int | 用户角色关联ID |
| user_id | int | 用户ID |
| role_id | int | 角色ID |
| ... | ... | ... |


5. 角色权限关联表（Role-Permission table）：将角色与权限关联起来。

| 列名 | 数据类型 | 描述 |
| --- | --- | --- |
| role_permission_id | int | 角色权限关联ID |
| role_id | int | 角色ID |
| permission_id | int | 权限ID |
| ... | ... | ... |


在这个设计方案中，用户可以被分配一个或多个角色，而每个角色又可以具有一个或多个权限。通过对用户角色关联和角色权限关联表进行操作，可以实现灵活的权限管理和访问控制。

它的核心好处就是“批量管理”。不用给成百上千的用户一个个分配具体权限，只需要给几个角色分配好权限，然后把用户放进对应角色里即可，修改权限时也只需修改角色，所有属于该角色的用户权限会自动更新，非常高效。

## 基于方法授权的代码实现
### 开启方法授权
如果要开启细粒度的方法授权，则需要在配置文件`WebSecurityConfig`上添加如下注解：

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1759379375268-86d54cd1-72ed-43e3-84a7-2418bbad7ee6.png" width="444.8888888888889" title="" crop="0,0,1,1" id="u9fae198d" class="ne-image" style="font-size: 16px">

```java
@EnableMethodSecurity
```



**<font style="color:#DF2A3F;">此时你需要把之前的授权代码注释掉：把红框中的也注释掉。在这个类中配置的都是基于 Request 的授权。</font>**

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1759380832892-9713a7c4-0a98-42b7-b757-56ac12ed670c.png" width="709.7777777777778" title="" crop="0,0,1,1" id="u5bcf5b8c" class="ne-image" style="font-size: 16px">

### 给用户授予角色
在 `DBUserDetailsManager`的 `loadUserByUsername`方法中授予角色：

```java
return org.springframework.security.core.userdetails.User
        .withUsername(user.getUsername())
        .password(user.getPassword())
        .accountLocked(false) // 用户未锁定
        .credentialsExpired(false) // 凭证未过期
        .disabled(false) // 账户启用
        .roles("ADMIN") // 授予角色
        .build();
```

使用授权注解标注要控制的方法，找到你要精确控制的方法，例如 `UserController`类中的方法：

```java
// 用户的角色是ADMIN，并且用户名是admin时，才能访问这个方法。
@PreAuthorize("hasRole('ADMIN') and authentication.name == 'admin'")
@GetMapping("/list")
public List<User> listUser(){
    return userService.list();
}

// 用户的角色是USER才可以访问这个方法
@PreAuthorize("hasRole('USER')")
@PostMapping("/add")
public void add(@RequestBody User user){
    userService.saveUserDetails(user);
}
```



**测试：**

第一步：使用 admin 用户登录，看看能不能访问 `/user/list`（预期是可以访问）

第二步：使用 admin 用户登录，看看能不能访问 `/user/add`（预期是不能访问）

### 给用户授予权限
在 `DBUserDetailsManager`的 `loadUserByUsername`方法中授予权限：

```java
return org.springframework.security.core.userdetails.User
        .withUsername(user.getUsername())
        .password(user.getPassword())
        .accountLocked(false) // 用户未锁定
        .credentialsExpired(false) // 凭证未过期
        .disabled(false) // 账户启用
        //.roles("ADMIN") // 授予角色
        .authorities("USER_ADD", "USER_EDIT") // 授予权限（注意授予权限的代码和授予角色的代码不可共存）
        .build();
```

使用授权注解标注要控制的方法，找到你要精确控制的方法，例如 `UserController`类中的方法：

```java
// 有 USER_LIST 权限的用户可以访问该方法
@PreAuthorize("hasAuthority('USER_LIST')")
@GetMapping("/list")
public List<User> listUser(){
    return userService.list();
}

// 有 USER_ADD 权限的用户可以访问该方法
@PreAuthorize("hasAuthority('USER_ADD')")
@PostMapping("/add")
public void add(@RequestBody User user){
    userService.saveUserDetails(user);
}
```



**测试：**

第一步：使用任意用户登录，看看能不能访问 `/user/list`（预期是不能访问）

第二步：使用任意用户登录，看看能不能访问 `/user/add`（预期是能访问）



### 方法上的 SpEL 表达式


针对方法进行授权时，这个`@PreAuthorize`注解中 `value`属性值是一个 `SpEL`表达式。`Security`中常用的表达式如下，可以自行参考：

| **<font style="color:rgb(15, 17, 21);">表达式</font>** | **<font style="color:rgb(15, 17, 21);">说明</font>** |
| --- | --- |
| `<font style="color:rgb(15, 17, 21);background-color:rgb(235, 238, 242);">hasRole('ROLE')</font>` | <font style="color:rgb(15, 17, 21);">是否有指定角色</font> |
| `<font style="color:rgb(15, 17, 21);background-color:rgb(235, 238, 242);">hasAnyRole('ROLE1','ROLE2')</font>` | <font style="color:rgb(15, 17, 21);">是否有任一角色</font> |
| `<font style="color:rgb(15, 17, 21);background-color:rgb(235, 238, 242);">hasAuthority('AUTH')</font>` | <font style="color:rgb(15, 17, 21);">是否有指定权限</font> |
| `<font style="color:rgb(15, 17, 21);background-color:rgb(235, 238, 242);">hasAnyAuthority('AUTH1','AUTH2')</font>` | <font style="color:rgb(15, 17, 21);">是否有任一权限</font> |
| `<font style="color:rgb(15, 17, 21);background-color:rgb(235, 238, 242);">authentication</font>` | <font style="color:rgb(15, 17, 21);">当前认证对象</font> |
| `<font style="color:rgb(15, 17, 21);background-color:rgb(235, 238, 242);">principal</font>` | <font style="color:rgb(15, 17, 21);">当前用户主体</font> |
| `<font style="color:rgb(15, 17, 21);background-color:rgb(235, 238, 242);">#argumentName</font>` | <font style="color:rgb(15, 17, 21);">方法参数</font> |
| `<font style="color:rgb(15, 17, 21);background-color:rgb(235, 238, 242);">@beanName.method()</font>` | <font style="color:rgb(15, 17, 21);">调用Spring Bean方法</font> |
| `<font style="color:rgb(15, 17, 21);background-color:rgb(235, 238, 242);">returnObject</font>` | <font style="color:rgb(15, 17, 21);">返回值（PostAuthorize）</font> |
| `<font style="color:rgb(15, 17, 21);background-color:rgb(235, 238, 242);">permitAll()</font>` | <font style="color:rgb(15, 17, 21);">永远允许</font> |
| `<font style="color:rgb(15, 17, 21);background-color:rgb(235, 238, 242);">denyAll()</font>` | <font style="color:rgb(15, 17, 21);">永远拒绝</font> |
| `<font style="color:rgb(15, 17, 21);background-color:rgb(235, 238, 242);">isAnonymous()</font>` | <font style="color:rgb(15, 17, 21);">是否匿名用户</font> |
| `<font style="color:rgb(15, 17, 21);background-color:rgb(235, 238, 242);">isAuthenticated()</font>` | <font style="color:rgb(15, 17, 21);">是否已认证</font> |
| `<font style="color:rgb(15, 17, 21);background-color:rgb(235, 238, 242);">isRememberMe()</font>` | <font style="color:rgb(15, 17, 21);">是否记住我登录</font> |
| `<font style="color:rgb(15, 17, 21);background-color:rgb(235, 238, 242);">isFullyAuthenticated()</font>` | <font style="color:rgb(15, 17, 21);">是否完整认证（非记住我）</font> |


