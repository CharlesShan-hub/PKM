id test01() {
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

**<font style="color:rgb(15, 17, 21);">不设置</font>****<font style="color:rgb(15, 17, 21);"> </font>**`**<font style="color:rgb(15, 17, 21);background-color:rgb(235, 238, 242);">acknowledge-mode: manual</font>**`**<font style="color:rgb(15, 17, 21);"> </font>****<font style="color:rgb(15, 17, 21);">的后果就是：</font>**

+ <font style="color:rgb(15, 17, 21);">Spring Boot 会自动管理消息确认</font>
+ <font style="color:rgb(15, 17, 21);">方法正常完成 →</font><font style="color:rgb(15, 17, 21);"> </font>**<font style="color:rgb(15, 17, 21);">自动ACK</font>**<font style="color:rgb(15, 17, 21);">（消息被删除）</font>
+ <font style="color:rgb(15, 17, 21);">方法抛出异常 →</font><font style="color:rgb(15, 17, 21);"> </font>**<font style="color:rgb(15, 17, 21);">自动NACK</font>**<font style="color:rgb(15, 17, 21);">（消息重新入队或进入死信）</font>

<font style="color:rgb(15, 17, 21);">手动模式让你对消息确认有完全的控制权，适合需要精确控制重试逻辑的业务场景。</font>

<font style="color:rgb(15, 17, 21);"></font>

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
            // 第二个参数是multiple：true表示支持多项操作。false表示不支持多项操作。啥意思？
            // 返回ACK后，消息队列会删除消息
            // 如果multiple为true表示将当前消息以及小于deliveryTag的消息都删除。
            // 如果multiple为false表示只将当前消息删除。（多数情况设置为false。）
            channel.basicAck(deliveryTag, false);
        } catch (Exception e) {
            // 出现异常就代表消费失败了。
            // 返回NACK的操作
            if(redelivered){
                // 告警或通知运维等人员
                System.out.println("你已经重试过一次了，还是失败，我给运维人员打电话吧！！！");
                channel.basicNack(deliveryTag, false, false);
            }else{
                // 返回队列重新消费。（由于你是第一次，再给你一次重试的机会）
                System.out.println("看在你是初犯，给你一次重试的机会。");
                channel.basicNack(deliveryTag, false, true);
            }
        }
    }
}

```



**第四步：**启动消费端，然后打开 web 管理界面，手动在管理界面上找到对应的交换机 `**<font style="color:black;">exchange.direct.order</font>**` 发消息给 `**queue.order**` <font style="color:#080808;background-color:#ffffff;">队列。</font>

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1763890838372-a73a132c-d76d-4a38-b629-4ef279ae8405.png" width="760.8" title="" crop="0,0,1,1" id="u0deae712" class="ne-image">

当 `try`语句块中没有发生异常时，消息能够正常消费：

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1763890858805-5cbedca3-50e0-47e8-9c9a-68aa07cf1f74.png" width="476.8" title="" crop="0,0,1,1" id="u500c9871" class="ne-image">



当 `try`语句块中发生异常时（**在代码中模拟异常**），消息不能正常消费，但如果是第一次发消息，会给一次机会重试，重试之后还是失败，则告警：

模拟异常：

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1763890900797-4d206369-ca3c-41b0-81a7-fca3b0a1c5f5.png" width="711.2" title="" crop="0,0,1,1" id="ud64490a7" class="ne-image">

在 web 管理界面发消息，观察控制台：

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1763890997441-550d229b-506c-461b-b5f7-6b30d8135196.png" width="463.2" title="" crop="0,0,1,1" id="u3671cf7f" class="ne-image">

## 总结
要想达到消息的可靠性传递，通常需要以上三种解决方法同时协作才行。绝非一个解决办法就能保证的。

# 消费端限流
并发量比较大的时候，如果消费端一次性将所有消息从消息队列中取出，消费端处理起来压力必然很大。我们可以启用消费端限流，让消费端慢慢从队列中消费，达到削峰填谷的效果。

## 当不启用限流时
我们找到生产端，让生产端发 100 条消息到队列，用 SpringBoot 集成 RabbitMQ 的第一个案例中的生产端，编写测试代码：

```java
@Test
public void test02(){
    for (int i = 1; i <= 100; i++) {
        rabbitTemplate.convertAndSend(EXCHANGE_NAME, ROUTING_KEY, "hello rabbit" + i);
    } 
}
```

运行测试程序，观察 web 管理界面 `queue.order`队列：

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1763892303223-4730975f-4b86-4ea0-99b1-d16e301a5b40.png" width="736" title="" crop="0,0,1,1" id="u6f195249" class="ne-image">



在 `consumer_confirm`项目中再编写一个新的消费端的监听，代码如下：

```java
@RabbitListener(queues = {QUEUE_NAME})
public void processMessagePrefetch(String dataString, Message message, Channel channel) throws IOException {
    try {
        TimeUnit.SECONDS.sleep(1);
    } catch (InterruptedException e) {
        throw new RuntimeException(e);
    }
    System.out.println("消费端接收到消息：" + dataString);
    channel.basicAck(message.getMessageProperties().getDeliveryTag(), false);
}
```

启动消费端，打开 web 管理界面，看看是不是 100 瞬间变成 0：

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1763892565191-caaf4ded-665d-4f19-a27a-ed000512ea8f.png" width="216" title="" crop="0,0,1,1" id="u5aa5dc0e" class="ne-image">

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1763892577218-0c1e3171-ade4-4a03-945c-f48d1865f2f7.png" width="205.6" title="" crop="0,0,1,1" id="u623c01b4" class="ne-image">

## 当启用限流时
在消费端的 `application.yml`中启用限流，一次少取，配置如下：

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
        prefetch: 1 # 消费端一次取一条进行消费
```

再重新执行生产端，发送 100 条消息到队列：

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1763893871565-ec0f6230-3217-48a5-b629-9b16e91da6d4.png" width="174.4" title="" crop="0,0,1,1" id="ub442f151" class="ne-image">

5 秒后刷新页面：达到了 1 秒取一条消息进行消费。

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1763893886496-1b425458-c246-41ae-b5ae-d09723deb681.png" width="232.8" title="" crop="0,0,1,1" id="ud8687366" class="ne-image">

## 一次取少量和一次取大量的区别
<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1763893247044-24882f77-627c-4732-917b-6d3393b3c2d7.png" width="779.2" title="" crop="0,0,1,1" id="u0e92423a" class="ne-image">

# 消息超时机制
消息在消息队列里放的时间太长，会导致消息队列内存耗尽，消息超时机制就是来解决这个问题的。

消息超时会被自动删除。



**可以从两个层面设置消息的超时机制：**

1. （类似于全局设置）设置消息队列的超时时间，这种方式将作用于消息队列当中的所有消息。（不是队列的超时时间，是队列中**所有消息**的超时时间。）
2. （类似于局部设置）通过代码设置某个消息的超时时间。

如果同时设置，以时间短的为准。

## 设置队列的超时时间
在 web 界面操作：

1. 创建交换机：`exchange.timeout`

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1763896968333-b865fd9d-d7aa-4426-a557-0ba25cef4aa1.png" width="506.4" title="" crop="0,0,1,1" id="u722f0079" class="ne-image">

2. 创建队列：`queue.timeout`

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1763897083238-885377f0-be73-47c7-ab23-72609e03639d.png" width="723.2" title="" crop="0,0,1,1" id="uf5e569bc" class="ne-image">

3. 配置路由键，绑定交换机和队列：`routing.key.timeout`

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1763897154516-58ab64b5-6e6c-40f3-87d4-7167889c25da.png" width="824.8" title="" crop="0,0,1,1" id="u9a85fcca" class="ne-image">



