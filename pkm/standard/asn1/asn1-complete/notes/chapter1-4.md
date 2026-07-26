# Chapter 4 The basic data types and construction mechanisms - closure 
第四章 基本数据类型与构造机制——闭包

## (Or: You need bricks - of various shapes and sizes!) （或者：你需要各种形状和大小的砖块！）

## Summary: 总结：

There are a number of types that are pre-defined in ASN.1, such as: 在 ASN 中，预定义了多种类型，例如：

• INTEGER, • 整数，

• BOOLEAN, • 布尔类型，

• UTF8String. • UTF8String。

These are used to build more complex user-defined types with construction mechanisms such as: 这些工具可用于构建更为复杂的用户自定义类型，其构建机制包括：

• SEQUENCE, • 序列，

• SET, • SET，

• CHOICE, • 选择，

• SEQUENCE OF, • 序列，

• SET OF, • 一组，

• etc. • 等等。

Many of these construction mechanisms have appeared in the examples and illustrations of earlier chapters. 这些构建机制中的许多内容在前面章节的示例和说明中已经出现过。

This chapter completes the detailed presentation of all the basic ASN.1 types, giving in each case a clear description of: 这一章详细介绍了所有基本的 ASN.1 类型，每种类型都给出了清晰的描述：

• the type-notation for the type, • 该类型的表示方式，即类型标记。

• the set of abstract values in the type, and • 类型中抽象值的集合，以及……

• the value-notation for values of that type. • 那种类型的值的表示方式。

Additional pieces of type/value-related notation are also covered, largely completing the discussion of syntax commonly used in pre-1994 specifications. 此外，还涉及了与类型/值相关的其他表示方式，这进一步补全了 1994 年前规范中常用的语法描述。

The chapter ends with a list of additional concepts whose treatment is deferred to either the next chapter (Discussion of advanced features), or to Section II. 这一章的结尾列出了一些需要后续章节（关于高级功能的讨论）或第二部分来详细探讨的附加概念。

## 1 Illustration by example 1. 以实例来说明

In order to illustrate some of the type and value notations, we will define our Return-of-Sales message as in Figure 22. Figure 22 has been designed to include all the basic ASN.1 types apart from NULL, and provides the hook for further discussion of these types. 为了说明一些类型与值表示的用法，我们将如图 22 所示定义“销售回款信息”这一消息格式。图 22 的设计包含了所有基本的 ASN.1 类型，除了 NULL 类型之外，还为进一步讨论这些类型提供了框架。

Figure 22 has been carefully constructed to complete your introduction to all the basic ASN.1 types - that's it folks! 图 22 经过精心制作，旨在帮助您全面了解所有基本的 ASN1 类型。就是这样，朋友们！

Have a good look at Figure 22. It should by now be fairly easy for you to understand its meaning. If you have no problems with it, you can probably skip the rest of this chapter, unless you want to understand ASN.1 well-enough to write a book, or to deliver a course, on it! (We included winecoitems in Figure 22 to reduce the verbosity of the object identifier values in figure 23 later!) 请仔细查看图 22。现在你应该能够比较容易理解它的含义了。如果你没有疑问，那么你可以跳过这一章的其余内容，除非你真的想深入了解 ASN.1，以至于愿意就此撰写一本书或开设一门课程！（我们在图 22 中加入了 winecoitems 元素，这样就能减少图 23 中对象标识符值的复杂性了！）

```asn1
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
... ! PrintableString : "See wineco manual chapter 15"}
Figure 22 (part 1): Illustration of the use of basic ASN.1 types 
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
}
wineco-items OBJECT IDENTIFIER ::=
{ joint-iso-itu-t internationalRA(23) set(42) set-vendors(9)
wineco(43) stock-items (0)}
Figure 22 (part 2): Illustration of the use of basic ASN.1 types 
```

## 2 Discussion of the built-in types 2. 内置类型的讨论

## 2.1 The BOOLEAN type 2.1 布尔类型

(See "ran-out-of-stock" in figure 22). There is nothing to add here. A "BOOLEAN" type has the obvious two abstract values, true and false, but notice that the value-notation is the words "TRUE" or "FALSE" all in capital letters. You can regard the use of capitals as either consistent with the fact that (almost) all the built-in names in ASN.1 are all upper-case, or as inconsistent with the fact that ASN.1 requires that value-reference-names begin with a lower case letter! ASN.1 does not always obey its own rules! （参见图 22 中的“库存耗尽”部分）。这里无需再补充任何内容。BOOLEAN 类型显然有两个抽象值：true 和 false。不过需要注意的是，这些值的表示方式都是用大写字母“TRUE”或“FALSE”来表示的。你可以将使用大写字母的做法视为与 ASN.1 中几乎所有内置名称都使用大写字母这一规则保持一致，或者认为这与 ASN.1 要求值引用名称以小写字母开头的规定相矛盾。实际上，ASN.1 并不总是遵循自己的规则哦！

## 2.2 The INTEGER type 2.2 整数类型

(See "number-of-days-reported-on" in figure 22). This example is a little more complicated than the simple use of "INTEGER" that we saw in Figure 13! The example here contains what are called distinguished values. In some early ASN.1 specifications (ENUMERATED was not added until around 1988) people would sometimes use the “INTEGER” type with a list of distinguished values where today they would use “ENUMERATED”. In fact, the syntax can look quite similar, so we can write the equivalent of the example in figure 13 as: （请参考图 22 中的“报告天数”这一项）。这个例子比图 13 中使用的简单“INTEGER”类型要复杂一些！在这个例子中，使用了所谓的“区分值”。在一些早期的 ASN.1 规范中（直到 1988 年左右才引入了“ENUMERATED”类型），人们有时会使用“INTEGER”类型来定义一组区分值，而如今则使用“ENUMERATED”类型。实际上，这两种语法看起来非常相似，因此我们可以将图 13 中的例子改写为：

<table><tbody><tr><td data-imt-p="1">The integer type 整数类型</td></tr><tr><td data-imt-p="1">Just the word INTEGER, nice and simple!; and/or 仅仅“INTEGER”这个词，既简洁又明了！; 或者……</td></tr><tr><td data-imt-p="1">Add a distinguished value list; and/or 添加一份有价值的清单；或者/和</td></tr><tr><td data-imt-p="1">Add a range specification (subtyping); then 添加范围指定（类型区分）；然后</td></tr><tr><td data-imt-p="1">Put an extension marker and exception specification in the range specification! (Getting complicated again!) 请在范围说明中加上扩展标记和异常说明吧！（又变得复杂了！）</td></tr></tbody></table>

```txt
urgency INTEGER
{tomorrow (0),
    three-day (1),
    week (2)} DEFAULT week 
```

It is, however, important here to notice some important differences. The presence of the list following “INTEGER” is entirely optional (for “ENUMERATED” it is required), and the presence of the list does in no way affect the set of abstract values in the type. 不过，这里需要注意的是一些重要的区别。在“INTEGER”类型之后出现列表是完全可选的（而在“ENUMERATED”类型中则必须是），而且这个列表的存在丝毫不会影响类型中抽象值的集合。

The following two definitions are almost equivalent: 以下两个定义几乎是一致的：

```txt
My-integer ::= INTEGER {tomorrow(0), three-day (1), week(2)} 
```

and 以及

```autohotkey
My-integer ::= INTEGER
tomorrow My-integer ::= 0
three-day My-integer ::= 1
week My-integer ::= 2 
```

The difference lies in ASN.1 scope rules. In the second example the names "tomorrow" etc are value-reference-names that can be assigned only once within the module, can be used anywhere within that module where an integer value is needed (even, in fact, as the number on an enumeration or in another distinguished value list or in a tag - but all these uses would be unusual!), and can appear in an EXPORTS statement at the head of the module. On the other hand, in the first example, the names "tomorrow" etc cannot be exported, can appear (with the same or different values) in other distinguished value lists, or indeed as value-reference names for a value of some totally different type. The name "tomorrow" in the first example has the meaning of identifying the zero value of “My-integer” ONLY when it appears in value notation that is governed by the type “My-integer”, such as when it is used as the “DEFAULT” value for a sequence element of that type. 两者的区别在于 ASN.1 的声明规则。在第二个例子中，诸如“tomorrow”这样的名称属于值引用类型，它们在该模块内只能被赋值一次，并且可以在该模块内的任何需要整数值的地方使用（实际上，它们也可以作为枚举项、其他区分值列表中的值或标签使用——不过这些用途都相当不常见！）。此外，这些名称还可以出现在模块开头的 EXPORTS 声明中。而在第一个例子中，诸如“tomorrow”这样的名称无法被导出，它们可以出现在其他区分值列表中，或者作为某种完全不同类型的值的值引用名称。在第一个例子中，“tomorrow”这个名称只有在以“My-integer”类型表示的值中才能被用作标识“My-integer”的零值。比如，当它被用作该类型序列元素的“默认值”时。

Notice also that although we have been using numbers in distinguished value lists in ascending order, there is no requirement for this - the order is irrelevant, and does not affect the resulting definitions. 请注意，虽然我们一直使用以升序排列的数值列表，但实际上并没有这样的要求——顺序并不重要，也不会影响最终的定义结果。

We have seen that a decimal number can be used as value-notation for a positive integer value. Negative values are, for example: 我们已经看到，十进制数可以用作正整数值的表示方式。例如，负数可以表示为：

```txt
minus-two INTEGER ::= -2 
```

but you are not allowed to write "-0", nor is any form of binary or hex notation valid as valuenotation for the “INTEGER” type. 但是，不允许使用“-0”来表示数值，任何形式的二进制或十六进制表示方式也不适用于“整数”类型的数值表示。

What are the set of abstract values for “INTEGER”? An early draft of the ASN.1 specification actually stated the maximum and minimum values of ASN.1 integers, based on restrictions imposed by BER encodings. However, a calculation showed that with a communications line running at a terabit a second, it would take approximately 100 million years to transmit the largest or smallest value! ASN.1 integers are "effectively unbounded". (And in the more recent PER encodings, there is no limit on the size of an integer value.) “INTEGER”这一抽象值的范围是多少？在 ASN.1 规范的早期版本中，确实规定了 ASN.1 整数的最大和最小值，这是基于 BER 编码所施加的限制。然而，经过计算后发现，如果通信线路的传输速度达到每秒一太比特，那么传输最大或最小值所需的时间将达到约 1 亿年！因此，ASN.1 中的整数“实际上是没有上限的”。而在更现代的 PER 编码中，整数值的大小则没有限制。

This raises the beginnings of a discussion that more properly belongs in a later chapter - do you really have to write your implementation code to handle arbitrarily large integers? If we look again at "no-of-days-reported-on" in Figure 13, we see the text "(1..56)" following the distinguished value list. (This can be present whether we have a distinguished value list or not). 这引发了一个值得在后续章节中详细讨论的问题：你是否真的需要编写代码来处理任意大的整数呢？如果我们再次看看图 13 中的“报告的天数”这一字段，会发现文本中包含了“(1..56)”这样的内容，无论是否有一个明确的数值列表。

This is our first example of a subtype constraint - a notation that restricts the range of our integer, or subsets it. In this case it is saying that the only values a conforming sender is permitted to send are values in the range 1 to 56, and it is clear that an implementor need only allocate one byte for this field. A fuller discussion of subtype notation (for other types as well as for the integer type) appears later, but this simple restriction of the range of an integer is by far the most common use of this notation. Application designers are encouraged to place a range constraint such as this on “INTEGER” types whenever they can do so, and to explicitly state in comment if they expect implementors to truly handle arbitrarily large integers. However, as an implementor, if you see simply "INTEGER", with no range constraint and no clarifying text, it is usually a safe assumption that a four-octet integer value will be the largest you will receive. 这是我们的第一个子类型约束示例——一种用于限制整数范围或子集范围的标记方式。在这个例子中，它规定符合要求的发送方只能发送 1 到 56 范围内的数值。显然，实现者只需为这个字段分配 1 个字节的空间即可。关于子类型标记的更多细节（包括其他类型以及整数类型的情况），我们将在后面讨论。不过，对整数范围进行如此简单的限制，无疑是这种标记方式最常见的应用场景。建议应用程序设计者在可能的情况下，为“INTEGER”类型添加类似的范围约束，并且如果实现者需要能够处理任意大的整数，则应在注释中明确说明这一点。不过，作为实现者，如果你只看到“INTEGER”这个类型，而没有范围限制或明确的说明，那么可以合理地假设，你所能获得的最大整数值应该是一个四个八位元的整数。

