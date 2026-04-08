# IEC 61850 Part 2 解读：术语词汇表——学会说这门语言

> **对应文件**：`860[1].2.pdf`  
> **正式标题**：IEC 61850-2 — Glossary（术语词汇表）  
> **页数**：约 40 页  
> **定位**：标准的"字典"，所有专业术语的权威定义

---

## 一、为什么术语很重要？

想象一下，你去德国出差，手里拿着一份德文菜单，但你不认识任何一个词。旁边有个德国人说："Schweinshaxe 很好吃！"你点头微笑，但其实根本不知道他说的是猪肘子还是猪饲料。

IEC 61850 的术语就是这种情况——满篇缩写，每个都有精确的技术含义。如果你不知道 ACSI 是"抽象通信服务接口"而不是某种化学物质，读后续章节就会一头雾水。

**好消息是**：这份词汇表已经帮你整理好了。坏消息是：它太长了，有几百个词条。

**本文要做的事**：不是罗列所有术语，而是挑出**最关键的 30 个**，用故事和类比帮你记住它们。

---

## 二、核心概念：三个世界

IEC 61850 描述的是"变电站自动化系统"，但这个系统可以从三个维度来理解：

```
         ┌─────────────────────────────────────┐
         │         功能世界 (Function)          │
         │   逻辑节点、数据对象、服务、报告       │
         │   「软件逻辑层面」                    │
         └─────────────────┬───────────────────┘
                           │ 映射
         ┌─────────────────▼───────────────────┐
         │         通信世界 (Communication)     │
         │   MMS、GOOSE、SV、TCP/IP、以太网      │
         │   「网络协议层面」                    │
         └─────────────────┬───────────────────┘
                           │ 映射
         ┌─────────────────▼───────────────────┐
         │         物理世界 (Physical)          │
         │   IED、交换机、光纤、断路器、互感器    │
         │   「硬件设备层面」                    │
         └─────────────────────────────────────┘
```

**记住这个三层结构**，它是理解所有术语的框架。

---

## 三、术语分类速查

### 📦 第一类：物理设备相关

| 术语 | 全称 | 定义 | 汽车类比 |
|------|------|------|---------|
| **IED** | Intelligent Electronic Device | 智能电子设备，任何能通信的变电站设备（保护继电器、测控装置等）| ECU（电子控制单元）|
| **SAS** | Substation Automation System | 变电站自动化系统，整套 IED + 通信网络 + 监控软件 | 整车网络系统 |
| **MU** | Merging Unit | 合并单元，把多个互感器的模拟信号合并成数字 SV 报文 | 传感器信号调理模块 |
| **BCU** | Bay Control Unit | 间隔控制单元，一个间隔（如一条出线）的主控设备 | 区域控制器 |
| **RTU** | Remote Terminal Unit | 远程终端单元，传统概念，在 IEC 61850 中通常被 IED 取代 | 老式诊断接口 |

**记忆技巧**：IED 是 IEC 61850 世界里的"基本粒子"，几乎所有操作都是围绕 IED 进行的。

---

### 🧩 第二类：信息模型相关（最重要）

这是 IEC 61850 最核心的创新，也是最容易让人困惑的地方。

| 术语 | 全称 | 定义 | 汽车类比 |
|------|------|------|---------|
| **LN** | Logical Node | 逻辑节点，代表一个功能实体（如断路器控制 XCBR、测量 MMXU）| 诊断服务 DID |
| **LD** | Logical Device | 逻辑设备，LN 的容器，通常对应一个物理 IED 的一个功能域 | ECU 内部的功能分区 |
| **DO** | Data Object | 数据对象，LN 内部的数据集合（如相电压 PhV）| 数据标识符分组 |
| **DA** | Data Attribute | 数据属性，DO 的最小数据单元（如幅值 mag、品质 q）| 具体参数值 |
| **CDC** | Common Data Class | 公共数据类，定义 DA 的标准结构（如 MV=测量值、SPS=单点状态）| 数据类型模板 |
| **FC** | Functional Constraint | 功能约束，对 DA 的分类标签（ST=状态、MX=测量、SP=设定等）| 访问权限/属性标签 |

