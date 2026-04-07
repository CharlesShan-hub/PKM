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