# 发布与订阅

**来源**：《Redis设计与实现》第 18 章

---

## 概述

Redis 的发布与订阅（Pub/Sub）功能支持消息的发布和订阅模式。

## 频道的订阅与退订

服务器为每个数据库维护一个 `pubsub_channels` 字典：

```c
struct redisServer {
    dict *pubsub_channels;  // 键为频道名，值为订阅该频道的客户端链表
};
```

- **SUBSCRIBE**：将客户端添加到对应频道的链表中
- **UNSUBSCRIBE**：从链表中移除客户端

## 模式的订阅与退订

服务器维护一个 `pubsub_patterns` 链表（保存模式+客户端）：

```c
struct redisServer {
    list *pubsub_patterns;  // 节点包含 subscribed_pattern
};
```

- **PSUBSCRIBE**：添加模式到链表中
- **PUNSUBSCRIBE**：从链表中移除模式

## 发送消息

```
PUBLISH channel message
```

执行步骤：
1. 将消息发送给 `pubsub_channels` 中 channel 频道的所有订阅者
2. 遍历 `pubsub_patterns` 链表，将消息发送给模式能匹配 channel 的所有订阅者

## 查看订阅信息

| 命令 | 说明 |
|------|------|
| `PUBSUB CHANNELS [pattern]` | 列出当前被订阅的频道 |
| `PUBSUB NUMSUB [channel ...]` | 返回频道的订阅者数量 |
| `PUBSUB NUMPAT` | 返回被订阅模式的数量 |
