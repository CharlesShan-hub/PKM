# 时间事件

**来源**：《Redis设计与实现》第 12 章

---

## 概述

Redis 的时间事件分为两类：
- **定时事件**：在指定时间之后执行一次（Redis 目前未使用）
- **周期性事件**：每隔指定时间执行一次（Redis 主要使用的方式）

## 时间事件的属性

```
id       — 全局唯一 ID（递增）
when     — 毫秒精度的 UNIX 时间戳，记录到达时间
timeProc — 事件处理器函数
```

- 若 timeProc 返回 `AE_NOMORE` → 定时事件（执行一次后删除）
- 若返回非 `AE_NOMORE` 的整数值 → 周期性事件（更新 when 后再次到达）

## 实现

所有时间事件存放在一个 **无序链表** 中（按 ID 逆序排序，不按 when 排序）：

```
Header → [ID=3] → [ID=2] → [ID=1]
```

时间事件执行器每次遍历整个链表，处理所有已到达的事件。

> **为什么无序链表不影响性能？**
> 正常模式下的 Redis 服务器只使用 serverCron 一个时间事件，benchmark 模式下也只使用两个。链表退化成一个指针，遍历性能不受影响。

## serverCron 函数

serverCron 是 Redis 最重要的周期性时间事件，默认 **每秒运行 10 次**（每 100 毫秒一次），从 Redis 2.8 开始可通过 `hz` 选项调整。

### serverCron 的主要工作

| 功能 | 说明 |
|------|------|
| 更新服务器时间缓存 | 更新 unixtime、mstime 属性 |
| 更新 LRU 时钟 | 更新 lruclock（每 10 秒一次） |
| 更新每秒执行命令次数 | 抽样估算 instantaneous_ops_per_sec |
| 更新内存峰值 | 记录 stat_peak_memory |
| 处理 SIGTERM 信号 | 检查 shutdown_asap 标识 |
| 管理客户端资源 | 释放超时连接、清理输入缓冲区 |
| 管理数据库资源 | 删除过期键、收缩字典 |
| 执行延迟的 BGREWRITEAOF | BGSAVE 完成后执行 |
| 检查持久化运行状态 | 检查 rdb_child_pid / aof_child_pid |
| 将 AOF 缓冲区写入文件 | 调用 flushAppendOnlyFile |
| 关闭异步客户端 | 关闭输出缓冲区超限的客户端 |
