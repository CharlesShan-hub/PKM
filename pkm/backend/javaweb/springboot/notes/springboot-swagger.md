# Swagger

---

## 认识 Swagger

### 什么是 Swagger

**Swagger能根据你在代码中添加的注解自动生成实时在线的RESTful API文档，并提供可视化的交互界面让你可以直接在浏览器中测试接口调用，实现"代码即文档、文档即测试"的一体化开发体验。**

### **Swagger 与 OpenAPI**

+ **最早在**2010年**，一个叫**Tony Tam**的工程师觉得写API文档和调试太麻烦了，就自己动手做了个叫“Swagger”的小工具。**
+ **工具在**2011年**免费开源后，吸引了好多程序员一起用，一下子就火了起来。**
+ **软件工具公司**SmartBear**看到了Swagger的价值。于是对项目提供了资金和资源支持。**
+ **到了**2015年**，**SmartBear**觉得它潜力巨大，但又觉得个人开发很难做大，于是把**Swagger 的核心设计**捐给了**Linux基金会**，成立了“OpenAPI倡议”。谷歌、微软这些大厂都加入进来，一起维护它。**
+ **2017年**，他们给这个核心设计起了个名字**OpenAPI规范**，而原来的“Swagger”这个名字，则专指实现这份规范的一系列**具体工具**。**
+ **现在**，OpenAPI规范 已经是业界的**通用标准**，而Swagger也被全世界开发者广泛使用，生态非常繁荣。总结一句话：Swagger 是实现 OpenAPI 规范的工具集**

### 不用 Swagger 之前

```plain
🟥 问题1：文档手工维护
程序员写代码 -> 手动写Word文档 -> 之后修改代码后经常忘记同步更新word文档 -> 文档过时

🟥 问题2：前后端沟通成本高
前端："这个接口参数怎么传？"
后端："等我翻下文档...哦，文档还没写，你看代码吧"
前端："看不懂Java..."

🟥 问题3：测试效率低
测试人员需要手动构造请求 -> 容易出错 -> 需要去反复确认
```

### 用 Swagger 之后

```plain
🟢 解决1：代码即文档
程序员编写代码的时候写几个注解 -> 自动实时生成在线API文档 -> 实时同步

🟢 解决2：标准化接口,swagger实现OpenAPI规范，因此API接口是按照标准写的。不是自己搞一套的混乱时代了。
统一参数格式、响应格式、错误码 -> 减少沟通

🟢 解决3：在线测试
直接在浏览器里测试

🟢 解决4：协作高效
前后端都能看同一个文档 -> 减少联调时间50%+
```

### Swagger 工具集中有哪些常见工具

| **工具名称** | **核心功能** | **主要应用场景** |
| --- | --- | --- |
| **Swagger UI** | **将OpenAPI规范文件渲染成可视化、交互式的API文档网页**。** | **前端查看、测试人员调试、交付API文档给合作方。** |
| **Swagger Editor** | **编写OpenAPI规范文件的在线编辑器**。** | **编写 OpenAPI 的 YAML/JSON文件。** |
| **Swagger Codegen** | **根据OpenAPI规范文件，自动生成服务器端骨架代码和客户端调用代码**。** | **前后端分离开发，快速生成客户端SDK，搭建项目基础。** |

### Swagger 和 Apipost 的区别和联系

**Swagger是API设计/文档工具，Apipost是API调试/协作平台，Apipost可导入Swagger文档进行测试和管理。第1步：后端开发**

```java
// 开发时就用Swagger注解
@PostMapping("/users")
@Operation(summary = "创建用户")
@ApiResponse(responseCode = "201", description = "创建成功")
public R<UserDTO> createUser(@Valid @RequestBody UserDTO dto) {
    // 业务逻辑
}
```

**第2步：导出OpenAPI规范**

```plain
访问 Swagger UI的地址：http://localhost:8080/doc.html
访问 http://localhost:8080/v3/api-docs
得到JSON格式的OpenAPI规范
```

