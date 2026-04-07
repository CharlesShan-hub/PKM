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