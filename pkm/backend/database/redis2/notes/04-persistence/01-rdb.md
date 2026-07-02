# RDB 持久化

**来源**：《Redis设计与实现》第 10 章；详细配置见 `d:\project\PKM\pkm\backend\database\redis\notes\rdb.md`

---

## 概述

RDB（Redis DataBase）持久化通过创建内存数据集的 **快照** 来实现持久化，以二进制格式存储。

## RDB 文件的创建与载入

| 命令 | 方式 | 说明 |
|------|------|------|
| `SAVE` | 同步 | 阻塞服务器直到 RDB 文件创建完毕 |
| `BGSAVE` | 异步 | 创建子进程处理，不阻塞服务器 |

### 自动间隔性保存

通过 `save` 配置：

```
save 900 1       # 900 秒内至少 1 次写操作
save 300 10      # 300 秒内至少 10 次写操作
save 60 10000    # 60 秒内至少 10000 次写操作
```

触发逻辑：
1. 从第一次写操作开始计时并计数
2. serverCron 每 100ms 检查一次
3. 条件满足时执行 BGSAVE
4. 进入下一个计时周期（不等 BGSAVE 结束）

### 写时复制（COW）

BGSAVE 创建子进程后，父子进程共享内存。主进程修改数据时，操作系统复制被修改的内存页，保证子进程读到的是快照时刻的数据。

## RDB 文件结构

RDB 文件是一个经过压缩的二进制文件，结构如下：

```
REDIS + db_version + databases + EOF + check_sum
```

- `REDIS`：5 字节魔数
- `db_version`：4 字节版本号
- `databases`：零个或多个数据库的数据
- `EOF`：1 字节结束标记
- `check_sum`：8 字节校验和

## 文件分析

使用 `redis-check-rdb` 工具可分析 RDB 文件内容。

## 详细配置

配置项（`redis.conf` 中 `SNAPSHOTTING` 部分）详见 `d:\project\PKM\pkm\backend\database\redis\notes\rdb.md`，包括：

- save、dbfilename、dir
- rdbcompression、rdbchecksum
- stop-writes-on-bgsave-error
