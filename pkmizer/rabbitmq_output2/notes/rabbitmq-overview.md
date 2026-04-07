color:rgb(15, 17, 21);">Erlang</font> | <font style="color:rgb(15, 17, 21);">Java</font> | <font style="color:rgb(15, 17, 21);">Java</font> | <font style="color:rgb(15, 17, 21);">Scala/Java</font> |
| **<font style="color:rgb(15, 17, 21);">单机吞吐量</font>** | **<font style="color:rgb(15, 17, 21);">几万级/秒</font>** | **<font style="color:rgb(15, 17, 21);">万级/秒</font>** | **<font style="color:rgb(15, 17, 21);">十万级/秒（双十一有战绩）</font>** | **<font style="color:rgb(15, 17, 21);">十万至百万级/秒</font>** |
| **<font style="color:rgb(15, 17, 21);">消息延迟</font>** | **<font style="color:rgb(15, 17, 21);">微秒～毫秒级</font>** | <font style="color:rgb(15, 17, 21);">毫秒级</font> | **<font style="color:rgb(15, 17, 21);">毫秒级</font>** | <font style="color:rgb(15, 17, 21);">毫秒级（受批处理影响）</font> |
| **<font style="color:rgb(15, 17, 21);">消息确认机制</font>** | **<font style="color:rgb(15, 17, 21);">最完善</font>** | <font style="color:rgb(15, 17, 21);"></font> |  |  |
| **<font style="color:rgb(15, 17, 21);"></font>** | **<font style="color:rgb(15, 17, 21);">仍然是普通微服务项目最常用</font>** | <font style="color:rgb(15, 17, 21);">比较老了，使用较少</font> | 阿里系的用的多 | 大数据领域专用 |


