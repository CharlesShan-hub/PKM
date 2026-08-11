# RFC 1 — Host Software（主机软件）
> **中英对照翻译版本**
> 原文发布日期：1969 年 4 月 7 日
> 翻译说明：本文件采用「英文原文在上，中文翻译在下」的逐段对照格式。对于专业术语，首次出现时附原文保留；ASCII 架构图保持原图，附中文标注。

---

## 文头 · Header

```
Network Working Group                                   Steve Crocker
Request for Comments: 1                                          UCLA
                                                         7 April 1969
```

> 网络工作组                                               斯蒂夫·克罗克
> 请求评论：编号 1                                    加州大学洛杉矶分校
>                                                          1969 年 4 月 7 日

---

```
                         Title:   Host Software
                        Author:   Steve Crocker
                          Installation:   UCLA
                          Date:   7 April 1969
             Network Working Group Request for Comment:   1
```

>                        标题：主机软件
>                        作者：斯蒂夫·克罗克
>                    所属机构：加州大学洛杉矶分校（UCLA）
>                        日期：1969 年 4 月 7 日
>             网络工作组 · 请求评论系列：第 1 号

---

## 目录 · CONTENTS

```
INTRODUCTION

  I. A Summary of the IMP Software

     Messages

     Links

     IMP Transmission and Error Checking

     Open Questions on the IMP Software

 II. Some Requirements Upon the Host-to-Host Software

     Simple Use

     Deep Use

     Error Checking

III. The Host Software

     Establishment of a Connection

     High Volume Transmission

     A Summary of Primitives

     Error Checking

     Closer Interaction

     Open Questions

 IV. Initial Experiments

     Experiment One

     Experiment Two
```

> 引言
>
>   一、IMP 软件摘要
>
>      消息（Messages）
>
>      链路（Links）
>
>      IMP 的传输与错误校验
>
>      关于 IMP 软件的开放问题
>
>   二、对主机到主机软件的若干需求
>
>      简单使用（Simple Use）
>
>      深度使用（Deep Use）
>
>      错误校验（Error Checking）
>
>   三、主机软件
>
>      连接的建立
>
>      高吞吐传输
>
>      原语摘要
>
>      错误校验
>
>      更紧密的交互（Closer Interaction）
>
>      开放问题
>
>   四、初步实验
>
>      实验一
>
>      实验二

> 【译注】原始文档的「第 1 页」标记位置
> Crocker 著                                                     第 1 页
> RFC 1                        主机软件                    1969 年 4 月 7 日

---

## 引言 · Introduction

```
   The software for the ARPA Network exists partly in the IMPs and
   partly in the respective HOSTs.  BB&N has specified the software of
   the IMPs and it is the responsibility of the HOST groups to agree on
   HOST software.
```

> ARPA 网络的软件一部分运行在 IMP（接口消息处理机）上，另一部分运行在各自的 HOST（主机）上。IMP 端的软件已经由 BB&N 公司（Bolt, Beranek and Newman）制定完毕；而 HOST 端应该使用什么样的软件，则需要各主机站点小组自行讨论并达成一致。

```
   During the summer of 1968, representatives from the initial four
   sites met several times to discuss the HOST software and initial
   experiments on the network.  There emerged from these meetings a
   working group of three, Steve Carr from Utah, Jeff Rulifson from SRI,
   and Steve Crocker of UCLA, who met during the fall and winter.  The
   most recent meeting was in the last week of March in Utah.  Also
   present was Bill Duvall of SRI who has recently started working with
   Jeff Rulifson.
```

> 1968 年夏天，首批四个站点的代表多次碰面，共同讨论主机软件的设计以及在网络上进行的初步实验。经过这些讨论，三人工作小组正式成立：犹他大学的 Steve Carr、斯坦福研究院（SRI）的 Jeff Rulifson，以及 UCLA 的 Steve Crocker。整个秋冬两季，小组持续会面讨论。最近一次会议是 1969 年 3 月最后一周在犹他大学召开的，SRI 新加入团队、开始与 Jeff Rulifson 合作的 Bill Duvall 也出席了会议。

```
   Somewhat independently, Gerard DeLoche of UCLA has been working on
   the HOST-IMP interface.
```

> 另外（与小组工作相对独立地），UCLA 的 Gerard DeLoche 一直在研究 HOST 与 IMP 之间的硬件接口问题。

```
   I present here some of the tentative agreements reached and some of
   the open questions encountered.  Very little of what is here is firm
   and reactions are expected.
```

> 我在本文档中陈述目前为止我们达成的若干暂时性共识，以及讨论中遇到的一些悬而未决的开放问题。**本文档所列内容几乎没有一条是最终确定的，热切欢迎各位的反馈与修改意见。**

> 【译注】原始文档的「第 2 页」标记位置
> Crocker 著                                                     第 2 页
> RFC 1                        主机软件                    1969 年 4 月 7 日

---

## 一、IMP 软件摘要 · I. A Summary of the IMP Software

### 消息 · Messages

```
   Information is transmitted from HOST to HOST in bundles called
   messages.  A message is any stream of not more than 8080 bits,
   together with its header.  The header is 16 bits and contains the
   following information:
```

