eueDeclare("direct_queue1",true, false, false, null);
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
<img src="https://cdn.nla