**第3步：ApiPost导入**

```plain
1. ApiPost中点击"导入"
2. 选择"OpenAPI/Swagger"
3. 粘贴JSON或上传文件
4. 自动生成完整项目
```

**第4步：各角色使用**

```plain
👨‍💻 前端：
1. 查看接口文档
2. 使用Mock数据开发
3. 不需等后端

🧪 测试：
1. 生成测试用例
2. 自动化测试
3. 性能测试

👨‍💼 产品：
1. 验证业务流程
2. 检查参数是否合理
```

---

## 认识 Knife4j

**Knife4j 是一个让你在Spring Boot项目中能获得“更好看、更好用、更安全”的API文档的工具，它是Swagger的全面增强版，是国内Java后端开发者的主流选择。Knife4j 是 100% 由国人（中国开发者）开发并维护的优秀开源项目。**

+ **创始人**：**肖雪（GitHub: xiaoymin）**。项目最初名为**`**Swagger-Bootstrap-UI**`**，后升级为**`**Knife4j**`**。**
+ **诞生原因**：正是因为在项目中使用原生的 Swagger UI 时，遇到了**界面不够友好、功能不满足国内团队需求、对Spring Boot集成不够便捷**等实际痛点，开发者才决定自己动手做一个更好的工具。**
+ **项目理念**：在完全遵循 OpenAPI 规范的基础上，做**深度增强和易用性改造**，而非另起炉灶。**

---

## **SpringBoot 项目中使用 Knife4j**

### 创建SpringBoot项目

使用Spring Initializr创建项目（**重点注意事项：SpringBoot 选择**3.3.6 版本才能兼容**Knife4j**），选择以下依赖：

+ Spring Web
+ Lombok

### 添加依赖

在`pom.xml`中添加以下依赖：

```xml
<!-- Knife4j OpenAPI3 -->
<dependency>
    <groupId>com.github.xiaoymin</groupId>
    <artifactId>knife4j-openapi3-jakarta-spring-boot-starter</artifactId>
    <version>4.5.0</version>
</dependency>

<!-- Validation -->
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-validation</artifactId>
</dependency>
```

### 编写 Knife4j配置

在 application.yml 中提供配置：

**配置Spring Boot 3的路径匹配策略，并设置Knife4j生成标题为"用户信息管理接口文档"、扫描指定控制器包的API文档。**

```yaml
spring:
  mvc:
    pathmatch:
      matching-strategy: ant_path_matcher  # Spring Boot 3集成swagger必须的配置
knife4j:
  enable: true
  openapi:
    title: 用户信息管理接口文档
    description: 用户信息管理接口文档
    contact:
      name: 老杜
      email: dujubin@126.com
      url: http://localhost:8080
    version: 1.0.0
  group:
    default:
      group-name: default
      api-rule: package
      api-rule-resources:
        - com.jkweilai.demo.controller
```

### 创建实体类

