# 第一个MyBatis-Plus

提示：MyBatis-Plus是基于SpringBoot框架的。

第一步：引入 `MyBatis-Plus`依赖（注意：以下引入的是适合于`Spring Boot 3`的依赖）

```xml

<dependency>
  <groupId>com.baomidou</groupId>
  <artifactId>mybatis-plus-spring-boot3-starter</artifactId>
  <version>3.5.11</version>
</dependency>

```

第二步：`Mapper`接口继承`BaseMapper`

```java

package com.jkweilai.mp.mapper;

import com.baomidou.mybatisplus.core.mapper.BaseMapper;
import com.jkweilai.mp.model.Car;

public interface CarMapper extends BaseMapper<Car> {
}

```

具体步骤如下：

第一步：依赖

```xml

<dependencies>
  <!--spring boot核心启动器-->
  <dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter</artifactId>
  </dependency>
  <!--MyBatis-Plus的Spring Boot 3的启动器-->
  <dependency>
    <groupId>com.baomidou</groupId>
    <artifactId>mybatis-plus-spring-boot3-starter</artifactId>
    <version>3.5.11</version>
  </dependency>
  <!--mysql驱动-->
  <dependency>
    <groupId>com.mysql</groupId>
    <artifactId>mysql-connector-j</artifactId>
    <scope>runtime</scope>
  </dependency>
  <!--lombok依赖-->
  <dependency>
    <groupId>org.projectlombok</groupId>
    <artifactId>lombok</artifactId>
    <optional>true</optional>
  </dependency>
  <!--Spring Boot 3测试启动器-->
  <dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-test</artifactId>
    <scope>test</scope>
  </dependency>
</dependencies>

```

第二步：编写实体类

```java

package com.jkweilai.mp.model;

import com.baomidou.mybatisplus.annotation.TableName;
import lombok.Data;

@Data
@TableName("t_car")
public class Car {
    private Long id;
    private String carNum;
    private String brand;
    private Double guidePrice;
    private String produceTime;
    private String carType;
}

```

第三步：编写yml配置

```yaml
