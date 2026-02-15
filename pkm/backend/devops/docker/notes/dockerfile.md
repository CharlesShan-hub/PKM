# dockerfile

* 官网：https://docs.docker.com/reference/dockerfile/

首先我们创建了一个java项目

```java
// src/main/java/com/example/HelloWorld.java
package org.example;

public class Main {
    public static void main(String[] args) {
        System.out.println("🎯 Hello from IDEA + Docker + Java!");
        System.out.println("===================================");
        System.out.println("Java Version: " + System.getProperty("java.version"));
        System.out.println("JVM: " + System.getProperty("java.vm.name"));
        System.out.println("OS: " + System.getProperty("os.name"));
        System.out.println("===================================");
    }
}
```



然后，我们使用idea进行打包。选择到project structure，进入到artifacts，点击加号，选择jar，选择from modules with dependents。弹窗中选择main class，切记！要把META-INF的目录的那个resource去掉，这样才能正常运行。

我们运行这个jar

```bash
charles@Charless-MacBook-Pro ~/w/d/d/j/j/o/a/javademo_jar> java -jar ./javademo.jar
🎯 Hello from IDEA + Docker + Java!
===================================
Java Version: 21.0.9
JVM: OpenJDK 64-Bit Server VM
OS: Mac OS X
===================================
```



下一步，构建dockerfile

```dockerfile
FROM eclipse-temurin:21

LABEL author=charlesshan

COPY javademo.jar /app.jar

EXPOSE 8080

ENTRYPOINT ["java", "-jar", "/app.jar"]
```



在dockerfile的同级目录，构建一下包

```bash
docker build -f dockerfile -t myjavaapp:v1.0 .
```



