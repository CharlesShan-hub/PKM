# ASN.1 教程 - 第3天：约束和模块化

## 🎯 学习目标
- 掌握5种常见的数据约束方法
- 学会模块化设计和代码组织
- 理解类型继承和FROM约束
- 能设计可维护的大型ASN.1项目结构

## ⏰ 建议时间：2-3小时

## 📖 课程大纲

### 一、数据约束详解（60分钟）

#### 1.1 为什么需要约束？

**约束的作用**：
1. **数据验证**：确保数据符合业务规则
2. **安全性**：防止无效或恶意数据
3. **性能优化**：提前知道数据范围
4. **文档化**：约束即文档

**约束分类**：

| 约束类型 | 语法 | 用途 |
|----------|------|------|
| 值范围约束 | `(min..max)` | 限制数值范围 |
| 大小约束 | `(SIZE (min..max))` | 限制字符串/数组大小 |
| 枚举约束 | `ENUMERATED {...}` | 限制为特定值集合 |
| 模式约束 | `(PATTERN "...")` | 正则表达式验证 |
| FROM约束 | `FROM Type` | 类型继承/子集 |

#### 1.2 值范围约束

```asn1
-- 1. 整数范围
Age ::= INTEGER (0..150)
Port ::= INTEGER (0..65535)
Percentage ::= INTEGER (0..100)

-- 2. 实数范围（REAL类型）
Temperature ::= REAL (-273.15..1000.0)
Score ::= REAL (0.0..100.0)

-- 3. 枚举值范围
Priority ::= INTEGER {
    low(0),
    medium(1..5),
    high(6..10)
}

-- 4. 特殊值
PositiveInt ::= INTEGER (0..MAX)      -- 非负整数
NonZeroInt ::= INTEGER (MIN..-1 | 1..MAX)  -- 非零整数

-- 5. 复杂范围
RGBValue ::= INTEGER (0..255)        -- 8位颜色值
Year ::= INTEGER (1900..2100)        -- 合理年份
```

**边界情况处理**：
```asn1
-- 包含边界
Inclusive ::= INTEGER (0..100)       -- 包含0和100

-- 排除边界（使用注释说明）
Exclusive ::= INTEGER (1..99)        -- 实际1-98，但编码为1..99

-- 半开区间（需要特殊处理）
HalfOpen ::= INTEGER (0..<100)       -- 0-99，但ASN.1不支持<符号
```

#### 1.3 大小约束

```asn1
-- 1. 字符串大小
Username ::= IA5String (SIZE (3..20))
Password ::= OCTET STRING (SIZE (8..32))
Email ::= UTF8String (SIZE (5..254))

-- 2. 固定大小
MACAddress ::= OCTET STRING (SIZE (6))      -- 固定6字节
UUID ::= OCTET STRING (SIZE (16))           -- 固定16字节
IPv4 ::= OCTET STRING (SIZE (4))            -- 固定4字节

-- 3. 数组大小
PhoneNumbers ::= SEQUENCE OF IA5String (SIZE (1..5))  -- 最多5个号码
Tags ::= SET OF IA5String (SIZE (0..10))              -- 最多10个标签

-- 4. 嵌套大小约束
UserProfile ::= SEQUENCE {
    name        IA5String (SIZE (2..50)),
    bio         IA5String (SIZE (0..500)) OPTIONAL,
    skills      SEQUENCE OF IA5String (SIZE (1..20)) (SIZE (0..10))
    -- 技能名称1-20字符，最多10个技能
}
```

#### 1.4 枚举约束

```asn1
-- 1. 基本枚举
Color ::= ENUMERATED {
    red(0),
    green(1),
    blue(2),
    yellow(3)
}

-- 2. 带描述的枚举
HttpStatus ::= ENUMERATED {
    ok(200),                -- 成功
    badRequest(400),        -- 客户端错误
    unauthorized(401),      -- 未授权
    notFound(404),          -- 未找到
    serverError(500)        -- 服务器错误
}

-- 3. 非连续枚举
ErrorCode ::= ENUMERATED {
    success(0),
    invalidInput(1001),
    networkError(1002),
    databaseError(2001),
    permissionDenied(3001)
}

-- 4. 扩展枚举（预留值）
DeviceType ::= ENUMERATED {
    smartphone(0),
    tablet(1),
    laptop(2),
    desktop(3),
    ...  -- 扩展点，未来可以添加
}

-- 5. 枚举别名
TrafficLight ::= ENUMERATED {
    stop(0),
    caution(1),
    go(2)
}

-- 使用别名
LightState ::= TrafficLight
```

