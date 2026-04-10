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

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1763810546280-ead9b95d-3844-4963-a7d0-2bb18568950f.png" width="298.4" title="" crop="0,0,1,1" id="ucc7d7a02" class="ne-image">

**使用 RabbitMQ Web 管理界面查看**

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1763810897646-3758254a-8d00-44a2-ae74-b1be386f07b1.png" width="1055.2" title="" crop="0,0,1,1" id="u6c677b04" class="ne-image">

**点击队列的名字可以看到更加详细的信息：**

<img src="https://cdn.nlark.com/yuque/0/2026/png/21376908/1770518372337-f7de6a58-a129-43dc-8c58-e4efa31aa399.png" width="834.4" title="" crop="0,0,1,1" id="u1b6a1998" class="ne-image">

<img src="https://cdn.nlark.com/yuque/0/2026/png/21376908/1770518500458-7788b87e-8ce1-4ff6-9b20-7e913deb3af3.png" width="728" title="" crop="0,0,1,1" id="u227340a4" class="ne-image">

通过这个管理界面可以看到，虽然生产者端程序已经结束了。但是这个消息并没有消失，消息就一直存放在消息队列中，等待消费。

### 编写消费者端 Consumer
消费者端属于被动接收消息，因此给消费者端注册一个回调函数。

```java
package com.jkweilai.rabbitmq;

import com.rabbitmq.client.*;

import java.io.IOException;

public class Consumer {
    public static void main(String[] args) throws Exception{
        ConnectionFactory connectionFactory = new ConnectionFactory();
        connectionFactory.setHost("localhost");
        connectionFactory.setPort(5672);
        connectionFactory.setVirtualHost("/");
        connectionFactory.setUsername("admin");
        connectionFactory.setPassword("123456");

        Connection connection = connectionFactory.newConnection();
        Channel channel = connection.createChannel();

        // 生产者主动发送消息，是同步调用。
        // 消费者被动接收消息，采用事件驱动模型。
        // 因此需要为消费者指定一个回调方法，当消息到达时自动触发。
        // 以下代码创建消费者
        DefaultConsumer consumer = new DefaultConsumer(channel){
            // 参数1: 消费者标识符，用于区分不同的消费者
            // 参数2: 消息的包装信息，包含元数据
            // 参数3: 消息的属性信息，如头信息、优先级等
            // 参数4: 消息体内容，即生产者发送的实际数据
            @Override
            public void handleDelivery(String consumerTag, Envelope envelope, AMQP.BasicProperties properties, byte[] body) throws IOException {
                System.out.println("consumerTag:" + consumerTag);
                System.out.println("Exchange:" + envelope.getExchange());
                System.out.println("RoutingKey:" + envelope.getRoutingKey());
                System.out.println("properties:" + properties);
                System.out.println("Content:" + new String(body));
            }
        };

        // 声明队列（为什么要在消费端声明队列？因为消费端要从这个队列进行消费，如果启动消费端的时候生产者端一次也没有运行过，需要写下面这一行代码）
        channel.queueDeclare("simple_queue",true, false, false, null);

        // 参数1: 要监听的队列名称
        // 参数2: 是否自动确认消息，true表示消费者收到后RabbitMQ立即从队列删除该消息
        // 参数3: 消费者对象，用于处理接收到的消息（即包含handleDelivery方法的回调对象）
        // 这个代码的作用是：注册回调。
        channel.basicConsume("simple_queue", true, consumer);

    }
}

```

运行效果如下：

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1763812439379-4c387399-23b4-409e-a46f-7f3c85a41f83.png" width="712.8" title="" crop="0,0,1,1" id="u778abd7f" class="ne-image">

**再次查看 web 端管理界面，可以看到消费者端已经将消息消费了，消息队列中的消息被删除了：**

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1763812525076-4531aa60-2db4-40a2-bb27-5abb1360f013.png" width="840" title="" crop="0,0,1,1" id="ua73f5458" class="ne-image">

## 对第一个 HelloWorld 程序的理解
**工作流程：**

1. **建立连接**：生产者和消费者都需要与**RabbitMQ服务器**建立一个TCP连接，并在其上创建一个通道（Channel）。
2. **发送消息**：生产者通过 Channel 将消息发送给**默认交换机**，**默认交换机**通过路由键 `simple_queue`将消息路由到 `simple_queue`队列。
    1. 没有指定交换机，Broker 使用默认交换机。
    2. **在默认交换机中，路由键就是队列名**
3. **存储消息**：Broker 将**接收到的消息**存储在**指定的队列**中，等待被消费。
4. **接收消息**：消费者通过 Channel **监听**指定的队列。
5. **消费消息**：当队列中有消息时，Broker 会将消息推送给消费者。消费者接收到消息并进行处理。
6. **确认消息**：消费者处理完消息后，会向 Broker 发送一个**确认信号（ack）**，告知消息已被成功处理。Broker 随后从队列中永久删除该消息。