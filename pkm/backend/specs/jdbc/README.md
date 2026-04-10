# JDBC

> 动力节点老韩JDBC： <https://www.bilibili.com/video/BV1SXiEBxEHn>
> 对应资料： <https://pan.quark.cn/s/76ed0271ff3f>

* [hsp-jdbc](notes/hsp-jdbc.md)
* [JDBC概述](notes/overview.md)
    * JDBC基础概念
    * 模拟JDBC接口
    * 配置CLASSPATH
* [JDBC的新增修改删除](notes/crud1.md)
    * 步骤详解：执行注册驱动、获取连接、获取数据库操作对象、执行sql语句、释放资源
    * 以上步骤的其他改进与优化
* [JDBC的查询](notescrud2.md)
    * 查询；获取插入数据的主键值；获取元信息等等
* [SQL注入](notes/injection.md)
    * SQL注入
    * PreparedStatement
    * 批处理
* [JDBC事务](notes/transaction.md)
    * 事务（就三行主要的代码）
    * 隔离级别（主要就一行代码）
* [JDBC调用存储过程](notes/procedure.md)
    * （使用较少）
* [DAO](notes/dao.md)
    * （其实dao就是mapper）
* [JDBC连接池](notes/pools.md)
    * 连接池概念
    * Druid
    * HikariCP