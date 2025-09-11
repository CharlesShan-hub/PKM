# JDBC

---
## 概述

1. JDBC（Java DataBase Connectivity）就是Java数据库连接，即一套使用Java语言来操作数据库的编程接口，也可以认为是一组规范。
2. 早期SUN公司的天才们想编写一套可以连接天下所有数据库的API，但是当他们刚刚开始时就发现这是不可完成的任务，因为各个厂商的数据库服务器差异太大了。后来SUN开始与数据库厂商们讨论，最终得出的结论是，由SUN提供一套访问数据库的规范（就是一组接口），并提供连接数据库的协议标准，然后各个数据库厂商会遵循SUN的规范提供一套访问自己公司的数据库服务器的API出现。SUN提供的规范命名为JDBC，而各个厂商提供的，遵循了JDBC规范的，可以访问自己数据库的API被称之为驱动！
3. JDBC是接口，而JDBC驱动才是接口的实现，没有驱动无法完成数据库连接！每个数据库厂商都有自己的驱动，用来连接自己公司的数据库。
4. JDBC API
   1. 提供者：Sun公司
   2. 内容：供程序员调用的接口与类，集成在java.sql和javax.sql包中，如
      1. DriverManager类，管理各种不同的JDBC驱动
      2. Connection接口，用于连接数据库
      3. Statement接口，用于执行SQL语句
      4. ResultSet接口，用于处理查询结果集
5. JDBC 驱动
   1. 提供者：各个数据库厂商
   2. 内容：遵循JDBC规范的数据库驱动，用于连接数据库服务器
6. SUN公司是规范制定者，制定了规范JDBC（连接数据库规范），数据库厂商微软、甲骨文等分别提供实现JDBC接口的驱动jar包，程序员学习JDBC规范来应用这些jar包里的类。

---
## JDBC操作数据库的步骤

### 加载数据库驱动

```xml
<dependency>  
    <groupId>com.mysql</groupId>  
    <artifactId>mysql-connector-j</artifactId>  
    <version>8.0.33</version>  
</dependency>
```

```java
package com.charles;  
  
public class DemoConnect {  
    public static void main(String[] args) {  
        try {  
            // MySQL 5.x及以前版本驱动  
            // Class.forName("com.mysql.jdbc.Driver");  
            // MySQL 8.x版本驱动  
            Class.forName("com.mysql.cj.jdbc.Driver");  
  
            // Oracle数据库驱动  
            // Class.forName("oracle.jdbc.OracleDriver");  
  
            // SQL Server数据库驱动  
            // Class.forName("com.microsoft.sqlserver.jdbc.SQLServerDriver");  
  
            // PostgreSQL数据库驱动  
            // Class.forName("org.postgresql.Driver");  
  
            // SQLite数据库驱动  
            // Class.forName("org.sqlite.JDBC");  
  
            // DB2数据库驱动  
            // Class.forName("com.ibm.db2.jcc.DB2Driver");  
  
            // Sybase数据库驱动  
            // Class.forName("com.sybase.jdbc.SybDriver");  
  
            // H2数据库驱动  
            // Class.forName("org.h2.Driver");  
  
            // Derby数据库驱动  
            // Class.forName("org.apache.derby.jdbc.ClientDriver");  
  
            // MariaDB数据库驱动  
            // Class.forName("org.mariadb.jdbc.Driver");  
  
            System.out.println("驱动加载成功！");  
        } catch (ClassNotFoundException e) {  
            System.out.println("错误原因分析：");  
            System.out.println("1. 没有添加对应的数据库驱动jar包到项目的classpath中");  
            System.out.println("2. 使用了错误版本的驱动类名");  
            System.out.println("3. 驱动jar包的路径配置不正确");  
            e.printStackTrace();  
        }  
    }  
}

/*
* 关于java.lang.ClassNotFoundException: com.mysql.jdbc.Driver的解决方案：
*
* 1. 下载MySQL JDBC驱动：
*    - 访问MySQL官网：https://dev.mysql.com/downloads/connector/j/
*    - 根据你的MySQL版本选择对应的驱动版本（MySQL 8.x建议使用8.x版本的驱动）
*    - 下载Platform Independent版本的ZIP文件
*
* 2. 添加驱动到项目：
*    - 方法1：使用命令行编译运行时指定classpath
*      javac Demo.java
*      java -cp .:mysql-connector-j-x.x.x.jar Demo
*    - 方法2：在IDE中添加为依赖
*      Eclipse：右键项目 -> Build Path -> Add External Archives...
*      IntelliJ IDEA：File -> Project Structure -> Libraries -> + -> Java
*
* 3. 注意版本兼容性：
*    - MySQL 5.x使用：com.mysql.jdbc.Driver
*    - MySQL 8.x使用：com.mysql.cj.jdbc.Driver
*    - 8.x版本驱动还需要指定时区：serverTimezone=UTC
*
* 4. Maven项目可以直接添加依赖：
*    <dependency>
*        <groupId>com.mysql</groupId>
*        <artifactId>mysql-connector-j</artifactId>
*        <version>8.2.0</version> <!-- 使用最新稳定版本 -->
*    </dependency>
*
* 5. 从JDBC 4.0开始，不需要显式调用Class.forName()来加载驱动
*    因为JDBC驱动jar包中包含了META-INF/services/java.sql.Driver文件
*    DriverManager会自动加载classpath中的驱动
*/
```

