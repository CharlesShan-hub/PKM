# Java

## 内容

### 基础语法

  > * 基础语法阶段主要按照网课[【零基础 快速学Java】韩顺平 零基础30天学会Java](https://www.bilibili.com/video/BV1fh411y7R8/)学记记录
  > * 本套Java课程为三个阶段，涵盖了Java基础的方方面面。
  > * 第一阶段:建立编程思想(包括:基本语法、数组、排序和查找、面向对象编程、零钱通、房屋出租系统、迷宫、八皇后、汉诺塔 )
  > * 第二阶段:提升编程能力(包括: 枚举和注解、Exception、常用类、集合、泛型、线程、IO流、坦克大战) 
  > * 第三阶段: 增强分析需求，代码实现能力(包括: 网络编程、反射、Mysql、JDBC和连接池、正则表达式、Java8 Java11 新特性、马踏棋盘、满汉楼、多用户通信系统)

* 第 1 章：概述
    * 0：目录和概述，介绍主要内容
    * 1：（可跳过）一小段话
    * 2：（可跳过）就业方向：EE 、大数据、安卓
    * 3：（可跳过）开发场景：SSM（Spring 、 SpringMVC 、 Mybatis）
    * 4：（可跳过）应用领域：后端、客户端、嵌入式
    * 5：（可跳过）之前的PPT，总结成了笔记
* 第 2 章：[[notes/basic/stage1/背景介绍|背景介绍]]，[第一个程序](notes/basic/stage1/第一个程序.md)，[反思总结](notes/basic/stage1/反思总结.md)，[[notes/basic/stage1/Dos指令|Dos指令]]
    * 6：（可跳过）什么是程序，Hello World
    * 7：（可跳过）Java 历史：sun、gosling、1995、oak、Oracle；SE、EE、ME
    * 8：（可跳过）Java 特性：OOP、GC 强类型、跨平台、解释型语言
    * 9：（可跳过）软件安装（初学者推荐 sublime，熟悉语法）
    * 10：JRE、JVM、JDK
    * 11：（可跳过）windows 操作常识
    * 12~15：（可跳过）不同系统 Java 安装、配环境变量
    * 16：Hello World的编写和运行，中文用 GBK 编码
    * 17：（可跳过）运行机制：.java到.class到运行的流程
    * 18：开发细节：一个.java文件里边只能有一个 public 类
    * 19：（可跳过）反思总结
    * 20：转义字符：`\r`是回到开头
    * 21：（可跳过）易犯错误
    * 22：（可跳过）注释的重要性
    * 23：（可跳过）单行注释、多行注释
    * 24：文档注释（javadoc）
    * 25：（可跳过）代码规范
    * 26：（可跳过）Dos指令
    * 27：（可跳过）相对路径、绝对路径
    * 28：（可跳过）Dos：dir 、cd（切换盘）
    * 29：（可跳过）Dos：tree 、cls 
    * 30：（可跳过）Dos：exit 、 md 、 rd 、 del 、 type 、 copy、 echo、 move
    * 31~32：（可跳过）[[notes/basic/stage1/第一章作业|第一章作业]]
    * 33：（可跳过）内容梳理
* 第 3 章：[[notes/basic/stage1/变量与数据类型|变量与数据类型]]，[[notes/basic/stage1/Java文档|Java文档]]，[[notes/basic/stage1/包|包]]，[编码](notes/basic/stage1/编码.md)
	* 34：（可跳过）变量原理：类型、名称、值
	* 35：（可跳过）变量概念：声明、赋值
	* 36：（可跳过）变量入门：int 、 double 、char 、 String 初识
	* 37：变量细节：没有遮蔽
	* 38：加号：数加数，字符串拼接字符串，数字变字符串拼接字符串
	* 39：（重点）数据类型。 char 2 字节
	* 40：（可跳过）整数
	* 41：整数细节：整形字面量默认是 int，long 要手动加 L/l；不同平台字节数一样
	* 42：（可跳过）浮点类型：float 、 double
	* 43：浮点数细节：字面量默认是 double
	* 44：浮点数细节： 0.3 陷阱，不要对小数做相等判断
	* 45：JavaAPI文档：[[notes/basic/stage1/Java文档|Java文档]]，[[notes/basic/stage1/包|包]]
	* 46：（可跳过）char 可以放汉字，一些 sublime 快捷键
	* 47：字符型细节：ascii 码，char 就是数字 可以直接运算
	* 48：字符类型的本质：还是char 就是数字，[编码](notes/basic/stage1/编码.md)
	* 49：（可跳过）复习编码
	* 50：（可跳过）布尔类型，不能用0 或非 0 代表布尔
	* 51：（重点）自动类型转换
	* 52～56：强制类型转换+练习
	* 57～58：基础数据类型与字符串相互转换，包装类
	* 59～60：[[notes/basic/stage1/第二章作业|第二章作业]]
	* 61：（可跳过）章末总结
* 第 4 章：[[notes/basic/stage1/运算符|运算符]]，[[notes/basic/stage1/标识符规则与规范|标识符规则与规范]]，[[notes/basic/stage1/键盘输入|键盘输入]]，[[notes/basic/stage1/进制|进制]]
	* 62：（可跳过）运算符简介
	* 63：除法、取摸、++
	* 64：（重点）i++面试题
	* 65～67：（可跳过）运算符案例
	* 68～69：（可跳过）关系运算符
	* 70：（可跳过）逻辑运算符 = 短路 + 逻辑
	* 71：短路与逻辑与
	* 72：短路或逻辑或
	* 73：逻辑非与逻辑异或
	* 74：逻辑运算符练习
	* 75～76：赋值运算符，（内含强制转换）
	* 77～79：三元运算符，（内涵自动转换）
	* 80：运算符优先级（不用特别的背）
	* 81~83：（可跳过）标识符规则和规范：[[notes/basic/stage1/标识符规则与规范|标识符规则与规范]]
	* 84：（可跳过）关键字、保留字
	* 85：（重要）键盘输入：[[notes/basic/stage1/键盘输入|键盘输入]]
	* 86：（重要）进制：[[notes/basic/stage1/进制|进制]]
	* 87～89：（可跳过）二、八、十六进制转十进制
	* 90～92：（可跳过）十进制转二、八、十六进制
	* 93～94：（可跳过）二进制转八、十六进制
	* 95～96：（可跳过）八、十六进制转二进制
	* 97：位运算思考题
	* 98：原码、补码、反码
	* 99～100：（重点）位运算详解
	* 101：[[notes/basic/stage1/第三章作业|第三章作业]]
	* 102：第三章总结
* 第 5 章：[控制结构](notes/basic/stage1/控制结构.md) 
	* 103：顺序控制
	* 104～113：if 与 if-else，级联 if else，嵌套分支
	* 114～116：switch基础用法和案例
	* 117：switch 细节
	* 118
	* 119
	* 120
	* 121
	* 122
	* 123
	* 124
	* 125
	* 126
	* 127
	* 128
	* 129
	* 130
	* 131
	* 132
	* 133
	* 134
	* 135
	* 136
	* 137
	* 138
	* 139
	* 140
	* 141
	* 142
	* 143
	* 144
	* 145
	* 146
	* 147
	* 148
	* 149
	* 150
	* 151
	* 152
	* 153



## Old Content

  * |                         第一阶段                          |               建立编程思想                |                                                              |
    | :-------------------------------------------------------: | :---------------------------------------: | :----------------------------------------------------------: |
    |                           Part1                           |                零散知识点                 |                                                              |
    |         [反思总结](notes/basic/stage1/反思总结.md)         | [背景介绍](notes/basic/stage1/背景介绍.md) |          [Java文档](notes/basic/stage1/Java文档.md)           |
    |          [Dos指令](notes/basic/stage1/Dos指令.md)          |     [编码](notes/basic/stage1/编码.md)     |                                                              |
    |                           Part2                           |                 基础语法                  |                                                              |
    |       [第一个程序](notes/basic/stage1/第一个程序.md)       |     [变量与数据类型](notes/basic/stage1/变量与数据类型.md)     |            [运算符](notes/basic/stage1/运算符.md)             |
    | [标识符规则与规范](notes/basic/stage1/标识符规则与规范.md) | [键盘输入](notes/basic/stage1/键盘输入.md) |              [进制](notes/basic/stage1/进制.md)               |
    |         [控制结构](notes/basic/stage1/控制结构.md)         |     [数组](notes/basic/stage1/数组.md)     |              [排序](notes/basic/stage1/排序.md)               |
    |             [查找](notes/basic/stage1/排序.md)             | [递归案例](notes/basic/stage1/递归案例.md) |                                                              |
    |                           Part3                           |                 类与对象                  |                                                              |
    |         [类与对象的引出](notes/basic/stage1/类与对象的引出.md)         | [属性与成员方法](notes/basic/stage1/属性与成员方法.md) | [构造器与this](notes/basic/stage1/构造器与this.md) |
    |  [面向对象基础案例](notes/basic/stage1/面向对象基础案例.md)  |       [包](notes/basic/stage1/包.md)       |         [访问修饰符](notes/basic/stage1/访问修饰符.md)          |
    |              [封装](notes/basic/stage1/封装.md)              |      [继承](notes/basic/stage1/继承.md)      |               [super](notes/basic/stage1/super.md)               |
    | [多态](notes/basic/stage1/多态.md) | [Object](notes/basic/stage1/Object.md) |  |
    
  * | 第二阶段 | 提升编程能力 |      |
    | :------: | :----------: | :--: |
    |          |              |      |
    |          |              |      |
    |          |              |      |
    |          |              |      |
  
  * | 第三阶段 | 增强分析需求 |      |
    | :------: | :----------: | :--: |
    |          |              |      |
    |          |              |      |
    |          |              |      |
    |          |              |      |

## 资源

* [Java 全栈知识体系](https://pdai.tech/)