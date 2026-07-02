# AOF 持久化

**来源**：《Redis设计与实现》第 11 章；详细配置见 `d:\project\PKM\pkm\backend\database\redis\notes\rdb.md`

---

## 概述

AOF（Append-Only File）持久化以日志形式记录每个写操作，Redis 启动时通过重放 AOF 文件中的所有命令来恢复数据。

## AOF 持久化的实现

### 命令追加

每个写命令执行后，以 RESP 协议格式追加到 AOF 缓冲区（`aof_buf`）。

### 文件写入与同步

由 `appendfsync` 配置控制：

| 配置 | 刷盘时机 | 安全性 | 性能 |
|------|----------|--------|------|
| `always` | 每个命令 | 最安全 | 最慢 |
| `everysec` | 每秒 | 默认推荐 | 折中 |
| `no` | 操作系统决定 | 最不安全 | 最快 |

## AOF 文件的载入与数据还原

1. 创建伪客户端（不联网）
2. 逐条读取 AOF 文件中的命令
3. 伪客户端执行命令，还原数据库状态

## AOF 重写

### 为什么需要重写

AOF 文件会随着写操作增多而膨胀，重写可以：
- 合并多个命令为一个（如 `LPUSH` 多次合并为一次）
- 删除已过期或无效的命令

### AOF 重写的实现

Redis 7.0+ 采用混合持久化：

```
appendonlydir/
├── appendonly.aof.1.base.rdb    # 全量数据快照（RDB 格式）
├── appendonly.aof.1.incr.aof    # 增量写命令（AOF 格式）
└── appendonly.aof.manifest      # 清单文件
```

### 重写流程

1. 创建子进程
2. 子进程将当前内存数据写入新的 base.rdb
3. 父进程继续处理写命令，同时写入旧的 incr.aof 和重写缓冲区
4. 子进程完成后通知父进程
5. 父进程将重写缓冲区的数据写入新的 incr.aof
6. 原子替换 manifest 文件

### 触发条件

```
auto-aof-rewrite-percentage 100   # 文件增长 100%
auto-aof-rewrite-min-size 64mb    # 最小 64MB
```
