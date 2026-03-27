# 内容协商时，设置请求参数的名字，默认为format

spring.mvc.contentnegotiation.parameter-name=type

```

再次测试：

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1765110658054-dd06e2f5-da84-4909-bb69-444445f3726a.png" width="547.2" title="" crop="0,0,1,1" id="u2660532f" class="ne-image">

---

## HTTP 消息转换器

### HttpMessageConverter的理解

`HttpMessageConverter`接口，对于这个接口来说，大家应该不陌生，它是消息转换器的顶级接口。

当程序中使用了 `@RequestBody`或 `@ResponseBody`注解时，消息转换器就起作用了。

### 系统默认提供了哪些HttpMessageConverter

查看源码：

WebMvcAutoConfiguration.EnableWebMvcConfiguration extends DelegatingWebMvcConfiguration extends WebMvcConfigurationSupport

在`WebMvcConfigurationSupport`类中有这样一个方法：`addDefaultHttpMessageConverters()` 用来添加默认的`HttpMessageConverter`对象。

通过断点调试，可以发现默认支持6个HttpMessageConverter，如下：

<img src="https://cdn.nlark.com/yuque/0/2024/png/21376908/1730774897755-ad87ddc8-4700-40e4-baee-a28d94000e7a.png" width="845" title="" crop="0,0,1,1" id="u0880e2fa" class="ne-image">

**这6个**`**HttpMessageConverter**`**作用如下：**

1. **ByteArrayHttpMessageConverter:**

用于将字节数组(byte[])与HTTP消息体之间进行转换。这通常用于处理二进制数据，如图片或文件。

2. **StringHttpMessageConverter:**

用于将字符串(String)与HTTP消息体之间进行转换。它支持多种字符集编码，能够处理纯文本内容。

3. **ResourceHttpMessageConverter:**

用于将Spring的Resource对象与HTTP消息体之间进行转换。Resource是Spring中表示资源的接口，可以读取文件等资源。这个转换器对于下载文件或发送静态资源有用。

4. **ResourceRegionHttpMessageConverter:**

用于处理资源的部分内容（即“Range”请求），特别是当客户端请求大文件的一部分时。这对于实现视频流媒体等功能很有用。

5. **AllEncompassingFormHttpMessageConverter:**

用于处理表单，是一个比较全面的form消息转换器。处理标准的application/x-www-form-urlencoded格式的数据，以及包含文件上传的multipart/form-data格式的数据。

6. **MappingJackson2HttpMessageConverter:**

使用Jackson库来序列化和反序列化JSON数据。可以将Java对象转换为JSON格式的字符串，反之亦然。

另外，通过以下源码，也可以看到SpringBoot是根据类路径中是否存在某个类，而决定是否添加对应的消息转换器的：

<img src="https://cdn.nlark.com/yuque/0/2024/png/21376908/1730775823305-dfc2b0c5-6ca1-4e8f-902b-506e3d86246d.png" width="1361" title="" crop="0,0,1,1" id="u3fadfd38" class="ne-image">

<img src="https://cdn.nlark.com/yuque/0/2024/png/21376908/1730775878229-960b3144-1727-4467-899a-6bd16f6bc965.png" width="1343" title="" crop="0,0,1,1" id="ub683010f" class="ne-image">

因此，我们只要引入相关的依赖，让类路径存在某个类，则对应的消息转换器就会被加载。

---

## 定义自己的HttpMessageConverter

可以看到以上6个消息转换器中没有yaml相关的消息转换器，可见，如果要实现yaml格式的内容协商，yaml格式的消息转换器就需要我们自定义了。

### 第一步：引入能够处理yaml格式的依赖

任何一个能够处理yaml格式数据的库都可以，这里选择使用`jackson`的库，因为它既可以处理json，xml，又可以处理yaml。

```xml

<dependency>
  <groupId>com.fasterxml.jackson.dataformat</groupId>
  <artifactId>jackson-dataformat-yaml</artifactId>
</dependency>

```

编写测试程序，简单测试一下这个库的用法：

```java

package com.jkweilai.springboot;

import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.ObjectMapper;
import com.fasterxml.jackson.dataformat.yaml.YAMLFactory;
import com.fasterxml.jackson.dataformat.yaml.YAMLGenerator;
import com.jkweilai.springboot.bean.User;

