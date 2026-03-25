# Spring 

---

## Spring Data 集成

### Springboot 基础配置

> 基于ACL + 密码（注意：以下案例讲解的是在Redis未启用TLS/SSL的前提下进行的）

pom.xml

```xml
<dependency>
  <groupId>org.springframework.boot</groupId>
  <artifactId>spring-boot-starter-data-redis</artifactId>
</dependency>

<!--做连接池优化的-->
<dependency>
  <groupId>org.apache.commons</groupId>
  <artifactId>commons-pool2</artifactId>
  <version>2.12.0</version>
</dependency>
```

application.yml

```yml
spring:
  data: # 经过测试，不加这个data也能运行，但是ai说还是加上更规范
    redis:
      host: 192.168.48.200
      port: 6379
      password: 123456
      username: default
      lettuce:
        pool:
          enabled: true
          max-active: 8
          max-idle: 8
          min-idle: 0
          max-wait: -1ms
```

### 创建 Redis 配置类

序列化器的作用：**将Java对象与Redis存储的二进制数据互相转换**

1. key用字符串序列化（方便查看）
2. value用JSON序列化（可存复杂对象）

对于比较复杂的内容比如把User类保存到redis里边，需要自己的像下边一样定义配置类，但如果只需要简单的了类型也可以不弄，比如value只能是String。

```java
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.data.redis.connection.RedisConnectionFactory;
import org.springframework.data.redis.core.RedisTemplate;
import org.springframework.data.redis.serializer.GenericJackson2JsonRedisSerializer;
import org.springframework.data.redis.serializer.StringRedisSerializer;

@Configuration
public class RedisConfig {
    @Bean
    public RedisTemplate<String, Object> redisTemplate(RedisConnectionFactory connectionFactory) {
        RedisTemplate<String, Object> template = new RedisTemplate<>();
        template.setConnectionFactory(connectionFactory);

        // 设置string/list/set/zset类型的序列化器
        // 使用 String 序列化器序列化 key
        template.setKeySerializer(new StringRedisSerializer());
        // 使用 Jackson 序列化器序列化 value
        template.setValueSerializer(new GenericJackson2JsonRedisSerializer());

        // 设置hash类型的序列化器
        template.setHashKeySerializer(new StringRedisSerializer());
        template.setHashValueSerializer(new GenericJackson2JsonRedisSerializer());

        return template;
    }
}
```

### RedisTemplate

RedisTemplate是 Spring Data Redis 框架提供的：（Spring Data Redis 是 Spring Data 的一部分，SpringBoot 框架自动集成了 Spring Data，这是他们三者的关系。）

- 底层可以使用 Jedis 或 Lettuce（更主流） 作为客户端
- 自动管理连接池和资源
- 提供更面向对象的操作方式
- 内置序列化支持
- 与 Spring 生态无缝集成

RedisTemplate 设计了两层 API：

第一层：Template自身方法（管理类操作）

```java
// 这些是"模板级"操作，不需要指定数据类型
redisTemplate.hasKey("key")          // 是否存在key
redisTemplate.delete("key")          // 删除key
redisTemplate.expire("key", 10, TimeUnit.SECONDS) // 设置过期
redisTemplate.type("key")            // 获取key类型
redisTemplate.keys("user:*")         // 模式匹配查询
redisTemplate.getConnectionFactory() // 获取连接工厂
redisTemplate.execute(...)           // 执行自定义操作
```

第二层：Operations接口（数据类操作）

```java
// 这些是"数据操作"，需要先指定操作哪种数据结构
redisTemplate.opsForValue().set("key", "value")      // String操作
redisTemplate.opsForList().leftPush("list", "item")  // List操作  
redisTemplate.opsForSet().add("set", "member")       // Set操作
redisTemplate.opsForHash().put("hash", "field", "val") // Hash操作
redisTemplate.opsForZSet().add("zset", "member", 100) // ZSet操作
```

### <font style="color:rgb(64, 64, 64);">创建业务类</font>

创建一个服务类来演示 Redis 操作：

```java
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.redis.core.RedisTemplate;
import org.springframework.stereotype.Service;

import java.util.concurrent.TimeUnit;

@Service
public class RedisService {

    @Autowired
    private RedisTemplate<String, Object> redisTemplate;

    public void setValue(String key, Object value) {
        redisTemplate.opsForValue().set(key, value);
    }

    public void setValueEx(String key, Object value, long timeout, TimeUnit unit) {
        redisTemplate.opsForValue().set(key, value, timeout, unit);
    }

    public Object getValue(String key) {
        return redisTemplate.opsForValue().get(key);
    }

    public Boolean deleteKey(String key) {
        return redisTemplate.delete(key);
    }

    public Boolean hasKey(String key) {
        return redisTemplate.hasKey(key);
    }
}

```

