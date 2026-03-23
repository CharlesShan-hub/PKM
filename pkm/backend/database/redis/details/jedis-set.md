# Jedis 操作 Set

```java
try (Jedis jedis = new Jedis("localhost", 6379)) {
    jedis.auth("yourpassword");

    String setKey = "tags";

    // 添加元素
    jedis.sadd(setKey, "java", "redis", "python");

    // 获取所有成员
    Set<String> members = jedis.smembers(setKey);
    System.out.println(members);

    // 判断是否是成员
    boolean exists = jedis.sismember(setKey, "java");
    System.out.println("是否存在java: " + exists);

    // 移除元素
    jedis.srem(setKey, "python");
}
```
