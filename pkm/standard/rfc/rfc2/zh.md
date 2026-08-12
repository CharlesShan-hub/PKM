# RFC 2 — Host Software（主机软件）
> **中英对照翻译版本**
> 原文作者：Bill Duvall（SRI 斯坦福研究院）
> 原文发布日期：1969 年 4 月
> 翻译说明：本文件采用「英文原文在上，中文翻译在下」的逐段对照格式。专业术语首次出现时附原文；编号条款结构保留原文层次；ASCII 图保持原图，附中文标注。

---

## 文头 · Header

```
Network Working Group                                        Bill Duvall
Request for Comments: 2                                              SRI

                            [unknown title]

[page 1 missing]
```

> 网络工作组                                               比尔·杜瓦尔（Bill Duvall）
> 请求评论：第 2 号                                      斯坦福研究院（SRI）
>
>                                                   【标题未知】
>
>                                                   【第 1 页缺失】

【译注】这份 RFC 的第一页丢了（[page 1 missing]），连标题都没留下来，所以全文直接从 "1 LINKS" 开始。1969 年文档管理的日常。

---

## 1 链路 · LINKS

```
   1a Control Links
```

> **1a 控制链路（Control Links）**

```
      1a1 Logical link 0 will be a control link between any two HOSTs on
      the network
```

> 1a1 逻辑链路 0 将是网络上任意两个 HOST 之间的控制链路。

```
         1a1a Only one control link may exist between any two HOSTs on
         the network. Thus, if there are n HOSTs on the network, there
         are n-1 control links from each HOST.
```

> 1a1a 网络上任意两个 HOST 之间只能存在一条控制链路。因此，如果网络上有 n 台 HOST，那么每台 HOST 都有 n-1 条控制链路。

```
      1a2 It will be primarily used for communication between HOSTs for
      the purposes of:

         1a2a Establishing user links

         1a2b Breaking user links

         1a2c Passing interrupts regarding the status of links and/or
         programs using the links

         1a2d Monitor communication
```

> 1a2 控制链路主要用于 HOST 之间的通信，用途包括：
>
> 1a2a 建立用户链路
>
> 1a2b 断开用户链路
>
> 1a2c 传递有关链路状态及使用链路的程序状态的中断信息
>
> 1a2d 监控（Monitor）通信

```
      1a3 Imps in the network may automatically trace all messages sent
      on link 0.
```

> 1a3 网络中的 IMP 可以自动追踪链路 0 上发送的所有消息。

```
   1b Primary Links
```

> **1b 主链路（Primary Links）**

```
      1b1 A user at a given HOST may have exactly 1 primary link to each
      of the other HOSTs on the network.
```

> 1b1 某台 HOST 上的一个用户，可以与该网络上其他每台 HOST 各建立恰好 1 条主链路。

```
         1b1a The primary link must be the first link established
         between a HOST user and another HOST.
```

> 1b1a 主链路必须是某台 HOST 的用户与另一台 HOST 之间**最先建立**的链路。

```
         1b1b Primary links are global to a user, i.e. a user program
         may open a primary link, and that link remains open until it is
         specifically closed.
```

> 1b1b 主链路对用户而言是**全局的**：即用户程序可以打开一条主链路，且该链路会一直保持打开，直到被显式关闭。

```
         1b1c The primary link is treated like a teletype connected over
         a normal data-phone or direct line by the remote HOST, i.e. the
         remote HOST considers a primary link to be a normal teletype
         user.
```

> 1b1c 远端 HOST 会把主链路当成一台通过普通数据电话（data-phone）或专线连接进来的电传打字机（teletype）——即远端 HOST 将主链路视为一名普通的电传打字机用户。

```
         1b1d The primary link is used for passing (user) control
         information to the remote HOST, e.g. it will be used for
         logging in to the remote host (using the remote hosts standard
         login procedure).
```

> 1b1d 主链路用于向远端 HOST 传递（用户的）控制信息，例如：用它登录远端主机（走远端主机标准的登录流程）。

```
   1c Auxilliary Links
```

> **1c 辅助链路（Auxiliary Links）**

