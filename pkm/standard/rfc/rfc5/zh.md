# RFC 5 — DEL（Decode-Encode Language，解码-编码语言）
> **中英对照翻译版本**
> 原文作者：Jeff Rulifson（SRI 斯坦福研究院）
> 原文发布日期：1969 年 6 月 2 日
> 翻译说明：本文件采用「英文原文在上，中文翻译在下」的逐段对照格式。形式语法部分保留原文（元符号记法），附中文说明；ASCII/符号块保持原样。

---

## 文头 · Header

```
Network Working Group                                           4691
RFC-5                                                           Jeff Rulifson
                                                                June 2, l969
```

> 网络工作组                                                    4691
> RFC 第 5 号                                                  杰夫·鲁利夫森（Jeff Rulifson）
>                                                               1969 年 6 月 2 日
>
> 【译注】原文日期写作 "l969"（以字母 l 代替数字 1），系打字错误，实为 1969 年。

---

## DEL

```
                                DEL
```

> 解码-编码语言（DEL）

---

## 文档开头：DEL 程序片段

```
:DEL, 02/06/69 1010:58   JFR   ;   .DSN=1; .LSP=0; ['=] AND NOT SP ; ['?];
dual transmission?
```

> 【译注】这是文档作者 Jeff Rulifson 在 SRI 的 NLS 系统上编写本文时留下的 DEL 代码示例开头：第一行带时间戳（02/06/69 1010:58）与作者缩写（JFR），是一段 DEL 程序语句；第二行 "dual transmission?"（双路传输？）是作者随手写下的疑问备注。两行均保留原样。

---

## ABSTRACT（摘要）

```
   The Decode-Encode Language (DEL) is a machine independent language
   tailored to two specific computer network tasks:

      accepting input codes from interactive consoles, giving immediate
      feedback, and packing the resulting information into message 
      packets for network transmissin.

      and accepting message packets from another computer, unpacking
      them, building trees of display information, and sending other
      information to the user at his interactive station.

   This is a working document for the evolution of the DEL language.
   Comments should be made through Jeff Rulifson at SRI.
```

> 解码-编码语言（DEL）是一种与机器无关（machine independent）的语言，专为两个特定的计算机网络任务而量身定制：
>
> - 接受来自交互式控制台的输入代码，给出即时反馈，并将所得信息打包成消息包（message packet）以供网络传输。
> - 以及接受来自另一台计算机的消息包，将其拆包，构建显示信息树，并将其他信息发送给在其交互工位（interactive station）上的用户。
>
> 这是一份用于 DEL 语言演进的进行中工作文档（working document）。意见应通过 SRI 的杰夫·鲁利夫森（Jeff Rulifson）转达。
>
> 【译注】原文 "transmissin" 为 "transmission"（传输）的打字错误。

---

## FORWARD（前言）

```
   The initial ARPA network working group met at SRI on October 25-26,
   1968.

      It was generally agreed beforehand that the runmning of interactive
      programs across the network was the first problem that would be
      faced.

      This group, already in agreement about the underlaying notions of
      a DEL-like approach, set down some terminology, expectations for
      DEL programs, and lists of proposed semantic capability.

      At the meeting were Andrews, Baray, Carr, Crocker, Rulifson, and
      Stoughton.

   A second round of meetings was then held in a piecemeal way.

      Crocker meet with Rulifson at SRI on November 18, 1968.  This
      resulted in the incorporation of formal co-routines.

      and Stoughton meet with Rulifson at SRI on Decembeer 12, 1968.  It
      was decided to meet again, as a group, probably at UTAH, in late
      January 1969.

   The first public release of this paper was at the BBN NET meeting in
   Cambridge on February 13, 1969.
```

> 最初的 ARPA 网络工作组于 1968 年 10 月 25 日至 26 日在 SRI 举行会议。
>
> - 与会者事先已普遍同意：通过网络运行交互式程序将是第一个要面对的问题。
> - 该小组已经就类 DEL（DEL-like）方法的基本概念达成一致，并确定了一些术语、对 DEL 程序的期望，以及拟议的语义能力清单。
> - 与会者有 Andrews、Baray、Carr、Crocker、Rulifson 和 Stoughton。
>
> 随后以零散的方式举行了第二轮会议。
>
> - Crocker 于 1968 年 11 月 18 日在 SRI 与 Rulifson 会面。这次会面导致了正式协程（co-routines）的纳入。
> - Stoughton 于 1968 年 12 月 12 日在 SRI 与 Rulifson 会面。会议决定在 1969 年 1 月下旬再次以小组形式会面，地点很可能在犹他大学（UTAH）。
>
> 本文的首次公开发布是在 1969 年 2 月 13 日于剑桥举行的 BBN 网络会议上。
>
> 【译注】原文 "runmning"（运行）、"underlaying"（基础）、"Decembeer"（十二月）均为打字错误，翻译按正确意思处理。

---

## NET STANDARD TRANSLATORS（网络标准翻译器）

```
   NST   The NST library is the set of programs necessary to mesh
   efficiently with the code compiled at the user sites from the DEL
   programs it receives.  The NST-DEL approach to NET interactive system
   communication is intended to operate over a broad spectrum.

   The lowest level of NST-DEL usage is direct transmission to the
   server-host, information in the same format that user programs
   would receive at the user-host.

      In this mode, the NST defaults to inaction.  The DEL program
      does not receive universal hardware representation input but 
      input in the normal fashion for the user-host.

      And the DEL 1 program becomes merely a message builder and
      sender.

   A more intermediate use of NST-DEL is to have echo tables for a
   TTY at the user-host.

      In this mode, the DEL program would run a full duplex TTY for
      the user.

      It would echo characters, translate them to the character set 
      of the server-host, pack the translated characters in messages,
      and on appropriate break characters send the messages.

      When messages come from the server-host, the DEL program would
      translate them to the user-host character set and print them on
      his TTY.

   A more ambitious task for DEL is the operation of large,
   display-oriented systems from remote consoles over the NET.

      Large interactive systems usually offer a lot of feedback to
      the user.  The unusual nature of the feedback make it
      impossible to model with echo table, and thus a user program
      must be activated in a TSS each time a button state is changed.

         This puts an unnecessarily large load on a TSS, and if the
         system is being run through the NET it could easily load two
         systems.

         To avoid this double overloading of TSS, a DEL program will
         run on the user-host.  It will handle all the immediate
         feedback, much like a complicated echo table.  At appropriate
         button pushes, message will be sent to the server-host and
         display updates received in return.

      One of the more difficult, and often neglected, problems is the
      effective simulation of one nonstandard console on another non-
      standard console.

         We attempt to offer a means of solving this problem through
         the co-routine structure of DEL programs.  For the
         complicated interactive systems, part of the DEL programs
         will be constructed by the server-host programmers.
         Interfaces between this program and the input stream may
         easily be inserted by programmers at the user-host site.
```

