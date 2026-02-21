## EXISTS / NOT EXISTS 示例

`EXISTS` 用于检查子查询是否返回任何行，通常与相关子查询一起使用。

**示例数据：**
- `dept` 表（部门表）：`deptno`（部门编号）, `dname`（部门名称）
- `emp` 表（员工表）：`empno`（员工编号）, `ename`（员工姓名）, `deptno`（部门编号）

**1. EXISTS 示例：查询有员工的部门**
```sql
-- 查询存在员工的部门信息
SELECT * FROM dept d
WHERE EXISTS (
    SELECT 1 FROM emp e
    WHERE e.deptno = d.deptno
);
```
*说明：对于 `dept` 表中的每一行，检查 `emp` 表中是否存在相同 `deptno` 的记录。*

**2. NOT EXISTS 示例：查询没有员工的部门**
```sql
-- 查询没有员工的部门信息
SELECT * FROM dept d
WHERE NOT EXISTS (
    SELECT 1 FROM emp e
    WHERE e.deptno = d.deptno
);
```

**3. 与 IN 子查询的对比**
```sql
-- 使用 IN（可能效率较低）
SELECT * FROM dept
WHERE deptno IN (SELECT deptno FROM emp);

-- 使用 EXISTS（通常更高效，特别是相关子查询）
SELECT * FROM dept d
WHERE EXISTS (SELECT 1 FROM emp e WHERE e.deptno = d.deptno);
```

**特点：**
- `EXISTS` 子查询不返回实际数据，只返回 `TRUE` 或 `FALSE`
- 子查询中的 `SELECT 1` 是惯例，可以用 `SELECT *` 或其他任意值
- 当子查询可能返回大量数据时，`EXISTS` 通常比 `IN` 更高效
- `NOT EXISTS` 常用于数据完整性检查或查找"孤儿"记录