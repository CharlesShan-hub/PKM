# 关于路径的总结及作业

1. 前端发送请求的路径：以 `/`开始，添加项目名。
2. `web.xml`中 `<url-pattern>` 配置的路径：以 `/` 开始，不添加项目名。
3. `String realPath = application.getRealPath("/WEB-INF/web.xml");` 以 `/` 开始，不添加项目名
4. `InputStream in = application.getResourceAsStream("/WEB-INF/web.xml");` 以 `/` 开始，不添加项目名
5. 欢迎页面：不以 `/` 开始。从项目的根路径下开始加载。
6. 转发路径：以 `/`开始，不添加项目名。
7. 重定向路径：以 `/`开始，添加项目名。

作业：将部门管理系统修改为三层架构+MVC 架构，加入异常处理机制，优化项目。