> NST：NST 库是为与其所接收的、在用户站点由 DEL 程序编译出的代码高效衔接所必需的一组程序。NET 交互式系统通信的 NST-DEL 方法旨在跨越宽广的范围（broad spectrum）运作。
>
> NST-DEL 使用的最低层级是向服务器主机（server-host）直接传输信息，格式与用户程序在用户主机（user-host）上收到的格式相同。
>
> - 在这种模式下，NST 默认为不作为。DEL 程序收到的不是通用硬件表示形式的输入，而是用户主机常规方式下的输入。
> - 于是 DEL 程序仅仅成为一个消息构建器和发送器。
>
> NST-DEL 一个更中间层的用法是为用户主机上的电传打字机（TTY）配备回显表（echo table）。
>
> - 在这种模式下，DEL 程序将为用户运行一台全双工（full duplex）的 TTY。
> - 它会回显字符，把它们翻译成服务器主机的字符集，将翻译后的字符打包进消息，并在合适的断行字符（break character）处发送这些消息。
> - 当消息从服务器主机传来时，DEL 程序会将其翻译成用户主机字符集，并打印在用户的 TTY 上。
>
> DEL 一个更宏大的任务，是通过网络从远程控制台运行大型的、面向显示（display-oriented）的系统。
>
> - 大型交互式系统通常向用户提供大量反馈。反馈的非同寻常特性使其无法用回显表来建模，因此每当按钮状态改变时，就必须在一个分时系统（TSS）中激活一个用户程序。
>   - 这给 TSS 带来了不必要的大量负载；而且如果系统是经由 NET 运行的，它很容易同时压垮（load）两个系统。
>   - 为了避免这种对 TSS 的双重过载，一个 DEL 程序将运行在用户主机上。它将处理所有的即时反馈，很像一张复杂的回显表。在合适的按钮按下时，消息会被发送到服务器主机，并收到返回的显示更新。
>
> 较困难、也往往被忽视的问题之一，是如何有效地在一台非标准控制台上模拟另一台非标准控制台。
>
> - 我们试图通过 DEL 程序的协程结构为解决这一问题提供手段。对于复杂的交互式系统，DEL 程序的一部分将由服务器主机程序员构建。这个程序与输入流之间的接口，可以很容易地由用户主机站点的程序员插入。

---

## UNIVERSAL HARDWARE REPRESENTATION（通用硬件表示法）

```
   To minimize the number of translators needed to map any facility's
   user codes to any other facility, there is a universal hardware
   representation.

   This is simply a way of talking, in general terms, about all the
   hardware devices at all the interactive display stations in the initial
   network.

   For example, a display is thought of as being a square, the
   mid-point has coordinates (0.0), the range is -1 to 1 on both
   axes.  A point may now be specified to any accuracy, regardless of
   the particular number of density of rastor points on a display.

   The representation is discussed in the semantic explanations
   accompanying the formal description of DEL.
```

> 为了把任何设施的用户代码映射到任何其他设施所需的翻译器数量降到最低，人们定义了一种通用硬件表示法。
>
> 这不过是一种以通用术语谈论初始网络中所有交互式显示站的全部硬件设备的方式。
>
> 例如，一个显示器被设想为一个正方形，中点的坐标为 (0.0)，两个轴上的范围都是 -1 到 1。这样一来，无论显示器上光栅点的数量或密度如何，任何点都可以被指定到任意精度。
>
> 这种表示法在伴随 DEL 形式描述的语义说明中加以讨论。
>
> 【译注】原文 "rastor" 为 "raster"（光栅）的打字错误；"number of density" 疑为 "number or density"（数量或密度）之误。

---

## INTRODUCTION TO THE NETWORK STANDARD TRANSLATOR (NST)（网络标准翻译器（NST）导论）

```
   Suppose that a user at a remote site, say Utah, is entered in the
   AHI system and wants to run NLS.

   The first step is to enter NLS in the normal way.  At that time
   the Utah system will request a symbolic program from NLS.

      REP   This program is written in DEL.  It is called the NLS
      Remote Encode Program (REP).

      The program accepts input in the Universal Hardware
      Representation and translates it to a form usable by NLS.

      It may pack characters in a buffer, also do some local
      feedback.

   When the program is first received at Utah it is compiled and
   loaded to be run in conjunction with a standard library.

   All input from the Utah console first goes to the NLS NEP.  It is
   processed, parsed, blocked, translated, etc.  When NEP receives a
   character appropriate to its state it may finally initiate
   transfers to the 940.  The bits transferred are in a form
   acceptable to the 940, and maybe in a standard form so that the
   NLSW need not differentiate between Utah and other NET users.
```

> 假设某个远程站点（比方说犹他，Utah）的用户登录了 AHI 系统，并且想运行 NLS。
>
> 第一步是以正常方式进入 NLS。那时犹他系统会向 NLS 请求一个符号程序（symbolic program）。
>
> - REP：这个程序用 DEL 编写。它被称为 NLS 远程编码程序（Remote Encode Program，REP）。
> - 该程序接受通用硬件表示形式的输入，并将其翻译成 NLS 可用的形式。
> - 它可以把字符打包进缓冲（buffer），也可以做一些本地反馈。
>
> 当该程序第一次在犹他收到时，它被编译并加载，与一个标准库（standard library）配合运行。
>
> 来自犹他控制台的所有输入首先进入 NLS 的 NEP。它被处理、解析、分块、翻译等。当 NEP 收到一个与其状态相符的字符时，它最终可以发起向 940 的传输。传输的比特采用 940 可接受的形式，而且可能采用标准形式，这样 NLSW 就不必区分犹他用户和其他的 NET 用户。
>
> 【译注】① "AHI" 疑为原文如此（可能是 "NLS" 或某系统的别名）。② "940" 指 SDS 940 计算机。③ "NLS NEP" 与前面的 "NLS REP" 应为同一程序，疑为原文笔误（REP，Remote Encode Program）。④ "NLSW" 疑为 "NLS" 之误。

