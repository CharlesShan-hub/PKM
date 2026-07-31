# RFC 1155 — Structure and Identification of Management Information (SMIv1)

> **原文链接**: [https://datatracker.ietf.org/doc/html/rfc1155](https://datatracker.ietf.org/doc/html/rfc1155)
>
> **状态**: Standard Protocol (Recommended) | **废止**: RFC 1065
>
> **核心定位**: 定义 SNMP 体系中「管理信息」如何**命名（Name）**、如何**描述结构（Syntax）**、如何**编码传输（Encoding）** 的元规范。
> asn1： https://github.com/lextudio/sharpsnmppro-mib/blob/master/RFC1155-SMI.txt
> [rfc1155-asn1.md](assets/rfc1155-asn1.md.md)

---

## 1. 背景

SMI（Structure of Management Information，管理信息结构）是 SNMP 体系的"元规范"。SMI 定义了信息的三个要素：命名（Naming）、语法与编码。

| 要素 | 解决的问题 | 对应规范 |
|------|-----------|---------|
| **Naming（命名）** | 如何唯一标识一个管理对象 | OID 树（OBJECT IDENTIFIER） |
| **Syntax（语法）** | 对象的数据结构长什么样 | ASN.1 受限子集 |
| **Encoding（编码）** | 数据在网络上怎么传输 | ASN.1 BER（基本编码规则） |

## 2. 命名

名称用于标识被管理的对象。SNMP 使用 OID 树来进行描述。

```asn1
ObjectName ::= OBJECT IDENTIFIER
```

树根 → `iso(1)` / `ccitt(0)` / `joint-iso-ccitt(2)`，其中SNMP属于`iso(1)`

Internet 子树路径：`1.3.6.1` = `iso(1)` → `org(3)` → `dod(6)` → `internet(1)`

```asn1
internet     OBJECT IDENTIFIER ::= { iso org(3) dod(6) 1 }
```

子树：

```asn1
directory     OBJECT IDENTIFIER ::= { internet 1 }
mgmt          OBJECT IDENTIFIER ::= { internet 2 }
experimental  OBJECT IDENTIFIER ::= { internet 3 }
private       OBJECT IDENTIFIER ::= { internet 4 }
enterprises   OBJECT IDENTIFIER ::= { private 1 }
```

| 节点 | OID 前缀 | 用途 |
|------|---------|------|
| **directory(1)** | `1.3.6.1.1` | 保留给 OSI 目录服务（预留） |
| **mgmt(2)** | `1.3.6.1.2` | IAB 批准的**标准 MIB 对象**，如 `1.3.6.1.2.1` → MIB-I |
| **experimental(3)** | `1.3.6.1.3` | 互联网**实验性**对象 |
| **private(4)** | `1.3.6.1.4` | 厂商**私有**对象 |
| **enterprises(1)** | `1.3.6.1.4.1` | 厂商**注册产品** |

## 3. 语法

定义管理对象可以使用的数据类型，是 ASN.1 的一个**受限子集**。

### 3.1 基本类型（Primitive Types, §3.2.1）

| 类型                    | 说明                                                  |
| --------------------- | --------------------------------------------------- |
| **INTEGER**           | 整数类型。当用作枚举（ENUMERATED）时，**禁止使用值 `0`**（即枚举项不能为0）。    |
| **OCTET STRING**      | 八位位组字符串，用于表示任意二进制或文本数据（如 MAC 地址、文本描述等）。             |
| **OBJECT IDENTIFIER** | 对象标识符（OID），用于在全球命名树中唯一标识一个管理对象节点（如 `.1.3.6.1.2.1`）。 |
| **NULL**              | 空值，表示“无值”或占位符，通常用于特定场景（如 `ASN.1` 中的 `NULL` 占位）。     |

这些就是 **非聚合类型**（non-aggregate types），也叫基本类型（primitive types），是构成 List 和 Table 的基础数据单元。

```asn1
INTEGER
OCTET STRING
OBJECT IDENTIFIER
NULL
```
### 3.2 构造类型（Constructor Types, §3.2.2）

| 结构类型 | 语法形式 | 说明 |
|---------|---------|------|
| **List** | `SEQUENCE { <type1>, ..., <typeN> }` | 行记录，用于定义一条数据记录（类似于关系数据库中的一行），由多个固定字段组成。 |
| **Table** | `SEQUENCE OF <entry>` | 表（多行），由多个 List（行记录）构成的集合，用于表示一个完整的表格数据。 |
| **SEQUENCE 限制** | 不支持 `DEFAULT` / `OPTIONAL` 子句 | 所有字段必须始终存在，不允许有默认值或可选字段，目的是简化编解码设计。 |

```asn1
 SEQUENCE { <type1>, ..., <typeN> }
 SEQUENCE OF <entry>
```

### 3.3 应用定义类型（Application-wide Types, §3.2.3）

| 类型                 | ASN.1 标签          | 含义                                  | 用途说明（通俗解释）                                                                     |
| ------------------ | ----------------- | ----------------------------------- | ------------------------------------------------------------------------------ |
| **NetworkAddress** | CHOICE            | 协议族地址选择（当时只定义了 Internet 族）          | 作为一个“地址容器”，用于兼容多种网络协议地址（如 IPX、AppleTalk），但实际 SNMP 早期只用了 IPv4 地址。               |
| **IpAddress**      | `[APPLICATION 0]` | 32 位 IPv4 地址，网络字节序的 OCTET STRING(4) | 专门用来表示设备的 IPv4 地址，比如 `192.168.1.1`，管理端通过它知道是哪台设备。                              |
| **Counter**        | `[APPLICATION 1]` | 单调递增计数，达 2^32-1 后回绕                 | 用于统计**只增不减**的累计量，比如网卡收包总数、系统中断次数。到最大值后从 0 重新开始数。                               |
| **Gauge**          | `[APPLICATION 2]` | 可增可减的整数，达 2^32-1 后锁定                | 用于表示**当前状态值**，比如 CPU 使用率、内存占用、当前温度。可升可降，到最大值后“卡住”不再增加。                         |
| **TimeTicks**      | `[APPLICATION 3]` | 百分之一秒计时（相对于某个 epoch）                | 用于记录时间差/运行时长，比如“设备已启动 3 天 5 小时”，单位是 0.01 秒。                                    |
| **Opaque**         | `[APPLICATION 4]` | 任意 ASN.1 数据的“双重包装”，用于扩展             | 当作“万能袋子”，当标准类型不够用时，把复杂/自定义数据打包塞进去。后来被更现代的语法（如 SNMPv2 的 `OCTET STRING` 扩展）逐渐替代。 |

```asn1
NetworkAddress ::=
   CHOICE {
       internet
           IpAddress
   }

IpAddress ::=
   [APPLICATION 0]          -- in network-byte order
       IMPLICIT OCTET STRING (SIZE (4))

Counter ::=
   [APPLICATION 1]
       IMPLICIT INTEGER (0..4294967295)

Gauge ::=
   [APPLICATION 2]
       IMPLICIT INTEGER (0..4294967295)

TimeTicks ::=
   [APPLICATION 3]
       IMPLICIT INTEGER (0..4294967295)

Opaque ::=
   [APPLICATION 4]          -- arbitrary ASN.1 value,
       IMPLICIT OCTET STRING   --   "double-wrapped"
```

### 3.5 Encoding — 编码传输（§3.3）

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

| RFC                   | 关系                              |
| --------------------- | ------------------------------- |
| **RFC 1156 (MIB-I)**  | 基于本 SMI 定义的第一个标准管理信息库           |
| **RFC 1157 (SNMPv1)** | 基于本 SMI 定义的管理协议，规定了实例引用和 PDU 格式 |
| **RFC 1212**          | 补充 SMIv1 的**简明 MIB 定义**格式       |
| **RFC 1213 (MIB-II)** | 取代 RFC 1156，仍基于 SMIv1 但扩充了大量对象  |

> 后续演进方向：SMIv2（RFC 2578/2579/2580）在此基础上升级，引入 `Counter64`、`RowStatus`、`INDEX` 子句等。

---

## 10. 学习要点与建议

- SMI = **命名 + 语法 + 编码**，这三者是理解 SNMP 的元知识
- OID 树是 SNMP 世界的"文件系统"：`1.3.6.1.2.1` 等价于根目录 `/`
- 结合 Wireshark 抓包观察 BER 编码：看 `0x02`(INTEGER)、`0x06`(OID)、`0x30`(SEQUENCE) 等 Tag Value
- 在阅读 RFC 1213 (MIB-II) 之前，先吃透 RFC 1155，因为 MIB 中每个对象的定义都严格遵循本规范

---

*大纲整理时间: 2026-07-17*
