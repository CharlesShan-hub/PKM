# RFC 1155 — Structure and Identification of Management Information (SMIv1)

> **原文链接**: [https://datatracker.ietf.org/doc/html/rfc1155](https://datatracker.ietf.org/doc/html/rfc1155)
>
> **状态**: Standard Protocol (Recommended) | **废止**: RFC 1065
>
> **核心定位**: 定义 SNMP 体系中「管理信息」如何**命名（Name）**、如何**描述结构（Syntax）**、如何**编码传输（Encoding）** 的元规范。

---

## 1. 背景与动机

- 为什么要定义 SMI —— 统一管理信息的组织方式，避免各厂商各自为政
- 设计目标：**简单性（Simplicity）** 与 **可扩展性（Extensibility）**
- 适用范围：TCP/IP 网络的设备管理
- 与 OSI 网络管理（CMOT）的关系和区别

## 2. SMI 三大核心要素

RFC 1155 围绕三个问题展开，这也是理解 SMI 的纲领：

| 要素 | 解决的问题 | 对应规范 |
|------|-----------|---------|
| **Names（命名）** | 如何唯一标识一个管理对象 | OID 树（OBJECT IDENTIFIER） |
| **Syntax（语法）** | 对象的数据结构长什么样 | ASN.1 受限子集 |
| **Encoding（编码）** | 数据在网络上怎么传输 | ASN.1 BER（基本编码规则） |

---

## 3. Names — 对象命名与 OID 树（§3.1）

### 3.1 OID 的全局树结构
- 树根 → `iso(1)` / `ccitt(0)` / `joint-iso-ccitt(2)`
- `1.3.6.1` 路径：`iso` → `org(3)` → `dod(6)` → `internet(1)`

### 3.2 Internet 子树下的四大分支
| 节点 | OID 前缀 | 用途 |
|------|---------|------|
| **directory(1)** | `1.3.6.1.1` | 保留给 OSI 目录服务（预留） |
| **mgmt(2)** | `1.3.6.1.2` | IAB 批准的**标准 MIB 对象**，如 `1.3.6.1.2.1` → MIB-I |
| **experimental(3)** | `1.3.6.1.3` | 互联网**实验性**对象 |
| **private(4)** | `1.3.6.1.4` | 厂商**私有**对象，其下 `enterprises(1)` 用于厂商注册产品 |

### 3.3 关键约定
- 禁止使用子标识符 `0`（§4.1）—— 保留给未来扩展（这个规定后续被废除了）
- OBJECT DESCRIPTOR 必须是唯一、助记、可打印的字符串

---

## 4. Syntax — 对象的数据结构（§3.2）

定义管理对象可以使用的数据类型，是 ASN.1 的一个**受限子集**。

### 4.1 基本类型（Primitive Types, §3.2.1）
- `INTEGER`（枚举 INTEGER 禁止使用值 `0`）
- `OCTET STRING`
- `OBJECT IDENTIFIER`
- `NULL`

### 4.2 构造类型（Constructor Types, §3.2.2）
- **List**: `SEQUENCE { <type1>, ..., <typeN> }` — 行记录
- **Table**: `SEQUENCE OF <entry>` — 表（多行）
- 不支持 DEFAULT / OPTIONAL 子句（简化设计）

### 4.3 应用定义类型（Application-wide Types, §3.2.3）
| 类型                 | ASN.1 标签          | 含义                                  |
| ------------------ | ----------------- | ----------------------------------- |
| **NetworkAddress** | CHOICE            | 协议族地址选择（当时只定义了 Internet 族）          |
| **IpAddress**      | `[APPLICATION 0]` | 32 位 IPv4 地址，网络字节序的 OCTET STRING(4) |
| **Counter**        | `[APPLICATION 1]` | 单调递增计数，达 2^32-1 后回绕                 |
| **Gauge**          | `[APPLICATION 2]` | 可增可减的整数，达 2^32-1 后锁定                |
| **TimeTicks**      | `[APPLICATION 3]` | 百分之一秒计时（相对于某个 epoch）                |
| **Opaque**         | `[APPLICATION 4]` | 任意 ASN.1 数据的"双重包装"，用于扩展             |

---

## 5. Encoding — 编码传输（§3.3）

- 对象实例的值使用 **ASN.1 基本编码规则（BER）** 编码后传输
- 引用 ITU-T X.690/ISO 8825（BER 标准）
- BER 的三段式编码：**Tag + Length + Value**

---

## 6. Managed Object — 对象类型定义规范（§4）

### 6.1 对象类型定义的五个字段
1. **OBJECT**: 文本名（OBJECT DESCRIPTOR）+ OID
2. **Syntax**: 数据类型（必须是 ObjectSyntax 的子集）
3. **Definition**: 语义描述（多厂商环境必须统一语义）
4. **Access**: `read-only` / `read-write` / `write-only` / `not-accessible`
5. **Status**: `mandatory` / `optional` / `obsolete`

### 6.2 OBJECT-TYPE 宏（§4.3）
- 提供正式的 ASN.1 宏定义，方便工具化处理 MIB 定义
- 示例：`atIndex OBJECT-TYPE ::= { atEntry 1 }` 的完整宏展开

### 6.3 对象类型 vs 对象实例（§4.2）
- **对象类型**：MIB 中的声明性定义（如路由表条目）
- **对象实例**：实际绑定到具体值的实体（如某条具体路由）
- 实例引用方式由下层管理协议（SNMP/CMOT）各自定义

### 6.4 表与行的递增示例
- MIB 中通过 `atTable` → `atEntry` → `atIndex` / `atPhysAddress` / `atNetAddress` 的嵌套结构，展示了 List + Table 的标准模式

---

## 7. MIB 版本扩展规则（§5）

新版本 MIB 可以：
1. 声明旧对象为 `obsolete`（**不能删除**名称）
2. 向 List 类型**追加**新的非聚合类型
3. 定义全新对象

新版本 MIB **不可以**：
- 在不改变名称的前提下修改已有对象的语义

> 核心原则：名称的 **tail（末尾路径）** 在不同版本之间保持语义不变。

---

## 8. ASN.1 正式定义（§6）

RFC 1155 提供了完整的 ASN.1 模块 `RFC1155-SMI`，内容包括：

- OID 声明：`internet`、`directory`、`mgmt`、`experimental`、`private`、`enterprises`
- OBJECT-TYPE 宏
- `ObjectName`、`ObjectSyntax`、`SimpleSyntax`、`ApplicationSyntax`
- `NetworkAddress`、`IpAddress`、`Counter`、`Gauge`、`TimeTicks`、`Opaque`

> 这些定义是 MIB 编写的基础，后续所有 MIB 模块都会 `IMPORTS` 自这里。

---

## 9. 与其他 RFC 的关系

| RFC | 关系 |
|-----|------|
| **RFC 1156 (MIB-I)** | 基于本 SMI 定义的第一个标准管理信息库 |
| **RFC 1157 (SNMPv1)** | 基于本 SMI 定义的管理协议，规定了实例引用和 PDU 格式 |
| **RFC 1212** | 补充 SMIv1 的**简明 MIB 定义**格式 |
| **RFC 1213 (MIB-II)** | 取代 RFC 1156，仍基于 SMIv1 但扩充了大量对象 |

> 后续演进方向：SMIv2（RFC 2578/2579/2580）在此基础上升级，引入 `Counter64`、`RowStatus`、`INDEX` 子句等。

---

## 10. 学习要点与建议

- SMI = **命名 + 语法 + 编码**，这三者是理解 SNMP 的元知识
- OID 树是 SNMP 世界的"文件系统"：`1.3.6.1.2.1` 等价于根目录 `/`
- 结合 Wireshark 抓包观察 BER 编码：看 `0x02`(INTEGER)、`0x06`(OID)、`0x30`(SEQUENCE) 等 Tag Value
- 在阅读 RFC 1213 (MIB-II) 之前，先吃透 RFC 1155，因为 MIB 中每个对象的定义都严格遵循本规范

---

*大纲整理时间: 2026-07-17*
