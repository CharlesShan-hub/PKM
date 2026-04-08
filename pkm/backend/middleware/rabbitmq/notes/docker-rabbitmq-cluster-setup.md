# docker 环境下搭建 RabbitMQ 集群
**<font style="color:#DF2A3F;">提醒：生产环境下，建议不要在一个物理机上搭建 RabbitMQ，防止物理机宕机，导致数据丢失。</font>**

基于之前的 `dajiankang` 网络和指定的可用IP，以下是完整的RabbitMQ集群搭建方案。

## 删除 mq 容器
我们要搭建集群了。把课程最开始创建的 mq 容器删除：

```shell
docker stop mq
docker rm mq
```

## 创建数据目录
```bash
# 为三个节点创建数据目录
mkdir -p /home/rabbitmq/{node1,node2,node3}/data
mkdir -p /home/rabbitmq/{node1,node2,node3}/conf
```

## 创建RabbitMQ配置文件
**<font style="color:rgb(15, 17, 21);">这些配置文件用于让三个RabbitMQ节点自动发现并组成集群，实现高可用和负载均衡，具体作用：</font>**

+ **<font style="color:rgb(15, 17, 21);">允许 guest 用户从</font>****<font style="color:#DF2A3F;">远程</font>****<font style="color:rgb(15, 17, 21);">连接 RabbitMQ</font>**
+ **<font style="color:rgb(15, 17, 21);">设置服务端口</font>**
    - **<font style="color:rgb(15, 17, 21);">（不配置端口时，rabbitmq 的默认端口也是 5672 和 15672，因此这两个配置可以省略，另外集群之间的节点通信端口默认是 25672，也不用配置，为什么三个端口一样？不冲突吗？不冲突，因为每个 docker 容器的环境是独立的。）</font>**
+ **<font style="color:rgb(15, 17, 21);">配置节点相互发现组成集群。</font>**

为每个节点创建配置文件：

**节点1配置** (`/home/rabbitmq/node1/conf/rabbitmq.conf`)：

```bash
cat > /home/rabbitmq/node1/conf/rabbitmq.conf << EOF
loopback_users.guest = false
listeners.tcp.default = 5672
management.tcp.port = 15672
cluster_formation.peer_discovery_backend = rabbit_peer_discovery_classic_config
cluster_formation.classic_config.nodes.1 = rabbit@rabbitmq-node1
cluster_formation.classic_config.nodes.2 = rabbit@rabbitmq-node2
cluster_formation.classic_config.nodes.3 = rabbit@rabbitmq-node3
EOF
```

**节点2配置** (`/home/rabbitmq/node2/conf/rabbitmq.conf`)：

```bash
cat > /home/rabbitmq/node2/conf/rabbitmq.conf << EOF
loopback_users.guest = false
listeners.tcp.default = 5672
management.tcp.port = 15672
cluster_formation.peer_discovery_backend = rabbit_peer_discovery_classic_config
cluster_formation.classic_config.nodes.1 = rabbit@rabbitmq-node1
cluster_formation.classic_config.nodes.2 = rabbit@rabbitmq-node2
cluster_formation.classic_config.nodes.3 = rabbit@rabbitmq-node3
EOF
```

**节点3配置** (`/home/rabbitmq/node3/conf/rabbitmq.conf`)：

```bash
cat > /home/rabbitmq/node3/conf/rabbitmq.conf << EOF
loopback_users.guest = false
listeners.tcp.default = 5672
management.tcp.port = 15672
cluster_formation.peer_discovery_backend = rabbit_peer_discovery_classic_config
cluster_formation.classic_config.nodes.1 = rabbit@rabbitmq-node1
cluster_formation.classic_config.nodes.2 = rabbit@rabbitmq-node2
cluster_formation.classic_config.nodes.3 = rabbit@rabbitmq-node3
EOF
```

## 创建hosts文件
**<font style="color:rgb(15, 17, 21);">这个配置用于在容器内部建立主机名与IP的映射关系，让三个RabbitMQ节点能够通过主机名相互识别和通信，从而成功组建集群。（RabbitMQ 节点间的通信是依赖主机名的。）</font>**

创建包含所有节点主机名映射的文件：

```bash
cat > /home/rabbitmq/hosts << EOF
172.16.0.13 rabbitmq-node1
172.16.0.15 rabbitmq-node2
172.16.0.16 rabbitmq-node3
EOF
```

## 启动三个RabbitMQ节点
注意：

+ RabbitMQ 要求：在同一个集群内的节点 Cookie 值必须相等，我们这里设置的 Cookie 值：`CLUSTER_COOKIE_123456`
+ 如果搭建集群，4369 端口必须映射。

**启动节点1 (172.16.0.13)**：

```bash
docker run -d --name rabbitmq-node1 \
  --hostname rabbitmq-node1 \
  --net dajiankang --ip 172.16.0.13 \
  -p 4369:4369 \
  -p 5672:5672 \
  -p 15672:15672 \
  -v /home/rabbitmq/node1/data:/var/lib/rabbitmq \
  -v /home/rabbitmq/node1/conf/rabbitmq.conf:/etc/rabbitmq/rabbitmq.conf \
  -v /home/rabbitmq/hosts:/etc/hosts \
  -e RABBITMQ_DEFAULT_USER=admin \
  -e RABBITMQ_DEFAULT_PASS=123456 \
  -e RABBITMQ_ERLANG_COOKIE="CLUSTER_COOKIE_123456" \
  -e TZ=Asia/Shanghai \
  -m 450m \
  --restart unless-stopped \
  rabbitmq:3.13-management
```

**启动节点2 (172.16.0.15)**：

