# 使用
---

## 基础使用

### 运行redis

* 进入docker的redis的指令：`docker exec -it iia-redis redis-cli`
* 进入这个容器的linux：`docker exec -it iia-redis /bin/sh`
* Redis默认数据库数量是16个，分别为0-15。但是在集群模式下仅有0号一个数据库，所以建议默认只是用0号库。
* 可以使用`select 0`来使用0号数据库.
* 查看当前数据库中key的数量：**dbsize**
* 清空数据库
    * 清空当前数据库：**flushdb**
    * 清空当前Redis实例中所有的数据库：**flushall**
    * 这两个命令会立即删除数据，且不可恢复（除非有备份），**生产环境务必备份数据或限制命令权限！**
* 关闭数据库使用`redis-cli shutdown`，不要去kill进程，使用指令可以进行数据持久化

### 设置密码

* 如何修改密码
    * 配置文件方式：编辑 `redis.conf`，添加 `requirepass yourpassword`，重启生效
    * 临时设置：`CONFIG SET requirepass "yourpassword"`（重启失效）
    * 客户端连接：`redis-cli -a yourpassword` 或连接后执行 `AUTH yourpassword`；这样不安全，也可以进入客户端后输入`auth yourpassword`
* 端口放行
    * firewalld: `firewall-cmd --permanent --add-port=6379/tcp && firewall-cmd --reload`
    * iptables: `iptables -A INPUT -p tcp --dport 6379 -j ACCEPT`
    * 云服务器：安全组添加入站规则允许 TCP 6379
    * 安全加固：配置 `bind 127.0.0.1 192.168.x.x` 限制访问IP；使用 `rename-command` 禁用 FLUSHALL/CONFIG 等危险命令

---

## 常用命令与Jedis

### Jedis连接

添加依赖（pom.xml）
```xml
<dependency>
    <groupId>redis.clients</groupId>
    <artifactId>jedis</artifactId>
    <version>4.4.0</version>
</dependency>
```

创建连接
```java
Jedis jedis = new Jedis("localhost", 6379);
// jedis.auth("password");  // 如有密码
jedis.ping();  // 测试连接，返回 "PONG"
jedis.set("key", "value");
String value = jedis.get("key");
jedis.close();  // 用完关闭
```

### Key 相关命令

| 命令 | 说明 |
| --- | --- |
| `DEL key [key ...]` | 删除给定的一个或多个 key |
| `EXISTS key` | 检查 key 是否存在 |
| `EXPIRE key seconds` | 为 key 设置过期时间（秒） |
| `TTL key` | 查看 key 剩余的生存时间（秒），-1 表示永不过期，-2 表示 key 不存在 |
| `KEYS pattern` | 查找所有符合给定模式 pattern 的 key（生产环境慎用） |
| `RENAME key newkey` | 将 key 改名为 newkey |
| `TYPE key` | 返回 key 所存储的值的类型 |

### String 类型常用命令

| 命令 | 说明 |
| --- | --- |
| `SET key value` | 设置指定 key 的值 |
| `GET key` | 获取指定 key 的值 |
| `GETSET key value` | 设置 key 的值，并返回 key 的旧值 |
| `MSET key value [key value ...]` | 同时设置多个 key-value |
| `MGET key [key ...]` | 获取所有给定 key 的值 |
| `INCR key` | 将 key 中储存的数字值增一 |
| `DECR key` | 将 key 中储存的数字值减一 |
| `INCRBY key increment` | 将 key 所储存的值加上给定的增量值 |
| `APPEND key value` | 将 value 追加到 key 原来的值的末尾 |

[jedis实现String相关命令](../details/jedis-string.md)

### List 类型常用命令

| 命令 | 说明 |
| --- | --- |
| `LPUSH key value [value ...]` | 将一个或多个值插入到列表头部 |
| `RPUSH key value [value ...]` | 在列表尾部添加一个或多个值 |
| `LPOP key` | 移除并返回列表的第一个元素 |
| `RPOP key` | 移除并返回列表的最后一个元素 |
| `LRANGE key start stop` | 返回列表中指定区间内的元素（0 -1 表示全部） |
| `LLEN key` | 获取列表长度 |
| `LINDEX key index` | 通过索引获取列表中的元素 |
| `LREM key count value` | 根据 count 的值，移除列表中与 value 相等的元素 |

