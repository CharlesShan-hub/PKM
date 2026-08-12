# RFC 3 — Documentation Conventions（文档约定）· Steve Crocker

> **一句话定位**：这份 RFC 不讲任何网络技术——它定义的是**整个 RFC 系列自己该怎么存在**。用今天的话说，这是"关于规则的规则"（meta-document）。全文不到一页，却是整个互联网标准化运动的宪法。
>
> 📄 原文见 [rfc3.txt](./rfc3.txt) ｜ 中英对照见 [zh.md](./zh.md)

---

## 〇、背景：先给"我们的笔记"立规矩

1969 年 4 月，NWG 已经发了 1、2 两号文档（都叫 HOST Software）。Crocker 意识到：这个系列会长久地写下去，而且谁都可以写、哪个站点都能发。**如果不先把"怎么写、发给谁、格式是什么"说清楚，这个系列迟早乱套。**

于是他写了 RFC 3，一篇纯粹的"组织纪律"文档。

---

## 一、内容细读

### 1. 成员名单："Membership is not closed（成员资格不封闭）"

开头就点名了当前的五位成员（Carr-Utah、Rulifson 和 Duvall-SRI、Crocker 和 Deloche-UCLA），然后立刻补了一句关键的话：

> **Membership is not closed.**
> （成员资格不封闭。）

在 1969 年说这句话，等于宣布：**这个小组不设门卫。** 任何站点、任何人，只要愿意干活就可以加入。后来互联网的开放文化，从这一句话开始。

### 2. 内容标准：宽松到令人震惊

RFC 3 规定什么内容可以写：

- 任何与主机软件或网络相关的**想法、建议、问题**
- **及时性优先于打磨**（timely rather than polished）
- 没有例子的哲学主张 ✅ 没有背景的具体建议 ✅ 没有答案的问题 ✅ **全都接受**
- **最短长度：一句话**

为什么故意定得这么宽松？Crocker 给了两个原因，每个都极其清醒：

> ① 人们容易把"白纸黑字"当成权威（ipso facto authoritative）——我们希望促进**远低于权威级别**的想法交换和讨论。
> ② 人们天生羞于发表没打磨的东西——我们希望**减轻这种心理障碍**。

这两条就是后来开源社区和敏捷开发"别怕发垃圾，发出来再改"信条的原版出处。**要摧毁"书面即权威"的权威迷信，办法不是禁止权威，而是让发表的门槛低到每个人都能参与。**

### 3. 格式要求：必须带四样东西

```
1. "Network Working Group" + "Request for Comments: x"
   （x 是序号，由 SRI 的 Bill Duvall 分配）
2. 作者和单位
3. 日期
4. 标题（标题不需要唯一）
```

注意：**序号由 Duvall 一个人分配**——这就是今天的 RFC 编号管理（RFC Editor 机构）的雏形。权威只有一件事：编号。内容大家随便写。

### 4. 分发机制：全手工电子邮件

作者站点只寄**一份**给固定 6 人名单：Bob Kahn（BB&N）、Larry Roberts（ARPA）、Steve Carr、Jeff Rulifson、Ron Stoughton、Steve Crocker。收到的人**自己复制**（"Reproduction if desired may be handled locally"——想复制就自己动手）。

1969 年没有邮件列表服务器，这就是它的"邮件列表"。Bob Kahn 和 Larry Roberts 在这个名单里——前者后来发明了 TCP，后者是 ARPANET 的项目经理。**他们是最早的两个订阅者。**

### 5. 工作计划："其他笔记"预告

文末预告了接下来要写的：Network Timetable（后来成了 RFC 4）、NIL 的哲学与规格、HOST Software 深入文档。**RFC 4 的诞生直接由这份预告催生。**

---

## 二、🔷 本质升华

> - **「人类发明的实现」**：6 人名单、序号由 Duvall 分配、必须带的 4 样信息、最短一句话——全是 1969 年的具体决定。换成 GitHub 仓库 + PR 审查、或邮件列表 + 主编，也是同一种精神的不同皮肤。
> - **「先于人类存在的规律」**：这条规律你在 RFC 1 的总括表里已经认过了——**「共识优先于权威律」**。RFC 3 是它的**正式出生证明**：当一群分布式的、互相没有上下级关系的工程师要协作构建一个大系统时，「开放讨论 + 低门槛发表 + 大体共识」永远战胜「中央权威 + 自上而下颁布」。而 RFC 3 还多贡献了一条配套规律——**「发表门槛与想法流动性成正比」**：写作的门槛越低，想法的流动越快；而想法流动越快，系统演化就越快。这和生物进化的"突变率"、城市文化的"人口流动率"是同一个动力学参数。
> - **后世重现**：
>   - 1992 年 David Clark 在 IETF 的著名宣言 **"We reject kings, presidents and voting. We believe in rough consensus and running code."**（我们拒绝国王、总统和投票，我们信仰大致共识和能跑的代码）——RFC 3 的精神半个世纪后的正式总结；
>   - 开源社区的 **"Release early, release often"**（早发布常发布）；
>   - 敏捷开发的 **"最小可用版本"**；
>   - 甚至 `#standards` 频道里那句 **"草案越烂，改得越快"**——全是 RFC 3 第一条规则的转世。

---

## 三、亮点速览

1. **"Membership is not closed"**——互联网开放文化的第一句话。
2. **"timely rather than polished"**——比敏捷宣言早 32 年。
3. **"Minimum length is one sentence"**——最低发表门槛的极端表达。
4. **序号只认 Duvall 一个人**——权威最小化到只剩编号权。
5. **"书面文字会被当成权威"这个自我认知**——一个组织肯主动拆解自己的权威，在那个年代几乎是绝无仅有的自觉。

---

## 四、成败与后续

- **大获成功**：这套格式（Network Working Group / Request for Comments / 作者 / 日期 / 标题）从第 3 号一直沿用到今天。RFC Editor（RFC 编辑）是如今全球互联网标准的官方编号机构，IAB 的正式宪章几乎就是 RFC 3 的现代化扩写。
- **被修正的**：序号分配从"一个人"变成了"一个机构"；分发从"6 人名单"变成了"公开档案 + 邮件列表"；"最短一句话"的极端宽松后来演化为分级的 Standards Track（标准轨道：Proposed/ Draft/ Standard）——但精神内核没变：**先发出来，让共识决定它配不配当标准。**
- **历史彩蛋**：分发名单里 Steve Carr 的机构被 Crocker 写成了 "UCLA"，但他其实是 Utah 的。**连定义格式的文档自己都打错字**——完美的 RFC 式黑色幽默，反而成了"不完美也要发"的最佳注脚。

---

## 五、思想传承对照表

| RFC 3 的规定 | 今天的对应物 |
|---|---|
| "Membership is not closed" | IETF 对所有人开放 / 开源社区无门卫 |
| timely rather than polished | 敏捷宣言 / Release early, release often |
| 最短一句话 | GitHub Issue / 一行 TODO 也是贡献 |
| 序号由 Duvall 分配 | RFC Editor 机构统一编号 |
| 寄给 6 人名单，自己复制 | 邮件列表 / 公开 RFC 档案库 |
| "书面即权威"的警觉 | IETF "rough consensus"（大致共识）原则 |
| 预告下期主题（NIL、Timetable） | Roadmap / 提案预告 |