```java
package com.jkweilai.demo.entity;

import com.fasterxml.jackson.annotation.JsonFormat;
import io.swagger.v3.oas.annotations.media.Schema;
import jakarta.validation.constraints.Email;
import jakarta.validation.constraints.NotBlank;
import jakarta.validation.constraints.NotNull;
import jakarta.validation.constraints.Pattern;
import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

import java.time.LocalDateTime;

@Data
@NoArgsConstructor
@AllArgsConstructor
/*
为整个实体类添加描述信息
在Swagger文档中会显示"用户实体"作为这个模型的描述
在API文档的"实体类列表"或"模型"部分会显示这个描述
 */
@Schema(description = "用户实体")
public class User {

    @Schema(description = "用户ID", example = "1")
    private Long id;

    @NotBlank(message = "用户名不能为空")
    /*
    description: 字段的描述信息
        会在API文档中显示字段的说明
        方便前端开发者理解字段含义
    example: 示例值
        在API文档中提供示例数据
        测试时会自动填充这个值
        有助于理解字段的格式和类型
    required: 是否必需
        required = true 表示该字段在请求中必须提供
        在文档中会标注为必填字段
        注意: 这只是文档层面的标注，实际校验需要配合 @NotNull、@NotBlank 等注解
     */
    @Schema(description = "用户名", example = "张三", required = true)
    private String username;

    @NotBlank(message = "密码不能为空")
    @Pattern(regexp = "^(?=.*[A-Za-z])(?=.*\\d)[A-Za-z\\d]{6,}$",
            message = "密码必须包含字母和数字，且长度至少6位")
    @Schema(description = "密码", example = "123456a", required = true)
    private String password;

    @NotBlank(message = "邮箱不能为空")
    @Email(message = "邮箱格式不正确")
    @Schema(description = "邮箱", example = "zhangsan@example.com", required = true)
    private String email;

    @NotNull(message = "年龄不能为空")
    @Schema(description = "年龄", example = "25", required = true)
    private Integer age;

    @NotBlank(message = "手机号不能为空")
    @Pattern(regexp = "^1[3-9]\\d{9}$", message = "手机号格式不正确")
    @Schema(description = "手机号", example = "13800138000", required = true)
    private String phone;

    @Schema(description = "创建时间", example = "2024-01-01 10:00:00")
    /*
        这个注解和swagger无关，属于jackson库中的注解。作用是指定日期对象在序列化和发序列化时的日期格式。
        不指定@JsonFormat时，LocalDateTime会默认序列化为包含"T"的ISO-8601格式（如"2024-01-01T10:00:00"）
     */
    @JsonFormat(pattern = "yyyy-MM-dd HH:mm:ss")
    private LocalDateTime createTime;

    @Schema(description = "更新时间", example = "2024-01-01 10:00:00")
    @JsonFormat(pattern = "yyyy-MM-dd HH:mm:ss")
    private LocalDateTime updateTime;
}
```

### 创建响应封装类

```java
package com.jkweilai.demo.common;

import io.swagger.v3.oas.annotations.media.Schema;
import lombok.Data;

@Data
@Schema(description = "统一响应结果")
public class Result<T> {

    @Schema(description = "状态码", example = "200")
    private Integer code;

    @Schema(description = "提示信息", example = "操作成功")
    private String message;

    @Schema(description = "响应数据")
    private T data;

    @Schema(description = "时间戳", example = "1704067200000")
    private Long timestamp;

    // 成功响应
    public static <T> Result<T> success(T data) {
        Result<T> result = new Result<>();
        result.setCode(200);
        result.setMessage("操作成功");
        result.setData(data);
        result.setTimestamp(System.currentTimeMillis());
        return result;
    }

    public static <T> Result<T> success(T data, String message) {
        Result<T> result = success(data);
        result.setMessage(message);
        return result;
    }

    // 失败响应
    public static <T> Result<T> error(String message) {
        Result<T> result = new Result<>();
        result.setCode(500);
        result.setMessage(message);
        result.setTimestamp(System.currentTimeMillis());
        return result;
    }

    public static <T> Result<T> error(Integer code, String message) {
        Result<T> result = new Result<>();
        result.setCode(code);
        result.setMessage(message);
        result.setTimestamp(System.currentTimeMillis());
        return result;
    }

    // 无数据成功
    public static <T> Result<T> success() {
        return success(null);
    }
}
```

### 创建Service层接口

```java
package com.jkweilai.demo.service;

import com.jkweilai.demo.entity.User;

import java.util.List;

public interface UserService {

    /**
     * 添加用户
     */
    User addUser(User user);

    /**
     * 更新用户
     */
    User updateUser(User user);

    /**
     * 删除用户
     */
    boolean deleteUser(Long id);

    /**
     * 根据ID查询用户
     */
    User getUserById(Long id);

    /**
     * 查询所有用户
     */
    List<User> getAllUsers();

    /**
     * 根据用户名查询用户
     */
    List<User> getUsersByUsername(String username);
}
```

