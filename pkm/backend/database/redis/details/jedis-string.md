# Jedis 操作 String

```java
try (Jedis jedis = new Jedis("localhost", 6379)) {
    jedis.auth("yourpassword");

    // 设置键值
    jedis.set("name", "Alice");
    jedis.setex("tempKey", 60, "临时数据"); // 60秒后过期

    // 获取值
    String name = jedis.get("name");
    System.out.println(name); // Alice

    // 自增
    jedis.set("counter", "10");
    jedis.incr("counter");
    System.out.println(jedis.get("counter")); // 11
}
```