---

## ADVANTAGES OF NST（NST 的优势）

```
   After each node has implemented the library part of the NST, it
   need only write one program for each subsystem, namely the
   symbolic file it sends to each user that maps the NET hardware
   representation into its own special bit formats.

      This is the minimum programming that can be expected if 
      console is used to its fullest extent.

      Since the NST which runs the encode translation is coded at the
      user site, it can take advantage of hardware at its consoles to
      the fullest extent.  It can also add or remove hardware 
      features without requiring new or different translation tables
      from the host.

      Local users are also kept up to date on any changes in the system
      offered at the host site.  As new features are added,
      the host programmers change the symbolic encode program.  When
      this new program is compiled and used at the user site, the new
      features are automatically included.

   The advantages of having the encode translation programs
   transferred symbolically should be obvious.

      Each site can translate any way it sees fit.  Thus machine code
      for each site can be produced to fit that site; faster run
      times and greater code density will be the result.

      Moreover, extra symbolic programs, coded at the user site, may
      be easily interfaced between the user's monitor system and the
      DEL program from the host machine.  This should ease the
      problem of console extension (e.g. accommodating unusual keys and
      buttons) without loss of the flexibility needed for man-machine
      interaction.


   It is expected that when there is matching hardware, the symbolic
   programs will take this into account and avoid any unnecessary
   computing.  This is immediately possible through the code
   translation constructs of DEL.  It may someday be possible through
   program composition (when Crocker tells us how??)
```

> 在每个节点都实现了 NST 的库部分之后，每个子系统只需编写一个程序，即它发送给每个用户的、把 NET 硬件表示映射为自身专用比特格式的符号文件。
>
> - 这是在控制台被最充分利用时所能期望的最低限度的编程量。
> - 由于运行编码翻译的 NST 是在用户站点编码的，它可以最充分地利用其控制台的硬件。它还可以增加或移除硬件特性，而不需要主机提供新的或不同的翻译表。
> - 本地用户也能随时了解主机站点所提供的系统的任何变化。随着新功能的加入，主机程序员会修改符号编码程序。当这个新程序在用户站点被编译并使用后，新功能就自动被包含了。
>
> 以符号形式传输编码翻译程序的优势应该是显而易见的。
>
> - 每个站点都可以按自己认为合适的方式翻译。因此可以为每个站点生成适应该站点的机器代码；结果将是更快的运行时间和更高的代码密度。
> - 此外，在用户站点编写的额外符号程序，可以很容易地插入到用户的监控系统（monitor system）与来自主机机器的 DEL 程序之间。这应该能缓解控制台扩展（例如容纳不寻常的按键和按钮）的问题，而不丧失人机交互所需的灵活性。
>
> 可以预期，当硬件匹配时，符号程序会考虑到这一点，并避免任何不必要的计算。这可以立即通过 DEL 的代码翻译结构（code translation constructs）实现。有朝一日也许可以通过程序组合（program composition）实现（等 Crocker 告诉我们怎么做？？）。
>
> 【译注】末尾的 "when Crocker tells us how??" 是 RFC 文化中典型的非正式吐槽，保留其语气。

---

## AHI NLS - USER CONSOLE COMMUNICATION - AN EXAMPLE（AHI NLS——用户控制台通信——一个示例）

```
   BLOCK DIAGRAM

      The right side of the picture represents functions done at the
      user's main computer; the left side represents those done at the
      host computer.

         Each label in the picture corresponds to a statement with the
         same name.

         There are four trails associated with this picture.  The first
         links (in a forward direction) the labels which are concerned
         only with network information.  The second links the total
         information flow (again in a forward direction).  The last two
         are equivalent to the first two but in a backward direction.
         They may be set with pointers t1 through t4 respectively.

         [">tif:] OR I" >nif"]; ["<tif:] OR ["<nif"];
```

> 框图（BLOCK DIAGRAM）
>
> 图的右侧表示在用户的主计算机上完成的功能；左侧表示在主机计算机上完成的功能。
>
> - 图中的每个标签都对应一条同名的语句。
> - 与该图相关联的有四条路径（trail）。第一条（向前方向）只把与网络信息有关的标签连接起来。第二条把总的信息流连接起来（同样是向前方向）。最后两条与前两条等价，但方向相反。它们可以分别用指针 t1 到 t4 设置。
> - `[">tif:] OR I" >nif"]; ["<tif:] OR ["<nif"];` 是设置上述路径指针的 DEL 代码片段，保留原样。

---

## USER-TO-HOST TRANSMISSION（用户到主机传输）

```
   Keyboard is the set of input devices at the user's console.
   Input bits from stations, after drifting through levels of monitor
   and interrupt handlers, eventually come to the encode translator.
   [>nif(encode)]

   Encode maps the semi-raw input bits into an input stream in a
   form suited to the serving-host subsystem which will process the
   input.  [>nif(hrt)<nif(keyboard)]

      The Encode program was supplied by the server-host subsystem
      when the subsystem was first requested.  It is sent to the user
      machine in symbolic form and is compiled at the user machine
      into code particularly suited to that machine.

      It may pack to break characters, map multiple characters to
      single characters and vice versa, do character translation, and
      give immediate feedback to the user.

   1 dm    Immediate feedback from the encode translator first goes to
   local display management, where it is mapped from the NET standard
   to the local display hardware.

      A wide range of echo output may come from the encode
      translator.  Simple character echoes would be a minimum, while
      command and machine-state feedback will be common.

      It is reasonable to expect control and feedback functions not
      even done at the server-host user stations to be done in local
      display control.  For example, people with high-speed displays
      may want to selectively clear curves on a Culler display, a
      function which is impossible on a storage tube.

   Output from the encode translator for the server-host goes to the
   invisible IMP, is broken into appropriate sizes and labeled by the
   encode translator, and then goes to the NET-to-host translator.

      Output from the user may be more than on-line input.  It may be
      larger items such as computer-generated data, or files
      generated and used exclusively at the server-host site but
      stored at the user-host site.

      Information of this kind may avoid translation, if it is already in
      server-host format, or it may undergo yet another kind of translation
      if it is a block of data.

   hrp  It finally gets to the host, and must then go through the
   host reception program.  This maps and reorders the standard
   transmission-style packets of bits sent by the encode programs
   into messages acceptable to the host.  This program may well be
   part of the monitor of the host machine. [>tif(net mode)<nif(code)]
```

