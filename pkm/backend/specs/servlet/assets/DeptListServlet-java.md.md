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

@WebServlet("/list")
public class DeptListServlet extends HttpServlet {

    private static final String HTML_HEAD = """
            <!DOCTYPE html>
            <html lang="zh-CN">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>Department Management</title>
                <style>
                    * { margin: 0; padding: 0; box-sizing: border-box; font-family: 'Arial', sans-serif; }
                    body { background-color: #f5f5f5; padding: 20px; }
                    .container { max-width: 1200px; margin: 0 auto; background: white; padding: 30px; border-radius: 8px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); }
                    .header { display: flex; justify-content: space-between; align-items: center; margin-bottom: 20px; }
                    .header h1 { color: #333; }
                    .add-btn { padding: 10px 20px; background-color: #4a90e2; color: white; border: none; border-radius: 4px; cursor: pointer; font-size: 14px; text-decoration: none; display: inline-block; }
                    .add-btn:hover { background-color: #3a7bc8; }
                    table { width: 100%; border-collapse: collapse; }
                    th, td { padding: 12px 15px; text-align: left; border-bottom: 1px solid #eee; }
                    th { background-color: #f8f9fa; font-weight: 600; color: #555; }
                    tr:hover { background-color: #f8f9fa; }
                    .action-btn { padding: 6px 12px; border: none; border-radius: 4px; cursor: pointer; font-size: 12px; text-decoration: none; display: inline-block; margin-right: 4px; }
                    .view-btn { background-color: #5cb85c; color: white; }
                    .edit-btn { background-color: #f0ad4e; color: white; }
                    .delete-btn { background-color: #d9534f; color: white; }
                    .modal { display: none; position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0,0,0,0.5); justify-content: center; align-items: center; z-index: 999; }
                    .modal-content { background: white; padding: 30px; border-radius: 8px; width: 400px; max-width: 90%; }
                    .modal-content h2 { margin-bottom: 20px; }
                    .modal-content label { display: block; margin: 10px 0 5px; font-weight: 600; }
                    .modal-content input { width: 100%; padding: 8px 12px; border: 1px solid #ccc; border-radius: 4px; }
                    .modal-content .btn-group { margin-top: 20px; display: flex; gap: 10px; justify-content: flex-end; }
                    .modal-content .btn-group button { padding: 8px 20px; border: none; border-radius: 4px; cursor: pointer; }
                    .btn-submit { background-color: #4a90e2; color: white; }
                    .btn-cancel { background-color: #ccc; color: #333; }
                    .toast { position: fixed; top: 20px; right: 20px; padding: 12px 24px; border-radius: 4px; color: white; font-weight: bold; z-index: 1000; display: none; }
                    .toast.success { background-color: #5cb85c; }
                    .toast.error { background-color: #d9534f; }
                </style>
            </head>
            <body>
                <div id="toast" class="toast"></div>
                <div class="container">
                    <div class="header">
                        <h1>Department List</h1>
                        <button class="add-btn" onclick="openModal('insert')">+ Add Department</button>
                    </div>
                    <table>
                        <thead>
                            <tr><th>Dept No.</th><th>Name</th><th>Location</th><th>Actions</th></tr>
                        </thead>
                        <tbody id="tableBody">
            """;

    private static final String HTML_ROW = """
                        <tr>
                            <td>%d</td>
                            <td>%s</td>
                            <td>%s</td>
                            <td>
                                <button class="action-btn view-btn" onclick="viewDept(%d)">View</button>
                                <button class="action-btn edit-btn" onclick="editDept(%d)">Edit</button>
                                <button class="action-btn delete-btn" onclick="deleteDept(%d)">Delete</button>
                            </td>
                        </tr>
            """;

