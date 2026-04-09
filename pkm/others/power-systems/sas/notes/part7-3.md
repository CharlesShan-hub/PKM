# IEC 61850 Part 7-3 解读：公共数据类 CDC

> **对应文件**：`860[1].7-3.pdf`  
> **正式标题**：IEC 61850-7-3 — Basic Communication Structure for Substation and Feeder Equipment - Common Data Classes（变电站和馈线设备的基本通信结构——公共数据类）  
> **页数**：约 100 页  
> **定位**：CDC 的完整规范，数据结构的"标准模板库"

---

## 一、这一章在说什么？

Part 7-3 是 CDC（Common Data Class）的**完整字典**。它定义了所有标准化的数据结构模板，确保不同厂家的设备用相同的格式描述相同类型的数据。

**类比**：CDC 就像 C 语言里的标准结构体（struct），或者编程语言里的类（class）。

---

## 二、CDC 的分类

Part 7-3 把 CDC 分为几大类：

```
CDC 分类
│
├── 状态类（Status）
│   ├── SPS - Single Point Status（单点状态）
│   ├── DPS - Double Point Status（双点状态）
│   ├── INS - Integer Status（整数状态）
│   └── ENS - Enumerated Status（枚举状态）
│
├── 测量类（Measurement）
│   ├── MV - Measured Value（测量值）
│   ├── CMV - Complex Measured Value（复数测量值）
│   ├── WYE - Wye Connection（三相星形）
│   ├── DEL - Delta Connection（三相三角形）
│   └── SAV - Sampled Analog Value（采样值）
│
├── 控制类（Control）
│   ├── SPC - Single Point Controllable（单点可控）
│   ├── DPC - Double Point Controllable（双点可控）
│   ├── INC - Integer Controllable（整数可控）
│   └── APC - Analogue Point Controllable（模拟可控）
│
├── 保护类（Protection）
│   ├── ACD - AC Directional（交流方向）
│   ├── ACT - Protection Activation（保护动作）
│   └── BCR - Binary Counter Reading（二进制计数器）
│
└── 设定类（Setting）
    ├── SPG - Single Point Setting（单点设定）
    ├── ING - Integer Setting（整数设定）
    └── ASG - Analog Setting（模拟设定）
```

---

## 三、状态类 CDC 详解

### SPS - Single Point Status（单点状态）

最常用的 CDC，表示 true/false 状态。

```
SPS 结构：
├── stVal      BOOLEAN      [ST]  状态值（true/false）
├── q          Quality      [ST]  品质
├── t          Timestamp    [ST]  时间戳
└── subVal     BOOLEAN      [SV]  替代值（调试时用）
```

**应用示例**：
```
XCBR1.Pos.stVal = true   ← 断路器合位
XCBR1.Pos.q = 0x00       ← 有效
XCBR1.Pos.t = 2024-01-15T10:30:00Z
```

---

### DPS - Double Point Status（双点状态）

用于需要区分"中间态"的设备，如断路器。

```
DPS 结构：
├── stVal      ENUMERATED   [ST]  状态值
│                    0 = 中间态（intermediate-state）
│                    1 = off（分位）
│                    2 = on（合位）
│                    3 = 坏状态（bad-state）
├── q          Quality      [ST]  品质
└── t          Timestamp    [ST]  时间戳
```

**应用示例**：
```
XCBR1.Pos.stVal = 2   ← 合位
XCBR1.Pos.stVal = 1   ← 分位
XCBR1.Pos.stVal = 0   ← 正在分合闸过程中（中间态）
```

---

## 四、测量类 CDC 详解

### MV - Measured Value（测量值）

单相测量值的标准结构。

```
MV 结构：
├── mag        AnalogueValue    [MX]  幅值
│   └── f      FLOAT32              浮点数值
│   └── i      INT32                整数值（可选）
├── q          Quality          [MX]  品质
├── t          Timestamp        [MX]  时间戳
├── units      Unit             [CF]  单位（配置参数）
│   └── SIUnit ENUMERATED           标准单位（A, V, W, Hz...）
│   └── multiplier ENUMERATED       倍率（m, k, M...）
└── db         INT32U           [CF]  死区（变化超过此值才报告）
```

**应用示例**：
```
MMXU1.TotW.mag.f = 125.5     ← 有功功率 125.5 MW
MMXU1.TotW.units.SIUnit = W
MMXU1.TotW.units.multiplier = M
MMXU1.TotW.db = 500          ← 死区 0.5 MW
```

---

### CMV - Complex Measured Value（复数测量值）

包含幅值和相角的测量值。

```
CMV 结构：
├── cVal       Vector           [MX]  复数值
│   ├── mag    AnalogueValue        幅值
│   └── ang    AnalogueValue        相角（度）
├── q          Quality          [MX]  品质
├── t          Timestamp        [MX]  时间戳
└── units      Unit             [CF]  单位
```

**应用示例**：
```
MMXU1.PhV.phsA.cVal.mag.f = 220.5   ← 幅值 220.5 kV
MMXU1.PhV.phsA.cVal.ang.f = 0.0     ← 相角 0°
```

---

### WYE - Wye Connection（三相星形连接）

三相测量值的标准结构。

```
WYE 结构：
├── phsA       CMV/MV          [MX]  A相
├── phsB       CMV/MV          [MX]  B相
├── phsC       CMV/MV          [MX]  C相
├── neut       CMV/MV          [MX]  中性点（可选）
└── net        CMV/MV          [MX]  零序（可选）
```