> 键盘（Keyboard）是用户控制台处输入设备的总称。来自各工位的输入比特，经过监控程序和中断处理程序各层级的漂移之后，最终到达编码翻译器（encode translator）。[>nif(encode)]
>
> 编码（Encode）将半原始的输入比特映射为一种适合处理该输入的服务器主机子系统（serving-host subsystem）的输入流。[>nif(hrt)<nif(keyboard)]
>
> - 编码程序是服务器主机子系统在首次被请求时提供的。它以符号形式被发送到用户机器，并在用户机器上被编译成特别适合该机器的代码。
> - 它可以打包到断行字符，把多个字符映射为单个字符或反之，做字符翻译，并给用户即时反馈。
>
> l dm：来自编码翻译器的即时反馈首先进入本地显示管理（local display management），在那里从 NET 标准映射到本地显示硬件。
>
> - 编码翻译器可能产生范围很广的回显输出。简单字符回显是最低限度，而命令和机器状态反馈将很常见。
> - 有理由预期，一些即使在服务器主机的用户工位上都不做的控制和反馈功能，也会在本地显示控制中完成。例如，拥有高速显示器的人可能想有选择地清除 Culler 显示器上的曲线——这是存储管（storage tube）上不可能实现的功能。
>
> 编码翻译器中发给服务器主机的输出进入「隐形 IMP」（invisible IMP），由编码翻译器分割成合适的大小并加上标签，然后进入网络到主机翻译器（NET-to-host translator）。
>
> - 用户的输出可能不止是联机输入。它可能是更大的条目，如计算机生成的数据，或仅在服务器主机站点生成和使用、但存储在用户主机站点的文件。
> - 这类信息如果已经是服务器主机格式，就可以避免翻译；如果它是一个数据块，则可能还要经受另一种翻译。
>
> hrp：它最终到达主机，然后必须经过主机接收程序（host reception program）。这个程序把编码程序发来的标准传输式比特包映射并重新排序为主机可接受的消息。这个程序很可能就是主机机器监控程序的一部分。[>tif(net mode)<nif(code)]
>
> 【译注】① 段首 "1 dm" 应为框图标签，疑为 "ldm"（local display management，本地显示管理）。② "隐形 IMP" 指不经用户主机监控程序直接与网络接口消息处理器（IMP）通信的部分。③ 方括号内的 `[>nif(encode)]` 等是原文框图中标签间路径/指针关系的记号，保留原样。

---

## HOST-TO-USER TRANSMISSION（主机到用户传输）

```
   decode   Output from the server-host initially goes through decode,
   a translation map similar to, and perhaps more complicated than,
   the encode map.  [>nif(urt)>tif(imp ctrl)<tif(net mode)]

      This map at least formats display output into a simplified
      logical-entity output stream, of which meaningful pieces may be
      dealt with in various ways at the user site.

         The Decode program was sent to the host machine at the same
         time that the Encode program was sent to the user machine.
         The program is initially in symbolic form and is compiled
         for efficient running at the host machine.
         
         Lines of charaters should be logically identified so that
         different line widths can be handled at the user site.

         Some form of logical line identification must also be made.
         For example, if a straight line is to be drawn across the
         display this fact should be transmitted, rather than a
         series of 500 short vectors.

         As things firm up, more and more complicated structural
         display information (in the manner of LEAP) should be sent
         and accommodated at user sites so that the responsibility for
         real-time display manipulation may shift closer to the user.

      imp ctrl   The server-host may also want to send control
      information to IMPs.  Formatting of this information is done by
      the host decoder.  [>tif(urt) <tif(decode)]

      The other control information supplied by the host decoder is
      message break up and identification so that proper assembly and
      sorting can be done at the user site.

   From the host decoder, information does to the invisible IMP, and
   directly to the NET-to-user translator.  The only operation done
   on the messages is that they may be shuffled.

   urt   The user reception translator accepts messages from the
   user-site IMP 1 and fixes them up for user-site display.  
   [>nif(d ctrl)>tif(prgm ctrl)<tif(imp ctrl)<nif(decode)]

      The minimal action is a reordering of the message pieces.
      
      dctrl   For display output, however, more needs to be done.  The
      NET logical display information must be put in the format of
      the user site.  Display control does this job.  Since it
      coordinates between (encode) and (decode) it is able to offer
      features of display management local to the user site.
      [>nif(display)<nif(urt)]

      prgmctrl   Another action may be the selective translation and
      routing of information to particular user-site subsystems.
      [>tif(dctrl)<tif(urt)]

         For example, blocks of floating-point information may be
         converted to user-style words and sent, in block form, to a
         subsystem for processing or storage.

         The styles and translation of this information may well be a 
         compact binary format suitable for quick translation, rather
         than a print-image-oriented format.

      (display)   is the output to the user.  [<nif(d ctrl)]
```