### 建立数据库连接

```java
Connection conn=null;
String url="jdbc:mysql://localhost:3306/bjpowernode?charsetUnicode=UTF8&serverTimezone=UTC";
String user="root";
String password="";
conn = DriverManager.getConnection(url, user, password);
```

### 创建Statement对象

Statement对象用于将 SQL 语句发送到数据库中，或者理解为执行sql语句
有三种 Statement对象：
* `Statement`：用于执行不带参数的简单SQL语句；
* `PreparedStatement`（从 Statement 继承）：用于执行带或不带参数的预编译SQL语句；
* `CallableStatement`（从PreparedStatement 继承）：用于执行数据库存储过程的调用。

### 处理查询结果集

* ResultSet executeQuery()：执行查询语句，返回一个 ResultSet 对象。
* int executeUpdate()：执行更新语句（如INSERT、UPDATE、DELETE），返回受影响的行数。
* boolean execute()：执行任意SQL语句，返回一个 boolean 值，指示是否返回 ResultSet。

ResultSet对象是executeQuery()方法的返回值，它被称为结果集，它代表符合SQL语句条件的所有行，并且它通过一套getXXX方法（这些get方法可以访问当前行中的不同列）提供了对这些行中数据的访问。
ResultSet里的数据一行一行排列，每行有多个字段，且有一个记录指针，指针所指的数据行叫做当前数据行，我们只能来操作当前的数据行。我们如果想要取得某一条记录，就要使用ResultSet的next()方法 ,如果我们想要得到ResultSet里的所有记录，就应该使用while循环。
ResultSet对象自动维护指向当前数据行的游标。每调用一次next()方法，游标向下移动一行。 
初始状态下记录指针指向第一条记录的前面，通过next()方法指向第一条记录。循环完毕后指向最后一条记录的后面。

* boolean next()：将记录指针移动到下一行。如果有下一行，则返回 true；如果没有下一行，则返回 false。
* boolean previous()：将记录指针移动到上一行。如果有上一行，则返回 true；如果没有上一行，则返回 false。
* getXXX()：用于获取当前数据行中指定列的值。XXX表示列的数据类型，如getInt()、getString()等。
* void close()：关闭ResultSet对象，释放数据库资源。

### 关闭数据库资源

作为一种好的编程风格，应在不需要Statement对象和Connection对象时显式地关闭它们。关闭Statement对象和Connection对象的语法形式为：
`public void close() throws SQLException`
用户不必关闭ResultSet。当它的 Statement 关闭、重新执行或用于从多结果序列中获取下一个结果时，该ResultSet将被自动关闭。
注意：要按先ResultSet结果集，后Statement，最后Connection的顺序关闭资源，因为Statement和ResultSet是需要连接是才可以使用的，所以在使用结束之后有可能其他的Statement还需要连接，所以不能先关闭Connection。

---
## 增删改查

