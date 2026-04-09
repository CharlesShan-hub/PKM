# IEC 61850 Part 7-4 解读：逻辑节点类和数据类

> **对应文件**：`860[1].7-4.pdf`  
> **正式标题**：IEC 61850-7-4 — Basic Communication Structure for Substation and Feeder Equipment - Compatible Logical Node Classes and Data Classes（变电站和馈线设备的基本通信结构——兼容逻辑节点类和数据类）  
> **页数**：约 300 页（最厚的一册）  
> **定位**：所有标准化逻辑节点的完整定义，LN 的"百科全书"

---

## 一、这一章在说什么？

Part 7-4 是 IEC 61850 的**逻辑节点字典**。它定义了所有标准化的逻辑节点类（LN Class），每个 LN 包含哪些数据对象（DO），每个 DO 用什么 CDC。

**类比**：如果 Part 7-3 是"数据类型手册"，Part 7-4 就是"功能模块手册"。

---

## 二、逻辑节点的命名规则

### 类名结构

```
LN 类名 = 第1字母（功能域）+ 第2-4字母（具体功能）

示例：
┌─────────┬──────────────────────────────────────┐
│ 第1字母 │ 功能域（Function Domain）             │
├─────────┼──────────────────────────────────────┤
│    L    │ 系统逻辑节点（Logical Node）          │
│    P    │ 保护功能（Protection）                │
│    R    │ 保护相关（Protection Related）        │
│    C    │ 监控（Supervisory Control）           │
│    G    │ 通用功能（General）                   │
│    M    │ 计量/测量（Metering/Measurement）     │
│    S    │ 传感器/监视（Sensor/Supervision）     │
│    T    │ 互感器（Instrument Transformer）      │
│    X    │ 开关设备（Switchgear）                │
│    Y    │ 电力变压器（Power Transformer）       │
│    Z    │ 其他设备（Further Equipment）         │
└─────────┴──────────────────────────────────────┘
```

---

## 三、系统逻辑节点（L 类）

### LLN0 - Logical Node Zero

每个逻辑设备（LD）必须包含的公用节点。

```
LLN0 包含的数据对象：
├── Loc          SPS    [ST]  就地/远方状态
├── OpTmh        INS    [ST]  运行时间（小时）
├── Health       ENS    [ST]  健康状态
├── Beh          ENS    [ST]  行为状态
├── Mod          ENC    [ST]  模式（运行/测试/阻塞）
├── InRef        ORG    [SP]  输入引用（数据集成员）
└── 数据集和控制块（在 SCL 中定义）
```

### LPHD - Physical Device Information

物理设备信息。

```
LPHD 包含的数据对象：
├── PhyNam       DPL    [DC]  物理设备名称
├── PhyHealth    ENS    [ST]  物理健康状态
├── OutOv        SPS    [ST]  输出溢出
├── Proxy        SPS    [ST]  代理状态
├── InOv         SPS    [ST]  输入溢出
└── NumPwrUp     INS    [ST]  上电次数
```

---

## 四、测量逻辑节点（M 类）

### MMXU - Measurement

三相电气量测量，最常用的测量 LN。

```
MMXU 包含的数据对象：
├── TotW         MV     [MX]  总有功功率
├── TotVAr       MV     [MX]  总无功功率
├── TotVA        MV     [MX]  总视在功率
├── TotPF        MV     [MX]  总功率因数
├── Hz           MV     [MX]  频率
├── PPV          DEL    [MX]  相间电压（线电压）
├── PhV          WYE    [MX]  相电压
├── A            WYE    [MX]  电流
├── W            WYE    [MX]  分相有功功率
├── VAr          WYE    [MX]  分相无功功率
├── VA           WYE    [MX]  分相视在功率
└── PF           WYE    [MX]  分相功率因数
```

**应用示例**：
```
MMXU1.PhV.phsA.cVal.mag.f = 220.5   ← A相电压
MMXU1.A.phsA.cVal.mag.f = 500.0     ← A相电流
MMXU1.TotW.mag.f = 330.75           ← 总有功功率
MMXU1.Hz.mag.f = 50.02              ← 频率
```

### MMTR - Metering

电能计量。

```
MMTR 包含的数据对象：
├── TotWh        BCR    [MX]  正向有功电能
├── TotVArh      BCR    [MX]  正向无功电能
├── SupWh        BCR    [MX]  供电有功电能
├── SupVArh      BCR    [MX]  供电无功电能
├── DmdWh        BCR    [MX]  需量有功电能
└── DmdVArh      BCR    [MX]  需量无功电能
```