**在 **`**producer_confirm**`**项目中编写测试代码，生产端发送 100 条消息到队列，看看超时之后，消息是否全部删除：**

```java
public static final String EXCHANGE_TIMEOUT = "exchange.timeout";
public static final String ROUTING_KEY_TIMEOUT = "routing.key.timeout";
@Test
void test02() {
    for (int i = 0; i < 100; i++) {
        rabbitTemplate.convertAndSend(EXCHANGE_TIMEOUT, ROUTING_KEY_TIMEOUT, "hello rabbit " + i);
    }
}
```

运行测试程序，观察 web 管理界面：

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1763897508094-4be978e4-dbe3-4837-8be9-056f1caf4061.png" width="197.6" title="" crop="0,0,1,1" id="u8bf86499" class="ne-image">

10 秒超时后：

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1763897515548-9783d76a-c5f4-4734-a70a-5319e7a482cc.png" width="171.2" title="" crop="0,0,1,1" id="ue16e320e" class="ne-image">

## 通过代码设置某条消息的超时时间
**在 **`**producer_confirm**`**项目中编写测试代码，生产端发送 1 条****<font style="color:#DF2A3F;">设置了超时时间</font>****的消息到队列，看看超时之后，消息是否全部删除：**

```java
@Test
void test03() {
    // 创建消息后处理器，这也是一个回调
    MessagePostProcessor messagePostProcessor = message -> {
        // 设置当前消息的超时时间为7秒
        message.getMessageProperties().setExpiration("7000");
        return message;
    };
    // 发送消息（记得将上面的消息后处理对象传到下面方法的末尾参数位置上）
    rabbitTemplate.convertAndSend(EXCHANGE_TIMEOUT, ROUTING_KEY_TIMEOUT, "hello rabbit", messagePostProcessor);
}
```

运行测试，看看 7 秒后该消息是否自动删除。

# 死信与死信队列
## 什么是死信
**<font style="color:rgb(15, 17, 21);">死信就是"屡次处理失败"或"无家可归"的消息，被系统打入"冷宫"单独处理。</font>**

## <font style="color:rgb(15, 17, 21);">导致死信的原因</font>
**<font style="color:rgb(15, 17, 21);">导致死信的原因有三个：</font>**

**<font style="color:rgb(15, 17, 21);">第一个：消息被拒绝且不重新入队</font>**

```java
// 返回NACK，并且第三个参数为false，不再重新入队。
channel.basicNack(deliveryTag, false, false); 
```

**<font style="color:rgb(15, 17, 21);">第二个：消息在队列中存活时间超限（TTL到期）</font>**

**<font style="color:rgb(15, 17, 21);">第三个：队列达到最大长度限制：</font>**<font style="color:rgb(15, 17, 21);">当队列已满，新消息进入时会挤掉最早的消息，被挤掉的消息就成为死信</font>

## <font style="color:rgb(15, 17, 21);">死信的处理方式</font>
死信处理方式通常包括以下三种：

1. **丢弃**：不重要的消息直接丢弃，不做处理。
2. **入库**：把死信写到数据库，以后再处理。
3. **监听**：配置死信队列，死信后会自动进入死信队列，设置消费端监听死信队列，做后续处理。（生产环境首选）

## 测试环境准备
### 创建死信交换机和死信队列
和创建正常交换机和正常队列没有区别。

**创建死信交换机**：`exchange.dead.letter.video`

**创建死信队列**：`queue.dead.letter.video`

**绑定路由键**：`routing.key.dead.letter`

### 创建正常交换机和正常队列
**创建正常交换机**：`exchange.normal.video`

**创建正常队列**：`queue.normal.video`

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1763963759632-23436d76-c3a0-4010-8b9f-bc24154b924c.png" width="828.8" title="" crop="0,0,1,1" id="u494abcd5" class="ne-image">

**绑定路由键**：`routing.key.normal`

## 死信第一种情况：消费端拒收
生产端的代码不用写，直接在 **web 界面中发消息**。

消费者端写两个监听。一个监听正常队列。一个监听死信队列。



**找到 **`**consumer_confirm**`**项目中的 **`**MyMessageListener**`**类。编写两个监听**。



**监听正常队列：**

```java
// 常量
public static final String QUEUE_NORMAL = "queue.normal.video";
// 监听正常队列
@RabbitListener(queues = {QUEUE_NORMAL})
public void processMessageNormal(String dataString, Message message, Channel channel) throws IOException {
    // 消费端拒收消息（拒收正常队列发过来的消息。看看消息会不会到死信队列）
    System.out.println("消息接收到了，但是我拒绝了");
    //channel.basicNack(message.getMessageProperties().getDeliveryTag(), false, false);
    // 或者也可以调用 basicReject 方法。可以少写一个参数。
    channel.basicReject(message.getMessageProperties().getDeliveryTag(), false);
}
```



**监听死信队列：**

```java
// 常量
public static final String QUEUE_DEAD_LETTER = "queue.dead.letter.video";
// 监听死信队列
@RabbitListener(queues = {QUEUE_DEAD_LETTER})
public void processMessageDead(String dataString, Message message, Channel channel) throws IOException {
    System.out.println("我是监听死信的，我接收到了死信：" + dataString);
    channel.basicAck(message.getMessageProperties().getDeliveryTag(), false);
}
```



在 Web 管理界面向**正常队列**发送消息（**在交换机页面**，通过交换机 `exchange.normal.video`+ 路由键 `routing.key.normal`发送消息）

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1763976041206-e73fee77-2a66-48b1-9cee-fc30c68ee481.png" width="872.8" title="" crop="0,0,1,1" id="u2bd6c8a7" class="ne-image">



**生产端发送消息后，查看控制台：**

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1763976083987-9786fe0e-4468-4a0d-b34b-1316cfa36512.png" width="353.6" title="" crop="0,0,1,1" id="u08d5b7ec" class="ne-image">



**大家要明白**，我们现在编写这个程序的目的是什么？其实主要测试目的有两个：

**第一个：**消息是不是变成死信了。

**第二个：**消息变成死信之后是否进入了死信队列。

## 死信第二种和第三种情况：消息超时/消息超过最大容量
注意：先将消费端的程序停掉。

我们用生产端的代码，发送 20 条消息到队列。队列的最大容量是 10，并且等待 10 秒后，看看会不会有 20 条消息进入死信队列。

为什么死信队列中应该有 20 条呢？这是因为最初发送了 20 条，其中 10 条是溢出的，剩下那 10 条在队列中最终也会超时，所以死信队列中应该有 20 条。



**找到 **`**producer_confirm**`**项目**，找到测试类，编写测试方法，发送 20 条消息：（**记得把消费端的程序先停掉**）

```java
public static final String EXCHANGE_NORMAL = "exchange.normal.video";
public static final String ROUTING_KEY_NORMAL = "routing.key.normal";

@Test
public void test04(){
    for (int i = 1; i <= 20; i++) {
        rabbitTemplate.convertAndSend(EXCHANGE_NORMAL, ROUTING_KEY_NORMAL, "hello rabbit " + i);
    }
}
```



通过 Web 管理界面可以看到，最初是有 10 条（为什么 10 条，队列最多放 10 条），一会超时之后变成 0 条。最终 20 条都放到了死信队列。

此时启动死信队列的监听，就是我们在验证第一种情况时编写的监听死信队列的代码，结果如下：

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1763977143487-5ae3cf22-3535-4629-be3d-b4167c3f0d6b.png" width="404" title="" crop="0,0,1,1" id="u9f90c7a0" class="ne-image">

# 延迟队列
**<font style="color:rgb(15, 17, 21);">延迟队列就是让消息在指定的延迟时间之后才被消费的特殊队列。</font>**

**<font style="color:rgb(15, 17, 21);"></font>**