```
      1c1 A user program may establish any number of auxilliary links
      between itself and a user program in a connected HOST.
```

> 1c1 用户程序可以在自己与已连接 HOST 上的用户程序之间，建立任意数量的辅助链路。

```
         1c1a These links may be used for either binary or character
         transmission.
```

> 1c1a 这些链路既可以用于二进制传输，也可以用于字符传输。

```
         1c1b Auxilliary links are local to the sub-system which
         establishes them, and therefore are closed when that subsystem
         is left.
```

> 1c1b 辅助链路**局部于**建立它的子系统——因此当离开该子系统时，这些链路就会被关闭。

---

## 2 链路的操纵 · MANIPULATION OF LINKS

```
   2a Control links
```

> **2a 控制链路（Control Links）**

```
      2a1 The control link is established at system load time.
```

> 2a1 控制链路在系统加载（启动）时建立。

```
      2a2 The status of a control link may be active or inactive
```

> 2a2 控制链路的状态可以是「激活」或「未激活」。

```
         2a2a The status of the control link should reflect the
         relationship between the HOSTs.
```

> 2a2a 控制链路的状态应当反映两台 HOST 之间的关系。

```
   2b Primary Links
```

> **2b 主链路（Primary Links）**

```
      2b1 Primary links are established by a user or executive call to
      the monitor
```

> 2b1 主链路由用户或执行程序（executive）调用监控程序（monitor）来建立。

```
         2b1a The network identification number of the HOST to be linked
         to must be included in the call
```

> 2b1a 调用中必须包含目标 HOST 的网络标识号（ID）。

```
         2b1b An attempt to establish more than one primary link to a
         particular HOST will be regarded as an error, and the request
         will be defaulted
```

> 2b1b 试图对同一台 HOST 建立超过一条主链路将被视为错误，该请求会被拒绝（defaulted）。

```
         2b1c Standard Transmission Character Set
```

> **2b1c 标准传输字符集（Standard Transmission Character Set）**

```
            2b1c1 There will be a standard character set for
            transmission of data over the primary links and control
            links.

               2b1c1a This will be full (8 bit) ASCII.
```

> 2b1c1 主链路和控制链路上传输数据时，将使用一套标准字符集。
>
> 2b1c1a 这套标准就是完整的 **8 位 ASCII**。

```
         2b1d (get link) The protocol for establishing a link to HOST B
         from HOST A is as follows
```

> **2b1d（获取链路 get link）** 从 HOST A 到 HOST B 建立链路的协议如下：

```
            2b1d1 A selects a currently unused link to HOST B from its
            allocation tables
```

> 2b1d1 A 从自己的分配表中，选择一条当前未使用的、通向 HOST B 的链路。

```
            2b1d2 A transmits a link-connect message to B over link 0.
```

> 2b1d2 A 通过链路 0 向 B 发送一条「链路连接」消息。

```
            2b1d3 A then waits for:

               2b1d3a A communication regarding that link from B

               2b1d3b A certain amount of time to elaspse
```

> 2b1d3 随后 A 等待以下两者之一：
>
> 2b1d3a 来自 B 的、关于该链路的通信消息
>
> 2b1d3b 一段指定时间的流逝（超时）

【译注】原文 "elaspse" 为 "elapse"（流逝）的笔误。

```
            2b1d4 If a communication regarding the link is received from
            B, it is examined to see if it is:

               2b1d4a A verification of the link from B.

                  2b1d4a1 This results in a successful return from the
                  monitor to the requestor. The link number is returned
                  to the requestor, and the link is established.

               2b1d4b A request from B to establish the link. This
               means: that B is trying to establish the same link as A
               independently of A.

                  2b1d4b1 If the network ID number of A(Na) is greater
                  than that of B(Nb), then A ignores the request, and
                  continues to await confirmation of the link from B.

                  2b1d4b2 If, on the other hand, Na<Nb, A:

                     2b1d4b2a Honors the request from B to establish the
                     link,

                     2b1d4b2b Sends verification as required,

                     2b1d4b2c Aborts its own request, and repeats the
                     allocation process.

               2b1d4c Some other communication from B regarding the
               link.

                  2b1d4c1 This is an error condition, meaning that
                  either:

                     2b1d4c1a A has faulted by selecting a previously
                     allocated link for allocation,

                     2b1d4c1b B is transmitting information over an un-
                     allocated link,

                     2b1d4c1c Or a message regarding allocation from B
                     to A has been garbled in transmission.

                  2b1d4c2 In this case, A's action is to:

                     2b1d4c2a Send a link disconnect message to B
                     concerning the attempted connection

                     2b1d4c2b Consider the state of HOST B to be in
                     error and initiate entry to a panic routine(error).
```

