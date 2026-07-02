# 事务

**来源**：《Redis设计与实现》第 19 章

---

## 概述

Redis 通过 `MULTI`、`EXEC`、`DISCARD`、`WATCH` 等命令实现事务功能。

## 事务的实现

### 事务状态

每个客户端状态包含一个 `mstate` 属性记录事务队列：

```c
typedef struct redisClient {
    multiState mstate;  // 事务状态
} redisClient;

typedef struct multiState {
    multiCmd *commands;  // 事务队列（FIFO）
    int count;           // 命令数
} multiState;
```

### 执行流程

1. **MULTI**：开启事务，客户端进入事务状态
2. **命令入队**：后续命令不立即执行，加入事务队列
3. **EXEC**：遍历事务队列，按顺序执行所有命令
4. **DISCARD**：清空事务队列，退出事务状态

## WATCH 命令的实现

WATCH 是一个乐观锁机制，用于在事务执行前监控一个或多个键。

```c
typedef struct redisDb {
    dict *watched_keys;  // 键 → 监视该键的客户端链表
} redisDb;
```

### WATCH 触发条件

- 在事务 EXEC 执行前，如果被 WATCH 的键被修改
- EXEC 会检查键是否被修改过（通过 REDIS_DIRTY_CAS 标志）
- 若被修改，EXEC 返回 nil，拒绝执行事务

### UNWATCH

取消所有 WATCH 监控。

## Redis 事务的 ACID 性质

| ACID | Redis 支持 | 说明 |
|------|-----------|------|
| **原子性** | ⚠️ 有限 | 事务中的所有命令会顺序执行，但 Redis 不支持回滚（即使某条命令失败，后续命令仍会执行） |
| **一致性** | ✅ | 通过类型检查、错误处理保证 |
| **隔离性** | ✅ | 单线程模型天然保证串行化执行 |
| **持久性** | ⚠️ 视持久化配置 | 取决于 RDB/AOF 配置（AOF everysec 可能丢 1 秒数据） |
