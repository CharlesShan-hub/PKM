
# 第一章 Redis概述
<img src="https://cdn.nlark.com/yuque/0/2025/jpeg/21376908/1757681056420-39d1bc52-55fe-4f3b-8183-b4d7ba79b166.jpeg" width="4308" title="" crop="0,0,1,1" id="eDZKS" class="ne-image" style="font-size: 16px">

## Redis是什么
Redis是一个缓存数据库。Redis以键值对（key-value）的方式存储数据。

Redis数据存储在内存中，速度非常快，不需要IO操作。

随着互联网行业的发展，现代的系统并发量很大，缓存数据库就是在这种背景下出现的。

## NoSQL是什么
NoSQL和Redis的关系？

+ NoSQL，全称Not Only SQL，翻译为不仅仅是SQL，又被称为非关系型数据库。
+ NoSQL 的出现并不是完全取代关系型数据库的，可以将 NoSQL 看做是对关系型数据库的补充和扩展。因此它的名字叫做 Not Only SQL。
+ Redis缓存数据库属于NoSQL数据库的一员。

## 数据库的分类
### 关系型数据库
MySQL、PostgreSQL（简称pgsql）、Oracle、SQL Server，属于**强一致性**。

**强一致性是指，在数据更新后，任何后续的读操作都必须立刻、绝对地读到这个最新的值。关系型数据库就是这样一个特点。**

### 非关系型数据库（NoSQL）
NoSQL 数据库包括：键值数据库、文档数据库、列族数据库、图数据库。

#### 键值数据库（Key-Value）
_缓存型_：如 Redis、Memcached（专为高速缓存设计）。  **<font style="color:#DF2A3F;">【注意：不要错误的认为NoSQL数据库都是缓存数据库，这是不对的！！！！】</font>**

_持久化型_：如 RocksDB（支持长期存储）。

#### 文档数据库：如 MongoDB（存储结构化文档，一个文档就是一个 JSON，不是你想的 word/pdf）。  
<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1743168385558-13a779f2-8175-4471-bb2e-5907db135dc6.png" width="379" title="" crop="0,0,1,1" id="ua16f287d" class="ne-image" style="font-size: 16px">

#### 列族数据库：如 Cassandra、HBase（适合海量数据分析）。  
传统的数据库都是行式存储：**以行为单位存储**

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1766401429000-fccad248-23d5-49c6-ae39-e10785a6c739.png" width="905.6" title="" crop="0,0,1,1" id="u5bd0d1d0" class="ne-image" style="font-size: 16px">

**优点：**<font style="color:rgb(15, 17, 21);">查询</font>**<font style="color:rgb(15, 17, 21);">单个用户</font>**<font style="color:rgb(15, 17, 21);">的全部信息极快，因为一次磁盘读取就能拿到整行。</font>

**缺点：**<font style="color:rgb(15, 17, 21);">如果想做一个分析，比如“</font>**<font style="color:rgb(15, 17, 21);">计算全国用户的平均年龄</font>**<font style="color:rgb(15, 17, 21);">”，数据库必须</font>**<font style="color:rgb(15, 17, 21);">扫描整张表</font>**<font style="color:rgb(15, 17, 21);">，把每一行（连同姓名、城市、职业等无关字段）都从磁盘读进内存，再挑出“年龄”这一列来计算。大量I/O被浪费在读取无关数据上。</font>

<font style="color:rgb(15, 17, 21);"></font>

**<font style="color:rgb(15, 17, 21);">列族数据库：以列为单位存储</font>**

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1766401636056-180e239c-f708-4e40-a730-1f06d264380d.png" width="532" title="" crop="0,0,1,1" id="u08aaafe2" class="ne-image" style="font-size: 16px">

**优点：**<font style="color:rgb(15, 17, 21);">进行上面那个“</font>**<font style="color:rgb(15, 17, 21);">计算平均年龄</font>**<font style="color:rgb(15, 17, 21);">”的分析时，数据库</font>**<font style="color:rgb(15, 17, 21);">只需要读取</font>**`**<font style="color:rgb(15, 17, 21);background-color:rgb(235, 238, 242);">年龄</font>**`**<font style="color:rgb(15, 17, 21);">这一个列文件</font>**<font style="color:rgb(15, 17, 21);">，极大地减少了I/O，计算速度飙升。</font>

**缺点：**<font style="color:rgb(15, 17, 21);">查询“用户ID=1的全部信息”反而变慢，因为它需要从多个列文件中分别读取数据再拼装起来。</font>

#### 图数据库：如 Neo4j（处理复杂关系网络）。
图数据库 = 用“节点”和“边”存储关系，直接映射现实世界的网络结构

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1743172293350-e39d9c6d-311b-4ae4-b0db-c0b763f0845b.png" width="766" title="" crop="0,0,1,1" id="u90a11135" class="ne-image" style="font-size: 16px">

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1743172262873-befb07a4-c52c-464f-90fd-bdad57ba2cde.png" width="542" title="" crop="0,0,1,1" id="wASgM" class="ne-image" style="font-size: 16px">



### 关系型数据库和非关系型数据库的区别
+ **关系型数据库**：
    - 用表存储数据
    - 用主键外键表示关系
    - 有严格的约束
    - 有严格的字段类型
    - 支持ACID确保数据可靠性
    - 通过标准的SQL语句完成数据的操作
    - **比较适合垂直扩展**：要提升性能，通过提高单机硬件的性能达到的扩展叫做垂直扩展。【**<font style="color:rgb(15, 17, 21);">关系型数据库的水平扩展会严重损害其核心优势（ACID事务和复杂关联查询），导致架构复杂度飙升，往往得不偿失。</font>**】
+ **非关系型数据库**：
    - 数据存储灵活
    - **支持水平扩展**：要提升性能，通过添加普通服务器节点达到的扩展叫做水平扩展。(**成本相对较低**)
    - 弱化ACID
    - 高吞吐

## Redis是什么语言实现的
Redis（REmote DIctionary Server）是由**Salvatore Sanfilippo**（网名**antirez**）开发的开源内存数据库，最初发布于2009年。它的底层主要用**C语言**编写，以高性能和低延迟著称，广泛应用于缓存、消息队列等场景。

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1743210825552-fcd89e0e-7fc4-4ca5-a810-a8f4b236b542.png" width="321" title="" crop="0,0,1,1" id="u42f4a9d0" class="ne-image" style="font-size: 16px">

+ **Salvatore Sanfilippo**（antirez）是意大利程序员，曾在多个开源项目上贡献代码，但最著名的成就就是Redis。
+ 2019年后，他将Redis的维护权移交给了Redis Labs公司（现更名为Redis Inc.），但早期版本完全由他主导开发。

## Redis应用场景
Redis 的典型应用场景，包括但不限于：缓存、会话存储、排行榜、分布式锁等。

### 缓存（Cache）
****将热点数据（高频访问）存储在内存中，减少对磁盘数据库（MySQL）的访问

### 会话存储（Session Storage）
**核心作用**：集中管理用户会话（Session），支持分布式服务

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1743216313545-d2096dde-aba4-4189-88f5-0fbe9d07a9f8.png" width="850" title="" crop="0,0,1,1" id="u820239fa" class="ne-image" style="font-size: 16px">

### 排行榜（Leaderboard）
<font style="color:rgb(15, 17, 21);">游戏排行榜、直播打赏榜、运动步数榜，这些排行榜，Redis 都可以提供高性能实现。</font>

<font style="color:rgb(15, 17, 21);">这是因为</font>**<font style="color:rgb(15, 17, 21);">Redis 底层有一个 Sorted Set（有序集合）数据结构，能在插入数据时就自动维护全局顺序，所以查询排名时无需临时计算。</font>**

### 分布式锁（Distributed Lock）
`synchronized`是单机锁，作用范围是：**<font style="color:rgb(15, 17, 21);">单进程内</font>**<font style="color:rgb(15, 17, 21);">，多个线程之间。</font>

<font style="color:rgb(15, 17, 21);">分布式锁：</font>**<font style="color:rgb(15, 17, 21);">解决的是跨进程、跨机器的资源竞争问题。分布式锁是一种在分布式系统中，让多个进程/机器能够互斥地访问共享资源的协调机制。</font>**

**<font style="color:rgb(15, 17, 21);">Redis 可以实现分布式锁。</font>**<font style="color:rgb(15, 17, 21);">防止重复提交、秒杀库存扣减，都需要用到分布式锁。</font>

## Redis特点
1. Redis以key-value方式将数据存储在内存中（缓存中）。
2. Redis的value支持多种类型，例如：string(字符串)/hash(哈希表)/list(列表)/set(集合)/zset(有序集合)，不同的类型底层数据结构不同。
3. Redis的核心网络模型是单线程的，采用单线程设计主要是为了避免多线程的竞争条件和锁的开销，简化实现并保证原子性操作。Redis从 **<font style="color:#DF2A3F;">6.0</font>** 版本开始引入了**<font style="color:#DF2A3F;">有限的多线程支持</font>**，但**<font style="color:#DF2A3F;">核心逻辑仍是单线程</font>**：
4. Redis存储的value支持各种丰富的函数，例如：push/pop，add/remove等，可以取交集、并集、差集等丰富的操作，并且操作都是原子性的。
5. Redis存储的value支持不同方式的排序。
6. Redis也会周期性的将更新的数据写入磁盘，或者把修改操作追加到记录文件中。
7. Redis可以搭建集群，并且实现了主从（**<font style="color:#DF2A3F;">master-slave</font>**）同步。
8. Redis缓存数据库结合关系型数据库（MySQL）可以实现高速缓存。口诀：
    1. 查数据：先看Redis，没有再查数据库。
    2. 改数据：先改数据库，再删Redis。

# 第二章 Redis安装、启动、关闭
<img src="https://cdn.nlark.com/yuque/0/2025/jpeg/21376908/1757681056420-39d1bc52-55fe-4f3b-8183-b4d7ba79b166.jpeg" width="4308" title="" crop="0,0,1,1" id="Tegie" class="ne-image" style="font-size: 16px">

Redis 官方在 3.2 版本 之后已不再支持 windows。因此我们将在Linux中安装Redis。

以下演示在`**<font style="color:#DF2A3F;">CentOS Stream 10</font>**`版本上安装`**<font style="color:#DF2A3F;">redis 7.4.2</font>**`版本。



Redis官方提供了两种安装方式：

+ 第一种方式：下载Redis源码，然后手动编译，手动安装。
    - 优点：手动编译安装，灵活性高
    - 缺点：需自行解决依赖（如 GCC、Make）
    - 适合：适合于开发人员，可以安装最新版本或特定版本的 Redis
+ 第二种方式：使用系统自带的包管理器自动安装，这种方式要求必须联网，也可以称为在线安装
    - 优点：简单快捷，自动解决依赖。
    - 缺点：版本可能较旧（取决于发行版的仓库）
    - 适合：适合于新手/生产环境，较稳定，易维护。

我们选择第一种方式。

## Redis的安装
### 第一步：获得redis源码
```shell
wget https://download.redis.io/releases/redis-7.4.2.tar.gz
```

### 第二步：安装C编译器和 C++编译器
Redis是C语言实现的，因此编译Redis源码需要C语言编译器。(新版本 redis 也用了 C++动态链接库，因此也需要安装 C++编译器。)

**测试 **`**gcc**`** 编译器是否可以用**：`**gcc --version**`

**测试 **`**g++**`**编译器是否可以用：**`**g++ --version**`

### 第三步：编译Redis源码
解压源码：tar -zxvf redis-7.4.2.tar.gz

切换到源码根目录：cd redis-7.4.2



如果要启用Redis的`TLS/SSL`安全协议，需要按照以下方式编译：

**<font style="color:rgb(15, 17, 21);">SSL/TLS就是给网络通信套上“加密信封”，让Redis的数据传输从“明信片”变成“密码信”，防止中间人偷看或篡改。</font>**

安装OpenSSL的开发包

```shell
sudo yum update
sudo yum install openssl-devel
```

编译时，按照支持TLS/SSL方式进行编译：在源码根目录下执行

```shell
make MALLOC=libc BUILD_TLS=yes
```



（**<font style="color:#DF2A3F;">不要采用这种方式</font>**）如果不启用 Redis 的 `TLS/SSL`安全协议，直接这样编译：

```shell
make
```



### 第四步：安装Redis
执行安装命令（**<font style="color:#DF2A3F;">仍然在根目录下</font>**）：`make install`

Redis的命令自动安装到这个目录下了：`/usr/local/bin`

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1743475235521-397f43c9-731d-47ea-ae8c-dff3ac5fcf69.png" width="557" title="" crop="0,0,1,1" id="u77ebd320" class="ne-image" style="font-size: 16px">

这几个命令都是干什么用的呢？

+ redis-benchmark：Redis 官方提供的性能测试工具，用于快速评估 Redis 服务器的吞吐量、延迟和并发处理能力。
+ redis-check-aof：Redis 官方提供的工具，用于 检查和修复 AOF（Append Only File）持久化文件 的完整性。
+ redis-check-rdb：Redis 官方提供的工具，专门用于 检查和验证 RDB 持久化文件（默认 dump.rdb）的完整性和有效性。
+ **<font style="color:#DF2A3F;">redis-cli</font>**：Redis 官方提供的 命令行客户端工具，用于与 Redis 服务器交互。
+ redis-sentinel：Redis 官方提供的 高可用性（HA）解决方案，核心功能是管理 Redis 主从架构的自动故障转移（Failover）和监控，确保服务持续可用。
+ **<font style="color:#DF2A3F;">redis-server</font>**：Redis 的核心程序，负责 启动和运行 Redis 数据库服务。

## Redis的启动
### 前台启动（不建议）
在`/usr/local/bin`目录下直接执行`redis-server`来完成前台启动：

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1743476039460-00c70158-cfdd-4a98-98fa-273a918e64dd.png" width="626" title="" crop="0,0,1,1" id="u00a52b5b" class="ne-image" style="font-size: 16px">

**<font style="color:#74B602;">可以看到Redis的默认端口号为：6379</font>**



这种启动方式存在的问题：

1. 不能继续在这个窗口执行其他操作。
2. 关闭这个窗口后Redis服务自动关闭。

使用后台启动方式可以解决这些问题。

**<font style="color:#DF2A3F;">停止现在的Redis：ctrl + c</font>**

### 后台启动（建议）
第一步：切换到redis源码根目录，将`redis.conf`文件拷贝到`/etc`目录下

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1766408093078-af9b2d46-baa3-45f6-8143-cb3824060933.png" width="865.6" title="" crop="0,0,1,1" id="ua8603044" class="ne-image" style="font-size: 16px">

第二步：将`/etc/redis.conf`文件中的`daemonize no`修改为`daemonize yes`，保存退出。

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1743476876315-d87001bf-bbdd-4d8a-9e92-2e0a90a2b206.png" width="571" title="" crop="0,0,1,1" id="u3f442e68" class="ne-image" style="font-size: 16px">

