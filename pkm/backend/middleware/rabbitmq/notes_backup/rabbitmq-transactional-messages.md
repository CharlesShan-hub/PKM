# 事务消息
在 RabbitMQ 中，使用 Java 客户端发消息的时候，在**同一个业务流程**当中，如何保证消息要么都成功发送，要么都不发送（只要有一条发失败了，就都不发送）。可以使用 RabbitMQ 提供的事务机制。

## RabbitMQ 事务的实现原理
```java
// 实际的事务操作序列
channel.txSelect();    // 开启事务

channel.basicPublish(); // 发送消息1 - 消息立即到达RabbitMQ服务器（但消费者不可见）
channel.basicPublish(); // 发送消息2 - 消息立即到达RabbitMQ服务器（但消费者不可见）

channel.txCommit();    // 提交事务 - 让消息对消费者可见

// 或者
channel.txRollback();  // 回滚事务 - 服务器丢弃已接收的消息
```

## 测试事务消息
创建一个新的 SpringBoot 项目，并引入 `RabbitMQ`的依赖。

### 编写配置类
```java
package com.jkweilai.tx.config;

import org.springframework.amqp.rabbit.connection.CachingConnectionFactory;
import org.springframework.amqp.rabbit.core.RabbitTemplate;
import org.springframework.amqp.rabbit.transaction.RabbitTransactionManager;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

@Configuration
public class RabbitConfig {

    // Rabbit专用事务管理器，交给Spring IoC容器
    @Bean
    public RabbitTransactionManager transactionManager(CachingConnectionFactory connectionFactory) {
        return new RabbitTransactionManager(connectionFactory);
    }
    
    @Bean
    public RabbitTemplate rabbitTemplate(CachingConnectionFactory connectionFactory) {
        RabbitTemplate rabbitTemplate = new RabbitTemplate(connectionFactory);
        // 重要设置
        rabbitTemplate.setChannelTransacted(true);
        return rabbitTemplate;
    }
}

```

**这个配置类的作用是：启用 RabbitMQ 的事务支持，让 RabbitTemplate 的操作能够参与到 Spring 的事务管理中。**

**简单说就是：****让 RabbitMQ 消息发送支持 Spring 的** `**@Transactional**` **事务控制。**

**这样配置后，就可以在方法上使用 **`**@Transactional**`**，其中的 RabbitMQ 消息发送就会在事务提交时一起提交，回滚时一起回滚。**

### **创建交换机 队列**
在 web 管理界面创建交换机：`exchange.tx`

创建队列：`queue.tx`

队列绑定路由键：`routing.key.tx`

### 编写测试程序发送消息
测试是否能够做到：成功后一起发送，或者失败后都不发送

```java
package com.jkweilai.tx;

import org.junit.jupiter.api.Test;
import org.springframework.amqp.rabbit.core.RabbitTemplate;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.test.annotation.Rollback;
import org.springframework.transaction.annotation.Transactional;

@SpringBootTest
class ProducerTxApplicationTests {

    @Autowired
    private RabbitTemplate rabbitTemplate;

    // 常量
    public static final String EXCHANGE_TX = "exchange.tx";
    public static final String ROUTING_KEY_TX = "routing.key.tx";

    // 先测试没有事务的情况
    @Test
    void test01() {
        rabbitTemplate.convertAndSend(EXCHANGE_TX, ROUTING_KEY_TX, "hello rabbit 1");
        System.out.println(10/0);
        rabbitTemplate.convertAndSend(EXCHANGE_TX, ROUTING_KEY_TX, "hello rabbit 2");
    }

    // 再测试有事务控制的情况
    @Test
    @Transactional
    @Rollback(true) // 手动回滚
    void test02() {
        rabbitTemplate.convertAndSend(EXCHANGE_TX, ROUTING_KEY_TX, "hello rabbit 1~");
        System.out.println(10/0);
        rabbitTemplate.convertAndSend(EXCHANGE_TX, ROUTING_KEY_TX, "hello rabbit 2~");
    }


    // 最终测试没有异常的情况，看看事务是否能够提交。
    @Test
    @Transactional
    @Rollback(false) // 在单元测试中，单元测试方法有一个特点：就算事务成功后，也不会提交，因此要在这里设置为 @Rollback(false)，表示事务成功后提交。
    void test03() {
        rabbitTemplate.convertAndSend(EXCHANGE_TX, ROUTING_KEY_TX, "hello rabbit 1~~");
        rabbitTemplate.convertAndSend(EXCHANGE_TX, ROUTING_KEY_TX, "hello rabbit 2~~");
    }

}
```

以上三个单元测试方法分别去执行，然后去 web 管理界面看数据是否和预期数据相同。

**注意：对于单元测试类中的单元测试方法来说，使用 **`**@Transactional**`**注解时需要配合 **`**@Rollback(true/false)**`**注解使用，如果不是单元测试类，这个 **`**@Rollback(true/false)**`**可以省略。**