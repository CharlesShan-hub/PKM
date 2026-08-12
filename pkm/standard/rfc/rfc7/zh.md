# RFC 7 — Host-IMP Interface（主机-IMP 接口）
> **中英对照翻译版本**
> 原文作者：G. Deloche（UCLA 加州大学洛杉矶分校）
> 原文发布日期：1969 年 5 月
> NIC 编号：4693
> 翻译说明：本文件采用「英文原文在上，中文翻译在下」的逐段对照格式。ASCII 架构图保持原图，附中文标注；原文 (unreadable)（无法辨认）处照实保留并标注。

---

## 文头 · Header

```
Network Working Group                                         G. Deloche
Request for Comment: 7           University of California at Los Angeles
NIC: 4693                                                       May 1969
```

> 网络工作组                                               G. 德洛什（G. Deloche）
> 请求评论：第 7 号                              加州大学洛杉矶分校
> NIC 编号：4693                                            1969 年 5 月

```
                           Host-Imp Interface
```

>                             主机-IMP 接口（Host-IMP Interface）

```
      G. Deloche      -->  Prof. J. Estrin
                           Prof. L. Kleinrock
                           Prof. B Bussel
                           D. Mandell
                           S. Crocker
                           L. Bonamy
```

>      G. 德洛什        -->  抄送：J. Estrin 教授
>                            L. Kleinrock 教授
>                            B. Bussel 教授
>                            D. Mandell
>                            S. Crocker
>                            L. Bonamy

【译注】这是 Deloche 写完文档后的"抄送列表"（相当于今天的 @mentions）——收件人包括 UCLA 的教授们和 Crocker。

```
   Object: Arpa Network - Specification Outlines for Host-IMP (HI)
   Interface Programs.
```

> 目的：ARPANET —— 主机-IMP（HI）接口程序的规格大纲。

```
                                  Outline

   I.  Introduction

   II.  Scope of the software organization.
           II-1    Network program
           II-2    Handler program

   III.  Questions
```

> **大纲**
>
> I. 引言
>
> II. 软件组织的范围
> > II-1 网络程序（Network program）
> > II-2 处理器程序（Handler program）
>
> III. 问题

```
   [The original of RFC 7 was hand-written, and only partially illegible
   copies exist.  RFC 7 was later typed int NLS by the Augmentation
   Research Center (ARC) at SRI.  The following is the best
   reconstruction we could do.  RFC Editor.]
```

> 【RFC 编辑注】RFC 7 的原稿是**手写的**，仅存部分无法辨认的副本。后来由 SRI 的扩展研究中心（ARC，Augmentation Research Center）用 NLS 系统重新录入（原文 "int" 为 "into" 的笔误）。以下是我们能做到的最佳重建版本。

---

## I. 引言 · Introduction

```
   This paper is concerned with the preliminary software design of the
   Host IMP interface.  Its main purpose is on the one hand to define
   functions that will be implemented, and on the other hand to provide
   a base for discussions and ...(unreadable).
```

> 本文关注主机-IMP 接口的**初步软件设计**。其主要目的：一方面定义将要实现的功能，另一方面为讨论提供基础……（无法辨认）。

```
   This study is based upon a study of the BBN Report No. 763.
```

> 本研究的依据是 BBN 报告第 763 号。

---

## II. 软件组织的范围 · Scope of the Software Organization

```
   The system is based upon two main programs: the Handler program that
   drives the channel hardware unit, and the Network program which
   carries out the user's transmission requests.
```

> 系统基于两个主要程序：**处理器程序（Handler program）**——驱动通道硬件单元；**网络程序（Network program）**——承载用户的传输请求。

```
   As the communication is full duplex, each of these programs can be
   viewed as divided into two parts: one is concerned with the output
   data, the other with the input. (See Fig. 1)
```

> 由于通信是**全双工**（full duplex）的，这两个程序都可以看作各自分为两部分：一部分负责输出数据，另一部分负责输入。（见图 1）

