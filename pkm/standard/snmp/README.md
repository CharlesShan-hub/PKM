# SNMP（Simple Network Management Protocol）

## Overview

本专题从技术背景，到标准解读，最后到代码实现，完整地解析 SNMP 的前世今生。

**有用链接：**
* 博客：[什么是SNMP](https://support.huawei.com/enterprise/zh/doc/EDOC1100087025/5d668861)
* 学习资料：[di-mgt.com.au - A Guide to ASN.1](https://di-mgt.com.au/guidumpasn1.html)
* MIB资源：[GitHub - lextudio/sharpsnmppro-mib](https://github.com/lextudio/sharpsnmppro-mib) (所有经典MIB库)
* 书籍：深入理解Net-Snmp (实战) (张春强)
* 书籍：Essential SNMP, Second Edition (Douglas R Mauro Douglas, Kevin Schmidt)
* 书籍：SNMP Mastery (Michael W Lucas)

## Learning Roadmap

### Phase 1: Foundation - SMI & MIB (理解数据定义)
| 阶段 | 核心 RFC | 目标 |
| :--- | :--- | :--- |
| **SMIv1** | 1155, 1212, 1215 | 理解ASN.1基础，OID树结构，以及如何定义一个MIB对象。 |
| **MIB-II** | 1213 (核心设备库) | 了解最经典、最基础的网络设备管理信息库。 |
| **SMIv2** | 2578, 2579, 2580 | 掌握现代的MIB定义语言，这是后续阅读的基础。 |

### Phase 2: Core Protocol Versions (理解协议操作)
| 版本 | 核心 RFC | 目标 |
| :--- | :--- | :--- |
| **SNMPv1** | 1157 | 理解5种PDU (Get, GetNext, Set, Response, Trap) 和Community安全模型。 |
| **SNMPv2c** | 1905 (协议核心), 1906 (传输映射) | 掌握GetBulk和Inform操作，理解其与v1的改进。 |
| **SNMPv3** (STD 62) | **3411** (架构), 3412 (消息处理), 3413 (应用), **3414** (USM), **3415** (VACM) | 核心是**USM** (用户安全模型)和**VACM** (视图访问控制模型)。掌握现代SNMP的安全、认证和授权机制。 |

### Phase 3: Advanced Topics (成为大师的路径)
*   **ASN.1 & BER 编码 (ITU-T X.690)**：从字节码层面理解SNMP报文。结合Wireshark抓包验证。
*   **Agent/Manager 实现**：阅读 `net-snmp` (C) 或 `pysnmp` (Python) 源码，理解RFC究竟是如何被实现的。
*   **MIB 设计与开发**：能够根据需求，使用SMIv2语法独立编写一个私有的MIB文件。
*   **高可用与性能**：深入SNMP over TCP, 代理架构 (Proxy Forwarder), 以及大规模设备管理中的性能优化。

## Articles

### Introduction
*   [CMOT 和 SNMP](details/cmot-vs-snmp.md)

### SNMPv1 Architecture
*   **SMI (数据定义)**
    *   [rfc1155](rfc-1155/README.md): SNMPv1 SMI 核心语法定义。
    *   [rfc1212](rfc-1212/README.md): OBJECT-TYPE 宏，定义具体对象的模板。
    *   [rfc1215](rfc-1215/README.md): 定义如何描述告警事件 (Trap)。
*   **SNMP (协议)**
    *   [rfc1157](rfc-1157/README.md): SNMPv1 协议规范。
*   **MIB (管理信息库)**
    *   [rfc1156](rfc-1156/README.md): MIB-I (已废弃，但具有历史意义)。
    *   [rfc1213](rfc-1213/README.md): MIB-II (核心标准，取代 rfc1156)。

### SNMPv2c Architecture
*   **SMI (数据定义)**
    *   [rfc2578](rfc-2578/README.md): SMIv2 规范 (沿用至v3)。
    *   [rfc2579](rfc-2579/README.md): 文本约定 (沿用至v3)。
    *   [rfc2580](rfc-2580/README.md): 一致性声明 (沿用至v3)。
*   **SNMP (协议)**
    *   [rfc1901](rfc-1901/README.md): 背景引言 (了解即可)。
    *   [rfc1905](rfc-1905/README.md): 协议操作核心 (GetBulk, Inform)。
    *   [rfc1906](rfc-1906/README.md): 传输映射 (UDP, 等)。
*   **MIB (管理信息库)**
    *   [rfc1213](rfc-1213/README.md): MIB-II (沿用)。
    *   [rfc1907](rfc-1907/README.md): SNMPv2 MIB。

### SNMPv3 Architecture
*   **SMI (数据定义)**
    *   [rfc2578](rfc-2578/README.md): SMIv2 (沿用)。
    *   [rfc2579](rfc-2579/README.md): 文本约定 (沿用)。
    *   [rfc2580](rfc-2580/README.md): 一致性声明 (沿用)。
*   **SNMP (协议与安全)**
    *   [rfc3411](rfc-3411/README.md): 架构概述 (Dispatcher, Message Processing Subsystem)。
    *   [rfc3412](rfc-3412/README.md): 消息处理与分发模型。
    *   [rfc3413](rfc-3413/README.md): SNMP应用 (命令生成器、通知接收器等)。
    *   [rfc3414](rfc-3414/README.md): USM (用户安全模型) —— 核心：认证 (MD5/SHA) 与加密 (DES/AES)。
    *   [rfc3415](rfc-3415/README.md): VACM (视图访问控制模型) —— 核心：细粒度的读/写/通知权限控制。
*   **MIB (管理信息库)**
    *   [rfc1213](rfc-1213/README.md): MIB-II (沿用)。
    *   [rfc3418](rfc-3418/README.md): SNMPv3 MIB (引擎自身的MIB，如 snmpEngine、snmpTarget)。