> 2b1d4 如果收到了来自 B 的、关于该链路的通信消息，则检查它属于哪种情况：
>
> **2b1d4a B 对该链路的确认（verification）。**
>
> 2b1d4a1 这导致监控程序向请求方成功返回：链路号返回给请求方，链路建立完成。
>
> **2b1d4b B 发来的建链请求。** 这意味着：B 正在独立地尝试建立与 A 相同的链路（撞车了）。
>
> 2b1d4b1 如果 A 的网络 ID（Na）大于 B 的（Nb），则 A 无视该请求，继续等待来自 B 的链路确认。
>
> 2b1d4b2 反之，如果 Na < Nb，则 A 需要：
>
> > 2b1d4b2a 接受（honors）B 的建链请求，
> >
> > 2b1d4b2b 按要求发送确认，
> >
> > 2b1d4b2c 放弃自己的请求，并重新执行链路分配流程。
>
> 【译注】这就是「ID 小的让」冲突仲裁规则：ID 较小的主机主动退让、成全对方，然后自己另选链路重来。与 RFC 1 的设计完全一致。
>
> **2b1d4c 来自 B 的、关于该链路的其他通信消息。**
>
> 2b1d4c1 这是错误状态，意味着以下三种情况之一：
>
> > 2b1d4c1a A 出错——选择了一条已经被分配的链路进行分配；
> >
> > 2b1d4c1b B 在一条未分配的链路上传输信息；
> >
> > 2b1d4c1c 或者 B 发给 A 的关于分配的某条消息在传输中被破坏（garbled）。
>
> 2b1d4c2 这种情况下，A 的动作是：
>
> > 2b1d4c2a 就这次尝试的连接，向 B 发送一条「链路断开」消息；
> >
> > 2b1d4c2b 认为 HOST B 处于错误状态，并进入恐慌例程（panic routine，错误处理）。

```
            2b1d5 If no communication regarding the link is received
            from B in the prescribed amount of time, HOST B is
            considered to be in an error state.

                  2b1d5a A link disconnect message is sent to B from A.

                  2b1d5b A panic routine is called(error).
```

> 2b1d5 如果在规定时间内没有收到来自 B 的任何关于该链路的通信消息，则认为 HOST B 处于错误状态。
>
> 2b1d5a A 向 B 发送一条「链路断开」消息。
>
> 2b1d5b 调用恐慌例程（错误处理）。

```
   2c Auxilliary Links
```

> **2c 辅助链路（Auxiliary Links）**

```
      2c1 Auxilliary links are established by a call to the monitor from
      a user program.

         2c1a The request must specify pertinent data about the desired
         link to the monitor

            2c1a1 The number of the primary link to B.

         2c1b The request for an auxilliary link must be made by a user
         program in each of the HOSTs (A and B).

         2c1c If Na > Nb, then HOST A proceeds to establish a link to
         HOST B in the manner outlined above (getlink).

         2c1d If Na<Nb, then A waits:

            2c1d1 For HOST B to establish the link (after looking to see
            if B has already established the corresponding link).

            2c1d2 For a specified amount of time to elapse.

               2c1d2a This means that HOST B did not respond to the
               request of HOST A.

               2c1d2b The program in HOST A and B should be able to
               specifiy the amount of time to wait for the timeout.
```