public class Jackson2YamlTest {
    public static void main(String[] args) throws JsonProcessingException {
        // 创建YAML工厂类
        YAMLFactory yamlFactory = new YAMLFactory().disable(YAMLGenerator.Feature.WRITE_DOC_START_MARKER); // 禁止使用文档头标记
        // 创建对象映射器
        ObjectMapper objectMapper = new ObjectMapper(yamlFactory);
        // 准备数据
        User user = new User("jackson", "jack123");
        // 将数据转换成YAML格式
        String s = objectMapper.writeValueAsString(user);
        System.out.println(s);
    }
}

```

执行结果如下：

<img src="https://cdn.nlark.com/yuque/0/2024/png/21376908/1730778662876-bf7851a4-1e8e-4d64-9584-443fd71cef7e.png" width="263" title="" crop="0,0,1,1" id="uca5f2c46" class="ne-image">

### 第二步：新增一种媒体类型yaml

默认支持xml和json两种媒体类型，要支持yaml格式的，需要新增一个yaml媒体类型，在springboot的配置文件中进行如下配置：

```properties

spring.mvc.contentnegotiation.media-types.yaml=text/yaml

```

注意，以上`types`后面的`yaml`是媒体类型的名字，名字随意，如果媒体类型起名为`xyz`，那么发送请求时的路径应该是这样的：http://localhost:8080/detail?format=xyz

### 第三步：自定义HttpMessageConverter

编写类`YamlHttpMessageConverter`继承`AbstractHttpMessageConverter`，代码如下：

```java

package com.jkweilai.springboot.config;

import com.fasterxml.jackson.databind.ObjectMapper;
import com.fasterxml.jackson.dataformat.yaml.YAMLFactory;
import com.fasterxml.jackson.dataformat.yaml.YAMLGenerator;
import com.jkweilai.springboot.bean.User;
import org.springframework.http.HttpInputMessage;
import org.springframework.http.HttpOutputMessage;
import org.springframework.http.MediaType;
import org.springframework.http.converter.AbstractHttpMessageConverter;
import org.springframework.http.converter.HttpMessageNotReadableException;
import org.springframework.http.converter.HttpMessageNotWritableException;

import java.io.IOException;
import java.nio.charset.Charset;

public class YamlHttpMessageConverter extends AbstractHttpMessageConverter<Object> {

    private ObjectMapper objectMapper = new ObjectMapper(new YAMLFactory().disable(YAMLGenerator.Feature.WRITE_DOC_START_MARKER));

    public YamlHttpMessageConverter() {
        // 让 消息转换器 和 媒体类型 text/yaml 绑定在一起。
        super(new MediaType("text", "yaml", Charset.forName("UTF-8")));
    }

    @Override
    protected boolean supports(Class<?> clazz) {
        // 表示User类型的数据支持yaml，其他类型不支持
        return User.class.isAssignableFrom(clazz);
    }

    // 处理 @RequestBody（将提交的yaml格式数据转换为java对象）
    @Override
    protected Object readInternal(Class<?> clazz, HttpInputMessage inputMessage) throws IOException, HttpMessageNotReadableException {
        return null;
    }

    // 处理 @ResponseBody（将java对象转换为yaml格式的数据）
    @Override
    protected void writeInternal(Object o, HttpOutputMessage outputMessage) throws IOException, HttpMessageNotWritableException {
        this.objectMapper.writeValue(outputMessage.getBody(), o);
        // 注意：spring框架会自动关闭输出流，无需程序员手动释放。
    }
}

```

### 第四步：配置消息转换器

重写`WebMvcConfigurer`接口的`configureMessageConverters`方法：

```java

package com.jkweilai.springboot.config;

import org.springframework.context.annotation.Configuration;
import org.springframework.http.converter.HttpMessageConverter;
import org.springframework.web.servlet.config.annotation.WebMvcConfigurer;

import java.util.List;

@Configuration
public class WebConfig implements WebMvcConfigurer {
    @Override
    public void configureMessageConverters(List<HttpMessageConverter<?>> converters) {
        converters.add(new YamlHttpMessageConverter());
    }
}

```

启动服务器并测试：http://localhost:8080/detail?type=yaml

<img src="https://cdn.nlark.com/yuque/0/2024/png/21376908/1730783005228-fe11e134-539e-4291-a12a-f2f83f9b9705.png" width="404" title="" crop="0,0,1,1" id="u21aa8574" class="ne-image">

