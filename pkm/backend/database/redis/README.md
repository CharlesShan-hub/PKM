# Redis

> 来源：<https://www.yuque.com/dujubin/java/uh9181pya4bfxwty?singleDoc#%20%E3%80%8ARedis%E3%80%8B>

---

## 笔记目录

* [基础背景](notes/introduction.md)
    * Redis 简介与特性
    * 数据类型概述
    * 应用场景

* [基本使用](notes/usage.md)
    * Docker 操作 Redis
    * 数据库操作（select、flushdb、flushall）
    * 密码设置与端口放行
    * Jedis 基础连接
    * 常用命令（Key、String、List、Hash、Set、ZSet）

* [Jedis 进阶](notes/jedis-advanced.md)
    * 连接池配置与使用
    * 管道（Pipeline）批量操作
    * 性能优化建议

* [集群与部署](notes/cluster.md)
    * Redis 集群（Cluster）原理与搭建
    * 主从复制（Replication）
    * 哨兵模式（Sentinel）
    * 三种模式对比

* [应用模式与问题](notes/patterns.md)
    * 事务（MULTI/EXEC/WATCH）
    * 发布订阅（Pub/Sub）
    * 缓存穿透及解决方案
    * 缓存雪崩及解决方案
    * 缓存击穿及解决方案

