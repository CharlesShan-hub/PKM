# Jedis 进阶使用

---

## 连接池

### 连接池概述

Redis连接池是一种管理Redis连接的技术，通过预先创建并维护一定数量的连接，避免频繁创建和销毁连接带来的性能开销。

### 连接池配置：`JedisPollConfig`

```java
// Jedis连接池配置
JedisPoolConfig poolConfig = new JedisPoolConfig();
poolConfig.setMaxTotal(100);           // 最大连接数
poolConfig.setMaxIdle(50);             // 最大空闲连接数，建议 maxTotal 的50%~70%
poolConfig.setMinIdle(10);              // 最小空闲连接数，建议预留出10到20个
poolConfig.setMaxWaitMillis(3000);    // 获取连接时的最大等待毫秒数，避免无限等待，超时报错
poolConfig.setTestOnBorrow(true);      // 在获取连接时检查有效性，推荐true
poolConfig.setTestOnReturn(false);      // 在归还连接时检查有效性，推荐false
poolConfig.setTestWhileIdle(true);     // 空闲时检查连接有效性，推荐true，并设置空闲检查周期
poolConfig.setTimeBetweenEvictionRunsMillis(60000); // 空闲检查周期，推荐每一分钟检测一次
poolConfig.setMinEvictableIdleTime(Duration.ofMinutes(3)); // 推荐三分钟，不连接了就标记空闲
poolConfig.setNumTestsPerEvictionRun(10); // 每次逐出检查的最大连接数
```

### 连接池使用示例：`JedisPool`

工具类

```java
public class JedisUtil {
    // 连接池
    private static JedisPool jedisPool;

    // 类加载时初始化连接池
    static {
        JedisPoolConfig config = new JedisPoolConfig();
        config.setMaxTotal(100);
        config.setMaxIdle(50);
        config.setTestOnBorrow(true);
        // Protocol.DEFAULT_TIMEOUT 是 Jedis 客户端连接 Redis 服务器时的默认超时时间（2000 毫秒/2 秒）
        jedisPool = new JedisPool(config, "192.168.48.200", 6379, Protocol.DEFAULT_TIMEOUT, "123456");
    }

    // 从连接池中获取空闲的 Jedis
    public static Jedis getResource() {
        return jedisPool.getResource();
    }

    // 一般整个应用结束的时候（服务器关闭）调用这个方法关闭连接池。
    public static void close(){
        jedisPool.close();
    }
}
```

使用连接池

```java
// 正确的做法：自动归还连接（try-with-resources）
try (Jedis jedis = JedisUtil.getResource()) {
    jedis.set("key", "value");
    String value = jedis.get("key");
}

// 错误的做法：忘记归还连接，导致泄漏！
Jedis jedis = JedisUtil.getResource();
jedis.set("key", "value");
```

### 异常处理

- `JedisConnectionException`：网络问题或Redis宕机。
- `JedisExhaustedPoolException`：连接池耗尽（`maxTotal` 太小）。
- `SocketTimeoutException`：Redis响应超时。

### 优化建议

**QPS（Queries Per Second）** 是指每秒查询数，用于衡量系统的吞吐量。

计算方式：

```plaintext
QPS = 总请求量 / 总时间(秒)
```

例如：1分钟内处理了6000次请求 → QPS = 6000 / 60 = 100。
一般通过压测工具（如**JMeter**）模拟请求统计得出。

连接池大小（**重点**）

- 计算公式：`maxTotal ≈ QPS × avg_query_time(ms) / 1000`
- 例如：QPS=1000，平均查询时间=10ms → maxTotal ≈ 10（这样的话，10 个连接理论上可以保证 10ms 内处理 1000 个查询）
- 安全系数：以上公式计算的是最小值。实际情况下需要考虑安全系数。它是来应付突发情况的。
- Redis连接池安全系数建议**1.2-1.5**倍，数据库连接池建议**2-3**倍，因为数据库连接创建成本更高、需要更多缓冲。

超时设置

- `maxWaitMillis` 不宜过长（避免线程堆积）。

健康检测

- 开启 `testOnBorrow` 或 `testWhileIdle`。

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

### 4. 连接池与管道结合使用的最佳实践

#### 资源管理

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

#### 性能优化建议

- **连接池大小**：根据并发量调整，一般建议最大连接数为并发线程数的1.5-2倍
- **管道批处理**：一次性处理100-1000个命令可获得最佳性能
- **资源释放**：确保在使用完毕后正确关闭连接

#### 错误处理

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

---

## Jedis 支持 ACL

### 封装用户名与密码： `DefaultJedisClientConfig`

Jedis 4.x 版本推荐使用 `DefaultJedisClientConfig` 配置用户名和密码（ACL 需要用户名+密码，而不仅仅是密码）。

