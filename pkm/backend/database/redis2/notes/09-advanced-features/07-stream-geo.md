# Stream 与 Geospatial

> 详细内容参见：`d:\project\PKM\pkm\backend\database\redis\notes\other.md`

## Stream（流）

Redis 5.0 引入的消息队列数据类型。

### 核心命令

| 命令 | 说明 |
|------|------|
| `XADD key ID field value [field value ...]` | 添加消息 |
| `XRANGE key start end` | 获取消息范围 |
| `XREAD [COUNT count] [BLOCK ms] STREAMS key [key ...] ID [ID ...]` | 读取消息 |
| `XGROUP CREATE key groupname ID` | 创建消费者组 |
| `XREADGROUP GROUP group consumer` | 消费者组读取 |

### 特性

- 支持持久化
- 支持消费者组
- 支持阻塞读取

## Geospatial（地理位置）

底层基于 ZSet 实现。

### 核心命令

| 命令 | 说明 |
|------|------|
| `GEOADD key lon lat member [lon lat member ...]` | 添加地理位置 |
| `GEOPOS key member [member ...]` | 获取位置坐标 |
| `GEODIST key member1 member2 [unit]` | 计算两地距离 |
| `GEORADIUS key lon lat radius unit` | 查找指定半径内的元素 |
