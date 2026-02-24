
演示：

| **A事务** | **B事务** |
| --- | --- |
| mysql> use powernode |  |
|  | mysql> use powernode |
| mysql> start transaction; |  |
|  | mysql> start transaction; |
| mysql> select empno,ename,sal from emp where empno=7369;
![image.png](https://cdn.nlark.com/yuque/0/2024/png/21376908/1709005877270-b84cdf55-866b-4b3b-b575-46552dfb84c0.png#averageHue=%23151312&clientId=u0fbbe02e-04ac-4&from=paste&height=109&id=u9a905011&originHeight=109&originWidth=344&originalType=binary&ratio=1&rotation=0&showTitle=false&size=5276&status=done&style=shadow&taskId=u85710df6-3409-4242-a3d5-92ea27f7fc2&title=&width=344) |  |
|  | mysql> update emp set ename='SMITH',sal=8000 where empno=7369; |
|  | mysql> commit; |
| mysql> select empno,ename,sal from emp where empno=7369;
![image.png](https://cdn.nlark.com/yuque/0/2024/png/21376908/1709005948358-4f23bd69-d6ed-4963-a349-ba35ecc61dc0.png#averageHue=%23151311&clientId=u0fbbe02e-04ac-4&from=paste&height=145&id=ub810f157&originHeight=145&originWidth=336&originalType=binary&ratio=1&rotation=0&showTitle=false&size=7381&status=done&style=shadow&taskId=ud25e00ad-83dc-4fa2-9858-de459ea77f8&title=&width=336) |  |

通过以上测试得知：当事务隔离级别设置为可重复读时，避免了不可重复读问题。

那么在MySQL当中，当事务隔离级别设置为可重复读时，能够避免幻读问题吗？测试一下：

| **事务A** | **事务B** |
| --- | --- |
| mysql> use powernode |  |
|  | mysql> use powernode |
| mysql> start transaction; |  |
|  | mysql> start transaction; |
| mysql> select * from a;
![image.png](https://cdn.nlark.com/yuque/0/2024/png/21376908/1709006316610-12c48e73-e894-49dc-8dfd-32f8d13ec991.png#averageHue=%230f0e0d&clientId=u0fbbe02e-04ac-4&from=paste&height=218&id=ud9dadda5&originHeight=218&originWidth=298&originalType=binary&ratio=1&rotation=0&showTitle=false&size=4645&status=done&style=shadow&taskId=ua4e22c07-45ef-467a-9a47-c66b5a21472&title=&width=298) |  |
|  | mysql> insert into a values(5); |
|  | mysql> commit; |
| mysql> select * from a;
![image.png](https://cdn.nlark.com/yuque/0/2024/png/21376908/1709006362804-0579079b-e054-4299-b1ab-6c16a68875f0.png#averageHue=%230f0e0d&clientId=u0fbbe02e-04ac-4&from=paste&height=218&id=u4c4264a7&originHeight=218&originWidth=297&originalType=binary&ratio=1&rotation=0&showTitle=false&size=4643&status=done&style=shadow&taskId=ua8b9a51a-306e-4b30-afdf-c88138fa2a7&title=&width=297) |  |

通过以上测试得知：**当事务隔离级别设置为可重复读时，也避免了幻读问题。是完全避免了幻读问题吗？并不是。**请看以下测试：

| **事务A** | **事务B** |
| --- | --- |
| mysql> use powernode |  |
|  | mysql> use powernode |
| mysql> start transaction; |  |
|  | mysql> start transaction; |
| mysql> select * from a;
![image.png](https://cdn.nlark.com/yuque/0/2024/png/21376908/1709006612649-1614f4b7-446f-487d-9c1b-000a7e5589d3.png#averageHue=%230f0e0d&clientId=u0fbbe02e-04ac-4&from=paste&height=241&id=ud98016d5&originHeight=241&originWidth=288&originalType=binary&ratio=1&rotation=0&showTitle=false&size=4986&status=done&style=shadow&taskId=u400d7356-cb23-442b-bf41-3a6c7851f3a&title=&width=288) |  |
|  | mysql> insert into a values(6); |
|  | mysql> commit; |
| mysql> select * from a **for update;**
![image.png](https://cdn.nlark.com/yuque/0/2024/png/21376908/1709006674069-b52a691f-2cc1-4721-bf23-0451f4bb7535.png#averageHue=%230e0d0d&clientId=u0fbbe02e-04ac-4&from=paste&height=269&id=uaeabeaf9&originHeight=269&originWidth=295&originalType=binary&ratio=1&rotation=0&showTitle=false&size=5453&status=done&style=shadow&taskId=u127a2aaf-fd6d-421c-be74-3f50b8fa988&title=&width=295) |  |

通过以上测试得知：**当事务隔离级别设置为可重复读，MySQL会尽最大努力避免幻读问题，但这种隔离级别无法完全避免幻读问题。**