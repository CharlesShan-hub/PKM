# SNMP（Simple Network Management Protocol）

## Overview

本专题从技术背景，到标准解读，最后到代码实现，完整的解析SNMP的前世今生。下面是整理一些有用的链接：
* 博客
    * [什么是SNMP](https://support.huawei.com/enterprise/zh/doc/EDOC1100087025/5d668861)

## Articles

* 介绍
    * [CMOT和SNMP](details/cmot-vs-snmp.md)

## Plan 

| 学习阶段        | 推荐研读的RFC（核心）                         | 说明与重点                              |
| ----------- | ------------------------------------ | ---------------------------------- |
| **SMIv1**   | RFC 1155, RFC 1212, RFC 1215         | 三者合在一起才是完整的SMIv1定义体系。              |
| **MIB-II**  | RFC 1213                             | 经典的设备基础MIB，虽古老但思想沿用至今。             |
| **SMIv2**   | RFC 2578, RFC 2579, RFC 2580         | 现代SNMP的数据定义语言，必读。                  |
| **通用MIB**   | RFC 3418                             | 定义了SNMP引擎自身的MIB，替代了旧版的部分MIB。       |
| **SNMPv1**  | RFC 1157                             | 核心协议操作，理解5种基本PDU。                  |
| **SNMPv2c** | **RFC 1905（核心）**， RFC 1901（背景）       | 重点学习`GetBulk`和`Inform`，这是v2c的最大贡献。 |
| **SNMPv3**  | **RFC 3411, 3412, 3413, 3414, 3415** | 这是STD 62的核心五部曲。你的重点（USM、VACM）完全正确。 |

**总结一句**：你提供的是一个**80分的学习框架**，大方向极佳，但在具体的RFC编号和归属上存在一些“民间理解”与“官方定义”的偏差。按照我上面修正后的表格去读，你的路线会更严谨，少走弯路。

从标准的权威角度深入学习 SNMP（简单网络管理协议），应当直接追踪 **IETF（互联网工程任务组）发布的 RFC（Request for Comments）标准文件**。 [[1](https://en.wikipedia.org/wiki/Simple_Network_Management_Protocol)]

以下是为您整理的系统性标准学习路线与核心规范导航：

1. 第一步：理解管理信息结构（SMI 与 MIB）

在看协议报文之前，必须先理解 SNMP 如何定义设备上的数据。

- **[RFC 1155](https://datatracker.ietf.org/doc/html/rfc1157) (SMIv1)**：定义了管理信息的结构与识别，规定了如何使用 ASN.1 语法和 OID（对象标识符）树状结构来描述网络设备。 [[1](https://info.support.huawei.com/info-finder/encyclopedia/en/SNMP.html), [2](https://ithelp.ithome.com.tw/articles/10275997)]
- **RFC 2578 (SMIv2)**：对 SMIv1 的全面升级，引入了更丰富的数据类型（如 Counter64）和宏定义。 [[1](https://support.huawei.com/enterprise/en/doc/EDOC1100365086/53a54b/overview-of-snmp)]
- **RFC 1213 (MIB-II)**：最核心的设备基础数据库标准，定义了所有网络设备必须支持的通用管理对象（如系统信息 `system`、网络接口 `interfaces`、IP/TCP/UDP 统计等）。

2. 第二步：按版本演进研读协议标准

每一个版本的 RFC 都详细规范了报文格式（PDU）、状态机以及行为定义： [[1](https://datatracker.ietf.org/doc/html/rfc3411)]

- **SNMPv1（基础与历史）**
    - **RFC 1157**：SNMPv1 的核心规范。重点学习：5种基本 PDU（Get, GetNext, Set, GetResponse, Trap）的封装格式，以及基于 Community（团体名）的明文认证机制。 [[1](https://support.huawei.com/enterprise/en/doc/EDOC1100365086/53a54b/overview-of-snmp), [2](https://info.support.huawei.com/info-finder/encyclopedia/en/SNMP.html), [3](https://ithelp.ithome.com.tw/articles/10275997), [5](https://www.cnblogs.com/LittleHann/p/3834860.html)]
- **SNMPv2c（增强与扩展）**
    - **RFC 1901 & RFC 1905**：定义了文本约定及协议操作。重点学习：新增的 **GetBulk**（批量获取）和 **Inform**（带确认的告警）操作，极大地优化了高带宽下的数据采集效率。 [[1](https://support.huawei.com/enterprise/en/doc/EDOC1100365086/53a54b/overview-of-snmp), [2](https://info.support.huawei.com/info-finder/encyclopedia/en/SNMP.html)]
- **SNMPv3（现代安全架构体系）**
    - SNMPv3 不再是一篇简单的文档，而是一个完整的 **STD 62（标准62号序列）** 框架。
    - **[RFC 3411](https://datatracker.ietf.org/doc/html/rfc3411)**：SNMP 实体架构，了解调度器（Dispatcher）、消息处理子系统等标准模块。
    - **RFC 3414 (USM)**：基于用户的安全模型，详细拆解了如何使用 HMAC-MD5/SHA 算法提供认证，以及使用 DES/AES 提供数据加密。
    - **RFC 3415 (VACM)**：基于视图的访问控制模型，规范了如何细粒度地为不同用户指派 MIB 树的读、写、告警权限。 [[1](https://www.snmp.com/snmpv3/v3white.shtml), [2](https://en.wikipedia.org/wiki/Simple_Network_Management_Protocol), [3](https://blog.csdn.net/fw0124/article/details/8557029), [4](https://www.scribd.com/document/582101821/L33-SNMPv3), [5](https://www.geeksforgeeks.org/computer-networks/simple-network-management-protocol-snmp/), [6](https://snmp.com/products/techinfo/secmodels.shtml), [7](https://info.support.huawei.com/info-finder/encyclopedia/en/SNMP.html)]

3. 第三步：配套的标准数据表示法（ASN.1 与 BER）

SNMP 的报文在传输时并不是纯文本或普通二进制，而是通过标准的 **ASN.1（抽象语法标记）** 描述，并使用 **BER（基本编码规则）** 进行序列化。 [[1](https://www.tsnien.idv.tw/Internet_WebBook/Book_PDF/%E7%AC%AC%E5%8D%81%E5%85%AD%E7%AB%A0%20SNMP%20%E7%B6%B2%E8%B7%AF%E7%AE%A1%E7%90%86%E5%8D%94%E5%AE%9A.pdf)]

- 若想从字节码层面看懂抓包数据（例如为什么 `0x02` 代表整数，`0x06` 代表 OID），需查阅 **ITU-T X.690** 标准（或相关的 ASN.1 编程教材）。

💡 辅助标准学习的实用建议

- **结合 Wireshark 抓包验证**：在阅读 RFC 的 PDU 结构时，使用 [Wireshark](https://www.wireshark.org/) 抓取一段 `snmpwalk` 或 `snmptrap` 的真实流量。Wireshark 的解析树是严格按照 RFC 规范定义的，对照标准看字段能产生具象化的理解。
- **官方标准门户**：可直接在 [IETF Datatracker](https://datatracker.ietf.org/) 中搜索上述 RFC 编号。它提供了标准的历史演进图（如哪篇 RFC 替代了哪篇），能清晰看到技术标准的生命周期。