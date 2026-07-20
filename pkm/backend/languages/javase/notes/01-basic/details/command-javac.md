# javac命令

使用javac命令进行编译。javac命令是Java编译器命令，用于将Java源代码文件编译成Java字节码文件。下面是javac命令的详细用法：

基本用法：

```plain
javac [options] [source files]
```

其中，`[options]`表示编译选项，`[source files]`表示要编译的Java源代码文件。

常用选项：

+ `-classpath <path>`：指定类路径，多个路径之间用分号（Windows）或冒号（Unix/Linux/Mac）分隔。
+ `-d <directory>`：指定输出目录，编译后的字节码文件将保存在该目录下。
+ `-verbose`：显示编译详细信息。
+ `-nowarn`：禁用警告信息。
+ `-source <version>`：指定源代码版本，例如1.8。
+ `-target <version>`：指定生成的字节码版本，例如1.8。
+ `-help`：显示帮助信息。

**要点：javac命令后面跟的是java源文件的路径。路径可以是绝对路径，也可以是相对路径。**

编译成功后会生成.class字节码文件。