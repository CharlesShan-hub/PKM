# Shovel 插件（铲子）
## Shovel 插件是干啥的
**<font style="color:rgb(15, 17, 21);">Shovel插件用于在两个RabbitMQ节点间 可靠地 </font>****<font style="color:#DF2A3F;">移动消息队列中的消息</font>**<font style="color:rgb(15, 17, 21);">，类似于一个单向的消息搬运工。</font>

**<font style="color:rgb(15, 17, 21);">Federation</font>**<font style="color:rgb(15, 17, 21);"> 是</font>**<font style="color:rgb(15, 17, 21);">交换机级别</font>**<font style="color:rgb(15, 17, 21);">的</font>**<font style="color:rgb(15, 17, 21);">实时消息复制</font>**<font style="color:rgb(15, 17, 21);">，而 </font>**<font style="color:rgb(15, 17, 21);">Shovel</font>**<font style="color:rgb(15, 17, 21);"> 是</font>**<font style="color:rgb(15, 17, 21);">队列级别</font>**<font style="color:rgb(15, 17, 21);">的</font>**<font style="color:rgb(15, 17, 21);">消息搬运和迁移</font>**<font style="color:rgb(15, 17, 21);">。</font>

## 启用 Shovel 插件
```shell