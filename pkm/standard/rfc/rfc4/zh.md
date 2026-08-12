# RFC 4 — Network Timetable（网络时间表）
> **中英对照翻译版本**
> 原文作者：Elmer B. Shapiro（SRI 斯坦福研究院）
> 原文发布日期：1969 年 3 月 24 日
> 类别：信息性文档（Informational）
> 翻译说明：本文件采用「英文原文在上，中文翻译在下」的逐段对照格式。ASCII 拓扑图保持原图，附中文标注。

---

## 文头 · Header

```
Network Working Group                                   Elmer B. Shapiro
Request for Comment: 4                       Stanford Research Institute
Category: Informational                                    24 March 1969
```

> 网络工作组                                            埃尔默·B. 夏皮罗（Elmer B. Shapiro）
> 请求评论：第 4 号                                   斯坦福研究院（Stanford Research Institute）
> 类别：信息性（Informational）                                1969 年 3 月 24 日

---

## 标题 · Network Timetable

```
                           Network Timetable
```

>                           网络时间表

---

## 一、网络联调与设备安装（第 1–4 节）

```
1  (n10) network checkout

2  Installation of communcation gear 8/1/69

   2a  From AT&T and/or BBN need dimensional, power and cabling
   specifications

   2b  Need to establish SRI desired alternate locations so as to
   determine maximum telco cable lengths

   2c  Need to establish location and drops on voice coordination
   circuits

   2d  Need circuit information on voice drops for tie to intercom
   system

   2e  Need to order and install a.c. power (coordinate with 4b)

   2f  See 16

3  Design and construct host-Imp interface 9/1/69

   3a  Need specifications from BBN

   3b  Develop trial design

   3c  Review with system programmers

   3d  Establish final design

   3e  Build and design hardware

   3f  Debug trial software with hardware loop test

4  Imp installation 9/15/69

   4a  from BBN get dimensional, power and cabling specifications

   4b  SRI orders and installs a.c. power (coordinate with 2e)

                                                                [Page 1]
```

> 1  （n10）网络联调（network checkout，即网络验收）
>
> 2  安装通信设备（communication gear）1969/8/1
>
>     2a  需要从 AT&T 和/或 BBN 获取尺寸、供电与布线规格
>
>     2b  需要确定 SRI 期望的备选安装位置，以便测算最长的电话公司（telco）线缆长度
>
>     2c  需要确定语音协调线路上的安装位置与分接点（drops）
>
>     2d  需要语音分接点的线路信息，以便接入内部对讲系统（intercom）
>
>     2e  需要订购并安装交流电源（与 4b 协调进行）
>
>     2f  参见第 16 条
>
> 3  设计并制造主机-IMP 接口（host-Imp interface）1969/9/1
>
>     3a  需要 BBN 提供规格说明
>
>     3b  制定试验性设计方案
>
>     3c  与系统程序员共同评审
>
>     3d  确定最终设计方案
>
>     3e  制造并设计硬件
>
>     3f  用硬件回环测试（hardware loop test）调试试验软件
>
> 4  安装 IMP（接口消息处理机）1969/9/15
>
>     4a  从 BBN 获取尺寸、供电与布线规格
>
>     4b  由 SRI 订购并安装交流电源（与 2e 协调进行）
>
> 【译注】原始文档的「第 1 页」分页标记（[Page 1]）位于第 4 节（4b）之后。

---

## 二、主机-IMP 接口调试（第 5 节）

```
5  Debug host-Imp interface 10/1/69

   5a  Get debug specifiations and procedures from BBN

   5b  Write programs to debug with BBN

       5b1  Transfers of test messages

       5b2  Test procedures for crash and recovery

       5b3  Check message fill and stripping procedures

   5c Try own transfer tests

       5c1  Verify transfers to Imp

       5c2  Verify transfers from Imp

       5c3  Verify transfers looped with Imp

   5d  Work out Imp reload and restart procedures
```

