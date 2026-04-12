# eq记录

<https://www.easy-query.com/easy-query-doc/startup/quick-start.html>

---
## 数据准备

pom.xml
```xml
<?xml version="1.0" encoding="UTF-8"?>  
<project xmlns="http://maven.apache.org/POM/4.0.0"  
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"  
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">  
    <modelVersion>4.0.0</modelVersion>  
  
    <groupId>top.charles</groupId>  
    <artifactId>test</artifactId>  
    <version>1.0-SNAPSHOT</version>  
  
    <properties>  
        <maven.compiler.source>8</maven.compiler.source>  
        <maven.compiler.target>8</maven.compiler.target>  
        <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>  
        <!-- 请永远使用最新版 -->  
        <easy-query.version>3.1.27</easy-query.version>  
        <hikari.version>3.3.1</hikari.version>  
        <mysql.version>9.2.0</mysql.version>  
        <lombok.version>1.18.40</lombok.version>  
    </properties>  
    <dependencies>  
  
    <!-- 引入eq核心依赖 -->  
    <dependency>  
        <groupId>com.easy-query</groupId>  
        <artifactId>sql-api-proxy</artifactId>  
        <version>${easy-query.version}</version>  
    </dependency>  
    <!-- 按需引入eq的数据库方言支持依赖 -->  
    <dependency>  
        <groupId>com.easy-query</groupId>  
        <artifactId>sql-mysql</artifactId>  
        <version>${easy-query.version}</version>  
    </dependency>  
    <!-- 引入支持eq的APT依赖 -->  
    <dependency>  
        <groupId>com.easy-query</groupId>  
        <artifactId>sql-processor</artifactId>  
        <version>${easy-query.version}</version>  
    </dependency>  
    <!-- 引入数据源 -->  
    <!-- https://mvnrepository.com/artifact/com.zaxxer/HikariCP -->    
    <dependency>  
        <groupId>com.zaxxer</groupId>  
        <artifactId>HikariCP</artifactId>  
        <version>${hikari.version}</version>  
    </dependency>  
    <!-- 引入需要的数据库驱动 -->  
    <!-- https://mvnrepository.com/artifact/com.mysql/mysql-connector-j -->    
    <dependency>  
        <groupId>com.mysql</groupId>  
        <artifactId>mysql-connector-j</artifactId>  
        <version>${mysql.version}</version>  
    </dependency>  
    <!-- https://mvnrepository.com/artifact/org.projectlombok/lombok -->  
    <dependency>  
        <groupId>org.projectlombok</groupId>  
        <artifactId>lombok</artifactId>  
        <version>${lombok.version}</version>  
        <scope>provided</scope>  
    </dependency>  
</dependencies>  
  
</project>
```

实体类
```java
package top.charles.entity;  
  
import com.easy.query.core.annotation.Column;  
import com.easy.query.core.annotation.EntityProxy;  
import com.easy.query.core.annotation.Table;  
import com.easy.query.core.proxy.ProxyEntityAvailable;  
import lombok.AllArgsConstructor;  
import lombok.Data;  
import lombok.NoArgsConstructor;  
import top.charles.entity.proxy.CompanyProxy;  
  
import java.math.BigDecimal;  
import java.time.LocalDateTime;  
  
@Data  
@Table("t_company")  
@EntityProxy  
@AllArgsConstructor  
@NoArgsConstructor  
public class Company implements ProxyEntityAvailable<Company , CompanyProxy> {  
    /**  
     * 企业id  
     */    @Column(primaryKey = true)  
    private String id;  
    /**  
     * 企业名称  
     */  
    private String name;  
  
    /**  
     * 企业创建时间  
     */  
    private LocalDateTime createTime;  
  
    /**  
     * 注册资金  
     */  
    private BigDecimal registerMoney;  
}
```