### 创建控制器测试 Redis

```java
import com.laodu.demo.service.RedisService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

@RequestMapping("/api/redis")
@RestController
public class RedisController {

    @Autowired
    private RedisService redisService;

    @PostMapping("/set")
    public String setValue(@RequestParam String key, @RequestParam String value) {
        redisService.setValue(key, value);
        return "set key-value success : " + key + "=" + value;
    }

    @GetMapping("/get/{key}")
    public Object getValue(@PathVariable("key") String key) {
        return redisService.getValue(key);
    }

    @DeleteMapping("/delete/{key}")
    public String deleteKey(@PathVariable("key") String key) {
        redisService.deleteKey(key);
        return "delete success : " + key;
    }

    @GetMapping("/has/{key}")
    public String hasKey(@PathVariable("key") String key) {
        return redisService.hasKey(key) ? "存在" + key : "不存在" + key;
    }

}
```

### 测试接口

1. 启动 SpringBoot 应用
2. 使用curl 测试接口：
    - `curl -X POST http://localhost:8080/api/redis/set" -d "key=test&value=hello"`
    - `curl "http://localhost:8080/api/redis/get/test"`
    - `curl -X DELETE "http://localhost:8080/api/redis/delete?key=test"`
    - `curl "http://localhost:8080/api/redis/hasKey?key=test"`

---

## Spring Cache 高速缓存

使用`SpringBoot3 + MySQL8 + Redis7 + MyBatisPlus`实现高速缓存。

其实核心就是三个注解
```JAVA
import org.springframework.cache.annotation.CacheEvict;
import org.springframework.cache.annotation.CachePut;
import org.springframework.cache.annotation.Cacheable;
```

> 所谓的高速缓存指的是，查询时先从Redis缓存中读取，如果没有再从数据库中获取，获取到之后，将数据放入Redis缓存，以备下次使用。

### 项目配置

确保pom.xml包含以下依赖：

```xml
<dependencies>
    <!-- Spring Boot Starter -->
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-web</artifactId>
    </dependency>
    
    <!-- Redis -->
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-data-redis</artifactId>
    </dependency>
    
    <!-- MySQL -->
    <dependency>
        <groupId>com.mysql</groupId>
        <artifactId>mysql-connector-j</artifactId>
        <scope>runtime</scope>
    </dependency>
    
    <!-- MyBatis-Plus -->
    <dependency>
        <groupId>com.baomidou</groupId>
        <artifactId>mybatis-plus-spring-boot3-starter</artifactId>
        <version>3.5.11</version>
    </dependency>
    
    <!-- Lombok -->
    <dependency>
        <groupId>org.projectlombok</groupId>
        <artifactId>lombok</artifactId>
        <optional>true</optional>
    </dependency>
    
    <!-- 测试 -->
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-test</artifactId>
        <scope>test</scope>
    </dependency>
</dependencies>

```

`application.yml`配置：

```yaml
server:
  port: 8080

spring:
  datasource:
    driver-class-name: com.mysql.cj.jdbc.Driver
    url: jdbc:mysql://localhost:3306/cache_demo?useSSL=false&serverTimezone=Asia/Shanghai&characterEncoding=utf8
    username: root
    password: 123456

  data:
    redis:
      host: 192.168.48.200
      port: 6379
      username: default
      password: 123456
      database: 0
      lettuce:
        pool:
          max-active: 8
          max-wait: -1ms
          max-idle: 8
          min-idle: 0
      timeout: 5000ms

mybatis-plus:
  configuration:
    log-impl: org.apache.ibatis.logging.stdout.StdOutImpl
  global-config:
    db-config:
      id-type: auto
      logic-delete-field: deleted
      logic-delete-value: 1
      logic-not-delete-value: 0
```

cache_demo.sql

```sql
CREATE DATABASE IF NOT EXISTS cache_demo DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

USE cache_demo;

CREATE TABLE IF NOT EXISTS product (
    id BIGINT NOT NULL AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    price DECIMAL(10,2) NOT NULL,
    stock INT NOT NULL,
    create_time DATETIME DEFAULT CURRENT_TIMESTAMP,
    update_time DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    deleted TINYINT(1) DEFAULT 0,
    PRIMARY KEY (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

INSERT INTO product (name, price, stock) VALUES 
('iPhone 15', 9999.00, 100),
('MacBook Pro', 14999.00, 50),
('AirPods Pro', 1999.00, 200);
```

