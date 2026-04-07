端接收到了消息：" + dataString);
    }
}

```

**此时启动消费端之后，如果 RabbitMQ 中交换机和队列不存在，交换机、队列、以及交换机和队列的绑定关系会创建出来**。



**如果你在启动消费端之前已经将交换机、队列、以及绑定关系创建出来了，在消费端其实只需要编写监听哪个队列就行了。也就是代码可以修改为：**

```java
package com.jkweilai.mq.listener;

import com.rabbitmq.client.Channel;
import org.springframework.amqp.core.Message;
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
    
    @RabbitListener(queues = QUEUE_NAME)
    public void processMessage(String dataString, Message message, Channel channel) {
        System.out.println("消费端接收到了消息：" + dataString);
    }
}
```

## 在 web 界面上也可以手动创建
### 手动创建交换机
<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1763872827296-54b69508-2fbd-435f-be63-27aba0ae23c8.png" width="804.8" title="" crop="0,0,1,1" id="ub366651c" class="ne-image">

### 手动创建队列
<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1763872880411-d485abb6-1064-4b4f-bdc4-c02521c13464.png" width="841.6" title="" crop="0,0,1,1" id="u19882761" class="ne-image">

### 手动绑定路由键
<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1763872936662-e15425a4-d0fe-4621-a421-1bc3e4bd627c.png" width="1008" title="" crop="0,0,1,1" id="ua5e1dd31" class="ne-image">

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1763873006551-f58886fc-0cfb-4ec6-b876-d928c94dc18e.png" width="900" title="" crop="0,0,1,1" id="u3f477e01" class="ne-image">

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1763873036320-5ec456ff-88ce-449a-b41f-345ea69bd248.png" width="585.6" title="" crop="0,0,1,1" id="u9fd1903e" class="ne-image">

## 创建生产端 SpringBoot 项目引入依赖
```xml
<dependencies>
    <!--RabbitMQ客户端程序-->
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-amqp</artifactId>
    </dependency>
    <!--测试程序-->
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-test</artifactId>
        <scope>test</scope>
    </dependency>
</dependencies>
```

## 编写生产端 yml 配置文件
```yaml
spring:
  rabbitmq:
    host: localhost
    port: 5672
    username: admin
    password: 123456
    virtual-host: /
```

## 编写生产端的测试程序
编写**单元测试**：

```java
package com.jkweilai.mq;

import org.junit.jupiter.api.Test;
import org.springframework.amqp.rabbit.core.RabbitTemplate;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;

@SpringBootTest
class SpringbootRabbitmqProducerApplicationTests {

    @Autowired
    private RabbitTemplate rabbitTemplate;

    // 交换机名称
    public static final String EXCHANGE_NAME = "exchange.direct.order";
    // 路由键
    public static final String ROUTING_KEY = "order";

    @Test
    void test01() {
        // 核心：通过它发送消息。指定走哪个交换机，哪个路由键。
        rabbitTemplate.convertAndSend(EXCHANGE_NAME, ROUTING_KEY, "hello rabbit!");
    }

}
```



运行生产端测试程序，观察消费端是否收到消息：

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1763874137388-bb2ce88f-fa51-4fb3-954c-e684482f0838.png" width="299.2" title="" crop="0,0,1,1" id="u9e747acb" class="ne-image"