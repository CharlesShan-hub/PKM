# DeptInsertServler.java

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

@WebServlet("/insert")
public class DeptInsertServlet extends HttpServlet {

    private final DeptDao deptDao = new DeptDaoImpl();

    @Override
    protected void doPost(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {

        // Set encoding to avoid Chinese garbled text
        request.setCharacterEncoding("UTF-8");
        response.setContentType("text/html;charset=UTF-8");

        String deptnoStr = request.getParameter("deptno");
        String dname = request.getParameter("dname");
        String loc = request.getParameter("loc");

        // Simple validation: all fields are required
        if (deptnoStr == null || deptnoStr.trim().isEmpty() ||
            dname == null || dname.trim().isEmpty() ||
            loc == null || loc.trim().isEmpty()) {

            try (PrintWriter out = response.getWriter()) {
                out.print("<h3 style='color:red;'>All fields are required!</h3>");
                out.print("<a href='javascript:history.back()'>Go Back</a>");
            }
            return;
        }

        try {
            int deptno = Integer.parseInt(deptnoStr);

            Dept dept = new Dept();
            dept.setDeptno(deptno);
            dept.setDname(dname);
            dept.setLoc(loc);

            int rows = deptDao.insert(dept);

            if (rows > 0) {
                // Insert successful, redirect to list page
                response.sendRedirect(request.getContextPath() + "/list");
            } else {
                // Insert failed, likely due to duplicate primary key
                try (PrintWriter out = response.getWriter()) {
                    out.print("<h3 style='color:red;'>Insert failed. Department number may already exist!</h3>");
                    out.print("<a href='javascript:history.back()'>Go Back</a>");
                }
            }

        } catch (NumberFormatException e) {
            try (PrintWriter out = response.getWriter()) {
                out.print("<h3 style='color:red;'>Department number must be a valid integer!</h3>");
                out.print("<a href='javascript:history.back()'>Go Back</a>");
            }
        } catch (Exception e) {
            e.printStackTrace();
            try (PrintWriter out = response.getWriter()) {
                out.print("<h3 style='color:red;'>System error. Please try again later.</h3>");
                out.print("<a href='javascript:history.back()'>Go Back</a>");
            }
        }
    }
}
```