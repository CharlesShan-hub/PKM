# 调度中心部署

---

## 源码下载

gitee地址：[https://gitee.com/xuxueli0323/xxl-job](https://gitee.com/xuxueli0323/xxl-job)

下载后解压：

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1744722225300-aaa87349-6bb7-4e7b-b1cc-e5d4e14214a2.png" width="157" title="" crop="0,0,1,1" id="u3356d280" class="ne-image" style="font-size: 16px">

---

## 初始化“调度数据库”

sql脚本位置：/xxl-job/doc/db/tables_xxl_job.sql

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1744722378887-bea3ead0-9368-4658-bcd4-15c74273f6d8.png" width="389" title="" crop="0,0,1,1" id="u0547cee9" class="ne-image" style="font-size: 16px">

执行该sql脚本：

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1744722454082-d3b3a136-b37a-4c4f-ac9c-a53176a486b7.png" width="198" title="" crop="0,0,1,1" id="u6224cb5e" class="ne-image" style="font-size: 16px">

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1744722464766-378b4ba6-a16d-48a3-8a7a-242a71416718.png" width="230" title="" crop="0,0,1,1" id="udc02ef0e" class="ne-image" style="font-size: 16px">

---

## 编译源码

将前面下载的源码导入到 IDEA 工具中进行编译。具体操作如下：

1. 将<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1744722805975-e889477a-c033-47c0-a94a-7c189b0d31f4.png" width="129" title="" crop="0,0,1,1" id="u1c2e08ae" class="ne-image" style="font-size: 16px">项目拷贝到IDEA的工作目录下。
2. 使用IDEA将这个工程打开即可。

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1744723153361-cfc22bb1-9c23-4764-aa5a-a72cc9387a74.png" width="236" title="" crop="0,0,1,1" id="u587a264a" class="ne-image" style="font-size: 16px">

官方解释：

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1744723196974-75cda34b-a842-4dcb-9007-c681dbaf80dc.png" width="854" title="" crop="0,0,1,1" id="u5ac08608" class="ne-image" style="font-size: 16px">

---

## 配置部署“调度中心”

调度中心项目：xxl-job-admin

### 调度中心配置

调度中心配置文件地址：/xxl-job/xxl-job-admin/src/main/resources/application.properties

该配置文件当下需要重点修改一下`数据源`的配置。主要修改：url、username、password。

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1744723645122-acdd7031-ae33-4905-b40f-73d31551b1d0.png" width="624" title="" crop="0,0,1,1" id="uefd3fd05" class="ne-image" style="font-size: 16px">

然后再配置 IDEA 的 Maven，下载项目的 Maven 依赖。

### 执行Spring Boot入口程序

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1744723726029-8ef4adcf-296a-41f2-b957-988a26b98c71.png" width="768" title="" crop="0,0,1,1" id="u87668d81" class="ne-image" style="font-size: 16px">

### 访问“调度中心”

调度中心访问地址：[http://localhost:8080/xxl-job-admin](http://localhost:8080/xxl-job-admin) (该地址执行器将会使用到，作为回调地址)

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1744723984658-0d242b09-4393-4ce6-89ca-9ffeef47b23a.png" width="413" title="" crop="0,0,1,1" id="u6a4fb2ac" class="ne-image" style="font-size: 16px">

默认登录账号 “admin/123456”, 登录后运行界面如下图所示：

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1744724035600-2dc48981-6257-44be-9c2c-ecf110227bed.png" width="1906" title="" crop="0,0,1,1" id="u70235628" class="ne-image" style="font-size: 16px">

