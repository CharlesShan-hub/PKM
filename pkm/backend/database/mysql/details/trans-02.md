
演示：

| **A事务** | **B事务** |
| --- | --- |
| mysql> use powernode |  |
|  | mysql> use powernode |
| mysql> start transaction; |  |
|  | mysql> start transaction; |
| mysql> select * from a;
![image.png](https://cdn.nlark.com/yuque/0/2024/png/21376908/1709003985270-00489f1c-e135-4bd6-aa08-84cdddf6f007.png#averageHue=%230f0e0d&clientId=u0fbbe02e-04ac-4&from=paste&height=191&id=u5d9d9ed4&originHeight=191&originWidth=289&originalType=binary&ratio=1&rotation=0&showTitle=false&size=4388&status=done&style=shadow&taskId=ub714d0fd-c9f2-48d8-9130-c4b0827471a&title=&width=289) |  |
|  | mysql> insert into a values(4); |
| mysql> select * from a;
![image.png](https://cdn.nlark.com/yuque/0/2024/png/21376908/1709003985270-00489f1c-e135-4bd6-aa08-84cdddf6f007.png#averageHue=%230f0e0d&clientId=u0fbbe02e-04ac-4&from=paste&height=191&id=yl5zF&originHeight=191&originWidth=289&originalType=binary&ratio=1&rotation=0&showTitle=false&size=4388&status=done&style=shadow&taskId=ub714d0fd-c9f2-48d8-9130-c4b0827471a&title=&width=289) |  |
|  | mysql> commit; |
| mysql> select * from a;
![image.png](https://cdn.nlark.com/yuque/0/2024/png/21376908/1709004165277-dac7bc73-55ba-4034-bd48-b975689ffb41.png#averageHue=%230f0e0d&clientId=u0fbbe02e-04ac-4&from=paste&height=214&id=ucc8e1eca&originHeight=214&originWidth=298&originalType=binary&ratio=1&rotation=0&showTitle=false&size=4626&status=done&style=shadow&taskId=u2cac7a44-ba45-4bd7-86c2-2d280c9de57&title=&width=298) |  |

通过以上测试看出，A事务只能读取到B事务提交之后的数据。这种隔离级别解决了脏读问题，但肯定是存在不可重复读和幻读问题。因为只要事务B进行了增删改操作之后并提交了，事务A读取到的数据肯定是不同的。即：不可重复读和幻读都存在。