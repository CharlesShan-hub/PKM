![](https://cdn.nlark.com/yuque/0/2023/jpeg/21376908/1692002570088-3338946f-42b3-4174-8910-7e749c31e950.jpeg#averageHue=%23f9f8f8&from=url&id=WWfbr&originHeight=78&originWidth=1400&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=shadow&title=)
# 简单查询

---

查询是SQL语言的核心，用于表达SQL查询的select查询命令是功能最强也是最为复杂的SQL语句，它的作用就是从数据库中检索数据，并将查询结果返回给用户。 select语句由：select子句(查询内容)、from子句(查询对象)、where子句(查询条件)、order by子句(排序方式)、group by子句(分组方式)等组成。查询语句属于SQL语句中的DQL语句，是所有SQL语句中最为复杂也是最重要的语句，所以必须掌握。接下来我们先从简单查询语句开始学习。
## 查一个字段

---

查询一个字段说的是：一个表有多列，查询其中的一列。
语法格式：select 字段名 from 表名;

- select和from是关键字，不能随便写
- **一条SQL语句必须以“;”结尾**
- **对于SQL语句来说，大小写都可以**
- 字段名和表名属于标识符，按照表的实际情况填写，不知道字段名的，可以使用desc命令查看表结构

案例1：查询公司中所有员工编号
```sql
select empno from emp; 
```
![image.png](https://cdn.nlark.com/yuque/0/2021/png/21376908/1620444005101-f8b17d19-7943-42da-868a-4353bbc39d72.png#averageHue=%230f0e0e&height=364&id=iefCx&originHeight=364&originWidth=331&originalType=binary&ratio=1&rotation=0&showTitle=false&size=12803&status=done&style=shadow&title=&width=331)
案例2：查询公司中所有员工姓名
```sql
SELECT ENAME FROM EMP;
```
![image.png](https://cdn.nlark.com/yuque/0/2021/png/21376908/1620444051586-c22b328d-726d-43a1-84c5-b61b053e4c76.png#averageHue=%2311100f&height=368&id=t1BP2&originHeight=368&originWidth=323&originalType=binary&ratio=1&rotation=0&showTitle=false&size=15288&status=done&style=shadow&title=&width=323)
![](https://cdn.nlark.com/yuque/0/2023/jpeg/21376908/1692002570088-3338946f-42b3-4174-8910-7e749c31e950.jpeg#averageHue=%23f9f8f8&from=url&id=Nooeq&originHeight=78&originWidth=1400&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=shadow&title=)
在mysql命令行客户端中，sql语句没有分号是不会执行的：
![image.png](https://cdn.nlark.com/yuque/0/2021/png/21376908/1620444166592-310dfb98-9eed-43ed-afa5-b479e03e0a79.png#averageHue=%230d0d0c&height=249&id=W3RxL&originHeight=249&originWidth=210&originalType=binary&ratio=1&rotation=0&showTitle=false&size=4063&status=done&style=shadow&title=&width=210)
末尾加上“;”就执行了：
![image.png](https://cdn.nlark.com/yuque/0/2021/png/21376908/1620444251765-5d3f1b6c-a491-4382-92a8-8ebb31a40b45.png#averageHue=%230e0d0d&height=236&id=AdNxg&originHeight=236&originWidth=943&originalType=binary&ratio=1&rotation=0&showTitle=false&size=16079&status=done&style=shadow&title=&width=943)
以上sql虽然以分号结尾之后执行了，但是报错了，错误信息显示：语法错误。
假设一个SQL语句在书写过程中出错了，怎么终止这条SQL呢？\c
![image.png](https://cdn.nlark.com/yuque/0/2021/png/21376908/1620444994820-7b03fb95-5097-418c-bc6f-75e3613c7d17.png#averageHue=%2312100f&height=74&id=DCv3D&originHeight=74&originWidth=168&originalType=binary&ratio=1&rotation=0&showTitle=false&size=2131&status=done&style=shadow&title=&width=168)

- [ ] 任务1：查询所有部门名称。
- [ ] 任务2：查询所有薪资等级。

![](https://cdn.nlark.com/yuque/0/2023/jpeg/21376908/1692002570088-3338946f-42b3-4174-8910-7e749c31e950.jpeg#averageHue=%23f9f8f8&from=url&id=Qws7R&originHeight=78&originWidth=1400&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=shadow&title=)
## 查多个字段

---

查询多个字段时，在字段名和字段名之间添加“,”即可。
语法格式：select 字段名1,字段名2,字段名3 from 表名;
案例1：查询员工编号以及员工姓名。
```sql
select empno, ename from emp;
```
![image.png](https://cdn.nlark.com/yuque/0/2021/png/21376908/1620445192077-e454043b-9203-4ca0-83f3-7e7d991187c5.png#averageHue=%2311100f&height=362&id=sYqFg&originHeight=362&originWidth=380&originalType=binary&ratio=1&rotation=0&showTitle=false&size=20812&status=done&style=shadow&title=&width=380)
![](https://cdn.nlark.com/yuque/0/2023/jpeg/21376908/1692002570088-3338946f-42b3-4174-8910-7e749c31e950.jpeg#averageHue=%23f9f8f8&from=url&id=KJw7E&originHeight=78&originWidth=1400&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=shadow&title=)
字段的前后顺序无所谓（只是显示结果列的时候顺序变了）：
```sql
select ename, empno from emp;
```
![image.png](https://cdn.nlark.com/yuque/0/2021/png/21376908/1620445262526-49d81087-7e1b-44f2-afe7-e8bad59dc21d.png#averageHue=%2312100f&height=367&id=Na24p&originHeight=367&originWidth=368&originalType=binary&ratio=1&rotation=0&showTitle=false&size=20595&status=done&style=shadow&title=&width=368)

- [ ] 任务1：查询部门编号、部门名称以及位置。
- [ ] 任务2：查询员工的名字以及工作岗位。

![](https://cdn.nlark.com/yuque/0/2023/jpeg/21376908/1692002570088-3338946f-42b3-4174-8910-7e749c31e950.jpeg#averageHue=%23f9f8f8&from=url&id=XEdDY&originHeight=78&originWidth=1400&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=shadow&title=)
## 查所有字段

---

查询所有字段的可以将每个字段都列出来查询，也可以采用“*”来代表所有字段
案例1：查询员工的所有信息
```sql
select * from emp;
```
![image.png](https://cdn.nlark.com/yuque/0/2021/png/21376908/1620446156182-c5776f47-0d54-45e1-b0a6-af8196b3cbcd.png#averageHue=%23191613&height=365&id=LwKfy&originHeight=365&originWidth=734&originalType=binary&ratio=1&rotation=0&showTitle=false&size=57245&status=done&style=shadow&title=&width=734)
案例2：查询所有部门信息
```sql
select * from dept;
```
![image.png](https://cdn.nlark.com/yuque/0/2021/png/21376908/1620452731531-c4b03af4-9f9f-46d8-acf5-7132317f89ae.png#averageHue=%23161311&height=186&id=ew3JJ&originHeight=186&originWidth=339&originalType=binary&ratio=1&rotation=0&showTitle=false&size=12122&status=done&style=shadow&title=&width=339)
采用“*”进行查询存在的缺点：

- select * from dept; 在执行的时候会被解析为 select DEPTNO, DNAME, LOC from dept; 再执行，所以这种效率方面弱一些。
- 采用“*”的可读性较差，通过“*”很难看出都有哪些具体的字段。

什么时候使用“*”？

- 这个SQL语句不在项目编码中使用，如果平时自己想快速查看表中所有数据的话，这种写法还是很给力的。

- [ ] 任务1：查询所有的薪资等级以及每个薪资等级的最低工资和最高工资。

![](https://cdn.nlark.com/yuque/0/2023/jpeg/21376908/1692002570088-3338946f-42b3-4174-8910-7e749c31e950.jpeg#averageHue=%23f9f8f8&from=url&id=goIwt&originHeight=78&originWidth=1400&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=shadow&title=)
## 查询时字段可参与数学运算

---

在进行查询操作的时候，字段是可以参与数学运算的，例如加减乘除等。
案例1：查询每个员工的月薪
```sql
select ename, sal from emp;
```
![image.png](https://cdn.nlark.com/yuque/0/2021/png/21376908/1620453626714-46aed4db-e9fb-49be-a9be-ce9662dbc962.png#averageHue=%2312100f&height=364&id=wOnEt&originHeight=364&originWidth=375&originalType=binary&ratio=1&rotation=0&showTitle=false&size=21162&status=done&style=shadow&title=&width=375)
![](https://cdn.nlark.com/yuque/0/2023/jpeg/21376908/1692002570088-3338946f-42b3-4174-8910-7e749c31e950.jpeg#averageHue=%23f9f8f8&from=url&id=FCK1j&originHeight=78&originWidth=1400&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=shadow&title=)
案例2：查询每个员工的年薪（月薪 * 12）
```sql
select ename, sal * 12 from emp;
```
![image.png](https://cdn.nlark.com/yuque/0/2021/png/21376908/1620453661204-ca783845-5f31-49fc-90d8-0f4426598cde.png#averageHue=%2313100f&height=364&id=Zkjv2&originHeight=364&originWidth=387&originalType=binary&ratio=1&rotation=0&showTitle=false&size=22636&status=done&style=shadow&title=&width=387)

- [ ] 任务1：查询每个员工月薪加1000之后的月薪
- [ ] 任务2：查询每个员工月薪加1000之后的年薪

![](https://cdn.nlark.com/yuque/0/2023/jpeg/21376908/1692002570088-3338946f-42b3-4174-8910-7e749c31e950.jpeg#averageHue=%23f9f8f8&from=url&id=NDttf&originHeight=78&originWidth=1400&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=shadow&title=)
## 查询时字段可起别名

---

我们借用一下之前的SQL语句
```sql
select ename, sal * 12 from emp;
```
![image.png](https://cdn.nlark.com/yuque/0/2021/png/21376908/1620453661204-ca783845-5f31-49fc-90d8-0f4426598cde.png#averageHue=%2313100f&height=364&id=EQnXg&originHeight=364&originWidth=387&originalType=binary&ratio=1&rotation=0&showTitle=false&size=22636&status=done&style=shadow&title=&width=387)
以上的查询结果列名“sal * 12”可读性较差，是否可以给查询结果的列名进行重命名呢？
### as关键字

- 使用as关键字
```sql
select ename, sal * 12 as yearsal from emp;
```
![image.png](https://cdn.nlark.com/yuque/0/2021/png/21376908/1620454420847-c739365b-440e-4cf7-b1e2-2bcf6d5cdb8b.png#averageHue=%2312100f&height=372&id=NImNH&originHeight=372&originWidth=473&originalType=binary&ratio=1&rotation=0&showTitle=false&size=25001&status=done&style=shadow&title=&width=473)
通过as关键字起别名后，查询结果列显示yearsal，可读性增强。
![](https://cdn.nlark.com/yuque/0/2023/jpeg/21376908/1692002570088-3338946f-42b3-4174-8910-7e749c31e950.jpeg#averageHue=%23f9f8f8&from=url&id=G4NWU&originHeight=78&originWidth=1400&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=shadow&title=)
### 省略as关键字

- 其实as关键字可以省略，只要使用空格即可
```sql
select ename, sal * 12 yearsal from emp;
```
![image.png](https://cdn.nlark.com/yuque/0/2021/png/21376908/1620466356467-fb4612f8-72f6-4506-b2bc-1744846c171d.png#averageHue=%2311100e&height=363&id=XWTbX&originHeight=363&originWidth=464&originalType=binary&ratio=1&rotation=0&showTitle=false&size=24234&status=done&style=shadow&title=&width=464)

- 通过以上测试，得知as可以省略，可以使用空格代替as，但如果别名中有空格呢？
### 别名中有空格
```sql
select ename, sal * 12 year sal from emp;
```
![image.png](https://cdn.nlark.com/yuque/0/2021/png/21376908/1620466540145-98adb10e-15a2-46df-9179-7e41ae1fc322.png#averageHue=%2313110f&height=87&id=LnbYI&originHeight=87&originWidth=946&originalType=binary&ratio=1&rotation=0&showTitle=false&size=12503&status=done&style=shadow&title=&width=946)
可以看出，执行报错了，说语法有问题，这是为什么？分析一下：SQL语句编译器在检查该语句的时候，在year后面遇到了空格，会继续找from关键字，但year后面不是from关键字，所以编译器报错了。怎么解决这个问题？记住：如果别名中有空格的话，可以将这个别名使用双引号或者单引号将其括起来。
```sql
select ename, sal * 12 "year sal" from emp;
select ename, sal * 12 'year sal' from emp;
```
![image.png](https://cdn.nlark.com/yuque/0/2021/png/21376908/1620467027246-b5cce57e-3ca3-4b3f-9298-a21fc3bb77c3.png#averageHue=%23110f0e&height=744&id=kyi8P&originHeight=744&originWidth=558&originalType=binary&ratio=1&rotation=0&showTitle=false&size=53259&status=done&style=shadow&title=&width=558)
**在mysql中，字符串既可以使用双引号也可以使用单引号，但还是建议使用单引号，因为单引号属于标准SQL。**
![](https://cdn.nlark.com/yuque/0/2023/jpeg/21376908/1692002570088-3338946f-42b3-4174-8910-7e749c31e950.jpeg#averageHue=%23f9f8f8&from=url&id=V2sJs&originHeight=78&originWidth=1400&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=shadow&title=)
### 别名中有中文

- 如果别名采用中文呢？
```sql
select ename, sal * 12 年薪 from emp;
```
![image.png](https://cdn.nlark.com/yuque/0/2021/png/21376908/1620467760618-b5df74f5-c8ee-4e39-88a9-e10fde59bb56.png#averageHue=%2311100e&height=373&id=AsiUs&originHeight=373&originWidth=445&originalType=binary&ratio=1&rotation=0&showTitle=false&size=24025&status=done&style=shadow&title=&width=445)
**别名是中文是可以的，但是对于低版本的mysql来说会报错，需要添加双引号或单引号。**我们当前使用的mysql版本是：8.0.24

- [ ] 任务：查询所有员工的信息，要求每个字段名采用中文显示。

![](https://cdn.nlark.com/yuque/0/2023/jpeg/21376908/1692002570088-3338946f-42b3-4174-8910-7e749c31e950.jpeg#averageHue=%23f9f8f8&from=url&id=e5sVc&originHeight=78&originWidth=1400&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=shadow&title=)
# 条件查询

---

通常在进行查询操作的时候，都是查询符合某些条件的数据，很少将表中所有数据都取出来。怎么取出表的部分数据？需要在查询语句中添加条件进行数据的过滤。常见的过滤条件如下：

| **条件** | **说明** |
| --- | --- |
| = | 等于 |
| <>或!= | 不等于 |
| >= | 大于等于 |
| <= | 小于等于 |
| > | 大于 |
| < | 小于 |
| between...and... | 等同于 >= and <= |
| is null | 为空 |
| is not null | 不为空 |
| <=> | 安全等于（可读性差，很少使用了）。 |
| and 或 && | 并且 |
| or 或 &#124;&#124; | 或者 |
| in | 在指定的值当中 |
| not in | 不在指定的值当中 |
| exists |  |
| not exists |  |
| like | 模糊查询 |

## 条件查询语法格式

---

```sql
select 
  ...
from
  ...
where
  过滤条件;
```
过滤条件放在where子句当中，以上语句的执行顺序是：
    第一步：先执行from
    第二步：再通过where条件过滤
    第三步：最后执行select，查询并将结果展示到控制台

![](https://cdn.nlark.com/yuque/0/2023/jpeg/21376908/1692002570088-3338946f-42b3-4174-8910-7e749c31e950.jpeg#averageHue=%23f9f8f8&from=url&id=WjVQY&originHeight=78&originWidth=1400&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=shadow&title=)
## 等于、不等于

---

### 等于 =
判断等量关系，支持多种数据类型，比如：数字、字符串、日期等。
案例1：查询月薪3000的员工编号及姓名
```sql
select 
  empno,ename
from
  emp
where
  sal = 3000;
```
![image.png](https://cdn.nlark.com/yuque/0/2021/png/21376908/1621907694609-eea9c573-f409-4291-b065-afdbf568e8c7.png#averageHue=%2312100f&height=267&id=Y8ZCX&originHeight=267&originWidth=306&originalType=binary&ratio=1&rotation=0&showTitle=false&size=10989&status=done&style=shadow&title=&width=306)
案例2：查询员工FORD的岗位及月薪
```sql
select
	job, sal
from
	emp
where
	ename = 'FORD';
```
![image.png](https://cdn.nlark.com/yuque/0/2021/png/21376908/1621907754724-3f628fe9-0c56-4057-8be7-60d0bf968b6c.png#averageHue=%2312100f&height=254&id=KB48O&originHeight=254&originWidth=309&originalType=binary&ratio=1&rotation=0&showTitle=false&size=9820&status=done&style=shadow&title=&width=309)
存储在表emp中的员工姓名是FORD，全部大写，如果在查询的时候，写成全部小写会怎样呢？
```sql
select
	job, sal
from
	emp
where
	ename = 'ford';
```
![image.png](https://cdn.nlark.com/yuque/0/2021/png/21376908/1621907908980-acfef2ac-247a-434a-846d-aebe132c534b.png#averageHue=%23131110&height=255&id=fOGhC&originHeight=255&originWidth=268&originalType=binary&ratio=1&rotation=0&showTitle=false&size=9405&status=done&style=shadow&title=&width=268)
![](https://cdn.nlark.com/yuque/0/2023/jpeg/21376908/1692002570088-3338946f-42b3-4174-8910-7e749c31e950.jpeg#averageHue=%23f9f8f8&from=url&id=vKAPe&originHeight=78&originWidth=1400&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=shadow&title=)
通过测试发现，即使写成小写ford，也是可以查询到结果的，**不过这里需要注意的是：在Oracle数据库当中是查询不到数据的，Oracle的语法要比MySQL的语法严谨。对于SQL语句本身来说是不区分大小写的，但是对于表中真实存储的数据，大写A和小写a还是不一样的，这一点Oracle做的很好。MySQL的语法更随性。另外在Oracle当中，字符串是必须使用单引号括起来的，但在MySQL当中，字符串可以使用单引号，也可以使用双引号**，如下：
```sql
select
	job, sal
from
  emp
where
  ename = "FORD";
```
![image.png](https://cdn.nlark.com/yuque/0/2021/png/21376908/1621908335672-ce3770ed-b906-44ad-8e6a-1255e620f77c.png#averageHue=%23110f0e&height=152&id=nVwF9&originHeight=152&originWidth=550&originalType=binary&ratio=1&rotation=0&showTitle=false&size=9330&status=done&style=shadow&title=&width=550)
案例3：查询岗位是MANAGER的员工编号及姓名
```sql
select
  empno, ename
from
  emp
where
  job = 'MANAGER';
```
![image.png](https://cdn.nlark.com/yuque/0/2021/png/21376908/1621908485311-e63dfa85-7530-4d2e-8652-f5885287dda7.png#averageHue=%23100f0e&height=190&id=vTZba&originHeight=190&originWidth=588&originalType=binary&ratio=1&rotation=0&showTitle=false&size=13081&status=done&style=shadow&title=&width=588)

- [ ] 任务：查询工资级别是1的最低工资以及最高工资

![](https://cdn.nlark.com/yuque/0/2023/jpeg/21376908/1692002570088-3338946f-42b3-4174-8910-7e749c31e950.jpeg#averageHue=%23f9f8f8&from=url&id=LSu5h&originHeight=78&originWidth=1400&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=shadow&title=)
### 不等于 <> 或 !=
判断非等量关系，支持字符串、数字、日期类型等。不等号有两种写法，第一种<>，第二种!=，第二种写法和Java程序中的不等号相同，第一种写法比较诡异，不过也很好理解，比如<>3，表示小于3、大于3，就是不等于3。你get到了吗？
案例1：查询工资不是3000的员工编号、姓名、薪资
```sql
select
  empno,ename,sal
from
  emp
where
  sal <> 3000;
```
![image.png](https://cdn.nlark.com/yuque/0/2021/png/21376908/1621909279969-92f574b8-825b-4774-ab25-b5ccb058ebd5.png#averageHue=%2312100f&height=365&id=x0euZ&originHeight=365&originWidth=577&originalType=binary&ratio=1&rotation=0&showTitle=false&size=31965&status=done&style=shadow&title=&width=577)
案例2：查询工作岗位不是MANAGER的员工姓名和岗位
```sql
select
  ename,job
from
	emp
where
	job <> 'MANAGER';
```
![image.png](https://cdn.nlark.com/yuque/0/2021/png/21376908/1621909394164-d589f9f5-30a1-477c-aef6-b659ae36d9e8.png#averageHue=%2311100f&height=351&id=X5qgA&originHeight=351&originWidth=575&originalType=binary&ratio=1&rotation=0&showTitle=false&size=26497&status=done&style=shadow&title=&width=575)

- [ ] 任务：查询不在部门编号为10的部门工作的员工信息

![](https://cdn.nlark.com/yuque/0/2023/jpeg/21376908/1692002570088-3338946f-42b3-4174-8910-7e749c31e950.jpeg#averageHue=%23f9f8f8&from=url&id=rXXwQ&originHeight=78&originWidth=1400&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=shadow&title=)
## 大于、大于等于、小于、小于等于

---

### 大于 >
案例：找出薪资大于3000的员工姓名、薪资
```sql
select 
  ename, sal
from
  emp
where
  sal > 3000;
```
![image.png](https://cdn.nlark.com/yuque/0/2021/png/21376908/1621909653019-47b3d57f-3690-46fb-9f47-7906f0fd3245.png#averageHue=%2311100f&height=148&id=k0f1J&originHeight=148&originWidth=514&originalType=binary&ratio=1&rotation=0&showTitle=false&size=8657&status=done&style=shadow&title=&width=514)
![](https://cdn.nlark.com/yuque/0/2023/jpeg/21376908/1692002570088-3338946f-42b3-4174-8910-7e749c31e950.jpeg#averageHue=%23f9f8f8&from=url&id=ydNP9&originHeight=78&originWidth=1400&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=shadow&title=)
### 大于等于 >=
案例：找出薪资大于等于3000的员工姓名、薪资
```sql
select 
  ename, sal
from
  emp
where
  sal >= 3000;
```
![image.png](https://cdn.nlark.com/yuque/0/2021/png/21376908/1621909723383-d1a6872b-5790-4d89-875b-e1116ea539cf.png#averageHue=%23110f0e&height=190&id=pnLPe&originHeight=190&originWidth=528&originalType=binary&ratio=1&rotation=0&showTitle=false&size=11463&status=done&style=shadow&title=&width=528)
### 小于 <
案例：找出薪资小于3000的员工姓名、薪资
```sql
select 
  ename, sal
from
  emp
where
  sal < 3000;
```
![image.png](https://cdn.nlark.com/yuque/0/2021/png/21376908/1621909833614-f9d57a1f-1d48-4d14-aaef-83c5bddb89a8.png#averageHue=%23110f0e&height=346&id=Ln9DW&originHeight=346&originWidth=535&originalType=binary&ratio=1&rotation=0&showTitle=false&size=24457&status=done&style=shadow&title=&width=535)
### 小于等于 <=
案例：找出薪资小于等于3000的员工姓名、薪资
```sql
select 
  ename, sal
from
  emp
where
  sal <= 3000;
```
![image.png](https://cdn.nlark.com/yuque/0/2021/png/21376908/1621909895715-9af5ab2f-b445-4b44-a643-fd2a312cac2c.png#averageHue=%23110f0e&height=387&id=ZVSfe&originHeight=387&originWidth=536&originalType=binary&ratio=1&rotation=0&showTitle=false&size=27408&status=done&style=shadow&title=&width=536)
![](https://cdn.nlark.com/yuque/0/2023/jpeg/21376908/1692002570088-3338946f-42b3-4174-8910-7e749c31e950.jpeg#averageHue=%23f9f8f8&from=url&id=VCbJ6&originHeight=78&originWidth=1400&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=shadow&title=)
## and

---

and表示并且，还有另一种写法：&&
案例：找出薪资大于等于3000并且小于等于5000的员工姓名、薪资。
```sql
select
  ename,sal
from
  emp
where
  sal >= 3000 and sal <= 5000;
```
![image.png](https://cdn.nlark.com/yuque/0/2021/png/21376908/1621910545661-438867ac-b8d0-4a80-929e-5a758b44add4.png#averageHue=%23100f0e&height=193&id=GpkEk&originHeight=193&originWidth=681&originalType=binary&ratio=1&rotation=0&showTitle=false&size=12734&status=done&style=shadow&title=&width=681)
![image.png](https://cdn.nlark.com/yuque/0/2021/png/21376908/1621910577682-f852440b-94f8-4299-89ad-c0a88fefc0d1.png#averageHue=%23100f0e&height=187&id=AyScE&originHeight=187&originWidth=672&originalType=binary&ratio=1&rotation=0&showTitle=false&size=13060&status=done&style=shadow&title=&width=672)

- [ ] 任务：找出工资级别为2~4（包含2和4）的最低工资和最高工资。

![](https://cdn.nlark.com/yuque/0/2023/jpeg/21376908/1692002570088-3338946f-42b3-4174-8910-7e749c31e950.jpeg#averageHue=%23f9f8f8&from=url&id=XfnXa&originHeight=78&originWidth=1400&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=shadow&title=)
## or

---

or表示或者，还有另一种写法：||
案例：找出工作岗位是MANAGER和SALESMAN的员工姓名、工作岗位
```sql
select 
  ename, job
from
  emp
where
  job = 'MANAGER' or job = 'SALESMAN';
```
![image.png](https://cdn.nlark.com/yuque/0/2021/png/21376908/1621910850853-c7030458-0c8f-4040-bc29-c6fa66caca7c.png#averageHue=%23110f0e&height=376&id=tQUI3&originHeight=376&originWidth=492&originalType=binary&ratio=1&rotation=0&showTitle=false&size=22698&status=done&style=shadow&title=&width=492)
![image.png](https://cdn.nlark.com/yuque/0/2021/png/21376908/1621910943353-4a9fb152-67b9-4044-a2b4-b90a2fbf3f57.png#averageHue=%23110f0e&height=370&id=k83WP&originHeight=370&originWidth=471&originalType=binary&ratio=1&rotation=0&showTitle=false&size=22916&status=done&style=shadow&title=&width=471)
![](https://cdn.nlark.com/yuque/0/2023/jpeg/21376908/1692002570088-3338946f-42b3-4174-8910-7e749c31e950.jpeg#averageHue=%23f9f8f8&from=url&id=yWWia&originHeight=78&originWidth=1400&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=shadow&title=)
注意：这个题目描述中有这样一句话：MANAGER和SALESMAN，有的同学一看到“和”，就直接使用“and”了，因为“和”对应的英文单词是“and”，如果是这样的话，就大错特错了，因为and表示并且，使用and表示工作岗位既是MANAGER又是SALESMAN的员工，这样的员工是不存在的，因为每一个员工只有一个岗位，不可能同时从事两个岗位。所以使用and是查询不到任何结果的。如下
```sql
select 
  ename, job
from
  emp
where
  job = 'MANAGER' and job = 'SALESMAN';
```
![image.png](https://cdn.nlark.com/yuque/0/2021/png/21376908/1621911189669-be42f087-b388-4eb2-80b7-602766996b82.png#averageHue=%23100f0e&height=151&id=DRxAe&originHeight=151&originWidth=471&originalType=binary&ratio=1&rotation=0&showTitle=false&size=8765&status=done&style=shadow&title=&width=471)

- [ ] 任务：查询20和30部门的员工信息。

![](https://cdn.nlark.com/yuque/0/2023/jpeg/21376908/1692002570088-3338946f-42b3-4174-8910-7e749c31e950.jpeg#averageHue=%23f9f8f8&from=url&id=E82Cs&originHeight=78&originWidth=1400&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=shadow&title=)
## and和or的优先级问题

---

and和or同时出现时，and优先级较高，会先执行，如果希望or先执行，这个时候需要给or条件添加小括号。另外，以后遇到不确定的优先级时，可以通过添加小括号的方式来解决。对于优先级问题没必要记忆。
案例：找出薪资小于1500，并且部门编号是20或30的员工姓名、薪资、部门编号。
先来看一下错误写法：
```sql
select
  ename,sal,deptno
from
  emp
where
  sal < 1500 and deptno = 20 or deptno = 30;
```
![image.png](https://cdn.nlark.com/yuque/0/2021/png/21376908/1621912213872-f2b1fe9e-384c-404e-bf24-d81bd895ae23.png#averageHue=%2311100f&height=388&id=DymCc&originHeight=388&originWidth=524&originalType=binary&ratio=1&rotation=0&showTitle=false&size=26693&status=done&style=shadow&title=&width=524)
认真解读题意得知：薪资小于1500是一个大前提，要找出的是薪资小于1500的，满足这个条件的前提下，再找部门编号是20或30的，显然以上的运行结果中出现了薪资为1600的，为什么1600的会出现呢？这是因为“sal < 1500 and deptno = 20”结合在一起了，“depnto = 30”成了一个独立的条件。会导致部门编号为30的所有员工全部查询出来。我们应该让“deptno = 20 or deptno = 30”结合在一起，正确写法如下：
```sql
select
  ename,sal,deptno
from
  emp
where
  sal < 1500 and (deptno = 20 or deptno = 30);
```
![image.png](https://cdn.nlark.com/yuque/0/2021/png/21376908/1621912713447-a9b7aeee-4998-4eae-8e53-71353a405890.png#averageHue=%2311100e&height=330&id=g19B4&originHeight=330&originWidth=539&originalType=binary&ratio=1&rotation=0&showTitle=false&size=21912&status=done&style=shadow&title=&width=539)

- [ ] 任务：找出薪资小于1500的，并且工作岗位是CLERK和SALESMAN的员工姓名、薪资、岗位。

![](https://cdn.nlark.com/yuque/0/2023/jpeg/21376908/1692002570088-3338946f-42b3-4174-8910-7e749c31e950.jpeg#averageHue=%23f9f8f8&from=url&id=L1XhP&originHeight=78&originWidth=1400&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=shadow&title=)
## between...and...

---

between...and...等同于 >= and <=
做区间判断的，包含左右两个边界值。
它支持数字、日期、字符串等数据类型。
between...and...在使用时一定是**左小右大**。左大右小时无法查询到数据。
between...and... 和 >= and <=只是在写法结构上有区别，执行原理和效率方面没有区别。
案例：找出薪资在1600到3000的员工姓名、薪资
```sql
select 
  ename,sal
from
  emp
where
	sal between 1600 and 3000;
```
![image.png](https://cdn.nlark.com/yuque/0/2021/png/21376908/1621913942714-15a74832-d5da-4215-8991-35a3d48f7061.png#averageHue=%2312100f&height=344&id=GTVA6&originHeight=344&originWidth=374&originalType=binary&ratio=1&rotation=0&showTitle=false&size=17629&status=done&style=shadow&title=&width=374)
采用左大右小的方式：
```sql
select 
  ename,sal
from
  emp
where
	sal between 3000 and 1600;
```
![image.png](https://cdn.nlark.com/yuque/0/2021/png/21376908/1621914030809-2ebf83da-aba0-429d-970e-2f6906611f11.png#averageHue=%2311100f&height=147&id=OG0Ah&originHeight=147&originWidth=358&originalType=binary&ratio=1&rotation=0&showTitle=false&size=7418&status=done&style=shadow&title=&width=358)
没有查询到任何数据，所以在使用的时候一定要注意：**左小右大**。

- [ ] 任务：查询在1982-01-23到1987-04-19之间入职的员工

![image.png](https://cdn.nlark.com/yuque/0/2021/png/21376908/1621914250873-25bff9ba-b4e6-4145-a5f8-9036fba35627.png#averageHue=%23161312&height=169&id=IPUnM&originHeight=169&originWidth=783&originalType=binary&ratio=1&rotation=0&showTitle=false&size=20676&status=done&style=shadow&title=&width=783)
注意：以上SQL语句中日期需要加上单引号。

![](https://cdn.nlark.com/yuque/0/2023/jpeg/21376908/1692002570088-3338946f-42b3-4174-8910-7e749c31e950.jpeg#averageHue=%23f9f8f8&from=url&id=JTZOF&originHeight=78&originWidth=1400&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=shadow&title=)
## is null、is not null

---

判断某个数据是否为null，不能使用等号，只能使用 is null
判断某个数据是否不为null，不能使用不等号，只能使用 is not null
在数据库中null不是一个值，不能用等号和不等号衡量，null代表什么也没有，没有数据，没有值
### is null
案例1：找出津贴为空的员工姓名、薪资、津贴。
```sql
select
  ename,sal,comm
from
  emp
where
  comm is null;
```
![image.png](https://cdn.nlark.com/yuque/0/2021/png/21376908/1621914737738-74345239-9ea8-4afa-a4bf-68fb0bb26e98.png#averageHue=%23161310&height=427&id=B8Ayw&originHeight=427&originWidth=298&originalType=binary&ratio=1&rotation=0&showTitle=false&size=23224&status=done&style=shadow&title=&width=298)
我们使用等号，尝试一下：
```sql
select
  ename,sal,comm
from
  emp
where
  comm = null;
```
![image.png](https://cdn.nlark.com/yuque/0/2021/png/21376908/1621914817611-97c0858b-a248-4a10-9fba-e5152283b553.png#averageHue=%2312100f&height=149&id=p0pLx&originHeight=149&originWidth=247&originalType=binary&ratio=1&rotation=0&showTitle=false&size=5999&status=done&style=shadow&title=&width=247)
查询不到任何数据，所以判断是否为空，不能用等号。
![](https://cdn.nlark.com/yuque/0/2023/jpeg/21376908/1692002570088-3338946f-42b3-4174-8910-7e749c31e950.jpeg#averageHue=%23f9f8f8&from=url&id=Byo2n&originHeight=78&originWidth=1400&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=shadow&title=)
### is not null
案例2：找出津贴不为空的员工姓名、薪资、津贴
```sql
select
  ename,sal,comm
from
  emp
where
  comm is not null;
```
![image.png](https://cdn.nlark.com/yuque/0/2021/png/21376908/1621914906515-cfd5351e-22bc-4184-b6d5-785f27049020.png#averageHue=%23141210&height=311&id=hC9OP&originHeight=311&originWidth=315&originalType=binary&ratio=1&rotation=0&showTitle=false&size=15140&status=done&style=shadow&title=&width=315)

![](https://cdn.nlark.com/yuque/0/2023/jpeg/21376908/1692002570088-3338946f-42b3-4174-8910-7e749c31e950.jpeg#averageHue=%23f9f8f8&from=url&id=pBBB0&originHeight=78&originWidth=1400&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=shadow&title=)
## in、not in

---

### in
job in('MANAGER','SALESMAN','CLERK') 等同于 job = 'MANAGER' or job = 'SALESMAN' or job = 'CLERK'
sal in(1600, 3000, 5000) 等同于 sal = 1600 or sal = 3000 or sal = 5000
in后面有一个小括号，小括号当中有多个值，值和值之间采用逗号隔开
sal in(1500, 5000)，需要注意的是：这个并不是说薪资在1500到5000之间，in不代表区间，表示sal是1500的和sal是5000的
案例1：找出工作岗位是MANAGER和SALESMAN的员工姓名、薪资、工作岗位
第一种：使用or
```sql
select
  ename,sal,job
from
  emp
where
  job = 'MANAGER' or job = 'SALESMAN';
```
![image.png](https://cdn.nlark.com/yuque/0/2021/png/21376908/1621979207586-14dece4a-ce7f-4db8-a43f-bbfee6fd6133.png#averageHue=%2313110f&height=435&id=O2KwT&originHeight=435&originWidth=549&originalType=binary&ratio=1&rotation=0&showTitle=false&size=35206&status=done&style=shadow&title=&width=549)
第二种：使用in
```sql
select
  ename,sal,job
from
  emp
where
  job in('MANAGER', 'SALESMAN');
```
![image.png](https://cdn.nlark.com/yuque/0/2021/png/21376908/1621979288013-a6975d0e-46f9-43d8-a226-6df047e6490e.png#averageHue=%23141210&height=438&id=GI28U&originHeight=438&originWidth=470&originalType=binary&ratio=1&rotation=0&showTitle=false&size=33948&status=done&style=shadow&title=&width=470)
案例2：找出薪资是1500/1600/3000的员工姓名、工作岗位
```sql
select
  ename,job
from
  emp
where
  sal in(1500, 1600, 3000);
```
![image.png](https://cdn.nlark.com/yuque/0/2021/png/21376908/1621979430766-b7dc80d4-568a-4216-a173-6ec7c49d1f9c.png#averageHue=%2311100f&height=371&id=vsqSR&originHeight=371&originWidth=433&originalType=binary&ratio=1&rotation=0&showTitle=false&size=20173&status=done&style=shadow&title=&width=433)

- [ ] 任务：找出部门编号是10和20的员工编号、姓名。（要求使用两种方案）

![](https://cdn.nlark.com/yuque/0/2023/jpeg/21376908/1692002570088-3338946f-42b3-4174-8910-7e749c31e950.jpeg#averageHue=%23f9f8f8&from=url&id=MHkjM&originHeight=78&originWidth=1400&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=shadow&title=)
### not in
job not in('MANAGER','SALESMAN') 等同于 job <> 'MANAGER' and job <> 'SALESMAN'
sal not in(1600, 5000) 等同于 sal <> 1600 and sal <> 5000
案例：找出工作岗位不是MANAGER和SALESMAN的员工姓名、工作岗位
第一种：使用and
```sql
select 
  ename,job
from
  emp
where
  job <> 'MANAGER' and job <> 'SALESMAN';
```
![image.png](https://cdn.nlark.com/yuque/0/2021/png/21376908/1621980958567-7c01fd48-a1ec-4392-85e1-120b86865b99.png#averageHue=%23100f0e&height=406&id=N24ds&originHeight=406&originWidth=599&originalType=binary&ratio=1&rotation=0&showTitle=false&size=26784&status=done&style=shadow&title=&width=599)
第二种：使用not in
```sql
select 
  ename,job
from
  emp
where
  job not in('MANAGER', 'SALESMAN');
```
![image.png](https://cdn.nlark.com/yuque/0/2021/png/21376908/1621981036376-d6cecc7a-b7b8-4342-a83e-19ee49d77697.png#averageHue=%23110f0e&height=436&id=udgWf&originHeight=436&originWidth=537&originalType=binary&ratio=1&rotation=0&showTitle=false&size=28126&status=done&style=shadow&title=&width=537)

- [ ] 任务：找出薪资不是1600和3000的员工姓名、薪资。

![](https://cdn.nlark.com/yuque/0/2023/jpeg/21376908/1692002570088-3338946f-42b3-4174-8910-7e749c31e950.jpeg#averageHue=%23f9f8f8&from=url&id=zGsfo&originHeight=78&originWidth=1400&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=shadow&title=)

### in、not in 与 NULL
先来看一下emp表中的数据
```sql
select * from emp;
```
![image.png](https://cdn.nlark.com/yuque/0/2021/png/21376908/1621981605595-632500b0-a2a0-401c-8995-1573468ae1f1.png#averageHue=%23161311&height=492&id=mVQz1&originHeight=492&originWidth=968&originalType=binary&ratio=1&rotation=0&showTitle=false&size=85972&status=done&style=shadow&title=&width=968)
通过表中数据观察到，有4个员工的津贴不为NULL，剩下10个员工的津贴都是NULL。
写这样一条SQL语句：
```sql
select * from emp where comm in(NULL, 300);
```
![image.png](https://cdn.nlark.com/yuque/0/2021/png/21376908/1621981810022-80718321-ffdd-496b-af1d-620cf268c993.png#averageHue=%23141211&height=172&id=xG35u&originHeight=172&originWidth=922&originalType=binary&ratio=1&rotation=0&showTitle=false&size=19587&status=done&style=shadow&title=&width=922)
为什么以上执行结果只有一条记录呢？分析一下：
首先你要知道in的执行原理实际上是采用=和or的方式，也就是说，以上SQL语句实际上是：
```sql
select * from emp where comm = NULL or comm = 300;
```
其中NULL不能用等号=进行判断，所以comm = NULL结果是false，然而中间使用的是or，所以comm = NULL被忽略了。所以查询结果就以上一条数据。
通过以上的测试得知：**in是自动忽略NULL的**。
再写这样一条SQL语句：
```sql
select * from emp where comm not in(NULL, 300);
```
![image.png](https://cdn.nlark.com/yuque/0/2021/png/21376908/1621982073198-d77677ed-77de-4086-aba9-4eaeda923a51.png#averageHue=%23141210&height=56&id=TPlkq&originHeight=56&originWidth=656&originalType=binary&ratio=1&rotation=0&showTitle=false&size=6518&status=done&style=shadow&title=&width=656)
以上的执行结果奇怪了，为什么没有查到任何数据呢？我们分析一下：
首先你要知道not in的执行原理实际上是采用<>和and的方式，也就是说，以上SQL语句实际上是：
```sql
select * from emp where comm <> NULL and comm <> 300;
```
其中NULL的判断不能使用<>，所以comm <> NULL结果是false，由于后面是and，and表示并且，comm <> NULL已经是false了，所以and右边的就没必要运算了，comm <> NULL and comm <> 300的整体运算结果就是false。所以查询不到任何数据。
通过以上测试得知，**not in是不会自动忽略NULL的**，所以在使用not in的时候一定要提前过滤掉NULL。

![](https://cdn.nlark.com/yuque/0/2023/jpeg/21376908/1692002570088-3338946f-42b3-4174-8910-7e749c31e950.jpeg#averageHue=%23f9f8f8&from=url&id=cnDUU&originHeight=78&originWidth=1400&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=shadow&title=)
## in和or的效率比拼

---

在MySQL当中，如何统计一个SQL语句的执行时长？

- 可以使用这个命令：show profiles;  这个命令可以查看在mysql中执行的所有SQL以及命令的耗费时长。
- show profiles; 是在mysql5.0.37之后添加的。所以要确保你的mysql版本没问题。
- 如何开启时长统计功能：set profiling = 1;
- 查看时长统计功能是否开启：show variables like '%pro%';
- 查看每条SQL的耗时：show profiles;
- 查看其中某条SQL耗时明细：show profile for query query_id;
- 查看最新一条SQL的耗时明细：show profile;
- 查看cpu，io等信息：show profile block io, cpu for query query_id; 

or的效率为O(n)，而in的效率为O(log n), 当n越大的时候效率相差越明显（**也就是说数据量越大的时候，in的效率越高**）。以下是测试过程：
第一步，创建测试表，并生成测试数据，测试数据为1000万条记录。数据库中关闭了query cache，因此数据库缓存不会对查询造成影响。具体的代码如下：
```sql
#创建测试的test表
DROP TABLE IF EXISTS test; 
CREATE TABLE test( 
    ID INT(10) NOT NULL, 
    `Name` VARCHAR(20) DEFAULT '' NOT NULL, 
    PRIMARY KEY( ID ) 
)ENGINE=INNODB DEFAULT CHARSET utf8; 

#创建生成测试数据的存储过程
DROP PROCEDURE IF EXISTS pre_test; 
DELIMITER //
CREATE PROCEDURE pre_test() 
BEGIN 
DECLARE i INT DEFAULT 0; 
SET autocommit = 0; 
WHILE i<10000000 DO 
INSERT INTO test ( ID,`Name` ) VALUES( i, CONCAT( 'Carl', i ) ); 
SET i = i+1; 
IF i%2000 = 0 THEN 
COMMIT; 
END IF; 
END WHILE; 
END; //
DELIMITER ;

#执行存储过程生成测试数据
CALL pre_test();
```
以上SQL看不懂没关系，先执行它，进行数据初始化准备工作。
第二步：分三种情况进行测试，分别是：
第1种情况：in和or所在列为主键的情形。
第2种情况：in和or所在列创建有索引的情形。
第3种情况：in和or所在列没有索引的情形。
每种情况又采用不同的in和or的数量进行测试。由于测试语句的数据量有4种情况，我这里就称为A组、B组、C组、D组，其中A组为3个值，B组为150个值，C组为300个值，D组为1000个值。具体的测试语句如下：
```sql
#A组
#in和or中有3条数据的情况
SELECT * FROM test WHERE id IN (1,23,48);
SELECT * FROM test WHERE id =1 OR id=23 OR id=48;

#B组
#in和or中有150条数据的情况
SELECT * FROM test WHERE id IN (59617932,98114476,89047409,26968186,56586105,35488201,53251989,18182139,71164231,57655852,7948544,60658339,50758185,66667117,34771253,68699137,27877290,44275282,1585444,71219424,90937482,83928635,24588528,81933207,9607562,12013895,84640278,85549596,53249244,8567444,85402877,15040223,54266509,17718135,91687882,22930500,94756430,66031097,13084573,18137443,89917778,46845456,43939093,35943480,18213703,46362815,49835919,83137546,2101409,74932951,11984477,93113331,77848222,68546065,33728734,90793684,44975642,61387237,52483391,97716233,49449060,22411182,30776331,60597240,6911731,45789095,62075344,8379933,97910423,86861971,81342386,93423963,83852896,18566482,22747687,51420625,75862064,26402882,93958561,85202979,97049369,67674725,9475653,92302381,78133617,49295001,36517340,81387142,15707241,60832834,93157830,64171432,58537826,70141767,7326025,36632075,9639624,8900056,99702164,35108945,87820933,57302965,16652391,41845132,62184393,70136913,79574630,32562398,94616790,61258220,73162018,81644480,19453596,97380163,1204733,33357040,84854495,13888863,49041868,89272326,38405345,571248,6349029,70755321,79307694,60619684,92624181,73135306,23279848,95612954,55845916,6223606,43836918,37459781,67969314,99398872,7616960,37189193,50151920,62881879,12364637,33204320,27135672,28441504,47373461,87967926,30631796,20053540,18735984,83406724);
SELECT * FROM test WHERE id=59617932 OR id=98114476 OR id=89047409 OR id=26968186 OR id=56586105 OR id=35488201 OR id=53251989 OR id=18182139 OR id=71164231 OR id=57655852 OR id=7948544 OR id=60658339 OR id=50758185 OR id=66667117 OR id=34771253 OR id=68699137 OR id=27877290 OR id=44275282 OR id=1585444 OR id=71219424 OR id=90937482 OR id=83928635 OR id=24588528 OR id=81933207 OR id=9607562 OR id=12013895 OR id=84640278 OR id=85549596 OR id=53249244 OR id=8567444 OR id=85402877 OR id=15040223 OR id=54266509 OR id=17718135 OR id=91687882 OR id=22930500 OR id=94756430 OR id=66031097 OR id=13084573 OR id=18137443 OR id=89917778 OR id=46845456 OR id=43939093 OR id=35943480 OR id=18213703 OR id=46362815 OR id=49835919 OR id=83137546 OR id=2101409 OR id=74932951 OR id=11984477 OR id=93113331 OR id=77848222 OR id=68546065 OR id=33728734 OR id=90793684 OR id=44975642 OR id=61387237 OR id=52483391 OR id=97716233 OR id=49449060 OR id=22411182 OR id=30776331 OR id=60597240 OR id=6911731 OR id=45789095 OR id=62075344 OR id=8379933 OR id=97910423 OR id=86861971 OR id=81342386 OR id=93423963 OR id=83852896 OR id=18566482 OR id=22747687 OR id=51420625 OR id=75862064 OR id=26402882 OR id=93958561 OR id=85202979 OR id=97049369 OR id=67674725 OR id=9475653 OR id=92302381 OR id=78133617 OR id=49295001 OR id=36517340 OR id=81387142 OR id=15707241 OR id=60832834 OR id=93157830 OR id=64171432 OR id=58537826 OR id=70141767 OR id=7326025 OR id=36632075 OR id=9639624 OR id=8900056 OR id=99702164 OR id=35108945 OR id=87820933 OR id=57302965 OR id=16652391 OR id=41845132 OR id=62184393 OR id=70136913 OR id=79574630 OR id=32562398 OR id=94616790 OR id=61258220 OR id=73162018 OR id=81644480 OR id=19453596 OR id=97380163 OR id=1204733 OR id=33357040 OR id=84854495 OR id=13888863 OR id=49041868 OR id=89272326 OR id=38405345 OR id=571248 OR id=6349029 OR id=70755321 OR id=79307694 OR id=60619684 OR id=92624181 OR id=73135306 OR id=23279848 OR id=95612954 OR id=55845916 OR id=6223606 OR id=43836918 OR id=37459781 OR id=67969314 OR id=99398872 OR id=7616960 OR id=37189193 OR id=50151920 OR id=62881879 OR id=12364637 OR id=33204320 OR id=27135672 OR id=28441504 OR id=47373461 OR id=87967926 OR id=30631796 OR id=20053540 OR id=18735984 OR id=83406724;


#C组
#in和or中有300条数据的情况
SELECT * FROM test WHERE id IN (37092877,94859722,74276090,8763830,38727241,95732954,93414819,55070016,3591352,73857925,92290525,15210159,83905516,54934589,83004136,31442143,6060569,22209206,27649629,11464943,77822402,28714780,10058522,62252663,13751461,38997875,47320577,64507359,36137908,54297630,97411161,56542672,22017966,55190708,70072386,24300664,93413617,23621629,74772508,62774612,43001947,46161388,85563006,70177147,63960440,18001207,81734850,10635060,6551152,54877885,44426798,73950635,18713144,21690065,82153543,26048520,79954773,22411093,97307339,74193176,1413532,88006544,36062746,24043946,17132007,95958217,26112542,27303972,17247403,56778979,60928031,69369613,90584759,86234538,41726089,25315005,27568726,25091624,15307765,83130887,42726438,75872353,18991223,47819224,75457713,54659391,54889687,65229322,17124556,38376043,1989975,45973571,48597804,58632319,43388664,97010450,94745635,13217373,40472912,40220510,58319808,48228318,48936085,86281500,65466706,96815281,11751559,50188155,76649755,35315411,20360954,17739218,10918461,51429591,41447650,65170472,26810295,80912347,17157209,75851858,61150903,4408208,61200404,6655467,66863737,51549112,61951371,14368308,14663119,8762531,31765056,30560647,41048147,95526521,94929131,56881239,79014587,62705983,15892901,66151473,98846144,79336731,35949035,26250054,97536202,40575682,6965144,91059908,97939380,30854180,1965937,17193347,76584991,70467475,6559872,97386594,13939914,20379091,84906436,45989448,17337270,4949675,96963499,12561575,77153018,73213368,68283041,33977574,86290771,70381017,73095085,454900,44614195,48171334,49603342,7430998,29447060,47643508,82393912,83169846,94256496,35275444,40024984,25377535,46571333,32510994,70927802,92017916,97302502,22859741,32726786,79071601,93977472,47409421,49311618,77366144,84838598,59401507,67110877,42075938,76962007,27984930,72982484,81363683,75017478,88624177,67220235,88290070,26311443,87681081,77960250,4996033,68448074,67762279,99650583,36766422,27233152,71436659,25428777,81481679,51070397,88351803,78755075,26783938,83610840,45650662,86305644,1717314,66176062,6507047,45084786,74402982,55661367,35721238,40424913,24294239,30223531,55367671,56777532,12604154,4870493,14750488,74039611,42549918,70710424,56247316,63002053,71117605,16510883,67417211,34057637,74185092,58603491,66987830,73584171,9178319,47096502,1554825,37756804,85168245,92690138,6120773,99586029,74696745,61803307,56631845,42681796,58965644,68703695,69660559,15879062,26713059,85186928,63117471,53007808,74576547,32187857,13701205,88645881,24507258,87453800,39624977,75862710,62419627,70804059,10461373,18265782,56366177,68093007,75760763,43931574,65808002,49148775,98019987,71183123,53762434,78851856,37767085,89124453,47566746);

SELECT * FROM test WHERE id=37092877 OR id=94859722 OR id=74276090 OR id=8763830 OR id=38727241 OR id=95732954 OR id=93414819 OR id=55070016 OR id=3591352 OR id=73857925 OR id=92290525 OR id=15210159 OR id=83905516 OR id=54934589 OR id=83004136 OR id=31442143 OR id=6060569 OR id=22209206 OR id=27649629 OR id=11464943 OR id=77822402 OR id=28714780 OR id=10058522 OR id=62252663 OR id=13751461 OR id=38997875 OR id=47320577 OR id=64507359 OR id=36137908 OR id=54297630 OR id=97411161 OR id=56542672 OR id=22017966 OR id=55190708 OR id=70072386 OR id=24300664 OR id=93413617 OR id=23621629 OR id=74772508 OR id=62774612 OR id=43001947 OR id=46161388 OR id=85563006 OR id=70177147 OR id=63960440 OR id=18001207 OR id=81734850 OR id=10635060 OR id=6551152 OR id=54877885 OR id=44426798 OR id=73950635 OR id=18713144 OR id=21690065 OR id=82153543 OR id=26048520 OR id=79954773 OR id=22411093 OR id=97307339 OR id=74193176 OR id=1413532 OR id=88006544 OR id=36062746 OR id=24043946 OR id=17132007 OR id=95958217 OR id=26112542 OR id=27303972 OR id=17247403 OR id=56778979 OR id=60928031 OR id=69369613 OR id=90584759 OR id=86234538 OR id=41726089 OR id=25315005 OR id=27568726 OR id=25091624 OR id=15307765 OR id=83130887 OR id=42726438 OR id=75872353 OR id=18991223 OR id=47819224 OR id=75457713 OR id=54659391 OR id=54889687 OR id=65229322 OR id=17124556 OR id=38376043 OR id=1989975 OR id=45973571 OR id=48597804 OR id=58632319 OR id=43388664 OR id=97010450 OR id=94745635 OR id=13217373 OR id=40472912 OR id=40220510 OR id=58319808 OR id=48228318 OR id=48936085 OR id=86281500 OR id=65466706 OR id=96815281 OR id=11751559 OR id=50188155 OR id=76649755 OR id=35315411 OR id=20360954 OR id=17739218 OR id=10918461 OR id=51429591 OR id=41447650 OR id=65170472 OR id=26810295 OR id=80912347 OR id=17157209 OR id=75851858 OR id=61150903 OR id=4408208 OR id=61200404 OR id=6655467 OR id=66863737 OR id=51549112 OR id=61951371 OR id=14368308 OR id=14663119 OR id=8762531 OR id=31765056 OR id=30560647 OR id=41048147 OR id=95526521 OR id=94929131 OR id=56881239 OR id=79014587 OR id=62705983 OR id=15892901 OR id=66151473 OR id=98846144 OR id=79336731 OR id=35949035 OR id=26250054 OR id=97536202 OR id=40575682 OR id=6965144 OR id=91059908 OR id=97939380 OR id=30854180 OR id=1965937 OR id=17193347 OR id=76584991 OR id=70467475 OR id=6559872 OR id=97386594 OR id=13939914 OR id=20379091 OR id=84906436 OR id=45989448 OR id=17337270 OR id=4949675 OR id=96963499 OR id=12561575 OR id=77153018 OR id=73213368 OR id=68283041 OR id=33977574 OR id=86290771 OR id=70381017 OR id=73095085 OR id=454900 OR id=44614195 OR id=48171334 OR id=49603342 OR id=7430998 OR id=29447060 OR id=47643508 OR id=82393912 OR id=83169846 OR id=94256496 OR id=35275444 OR id=40024984 OR id=25377535 OR id=46571333 OR id=32510994 OR id=70927802 OR id=92017916 OR id=97302502 OR id=22859741 OR id=32726786 OR id=79071601 OR id=93977472 OR id=47409421 OR id=49311618 OR id=77366144 OR id=84838598 OR id=59401507 OR id=67110877 OR id=42075938 OR id=76962007 OR id=27984930 OR id=72982484 OR id=81363683 OR id=75017478 OR id=88624177 OR id=67220235 OR id=88290070 OR id=26311443 OR id=87681081 OR id=77960250 OR id=4996033 OR id=68448074 OR id=67762279 OR id=99650583 OR id=36766422 OR id=27233152 OR id=71436659 OR id=25428777 OR id=81481679 OR id=51070397 OR id=88351803 OR id=78755075 OR id=26783938 OR id=83610840 OR id=45650662 OR id=86305644 OR id=1717314 OR id=66176062 OR id=6507047 OR id=45084786 OR id=74402982 OR id=55661367 OR id=35721238 OR id=40424913 OR id=24294239 OR id=30223531 OR id=55367671 OR id=56777532 OR id=12604154 OR id=4870493 OR id=14750488 OR id=74039611 OR id=42549918 OR id=70710424 OR id=56247316 OR id=63002053 OR id=71117605 OR id=16510883 OR id=67417211 OR id=34057637 OR id=74185092 OR id=58603491 OR id=66987830 OR id=73584171 OR id=9178319 OR id=47096502 OR id=1554825 OR id=37756804 OR id=85168245 OR id=92690138 OR id=6120773 OR id=99586029 OR id=74696745 OR id=61803307 OR id=56631845 OR id=42681796 OR id=58965644 OR id=68703695 OR id=69660559 OR id=15879062 OR id=26713059 OR id=85186928 OR id=63117471 OR id=53007808 OR id=74576547 OR id=32187857 OR id=13701205 OR id=88645881 OR id=24507258 OR id=87453800 OR id=39624977 OR id=75862710 OR id=62419627 OR id=70804059 OR id=10461373 OR id=18265782 OR id=56366177 OR id=68093007 OR id=75760763 OR id=43931574 OR id=65808002 OR id=49148775 OR id=98019987 OR id=71183123 OR id=53762434 OR id=78851856 OR id=37767085 OR id=89124453 OR id=47566746;


#D组
#in和or中有1000条数据的情况
SELECT * FROM test WHERE id IN (93674701,9720356,31732184,53855095,33144472,71864888,27541768,27238726,83648428,12942332,26918445,19781953,81861032,74800064,12286132,6624397,64942581,70512799,46356598,88292448,87069909,38175756,98121997,62570414,15900806,51527968,89092372,8084203,53772848,78871524,3608561,85909562,41702172,61800503,57877634,93407278,30824340,13159046,49055339,73058078,983603,73571456,51694978,75136628,82716874,83551181,7964224,47505945,92695321,15885152,79282709,18572099,27392970,14552787,19848227,4518183,11773920,22285326,71605145,2402625,63365854,70973600,10584706,83688869,84268419,6026005,36545233,24462648,19293921,17561083,52105483,59243514,35230465,34650779,30053489,24225251,59642405,81933853,94495716,26364324,25980634,5579237,14569289,89417845,71178959,4143920,20467990,53316808,21288525,82249537,37737589,44712689,36788133,15668654,4697556,63785060,11555169,36401204,92276179,4135929,75453019,28231031,8649240,11576980,20262028,56242424,11305608,5655216,90240601,28569373,5296027,10739594,72751648,22531251,12535926,36347415,19740655,69125465,7523885,88128548,88830806,25010302,29411467,99614288,32646290,16592563,69036910,32604729,88737786,90169676,57646877,72105460,40027541,70362483,37221415,25284914,69691185,17972978,1544661,47324366,25337670,91133621,63697117,48652228,18538437,79966496,26066529,65334307,8305141,86289387,20178085,88836090,74948034,14101728,7837868,83548120,65602502,83129211,24785681,65000269,49140174,62636621,31096695,52276400,28546681,83631937,57100225,42531528,28326396,38641032,93055463,20525612,66073509,35154065,29007664,12600294,76829494,73917074,67226149,12478806,39842542,70312958,82792046,49668650,46280815,96555182,22966062,83158116,87566530,66277804,7944142,90649884,64342810,9881875,14833854,82959569,50523207,48788762,3801076,14677723,63080506,96215352,36302231,35067168,11695282,19447382,66401373,40822285,41406321,48630216,78955925,57194625,52097877,16169037,44834346,2593695,29948466,41842778,50510473,39669493,64590865,26160800,94882286,2703212,41243905,89363549,82819429,25565895,86836890,58385785,55898457,99305620,43332680,98223672,4494624,25408421,28054121,48197701,90633404,25825550,90631154,24867226,61846156,38911183,67826056,10676975,57116645,474292,82387517,56211477,46555785,49282428,99468990,81172472,26720330,38692582,96073680,88412290,28829489,1816508,75321051,81650509,23175973,42008725,60743468,52532114,731909,77811415,86804961,29675484,33584929,180367,93687804,41093066,5987495,27291494,78229979,63194139,34357776,9992084,22643334,22407822,69740170,29581361,50036776,88768091,82537322,83709895,55361776,90616169,44595355,9468440,54552233,73496954,46104486,92947715,38522993,88515232,57725249,48507967,25309486,91597013,85635814,69579638,68775627,57556546,77900275,95965693,9601780,5448068,54075952,64335883,80114875,14793294,21016639,1959922,93176996,7893733,51407895,45849129,33857790,30096194,78021982,66555961,15842998,77678123,56648395,8171848,80152264,78616680,80098122,22882409,77242219,3124519,60865422,43164198,43256621,73261157,12541949,49780175,23167183,10509251,41809106,25655902,6752559,39850293,50992519,40061483,84526968,93056718,53267125,53914467,39404926,83672449,21484465,34147538,13437853,74079093,50400032,85705998,7557614,10300505,79264856,65669946,23899714,53506926,36081544,11113765,65755643,5826515,60392667,55562374,98132987,80904530,92663352,7283593,3709276,52078745,84847057,34235334,63889320,70036669,58603533,27394053,54766781,50920854,80202681,67618417,82912294,20150728,20042189,86403320,38738266,58393070,50887299,12170654,16212895,37361223,13677457,19503506,20213757,84240441,39618969,26401150,47937678,55871130,79189571,5717133,12444503,95283334,14827147,22008485,56345882,43237192,56980197,68699371,46407250,72120555,70694039,46438829,17774982,36484024,138767,89563532,54847019,7815592,44909604,50479084,17462504,96594465,58317102,92426225,91894699,4501659,43315607,9442814,19705166,87751308,95588126,92372510,20281564,19251355,10321183,34573093,19074704,84678191,24383998,27670253,50223562,34091936,99304371,32477827,54273037,86525073,73253547,33316827,6724062,76707318,78171148,44729510,16697684,68966388,57448392,51380186,35344477,98153122,51825492,27202774,26901641,37527637,88241695,15100257,30418000,21821200,95511035,9289513,83870196,54628801,39402988,88345504,84232433,13925255,70816934,6822742,14400466,430652,87397095,89773413,10883914,89939310,39597573,49356789,62857680,93292662,55644642,81922551,94304087,63705961,137763,22392805,65195561,39498904,22576234,59467794,46389072,66341462,44602153,18204976,45366397,3880945,98231882,27999162,38209350,10599910,77139550,35114264,57109708,93064441,34801782,24938667,84955486,53018874,37969943,64372852,69596670,21288762,12774121,97588451,23575359,10954061,50363988,56263940,61520763,85096643,36250068,19807406,20984386,24520668,44631794,62587890,44963362,7663521,78505677,98442373,90280978,14494324,16069861,11397153,87726305,26133866,42024935,93393929,72575268,76384597,42272046,81658814,40811718,86054463,35997739,51075676,62839927,68179261,19292480,10464999,6342696,75842285,28671096,30029838,19617648,94667632,75855376,83477767,456684,81197213,1961395,79590898,470693,64786459,90138714,30486571,75566704,64467558,21380112,17742907,7733647,92017,64615799,72272722,66873854,77198963,35594848,42694993,12431322,2247181,11020746,42416726,19127785,95444937,36842133,4203521,48149533,45322440,59710953,38250773,31370132,26889920,45927952,55298246,31197238,44744953,35531670,38850041,29759177,76433451,33696500,2823716,68574340,68889919,35744793,64772909,41562277,72606631,54617176,76086087,61060196,1593669,4666059,44201567,97015910,51039786,47534369,36899420,95163693,34278055,24361819,93200909,29991418,63172824,53644148,61454424,44726508,64910883,31088636,14005026,83267869,28497493,12406441,34686539,70646963,7687253,23115957,64556990,49701688,76843379,22370877,11199132,15492661,72101877,47154152,54969058,96696025,33567129,95788960,13301506,38695877,52992551,37817234,82136809,28111091,84977065,93404791,56350318,27576451,84170153,37381626,22432144,35119973,23922989,98961080,14336913,49612713,47410677,41559348,64216475,75502736,16203656,81726720,64541981,82181762,95869963,1086041,76856852,99484886,47292021,99746735,79082859,67416188,46391963,58631281,80994168,9464550,5851058,16534935,63307701,91875109,18716507,15870646,6003995,836024,35610568,39574140,76244639,83403189,51252728,6516065,94907007,81605606,40398075,40258386,6692981,50852074,2869416,97682971,44427361,9608914,58464559,81806036,20047387,66264452,58063775,54179837,48463792,17877188,31718426,64192249,35574859,3671766,88905164,78137697,46929619,21063327,83078770,93293821,41618319,3832324,91310612,79854291,68734227,8826717,80881657,95208907,7079422,30037415,5494004,44809486,97620027,35689182,13120783,26108678,1537176,16538727,50841024,36515680,82635278,11112660,16276555,72997511,93487848,88201238,53997085,15198916,61214583,78412499,3585265,1402827,56445518,47661453,25615629,58263458,62155263,46608555,15822703,82285214,76021596,84571697,45999350,40074628,8219220,5429523,74024203,22354037,17605466,60436920,52777032,65801717,43656316,10424270,48035786,29493228,83897372,62101275,84793857,56894828,70636689,72497148,67388694,68146510,64298548,97117498,25553211,54226533,90395845,24172623,91712292,98280822,54042497,25032894,6833135,39011254,9837753,63507766,26747954,45941264,99955245,80051546,78510759,71322333,92407609,95809491,18999217,23430377,11861293,42583098,24163209,11358738,3237302,3176665,87151132,2789150,63905882,59864282,3673596,19570439,22883042,72375525,51614404,47526636,98443133,99140135,33855918,28333489,81416033,2670097,4897577,24439616,36643479,40817600,76022791,40072872,95193435,96967607,24983145,49883271,94602753,83555050,85455145,34563229,72328311,12002151,71481181,72998351,1489188,38426973,91893116,61594591,89693630,6268166,20056665,62169880,17143472,35103925,22452590,54272289,34236829,78028543,84474414,40386926,50550952,49413559,48781941,22927237,44447815,29960478,47578119,10192558,87733936,88699383,38808712,79944807,84014713,31865463,72617685,19557568,47865990,39069638,20086122,1777562,29018078,78358083,94561719,46281152,99789008,86929490,16534451,55989144,52455669,54561585,97379646,20416183,87617750,76115505,3282482,8383619,45456319,29576432,67750627,61736333,33745442,51502165,35349384,78106651,23232822,94851387,78254073,82406754,10317954,70125940,45067526,27061875,25640164,52574899,93819227,93789607,96122951,31673246,70431904,54067896,37146857,37817889,14058940,60710246,64844350,91604383,71972005,13888349,19093493,27397281,61085409,66529387,82761299,72236310,19277077,96599501,68304096,48292937,97503321,88011133,29224803,79782945,79965966,83716914,90432214,48938902,12498489,30246261,91624049,68652396,23677785,44084687,3865123,37823170,45287730,38784682,28058351,68226368,61569897,44737876,70575908,25568463,24668386,88650569,35559584,1897737,77844785,29780669,84004602,29029776,91003545,48058106,9463847);

SELECT * FROM test WHERE id=93674701 OR id=9720356 OR id=31732184 OR id=53855095 OR id=33144472 OR id=71864888 OR id=27541768 OR id=27238726 OR id=83648428 OR id=12942332 OR id=26918445 OR id=19781953 OR id=81861032 OR id=74800064 OR id=12286132 OR id=6624397 OR id=64942581 OR id=70512799 OR id=46356598 OR id=88292448 OR id=87069909 OR id=38175756 OR id=98121997 OR id=62570414 OR id=15900806 OR id=51527968 OR id=89092372 OR id=8084203 OR id=53772848 OR id=78871524 OR id=3608561 OR id=85909562 OR id=41702172 OR id=61800503 OR id=57877634 OR id=93407278 OR id=30824340 OR id=13159046 OR id=49055339 OR id=73058078 OR id=983603 OR id=73571456 OR id=51694978 OR id=75136628 OR id=82716874 OR id=83551181 OR id=7964224 OR id=47505945 OR id=92695321 OR id=15885152 OR id=79282709 OR id=18572099 OR id=27392970 OR id=14552787 OR id=19848227 OR id=4518183 OR id=11773920 OR id=22285326 OR id=71605145 OR id=2402625 OR id=63365854 OR id=70973600 OR id=10584706 OR id=83688869 OR id=84268419 OR id=6026005 OR id=36545233 OR id=24462648 OR id=19293921 OR id=17561083 OR id=52105483 OR id=59243514 OR id=35230465 OR id=34650779 OR id=30053489 OR id=24225251 OR id=59642405 OR id=81933853 OR id=94495716 OR id=26364324 OR id=25980634 OR id=5579237 OR id=14569289 OR id=89417845 OR id=71178959 OR id=4143920 OR id=20467990 OR id=53316808 OR id=21288525 OR id=82249537 OR id=37737589 OR id=44712689 OR id=36788133 OR id=15668654 OR id=4697556 OR id=63785060 OR id=11555169 OR id=36401204 OR id=92276179 OR id=4135929 OR id=75453019 OR id=28231031 OR id=8649240 OR id=11576980 OR id=20262028 OR id=56242424 OR id=11305608 OR id=5655216 OR id=90240601 OR id=28569373 OR id=5296027 OR id=10739594 OR id=72751648 OR id=22531251 OR id=12535926 OR id=36347415 OR id=19740655 OR id=69125465 OR id=7523885 OR id=88128548 OR id=88830806 OR id=25010302 OR id=29411467 OR id=99614288 OR id=32646290 OR id=16592563 OR id=69036910 OR id=32604729 OR id=88737786 OR id=90169676 OR id=57646877 OR id=72105460 OR id=40027541 OR id=70362483 OR id=37221415 OR id=25284914 OR id=69691185 OR id=17972978 OR id=1544661 OR id=47324366 OR id=25337670 OR id=91133621 OR id=63697117 OR id=48652228 OR id=18538437 OR id=79966496 OR id=26066529 OR id=65334307 OR id=8305141 OR id=86289387 OR id=20178085 OR id=88836090 OR id=74948034 OR id=14101728 OR id=7837868 OR id=83548120 OR id=65602502 OR id=83129211 OR id=24785681 OR id=65000269 OR id=49140174 OR id=62636621 OR id=31096695 OR id=52276400 OR id=28546681 OR id=83631937 OR id=57100225 OR id=42531528 OR id=28326396 OR id=38641032 OR id=93055463 OR id=20525612 OR id=66073509 OR id=35154065 OR id=29007664 OR id=12600294 OR id=76829494 OR id=73917074 OR id=67226149 OR id=12478806 OR id=39842542 OR id=70312958 OR id=82792046 OR id=49668650 OR id=46280815 OR id=96555182 OR id=22966062 OR id=83158116 OR id=87566530 OR id=66277804 OR id=7944142 OR id=90649884 OR id=64342810 OR id=9881875 OR id=14833854 OR id=82959569 OR id=50523207 OR id=48788762 OR id=3801076 OR id=14677723 OR id=63080506 OR id=96215352 OR id=36302231 OR id=35067168 OR id=11695282 OR id=19447382 OR id=66401373 OR id=40822285 OR id=41406321 OR id=48630216 OR id=78955925 OR id=57194625 OR id=52097877 OR id=16169037 OR id=44834346 OR id=2593695 OR id=29948466 OR id=41842778 OR id=50510473 OR id=39669493 OR id=64590865 OR id=26160800 OR id=94882286 OR id=2703212 OR id=41243905 OR id=89363549 OR id=82819429 OR id=25565895 OR id=86836890 OR id=58385785 OR id=55898457 OR id=99305620 OR id=43332680 OR id=98223672 OR id=4494624 OR id=25408421 OR id=28054121 OR id=48197701 OR id=90633404 OR id=25825550 OR id=90631154 OR id=24867226 OR id=61846156 OR id=38911183 OR id=67826056 OR id=10676975 OR id=57116645 OR id=474292 OR id=82387517 OR id=56211477 OR id=46555785 OR id=49282428 OR id=99468990 OR id=81172472 OR id=26720330 OR id=38692582 OR id=96073680 OR id=88412290 OR id=28829489 OR id=1816508 OR id=75321051 OR id=81650509 OR id=23175973 OR id=42008725 OR id=60743468 OR id=52532114 OR id=731909 OR id=77811415 OR id=86804961 OR id=29675484 OR id=33584929 OR id=180367 OR id=93687804 OR id=41093066 OR id=5987495 OR id=27291494 OR id=78229979 OR id=63194139 OR id=34357776 OR id=9992084 OR id=22643334 OR id=22407822 OR id=69740170 OR id=29581361 OR id=50036776 OR id=88768091 OR id=82537322 OR id=83709895 OR id=55361776 OR id=90616169 OR id=44595355 OR id=9468440 OR id=54552233 OR id=73496954 OR id=46104486 OR id=92947715 OR id=38522993 OR id=88515232 OR id=57725249 OR id=48507967 OR id=25309486 OR id=91597013 OR id=85635814 OR id=69579638 OR id=68775627 OR id=57556546 OR id=77900275 OR id=95965693 OR id=9601780 OR id=5448068 OR id=54075952 OR id=64335883 OR id=80114875 OR id=14793294 OR id=21016639 OR id=1959922 OR id=93176996 OR id=7893733 OR id=51407895 OR id=45849129 OR id=33857790 OR id=30096194 OR id=78021982 OR id=66555961 OR id=15842998 OR id=77678123 OR id=56648395 OR id=8171848 OR id=80152264 OR id=78616680 OR id=80098122 OR id=22882409 OR id=77242219 OR id=3124519 OR id=60865422 OR id=43164198 OR id=43256621 OR id=73261157 OR id=12541949 OR id=49780175 OR id=23167183 OR id=10509251 OR id=41809106 OR id=25655902 OR id=6752559 OR id=39850293 OR id=50992519 OR id=40061483 OR id=84526968 OR id=93056718 OR id=53267125 OR id=53914467 OR id=39404926 OR id=83672449 OR id=21484465 OR id=34147538 OR id=13437853 OR id=74079093 OR id=50400032 OR id=85705998 OR id=7557614 OR id=10300505 OR id=79264856 OR id=65669946 OR id=23899714 OR id=53506926 OR id=36081544 OR id=11113765 OR id=65755643 OR id=5826515 OR id=60392667 OR id=55562374 OR id=98132987 OR id=80904530 OR id=92663352 OR id=7283593 OR id=3709276 OR id=52078745 OR id=84847057 OR id=34235334 OR id=63889320 OR id=70036669 OR id=58603533 OR id=27394053 OR id=54766781 OR id=50920854 OR id=80202681 OR id=67618417 OR id=82912294 OR id=20150728 OR id=20042189 OR id=86403320 OR id=38738266 OR id=58393070 OR id=50887299 OR id=12170654 OR id=16212895 OR id=37361223 OR id=13677457 OR id=19503506 OR id=20213757 OR id=84240441 OR id=39618969 OR id=26401150 OR id=47937678 OR id=55871130 OR id=79189571 OR id=5717133 OR id=12444503 OR id=95283334 OR id=14827147 OR id=22008485 OR id=56345882 OR id=43237192 OR id=56980197 OR id=68699371 OR id=46407250 OR id=72120555 OR id=70694039 OR id=46438829 OR id=17774982 OR id=36484024 OR id=138767 OR id=89563532 OR id=54847019 OR id=7815592 OR id=44909604 OR id=50479084 OR id=17462504 OR id=96594465 OR id=58317102 OR id=92426225 OR id=91894699 OR id=4501659 OR id=43315607 OR id=9442814 OR id=19705166 OR id=87751308 OR id=95588126 OR id=92372510 OR id=20281564 OR id=19251355 OR id=10321183 OR id=34573093 OR id=19074704 OR id=84678191 OR id=24383998 OR id=27670253 OR id=50223562 OR id=34091936 OR id=99304371 OR id=32477827 OR id=54273037 OR id=86525073 OR id=73253547 OR id=33316827 OR id=6724062 OR id=76707318 OR id=78171148 OR id=44729510 OR id=16697684 OR id=68966388 OR id=57448392 OR id=51380186 OR id=35344477 OR id=98153122 OR id=51825492 OR id=27202774 OR id=26901641 OR id=37527637 OR id=88241695 OR id=15100257 OR id=30418000 OR id=21821200 OR id=95511035 OR id=9289513 OR id=83870196 OR id=54628801 OR id=39402988 OR id=88345504 OR id=84232433 OR id=13925255 OR id=70816934 OR id=6822742 OR id=14400466 OR id=430652 OR id=87397095 OR id=89773413 OR id=10883914 OR id=89939310 OR id=39597573 OR id=49356789 OR id=62857680 OR id=93292662 OR id=55644642 OR id=81922551 OR id=94304087 OR id=63705961 OR id=137763 OR id=22392805 OR id=65195561 OR id=39498904 OR id=22576234 OR id=59467794 OR id=46389072 OR id=66341462 OR id=44602153 OR id=18204976 OR id=45366397 OR id=3880945 OR id=98231882 OR id=27999162 OR id=38209350 OR id=10599910 OR id=77139550 OR id=35114264 OR id=57109708 OR id=93064441 OR id=34801782 OR id=24938667 OR id=84955486 OR id=53018874 OR id=37969943 OR id=64372852 OR id=69596670 OR id=21288762 OR id=12774121 OR id=97588451 OR id=23575359 OR id=10954061 OR id=50363988 OR id=56263940 OR id=61520763 OR id=85096643 OR id=36250068 OR id=19807406 OR id=20984386 OR id=24520668 OR id=44631794 OR id=62587890 OR id=44963362 OR id=7663521 OR id=78505677 OR id=98442373 OR id=90280978 OR id=14494324 OR id=16069861 OR id=11397153 OR id=87726305 OR id=26133866 OR id=42024935 OR id=93393929 OR id=72575268 OR id=76384597 OR id=42272046 OR id=81658814 OR id=40811718 OR id=86054463 OR id=35997739 OR id=51075676 OR id=62839927 OR id=68179261 OR id=19292480 OR id=10464999 OR id=6342696 OR id=75842285 OR id=28671096 OR id=30029838 OR id=19617648 OR id=94667632 OR id=75855376 OR id=83477767 OR id=456684 OR id=81197213 OR id=1961395 OR id=79590898 OR id=470693 OR id=64786459 OR id=90138714 OR id=30486571 OR id=75566704 OR id=64467558 OR id=21380112 OR id=17742907 OR id=7733647 OR id=92017 OR id=64615799 OR id=72272722 OR id=66873854 OR id=77198963 OR id=35594848 OR id=42694993 OR id=12431322 OR id=2247181 OR id=11020746 OR id=42416726 OR id=19127785 OR id=95444937 OR id=36842133 OR id=4203521 OR id=48149533 OR id=45322440 OR id=59710953 OR id=38250773 OR id=31370132 OR id=26889920 OR id=45927952 OR id=55298246 OR id=31197238 OR id=44744953 OR id=35531670 OR id=38850041 OR id=29759177 OR id=76433451 OR id=33696500 OR id=2823716 OR id=68574340 OR id=68889919 OR id=35744793 OR id=64772909 OR id=41562277 OR id=72606631 OR id=54617176 OR id=76086087 OR id=61060196 OR id=1593669 OR id=4666059 OR id=44201567 OR id=97015910 OR id=51039786 OR id=47534369 OR id=36899420 OR id=95163693 OR id=34278055 OR id=24361819 OR id=93200909 OR id=29991418 OR id=63172824 OR id=53644148 OR id=61454424 OR id=44726508 OR id=64910883 OR id=31088636 OR id=14005026 OR id=83267869 OR id=28497493 OR id=12406441 OR id=34686539 OR id=70646963 OR id=7687253 OR id=23115957 OR id=64556990 OR id=49701688 OR id=76843379 OR id=22370877 OR id=11199132 OR id=15492661 OR id=72101877 OR id=47154152 OR id=54969058 OR id=96696025 OR id=33567129 OR id=95788960 OR id=13301506 OR id=38695877 OR id=52992551 OR id=37817234 OR id=82136809 OR id=28111091 OR id=84977065 OR id=93404791 OR id=56350318 OR id=27576451 OR id=84170153 OR id=37381626 OR id=22432144 OR id=35119973 OR id=23922989 OR id=98961080 OR id=14336913 OR id=49612713 OR id=47410677 OR id=41559348 OR id=64216475 OR id=75502736 OR id=16203656 OR id=81726720 OR id=64541981 OR id=82181762 OR id=95869963 OR id=1086041 OR id=76856852 OR id=99484886 OR id=47292021 OR id=99746735 OR id=79082859 OR id=67416188 OR id=46391963 OR id=58631281 OR id=80994168 OR id=9464550 OR id=5851058 OR id=16534935 OR id=63307701 OR id=91875109 OR id=18716507 OR id=15870646 OR id=6003995 OR id=836024 OR id=35610568 OR id=39574140 OR id=76244639 OR id=83403189 OR id=51252728 OR id=6516065 OR id=94907007 OR id=81605606 OR id=40398075 OR id=40258386 OR id=6692981 OR id=50852074 OR id=2869416 OR id=97682971 OR id=44427361 OR id=9608914 OR id=58464559 OR id=81806036 OR id=20047387 OR id=66264452 OR id=58063775 OR id=54179837 OR id=48463792 OR id=17877188 OR id=31718426 OR id=64192249 OR id=35574859 OR id=3671766 OR id=88905164 OR id=78137697 OR id=46929619 OR id=21063327 OR id=83078770 OR id=93293821 OR id=41618319 OR id=3832324 OR id=91310612 OR id=79854291 OR id=68734227 OR id=8826717 OR id=80881657 OR id=95208907 OR id=7079422 OR id=30037415 OR id=5494004 OR id=44809486 OR id=97620027 OR id=35689182 OR id=13120783 OR id=26108678 OR id=1537176 OR id=16538727 OR id=50841024 OR id=36515680 OR id=82635278 OR id=11112660 OR id=16276555 OR id=72997511 OR id=93487848 OR id=88201238 OR id=53997085 OR id=15198916 OR id=61214583 OR id=78412499 OR id=3585265 OR id=1402827 OR id=56445518 OR id=47661453 OR id=25615629 OR id=58263458 OR id=62155263 OR id=46608555 OR id=15822703 OR id=82285214 OR id=76021596 OR id=84571697 OR id=45999350 OR id=40074628 OR id=8219220 OR id=5429523 OR id=74024203 OR id=22354037 OR id=17605466 OR id=60436920 OR id=52777032 OR id=65801717 OR id=43656316 OR id=10424270 OR id=48035786 OR id=29493228 OR id=83897372 OR id=62101275 OR id=84793857 OR id=56894828 OR id=70636689 OR id=72497148 OR id=67388694 OR id=68146510 OR id=64298548 OR id=97117498 OR id=25553211 OR id=54226533 OR id=90395845 OR id=24172623 OR id=91712292 OR id=98280822 OR id=54042497 OR id=25032894 OR id=6833135 OR id=39011254 OR id=9837753 OR id=63507766 OR id=26747954 OR id=45941264 OR id=99955245 OR id=80051546 OR id=78510759 OR id=71322333 OR id=92407609 OR id=95809491 OR id=18999217 OR id=23430377 OR id=11861293 OR id=42583098 OR id=24163209 OR id=11358738 OR id=3237302 OR id=3176665 OR id=87151132 OR id=2789150 OR id=63905882 OR id=59864282 OR id=3673596 OR id=19570439 OR id=22883042 OR id=72375525 OR id=51614404 OR id=47526636 OR id=98443133 OR id=99140135 OR id=33855918 OR id=28333489 OR id=81416033 OR id=2670097 OR id=4897577 OR id=24439616 OR id=36643479 OR id=40817600 OR id=76022791 OR id=40072872 OR id=95193435 OR id=96967607 OR id=24983145 OR id=49883271 OR id=94602753 OR id=83555050 OR id=85455145 OR id=34563229 OR id=72328311 OR id=12002151 OR id=71481181 OR id=72998351 OR id=1489188 OR id=38426973 OR id=91893116 OR id=61594591 OR id=89693630 OR id=6268166 OR id=20056665 OR id=62169880 OR id=17143472 OR id=35103925 OR id=22452590 OR id=54272289 OR id=34236829 OR id=78028543 OR id=84474414 OR id=40386926 OR id=50550952 OR id=49413559 OR id=48781941 OR id=22927237 OR id=44447815 OR id=29960478 OR id=47578119 OR id=10192558 OR id=87733936 OR id=88699383 OR id=38808712 OR id=79944807 OR id=84014713 OR id=31865463 OR id=72617685 OR id=19557568 OR id=47865990 OR id=39069638 OR id=20086122 OR id=1777562 OR id=29018078 OR id=78358083 OR id=94561719 OR id=46281152 OR id=99789008 OR id=86929490 OR id=16534451 OR id=55989144 OR id=52455669 OR id=54561585 OR id=97379646 OR id=20416183 OR id=87617750 OR id=76115505 OR id=3282482 OR id=8383619 OR id=45456319 OR id=29576432 OR id=67750627 OR id=61736333 OR id=33745442 OR id=51502165 OR id=35349384 OR id=78106651 OR id=23232822 OR id=94851387 OR id=78254073 OR id=82406754 OR id=10317954 OR id=70125940 OR id=45067526 OR id=27061875 OR id=25640164 OR id=52574899 OR id=93819227 OR id=93789607 OR id=96122951 OR id=31673246 OR id=70431904 OR id=54067896 OR id=37146857 OR id=37817889 OR id=14058940 OR id=60710246 OR id=64844350 OR id=91604383 OR id=71972005 OR id=13888349 OR id=19093493 OR id=27397281 OR id=61085409 OR id=66529387 OR id=82761299 OR id=72236310 OR id=19277077 OR id=96599501 OR id=68304096 OR id=48292937 OR id=97503321 OR id=88011133 OR id=29224803 OR id=79782945 OR id=79965966 OR id=83716914 OR id=90432214 OR id=48938902 OR id=12498489 OR id=30246261 OR id=91624049 OR id=68652396 OR id=23677785 OR id=44084687 OR id=3865123 OR id=37823170 OR id=45287730 OR id=38784682 OR id=28058351 OR id=68226368 OR id=61569897 OR id=44737876 OR id=70575908 OR id=25568463 OR id=24668386 OR id=88650569 OR id=35559584 OR id=1897737 OR id=77844785 OR id=29780669 OR id=84004602 OR id=29029776 OR id=91003545 OR id=48058106 OR id=9463847;
```
测试结果如下：
第一种情况，ID列为主键的情况，4组测试执行计划一样，执行的时间也基本没有区别。
A组or和in的执行时间： or的执行时间为：0.002s     in的执行时间为：0.002s
B组or和in的执行时间： or的执行时间为：0.004s     in的执行时间为：0.004s
C组or和in的执行时间： or的执行时间为：0.006s     in的执行时间为：0.005s
D组or和in的执行时间： or的执行时间为：0.018s     in的执行时间为：0.014s
第二种情况，ID列为一般索引的情况，4组测试执行计划一样，执行的时间也基本没有区别。
A组or和in的执行时间： or的执行时间为：0.002s     in的执行时间为：0.002s
B组or和in的执行时间： or的执行时间为：0.006s     in的执行时间为：0.005s  
C组or和in的执行时间： or的执行时间为：0.008s     in的执行时间为：0.008s
D组or和in的执行时间： or的执行时间为：0.021s     in的执行时间为：0.020s  
第三种情况，ID列没有索引的情况，4组测试执行计划一样，执行的时间有很大的区别。
A组or和in的执行时间： or的执行时间为：5.016s      in的执行时间为：5.071s
B组or和in的执行时间： or的执行时间为：1min 02s     in的执行时间为：5.018s
C组or和in的执行时间： or的执行时间为：1min 55s     in的执行时间为：5.018s
D组or和in的执行时间： or的执行时间为：6min 17s     in的执行时间为：5.057s

**结论：从上面的测试结果，可以看出如果in和or所在列有索引或者主键的话，or和in没啥差别，执行计划和执行时间都几乎一样。如果in和or所在列没有索引的话，性能差别就很大了。在没有索引的情况下，随着in或者or后面的数据量越多，in的效率不会有太大的下降，但是or会随着记录越多的话性能下降非常厉害，从第三种测试情况中可以很明显地看出了，基本上是指数级增长。因此在给in和or的效率下定义的时候，应该再加上一个条件，就是所在的列是否有索引或者是否是主键。如果有索引或者主键性能没啥差别，如果没有索引，性能差别不是一点点！** 

![](https://cdn.nlark.com/yuque/0/2023/jpeg/21376908/1692002570088-3338946f-42b3-4174-8910-7e749c31e950.jpeg#averageHue=%23f9f8f8&from=url&id=qptNa&originHeight=78&originWidth=1400&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=shadow&title=)
## 模糊查询like

---

模糊查询又被称为模糊匹配，在实际开发中使用较多，比如：查询公司中所有姓张的，查询岗位中带有经理两个字的职位等等，这些都需要使用模糊查询。
模糊查询的语法格式如下：
```sql
select .. from .. where 字段 like '通配符表达式';
```
在模糊查询中，通配符主要包括两个：一个是%，一个是下划线_。其中%代表任意多个字符。下划线_代表任意一个字符。
案例1：查询员工名字以'S'开始的员工姓名
```sql
select ename from emp where ename like 'S%';
```
![image.png](https://cdn.nlark.com/yuque/0/2021/png/21376908/1622000884924-f3303ff0-cb9a-4393-831c-01d3e705606d.png#averageHue=%230f0e0d&height=201&id=nTI0r&originHeight=201&originWidth=636&originalType=binary&ratio=1&rotation=0&showTitle=false&size=11624&status=done&style=shadow&title=&width=636)
案例2：查询员工名字以'T'结尾的员工姓名
```sql
select ename from emp where ename like '%T';
```
![image.png](https://cdn.nlark.com/yuque/0/2021/png/21376908/1622000970235-0265da36-1e10-4da5-abb8-c651452fad21.png#averageHue=%230f0e0d&height=188&id=skACT&originHeight=188&originWidth=624&originalType=binary&ratio=1&rotation=0&showTitle=false&size=10432&status=done&style=shadow&title=&width=624)
案例3：查询员工名字中含有'O'的员工姓名
```sql
select ename from emp where ename like '%O%';
```
![image.png](https://cdn.nlark.com/yuque/0/2021/png/21376908/1622001027995-71da44df-e3b1-4e56-a6e2-922a50ccc2b7.png#averageHue=%230f0e0e&height=231&id=Aa56U&originHeight=231&originWidth=632&originalType=binary&ratio=1&rotation=0&showTitle=false&size=13088&status=done&style=shadow&title=&width=632)
![](https://cdn.nlark.com/yuque/0/2023/jpeg/21376908/1692002570088-3338946f-42b3-4174-8910-7e749c31e950.jpeg#averageHue=%23f9f8f8&from=url&id=Kl5BB&originHeight=78&originWidth=1400&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=shadow&title=)
案例4：查询员工名字中第二个字母是'A'的员工姓名
```sql
select ename from emp where ename like '_A%';
```
![image.png](https://cdn.nlark.com/yuque/0/2021/png/21376908/1622001108864-1abbac56-669f-4c35-9b48-6d80452ad8ce.png#averageHue=%230f0e0d&height=226&id=ICQ6h&originHeight=226&originWidth=636&originalType=binary&ratio=1&rotation=0&showTitle=false&size=13307&status=done&style=shadow&title=&width=636)
案例5：查询学员名字中含有下划线的。
执行以下SQL语句，先准备测试数据：
```sql
drop table if exists student;
create table student(
  id int,
  name varchar(255)
);
insert into student(id,name) values(1, 'susan');
insert into student(id,name) values(2, 'lucy');
insert into student(id,name) values(3, 'jack_son');
select * from student;
```
![image.png](https://cdn.nlark.com/yuque/0/2021/png/21376908/1622001536746-e0d05c73-f941-4f28-9190-bbfcf248c41b.png#averageHue=%2311100f&height=222&id=ttwgx&originHeight=222&originWidth=371&originalType=binary&ratio=1&rotation=0&showTitle=false&size=10496&status=done&style=shadow&title=&width=371)
查询学员名字中含有下划线的，执行以下SQL试试：
```sql
select * from student where name like '%_%';
```
![image.png](https://cdn.nlark.com/yuque/0/2022/png/21376908/1667523151909-c112a3cb-9968-4b4a-8bee-5a75c4b6a9f2.png#averageHue=%230f0e0e&clientId=ud0c47669-2d83-4&from=paste&height=232&id=u08a9aa32&originHeight=232&originWidth=664&originalType=binary&ratio=1&rotation=0&showTitle=false&size=12182&status=done&style=shadow&taskId=u2055ec95-4933-45ca-b17f-c384a54205d&title=&width=664)
显然这个查询结果不是我们想要的，以上SQL之所以将所有数据全部显示了，因为下划线代表任意单个字符，如果你想让这个下划线变成一个普通的下划线字符，就要使用转义字符了，在mysql当中转义字符是“\”，这个和java语言中的转义字符是一样的：
```sql
select * from student where name like '%\_%';
```
![image.png](https://cdn.nlark.com/yuque/0/2022/png/21376908/1667523291579-62dc328f-17ef-4e97-a22a-374ade19e797.png#averageHue=%23100f0e&clientId=ud0c47669-2d83-4&from=paste&height=139&id=u14f2fd6c&originHeight=139&originWidth=635&originalType=binary&ratio=1&rotation=0&showTitle=false&size=7682&status=done&style=shadow&taskId=u5f6488c4-25a2-4517-8936-801669b340e&title=&width=635)

![](https://cdn.nlark.com/yuque/0/2023/jpeg/21376908/1692002570088-3338946f-42b3-4174-8910-7e749c31e950.jpeg#averageHue=%23f9f8f8&from=url&id=tOgJQ&originHeight=78&originWidth=1400&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=shadow&title=)
# 排序操作

---

排序操作很常用，比如查询学员成绩，按照成绩降序排列。排序的SQL语法：
```sql
select .. from .. order by 字段 asc/desc
```
## 单一字段升序
查询员工的编号、姓名、薪资，按照薪资升序排列。
```sql
select empno,ename,sal from emp order by sal asc;
```
![image.png](https://cdn.nlark.com/yuque/0/2022/png/21376908/1667524015631-e1f1b6c3-0a5b-4f04-91d1-7a11df8fc7ff.png#averageHue=%2312100f&clientId=ud0c47669-2d83-4&from=paste&height=490&id=u337ff7e2&originHeight=490&originWidth=697&originalType=binary&ratio=1&rotation=0&showTitle=false&size=40038&status=done&style=shadow&taskId=uc89e7030-c586-4582-bdaa-6b231e3ab16&title=&width=697)

![](https://cdn.nlark.com/yuque/0/2023/jpeg/21376908/1692002570088-3338946f-42b3-4174-8910-7e749c31e950.jpeg#averageHue=%23f9f8f8&from=url&id=xJx1t&originHeight=78&originWidth=1400&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=shadow&title=)
## 单一字段降序
查询员工的编号、姓名、薪资，按照薪资降序排列。
```sql
select empno,ename,sal from emp order by sal desc;
```
![image.png](https://cdn.nlark.com/yuque/0/2022/png/21376908/1667524068322-84c1f716-5b7a-4b72-8a41-c0f8ec433d57.png#averageHue=%2311100f&clientId=ud0c47669-2d83-4&from=paste&height=490&id=ub06f2a23&originHeight=490&originWidth=737&originalType=binary&ratio=1&rotation=0&showTitle=false&size=40326&status=done&style=shadow&taskId=ube0d34dc-9629-4733-ac61-e9df253d566&title=&width=737)

![](https://cdn.nlark.com/yuque/0/2023/jpeg/21376908/1692002570088-3338946f-42b3-4174-8910-7e749c31e950.jpeg#averageHue=%23f9f8f8&from=url&id=cS1fD&originHeight=78&originWidth=1400&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=shadow&title=)
## 默认采用升序
查询员工的编号、姓名、薪资，按照薪资升序排列。
```sql
select empno,ename,sal from emp order by sal;
```
![image.png](https://cdn.nlark.com/yuque/0/2022/png/21376908/1667524117390-bd4560ff-accf-45ee-97f1-d098f86fd31f.png#averageHue=%2312100f&clientId=ud0c47669-2d83-4&from=paste&height=486&id=u288be0fb&originHeight=486&originWidth=664&originalType=binary&ratio=1&rotation=0&showTitle=false&size=39701&status=done&style=shadow&taskId=ucd8a5bf0-4f87-444a-a13b-dcbb808b75f&title=&width=664)
查询员工的编号、姓名，按照姓名升序排列。
```sql
select empno,ename from emp order by ename;
```
![image.png](https://cdn.nlark.com/yuque/0/2022/png/21376908/1667524169552-6abc923e-3638-4a65-ab97-741c22f885fa.png#averageHue=%23110f0e&clientId=ud0c47669-2d83-4&from=paste&height=488&id=ubf5dc2c5&originHeight=488&originWidth=626&originalType=binary&ratio=1&rotation=0&showTitle=false&size=32304&status=done&style=shadow&taskId=uf1ac3bd4-f65a-4d1a-ac9e-a6d5d5b7e8e&title=&width=626)

![](https://cdn.nlark.com/yuque/0/2023/jpeg/21376908/1692002570088-3338946f-42b3-4174-8910-7e749c31e950.jpeg#averageHue=%23f9f8f8&from=url&id=CqDmt&originHeight=78&originWidth=1400&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=shadow&title=)
## 多个字段排序
查询员工的编号、姓名、薪资，按照薪资升序排列，如果薪资相同的，再按照姓名升序排列。
```sql
select empno,ename,sal from emp order by sal asc, ename asc;
```
![image.png](https://cdn.nlark.com/yuque/0/2022/png/21376908/1667524337952-bbef44e7-488e-4c3e-9317-1fda80054c92.png#averageHue=%23110f0e&clientId=ud0c47669-2d83-4&from=paste&height=490&id=ud4173d66&originHeight=490&originWidth=813&originalType=binary&ratio=1&rotation=0&showTitle=false&size=40815&status=done&style=shadow&taskId=u231edd4c-d353-41e1-ba19-ebcc71d1d7b&title=&width=813)
## where和order by的位置
找出岗位是MANAGER的员工姓名和薪资，按照薪资升序排列。
```sql
select ename,sal from emp where job = 'MANAGER' order by sal asc;
```
![image.png](https://cdn.nlark.com/yuque/0/2022/png/21376908/1667524386864-8d24513b-85f9-4f31-9462-4fe094cb0843.png#averageHue=%230f0e0e&clientId=ud0c47669-2d83-4&from=paste&height=233&id=ub579bda3&originHeight=233&originWidth=887&originalType=binary&ratio=1&rotation=0&showTitle=false&size=16318&status=done&style=shadow&taskId=u0fd108a3-5c49-4ec2-843b-b8e4f5861c3&title=&width=887)
**通过这个例子主要是想告诉大家：where先执行，order by语句是最后执行的。**

![](https://cdn.nlark.com/yuque/0/2023/jpeg/21376908/1692002570088-3338946f-42b3-4174-8910-7e749c31e950.jpeg#averageHue=%23f9f8f8&from=url&id=qfi4f&originHeight=78&originWidth=1400&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=shadow&title=)
# distinct去重
查询工作岗位
```sql
select job from emp;
```
![image.png](https://cdn.nlark.com/yuque/0/2022/png/21376908/1668570471000-b0d2c628-c149-4b13-b44c-ae6f5edefcf6.png#averageHue=%23110f0e&clientId=u005f32df-cdfa-4&from=paste&height=570&id=u3464010b&originHeight=570&originWidth=461&originalType=binary&ratio=1&rotation=0&showTitle=false&size=27010&status=done&style=shadow&taskId=ud01ef31e-b7e3-444e-a422-927baef293a&title=&width=461)
可以看到工作岗位中有重复的记录，如何在显示的时候去除重复记录呢？在字段前添加distinct关键字。
```sql
select distinct job from emp;
```
![image.png](https://cdn.nlark.com/yuque/0/2022/png/21376908/1668570545279-ba8dcff3-533d-4ca8-9cc9-4b544ae47e8c.png#averageHue=%23100f0e&clientId=u005f32df-cdfa-4&from=paste&height=316&id=u847f8b1c&originHeight=316&originWidth=512&originalType=binary&ratio=1&rotation=0&showTitle=false&size=15359&status=done&style=shadow&taskId=uad426308-7527-406f-ac5a-83b5f426f2c&title=&width=512)
注意：这个去重只是将显示的结果去重，原表数据不会被更改。
接下来测试一下，在distinct关键字前添加其它字段是否可以？
```sql
select ename, distinct job from emp;
```
分析一下：ename是14条记录，distinct job是5条记录，可以同时显示吗？
![image.png](https://cdn.nlark.com/yuque/0/2022/png/21376908/1668570696423-05844698-00b1-4e9e-aa98-1a53f465cff4.png#averageHue=%23151311&clientId=u005f32df-cdfa-4&from=paste&height=104&id=uc30b7a53&originHeight=104&originWidth=945&originalType=binary&ratio=1&rotation=0&showTitle=false&size=15129&status=done&style=shadow&taskId=u877fbe24-2e82-46b5-85a4-fabccbe2c07&title=&width=945)
报错了，通过测试得知，distinct只能出现在所有字段的最前面。
**当distinct出现后，后面多个字段一定是联合去重的**，我们来做两个练习就知道了：
练习1：找出公司中所有的工作岗位。
![image.png](https://cdn.nlark.com/yuque/0/2022/png/21376908/1668570864793-732f34aa-5b7d-4389-b4af-51cbd964215f.png#averageHue=%23100f0e&clientId=u005f32df-cdfa-4&from=paste&height=316&id=ub89f2b22&originHeight=316&originWidth=540&originalType=binary&ratio=1&rotation=0&showTitle=false&size=15489&status=done&style=shadow&taskId=u5dab6bed-8c9b-4ae8-b617-37c86a9d8f2&title=&width=540)
![](https://cdn.nlark.com/yuque/0/2023/jpeg/21376908/1692002570088-3338946f-42b3-4174-8910-7e749c31e950.jpeg#averageHue=%23f9f8f8&from=url&id=n5ZcV&originHeight=78&originWidth=1400&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=shadow&title=)
练习2：找出公司中不同部门的不同工作岗位。
![image.png](https://cdn.nlark.com/yuque/0/2022/png/21376908/1668570891921-9c547b9b-d20e-4695-9704-051863b5e868.png#averageHue=%23110f0e&clientId=u005f32df-cdfa-4&from=paste&height=429&id=u755429fe&originHeight=429&originWidth=634&originalType=binary&ratio=1&rotation=0&showTitle=false&size=26800&status=done&style=shadow&taskId=ub3689df0-e1a9-40c1-a4e6-1f2f509c001&title=&width=634)

![](https://cdn.nlark.com/yuque/0/2023/jpeg/21376908/1692002570088-3338946f-42b3-4174-8910-7e749c31e950.jpeg#averageHue=%23f9f8f8&from=url&id=P2tc2&originHeight=78&originWidth=1400&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=shadow&title=)
# 数据处理函数

---

关于select语句，我们之前都是这样写：select 字段名 from 表名; 其实，这里的字段名可以看做“变量”，select后面既然可以跟变量，那么可以跟常量吗，尝试一下：
![image.png](https://cdn.nlark.com/yuque/0/2022/png/21376908/1668568118423-c5b5d189-4d32-41ab-a189-3f155d0d0efa.png#averageHue=%230e0d0d&clientId=u005f32df-cdfa-4&from=paste&height=502&id=uf4590195&originHeight=502&originWidth=866&originalType=binary&ratio=1&rotation=0&showTitle=false&size=24621&status=done&style=shadow&taskId=u9bf03714-2a03-4e7b-98d7-9996316a176&title=&width=866)
通过以上sql的测试得知，select后面既可以跟变量，又可以跟常量。
以上三条SQL中前两条中100和'abc'都是常量，最后一条SQL的abc没有添加单引号，它会被当做某个表的字段名，因为没有这个字段所以报错。 
![](https://cdn.nlark.com/yuque/0/2023/jpeg/21376908/1692002570088-3338946f-42b3-4174-8910-7e749c31e950.jpeg#averageHue=%23f9f8f8&from=url&id=KpG9f&originHeight=78&originWidth=1400&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=shadow&title=)
## 字符串相关
### 转大写upper和ucase
```sql
# 查询所有员工名字，以大写形式展现
select upper(ename) as ename from emp;
```
![image.png](https://cdn.nlark.com/yuque/0/2022/png/21376908/1668565912887-88d14d6c-707b-4e50-ac47-f8ad61b40d14.png#averageHue=%230e0e0d&clientId=u005f32df-cdfa-4&from=paste&height=531&id=ud706ac81&originHeight=531&originWidth=711&originalType=binary&ratio=1&rotation=0&showTitle=false&size=22988&status=done&style=shadow&taskId=ua5341942-dd96-4402-8f3e-05136a93880&title=&width=711)
还有一个和upper函数功能相同的函数ucase，也可以转大写，了解一下即可：
```sql
# 查询所有员工姓名，以大写形式展现
select ucase(ename) as ename from emp;
```
![image.png](https://cdn.nlark.com/yuque/0/2022/png/21376908/1668566229563-55802f88-f6d6-436a-b478-18832d7a0342.png#averageHue=%230f0e0d&clientId=u005f32df-cdfa-4&from=paste&height=534&id=uff6a6590&originHeight=534&originWidth=674&originalType=binary&ratio=1&rotation=0&showTitle=false&size=23082&status=done&style=shadow&taskId=uface697c-6972-498a-86af-50b161e48cd&title=&width=674)
```sql
# 查询员工smith的岗位、薪资（假如你不知道数据库表中的人名是大写、小写还是大小写混合）
select ename, job, sal from emp where upper(ename) = 'SMITH';
```
![image.png](https://cdn.nlark.com/yuque/0/2022/png/21376908/1668566360054-6e77882a-21fc-4b6e-9a04-3e0098606db8.png#averageHue=%23100f0e&clientId=u005f32df-cdfa-4&from=paste&height=178&id=uf8993c00&originHeight=178&originWidth=982&originalType=binary&ratio=1&rotation=0&showTitle=false&size=11947&status=done&style=shadow&taskId=u72025ccb-5725-4313-bf7b-3edebed799a&title=&width=982)
![](https://cdn.nlark.com/yuque/0/2023/jpeg/21376908/1692002570088-3338946f-42b3-4174-8910-7e749c31e950.jpeg#averageHue=%23f9f8f8&from=url&id=Myp3w&originHeight=78&originWidth=1400&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=shadow&title=)
### 转小写lower和lcase
**很简单，不再赘述，直接上代码：**
```sql
# 查询员工姓名，以小写形式展现
select lower(ename) as ename from emp;
select lcase(ename) as ename from emp;
```
![image.png](https://cdn.nlark.com/yuque/0/2022/png/21376908/1668566699289-0a479f71-ecf4-4a3f-ac4c-8516a4f0fee8.png#averageHue=%230f0e0d&clientId=u005f32df-cdfa-4&from=paste&height=216&id=u0f889bef&originHeight=216&originWidth=646&originalType=binary&ratio=1&rotation=0&showTitle=false&size=9493&status=done&style=shadow&taskId=u5f16833e-e425-424b-a769-1761dd7023f&title=&width=646)
![image.png](https://cdn.nlark.com/yuque/0/2022/png/21376908/1668566716526-c8fac5f9-7079-4738-a3d1-2a5c3c5e1145.png#averageHue=%230f0e0d&clientId=u005f32df-cdfa-4&from=paste&height=189&id=ue19b9b87&originHeight=189&originWidth=643&originalType=binary&ratio=1&rotation=0&showTitle=false&size=8007&status=done&style=shadow&taskId=u7fc1e3dd-17d7-4f33-b8ed-b88901fb087&title=&width=643)
### 截取字符串substr
语法：substr('被截取的字符串', 起始下标, 截取长度)
有两种写法：
第一种：substr('被截取的字符串', 起始下标, 截取长度)
第二种：substr('被截取的字符串', 起始下标)，当第三个参数“截取长度”缺失时，截取到字符串末尾
注意：起始下标从1开始，不是从0开始。（1表示从左侧开始的第一个位置，-1表示从右侧开始的第一个位置。）
![image.png](https://cdn.nlark.com/yuque/0/2022/png/21376908/1668567142258-6748508c-c3bb-440f-8ad7-c64df6c0028d.png#averageHue=%23100f0e&clientId=u005f32df-cdfa-4&from=paste&height=648&id=u521d5ef0&originHeight=648&originWidth=664&originalType=binary&ratio=1&rotation=0&showTitle=false&size=35242&status=done&style=shadow&taskId=u50bb124d-9e6b-4c8a-b48c-76594e0ec3c&title=&width=664)
![](https://cdn.nlark.com/yuque/0/2023/jpeg/21376908/1692002570088-3338946f-42b3-4174-8910-7e749c31e950.jpeg#averageHue=%23f9f8f8&from=url&id=xkp87&originHeight=78&originWidth=1400&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=shadow&title=)
练习：找出员工名字中第二个字母是A的
```sql
select ename from emp where substr(ename, 2, 1) = 'A';
```
![image.png](https://cdn.nlark.com/yuque/0/2022/png/21376908/1668567271612-710d3592-6111-4ab5-97c1-12f809ac7645.png#averageHue=%230f0e0d&clientId=u005f32df-cdfa-4&from=paste&height=254&id=u2313b4ee&originHeight=254&originWidth=854&originalType=binary&ratio=1&rotation=0&showTitle=false&size=14523&status=done&style=shadow&taskId=u8ae9b244-f6d3-441c-89d0-4466eaa73e4&title=&width=854)
### 获取字符串长度length
![image.png](https://cdn.nlark.com/yuque/0/2023/png/21376908/1672736218451-70fddda1-2541-4c91-9f39-3f968a6b6e12.png#averageHue=%23100f0f&clientId=uc0e8c595-6b95-4&from=paste&height=167&id=u69789788&originHeight=167&originWidth=525&originalType=binary&ratio=1&rotation=0&showTitle=false&size=7442&status=done&style=shadow&taskId=u39c20cea-67f3-49eb-9d8e-8c548360b72&title=&width=525)
注意：一个汉字是2个长度。
### 获取字符的个数char_length
![image.png](https://cdn.nlark.com/yuque/0/2023/png/21376908/1672736125194-177317bd-f65c-4c05-bda7-f58961b78fd7.png#averageHue=%2311100f&clientId=uc0e8c595-6b95-4&from=paste&height=168&id=uKcvT&originHeight=168&originWidth=582&originalType=binary&ratio=1&rotation=0&showTitle=false&size=8283&status=done&style=shadow&taskId=u2abebb18-4522-415a-bf80-859153252d1&title=&width=582)
### 字符串拼接
语法：concat('字符串1', '字符串2', '字符串3'....)
拼接的字符串数量没有限制。
![image.png](https://cdn.nlark.com/yuque/0/2022/png/21376908/1668569810019-a8c939c4-518d-4ed9-961a-27d4440d13d0.png#averageHue=%2311100f&clientId=u005f32df-cdfa-4&from=paste&height=437&id=u00e5d696&originHeight=437&originWidth=860&originalType=binary&ratio=1&rotation=0&showTitle=false&size=29849&status=done&style=shadow&taskId=ufbffbf88-a2ed-4341-a706-959748e2260&title=&width=860)
注意：在mysql8之前，双竖线||也是可以完成字符串拼接的。但在mysql8之后，||只作为逻辑运算符，不能再进行字符串拼接了。
```sql
select 'abc' || 'def' || 'xyz';
```
mysql8之后，|| 只作为“或者”运算符，例如：找出工资高于3000或者低于900的员工姓名和薪资：
```sql
select ename, sal from emp where sal > 3000 || sal < 900;
```
![image.png](https://cdn.nlark.com/yuque/0/2022/png/21376908/1669780282134-d3a16d8a-e0fc-4744-beff-83b3579f6161.png#averageHue=%230f0f0e&clientId=u6210fc1e-5e54-4&from=paste&height=196&id=uc7e77230&originHeight=196&originWidth=950&originalType=binary&ratio=1&rotation=0&showTitle=false&size=11249&status=done&style=shadow&taskId=u19693054-9222-4df2-899e-3ed69a01a71&title=&width=950)
mysql中可以使用+进行字符串的拼接吗？不可以，在mysql中+只作加法运算，在进行加法运算时，会将加号两边的数据尽最大的努力转换成数字再求和，如果无法转换成数字，最终运算结果通通是0
![](https://cdn.nlark.com/yuque/0/2023/jpeg/21376908/1692002570088-3338946f-42b3-4174-8910-7e749c31e950.jpeg#averageHue=%23f9f8f8&from=url&id=r5hjr&originHeight=78&originWidth=1400&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=shadow&title=)
### 去除字符串前后空白trim
```sql
select concat(trim('    abc    '), 'def');
```
![image.png](https://cdn.nlark.com/yuque/0/2022/png/21376908/1668570023583-bcf0b431-c34c-486b-9ee0-e571ff3c158d.png#averageHue=%2310100f&clientId=u005f32df-cdfa-4&from=paste&height=204&id=u800e8929&originHeight=204&originWidth=715&originalType=binary&ratio=1&rotation=0&showTitle=false&size=12536&status=done&style=shadow&taskId=uc6e946c5-bd11-4f08-83a5-34b7d5e1a78&title=&width=715)
默认是去除前后空白，也可以去除指定的前缀后缀，例如：
去除前置0
```sql
select trim(leading '0' from '000111000');
```
![image.png](https://cdn.nlark.com/yuque/0/2022/png/21376908/1668570194415-8f78ced1-8f36-42d3-a829-b81fc4132c85.png#averageHue=%23121110&clientId=u005f32df-cdfa-4&from=paste&height=214&id=u54da0ae5&originHeight=214&originWidth=706&originalType=binary&ratio=1&rotation=0&showTitle=false&size=12307&status=done&style=shadow&taskId=u4bd5c984-5076-4b41-936e-2cb2934e2a0&title=&width=706)
去除后置0
```sql
select trim(trailing '0' from '000111000');
```
![image.png](https://cdn.nlark.com/yuque/0/2022/png/21376908/1668570218215-c862c7d8-1ee3-4066-8e25-055767efee61.png#averageHue=%2312100f&clientId=u005f32df-cdfa-4&from=paste&height=207&id=ud1b70c2d&originHeight=207&originWidth=704&originalType=binary&ratio=1&rotation=0&showTitle=false&size=11888&status=done&style=shadow&taskId=u3680db7d-b909-4cfe-8636-aef9213b9cb&title=&width=704)
前置0和后置0全部去除
```sql
select trim(both '0' from '000111000');
```
![image.png](https://cdn.nlark.com/yuque/0/2022/png/21376908/1668570238062-dff388d3-3106-457d-a9ae-819f41821792.png#averageHue=%2311100f&clientId=u005f32df-cdfa-4&from=paste&height=203&id=uca889e8f&originHeight=203&originWidth=678&originalType=binary&ratio=1&rotation=0&showTitle=false&size=10559&status=done&style=shadow&taskId=u39829e4b-560a-42a1-b27c-315e566e9ae&title=&width=678)
![](https://cdn.nlark.com/yuque/0/2023/jpeg/21376908/1692002570088-3338946f-42b3-4174-8910-7e749c31e950.jpeg#averageHue=%23f9f8f8&from=url&id=EDgfQ&originHeight=78&originWidth=1400&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=shadow&title=)
## 数字相关
### rand()和rand(x)
rand()生成0到1的随机浮点数。
![image.png](https://cdn.nlark.com/yuque/0/2022/png/21376908/1669797997130-63b2c8d0-6169-4ee8-9b6b-c3087e9d733b.png#averageHue=%2311100f&clientId=u57006619-2538-4&from=paste&height=432&id=uc1af8ae1&originHeight=432&originWidth=488&originalType=binary&ratio=1&rotation=0&showTitle=false&size=21196&status=done&style=shadow&taskId=uf2b4c16d-fc16-42a5-91c6-c840e24096b&title=&width=488)
rand(x)生成0到1的随机浮点数，通过指定整数x来确定每次获取到相同的浮点值。
![image.png](https://cdn.nlark.com/yuque/0/2022/png/21376908/1669798044104-7fc0b727-ff91-4d3e-be33-9954d556afe2.png#averageHue=%23121110&clientId=u57006619-2538-4&from=paste&height=431&id=uddf41de3&originHeight=431&originWidth=404&originalType=binary&ratio=1&rotation=0&showTitle=false&size=23014&status=done&style=shadow&taskId=uc8b8c1f9-b44d-4886-8442-9c6d0e0beb7&title=&width=404)
![image.png](https://cdn.nlark.com/yuque/0/2022/png/21376908/1669798069147-75492782-759d-46d9-84c5-a83b3a63594c.png#averageHue=%23121110&clientId=u57006619-2538-4&from=paste&height=431&id=ud22d346e&originHeight=431&originWidth=417&originalType=binary&ratio=1&rotation=0&showTitle=false&size=21817&status=done&style=shadow&taskId=u01cf1b31-7d8b-4bc0-8eba-573138f7c49&title=&width=417)
### round(x)和round(x,y)四舍五入
round(x) 四舍五入，保留整数位，舍去所有小数
![image.png](https://cdn.nlark.com/yuque/0/2022/png/21376908/1669798450055-e26955bd-ea2d-445a-be98-721b54d3ca35.png#averageHue=%2311100f&clientId=u57006619-2538-4&from=paste&height=427&id=u633ac709&originHeight=427&originWidth=438&originalType=binary&ratio=1&rotation=0&showTitle=false&size=19800&status=done&style=shadow&taskId=u5ae99c90-04bd-47b9-9338-3be2146f355&title=&width=438)
round(x,y) 四舍五入，保留y位小数
![image.png](https://cdn.nlark.com/yuque/0/2022/png/21376908/1669798534269-9c494800-7878-4ccf-bacc-a8c4cdafbbe6.png#averageHue=%23100f0e&clientId=u57006619-2538-4&from=paste&height=656&id=ub44adc1f&originHeight=656&originWidth=467&originalType=binary&ratio=1&rotation=0&showTitle=false&size=30665&status=done&style=shadow&taskId=u06d2a339-d070-4c04-9d62-a6ca361ad3c&title=&width=467)
![](https://cdn.nlark.com/yuque/0/2023/jpeg/21376908/1692002570088-3338946f-42b3-4174-8910-7e749c31e950.jpeg#averageHue=%23f9f8f8&from=url&id=lpAuL&originHeight=78&originWidth=1400&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=shadow&title=)
### truncate(x, y)舍去
![image.png](https://cdn.nlark.com/yuque/0/2022/png/21376908/1669798594158-7e51e7a5-27af-4f7f-8021-a751f425a316.png#averageHue=%2311100f&clientId=u57006619-2538-4&from=paste&height=220&id=u7586a0cc&originHeight=220&originWidth=492&originalType=binary&ratio=1&rotation=0&showTitle=false&size=10521&status=done&style=shadow&taskId=u4aea8b0c-2612-4b7c-af22-e5b68687b80&title=&width=492)
以上SQL表示保留两位小数，剩下的全部舍去。
### ceil与floor
数字处理函数除了以上的之外，还有ceil和floor函数：

- ceil函数：返回大于或等于数值x的最小整数
- floor函数：返回小于或等于数值x的最大整数

![image.png](https://cdn.nlark.com/yuque/0/2023/png/21376908/1672735932932-f0dfc7de-1f77-4eb0-b6e9-b6c6c2ce7ae3.png#averageHue=%23100f0e&clientId=uc0e8c595-6b95-4&from=paste&height=433&id=ua803b791&originHeight=433&originWidth=402&originalType=binary&ratio=1&rotation=0&showTitle=false&size=13778&status=done&style=shadow&taskId=uf4127f6b-bfd8-454a-8aa8-2e1fec9edab&title=&width=402)
![](https://cdn.nlark.com/yuque/0/2023/jpeg/21376908/1692002570088-3338946f-42b3-4174-8910-7e749c31e950.jpeg#averageHue=%23f9f8f8&from=url&id=HydiS&originHeight=78&originWidth=1400&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=shadow&title=)
## 空处理
ifnull(x, y)，空处理函数，当x为NULL时，将x当做y处理。
ifnull(comm, 0)，表示如果员工的津贴是NULL时当做0处理。
在SQL语句中，凡是有NULL参与的数学运算，最终的计算结果都是NULL：
![image.png](https://cdn.nlark.com/yuque/0/2022/png/21376908/1669798864111-5cffd59f-d15c-4f6c-a2d8-0b623ec1f16c.png#averageHue=%23100f0e&clientId=u57006619-2538-4&from=paste&height=658&id=ue1cf6783&originHeight=658&originWidth=408&originalType=binary&ratio=1&rotation=0&showTitle=false&size=23225&status=done&style=shadow&taskId=ua42e9e3c-fa93-4f6c-979d-d5444c21108&title=&width=408)
看这样一个需求：查询每个员工的年薪。（年薪 = (月薪 + 津贴) * 12个月。注意：有的员工津贴comm是NULL。）
![image.png](https://cdn.nlark.com/yuque/0/2022/png/21376908/1669798945415-90bccaa6-1dda-4ebd-bc50-63ab5ba2b89a.png#averageHue=%23100f0e&clientId=u57006619-2538-4&from=paste&height=573&id=u514525d4&originHeight=573&originWidth=850&originalType=binary&ratio=1&rotation=0&showTitle=false&size=36066&status=done&style=shadow&taskId=ubb59ae71-c22d-456f-85bf-df0182998af&title=&width=850)
![](https://cdn.nlark.com/yuque/0/2023/jpeg/21376908/1692002570088-3338946f-42b3-4174-8910-7e749c31e950.jpeg#averageHue=%23f9f8f8&from=url&id=qqGmB&originHeight=78&originWidth=1400&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=shadow&title=)
以上查询结果中显示SMITH等人的年薪是NULL，这是为什么，这是因为SMITH等人的津贴comm是NULL，有NULL参与的数学运算，最终结果都是NULL，显然这个需要空处理，此时就用到了ifnull函数：
![image.png](https://cdn.nlark.com/yuque/0/2022/png/21376908/1669799067232-4896fa47-5c64-409a-b970-dddc31e06050.png#averageHue=%23100f0e&clientId=u57006619-2538-4&from=paste&height=573&id=u59b02703&originHeight=573&originWidth=982&originalType=binary&ratio=1&rotation=0&showTitle=false&size=42887&status=done&style=shadow&taskId=u063b2776-3482-4b4f-888c-3623426b77b&title=&width=982)
![](https://cdn.nlark.com/yuque/0/2023/jpeg/21376908/1692002570088-3338946f-42b3-4174-8910-7e749c31e950.jpeg#averageHue=%23f9f8f8&from=url&id=X7H0g&originHeight=78&originWidth=1400&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=shadow&title=)
## 日期和时间相关函数
### 获取当前日期和时间
![image.png](https://cdn.nlark.com/yuque/0/2023/png/21376908/1672707310711-3115e4af-385c-4565-89c7-25bad76e8a6a.png#averageHue=%23121110&clientId=uc0e8c595-6b95-4&from=paste&height=162&id=uc379723b&originHeight=162&originWidth=404&originalType=binary&ratio=1&rotation=0&showTitle=false&size=7211&status=done&style=shadow&taskId=uedf1c447-2a71-4f9a-9f96-98b9f249622&title=&width=404)
![image.png](https://cdn.nlark.com/yuque/0/2023/png/21376908/1672707382021-d8d296b7-9d9a-4072-b714-c99da604ac12.png#averageHue=%23151312&clientId=uc0e8c595-6b95-4&from=paste&height=163&id=ua9b22a07&originHeight=163&originWidth=377&originalType=binary&ratio=1&rotation=0&showTitle=false&size=8104&status=done&style=shadow&taskId=u0aa13932-ae31-46ba-94b7-f5cee861153&title=&width=377)
![image.png](https://cdn.nlark.com/yuque/0/2023/png/21376908/1672707469394-4fe3f0fb-ca9e-4484-b939-db716f6ddd38.png#averageHue=%23131211&clientId=uc0e8c595-6b95-4&from=paste&height=168&id=ue97dcb2c&originHeight=168&originWidth=801&originalType=binary&ratio=1&rotation=0&showTitle=false&size=12054&status=done&style=shadow&taskId=uf047d345-596d-4f3c-a996-3d1f6850219&title=&width=801)
now()和sysdate()的区别：

- now()：获取的是执行select语句的时刻。
- sysdate()：获取的是执行sysdate()函数的时刻。

![](https://cdn.nlark.com/yuque/0/2023/jpeg/21376908/1692002570088-3338946f-42b3-4174-8910-7e749c31e950.jpeg#averageHue=%23f9f8f8&from=url&id=l9noP&originHeight=78&originWidth=1400&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=shadow&title=)
### 获取当前日期
![image.png](https://cdn.nlark.com/yuque/0/2023/png/21376908/1672707770762-e9723219-562f-4a53-9d8a-9055ee80c25d.png#averageHue=%2311100f&clientId=uc0e8c595-6b95-4&from=paste&height=543&id=ufc58343c&originHeight=655&originWidth=440&originalType=binary&ratio=1&rotation=0&showTitle=false&size=29141&status=done&style=shadow&taskId=u707d5711-bda8-4f35-89c5-f39da3e879f&title=&width=365)
获取当前日期有三种写法，掌握任意一种即可：

- curdate()
- current_date()
- current_date
### 获取当前时间
![image.png](https://cdn.nlark.com/yuque/0/2023/png/21376908/1672707856778-8eec2322-c3c8-4ddc-94c4-3e08eea430a8.png#averageHue=%23121010&clientId=uc0e8c595-6b95-4&from=paste&height=653&id=u57a306e4&originHeight=653&originWidth=430&originalType=binary&ratio=1&rotation=0&showTitle=false&size=28651&status=done&style=shadow&taskId=ua03065f0-48bc-43c2-ae47-b77fab8249f&title=&width=430)
获取档期时间有三种写法，掌握其中一种即可：

- curtime()
- current_time()
- current_time

![](https://cdn.nlark.com/yuque/0/2023/jpeg/21376908/1692002570088-3338946f-42b3-4174-8910-7e749c31e950.jpeg#averageHue=%23f9f8f8&from=url&id=CDxHw&originHeight=78&originWidth=1400&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=shadow&title=)
### 获取单独的年、月、日、时、分、秒
![image.png](https://cdn.nlark.com/yuque/0/2023/png/21376908/1672708190559-a1d93032-699d-49dc-87cc-4ccb045bee28.png#averageHue=%23100f0e&clientId=uc0e8c595-6b95-4&from=paste&height=651&id=u5badb85c&originHeight=651&originWidth=456&originalType=binary&ratio=1&rotation=0&showTitle=false&size=28555&status=done&style=shadow&taskId=u742f8377-b4d8-44e9-950d-da020890e07&title=&width=456)
![image.png](https://cdn.nlark.com/yuque/0/2023/png/21376908/1672708242288-89a20209-4ca2-4d1c-a1b0-5ad5f1179841.png#averageHue=%2311100f&clientId=uc0e8c595-6b95-4&from=paste&height=653&id=u7cfcb11b&originHeight=653&originWidth=483&originalType=binary&ratio=1&rotation=0&showTitle=false&size=28868&status=done&style=shadow&taskId=u43769b4b-00e8-4dfb-a085-19858d725f1&title=&width=483)
注意：这些函数在使用的时候，需要传递一个日期参数给它，它可以获取到你给定的这个日期相关的年、月、日、时、分、秒的信息。
一次性提取一个给定日期的“年月日”部分，可以使用date()函数，例如：
![image.png](https://cdn.nlark.com/yuque/0/2023/png/21376908/1672713926559-d9c4257b-3536-4124-b4f4-3fd3626a293e.png#averageHue=%2311100f&clientId=uc0e8c595-6b95-4&from=paste&height=168&id=u161f961c&originHeight=168&originWidth=438&originalType=binary&ratio=1&rotation=0&showTitle=false&size=7552&status=done&style=shadow&taskId=ub9643e54-a1b4-424f-a2d7-e15c7538b83&title=&width=438)
一次性提取一个给定日期的“时分秒”部分，可以使用time()函数，例如：
![image.png](https://cdn.nlark.com/yuque/0/2023/png/21376908/1672721340191-9c568184-73b5-4c26-9035-95245016ba4f.png#averageHue=%2311100f&clientId=uc0e8c595-6b95-4&from=paste&height=161&id=u0bb5bc88&originHeight=161&originWidth=428&originalType=binary&ratio=1&rotation=0&showTitle=false&size=7598&status=done&style=shadow&taskId=u09037fc7-e074-481b-bf6a-ccc8fc49cf6&title=&width=428)
![](https://cdn.nlark.com/yuque/0/2023/jpeg/21376908/1692002570088-3338946f-42b3-4174-8910-7e749c31e950.jpeg#averageHue=%23f9f8f8&from=url&id=JhMuY&originHeight=78&originWidth=1400&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=shadow&title=)
### date_add函数
date_add函数的作用：给指定的日期添加间隔的时间，从而得到一个新的日期。
date_add函数的语法格式：date_add(日期, interval expr 单位)，例如：
![image.png](https://cdn.nlark.com/yuque/0/2023/png/21376908/1672709352877-e64de4c0-d776-4e30-908b-4a96c04bc186.png#averageHue=%23121110&clientId=uc0e8c595-6b95-4&from=paste&height=174&id=ub79687f8&originHeight=174&originWidth=771&originalType=binary&ratio=1&rotation=0&showTitle=false&size=11929&status=done&style=shadow&taskId=u79db77b4-bf0f-41ee-91ba-e6e48424d32&title=&width=771)
以'2023-01-03'为基准，间隔3天之后的日期：'2023-01-06'
![image.png](https://cdn.nlark.com/yuque/0/2023/png/21376908/1672709436259-c6d671c6-ccc8-4109-9612-1f178801ef64.png#averageHue=%23121110&clientId=uc0e8c595-6b95-4&from=paste&height=171&id=ub0dc1d88&originHeight=171&originWidth=778&originalType=binary&ratio=1&rotation=0&showTitle=false&size=11798&status=done&style=shadow&taskId=u06a7162d-aafa-4469-8f12-d3ea81c1f63&title=&width=778)
![](https://cdn.nlark.com/yuque/0/2023/jpeg/21376908/1692002570088-3338946f-42b3-4174-8910-7e749c31e950.jpeg#averageHue=%23f9f8f8&from=url&id=flAzu&originHeight=78&originWidth=1400&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=shadow&title=)
以'2023-01-03'为基准，间隔3个月之后的日期：'2023-04-03'
详细解释一下这个函数的相关参数：

- 日期：一个日期类型的数据
- interval：关键字，翻译为“间隔”，固定写法
- expr：指定具体的间隔量，一般是一个数字。**也可以为负数，如果为负数，效果和date_sub函数相同**。
- 单位：
   - year：年
   - month：月
   - day：日
   - hour：时
   - minute：分
   - second：秒
   - microsecond：微秒（1秒等于1000毫秒，1毫秒等于1000微秒）
   - week：周
   - quarter：季度

请分析下面这条SQL语句所表达的含义：
![image.png](https://cdn.nlark.com/yuque/0/2023/png/21376908/1672710673500-8afb96ad-3aa5-4adb-9160-9aaac4b4ff83.png#averageHue=%23131211&clientId=uc0e8c595-6b95-4&from=paste&height=162&id=u455ecd04&originHeight=162&originWidth=1036&originalType=binary&ratio=1&rotation=0&showTitle=false&size=12957&status=done&style=shadow&taskId=u3148a05b-3fbe-432e-8492-373fde1d2db&title=&width=1036)
以上SQL表示：以2022-10-01 10:10:10为基准，在这个时间基础上添加-1微秒，也就是减去1微秒。
以上SQL也可以采用date_sub函数完成，例如：
![image.png](https://cdn.nlark.com/yuque/0/2023/png/21376908/1672710799157-9775a5b0-143f-493b-a6f0-cd8db5c6ca31.png#averageHue=%23131211&clientId=uc0e8c595-6b95-4&from=paste&height=159&id=u70af0451&originHeight=159&originWidth=990&originalType=binary&ratio=1&rotation=0&showTitle=false&size=13185&status=done&style=shadow&taskId=u7bf2be69-c836-4951-bd99-69c09f553ec&title=&width=990)
另外，单位也可以采用复合型单位，例如：

- SECOND_MICROSECOND
- MINUTE_MICROSECOND
- MINUTE_SECOND：几分几秒之后
- HOUR_MICROSECOND
- HOUR_SECOND
- HOUR_MINUTE：几小时几分之后
- DAY_MICROSECOND
- DAY_SECOND
- DAY_MINUTE
- DAY_HOUR：几天几小时之后
- YEAR_MONTH：几年几个月之后

如果单位采用复合型的话，expr该怎么写呢？例如单位采用：day_hour，假设我要表示3天2小时之后，怎么写？
![image.png](https://cdn.nlark.com/yuque/0/2023/png/21376908/1672711325140-0a281589-4bc2-4fc8-bd7f-9a5ff180ba71.png#averageHue=%23121110&clientId=uc0e8c595-6b95-4&from=paste&height=171&id=u186c11d0&originHeight=171&originWidth=1009&originalType=binary&ratio=1&rotation=0&showTitle=false&size=13317&status=done&style=shadow&taskId=u2827b5bf-37d2-486f-9db8-fa8b15ce510&title=&width=1009)
'3,2'这个应该很好理解，表示3天2个小时之后。'3,2'和day_hour是对应的。

![](https://cdn.nlark.com/yuque/0/2023/jpeg/21376908/1692002570088-3338946f-42b3-4174-8910-7e749c31e950.jpeg#averageHue=%23f9f8f8&from=url&id=BfJl7&originHeight=78&originWidth=1400&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=shadow&title=)
### date_format日期格式化函数
将日期转换成具有某种格式的日期字符串，通常用在查询操作当中。（date类型转换成char类型）
语法格式：date_format(日期, '日期格式')
该函数有两个参数：

- 第一个参数：日期。这个参数就是即将要被格式化的日期。类型是date类型。
- 第二个参数：指定要格式化的格式字符串。
   - %Y：四位年份
   - %y：两位年份
   - %m：月份（1..12）
   - %d：日（1..30）
   - %H：小时（0..23）
   - %i：分（0..59）
   - %s：秒（0..59）

例如：获取当前系统时间，让其以这个格式展示：2000-10-11 20:15:30
![image.png](https://cdn.nlark.com/yuque/0/2023/png/21376908/1672716928881-badddb77-c670-43f3-8b25-8e2eb4952a04.png#averageHue=%23121110&clientId=uc0e8c595-6b95-4&from=paste&height=168&id=uf1769116&originHeight=168&originWidth=790&originalType=binary&ratio=1&rotation=0&showTitle=false&size=12687&status=done&style=shadow&taskId=u0936983e-6c2d-4e0f-96a9-905426534b9&title=&width=790)
注意：在mysql当中，默认的日期格式就是：%Y-%m-%d %H:%i:%s，所以当你直接输出日期数据的时候，会自动转换成该格式的字符串：
![image.png](https://cdn.nlark.com/yuque/0/2023/png/21376908/1672717081322-e99bdff0-76df-4fcc-958a-463bf9e65d9d.png#averageHue=%23131110&clientId=uc0e8c595-6b95-4&from=paste&height=164&id=udf0a9e15&originHeight=164&originWidth=369&originalType=binary&ratio=1&rotation=0&showTitle=false&size=7005&status=done&style=shadow&taskId=ua8a7ba31-3b81-427d-8a55-a8a84114389&title=&width=369)
![](https://cdn.nlark.com/yuque/0/2023/jpeg/21376908/1692002570088-3338946f-42b3-4174-8910-7e749c31e950.jpeg#averageHue=%23f9f8f8&from=url&id=AePyP&originHeight=78&originWidth=1400&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=shadow&title=)
### str_to_date函数
该函数的作用是将char类型的日期字符串转换成日期类型date，通常使用在插入和修改操作当中。（char类型转换成date类型）
假设有一个学生表t_student，学生有一个生日的字段，类型是date类型：
```sql
drop table if exists t_student;
create table t_student(
  name varchar(255),
  birth date
);
desc t_student;
```
我们要给这个表插入一条数据：姓名zhangsan，生日85年10月1日，执行以下insert语句：
![image.png](https://cdn.nlark.com/yuque/0/2023/png/21376908/1672718111465-698c085a-b3f1-4523-9f3f-d27ceb4410d5.png#averageHue=%231b1815&clientId=uc0e8c595-6b95-4&from=paste&height=59&id=u816b6342&originHeight=59&originWidth=1163&originalType=binary&ratio=1&rotation=0&showTitle=false&size=13327&status=done&style=shadow&taskId=u25e9289a-7274-49fc-9db5-e54cc764c7d&title=&width=1163)
错误原因：日期值不正确。意思是：birth字段需要一个日期，你给的这个字符串'10/01/1985'我识别不了。这种情况下，我们就可以使用str_to_date函数进行类型转换：
![image.png](https://cdn.nlark.com/yuque/0/2023/png/21376908/1672718492868-58ab55ff-a4e7-481f-9c58-9c81014d1762.png#averageHue=%2315100f&clientId=uc0e8c595-6b95-4&from=paste&height=83&id=u3cdb0924&originHeight=83&originWidth=1379&originalType=binary&ratio=1&rotation=0&showTitle=false&size=12797&status=done&style=shadow&taskId=u619f99b1-3107-44e6-8738-542c8b9aaf8&title=&width=1379)
![image.png](https://cdn.nlark.com/yuque/0/2023/png/21376908/1672718610506-ec24a44e-7854-4037-8567-b42dfb9228c0.png#averageHue=%23121110&clientId=uc0e8c595-6b95-4&from=paste&height=159&id=uf93570e5&originHeight=159&originWidth=533&originalType=binary&ratio=1&rotation=0&showTitle=false&size=8550&status=done&style=shadow&taskId=ua5be6705-7bc3-46b4-9922-15d9020df6e&title=&width=533)
当然，如果你提供的日期字符串格式能够被mysql解析，str_to_date函数是可以省略的，底层会自动调用该函数进行类型转换：
![image.png](https://cdn.nlark.com/yuque/0/2023/png/21376908/1672718807175-8b62c13a-e771-482d-a999-7548501da25e.png#averageHue=%23110f0e&clientId=uc0e8c595-6b95-4&from=paste&height=625&id=u14b85262&originHeight=625&originWidth=1088&originalType=binary&ratio=1&rotation=0&showTitle=false&size=66015&status=done&style=shadow&taskId=uae019b86-851f-4348-962a-a15199adc0f&title=&width=1088)
如果日期格式符合以上的几种格式，mysql都会自动进行类型转换的。
![](https://cdn.nlark.com/yuque/0/2023/jpeg/21376908/1692002570088-3338946f-42b3-4174-8910-7e749c31e950.jpeg#averageHue=%23f9f8f8&from=url&id=qPxdF&originHeight=78&originWidth=1400&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=shadow&title=)
### dayofweek、dayofmonth、dayofyear函数
![image.png](https://cdn.nlark.com/yuque/0/2023/png/21376908/1672719401783-7ea51704-954a-4f96-aa81-3a8da4b34582.png#averageHue=%23110f0e&clientId=uc0e8c595-6b95-4&from=paste&height=665&id=u1a4c7890&originHeight=665&originWidth=685&originalType=binary&ratio=1&rotation=0&showTitle=false&size=39505&status=done&style=shadow&taskId=u36f1ca0f-c525-47e4-8ccf-df5d8210281&title=&width=685)
dayofweek：一周中的第几天（1~7），周日是1，周六是7。
dayofmonth：一个月中的第几天（1~31）
dayofyear：一年中的第几天（1~366）
![](https://cdn.nlark.com/yuque/0/2023/jpeg/21376908/1692002570088-3338946f-42b3-4174-8910-7e749c31e950.jpeg#averageHue=%23f9f8f8&from=url&id=aDRcH&originHeight=78&originWidth=1400&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=shadow&title=)
### last_day函数
获取给定日期所在月的最后一天的日期：
![image.png](https://cdn.nlark.com/yuque/0/2023/png/21376908/1672719572099-bba462b8-da22-42b7-9a40-9c2c545596ef.png#averageHue=%23121010&clientId=uc0e8c595-6b95-4&from=paste&height=163&id=u8cab6ec4&originHeight=163&originWidth=498&originalType=binary&ratio=1&rotation=0&showTitle=false&size=8323&status=done&style=shadow&taskId=ucef40e03-23be-4936-a671-ac674c20438&title=&width=498)
### datediff函数
计算两个日期之间所差天数：
![image.png](https://cdn.nlark.com/yuque/0/2023/png/21376908/1672720897012-c5e7e6dd-29de-46b0-b2c1-e1de3e8d6e54.png#averageHue=%23121110&clientId=uc0e8c595-6b95-4&from=paste&height=169&id=u9b900968&originHeight=169&originWidth=865&originalType=binary&ratio=1&rotation=0&showTitle=false&size=10814&status=done&style=shadow&taskId=ufb6d4060-84b9-44b3-8694-a9cf990bc54&title=&width=865)
时分秒不算，只计算日期部分相差的天数。
![](https://cdn.nlark.com/yuque/0/2023/jpeg/21376908/1692002570088-3338946f-42b3-4174-8910-7e749c31e950.jpeg#averageHue=%23f9f8f8&from=url&id=H86Gm&originHeight=78&originWidth=1400&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=shadow&title=)
### timediff函数
计算两个日期所差时间，例如日期1和日期2所差10:20:30，表示差10小时20分钟30秒。
![image.png](https://cdn.nlark.com/yuque/0/2023/png/21376908/1672721193551-f65b470a-9060-4010-b172-b34eb1787e55.png#averageHue=%23121110&clientId=uc0e8c595-6b95-4&from=paste&height=168&id=u56a06c8e&originHeight=168&originWidth=987&originalType=binary&ratio=1&rotation=0&showTitle=false&size=11553&status=done&style=shadow&taskId=ua81b206f-eb6b-47b3-ad2a-e4b048fdd31&title=&width=987)

![](https://cdn.nlark.com/yuque/0/2023/jpeg/21376908/1692002570088-3338946f-42b3-4174-8910-7e749c31e950.jpeg#averageHue=%23f9f8f8&from=url&id=URBHc&originHeight=78&originWidth=1400&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=shadow&title=)
## if函数
如果条件为TRUE则返回“YES”，如果条件为FALSE则返回“NO”：
```sql
SELECT IF(500<1000, "YES", "NO");
```
例如：如果工资高于3000，则输出1，反之则输出0
![image.png](https://cdn.nlark.com/yuque/0/2023/png/21376908/1672725980625-f929cbdc-41ec-49d4-a5de-bc753dfbe67e.png#averageHue=%230f0e0e&clientId=uc0e8c595-6b95-4&from=paste&height=536&id=ued7bfdee&originHeight=536&originWidth=747&originalType=binary&ratio=1&rotation=0&showTitle=false&size=29371&status=done&style=shadow&taskId=uec5813f3-7f94-4ae2-9644-78e1fd281f6&title=&width=747)
再例如：如果名字是SMITH的，工资上调10%，其他员工工资正常显示。
![image.png](https://cdn.nlark.com/yuque/0/2023/png/21376908/1672726073468-51733168-6ebe-477d-9aba-267adcefd10a.png#averageHue=%23100f0e&clientId=uc0e8c595-6b95-4&from=paste&height=534&id=uf2148f3a&originHeight=534&originWidth=992&originalType=binary&ratio=1&rotation=0&showTitle=false&size=38069&status=done&style=shadow&taskId=u7679358d-9412-4000-b8cd-872e9980209&title=&width=992)
再例如：工作岗位是MANAGER的工资上调10%，是SALESMAN的工资上调20%，其他岗位工资正常。
![image.png](https://cdn.nlark.com/yuque/0/2023/png/21376908/1672726371265-19128e1a-47cf-46b0-9b80-310d37010535.png#averageHue=%23100f0e&clientId=uc0e8c595-6b95-4&from=paste&height=532&id=u575eb753&originHeight=532&originWidth=1441&originalType=binary&ratio=1&rotation=0&showTitle=false&size=55630&status=done&style=shadow&taskId=uf0e71940-399c-4edf-bd67-14f893e719e&title=&width=1441)
**上面这个需求也可以使用：case.. when.. then.. when.. then.. else.. end来完成：**
![image.png](https://cdn.nlark.com/yuque/0/2023/png/21376908/1672726864928-8206091b-3bd3-4f12-b784-173aff775d6f.png#averageHue=%23141210&clientId=uc0e8c595-6b95-4&from=paste&height=724&id=u37fc5544&originHeight=724&originWidth=561&originalType=binary&ratio=1&rotation=0&showTitle=false&size=57934&status=done&style=shadow&taskId=u812c7487-a5f1-4d90-a5bd-891e360d45b&title=&width=561)
![](https://cdn.nlark.com/yuque/0/2023/jpeg/21376908/1692002570088-3338946f-42b3-4174-8910-7e749c31e950.jpeg#averageHue=%23f9f8f8&from=url&id=sWtRV&originHeight=78&originWidth=1400&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=shadow&title=)
## cast函数
cast函数用于将值从一种数据类型转换为表达式中指定的另一种数据类型
语法：cast(值 as 数据类型)
例如：cast('2020-10-11' as date)，表示将字符串'2020-10-11'转换成日期date类型。
在使用cast函数时，可用的数据类型包括：

- date：日期类型
- time：时间类型
- datetime：日期时间类型
- signed：有符号的int类型（有符号指的是正数负数）
- char：定长字符串类型
- decimal：浮点型

![image.png](https://cdn.nlark.com/yuque/0/2023/png/21376908/1672737293605-d7e38772-e9c3-40ab-a7ea-3311aa14a1a9.png#averageHue=%2311100f&clientId=uc0e8c595-6b95-4&from=paste&height=662&id=u174ddf1e&originHeight=662&originWidth=778&originalType=binary&ratio=1&rotation=0&showTitle=false&size=34283&status=done&style=shadow&taskId=u2531ed29-bfef-4efc-a5b0-6ff107330b6&title=&width=778)
![image.png](https://cdn.nlark.com/yuque/0/2023/png/21376908/1672737634602-96cdd564-1220-445e-9b18-b3f0a2a55379.png#averageHue=%2311100f&clientId=uc0e8c595-6b95-4&from=paste&height=435&id=ued100771&originHeight=435&originWidth=545&originalType=binary&ratio=1&rotation=0&showTitle=false&size=18617&status=done&style=shadow&taskId=u559bfe74-f2ec-4e05-a37f-2cd08b29cde&title=&width=545)
![image.png](https://cdn.nlark.com/yuque/0/2023/png/21376908/1672737720321-3812fd42-d3a4-4985-96d2-629947d9ce48.png#averageHue=%23111010&clientId=uc0e8c595-6b95-4&from=paste&height=213&id=ua7df14ff&originHeight=213&originWidth=604&originalType=binary&ratio=1&rotation=0&showTitle=false&size=10420&status=done&style=shadow&taskId=u66dc0647-a030-400f-8ec0-b3c2b22a844&title=&width=604)
![image.png](https://cdn.nlark.com/yuque/0/2023/png/21376908/1672737802812-d04d581c-138c-4e4e-97d4-c979558e9b2e.png#averageHue=%2311100f&clientId=uc0e8c595-6b95-4&from=paste&height=170&id=u214f15ff&originHeight=170&originWidth=714&originalType=binary&ratio=1&rotation=0&showTitle=false&size=8572&status=done&style=shadow&taskId=ud2929b4c-8582-4dc3-a2ba-8de75b96e58&title=&width=714)
![](https://cdn.nlark.com/yuque/0/2023/jpeg/21376908/1692002570088-3338946f-42b3-4174-8910-7e749c31e950.jpeg#averageHue=%23f9f8f8&from=url&id=zcFrS&originHeight=78&originWidth=1400&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=shadow&title=)
## 加密函数
md5函数，可以将给定的字符串经过md5算法进行加密处理，字符串经过加密之后会生成一个固定长度32位的字符串，md5加密之后的密文通常是不能解密的：
![image.png](https://cdn.nlark.com/yuque/0/2023/png/21376908/1672737046172-5ee0458a-60c6-4bae-b075-94b7dee440ab.png#averageHue=%23131110&clientId=uc0e8c595-6b95-4&from=paste&height=220&id=u6e900f32&originHeight=220&originWidth=568&originalType=binary&ratio=1&rotation=0&showTitle=false&size=10865&status=done&style=shadow&taskId=uabd2a6f3-e59b-4dac-ba4c-bcc743fafad&title=&width=568)

![](https://cdn.nlark.com/yuque/0/2023/jpeg/21376908/1692002570088-3338946f-42b3-4174-8910-7e749c31e950.jpeg#averageHue=%23f9f8f8&from=url&id=ilOoD&originHeight=78&originWidth=1400&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=shadow&title=)
# 分组函数
**分组函数的执行原则：先分组，然后对每一组数据执行分组函数。如果没有分组语句group by的话，整张表的数据自成一组。**
分组函数包括五个：

- max：最大值
- min：最小值
- avg：平均值
- sum：求和
- count：计数

![](https://cdn.nlark.com/yuque/0/2023/jpeg/21376908/1692002570088-3338946f-42b3-4174-8910-7e749c31e950.jpeg#averageHue=%23f9f8f8&from=url&id=AjG5x&originHeight=78&originWidth=1400&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=shadow&title=)
## max
**找出员工的最高薪资**
```sql
select max(sal) from emp;
```
## min
**找出员工的最低工资**
```sql
select min(sal) from emp;
```
## avg
**计算员工的平均薪资**
```sql
select avg(sal) from emp;
```
## sum
**计算员工的工资和**
```sql
select sum(sal) from emp;
```
**计算员工的津贴之和**
```sql
select sum(comm) from emp;
```
重点：所有的分组函数都是自动忽略NULL的。
![](https://cdn.nlark.com/yuque/0/2023/jpeg/21376908/1692002570088-3338946f-42b3-4174-8910-7e749c31e950.jpeg#averageHue=%23f9f8f8&from=url&id=QJCgr&originHeight=78&originWidth=1400&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=shadow&title=)
## count
**统计员工人数**
```sql
select count(ename) from emp;
select count(*) from emp;
select count(1) from emp;
```
count(*)和count(1)的效果一样，统计该组中总记录行数。
count(ename)统计的是这个ename字段中不为NULL个数总和。
例如：count(comm) 结果是 4，而不是14
```sql
select count(comm) from emp;
```
**统计岗位数量**
```sql
select count(distinct job) from emp;
```
## 分组函数组合使用
select count(*),max(sal),min(sal),avg(sal),sum(sal) from emp;
## 分组函数注意事项
**分组函数不能直接使用在where子句当中**
select ename,job from emp where sal > avg(sal); 这个会报错的
原因：分组的行为是在where执行之后才开始的。

![](https://cdn.nlark.com/yuque/0/2023/jpeg/21376908/1692002570088-3338946f-42b3-4174-8910-7e749c31e950.jpeg#averageHue=%23f9f8f8&from=url&id=guJg0&originHeight=78&originWidth=1400&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=shadow&title=)
# 分组查询
## group by
按照某个字段分组，或者按照某些字段联合分组。注意：group by的执行是在where之后执行。
语法：
group by 字段
group by 字段1,字段2,字段3....
**找出每个岗位的平均薪资**
```sql
select job, avg(sal) from emp group by job;
```
**找出每个部门最高工资**
```sql
select deptno,max(sal) from emp group by deptno;
```
**找出每个部门不同岗位的平均薪资**
```sql
select deptno,job,avg(sal) from emp group by deptno,job;
```


**当select语句中有group by的话，select后面只能跟分组函数或参加分组的字段**
```sql
select ename,deptno,avg(sal) from emp group by deptno; // 这个SQL执行后会报错。
```
![image.png](https://cdn.nlark.com/yuque/0/2023/png/21376908/1676866192155-44d23157-87d0-4a58-a9d5-2641619d74fe.png#averageHue=%23171412&clientId=u417b9e29-4007-4&from=paste&height=140&id=uae74e6b8&originHeight=140&originWidth=1141&originalType=binary&ratio=1&rotation=0&showTitle=false&size=25591&status=done&style=shadow&taskId=u4097c74b-3d21-485a-a74f-1390352d2e3&title=&width=1141)
## having
having写在group by的后面，当你对分组之后的数据不满意，可以继续通过having对分组之后的数据进行过滤。
where的过滤是在分组前进行过滤。
使用原则：尽量在where中过滤，实在不行，再使用having。越早过滤效率越高。

**找出除20部分之外，其它部门的平均薪资。**
```sql
select deptno,avg(sal) from emp where deptno<>20 group by deptno; // 建议
select deptno,avg(sal) from emp group by deptno having deptno <> 20; // 不建议
```


**查询每个部门平均薪资，找出平均薪资高于2000的。**
```sql
select deptno,avg(sal) from emp group by deptno having avg(sal) > 2000;
```
## 组内排序
案例：找出每个工作岗位的工资排名在前两名的。
substring_index函数的使用：
![image.png](https://cdn.nlark.com/yuque/0/2023/png/21376908/1678080182698-009c47d2-eb75-4f67-afaa-874c7904ed45.png#averageHue=%2312100f&clientId=ue32f086e-fc2b-4&from=paste&height=379&id=rhnfq&originHeight=379&originWidth=755&originalType=binary&ratio=1&rotation=0&showTitle=false&size=27939&status=done&style=shadow&taskId=u49228cac-a6a0-4d31-8dbc-abc432cd804&title=&width=755)
group_concat函数的使用：
![image.png](https://cdn.nlark.com/yuque/0/2023/png/21376908/1678082111760-02413f4e-a8b0-4837-8cb0-3b201151293f.png#averageHue=%23100f0e&clientId=ue32f086e-fc2b-4&from=paste&height=272&id=bhhYI&originHeight=272&originWidth=904&originalType=binary&ratio=1&rotation=0&showTitle=false&size=20533&status=done&style=shadow&taskId=uac8b6d07-c85c-47d4-9724-b29c1e8f927&title=&width=904)
学习了这两个函数之后，自己可以尝试写出来吗？
![](https://cdn.nlark.com/yuque/0/2023/jpeg/21376908/1692002570088-3338946f-42b3-4174-8910-7e749c31e950.jpeg#averageHue=%23f9f8f8&from=url&id=UeABU&originHeight=78&originWidth=1400&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=shadow&title=)
# 总结单表的DQL语句
select ...5
from ...1
where ...2
group by ...3
having ...4
order by ...6
重点掌握一个完整的DQL语句执行顺序。

![](https://cdn.nlark.com/yuque/0/2023/jpeg/21376908/1692002570088-3338946f-42b3-4174-8910-7e749c31e950.jpeg#averageHue=%23f9f8f8&from=url&id=aOHbB&originHeight=78&originWidth=1400&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=shadow&title=)
# 连接查询
## 什么是连接查询

1. 从一张表中查询数据称为单表查询。
2. 从两张或更多张表中联合查询数据称为多表查询，又叫做连接查询。
3. 什么时候需要使用连接查询？
   1. 比如这样的需求：员工表中有员工姓名，部门表中有部门名字，要求查询每个员工所在的部门名字，这个时候就需要连接查询。
## 连接查询的分类

1. 根据语法出现的年代进行分类：
   1. SQL92（这种语法很少用，可以不用学。）
   2. SQL99（我们主要学习这种语法。）
2. 根据连接方式的不同进行分类：
   1. 内连接
      1. 等值连接
      2. 非等值连接
      3. 自连接
   2. 外连接
      1. 左外连接（左连接）
      2. 右外连接（右连接）
   3. 全连接

![](https://cdn.nlark.com/yuque/0/2023/jpeg/21376908/1692002570088-3338946f-42b3-4174-8910-7e749c31e950.jpeg#averageHue=%23f9f8f8&from=url&id=RfJym&originHeight=78&originWidth=1400&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=shadow&title=)
## 笛卡尔积现象

1. 当两张表进行连接查询时，如果没有任何条件进行过滤，最终的查询结果条数是两张表条数的乘积。为了避免笛卡尔积现象的发生，需要添加条件进行筛选过滤。
2. 需要注意：添加条件之后，虽然避免了笛卡尔积现象，但是匹配的次数没有减少。
3. 为了SQL语句的可读性，为了执行效率，建议给表起别名。
## 内连接
### 什么叫内连接
![内连接.png](https://cdn.nlark.com/yuque/0/2023/png/21376908/1677398804476-afbffad7-7d5a-4318-9e86-a3f8092dfcc8.png#averageHue=%23f7f5f5&clientId=u1be67ea7-0240-4&from=paste&height=233&id=u4f6abf7d&originHeight=233&originWidth=300&originalType=binary&ratio=1&rotation=0&showTitle=false&size=29826&status=done&style=shadow&taskId=u51112874-93e5-4ef2-8366-f78cc265d04&title=&width=300)
满足条件的记录才会出现在结果集中。
### 内连接之等值连接
连接时，条件为等量关系。
案例：查询每个员工所在的部门名称，要求显示员工名、部门名。
```sql
select
	e.ename,d.dname
from
	emp e
inner join
	dept d
on
	e.deptno = d.deptno;
```
注意：inner可以省略。
![image.png](https://cdn.nlark.com/yuque/0/2023/png/21376908/1677401675659-04e46e96-9f00-4210-8beb-e8148807ae10.png#averageHue=%231a1613&clientId=u1be67ea7-0240-4&from=paste&height=380&id=u91e060d7&originHeight=380&originWidth=258&originalType=binary&ratio=1&rotation=0&showTitle=false&size=15942&status=done&style=shadow&taskId=u2319a8db-57a3-4bcb-a42b-b58c46e0381&title=&width=258)
![](https://cdn.nlark.com/yuque/0/2023/jpeg/21376908/1692002570088-3338946f-42b3-4174-8910-7e749c31e950.jpeg#averageHue=%23f9f8f8&from=url&id=clVoK&originHeight=78&originWidth=1400&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=shadow&title=)
### 内连接之非等值连接
连接时，条件是非等量关系。
案例：查询每个员工的工资等级，要求显示员工名、工资、工资等级。
```sql
select
	e.ename,e.sal,s.grade
from
	emp e
join
	salgrade s
on
	e.sal between s.losal and s.hisal;
```
![image.png](https://cdn.nlark.com/yuque/0/2023/png/21376908/1677401628377-11f115a0-b961-4e10-b411-97ea04a89035.png#averageHue=%23191613&clientId=u1be67ea7-0240-4&from=paste&height=380&id=u9ef14890&originHeight=380&originWidth=279&originalType=binary&ratio=1&rotation=0&showTitle=false&size=17957&status=done&style=shadow&taskId=u97872f0c-74c1-40ef-b3bb-607697cbe62&title=&width=279)
![](https://cdn.nlark.com/yuque/0/2023/jpeg/21376908/1692002570088-3338946f-42b3-4174-8910-7e749c31e950.jpeg#averageHue=%23f9f8f8&from=url&id=ianfB&originHeight=78&originWidth=1400&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=shadow&title=)
### 内连接之自连接
连接时，一张表看做两张表，自己和自己进行连接。
案例：找出每个员工的直属领导，要求显示员工名、领导名。
```sql
select
	e.ename 员工名, l.ename 领导名
from
	emp e
join
	emp l
on
	e.mgr = l.empno;
```
![image.png](https://cdn.nlark.com/yuque/0/2023/png/21376908/1677402107820-a3fc38cc-4e13-4a39-8bb4-f1d9de713cd9.png#averageHue=%23161311&clientId=u1be67ea7-0240-4&from=paste&height=363&id=ub784a9c1&originHeight=363&originWidth=256&originalType=binary&ratio=1&rotation=0&showTitle=false&size=15854&status=done&style=shadow&taskId=u67543946-a969-42f9-a55b-91571731d16&title=&width=256)
思路：
将emp表当做员工表 e
![image.png](https://cdn.nlark.com/yuque/0/2023/png/21376908/1677401951879-b0967e07-82f4-41e3-861e-d61e7d679e71.png#averageHue=%23141210&clientId=u1be67ea7-0240-4&from=paste&height=409&id=u4a5d8630&originHeight=409&originWidth=409&originalType=binary&ratio=1&rotation=0&showTitle=false&size=28580&status=done&style=shadow&taskId=ua9050736-6b86-415c-9f4d-e4e8d72c0b5&title=&width=409)
将emp表当做领导表 l
![image.png](https://cdn.nlark.com/yuque/0/2023/png/21376908/1677401973338-4bc03ba9-815d-4fca-90fb-de34e5848da3.png#averageHue=%2312100f&clientId=u1be67ea7-0240-4&from=paste&height=409&id=uffcf8f58&originHeight=409&originWidth=374&originalType=binary&ratio=1&rotation=0&showTitle=false&size=19851&status=done&style=shadow&taskId=uad8210e5-8156-449c-bc2f-25f2614109b&title=&width=374)
可以发现连接条件是：e.mgr = l.empno（员工的领导编号=领导的员工编号）
注意：KING这个员工没有查询出来。如果想将KING也查询出来，需要使用外连接。

![](https://cdn.nlark.com/yuque/0/2023/jpeg/21376908/1692002570088-3338946f-42b3-4174-8910-7e749c31e950.jpeg#averageHue=%23f9f8f8&from=url&id=Kz0kN&originHeight=78&originWidth=1400&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=shadow&title=)
## 外连接
### 什么叫外连接
内连接是满足条件的记录查询出来。也就是两张表的交集。
外连接是除了满足条件的记录查询出来，再将其中一张表的记录全部查询出来，另一张表如果没有与之匹配的记录，自动模拟出NULL与其匹配。
左外连接：
![左连接.png](https://cdn.nlark.com/yuque/0/2023/png/21376908/1677398828684-41b0bde2-1689-47a4-ae7b-3c5c4fb82ce6.png#averageHue=%23f5e6e4&clientId=u1be67ea7-0240-4&from=paste&height=233&id=ue0f4c04f&originHeight=233&originWidth=300&originalType=binary&ratio=1&rotation=0&showTitle=false&size=42064&status=done&style=shadow&taskId=u3697d149-d9f5-4090-8773-ffb0962ff90&title=&width=300)
右外连接：
![右连接.png](https://cdn.nlark.com/yuque/0/2023/png/21376908/1677398837026-688ff40f-d74b-4da6-a2e4-9573f5ba1580.png#averageHue=%23f4e6e3&clientId=u1be67ea7-0240-4&from=paste&height=233&id=ua18b1d44&originHeight=233&originWidth=300&originalType=binary&ratio=1&rotation=0&showTitle=false&size=43272&status=done&style=shadow&taskId=u4bb1c6ab-4c51-4fe0-938b-a7950969180&title=&width=300)
![](https://cdn.nlark.com/yuque/0/2023/jpeg/21376908/1692002570088-3338946f-42b3-4174-8910-7e749c31e950.jpeg#averageHue=%23f9f8f8&from=url&id=XFps5&originHeight=78&originWidth=1400&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=shadow&title=)
### 外连接之左外连接（左连接）
案例：查询所有部门信息，并且找出每个部门下的员工。
```sql
select
  d.*,e.ename
from
  dept d
left outer join
  emp e
on
  d.deptno = e.deptno;
```
![image.png](https://cdn.nlark.com/yuque/0/2023/png/21376908/1677402955987-bdcd956a-8dd4-481b-97de-c785b200e902.png#averageHue=%23171411&clientId=u1be67ea7-0240-4&from=paste&height=408&id=ud8f95a62&originHeight=408&originWidth=470&originalType=binary&ratio=1&rotation=0&showTitle=false&size=36154&status=done&style=shadow&taskId=u3263d663-860e-41a9-b973-50a3be9baa0&title=&width=470)
注意：outer可以省略。
任何一个左连接都可以写作右连接。
![](https://cdn.nlark.com/yuque/0/2023/jpeg/21376908/1692002570088-3338946f-42b3-4174-8910-7e749c31e950.jpeg#averageHue=%23f9f8f8&from=url&id=PUaJ7&originHeight=78&originWidth=1400&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=shadow&title=)
### 外连接之右外连接（右连接）
还是上面的案例，可以写作右连接。
```sql
select
  d.*,e.ename
from
  emp e
right outer join
  dept d
on
  d.deptno = e.deptno;
```
![image.png](https://cdn.nlark.com/yuque/0/2023/png/21376908/1677403445932-325502d5-b568-46a5-8f7a-d91030f3cac3.png#averageHue=%23191411&clientId=u1be67ea7-0240-4&from=paste&height=412&id=ue32d3266&originHeight=412&originWidth=454&originalType=binary&ratio=1&rotation=0&showTitle=false&size=36142&status=done&style=shadow&taskId=u28ef1b62-f835-472a-b916-1ee2eb5299b&title=&width=454)
案例：找出所有员工的上级领导，要求显示员工名和领导名。
```sql
select 
  e.ename 员工名,l.ename 领导名 
from 
  emp e 
left join 
  emp l 
on
  e.mgr = l.empno;
```
```sql
select 
  e.ename 员工名,l.ename 领导名 
from 
  emp l 
right join 
  emp e 
on
  e.mgr = l.empno;
```
![image.png](https://cdn.nlark.com/yuque/0/2023/png/21376908/1677403569294-c9688076-61e2-4e33-bb40-06d4307c6b43.png#averageHue=%23171210&clientId=u1be67ea7-0240-4&from=paste&height=386&id=ud80e0755&originHeight=386&originWidth=273&originalType=binary&ratio=1&rotation=0&showTitle=false&size=16908&status=done&style=shadow&taskId=uded0f105-8d51-486b-97fb-acb24822774&title=&width=273)
![](https://cdn.nlark.com/yuque/0/2023/jpeg/21376908/1692002570088-3338946f-42b3-4174-8910-7e749c31e950.jpeg#averageHue=%23f9f8f8&from=url&id=t1JJ5&originHeight=78&originWidth=1400&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=shadow&title=)

## 全连接
什么是全连接？
MySQL不支持full join。oracle数据库支持。
![全连接.png](https://cdn.nlark.com/yuque/0/2023/png/21376908/1677398846702-4a3f3e0f-16bb-4e00-8015-490dc44d114b.png#averageHue=%23f2d7d2&clientId=u1be67ea7-0240-4&from=paste&height=233&id=u050103a2&originHeight=233&originWidth=300&originalType=binary&ratio=1&rotation=0&showTitle=false&size=51399&status=done&style=shadow&taskId=ued746d97-47c2-46a3-83cd-097182ea146&title=&width=300)
两张表数据全部查询出来，没有匹配的记录，各自为对方模拟出NULL进行匹配。
客户表：t_customer
![image.png](https://cdn.nlark.com/yuque/0/2023/png/21376908/1677405118434-d9979d32-5647-4b0a-8d65-1ff6b61c6d44.png#averageHue=%23131210&clientId=u1be67ea7-0240-4&from=paste&height=137&id=u66bb1e76&originHeight=137&originWidth=235&originalType=binary&ratio=1&rotation=0&showTitle=false&size=4218&status=done&style=shadow&taskId=u7d338668-6c7a-488f-851d-635afa97d29&title=&width=235)
订单表：t_order
![image.png](https://cdn.nlark.com/yuque/0/2023/png/21376908/1677405287024-4df811ac-9216-47c3-98b2-20f5d7ce2886.png#averageHue=%23151311&clientId=u1be67ea7-0240-4&from=paste&height=136&id=u8ef1b39a&originHeight=136&originWidth=261&originalType=binary&ratio=1&rotation=0&showTitle=false&size=4032&status=done&style=shadow&taskId=u69ae2de5-204a-4a0b-8d2f-67ccbc73ad2&title=&width=261)
案例：查询所有的客户和订单。
```sql
select 
 c.*,o.* 
from 
 t_customer c 
full join 
 t_order o 
on 
 c.cid = o.cid;
```
![](https://cdn.nlark.com/yuque/0/2023/jpeg/21376908/1692002570088-3338946f-42b3-4174-8910-7e749c31e950.jpeg#averageHue=%23f9f8f8&from=url&id=URWP1&originHeight=78&originWidth=1400&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=shadow&title=)
## 多张表连接
三张表甚至更多张表如何进行表连接
案例：找出每个员工的部门，并且要求显示每个员工的薪资等级。
```sql
select 
 e.ename,d.dname,s.grade 
from 
 emp e 
join 
 dept d 
on 
 e.deptno = d.deptno 
join 
 salgrade s 
on 
 e.sal between s.losal and s.hisal;
```
![image.png](https://cdn.nlark.com/yuque/0/2023/png/21376908/1677404511432-b8fe8eb2-c828-4913-8d7c-a7b47a0ee270.png#averageHue=%23171411&clientId=u1be67ea7-0240-4&from=paste&height=381&id=u6047af30&originHeight=381&originWidth=324&originalType=binary&ratio=1&rotation=0&showTitle=false&size=18547&status=done&style=shadow&taskId=uc90c12f6-bdbb-4221-abe5-dcc4e221c96&title=&width=324)

![](https://cdn.nlark.com/yuque/0/2023/jpeg/21376908/1692002570088-3338946f-42b3-4174-8910-7e749c31e950.jpeg#averageHue=%23f9f8f8&from=url&id=oPaaH&originHeight=78&originWidth=1400&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=shadow&title=)
# 子查询
## 什么是子查询

1. select语句中嵌套select语句就叫做子查询。
2. select语句可以嵌套在哪里？
   1. where后面、from后面、select后面都是可以的。

```sql
select ..(select)..
from ..(select)..
where ..(select)..
```



## where后面使用子查询
案例：找出高于平均薪资的员工姓名和薪资。
错误的示范：
```sql
select ename,sal from emp where sal > avg(sal);
```
错误原因：where后面不能直接使用分组函数。
可以使用子查询：
```sql
select ename,sal from emp where sal > (select avg(sal) from emp);
```
![](https://cdn.nlark.com/yuque/0/2023/jpeg/21376908/1692002570088-3338946f-42b3-4174-8910-7e749c31e950.jpeg#averageHue=%23f9f8f8&from=url&id=L4mS0&originHeight=78&originWidth=1400&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=shadow&title=)
## from后面使用子查询
小窍门：from后面的子查询可以看做一张临时表。
案例：找出每个部门的平均工资的等级。
第一步：先找出每个部门平均工资。
```sql
select deptno, avg(sal) avgsal from emp group by deptno;
```
![image.png](https://cdn.nlark.com/yuque/0/2023/png/21376908/1677477788393-e2525a0a-2092-4a5e-80e7-7f8df04f6a6c.png#averageHue=%23151311&clientId=ud7d035d7-9c64-4&from=paste&height=163&id=u397cf064&originHeight=163&originWidth=303&originalType=binary&ratio=1&rotation=0&showTitle=false&size=5620&status=done&style=shadow&taskId=uc8a5cf34-abe3-446f-9948-e3cedf385f9&title=&width=303)
第二步：将以上查询结果当做临时表t，t表和salgrade表进行连接查询。条件：t.avgsal between s.losal and s.hisal
```sql
select t.*,s.grade from (select deptno, avg(sal) avgsal from emp group by deptno) t join salgrade s on t.avgsal between s.losal and s.hisal;
```
![image.png](https://cdn.nlark.com/yuque/0/2023/png/21376908/1677477892811-ef9b366b-82be-4407-86f1-8dfa81492d8c.png#averageHue=%23151311&clientId=ud7d035d7-9c64-4&from=paste&height=162&id=u5d9f4ab4&originHeight=162&originWidth=397&originalType=binary&ratio=1&rotation=0&showTitle=false&size=7422&status=done&style=shadow&taskId=uc90565b7-edc2-43bf-ba54-1e7db925c63&title=&width=397)
![](https://cdn.nlark.com/yuque/0/2023/jpeg/21376908/1692002570088-3338946f-42b3-4174-8910-7e749c31e950.jpeg?x-oss-process=image%2Fresize%2Cw_1177%2Climit_0%2Finterlace%2C1#averageHue=%23f9f8f8&from=url&id=Nae5T&originHeight=66&originWidth=1177&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=shadow&title=)
## select后面使用子查询
```sql
select e.ename,(select d.dname from dept d where e.deptno = d.deptno) as dname from emp e;
```
![image.png](https://cdn.nlark.com/yuque/0/2023/png/21376908/1678063689524-a204a93a-6454-4ff7-a1c6-ac5229edae91.png#averageHue=%231a1714&clientId=ud9fded62-54bb-4&from=paste&height=428&id=u2b69cf05&originHeight=428&originWidth=276&originalType=binary&ratio=1&rotation=0&showTitle=false&size=16342&status=done&style=shadow&taskId=ua4f4e977-d3e6-4e90-8781-42050638d4a&title=&width=276)
## exists、not exists
在 MySQL 数据库中，EXISTS（存在）用于检查子查询的查询结果行数是否大于0。如果子查询的查询结果行数大于0，则 EXISTS 条件为真。（即存在查询结果则是true。）

主要应用场景：

- EXISTS 可以与 SELECT、UPDATE、DELETE 一起使用，用于检查另一个查询是否返回任何行；
- EXISTS 可以用于验证条件子句中的表达式是否存在；
- EXISTS 常用于子查询条件过滤，例如查询有订单的用户等。

```sql
drop table if exists t_customer;
drop table if exists t_order;

create table t_customer(
  customer_id int,
  customer_name varchar(32)
);

create table t_order(
  order_id int,
  order_price decimal(5,1),
  customer_id int
);

insert into t_customer(customer_id,customer_name) values(1,'zhangsan');
insert into t_customer(customer_id,customer_name) values(2,'lisi');
insert into t_customer(customer_id,customer_name) values(3,'wangwu');

insert into t_order(order_id, order_price, customer_id) values(10, 1000.0, 1);
insert into t_order(order_id, order_price, customer_id) values(20, 2000.0, 1);
insert into t_order(order_id, order_price, customer_id) values(30, 3000.0, 2);
insert into t_order(order_id, order_price, customer_id) values(40, 4000.0, 2);

commit;
select * from t_customer;
select * from t_order;
```
现在我们来看一个简单的案例，假设我们要查询先前有过订单的顾客，而订单信息保存在 t_order 表中，顾客信息保存在 t_customer 表中。我们可以使用以下 sql 语句：

```sql
select * from t_customer c where exists(select * from t_order o where o.customer_id=c.customer_id);
```

在这个查询语句中，子查询用于检查是否有订单与每个客户相关联。如果子查询返回至少一行，则表示该顾客已经下过订单，并返回此客户的所有信息，否则该顾客将不被包含在结果中。

以下是这个查询语句的执行过程：

1.  首先查询表 t_customer 中的所有顾客信息（以下简称为顾客表）； 
2.  对于顾客表中的每一行，都执行一次子查询，子查询查询该顾客有没有订单，如果有，则在结果集中保留该顾客信息；如果没有，则将该顾客排除； 
3.  最终返回有订单顾客的所有信息。 

除了 EXISTS，也可以使用 NOT EXISTS 条件从 SELECT、UPDATE、DELETE 语句中获取子查询的返回结果。NOT EXISTS 用于检查一个子查询是否返回任何行，如果没有行返回，那么 NOT EXISTS 将返回 true。

例如，我们想要查找所有没有下过订单的顾客，可以使用以下 sql 语句：

```sql
select * from t_customer c where not exists(select * from t_order o where o.customer_id=c.customer_id);
```

在这个查询语句中，如果没有任何与顾客相关联的订单，则 NOT EXISTS 子查询将返回一个空结果集，这时候 WHERE 条件为 true，并将返回所有顾客信息。如果顾客有订单，则 NOT EXISTS 子查询的结果集将不为空，WHERE 条件为 false，则不会返回该顾客的信息。

总之，无论是 EXISTS 还是 NOT EXISTS，都是非常有用的 SQL 工具。可以通过它们来结合子查询来动态过滤查询结果，使 SQL 查询变得更加灵活和高效。
![](https://cdn.nlark.com/yuque/0/2023/jpeg/21376908/1692002570088-3338946f-42b3-4174-8910-7e749c31e950.jpeg#averageHue=%23f9f8f8&from=url&id=XvFk9&originHeight=78&originWidth=1400&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=shadow&title=)
## in和exists区别
IN 和 EXISTS 都是用于关系型数据库查询的操作符。不同之处在于：

1.  IN 操作符是根据指定列表中的值来判断是否满足条件，而 EXISTS 操作符则是根据子查询的结果是否有返回记录集来判断。 
2.  EXISTS 操作符通常比 IN 操作符更快，尤其是在子查询返回记录数很大的情况下。因为 EXISTS 只需要判断是否存在符合条件的记录，而 IN 操作符需要比对整个列表，因此执行效率相对较低。 
3.  IN 操作符可同时匹配多个值，而 EXISTS 只能匹配一组条件。 

下面是一个简单的示例，用于演示 IN 和 EXISTS 之间的区别。假设我们有两个表 orders 和 products，orders 表中记录了订单信息，products 表中记录了商品信息。现在我们想查询所有“手机”和“平板电脑”这两种商品中，至少有一笔订单销售了 $1000 以上的商品：

使用 IN 操作符：

```sql
SELECT *
FROM products
WHERE product_name IN ('手机', '平板电脑')
AND product_id IN (
  SELECT product_id
  FROM orders
  WHERE order_amount > 1000
);
```

使用 EXISTS 操作符：

```sql
SELECT *
FROM products
WHERE product_name IN ('手机', '平板电脑')
AND EXISTS (
  SELECT *
  FROM orders
  WHERE orders.product_id = products.product_id
  AND order_amount > 1000
);
```

总之，IN 和 EXISTS 都是用于条件过滤的操作符，但其实现方式和性能特点都不同，需要根据具体情况进行选择和使用。
# union&union all
不管是union还是union all都可以将两个查询结果集进行合并。
union会对合并之后的查询结果集进行去重操作。
union all是直接将查询结果集合并，不进行去重操作。（union all和union都可以完成的话，优先选择union all，union all因为不需要去重，所以效率高一些。）
![image.png](https://cdn.nlark.com/yuque/0/2023/png/21376908/1678078225300-461e069f-0c80-4745-88a7-2969acccd076.png#averageHue=%23141210&clientId=ue32f086e-fc2b-4&from=paste&height=488&id=u46d82364&originHeight=488&originWidth=404&originalType=binary&ratio=1&rotation=0&showTitle=false&size=31584&status=done&style=shadow&taskId=u459bc800-2e1c-4247-866e-b06b0313a0c&title=&width=404)
![image.png](https://cdn.nlark.com/yuque/0/2023/png/21376908/1678078278429-e97f96a1-7429-4b68-8df9-3bda3a890797.png#averageHue=%23151210&clientId=ue32f086e-fc2b-4&from=paste&height=884&id=u2ef6109a&originHeight=884&originWidth=408&originalType=binary&ratio=1&rotation=0&showTitle=false&size=60134&status=done&style=shadow&taskId=u8c39e0b0-c274-46f0-8866-347160e1418&title=&width=408)
案例：查询工作岗位是MANAGER和SALESMAN的员工。
```sql
select ename,sal from emp where job='MANAGER'
union all
select ename,sal from emp where job='SALESMAN';
```
以上案例采用or也可以完成，那or和union all有什么区别？考虑走索引优化之类的选择union all，其它选择or。
两个结果集合并时，列数量要相同：
![image.png](https://cdn.nlark.com/yuque/0/2023/png/21376908/1678078078467-89b7ba88-52ae-4e70-b5cc-b4fe4a3daf76.png#averageHue=%2312110f&clientId=ue32f086e-fc2b-4&from=paste&height=101&id=u85e05b84&originHeight=101&originWidth=999&originalType=binary&ratio=1&rotation=0&showTitle=false&size=11813&status=done&style=shadow&taskId=u29bd097d-8994-4842-be9e-3bcb8865687&title=&width=999)
![](https://cdn.nlark.com/yuque/0/2023/jpeg/21376908/1692002570088-3338946f-42b3-4174-8910-7e749c31e950.jpeg?x-oss-process=image%2Fresize%2Cw_1177%2Climit_0%2Finterlace%2C1#averageHue=%23f9f8f8&from=url&id=IRARo&originHeight=66&originWidth=1177&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=shadow&title=)
# limit

1. limit作用：查询第几条到第几条的记录。通常是因为表中数据量太大，需要分页显示。
2. limit语法格式：
   1. limit 开始下标, 长度
3. 案例：查询员工表前5条记录
```sql
select ename,sal from emp limit 0, 5;
```
如果下标是从0开始，可以简写为：
```sql
select ename,sal from emp limit 5;
```

4. 查询工资排名在前5名的员工（limit是在order by执行之后才会执行的）
```sql
select ename,sal from emp order by sal desc limit 5;
```

5. 通用的分页sql

假设每页显示3条记录：pageSize = 3
第1页：limit 0, 3
第2页：limit 3, 3
第3页：limit 6, 3
第pageNo页：limit (pageNo - 1)*pageSize, pageSize
![](https://cdn.nlark.com/yuque/0/2023/jpeg/21376908/1692002570088-3338946f-42b3-4174-8910-7e749c31e950.jpeg?x-oss-process=image%2Fresize%2Cw_1177%2Climit_0%2Finterlace%2C1#averageHue=%23f9f8f8&from=url&id=bmktU&originHeight=66&originWidth=1177&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=shadow&title=)
# 35个DQL练手题
## 第1题

1. 取得每个部门最高薪水的人员名称

   第一步：取得每个部门最高薪水
```sql
select deptno,max(sal) as maxsal from emp group by deptno;
```

第二步：将上面第一步的查询结果当做一张临时表t，进行表连接，条件是：t.deptno=e.deptno and t.maxsal=e.sal

```sql
select e.ename,t.* from emp e join (select deptno,max(sal) as maxsal from emp group by deptno) t on e.deptno = t.deptno and e.sal = t.maxsal;
```
## 第2题

2. 哪些人的薪水在部门的平均薪水之上
   
   第一步：取得每个部门的平均薪水
```sql
select deptno,avg(sal) as avgsal from emp group by deptno;
```

第二步：将上面的查询结果当做临时表t，让t和emp e表进行表连接，条件是：t.deptno=e.deptno and e.sal>t.avgsal

```sql
select e.ename,e.sal,t.* from emp e join (select deptno,avg(sal) as avgsal from emp group by deptno) t on t.deptno=e.deptno and e.sal>t.avgsal;
```
## 第3题

3. 取得每个部门平均薪水的等级
   
   第一步：取得每个部门的平均薪水
```sql
select deptno,avg(sal) as avgsal from emp group by deptno;
```

第二步：将上面的查询结果当做临时表t，然后t和salgrade s表进行连接，条件是：t.avgsal between s.losal and s.hisal

```sql
select t.*,s.grade from (select deptno,avg(sal) as avgsal from emp group by deptno) t join salgrade s on t.avgsal between s.losal and s.hisal;
```
![](https://cdn.nlark.com/yuque/0/2023/jpeg/21376908/1692002570088-3338946f-42b3-4174-8910-7e749c31e950.jpeg#averageHue=%23f9f8f8&from=url&id=p5mdX&originHeight=78&originWidth=1400&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=shadow&title=)
## 第4题

4. 取得部门中（所有人的）平均的薪水等级
   
   第一步：找出每个人的薪水等级
```sql
select e.ename,e.sal,s.grade from emp e join salgrade s on e.sal between s.losal and s.hisal;
```

第二步：在上面的查询结果当中继续按照部门编号进行分组，求平均值。（不需要将上面的查询结果当做临时表，继续基于它进行分组即可。）

```sql
select 
   e.deptno,avg(s.grade) 
from 
  emp e 
join 
  salgrade s 
on 
  e.sal between s.losal and s.hisal 
group by 
  e.deptno;
```
## 第5题

5. 不准用组函数（Max），取得最高薪水（给出两种解决方案）
   
   第一种方案：按照薪资降序排列，取第一个。
```sql
select sal from emp order by sal desc limit 1;
```

第二种方案：采用表的自连接方式。

```sql
select ename,sal from emp where sal not in(select distinct a.sal from emp a join emp b on a.sal < b.sal);
```
![](https://cdn.nlark.com/yuque/0/2023/jpeg/21376908/1692002570088-3338946f-42b3-4174-8910-7e749c31e950.jpeg#averageHue=%23f9f8f8&from=url&id=r2oDz&originHeight=78&originWidth=1400&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=shadow&title=)
## 第6题

6. 取得平均薪水最高的部门的部门编号（至少给出两种解决方案）
   
   第一种方案：降序排列取第一个
```sql
select deptno,avg(sal) as avgsal from emp group by deptno order by avgsal desc limit 1;
```

第二种方案：max函数

```sql
select deptno,avg(sal) as avgsal from emp group by deptno having avg(sal)=(select max(t.avgsal) from (select avg(sal) as avgsal from emp group by deptno) t);
```
## 第7题

7. 取得平均薪水最高的部门的部门名称
   
   比上面的题目多一个表连接，和dept表连接，按照部门名称进行分组。
```sql
select d.dname,avg(e.sal) as avgsal from emp e join dept d on e.deptno=d.deptno group by d.dname order by avgsal desc limit 1;
```
## 第8题

8. 求平均薪水的等级最低的部门的部门名称
   
   第一步：求每个部门的平均薪水
```sql
select d.dname,avg(e.sal) as avgsal from emp e join dept d on e.deptno = d.deptno group by d.dname;
```

第二步：求每个部门的平均薪水等级（将以上的执行结果当做临时表t，t和salgrade s表进行连接，条件：t.avgsal between .s.losal and s.hisal）

```sql
select t.*,s.grade from (select d.dname,avg(e.sal) as avgsal from emp e join dept d on e.deptno = d.deptno group by d.dname) t join salgrade s on t.avgsal between s.losal and s.hisal;
```

第三步：找到最低的部门名称（以上结果继续按照grade进行升序，然后limit 1）

```sql
select t.*,s.grade from (select d.dname,avg(e.sal) as avgsal from emp e join dept d on e.deptno = d.deptno group by d.dname) t join salgrade s on t.avgsal between s.losal and s.hisal order by s.grade asc limit 1;
```
![](https://cdn.nlark.com/yuque/0/2023/jpeg/21376908/1692002570088-3338946f-42b3-4174-8910-7e749c31e950.jpeg#averageHue=%23f9f8f8&from=url&id=gxih5&originHeight=78&originWidth=1400&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=shadow&title=)
## 第9题

9. 取得比普通员工(员工代码没有在mgr字段上出现的)的最高薪水还要高的领导人姓名
   
   第一步：找出所有的普通员工的最高薪水
```sql
select max(sal) from emp where empno not in(select mgr from emp where mgr is not null);
```

第二步：大于以上最高薪水的一定是要找的领导人。

```sql
select ename,sal from emp where sal > (select max(sal) from emp where empno not in(select mgr from emp where mgr is not null));
```
## 第10题

10. 取得薪水最高的前五名员工
```sql
select ename,sal from emp order by sal desc limit 5;
```
## 第11题

11. 取得薪水最高的第六到第十名员工
```sql
select ename,sal from emp order by sal desc limit 5, 5;
```
## 第12题

12. 取得最后入职的5名员工
```sql
select ename,sal,hiredate from emp order by hiredate desc limit 5;
```
![](https://cdn.nlark.com/yuque/0/2023/jpeg/21376908/1692002570088-3338946f-42b3-4174-8910-7e749c31e950.jpeg#averageHue=%23f9f8f8&from=url&id=rqjpz&originHeight=78&originWidth=1400&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=shadow&title=)
## 第13题

13. 取得每个薪水等级有多少员工

    第一步：找出每个员工的薪水等级
```sql
select e.ename,s.grade from emp e join salgrade s on e.sal between s.losal and s.hisal;
```

第二步：基于以上的记录继续根据等级分组，count即可。

```sql
select s.grade,count(*) from emp e join salgrade s on e.sal between s.losal and s.hisal group by s.grade;
```
## 第14题

14. 列出所有员工及领导的姓名
```sql
select e.ename 员工名, l.ename 领导名 from emp e left join emp l on e.mgr = l.empno;
```
## 第15题

15. 列出受雇日期早于其直接上级的所有员工的编号,姓名,部门名称
```sql
select e.ename 员工名,e.hiredate, l.ename 领导名,l.hiredate,d.dname from emp e join emp l on e.mgr = l.empno join dept d on e.deptno = d.deptno where e.hiredate < l.hiredate;
```
![](https://cdn.nlark.com/yuque/0/2023/jpeg/21376908/1692002570088-3338946f-42b3-4174-8910-7e749c31e950.jpeg#averageHue=%23f9f8f8&from=url&id=tVRuo&originHeight=78&originWidth=1400&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=shadow&title=)
## 第16题

16. 列出部门名称和这些部门的员工信息,同时列出那些没有员工的部门
```sql
select d.dname,e.ename,e.sal from dept d left join emp e on d.deptno = e.deptno;
```
## 第17题

17. 列出至少有5个员工的所有部门
```sql
select deptno, count(*) from emp group by deptno having count(*) >= 5;
```
## 第18题

18. 列出薪金比"SMITH"多的所有员工信息
```sql
select ename,sal from emp where sal > (select sal from emp where ename = 'SMITH');
```
![](https://cdn.nlark.com/yuque/0/2023/jpeg/21376908/1692002570088-3338946f-42b3-4174-8910-7e749c31e950.jpeg#averageHue=%23f9f8f8&from=url&id=vMkIU&originHeight=78&originWidth=1400&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=shadow&title=)
## 第19题

19. 列出所有"CLERK"(办事员)的姓名及其部门名称,部门的人数
```sql
select t1.ename,t1.dname,t2.total from (select e.ename,d.dname,d.deptno from emp e join dept d on e.deptno = d.deptno where e.job = 'CLERK') t1 join (select count(*) as total,deptno  from emp group by deptno) t2 on t1.deptno = t2.deptno;
```
## 第20题

20. 列出最低薪金大于1500的各种工作及从事此工作的全部雇员人数
```sql
select job,min(sal),count(*) from emp group by job having min(sal)>1500;
```
## 第21题

21. 列出在部门"SALES"<销售部>工作的员工的姓名,假定不知道销售部的部门编号
```sql
select e.ename,d.dname from emp e join dept d on e.deptno = d.deptno where d.dname='sales';
```
![](https://cdn.nlark.com/yuque/0/2023/jpeg/21376908/1692002570088-3338946f-42b3-4174-8910-7e749c31e950.jpeg#averageHue=%23f9f8f8&from=url&id=SEvqk&originHeight=78&originWidth=1400&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=shadow&title=)
## 第22题

22. 列出薪金高于公司平均薪金的所有员工,所在部门,上级领导,雇员的工资等级
```sql
select e.ename 员工,l.ename 领导,d.dname,s.grade from 
emp e left join emp l on e.mgr = l.empno 
join dept d on e.deptno = d.deptno 
join salgrade s on e.sal between s.losal and s.hisal 
where e.sal > (select avg(sal) from emp);
```
## 第23题

23. 列出与"SCOTT"从事相同工作的所有员工及部门名称
```sql
select e.ename,d.dname,e.job from emp e join dept d on e.deptno=d.deptno where job=(select job from emp where ename ='scott');
```
## 第24题

24. 列出薪金等于部门30中员工的薪金的其他员工的姓名和薪金
```sql
select ename,sal,deptno from emp where sal in(select distinct sal from emp where deptno=30) and deptno <> 30;
```
![](https://cdn.nlark.com/yuque/0/2023/jpeg/21376908/1692002570088-3338946f-42b3-4174-8910-7e749c31e950.jpeg#averageHue=%23f9f8f8&from=url&id=SgqpX&originHeight=78&originWidth=1400&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=shadow&title=)
## 第25题

25. 列出薪金高于在部门30工作的所有员工的薪金的员工姓名和薪金.部门名称
```sql
select e.ename,e.sal,d.dname from emp e join dept d on e.deptno = d.deptno where sal > (select max(sal) from emp where deptno=30);
```
## 第26题

26. 列出在每个部门工作的员工数量,平均工资和平均服务期限
```sql
select avg(sal),count(*),deptno,avg(datediff(now(),hiredate)) as avgtime from emp group by deptno;
```
## 第27题

27. 列出所有员工的姓名、部门名称和工资
```sql
select e.ename,e.sal,d.dname from emp e join dept d on e.deptno = d.deptno;
```
![](https://cdn.nlark.com/yuque/0/2023/jpeg/21376908/1692002570088-3338946f-42b3-4174-8910-7e749c31e950.jpeg#averageHue=%23f9f8f8&from=url&id=wiyCY&originHeight=78&originWidth=1400&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=shadow&title=)
## 第28题

28. 列出所有部门的详细信息和人数
```sql
select d.deptno,d.dname,d.loc,count(e.deptno) from emp e right join dept d on e.deptno=d.deptno group by  d.deptno,d.dname,d.loc;
```
## 第29题

29. 列出各种工作的最低工资及从事此工作的雇员姓名
```sql
select t.job,t.minsal,e.ename from emp e join (select job,min(sal) as minsal from emp group by job) t on e.job=t.job and e.sal=t.minsal;
```
## 第30题

30. 列出各个部门的MANAGER(领导)的最低薪金
```sql
select deptno,min(sal) from emp where job='MANAGER' group by deptno
```
![](https://cdn.nlark.com/yuque/0/2023/jpeg/21376908/1692002570088-3338946f-42b3-4174-8910-7e749c31e950.jpeg#averageHue=%23f9f8f8&from=url&id=kU3lu&originHeight=78&originWidth=1400&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=shadow&title=)
## 第31题

31. 列出所有员工的年工资,按年薪从低到高排序
```sql
select ename,(sal+ifnull(comm,0))*12 as yearsal from emp order by yearsal asc;
```
## 第32题

32. 求出员工领导的薪水超过3000的员工名称与领导名称
```sql
select e.ename 员工名, l.ename 领导名 from emp e join emp l on e.mgr = l.empno where l.sal>3000;
```
## 第33题

33. 求出部门名称中,带'S'字符的部门员工的工资合计、部门人数
```sql
select d.dname,ifnull(sum(sal),0) as sumsal,count(e.ename) from emp e right join dept d on e.deptno=d.deptno where d.dname like '%S%' group by d.dname;
```
## 第34题

34. 给任职日期超过30年的员工加薪10%
```sql
update emp set sal=sal*1.1 where datediff(now(),hiredate)/365 > 30;
```
![](https://cdn.nlark.com/yuque/0/2023/jpeg/21376908/1692002570088-3338946f-42b3-4174-8910-7e749c31e950.jpeg#averageHue=%23f9f8f8&from=url&id=oteIN&originHeight=78&originWidth=1400&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=shadow&title=)
## 第35题

35. 某公司面试题

有3个表S（学生表），C（课程表），SC（学生选课表）
S（SNO，SNAME）代表（学号，姓名）  
C（CNO，CNAME，CTEACHER）代表（课号，课名，教师）
SC（SNO，CNO，SCGRADE）代表（学号，课号，成绩）
```sql
CREATE TABLE SC
(
  SNO      VARCHAR(200),
  CNO      VARCHAR(200),
  SCGRADE  VARCHAR(200)
);

CREATE TABLE S
(
  SNO    VARCHAR(200 ),
  SNAME  VARCHAR(200)
);

CREATE TABLE C
(
  CNO       VARCHAR(200),
  CNAME     VARCHAR(200),
  CTEACHER  VARCHAR(200)
);

INSERT INTO C ( CNO, CNAME, CTEACHER ) VALUES ( '1', '语文', '张'); 
INSERT INTO C ( CNO, CNAME, CTEACHER ) VALUES ( '2', '政治', '王'); 
INSERT INTO C ( CNO, CNAME, CTEACHER ) VALUES ( '3', '英语', '李'); 
INSERT INTO C ( CNO, CNAME, CTEACHER ) VALUES ( '4', '数学', '赵'); 
INSERT INTO C ( CNO, CNAME, CTEACHER ) VALUES ( '5', '物理', '黎明'); 
commit;
 
INSERT INTO S ( SNO, SNAME ) VALUES ( '1', '学生1'); 
INSERT INTO S ( SNO, SNAME ) VALUES ( '2', '学生2'); 
INSERT INTO S ( SNO, SNAME ) VALUES ( '3', '学生3'); 
INSERT INTO S ( SNO, SNAME ) VALUES ( '4', '学生4'); 
commit;
 
INSERT INTO SC ( SNO, CNO, SCGRADE ) VALUES ( '1', '1', '40'); 
INSERT INTO SC ( SNO, CNO, SCGRADE ) VALUES ( '1', '2', '30'); 
INSERT INTO SC ( SNO, CNO, SCGRADE ) VALUES ( '1', '3', '20'); 
INSERT INTO SC ( SNO, CNO, SCGRADE ) VALUES ( '1', '4', '80'); 
INSERT INTO SC ( SNO, CNO, SCGRADE ) VALUES ( '1', '5', '60'); 
INSERT INTO SC ( SNO, CNO, SCGRADE ) VALUES ( '2', '1', '60'); 
INSERT INTO SC ( SNO, CNO, SCGRADE ) VALUES ( '2', '2', '60'); 
INSERT INTO SC ( SNO, CNO, SCGRADE ) VALUES ( '2', '3', '60'); 
INSERT INTO SC ( SNO, CNO, SCGRADE ) VALUES ( '2', '4', '60'); 
INSERT INTO SC ( SNO, CNO, SCGRADE ) VALUES ( '2', '5', '40'); 
INSERT INTO SC ( SNO, CNO, SCGRADE ) VALUES ( '3', '1', '60'); 
INSERT INTO SC ( SNO, CNO, SCGRADE ) VALUES ( '3', '3', '80'); 
commit;
```
问题：
1，找出没选过“黎明”老师的所有学生姓名。
```sql
select sname from s where sno not in(select sno from sc where cno=(select cno from c where cteacher='黎明'));
```
2，列出2门以上（含2门）不及格学生姓名及平均成绩。
```sql
select a.*,b.avgscore from (select s.sno,s.sname,count(sc.scgrade) as num from sc join s on sc.sno=s.sno where sc.scgrade < 60 group by s.sname,s.sno having count(sc.scgrade) >= 2) a join (select sno,avg(scgrade) avgscore from sc group by sno) b on a.sno = b.sno;
```
3，既学过1号课程又学过2号课所有学生的姓名。
```sql
select sc.sno,s.sname from sc join s on sc.sno=s.sno where sc.cno=1 and sc.sno in(select sno from sc where cno=2);
```
![](https://cdn.nlark.com/yuque/0/2023/jpeg/21376908/1692002570088-3338946f-42b3-4174-8910-7e749c31e950.jpeg?x-oss-process=image%2Fresize%2Cw_1177%2Climit_0%2Finterlace%2C1#averageHue=%23f9f8f8&from=url&id=mxe5h&originHeight=66&originWidth=1177&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=shadow&title=)
