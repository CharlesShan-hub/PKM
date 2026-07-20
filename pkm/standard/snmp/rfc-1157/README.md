# RFC 1157 — A Simple Network Management Protocol (SNMPv1)

> **原文链接**: [https://datatracker.ietf.org/doc/html/rfc1157](https://datatracker.ietf.org/doc/html/rfc1157)
>
> **状态**: Standard Protocol (Recommended) | **废止**: RFC 1098
>
> **核心定位**: 定义了 SNMPv1 的**协议规范**——管理站与代理之间如何通信、交换哪些消息、消息的格式与处理规则。与 RFC 1155（SMI）、RFC 1156（MIB-I）组成 SNMPv1 三驾马车。
>
> **参考**: 前身为 SGMP（Simple Gateway Monitoring Protocol），**不向后兼容**。分配了新 UDP 端口。

---

## 1. Status of this Memo & Introduction（§1-§2）

* 简单网关监控协议（**SGMP** - RFC 1098）：SNMP（RFC - 1157）的前身。rfc1157对其进行分叉，不在追踪其后续进展。SGMP只监控网关（路由器），SNMP 将其泛化为管理所有网络设备的通用协议。
* OSI 网络管理（CMIS/CMIP）（**CMOT**（RFC-1095））：由于 IAB 双轨策略打算以后使用，但后来废弃。
- **SNMP**：定位是简单、可快速部署的短期方案。后来成功普及，成为事实标准。SNMP 进行了新 UDP 端口分配：代理监听 **161**，Trap 接收 **162**。

---

## 2. Architecture（§3）

名词解析：考虑下面场景，公司有一个主交换机，各自连接到一楼到六楼的楼层交换机，他们所有都打开了SNMP协议。我在某一个未知请求他们，获取网络拓扑结构。
* SNMP：管理站与代理之间传递管理信息的协议
* 管理站：我的电脑（运行的 SNMP 管理应用程序）
* 网络元素：中心和楼层交换机
* Agent：每个交换机上运行的 SNMP 代理
* 被管对象：每个交换机的端口状态、流量、MAC 表等

### 3.2 架构六要素（§3.2）

| 要素                     | 说明                                                       |
| ---------------------- | -------------------------------------------------------- |
| **管理信息的范围**（§3.2.1）    | 仅包含 MIB 中的非聚合（non-aggregate）对象类型                         |
| **管理信息的表示**（§3.2.2）    | 使用 ASN.1 受限子集（同 SMI），BER 编码使用**定长形式**                    |
| **支持的操作**（§3.2.3）      | 本质上只有两种：**get**（取值）和 **set**（赋值）；通过**轮询 + 有限 Trap** 实现监控 |
| **协议交换的形式与含义**（§3.2.4） | 基于不可靠数据报（UDP），每条消息独立由单个数据报表示                             |
| **管理关系定义**（§3.2.5）     | Community（团体）体系                                          |
| **管理对象引用**（§3.2.6）     | 对象实例的命名规则                                                |

### 3.3 关键概念：Community 模型（§3.2.5）

SNMPv1 的安全模型完全基于 **Community（团体）** 字符串：

| 概念 | 定义 |
|------|------|
| **SNMP Community** | 代理（Agent）与一组管理应用的配对关系，用 **community name**（OCTET STRING）标识 |
| **Authentication Scheme** | 鉴定消息是否属于某 Community 的规则集；v1 仅提供**弱认证**（community 字符串明文传输） |
| **SNMP MIB View** | 某个网络元素上可访问的 MIB 对象子集 |
| **SNMP Access Mode** | READ-ONLY 或 READ-WRITE |
| **SNMP Community Profile** | MIB View + Access Mode 的组合 |
| **SNMP Access Policy** | Community + Profile 的组合，定义了代理对某个 Community 的授权 |
| **SNMP Proxy Agent** | 提供协议转换，允许管理站通过代理管理非 SNMP 设备 |

> **关键**：v1 没有加密，community 字符串以明文出现在每个消息中，是后来 SNMPv3 USM 要解决的核心问题之一。

---

## 4. 对象实例的命名（§3.2.6）

SNMP 如何唯一标识某个具体对象实例？规则如下：

### 4.1 标量对象
- 格式：`对象类型OID . 0`
- 示例：`sysDescr.0` → `1.3.6.1.2.1.1.1.0`

### 4.2 表对象

| 表 | 实例标识方式 | 示例 | 注释 |
|----|-------------|------|------|
| **ifTable** | `类型OID . ifIndex` | `ifType.2` | 按接口索引，唯一标识一个接口 |
| **atTable** | `类型OID . ifIndex . IP地址` | `atPhysAddress.3.1.89.1.1.42` | 接口 3 上 IP 为 89.1.1.42 的地址转发表条目 |
| **ipAddrTable** | `类型OID . IP地址` | `ipAdEntNetMask.89.1.1.42` | 设备上 IP 地址为 89.1.1.42 的接口配置条目 |
| **ipRoutingTable** | `类型OID . 目的地址` | `ipRouteNextHop.89.1.1.42` | 以 89.1.1.42 为目的的路由条目 |
| **tcpConnTable** | `类型OID . 本地IP.本地端口.远端IP.远端端口` | `tcpConnState.89.1.1.42.21.10.0.0.51.2059` | TCP 连接：本地 89.1.1.42:21 → 远端 10.0.0.51:2059 |
| **egpNeighTable** | `类型OID . 邻居IP` | `egpNeighState.89.1.1.42` | EGP 邻居 89.1.1.42 的邻居关系状态 |

> **核心思想**：所有实例名按**字典序（lexicographical order）** 组织，这是 GetNextRequest 实现表遍历的基础。

---

## 5. 协议规范（§4）
### 5.1 消息格式 — Message 结构

```
Message ::= SEQUENCE {
    version     INTEGER { version-1(0) },
    community   OCTET STRING,
    data        ANY     -- PDU
}
```

- 版本固定为 `version-1(0)`
- Community 为明文
- PDU 通过 ASN.1 BER 编码后放入 data 字段

### 5.2 五种 PDU 类型

| PDU                    | ASN.1 Tag | 方向              | 说明                       |
| ---------------------- | --------- | --------------- | ------------------------ |
| **GetRequest-PDU**     | `[0]`     | Manager → Agent | 请求获取一个或多个变量的值            |
| **GetNextRequest-PDU** | `[1]`     | Manager → Agent | 请求获取字典序下一个变量的值，用于**遍历表** |
| **GetResponse-PDU**    | `[2]`     | Agent → Manager | 对 Get/GetNext/Set 请求的响应  |
| **SetRequest-PDU**     | `[3]`     | Manager → Agent | 设置一个或多个变量的值              |
| **Trap-PDU**           | `[4]`     | Agent → Manager | **主动上报**事件（无需轮询）         |

### 5.3 五种 PDU 的公共结构

GetRequest / GetNextRequest / GetResponse / SetRequest 共享同一个 `PDU` 结构：

```asn1
PDU ::= SEQUENCE {
    request-id        INTEGER,
    error-status      INTEGER { noError(0), tooBig(1), noSuchName(2),
                                badValue(3), readOnly(4), genErr(5) },
    error-index       INTEGER,
    variable-bindings VarBindList
}
```

| 错误码 | 含义 | 触发场景 |
|--------|------|---------|
| noError(0) | 无错误 | 正常响应 |
| tooBig(1) | 响应超长 | 响应超过 484 字节限制 |
| noSuchName(2) | 变量不存在 | Get/GetNext 请求了不存在的变量 |
| badValue(3) | 值不正确 | Set 请求的值类型/长度不匹配 |
| readOnly(4) | 只读 | Set 请求尝试写只读变量 |
| genErr(5) | 其他错误 | 无法归类的错误 |

### 5.4 GetRequest 处理流程（§4.1.2）
1. 变量名不存在 → `noSuchName`
2. 变量是聚合类型 → `noSuchName`
3. 响应超限 → `tooBig`
4. 其他无法获取 → `genErr`
5. 正常 → 返回 `noError` + 所有变量的值

### 5.5 GetNextRequest 与表遍历（§4.1.3、§4.1.3.1）

- GetNextRequest 在字典序中找到**紧邻的下一个**变量
- 这是 SNMP 中**遍历表**的核心机制 —— 不需要知道表有多大
- §4.1.3.1 给出了完整的路由表示例遍历过程

### 5.6 SetRequest 处理流程（§4.1.5）
1. 变量不可写 → `noSuchName`
2. 值类型/长度不符 → `badValue`
3. 响应超限 → `tooBig`
4. 其他 → `genErr`
5. 正常 → 所有变量**原子式同步赋值**，返回 `noError`

### 5.7 Trap-PDU（§4.1.6）

Trap 是**唯一由 Agent 主动发起**的 PDU，结构与其他不同：

```
Trap-PDU ::= SEQUENCE {
    enterprise        OBJECT IDENTIFIER,   -- 产生 trap 的设备类型 (sysObjectID)
    agent-addr        NetworkAddress,      -- 产生 trap 的设备地址
    generic-trap      INTEGER { 0..6 },    -- 通用 trap 类型
    specific-trap     INTEGER,             -- 企业自定义 trap 码
    time-stamp        TimeTicks,           -- 自上次初始化以来的时间
    variable-bindings VarBindList          -- 附加信息
}
```

#### 7 种通用 Trap 类型

| 类型 | 值 | 含义 |
|------|-----|------|
| **coldStart** | 0 | 代理**冷启动** — 配置或实现可能已改变 |
| **warmStart** | 1 | 代理**热启动** — 配置未改变 |
| **linkDown** | 2 | 通信链路故障，VarBind 首项为 `ifIndex` |
| **linkUp** | 3 | 通信链路恢复，VarBind 首项为 `ifIndex` |
| **authenticationFailure** | 4 | 认证失败（可配置抑制） |
| **egpNeighborLoss** | 5 | EGP 邻居关系中断，VarBind 首项为 `egpNeighAddr` |
| **enterpriseSpecific** | 6 | 企业自定义事件，`specific-trap` 标识具体类型 |

### 5.8 变量绑定（VarBind / VarBindList）

```
VarBind ::= SEQUENCE {
    name    ObjectName,
    value   ObjectSyntax
}
VarBindList ::= SEQUENCE OF VarBind
```

- 一个 PDU 可以携带**多个** VarBind，实现一次请求读写多个变量
- GetRequest 的 value 部分为 NULL（被忽略）
- 建议的最大消息长度：**484 字节**（最早的实现限制）

---

## 6. ASN.1 正式定义（§5）

模块 `RFC1157-SNMP` 定义：

- **导入自 RFC1155-SMI**：`ObjectName`、`ObjectSyntax`、`NetworkAddress`、`IpAddress`、`TimeTicks`
- **Message**：顶层消息结构
- **PDUs**：五种 PDU 的 CHOICE
- **GetRequest-PDU / GetNextRequest-PDU / GetResponse-PDU / SetRequest-PDU**：共享 `PDU` 结构
- **Trap-PDU**：独立的结构（enterprise、agent-addr、generic-trap、specific-trap、time-stamp）
- **VarBind / VarBindList**：变量绑定

---

## 7. 协议操作总结

| 操作              | 方向    | 典型用途                  |
| --------------- | ----- | --------------------- |
| **Get**         | M → A | 查询设备的一个或多个变量          |
| **GetNext**     | M → A | 遍历表、发现未知对象            |
| **GetResponse** | A → M | 对 Get/GetNext/Set 的应答 |
| **Set**         | M → A | 修改设备配置、触发动作           |
| **Trap**        | A → M | 事件上报（启动、故障、认证失败等）     |

---

## 8. 与其他 RFC 的关系

| RFC | 关系 |
|-----|------|
| **RFC 1155 (SMIv1)** | 定义数据类型和 OID 结构，本协议中的 ObjectSyntax、ObjectName 均导入自此处 |
| **RFC 1156 (MIB-I)** | 本协议操作的管理对象集合，对象实例的命名规则专门为 MIB-I 中的表做了适配 |
| **RFC 1905 (SNMPv2c)** | SNMPv2 协议操作，新增 **GetBulk** 和 **Inform** 两种 PDU |
| **RFC 3411-3415 (SNMPv3)** | 引入 USM（认证加密）和 VACM（视图访问控制），完全替代 v1 的 Community 模型 |
| **RFC 1098** | RFC 1157 的前身（重新发布，技术内容不变） |

---

## 9. 学习要点与建议

- SNMPv1 的设计哲学：**把复杂留给管理站，让代理保持简单**。代理只有 Get 和 Set 两类本质操作
- **GetNextRequest + 字典序** 是 SNMP 最精巧的设计之一，实现了变量发现和表遍历而无需预知 MIB 结构
- **Community 字符串** 就是 v1 的全部安全机制 —— 明文传输，等同于密码，是后来 v3 改进的重点
- Trap 是唯一由代理发起的消息，发送到 **UDP 162**（区别于其他 PDU 的 161）
- 建议使用 Wireshark 抓一次 `snmpwalk` 和 `snmptrap` 的包，观察五种 PDU 的实际字节流和 BER 编码

---

*大纲整理时间: 2026-07-17*