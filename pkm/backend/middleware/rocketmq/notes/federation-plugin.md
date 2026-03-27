# Federation 插件

这部分内容和之前搭建的集群就没有关系了。

Federation 翻译为联邦。

---

## 理解 Federation

**RabbitMQ Federation 用于在不同 RabbitMQ 集群之间自动复制消息，实现跨******网络域******的消息传输。**

**它是 RabbitMQ 的一个插件。**

### 主要场景

1. **跨******机房/地域****** 复制** - 北京集群 ↔ 上海集群
2. **上下游系统集成** - 生产集群 → 消费集群

### Federation vs 镜像队列/仲裁队列

| **特性** | **镜像/仲裁队列 (Mirroring)** | **Federation** |
| --- | --- | --- |
| **范围** | 同一集群内节点 | **跨集群/跨网络** |
| **网络要求** | 低延迟局域网 | 可容忍较高延迟 |
| **数据一致性** | 强一致性 | **最终一致性** |
| **使用场景** | 高可用 | 地理分布、系统集成 |

### 需要 Federation

+ 多地数据中心消息同步
+ 云上云下混合架构
+ 不同业务域消息互通

### 不需要 Federation

+ 单一机房内的集群
+ 实时性要求极高的场景
+ 网络稳定的局域网环境

### 总结一下

**Federation 是 RabbitMQ 的"广域网消息桥梁"**，解决了镜像队列只能在局域网使用的问题，让你可以构建地理分布的 RabbitMQ 架构。

如果你的系统需要：

+ 跨地域部署
+ 混合云架构  
+ 系统间消息集成

那么 Federation **非常重要**！如果只是单个机房内的集群，用镜像队列/仲裁队列就够了。

---

## 创建两个 RabbitMQ 实例

使用 docker 容器创建两个 RabbitMQ 的实例。

```shell

docker run -d --name rabbitmq-beijing \
  --net dajiankang --ip 172.16.0.21 \
  -p 56722:5672 \
  -p 15675:15672 \
  -e RABBITMQ_DEFAULT_USER=admin \
  -e RABBITMQ_DEFAULT_PASS=123456 \
  -e TZ=Asia/Shanghai \
  -m 450m \
  --restart unless-stopped \
  rabbitmq:3.13-management

```

```java

docker run -d --name rabbitmq-shanghai \
  --net dajiankang --ip 172.16.0.22 \
  -p 56723:5672 \
  -p 15676:15672 \
  -e RABBITMQ_DEFAULT_USER=admin \
  -e RABBITMQ_DEFAULT_PASS=123456 \
  -e TZ=Asia/Shanghai \
  -m 450m \
  --restart unless-stopped \
  rabbitmq:3.13-management

```

---

## 配置端口转发

| **windows 端口** | **虚拟机端口** | **docker 端口** |
| --- | --- | --- |
| 56722 | 56722 | 5672 |
| 15675 | 15675 | 15672 |

| **windows 端口** | **虚拟机端口** | **docker 端口** |
| --- | --- | --- |
| 56723 | 56723 | 5672 |
| 15676 | 15676 | 15672 |

---

## 启用 Federation 插件

```shell
