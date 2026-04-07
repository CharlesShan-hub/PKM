# 集群下的负载均衡
使用 HAProxy 为 RabbitMQ 集群做负载均衡是一个**非常标准和推荐**的做法。

客户端连接 HAProxy 提供的统一入口。HAProxy 负载均衡的方式访问各节点。 

## 客户端的负载均衡方案
<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1764061851134-699b045a-93f7-47cc-9608-f4db36dc7943.png" width="500.4000244140625" title="" crop="0,0,1,1" id="u7904150c" class="ne-image">

## Web 管理界面的负载均衡方案
<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1764061911033-1a66d151-5cc9-444b-b6f2-86a106fb1444.png" width="470.4000244140625" title="" crop="0,0,1,1" id="u75b8536d" class="ne-image">

## 什么是 HAProxy？
**HAProxy**（High Availability Proxy）是一个开源、高性能的 **TCP/HTTP 负载均衡器**。

## 为什么 RabbitMQ 集群需要 HAProxy？
虽然已经搭建了 RabbitMQ 集群，数据在节点间是同步的，但**客户端连接**仍然需要处理，HAProxy 提供了：

1. **统一入口点**：客户端不需要在代码里写三个地址。
2. **负载均衡**：成千上万的客户端连接可以被均匀地分散到三个 RabbitMQ 节点上，防止某个节点的连接数过多。
3. **管理界面负载均衡**：同样，对管理界面的访问也可以通过 HAProxy 进行负载。

## 如何为 RabbitMQ 集群部署 HAProxy？
基于已有的 `dajiankang` 网络，以下是一个部署方案。

### 创建 HAProxy 配置文件
创建一个目录存放配置：

```bash
mkdir -p /home/haproxy/conf
```

创建配置文件 `/home/haproxy/conf/haproxy.cfg`：

```plain
cat > /home/haproxy/conf/haproxy.cfg << 'EOF'
global
    daemon
    maxconn 4000
    log stdout format raw local0 info

defaults
    mode tcp
    option tcplog
    option dontlognull
    timeout connect 5000ms
    timeout client 50000ms
    timeout server 50000ms
    log global