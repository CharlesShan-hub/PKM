# Redis 基础入门

## NoSQL

1. 数据库 = 关系型数据库 + 非关系型数据库（NoSQL）
2. NoSQL 可译为 Not Only SQL（不仅仅是 SQL）或 No SQL（非 SQL 的数据库），是相对于传统关系型数据库而言有很大差异的一类数据库
3. NoSQL 分类：
   - **键值型数据库**：Redis（缓存型）、RocksDB（持久型）、Memcached（已逐渐被 Redis 取代）
   - **文档数据库**：MongoDB，一个 JSON 就是一个文档
   - **列数据库**：Cassandra、HBase，以列为单位存储，适合大数据方向
   - **图数据库**：Neo4j，采用节点和边结构，适用于社交网络、欺诈检测、推荐系统、知识图谱
4. NoSQL 特点：弱化 ACID（支持高吞吐），更适合做水平扩展（关系型更适合垂直扩展）

## Redis 简介

- Redis（REmote DIctionary Server）由 Salvatore Sanfilippo（antirez）开发的开源内存数据库，2009 年发布
- 底层主要用 **C 语言**编写，以高性能和低延迟著称
- 广泛应用于缓存、消息队列、会话存储等场景

### 应用场景

1. **缓存**（最常用）
2. **会话存储**（Session Storage）— 如 Nginx 负载均衡时将会话存到 Redis
3. **分布式锁**（Distributed Lock）— 防止重复提交、秒杀库存扣减
4. **排行榜** — 利用 ZSet 的有序特性
5. **计数器** — 利用 INCR/DECR 原子操作

### Redis 核心特性

- key-value 存储：key 永远是字符串，value 支持多种类型
- **单线程核心模型**：数据读写、命令执行是单线程的，避免多线程竞争和锁开销
- 6.0 版本开始引入有限的多线程支持（仅用于辅助 I/O）
- 支持持久化（RDB + AOF）
- 支持集群（主从复制、哨兵、Cluster）
- **I/O 多路复用**：通过 epoll 机制 + 非阻塞 Socket 实现单线程高并发

### 单线程为什么还快？

1. 数据在 **内存** 中，操作速度极快
2. **I/O 多路复用**（epoll）处理大量网络连接
3. 无上下文切换和锁竞争，CPU 缓存利用率高

## Redis 版本演变

| 版本 | 主要特性 |
|------|----------|
| 2.6 | Lua 脚本支持 |
| 2.8 | Sentinel 初始版本、PSYNC 命令 |
| 3.0 | Redis Cluster 正式发布 |
| 3.2 | GEO 地理位置功能 |
| 4.0 | 模块系统、混合持久化 |
| 5.0 | Stream 数据类型、动态调整哈希槽 |
| 6.0 | **ACL 访问控制**、多线程 I/O、RESP3 协议 |
| 7.0 | AOF 多文件分段存储、Function、Sharded Pub/Sub |
| 7.2 | 自动故障改进、新的管理命令 |
| 7.4 | 性能优化、安全增强 |