> 5  调试主机-IMP 接口 1969/10/1
>
>     5a  从 BBN 获取调试规格与调试程序（原文 specifiations 为拼写笔误）
>
>     5b  编写与 BBN 联合调试用的程序
>
>         5b1  测试消息的传输
>
>         5b2  崩溃与恢复（crash and recovery）的测试程序
>
>         5b3  检查消息的填充（fill）与剥离（stripping）程序
>
>     5c  尝试自行进行的传输测试
>
>         5c1  验证发往 IMP 的传输
>
>         5c2  验证来自 IMP 的传输
>
>         5c3  验证经 IMP 回环（looped）的传输
>
>     5d  制定 IMP 的重载（reload）与重启（restart）程序

---

## 三、UCLA 与 SRI 之间的测试消息（第 6 节）

```
6  Test messages between UCLA-SRI 10/15/69

   6a  Network configuration
```

```
           SRI  |
                |
                |
                |
                |
                |
                |
                |
           UCLA |
```

> 第 6 节：UCLA 与 SRI 两节点直连拓扑。图中上方标注「SRI」，下方标注「UCLA」，中间的竖线表示两者之间的直连通信链路。

> 6  UCLA 与 SRI 之间的测试消息 1969/10/15
>
>     6a  网络配置（拓扑图见上）

```
   6b  Agree with UCLA on nature of test messages

       6b1  Formats

       6b2  Sequences

       6b3  Checks

       6b4  Test procedures

       6b5  Fault reporting

                                                                [Page 2]
```

>     6b  与 UCLA 就测试消息的性质达成一致
>
>         6b1  格式（Formats）
>
>         6b2  序列（Sequences）
>
>         6b3  校验（Checks）
>
>         6b4  测试程序（Test procedures）
>
>         6b5  故障上报（Fault reporting）
>
> 【译注】原始文档的「第 2 页」分页标记（[Page 2]）位于 6b5 之后。

```
   6c  Test integrity of messages

   6d  Test sequence of delivery

   6e  Measure delays

   6f  Loop with UCLA

   6g  System response to invalid and abnormal conditions

   6h  Lose and restore facilities

       6h1  Communication link

       6h2  Imps

       6h3  Hosts

   6i  Develop net trouble reporting scheme
```

>     6c  测试消息的完整性
>
>     6d  测试消息投递的顺序
>
>     6e  测量时延（delays）
>
>     6f  与 UCLA 进行回环（loop）测试
>
>     6g  系统对无效与异常状况的响应
>
>     6h  设施的丢失与恢复
>
>         6h1  通信链路
>
>         6h2  IMP
>
>         6h3  主机（HOST）
>
>     6i  制定网络故障上报方案

---

## 四、UCSB 与 SRI 之间的测试消息（第 7 节）

```
7  Test messages between UCSB-SRI 11/15/69

   7a  Network configuration
```

```
           SRI .
              |  .
              |   .
              |     .
              |       .
              |         .
              ------------
           UCLA           UCSB
```

> 第 7 节：UCLA、SRI 与 UCSB 三节点三角形拓扑。图中上方为 SRI，左下为 UCLA、右下为 UCSB；SRI 与 UCLA、UCSB 之间以虚线相连，底部的横线为 UCLA 与 UCSB 之间的链路，共同构成三角环。

> 7  UCSB 与 SRI 之间的测试消息 1969/11/15
>
>     7a  网络配置（拓扑图见上）

```
   7b  All of 6

   7c  Load network for alternate routing to be effective

   7d  Develop voice coordination scheme

       7d1  Three way conference

       7d2  Design and build conference gear

       7d3  Deliver conference gear to UCLA and UCSB

   7e  Route messages around ring

       7e1  Via Imps

                                                                [Page 3]
```

>     7b  第 6 节的全部内容
>
>     7c  对网络施加负载，使备用路由（alternate routing）能够实际发挥作用
>
>     7d  制定语音协调方案
>
>         7d1  三方会议（Three way conference）
>
>         7d2  设计并制造会议设备
>
>         7d3  将会议设备交付给 UCLA 与 UCSB
>
>     7e  绕环（ring）路由消息
>
>         7e1  经由 IMP
>
> 【译注】原始文档的「第 3 页」分页标记（[Page 3]）位于 7e1 之后。

```
       7e2  Via hosts

       7e3  Six tests

         7e3a  UCLA-I, UCSB-I

         7e3b  UCLA-H, UCSB-I

         7e3c  UCLA-H, UCSB-H

         7e3d  UCSB-I, UCLA-I

         7e3e  UCSB-H, UCLA-I

         7e3f  UCSB-H, UCLA-H
```