**<font style="color:rgb(15, 17, 21);">在电商平台上，用户下单之后，会显示：请在多长时间内支付。这个机制实现有多种方案，但其中有一种方案就是：采用延迟队列来完成。</font>**

**<font style="color:rgb(15, 17, 21);"></font>**

## <font style="color:rgb(15, 17, 21);">实现延迟队列的第一种方案</font>
设置消息的超时时间，然后监听死信队列。（不监听正常队列，而是监听死信队列。）

等时间一到，消息就会从正常队列发送到死信队列。当死信队列的监听收到消息则表示时间已到。

这种方式就不需要演示了，上面我们刚测试过。



## 实现延迟队列的第二种方案：使用 RabbitMQ 的插件
### 安装插件
```shell
# 进入容器（建立在我们大健康项目的基础之上的哈。）
docker exec -it mq bash

# 容器内安装wget命令
apt-get update && apt-get install -y wget

# 下载延迟插件（在容器内）
wget https://github.com/rabbitmq/rabbitmq-delayed-message-exchange/releases/download/v3.13.0/rabbitmq_delayed_message_exchange-3.13.0.ez

# 复制到插件目录
cp rabbitmq_delayed_message_exchange-3.13.0.ez /opt/rabbitmq/plugins/

# 启用插件
rabbitmq-plugins enable rabbitmq_delayed_message_exchange

# 退出并重启容器
exit
docker restart mq
```



怎么验证插件安装成功了呢？通过 web 管理界面查看，如果创建交换机时，下拉列表有下图的选项，表示安装成功：

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1763993700616-8862f377-0063-4117-bc4f-5ccf47e1d991.png" width="406.4" title="" crop="0,0,1,1" id="ud68fe779" class="ne-image">



另外，也可以通过以下方式查看：

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1763993772275-f5d9cf02-b359-4c56-96e0-aeeb48a26b3f.png" width="388" title="" crop="0,0,1,1" id="u304e6592" class="ne-image">

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1763993793115-875830a9-3bf9-49f8-b4e3-b9774831f7c8.png" width="536" title="" crop="0,0,1,1" id="u0c781a85" class="ne-image">



`Advanced`点开之后，往下拉：

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1763993811204-c29d69d5-873a-4196-8347-a2e46d5196a2.png" width="638.4" title="" crop="0,0,1,1" id="ue0527a41" class="ne-image">

### 创建交换机 队列 绑定路由键
**创建交换机：**和之前不一样，注意看。交换机的名字 `exchange.delay`，参数 `x-delayed-type`，参数值：`direct`。

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1763994138688-69388b15-e73f-40a4-93f0-85b232a73c6f.png" width="731.2" title="" crop="0,0,1,1" id="u61c6c233" class="ne-image">



**创建队列：**队列名字 `queue.delay`



**队列绑定路由键**：`routing.key.delay`

### 编写测试程序
**编写生产端的测试程序**，写到这个项目中吧：

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1763994801041-5348ae8d-103f-4a47-a163-ddbe622f5b09.png" width="220.8" title="" crop="0,0,1,1" id="ucff41bb3" class="ne-image">

```java
public static final String EXCHANGE_DELAY = "exchange.delay";
public static final String ROUTING_KEY_DELAY = "routing.key.delay";
@Test
public void test(){
    // 消息后处理器中设置延迟时间
    MessagePostProcessor postProcessor = message -> {
        message.getMessageProperties().setHeader("x-delay", 10000);
        return message;
    };

    rabbitTemplate.convertAndSend(
            EXCHANGE_DELAY,
            ROUTING_KEY_DELAY,
            "一条延迟10秒的消息：" + new SimpleDateFormat("HH:mm:ss").format(new Date()),
            postProcessor);
}
```



**编写消费端监听代码**，写到这个项目中吧：

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1763994811534-5d8fe189-ab29-450e-8580-9f7fd8309bf2.png" width="232" title="" crop="0,0,1,1" id="ufa4b3df5" class="ne-image">

```java
// 常量
public static final String QUEUE_DELAY =  "queue.delay";
// 监听延迟队列
@RabbitListener(queues = {QUEUE_DELAY})
public void processMessageDelay(String dataString, Message message, Channel channel) throws IOException {
    System.out.println(dataString);
    System.out.println("系统当前时间：" + new SimpleDateFormat("HH:mm:ss").format(new Date()));
    channel.basicAck(message.getMessageProperties().getDeliveryTag(), false);
}
```



**测试：**先启动消费端监听程序，再启动生产端发送消息。

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1763995296320-2b866780-b1a6-4a64-a497-68560368afb0.png" width="240" title="" crop="0,0,1,1" id="u016de9be" class="ne-image">

使用这种方式比之前的死信队列要好很多。

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

**<font style="color:rgb(15, 17, 21);">这个配置类的作用是：启用 RabbitMQ 的事务支持，让 RabbitTemplate 的操作能够参与到 Spring 的事务管理中。</font>**

<font style="color:rgb(15, 17, 21);">简单说就是：</font>**<font style="color:rgb(15, 17, 21);">让 RabbitMQ 消息发送支持 Spring 的</font>****<font style="color:rgb(15, 17, 21);"> </font>**`**<font style="color:rgb(15, 17, 21);background-color:rgb(235, 238, 242);">@Transactional</font>**`**<font style="color:rgb(15, 17, 21);"> </font>****<font style="color:rgb(15, 17, 21);">事务控制。</font>**

<font style="color:rgb(15, 17, 21);">这样配置后，就可以在方法上使用 </font>`<font style="color:rgb(15, 17, 21);background-color:rgb(235, 238, 242);">@Transactional</font>`<font style="color:rgb(15, 17, 21);">，其中的 RabbitMQ 消息发送就会在事务提交时一起提交，回滚时一起回滚。</font>

### <font style="color:rgb(15, 17, 21);">创建交换机 队列</font>
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

# 惰性队列
## 什么是惰性队列？
<font style="color:rgb(15, 17, 21);">惰性队列会将消息直接存入磁盘，而非内存。只有当消费者来取消息时，才会将其从磁盘加载到内存中。</font>

## 它是如何工作的？
对于普通队列，RabbitMQ 会尽最大努力将消息保留在内存中，以追求极致的性能。只有当发布速度过快、内存告急时，或者触发了某些条件时，才会将消息刷到磁盘。

而**惰性队列的行为则完全相反**：

+ **优先写到磁盘**：消息一进入队列，就会被写入磁盘。
+ **读取时才加载到内存**：当消费者准备处理消息时，系统才会将消息从磁盘加载到内存，然后发送给消费者。

## 如何创建一个惰性队列？
**在声明队列时指定参数**（以 Java 客户端为例）：

```java
Map<String, Object> args = new HashMap<>();
args.put("queue-mode", "lazy");
channel.queueDeclare("my_lazy_queue", true, false, false, args);
```

SpringBoot 项目中怎么设置？

```java
@Configuration
public class RabbitMQConfig {
    
    // 在监听器中声明惰性队列
    @RabbitListener(bindings = @QueueBinding(
        value = @Queue(
            name = "my_lazy_queue",
            durable = "true",
            arguments = @Argument(name = "x-queue-mode", value = "lazy")
        ),
        exchange = @Exchange(name = "my_exchange", type = ExchangeTypes.DIRECT),
        key = "lazy.routing.key"
    ))
    public void handleLazyQueueMessage(String message) {
        System.out.println("Received from lazy queue: " + message);
    }
}
```

