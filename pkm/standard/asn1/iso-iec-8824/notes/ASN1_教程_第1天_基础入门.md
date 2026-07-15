# ASN.1 基础入门

## 1. ASN.1概览

### 1.1 ASN.1是什么？

ASN.1（Abstract Syntax Notation One）是一种**抽象语法记法一**，用于定义数据类型、值和数据类型的约束。根据GB/T 16262.1-2025，它是"一个称为抽象语法记法一的标准记法"。

**核心特点**：

- 定义数据结构"长什么样"，不定义怎么处理数据
- 类似于JSON Schema + XML Schema
- 可生成多种编程语言的代码

## 2. 实战：完整的可编译ASN.1文件

> 本文使用工具[asn1c](asn1c.md)将asn1文件解码成c语言代码，在windows上使用msys32进行c语言的编译运行。

### 2.1 保存为`basic_types.asn1`

```
-- ===========================================
-- 文件：basic_types.asn1
-- 描述：基本数据类型定义
-- 可直接编译
-- ===========================================

BasicTypesModule DEFINITIONS AUTOMATIC TAGS ::= BEGIN

-- 整数类型定义
AgeType ::= INTEGER
AgeRangeType ::= INTEGER (0..150)
PortNumberType ::= INTEGER (0..65535)

-- 布尔类型定义
BooleanType ::= BOOLEAN
EnabledType ::= BOOLEAN DEFAULT TRUE

-- 八位位组串类型定义
PasswordType ::= OCTET STRING
MacAddressType ::= OCTET STRING (SIZE(6))
DataBlockType ::= OCTET STRING (SIZE(0..4096))

-- 字符串类型定义
UsernameType ::= IA5String
EmailType ::= IA5String (SIZE(5..254))
DomainType ::= IA5String (PATTERN "[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}")

END
```

### 2.2 保存为`person_info.asn1`

```
-- ===========================================
-- 文件：person_info.asn1
-- 描述：个人信息管理系统
-- 可直接编译
-- ===========================================

PersonInfoModule DEFINITIONS AUTOMATIC TAGS ::= BEGIN

-- 性别枚举
Gender ::= ENUMERATED {
    male(0),
    female(1),
    other(2)
}

-- 联系方式类型
ContactType ::= ENUMERATED {
    mobile(0),
    email(1),
    wechat(2),
    qq(3)
}

-- 联系方式结构
ContactInfo ::= SEQUENCE {
    type        ContactType,
    value       IA5String,
    isPrimary   BOOLEAN DEFAULT FALSE
}

-- 人员信息结构
Person ::= SEQUENCE {
    id          INTEGER,
    name        IA5String (SIZE(1..50)),
    gender      Gender OPTIONAL,
    age         INTEGER (0..150),
    contacts    SEQUENCE OF ContactInfo,
    hobbies     SEQUENCE OF IA5String OPTIONAL
}

-- 地址结构
Address ::= SEQUENCE {
    country     IA5String (SIZE(2)),
    province    IA5String (SIZE(1..50)),
    city        IA5String (SIZE(1..50)),
    street      IA5String (SIZE(1..100)),
    zipCode     IA5String (SIZE(6))
}

END
```

### 2.3 保存为`network_protocol.asn1`

```
-- ===========================================
-- 文件：network_protocol.asn1
-- 描述：网络协议示例
-- 可直接编译
-- ===========================================

NetworkProtocolModule DEFINITIONS AUTOMATIC TAGS ::= BEGIN

-- 端口号定义
PortNumber ::= INTEGER (0..65535)

-- 常见端口枚举
WellKnownPorts ::= ENUMERATED {
    ftp(21),
    ssh(22),
    telnet(23),
    smtp(25),
    http(80),
    https(443)
}

-- IP地址类型
IPAddress ::= OCTET STRING (SIZE(4) | SIZE(16))

-- 消息类型定义
MessageType ::= ENUMERATED {
    request(1),
    response(2),
    notification(3),
    error(4)
}

-- 通用消息头
MessageHeader ::= SEQUENCE {
    version     INTEGER,
    type        MessageType,
    source      IPAddress,
    destination IPAddress,
    sourcePort  PortNumber,
    destPort    PortNumber
}

-- 数据消息结构
DataMessage ::= SEQUENCE {
    header  MessageHeader,
    payload OCTET STRING
}

END
```

## 3. 编译使用方法

### 3.1 编译命令

```
# 使用asn1c编译器
asn1c basic_types.asn1
asn1c person_info.asn1
asn1c network_protocol.asn1
```

### 3.2 编译结果

编译成功后，会生成对应的C语言文件：

- `.h`头文件
- `.c`源文件
- 编码/解码函数

## 4. 关键语法说明

### 4.1 必须的模块结构

根据GB/T 16262.1-2025第13章，每个ASN.1文件必须有：

```
ModuleName DEFINITIONS AUTOMATIC TAGS ::= BEGIN
    -- 类型定义放在这里
END
```

### 4.2 类型定义规则

1. **类型名**：以大写字母开头（文档12.2）
2. **赋值符号**：`::=`（文档12.20）
3. **结束符**：每个类型定义以`;`结束

### 4.3 完整的类型示例

```
-- 简单类型
MyInteger ::= INTEGER
MyBoolean ::= BOOLEAN

-- 带约束的类型
LimitedString ::= IA5String (SIZE(1..100))
RangeInteger ::= INTEGER (0..1000)

-- 结构类型
PersonRecord ::= SEQUENCE {
    id      INTEGER,
    name    IA5String,
    age     INTEGER (0..150) OPTIONAL
}

-- 数组类型
NumberList ::= SEQUENCE OF INTEGER
NameList ::= SEQUENCE OF IA5String
```

## 5. 常见错误避免

### 错误1：缺少模块定义

```
-- ❌ 错误：没有模块定义
Age ::= INTEGER
Name ::= IA5String
```

```
-- ✅ 正确：有完整的模块定义
ValidModule DEFINITIONS ::= BEGIN
    Age ::= INTEGER
    Name ::= IA5String
END
```

### 错误2：类型名不规范

```
-- ❌ 错误：类型名小写开头
ageType ::= INTEGER
nameType ::= IA5String
```

```
-- ✅ 正确：类型名大写开头
AgeType ::= INTEGER
NameType ::= IA5String
```

### 错误3：语法不完整

```
-- ❌ 错误：缺少结束符号
Person ::= SEQUENCE {
    id INTEGER
    name IA5String
-- 缺少END
```

```
-- ✅ 正确：完整语法
PersonModule DEFINITIONS ::= BEGIN
    Person ::= SEQUENCE {
        id INTEGER,
        name IA5String
    }
END
```