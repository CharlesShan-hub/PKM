# Spring Data Redis

> 基于ACL + 密码（注意：以下案例讲解的是在Redis未启用TLS/SSL的前提下进行的）

---

## SpringBoot 项目配置

### 添加依赖

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

### 配置 application.yml

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

## 创建 Redis 配置类

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

## RedisTemplate

**<font style="color:#000000;">RedisTemplate是 Spring Data Redis 框架提供的：（Spring Data Redis 是 Spring Data 的一部分，SpringBoot 框架自动集成了 Spring Data，这是他们三者的关系。）</font>**

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

## <font style="color:rgb(64, 64, 64);">创建业务类</font>

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

## 创建控制器测试 Redis

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

## 测试接口

1. 启动 SpringBoot 应用
2. 使用curl 测试接口：
    - `curl -X POST http://localhost:8080/api/redis/set" -d "key=test&value=hello"`
    - `curl "http://localhost:8080/api/redis/get/test"`
    - `curl -X DELETE "http://localhost:8080/api/redis/delete?key=test"`
    - `curl "http://localhost:8080/api/redis/hasKey?key=test"`
