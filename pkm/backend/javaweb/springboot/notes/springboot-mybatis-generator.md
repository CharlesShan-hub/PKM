# MyBatis逆向生成

MyBatis逆向工程：使用IDEA插件可以根据数据库表的设计逆向生成MyBatis的Mapper接口 与 MapperXML文件。

---

## 安装插件`free mybatis tools`

<img src="https://cdn.nlark.com/yuque/0/2024/png/21376908/1729234849712-989025f9-e324-45c0-a126-48ea9186582b.png" width="974" title="" crop="0,0,1,1" id="ue7276e0c" class="ne-image">

---

## 在IDEA中配置数据源

<img src="https://cdn.nlark.com/yuque/0/2024/png/21376908/1729234975933-38892ecf-5c92-4626-904b-223426f8f026.png" width="873" title="" crop="0,0,1,1" id="u0f8e0ca8" class="ne-image">

---

## 创建数据库，创建表，准备数据

<img src="https://cdn.nlark.com/yuque/0/2024/png/21376908/1729235029429-c3c14165-a775-45e5-a4b8-d9ca303c4a95.png" width="1096" title="" crop="0,0,1,1" id="uf18219e3" class="ne-image">

---

## 使用脚手架创建SpringBoot项目

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1764860374189-0473287e-b071-4f15-a30a-39f3cd29f95b.png" width="735.2" title="" crop="0,0,1,1" id="ub2141eb3" class="ne-image">

添加依赖：mybatis依赖、mysql驱动、Lombok库

<img src="https://cdn.nlark.com/yuque/0/2024/png/21376908/1729235310734-659b79b7-df95-4157-b405-9c0c316f754b.png" width="960" title="" crop="0,0,1,1" id="u57a2b70b" class="ne-image">

---

## 生成MyBatis代码放到SpringBoot项目中

在表上右键：Mybatis-Generator

<img src="https://cdn.nlark.com/yuque/0/2024/png/21376908/1729235071633-a4d6bd7a-dc80-45c3-bc52-31dfee5789bf.png" width="452" title="" crop="0,0,1,1" id="udb3d5963" class="ne-image">

<img src="https://cdn.nlark.com/yuque/0/2024/png/21376908/1729235692907-6637331b-7b98-41d0-9ca2-47ed44c9bab0.png" width="1317" title="" crop="0,0,1,1" id="u7e5420eb" class="ne-image">

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1764940615491-c49e1478-68ec-4ae7-b7ca-7d340bb750e9.png" width="943.2" title="" crop="0,0,1,1" id="u0d53713f" class="ne-image">

代码生成后，如果在IDEA中看不到，这样做（重新从硬盘加载）：

<img src="https://cdn.nlark.com/yuque/0/2024/png/21376908/1729235782802-6c83273c-0b14-405f-a1c8-793fc80c9123.png" width="418" title="" crop="0,0,1,1" id="u96411cc8" class="ne-image">

---

## 编写mybatis相关配置

application.properties属性文件的配置：

```properties
spring.datasource.driver-class-name=com.mysql.cj.jdbc.Driver
spring.datasource.url=jdbc:mysql://localhost:3306/springboot
spring.datasource.username=root
spring.datasource.password=123456

