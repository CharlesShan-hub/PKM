# JDBC架构原理

## 1. 三个核心角色
- **制定者**：SUN公司定义JDBC接口规范
- **实现者**：数据库厂商提供具体驱动实现
- **调用者**：Java程序员使用接口编程

## 2. 接口定义与实现
```java
// JDBC接口定义
public interface JDBC {
    void getConnection();
}

// MySQL驱动实现
public class MySQLDriver implements JDBC {
    public void getConnection() {
        System.out.println("连接MySQL数据库");
    }
}

// Oracle驱动实现
public class OracleDriver implements JDBC {
    public void getConnection() {
        System.out.println("连接Oracle数据库");
    }
}
```

## 3. 面向接口编程
```java
// 直接使用具体驱动（硬编码）
JDBC jdbc = new MySQLDriver();
jdbc.getConnection();
```

## 4. 配置文件解耦（OCP原则）
```properties
# jdbc.properties
driver=MySQLDriver
```

```java
// 通过反射动态加载驱动
String driverClassName = ResourceBundle.getBundle("jdbc").getString("driver");
Class c = Class.forName(driverClassName);
JDBC jdbc = (JDBC)c.newInstance();
jdbc.getConnection();
```