>         7e2  经由主机（HOST）
>
>         7e3  六项测试
>
>             7e3a  UCLA-I、UCSB-I（UCLA 侧经 IMP 接入，UCSB 侧经 IMP 接入，UCLA → UCSB 方向）
>
>             7e3b  UCLA-H、UCSB-I（UCLA 侧经主机接入，UCSB 侧经 IMP 接入，UCLA → UCSB 方向）
>
>             7e3c  UCLA-H、UCSB-H（UCLA 侧经主机接入，UCSB 侧经主机接入，UCLA → UCSB 方向）
>
>             7e3d  UCSB-I、UCLA-I（接入组合同 7e3a，方向相反，UCSB → UCLA）
>
>             7e3e  UCSB-H、UCLA-I（接入组合同 7e3b，方向相反，UCSB → UCLA）
>
>             7e3f  UCSB-H、UCLA-H（接入组合同 7e3c，方向相反，UCSB → UCLA）
>
> 【译注】7e3a–f 中的 I 指经 IMP 接入/传输，H 指经主机（HOST）接入/传输。六项测试是三种接入组合在两个传输方向上的完整遍历。

---

## 五、UTAH 与 SRI 之间的测试消息（第 8 节）

```
8  Test messges between UTAH-SRI 12/15/69

   8a  Network configuration
```

```
           SRI .----------------UTAH
               | .
               |   .
               |     .
               |       .
               |         .
               |           .
               |             .
               |               .
           UCLA-----------------UCSB
```

> 第 8 节：UCLA、SRI、UCSB、UTAH 四节点环形拓扑。图中 SRI 与 UTAH 之间、UCLA 与 UCSB 之间为实线直连；SRI 与 UCLA 之间、UCSB 与 UTAH 之间为虚线，共同构成完整的四节点环。

> 8  犹他大学（UTAH）与 SRI 之间的测试消息 1969/12/15
>
>     8a  网络配置（拓扑图见上）

```
   8b  Selected group of previous test

       8b1  All of 6

       8b2  7b

   8c  Expand voice coordination scheme

       8c1  UTAH has access to UCLA and UCSB via SRI

       8c2  with BBN and ARPA
```

>     8b  此前测试的精选子集
>
>         8b1  第 6 节的全部内容
>
>         8b2  第 7b 项
>
>     8c  扩展语音协调方案
>
>         8c1  犹他大学（UTAH）经由 SRI 与 UCLA、UCSB 建立语音通道
>
>         8c2  与 BBN 和 ARPA 的语音通道

---

## 六、运行简单的 TTY 系统（第 9 节）

```
9  Run simple TTY systems

   9a  Single user access

       9a1  On a serving host

         9a1a  A to B

       9a2  From a using host

         9a2a  A to B

                                                                [Page 4]
```

> 9  运行简单的 TTY（电传打字机）系统
>
>     9a  单用户接入
>
>         9a1  在服务主机（serving host）上
>
>             9a1a  A 到 B（A：使用终端/用户，B：服务主机）
>
>         9a2  从使用主机（using host）接入
>
>             9a2a  A 到 B
>
> 【译注】原始文档的「第 4 页」分页标记（[Page 4]）位于 9a2a 之后。

```
   9b Multiple user access

       9b1  On a serving host

         9b1a  A,C to B

       9b2  From a using host

         9b2a  A,A to B

       9b3  Various combinations

   9c  Login, logout, in and out of subsystems

   9d  Handling of error messages, crashes, recoveries

   9e  Establish message formats

   9f  Establish protocols

   9g  File storage and retrieval

   9h  Need user's guides for each site

   9i  Need to establish usage schedules

   9j  Need to set user names

   9k  Design and build comm exec or its equivalent
```

>     9b  多用户接入
>
>         9b1  在服务主机上
>
>             9b1a  A、C 到 B（用户 A 与 C 同时连到服务主机 B）
>
>         9b2  从使用主机接入
>
>             9b2a  A、A 到 B（用户 A 的两个终端同时连到 B）
>
>         9b3  各种组合
>
>     9c  登录、登出，进出子系统
>
>     9d  错误消息、崩溃与恢复的处理
>
>     9e  确定消息格式
>
>     9f  确定协议（protocols）
>
>     9g  文件存储与检索
>
>     9h  各站点需要编制用户指南
>
>     9i  需要确定使用时间表
>
>     9j  需要设置用户名
>
>     9k  设计并实现通信执行程序（comm exec，通信管理程序）或其等效物

