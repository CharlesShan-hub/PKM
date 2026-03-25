# Redis 集群与部署

---

## Redis 集群（Redis Cluster）

### 1. 什么是 Redis 集群？

Redis 集群是 Redis 官方提供的分布式数据库方案，用于在多个节点间自动分区数据，支持高可用和横向扩展。

### 2. 集群特点

- **数据分片**：将数据自动分布到多个节点，每个节点保存部分数据。
- **高可用性**：主节点故障时，从节点可自动提升为主节点。
- **无中心结构**：每个节点都保存集群的元数据，节点间通过 Gossip 协议通信。
- **客户端路由**：客户端可直连任意节点，若请求的 key 不在该节点，会返回 MOVED 重定向。

### 3. 集群数据分片方式

Redis 集群采用哈希槽（hash slot）机制，共 16384 个槽位，每个节点负责一部分槽位。  
**数据映射公式**：`slot = CRC16(key) mod 16384`

### 4. 集群节点角色

- **主节点（Master）**：负责处理槽位数据读写。
- **从节点（Slave）**：复制主节点数据，主节点故障时可接替。

### 5. 集群搭建步骤

1. 配置多个 Redis 实例，开启集群模式。
2. 使用 `redis-cli --cluster create` 创建集群。
3. 分配槽位，建立主从关系。

---

## Redis 主从复制（Replication）

### 1. 主从复制概念

* 主从复制是指将一个 Redis 服务器（主节点）的数据复制到其他 Redis 服务器（从节点）的过程，实现数据冗余和读写分离。
* 比如：一个主节点搭配两个子节点的小型集群。主节点拥有写的权限，子节点拷贝主节点的数据，只拥有读的权限。符合实际需求中，读的需求更多，从而分配更多节点。

### 2. 复制流程

1. 从节点启动后，向主节点发送 `PSYNC` 命令请求同步。
2. 主节点执行 BGSAVE 生成 RDB 快照，发送给从节点。
3. 从节点载入 RDB 文件，恢复数据。
4. 主节点将后续的写命令通过缓冲区发送给从节点，保持数据同步。

### 3. 主从复制模式

- **全量同步**：从节点初次连接或复制偏移量不匹配时，执行全量 RDB 同步。
- **部分同步（增量）**：主节点维护复制积压缓冲区，从节点断线重连后可从中获取断线期间的写命令。

### 4. 配置方法

在从节点配置文件中设置：
```
slaveof <masterip> <masterport>
```
或启动后执行命令：
```
SLAVEOF 127.0.0.1 6379
```

具体而言，下边是一个案例，配置6380和6381两个端口的从节点，主节点是默认的6379.

配置从节点1 6380：创建从节点配置文件。将 `/etc/redis.conf` 复制一份生成 `/etc/redis/6380.conf`，然后按照以下配置对`6380.conf`文件进行修改：（一个一个修改。不要一下子粘贴进去）

```nginx
# 端口配置
port 6380
daemonize yes # 这个我们之前修改过
pidfile /var/run/redis_6380.pid
logfile "/var/log/redis/redis_6380.log"
dir /var/lib/redis/6380

# 从节点的主要配置（让当前节点成为192.168.48.200 6379节点的从节点）
replicaof 192.168.48.200 6379
masterauth 123456
masteruser default

# 主从失去联系后，从节点仍然使用旧数据响应客户端
# 默认值就是它，不用修改
replica-serve-stale-data yes 
replica-read-only yes

# 开启AOF
appendonly yes
appendfilename "appendonly_6380.aof"
appenddirname "appendonlydir_6380"
```

创建必要的目录：这个目录和从节点的创建没有关系。

```shell
mkdir -p /var/lib/redis/6380 /var/log/redis
```

启动从节点：

```shell
redis-server /etc/redis/6380.conf
```

登录从节点1客户端：

```shell
redis-cli -p 6380
```

