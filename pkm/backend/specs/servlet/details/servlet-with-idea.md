# IDEA 开发 Servlet

---

## 创建空项目

![](../assets/1748913446753-c21964d5-0b72-4e48-b350-6bf20e3c6e40.png)

设置空项目的 JDK 版本：

![](../assets/1748913502974-8d899685-e3be-4f44-8a3d-f9e8e63c30b4.png)

---

## 创建普通 java 模块

![](../assets/1748913558492-74e52755-cc21-49b4-b4c5-c17afbd13769.png)

![](../assets/1748913583573-6e2f8ac5-ffc3-4ae1-b31e-6b7530d34e1e.png)

---

## 创建 web 目录作为 webapproot

![](../assets/1748913709042-03821308-47fa-41ae-829e-e7f4d5aa521e.png)

---

## 添加 web 支持

![](../assets/1748914364625-5f2c75ee-3639-48f3-bca0-5e86753c8b06.png)

添加 `web.xml`文件时，选择 `6.0`版本。

---

## 添加 Artifact（构件）

Artifact 是构件的意思，通常指代 **可部署的输出文件** 。

![](../assets/1748914057428-fbd16feb-2246-4004-b23b-bb6abf369172.png)

![](../assets/1748914077270-7e67a197-1bef-4fef-b2fc-a885b912d7ac.png)

---

## 将 servlet-api.jar 添加到 classpath 中

注意，这个 jar 包只是起到一个编译阶段的作用（只是让我们在 IDEA 中编写的 Servlet 程序能够正常编译），因此这个 jar 包不需要放到 `WEB-INF/lib`目录中。因为 `WEB-INF/lib`目录下的 jar 包是在运行阶段起作用的，Tomcat 服务器运行时 `servlet-api.jar` 已经在 `CATALINA_HOME/lib`目录下了。

在 `web01`模块下随意创建一个目录，例如 `lib`，然后将 `servlet-api.jar`拷贝到该目录下，然后 右键-->Add as Library...

如果找不到这个jar包，我提供一个下载的命令

```bash
curl -O https://repo1.maven.org/maven2/jakarta/servlet/jakarta.servlet-api/6.0.0/jakarta.servlet-api-6.0.0.jar
```

推荐下载到src同级别的lib（自己创建）下面

```bash
charles@192 lib % pwd
/Users/charles/workspace/project/learn-servlet/web_porjects/web01/lib
charles@192 lib % ls
jakarta.servlet-api-6.0.0.jar
```


![](../assets/1748914910543-fc6dcee0-621d-4a91-aa78-2d623a5ec4e7.png)

![](../assets/1748914926007-4f215335-359f-492e-9c46-6be98e9e02b6.png)

---

## 添加数据库驱动

在 `WEB-INF`目录下新建 `lib`目录，将 mysql 驱动 jar 包拷贝到该目录下：

![](../assets/1748915011637-3a8d4316-3331-4d59-8be3-cb1f949978e4.png)

这个 jar 包是在运行阶段起作用的，编译阶段不需要。

---

## 编写 Servlet 和 web.xml

使用之前的 `DeptListServlet`程序即可。

```xml
<?xml version="1.0" encoding="UTF-8"?>
<web-app xmlns="https://jakarta.ee/xml/ns/jakartaee"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="https://jakarta.ee/xml/ns/jakartaee https://jakarta.ee/xml/ns/jakartaee/web-app_6_0.xsd"
         version="6.0">
    <servlet>
        <servlet-name>listServlet</servlet-name>
        <servlet-class>com.jkweilai.servlet.DeptListServlet</servlet-class>
    </servlet>
    <servlet-mapping>
        <servlet-name>listServlet</servlet-name>
        <url-pattern>/list</url-pattern>
    </servlet-mapping>
</web-app>
```

---

## IDEA 配置 Tomcat

![](../assets/1748915210485-e44e85af-eec1-44dd-9b72-885e46550159.png)

![](../assets/1748915242384-45f0abe4-6ffe-43e6-b582-642159598d0a.png)

![](../assets/1748915305459-ce611048-6200-402e-ae99-b69815d03ad4.png)

---

## 部署构件到 Tomcat

![](../assets/1748915349507-cd12b852-21db-4040-8179-c7a4b457c28b.png)

![](../assets/1748915490221-5a8b3878-1261-4d52-bb3b-1fee2a75c13e.png)

---

## 启动 Tomcat 测试

![](../assets/1748915526682-0318b4f6-1809-4c59-b52c-6caa7388a274.png)

![](../assets/1748915631683-fb55615b-edcd-4aa2-b736-412dd7d35e37.png)

启动成功，但控制台有中文乱码，这是因为 IDEA 默认的字符编码方式为 UTF-8，需要将 `CATALINA_HOME/conf/logging.properties`文件中之前的修改的 `GBK`，再次改回 `UTF-8`即可：

![](../assets/1748915727373-7b572fd1-07cc-4e9a-83cf-2fcc58db9c2f.png)

打开浏览器访问：<http://localhost:8080/web01/list>

![](../assets/1748915896203-1f751a25-2e85-4251-a00d-ad9c8581e2c7.png)
