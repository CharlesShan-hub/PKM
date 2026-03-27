# SSM 整合-全注解式开发

在我们上面 SpringMVC 全注解开发的基础之上添加 Spring+MyBatis 的配置就行了。

我们在前面学习 Spring 的时候，已经实现了 Spring+MyBatis 的全注解方式开发，我们将当时的配置拿过来就行了。

---

## 第一步：引入 SSM 依赖

```xml

<dependencies>
    <!--springmvc依赖-->
    <dependency>
        <groupId>org.springframework</groupId>
        <artifactId>spring-webmvc</artifactId>
        <version>6.2.13</version>
    </dependency>
    <!--servlet依赖-->
    <dependency>
        <groupId>jakarta.servlet</groupId>
        <artifactId>jakarta.servlet-api</artifactId>
        <version>6.0.0</version>
        <scope>provided</scope>
    </dependency>
    <!--lombok：可选-->
    <dependency>
        <groupId>org.projectlombok</groupId>
        <artifactId>lombok</artifactId>
        <version>1.18.42</version>
        <scope>compile</scope>
    </dependency>
    <!--thymeleaf与spring整合依赖-->
    <dependency>
        <groupId>org.thymeleaf</groupId>
        <artifactId>thymeleaf-spring6</artifactId>
        <version>3.1.3.RELEASE</version>
    </dependency>
    <!--spring context-->
    <dependency>
        <groupId>org.springframework</groupId>
        <artifactId>spring-context</artifactId>
        <version>6.2.13</version>
    </dependency>
    <!--AspectJ依赖-->
    <dependency>
        <groupId>org.springframework</groupId>
        <artifactId>spring-aspects</artifactId>
        <version>6.2.13</version>
    </dependency>
    <!--spring jdbc-->
    <dependency>
        <groupId>org.springframework</groupId>
        <artifactId>spring-jdbc</artifactId>
        <version>6.2.13</version>
    </dependency>
    <!--mysql驱动-->
    <dependency>
        <groupId>com.mysql</groupId>
        <artifactId>mysql-connector-j</artifactId>
        <version>8.4.0</version>
    </dependency>
    <!--mybatis依赖-->
    <dependency>
        <groupId>org.mybatis</groupId>
        <artifactId>mybatis</artifactId>
        <version>3.5.16</version>
    </dependency>
    <!--mybatis和spring集成的依赖-->
    <dependency>
        <groupId>org.mybatis</groupId>
        <artifactId>mybatis-spring</artifactId>
        <version>3.0.4</version>
    </dependency>
    <!--HikariCP连接池的依赖-->
    <dependency>
        <groupId>com.zaxxer</groupId>
        <artifactId>HikariCP</artifactId>
        <version>7.0.2</version>
    </dependency>
    <!--junit的依赖-->
    <dependency>
        <groupId>org.junit.jupiter</groupId>
        <artifactId>junit-jupiter-api</artifactId>
        <version>5.11.0</version>
        <scope>test</scope>
    </dependency>
    <dependency>
        <groupId>org.springframework</groupId>
        <artifactId>spring-test</artifactId>
        <version>6.2.13</version>
        <scope>test</scope>
    </dependency>
</dependencies>

```

---

## 第二步：编写 mybatis-config.xml 文件

在类的根路径下创建该配置文件：`mybatis-config.xml`

```xml

<?xml version="1.0" encoding="UTF-8" ?>
<!DOCTYPE configuration
        PUBLIC "-//mybatis.org//DTD Config 3.0//EN"
        "http://mybatis.org/dtd/mybatis-3-config.dtd">
<configuration>
    <settings>
        <setting name="logImpl" value="STDOUT_LOGGING"/>
    </settings>
</configuration>

```

---

## 第三步：编写 application.properties 文件

在类的根路径下创建该属性配置文件：`application.properties`

```properties

spring.datasource.driver=com.mysql.cj.jdbc.Driver
spring.datasource.url=jdbc:mysql://localhost:3306/ssm
spring.datasource.user=root
spring.datasource.password=123456
mybatis.config.location=mybatis-config.xml
mybatis.type.aliases.package=com.jkweilai.ssm.entity

```

---

## 第四步：编写 Spring 和 MyBatis 的配置

我们之前编写 SpringMVC 全注解式开发的时候，写过一个 `SpringConfig`配置类，将以下代码拷贝进去即可。