#### 1.5 模式约束（正则表达式）

```asn1
-- 1. 邮箱验证
EmailStrict ::= IA5String (PATTERN "[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}")

-- 2. 电话号码
PhoneNumberCN ::= IA5String (PATTERN "1[3-9]\\d{9}")
PhoneNumberUS ::= IA5String (PATTERN "\\d{3}-\\d{3}-\\d{4}")

-- 3. 日期格式
DateISO ::= IA5String (PATTERN "\\d{4}-\\d{2}-\\d{2}")
TimeISO ::= IA5String (PATTERN "\\d{2}:\\d{2}:\\d{2}")

-- 4. URL验证
HttpURL ::= IA5String (PATTERN "https?://[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}(?:/[^\\s]*)?")
SecureURL ::= IA5String (PATTERN "https://[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}(?:/[^\\s]*)?")

-- 5. 用户名规则
UsernameRule ::= IA5String (PATTERN "[a-zA-Z][a-zA-Z0-9_]{2,19}")

-- 6. 密码强度
PasswordStrong ::= IA5String (PATTERN "(?=.*[a-z])(?=.*[A-Z])(?=.*\\d)(?=.*[@$!%*?&])[A-Za-z\\d@$!%*?&]{8,}")

-- 7. IP地址
IPv4Address ::= IA5String (PATTERN "(?:25[0-5]|2[0-4]\\d|1\\d\\d|[1-9]?\\d)(?:\\.(?:25[0-5]|2[0-4]\\d|1\\d\\d|[1-9]?\\d)){3}")
IPv6Address ::= IA5String (PATTERN "(?:[0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}")
```

#### 1.6 FROM约束（类型继承）

```asn1
-- 1. 基本FROM约束
BaseType ::= INTEGER (0..100)

-- 子类型继承父类型的约束
SmallRange ::= BaseType (0..10)      -- 进一步约束
LargeRange ::= BaseType (90..100)    -- 另一个子集

-- 2. 字符串继承
BaseString ::= IA5String (SIZE (1..100))

ShortString ::= BaseString (SIZE (1..20))
LongString ::= BaseString (SIZE (50..100))

-- 3. 枚举继承
BaseEnum ::= ENUMERATED {
    option1(0),
    option2(1),
    option3(2),
    option4(3)
}

SubEnum ::= BaseEnum (0..2)  -- 只允许0,1,2

-- 4. 复杂类型继承
BasePerson ::= SEQUENCE {
    name    IA5String,
    age     INTEGER (0..150)
}

-- 错误：不能直接继承SEQUENCE
-- Student ::= BasePerson (name (SIZE (2..20)))

-- 正确：使用新的SEQUENCE并引用
Student ::= SEQUENCE {
    base    BasePerson,
    grade   INTEGER (1..12)
}
```

### 二、模块化设计（60分钟）

#### 2.1 为什么需要模块化？

**模块化的好处**：
1. **可维护性**：修改一处不影响其他
2. **复用性**：通用模块多处使用
3. **团队协作**：不同团队负责不同模块
4. **编译优化**：只编译修改的模块

#### 2.2 模块基本语法

```asn1
-- 模块定义
ModuleName DEFINITIONS
    AUTOMATIC TAGS  -- 可选：自动生成标签
    EXTENSIBILITY IMPLIED  -- 可选：允许扩展
    ::= BEGIN
    
    -- 类型定义
    Type1 ::= INTEGER
    Type2 ::= IA5String
    
    -- 值定义
    constant1 Type1 ::= 100
    constant2 Type2 ::= "hello"
    
    -- 导入导出
    EXPORTS Type1, constant1;
    IMPORTS Type3 FROM OtherModule;
    
END
```

#### 2.3 实战：三层架构模块设计

##### 2.3.1 基础层模块（base.asn1）