```bash
docker run -d --name rabbitmq-node2 \
  --hostname rabbitmq-node2 \
  --net dajiankang --ip 172.16.0.15 \
  -p 43690:4369 \
  -p 56720:5672 \
  -p 15673:15672 \
  -v /home/rabbitmq/node2/data:/var/lib/rabbitmq \
  -v /home/rabbitmq/node2/conf/rabbitmq.conf:/etc/rabbitmq/rabbitmq.conf \
  -v /home/rabbitmq/hosts:/etc/hosts \
  -e RABBITMQ_DEFAULT_USER=admin \
  -e RABBITMQ_DEFAULT_PASS=123456 \
  -e RABBITMQ_ERLANG_COOKIE="CLUSTER_COOKIE_123456" \
  -e TZ=Asia/Shanghai \
  -m 450m \
  --restart unless-stopped \
  rabbitmq:3.13-management
```

**启动节点3 (172.16.0.16)**：

```bash
docker run -d --name rabbitmq-node3 \
  --hostname rabbitmq-node3 \
  --net dajiankang --ip 172.16.0.16 \
  -p 43691:4369 \
  -p 56721:5672 \
  -p 15674:15672 \
  -v /home/rabbitmq/node3/data:/var/lib/rabbitmq \
  -v /home/rabbitmq/node3/conf/rabbitmq.conf:/etc/rabbitmq/rabbitmq.conf \
  -v /home/rabbitmq/hosts:/etc/hosts \
  -e RABBITMQ_DEFAULT_USER=admin \
  -e RABBITMQ_DEFAULT_PASS=123456 \
  -e RABBITMQ_ERLANG_COOKIE="CLUSTER_COOKIE_123456" \
  -e TZ=Asia/Shanghai \
  -m 450m \
  --restart unless-stopped \
  rabbitmq:3.13-management
```

## 启用集群插件并加入集群
等待所有节点启动完成（约30秒），然后执行：

**在节点2上执行，加入集群**：

```bash
# 进入节点2容器
docker exec -it rabbitmq-node2 bash

# 在容器内执行以下命令
rabbitmqctl stop_app
rabbitmqctl reset
rabbitmqctl join_cluster rabbit@rabbitmq-node1
rabbitmqctl start_app
exit
```

**在节点3上执行，加入集群**：

```bash
# 进入节点3容器
docker exec -it rabbitmq-node3 bash

# 在容器内执行以下命令
rabbitmqctl stop_app
rabbitmqctl reset
rabbitmqctl join_cluster rabbit@rabbitmq-node1
rabbitmqctl start_app
exit
```

## 验证集群状态
```bash
# 在任何节点上检查集群状态
docker exec -it rabbitmq-node1 rabbitmqctl cluster_status
```

## 设置镜像队列策略（这一步不要做）
为了 **数据** 高可用，设置镜像队列：

```bash
docker exec -it rabbitmq-node1 rabbitmqctl set_policy ha-all "^" '{"ha-mode":"all"}'
```

**<font style="color:rgb(15, 17, 21);">将集群中所有队列设置为全节点镜像，实现数据高可用。</font>**

<font style="color:rgb(15, 17, 21);">这句话的含义是：</font>

+ <font style="color:rgb(15, 17, 21);">对所有队列（</font>`<font style="color:rgb(15, 17, 21);background-color:rgb(235, 238, 242);">"^"</font>`<font style="color:rgb(15, 17, 21);"> </font><font style="color:rgb(15, 17, 21);">匹配所有队列名）</font>
+ <font style="color:rgb(15, 17, 21);">在所有节点上创建镜像副本（</font>`<font style="color:rgb(15, 17, 21);background-color:rgb(235, 238, 242);">"ha-mode":"all"</font>`<font style="color:rgb(15, 17, 21);">）</font>
+ <font style="color:rgb(15, 17, 21);">确保任一节点宕机时队列数据不丢失，服务自动切换</font>

<font style="color:rgb(15, 17, 21);"></font>

**<font style="color:#DF2A3F;">注意：在 RabbitMQ 3.8.x 版本之后引入了仲裁队列。使用仲裁队列的话，就不需要再配置镜像队列了。通过仲裁队列默认就可以达到高可用。并且使用仲裁队列就不需要指定以上这些复杂的规则了。</font>**

## 配置端口转发
要在 windows 上访问虚拟机中 docker 中的 RabbitMQ 节点。需要在 `Oracle VirtualBox`上配置端口映射：

**节点 1 的端口映射：**

| **windows 端口** | **虚拟机端口** | **docker 端口** | **备注** |
| --- | --- | --- | --- |
| 4369 | 4369 | 4369 |  |
| 5672 | 5672 | 5672 | **这个之前已配置** |
| 15672 | 15672 | 15672 | **这个之前已配置** |




**节点 2 的端口映射：**

| **windows 端口** | **虚拟机端口** | **docker 端口** |
| --- | --- | --- |
| 43690 | 43690 | 4369 |
| 56720 | 56720 | 5672 |
| 15673 | 15673 | 15672 |




**节点 3 的端口映射：**

| **windows 端口** | **虚拟机端口** | **docker 端口** |
| --- | --- | --- |
| 43691 | 43691 | 4369 |
| 56721 | 56721 | 5672 |
| 15674 | 15674 | 15672 |


## 访问信息
+ **管理界面**：
    - 节点1: `http://localhost:15672`
    - 节点2: `http://localhost:15673`
    - 节点3: `http://localhost:15674`
+ **用户名**: `admin`
+ **密码**: `123456`



另外，通过 web 管理界面也可以看到三个节点的集群已经做到了相互感知和发现了：

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1764049992301-111cf21f-dd84-474b-882e-0c8af5faf2f4.png" width="479.2" title="" crop="0,0,1,1" id="u045426f7" class="ne-image">