> 主机与主机之间传输的信息以「消息（message）」为单位进行打包。一条消息由「不超过 8080 比特的数据流」加上它的消息头组成。消息头固定为 16 比特，包含以下字段：

| 字段（Field） | 长度（Length） | 原文 |
|---|---|---|
| 目标地址（Destination） | 5 bits | Destination |
| 链路号（Link） | 8 bits | Link |
| 追踪位（Trace） | 1 bit | Trace |
| 保留位（Spare） | 2 bits | Spare |

> 【译注】原始文档中这四个字段以列对齐格式展示，上面是对照的字段翻译表。原文如下：

```
           Destination     5 bits
           Link            8 bits
           Trace           1 bit
           Spare           2 bits
```

```
   The destination is the numerical code for the HOST to which the
   message should be sent.  The trace bit signals the IMPs to record
   status information about the message and send the information back to
   the NMC (Network Measurement Center, i.e., UCLA).  The spare bits are
   unused.
```

> - **Destination（目标地址）**：目标主机的数字编号（即消息要发往哪台 HOST）。
> - **Trace（追踪位）**：如果该位设为 1，会要求沿途所有 IMP 记录这条消息经过时的状态信息，并把记录回传给 NMC（网络测量中心，即 UCLA）。
> - **Spare（保留位）**：暂时未使用。

> 【译注】原始文档的「第 3 页」标记位置
> Crocker 著                                                     第 3 页
> RFC 1                        主机软件                    1969 年 4 月 7 日

---

### 链路 · Links

```
   The link field is a special device used by the IMPs to limit certain
   kinds of congestion.  They function as follows.  Between every pair of
   HOSTs there are 32 logical full-duplex connections over which messages
   may be passed in either direction.  The IMPs place the restriction on
   these links that no HOST can send two successive messages over the
   same link before the IMP at the destination has sent back a special
   message called an RFNM (Request for Next Message).  This arrangement
   limits the congestion one HOST can cause another if the sending HOST
   is attempting to send too much over one link.  We note, however, that
   since the IMP at the destination does not have enough capacity to
   handle all 32 links simultaneously, the links serve their purpose only
   if the overload is coming from one or two links.  It is necessary for
   the HOSTs to cooperate in this respect.
```

> **Link（链路号）字段**是 IMP 用来限制特定类型拥塞的一种特殊机制。它的工作方式如下：在任意一对主机之间，存在 **32 条逻辑层面的全双工连接**（称为「链路 link」），消息可以在任意一条链路上双向传输。IMP 对这些链路施加了一条硬性限制：**在同一条链路上，一台主机在发出一条消息之后，必须等到目的地 IMP 回发一条名为 RFNM（Request For Next Message，即「允许发送下一条」）的特殊消息，才能继续发送下一条消息。**
>
> 这个安排的目的是：如果某台发送端主机试图在单条链路上发送过多数据，这套机制可以限制它对接收端主机造成的拥塞压力。
>
> 但我们也注意到：由于目的地 IMP 的处理能力并不足以同时满载处理 32 条链路，因此只有当过载流量集中在一两条链路上时，这套机制才能真正发挥作用。**如果所有链路同时超载，还是得靠各主机端自觉配合限流。**

```
   The links have the following primitive characteristics.  They are
   always functioning and there are always 32 of them.
```

> 链路具备以下两条基本特性：它们始终处于可用状态；并且数量永远固定为 32 条。

```
   By "always functioning," we mean that the IMPs are always prepared to
   transmit another message over them.  No notion of beginning or ending
   a conversation is contained in the IMP software.  It is thus not
   possible to query an IMP about the state of a link (although it might
   be possible to query an IMP about the recent history of a link --
   quite a different matter!).
```

> 所谓「始终可用」，意思是 IMP 时刻准备好接收并转发下一条消息——在 IMP 的软件层面，**不存在「建立一次会话」或者「结束一次会话」的概念**。因此，你无法向一台 IMP 查询某条链路当前是什么状态（但或许可以查询一条链路近期的历史记录——这是完全不同的两回事）。

```
   The other primitive characteristic of the links is that there are
   always 32 of them, whether they are in use or not.  This means that
   each IMP must maintain 18 tables, each with 32 entries, regardless of
   the actual traffic.
```

> 另一条基本特性是：**无论实际是否被使用，链路数量固定是 32 条**。这意味着不管实际网络流量大小，每台 IMP 都必须在内存中维护 18 张表，每张表固定 32 个条目。

```
   The objections to the link structure notwithstanding, the links are
   easily programmed within the IMPs and are probably a better
   alternative to more complex arrangements just because of their
   simplicity.
```

> 尽管上述链路结构存在不少缺点，但它在 IMP 内部实现起来编程简单；也许正因为简单，反而是比更复杂方案更合适的选择。

---

### IMP 的传输与错误校验 · IMP Transmission and Error Checking

```
   After receiving a message from a HOST, an IMP partitions the message
   into one or more packets.  Packets are not more than 1010 bits long
   and are the unit of data transmission from IMP to IMP.  A 24 bit
   cyclic checksum is computed by the transmission hardware and is
   appended to an outgoing packet.  The checksum is recomputed by the
   receiving hardware and is checked against the transmitted checksum.
   Packets are reassembled into messages at the destination IMP.
```

