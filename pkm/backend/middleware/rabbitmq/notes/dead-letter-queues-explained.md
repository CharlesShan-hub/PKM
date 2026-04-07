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