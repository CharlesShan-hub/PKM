# DeptDaoImpl.java

```java
package com.jkweilai.servlet.dao.impl;  
  
import com.jkweilai.servlet.dao.DeptDao;  
import com.jkweilai.servlet.entity.Dept;  
import com.jkweilai.servlet.util.DbUtils;  
  
import java.sql.Connection;  
import java.sql.PreparedStatement;  
import java.sql.ResultSet;  
import java.sql.SQLException;  
import java.util.ArrayList;  
import java.util.List;  
  
public class DeptDaoImpl implements DeptDao {  
  
    private static final String SQL_INSERT = "INSERT INTO dept (deptno, dname, loc) VALUES (?, ?, ?)";  
    private static final String SQL_DELETE = "DELETE FROM dept WHERE deptno = ?";  
    private static final String SQL_UPDATE = "UPDATE dept SET dname = ?, loc = ? WHERE deptno = ?";  
    private static final String SQL_SELECT_BY_ID = "SELECT deptno, dname, loc FROM dept WHERE deptno = ?";  
    private static final String SQL_SELECT_ALL = "SELECT deptno, dname, loc FROM dept ORDER BY deptno";  
    private static final String SQL_SELECT_MAX_ID = "SELECT MAX(deptno) FROM dept";  
  
    @Override  
    public int insert(Dept dept) {  
        Connection conn = null;  
        PreparedStatement pst = null;  
        try {  
            conn = DbUtils.getConnection();  
            pst = conn.prepareStatement(SQL_INSERT);  
            pst.setInt(1, dept.getDeptno());  
            pst.setString(2, dept.getDname());  
            pst.setString(3, dept.getLoc());  
            return pst.executeUpdate();  
        } catch (SQLException e) {  
            e.printStackTrace();  
            return 0;  
        } finally {  
            DbUtils.close(conn, pst, null);  
        }  
    }  
  
    @Override  
    public int deleteById(Integer deptno) {  
        Connection conn = null;  
        PreparedStatement pst = null;  
        try {  
            conn = DbUtils.getConnection();  
            pst = conn.prepareStatement(SQL_DELETE);  
            pst.setInt(1, deptno);  
            return pst.executeUpdate();  
        } catch (SQLException e) {  
            e.printStackTrace();  
            return 0;  
        } finally {  
            DbUtils.close(conn, pst, null);  
        }  
    }  
  
    @Override  
    public int update(Dept dept) {  
        Connection conn = null;  
        PreparedStatement pst = null;  
        try {  
            conn = DbUtils.getConnection();  
            pst = conn.prepareStatement(SQL_UPDATE);  
            pst.setString(1, dept.getDname());  
            pst.setString(2, dept.getLoc());  
            pst.setInt(3, dept.getDeptno());  
            return pst.executeUpdate();  
        } catch (SQLException e) {  
            e.printStackTrace();  
            return 0;  
        } finally {  
            DbUtils.close(conn, pst, null);  
        }  
    }  
  
    @Override  
    public Dept selectById(Integer deptno) {  
        Connection conn = null;  
        PreparedStatement pst = null;  
        ResultSet rs = null;  
        try {  
            conn = DbUtils.getConnection();  
            pst = conn.prepareStatement(SQL_SELECT_BY_ID);  
            pst.setInt(1, deptno);  
            rs = pst.executeQuery();  
            if (rs.next()) {  
                Dept dept = new Dept();  
                dept.setDeptno(rs.getInt("deptno"));  
                dept.setDname(rs.getString("dname"));  
                dept.setLoc(rs.getString("loc"));  
                return dept;  
            }  
            return null;  
        } catch (SQLException e) {  
            e.printStackTrace();  
            return null;  
        } finally {  
            DbUtils.close(conn, pst, rs);  
        }  
    }  
  
    @Override  
    public List<Dept> selectAll() {  
        Connection conn = null;  
        PreparedStatement pst = null;  
        ResultSet rs = null;  
        List<Dept> list = new ArrayList<>();  
        try {  
            conn = DbUtils.getConnection();  
            pst = conn.prepareStatement(SQL_SELECT_ALL);  
            rs = pst.executeQuery();  
            while (rs.next()) {  
                Dept dept = new Dept();  
                dept.setDeptno(rs.getInt("deptno"));  
                dept.setDname(rs.getString("dname"));  
                dept.setLoc(rs.getString("loc"));  
                list.add(dept);  
            }  
            return list;  
        } catch (SQLException e) {  
            e.printStackTrace();  
            return list;  
        } finally {  
            DbUtils.close(conn, pst, rs);  
        }  
    }  
  
    @Override  
    public Integer selectMaxId() {  
        Connection conn = null;  
        PreparedStatement pst = null;  
        ResultSet rs = null;  
        try {  
            conn = DbUtils.getConnection();  
            pst = conn.prepareStatement(SQL_SELECT_MAX_ID);  
            rs = pst.executeQuery();  
            if (rs.next()) {  
                return rs.getInt(1);  
            }  
            return 0;  
        } catch (SQLException e) {  
            e.printStackTrace();  
            return 0;  
        } finally {  
            DbUtils.close(conn, pst, rs);  
        }  
    }  
}
```