---

## 七、运行简单的打字机系统与任意终端（第 10–13 节）

```
10  Run simple typewriter systems

   10a  Same as 9c - 9g

   10b  How define when in half or full duplex mode

   10c  How to set "break" characters

11  Run arbitrary terminals without local feedback

                                                                [Page 5]
```

> 10  运行简单的打字机（typewriter）系统
>
>     10a  同第 9 节 9c – 9g 项
>
>     10b  如何定义半双工/全双工模式
>
>     10c  如何设置「打断（break）」字符
>
> 11  运行无本地回显（local feedback）的任意终端
>
> 【译注】原始文档的「第 5 页」分页标记（[Page 5]）位于第 11 节之后。

```
12  Run arbitrary terminals

13  Move files
```

> 12  运行任意终端
>
> 13  传输文件

---

## 八、开发调试技术（第 14 节）

```
14  Develop debugging techniques

   14a  Fault detection

       14a1  Conformance to manual

       14a2  "Reasonableness" of result

       14a3  Comparison with alternate form of use

   14b  Cause localization

       14b1  Comm-Imp complex

       14b2  Serving host

       14b3  Using host

       14b3  Try other programs

       14b5  Monitor subsystem via "link" procedures, where possible

         14b5a  Use dialup Dataphone

         14b5b  Use voice coordination channel

       14b6  Move canned messages

   14c  Cause determination

   14d  Cause correction

         [ This RFC was put into machine readable form for entry ]
          [ into the online RFC archives by David Capshaw 11/97 ]

                                                                [Page 6]
```

> 14  开发调试技术
>
>     14a  故障检测（Fault detection）
>
>         14a1  与手册（manual）的一致性
>
>         14a2  结果的「合理性」（"Reasonableness"）
>
>         14a3  与替代使用方式的比较
>
>     14b  原因定位（Cause localization）
>
>         14b1  通信-IMP 综合体（Comm-Imp complex）
>
>         14b2  服务主机
>
>         14b3  使用主机（Using host）
>
>         14b3  尝试其他程序（Try other programs）
>
>         【译注】原文此处存在编号笔误：14b3 出现了两次（第一次对应「使用主机 Using host」，第二次对应「尝试其他程序 Try other programs」），此处按原文保留；按编号顺序推断，第二个 14b3 应为 14b4（后文亦直接从 14b3 跳至 14b5）。
>
>         14b5  在可行的情况下，通过「链路（link）」规程监视子系统
>
>             14b5a  使用拨号数据电话（dialup Dataphone，AT&T 的拨号数据线路服务）
>
>             14b5b  使用语音协调信道
>
>         14b6  传输预置消息（canned messages，预先准备好的消息）
>
>     14c  原因判定（Cause determination）
>
>     14d  原因纠正（Cause correction）
>
> 【译注】本节的调试方法论流程为：故障检测 → 原因定位 → 原因判定 → 原因纠正。
>
> 【译注】归档说明：原文最末两行注明，本 RFC 由 David Capshaw 于 1997 年 11 月转成机器可读形式，录入在线 RFC 档案库。
>
> 【译注】原始文档的「第 6 页」分页标记（[Page 6]）位于文档最末。

---

## 附录 · 历史背景（译注）

> 【译注】本表是 ARPANET 最初的正式施工进度表：8/1 安装通信设备 → 9/1 制造主机-IMP 接口 → 9/15 安装 IMP → 10/15 UCLA 与 SRI 首次互测 → 11/15 UCSB 加入 → 12/15 UTAH 加入，之后运行 TTY 系统、传输文件、开发调试技术。计划与真实历史大体吻合：第一条 ARPANET 消息实际于 1969 年 10 月 29 日由 UCLA 发出（比计划中的 10/15 首测晚约两周）；犹他大学（UTAH）于同年 12 月入网，UCLA、SRI、UCSB、UTAH 四节点构成的 ARPANET 最初网络正式运转，这份时间表大体兑现。