第三步：切换到`/usr/local/bin`目录下，执行`redis-server /etc/redis.conf`命令

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1743477023038-bd0e48a2-0351-4c47-b487-bf82b6c46932.png" width="687" title="" crop="0,0,1,1" id="u514c326b" class="ne-image" style="font-size: 16px">



测试一下：使用 `redis-cli` 客户端工具登录并`ping`测试一下

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1743477173215-6b690336-27e1-4d4d-8eb4-6aaf463c5ea0.png" width="245" title="" crop="0,0,1,1" id="u953a82d5" class="ne-image" style="font-size: 16px">



**扩展：redis服务启动时出现了以下的警告信息：**

WARNING Memory overcommit must be enabled! Without it, a background save or replication may fail under low memory condition. Being disabled, it can also cause failures without low memory condition, see [https://github.com/jemalloc/jemalloc/issues/1328.](https://github.com/jemalloc/jemalloc/issues/1328.) To fix this issue add 'vm.overcommit_memory = 1' to /etc/sysctl.conf and then reboot or run the command 'sysctl vm.overcommit_memory=1' for this to take effect.

**以上信息翻译为：警告：必须启用内存过量提交（memory overcommit）！若不启用，在低内存条件下后台保存（BGSAVE）或复制（replication）可能会失败。**

执行以下命令来解决这个警告：

```shell
sysctl vm.overcommit_memory=1
```

## Redis默认数据库数量
1. Redis默认数据库数量是16个（index：0 ~ 15）

默认数量16可以在`redis.conf`配置文件中找到，如下：

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1743490321181-5ce019e4-2493-4a9a-8457-3326f0fb2154.png" width="307" title="" crop="0,0,1,1" id="uef71e2ea" class="ne-image" style="font-size: 16px">

也可以通过修改这个数字来改变数据库的数量，修改为32，或者64等都可以，修改后需要重启redis服务便可生效。

2. 默认使用的数据库是：0
3. 切换数据库的命令：`select <index>`，例如：select 1

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1743490505385-f7d23bd1-28c7-4a3f-9b09-fafe3274141e.png" width="371" title="" crop="0,0,1,1" id="ud492bd7b" class="ne-image" style="font-size: 16px">

4. **实际使用建议：集群模式** 下不支持多数据库（仅 DB 0 可用），因此多数场景下建议使用 DB 0，或通过key的前缀区分数据（例如 `user:info`、`order:info`），而非依赖多数据库，如果需要更高隔离性，可考虑多个Redis实例，而非多DB。
5. 查看当前数据库中key的数量：**dbsize**
6. 清空数据库：
    1. 清空当前数据库：**flushdb**
    2. 清空当前Redis实例中所有的数据库：**flushall**
    3. 这两个命令会立即删除数据，且不可恢复（除非有备份），**生产环境务必备份数据或限制命令权限！**

## Redis的关闭
### 第一种：redis-cli shutdown
这是最安全的方式，也是推荐的方式，正常关闭 Redis，执行持久化（如果配置了 RDB/AOF），并清理资源。



这样做：

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1743488854848-bc56c69a-968d-4ea9-a2b5-0df62f95c1c4.png" width="241" title="" crop="0,0,1,1" id="u56c1ca56" class="ne-image" style="font-size: 16px">

或者这样做：

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1743488966939-e9db1b81-a1c2-4aed-a740-956a645cf9af.png" width="313" title="" crop="0,0,1,1" id="u9d77035a" class="ne-image" style="font-size: 16px">



如果Redis设置了密码，则关闭时需要指定密码：`redis-cli -a password shutdown`



验证redis服务是否已经关闭：

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1743488916571-adf457f9-54b4-48eb-8ba0-688b0c769e10.png" width="464" title="" crop="0,0,1,1" id="u4cd271d0" class="ne-image" style="font-size: 16px">



以上是关闭默认端口号6379的Redis服务，如果要关闭指定端口的Redis服务（比如端口是6378），可以执行：`redis-cli -p 6378 shutdown`

### 第二种：杀死进程
使用`ps -ef | grep redis`命令查看redis服务进程id，然后执行`kill -9 进程id`来停止redis服务。

未持久化的数据会丢失，且可能损坏 AOF/RDB 文件。（一般不要用）

# 第三章 Redis的核心设计

<img src="https://cdn.nlark.com/yuque/0/2025/jpeg/21376908/1757681056420-39d1bc52-55fe-4f3b-8183-b4d7ba79b166.jpeg" width="4308" title="" crop="0,0,1,1" id="gc8Tu" class="ne-image" style="font-size: 16px">

Redis 是一个高性能的内存数据库，它的核心设计采用了 **单线程模型**、**I/O 多路复用** 和 **多线程辅助** 等技术来保证高效运行。

下面我会用简单易懂的方式解释这些概念：

## 单线程模型（核心部分）
+ **Redis 的核心操作（数据读写、命令执行）是单线程的**，这意味着它一次只处理一个客户端请求，不会出现多线程竞争资源的问题。
+ **优点**：
    - 避免多线程竞争锁的开销，简化实现。
    - 无上下文切换，CPU 缓存利用率高，适合内存操作。
+ **缺点**：
    - 所有操作必须 串行执行，长耗时命令（如 KEYS *、大 Key 操作）会阻塞其他请求。

> **为什么单线程还这么快？**
>
> + Redis 的数据都在内存中，操作速度极快。
> + 通过** I/O 多路复用**处理大量网络连接。
>

## I/O 多路复用（处理高并发连接）
+ **问题**：I/O指的是客户端和redis数据库的交互，输入指的是客户端向redis数据库发送数据，输出指的是redis数据库向客户端发送数据。每一个客户端和redis数据库之间交互都是一个独立的Socket通道，独立的I/O通道，假设有10个客户端和redis数据库交互，就是10个Socket通道，10个I/O通道。需要注意的是redis是单线程的，也就是说这10个I/O通道并不是10个线程，本质上是一个线程处理这10个I/O通道。那么单线程如何同时处理成千上万的客户端连接？
+ **解决方案**：I/O 多路复用。【**<font style="color:#DF2A3F;">用同一个线程，来轮流处理多个网络连接上的IO事件</font>**】
    - Redis 通过主线程监听多个客户端连接，当某个连接有数据到达时，才通知 Redis 处理。
    - Redis不会主动去轮询每个客户端，如果去轮询的话，就属于采用`阻塞I/O`的设计方案，这样CPU的压力非常大，非常影响性能。
    - 单线程同时监听多个客户端连接，当某个连接有数据到达时触发事件处理，而非轮询阻塞。
    - 类似于餐厅服务员（单线程）同时照看多个餐桌（客户端），谁需要点菜就过去服务，而不是一直等待某一个桌。
    - **<font style="color:#DF2A3F;">I/O 多路复用本质上是通过 Linux 系统内部提供的 epoll 机制+非阻塞 socket 实现的。</font>**
    - **<font style="color:#DF2A3F;">epoll（Event Poll）：事件通知机制。</font>**
    - **<font style="color:#DF2A3F;">非阻塞 Socket：调用完 read/write 立即返回，不会阻塞主线程，需要配合事件通知机制（epoll）来实现。比喻：比如你发完微信后立即去干别的，而不是一直盯着微信等回信，对方回信之后自然会通过手机铃声通知你。</font>**
+ **优点**：
    - 用单线程就能高并发处理连接，减少线程切换开销。
    - I/O多路复用采用非阻塞 I/O，避免空等。

## 多线程辅助（Redis 6.0+ 的优化）
+ **问题**：单线程虽然高效，但在某些场景（如大键删除、持久化）可能成为瓶颈。
+ **解决方案**：Redis 6.0 引入了多线程辅助功能：
    - **主线程**：仍单线程处理核心命令（如 `GET/SET`）。
    - **后台线程**：
        * 处理网络 I/O（读取请求、发送响应），减轻主线程负担。（**后台线程不执行命令，只做数据传输**）
        * 执行某些耗时操作（如 `UNLINK` 删除大键、`AOF` 持久化刷盘）。
+ **注意**：
    - 数据操作仍是单线程的，多线程仅用于辅助任务。
    - 默认关闭，需通过配置开启（如 `io-threads 4`）。

## 类比理解
+ **单线程**：像一家只有一个厨师的快餐店，但厨师做菜极快（内存操作）。
+ **I/O 多路复用**：厨师用一个对讲机监听所有顾客的点单，谁好了就处理谁的。
+ **多线程辅助**：雇了几个帮手（后台线程）专门端菜、打扫卫生，但核心炒菜还是厨师亲自做。

## 总结
| **技术** | **作用** | **是否默认启用** |
| --- | --- | --- |
| 单线程模型 | 核心命令执行（保证简单高效） | 是 |
| I/O 多路复用 | 高并发处理网络连接 | 是 |
| 多线程辅助 | 加速网络 I/O 和后台任务 | Redis 6.0+ 需配置 |


如果你是小白，只需记住：

+ Redis 的核心是单线程的，但通过 I/O 多路复用支持高并发。
+ 多线程辅助是锦上添花，不是推翻单线程设计。

# 第四章 **Redis的常用数据类型**
<img src="https://cdn.nlark.com/yuque/0/2025/jpeg/21376908/1757681056420-39d1bc52-55fe-4f3b-8183-b4d7ba79b166.jpeg" width="4308" title="" crop="0,0,1,1" id="s6dJV" class="ne-image" style="font-size: 16px">

1. redis数据类型说的是value的数据类型。**key永远都是string类型**。
2. value不同的数据类型，对应不同的数据结构。
3. redis的value常用数据类型包括：
    1. string类型
    2. list类型：列表（有序可重复）
    3. hash类型：map
    4. set类型：set集合（无序不可重复）
    5. zset类型（sortedset）：可排序的set集合

# 第五章 Redis常用命令
<img src="https://cdn.nlark.com/yuque/0/2025/jpeg/21376908/1757681056420-39d1bc52-55fe-4f3b-8183-b4d7ba79b166.jpeg" width="4308" title="" crop="0,0,1,1" id="XhsfX" class="ne-image" style="font-size: 16px">

## key相关命令
| **命令** | **说明** |
| --- | --- |
| keys * | 获取所有key |
| move <key> <dbindex> | 将当前库中数据移动到dbindex库中，如果dbindex库中已存在该key，则无法移动 |
| randomkey | 随机返回当前库中的一个key |
| type <key> | 获取value的数据类型 |
| del <key> | 删除key-value数据 |
| exists <key> | 判断key是否存在，0表示不存在，1表示存在 |
| expire <key> seconds | 设置key有效期，失效后会自动删除，单位秒 |
| pexpire <key> milliseconds | 设置key有效期，失效后会自动删除，单位毫秒 |
| persist <key> | 删除`过期时间` |


## string类型常用命令
| **命令** | **说明** |
| --- | --- |
| set <key> <value> | 存数据，如果key已经存在，则value自动覆盖。 |
| get <key> | 取数据。如果指定的key不存在，则返回结果`(nil)`，该结果表示无任何数据。当然，`删除`或`修改`类的操作如果返回结果是`(nil)`，则表示未执行任何操作（因为目标不存在）。 |
| getrange <key> start end | 获取value的片段，start用来指定开始下标，end用来指定结束下标。 |
| getset <key> <value> | 返回旧的值，再设置新的值。 |
| mset k1 v1 k2 v2 k3 v3 | 批量存数据 |
| mget k1 k2 k3 | 批量取数据 |
| setnx <key> <value> | 存数据，区别是：如果key不存在则存储，key存在则放弃存储。 |
| setrange <key> offset <value> | 从指定下标`offset`位置开始替换（要求下标必须是 `>= 0` 的整数），假设`username=zhangsan`，执行`setrange username 5 si`，最后的执行结果是`zhangsan`变成了`zhangsin`。 |
| incr <key> | **只支持整数字符串**，递增1，如果key不存在，第一次执行`incr`时，会自动执行`set key 0`，然后将值增长1。 |
| incrby <key> increment | **只支持整数字符串**，以指定步长递增。 |
| decr <key> | **只支持整数字符串**，递减1。 |
| decrby <key> increment | **只支持整数字符串**，以指定步长递减。 |
| incrbyfloat <key> increment | ****以指定步长递增，支持浮点数操作。 |
| append <key> <value> | 在原数据后面追加 |
| strlen <key> | 获取数据的长度 |
| object encoding <key> | Redis 的一个调试命令，用于查看指定 key 的底层存储编码（即 Redis 内部使用的数据结构类型）。它可以帮助开发者优化内存使用或排查性能问题。 |




object encoding命令的`返回值`详细说明：

1. 返回值：返回 key 对应值的内部编码（字符串形式）。
2. 返回值说明：
    1. `"int"`：使用 INCR 操作的整数或小整数
    2. `"embstr"`：长度 ≤ 44 字节的字符串
    3. `"raw"`：长度 > 44 字节的字符串
    4. `"quicklist"`：LIST 类型
    5. `"hashtable"`：大型哈希或集合
    6. `"intset"`：仅含整数的小规模 SET
    7. `"skiplist"`：ZSET 类型（sorted set）
    8. `"listpack"`：哈希、列表、有序集合的小规模存储

## list类型常用命令
提示：list类型相关命令中`l`对应的是`left`，`r`对应的是`right`。

注意：**<font style="color:#DF2A3F;">红色字体</font>**相关命令的第一个字母 `l`表示 `list`

| **命令** | **说明** |
| --- | --- |
| lpush <key> element [element ...] | 左压入。添加操作。`lpush numbers 1 2 3` |
| rpush <key> element [element ...] | 右压入。添加操作。`rpush numbers 4 5 6` |
| <font style="color:#DF2A3F;">lrange <key> start stop</font> | 将列表中的数据读取出来，start指定起始下标，stop指定结束下标。0是起始下标，-1是最后一个元素的下标。读取操作，无删除操作。 |
| lpop <key> [count] | 左弹出。删除操作。未指定`count`时删除`1`个。 |
| rpop <key> [count] | 右弹出。删除操作。未指定`count`时删除`1`个。 |
| <font style="color:#DF2A3F;">llen <key></font> | 获取列表中数据的个数 |
| <font style="color:#DF2A3F;">lrem <key> count element</font> | `count > 0`：从左侧开始搜索，移除与`element`相等的元素，移除数量为count<br/>`count < 0`：从右侧开始搜索，移除与`element`相等的元素，移除数量为count<br/>`count = 0`：移除列表中所有与`element`相等的元素 |
| <font style="color:#DF2A3F;">lindex <key> index</font> | 获取指定索引位置的元素。只读取，不删除。0是第一个元素，-1是最后一个元素。 |
| <font style="color:#DF2A3F;">lset <key> index element</font> | 修改指定索引处的值。0是第一个元素，-1是最后一个元素。 |
| <font style="color:#DF2A3F;">ltrim <key> start stop</font> | 裁剪列表，只保留`start`和`stop`区间的数据，其它数据删除。0是第一个元素，-1可以表示最后一个元素。 |
| <font style="color:#DF2A3F;">linsert <key> before|after pivot element</font> | 在基准元素`pivot`前或后插入新元素`element` |
| rpoplpush source destination | 用于移除`source`列表的最后一个元素，并将移除的元素添加到`destination`列表。<br/>rpoplpush：source列表右弹，destination列表左压。 |


## hash类型常用命令
| **命令** | **说明** |
| --- | --- |
| hset <key> field value [field value ...] | 1. 作用：给哈希表的字段赋值。<br/>2. 哈希表不存在时，新建哈希表，并将`field value...`添加到哈希表。<br/>3. 哈希表存在时，并且`field`已存在时，`value`将覆盖。 |
| hget <key> field | 通过`field`获取`value` |
| hmget <key> field [field ...] | 通过多个`field`获取多个`value` |
| hgetall <key> | 获取所有的`field value` |
| hexists <key> field | 判断这样的`field`是否存在，1表示存在，0表示不存在。 |
| hsetnx <key> field value | 当哈希表中不存在这个`field`，则添加，如果`field`存在，则不处理。 |
| hincrby <key> field increment | 把`field`对应的`value`以`increment`步长增长。如果`value`不是一个integer会报错。 |
| hdel <key> field [field ...] | 删除一个或多个`field` |
| hkeys <key> | 取出所有的`field` |
| hvals <key> | 取出所有的`value` |
| hlen <key> | 获取`field-value`的个数 |


## set类型常用命令
| **命令** | **说明** |
| --- | --- |
| sadd <key> member [member ...] | 向set集合中添加成员。重复的成员只能添加1个。 |
| smembers <key> | 列出所有成员。 |
| srem <key> member [member ...] | 删除set集合中的成员。 |
| sismember <key> member | 判断set集合中是否存在这个成员，1表示存在，0表示不存在。 |
| scard <key> | 获取set集合中成员个数 |
| srandmember <key> [count] | 随机获取set集合中的`[count]`个成员 |
| spop <key> | 从set集合中随机的弹出一个成员（会删除掉） |
| sdiff key [key ...] | 差集 （得到一个新的结果，不会修改原集合，直接将结果返回/输出） |
| sdiffstore destination key [key ...] | 差集并存储到一个新的集合 |
| sinter key [key ...] | 交集 |
| sinterstore destination key [key ...] | 交集并存储到一个新的集合 |
| sunion key [key ...] | 并集 |
| sunionstore destination key [key ...] | 并集并存储到一个新的集合 |


## zset类型常用命令
| **命令** | **说明** |
| --- | --- |
| zadd <key> score member [score member ...] | 1. 添加数据到有序集合<br/>2. score必须是一个数字型的<br/>3. score存储的是双精度浮点数，如果score是10这样的整数，<br/>底层也会存储为双精度浮点数。<br/>4. score决定成员的排序顺序<br/>5. 可以一次添加多个 |
| zincrby <key> increment member | 将`member`的`score`增长`increment` |
| zscore <key> member | 获取`member`的`score` |
| **<font style="color:#E746A4;">zrange <key> start stop</font>** | 从已排序的集合中获取`start`到`stop`之间的`member列表`，<br/>0是第一个元素的下标，-1是最后一个元素的下标。 |
| **<font style="color:#E746A4;">zrange <key> start stop withscores</font>** | 获取`member列表`时带上`score` |
| **<font style="color:#117CEE;">zrangebyscore <key> min max</font>** | 根据`score`来获取成员，`min`指定最低`score`，`max`指定最高`score` |
| **<font style="color:#117CEE;">zrangebyscore <key> min max withscores</font>** | 获取`member列表`时带上`score` |
| **<font style="color:#117CEE;">zrangebyscore <key> min max withscores limit offset count</font>** | 支持分页 |
| **<font style="color:#DF2A3F;">zrevrangebyscore <key> max min withscores limit offset count</font>** | 降序方式取 |
| zcard <key> | 成员个数 |
| zcount <key> min max | 获取`min score`和`max score`之间成员个数 |
| zrem <key> member [member ...] | 删除一个或多个成员 |




# 第六章 Java使用Jedis操作Redis
<img src="https://cdn.nlark.com/yuque/0/2025/jpeg/21376908/1757681056420-39d1bc52-55fe-4f3b-8183-b4d7ba79b166.jpeg" width="4308" title="" crop="0,0,1,1" id="bhG0a" class="ne-image" style="font-size: 16px">

Jedis API帮助文档地址：[https://javadoc.io/doc/redis.clients/jedis/latest/index.html](https://javadoc.io/doc/redis.clients/jedis/latest/index.html)

## 设置密码及端口放行
### 修改 Redis 配置文件
```bash
vim /etc/redis.conf
```

找到并修改以下关键配置：

```nginx
# 绑定所有网络接口（默认只绑定127.0.0.1）
bind 0.0.0.0

# 关闭保护模式
protected-mode no

# 设置密码（强烈建议）
requirepass your_strong_password
```

提醒：如果开启了密码，那么`redis-cli`登录之后，要使用`auth`命令认证才能使用以往的命令窗口的操作。例如 `127.0.0.1:6379> auth "123456"`

### 开放防火墙端口
```bash
# 启用防火墙
sudo systemctl start firewalld.service

# 添加防火墙规则
sudo firewall-cmd --permanent --add-port=6379/tcp
sudo firewall-cmd --reload

# 验证端口开放
sudo firewall-cmd --list-ports
```

### 重启 Redis 服务
```bash
# 关闭
redis-cli shutdown       #如果有密码，执行这个：redis-cli -a "123456" shutdown

# 启动
redis-server /etc/redis.conf
```

### 验证 Redis 监听状态
```bash
sudo netstat -tulnp | grep redis
# 应该显示 0.0.0.0:6379
```

## 开发环境准备
### 添加Jedis依赖
```xml
<dependency>
    <groupId>redis.clients</groupId>
    <artifactId>jedis</artifactId>
    <version>4.3.1</version>
</dependency>
```

### 创建Jedis连接
```java
import redis.clients.jedis.Jedis;

public class RedisBasic {
    public static void main(String[] args) {
        // 创建Jedis连接
        Jedis jedis = new Jedis("localhost", 6379);

        // 设置密码
        jedis.auth("123456");
        
        // 测试连接
        System.out.println("连接状态: " + jedis.ping());
        
        // 关闭连接
        jedis.close();
    }
}
```

## String类型操作
```java
public class StringDemo {
    public static void main(String[] args) {
        // 创建Jedis对象，建立连接
        Jedis jedis = new Jedis("localhost", 6379);
        // 设置密码
        jedis.auth("123456");
        // set
        jedis.set("name", "zhangsan");
        // get
        String name = jedis.get("name");
        System.out.println(name);
        // 设置数据的过期时间
        jedis.setex("password", 10, "admin123");
        String password = jedis.get("password");
        System.out.println(password);
        // 休眠10S
        try {
            TimeUnit.SECONDS.sleep(11);
        } catch (InterruptedException e) {
            throw new RuntimeException(e);
        }
        password = jedis.get("password");
        System.out.println(password);
        // 操作数字
        jedis.set("count", "100");
        jedis.incr("count");
        String count = jedis.get("count");
        System.out.println(count); // 101
        // 关闭
        jedis.close();
    }
}

```

## List类型操作
```java
public class ListDemo {
    public static void main(String[] args) {
        // 创建Jedis对象，建立连接
        Jedis jedis = new Jedis("192.168.48.200", 6379);
        // 设置密码
        jedis.auth("123456");

        // 1.左压
        jedis.lpush("names", "zhangsan", "lisi", "wangwu");

        // 2.右压
        jedis.rpush("names", "zhangsan", "lisi", "wangwu");

        // 3.取长度
        long len = jedis.llen("names");
        System.out.println("长度：" + len);

        // 4.取范围
        List<String> names = jedis.lrange("names", 0, -1);
        names.forEach(System.out::println);

        // 5.右弹出
        String name = jedis.rpop("names");
        System.out.println("右弹出的数据：" + name);

        // 6.取长度
        len = jedis.llen("names");
        System.out.println("长度：" + len);

        // 关闭
        jedis.close();
    }
}
```

## Hash类型操作
```java
public class HashDemo {
    public static void main(String[] args) {
        // 创建Jedis对象，建立连接
        Jedis jedis = new Jedis("192.168.48.200", 6379);
        // 设置密码
        jedis.auth("123456");

        // 1.存
        jedis.hset("user:110", "name", "jack");
        jedis.hset("user:110", "age", "20");
        jedis.hset("user:110", "phone", "12345645685");
        // 创建Map集合
        Map<String,String> userMap = new HashMap<>();
        userMap.put("sex", "f");
        userMap.put("id", "110");
        jedis.hmset("user:110", userMap);

        // 2.取
        String phone = jedis.hget("user:110", "phone");
        System.out.println("phone:" + phone);

        // 3.取所有
        Map<String, String> map = jedis.hgetAll("user:110");
        System.out.println(map);

        // 4.根据field删除
        jedis.hdel("user:110", "phone");

        // 5.查看map中的键值对个数
        long len = jedis.hlen("user:110");
        System.out.println("键值对个数：" + len);

        // 关闭
        jedis.close();
    }
}
```

## Set类型操作
```java
public class SetDemo {
    public static void main(String[] args) {
        // 创建Jedis对象，建立连接
        Jedis jedis = new Jedis("192.168.48.200", 6379);
        // 设置密码
        jedis.auth("123456");

        // 刷新
        jedis.flushAll();

        // 1. 添加成员
        jedis.sadd("names", "jack", "lucy", "tom", "cat");

        // 2. 获取所有成员
        Set<String> names = jedis.smembers("names");
        names.forEach(System.out::println);

        // 3. 删除成员
        jedis.srem("names", "tom", "cat");

        // 4. 获取成员个数
        long card = jedis.scard("names");
        System.out.println("成员个数：" + card);

        // 5. 是否存在这个成员
        boolean isMember = jedis.sismember("names", "tom");
        System.out.println(isMember); // false

        isMember = jedis.sismember("names", "jack");
        System.out.println(isMember); // true

        // 关闭
        jedis.close();
    }
}
```

## Sorted Set类型操作
```java
public class SortedSetDemo {
    public static void main(String[] args) {
        // 创建Jedis对象，建立连接
        Jedis jedis = new Jedis("192.168.48.200", 6379);
        // 设置密码
        jedis.auth("123456");
        // 添加
        jedis.zadd("students", 90, "李四");
        jedis.zadd("students", 92, "王五");
        jedis.zadd("students", 89, "赵六");
        jedis.zadd("students", 100, "陈琦");

        // 按照升序取出
        List<String> students = jedis.zrange("students", 0, -1);
        students.forEach(System.out::println);

        // 按照降序取出
        students = jedis.zrevrange("students", 0, -1);
        students.forEach(System.out::println);

        // 获取元素分数
        Double score = jedis.zscore("students", "陈琦");
        System.out.println(score);

        // 关闭
        jedis.close();
    }
}
```

## 综合示例
```java
public class RedisExample {
    public static void main(String[] args) {
        Jedis jedis = new Jedis("192.168.48.200", 6379);
        
        // 1. 用户登录记录(String)
        jedis.setex("user:1001:token", 3600, "abc123xyz");
        
        // 2. 用户购物车(Hash)
        jedis.hset("cart:1001", "item1", "2");
        jedis.hset("cart:1001", "item2", "1");
        
        // 3. 最近浏览商品(List)
        jedis.lpush("recent:1001", "product003", "product007");
        jedis.ltrim("recent:1001", 0, 4);  // 保留最近5个
        
        // 4. 商品标签(Set)
        jedis.sadd("product:1001:tags", "电子产品", "数码", "热门");
        
        // 5. 商品销量排行(Sorted Set)
        jedis.zadd("product:sales", 1500, "product1001");
        jedis.zadd("product:sales", 3000, "product1002");
        
        jedis.close();
    }
}
```

## 注意事项
1. 每次操作后应及时关闭Jedis连接
2. 键名设计应有意义，建议使用冒号分隔
3. 注意数据类型的正确使用场景
4. 生产环境应考虑添加密码认证

# 第七章 Jedis连接池技术
<img src="https://cdn.nlark.com/yuque/0/2025/jpeg/21376908/1757681056420-39d1bc52-55fe-4f3b-8183-b4d7ba79b166.jpeg" width="4308" title="" crop="0,0,1,1" id="By8oU" class="ne-image" style="font-size: 16px">

## 连接池基础概念
### 什么是连接池？
+ 连接池是一种管理数据库/缓存连接的技术，用于复用连接，避免频繁创建和销毁的开销。
+ 适用于高并发场景，提高系统性能。

### 为什么使用Jedis连接池？
+ **直接创建Jedis的问题**：
    - 每次操作都新建连接，性能低。
    - 频繁连接/断开增加Redis服务器负担。
    - 连接泄漏风险高。
+ **Jedis连接池的优势**：
    - 连接复用，减少创建/销毁开销。
    - 控制最大连接数，防止资源耗尽。
    - 提供连接健康检测，避免使用失效连接。

## JedisPool核心类
### `JedisPool`
+ 核心连接池实现，负责管理Jedis连接。
+ 初始化方式：

```java
JedisPoolConfig config = new JedisPoolConfig();
config.setMaxTotal(100); // 最大连接数
JedisPool jedisPool = new JedisPool(config, "192.168.48.200", 6379);
```

### `JedisPoolConfig`
+ 用于配置连接池参数：

```java
JedisPoolConfig config = new JedisPoolConfig();
config.setMaxTotal(100);  // 最大连接数
config.setMaxIdle(50);    // 最大空闲连接数
config.setMinIdle(10);    // 最小空闲连接数
config.setMaxWaitMillis(3000); // 获取连接最大等待时间（ms）
config.setTestOnBorrow(true);  // 借出时检测连接是否有效
```

## 连接池配置参数详解
| **参数** | **说明** | **推荐值** |
| --- | --- | --- |
| `maxTotal` | 最大连接数 | 根据并发量调整（如100） |
| `maxIdle` | 最大空闲连接数 | 建议 `maxTotal` 的50%~70% |
| `minIdle` | 最小空闲连接数 | 避免连接频繁创建/销毁（如10） |
| `maxWaitMillis` | 获取连接最大等待时间 | 3000ms（避免无限等待） |
| `testOnBorrow` | 借出时检测连接是否有效 | `true`（生产环境建议开启） |
| `testOnReturn` | 归还时检测连接是否有效 | `false`（影响性能） |
| `testWhileIdle` | 空闲时检测连接 | `true`（推荐） |
| `timeBetweenEvictionRunsMillis` | 空闲检测周期 | 60000ms（1分钟） |
| `minEvictableIdleTimeMillis` | 连接最小空闲时间 | **180000ms（3分钟）,表示至少允许人家空闲 3 分钟，超过 3 分钟该连接可以被标记为可清理。** |


## Jedis连接池使用
### Jedis工具类
```java
public class JedisUtil {
    // 连接池
    private static JedisPool jedisPool;

    // 类加载时初始化连接池
    static {
        JedisPoolConfig config = new JedisPoolConfig();
        config.setMaxTotal(100);
        config.setMaxIdle(50);
        config.setTestOnBorrow(true);
        // Protocol.DEFAULT_TIMEOUT 是 Jedis 客户端连接 Redis 服务器时的默认超时时间（2000 毫秒/2 秒）
        jedisPool = new JedisPool(config, "192.168.48.200", 6379, Protocol.DEFAULT_TIMEOUT, "123456");
    }

    // 从连接池中获取空闲的 Jedis
    public static Jedis getResource() {
        return jedisPool.getResource();
    }

    // 一般整个应用结束的时候（服务器关闭）调用这个方法关闭连接池。
    public static void close(){
        jedisPool.close();
    }
}
```

### 使用工具类
```java
try (Jedis jedis = JedisUtil.getResource()) {
    jedis.set("key", "value");
    String value = jedis.get("key");
} // 自动归还连接（try-with-resources）
```

### 连接泄漏问题
+ **错误示例**：

```java
Jedis jedis = JedisUtil.getResource();
jedis.set("key", "value");
// 忘记归还连接，导致泄漏！
```

+ **解决方案**：
    - 使用 `try-with-resources`(推荐) 或 `finally` 确保归还。

## 异常处理与性能优化
### 常见异常
在使用连接池的时候，经常会遇到以下这些异常：

+ `JedisConnectionException`：网络问题或Redis宕机。
+ `JedisExhaustedPoolException`：连接池耗尽（`maxTotal` 太小）。
+ `SocketTimeoutException`：Redis响应超时。

### 优化建议
**QPS（Queries Per Second）** 是指 **每秒查询数**，用于衡量系统的吞吐量。  

**计算方式**：

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1745806464430-6f973988-f9c2-41ad-9d06-a467ef9eaca9.png" width="234" title="" crop="0,0,1,1" id="u862a9713" class="ne-image" style="font-size: 16px">  
例如：1分钟内处理了6000次请求 → QPS = 6000 / 60 = 100。  

一般通过压测工具（如JMeter）模拟请求统计得出。  

****

**连接池大小**：

+ 计算公式：`maxTotal ≈ QPS × avg_query_time(ms) / 1000`
+ 例如：QPS=1000，平均查询时间=10ms → `maxTotal ≈ 10`（这样的话，10 个连接理论上可以保证 10ms 内处理 1000 个查询）

**安全系数：以上公式计算的是最小值。实际情况下需要考虑****<font style="color:#DF2A3F;">安全系数</font>****。****<font style="color:rgb(15, 17, 21);">它是来应付突发情况的。</font>**

+ **<font style="color:rgb(15, 17, 21);">Redis连接池安全系数建议1.2-1.5倍，数据库连接池建议2-3倍，因为数据库连接创建成本更高、需要更多缓冲。</font>**

**超时设置**：

+ `maxWaitMillis` 不宜过长（避免线程堆积）。

**健康检测**：

+ 开启 `testOnBorrow` 或 `testWhileIdle`。

# 第八章Redis的ACL
<img src="https://cdn.nlark.com/yuque/0/2025/jpeg/21376908/1757681056420-39d1bc52-55fe-4f3b-8183-b4d7ba79b166.jpeg" width="4308" title="" crop="0,0,1,1" id="B4jWF" class="ne-image" style="font-size: 16px">

Redis ACL (**Access Control List**) 是 Redis 6.0 引入的访问控制系统，它提供了更细粒度的权限控制机制。

## 什么是 Redis ACL
Redis ACL 允许你：

+ 定义多个用户，每个用户有独立的密码
+ 为每个用户分配特定的命令权限
+ 控制用户对特定键模式的访问，例如执行 `ACL SETUSER username ~order:* ~product:*`，用户只能访问以 "order:" 或 "product:" 开头的键
    - `**<font style="color:rgb(15, 17, 21);background-color:rgb(235, 238, 242);">~</font>**`**<font style="color:rgb(15, 17, 21);"> 符号表示"键模式匹配"的权限前缀</font>**

## 如何开启 ACL
1. **Redis 6.0+ 默认启用** ACL，但默认只有一个默认用户：default
2. **配置文件中启用**：  
在 redis.conf 中添加：

```plain
aclfile /etc/redis/users.acl
```

然后创建对应的 ACL 文件：**touch /etc/redis/users.acl**

3. **重启 Redis服务（****<font style="color:#DF2A3F;">修改配置文件一定要重启 redis 服务</font>****）之后用以下命令**：

使用 `ACL SETUSER` 命令创建用户

使用 `ACL SAVE` 保存到 ACL 文件

## 基本 ACL 命令
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

ACL 是 Redis 安全性的重要组成部分，特别适合多用户共享的 Redis 环境。

# 第九章Redis7 + ACL的连接方式
<img src="https://cdn.nlark.com/yuque/0/2025/jpeg/21376908/1757681056420-39d1bc52-55fe-4f3b-8183-b4d7ba79b166.jpeg" width="4308" title="" crop="0,0,1,1" id="EFbBu" class="ne-image" style="font-size: 16px">

## 使用 `DefaultJedisClientConfig`
Jedis 4.x 版本推荐使用 `DefaultJedisClientConfig` 配置用户名和密码（ACL 需要用户名+密码，而不仅仅是密码）。

```java
import redis.clients.jedis.Jedis;
import redis.clients.jedis.JedisClientConfig;
import redis.clients.jedis.DefaultJedisClientConfig;

public class JedisACLExample {
    public static void main(String[] args) {
        // Redis 7 + ACL 需要 username + password
        String username = "laodu";  // Redis 默认用户是 "default"，也可能是你自定义的
        String password = "laodu123";
        
        // 使用 DefaultJedisClientConfig 配置
        JedisClientConfig config = DefaultJedisClientConfig.builder()
            .user(username)  // ACL 用户名
            .password(password)  // ACL 密码
            .timeoutMillis(5000)  // 超时时间
            .build();
        
        try (Jedis jedis = new Jedis("192.168.48.200", 6379, config)) {
            // 测试连接
            System.out.println("Ping: " + jedis.ping());
            
            // 执行命令
            jedis.set("key", "value");
            System.out.println("Get key: " + jedis.get("key"));
        }
    }
}
```

## 使用 `JedisPool` + ACL（生产推荐）
生产环境推荐使用连接池，避免频繁创建/销毁连接。

```java
public class JedisPoolACLExample {
    public static void main(String[] args) {
        String username = "laodu";  // 或你的自定义ACL用户
        String password = "laodu123";
        
        // 1. 配置连接池
        JedisPoolConfig poolConfig = new JedisPoolConfig();
        poolConfig.setMaxTotal(10);  // 最大连接数
        poolConfig.setMaxIdle(5);    // 最大空闲连接
        poolConfig.setMinIdle(1);    // 最小空闲连接
        
        // 2. 使用 DefaultJedisClientConfig 配置 ACL
        JedisClientConfig jedisClientConfig = DefaultJedisClientConfig.builder()
            .user(username)
            .password(password)
            .timeoutMillis(5000)
            .build();
        
        // 3. 创建连接池
        try (JedisPool jedisPool = new JedisPool(poolConfig, new HostAndPort("192.168.48.200", 6379), jedisClientConfig);) {
            // 4. 从连接池获取连接
            try (Jedis jedis = jedisPool.getResource()) {
                System.out.println("Ping: " + jedis.ping());
                jedis.set("key", "value");
                System.out.println("Get key: " + jedis.get("key"));
            }
        }
    }
}
```

## 使用 `URI` 方式（支持ACL）
Redis 6+ 支持 `ACL`，可以使用 `redis://` 或 `rediss://`（SSL）格式，包含用户名和密码：

```java
import redis.clients.jedis.Jedis;
import redis.clients.jedis.JedisPool;
import redis.clients.jedis.JedisPoolConfig;
import java.net.URI;

public class JedisURIACLExample {
    public static void main(String[] args) {
        // Redis 7 + ACL 的 URI 格式：redis://username:password@host:port
        String uriString = "redis://laodu:laodu123@192.168.48.200:6379"; 

        // 如果启用TLS/SSL的话，以上的uri写法如下：
        //String uriString = "rediss://laodu:laodu123@192.168.48.200:6379"; 
        
        // 单个连接
        try (Jedis jedis = new Jedis(URI.create(uriString))) {
            System.out.println("Ping: " + jedis.ping());
        }

        // -------------------------连接池方式---------------------------------------
        JedisPoolConfig poolConfig = new JedisPoolConfig();
        try (JedisPool jedisPool = new JedisPool(poolConfig, URI.create(uriString))) {
            try (Jedis jedis = jedisPool.getResource()) {
                jedis.set("key", "value");
                System.out.println("Get key: " + jedis.get("key"));
            }
        }
    }
}
```

## 如果Redis 7启用了TLS/SSL
Redis7并没有默认开启TLS/SSL，开启它之后，密码和数据在网络传输过程中是经过加密的，比较安全。

```java
import redis.clients.jedis.Jedis;
import redis.clients.jedis.JedisClientConfig;
import redis.clients.jedis.DefaultJedisClientConfig;

public class JedisSSLACLExample {
    public static void main(String[] args) {
        String username = "laodu";
        String password = "laodu123";
        
        JedisClientConfig config = DefaultJedisClientConfig.builder()
            .user(username)
            .password(password)
            .ssl(true)  // 启用SSL之后，代码中要添加这一行（如果采用URI的方式，开头协议要写为：rediss://）
            .build();
        
        try (Jedis jedis = new Jedis("192.168.48.200", 6379, config)) {
            System.out.println("Ping: " + jedis.ping());
        }
    }
}
```

## 如何开启TLS/SSL
### Redis 的 TLS/SSL 是干啥的
**<font style="color:rgb(15, 17, 21);">TLS主要保护客户端不被骗，同时保护数据不被偷看。</font>**

### <font style="color:rgb(15, 17, 21);">TLS/SSL 实现原理</font>
1. Redis服务器需要向CA机构申请证书，这个证书相当于现实生活中的营业执照。
2. 营业执照申请下来挂到店里，等于是放到 Redis服务器的某个目录中。
3. 然后 `java` 客户端内置了根证书（用它来验证营业执照真伪），jdk安装之后jdk的目录中就自带了根证书。【**<font style="color:#DF2A3F;">JAVA_HOME\lib\security\cacerts</font>**】
4. 当java客户端发送数据给redis服务器的时候，java客户端会使用根证书验证 Redis 服务器的真伪，如果验证失败，立即中断连接。
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

**<font style="color:#DF2A3F;">这一步在我们最开始安装 Redis 的时候已经完成了。</font>**

### 启用TLS/SSL
**第一步**：生成证书：使用Redis自带的工具gen-test-certs.sh生成证书。切换redis的源码目录下，然后运行如下命令：

```shell
cd utils
./gen-test-certs.sh
```

生成的证书将位于 `utils/tests/tls/` 目录下。

**<font style="color:#DF2A3F;">这里生成的证书是自签名证书哈（仅用于开发和测试，或者说你的项目以后是在局域网中运行的，这种方式完全够用）。</font>**

**<font style="color:#DF2A3F;">生成自签名证书的意思是：自己给自己发证。自己给自己发营业执照。（正常来说这个证书应该是 CA 机构来发证）</font>**

**<font style="color:#DF2A3F;">生产环境下一般是连接云服务商的 Redis，你什么都不用做，服务商已经配好证书了。服务商配置的证书都是 CA 机构给发的。</font>**



**第二步**：在Redis的配置文件中添加以下内容：**<font style="color:#DF2A3F;">把配置文件中的 </font>**`**<font style="color:#DF2A3F;">port 6379</font>**`**<font style="color:#DF2A3F;">注释掉，然后添加以下配置</font>**

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



**第四步**：将redis证书导入Java信任库：**使用 **`**Windows PowerShell**`**，并且使用管理员身份打开**

1. 将生成的 `/root/redis-7.4.2/utils/tests/tls/redis.crt` 文件从centos系统中传送到windows环境下，放到 IDEA 项目的resources目录下。并拷贝该文件的绝对路径。
2. 使用**<font style="color:#DF2A3F;">管理员身份</font>**启动dos命令窗口，执行以下命令：

```plain
keytool.exe -importcert -file /path/redis.crt -alias redis-tls-cert -keystore "JAVA_HOME\lib\security\cacerts" -storepass changeit
```

注意：以上命令中两个路径需要修改，第一个是`/path/redis.crt`，另一个是`JAVA_HOME`。



**注意：当你开启了 SSL 之后，使用 **`**redis-cli**`**再次登录 redis 的时候和之前的方式就不同了：**

```shell
redis-cli --tls -u redis://default:123456@localhost:6379 --insecure
```

# 第十章 Spring Data Redis
<img src="https://cdn.nlark.com/yuque/0/2025/jpeg/21376908/1757681056420-39d1bc52-55fe-4f3b-8183-b4d7ba79b166.jpeg" width="4308" title="" crop="0,0,1,1" id="VkwA4" class="ne-image" style="font-size: 16px">

基于ACL + 密码（**<font style="color:#DF2A3F;">注意：以下案例讲解的是在Redis未启用TLS/SSL的前提下进行的。</font>**）

你需要把 Redis 配置文件中之前添加的内容注释掉，并且将 `port 6379`的注释去掉：

```nginx
# port 0
# tls-port 6379
# tls-cert-file /root/redis-7.4.2/utils/tests/tls/redis.crt
# tls-key-file /root/redis-7.4.2/utils/tests/tls/redis.key
# tls-ca-cert-file /root/redis-7.4.2/utils/tests/tls/ca.crt
# tls-auth-clients no
```

**重启 Redis 服务。**

## SpringBoot 项目配置
### 添加依赖
```xml
<dependency>
  <groupId>org.springframework.boot</groupId>
  <artifactId>spring-boot-starter-data-redis</artifactId>
</dependency>

<!--做连接池优化的-->
<dependency>
  <groupId>org.apache.commons</groupId>
  <artifactId>commons-pool2</artifactId>
  <version>2.12.0</version>
</dependency>
```

### 配置 application.properties
```properties
# Redis 配置
spring.data.redis.host=192.168.48.200
spring.data.redis.port=6379
spring.data.redis.password=123456
spring.data.redis.username=default
spring.data.redis.lettuce.pool.enabled=true
spring.data.redis.lettuce.pool.max-active=8
spring.data.redis.lettuce.pool.max-idle=8
spring.data.redis.lettuce.pool.min-idle=0
spring.data.redis.lettuce.pool.max-wait=-1ms
```

## 创建 Redis 配置类
可以创建一个配置类：

```java
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.data.redis.connection.RedisConnectionFactory;
import org.springframework.data.redis.core.RedisTemplate;
import org.springframework.data.redis.serializer.GenericJackson2JsonRedisSerializer;
import org.springframework.data.redis.serializer.StringRedisSerializer;

@Configuration
public class RedisConfig {
    @Bean
    public RedisTemplate<String, Object> redisTemplate(RedisConnectionFactory connectionFactory) {
        RedisTemplate<String, Object> template = new RedisTemplate<>();
        template.setConnectionFactory(connectionFactory);

        // 设置string/list/set/zset类型的序列化器
        // 使用 String 序列化器序列化 key
        template.setKeySerializer(new StringRedisSerializer());
        // 使用 Jackson 序列化器序列化 value
        template.setValueSerializer(new GenericJackson2JsonRedisSerializer());

        // 设置hash类型的序列化器
        template.setHashKeySerializer(new StringRedisSerializer());
        template.setHashValueSerializer(new GenericJackson2JsonRedisSerializer());

        return template;
    }
}
```



**<font style="color:#DF2A3F;">序列化器的作用</font>**：将Java对象与Redis存储的二进制数据互相转换

1. key用字符串序列化（方便查看）
2. value用JSON序列化（可存复杂对象）

## RedisTemplate
**<font style="color:#000000;">RedisTemplate是 Spring Data Redis 框架提供的：（Spring Data Redis 是 Spring Data 的一部分，SpringBoot 框架自动集成了 Spring Data，这是他们三者的关系。）</font>**

+ <font style="color:#DF2A3F;">底层可以使用 </font>**<font style="color:#000000;">Jedis</font>**<font style="color:#000000;"> </font><font style="color:#DF2A3F;">或 </font>**<font style="color:#000000;">Lettuce</font>**<font style="color:#DF2A3F;"> 作为客户端</font>
+ <font style="color:#DF2A3F;">自动管理连接池和资源</font>
+ <font style="color:#DF2A3F;">提供更面向对象的操作方式</font>
+ <font style="color:#DF2A3F;">内置序列化支持</font>
+ <font style="color:#DF2A3F;">与 Spring 生态无缝集成</font>

**<font style="color:rgb(15, 17, 21);"></font>**

**<font style="color:rgb(15, 17, 21);">RedisTemplate 设计了两层 API：</font>**

**<font style="color:rgb(15, 17, 21);">第一层：Template自身方法（管理类操作）</font>**

```java
// 这些是"模板级"操作，不需要指定数据类型
redisTemplate.hasKey("key")          // 是否存在key
redisTemplate.delete("key")          // 删除key
redisTemplate.expire("key", 10, TimeUnit.SECONDS) // 设置过期
redisTemplate.type("key")            // 获取key类型
redisTemplate.keys("user:*")         // 模式匹配查询
redisTemplate.getConnectionFactory() // 获取连接工厂
redisTemplate.execute(...)           // 执行自定义操作
```

**第二层：Operations接口（数据类操作）**

```java
// 这些是"数据操作"，需要先指定操作哪种数据结构
redisTemplate.opsForValue().set("key", "value")      // String操作
redisTemplate.opsForList().leftPush("list", "item")  // List操作  
redisTemplate.opsForSet().add("set", "member")       // Set操作
redisTemplate.opsForHash().put("hash", "field", "val") // Hash操作
redisTemplate.opsForZSet().add("zset", "member", 100) // ZSet操作
```

## <font style="color:rgb(64, 64, 64);">创建业务类</font>
创建一个服务类来演示 Redis 操作：

```java
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.redis.core.RedisTemplate;
import org.springframework.stereotype.Service;

import java.util.concurrent.TimeUnit;

@Service
public class RedisService {

    @Autowired
    private RedisTemplate<String, Object> redisTemplate;

    public void setValue(String key, Object value) {
        redisTemplate.opsForValue().set(key, value);
    }

    public void setValueEx(String key, Object value, long timeout, TimeUnit unit) {
        redisTemplate.opsForValue().set(key, value, timeout, unit);
    }

    public Object getValue(String key) {
        return redisTemplate.opsForValue().get(key);
    }

    public Boolean deleteKey(String key) {
        return redisTemplate.delete(key);
    }

    public Boolean hasKey(String key) {
        return redisTemplate.hasKey(key);
    }
}

```

## 创建控制器测试 Redis
```java
import com.laodu.demo.service.RedisService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

@RequestMapping("/api/redis")
@RestController
public class RedisController {

    @Autowired
    private RedisService redisService;

    @PostMapping("/set")
    public String setValue(@RequestParam String key, @RequestParam String value) {
        redisService.setValue(key, value);
        return "set key-value success : " + key + "=" + value;
    }

    @GetMapping("/get/{key}")
    public Object getValue(@PathVariable("key") String key) {
        return redisService.getValue(key);
    }

    @DeleteMapping("/delete/{key}")
    public String deleteKey(@PathVariable("key") String key) {
        redisService.deleteKey(key);
        return "delete success : " + key;
    }

    @GetMapping("/has/{key}")
    public String hasKey(@PathVariable("key") String key) {
        return redisService.hasKey(key) ? "存在" + key : "不存在" + key;
    }

}
```

## 测试接口
1. 启动 SpringBoot 应用
2. 使用curl 测试接口：
    - curl -X POST "[http://localhost:8080/api/redis/set"](http://localhost:8080/api/redis/set") -d "key=test&value=hello"
    - curl "[http://localhost:8080/api/redis/get/test](http://localhost:8080/api/redis/get/test)"
    - curl -X DELETE "[http://localhost:8080/api/redis/delete/test"](http://localhost:8080/api/redis/delete?key=test")
    - curl "[http://localhost:8080/api/redis/has/test"](http://localhost:8080/api/redis/hasKey?key=test")

# 第十一章Redis的持久化
<img src="https://cdn.nlark.com/yuque/0/2025/jpeg/21376908/1757681056420-39d1bc52-55fe-4f3b-8183-b4d7ba79b166.jpeg" width="4308" title="" crop="0,0,1,1" id="oxJbe" class="ne-image" style="font-size: 16px">

Redis提供了两种持久化：

1. 第一种：RDB（Redis DataBase）,默认情况下这种方式就是启动的。(全量备份)
2. 第二种：AOF（Append Only File），默认情况下这种方式不开启。（增量备份）

## RDB
### 什么是RDB？
在指定的**<font style="color:#DF2A3F;">时间间隔</font>**内将内存中的**<font style="color:#DF2A3F;">数据集快照</font>**写入磁盘。恢复数据时会将当时的快照文件直接导入到内存中。

+ 时间间隔：例如每隔1小时，每隔5分钟，每隔1分钟等。
+ 数据集快照：当前时间点下的Redis缓存中的数据。



提示：

1. RDB以二进制的格式存储数据。
2. 文件名默认：dump.rdb（可配置）
3. 文件存放目录默认和`redis-server`在同级目录下。（可配置）

### 怎么触发 RDB 快照
#### 手动触发
使用 `redis-cli SAVE` 命令或 `redis-cli BGSAVE` 命令。

+ redis-cli SAVE 会阻塞服务器直到 RDB 文件创建完毕
+ redis-cli BGSAVE 会创建一个子进程来处理 RDB 文件的创建，不会阻塞服务器。

#### 自动触发
在`redis.conf`文件中进行如下配置，方可开启自动触发。

例如，可以配置在满足一定条件下（如多少秒内有多少次写操作）自动执行 BGSAVE。

```nginx
save 3600 1           # 在1小时内至少有1次写操作，则执行BGSAVE
save 300 100          # 在5分钟内至少有100次写操作，则执行BGSAVE
save 60 10000       # 在1分钟内至少有10000次写操作，则执行BGSAVE
```

以上的配置是Redis7的默认配置。

**<font style="color:#DF2A3F;">可以通过这个命令查看当前的 配置情况：</font>**

```shell
redis-cli CONFIG GET save
```



**<font style="color:#DF2A3F;">触发逻辑：</font>**

假设配置信息`save 30 3`，那么它的触发逻辑是：

1. 从用户的第一次`写操作`开始计时，并记录写的次数为1。
2. Redis 内部有一个周期性任务（默认每 100 毫秒检查一次）。
3. 检查内容：当 `**计时器 >= 30秒 并且 写的次数 >= 3**`条件成立时，则触发RDB快照。
4. 底层只要开始执行 `BGSAVE`命令，计时器就立即进入下一个计时周期。（**注意：不会等 BGSAVE 执行结束后才进入下一个计时周期**）
5. 当下一个计时周期达到，并且满足写的次数，会再次执行 `BGSAVE`保存。（**小细节：如果上一次的 BGSAVE 执行比较耗时，超过了下一个计时周期，那么新的执行周期对应的 BGSAVE 会延迟执行**）

### RDB备份的执行过程
当执行`BGSAVE`命令时，redis会单独`fork`一个子进程（**fork可以理解为复刻/复制一个和主进程完全一样的进程，这表示主进程不进行任何IO操作，确保redis极高性能**），该进程会将当下redis内存中的数据写入到一个**<font style="color:#DF2A3F;">临时文件</font>**中，当内存中的数据全部同步到临时文件后，临时文件再替换上一次的`dump.rdb`。



为什么要用临时文件？而不是直接写入dump.rdb文件？

| **方式** | **直接写入dump.rdb** | **临时文件 + 原子替换** |
| --- | --- | --- |
| **<font style="color:rgb(64, 64, 64);">崩溃一致性</font>** | <font style="color:rgb(64, 64, 64);">可能生成部分损坏的 RDB 文件</font> | <font style="color:rgb(64, 64, 64);">旧文件始终完整，新文件全量校验</font> |
| **<font style="color:rgb(64, 64, 64);">并发安全</font>** | <font style="color:rgb(64, 64, 64);">其他进程可能读取到不完整文件</font> | <font style="color:rgb(64, 64, 64);">替换是原子操作，无中间状态</font> |
| **<font style="color:rgb(64, 64, 64);">实现复杂度</font>** | <font style="color:rgb(64, 64, 64);">需额外逻辑处理中断恢复</font> | <font style="color:rgb(64, 64, 64);">简单可靠</font> |




另外大家再思考一个问题：上述描述中提到子进程会将内存中的数据写入到一个临时文件中，那如果在写到临时文件的过程中**主进程又进行了写操作**，内存中的数据又变化了，子进程会把变化后的数据写入到临时文件中吗？不会的。永远要记住，RDB备份的是内存快照，备份的是某一个时刻的内存数据。快照是如何实现的呢？**<font style="color:#DF2A3F;">底层使用了写时复制技术（著名的COW技术：Copy On Write）</font>**。



**<font style="color:#DF2A3F;">写时复制技术原理</font>**

1. fork() 机制：
+ 当触发 RDB 持久化时，Redis 主进程会调用 fork() 创建一个子进程。子进程与父进程共享相同的内存数据（物理内存页）
2. 写操作触发复制（写时复制）：
+ 读操作：父子进程继续共享内存页。
+ 写操作：当父进程修改某块数据时，<font style="color:rgb(64, 64, 64);">操作系统</font>**<font style="color:rgb(64, 64, 64);">复制该内存页</font>**<font style="color:rgb(64, 64, 64);">，主进程修改副本，子进程仍读原页（</font>**<font style="color:rgb(64, 64, 64);">这里的原页可以理解为内存快照</font>**<font style="color:rgb(64, 64, 64);">）</font>。



**COW 的一个形象的比喻：**

```plain
📚 实体书 = 物理内存
📇 借书卡A = 主进程的页表
📇 借书卡B = 子进程的页表（fork产生）
👤 我 = Redis主进程（处理写请求）
👥 哥们 = Redis子进程（负责备份）

✅ 动作：
1. 我要改书（主进程SET）
2. 不能直接改实体书（因为哥们看着）
3. 复印我改的那一页（COW复制内存页）
4. 我改复印页（主进程写入新副本）
5. 哥们继续看原页（子进程保持原数据）
```

### RDB备份之后的数据如何恢复
redis服务在启动之后，自动去找`redis.conf`配置文件中配置的`dump.rdb`文件，自动恢复数据到内存中。

### RDB缺点
1. **数据丢失风险**  
    - 最后一次快照之后的数据可能丢失（因故障宕机时，未到达下一次持久化时间点的数据会永久消失）
2. **性能影响**  
    - 生成快照时会 fork 子进程，数据集过大时可能导致 Redis 服务短暂阻塞
3. **实时性不足**  
    - 仅支持定时持久化，无法像 AOF 那样实现秒级数据安全
4. **版本兼容性问题**  
    - 老版本 Redis 生成的 RDB 文件可能无法兼容新版本
5. **存储空间不灵活**  
    - **<font style="color:#DF2A3F;">全量备份</font>**机制下，单个 RDB 文件体积较大（相比 **<font style="color:#DF2A3F;">AOF 的增量</font>**日志）

### RDB的相关配置
在`redis.conf`中搜索`SNAPSHOTTING`：

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1745741263297-3640a662-d51f-4baf-80dc-ef7c89e810e4.png" width="684.6666666666666" title="" crop="0,0,1,1" id="w5EON" class="ne-image" style="font-size: 16px">



设置RDB备份规则：

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1745741349504-4deafda3-29f2-49aa-bf0a-656f5714edcb.png" width="910" title="" crop="0,0,1,1" id="SfE1b" class="ne-image" style="font-size: 16px">

以上英文翻译为：你可以通过取消以下行的注释来显式设置这些参数



设置文件名：

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1745741519632-ca08fd8a-6006-4b3a-818e-0910f489abb9.png" width="468" title="" crop="0,0,1,1" id="LktZE" class="ne-image" style="font-size: 16px">



设置存储目录：

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1745741537046-e3d391b4-67f7-4172-aa9b-6de3ac5e979e.png" width="870.6666666666666" title="" crop="0,0,1,1" id="roiLw" class="ne-image" style="font-size: 16px">



设置备份失败是否停止写入：默认是yes，表示RDB备份失败后，redis的set、hset、lpush等写操作将无法使用。但读取命令仍然可用。

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1745743128857-eadb29b8-c677-470e-af48-9c878f3429b3.png" width="966" title="" crop="0,0,1,1" id="JX6xn" class="ne-image" style="font-size: 16px">



设置是否压缩rdb文件：默认yes

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1745743220390-7b464357-3402-4af3-8e8a-a7fa2c0371ed.png" width="985.3333333333334" title="" crop="0,0,1,1" id="c3zAW" class="ne-image" style="font-size: 16px">

当配置 rdbcompression yes（默认开启）时，Redis 在生成 RDB 快照文件（如 dump.rdb）时会对数据进行二进制压缩，显著减少磁盘占用。

Redis 使用 LZF 压缩算法（一种轻量级实时压缩算法）。修改算法的话就需要修改Redis的源码。



设置是否校验RDB文件的完整性：默认是yes

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1745743292281-131a9239-b3d2-44be-bf6e-95ea1a76da28.png" width="1059.3333333333333" title="" crop="0,0,1,1" id="MJkfq" class="ne-image" style="font-size: 16px">

当配置 rdbchecksum yes（默认开启）时，Redis 会在 RDB 文件末尾 写入一个 CRC64 校验和（8字节）。

主要用于在 加载 RDB 文件时验证数据完整性，防止因磁盘损坏、传输错误或文件篡改导致的数据异常。



**以下是生产环境下的建议配置：**

| **参数** | **推荐值** | **说明** |
| --- | --- | --- |
| `<font style="color:rgb(64, 64, 64);">save</font>` | `<font style="color:rgb(64, 64, 64);">save 900 1</font>`<font style="color:rgb(64, 64, 64);">   </font>`<font style="color:rgb(64, 64, 64);">save 300 10</font>`<font style="color:rgb(64, 64, 64);">   </font>`<font style="color:rgb(64, 64, 64);">save 60 10000</font>` | **<font style="color:rgb(64, 64, 64);">多级备份规则</font>**<font style="color:rgb(64, 64, 64);">：</font><br/>+ <font style="color:rgb(64, 64, 64);">15分钟1次修改 → 备份</font><br/>+ <font style="color:rgb(64, 64, 64);">5分钟10次修改 → 备份</font><br/>+ <font style="color:rgb(64, 64, 64);">1分钟1万次修改 → 备份</font> |
| `<font style="color:rgb(64, 64, 64);">stop-writes-on-bgsave-error</font>` | `<font style="color:rgb(64, 64, 64);">yes</font>` | **<font style="color:rgb(64, 64, 64);">备份失败时拒绝写入</font>**<font style="color:rgb(64, 64, 64);">，避免数据不一致（需配合监控）。</font> |
| `<font style="color:rgb(64, 64, 64);">rdbcompression</font>` | `<font style="color:rgb(64, 64, 64);">yes</font>` | **<font style="color:rgb(64, 64, 64);">启用压缩</font>**<font style="color:rgb(64, 64, 64);">（LZF算法），减少磁盘占用（CPU换空间）。</font> |
| `<font style="color:rgb(64, 64, 64);">rdbchecksum</font>` | `<font style="color:rgb(64, 64, 64);">yes</font>` | **<font style="color:rgb(64, 64, 64);">启用CRC64校验</font>**<font style="color:rgb(64, 64, 64);">，防止损坏的RDB文件被加载。</font> |
| `<font style="color:rgb(64, 64, 64);">dbfilename</font>` | `<font style="color:rgb(64, 64, 64);">dump-${port}.rdb</font>` | **<font style="color:rgb(64, 64, 64);">按端口命名文件</font>**<font style="color:rgb(64, 64, 64);">（多实例部署时避免冲突）。</font> |
| `<font style="color:rgb(64, 64, 64);">dir</font>` | `<font style="color:rgb(64, 64, 64);">/data/redis/rdb</font>` | **<font style="color:rgb(64, 64, 64);">指定备份目录</font>**<font style="color:rgb(64, 64, 64);">：</font><br/>+ <font style="color:rgb(64, 64, 64);">使用独立磁盘分区</font><br/>+ <font style="color:rgb(64, 64, 64);">避免与AOF日志混存</font> |


### RDB选择建议
如果需要快速恢复大数据集，并且对数据恢复的完整性不是非常敏感，可以选择RDB方式。

为什么这种方式恢复的快？因为这种方式生成的dump.rdb文件是一个紧凑的二进制文件

## AOF
### 什么是AOF
AOF（Append-Only File）以日志的形式来记录每个写操作，将Redis执行过的所有**<font style="color:#DF2A3F;">写指令</font>**记录下来，读操作不记录，只许以追加的方式写入aof文件。（AOF文件中记录的时候以普通文本形式记录，将所有的写的操作命令记录到日志文件中。）

Redis启动时，会读取aof文件，然后将aof文件中的所有指令全部执行一次，以完成数据的恢复。

AOF支持秒级实时同步，但文件体积较大，恢复速度慢于RDB。（因为AOF文件是普通文本文件，不是二进制文件，另外也需要让所有的指令从头到尾执行一遍，因此恢复较慢。）

### 开启AOF功能
默认情况下AOF是不开启的。

修改配置来开启AOF：

```nginx
appendonly yes
```



### AOF文件名及存储目录
**Redis7之前**只有以下这一项配置，设置文件名：

```nginx
appendfilename "appendonly.aof"
```

会在redis的`/usr/local/bin`目录下生成`appendonly.aof`文件。



**Redis7之后**有以下两项配置：

第一项配置：设置文件名，这一项配置在redis7+之后不起作用。依然保留的原因是为了兼容旧版本。

```nginx
appendfilename "appendonly.aof"
```



第二项配置：设置存储目录，这是Redis7的新特性，新增的配置。

```nginx
appenddirname "appendonlydir"
```

会在redis的`/usr/local/bin`目录下新建`appendonlydir`目录，在该目录下存储以下三类文件：

+ xxx.**<font style="color:#DF2A3F;">base.rdb</font>**
+ xxx.**<font style="color:#DF2A3F;">incr.aof</font>**
+ xxx.**<font style="color:#DF2A3F;">manifest</font>**



### base.rdb、incr.aof、manifest文件
在高版本 Redis（7.0+）中，`appenddirname "appendonlydir"` 表示 **AOF 文件的存储目录**，但文件结构与传统 AOF 不同，采用了**多文件混合持久化**设计。以下是对**AOF 分段存储机制**的具体解释：



#### 文件作用说明
| 文件名 | 类型 | 作用 |
| --- | --- | --- |
| `appendonly.aof.1.base.rdb` | **RDB 文件** | 全量数据快照（AOF 重写时生成，二进制压缩格式，体积小，恢复速度快） |
| `appendonly.aof.1.incr.aof` | **AOF 文件** | 增量写命令（记录 `base.rdb` 后的新操作，文本格式，实时性强） |
| `appendonly.aof.manifest` | **清单文件** | 记录当前有效的 `base.rdb` 和 `incr.aof` 组合（JSON 格式，维护文件关系） |




#### 设计原理（Redis 7.0+）
+ **混合持久化**：  
    - **<font style="color:rgb(15, 17, 21);">混合持久化</font>**<font style="color:rgb(15, 17, 21);">就是</font>**<font style="color:rgb(15, 17, 21);">用RDB格式存“老数据”快照（base.rdb），用AOF格式存“新变动”日志（incr.aof），重启时先读快照再补日志，实现又快又全的恢复</font>**<font style="color:rgb(15, 17, 21);">。</font>
+ **分段滚动更新**：  
    - <font style="color:rgb(15, 17, 21);">“分段”体现在将完整数据</font>**<font style="color:rgb(15, 17, 21);">拆成基础快照(base.rdb)和增量日志(incr.aof)两个文件</font>**<font style="color:rgb(15, 17, 21);">；</font>
    - <font style="color:rgb(15, 17, 21);">“滚动”体现在通过</font>**<font style="color:rgb(15, 17, 21);">原子切换清单(manifest)</font>**<font style="color:rgb(15, 17, 21);">来版本升级，像翻书一样无感更替。</font>



#### 文件生成逻辑
1. **首次启用 AOF**：  
    - 生成 `base.rdb`（全量数据） + 空的 `incr.aof`。
2. **写入新命令**：  
    - 增量操作追加到 `incr.aof`（如 `SET`/`DEL`）。
3. **触发 AOF 重写**：  
    - 创建新的 `base.rdb`（当前数据快照）和新的 `incr.aof`，更新 `manifest`。

****

#### 生产环境建议
+ **不要手动删除文件**：依赖 Redis 自动管理（通过 `manifest` 维护）。  
+ **备份策略**：同时备份 `appendonlydir/` 整个目录（需包含 `manifest` 文件）。

****

#### 与传统 AOF 的对比
| **特性** | **旧版 AOF（单文件）** | **Redis 7.0+ AOF（多文件）** |
| --- | --- | --- |
| **文件结构** | 单一 `.aof` 文本文件 | `base.rdb` + `incr.aof` + `manifest` |
| **恢复速度** | 慢（需重放所有命令） | 快（优先加载 `base.rdb`） |
| **磁盘占用** | 较大（纯文本） | 更小（RDB 压缩 + 增量 AOF） |
| **兼容性** | 所有版本 | Redis 7.0+ |


### 怎么触发AOF？
在 Redis 7 及更高版本中，**AOF（Append-Only File）持久化的触发方式**分为 **自动触发** 和 **手动触发** 两种，以下是详细说明：

#### 手动触发
手动执行这个命令：redis-cli BGREWRITEAOF



执行该命令后，查看文件是否更新：

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1745925753085-47a5c470-d3f4-4f8e-bbff-1a3d74f32f29.png" width="959" title="" crop="0,0,1,1" id="u3ebab243" class="ne-image" style="font-size: 16px">

#### 自动触发
1. **<font style="color:#DF2A3F;"></font>****实时写入（默认开启）**

+ 每个写命令（如 `SET`、`DEL`）会立即追加到 **增量 AOF 文件**（`appendonly.aof.?.incr.aof`），由 `appendfsync` 控制刷盘策略：

```nginx
appendfsync always   # 每个命令刷盘（最安全，性能最低）
appendfsync everysec # 每秒刷盘（默认推荐）
appendfsync no       # 依赖操作系统刷盘（最快，可能丢数据）
```

2. **AOF 重写（满足条件时自动触发）**

+ **触发条件**：  
    - 根据 `auto-aof-rewrite-percentage` 和 `auto-aof-rewrite-min-size` 参数判断：  **<font style="color:#DF2A3F;">两个是并且关系，同时满足时才会触发 AOF 重写。</font>**

```nginx
auto-aof-rewrite-percentage 100  # 当前AOF文件比上次重写后增长100%时触发
auto-aof-rewrite-min-size 64mb   # AOF文件最小达到64MB才触发
```

+ **重写过程**：  
    1. 创建子进程，生成 **全量数据的 RDB 快照**（写入 `appendonly.aof.1.base.rdb`）。  
    2. 后续增量命令写入新的 `incr.aof` 文件。  
    3. 更新 `manifest` 文件记录有效文件组合。

#### 总结
Redis 7+ 的 AOF 触发机制通过 **<font style="color:#DF2A3F;">实时追加 + 条件化重写</font>** 实现，结合 RDB 快照提升性能。多文件设计解决了传统 AOF 体积过大和恢复慢的问题，同时保持数据安全性。

### RDB和AOF同时开启会怎样
在 Redis 7 及更高版本中，**当 RDB 和 AOF 持久化同时开启时，Redis 会同时维护两种持久化机制**，但它们的用途和触发逻辑是独立的，具体行为如下：

#### 同时开启时的关键行为
**(1) 数据写入流程**

+ **AOF 优先**：所有写命令会**实时追加到 AOF 文件**（`incr.aof`），确保操作日志不丢失。  
+ **RDB 异步触发**：根据 `save` 配置或手动命令生成快照，**不影响 AOF 的实时记录**。

**(2) 数据恢复流程**

+ **重启加载时**：Redis 会**优先加载 AOF 文件**（因为 AOF 记录更完整），仅当 AOF 关闭或文件不存在时才会加载 RDB。  

#### 注意事项
+ **磁盘空间**：同时开启会占用更多存储（需监控 `dir` 目录）。  
+ **性能影响**：RDB 的 `BGSAVE` 和 AOF 的 `BGREWRITEAOF` **不会同时运行**（Redis 内部有任务调度机制）。

#### 如何验证当前持久化状态？
```bash
# 检查 RDB 最后一次保存时间
redis-cli INFO PERSISTENCE | grep rdb_last_save_time

# 检查 AOF 是否生效
redis-cli INFO PERSISTENCE | grep aof_enabled

# 查看 AOF 文件类型（Redis 7+）
# ls -lh 这里的linux命令中带了 -h 参数，这样文件大小显示更加人性化。这个参数和redis没有关系。
ls -lh /usr/local/bin/appendonlydir/
```

#### 总结
**<font style="color:#DF2A3F;">在 Redis 7+ 中，RDB 和 AOF 同时开启时会并行工作，但 AOF 在数据恢复时优先级更高。推荐生产环境同时启用两者，利用 RDB 的快照优势和 AOF 的实时安全性，并通过 </font>**`**<font style="color:#DF2A3F;">aof-use-rdb-preamble</font>**`**<font style="color:#DF2A3F;"> 进一步优化性能。</font>**

### AOF的所有建议配置
以下是 Redis 7 中 AOF（Append Only File）持久化相关配置的整理，并附上生产环境建议配置：

| **配置项** | **白话描述** | **生产环境建议** |
| --- | --- | --- |
| `appendonly` | 是否开启 AOF 持久化，默认不开启（RDB是默认的）。 | 如果需要高数据安全性，建议设为 `yes`。 |
| `appendfilename` | AOF 文件的名称，默认是 `appendonly.aof`。 | 通常不用改，保持默认即可。 |
| `appendfsync` | 控制 AOF 文件同步到磁盘的频率：   - `no`：让操作系统决定何时同步（最快但最不安全）。   - `everysec`：每秒同步一次（折中方案，默认值）。   - `always`：每次写命令都同步（最安全但最慢）。 | 推荐 `everysec`，兼顾性能和数据安全。如果对数据一致性要求极高（如金融场景），可以用 `always`，但性能会下降。 |
| `no-appendfsync-on-rewrite` | AOF 重写时是否禁止 `fsync`（同步到磁盘），默认 `no`（允许同步）。如果设为 `yes`，重写期间可能丢失数据，但能减轻磁盘 I/O 压力。 | 如果对数据丢失有一定容忍度（如缓存场景），可以设为 `yes` 提升性能。否则保持 `no`。 |
| `auto-aof-rewrite-percentage` | AOF 文件比上次重写后增长多少百分比时触发重写（默认 `100%`，即翻倍）。 | 保持默认即可，或根据磁盘空间调整（如设为 `80%` 更频繁重写）。 |
| `auto-aof-rewrite-min-size` | AOF 文件至少达到多大才会触发重写（默认 `64MB`）。 | 生产环境建议调大（如 `1GB`），避免频繁重写小文件。 |
| `aof-load-truncated` | 如果 AOF 文件末尾损坏（比如服务器突然崩溃），是否加载截断的文件（默认 `yes`）。 | 保持 `yes`，至少能恢复大部分数据。如果对完整性要求极高，可以设为 `no` 并配合人工修复。 |
| `aof-use-rdb-preamble` | 是否启用混合模式。默认值 yes（这就是我们上面所说的新特性） | 强烈建议保持 `yes`，兼顾速度和可读性。 |
| `aof-rewrite-incremental-fsync` | AOF 重写时是否分批同步数据到磁盘（默认 `yes`），避免单次 `fsync` 卡顿。 | 保持 `yes`，减少对主线程的影响。 |


# 第十二章Spring Cache 搭建高速缓存
<img src="https://cdn.nlark.com/yuque/0/2025/jpeg/21376908/1757681056420-39d1bc52-55fe-4f3b-8183-b4d7ba79b166.jpeg" width="4308" title="" crop="0,0,1,1" id="aIjOF" class="ne-image" style="font-size: 16px">

使用`SpringBoot3 + MySQL8 + Redis7 + MyBatisPlus`实现高速缓存。

所谓的高速缓存指的是，查询时先从Redis缓存中读取，如果没有再从数据库中获取，获取到之后，将数据放入Redis缓存，以备下次使用。

## 项目配置
### 添加依赖
确保pom.xml包含以下依赖：

```xml
<dependencies>
    <!-- Spring Boot Starter -->
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-web</artifactId>
    </dependency>
    
    <!-- Redis -->
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-data-redis</artifactId>
    </dependency>
    
    <!-- MySQL -->
    <dependency>
        <groupId>com.mysql</groupId>
        <artifactId>mysql-connector-j</artifactId>
        <scope>runtime</scope>
    </dependency>
    
    <!-- MyBatis-Plus -->
    <dependency>
                        <groupId>com.baomidou</groupId>
                        <artifactId>mybatis-plus-spring-boot3-starter</artifactId>
                        <version>3.5.11</version>
                </dependency>
    
    <!-- Lombok -->
    <dependency>
        <groupId>org.projectlombok</groupId>
        <artifactId>lombok</artifactId>
        <optional>true</optional>
    </dependency>
    
    <!-- 测试 -->
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-test</artifactId>
        <scope>test</scope>
    </dependency>
</dependencies>

```

### 配置文件
`application.yml`配置：

```yaml
server:
  port: 8080

spring:
  datasource:
    driver-class-name: com.mysql.cj.jdbc.Driver
    url: jdbc:mysql://localhost:3306/cache_demo?useSSL=false&serverTimezone=Asia/Shanghai&characterEncoding=utf8
    username: root
    password: 123456

  data:
    redis:
      host: 192.168.48.200
      port: 6379
      username: default
      password: 123456
      database: 0
      lettuce:
        pool:
          max-active: 8
          max-wait: -1ms
          max-idle: 8
          min-idle: 0
      timeout: 5000ms

mybatis-plus:
  configuration:
    log-impl: org.apache.ibatis.logging.stdout.StdOutImpl
  global-config:
    db-config:
      id-type: auto
      logic-delete-field: deleted
      logic-delete-value: 1
      logic-not-delete-value: 0
```

## 数据库准备
cache_demo.sql

```sql
CREATE DATABASE IF NOT EXISTS cache_demo DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

USE cache_demo;

CREATE TABLE IF NOT EXISTS product (
    id BIGINT NOT NULL AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    price DECIMAL(10,2) NOT NULL,
    stock INT NOT NULL,
    create_time DATETIME DEFAULT CURRENT_TIMESTAMP,
    update_time DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    deleted TINYINT(1) DEFAULT 0,
    PRIMARY KEY (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

INSERT INTO product (name, price, stock) VALUES 
('iPhone 15', 9999.00, 100),
('MacBook Pro', 14999.00, 50),
('AirPods Pro', 1999.00, 200);
```

## 代码实现
### 实体类
```java
package com.laodu.cache.model.po;

import com.baomidou.mybatisplus.annotation.*;
import lombok.Data;

import java.math.BigDecimal;
import java.util.Date;

@Data
@TableName("product")
public class Product {
    @TableId(value = "id", type = IdType.AUTO)
    private Long id;
    private String name;
    private BigDecimal price;
    private Integer stock;

    @TableField(fill = FieldFill.INSERT) // 执行insert操作时自动填充
    private Date createTime;

    @TableField(fill = FieldFill.INSERT_UPDATE) // 执行insert和update操作时自动填充
    private Date updateTime;

    @TableLogic
    private Integer deleted;
}
```

### Mapper接口
```java
package com.laodu.cache.mapper;

import com.baomidou.mybatisplus.core.mapper.BaseMapper;
import com.laodu.cache.model.po.Product;

public interface ProductMapper extends BaseMapper<Product> {
}
```

### Service层
接口

```java
package com.laodu.cache.service;

import com.baomidou.mybatisplus.extension.service.IService;
import com.laodu.cache.model.po.Product;

public interface ProductService extends IService<Product> {
    Product getProductById(Long id);

    Product updateProduct(Product product);

    boolean removeProductById(Long id);
}

```

实现类

```java
package com.laodu.cache.service.impl;

import com.baomidou.mybatisplus.extension.service.impl.ServiceImpl;
import com.laodu.cache.mapper.ProductMapper;
import com.laodu.cache.model.po.Product;
import com.laodu.cache.service.ProductService;
import org.springframework.cache.annotation.CacheEvict;
import org.springframework.cache.annotation.CachePut;
import org.springframework.cache.annotation.Cacheable;
import org.springframework.stereotype.Service;

@Service
public class ProductServiceImpl extends ServiceImpl<ProductMapper, Product> implements ProductService {

    // 1.@Cacheable注解是spring框架提供的，专门用于整合缓存数据库而存在的注解。
    // 2.该注解作用是：从缓存中读取数据，如果缓存中没有数据就从数据库中取数据，取到的数据放入缓存中。
    // 3.放入Redis缓存中的数据都需要设置key，该注解中的value和key属性联合起来生成Redis的key
    // 4.假设商品id是123，则生成的Redis的key是：product::123，两个冒号是Spring Cache的默认规则。
    // 5. #id 中的 #是SpEL语法规则，表示将参数id拿到后放到这里。如果取参数，则必须使用 # 开头。
    // 6. @Cacheable 优先读缓存，缓存不存在才执行方法。
    @Override
    @Cacheable(value = "product", key = "#id")
    public Product getProductById(Long id) {
        System.out.println("查询数据库获取产品，ID：" + id);
        return getById(id);
    }

    // 1. @CachePut 这个注解标注的方法，每一次都会执行该方法。
    // 2. 方法执行时更新数据库，然后将方法的返回值更新Redis缓存。
    @Override
    @CachePut(value = "product", key = "#product.id")
    public Product updateProduct(Product product) {
        System.out.println("更新数据库中的产品，ID：" + product.getId());
        updateById(product);
        return product;
    }

    // 1. @CacheEvict 执行该方法后清除缓存。
    @Override
    @CacheEvict(value = "product", key = "#id")
    public boolean removeProductById(Long id) {
        System.out.println("删除数据库中的产品，ID：" + id);
        return removeById(id);
    }
}

```

### 控制器
```java
package com.laodu.cache.controller;

import com.laodu.cache.model.po.Product;
import com.laodu.cache.service.ProductService;
import lombok.RequiredArgsConstructor;
import org.springframework.web.bind.annotation.*;

@RequestMapping("/product")
@RestController
@RequiredArgsConstructor
public class ProductController {
    private final ProductService productService;

    @GetMapping("/{id}")
    public Product getProductById(@PathVariable Long id) {
        return productService.getProductById(id);
    }

    @PutMapping
    public Product modifyProduct(@RequestBody Product product) {
        return productService.updateProduct(product);
    }

    @DeleteMapping("/{id}")
    public boolean removeById(@PathVariable Long id) {
        return productService.removeProductById(id);
    }
}


```

### 缓存配置类
```java
package com.laodu.cache.config;

import org.springframework.cache.annotation.EnableCaching;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.data.redis.cache.RedisCacheConfiguration;
import org.springframework.data.redis.cache.RedisCacheManager;
import org.springframework.data.redis.connection.RedisConnectionFactory;
import org.springframework.data.redis.serializer.GenericJackson2JsonRedisSerializer;
import org.springframework.data.redis.serializer.RedisSerializationContext;
import org.springframework.data.redis.serializer.StringRedisSerializer;

import java.time.Duration;

@Configuration
@EnableCaching
public class RedisConfig {

    @Bean
    public RedisCacheManager cacheManager(RedisConnectionFactory connectionFactory) {
        RedisCacheConfiguration config = RedisCacheConfiguration.defaultCacheConfig().entryTtl(Duration.ofMinutes(30)) // 默认缓存30分钟
                .serializeKeysWith(RedisSerializationContext.SerializationPair.fromSerializer(new StringRedisSerializer()))
                .serializeValuesWith(RedisSerializationContext.SerializationPair.fromSerializer(new GenericJackson2JsonRedisSerializer()))
                .disableCachingNullValues(); // 不允许缓存null值。

        return RedisCacheManager.builder(connectionFactory).cacheDefaults(config).transactionAware().build();
    }
}


```

## 测试与验证
### 启动类
```java
package com.laodu.cache;

import org.mybatis.spring.annotation.MapperScan;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@MapperScan(basePackages = "com.laodu.cache.mapper")
@SpringBootApplication
public class CacheApplication {

        public static void main(String[] args) {
                SpringApplication.run(CacheApplication.class, args);
        }

}
```

### 测试步骤
1. 启动Redis服务器和MySQL服务器
2. 运行Spring Boot应用
3. 使用Postman或curl测试以下接口：

#### 测试获取产品（第一次查询会访问数据库，后续查询会走缓存）
```bash
curl http://localhost:8080/product/1
```

#### 测试更新产品（会同时更新数据库和缓存）
```bash
curl -X PUT http://localhost:8080/product -H "Content-Type: application/json" -d "{\"id\":1,\"name\":\"iPhone 15 Pro\",\"price\":10999.00,\"stock\":80}"
```

#### 测试删除产品（会同时删除数据库记录和缓存）
```bash
curl -X DELETE http://localhost:8080/product/1
```

# 第十三章 主从复制
<img src="https://cdn.nlark.com/yuque/0/2025/jpeg/21376908/1757681056420-39d1bc52-55fe-4f3b-8183-b4d7ba79b166.jpeg" width="4308" title="" crop="0,0,1,1" id="IhMqK" class="ne-image" style="font-size: 16px">

## 主从复制的理解
主从复制指将一个Redis服务器（主节点）的数据复制到其他Redis服务器（从节点）。主节点负责**<font style="color:#DF2A3F;">写操作</font>**，从节点同步主节点数据并支持**<font style="color:#DF2A3F;">读操作</font>**。

## 主从复制有啥用
**读写分离：主节点写，从节点读。  **

**容灾恢复：主节点故障后，从节点可升级为主节点。**

**高可用：主节点故障时，从节点能继续服务。**

## Redis7主从复制的实现步骤
### 配置从节点1：6380
创建从节点配置文件。将 `/etc/redis.conf` 复制一份生成 `/etc/redis/6380.conf`，然后按照以下配置对`6380.conf`文件进行修改：（**<font style="color:#DF2A3F;">一个一个修改</font>**）

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

### 配置从节点2：6381
创建从节点配置文件。将 `/etc/redis.conf` 复制一份生成 `/etc/redis/6381.conf`，然后按照以下配置对`6381.conf`文件进行修改：（**<font style="color:#DF2A3F;">一个一个修改</font>**）

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

### 取消复制（从节点恢复为独立节点）
```bash
replicaof no one
```

## 哨兵（Sentinel）
之前我们只是实现了主从复制，读写分离的效果。但是**主节点宕机**之后，从节点不会自动提升为主节点，如果要实现这个效果就需要哨兵。

哨兵的作用：监控主从节点，自动故障转移（主节点宕机时提升从节点为主节点）。

### 哨兵的作用
Redis哨兵系统主要提供以下功能：

1. **监控**：持续检查主从服务器是否正常运行
2. **通知**：当被监控的Redis实例出现问题时，可以通过API通知系统管理员或通知其他应用程序
3. **自动故障转移**：如果主服务器故障，哨兵可以自动将一个从服务器升级为主服务器，并让其他从服务器改为复制新的主服务器
4. **为客户端提供信息**：哨兵可以为客户端程序提供当前 Redis 主服务器的地址

### 多个哨兵的作用
在生产环境中，通常需要部署多个哨兵实例(通常是3个或5个)，原因如下：

1. **容错**：避免单点故障，单个哨兵可能误判主节点下线
2. **共识机制**：多个哨兵通过投票机制决定是否执行故障转移，避免误判
3. **高可用**：即使部分哨兵进程或机器故障，系统仍能正常工作

### 实现过程
#### 准备Redis主从配置
我们现在已经配置了一主两从：

+ 主节点：192.168.48.200:6379
+ 从节点1：192.168.48.200:6380
+ 从节点2：192.168.48.200:6381

#### 创建哨兵配置文件
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

#### 配置参数说明
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

#### 启动哨兵服务
```bash
# 创建日志目录
sudo mkdir -p /var/log/redis

# 启动哨兵
redis-server /etc/redis/sentinel_26379.conf --sentinel
redis-server /etc/redis/sentinel_26380.conf --sentinel
redis-server /etc/redis/sentinel_26381.conf --sentinel
```

#### 验证哨兵状态
```bash
# 连接任意哨兵实例
redis-cli -p 26379

sentinel master mymaster  # 查看被监控的主节点详细信息
sentinel slaves mymaster  # 查看该主节点下所有从节点的信息列表
sentinel sentinels mymaster # 查看监控同一主节点的其他哨兵实例信息
```

#### 测试故障转移
1. 手动停止主Redis服务(6379)
2. 等待约5秒(down-after-milliseconds设置的时间)
3. 哨兵将选举新的主服务器
4. 检查新的主从关系

### 注意事项
1. 确保哨兵实例之间的时间同步(使用NTP)
2. 生产环境建议将哨兵部署在不同的物理机器上
3. 哨兵配置会自动更新，不要手动修改哨兵运行时生成的配置文件
4. 生产环境集群标准配置：1 主 2 从 3 哨兵。

# 第十四章 Redis 事务
<img src="https://cdn.nlark.com/yuque/0/2025/jpeg/21376908/1757681056420-39d1bc52-55fe-4f3b-8183-b4d7ba79b166.jpeg" width="4308" title="" crop="0,0,1,1" id="h4qgv" class="ne-image" style="font-size: 16px">

## Redis真的是“单线程”吗？
首先澄清一个常见误解：

+ **Redis核心是单线程**处理命令（6.0+版本对网络I/O等使用多线程，但命令执行仍是单线程）
+ 正是因为是单线程，**所有命令都是串行执行**，天然避免了并发问题
+ 那为什么还需要事务？

## Redis事务是什么？
Redis事务通过`MULTI/EXEC`命令实现：

```plain
MULTI          # 开始事务
SET key1 "A"
SET key2 "B"
INCR counter
EXEC           # 执行事务
```

**关键特点：**

+ **批量执行**：所有命令排队，一次性执行
+ **原子性**：要么全部执行，要么全部不执行（**执行中不会被其他客户端打扰：因为 redis 是单线程，在批处理执行队列中的命令时，也没有机会去处理其他的客户端**）
+ **无回滚**：Redis事务**不支持回滚**（ROLLBACK）

## Redis事务有什么用？
### 主要应用场景
```plain
# 场景1：批量操作保证原子性
MULTI
HSET user:1000 name "Alice"
HSET user:1000 age 30
SADD online_users 1000
EXEC

# 场景2：配合WATCH实现乐观锁机制
WATCH age      # 监控键
MULTI
SET age 100  # 如果age被其他客户端修改，此处会失败
EXEC
```

### 核心价值
1. **减少网络开销**：多个命令一次发送
2. **避免并发干扰**：执行期间不会被其他命令打断
3. **实现乐观锁**：通过`WATCH`实现CAS（Compare-And-Swap）

## 与传统数据库事务的区别
| **特性** | **Redis事务** | **数据库传统事务（如MySQL）** |
| --- | --- | --- |
| **原子性** | ✅ 执行原子性 | ✅ ACID原子性 |
| **一致性** | ⚠️ 有限保证 | ✅ 强一致性 |
| **隔离性** | ✅ 串行化隔离（天然） | 支持多级别隔离 |
| **回滚** | ❌ **不支持** | ✅ 支持ROLLBACK |
| **隔离级别** | 总是串行化 | 可配置（读未提交、读已提交等） |
| **实现方式** | 命令队列 | 日志（UNDO/REDO） |
| **锁机制** | 乐观锁（WATCH） | 悲观锁（行锁、表锁） |


## Redis事务的局限性
```plain
# 注意：事务中的错误处理
MULTI
SET a 1
INCR b  # 如果b不是数字，这个命令会失败
SET c 2
EXEC
# 即使INCR失败，SET c 2仍会执行！
```

**注意：Redis只保证语法错误时整个事务失败，运行时错误不影响其他命令**

## 总结 Redis 事务
**Redis事务的核心价值：**

1. **批量执行的原子性** - 多个命令作为一个单元执行
2. **乐观锁的实现基础** - 通过`WATCH`实现CAS操作
3. **性能优化** - 减少网络往返时间

**适用场景：**

+ 需要批量操作的原子性
+ 简单的乐观锁需求

Redis事务更像是“命令批处理+乐观锁”，而不是传统意义上的数据库事务。理解这个区别对正确使用Redis至关重要。

## RedisTemplate 代码中使用事务
**实现事务的代码示例：**

```java
public void basicTransaction() {
    
    // 使用SessionCallback确保所有操作在同一个连接
    redisTemplate.execute(new SessionCallback<List<Object>>() {
        @Override
        public List<Object> execute(RedisOperations operations) throws DataAccessException {
            // 1. 开启事务
            operations.multi();
            
            // 2. 执行多个操作（只是入队，不真正执行）
            operations.opsForValue().set("name", "张三");
            operations.opsForValue().set("age", "25");
            operations.opsForSet().add("skills", "Java", "Redis");
            
            // 3. 提交事务，返回所有命令的执行结果
            return operations.exec();
        }
    });
}
```



**使用 WATCH 实现的乐观锁**

```java
// 带乐观锁的事务示例
public void watchTransaction() {
    List<Object> results = redisTemplate.execute(new SessionCallback<List<Object>>() {
        @Override
        public List<Object> execute(RedisOperations operations) throws DataAccessException {
            String key = "counter";
            
            // 1. 监控key，如果被其他客户端修改，事务会失败
            operations.watch(key);
            
            // 2. 获取当前值
            Object current = operations.opsForValue().get(key);
            int value = current == null ? 0 : Integer.parseInt(current.toString());
            
            // 3. 开启事务
            operations.multi();
            
            // 4. 在事务中执行操作
            operations.opsForValue().set(key, String.valueOf(value + 1));
            operations.opsForValue().set("last_update", System.currentTimeMillis());
            
            // 5. 提交事务
            // 如果key被其他客户端修改过，exec()会返回null
            List<Object> execResults = operations.exec();
            
            if (execResults == null) {
                System.out.println("事务失败：key被其他客户端修改");
            } else {
                System.out.println("事务成功：" + execResults);
            }
            
            return execResults;
        }
    });
}
```



**lambda 方式：**

```java
redisTemplate.execute((RedisOperations ops) -> {
    ops.multi();
    ops.opsForValue().set("a", "1");
    ops.opsForValue().set("b", "2");
    return ops.exec();  // 提交事务
});

redisTemplate.execute((RedisOperations ops) -> {
    ops.watch("count");        // 监控
    ops.multi();               // 开启事务
    ops.opsForValue().increment("count", 1);
    return ops.exec();         // 提交，如果count被改过则返回null
});
```

# 第十五章 Redis 的其他类型（扩展）
我们已经学习了 string、list、hash、set、zset。其实 Redis 有 9 个类型。剩下的 4 个分别是：<font style="color:rgb(15, 17, 21);">Bitmaps、HyperLogLog、Geospatial、Stream。</font>

<font style="color:rgb(15, 17, 21);">对于 string、list、hash、set、zset、bitmaps，Geospatial 来说，本质上最终底层存储的都是字符串，只不过具体存储时的数据结构不同。</font>

<font style="color:rgb(15, 17, 21);">但对于HyperLogLog、Stream 来说，底层则不再是字符串了。</font>

## <font style="color:rgb(15, 17, 21);">Bitmaps（位图）</font>
你可以把它看做底层是一个二进制位数组。也就是说直接存的是二进制形式。但 type 命令的执行结果显示 string。

**<font style="color:rgb(15, 17, 21);">Bitmaps就是String的一种特殊用法——把每个字节的8个位分别用作布尔标记，这样内存效率极高，比如1亿用户在线状态只需约12MB。</font>**

### 相关命令
```plain
# 设置指定偏移量的位值（0或1）
# value只能是0或1，不能是其他值。
# offset是偏移量，表示第几个二进制位。偏移量从0开始。
SETBIT key offset value

# 例如
setbit a 0 1
setbit a 1 0
setbit a 2 1
setbit a 3 0

# 执行以上4条命令后，实际上这个a键存储的value底层对应这样一个二进制：00000101

```

```plain
# 获取指定偏移量的位值
GETBIT key offset

# 例如
getbit a 3   # 获取第4个二进制位
```

```plain
# 统计指定范围内位值为1的数量
BITCOUNT key [start end]

# 例如
bitcount a   # 统计所有 bit位 为1的数量
bitcount a 0 4 # 统计前5个bit位中1个数量
```

### 实际应用
**用户画像：**

```plain
# 32位特征标记（一个整数搞定）
位0: 性别男(1)/女(0)
位1: 是否VIP
位2: 是否学生
位3: 是否新用户
位4-7: 年龄段（0000-1111）
位8-15: 兴趣标签（8个）
位16-31: 行为特征（16个）
```

**状态标记：**

```plain
# 用户特征标记（每个特征一个位）
SETBIT user:flags:1001 0 1  # 位0=VIP
SETBIT user:flags:1001 1 1  # 位1=实名
SETBIT user:flags:1001 2 0  # 位2=未绑卡
SETBIT user:flags:1001 3 1  # 位3=已付费

# 检查是否为VIP
GETBIT user:flags:1001 0
```

### Bitmaps 的最大优点
两个杀手锏：

1. 速度快。
2. 省空间。

但它也有缺点，就是在需要存储具体值的场景下是不适用的。仅适用于两种状态的表示。

Bitmaps 本质上**<font style="color:rgb(15, 17, 21);">就是一个超长的开关阵列，每个位置只能是 开(1) 或 关(0)。</font>**

## <font style="color:rgb(15, 17, 21);">HyperLogLog</font>
<font style="color:rgb(15, 17, 21);">HyperLogLog 的核心作用：用极小空间（~12KB）估算海量数据中不重复元素的个数，接受微小误差（~1%），换取巨大内存节省。</font>

<font style="color:rgb(15, 17, 21);"></font>

**<font style="color:rgb(15, 17, 21);">HyperLogLog = 统计海量唯一值的"模糊计数器"，用固定12KB内存换0.81%误差，适合"只关心数量不关心细节"的场景。</font>**

**<font style="color:rgb(15, 17, 21);">HyperLogLog 的原理：通过观察"哈希值尾部连续0的最大长度"来估算数据规模——就像根据"最长连阴天"推断雨季长短。</font>**

**<font style="color:rgb(15, 17, 21);">HyperLogLog 经常用来进行 UV 统计。</font>**

**<font style="color:rgb(15, 17, 21);">UV 统计：UV = 独立访客数（Unique Visitors）,UV 就是"有多少个不同的人来过"，一个人来100次也只算1次。</font>**

**<font style="color:rgb(15, 17, 21);"></font>**

**<font style="color:rgb(15, 17, 21);">还有一个 PV，PV = 页面浏览量（Page Views）</font>**

**<font style="color:rgb(15, 17, 21);">PV 就是"页面被打开的总次数"，刷新一次页面就+1。</font>**

**<font style="color:rgb(15, 17, 21);"></font>**

**<font style="color:rgb(15, 17, 21);">PV = 10+5+3+1 = 19次（总访问量）</font>**

**<font style="color:rgb(15, 17, 21);">UV = 4人（A、B、C、D四个不同的人）</font>**

**<font style="color:rgb(15, 17, 21);"></font>**

**<font style="color:rgb(15, 17, 21);">PV 的统计很简单：使用单个计数器即可完成。</font>**

```plain
# 按天统计
INCR pv:20240101      # 2024年1月1日PV
INCR pv:20240102      # 第二天

# 查看某天PV
GET pv:20240101
```





**HyperLogLog的原理：**

想象一下，你是一位马戏团的经理，你的任务是**在表演散场后，快速估算今天来了多少位不同的观众（UV）**，但你不能去数每个人的票，因为那样太慢了。

你会怎么做呢？

**第一步：观察一个神奇的现象**

你发现，表演结束后，观众会陆续从一个大帐篷里走出来。帐篷有**10个出口**（编号0-9），而且观众**完全随机**地选择从哪个出口离开。

你站在**1号出口**观察，然后注意到一个有趣的现象：

+ 如果今天只来了**1位**观众，他有1/10的概率从1号口出来。如果他真的从1号口出来了，这没什么特别的。
+ 如果今天来了**10位**观众，那么至少有一位从1号口出来的概率就很大了。
+ 如果今天来了**100位**观众，你可能会看到很多人从1号口涌出。
+ **但是**，你发现了一个更聪明的办法：你不再数有多少人从1号口出来，而是记录一个**特殊数据**：从1号口出来的**观众中，他们的“票号”末尾有多少个连续的0**。



**第二步：收集“特殊数据”**

假设每个观众的票上都有一个唯一的、随机的二进制编号（比如由哈希函数生成）。

你规定：只看从1号口出来的观众，记录他们票号**末尾连续0的最大个数**。

+ 观众A票号是 `...1000`（末尾3个0）。你记录下来：**当前最大连续0 = 3**。
+ 观众B票号是 `...0100`（末尾2个0）。最大值还是3。
+ 观众C票号是 `...0001`（末尾0个0）。最大值还是3。
+ 观众D票号是 `...0000 0000`（末尾8个0！）。**哇！** 你更新记录：**当前最大连续0 = 8**。

**关键洞察来了：**

+ 要碰到一个末尾有8个0的票号，概率是非常低的（大约 1/2^8 = 1/256）。
+ 除非……有**足够多**的观众从1号口经过，使得这种低概率事件有机会发生！
+ **所以，“最大连续0的个数”这个数字（记为k），间接反映了从1号口经过的观众数量。** 数量越多，k值可能越大。
+ 具体估算公式是：`从1号口出来的人数 ≈ 2^k`。比如k=8，估算人数就是256。



**第三步：解决单一出口的误差问题（引入多桶）**

但只靠1号口的数据很不准。如果今天大部分观众碰巧都走了其他出口，1号口的估算就会严重偏低。

怎么办？**动用所有出口！**

你派10个助手，每人守一个出口（0-9号），都用同样的方法记录各自出口的“**最大连续0个数**”。

表演结束，你收集到10个数据：  
`[3, 5, 4, 8, 2, 4, 3, 6, 5, 4]`

现在你有10个独立的估算样本了。如果直接平均，还是会受极端值（比如那个8）影响。HyperLogLog采用的方法是：

1. 对每个出口的数据，先用公式 `2^k` 估算从该出口出来的人数。
2. 然后取它们的**调和平均数**（一种平均方式，能削弱极大值的影响）。
3. 再乘以一个根据桶数（这里是10）确定的修正常数。

最终，你就能得出一个对**总观众数**相对准确的估算。



**总结**

1. **目标**：快速估算海量数据中有多少**不重复**的元素（UV）。
2. **核心魔法**：给每个用户ID算一个“随机哈希值”，看作他的“随机票号”。
3. **关键观察**：哈希值**前缀或末尾的特定模式**（比如连续0的个数）出现的概率是固定的。人越多，越有可能观察到这种罕见的模式。
4. **分桶平均**：为了避免偶然性，把数据分到多个“桶”里分别观察，然后用聪明的数学方法（调和平均）汇总所有桶的观察结果，得出最终估算值。

**HyperLogLog的精髓就是：**

> **用概率统计中一个低概率事件的“是否发生”，来倒推样本的“规模有多大”。**  
它不存储每个用户ID，只存储那些“罕见模式”的计数器，因此占用内存**极小**（通常只要几KB），就能估算上亿的UV，虽有微小误差（约1-2%），但对于大数据场景完全可接受。
>

这就好比，你想知道湖里有多少条鱼，不用把鱼都捞上来数，而是通过“钓到一条特别罕见的珍稀鱼”这件事来推断——钓到它，说明你可能已经钓了非常多次了，从而反推出鱼的总量大概有多少。

## <font style="color:rgb(15, 17, 21);">Stream 流</font>
**<font style="color:rgb(15, 17, 21);">Stream 是 Redis 的消息队列，让你能像微信聊天一样收发消息记录。</font>**

<font style="color:rgb(15, 17, 21);">就像：有人往群里发消息（XADD），其他人可以查看历史消息（XRANGE）或实时接收新消息（XREAD）。</font>

<font style="color:rgb(15, 17, 21);">实际开发中，我们一般会使用消息队列中间件来实现消息队列。</font>

## **<font style="color:rgb(15, 17, 21);">Geospatial</font>**
**<font style="color:rgb(15, 17, 21);">“地图钉上的计算器”</font>**

+ **<font style="color:rgb(15, 17, 21);">地图钉</font>**<font style="color:rgb(15, 17, 21);">：用来存储地理位置（经纬度坐标），就像在地图上扎钉子做标记。</font>
+ **<font style="color:rgb(15, 17, 21);">计算器</font>**<font style="color:rgb(15, 17, 21);">：能对这些坐标进行快速计算，比如“找出我周围5公里内所有的钉子”，并算出它们离我多远。</font>

<font style="color:rgb(15, 17, 21);">Redis的</font>**<font style="color:rgb(15, 17, 21);">Geospatial类型底层是使用ZSet实现的</font>**<font style="color:rgb(15, 17, 21);">。（不是一种全新的类型，是基于 zset 实现的语法糖。）</font>