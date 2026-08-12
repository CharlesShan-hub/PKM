# RFC 10 — Documentation Conventions（文档约定·修订版）
> **中英对照翻译版本**
> 原文作者：Steve Crocker（UCLA 加州大学洛杉矶分校）
> 原文发布日期：1969 年 7 月 29 日
> 翻译说明：本文件采用「英文原文在上，中文翻译在下」的逐段对照格式。通讯录部分以中英对照表格呈现。

---

## 文头 · Header

```
Network Working Group                                           S. Crocker
RFC-10                                                          UCLA
                                                                29 July 1969
```

> 网络工作组                                                   S. 克罗克
> RFC 第 10 号                                                 加州大学洛杉矶分校
>                                                               1969 年 7 月 29 日

```
                          DOCUMENTATION CONVENTIONS
```

>                             文档约定（Documentation Conventions）

```
This note is a revision of NWG/RFC #3
```

> 本笔记是 NWG/RFC 第 3 号的**修订版**。

【译注】RFC 10 是 RFC 3 的修订版——标准版本化思想的最早实例。

```
The Network Working Group seems to consist of Steve Carr at Utah, Elmer
Shapiro and Bill English SRI, Steve Crocker at UCLA, John Haefner at
RAND, Paul Rovner and Jim Curry at Lincoln Labs.  Membership is not closed.
```

> 网络工作组目前似乎由以下成员组成：犹他大学（Utah）的 Steve Carr，斯坦福研究院（SRI）的 Elmer Shapiro 和 Bill English，加州大学洛杉矶分校（UCLA）的 Steve Crocker，兰德公司（RAND）的 John Haefner，林肯实验室（Lincoln Labs）的 Paul Rovner 和 Jim Curry。成员资格并未封闭——欢迎任何人加入。

【译注】与 RFC 3 相比：新增了 Shapiro、English（SRI）、Haefner（RAND）、Rovner 和 Curry（Lincoln Lab）；原来的 Rulifson 和 Duvall 这次未列入——1969 年的名单就是这么随意。

```
The Network Working Group (NWG) is concerned with the HOST software, the
strategies for using the network, and initial experience with the network.
```

> 网络工作组（NWG）关注：主机软件（HOST software）、使用网络的策略、以及网络的最初使用经验。

```
Documentation of the NWG's effort is through notes such as this.  Notes
may be produced at any site by anybody and included in this series.
```

> NWG 的工作通过此类笔记来记录。任何站点、任何人都可以撰写笔记并收入本系列。

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

> 一份 NWG 笔记的内容可以是任何与主机软件或网络其他方面相关的想法、建议等。笔记鼓励**及时性优先于打磨**（timely rather than polished）。没有例子或具体细节的哲学主张、没有引言或背景说明的具体建议或实现技术、没有尝试给出任何答案的明确问题——**全部可以接受**。一份 NWG 笔记的最短长度是**一句话**。

```
These standards (or lack of them) are stated explicitly for two reasons.
First, there is a tendency to view a written statement as ipso facto
authoritative, and we hope to promote the exchange and discussion of 
considerably less than authoritative ideas.  Second, there is a natural
hesitancy to publish something unpolished, and we hope to ease this
inhibition.
```

> 之所以明确写出这些标准（或"标准的缺失"），有两个原因：第一，人们倾向于把书面陈述**本身就当作权威**（ipso facto authoritative），而我们希望促进那些远低于权威级别想法的交换与讨论；第二，人们天生羞于发表未打磨的东西，而我们希望减轻这种心理障碍。

【译注】此段与 RFC 3 完全相同——三个月后内容标准一字未改。

---

## 格式要求 · FORM

```
Every NWG note should bear the following information:

        1.  "Network Working Group"
            "Request for Comments:"x (x underscored)
            where x is a serial number (x underscored)
            Serial numbers are assigned by Steve Crocker at UCLA

        2.  Author and affiliation

        3.  Date

        4.  Title.  The title need not be unique.
```