> decode（解码）：来自服务器主机的输出最初经过解码，这是一个与编码映射相似、或许更复杂的翻译映射。[>nif(urt)>tif(imp ctrl)<tif(net mode)]
>
> - 这个映射至少把显示输出格式化为一种简化的逻辑实体输出流，其中有意义的部分可以在用户站点以各种方式处理。
>   - 解码程序是在编码程序发送到用户机器的同时被发送到主机机器的。该程序最初是符号形式，并被编译以便在主机机器上高效运行。
>   - 字符行应被逻辑标识，以便不同的行宽可以在用户站点处理。
>   - 还必须进行某种形式的逻辑行标识。例如，如果要在显示器上画一条直线，应该传输"这是一条直线"这个事实，而不是传输 500 个短向量。
>   - 随着事物逐渐定型，越来越多复杂的结构显示信息（以 LEAP 的方式）应该被发送并在用户站点容纳，从而使实时显示操作（real-time display manipulation）的职责可能更靠近用户。
>
> imp ctrl：服务器主机可能还想向 IMP 发送控制信息。这些信息的格式化由主机解码器（host decoder）完成。[>tif(urt) <tif(decode)]
>
> - 主机解码器提供的其他控制信息是消息的分解和标识，以便在用户站点进行正确的组装和分类。
>
> 从主机解码器出发，信息进入隐形 IMP，然后直接进入网络到用户翻译器（NET-to-user translator）。对消息所做的唯一操作是它们可能被重排（shuffled）。
>
> urt：用户接收翻译器（user reception translator）接受来自用户站点 IMP 的消息，并把它们整理好供用户站点显示。[>nif(d ctrl)>tif(prgm ctrl)<tif(imp ctrl)<nif(decode)]
>
> - 最小动作是重新排列消息的各个部分。
> - dctrl（显示控制）：然而，对于显示输出，还需要做更多。NET 逻辑显示信息必须被置入用户站点的格式。显示控制（Display control）负责这项工作。由于它在（encode）和（decode）之间进行协调，它能够提供用户站点本地的显示管理功能。[>nif(display)<nif(urt)]
> - prgmctrl（程序控制）：另一个动作可能是对信息的选择性翻译和路由，将其发送到特定的用户站点子系统。[>tif(dctrl)<tif(urt)]
>   - 例如，浮点信息块可以被转换为用户风格的词，并以块的形式发送给某个子系统进行处理或存储。
>   - 这类信息的样式和翻译很可能是一种适合快速翻译的紧凑二进制格式，而不是面向打印映像（print-image）的格式。
> - (display)：是给用户的输出。[<nif(d ctrl)]
>
> 【译注】① "IMP 1" 疑为 "IMP" 之误。② 原文 "information does to" 应为 "information goes to"（信息前往），系打字错误。③ 原文 "Lines of charaters" 中 "charaters" 为 "characters"（字符）的打字错误。

---

## USER-TO-HOST INDIRECT TRANSMISSION（用户到主机间接传输）

```
      (net mode)   This is the mode where a remote user can link to a node
      indirectly through another node.   [<nif(decode)<tif(hrt)]
```

> （net mode，网络模式）：在这种模式下，远程用户可以通过另一个节点间接链接到一个节点。[<nif(decode)<tif(hrt)]

---

## DEL SYNTAX（DEL 语法）

```
   NOTES FOR NLS USERS

      All statements in this branch which are not part of the compiler
      must end with a period.

      To compile the DEL compiler:

         Set this pattern for the content analyzer ( (symbol for up arrow)P1
         SE(P1) <-"-;). The pointer "del" is on the first character of pattern.

         Jump to the first statement of the compiler.  The pointer "c"
         is on this statement.

         And output the compiler to file  ( '/A-DEL' ).  The pointer "f"
         is on the name of the file for the compiler output -
```