### 初始化
```sql
# 创建数据库  
CREATE DATABASE IF NOT EXISTS learnjdbc;  
# 使用数据库  
USE learnjdbc;  
# 如果表存在则删除  
DROP TABLE IF EXISTS tbl_student;  
# 创建学生表  
CREATE TABLE tbl_student (  
	 id INT AUTO_INCREMENT PRIMARY KEY,  
	 name VARCHAR(50) NOT NULL,  
	 age INT  
);  
# 插入示例数据  
INSERT INTO tbl_student (name, age) VALUES  
('张三', 23),  
('李四', 25),  
('王五', 22),  
('赵六', 24);
```

### 插入
```java
package com.charles;  
  
import java.sql.Connection;  
import java.sql.DriverManager;  
import java.sql.SQLException;  
import java.sql.Statement;  
  
public class AddStudent {  
    public static void main(String[] args) {  
  
        //定义连接对象  
        Connection conn=null;  
        //定义SQL装在容器  
        Statement st=null;  
        String sql="insert into tbl_student (name,age)values('张三',23)";  
        String url="jdbc:mysql://localhost:3306/learnjdbc";  
        String username="root";  
        String password= "";  
  
        try {  
            //加载数据库驱动  
            Class.forName("com.mysql.cj.jdbc.Driver");  
            //创建数据库连接  
            conn= DriverManager.getConnection(url,username,password);  
            //创建SQL容器  
            st=conn.createStatement();  
            //装在并执行SQL语句的写操作,返回int类型的参数，表示本条SQL影响了几条记录  
            int result= st.executeUpdate(sql);  
            System.out.println("本条SQL影响了："+result+"条记录");  
  
        } catch (ClassNotFoundException | SQLException e) {  
            e.printStackTrace();  
        }finally {  
            if(st!=null){  
                try {  
                    st.close();  
                } catch (SQLException throwables) {  
                    throwables.printStackTrace();  
                }  
            }  
            if(conn!=null){  
                try {  
                    conn.close();  
                } catch (SQLException throwables) {  
                    throwables.printStackTrace();  
                }  
            }  
        }  
    }  
}
```

### 修改数据

```java
package com.charles;  
  
import java.sql.Connection;  
import java.sql.DriverManager;  
import java.sql.SQLException;  
import java.sql.Statement;  
  
public class ModifyStudent {  
    public static void main(String[] args) {  
  
        //定义连接对象  
        Connection conn=null;  
        //定义SQL装在容器  
        Statement st=null;  
        String sql="update tbl_student set name='李四' ,age=24 where id=2";  
        String url="jdbc:mysql://localhost:3306/learnjdbc";  
        String username="root";  
        String password= "";  
  
        try {  
            //加载数据库驱动  
            Class.forName("com.mysql.cj.jdbc.Driver");  
            //创建数据库连接  
            conn= DriverManager.getConnection(url,username,password);  
            //创建SQL容器  
            st=conn.createStatement();  
            //装在并执行SQL语句的写操作,返回int类型的参数，表示本条SQL影响了几条记录  
            int result= st.executeUpdate(sql);  
            System.out.println("本条SQL影响了："+result+"条记录");  
  
        } catch (ClassNotFoundException | SQLException e) {  
            e.printStackTrace();  
        }finally {  
            if(st!=null){  
                try {  
                    st.close();  
                } catch (SQLException throwables) {  
                    throwables.printStackTrace();  
                }  
            }  
            if(conn!=null){  
                try {  
                    conn.close();  
                } catch (SQLException throwables) {  
                    throwables.printStackTrace();  
                }  
            }  
        }  
    }  
}
```

### 进行简单封装

