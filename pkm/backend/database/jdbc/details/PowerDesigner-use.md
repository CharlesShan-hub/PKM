
## 使用PowerDesigner进行物理数据建模
打开PowerDesigner：
![image.png](https://cdn.nlark.com/yuque/0/2023/png/21376908/1702352345350-1c1441c3-560f-4485-ba11-aff5522c7d42.png#averageHue=%239ec58f&clientId=u0cd9c8dc-062f-4&from=paste&height=694&id=u62d067c3&originHeight=694&originWidth=964&originalType=binary&ratio=1&rotation=0&showTitle=false&size=246317&status=done&style=shadow&taskId=u188417d2-31ad-44c7-b177-094b4303fc0&title=&width=964)

点击“Create Model...”来创建PDM（Physical Data Model，物理数据模型）：
![image.png](https://cdn.nlark.com/yuque/0/2023/png/21376908/1702352495755-cdb4ac5b-cdf4-408f-b87c-6f08208eadb8.png#averageHue=%23f1f0ef&clientId=u0cd9c8dc-062f-4&from=paste&height=693&id=ud8fcd53d&originHeight=693&originWidth=963&originalType=binary&ratio=1&rotation=0&showTitle=false&size=83783&status=done&style=none&taskId=u265fe6c8-c8b6-4f39-9dbc-2ba19711344&title=&width=963)

**什么是物理数据模型PDM？**
`物理数据模型（Physical Data Model，PDM）是数据管理领域中表示数据库逻辑设计后，通过物理设计最终转化为实际数据结构的过程，即在逻辑模型的基础上，进行数据存储结构的设计。PDM 是一个详细的数据库设计计划，它描述了如何在关系数据库中存储数据。物理数据模型包含了所有数据表，列、键和索引以及物理存储的详细信息，包括数据类型、字段宽度、默认值、统计信息等。此外，PDM 还描述了如何将数据表存储在文件或表空间中，这些信息可以帮助开发人员建立实际的数据库系统。通常，PDM 包含了完整的 ER 模型，数据表和关系的详细信息，包括数据的主键、外键、唯一键、索引、约束条件等。物理数据模型可以使用各种建模工具来手工创建或自动生成。在数据库设计阶段，生成 PDM 是非常重要的一步，是将逻辑设计转换为实际实现的重要步骤之一。它可以帮助开发人员在实现时更加清晰地了解数据的存储结构，同时也方便后续的数据库管理和维护工作。`

创建完成后是这样的：
![image.png](https://cdn.nlark.com/yuque/0/2023/png/21376908/1702352840475-faf7c39e-6a3e-4d72-872b-1de849baf668.png#averageHue=%23f0f0ef&clientId=u0cd9c8dc-062f-4&from=paste&height=331&id=u2e5d668a&originHeight=331&originWidth=843&originalType=binary&ratio=1&rotation=0&showTitle=false&size=35414&status=done&style=none&taskId=u6d34e397-b10c-4c92-8e2e-82c926f7d40&title=&width=843)
注意：右侧的小格子是可以放大和缩小的。看着像是很大的一张网。在每个格子当中可以容纳多个表。并且在这张网上可以清晰的看到表与表的关系。（一对多，一对一，多对多等。）

记得保存，ctrl+s保存时会生成一个xxx.pdm文件，以后如果要修改设计，双击这个xxx.pdm文件即可打开，进行编辑：
![image.png](https://cdn.nlark.com/yuque/0/2023/png/21376908/1702353117948-32a0da6b-393c-4282-a2b0-d2e893d7d04b.png#averageHue=%23f4f3f1&clientId=u0cd9c8dc-062f-4&from=paste&height=423&id=u33b947b9&originHeight=423&originWidth=553&originalType=binary&ratio=1&rotation=0&showTitle=false&size=29718&status=done&style=none&taskId=uc05f19a2-26bf-4720-bd21-db4d30c3125&title=&width=553)
保存后的文件：
![image.png](https://cdn.nlark.com/yuque/0/2023/png/21376908/1702353151163-22027c70-a1cc-463a-835e-30b23631ddf6.png#averageHue=%23383c95&clientId=u0cd9c8dc-062f-4&from=paste&height=88&id=u81c8d25f&originHeight=88&originWidth=82&originalType=binary&ratio=1&rotation=0&showTitle=false&size=5944&status=done&style=none&taskId=u69e2e523-6384-4974-9bd9-b39ceed8c0d&title=&width=82)

开始进行表的设计，这里不搞那么复杂，先创建一张表即可：t_user，用户表：
![image.png](https://cdn.nlark.com/yuque/0/2023/png/21376908/1702353507900-d3538143-07a6-4a08-b69e-4d7c23f1d6e3.png#averageHue=%23e4ded3&clientId=u0cd9c8dc-062f-4&from=paste&height=292&id=uc0708eab&originHeight=292&originWidth=580&originalType=binary&ratio=1&rotation=0&showTitle=false&size=21497&status=done&style=none&taskId=u37987bcd-cc58-4272-9158-47add73ca55&title=&width=580)

双击后，弹出设计窗口：
![image.png](https://cdn.nlark.com/yuque/0/2023/png/21376908/1702353664176-dbbccc05-2711-4e31-b6fc-4cf6238bacea.png#averageHue=%23f6f5f5&clientId=u0cd9c8dc-062f-4&from=paste&height=593&id=ucdbe63e9&originHeight=593&originWidth=1093&originalType=binary&ratio=1&rotation=0&showTitle=false&size=33708&status=done&style=shadow&taskId=u5d1fdc0d-9fda-4133-a7da-91b18ffb6d6&title=&width=1093)

设计表名：
![image.png](https://cdn.nlark.com/yuque/0/2023/png/21376908/1702354144428-887e8efb-c136-42e4-90de-4ec26815ab6f.png#averageHue=%23f5f5f4&clientId=u0cd9c8dc-062f-4&from=paste&height=445&id=ufd3ac07c&originHeight=445&originWidth=1068&originalType=binary&ratio=1&rotation=0&showTitle=false&size=22473&status=done&style=none&taskId=u0fd54ac3-7fba-48bf-87d0-6eb844decba&title=&width=1068)
注意：

1. Name：用来设置显示的表名
2. Code：用来设置数据库中真实创建的表名
3. Comment：对表的注释说明

设计字段：
![image.png](https://cdn.nlark.com/yuque/0/2023/png/21376908/1702356255883-27bed5c1-8cb5-41ed-ac06-d2a479327a93.png#averageHue=%23eceaea&clientId=u0cd9c8dc-062f-4&from=paste&height=726&id=ud50f83d4&originHeight=726&originWidth=1171&originalType=binary&ratio=1&rotation=0&showTitle=false&size=90439&status=done&style=shadow&taskId=u48387018-6792-4aa3-89c4-5fc6b175d4e&title=&width=1171)
把每个字段设计好，包括：字段名，数据类型，长度，约束等。

设计完成后：
![image.png](https://cdn.nlark.com/yuque/0/2023/png/21376908/1702356365447-df18d670-da99-40f0-b80f-95918bdf20f6.png#averageHue=%23dee8f2&clientId=u0cd9c8dc-062f-4&from=paste&height=189&id=u223a5402&originHeight=189&originWidth=348&originalType=binary&ratio=1&rotation=0&showTitle=false&size=10585&status=done&style=none&taskId=u6394b4c2-2385-400d-9a4a-b5ad2483556&title=&width=348)

## 使用PowerDesigner导出建表语句
![image.png](https://cdn.nlark.com/yuque/0/2023/png/21376908/1702356449130-0ab2e139-0029-4db4-a89d-c4d46ca800e4.png#averageHue=%23f5f4f4&clientId=u0cd9c8dc-062f-4&from=paste&height=663&id=u93450af9&originHeight=663&originWidth=1088&originalType=binary&ratio=1&rotation=0&showTitle=false&size=49050&status=done&style=shadow&taskId=u551f93ed-f4ad-4e51-b667-2fc25c38dbd&title=&width=1088)

```sql
drop table if exists t_user;

/*==============================================================*/
/* Table: t_user                                                */
/*==============================================================*/
create table t_user
(
   id                   bigint not null comment '用户的唯一标识',
   name                 varchar(255) not null,
   password             varchar(255) not null,
   realname             varchar(255),
   gender               char(2),
   tel                  char(11),
   primary key (id)
);

alter table t_user comment '用户表存储用户信息。';

```