### Service 实现类

```java
package com.jkweilai.demo.service.impl;

import com.jkweilai.demo.entity.User;
import com.jkweilai.demo.service.UserService;
import org.springframework.stereotype.Service;

import java.time.LocalDateTime;
import java.util.ArrayList;
import java.util.List;
import java.util.concurrent.ConcurrentHashMap;
import java.util.concurrent.atomic.AtomicLong;

@Service
public class UserServiceImpl implements UserService {

    // 使用ConcurrentHashMap模拟数据存储
    private ConcurrentHashMap<Long, User> userMap = new ConcurrentHashMap<>();

    // 使用AtomicLong生成ID
    // 自动维护一个线程安全的自增id。
    private AtomicLong idGenerator = new AtomicLong(1);

    // 初始化一些测试数据
    public UserServiceImpl() {
        LocalDateTime now = LocalDateTime.now();

        for (int i = 1; i <= 5; i++) {
            Long id = (long) i;
            User user = new User();
            user.setId(id);
            user.setUsername("用户" + i);
            user.setPassword("123456");
            user.setEmail("user" + i + "@jk.com");
            user.setAge(20 + i);
            user.setPhone("1380013800" + i);
            user.setCreateTime(now.minusDays(i));
            user.setUpdateTime(now.minusDays(i));

            userMap.put(id, user);
            idGenerator.set(i + 1);
        }
    }

    @Override
    public User addUser(User user) {
        // 生成ID
        Long id = idGenerator.getAndIncrement();
        user.setId(id);

        // 设置创建时间和更新时间
        LocalDateTime now = LocalDateTime.now();
        user.setCreateTime(now);
        user.setUpdateTime(now);

        // 保存用户
        userMap.put(id, user);

        return user;
    }

    @Override
    public User updateUser(User user) {
        Long id = user.getId();
        if (id == null || !userMap.containsKey(id)) {
            throw new RuntimeException("用户不存在");
        }

        // 获取原用户数据
        User existingUser = userMap.get(id);

        // 更新字段（在实际项目中，这里需要逐个字段判断是否更新）
        if (user.getUsername() != null) {
            existingUser.setUsername(user.getUsername());
        }
        if (user.getPassword() != null) {
            existingUser.setPassword(user.getPassword());
        }
        if (user.getEmail() != null) {
            existingUser.setEmail(user.getEmail());
        }
        if (user.getAge() != null) {
            existingUser.setAge(user.getAge());
        }
        if (user.getPhone() != null) {
            existingUser.setPhone(user.getPhone());
        }

        // 更新时间
        existingUser.setUpdateTime(LocalDateTime.now());

        // 保存更新
        userMap.put(id, existingUser);

        return existingUser;
    }

    @Override
    public boolean deleteUser(Long id) {
        if (!userMap.containsKey(id)) {
            return false;
        }

        userMap.remove(id);
        return true;
    }

    @Override
    public User getUserById(Long id) {
        return userMap.get(id);
    }

    @Override
    public List<User> getAllUsers() {
        return new ArrayList<>(userMap.values());
    }

    @Override
    public List<User> getUsersByUsername(String username) {
        List<User> result = new ArrayList<>();
        for (User user : userMap.values()) {
            if (user.getUsername().contains(username)) {
                result.add(user);
            }
        }
        return result;
    }
}
```

### 创建Controller层