> 2c1 辅助链路由用户程序调用监控程序来建立。
>
> 2c1a 请求中必须向监控程序说明所期望链路的相关数据：
>
> > 2c1a1 通向 B 的主链路号。
>
> 2c1b 辅助链路的请求必须由两台 HOST（A 和 B）各自的用户程序分别发出。
>
> 2c1c 如果 Na > Nb，则 HOST A 按上述 getlink 流程向 HOST B 建立链路。
>
> 2c1d 如果 Na < Nb，则 A 等待：
>
> > 2c1d1 等待 HOST B 来建立这条链路（先检查 B 是否已经建立了对应的链路）。
> >
> > 2c1d2 等待一段指定的时间流逝（超时）。
> >
> > > 2c1d2a 这意味着 HOST B 没有响应 HOST A 的请求。
> > >
> > > 2c1d2b A 和 B 中的程序应当能够指定超时等待的时间长度。

---

## 3 错误检查 · ERROR CHECKING

```
   3a All messages sent over the network will be error checked initally
   so as to help isolate software and hardware bugs.
```

> 3a 网络上发送的所有消息最初都要做错误检查，以便帮助隔离软件和硬件 bug。

```
   3b A checksum will be associated with each message, which is order
   dependent.
```

> 3b 每条消息都要附带一个校验和（checksum），并且这个校验和是**顺序相关**的（order dependent）。

```
      3b1 The following algorithm is one which might be used:

         3b1a A checksum of length 1 may be formed by adding successive
         fields in the string to be checked serially, and adding the
         carry bit into the lowest bit position of the sum.
```

> 3b1 以下是一种可用的算法：
>
> 3b1a 长度为 1 的校验和可以这样生成：把待校验字符串中的各字段串行地依次相加，并把进位位（carry bit）加到和的**最低位**上。

```
              +--------------+
              |              |
              +---FIELD 1----+

          ADD +--------------+
              |              |
              +----FIELD 2---+

            +-+--------------+
            | |              |
            +-+--------------+
              \
               \          +--+
          ADD   CARRY---> |  |
                          +--+

              +--------------+
              |              |
              +----RESULT----+
```

> 上图：字段 1 加字段 2，把产生的进位（CARRY）回加到最低位，得到结果（RESULT）。

```
            3b1a1 This process is known as folding.
```

> 3b1a1 这个过程称为「折叠」（folding）。

```
            3b1a2 Several fields may be added and folded in parallel, if
            they are folded appropiately after the addition.
```

> 3b1a2 如果相加之后恰当地进行折叠，多个字段也可以并行相加并折叠。

```
              +---------+---------+---------+---------+
              | FIELD 4 | FIELD 3 | FIELD 2 | FIELD 1 |
              +---------+---------+---------+---------+

              +---------+---------+---------+---------+
              | FIELD 8 | FIELD 7 | FIELD 6 | FIELD 5 |
              +---------+---------+---------+---------+
            ADD
            +-+---------+---------+---------+---------+
            | |         |         |         |         |
            +-+---------+---------+---------+---------+
             |      |        |         |         |
             |      |        |         |         v
             |      |        |         |    +---------+
             |      |        |         |    |         |
             |      |        |         |    +---------+
             |      |        |         |
             |      |        |         \    +---------+
             |      |        |          `-> |         |
             |      |        |              +---------+
             |      |        |
             |      |        \              +---------+
             |      |         `-----------> |         |
             |      |                       +---------+
             |      |
             |      \                       +---------+
             |       `--------------------->|         |
             |                              +---------+
             |
             \                                    +---+
              `-----CARRY------------------------>|   |
                                                  +---+
                                  ADD
                                  +---------+---------+
                                  |         |         |
                                  +--CARRY--+---------+
                                       |
                                       \        +-----+
                                    ADD `-----> |     |
                                                +-----+

                                            +---------+
                                            |         |
                                            +-RESULT--+
