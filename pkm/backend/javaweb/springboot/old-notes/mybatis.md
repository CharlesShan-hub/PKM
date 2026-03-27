# 整合 MyBatis

我们把👉[[../../mybatis/notes/introduction|introduction]]，升级成注解开发版本

---
## 资源

* https://www.bilibili.com/video/BV14z4y1N7pg/?p=7

---
## 数据准备
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

本案例演示的是 springboot+mybatis。首先是 maven 的 `pom.xml`，加入 mysql 和 mybatis 的依赖，注意要加入`org.mybatis.spring.boot`！
```xml
<dependency>
    <groupId>mysql</groupId>
    <artifactId>mysql-connector-java</artifactId>
    <version>8.0.30</version>
</dependency>

<dependency>
    <groupId>org.mybatis.spring.boot</groupId>
    <artifactId>mybatis-spring-boot-starter</artifactId>
    <version>3.0.3</version>
</dependency>
```

我们的 springboot 项目，直接在`application.yaml`配置就可以了，更简单。
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
	configuration:
		map-underscore-to-camel-case: true # 开启驼峰映射，比如create_time对应到createTime
```

### 具体代码

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

Mapper，用来连接 mybatis：`UserMapper.java`。这次使用注解进行sql语句配置。
```Java
package com.charlesshan.helloworld.mapper;

import com.charlesshan.helloworld.entity.User;
import org.apache.ibatis.annotations.Mapper;
import org.apache.ibatis.annotations.Select;

import java.util.List;

@Mapper
public interface UserMapper {
    @Select("select * from user")
    List<User> selectAllUsers();
}
```

Service 接口：`UserService.java`
```Java
package com.charlesshan.helloworld.service;

import com.charlesshan.helloworld.entity.User;

import java.util.List;

public interface UserService {
    public List<User> findAll();
}
```

Service 的 impl：`UserServiceImpl.java`
```Java
package com.charlesshan.helloworld.service.impl;

import com.charlesshan.helloworld.entity.User;
import com.charlesshan.helloworld.mapper.UserMapper;
import com.charlesshan.helloworld.service.UserService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class UserServiceImpl implements UserService {
    @Autowired
    private UserMapper userMapper;
    @Override
    public List<User> findAll() {
        return userMapper.selectAllUsers();
    }
}
```

Controller：`HelloController.java`
```Java
package com.charlesshan.helloworld.controller;

import com.charlesshan.helloworld.entity.User;
import com.charlesshan.helloworld.service.UserService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;

@RestController
public class HelloController {
    @Autowired
    private UserService userService;

    @RequestMapping("/findAll")
    public List<User> findeAll() {
        return userService.findAll();
    }
}
```

访问http://localhost:8080/findAll，就可以得到
```json
[{"id":1,"name":"张三","age":25,"email":"zhangsan@example.com","createTime":"2025-07-01T11:51:18.000+00:00","updateTime":"2025-07-01T11:51:18.000+00:00"},{"id":2,"name":"李四","age":30,"email":"lisi@example.com","createTime":"2025-07-01T11:51:18.000+00:00","updateTime":"2025-07-01T11:51:18.000+00:00"},{"id":3,"name":"王五","age":28,"email":"wangwu@example.com","createTime":"2025-07-01T11:51:18.000+00:00","updateTime":"2025-07-01T11:51:18.000+00:00"},{"id":4,"name":"赵六","age":35,"email":"zhaoliu@example.com","createTime":"2025-07-01T11:51:18.000+00:00","updateTime":"2025-07-01T11:51:18.000+00:00"},{"id":5,"name":"钱七","age":22,"email":"qianqi@example.com","createTime":"2025-07-01T11:51:18.000+00:00","updateTime":"2025-07-01T11:51:18.000+00:00"}]