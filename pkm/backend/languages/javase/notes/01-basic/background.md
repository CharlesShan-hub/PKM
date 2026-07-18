# 背景介绍

## 版本
![Java-basic-version.excalidraw|500](../../assets/java-basic-version.svg)
- java的诞生与八卦：[interests](../../details/interests.md)
- LTS（长期支持）：Java 8、Java 11、Java 17、Java21、Java25
- Java 8、JDK 8、JDK 1.8 是同一个版本
- [Java 版本特性总结（官网）](https://www.oracle.com/java/technologies/javase/jdk-relnotes-index.html)
- 新版本更新详细内容：[java-new](../06-java-advanced/java-new.md)
- 商用付费问题（OracleJDK要钱，OpenJDK不要钱）：[money](../../details/money.md)


## 类型
![Java-basic-branch.excalidraw](../../assets/java-basic-branch.svg)

> Java SE是Java的基础，Java EE和Java ME都是在Java SE的基础上进行扩展和定制，用于不同领域的应用程序开发。
+ **Java SE（Java Standard Edition）**：Java的标准版，它包含了Java语言的核心部分，包括基础类库、虚拟机和开发工具等。Java SE主要用于开发桌面应用程序、控制台程序和小型服务器端应用程序等。
+ **Java EE（Java Enterprise Edition）**：Java的企业版，它是在Java SE的基础上扩展而来，主要用于开发大型企业级应用程序，如电子商务系统、ERP系统和CRM系统等。Java EE包含了许多企业级技术，如Servlet、JSP、EJB、JMS、JTA等。
+ **Java ME（Java Micro Edition）**：Java的微型版，它主要用于嵌入式设备和移动设备上的应用程序开发，如手机、平板电脑、数码相机、路由器等。Java ME的特点是体积小、速度快、资源占用少，可以在较小的内存和处理能力的设备上运行。
- [Java 系统学习之三大版本 JavaSE、JavaEE、JavaME](https://blog.csdn.net/fi0stBlooder/article/details/118456420)


## 特性
- 面向对象：继承、封装、多态
- 健壮：强类型机制、异常处理
- 垃圾自动收集（Garbage Collection，简称GC）：在传统的编程语言中，需要手动分配和释放内存，容易出现内存泄漏和悬挂指针等问题。GC可以自动分配和释放内存。
- 跨平台：JVM（class 文件运行在各操作系统的 Java 虚拟机上）
- 解释型语言（class 文件由解释器运行）

> 🤔 为什么 有人说 Java 是“编译与解释并存”的语言？
> 📖 编译器将**源代码**编译为**字节码**（字节码不是二进制，不是机器码），虚拟机解释或 JIT 编译执行生成的**机器码**


## IDE
- [EditPlus](https://www.editplus.com/)
- [Notepad++](https://notepad-plus-plus.org/)
- IntelliJ IDEA
- Eclipse
- Sublime Text
- （以上都是2026年之前的讨论，现在已经vibe coding了）


## JVM、JRE、JDK
![Java-basic-core.excalidraw](../../assets/java-basic-core.svg)

- JVM（**J**ava **V**irtual **M**achine）：虚拟机
- JRE（**J**ava **R**untime **E**nvironment）= JVM + Java 核心库；运行 class 文件需要安装 JRE
- JDK（**J**ava **D**evelopment **K**it）= JRE + 开发工具（如 javac）；开发者安装 JDK 即可
- [JDK、JRE、JVM 关系简述](http://t.csdn.cn/5ctUI)
- [JVM 详解](https://blog.csdn.net/weixin_43410245/article/details/126471338)


## 代码规范
- [Google Java 代码规范](http://doc.vrd.net.cn/codingstyle/google-java-styleguide-zh.pdf)
- [Java 语言规范（JLS）](https://docs.oracle.com/javase/specs/jls/se21/html/)
