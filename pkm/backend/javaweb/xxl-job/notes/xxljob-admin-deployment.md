# 调度中心部署

1. 简单来讲，就是xxl-job需要配套一个调度中心，这是一个springboot项目，自己写的程序的任务发到这个调度中心上来，调度中心是一个独立的服务器。
2. 首先去下载源码
    1. 官网：<https://www.xuxueli.com/index.html>
    2. gihtub：<https://github.com/xuxueli/xxl-job>
3. 然后去运行源码里边的数据库初始化脚本
4. 配置源码里边的xxl-job-admin模块，注意改一下端口（默认是8080，比如改成9090），还有数据库密码。
5. 访问<http://127.0.0.1:9090/xxl-job-admin>即可进入调度中心管理系统。

---

## 源码下载

gitee地址：[https://gitee.com/xuxueli0323/xxl-job](https://gitee.com/xuxueli0323/xxl-job)

下载后解压：

![1744722225300-aaa87349-6bb7-4e7b-b1cc-e5d4e14214a2.png](../assets/1744722225300-aaa87349-6bb7-4e7b-b1cc-e5d4e14214a2.png)

---

## 初始化“调度数据库”

sql脚本位置：/xxl-job/doc/db/tables_xxl_job.sql

![1744722378887-bea3ead0-9368-4658-bcd4-15c74273f6d8.png](../assets/1744722378887-bea3ead0-9368-4658-bcd4-15c74273f6d8.png)

执行该sql脚本：

![1744722454082-d3b3a136-b37a-4c4f-ac9c-a53176a486b7.png](../assets/1744722454082-d3b3a136-b37a-4c4f-ac9c-a53176a486b7.png)

![1744722464766-378b4ba6-a16d-48a3-8a7a-242a71416718.png](../assets/1744722464766-378b4ba6-a16d-48a3-8a7a-242a71416718.png)

---

## 编译源码

将前面下载的源码导入到 IDEA 工具中进行编译。具体操作如下：

1. 将![1744722805975-e889477a-c033-47c0-a94a-7c189b0d31f4.png](../assets/1744722805975-e889477a-c033-47c0-a94a-7c189b0d31f4.png)项目拷贝到IDEA的工作目录下。
2. 使用IDEA将这个工程打开即可。

![1744723153361-cfc22bb1-9c23-4764-aa5a-a72cc9387a74.png](../assets/1744723153361-cfc22bb1-9c23-4764-aa5a-a72cc9387a74.png)

官方解释：

![1744723196974-75cda34b-a842-4dcb-9007-c681dbaf80dc.png](../assets/1744723196974-75cda34b-a842-4dcb-9007-c681dbaf80dc.png)

---

## 配置部署“调度中心”

调度中心项目：xxl-job-admin

### 调度中心配置

调度中心配置文件地址：/xxl-job/xxl-job-admin/src/main/resources/application.properties

该配置文件当下需要重点修改一下`数据源`的配置。主要修改：url、username、password。

![1744723645122-acdd7031-ae33-4905-b40f-73d31551b1d0.png](../assets/1744723645122-acdd7031-ae33-4905-b40f-73d31551b1d0.png)

然后再配置 IDEA 的 Maven，下载项目的 Maven 依赖。

### 执行Spring Boot入口程序

![1744723726029-8ef4adcf-296a-41f2-b957-988a26b98c71.png](../assets/1744723726029-8ef4adcf-296a-41f2-b957-988a26b98c71.png)

### 访问“调度中心”

调度中心访问地址：[http://localhost:8080/xxl-job-admin](http://localhost:8080/xxl-job-admin) (该地址执行器将会使用到，作为回调地址)

![1744723984658-0d242b09-4393-4ce6-89ca-9ffeef47b23a.png](../assets/1744723984658-0d242b09-4393-4ce6-89ca-9ffeef47b23a.png)

默认登录账号 “admin/123456”, 登录后运行界面如下图所示：

![1744724035600-2dc48981-6257-44be-9c2c-ecf110227bed.png](../assets/1744724035600-2dc48981-6257-44be-9c2c-ecf110227bed.png)