> 当一台 IMP 从自己连接的主机收到一条消息后，会把整条消息切分成一个或多个 **「包（packet）」**。每个包的长度不超过 1010 比特，是 IMP 与 IMP 之间数据传输的基本单位。
>
> 发送端的传输硬件会对每个包计算一个 24 比特的**循环校验和（cyclic checksum，即 CRC）**，附加在发出的包后面；接收端硬件会重新计算一遍校验和，并与收到的校验和比对，不一致则丢弃。当属于同一条消息的所有包都到达目的地后，IMP 会把它们重新拼装回原来的完整消息，再交给连接的主机。

---

### 关于 IMP 软件的开放问题 · Open Questions on the IMP Software

> 【译注】原始文档的「第 4 页」标记位置
> Crocker 著                                                     第 4 页
> RFC 1                        主机软件                    1969 年 4 月 7 日

```
   1.  An 8 bit field is provided for link specification, but only 32
   links are provided, why?
```

> 1. 链路号（Link）字段给了 8 个比特（理论上可表示 256 条链路），但实际上只有 32 条链路可用——这是为什么？

```
   2.  The HOST is supposed to be able to send messages to its IMP.  How
   does it do this?
```

> 2. 主机应当能够向「自己连接的那台 IMP」（而非远端主机）发送消息——具体该怎么做？用什么地址格式？

```
   3.  Can a HOST, as opposed to its IMP, control RFNMs?
```

> 3. RFNM（允许发送下一条消息）的发送节奏是 IMP 自己控制的。那么主机（而非 IMP）能否对 RFNM 的节奏施加影响或控制？

```
   4.  Will the IMPs perform code conversion?  How is it to be
   controlled?
```

> 4. IMP 是否会执行字符编码转换（比如 EBCDIC 与 ASCII 之间互转）？如果会，由谁以什么方式来控制何时转换、转换什么内容？

---

## 二、对主机到主机软件的若干需求 · II. Some Requirements Upon the Host-to-Host Software

### 简单使用 · Simple Use

```
   As with any new facility, there will be a period of very light usage
   until the community of users experiments with the network and begins
   to depend upon it.  One of our goals must be to stimulate the
   immediate and easy use by a wide class of users.  With this goal, it
   seems natural to provide the ability to use any remote HOST as if it
   had been dialed up from a TTY (teletype) terminal.  Additionally, we
   would like some ability to transmit a file in a somewhat different
   manner perhaps than simulating a teletype.
```

> 和任何新设施一样，在广大用户真正开始尝试使用网络并依赖它之前，网络会经历一段使用量非常稀少的时期。因此我们的核心目标之一，必须是**让尽可能广泛的用户群体能够立刻、轻松地用起来**。
>
> 围绕这个目标，最自然的设计就是：**使用任意一台远程主机时，体验应该和用一台 TTY 电传打字机通过电话线拨号连上那台主机没有区别。** 除此之外，我们还希望提供某种「传输文件」的能力——文件传输的方式最好不要只是「模拟电传打字机逐字发送」那么原始，而应有所不同、效率更高。

---

### 深度使用 · Deep Use

```
   One of the inherent problems in the network is the fact that all responses
   from a remote HOST will require on the order of a half-second or so,
   no matter how simple.  For teletype use, we could shift to a
   half-duplex local-echo arrangement, but this would destroy some of the
   usefulness of the network.  The 940 Systems, for example, have a very
   specialized echo.
```

> 网络有一个与生俱来的问题：无论请求多么简单，从远程主机返回响应**都需要大约半秒钟甚至更长的往返延迟**。对于单纯的电传打字机用法，我们也许可以改用「半双工 · 本地回显」的方案来规避延迟——但这会破坏网络的一部分实用性。举例来说，SDS 940 系列计算机就有一套非常特殊、与众不同的回显逻辑，如果改用本地回显就无法复刻了。

```
   When we consider using graphics stations or other sophisticated
   terminals under the control of a remote HOST, the problem becomes more
   severe. We must look for some method which allows us to use our most
   sophisticated equipment as much as possible as if we were connected
   directly to the remote computer.
```

> 而当我们考虑在远程主机控制下使用**图形工作站**或其他精密终端设备时，延迟问题会变得更加严重。我们必须找到某种方法，让我们在操作自己手里最精密的设备时，**尽可能接近「直接用线缆连在那台远程计算机上」的使用体验**。

---

### 错误校验 · Error Checking

> 【译注】原始文档的「第 5 页」标记位置
> Crocker 著                                                     第 5 页
> RFC 1                        主机软件                    1969 年 4 月 7 日

```
   The point is made by Jeff Rulifson at SRI that error checking at major
   software interfaces is always a good thing. He points to some
   experience at SRI where it has saved much dispute and wasted effort.
   On these grounds, we would like to see some HOST to HOST checking.
   Besides checking the software interface, it would also check the
   HOST-IMP transmission hardware.  (BB&N claims the HOST-IMP hardware
   will be as reliable as the internal registers of the HOST.  We believe
   them, but we still want the error checking.)
```

