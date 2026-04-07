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

## <font style="color:rgb(15, 17, 21);">Publish/Subscribe（发布与订阅模式）</font>
### 模式的理解
<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1763812763977-8b21dbf4-5a5b-4fa0-ac0c-54e3491d3d9f.png" width="331.2" title="" crop="0,0,1,1" id="u48fb8197" class="ne-image">

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1763813424160-d1688434-0dd2-4503-9edf-9e7ec0fbc727.png" width="587" title="" crop="0,0,1,1" id="u62d10bd2" class="ne-image">

+ <font style="color:rgb(15, 17, 21);">一个生产者，</font>**<font style="color:rgb(15, 17, 21);">多个队列</font>**<font style="color:rgb(15, 17, 21);">，多个消费者</font>
+ **<font style="color:rgb(15, 17, 21);">一条消息被所有消费者处理</font>**<font style="color:rgb(15, 17, 21);">（每个队列都收到消息的副本）</font>
+ <font style="color:rgb(15, 17, 21);">用于</font>**<font style="color:rgb(15, 17, 21);">广播，</font>**<font style="color:rgb(15, 17, 21);">让</font>**<font style="color:rgb(15, 17, 21);">所有消费者都收到同一条消息</font>**
+ **<font style="color:#DF2A3F;">发布与订阅模式要求交换机的类型必须是：fanout 类型。</font>**

### <font style="color:rgb(15, 17, 21);">交换机(Exchange)</font>
生产者把消息发送到交换机。

交换机接收消息，如何处理消息取决于交换机的类型。

**常见的 3 种交换机类型：**

1. **Fanout 交换机：广播，将消息发送到绑定交换机的队列。**
2. **Direct 交换机：定向，把消息发给符合路由键（routing key）的队列。**
3. **Topic 交换机：通配符，把消息发给符合 routing pattern 的队列。**



**注意：交换机不存储消息，只是一个消息中转站，如果交换机没有找到对应的队列， 消息将****<font style="color:#DF2A3F;">丢失</font>****。**

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

## <font style="color:rgb(15, 17, 21);">Routing（Direct路由模式）</font>
这种模式是我们最常用的，几乎 99%都是使用它。

### 模式的理解
<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1763812783407-98de9cf3-2daa-4a8f-a3ab-8ac67af00136.png" width="264.8" title="" crop="0,0,1,1" id="u4a14a94f" class="ne-image">

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1763813799660-92f2f352-69f4-4e5e-8d82-27e576145ef0.png" width="736" title="" crop="0,0,1,1" id="u7494a962" class="ne-image">

**<font style="color:rgb(15, 17, 21);">生产者发送消息时指定一个路由键，交换机根据路由键的精确匹配，将消息只投递到绑定键完全相同的队列。</font>**

**<font style="color:rgb(15, 17, 21);">消费者也可以选择性的只接收自己关心的特定路由键的消息</font>**

**<font style="color:rgb(15, 17, 21);">交换机类型</font>**<font style="color:rgb(15, 17, 21);">：使用 </font>**<font style="color:rgb(15, 17, 21);">Direct Exchange</font>**

**<font style="color:rgb(15, 17, 21);">精确匹配</font>**<font style="color:rgb(15, 17, 21);">：消息的</font>**<font style="color:rgb(15, 17, 21);">路由键</font>**<font style="color:rgb(15, 17, 21);">必须与队列的</font>**<font style="color:rgb(15, 17, 21);">绑定键</font>**<font style="color:rgb(15, 17, 21);">完全一致</font>

### <font style="color:rgb(15, 17, 21);">编写生产者</font>
```java
package com.jkweilai.rabbitmq.routing;

import com.jkweilai.rabbitmq.util.ConnectionUtil;
import com.rabbitmq.client.BuiltinExchangeType;
import com.rabbitmq.client.Channel;
import com.rabbitmq.client.Connection;

// 1.创建交换机（指定交换机类型）
// 2.创建队列
// 3.使用路由键绑定交换机和队列
// 4.发送消息时指定交换机+路由键
public class Producer {
    public static void main(String[] args) throws Exception {
        Connection connection = ConnectionUtil.getConnection();
        Channel channel = connection.createChannel();

        // 创建交换机
        String exchangeName = "direct_exchange";
        channel.exchangeDeclare(exchangeName, BuiltinExchangeType.DIRECT, true, false, false, null);

        // 创建两个队列
        String queueName1 = "direct_queue1";
        String queueName2 = "direct_queue2";
        channel.queueDeclare(queueName1, true, false, false, null);
        channel.queueDeclare(queueName2, true, false, false, null);

        // 给第一个队列绑定1个路由键。(1个bindingKey)
        channel.queueBind(queueName1, exchangeName, "info");

        // 给第二个队列绑定3个路由键。(3个bindingKey)
        channel.queueBind(queueName2, exchangeName, "info");
        channel.queueBind(queueName2, exchangeName, "error");
        channel.queueBind(queueName2, exchangeName, "warning");

        // 发送消息
        String msg = "2025-10-10 20:20:10 [INFO] 账户A向账户B转账10000.0元";
        // 发送消息时指定路由键（routingKey）
        channel.basicPublish(exchangeName, "info", null, msg.getBytes());

        // 释放资源
        channel.close();
        connection.close();
    }
}

```