**用一个例子串起来**：

```
对象引用路径：IED1/LD1/MMXU1.PhV.phsA.cVal.mag.f

IED1      ← 物理设备（IED）
  LD1     ← 逻辑设备（LD）
    MMXU1 ← 测量逻辑节点（LN），测量单元 #1
      PhV ← 相电压（DO），Data Object
        phsA ← A相（子对象）
          cVal ← 复数值（Complex Value）
            mag ← 幅值（Magnitude）
              f ← 浮点数值（Float）= 220.5
```

这就像文件系统路径：`C:/Users/John/Documents/report.txt`

---

### 🔌 第三类：通信服务相关

| 术语 | 全称 | 定义 | 汽车类比 |
|------|------|------|---------|
| **ACSI** | Abstract Communication Service Interface | 抽象通信服务接口，定义"读/写/报告/控制"等服务的抽象规范 | UDS 服务规范 |
| **SCSM** | Specific Communication Service Mapping | 特定通信服务映射，把 ACSI 映射到具体协议（如 MMS）| 协议适配层 |
| **MMS** | Manufacturing Message Specification | 制造报文规范，ISO 9506 标准，IEC 61850 的主要传输协议 | TCP 上的诊断协议 |
| **GOOSE** | Generic Object Oriented Substation Event | 通用面向对象变电站事件，以太网二层快速广播机制 | CAN 广播帧 |
| **SV** | Sampled Values | 采样值，实时传输电流/电压采样数据 | 传感器数据流 |
| **PDU** | Protocol Data Unit | 协议数据单元，一个完整的数据包 | CAN 帧 / IP 包 |
| **SDU** | Service Data Unit | 服务数据单元，上层交给下层的数据 | 应用层 payload |

**关键理解**：ACSI 是"抽象语言"，SCSM 是"翻译器"。比如 ACSI 说"读数据"，SCSM 翻译成 MMS 的 Read 请求。

---

### 📊 第四类：报告与控制相关

| 术语 | 全称 | 定义 | 汽车类比 |
|------|------|------|---------|
| **URCB** | Unbuffered Report Control Block | 非缓存报告控制块，服务器主动推送数据（不缓存历史）| 实时事件上报 |
| **BRCB** | Buffered Report Control Block | 缓存报告控制块，服务器缓存数据，客户端可补读 | 带历史缓存的上报 |
| **RCB** | Report Control Block | 报告控制块，URCB 和 BRCB 的统称 | 报告配置对象 |
| **SGCB** | Setting Group Control Block | 定值组控制块，管理多套参数配置的切换 | 标定数据组切换 |
| **SBO** | Select Before Operate | 选择-执行模式，控制操作的两步确认机制 | 先请求后执行 |
| **Oper** | Operate | 执行操作（控制命令的第二步）| 执行确认 |
| **Cancel** | Cancel | 取消操作（SBO 模式下可取消已选择的控制）| 取消请求 |

**SBO 的故事**：

想象你要远程操作一个断路器跳闸。如果直接发"跳闸"命令，万一网络延迟导致你发了两次，断路器就会跳闸→合闸→再跳闸，造成事故。

SBO 机制是这样的：
1. **Select**：先发送"我要控制这个对象"，服务器锁定该对象
2. **Operate**：确认后再发送"执行"
3. 如果在超时内没有 Operate，自动 Cancel

这就像银行转账的"确认页"——先选收款人，再输密码确认。

---

### 📝 第五类：配置与描述相关

