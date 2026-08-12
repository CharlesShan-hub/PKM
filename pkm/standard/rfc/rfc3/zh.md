# RFC 3 — Documentation Conventions（文档约定）
> **中英对照翻译版本**
> 原文作者：Steve Crocker（UCLA 加州大学洛杉矶分校）
> 原文发布日期：1969 年 4 月
> 翻译说明：本文件采用「英文原文在上，中文翻译在下」的逐段对照格式。专业术语首次出现时附原文。

---

## 文头 · Header

```
Network Working Group                                                 4689
RFC-3                                                           April 1969
                                                             Steve Crocker
                                                                      UCLA
```

> 网络工作组（Network Working Group）                                编号 4689
> RFC-3                                                        1969 年 4 月
>                                                             斯蒂夫·克罗克
>                                                             加州大学洛杉矶分校

> 【译注】文头右上角的「4689」是斯坦福研究院（SRI）网络信息中心（Network Information Center, NIC）为本文档分配的内部编号，与 RFC 序号无关。

```
                        DOCUMENTATION CONVENTIONS
```

>                             文档约定（Documentation Conventions）

---

```
The Network Working Group seems to consist of Steve Carr of Utah, Jeff
Rulifson and Bill Duvall at SRI, and Steve Crocker and Gerard Deloche
at UCLA.  Membership is not closed.
```

> 网络工作组（Network Working Group）目前似乎由以下成员组成：犹他大学（Utah）的 Steve Carr，斯坦福研究院（SRI）的 Jeff Rulifson 和 Bill Duvall，以及加州大学洛杉矶分校（UCLA）的 Steve Crocker 和 Gerard Deloche。成员资格并未封闭——欢迎任何人加入。

```
The Network Working Group (NWG) is concerned with the HOST software, the
strategies for using the network, and initial experiments with the network.
```

> 网络工作组（NWG）关注的是主机（HOST）软件、网络的使用策略，以及与网络相关的初步实验。

```
Documentation of the NWG's effort is through notes such as this.  Notes
may be produced at any site by anybody and included in this series.
```

> NWG 的工作成果通过诸如此类的备忘（note）来记录。任何站点的任何人都可以撰写备忘，并将其收录进本系列。

---

## 内容标准 · CONTENT

```
The content of a NWG note may be any thought, suggestion, etc. related to
the HOST software or other aspect of the network.  Notes are encouraged to
be timely rather than polished.  Philosophical positions without examples
or other specifics, specific suggestions or implementation techniques
without introductory or background explication, and explicit questions
without any attempted answers are all acceptable.  The minimum length for 
a NWG note is one sentence.
```

> 一篇 NWG 备忘的内容，可以是任何与主机软件或网络其他方面相关的想法、建议等。我们鼓励备忘做到「及时性优先于打磨」（timely rather than polished）——内容未及润色便发布。以下情形都是可以接受的：没有实例或其他具体细节的哲学立场阐述；没有引言或背景说明的具体建议或实现技术；以及没有给出任何尝试性回答的明确提问。一篇 NWG 备忘的最短长度，是一句话。

```
These standards (or lack of them) are stated explicitly for two reasons.
First, there is a tendency to view a written statement as ipso facto 
authoritative, and we hope to promote the exchange and discussion of 
considerably less than authoritative ideas.  Second, there is a natural
hesitancy to publish something unpolished, and we hope to ease this
inhibition.
```

> 我们之所以明确写出这些标准（或者说标准的缺失），有两个原因。其一，人们往往倾向于将白纸黑字的陈述视为「本身就是」权威（ipso facto authoritative），而我们希望促进的是那些远非权威的想法的交流与讨论。其二，人们天生对公开发布未打磨的作品心存犹豫，我们希望打消这种顾虑。

---

## 格式要求 · FORM

```
Every NWG note should bear the following information:

        1.  "Network Working Group"
            "Request for Comments:" x
            where x is a serial number.
            Serial numbers are assigned by Bill Duvall at SRI

        2.  Author and affiliation

        3.  Date

        4.  Title.  The title need not be unique.
```

> 每篇 NWG 备忘都应包含以下信息：
>
>         1.  「Network Working Group（网络工作组）」
>             「Request for Comments: x（请求评论：编号 x）」
>             其中 x 为序号（serial number）。
>             序号由斯坦福研究院（SRI）的 Bill Duvall 负责分配。
>
>         2.  作者及其所属机构（Author and affiliation）
>
>         3.  日期（Date）
>
>         4.  标题（Title）。标题不必唯一。

---

## 分发名单 · DISTRIBUTION

```
One copy only will be sent from the author's site to"

        1.  Bob Kahn, BB&N
        2.  Larry Roberts, ARPA
        3.  Steve Carr, UCLA
        4.  Jeff Rulifson, UTAH
        5.  Ron Stoughton, UCSB
        6.  Steve Crocker, UCLA

Reproduction if desired may be handled locally.
```

> 作者所在站点仅需向以下地址各寄送一份副本：
>
>         1.  Bob Kahn，BB&N（Bolt, Beranek and Newman 公司）
>         2.  Larry Roberts，ARPA（美国国防部高级研究计划局）
>         3.  Steve Carr，UCLA
>         4.  Jeff Rulifson，UTAH
>         5.  Ron Stoughton，UCSB
>         6.  Steve Crocker，UCLA
>
> 如需复制，可由本地自行处理。

> 【译注】原文此句「to」后面多了一个引号「"」，疑为打字错误，译文按「作者所在站点仅需向以下地址各寄送一份副本」理解。
> 【译注】分发名单第 3、4 条的单位标注与正文矛盾：根据文档开头，Steve Carr 属于犹他大学（Utah）、Jeff Rulifson 属于斯坦福研究院（SRI），而名单中分别写成了「UCLA」和「UTAH」，应为笔误（原文如此，此处按字面翻译保留原貌）。

---

## 其他说明 · OTHER NOTES

```
Two notes (1 & 2) have been written so far.  These are both titled HOST
Software and are by Steve Crocker and Bill Duvall, separately.
```

> 到目前为止已撰写了备忘 1 号与 2 号。这两篇的标题均为「HOST Software（主机软件）」，分别由 Steve Crocker 和 Bill Duvall 各自撰写。

```
Other notes planned are on

        1.  Network Timetable
        2.  The Philosophy of NIL
        3.  Specifications for NIL
        4.  Deeper Documentation of HOST Software.
```

> 计划中的其他备忘主题包括：
>
>         1.  网络时间表（Network Timetable）
>         2.  NIL 的哲学（The Philosophy of NIL）
>         3.  NIL 的规范说明（Specifications for NIL）
>         4.  主机软件的更深入文档（Deeper Documentation of HOST Software）

> 【译注】NIL 是计划中设计的一种实验性编程语言（Network Implementation Language，网络实现语言），拟用于编写网络实现，由 Crocker 等人主导设计。
