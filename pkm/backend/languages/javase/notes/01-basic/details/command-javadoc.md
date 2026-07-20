# JavaDoc命令

基本语法

```bash
javadoc [选项] [包名] [源文件]
```

常用选项

```bash
-d <directory>      # 指定输出目录
-author             # 包含@author信息
-version            # 包含@version信息
-encoding <编码>    # 指定源文件编码
-windowtitle <文本> # 浏览器窗口标题
-doctitle <HTML>    # 文档标题
```

案例演示

```bash
# 创建文档目录
mkdir doc

# 示例：为单个文件生成文档
javadoc -d ./doc -author -version Student.java

# 示例：为包生成文档
javadoc -d ./doc -author -version com.example.util

# 示例：指定编码（处理中文）
javadoc -d ./doc -author -version -encoding UTF-8 Student.java

# 示例：生成文档
javadoc -d ./doc \
        -author \
        -version \
        -windowtitle "学生管理系统API" \
        -doctitle "<h1>学生管理系统</h1>" \
        Student.java Course.java Teacher.java

# 查看文档
open ./doc/index.html  # Mac
# 或
start ./doc/index.html # Windows
```