## 惰性队列的核心价值
1. **<font style="color:rgb(15, 17, 21);">防内存崩溃</font>**<font style="color:rgb(15, 17, 21);">  
</font><font style="color:rgb(15, 17, 21);">惰性队列将消息存于磁盘，不耗费内存，当然不存在内存崩溃的情况。</font>
2. **<font style="color:rgb(15, 17, 21);">支持海量堆积</font>**<font style="color:rgb(15, 17, 21);">  
</font><font style="color:rgb(15, 17, 21);">惰性队列可容纳数十亿条消息，适用于日志、报表等允许延迟的场景。</font>
3. **<font style="color:rgb(15, 17, 21);">更强持久化</font>**<font style="color:rgb(15, 17, 21);">  
</font><font style="color:rgb(15, 17, 21);">消息几乎同步写入磁盘，几乎不会丢失消息。</font>

## 惰性队列的缺点
天下没有免费的午餐，惰性队列的优点是以牺牲**性能**为代价的：

1. **更高的磁盘 I/O**：每次发布消息都需要进行磁盘写入操作，这比写入内存要慢得多。
2. **更高的消费延迟**：由于消费者每次获取消息都需要从磁盘读取，而不是直接从内存获取，所以消息的投递速率（吞吐量）会显著降低。

## 何时使用惰性队列？
| **特性** | **普通队列** | **惰性队列** |
| --- | --- | --- |
| **核心目标** | **性能、低延迟** | **稳定性、可靠性** |
| **消息存储** | 优先内存 | 优先磁盘 |
| **内存占用** | 高（消息堆积时危险） | 极低 |
| **吞吐量** | 高 | 较低 |
| **适用场景** | 实时处理、高吞吐、消息不积压 | 消息可能大量堆积、允许延迟、日志处理 |


**决策建议**：

+ 如果你的场景是**实时交易、高并发、低延迟**，并且你确信消费者能及时处理消息，不会产生大量堆积，那么请使用**普通队列**。
+ 如果你的场景是**日志收集、事件记录、任务队列**，并且可能因为消费者故障或处理速度慢导致消息大量积压，那么请使用**惰性队列**来保护你的 RabbitMQ 服务器免于内存崩溃。

简单来说，**惰性队列是你的“安全网”，它用性能换取了****<font style="color:#DF2A3F;">在面对不可预测的消息洪峰时</font>****的系统稳定性。**

# 优先级队列
默认情况下，消息队列的特点是：FIFO 结构（先进先出），在某些特定业务场景中，我们可能需要某些消息先被消费，怎么办？消息可以设置优先级，优先级越高的消息，会**优先被消费**。

## 创建交换机 队列 绑定路由键
**创建交换机：**`exchange.priority`



**创建队列：**`queue.priority`

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1763990360324-f0fc0992-b4b8-4e79-9501-0ccb6c33848d.png" width="767.2" title="" crop="0,0,1,1" id="u53ced881" class="ne-image">

优先级的最高值必须设置，这个参数如果不设置的话，设置优先级没用。最高值不一定是 10，但一定要设置这个参数。

参数名为：`x-max-priority`，千万别写错！！！



**队列页面绑定路由键：**`routing.key.priority`

## 编写测试代码测试
**在之前项目中随便找一个生产端，编写发送消息的测试程序。在这个项目中写吧：**

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1763990493740-b7c068c0-ed22-4cfd-be8b-447c9038cc51.png" width="206.4" title="" crop="0,0,1,1" id="ub5bf4e85" class="ne-image">

```java
public static final String EXCHANGE_PRIORITY = "exchange.priority";
public static final String ROUTING_KEY_PRIORITY = "routing.key.priority";
@Test
public void test05(){
    // 最后一个参数是消息后处理器，使用消息后处理器来设置消息的优先级。
    rabbitTemplate.convertAndSend(EXCHANGE_PRIORITY, ROUTING_KEY_PRIORITY, "hello rabbit 1", message -> {
        // x-max-priority:10 最高优先级我设置的是10，因此优先级不要超范围。
        message.getMessageProperties().setPriority(1);
        return message;
    });
}
@Test
public void test06(){
    rabbitTemplate.convertAndSend(EXCHANGE_PRIORITY, ROUTING_KEY_PRIORITY, "hello rabbit 2", message -> {
        message.getMessageProperties().setPriority(2);
        return message;
    });
}
@Test
public void test07(){
    rabbitTemplate.convertAndSend(EXCHANGE_PRIORITY, ROUTING_KEY_PRIORITY, "hello rabbit 3", message -> {
        message.getMessageProperties().setPriority(3);
        return message;
    });
}
```

执行以上测试程序，观察 web 管理界面，队列中是否有三条消息：

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1763990863345-e22adf76-65b5-4f66-8617-672bf9b6bb24.png" width="220.8" title="" crop="0,0,1,1" id="ud4d0bb8b" class="ne-image">





**在之前项目中随便找一个消费端，编写监听程序。我们就在这个项目中编写吧：**

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1763990897678-1fc2ee5c-b804-446d-9876-96669fde1d90.png" width="197.6" title="" crop="0,0,1,1" id="u2b43f1db" class="ne-image">

```java
// 常量 
public static final String QUEUE_PRIORITY = "queue.priority";

// 监听优先级队列
@RabbitListener(queues = {QUEUE_PRIORITY})
public void processMessagePriority(String dataString, Message message, Channel channel) throws IOException {
    System.out.println(dataString);
    channel.basicAck(message.getMessageProperties().getDeliveryTag(), false);
}
```

执行这个程序，看看控制台，是不是优先级最高的那条消息最先被消费：

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1763991042509-e1dd799a-5d35-409a-89ad-0f4c1f3d916b.png" width="213.6" title="" crop="0,0,1,1" id="u5dc1fffd" class="ne-image">

# docker 环境下搭建 RabbitMQ 集群
**<font style="color:#DF2A3F;">提醒：生产环境下，建议不要在一个物理机上搭建 RabbitMQ，防止物理机宕机，导致数据丢失。</font>**

基于之前的 `dajiankang` 网络和指定的可用IP，以下是完整的RabbitMQ集群搭建方案。

## 删除 mq 容器
我们要搭建集群了。把课程最开始创建的 mq 容器删除：

```shell
docker stop mq
docker rm mq
```

## 创建数据目录
```bash
# 为三个节点创建数据目录
mkdir -p /home/rabbitmq/{node1,node2,node3}/data
mkdir -p /home/rabbitmq/{node1,node2,node3}/conf
```

## 创建RabbitMQ配置文件
**<font style="color:rgb(15, 17, 21);">这些配置文件用于让三个RabbitMQ节点自动发现并组成集群，实现高可用和负载均衡，具体作用：</font>**

+ **<font style="color:rgb(15, 17, 21);">允许 guest 用户从</font>****<font style="color:#DF2A3F;">远程</font>****<font style="color:rgb(15, 17, 21);">连接 RabbitMQ</font>**
+ **<font style="color:rgb(15, 17, 21);">设置服务端口</font>**
    - **<font style="color:rgb(15, 17, 21);">（不配置端口时，rabbitmq 的默认端口也是 5672 和 15672，因此这两个配置可以省略，另外集群之间的节点通信端口默认是 25672，也不用配置，为什么三个端口一样？不冲突吗？不冲突，因为每个 docker 容器的环境是独立的。）</font>**
+ **<font style="color:rgb(15, 17, 21);">配置节点相互发现组成集群。</font>**

为每个节点创建配置文件：

**节点1配置** (`/home/rabbitmq/node1/conf/rabbitmq.conf`)：

```bash
cat > /home/rabbitmq/node1/conf/rabbitmq.conf << EOF
loopback_users.guest = false
listeners.tcp.default = 5672
management.tcp.port = 15672
cluster_formation.peer_discovery_backend = rabbit_peer_discovery_classic_config
cluster_formation.classic_config.nodes.1 = rabbit@rabbitmq-node1
cluster_formation.classic_config.nodes.2 = rabbit@rabbitmq-node2
cluster_formation.classic_config.nodes.3 = rabbit@rabbitmq-node3
EOF
```

