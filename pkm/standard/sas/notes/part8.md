# IEC 61850 Part 8-1 解读：SCSM-MMS 映射

> **对应文件**：`860[1].8-1.pdf`  
> **正式标题**：IEC 61850-8-1 — Specific Communication Service Mapping (SCSM) - Mappings to MMS (ISO/IEC 9506-1 and ISO/IEC 9506-2) over ISO/IEC 8802-3（特定通信服务映射——映射到 MMS）  
> **页数**：约 200 页  
> **定位**：ACSI 到 MMS 的具体映射规则，iec61850bean 的实现依据

---

## 一、这一章在说什么？

Part 8-1 是 IEC 61850 的**实现层**规范。它定义了如何把 Part 7-2 的 ACSI 抽象服务，映射到具体的 MMS（Manufacturing Message Specification）协议。

**关键理解**：
- Part 7-2 说"读数据"这个服务长什么样（抽象）
- Part 8-1 说"读数据"用 MMS 的哪个服务实现（具体）

---

## 二、MMS 简介

### 什么是 MMS？

MMS（Manufacturing Message Specification，制造报文规范）是 ISO 9506 标准，诞生于 1990 年代，用于工业自动化领域的设备通信。

**特点**：
- 基于客户端-服务器模型
- 运行在 TCP/IP 之上（端口 102）
- 支持变量读写、事件通知、文件传输
- 已被 IEC 61850 采纳为主要通信协议

### MMS 协议栈

```
┌─────────────────────────────────────┐
│           MMS 应用层                 │
│  (ISO 9506-1: 服务定义)              │
├─────────────────────────────────────┤
│           MMS 协议层                 │
│  (ISO 9506-2: 协议规范)              │
├─────────────────────────────────────┤
│           表示层 (Presentation)      │
│  (ISO 8823 / ASN.1 BER 编码)         │
├─────────────────────────────────────┤
│           会话层 (Session)           │
│  (ISO 8327)                          │
├─────────────────────────────────────┤
│           传输层                     │
│  (TCP, 端口 102)                     │
├─────────────────────────────────────┤
│           网络层/链路层              │
│  (IP / Ethernet)                     │
└─────────────────────────────────────┘
```

---

## 三、ACSI 到 MMS 的映射总览

| ACSI 服务 | MMS 服务 | 说明 |
|----------|---------|------|
| **Associate** | Initiate / Conclude | 建立/释放连接 |
| **Abort** | Abort | 异常断开 |
| **GetDataValues** | Read | 读变量值 |
| **SetDataValues** | Write | 写变量值 |
| **GetDataDirectory** | GetNameList | 获取对象列表 |
| **GetDataDefinition** | GetVariableAccessAttributes | 获取对象定义 |
| **CreateDataSet** | DefineNamedVariableList | 定义数据集 |
| **GetDataSetValues** | Read (NamedVariableList) | 读数据集 |
| **SetDataSetValues** | Write (NamedVariableList) | 写数据集 |
| **Report** | InformationReport / EventNotification | 报告/事件通知 |
| **Select** | Write (to SBOw) | 选择操作 |
| **Operate** | Write (to Oper) | 执行操作 |
| **Cancel** | Write (to Cancel) | 取消操作 |
| **GetFile** | FileOpen + FileRead | 读取文件 |
| **SetFile** | FileOpen + FileWrite | 写入文件 |

---

## 四、MMS 变量访问模型

### MMS 命名层次

```
MMS 命名空间：
├── VMD（Virtual Manufacturing Device）
│   └── 对应 IEC 61850 的 IED
│
├── Domain（域）
│   └── 对应 IEC 61850 的 LD（Logical Device）
│
├── Named Variable（命名变量）
│   └── 对应 IEC 61850 的 DO/DA
│
└── Named Variable List（命名变量列表）
    └── 对应 IEC 61850 的 DataSet
```

### 对象引用映射

