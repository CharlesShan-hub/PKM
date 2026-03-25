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
    * Jedis 基础连接
    * 常用命令（Key、String、List、Hash、Set、ZSet）
    * 密码设置与端口放行
    * Redis ACL 访问控制（6.0+）
    * TLS/SSL 加密传输（7.0+）
* [Jedis客户端](notes/jedis.md)
    * 连接池配置与使用
    * 管道（Pipeline）批量操作
    * Redis ACL与TLS/SSL的方式
* [数据持久化](notes/rdb.md)
    * RDB
    * AOF
* [Spring集成](notes/spring.md)
    * springboot集成redis
    * springcache高速缓存
    * springdata支持事务
* [集群与部署](notes/cluster.md)
    * Redis 集群（Cluster）
    * 主从复制（Replication）
    * 哨兵模式（Sentinel）
* [应用模式与问题](notes/patterns.md)
    * 事务（MULTI/EXEC/WATCH）
    * 发布订阅（Pub/Sub）
    * 缓存穿透及解决方案
    * 缓存雪崩及解决方案
    * 缓存击穿及解决方案
* [Redis其他数据类型](notes/other.md)
    * Bitmaps（位图）
    * HyperLogLog
    * Stream 流
    * Geospatial
