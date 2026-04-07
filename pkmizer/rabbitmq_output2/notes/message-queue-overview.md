der(Order order) {
        // 1. 验证订单
        validateOrder(order);
        
        // 2. 扣减库存
        inventoryService.deduct(order);
        
        // 3. 创建支付记录
        paymentService.create(order);
        
        // 4. 发送消息到消息队列
        rabbitTemplate.convertAndSend(
            "order.exchange",      // 交换机
            "order.completed",     // 路由键
            order                  // 消息内容
        );
        
        // 5. 记录日志
        logService.log(order);
    }
}
```

**要扩展一个新的功能，只需要额外添加一个类：**

```java
@Component
class SmsConsumer {
    // 消费者从消息队列中消费即可
    @RabbitListener(queues = "sms.queue")
    public void handleOrderMessage(Order order) {
        smsService.sendOrderSMS(order);
    }
}
```

**优势：**

1. <font style="color:rgb(15, 17, 21);"></font>**<font style="color:rgb(15, 17, 21);">不修改核心业务代码</font>**<font style="color:rgb(15, 17, 21);">（OrderService完全不变）</font>
2. **<font style="color:rgb(15, 17, 21);">短信服务挂了不影响订单主流程</font>**<font style="color:rgb(15, 17, 21);">（解耦）</font>
3. **<font style="color:rgb(15, 17, 21);">只需测试新的SmsConsumer</font>**<font style="color:rgb(15, 17, 21);">（隔离测试）</font>

# 消息队列概述
## 什么是消息队列
消息队列就是实现**<font style="color:#DF2A3F;">应用程序</font>**和**<font style="color:#DF2A3F;">应用程序</font>**之间**<font style="color:#DF2A3F;">通信</font>**的中间件产品。



这里的应用程序可以理解为分布式环境下的**<font style="color:#DF2A3F;">微服务</font>**。



<font style="color:rgb(15, 17, 21);">这种通信方式的巨大价值在于实现了应用间的</font>**<font style="color:rgb(15, 17, 21);">解耦</font>**<font style="color:rgb(15, 17, 21);">。具体表现为：</font>**<font style="color:rgb(15, 17, 21);">双方不必同时在线，不必知道对方存在，不必等待对方响应，更不必依赖对方状态</font>**<font style="color:rgb(15, 17, 21);">。它们只需遵守统一的</font>**<font style="color:rgb(15, 17, 21);">通信协议与消息格式</font>**<font style="color:rgb(15, 17, 21);">，提升了系统灵活性。</font>

## <font style="color:rgb(15, 17, 21);">消息队列的通信协议</font>
消息队列的通信协议很多，可以重点关注：**<font style="color:#DF2A3F;">AMQP、JMS。</font>**

1. **<font style="color:#DF2A3F;">AMQP（</font>****<font style="color:rgb(15, 17, 21);">Advanced Message Queuing Protocol 高级消息队列协议</font>****<font style="color:#DF2A3F;">）</font>**<font style="color:#DF2A3F;"> </font><font style="color:rgb(15, 17, 21);">- 一个功能丰富的企业级消息协议，支持复杂的路由、队列和可靠的传输，是RabbitMQ等消息队列的核心。</font>
2. **<font style="color:rgb(15, 17, 21);">MQTT</font>**<font style="color:rgb(15, 17, 21);"> </font><font style="color:rgb(15, 17, 21);">- 一个极其轻量级的发布/订阅协议，专为低功耗、高延迟的物联网设备通信而设计。</font>
3. **<font style="color:rgb(15, 17, 21);">Kafka Protocol</font>**<font style="color:rgb(15, 17, 21);"> </font><font style="color:rgb(15, 17, 21);">- 一个为Kafka设计的二进制协议，核心目标是实现高吞吐量的流数据传输与持久化。</font>
4. **<font style="color:rgb(15, 17, 21);">STOMP</font>**<font style="color:rgb(15, 17, 21);"> </font><font style="color:rgb(15, 17, 21);">- 一个非常简单的、基于文本的协议，它使用类似HTTP的帧格式，使得客户端实现变得容易。</font>
5. **<font style="color:#DF2A3F;">JMS（</font>****<font style="color:rgb(15, 17, 21);">Java Message Service：Java 消息规范，JakartaEE 规范之一</font>****<font style="color:#DF2A3F;">）</font>**<font style="color:#DF2A3F;"> </font><font style="color:rgb(15, 17, 21);">- 一个Java平台的API标准（</font>**<font style="color:rgb(15, 17, 21);">非网络协议</font>**<font style="color:rgb(15, 17, 21);">），它定义了Java应用程序之间使用消息中间件的统一接口。</font>
6. **<font style="color:rgb(15, 17, 21);">OpenWire</font>**<font style="color:rgb(15, 17, 21);"> - 一个高性能的二进制协议，旨在为ActiveMQ提供跨语言的客户端和强大的功能集。</font>

## <font style="color:rgb(15, 17, 21);">主流的 MQ 产品对比</font>
| **<font style="color:rgb(15, 17, 21);"></font>** | **<font style="color:rgb(15, 17, 21);">RabbitMQ</font>** | **<font style="color:rgb(15, 17, 21);">ActiveMQ</font>** | **<font style="color:rgb(15, 17, 21);">RocketMQ</font>** | **<font style="color:rgb(15, 17, 21);">Kafka</font>** |
| --- | --- | --- | --- | --- |
| **<font style="color:rgb(15, 17, 21);">研发团队</font>** | <font style="color:rgb(15, 17, 21);">Rabbit 公司</font> | <font style="color:rgb(15, 17, 21);">Apache</font> | <font style="color:rgb(15, 17, 21);">阿里巴巴 / Apache</font> | <font style="color:rgb(15, 17, 21);">LinkedIn / Apache</font> |
| **<font style="color:rgb(15, 17, 21);">开发语言</font>** | <font style="