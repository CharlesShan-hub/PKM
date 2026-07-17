# IEC 61850 Part 9-2 解读：采样值——以太网传输

> **对应文件**：`860[1].9-2.pdf`  
> **正式标题**：IEC 61850-9-2 — Specific Communication Service Mapping (SCSM) - Sampled Values over ISO/IEC 8802-3（特定通信服务映射——ISO/IEC 8802-3 上的采样值）  
> **页数**：约 80 页  
> **定位**：SV 采样值的以太网传输映射，现代变电站的主流方案

---

## 一、这一章在说什么？

Part 9-2 定义了如何通过**以太网**传输采样值（SV）数据。这是目前**最主流**的 SV 传输方案，广泛应用于数字化变电站。

**关键地位**：
- 数字化变电站的核心技术之一
- 取代传统模拟量接线（电缆）
- 支持保护、测量、故障录波等多种应用

---

## 二、为什么用以太网传采样值？

### 传统方式的痛点

传统变电站使用模拟量传输：
```
互感器（CT/VT）
    ↓ 铜电缆（二次回路）
保护/测控装置
    ↓ 铜电缆
监控后台
```

**问题**：
- 电缆多、接线复杂
- 电缆损耗、干扰
- 难以实现信息共享
- 扩建改造困难

### 数字化方案

```
电子式互感器（ECT/EVT）
    ↓ 光纤
合并单元（MU）
    ↓ 以太网（SV 报文）
保护/测控/计量/录波装置
    ↓ 以太网
监控后台
```

**优势**：
- 一根光纤代替多根电缆
- 数字传输无损耗
- 多装置共享采样值
- 灵活组网、易于扩展

---

## 三、SV 以太网帧结构

### 以太网帧格式

```
SV 以太网帧：
┌─────────────────────────────────────────────────────────────┐
│  目的 MAC 地址（6字节）                                       │
│  ├── 01-0C-CD-04-00-00 ~ 01-0C-CD-04-01-FF（SV 组播地址）   │
│  └── 由 SCL 文件中的 Communication/SMV/Address/P 定义        │
├─────────────────────────────────────────────────────────────┤
│  源 MAC 地址（6字节）                                         │
│  └── 合并单元的 MAC 地址                                      │
├─────────────────────────────────────────────────────────────┤
│  VLAN TPID + TCI（4字节，可选）                               │
│  ├── TPID：0x8100                                            │
│  ├── VLAN ID：0~4095（由 SCL 定义）                          │
│  └── Priority：0~7（SV 通常用 4）                             │
├─────────────────────────────────────────────────────────────┤
│  以太网类型（2字节）                                          │
│  └── 0x88BA（IEC 61850-9-2 专用类型）                         │
├─────────────────────────────────────────────────────────────┤
│  APDU（应用协议数据单元）                                     │
│  └── ASN.1 BER 编码的 SV 数据                                 │
├─────────────────────────────────────────────────────────────┤
│  FCS（帧校验序列，4字节）                                     │
└─────────────────────────────────────────────────────────────┘
```

---

## 四、SV APDU 结构

### ASN.1 定义

```asn1
SV APDU ::= SEQUENCE {
    savPdu          [0] IMPLICIT SavPdu
}

SavPdu ::= SEQUENCE {
    noASDU          [0] IMPLICIT INTEGER,           -- ASDU 数量
    seqASDU         [2] IMPLICIT SEQUENCE OF ASDU   -- ASDU 序列
}

ASDU ::= SEQUENCE {
    svID            [0] IMPLICIT VisibleString,     -- SV 标识
    smpCnt          [1] IMPLICIT INTEGER,           -- 采样计数器
    confRev         [2] IMPLICIT INTEGER,           -- 配置版本
    refrTm          [3] IMPLICIT UtcTime OPTIONAL,  -- 参考时间
    smpSynch        [4] IMPLICIT INTEGER,           -- 同步标志
    seqData         [5] IMPLICIT OCTET STRING       -- 采样数据
}
```

### ASDU 详解

```
ASDU（Application Service Data Unit）：
┌─────────────────────────────────────────────────────────────┐
│  svID（SV 标识）                                             │
│  ├── 字符串，标识这组采样值的来源                            │
│  ├── 例如："MU_Line1"、"MU_T1"                              │
│  └── 由 SCL 文件中的 DataSet/name 定义                       │
├─────────────────────────────────────────────────────────────┤
│  smpCnt（采样计数器）                                        │
│  ├── 范围：0 ~ (SmpRate - 1)                                 │
│  ├── 每个采样周期 +1，循环计数                               │
│  └── 用于检测丢帧和同步                                      │
├─────────────────────────────────────────────────────────────┤
│  confRev（配置版本）                                         │
│  └── 数据集配置版本号，配置变更时 +1                         │
├─────────────────────────────────────────────────────────────┤
│  refrTm（参考时间，可选）                                    │
│  └── UTC 时间戳，用于绝对时间同步                            │
├─────────────────────────────────────────────────────────────┤
│  smpSynch（同步标志）                                        │
│  ├── 0 = 未同步                                              │
│  ├── 1 = 本地同步（与其他 MU 同步）                          │
│  └── 2 = 全局同步（与绝对时间同步）                          │
├─────────────────────────────────────────────────────────────┤
│  seqData（采样数据序列）                                     │
│  └── 二进制编码的采样值数组                                  │
└─────────────────────────────────────────────────────────────┘
```

