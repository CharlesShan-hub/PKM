# 整合SpringMVC（SSM整合）

SSM整合：Spring + SpringMVC + MyBatis

Spring Boot项目本身就是基于Spring框架实现的。因此SSM整合时，只需要在整合MyBatis框架之后，引入`web启动器`即可完成SSM整合。

---

## 使用脚手架创建SpringBoot项目

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1764860440431-1b1d9d22-9df1-4188-9a14-60dc1e5d47af.png" width="693.6" title="" crop="0,0,1,1" id="ub0179b14" class="ne-image">

添加依赖：web启动器、mybatis启动器、mysql驱动依赖、lombok依赖

<img src="https://cdn.nlark.com/yuque/0/2024/png/21376908/1729239349172-b9c47742-c09f-4f5b-8422-35a7a9dbab72.png" width="961" title="" crop="0,0,1,1" id="uda13af2c" class="ne-image">

---

## 使用`free mybatis tool`插件逆向生成MyBatis代码

将`springboot`数据库中的`t_vip`表逆向生成mybatis代码。这里不再赘述。

---

## 整合MyBatis

1. 编写数据源的配置

```properties
spring.datasource.driver-class-name=com.mysql.cj.jdbc.Driver
spring.datasource.url=jdbc:mysql://localhost:3306/springboot
spring.datasource.username=root
spring.datasource.password=123456
spring.datasource.type=com.zaxxer.hikari.HikariDataSource
```

2. 编写mapper xml配置文件的位置

```properties
mybatis.mapper-locations=classpath:mapper/*.xml
mybatis.configuration.map-underscore-to-camel-case=true
```

3. 在主入口类上添加`@MapperScan`注解

```java
package com.jkweilai.sb307ssm;

import org.mybatis.spring.annotation.MapperScan;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@MapperScan(basePackages = {"com.jkweilai.sb307ssm.repository"})
@SpringBootApplication
public class Sb307SsmApplication {

    public static void main(String[] args) {
        SpringApplication.run(Sb307SsmApplication.class, args);
    }

}
```

---

## 编写service

编写`VipService`接口：

```java
package com.jkweilai.sb307ssm.service;

import com.jkweilai.sb307ssm.entity.Vip;

public interface VipService {
    /**
     * 根据id获取会员信息
     * @param id 会员标识
     * @return 会员信息
     */
    Vip getById(Long id);
}

```

编写`VipServiceImpl`实现类：

```java
package com.jkweilai.sb307ssm.service.impl;

import com.jkweilai.sb307ssm.entity.Vip;
import com.jkweilai.sb307ssm.repository.VipMapper;
import com.jkweilai.sb307ssm.service.VipService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

@Service("vipService")
public class VipServiceImpl implements VipService {

    @Autowired
    private VipMapper vipMapper;

    @Override
    public Vip getById(Long id) {
        return vipMapper.selectByPrimaryKey(id);
    }
}

```

---

## 编写controller

编写`VipController`，代码如下：

```java
package com.jkweilai.sb307ssm.controller;

import com.jkweilai.sb307ssm.entity.Vip;
import com.jkweilai.sb307ssm.service.VipService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class VipController {
    
    @Autowired
    private VipService vipService;
    
    @GetMapping("/vip/{id}")
    public Vip detailById(@PathVariable("id") Long id){
        Vip vip = vipService.getById(id);
        return vip;
    }
}

```

---

## 启动服务器测试

执行SpringBoot项目主入口的main方法，启动Tomcat服务器：

<img src="https://cdn.nlark.com/yuque/0/2024/png/21376908/1729242182367-079ee0e1-acaa-42f3-970e-c7ff410b336c.png" width="1209" title="" crop="0,0,1,1" id="ufc9fb32e" class="ne-image">

打开浏览器访问：

<img src="https://cdn.nlark.com/yuque/0/2024/png/21376908/1729242269867-255b4446-4fae-4788-beb6-fc395155ed61.png" width="394" title="" crop="0,0,1,1" id="uf735c5f5" class="ne-image">

到此为止，SSM框架就集成完毕了，通过这个集成也可以感觉到SpringBoot简化了SSM三大框架的集成。

