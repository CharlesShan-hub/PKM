# 最佳实践总结

---

## 内存优化

1. **使用合适的数据结构**：小数据量用 ziplist/intset 编码，大数据量用 hashtable/skiplist
2. **设置过期时间**：临时数据必须设置 TTL
3. **禁用大 Key**：超过 10KB 的 String 或超过 1000 个元素的集合要及时拆分
4. **合理设置 maxmemory**：并配置合适的淘汰策略

## 性能优化

1. **避免慢查询**：慎用 `KEYS`、`SMEMBERS` 等命令，用 `SCAN`、`SSCAN` 代替
2. **使用 Pipeline**：批量操作时用 Pipeline 减少 RTT
3. **连接池**：生产环境必须使用连接池，合理设置池大小
   - `maxTotal ≈ QPS × avg_query_time(ms) / 1000`
4. **调整 hz 配置**：高并发场景可适当提高 hz（默认 10）
5. **I/O 多线程**：Redis 6.0+ 可配置 `io-threads` 提升网络 I/O

## 数据安全

1. **开启 RDB + AOF**：同时启用两种持久化方式
2. **AOF 配置**：
   - `appendfsync everysec`（默认推荐）
   - 设置 `auto-aof-rewrite-percentage` 和 `auto-aof-rewrite-min-size`
3. **主从复制**：至少配置一个从节点
4. **密码保护**：
   - 使用复杂密码
   - ACL 精细化权限控制
   - 限制 IP 绑定（`bind`）

## 高可用部署

| 规模 | 推荐方案 |
|------|----------|
| 小（单机） | 主从 + Sentinel（1 主 2 从 3 哨兵） |
| 中（数据量大） | Redis Cluster（至少 3 主 3 从） |
| 大（跨机房） | Cluster + 跨机房部署 |

## 缓存一致性

改数据操作口诀：

> **先改数据库，再删 Redis**（而非更新 Redis）

为什么删而不是更新？
- 删除操作是幂等的
- 避免并发读写带来的数据不一致

## 监控与报警

1. **监控指标**：
   - 内存使用率（used_memory）
   - 命中率（keyspace_hits / keyspace_misses）
   - 慢查询数量（SLOWLOG）
   - 连接数（connected_clients）
   - 复制延迟（master_repl_offset - slave_repl_offset）
2. **设置合理阈值**，配置报警