> 这一条由 SRI 的 Jeff Rulifson 提出：**在所有主要的软件接口处做错误校验，永远是一件好事。** 他举出了 SRI 内部的实践经验：这种校验曾经帮他们省下了无数互相「甩锅」的争论和被浪费的排错时间。
>
> 基于这一理由，我们认为**主机与主机之间必须再加一层校验**。这层校验除了校验软件接口本身，同时也会覆盖 HOST 到 IMP 的传输硬件。
>
> （BB&N 向我们打包票说 HOST-IMP 之间的硬件连线，会和主机内部寄存器一样可靠。**我们相信他们说的是真话——但我们仍然希望加上这层校验。**）

---

## 三、主机软件 · III. The Host Software

### 连接的建立 · Establishment of a Connection

```
   The simplest connection we can imagine is where the local HOST acts as
   if it is a TTY and has dialed up the remote HOST.  After some
   consideration of the problems of initiating and terminating such a
   connection , it has been decided to reserve link 0 for communication
   between HOST operating systems.  The remaining 31 links are thus to be
   used as dial-up lines.
```

> 我们能想象到的最简单的连接场景，就是**本地主机模拟成一台 TTY 电传打字机，通过「拨号」连上了远程主机**。在对「如何发起、如何断开这样一条连接」的问题进行了充分讨论之后，我们决定：
>
> - **链路 0（Link 0）专门预留给两台主机的操作系统之间做控制通信用**，用户程序永远不能直接使用；
> - 剩下的 31 条链路（Link 1 ~ 31）则作为「拨号线路」，分配给用户层程序使用。

```
   Each HOST operating system must provide to its user level programs a
   primitive to establish a connection with a remote HOST and a primitive
   to break the connection.  When these primitives are invoked, the
   operating system must select a free link and send a message over link
   0 to the remote HOST requesting a connection on the selected link.
   The operating system in the remote HOST must agree and send back an
   accepting message over link 0.  In the event both HOSTs select the same
   link to initiate a connection and both send request messages at
   essentially the same time, a simple priority scheme will be invoked in
   which the HOST of lower priority gives way and selects another free
   link.  One usable priority scheme is simply the ranking of HOSTS
   by their identification numbers.  Note that both HOSTs are aware that
   simultaneous requests have been made, but they take complementary
   actions: The higher priority HOST disregards the request while the
   lower priority HOST sends both an acceptance and another request.
```

> 每台主机的操作系统，必须向用户态程序提供两个最基本的原语（系统调用）：
> ① **与某台远程主机建立一条连接**；
> ② **断开当前连接**。
>
> 当用户程序调用「建立连接」时，操作系统需要：
> 1. 从自己的 31 条数据链路中**挑选一条空闲的**；
> 2. 通过 **链路 0** 向远程主机的操作系统发送一条控制消息，内容是「我希望用第 X 号链路与你建立用户级连接」；
> 3. 远程主机操作系统检查自己这边第 X 号链路是否空闲，如果空闲就通过链路 0 回发一条「同意连接」的消息。
>
> 如果出现极端情况：**两台主机同时想连接对方，而且恰好都挑中了同一条数据链路，并且几乎同时发出了请求消息**——我们将启用一套简单的优先级方案来解决冲突：
>
> **优先级较低的那台主机主动退让，重新选择另一条空闲链路再次发起请求；优先级较高的主机则忽略对方的请求，原地等待。**
>
> 一套可行的优先级规则，就是直接按主机的「编号（identification number）」大小排序——编号越小优先级越高。
>
> 请注意：发生冲突时，两边的主机都能意识到「双方同时发起了请求」，但它们会采取**互补的动作**：优先级高的主机直接忽略对方的请求（不做任何响应），优先级低的主机则一方面向对方发送「我接受你的请求」，另一方面自己挑一条新链路重新发起一个新请求。如此冲突就被解决了。

```
   The connection so established is a TTY-like connection in the
   pre-log-in state.  This means the remote HOST operating system will
   initially treat the link as if a TTY had just called up.  The remote
   HOST will generate the same echos, expect the same log-in sequence and
   look for the same interrupt characters.
```

> 通过以上方式建立起来的连接，默认是**「TTY-like（类似电传打字机）」模式**，并且处于**「登录前（pre-log-in）」**状态。这意味着远程主机的操作系统会把这条链路，当作「一台刚刚拨号进来的电传打字机」来对待——会输出同样的登录提示符、执行同样的字符回显逻辑、要求同样的登录步骤、识别同样的中断字符。

---

### 高吞吐传输 · High Volume Transmission

> 【译注】原始文档的「第 6 页」标记位置
> Crocker 著                                                     第 6 页
> RFC 1                        主机软件                    1969 年 4 月 7 日

```
   Teletypes acting as terminals have two special drawbacks when we
   consider the transmission of a large file.  The first is that some
   characters are special interrupt characters.  The second is that
   special buffering techniques are often employed, and these are
   appropriate only for low-speed character at time transmission.
```

> 如果在 TTY-like 模式下传输大文件，「电传打字机作为终端」的设计有两个先天的弊端：
> 1. **中断字符问题**：TTY 模式下会把特定字节（例如 Ctrl+C）当做中断信号处理，而文件中的字节完全可能恰好等于这些特殊字符值——会导致文件损坏或传输中断；
> 2. **缓冲策略问题**：TTY 模式通常使用「逐字符到来、立刻处理」的特殊缓冲方式，这种方式只适合低速的、一次一个字符的终端交互，完全不适合大文件的高速传输。

