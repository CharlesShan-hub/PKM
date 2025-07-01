# Mybatis Introduction
## 资料

* 黑马mybatis教程: https://www.bilibili.com/video/BV1MT4y1k7wZ
* 官网: https://mybatis.org/mybatis-3/zh_CN/index.html
* MyBatis 是一个 ​**​Java 持久层框架​**​，它通过 XML 或注解将 SQL 与 Java 对象映射，避免了传统 JDBC 的复杂代码。

---
## 快速入门

### 数据准备
```sql
-- =============================================
-- 创建数据库和用户表（MyBatis 快速入门示例）
-- 数据库名: mybatis_demo
-- 表名: user
-- =============================================

-- 1. 删除旧数据库（如果存在）
DROP DATABASE IF EXISTS mybatis_demo;

-- 2. 创建数据库（使用utf8mb4字符集）
CREATE DATABASE mybatis_demo 
DEFAULT CHARACTER SET utf8mb4 
COLLATE utf8mb4_unicode_ci;

-- 3. 使用数据库
USE mybatis_demo;

-- 4. 创建用户表
CREATE TABLE IF NOT EXISTS `user` (
  `id` INT NOT NULL AUTO_INCREMENT COMMENT '主键ID',
  `name` VARCHAR(50) NOT NULL COMMENT '用户名',
  `age` INT DEFAULT NULL COMMENT '年龄',
  `email` VARCHAR(100) DEFAULT NULL COMMENT '邮箱',
  `create_time` DATETIME DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `update_time` DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间',
  PRIMARY KEY (`id`),
  INDEX `idx_name` (`name`) COMMENT '用户名索引'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='用户表';

-- 5. 插入测试数据
INSERT INTO `user` (`name`, `age`, `email`) VALUES
('张三', 25, 'zhangsan@example.com'),
('李四', 30, 'lisi@example.com'),
('王五', 28, 'wangwu@example.com'),
('赵六', 35, 'zhaoliu@example.com'),
('钱七', 22, 'qianqi@example.com');

-- 6. 验证数据
SELECT '=== 用户表数据 ===' AS '';
SELECT * FROM `user`;

-- 7. 显示表结构
SELECT '=== 表结构 ===' AS '';
DESCRIBE `user`;
```

假设上边的文件保存成`init.sql`
那么首先进入 mysql 命令行模式，然后运行source命令
```shell
mysql> source /home/charles/project/test/mybatis_demo/init.sql
```

### 依赖配置

本案例演示的是 springboot+mybatis。首先是 maven 的 pom.xml，加入 mysql 和 mybatis 的依赖，注意要加入`org.mybatis.spring.boot`！
```xml
<dependency>
    <groupId>mysql</groupId>
    <artifactId>mysql-connector-java</artifactId>
    <version>8.0.30</version>
</dependency>

<dependency>
    <groupId>org.mybatis</groupId>
    <artifactId>mybatis</artifactId>
    <version>3.5.17</version>
</dependency>

<dependency>
    <groupId>org.mybatis.spring.boot</groupId>
    <artifactId>mybatis-spring-boot-starter</artifactId>
    <version>3.0.3</version>
</dependency>
```

然后要创建 mybatis 自己的配置文件`mybatis-config.xml`，但是我们是 springboot 项目，所以换一个方式，直接在`application.yaml`配置就可以了。
```YAML
server:
  port: 8080

spring:
  datasource:
    url: jdbc:mysql://localhost:3306/mybatis_demo
    username: root
    password: 123456
    driver-class-name: com.mysql.cj.jdbc.Driver

mybatis:
  mapper-locations: classpath:mapper/*.xml
  configuration:
    map-underscore-to-camel-case: true
```

对应的还要每一个 mapper 写一个xml
```XML
<?xml version="1.0" encoding="UTF-8" ?>
<!DOCTYPE mapper
        PUBLIC "-//mybatis.org//DTD Mapper 3.0//EN"
        "https://mybatis.org/dtd/mybatis-3-mapper.dtd">
<mapper namespace="com.charlesshan.helloworld.mapper.UserMapper">
    <select id="selectAllUsers" resultType="com.charlesshan.helloworld.entity.User">
        select * from user;
    </select>
</mapper>
```

### 具体代码

Contorller：`HelloController.java`
```Java
package com.charlesshan.helloworld.controller;

import com.charlesshan.helloworld.entity.User;
import com.charlesshan.helloworld.mapper.UserMapper;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;

@RestController
public class HelloController {
    private final UserMapper userMapper;
    public HelloController(UserMapper userMapper) {
        this.userMapper = userMapper;
    }

    @GetMapping("/users")
    public List<User> selectAllUsers() {
        return userMapper.selectAllUsers();
    }
}
```

实体类：`User.java`
```Java
package com.charlesshan.helloworld.entity;

import java.util.Date;
import lombok.Data;

@Data
public class User {
    private Integer id;
    private String name;
    private Integer age;
    private String email;
    private Date createTime;
    private Date updateTime;
}
```

Mapper，用来连接 mybatis：`UserMapper.java`
```Java
package com.charlesshan.helloworld.mapper;

import com.charlesshan.helloworld.entity.User;
import org.apache.ibatis.annotations.Mapper;

import java.util.List;

@Mapper
public interface UserMapper {
    List<User> selectAllUsers();
}
```

最后注意入口程序，需要用 MapperScan 指定 Mapper
```Java
package com.charlesshan.helloworld;

import org.mybatis.spring.annotation.MapperScan;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
@MapperScan("com.charlesshan.helloworld.mapper")
public class HelloWorldApplication {
    public static void main(String[] args) {
        SpringApplication.run(HelloWorldApplication.class, args);
    }
}
```

访问http://localhost:8080/users，就可以得到
```json
[{"id":1,"name":"张三","age":25,"email":"zhangsan@example.com","createTime":"2025-07-01T11:51:18.000+00:00","updateTime":"2025-07-01T11:51:18.000+00:00"},{"id":2,"name":"李四","age":30,"email":"lisi@example.com","createTime":"2025-07-01T11:51:18.000+00:00","updateTime":"2025-07-01T11:51:18.000+00:00"},{"id":3,"name":"王五","age":28,"email":"wangwu@example.com","createTime":"2025-07-01T11:51:18.000+00:00","updateTime":"2025-07-01T11:51:18.000+00:00"},{"id":4,"name":"赵六","age":35,"email":"zhaoliu@example.com","createTime":"2025-07-01T11:51:18.000+00:00","updateTime":"2025-07-01T11:51:18.000+00:00"},{"id":5,"name":"钱七","age":22,"email":"qianqi@example.com","createTime":"2025-07-01T11:51:18.000+00:00","updateTime":"2025-07-01T11:51:18.000+00:00"}]
```
