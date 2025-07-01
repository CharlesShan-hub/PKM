## Springboot Config

## 资源

* https://www.bilibili.com/video/BV14z4y1N7pg/?p=5
* Spring Boot中的yaml配置简介: https://mp.weixin.qq.com/s/dbSBzFICIDPLkj5Tuv2-yA
* 是时候彻底搞清楚 Spring Boot 的配置文件 application.properties 了！: https://www.javaboy.org/2019/0530/application.properties.html
* 官方文档: https://docs.spring.io/spring-boot/appendix/application-properties/index.html

---
## 配置文件格式

1. 我们在`application.properties`进行 springboot 的一些配置。
2. 可以使用properties格式
```properties
	# 服务器端口
	server.port=8080
	
	# 数据库配置 (H2内存数据库示例)
	spring.datasource.url=jdbc:h2:mem:testdb
	spring.datasource.driver-class-name=org.h2.Driver
	spring.datasource.username=sa
	spring.datasource.password=
	
	# JPA/Hibernate配置
	spring.jpa.show-sql=true
	spring.jpa.hibernate.ddl-auto=update
	
	# 应用名称
	spring.application.name=my-demo-app
```
3. 可以使用 yaml 格式（更加常用）
```yaml
# 服务器端口
server:
  port: 8080

# 数据库配置 (H2内存数据库示例)
spring:
  datasource:
    url: jdbc:h2:mem:testdb
    driver-class-name: org.h2.Driver
    username: sa
    password: ""
  jpa:
    show-sql: true
    hibernate:
      ddl-auto: update
  application:
    name: my-demo-app
```

---
## 使用配置文件

### value
application.yaml
```yaml
server:
  port: 8080
user:
  name: 'Charles'
```

HelloWorldController.java：采用`@Value`进行配置的获取。
```Java
package com.charlesshan.helloworld.controller;

import org.springframework.beans.factory.annotation.Value;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class HelloController {
    @Value("${user.name}")
    public String name;
    
    @RequestMapping("/name")
    public String name(){
        return name;
    }
}
```

使用，访问`http://localhost:8080/name`，返回`Charles`

### ConfigrationProtites
如果我们的配置是一个完整的对象，一项一项的读太麻烦了，如何作为一个整体读进来呢

application.yaml
```YAML
server:
  port: 8080
spring:
  datasource:
    url: jdbc:mysql://localhost:3306/test_db?useSSL=false&serverTimezone=UTC
    username: root
    password: 123456
```

DbConfig.java：写一个配置类用来保存配置
```Java
package com.charlesshan.helloworld.config;

import lombok.Data;
import org.springframework.boot.context.properties.ConfigurationProperties;
import org.springframework.stereotype.Component;

@Data
@Component
@ConfigurationProperties(prefix = "spring.datasource")
public class DbConfig {
    private String url;
    private String username;
    private String password;
}
```

HelloController.java
```Java
package com.charlesshan.helloworld.controller;

import com.charlesshan.helloworld.config.DbConfig;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class HelloController {
    @Autowired
    private DbConfig dbConfig;
    @RequestMapping("/db_config")
    public DbConfig default_user() {
        if (dbConfig == null) {
            dbConfig = new DbConfig();
        }
        return dbConfig;
    }
}
```

访问http://localhost:8080/db_config，可以看到返回的内容
```json
{
	"url":"jdbc:mysql://localhost:3306/test_db?useSSL=false&serverTimezone=UTC",
	"username":"root",
	"password":"123456"
}
```

---
## 整合 MyBatis