**节点2配置** (`/home/rabbitmq/node2/conf/rabbitmq.conf`)：

```bash
cat > /home/rabbitmq/node2/conf/rabbitmq.conf << EOF
loopback_users.guest = false
listeners.tcp.default = 5672
management.tcp.port = 15672
cluster_formation.peer_discovery_backend = rabbit_peer_discovery_classic_config
cluster_formation.classic_config.nodes.1 = rabbit@rabbitmq-node1
cluster_formation.classic_config.nodes.2 = rabbit@rabbitmq-node2
cluster_formation.classic_config.nodes.3 = rabbit@rabbitmq-node3
EOF
```

**节点3配置** (`/home/rabbitmq/node3/conf/rabbitmq.conf`)：

```bash
cat > /home/rabbitmq/node3/conf/rabbitmq.conf << EOF
loopback_users.guest = false
listeners.tcp.default = 5672
management.tcp.port = 15672
cluster_formation.peer_discovery_backend = rabbit_peer_discovery_classic_config
cluster_formation.classic_config.nodes.1 = rabbit@rabbitmq-node1
cluster_formation.classic_config.nodes.2 = rabbit@rabbitmq-node2
cluster_formation.classic_config.nodes.3 = rabbit@rabbitmq-node3
EOF
```

## 创建hosts文件
**<font style="color:rgb(15, 17, 21);">这个配置用于在容器内部建立主机名与IP的映射关系，让三个RabbitMQ节点能够通过主机名相互识别和通信，从而成功组建集群。（RabbitMQ 节点间的通信是依赖主机名的。）</font>**

创建包含所有节点主机名映射的文件：

```bash
cat > /home/rabbitmq/hosts << EOF
172.16.0.13 rabbitmq-node1
172.16.0.15 rabbitmq-node2
172.16.0.16 rabbitmq-node3
EOF
```

## 启动三个RabbitMQ节点
注意：

+ RabbitMQ 要求：在同一个集群内的节点 Cookie 值必须相等，我们这里设置的 Cookie 值：`CLUSTER_COOKIE_123456`
+ 如果搭建集群，4369 端口必须映射。

**启动节点1 (172.16.0.13)**：

```bash
docker run -d --name rabbitmq-node1 \
  --hostname rabbitmq-node1 \
  --net dajiankang --ip 172.16.0.13 \
  -p 4369:4369 \
  -p 5672:5672 \
  -p 15672:15672 \
  -v /home/rabbitmq/node1/data:/var/lib/rabbitmq \
  -v /home/rabbitmq/node1/conf/rabbitmq.conf:/etc/rabbitmq/rabbitmq.conf \
  -v /home/rabbitmq/hosts:/etc/hosts \
  -e RABBITMQ_DEFAULT_USER=admin \
  -e RABBITMQ_DEFAULT_PASS=123456 \
  -e RABBITMQ_ERLANG_COOKIE="CLUSTER_COOKIE_123456" \
  -e TZ=Asia/Shanghai \
  -m 450m \
  --restart unless-stopped \
  rabbitmq:3.13-management
```

**启动节点2 (172.16.0.15)**：

```bash
docker run -d --name rabbitmq-node2 \
  --hostname rabbitmq-node2 \
  --net dajiankang --ip 172.16.0.15 \
  -p 43690:4369 \
  -p 56720:5672 \
  -p 15673:15672 \
  -v /home/rabbitmq/node2/data:/var/lib/rabbitmq \
  -v /home/rabbitmq/node2/conf/rabbitmq.conf:/etc/rabbitmq/rabbitmq.conf \
  -v /home/rabbitmq/hosts:/etc/hosts \
  -e RABBITMQ_DEFAULT_USER=admin \
  -e RABBITMQ_DEFAULT_PASS=123456 \
  -e RABBITMQ_ERLANG_COOKIE="CLUSTER_COOKIE_123456" \
  -e TZ=Asia/Shanghai \
  -m 450m \
  --restart unless-stopped \
  rabbitmq:3.13-management
```

**启动节点3 (172.16.0.16)**：

```bash
docker run -d --name rabbitmq-node3 \
  --hostname rabbitmq-node3 \
  --net dajiankang --ip 172.16.0.16 \
  -p 43691:4369 \
  -p 56721:5672 \
  -p 15674:15672 \
  -v /home/rabbitmq/node3/data:/var/lib/rabbitmq \
  -v /home/rabbitmq/node3/conf/rabbitmq.conf:/etc/rabbitmq/rabbitmq.conf \
  -v /home/rabbitmq/hosts:/etc/hosts \
  -e RABBITMQ_DEFAULT_USER=admin \
  -e RABBITMQ_DEFAULT_PASS=123456 \
  -e RABBITMQ_ERLANG_COOKIE="CLUSTER_COOKIE_123456" \
  -e TZ=Asia/Shanghai \
  -m 450m \
  --restart unless-stopped \
  rabbitmq:3.13-management
```

## 启用集群插件并加入集群
等待所有节点启动完成（约30秒），然后执行：

**在节点2上执行，加入集群**：

```bash
# 进入节点2容器
docker exec -it rabbitmq-node2 bash

# 在容器内执行以下命令
rabbitmqctl stop_app
rabbitmqctl reset
rabbitmqctl join_cluster rabbit@rabbitmq-node1
rabbitmqctl start_app
exit
```

**在节点3上执行，加入集群**：

```bash
# 进入节点3容器
docker exec -it rabbitmq-node3 bash

# 在容器内执行以下命令
rabbitmqctl stop_app
rabbitmqctl reset
rabbitmqctl join_cluster rabbit@rabbitmq-node1
rabbitmqctl start_app
exit
```

## 验证集群状态
```bash
# 在任何节点上检查集群状态
docker exec -it rabbitmq-node1 rabbitmqctl cluster_status
```

## 设置镜像队列策略（这一步不要做）
为了 **数据** 高可用，设置镜像队列：

```bash
docker exec -it rabbitmq-node1 rabbitmqctl set_policy ha-all "^" '{"ha-mode":"all"}'
```

**<font style="color:rgb(15, 17, 21);">将集群中所有队列设置为全节点镜像，实现数据高可用。</font>**

<font style="color:rgb(15, 17, 21);">这句话的含义是：</font>

+ <font style="color:rgb(15, 17, 21);">对所有队列（</font>`<font style="color:rgb(15, 17, 21);background-color:rgb(235, 238, 242);">"^"</font>`<font style="color:rgb(15, 17, 21);"> </font><font style="color:rgb(15, 17, 21);">匹配所有队列名）</font>
+ <font style="color:rgb(15, 17, 21);">在所有节点上创建镜像副本（</font>`<font style="color:rgb(15, 17, 21);background-color:rgb(235, 238, 242);">"ha-mode":"all"</font>`<font style="color:rgb(15, 17, 21);">）</font>
+ <font style="color:rgb(15, 17, 21);">确保任一节点宕机时队列数据不丢失，服务自动切换</font>

<font style="color:rgb(15, 17, 21);"></font>

**<font style="color:#DF2A3F;">注意：在 RabbitMQ 3.8.x 版本之后引入了仲裁队列。使用仲裁队列的话，就不需要再配置镜像队列了。通过仲裁队列默认就可以达到高可用。并且使用仲裁队列就不需要指定以上这些复杂的规则了。</font>**

## 配置端口转发
要在 windows 上访问虚拟机中 docker 中的 RabbitMQ 节点。需要在 `Oracle VirtualBox`上配置端口映射：

**节点 1 的端口映射：**

| **windows 端口** | **虚拟机端口** | **docker 端口** | **备注** |
| --- | --- | --- | --- |
| 4369 | 4369 | 4369 |  |
| 5672 | 5672 | 5672 | **这个之前已配置** |
| 15672 | 15672 | 15672 | **这个之前已配置** |




