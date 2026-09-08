# DeptDetailServlet

```java
package com.jkweilai.servlet;  
  
import com.jkweilai.servlet.dao.DeptDao;  
import com.jkweilai.servlet.dao.impl.DeptDaoImpl;  
import com.jkweilai.servlet.entity.Dept;  
import jakarta.servlet.ServletException;  
import jakarta.servlet.annotation.WebServlet;  
import jakarta.servlet.http.HttpServlet;  
import jakarta.servlet.http.HttpServletRequest;  
import jakarta.servlet.http.HttpServletResponse;  
  
import java.io.IOException;  
import java.io.PrintWriter;  
  
@WebServlet("/api/detail")  
public class DeptDetailServlet extends HttpServlet {  
  
    private final DeptDao deptDao = new DeptDaoImpl();  
  
    @Override  
    protected void doGet(HttpServletRequest request, HttpServletResponse response)  
            throws ServletException, IOException {  
  
        response.setContentType("application/json;charset=UTF-8");  
        String deptnoStr = request.getParameter("deptno");  
  
        try (PrintWriter out = response.getWriter()) {  
            if (deptnoStr == null || deptnoStr.isEmpty()) {  
                out.print("{\"error\":\"Missing deptno\"}");  
                return;  
            }            
            int deptno = Integer.parseInt(deptnoStr);  
            Dept dept = deptDao.selectById(deptno);  
            if (dept == null) {  
                out.print("{\"error\":\"Department not found\"}");  
            } else {  
                out.printf("{\"deptno\":%d,\"dname\":\"%s\",\"loc\":\"%s\"}",  
                        dept.getDeptno(), dept.getDname(), dept.getLoc());  
            }        
        } catch (NumberFormatException e) {  
            response.getWriter().print("{\"error\":\"Invalid deptno\"}");  
        } catch (Exception e) {  
            e.printStackTrace();  
            response.setStatus(HttpServletResponse.SC_INTERNAL_SERVER_ERROR);  
            response.getWriter().print("{\"error\":\"Internal server error\"}");  
        }    
    }
}
```