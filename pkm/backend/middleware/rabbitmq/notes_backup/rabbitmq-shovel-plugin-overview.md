# Shovel 插件（铲子）
## Shovel 插件是干啥的
**Shovel插件用于在两个RabbitMQ节点间 可靠地 **移动消息队列中的消息**，类似于一个单向的消息搬运工。**

**Federation** 是**交换机级别**的**实时消息复制**，而 **Shovel** 是**队列级别**的**消息搬运和迁移**。

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