One final point: the similarity of the syntax for defining distinguished values to that for defining enumerations can be confusing. As the definition of distinguished values does not change in any way the set of abstract values in the type or the way they are encoded, there is never any "extensibility" question in moving to version 2 - if additional distinguished values are added, this is simply a notational convenience and does not affect the bits on the line. So the ellipsis extensibility marker (available for the list in the enumerated type), is neither needed nor allowed in the list of distinguished values (although it can appear in a range constraint, as we will see later). 最后一个要点：定义特殊值时的语法与定义枚举项时的语法相似，这可能会让人感到困惑。因为特殊值的定义本身并不改变，类型中的抽象值集合及其编码方式也不会发生变化。因此，在迁移到版本 2 时，根本不存在“扩展性”问题——如果添加了额外的特殊值，那仅仅是一种符号上的便利处理，并不会影响代码行的功能。所以，在特殊值列表中，不需要使用省略号来表示扩展性标记（这种标记在枚举类型中的列表中是可用的），同时也不允许使用这种标记。不过，这种标记可以在范围约束中出现，我们稍后会看到这一点。

## 2.3 The ENUMERATED type 2.3 ENUMERATED 类型

(See "urgency" in figure 13 and "reason-for-delay" in figure 22). There is little to add to our earlier discussions. The numbers in round brackets were required pre-1994, and are optional post-1994. The type consists precisely and only of values corresponding to each of the listed names. （参见图 13 中的“紧急程度”以及图 22 中的“延迟原因”部分）。关于这一点，我们之前已经讨论过很多了。在 1994 年之前，需要使用方括号中的数字来表示数据；而在 1994 年之后，这些数字则可以选择是否使用。该类型的数据仅包含与所列名称相对应的数值。

Numbers for encodings needed pre-1994, optional post-1994. 关于编码的编号需求，在 1994 年之前是有要求的，而 1994 年之后则可以选择不使用编号。

The numbers were originally present to avoid extensibility problems - if version 2 added a new enumeration, it was important that this should not affect the values used (in encodings) to denote original enumerations, and the easiest way to ensure this was to let the application designer list the numbers to be used. Post-1994, extensibility is more explicit, and we might see: 这些数字最初的存在是为了避免可扩展性问题——如果版本 2 增加了新的枚举类型，那么重要的是，这不应影响到用于表示原始枚举值的各种编码方式。而实现这一点的最简单方法就是让应用程序设计者可以自行选择要使用的数字。自 1994 年之后，可扩展性得到了更明确的体现，我们可能会看到这样的情况：

$$
\begin{array}{l} \text {Urgency - type : : = ENUMERATED} \\ \{\text {tomorrow}, \\ \text {three - day}, \\ \text {week}, \\ \dots , \\ \quad -- \text {Version 1 systems should assume any other value} \\ \quad -- \text {means "week".} \\ \text {month} \} \end{array}
$$

Here "month" was added in version 2, although the requirement placed on version 1 systems when version 1 was first specified actually means that such deployed systems will treat "month" as "week". This illustrates the importance of thinking hard about the exception handling you want from version 1 systems. If instead the version 1 spec had said "treat any unknown enumeration as tomorrow", then the effect of adding "month" in version 2 might have been less satisfying! Notice that in this case we chose to give the exception-handling behaviour in comment after the ellipsis, rather than using an exception specification - this is quite satisfactory, particularly if the exception handling is peculiar to this field. Selection of appropriate exception handling is discussed further in 2.6 of Chapter 7. 在版本 2 中增加了“月份”这个参数。不过，当定义版本 1 系统时，对系统所施加的要求实际上意味着，这样的系统会将“月份”视为“周”。这凸显了需要仔细考虑对版本 1 系统的异常处理机制的重要性。如果版本 1 的规范中明确规定“将任何未知枚举值视为明天”，那么版本 2 中增加“月份”这一参数的效果可能会不那么理想。注意，在这种情况下，我们选择将异常处理机制的描述放在注释中，而不是使用专门的异常处理规范——这种做法相当合理，尤其是当异常处理机制属于该领域特有的情况时。关于如何选择合适的异常处理机制，可以在第 7 章的 2.6 节中进一步了解。

Finally, if you want to be really weird, you can put numbers in for some enumerations and not for others. If you are lucky, the result will still be legal! Go and read the ASN.1 specification if you want to do daft things like that, this book will not help you! 最后，如果你真的想做一些很奇怪的事情，你可以为某些枚举项使用数字，而另一些则不用。如果运气好的话，结果仍然可能是合法的！如果你想做这种疯狂的事情，那就去阅读 ASN.1 规范吧。这本书可帮不了你哦！

## 2.4 The REAL type 2.4 真正的类型

(See "min-stock-level" etc in Figure 22). The type-notation for the “REAL” type is given in Figure 22. This is the only option. （请参见图 22 中的“min-stock-level”等描述）。“REAL”类型的类型标记在图 22 中有所说明。这是唯一可行的选项。

```txt
Real
Two sets of abstract values, Base 10 and Base 2, distinct even if mathematically equal. The value notation is a comma-separated list of integers for the mantissa, the base (2 or 10), and the exponent. Also PLUS-INFINITY and MINUS-INFINITY. 
```

The value notation is slightly curious. Here are examples of some pieces of value notation for the real type: 数值表示法有些特别，值得注意。以下是实数类型的一些数值表示法的例子：

```autohotkey
v1 REAL ::= {mantissa 314159, base 10, exponent -5}
v2 REAL ::= {mantissa 3141590, base 10, exponent -6}
v3 REAL ::= {mantissa 1, base 2, exponent -1}
v4 REAL ::= {mantissa 5, base 10, exponent -1}
v5 REAL ::= 0
v6 REAL ::= {mantissa 0, base 2, exponent 100}
v7 REAL ::= {mantissa 0, base 10, exponent 100} 
```

Notice that apart from v5, these are all comma-separated lists of three numbers. (Commaseparated lists occur frequently in ASN.1 value notation and were chosen for type REAL because an ASN.1 tool may encounter the value notation when the governor is a type-reference name that has not yet been defined, and the tool needs a simple means of finding the end of the notation). The mathematical value being identified by {x, y, z} is (x times (y to the power z)), but y is allowed to take only the values 2 and 10. 请注意，除了 v5 之外，这些全部都是由三个数字组成的逗号分隔的列表。这种逗号分隔列表在 ASN.1 值表示法中很常见，而选择这种类型是因为当类型引用名称尚未定义时，ASN.1 工具可能会遇到这种值表示法；此时工具需要一种简单的方法来找到该表示法的结尾。通过{x, y, z}表示的数学表达式是(x 乘以(y 的 z 次方))，不过 y 只能取 2 和 10 这两个值。

There are also explicitly included (and encoded specially) two values with the following value notation: 此外，还特别包含了两个数值，其表示方式如下：

```txt
PLUS-INFINITY
MINUS-INFINITY 
```

Again, all upper-case letters. When "REAL" was first introduced, there was discussion of adding additional special "values" such as "OVERFLOW", or even "PI" etc, but this never happened. 同样，所有的字母都是大写形式。在“REAL”这个概念首次被提出时，曾经讨论过添加一些额外的“值”，比如“OVERFLOW”，甚至是“PI”等等，但实际上并没有实现这一点。

That is really all you need to know, as the "REAL" type is infrequently used in actual application specifications. The rest of the discussion of the "REAL" type is a bit academic, and you can omit it without any “real” damage to your health! But if you want to know which of v1 to v7 represent the same abstract value and which different ones, read on! 实际上，你只需要知道这些就够了，因为“REAL”这个术语在实际的应用规范中很少被使用。关于“REAL”这个术语的其他讨论都相当学术性，你可以忽略它们，因为它们并不会对你的健康造成任何真正的危害！不过，如果你想知道从版本 1 到版本 7 究竟代表了哪些不同的抽象概念，那就继续阅读吧！

You might expect from the name that the abstract values are (mathematical) real numbers, but for those of a mathematical bent, only the rationals are included. 从名称来看，人们可能会认为这些抽象值都是数学上的实数。不过，对于喜欢数学的人来说，实际上只有有理数被包含在内。

Formally, the type contains two sets of abstract values, one set comprising all the numbers with a finite representation using base 10, and the other set comprising all the numbers with a finite representation base 2. (Notice that from a purely mathematical point of view, the latter values are a strict subset of the former, but the former contains values that are not in the latter set). In all ASN.1 encoding rules, there are binary encodings for "REAL", and there are also decimal encodings as specified in the ISO standard ISO 6093. This standard specifies a character string to represent the value, which is then encoded using ASCII. An example of these encodings is: 从形式上讲，这种类型包含两组抽象数值。一组包含所有可以用 10 进制表示的数值，另一组则包含所有可以用 2 进制表示的数值。（请注意，从纯数学的角度来看，后一组数值是前一组数值的严格子集，但实际上前一组数值中有些并不属于后一组数值。）在所有 ASN.1 编码规则中，对于“REAL”类型有二进制编码方式，同时也有按照 ISO 标准 ISO 6093 规定的十进制编码方式。该标准规定使用字符串来表示数值，然后利用 ASCII 编码进行编码。这种编码的一个例子是：

## but ISO 6093 contains many options! 不过，ISO 6093 标准包含了许多可选参数！

It is possible (post-1994) to restrict the set of abstract values in "REAL" to be only the base 10 or only the base 2 set, effectively giving the application designer control over whether the binary or the decimal encoding is to be used. Where the type is unrestricted, it is theoretically possible to put different application semantics on a base 10 value from that on the mathematically-equal base 2 value, but probably no-one would be daft enough! (Actually, "REAL" is not used much anyway in real protocols). 在 1994 年之后，可以限制“REAL”类型中的抽象值只采用十进制或二进制表示。这样，应用程序开发者就可以决定是使用二进制编码还是十进制编码。如果类型没有限制，理论上可以在十进制值上赋予与数学上相等的二进制值不同的应用语义，不过大概没人会这么做吧！（实际上，在实际的协议中，根本不会使用“REAL”这个类型。）

But just to wrap this discussion up ... looking at the values v1 to v7 above, we can observe that the value-reference-names listed on the same line below are value notation for the same abstract value, and those on different lines are names for different abstract values: 不过，为了结束这个讨论……观察上面列出的 v1 到 v7 这些值，我们可以发现，同一行中列出的值引用名称实际上指的是同一个抽象值；而不同行中的名称则指的是不同的抽象值。

```csv
v1, v2
v3
v4
v5, v6
v7 
```

(V5 equals V6 because V5 is defined to represent the base2 value zero.) （因为 V5 被定义为表示二进制值 0，所以 V5 实际上等于 V6。）

## 2.5 The BIT STRING type 2.5 二进制字符串类型

(See "version" in figure 22). There are two main uses of the bitstring type. The first is that given for "version", where we have a list of named bits associated with the type. The second and simplest is the type-notation: （参见图 22 中的“版本”部分）。这种位串类型主要有两种用途。第一种是作为“版本”的表示方式，即可以将一组具有名称的位与该类型关联起来。第二种也是最为简单的用途就是用于类型表示法：

<table><tbody><tr><td data-imt-p="1">BIT STRING is often used with named bits to support a bit-map for version negotiation. 位串通常用于与命名位一起使用，以支持版本协商所需的位图操作。</td></tr></tbody></table>