[jedis实现List相关命令](../details/jedis-list.md)

### Hash 类型常用命令

| 命令 | 说明 |
| --- | --- |
| `HSET key field value` | 将哈希表 key 中字段 field 的值设为 value |
| `HGET key field` | 获取哈希表中指定字段的值 |
| `HGETALL key` | 获取哈希表中指定 key 的所有字段和值 |
| `HDEL key field [field ...]` | 删除一个或多个哈希表字段 |
| `HEXISTS key field` | 查看哈希表 key 中指定字段是否存在 |
| `HKEYS key` | 获取哈希表中的所有字段名 |
| `HVALS key` | 获取哈希表中的所有值 |
| `HINCRBY key field increment` | 为哈希表 key 中指定字段的整数值加上增量 |

[jedis实现Hash相关命令](../details/jedis-hash.md)

### Set 类型常用命令

| 命令 | 说明 |
| --- | --- |
| `SADD key member [member ...]` | 向集合添加一个或多个成员 |
| `SREM key member [member ...]` | 移除集合中一个或多个成员 |
| `SMEMBERS key` | 返回集合中的所有成员 |
| `SISMEMBER key member` | 判断 member 是否是集合 key 的成员 |
| `SCARD key` | 获取集合的成员数 |
| `SINTER key [key ...]` | 返回给定所有集合的交集 |
| `SUNION key [key ...]` | 返回给定所有集合的并集 |
| `SDIFF key [key ...]` | 返回给定所有集合的差集 |

[jedis实现Set相关命令](../details/jedis-set.md)

### ZSet 类型常用命令

| 命令 | 说明 |
| --- | --- |
| `ZADD key score member [score member ...]` | 向有序集合添加一个或多个成员，或更新已存在成员的分数 |
| `ZRANGE key start stop [WITHSCORES]` | 按索引区间返回有序集合指定区间内的成员（分数从低到高） |
| `ZREVRANGE key start stop [WITHSCORES]` | 返回有序集合指定区间内的成员（分数从高到低） |
| `ZREM key member [member ...]` | 移除有序集合中的一个或多个成员 |
| `ZCARD key` | 获取有序集合的成员数 |
| `ZCOUNT key min max` | 计算有序集合中指定分数区间内的成员数 |
| `ZRANK key member` | 返回有序集合中指定成员的排名（从小到大，从 0 开始） |
| `ZREVRANK key member` | 返回有序集合中指定成员的排名（从大到小，从 0 开始） |
| `ZINCRBY key increment member` | 对有序集合中指定成员的分数加上增量 increment |

[jedis实现ZSet相关命令](../details/jedis-zset.md)

---
## ACL 与 Jedis

### Redis ACL 概念

* Redis ACL (**Access Control List**) 是 Redis **6.0** 引入的访问控制系统，它提供了更细粒度的权限控制机制。
- ACL 是 Redis 安全性的重要组成部分，特别适合多用户共享的 Redis 环境。
- **定义多个用户**，每个用户有独立的密码，为每个用户分配特定的命令权限。
- 控制用户对特定**键模式**的访问
    - 例如执行 `ACL SETUSER username ~order:* ~product:*`，用户只能访问以 "order:" 或 "product:" 开头的键
    - `~` 符号表示"键模式匹配"的权限前缀

### 开启 ACL

1. **Redis 6.0+ 默认启用** ACL，但默认只有一个默认用户：default
2. **配置文件中启用**
    1. 在 redis.conf 中添加：`aclfile /etc/redis/users.acl
    2. 然后创建对应的 ACL 文件：`touch /etc/redis/users.acl`
3. **重启 Redis服务（修改配置文件一定要重启 redis 服务）之后用以下命令**：
    1. 使用 `ACL SETUSER` 命令创建用户
    2. 使用 `ACL SAVE` 保存到 ACL 文件

### 基本 ACL 命令

开启了 acl 文件之后，再次使用 redis-cli 进行登录的时候。这样做：

```shell
[root@master bin]# redis-cli
127.0.0.1:6379> auth default 123456
OK
```

另一种登录方式：

```shell
redis-cli -u redis://default:123456@localhost:6379/0
```

基本的 ACL 命令：

```shell
# default用户是最高权限，先使用default用户登录上去
redis-cli -u redis://default:123456@localhost:6379/0

