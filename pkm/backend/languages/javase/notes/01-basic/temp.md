<img src="https://cdn.nlark.com/yuque/0/2025/jpeg/21376908/1757681056420-39d1bc52-55fe-4f3b-8183-b4d7ba79b166.jpeg" width="4308" title="" crop="0,0,1,1" id="u7e6a4c9c" class="ne-image">

# 本章内容概要

+ 计算机概述（了解）ok
+ 计算机语言概述（了解）ok
+ Java语言概述（了解）ok
+ Java的加载与执行（理解）
+ 第一个Java程序（掌握）
+ Java程序的注释（掌握）
+ public class与class的区别（掌握）

# 本章内容详解

### Java的三大分支

Java的三大分支：

+ **Java SE（Java Standard Edition）**：Java的标准版，它包含了Java语言的核心部分，包括基础类库、虚拟机和开发工具等。Java SE主要用于开发桌面应用程序、控制台程序和小型服务器端应用程序等。
+ **Java EE（Java Enterprise Edition）**：Java的企业版，它是在Java SE的基础上扩展而来，主要用于开发大型企业级应用程序，如电子商务系统、ERP系统和CRM系统等。Java EE包含了许多企业级技术，如Servlet、JSP、EJB、JMS、JTA等。
+ **Java ME（Java Micro Edition）**：Java的微型版，它主要用于嵌入式设备和移动设备上的应用程序开发，如手机、平板电脑、数码相机、路由器等。Java ME的特点是体积小、速度快、资源占用少，可以在较小的内存和处理能力的设备上运行。

Java的三大分支之间存在一定的关系，可以简单概括为：

+ Java SE是Java的核心部分，Java EE和Java ME都是在Java SE的基础上进行扩展和定制。
+ Java EE是在Java SE的基础上增加了更多的企业级技术，如Servlet、JSP、EJB、JMS、JTA等，用于开发大型企业级应用程序。
+ Java ME是在Java SE的基础上进行裁剪和优化，使其适合嵌入式设备和移动设备上的应用程序开发。

总之，Java SE是Java的基础，Java EE和Java ME都是在Java SE的基础上进行扩展和定制，用于不同领域的应用程序开发。

### Java语言特性

Java语言的特点包括：

1. **简单易学**：Java语言的语法和C语言很相似，但是它去掉了C中的复杂的指针和多重继承等特性，使得Java语言更加简单易学。
2. **面向对象**：Java语言是一种纯面向对象的编程语言，它支持对象的封装、继承和多态等面向对象的特性。
3. **<font style="color:#DF2A3F;">平台无关性（跨平台性：一次编译到处运行）</font>**：Java语言的程序可以在不同的操作系统和硬件平台上运行，这是因为Java程序被编译成字节码，而不是机器码，字节码可以在任何支持Java虚拟机的平台上运行。实现原理：不同的操作系统上安装属于自己的Java虚拟机，而Java虚拟机屏蔽了各个操作系统之间的差异，从而做到跨平台。
4. **安全性**：Java语言具有很高的安全性，它提供了一系列的安全措施来保护程序不受恶意攻击和病毒侵害。
5. **高性能**：Java语言具有很高的性能，它采用了一系列优化措施来提高程序的执行速度和内存使用效率。
6. **多线程支持**：Java语言具有很好的多线程支持，它提供了一系列的线程控制机制，使得程序可以更好地利用计算机的多核处理能力。
7. **<font style="color:#DF2A3F;">自动垃圾回收机制</font>**：Java语言采用的是垃圾回收机制（Garbage Collection，简称GC），也就是自动内存管理机制。在传统的编程语言中，程序员需要手动分配和释放内存，容易出现内存泄漏和悬挂指针等问题。而Java语言采用的垃圾回收机制可以自动分配和释放内存，避免了这些问题。

总之，Java语言是一种强大的、易学的、安全的、跨平台的编程语言，它在企业级应用开发、Web应用开发、移动应用开发和嵌入式系统开发等领域都有广泛的应用。

<img src="https://cdn.nlark.com/yuque/0/2025/jpeg/21376908/1757681161591-5634ad1e-a790-40da-8125-381974007490.jpeg" width="4308" title="" crop="0,0,1,1" id="ud097d47e" class="ne-image">

## Java的加载与执行（理解）

