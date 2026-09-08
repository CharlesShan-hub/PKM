# DeptDeleteServlet

```java
package com.jkweilai.servlet;

import com.jkweilai.servlet.dao.DeptDao;
import com.jkweilai.servlet.dao.impl.DeptDaoImpl;
import jakarta.servlet.ServletException;
import jakarta.servlet.annotation.WebServlet;
import jakarta.servlet.http.HttpServlet;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

import java.io.IOException;
import java.io.PrintWriter;

@WebServlet("/api/delete")
public class DeptDeleteServlet extends HttpServlet {

    private final DeptDao deptDao = new DeptDaoImpl();

    @Override
    protected void doPost(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {

        response.setContentType("text/plain;charset=UTF-8");

        try (PrintWriter out = response.getWriter()) {
            String deptnoStr = request.getParameter("deptno");
            if (deptnoStr == null || deptnoStr.isEmpty()) {
                out.print("Missing deptno");
                return;
            }

            int deptno = Integer.parseInt(deptnoStr);
            int rows = deptDao.deleteById(deptno);
            out.print(rows > 0 ? "Department deleted successfully" : "Delete failed");
        } catch (NumberFormatException e) {
            response.getWriter().print("Invalid department number");
        } catch (Exception e) {
            e.printStackTrace();
            response.getWriter().print("System error");
        }
    }
}
```