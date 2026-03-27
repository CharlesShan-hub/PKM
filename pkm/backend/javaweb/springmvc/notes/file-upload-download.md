# 文件上传和下载

---

## 文件上传

前端页面：

```html

<!DOCTYPE html>
<html lang="en" xmlns:th="http://www.thymeleaf.org">
<head>
    <meta charset="UTF-8">
    <title>文件上传</title>
</head>
<body>

<!--文件上传表单-->
<form th:action="@{/file/up}" method="post" enctype="multipart/form-data">
    文件：<input type="file" name="fileName"/><br>
    <input type="submit" value="上传">
</form>

</body>
</html>

```

重点是：form表单采用post请求，enctype是multipart/form-data，并且上传组件是：type="file"

web.xml文件：

```xml

<!--前端控制器-->
<servlet>
    <servlet-name>dispatcherServlet</servlet-name>
    <servlet-class>org.springframework.web.servlet.DispatcherServlet</servlet-class>
    <init-param>
        <param-name>contextConfigLocation</param-name>
        <param-value>classpath:springmvc.xml</param-value>
    </init-param>
    <load-on-startup>1</load-on-startup>
    <multipart-config>
        <!--设置单个支持最大文件的大小-->
        <max-file-size>102400</max-file-size>
        <!--设置整个表单所有文件上传的最大值-->
        <max-request-size>102400</max-request-size>
        <!--设置最小上传文件大小-->
        <file-size-threshold>0</file-size-threshold>
    </multipart-config>
</servlet>
<servlet-mapping>
    <servlet-name>dispatcherServlet</servlet-name>
    <url-pattern>/</url-pattern>
</servlet-mapping>

```

****重点：在DispatcherServlet配置时，添加 multipart-config 配置信息。****

Controller中的代码：

```java

package com.jkweilai.springmvc.controller;

import jakarta.servlet.http.HttpServletRequest;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.multipart.MultipartFile;

import java.io.*;
import java.util.UUID;

@Controller
public class FileController {

    @RequestMapping(value = "/file/up", method = RequestMethod.POST)
    public String fileUp(@RequestParam("fileName") MultipartFile multipartFile, HttpServletRequest request) throws IOException {
        String name = multipartFile.getName();
        System.out.println(name);
        // 获取文件名
        String originalFilename = multipartFile.getOriginalFilename();
        System.out.println(originalFilename);
        // 将文件存储到服务器中
        // 获取输入流
        InputStream in = multipartFile.getInputStream();
        // 获取上传之后的存放目录
        File file = new File(request.getServletContext().getRealPath("/upload"));
        // 如果服务器目录不存在则新建
        if(!file.exists()){
            file.mkdirs();
        }
        // 开始写
        //BufferedOutputStream out = new BufferedOutputStream(new FileOutputStream(file.getAbsolutePath() + "/" + originalFilename));
        // 可以采用UUID来生成文件名，防止服务器上传文件时产生覆盖
        BufferedOutputStream out = new BufferedOutputStream(new FileOutputStream(file.getAbsolutePath() + "/" + UUID.randomUUID().toString() + originalFilename.substring(originalFilename.lastIndexOf("."))));
        byte[] bytes = new byte[1024 * 100];
        int readCount = 0;
        while((readCount = in.read(bytes)) != -1){
            out.write(bytes,0,readCount);
        }
        // 刷新缓冲流
        out.flush();
        // 关闭流
        in.close();
        out.close();

        return "ok";
    }

}

```

最终测试结果：

<img src="https://cdn.nlark.com/yuque/0/2024/png/21376908/1711331360045-38714fe4-a729-4068-b0a8-f805117da5bf.png" width="372" title="" crop="0,0,1,1" id="ub22497ea" class="ne-image" style="font-size: 16px">

<img src="https://cdn.nlark.com/yuque/0/2024/png/21376908/1711331351567-6b421e6f-b5b6-4bf4-95b8-69404a864530.png" width="388" title="" crop="0,0,1,1" id="u050475b2" class="ne-image" style="font-size: 16px">

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1764670157207-0861a883-7630-4a8c-9681-978099360172.png" width="260.8" title="" crop="0,0,1,1" id="u8dd224d7" class="ne-image" style="font-size: 16px">

****建议：上传文件时，文件起名采用UUID。以防文件覆盖。****

---

## 文件下载

```html

<!--文件下载-->
<a th:href="@{/download}">文件下载</a>

```

文件下载核心程序，使用ResponseEntity：

```java

@GetMapping("/download")
public ResponseEntity<byte[]> downloadFile(HttpServletResponse response, HttpServletRequest request) throws IOException {
    File file = new File(request.getServletContext().getRealPath("/upload") + "/1.jpeg");
    // 创建响应头对象
    HttpHeaders headers = new HttpHeaders();
    // 设置响应内容类型
    headers.setContentType(MediaType.APPLICATION_OCTET_STREAM);
    // 设置下载文件的名称
    headers.setContentDispositionFormData("attachment", file.getName());

    // 下载文件
    ResponseEntity<byte[]> entity = new ResponseEntity<byte[]>(Files.readAllBytes(file.toPath()), headers, HttpStatus.OK);
    return entity;
}

```

效果：

<img src="https://cdn.nlark.com/yuque/0/2024/png/21376908/1711332732449-ed2ddda1-7b8e-405a-af51-e5e2f8452558.png" width="324" title="" crop="0,0,1,1" id="u82ac9055" class="ne-image" style="font-size: 16px">

<img src="https://cdn.nlark.com/yuque/0/2024/png/21376908/1711332745775-3de01f16-df6d-41bd-bc4d-905bedf34687.png" width="1001" title="" crop="0,0,1,1" id="uaf265e4e" class="ne-image" style="font-size: 16px">
