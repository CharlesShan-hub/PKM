# 在容器内执行以下命令
rabbitmqctl stop_app
rabbitmqctl reset
rabbitmqctl join_cluster rabbit@rabbitmq-node1
rabbitmqctl start_app
exit
```

**在节点3上执行，加入集群**：

```bash