>



# 消息的可靠性投递
什么是可靠性投递：生产者发了一条消息，消费者就要消费一条消息。这才是正常的。但实际应用中可能会出现投递失败。

## 故障及解决方案描述
### 故障情况 1
**消息压根没有发到消息队列**，解决方案包括两个：

1. <font style="color:rgb(15, 17, 21);">在生产者端启用</font>**<font style="color:rgb(15, 17, 21);">确认</font>**<font style="color:rgb(15, 17, 21);">机制。当消息发送失败（如交换机或队列不存在）时，生产者立即感知并执行重发。</font>
2. <font style="color:rgb(15, 17, 21);">为</font>**<font style="color:rgb(15, 17, 21);">主交换机</font>**<font style="color:rgb(15, 17, 21);">配置一个</font>**<font style="color:rgb(15, 17, 21);">备份交换机</font>**<font style="color:rgb(15, 17, 21);">。当消息无法路由到任何队列时，自动转发到</font>**<font style="color:rgb(15, 17, 21);">备份交换机</font>**<font style="color:rgb(15, 17, 21);">，保证消息不丢失。</font>

### 故障情况 2
消息发到消息服务器后，服务器宕机了，导致内存中消息丢失，解决方案是：**将消息持久化到硬盘上。**

### 故障情况 3
消息发到消息服务器了，消息服务器也没有宕机，但是消费端在消费的时候出现异常了。导致消息没有成功消费，解决方案是：

1. **<font style="color:rgb(15, 17, 21);">成功则确认</font>**<font style="color:rgb(15, 17, 21);">：处理成功时消费端返回确认(ACK)，消息服务器删除消息。</font>
2. **<font style="color:rgb(15, 17, 21);">失败则拒收</font>**<font style="color:rgb(15, 17, 21);">：处理失败时消费端返回(NACK)，消息可以重新入队等待再次消费。（这属于消费端的重试机制）</font>

## <font style="color:rgb(15, 17, 21);">解决故障情况 1 的具体实践</font>
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

**第二步：**在 `application.yml`中启用生产端确认机制。重点关注以下**<font style="color:#DF2A3F;">两个配置</font>**。

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
public class ProducerAckConfig implements RabbitTemplate.ConfirmCallback, RabbitTempl