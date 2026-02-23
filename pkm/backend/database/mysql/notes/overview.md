# 数据库概述

---
## 什么是数据库

- 数据库是长期存储在计算机内、有组织、可共享、统一管理的大量数据的集合。
- 数据库按照特定规则组织数据，以提高查询效率。
- 数据库对应的英文单词是DataBase，简称DB。

---
## 数据库类型

- 关系型数据库
	- 基于关系模型（二维表）组织数据，能清晰表达一对一、一对多、多对多等关系。
	- 关系模型包括数据结构（数据存储的问题，二维表）、操作指令集合（SQL语句）、完整性约束(表内数据约束、表与表之间的约束)。
- 非关系型数据库（NoSQL）
	- NoSQL，泛指非关系型的数据库。随着互联网web2.0网站的兴起，传统的关系数据库在处理web2.0网站，特别是超大规模和高并发的SNS类型的web2.0纯动态网站已经显得力不从心。
	- NoSQL最常见的解释是“non-relational”， “Not Only SQL”也被很多人接受。
	- NoSQL仅仅是一个概念，泛指非关系型的数据库，区别于关系数据库，它们不保证关系数据的ACID特性。
	- 特点：易扩展、大数据量下高性能、数据模型灵活。

---
## 数据库管理系统

- 数据库管理系统（Database Management System，简称DBMS）是为管理数据库而设计的电脑软件系统，一般具有存储、截取、安全保障、备份等基础功能。
- 数据库管理系统是数据库系统的核心组成部分，主要完成对数据库的操作与管理功能，实现数据库对象的创建、数据库存储数据的查询、添加、修改与删除操作和数据库的用户管理、权限管理等。
- 常见的数据库管理系统有：MySQL、Oracle、DB2、MS SQL Server、SQLite、PostgreSQL、Sybase等。
	- 目前 MySQL 已经被 Oracle 收购。

---
## 什么是SQL

- **结构化查询语言**（Structured Query Language）简称SQL，是一种特殊目的的编程语言，是一种数据库查询和程序设计语言，用于存取数据以及查询、更新和管理关系数据库系统。
- 结构化查询语言是高级的非过程化编程语言，允许用户在高层数据结构上工作。它不要求用户指定对数据的存放方法，也不需要用户了解具体的数据存放方式，所以具有完全不同底层结构的不同数据库系统, 可以使用相同的结构化查询语言作为数据输入与管理的接口。结构化查询语言语句可以嵌套，这使它具有极大的灵活性和强大的功能。
- SQL的分类（DDL表、DQL查、DML改、DCL控制、TPL事物、CCL指针）
   - DQL（SELECT）
      - 数据查询语言（Data **Query** Language, DQL）是SQL语言中，负责进行数据查询而不会对数据本身进行修改的语句，这是最基本的SQL语句。保留字**SELECT**是DQL（也是所有SQL）用得最多的动词，其他DQL常用的保留字有FROM，WHERE，GROUP BY，HAVING和ORDER BY。这些DQL保留字常与其他类型的SQL语句一起使用。
   - DDL（修改表结构）
      - 数据定义语言 (Data **Definition** Language, DDL) 是SQL语言集中，负责数据结构定义与数据库对象定义的语言，由CREATE、ALTER与DROP三个语法所组成，最早是由 Codasyl (Conference on Data Systems Languages) 数据模型开始，现在被纳入 SQL 指令中作为其中一个子集。
   - DML（修改表数据）
      - 数据操纵语言（Data **Manipulation** Language, DML）是SQL语言中，负责对数据库对象运行数据访问工作的指令集，以INSERT、UPDATE、DELETE三种指令为核心，分别代表插入、更新与删除。
   - DCL
      - 数据控制语言 (Data **Control** Language) 在SQL语言中，是一种可对数据访问权进行控制的指令，它可以控制特定用户账户对数据表、查看表、预存程序、用户自定义函数等数据库对象的控制权。由 GRANT 和 REVOKE 两个指令组成。DCL以控制用户的访问权限为主，GRANT为授权语句，对应的REVOKE是撤销授权语句。
   - TPL
      - 数据事务管理语言（Transaction Processing Language）它的语句能确保被DML语句影响的表的所有行及时得以更新。TPL语句包括BEGIN TRANSACTION，COMMIT和ROLLBACK。
   - CCL
      - 指针控制语言（Cursor Control Language），它的语句，像DECLARE CURSOR，FETCH INTO和UPDATE WHERE CURRENT用于对一个或多个表单独行的操作。
- DBMS、SQL、DB之间的关系
	- DBMS通过执行SQL来操作DB中的数据。

## 数据库客户端工具

* DBeaver
* navicat：我喜欢用这个，比较权威
	* 可以去这里下载： https://www.macwk.com/
* SQLyog: 字体可以放大，老韩推荐
* [client](../details/client.md)