```java
package com.charles;  
  
import java.sql.Connection;  
import java.sql.DriverManager;  
import java.sql.SQLException;  
import java.sql.Statement;  
import java.util.Collection;  
  
/**  
 * 数据库JDBC的工具类，用于维护连接对象  
 *  
 */class Utils {  
    private static String DRIVER_CLASS_NAME="com.mysql.cj.jdbc.Driver";  
    private static String URL="jdbc:mysql://localhost:3306/learnjdbc";  
    private static String USERNAME="root";  
    private static String PASSWORD= "";  
    static{  
        try {  
            Class.forName(DRIVER_CLASS_NAME);  
        } catch (ClassNotFoundException e) {  
            e.printStackTrace();  
        }  
    }  
  
    public static Connection getConn(){  
        Connection conn=null;  
        try {  
            conn= DriverManager.getConnection(URL,USERNAME,PASSWORD);  
        } catch (SQLException throwables) {  
            throwables.printStackTrace();  
        }  
        return conn;  
    }  
  
    public static void execute(Connection conn, String sql){  
        if (sql != null && conn !=null){  
            try{  
                Statement st=conn.createStatement();  
                st.execute(sql);  
            } catch (SQLException e) {  
                throw new RuntimeException(e);  
            }  
        }  
    }  
  
    public static void close(Statement st,Connection conn){  
        if(st!=null){  
            try {  
                st.close();  
            } catch (SQLException throwables) {  
                throwables.printStackTrace();  
            }  
        }  
        if(conn!=null){  
            try {  
                conn.close();  
            } catch (SQLException throwables) {  
                throwables.printStackTrace();  
            }  
        }  
    }  
}  
  
public class DemoUtil {  
    public static void main(String[] args)  
    {  
        Connection conn=Utils.getConn();  
        Utils.execute(conn, "insert into tbl_student values(6,'张三',18)");  
        Utils.close(null,null);  
    }  
}
```

### 查询

增删改查一体化

```java
package com.charles;  
  
import java.sql.*;  
import java.util.ArrayList;  
import java.util.List;  
  
class Student{  
    public int id;  
    public String name;  
    public int age;  
    @Override  
    public String toString() {  
        return "Student{" +  
                "id=" + id +  
                ", name='" + name + '\'' +  
                ", age=" + age +  
                '}';  
    }  
}  
  
class DBUtil {  
    private static String DRIVER_CLASS_NAME="com.mysql.cj.jdbc.Driver";  
    private static String URL="jdbc:mysql://localhost:3306/learnjdbc";  
    private static String USERNAME="root";  
    private static String PASSWORD= "";  
    public static Connection conn=null;  
    public static Statement st=null;  
    static{  
        try {  
            Class.forName(DRIVER_CLASS_NAME);  
            conn= DriverManager.getConnection(URL,USERNAME,PASSWORD);  
            st=conn.createStatement();  
        } catch (ClassNotFoundException e) {  
            throw new RuntimeException(e);  
        } catch (SQLException e) {  
            throw new RuntimeException(e);  
        }  
    }  
  
    public static boolean addStudent(String name, int age) throws SQLException {  
        // 检查学生是否已存在  
        String checkSql = "SELECT * FROM tbl_student WHERE name = '" + name + "' AND age = " + age;  
        ResultSet rs = st.executeQuery(checkSql);  
  
        // 如果没有找到相同的记录，则添加新学生  
        if (!rs.next()) {  
            String sql = "INSERT INTO tbl_student VALUES(null,'" + name + "'," + age + ")";  
            st.execute(sql);  
            rs.close();  
            return true; // 添加成功  
        } else {  
            rs.close();  
            return false; // 学生已存在，添加失败  
        }  
    }  
  
    public static boolean deleteStudentById(int id) throws SQLException {  
        // 检查学生是否存在  
        String checkSql = "SELECT * FROM tbl_student WHERE id = " + id;  
        ResultSet rs = st.executeQuery(checkSql);  
  
        // 如果找到该学生，则删除  
        if (rs.next()) {  
            String sql = "DELETE FROM tbl_student WHERE id = " + id;  
            st.execute(sql);  
            rs.close();  
            return true; // 删除成功  
        } else {  
            rs.close();  
            return false; // 学生不存在，删除失败  
        }  
    }  
  
    public static int getStudentId(String name, int age) throws SQLException {  
        String sql = "SELECT id FROM tbl_student WHERE name = '" + name + "' AND age = " + age;  
        ResultSet rs = st.executeQuery(sql);  
  
        if (rs.next()) {  
            return rs.getInt("id");  
        } else {  
            return -1; // 未找到该学生  
        }  
    }  
  
    public static boolean modifyStudent(int id, String name, int age) throws SQLException {  
        // 检查学生是否存在  
        String checkSql = "SELECT * FROM tbl_student WHERE id = " + id;  
        ResultSet rs = st.executeQuery(checkSql);  
  
        // 如果找到该学生，则修改  
        if (rs.next()) {  
            String sql = "UPDATE tbl_student SET name = '" + name + "', age = " + age + " WHERE id = " + id;  
            st.execute(sql);  
            rs.close();  
            return true;  
        }else{  
            rs.close();  
            return false;  
        }  
    }  
  
    public static void showAllStudents() throws SQLException {  
        String sql = "SELECT * FROM tbl_student";  
        ResultSet rs = st.executeQuery(sql);  
        List<Student> students = new ArrayList<>();  
  
        while (rs.next()) {  
            Student student = new Student();  
            student.id = rs.getInt("id");  
            student.name = rs.getString("name");  
            student.age = rs.getInt("age");  
            students.add(student);  
        }  
        for (Student student : students) {  
            System.out.println(student);  
        }  
    }  
  
    public static void showAllStudents(int pageNum, int pageSize) throws SQLException {  
        String sql = "SELECT * FROM tbl_student LIMIT " + (pageNum - 1) * pageSize + ", " + pageSize;  
        ResultSet rs = st.executeQuery(sql);  
        List<Student> students = new ArrayList<>();  
        while (rs.next()) {  
            Student student = new Student();  
            student.id = rs.getInt("id");  
            student.name = rs.getString("name");  
            student.age = rs.getInt("age");  
            students.add(student);  
        }  
        for (Student student : students) {  
            System.out.println(student);  
        }  
    }  
  
    public static void close() throws SQLException {  
        st.close();  
        conn.close();  
    }  
}  
  
public class DemoCheck {  
    public static void main(String[] args) throws SQLException {  
        // 增  
        DBUtil.addStudent("张三",18);  
        DBUtil.addStudent("王五",19);  
        DBUtil.addStudent("赵六",20);  
  
        // 查  
        int i = DBUtil.getStudentId("张三",18);  
        int j = DBUtil.getStudentId("王五",19);  
  
        // 删  
        DBUtil.deleteStudentById(i);  
  
        // 改  
        DBUtil.modifyStudent(j,"王五",20);  
  
        // 显示  
        DBUtil.showAllStudents();  
  
        // 分页  
        System.out.println("分页显示：page 1");  
        DBUtil.showAllStudents(1, 2);  
        System.out.println("分页显示：page 2");  
        DBUtil.showAllStudents(2, 2);  
  
        // 关闭  
        DBUtil.close();  
    }  
}
```

