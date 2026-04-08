# IEC 61850 Part 6 解读：SCL 配置语言——系统的 DNA

> **对应文件**：`860[1].6.pdf`  
> **正式标题**：IEC 61850-6 — Configuration Description Language for Communication in Electrical Substations Related to IEDs（变电站 IED 通信配置描述语言）  
> **页数**：约 150 页（最厚的部分之一）  
> **定位**：SCL（Substation Configuration Language）的完整语法规范

---

## 一、这一章在说什么？

SCL 是 IEC 61850 的**配置语言**，基于 XML 格式。它把变电站的所有信息——一次系统拓扑、IED 能力、通信参数、数据流——都描述在一个（或一组）文件里。

**一句话理解**：SCL 文件就是变电站自动化系统的"DNA"，包含了构建和配置整个系统所需的全部遗传信息。

---

## 二、SCL 的五种文件类型

Part 6 定义了五种 SCL 文件，每种有不同的用途和生命周期：

```
┌─────────────────────────────────────────────────────────────────┐
│                        SCL 文件类型                              │
├─────────┬───────────────────────────────────────────────────────┤
│  SSD    │ System Specification Description（系统规格描述）       │
│         │ • 描述变电站一次系统（主接线、电压等级、间隔）          │
│         │ • 由系统集成商创建                                     │
│         │ • 不包含 IED 具体信息                                  │
├─────────┼───────────────────────────────────────────────────────┤
│  ICD    │ IED Capability Description（IED 能力描述）             │
│         │ • 描述单个 IED 的能力（有什么 LN、支持什么服务）        │
│         │ • 由设备厂商提供                                       │
│         │ • 是设备的"产品说明书"                                 │
├─────────┼───────────────────────────────────────────────────────┤
│  SCD    │ Substation Configuration Description（系统配置描述）   │
│         │ • 完整的系统配置（SSD + 所有 ICD + 通信配置）           │
│         │ • 由系统集成商创建                                     │
│         │ • 是项目的"总设计图"                                   │
├─────────┼───────────────────────────────────────────────────────┤
│  CID    │ Configured IED Description（已配置 IED 描述）          │
│         │ • 单个 IED 的实例化配置                                │
│         │ • 从 SCD 导出，下载到 IED                              │
│         │ • 是设备的"身份证"                                     │
├─────────┼───────────────────────────────────────────────────────┤
│  IID    │ Instantiated IED Description（实例化 IED 描述）        │
│         │ • 工程实例化的 IED 配置                                │
│         │ • 用于 IED 之间的配置交换                              │
│         │ • 较少使用                                             │
└─────────┴───────────────────────────────────────────────────────┘
```

---

## 三、SCL 文件的结构

所有 SCL 文件都遵循相同的 XML Schema，根元素是 `<SCL>`：

```xml
<?xml version="1.0" encoding="UTF-8"?>
<SCL xmlns="http://www.iec.ch/61850/2003/SCL" version="2007" revision="B">
    
    <!-- 1. 头部信息 -->
    <Header id="Project_Example" version="1.0" revision="1.0"/>
    
    <!-- 2. 变电站一次系统描述（SSD/SCD 有，ICD 没有）-->
    <Substation name="Sub1">
        ...
    </Substation>
    
    <!-- 3. IED 描述（ICD/SCD/CID 有）-->
    <IED name="IED1" type="ProtectionRelay" manufacturer="ABC">
        ...
    </IED>
    
    <!-- 4. 通信系统配置（SCD/CID 有）-->
    <Communication>
        ...
    </Communication>
    
    <!-- 5. 数据类型模板（ICD 有，SCD/CID 引用）-->
    <DataTypeTemplates>
        ...
    </DataTypeTemplates>
    
</SCL>
```

---

## 四、Substation 部分：一次系统拓扑

`<Substation>` 描述变电站的物理结构：

