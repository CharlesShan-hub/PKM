# Java新特性
---

## 主要内容
1. 新特性的概述
2. 新语法的结构
3. API层面的变化

---


## 学习目标
| **知识点** | **要求** |
| --- | --- |
| 新特性的概述 | 了解 |
| 新语法方面的变化 | 理解 |
| API层面的变化 | 理解 |

---


## Java语言发展史
Java语言的发展历程中的重要事件：

1. 1995年：Java语言诞生，由Sun Microsystems的James Gosling等人开发。
2. 1996年：发布Java 1.0版本。
3. 1998年：发布Java 2（也称为Java SE）版本，引入了重要的新特性，如Swing图形界面工具包、JavaBeans组件技术等。
4. 2004年：发布Java SE 5.0版本，引入了自动装箱/拆箱、泛型、枚举、注解等重要特性。
5. 2006年：Sun Microsystems发布Java SE 6版本，引入了更多的新特性，如JDBC 4.0、JAX-WS 2.0等。
6. 2010年：Oracle公司收购了Sun Microsystems，成为Java语言的主要维护者。
7. 2011年：发布Java SE 7版本，引入了重要的新特性，如Switch语句的字符串支持、NIO 2.0等。
8. 2014年：发布Java SE 8版本，引入了Lambda表达式、Stream API、新的日期/时间API等重要特性。
9. 2017年：发布Java SE 9版本，引入了模块化系统、REPL工具等新特性。
10. 2018年3月：发布Java SE 10版本，引入了局部变量类型推断、G1垃圾收集器等新特性。
11. 2018年9月：发布Java SE 11版本，成为长期支持版本，移除了一些过时的API，引入了新的HTTP Client API等新特性。
12. 2019年3月：发布Java SE 12版本，增加了Switch表达式、新的垃圾回收器Shenandoah等特性。
13. 2019年9月：发布Java SE 13版本，增加了文本块、改进的Switch表达式、动态CDS等特性。
14. 2020年3月：发布Java SE 14版本，增加了Switch表达式的模式匹配、Records、改进的垃圾回收器等特性。
15. 2020年9月：发布Java SE 15版本，增加了Sealed类、文本块、ZGC（Z Garbage Collector）等功能。
16. 2021年3月：发布Java SE 16版本，增加了Records、Pattern Matching for instanceof、Vector API等功能。
17. 2021年9月：发布Java SE 17版本，增加了Sealed类、Pattern Matching for switch、Records、Foreign Linker API等功能。
18. 2023 年 9 月：发布 JavaSE21 版本，这也是一个 LTS 版（Long-Term Support，长期支持版）
19. 2025年9月：发布JavaSE25版本，它也是一个LTS版本。


## 新特性的概述
纵观Java这几年的版本变化，在Java被收入Oracle之后，Java以小步快跑的迭代方式，在功能更新上迈出了更加轻快的步伐。基于时间发布的版本，可以让Java研发团队及时获得开发人员的反馈，因此可以看到最近的Java版本，有很多语法层面简化的特性。同时，Java在支持容器化场景，提供低延迟的GC方面(ZGC等)也取得了巨大的进步。

注意一个新特性的出现通常会经过以下阶段：

1. 孵化器（Incubator）阶段：这是新特性最早的开发和试验阶段，此时新特性只能作为一个单独的模块或库出现，而不会包含在Java SE中。在这个阶段，特性的设计可能会有些不稳定，而且会经常调整和变更。
2. 预览（Preview）阶段：在经过了孵化器阶段的验证和修改后，新特性进入了预览阶段，这是一种在Java SE内部实现的，开发人员可以使用并对其提供反馈的渠道。此时特性可能被包含在Java SE版本中，但是它默认是未开启的，需要通过特定的命令行参数或其他方式进行启用。
3. 正式版（GA）阶段：在经过了预览阶段的反复测试和修复后，新特性最终会在Java SE的稳定版本中发布。此时，特性被默认开启，成为Java SE的一部分，并可以在各个Java应用程序中使用。

需要注意的是，上述阶段并非一成不变，并不是所有JEP（Java Enhancement Proposal：Java增强方案）都需要经过孵化器阶段和预览阶段，这取决于特定的提案和规划。但是，Java SE领导小组通常会遵循这些阶段的流程，以确保新特性可以经过充分的评估和测试，以便能够稳定和可靠地使用在Java应用程序中。

在以下的内容中，我们对Java9到Java21新特性做一个简单的概述。

### Java9新特性
Java9经过4次推迟，历经曲折的Java9最终在2017年9月21日发布，提供了超过150项新功能特性。

- JEP 261: Module System
  - JDK 9 开始引入的一种全新的模块化编程方式。JPMS 的目的是为了更好地支持大型应用程序的开发和维护，同时也可以使 Java 程序在更为动态、可移植和安全的环境下运行。
- JEP 222: jshell: The Java Shell (Read-Eval-Print Loop)
  - 一种交互式的 Java Shell，可以在命令行上快速地进行 Java 代码的编写、验证和执行，从而提高开发者的生产力。
- JEP 213: Milling Project Coin（细化工程改进，该计划旨在引入小型语言特性来提高代码的简洁性和可读性）
  - 在Java 9中，@SafeVarargs注解可以用于一个私有实例方法上。在Java 7和Java 8中，@SafeVarargs注解只能用于静态方法、final实例方法和构造函数。
  - 在Java 9中，可以将效果等同于final变量作为try-with-resources语句块中的资源来使用。在Java 7/8中，try-with-resources语句块中的资源必须是显式的final或事实上的final（即变量在初始化后未被修改），否则编译器会报错。这个限制限制了Java程序员使用try-with-resources语句块的能力，特别是在涉及lambda表达式、匿名类或其他读取外部变量的代码段时。
  - Java 9允许在匿名类实例化时使用钻石操作符(<>)来简化代码，但参数类型必须是具体的、可推导的类型。
  - 从Java9开始，不能使用一个单一的`_`作为标识符了。
  - 从Java9开始，接口中支持定义私有方法。