## BIT STRING 位串

Note that, as we would expect, this is all upper-case, but as we might not expect, the name of the type (effectively a type-reference-name) contains a space! The space is not merely permitted, it is required! Again ASN.1 breaks its own rules! 请注意，正如我们所预期的那样，这里的所有内容都使用了大写字母。不过，出乎我们的意料的是，类型名称（实际上是一个类型引用名称）中包含了一个空格！实际上，使用空格是被允许的，甚至是必须的！再次证明，ASN.1 确实打破了自身的规则！

We will return to figure 22 in a moment. Let us take the simpler case where there is no list of named bits. 我们稍后会回到图 22 的讲解。现在让我们考虑一个更简单的情况，即不存在名为各个位的列表。

If a field of a sequence (say) is defined as simply "BIT STRING", then this can be a sign of an inadequately-specified protocol, as semantics need to be applied to any field in a protocol. "BIT STRING" with no further explanation is one of several ways in which "holes" can legally be left in ASN.1 specifications, but to the detriment of the specification as a whole. 如果某个序列的字段被简单地定义为“BIT STRING”，那么这可能表明该协议的描述不够详尽。因为对于任何协议中的字段来说，都需要有明确的语义描述。“BIT STRING”这种表述本身就是一个例子，它属于 ASN.1 规范中允许存在的“漏洞”之一——不过，这样做会整体性地削弱规范的完整性。

We will see later that where any "hole" is left, it is important to provide fields that will clearly identify the content of the hole in an instance of communication, and to either ensure that all communicating partners will understand all identifications (and the resulting contents of the hole), or will know what action to take on an unknown identifier. ASN.1 makes provision for such "holes" and the associated identification, and it is not a good idea to use "BIT STRING" to grow your own "holes" (but some people do)! 我们稍后会看到，当存在“空洞”时，就需要提供能够明确标识该空洞中内容的字段。这样既能确保所有通信方都能理解这些标识内容，也能让他们知道如何处理未知的标识符。ASN.1 规范为这类“空洞”及其相关标识提供了支持。因此，使用“位串”来制造自己的“空洞”并不是一个好主意（不过，有些人确实这么做了）！

So ... BIT STRING without named bits has a legitimate use to carry encodings produced by wellidentified algorithms, and in particular to carry encryptions for either concealment or signature purposes. But even in this case, there is usually a need to clearly identify the security algorithm to be 因此，没有命名位的位串在某种情况下可以用于承载由特定算法产生的编码，尤其是用于加密目的，以实现隐蔽或签名功能。不过，即便在这种情况下，通常仍然需要明确说明所使用的加密算法。

<table><tbody><tr><td data-imt-p="1">BIT STRING without named bits is also frequently used as part or a more complex structure to carry encrypted information. 不包含命名位的位串也被经常用作存储加密信息的一种方式，或者作为更复杂结构的一部分来承载加密数据。</td></tr></tbody></table>

applied, and perhaps to indirectly reference specific keys that are in use. The BIT STRING data type is (legitimately) an important building block for those providing security enhancements to protocols, but further data is usually carried with it. 该数据类型具有实用性，或许还能间接指向某些正在被使用的密钥。BIT STRING 数据类型确实是为那些为协议提供安全增强功能的开发者而设计的非常重要的基础组件；通常，该数据类型还会携带其他数据。

The use of BIT STRING with named bits as for "version" in figure 13 is common. The names in curly brackets simply provide names for the bits of the bit-string and the associated bit-number. It is important to note that the presence of a named bit list (as with distinguished values for integers), does not affect the type. The list in no way constrains the possible length of the bit-string, nor do bits have to be named in order. 在图 13 中，使用带有名称的位串作为“版本”表示方式是很常见的。括号中的名称只是为位串中的各个位以及相应的位数提供了标识。需要注意的是，虽然存在名为位列表的结构（就像整数中的不同值一样），但这并不会影响位串的类型。该列表并不会限制位串的可能长度，而且位也不必一定要有名称。

ASN.1 talks about "the leading bit" as "bit zero", down to the "trailing bit". Encoding rules map the "leading bit" to the "trailing bit" of a bit-string type into octets when encoding. 在 ASN.1 标准中，将“前导位”称为“位零”，而“尾位”则被称为“后导位”。在编码过程中，会将“前导位”与位串中的“尾位”对应起来，并分别转换为八位元数据。

(BER - arbitrarily, it could have chosen the opposite rule - specifies that the leading bit be placed in the most significant bit of the first octet of the encoding, and so on.) （BER——可以任意选择相反的规则；例如，可以规定将主导位放置在编码的第一个八位组的最高有效位上，以此类推。）

How are these names of bits used? As usual, they can provide a handle for reference to specific bits by the human-readable text. They can also, however, be used in the value notation. 这些位名是如何被使用的呢？通常，它们可以通过人类可读的文本来指代特定的位。不过，这些名称也可以用于数值表示中。

The obvious (and simplest) value notation for a bitstring is to specify the value in binary, for example: 对于位串来说，最直观（也是最简单）的价值表示方式就是用二进制来表示其值，例如：

## '101100110001'B ‘101100110001’B

If the value is a multiple of four bits, it is also permissible to use hexadecimal: 如果该值至少是 4 位数的倍数，那么也可以使用十六进制表示：

$$
^ \prime \mathrm{B31} ^ {\prime} \mathrm{H}
$$

(Note that in ASN.1 hexadecimal notation, only upper case letters are allowed.) （请注意，在 ASN.1 的十六进制表示法中，只允许使用大写字母。）

If, however, there are named bits available, then an additional value notation is available which is a comma-separated list of bit-names within curly brackets (see, for example, the “DEFAULT” value of “version” in figure 22). The value being defined is one in which the bit for every listed bit-name is set to one, and all other bits are set to zero. 不过，如果还有名为特定位数的位可用，那么可以使用一种额外的数值表示方式。这种表示方式是将位名称用逗号分隔，放在大括号之间（例如，可以在图 22 中看到“version”这一值的设定）。所定义的值意味着，所有列出的位名称对应的位都被设置为 1，而其他所有位则被设置为 0。

The alert reader (I have done it again!) will spot that this statement is not sufficient to define a bitstring value, as it leaves undetermined how many (if any) trailing zero bits are present in the value. So the use of such a "value-notation" if the length of the bitstring is not constrained does not really define a value at all - it defines a set of values! All those with the same one bits, but zero to infinity trailing zero bits! 敏锐的读者会注意到，这样的表述并不足以定义一个位串值，因为它没有明确说明该位串中究竟有多少个（如果有的话）末尾是零的位。因此，如果位串的长度没有限制，那么这种“值表示法”实际上并不能定义一个具体的数值——它只是定义了一组数值而已！所有那些具有相同一个位，但末尾有零位到无限多个零位的位串，都属于这一组数值。

The ASN.1 specifications post around 1986 get round this problem with some weasel words (slightly changed in different versions): "If a named bit list is present, trailing zero bits shall have no semantic significance"; augmented later by "encoding rules are free to add (or remove) trailing zero bits to (or from) values that are being encoded"! 大约在 1986 年左右，ASN.1 规范通过一些模糊的措辞解决了这个问题（在不同版本中有些细节有所调整）：“如果存在一个名为位列表，那么末尾的零位将不具有任何语义意义”；后来又补充了“编码规则可以自由地为被编码的值添加或删除末尾的零位”这一条款。

<table><tbody><tr><td data-imt-p="1">BIT STRING with named bits raises interesting issues about what is the precise set of abstract values of such a type: 包含命名位的位串会引出一些有趣的问题：这类类型的抽象值究竟是什么？</td></tr><tr><td data-imt-p="1">IGNORE SUCH QUESTIONS, they don't matter! 忽略这些问题吧，它们并不重要！</td></tr></tbody></table>

This issue is not a big one for normal BER, where it does not matter if there is doubt over whether some value exactly matches the "DEFAULT" value, but it matters rather more in the canonical encoding rules described later. 对于普通的 BER 来说，这个问题并不重要，因为是否某个数值与“默认”值完全匹配并不重要。但在后面描述的规范编码规则中，这个问题就变得比较重要了。

The most common use for named bits is as a "version" map, as illustrated in figure 13. Here an implementation would be instructed to set the bits corresponding to the versions that it is capable of supporting, and - typically - there would be some reply message in which the receiver would set precisely one bit (one of those set in the original message), or would send some sort of rejection message. 命名位最常见的用途是作为“版本”标识，如图 13 所示。在这种情况下，系统会被指示设置与其所支持的版本相对应的位。通常，会有一个回复消息，接收方会精确设置其中一个位（即原始消息中设置的那个位），或者发送某种拒绝消息。

## Formal/advanced discussion 正式/高级讨论

NOTE — Most readers should skip this next bit! Go on to OCTET STRING, that has fewer problems! If you insist on reading on, please read figure 999 again! 注意：大多数读者无需阅读接下来的内容！继续阅读关于 OCTET STRING 的部分吧，那里的问题相对较少。如果你还是坚持要继续阅读，请再次阅读图 999 吧！

There have been many different texts in the ASN.1 specifications over the last 15 years associated with “BIT STRING” definitions with named bits. Most have been constrained by the desire: 在 ASN.1 规范中，过去 15 年里出现了许多与“位串”定义相关的不同文本。这些文本都受到了某种限制，其目的都是为了满足特定的需求。

a) not to really change what was being specified, or at least, not to break current deployed implementations; and a) 不要真正改变原有的规定，或者至少，不要破坏当前已部署的实现方式；而且……

b) not to add a large amount of text that would seem to imply a) above even if it didn't really do it! b) 不要添加大量似乎暗示了上述内容的文本，即使实际上并没有这样的含义！

The result is that you as an alert and intelligent reader(!) may well be able to take issue with what follows, depending on the vintage of the specification that you are reading, and/or on whether people insist on calling you an "ASN.1 Expert"! 因此，作为一位敏锐且聪明的读者，你可能会对以下内容产生质疑。这种质疑取决于你阅读到的规范版本，以及人们是否坚持称你为“ASN.1 专家”！

The ASN.1 Standard seems to imply that the presence of a named bit list (and the extent of such a list) has no impact on the set of abstract values in the type being defined. However, abstract values are there to enable application designers to associate different application semantics with them, with the assurance that each value will have a distinct encoding, and with the equal assurance that for canonical encodings there will be precisely one encoding for each value. ASN.1 标准似乎认为，某个命名位列表的存在（以及该列表的详细程度）并不会影响所定义类型的抽象值集。不过，这些抽象值的存在是为了让应用程序设计者能够将其与不同的应用语义关联起来。同时，每个值都会有一个独特的编码方式，而且对于规范编码来说，每个值都只有一种编码方式。

(Controversial remark follows!) The specification states that "application designers should ensure that different (application) semantics are not associated with ... values (of types with named bits) which differ only in the number of trailing zero bits". What this is actually saying is that such apparently distinct abstract values are actually a single abstract value. （接下来是颇具争议的评论！）规范中提到：“应用程序设计者应确保，不同的应用程序语义不会与那些仅在尾随零位数量上有所不同的值相关联。”实际上，这意味着这些看似不同的抽象值其实是一种抽象值而已。

The only remaining issue is how such abstract bitstring values should be represented by encoding rules. The standard gives guidance: "encoding rules are free to add (or remove) arbitrarily many trailing zero bits to (or from) values that are being encoded or decoded". Perhaps not the best way of expressing it, but the principles are clear: 目前唯一的问题在于，如何通过编码规则来表示这些抽象的比特串值。标准规定：“在编码或解码过程中，可以任意增加或减少末尾的零比特。”或许这不是最直观的表达方式，但原理很清楚：

