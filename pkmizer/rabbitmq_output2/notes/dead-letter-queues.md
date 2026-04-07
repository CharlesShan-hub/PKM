rk.com/yuque/0/2025/png/21376908/1763812791351-3b855a2e-2805-4e2b-87ba-1d00ffeaa80f.png" width="259.2" title="" crop="0,0,1,1" id="uac084399" class="ne-image">

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1763813986720-72095c2d-a0ac-465d-bbe7-0f7eb3ffd5e5.png" width="935.4000244140625" title="" crop="0,0,1,1" id="u38a0c504" class="ne-image">

**<font style="color:rgb(15, 17, 21);">在Routing模式的基础上，支持使用通配符进行更灵活的模式匹配，实现基于主题的消息路由。</font>**

**<font style="color:rgb(15, 17, 21);">通配符匹配</font>**<font style="color:rgb(15, 17, 21);">：支持 </font>`<font style="color:rgb(15, 17, 21);background-color:rgb(235, 238, 242);">*</font>`<font style="color:rgb(15, 17, 21);">（匹配一个单词）和 </font>`<font style="color:rgb(15, 17, 21);background-color:rgb(235, 238, 242);">#</font>`<font style="color:rgb(15, 17, 21);">（匹配零个或多个单词）</font>

**<font style="color:rgb(15, 17, 21);">交换机类型</font>**<font style="color:rgb(15, 17, 21);">：使用 </font>**<font style="color:rgb(15, 17, 21);">Topic Exchange</font>**

**<font style="color:rgb(15, 17, 21);">灵活路由</font>**<font style="color:rgb(15, 17, 21);">：基于主题的发布订阅，比Direct模式更灵活</font>

### <font style="color:rgb(15, 17, 21);">编写生产者端</font>
```java
package com.jkweilai.rabbitmq.topic;

import com.jkweilai.rabbitmq.util.ConnectionUtil;
import com.rabbitmq.client.BuiltinExchangeType;
import com.rabbitmq.client.Channel;
import com.rabbitmq.client.Connection;

// 1.创建交换机（指定交换机类型）
// 2.创建队列
// 3.使用 模糊路由键 绑定交换机和队列
// 4.发消息的时候指定交换机和具体的路由键
public class Producer {
    public static void main(String[] args) throws Exception {
        Connection connection = ConnectionUtil.getConnection();
        Channel channel = connection.createChannel();

        // 创建交换机
        String exchangeName = "topic_exchange";
        channel.exchangeDeclare(exchangeName, BuiltinExchangeType.TOPIC, true, false, false, null);

        // 创建两个队列
        String queueName1 = "topic_queue1";
        String queueName2 = "topic_queue2";
        channel.queueDeclare(queueName1, true, false, false, null);
        channel.queueDeclare(queueName2, true, false, false, null);

        // 交换机 + 队列1 + bindingKey(主题Key/模糊Key)
        // 需求：所有error级别的日志都插入到数据库。order系统的日志都插入到数据库。
        channel.queueBind(queueName1, exchangeName, "#.error");
        channel.queueBind(queueName1, exchangeName, "order.*");
        // 交换机 + 队列2 + bindingKey(主题Key/模糊Key)
        channel.queueBind(queueName2, exchangeName, "*.*");

        // 发送消息时指定路由键（routingKey）
        channel.basicPublish(exchangeName, "order.info", null, "2025-10-10 20:20:10 [INFO] 生成订