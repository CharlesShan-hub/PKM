# Jedis 操作 Hash

```java
try (Jedis jedis = new Jedis("localhost", 6379)) {
    jedis.auth("yourpassword");

    String hashKey = "user:1001";

    // 设置字段值
    jedis.hset(hashKey, "name", "张三");
    jedis.hset(hashKey, "age", "25");

    // 获取单个字段
    String name = jedis.hget(hashKey, "name");
    System.out.println(name); // 张三

    // 获取所有字段和值
    Map<String, String> user = jedis.hgetAll(hashKey);
    System.out.println(user); // {name=张三, age=25}

    // 自增字段
    jedis.hincrBy(hashKey, "age", 1);
    System.out.println(jedis.hget(hashKey, "age")); // 26
}
```