- JEP 224: HTML5 Javadoc
  - 从Java9开始，javadoc开始支持HTML5的语法。
- JEP 254: Compact Strings
  - 一种新的字符串表示方式，称为紧凑型字符串，以提高Java应用程序的性能和内存利用率。通过String源码得知：`char[]` 变成了 `byte[]`。
- JEP 269: Convenience Factory Methods for Collections
  - 更加方便的创建只读集合：List.of("abc", "def", "xyz");
- JEP 269：对Stream API进行了增强
  - 其中最显著的是引入了四个新的方法，分别是 `takeWhile()`, `dropWhile()`, `ofNullable()` 和 `iterate()`
- JEP 110：一个新的HTTP客户端API，名为HttpClient，它是一种基于异步和事件驱动的方式，更加高效和灵活的HTTP客户端。


### Java10新特性
2018年3月21日，Oracle官方宣布JAVA10正式发布。JAVA10一共定义了109个新特性，其中包含JEP，对开发人员来说，真正的新特性也就一个，还有一些新的API和JVM规范以及Java语言规范上的改动。

- JEP 286：局部变量类型推断
- JEP 296：将 JDK 森林合并到单个存储库中
- JEP 304：垃圾收集器接口
- JEP 307：G1 的并行完整 GC
- JEP 310：应用程序类数据共享
- JEP 312：线程局部握手
- JEP 313：删除本机头生成工具 (javah)
- JEP 314：附加 Unicode 语言标签扩展
- JEP 316：替代内存设备上的堆分配
- JEP 317：基于 Java 的实验性 JIT 编译器
- JEP 319：根证书
- JEP 322：基于时间的发布版本控制


### Java11新特性
2018年9月26日，Oracle官方发布JAVA11。这是Java大版本周期变化后的第一个长期支持版本，官方支持到2026年。

- JEP 181：基于 Nest 的访问控制
- JEP 309：动态类文件常量
- JEP 315：改进 Aarch64 内部函数
- JEP 318：Epsilon：无操作垃圾收集器
- JEP 320：删除 Java EE 和 CORBA 模块
- JEP 321：HTTP 客户端（标准）
- JEP 323：本地变量语法LAMBDA参数
- JEP 324：与Curve25519密钥协商和Curve448
- JEP 327：Unicode的10
- JEP 328：飞行记录器
- JEP 329：ChaCha20和Poly1305加密算法
- JEP 330：启动单文件源代码程序
- JEP 331：低开销堆纹
- JEP 332：传输层安全性 (TLS) 1.3
- JEP 333：ZGC：可扩展的低延迟垃圾收集器（实验性）
- JEP 335：弃用 Nashorn JavaScript 引擎
- JEP 336：弃用 Pack200 工具和 API


### Java12新特性
2019年3月19日，java12正式发布。

- JEP 189：Shenandoah：一个低暂停时间的垃圾收集器（实验性）
- JEP 230：微基准套件
- JEP 325：switch表达式（预览）
- JEP 334：JVM 常量 API
- JEP 340：一个 AArch64 端口
- JEP 341：默认 CDS 档案
- JEP 344：G1 支持可中断的 Mixed GC
- JEP 346：及时从 G1 返回未使用的已提交内存


### Java13新特性
- JEP 350：动态 CDS 档案
- JEP 351：ZGC：取消提交未使用的内存
- JEP 353：重新实现旧的 Socket API
- JEP 354：开关表达式（预览）
- JEP 355：文本块（预览）


### Java14新特性
- JEP 305：instanceof 的模式匹配（预览）
- JEP 343：包装工具（孵化器）
- JEP 345：G1 的 NUMA 感知内存分配
- JEP 349：JFR 事件流
- JEP 352：非易失性映射字节缓冲区
- JEP 358：有用的空指针异常
- JEP 359：记录（预览）
- JEP 361： switch表达式（标准）
- JEP 362：弃用 Solaris 和 SPARC 端口
- JEP 363：删除并发标记清除 (CMS) 垃圾收集器
- JEP 364：macOS 上的 ZGC
- JEP 365：Windows 上的 ZGC
- JEP 366：弃用 ParallelScavenge + SerialOld GC 组合
- JEP 367：删除 Pack200 工具和 API
- JEP 368：文本块（第二次预览）
- JEP 370：外部内存访问 API（孵化器）


### Java15新特性
- JEP 339：爱德华兹曲线数字签名算法 (EdDSA)
- JEP 360：密封类（预览）
- JEP 371：隐藏类
- JEP 372：删除 Nashorn JavaScript 引擎
- JEP 373：重新实现旧版 DatagramSocket API
- JEP 374：禁用和弃用偏向锁定
- JEP 375：instanceof 的模式匹配（第二次预览，无改动）
- JEP 377：ZGC：可扩展的低延迟垃圾收集器（确定正式版）
- JEP 378：文本块（确定正式版）
- JEP 379：Shenandoah：一个低暂停时间的垃圾收集器（确定正式版）
- JEP 381：删除 Solaris 和 SPARC 端口
- JEP 383：外内存访问API（第二孵化器）
- JEP 384：记录（第二次预览）
- JEP 385：弃用 RMI 激活以进行删除


### Java16新特性
- JEP 338：Vector API（孵化器）
- JEP 347：启用 C++14 语言功能
- JEP 357：从 Mercurial 迁移到 Git
- JEP 369：迁移到 GitHub
- JEP 376：ZGC：并发线程栈处理
- JEP 380：Unix 域套接字通道
- JEP 386：Alpine Linux 端口
- JEP 387：弹性元空间
- JEP 388：Windows/AArch64 端口
- JEP 389：外链 API（孵化器）
- JEP 390：基于值的类的警告
- JEP 392：打包工具
- JEP 393：外内存访问API（第三孵化器）
- JEP 394：instanceof 的模式匹配
- JEP 395：记录
- JEP 396：默认情况下强封装JDK内部
- JEP 397：密封类（第二次预览）


### Java17新特性
2021年9月14日，java17正式发布（LTS）。长期支持版，支持到2029年。Oracle 宣布，从JDK17开始，后面的JDK都全部免费提供。