---
## 常用接口详解

### DriverManager

用于管理JDBC驱动的服务类。程序中使用该类的的主要功能是获取Connection对象，该类包含如下方法：

```java
public static Connection getConnection(String url, String user, String password) throws SQLException
```

该方法获得url对应数据库的连接；

### Connection

代表数据库**连接对象**，每个Connection代表一个**物理连接会话**。要想访问数据库，必须先得到数据库连接。该接口的常用方法如下：

* `Statement createStatement() throws SQLException; 该方法返回一个Statement对象；`
* `PreparedStatement prepareStatement(String sql)throws SQLException;`：该方法返回预编译的Statement对象，即将SQL语句提交到数据库进行预编译；
* `CallableStatement prepareCall(String sql) throws SQLException;`：该方法返回CallableStatement对象，该对象用于调用存储过程。

上面上个方法都返回用于执行sql语句的Statement对象，PreparedStatement和CallableStatement是Statement的子类，只有获得了Statement之后才可以执行sql语句；

除此之外，Connection还有如下几个用于控制事务的方法。

* `Savepoint setSavepoint() throws SQLException;` 创建一个保存点；
* `Savepoint setSavepoint(String name) throws SQLException;`以指定名字来创建一个保存点；
* `void setTransactionIsolation(int level) throws SQLException;`设置事务的隔离级别;
* `void rollback() throws SQLException;`回滚事务；
* `void rollback(Savepoint savepoint) throws SQLException;`将事务回滚到指定的保存点；
* `void setAutoCommit(boolean autoCommit) throws SQLException;`关闭自动提交，打开事务；
* `void commit() throws SQLException;`提交事务；

### Statement

用于执行sql语句的工具接口。该对象既可以执行DDL，DCL语句，也可以用于执行DML语句，还可以用于执行sql查询。当执行sql查询时，返回查询到的结果集。它的常用方法如下：