```java
package top.charles;  
  
import redis.clients.jedis.Jedis;  
import redis.clients.jedis.JedisClientConfig;  
import redis.clients.jedis.DefaultJedisClientConfig;  
  
public class TestACL {  
    public static void main(String[] args) {  
        // Redis 7 + ACL 需要 username + password
        String username = "default";  // Redis 默认用户是 "default"，也可能是你自定义的
        String password = "123456";  
  
        // 使用 DefaultJedisClientConfig 配置
        JedisClientConfig config = DefaultJedisClientConfig.builder()
                .user(username)  // ACL 用户名
                .password(password)  // ACL 密码
                .timeoutMillis(5000)  // 超时时间
                .build();  
  
        try (Jedis jedis = new Jedis("127.0.0.1", 6379, config)) {
            // 测试连接
            System.out.println("Ping: " + jedis.ping());  
  
            // 执行命令
            jedis.set("mykey", "myvalue");  
            System.out.println("Get key: " + jedis.get("mykey"));  
        }  
    }  
}
```

### `JedisPool` + ACL（生产推荐）

生产环境推荐使用连接池，避免频繁创建/销毁连接。

```java
package top.charles;  
  
import redis.clients.jedis.*;  
  
public class TestACLPool {  
    public static void main(String[] args) {  
        String username = "default";  // 或你的自定义ACL用户  
        String password = "123456";  
  
        // 1. 配置连接池  
        JedisPoolConfig poolConfig = new JedisPoolConfig();  
        poolConfig.setMaxTotal(10);  // 最大连接数  
        poolConfig.setMaxIdle(5);    // 最大空闲连接  
        poolConfig.setMinIdle(1);    // 最小空闲连接  
  
        // 2. 使用 DefaultJedisClientConfig 配置 ACL
        JedisClientConfig jedisClientConfig = DefaultJedisClientConfig.builder()  
                .user(username)  
                .password(password)  
                .timeoutMillis(5000)  
                .build();  
  
        // 3. 创建连接池  
        try (JedisPool jedisPool = new JedisPool(
            poolConfig, new HostAndPort("127.0.0.1", 6379), jedisClientConfig);
        ) {  
            // 4. 从连接池获取连接  
            try (Jedis jedis = jedisPool.getResource()) {  
                System.out.println("Ping: " + jedis.ping());  
                jedis.set("key", "value");  
                System.out.println("Get key: " + jedis.get("key"));  
            }  
        }  
    }  
}
```

### 使用 `URI` 方式（支持ACL）

Redis 6+ 支持 `ACL`，可以使用 `redis://` 或 `rediss://`（SSL）格式，包含用户名和密码：

```java
import redis.clients.jedis.Jedis;
import redis.clients.jedis.JedisPool;
import redis.clients.jedis.JedisPoolConfig;
import java.net.URI;

public class JedisURIACLExample {
    public static void main(String[] args) {
        // Redis 7 + ACL 的 URI 格式：redis://username:password@host:port
        String uriString = "redis://laodu:laodu123@192.168.48.200:6379"; 

        // 如果启用TLS/SSL的话，以上的uri写法如下：
        //String uriString = "rediss://laodu:laodu123@192.168.48.200:6379"; 
        
        // 单个连接
        try (Jedis jedis = new Jedis(URI.create(uriString))) {
            System.out.println("Ping: " + jedis.ping());
        }

        // -------------------------连接池方式---------------------------------------
        JedisPoolConfig poolConfig = new JedisPoolConfig();
        try (JedisPool jedisPool = new JedisPool(poolConfig, URI.create(uriString))) {
            try (Jedis jedis = jedisPool.getResource()) {
                jedis.set("key", "value");
                System.out.println("Get key: " + jedis.get("key"));
            }
        }
    }
}
```

### TLS/SSL

Redis7并没有默认开启TLS/SSL，开启它之后，密码和数据在网络传输过程中是经过加密的，比较安全。

```java
import redis.clients.jedis.Jedis;
import redis.clients.jedis.JedisClientConfig;
import redis.clients.jedis.DefaultJedisClientConfig;

public class JedisSSLACLExample {
    public static void main(String[] args) {
        String username = "laodu";
        String password = "laodu123";
        
        JedisClientConfig config = DefaultJedisClientConfig.builder()
            .user(username)
            .password(password)
            .ssl(true)  // 启用SSL之后，代码中要添加这一行（如果采用URI的方式，开头协议要写为：rediss://）
            .build();
        
        try (Jedis jedis = new Jedis("192.168.48.200", 6379, config)) {
            System.out.println("Ping: " + jedis.ping());
        }
    }
}
```