<img src="https://cdn.nlark.com/yuque/0/2023/png/21376908/1684555441572-1410145a-2783-4eb4-99c8-6a9a8e953c27.png" width="1586" title="" crop="0,0,1,1" id="u3b26fd19" class="ne-image">

1. 包含两个阶段：编译阶段和运行阶段。
2. 编译阶段和运行阶段可以在不同的操作系统上完成。
3. 编译后删除java源程序，不会影响程序的执行。
4. 生成的class文件如果是A.class，则类名为A。如果是Hello.class，则类名为Hello。
5. javac是负责编译的命令。
6. java是负责运行的命令。
7. class文件不是机器码，操作系统无法直接执行。只有JVM才能看懂。
8. JVM会把class字节码解释为机器码，这样操作系统才能看懂。
9. 类加载器是如何找到class文件的？是通过环境变量CLASSPATH中的路径去搜索的。
10. Java程序要想运行，必须有JVM才行。JVM怎么安装？只要安装了JRE，JRE中自带JVM。
11. JDK、JRE、JVM分别是什么？它们的关系是？

<img src="https://cdn.nlark.com/yuque/0/2023/jpeg/21376908/1684554172873-99561050-f5cc-429f-9d2f-7b188f6d82d3.jpeg" width="775" title="" crop="0,0,1,1" id="u2615497d" class="ne-image">

+ **JDK（Java Development Kit）**：Java开发工具包，包含了Java开发所需的所有工具和类库，包括JRE（Java Runtime Environment）和JVM（Java Virtual Machine）。
+ **JRE（Java Runtime Environment）**：Java运行时环境，包含了Java虚拟机和运行Java程序所需的类库等文件。
+ **JVM（Java Virtual Machine）**：Java虚拟机，是Java程序的运行环境，能够在各种平台上运行Java程序，它将Java字节码解释成本地机器码执行。

<img src="https://cdn.nlark.com/yuque/0/2025/jpeg/21376908/1757681168720-a82b410b-2bbe-4749-a27f-903a1d96ef68.jpeg" width="4308" title="" crop="0,0,1,1" id="ub4f6da3c" class="ne-image">

## 第一个Java程序（掌握）

### JDK下载和安装（Windows）

以下是详细的步骤：

