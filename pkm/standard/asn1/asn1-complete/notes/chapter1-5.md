# Chapter 5 Reference to more complex areas 第五章 关于更复杂区域的参考内容

# (Or: There is always more to learn!) （或者可以说：总是有更多的东西可以学习！）

## Summary: 总结：

This chapter provides an introduction to concepts and notation that are treated more fully in Section II. Some of these features have been briefly mentioned already, but without a full treatment. This includes: 这一章节介绍了一些概念与符号的概述，这些内容将在第二部分中详细讨论。虽然其中一些要点已经简要提及过，但并未进行全面的阐述。具体包括：

• Object identifiers • 对象标识符

• Character string types • 字符字符串类型

• Subtyping • 亚型分类

• Tagging • 标签标注

• Extensibility, exceptions, and version brackets • 可扩展性、异常处理机制以及版本管理功能

Other topics that are introduced here for the first time are: 这里首次介绍的其他主题包括：

• Hole types • 洞的类型

• Macros • 宏

• Information object classes and objects and object sets • 信息对象类、单个对象以及对象集合

• Other types of constraint • 其他类型的约束条件

• Parameterization • 参数化处理

• The ASN.1 semantic model • ASN.1 语义模型

An introduction is provided here for the reader who wishes to ignore Section II. As at mid-1998, there are no areas or concepts concerned with the ASN.1 notation that have not been at least introduced by the end of this chapter. 对于那些希望忽略第二部分内容的读者，这里提供一下介绍。截至 1998 年中期，关于 ASN.1 标记语言的任何相关领域或概念，至少都已经在本章中有所涉及了。

The aim of the text in this chapter is: 本章文本的目标是：

• to describe the concept and the problem that is being addressed; • 用来描述所涉及的概念以及需要解决的问题；

to illustrate where necessary key aspects of the notational support so that the presence of these features in a published protocol can be easily recognised; and 为了便于人们识别在已发表的实验报告中出现的这些标记符号，有必要对相关的标记方式进行说明；

• to summarise the additional text available in Section II. • 请总结第二部分中提供的附加文本内容。