**运行结果如下：**

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1763865204269-587a18f3-9a06-45c7-bc0c-2e1687f10bf5.png" width="949.6" title="" crop="0,0,1,1" id="ua846b666" class="ne-image">

### 编写两个消费者
消费者 1：

```java
package com.jkweilai.rabbitmq.routing;

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
        channel.queueDeclare("direct_queue1",true, false, false, null);
        // 注册回调函数，开始消费
        channel.basicConsume("direct_queue1", true, consumer);
    }
}

```

消费者 2：

```java
package com.jkweilai.rabbitmq.routing;

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
        channel.queueDeclare("direct_queue2",true, false, false, null);
        // 注册回调函数，开始消费
        channel.basicConsume("direct_queue2", true, consumer);
    }
}

```



运行结果：

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1763866053624-7f6859d0-043d-405c-beed-bc0575c35f34.png" width="535.2" title="" crop="0,0,1,1" id="u68ae9af0" class="ne-image">

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1763866068204-d6c6d3e3-4a62-40e8-86f1-8cce5bd16967.png" width="524.8" title="" crop="0,0,1,1" id="ua23393b1" class="ne-image">

接下来，可以将发送消息时的路由键修改一下，再观察一下发送到哪个队列了。进而理解路由模式。



## Topics（主题模式）
### 模式的理解
<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1763812791351-3b855a2e-2805-4e2b-87ba-1d00ffeaa80f.png" width="259.2" title="" crop="0,0,1,1" id="uac084399" class="ne-image">

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1763813986720-72095c2d-a0ac-465d-bbe7-0f7eb3ffd5e5.png" width="935.4000244140625" title="" crop="0,0,1,1" id="u38a0c504" class="ne-image">

**<font style="color:rgb(15, 17, 21);">在Routing模式的基础上，支持使用通配符进行更灵活的模式匹配，实现基于主题的消息路由。</font>**

**<font style="color:rgb(15, 17, 21);">通配符匹配</font>**<font style="color:rgb(15, 17, 21);">：支持 </font>`<font style="color:rgb(15, 17, 21);background-color:rgb(235, 238, 242);">*</font>`<font style="color:rgb(15, 17, 21);">（匹配一个单词）和 </font>`<font style="color:rgb(15, 17, 21);background-color:rgb(235, 238, 242);">#</font>`<font style="color:rgb(15, 17, 21);">（匹配零个或多个单词）</font>

**<font style="color:rgb(15, 17, 21);">交换机类型</font>**<font style="color:rgb(15, 17, 21);">：使用 </font>**<font style="color:rgb(15, 17, 21);">Topic Exchange</font>**

**<font style="color:rgb(15, 17, 21);">灵活路由</font>**<font style="color:rgb(15, 17, 21);">：基于主题的发布订阅，比Direct模式更灵活</font>

### <font style="color:rgb(15, 17, 21);">编写生产者端</font>
```java
package com.jkweilai.rabbitmq.topic;

import com.jkweilai.rabbitmq.util.ConnectionUtil;
import com.rabbitmq.client.BuiltinExchangeType;
import com.rabbitmq.client.Channel;
import com.rabbitmq.client.Connection;

// 1.创建交换机（指定交换机类型）
// 2.创建队列
// 3.使用 模糊路由键 绑定交换机和队列
// 4.发消息的时候指定交换机和具体的路由键
public class Producer {
    public static void main(String[] args) throws Exception {
        Connection connection = ConnectionUtil.getConnection();
        Channel channel = connection.createChannel();

        // 创建交换机
        String exchangeName = "topic_exchange";
        channel.exchangeDeclare(exchangeName, BuiltinExchangeType.TOPIC, true, false, false, null);

        // 创建两个队列
        String queueName1 = "topic_queue1";
        String queueName2 = "topic_queue2";
        channel.queueDeclare(queueName1, true, false, false, null);
        channel.queueDeclare(queueName2, true, false, false, null);

        // 交换机 + 队列1 + bindingKey(主题Key/模糊Key)
        // 需求：所有error级别的日志都插入到数据库。order系统的日志都插入到数据库。
        channel.queueBind(queueName1, exchangeName, "#.error");
        channel.queueBind(queueName1, exchangeName, "order.*");
        // 交换机 + 队列2 + bindingKey(主题Key/模糊Key)
        channel.queueBind(queueName2, exchangeName, "*.*");

        // 发送消息时指定路由键（routingKey）
        channel.basicPublish(exchangeName, "order.info", null, "2025-10-10 20:20:10 [INFO] 生成订单".getBytes());
        //channel.basicPublish(exchangeName, "goods.info", null, "2025-10-10 20:20:10 [INFO] 商品入库".getBytes());
        //channel.basicPublish(exchangeName, "goods.error", null, "2025-10-10 20:20:10 [ERROR] 商品保存失败".getBytes());

        // 释放资源
        channel.close();
        connection.close();
    }
}

```

