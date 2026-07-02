# 数据类型与常用命令

> 参考用法笔记：`d:\project\PKM\pkm\backend\database\redis\notes\usage.md`

Redis 共有 9 种数据类型，以下是前 5 种核心类型及命令参考。

---

## String（字符串）

| 命令 | 说明 |
|------|------|
| `SET key value` | 设置指定 key 的值 |
| `GET key` | 获取指定 key 的值 |
| `GETSET key value` | 设置 key 的值，返回旧值 |
| `MSET key value [key value ...]` | 同时设置多个 key-value |
| `MGET key [key ...]` | 获取所有给定 key 的值 |
| `INCR key` | 将 key 中储存的数字值增一 |
| `DECR key` | 将 key 中储存的数字值减一 |
| `INCRBY key increment` | 将 key 所储存的值加上给定的增量值 |
| `APPEND key value` | 将 value 追加到 key 原来的值的末尾 |
| `STRLEN key` | 返回 key 所储存的字符串值的长度 |

## List（列表）

| 命令 | 说明 |
|------|------|
| `LPUSH key value [value ...]` | 将一个或多个值插入到列表头部 |
| `RPUSH key value [value ...]` | 在列表尾部添加一个或多个值 |
| `LPOP key` | 移除并返回列表的第一个元素 |
| `RPOP key` | 移除并返回列表的最后一个元素 |
| `LRANGE key start stop` | 返回列表中指定区间内的元素（0 -1 表示全部） |
| `LLEN key` | 获取列表长度 |
| `LINDEX key index` | 通过索引获取列表中的元素 |
| `LREM key count value` | 根据 count 的值，移除列表中与 value 相等的元素 |

## Hash（哈希）

| 命令 | 说明 |
|------|------|
| `HSET key field value` | 将哈希表 key 中字段 field 的值设为 value |
| `HGET key field` | 获取哈希表中指定字段的值 |
| `HGETALL key` | 获取哈希表中指定 key 的所有字段和值 |
| `HDEL key field [field ...]` | 删除一个或多个哈希表字段 |
| `HEXISTS key field` | 查看哈希表 key 中指定字段是否存在 |
| `HKEYS key` | 获取哈希表中的所有字段名 |
| `HVALS key` | 获取哈希表中的所有值 |
| `HINCRBY key field increment` | 为哈希表 key 中指定字段的整数值加上增量 |

## Set（集合）

| 命令 | 说明 |
|------|------|
| `SADD key member [member ...]` | 向集合添加一个或多个成员 |
| `SREM key member [member ...]` | 移除集合中一个或多个成员 |
| `SMEMBERS key` | 返回集合中的所有成员 |
| `SISMEMBER key member` | 判断 member 是否是集合 key 的成员 |
| `SCARD key` | 获取集合的成员数 |
| `SINTER key [key ...]` | 返回给定所有集合的交集 |
| `SUNION key [key ...]` | 返回给定所有集合的并集 |
| `SDIFF key [key ...]` | 返回给定所有集合的差集 |

## ZSet（有序集合）

| 命令 | 说明 |
|------|------|
| `ZADD key score member [score member ...]` | 向有序集合添加成员，或更新已存在成员的分数 |
| `ZRANGE key start stop [WITHSCORES]` | 按索引区间返回成员（分数从低到高） |
| `ZREVRANGE key start stop [WITHSCORES]` | 返回成员（分数从高到低） |
| `ZREM key member [member ...]` | 移除有序集合中的一个或多个成员 |
| `ZCARD key` | 获取有序集合的成员数 |
| `ZCOUNT key min max` | 计算指定分数区间内的成员数 |
| `ZRANK key member` | 返回指定成员的排名（从小到大） |
| `ZREVRANK key member` | 返回指定成员的排名（从大到小） |
| `ZINCRBY key increment member` | 对指定成员的分数加上增量 increment |

## 其他 4 种类型

详见 `09-advanced-features/`：
- **Bitmaps** — 位图，String 的特殊用法
- **HyperLogLog** — 基数估算
- **Geospatial** — 地理位置，基于 ZSet 实现
- **Stream** — 消息队列
