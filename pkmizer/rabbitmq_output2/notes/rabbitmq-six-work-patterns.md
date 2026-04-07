1" id="ucc7d7a02" class="ne-image">



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
**<font style="color:rgb(15, 17, 21);">工作流程：</font>**

1. **<font style="color:rgb(15, 17, 21);">建立连接</font>**<font style="color:rgb(15, 17, 21);">：生产者和消费者都需要与</font>**<font style="color:rgb(15, 17, 21);">RabbitMQ服务器</font>**<font style="color:rgb(15, 17, 21);">建立一个TCP连接，并在其上创建一个通道（Channel）。</font>
2. **<font style="color:rgb(15, 17, 21);">发送消息</font>**<font style="color:rgb(15, 17, 21);">：生产者通过 Channel 将消息发送给</font>**<font style="color:rgb(15, 17, 21);"> 默认交换机</font>**<font style="color:rgb(15, 17, 21);">，</font>**<font style="color:rgb(15, 17, 21);">默认交换机</font>**<font style="color:rgb(15, 17, 21);">通过路由键 </font>`<font style="color:rgb(15, 17, 21);">simple_queue</font>`<font style="color:rgb(15, 17, 21);">将消息路由到 </font>`<font style="color:rgb(15, 17, 21);">simple_queue</font>`<font style="color:rgb(15, 17, 21);">队列。</font>
    1. <font style="color:rgb(15, 17, 21);">没有指定交换机，Broker 使用默认交换机。</font>
    2. **<font style="color:rgb(15, 17, 21);">在默认交换机中，路由键就是队列名</font>**
3. **<font style="color:rgb(15, 17, 21);">存储消息</font>**<font style="color:rgb(15, 17, 21);">：Broker 将</font>**<font style="color:rgb(15, 17, 21);">接收到的消息</font>**<font style="color:rgb(15, 17, 21);">存储在</font>**<font style="color:rgb(15, 17, 21);">指定的队列</font>**<font style="color:rgb(15, 17, 21);">中，等待被消费。</font>
4. **<font style="color:rgb(15, 17, 21);">接收消息</font>**<font style="color:rgb(15, 17, 21);">：消费者通过 Channel </font>**<font style="color:rgb(15, 17, 21);">监听</font>**<font style="color:rgb(15, 17, 21);">指定的队列。</font>
5. **<font style="color:rgb(15, 17, 21);">消费消息</font>**<font style="color:rgb(15, 17, 21);">：当队列中有消息时，Broker 会将消息推送给消费者。消费者接收到消息并进行处理。</font>
6. **<font style="color:rgb(15, 17, 21);">确认消息</font>**<font style="color:rgb(15, 17, 21);">：消费者处理完消息后，会向 Broker 发送一个</font>**<font style="color:rgb(15, 17, 21);">确认信号（ack）</font>**<font style="color:rgb(15, 17, 21);">，告知消息已被成功处理。Broker 随后从队列中永久删除该消息。</font>