    private static final String HTML_TAIL = """
                        </tbody>
                    </table>
                </div>

                <!-- Insert/Edit Modal -->
                <div id="formModal" class="modal">
                    <div class="modal-content">
                        <h2 id="modalTitle">Add Department</h2>
                        <form id="deptForm" onsubmit="submitForm(event)">
                            <input type="hidden" id="mode" value="insert">
                            <input type="hidden" id="editDeptno">
                            <label>Dept No.</label>
                            <input type="number" id="deptno" required>
                            <label>Department Name</label>
                            <input type="text" id="dname" required>
                            <label>Location</label>
                            <input type="text" id="loc" required>
                            <div class="btn-group">
                                <button type="button" class="btn-cancel" onclick="closeModal()">Cancel</button>
                                <button type="submit" class="btn-submit">Save</button>
                            </div>
                        </form>
                    </div>
                </div>

                <!-- View Modal -->
                <div id="viewModal" class="modal">
                    <div class="modal-content">
                        <h2>Department Detail</h2>
                        <p><strong>Dept No.:</strong> <span id="viewDeptno"></span></p>
                        <p><strong>Name:</strong> <span id="viewDname"></span></p>
                        <p><strong>Location:</strong> <span id="viewLoc"></span></p>
                        <div class="btn-group">
                            <button class="btn-cancel" onclick="closeViewModal()">Close</button>
                        </div>
                    </div>
                </div>

                <script>
                    function showToast(msg, type) {
                        var t = document.getElementById('toast');
                        t.textContent = msg;
                        t.className = 'toast ' + type;
                        t.style.display = 'block';
                        setTimeout(function() { t.style.display = 'none'; }, 3000);
                    }

                    function openModal(mode, data) {
                        document.getElementById('formModal').style.display = 'flex';
                        document.getElementById('mode').value = mode;
                        if (mode === 'insert') {
                            document.getElementById('modalTitle').textContent = 'Add Department';
                            document.getElementById('deptno').value = '';
                            document.getElementById('dname').value = '';
                            document.getElementById('loc').value = '';
                            document.getElementById('deptno').disabled = false;
                        } else if (mode === 'edit' && data) {
                            document.getElementById('modalTitle').textContent = 'Edit Department';
                            document.getElementById('editDeptno').value = data.deptno;
                            document.getElementById('deptno').value = data.deptno;
                            document.getElementById('dname').value = data.dname;
                            document.getElementById('loc').value = data.loc;
                            document.getElementById('deptno').disabled = true;
                        }
                    }

                    function closeModal() {
                        document.getElementById('formModal').style.display = 'none';
                    }

                    function closeViewModal() {
                        document.getElementById('viewModal').style.display = 'none';
                    }

                    function viewDept(deptno) {
                        fetch('/web08/detail?deptno=' + deptno)
                            .then(res => res.json())
                            .then(data => {
                                document.getElementById('viewDeptno').textContent = data.deptno;
                                document.getElementById('viewDname').textContent = data.dname;
                                document.getElementById('viewLoc').textContent = data.loc;
                                document.getElementById('viewModal').style.display = 'flex';
                            })
                            .catch(() => showToast('Failed to load detail', 'error'));
                    }

                    function editDept(deptno) {
                        fetch('/web08/detail?deptno=' + deptno)
                            .then(res => res.json())
                            .then(data => openModal('edit', data))
                            .catch(() => showToast('Failed to load data', 'error'));
                    }

                    function deleteDept(deptno) {
                        if (confirm('Are you sure you want to delete department ' + deptno + '?')) {
                            fetch('/web08/delete?deptno=' + deptno, { method: 'POST' })
                                .then(res => res.text())
                                .then(msg => {
                                    showToast(msg, 'success');
                                    location.reload();
                                })
                                .catch(() => showToast('Delete failed', 'error'));
                        }
                    }

                    function submitForm(e) {
                        e.preventDefault();
                        var mode = document.getElementById('mode').value;
                        var deptno = document.getElementById('deptno').value;
                        var dname = document.getElementById('dname').value;
                        var loc = document.getElementById('loc').value;
                        var url = mode === 'insert' ? '/web08/insert' : '/web08/update';
                        var data = { deptno: deptno, dname: dname, loc: loc };
                        if (mode === 'edit') data.deptno = document.getElementById('editDeptno').value;

                        fetch(url, {
                            method: 'POST',
                            headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
                            body: 'deptno=' + data.deptno + '&dname=' + dname + '&loc=' + loc
                        })
                        .then(res => res.text())
                        .then(msg => {
                            closeModal();
                            showToast(msg, 'success');
                            location.reload();
                        })
                        .catch(() => showToast('Operation failed', 'error'));
                    }
                </script>
            </body>
            </html>
            """;

    private final DeptDao deptDao = new DeptDaoImpl();

    @Override
    protected void doGet(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        response.setContentType("text/html;charset=UTF-8");
        try (PrintWriter out = response.getWriter()) {
            out.print(HTML_HEAD);
            printRows(out);
            out.print(HTML_TAIL);
        }
    }

    private void printRows(PrintWriter out) {
        try {
            List<Dept> list = deptDao.selectAll();
            if (list == null || list.isEmpty()) {
                out.print("<tr><td colspan='4'>No departments found.</td></tr>");
                return;
            }
            for (Dept d : list) {
                out.printf(HTML_ROW, d.getDeptno(), d.getDname(), d.getLoc(),
                           d.getDeptno(), d.getDeptno(), d.getDeptno());
            }
        } catch (Exception e) {
            e.printStackTrace();
            out.print("<tr><td colspan='4' style='color:red;'>Error loading data</td></tr>");
        }
    }
}
```