```xml
<Substation name="500kV_Substation" desc="某变电站">
    
    <!-- 电压等级 -->
    <VoltageLevel name="VL500" nomFreq="50" numPhases="3">
        <Voltage unit="V" multiplier="k">500</Voltage>
        
        <!-- 间隔（Bay）：变电站的功能单元 -->
        <Bay name="Bay_Line1" desc="出线间隔1">
            
            <!-- 导体（ConductingEquipment）：断路器、隔离开关等 -->
            <ConductingEquipment name="CB1" type="CBR">
                <Terminal name="T1" connectivityNode="VL500/Bay_Line1/Node1"/>
                <Terminal name="T2" connectivityNode="VL500/Bay_Line1/Node2"/>
            </ConductingEquipment>
            
            <ConductingEquipment name="DS1" type="DIS">
                <Terminal name="T1" connectivityNode="VL500/Bay_Line1/Node2"/>
                <Terminal name="T2" connectivityNode="VL500/Bay_Line1/Node3"/>
            </ConductingEquipment>
            
            <!-- 连接节点 -->
            <ConnectivityNode name="Node1" pathName="VL500/Bay_Line1/Node1"/>
            <ConnectivityNode name="Node2" pathName="VL500/Bay_Line1/Node2"/>
            <ConnectivityNode name="Node3" pathName="VL500/Bay_Line1/Node3"/>
            
        </Bay>
        
    </VoltageLevel>
    
</Substation>
```

**关键概念**：
- **VoltageLevel**：电压等级（500kV、220kV、110kV...）
- **Bay**：间隔，变电站的功能单元（一条出线、一台变压器对应一个间隔）
- **ConductingEquipment**：一次设备（CBR=断路器、DIS=隔离开关、CTR=电流互感器...）
- **ConnectivityNode**：连接点，描述设备之间的电气连接关系

---

## 五、IED 部分：智能设备描述

`<IED>` 是 SCL 的核心，描述智能设备的所有信息：

```xml
<IED name="PROT_Line1" type="LineProtection" manufacturer="SIEMENS" 
     configVersion="1.0" originalSclVersion="2007" originalSclRevision="B">
    
    <!-- 服务配置：这个 IED 支持哪些服务 -->
    <Services>
        <DynAssociation max="10"/>
        <DynDataSet max="20"/>
        <ConfDataSet max="20" maxAttributes="100"/>
        <ConfReportControl max="10"/>
        <ConfLogControl max="5"/>
        <FileHandling/>
        <TimeSyncProt sntp="true" ptp="true"/>
    </Services>
    
    <!-- 访问点：IED 的通信接口 -->
    <AccessPoint name="S1">
        
        <!-- 服务器：提供数据和服务 -->
        <Server>
            
            <!-- 逻辑设备（LD）：功能分区 -->
            <LDevice inst="LD0" desc="公用 LD">
                
                <!-- 逻辑节点（LN）：具体功能 -->
                <LN0 lnClass="LLN0" inst="" lnType="LLN0_1">
                    <!-- 数据集：一组数据的集合 -->
                    <DataSet name="dsMeasurements">
                        <FCDA ldInst="LD0" lnClass="MMXU" lnInst="1" 
                              doName="PhV" daName="phsA" fc="MX"/>
                        <FCDA ldInst="LD0" lnClass="MMXU" lnInst="1" 
                              doName="PhV" daName="phsB" fc="MX"/>
                        <FCDA ldInst="LD0" lnClass="MMXU" lnInst="1" 
                              doName="PhV" daName="phsC" fc="MX"/>
                    </DataSet>
                    
                    <!-- 报告控制块：定义如何主动上报数据 -->
                    <ReportControl name="URCB_Meas" datSet="dsMeasurements" 
                                   confRev="1" buffered="false" 
                                   rptID="Measurements">
                        <TrgOps dchg="true" qchg="true"/>
                        <OptFields seqNum="true" timeStamp="true"/>
                        <RptEnabled max="5"/>
                    </ReportControl>
                </LN0>
                
                <!-- 测量逻辑节点 -->
                <LN lnClass="MMXU" inst="1" lnType="MMXU_1" prefix="">
                    <!-- 数据对象实例 -->
                </LN>
                
                <!-- 断路器控制逻辑节点 -->
                <LN lnClass="XCBR" inst="1" lnType="XCBR_1"/>
                
            </LDevice>
            
            <LDevice inst="PROT" desc="保护 LD">
                <LN0 lnClass="LLN0" inst="" lnType="LLN0_PROT"/>
                <LN lnClass="PDIS" inst="1" lnType="PDIS_1"/>
                <LN lnClass="PTOC" inst="1" lnType="PTOC_1"/>
            </LDevice>
            
        </Server>
        
    </AccessPoint>
    
</IED>
```