1. 下载 JDK21 安装文件
   在Oracle官网下载JDK21 的安装文件，下载地址为：[https://www.oracle.com/java/technologies/downloads/#jdk21-windows](https://www.oracle.com/java/technologies/downloads/#jdk21-windows)。根据你的操作系统版本和位数，选择相应的安装文件进行下载。
2. 运行安装程序
   双击下载的安装文件，启动安装程序。在弹出的安装程序窗口中，点击"Next"按钮，开始安装。
3. 选择安装路径
   在弹出的"Custom Setup"窗口中，选择JDK17的安装路径。建议选择默认路径，也可以根据需要进行自定义路径设置。点击"Next"按钮继续。
4. 安装组件
   在弹出的"Custom Setup"窗口中，选择需要安装的组件。建议选择全部组件，以确保安装的完整性。点击"Next"按钮继续。
5. 等待安装完成
   在弹出的"Ready to Install"窗口中，点击"Install"按钮，开始安装。安装程序会自动完成安装，需要等待一段时间。
6. **<font style="color:#DF2A3F;">配置环境变量PATH</font>**
   在安装完成后，需要将JDK17的安装路径添加到环境变量中，使其可以被系统识别。具体操作步骤如下：
   + 右键点击"我的电脑"或"此电脑"图标，选择"属性"。
   + 在弹出的窗口中，选择"高级系统设置"。
   + 在弹出的"系统属性"窗口中，选择"高级"选项卡，点击"环境变量"按钮。
   + 在弹出的"环境变量"窗口中，找到"系统变量"中的"Path"变量，点击"编辑"按钮。
   + 在弹出的"编辑环境变量"窗口中，点击"新建"按钮，添加JDK17的安装路径。例如：C:\Program Files\Java\jdk-17。
   + 点击"确定"按钮，保存设置。
7. 验证安装
   打开命令行窗口，输入"java -version"命令，如果输出JDK17的版本信息，则安装成功。如果未能输出版本信息，则需要重新检查环境变量的设置是否正确。

<img src="https://cdn.nlark.com/yuque/0/2025/jpeg/21376908/1757681177017-ee872c21-608a-441e-bcdc-dfcf506abe50.jpeg" width="4308" title="" crop="0,0,1,1" id="u393c7468" class="ne-image">

### JDK下载和安装（macOS）

以下是详细的步骤：

1. 下载地址：[https://www.oracle.com/java/technologies/downloads/#jdk17-mac](https://www.oracle.com/java/technologies/downloads/#jdk17-mac)
   <img src="https://cdn.nlark.com/yuque/0/2023/png/21376908/1684592443947-d71e0db9-e335-4cd8-a665-eb9dda18fbdf.png" width="1167" title="" crop="0,0,1,1" id="u662a38bd" class="ne-image">
2. 下载后的dmg文件
   <img src="https://cdn.nlark.com/yuque/0/2023/png/21376908/1684592481903-dc01e203-484a-4775-909d-df55974b02a0.png" width="266" title="" crop="0,0,1,1" id="u07b72c6d" class="ne-image">
3. 双击dmg安装包
   <img src="https://cdn.nlark.com/yuque/0/2023/png/21376908/1684592490602-6b2417a7-53e0-4c5f-8f9c-ae6101b889a8.png" width="299" title="" crop="0,0,1,1" id="u50a7537b" class="ne-image">
4. 双击pkg文件后，一步一步安装即可
   <img src="https://cdn.nlark.com/yuque/0/2023/png/21376908/1684592577210-fc4ac665-19fa-4906-a3ed-e2ce4004daaa.png" width="615" title="" crop="0,0,1,1" id="u22b14a8a" class="ne-image">
   <img src="https://cdn.nlark.com/yuque/0/2023/png/21376908/1684592632674-008f3d31-6f00-40bd-bd7b-d4b5f29aca4c.png" width="620" title="" crop="0,0,1,1" id="ue9b09383" class="ne-image">
   <img src="https://cdn.nlark.com/yuque/0/2023/png/21376908/1684592646074-2304e049-50a7-4bfd-acca-878180f32f16.png" width="612" title="" crop="0,0,1,1" id="u079c1a2a" class="ne-image">
   <img src="https://cdn.nlark.com/yuque/0/2023/png/21376908/1684592659261-a272abed-e1c0-45d4-8e65-a793a18908ea.png" width="620" title="" crop="0,0,1,1" id="u7f7eb9f8" class="ne-image">
5. 安装完毕后，打开终端，输入java -version，然后输入javac -version，如下图显示表示安装成功了
   <img src="https://cdn.nlark.com/yuque/0/2023/png/21376908/1684592673881-10215487-6ebc-42ec-8cbe-502ab46d364c.png" width="613" title="" crop="0,0,1,1" id="uc1d8b982" class="ne-image">

如果你的macOS上曾经安装过JDK其他版本，如果你想让系统默认使用你安装的最新的JDK17，你还需要按照以下步骤设置环境变量JAVA_HOME：

1. 打开终端，输入以下命令查看JDK的安装路径：
   ```bash
   /usr/libexec/java_home -v 17
   ```
2. 复制上述命令输出的路径，例如：
   ```bash
   /Library/Java/JavaVirtualMachines/jdk-17.jdk/Contents/Home
   ```
3. 打开终端，输入以下命令打开.bash_profile文件：
   ```bash
   sudo vim ~/.bash_profile
   ```
4. 在.bash_profile文件中添加以下内容：
   ```bash
   export JAVA_HOME=/Library/Java/JavaVirtualMachines/jdk-17.jdk/Contents/Home
   export PATH=$PATH:$JAVA_HOME/bin
   ```
   重点：在 ~/.bash_profile 文件中添加以上内容后，按ESC键，输入:wq，保存退出。
5. 保存并关闭.bash_profile文件，输入以下命令使配置生效：
   ```bash
   source ~/.bash_profile
   ```
6. 输入以下命令测试JAVA_HOME环境变量是否配置成功：
   ```bash
   echo $JAVA_HOME
   ```
   如果输出的路径与步骤2中复制的路径一致，则说明配置成功。

<img src="https://cdn.nlark.com/yuque/0/2025/jpeg/21376908/1757681188275-dc0f0c02-dc8c-48a8-b6bc-b2cb2e01ca66.jpeg" width="4308" title="" crop="0,0,1,1" id="u05ee77c4" class="ne-image">

### JDK目录说明

1. <font style="color:#DF2A3F;">bin目录：包含JDK17的可执行文件，如java、javac、javadoc等。</font>
2. conf目录：包含JDK17的配置文件，如Java安全策略文件、JVM配置文件等。
3. include目录：包含头文件，用于开发C和C++应用程序。
4. jmods目录：包含模块化的JDK17组件，使得开发者可以更方便地构建和管理应用程序。
5. legal目录：包含JDK17的相关法律文件和许可证信息。
6. <font style="color:#DF2A3F;">lib目录：包含JDK17的类库和其他支持文件，如JVM库、JDBC驱动程序等。</font>
7. release文件：包含JDK17的版本信息和发布说明。
8. <font style="color:#DF2A3F;">lib/src.zip文件：包含JDK17的源代码，用于开发者进行Java开发。</font>
9. README文件：包含JDK17的安装说明和使用指南。
10. LICENSE文件：包含JDK17的许可证信息，开发者需要了解并遵守相关规定。

### 编写第一个Java程序

在任意位置新建HelloWorld.java文件，注意：必须确保该文件的扩展名是：.java，然后使用任意一个文本编辑器打开并编写如下代码。代码要严格照抄，包括大小写、换行、缩进等，总之，要和以下代码一模一样：

```java
public class HelloWorld {
    public static void main(String[] args){
        System.out.println("Hello World!");
    }
}
```

### 编译第一个Java程序

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

**<font style="color:#DF2A3F;">要点：javac命令后面跟的是java源文件的路径。路径可以是绝对路径，也可以是相对路径。</font>**

编译成功后会生成.class字节码文件。

<img src="https://cdn.nlark.com/yuque/0/2025/jpeg/21376908/1757681192323-5fd5bb7b-114a-433e-adab-2abe0b734cb1.jpeg" width="4308" title="" crop="0,0,1,1" id="u7b058810" class="ne-image">

### 运行第一个Java程序

**<font style="color:#DF2A3F;">这里有一个非常重要的步骤：首先在DOS命令窗口中将路径切换到class文件所在位置。这一步非常关键。</font>**

然后执行以下命令：

```plain
java 类名
```

运行Java程序需要使用的命令是：java

java命令怎么用？java命令后面跟的是"类名"，而不是文件的路径。

什么是类名：A.class则类名为A；B.class则类名为B；HelloWorld.class则类名为HelloWorld

运行成功后，会打印一句话。

### 理解环境变量CLASSPATH

1. CLASSPATH是一个环境变量。隶属于Java。（之前接触过的PATH也是一个环境变量，隶属于windows系统的。）
2. CLASSPATH环境变量是给JVM的类加载器指路的。
3. 如果CLASSPATH没有配置的话，默认从当前路径下查找并加载类。
4. 如果显示的配置了CLASSPATH的话，只会从配置的CLASSPATH中加载类。不再从当前路径下加载。

## Java注释（掌握）

### 注释有什么用

Java中的注释是用于解释和说明代码的文本，它不会被编译器编译，也不会被程序执行。注释的作用如下：

1. 代码的解释说明：注释可以解释代码的功能，作用，实现方法等，让其他程序员更容易理解代码。
2. 代码的调试：在程序调试的过程中，注释可以帮助程序员快速定位问题所在。
3. 文档生成：注释可以用于自动生成文档，方便其他人阅读和使用代码。
4. 代码的维护：注释可以帮助程序员更好地维护代码，防止出现不必要的错误。

总之，注释是程序设计中的重要工具，能够提高代码的可读性和可维护性，减少程序错误。

<img src="https://cdn.nlark.com/yuque/0/2025/jpeg/21376908/1757681205413-7656d173-7b84-4850-a4e9-1c0093a471e1.jpeg" width="4308" title="" crop="0,0,1,1" id="u4a7ae208" class="ne-image">

### 怎么写好注释

写好注释需要一定的技巧和经验，以下是一些写好注释的技巧：

1. 注释要简洁明了。注释应该简短、精炼、易于理解，不要冗长、重复或者难以理解。
2. 注释要准确无误。注释必须准确描述代码的功能、参数、返回值、限制条件等，不能有误导性的描述。
3. 注释要规范化。注释应该遵循一定的规范，如使用特定的注释格式、标记、缩进等，以便于其他程序员阅读和维护。
4. 注释要适当。注释应该适当地使用，不要在每一行代码都加注释，也不要在显而易见的代码上浪费注释。
5. 注释要更新。注释应该及时更新，反映代码的变化和更新，避免注释与代码不一致。
6. 注释要有意义。注释应该有意义，能够解释代码的意图和目的，帮助其他程序员理解代码的设计思想。