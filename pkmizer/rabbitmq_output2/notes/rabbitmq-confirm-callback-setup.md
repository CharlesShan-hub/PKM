private RabbitTemplate rabbitTemplate;

    // 这个注解的作用是：构造方法执行后立即执行该方法。JDK内置注解。
    @PostConstruct
    public void init() {
        rabbitTemplate.setConfirmCallback(this);
        rabbitTemplate.setReturnsCallback(this);
    }
    // =====================这段代码是将回调注册到RabbitTemplate===============================




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
        System.out.println("队列 消息主题：" + new String(returned.getMessage().getBody()));
        System.out.println("队列 应答码：" + returned.getReplyCode());
        System.out.println("队列 应答描述：" + returned.getReplyText());
        System.out.println("队列 对应的交换机：" + returned.getExchange());
        System.out.println("队列 对应的路由键：" + returned.getRoutingKey());
    }
}

```

**第五步：**编写测试程序，发送消息。分别演示三种情况：（1）一切正常的情况。（2）交换机名字写错的情况。（3）队列名字写错的情况。观察回调的执行情况。

```java
package com.jkweilai.mq;

import org.junit.jupiter.api.Test;
import org.springframework.amqp.rabbit.core.RabbitTemplate;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;

@SpringBootTest
class ProducerConfirmApplicationTests {

    @Autowired
    private RabbitTemplate rabbitTemplate;

    // 交换机名称
    public static final String EXCHANGE_NAME = "exchange.direct.order";
    // 路由键
    public static final String ROUTING_KEY = "order";

    @Test
    void test01() {
        // 测试到交换机和队列都成功的情况
        //rabbitTemplate.convertAndSend(EXCHANGE_NAME, ROUTING_KEY, "hello rabbit!");
        // 测试发送到交换机失败
        //rabbitTemplate.convertAndSend(EXCHANGE_NAME + "error", ROUTING_KEY, "hello rabbit!");
        // 测试发送到队列失败
        rabbitTemplate.convertAndSend(EXCHANGE_NAME, ROUTING_KEY + "error", "hello rabbit!");
    }
}

```

三种情况的测试结果：

都成功：

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1763880929607-9a4951f8-2724-4ebe-b81a-fbb2fa4bcbc6.png" width="270.4" title="" crop="0,0,1,1" id="u6c89134f" class="ne-image">

到达交换机失败：

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1763880972864-133eb971-577e-4717-9575-153c66e73e0a.png" width="860" title="" crop="0,0,1,1" id="u602bc35a" class="ne-image">

到达队列失败：

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1763880998739-f9ceee06-4aa8-46af-938e-5bd637bcbb5d.png" width="348.8" title="" crop="0,0,1,1" id="u570f2f2d" class="ne-image">

### 方案 2：启用备用交换机（使用较少）
**注意：测试代码我们使用 SpringBoot 第一次集成 RabbitMQ 的案例。**

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1763882982507-a8195421-f2d2-4760-aa67-6e903afc8505.png" width="844.8" title="" crop="0,0,1,1" id="u1c0d6e15" class="ne-image">

启用备用交换机原理：消息到达目标交换机，目标交换机绑定队列时失败，启用备用交换机， 备用交换机会将消息绑定到其他队列，消费者端一般的消费方式为：**<font style="color:#DF2A3F;">记录日志/告警</font>**（通知运维人员/开发人员等）。



**实现步骤如下：**

**第一步：**创建备用交换机。（注意：备用交换机的类型必须选择 **Fanout**，因为**主交换机**将消息发到**备用交换机**的时候**没有带路由键**，因此备用交换机只能以广播形式将消息发送到其他队列）

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1763881859296-34de893a-8cce-471c-a1ce-bcf459f9982b.png" width="846.4" title="" crop="0,0,1,1" id="u1625aea7" class="ne-image">



**第二步：**创建和备用交换机绑定的**队列**。

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1763881969089-81309191-dbf0-422e-8004-d0849ab609db.png" width="1000" title="" crop="0,0,1,1" id="uedc5b4dc" class="ne-image">



**第三步：**备用交换机绑定新建的队列（**不需要指定路由键，因为该交换机类型是 Fanout**）

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1763882192756-28c0527d-5c8c-4bf4-a6a2-6b3eb51ca8ca.png" width="852" title="" crop="0,0,1,1" id="u9d80c34d" class="ne-image">



**第四步：**目标交换机绑定备用交换机

没有提供修改功能，只能删除目标交换机，重新创建新的目标交换机，然后将目标交换机和备用交换机进行绑定。

**删除目标交换机：**

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1763883298691-5fcc36e2-d036-447c-8b07-9b86a34c0c34.png" width="424.8" title="" crop="0,0,1,1" id="u6160223d" class="ne-image">

**新建目标交换机时绑定备用交换机：**

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1763883450499-f5433ee4-74cd-4f53-9c2c-406c2de19d5b.png" width="789.6" title="" crop="0,0,1,1" id="u4d4f7dd4" class="ne-image">



**第五步：**目标队列 `queue.order` 重新绑定路由键

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1763884014006-e9c321a9-c52a-4b22-891c-9568d72e2733.png" width="831.2" title="" crop="0,0,1,1" id="u8b15cbf4" class="ne-image">



**第六步：**测试

1. 运行我们 SpringBoot 集成 RabbitMQ 的第一个案例的消费端程序。再运行生产端的程序，看看正常情况下，消费端是否能够收到消息。

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1763884414893-24467c3a-e672-4ee6-98cf-9506cb6b3f0b.png" width="256.8" title="" crop="0,0,1,1" id="uf57f4f62" class="ne-image">

2. 接下来将生产端发送消息的代码中路由键修改一下，让路由键不存在，看看备用交换机和备用队列是否能够正常起作用。

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1763884449317-8f601b3a-9274-477e-81d4-889ff08e318b.png" width="899.2" title="" crop="0,0,1,1" id="u02f25e14" class="ne-image">

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1763884522053-9e749943-987e-422e-a3be-3c30e88efba5.png" width="1048.8" title="" crop="0,0,1,1" id="ud0dc2de7" class="ne-image">

## 解决故障情况 2 的具体实践
当消息服务器宕机后，保存在内存当中的消息会丢失，可以将消息进行持久化，这样服务器宕机，消息就不会丢失了。

好消息：对于 SpringBoot 项目集成 RabbitMQ，默认消息就是支持持久化的，比如我们编写这样一段生产者发送消息的代码：

```java
@SpringBootTest
class SpringbootRabbitmqProducerApplicationTests {
    @Resource
    private RabbitTemplate rabbitTemplate;
    @Test
    vo