```
   These two programs exchange data through a pool of buffers, and
   logical information through an interface table.
```

> 这两个程序通过**缓冲池（pool of buffers）**交换数据，通过**接口表（interface table）**交换逻辑信息。

```
   In the following we only focus on the output part of each program
   (See Fig. 2).  The input part would be very similar.
```

> 下文我们只关注每个程序的输出部分（见图 2）。输入部分与之非常相似。

---

## II-1. 网络程序 · Network Program

```
II-1-1. Multiplex function.
```

> **II-1-1 多路复用功能（Multiplex Function）**

```
   This program multiplexes the outgoing messages (and distributes the
   incoming messages).  The multiplexing consists in stacking up all the
   user's (or caller, or party) requests and filling up the pool of
   buffers so as to keep the handler busy emitting.
```

> 该程序对发出去的消息进行**多路复用**（并对收到的消息进行分发）。多路复用就是把所有用户（或调用者 caller、参与方 party）的请求堆叠起来，把缓冲池填满，以保持处理器程序一直忙于发送（keep the handler busy emitting）。

```
   Multiplexing (and distribution) is based on the link identification
   numbers.  (Link = logical connection between two users).  The
   multiplexing problem is closely related to the interface between a
   user's program and the network program, that is in
   fact...(unreadable) operating system (See below: Questions).
```

> 多路复用（及分发）基于**链路标识号**（Link = 两个用户之间的逻辑连接）。多路复用问题与用户程序和网络程序之间的接口密切相关，实际上就是……（无法辨认）操作系统（见下文：问题）。

```
II-1-2.  Output message processing.
```

> **II-1-2 输出消息处理（Output Message Processing）**

```
   When a user's program wants to send out text it should indicate the
   following information (through a macro, or as call parameters): text
   location, text length in bytes, and destination.
```

> 当用户程序想要发送文本时，应说明以下信息（通过宏，或作为调用参数）：**文本位置、文本长度（以字节计）、目的地**。

```
   Using these data the Network program:

      *  prepares a 16 bit Host heading (1 bit: trace, 2 bits: spares, 8
         bits: link identification no., 5 bits: destination host)

      *  inserts a 16 bits marking between the header and the text so as
         to start the text at a word boundary.  This marking consists of
         a one preceding the first bit of the text and, in turn,
         preceded by fifteen zeros to fill up the gap.

      *  checks the length of the user's text - if it exceeds 1006 bytes

          +-                                                     -+
          |8080 (max host message length) - 32 (heading + marking)|
          |-------------------------------------------------------|
          |                8 (byte = 8 bits)                      |
          +-                                                     -+

   the program breaks down the text into a sequence of messages whose
   maximum length is 1006 bytes - Each of these messages is preceded by
   a heading as explained above.
```

> 利用这些数据，网络程序会：
>
> ① 构建一个 **16 位的主机消息头**（1 位：追踪 trace；2 位：备用 spares；8 位：链路标识号；5 位：目的主机）；
>
> ② 在消息头与正文之间插入一个 **16 位标记**，使正文从**字边界（word boundary）**开始。这个标记由正文第一个位之前的一个 1 构成，其前再补 15 个 0 以填满空隙；
>
> ③ 检查用户文本的长度——如果超过 **1006 字节**（如上计算式：8080 最大主机消息长度 − 32 头部与标记，再除以 8 位/字节），程序就把文本拆分成一系列最大长度为 1006 字节的消息——每条消息前面都按上述方式加一个消息头。

```
   Remark: in that case one of the heading space bits could be used for
   indicating that several messages belong to the same text.
```

> 备注：这种情况下，消息头中某个备用位可以用来指示"多条消息属于同一段文本"。

```
      *  _transcodes_ the EBCDIC characters constituting the messages
         into ASCII characters.

      *  _fills_ the buffers of the pool with the content of the
         messages.

      *  _updates_ the content of the interface table and moves the
         filling pointers (see below).
```

