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