when a named bit list is present, we have just one abstract value corresponding to different bit-patterns that differ only in the number of their trailing zero bits; 当存在名为“位列表”的数据时，我们其实只有一个抽象值，这个值对应于各种不同的位模式，这些位模式的区别仅在于其末尾零位的数量；

• encoding rules are (of course!) free to represent this abstract value how they like, but one option is to encode any one of those bit-patterns that differ only in their trailing zero bits. • 当然，编码规则可以随心所欲地来表示这个抽象值。不过，其中一种方法是将那些仅在末尾有零位的位模式进行编码。

For BER, which does not claim to provide a single encoding for each abstract value, the rules permit arbitrarily many trailing zero bits in the encoding. (The decision to allow this was necessary to avoid breaking existing implementations when this rather abstract(!) problem was first understood.) Existing BER implementations will frequently include trailing zero bits in the encoding of a value of a bitstring type with a named-bit list. 对于 BER 来说，由于它并不要求为每个抽象值提供唯一的编码方式，因此规则允许在编码中包含任意多的末尾零位。（允许这种做法是必要的，这样可以避免在新发现这个较为抽象的问题时破坏现有的实现。）现有的 BER 实现通常会在一个包含命名位列表的位串类型的值的编码中包含末尾零位。

For canonical encoding rules, however, including PER, a single encoding is necessary, and at first sight saying that such encoding rules never have trailing bits in the encoding looks like a good solution. 不过，对于规范编码规则来说，包括 PER 在内，只需要一种编码方式即可。乍一看，认为这种编码方式在编码过程中不会包含末尾的位，似乎是个不错的解决方案。

But the choice of encoding (and indeed the selection of the precise abstract bitstring value - from the set of abstract values with the same semantics - that is to be used for encoding) is complicated if there are length constraints at the abstract level on the bitstring type. 但是，当在抽象层面对比特串类型有长度限制时，选择编码方式（以及从具有相同语义的抽象值集中确定用于编码的具体比特串值）就会变得非常复杂。

The matter is further complicated because in BER-related encoding rules, length constraints are "not visible" - do not affect the encoding! In PER, they may or may not be visible! 这个问题更加复杂了，因为在与 BER 相关的编码规则中，长度限制是“不可见的”——也就是说，它们不会影响编码过程。而在 PER 中，长度限制可能是可见的，也可能不可见。

The up-shot of all this is that in the canonical versions of BER trailing zero bits are never transmitted in an encoding, but the value delivered to the application is required to have sufficient zero bits added (the minimum necessary) to enable it to satisfy any length constraints that might have been applied. (Such constraints are assumed to be visible to the application and to the Application Program Interface -API- code, whether they are visible to - affect - the encoding rules or not.) 这一切的积极效果是，在标准的 BER 编码中，不会传输多余的零位比特。而是会将一个足够多的零位比特添加到传递给应用程序的值中（至少达到最低要求），以便能够满足可能存在的任何长度限制。这些限制假定是明确可见的，无论是对于应用程序还是应用程序编程接口（API）代码来说都是如此——无论这些限制是否会影响编码规则。

PER, where (some) length constraints are PER-visible, changes this slightly: what is transmitted is always consistent with PER-visible constraints - so (the minimum number of) trailing zero bits are present in transfer if they are needed to satisfy a length constraint. The encoding can thus be delivered to the application unchanged, provided there are no not-PER-visible constraints applied, otherwise the canonical BER rules would apply - the application gets a value that is permitted by the constraints and carries the same application semantics as that derived directly from the transmitted encoding. PER 的 경우，当存在某些长度限制时，传输的数据会稍微有所调整：传输的数据始终符合 PER 可见性的限制——因此，如果为了满足长度限制而需要的话，传输数据中会包含尽可能多的尾随零位。这样，只要没有非 PER 可见性的限制，编码内容就可以原样传递给应用程序；否则，就会适用标准的 BER 规则——应用程序接收到的数据将是符合约束条件的有效数据，其语义与直接从传输编码中得到的数据相同。

And if you have read this far, I bet you wish you hadn't! It kind of all works, but it is not simple! 如果你已经读到了这里，我猜你一定希望自己当初没有开始读下去吧！虽然这一切看起来还算可行，但实际上并不容易！

Issues like this do not affect the normal application designer - just do the obvious things and it will all work, nor do they affect the normal implementor that obeys the well-known rules: encode the obvious encoding; be liberal in your decoding. 这类问题并不会影响到普通的应用程序设计者——只要按照常规的做法来操作，一切都会正常运行。同样，这些问题也不会影响到那些遵守常见规则的普通实施者：对明显需要编码的数据进行编码处理；在解码时保持灵活性即可。

These issues are, however, of importance to tool vendors that provide an option for "strict diagnostics" if incoming material is perceived to be erroneous. In such cases a very precise statement of what is "erroneous" is required! 不过，这些问题对于那些提供“严格诊断”功能的工具供应商来说非常重要。因为如果检测到传入的物料存在错误，那么就需要有一个非常精确的说明来界定什么是“错误”！

## 2.6 The OCTET STRING type 2.6 OCTET STRING 类型