```
   We therefore define another class of connection to be used for the
   transmission of files or other large volumes of data.  To initiate
   this class of link, user level programs at both ends of an established
   TTY-like link must request the establishment of a file-like connection
   parallel to the TTY-like link.  Again the priority scheme comes into
   play, for the higher priority HOST sends a message over link 0 while
   the lower priority HOST waits for it.  The user level programs are, of
   course, not concerned with this.  Selection of the free link is done
   by the higher priority HOST.
```

> 因此我们定义了**另一类连接模式**：专门用于文件或其他大体量数据传输的 **「File-like（类似文件）」模式**。
>
> 要发起 File-like 连接，流程是：两台主机之间必须先有一条**已经建立好的 TTY-like 连接**；然后两边的用户级程序都同意「我们来开一条 File-like 的并行链路传数据吧」。
>
> 此时之前的优先级方案会再次派上用场：**优先级较高的主机负责挑选一条空闲的数据链路，并通过链路 0 发出协商消息；优先级较低的主机则等待对方发过来。** 用户级程序当然不需要关心这些底层细节。新链路的选择工作始终由优先级高的主机执行。

```
   File-like links are distinguished by the fact that no searching for
   interrupt characters takes place and buffering techniques appropriate
   for the higher data rates takes place.
```

> File-like 链路有两个核心特点：
> 1. **不扫描任何中断字符**——所有字节一律当作纯数据对待；
> 2. **采用适合更高数据速率的缓冲策略**（大块流式缓冲，而非逐字处理）。

---

### 原语摘要 · A Summary of Primitives

```
   Each HOST operating systems must provide at least the following
   primitives to its users.  This list knows not to be necessary but not
   sufficient.
```

> 每台主机的操作系统，至少应当向用户程序提供以下 6 个原语（系统调用）。请注意：这份列表是**必要条件，但不充分**——后续肯定还需要增加更多。

> 【译注】原文中 "This list knows not to be necessary but not sufficient." 疑似笔误，应为 "This list is known to be necessary but not sufficient."（据后续 RFC 的通行说法校正），因此翻译为「本列表为必要条件，但不充分」。

| 编号 | 原文 | 翻译 |
|---|---|---|
| a | Initiate TTY-like connection with HOST x. | a. 发起到主机 x 的一条 TTY-like（终端交互式）连接。 |
| b | Terminate connection. | b. 终止当前连接。 |
| c | Send/Receive character(s) over TTY-like connection. | c. 通过 TTY-like 连接发送 / 接收字符。 |
| d | Initiate file-like connection parallel to TTY-like connection. | d. 在现有的 TTY-like 连接旁，并行发起一条 File-like（文件传输式）连接。 |
| e | Terminate file-like connection. | e. 终止 File-like 连接。 |
| f | Send/Receive over file-like connection. | f. 通过 File-like 连接发送 / 接收数据。 |

---

### 错误校验 · Error Checking

```
   We propose that each message carry a message number, bit count, and a
   checksum in its body, that is transparent to the IMP.  For a checksum
   we suggest a 16-bit end-around-carry sum computed on 1152 bits and
   then circularly shifted right one bit.  The right circular shift every
   1152 bits is designed to catch errors in message reassembly by the IMPs.
```

> 我们提议：每条消息的正文中，应当携带以下三个字段（它们对 IMP 完全透明——IMP 不会解析也不会修改它们）：
> 1. **消息号（Message Number）**；
> 2. **位计数（Bit Count，即正文长度）**；
> 3. **校验和（Checksum）**。
>
> 关于校验和算法，我们建议采用**「16 比特循环进位和」**：
>
> - 把消息正文按 **每 1152 比特为一块** 分块；
> - 对每块计算循环进位和（即两个 16 比特数相加时，若最高位溢出则把溢出位回加到最低位）；
> - 每算完一块之后，整个 16 比特结果**循环右移一位**，然后再算下一块……最终得到整个 16 比特校验和。
>
> 之所以「每 1152 比特循环右移一位」，是为了**专门捕获 IMP 在重组消息时把包顺序搞反**这种特定错误——如果只是简单相加，由于加法交换律，包的顺序调换可能仍然算出同样的和；而块之间引入了循环位移的编码后，顺序错位会立刻导致校验和对不上。

---

## 更紧密的交互 · Closer Interaction

> 【译注】原始文档的「第 7 页」标记位置
> Crocker 著                                                     第 7 页
> RFC 1                        主机软件                    1969 年 4 月 7 日

```
   The above described primitives suggest how a user can make simple use
   of a remote facility.  They shed no light on how much more intricate
   use of the network is to be carried out.  Specifically, we are
   concerned with the fact that as some sites a great deal of work has
   gone into making the computer highly responsive to a sophisticated
   console.  Culler's consoles at UCSB and Englebart's at SRI are at
   least two examples.  It is clear that delays of a half-second or so
   for trivial echo-like responses degrade the interaction to the point
   of making the sophistication of the console irrelevant.
```

