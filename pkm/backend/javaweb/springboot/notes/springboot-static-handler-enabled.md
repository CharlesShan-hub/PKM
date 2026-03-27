# 4. 是否开启静态资源默认处理方式（默认是：开启）

spring.web.resources.add-mappings=true

```

注意：`cachecontrol.max-age`配置的话，`period`会被覆盖。

<img src="https://cdn.nlark.com/yuque/0/2024/png/21376908/1730430084806-2086f0b6-646a-4e6a-a39c-8fa8dba74be0.png" width="666" title="" crop="0,0,1,1" id="u9aab9bad" class="ne-image">

启动服务器测试：看看是否在20秒内走缓存，20秒之后是不是就不走缓存了！！！

第一次访问：请求服务器

<img src="https://cdn.nlark.com/yuque/0/2024/png/21376908/1730430573829-f3ac9ce5-fe18-4de9-85b8-4489c3799d74.png" width="960" title="" crop="0,0,1,1" id="u68bc65d7" class="ne-image">

第二次访问：20秒内**开启一个新的浏览器窗口**，再次访问，发现走了缓存

<img src="https://cdn.nlark.com/yuque/0/2024/png/21376908/1730430633080-eb7ae6d1-fb6a-4bcd-beb4-e5df47d9fdf7.png" width="1069" title="" crop="0,0,1,1" id="u0df659fd" class="ne-image">

第三次访问：20秒后**开启一个新的浏览器窗口**，再次访问，发现重新请求服务器

<img src="https://cdn.nlark.com/yuque/0/2024/png/21376908/1730430687390-dc5d00f4-9b08-43cd-9ffc-b538dd4f1fb6.png" width="1076" title="" crop="0,0,1,1" id="u21ec5fbf" class="ne-image">

提示，为什么显示`304`，这是因为这个配置：`spring.web.resources.cache.use-last-modified=true`，浏览器发送了一次验证请求，发现静态资源没有发生变化，最终还是会走缓存的。

---

## web应用的欢迎页面

只要在静态资源路径下提供`index.html`，则被当做欢迎页面。静态资源路径指的是之前的4个路径：

```plain

{ "classpath:/META-INF/resources/", "classpath:/resources/", "classpath:/static/", "classpath:/public/" }

```

测试一下，在`classpath:/static/`目录下新建`index.html`页面：

<img src="https://cdn.nlark.com/yuque/0/2024/png/21376908/1730422047114-993504b3-e8b2-4570-a789-53d1427bb0be.png" width="315" title="" crop="0,0,1,1" id="uf46bcd3f" class="ne-image">

启动服务器，测试结果如下：

<img src="https://cdn.nlark.com/yuque/0/2024/png/21376908/1730422096295-c5fedb9e-df71-4cac-9a24-f2d6da9b071f.png" width="366" title="" crop="0,0,1,1" id="ua606ceb5" class="ne-image">

如果同时在4个静态资源路径下都提供`index.html`，哪个页面会被当做欢迎页呢？

<img src="https://cdn.nlark.com/yuque/0/2024/png/21376908/1730422239619-ba967027-498c-4f90-a139-c1565c91328d.png" width="269" title="" crop="0,0,1,1" id="uc56902eb" class="ne-image">

启动服务器，测试结果如下：

<img src="https://cdn.nlark.com/yuque/0/2024/png/21376908/1730422275754-3b1e145f-f34b-4eac-ae6f-0187eb852282.png" width="935" title="" crop="0,0,1,1" id="u446389e5" class="ne-image">

原因是什么呢？这是因为`classpath:/META-INF/resources/`是数组的首元素，因此先从这个路径下找欢迎页。

<img src="https://cdn.nlark.com/yuque/0/2024/png/21376908/1730422431137-93db3613-613e-434b-b7b8-c9f1af68636c.png" width="1060" title="" crop="0,0,1,1" id="u4fdaf209" class="ne-image">

---

## favorite icon

favicon（也称为“收藏夹图标”或“网站图标”）是大多数现代网页浏览器的默认行为之一。当用户访问一个网站时，浏览器通常会尝试从该网站的根目录下载名为 favicon.ico 的文件，并将其用作标签页的图标。

如果网站没有提供 favicon.ico 文件，浏览器可能会显示一个默认图标，或者根本不显示任何图标。为了确保良好的用户体验，网站开发者通常会在网站的根目录下放置一个 favicon.ico 文件。

Spring Boot项目中`favicon.ico`文件应该放在哪里呢？Spring Boot官方是这样说明的：

<img src="https://cdn.nlark.com/yuque/0/2024/png/21376908/1730427556830-9ba1ca93-5b91-477c-af0f-af51ee850b31.png" width="1905" title="" crop="0,0,1,1" id="u8aff60a0" class="ne-image">

这段话翻译为：

与其他静态资源一样，Spring Boot 会在配置的静态内容位置检查是否存在 `favicon.ico`文件。如果存在这样的文件，它将自动作为应用程序的 favicon 使用。

以上官方说明的：将`favicon.ico`文件放到静态资源路径下即可。

web站点没有提供`favicon.ico`时：

<img src="https://cdn.nlark.com/yuque/0/2024/png/21376908/1730427725460-6c4062dc-df53-495c-8709-431dd38f2337.png" width="370" title="" crop="0,0,1,1" id="u326362e7" class="ne-image">

我们在[https://www.iconfont.cn/](https://www.iconfont.cn/) （阿里巴巴提供的图标库）上随便找一个图标，然后将图片名字命名为`favicon.ico`，然后将其放到SpringBoot项目的静态资源路径下：

<img src="https://cdn.nlark.com/yuque/0/2024/png/21376908/1730427919469-60975be4-d0d3-43ba-8435-98d9da427282.png" width="220" title="" crop="0,0,1,1" id="udea225a4" class="ne-image">

启动服务器测试：记住（ctrl + F5强行刷新一下，避免影响测试效果）

<img src="https://cdn.nlark.com/yuque/0/2024/png/21376908/1730428251364-894a09fe-92fb-408c-89d0-42d8e27b222b.png" width="295" title="" crop="0,0,1,1" id="u6d7e49b4" class="ne-image">