---

## 五、开关设备逻辑节点（X 类）

### XCBR - Circuit Breaker

断路器。

```
XCBR 包含的数据对象：
├── Loc          SPS    [ST]  就地/远方
├── OpCnt        INS    [ST]  操作计数
├── Pos          DPC    [ST]  位置（合/分/中间）
├── BlkOpn       SPC    [ST]  闭锁分闸
├── BlkCls       SPC    [ST]  闭锁合闸
├── ChaMotEna    SPC    [ST]  储能电机使能
├── SumSwARs     BCR    [ST]  累计开关电流
├── CBOpCap      INS    [ST]  断路器操作能力
├── PwrUp        SPS    [ST]  上电状态
└── 控制对象（SPC/DPC 的 Oper/SBOw）
```

**应用示例**：
```
XCBR1.Pos.stVal = 2          ← 合位
XCBR1.OpCnt.stVal = 1523     ← 操作1523次
XCBR1.BlkOpn.stVal = false   ← 未闭锁分闸
```

### XSWI - Switch

隔离开关/接地开关。

```
XSWI 包含的数据对象：
├── Loc          SPS    [ST]  就地/远方
├── OpCnt        INS    [ST]  操作计数
├── Pos          DPC    [ST]  位置
├── BlkOpn       SPC    [ST]  闭锁分闸
├── BlkCls       SPC    [ST]  闭锁合闸
└── SwTyp        INS    [DC]  开关类型
```

---

## 六、保护逻辑节点（P 类）

### PTOC - Time Overcurrent Protection

过流保护（定时限/反时限）。

```
PTOC 包含的数据对象：
├── Str          ACD    [ST]  启动（故障检测）
├── Op           ACT    [ST]  动作（跳闸输出）
├── Mod          ENC    [ST]  模式
├── Health       ENS    [ST]  健康状态
├── Beh          ENS    [ST]  行为状态
├── StrVal       ASG    [SP]  启动值（定值）
├── OpDlTmms     ING    [SP]  动作延时（ms）
├── RsDlTmms     ING    [SP]  返回延时（ms）
├── MinOpTmms    ING    [SP]  最小动作时间
├── MaxOpTmms    ING    [SP]  最大动作时间
├── OpTyp        ENG    [SP]  动作类型（定时限/反时限）
└── TmAChr       CURVE  [SP]  反时限特性曲线
```

**应用示例**：
```
PTOC1.StrVal.setMag.f = 5.0       ← 启动电流 5A
PTOC1.OpDlTmms.setVal = 500       ← 动作延时 500ms
PTOC1.Str.general = true          ← 故障检测
PTOC1.Op.general = true           ← 保护动作跳闸
```

### PDIS - Distance Protection

距离保护。

```
PDIS 包含的数据对象：
├── Str          ACD    [ST]  启动
├── Op           ACT    [ST]  动作
├── Mod          ENC    [ST]  模式
├── Health       ENS    [ST]  健康状态
├── Zn           ASG    [SP]  阻抗定值
├── OpDlTmms     ING    [SP]  动作延时
├── RsDlTmms     ING    [SP]  返回延时
├── TypRs        SPG    [SP]  返回类型
├── LinAng       ASG    [SP]  线路阻抗角
├── NumPol       ING    [SP]  极对数
└── ChNum        ING    [SP]  通道号
```

### PDIF - Differential Protection

差动保护。

```
PDIF 包含的数据对象：
├── Str          ACD    [ST]  启动
├── Op           ACT    [ST]  动作
├── Mod          ENC    [ST]  模式
├── Health       ENS    [ST]  健康状态
├── StrVal       ASG    [SP]  启动值
├── OpDlTmms     ING    [SP]  动作延时
├── RsDlTmms     ING    [SP]  返回延时
├── LinCap       SPS    [ST]  线性范围能力
├── DifAClc      MV     [MX]  差动电流计算值
├── RstA         MV     [MX]  制动电流
└── AngRef       ASG    [SP]  参考角度
```

---

## 七、控制逻辑节点（C 类）

### CSWI - Switch Controller

开关控制器，接收控制命令并转发给 XCBR/XSWI。

