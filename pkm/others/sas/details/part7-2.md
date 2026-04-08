# IEC 61850 Part 7-2 解读：ACSI 抽象通信服务接口

> **对应文件**：`860[1].7-2.pdf`  
> **正式标题**：IEC 61850-7-2 — Basic Communication Structure for Substation and Feeder Equipment - Abstract Communication Service Interface (ACSI)（变电站和馈线设备的基本通信结构——抽象通信服务接口）  
> **页数**：约 150 页  
> **定位**：定义 IEC 61850 的所有服务接口，是"抽象层"的核心规范

---

## 一、这一章在说什么？

Part 7-1 定义了"数据长什么样"，Part 7-2 定义了"能对这些数据做什么"。

ACSI（Abstract Communication Service Interface）是 IEC 61850 的**服务抽象层**。它定义了一套标准化的服务（读、写、报告、控制等），但不规定这些服务用什么协议实现。

**类比**：
- ACSI 就像 Java 的接口（Interface），定义了方法签名
- 具体实现（如 MMS）就像实现类（Implementation）

---

## 二、ACSI 的核心思想

### 抽象与分离

```
┌─────────────────────────────────────────────────────────────┐
│                    应用层（ACSI）                            │
│  ┌───────────────────────────────────────────────────────┐  │
│  │  服务接口：GetDataValues, SetDataValues, Report,      │  │
│  │           Select, Operate, Cancel, ...                │  │
│  │  特点：协议无关、抽象、标准化                           │  │
│  └───────────────────────────────────────────────────────┘  │
│                            │                                │
│  ┌─────────────────────────▼─────────────────────────────┐  │
│  │                 SCSM 映射层（Part 8/9）                 │  │
│  │  MMS 映射 / GOOSE 映射 / SV 映射                        │  │
│  │  特点：协议相关、具体实现                               │  │
│  └───────────────────────────────────────────────────────┘  │
│                            │                                │
│  ┌─────────────────────────▼─────────────────────────────┐  │
│  │                  传输层（TCP/IP, Ethernet）             │  │
│  │  实际的网络通信                                        │  │
│  └───────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────┘
```

**好处**：
- 上层应用不关心底层用什么协议
- 底层协议可以升级替换，不影响上层
- 不同协议映射可以共存（MMS + GOOSE + SV）

---

## 三、ACSI 服务分类

Part 7-2 定义了 6 大类服务：

| 服务类别 | 说明 | 关键服务 |
|---------|------|---------|
| **关联服务** | 建立/释放客户端与服务器的连接 | Associate, Release, Abort |
| **数据服务** | 读写数据值 | GetDataValues, SetDataValues |
| **数据集服务** | 操作数据集（批量数据）| GetDataSetValues, SetDataSetValues |
| **报告服务** | 订阅和接收报告 | Report, EnableReporting |
| **控制服务** | 控制设备（开关等）| Select, Operate, Cancel |
| **文件服务** | 传输文件（录波等）| GetFile, SetFile, DeleteFile |

---

## 四、关联服务（Association Services）

### 建立连接：Associate

```
客户端                                    服务器
   │                                         │
   │  AssociateRequest(应用引用, 认证信息)     │
   │────────────────────────────────────────>│
   │                                         │
   │         AssociateResponse(结果, 协商参数) │
   │<────────────────────────────────────────│
   │                                         │
   │         [连接建立，可以开始通信]           │
```

**关键参数**：
- **应用引用（Application Reference）**：标识客户端应用
- **认证信息（Authentication）**：用户名/密码或证书
- **协商参数（Negotiated Parameters）**：最大 PDU 大小、支持的服务等

### 释放连接：Release

正常断开连接，双方都有准备。

### 异常断开：Abort

网络故障或严重错误时的强制断开。

---

## 五、数据服务（Data Services）

### 读数据：GetDataValues

```
客户端                                    服务器
   │                                         │
   │  GetDataValuesRequest([对象引用列表])     │
   │  例如：["IED1/LD0/MMXU1.PhV.phsA.cVal.mag.f[MX]"] │
   │────────────────────────────────────────>│
   │                                         │
   │  GetDataValuesResponse([数据值列表])      │
   │  例如：[{value: 220.5, quality: 0, time: ...}] │
   │<────────────────────────────────────────│
```

