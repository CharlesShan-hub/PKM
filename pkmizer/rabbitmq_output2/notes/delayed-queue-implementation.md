单".getBytes());
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

## <font style="color:rgb(15, 17