```
IEC 61850 引用：
IED1/LD0/MMXU1.PhV.phsA.cVal.mag.f

映射到 MMS：
Domain: LD0
Item: MMXU1$PhV$phsA$cVal$mag$f

或（使用 AA 特定引用）：
Domain: IED1LD0
Item: MMXU1.PhV.phsA.cVal.mag.f
```

**分隔符转换**：
- IEC 61850 用 `/` 分隔层次
- MMS 用 `$` 或 `.` 分隔层次

---

## 五、关联服务映射

### Associate → MMS Initiate

```
IEC 61850 Associate Request:
├── Application Reference
├── Authentication
└── Proposed Parameters

映射到 MMS Initiate Request:
├── Initiate Request Detail
│   ├── Proposed MMS Version Number
│   ├── Proposed Parameter CBB
│   ├── Services Supported Calling
│   └── Additional Support
├── Local Detail
└── Proposed Max Serv Outstanding
```

### 连接参数协商

```
协商内容：
├── Max MMS PDU Size（最大报文大小，默认 65000）
├── Max Services Outstanding（最大并发服务数）
├── Services Supported（支持的服务列表）
└── Parameter CBB（参数支持位图）
```

---

## 六、数据服务映射

### GetDataValues → MMS Read

**请求映射**：
```
IEC 61850:
GetDataValuesRequest(
    ReferenceList: ["LD0/MMXU1.PhV.phsA.cVal.mag.f"]
)

MMS:
Read Request(
    VariableAccessSpecification: 
        ListOfVariable: [
            {Domain: "LD0", Item: "MMXU1$PhV$phsA$cVal$mag$f"}
        ]
)
```

**响应映射**：
```
IEC 61850:
GetDataValuesResponse(
    DataValueList: [
        {value: 220.5, quality: 0, timestamp: ...}
    ]
)

MMS:
Read Response(
    ListOfAccessResult: [
        {Value: {Real: 220.5}, Success}
    ]
)
```

### SetDataValues → MMS Write

**请求映射**：
```
IEC 61850:
SetDataValuesRequest(
    Reference: "LD0/CSWI1.Pos.Oper.ctlVal",
    Value: true
)

MMS:
Write Request(
    VariableAccessSpecification:
        {Domain: "LD0", Item: "CSWI1$Pos$Oper$ctlVal"},
    ListOfData: [{Boolean: true}]
)
```

---

## 七、数据集服务映射

### DataSet → MMS NamedVariableList

```
IEC 61850 DataSet:
DataSet Name: "dsMeasurements"
Members:
  - LD0/MMXU1.PhV.phsA.cVal.mag.f
  - LD0/MMXU1.PhV.phsB.cVal.mag.f
  - LD0/MMXU1.PhV.phsC.cVal.mag.f

映射到 MMS NamedVariableList:
NamedVariableList Name: "dsMeasurements"
Members:
  - {Domain: "LD0", Item: "MMXU1$PhV$phsA$cVal$mag$f"}
  - {Domain: "LD0", Item: "MMXU1$PhV$phsB$cVal$mag$f"}
  - {Domain: "LD0", Item: "MMXU1$PhV$phsC$cVal$mag$f"}
```

### GetDataSetValues → MMS Read (NamedVariableList)

```
MMS Read Request:
VariableAccessSpecification:
    VariableListName: "dsMeasurements"

MMS Read Response:
ListOfAccessResult: [
    {Value: {Real: 220.5}},
    {Value: {Real: 221.0}},
    {Value: {Real: 220.8}}
]
```

---

## 八、报告服务映射

### Report → MMS InformationReport / EventNotification

**URCB（非缓存报告）映射**：
```
IEC 61850 Report:
RptID: "URCB_Meas"
Data:
  - Reference: MMXU1.PhV.phsA.cVal.mag.f
    Value: 221.0
    Reason: data-change

MMS InformationReport:
VariableAccessSpecification:
    ListOfVariable: [
        {Domain: "LD0", Item: "MMXU1$PhV$phsA$cVal$mag$f"}
    ]
ListOfAccessResult: [
    {Value: {Real: 221.0}}
]
```

