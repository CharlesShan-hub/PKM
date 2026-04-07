el:
    com.jkweilai.mq.listener.MyMessageListener: info
```

## 编写消费端的监听器
```java
package com.jkweilai.mq.listener;

import com.rabbitmq.client.Channel;
import org.springframework.amqp.core.Message;
import org.springframework.amqp.rabbit.annotation.Exchange;
import org.springframework.amqp.rabbit.annotation.Queue;
import org.springframework.amqp.rabbit.annotation.QueueBinding;
import org.springframework.amqp.rabbit.annotation.RabbitListener;
import org.springframework.stereotype.Component;

@Component
public class MyMessageListener {

    // 交换机名称
    public static final String EXCHANGE_NAME = "exchange.direct.order";
    // 路由键
    public static final String ROUTING_KEY = "order";
    // 队列名称
    public static final String QUEUE_NAME = "queue.order";

    // 该注解中三个属性作用是：如果生产者没有创建队列，没有创建交换机，没有进行路由键绑定，在消费端完成创建与绑定。
    @RabbitListener(bindings = @QueueBinding(
            // 队列 (durable = "true" 表示队列是持久化的，也就是说RabbitMQ服务器重启后，队列以及队列中的消息还在。)
            value = @Queue(value = QUEUE_NAME, durable = "true"),
            // 交换机
            exchange = @Exchange(value = EXCHANGE_NAME),
            // 路由键
            key = {ROUTING_KEY}
    ))
    public void processMessage(String dataString, Message message, Channel channel) {
        // 参数总结：
        // String dataString - 消息体内容（自动反序列化的字符串）
        // Message message   - 完整的原始消息对象（包含头信息、属性等元数据）
        // Channel channel   - RabbitMQ信道（用于手动确认、拒绝等操作）
        System.out.println("消费