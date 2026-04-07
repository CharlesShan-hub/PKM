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
| **<font style="color:rgb(15, 17, 21);">开发语言</font>** | <font style="color:rgb(15, 17, 21);">Erlang</font> | <font style="color:rgb(15, 17, 21);">Java</font> | <font style="color:rgb(15, 17, 21);">Java</font> | <font style="color:rgb(15, 17, 21);">Scala/Java</font> |
| **<font style="color:rgb(15, 17, 21);">单机吞吐量</font>** | **<font style="color:rgb(15, 17, 21);">几万级/秒</font>** | **<font style="color:rgb(15, 17, 21);">万级/秒</font>** | **<font style="color:rgb(15, 17, 21);">十万级/秒（双十一有战绩）</font>** | **<font style="color:rgb(15, 17, 21);">十万至百万级/秒</font>** |
| **<font style="color:rgb(15, 17, 21);">消息延迟</font>** | **<font style="color:rgb(15, 17, 21);">微秒～毫秒级</font>** | <font style="color:rgb(15, 17, 21);">毫秒级</font> | **<font style="color:rgb(15, 17, 21);">毫秒级</font>** | <font style="color:rgb(15, 17, 21);">毫秒级（受批处理影响）</font> |
| **<font style="color:rgb(15, 17, 21);">消息确认机制</font>** | **<font style="color:rgb(15, 17, 21);">最完善</font>** | <font style="color:rgb(15, 17, 21);"></font> |  |  |
| **<font style="color:rgb(15, 17, 21);"></font>** | **<font style="color:rgb(15, 17, 21);">仍然是普通微服务项目最常用</font>** | <font style="color:rgb(15, 17, 21);">比较老了，使用较少</font> | 阿里系的用的多 | 大数据领域专用 |