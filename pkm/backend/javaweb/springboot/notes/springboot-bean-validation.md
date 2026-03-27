# **Bean Validation**

---

## 什么是 Bean Validation

**Bean Validation**是一个 Java 规范，使用注解的方式对 Java Bean 进行声明式验证，**是 Jakarta EE 的一部分**。通过注解直接在**字段或方法**上声明验证规则，而不是在业务逻辑中写 if-else。**

```java
public class User {
    @NotNull
    @Size(min=2, max=30)
    private String name;
    
    @Email
    private String email;
    
    @Min(18)
    private int age;
}
```

实际开发中，最常见于 Web 层验证用户输入（但实际上它可以使用在三层架构的任何一层）

---

## 基础约束

| **注解** | **说明** | **适用类型** |
| --- | --- | --- |
| `**@NotNull**` | **值不为 null** | **任何类型** |
| `**@NotEmpty**` | **不为 null 且长度/大小>0** | **String、Collection、Map、Array** |
| `**@NotBlank**` | **不为 null 且 trim 后长度>0** | **String** |
| `**@Size(min,max)**` | **长度/大小范围** | **String、Collection、Map、Array** |
| `**@Min(value)**` | **最小值** | **数值类型** |
| `**@Max(value)**` | **最大值** | **数值类型** |
| `**@Email**` | **邮箱格式** | **String** |
| `**@Pattern(regexp)**` | **正则匹配** | **String** |

---

## 特殊约束

| **注解** | **说明** |
| --- | --- |
| `**@Positive**`**/**`**@PositiveOrZero**` | **正数/正数或零（应用在数字上）** |
| `**@Negative**`**/**`**@NegativeOrZero**` | **负数/负数或零（应用在数字上）** |
| `**@Past**`**/**`**@PastOrPresent**` | **过去/过去或现在 【时间】，应用在日期 API 上。** |
| `**@Future**`**/**`**@FutureOrPresent**` | **未来/未来或现在【时间】，应用在日期 API 上。** |
| `**@Digits(integer,fraction)**` | 数字位数限制，integer 设置整数部分的数字个数，fraction 设置小数部分的数字个数。 |

---

## SpringBoot 与 Bean Validation 关系

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1765202022187-c728ee2d-a913-4945-baf9-a8baeb642bfb.png" width="2271.2" title="" crop="0,0,1,1" id="u41fc70fc" class="ne-image">

**Spring Boot 自动集成了 Bean Validation 标准规范（JSR 380）及其参考实现 Hibernate Validator，使开发者能通过**`**@Valid**`**等注解便捷使用验证功能，但 Bean Validation 本身是独立于 Spring 的技术标准。**

---

## **在 SpringBoot 中的使用**

### 第一步：引入启动器

```xml
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-validation</artifactId>
</dependency>
```

### 第二步：编写 DTO

假设从前端系统提交过来的信息包含：

1. 用户名：不能为空，姓名必须是汉字
2. 邮箱地址：不能为空，必须符合邮箱格式
3. 手机号：不能为空，并且必须是手机号

```java
package com.jkweilai.demo.controller.dto;

import jakarta.validation.constraints.Email;
import jakarta.validation.constraints.NotBlank;
import jakarta.validation.constraints.Pattern;
import lombok.Data;

@Data
public class UserCreateDTO {
    // 1. 用户名：不能为空，必须是汉字
    @NotBlank(message = "用户名不能为空")
    @Pattern(regexp = "^[\\u4e00-\\u9fa5]{2,20}$", message = "姓名必须是2-20个汉字")
    private String username;

    // 2. 邮箱地址：不能为空，必须符合邮箱格式
    @NotBlank(message = "邮箱不能为空")
    @Email(message = "邮箱格式不正确")
    private String email;

    // 3. 手机号：不能为空，并且必须是手机号
    @NotBlank(message = "手机号不能为空")
    @Pattern(regexp = "^1[3-9]\\d{9}$", message = "手机号格式不正确")
    private String phone;
}

```

### 第三步：编写 Controller

重点关注 `@Valid`注解：

```java
package com.jkweilai.demo.controller;

import com.jkweilai.demo.controller.dto.UserCreateDTO;
import jakarta.validation.Valid;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class UserController {

    @PostMapping("/createUser")
    public UserCreateDTO createUser(@Valid @RequestBody UserCreateDTO userCreateDTO) {
        // 校验失败不会走到这里
        return userCreateDTO;
    }
}

```

### 第四步：编写全局异常处理

只要校验失败，底层就会自动抛出异常，然后走我们编写的全局异常处理器，给前端系统返回 JSON ：

```java
package com.jkweilai.demo.handler;

import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.MethodArgumentNotValidException;
import org.springframework.web.bind.annotation.ExceptionHandler;
import org.springframework.web.bind.annotation.RestControllerAdvice;

import java.util.HashMap;
import java.util.Map;

@RestControllerAdvice
public class GlobalExceptionHandler {

    @ExceptionHandler(MethodArgumentNotValidException.class)
    public ResponseEntity<Map<String, Object>> handleValidationException(MethodArgumentNotValidException ex) {

        Map<String, Object> errors = new HashMap<>();
        Map<String, String> fieldErrors = new HashMap<>();

        // 提取字段错误信息
        ex.getBindingResult().getFieldErrors().forEach(error -> {
            fieldErrors.put(error.getField(), error.getDefaultMessage());
        });

        errors.put("code", 400);
        errors.put("message", "参数校验失败");
        errors.put("timestamp", System.currentTimeMillis());
        errors.put("errors", fieldErrors);

        return ResponseEntity.badRequest().body(errors);
    }
}

```

### 第五步：测试

使用 Apipost 工具进行测试：

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1765204305570-d7c94609-cf45-4b93-9336-4d38ff74abc4.png" width="436.8" title="" crop="0,0,1,1" id="ufa42825e" class="ne-image">

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1765204332077-3e38db14-5417-4a40-96cb-7c7b981d2d78.png" width="460" title="" crop="0,0,1,1" id="ub98e5584" class="ne-image">

