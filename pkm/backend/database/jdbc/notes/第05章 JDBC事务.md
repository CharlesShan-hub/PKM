![](https://cdn.nlark.com/yuque/0/2023/jpeg/21376908/1692002570088-3338946f-42b3-4174-8910-7e749c31e950.jpeg#averageHue=%23f9f8f8&from=url&id=O8j9i&originHeight=78&originWidth=1400&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=shadow&title=)
# 什么是事务
事务是一个完整的业务，在这个业务中需要多条DML语句共同联合才能完成，而事务可以保证多条DML语句同时成功或者同时失败，从而保证数据的安全。例如A账户向B账户转账一万，A账户减去一万(update)和B账户加上一万(update)，必须同时成功或者同时失败，才能保证数据是正确的。

另请参见老杜发布的2024版MySQL教学视频。在本套教程中详细讲解了数据库事务机制。
![image.png](https://cdn.nlark.com/yuque/0/2024/png/21376908/1712894899237-1fa7df77-5280-4f8c-a5a4-6871f3da1cd7.png#averageHue=%23e5e9ec&clientId=ue29f8164-f6f8-4&from=paste&height=343&id=u9b97baef&originHeight=343&originWidth=329&originalType=binary&ratio=1&rotation=0&showTitle=false&size=24858&status=done&style=none&taskId=u934375cb-bdd7-4482-a28e-b9b34241ef0&title=&width=329)
![image.png](https://cdn.nlark.com/yuque/0/2024/png/21376908/1712903200531-94b35a50-694e-4295-a8db-23edcee137c9.png#averageHue=%23dee3e7&clientId=ue29f8164-f6f8-4&from=paste&height=101&id=udbdb240f&originHeight=101&originWidth=298&originalType=binary&ratio=1&rotation=0&showTitle=false&size=8273&status=done&style=none&taskId=ua916b075-e34b-4f2b-bfa3-157432983bc&title=&width=298)

![](https://cdn.nlark.com/yuque/0/2023/jpeg/21376908/1692002570088-3338946f-42b3-4174-8910-7e749c31e950.jpeg#averageHue=%23f9f8f8&from=url&id=qxrS1&originHeight=78&originWidth=1400&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=shadow&title=)
# 使用转账案例演示事务
## 表和数据的准备
t_act表：
![image.png](https://cdn.nlark.com/yuque/0/2024/png/21376908/1712906363176-935497e0-164e-4dd7-9c0d-a461fec09668.png#averageHue=%23f3f1ef&clientId=u97001951-01ca-4&from=paste&height=162&id=u10ee4509&originHeight=162&originWidth=708&originalType=binary&ratio=1&rotation=0&showTitle=false&size=14804&status=done&style=shadow&taskId=udbf1b96a-bdb2-4fe5-b063-fcb0ac2fe9c&title=&width=708)
![image.png](https://cdn.nlark.com/yuque/0/2024/png/21376908/1712906313124-77170d5b-9a14-4973-a063-2404228e0c60.png#averageHue=%23d2a868&clientId=u97001951-01ca-4&from=paste&height=90&id=u3af1ccf6&originHeight=90&originWidth=216&originalType=binary&ratio=1&rotation=0&showTitle=false&size=2558&status=done&style=shadow&taskId=ubd814fdf-4d6f-4ab9-9f29-289e6cd48d4&title=&width=216)

![](https://cdn.nlark.com/yuque/0/2023/jpeg/21376908/1692002570088-3338946f-42b3-4174-8910-7e749c31e950.jpeg#averageHue=%23f9f8f8&from=url&id=jDh6I&originHeight=78&originWidth=1400&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=shadow&title=)
## 实现转账功能
```java
package com.powernode.jdbc;

import com.powernode.jdbc.utils.DbUtils;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.SQLException;

/**
 * ClassName: JDBCTest19
 * Description: 实现账户转账
 * Datetime: 2024/4/12 15:20
 * Author: 老杜@动力节点
 * Version: 1.0
 */
public class JDBCTest19 {
    public static void main(String[] args) {
        // 转账金额
        double money = 10000.0;

        Connection conn = null;
        PreparedStatement ps1 = null;
        PreparedStatement ps2 = null;
        try {
            conn = DbUtils.getConnection();

            // 更新 act-001 账户
            String sql1 = "update t_act set balance = balance - ? where actno = ?";
            ps1 = conn.prepareStatement(sql1);
            ps1.setDouble(1, money);
            ps1.setString(2, "act-001");
            int count1 = ps1.executeUpdate();

            // 更新 act-002账户
            String sql2 = "update t_act set balance = balance + ? where actno = ?";
            ps2 = conn.prepareStatement(sql2);
            ps2.setDouble(1, money);
            ps2.setString(2, "act-002");
            int count2 = ps2.executeUpdate();

        } catch (SQLException e) {
            throw new RuntimeException(e);
        } finally {
            DbUtils.close(null, ps1, null);
            DbUtils.close(conn, ps1, null);
        }

    }
}

```
执行结果：
![image.png](https://cdn.nlark.com/yuque/0/2024/png/21376908/1712911942800-db916080-94e4-4b32-be09-ce7b4b21287d.png#averageHue=%23d2a664&clientId=u97001951-01ca-4&from=paste&height=86&id=u2d4983d9&originHeight=86&originWidth=199&originalType=binary&ratio=1&rotation=0&showTitle=false&size=2553&status=done&style=shadow&taskId=u02304cce-ffe2-4af8-92c6-e492cec7476&title=&width=199)

![](https://cdn.nlark.com/yuque/0/2023/jpeg/21376908/1692002570088-3338946f-42b3-4174-8910-7e749c31e950.jpeg#averageHue=%23f9f8f8&from=url&id=fHdee&originHeight=78&originWidth=1400&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=shadow&title=)
## JDBC事务默认是自动提交的
JDBC事务默认情况下是自动提交的，所谓的自动提交是指：只要执行一条DML语句则自动提交一次。测试一下，在以下代码位置添加断点：
![image.png](https://cdn.nlark.com/yuque/0/2024/png/21376908/1712912172123-b229ef63-3755-4993-84f4-2e303874c710.png#averageHue=%23312f2d&clientId=u97001951-01ca-4&from=paste&height=373&id=u573a3f7b&originHeight=373&originWidth=957&originalType=binary&ratio=1&rotation=0&showTitle=false&size=59857&status=done&style=none&taskId=u17724b8f-dfd5-4e9f-a6f8-0a386f0d45b&title=&width=957)
让代码执行到断点处：
![image.png](https://cdn.nlark.com/yuque/0/2024/png/21376908/1712912197579-f0e09df6-2183-4ace-addf-a2c7d3d9c5f7.png#averageHue=%23302f2d&clientId=u97001951-01ca-4&from=paste&height=290&id=u02cfda53&originHeight=290&originWidth=966&originalType=binary&ratio=1&rotation=0&showTitle=false&size=57805&status=done&style=none&taskId=u9df5ba14-964d-42cd-b50c-811a21a75d6&title=&width=966)
让程序停在此处，看看数据库表中的数据是否发生变化：
![image.png](https://cdn.nlark.com/yuque/0/2024/png/21376908/1712912226628-a32ded77-a2fe-4788-b5b5-3e2083b0926e.png#averageHue=%23d3a766&clientId=u97001951-01ca-4&from=paste&height=89&id=u673ed043&originHeight=89&originWidth=226&originalType=binary&ratio=1&rotation=0&showTitle=false&size=2614&status=done&style=none&taskId=ub49a46a4-439d-4766-ac4e-b856a169476&title=&width=226)
可以看到，整个转账的业务还没有执行完毕，act-001 账户的余额已经被修改为 30000了，为什么修改为 30000了，因为JDBC事务默认情况下是自动提交，只要执行一条DML语句则自动提交一次。这种自动提交是极其危险的。如果在此时程序发生了异常，act-002账户的余额未成功更新，则钱会丢失一万。我们可以测试一下：测试前先将数据恢复到起初的时候
![image.png](https://cdn.nlark.com/yuque/0/2024/png/21376908/1712912419988-1a2030f1-6603-47a8-9d25-224f767322ea.png#averageHue=%23e4cd91&clientId=u97001951-01ca-4&from=paste&height=66&id=u315a789b&originHeight=66&originWidth=220&originalType=binary&ratio=1&rotation=0&showTitle=false&size=2453&status=done&style=shadow&taskId=u689e596d-44f7-4cd1-8a17-09505c1a74c&title=&width=220)
在以下代码位置，让其发生异常：
![image.png](https://cdn.nlark.com/yuque/0/2024/png/21376908/1712912470809-0f61ba45-3562-4531-8fa9-d1d5efba0b81.png#averageHue=%23302f2c&clientId=u97001951-01ca-4&from=paste&height=439&id=u3bd9f666&originHeight=439&originWidth=840&originalType=binary&ratio=1&rotation=0&showTitle=false&size=63429&status=done&style=none&taskId=u60a55628-103d-4326-a67b-ffaf8b4a37c&title=&width=840)
执行结果如下：
![image.png](https://cdn.nlark.com/yuque/0/2024/png/21376908/1712912493027-d440b333-56ea-4995-935f-fd45355d8750.png#averageHue=%23322d2c&clientId=u97001951-01ca-4&from=paste&height=78&id=uc1d9654f&originHeight=78&originWidth=1298&originalType=binary&ratio=1&rotation=0&showTitle=false&size=18800&status=done&style=none&taskId=u0a612972-bba6-4f53-8491-4e4080fe61a&title=&width=1298)
![image.png](https://cdn.nlark.com/yuque/0/2024/png/21376908/1712912515925-d895e1d5-14c1-4858-8fe0-eab02faa8100.png#averageHue=%23d3ac6d&clientId=u97001951-01ca-4&from=paste&height=80&id=uda3f3356&originHeight=80&originWidth=217&originalType=binary&ratio=1&rotation=0&showTitle=false&size=2500&status=done&style=none&taskId=ue40ea47f-e486-4281-8655-0de79757e1a&title=&width=217)
经过测试得知，丢失了一万元。

![](https://cdn.nlark.com/yuque/0/2023/jpeg/21376908/1692002570088-3338946f-42b3-4174-8910-7e749c31e950.jpeg#averageHue=%23f9f8f8&from=url&id=pDSoJ&originHeight=78&originWidth=1400&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=shadow&title=)
## 添加事务控制
如何解决以上问题，分三步：
第一步：将JDBC事务的自动提交机制修改为手动提交（即开启事务）
```java
conn.setAutoCommit(false);
```
第二步：当整个业务完整结束后，手动提交事务（即提交事务，事务结束）
```java
conn.commit();
```
第三步：在处理业务过程中，如果发生异常，则进入catch语句块进行异常处理，手动回滚事务（即回滚事务，事务结束）
```java
conn.rollback();
```

代码如下：
```java
public class JDBCTest19 {
    public static void main(String[] args) {
        // 转账金额
        double money = 10000.0;

        Connection conn = null;
        PreparedStatement ps1 = null;
        PreparedStatement ps2 = null;
        try {
            conn = DbUtils.getConnection();
            
            // 开启事务（关闭自动提交机制）
            conn.setAutoCommit(false);

            // 更新 act-001 账户
            String sql1 = "update t_act set balance = balance - ? where actno = ?";
            ps1 = conn.prepareStatement(sql1);
            ps1.setDouble(1, money);
            ps1.setString(2, "act-001");
            int count1 = ps1.executeUpdate();

            String s = null;
            s.toString();

            // 更新 act-002账户
            String sql2 = "update t_act set balance = balance + ? where actno = ?";
            ps2 = conn.prepareStatement(sql2);
            ps2.setDouble(1, money);
            ps2.setString(2, "act-002");
            int count2 = ps2.executeUpdate();
            
            // 提交事务
            conn.commit();

        } catch (Exception e) {
            // 遇到异常回滚事务
            try {
                conn.rollback();
            } catch (SQLException ex) {
                throw new RuntimeException(ex);
            }
            throw new RuntimeException(e);
        } finally {
            DbUtils.close(null, ps1, null);
            DbUtils.close(conn, ps1, null);
        }

    }
}
```

将数据恢复如初：
![image.png](https://cdn.nlark.com/yuque/0/2024/png/21376908/1712913009901-fda0cf51-2d89-4aed-907c-92803e51370a.png#averageHue=%23e4cd91&clientId=u97001951-01ca-4&from=paste&height=67&id=ue9b4ea30&originHeight=67&originWidth=214&originalType=binary&ratio=1&rotation=0&showTitle=false&size=2451&status=done&style=none&taskId=u6166f100-beb6-4bf6-a902-c89810f708f&title=&width=214)
执行程序，仍然会出现异常：
![image.png](https://cdn.nlark.com/yuque/0/2024/png/21376908/1712913037024-0052d9be-b8d1-4999-8449-8e574ff77b7b.png#averageHue=%23332d2c&clientId=u97001951-01ca-4&from=paste&height=125&id=u06ce920e&originHeight=125&originWidth=1588&originalType=binary&ratio=1&rotation=0&showTitle=false&size=36811&status=done&style=none&taskId=ud1dac9aa-e898-49ee-ac1c-baaaa07a47a&title=&width=1588)
但是数据库表中的数据是安全的：
![image.png](https://cdn.nlark.com/yuque/0/2024/png/21376908/1712913054649-53befbcc-2748-433c-9f27-6c2dca4a1bd6.png#averageHue=%23d3ac6e&clientId=u97001951-01ca-4&from=paste&height=79&id=u7f62bbd8&originHeight=79&originWidth=221&originalType=binary&ratio=1&rotation=0&showTitle=false&size=2524&status=done&style=none&taskId=u08b27fbc-4242-4975-a808-915f75e0f8a&title=&width=221)
当程序不出现异常时：
![image.png](https://cdn.nlark.com/yuque/0/2024/png/21376908/1712913078723-158ff1de-43b9-4ae0-b1c5-68dc011ec2c7.png#averageHue=%232f2e2d&clientId=u97001951-01ca-4&from=paste&height=130&id=u253e2ea4&originHeight=130&originWidth=545&originalType=binary&ratio=1&rotation=0&showTitle=false&size=10501&status=done&style=none&taskId=u7dbd8a8c-de19-4fcc-b76f-f46e22d3aa4&title=&width=545)
数据库表中的数据也是正确的：
![image.png](https://cdn.nlark.com/yuque/0/2024/png/21376908/1712913097670-fd86b9a8-dab3-4bab-b5b5-ccfff28e1cba.png#averageHue=%23d5af70&clientId=u97001951-01ca-4&from=paste&height=99&id=ud6fe728c&originHeight=99&originWidth=201&originalType=binary&ratio=1&rotation=0&showTitle=false&size=3862&status=done&style=none&taskId=u8b00c2e2-226c-45e2-8384-f91f1132a53&title=&width=201)
这样就采用了JDBC事务解决了数据安全的问题。

![](https://cdn.nlark.com/yuque/0/2023/jpeg/21376908/1692002570088-3338946f-42b3-4174-8910-7e749c31e950.jpeg#averageHue=%23f9f8f8&from=url&id=nEZmX&originHeight=78&originWidth=1400&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=shadow&title=)
# 设置JDBC事务隔离级别
关于事务隔离级别相关内容另请参见：老杜发布的2024版MySQL教程。
设置事务的隔离级别也是比较重要的，在JDBC程序中应该如何设置事务的隔离级别呢？代码如下：
```java
public class JDBCTest20 {
    public static void main(String[] args) {
        Connection conn = null;
        try {
            conn = DbUtils.getConnection();
            conn.setTransactionIsolation(Connection.TRANSACTION_SERIALIZABLE);
        } catch (SQLException e) {
            throw new RuntimeException(e);
        } finally {
            DbUtils.close(conn, null, null);
        }
    }
}
```
![](https://cdn.nlark.com/yuque/0/2023/jpeg/21376908/1692002570088-3338946f-42b3-4174-8910-7e749c31e950.jpeg#averageHue=%23f9f8f8&from=url&id=mPMWn&originHeight=78&originWidth=1400&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=shadow&title=)
