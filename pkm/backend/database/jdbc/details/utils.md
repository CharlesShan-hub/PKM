# DbUtils工具类的封装

JDBC编程六步中，很多代码是重复出现的，可以为这些代码封装一个工具类。让JDBC代码变的更简洁。

```java
package top.charles.utils;  
  
import java.sql.*;  
import java.util.ResourceBundle;  
  
/**  
 * ClassName: DbUtils * Description: JDBC工具类  
 * Datetime: 2024/4/10 22:29  
 * Author: 老杜@动力节点  
 * Version: 1.0  
 */public class DbUtils {  
    private static String url;  
    private static String user;  
    private static String password;  
  
    static {  
        // 读取属性资源文件  
        ResourceBundle bundle = ResourceBundle.getBundle("jdbc");  
        String driver = bundle.getString("driver");  
        url = bundle.getString("url");  
        user = bundle.getString("user");  
        password = bundle.getString("password");  
        // 注册驱动  
        try {  
            Class.forName(driver);  
        } catch (ClassNotFoundException e) {  
            throw new RuntimeException(e);  
        }    }  
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
            }        }        if (stmt != null) {  
            try {  
                stmt.close();  
            } catch (SQLException e) {  
                throw new RuntimeException(e);  
            }        }        if (conn != null) {  
            try {  
                conn.close();  
            } catch (SQLException e) {  
                throw new RuntimeException(e);  
            }        }    }}
package top.charles.utils;

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
        ResourceBundle bundle = ResourceBundle.getBundle("jdbc");
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
    public static void close(Connection conn, Statement stmt, ResultSet rs) {
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

下边是jdbc.properties

```properties
driver=com.mysql.cj.jdbc.Driver  
url=jdbc:mysql://localhost:3306/jdbc?useUnicode=true&serverTimezone=Asia/Shanghai&useSSL=true&characterEncoding=utf-8  
user=root  
password=
```