**关键概念**：
- **AccessPoint**：访问点，IED 的通信接口（一个 IED 可以有多个）
- **LDevice**：逻辑设备，功能分区（LD0=公用、PROT=保护、CTRL=控制...）
- **LN/LN0**：逻辑节点，具体功能（LLN0=每个 LD 的公用节点、MMXU=测量、XCBR=断路器...）
- **DataSet**：数据集，一组功能相关数据的集合
- **ReportControl**：报告控制块，定义数据如何主动上报

---

## 六、Communication 部分：通信配置

`<Communication>` 描述整个系统的通信参数：

```xml
<Communication>
    
    <!-- 子网：按功能或区域划分 -->
    <SubNetwork name="StationBus" type="8-MMS">
        <BitRate unit="b/s" multiplier="M">100</BitRate>
        
        <!-- 连接到子网的 IED -->
        <ConnectedAP iedName="PROT_Line1" apName="S1">
            <!-- IP 地址 -->
            <Address>
                <P type="IP">192.168.1.10</P>
                <P type="IP-SUBNET">255.255.255.0</P>
                <P type="IP-GATEWAY">192.168.1.1</P>
            </Address>
            
            <!-- GOOSE 配置 -->
            <GSE ldInst="LD0" cbName="GOOSE_CB">
                <Address>
                    <P type="MAC-Address">01-0C-CD-01-00-10</P>
                    <P type="VLAN-ID">100</P>
                    <P type="VLAN-PRIORITY">4</P>
                    <P type="APPID">0x1000</P>
                </Address>
                <MinTime unit="s" multiplier="m">4</MinTime>
                <MaxTime unit="s" multiplier="m">1000</MaxTime>
            </GSE>
            
            <!-- SV 采样值配置 -->
            <SMV ldInst="LD0" cbName="SV_CB">
                <Address>
                    <P type="MAC-Address">01-0C-CD-04-00-10</P>
                    <P type="VLAN-ID">200</P>
                    <P type="VLAN-PRIORITY">4</P>
                    <P type="APPID">0x4000</P>
                </Address>
            </SMV>
        </ConnectedAP>
        
        <ConnectedAP iedName="MU_Line1" apName="S1">
            <Address>
                <P type="IP">192.168.1.20</P>
                <P type="IP-SUBNET">255.255.255.0</P>
            </Address>
        </ConnectedAP>
        
    </SubNetwork>
    
</Communication>
```

**关键概念**：
- **SubNetwork**：子网，可以按功能划分（站控网、过程网）
- **ConnectedAP**：连接访问点，IED 到子网的连接
- **GSE**：Generic Substation Event，GOOSE 的通信配置
- **SMV**：Sampled Value，SV 的通信配置
- **MAC-Address**：GOOSE/SV 使用组播 MAC 地址（01-0C-CD-01-xx-xx 是 GOOSE，01-0C-CD-04-xx-xx 是 SV）

---

## 七、DataTypeTemplates 部分：数据类型模板

`<DataTypeTemplates>` 定义所有 LN、DO、DA 的类型模板：

```xml
<DataTypeTemplates>
    
    <!-- 逻辑节点类型（LNodeType）-->
    <LNodeType lnClass="MMXU" id="MMXU_1">
        <!-- 数据对象（DO）-->
        <DO name="PhV" type="WYE"/>
        <DO name="A" type="WYE"/>
        <DO name="TotW" type="MV"/>
        <DO name="TotVAr" type="MV"/>
        <DO name="Hz" type="MV"/>
    </LNodeType>
    
    <!-- 数据对象类型（DOType）-->
    <DOType cdc="WYE" id="WYE">
        <!-- 数据属性（DA）-->
        <DA name="phsA" type="CMV"/>
        <DA name="phsB" type="CMV"/>
        <DA name="phsC" type="CMV"/>
        <DA name="neut" type="CMV"/>
    </DOType>
    
    <!-- 公共数据类（DAType）-->
    <DAType id="CMV">
        <BDA name="cVal" type="Vector"/>
        <BDA name="q" type="Quality"/>
        <BDA name="t" type="Timestamp"/>
    </DAType>
    
    <!-- 基本数据属性类型（EnumType/BDA）-->
    <EnumType id="BehaviourMode">
        <EnumVal ord="1">on</EnumVal>
        <EnumVal ord="2">blocked</EnumVal>
        <EnumVal ord="3">test</EnumVal>
        <EnumVal ord="4">test/blocked</EnumVal>
        <EnumVal ord="5">off</EnumVal>
    </EnumType>
    
</DataTypeTemplates>
```

