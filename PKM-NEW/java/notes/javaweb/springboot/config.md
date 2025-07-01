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