# <font style="color:rgb(15, 17, 21);">RabbitMQ 的 6 种工作模式</font>
官方文档：[https://www.rabbitmq.com/tutorials](https://www.rabbitmq.com/tutorials)

## Hello World（简单模式）
<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1763812743757-bd1a7e6f-76c2-46a2-992a-b3a928d53565.png" width="264" title="" crop="0,0,1,1" id="ucbd4f050" class="ne-image">

+ <font style="color:rgb(15, 17, 21);">一个生产者，一个队列，一个消费者</font>
+ **<font style="color:#DF2A3F;">最基本</font>****<font style="color:rgb(15, 17, 21);">的点对点模式（点对点：一条消息只被一个消费者消费）</font>**

## <font style="color:rgb(15, 17, 21);">Work Queues（竞争消费者模式）</font>
### 模式的理解
<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1763812754027-913b04c9-bb65-4e08-aaa6-7971135b159c.png" width="255.2" title="" crop="0,0,1,1" id="ud04cf1c5" class="ne-image">



<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1763813286164-824f371b-b050-493d-9874-bf9880bc9fe4.png" width="414.8000183105469" title="" crop="0,0,1,1" id="u610a767c" class="ne-image">

+ <font style="color:rgb(15, 17, 21);">一个生产者，</font>**<font style="color:rgb(15, 17, 21);">一个队列</font>**<font style="color:rgb(15, 17, 21);">，多个消费者</font>
+ **<font style="color:#DF2A3F;">一条消息只被一个消费者处理</font>**<font style="color:rgb(15, 17, 21);">（轮询分发：消费者是竞争状态）</font>
+ <font style="color:rgb(15, 17, 21);">用于</font>**<font style="color:rgb(15, 17, 21);">负载均衡</font>**
+ **<font style="color:rgb(15, 17, 21);">竞争消费者模式又是</font>****<font style="color:#DF2A3F;">通用的</font>****<font style="color:rgb(15, 17, 21);">点对点模式。</font>**

**<font style="color:rgb(15, 17, 21);"></font>**

**<font style="color:rgb(15, 17, 21);">接下来编写代码演示一下。</font>**

### 编写工具类
每一次获取连接太麻烦，封装一个工具类。

```java
package com.jkweilai.rabbitmq.util;

import com.rabbitmq.client.Connection;
import com.rabbitmq.client.ConnectionFactory;

public class ConnectionUtil {

    public static final String HOST_ADDR = "localhost";

    public static Connection getConnection() throws Exception {
        ConnectionFactory factory = new ConnectionFactory();
        factory.setHost(HOST_ADDR);
        factory.setPort(5672);
        factory.setVirtualHost("/");
        factory.setUsername("admin");
        factory.setPassword("123456");
        Connection connection = factory.newConnection();
        return connection;
    }

    public static void main(String[] args) throws Exception {
        System.out.println(ConnectionUtil.getConnection());
    }
}
```

测试工具类是否能够获取连接：

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1763816864351-3440a83d-8bb2-4300-b21c-c377678012b8.png" width="297.6" title="" crop="0,0,1,1" id="u0a3c3191" class="ne-image">

### 编写生产者端
循环 10 次，发送 10 条消息：

```java
package com.jkweilai.rabbitmq.work;

import com.jkweilai.rabbitmq.util.ConnectionUtil;
import com.rabbitmq.client.Channel;
import com.rabbitmq.client.Connection;

public class Producer {
    public static void main(String[] args)throws Exception {
        Connection connection = ConnectionUtil.getConnection();
        Channel channel = connection.createChannel();
        // 声明队列
        channel.queueDeclare("work_queues", true, false, false, null);
        // 发送消息
        for (int i = 1; i <= 10; i++) {
            String msg = "work_queues " + i;
            channel.basicPublish("", "work_queues", null, msg.getBytes());
        }
        // 释放资源
        channel.close();
        connection.close();
    }
}
```

****

**执行后，查看 web 管理界面：**

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1763817187630-94e86371-3b5a-4bd8-8387-a2451799abcf.png" width="1008" title="" crop="0,0,1,1" id="uf9cb9b9e" class="ne-image">

### 编写两个消费者端
**消费者 1：**`**Consumer1**`

```java
package com.jkweilai.rabbitmq.work;

import com.jkweilai.rabbitmq.util.ConnectionUtil;
import com.rabbitmq.client.*;

import java.io.IOException;

public class Consumer1 {
    public static void main(String[] args) throws Exception {
        Connection connection = ConnectionUtil.getConnection();
        Channel channel = connection.createChannel();
        DefaultConsumer consumer = new DefaultConsumer(channel){
            @Override
            public void handleDelivery(String consumerTag, Envelope envelope, AMQP.BasicProperties properties, byte[] body) throws IOException {
                System.out.println("Consumer1:" + new String(body));
                // "Work Queues" 模式要求，收到消息后手动确认
                // 第一个参数：这条消息的"快递单号"（唯一标识）
                // 第二个参数：是否批量确认，false表示只确认这一条
                channel.basicAck(envelope.getDeliveryTag(), false);
            }
        };
        // 声明队列（为什么要在消费端声明队列？因为消费端要从这个队列进行消费，如果启动消费端的时候生产者端一次也没有运行过，需要写下面这一行代码）
        channel.queueDeclare("work_queues",true, false, false, null);
        // "Work Queues" 模式：我一次只能消费1条消息。
        channel.basicQos(1);
        // 注册回调函数，开始消费
        // "Work Queues" 模式要求第二个参数是false。要求是手动确认，不能自动确认。
        channel.basicConsume("work_queues", false, consumer);
    }
}
```

****

**消费者 2：**`**Consumer2**`

```java
package com.jkweilai.rabbitmq.work;

import com.jkweilai.rabbitmq.util.ConnectionUtil;
import com.rabbitmq.client.*;

import java.io.IOException;

public class Consumer2 {
    public static void main(String[] args) throws Exception {
        Connection connection = ConnectionUtil.getConnection();
        Channel channel = connection.createChannel();
        DefaultConsumer consumer = new DefaultConsumer(channel){
            @Override
            public void handleDelivery(String consumerTag, Envelope envelope, AMQP.BasicProperties properties, byte[] body) throws IOException {
                System.out.println("Consumer2:" + new String(body));
                channel.basicAck(envelope.getDeliveryTag(), false);
            }
        };