**关键概念**：
- **LNodeType**：逻辑节点类型，定义 LN 包含哪些 DO
- **DOType**：数据对象类型，定义 DO 包含哪些 DA
- **DAType**：数据属性类型，定义 DA 的结构
- **EnumType**：枚举类型，定义状态值的含义

---

## 八、SCL 文件的工作流程

```
阶段1: 厂商提供 ICD
    │
    ▼
<IED name="TEMPLATE">      ← 模板化 IED，name="TEMPLATE"
    <Services>...</Services>   ← 支持的服务
    <DataTypeTemplates>...</DataTypeTemplates>  ← 数据类型定义
</IED>

阶段2: 集成商创建 SCD
    │
    ▼
<Substation>...</Substation>   ← 添加一次系统拓扑
<IED name="IED1" ...>          ← 实例化 IED，指定 name、IP
<Communication>...</Communication>  ← 配置通信参数

阶段3: 导出 CID 下载到设备
    │
    ▼
<IED name="IED1" ...>          ← 只保留该 IED 的配置
    <Communication>...</Communication>  ← 只保留相关通信配置
```

---

## 九、与汽车诊断配置的对比

| 特性 | IEC 61850 SCL | 汽车 ODX/A2L |
|------|---------------|-------------|
| 格式 | XML（标准化） | XML/二进制（厂商实现不一）|
| 描述范围 | 整个系统 + 单个设备 | 单个 ECU |
| 系统拓扑 | 完整支持（Substation/Bay）| 不支持 |
| 通信配置 | 完整支持（IP、MAC、VLAN）| 有限支持 |
| 数据模型 | 面向对象（LN/DO/DA）| 面向信号（Signal/Message）|
| 工具生态 | 成熟（多种商业工具）| 分散（各厂商自有工具）|
| 标准化程度 | 高（强制 Schema）| 中（格式标准，内容私有）|

**关键区别**：
- SCL 是**系统级**配置，强调多设备集成
- ODX 是**设备级**配置，强调单设备诊断能力

---

## 十、实用技巧：如何阅读 SCL 文件

### 技巧1：先看 Header
```xml
<Header id="Project_X" version="1.0" revision="2"/>
```
- version：大版本（结构变化）
- revision：小修订（内容更新）

### 技巧2：用工具验证
使用 SCL 验证工具检查文件是否符合 Schema：
- OMICRON IEDScout
- Siemens SICAM TOOLBOX
- 开源：openSCD

### 技巧3：理解命名规则
```
对象引用：IED1/LD0/MMXU1.PhV.phsA.cVal.mag.f
         │    │   │     │   │   │   │   └─ 浮点值
         │    │   │     │   │   │   └─ 幅值
         │    │   │     │   │   └─ 复数值
         │    │   │     │   └─ A相
         │    │   │     └─ 相电压
         │    │   └─ 测量逻辑节点实例1
         │    └─ 逻辑设备实例0
         └─ IED 名称
```

---

## 十一、总结

Part 6 是 IEC 61850 最实用的部分之一：

1. **SCL 是系统的 DNA**——所有配置信息都在 XML 里
2. **五种文件各司其职**——SSD/ICD/SCD/CID/IID 形成完整工作流
3. **结构清晰分层**——Substation → IED → LD → LN → DO → DA
4. **通信配置完整**——IP、MAC、VLAN、APPID 一网打尽
5. **工具支持成熟**——可以用工具导入导出、验证、比较

**一句话记忆**：
> SCL = 变电站的"配置语言"，XML 格式，描述一切，驱动一切。

---

## 下一步阅读建议

理解了 SCL 的结构，就可以：
- 打开项目里的 `sample-model.icd` 文件对照阅读
- 研究 `iec61850bean` 的 `SclParser` 类，看代码如何解析 SCL
- 尝试修改 SCL 文件，观察系统行为变化

下一步建议阅读：
- **Part 7-1**：信息模型的设计原则——为什么 SCL 要这样设计
- **Part 8-1**：MMS 映射——SCL 里的配置如何变成实际的 MMS 报文

---

*文档系列：IEC 61850 标准解读 | Part 6/13 | 生成于 2026-04-08*
