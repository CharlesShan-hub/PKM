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