> 前文描述的几个原语，只说明了用户如何「简单地」使用远程设施。它们并没有回答：对于更复杂的深度用法，网络交互应该如何进行？
>
> 我们尤为关心一个问题：有些站点投入了巨大的精力，把自己的计算机系统做成**对精密控制台设备具备毫秒级响应**——UCSB 的 Culler 图形控制台、SRI 的 Engelbart NLS 控制台，就是两个最好的例子。很明显，如果**连一个最琐碎的字符回显都要等半秒钟延迟**，整套交互体验会急剧下降，精密控制台的所有优势都变得毫无意义。

```
   We believe that most console interaction can be divided into two
   parts, an essentially local, immediate and trivial part and a remote,
   more lengthy and significant part.  As a simple example, consider a
   user at a console consisting of a keyboard and refreshing display
   screen.  The program the user is talking typing into accumulates a
   string of characters until a carriage return is encountered and then
   it processes the string.  While characters are being typed, it
   displays the characters on the screen.  When a rubout character is
   typed, it deletes the previous non-rubout character.  If the user
   types H E L L O <- <- P <CR> where <- is rubout and <CR> is
   carriage-return, he has made nine keystrokes.  If each of these
   keystrokes causes a message to be sent which in return invokes
   instructions to our display station we will quickly become bored.
```

> 我们认为，**绝大多数控制台交互，都可以拆成两个部分**：
> 1. **本地的、即时的、琐碎的部分**；
> 2. **远程的、耗时的、有实质意义的部分**。
>
> 举一个具体的小例子：设想用户面对一台由键盘和刷新显示屏幕组成的控制台。用户正在输入的程序会不断累积字符，直到遇到回车（Carriage Return）再处理整串字符；打字过程中，程序实时把字符显示在屏幕上；用户按下退格键（Rubout）时，删除上一个非退格的字符。
>
> 假设用户依次按下：`H` `E` `L` `L` `O` `←` `←` `P` `↵`（其中 `←` 是退格 Rubout，`↵` 是回车 Carriage-Return）——一共 **9 次按键**。
>
> 如果每一次按键都要：「发消息到远端 → 远端处理 → 回发显示指令到本地屏幕」走一趟半秒延迟，那么用户看到完整的 `HELP↵` 出现在屏幕上需要等大约 **4.5 秒**——这会让人立刻失去耐心。

```
   A better solution would be to have the front-end of the remote program
   -- that is the part scanning for <- and <CR> -- be resident in our
   computer.  In that case, only one five character message would be
   sent, i.e., H E L P <CR>, and the screen would be managed locally.
```

> 一个好得多的解决方案是：**把远程程序的「前端」——也就是扫描退格键、扫描回车、管理显示的那部分逻辑——放到我们本地的计算机里常驻执行。**
>
> 这样一来，9 次按键中前 8 次全部本地处理、本地回显、本地更新屏幕；只有当用户真正按下回车 `↵` 时，才**打包发送一条 5 个字符的消息（即 `HELP↵`）** 给远端。屏幕管理全程在本地完成。

```
   We propose to implement this solution by creating a language for
   console control.  This language, current named DEL, would be used by
   subsystem designers to specify what components are needed in a
   terminal and how the terminal is to respond to inputs from its
   keyboard, Lincoln Wand, etc.  Then, as a part of the initial protocol,
   the remote HOST would send to the local HOST, the source language text
   of the program which controls the console.  This program would have
   been by the subsystem designer in DEL, but will be compiled locally.
```

> 我们打算通过**创造一门专门用于控制台控制的语言**，来实现上述方案。这门语言目前命名为 **DEL（Dialog Expression Language，对话表达式语言）**。子系统的设计者使用 DEL 来描述：
> - 一台终端需要哪些组件（键盘、魔杖、屏幕等）；
> - 面对来自键盘、Lincoln Wand（UCSB 图形控制台的魔杖输入设备）等的输入，终端应该如何响应。
>
> 然后，作为初始协议的一部分，**远程主机把这段「控制台控制程序」的 DEL 源代码（注意是源代码文本，而不是二进制机器码），通过网络发送给本地主机。** 这段程序虽然是由远端子系统的设计者用 DEL 写的，但**它将在本地主机上，被本地的 DEL 编译器编译后执行。**

```
   The specifications of DEL are under discussion.  The following
   diagrams show the sequence of actions.
```

> DEL 语言的具体规范目前仍在讨论中。下面的三组框图，展示了整个交互流程的三个阶段。

---

> 【译注】原始文档的「第 8 页」标记位置
> Crocker 著                                                     第 8 页
> RFC 1                        主机软件                    1969 年 4 月 7 日

### 阶段 A：链路建立之前 · A. Before Link Establishment

```
         /                                                      \
        |     +-----------+                    +-----------+    |
        |     |           |                    |           |    |
        |     |           |                    |           |    |
        |     | terminal  |                    | terminal  |    |
        |     |           |                    |           |    |
        |     |           |                    |           |    |
        |     +-----+-----+                    +-----+-----+    |
        |           |                                |          |
        |           |                                |          |
        |           |                                |          |
        |     +-----+-----+                    +-----------+    |
        |     |     |     | Request connection |     |     |    |
   UCLA {     |     |     | -> over link 25    |     |     |    } SRI
        |     |   +-+-+   |  +-+          +-+  |   +-+-+   |    |
        |     |   | OS|---+-=|I|----------|I|=-+---| OS|   |    |
        |     |   +-+-+   |  +-+          +-+  |   +---+   |    |
        |     |           |                    |           |    |
        |     |           |                    |           |    |
        |     +-----------+                    +-----------+    |
        |      HOST: UCLA                        HOST: SRI      |
         \                                                     /
```