### Entity

```java
package com.laodu.cache.model.po;

import com.baomidou.mybatisplus.annotation.*;
import lombok.Data;

import java.math.BigDecimal;
import java.util.Date;

@Data
@TableName("product")
public class Product {
    @TableId(value = "id", type = IdType.AUTO)
    private Long id;
    private String name;
    private BigDecimal price;
    private Integer stock;

    @TableField(fill = FieldFill.INSERT) // 执行insert操作时自动填充
    private Date createTime;

    @TableField(fill = FieldFill.INSERT_UPDATE) // 执行insert和update操作时自动填充
    private Date updateTime;

    @TableLogic
    private Integer deleted;
}
```

### Mapper

```java
package com.laodu.cache.mapper;

import com.baomidou.mybatisplus.core.mapper.BaseMapper;
import com.laodu.cache.model.po.Product;

public interface ProductMapper extends BaseMapper<Product> {
}
```

### Service

接口

```java
package com.laodu.cache.service;

import com.baomidou.mybatisplus.extension.service.IService;
import com.laodu.cache.model.po.Product;

public interface ProductService extends IService<Product> {
    Product getProductById(Long id);

    Product updateProduct(Product product);

    boolean removeProductById(Long id);
}

```

实现类

```java
package com.laodu.cache.service.impl;

import com.baomidou.mybatisplus.extension.service.impl.ServiceImpl;
import com.laodu.cache.mapper.ProductMapper;
import com.laodu.cache.model.po.Product;
import com.laodu.cache.service.ProductService;
import org.springframework.cache.annotation.CacheEvict;
import org.springframework.cache.annotation.CachePut;
import org.springframework.cache.annotation.Cacheable;
import org.springframework.stereotype.Service;

@Service
public class ProductServiceImpl extends ServiceImpl<ProductMapper, Product> implements ProductService {

    // 1.@Cacheable注解是spring框架提供的，专门用于整合缓存数据库而存在的注解。
    // 2.该注解作用是：从缓存中读取数据，如果缓存中没有数据就从数据库中取数据，取到的数据放入缓存中。
    // 3.放入Redis缓存中的数据都需要设置key，该注解中的value和key属性联合起来生成Redis的key
    // 4.假设商品id是123，则生成的Redis的key是：product::123，两个冒号是Spring Cache的默认规则。
    // 5. #id 中的 #是SpEL语法规则，表示将参数id拿到后放到这里。如果取参数，则必须使用 # 开头。
    // 6. @Cacheable 优先读缓存，缓存不存在才执行方法。
    // 底层是aop实现的
    @Override
    @Cacheable(value = "product", key = "#id")
    public Product getProductById(Long id) {
        System.out.println("查询数据库获取产品，ID：" + id);
        return getById(id);
    }

    // 1. @CachePut 这个注解标注的方法，每一次都会执行该方法。
    // 2. 方法执行时更新数据库，然后将方法的返回值更新Redis缓存。
    @Override
    @CachePut(value = "product", key = "#product.id")
    public Product updateProduct(Product product) {
        System.out.println("更新数据库中的产品，ID：" + product.getId());
        updateById(product);
        return product;
    }

    // 1. @CacheEvict 执行该方法后清除缓存。
    @Override
    @CacheEvict(value = "product", key = "#id")
    public boolean removeProductById(Long id) {
        System.out.println("删除数据库中的产品，ID：" + id);
        return removeById(id);
    }
}

```

### Controller

```java
package com.laodu.cache.controller;

import com.laodu.cache.model.po.Product;
import com.laodu.cache.service.ProductService;
import lombok.RequiredArgsConstructor;
import org.springframework.web.bind.annotation.*;

@RequestMapping("/product")
@RestController
@RequiredArgsConstructor
public class ProductController {
    private final ProductService productService;

    @GetMapping("/{id}")
    public Product getProductById(@PathVariable Long id) {
        return productService.getProductById(id);
    }

    @PutMapping
    public Product modifyProduct(@RequestBody Product product) {
        return productService.updateProduct(product);
    }

    @DeleteMapping("/{id}")
    public boolean removeById(@PathVariable Long id) {
        return productService.removeProductById(id);
    }
}


```

### 缓存配置类

