# Jedis 进阶使用

---

## 连接池

### 1. 连接池概述
Redis连接池是一种管理Redis连接的技术，通过预先创建并维护一定数量的连接，避免频繁创建和销毁连接带来的性能开销。

### 2. 连接池配置参数
```java
// Jedis连接池配置
JedisPoolConfig poolConfig = new JedisPoolConfig();
poolConfig.setMaxTotal(100);           // 最大连接数
poolConfig.setMaxIdle(20);             // 最大空闲连接数
poolConfig.setMinIdle(5);              // 最小空闲连接数
poolConfig.setMaxWaitMillis(3000);    // 获取连接时的最大等待毫秒数
poolConfig.setTestOnBorrow(true);      // 在获取连接时检查有效性
poolConfig.setTestOnReturn(true);      // 在归还连接时检查有效性
poolConfig.setTestWhileIdle(true);     // 空闲时检查连接有效性
poolConfig.setTimeBetweenEvictionRunsMillis(30000); // 逐出扫描的时间间隔
poolConfig.setNumTestsPerEvictionRun(10); // 每次逐出检查的最大连接数
```

### 3. 连接池使用示例
```java
// 创建连接池
JedisPool jedisPool = new JedisPool(poolConfig, "localhost", 6379);

// 从连接池获取连接
try (Jedis jedis = jedisPool.getResource()) {
    // 执行Redis命令
    jedis.set("key", "value");
    String value = jedis.get("key");
    System.out.println(value);
}

// 关闭连接池
jedisPool.close();
```

---

## 管道（Pipeline）

### 1. 管道概述
Redis管道技术允许客户端一次性发送多个命令到服务器，而不需要等待每个命令的响应，最后一次性读取所有响应，大大减少网络往返时间。

### 2. 管道使用示例
```java
// 使用管道批量操作
try (Jedis jedis = jedisPool.getResource()) {
    Pipeline pipeline = jedis.pipelined();
    
    // 批量设置多个键值对
    for (int i = 0; i < 100; i++) {
        pipeline.set("key" + i, "value" + i);
    }
    
    // 执行所有命令
    pipeline.sync();
}

// 管道与事务结合使用
try (Jedis jedis = jedisPool.getResource()) {
    Pipeline pipeline = jedis.pipelined();
    
    // 开启事务
    pipeline.multi();
    
    // 在事务中执行多个命令
    pipeline.set("user:1:name", "张三");
    pipeline.set("user:1:age", "25");
    pipeline.incr("user:1:visits");
    
    // 提交事务
    pipeline.exec();
    
    // 同步执行
    pipeline.sync();
}
```

### 3. 管道响应处理
```java
try (Jedis jedis = jedisPool.getResource()) {
    Pipeline pipeline = jedis.pipelined();
    
    // 发送多个命令
    Response<String> response1 = pipeline.get("key1");
    Response<String> response2 = pipeline.get("key2");
    Response<Long> response3 = pipeline.incr("counter");
    
    // 同步执行
    pipeline.sync();
    
    // 获取响应结果
    String value1 = response1.get();
    String value2 = response2.get();
    Long counter = response3.get();
    
    System.out.println("key1: " + value1);
    System.out.println("key2: " + value2);
    System.out.println("counter: " + counter);
}
```

---

## 连接池与管道结合使用的最佳实践

### 1. 资源管理
```java
public class RedisUtil {
    private static JedisPool jedisPool;
    
    static {
        JedisPoolConfig config = new JedisPoolConfig();
        config.setMaxTotal(50);
        config.setMaxIdle(10);
        config.setMinIdle(5);
        config.setMaxWaitMillis(3000);
        config.setTestOnBorrow(true);
        
        jedisPool = new JedisPool(config, "localhost", 6379, 2000, "password");
    }
    
    // 使用管道进行批量操作
    public void batchSet(Map<String, String> keyValueMap) {
        try (Jedis jedis = jedisPool.getResource()) {
            Pipeline pipeline = jedis.pipelined();
            
            for (Map.Entry<String, String> entry : keyValueMap.entrySet()) {
                pipeline.set(entry.getKey(), entry.getValue());
            }
            
            pipeline.sync();
        }
    }
}
```

### 2. 性能优化建议
- **连接池大小**：根据并发量调整，一般建议最大连接数为并发线程数的1.5-2倍
- **管道批处理**：一次性处理100-1000个命令可获得最佳性能
- **资源释放**：确保在使用完毕后正确关闭连接

### 3. 错误处理
```java
try (Jedis jedis = jedisPool.getResource()) {
    Pipeline pipeline = jedis.pipelined();
    
    try {
        // 管道操作
        pipeline.set("key1", "value1");
        pipeline.set("key2", "value2");
        
        pipeline.sync();
    } catch (Exception e) {
        // 错误处理
        pipeline.discard();
        throw e;
    }
}
```