**节点 2 的端口映射：**

| **windows 端口** | **虚拟机端口** | **docker 端口** |
| --- | --- | --- |
| 43690 | 43690 | 4369 |
| 56720 | 56720 | 5672 |
| 15673 | 15673 | 15672 |




**节点 3 的端口映射：**

| **windows 端口** | **虚拟机端口** | **docker 端口** |
| --- | --- | --- |
| 43691 | 43691 | 4369 |
| 56721 | 56721 | 5672 |
| 15674 | 15674 | 15672 |


## 访问信息
+ **管理界面**：
    - 节点1: `http://localhost:15672`
    - 节点2: `http://localhost:15673`
    - 节点3: `http://localhost:15674`
+ **用户名**: `admin`
+ **密码**: `123456`



另外，通过 web 管理界面也可以看到三个节点的集群已经做到了相互感知和发现了：

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1764049992301-111cf21f-dd84-474b-882e-0c8af5faf2f4.png" width="479.2" title="" crop="0,0,1,1" id="u045426f7" class="ne-image">

# 集群下的负载均衡
使用 HAProxy 为 RabbitMQ 集群做负载均衡是一个**非常标准和推荐**的做法。

客户端连接 HAProxy 提供的统一入口。HAProxy 负载均衡的方式访问各节点。 

## 客户端的负载均衡方案
<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1764061851134-699b045a-93f7-47cc-9608-f4db36dc7943.png" width="500.4000244140625" title="" crop="0,0,1,1" id="u7904150c" class="ne-image">

## Web 管理界面的负载均衡方案
<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1764061911033-1a66d151-5cc9-444b-b6f2-86a106fb1444.png" width="470.4000244140625" title="" crop="0,0,1,1" id="u75b8536d" class="ne-image">

## 什么是 HAProxy？
**HAProxy**（High Availability Proxy）是一个开源、高性能的 **TCP/HTTP 负载均衡器**。

## 为什么 RabbitMQ 集群需要 HAProxy？
虽然已经搭建了 RabbitMQ 集群，数据在节点间是同步的，但**客户端连接**仍然需要处理，HAProxy 提供了：

1. **统一入口点**：客户端不需要在代码里写三个地址。
2. **负载均衡**：成千上万的客户端连接可以被均匀地分散到三个 RabbitMQ 节点上，防止某个节点的连接数过多。
3. **管理界面负载均衡**：同样，对管理界面的访问也可以通过 HAProxy 进行负载。

## 如何为 RabbitMQ 集群部署 HAProxy？
基于已有的 `dajiankang` 网络，以下是一个部署方案。

### 创建 HAProxy 配置文件
创建一个目录存放配置：

```bash
mkdir -p /home/haproxy/conf
```

创建配置文件 `/home/haproxy/conf/haproxy.cfg`：

```plain
cat > /home/haproxy/conf/haproxy.cfg << 'EOF'
global
    daemon
    maxconn 4000
    log stdout format raw local0 info

defaults
    mode tcp
    option tcplog
    option dontlognull
    timeout connect 5000ms
    timeout client 50000ms
    timeout server 50000ms
    log global

# 统计信息页面
listen stats
    bind *:8100
    mode http
    stats enable
    stats uri /
    stats refresh 5s

# RabbitMQ AMQP 负载均衡
listen rabbitmq_amqp
    bind *:5670
    mode tcp
    balance roundrobin
    server rabbitmq1 172.16.0.13:5672 check inter 5s rise 2 fall 3
    server rabbitmq2 172.16.0.15:5672 check inter 5s rise 2 fall 3
    server rabbitmq3 172.16.0.16:5672 check inter 5s rise 2 fall 3

# RabbitMQ 管理界面负载均衡
listen rabbitmq_http
    bind *:15670
    mode tcp
    balance roundrobin
    server rabbitmq1 172.16.0.13:15672 check inter 10s rise 2 fall 3
    server rabbitmq2 172.16.0.15:15672 check inter 10s rise 2 fall 3
    server rabbitmq3 172.16.0.16:15672 check inter 10s rise 2 fall 3
EOF
```

**关键配置说明：**

+ `bind *:5670`：使用 `5670` 作为新的 AMQP 端口，避免和之前映射的 `5672` 等端口冲突。客户端程序以后就连接这个端口。
+ `balance roundrobin`：轮询算法，依次将新连接分发给后端服务器。
+ `option tcp-check`：对 AMQP 端口进行 TCP 层面的健康检查。
+ `option httpchk`：对管理界面进行 HTTP API 健康检查。
+ `inter 5s`：每 5 秒检查一次。
+ `rise 2`：连续 2 次检查成功，标记服务器为健康。
+ `fall 3`：连续 3 次检查失败，标记服务器为宕机，并从负载均衡池中移除。

### 启动 HAProxy 容器
拉取 docker 镜像：

```shell
docker pull haproxy:2.8.1
```

使用一个固定的 IP（例如 `172.16.0.20`）启动 HAProxy：

```bash
docker run -d --name haproxy \
  --net dajiankang --ip 172.16.0.20 \
  -p 5670:5670 \
  -p 15670:15670 \
  -p 8100:8100 \
  -v /home/haproxy/conf:/usr/local/etc/haproxy:ro \
  --restart unless-stopped \
  haproxy:2.8.1
```

### 配置 VirtualBox 端口转发
在 VirtualBox 中为 HAProxy 的端口添加转发规则：

| **Windows 端口** | **虚拟机端口** | **Docker 容器端口** | **用途** |
| --- | --- | --- | --- |
| 5670 | 5670 | 5670 | **新的 AMQP 统一入口**，客户端连接此端口 |
| 15670 | 15670 | 15670 | **新的管理界面统一入口** |


## 架构总结
部署 HAProxy 后，整体架构将变为：

```plain
[应用程序]
        |
        | (连接 localhost:5670)
        v
    [HAProxy] (172.16.0.20:5670) - 负载均衡器 & 单一入口
        |
        | (根据策略分发连接)
    +---+-----------+-----------+
    |               |           |
    v               v           v
[Node1]         [Node2]       [Node3]
(172.16.0.13)  (172.16.0.15) (172.16.0.16)
```

**这个架构在生产环境中是非常经典和可靠的。它实现了负载均衡，并且还可以自动将故障节点从集群中删除。**

## 测试 Web 界面是否可用
注意：访问端口是 `15670`，是通过 HAProxy 访问的。

