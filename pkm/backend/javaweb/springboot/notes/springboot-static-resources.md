# 自动配置中的静态资源处理

web站点中的静态资源指的是：js、css、图片、webjars 等。

webjars 是：**将前端资源（如jQuery、Bootstrap）打包成Java的JAR包，通过Maven依赖管理，像引入Java库一样引入前端库，**现代开发中很少这样用，了解即可**。**

---

## 静态资源处理源码分析

**知识点清单：**

1. **通过spring.web.resources.add-mappings=false 可以关闭默认的静态资源配置。**
2. **当请求路径是 **`**/webjars/**`**格式时，会去 **`**/META-INF/resources/webjars/**`**目录下找静态资源。**
3. **当请求路径是 **`**/**`**格式时（优先匹配控制器，如果匹配不到控制器，才会...），会去 **`**{ "classpath:/META-INF/resources/","classpath:/resources/", "classpath:/static/", "classpath:/public/" }**`**目录下找。**
4. **通过 **`**spring.mvc.static-path-pattern=...**`**配置 URL，通过 **`**spring.web.resources.static-locations=...,...,...,...**`**配置物理路径。**

关于**SpringBoot对静态资源处理的默认配置**，查看`WebMvcAutoConfigurationAdapter`源码，核心源码如下：

<img src="https://cdn.nlark.com/yuque/0/2024/png/21376908/1730356581883-80169fed-c487-4b68-a1f2-70ef95d6c9a6.png" width="1272" title="" crop="0,0,1,1" id="udb36312b" class="ne-image">

对以上源码进行解释：

```java
@Override
public void addResourceHandlers(ResourceHandlerRegistry registry) {

    // 检查 resourceProperties 中的 addMappings 属性是否为 false。如果为 false，则表示不启用默认的静态资源映射处理。
    // 在application.properties配置文件中进行`spring.web.resources.add-mappings=false`配置，可以将其设置为false。
    // 当然，如果没有配置的话，默认值是true。
    if (!this.resourceProperties.isAddMappings()) {
        logger.debug("Default resource handling disabled");
        return;
    }

    // 配置 WebJars 的静态资源处理。
    // this.mvcProperties.getWebjarsPathPattern()的执行结果是：/webjars/**
    // 也就是说，如果请求路径是 http://localhost:8080/webjars/** ，则自动去类路径下的 /META-INF/resources/webjars/ 目录中找静态资源。
    // 如果要改变这个默认的配置，需要在application.properties文件中进行这样的配置：`spring.mvc.webjars-path-pattern=...`
    addResourceHandler(registry, this.mvcProperties.getWebjarsPathPattern(),
            "classpath:/META-INF/resources/webjars/");

    // 配置普通静态资源处理
    // this.mvcProperties.getStaticPathPattern()的执行结果是：/**
    // this.resourceProperties.getStaticLocations()的执行结果是：{ "classpath:/META-INF/resources/","classpath:/resources/", "classpath:/static/", "classpath:/public/" }
    // 也就是说，如果请求路径是：http://localhost:8080/**，根据控制器方法优先原则，会先去找合适的控制器方法，如果没有合适的控制器方法，静态资源处理才会生效，则自动去类路径下的/META-INF/resources/、/resources/、/static/、/public/ 4个位置找。
    // 如果要改变这个默认的配置，需要在application.properties中进行如下的两个配置：
    // 配置URL：spring.mvc.static-path-pattern=...
    // 配置物理路径：spring.web.resources.static-locations=...,...,...,...
    addResourceHandler(registry, this.mvcProperties.getStaticPathPattern(), (registration) -> {
        registration.addResourceLocations(this.resourceProperties.getStaticLocations());
        if (this.servletContext != null) {
            ServletContextResource resource = new ServletContextResource(this.servletContext, SERVLET_LOCATION);
            registration.addResourceLocations(resource);
        }
    });
}
```

---

## 关于WebJars静态资源处理

**知识点清单：**

