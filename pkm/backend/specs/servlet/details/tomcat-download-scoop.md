# Windows + Scoop 安装 tomcat

```bash
#添加官方仓库：因为 Tomcat 在 `versions` 这个 bucket 里，先把它加进来。
scoop bucket add versions
    
# 搜索可用版本：加完仓库后，可以搜索一下都有哪些版本能装。
scoop search tomcat
#搜索结果里一般会显示 `tomcat7`、`tomcat8`、`tomcat9`、`tomcat10` 等[](https://blyrin.cn/posts/scoop/)。
    
# 安装指定版本：确定版本后，直接安装就行。比如想装 Tomcat 10：
scoop install versions/tomcat10
```

我一开始scoop默认用的是java8，然后跑不起来，后来换成java21就好了

```bash
scoop reset corretto21-jdk

catalina run
```