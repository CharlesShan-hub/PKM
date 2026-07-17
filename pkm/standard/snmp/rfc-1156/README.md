# RFC 1156 — Management Information Base for Network Management of TCP/IP-based Internets (MIB-I)

> **原文链接**: [https://datatracker.ietf.org/doc/html/rfc1156](https://datatracker.ietf.org/doc/html/rfc1156)
>
> **状态**: Standard Protocol (Recommended) | **废止**: RFC 1066
>
> **核心定位**: 定义了**第一个标准的管理信息库（MIB-I）**，即网络设备必须实现的管理对象集合。与 RFC 1155（SMI）、RFC 1157（SNMPv1）组成 SNMPv1 三驾马车。
>
> **后继承接**: 被 RFC 1213（MIB-II）全面取代。

---

## 1. 背景与动机（§1-§3）

- RFC 1066 的重新发布，保留技术内容不变
- **IAB 策略**：所有 IP/TCP 实现必须支持网络管理，MIB 采用**分组（Group）** 方式组织，组内所有对象必须全部实现
- 设计思想：只取**最必要的对象（essential objects）**，总数控制在约 100 个
- SMI 提供三种扩展机制：
  1. 新版本 MIB 添加新标准对象
  2. 多方实验子树
  3. 企业私有子树（enterprises）
- 入选标准（7 条关键准则）：仅限故障/配置管理、弱控制对象、有实际使用证据、总数约 100 个、不包含冗余变量、排除平台特定对象、每个关键路径每层只放一个计数器

---

## 2. 对象组织方式（§4）

### 2.1 八个对象组（Object Groups）

| 编号 | 组名 | OID | 适用性 |
|------|------|-----|--------|
| 1 | **System** | `{ mib 1 }` | 所有系统强制 |
| 2 | **Interfaces** | `{ mib 2 }` | 所有系统强制 |
| 3 | **Address Translation** | `{ mib 3 }` | 所有系统强制 |
| 4 | **IP** | `{ mib 4 }` | 强制（所有支持 IP 的系统） |
| 5 | **ICMP** | `{ mib 5 }` | 强制（所有支持 ICMP 的系统） |
| 6 | **TCP** | `{ mib 6 }` | 运行 TCP 时强制 |
| 7 | **UDP** | `{ mib 7 }` | 运行 UDP 时强制 |
| 8 | **EGP** | `{ mib 8 }` | 运行 EGP 时强制 |

### 2.2 对象定义格式（§4.2）
- 遵循 RFC 1155 SMI 规范，每个对象含五个字段：**OBJECT**（描述符 + OID）、**Syntax**（数据类型）、**Definition**（语义）、**Access**（读写级别）、**Status**（mandatory/optional/obsolete）

---

## 3. System 组 — 系统信息（§5.1）

强制实现，描述设备自身基本属性。

| 对象 | OID | 语法 | 描述 |
|------|-----|------|------|
| **sysDescr** | `{ system 1 }` | OCTET STRING | 设备的硬件/软件/网络软件描述 |
| **sysObjectID** | `{ system 2 }` | OBJECT IDENTIFIER | 厂商在 enterprises 子树下分配的唯一标识 |
| **sysUpTime** | `{ system 3 }` | TimeTicks | 网络管理子系统自上次初始化以来的时间（百分之一秒） |

---

## 4. Interfaces 组 — 网络接口（§5.2）

强制实现，描述设备上所有网络接口。

### 4.1 简单对象
| 对象 | OID | 语法 | 描述 |
|------|-----|------|------|
| **ifNumber** | `{ interfaces 1 }` | INTEGER | 网络接口总数 |

### 4.2 接口表 ifTable（§5.2.1）
- **ifTable** `{ interfaces 2 }` → SEQUENCE OF IfEntry
- **ifEntry** `{ ifTable 1 }` → 包含 22 个字段的 SEQUENCE

| 字段 | OID | 语法 | 描述 |
|------|-----|------|------|
| ifIndex | `{ ifEntry 1 }` | INTEGER | 唯一索引（1~ifNumber） |
| ifDescr | `{ ifEntry 2 }` | OCTET STRING | 接口描述 |
| ifType | `{ ifEntry 3 }` | INTEGER | 接口类型枚举（22 种：ethernet、tokenRing、fddi 等） |
| ifMtu | `{ ifEntry 4 }` | INTEGER | 最大传输单元 |
| ifSpeed | `{ ifEntry 5 }` | Gauge | 当前带宽估计（bps） |
| ifPhysAddress | `{ ifEntry 6 }` | OCTET STRING | 物理地址（MAC） |
| ifAdminStatus | `{ ifEntry 7 }` | INTEGER | 期望状态：up(1) / down(2) / testing(3) |
| ifOperStatus | `{ ifEntry 8 }` | INTEGER | 当前状态：up(1) / down(2) / testing(3) |
| ifLastChange | `{ ifEntry 9 }` | TimeTicks | 上次状态变更时的 sysUpTime |
| ifInOctets | `{ ifEntry 10 }` | Counter | 接收字节数 |
| ifInUcastPkts | `{ ifEntry 11 }` | Counter | 接收单播包数 |
| ifInNUcastPkts | `{ ifEntry 12 }` | Counter | 接收非单播包数（广播+多播） |
| ifInDiscards | `{ ifEntry 13 }` | Counter | 入方向丢弃包数（无错误） |
| ifInErrors | `{ ifEntry 14 }` | Counter | 入方向错误包数 |
| ifInUnknownProtos | `{ ifEntry 15 }` | Counter | 未知协议丢弃数 |
| ifOutOctets | `{ ifEntry 16 }` | Counter | 发送字节数 |
| ifOutUcastPkts | `{ ifEntry 17 }` | Counter | 发送单播包数 |
| ifOutNUcastPkts | `{ ifEntry 18 }` | Counter | 发送非单播包数 |
| ifOutDiscards | `{ ifEntry 19 }` | Counter | 出方向丢弃包数（无错误） |
| ifOutErrors | `{ ifEntry 20 }` | Counter | 出方向错误包数 |
| ifOutQLen | `{ ifEntry 21 }` | Gauge | 输出队列长度 |

---

## 5. Address Translation 组 — 地址转换表（§5.3）

强制实现，用于将网络地址（IP）映射到物理地址。相当于**ARP 缓存**的抽象。

| 对象 | OID | 语法 | 描述 |
|------|-----|------|------|
| **atTable** | `{ at 1 }` | SEQUENCE OF AtEntry | 地址转换表 |
| **atEntry** | `{ atTable 1 }` | SEQUENCE | 单条映射条目 |
| atIfIndex | `{ atEntry 1 }` | INTEGER | 对应接口索引 |
| atPhysAddress | `{ atEntry 2 }` | OCTET STRING | 物理地址 |
| atNetAddress | `{ atEntry 3 }` | NetworkAddress | 网络地址（IP） |

> 注：MIB-II（RFC 1213）中该组被标记为废弃（deprecated），由每个网络层协议的专用表替代。

---

## 6. IP 组 — IP 协议统计（§5.4）

### 6.1 标量对象

| 对象 | OID | 语法 | 描述 |
|------|-----|------|------|
| **ipForwarding** | `{ ip 1 }` | INTEGER | gateway(1) / host(2) |
| **ipDefaultTTL** | `{ ip 2 }` | INTEGER | 默认 TTL 值 |
| **ipInReceives** | `{ ip 3 }` | Counter | 接收 IP 数据报总数 |
| **ipInHdrErrors** | `{ ip 4 }` | Counter | 头部错误丢弃数 |
| **ipInAddrErrors** | `{ ip 5 }` | Counter | 地址错误丢弃数 |
| **ipForwDatagrams** | `{ ip 6 }` | Counter | 转发数据报数 |
| **ipInUnknownProtos** | `{ ip 7 }` | Counter | 未知协议丢弃数 |
| **ipInDiscards** | `{ ip 8 }` | Counter | 入方向丢弃数（无错误） |
| **ipInDelivers** | `{ ip 9 }` | Counter | 成功交付给上层协议数 |
| **ipOutRequests** | `{ ip 10 }` | Counter | 本地发出请求数 |
| **ipOutDiscards** | `{ ip 11 }` | Counter | 出方向丢弃数 |
| **ipOutNoRoutes** | `{ ip 12 }` | Counter | 无路由丢弃数 |
| **ipReasmTimeout** | `{ ip 13 }` | INTEGER | 分片重组超时（秒） |
| **ipReasmReqds** | `{ ip 14 }` | Counter | 需要重组的片数 |
| **ipReasmOKs** | `{ ip 15 }` | Counter | 成功重组的片数 |
| **ipReasmFails** | `{ ip 16 }` | Counter | 重组失败数 |
| **ipFragOKs** | `{ ip 17 }` | Counter | 成功分片的数 |
| **ipFragFails** | `{ ip 18 }` | Counter | 分片失败数 |
| **ipFragCreates** | `{ ip 19 }` | Counter | 创建的分片数 |
| **ipRoutingDiscards** | `{ ip 23 }` | Counter | 路由丢弃数 |

### 6.2 表对象

#### IP 地址表 ipAddrTable（§5.4.1）
- **ipAddrTable** `{ ip 20 }` → 绑定到本机的 IP 地址列表
- **ipAdEntAddr** / **ipAdEntIfIndex** / **ipAdEntNetMask** / **ipAdEntBcastAddr** / **ipAdEntReasmMaxSize**

#### IP 路由表 ipRoutingTable（§5.4.2）
- **ipRoutingTable** `{ ip 21 }` → IP 路由表
- 关键字段：**ipRouteDest**、**ipRouteIfIndex**、**ipRouteMetric1~5**、**ipRouteNextHop**、**ipRouteType**（other(1)/invalid(2)/direct(3)/indirect(4)）、**ipRouteProto**、**ipRouteAge**、**ipRouteMask**、**ipRouteInfo**

---

## 7. ICMP 组 — ICMP 协议统计（§5.5）

- 共约 26 个 Counter 对象，覆盖各类 ICMP 消息的收发统计
- 包括：**icmpInMsgs**、**icmpInErrors**、**icmpInDestUnreachs**、**icmpInTimeExcds**、**icmpInParmProbs**、**icmpInSrcQuenchs**、**icmpInRedirects**、**icmpInEchos**、**icmpInEchoReps**、**icmpInTimestamps**、**icmpInTimestampReps**、**icmpInAddrMasks**、**icmpInAddrMaskReps**
- 以及对应的 **icmpOut*** 出方向统计

---

## 8. TCP 组 — TCP 协议统计（§5.6）

| 对象 | 描述 |
|------|------|
| **tcpRtoAlgorithm** | 重传超时算法（other(1)/constant(2)/rsre(3)/vanj(4)） |
| **tcpRtoMin** | 最小重传超时（毫秒） |
| **tcpRtoMax** | 最大重传超时（毫秒） |
| **tcpMaxConn** | 最大连接数（-1 表示动态） |
| **tcpActiveOpens** | 活跃打开连接数 |
| **tcpPassiveOpens** | 被动打开连接数 |
| **tcpAttemptFails** | 连接尝试失败数 |
| **tcpEstabResets** | 已建立连接的复位数 |
| **tcpCurrEstab** | 当前 ESTABLISHED 状态的连接数 |
| **tcpInSegs** / **tcpOutSegs** | 收发段数 |
| **tcpRetransSegs** | 重传段数 |
| **tcpConnTable** | TCP 连接表（本地/远端地址、端口、状态） |

### TCP 连接表 tcpConnTable
- 关键字段：**tcpConnState**（closed(1)~timeWait(11) 全状态枚举）、**tcpConnLocalAddress**、**tcpConnLocalPort**、**tcpConnRemAddress**、**tcpConnRemPort**

---

## 9. UDP 组 — UDP 协议统计（§5.7）

| 对象 | 描述 |
|------|------|
| **udpInDatagrams** | 接收 UDP 数据报数 |
| **udpNoPorts** | 无端口收到的数据报数 |
| **udpInErrors** | 入方向错误数 |
| **udpOutDatagrams** | 发送 UDP 数据报数 |
| **udpTable** | UDP 监听表（本地地址 + 本地端口） |

---

## 10. EGP 组 — EGP 协议统计（§5.8）

- **egpInMsgs** / **egpInErrors** / **egpOutMsgs** / **egpOutErrors**
- **egpNeighTable**：EGP 邻居表，包含邻接状态、模式、AS 号等
- **egpAs**：本机自治系统号

---

## 11. ASN.1 正式定义（§6）

模块 `RFC1156-MIB` 定义：

- 导入自 `RFC1155-SMI`：`mgmt`、`OBJECT-TYPE`、`NetworkAddress`、`IpAddress`、`Counter`、`Gauge`、`TimeTicks`
- 八个组 OID：`mib(1)` → system(1) / interfaces(2) / at(3) / ip(4) / icmp(5) / tcp(6) / udp(7) / egp(8)
- 所有对象的完整 `OBJECT-TYPE` 宏定义和 ASN.1 类型声明

---

## 12. 与其他 RFC 的关系

| RFC | 关系 |
|-----|------|
| **RFC 1155 (SMIv1)** | 本 MIB 遵循的元规范——定义数据类型、OID 结构和编码方式 |
| **RFC 1157 (SNMPv1)** | 本 MIB 通过 SNMPv1 协议访问，协议定义实例引用方式 |
| **RFC 1213 (MIB-II)** | **取代** RFC 1156，增加了更多组（如 CMOT、SNMP、DNS 等），修正了设计问题 |
| **RFC 1066** | RFC 1156 是 RFC 1066 的重新发布（内容不变） |

---

## 13. 学习要点与建议

- MIB-I 约含 **115 个对象**，分为 8 个组。用一个 `snmpwalk` 就能基本扫完这些对象
- **System 组**是入门最佳切入点：`sysDescr` 看设备描述、`sysObjectID` 看厂商标识、`sysUpTime` 看运行时长
- **Interfaces 组**是最常用的性能监控对象族，`ifInOctets`/`ifOutOctets` 是流量统计的基础
- **TCP 连接表**的 `tcpConnState` 枚举了完整的 TCP 状态机（11 种状态），是理解 TCP 的窗口
- MIB-I 的 **Address Translation 组**和 IP 路由表设计在后来的 MIB-II 中都有显著改进，阅读时可以对比

---

*大纲整理时间: 2026-07-17*