1. **默认规则是：当请求路径是**`**/webjars/**`**，则会去**`**classpath:/META-INF/resources/webjars/**`**找。WebJars介绍WebJars 是一种将常用的前端库（如 jQuery、Bootstrap、Font Awesome 等）打包成 JAR 文件的形式，方便在 Java 应用程序中使用。WebJars 提供了一种标准化的方式来管理前端库，使其更容易集成到 Java 项目中，并且可以利用 Maven 的依赖管理功能。WebJars在SpringBoot中的使用WebJars官网：**[https://www.webjars.org/](https://www.webjars.org/)

<img src="https://cdn.nlark.com/yuque/0/2024/png/21376908/1730364165294-a000b7b4-9fdb-4c40-99f5-c47f2f25ad9e.png" width="1662" title="" crop="0,0,1,1" id="u242a8d01" class="ne-image">

在官网上可以找到某个webjars的maven依赖，将依赖加入到SpringBoot项目中，例如我们添加vue的依赖：

```xml
<dependency>
    <groupId>org.webjars.npm</groupId>
    <artifactId>vue</artifactId>
    <version>3.5.12</version>
</dependency>
```

如下图表示加入成功：

<img src="https://cdn.nlark.com/yuque/0/2024/png/21376908/1730364253405-dc6801f0-6122-49eb-9e77-36ef92668f5b.png" width="423" title="" crop="0,0,1,1" id="u48c3a316" class="ne-image">

在jar包列表中也可以看到：

<img src="https://cdn.nlark.com/yuque/0/2024/png/21376908/1730364333436-43d60b44-fb7b-454d-b586-f948930ea146.png" width="348" title="" crop="0,0,1,1" id="u91db16e9" class="ne-image">

在SpringBoot中，对WebJars的默认访问规则是：当请求路径是`/webjars/**`，则会去`classpath:/META-INF/resources/webjars/`找。

因此我们要想访问上图的`index.js`，则应该发送这样的请求路径：`http://localhost:8080/webjars/vue/3.5.12/index.js`

启动服务器，打开浏览器，访问，测试结果如下：

<img src="https://cdn.nlark.com/yuque/0/2024/png/21376908/1730364535656-fd9fb574-ce9d-4278-96a4-7d71207e1446.png" width="569" title="" crop="0,0,1,1" id="u97e53581" class="ne-image">

和IDEA中的文件对比一下，完全一样则表示测试成功：

<img src="https://cdn.nlark.com/yuque/0/2024/png/21376908/1730364567084-7ac48323-e220-4e10-a4b6-dc5a30ab6955.png" width="640" title="" crop="0,0,1,1" id="u0888bca8" class="ne-image">

---

## 关于普通静态资源处理**知识点清单：当请求路径是**[**http://localhost:8080/**](http://localhost:8080/**)**，根据控制器方法优先原则，会先去找合适的控制器方法，如果没有合适的控制器方法，静态资源处理才会生效，则自动去类路径下的以下4个位置查找：**

+ **classpath:/META-INF/resources/**
+ **classpath:/resources/**
+ **classpath:/static/**
+ **classpath:/public/ **

我们可以在项目中分别创建以上4个目录，在4个目录当中放入静态资源，例如4张图片：

<img src="https://cdn.nlark.com/yuque/0/2024/png/21376908/1730364803886-d7b87794-d9b4-45ef-b5c2-3f2e4175675c.png" width="243" title="" crop="0,0,1,1" id="ud79cc286" class="ne-image">

<img src="https://cdn.nlark.com/yuque/0/2024/png/21376908/1730364994809-b6cfb675-1518-4a77-acbd-d8dfa5f4c638.png" width="315" title="" crop="0,0,1,1" id="u300fccec" class="ne-image">

然后启动服务器，打开浏览器，访问，测试是否可以正常访问图片：

<img src="https://cdn.nlark.com/yuque/0/2024/png/21376908/1730365066712-a89265e6-eb88-4306-b95b-bc85d2e72f9d.png" width="479" title="" crop="0,0,1,1" id="u9759e11f" class="ne-image">

<img src="https://cdn.nlark.com/yuque/0/2024/png/21376908/1730365080259-ad76485e-b65e-4660-9a70-8cfbc4497383.png" width="450" title="" crop="0,0,1,1" id="u3e9c81f5" class="ne-image">

<img src="https://cdn.nlark.com/yuque/0/2024/png/21376908/1730365090833-de32f7cc-a61c-4896-b151-4851c8d10bc2.png" width="442" title="" crop="0,0,1,1" id="ub6ba10e3" class="ne-image">

<img src="https://cdn.nlark.com/yuque/0/2024/png/21376908/1730365102733-3c375cf4-4bd2-4888-8090-b222a15907d3.png" width="446" title="" crop="0,0,1,1" id="u42ac3ea3" class="ne-image">

---

## 关于静态资源缓存处理

**什么是静态资源缓存，谁缓存，有什么用？**

静态资源缓存指的是浏览器的缓存行为，浏览器可以将静态资源（js、css、图片、声音、视频）缓存到浏览器中，只要下一次用户访问同样的静态资源直接从缓存中取，不再从服务器中获取，可以降低服务器的压力，提高用户的体验。而这个缓存策略可以在服务器端程序中进行设置，SpringBoot对静态资源缓存的默认策略就是以下这三行代码：

<img src="https://cdn.nlark.com/yuque/0/2024/png/21376908/1730365697951-98a6687d-dc95-49fe-bf63-6afac28ac62b.png" width="1160" title="" crop="0,0,1,1" id="u4b1f0213" class="ne-image">

**以上三行代码的解释如下：**

+ **registration.setCachePeriod(getSeconds(this.resourceProperties.getCache().getPeriod()));**
    - 设置缓存的过期时间，默认配置是 null。不设置缓存时间，由浏览器自己决定。
    -  假设配置为 3600 秒，则在 1 小时内浏览器都走缓存。
    - 可以通过`application.properties`的来修改默认的过期时间，例如：`**spring.web.resources.cache.period=3600**`**或者**`**spring.web.resources.cache.period=1h**`
+ **registration.setCacheControl(this.resourceProperties.getCache().getCachecontrol().toHttpCacheControl());**
    - 设置静态资源的 Cache-Control HTTP 响应头，告诉浏览器如何去缓存这些资源。
    - `**Cache-Control**`**HTTP 响应头   是HTTP响应协议的一部分内容。如下图：**

<img src="https://cdn.nlark.com/yuque/0/2024/png/21376908/1730367060571-fb49d8ba-39d5-4a04-9c6b-cbce0add9283.png" width="834" title="" crop="0,0,1,1" id="u80015d4f" class="ne-image">

    - **常见的 Cache-Control 指令包括：**
        * **max-age=<seconds>**：资源在指定秒数内被视为新鲜，浏览器直接使用缓存，无需请求服务器。**
        * **public**：明确声明该响应可以被所有缓存（浏览器、CDN、代理服务器）存储和共享。**
        * **private**：该响应只能存储在最终用户的浏览器缓存中，禁止CDN或代理服务器缓存。**
        * **no-cache**：可以缓存响应副本，但每次使用前必须向服务器验证其有效性（Last-Modified）。**
        * **no-store**：禁止以任何形式（内存或磁盘）缓存响应内容，每次都必须从服务器获取。**
    - 例如：max-age=3600, public：表示响应在 3600 秒内有效，并且可以被任何缓存机制缓存。
    - 可以通过`spring.web.resources.cache.cachecontrol.max-age=3600`以及`spring.web.resources.cache.cachecontrol.cache-public=true`进行重新配置。
+ **registration.setUseLastModified(this.resourceProperties.getCache().isUseLastModified());**
    - **作用**：控制是否在静态资源响应头中添加资源的最后修改时间。**
    - **默认值**：Spring Boot 默认启用，会添加最后修改时间。**
    - **浏览器行为**：浏览器会发送请求，将缓存资源的最后修改时间与服务器端比对，无变化则使用缓存。**
    - **配置方式**：通过**`**spring.web.resources.cache.use-last-modified=false**`**可禁用此功能。**

---

## 静态资源缓存测试

根据之前源码分析，得知`静态资源缓存`相关的配置应该使用`spring.web.resources.cache`：

<img src="https://cdn.nlark.com/yuque/0/2024/png/21376908/1730429586708-40337969-1725-4459-879b-2299ab2a4405.png" width="1107" title="" crop="0,0,1,1" id="u57b7f807" class="ne-image">

<img src="https://cdn.nlark.com/yuque/0/2024/png/21376908/1730429704722-ad0a5409-038f-48f1-9986-809c24f82369.png" width="943" title="" crop="0,0,1,1" id="u414de729" class="ne-image">

<img src="https://cdn.nlark.com/yuque/0/2024/png/21376908/1730429724705-e10888fe-f2aa-4b87-9581-e2641c3e30fd.png" width="897" title="" crop="0,0,1,1" id="u16406168" class="ne-image">

<img src="https://cdn.nlark.com/yuque/0/2024/png/21376908/1730429747795-51fcc7b3-9dc6-49e3-8cbf-647cfff03b09.png" width="873" title="" crop="0,0,1,1" id="u3a897c50" class="ne-image">

在`application.properties`文件中对缓存进行如下的配置：

```properties