```java
package top.charles.entity;  
  
import com.easy.query.core.annotation.Column;  
import com.easy.query.core.annotation.EntityProxy;  
import com.easy.query.core.annotation.Table;  
import com.easy.query.core.proxy.ProxyEntityAvailable;  
import lombok.AllArgsConstructor;  
import lombok.Data;  
import lombok.NoArgsConstructor;  
import top.charles.entity.proxy.SysUserProxy;  
  
import java.time.LocalDateTime;  
  
@Data  
@Table("t_user")  
@EntityProxy  
@AllArgsConstructor  
@NoArgsConstructor  
public class SysUser implements ProxyEntityAvailable<SysUser , SysUserProxy> {  
    /**  
     * 用户id  
     */    @Column(primaryKey = true)  
    private String id;  
    /**  
     * 用户姓名  
     */  
    private String name;  
    /**  
     * 用户出生日期  
     */  
    private LocalDateTime birthday;  
  
    /**  
     * 用户所属企业id  
     */    private String companyId;  
  
}
```

建好数据库，什么别的都不用做
```sql
CREATE DATABASE eq_db;
```

使用下边代码初始化数据库，建立对应的表，创建数据
```java
package top.charles;  
  
import com.easy.query.api.proxy.client.DefaultEasyEntityQuery;  
import com.easy.query.api.proxy.client.EasyEntityQuery;  
import top.charles.entity.Company;  
import top.charles.entity.SysUser;  
import com.easy.query.core.api.client.EasyQueryClient;  
import com.easy.query.core.basic.api.database.CodeFirstCommand;  
import com.easy.query.core.basic.api.database.DatabaseCodeFirst;  
import com.easy.query.core.bootstrapper.EasyQueryBootstrapper;  
import com.easy.query.core.logging.LogFactory;  
import com.easy.query.mysql.config.MySQLDatabaseConfiguration;  
import com.zaxxer.hikari.HikariDataSource;  
  
import javax.sql.DataSource;  
import java.math.BigDecimal;  
import java.time.LocalDateTime;  
import java.util.Arrays;  
import java.util.List;  
  
public class BaseTest {  
    protected static EasyEntityQuery entityQuery;  
  
    static {  
        LogFactory.useStdOutLogging();  
        DataSource dataSource = getDataSource();  
        EasyQueryClient client = EasyQueryBootstrapper.defaultBuilderConfiguration()  
                .setDefaultDataSource(dataSource)  
                .optionConfigure(op -> {  
                    //进行一系列可以选择的配置  
                    //op.setPrintSql(true);  
                })  
                .useDatabaseConfigure(new MySQLDatabaseConfiguration())  
                .build();  
        entityQuery = new DefaultEasyEntityQuery(client);  
    }  
  
    public static void initTables() {  
  
        DatabaseCodeFirst databaseCodeFirst = entityQuery.getDatabaseCodeFirst();  
        //如果不存在数据库则创建  
        databaseCodeFirst.createDatabaseIfNotExists();  
        //自动同步数据库表  
        CodeFirstCommand codeFirstCommand = databaseCodeFirst.syncTableCommand(Arrays.asList(Company.class, SysUser.class));  
        //执行命令  
        codeFirstCommand.executeWithTransaction(arg->{  
            System.out.println(arg.getSQL());  
            arg.commit();  
        });  
    }  
  
    public static void initData() {  
        clearTestData();  
  
        List<Company> companies = Arrays.asList(  
                // id, 名称, 成立时间, 注册资金  
                new Company("1", "腾讯", LocalDateTime.of(2010, 1, 15, 10, 30), new BigDecimal("1000.00")),  
                new Company("2", "阿里巴巴", LocalDateTime.of(2012, 3, 20, 14, 15), new BigDecimal("500.00")),  
                new Company("3", "百度", LocalDateTime.of(2011, 5, 10, 9, 0), new BigDecimal("200.00")),  
                new Company("4", "字节跳动", LocalDateTime.of(2018, 8, 8, 16, 45), new BigDecimal("300.00")),  
                new Company("5", "华为", LocalDateTime.of(2005, 12, 25, 8, 0), new BigDecimal("2000.00")),  
                new Company("6", "小米", LocalDateTime.of(2013, 7, 7, 11, 30), new BigDecimal("100.00")),  
                new Company("7", "京东", LocalDateTime.of(2014, 9, 9, 15, 20), new BigDecimal("150.00")),  
                new Company("8", "美团", LocalDateTime.of(2015, 10, 10, 13, 10), new BigDecimal("80.00")),  
                new Company("9", "拼多多", LocalDateTime.of(2017, 11, 11, 12, 0), new BigDecimal("50.00")),  
                new Company("10", "网易", LocalDateTime.of(2009, 6, 6, 9, 45), new BigDecimal("120.00"))  
        );  
  
        for (Company company : companies) {  
            entityQuery.insertable(company).executeRows();  
        }  
  
        System.out.println("✅ 初始化公司数据完成，共" + companies.size() + "条");  
  
        // 初始化用户数据  
        List<SysUser> users = Arrays.asList(  
                // id, name, birthday, companyId  
                new SysUser("101", "张三", LocalDateTime.of(1990, 3, 10, 0, 0), "1"),  
                new SysUser("102", "李四", LocalDateTime.of(1992, 5, 20, 0, 0), "1"),  
                new SysUser("103", "王五", LocalDateTime.of(1988, 7, 15, 0, 0), "2"),  
                new SysUser("104", "赵六", LocalDateTime.of(1995, 9, 5, 0, 0), "3"),  
                new SysUser("105", "钱七", LocalDateTime.of(1993, 11, 20, 0, 0), "4"),  
                new SysUser("106", "孙八", LocalDateTime.of(1991, 2, 14, 0, 0), "5"),  
                new SysUser("107", "周九", LocalDateTime.of(1994, 4, 18, 0, 0), "6"),  
                new SysUser("108", "吴十", LocalDateTime.of(1996, 6, 22, 0, 0), "7"),  
                new SysUser("109", "郑十一", LocalDateTime.of(1997, 8, 30, 0, 0), "8"),  
                new SysUser("110", "王十二", LocalDateTime.of(1998, 10, 12, 0, 0), "9")  
        );  
  
        for (SysUser user : users) {  
            entityQuery.insertable(user).executeRows();  
        }  
  
        System.out.println("✅ 初始化用户数据完成，共" + users.size() + "条");  
    }  
  
    private static void clearTestData() {  
        try {  
            // 1. 删除所有用户（外键依赖公司）  
            Long userCount = entityQuery.queryable(SysUser.class).count();  
            if (userCount > 0) {  
                entityQuery.deletable(SysUser.class)  
                        .where(u -> u.companyId().isNotNull())  // 加个条件  
                        .disableLogicDelete()  
                        .allowDeleteStatement(true)  
                        .executeRows();  
                System.out.println("删除用户: " + userCount + " 条");  
            }  
  
            // 2. 删除所有公司  
            Long companyCount = entityQuery.queryable(Company.class).count();  
            if (companyCount > 0) {  
                entityQuery.deletable(Company.class)  
                        .where(c -> c.id().isNotNull())  // 加个条件  
                        .disableLogicDelete()  
                        .allowDeleteStatement(true)  
                        .executeRows();  
                System.out.println("删除公司: " + companyCount + " 条");  
            }  
  
            System.out.println("✅ 清表完成");  
        } catch (Exception e) {  
            System.err.println("❌ 清表失败：" + e.getMessage());  
        }  
    }  
  
    public static void main(String[] args) {  
        initTables();  
        initData();  
    }  
  
    /**  
     * 初始化数据源  
     * @return  
     */  
    private static DataSource getDataSource(){  
        HikariDataSource dataSource = new HikariDataSource();  
        dataSource.setJdbcUrl("jdbc:mysql://127.0.0.1:3306/eq_db?characterEncoding=utf-8&useSSL=false&allowMultiQueries=true&rewriteBatchedStatements=true");  
        dataSource.setUsername("root");  
        dataSource.setPassword("");  
        dataSource.setDriverClassName("com.mysql.cj.jdbc.Driver");  
        dataSource.setMaximumPoolSize(20);  
  
        return dataSource;  
    }  
}
```

---
## 单表查询

<https://www.easy-query.com/easy-query-doc/ability/select/query-bean.html>

```java

```