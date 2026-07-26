# 1 The Wineco protocol scenario 
1. Wineco 协议场景

Many of the examples in this book are based on the development of the "Wineco protocol". This is a fictitious protocol, used simply to illustrate various parts of ASN.1. The first parts of it appear in Figure 13 of Section 1 Chapter 2, and a full copy of the final protocol is given in Appendix 2 below. 本书中的许多示例都是基于“Wineco 协议”的开发的。这实际上是一个虚构的协议，用于说明 ASN.1 中的各种组成部分。该协议的初始部分出现在第 2 章第 1 节的图 13 中，而完整的协议文本则可以在下面的附录 2 中找到。

Wineco is a company selling wine from a variety of outlets, and owning two warehouses, one northern and one southern. Initially all outlets were in the UK only (where the name of an outlet could be supported by the ASCII character set), but later Wineco extended to overseas territories, where a larger character set was needed. Wineco 是一家通过多种渠道销售葡萄酒的公司，同时拥有两个仓库，一个位于北部地区，另一个位于南部地区。最初，所有销售点都仅位于英国境内（此时销售点的名称可以使用 ASCII 字符集来表示）。后来，Wineco 扩展到海外地区，因为在这些地区需要使用更大的字符集来表示销售点名称。

In Figure 13 we see one of the messages we use in the protocol, "Order-for-stock", to request a number of cases of particular types of wine with a specified urgency. We also see the form of a "Branch-identification" type. 在图 13 中，我们看到了该协议中使用的一种消息类型——“订单需求”，用于请求特定类型葡萄酒的一定数量，并明确指定了紧急程度。此外，我们还看到了“分支识别”类型的格式。

In Section 1 Chapter 3 we add the necessary module headers, and some extensibility markers with an insertion point not at the end. Later we turn it into a multi-module specification with "common types" in one module, the top-level type in another, and the ordering protocol message "Order-forstock" in a third. We also introduced a second top-level message in Figure 21, "Return-of-sales", which provides for a report on the sales that have been made within the last period. 在第三章的第一节中，我们添加了必要的模块头文件，以及一些扩展性标记，这些标记的位置并不位于代码的末尾。之后，我们将这个规范扩展为多个模块的组合，其中一个模块包含“通用类型”，另一个模块包含顶层类型，而第三个模块则包含用于排序的协议消息“Order-forstock”。此外，我们在图 21 中引入了第二个顶层消息“Return-of-sales”，该消息用于报告过去一段时间内的销售情况。

In Chapter 4 of Section 1 we populated the "Return-of-sales" message in a hopefully plausible way, but really solely in order to illustrate the remaining ASN.1 basic data types! Exception markers and exception handling are introduced in this Chapter. "Return-of-sales" and the "Reportitem" type it uses are used as the main example for illustration of the output from an ASN.1- compiler-tool, given in Appendix 3 for C and in Appendix 4 for Java. 在第一节的第四章中，我们以一种看似合理的方式填充了“销售回款”信息，但实际上这只是为了展示剩余的 ASN.1 基本数据类型而已！本章还介绍了异常标记和异常处理机制。“销售回款”以及它所使用的“Reportitem”类型，被用作示例来说明 ASN.1 编译器工具的输出结果。相关示例可以在附录 3 中针对 C 语言，以及附录 4 中针对 Java 语言找到。

"Return-of-sales" is also used to illustrate the ASN.1 value notation in at the Section I Chapter 4 (Figure 23). “销售回潮”这一术语也被用来描述 ASN 中的数值表示方式。详见第 I 部分第 4 章（图 23）。

The next use of our example is in Chapter 3 of Section II, when we decide to define a "basic class" protocol as a strict subset of our "full class" protocol, both for ordering and for return of sales. Here we have also added a third top-level message as we enter the digital-cash age! We are up-loading the contents of our electronic till using an enhanced protocol. 我们示例的下一个应用出现在第二部分第 3 章中。在那里，我们决定将“基础类”协议定义为“完整类”协议的严格子集，这一定义适用于排序以及销售退货操作。此外，随着数字现金时代的到来，我们还增加了第三种顶层消息类型。我们现在正在使用一种改进的协议来上传电子收银机的内部数据。

