# Jedis 操作 List

```java
try (Jedis jedis = new Jedis("localhost", 6379)) {
    jedis.auth("yourpassword");

    String listKey = "mylist";

    // 从左侧插入
    jedis.lpush(listKey, "value1", "value2");
    // 从右侧插入
    jedis.rpush(listKey, "value3");

    // 获取列表长度
    Long len = jedis.llen(listKey);
    System.out.println("列表长度: " + len);

    // 获取所有元素
    List<String> all = jedis.lrange(listKey, 0, -1);
    System.out.println(all); // [value2, value1, value3]

    // 弹出左侧第一个元素
    String leftPop = jedis.lpop(listKey);
    System.out.println("左侧弹出: " + leftPop);
}
```
