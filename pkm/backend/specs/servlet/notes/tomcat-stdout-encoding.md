# 关于 Tomcat 标准输出流乱码问题

**当前环境信息如下：**

1. win10 简体中文环境
2. Tomcat 版本： 10.1.48
3. IDEA 版本：2025.2.2
4. JDK 版本：21



**前提是：**

1. IDEA 工具所有涉及到字符编码配置方面都已经配置了 UTF-8
2. Tomcat 服务器的 config/logging.properties 中的字符编码方式也都配置了 UTF-8



**问题是：**在这种情况下，在 Servlet 中使用 `System.out.println()`打印中文时仍然会出现乱码。



**什么原因？**

+ **根本原因：Tomcat容器的标准输出流(System.out)编码与IDEA控制台显示编码不一致。**
+ **具体来说：Tomcat的System.out默认使用GBK编码输出，IDEA控制台期望接收UTF-8编码的文本，编码不匹配导致中文显示为乱码。**
+ **在**`**Servlet**`**程序中可以通过**`****System.out.charset()****`****方法******来获取 Tomcat 容器的标准输出流的字符编码方式，结果是 GBK。**



**怎么解决？在 Tomcat 服务器的 **`**VM options**`**配置中添加这个配置：****-Dstdout.encoding=UTF-8**

![](https://cdn.nlark.com/yuque/0/2025/png/21376908/1762937114583-cb3378ea-1d25-4a48-a6d3-d45eec9c0167.png)
