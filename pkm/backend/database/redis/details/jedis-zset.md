# Jedis 操作 ZSet

```java
try (Jedis jedis = new Jedis("localhost", 6379)) {
    jedis.auth("yourpassword");

    String zsetKey = "rank";

    // 添加成员和分数
    jedis.zadd(zsetKey, 90, "Alice");
    jedis.zadd(zsetKey, 85, "Bob");
    jedis.zadd(zsetKey, 95, "Charlie");

    // 按分数升序获取
    Set<String> ascMembers = jedis.zrange(zsetKey, 0, -1);
    System.out.println("升序排名: " + ascMembers);

    // 按分数降序获取
    Set<String> descMembers = jedis.zrevrange(zsetKey, 0, -1);
    System.out.println("降序排名: " + descMembers);

    // 获取分数
    Double score = jedis.zscore(zsetKey, "Alice");
    System.out.println("Alice分数: " + score);

    // 按分数范围获取
    Set<String> range = jedis.zrangeByScore(zsetKey, 85, 93);
    System.out.println("85~93分的成员: " + range);
}
```