If further detail is needed on a particular topic (if something takes the reader's interest), then the appropriate chapter in Section II can be consulted. The Section II chapter provides "closure" on all items mentioned in this chapter unless otherwise stated. 如果需要对某个主题进行更详细的介绍（当某些内容能够吸引读者的兴趣时），可以参考第二部分中的相应章节。除非另有说明，否则第二部分中的章节将涵盖本章中所有提到的内容。

## 1 Object identifiers 1. 对象标识符

The OBJECT IDENTIFIER type was briefly introduced in Chapter 4 (clause 2.9) of this section, where the broad purpose and use of this type was explained (with the type notation). Examples of its value notation have appeared throughout the text, although these have not completely illustrated all possible forms of this value notation. OBJECT IDENTIFIER 类型在本书第 4 章（2.9 条款）中简要介绍过，其中阐述了该类型的通用用途和用法（包括类型表示方式）。虽然在整个文本中出现了一些该类型值的示例，但这些示例并未完全涵盖所有可能的取值形式。

A more detailed discussion of the form of the 关于这种形式的更详细讨论如下：

OBJECT IDENTIFIERs have a simple type notation, and a value notation that has already been seen. The "Further Details" chapter tells you about the form of the name space and how to get some, and provides discussion of the value notation. 对象标识符具有简单的类型表示法，而其数值表示法则已在前面介绍过。在“更多细节”章节中，会详细说明命名空间的格式以及如何获取某些值，同时也会讨论数值表示法的相关内容。

object identifier tree (the name-space) is given in Section 2 (Further Details) Chapter 1, together with a full treatment of the possible forms of value notation. 对象标识符树（命名空间）的相关信息位于第 1 章的第 2 节“更多细节”中，该节还详细介绍了数值表示形式的各种可能性。

Earlier text has given enough for a normal understanding of this type and the ability to read existing specifications. It is only if you feel you need some object identifier name space and don't know how to go about getting some that the "Further Details" material will be useful. This material also contains some discussion about the (legal) object identifier value notation that omits all names and uses numbers only, and about the (contentious) value notation where different names are associated with components, depending on where the value is being published and/or the nature of lower arcs. 前面的文本已经足够让我们理解这类对象以及如何阅读现有的规范了。不过，如果你觉得需要一些对象标识符的名称空间，并且不知道如何获取这些名称，那么“更多细节”部分的内容将会很有用。该部分还讨论了关于（法律上的）对象标识符值表示法的内容——这种表示法不使用任何名称，只使用数字；同时，也涉及了（有争议的）值表示法，即根据值发布的地点以及下层弧线的性质，不同的名称会被用于不同的组件。

## 2 Character string types 2 种字符字符串类型

The names of types whose values are strings of characters from some particular character repertoire have appeared throughout the earlier text, and Chapter 4 Clause 2.8 of this section discussed in some detail the type notations: 在之前的文本中，出现过一些类型的名称，这些类型的值是由特定字符集中的字符构成的字符串。本节的第四章第 2.8 条详细讨论了这些类型的表示方式。

## PrintableString VisibleString ISO646String UTF8String 可打印字符串 可见字符串 ISO646 字符串 UTF8 字符串

although the treatment introduced terms such as "Unicode" that may be unfamiliar to some readers. 虽然这种处理方式引入了一些可能对某些读者来说比较陌生的术语，比如“Unicode”。

There has also been little treatment so far of the value notation for these types, nor has the precise set of characters in each repertoire been identified fully. 目前，对于这些类型的值表示法也几乎没有得到妥善处理；此外，每种字符集的具体组成也尚未完全确定。

There are many more character string types than you have met so far, and mechanisms for constructing custom types and types where the character repertoire is not defined until runtime. The value notation provides both a simple "quoted string" mechanism and a more complex mechanism to deal with "funny" characters. 除了目前已经遇到的之外，还有许多其他类型的字符字符串。此外，还有办法可以创建自定义类型，或者在这些类型中，字符集在运行时才被定义。值表示法提供了一种简单的“ quoted string”机制，同时也提供了处理特殊字符的更复杂机制。

Section II (Further Details) Chapter 2 provides a full treatment of the value notation and provides references to the precise definitions of the character repertoires for all character string types. It describes the following additional character string types that you will encounter in published specifications (all the character string types are used in at least one published specification): 第二部分（更多细节）第 2 章详细介绍了字符表示法的相关内容，并给出了所有字符串类型中字符集的精确定义。该章节还描述了一些在公开规范中可能出现的额外字符串类型（所有字符串类型至少出现在其中一个公开规范中）。

```txt
NumericString
IA5String
TeletexString
T61String
VideotexString
GraphicString
GeneralString
UniversalString
BMPString
UTF8String 
```

The simplest value notation for the character string types is simply the actual characters enclosed in quotation marks (the ASCII character QUOTATION MARK, usually represented as two vertical lines in the upper quartile of the character glyph). For example: 对于字符串类型，最简单的数值表示方式就是直接用引号将字符括起来（即 ASCII 码中的引号字符，通常表示为字符字形上半部分两条竖线）。例如：

## "This is an example character string value" “这是一个示例字符字符串值”

The (alert - I hope we still have some!) reader will ask four questions: （提醒一下——希望我们还能保留一些这样的机会！）读者们会提出四个问题：

• How do I express characters appearing in character string values that are not in the character set repertoire used to publish the ASN.1 specification? (Publication of ASN.1 specifications as ASCII text is common). • 如何表示那些不在用于发布 ASN.1 规范的字符集中的字符值？（通常将 ASN.1 规范以 ASCII 文本的形式进行发布）。

• How do I include the ASCII QUOTATION MARK character (") in a character string value? • 如何在字符字符串值中包含 ASCII 引号字符（"）？

• Can I split long character string values across several lines in a published specification? • 在发布的规范中，可以将较长的字符字符串值分成多行显示吗？

• How do I precisely define the white-space characters and control characters in a character string value? • 如何精确地定义字符字符串中的空白字符和控制字符？

These are topics addressed in the "Further Details" section. 这些都是在“更多细节”部分中提到的主题。

In summary: 总结来说：

• A QUOTATION MARK character is included by the presence of adjacent quotation marks (a very common technique in programming languages). • 当一个引号字符与另一个引号字符相邻时，就会形成一个引用标记字符（这是编程语言中非常常见的技术）。

ASN.1 provides (by reference to character set standards), names for all the characters in the world (the names of these characters use only ASCII characters), and a value notation which allows the use of these names. ASN.1 规范通过引用字符集标准来定义所有字符的名称（这些字符的名称仅使用 ASCII 字符），并采用了一种数值表示方式，使得可以方便地使用这些名称。

• Cell references are also available for ISO 646 and for ISO 10646 to provide precise specification of the different forms of white-space and of control characters appearing in ASCII. • 对于 ISO 646 和 ISO 10646 标准，也提供了单元格引用功能，从而可以精确地指定 ASCII 编码中各种空白字符和控制字符的具体形式。

An example of a more complex piece of character string value notation described in the "Further Details" section is: 在“更多细节”部分中描述的一种更为复杂的字符字符串值表示方式示例如下：

$$
\{\text { nul }, \{0, 0, 4, 2 9 \}, \text { cyrillicCapitalLetterIe }," A B C" \}
$$

go to "Further Details" if you want to know what that represents! 如果你想要了解这些数字代表的具体含义，可以点击“更多详细信息”。

The above provision is, however, not the end of the story. If UniversalString or BMPString or UTF8String are used, then ASN.1 has built-in names (again defined by reference to character set standards) for about 80 so-called "collections" of characters. Here are the names of some of these collections: 不过，上述规定并非故事的终点。如果使用了 UniversalString、BMPString 或 UTF8String 这些类型，那么 ASN.1 提供了内置的命名规则，用于指代大约 80 种所谓的“字符集合”。以下是一些这些集合的名称：

```txt
BasicLatin
BasicGreek
Cyrillic
Katakana
IpaExtensions
MathematicalOperators
ControlPictures
Dingbats 
```

Formally, these collections are subsets (subtypes - see the next clause of this chapter) of the BMPString type, and it is possible to build custom character string types using combinations of these pre-defined types. 从形式上讲，这些集合都是 BMPString 类型的子集（或称亚型——请参考本章的下一节）。通过使用这些预定义类型进行组合，可以构建出自定义的字符字符串类型。

Section II Chapter 2 provides full coverage of these features, but a more detailed discussion of the form and historical progression of character set standardization has been placed in Section IV (History and Applications). Readers interested in gaining a full understanding of this area may wish to read the relevant chapter in Section IV before reading the Section II chapter. 第二部分第二章详细介绍了这些特性。而关于字符集标准化形式及历史发展的更详细讨论则位于第四部分（历史与应用）。对于那些希望全面了解这一领域的人士来说，建议在阅读第二部分章节之前先阅读第四部分的相关章节。

Finally, ASN.1 also includes the type: 最后，ASN.1 还定义了类型这一概念：

## CHARACTER STRING 字符字符串

which can be included in a SEQUENCE or SET (for example) to denote a field that will contain a character string, but without (at this stage) determining either the character repertoire or the encoding. 这可以被包含在一个序列或集合中，用来表示一个包含字符串的字段。不过，在现阶段，还无法确定该字段所使用的字符集或编码方式。

This is an incomplete specification or "hole", and is covered in Section II Chapter 7. If this character string type is used, both the repertoire and the encoding are determined by announcement (or if the OSI stack is in use, by negotiation) at run-time, but can be constrained by additional specification using "constraints" (see "Other types of constraint" below), either at primary specification time, or by "profiles" (additional specifications produced by some group that reduces options in a base standard). 这其实是一个不完整的规范或“空白”部分，相关内容将在第二章的第七节中详细说明。如果使用了这种字符字符串类型，那么其编码方式以及可用字符集都是在运行时通过协商来确定的（如果使用的是 OSI 协议栈，则通过协商来决定）。不过，可以通过额外的规范来对其进行约束，这些约束可以通过“约束条件”来实现（详见下文的“其他类型的约束”部分）。此外，还可以根据“配置文件”来进行约束，这些配置文件是由某些团体制定的额外规范，它们可以在基础标准中减少选择的可能性。

## 3 Subtyping 3.亚型分类

There has been little text on this subject so far. We have seen an example of: 目前关于这个主题的文字很少。我们已经看到过一个例子：

 

$$
\text { INTEGER } (1.. 5 6)
$$

to specify an integer type containing only a subset of the integer values - those in the range from 1 to 56 inclusive. This is called "simple subtyping" and was provided in the ASN.1 Specifications from about 用于指定一种整数类型，该类型只包含一部分整数值——即从 1 到 56inclusive 范围内的数值。这种机制被称为“简单子类型划分”，大约在 ASN.1 规范中有所提及。

From simple subtyping through to relational constraints. ASN.1 provides powerful mechanisms for selecting a subset of the values of an ASN.1 type, and (in PER) for encoding that selected subset in a very efficient manner. 从简单的类型划分到关系约束。ASN.1 提供了强大的机制，可以用来选择 ASN 类型中的一部分值，并且能够以非常高效的方式将这些选中的值编码出来。

1986 onwards. 1986 年起。

Simple subtyping enables a subset of the values of any ASN.1 type to be selected to define a new type, using a variety of quite powerful mechanisms. Note that an abstract syntax (the set of abstract values that can be communicated) for a "Full Class" protocol is normally defined as the set of values of a single ASN.1 type (see Chapter 1 clauses 2.1, 2.3 and 3, and Chapter 3 clause 4). If a "Basic Class" protocol is needed, then this can conveniently be defined as a subset of those values. The "simple subtyping" mechanisms described in Section II Chapter 3 contain enough power to enable such a specification to be formally provided using the ASN.1 notation. 简单的类型继承机制允许选择任意 ASN.1 类型的部分值来定义新的类型。通过使用一系列非常强大的机制，可以实现这一功能。需要注意的是，对于“完整类”协议来说，其抽象语法（即可以传输的抽象值集合）通常定义为单个 ASN.1 类型的所有值（详见第 1 章的 2.1 节、2.3 节和 3 节，以及第 3 章的 4 节）。如果需要一个“基础类”协议，那么可以方便地将其定义为上述值的子集。第 3 章第二节中描述的“简单类型继承”机制具有足够的灵活性，能够使用 ASN.1 表示法来正式定义这样的类型规范。

An example of a more complex form of subtyping would be: 一种更复杂的类型划分形式示例如下：

```txt
Basic-Ordering-Class ::= Wineco-Protocol
(WITH COMPONENTS
ordering (Basic-Order) PRESENT,
sales ABSENT }) 
```

Note that all subtyping (and application of constraints - see below) is done by syntax which is enclosed in round parentheses and follows some piece of type notation (frequently a type reference name). 请注意，所有的类型划分（以及约束条件的应用——详见下文）都是通过语法来实现的。这些语法被包裹在圆括号中，并且遵循特定的类型表示方式（通常是一个类型引用名称）。

It is, however, possible to also view the notation: 不过，也可以这样理解这个符号表示：

INTEGER (1..56) 整数类型 (1..56)

as putting a constraint on the integer field, and this gives rise to considerations of what is to be done if the constraint is violated in received material. (This should normally only occur if the sender has implemented a later version of the protocol where the constraint has been relaxed. This is covered in Chapter 5 of Section II (see below). 这其实是一种对整数字段的约束，因此需要考虑如果在接收到的数据中违反了这一约束该怎么办。（这种情况通常只会在发送方采用了该协议的后续版本时才会出现，因为在那个版本中约束条件已经被放宽了。这一点在第二部分第五章中有详细说明。）

A number of other forms of constraint have been introduced into ASN.1 in 1994 related to constraining what can fill in a "hole", or to relating the contents of that "hole" to the value of some other field. These other forms of constraint are covered in Section II Chapter 9. 在 1994 年，还引入了一些其他类型的约束条件，这些约束条件用于限制可以填充“空位”的内容，或者将“空位”的内容与某个其他字段的值联系起来。这些其他类型的约束条件在第二章第 9 节中有详细说明。

## 4 Tagging 4. 标签标注

Earlier text has dipped in and out of tagging, but has never given a full treatment. The TLV concept (which underlies tagging) was introduced in Chapter 1 Clause 5.2, and further text on ASN.1 tagging appeared in Chapter 2 Clause 2.7 and Chapter 3 Clause 3.2, where tagging was described entirely in relation to the TLV encoding philosophy, and the concepts of "implicit tagging" and "explicit tagging" were introduced. 之前的文本中偶尔会提到标签化概念，但从未有过全面的描述。TLV 概念（作为标签化的基础）在第一章第 5.2 条中有所介绍。关于 ASN.1 标签化的更多内容则出现在第二章第 2.7 条和第三章第 3.2 条中，这些描述完全基于 TLV 编码理念，同时引入了“隐式标签化”和“显式标签化”的概念。

Up to 1994, getting your tags right was fundamental to writing a correct specification. Post-1994, AUTOMATIC TAGS in the module header enables them to be forgotten. So details are relegated to Section II. If you want to read and understand a specification (or even to implement one), you already know enough about the tag concept, but if you want to take control of your tags (as you had to pre-1994), you will need the Section II material 在 1994 年之前，正确标注标签是编写规范文件的基础。而在 1994 年之后，模块头部的自动标签功能使得这些标签可以被遗忘。因此，细节内容被放在了第二部分中。如果你想要阅读和理解一份规范文件（甚至想要实现某个功能），那么你已经对标签概念有了足够的了解。但如果你想要重新控制自己的标签标注方式（就像在 1994 年之前那样），那么你就需要参考第二部分的内容了。

```txt
[3] INTEGER
My-Useful-Type ::= [APPLICATION 4] SEQUENCE { .... }
[PRIVATE 4] INTEGER
[UNIVERSAL 25] GraphicString 
```

Section II Chapter 4: 第二部分第四章：

• Gives a full treatment of the different classes of tag. • 对各类标签进行了全面的描述。

Provides an abstract model of types and values that makes the concepts of explicit and implicit tagging meaningful, even if encoding rules are being employed that are not TLVbased. 提供了一个关于类型和值的抽象模型，使得显式标记和隐式标记的概念变得有意义。即使使用的是非基于 TLV 的编码规则，这个抽象模型仍然能够解释这些概念。

• Discusses matters of style in the choice of tag-class used in a specification. • 讨论了在规范中使用的标签类别选择时所需要考虑的风格问题。

• Gives the detailed rules on when tags on different elements of sets and sequences or alternatives of choices are required to be distinct. • 提供了详细的规则，说明在何种情况下，集合中的不同元素或选择项所需的标签必须保持不同。

## 5 Extensibility, exceptions and version brackets 5 扩展性、异常处理以及版本标签

The first two terms - extensibility and exceptions - have been mentioned in several places already. 前两个术语——可扩展性和例外情况——已经在多个地方被提及过。

Clause 2 of the Introduction defined "extensibility" as the means of providing interworking between deployed "version 1" systems and "version 2" systems that are designed and deployed many years later. 在引言的第 2 条中，将“扩展性”定义为一种实现手段，它能够使已部署的“版本 1”系统与那些在多年后才设计和部署的“版本 2”系统之间进行互联互通。

You will recognise the use of extensibility provision by an ellipsis (three dots), of exception specification by the use of an exclamation mark (!), and of version brackets by the use of an adjacent pair of open square brackets with a matching adjacent pair of closing square brackets. 你会通过三个点的省略号来识别可扩展性的设置；通过感叹号来表示异常情况的指定；而版本号的标识则可以通过一对开方括号和另一对闭方括号来实现。

```txt
If a very great provision is made for 
```

extensibility, then almost every element in an encoding has to be "wrapped up" with a length field and an identification, even when both parties (if they know the full specification) are perfectly aware that these are fixed values. In other words, we are forced into a "TLV" (see Chapter 1 clause 5.2) style of encoding. If, however, we restrict the places where a version 2 specification can add new material (and wrap up only the new version 2 material), we can produce a much more efficient encoding. This is provided by the Packed Encoding Rules (PER). 在可扩展性方面，几乎每个编码元素都需要用一个长度字段和一个标识符来标识。即使双方都完全了解这些值是固定不变的，这种情况仍然会发生。换句话说，我们被迫采用一种“TLV”式的编码方式（参见第 1 章第 5.2 条）。然而，如果我们限制版本 2 规范在哪些位置可以添加新内容（并且只对新增的内容进行编码），那么就可以实现更高效的编码方式。这种编码方式是由“打包编码规则”来实现的。

The extension marker was briefly introduced in Chapter 3 clause 3.3, together with the exception specification that identifies actions that version 1 systems should take with any added material. 在第三章的 3.3 条款中，简要介绍过这个扩展标记。同时，还提到了一个例外情况，即版本 1 的系统在接收到任何新增内容时，需要采取相应的行动。

Section 2 Chapter 5: 第 2 节 第 5 章：

• expands on the Chapter 3 text; • 对第三章的内容进行了扩展；

• describes all the places where extension markers can be placed; • 描述了可以放置扩展标记的所有位置；

• illustrates the exception specification; and • 还阐述了例外情况的指定方式；此外……

• introduces and describes the concept of "version brackets" (see below). • 介绍了“版本括号”这一概念，并对其进行了解释（详见下文）。

When extensibility provision was first introduced into ASN.1, every added sequence or set element was "wrapped up", but it later became apparent that this was not necessary - all that needed "wrapping up" was the totality of the material added in this place in the new version. Hence we have the concept of bracketing this material together with so-called "version brackets". This is 在 ASN.1 中首次引入可扩展性功能时，每个新增的序列或集合元素都需要被“包装”起来。不过后来发现，其实并不需要这样做——只需要对新版本中新增的所有内容整体进行“包装”即可。因此，我们提出了将这部分内容纳入所谓的“版本括号”中的概念。这就是所谓的“版本括号”的用法。

```txt
SEQUENCE
{field1 TypeA,
    field2 TypeB,
    ... ! PrintableString : "See clause 59",
    -- The following is handled by old systems
    -- as specified in clause 59.
    [[ v2-field1 Type2A,
    v2-field2 Type2B ]],
    [[ v3-field1 Type3A,
    v3-field2 Type3B ]],
    ...
    -- The following is version 1 material.
    field3 TypeC} 
```

## Figure 24: Illustration of extensibility markers and version brackets 图 24：可扩展标记和版本区间的示意图

illustrated in figure 24, which is repeated and described more fully in Section II Chapter 5. 如图 24 所示，这一内容在第二章第 5 节中有更详细的说明和复述。

Notice that it is not mandatory to include version brackets. If they are absent the effect is as if each element of the sequence had been added separately in a succession of versions. 请注意，并不一定要包含版本号括号。如果省略了这些括号，那么就会给人一种感觉，就像序列中的每个元素都是分别在不同的版本中添加的。

Note also that if there is no further version 1 material ("field3 TypeC" in Figure 24 is not present), then the final ellipsis is not required, and will frequently be omitted. 另外需要注意的是，如果不再有与版本 1 相关的内容出现（例如图 24 中的“field3 TypeC”这一项不存在），那么最后的省略号就不需要了，通常也会被省略掉。

## 6 Hole types 6 种孔的类型

Chapter 2 Clause 2.1 introduced the concept of "holes": parts of a specification left undefined to allow other groups to "customise" the specification to their needs, or to provide a carrier mechanism for a wide variety of other types of material. 第 2 章，第 2.1 条介绍了“空洞”这一概念：所谓“空洞”，指规范中那些未明确规定的部分，这些部分可以被其他团队根据需要进行调整，或者用作承载各种不同类型数据的机制。

You can leave a hole by using one of several ASN.1 types, but it may be better to use Information Object Classes instead! 你可以使用多种 ASN.1 类型来创建空洞，但或许使用信息对象类会更合适！

In general, specifiers can insert in their protocols any ASN.1 type and leave the semantics to be associated with values of that type undefined. This would constitute a "hole". Thus "holes" can in principle be provided using INTEGER or PrintableString! But usually when specifiers leave a "hole", they want the container to be capable of carrying an arbitrary bit-pattern. Thus using OCTET STRING or BIT STRING to form a "hole" would be more common. This is generally not recommended, as there are specific ASN.1 types that are introduced to clearly identify the presence of a hole, and in some cases to provide an associated identification field which will identify the material in the "hole". 通常，规范器可以在协议中插入任何 ASN.1 类型，而将相关语义留给该类型的数值来定义。这就形成了一种“空洞”。因此，原则上可以使用 INTEGER 或 PrintableString 来填充这种“空洞”。不过，当规范器留下“空洞”时，他们通常希望容器能够容纳任意的位模式。因此，使用 OCTET STRING 或 BIT STRING 来填充“空洞”更为常见。不过，这种方法一般并不推荐，因为有一些特定的 ASN.1 类型被引入用来明确标识“空洞”的存在，并且在某些情况下，还会使用相关的标识字段来标识“空洞”中的内容。

Provision for "hole"s has been progressively enriched during the life of ASN.1, and some of the early mechanisms are deprecated now. The following are the types normally regarded as "hole" types, and are described fully in Section II Chapter 7: 在 ASN.1 的整个生命周期中，对“空类型”的支持一直得到了逐步加强。不过，现在有一些早期的机制已经不再被推荐使用。以下这些类型通常被视为“空类型”，详细内容请参考第二章第 7 节：

## 7 Macros 3 月 7 日

ASN.1 contained (from 1984 to 1994) a very complex piece of syntax called "the macro notation". It was removed in 1994, with equivalent (but much improved) facilities provided by the "Information Object Class" and related concepts (see below). 在 1984 年至 1994 年期间，ASN.1 规范中包含了一种非常复杂的语法结构，称为“宏表示法”。这一语法结构在 1994 年被弃用，之后由“信息对象类”及相关概念来替代，这些替代方案虽然功能相当，但性能得到了显著提升（详见下文）。

Many languages, graphics packages, and word processors, have a macro facility. The name "macro" is very respectable. However, the use of this term in ASN.1 bears very little relationship to its use in these other packages. 许多编程语言、图形软件包和文字处理软件都提供了宏功能。所谓“宏”，这个名称本身就很不错。不过，在 ASN.1 中，这个术语的使用与其在那些其他软件中的含义几乎没有关联。

There is much controversy surrounding macros. They were part of ASN.1 for its first decade, but produced many problems, and were replaced by Information Object Classes in 1994. You will not often see text defining a macro (and should certainly not write any today), but you may still see in older specifications text whose form depends on a macro definition imported into a module. 关于宏定义，一直存在很多争议。在最初的十年里，宏定义是 ASN.1 规范的一部分，但后来引发了诸多问题，因此于 1994 年被信息对象类所取代。如今，你很少会看到关于宏的定义文本了（当然也不应该再编写这样的文本），但在一些较旧的规范中，仍可能找到以宏定义形式嵌入到模块中的文本。

```txt
MY-MACRO MACRO ::=
BEGIN
TYPE NOTATION ::= ....
.....
VALUE NOTATION ::= ....
.....
END 
```

## Figure 25: The structure of a macro definition 图 25：宏定义的结构

Section IV ("History") says a little more about what macros are all about. You are unlikely to meet the definition of a macro (use of the macro notation) in specifications that you read, but figure 25 illustrates the general structure (the four dots representing further text whose form is defined by the macro notation specification). This piece of syntax can appear anywhere in a module where a type reference assignment can occur, and the name of the macro (conventionally always in upper case) can be (and usually is) exported from the module for use in other modules. 第四部分“历史”部分进一步介绍了宏的概念。在您阅读的规范中，可能不太会看到宏的定义（即宏标记的使用方式），但图 25 展示了宏的一般结构（四个点表示需要进一步描述的文本，其形式由宏标记规范定义）。这种语法结构可以出现在任何可以进行类型引用赋值的模块中，而宏的名称（通常一律使用大写字母）可以被导出到模块之外，以便其他模块使用。

The macro notation is the only part of ASN.1 that is not covered fully in this book! Readers of this book should NEVER write macros! However, you will encounter modules which import a macro name and then have syntax that is an invocation of that macro. Again, a macro invocation can appear anywhere that a type definition can appear. 宏注释是 ASN.1 中唯一没有在这本书中充分讨论的部分！阅读这本书的人绝对不应该编写宏代码！不过，你会遇到一些模块，这些模块会导入宏名称，然后使用某种语法来调用该宏。再次强调，宏调用的位置可以与类型定义的任何位置结合使用。

One standard that contains a lot of "holes" is called "Remote Operations Service Element (ROSE)". ROSE defines (and exports) a macro called the OPERATION macro to enable its users to provide sets of information to complete the ROSE protocol. A typical piece of syntax that uses the OPERATION macro would look like Figure 26 (but most real examples are much longer). 一种包含大量“漏洞”的标准被称为“远程操作服务元素（ROSE）”。ROSE 定义了一个名为 OPERATION 的宏，用户可以通过该宏提供一系列信息以完成 ROSE 协议的操作。使用 OPERATION 宏的典型语法结构如图 26 所示（但实际上大多数实际案例的语法结构要复杂得多）。

```txt
lookup OPERATION
    ARGUMENT IA5String
    RESULT OCTET STRING
    ERRORS {invalidName, nameNotFound}
    ::= 1

Figure 26: An example of use of the ROSE OPERATION macro ©OSS.31 May 1999 
```

To fully understand this you need some knowledge or ROSE. ROSE is briefly described in Section II Chapter 7, partly because of its wide-spread use, but mainly because it provides good illustrations of macro use, Information Object Class specification, and exception handling. 要完全理解这一点，你需要一些相关的知识或背景知识。ROSE 的相关内容在第七章的第二部分中有简要介绍，其原因在于 ROSE 的广泛应用，同时也因为它能够很好地说明宏变量使用、信息对象类规范以及异常处理等方面的问题。

The OPERATION macro definition was replaced in the 1994 ROSE specification by specification of an OPERATOR Information Object Class, and specifications including syntax like figure 26 are gradually being changed make us of the OPERATOR Information Object Class instead. 在 1994 年的 ROSE 规范中，OPERATION 宏定义被替换为 OPERATOR 信息对象类的定义。现在，像图 26 这样的语法规范也在逐步被修改，以使用 OPERATOR 信息对象类来替代原有的定义。

## 8 Information object classes and objects and object sets 8 个信息对象类以及相应的对象和对象集

When protocol specifiers leave "holes" in their specification, there are frequently several such holes, and the users of the specification need to provide information of a specified nature to fill in these holes. Most of the uses of the macro notation were to enable these users to have a notation to specify this additional information. 当协议规范中留有“空白”时，通常会有多个这样的空白点。此时，规范的使用者就需要提供相应的信息来填充这些空白。宏表示法的大部分用途，就是为了让使用者能够使用这种表示方式来指定这些额外的信息。

Information Object Classes (with objects and object sets) was the main addition to the ASN.1 notation in 1994, replacing macros with a much enhanced functionality. Detail in these areas are left to Section II, but an increasing number of old specifications are being revised to use this notation, and most new specifications use it. These areas are important! 在 1994 年，信息对象类（包括对象和对象集）成为了 ASN.1 表示法的主要新增功能。这一功能相比之前的宏定义有了显著的提升。关于这些方面的详细信息请参考第二部分的内容。越来越多的旧规范正在被修订以采用这种表示法，而大多数新的规范都使用了这种格式。这些改进非常重要！

The Information Object Class concept recognises that specifiers leaving "holes" need to clearly identify where these holes are, but more particularly to be able to list the information required to complete the "hole". In the simplest case, the information needed will be a set of ASN.1 types (with their associated semantics) that can fill the hole, together with either an integer or an object identifier value which is associated with that type and its semantics. The identifier will be carried in the carrier protocol, as well as a value of the type. 信息对象类概念认为，那些留下“空缺”的指定项需要明确指出这些空缺的位置，并且能够列出填补这些空缺所需的信息。在最简单的情况下，所需的信息将是一组 ASN.1 类型（附带相关的语义描述），再加上一个与该类型及其语义相关联的整数或对象标识符值。这个标识符会包含在传输协议中，同时还会包含该类型的值。

ASN.1 provides a syntax for defining the form of information to be collected. This is illustrated in figure 27: ASN.1 提供了一种用于定义需要收集的信息格式的语法。如图 27 所示：

```txt
MY-CLASS ::= CLASS
    {&Type-to-fill-hole,
    &identifier INTEGER}
Figure 27: Notation to define an Information Object Class 
```

Note the use of the "&" character. This is the only place that "&" is used in ASN.1, and its presence is a clear indication that you need to read the Section II material on Information Object Classes! 请注意使用了“&”符号。在 ASN1 中，只有在这个位置使用了“&”符号。它的存在清楚地表明你需要阅读关于信息对象类的相关内容，即第二部分的内容！

<table><tbody><tr><td data-imt-p="1">Table constraints, relational constraints- the way to constrain holes in amanner consistent with the definition ofan Information Object Set. Go toSection II. 表级约束、关系型约束——这些机制可以用来限制模式中的空洞现象，从而确保符合信息对象集的定义。请参见第二部分。</td></tr><tr><td data-imt-p="1">User-defined constraints - a catch-allfor any other constraint that you need! 用户自定义约束——可以适用于任何你需要的其他约束条件！</td></tr></tbody></table>

Once a specifier has defined an Information Object Class (and typically exported the reference name), users can then define sets of objects of that class, and link them into the base protocol. This is amplified and illustrated in Section II. 一旦一个规范定义了一个信息对象类（通常还会导出该类的引用名称），用户就可以定义该类的对象集合，并将这些对象链接到基础协议中。这一机制在第二部分中有详细的说明和示例。

## 9 Other types of constraints 9. 其他类型的约束条件

There are forms of constraint that are a little more complex than the simple subtyping discussed earlier. They are called "table constraints", "relational constraints", and "user-defined" constraints. The first two are closely related to the use of a defined set of information objects to fill in holes in a consistent manner. The latter relates to specification of hole contents which can not be done in a wholly formal manner within the ASN.1 notation. Like simple subtyping, these constraints always appear in round brackets following a type name (or a hole specification). They are illustrated and described in Section II 有一些约束形式比之前讨论的简单类型继承要复杂一些。这些约束被称为“表约束”、“关系约束”以及“用户定义约束”。前两种约束与使用一组定义好的信息对象来填补其中的空白密切相关。而第三种约束则涉及到那些在 ASN.1 标记法中无法以完全正式的方式指定出来的空白内容。与简单类型继承类似，这些约束总是以圆括号的形式出现在类型名称之后（或者空白说明之后）。这些约束在第二节中有详细的说明和示例。

## 10 Parameterization 10 种参数化方式

The ability to parameterize an ASN.1 specification is a very simple but extremely powerful mechanism. It was introduced in 1994. The concept of dummy parameters of functions or methods in a programming language is quite 对 ASN.1 规范进行参数化的能力是一种非常简单但极其强大的机制。这一机制是在 1994 年引入的。在编程语言中，为函数或方法定义虚拟参数的概念其实相当简单。

Parameterization - very simple but very powerful. All ASN.1 reference names can have a dummy parameter list, actual parameters are supplied when they are used. 参数化设计——非常简单但功能强大。所有 ASN.1 参考名称都可以包含一个虚拟参数列表，实际参数在需要使用时才会被提供。

common, with actual parameters being supplied when the function or method is invoked. 常见的形式是在调用函数或方法时，需要提供具体的参数值。

In a similar way, an ASN.1 type-reference name can be given dummy parameters, with actual parameters being supplied when that type is used. 同样地，ASN.1 类型引用名称也可以被赋予虚拟参数，而实际参数则会在使用该类型时才会被提供。

For example: 例如：

$$
\begin{array}{l} \text {My - Type} \left\{\text {INTEGER:dummy1, Dummy2} \right\}: := \\ \text {SEQUENCE} \\ \left\{\text {first - field Dummy2,} \right. \\ \text {second - field INTEGER (1..dummy1)} \end{array}
$$

Here "My-Type" has two dummy parameters, the first an integer used to provide a bound on "second-field", and a second that provides the type for the first field. Typically, My-Type will be used in several different places in the total specification, with different actual parameters in each case. 在这里，“My-Type”有两个虚拟参数：第一个是整数类型，用于限制“second-field”的取值范围；第二个则是用于指定第一个字段的类型。通常，“My-Type”会在整个规范中的多个不同位置被使用，且每个位置的实际参数也会有所不同。

Parameterization is an important tool to enable the linking of Information Object Sets defined by user groups into the holes left by the original specifier, although its use is wider than this. 参数化是一种重要的工具，它能够将用户组所定义的信息对象集与原始规范中留下的空白区域联系起来。不过，参数化的应用范围其实远不止于此。

## 12 The ASN.1 semantic model 12 ASN.1 语义模型

There are many places in ASN.1 where the phrase "must be of the same type as" appears. For example, if a dummy parameter is the value of some type, then the actual parameter "must be of the same type as the dummy parameter". A value following DEFAULT "must be of the same type as the type preceding the word DEFAULT". It is clear that if the types in question are the same type-reference name, then they "are the same type". But suppose 在 ASN 中，有很多地方出现了“必须与某种类型相同”这样的表述。例如，如果一个虚拟参数的值是某种类型，那么实际参数也“必须与虚拟参数属于同一种类型”。在“DEFAULT”之后的值也“必须与‘DEFAULT’之前的类型相同”。显然，如果所涉及的类型都是使用相同的类型引用名称，那么它们就是“同一种类型”。但假设……

Abstractions, abstractions, models, models. Everybody has their own. 抽象、抽象、模型、模型……每个人都有自己的模型。

But sometimes they need to be explicit in order to express clearly what is legal and what is not. 不过，有时候就需要明确说明哪些行为是合法的，哪些是不合法的。

the two types in question are specified with textually distinct but identical text? Or textually distinct but with some minor variations in the text? Are they still "the same type"? What "minor variations" might be permitted? ASN.1 text up to 1999 had little to say to clarify these questions! Fortunately, difficult cases rarely appear in real specifications, but writers of ASN.1 tools do need to know what is legal and what is not (or to make assumptions themselves)! 这两种类型是通过文字上明显不同但内容相同的文本来定义的？还是通过文字上有所不同但在某些细节上存在轻微差异来定义的？它们仍然属于“同一种类型”吗？那些“轻微差异”究竟指的是什么呢？在 1999 年之前的 ASN.1 标准中，几乎没有相关的规定来明确这些问题！幸运的是，在实际的规范中，很少会出现复杂的案例。不过，编写 ASN.1 工具的开发者确实需要清楚哪些行为是合法的，哪些是不合法的（或者他们自己需要做出一些假设！）。

An attempt was made in 1990 to remove all such phrases and provide more rigour in these areas, but it proved impossible to get satisfactory text agreed in time, and at the last minute text for the 1994 specification reverted back to the original "must be of the same type". 在 1990 年，人们尝试删除所有此类表述，并力求在这些方面实现更严格的规定。然而，最终未能在规定时间内就达成令人满意的文本协议。因此，在 1994 年的规范中，这些表述又回到了原来的“必须属于同一类型”这一表述。

Work in this area, however, continued. It was recognised that to solve the problem there needed to be a well-defined "abstract model" or "mental model" or "semantic model" (the latter term was eventually chosen) to define the underlying abstractions that were represented by a piece of ASN.1 text, with the starting point being the concept of a type as a container of a set of abstract values as first described in Chapter 1 Clause 3.1. 不过，相关工作仍然持续进行。人们认识到，要解决这个问题，就需要有一个明确的“抽象模型”或“语义模型”来定义那些由 ASN1 文本所表示的底层抽象概念。而这一模型的起点，就是第一章第 3.1 条中首次提出的“类型”概念，即类型作为一组抽象值的容器。

At the time of writing (early 1999), the work is complete and agreed, and publication is expected later in 1999. 在撰写本文时（1999 年初），这项工作已经完成并得到了双方同意，预计将在 1999 年晚些时候出版。

## 13 Conclusion 13 结论

This completes the discussion of the ASN.1 notation for Section I "ASN.1 Overview" (the remaining chapters discuss ASN.1 tools and management and design issues). If more detail is needed on any of the topics that have not been fully described in this section, then the appropriate chapter of Section II should be consulted. These are largely independent, and can be taken in any order. 至此，关于 ASN.1 标记的讨论已经结束。在第一节“ASN.1 概述”中已经对相关内容进行了介绍；其余章节则涉及 ASN.1 工具以及相关管理和设计问题。如果某些主题还需要更多细节说明，可以参考第二节中的相应章节。这些章节内容大多是独立的，可以按照任意顺序阅读。

For more details about Encoding Rules, see Section III, and for a history of the development of ASN.1 and some of its applications, see Section IV. 有关编码规则的更多详细信息，请参见第三部分。而关于 ASN.1 的发展历史及其一些应用情况，请参阅第四部分。
