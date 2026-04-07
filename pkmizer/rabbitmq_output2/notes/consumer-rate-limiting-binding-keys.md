绑定1个路由键。(1个bindingKey)
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
        channel.qu