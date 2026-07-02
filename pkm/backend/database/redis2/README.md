# 笔记重构计划

> 来源书籍：《Redis设计与实现》
> 目标：将底层原理与实战笔记融合，形成"用法+原理"双层次的知识体系

---

## 现状分析

### 已有笔记（`d:\project\PKM\pkm\backend\database\redis\`）

当前笔记来自网课实战视角，覆盖内容：

| 文件 | 内容 | 处理方式 |
|------|------|----------|
| `notes/introduction.md` | Redis简介、NoSQL、单线程模型、I/O多路复用 | 保留，补充版本演变、内存模型 |
| `notes/usage.md` | 基础使用（Docker、命令表）、ACL、TLS/SSL | 拆分为 `data-types.md` + `acl-tls.md` |
| `notes/jedis.md` | 连接池、管道、ACL代码示例 | 保留不动 |
| `notes/structure.md` | SDS简记（仅一段） | 并入数据结构目录，大幅扩展 |
| `notes/rdb.md` | RDB+AOF持久化配置详解 | 拆为 `rdb.md` + `aof.md` |
| `notes/cluster.md` | 主从/哨兵/集群部署配置 | 保留部署部分，补充底层实现机制 |
| `notes/spring.md` | Spring Boot集成、Spring Cache高速缓存 | 保留不动 |
| `notes/patterns.md` | 事务、Pub/Sub、缓存穿透/雪崩/击穿 | 事务/Pub/Sub并入高级功能，问题方案保留 |
| `notes/other.md` | Bitmaps、HyperLogLog、Stream、Geospatial | 并入高级功能目录 |

### 核心缺失（需要从书籍补充的底层知识）

| 领域 | 缺失内容 |
|------|----------|
| 数据结构 | 跳跃表、整数集合、压缩列表、字典渐进式rehash、对象系统（类型编码/内存回收/对象共享） |
| 数据库 | 键空间、过期删除策略（惰性删除+定期删除）、AOF/RDB/复制对过期键的处理、数据库通知 |
| 事件 | 文件事件（epoll机制）、时间事件、事件调度与执行 |
| 客户端/服务器 | 客户端属性、命令执行完整流程、serverCron、服务器初始化 |
| 复制 | 旧版复制缺陷、部分重同步实现、PSYNC命令、心跳检测 |
| 哨兵 | 主观下线/客观下线、选举领头Sentinel、故障转移实现细节 |
| 集群 | 槽指派、MOVED/ASK重定向、重新分片、Gossip消息 |
| 高级功能 | Lua脚本实现、SORT命令实现、BITCOUNT算法、慢查询日志、监视器 |

---

## 新目录结构

```
redis/
├── README.md                            # 目录索引（更新）
├── assets/                              # 图片资源（保留）
├── details/                             # Jedis细节代码（保留）
│
├── 01-basics/                           # 基础入门
│   ├── 01-introduction.md               # 现有introduction.md
│   ├── 02-data-types.md                 # 9种数据类型命令参考
│   └── 03-acl-tls.md                    # ACL + TLS/SSL
│
├── 02-data-structures/                  # 底层数据结构 ★新增核心
│   ├── 01-sds.md                        # SDS（扩展现有笔记）
│   ├── 02-linkedlist.md                 # 链表
│   ├── 03-dict.md                       # 字典 + 渐进式rehash
│   ├── 04-skiplist.md                   # 跳跃表
│   ├── 05-intset.md                     # 整数集合 + 升级机制
│   ├── 06-ziplist.md                    # 压缩列表 + 连锁更新
│   └── 07-object-system.md              # 对象类型编码/内存回收/共享
│
├── 03-jedis/                            # Jedis客户端
│   └── jedis.md                         # 现有jedis.md
│
├── 04-persistence/                      # 持久化
│   ├── 01-rdb.md                        # 现有RDB部分 + RDB文件结构
│   ├── 02-aof.md                        # 现有AOF部分 + AOF重写实现
│   └── 03-expiration.md                 # ★新增 过期键删除策略
│
├── 05-event-system/                     # ★新增 事件系统
│   ├── 01-file-event.md                 # 文件事件
│   ├── 02-time-event.md                 # 时间事件
│   └── 03-event-scheduling.md           # 事件调度
│
├── 06-server/                           # ★新增 服务器与客户端
│   ├── 01-client.md                     # 客户端
│   └── 02-server.md                     # 服务器
│
├── 07-cluster/                          # 集群与高可用
│   ├── 01-replication.md                # 现有内容 + 补充PSYNC/部分重同步
│   ├── 02-sentinel.md                   # 现有内容 + 补充选举/故障转移
│   └── 03-cluster.md                    # 现有内容 + 补充槽/Gossip/重定向
│
├── 08-spring-integration/               # Spring集成
│   └── spring.md                        # 现有spring.md
│
├── 09-advanced-features/                # 高级功能
│   ├── 01-pubsub.md                     # 发布与订阅（补充实现）
│   ├── 02-transaction.md                # 事务（补充WATCH实现）
│   ├── 03-lua-script.md                 # ★新增 Lua脚本
│   ├── 04-sort.md                       # ★新增 SORT命令
│   ├── 05-bitmap.md                     # Bitmaps + BITCOUNT算法
│   ├── 06-hyperloglog.md                # HyperLogLog（保留现有）
│   ├── 07-stream-geo.md                 # Stream + Geospatial
│   ├── 08-slowlog.md                    # ★新增 慢查询日志
│   └── 09-monitor.md                    # ★新增 监视器
│
└── 10-problems-patterns/                # 常见问题与最佳实践
    ├── 01-cache-penetration.md          # 穿透/雪崩/击穿（保留现有）
    └── 02-best-practices.md             # ★新增 最佳实践总结
```

> 标注 **★新增** 的为需要从《Redis设计与实现》书中提炼的新文件

---

## 参考资料

- 底层实现原理：`.claude/skills/redis-internals/resources/Redis设计与实现/`
- 每章末尾的 `*_重点回顾.md` 可作为笔记提纲
- 书籍配套图片：`resources/images/`