The final major extension is when we decide (in Section II Chapter 6 to change over to use of a Remote Operations metaphor, with four defined operations. This leads to two further modules - one to define the Remote Operations PDU (which in the real world would have been imported from the Remote Operations Service (ROSE) Standard, and one to define the Wineco operation Information Objects. 最后一个重要的扩展环节是，我们在第六章的第二部分中决定采用“远程操作”这一隐喻，并定义出四种具体的操作。这一决策还导致了两个新的模块的创建——一个用于定义远程操作的数据单元（在实际应用中，该数据单元通常来自远程操作服务标准），另一个则用于定义 Wineco 操作的信息对象。

# 2 The full protocol for Wineco 
2. Wineco 的完整协议说明

This appendix gives the final version of the specification of the Wineco protocol in a form that is syntactically correct and complete. 这个附录提供了 Wineco 协议规范的最终版本，其语法正确且内容完整。

```txt
Wineco-common-top-level
{joint-iso-itu-t international-organization(23) set(42)
set-vendors(9) wineco(43) modules(2) top(0)}
DEFINITIONS
AUTOMATIC TAGS ::= BEGIN

EXPORTS;
IMPORTS Order-for-stock FROM
Wineco-ordering-protocol
{wineco-OID modules(2) ordering(1)}
Return-of-sales FROM
Wineco-returns-protocol
{wineco-OID modules(2) returns(2)};
wineco-OID OBJECT IDENTIFIER ::= 
{joint-iso-itu-t international-organization(23) set(42)
set-vendors(9) wineco(43)}

wineco-abstract-syntax ABSTRACT-SYNTAX ::= 
{Wineco-protocol IDENTIFIED BY
{wineco-OID abstract-syntax(1)}
HAS PROPERTY
{handles-invalid-encodings}
--See clause 45.6 --
}

Wineco-protocol ::= CHOICE
{ordering [APPLICATION 1] Order-for-stock,
sales [APPLICATION 2] Return-of-sales,
... ! PrintableString : "See clause 45.7"
}

END
--New page in published spec.
Wineco-ordering-protocol
{joint-iso-itu-t international-organization(23) set(42)
set-vendors(9) wineco(43)modules(2) ordering(1)}
DEFINITIONS
AUTOMATIC TAGS ::= BEGIN

EXPORTS Order-for-stock;

IMPORTS OutletType, Address, Security-Type FROM
Wineco-common-types
{wineco-OID modules(2) common (3)};
wineco-OID OBJECT IDENTIFIER ::= 
{joint-iso-itu-t international-organization(23) set(42)
set-vendors(9) wineco(43)}

Order-for-stock ::= SEQUENCE
{order-no INTEGER,
name-address BranchIdentification,
details SEQUENCE OF

© OS, 31 May 1999 
```

```txt
SEQUENCE
{item OBJECT IDENTIFIER,
cases INTEGER},
urgency ENUMERATED
{tomorrow(0),
three-day(1),
week(2)} DEFAULT week,
authenticator Security-Type}

BranchIdentification ::= SET
{unique-id OBJECT IDENTIFIER,
details CHOICE
{uk [0] SEQUENCE
{name VisibleString,
type OutletType,
location Address},
overseas [1] SEQUENCE
{name UTF8String,
type OutletType,
location Address},
warehouse [2] CHOICE
{northern [0] NULL,
southern [1] NULL} }
}
END
New page in published spec.
Wineco-returns-protocol
{joint-iso-itu-t international-organization(23) set(42)
set-vendors(9) wineco(43) modules(2) returns(2)}
DEFINITIONS
AUTOMATIC TAGS ::=
BEGIN

EXPORTS Return-of-sales;

IMPORTS OutletType, Address, Security-Type FROM
Wineco-common-types
{wineco-OID modules(2) common (3)};
wineco-OID OBJECT IDENTIFIER ::=
{joint-iso-itu-t international-organization(23) set(42)
set-vendors(9) wineco(43)}

Return-of-sales ::= SEQUENCE
{version BIT STRING
{version1 (0), version2 (1)} DEFAULT {version1},
no-of-days-reported-on INTEGER
{week(7), month (28), maximum (56)} (1..56) DEFAULT week,
time-and-date-of-report CHOICE
{two-digit-year UTCTime,
four-digit-year GeneralizedTime},
-- If the system clock provides a four-digit year,
-- the second alternative shall be used. With the
-- first alternative the time shall be interpreted
-- as a sliding window.
reason-for-delay ENUMERATED
{computer-failure, network-failure, other} OPTIONAL,
-- Include this field if and only if the
-- no-of-days-reported-on exceeds seven.
additional-information SEQUENCE OF PrintableString OPTIONAL,
-- Include this field if and only if the
-- reason-for-delay is "other".
sales-data SET OF Report-item,
... ! PrintableString : "See wineco manual chapter 15" } 
```

```txt
Report-item ::= SEQUENCE
{item OBJECT IDENTIFIER,
item-description ObjectDescriptor OPTIONAL,
-- To be included for any newly-stocked item.
bar-code-data OCTET STRING,
-- Represents the bar-code for the item as specified
-- in the wineco manual chapter 29.
ran-out-of-stock BOOLEAN DEFAULT FALSE,
-- Send TRUE if stock for item became exhausted at any
-- time during the period reported on.
min-stock-level REAL,
max-stock-level REAL,
average-stock-level REAL
-- Give minimum, maximum, and average levels during the
-- period as a percentage of normal target stock-level--
wineco-items OBJECT IDENTIFIER ::=
{joint-iso-itu-t international-organization(23) set(42)
set-vendors(9) wineco(43)stock-items (0)}
END

Wineco-common-types
{joint-iso-itu-t internationalRA(23) set(42)
set-vendors(9) wineco(43) modules(2) common(3)}
DEFINITIONS
AUTOMATIC TAGS ::=
BEGIN

EXPORTS OutletType, Address, Security-Type;
-- IMPORTS Security-Type FROM
-- SET-module
-- {joint-iso-itu-t internationalRA(23) set(42) module(6) 0};
--Removed for this appendix to avoid needing the import,
--and replaced by the type below.

Security-Type ::= SEQUENCE{
    algorithm OBJECT IDENTIFIER,
    encoding OCTET STRING}

--OutletType is not populated in main text--
OutletType ::= SEQUENCE
{type ENUMERATED{mail-order, retail},
description CHARACTER STRING}

--Address is not populated in main text--
Address ::= SEQUENCE
{name UTF8String,
town UTF8String,
country UTF8String}
END 
```

# 3 Compiler output for C support for the Wineco protocol 
3. 编译器输出结果：C 语言支持 Wineco 协议

This appendix contains the text produced by the "OSS ASN.1 Tools" product to provide support for a C implementation of "Return-of-sales" and "Report-item" in our Wineco protocol. (Some of this text is generated just for wineco, some is generic definitions obtained from an include file, for example "GeneralizedTime" and "ossBoolean"): 这个附录包含了“OSS ASN.1 工具”产品所生成的文本。这些文本旨在为 Wineco 协议中的“退货信息”和“报告项”功能提供 C 语言实现的支持。（其中一些文本是专门为 Wineco 设计的，另一些则来自包含文件中的通用定义，例如“GeneralizedTime”和“ossBoolean”）。

```c
typedef struct {
    short year; /* YYYY format when used for GeneralizedTime */
    /* YY format when used for UTCTime */

    short month;
    short day;
    short hour;
    short minute;
    short second;
    short millisec;
    short mindiff; /* UTC +/- minute differential */
    ossBoolean utc; /* TRUE means UTC time */
} GeneralizedTime;

typedef GeneralizedTime UTCTime;

typedef struct ObjectID {
    unsigned short length;
    unsigned char *value;
} ObjectID;

typedef struct Report_item {
    unsigned char bit_mask;
# define ran_out_of_stock_present 0x80
    ObjectID item;
char *item_description; /* NULL for not present */
struct {
    unsigned int length;
    unsigned char *value;
} bar_code_data;
ossBoolean ran_out_of_stock; /* ran_out_of_stock_present not set in
* bit_mask implies value is FALSE */
double min_stock_level;
double max_stock_level;
double average_stock_level;
} Report_item;

typedef struct Return_of_sales {
    unsigned char bit_mask;
# define version_present 0x80
# define no_of_days_reported_on_present 0x40
# define reason_for_delay_present 0x20
# define additional_information_present 0x10
    unsigned char version; /* version_present not set in bit_mask
* implies value is { version1 } */ 
```

```c
#    define version1 0x80
#    define version2 0x40
unsigned short no_of_days_reported_on; /* no_of_days_reported_on_present not set * in bit_mask implies value is week */
#    define week 7
#    define month 28
#    define maximum 56
struct {
    unsigned short choice;
    define two_digit_year_chosen 1
    define four_digit_year_chosen 2
    union {
    UTCTime two_digit_year; /* to choose, set choice to * two_digit_year_chosen */
    GeneralizedTime four_digit_year; /* to choose, set choice to * four_digit_year_chosen */
    } u;
} time_and_date_of_report;
enum {
    computer_failure = 0,
    network_failure = 1,
    other = 2
} reason_for_delay; /* optional; set in bit_mask * reason_for_delay_present * if present */
struct _seqof1 {
    struct _seqof1 *next;
    char *value;
} *additional_information; /* optional; set in bit_mask * additional_information_present if present */
struct _setof1 {
    struct _setof1 *next;
    Report_item value;
} *sales_data;
} Return_of_sales; 
```

# 4 Compiler output for Java support for the Wineco protocol 4. 关于 Java 支持 Wineco 协议的编译器输出结果

This appendix contains the text for Java support for the "Return-of-sales" and the "Report-item" types in the Wineco protocol. This is a part of the output produced by the "OSS ASN.1 Tools" product when it is fed with the Wineco modules. This is a bit more bulky than Annex 3 - does that say anything? Whoops - BAD STATEMENT - no way can one appear to be criticising Java! This is more than Figure 999 stuff!. The Java code is bulkier because it contains all the methods for setting and reading fields and for inserting and deleting items in SEQUENCE OF, so it does rather more than the C code in Appendix 3. If you don't know Java, you will certainly want to ignore this appendix. Even if you do know Java, you will probably only want to look at a few sample classes and methods. Here is the Java code: 这个附录包含了关于 Wineco 协议中“销售回执”和“报告项”类型的 Java 支持的相关文本。这部分内容是由“OSS ASN.1 工具”产品在接收 Wineco 模块后生成的输出结果。这部分内容比附件 3 要复杂一些——不过，这难道意味着我在批评 Java 吗？哎呀，这种说法不对哦！这根本不是批评 Java，而是指出其中的一些细节问题。Java 代码比较冗长，因为它包含了设置读取字段以及使用“SEQUENCE OF”结构来插入和删除项的所有方法，所以它的复杂度比附录 3 中的 C 代码要高得多。如果你不懂 Java，那么肯定不想看这个附录。即使你懂 Java，也大概只会想看看其中的几个示例类和方法而已。以下是 Java 代码：

```java
package wineco.wineco_returns_protocol;
import com.oss.asn1.*;
import com.oss.util.*;
import wineco.*;
import wineco.wineco_common_types.*;

public class Return_of_sales extends Sequence {

    /**
    The default constructor.
    */
    public Return_of_sales() {}

    protected ASN1World getASN1World()
    { return wineco.Wineco.cASN1World; }
    protected int getTypeIndex()
    { return Wineco_returns_protocol.Return_of_sales_PDU; }

    /**
    Construct from a IAAPI Value Reference.
    */
    public Return_of_sales(ASN1World world, int index)
    { ASN1Module.getValueReference(world, this, index); }

    /**
    Construct with components.
    */
    public Return_of_sales(
    Version version,
    No_of_days_reported_on no_of_days_reported_on,
    Time_and_date_of_report time_and_date_of_report,
    Reason_for_delay reason_for_delay,
    Additional_information additional_information,
    Sales_data sales_data)
    {
    SetVersion(version);
    SetNo_of_days_reported_on(no_of_days_reported_on);
    SetTime_and_date_of_report(time_and_date_of_report);
    SetReason_for_delay(reason_for_delay);
    SetAdditional_information(additional_information);

    }
} 
```

```txt
SetSales_data(sales_data);
}

/**
Construct with required components.
*/
public Return_of_sales(
    Time_and_date_of_report time_and_date_of_report,
    Sales_data sales_data)
{
    SetTime_and_date_of_report(time_and_date_of_report);
    SetSales_data(sales_data);
}

protected void initComponents()
{
    mComponents[0] = new Version();
    mComponents[1] = new No_of_days_reported_on();
    mComponents[2] = new Time_and_date_of_report();
    mComponents[3] = new Reason_for_delay();
    mComponents[4] = new Additional_information();
    mComponents[5] = new Sales_data();
}

// Instance initializer
{
    mComponents = new AbstractData[6];
    mPresentBits = new java.util.BitSet(mComponents.length);
}

// Methods for field "version"
public Version getVersion()
{
    return (Version)mComponents[0];
}
public void SetVersion(Version version)
{
    mComponents[0] = version;
    SetComponentPresent(0);
}
public void SetVersionToDefault() {SetComponentAbsent(0); }
public boolean hasDefaultVersion() { return componentIsPresent(0); }
public boolean hasVersion() { return componentIsPresent(0); }
public void deleteVersion() { SetComponentAbsent(0); }

public static class Version extends BitString {
    /**
    The default constructor.
    */
    public Version() { super(new byte[1], 2); }

    /**
    Construct Bit String from a byte array and significant bits.
    @param value the byte array to set this object to.
    @param sigBits the number of significant bits.
    */
    public Version(byte[] value, int sigBits)
    { super(value, sigBits); }

    protected ASN1World getASN1World()
    { return wineco.Wineco.cASN1World; }

    // Named list definitions.
    public static final int version1 = 0;
S, 31 May 1999 
```

```lisp
public static final int version2 = 1;
} // End class definition for Version

// Methods for field "no_of_days_reported_on"
public No_of_days_reported_on getNo_of_days_reported_on()
{
    return (No_of_days_reported_on)mComponents[1];
}
public void SetNo_of_days_reported_on
    (No_of_days_reported_on no_of_days_reported_on)
{
    mComponents[1] = no_of_days_reported_on;
    SetComponentPresent(1);
}
public void SetNo_of_days_reported_onToDefault()
    {SetComponentAbsent(1); }
public boolean hasDefaultNo_of_days_reported_on()
    {return componentIsPresent(1); }
public boolean hasNo_of_days_reported_on()
    {return componentIsPresent(1); }
public void deleteNo_of_days_reported_on()
    {SetComponentAbsent(1); }

public static class No_of_days_reported_on extends INTEGER {

    /**
    The default constructor.
    */
    public No_of_days_reported_on() {}
    public No_of_days_reported_on(short value) { super(value);}
    public No_of_days_reported_on(int value) { super(value);}
    public No_of_days_reported_on(long value) { super(value);}
    protected ASN1World getASN1World()
    { return wineco.Wineco.cASN1World; }

    // Named list definitions.
    public static final No_of_days_reported_on week =
    new No_of_days_reported_on(7);
    public static final No_of_days_reported_on month =
    new No_of_days_reported_on(28);
    public static final No_of_days_reported_on maximum =
    new No_of_days_reported_on(56);
    private final static No_of_days_reported_on cNamedNumbers[] = {week, month, maximum};
    protected final static long cFirstNumber = 7;
    protected final static boolean cLinearNumbers = false;
    protected INTEGER[] getNamedNumbers() { return cNamedNumbers;}
    protected boolean hasLinearNumbers() { return cLinearNumbers;}
    protected long getFirstNumber() { return cFirstNumber;}
} // End class definition for No_of_days_reported_on

// Methods for field "time_and_date_of_report"
public Time_and_date_of_report getTime_and_date_of_report()
{
    return (Time_and_date_of_report)mComponents[2];
}
public void SetTime_and_date_of_report
    (Time_and_date_of_report time_and_date_of_report)
{
    mComponents[2] = time_and_date_of_report;
} 
```

```java
public static class Time_and_date_of_report extends Choice {

    /**
    The default constructor.
    */
    public Time_and_date_of_report() {}

    protected ASN1World getASN1World()
    { return wineco.Wineco.cASN1World; }

    /**
    Construct from a IAAPI Value Reference.
    */
    public Time_and_date_of_report(ASN1World world, int index)
    { ASN1Module.getValueReference(world, this, index); }

    public static final int two_digit_year_chosen = 1;
    public static final int four_digit_year_chosen = 2;

    // Methods for field "two_digit_year"
    public static Time_and_date_of_report
    createTime_and_date_of_reportWithTwo_digit_year
    (UTCTime two_digit_year)
    {Time_and_date_of_report __object =
    new Time_and_date_of_report();
    __object.SetTwo_digit_year(two_digit_year);
    return __object;
    }
    public boolean hasTwo_digit_year() {
    return getChosenFlag() == two_digit_year_chosen;
    }
    public void SetTwo_digit_year (UTCTime two_digit_year) {
    SetChosenValue(two_digit_year);
    SetChosenFlag(two_digit_year_chosen);
    }
    // Methods for field "four_digit_year"
    public static Time_and_date_of_report
    createTime_and_date_of_reportWithFour_digit_year
    (GeneralizedTime four_digit_year)
    {Time_and_date_of_report __object =
    new Time_and_date_of_report();
    __object.SetFour_digit_year(four_digit_year);
    return __object;
    }
    public boolean hasFour_digit_year() {
    return getChosenFlag() == four_digit_year_chosen;
    }
    public void SetFour_digit_year
    (GeneralizedTime four_digit_year) {
    SetChosenValue(four_digit_year);
    SetChosenFlag(four_digit_year_chosen);
    }
    // Method to create a specific choice instance
    protected AbstractData createInstance(int chosen) {
    switch(chosen) {
    case two_digit_year_chosen: return
    new UTCTime();
    case four_digit_year_chosen: return
    new GeneralizedTime();
    default: throw
    new InternalError("Choice.createInstance()");
    }
    }
} // End class definition for Time_and_date_of_report 
```

```txt
// Methods for field "reason_for_delay"
public Reason_for_delay getReason_for_delay()
{
    return (Reason_for_delay)mComponents[3];
}
public void SetReason_for_delay(Reason_for_delay reason_for_delay)
{
    mComponents[3] = reason_for_delay;
    SetComponentPresent(3);
}
public boolean hasReason_for_delay()
    { return componentIsPresent(3); }
public void deleteReason_for_delay()
    { SetComponentAbsent(3); }

public static class Reason_for_delay extends Enumerated {

    /**
    The default constructor.
    */
    public Reason_for_delay() {super(cFirstNumber);}
    protected Reason_for_delay(long value) { super(value); }

    protected ASN1World getASN1World()
    { return wineco.Wineco.cASN1World; }

    // Named list definitions.
    public static final Reason_for_delay computer_failure =
    new Reason_for_delay(0);
    public static final Reason_for_delay network_failure =
    new Reason_for_delay(1);
    public static final Reason_for_delay other =
    new Reason_for_delay(2);
    private final static Reason_for_delay cNamedNumbers[] =
    {computer_failure, network_failure, other};
    protected final static long cFirstNumber = 0;
    protected final static boolean cLinearNumbers = false;
    protected Enumerated[] getNamedNumbers() { return cNamedNumbers;}
    protected boolean hasLinearNumbers() { return cLinearNumbers;}
    protected long getFirstNumber() { return cFirstNumber;}
} // End class definition for Reason_for_delay

// Methods for field "additional_information"
public Additional_information getAdditional_information()
{
    return (Additional_information)mComponents[4];
}
public void SetAdditional_information
    (Additional_information additional_information)
{
    mComponents[4] = additional_information;
    SetComponentPresent(4);
}
public boolean hasAdditional_information()
    { return componentIsPresent(4); }
public void deleteAdditional_information()
    { SetComponentAbsent(4); }

public static class Additional_information extends SequenceOf {

    /**
    The default constructor.
    */ 
```

```lisp
public Additional_information() {}

protected ASN1World getASN1World()
    { return wineco.Wineco.cASN1World; }

/**
Construct from a IAAPI Value Reference.
*/
public Additional_information(ASN1World world, int index)
{ASN1Module.getValueReference(world, this, index); }

/**
Add an Element to the SEQUENCE OF/SET OF.
*/
public synchronized void add(PrintableString element)
{
    super.addElement(element);
}
/**
Set an Element in the SEQUENCE OF/SET OF.
*/
public synchronized void set
(PrintableString element, int atIndex)
{
    super.SetElement(element, atIndex);
}
/**
Get an Element from the SEQUENCE OF/SET OF.
*/
public synchronized PrintableString get(int atIndex)
{
    return (PrintableString) super.getElementById(atIndex);
}
/**
Insert an Element into the SEQUENCE OF/SET OF.
*/
public synchronized void insert
(PrintableString element, int atIndex)
{
    super.insertElement(element, atIndex);
}
/**
Remove an Element from the SEQUENCE OF/SET OF.
*/
public synchronized void remove(PrintableString element)
{
    super.removeElement(element);
}
/**
Create an instance of SEQUENCE OF/SET OF.
*/
public AbstractData createInstance()
{
    return ((AbstractData) new PrintableString());
}
} // End class definition for Additional_information

// Methods for field "sales_data"
public Sales_data getSales_data()
{
    return (Sales_data)mComponents[5];
}
public void SetSales_data(Sales_data sales_data)
{
    }
} 
```

```txt
mComponents[5] = sales_data;
}

public static class Sales_data extends SetOf {

    /**
    The default constructor.
    */
    public Sales_data() {}

    protected ASN1World getASN1World()
    { return wineco.Wineco.cASN1World; }

    /**
    Construct from a IAAPI Value Reference.
    */
    public Sales_data(ASN1World world, int index)
    { ASN1Module.getValueReference(world, this, index); }

    /**
    Add an Element to the SEQUENCE OF/SET OF.
    */
    public synchronized void add(Report_item element)
    {
    super.addElement(element);
    }
    /**
    Set an Element in the SEQUENCE OF/SET OF.
    */
    public synchronized void set(Report_item element, int atIndex)
    {
    super.SetElement(element, atIndex);
    }
    /**
    Get an Element from the SEQUENCE OF/SET OF.
    */
    public synchronized Report_item get(int atIndex)
    {
    return (Report_item) super Element(atIndex);
    }
    /**
    Insert an Element into the SEQUENCE OF/SET OF.
    */
    public synchronized void insert
    (Report_item element, int atIndex)
    {
    super.insertElement(element, atIndex);
    }
    /**
    Remove an Element from the SEQUENCE OF/SET OF.
    */
    public synchronized void remove(Report_item element)
    {
    super.removeElement(element);
    }
    /**
    Create an instance of SEQUENCE OF/SET OF.
    */
    public AbstractData createInstance()
    {
    return ((AbstractData) new Report_item());
    }
} // End class definition for Sales_data
// End class definition for Return_of_sales 
```

```java
public class Report_item extends Sequence {

    /**
    The default constructor.
    */
    public Report_item() {}

    protected ASN1World getASN1World()
    { return wineco.Wineco.cASN1World; }

    /**
    Construct from an IAAPI Value Reference.
    */
    public Report_item(ASN1World world, int index)
    { ASN1Module.getValueReference(world, this, index); }

    /**
    Construct with components.
    */
    public Report_item(
    ObjectIdentifier item,
    ObjectDescriptor item_description,
    OctetString bar_code_data,
    boolean ran_out_of_stock,
    double min_stock_level,
    double max_stock_level,
    double average_stock_level)
    {
    SetItem(item);
    SetItem_description(item_description);
    SetBar_code_data(bar_code_data);
    SetRan_out_of_stock(ran_out_of_stock);
    SetMin_stock_level(min_stock_level);
    SetMax_stock_level(max_stock_level);
    SetAverage_stock_level(average_stock_level);
    }

    /**
    Construct with required components.
    */
    public Report_item(
    ObjectIdentifier item,
    OctetString bar_code_data,
    double min_stock_level,
    double max_stock_level,
    double average_stock_level)
    {
    SetItem(item);
    SetBar_code_data(bar_code_data);
    SetMin_stock_level(min_stock_level);
    SetMax_stock_level(max_stock_level);
    SetAverage_stock_level(average_stock_level);
    }

    protected void initComponents()
    {
    mComponents[0] = new ObjectIdentifier();
    mComponents[1] = new ObjectDescriptor();
    mComponents[2] = new OctetString();
    mComponents[3] = new BOOLEAN();
    mComponents[4] = new Real();
    mComponents[5] = new Real();
    mComponents[6] = new Real();
} 
```

```lisp
// Instance initializer
{
    mComponents = new AbstractData[7];
    mPresentBits = new java.util.BitSet(mComponents.length);
    mComponents[3] = new BOOLEAN();
    mComponents[4] = new Real();
    mComponents[5] = new Real();
    mComponents[6] = new Real();
}

// Methods for field "item"
public ObjectIdentifier getItem()
{
    return (ObjectIdentifier)mComponents[0];
}
public void SetItem(ObjectIdentifier item)
{
    mComponents[0] = item;
}

// Methods for field "item_description"
public ObjectDescriptor getItem_description()
{
    return (ObjectDescriptor)mComponents[1];
}
public void SetItem_description(ObjectDescriptor item_description)
{
    mComponents[1] = item_description;
    SetComponentPresent(1);
}
public boolean hasItem_description()
    { return componentIsPresent(1); }
public void deleteItem_description()
    { SetComponentAbsent(1); }

// Methods for field "bar_code_data"
public OctetString getBar_code_data()
{
    return (OctetString)mComponents[2];
}
public void SetBar_code_data(OctetString bar_code_data)
{
    mComponents[2] = bar_code_data;
}

// Methods for field "ran_out_of_stock"
public boolean getRan_out_of_stock()
{
    return ((BOOLEAN) mComponents[3]).booleanValue();
}
public void SetRan_out_of_stock(boolean ran_out_of_stock)
{
    ((BOOLEAN) mComponents[3]).SetValue(ran_out_of_stock);
    SetComponentPresent(3);
}
public void SetRan_out_of_stockToDefault()
    {SetComponentAbsent(3); }
public boolean hasDefaultRan_out_of_stock()
    { return componentIsPresent(3); }
public boolean hasRan_out_of_stock()
    { return componentIsPresent(3); }
public void deleteRan_out_of_stock() 
```

```cpp
{
    SetComponentAbsent(3);
}

// Methods for field "min_stock_level"
public double getMin_stock_level()
{
    return ((Real) mComponents[4]).doubleValue();
}
public void SetMin_stock_level(double min_stock_level)
{
    ((Real) mComponents[4]).SetValue(min_stock_level);
}

// Methods for field "max_stock_level"
public double getMax_stock_level()
{
    return ((Real) mComponents[5]).doubleValue();
}
public void SetMax_stock_level(double max_stock_level)
{
    ((Real) mComponents[5]).SetValue(max_stock_level);
}

// Methods for field "average_stock_level"
public double getAverage_stock_level()
{
    return ((Real) mComponents[6]).doubleValue();
}
public void SetAverage_stock_level(double average_stock_level)
{
    ((Real) mComponents[6]).SetValue(average_stock_level);
}
} // End class definition for Report_item 
```

## 5 ASN.1 resources via the Web 
通过网络获取 5 个 ASN.1 资源。

This appendix provides a single link to an OSS Nokalva site that contains both links to other Web resources and extensions of this book. In particular, it contains: 这个附录提供了一个链接到 OSS Nokalva 网站的途径，该网站包含对其他网络资源的链接以及本书内容的扩展内容。具体来说，它包含以下内容：

References to other publications (both Web-based and hard-copy) that are relevant to readers of this book. 本书的读者可以参考其他相关出版物（包括网络版和纸质版）。

• A glossary of terms relevant to ASN.1, including all the acronyms used in this book. (Most of the acronyms used here are also included in the index, which will provide you with a quick look-up and perhaps a little more information.) • 一份与 ASN.1 相关的术语表，包含了本书中使用的所有缩写词。这里使用的绝大多数缩写词也都在索引中有所记载，您可以通过索引快速查找相关信息，或许还能获得一些额外的信息。

Details of, and/or links to other web-based ASN.1 resources such as mailing lists, Olivier Dubuisson's site with his book, the Unicode site, my own site with my book "Understanding OSI", the International Register site, ITU-T and ETSI sites, a site giving the allocations for some parts of the Object Identifier tree, etc etc. 其他基于网络的 ASN 资源的相关信息及链接，例如邮件列表、Olivier Dubuisson 关于其书籍的网站、Unicode 相关网站、我自己的网站（上面有我的书籍《理解 OSI》的介绍）、国际注册数据库网站、ITU-T 和 ETSI 相关网站、以及一些关于对象标识符树中各个部分分配情况的网站等。

More details of specifications that are defined using ASN.1, with links to electronic versions of those specifications where these are known to be publicly available. 关于使用 ASN 定义的规范细节，包括这些规范的电子版本链接。如果这些规范确实可以公开获取，那么还会提供相应的链接。

Errata sheets for this book as and when they are produced. 关于本书的错误说明会会在需要的时候被发布出来。

• An electronic copy of this book. • 这本书的电子版。

The URL for the OSS Nokalva site is: OSS Nokalva 网站的 URL 是：

[http://www.nokalva.com](http://www.nokalva.com)

Please come and visit! 请来参观吧！

And just in case things might move – URLs have a habit of changing – a cross-link is also provided at: 以防情况发生变化——URL 往往会更改——同时，还提供了一个交叉链接：

[http://www.larmouth.demon.co.uk/books](http://www.larmouth.demon.co.uk/books)

## Index 索引

{ ...}....229 7 7-layer model....25 A abstract syntax....25 Abstract Syntax Notation One....16, 328 abstract syntaxes....345 ABSTRACT-SYNTAX....49, 73, 76 ANY....230 ANY DEFINED BY....231 API....117, 122 application-required modules....77 application-required types....76 applications of ASN.1....357 ASN.1 module....62 ASN.1 tools....39, 44 ASN.1-compiler-tool....111 automatic tagging....68 AUTOMATIC TAGGING....54 AUTOMATIC TAGS....66 B Bacchus-Naur Form....42 Basic Encoding Rules....30, 236, 252 BER....30, 252 Binary-based Specification....24 BIT STRING....84 BMPString....153 BOOLEAN....80 C canonical....34 canonical order of tags....291 CGM....35 CHARACTER STRING....233 character string types....97, 100, 149, 338 value notation....155 Character-based Specification....24 collections....102, 157 colon....58 comment....58 Common Object Request Broker Architecture....32 compiler....111 COMPONENTS OF....94 © OS, 31 May 1999 { ...}....229 7 7 层模型....25 抽象语法规范....25 抽象语法表示法....16, 328 各种抽象语法结构....345 抽象语法....49, 73, 76 任意....230 由…定义的任意对象....231 API 接口....117, 122 应用程序所需的模块....77 应用程序所需的类型....76 ASN.1 的应用....357 ASN.1 模块....62 ASN.1 工具....39, 44 ASN.1 编译器工具....111 自动标记....68 自动标记技术....54 自动标记....66 B 巴克斯-诺尔格式....42 基本编码规则....30, 236, 252 BER 编码....30, 252 基于二进制的规范描述....24 位串....84 BMP 字符串....153 布尔类型....80 C 规范版本....34 标签的规范顺序....291 CGM 代码....35 字符串....233 字符串类型....97, 100, 149, 338 值表示法....155 基于字符的规范描述....24 集合描述....102, 157 冒号....58 注释....58 通用对象请求代理架构....32 编译器....111 组件列表....94 © 操作系统，1999 年 5 月 31 日

Computer Graphics Metafile....35 concrete syntax....34 CONSTRAINED BY....220 constraints....97, 108 contained subtype constraints....166 CORBA....32 Courier....43, 325, 334 计算机图形元文件……35 种具体语法规则……34 种受约束的条件……220 个约束条件……97 个、108 个包含的子类型约束条件……166 个 CORBA 相关规则……32 条 Courier 规则……43 条、325 条、334 条规则

D date/time types....91 DEFAULT....51 design issues....123 development process....18 distinguished values....80 duplicating text....64 日期/时间类型……91 默认设置……51 设计问题……123 开发过程……18 独特的数值……80 重复文本的处理……64

E EDIFACT....41 effective alphabet constraint....290 effective size constraint....290 ellipsis....69, 130, 182, 352 EMBEDDED PDV....232 Encoding....33 encoding rules....16, 30, 236 ENUMERATED....82 ERROR....345 exception handling....131, 139 exception specification....134 exceptions....104, 181 EXPLICIT....54 explicit tagging....68 EXPLICIT TAGS....66 EXPORTS....71 extensibility28, 60, 66, 70, 97, 104, 129, 139, 181, 282 EXTENSIBILITY IMPLIED....66 EXTERNAL....231 E EDIFACT……41 种有效的字母表约束条件……290 种有效的尺寸约束条件……290 个省略号……69、130、182、352 条嵌入式 PDV 约束条件……232 条编码约束条件……33 条编码规则……16、30、236 条例外处理规则……82 条错误处理规则……131、139 条异常处理规则……134 条异常说明……104、181 条直接约束条件……54 条明确标签约束条件……68 条明确标签……66 条导出约束条件……71 条可扩展性约束条件……28、60、66、70、97、104、129、139、181、282 条可扩展性约束条件……66 条隐含可扩展性约束条件……66 条外部约束条件……231 条

G GeneralizedTime....91 GeneralString....153 governor....56 GraphicString....153 G 扩展时间....91 G 通用字符串....153 州长....56 图形字符串....153

H holes....26, 97, 105, 188, 190, 275 H 数字……26、97、105、188、190、275

## I

IA5String ..... 152 IDL ..... 32 IETF ..... 15 IMPLICIT ..... 54 implicit tagging ..... 67 IMPLICIT TAGS ..... 66 IMPORTS ..... 71 information object classes ..... 107, 209 information object sets ..... 201 inner subtyping ..... 166 insertion point ..... 70, 184, 308 INSTANCE OF ..... 276 INTEGER ..... 80 Interface Definition Language ..... 32, 191 International Standards Organization ..... 15, 25 International Telecommunications Union Telecommunications Standards Sector ..... 15 Internet Engineering Task Force ..... 15 Internet Protocol ..... 16, 39 IP23, 39 IPv6 ..... 28 ISO ..... 15, 25 ISO646String ..... 151 ITU-T ..... 15, 43, 361 IA5String..... 152 接口定义语言..... 32 IETF..... 15 隐式标签..... 54 隐式标签标注..... 67 隐式标签..... 66 导入语句..... 71 信息对象类..... 107, 209 信息对象集..... 201 内部类型标注..... 166 插入点..... 70, 184, 308 实例引用..... 276 整数..... 80 接口定义语言..... 32, 191 国际标准化组织..... 15, 25 国际电信联盟电信标准部门..... 15 互联网工程任务组..... 15 互联网协议..... 16, 39 IP23, 39 IPv6..... 28 ISO 标准..... 15, 25 ISO646String..... 151 ITU-T 标准..... 15, 43, 361

## L

layering....25 分层……25
layout....57 布局……57
leading bit....85, 266 领先的部分……85, 266
Light-Weight Encoding Rules....316 轻量级编码规则……316
line monitor....38, 140 线路监控器……38, 140
line numbers....63 行数……63
LWER....316 LWER……316

## M

machine-readable version....64 macros....97, 106, 345 mailing list....140 management issues....123 mapping....117 MBER....319 Message Handling Systems....43, 359 Minimum Bit Encoding Rules....319 机器可读取版本……64 个宏函数……97、106、345 个邮件列表……140 个管理问题……123 个映射操作……117 个 MBER 功能……319 个消息处理系统功能……43、359 条最小位编码规则……319

## N

named bits....84, 85, 86, 266 名为的位……84、85、86、266
names....57 名称……57 个
NULL....88 空值……88
NumericString....150 数字字符串……150

## O

OBJECT IDENTIFIER.....49, 89, 97, 100, 143, 334 对象标识符……49、89、97、100、143、334

object identifier encoding....270 object identifier tree....144 ObjectDescriptor....90 OCTET STRING....87 ODA....36 Office Document Architecture....36, 353 OID tree....90 OMG....15 Open Management Group....15 Open Systems Interconnection....25 open types....134 OPERATION....345 OSI....25 OSI layering....189 OSS ASN.1 Tools....13, 110, 372, 374 对象标识符编码....270 对象标识符树....144 对象描述符....90 八位组字符串编码....87 对象标识符编码....36 办公文档架构....36, 353 对象标识符树....90 开放管理组....15 开放系统互连....25 开放类型....134 操作类型....345 OSI 模型....25 OSI 层结构....189 OSS ASN.1 工具....13, 110, 372, 374

## P

Packed Encoding Rules....30, 243, 278 parameterization....108, 134, 205, 221 people....325 PER....30, 243, 278 PER visible constraints....284 permitted alphabet constraints....163 PrintableString....89, 151 protocol....22 Protocol specification....24 Publication style....62 压缩编码规则……30、243、278 个参数化选项……108、134、205、221 个人因素……325 个 PER 值……30、243、278 个可见约束条件……284 个允许的字母表约束条件……163 个可打印字符串……89、151 个协议……22 个协议规范……24 种出版风格……62

## R

range constraint....82, 97, 162, 164 范围限制……82、97、162、164
REAL....83, 337 真正的……83, 337
relational constraint....108 关系约束……108
RELATIVE OID....336 相对对象标识……336
remote operations....190 远程操作……190
ROSE....190 玫瑰……190

## S

scope rules....81 Secure Electronic Transactions....15, 365 selection type notation....93 semantic model....109 semi-colon....58 SEQUENCE....95 SET....15, 95, 147, 365 size constraints....164 sliding window....91 style....128 subsetting....168 subtypes....97, 102, 159 范围规则……81 安全电子交易……15，365 选择类型表示法……93 语义模型……109 分号……58 序列……95 集合……15，95，147，365 大小限制……164 滑动窗口……91 风格……128 子集化……168 子类型……97，102，159

## T

T61String....152 table constraint....108 tagging environment....66 T61String……152 表格约束条件……108 标签环境……66

tags ....54, 97, 103, 136, 172 标签：....54、97、103、136、172
TCP/IP ....16, 23
TeletexString....152 TeletexString…152
time differential....92 时间差……92
TLV ....29, 40, 236, 239 TLV：29、40、236、239
top-level type....49 顶级类型……49
trailing bit ....85, 266 尾位……85, 266
transfer syntax....30, 34 转移语法……30, 34
Transmission Control Protocol ....16 传输控制协议……16
type assignment....56 类型赋值……56
TYPE-IDENTIFIER....225 类型标识符……225

## U

Unicode....342 UniversalString....153 Useful Type....90 user-defined constraint....108, 220 Unicode……342 UniversalString……153 Useful Type……90 用户自定义约束条件……108, 220

UTCTime....91 UTF8String....154 V value assignments....56 value reference assignment....56 variable syntax....216 version brackets....97, 104, 181 VideotexString....152 VisibleString....151 W WITH SYNTAX....216 X X.400....43, 358 UTCTime....91 UTF8String....154 变量赋值....56 变量引用赋值....56 变量语法错误....216 版本括号....97、104、181 VideotexString....152 VisibleString....151 语法说明....216 X X.400....43、358