```asn1
-- 文件：base.asn1
-- 描述：基础数据类型和常量
BaseModule DEFINITIONS AUTOMATIC TAGS ::= BEGIN

-- ====== 导出声明 ======
EXPORTS
    -- 基础类型
    ID, Name, Description, Timestamp,
    -- 状态类型
    Status, Priority,
    -- 常量
    MAX_NAME_LENGTH, MAX_DESC_LENGTH;

-- ====== 基础类型 ======

-- ID类型（各种ID的基础）
ID ::= INTEGER (1..MAX)  -- 正整型ID

-- 名称类型
Name ::= IA5String (SIZE (1..MAX_NAME_LENGTH))

-- 描述类型
Description ::= IA5String (SIZE (0..MAX_DESC_LENGTH))

-- 时间戳
Timestamp ::= GeneralizedTime

-- ====== 状态类型 ======

-- 通用状态
Status ::= ENUMERATED {
    active(0),
    inactive(1),
    pending(2),
    deleted(3),
    archived(4)
}

-- 优先级
Priority ::= ENUMERATED {
    low(0),
    medium(1),
    high(2),
    critical(3)
}

-- ====== 常量定义 ======
MAX_NAME_LENGTH ::= 100
MAX_DESC_LENGTH ::= 1000
DEFAULT_PAGE_SIZE ::= 20
MAX_PAGE_SIZE ::= 100

-- ====== 工具函数注释 ======
-- 注意：ASN.1不支持函数，这里用注释说明用途

END
```

##### 2.3.2 领域层模块（domain.asn1）

```asn1
-- 文件：domain.asn1
-- 描述：业务领域模型
DomainModule DEFINITIONS AUTOMATIC TAGS ::= BEGIN

-- ====== 导入声明 ======
IMPORTS
    ID, Name, Description, Timestamp, Status, Priority,
    MAX_NAME_LENGTH, MAX_DESC_LENGTH
    FROM BaseModule;

-- ====== 用户模块 ======

-- 用户角色
UserRole ::= ENUMERATED {
    guest(0),
    user(1),
    moderator(2),
    admin(3),
    superAdmin(4)
}

-- 用户信息
User ::= SEQUENCE {
    userId      ID,                    -- 用户ID
    username    Name,                  -- 用户名
    email       IA5String (PATTERN "[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}"),
    password    OCTET STRING (SIZE (32)),  -- 密码哈希
    role        UserRole DEFAULT user, -- 角色
    status      Status DEFAULT active, -- 状态
    createdAt   Timestamp,             -- 创建时间
    lastLogin   Timestamp OPTIONAL,    -- 最后登录
    profile     UserProfile OPTIONAL   -- 扩展信息
}

-- 用户配置文件
UserProfile ::= SEQUENCE {
    fullName    Name OPTIONAL,
    avatar      OCTET STRING OPTIONAL,  -- 头像二进制
    bio         Description OPTIONAL,
    settings    UserSettings OPTIONAL
}

-- 用户设置
UserSettings ::= SEQUENCE {
    theme       IA5String DEFAULT "light",
    language    IA5String DEFAULT "zh-CN",
    notifications BOOLEAN DEFAULT TRUE,
    privacyLevel INTEGER (0..3) DEFAULT 1
}

-- ====== 产品模块 ======

-- 产品分类
ProductCategory ::= ENUMERATED {
    electronics(0),
    clothing(1),
    books(2),
    food(3),
    other(4)
}

-- 产品信息
Product ::= SEQUENCE {
    productId   ID,                    -- 产品ID
    name        Name,                  -- 产品名称
    category    ProductCategory,       -- 分类
    price       INTEGER (0..MAX),      -- 价格（分）
    stock       INTEGER (0..MAX),      -- 库存
    description Description OPTIONAL,  -- 描述
    images      SEQUENCE OF OCTET STRING OPTIONAL,  -- 图片
    status      Status DEFAULT active, -- 状态
    createdAt   Timestamp,             -- 创建时间
    updatedAt   Timestamp OPTIONAL     -- 更新时间
}

-- ====== 订单模块 ======

-- 订单状态
OrderStatus ::= ENUMERATED {
    pending(0),      -- 待支付
    paid(1),         -- 已支付
    shipped(2),      -- 已发货
    delivered(3),    -- 已送达
    canceled(4),     -- 已取消
    refunded(5)      -- 已退款
}

-- 订单项
OrderItem ::= SEQUENCE {
    productId   ID,                    -- 产品ID
    quantity    INTEGER (1..MAX),      -- 数量
    unitPrice   INTEGER (0..MAX),      -- 单价
    subtotal    INTEGER (0..MAX)       -- 小计
}

-- 订单信息
Order ::= SEQUENCE {
    orderId     ID,                    -- 订单ID
    userId      ID,                    -- 用户ID
    items       SEQUENCE OF OrderItem, -- 订单项
    totalAmount INTEGER (0..MAX),      -- 总金额
    status      OrderStatus,           -- 状态
    shippingAddress Address OPTIONAL,  -- 收货地址
    createdAt   Timestamp,             -- 创建时间
    updatedAt   Timestamp OPTIONAL     -- 更新时间
}

-- 地址信息
Address ::= SEQUENCE {
    country     IA5String (SIZE (2)),       -- 国家代码
    province    Name,                       -- 省份
    city        Name,                       -- 城市
    district    Name OPTIONAL,              -- 区县
    street      IA5String (SIZE (1..200)),  -- 街道
    zipCode     IA5String (SIZE (6)),       -- 邮编
    recipient   Name,                       -- 收件人
    phone       IA5String (PATTERN "1[3-9]\\d{9}")
}

END
```