- JEP 306：恢复始终严格的浮点语义
- JEP 356：增强型伪随机数发生器
- JEP 382：新的 macOS 渲染管线
- JEP 391：macOS/AArch64 端口
- JEP 398：弃用 Applet API 以进行删除
- JEP 403：强封装JDK内部
- JEP 406：switch模式匹配（预览）
- JEP 407：删除 RMI 激活
- JEP 409：密封类（正式确定）
- JEP 410：删除实验性 AOT 和 JIT 编译器
- JEP 411：弃用安全管理器以进行删除
- JEP 412：外部函数和内存 API（孵化器）
- JEP 414：Vector API（第二孵化器）
- JEP 415：上下文特定的反序列化过滤器


### Java18新特性
2022年3月22日发布。非长期支持版本。

- JEP 400：从JDK18开始，UTF-8是Java SE API的默认字符集。
- JEP 408：从JDK18开始，引入了jwebserver这样一个简单的WEB服务器，它是一个命令工具。
- JEP 416：使用方法句柄重新实现核心反射
- JEP 418：互联网地址解析SPI
- JEP 413：Java API文档中的代码段（javadoc注释中使用<pre></pre>括起来的代码段会原模原样的生成到帮助文档中）
- JEP 417：Vector API（第三孵化器）
- JEP 419：Foreign Function & Memory API（第二孵化器）
- JEP 420：switch 的模式匹配（第二次预览）
- JEP 421：Object中的finalize()方法被移除


### Java19新特性
2022年9月20日发布。非长期支持的版本。直到 2023 年 3 月它将被 JDK 20 取代。

- JEP 425：虚拟线程（预览版）
  - 一种新的线程模型，即虚拟线程；"虚拟线程" 指的是一种轻量级线程，可以通过 JVM 进行管理和调度，而不需要操作系统进行支持
- JEP 428：结构化并发（孵化器）
  - 一组新的API和规范，用于优化并简化Java程序的并发编程
- JEP 405：Record模式 (预览版)
- JEP 427：switch语句中的模式匹配（第三次预览版）
  - "switch语句中的模式匹配"表示该特性是针对 switch 语句的改进，可以使用模式匹配的方式处理 switch 语句中的分支
- JEP 424：外部函数和内存API（预览版）
  - “外部函数”指的是在Java程序中调用非Java语言编写的函数，比如C/C++函数
  - “内存API”指的是在Java程序中直接操作内存的API
- JEP 426：向量API（第四版孵化器）
  - 一组专用于向量化处理的API，允许在Java程序中轻松高效地执行向量化计算


### Java20新特性
2023年3月21日发布。非长期支持版本。直到 2023 年 9月它将被 JDK 21 取代。

- JEP 432： Record模式(第二次预览版)
- JEP 433： switch的模式匹配 (第四次预览版)
- JEP 434： 外部函数和内存API（第二次预览版）
- JEP 438： 向量API (第五版孵化器)
- JEP 429： Scoped Values (Incubator)
- JEP 436： 虚拟线程(第二次预览版)
- JEP 437： 结构化并发（第二版孵化器）


### Java21新特性
2023年9月19日发布。长期支持版本。

- JEP 440：Record模式（正式确定）
- JEP 441：switch的模式匹配（正式确定）
- JEP 430：String Templates (Preview)
- JEP 443：Unnamed Patterns and Variables (Preview)
- JEP 445：Unnamed Classes and Instance Main Methods (Preview)
- JEP 444：Virtual Threads（正式确定）
- JEP 431：Sequenced Collections（正式确定）
- JEP 452：Key Encapsulation Mechanism API
- JEP 442：Foreign Function & Memory API (Third Preview)
- JEP 453：Structured Concurrency (Preview)
- JEP 446：Scoped Values (Preview)
- JEP 448：Vector API (Sixth Incubator)
- JEP 439：Generational ZGC
- JEP 451：Prepare to Disallow the Dynamic Loading of Agents


## 新语法方面的变化