验证主从复制：从主节点上和从节点上执行以下命令查看主从关系

```shell
info replication
```

配置从节点2 6381：创建从节点配置文件。将 `/etc/redis.conf` 复制一份生成 `/etc/redis/6381.conf`，然后按照以下配置对`6381.conf`文件进行修改

```nginx
# 端口配置
port 6381
daemonize yes
pidfile /var/run/redis_6381.pid
logfile "/var/log/redis/redis_6381.log"
dir /var/lib/redis/6381

# 从节点的主要配置
replicaof 192.168.48.200 6379
masterauth 123456
masteruser default
# 主从失去联系后，从节点仍然使用旧数据响应客户端
replica-serve-stale-data yes 
replica-read-only yes

# 开启AOF
appendonly yes
appendfilename "appendonly_6381.aof"
appenddirname "appendonlydir_6381"
```

创建必要的目录：这个目录和从节点的创建没有关系。

```shell
mkdir -p /var/lib/redis/6381 /var/log/redis
```

启动从节点：

```shell
redis-server /etc/redis/6381.conf
```

登录从节点2客户端：

```shell
redis-cli -p 6381
```

验证主从复制：从主节点上和从节点上执行以下命令查看主从关系

```shell
info replication
```

如果要取消复制（从节点恢复为独立节点）

```bash
replicaof no one
```

---

## Redis 哨兵模式（Sentinel）

### 1. 哨兵模式概述

Redis Sentinel 是 Redis 官方提供的高可用性解决方案，用于监控主从节点，并在主节点故障时自动完成故障转移。（主节点宕机后，从节点自动提升为主节点）

### 2. 哨兵功能

- **监控**：定期检查主从节点是否正常运行。
- **通知**：通过 API 向管理员报告故障。
- **自动故障转移**：主节点不可用时，哨兵会选举一个从节点升级为主节点，并更新配置。
- **配置提供者**：客户端可连接哨兵获取当前主节点地址。

### 3. 哨兵集群

哨兵本身也可以部署为多个节点，通过投票机制决定是否进行故障转移，避免单点问题。

### 4. 哨兵配置示例

创建哨兵配置文件 `sentinel.conf`：
```
sentinel monitor mymaster 127.0.0.1 6379 2
sentinel down-after-milliseconds mymaster 5000
sentinel failover-timeout mymaster 10000
```
启动哨兵：
```
redis-sentinel sentinel.conf
```

下边是具体实现方案

准备Redis主从配置
我们现在已经配置了一主两从：

+ 主节点：192.168.48.200:6379
+ 从节点1：192.168.48.200:6380
+ 从节点2：192.168.48.200:6381

创建哨兵配置文件
为每个哨兵实例创建配置文件，通常建议至少3个哨兵实例：

哨兵1配置文件，将 `redis源码中的sentinel.conf` 复制一份生成 `/etc/redis/sentinel_26379.conf`，然后按照以下配置对`sentinel_26379.conf`文件进行修改：

```plain
port 26379
bind 0.0.0.0  # 这个是新增的配置
protected-mode no # 这个不需要修改
daemonize yes # 如果需要后台运行修改为yes
logfile "/var/log/redis/sentinel1.log"  # 需要修改
pidfile "/var/run/redis/sentinel_26379.pid" # 需要修改

# 主节点监控配置
sentinel monitor mymaster 192.168.48.200 6379 2 # 这一行不用配置，默认就有
sentinel auth-user mymaster default
sentinel auth-pass mymaster 123456

# 故障检测和转移配置
sentinel down-after-milliseconds mymaster 5000  # 修改为5000
sentinel failover-timeout mymaster 10000 # 修改为10000
sentinel parallel-syncs mymaster 1  # 不需要修改
```

哨兵2配置文件，将 `redis源码中的sentinel.conf` 复制一份生成 `/etc/redis/sentinel_26380.conf`，然后按照以下配置对`sentinel_26380.conf`文件进行修改：

