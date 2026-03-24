# 使用
---

## 基础使用

* 进入docker的redis的指令：`docker exec -it iia-redis redis-cli`
* 进入这个容器的linux：`docker exec -it iia-redis /bin/sh`
* Redis默认数据库数量是16个，分别为0-15。但是在集群模式下仅有0号一个数据库，所以建议默认只是用0号库。
* 可以使用`select 0`来使用0号数据库.
* 查看当前数据库中key的数量：**dbsize**
* 清空数据库
    * 清空当前数据库：**flushdb**
    * 清空当前Redis实例中所有的数据库：**flushall**
    * 这两个命令会立即删除数据，且不可恢复（除非有备份），**生产环境务必备份数据或限制命令权限！**
* 关闭数据库使用`redis-cli shutdown`，不要去kill进程，使用指令可以进行数据持久化
* 如何修改密码
    * 配置文件方式：编辑 `redis.conf`，添加 `requirepass yourpassword`，重启生效
    * 临时设置：`CONFIG SET requirepass "yourpassword"`（重启失效）
    * 客户端连接：`redis-cli -a yourpassword` 或连接后执行 `AUTH yourpassword`；这样不安全，也可以进入客户端后输入`auth yourpassword`
* 端口放行
    * firewalld: `firewall-cmd --permanent --add-port=6379/tcp && firewall-cmd --reload`
    * iptables: `iptables -A INPUT -p tcp --dport 6379 -j ACCEPT`
    * 云服务器：安全组添加入站规则允许 TCP 6379
    * 安全加固：配置 `bind 127.0.0.1 192.168.x.x` 限制访问IP；使用 `rename-command` 禁用 FLUSHALL/CONFIG 等危险命令


---

## 常用命令与Jedis

### Jedis连接

添加依赖（pom.xml）
```xml
<dependency>
    <groupId>redis.clients</groupId>
    <artifactId>jedis</artifactId>
    <version>4.4.0</version>
</dependency>
```

创建连接
```java
Jedis jedis = new Jedis("localhost", 6379);
// jedis.auth("password");  // 如有密码
jedis.ping();  // 测试连接，返回 "PONG"
jedis.set("key", "value");
String value = jedis.get("key");
jedis.close();  // 用完关闭
```

### Key 相关命令

| 命令 | 说明 |
| --- | --- |
| `DEL key [key ...]` | 删除给定的一个或多个 key |
| `EXISTS key` | 检查 key 是否存在 |
| `EXPIRE key seconds` | 为 key 设置过期时间（秒） |
| `TTL key` | 查看 key 剩余的生存时间（秒），-1 表示永不过期，-2 表示 key 不存在 |
| `KEYS pattern` | 查找所有符合给定模式 pattern 的 key（生产环境慎用） |
| `RENAME key newkey` | 将 key 改名为 newkey |
| `TYPE key` | 返回 key 所存储的值的类型 |

### String 类型常用命令

| 命令 | 说明 |
| --- | --- |
| `SET key value` | 设置指定 key 的值 |
| `GET key` | 获取指定 key 的值 |
| `GETSET key value` | 设置 key 的值，并返回 key 的旧值 |
| `MSET key value [key value ...]` | 同时设置多个 key-value |
| `MGET key [key ...]` | 获取所有给定 key 的值 |
| `INCR key` | 将 key 中储存的数字值增一 |
| `DECR key` | 将 key 中储存的数字值减一 |
| `INCRBY key increment` | 将 key 所储存的值加上给定的增量值 |
| `APPEND key value` | 将 value 追加到 key 原来的值的末尾 |

[jedis实现String相关命令](../details/jedis-string.md)

### List 类型常用命令

| 命令 | 说明 |
| --- | --- |
| `LPUSH key value [value ...]` | 将一个或多个值插入到列表头部 |
| `RPUSH key value [value ...]` | 在列表尾部添加一个或多个值 |
| `LPOP key` | 移除并返回列表的第一个元素 |
| `RPOP key` | 移除并返回列表的最后一个元素 |
| `LRANGE key start stop` | 返回列表中指定区间内的元素（0 -1 表示全部） |
| `LLEN key` | 获取列表长度 |
| `LINDEX key index` | 通过索引获取列表中的元素 |
| `LREM key count value` | 根据 count 的值，移除列表中与 value 相等的元素 |

[jedis实现List相关命令](../details/jedis-list.md)

### Hash 类型常用命令

| 命令 | 说明 |
| --- | --- |
| `HSET key field value` | 将哈希表 key 中字段 field 的值设为 value |
| `HGET key field` | 获取哈希表中指定字段的值 |
| `HGETALL key` | 获取哈希表中指定 key 的所有字段和值 |
| `HDEL key field [field ...]` | 删除一个或多个哈希表字段 |
| `HEXISTS key field` | 查看哈希表 key 中指定字段是否存在 |
| `HKEYS key` | 获取哈希表中的所有字段名 |
| `HVALS key` | 获取哈希表中的所有值 |
| `HINCRBY key field increment` | 为哈希表 key 中指定字段的整数值加上增量 |

[jedis实现Hash相关命令](../details/jedis-hash.md)

### Set 类型常用命令

| 命令 | 说明 |
| --- | --- |
| `SADD key member [member ...]` | 向集合添加一个或多个成员 |
| `SREM key member [member ...]` | 移除集合中一个或多个成员 |
| `SMEMBERS key` | 返回集合中的所有成员 |
| `SISMEMBER key member` | 判断 member 是否是集合 key 的成员 |
| `SCARD key` | 获取集合的成员数 |
| `SINTER key [key ...]` | 返回给定所有集合的交集 |
| `SUNION key [key ...]` | 返回给定所有集合的并集 |
| `SDIFF key [key ...]` | 返回给定所有集合的差集 |

[jedis实现Set相关命令](../details/jedis-set.md)

### ZSet 类型常用命令

| 命令 | 说明 |
| --- | --- |
| `ZADD key score member [score member ...]` | 向有序集合添加一个或多个成员，或更新已存在成员的分数 |
| `ZRANGE key start stop [WITHSCORES]` | 按索引区间返回有序集合指定区间内的成员（分数从低到高） |
| `ZREVRANGE key start stop [WITHSCORES]` | 返回有序集合指定区间内的成员（分数从高到低） |
| `ZREM key member [member ...]` | 移除有序集合中的一个或多个成员 |
| `ZCARD key` | 获取有序集合的成员数 |
| `ZCOUNT key min max` | 计算有序集合中指定分数区间内的成员数 |
| `ZRANK key member` | 返回有序集合中指定成员的排名（从小到大，从 0 开始） |
| `ZREVRANK key member` | 返回有序集合中指定成员的排名（从大到小，从 0 开始） |
| `ZINCRBY key increment member` | 对有序集合中指定成员的分数加上增量 increment |

[jedis实现ZSet相关命令](../details/jedis-zset.md)