```java

package com.jkweilai.ssm.config;

import com.zaxxer.hikari.HikariDataSource;
import org.mybatis.spring.SqlSessionFactoryBean;
import org.mybatis.spring.annotation.MapperScan;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.context.annotation.*;
import org.springframework.core.io.ClassPathResource;
import org.springframework.core.io.Resource;
import org.springframework.jdbc.datasource.DataSourceTransactionManager;
import org.springframework.transaction.annotation.EnableTransactionManagement;

import javax.sql.DataSource;

@Configuration
@ComponentScan("com.jkweilai.ssm")
@PropertySource("classpath:application.properties")
@EnableTransactionManagement
@EnableAspectJAutoProxy
@MapperScan("com.jkweilai.ssm.mapper")
public class SpringConfig {

    @Bean
    public DataSource dataSource(
            @Value("${spring.datasource.driver}")
            String driver,
            @Value("${spring.datasource.url}")
            String url,
            @Value("${spring.datasource.user}")
            String user,
            @Value("${spring.datasource.password}")
            String password) {
        HikariDataSource dataSource = new HikariDataSource();
        dataSource.setDriverClassName(driver);
        dataSource.setJdbcUrl(url);
        dataSource.setUsername(user);
        dataSource.setPassword(password);
        return dataSource;
    }

    @Bean
    public SqlSessionFactoryBean sqlSessionFactoryBean(
            DataSource dataSource,
            @Value("${mybatis.config.location}")
            String mybatisConfigLocation,
            @Value("${mybatis.type.aliases.package}")
            String typeAliasesPackage) {
        SqlSessionFactoryBean sqlSessionFactoryBean = new SqlSessionFactoryBean();
        Resource resource = new ClassPathResource(mybatisConfigLocation);
        sqlSessionFactoryBean.setConfigLocation(resource);
        sqlSessionFactoryBean.setDataSource(dataSource);
        sqlSessionFactoryBean.setTypeAliasesPackage(typeAliasesPackage);
        return sqlSessionFactoryBean;
    }

    @Bean
    public DataSourceTransactionManager transactionManager(DataSource dataSource) {
        DataSourceTransactionManager dataSourceTransactionManager = new DataSourceTransactionManager();
        dataSourceTransactionManager.setDataSource(dataSource);
        return dataSourceTransactionManager;
    }

}

```

---

## 第五步：编写测试程序

1. **准备数据库表**

创建数据库 ssm，并且在该数据库中创建表 t_user

```sql

drop table if exists t_user;
create table t_user(
  id int primary key auto_increment,
  username varchar(255),
  password varchar(255)
);

```

2. **编写实体类**

```java

package com.jkweilai.ssm.entity;

import lombok.Data;

@Data
public class User {
    private Integer id;
    private String username;
    private String password;
}

```

3. **编写 SqlMapper.xml 文件**

在 `resources`目录下创建目录：`com/jkweilai/ssm/mapper`，并创建 `UserMapper.xml`配置文件：

```xml

<?xml version="1.0" encoding="UTF-8" ?>
<!DOCTYPE mapper
        PUBLIC "-//mybatis.org//DTD Mapper 3.0//EN"
        "http://mybatis.org/dtd/mybatis-3-mapper.dtd">
<mapper namespace="com.jkweilai.ssm.mapper.UserMapper">
    <insert id="insert">
        insert into t_user(username,password) values(#{username}, #{password})
    </insert>
</mapper>

```

4. **编写 Mapper 接口**

```java

package com.jkweilai.ssm.mapper;

import com.jkweilai.ssm.entity.User;

public interface UserMapper {
    int insert(User user);
}

```

5. **编写 service 接口和实现**

```java

package com.jkweilai.ssm.service;

import com.jkweilai.ssm.entity.User;

public interface UserService {
    int save(User user);
}

```

```java

package com.jkweilai.ssm.service.impl;

import com.jkweilai.ssm.entity.User;
import com.jkweilai.ssm.mapper.UserMapper;
import com.jkweilai.ssm.service.UserService;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

@Service
@RequiredArgsConstructor
public class UserServiceImpl implements UserService {

    private final UserMapper userMapper;

    @Override
    @Transactional // 添加事务控制
    public int save(User user) {
        return userMapper.insert(user);
    }
}

```

6. **编写 controller**

```java

package com.jkweilai.ssm.controller;

import com.jkweilai.ssm.entity.User;
import com.jkweilai.ssm.service.UserService;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.PostMapping;

@Controller
@RequiredArgsConstructor
public class UserController {
    
    private final UserService userService;
    
    @PostMapping("/save")
    public String save(User user){
        userService.save(user);
        return "success";
    }
}

```

7. **编写页面**

```html

<!DOCTYPE html>
<html lang="en" xmlns:th="http://www.thymeleaf.org">
<head>
    <meta charset="UTF-8">
    <title>index page</title>
</head>
<body>
<h1>SSM整合（全注解开发）</h1>
<form th:action="@{/save}" method="post">
    用户名：<input type="text" name="username">
    <br>
    密码：<input type="password" name="password">
    <br>
    <button>保存</button>
</form>
</body>
</html>

```

```html

<!DOCTYPE html>
<html lang="en" xmlns:th="http://www.thymeleaf.org">
<head>
    <meta charset="UTF-8">
    <title>success</title>
</head>
<body>
<h1>保存成功</h1>
</body>
</html>

```

启动服务器，然后打开首页面，填写表单，保存数据，最终数据库中成功插入一条记录，则表示 SSM 整合成功。

到此，SpringMVC 的课程就结束了。