```

> 上图：8 个字段两行并行相加，把各列的进位（CARRY）回卷（fold）到结果（RESULT），再进行二次进位回卷。

```
                  3b1a2a Using this scheme, it is assumed that, if there
                  are n fields, the carries from the first n-1 fields
                  are automatically added into the low order position of
                  the next higher field, so that in folding, one need
                  only add the [n] result fields to the carry from the
                  nth field, and then add in an appropiately sized carry
                  from that addition (and repeat the desired number of
                  times to achieve the result.
```

> 3b1a2a 使用这个方案时，假设有 n 个字段：前 n-1 个字段产生的进位会自动进入下一个更高位字段的低位位置；因此在折叠时，只需把 [n] 个结果字段与第 n 个字段产生的进位相加，再把这次加法产生的大小合适的进位也加进去（并按需要重复数次）即可得到结果。

```
            3b1a3 A checksum computed in this manner has the advantage
            that the word lengths of different machines may each be used
            optimally:

               3b1a3a If a string of suitable length is chosen for
               computing the checksum, and a suitable checksum field
               length is selected, the checksum technique for each of
               the machines will be relatively optimal.

                  3b1a3a1 Field length: 288 bits (lowest common
                  denomenator of (24,32,36)

                  3b1a3a2 Checksum length: 8 bits (convenient field size
                  for all machines)
```

> 3b1a3 以这种方式计算的校验和有一个优点：**不同机器的字长都可以得到最优利用**：
>
> 3b1a3a 如果为校验和计算选择了合适的字符串长度、并选择了合适的校验和字段长度，那么每台机器上的校验技术都会是相对最优的。
>
> > 3b1a3a1 字段长度：**288 bits**（即 24、32、36 的最小公倍数）
> >
> > 3b1a3a2 校验和长度：**8 bits**（对所有机器都方便的字段大小）

【译注】288 = lcm(24, 32, 36)：因为四站主机字长不同（UCLA 的 Sigma 7 是 32 位、SRI 的 SDS 940 是 24 位、Utah 的 PDP-10 是 36 位），选最小公倍数做字段长度，能让每台机器都整数次对齐、各自最优。

```
         3b1b If a message is divided into groups of fields, and each
         group is checksummed in this manner, an order dependent
         checksum may be got by shifting the checksum for each group,
         and adding it in (successively) to the checksum of the next
         group
```

> 3b1b 如果把一条消息分成若干字段组、每组都用这种方式计算校验和，那么就可以得到一个**顺序相关**的校验和：把每一组的校验和循环移位（shifting）后，再（依次）加到下一组的校验和上。

【译注】这和 RFC 1 的「每 1152 bits 右旋一位」是同一家族的设计：把「块边界」信息编码进校验和，专门对付「包顺序调换」类错误。

```
   3c A facility will be provided where two HOSTs may enter a mode which
   requires positive verification of all messages. This verification is
   sent over the control link.
```

> 3c 将提供一种机制：两台 HOST 可以进入一个要求**对所有消息进行正验证（positive verification）**的模式。这种验证通过控制链路发送。

---

## 4 监控程序功能 · MONITOR FUNCTIONS

```
   4a Network I/O drivers
```

> **4a 网络 I/O 驱动（Network I/O Drivers）**

```
      4a1 Input
```

> **4a1 输入（Input）**

```
         4a1a Input message from IMP.

         4a1b Do error checking on message.

            4a1b1 Verify checksum,

            4a1b2 Send "message recieved" aknowledgement over control
            link if aknowledge mode is in effect.

         4a1c (trans)character translation

            4a1c1 There is a strong possibility that the character
            translation may be done in the IMP.

            4a1c2 This needs to be explored further with BBN.

            4a1c3 There are two main considerations

               4a1c3a Should the translation be done by table or
               algorithm?

                  4a1c3a1 Initially it seems as though the best way to
                  go is table.

               4a1c3b How should we decide which messages should be
               translated, i.e. is it desirable to not translate
               everything (YES!!) and by what means can we use to
               differentiate?

         4a1d Decode header, and pass message to correct recipient as
         identified by source, and link.
```

> 4a1a 从 IMP 输入消息。
>
> 4a1b 对消息做错误检查。
>
> > 4a1b1 校验校验和；
> >
> > 4a1b2 如果「确认模式」（acknowledge mode）生效，则通过控制链路发送「消息已收到」的确认。
>
> 4a1c （trans）字符翻译。
>
> > 4a1c1 字符翻译很有可能可以在 IMP 内部完成。
> >
> > 4a1c2 这点需要与 BBN 进一步探讨。
> >
> > 4a1c3 有两个主要的考虑：
> >
> > > 4a1c3a 翻译应该用查表（table）还是算法（algorithm）？
> > >
> > > 4a1c3a1 一开始看来，最好采用查表方式。
> > >
> > > 4a1c3b 我们应该如何决定哪些消息需要翻译？即：不对所有消息做翻译是不是更好（**是的！！**），以及用什么手段来区分它们？
>
> 4a1d 解码头部，并按消息头标识的源（source）和链路（link），把消息交给正确的接收者。

```
      4a2 Output
```

> **4a2 输出（Output）**

```
         4a2a Build header

         4a2b Character translation

            4a2b1 See remarks under the section on output translation
            (trans).

         4a2c Create checksum

         4a2d Check status of link

            4a2d1 If there has not been a RFNM since the last message
            transmitted out the link, wait for it.

         4a2e Transmit message to IMP

         4a2f If aknowledge mode is in effect,wait for

            4a2f1 RFNM from destination IMP.

            4a2f2 Response from destination HOST over control line 0.
```

> 4a2a 构建头部。
>
> 4a2b 字符翻译。
>
> > 4a2b1 参见上文 4a1c（trans）关于输出翻译的备注。
>
> 4a2c 生成校验和。
>
> 4a2d 检查链路状态。
>
> > 4a2d1 如果自上次在该链路上发送消息以来还没有收到 RFNM，则等待它。
> >
> > 【译注】RFNM = Request For Next Message，即「可以发下一条了」的流控确认。
>
> 4a2e 向 IMP 发送消息。
>
> 4a2f 如果「确认模式」生效，则等待：
>
> > 4a2f1 目的端 IMP 的 RFNM；
> >
> > 4a2f2 目的端 HOST 通过控制链路 0 发来的响应。

```
   4b Network status
```

> **4b 网络状态（Network Status）**

```
      4b1 Maintain status of other HOSTs on network

         4b1a If an IMP is down, then his HOST is considered to be down.

      4b2 Maintain status of control lines.

      4b3 Answer status queries from other HOSTs.

      4b4 Inform other HOSTs as to status of primary and auxilliary
      links on an interrupt basis.

      4b5 Inform other HOSTs as to status of programs using primary and
      secondary links
```

> 4b1 维护网络上其他 HOST 的状态。
>
> > 4b1a 如果某台 IMP 宕机，则认为它的 HOST 也宕机了。
>
> 4b2 维护控制链路的状态。
>
> 4b3 回答其他 HOST 发来的状态查询。
>
> 4b4 以中断方式通知其他 HOST：主链路和辅助链路的状态。
>
> 4b5 通知其他 HOST：使用主链路和辅助链路的程序的状态。

---

## 5 执行原语 · EXECUTIVE PRIMITIVES

```
   5a Primary Links
```

> **5a 主链路（Primary Links）**

```
      5a1 These require the HOST number as a parameter.

         5a1a Establish primary link

         5a1b Connect controlling teletype to primary link

         5a1c INPUT/OUTPUT over primary link

         5a1d Interrogate status of primary link

            5a1d1 Don't know what, exactly, this should do, but it seems
            as though it might be useful.

         5a1e Disconnect controlling teletype from primary link

         5a1f Kill primary link
```

> 5a1 这些原语都需要以 HOST 号作为参数。
>
> 5a1a 建立主链路
>
> 5a1b 把控制电传打字机连接到主链路
>
> 5a1c 通过主链路进行输入/输出
>
> 5a1d 查询主链路的状态
>
> > 5a1d1 不太清楚这个具体该做什么，但看起来可能有用。
> >
> > 【译注】Duvall 的实诚话：列了个 API 却不知道它该干嘛——"好像会有用"。1969 年的工程文档就是这么坦诚。
>
> 5a1e 断开控制电传打字机与主链路的连接
>
> 5a1f 杀死（终止）主链路

```
   5b Auxilliary Links.
```

> **5b 辅助链路（Auxiliary Links）**

```
      5b1 Establish auxilliary link.

         5b1a requires the HOST number as a parameter

         5b1b It returns a logical link number which is similar to a
         file index. It is this number which is passed to all of the
         other Auxilliary routines as a parameter.

      5b2 INPUT/OUTPUT over auxilliary link

      5b3 Interrogate status auxilliary link.

         5b3a Don't know what, exactly, this should do, but it seems as
         though it might be useful.

      5b4 Kill auxilliary link.
```

> 5b1 建立辅助链路。
>
> > 5b1a 需要以 HOST 号作为参数；
> >
> > 5b1b 它返回一个逻辑链路号，类似于文件索引（file index）。后续所有其他辅助链路例程都把这个编号作为参数传入。
>
> 5b2 通过辅助链路进行输入/输出
>
> 5b3 查询辅助链路状态
>
> > 5b3a 不太清楚这个具体该做什么，但看起来可能有用。
>
> 5b4 杀死（终止）辅助链路

```
   5c Special executive functions
```

> **5c 特殊执行功能（Special Executive Functions）**

```
      5c1 Transparent. INPUT/OUTPUT over link

         5c1a This may be used to do block I/O transfers over a link

         5c1b The function of the monitor in this instance is to
         transfer a buffer directly to its IMP

         5c1c At does not modify it in any way

            5c1c1 This means that the header and other control
            information must be in the buffer.

         5c1d The indended use of this is for network debugging.
```

> 5c1 透明（Transparent）的链路上输入/输出。
>
> > 5c1a 它可以用于在链路上进行块（block）I/O 传输；
> >
> > 5c1b 此时监控程序的功能是：把缓冲（buffer）直接交给它的 IMP；
> >
> > 5c1c 而且监控程序不以任何方式修改它；
> >
> > > 5c1c1 这意味着：消息头和所有其他控制信息都必须放在缓冲区里。
> >
> > 5c1d 此功能的预期用途是**网络调试**。

【译注】这就是"裸管道"：监控层完全不碰数据，头部都让调用者自己拼。今天的 raw socket / AF_PACKET 就是它的后代。

---

## 6 初始联调 · INITIAL CHECKOUT

```
   6a The network will be initially checked out using the links in a
   simulated data-phone mode.

      6a1 All messages will be one character in length.

      6a2 Links will be transparent to the monitor, and controlled by
      user program via a special executive primitive.

         6a2a The initial test will be run from two user programs in
         different HOSTs, e.g. DDT to DDT.

         6a2b It will be paralleled by a telephone link or similar.
```

> 6a 网络最初将使用「模拟数据电话模式」（simulated data-phone mode）下的链路进行联调。
>
> 6a1 所有消息的长度都是一个字符。
>
> 6a2 链路对监控程序透明（transparent），由用户程序通过一个特殊的执行原语来控制。
>
> > 6a2a 初始测试将在不同 HOST 上的两个用户程序之间进行，例如 **DDT 对 DDT**。
> > >
> > > 【译注】DDT（Dynamic Debugging Technique）是那个年代的调试器，相当于 1969 年的 gdb。
> >
> > 6a2b 测试将并行地由一条电话线路（或类似物）作对照。

【译注】"模拟数据电话模式 + 一次一个字符 + 电话线人肉对照"——把最慢、最原始的路径先跑通，再谈效率。这就是最小可用实验（MVP）在 1969 年的样子。

---

```
          [  This RFC was put into machine readable form for entry  ]
          [  into the online RFC archives by Robbie Bennet 10/1998  ]
          [  This RFC was nroffed by Kelly Tardif, Viagenie 10/1999 ]
```

> 【归档说明】这份 RFC 由 Robbie Bennet 于 1998 年 10 月录入为机器可读形式，收入在线 RFC 档案；1999 年 10 月由 Viagenie 公司的 Kelly Tardif 做了 nroff 排版。

---

## 翻译说明

- 本文档以「英文原文在上（代码块）、中文译文在下（引用块）」的方式逐段对照，原文的编号条款层次（如 2b1d4b1）全部保留，便于对照查阅。
- 【译注】为译者补充的背景说明，帮助理解 1969 年的语境。
- 折叠校验和的 ASCII 图按原文保留原样（图内 FIELD 1~8、CARRY、RESULT 为图中元素，未翻译以保持排版）。
