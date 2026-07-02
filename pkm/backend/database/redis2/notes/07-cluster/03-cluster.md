# 集群（Cluster）

**来源**：《Redis设计与实现》第 17 章；配置部署参考 `d:\project\PKM\pkm\backend\database\redis\notes\cluster.md`

---

## 概述

Redis 集群是 Redis 官方提供的分布式数据库方案，通过分片实现数据自动分布和高可用。

## 节点

- 一个 Redis 集群由多个节点组成
- 通过 `CLUSTER MEET` 命令将节点连接起来
- 每个节点使用 `clusterNode` 结构保存其他节点的信息
- 所有节点使用 `clusterState` 结构保存集群状态

## 槽指派

Redis 集群将整个数据库分为 **16384 个槽**（slot）。

### 数据映射公式

```
slot = CRC16(key) & 16383
```

### 槽的存储

- `clusterNode.slots`：二进制位数组（2048 字节），标记节点负责的槽
- `clusterState.slots`：16384 个指针的数组，指向负责该槽的节点

### 集群上线条件

所有 16384 个槽都有节点负责时，集群进入上线状态。

### CLUSTER ADDSLOTS

```
CLUSTER ADDSLOTS <slot> [slot ...]
```

将指定槽指派给当前节点。

## 在集群中执行命令

### MOVED 错误

当客户端向节点发送命令，但键所属的槽不在该节点时，节点返回 MOVED 错误，指引客户端转向正确的节点：

```
MOVED <slot> <ip>:<port>
```

### 节点对键的检查

1. 计算键所属的槽 `slot = CRC16(key) & 16383`
2. 检查 `clusterState.slots[slot]` 是否指向当前节点
3. 是 → 执行命令；否 → 返回 MOVED 错误

## 重新分片

### 流程

由 redis-trib 负责执行：

1. 向目标节点发送 `CLUSTER SETSLOT <slot> IMPORTING <source_id>`
2. 向源节点发送 `CLUSTER SETSLOT <slot> MIGRATING <target_id>`
3. 获取源节点中属于该槽的键：`CLUSTER GETKEYSINSLOT <slot> <count>`
4. 迁移键：`MIGRATE <target_ip> <target_port> <key> 0 <timeout>`
5. 重复 3-4 直到全部迁移
6. 向集群广播 `CLUSTER SETSLOT <slot> NODE <target_id>`

## ASK 错误

重分片期间使用的临时转向机制：

- 若源节点没找到键 → 检查 `migrating_slots_to[slot]`
- 正迁移中 → 返回 ASK 错误
- 客户端先发送 `ASKING` 命令，再重发原命令

### ASK 与 MOVED 的区别

| 特性 | MOVED | ASK |
|------|-------|-----|
| 性质 | 永久转移 | 临时措施 |
| 客户端行为 | 后续命令直接发往新节点 | 仅下次命令转向，后续仍发往原节点 |
| 触发时机 | 槽已完全转移 | 槽正在迁移 |

## 复制与故障转移

- 集群中的节点可以设置从节点
- 主节点故障时，从节点自动提升为主节点
- 选举过程类似于 Sentinel

## 消息

集群中的节点通过 Gossip 协议通信：

| 消息类型 | 用途 |
|----------|------|
| MEET | 将节点加入集群 |
| PING | 检测节点是否在线 |
| PONG | 回应 PING/MEET |
| FAIL | 节点 A 认为节点 B 已下线 |

## 配置部署

详细配置步骤参考：`d:\project\PKM\pkm\backend\database\redis\notes\cluster.md`
