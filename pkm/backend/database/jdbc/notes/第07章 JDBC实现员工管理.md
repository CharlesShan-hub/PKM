![](https://cdn.nlark.com/yuque/0/2023/jpeg/21376908/1692002570088-3338946f-42b3-4174-8910-7e749c31e950.jpeg#averageHue=%23f9f8f8&from=url&id=O8j9i&originHeight=78&originWidth=1400&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=shadow&title=)
# 数据库表的准备
```sql
drop table if exists t_employee;

create table t_employee(
  id bigint primary key auto_increment,
  name varchar(255),
  job varchar(255),
  hiredate char(10),
  salary decimal(10,2),
  address varchar(255)
);

insert into t_employee(name,job,hiredate,salary,address) values('张三','销售员','1999-10-11',5000.0,'北京朝阳');
insert into t_employee(name,job,hiredate,salary,address) values('李四','编码人员','1998-02-12',5000.0,'北京海淀');
insert into t_employee(name,job,hiredate,salary,address) values('王五','项目经理','2000-08-11',5000.0,'北京大兴');
insert into t_employee(name,job,hiredate,salary,address) values('赵六','产品经理','2022-09-11',5000.0,'北京东城');
insert into t_employee(name,job,hiredate,salary,address) values('钱七','测试员','2024-12-11',5000.0,'北京西城');

commit;

select * from t_employee;
```

![image.png](https://cdn.nlark.com/yuque/0/2024/png/21376908/1713071562929-40bc3b9b-59e0-4447-a6d2-ee9a402112d7.png#averageHue=%23161412&clientId=u0929d9a6-cc56-4&from=paste&height=215&id=uc93280dc&originHeight=215&originWidth=785&originalType=binary&ratio=1&rotation=0&showTitle=false&size=30172&status=done&style=none&taskId=u89bc78cb-d7b8-4d61-8c0d-3ab3a620ad7&title=&width=785)

![](https://cdn.nlark.com/yuque/0/2023/jpeg/21376908/1692002570088-3338946f-42b3-4174-8910-7e749c31e950.jpeg#averageHue=%23f9f8f8&from=url&id=Tit1x&originHeight=78&originWidth=1400&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=shadow&title=)
# 实现效果
## 查看员工列表
![image.png](https://cdn.nlark.com/yuque/0/2024/png/21376908/1713087932128-c20f65b8-19f2-435d-b926-4fcf9e76942b.png#averageHue=%23222326&clientId=u51a6216a-4bdd-4&from=paste&height=465&id=ubd9d0e1b&originHeight=465&originWidth=633&originalType=binary&ratio=1&rotation=0&showTitle=false&size=15839&status=done&style=none&taskId=u5b9c816e-73d5-4892-8517-e1e5c7d7e4d&title=&width=633)

![](https://cdn.nlark.com/yuque/0/2023/jpeg/21376908/1692002570088-3338946f-42b3-4174-8910-7e749c31e950.jpeg#averageHue=%23f9f8f8&from=url&id=eJf90&originHeight=78&originWidth=1400&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=shadow&title=)
## 查看员工详情
![image.png](https://cdn.nlark.com/yuque/0/2024/png/21376908/1713087955719-046dd8f5-0e08-464b-99f2-e3082468e90d.png#averageHue=%23222326&clientId=u51a6216a-4bdd-4&from=paste&height=675&id=u6e8c1a73&originHeight=675&originWidth=589&originalType=binary&ratio=1&rotation=0&showTitle=false&size=27719&status=done&style=none&taskId=u69513093-6a8c-4064-a1f2-ad2aa7906c1&title=&width=589)

![](https://cdn.nlark.com/yuque/0/2023/jpeg/21376908/1692002570088-3338946f-42b3-4174-8910-7e749c31e950.jpeg#averageHue=%23f9f8f8&from=url&id=sDZ4B&originHeight=78&originWidth=1400&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=shadow&title=)
## 新增员工
![image.png](https://cdn.nlark.com/yuque/0/2024/png/21376908/1713088066941-2485c84a-81e3-4bed-b60b-d5ab1ce1e519.png#averageHue=%23222326&clientId=u51a6216a-4bdd-4&from=paste&height=621&id=u41b83656&originHeight=621&originWidth=624&originalType=binary&ratio=1&rotation=0&showTitle=false&size=26277&status=done&style=none&taskId=uee76f7c1-1123-42a8-8f30-49ae8c70a9d&title=&width=624)

![](https://cdn.nlark.com/yuque/0/2023/jpeg/21376908/1692002570088-3338946f-42b3-4174-8910-7e749c31e950.jpeg#averageHue=%23f9f8f8&from=url&id=o3IRP&originHeight=78&originWidth=1400&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=shadow&title=)
## 修改员工
![image.png](https://cdn.nlark.com/yuque/0/2024/png/21376908/1713088222666-785c5584-713d-45a0-b043-5df952816849.png#averageHue=%23212226&clientId=u51a6216a-4bdd-4&from=paste&height=811&id=u61d10dbc&originHeight=811&originWidth=489&originalType=binary&ratio=1&rotation=0&showTitle=false&size=38407&status=done&style=none&taskId=uc8d4c2e4-6e41-4c0f-b589-eb6705e34dc&title=&width=489)

![](https://cdn.nlark.com/yuque/0/2023/jpeg/21376908/1692002570088-3338946f-42b3-4174-8910-7e749c31e950.jpeg#averageHue=%23f9f8f8&from=url&id=QMw6x&originHeight=78&originWidth=1400&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=shadow&title=)
## 删除员工
![image.png](https://cdn.nlark.com/yuque/0/2024/png/21376908/1713088256331-8e3f1218-7136-4af7-957b-4ef3ed59fb30.png#averageHue=%23212226&clientId=u51a6216a-4bdd-4&from=paste&height=728&id=u273d2b97&originHeight=728&originWidth=629&originalType=binary&ratio=1&rotation=0&showTitle=false&size=22918&status=done&style=none&taskId=u0e89aba5-394b-48bb-82b5-693157a38a2&title=&width=629)

![](https://cdn.nlark.com/yuque/0/2023/jpeg/21376908/1692002570088-3338946f-42b3-4174-8910-7e749c31e950.jpeg#averageHue=%23f9f8f8&from=url&id=e9yPL&originHeight=78&originWidth=1400&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=shadow&title=)
## 退出系统
![image.png](https://cdn.nlark.com/yuque/0/2024/png/21376908/1713088276650-2f1eb4aa-10aa-45ac-b280-fd195590c294.png#averageHue=%23242529&clientId=u51a6216a-4bdd-4&from=paste&height=304&id=u8ff9e92f&originHeight=304&originWidth=581&originalType=binary&ratio=1&rotation=0&showTitle=false&size=11582&status=done&style=none&taskId=ud6a33007-f21a-4260-84ec-c7e93dac5e8&title=&width=581)
![](https://cdn.nlark.com/yuque/0/2023/jpeg/21376908/1692002570088-3338946f-42b3-4174-8910-7e749c31e950.jpeg#averageHue=%23f9f8f8&from=url&id=BvnCD&originHeight=78&originWidth=1400&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=shadow&title=)