| 术语 | 全称 | 定义 | 汽车类比 |
|------|------|------|---------|
| **SCL** | Substation Configuration Language | 变电站配置语言，基于 XML 的描述语言 | ODX / A2L 文件 |
| **ICD** | IED Capability Description | IED 能力描述文件，厂商提供的设备能力说明 | ECU 描述文件 |
| **SSD** | System Specification Description | 系统规格描述文件，描述变电站一次系统拓扑 | 系统架构图 |
| **SCD** | Substation Configuration Description | 变电站配置描述文件，完整的系统配置（IED + 通信 + 拓扑）| 整车网络配置 |
| **CID** | Configured IED Description | 已配置 IED 描述文件，单个 IED 的实例化配置 | 单个 ECU 配置 |
| **IID** | Instantiated IED Description | 实例化 IED 描述文件，工程实例化的 IED 配置 | 实例化配置 |
| **SED** | System Exchange Description | 系统交换描述文件，用于不同工程间的配置交换 | 配置导出文件 |

**SCL 文件的关系**：

```
厂商提供 ICD（设备能力模板）
    ↓
系统集成商用 SSD + ICD 生成 SCD（完整系统配置）
    ↓
从 SCD 提取 CID（单个 IED 配置）下载到设备
```

这就像：
- ICD = 手机的产品说明书（这台手机有什么功能）
- SCD = 你家里的智能设备清单（手机+音箱+门锁如何联动）
- CID = 你的手机实际配置（连了哪个 WiFi、登录了哪个账号）

---

### ⚡ 第六类：保护与测量相关

| 术语 | 全称 | 定义 | 说明 |
|------|------|------|------|
| **CT** | Current Transformer | 电流互感器 | 传统模拟 CT，输出小电流 |
| **VT/PT** | Voltage Transformer / Potential Transformer | 电压互感器 | 传统模拟 VT，输出小电压 |
| **NCIT** | Non-Conventional Instrument Transformer | 非常规互感器 | 电子式互感器，直接输出数字信号 |
| **SmpCnt** | Sample Counter | 采样计数器 | SV 报文中的序列号，用于检测丢包 |
| **SmpSynch** | Sample Synchronization | 采样同步 | 确保多个 MU 的采样时间对齐 |
| **TCTR** | Current Transformer logical Node | 电流互感器逻辑节点 | LN 类型，代表 CT |
| **TVTR** | Voltage Transformer logical Node | 电压互感器逻辑节点 | LN 类型，代表 VT |

---

## 四、缩写速查表（按字母序）

工作中遇到不认识的缩写，来这里查：

| 缩写 | 含义 | 所属类别 |
|------|------|---------|
| ACSI | Abstract Communication Service Interface | 通信服务 |
| BRCB | Buffered Report Control Block | 报告机制 |
| CDC | Common Data Class | 数据模型 |
| CID | Configured IED Description | 配置文件 |
| CT | Current Transformer | 物理设备 |
| DA | Data Attribute | 数据模型 |
| DO | Data Object | 数据模型 |
| FC | Functional Constraint | 数据模型 |
| GOOSE | Generic Object Oriented Substation Event | 通信服务 |
| IED | Intelligent Electronic Device | 物理设备 |
| ICD | IED Capability Description | 配置文件 |
| LD | Logical Device | 数据模型 |
| LN | Logical Node | 数据模型 |
| MMS | Manufacturing Message Specification | 通信协议 |
| MU | Merging Unit | 物理设备 |
| NCIT | Non-Conventional Instrument Transformer | 物理设备 |
| RCB | Report Control Block | 报告机制 |
| SBO | Select Before Operate | 控制模式 |
| SCD | Substation Configuration Description | 配置文件 |
| SCL | Substation Configuration Language | 配置文件 |
| SCSM | Specific Communication Service Mapping | 通信服务 |
| SGCB | Setting Group Control Block | 控制配置 |
| SV | Sampled Values | 通信服务 |
| URCB | Unbuffered Report Control Block | 报告机制 |
| VT/PT | Voltage Transformer / Potential Transformer | 物理设备 |

---

## 五、术语之间的关系图

