# 服务器

**来源**：《Redis设计与实现》第 14 章

---

## 命令请求的执行过程

一个命令请求从发送到获得回复的完整过程（以 `SET KEY VALUE` 为例）：

### 步骤 1：发送命令请求

客户端将命令转换成 RESP 协议格式，通过套接字发送给服务器：

```
*3\r\n$3\r\nSET\r\n$3\r\nKEY\r\n$5\r\nVALUE\r\n
```

### 步骤 2：读取命令请求

服务器调用命令请求处理器：
1. 读取协议格式命令 → 保存到客户端输入缓冲区（querybuf）
2. 分析命令 → 提取参数到 argv、argc
3. 调用命令执行器

### 步骤 3：查找命令实现

在 **命令表**（字典）中根据 argv[0] 查找对应的 redisCommand 结构

- 命令表不区分大小写（"SET"、"set"、"Set" 都对应 setCommand）
- 将找到的结构保存到客户端状态 cmd 属性

### 步骤 4：执行预备操作

执行命令前需检查：
- cmd 指针是否非 NULL
- 参数个数是否正确（arity）
- 客户端是否已通过身份验证
- 内存占用是否超限（maxmemory）
- 是否正在执行持久化、载入数据、Lua 脚本超时等
- 是否处于事务模式、订阅模式

### 步骤 5：调用命令实现函数

```
client->cmd->proc(client);
```

例如 SET 命令调用 setCommand(client)，执行后将回复保存到输出缓冲区。

### 步骤 6：执行后续工作

- 慢查询日志检查
- 更新命令统计（milliseconds、calls）
- AOF 缓冲区写入
- 命令传播给从服务器

### 步骤 7：发送回复

客户端套接字变为可写时，命令回复处理器将输出缓冲区内容发送给客户端。

### 步骤 8：客户端接收并打印回复

客户端将协议格式回复转为人类可读格式并打印。

---

## serverCron 函数

详见 [05-event-system/02-time-event.md](../05-event-system/02-time-event.md)

serverCron 默认每 100 毫秒执行一次，负责：
- 更新服务器时间缓存（unixtime / mstime）
- 更新 LRU 时钟（lruclock，每 10 秒）
- 更新每秒执行命令次数（instantaneous_ops_per_sec）
- 更新内存峰值
- 处理 SIGTERM 信号
- 管理客户端资源（释放超时连接）
- 管理数据库资源（删除过期键）
- 执行被延迟的 BGREWRITEAOF
- 检查持久化操作状态
- 将 AOF 缓冲区写入文件
- 关闭输出缓冲区超限的客户端

---

## 服务器初始化流程

```
main():
    1. init_server_config()    — 初始化服务器配置（读取 redis.conf）
    2. init_server()           — 初始化数据结构、创建共享对象
    3. init_server_last()      — 创建事件循环、监听端口、注册事件处理器
    4. load_data()             — 载入 RDB/AOF 文件恢复数据
    5. aeMain()                — 进入事件循环（aeProcessEvents）
```