> NLS 用户须知（NOTES FOR NLS USERS）
>
> 本分支（branch，指 NLS 文档树中的这一支）中所有不属于编译器的语句都必须以句号结尾。
>
> 要编译 DEL 编译器：
>
> - 为内容分析器（content analyzer）设置这个模式：(（向上箭头符号）P1 SE(P1) <-"-;)。指针 "del" 位于该模式的第一个字符上。
> - 跳转到编译器的第一条语句。指针 "c" 位于这条语句上。
> - 并把编译器输出到文件（'/A-DEL'）。指针 "f" 位于编译器输出文件的名称上。

---

### PROGRAMS（程序）

```
      SYNTAX

         -meta file (k=100.m=300,n=20,s=900)

         file = mesdecl $declaration $procedure "FINISH";

         procedure =

           procname (

              (

                 type "FUNCTION" /

                 "PROCEDURE" ) .id (type .id / -empty)) /

              "CO-ROUTINE") ' /

           $declaration labeledst $(labeledst ';) "endp.";

         labeledst = ((left arrow symbol).id ': / .empty) statement;

         type = "INTEGER" / "REAL" ;

         procname = .id;
```

> 本节定义了 DEL 程序文件的整体结构：一个文件（file）由消息声明、若干声明和若干过程组成，以 "FINISH" 结束；并区分了 FUNCTION（函数）、PROCEDURE（过程）与 CO-ROUTINE（协程）三类程序单元。
>
> 函数与过程加以区分，是为了帮助编译器生成更好的代码并做运行时检查。
>
> - 函数（Functions）返回数值。
> - 过程（Procedures）不返回数值。
>
> 协程（Co-routines）没有名字和参数。它们的初始唤起点（envocation points）由管道（pipe）声明给出。
>
> 目前尚不清楚全局声明究竟该如何处理？？（原文如此，保留作者的疑问语气）

---

### DECLARATIONS（声明）

```
   SYNTAX

      declaration = numbertype / structuredtype / label / lcl2uhr /
      uhr2rmt / pipetype;

      numbertype = : ("REAL" / "INTEGER") ("CONSTANT" conlist /
      varlist);

      conlist =

         .id '(left arrow symbol)constant

         $('. .id '(left arrow symbol)constant);

      varlist =

         .id ('(left arrow symbol)constant / .empty)

         $('. .id('(left arrow symbol)constant / .empty));

      idlist = .id $('. .id);

      structuredtype = (tree" / "pointer" / "buffer" ) idlist;

      label = "LABEL1" idlist;

      pipetype = PIPE" pairedids $(', pairedids);

      pairedids = .id .id;

      procname = .id;

      integerv = .id;

      pipename = .id;

      labelv = .id;
```

> 本节定义了各类声明语句：数值类型（numbertype，实数/整数，含常量表与变量表）、结构化类型（structuredtype，tree 树 / pointer 指针 / buffer 缓冲）、标签（label）、本地到通用表示 / 通用表示到远程的映射声明（lcl2uhr / uhr2rmt）以及管道类型（pipetype，把协程与管道名配对）。
>
> 被声明为常量的变量，在运行时可以放入只读内存（read-only memory）。
>
> 标签声明（label declaration）用于声明一些单元，这些单元以程序中标签的机器地址作为它们的值。这不是 B5500 的标签声明。
>
> 在管道（pipe）声明中，每对的第一个 .ID 是管道名，第二个是该管道的初始起点（原文 "thke" 为 "the" 的打字错误）。

---

### ARITHMETIC（算术）

```
   SYNTAX

      exp = "IF" conjunct "THEN" exp "ELSE" exp;

      sum = term (

         '+ sum /

         '- sum /

         -empty);

      term = factor (

         '* term /

         '/ term /

         '(up arrow symbol) term /

         .empty);

      factor = '- factor / bitop;

      bitop = compliment (

         '/' bitop /

         '/'\ bitop /

         '& bitop / (

         .empty);

      compliment = "--" primary / primary;
```

> 本节定义了算术与位运算表达式：IF-THEN-ELSE 表达式、加减乘除、求模（↑）、位运算（/、/\、&）以及按位取反等。
>
> （向上箭头符号）表示模（mod），/\ 表示异或（exclusive or）。
>
> 注意，一元减号（uniary minus，原文如此，应为 unary）是允许的，而且解析方式让你可以写出 x*-y。
>
> 由于位运算符没有标准约定，它们都有相同的优先级，必须用括号进行分组。
>
> 补码（Compliment）是 1 的补码（1's compliment，即 one's complement）。
>
> 假定所有的算术和位运算都在运行该代码的机器的模式和风格下进行。任何利用字长、二进制补码（two's compliment）算术等特性的人最终都会遇到问题。

---

### PRIMARY（初等量）

```
   SYNTAX

      primary =

         constant /

         builtin /

         variable / (

         block /

         '( exp ');

      variable = .id (

         '(symbol for left arrow) exp /

         '( block ') /

         .empty);

      constant =  integer / real / string;

      builtin =

         mesinfo /

         cortnin /

         ("MIN" / "MAX") exp $('. exp) '/ ;
```

> 本节定义了表达式的基本构成单元：常量（整数/实数/字符串）、内建函数（builtin，如消息信息、协程唤起 FETCH、MIN/MAX）、变量（可带下标或参数）、块（block）以及括号表达式。
>
> 带括号的表达式可以是一系列表达式。一个系列的值是运行时最后执行的那个表达式的值。
>
> 子程序可以有一个按名调用（call by name）的参数。
>
> 表达式可以混合。字符串是个大问题？鲁利夫森（Rulifson）还想干掉实数！！（原文吐槽，保留语气）

---

### CONJUNCTIVE EXPRESSION（合取表达式）

```
   SYNTAX

      conjunct = disjunct ("AND" conjunct / .empty);

      disjunct = negation ("OR" negation / .empty);

      negation = "NOT" relation / relation;

      relation =

         '( conjunct ') /

         sum (

           "<=" sum /

           ">=" sum /

           '< sum /

           '> sum /

           '= sum /

           '" sum /

           .empty);
```

> 本节定义了布尔逻辑表达式：合取（AND）、析取（OR）、否定（NOT）以及关系运算（≤、≥、<、>、=、≠）。
>
> 合取（conjunct）结构的设置方式使得一个不是求和（sum）的合取不必有值，并且可以在代码中使用跳转来求值。只有在需要逻辑判断的地方（例如 if 和 while 语句）才引用合取。
>
> 我们希望大多数编译器足够聪明，能在运行时跳过不必要的求值。即，合取中左部为假，或析取（disjunct）中左部为真时，不必对相应的右部求值。

---

### ARITHMETIC EXPRESSION（算术表达式）

```
   SYNTAX

      statement = conditional / unconditional;

      unconditional = loopst / cases / cibtrikst / uist / treest /
      block / null / exp;

      conditional = "IF" conjunct "THEN" unconditional (

         "ELSE" conditional /

         .empty);

      block = "begin" exp $('; exp) "end";
```

> 本节定义了语句的整体结构：语句分为条件语句（conditional）与无条件语句（unconditional）；无条件语句可以是循环、CASE、树操作（cibtrikst / uist 疑为树操作与 I/O 语句的缩写）、块、空语句或表达式。
>
> 一个表达式可以是一条语句。在条件语句中，else 部分是可选的；而在表达式中，它是强制的。这是语法规则左侧（left part）排列方式的一个副作用。

---

### SEMI-TREE MANIPULATION AND TESTING（半树操作与测试）

```
   SYNTAX

      treest = setpntr / insertpntr / deletepntr;

      setpntr = "set" "pointer" pntrname "to" pntrexp;

      pntrexp = direction pntrexp / pntrname;

      insertpntr = "insert" pntrexp "as"

         (("left" / "right") "brother") /

         (("first" / "last: ) "daughter") "of" pntrexp;

      direction =

         "up" /

         "down" /

         "forward" /

         "backward: /

         "head" /

         "tail";

      plantree = "replace" pntrname "with" pntrexp;

      deletepntr = "delete: pntrname;

      tree = '( tree1 ') ;

      tree1 = nodename $nodename ;

      nodename = terminal / '( tree1 ');

      terminal = treename / buffername / point ername;

      treename = id;

      treedecl = "pointer" .id / "tree" .id;
```

> 本节定义了半树（semi-tree）数据结构的操作与测试语句：设置指针（set pointer）、按方向移动指针、插入兄弟（brother）/女儿（daughter）节点、删除指针、用子树替换节点，以及树的字面量表示（树由节点名递归构成，很像 LISP 的 S 表达式）。
>
> 在构建树时使用多余的括号会产生线性的子分类（linear subcategorization），正如在 LISP 中一样。
>
> 【译注】「半树」（semi-tree）是比完整树更自由的数据结构概念。原文语法中 "last: ) "、"backward:、"、"delete: "、"point ername" 等处的引号缺失/错乱系原文排版问题，按原文保留。

---

### FLOW AND CONTROL（流程与控制）

#### GO TO STATEMENTS（GO TO 语句）

```
      controlst = gost / subst / loopstr / casest;

      gost = "GO" "TO" (labelv / .id);

         assignlabel = "ASSIGN" .id "TO" labelv;
```

> 本节开头给出流程控制语句的总分类（go to、子程序、循环、CASE），并定义了 GO TO 语句与 ASSIGN（把标签赋给标签变量）语句。

#### SUBROUTINES（子程序）

```
      subst = callst / returnst / cortnout;

         callst = "CALL" procname (exp / .emptyu);

         returnst = "RETURN" (exp / .empty);

         cortnout = "STUFF" exp "IN" pipename;

      cortnin = "FETCH" pipename;
```

> 本节定义了子程序调用（CALL）、返回（RETURN）以及协程之间的通信：把值「塞进」（STUFF ... IN）管道，或从管道「取回」（FETCH）一个协程的结果。
>
> FETCH 是一个内建函数，其值通过唤起（envoking）指定的协程来计算。

#### LOOP STATEMENTS（循环语句）

```
      SYNTAX

         loopst = whilest / untilst / forst;

         whilest = "WHILE" conjunct "DO" statement;

         untilst = "UNTIL" conjunct "DO" statement;

         forst = "FOR" integerv '- exp ("BY" exp / .empty) "TO" exp

         "DO" statements;
```

> 本节定义了三种循环语句：WHILE（当……时重复）、UNTIL（直到……时重复）和 FOR（带初值、步长 BY、上界 TO 的计数循环）。
>
> while 和 until 语句的值分别被定义为假和真（即 0 和非 0）。
>
> for 语句在初始化时对初始表达式、by 部分和 to 部分各求值一次。for 语句的运行索引在循环内不可更改，它只能被读取。如果某些编译器能利用这一点（比如说把它放进寄存器），那就更好了。增量和 to 边界都将在初始化期间被四舍五入为整数。

---

### CASE STATEMENTS（CASE 语句）

```
   SYNTAX

      casest = ithcasest / condcasest;

      ithcasest = "ITHCASE" exp "OF" "BEGIN" statement $(';
      statement) "END";

      condcasest = "CASE" exp "OF" "BEGIN" condcs $('; condcs)
      "OTHERWISE" statement "END";


      condcs = conjunct ': statement;
```

> 本节定义了两种 CASE 语句：ITHCASE（按第几个分支选择，即索引式分支）和 CASE（按条件选择，带 OTHERWISE 缺省分支）。
>
> CASE 语句的值是最后执行的那个分支的值。

---

### EXTRA STATEMENTS（附加语句）

```
   null = "NULL";
```

> 本节只定义了一条附加语句 NULL（空语句），执行时不产生任何操作。

---

### I/O STATEMENTS（输入/输出语句）

#### MESSAGES（消息）

```
   SYNTAX

      messagest = buildmes / demand;

         buildmest = startmes / appendmes / sendmes;

              startmes = "start" "message";

              appendmes = "append" "message" "byute" exp;

              sendmes = "send" "message";

              
           demandmes = "demand" "Message";

      mesinfo =

         "get" "message" "byte"

         "message1" "length" /

         "message" empty: '?;

      mesdecl = "message" "bytes" "are" ,byn "bits" long" '..
```

> 本节定义了与消息（message）有关的 I/O 语句：start message（开始消息）、append message byte（追加消息字节）、send message（发送消息）、demand message（索取/请求消息），以及消息字节、消息长度等内建信息函数（mesinfo）与消息字节长度声明（mesdecl）。
>
> 【译注】原文语法中 "byute"（应为 byte）、"message1"（应为 message）、"empty: '?"、",byn"、long" '.." 等处系原文打字与排版错误，按原文保留。

---

### DISPLAY BUFFERS（显示缓冲）

```
   SYNTAX

      dspyst = startbuffer / bufappend / estab;

      startbuffer - "start" "buffer";

      bufappend = "append" bufstuff $('& bufstuff);

      bufstuff = :

         "parameters" dspyparm $('. dspyparm) /

         "character" exp /

         "string"1 strilng /

         "vector" ("from" exp ':exp / .empty) "to" exp '. exp /

         "position" (onoff / .empty) "beam" "to" exp '= exp/

         curve" ;

      dspyparm F :

         "intensity" "to" exp /

         "character" "width" "to" exp /

         "blink" onoff /

        "italics" onff;

      onoff = "on" / "off";

      estab = "establish" buffername;
```

> 本节定义了显示缓冲（display buffer）的构建语句：start buffer（开始缓冲）、append（追加各种逻辑实体 bufstuff，如参数、字符、字符串、向量、光束定位、曲线等）以及 establish（把缓冲确立为缓冲名 buffername）。
>
> 【译注】原文语法中 "strilng"（应为 string）、"curve" ;"、"F :"、"onff"（应为 onoff）、"exp '= exp" 等处的引号/冒号错乱与错字系原文打字错误，按原文保留。

#### LOGICAL SCREEN（逻辑屏幕）

```
      The screen is taken to be a square.  The coordinates are
      normalized from -1 to +1 on both axes.

      Associated with the screen is a position register, called
      PREG.  The register is a triple <x.y.r> where x and y 
      specify a point on the screen and r is a rotation in
      radians, counter clockwise, from the x-axis.

      The intensity, called INTENSITY, is a real number in the
      range from 0 to 1.  0 is black, 1 is as light as your
      display can go, and numbers in between specify the relative
      log of the intensity difference.

      Character frame size.

      Blink bit.
```

> 屏幕被设想为一个正方形。两个轴上的坐标都归一化为 -1 到 +1。
>
> 与屏幕关联着一个位置寄存器，称为 PREG。该寄存器是一个三元组 <x.y.r>，其中 x 和 y 指定屏幕上的一个点，r 是以弧度为单位、从 x 轴逆时针方向的旋转。
>
> 强度（称为 INTENSITY）是范围 0 到 1 的实数。0 是黑色，1 是你的显示器所能达到的最亮，之间的数值指定强度差异的相对对数（relative log）。
>
> 字符框大小（Character frame size）。
>
> 闪烁位（Blink bit）。

#### BUFFER BUILDING（缓冲构建）

```
      The terminal nodes of semi-trees are either semi-tree names
      or display buffers.  A display buffer is a series of logical
      entities, called bufstuff.

      When the buffer is initilized, it is empty.  If no
      parameters are initially appended, those in effect at the
      end of the display of the last node in the semi-tree will be in
      effect for the display of this node.

      As the buffer is built, the logical entities are added to it.
      When it is established as a buffername, the buffer is
      closed, and further appends are prohibited.  It is only a
      buffername has been established that it may be used in a tree
      building statement.
```

> 半树的终端节点要么是半树名，要么是显示缓冲。显示缓冲是一系列称为 bufstuff 的逻辑实体。
>
> 当缓冲被初始化时，它是空的。如果最初没有追加任何参数，那么半树中最后一个节点显示结束时生效的参数，将对这个节点的显示生效。
>
> 随着缓冲的构建，逻辑实体被添加到其中。当它被确立为缓冲名（buffername）时，缓冲即被关闭，进一步的追加被禁止。只有在缓冲名被确立之后，它才能在构建树的语句中使用。
>
> 【译注】原文 "initilized" 为 "initialized"（初始化）的打字错误。

---

### LOGICAL INPUT DEVICES（逻辑输入设备）

```
      Wand

      Joy Stick

      Keyboard

      Buttons

      Light Pens

      Mice
```

> 逻辑输入设备（1969 年的设想清单）：
>
> - 魔杖（Wand）
> - 操纵杆（Joy Stick）
> - 键盘（Keyboard）
> - 按钮（Buttons）
> - 光笔（Light Pens）
> - 鼠标（Mice）

---

### AUDIO OUTPUT DEVICES（音频输出设备）

```
   AUDIO OUTPUT DEVICES

   .end
```

> 音频输出设备（AUDIO OUTPUT DEVICES）——原文此节仅有标题而无具体内容。
>
> `.end` 是本文 DEL 语法部分的结束标记。

---

## SAMPLE PROGRAMS（示例程序）

```
   Program to run display and keyboard as tty.

   to run NLS

      input part

      display part

         DEMAND MESSAGE;

         While LENGTH " O DO

            ITHCASE GETBYTE OF Begin

            ITHCASE GETBYTE OF %file area uipdate% BEGIN

               %literal area%

               %message area%

               %name area%

               %bug%

               %sequence specs%

               %filter specs%

               %format specs%

               %command feedback line%

               %filer area%

               %date time%

               %echo register%

           BEGIN %DEL control%
```

> 把显示器和键盘当作电传打字机（tty）运行的程序。
>
> 运行 NLS：
>
> - 输入部分（input part）
> - 显示部分（display part）：
>
> 程序片段（保留原样）：索取消息（DEMAND MESSAGE）；当 LENGTH ≠ 0 时，用 ITHCASE 按消息字节（GETBYTE）分派处理，各分支对应 NLS 中的文件区更新（%file area update%，原文 "uipdate" 系打字错误）、字面量区、消息区、名字区、bug、序列规格、过滤规格、格式规格、命令反馈行、文件区、日期时间、回显寄存器等区域，最后进入 %DEL control%（DEL 控制）分支。

---

## DISTRIBUTION LIST（分发名单）

> 原文：

```
   Steve Carr
      Department of Computer Science
      University of Utah
      Salt Lake City, Utah  84112
      Phone 801-322-7211 X8224

   Steve Crocker

      Boelter Hall
      University of California
      Los Angeles, California
      Phone 213-825-4864

   Jeff Rulifson

      Stanford Research Institute
      333 Ravenswood
      Menlo Park, California  94035
      Phone 415-326-6200 X4116

   Ron Stoughton

      Computer Research Laboratory
      University of California
      Santa Barbara, California  93106
      Phone 805-961-3221

   Mehmet Baray

      Corey Hall
      University of California
      Berkeley, California  94720
      Phone 415-843-2621
```

> 中文对照：

| 姓名 | 机构 / 地址 | 电话 |
|------|-------------|------|
| 史蒂夫·卡尔（Steve Carr） | 犹他大学计算机科学系（Department of Computer Science, University of Utah），犹他州盐湖城（Salt Lake City, Utah）84112 | 801-322-7211 转 8224 |
| 史蒂夫·克罗克（Steve Crocker） | 加州大学洛杉矶分校（University of California），加州洛杉矶（Los Angeles, California）Boelter 楼（Boelter Hall） | 213-825-4864 |
| 杰夫·鲁利夫森（Jeff Rulifson） | 斯坦福研究院（Stanford Research Institute），加州门洛帕克（Menlo Park, California）94035 Ravenswood 路 333 号（333 Ravenswood） | 415-326-6200 转 4116 |
| 罗恩·斯托顿（Ron Stoughton） | 加州大学圣巴巴拉分校（University of California）计算机研究实验室（Computer Research Laboratory），加州圣巴巴拉（Santa Barbara, California）93106 | 805-961-3221 |
| 迈赫迈特·巴赖（Mehmet Baray） | 加州大学伯克利分校（University of California），加州伯克利（Berkeley, California）94720 Corey 楼（Corey Hall） | 415-843-2621 |

---

## 附：翻译要点备忘

- **Decode-Encode Language (DEL)** → 解码-编码语言（保留 DEL 缩写）。DEL 是 RFC 1 中提出的「前端代码下载到本地编译执行」概念的正式语言规范：主机把用 DEL 写成的符号程序（如 NLS 的 REP）发给用户站点，由用户站点编译后在本地运行，负责输入编解码、即时反馈与显示树构建。
- **Network Standard Translator (NST)** → 网络标准翻译器。文档给出 NST-DEL 的三个使用层级：①最低层——直接透传（NST 不作为）；②中间层——为用户主机 TTY 配备回显表；③高层——用协程结构驱动大型面向显示的系统。
- **Universal Hardware Representation** → 通用硬件表示法（显示器=正方形，坐标在两个轴上均归一化为 -1 到 1）。
- **Remote Encode Program (REP)** → 远程编码程序。
- **co-routine** → 协程；**semi-tree** → 半树（比完整树更自由的数据结构概念）；**display buffer** → 显示缓冲；**logical screen** → 逻辑屏幕。
- **TSS** → Time-Sharing System（分时系统）；**LEAP** → 保留原文（SRI 的一个数据结构语言/系统）；**BBN** → 博尔特·贝拉内克·纽曼公司（RFC 系列的早期主办方）。
