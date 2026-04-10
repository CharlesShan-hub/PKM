# 仲裁队列（`Quorum`）
在 RabbitMQ 3.8.x 版本之后支持的新内容。

镜像队列可以实现高可用，仲裁队列也可以实现高可用（自动选举机制），RabbitMQ 建议使用仲裁队列。

**使用仲裁队列后，会自动发生以下的事情：**

+ **在集群所有节点上创建队列副本**
+ **所有消息自动复制到所有节点**
+ **Master 节点处理读写，Slaves 作为备份**

## 准备交换机 队列 路由键
**创建交换机：**`exchange.quorum`

**创建队列：**`queue.quorum`

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1764067625080-577d37e0-1a89-4d50-94f4-0a4a94a46a5d.png" width="734.4" title="" crop="0,0,1,1" id="u322dfc39" class="ne-image">

创建完成之后，从下图位置就可以看出它与普通队列的区别：

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1764067660788-728882fa-0b60-43b7-981b-cc15dcb289be.png" width="553.6" title="" crop="0,0,1,1" id="u75dee8fd" class="ne-image">

**绑定路由键：**`routing.key.quorum`

## 编写生产端程序
```java
public static final String EXCHANGE_QUORUM = "exchange.quorum";
public static final String ROUTING_KEY_QUORUM = "routing.key.quorum";

@Test
public void test01() {
    rabbitTemplate.convertAndSend(EXCHANGE_QUORUM, ROUTING_KEY_QUORUM, "hello rabbit!");
}
```

执行后，看看 web 管理界面：

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1764067819276-b0cd40e3-f206-402f-b162-e525940b69e3.png" width="829.6" title="" crop="0,0,1,1" id="u6b0e3144" class="ne-image">

队列上有一条消息了。

## 让主节点宕机
```shell
docker stop rabbitmq-node1
```

## 编写消费端监听代码
创建新的项目 `consumer-cluster`，配置文件：

```yaml
spring:
  rabbitmq:
    host: localhost
    port: 5670
    username: admin
    password: 123456
    virtual-host: /
```

当主节点宕机之后，我们编写消费端的监听代码，看看还能否进行消费，如果还能够正常消费，表示我们现在已达到高可用。

```java
package com.jkweilai.consumercluster.listener;

import com.rabbitmq.client.Channel;
import org.springframework.amqp.core.Message;
import org.springframework.amqp.rabbit.annotation.RabbitListener;
import org.springframework.stereotype.Component;

import java.io.IOException;

@Component
public class MyMessageListener {

    // 常量
    public static final String QUEUE_QUORUM =  "queue.quorum";
    // 监听延迟队列
    @RabbitListener(queues = {QUEUE_QUORUM})
    public void processMessageDelay(String dataString, Message message, Channel channel) throws IOException {
        System.out.println(dataString);
        channel.basicAck(message.getMessageProperties().getDeliveryTag(), false);
    }
}
```

可以看到，虽然报错，但是消息还是可以进行消费：

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1764068223817-bbfff8f9-df78-402b-a909-34e349b9b016.png" width="400.8" title="" crop="0,0,1,1" id="u570db9c6" class="ne-image">

**最后记得把主节点再启动起来：**

```shell
docker restart rabbitmq-node1
```