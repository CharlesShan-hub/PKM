# Sentinel（哨兵）

**来源**：《Redis设计与实现》第 16 章；配置部署参考 `d:\project\PKM\pkm\backend\database\redis\notes\cluster.md`

---

## 概述

Redis Sentinel 是 Redis 官方提供的高可用性解决方案，用于监控主从节点并在主节点故障时自动完成故障转移。

## 启动并初始化 Sentinel

1. 初始化服务器（Sentinel 专用配置）
2. 将普通 Redis 服务器替换为 Sentinel 专用代码
3. 初始化 Sentinel 状态
4. 创建连向主服务器的网络连接（命令连接 + 订阅连接）

## 获取主服务器信息

Sentinel 默认每 10 秒向主服务器发送 INFO 命令，获取：
- 主服务器本身的信息
- 主服务器下所有从服务器的信息

## 获取从服务器信息

根据主服务器 INFO 回复中的从服务器列表，Sentinel 为每个从服务器创建实例结构，并创建命令连接。

## 检测下线状态

### 主观下线

- Sentinel 每秒向所有实例发送 PING
- 若 `down-after-milliseconds` 内未收到有效回复 → 标记为主观下线

### 客观下线

- Sentinel 向其他 Sentinel 发送 `SENTINEL is-master-down-by-addr` 命令
- 收到足够数量（quorum）的确认后 → 标记为客观下线

## 选举领头 Sentinel

使用 Raft 算法的简化版本：
1. 每个发现主服务器客观下线的 Sentinel 都可以成为候选人
2. 候选人向其他 Sentinel 发送竞选请求
3. 先到先得：每个配置纪元中，每个 Sentinel 只能投票给一个候选人
4. 获得半数以上投票的 Sentinel 成为领头 Sentinel

## 故障转移

### 1. 选出新主服务器

筛选标准（按优先级）：
1. 删除下线/断线的从服务器
2. 删除最近 5 秒未回复的从服务器
3. 删除断开时间超过 `down-after-milliseconds × 10` 毫秒的从服务器
4. 按优先级排序 → 选最高优先级
5. 若优先级相同 → 选复制偏移量最大的
6. 若仍相同 → 选运行 ID 最小的

### 2. 修改从服务器的复制目标

向所有从服务器发送 `SLAVEOF`，让它们复制新的主服务器。

### 3. 将旧主服务器变为从服务器

旧主服务器重新上线后，Sentinel 向其发送 `SLAVEOF`，使之成为新主服务器的从服务器。

## 配置说明

详细配置步骤参考：`d:\project\PKM\pkm\backend\database\redis\notes\cluster.md`

关键配置：

```
sentinel monitor mymaster 127.0.0.1 6379 2    # 2 = quorum
sentinel down-after-milliseconds mymaster 5000
sentinel failover-timeout mymaster 10000
sentinel parallel-syncs mymaster 1
```

## 三种模式对比

| 模式 | 适用场景 | 优点 | 缺点 |
|------|----------|------|------|
| 主从复制 | 读写分离、数据备份 | 配置简单 | 主节点单点故障 |
| 哨兵模式 | 高可用，自动故障转移 | 自动监控和切换 | 配置较复杂 |
| Redis 集群 | 大数据量、高并发 | 数据分片，横向扩展 | 部署和维护复杂 |