```java
package com.jkweilai.demo.controller;

import com.jkweilai.demo.common.Result;
import com.jkweilai.demo.entity.User;
import com.jkweilai.demo.service.UserService;
import io.swagger.v3.oas.annotations.Operation;
import io.swagger.v3.oas.annotations.Parameter;
import io.swagger.v3.oas.annotations.tags.Tag;
import jakarta.validation.Valid;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/users")
// @Tag 注解会在 API 文档的顶部导航栏显示为标签页/分组标签
@Tag(name = "用户管理", description = "用户相关的CRUD操作")
public class UserController {

    @Autowired
    private UserService userService;

    @PostMapping
    // 为API接口添加详细的描述信息，包括接口摘要和详细说明
    @Operation(summary = "创建用户", description = "添加一个新用户")
    public Result<User> createUser(
            // 描述API接口中的单个参数，包括参数说明、是否必需、示例值等信息
            @Parameter(description = "用户信息", required = true)
            @Valid @RequestBody User user) {
        User savedUser = userService.addUser(user);
        return Result.success(savedUser, "创建成功");
    }

    @PutMapping
    @Operation(summary = "更新用户", description = "更新用户信息")
    public Result<User> updateUser(
            @Parameter(description = "用户信息", required = true)
            @Valid @RequestBody User user) {
        User updatedUser = userService.updateUser(user);
        return Result.success(updatedUser, "更新成功");
    }

    @DeleteMapping("/{id}")
    @Operation(summary = "删除用户", description = "根据ID删除用户")
    public Result<Void> deleteUser(
            @Parameter(description = "用户ID", required = true, example = "1")
            @PathVariable Long id) {
        boolean success = userService.deleteUser(id);
        if (success) {
            return Result.success(null, "删除成功");
        } else {
            return Result.error("用户不存在");
        }
    }

    @GetMapping("/{id}")
    @Operation(summary = "获取用户详情", description = "根据ID查询用户")
    public Result<User> getUserById(
            @Parameter(description = "用户ID", required = true, example = "1")
            @PathVariable Long id) {
        User user = userService.getUserById(id);
        if (user != null) {
            return Result.success(user);
        } else {
            return Result.error(404, "用户不存在");
        }
    }

    @GetMapping
    @Operation(summary = "获取所有用户", description = "查询所有用户列表")
    public Result<List<User>> getAllUsers() {
        List<User> users = userService.getAllUsers();
        return Result.success(users);
    }

    @GetMapping("/search")
    @Operation(summary = "搜索用户", description = "根据用户名搜索用户")
    public Result<List<User>> searchUsers(
            @Parameter(description = "用户名关键字", required = true, example = "张三")
            @RequestParam String username) {
        List<User> users = userService.getUsersByUsername(username);
        return Result.success(users);
    }
}
```

### 创建全局异常处理器