**BRCB（缓存报告）映射**：
```
BRCB 使用 MMS EventNotification 服务
包含额外的缓冲信息（序列号、缓冲时间等）
```

---

## 九、控制服务映射

### SBO 控制映射

**Select → MMS Write to SBOw**：
```
IEC 61850 Select Request:
ControlObject: "LD0/XCBR1.Pos"

MMS Write Request:
Domain: "LD0"
Item: "XCBR1$Pos$SBOw"
Data: {Structure: [
    {Boolean: true},      -- ctlVal
    {Integer: 1},         -- ctlNum
    {OctetString: ...},   -- origin
    {UtcTime: ...},       -- T
    {Boolean: false}      -- Test
]}
```

**Operate → MMS Write to Oper**：
```
MMS Write Request:
Domain: "LD0"
Item: "XCBR1$Pos$Oper"
Data: {Structure: [...]}  -- 同上
```

---

## 十、文件服务映射

### GetFile → MMS File Services

```
IEC 61850 GetFile:
FileName: "/COMTRADE/fault.cfg"

MMS 流程:
1. FileOpen Request:
   FileName: "COMTRADE/fault.cfg"
   InitialPosition: 0

2. FileOpen Response:
   FileAttributes: {size: 2048, ...}
   FrsmID: 1

3. FileRead Request:
   FrsmID: 1
   RequestedOctetCount: 2048

4. FileRead Response:
   FileData: [...]
   MoreFollows: false

5. FileClose Request:
   FrsmID: 1
```

---

## 十一、ASN.1 编码示例

MMS 使用 ASN.1 BER（Basic Encoding Rules）编码。以下是 Read Request 的编码示例：

```
MMS Read Request 的 ASN.1 结构：
Read-Request ::= SEQUENCE {
    specificationWithResult [0] IMPLICIT BOOLEAN DEFAULT TRUE,
    variableAccessSpecification VariableAccessSpecification
}

VariableAccessSpecification ::= CHOICE {
    listOfVariable          [0] IMPLICIT SEQUENCE OF ...,
    variableListName        [1] IMPLICIT ObjectName,
    ...
}

编码示例（十六进制）：
A0 1A                    -- [0] SEQUENCE (26 bytes)
  80 01 01               -- [0] BOOLEAN: TRUE
  A0 15                  -- [0] SEQUENCE (21 bytes)
    30 13                -- SEQUENCE (19 bytes)
      A1 06              -- [1] CHOICE (6 bytes)
        1A 04 4C 44 30   -- VisibleString: "LD0"
      A2 09              -- [2] CHOICE (9 bytes)
        1A 07 ...        -- VisibleString: "MMXU1$PhV$phsA$cVal$mag$f"
```

---

## 十二、与 iec61850bean 的对应

项目中的 iec61850bean 实现了 Part 8-1 的映射：

| iec61850bean 类 | 对应 MMS 功能 |
|----------------|--------------|
| `ClientAssociation` | MMS 关联管理 |
| `ServerAssociation` | MMS 服务器端 |
| `ClientSap` / `ServerSap` | 服务访问点 |
| `Read` / `Write` 方法 | MMS Read/Write 服务 |
| `FcDataObject` | MMS 变量访问 |
| `Urcb` / `Brcb` | MMS 报告机制 |

---

## 十三、总结

Part 8-1 的核心：

1. **ACSI → MMS 映射**——抽象服务到具体协议的转换
2. **命名映射**——IEC 61850 引用转换为 MMS 变量名
3. **服务映射**——每个 ACSI 服务对应 MMS 的具体服务
4. **ASN.1 编码**——MMS 报文的二进制格式

**一句话记忆**：
> Part 8-1 = ACSI 的 MMS 实现 = iec61850bean 的协议基础

---

*文档系列：IEC 61850 标准解读 | Part 8-1/13 | 生成于 2026-04-08*