> ④ 将构成消息的 **EBCDIC 字符转码（transcodes）为 ASCII 字符**；
>
> ⑤ 用消息的内容**填满**缓冲池中的缓冲；
>
> ⑥ **更新**接口表的内容并移动填充指针（见下文）。

---

## II-2. 处理器程序 · Handler Program

```
   This program is initiated either by the network program, or by the
   I/O interrupt.
```

> 这个程序由网络程序或 I/O 中断来启动。

```
   This program will be very short.  It will be coded in master mode
   (privileged instructions) and should be integrated in the I/O
   supervisor of the operating system.
```

> 这个程序会**非常短**。它将用**主模式（master mode，特权指令）**编写，并应集成到操作系统的 I/O 监控程序（supervisor）中。

```
   This program:

      *  _controls_ the channel hardware unit.  It initiates the
         emission, eventually provides data chaining between the
         buffers, tests the different device status upon receiving an
         interrupt.

      *  _empties_ the buffers that are filled up by the network
         program.

      *  _explores_ and _updates_ the interface table (see below).

      *  can eventually insure a control transmission procedure with the
         IMP (See Questions).
```

> 这个程序：
>
> ① **控制**通道硬件单元：发起发送、在缓冲之间提供数据链式传输（data chaining）、收到中断时测试各种设备状态；
>
> ② **清空**网络程序填好的缓冲；
>
> ③ **探查并更新**接口表（见下文）；
>
> ④ 最终可以与 IMP 之间保证一套控制传输规程（见"问题"部分）。

【译注】"数据链式传输（data chaining）"——硬件级的 DMA 链式缓冲，把多个不连续的内存块串起来连续发送，正是今天 scatter-gather I/O 的前身。

---

## II-3. 缓冲与接口表 · Buffers and Interface Table

```
II-3-1  Buffers.
```

> **II-3-1 缓冲（Buffers）**

```
   They should be large enough for containing the maximum host message
   text + heading and marking (1006 + 4 = 1010 bytes).
```

> 它们应足够大，能容纳最大主机消息的正文 + 消息头与标记（1006 + 4 = **1010 字节**）。

```
   Consequently the buffer size could be chosen equal to 256 words (1024
   bytes).  As for the buffer number it will determine the link
   utilization frequency -
```

> 因此缓冲大小可选为 **256 字（1024 字节）**。至于缓冲的数量，它将决定链路的利用率。

```
II-3-2  Interface table.
```

> **II-3-2 接口表（Interface Table）**

```
   It is through this table that the network program informs the handler
   with the location and length of the emitting data.
```

> 网络程序正是通过这张表，把待发送数据的位置和长度告知处理器程序。

```
   This table could be a ring table with 2 pointers: one for filling,
   the other for extracting.  They are respectively updated by the
   network and the handler program.
```

> 这张表可以是一张**环形表（ring table），带两个指针**：一个用于填充（filling）、一个用于提取（extracting）。它们分别由网络程序和处理器程序更新。

```
                      [Length] of the message
                           contained
                           in the buffer
                               ^
                               |
           +--------------+----------+
           | Buffer addr. | nb bytes |
           +--------------+----------+
           |              |          | <== Filling pointer
           +--------------+----------+         |
           |                         |         V
           |                         |
           //                        //
           |                         |
           |                         |
           |                         |
           +--------------+----------+
           | Buffer addr. | nb bytes | <== eEtracting pointer
           +--------------+----------+         |
           | Buffer addr. | nb bytes |         V
           +--------------+----------+
```

> 上图：接口表（环形表）——每行记录一块缓冲的地址（Buffer addr.）和其中的字节数（nb bytes，即消息长度）。**填充指针（Filling pointer）**由网络程序向下移动，**提取指针（Extracting pointer，原文拼作 eEtracting）**由处理器程序向下移动。

【译注】这就是教科书级的**环形缓冲 + 双指针生产者-消费者队列**：生产方（网络程序）填、消费方（处理器程序）取，两个指针各自推进，互不阻塞。