---

## 五、采样数据编码

### 数据格式

```
每个采样值：
├── 数据类型：32位有符号整数（INT32）
├── 字节序：大端（Big Endian）
├── 比例：额定值对应 0x01D4（4672）
└── 额定值定义：
    ├── 电流：1A 或 5A（额定二次电流）
    └── 电压：100V 或 110V（额定二次电压）

编码示例：
额定电流 1A → 编码值 4672（0x00001240）
实际值 = 编码值 × 额定值 / 4672

例如：
编码值 = 9344（0x00002480）
实际电流 = 9344 × 1A / 4672 = 2A
```

### 典型 ASDU 数据内容

```
一个典型的 ASDU 包含 8 个通道：
├── 电流 Ia（4字节）
├── 电流 Ib（4字节）
├── 电流 Ic（4字节）
├── 电流 In（4字节，中性点）
├── 电压 Ua（4字节）
├── 电压 Ub（4字节）
├── 电压 Uc（4字节）
└── 电压 Un（4字节，中性点）

总数据长度：8 × 4 = 32 字节
```

---

## 六、采样率与网络负载

### 标准采样率

| 采样率 | 周期 | 应用场景 |
|--------|------|---------|
| 80 Hz | 12.5 ms | 低速保护、监测 |
| 256 Hz | 3.9 ms | 中速保护 |
| 4000 Hz | 250 μs | 高速保护、故障录波 |
| 4800 Hz | 208 μs | 高精度测量 |

### 网络负载计算

```
以 4000 Hz、8 通道为例：

每帧大小：
├── 以太网头：14 字节（MAC 头）
├── VLAN：4 字节
├── 以太网类型：2 字节
├── APDU：约 100 字节（svID + smpCnt + 8×4 字节数据）
├── FCS：4 字节
└── 帧间隙：12 字节
总计：约 136 字节/帧

每秒帧数：4000

带宽占用：
136 字节 × 8 bit × 4000 /s = 4.35 Mbps

考虑 100 Mbps 以太网：
负载率 = 4.35 / 100 = 4.35%
```

**结论**：即使是 4000 Hz 高速采样，100 Mbps 以太网也完全可以承载。

---

## 七、时间同步

### 为什么需要同步？

```
场景：差动保护需要比较线路两侧电流

线路侧 A                    线路侧 B
   │                            │
   MU-A                         MU-B
   │                            │
   └──→ 保护装置 ←──┘
        
如果 MU-A 和 MU-B 的采样时间不同步：
- 外部故障时，两侧电流波形相位差 ≠ 180°
- 保护可能误判为内部故障，导致误动！

同步要求：
- 差动保护：采样同步误差 < 10 μs
- 一般保护：采样同步误差 < 100 μs
```

### 同步方案：IEEE 1588 PTP

```
PTP（Precision Time Protocol）同步架构：

┌─────────────┐         ┌─────────────┐
│  PTP 主时钟  │◄───────►│  PTP 主时钟  │
│  （GPS/北斗）│  热备份  │  （GPS/北斗）│
└──────┬──────┘         └─────────────┘
       │
       │ PTP 协议（以太网组播）
       ▼
┌─────────────┐
│   交换机     │◄── PTP 透明时钟
│  （带 BMCA） │    （补偿驻留时间）
└──────┬──────┘
       │
   ┌───┴───┐
   ▼       ▼
┌─────┐ ┌─────┐
│ MU1 │ │ MU2 │ ...
└─────┘ └─────┘

同步精度：亚微秒级（< 1 μs）
```

### SV 中的同步标志

```
smpSynch 字段：
├── 0：未同步（Local）
│   └── MU 使用本地时钟，未与外部同步
│
├── 1：本地同步（Local Clocked）
│   └── 与其他 MU 同步，但可能未与绝对时间同步
│
└── 2：全局同步（Global Clocked）
    └── 与绝对时间同步（如 GPS 时间）

保护装置使用规则：
- smpSynch = 0：闭锁差动保护（数据不可靠）
- smpSynch = 1/2：允许差动保护
```

---

## 八、SCL 配置

### SV 通信配置示例