在 windows 环境下，通过这个 url 看看能不能访问：[http://localhost:15670/#/](http://localhost:15670/#/)

如果能够正常访问则表示 Web 界面的负载均衡是有效的。

另外，刷新页面后，浏览器右上角会进行 MQ 节点的切换。

## 测试客户端程序是否可以正常使用
使用 Web 管理界面创建：

+ 创建交换机：`exchange.cluster`
+ 创建队列：`queue.cluster`
+ 队列绑定路由键：`routing.key.cluster`



**编写生产端的代码：**和之前生产端的代码相同，只是配置文件中的端口号变化了。使用 HAProxy 的端口号。

```yaml
spring:
  rabbitmq:
    host: localhost
    port: 5670
    username: admin
    password: 123456
    virtual-host: /
```

**测试程序如下：**

```java
package com.jkweilai.producercluster;

import org.junit.jupiter.api.Test;
import org.springframework.amqp.rabbit.core.RabbitTemplate;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;

@SpringBootTest
class ProducerClusterApplicationTests {

    @Autowired
    private RabbitTemplate rabbitTemplate;

    public static final String EXCHANGE_CLUSTER = "exchange.cluster";
    public static final String ROUTING_KEY_CLUSTER = "routing.key.cluster";

    @Test
    public void test() {
        rabbitTemplate.convertAndSend(EXCHANGE_CLUSTER, ROUTING_KEY_CLUSTER, "hello rabbit!");
    }
}

```



**查看队列上是否有消息：**

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1764066093295-b1bc6921-278b-4a64-ada9-9d9c08bfa8e0.png" width="420" title="" crop="0,0,1,1" id="u1886eb78" class="ne-image">

# 仲裁队列（`Quorum`）
在 RabbitMQ 3.8.x 版本之后支持的新内容。

镜像队列可以实现高可用，仲裁队列也可以实现高可用（自动选举机制），RabbitMQ 建议使用仲裁队列。

**<font style="color:rgb(15, 17, 21);">使用仲裁队列后，会</font>****<font style="color:#DF2A3F;">自动发生</font>****<font style="color:rgb(15, 17, 21);">以下的事情：</font>**

+ <font style="color:rgb(15, 17, 21);">在集群所有节点上创建队列副本</font>
+ <font style="color:rgb(15, 17, 21);">所有消息自动复制到所有节点</font>
+ <font style="color:rgb(15, 17, 21);">Master 节点处理读写，Slaves 作为备份</font>

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

# Federation 插件
这部分内容和之前搭建的集群就没有关系了。

Federation 翻译为联邦。

## 理解 Federation
**RabbitMQ Federation 用于在不同 RabbitMQ 集群之间自动复制消息，实现跨****<font style="color:#DF2A3F;">网络域</font>****的消息传输。**

**它是 RabbitMQ 的一个插件。**

### 主要场景
1. **跨****<font style="color:#DF2A3F;">机房/地域</font>**** 复制** - 北京集群 ↔ 上海集群
2. **上下游系统集成** - 生产集群 → 消费集群

### Federation vs 镜像队列/仲裁队列
| **特性** | **镜像/仲裁队列 (Mirroring)** | **Federation** |
| --- | --- | --- |
| **范围** | 同一集群内节点 | **跨集群/跨网络** |
| **网络要求** | 低延迟局域网 | 可容忍较高延迟 |
| **数据一致性** | 强一致性 | **最终一致性** |
| **使用场景** | 高可用 | 地理分布、系统集成 |


### 需要 Federation
+ 多地数据中心消息同步
+ 云上云下混合架构
+ 不同业务域消息互通

### 不需要 Federation
+ 单一机房内的集群
+ 实时性要求极高的场景
+ 网络稳定的局域网环境

### 总结一下
**Federation 是 RabbitMQ 的"广域网消息桥梁"**，解决了镜像队列只能在局域网使用的问题，让你可以构建地理分布的 RabbitMQ 架构。

如果你的系统需要：

+ 跨地域部署
+ 混合云架构  
+ 系统间消息集成

那么 Federation **非常重要**！如果只是单个机房内的集群，用镜像队列/仲裁队列就够了。

## 创建两个 RabbitMQ 实例
使用 docker 容器创建两个 RabbitMQ 的实例。

```shell
docker run -d --name rabbitmq-beijing \
  --net dajiankang --ip 172.16.0.21 \
  -p 56722:5672 \
  -p 15675:15672 \
  -e RABBITMQ_DEFAULT_USER=admin \
  -e RABBITMQ_DEFAULT_PASS=123456 \
  -e TZ=Asia/Shanghai \
  -m 450m \
  --restart unless-stopped \
  rabbitmq:3.13-management
```

```java
docker run -d --name rabbitmq-shanghai \
  --net dajiankang --ip 172.16.0.22 \
  -p 56723:5672 \
  -p 15676:15672 \
  -e RABBITMQ_DEFAULT_USER=admin \
  -e RABBITMQ_DEFAULT_PASS=123456 \
  -e TZ=Asia/Shanghai \
  -m 450m \
  --restart unless-stopped \
  rabbitmq:3.13-management
```



## 配置端口转发
| **windows 端口** | **虚拟机端口** | **docker 端口** |
| --- | --- | --- |
| 56722 | 56722 | 5672 |
| 15675 | 15675 | 15672 |




| **windows 端口** | **虚拟机端口** | **docker 端口** |
| --- | --- | --- |
| 56723 | 56723 | 5672 |
| 15676 | 15676 | 15672 |


## 启用 Federation 插件
```shell
# 北京的
docker exec -it rabbitmq-beijing rabbitmq-plugins enable rabbitmq_federation
docker exec -it rabbitmq-beijing rabbitmq-plugins enable rabbitmq_federation_management

# 上海的
docker exec -it rabbitmq-shanghai rabbitmq-plugins enable rabbitmq_federation
docker exec -it rabbitmq-shanghai rabbitmq-plugins enable rabbitmq_federation_management
```



北京的 web 管理界面：[http://localhost:15675/](http://localhost:15675/)



上海的 web 管理界面：[http://localhost:15676/](http://localhost:15675/)



如果进入 web 管理界面，看到如下图，表示插件启用成功了。

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1764070775597-38fec8ec-4839-434d-a9a2-316d2ff46db8.png" width="1355.2" title="" crop="0,0,1,1" id="ud1c26c14" class="ne-image">

## 联邦交换机
### 在下游<font style="color:#DF2A3F;">定义</font>上游的地址
假设北京是上游（端口 15675）。上海是下游（端口 15676）。需要在下游中配置：告诉下游，它的上游节点在哪里。

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1764071171721-695b56f0-ddc1-4e9a-ba3d-0ae7882982dc.png" width="1464.8" title="" crop="0,0,1,1" id="ud3af1d32" class="ne-image">

上游的名字就填（**随便起名**）：`beijing.upstream`

上游的 URI：`amqp://admin:123456@rabbitmq-beijing:5672`

**在下游配置联邦交换机，在下游中需要指定上游的地址。**

### 下游配置 Federation 交换机策略
在下游配置交换机策略：

**<font style="color:rgb(15, 17, 21);">这个策略的作用是：自动将匹配 </font>**`**<font style="color:rgb(15, 17, 21);background-color:rgb(235, 238, 242);">^federation\.</font>**`**<font style="color:rgb(15, 17, 21);"> 的交换机设置为联邦交换机（Federation Exchange），并连接到北京的上游集群。</font>**

`**<font style="color:rgb(15, 17, 21);background-color:rgb(235, 238, 242);">^federation\.</font>**`**<font style="color:rgb(15, 17, 21);"> 是正则表达式：表示交换机名字以 </font>**`**<font style="color:rgb(15, 17, 21);">federation.</font>**`**<font style="color:rgb(15, 17, 21);">开头的都设置为联邦交换机。</font>**

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1764073208259-172ef6d5-90c1-4c97-a977-a5e4e938d00b.png" width="1448" title="" crop="0,0,1,1" id="u83bff58a" class="ne-image">

策略名字（**随便写**）：`policy.federation.exchange`

正则表达式：`^federation\.`

应用到交换机：`Exchanges`

优先级：`10`

定义：`federation-upstream`=`beijing.upstream`

### 注意事项
<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1764073999436-2ec179e8-8b74-4d7c-aa3d-f59f7c8958f3.png" width="605.4000244140625" title="" crop="0,0,1,1" id="u289021f7" class="ne-image">

**注意：**

1. **普通交换机**和**联邦交换机**名称必须一致。
2. **交换机名称**要求和**策略中的正则表达式**匹配上。
3. 发送消息时，两边使用的**路由键要一致**。
4. 队列名称可以不一致。

### 上游创建组件
创建交换机：`federation.exchange.demo`

创建队列：`queue.normal.beijing`

队列绑定路由键：`routing.key.demo.test`

### 下游创建组件
创建交换机：`federation.exchange.demo`

创建队列：`queue.normal.shanghai`

队列绑定路由键：`routing.key.demo.test`

### 在上游<font style="color:#DF2A3F;">交换机上</font>发条消息测试
在上游的 web 管理界面中发送一条消息，进行测试，看看下游的队列中是否也存在这条消息：注意，是在交换机上发送消息。**<font style="color:#DF2A3F;">因为现在配置的是联邦交换机</font>**。

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1764077482490-cbb0a24b-6cf8-4d75-8a05-78ed7c0643a1.png" width="843.2" title="" crop="0,0,1,1" id="u66a72ee6" class="ne-image">



**发送之后，去下游看看，队列中也有数据就对了：**

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1764077514501-763141a1-7fd0-42e5-89d2-0cd2f366a7e9.png" width="247.2" title="" crop="0,0,1,1" id="u4f5a1b34" class="ne-image">

## 联邦队列
### 下游配置 Federation<font style="color:#DF2A3F;"> 队列</font>策略
<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1764078244455-1c415efd-7287-46c1-a0ad-330bfa535bed.png" width="1468" title="" crop="0,0,1,1" id="uba2e657b" class="ne-image">

**名字：**`policy.federation.queue`

**正则：**`^fed\.`

**应用到：**`Queues`

**优先级：**`10`

**定义：**`federation-upstream`= `beijing.upstream`

### 注意事项
1. 上游和下游的队列名称相同。
2. 下游不需要创建交换机和路由键。下游只需要创建队列。
3. 上游需要创建交换机、队列、绑定路由键。
4. 队列的名字要以：`fed.`开头。**因为策略中的正则规定了**。

### 上游创建组件
创建交换机：`exchange.normal.beijing`

创建队列：`fed.queue.demo`

绑定路由键：`routing.key.normal.beijing`

### 下游创建组件
创建队列：`fed.queue.demo`

### 在上游的<font style="color:#DF2A3F;">交换机</font>位置发送一条消息
<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1764078820564-440dbf05-4b87-467a-aaaa-0f17a30d0e79.png" width="728.8" title="" crop="0,0,1,1" id="udaf2407b" class="ne-image">



**你会看到，上游的队列中是有消息的：**

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1764078857154-e21dd386-da8f-4f48-82b1-659922c055bb.png" width="195.2" title="" crop="0,0,1,1" id="ud83d022d" class="ne-image">



**但是下游队列看不到消息：**

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1764078880939-267d4bab-95b2-4aad-9878-d9390a3dc49e.png" width="156.8" title="" crop="0,0,1,1" id="u597fcc9d" class="ne-image">



**这是联邦队列特有的特点。和联邦交换机的工作原理不同。对于联邦队列来说，要想从上游的队列中获取消息，需要编写消费端的监听程序。并且消费端的监听程序是优先消费自己队列中的数据，只有当自己队列中的消息消费完了，才会从上游队列中进行消费。接下来编写消费者监听程序，看看能不能消费上游的消息。**

### 编写消费者监听程序
创建一个新的消费者项目，yml 配置如下：

```yaml
spring:
  rabbitmq:
    host: localhost
    port: 56723
    username: admin
    password: 123456
    virtual-host: /
```



编写消费者监听程序，监听队列：

```java
package com.jkweilai.mq.listener;

import com.rabbitmq.client.Channel;
import org.springframework.amqp.core.Message;
import org.springframework.amqp.rabbit.annotation.RabbitListener;
import org.springframework.stereotype.Component;

import java.io.IOException;

@Component
public class MyMessageListener {

    public static final String QUEUE_FED =  "fed.queue.demo";
    @RabbitListener(queues = {QUEUE_FED})
    public void processMessageDelay(String dataString, Message message, Channel channel) throws IOException {
        System.out.println(dataString);
        channel.basicAck(message.getMessageProperties().getDeliveryTag(), false);
    }
}

```



**启动消费者监听，查看控制台，有没有消息：**

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1764079408040-1a02b6b9-4f4a-4876-85fb-ca71e18f1127.png" width="440.8" title="" crop="0,0,1,1" id="u574cec04" class="ne-image">

不需要管这个异常，看到消息消费了就表示成功了。



**联邦队列和联邦交换机的区别：**

1. 联邦交换机主要完成上游集群和下游集群数据的复制/同步。下游消费的时候只消费下游的队列中的消息。
2. 联邦队列在下游进行消费的时候，先消费下游队列的消息，如果消费已经消费完了。会继续消费上游队列中的消息。

# Shovel 插件（铲子）
## Shovel 插件是干啥的
**<font style="color:rgb(15, 17, 21);">Shovel插件用于在两个RabbitMQ节点间 可靠地 </font>****<font style="color:#DF2A3F;">移动消息队列中的消息</font>**<font style="color:rgb(15, 17, 21);">，类似于一个单向的消息搬运工。</font>

**<font style="color:rgb(15, 17, 21);">Federation</font>**<font style="color:rgb(15, 17, 21);"> 是</font>**<font style="color:rgb(15, 17, 21);">交换机级别</font>**<font style="color:rgb(15, 17, 21);">的</font>**<font style="color:rgb(15, 17, 21);">实时消息复制</font>**<font style="color:rgb(15, 17, 21);">，而 </font>**<font style="color:rgb(15, 17, 21);">Shovel</font>**<font style="color:rgb(15, 17, 21);"> 是</font>**<font style="color:rgb(15, 17, 21);">队列级别</font>**<font style="color:rgb(15, 17, 21);">的</font>**<font style="color:rgb(15, 17, 21);">消息搬运和迁移</font>**<font style="color:rgb(15, 17, 21);">。</font>

## 启用 Shovel 插件
```shell
# 北京的
docker exec -it rabbitmq-beijing rabbitmq-plugins enable rabbitmq_shovel
docker exec -it rabbitmq-beijing rabbitmq-plugins enable rabbitmq_shovel_management

# 上海的
docker exec -it rabbitmq-shanghai rabbitmq-plugins enable rabbitmq_shovel
docker exec -it rabbitmq-shanghai rabbitmq-plugins enable rabbitmq_shovel_management
```



<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1764079777278-14b206ab-a687-41bf-93af-0a677f622541.png" width="940" title="" crop="0,0,1,1" id="uafce4dc6" class="ne-image">

显示以上界面则表示成功。

## 配置 Shovel
在上游可以配置，下游也可以配置。我们这里在下游配置一下吧：



<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1764080249380-e92c7a89-4672-445a-a8eb-155715e1845c.png" width="1505.6" title="" crop="0,0,1,1" id="u270beed3" class="ne-image">



名字：`myshovel`



源的地址：`amqp://admin:123456@rabbitmq-beijing:5672`

源队列：`queue.shovel.beijing`



目标地址：`amqp://admin:123456@rabbitmq-shanghai:5672`

目标队列：`queue.shovel.shanghai`



## 上游创建组件
创建交换机：`exchange.shovel.test`

创建队列：`queue.shovel.beijing`

队列绑定路由键：`routing.key.shovel`

## 下游创建组件
创建队列：`queue.shovel.shanghai`

## 测试
在上游的交换机上发消息。可以观察到：上游的队列中看不到消息，下游的队列中可以看到消息。因为消息发到上游队列之后，被 shovel 移动到了下游队列中



<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1764080968553-6c09a742-2941-47e1-966f-1b0f984f27ad.png" width="681.6" title="" crop="0,0,1,1" id="u797dd860" class="ne-image">



**上游队列：**

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1764080848569-8c666480-1db7-4bb3-8376-0dd421f4940b.png" width="220.8" title="" crop="0,0,1,1" id="ue7f405e9" class="ne-image">



**下游队列：**

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1764080887138-c499f28c-2cb6-4115-af91-758470d4aed2.png" width="180" title="" crop="0,0,1,1" id="uadfbebee" class="ne-image">



到此，我们的 RabbitMQ 的课程就结束了。