---

## III. 问题 · Questions

```
III-1.  Why is there not a simple control procedure between the HOST and
        the IMP?  What happens if a message, issued from the HOST,
        reaches the IMP with an error due to the transmission?

   From the BBN specifications it appears that this error will be
   transmitted as far [as] the receiving HOST.

   In that case must an HOST-HOST control procedure be provided?
```

> **III-1** 为什么 HOST 和 IMP 之间没有一个简单的控制规程？如果一条由 HOST 发出的消息，因传输错误而到达 IMP，会发生什么？
>
> 从 BBN 的规格来看，这个错误会被一路传送到接收端 HOST。
>
> 如果是这样，是否必须提供一套 **HOST-HOST 的控制规程**？

```
III-2.  Where will the special channel hardware unit be connected
        (MIOP/SIOP)?

   How will this device be notified of an outgoing message end in order
   to start the padding?

   (The program will provide to the MIOP SIOP the number of bytes of the
   outgoing message, and will receive back an interrupt when the last
   byte is sent out.  Is it that signal which will be also sent to the
   special device?)

   Vice versa how does the Handler know the length of the incoming
   message?  From the contents of the previous one or should this
   program always ready to receive a message of maximum length?  (Then
   an interrupt should be triggered when the real end is detected by the
   hardware).
```

> **III-2** 特殊通道硬件单元将接在哪里（**MIOP/SIOP**）？
>
> 这个设备如何被通知"输出消息已结束"，以便开始填充（padding）？
>
> （程序将向 MIOP/SIOP 提供输出消息的字节数，并在最后一个字节发送出去时收到一个中断。这个信号是否也会同时发给那个特殊设备？）
>
> 反过来，处理器程序如何知道**输入**消息的长度？是从上一条消息的内容推断，还是让这个程序总是准备接收最大长度的消息？（如果是后者，那么硬件检测到真正的结尾时应该触发一个中断。）

【译注】MIOP/SIOP 是 Sigma 7 主机的 I/O 处理器型号。"按最大长度准备接收 vs 从内容推断长度"——今天每个流式解析器都要做同样的选择。

```
III-3.  When does the Gordo documentation will be available in order to
        design the user-network program interface.  What are the
        mechanisms for program initiations, transferring parameters from
        one program to another, etc...
```

> **III-3** "Gordo"文档什么时候能提供？我们需要它来设计用户-网络程序接口。程序启动的机制是什么？参数如何在程序之间传递？等等……

【译注】"Gordo"是 UCLA Sigma 7 主机的操作系统。Deloche 在等操作系统的接口文档才能定用户-网络接口——1969 年的依赖地狱。

---

## 图 1 · Fig. 1（系统总体架构）

```
                           HOST (Sigma 7) <--|/|--> Outside world
   Users                                     |/|
    |                                        |/|
    |                                        |/|   Special  Standard
    V                                        |/|      |       |
         +--------------+   +------------+   |/|      V   |   V
    o----|              |   |            |   |/|   +------+------+
         |   Output     |-->|   Output   |-->|/|-->|      |      |-->IMP
    . . .|              |   |            |   |/|   |             |
         |              |   |            |   |/|   |      |      |
    o----| (Multiplex)  |   |            |   |/|   |             |
         |_ _ _ _ _ _ _ |   |_ _ _ _ _ _ |   |/|   | _ _ _| _ _ _|
    o----|              |   |            |   |/|   |      |      |
         |   Input      |<--|    Input   |<--|/|<--|             |<--IMP
    . . .|              |   |            |   |/|   |      |      |
         |              |   |            |   |/|   |             |
    o----|(Distribution)|   |            |   |/|   +------|------+
         |              |   |            |   |/|       HARDWARE
         +--------------+   +------------+   |/|       Interface
             NETWORK          HANDLER        |/|
             Program          Program        |/|
                                             |/|    (Fig. 1)
```