* `ResultSet executeQuery(String sql) throws SQLException;`该方法用于执行查询语句，并返回查询结果对应ResultSet对象。该方法只能用于执行查询语句;
* `int executeUpdate(String sql) throws SQLException;`该方法用于执行DML语句，并返回受影响的行数；该方法也可用于执行DDL语句，执行DDL语句将返回0;
* `boolean execute(String sql) throws SQLException;`改方法可以执行任何sql语句。如果执行后第一个结果为ResultSet对象，则返回true；如果执行后第一个结果为受影响的行数或没有任何结果，则返回false；

### PreparedStatement

预编译的Statement对象，PreparedStatement是Statement的子接口，它允许数据库预编译sql语句(这些sql语句通常带有参数)，以后每次只改变sql命令的参数，避免数据库每次都需要编译sql语句，无需再传入sql语句，

只要为预编译的sql语句传入参数值即可。所以它比Statement多了如下方法：

`void setXxx(int parameterIndex, Xxx value)`:该方法根据传入参数值的类型不同，需要使用不同的方法。传入的值根据索引传给sql语句中指定位置的参数。

### ResultSet

结果集对象。该对象包含访问查询结果的方法，ResultSet可以通过列索引或列名获得列数据。它包含了如下常用方法来移动记录指针。

void close() throws SQLException;释放ResultSet对象；

boolean absolute( int row ) throws SQLException;将结果集的记录指针移动到第row行，如果row是负数，则移动到倒数第row行，如果移动后的记录指针指向一条有效记录，则该方法返回true；

boolean next() throws SQLException;将结果集的记录指针定位到下一行，如果移动后的记录指针指向一条有效的记录，则该方法返回true；

boolean last() throws SQLException;将结果集的记录指针定位到最后一行，如果移动后的记录指针指向一条有效的记录，则该方法返回true；

---
## SQL注入问题

### 问题引出

先准备表

```sql
# 创建数据库  
CREATE DATABASE IF NOT EXISTS learnjdbc;  
# 使用数据库  
USE learnjdbc;  
# 如果表存在则删除  
DROP TABLE IF EXISTS tbl_auth;  
# 创建学生表  
CREATE TABLE tbl_auth (  
	 name VARCHAR(50) NOT NULL,  
	 password VARCHAR(50) NOT NULL
);  
# 插入示例数据  
INSERT INTO tbl_auth (name, password) VALUES  
('admin','123456'),
('admin2','123 456');
```

当前代码直接将用户输入拼接到SQL语句中，会导致SQL注入问题

```java
package com.charles;  
  
import java.sql.*;  
import java.util.Scanner;  
  
public class Inject{  
    public static void main(String[] args) throws ClassNotFoundException, SQLException {  
        Class.forName("com.mysql.cj.jdbc.Driver");  
        Connection conn = DriverManager.getConnection("jdbc:mysql://localhost:3306/learnjdbc", "root", "");  
        Statement st = conn.createStatement();  
        ResultSet rs = null;  
  
        Scanner input=new Scanner(System.in);  
        System.out.println("请输入账号：");  
        String username=input.nextLine();  
        System.out.println("请求输入密码：");  
        String password=input.nextLine();  
  
        String sql="select * from tbl_auth where name='"+username+"' and password='"+password+"'";  
        System.out.println(sql);  
  
        rs=st.executeQuery(sql);//执行查询  
        //光标向下移动，如果返回true则表示有数据，如果返回false则表示结果集中没有数据了  
        if(rs.next()){  
            System.out.println("登录成功");  
            System.out.println(rs.getString("name")+"-----"+rs.getString("password"));  
        }else{  
            System.out.println("登录失败");  
        }  
  
        st.close();  
        conn.close();  
    }  
}
```

```bash
请输入账号：
admin
请求输入密码：
' OR '1'='1
select * from tbl_auth where name='admin' and password='' OR '1'='1'
登录成功
admin-----123456
```

### 解决办法 - PreparedStatement

该 PreparedStatement接口继承Statement，并与之在两方面有所不同：

PreparedStatement 实例包含已编译的 SQL 语句。这就是使语句“准备好”**。包含于 PreparedStatement 对象中的 SQL 语句可具有一个或多个 IN 参数。IN参数的值在 SQL 语句创建时未被指定。相反的，该语句为每个 IN 参数保留一个问号**（“？”）作为占位符。每个问号的值必须在该语句执行之前，通过适当的setXXX 方法来提供。

