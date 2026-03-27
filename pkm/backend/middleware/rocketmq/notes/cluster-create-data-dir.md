# 为三个节点创建数据目录

mkdir -p /home/rabbitmq/{node1,node2,node3}/data
mkdir -p /home/rabbitmq/{node1,node2,node3}/conf

```

---

## 创建RabbitMQ配置文件

****这些配置文件用于让三个RabbitMQ节点自动发现并组成集群，实现高可用和负载均衡，具体作用：****

+ ****允许 guest 用户从********远程********连接 RabbitMQ****
+ ****设置服务端口****
    - ****（不配置端口时，rabbitmq 的默认端口也是 5672 和 15672，因此这两个配置可以省略，另外集群之间的节点通信端口默认是 25672，也不用配置，为什么三个端口一样？不冲突吗？不冲突，因为每个 docker 容器的环境是独立的。）****
+ ****配置节点相互发现组成集群。****

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

---

## 创建hosts文件

****这个配置用于在容器内部建立主机名与IP的映射关系，让三个RabbitMQ节点能够通过主机名相互识别和通信，从而成功组建集群。（RabbitMQ 节点间的通信是依赖主机名的。）****

创建包含所有节点主机名映射的文件：

```bash

cat > /home/rabbitmq/hosts << EOF
172.16.0.13 rabbitmq-node1
172.16.0.15 rabbitmq-node2
172.16.0.16 rabbitmq-node3
EOF

```

---

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

---

## 启用集群插件并加入集群

等待所有节点启动完成（约30秒），然后执行：

**在节点2上执行，加入集群**：

```bash