```
┌─────────────────────────────────────────────────────────────┐
│                        物理层                                │
│  ┌─────────┐  ┌─────────┐  ┌─────────┐                      │
│  │   IED   │  │   MU    │  │交换机   │                      │
│  │ (LD1)   │  │         │  │         │                      │
│  │ (LD2)   │  │         │  │         │                      │
│  └────┬────┘  └────┬────┘  └─────────┘                      │
│       │            │                                        │
│       └────────────┴────────────────┐                       │
│                                     │                       │
│  ┌──────────────────────────────────▼──────────────────┐   │
│  │                  通信层 (ACSI/SCSM)                  │   │
│  │  ┌─────────┐  ┌─────────┐  ┌─────────┐              │   │
│  │  │   MMS   │  │  GOOSE  │  │   SV    │              │   │
│  │  │(客户端) │  │(广播)   │  │(采样流) │              │   │
│  │  └─────────┘  └─────────┘  └─────────┘              │   │
│  └─────────────────────────────────────────────────────┘   │
│                            │                                │
│  ┌─────────────────────────▼─────────────────────────────┐  │
│  │                   功能层 (信息模型)                     │  │
│  │                                                       │  │
│  │  IED1/LD1/MMXU1.PhV.phsA.cVal.mag.f = 220.5           │  │
│  │   │    │    │    │   │   │    │   │                  │  │
│  │   │    │    │    │   │   │    │   └─ DA (数据属性)    │  │
│  │   │    │    │    │   │   │    └───── DA              │  │
│  │   │    │    │    │   │   └────────── DA              │  │
│  │   │    │    │    │   └────────────── DO (数据对象)    │  │
│  │   │    │    │    └────────────────── LN (逻辑节点)    │  │
│  │   │    │    └─────────────────────── LD (逻辑设备)    │  │
│  │   │    └──────────────────────────── IED (物理设备)    │  │
│  │   └───────────────────────────────── 对象引用路径      │  │
│  │                                                       │  │
│  │  服务：GetDataValues / SetDataValues / Report / Control│  │
│  │                                                       │  │
│  └───────────────────────────────────────────────────────┘  │
│                            │                                │
│  ┌─────────────────────────▼─────────────────────────────┐  │
│  │                   配置层 (SCL)                         │  │
│  │                                                       │  │
│  │  ICD ──→ SCD ──→ CID                                  │  │
│  │   ↑       ↑      ↑                                    │  │
│  │  厂商   集成商  现场                                   │  │
│  │                                                       │  │
│  └───────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────┘
```

---

## 六、与汽车诊断术语的对照

既然你有汽车背景，这里是一份详细的对照表，帮你用已知理解未知：

| IEC 61850 | 含义 | 汽车诊断 | 相似度 |
|-----------|------|---------|--------|
| IED | 智能电子设备 | ECU | ⭐⭐⭐⭐⭐ |
| LD | 逻辑设备 | ECU 功能域/会话 | ⭐⭐⭐⭐ |
| LN | 逻辑节点 | DID/RID 功能组 | ⭐⭐⭐⭐ |
| DO | 数据对象 | 数据标识符 DID | ⭐⭐⭐⭐ |
| DA | 数据属性 | 数据记录内容 | ⭐⭐⭐⭐ |
| FC | 功能约束 | 数据属性标签 | ⭐⭐⭐ |
| ACSI | 抽象通信服务 | UDS 服务层 | ⭐⭐⭐⭐ |
| MMS | 制造报文规范 | ISO-TP + UDS | ⭐⭐⭐ |
| GOOSE | 快速事件广播 | CAN 广播帧 | ⭐⭐⭐⭐⭐ |
| SV | 采样值传输 | 传感器数据流 | ⭐⭐⭐⭐ |
| SCL/ICD | 配置描述文件 | ODX / A2L | ⭐⭐⭐⭐⭐ |
| URCB/BRCB | 报告机制 | DTC 上报 / 事件记录 | ⭐⭐⭐⭐ |
| SBO | 选择-执行 | 安全访问/确认机制 | ⭐⭐⭐⭐ |
| SGCB | 定值组 | 标定数据组 | ⭐⭐⭐⭐ |

