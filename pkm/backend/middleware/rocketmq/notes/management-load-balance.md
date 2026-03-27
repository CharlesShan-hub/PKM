# RabbitMQ 管理界面负载均衡

listen rabbitmq_http
    bind *:15670
    mode tcp
    balance roundrobin
    server rabbitmq1 172.16.0.13:15672 check inter 10s rise 2 fall 3
    server rabbitmq2 172.16.0.15:15672 check inter 10s rise 2 fall 3
    server rabbitmq3 172.16.0.16:15672 check inter 10s rise 2 fall 3
EOF

```

**关键配置说明：**

+ `bind *:5670`：使用 `5670` 作为新的 AMQP 端口，避免和之前映射的 `5672` 等端口冲突。客户端程序以后就连接这个端口。
+ `balance roundrobin`：轮询算法，依次将新连接分发给后端服务器。
+ `option tcp-check`：对 AMQP 端口进行 TCP 层面的健康检查。
+ `option httpchk`：对管理界面进行 HTTP API 健康检查。
+ `inter 5s`：每 5 秒检查一次。
+ `rise 2`：连续 2 次检查成功，标记服务器为健康。
+ `fall 3`：连续 3 次检查失败，标记服务器为宕机，并从负载均衡池中移除。

### 启动 HAProxy 容器

拉取 docker 镜像：

```shell

docker pull haproxy:2.8.1

```

使用一个固定的 IP（例如 `172.16.0.20`）启动 HAProxy：

```bash

docker run -d --name haproxy \
  --net dajiankang --ip 172.16.0.20 \
  -p 5670:5670 \
  -p 15670:15670 \
  -p 8100:8100 \
  -v /home/haproxy/conf:/usr/local/etc/haproxy:ro \
  --restart unless-stopped \
  haproxy:2.8.1

```

### 配置 VirtualBox 端口转发

在 VirtualBox 中为 HAProxy 的端口添加转发规则：

| **Windows 端口** | **虚拟机端口** | **Docker 容器端口** | **用途** |
| --- | --- | --- | --- |
| 5670 | 5670 | 5670 | **新的 AMQP 统一入口**，客户端连接此端口 |
| 15670 | 15670 | 15670 | **新的管理界面统一入口** |

---

## 架构总结

部署 HAProxy 后，整体架构将变为：

```plain

[应用程序]
        |
        | (连接 localhost:5670)
        v
    [HAProxy] (172.16.0.20:5670) - 负载均衡器 & 单一入口
        |
        | (根据策略分发连接)
    +---+-----------+-----------+
    |               |           |
    v               v           v
[Node1]         [Node2]       [Node3]
(172.16.0.13)  (172.16.0.15) (172.16.0.16)

```

**这个架构在生产环境中是非常经典和可靠的。它实现了负载均衡，并且还可以自动将故障节点从集群中删除。**

---

## 测试 Web 界面是否可用

注意：访问端口是 `15670`，是通过 HAProxy 访问的。

在 windows 环境下，通过这个 url 看看能不能访问：[http://localhost:15670/#/](http://localhost:15670/#/)

如果能够正常访问则表示 Web 界面的负载均衡是有效的。

另外，刷新页面后，浏览器右上角会进行 MQ 节点的切换。

---

## 测试客户端程序是否可以正常使用

使用 Web 管理界面创建：

+ 创建交换机：`exchange.cluster`
+ 创建队列：`queue.cluster`
+ 队列绑定路由键：`routing.key.cluster`

**编写生产端的代码：**和之前生产端的代码相同，只是配置文件中的端口号变化了。使用 HAProxy 的端口号。

```yaml

spring:
  rabbitmq:
    host: localhost
    port: 5670
    username: admin
    password: 123456
    virtual-host: /

```

**测试程序如下：**

```java

package com.jkweilai.producercluster;

import org.junit.jupiter.api.Test;
import org.springframework.amqp.rabbit.core.RabbitTemplate;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;

@SpringBootTest
class ProducerClusterApplicationTests {

    @Autowired
    private RabbitTemplate rabbitTemplate;

    public static final String EXCHANGE_CLUSTER = "exchange.cluster";
    public static final String ROUTING_KEY_CLUSTER = "routing.key.cluster";

    @Test
    public void test() {
        rabbitTemplate.convertAndSend(EXCHANGE_CLUSTER, ROUTING_KEY_CLUSTER, "hello rabbit!");
    }
}

```

**查看队列上是否有消息：**

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1764066093295-b1bc6921-278b-4a64-ada9-9d9c08bfa8e0.png" width="420" title="" crop="0,0,1,1" id="u1886eb78" class="ne-image">
