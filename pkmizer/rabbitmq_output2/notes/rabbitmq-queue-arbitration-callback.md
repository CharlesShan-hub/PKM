ate.ReturnsCallback {

    // 消息是否发送到交换机的回调。发送成功或失败，这个回调都会执行。
    // correlationData：消息的"身份证"，用来匹配哪条消息被确认了（你在发送消息时没有设置关联数据时，它是null）
    // ack：投递结果（true=成功，false=失败）
    // cause: 失败原因（成功时为null）
    @Override
    public void confirm(CorrelationData correlationData, boolean ack, String cause) {
        System.out.println("交换机 correlationData：" + correlationData);
        System.out.println("交换机 ack：" + ack);
        System.out.println("交换机 cause：" + cause);
    }

    // 消息是否发送到队列的回调。发送失败，这个回调才会执行。（发送成功，回调不执行。）
    // ReturnedMessage returned - 消息投递失败的完整返回信息包
    @Override
    public void returnedMessage(ReturnedMessage returned) {
        System.out.println("队列 消息主题：" +  new String(returned.getMessage().getBody()));
        System.out.println("队列 应答码：" + returned.getReplyCode());
        System.out.println("队列 应答描述：" + returned.getReplyText());
        System.out.println("队列 对应的交换机：" + returned.getExchange());
        System.out.println("队列 对应的路由键：" + returned.getRoutingKey());
    }
}

```

**第四步：**将回调函数注册到 `RabbitTemplate`对象中。

```java
package com.jkweilai.mq.config;

import jakarta.annotation.PostConstruct;
import org.springframework.amqp.core.ReturnedMessage;
import org.springframework.amqp.rabbit.connection.CorrelationData;
import org.springframework.amqp.rabbit.core.RabbitTemplate;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.annotation.Configuration;

@Configuration
public class ProducerAckConfig implements RabbitTemplate.ConfirmCallback, RabbitTemplate.ReturnsCallback {

    // =====================这段代码是将回调注册到RabbitTemplate===============================
    @Autowired