##### 2.3.3 应用层模块（api.asn1）

```asn1
-- 文件：api.asn1
-- 描述：API接口定义
ApiModule DEFINITIONS AUTOMATIC TAGS ::= BEGIN

-- ====== 导入声明 ======
IMPORTS
    ID, Name, Status, Priority, Timestamp
    FROM BaseModule;
    
IMPORTS
    User, Product, Order, OrderStatus, Address
    FROM DomainModule;

-- ====== 通用响应结构 ======

-- API响应状态
ApiStatus ::= ENUMERATED {
    success(0),
    error(1),
    warning(2),
    unauthorized(3),
    notFound(4)
}

-- 错误信息
ErrorInfo ::= SEQUENCE {
    code        INTEGER,        -- 错误代码
    message     IA5String,      -- 错误消息
    details     IA5String OPTIONAL,  -- 详细说明
    timestamp   Timestamp       -- 发生时间
}

-- 分页信息
Pagination ::= SEQUENCE {
    page        INTEGER (1..MAX),  -- 当前页码
    pageSize    INTEGER (1..100),  -- 每页大小
    totalPages  INTEGER (0..MAX),  -- 总页数
    totalItems  INTEGER (0..MAX)   -- 总条数
}

-- 通用响应
ApiResponse ::= SEQUENCE {
    status      ApiStatus,      -- 响应状态
    data        CHOICE {
        successData [0] OCTET STRING,  -- 成功数据
        errorInfo   [1] ErrorInfo      -- 错误信息
    },
    pagination  Pagination OPTIONAL,  -- 分页信息
    serverTime  Timestamp      -- 服务器时间
}

-- ====== 用户API ======

-- 登录请求
LoginRequest ::= SEQUENCE {
    username    IA5String,
    password    OCTET STRING,
    deviceId    IA5String OPTIONAL
}

-- 登录响应
LoginResponse ::= SEQUENCE {
    token       OCTET STRING,   -- JWT令牌
    user        User,           -- 用户信息
    expiresAt   Timestamp       -- 过期时间
}

-- 用户查询请求
UserQueryRequest ::= SEQUENCE {
    userId      ID OPTIONAL,
    username    IA5String OPTIONAL,
    role        UserRole OPTIONAL,
    status      Status OPTIONAL,
    page        INTEGER DEFAULT 1,
    pageSize    INTEGER DEFAULT 20
}

-- 用户查询响应
UserQueryResponse ::= SEQUENCE {
    users       SEQUENCE OF User,
    pagination  Pagination
}

-- ====== 产品API ======

-- 产品查询请求
ProductQueryRequest ::= SEQUENCE {
    productId   ID OPTIONAL,
    name        IA5String OPTIONAL,
    category    ProductCategory OPTIONAL,
    minPrice    INTEGER OPTIONAL,
    maxPrice    INTEGER OPTIONAL,
    inStock     BOOLEAN OPTIONAL,
    page        INTEGER DEFAULT 1,
    pageSize    INTEGER DEFAULT 20
}

-- 产品查询响应
ProductQueryResponse ::= SEQUENCE {
    products    SEQUENCE OF Product,
    pagination  Pagination
}

-- ====== 订单API ======

-- 创建订单请求
CreateOrderRequest ::= SEQUENCE {
    userId      ID,
    items       SEQUENCE OF OrderItem,
    shippingAddress Address OPTIONAL,
    notes       IA5String OPTIONAL
}

-- 订单状态更新请求
UpdateOrderStatusRequest ::= SEQUENCE {
    orderId     ID,
    newStatus   OrderStatus,
    reason      IA5String OPTIONAL
}

-- 订单查询请求
OrderQueryRequest ::= SEQUENCE {
    orderId     ID OPTIONAL,
    userId      ID OPTIONAL,
    status      OrderStatus OPTIONAL,
    startDate   Timestamp OPTIONAL,
    endDate     Timestamp OPTIONAL,
    page        INTEGER DEFAULT 1,
    pageSize    INTEGER DEFAULT 20
}

-- 订单查询响应
OrderQueryResponse ::= SEQUENCE {
    orders      SEQUENCE OF Order,
    pagination  Pagination
}

-- ====== 消息类型 ======

-- API消息封装
ApiMessage ::= CHOICE {
    loginReq        [0] LoginRequest,
    loginResp       [1] LoginResponse,
    userQueryReq    [2] UserQueryRequest,
    userQueryResp   [3] UserQueryResponse,
    productQueryReq [4] ProductQueryRequest,
    productQueryResp [5] ProductQueryResponse,
    createOrderReq  [6] CreateOrderRequest,
    updateOrderReq  [7] UpdateOrderStatusRequest,
    orderQueryReq   [8] OrderQueryRequest,
    orderQueryResp  [9] OrderQueryResponse,
    errorResp       [10] ErrorInfo
}

END
```