(See "bar-code-data" in figure 22). Once again, a space is needed between "OCTET" and "STRING"! And once again, an octetstring is a tempting candidate to "carry anything" - a delimited hole. (But don't be tempted!) Yet again, it is not appropriate unless supported by identification fields and exception handling. ASN.1 provides better （请参考图 22 中的“条形码数据”部分）。同样，在“OCTET”和“STRING”之间需要有一个空格！而这次，一个八位组字符串确实是一个很有吸引力的“携带任何数据”的候选者——一个具有明确边界的数据单元。不过，不要被这种诱惑所迷惑！除非有相应的标识字段和异常处理机制作为支持，否则这样做是不合适的。ASN.1 提供了更好的解决方案。

The OCTET STRING type is simple - but don't use it! It usually represents a poorly-supported "hole", and it is better to use a pre-fabricated "hole" - see later! OCTET STRING 类型很简单——但千万不要使用它！它通常代表着一种支持不足的“空缺”状态，因此最好使用预先构建好的“空缺”表示方式——稍后会有详细说明！

mechanisms to support "holes". 支持“漏洞”的机制。

In the case shown in figure 22, the precise contents of the octet string are (hopefully!) wellspecified in “chapter 29 of the wineco manual”. However, this specification is not very general. The intent is clearly to provide a container for additional identification information, using some encoding outside of ASN.1. In general, and over time, there may be a number of different encodings of various forms of identification that the designer may wish to carry in this octetstring, and again we see the need for additional identification fields saying "this is a bar-code version 1" - or something else, and "this is how it is encoded today", rather than hard-wiring these decisions into "chapter 29". Once again, we see we are discussing "holes". 在图 22 中所示的情况下，那个八位元字符串的确切内容（希望如此！）在“wineco 手册的第 29 章”中有明确的规定。不过，这个规范并不十分通用。显然，其目的是通过使用一些超出 ASN.1 标准的编码方式，来为额外的识别信息提供一个容器。一般来说，随着时间的推移，设计者可能会希望在这个八位元字符串中包含多种形式的识别信息。因此，我们需要额外的识别字段来说明“这是条形码版本 1”之类的信息，或者说明“目前这种编码方式是如何使用的”。而不是将这些决策硬编码到“第 29 章”中。再次，我们看到这里存在“空白”之处。

In summary (but see Figure 999 again!) it is probably a BAD THING to have OCTET STRING or BIT STRING (other than for version bit-maps) fields in application specifications unless you really know what you are doing and really want to "dig your own hole". But of course, perhaps you do! 总结来说（不过还是请参考图 999！），在应用规格中包含 OCTET STRING 或 BIT STRING 字段可能是一件坏事——除非你真的明白自己在做什么，并且愿意承担由此带来的风险。不过，当然，也许你确实愿意这么做吧！

The value notation for OCTET STRING is always hexadecimal or binary as illustrated earlier for bitstring. If the result is not an integral multiple of eight bits, then zero bits are added at the end. OCTET STRING 的值表示方式始终采用十六进制或二进制格式，就像之前提到的 BITSTRING 一样。如果结果不是 8 位整数的倍数，那么会在末尾添加 0 位。

## 2.7 The NULL type 2.7 空类型

(See "warehouse" in figure 13). Formally, NULL is a type that has just one value. The value-notation for this value is rather confusingly: （参见图 13 中的“仓库”部分）。从形式上讲，NULL 是一种只有一种值的类型。这种值的表示方式相当令人困惑：

For NULL, you know it all - a place-holder: no problems. 对于 NULL 来说，你完全不需要担心——它只是一个占位符而已，没有任何问题。

## NULL 空

again, all upper-case, where one might expect an initial lower-case letter. 同样，所有的字母都是大写的，而人们通常会期望开头的字母是小写的。

The normal use is very much as in figure 13 - where we need a type to provide a TLV (whose presence or absence carries some semantics), but where there is no additional information to be carried with the type. NULL is often referred to as a "place-holder" in ASN.1 courses. 正常使用情况与图 13 中的描述非常相似——我们需要一个类型来提供 TLV 信息（该信息的存在或缺失具有一定的语义意义），但类型本身并不包含其他额外的信息。在 ASN1 教程中，NULL 通常被称为“占位符”。

## 2.8 Some character string types 2.8 一些字符串类型

(See "additional-information" in figure 22 and "name" (twice) in figure 13). In the examples so far, you have met "PrintableString" (present in the earliest ASN.1 drafts), "VisibleString" (deprecated synonym "ISO646String"), and "UTF8String" (added in 1998). There are several others. （请参阅图 22 中的“附加信息”部分，以及图 13 中的“名称”部分）。在迄今为止的示例中，你已经见过“PrintableString”（出现在最早的 ASN.1 草案中）、“VisibleString”（已被弃用的同义词“ISO646String”），以及“UTF8String”（于 1998 年新增的类型）。此外还有几种其他类型。

Despite not being all-upper-case, these (and the other character string type names) have been reserved words (names you may not use for your own types) since about 1988/90. The early designers of ASN.1 felt (rightly!) that the character string types and their names were a bit "ad hoc", and gave them a somewhat reduced status! 虽然这些词汇并不是完全属于“顶级词汇”，但自 1988/90 年左右起，它们就被列为保留词汇了（即那些不能被用来定义自定义类型的词汇）。ASN.1 的早期设计者认为，字符串类型及其名称有些“随意”的性质，因此将它们赋予了相对较低的优先级。不过，这种做法其实也是合理的。

Actually, in the earliest ASN.1 specification, there was the concept of "Useful Types", that is, types that were defined using the ASN.1 notation rather than pure human-language, and these all used mixed upper/lower-case. The character string types were originally included as "Useful types", and were defined as a tagged OCTET STRING. Today (since about 1990 when they became reserved words) they are regarded as fairly fundamental types with a status more-or-less equal to that of INTEGER or BOOLEAN. 实际上，在最早的 ASN.1 规范中，存在“有用类型”的概念。这些类型是用 ASN.1 标记法定义的，而不是用纯人类语言描述的。这些类型的命名方式同时使用大小写字母。字符串类型最初也被归类为“有用类型”，并被定义为带有标签的 OCTET STRING 类型。如今（自 1990 年左右这些关键字被限制使用以来），字符串类型被视为相当基础的类型，其地位大致与 INTEGER 或 BOOLEAN 类型相当。

The set of characters in "PrintableString" values is "hard-wired" into ASN.1, and is roughly the old telex character set, plus lower-case letters. The BER encoding in the "V" part of the TLV is the ASCII encoding, so the reduced character set over "VisibleString" (following) is not really useful, although a number of application specifications do use "PrintableString". “PrintableString”中定义的字符集是硬编码在 ASN.1 中的，大致相当于旧的电报字符集，再加上小写字母。TLV 中“V”部分使用的 BER 编码就是 ASCII 编码。因此，相比“VisibleString”来说，这种缩小的字符集其实并没有太大用处，不过有一些应用规范确实使用了“PrintableString”字符集。

The set of characters in "VisibleString" values is simply the printing ASCII characters plus "space". The BER encoding in the "V" part of the TLV is, of course, ASCII. “VisibleString”中字符集仅包含用于打印的 ASCII 字符，再加上“空格”字符。在 TLV 文件的“V”部分所采用的 BER 编码方式，本质上就是 ASCII 编码。

The set of characters in "UTF8String" is any character - from Egyptian hieroglyphs to things carved in wood in the deepest Amazon jungle to things that we will in due course find on Mars - that has been properly researched and documented (including the ASCII control characters). The BER (and PER if the type is not constrained to a reduced character set) encoding per character is variable length, and has the "nice" property that for ASCII characters the encoding per character is one octet, stretching to three octets for all characters researched and documented so far, and going to at most six octets per character once we have all the languages of the galaxy in there! Those who are "into" character set stuff may recognise the name "Unicode". UTF8 is an encoding scheme covering the whole of Unicode (and more) that is becoming (circa 1999) extremely popular for communication and storage of character information. Advice: If you are designing a new protocol, use UTF8String for your character string fields unless you have a very good reason not to do so. “UTF8String”中的字符集包含了所有能够被识别的字符——从埃及象形文字到亚马逊丛林中雕刻在木头上的符号，再到我们未来可能在火星上发现的字符。这些字符都经过了充分的研究和记录，包括 ASCII 控制字符在内。每个字符的编码采用 BER 编码方式（如果类型不受有限字符集的限制，也可以使用 PER 编码方式）。这种编码方式是可变长度的，而且有一个优点：对于 ASCII 字符来说，每个字符只需要一个八位元即可表示；而对于所有已被研究和记录的字符，每个字符的编码最多可达三个八位元。一旦包含了银河系中的所有语言字符，每个字符的编码长度则最多可达六个八位元。那些熟悉字符集相关概念的人可能会认出“Unicode”这个名称。UTF8 是一种覆盖整个 Unicode 范围的编码方案，自 1999 年以来，它变得越来越流行，被广泛用于字符信息的传输和存储。建议：如果您正在设计一种新的协议，请使用 UTF8String 来表示字符字符串字段，除非您有非常充分的理由不这样做。

## 2.9 The OBJECT IDENTIFIER type 2.9 对象标识符类型

(See "item" and "wineco-items" in figure 22, and module identifiers in figure 21.) Values of the object identifier type have been used and introduced from the start of this book. But we are still going to postpone to a later chapter a detailed discussion of this type! （请参阅图 22 中的“物品”和“wineco-物品”部分，以及图 21 中的模块标识符。本书从一开始就已经使用了对象标识符类型，并且一直沿用至今。不过，关于这种类型的详细讨论，我们还是将推迟到后面的章节中再进行讨论吧！）

OBJECT IDENTIFIER perhaps more used than any other basic ASN.1 type - you can get some name-space in lots of ways, but you don't really need it! 对象标识符可能是其他基本 ASN 类型中使用最广泛的类型——你可以以多种方式来指定名称空间，但实际上并不需要使用它。

The OBJECT IDENTIFIER type may well lay claim to being the most used of all the ASN.1 types (excluding the constructors SEQUENCE, SET, and CHOICE, of course). Wherever world-wide unambiguous identification is needed in an ASN.1- based specification, the object identifier type is used. 对象标识符类型可能是所有 ASN.1 类型中使用最广泛的类型（当然，不包括序列、集合和选择这些类型）。在基于 ASN.1 的规范中，当需要全球范围内唯一标识某个对象时，就会使用对象标识符类型。

Despite the apparent verbosity of the value-notation, the encoding of values of type object identifier is actually very compact (the human-readable names present in the value notation do not appear in the encoding). For the early components of an object identifier value, the mapping of names to integer values is "well-known", and for later components in any value-notation, the corresponding integer value is present (usually in round brackets). 尽管对象标识符的值表示方式看起来相当冗长，但实际上这种值的编码方式其实非常简洁（在值表示方式中出现的、人类可读的名称在编码中并不会出现）。对于对象标识符值的早期组成部分，名称与整数值的对应关系已经广为人知；而对于任何值表示方式中的后续组成部分，相应的整数值则通常位于圆括号之中。

The basic name-space is a hierarchically allocated tree-structure, with global authorities responsible for allocation of top-level arcs, and progressively more local authorities responsible for the lower-level arcs. 基本命名空间是一个分层分配的树形结构。顶层弧的分配由全局性权限负责，而较低级别的弧的分配则由更具体的权限负责。

For you (as an application designer) to be able to allocate values from the object identifier name space, you merely need to "get hung" from this tree. It really doesn't matter where you are "hung" from (although encodings of your values will be shorter the nearer you are to the top, and international organizations tend to be sensitive about where they are "hung"!). 对于你这样的应用程序设计师来说，要能够从对象标识符的命名空间中分配值，只需从这个树状结构中“获取”它们即可。实际上，你“获取”这些值的位置并不重要（不过，越靠近树顶，值的表示方式就越简洁；而且，一些国际组织对于值的“获取位置”比较敏感！）。

For a standards-making group, or a private company, or even an individual, there are a range of mechanisms for getting some of this name-space, most of which require no administrative effort (you probably have an allocation already!). These mechanisms are described later, although such is the proliferation of branches of the OID tree (as it is often described) that it is hard to describe all the finer parts! 对于制定标准的组织、私人公司，甚至是个人来说，都有多种方式来获取这部分命名空间。其中大多数方式都不需要任何管理上的努力（很可能你已经获得了相应的命名权限！）。这些机制将在后面详细描述，不过，由于 OID 树的分支数量不断增加，要全面介绍所有细节其实是非常困难的。

It has been a criticism of ASN.1 that you need to get some OID space to be able to authoritatively write ASN.1 modules. This is actually not true - the module identifier is not required. However, most people producing ASN.1 modules do (successfully) try to get a piece of the OID space and do identify their modules with OID values. But if this provides you with problems, it is not a requirement. 一直以来，人们都批评 ASN.1 标准：要想能够权威地编写 ASN.1 模块，就需要获得一些 OID 空间。但实际上这种情况并不存在——编写模块标识符并不是必须的。不过，大多数编写 ASN.1 模块的人都会尝试获得一些 OID 空间中的资源，并使用 OID 值来标识他们的模块。不过，如果这样做确实带来了问题，那也并不属于该标准的强制要求。

## 2.10 The ObjectDescriptor type 2.10 对象描述器类型

(See "item-description" in figure 22). The typenotation for the ObjectDescriptor type is: （请参见图 22 中的“项目描述”部分）。ObjectDescriptor 类型的类型标注为：

## ObjectDescriptor 对象描述符

without a space, and using mixed upper and lower case! This is largely a historical accident. This type was formally-defined as a tagged 不使用空格，并且统一使用大小写字母！这主要是一种历史性的偶然现象。这种类型最初是被正式定义出来的。

## ObjectDescriptor 对象描述符

Yes, mixed case! You will never see it in a specification, and you are unlikely to want to use it - ignore this text! 是的，这是一款混合类型的案例！你在规格说明中永远不会看到它的相关信息，而且你也不太可能想要使用它——所以无需理会这段描述吧！

"GraphicString" (another character string type capable of carrying most of the world's languages, but regarded as obsolete today). Because its definition was by an ASN.1 type-assignment statement, it was deemed originally to be merely a "Useful Type", and was given a mixed upper/lower-case name with no space. Today, the term "Useful Type" is not used in the ASN.1 specification, and the use of mixed case for this built-in type is a bit of an anachronism. “GraphicString”是一种字符字符串类型，能够承载世界上大多数语言的内容。不过，如今这种类型被认为已经过时了。由于它的定义是通过 ASN.1 类型声明来确定的，因此最初它只被视作一种“实用类型”。当时，这种类型被赋予了大小写混合的命名方式，且没有使用空格。如今，ASN.1 规范中已不再使用“实用类型”这一术语，而且这种内置类型使用大小写混合命名方式也显得有些过时了。

The existence of the type stems from arguments over the form of the OBJECT IDENTIFIER type. There were those who (successfully) argued for an identification mechanism that produced short, numerical, identifiers when encoded on the line. There were others who argued (unsuccessfully) for an identification mechanism that was "human-friendly", and contained a lot of text (for example, something like a simple ASCII encoding of the value notation we have met earlier), and perhaps no numbers. As the debate developed, a sort of compromise was reached which involved the introduction of the "OBJECT IDENTIFIER" type - short, numerical, guaranteed to be worldwide unambiguous, but supplemented by an additional type "ObjectDescriptor" that provided an indefinitely long (but usually around 80 characters) string of characters plus space to "describe" an object. The "ObjectDescriptor" value is not in any way guaranteed to be world-wide unambiguous (the string is arbitrarily chosen by each designer wishing to describe an object), but because of the length of the string, usually it is unambiguous. 这种类型的存在源于关于 OBJECT IDENTIFIER 类型形式的争论。有些人主张使用一种能够在行中生成简短数字标识符的标识机制，这种机制在编码时不会产生歧义。而另一些人则主张使用一种“易于人类理解”的标识机制，该机制包含大量文本信息（例如，类似于我们之前遇到的数值表示的简单 ASCII 编码），并且可能不包含数字。随着争论的深入，人们最终达成了一项妥协方案，即引入“OBJECT IDENTIFIER”类型——这种类型简洁、数字化，且保证在全球范围内具有唯一性。同时，还增加了“ObjectDescriptor”类型，它提供了一个无限长的字符序列，通常约为 80 个字符，用于“描述”一个对象。“ObjectDescriptor”的值并不保证在全球范围内具有唯一性。“字符串”是由每个想要描述某个对象的设计师任意选择的，但由于字符串的长度问题，通常来说这种描述是明确的。

There is a strong recommendation in the ASN.1 specification that whenever an object identifier value is allocated to identify an object, an object descriptor value should also be allocated to describe it. It is then left for application designers to include in their protocol (when referring to some object) either an "OBJECT IDENTIFIER" element only, or both an "OBJECT IDENTIFIER" and an "ObjectDescriptor", perhaps making the inclusion of the latter "OPTIONAL". 在 ASN.1 规范中有一项重要的建议：每当为某个对象分配一个对象标识符时，同时也应该分配一个对象描述符来对其进行描述。接下来就由应用程序设计者在他们的协议中（在提及某个对象时），选择仅包含“OBJECT IDENTIFIER”元素，或者同时包含“OBJECT IDENTIFIER”和“ObjectDescriptor”元素。当然，后者也可以作为可选内容包含进来。

In practice (apart from the artificial example of figure 22!) you will never encounter an "ObjectDescriptor" in an application specification! Designers have chosen not to use it. Moreover, the rule that whenever an object identifier value is allocated for some object, there should also be an object descriptor value assigned, is frequently broken. 在实践中（除了图 22 这样的虚构例子之外），你永远不会在应用程序规范中看到“对象描述符”这一术语！设计师们选择不使用它。此外，通常的规则是：每当某个对象被赋予一个对象标识符时，也应该同时赋予一个对象描述符。但实际上，这一规则经常被违反。

Take the most visible use of object identifier values - in the header of an ASN.1 module: what is the corresponding object descriptor value? It is not explicitly stated, but most people would say that the module name appearing immediately before the object identifier in the header forms the corresponding object descriptor. Well - OK! 在 ASN.1 模块的头部，对象标识符值有着最为明显的应用。那么，对应的对象描述符值是什么呢？虽然并没有明确说明，但大多数人会认为，在头部中位于对象标识符之前的模块名称，就构成了对应的对象描述符。嗯——好吧！

But there are other object identifier values originally assigned in the ASN.1 specification itself, such as: 不过，在 ASN.1 规范中，还有其他一些原本就分配好的对象标识符值，例如：

```txt
{iso standard 8571} 
```

This identifies the numbered standard (which is actually a multi-part standard), and also gives object identifier name-space to those responsible for that standard. There is, however, no corresponding object descriptor value assigned! 这标识了该编号标准的名称（实际上这是一个多部分的标准），同时也为负责该标准的人提供了对象标识符命名空间。不过，目前还没有分配相应的对象描述符值！

## 2.11 The two ASN.1 date/time types 2.11 两种 ASN.1 日期/时间类型

Yes, you did indeed interpret figure 22 correctly - UTCTime is a date/time type that carries only a twodigit year! 是的，您确实正确地理解了图 22 的含义——UTCTime 是一种日期/时间类型的数据结构，它只包含一个两位数的年份。

You will also notice that both "UTCTime" and "GeneralizedTime" are again mixed upper/lower- 你还会注意到，这里的“UTCTime”和“GeneralizedTime”这两个字段再次使用了上下半天的表示方式。

UTCTime and GeneralizedTime UTCTime 和 GeneralizedTime

Simple in concept, easy to use, but not without their problems! 这个概念很简单，使用起来也很方便，不过也并非毫无问题！

case. Again this is a historical accident: they were defined using an ASN.1 type-assignment statement as a tagged "VisibleString", and were originally listed as "Useful Types". 这又是一个历史性的偶然事件：这些类型是通过 ASN.1 类型分配语句来定义的，被标记为“VisibleString”类型，并且最初被列在“有用的类型”选项中。

Why both? Was GeneralizedTime added later? Yes and no! In the early drafts in 1982, UTCTime was all that was present, and contained the specification of the character string to be used to represent dates and times "hard-wired" into the ASN.1 specification: that is to say, the complete text defining this type was present in the ASN.1 specification. 为什么是两者呢？是后来才添加了 GeneralizedTime 这个类型吗？不是的！在 1982 年的早期草稿中，只有 UTCTime 这个类型存在，而且用于表示日期和时间的字符串规范被“硬编码”在了 ASN.1 规范中。也就是说，定义这个类型的完整文本其实就存在于 ASN.1 规范中。

GeneralizedTime was added before the first ASN.1 specification was published in 1984, but did not contain the full specification - it referred to what was then a new ISO Standard (ISO 8601). However, early users of ASN.1 were already finalising their texts based on use of UTCTime, and it was left in the ASN.1 specification. The fact that UTCTime only used a two digit year and GeneralizedTime a four-digit year was not even a subject of discussion in 1982! (The other difference between the two types was in the precision of the time - at best a precision of a second for UTCTime, more for GeneralizedTime). GeneralizedTime 这一术语在 1984 年第一个 ASN.1 规范发布之前就已经被引入了，但当时并没有包含完整的规范内容——它只指的是当时新的 ISO 标准（ISO 8601）。不过，早期的 ASN.1 使用者们已经根据 UTCTime 的定义来整理他们的规范，因此 GeneralizedTime 也被纳入了 ASN.1 规范中。实际上，在 1982 年时，UTCTime 使用两位数表示年份，而 GeneralizedTime 则使用四位数表示年份，这两个类型之间的区别甚至都没有被讨论过！（这两个类型之间的另一个区别在于时间的精度——UTCTime 最多只能精确到秒，而 GeneralizedTime 则可以精确到更多位）。

Slightly less forgivable was the Directory work, which was not published until 1988, but also used UTCTime! It is possible that the attraction of a "hard-wired" specification - you don't need to seek out another publication in order to see what you are getting - was an influence in encouraging designers to use UTCTime (rather than GeneralizedTime) during the 1980s. 稍微不可原谅的是《Directory》这个作品，因为它直到 1988 年才出版，而且还是使用了 UTCTime 这个规范。或许，“固化”规范的优势——无需寻找其他资料来了解自己所使用的规范——正是促使设计师在 20 世纪 80 年代选择使用 UTCTime 而非 GeneralizedTime 的原因。

The comment in figure 22 about interpreting a UTCTime value as a "sliding window" is one of three varying recommendations often made for two-digit year fields: 在图 22 中的评论中，将 UTCTime 值解释为“滑动窗口”是一种常见的建议方式。这只是针对两位数年份字段的三种不同建议之一。

(DEFAULT in the past). Interpret as a year between 1900 and 1999 - the default setting, and certainly the intent in 1982, but a bad idea today! （过去常采用此默认设置）。可以将其解释为 1900 年至 1999 年之间的任何年份——这确实是 1982 年的默认设定，但如今看来这是个糟糕的想法！

(SIMPLE proposal for now). Interpret as a year between 1950 and 2049 - simple, and it buys us another 50 years! （目前只是一个简单的提议）。可以将这一时间范围理解为 1950 年到 2049 年之间的一整年——这样，我们就能多获得 50 年的时间了！

• (SLIDING WINDOW - works forever!). Interpret any 2-digit year that matches the bottom two digits of the current year as the current year. Interpret all other values as years within a window from the current year minus fifty years to the current year plus 49 years (or minus 49 to plus 50 - a matter of choice - but it should be clearly defined). This means that on the 31 December each year, the interpretation of dates fifty years in the past changes to an interpretation as a date fifty years in the future. If there never are dates in your system that are fifty years in the past (and no need to refer to any that are more than forty-nine years in the future), this system clearly works, and allows two-digit years to be used indefinitely. A neat solution! • （滑动窗口机制——永远适用！）将任何与当前年份最后两位数字相匹配的两位数字年份视为当前年份。其余所有数值则视为从当前年份往前推 50 年，或者往后推 49 年之间的年份（或者往前推 50 年或者往后推 49 年——这由用户自行选择；但必须明确说明）。这意味着每年 12 月 31 日时，过去 50 年的日期表达方式会变为未来 50 年的日期表达方式。如果您的系统中永远不存在过去 50 年的日期（也不需要使用未来超过 49 年的日期），那么这个系统显然非常适用，而且使得两位数字的年份可以无限使用。真是巧妙的解决方案啊！

What does "UTC" stand for? It comes from the CCIR (Consultative Committee on International Radio), and stands for "Co-ordinated Universal Time" (the curious order of the initials comes from the name in other languages). In fact, despite the different name, "GeneralizedTime" also records Co-ordinated Universal Time. What is this time standard? Basically, it is Greenwich Mean Time, but for strict accuracy, Greenwich Mean Time is based on the stars and there is a separate time standard based on an atomic clock in Paris. Co-ordinated Universal Time has individual "ticks" based on the atomic clock, but from time-to-time it inserts a "leap-second" at the end of a year (or at the end of June), or removes a second, to ensure that time on a global basis remains aligned with the earth's position round the sun. This is, however, unlikely to affect any ASN.1 protocol! “UTC”代表什么？这个缩写来自国际无线电咨询委员会，意为“协调世界时”。虽然名称不同，但“GeneralizedTime”同样记录了协调世界时。那么，这种时间标准究竟是什么呢？实际上，它就是格林尼治标准时间。不过，为了追求更高的精度，格林尼治标准时间是以恒星为基准的，而巴黎的原子钟则构成了另一个独立的时间标准。协调世界时有基于原子钟的“计时单位”，但每隔一段时间，会在一年结束时（或六月底）插入一个“闰秒”，或者删除一个计时单位，以确保全球时间能够保持与地球绕太阳公转的位置同步。不过，这种情况不太可能影响任何 ASN 协议吧！

What is the exact set of values of UTCTime? The values of the type are character strings of the following form: UTCTime 类型的确切值集是什么？该类型的数值形式为以下形式的字符串：

<table><tbody><tr><td data-imt-p="1" data-imt_insert_failed_reason="same_text">yymmddhhmmZ</td></tr><tr><td data-imt-p="1" data-imt_insert_failed_reason="same_text">yymmddhhmmssZ</td></tr><tr><td data-imt-p="1" data-imt_insert_failed_reason="same_text">yymmddhhmm+hhmm</td></tr><tr><td data-imt-p="1">yymmddhhmm-hhmm 耶耶耶——嗯……</td></tr><tr><td data-imt-p="1" data-imt_insert_failed_reason="same_text">yymmddhhmmss+hhmm</td></tr><tr><td data-imt-p="1" data-imt_insert_failed_reason="same_text">yymmddhhmmss-hhmm</td></tr></tbody></table>

"yymmdd" is year (00 to 99), month (01 to 12), day (01 to 31), and "hhmmss" is hours (00 to 23), minutes (00 to 59), seconds (00 to 59). “yymmdd”表示年份（00 到 99），月份（01 到 12），日期（01 到 31）；而“hhmmss”则代表小时（00 到 23），分钟（00 到 59），秒数（00 到 59）。

The "Z" is a commonly-used suffix on time values to indicate "Greenwich Mean Time" (or UTC time), others being "A" for one hour ahead, "Y" for one hour behind, etc, but these are NOT used in ASN.1. “Z”是一个常用的后缀，用于表示“格林尼治标准时间”（即 UTC 时间）。其他符号表示不同的时间差异，例如“A”表示快一小时，“Y”表示慢一小时等等。不过，在 ASN.1 标准中并不使用这些符号。

If the "+hhmm" or "-hhmm" forms are used (called a time differential), then the first part of the value expresses local time, with UTC time obtained by subtracting the "hhmm" for "+hhmm", and adding it for "-hhmm". The ASN.1 specification contains the following example (another example, added in 1994 shows a "yy" of "01" representing 2001!): 如果使用“+hhmm”或“-hhmm”的形式来表示时间（这被称为时间差分表示法），那么值的第一部分表示本地时间；而 UTC 时间则可以通过从“+hhmm”中减去“hhmm”来获得，然后再加上“-hhmm”来得到。ASN.1 规范中包含了以下示例（另一个示例是 1994 年添加的，其中“yy”为“01”，表示 2001 年！）：

```txt
If local time is 7am on 2 January 1982 and co-ordinated universal time is 12 noon on 2 January 1982, the value of UTCTime is either of "8201021200Z" or "8201020700-0500". 
```

GeneralizedTime is the same overall format, but has a four-digit year, and allows "any of the precisions specified in ISO 8601". GeneralizedTime 格式总体上保持不变，但会包含一个四位数的年份，并且允许使用 ISO 8601 标准中规定的任何精度表示方式。

GeneralizedTime is not without its problems, however. ISO Standards undergo revision from time to time, and referencing them from within another specification can allow things to change under your feet! It became clear in the mid-1990s that many people had implemented GeneralizedTime assuming that the maximum available precision for seconds was three digits after the decimal point (a milli-second). On closer inspection of ISO 8601 (current version), it is clear that unlimited precision is permitted - there is no restriction on the number of digits after the decimal point. It was an uncompleted homework task for the author to try to find earlier versions (and in particular the version current in 1982!) of ISO 8601 to determine for how long an arbitrary precision had been permitted. Perhaps a reviewer will undertake the research? Otherwise it is left as another small exercise for the reader! 不过，GeneralizedTime 也有其不足之处。ISO 标准会不时进行修订，而如果在其他规范中引用这些标准，可能会导致实际情况发生变化。在 20 世纪 90 年代中期，人们发现许多人使用 GeneralizedTime 时，认为秒数的最大精度为小数点后三位（即毫秒）。但仔细查看当前的 ISO 8601 标准，就会发现实际上允许无限精度的表示——小数点后数字的位数没有限制。对于作者来说，完成一项未竟的任务就是找到更早版本的 ISO 8601 标准，特别是 1982 年生效的版本，以了解究竟在何时开始允许如此高的精度。或许可以由某位审稿人来研究这个问题吧？否则，这就可以作为一项留给读者的小练习了！

Another issue arising with both UTCTime and GeneralizedTime relates to canonical encodings: should the different precisions be regarded as different encodings for the same abstract value (a given time) where trailing zeros are present ("8202021200Z" v "820202120000Z"), or as different abstract values (because precision is a part of the abstract information conveyed)? A similar question occurs with the time differential. It actually doesn't matter much which approach is taken, so long as those using canonical encoding rules know the answer. The current text says that the precision and time differential are different ways of encoding a time (a single abstract value), and that in canonical encoding rules, the time differential shall not be present (and the "Z" shall), and that there shall be no trailing zeros in the precision, so the example "8202022120000Z" is not legal in the canonical encoding rules. This is another area where arguments can continue over the precise set of abstract values of this type. 另一个与 UTCTime 和 GeneralizedTime 相关的问题是关于规范编码的：不同的精度是否应被视为同一个抽象值（即某个具体时间）的不同编码方式，当存在末尾零时（“8202021200Z”与“820202120000Z”）；还是应该将它们视为不同的抽象值（因为精度属于所表示的抽象信息的一部分）？关于时间差的问题也有类似的疑问。实际上，采用哪种编码方式并没有太大区别，只要使用规范编码规则的人知道如何处理这些差异即可。当前的规定指出，精度和时间差是表示时间（单个抽象值）的两种不同编码方式；在规范编码规则中，时间差不应出现，而末尾的零则必须去除。因此，在规范编码规则中，“8202022120000Z”这种格式是不被允许的。这也是一个可能会因这类抽象价值的确切定义而引发争论的领域。

## 3 Additional notational constructs 3 个额外的符号构造

## 3.1 The selection-type notation 3.1 选择型表示法

There is no example in figure 22! I have only seen "selection types" used in one application specification. They are not common! 在图 22 中没有提到这一点的例子！我只在一个应用规范中看到过“选择类型”的使用。这种用法并不常见啊！

The SELECTION TYPE notation - you are unlikely ever to see this - forget it! SELECTION 类型标记——你几乎不可能遇到这种标记，所以还是别考虑了吧！

The ASN.1 specification talks about "The selection type", but the heading in this clause is more accurate - ASN.1 规范中提到了“选择类型”这一概念，不过这一条款的标题更为准确——

this is a piece of notation more akin to "IMPORTS" than to a type definition: it references an existing definition. 这是一种类似于“导入”的注释方式，而不是类型定义。它指的是一个已有的定义。

The selection-type notation takes the following form: 选择型表示法的格式如下：

```typescript
identifier-of-a-choice-alternative < Type-notation-for-a-CHOICE 
```

For example, given: 例如，给定以下条件：

```asn1
Example-choice ::= CHOICE
{alt1 Type1,
alt2 Type2,
alt3 Type3} 
```

Then the following type-notation can be used wherever type-notation is required within the scope (module) in which "Example-choice" is available: 那么在“Example-choice”这个模块中，当需要使用类型表示法时，就可以使用以下类型表示法了：

```shell
alt1 < Example-choice
alt2 < Example-choice
alt3 < Example-choice 
```

This notation references the type defined as the named alternative of the identified choice type, and should be seen as another form of type-reference-name. Notice that if the selection-type notation is in a module different from that in which "Example-choice" was originally defined, any tagging or extensibility environment applied to the referenced type is that of the module containing the original definition of Example-choice, not that of the selection-type notation. 这种标记方式指的是作为已识别的选择类型的一种命名替代形式。可以将其视为另一种类型引用名称的表示方式。需要注意的是，如果选择类型的标记位于与定义“Example-choice”的模块不同的模块中，那么对被引用类型的任何标签或扩展性处理都将发生在包含“Example-choice”原始定义的模块中，而不是选择类型标记所指示的模块中。

Value notation for "a selection type" is just the value notation for the selected type. “选择类型”的值表示方式，其实就是所选类型的值表示方式。

In other words, for the type-notation "alt3 < Example-choice", the value-notation is the valuenotation for "Type3". (The identifier "alt3" does not appear in the value-notation for the "selection type", nor are there any colons present.) 换句话说，对于类型标记“alt3 < 示例选择”，数值标记就是对应“Type3”的数值表示。（标识符“alt3”并未出现在“选择类型”的数值标记中，也沒有冒号符号。）

## 3.2 The COMPONENTS OF notation 3.2 符号的组成部分

This is another example of a rarely-used piece of notation that references the inner part of a sequence or set. The only reason to use it is that you can avoid an extra TLV wrapper in BER! It is again not illustrated in figure 22! 这是另一个较少使用的符号表示方式，用于指代序列或集合的内部元素。使用它的唯一原因是为了避免在 BER 编码中需要额外的 TLV 封装层！不过，这一点在图 22 中并没有被展示出来。

The COMPONENTS OF notation you won't often see this either, so forget this too! 那些你不常看到的符号组成部分，也无需去理会它们！

What follows is described in relation to "SEQUENCE", but applies equally to "SET". However, a "COMPONENTS OF" in a "SEQUENCE" must be followed by type-notation for a sequence-type (which remember may, and usually will, be a type-reference-name), and similarly for SET. 以下描述与“序列”相关的内容，但这些描述同样适用于“集合”。不过，在“序列”中的“组成部分”之后，需要使用类型表示法来指明序列的类型（记住，这个类型名称通常是一个类型引用名）；对于集合也是如此。

Suppose we have a collection of elements (identifiers and type-notation) that we want to include in quite a few of the sequence types in our application specification. Clearly we do not want to write them out several times, for all the obvious reasons. We could, of course, define a type: 假设我们有一些元素（标识符和类型标记），这些元素需要在我们的应用程序规范中的多个序列类型中引用。显然，由于种种显而易见的原因，我们不想多次书写这些元素。当然，我们可以定义一个类型来容纳这些元素。

```asn1
Common-elements ::= SEQUENCE
{element1 Type1,
element2 Type2,
...
element23 Type23} 
```

and include that type as the first (or last) element of each of our "actual" sequences: 并将该类型作为我们每个“实际”序列的第一个（或最后一个）元素。

```css
First-actual-sequence ::= SEQUENCE
{used-by-all Common-elements,
next-element Some-special-type,
next-again Special2,
etc The-last} 
```

We do the same for all the sequences we need these common elements in. That is fine. (And with PER it really is fine!) But with BER, if you recall the way BER works, we get an outer-level TLV for "First-actual-sequence", and in the "V" part a TLV for each of its elements, and in particular a TLV for the "used-by-all" element. Within the "V" part of that we get the TLVs for the elements of "Common-elements". But if we had copied - textually - the body of "Common-elements" into "First-actual-sequence", there would be no TLV for "Common-elements" - we would have saved (with BER) two or three - perhaps four! - octets! 我们对所有需要这些公共元素的序列都执行同样的操作。这没什么问题。（使用 PER 的话，确实没有问题！）但是在使用 BER 时，如果你还记得 BER 的工作方式的话，我们会为“First-actual-sequence”得到一个外部级别的 TLV，而在“V”部分，我们会为每个元素都得到一个 TLV，尤其是“used-by-all”元素的 TLV。在“V”部分中，我们还会得到“Common-elements”中各个元素的 TLV。不过，如果我们直接把“Common-elements”的内容复制到了“First-actual-sequence”中，那么“Common-elements”就不会有单独的 TLV 了——使用 BER 的话，我们可能会浪费两三个，甚至四个八位元！

If we use "COMPONENTS OF", we can write: 如果我们使用“组成部分”这个词，我们可以这样表达：

```css
First-actual-sequence ::= SEQUENCE
{
    COMPONENTS OF Common-elements,
    next-element Some-special-type,
    next-again Special2,
    etc The-last} 
```

The "COMPONENTS OF" notation provides for such copying without textually copying - it "unwraps" the sequence type it references. “COMPONENTS OF”这种表示方式允许无需逐字复制即可进行复制操作——它实际上是将所引用的序列类型“解包”出来。

Note that there is no identifier on the "COMPONENTS OF element". This is not optional - the "identifier" must be omitted. The "COMPONENTS OF is not really an element of the SEQUENCE - it is a piece of notation that extracts or unwraps the elements. It is often referred to as "textual substitution", but that is not quite correct (alert reader!) because the tagging and extensibility environment for the extracted elements remains that of the module where they were originally defined. 请注意，在“COMPONENTS OF”这个元素上并没有标识符。这一点是不可或缺的——所谓的“标识符”实际上是可以被省略的。“COMPONENTS OF”并不真正属于序列的一部分，它只是一种用于提取或解包元素的标记方式。这种方式常被称作“文本替换”，但这个说法并不完全准确（提醒一下！）。因为被提取出的元素仍然遵循着它们最初被定义时的模块标签和扩展性规则。

There is some complexity if automatic tagging is applied and COMPONENTS OF is used. The reader has two choices: just forget it and note that it all works (unless you are a hand-coding implementor, in which case see the next option!), or as a good exercise (none are formally set in this book!) go to the ASN.1 specification and work out the answer! 如果采用自动标记功能，并且使用 COMPONENTS OF 这个参数，的话，就会有一些复杂的情况出现。读者可以选择两种处理方式：要么直接忽略这个问题，认为一切都能正常工作（除非你是那种习惯手工编写代码的人，这种情况下，请参阅下一个选项！）；要么作为一个练习，去研究 ASN.1 规范，自己找出答案！不过，本书中并没有正式规定这些规范的内容。

## 3.3 SEQUENCE or SET? 3.3 是序列还是集合？

The type-notation for SEQUENCE, SET, SEQUENCE OF and SET OF has been wellillustrated in earlier text and examples, together with the use of "DEFAULT" and "OPTIONAL". Remember that in BER (not CER/DER/PER), the default value is 对于“SEQUENCE”、“SET”、“SEQUENCE OF”和“SET OF”这种类型标记，前面的文本和示例中已经有过详细的说明。同时，也提到了“DEFAULT”和“OPTIONAL”这些用法。需要记住的是，在 BER 协议中（而非 CER/DER/PER 协议中），默认值是……

```txt
An application designer can generally choose to use SEQUENCE or SET more or less arbitrarily. Read this text then use SEQUENCE always! 
```

essentially advisory. An encoder is permitted to encode explicitly a default value, or to omit the corresponding TLV, entirely as an encoders option. 本质上属于建议性的功能。编码器可以选择明确指定一个默认值，或者完全省略相应的 TLV 条目，这属于编码器的选项之一。

We have already discussed briefly the differences between 我们已经简要讨论过这两种方式之间的区别了。

 

$$
\text { SEQUENCE } \{\dots \} \quad \text { and } \quad \text { SET } \{\dots \}
$$

from an encoding point of view in BER (the TLVs are in textual order for SEQUENCE, in an order chosen by the encoder for SET), and also from the more theoretical stand-point that "order is not semantically significant" in SET. 从编码的角度来看，在 BER 编码中，TLV 按文本顺序排列，而这一顺序是由编码器自行选定的。从更理论的角度来说，在 SET 编码中，“顺序在语义上并不重要”。

The problem is that if we regard the abstract value as a collection of unordered information, and we want a single bit-pattern to represent that in an encoding, we have to invent some more-or-less arbitrary criteria to order the collection in order to form a single bit-pattern encoding! This can make for expensive (in CPU and perhaps also in memory terms) encoding rules. In the case of SET { .... }, if we want to remove encoders options, it is possible to use either textual order (not really a good idea) or tag order (tags are required to be distinct among the elements in a SET) to provide the ordering as a static decision. However, in the case of "SET OF", no-one has found a way of providing a single bit-pattern for a complete set-of value without doing a run-time sort of the encodings of each element! This can be expensive! 问题在于，如果我们把抽象价值视为一组无序的信息，而想要用一种单一的位模式来表示这些信息，那么我们就必须发明一些或多或少任意性的标准来对这些信息进行排序，从而形成一个单一的位模式编码。这可能会导致昂贵的编码规则，无论是在 CPU 资源还是内存方面。在“集合{…}”的情况下，如果我们想要去除编码选项，可以使用文本排序（这并不是一个好的方法）或标签排序（因为集合中的元素之间需要具有独特性），来提供静态的排序方式。然而，在“价值集合”的情况下，还没有人找到一种方法，可以在不对每个元素的编码进行运行时排序的情况下，为整个价值集合提供一个单一的位模式编码。这可能会非常耗费资源。

We will return to this point when we discuss the canonical (CER) and distinguished (DER) encoding rules in Section III, but advice today (but see figure 999!) would be: Best to keep off "SET {", and avoid "SET OF" like the plague! 当我们在第 III 节讨论规范编码（CER）和特殊编码（DER）规则时，我们会再次提到这一点。不过，今天的建议是：最好避免使用“SET {}”这种表达方式，而应该像躲避瘟疫一样避免使用“SET OF”这种表述方式。

One very small detail to mention here: the default tag provided for "SET {" and for "SET OF" is the same. It is different from that provided for "SEQUENCE {" and for "SEQUENCE OF", but these are also the same. This only matters if you are carefully applying tags within CHOICEs and SETs etc with the minimal application of tags. In this case you will have studied and be happy with later text on tagging, and will carefully check the ASN.1 specification to determine the © OS, 31 May 1999 95 default tag for all types! If you are a normal mortal, however, you will routinely apply tags to everything (pre-1994), or will use "AUTOMATIC TAGS" (post-1994), and the fact that the default tag for "SEQUENCE {" is the same as that for "SEQUENCE OF" will not worry you in either case! 这里还有一个非常小的细节需要提及：对于“SET{}”和“SET OF”来说，默认的标签是相同的。这与“SEQUENCE{}”和“SEQUENCE OF”的默认标签不同，但这两个情况的默认标签也是相同的。这一点只有在你在为 CHOICE 和 SET 等结构仔细地分配标签时才重要，因为在这种情况下，你之后会学习到关于标签使用的知识，并且会仔细参考 ASN.1 规范来确定所有类型的默认标签。不过，如果你只是普通的人，那么你可以随意地为所有事物分配标签（在 1994 年之前），或者选择使用“自动标签”（在 1994 年之后）。无论哪种情况， “SEQUENCE{}”的默认标签与“SEQUENCE OF”的默认标签相同，这一点都不会让你感到困扰！

## 3.4 SEQUENCE, SET, and CHOICE (etc) value-notation 3.4 序列、集合和选择等值的表示方式

We have used the type notation for these constructions almost from the first page of this book, but now we need to look at their valuenotation. (Actually, you will never encounter this except in courses or an illustrative annex to the ASN.1 specification, but it reinforces the point that for any type you can define with ASN.1 there is a well-defined notation for all of its values.) 在本书的几乎每一页中，我们都使用了类型表示法来描述这些构造。但现在我们需要关注一下这些值的表示方式。（实际上，除了在课程教学或 ASN.1 规范的说明性附录中之外，你很少会接触到这种表示法。不过，这种表示法确实强调了这样一个观点：对于可以用 ASN.1 定义的任何类型，其所有值都有一套明确的表示方式。）

```txt
SEQUENCE, SET, CHOICE, etc value-notation
You won't ever need to write it, and will only ever read it in courses and ASN.1 tutorials and silly books like this, but here it is. It is good to complete your education! 
```

To say it simply: value notation for "SET {" and "SEQUENCE {" is a pair of curly braces containing a comma-separated list. Each item in the list is the identifier for an element of the "SEQUENCE {" (taken in order) or "SET {" (in any order), followed by value-notation for a value of that element. Of course this rule is recursively applied if there are nested "SEQUENCE {" constructs. 简单来说，对于“SET {}”和“SEQUENCE {}”，值表示法就是一对花括号，里面包含一个由逗号分隔的列表。列表中的每个元素都是“SEQUENCE {}”（按顺序排列）或“SET {}”中的一个元素的标识符，后面跟着该元素的值用值表示法表示。当然，如果包含嵌套的“SEQUENCE {}”结构，那么这个规则会递归地应用下去。

For "SET OF" and "SEQUENCE OF" we again get a pair of curly braces containing a commaseparated list, with each item being the value notation for a value of the type-notation following the "OF". 对于“SET OF”和“SEQUENCE OF”这两个词，我们再次得到一对大括号，里面包含一个用逗号分隔的列表。列表中的每个元素都是一种特定类型的值的表示形式，这些值都是按照“OF”来连接的。

```txt
todays-return Return-of-sales ::=
{version {version2},
no-of-days-reported-on 8,
time-and-date-of-report
two-digit-year:"9901022359Z",
reason-for-delay {network-failure},
-- additional-information not included
sales-data
{--Report-item 1:
{item {wineco-items special-tiop (112)},
item-description "Special Reserve Purchase Tio Pepe",
-- A newly-stocked item.
bar-code-data 'A0B98764934174CDF'H,
-- ran-out-of-stock is defaulted to FALSE.
min-stock-level {mantissa 2056, base 10, exponent -2},
max-stock-level {mantissa 100, base 10, exponent 0},
average-stock-level {mantissa 7025, base 10, exponent -2} },
--Report-item 2:
{item {wineco-items own-dry-sherry (19)},
bar-code-data 'A0B897632910DFE974'H,
ran-out-of-stock TRUE,
min-stock-level {mantissa 0, base 10, exponent 1},
max-stock-level {mantissa 105, base 10, exponent 0},
average-stock-level {mantissa 5032, base 10, exponent -2} }
--Only two report items in this illustration
}
Figure 23: A value for "return-of-sales" 
```

Finally, for "CHOICE", it is NOT what you might expect - no curly braces! Instead you get the identifier of one of the alternatives, then a colon (:), then value notation for a value of that alternative. There is no value notation for any occurrence of tags, nor for extensibility markers or exception specifications. The colon in choice values was not present pre-1994. 最后，对于“CHOICE”这个标识符，实际情况并不像你想象的那样——没有使用大括号。而是先列出某个选项的名称，然后是一个冒号，接着是该选项的值。对于标签、可扩展标记或异常说明来说，并没有使用值表示法。在 1994 年之前，选择值中并不使用冒号来表示结构。

This should be sufficient for the reader to work through figure 23, which is cast as "todays-return" a (random) value for the type "Return-of-sales" given in figure 22. 对于读者来说，这些信息应该足以理解图 23 的内容。图 23 展示了在图 22 中给出的“销售退回”类型时，对应的（随机）返回值。

## 4 What else is in X.680/ISO 8824-1? 4. X.680/ISO 8824-1 中还包含哪些内容呢？

This chapter has attempted to cover "Basic ASN.1" - the material present in the first of the four documents specifying the ASN.1 notation, and in common use in specifications today. There is, however, some additional material in this first of the ASN.1 documents that has been deferred to later chapters. For completeness of this chapter, this is briefly mentioned below. 这一章节试图涵盖“基础 ASN.1”相关内容——即那些出现在指定 ASN.1 表示法的四份文档中的基础内容，这些文档在当前的规范中也被广泛采用。不过，在这份 ASN.1 文档中还有一些额外的内容被推迟到后续章节中去讨论。为了完整性，下面简要提及这些内容。

The additional areas are: 额外的区域包括：

Extensibility and version brackets: This is a big subject, touched on briefly already, and first introduced in 1994. (Exception specifications are a related subject, but don't appear in X.680 - they are in X.682 - and are also treated later.) 可扩展性和版本标签：这是一个非常重要的主题，虽然之前已经简要提及过，但实际上是在 1994 年首次被引入的。（异常规范也是一个相关的主题，不过在 X.680 标准中并未涉及——它们位于 X.682 标准中，并且会在后面进一步讨论。）

• Tagging: Touched on briefly already. This was important in the past, but with the introduction of automatic tagging in 1994 is much less important now. • 标签标注：之前这一点已经简要提及过。虽然过去标签标注非常重要，但自从 1994 年引入自动标签标注功能之后，其重要性就大大降低了。

The object identifier type: This was fully-covered in X.680/ISO 8824-1 pre-1998, but parts of the material are now split off into another Recommendation/Standard. Previous chapters of this book produced a lot of introductory material, but the discussion remains incomplete! 对象标识符类型：这一主题在 X.680/ISO 8824-1 标准（1998 年前版本）中已经详细阐述过了，不过其中的一些内容现在被分离到了另一个推荐标准之中。本书之前的章节已经介绍了很多相关的内容，但讨论仍然不够全面！

Hole types: This term is used for the more formal ASN.1 terms EXTERNAL, EMBEDDED PDV, CHARACTER STRING, and "Open Types" (post-1994). And dare we mention ANY and ANY DEFINED BY (pre-1994)? If you have never heard of ANY or ANY DEFINED BY, that is a good thing. But you will have to be sullied by later text - sorry! 类型分类：这一术语在更为正式的 ASN 标准中被称为 EXTERNAL、EMBEDDED PDV、CHARACTER STRING，以及“开放类型”（1994 年之后的分类）。另外，还有“由某种方式定义的类型”（1994 年之前使用的分类）。如果你从未听说过“由某种方式定义的类型”，那也是好事。不过，后续的内容可能会让你感到困惑——抱歉！

The character string types: There are about a dozen different types for carrying strings of characters from various world-wide character sets. So far we have met PrintableString, VisibleString, GraphicString, and UTF8String, and discussed them briefly. There is a lot more to say! 字符字符串类型：大约有十几种不同的类型可以用来存储来自各种全球字符集的字符序列。到目前为止，我们已经介绍了 PrintableString、VisibleString、GraphicString 和 UTF8String 这些类型，并简要讨论了它们。不过，还有更多内容需要提及！

Sub-typing, or constrained types: This is a big area, with treatment split between X.680/ISO 8824-1 and X.682/ISO 8824-3. We have already seen an example of it with the range constraint "(1..56)" on "no-of-days-reported-on" in figure 22. This form is the one you will most commonly encounter or want to use, but there are many other powerful notations available if you have need of them. 子类型或受限类型：这是一大类概念，相关的处理被分散在 X.680/ISO 8824-1 和 X.682/ISO 8824-3 标准中。我们已经在图 22 中看到了一个例子，其中“报告的天数”这一字段受到了“(1..56)”这样的范围限制。这种表示方式是最常用的，但如果你需要更多强大的表示方式，还有许多其他可用的符号可供选择。

Macros: We have to end this chapter on an obscenity! Some reviewers said, "Don't dirty the book with this word!" But macros were very important (and valued) in ASN.1 up to the late 1980s, and will still be frequently encountered today. But I hope none of you will be driven to writing one! Sections I and II will not tell you much more about macros, but the historical material in Section IV discusses their introduction and development over the life of ASN.1. It is a fascinating story! 宏指令：我们得用一些粗俗的词汇来结束这一章节吧！有些评论者说：“不要用这样的词汇来污染这本书的内容！”不过，在 1980 年代末之前，宏指令在 ASN.1 中一直非常重要（并且受到重视）。直到今天，人们仍然经常需要使用宏指令。不过，希望你们中没有人会真的想要编写宏指令吧！在第一和第二部分中，我们不会详细介绍宏指令的细节，但在第四部分的历史资料中，可以了解到宏指令在 ASN.1 发展过程中的引入和发展过程。这真是一个有趣的故事啊！

Additionally, there are a number of new concepts and notations that appear in X.681/ISO 8824-2, X.682/ISO 8824-3, and X.683/ISO 8824-4 (published in 1994). These are: information object classes (including information object definition and information object sets), and parameterization. 此外，X.681/ISO 8824-2、X.682/ISO 8824-3 和 X.683/ISO 8824-4（于 1994 年发布）中出现了一些新的概念和符号。这些新概念包括：信息对象类（包括信息对象的定义和集合）、以及参数化机制。

Where the above items have already been introduced (in this chapter or earlier), their detailed treatment is left to a chapter of Section II. Where they have not yet been discussed, a brief introduction appears in the following short chapter. 在前面已经介绍了上述各项内容的地方（在本章或之前的部分），其详细论述则留到了第二部分的章节中。而对于那些尚未被讨论的内容，则会在接下来的简短章节中做出简要介绍。