# RabbitMQ 概述
## RabbitMQ 简介
1. 官网地址：[https://www.rabbitmq.com/](https://www.rabbitmq.com/)
2. logo：

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1763734245609-f8dcb23b-667a-456e-b58d-e4c54b1c153c.png" width="212.8" title="" crop="0,0,1,1" id="u6ebbde96" class="ne-image">

3. RabbitMQ 是一款基于 AMQP、由 Erlang 语言开发的消息队列产品。2007 年由 Rabbit 技术公司发布了 1.0 版本。

## RabbitMQ 的内部体系结构
<img src="https://cdn.nlark.com/yuque/0/2026/png/21376908/1770514323809-f3218018-7787-4c0b-9d01-998cff08e415.png" width="1462.4" title="" crop="0,0,1,1" id="ua4206fcc" class="ne-image">

### 生产者 Producer 与消费者 Consumer
消息的发送端被称为**生产者 Producer**

消息的接收端被称为**消费者 Consumer**

**Producer **和 **Consumer** 都可以是 Spring Cloud 当中的一个**微服务**

### 消息队列中的 Connection 与 Channel
当**生产者发送消息**的时候，或者**消费者接收消息**的时候，都必须与**消息队列服务器**建立连接，这个连接被称为 **Connection**。但是这个 Connection 是基于 TCP 协议的，如果每一次连接都进行三次握手，那效率就会很低，怎么能够提高效率呢？如果让 Connection 复用就可以提升效率了，因此在 Connection 中弄了很多 Channel。

**<font style="color:rgb(15, 17, 21);"></font>**

**<font style="color:rgb(15, 17, 21);">Connection（连接）：重量级的TCP长连接</font>**

+ <font style="color:rgb(15, 17, 21);">这是一个建立在TCP协议之上的网络连接。创建和销毁它需要三次握手和四次挥手，开销很大。</font>

**<font style="color:rgb(15, 17, 21);">Channel（信道）：轻量级的逻辑连接</font>**

+ <font style="color:rgb(15, 17, 21);">Channel是建立在</font>**<font style="color:rgb(15, 17, 21);">一个Connection内部的虚拟连接</font>**<font style="color:rgb(15, 17, 21);">。它是一个逻辑概念，不存在于TCP层。</font>
+ <font style="color:rgb(15, 17, 21);">创建和销毁Channel的开销极低，因为它</font>**<font style="color:rgb(15, 17, 21);">不需要进行网络握手</font>**<font style="color:rgb(15, 17, 21);">。</font>
+ <font style="color:rgb(15, 17, 21);">它的主要作用是</font>**<font style="color:rgb(15, 17, 21);">实现多路复用</font>**<font style="color:rgb(15, 17, 21);">，允许在单个Connection上同时进行多个不同的消息流操作。</font>

**现实生活中的例子：**

+ **<font style="color:rgb(15, 17, 21);">Connection</font>**<font style="color:rgb(15, 17, 21);"> </font><font style="color:rgb(15, 17, 21);">就像是在两个城市之间修建的一条</font>**<font style="color:rgb(15, 17, 21);">高速公路</font>**<font style="color:rgb(15, 17, 21);">。修路的成本很高（TCP握手），但一旦修好，就可以长期使用。</font>
+ **<font style="color:rgb(15, 17, 21);">Channel</font>**<font style="color:rgb(15, 17, 21);"> 就像是这条高速公路上的一条条</font>**<font style="color:rgb(15, 17, 21);">独立车道</font>**<font style="color:rgb(15, 17, 21);">。你可以在一条高速路上轻松地划出多条车道（创建Channel），每条车道都可以同时跑不同的车（传输不同的消息），互不干扰。开辟新车道的成本很低，不需要重新修路。</font>

### <font style="color:rgb(15, 17, 21);">Broker</font>
每个 RabbitMQ 的实例被称为 Broker。就是 RabbitMQ 主体服务器本身，负责接收和分发消息。<font style="color:rgb(15, 17, 21);">在实际生产环境中，为了实现高可用和高性能，我们通常不会只使用一个 Broker。我们会将多个 Broker 实例组成一个</font>**<font style="color:rgb(15, 17, 21);">集群</font>**<font style="color:rgb(15, 17, 21);">。</font>

### <font style="color:rgb(15, 17, 21);">Virtual Host</font>
虚拟分组，在每个 Broker 实例中可以划分多个虚拟分组（**Virtual Host 可以有很多个，但一般一个分布式系统对应一个 Virtual Host**）。

用户在自己的 Virtual Host 中使用 RabbitMQ。

在实际开发中，通过 Virtual Host 区分不同项目。

### Exchange 与 Queue
翻译为交换机，是消息到达之后的第一站。也就是发送消息的时候，先把消息发送到交换机上。再通过交换机这个中转站把消息发到队列（Queue）上。

注意：Exchange 不负责存储消息，只是消息的中转站。真正存储消息的是 Queue。如果被消费端取走的话，也是从队列 Queue 中删除。

Exchange 可以有很多个。Queue 也可以有很多个。

交换机是如何知道将消息发送到哪个队列呢？就看 Exchange 和 Queue 之间的绑定关系（**路由键**）。

Exchange 可以绑定一个队列 Queue，也可以绑定多个队列 Queue。

### 一条消息的发送与接收流程
<font style="color:rgb(15, 17, 21);">想象一下，你是一个</font>**<font style="color:rgb(15, 17, 21);">生产者（Producer）</font>**<font style="color:rgb(15, 17, 21);">，比如一个订单微服务，需要发送一条“订单创建”的消息。你首先需要与远方的</font>**<font style="color:rgb(15, 17, 21);">RabbitMQ Broker</font>**<font style="color:rgb(15, 17, 21);">（消息中转局）建立一条</font>**<font style="color:rgb(15, 17, 21);">Connection</font>**<font style="color:rgb(15, 17, 21);">（好比在两个城市间修建了一条高速公路）。为了高效，你在这条公路上轻松地开辟了一条</font>**<font style="color:rgb(15, 17, 21);">Channel</font>**<font style="color:rgb(15, 17, 21);">（一条专用车道）。你沿着这条车道，把消息寄给了Broker里的一个</font>**<font style="color:rgb(15, 17, 21);">Exchange</font>**<font style="color:rgb(15, 17, 21);">（中央分拣中心）。Exchange根据你提供的地址（路由键）与 </font>**<font style="color:rgb(15, 17, 21);">Queue</font>**<font style="color:rgb(15, 17, 21);">（暂存仓库）的绑定关系，将消息精准地投递到“订单队列”仓库中。此时，作为</font>**<font style="color:rgb(15, 17, 21);">消费者（Consumer）</font>**<font style="color:rgb(15, 17, 21);"> 的库存微服务，也建立了一条到Broker的高速公路和自己的车道，它一直在“订单队列”仓库边守候，消息一来便立刻取走处理。所有这些组件（订单微服务、库存微服务、订单队列）都隔离在同一个</font>**<font style="color:rgb(15, 17, 21);">Virtual Host</font>**<font style="color:rgb(15, 17, 21);">（例如“电商项目组”）内，与其它项目互不干扰。至此，消息成功完成了一次从发送到接收的旅程。</font>

<font style="color:rgb(15, 17, 21);"></f