> **图 1 标注**（按原文保留）：
> - 左侧：多个用户程序（Users）分别接入 **NETWORK 程序**（上方 Output / 多路复用 Multiplex，下方 Input / 分发 Distribution）；
> - 中部：**HANDLER 程序**（输出与输入半部），中间竖线 `|/|` 为隔离符号；
> - 右侧：硬件接口（HARDWARE Interface），分 **Special**（特殊通道）与 **Standard**（标准通道）两条，最终通向 IMP。
>
> 数据流：用户 → 网络程序（多路复用）→ 处理器程序（输出）→ 硬件接口 → IMP；反向由 IMP → 硬件接口 → 处理器程序（输入）→ 网络程序（分发）→ 用户。

---

## 图 2 · Fig. 2（输出半部详细架构）

```
                                                   +------------------+
                                                   | | |              |
                                                   | | | interface    |
                                                   | | |              |
                                                   |                  |
                                                   | ====> Data       |
                                                   |                  |
                                                   | ----- Logical    |
                                                   |       information|
                                                   +------------------+

                      + - - - - - - - - - - - - - -+
                      |                            |
                              interface table
                      |        +----------+        |               | |
        | |              +---->|          |<----+                  | |
        | |           |  |     +----------+     |  |   interrupt   | |
        | |           ^  |                      |     +----<-------| |
        | |           |  |    +-          -+    |  |  |            | |
        | |           |  V    |  _________ |    V  V  V            | |
   o----| |-+  +---------+-+  | |         ||  +-+--+--+---+        | |
        | |  \ |+---------+|  | |_________||  |+---------+|        | |
        | |   \||         ||  |            |  ||         ||        | |
        | |    +|         ||  | - - - - - -|  ||         ||        | |
        | |    ||         ||  |            |  ||         ||        | |
    - - - - - -|| NETWORK ||=>-  _________ -=>|| HANDLER ||=======>| |
        | |    +| Progr.  ||  | |         ||  || Progr.  ||        | |
        | |   /||         ||  | |_________||  ||         ||        | |
        | |  / |+---------+|  |            |  |+---------+|        | |
   o----| |-+  +-----------+  |  _________ |  +----+------+        | |
   ^    | |                   | |         ||       |               | |
   |    | |                   | |_________||       +--->---------->| |
   |     ^                    +-    ^     -+         Commands      | |
   | Users                          |                              | |
         |                    Pool of buffers                      | |
       User's                                                       ^
      Interface                                                     |
                                                              Hardware
                                                             Interface

                           (Fig. 2)
```

> **图 2 标注**（按原文保留）：
> - 左侧：用户（Users）通过用户接口（User's Interface）进入 **NETWORK 程序**（网络程序）；
> - 中部上方：**接口表（interface table）**——网络程序与处理器程序通过它交换逻辑信息；
> - 中部下方：**缓冲池（Pool of buffers）**——虚线框内的缓冲块，数据经此从网络程序流向处理器程序；
> - 右侧：**HANDLER 程序**（处理器程序），向下输出命令（Commands）到硬件接口（Hardware Interface）；硬件侧还有中断（interrupt）信号回到处理器程序。
>
> 两张图展示了本文的核心设计：网络程序与处理器程序之间，数据走缓冲池、逻辑信息走接口表——生产者-消费者结构的 1969 版。

---

```
         [ This RFC was put into machine readable form for entry ]
   [ into the online RFC archives by Bob German & Lorrie Shiota 1/02 ]
```

> 【归档说明】这份 RFC 由 Bob German 与 Lorrie Shiota 于 2002 年 1 月录入为机器可读形式，收入在线 RFC 档案。

---

## 翻译说明

- 本文档以「英文原文在上（代码块）、中文译文在下（引用块）」的方式逐段对照。
- 图 1、图 2 为原文 ASCII 架构图，按原样保留，图下附中文标注说明数据流。
- 原文中 "eEtracting"、"int" 等笔误及 "(unreadable)"（无法辨认）处均照实保留并加注。
- 【译注】为译者补充的背景说明。

