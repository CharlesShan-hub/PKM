![](https://cdn.nlark.com/yuque/0/2023/jpeg/21376908/1692002570088-3338946f-42b3-4174-8910-7e749c31e950.jpeg#averageHue=%23f9f8f8&from=url&id=O8j9i&originHeight=78&originWidth=1400&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=shadow&title=)
# 什么是DAO
DAO是：Data Access Object，翻译为：数据访问对象。
一种JavaEE的设计模式，专门用来做数据增删改查的类。
在实际的开发中，通常我们会将数据库的操作封装为一个单独的DAO去完成，这样做的目的是：提高代码的复用性，另外也可以降低程序的耦合度，提高扩展力。
例如：操作用户数据的叫做UserDao，操作员工数据的叫做EmployeeDao，操作产品数据的叫做ProductDao，操作订单数据的叫做OrderDao等。

![](https://cdn.nlark.com/yuque/0/2023/jpeg/21376908/1692002570088-3338946f-42b3-4174-8910-7e749c31e950.jpeg#averageHue=%23f9f8f8&from=url&id=B8M6O&originHeight=78&originWidth=1400&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=shadow&title=)
# 使用DAO改造员工信息管理
## 定义Employee封装数据
Employee类是一个Java Bean，专门用来封装员工的信息：
```java
package com.powernode.jdbc.beans;

/**
 * ClassName: Employee
 * Description:
 * Datetime: 2024/4/14 23:32
 * Author: 老杜@动力节点
 * Version: 1.0
 */
public class Employee {
    private Long id;
    private String name;
    private String job;
    private Double salary;
    private String hiredate;
    private String address;

    @Override
    public String toString() {
        return "Employee{" +
                "id=" + id +
                ", name='" + name + '\'' +
                ", job='" + job + '\'' +
                ", salary=" + salary +
                ", hiredate='" + hiredate + '\'' +
                ", address='" + address + '\'' +
                '}';
    }

    public Employee() {
    }

    public Employee(Long id, String name, String job, Double salary, String hiredate, String address) {
        this.id = id;
        this.name = name;
        this.job = job;
        this.salary = salary;
        this.hiredate = hiredate;
        this.address = address;
    }

    public Long getId() {
        return id;
    }

    public void setId(Long id) {
        this.id = id;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getJob() {
        return job;
    }

    public void setJob(String job) {
        this.job = job;
    }

    public Double getSalary() {
        return salary;
    }

    public void setSalary(Double salary) {
        this.salary = salary;
    }

    public String getHiredate() {
        return hiredate;
    }

    public void setHiredate(String hiredate) {
        this.hiredate = hiredate;
    }

    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }
}

```
![](https://cdn.nlark.com/yuque/0/2023/jpeg/21376908/1692002570088-3338946f-42b3-4174-8910-7e749c31e950.jpeg#averageHue=%23f9f8f8&from=url&id=ZQhjT&originHeight=78&originWidth=1400&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=shadow&title=)
## 定义EmployeeDao
定义五个方法，分别完成五个功能：新增，修改，删除，查看一个，查看所有。
```java
package com.powernode.jdbc.dao;

import com.powernode.jdbc.beans.Employee;
import com.powernode.jdbc.utils.DbUtils;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.ArrayList;
import java.util.List;

/**
 * ClassName: EmployeeDao
 * Description:
 * Datetime: 2024/4/14 23:34
 * Author: 老杜@动力节点
 * Version: 1.0
 */
public class EmployeeDao {
    /**
     * 新增员工
     * @param employee
     * @return
     */
    public int insert(Employee employee) {
        Connection conn = null;
        PreparedStatement ps = null;
        int count = 0;
        try {
            conn = DbUtils.getConnection();
            String sql = "insert into t_employee(name,job,salary,hiredate,address) values(?,?,?,?,?)";
            ps = conn.prepareStatement(sql);
            ps.setString(1, employee.getName());
            ps.setString(2, employee.getJob());
            ps.setDouble(3, employee.getSalary());
            ps.setString(4, employee.getHiredate());
            ps.setString(5, employee.getAddress());
            count = ps.executeUpdate();
        } catch (SQLException e) {
            throw new RuntimeException(e);
        } finally {
            DbUtils.close(conn, ps, null);
        }
        return count;
    }

    /**
     * 修改员工
     * @param employee
     * @return
     */
    public int update(Employee employee){
        Connection conn = null;
        PreparedStatement ps = null;
        int count = 0;
        try {
            conn = DbUtils.getConnection();
            String sql = "update t_employee set name=?, job=?, salary=?, hiredate=?, address=? where id=?";
            ps = conn.prepareStatement(sql);
            ps.setString(1, employee.getName());
            ps.setString(2, employee.getJob());
            ps.setDouble(3, employee.getSalary());
            ps.setString(4, employee.getHiredate());
            ps.setString(5, employee.getAddress());
            ps.setLong(6, employee.getId());
            count = ps.executeUpdate();
        } catch (SQLException e) {
            throw new RuntimeException(e);
        } finally {
            DbUtils.close(conn, ps, null);
        }
        return count;
    }

    /**
     * 根据id删除员工信息
     * @param id 员工id
     * @return 1表示成功
     */
    public int deleteById(Long id){
        Connection conn = null;
        PreparedStatement ps = null;
        int count = 0;
        try {
            conn = DbUtils.getConnection();
            String sql = "delete from t_employee where id = ?";
            ps = conn.prepareStatement(sql);
            ps.setLong(1, id);
            count = ps.executeUpdate();
        } catch (SQLException e) {
            throw new RuntimeException(e);
        } finally {
            DbUtils.close(conn, ps, null);
        }
        return count;
    }

    /**
     * 根据id查询所有员工
     * @param id
     * @return
     */
    public Employee selectById(Long id){
        Connection conn = null;
        PreparedStatement ps = null;
        ResultSet rs = null;
        Employee employee = null;
        try {
            conn = DbUtils.getConnection();
            String sql = "select * from t_employee where id = ?";
            ps = conn.prepareStatement(sql);
            ps.setLong(1, id);
            rs = ps.executeQuery();
            if(rs.next()){
                employee = new Employee();
                employee.setId(id);
                employee.setName(rs.getString("name"));
                employee.setJob(rs.getString("job"));
                employee.setSalary(rs.getDouble("salary"));
                employee.setHiredate(rs.getString("hiredate"));
                employee.setAddress(rs.getString("address"));
            }
        } catch (SQLException e) {
            throw new RuntimeException(e);
        } finally {
            DbUtils.close(conn, ps, rs);
        }
        return employee;
    }

    /**
     * 查询所有员工信息
     * @return 员工列表
     */
    public List<Employee> selectAll(){
        List<Employee> employees = new ArrayList<>();
        Connection conn = null;
        PreparedStatement ps = null;
        ResultSet rs = null;
        try {
            conn = DbUtils.getConnection();
            String sql = "select * from t_employee";
            ps = conn.prepareStatement(sql);
            rs = ps.executeQuery();
            while(rs.next()){
                Employee employee = new Employee();
                employee.setId(rs.getLong("id"));
                employee.setName(rs.getString("name"));
                employee.setJob(rs.getString("job"));
                employee.setSalary(rs.getDouble("salary"));
                employee.setHiredate(rs.getString("hiredate"));
                employee.setAddress(rs.getString("address"));
                employees.add(employee);
            }
        } catch (SQLException e) {
            throw new RuntimeException(e);
        } finally {
            DbUtils.close(conn, ps, rs);
        }
        return employees;
    }
}
```
![](https://cdn.nlark.com/yuque/0/2023/jpeg/21376908/1692002570088-3338946f-42b3-4174-8910-7e749c31e950.jpeg#averageHue=%23f9f8f8&from=url&id=QuvZJ&originHeight=78&originWidth=1400&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=shadow&title=)
# BaseDao的封装
```java
package com.powernode.jdbc.dao;

import com.powernode.jdbc.utils.DbUtils;

import java.lang.reflect.Field;
import java.sql.*;
import java.util.ArrayList;
import java.util.List;

/**
 * ClassName: BaseDao
 * Description: 最基础的Dao，所有的Dao应该去继承该BaseDao
 * Datetime: 2024/4/15 11:08
 * Author: 老杜@动力节点
 * Version: 1.0
 */
public class BaseDao {

    /**
     * 这是一个通用的执行insert delete update语句的方法。
     * @param sql
     * @param params
     * @return
     */
    public int executeUpdate(String sql, Object... params) {
        Connection conn = null;
        PreparedStatement ps = null;
        int count = 0;
        try {
            // 获取连接
            conn = DbUtils.getConnection();
            // 获取预编译的数据库操作对象
            ps = conn.prepareStatement(sql);
            // 给 ? 占位符传值
            if(params != null && params.length > 0){
                // 有占位符 ?
                for (int i = 0; i < params.length; i++) {
                    ps.setObject(i + 1, params[i]);
                }
            }
            // 执行SQL语句
            count = ps.executeUpdate();
        } catch (SQLException e) {
            throw new RuntimeException(e);
        } finally {
            DbUtils.close(conn, ps, null);
        }
        return count;
    }

    /**
     * 这是一个通用的查询语句
     * @param clazz
     * @param sql
     * @param params
     * @return
     * @param <T>
     */
    public <T> List<T> executeQuery(Class<T> clazz, String sql, Object... params){
        List<T> list = new ArrayList<>();
        Connection conn = null;
        PreparedStatement ps = null;
        ResultSet rs = null;
        try {
            // 获取连接
            conn = DbUtils.getConnection();
            // 获取预编译的数据库操作对象
            ps = conn.prepareStatement(sql);
            // 给?传值
            if(params != null && params.length > 0){
                for (int i = 0; i < params.length; i++) {
                    ps.setObject(i + 1, params[i]);
                }
            }
            // 执行SQL语句
            rs = ps.executeQuery();

            // 获取查询结果集元数据
            ResultSetMetaData rsmd = rs.getMetaData();

            // 获取列数
            int columnCount = rsmd.getColumnCount();

            // 处理查询结果集
            while(rs.next()){
                // 封装bean对象
                T obj = clazz.newInstance();
                // 给bean对象属性赋值
                /*
                比如现在有一张表：t_user，然后表中有两个字段，一个是 user_id，一个是user_name
                现在javabean是User类，该类中的属性名是：userId,username
                执行这样的SQL语句：select user_id as userId, user_name as username from t_user;
                 */
                for (int i = 1; i <= columnCount; i++) {
                    // 获取查询结果集中的列的名字
                    // 这个列的名字是通过as关键字进行了起别名，这个列名就是bean的属性名。
                    String fieldName = rsmd.getColumnLabel(i);
                    // 获取属性Field对象
                    Field declaredField = clazz.getDeclaredField(fieldName);
                    // 打破封装
                    declaredField.setAccessible(true);
                    // 给属性赋值
                    declaredField.set(obj, rs.getObject(i));
                }

                // 将对象添加到List集合
                list.add(obj);
            }
        } catch (Exception e) {
            throw new RuntimeException(e);
        } finally {
            DbUtils.close(conn, ps, rs);
        }
        // 返回List集合
        return list;
    }


    /**
     *
     * @param clazz
     * @param sql
     * @param params
     * @return
     * @param <T>
     */
    public <T> T queryOne(Class<T> clazz, String sql, Object... params){
        List<T> list = executeQuery(clazz, sql, params);
        if(list == null || list.size() == 0){
            return null;
        }
        return list.get(0);
    }

}

```
![](https://cdn.nlark.com/yuque/0/2023/jpeg/21376908/1692002570088-3338946f-42b3-4174-8910-7e749c31e950.jpeg#averageHue=%23f9f8f8&from=url&id=sQZNC&originHeight=78&originWidth=1400&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=shadow&title=)
