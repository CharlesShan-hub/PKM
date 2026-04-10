# **RabbitMQ 的 6 种工作模式**
官方文档：[https://www.rabbitmq.com/tutorials](https://www.rabbitmq.com/tutorials)

## Hello World（简单模式）
<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1763812743757-bd1a7e6f-76c2-46a2-992a-b3a928d53565.png" width="264" title="" crop="0,0,1,1" id="ucbd4f050" class="ne-image">

+ **一个生产者，一个队列，一个消费者**
+ 最基本点对点模式（点对点：一条消息只被一个消费者消费）

## **Work Queues（竞争消费者模式）**
### 模式的理解
<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1763812754027-913b04c9-bb65-4e08-aaa6-7971135b159c.png" width="255.2" title="" crop="0,0,1,1" id="ud04cf1c5" class="ne-image">



<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1763813286164-824f371b-b050-493d-9874-bf9880bc9fe4.png" width="414.8000183105469" title="" crop="0,0,1,1" id="u610a767c" class="ne-image">

+ **一个生产者，****一个队列****，多个消费者**
+ ****一条消息只被一个消费者处理******（轮询分发：消费者是竞争状态）**
+ **用于****负载均衡**
+ ****竞争消费者模式又是******通用的******点对点模式。**

****

****接下来编写代码演示一下。**

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
        // 声明队列（为什么要在消费端声明队列？因为消费端要从这个队列进行消费，如果启动消费端的时候生产者端一次也没有运行过，需要写下面这一行代码）
        channel.queueDeclare("work_queues",true, false, false, null);
        channel.basicQos(1);
        // 注册回调函数，开始消费
        channel.basicConsume("work_queues", false, consumer);
    }
}
```

### 测试
先启动两个消费者端，然后再启动生产者端。

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1763817465954-f140df76-5724-4ea8-9265-3dd915436dee.png" width="280" title="" crop="0,0,1,1" id="u78f5b26c" class="ne-image">

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1763817483560-05530e6a-dfad-45cf-90ff-ec6326cb6d7e.png" width="267.2" title="" crop="0,0,1,1" id="u32598a13" class="ne-image">

通过测试，可以看到，消费者确实是竞争的关系。

查看 web 管理界面，也可以看到所有消息已经全部消费了：

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1763817557160-4df2520a-938e-4285-a382-51a511013524.png" width="1160.8" title="" crop="0,0,1,1" id="u99efb5e4" class="ne-image">

## **Publish/Subscribe（发布与订阅模式）**
### 模式的理解
<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1763812763977-8b21dbf4-5a5b-4fa0-ac0c-54e3491d3d9f.png" width="331.2" title="" crop="0,0,1,1" id="u48fb8197" class="ne-image">

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1763813424160-d1688434-0dd2-4503-9edf-9e7ec0fbc727.png" width="587" title="" crop="0,0,1,1" id="u62d10bd2" class="ne-image">

+ **一个生产者，****多个队列****，多个消费者**
+ ****一条消息被所有消费者处理******（每个队列都收到消息的副本）**
+ **用于****广播，****让****所有消费者都收到同一条消息**
+ ****发布与订阅模式要求交换机的类型必须是：fanout 类型。**

### **交换机(Exchange)**
生产者把消息发送到交换机。

交换机接收消息，如何处理消息取决于交换机的类型。

**常见的 3 种交换机类型：**

1. **Fanout 交换机：广播，将消息发送到绑定交换机的队列。**
2. **Direct 交换机：定向，把消息发给符合路由键（routing key）的队列。**
3. **Topic 交换机：通配符，把消息发给符合 routing pattern 的队列。**



**注意：交换机不存储消息，只是一个消息中转站，如果交换机没有找到对应的队列， 消息将****丢失****。**

### 编写生产者代码
和之前代码不同之处：创建一个 Fanout 交换机，让交换机绑定两个队列。然后生产者发消息，Fanout 交换机是广播模式，看看两个队列中是否都有消息。

```java
package com.jkweilai.rabbitmq.fanout;

import com.jkweilai.rabbitmq.util.ConnectionUtil;
import com.rabbitmq.client.BuiltinExchangeType;
import com.rabbitmq.client.Channel;
import com.rabbitmq.client.Connection;

