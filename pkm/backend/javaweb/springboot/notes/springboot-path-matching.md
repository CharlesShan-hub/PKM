# web请求的路径匹配

在 SpringBoot 的 web 应用中，web 的请求路径仍然支持模糊匹配，默认支持两种主要的路径匹配策略：

+ Ant风格路径匹配 (AntPathMatcher)【传统方式，现代开发几乎不用】
+ 正则表达式路径匹配 (PathPatternParser)【性能好，现代开发中都用它】

**正则表达式路径匹配语法：匹配 0-N 个字符，不包括 `/`。**    匹配任意数量的目录层级，只能出现在路径末尾。

**?匹配**任意单个字符**。

**[]匹配指定范围内的单个字符。

**{}路径变量，用于提取路径的一部分作为参数。示例：/users/{userId} 匹配 /users/123，提取 userId=123。

```java
@GetMapping("/{path:[a-z]+}/a?/*.do/**")
public String path(HttpServletRequest request, @PathVariable String path){
    return request.getRequestURI() + "," + path;
}
```

启动服务器测试，可用：

<img src="https://cdn.nlark.com/yuque/0/2024/png/21376908/1730472772231-d18e628f-1b62-4757-9299-eaa604344ce6.png" width="521" title="" crop="0,0,1,1" id="TkyEb" class="ne-image">