> 每份 NWG 笔记都应携带以下信息：
>
> 1. "Network Working Group" + "Request for Comments:"x（x 加下划线）
>    其中 x 是序号（加下划线）；**序号现在由 UCLA 的 Steve Crocker 分配**
> 2. 作者和所属机构
> 3. 日期
> 4. 标题（标题不需要唯一）

【译注】与 RFC 3 相比：序号分配权从 SRI 的 Bill Duvall 移交给了 UCLA 的 Steve Crocker，且序号 x 明确要求加下划线（排版规范化）。

---

## 分发 · DISTRIBUTION

```
One copy only will bve sent from the author's site to:

        1.  Steve Crocker, UCLA
        2.  Ron Stoughton, UCSB
        3.  Elmer Shapiro, SRI
        4.  Steve Carr, Utah
        5.  John Haefner, RAND
        6.  Paul Rovner, LL
        7.  Bob Kahn, BB&N
        8.  Larry Roberts, ARPA
        9.  Jerry Cole, SDC

Reproduction if desired may be handled locally.
```

> 作者站点只向以下 9 人各寄**一份**：
>
> 1. Steve Crocker，UCLA
> 2. Ron Stoughton，UCSB
> 3. Elmer Shapiro，SRI
> 4. Steve Carr，Utah
> 5. John Haefner，RAND
> 6. Paul Rovner，LL（林肯实验室）
> 7. Bob Kahn，BB&N
> 8. Larry Roberts，ARPA
> 9. **Jerry Cole，SDC**（新增）
>
> 如需复制，可在本地自行处理。

【译注】原文 "bve" 为 "be" 的笔误。

---

## 通讯录 · ADDRESSES

```
Below are the most current addresses I have.  Please correct as necessary.
```

> 以下是我手头最新的地址。如有出入请更正。

【译注】通讯录以中英对照表格呈现（原文为逐行排版，这里用表格便于对照）。电话中 "X" 为分机号、OX 为旧式交换局名。

| 姓名 · Name | 单位 · Affiliation | 地址 · Address | 电话 · Phone |
|---|---|---|---|
| Steve Crocker | UCLA | 3732 Boelter Hall, UCLA, Los Angeles, California 90024 | (213) 825-4864；秘书 825-2543 |
| Ron Stoughton | UCSB | Computer Research Lab., UCSB, Santa Barbara, California 93106 | (805) 961-3221 |
| Elmer Shapiro | SRI | Stanford Research Institute, 333 Ravenswood, Menlo Park, California 94025 | (415) 326-6200 |
| Steve Carr | Utah | Computer Science Dept., University of Utah, Salt Lake City, Utah 84ll2 | (801) 322-8224 |
| John Haefner | RAND | The Rand Corp., 1700 Main Street, Santa Monica, California 90406 | (213) 393-0411 |
| Paul D. Rovner | LL | Mass. Inst. of Tech., Lincoln Laboratory B-115, P.O. Box 73, Lexington, Mass. 02173 | (617) 662-5500 X7211 |
| Robert Kahn | BBN | Bolt, Beranek and Newman, 50 Moulton St., Cambridge, Mass. 02138 | (617) 491-1850；49l-1868 |
| Larry Roberts | ARPA | ODS/ARPA, 3D167 Pentagon, Washington, D.C. 2030l | (202) OX 7-8663；OX 7-8654 |
| Jerry Cole | SDC | 7842 Croyden, L.A., California 90045 / 2500 Colorado, Santa Monica, California 90406 | (213) 393-9411 X438；秘书 X6019 |

【译注】
- "84ll2"、"2030l" 中的 "l" 均为数字 1 的打字机笔误。
- **Larry Roberts 的办公地点是五角大楼 3D167**——ARPANET 的项目经理在国防部大楼里调度全美网络的建设。

---

## 翻译说明

- 本文档以「英文原文在上（代码块）、中文译文在下（引用块）」的方式逐段对照。
- 通讯录部分原文为逐行排版，翻译时改为中英对照表格，字段与原地址一一对应。
- 【译注】为译者补充的背景说明。