# 创建新用户，并指定密码，这个用户只能读redis库中以cache开头的键。
ACL SETUSER laodu on >laodu123 +@read ~cache:*

# 给laodu所有权限
ACL SETUSER laodu on >laodu123 +@all ~*

# 查看用户
ACL LIST

# 保存 ACL 配置
ACL SAVE

# 以特定用户连接
redis-cli -u redis://laodu:laodu123@localhost:6379/0
```

## TLS/SSL

TLS主要保护客户端不被骗，同时保护数据不被偷看。

### TLS/SSL 实现原理

1. Redis服务器需要向CA机构申请证书，这个证书相当于现实生活中的营业执照。
2. 营业执照申请下来挂到店里，等于是放到 Redis服务器的某个目录中。
3. 然后 `java` 客户端内置了**根证书**（用它来验证营业执照真伪），jdk安装之后jdk的目录中就自带了根证书。【**JAVA_HOME\lib\security\cacerts**】
4. 当java客户端发送数据给redis服务器的时候，**java客户端**会使用根证书验证 **Redis 服务器**的真伪，如果验证失败，立即中断连接。
5. 如果验证通过，建立加密通道进行通信（加密的实现是：java 客户端和 Redis 服务器商量好一个暗号，按照这个暗号进行数据传输。即使窃听了也没事）

### 安装Redis7时的注意事项

安装OpenSSL的开发包

```shell
sudo yum update
sudo yum install openssl-devel
```

编译时，按照支持TLS/SSL方式进行编译：

```shell
make MALLOC=libc BUILD_TLS=yes
```

**这一步在我们最开始安装 Redis 的时候已经完成了。**

### 启用TLS/SSL

**第一步**：生成证书：使用Redis自带的工具gen-test-certs.sh生成证书。切换redis的源码目录下，然后运行如下命令：

```shell
cd utils
./gen-test-certs.sh
```

生成的证书将位于 `utils/tests/tls/` 目录下。

**这里生成的证书是自签名证书哈（仅用于开发和测试，或者说你的项目以后是在局域网中运行的，这种方式完全够用）。**

**生成自签名证书的意思是：自己给自己发证。自己给自己发营业执照。（正常来说这个证书应该是 CA 机构来发证）**

**生产环境下一般是连接云服务商的 Redis，你什么都不用做，服务商已经配好证书了。服务商配置的证书都是 CA 机构给发的。**

**第二步**：在Redis的配置文件中添加以下内容：**把配置文件中的 `port 6379`注释掉，然后添加以下配置**

```shell
port 0            # port 0 表示完全禁用非加密的普通端口
tls-port 6379
tls-cert-file /root/redis-7.4.2/utils/tests/tls/redis.crt
tls-key-file /root/redis-7.4.2/utils/tests/tls/redis.key
tls-ca-cert-file /root/redis-7.4.2/utils/tests/tls/ca.crt
tls-auth-clients no  # 禁用客户端证书验证（表示Redis服务器不要求客户端提供证书）
```

**第三步**：重启 redis服务：

```shell
redis-server /etc/redis.conf
```

**第四步**：将redis证书导入Java信任库：**使用 Windows PowerShell，并且使用管理员身份打开**

1. 将生成的 `/root/redis-7.4.2/utils/tests/tls/redis.crt` 文件从centos系统中传送到windows环境下，放到 IDEA 项目的resources目录下。并拷贝该文件的绝对路径。
2. 使用**管理员身份**启动dos命令窗口，执行以下命令：

```plain
keytool.exe -importcert -file /path/redis.crt -alias redis-tls-cert -keystore "JAVA_HOME\lib\security\cacerts" -storepass changeit
```

注意：以上命令中两个路径需要修改，第一个是`/path/redis.crt`，另一个是`JAVA_HOME`。

**注意：当你开启了 SSL 之后，使用 `redis-cli`再次登录 redis 的时候和之前的方式就不同了：**

```shell
redis-cli --tls -u redis://default:123456@localhost:6379 --insecure
```