```plain
port 26380
bind 0.0.0.0
protected-mode no
daemonize yes
logfile "/var/log/redis/sentinel2.log"
pidfile "/var/run/redis/sentinel_26380.pid"

# 主节点监控配置
sentinel monitor mymaster 192.168.48.200 6379 2 # 这一行不用配置，默认就有
sentinel auth-user mymaster default
sentinel auth-pass mymaster 123456

# 故障检测和转移配置
sentinel down-after-milliseconds mymaster 5000
sentinel failover-timeout mymaster 10000
sentinel parallel-syncs mymaster 1
```

哨兵3配置文件，将 `redis源码中的sentinel.conf` 复制一份生成 `/etc/redis/sentinel_26381.conf`，然后按照以下配置对`sentinel_26381.conf`文件进行修改：

```plain
port 26381
bind 0.0.0.0
protected-mode no
daemonize yes
logfile "/var/log/redis/sentinel3.log"
pidfile "/var/run/redis/sentinel_26381.pid"

# 主节点监控配置
sentinel monitor mymaster 192.168.48.200 6379 2  # 这一行不用配置，默认就有
sentinel auth-user mymaster default
sentinel auth-pass mymaster 123456

# 故障检测和转移配置
sentinel down-after-milliseconds mymaster 5000
sentinel failover-timeout mymaster 10000
sentinel parallel-syncs mymaster 1
```

配置参数说明
+ `port`：哨兵监听的端口
+ `sentinel monitor <master-name> <ip> <port> <quorum>`：
    - `mymaster`：主服务器名称
    - `ip`和`port`：主服务器地址
    - `quorum`：确认主服务器不可达所需的哨兵数量，如果是2表示至少有两个哨兵认为主服务器挂了，哨兵们才会认为主服务器挂了，然后开始商量换一个新主机。
+ `sentinel down-after-milliseconds`：主服务器无响应多少毫秒后认为其下线
+ `sentinel failover-timeout`：故障转移超时时间
+ `sentinel parallel-syncs`：故障转移后同时进行同步的从服务器数量
+ `daemonize`：以守护进程方式运行
+ `logfile`：日志文件路径

启动哨兵服务
```bash
# 创建日志目录
sudo mkdir -p /var/log/redis

# 启动哨兵
redis-server /etc/redis/sentinel_26379.conf --sentinel
redis-server /etc/redis/sentinel_26380.conf --sentinel
redis-server /etc/redis/sentinel_26381.conf --sentinel
```

验证哨兵状态
```bash
# 连接任意哨兵实例
redis-cli -p 26379

sentinel master mymaster  # 查看被监控的主节点详细信息
sentinel slaves mymaster  # 查看该主节点下所有从节点的信息列表
sentinel sentinels mymaster # 查看监控同一主节点的其他哨兵实例信息
```

测试故障转移
1. 手动停止主Redis服务(6379)
2. 等待约5秒(down-after-milliseconds设置的时间)
3. 哨兵将选举新的主服务器
4. 检查新的主从关系

注意事项
1. 确保哨兵实例之间的时间同步(使用NTP)
2. 生产环境建议将哨兵部署在不同的物理机器上
3. 哨兵配置会自动更新，不要手动修改哨兵运行时生成的配置文件
4. 生产环境集群标准配置：1 主 2 从 3 哨兵。

---

## 三种模式对比

| 模式 | 适用场景 | 优点 | 缺点 |
|------|----------|------|------|
| 主从复制 | 读写分离、数据备份 | 配置简单，数据冗余 | 主节点单点故障 |
| 哨兵模式 | 高可用，自动故障转移 | 自动监控和切换 | 配置较复杂，需多个哨兵实例 |
| Redis 集群 | 大数据量、高并发、分布式 | 数据分片，支持横向扩展 | 部署和维护复杂，客户端需支持集群协议 |
