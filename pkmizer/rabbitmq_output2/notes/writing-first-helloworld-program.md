ont>

**<font style="color:rgb(15, 17, 21);">对于编程来说，如何实现呢？</font>**

+ 对于生产者来说
    - **声明**交换机（创建交换机：如果该交换机已存在，则直接使用，不需要重复创建）
    - **声明**队列（创建队列：如果该队列已存在，则直接使用，不需要重复创建）
    - 使用**路由键**将**交换机**和**队列**绑定在一起
    - 发送消息时只需要指定：**交换机** 和 **路由键**
+ 对于消费者来说
    - 只需要指定**哪个队列**就行。

## 安装 RabbitMQ
**第一步：拉取镜像**

```bash
docker pull rabbitmq:3.13-management
```



**第二步：创建 RabbitMQ 容器（基于我们之前大健康项目的网络 IP 来创建）**

```bash
docker run -d --name mq \
  --net dajiankang --ip 172.16.0.13 \
  -p 5672:5672 \
  -p 15672:15672 \
  -e RABBITMQ_DEFAULT_USER=admin \
  -e RABBITMQ_DEFAULT_PASS=123456 \
  -e TZ=Asia/Shanghai \
  -m 450m \
  --restart unless-stopped \
  rabbitmq:3.13-management
```

5672 端口是和客户端程序交互使用的。(将来生产者端和消费者端都是通过 5672 访问 RabbitMQ)

15672 是 web 管理的端口。



**第三步：端口转发**

在 `Oracle VirtualBox`软件中配置端口转发。这样在 windows 系统上就可以使用 `localhost`方式访问了。

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1764038935571-39e6268a-509d-4c42-945e-fae5f6012397.png" width="914.4" title="" crop="0,0,1,1" id="ua05afef8" class="ne-image">

| **windows 端口** | **虚拟机端口** | **docker 端口** |
| --- | --- | --- |
| 5672 | 5672 | 5672 |
| 15672 | 15672 | 15672 |




**第四步：打开 Web 管理界面：**[**http://localhost:15672/**](http://localhost:15672/)

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1764038774581-d900af0d-21dd-4929-9599-a1d96f9c5359.png" width="287.2" title="" crop="0,0,1,1" id="u77a69977" class="ne-image">

# 编写第一个 HelloWorld 程序
刚开始，我们不弄那么复杂，发消息也不经过交换机。直接生产者将消息发送到消息队列，消费者直接消费。先实现第一个程序体验一下。

## 编写第一个 HelloWorld 程序
### 引入 RabbitMQ 客户端程序的依赖
```xml
<dependency>
    <groupId>com.rabbitmq</groupId>
    <artifactId>amqp-client</artifactId>
    <version>5.20.0</version>
</dependency>
```

### 编写生产者端 Producer
这个代码不需要掌握，这是最原生的程序，使用框架的话，都已经封装好了，不需要写这个代码。理解一下就行：

```java
package com.jkweilai.rabbitmq;

import com.rabbitmq.client.Channel;
import com.rabbitmq.client.Connection;
import com.rabbitmq.client.ConnectionFactory;

public class Producer {
    public static void main(String[] args) throws Exception {
        // 创建连接工厂
        ConnectionFactory connectionFactory = new ConnectionFactory();
        // 设置RabbitMQ服务器的IP和PORT
        connectionFactory.setHost("localhost");
        connectionFactory.setPort(5672);
        // 设置虚拟分组，默认就是 /
        connectionFactory.setVirtualHost("/");
        // 设置用户名和密码
        connectionFactory.setUsername("admin");
        connectionFactory.setPassword("123456");
        // 创建连接
        Connection connection = connectionFactory.newConnection();
        // 创建信道
        Channel channel = connection.createChannel();
        // 声明队列
        // 参数1: 队列名称，如果不存在则自动创建
        // 参数2: 是否持久化，true表示队列在RabbitMQ重启后仍然存在
        // 参数3: 是否排他，true表示该队列仅对当前连接可见（连接关闭时队列自动删除）
        // 参数4: 是否自动删除，true表示当最后一个消费者断开后队列自动删除
        // 参数5: 其他可选参数（如消息TTL、队列长度限制等），null表示使用默认值
        channel.queueDeclare("simple_queue", true, false, false, null);
        // 准备消息
        String msg = "hello, rabbitmq";
        // 发送消息
        // 参数1: 交换机名称，空字符串表示使用默认的(匿名)交换机
        // 参数2: 路由键，对于默认交换机，直接填写目标队列的名称
        // 参数3: 消息属性（如优先级、过期时间等），null表示使用默认属性
        // 参数4: 消息体，必须是字节数组格式
        channel.basicPublish("", "simple_queue", null, msg.getBytes());
        System.out.println("已发送消息：" + msg);
        // 关闭信道
        channel.close();
        // 关闭连接
        connection.close();
    }
}

```

运行程序：

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1763810546280-ead9b95d-3844-4963-a7d0-2bb18568950f.png" width="298.4" title="" crop="0,0,1,