# RFC 6 — Conversation with Bob Kahn（与 Bob Kahn 的谈话）
> **中英对照翻译版本**
> 原文作者：Steve Crocker（UCLA 加州大学洛杉矶分校）
> 原文发布日期：1969 年 4 月 10 日
> 翻译说明：本文件采用「英文原文在上，中文翻译在下」的逐段对照格式。专业术语首次出现时附原文。

---

## 文头 · Header

```
Network Working Note                                    Steve Crocker, UCLA
RFC-6                                                   10 April 1969
```

> 网络工作笔记（Network Working Note）                   斯蒂夫·克罗克，加州大学洛杉矶分校
> RFC 第 6 号                                              1969 年 4 月 10 日

【译注】注意这里自称 "Network Working Note"（网络工作笔记）而非 "Request for Comments"——早期 RFC 系列连自己的叫法都还没统一。

```
                        CONVERSATION WITH BOB KAHN
```

>                             与鲍勃·卡恩的谈话

---

## 正文 · Body

```
I talked with Bob Kahn at BB&N yesterday.  We talked about code conversion
in the IMP's, IMP-HOST communication, and HOST software.
```

> 昨天我在 BB&N 与鲍勃·卡恩（Bob Kahn）谈了谈。我们讨论了 IMP 中的代码转换（code conversion）、IMP-主机通信（IMP-HOST communication）以及主机软件（HOST software）。

```
BB&N is prepared to convert 6, 7, 8, or 9 bit character codes into 8-bit
ASCII for transmission and convert again upon assembly at the destination
IMP.  BB&N plans a one for one conversion scheme with tables unique to the
HOST.  I suggested that places with 6-bit codes may also want case shifting.
Bob said this may result in overflow if too many case shifts are necessary.
I suggested that this is rare and we could probably live with an overflow
indication instead of a guarantee.
```

> BB&N 准备将 6、7、8 或 9 位的字符编码转换为 8 位 ASCII 以便传输，并在目的端 IMP 组装消息时再转换回来。BB&N 计划采用**一对一转换方案**，每台主机各配一张**独特的转换表**。
>
> 我建议：使用 6 位编码的站点可能还想要大小写切换（case shifting）。鲍勃说，如果需要的切换次数太多，可能会导致溢出（overflow）。我回应说这种情况很罕见，我们大概可以**用溢出指示来代替保证**（即出错了给个标记，而不是保证一定能处理）。

【译注】"用溢出指示代替保证"——1969 年的工程取舍谈判：设计者提需求、制造商报成本、最后以"覆盖 99% 情况 + 显式错误标记"成交。

```
With respect to HOST-IMP communication, we now have a five bit link field
and a bit to indicate conversion.  Also possible is a 2-bit conversion
indicator, one for converting before sending and one for converting after.
This would allow another handle for checking or controlling the system.
```

> 关于主机-IMP 通信：我们现在有了一个 **5 位链路字段**（link field）和 **1 位转换指示位**。还有可能增加一个 **2 位转换指示器**——一位表示发送前转换、一位表示接收后转换。这样系统就多了一个用于检查或控制的抓手（handle）。

```
The HOST can send messages or portions of a message to its IMP specifying

        1.  Tracing
        2.  Conversion
        3.  Whether message is for destination IMP or HOST
        4.  Send RFNM
        5.  HOST up or down
        6.  Synchronization
        7.  Format Error Messages
        8.  Master Link Clear
        9.  Status Requested
```

> 主机可以向它的 IMP 发送消息（或消息的一部分），并指定以下 9 种事项：
>
> 1. 追踪（Tracing）
> 2. 转换（Conversion）
> 3. 消息是发给目的端 IMP 还是目的端 HOST
> 4. 发送 RFNM（请求下一条消息）
> 5. HOST 开机 / 关机
> 6. 同步（Synchronization）
> 7. 格式错误消息（Format Error Messages）
> 8. 主链路清除（Master Link Clear）
> 9. 请求状态（Status Requested）

```
The IMP can send to its HOST information on

        1.  Conversion
        2.  REFNM Arrived
        3.  IMP up or down
        4.  Synchornization
        5.  Called HOST not Responding
        6.  Format Error
        7.  Status in IMP
```

> IMP 可以向它的 HOST 发送以下 7 种信息：
>
> 1. 转换（Conversion）
> 2. RFNM 已到达（REFNM Arrived）
> 3. IMP 开机 / 关机
> 4. 同步（Synchornization）
> 5. 被叫 HOST 无响应（Called HOST not Responding）
> 6. 格式错误（Format Error）
> 7. IMP 内状态（Status in IMP）

【译注】原文 "REFNM" 应为 "RFNM" 的笔误；"Synchornization" 应为 "Synchronization"。这两张清单（9 条下行 + 7 条上行）就是最早的"控制面协议消息类型定义"，今天 ICMP 消息类型、USB 控制请求的直系祖先。

```
I also summarized for Bob the contents of Network Notes l, 2, and 3.
```

> 我还给鲍勃总结了网络笔记（Network Notes）第 1、2、3 号的内容。

【译注】即 RFC 1、2、3——设计者给硬件制造商补课。

---

## 翻译说明

- 本文档以「英文原文在上（代码块）、中文译文在下（引用块）」的方式逐段对照。
- 【译注】为译者补充的背景说明。
- 原文结尾 "Network Notes l, 2, and 3" 中 "l" 为数字 1 的笔误（或老式打字机的字模效果）。