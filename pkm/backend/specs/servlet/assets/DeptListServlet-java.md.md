# DeptListServlet

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
import java.util.List;
import java.util.stream.Collectors;

@WebServlet("/api/list")
public class DeptListServlet extends HttpServlet {

    private final DeptDao deptDao = new DeptDaoImpl();

    @Override
    protected void doGet(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {

        response.setContentType("application/json;charset=UTF-8");

        try (PrintWriter out = response.getWriter()) {
            List<Dept> list = deptDao.selectAll();
            if (list == null || list.isEmpty()) {
                out.print("[]");
                return;
            }
            String json = list.stream()
                    .map(d -> "{\"deptno\":" + d.getDeptno() +
                            ",\"dname\":\"" + d.getDname() +
                            "\",\"loc\":\"" + d.getLoc() + "\"}")
                    .collect(Collectors.joining(",", "[", "]"));
            out.print(json);
        } catch (Exception e) {
            e.printStackTrace();
            response.setStatus(HttpServletResponse.SC_INTERNAL_SERVER_ERROR);
            response.getWriter().print("{\"error\":\"Internal server error\"}");
        }
    }
}
```

