# Path 与 Classpath
* 二者区分
    * `Path`：windows系统的环境变量
    * `Classpath`：java类加载器（classloader）的环境变量，**隶属于Java语言**。
* 使用`Classpath`
    * `java Test`命令执行之后，JVM启动类加载器classloader，classloader会通过`classpath`中的路径查找`Test.class`文件。
    * 当`classpath`没有配置的情况下，**默认从当前路径下查找**。 
    * 当`classpath`显式得配置出来之后，则只会从配置的路径中查找，不再从当前路径下查找。