#### 2.4 模块化最佳实践

**实践1：分层架构**
```
project/
├── base/          # 基础类型
│   ├── types.asn1
│   └── constants.asn1
├── domain/        # 领域模型
│   ├── user.asn1
│   ├── product.asn1
│   └── order.asn1
├── api/           # 接口定义
│   ├── request.asn1
│   └── response.asn1
└── protocol/      # 协议定义
    ├── message.asn1
    └── encoding.asn1
```

**实践2：命名约定**
- 模块名：`业务域_用途`，如`UserModule`
- 类型名：大驼峰，如`UserProfile`
- 常量名：全大写+下划线，如`MAX_LENGTH`
- 文件名：小写+下划线，如`user_profile.asn1`

**实践3：依赖管理**
- 单向依赖：下层不依赖上层
- 循环依赖：严格禁止
- 显式导入：明确列出需要的类型

### 三、约束组合与验证（30分钟）

#### 3.1 多重约束

```asn1
-- 1. 范围和大小组合
StrictString ::= IA5String (SIZE (1..100)) (PATTERN "[a-zA-Z][a-zA-Z0-9_]*")

-- 2. FROM + 其他约束
BaseRange ::= INTEGER (0..1000)
StrictRange ::= BaseRange (100..200) (FROM ODD-VALUES)  -- 100-200的奇数

-- 3. 数组元素约束
StrictArray ::= SEQUENCE OF IA5String (SIZE (1..50)) (SIZE (1..10))
-- 每个字符串1-50字符，数组长度1-10

-- 4. 嵌套约束
ComplexStruct ::= SEQUENCE {
    id      INTEGER (1..10000),
    name    IA5String (SIZE (2..50)) (PATTERN "[a-zA-Z][a-zA-Z ]*"),
    scores  SEQUENCE OF INTEGER (0..100) (SIZE (1..10)),
    tags    SET OF IA5String (SIZE (1..20)) (SIZE (0..5))
}
```

#### 3.2 约束验证时机

| 验证阶段 | 验证内容 | 工具/方法 |
|----------|----------|-----------|
| **编译时** | 语法检查、类型检查 | ASN.1编译器 |
| **编码时** | 值范围、大小约束 | 编码库 |
| **运行时** | 业务逻辑约束 | 应用代码 |
| **传输时** | 数据完整性 | 协议验证 |

#### 3.3 约束错误处理

```asn1
-- 在API响应中包含约束验证错误
ValidationError ::= SEQUENCE {
    field       IA5String,      -- 字段名
    value       IA5String,      -- 原始值
    constraint  IA5String,      -- 约束条件
    message     IA5String       -- 错误信息
}

ValidationResult ::= SEQUENCE {
    isValid     BOOLEAN,
    errors      SEQUENCE OF ValidationError OPTIONAL
}
```

### 四、今日练习

