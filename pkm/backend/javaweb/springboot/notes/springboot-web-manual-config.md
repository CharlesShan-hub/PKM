# Web 的手动配置(静态资源处理)

**手动配置 web 包括两种方式：**

+ 第一种：配置文件方式（**实际开发中，经常通过这种方式改变默认配置**）
    - 通过修改`application.properties`或`application.yml`，添加`spring.mvc`和`spring.web`相关的配置。
+ 第二种：编写代码方式（**实际开发中，经常通过这种方式扩展新配置**）
    - `编写一个类`实现`WebMvcConfigurer`接口，并`对应重写`接口中的方法即可扩展新的配置。

---

## 配置文件方式

要修改`访问静态资源URL的前缀`，这样配置：

```properties
