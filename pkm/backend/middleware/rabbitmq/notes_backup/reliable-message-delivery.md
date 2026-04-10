# 消息的可靠性投递
什么是可靠性投递：生产者发了一条消息，消费者就要消费一条消息。这才是正常的。但实际应用中可能会出现投递失败。

## 故障及解决方案描述
### 故障情况 1
**消息压根没有发到消息队列**，解决方案包括两个：

1. **在生产者端启用****确认****机制。当消息发送失败（如交换机或队列不存在）时，生产者立即感知并执行重发。**
2. **为****主交换机****配置一个****备份交换机****。当消息无法路由到任何队列时，自动转发到****备份交换机****，保证消息不丢失。**

### 故障情况 2
消息发到消息服务器后，服务器宕机了，导致内存中消息丢失，解决方案是：**将消息持久化到硬盘上。**

### 故障情况 3
消息发到消息服务器了，消息服务器也没有宕机，但是消费端在消费的时候出现异常了。导致消息没有成功消费，解决方案是：

1. ****成功则确认******：处理成功时消费端返回确认(ACK)，消息服务器删除消息。**
2. ****失败则拒收******：处理失败时消费端返回(NACK)，消息可以重新入队等待再次消费。（这属于消费端的重试机制）**

## **解决故障情况 1 的具体实践**
### 方案 1：生产端确认机制
**第一步：**创建生产端的 SpringBoot 项目 `**producer-confirm**`，引入依赖。操作和之前相同。

```xml
<dependencies>
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-amqp</artifactId>
    </dependency>
    <dependency>
        <groupId>org.projectlombok</groupId>
        <artifactId>lombok</artifactId>
        <optional>true</optional>
    </dependency>
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-test</artifactId>
        <scope>test</scope>
    </dependency>
</dependencies>
```

**第二步：**在 `application.yml`中启用生产端确认机制。重点关注以下****两个配置****。

```yaml
spring:
  rabbitmq:
    host: localhost
    port: 5672
    username: admin
    password: 123456
    virtual-host: /
    publisher-confirm-type: correlated # 启用交换机的确认
    publisher-returns: true # 启用队列的确认
```

**第三步：**编写配置类，配置类中编写交换机的回调和队列的回调。（**对方收到还是没有收到，我们生产端是不知道的，只能编写回调，等着别人通知咱。**）

```java
package com.jkweilai.mq.config;

import org.springframework.amqp.core.ReturnedMessage;
import org.springframework.amqp.rabbit.connection.CorrelationData;
import org.springframework.amqp.rabbit.core.RabbitTemplate;
import org.springframework.context.annotation.Configuration;

@Configuration
public class ProducerAckConfig implements RabbitTemplate.ConfirmCallback, RabbitTemplate.ReturnsCallback {

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

启用备用交换机原理：消息到达目标交换机，目标交换机绑定队列时失败，启用备用交换机， 备用交换机会将消息绑定到其他队列，消费者端一般的消费方式为：****记录日志/告警****（通知运维人员/开发人员等）。



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
    void test01() {
        rabbitTemplate.convertAndSend("exchange.direct.order", "order", "hello rabbit mq!!!");
    }
}
```

执行测试程序，完成消息的发送，接下来，我们从 web 管理界面上可以看到下图效果：

<img src="https://cdn.nlark.com/yuque/0/2026/png/21376908/1770631688431-6990d3c1-7bd4-4add-a80c-fd0769e0ae64.png" width="418.4" title="" crop="0,0,1,1" id="u899499b6" class="ne-image">

## 解决故障情况 3 的具体实践
消费端在消费的过程中如果**出现了异常**表示**消费失败**，如果**没有出现异常**表示**消费成功**。

消费成功，返回 ACK，消息队列将消息删除。

消费失败，返回 NACK，消费端可以选择：**将消息重新放回队列再次消费 **或 **发出告警信息**。



**实现步骤如下：**

**第一步：**创建 SpringBoot 项目 `consumer-confirm`，引入依赖：

```xml
<dependencies>
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-amqp</artifactId>
    </dependency>
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-web</artifactId>
    </dependency>
</dependencies>
```

**第二步：**编写 yml 配置文件（**添加一项重要的配置**）

```yaml
spring:
  rabbitmq:
    host: localhost
    port: 5672
    username: admin
    password: 123456
    virtual-host: /
    listener:
      simple:
        acknowledge-mode: manual # 把消息确认默认修改为手动确认
```

****不设置**** `****acknowledge-mode: manual****` ****的后果就是：****

+ **Spring Boot 会自动管理消息确认**
+ **方法正常完成 → ****自动ACK****（消息被删除）**
+ **方法抛出异常 → ****自动NACK****（消息重新入队或进入死信）**

**手动模式让你对消息确认有完全的控制权，适合需要精确控制重试逻辑的业务场景。**



**第三步：**编写消费端的监听程序（**核心代码**）

```java
package com.jkweilai.mq.listener;

import com.rabbitmq.client.Channel;
import org.springframework.amqp.core.Message;
import org.springframework.amqp.rabbit.annotation.RabbitListener;
import org.springframework.stereotype.Component;

import java.io.IOException;

@Component
public class MyMessageListener {

    public static final String QUEUE_NAME = "queue.order";

    @RabbitListener(queues = {QUEUE_NAME})
    public void processMessage(String dataString, Message message, Channel channel) throws IOException {
        // false：表示该消失是首次投递的消息。
        // true：表示该消息不是首次投递的消息，已经重试过了。
        Boolean redelivered = message.getMessageProperties().getRedelivered();
        // 通过 message 获取 deliveryTag（可以看做是消息的唯一标识：身份证号）
        // 队列要用这个身份证号，队列根据身份证号获取该消息，进行后续操作（例如：删除消息）。
        long deliveryTag = message.getMessageProperties().getDeliveryTag();
        try {
            System.out.println("消费端收到消息:" + dataString + "，正在处理消息，处理核心业务.....");
            // 返回ACK的操作
            // 第一个参数是：消息的唯一标识。
            // 第二个参数是multiple：true表示支持多项