由于 PreparedStatement 对象已预编译过，所以其执行速度要快于 Statement 对象。因此，多次执行的 SQL 语句经常创建为 PreparedStatement 对象，以提高效率。

作为 Statement 的子类，PreparedStatement 继承了 Statement 的所有功能。另外它还添加了一整套方法，用于设置发送给数据库以取代 IN 参数占位符的值。同时，三种方法 execute、 executeQuery 和 executeUpdate 已被更改以使之不再需要参数。这些方法的 Statement 形式（接受 SQL 语句参数的形式）不应该用于 PreparedStatement 对象。

```java
package com.charles;  
  
import java.sql.*;  
import java.util.Scanner;  
  
public class Inject{  
    public static void main(String[] args) throws ClassNotFoundException, SQLException {  
        Class.forName("com.mysql.cj.jdbc.Driver");  
        Connection conn = DriverManager.getConnection("jdbc:mysql://localhost:3306/learnjdbc", "root", "");  
        ResultSet rs = null;  
  
        Scanner input=new Scanner(System.in);  
        System.out.println("请输入账号：");  
        String username=input.nextLine();  
        System.out.println("请求输入密码：");  
        String password=input.nextLine();  
  
        // 使用PreparedStatement防止SQL注入  
        String sql = "SELECT * FROM tbl_auth WHERE name = ? AND password = ?";  
        System.out.println(sql);  
        PreparedStatement pst = conn.prepareStatement(sql);  
        pst.setString(1, username);  
        pst.setString(2, password);  
  
        rs=pst.executeQuery();//执行查询  

        if(rs.next()){  
            System.out.println("登录成功");  
            System.out.println(rs.getString("name")+"-----"+rs.getString("password"));  
        }else{  
            System.out.println("登录失败");  
        }  
  
        pst.close();  
        conn.close();  
    }  
}
```

---
## 事务处理

### 什么是事务

是数据库操作的最小工作单元，是作为单个逻辑工作单元执行的一系列操作；这些操作作为一个整体一起向系统提交，要么都执行、要么都不执行；事务是一组不可再分割的操作集合（工作逻辑单元）

### 事务的四大特性

acid

#### **原子性**

事务是数据库的逻辑工作单位，事务中包含的各操作要么都做，要么都不做

#### **一致性**

事 务执行的结果必须是使数据库从一个一致性状态变到另一个一致性状态。因此当数据库只包含成功事务提交的结果时，就说数据库处于一致性状态。如果数据库系统 运行中发生故障，有些事务尚未完成就被迫中断，这些未完成事务对数据库所做的修改有一部分已写入物理数据库，这时数据库就处于一种不正确的状态，或者说是 不一致的状态。

#### **隔离性**

一个事务的执行不能其它事务干扰。即一个事务内部的操作及使用的数据对其它并发事务是隔离的，并发执行的各个事务之间不能互相干扰。

#### **持久性**

也称永久性，指一个事务一旦提交，它对数据库中的数据的改变就应该是永久性的。接下来的其它操作或故障不应该对其执行结果有任何影响。

### 案例

需求描述：完成转账操作，要求，两次数据库操作，要么全成功。要么全失败

初始化

```sql
# 创建数据库  
CREATE DATABASE IF NOT EXISTS learnjdbc;  
# 使用数据库  
USE learnjdbc;  
# 如果表存在则删除  
DROP TABLE IF EXISTS tbl_account;  
# 创建学生表  
CREATE TABLE tbl_account (  
	 id INT AUTO_INCREMENT PRIMARY KEY,  
	 name VARCHAR(50) NOT NULL,  
	 amount INT  
);
# 插入示例数据  
INSERT INTO tbl_account (name, amount) VALUES  
('a',10000),
('b',20000);
```

没有事务的案例