```java
package com.jkweilai.demo.handler;

import com.jkweilai.demo.common.Result;
import jakarta.validation.ConstraintViolation;
import jakarta.validation.ConstraintViolationException;
import org.springframework.validation.BindException;
import org.springframework.validation.FieldError;
import org.springframework.web.bind.MethodArgumentNotValidException;
import org.springframework.web.bind.annotation.ExceptionHandler;
import org.springframework.web.bind.annotation.RestControllerAdvice;

import java.util.ArrayList;
import java.util.List;
import java.util.Set;

@RestControllerAdvice
public class GlobalExceptionHandler {

    /**
     * 处理 @RequestBody 参数校验异常
     *
     * @PostMapping public Result<User> createUser(
     * @Valid @RequestBody User user  // 这个注解触发的异常
     * )
     */
    @ExceptionHandler(MethodArgumentNotValidException.class)
    public Result<Void> handleMethodArgumentNotValidException(MethodArgumentNotValidException e) {
        // 获取所有字段校验错误列表
        List<FieldError> fieldErrors = e.getBindingResult().getFieldErrors();
        // 创建列表用于存储所有错误提示信息
        List<String> errorMessages = new ArrayList<>();
        // 遍历每个字段校验错误
        for (FieldError fieldError : fieldErrors) {
            // 获取校验注解中定义的错误提示信息
            // 例如：@NotBlank(message="用户名不能为空") → "用户名不能为空"
            errorMessages.add(fieldError.getDefaultMessage());
        }
        String message = String.join("; ", errorMessages);
        return Result.error(400, message);
    }

    /**
     * 处理普通表单参数绑定异常
     *
     * @PostMapping("/form") public Result<User> createUserByForm(
     * @Valid User user  // 没有 @RequestBody
     * )
     */
    @ExceptionHandler(BindException.class)
    public Result<Void> handleBindException(BindException e) {
        // 获取所有字段校验错误列表
        List<FieldError> fieldErrors = e.getBindingResult().getFieldErrors();
        // 创建列表存储所有错误信息
        List<String> errorMessages = new ArrayList<>();
        // 遍历每个字段错误，提取错误提示信息
        for (FieldError fieldError : fieldErrors) {
            String errorMessage = fieldError.getDefaultMessage();
            errorMessages.add(errorMessage);
        }
        String message = String.join("; ", errorMessages);
        return Result.error(400, message);
    }

    /**
     * 处理 @RequestParam/@PathVariable 参数校验异常
     *
     * @GetMapping("/{id}") public Result<User> getUser(
     * @PathVariable @Min(1) Long id,  // 这个注解触发的异常
     * @RequestParam @NotBlank String name  // 这个注解触发的异常
     * )
     */
    @ExceptionHandler(ConstraintViolationException.class)
    public Result<Void> handleConstraintViolationException(ConstraintViolationException e) {
        // 获取所有校验失败的约束违规信息集合
        Set<ConstraintViolation<?>> violations = e.getConstraintViolations();
        // 创建列表用于存储所有错误信息
        List<String> errorMessages = new ArrayList<>();
        // 遍历每个违规信息，提取错误提示
        for (ConstraintViolation<?> violation : violations) {
            // 获取校验注解中的message信息，如"用户名不能为空"
            errorMessages.add(violation.getMessage());
        }
        // 将所有错误信息用分号连接成一个字符串
        String message = String.join("; ", errorMessages);
        // 返回400状态码和错误信息
        return Result.error(400, message);
    }

    /**
     * 处理运行时异常
     */
    @ExceptionHandler(RuntimeException.class)
    public Result<Void> handleRuntimeException(RuntimeException e) {
        return Result.error(e.getMessage());
    }

    /**
     * 处理其他异常
     */
    @ExceptionHandler(Exception.class)
    public Result<Void> handleException(Exception e) {
        return Result.error("系统异常: " + e.getMessage());
    }
}
```

### 创建主启动类

```java
package com.jkweilai.demo;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class MyApplication {

    public static void main(String[] args) {
        SpringApplication.run(MyApplication.class, args);
        System.out.println("应用启动成功！");
        System.out.println("API文档地址：http://localhost:8080/doc.html");
        System.out.println("OpenAPI文档地址：http://localhost:8080/v3/api-docs");
    }
}
```

---

## 将 OpenAPI 导入 Apipost

**第一步：新建并导入项目**

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1765324954473-07089f27-0d74-4db5-a780-25aaea32266e.png" width="483.2" title="" crop="0,0,1,1" id="u2d9368dd" class="ne-image">

**第二步：填写 OpenAPI 地址：**[**http://localhost:8080/v3/api-docs**](http://localhost:8080/v3/api-docs)

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1765325002844-8e3f9967-6efc-4f1f-81ad-dfa0aa48fdb6.png" width="622.4" title="" crop="0,0,1,1" id="u8e05bd04" class="ne-image">

**第三步：设置 Apipost 基础 URL**

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1765325058771-ad0e5500-93ff-4b00-9070-88918f8a88a7.png" width="311.2" title="" crop="0,0,1,1" id="ueaef0068" class="ne-image">

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1765325087214-d58b4f60-56a8-4716-9daf-3e16c0077156.png" width="1062.4" title="" crop="0,0,1,1" id="udb5831b0" class="ne-image">

然后就可以在 Apipost 中进行接口的测试工作了。