```java
package com.laodu.cache.config;

import org.springframework.cache.annotation.EnableCaching;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.data.redis.cache.RedisCacheConfiguration;
import org.springframework.data.redis.cache.RedisCacheManager;
import org.springframework.data.redis.connection.RedisConnectionFactory;
import org.springframework.data.redis.serializer.GenericJackson2JsonRedisSerializer;
import org.springframework.data.redis.serializer.RedisSerializationContext;
import org.springframework.data.redis.serializer.StringRedisSerializer;

import java.time.Duration;

@Configuration
@EnableCaching
public class RedisConfig {

    @Bean
    public RedisCacheManager cacheManager(RedisConnectionFactory connectionFactory) {
        RedisCacheConfiguration config = RedisCacheConfiguration.defaultCacheConfig().entryTtl(Duration.ofMinutes(30)) // 默认缓存30分钟
                .serializeKeysWith(RedisSerializationContext.SerializationPair.fromSerializer(new StringRedisSerializer()))
                .serializeValuesWith(RedisSerializationContext.SerializationPair.fromSerializer(new GenericJackson2JsonRedisSerializer()))
                .disableCachingNullValues(); // 不允许缓存null值。

        return RedisCacheManager.builder(connectionFactory).cacheDefaults(config).transactionAware().build();
    }
}


```

### 测试与验证

#### 启动类

```java
package com.laodu.cache;

import org.mybatis.spring.annotation.MapperScan;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@MapperScan(basePackages = "com.laodu.cache.mapper")
@SpringBootApplication
public class CacheApplication {

        public static void main(String[] args) {
                SpringApplication.run(CacheApplication.class, args);
        }

}
```

#### 测试步骤

1. 启动Redis服务器和MySQL服务器
2. 运行Spring Boot应用
3. 使用Postman或curl测试以下接口：

测试获取产品（第一次查询会访问数据库，后续查询会走缓存）

```bash
curl http://localhost:8080/product/1
```

测试更新产品（会同时更新数据库和缓存）

```bash
curl -X PUT http://localhost:8080/product -H "Content-Type: application/json" -d "{\"id\":1,\"name\":\"iPhone 15 Pro\",\"price\":10999.00,\"stock\":80}"
```

对于windows的powershell，更新产品的指令修改一点

```powershell
irm -Method PUT http://localhost:8080/product -ContentType "application/json" -Body '{"id":1,"name":"iPhone 15 Pro","price":10999.00,"stock":80}'
```

测试删除产品（会同时删除数据库记录和缓存）

```bash
curl -X DELETE http://localhost:8080/product/1
```

---
## 事务

`RedisTemplate` 代码中使用事务

实现事务的代码示例：

```java
public void basicTransaction() {
    
    // 使用SessionCallback确保所有操作在同一个连接
    redisTemplate.execute(new SessionCallback<List<Object>>() {
        @Override
        public List<Object> execute(RedisOperations operations) throws DataAccessException {
            // 1. 开启事务
            operations.multi();
            
            // 2. 执行多个操作（只是入队，不真正执行）
            operations.opsForValue().set("name", "张三");
            operations.opsForValue().set("age", "25");
            operations.opsForSet().add("skills", "Java", "Redis");
            
            // 3. 提交事务，返回所有命令的执行结果
            return operations.exec();
        }
    });
}
```

使用 WATCH 实现的乐观锁

```java
// 带乐观锁的事务示例
public void watchTransaction() {
    List<Object> results = redisTemplate.execute(new SessionCallback<List<Object>>() {
        @Override
        public List<Object> execute(RedisOperations operations) throws DataAccessException {
            String key = "counter";
            
            // 1. 监控key，如果被其他客户端修改，事务会失败
            operations.watch(key);
            
            // 2. 获取当前值
            Object current = operations.opsForValue().get(key);
            int value = current == null ? 0 : Integer.parseInt(current.toString());
            
            // 3. 开启事务
            operations.multi();
            
            // 4. 在事务中执行操作
            operations.opsForValue().set(key, String.valueOf(value + 1));
            operations.opsForValue().set("last_update", System.currentTimeMillis());
            
            // 5. 提交事务
            // 如果key被其他客户端修改过，exec()会返回null
            List<Object> execResults = operations.exec();
            
            if (execResults == null) {
                System.out.println("事务失败：key被其他客户端修改");
            } else {
                System.out.println("事务成功：" + execResults);
            }
            
            return execResults;
        }
    });
}
```

lambda 方式

```java
redisTemplate.execute((RedisOperations ops) -> {
    ops.multi();
    ops.opsForValue().set("a", "1");
    ops.opsForValue().set("b", "2");
    return ops.exec();  // 提交事务
});

redisTemplate.execute((RedisOperations ops) -> {
    ops.watch("count");        // 监控
    ops.multi();               // 开启事务
    ops.opsForValue().increment("count", 1);
    return ops.exec();         // 提交，如果count被改过则返回null
});
```
