# DeptDao.java

```java
package com.jkweilai.servlet.dao;  
  
import com.jkweilai.servlet.entity.Dept;  
  
import java.util.List;  
  
public interface DeptDao {  
    int insert(Dept dept);  
    int deleteById(Integer deptno);  
    int update(Dept dept);  
    Dept selectById(Integer deptno);  
    List<Dept> selectAll();  
    Integer selectMaxId();  
}
```