```java
package com.charles;  
  
import java.sql.Connection;  
import java.sql.DriverManager;  
import java.sql.PreparedStatement;  
import java.sql.SQLException;  
  
public class Transaction {  
    public static void main(String[] args) throws ClassNotFoundException, SQLException {  
        Class.forName("com.mysql.cj.jdbc.Driver");  
        Connection conn = DriverManager.getConnection("jdbc:mysql://localhost:3306/learnjdbc", "root", "");  
        PreparedStatement ps=null;  
        String sql="update tbl_account set amount=amount-? where id=?";  
  
        ps=conn.prepareStatement(sql);  
        ps.setInt(1,1000);  
        ps.setInt(2,1);  
        ps.executeUpdate();  
  
        //抛出异常，导致第二条SQL无法执行，  
        //由于MySQL事务是自动提交，因此第一条SQL已经完成了减少，但是第二条SQL无法执行，所以导致丢钱了  
        System.out.println(10/0);  
        ps.setInt(1,-1000);  
        ps.setInt(2,2);  
        ps.executeUpdate();  
    }  
}
```

添加了事务的案例

```java
package com.charles;  
  
import java.sql.Connection;  
import java.sql.DriverManager;  
import java.sql.PreparedStatement;  
import java.sql.SQLException;  
  
public class Transaction {  
    public static void main(String[] args) throws SQLException {  
        try{  
            Class.forName("com.mysql.cj.jdbc.Driver");  
        }catch (ClassNotFoundException e){  
            e.printStackTrace();  
        }  
  
        Connection conn = null;  
        PreparedStatement ps=null;  
        try{  
            conn = DriverManager.getConnection("jdbc:mysql://localhost:3306/learnjdbc", "root", "");  
            conn.setAutoCommit(false); // 关闭自动提交  
            String sql="update tbl_account set amount=amount-? where id=?";  
  
            ps=conn.prepareStatement(sql);  
            ps.setInt(1,1000);  
            ps.setInt(2,1);  
            ps.executeUpdate();  
  
            //抛出异常，导致第二条SQL无法执行，  
            System.out.println(10/0);  
            ps.setInt(1,-1000);  
            ps.setInt(2,2);  
            ps.executeUpdate();  
  
            conn.commit(); // 提交事务  
        }catch (SQLException e){  
            conn.rollback(); // 回滚事务  
            e.printStackTrace();  
        }finally {  
            if(ps!=null){  
                ps.close();  
            }  
            if(conn!=null){  
                conn.close();  
            }  
        }  
    }  
}
```

---
## JDBC批处理

### 什么是批处理

批处理是建立一次连接(创建一个Connection对象)的情况下批量执行多个DML语句，这些DML语句要么全部成功要么全部失败。如何确保全部成功or全部失败呢？在JDBC中开启事务，使用事务管理DML语句。

### 需求描述及操作步骤

使用批处理根据id批量的删除student表中的数据

1 定义SQL配置文件
2 创建Connection对象
3 创建PreparedStatement对象
4 将提交方式设置为手动提交，开启事务
5 设置占位符
6 将占位符添加到批处理中（相当于收集若干个本子，放入包包中）
7 执行批处理
8 提交事务
9 如果批处理失败，在catch块中回滚事务
10 关闭资源

### 案列代码

```java
package com.charles;  
  
import java.sql.Connection;  
import java.sql.DriverManager;  
import java.sql.PreparedStatement;  
import java.sql.SQLException;  
  
public class Batch {  
    public static void main(String[] args) throws ClassNotFoundException, SQLException {  
        Class.forName("com.mysql.cj.jdbc.Driver");  
        Connection conn = DriverManager.getConnection("jdbc:mysql://localhost:3306/learnjdbc", "root", "");  
        conn.setAutoCommit(false);  
        String sql="insert into tbl_student (name,age)values(?,?)";  
        PreparedStatement ps = conn.prepareStatement(sql);  
  
        for(int i=0;i<10;i++){  
            ps.setString(1,"呵呵");  
            ps.setInt(2,20+i);  
            ps.addBatch();//将SQL语句提交到，批量SQL容器中，等待提交给数据库  
        }  
        //执行批量SQL返回一个int类型的数组，数组中每个元素表示当前SQL影响了几条记录  
  
        int rows[]=ps.executeBatch();  
        for(int row:rows){  
            System.out.println("本条SQL影响了："+row+"条记录");  
        }  
        //提交事务  
        conn.commit();  
  
        ps.close();  
        conn.close();  
    }  
}
```