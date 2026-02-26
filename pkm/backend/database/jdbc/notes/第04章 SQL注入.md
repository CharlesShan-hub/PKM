![](https://cdn.nlark.com/yuque/0/2023/jpeg/21376908/1692002570088-3338946f-42b3-4174-8910-7e749c31e950.jpeg#averageHue=%23f9f8f8&from=url&id=O8j9i&originHeight=78&originWidth=1400&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=shadow&title=)
# SQL注入问题
SQL注入问题说的是：用户输入的信息中含有SQL语句关键字，和程序中的SQL语句进行字符串拼接，导致程序中的SQL语句改变了原意。（SQL注入问题是一种系统安全问题）
接下来我们来演示一下SQL注入问题。以用户登录为例。使用表：t_user
业务描述：系统启动后，给出登录页面，用户可以输入用户名和密码，用户名和密码全部正确，则登录成功，反之，则登录失败。
分析一下要执行怎样的SQL语句？是不是这样的？

```sql
select * from t_user where name = 用户输入的用户名 and password = 用户输入的密码;
```
如果以上的SQL语句能够查询到结果，说明用户名和密码是正确的，则登录成功。如果查不到，说明是错误的，则登录失败。
代码实现如下：
```java
package com.powernode.jdbc;

import java.sql.*;
import java.util.ResourceBundle;
import java.util.Scanner;

/**
 * 用户登录案例演示SQL注入问题
 */
public class JDBCTest02 {
    public static void main(String[] args) {
        // 输出欢迎页面
        System.out.println("欢迎使用用户管理系统，请登录！");
        // 接收用户名和密码
        Scanner scanner = new Scanner(System.in);
        System.out.print("用户名：");
        String loginName = scanner.nextLine();
        System.out.print("密码：");
        String loginPwd = scanner.nextLine();
        // 读取属性配置文件，获取连接数据库的信息。
        ResourceBundle bundle = ResourceBundle.getBundle("com.powernode.jdbc.jdbc");
        String driver = bundle.getString("driver");
        String url = bundle.getString("url");
        String user = bundle.getString("user");
        String password = bundle.getString("password");
        // JDBC程序验证用户名和密码是否正确
        Connection conn = null;
        Statement stmt = null;
        ResultSet rs = null;
        try {
            // 1.注册驱动
            Class.forName(driver);
            // 2.获取连接
            conn = DriverManager.getConnection(url, user, password);
            // 3.获取数据库操作对象
            stmt = conn.createStatement();
            // 4.执行SQL语句
            String sql = "select realname from t_user where name = '"+loginName+"' and password = '"+loginPwd+"'";
            rs = stmt.executeQuery(sql);
            // 5.处理查询结果集
            if (rs.next()) { // 如果可以确定结果集中最多只有一条记录的话，可以使用if语句，不一定非要用while循环。
                String realname = rs.getString("realname");
                System.out.println("登录成功，欢迎您" + realname);
            } else {
                System.out.println("登录失败，用户名不存在或者密码错误。");
            }
        } catch (ClassNotFoundException | SQLException e) {
            throw new RuntimeException(e);
        } finally {
            // 6.释放资源
            if (rs != null) {
                try {
                    rs.close();
                } catch (SQLException e) {
                    throw new RuntimeException(e);
                }
            }
            if (stmt != null) {
                try {
                    stmt.close();
                } catch (SQLException e) {
                    throw new RuntimeException(e);
                }
            }
            if (conn != null) {
                try {
                    conn.close();
                } catch (SQLException e) {
                    throw new RuntimeException(e);
                }
            }
        }
    }
}

```

如果用户名和密码正确的话，执行结果如下：
![image.png](https://cdn.nlark.com/yuque/0/2023/png/21376908/1702976483919-52a9ff26-1ded-4a07-bcc8-d2846f17a045.png#averageHue=%231f2126&clientId=u156f6b41-7663-4&from=paste&height=141&id=ub10f6c60&originHeight=141&originWidth=362&originalType=binary&ratio=1&rotation=0&showTitle=false&size=13354&status=done&style=none&taskId=u7106c062-d627-45bf-801f-95ca72438bb&title=&width=362)

如果用户名不存在或者密码错误的话，执行结果如下：
![image.png](https://cdn.nlark.com/yuque/0/2023/png/21376908/1702976532157-a3d29aad-a0e8-44c9-9571-63cc3052fe5b.png#averageHue=%23202327&clientId=u156f6b41-7663-4&from=paste&height=125&id=udffad2a4&originHeight=125&originWidth=357&originalType=binary&ratio=1&rotation=0&showTitle=false&size=15356&status=done&style=none&taskId=uf2850b49-75b0-40b5-a3b3-ea7386b756d&title=&width=357)

接下来，见证奇迹的时刻，当我分别输入以下的用户名和密码时，系统被攻破了：
![image.png](https://cdn.nlark.com/yuque/0/2023/png/21376908/1702976830213-7483fb5c-6c7c-466c-b7c4-a2feb26b12bb.png#averageHue=%23202226&clientId=u156f6b41-7663-4&from=paste&height=134&id=u347825d4&originHeight=134&originWidth=325&originalType=binary&ratio=1&rotation=0&showTitle=false&size=11860&status=done&style=none&taskId=u8826f589-046f-4233-af61-95d1c099bf2&title=&width=325)
这种现象就叫做：SQL注入。为什么会发生以上的事儿呢？原因是：用户提供的信息中有SQL语句关键字，并且和底层的SQL字符串进行了拼接，变成了一个全新的SQL语句。
例如：本来程序想表达的是这样的SQL：
```sql
select realname from t_user where name = 'sunwukong' and password = '123';
```
结果被SQL注入之后，SQL语句就变成这样了：
```sql
select realname from t_user where name = 'aaa' and password = 'bbb' or '1'='1';
```
我们可以执行一下这条SQL，看看结果是什么？
![image.png](https://cdn.nlark.com/yuque/0/2023/png/21376908/1702977070115-c06f8f95-d42f-43e7-9b69-53eac3b155b2.png#averageHue=%23f0efee&clientId=u156f6b41-7663-4&from=paste&height=171&id=ue79d55bc&originHeight=171&originWidth=144&originalType=binary&ratio=1&rotation=0&showTitle=false&size=3817&status=done&style=shadow&taskId=u33810237-dd0a-4fa9-9aef-067015aad10&title=&width=144)
把所有结果全部查到了，这是因为 '1'='1' 是恒成立的，并且使用的是 or 运算符，所以 or 前面的条件等于是没有的。这样就会把所有数据全部查到。而在程序中的判断逻辑是只要结果集中有数据，则表示登录成功。所以以上的输入方式最终的结果就是登录成功。你设想一下，如果这个系统是一个高级别保密系统，只有登录成功的人才有权限，那么这个系统是不是极其危险了。

![](https://cdn.nlark.com/yuque/0/2023/jpeg/21376908/1692002570088-3338946f-42b3-4174-8910-7e749c31e950.jpeg#averageHue=%23f9f8f8&from=url&id=b1eb1&originHeight=78&originWidth=1400&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=shadow&title=)
# 解决SQL注入问题
导致SQL注入的根本原因是什么？只有找到真正的原因，问题才能得到解决。

最根本的原因是：Statement造成的。

Statement执行原理是：先进行字符串的拼接，将拼接好的SQL语句发送给数据库服务器，数据库服务器进行SQL语句的编译，然后执行。因此用户提供的信息中如果含有SQL语句的关键字，那么这些关键字正好参加了SQL语句的编译，所以导致原SQL语句被扭曲。

因此，JDBC为了解决这个问题，引入了一个新的接口：PreparedStatement，我们称为：预编译的数据库操作对象。PreparedStatement是Statement接口的子接口。它俩是继承关系。

PreparedStatement执行原理是：先对SQL语句进行预先的编译，然后再向SQL语句指定的位置传值，也就是说：用户提供的信息中即使含有SQL语句的关键字，那么这个信息也只会被当做一个值传递给SQL语句，用户提供的信息不再参与SQL语句的编译了，这样就解决了SQL注入问题。

使用PreparedStatement解决SQL注入问题：
```java
package com.powernode.jdbc;

import java.sql.*;
import java.util.ResourceBundle;
import java.util.Scanner;

/**
 * PreparedStatement解决SQL注入问题
 */
public class JDBCTest03 {
    public static void main(String[] args) {
        // 输出欢迎页面
        System.out.println("欢迎使用用户管理系统，请登录！");
        // 接收用户名和密码
        Scanner scanner = new Scanner(System.in);
        System.out.print("用户名：");
        String loginName = scanner.nextLine();
        System.out.print("密码：");
        String loginPwd = scanner.nextLine();
        // 读取属性配置文件，获取连接数据库的信息。
        ResourceBundle bundle = ResourceBundle.getBundle("com.powernode.jdbc.jdbc");
        String driver = bundle.getString("driver");
        String url = bundle.getString("url");
        String user = bundle.getString("user");
        String password = bundle.getString("password");
        // JDBC程序验证用户名和密码是否正确
        Connection conn = null;
        PreparedStatement pstmt = null;
        ResultSet rs = null;
        try {
            // 1.注册驱动
            Class.forName(driver);
            // 2.获取连接
            conn = DriverManager.getConnection(url, user, password);
            // 3.获取数据库操作对象（获取的是预编译的数据库操作对象）
            String sql = "select realname from t_user where name=? and password=?";
            pstmt = conn.prepareStatement(sql);
            pstmt.setString(1, loginName);
            pstmt.setString(2, loginPwd);
            // 4.执行SQL语句
            rs = pstmt.executeQuery();
            // 5.处理查询结果集
            if (rs.next()) {
                String realname = rs.getString("realname");
                System.out.println("登录成功，欢迎您" + realname);
            } else {
                System.out.println("登录失败，用户名不存在或者密码错误。");
            }
        } catch (ClassNotFoundException | SQLException e) {
            throw new RuntimeException(e);
        } finally {
            // 6.释放资源
            if (rs != null) {
                try {
                    rs.close();
                } catch (SQLException e) {
                    throw new RuntimeException(e);
                }
            }
            if (pstmt != null) {
                try {
                    pstmt.close();
                } catch (SQLException e) {
                    throw new RuntimeException(e);
                }
            }
            if (conn != null) {
                try {
                    conn.close();
                } catch (SQLException e) {
                    throw new RuntimeException(e);
                }
            }
        }
    }
}

```

用户名和密码正确的话，执行结果如下：
![image.png](https://cdn.nlark.com/yuque/0/2023/png/21376908/1702978597923-7cce7d0a-6a79-43a5-b9f3-a8ce2e4785e6.png#averageHue=%23202226&clientId=u156f6b41-7663-4&from=paste&height=134&id=uf32095e8&originHeight=134&originWidth=324&originalType=binary&ratio=1&rotation=0&showTitle=false&size=13158&status=done&style=none&taskId=u994aaff2-25f2-447f-b015-c44013c610c&title=&width=324)

用户名和密码错误的话，执行结果如下：
![image.png](https://cdn.nlark.com/yuque/0/2023/png/21376908/1702978634050-b50580fc-f9ce-48ec-9200-425ea078782c.png#averageHue=%23202227&clientId=u156f6b41-7663-4&from=paste&height=136&id=u5810b10f&originHeight=136&originWidth=347&originalType=binary&ratio=1&rotation=0&showTitle=false&size=15416&status=done&style=none&taskId=u122f18ad-44c3-425f-aa33-e826821bb0f&title=&width=347)

尝试SQL注入，看看还能不能？
![image.png](https://cdn.nlark.com/yuque/0/2023/png/21376908/1702978663699-a5c38388-b4f5-43b6-8d00-3e56fdb77178.png#averageHue=%23202227&clientId=u156f6b41-7663-4&from=paste&height=136&id=u7ba6dcfc&originHeight=136&originWidth=349&originalType=binary&ratio=1&rotation=0&showTitle=false&size=13154&status=done&style=none&taskId=u88bcd970-8d9d-43b2-91ef-7affbe84c1b&title=&width=349)
通过测试得知，SQL注入问题已经解决了。**根本原因是：bbb' or '1'='1 这个字符串中虽然含有SQL语句的关键字，但是只会被当做普通的值传到SQL语句中，并没有参与SQL语句的编译**。

**关于使用PreparedStatement要注意的是：**

- 带有占位符 ? 的SQL语句我们称为：预处理SQL语句。
- 占位符 ? 不能使用单引号或双引号包裹。如果包裹，占位符则不再是占位符，是一个普通的问号字符。
- 在执行SQL语句前，必须给每一个占位符 ? 传值。
- 如何给占位符 ? 传值，通过以下的方法：
   - pstmt.setXxx(第几个占位符, 传什么值)
   - “第几个占位符”：从1开始。第1个占位符则是1，第2个占位符则是2，以此类推。
   - “传什么值”：具体要看调用的什么方法？
      - 如果调用pstmt.setString方法，则传的值必须是一个字符串。
      - 如果调用pstmt.setInt方法，则传的值必须是一个整数。
      - 以此类推......

**PreparedStatement和Statement都是用于执行SQL语句的接口，它们的主要区别在于：**

- PreparedStatement预编译SQL语句，Statement直接提交SQL语句；
- PreparedStatement执行速度更快，可以避免SQL注入攻击；(PreparedStatement对于同一条SQL语句来说，编译一次，执行N次。而Statement是每次都要进行编译的。因此PreparedStatement效率略微高一些。)
- PreparedStatement会做类型检查，是类型安全的；

![](https://cdn.nlark.com/yuque/0/2023/jpeg/21376908/1692002570088-3338946f-42b3-4174-8910-7e749c31e950.jpeg#averageHue=%23f9f8f8&from=url&id=ix3qZ&originHeight=78&originWidth=1400&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=shadow&title=)
# PreparedStatement的使用
## 新增操作
需求：向 emp 表中插入这样一条记录：
empno：8888
ename：张三
job：销售员
mgr：7369
hiredate：2024-01-01
sal：1000.0
comm：500.0
deptno：10
```java
package com.powernode.jdbc;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.SQLException;
import java.time.LocalDate;
import java.util.ResourceBundle;

public class JDBCTest04 {
    public static void main(String[] args) {

        ResourceBundle bundle = ResourceBundle.getBundle("com.powernode.jdbc.jdbc");
        String driver = bundle.getString("driver");
        String url = bundle.getString("url");
        String user = bundle.getString("user");
        String password = bundle.getString("password");

        Connection conn = null;
        PreparedStatement pstmt = null;
        try {
            // 1. 注册驱动
            Class.forName(driver);
            // 2. 获取连接
            conn = DriverManager.getConnection(url, user, password);
            // 3. 获取预编译的数据操作对象
            String sql = "insert into emp(empno,ename,sal,comm,job,mgr,hiredate,deptno) values(?,?,?,?,?,?,?,?)";
            // 预编译SQL语句
            pstmt = conn.prepareStatement(sql);
            // 给 ? 传值
            pstmt.setInt(1, 8888);
            pstmt.setString(2, "张三");
            pstmt.setDouble(3, 10000.0);
            pstmt.setDouble(4, 500.0);
            pstmt.setString(5, "销售员");
            pstmt.setInt(6, 7369);
            LocalDate localDate = LocalDate.parse("2024-01-01");
            pstmt.setDate(7, java.sql.Date.valueOf(localDate));
            pstmt.setInt(8, 10);
            // 4. 执行SQL语句
            int count = pstmt.executeUpdate();
            if (1 == count) {
                System.out.println("成功更新" + count + "条记录");
            }
        } catch (Exception e) {
            e.printStackTrace();
        } finally {
            // 6. 释放资源
            if (pstmt != null) {
                try {
                    pstmt.close();
                } catch (SQLException e) {
                    throw new RuntimeException(e);
                }
            }
            if (conn != null) {
                try {
                    conn.close();
                } catch (SQLException e) {
                    throw new RuntimeException(e);
                }
            }
        }
    }
}
```
重点学习内容：如何给占位符 ? 传值。
执行结果如下：
![image.png](https://cdn.nlark.com/yuque/0/2024/png/21376908/1708238667879-fe0a662a-f9e8-4933-afd0-5290856c21fd.png#averageHue=%23f4eeeb&clientId=u12e62e1b-f7c7-4&from=paste&height=370&id=uef77b401&originHeight=370&originWidth=673&originalType=binary&ratio=1&rotation=0&showTitle=false&size=36467&status=done&style=none&taskId=uc7a3d803-b1e3-40ee-98ca-368bb593c98&title=&width=673)

![](https://cdn.nlark.com/yuque/0/2023/jpeg/21376908/1692002570088-3338946f-42b3-4174-8910-7e749c31e950.jpeg#averageHue=%23f9f8f8&from=url&id=X4tEj&originHeight=78&originWidth=1400&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=shadow&title=)
## 修改操作
需求：将员工编号为8888的员工，姓名修改为李四，岗位修改为产品经理，月薪修改为5000.0，其他不变。
```java
package com.powernode.jdbc;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.SQLException;
import java.time.LocalDate;
import java.util.ResourceBundle;

public class JDBCTest05 {
    public static void main(String[] args) {
        ResourceBundle bundle = ResourceBundle.getBundle("com.powernode.jdbc.jdbc");
        String driver = bundle.getString("driver");
        String url = bundle.getString("url");
        String user = bundle.getString("user");
        String password = bundle.getString("password");

        Connection conn = null;
        PreparedStatement pstmt = null;
        try {
            // 1. 注册驱动
            Class.forName(driver);
            // 2. 获取连接
            conn = DriverManager.getConnection(url, user, password);
            // 3. 获取预编译的数据操作对象
            String sql = "update emp set ename = ?, job = ?, sal = ? where empno = ?";
            // 预编译SQL语句
            pstmt = conn.prepareStatement(sql);
            // 给 ? 传值
            pstmt.setString(1, "李四");
            pstmt.setString(2, "产品经理");
            pstmt.setDouble(3, 5000.0);
            pstmt.setInt(4, 8888);
            // 4. 执行SQL语句
            int count = pstmt.executeUpdate();
            if (1 == count) {
                System.out.println("成功更新" + count + "条记录");
            }
        } catch (Exception e) {
            e.printStackTrace();
        } finally {
            // 6. 释放资源
            if (pstmt != null) {
                try {
                    pstmt.close();
                } catch (SQLException e) {
                    throw new RuntimeException(e);
                }
            }
            if (conn != null) {
                try {
                    conn.close();
                } catch (SQLException e) {
                    throw new RuntimeException(e);
                }
            }
        }
    }
}
```
执行结果如下：
![image.png](https://cdn.nlark.com/yuque/0/2024/png/21376908/1708239544671-626c918f-fd56-4cfa-8aa2-df1976979414.png#averageHue=%23f6f0ed&clientId=u12e62e1b-f7c7-4&from=paste&height=375&id=u7bfa3f92&originHeight=375&originWidth=675&originalType=binary&ratio=1&rotation=0&showTitle=false&size=36597&status=done&style=none&taskId=u16478375-ba9f-4cac-89e8-61688719844&title=&width=675)

![](https://cdn.nlark.com/yuque/0/2023/jpeg/21376908/1692002570088-3338946f-42b3-4174-8910-7e749c31e950.jpeg#averageHue=%23f9f8f8&from=url&id=yiZjS&originHeight=78&originWidth=1400&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=shadow&title=)
## 删除操作
需求：将员工编号为8888的删除。
```java
package com.powernode.jdbc;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.SQLException;
import java.util.ResourceBundle;

public class JDBCTest06 {
    public static void main(String[] args) {
        ResourceBundle bundle = ResourceBundle.getBundle("com.powernode.jdbc.jdbc");
        String driver = bundle.getString("driver");
        String url = bundle.getString("url");
        String user = bundle.getString("user");
        String password = bundle.getString("password");

        Connection conn = null;
        PreparedStatement pstmt = null;
        try {
            // 1. 注册驱动
            Class.forName(driver);
            // 2. 获取连接
            conn = DriverManager.getConnection(url, user, password);
            // 3. 获取预编译的数据操作对象
            String sql = "delete from emp where empno = ?";
            // 预编译SQL语句
            pstmt = conn.prepareStatement(sql);
            // 给 ? 传值
            pstmt.setInt(1, 8888);
            // 4. 执行SQL语句
            int count = pstmt.executeUpdate();
            if (1 == count) {
                System.out.println("成功更新" + count + "条记录");
            }
        } catch (Exception e) {
            e.printStackTrace();
        } finally {
            // 6. 释放资源
            if (pstmt != null) {
                try {
                    pstmt.close();
                } catch (SQLException e) {
                    throw new RuntimeException(e);
                }
            }
            if (conn != null) {
                try {
                    conn.close();
                } catch (SQLException e) {
                    throw new RuntimeException(e);
                }
            }
        }
    }
}

```
执行结果如下：
![image.png](https://cdn.nlark.com/yuque/0/2024/png/21376908/1708240126660-979bd865-6e83-41c7-9724-68c247209e9e.png#averageHue=%23d9ac6c&clientId=u12e62e1b-f7c7-4&from=paste&height=344&id=u8aa56fc6&originHeight=344&originWidth=658&originalType=binary&ratio=1&rotation=0&showTitle=false&size=33453&status=done&style=none&taskId=u5931a97b-d280-4586-abc4-aab041a7523&title=&width=658)

![](https://cdn.nlark.com/yuque/0/2023/jpeg/21376908/1692002570088-3338946f-42b3-4174-8910-7e749c31e950.jpeg#averageHue=%23f9f8f8&from=url&id=RDFvt&originHeight=78&originWidth=1400&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=shadow&title=)
## 模糊查询
需求：查询员工名字中第二个字母是 O 的。
```java
package com.powernode.jdbc;

import java.sql.*;
import java.util.ResourceBundle;

public class JDBCTest07 {
    public static void main(String[] args) {
        ResourceBundle bundle = ResourceBundle.getBundle("com.powernode.jdbc.jdbc");
        String driver = bundle.getString("driver");
        String url = bundle.getString("url");
        String user = bundle.getString("user");
        String password = bundle.getString("password");

        Connection conn = null;
        PreparedStatement pstmt = null;
        ResultSet rs = null;
        try {
            // 1. 注册驱动
            Class.forName(driver);
            // 2. 获取连接
            conn = DriverManager.getConnection(url, user, password);
            // 3. 获取预编译的数据操作对象
            String sql = "select ename from emp where ename like ?";
            // 预编译SQL语句
            pstmt = conn.prepareStatement(sql);
            // 给 ? 传值
            pstmt.setString(1, "_O%");
            // 4. 执行SQL语句
            rs = pstmt.executeQuery();
            // 5. 处理查询结果集
            while (rs.next()) {
                String ename = rs.getString("ename");
                System.out.println(ename);
            }
        } catch (Exception e) {
            e.printStackTrace();
        } finally {
            // 6. 释放资源
            if (rs != null) {
                try {
                    rs.close();
                } catch (SQLException e) {
                    throw new RuntimeException(e);
                }
            }
            if (pstmt != null) {
                try {
                    pstmt.close();
                } catch (SQLException e) {
                    throw new RuntimeException(e);
                }
            }
            if (conn != null) {
                try {
                    conn.close();
                } catch (SQLException e) {
                    throw new RuntimeException(e);
                }
            }
        }
    }
}
```
执行结果如下：
![image.png](https://cdn.nlark.com/yuque/0/2024/png/21376908/1708240400162-5eb57d8c-e52c-4780-9ec2-88f117377328.png#averageHue=%23fcfaf9&clientId=u12e62e1b-f7c7-4&from=paste&height=62&id=u2c407fa5&originHeight=62&originWidth=148&originalType=binary&ratio=1&rotation=0&showTitle=false&size=1908&status=done&style=shadow&taskId=u33a476d5-410d-4341-824c-3a9327ab37e&title=&width=148)
通过这个例子主要告诉大家，程序不能这样写：
```java
String sql = "select ename from emp where ename like '_?%'";
pstmt.setString(1, "O");
```
由于占位符 ? 被单引号包裹，因此这个占位符是无效的。

![](https://cdn.nlark.com/yuque/0/2023/jpeg/21376908/1692002570088-3338946f-42b3-4174-8910-7e749c31e950.jpeg#averageHue=%23f9f8f8&from=url&id=pU8Ea&originHeight=78&originWidth=1400&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=shadow&title=)
## 分页查询
对于MySQL来说，通用的分页SQL语句：
假设每页显示3条记录：pageSize = 3
第1页：limit 0, 3
第2页：limit 3, 3
第3页：limit 6, 3
**第pageNo页：limit (pageNo - 1)*pageSize, pageSize**
需求：查询所有员工姓名，每页显示3条(pageSize)，显示第2页(pageNo)。

```java
package com.powernode.jdbc;

import java.sql.*;
import java.util.ResourceBundle;

public class JDBCTest08 {
    public static void main(String[] args) {
        ResourceBundle bundle = ResourceBundle.getBundle("com.powernode.jdbc.jdbc");
        String driver = bundle.getString("driver");
        String url = bundle.getString("url");
        String user = bundle.getString("user");
        String password = bundle.getString("password");

        Connection conn = null;
        PreparedStatement pstmt = null;
        ResultSet rs = null;

        // 每页显示记录条数
        int pageSize = 3;
        // 显示第几页
        int pageNo = 2;

        try {
            // 1. 注册驱动
            Class.forName(driver);
            // 2. 获取连接
            conn = DriverManager.getConnection(url, user, password);
            // 3. 获取预编译的数据操作对象
            String sql = "select ename from emp limit ?, ?";
            // 预编译SQL语句
            pstmt = conn.prepareStatement(sql);
            // 给 ? 传值
            pstmt.setInt(1, (pageNo - 1) * pageSize);
            pstmt.setInt(2, pageSize);
            // 4. 执行SQL语句
            rs = pstmt.executeQuery();
            // 5. 处理查询结果集
            while (rs.next()) {
                String ename = rs.getString("ename");
                System.out.println(ename);
            }
        } catch (Exception e) {
            e.printStackTrace();
        } finally {
            // 6. 释放资源
            if (rs != null) {
                try {
                    rs.close();
                } catch (SQLException e) {
                    throw new RuntimeException(e);
                }
            }
            if (pstmt != null) {
                try {
                    pstmt.close();
                } catch (SQLException e) {
                    throw new RuntimeException(e);
                }
            }
            if (conn != null) {
                try {
                    conn.close();
                } catch (SQLException e) {
                    throw new RuntimeException(e);
                }
            }
        }
    }
}
```
执行结果如下：
![image.png](https://cdn.nlark.com/yuque/0/2024/png/21376908/1708241685820-a51b06ef-5b38-4e64-806c-0c1b86fe1fab.png#averageHue=%23fbf9f8&clientId=u907c0c1a-424e-4&from=paste&height=99&id=u9d0f25ee&originHeight=99&originWidth=152&originalType=binary&ratio=1&rotation=0&showTitle=false&size=3174&status=done&style=shadow&taskId=u2501bf73-20d4-4c69-a735-1ba98ec06af&title=&width=152)

![](https://cdn.nlark.com/yuque/0/2023/jpeg/21376908/1692002570088-3338946f-42b3-4174-8910-7e749c31e950.jpeg#averageHue=%23f9f8f8&from=url&id=hAryG&originHeight=78&originWidth=1400&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=shadow&title=)
## blob数据的插入和读取
准备一张表：t_img，三个字段，一个id主键，一个图片名字name，一个img。
建表语句如下：

```sql
create table `t_img` (
  `id` bigint primary key auto_increment,
  `name` varchar(255),
  `img` blob
) engine=innodb;
```


准备一张图片：
![dog.jpg](https://cdn.nlark.com/yuque/0/2024/jpeg/21376908/1708242724736-094b007d-d418-4c4d-9a21-b12f20176daf.jpeg#averageHue=%23b0b4b2&clientId=u907c0c1a-424e-4&from=paste&height=200&id=u4371d107&originHeight=200&originWidth=200&originalType=binary&ratio=1&rotation=0&showTitle=false&size=9603&status=done&style=shadow&taskId=u4fc1ce36-27c9-4401-8282-e7cb4e89bd9&title=&width=200)

需求1：向t_img 表中插入一张图片。
```java
package com.powernode.jdbc;

import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStream;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.SQLException;
import java.util.ResourceBundle;

public class JDBCTest09 {
    public static void main(String[] args) {
        ResourceBundle bundle = ResourceBundle.getBundle("com.powernode.jdbc.jdbc");
        String driver = bundle.getString("driver");
        String url = bundle.getString("url");
        String user = bundle.getString("user");
        String password = bundle.getString("password");

        Connection conn = null;
        PreparedStatement pstmt = null;
        InputStream in = null;
        try {
            // 1. 注册驱动
            Class.forName(driver);
            // 2. 获取连接
            conn = DriverManager.getConnection(url, user, password);
            // 3. 获取预编译的数据操作对象
            String sql = "insert into t_img(img) values(?)";
            pstmt = conn.prepareStatement(sql);
            // 获取文件输入流
            in = new FileInputStream("d:/dog.jpg");
            pstmt.setBlob(1, in);
            // 4. 执行SQL语句
            int count = pstmt.executeUpdate();
            System.out.println("插入了" + count + "条记录");
        } catch (Exception e) {
            e.printStackTrace();
        } finally {
            // 6. 释放资源
            if (in != null) {
                try {
                    in.close();
                } catch (IOException e) {
                    throw new RuntimeException(e);
                }
            }
            if (pstmt != null) {
                try {
                    pstmt.close();
                } catch (SQLException e) {
                    throw new RuntimeException(e);
                }
            }
            if (conn != null) {
                try {
                    conn.close();
                } catch (SQLException e) {
                    throw new RuntimeException(e);
                }
            }
        }
    }
}
```
执行结果如下：
![image.png](https://cdn.nlark.com/yuque/0/2024/png/21376908/1708243266510-6d057b29-ab51-49d2-839b-322dae79a50e.png#averageHue=%23dde3b0&clientId=u907c0c1a-424e-4&from=paste&height=58&id=u1d8aaf1a&originHeight=58&originWidth=304&originalType=binary&ratio=1&rotation=0&showTitle=false&size=1815&status=done&style=shadow&taskId=u1af58cb1-140b-4fcf-8434-0a7c1aeba9a&title=&width=304)

需求2：从t_img 表中读取一张图片。（从数据库中读取一张图片保存到本地。）
```java
package com.powernode.jdbc;

import java.io.FileOutputStream;
import java.io.InputStream;
import java.io.OutputStream;
import java.sql.*;
import java.util.ResourceBundle;

public class JDBCTest10 {
    public static void main(String[] args) {
        ResourceBundle bundle = ResourceBundle.getBundle("com.powernode.jdbc.jdbc");
        String driver = bundle.getString("driver");
        String url = bundle.getString("url");
        String user = bundle.getString("user");
        String password = bundle.getString("password");

        Connection conn = null;
        PreparedStatement pstmt = null;
        ResultSet rs = null;
        try {
            // 1. 注册驱动
            Class.forName(driver);
            // 2. 获取连接
            conn = DriverManager.getConnection(url, user, password);
            // 3. 获取预编译的数据操作对象
            String sql = "select img from t_img where id = ?";
            pstmt = conn.prepareStatement(sql);
            pstmt.setInt(1, 1);
            // 4. 执行SQL语句
            rs = pstmt.executeQuery();
            // 5. 处理查询结果集
            if (rs.next()) {
                // 获取二进制大对象
                Blob img = rs.getBlob("img");
                // 获取输入流
                InputStream binaryStream = img.getBinaryStream();
                // 创建输出流，该输出流负责写到本地
                OutputStream out = new FileOutputStream("d:/dog2.jpg");
                byte[] bytes = new byte[1024];
                int readCount = 0;
                while ((readCount = binaryStream.read(bytes)) != -1) {
                    out.write(bytes, 0, readCount);
                }
                out.flush();
                binaryStream.close();
                out.close();
            }
        } catch (Exception e) {
            e.printStackTrace();
        } finally {
            // 6. 释放资源
            if (rs != null) {
                try {
                    rs.close();
                } catch (SQLException e) {
                    throw new RuntimeException(e);
                }
            }
            if (pstmt != null) {
                try {
                    pstmt.close();
                } catch (SQLException e) {
                    throw new RuntimeException(e);
                }
            }
            if (conn != null) {
                try {
                    conn.close();
                } catch (SQLException e) {
                    throw new RuntimeException(e);
                }
            }
        }
    }
}
```
执行完毕之后，查看一下图片大小是否和原图片相同，打开看看是否可以正常显示。

![](https://cdn.nlark.com/yuque/0/2023/jpeg/21376908/1692002570088-3338946f-42b3-4174-8910-7e749c31e950.jpeg#averageHue=%23f9f8f8&from=url&id=mIusF&originHeight=78&originWidth=1400&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=shadow&title=)
# JDBC批处理操作
准备一张商品表：t_product
建表语句如下：
```sql
create table t_product(
  id bigint primary key,
  name varchar(255)
);
```
## 不使用批处理
不使用批处理，向 t_product 表中插入一万条商品信息，并记录耗时！
```java
package com.powernode.jdbc;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.SQLException;
import java.util.ResourceBundle;

public class NoBatchTest {
    public static void main(String[] args) {
        ResourceBundle bundle = ResourceBundle.getBundle("com.powernode.jdbc.jdbc");
        String driver = bundle.getString("driver");
        String url = bundle.getString("url");
        String user = bundle.getString("user");
        String password = bundle.getString("password");

        long begin = System.currentTimeMillis();
        Connection conn = null;
        PreparedStatement pstmt = null;
        try {
            // 1. 注册驱动
            Class.forName(driver);
            // 2. 获取连接
            conn = DriverManager.getConnection(url, user, password);
            // 3. 获取预编译的数据操作对象
            String sql = "insert into t_product(id, name) values (?, ?)";
            pstmt = conn.prepareStatement(sql);
            int count = 0;
            for (int i = 1; i <= 10000; i++) {
                pstmt.setInt(1, i);
                pstmt.setString(2, "product" + i);
                // 4. 执行SQL语句
                count += pstmt.executeUpdate();
            }
            System.out.println("插入了" + count + "条记录");
        } catch (Exception e) {
            e.printStackTrace();
        } finally {
            // 6. 释放资源
            if (pstmt != null) {
                try {
                    pstmt.close();
                } catch (SQLException e) {
                    throw new RuntimeException(e);
                }
            }
            if (conn != null) {
                try {
                    conn.close();
                } catch (SQLException e) {
                    throw new RuntimeException(e);
                }
            }
        }
        long end = System.currentTimeMillis();
        System.out.println("总耗时" + (end - begin) + "毫秒");
    }
}

```
执行结果如下：
![image.png](https://cdn.nlark.com/yuque/0/2024/png/21376908/1708249553654-263146be-a485-4313-831f-892a776abd1d.png#averageHue=%23edeceb&clientId=u21834790-ed4d-4&from=paste&height=67&id=u376a8236&originHeight=67&originWidth=175&originalType=binary&ratio=1&rotation=0&showTitle=false&size=2603&status=done&style=shadow&taskId=u9b065934-65ea-4ab2-8bd0-0a29936bbb8&title=&width=175)

![](https://cdn.nlark.com/yuque/0/2023/jpeg/21376908/1692002570088-3338946f-42b3-4174-8910-7e749c31e950.jpeg#averageHue=%23f9f8f8&from=url&id=PoOE1&originHeight=78&originWidth=1400&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=shadow&title=)
## 使用批处理
使用批处理，向 t_product 表中插入一万条商品信息，并记录耗时！
**注意：启用批处理需要在URL后面添加这个的参数：rewriteBatchedStatements=true**
![image.png](https://cdn.nlark.com/yuque/0/2024/png/21376908/1708249622292-576aa82d-5874-4013-a9b4-d94c00cef0ce.png#averageHue=%23fefdfb&clientId=u21834790-ed4d-4&from=paste&height=177&id=u4263b9d7&originHeight=177&originWidth=1592&originalType=binary&ratio=1&rotation=0&showTitle=false&size=24176&status=done&style=shadow&taskId=u444819ae-8458-45a1-b734-bb75ab7faf4&title=&width=1592)
```java
package com.powernode.jdbc;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.SQLException;
import java.util.ResourceBundle;

public class BatchTest {
    public static void main(String[] args) {
        ResourceBundle bundle = ResourceBundle.getBundle("com.powernode.jdbc.jdbc");
        String driver = bundle.getString("driver");
        String url = bundle.getString("url");
        String user = bundle.getString("user");
        String password = bundle.getString("password");

        long begin = System.currentTimeMillis();
        Connection conn = null;
        PreparedStatement pstmt = null;
        try {
            // 1. 注册驱动
            Class.forName(driver);
            // 2. 获取连接
            conn = DriverManager.getConnection(url, user, password);
            // 3. 获取预编译的数据操作对象
            String sql = "insert into t_product(id, name) values (?, ?)";
            pstmt = conn.prepareStatement(sql);
            int count = 0;
            for (int i = 1; i <= 10000; i++) {
                pstmt.setInt(1, i);
                pstmt.setString(2, "product" + i);
                pstmt.addBatch();
            }
            count += pstmt.executeBatch().length;
            System.out.println("插入了" + count + "条记录");
        } catch (Exception e) {
            e.printStackTrace();
        } finally {
            // 6. 释放资源
            if (pstmt != null) {
                try {
                    pstmt.close();
                } catch (SQLException e) {
                    throw new RuntimeException(e);
                }
            }
            if (conn != null) {
                try {
                    conn.close();
                } catch (SQLException e) {
                    throw new RuntimeException(e);
                }
            }
        }
        long end = System.currentTimeMillis();
        System.out.println("总耗时" + (end - begin) + "毫秒");
    }
}

```
执行结果如下：
![image.png](https://cdn.nlark.com/yuque/0/2024/png/21376908/1708249131242-0bf6746b-86f7-4bc9-966b-00d22994e177.png#averageHue=%23ecebea&clientId=u21834790-ed4d-4&from=paste&height=62&id=u8650f4b7&originHeight=62&originWidth=176&originalType=binary&ratio=1&rotation=0&showTitle=false&size=2142&status=done&style=shadow&taskId=u5e5c9eb2-21df-410b-bafb-e9edb16ccb3&title=&width=176)

在进行大数据量插入时，批处理为什么可以提高程序的执行效率？

1.  减少了网络通信次数：JDBC 批处理会将多个 SQL 语句一次性发送给服务器，减少了客户端和服务器之间的通信次数，从而提高了数据写入的速度，特别是对于远程服务器而言，优化效果更为显著。 
2.  减少了数据库操作次数：JDBC 批处理会将多个 SQL 语句合并成一条 SQL 语句进行执行，从而减少了数据库操作的次数，减轻了数据库的负担，大大提高了数据写入的速度。  

![](https://cdn.nlark.com/yuque/0/2023/jpeg/21376908/1692002570088-3338946f-42b3-4174-8910-7e749c31e950.jpeg#averageHue=%23f9f8f8&from=url&id=g9Pw5&originHeight=78&originWidth=1400&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=shadow&title=)
# DbUtils工具类的封装
JDBC编程六步中，很多代码是重复出现的，可以为这些代码封装一个工具类。让JDBC代码变的更简洁。
```java
package com.powernode.jdbc;

import java.sql.*;
import java.util.ResourceBundle;

/**
 * ClassName: DbUtils
 * Description: JDBC工具类
 * Datetime: 2024/4/10 22:29
 * Author: 老杜@动力节点
 * Version: 1.0
 */
public class DbUtils {
    private static String url;
    private static String user;
    private static String password;

    static {
        // 读取属性资源文件
        ResourceBundle bundle = ResourceBundle.getBundle("com.powernode.jdbc.jdbc");
        String driver = bundle.getString("driver");
        url = bundle.getString("url");
        user = bundle.getString("user");
        password = bundle.getString("password");
        // 注册驱动
        try {
            Class.forName(driver);
        } catch (ClassNotFoundException e) {
            throw new RuntimeException(e);
        }
    }

    /**
     * 获取数据库连接
     * @return
     * @throws SQLException
     */
    public static Connection getConnection() throws SQLException {
        Connection conn = DriverManager.getConnection(url, user, password);
        return conn;
    }

    /**
     * 释放资源
     * @param conn 连接对象
     * @param stmt 数据库操作对象
     * @param rs 结果集对象
     */
    public static void close(Connection conn, Statement stmt, ResultSet rs){
        if (rs != null) {
            try {
                rs.close();
            } catch (SQLException e) {
                throw new RuntimeException(e);
            }
        }
        if (stmt != null) {
            try {
                stmt.close();
            } catch (SQLException e) {
                throw new RuntimeException(e);
            }
        }
        if (conn != null) {
            try {
                conn.close();
            } catch (SQLException e) {
                throw new RuntimeException(e);
            }
        }
    }
}

```

![](https://cdn.nlark.com/yuque/0/2023/jpeg/21376908/1692002570088-3338946f-42b3-4174-8910-7e749c31e950.jpeg#averageHue=%23f9f8f8&from=url&id=Ttvmv&originHeight=78&originWidth=1400&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=shadow&title=)