### 编写两个消费者端
消费者 1：

```java
package com.jkweilai.rabbitmq.topic;

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
        channel.queueDeclare("topic_queue1",true, false, false, null);
        // 注册回调函数，开始消费
        channel.basicConsume("topic_queue1", true, consumer);
    }
}

```

消费者 2：

```java
package com.jkweilai.rabbitmq.topic;

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
        channel.queueDeclare("topic_queue2",true, false, false, null);
        // 注册回调函数，开始消费
        channel.basicConsume("topic_queue2", true, consumer);
    }
}

```



**反复测试：**

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1763868305814-4ac2b9c0-c5b5-4298-8b7c-2eb26c8cca06.png" width="1012.8" title="" crop="0,0,1,1" id="uef583f68" class="ne-image">

## <font style="color:rgb(15, 17, 21);">RPC 模式</font>
<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1763812799030-a3ba00c8-1256-4d51-b4dc-900d55874864.png" width="333.6" title="" crop="0,0,1,1" id="uc75dbda8" class="ne-image">

**<font style="color:rgb(15, 17, 21);">通过消息队列实现远程过程调用，生产者发送请求消息并</font>****<font style="color:#DF2A3F;">同步等待</font>****<font style="color:rgb(15, 17, 21);">消费者返回响应结果。</font>**

<font style="color:rgb(15, 17, 21);">这是一种利用消息队列 </font>**<font style="color:rgb(15, 17, 21);">“笨拙地”实现同步调用</font>**<font style="color:rgb(15, 17, 21);"> 的方式，让发送请求的程序像调用本地函数一样，停下来等待远方的处理结果。</font>

<font style="color:rgb(15, 17, 21);">很少用：因为它本质上是在用一个为 </font>**<font style="color:rgb(15, 17, 21);">“异步通信”</font>**<font style="color:rgb(15, 17, 21);"> 设计的工具（消息队列）去实现 </font>**<font style="color:rgb(15, 17, 21);">“同步通信”</font>**<font style="color:rgb(15, 17, 21);"> 的功能，显得很别扭。现在我们有更专业、更高效的替代方案：</font>**<font style="color:rgb(15, 17, 21);">gRPC 、Dubbo、Spring Cloud OpenFeign 等。</font>**

**<font style="color:rgb(15, 17, 21);"></font>**

## <font style="color:rgb(15, 17, 21);">Publisher Confirms（发布者确认机制）</font>
**这个是可靠性机制，不是工作模式。**

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1763812807667-ece845ec-e010-4efd-80b1-05b8cfd064c6.png" width="264" title="" crop="0,0,1,1" id="u13c2cf2f" class="ne-image">

这个机制是用来确认**<font style="color:rgb(15, 17, 21);">消息是否成功到达 RabbitMQ（Broker）</font>**

**<font style="color:rgb(15, 17, 21);">生产者发送消息后，Broker会异步返回一个确认信号，确保</font>****<font style="color:#DF2A3F;">消息已收到并持久化到磁盘</font>****<font style="color:rgb(15, 17, 21);">，从而实现可靠的消息投递。</font>**

**<font style="color:rgb(15, 17, 21);">解决了什么问题？</font>**<font style="color:rgb(15, 17, 21);"> 防止消息在传输过程中（Broker接收后、存盘前）因服务器宕机而丢失。</font>

**<font style="color:rgb(15, 17, 21);">典型场景？</font>**<font style="color:rgb(15, 17, 21);"> 用在金融交易、订单处理等不允许消息丢失的业务中。</font>

<font style="color:rgb(15, 17, 21);"></font>