public class Producer {
    public static void main(String[] args) throws Exception {
        Connection connection = ConnectionUtil.getConnection();
        Channel channel = connection.createChannel();

        
        // 声明交换机
        String exchangeName = "fanout_exchange";
        /*
            exchangeName - 交换机的名称标识符
            BuiltinExchangeType.FANOUT - 交换机类型为广播模式（消息发送给所有绑定队列）
            true - 交换机持久化（服务器重启后仍然存在）
            false - 不自动删除交换机（没有消费者时不会自动删除）
            false - 不是内部交换机（内部交换机：只能被其他交换机路由消息，不能被客户端直接发布消息）
            null - 无额外参数（用于高级配置）
         */
        channel.exchangeDeclare(exchangeName, BuiltinExchangeType.FANOUT, true, false, false, null);

        
        // 声明队列1、队列2
        String queueName1 = "fanout_queue1";
        String queueName2 = "fanout_queue2";
        channel.queueDeclare(queueName1, true, false, false, null);
        channel.queueDeclare(queueName2, true, false, false, null);
        
        
        // 交换机绑定队列
        // 第三个参数是指定路由键的，但由于是Fanout交换机，不需要指定路由键，因此空字符串就行。
        channel.queueBind(queueName1, exchangeName, "");
        channel.queueBind(queueName2, exchangeName, "");

        
        // 发消息
        String body = "2025-10-11 12:20:32 User.selectById(#id) invoked";
        /*
            exchangeName - 指定要发布消息的交换机名称
            "" - 路由键为空字符串（在FANOUT模式下路由键被忽略）
            null - 不使用消息属性（如优先级、过期时间等高级设置）
            body.getBytes() - 消息内容转换为字节数组进行传输
         */
        channel.basicPublish(exchangeName, "", null, body.getBytes());

        
        // 释放资源
        channel.close();
        connection.close();
    }
}

```



**运行程序，通过 web 管理界面可以看到，创建了一个交换机：**

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1763827018502-25830d59-3ac9-4f71-9e14-2e32534ad6dd.png" width="854.4" title="" crop="0,0,1,1" id="u9224bdda" class="ne-image">



**再查看队列，看看有没有新建的两个队列，并且每个队列中是否各有一条消息：**

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1763827127364-2d84a1e5-b27d-4868-a205-0a87c4e60e0f.png" width="989.6" title="" crop="0,0,1,1" id="uef63f20c" class="ne-image">



**在 web 管理界面查看具体消息：**

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1763827459580-46edd2d6-97e5-49a0-8106-a001cc1f250a.png" width="840.8" title="" crop="0,0,1,1" id="ua81c9612" class="ne-image">

### 编写两个消费者
**消费者 1：去消费队列 1 中的消息。**

```java
package com.jkweilai.rabbitmq.fanout;

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
            }
        };
        // 声明队列（为什么要在消费端声明队列？因为消费端要从这个队列进行消费，如果启动消费端的时候生产者端一次也没有运行过，需要写下面这一行代码）
        channel.queueDeclare("fanout_queue1",true, false, false, null);
        // 注册回调函数，开始消费
        channel.basicConsume("fanout_queue1", true, consumer);
    }
}

```

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1763827875510-ce69dc72-5c37-428b-9d71-bfd7a779d64a.png" width="491.2" title="" crop="0,0,1,1" id="ua0572b32" class="ne-image">



**消费者 2：去消费队列 2 中的消息。**

```java
package com.jkweilai.rabbitmq.fanout;

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
            }
        };
        // 声明队列（为什么要在消费端声明队列？因为消费端要从这个队列进行消费，如果启动消费端的时候生产者端一次也没有运行过，需要写下面这一行代码）
        channel.queueDeclare("fanout_queue2",true, false, false, null);
        // 注册回调函数，开始消费
        channel.basicConsume("fanout_queue2", true, consumer);
    }
}

```

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1763827893870-3f2c6b90-28e1-4d7f-9eae-c4695152a33f.png" width="488.8" title="" crop="0,0,1,1" id="u249d92ca" class="ne-image">

## **Routing（Direct路由模式）**
这种模式是我们最常用的，几乎 99%都是使用它。

### 模式的理解
<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1763812783407-98de9cf3-2daa-4a8f-a3ab-8ac67af00136.png" width="264.8" title="" crop="0,0,1,1" id="u4a14a94f" class="ne-image">

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1763813799660-92f2f352-69f4-4e5e-8d82-27e576145ef0.png" width="736" title="" crop="0,0,1,1" id="u7494a962" class="ne-image">

****生产者发送消息时指定一个路由键，交换机根据路由键的精确匹配，将消息只投递到绑定键完全相同的队列。****

****消费者也可以选择性的只接收自己关心的特定路由键的消息****

****交换机类型******：使用 ****Direct Exchange****

****精确匹配******：消息