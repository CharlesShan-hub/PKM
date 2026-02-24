
演示：

| **事务A** | **事务B** |
| --- | --- |
| mysql> use powernode |   |
|   | mysql> use powernode |
| mysql> start transaction; |   |
|   | mysql> start transaction; |
| mysql> select * from a;
![image.png](https://cdn.nlark.com/yuque/0/2024/png/21376908/1709013080885-bf7ad024-3bdd-4497-997b-1bdc2c81a7da.png#averageHue=%230e0e0d&clientId=u0fbbe02e-04ac-4&from=paste&height=262&id=u98eae3de&originHeight=262&originWidth=292&originalType=binary&ratio=1&rotation=0&showTitle=false&size=5406&status=done&style=shadow&taskId=u7fd54c94-2d24-4710-a2f2-4eb6a0f50ad&title=&width=292) |   |
| mysql> insert into a values(7); |   |
|   | mysql> select * from a;
![image.png](https://cdn.nlark.com/yuque/0/2024/png/21376908/1709013571200-5bfdf9a5-8238-4601-92b7-5eacbd2de16f.png#averageHue=%230e0e0d&clientId=u0fbbe02e-04ac-4&from=paste&height=122&id=ubd8c88a4&originHeight=122&originWidth=284&originalType=binary&ratio=1&rotation=0&showTitle=false&size=2887&status=done&style=shadow&taskId=u18918bf7-edf5-48f1-95c0-21c1e7ae7e7&title=&width=284) |
| mysql> commit; |   |
|   | ![image.png](https://cdn.nlark.com/yuque/0/2024/png/21376908/1709013621752-5b81823b-362d-4cdc-8b49-f941eebd827f.png#averageHue=%230e0d0d&clientId=u0fbbe02e-04ac-4&from=paste&height=288&id=ufcf1f12d&originHeight=288&originWidth=297&originalType=binary&ratio=1&rotation=0&showTitle=false&size=5866&status=done&style=shadow&taskId=u385c19ee-7e7d-43de-8d5d-e9cee03e4e4&title=&width=297) |

通过以上测试得知：当事务隔离级别设置为串行化时，事务只能排队执行，不支持并发。