**特点**：
- 可以一次读多个数据（批量读取）
- 返回值的结构包含：值（value）、品质（quality）、时间戳（timestamp）

### 写数据：SetDataValues

```
客户端                                    服务器
   │                                         │
   │  SetDataValuesRequest([对象引用, 值列表]) │
   │  例如：["IED1/LD0/CSWI1.Pos.Oper.ctlVal[CO]", true] │
   │────────────────────────────────────────>│
   │                                         │
   │  SetDataValuesResponse(结果码)            │
   │  例如：success / failure-reason          │
   │<────────────────────────────────────────│
```

**注意**：不是所有数据都能写。只有 FC=SP/CF/SV/SE 的数据才能写。

---

## 六、数据集服务（DataSet Services）

数据集（DataSet）是一组功能相关数据的集合，可以批量操作。

### 获取数据集值：GetDataSetValues

```
请求：GetDataSetValuesRequest("IED1/LD0/LLN0.dsMeasurements")

响应：GetDataSetValuesResponse([
    {ref: "MMXU1.PhV.phsA.cVal.mag.f", value: 220.5},
    {ref: "MMXU1.PhV.phsB.cVal.mag.f", value: 221.0},
    {ref: "MMXU1.PhV.phsC.cVal.mag.f", value: 220.8},
    {ref: "MMXU1.A.phsA.cVal.mag.f", value: 500.0}
])
```

**好处**：一次请求获取多个相关数据，减少通信开销。

---

## 七、报告服务（Report Services）

报告是 IEC 61850 最重要的机制之一，服务器**主动推送**数据变化给客户端。

### 报告控制块（RCB）

```
报告控制块结构（URCB/BRCB）：
├── RptID        ← 报告标识
├── DatSet       ← 关联的数据集
├── ConfRev      ← 配置版本
├── OptFlds      ← 可选字段（序号、时间戳、原因等）
├── BufTm        ← 缓冲时间（BRCB 用）
├── SqNum        ← 序列号
├── TrgOps       ← 触发条件（数据变化、品质变化等）
└── RptEna       ← 报告使能开关
```

### 报告触发条件（TrgOps）

| 触发条件 | 说明 |
|---------|------|
| **dchg** | 数据值变化（data change）|
| **qchg** | 品质变化（quality change）|
| **dupd** | 数据更新（data update，周期性）|
| **GI** | 总召唤（General Interrogation）|

### 报告流程

```
步骤1：客户端使能报告
客户端  ──EnableReporting(URCB1)──> 服务器

步骤2：服务器监测数据变化
服务器内部：MMXU1.PhV.phsA 从 220.5 变为 221.0

步骤3：服务器主动发送报告
服务器  ──Report(URCB1, 变化数据)──> 客户端

报告内容：
- RptID: "Measurements"
- SeqNum: 15
- TimeOfEntry: 2024-01-15T10:30:00.500Z
- Data: [{ref: "PhV.phsA", value: 221.0, reason: "dchg"}]
```

### URCB vs BRCB

| 特性 | URCB（非缓存） | BRCB（缓存） |
|------|--------------|-------------|
| 全称 | Unbuffered RCB | Buffered RCB |
| 行为 | 实时发送，不缓存 | 缓存事件，可补读 |
| 适用场景 | 实时监控 | 故障录波、事件顺序记录 |
| 客户端离线 | 报告丢失 | 缓存，重连后补发 |

---

## 八、控制服务（Control Services）

控制服务用于操作开关设备（断路器、隔离开关等）。

### 直接控制（Direct Control）

```
客户端                                    服务器
   │                                         │
   │  OperateRequest(对象引用, 控制值)         │
   │  例如：(XCBR1.Pos, "ON")                 │
   │────────────────────────────────────────>│
   │                                         │
   │  [服务器执行控制操作]                      │
   │                                         │
   │  OperateResponse(结果)                    │
   │<────────────────────────────────────────│
```