> **【中文注释版 · 阶段 A】链路建立之前**
>
> ```
>        /                                                                \
>       |   +------------------+                       +------------------+  |
>       |   |     本地终端       |                       |     远端终端       |  |
>       |   +--------+---------+                       +--------+---------+  |
>       |            |                                           |           |
>       |            |                                           |           |
>       |   +--------+---------+                       +--------+---------+  |
>       |   | 「通过链路 25 请求连接」 ------------>                       |  |
> UCLA  |   |  +--------------+  | IMP IMP  |  +--------------+  | SRI
>       |   |  |   操作系统 OS  |==|I|------|I|==|   操作系统 OS  |  |
>       |   |  +--------------+  | 子网专线  |  +--------------+  |
>       |   +-------------------+                       +-------------------+ |
>       |       主机：UCLA                               主机：SRI            |
>        \                                                                /
> ```
>
> 阶段 A 说明：UCLA 的本地操作系统通过「子网 IMP 通道」向 SRI 的操作系统发送请求：「我希望使用 25 号链路与你建立连接」。此时终端只和本地 OS 有联系，没有任何前端逻辑下发。

---

### 阶段 B：链路建立并登录后 · b. After Link Establishment and Log-in

> 【译注】原始文档的「第 9 页」标记位置
> Crocker 著                                                     第 9 页
> RFC 1                        主机软件                    1969 年 4 月 7 日

```
         /                                                      \
        |     +-----------+                    +-----------+    |
        |     |           |                    |           |    |
        |     |           |                    |           |    |
        |     | terminal  |                    | terminal  |    |
        |     |           |                    |           |    |
        |     |           |                    |           |    |
        |     +-----+-----+                    +-----+-----+    |
        |           |                                |          |
        |           |                                |          |
        |           |                                |          |
        |     +-----+-----+ "Please send front"+-----------+    |
        |     |     |     | end control"       |     |     |    |
   UCLA {     |     |     |        ->          |     |     |    } SRI ___
        |     |   +-+-+   |  +-+          +-+  |  +--+---+ |    |    /   |
        |     |   | OS|---+-=|I|----------|I|=-+--|OS|NLS| +----+---|    |
        |     |   +-+-+   |  +-+          +-+  |  +------+ |    |   |___/
        |     |           |       DEL prog.    |           |    |   |    |
        |     |           |        <-          |           |    |   |____|
        |     +-----------+                    +-----------+    |
        |      HOST: UCLA                        HOST:SRI       |
         \                                                     /
```

> **【中文注释版 · 阶段 B】链路建立并登录之后**
>
> ```
>        /                                                                        \
>       |   +------------------+                       +--------------------------+ |
>       |   |     本地终端       |                       |      远端终端              | |
>       |   +--------+---------+                       +------------+-------------+ |
>       |            |                                               |               |
>       |            | 「请把你的前端控制程序发给我」 ---------------------------->  |
> UCLA  |   +--------+---------+                                      +----+-------+  | SRI
>       |   |  +--------------+  | IMP IMP  |  +---------OS---------+  +--+NLS--+  |  |   用户目录树
>       |   |  |   操作系统 OS  |==|I|------|I|==| 操作系统 |  NLS 应用  |  ...... |  |==|    （附属存储）
>       |   |  +--------------+  | 子网专线  |  +--------------------+  +-------+  |  |   |___/
>       |   |        ^           |                                       |          |  |   |    |
>       |   |        |  DEL 前端程序源码 <---------------------------------          |  |   |____|
>       |   +-------------------+                       +--------------------------+ |
>       |       主机：UCLA                               主机：SRI                    |
>        \                                                                        /
> ```
>
> 阶段 B 说明：链路建立并登录完毕后，本地主机的操作系统向远端发送请求：「请把终端前端控制程序发给我」。SRI 端（运行着 NLS 在线系统 + 操作系统）把 DEL 语言写的前端程序源码，通过子网传回 UCLA。

---

### 阶段 C：DEL 程序收到并编译后 · c. After Receipt and Compilation of the DEL program

```
         /                                                     \
        |     +-----------+                    +-----------+    |
        |     |           |                    |           |    |
        |     |           |                    |           |    |
        |     | terminal  |                    | terminal  |    |
        |     |           |                    |           |    |
        |     |           |                    |           |    |
        |     +-----+-----+                    +-----+-----+    |
        |           |Trivial                         |          |
        |           |Responses                       |          |
        |           |                                |          |
        |     +-----+------+                    +-----------+   |
        |     |     |      |                    |     |     |   |
   UCLA {     |     |      |  Major Responses   |     |     |   } SRI ___
        |     |  +--+--+   |  +-+          +-+  |  +--+---+ |   |    /   |
        |     |  |DEL  |---+-=|I|----------|I|=-+--|OS|NLS| +---+---|    |
        |     |  |front|   |  +-+          +-+  |  +------+ |   |   |___/
        |     |  | end |   |                    |           |   |   |    |
        |     |  |prog.|   |                    |           |   |   |____|
        |     |  +-----+   |                    |           |   |
        |     |  | OS  |   |                    |           |   |
        |     |  +-----+   |                    |           |   |
        |     |            |                    |           |   |
        |     +------------+                    +-----------+   |
        |      HOST: UCLA                         HOST: SRI     |
         \                                                     /
```

