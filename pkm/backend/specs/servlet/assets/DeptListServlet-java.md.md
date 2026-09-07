# DeptListServlet

```java
package com.jkweilai.servlet;

import jakarta.servlet.ServletException;
import jakarta.servlet.annotation.WebServlet;
import jakarta.servlet.http.HttpServlet;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.io.IOException;
import java.io.PrintWriter;
import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;

@WebServlet("/list")
public class DeptListServlet extends HttpServlet {

    // ========== HTML Template Constants ==========
    private static final String HTML_HEAD = """
            <!DOCTYPE html>
            <html lang="zh-CN">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>Department Management - List</title>
                <style>
                    * { margin: 0; padding: 0; box-sizing: border-box; font-family: 'Arial', sans-serif; }
                    body { background-color: #f5f5f5; }
                    .container { max-width: 1200px; margin: 0 auto; padding: 20px; }
                    .header { display: flex; justify-content: space-between; align-items: center; margin-bottom: 30px; }
                    .header h1 { color: #333; font-size: 24px; }
                    .add-btn { padding: 10px 20px; background-color: #4a90e2; color: white; border: none; border-radius: 4px; cursor: pointer; text-decoration: none; font-size: 14px; transition: background-color 0.3s; }
                    .add-btn:hover { background-color: #3a7bc8; }
                    .department-table { width: 100%; border-collapse: collapse; background-color: white; box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1); border-radius: 4px; overflow: hidden; }
                    .department-table th, .department-table td { padding: 15px; text-align: left; border-bottom: 1px solid #eee; }
                    .department-table th { background-color: #f8f9fa; font-weight: 600; color: #555; }
                    .department-table tr:hover { background-color: #f8f9fa; }
                    .action-btn { padding: 6px 12px; margin-right: 5px; border: none; border-radius: 4px; cursor: pointer; font-size: 13px; transition: all 0.3s; text-decoration: none; display: inline-block; }
                    .view-btn { background-color: #5cb85c; color: white; }
                    .view-btn:hover { background-color: #4cae4c; }
                    .edit-btn { background-color: #f0ad4e; color: white; }
                    .edit-btn:hover { background-color: #eea236; }
                    .delete-btn { background-color: #d9534f; color: white; }
                    .delete-btn:hover { background-color: #d43f3a; }
                    .logout { text-align: right; margin-top: 20px; }
                    .logout a { color: #777; text-decoration: none; font-size: 14px; }
                    .logout a:hover { color: #333; }
                </style>
            </head>
            <body>
                <div class="container">
                    <div class="header">
                        <h1>Department List</h1>
                        <a href="" class="add-btn">+ Add Department</a>
                    </div>
                    <table class="department-table">
                        <thead>
                            <tr>
                                <th>Dept No.</th>
                                <th>Department Name</th>
                                <th>Location</th>
                                <th>Actions</th>
                            </tr>
                        </thead>
                        <tbody>
            """;

    private static final String HTML_ROW = """
                    <tr>
                        <td>%s</td>
                        <td>%s</td>
                        <td>%s</td>
                        <td>
                            <a href='' class='action-btn view-btn'>View</a>
                            <a href='' class='action-btn edit-btn'>Edit</a>
                            <a href='' class='action-btn delete-btn'>Delete</a>
                        </td>
                    </tr>
            """;

    private static final String HTML_TAIL = """
                        </tbody>
                    </table>
                    <div class="logout">
                        <a href="">Logout</a>
                    </div>
                </div>
            </body>
            </html>
            """;

    // ========== SQL Constants ==========
    private static final String SQL_SELECT_DEPT = "SELECT deptno, dname, loc FROM dept";

    // ========== Error Messages ==========
    private static final String ERROR_LOADING_DATA =
            "<tr><td colspan='4' style='color:red;text-align:center;'>Failed to load data, please try again later.</td></tr>";

    @Override
    protected void doGet(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {

        response.setContentType("text/html;charset=UTF-8");

        try (PrintWriter out = response.getWriter()) {
            out.print(HTML_HEAD);
            printDepartmentRows(out);
            out.print(HTML_TAIL);
        }
    }

    /**
     * Queries the database and prints department list rows.
     *
     * @param out the PrintWriter to write HTML output
     */
    private void printDepartmentRows(PrintWriter out) {
        Connection conn = null;
        PreparedStatement pst = null;
        ResultSet rs = null;

        try {
            conn = DbUtils.getConnection();
            pst = conn.prepareStatement(SQL_SELECT_DEPT);
            rs = pst.executeQuery();

            while (rs.next()) {
                String deptno = rs.getString("deptno");
                String dname = rs.getString("dname");
                String loc = rs.getString("loc");
                out.printf(HTML_ROW, deptno, dname, loc);
            }

        } catch (Exception e) {
            // Log the error for debugging
            e.printStackTrace();
            out.print(ERROR_LOADING_DATA);
        } finally {
            DbUtils.close(conn, pst, rs);
        }
    }
}
```