**特点**：简单直接，但安全性较低。

### 选择-执行控制（SBO - Select Before Operate）

```
步骤1：选择
客户端  ──SelectRequest(XCBR1.Pos)──> 服务器
服务器  ──SelectResponse(成功)───────> 客户端
        [服务器锁定该对象，其他客户端不能操作]

步骤2：执行（在超时时间内）
客户端  ──OperateRequest(XCBR1.Pos, "ON")──> 服务器
服务器  ──OperateResponse(成功)────────────> 客户端
        [执行控制，解锁对象]

或步骤2'：取消
客户端  ──CancelRequest(XCBR1.Pos)──> 服务器
服务器  ──CancelResponse(成功)───────> 客户端
        [取消操作，解锁对象]

或超时：
        [超时未收到 Operate，自动 Cancel，解锁对象]
```

**SBO 的安全性**：
- 防止重复操作（网络重传导致）
- 防止冲突操作（多个客户端同时操作）
- 提供撤销机会（选择后可以取消）

---

## 九、文件服务（File Services）

用于传输大文件，如故障录波文件、配置文件等。

### 获取文件：GetFile

```
请求：GetFileRequest("/COMTRADE/20240115_103000.cfg")

响应：GetFileResponse(文件内容)
```

### 文件目录：GetFileDirectory

```
请求：GetFileDirectoryRequest("/COMTRADE/")

响应：GetFileDirectoryResponse([
    {name: "20240115_103000.cfg", size: 2048, time: ...},
    {name: "20240115_103000.dat", size: 102400, time: ...}
])
```

---

## 十、ACSI 与 MMS 的映射关系

Part 7-2 只定义抽象服务，Part 8-1 定义如何映射到 MMS。这里是预览：

| ACSI 服务 | MMS 服务 | 说明 |
|----------|---------|------|
| Associate | Initiate | 建立连接 |
| GetDataValues | Read | 读变量 |
| SetDataValues | Write | 写变量 |
| Report | InformationReport | 主动上报 |
| Select | Write (to SBOw) | 选择操作 |
| Operate | Write (to Oper) | 执行操作 |
| GetFile | FileOpen + FileRead | 读取文件 |

---

## 十一、与汽车诊断的对比

| 特性 | IEC 61850 ACSI | 汽车 UDS |
|------|----------------|---------|
| 服务模式 | 客户端-服务器 + 发布-订阅 | 客户端-服务器（请求-响应）|
| 主动上报 | Report 机制（服务器推送）| DTC 上报（有限）|
| 批量操作 | DataSet 支持 | 有限（ReadDataByIdentifier）|
| 控制安全 | SBO 选择-执行 | 安全访问（SecurityAccess）|
| 文件传输 | 标准服务 | 标准服务（TransferData）|
| 连接管理 | Associate/Release | 诊断会话控制 |

**关键区别**：
- IEC 61850 支持**服务器主动推送**（Report），汽车诊断主要是**客户端轮询**
- IEC 61850 的**数据集**机制更高效，汽车诊断通常一次读一个 DID

---

## 十二、总结

Part 7-2 的核心：

1. **ACSI 是抽象层**——定义服务接口，不涉及具体协议
2. **六大服务类别**——关联、数据、数据集、报告、控制、文件
3. **报告是核心机制**——服务器主动推送，减少轮询
4. **SBO 保障安全**——选择-执行模式防止误操作
5. **映射到具体协议**——ACSI → MMS/GOOSE/SV

**一句话记忆**：
> ACSI = 抽象服务接口 = 读/写/报告/控制的标准化定义

---

## 下一步阅读建议

理解了 ACSI 服务，接下来要看：
- **Part 8-1**：ACSI 如何映射到 MMS——具体报文格式
- **Part 7-4**：所有逻辑节点的详细定义——哪些对象支持哪些服务
- **iec61850bean 代码**：看 Java 如何实现这些服务

---

*文档系列：IEC 61850 标准解读 | Part 7-2/13 | 生成于 2026-04-08*