**应用示例**：
```
MMXU1.PhV.phsA.cVal.mag.f = 220.5   ← A相电压
MMXU1.PhV.phsB.cVal.mag.f = 221.0   ← B相电压
MMXU1.PhV.phsC.cVal.mag.f = 220.8   ← C相电压
```

---

## 五、控制类 CDC 详解

### SPC - Single Point Controllable（单点可控）

可控制的单点状态。

```
SPC 结构：
├── stVal      BOOLEAN      [ST]  当前状态值
├── q          Quality      [ST]  品质
├── t          Timestamp    [ST]  时间戳
├── Oper       SBOw/Oper    [CO]  控制操作对象
│   ├── ctlVal BOOLEAN          控制值（目标值）
│   ├── origin Origin             操作来源
│   ├── ctlNum INT8U              控制序号
│   ├── T      Timestamp          操作时间
│   ├── Test   BOOLEAN            测试标志
│   └── Check  Check              检查条件
└── SBOw       SBOw          [CO]  选择操作对象（SBO模式用）
```

**控制流程**：
```
1. 客户端写 SBOw（选择）
   CSWI1.Oper.ctlVal = true
   CSWI1.Oper.origin = {orCat: remote-control, orIdent: "SCADA"}
   
2. 客户端写 Oper（执行）
   CSWI1.Oper.ctlVal = true
   
3. 服务器执行后，stVal 变化
   CSWI1.stVal = true
```

---

## 六、保护类 CDC 详解

### ACT - Protection Activation（保护动作）

保护动作信号的标准结构。

```
ACT 结构：
├── general    BOOLEAN      [ST]  总动作信号
├── phsA       BOOLEAN      [ST]  A相动作
├── phsB       BOOLEAN      [ST]  B相动作
├── phsC       BOOLEAN      [ST]  C相动作
├── neut       BOOLEAN      [ST]  中性点动作（可选）
├── q          Quality      [ST]  品质
└── t          Timestamp    [ST]  时间戳
```

**应用示例**：
```
PDIS1.Op.general = true    ← 距离保护动作
PDIS1.Op.phsA = true       ← A相动作
PDIS1.Op.t = 2024-01-15T10:30:00.123Z
```

---

## 七、设定类 CDC 详解

### ASG - Analog Setting（模拟设定值）

模拟量设定值，如保护定值。

```
ASG 结构：
├── setMag     AnalogueValue    [SP]  设定值
├── q          Quality          [SP]  品质
├── t          Timestamp        [SP]  时间戳
├── units      Unit             [CF]  单位
├── minVal     AnalogueValue    [CF]  最小值（范围限制）
├── maxVal     AnalogueValue    [CF]  最大值（范围限制）
└── stepSize   AnalogueValue    [CF]  步长（调节增量）
```

**应用示例**：
```
PDIS1.Zn.setMag.f = 5.0        ← 距离保护定值 5 Ω
PDIS1.Zn.units.SIUnit = Ohm
PDIS1.Zn.minVal.f = 0.1
PDIS1.Zn.maxVal.f = 50.0
PDIS1.Zn.stepSize.f = 0.1
```

---

## 八、品质（Quality）详解

每个 CDC 都包含 `q`（品质）属性，表示数据的可信度。

```
Quality 结构（16位）：
┌────┬────┬────┬────┬────┬────┬────┬────┐
│validity│  │  │  │  │source│test│operator│
│ 2bits  │  │  │  │  │ 1bit │1bit│ 1bit   │
└────┴────┴────┴────┴────┴────┴────┴────┘

validity（有效性）：
  00 = good（有效）
  01 = invalid（无效）
  10 = reserved（保留）
  11 = questionable（可疑）

detail（详细原因）：
  - overflow（溢出）
  - outOfRange（超范围）
  - badReference（基准错误）
  - oscillatory（振荡）
  - failure（故障）
  - oldData（数据过期）
  - inconsistent（不一致）
  - inaccurate（不精确）
```

---

## 九、CDC 速查表

| CDC | 用途 | 关键属性 |
|-----|------|---------|
| SPS | 单点状态 | stVal, q, t |
| DPS | 双点状态 | stVal(0/1/2/3), q, t |
| INS | 整数状态 | stVal, q, t |
| MV | 测量值 | mag, q, t, units, db |
| CMV | 复数测量值 | cVal(mag,ang), q, t |
| WYE | 三相星形 | phsA, phsB, phsC, neut |
| DEL | 三相三角形 | phsAB, phsBC, phsCA |
| SPC | 单点可控 | stVal, Oper, SBOw |
| DPC | 双点可控 | stVal, Oper, SBOw |
| ACT | 保护动作 | general, phsA, phsB, phsC, q, t |
| ACD | 交流方向 | general, dir, phsA, phsB, phsC |
| SPG | 单点设定 | setVal, q, t |
| ING | 整数设定 | setVal, q, t, minVal, maxVal |
| ASG | 模拟设定 | setMag, q, t, units, minVal, maxVal |
| CURVE | 曲线设定 | 保护特性曲线 |

---

## 十、总结

Part 7-3 的核心：

1. **CDC 是数据模板**——标准化的数据结构
2. **分类清晰**——状态、测量、控制、保护、设定
3. **结构统一**——都包含值、品质、时间戳
4. **可扩展**——厂商可以在标准基础上扩展

**一句话记忆**：
> CDC = 数据结构模板 = 确保不同厂家用相同格式描述相同类型的数据

---

*文档系列：IEC 61850 标准解读 | Part 7-3/13 | 生成于 2026-04-08*