```
CSWI 包含的数据对象：
├── Loc          SPS    [ST]  就地/远方
├── OpCnt        INS    [ST]  操作计数
├── Pos          DPC    [ST]  位置（反馈）
├── PosA         DPC    [CO]  位置A（控制对象）
├── PosB         DPC    [CO]  位置B（控制对象）
├── PosC         DPC    [CO]  位置C（控制对象）
├── OpOpn        ACT    [ST]  分闸操作
├── OpCls        ACT    [ST]  合闸操作
├── BlkOpn       SPC    [ST]  闭锁分闸
├── BlkCls       SPC    [ST]  闭锁合闸
└── SwTyp        INS    [DC]  开关类型
```

**控制流程**：
```
SCADA 下发控制命令
    ↓
CSWI1.PosA.Oper.ctlVal = true（合闸）
    ↓
CSWI 处理控制逻辑（联闭锁检查）
    ↓
CSWI 输出到 XCBR
    ↓
XCBR 执行分合闸操作
```

### CILO - Interlocking

联闭锁逻辑。

```
CILO 包含的数据对象：
├── EnaOpn       SPS    [ST]  允许分闸
├── EnaCls       SPS    [ST]  允许合闸
├── Mod          ENC    [ST]  模式
├── Health       ENS    [ST]  健康状态
├── Beh          ENS    [ST]  行为状态
└── 各种联闭锁条件输入...
```

---

## 八、互感器逻辑节点（T 类）

### TCTR - Current Transformer

电流互感器。

```
TCTR 包含的数据对象：
├── Mod          ENC    [ST]  模式
├── Health       ENS    [ST]  健康状态
├── Beh          ENS    [ST]  行为状态
├── Amp          MV     [MX]  电流幅值
├── Hz           MV     [MX]  频率
├── ClcRf        SPC    [SP]  计算参考值
├── CorRot       SPC    [SP]  纠正旋转
└── AngRef       ASG    [SP]  角度参考
```

### TVTR - Voltage Transformer

电压互感器。

```
TVTR 包含的数据对象：
├── Mod          ENC    [ST]  模式
├── Health       ENS    [ST]  健康状态
├── Beh          ENS    [ST]  行为状态
├── Vol          MV     [MX]  电压幅值
├── Hz           MV     [MX]  频率
├── ClcRf        SPC    [SP]  计算参考值
├── CorRot       SPC    [SP]  纠正旋转
└── AngRef       ASG    [SP]  角度参考
```

---

## 九、逻辑节点速查表

| 类别 | LN 类名 | 功能 | 关键 DO |
|------|---------|------|---------|
| 系统 | LLN0 | 逻辑设备公用 | Loc, Health, Beh, Mod |
| 系统 | LPHD | 物理设备信息 | PhyNam, PhyHealth |
| 测量 | MMXU | 三相电气量测量 | PhV, A, PPV, TotW, Hz |
| 测量 | MMTR | 电能计量 | TotWh, TotVArh |
| 开关 | XCBR | 断路器 | Pos, OpCnt, BlkOpn, BlkCls |
| 开关 | XSWI | 隔离开关 | Pos, OpCnt |
| 保护 | PTOC | 过流保护 | Str, Op, StrVal, OpDlTmms |
| 保护 | PDIS | 距离保护 | Str, Op, Zn, OpDlTmms |
| 保护 | PDIF | 差动保护 | Str, Op, StrVal, DifAClc |
| 保护 | PTRC | 保护跳闸输出 | Op, Str |
| 控制 | CSWI | 开关控制器 | Pos, PosA, BlkOpn, BlkCls |
| 控制 | CILO | 联闭锁 | EnaOpn, EnaCls |
| 互感器 | TCTR | 电流互感器 | Amp, Hz |
| 互感器 | TVTR | 电压互感器 | Vol, Hz |

---

## 十、总结

Part 7-4 的核心：

1. **LN 是功能的标准化封装**——每个 LN 代表一个明确的功能实体
2. **命名有规律**——首字母表示功能域
3. **结构统一**——都包含状态、测量、控制、配置等 DO
4. **可组合**——一个 IED 可以包含多个 LN，实现复杂功能

**一句话记忆**：
> Part 7-4 = 逻辑节点字典 = 变电站功能的标准化封装

---

## 下一步阅读建议

理解了逻辑节点，接下来：
- **Part 8-1**：看这些 LN 如何通过 MMS 通信
- **实践**：打开项目里的 ICD 文件，对照 Part 7-4 理解每个 LN

---

*文档系列：IEC 61850 标准解读 | Part 7-4/13 | 生成于 2026-04-08*
