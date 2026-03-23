# Jedis 连接 Redis

```java
import redis.clients.jedis.Jedis;
import redis.clients.jedis.JedisPool;
import redis.clients.jedis.JedisPoolConfig;

public class JedisConnectionExample {
    public static void main(String[] args) {
        // 方式1：直连
        try (Jedis jedis = new Jedis("localhost", 6379)) {
            jedis.auth("yourpassword"); // 如果有密码
            System.out.println("连接成功：" + jedis.ping());
        }

        // 方式2：连接池（推荐）
        JedisPoolConfig config = new JedisPoolConfig();
        config.setMaxTotal(10);
        try (JedisPool jedisPool = new JedisPool(config, "localhost", 6379, 2000, "yourpassword");
             Jedis jedis = jedisPool.getResource()) {
            System.out.println("连接池示例：" + jedis.ping());
        }
    }
}
```