### jShell命令
jShell命令是Java9引进的新特性，像Python和Scala之类的语言早就有交互式编程环境REPL (read-evaluate-print-loop)，以交互式的方式对语句和表达式进行求值。开发者只需要输入一些代码，就可以在编译前获得对程序的反馈。而之前的Java 版本要想执行代码，必须创建文件、声明类、提供测试方法方可实现。
我们打开DOS命令窗口，然后输入jshell，就能进入交互式编程环境REPL，如下图所示：
![图片1.png](https://cdn.nlark.com/yuque/0/2023/png/21376908/1693815555675-419b4573-2adc-49d9-802e-f1cdd8a11232.png#averageHue=%230a0a0a&clientId=u5039a3e5-4a28-4&from=paste&height=95&id=u5191846f&originHeight=95&originWidth=435&originalType=binary&ratio=1&rotation=0&showTitle=false&size=3194&status=done&style=none&taskId=u2482601c-6fe2-48e5-bb1d-394d37b5297&title=&width=435)
通过jShell命令，我们能够定义一些变量，并执行相关的运算操作，如下图所示：
![图片2.png](https://cdn.nlark.com/yuque/0/2023/png/21376908/1693815610537-81d03d46-682f-4dba-bb4e-cbf4535858cf.png#averageHue=%230b0505&clientId=u5039a3e5-4a28-4&from=paste&height=157&id=u7d18aa94&originHeight=157&originWidth=552&originalType=binary&ratio=1&rotation=0&showTitle=false&size=7031&status=done&style=none&taskId=u0858fee5-3655-43cc-b9fa-7ba770f4bd5&title=&width=552)
通过jShell命令，我们能够定义方法，并执行调用方法的操作，如下图所示：
![图片3.png](https://cdn.nlark.com/yuque/0/2023/png/21376908/1693815641380-7f2b363f-c725-45c8-9d9c-8ae591f24049.png#averageHue=%230f0b0b&clientId=u5039a3e5-4a28-4&from=paste&height=89&id=ua653a84b&originHeight=89&originWidth=640&originalType=binary&ratio=1&rotation=0&showTitle=false&size=5942&status=done&style=none&taskId=u9d6c5a43-a7ab-43c6-b0f1-39d2c377b53&title=&width=640)
想要查看JShell提供的所有指令，则直接输入“/help”即可，如下图所示：
![图片4.png](https://cdn.nlark.com/yuque/0/2023/png/21376908/1693815668710-270b9de8-57c0-4b54-8e16-3d695931c3f9.png#averageHue=%230c0c0c&clientId=u5039a3e5-4a28-4&from=paste&height=673&id=u11aa2377&originHeight=673&originWidth=637&originalType=binary&ratio=1&rotation=0&showTitle=false&size=24015&status=done&style=none&taskId=u99c2527b-e360-4cb2-8e2f-2a68bcaadcc&title=&width=637)
想要查看书写的所有代码，则直接输入“/list”指令即可，如下图所示：
![图片5.png](https://cdn.nlark.com/yuque/0/2023/png/21376908/1693815697610-80f9b33b-0f6b-415a-bf9d-802efa222100.png#averageHue=%23070707&clientId=u5039a3e5-4a28-4&from=paste&height=140&id=u3abe976f&originHeight=140&originWidth=612&originalType=binary&ratio=1&rotation=0&showTitle=false&size=2988&status=done&style=none&taskId=u05961e25-ee6f-430e-b564-48a85e4776b&title=&width=612)
想要查看定义的所有变量，则直接输入“/vars”指令即可，如下图所示：
![图片6.png](https://cdn.nlark.com/yuque/0/2023/png/21376908/1693815723022-6ee3a848-5a44-4544-88a1-a6a0ea4c2a3f.png#averageHue=%23060606&clientId=u5039a3e5-4a28-4&from=paste&height=93&id=ubd0bcd85&originHeight=93&originWidth=328&originalType=binary&ratio=1&rotation=0&showTitle=false&size=1260&status=done&style=none&taskId=u02ba7182-bf8c-48a2-a5b3-3f75e9fdec8&title=&width=328)
想要查看定义的所有方法，则直接输入“/methods”指令即可，如下图所示：
![图片7.png](https://cdn.nlark.com/yuque/0/2023/png/21376908/1693815752017-9e861fd1-b88c-4fd7-9909-5e27b41d78d3.png#averageHue=%230a0a0a&clientId=u5039a3e5-4a28-4&from=paste&height=45&id=u894785f0&originHeight=45&originWidth=294&originalType=binary&ratio=1&rotation=0&showTitle=false&size=768&status=done&style=none&taskId=u523b6e31-8f88-48f9-9aec-c0aa279ab81&title=&width=294)
想要将输入的历史代码片段保存到文件中，就需要使用“ /save”指令，如下图所示：
![图片8.png](https://cdn.nlark.com/yuque/0/2023/png/21376908/1693815779555-09e830d6-40c4-42ca-a762-78a53132c67b.png#averageHue=%23100808&clientId=u5039a3e5-4a28-4&from=paste&height=47&id=u974bf0dd&originHeight=47&originWidth=454&originalType=binary&ratio=1&rotation=0&showTitle=false&size=2596&status=done&style=none&taskId=u080aed12-84fc-44fa-ae72-6d3a0501f84&title=&width=454)


### try-with-resources
众所周知，所有被打开的系统资源，比如流、文件、Socket连接等，都需要被开发者手动关闭，否则随着程序的不断运行，资源泄露将会累积成重大的生产事故。
在Java7以前，我们想要关闭资源就必须的finally代码块中完成。
【示例】Java7之前资源的关闭的方式

```java
public void copyFile1(File srcFile, File destFile) {
    FileInputStream fis = null;
    FileOutputStream fos = null;
    try {
        // 实例化IO流（输入流和输出流）
        fis = new FileInputStream(srcFile);
        fos = new FileOutputStream(destFile);
        // 拷贝文件（存储和读取）
        int len = 0;
        byte[] bytes = new byte[1024];
        while ((len = fis.read(bytes)) != -1) {
            fos.write(bytes, 0, len);
        }
    } catch (FileNotFoundException e) {
        e.printStackTrace();
    } catch (IOException e) {
        e.printStackTrace();
    } finally {
        // 关闭资源
        if (fis != null) {
            try {
                fis.close();
            } catch (IOException e) {
                e.printStackTrace();
            }
        }
        if (fos != null) {
            try {
                fos.close();
            } catch (IOException e) {
                e.printStackTrace();
            }
        }
    }
}
```

Java7及以后关闭资源的正确姿势：try-with-resource，该语法格式为：

```java
try(/*实例化需要关闭资源的对象或引用需要关闭资源的对象*/){
    // 书写可能出现异常的代码
} catch(Exception e) {
    // 处理异常
}
```

使用try-with-resource来自动关闭资源，则需要关闭资源的对象对应的类就必须实现Java.lang.AutoCloseable接口，该接口中提供了一个close()的抽象方法，而自动关闭资源默认调用的就是实现于Java.lang.AutoCloseable接口中的close()方法。
因为FileInputStream类和FileOutputStream类都属于Java.lang.AutoCloseable接口的实现类，因此此处文件拷贝的操作就可以使用try-with-resource来自动关闭资源。
【示例】Java7之后资源的关闭的方式

```java
public void copyFile(File srcFile, File destFile) {
    // 实例化IO流（输入流和输出流）
    try (FileInputStream fis = new FileInputStream(srcFile);
         FileOutputStream fos = new FileOutputStream(destFile)) {
        // 拷贝文件（存储和读取）
        int len = 0;
        byte[] bytes = new byte[1024];
        while ((len = fis.read(bytes)) != -1) {
            fos.write(bytes, 0, len);
        }
    } catch (FileNotFoundException e) {
        e.printStackTrace();
    } catch (IOException e) {
        e.printStackTrace();
    }
}
```

通过try-with-resource来关闭放资源，即使资源很多，代码也可以写的很简洁，如果用Java7之前的方式去关闭资源，那么资源越多，用finally关闭资源时嵌套也就越多。
在Java9之后，为了避免在try后面的小括号中去实例化很多需要关闭资源的对象（复杂），则就可以把需要关闭资源的多个对象在try之前实例化，然后在try后面的小括号中引用需要关闭资源的对象即可，从而提高了代码的可读性。
【示例】Java9之后的使用方式

```java
public void copyFile(File srcFile, File destFile) throws FileNotFoundException {
    // 实例化IO流（输入流和输出流）
    FileInputStream fis = new FileInputStream(srcFile);
    FileOutputStream fos = new FileOutputStream(destFile);
    // 拷贝文件（存储和读取）
    try (fis; fos) {
        int len = 0;
        byte[] bytes = new byte[1024];
        while ((len = fis.read(bytes)) != -1) {
            fos.write(bytes, 0, len);
        }
    } catch (IOException e) {
        e.printStackTrace();
    }
}
```

在以上代码中，表达式中引用了fis和fos，那么在fis和fos就自动变为常量啦，也就意味着在try代码块中不能修改fis和fos的指向，从而保证打开的资源肯定能够关闭。


### 局部变量类型判断
在Java10中，新增了局部变量类型判断。在方法体或代码块中，对于可以在编译期确定的类型，可以使用var来定义。这个特性并不意味着Java是弱类型的语言，仅是提供了更简洁的书写方式。对于编译期无法确定的类型，依然要写清楚类型。
【示例】局部变量类型判断案例

```java
// 使用var来作为变量的引用声明
var num = 123;
var str = "hello world";
var arr = new int[] {11, 22, 33};
var arrayList = new ArrayList<String>();
var calendar = Calendar.getInstance();
// 以下为不可以声明为var的情况
// 1.使用var必须要求变量必须初始化
// var userName;
// 2.不能给变量赋null值
// var userName = null;
// 3.lambda表达式不可以声明为var
// var function = (num) -> Math.round(3.51);
// 4.方法引用不可以声明为var
// var method = System.out :: println;
// 5.数组静态初始化不可以声明为var
// var arr = {"aa", "bb", "cc"};
// 6.类的成员变量不可以使用var类型推断
// 7.所有参数声明，返回值类型，构造方法参数都不可以
```


### instanceof的模式匹配
在JDK14中新增instanceof模式匹配增强(预览)，在JDK16中转正。通过instanceof模式匹配增强，我们就可以直接在模式匹配的括号内声明对应类型的局部变量。
【示例】执行向下转型的操作，从而调用show()方法

```java
/**
 * 以前的代码实现方式
 */
@Test
public void testOld() {
    // 父类引用指向子类对象（多态）
    Animal animal = new Dog();
    // 判断animal是否为Dog类的实例
    if (animal instanceof Dog) {
        // 指向向下转型的操作
        Dog dog = (Dog) animal;
        // 调用Dog类特有的show()方法
        dog.show();
    }
}
/**
 * 使用instanceof模式匹配增强的实现方式
 */
public void testNew() {
    // 父类引用指向子类对象（多态）
    Animal animal = new Dog();
    // 如果animal是Dog类的实例，则向下转型后就命名为dog
    if (animal instanceof Dog dog) {
        // 调用Dog类特有的show()方法
        dog.show();
    }
}
```

【示例】重写equals()，判断成员变量是否相等

```java
public class Tiger {
    String name;
    int age;

    /**
     * 以前的代码实现方式
     */
    /*@Override
    public boolean equals(Object obj) {
        if (this == obj) return true;
        if (obj == null) return false;
        // 如果obj属于Tiger类型，则就执行向下转型的操作
        if (obj instanceof Tiger) {
            // 执行向下转型的操作，恢复对象的实际类型
            Tiger tiger = (Tiger) obj;
            // 如果成员变量都相等，则返回true，否则返回false
            return age == tiger.age && Objects.equals(name, tiger.name);
        }
        // 如果obj不属于Tiger类型，则返回false即可
        return false;
    }*/

    /**
     * 使用instanceof模式匹配增强的实现方式
     */
    @Override
    public boolean equals(Object obj) {
        if (this == obj) return true;
        if (obj == null) return false;
        // 如果obj属于Tiger类型并且成员变量值都相等，那么返回true
        if (obj instanceof Tiger tiger) {
            return age == tiger.age && Objects.equals(name, tiger.name);
        }
        // 如果obj不属于Tiger类型，则返回false即可
        return false;
    }
}
```


### switch表达式
目前switch表达式的问题：

1. 匹配自上而下，若无break，后面的case语句都会执行
2. 不同的case语句定义的变量名不能相同
3. 不能在一个case后面写多个值
4. 整个switch不能作为表达式的返回值

在Java12中对switch表达式做了增强（预览），能够使用更加简洁的代码来解决这些问题。
【示例】switch表达式使用的案例

```java
/**
 * 需求：根据月份输出对应季节的特点
 * 方案一：使用以前的技术来实现
 */
public static void normalSwitch(int month) {
    // 定义一个变量，用于保存季节的特点
    String season;
    // 判断month的取值，从而知晓对应的季节
    switch (month) {
        case 12:
        case 1:
        case 2:
            season = "白雪皑皑";
            break;
        case 3:
        case 4:
        case 5:
            season = "春意盎然";
            break;
        case 6:
        case 7:
        case 8:
            season = "夏日炎炎";
            break;
        case 9:
        case 10:
        case 11:
            season = "秋高气爽";
            break;
        default:
            throw new RuntimeException("没有该月份。。。");
    }
    // 输出month对应季节的特点
    System.out.println(season);
}

/**
 * 需求：根据月份输出对应季节的特点
 * 方案二：使用Java12的新特性来实现
 */
public static void newSwitch(int month) {
    // 判断month的取值，获得对应季节的特点
    String season = switch (month) {
        case 12, 1, 2 -> "白雪皑皑";
        case 3, 4, 5 -> "春意盎然";
        case 6, 7, 8 -> "夏日炎炎";
        case 9, 10, 11 -> "秋高气爽";
        default -> throw new RuntimeException("没有该月份。。。");
    };
    // 输出month对应季节的特点
    System.out.println(season);
}
```

在Java13中，增加关键字yield关键字（预览）， 用于在switch表达式中返回结果。到Java14版本中，Java12和Java13中关于switch的新特性都确定为正式版本。
【示例】switch表达式中的yield关键字

```java
/**
 * 需求：根据月份输出对应季节的特点
 * 演示：Java13版本中新增的yield新特性
 */
public static void yieldSwitch1(int month) {
    // 判断month的取值，获得对应季节的特点
    String season = switch (month) {
        case 12, 1, 2:
            yield "白雪皑皑";
        case 3, 4, 5:
            yield "春意盎然";
        case 6, 7, 8:
            yield "夏日炎炎";
        case 9, 10, 11:
            yield "秋高气爽";
        default:
            throw new RuntimeException("没有该月份。。。");
    };
    // 输出month对应季节的特点
    System.out.println(season);
}
```


### 文本块
在Java语言中，通常需要使用String类型表达HTML，XML，SQL或JSON等格式的字符串，在进行字符串赋值时需要进行转义和连接操作，然后才能编译该代码，这种表达方式难以阅读并且难以维护。
在Java12版本中，新增了文本块（预览）。文本块就是指多行字符串，例如一段格式化后的xml、json等。而有了文本块以后，用户不需要转义，Java能自动搞定。因此，文本块将提高Java程序的可读性和可写性。
【示例】演示文本块的使用

```java
// 使用以前拼接的方式
String html1 = "<html>\n" +
        "      <body>\n" +
        "            <p>Hello， world</p>\n" +
        "      </body>\n" +
        "</html>";
System.out.println(html1);
// 使用文本块的方式
String html2 = """
        <html>
              <body>
                    <p>Hello， world</p>
              </body>
        </html>
        """;
System.out.println(html2);
```

在Java14版本中，针对文本块又新增两个特性（阅览）。1)在一行的结尾增加“\”可以取消改行的换行符；2)可以通过“\s”增加空格。
【示例】演示文本块新增特性

```java
// 取消换行（\）
String json1 = """
        {
            "username":"ande"，\
            "age":18
        }
        """;
System.out.println(json1);
// 添加空格（\s）
String json2 = """
        {
            "username"\s:\s"ande"，
            "age"\s:\s18
        }
        """;
System.out.println(json2);
```


### Record
早在2019年2月份，Java语言架构师Brian Goetz就吐槽了Java语言，他和很多程序员一样抱怨“Java太啰嗦”或有太多的“繁文缛节”，他提到：开发人员想要创建纯数据载体类，通常都必须编写大量低价值、重复的、容易出错的代码。例如：构造方法、getter/setter、equals()、hashCode()以及toString()等。
以至于很多人选择使用IDE的功能来自动生成这些代码。还有一些开发会选择使用一些第三方类库，如Lombok等来生成这些方法，从而会导致了令人吃惊的表现和糟糕的可调试性。
那么，Brian Goetz大神提到的纯数据载体到底指的是什么呢？我们举了一个简单的例子：

```java
public final class Tiger {
    private final String name;
    private final int age;

    public Tiger(String name, int age) {
        this.name = name;
        this.age = age;
    }

    public String name() {
        return name;
    }

    public int age() {
        return age;
    }

    @Override
    public boolean equals(Object obj) {
        if (obj == this) return true;
        if (obj == null || obj.getClass() != this.getClass()) return false;
        var that = (Tiger) obj;
        return Objects.equals(this.name, that.name) &&
                this.age == that.age;
    }

    @Override
    public int hashCode() {
        return Objects.hash(name, age);
    }

    @Override
    public String toString() {
        return "Tiger[" +
                "name=" + name + ", " +
                "age=" + age + ']';
    }
}
```

这里面的Tiger其实就是一个纯数据载体，Tiger类中提供了name和age两个私有常量，并且只提供了全参构造方法和常量名相同的getter方法，以及一些equals、hashCode和toString等方法。于是，BrianGoetz大神提出一种想法，他提到，Java完全可以对于这种纯数据载体通过另外一种方式表示。
在Java14版本中，新增了Record类型。Record是Java的一种新的类型，Record使数据类型变得非常简洁，一般可以帮助我们定义一些简单的用于纯数据载体的实体类。

**Record类的特点：**
状态声明中的每个属性，都是默认采用了private和final修饰，则属性值就不可修改
在Record类中，默认已经重写了Object类提供的equals()，hashcode()，toString()方法
在Record类中，默认提供全参的构造方法，并且提供的getter方法名和属性名保持一致。
Record类采用了final修饰，并且显示的继承于Java.lang.Record类，因此就不能继承别的父类。
【示例】将以上的Tiger类转化为Record类

```java
public record Tiger(String name, int age)  {

}
```

在以上的Record类中，Tiger类默认采用了final修饰，并且显示的继承于Java.lang.Record抽象类，因此Tiger类就不能继承于别的父类。在Tiger类中，提供了name和age两个私有常量，并且还提供了一个public修饰的全参构造方法，提供的getter方法的名字和属性名保持一致，但是并没有提供setter方法。并且，在Tiger类中还重写了Object类提供的equals()，hashcode()，toString()方法。
在Record类中，我们还可以新增静态属性、无参构造方法、成员方法和静态方法，但是创建对象时不能调用无参构造方法，而是通过全参构造方法创建对象的时候，默认就会调用Record类中的无参构造方法。
【示例】在Record类中添加的内容

```java
public record Tiger(String name, int age)  {
    // 新增静态属性
    static double score;
    // 新增无参构造方法
    // 注意：通过全参构造方法创建对象，默认就会调用此处的无参构造方法
    public Tiger {
        System.out.println("无参构造方法");
    }
    // 新增成员方法
    void show() {
        System.out.println("show. ..");
    }
    // 新增静态方法
    static void method() {
        System.out.println("method ...");
    }
}
```


### 密封类
Java中的密封类是一种新的类修饰符，它可以修饰类和接口，可以控制哪些类可以扩展或实现该类或接口。下面是密封类的一些主要用途：

1. 维护类层次结构的封闭性

密封类的一个主要用途是确保类层次结构的封闭性。这意味着，如果您想保护一组类，而不希望其他类继承或实现它们，可以使用密封类来实现这一目标。这对于确保代码的安全性和稳定性非常有用。

1. 预防代码的意外扩展

密封类可以防止其他程序员意外地扩展一个类。在进行类设计时，您可能希望自己或其他程序员只能在特定的类中实现或继承指定的类。在这种情况下，您可以将类标记为“密封”，强制限制其他程序员可以实现或继承的类的范围。

1. 增强代码的可读性和可维护性

密封类可以增强代码的可读性和可维护性。由于密封类明确规定了哪些类可以扩展或实现它，因此其他开发人员可以更清晰地看到代码的结构并理解它们的关系。这使得代码更易于维护和修改。
总之，密封类是一种灵活而有用的类修饰符，可以帮助您维护类的封闭性、预防代码的意外扩展、增强代码的可读性和可维护性。

在Java15版本中，新增了密封类和密封接口（预览）。
使用sealed关键字修饰的类，我们就称之为密封类。密封类必须是一个父类，我们可以使用permits关键字来指定哪些子类可以继承于密封类，并且密封类的子类必须使用sealed、final或non-sealed来修饰。
【示例】密封类的演示

```java
// 密封类必须被继承，并且使用permits来指定哪些子类可以被继承
sealed class Animal permits Dog, Bird, Tiger { }
// 注意：密封类的子类必须使用sealed、final或non-sealed来修饰
// final关键字修饰的子类，则该子类不能被继承
final class Tiger extends Animal { }
// non-sealed修饰的子类，则该子类就是一个普通类
non-sealed class Bird extends Animal { }
// sealed修饰的子类，则该类就必须被继承，否则就会编译错误
sealed class Dog extends Animal {}
non-sealed class SmallDog extends Dog {}
```

使用sealed关键字修饰的接口，我们就称之为密封接口。密封接口必须使用permits关键字来指定实现类或子接口。针对密封接口的实现类，则必须使用sealed、final或non-sealed来修饰；针对密封接口的子接口，则必须使用sealed或non-sealed来修饰。
【示例】密封接口的演示

```java
// 使用sealed修饰的接口，则必须使用permits来指定实现类或子接口。
public sealed interface InterA permits Student, InterB { }
// 密封接口的实现类，必须使用sealed、final或non-sealed来修饰
non-sealed /*final*/ /*sealed*/ class Student implements InterA { }
// 密封接口的子接口，必须使用sealed或non-sealed来修饰
non-sealed /*sealed*/ interface InterB extends InterA {}
```

**sealed与record：**
因为Record类默认采用了final关键字修饰，因此Record类就可以作为密封接口的实现类。
【示例】密封接口和Record类

```java
// 密封接口
sealed interface Flyable permits SuperMan { }
// 让Record类作为密封接口的实现类
record SuperMan(String name, int age) implements Flyable { }
```

---


## API层面的变化

### String存储结构改变
在Java8及其之前，String底层采用char类型数组来存储字符；在Java9及其以后，String底层采用byte类型的数组来存储字符。将char[]转化为byte[]，其目的就是为了节约存储空间。
![图片9.png](https://cdn.nlark.com/yuque/0/2023/png/21376908/1693816288883-1977353d-6a2b-4f8a-8136-ef732f257496.png#averageHue=%23fcfaf8&clientId=u5039a3e5-4a28-4&from=paste&height=431&id=ua4df4a81&originHeight=431&originWidth=746&originalType=binary&ratio=1&rotation=0&showTitle=false&size=33019&status=done&style=none&taskId=u4388d723-406b-43f5-b8a9-0f7797be2ee&title=&width=746)


### String 新增的方法
在Java11版本中，对String类新增了一些方法，新增的方法如下：

```java
// 空格，制表符，换行等都认为是空的
boolean blank = "\t \n".isBlank();
System.out.println(blank); // 输出：true

String source = "\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000www.baidu.com\u3000\u3000\u3000\u3000\u3000";
// 去除“前后”的中文空格
System.out.println(source.strip());
// 去除“开头”的中文空格
System.out.println(source.stripLeading());
// 去除“末尾”的中文空格
System.out.println(source.stripTrailing());

// 把字符串内容重复n份
String repeat = "xixi".repeat(3);
System.out.println(repeat); // 输出：xixixixixixi

// 按照换行来分割字符串，返回的结果是Stream对象
Stream<String> lines = "a\nb\nc\n".lines();
System.out.println(lines.count()); // 输出：3
```

在Java12版本中，对String类新增了一些方法，新增的方法如下：

```java
// 在字符串前面添加n个空格
String result2 = "Java Golang".indent(4);
System.out.println(result2);
```


### 接口支持私有方法
在Java8版本中，接口中支持“公开”的静态方法和公开的默认方法；在Java9版本中，接口中还允许定义“私有”的静态方法和成员方法，但是不能定义私有的默认方法。
【示例】演示接口中的私有静态方法和成员方法

```java
/**
 * 接口（JDK1.9）
 */
public interface Flyable {
    // 私有的静态方法
    private static void staticMethod() {
        System.out.println("static method ...");
    }
    // 私有的成员方法
    private void method() {
        System.out.println("default method ...");
    }
}
```


### 标识符命名的变化
在Java8及其之前，标识符可以独立使用`_`来命名。

```java
String _ = "hello";
System.out.println(_);
```

但是，在Java9中规定`_`不能独立命名标识符了，如果使用就会报错：
![图片10.png](https://cdn.nlark.com/yuque/0/2023/png/21376908/1693816390382-1812ee1d-c55c-4a79-ac8e-219203126225.png#averageHue=%23f8f7f5&clientId=u5039a3e5-4a28-4&from=paste&height=132&id=uc65db047&originHeight=132&originWidth=911&originalType=binary&ratio=1&rotation=0&showTitle=false&size=11105&status=done&style=none&taskId=u5bfb5efa-8086-4933-b572-0d8b7daeeff&title=&width=911)


### 简化编译运行程序
在我们的认知里面，要运行一个Java源代码必须先编译（javac命令），再运行（Java命令），两步执行动作。而在Java 11版本中，通过一个Java命令就直接搞定了。
需要执行的程序：

```java
public class HelloWorld {
    public static void main(String[] args) {
        System.out.println("hello world");
    }
}
```

执行Java命令进行运行，如下图所示：
![图片11.png](https://cdn.nlark.com/yuque/0/2023/png/21376908/1693816436316-0a490d10-91c4-48c7-8958-1e5250d7c0a9.png#averageHue=%230c0c0c&clientId=u5039a3e5-4a28-4&from=paste&height=48&id=u27423f8c&originHeight=48&originWidth=422&originalType=binary&ratio=1&rotation=0&showTitle=false&size=1206&status=done&style=none&taskId=ufe0f2e4a-3da9-4019-b43f-ed80ffd70aa&title=&width=422)


### 创建不可变集合
在Java9版本中，我们可以通过List、Set和Map接口提供的`of(E... elements)`静态方法来创建不可变集合。通过此方式创建的不可变集合，我们不但不能添加或删除元素，并且还不能修改元素。

【示例】创建不可变集合

```java
// 创建不可变List集合
List<Integer> list = List.of(1, 2, 3, 4, 5);
System.out.println(list);
// 创建不可变Set集合
// 注意：如果Set集合中有相同的元素，则就会抛出IllegalArgumentException异常。
Set<Integer> set = Set.of(1, 2, 3, 4, 5, 4);
System.out.println(set);
// 创建不可变Map集合
Map<Integer, String> map = Map.of(123, "武汉", 456, "成都");
System.out.println(map);
```

`Arrays.asList`与`List.of`的区别：
`List.of`：不能向集合中添加或删除元素，也不能修改集合中的元素。
`Arrays.asList`：不能向集合中添加或删除元素，但是可以修改集合中的元素。

【示例】`Arrays.asList`与`List.of`的区别

```java
// 通过Arrays.asList()方法创建不可变集合
List<Integer> list1 = Arrays.asList(1, 2, 3, 4, 5);
// list1.add(6); // 抛出UnsupportedOperationException异常
// list1.remove(2); // 抛出UnsupportedOperationException异常
list1.set(2, 33); // 没有问题
System.out.println(list1); // 输出：[1, 2, 33, 4, 5]

// 通过List.of()方法创建不可变集合
List<Integer> list2 = List.of(1, 2, 3, 4, 5);
// list2.add(6); // 抛出UnsupportedOperationException异常
// list2.remove(2); // 抛出UnsupportedOperationException异常
// list2.set(2, 33); // 抛出UnsupportedOperationException异常
```


### Optional API
在Java8以前，Java程序员操作对象时，为了避免错误引用null造成的空指针异常，往往需要一系列繁杂冗余的判空操作，增加了许多重复代码，降低了代码可读性，于是Java 8引入Optional类，优雅简洁的对null值进行处理，从而避免出现空指针异常（NullPointerException）。
本质上，Optional 类是一个包含有可选值的包装类，这意味着 Optional 类中既可以含有对象也可以为null。

#### 创建Optional对象
使用Optional类提供的of()和ofNullable() 静态方法来创建包含值的Optioanal实例。
如果将null当作参数传进去of()会抛出空指针异常，如果将null当作参数传进去 ofNullable() 就不会抛出空指针异常。
因此当对象可能存在或者不存在，应该使用 ofNullable()方法来创建Optional实例。
【示例】创建一个Optional实例

```java
// 创建一个包含“null”的Optional示例
Optional<Object> optional1 = Optional.ofNullable(null);
// 创建一个包含“对象”的Optional示例
Optional<String> optional2 = Optional.ofNullable("hello");
```


#### Optional类的方法
想要获得Optional实例中包含的值，那么就可以使用以下两个方法来实现。

| **方法名**                    | **描述**                                      |
| -------------------------- | ------------------------------------------- |
| `public T get()`           | 如果值不为null，则直接取出该值；如果值为null，则抛出空指针异常。        |
| `public T orElse(T other)` | 如果值不为null，则直接取出该值；如果值为null，则取出的就是参数other的值。 |

开发中，我们获取Optional中存储的值，一般都是采用`orElse(T other)`方法来实现。
【示例】演示get()方法

```java
// 创建一个包含“null”的Optional示例
Optional<Object> optional1 = Optional.ofNullable(null);
Object obj1 = optional1.get(); // 抛出空指针异常
// 创建一个包含“对象”的Optional示例
Optional<String> optional2 = Optional.ofNullable("hello");
String str = optional2.get();
System.out.println(str); // 输出：hello
```

【示例】演示`orElse(T other)`方法

```java
// 创建一个包含“null”的Optional示例
Optional<Object> optional1 = Optional.ofNullable(null);
Object str1 = optional1.orElse("world");
System.out.println(str1); // 输出：world
// 创建一个包含“对象”的Optional示例
Optional<String> optional2 = Optional.ofNullable("hello");
String str2 = optional2.orElse("world");
System.out.println(str2); // 输出：hello
```


#### Optional的使用案例
需求：有一场商业表演，原计划让“刘亦菲”来表演，如果“刘亦菲”不能参加，则就换“佟丽娅”来表演，该需求的实现代码如下：

```java
// 定义一个变量，用于保存表演者的名字
// String name = "刘亦菲"; // 原计划
String name = null; // 刘亦菲不能参加的情况
// 使用Optional来封装表演者的名字
Optional<String> optional = Optional.ofNullable(name);
// 获得实际参与表演对应人的名字
// 如果name的值为null，则就换为“佟丽娅”参与表演
String finalName = optional.orElse("佟丽娅");
// 输出实际表演者的名字
System.out.println(finalName);
```