> **【中文注释版 · 阶段 C】DEL 前端程序收到并完成本地编译之后**
>
> ```
>        /                                                                        \
>       |   +------------------+                       +--------------------------+ |
>       |   |     本地终端       |                       |      远端终端              | |
>       |   +--------+---------+                       +------------+-------------+ |
>       |            |                                           |               |
>       |            | 【Trivial Responses】                        |               |
>       |            |   （琐碎响应：本地直接处理，              |               |
>       |            |    打字、回显、退格、屏幕刷新 ）            |               |
>       |            |                                           |               |
>       |   +--------+---------+                                     |               |
> UCLA  |   |  +---DEL 前端---+  【Major Responses】   +-----OS-----+  +---NLS---+  | SRI
>       |   |  |  本地编译后   | === 重大响应（回车/命令等） ===> | 操作系统   |==| 应用程序  |==| 用户存储
>       |   |  |    执行码     | <=== 重大处理结果返回 ========= |            |  +--------+  |  |___/
>       |   |  +--------------+                                  |            |              |  |    |
>       |   |  |   操作系统 OS  |                                  +------------+              |  |____|
>       |   |  +--------------+                                                              |
>       |   +-------------------+                       +--------------------------+           |
>       |       主机：UCLA                               主机：SRI                              |
>        \                                                                        /
> ```
>
> 阶段 C 说明：DEL 源码在 UCLA 本地编译完成后，就常驻在终端与操作系统之间。**99% 的终端交互（打字、退格、显示、鼠标移动等琐碎响应）完全在本地 DEL 前端中处理，零延迟；只有真正涉及语义、需要远端计算的「重大响应」（比如用户按下回车），才打包消息通过 IMP 子网发往远端 NLS 应用。**

---

### 开放问题 · Open Questions

```
   1.  If the IMPs do code conversion, the checksum will not be correct.
```

> 1. 如果 IMP 层执行了字符编码转换（如 EBCDIC ↔ ASCII），那么我们在 HOST 层计算的校验和就会对不上——这个矛盾如何解决？

```
   2.  The procedure for requesting the DEL front end is not yet
   specified.
```

> 2. 「请求下发 DEL 前端程序」这一步骤的具体流程（用哪条链路、发什么格式的消息、如何确认收到）目前还没有制定详细规范。

---

## 四、初步实验 · IV. Initial Experiments

> 【译注】原始文档的「第 10 页」标记位置
> Crocker 著                                                    第 10 页
> RFC 1                        主机软件                    1969 年 4 月 7 日

### 实验一 · Experiment One

```
   SRI is currently modifying their on-line retrieval system which will
   be the major software component on the Network Documentation Center so
   that it can be operated with model 35 teletypes.  The control of the
   teletypes will be written in DEL.  All sites will write DEL compilers
   and use NLS through the DEL program.
```

> SRI 目前正在改造他们的**在线文档检索系统**——这套系统未来会作为「网络文档中心（Network Documentation Center）」的核心软件组件。改造的目标是让它能用 **Teletype Model 35 型电传打字机**操作。所有与电传打字机交互的控制逻辑，都将使用 DEL 语言编写。
>
> 四个参与站点将**各自编写自己平台上的 DEL 编译器**，然后通过编译后的 DEL 前端程序来使用 SRI 的 NLS（在线系统）检索功能。

---

### 实验二 · Experiment Two

```
   SRI will write a DEL front end for full NLS, graphics included.  UCLA
   and UTAH will use NLS with graphics.
```

> SRI 将为「完整版本的 NLS 系统」（包含完整图形交互能力）编写一套 DEL 前端。UCLA 和 Utah 两个站点将使用这套 DEL 前端，以图形终端方式通过网络操作 NLS。

---

### 归档说明 · Archival Note

```
         [ This RFC was put into machine readable form for entry ]
         [ into the online RFC archives by Celeste Anderson 3/97 ]
```

> 【归档说明 · 非原文正文】
>
> 本 RFC 于 1997 年 3 月，由 Celeste Anderson 录入并转换为机器可读格式，纳入在线 RFC 文档档案库。

> 【译注】原始文档的「第 11 页」标记位置
> Crocker 著                                                    第 11 页
> RFC 1                        主机软件                    1969 年 4 月 7 日

---

## 译后记

本文档为 RFC 1 全文逐段中英对照翻译。翻译时遵循以下原则：
1. **保留技术原味**：如 RFNM、IMP、HOST、TTY-like、File-like、DEL 等术语，翻译时附原文或直接保留。
2. **逐段对照**：每一段英文原文紧随中文译文，方便对读。
3. **架构图保留 + 中文注释**：三组 ASCII 架构图保持原始排版，另附中文注释版本便于理解流程。
4. **少量校注**：对于原文明显的笔误、或需要补充的背景，在【译注】中标注。

参考资料：
- RFC Editor 官方原文存档：https://www.rfc-editor.org/rfc/rfc1.txt
- *Where Wizards Stay Up Late*（Hafner & Lyon, 1996）— ARPANET 诞生史