#### 练习1：设计车辆管理系统约束

创建`Vehicle.asn1`，为以下类型添加约束：
1. `Vehicle`：车牌号（正则验证）、VIN码（17位）、生产年份（1900-今年）
2. `Driver`：驾驶证号（规则验证）、年龄（18-70）、驾龄（0-50）
3. `Trip`：里程（0-10000公里）、油耗（0-100L/100km）、时间范围
4. 添加复合约束：重型货车需要A照，客车需要B照

#### 练习2：模块重构

将第2天的`EmployeeModule`重构为三层结构：
1. `base_employee.asn1`：基础类型和常量
2. `domain_employee.asn1`：员工、部门、薪资等模型
3. `api_employee.asn1`：HR系统API接口

要求：支持导入导出，避免循环依赖。

#### 练习3：约束优化

优化`NetworkProtocol`模块：
1. 添加消息大小限制（最大1MB）
2. 添加频率限制（每秒最多100条）
3. 添加内容安全约束（禁止特定关键词）
4. 设计约束验证报告格式

### 五、学习要点总结

| 主题 | 关键技能 | 应用场景 |
|------|----------|----------|
| **值范围约束** | `(min..max)` | 年龄、端口号、百分比 |
| **大小约束** | `(SIZE (...))` | 用户名、密码、数组长度 |
| **模式约束** | `(PATTERN "...")` | 邮箱、电话、URL验证 |
| **FROM约束** | `FROM Type` | 类型继承、子集定义 |
| **模块导入** | `IMPORTS ... FROM` | 代码复用、依赖管理 |
| **模块导出** | `EXPORTS ...` | 接口暴露、封装 |
| **分层设计** | 基础/领域/应用层 | 大型项目架构 |

### 六、今日成就检查

✅ **完成标志**：
- [ ] 能为数值类型添加合理的范围约束
- [ ] 能使用正则表达式验证字符串格式
- [ ] 能设计三层模块化架构
- [ ] 理解IMPORTS和EXPORTS的作用
- [ ] 能回答：FROM约束和子类型有什么区别？

### 七、常见问题与解决

**Q1：约束太多影响性能怎么办？**
- 编译时约束：由编译器检查，不影响运行时
- 编码时约束：轻量级检查（如范围）
- 业务约束：放在应用层，按需检查

**Q2：如何设计可扩展的枚举？**
```asn1
-- 使用...表示可扩展
DeviceType ::= ENUMERATED {
    smartphone(0),
    tablet(1),
    ...  -- 未来可以添加新设备
}

-- 解码时处理未知值
-- 保留一些值用于扩展
ErrorCode ::= ENUMERATED {
    knownError(0..999),
    reserved(1000..1999),  -- 保留给未来使用
    customError(2000..MAX) -- 用户自定义错误
}
```

**Q3：模块循环依赖如何解决？**
1. 提取公共类型到基础模块
2. 使用接口（CHOICE）而不是具体类型
3. 重新设计领域划分
4. 使用前向声明（谨慎使用）

### 八、明日预告

**第4天：标签和编码**
- 标签系统深度解析：UNIVERSAL/APPLICATION/PRIVATE
- 编码规则对比：BER vs DER vs PER vs XER
- IMPLICIT和EXPLICIT的区别与应用
- 实际编码示例和优化技巧

---

## 💡 设计原则总结

1. **约束即文档**：好的约束减少沟通成本
2. **最小权限原则**：只给必要的访问权限
3. **明确接口**：EXPORTS定义清晰接口
4. **单向依赖**：避免循环依赖
5. **渐进式复杂**：从简单开始，逐步添加约束

## 🚀 快速参考

```asn1
-- 今日核心语法
1. INTEGER (0..100)                    -- 值范围
2. IA5String (SIZE (1..50))             -- 大小约束
3. (PATTERN "...")                      -- 模式约束
4. FROM BaseType (subrange)             -- 类型继承
5. IMPORTS ... FROM Module             -- 导入
6. EXPORTS Type1, Type2;               -- 导出
7. Module DEFINITIONS ::= BEGIN ... END -- 模块定义
```

**记住**：约束不是限制，而是保障。好的约束设计能让代码更健壮，减少运行时错误。明天我们将学习数据如何被编码和传输！

---

*模块化设计时，画一张依赖关系图，确保没有循环依赖和过度耦合。*