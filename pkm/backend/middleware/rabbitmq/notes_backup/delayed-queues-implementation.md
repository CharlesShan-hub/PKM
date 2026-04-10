# 延迟队列
**延迟队列就是让消息在指定的延迟时间之后才被消费的特殊队列。**

****

**在电商平台上，用户下单之后，会显示：请在多长时间内支付。这个机制实现有多种方案，但其中有一种方案就是：采用延迟队列来完成。**

****

## **实现延迟队列的第一种方案**
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