**关键区别**：
- 汽车诊断主要是"查询-响应"模式（你去问 ECU，ECU 回答）
- IEC 61850 是"发布-订阅"模式（IED 主动推送报告，客户端订阅即可）

---

## 七、常见困惑解答

### Q1: LD 和 IED 是什么关系？

一个 IED 可以有多个 LD。比如一台保护测控一体化装置：
- LD1 = 保护功能域（包含 PTOC、PDIS 等保护 LN）
- LD2 = 测量功能域（包含 MMXU、MMTR 等测量 LN）
- LD3 = 控制功能域（包含 XCBR、XSWI 等控制 LN）

类比：一台电脑（IED）可以有多个分区（LD），每个分区装不同的软件。

### Q2: CDC 和 FC 有什么区别？

- **CDC** 是"数据结构的模板"——比如 MV（测量值）这个 CDC 规定必须包含 mag（幅值）、q（品质）、t（时间戳）
- **FC** 是"数据的用途标签"——比如同一个 mag，FC=MX 表示它是测量值，FC=SP 表示它是设定值

类比：CDC 是"表格格式"，FC 是"这格数据的用途"。

### Q3: 为什么要有这么多配置文件（ICD/SCD/CID）？

这是"分离关注点"的设计：
- **ICD** 由设备厂商维护，描述"这台设备能做什么"
- **SCD** 由系统集成商维护，描述"整个系统如何配合"
- **CID** 是 SCD 的子集，描述"这台设备在这个系统里具体怎么配"

这样，换一台同型号的设备，只需要重新生成 CID，不需要改 SCD。

### Q4: GOOSE 和 SV 都是"快"，有什么区别？

| 特性 | GOOSE | SV |
|------|-------|-----|
| 数据类型 | 事件/状态（跳闸信号、开关位置）| 模拟量采样（电流、电压瞬时值）|
| 触发方式 | 事件触发 + 心跳 | 周期发送（固定频率）|
| 典型频率 | 平时 5 秒一次，事件时连发 3 次 | 每秒 80/256/4000 个采样点 |
| 可靠性机制 | 重发 + 序列号 + 生存时间 | 采样计数器 + 同步标志 |

GOOSE 是"有事发通知"，SV 是"一直发数据"。

---

## 八、记忆口诀

**信息模型层次**：
> IED 装 LD，LD 装 LN，LN 装 DO，DO 装 DA，DA 有 FC。

**配置文件流程**：
> 厂商给 ICD，集成出 SCD，现场下 CID。

**三种通信**：
> MMS 慢慢聊，GOOSE 喊一嗓，SV 一直唱。

**控制模式**：
> 先 Select 后 Operate，超时 Cancel 保安全。

---

## 九、下一步阅读建议

掌握了这些术语，你已经可以：
- 看懂 `iec61850bean` 代码里的类名（LogicalNode、FcDataObject 等）
- 理解 SCL/ICD 文件的结构
- 阅读后续 Parts 时不再被缩写困扰

推荐阅读顺序：
1. **Part 7-1**（`860[1].7-1.pdf`）：信息模型的设计原则
2. **Part 7-4**（`860[1].7-4.pdf`）：所有标准化逻辑节点的定义
3. **Part 6**（`860[1].6.pdf`）：SCL 配置语言的 XML Schema

---

## 附录：术语索引（按功能分类）

### 物理设备
- IED, SAS, MU, BCU, RTU, CT, VT, PT, NCIT

### 信息模型
- LD, LN, DO, DA, CDC, FC

### 通信服务
- ACSI, SCSM, MMS, GOOSE, SV, PDU, SDU

### 报告与控制
- RCB, URCB, BRCB, SGCB, SBO, Oper, Cancel

### 配置文件
- SCL, ICD, SSD, SCD, CID, IID, SED

### 测量与采样
- SmpCnt, SmpSynch, TCTR, TVTR

---

*文档系列：IEC 61850 标准解读 | Part 2/13 | 生成于 2026-04-08*