```xml
<Communication>
    <SubNetwork name="ProcessBus" type="8-MMS">
        <BitRate unit="b/s" multiplier="M">100</BitRate>
        
        <!-- 合并单元 -->
        <ConnectedAP iedName="MU_Line1" apName="S1">
            <SMV ldInst="MU" cbName="SVCB">
                <Address>
                    <!-- 组播 MAC 地址 -->
                    <P type="MAC-Address">01-0C-CD-04-00-10</P>
                    <!-- VLAN ID -->
                    <P type="VLAN-ID">100</P>
                    <!-- 优先级 -->
                    <P type="VLAN-PRIORITY">4</P>
                    <!-- APPID -->
                    <P type="APPID">0x4000</P>
                </Address>
            </SMV>
        </ConnectedAP>
        
        <!-- 保护装置（订阅 SV）-->
        <ConnectedAP iedName="PROT_Line1" apName="S1">
            <!-- 订阅 MU_Line1 的 SV -->
        </ConnectedAP>
        
    </SubNetwork>
</Communication>
```

### 数据集定义

```xml
<IED name="MU_Line1">
    <AccessPoint name="S1">
        <Server>
            <LDevice inst="MU">
                <LN0 lnClass="LLN0" inst="" lnType="LLN0_1">
                    <!-- SV 控制块 -->
                    <SampledValueControl name="SVCB" 
                                         datSet="dsSV" 
                                         confRev="1"
                                         smvID="MU_Line1">
                        <SmvOpts refreshTime="false" 
                                 sampleRate="false" 
                                 dataSet="false" 
                                 security="false"/>
                    </SampledValueControl>
                    
                    <!-- 数据集 -->
                    <DataSet name="dsSV">
                        <FCDA ldInst="MU" lnClass="TCTR" lnInst="1" 
                              doName="Amp" daName="instMag" fc="MX"/>
                        <FCDA ldInst="MU" lnClass="TCTR" lnInst="2" 
                              doName="Amp" daName="instMag" fc="MX"/>
                        <FCDA ldInst="MU" lnClass="TCTR" lnInst="3" 
                              doName="Amp" daName="instMag" fc="MX"/>
                        <FCDA ldInst="MU" lnClass="TVTR" lnInst="1" 
                              doName="Vol" daName="instMag" fc="MX"/>
                        <FCDA ldInst="MU" lnClass="TVTR" lnInst="2" 
                              doName="Vol" daName="instMag" fc="MX"/>
                        <FCDA ldInst="MU" lnClass="TVTR" lnInst="3" 
                              doName="Vol" daName="instMag" fc="MX"/>
                    </DataSet>
                </LN0>
                
                <!-- 电流互感器逻辑节点 -->
                <LN lnClass="TCTR" inst="1" lnType="TCTR_1"/>
                <LN lnClass="TCTR" inst="2" lnType="TCTR_1"/>
                <LN lnClass="TCTR" inst="3" lnType="TCTR_1"/>
                
                <!-- 电压互感器逻辑节点 -->
                <LN lnClass="TVTR" inst="1" lnType="TVTR_1"/>
                <LN lnClass="TVTR" inst="2" lnType="TVTR_1"/>
                <LN lnClass="TVTR" inst="3" lnType="TVTR_1"/>
            </LDevice>
        </Server>
    </AccessPoint>
</IED>
```

---

## 九、与 GOOSE 的对比

| 特性 | SV（采样值） | GOOSE |
|------|-------------|-------|
| **传输内容** | 模拟量采样（电流/电压）| 开关量状态（跳闸/位置）|
| **发送频率** | 固定周期（80/256/4000 Hz）| 事件触发 + 心跳 |
| **延迟要求** | < 0.5 ms | < 4 ms |
| **MAC 地址** | 01-0C-CD-04-xx-xx | 01-0C-CD-01-xx-xx |
| **以太网类型** | 0x88BA | 0x88B8 |
| **主要应用** | 保护计算、测量、录波 | 保护跳闸、联闭锁 |

---

## 十、总结

Part 9-2 的核心：

1. **以太网传输 SV**——数字化变电站的核心技术
2. **ASN.1 BER 编码**——标准化的数据格式
3. **高采样率支持**——最高 4800 Hz
4. **精确时间同步**——IEEE 1588 PTP
5. **网络负载可控**——100 Mbps 轻松承载

**一句话记忆**：
> Part 9-2 = 以太网采样值 = 数字化变电站的"神经网络"

---

## 下一步阅读建议

理解了 SV 传输，可以：
- 研究合并单元（MU）的工作原理
- 学习 PTP 时间同步的实现
- 查看数字化变电站的工程案例

---

*文档系列：IEC 61850 标准解读 | Part 9-2/13 | 生成于 2026-04-08*
