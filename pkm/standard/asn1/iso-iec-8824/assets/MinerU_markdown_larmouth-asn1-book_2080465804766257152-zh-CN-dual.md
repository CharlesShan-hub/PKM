
## SECTION I 第一节

ASN.1 Overview ASN.1 概述


# Chapter 3 Structuring an ASN.1 specification 第三章 构建 ASN.1 规范的结构

(Or: The walls, floors, door-ways and lifts, with some environmental considerations!) （或者：墙壁、地板、门厅以及电梯等建筑构件，以及一些相关的环境考虑因素！）

## Summary: 总结：

ASN.1-based application specifications consist mainly of type definitions as illustrated in Section 1 Chapter 2, but these are normally (and are formally required to be) grouped into collections called modules. 基于 ASN.1 的应用规范主要包含类型定义，如第 2 章第 1 节所描述的那样。不过，这些定义通常会被归类到不同的模块中。

This chapter: 这一章：

• introduces the module structure, • 介绍了该模块的结构。

• describes the form of module headers, • 描述了模块头部的格式。

• shows how to identify modules, • 展示了如何识别各个模块。

• describes how to export and import type definitions between modules. • 描述了如何在不同的模块之间导出和导入类型定义。

The chapter also discusses: 本章还讨论了以下内容：

• some issues of publication format for a complete application specification, and • 关于完整应用规格的某些出版格式问题，以及…

• the importance of making machine-readable copy of the ASN.1 parts available. Part of the definition of a module is the establishment of: • 制作机器可读取的 ASN.1 部分副本的重要性。模块定义的一部分就是需要明确这些副本的可用性。

• a tagging environment, • 一个用于标记的环境，

• an extensibility environment • 一个具有可扩展性的环境

for the type-notations appearing in that specification. The meaning and importance of these terms is discussed in this chapter, with final details in Section II. 关于该规格书中出现的各种类型说明。这些术语的含义和重要性将在本章中讨论，具体细节则位于第二部分。

```txt
Modules
All ASN.1 type and value assignments are required to appear within a module, starting with a module header and ending with "END". 
```

## 1 An example 1 一个例子

The example we gave in figure 13 had one top-level type ("Order-for-stock"), and a number of supporting types, most of which we left incomplete. We will still leave the supporting types incomplete (and, indeed, will use three lines of four dots for the body of all the types to avoid repetition), but will now otherwise turn the example in Figure 我们在图 13 中给出的例子包含一个顶层类型（“Order-for-stock”），以及若干辅助类型。这些辅助类型我们大都未详细描述。我们仍会让辅助类型保持不完整状态（实际上，为了避免重复，我们会用三行四个点来表示所有类型的主体），但现在我们将继续展示图例中的例子。

```txt
Wineco-ordering-protocol
{joint-iso-itu-t internationalRA(23) set(42) set-vendors(9)
wineco(43) modules(2) ordering(1)}
DEFINITIONS
    AUTOMATIC TAGS ::=
BEGIN
    Order-for-stock ::= SEQUENCE
    { ....
    ....
    ....}
    BranchIdentification ::= SET
    { ....
    ....
    ....}
    Security-Type ::= SET
    { ....
    ....
    ....}
    OutletType ::= SEQUENCE
    { ....
    ....
    ....}
    Address ::= SEQUENCE
    { ....
    ....
    ....}
END
Figure 14: A complete single-module ASN.1 specification 
```

13 into a complete ASN.1 specification that follows the rules of the language, and that could be fed into an ASN.1 compiler tool. 将 13 个元素整合成一个遵循该语言规则的完整 ASN.1 规范，然后将其输入到 ASN.1 编译器工具中进行处理。

NOTE — The use of three lines of four dots used in figures 13 and 14 is not legal ASN.1! It is used in this book out of sheer laziness! In a real specification there would be a complete list of named and fullyspecified (directly or by type-reference-names) elements. In figure 14, it is assumed that no further typereference-names are used in the body of these types - they use only the built-in types of the language like INTEGER, BOOLEAN, VisibleString, etc. 注意——在图 13 和图 14 中，使用三行四个点的表示方式在合法的 ASN.1 标准中是不被允许的！在本书中之所以采用这种方式，纯粹是因为过于懒散而已。在真正的规范中，应该有一份完整的、包含所有命名且经过明确规定的元素列表。在图 14 中，假设这些类型的内部不再使用其他类型引用，而是仅使用语言内置的类型，如 INTEGER、BOOLEAN、VisibleString 等。

The complete specification is shown in figure 14. 完整的规格说明如图 14 所示。

This example forms what is called an ASN.1 module consisting of a six-line (in this - simple! - case) module header, a set of type (or value) assignment statements, and an "END" statement. This is the smallest legal piece of ASN.1 specification, and many early specifications were of this form - a single module. Today, it is more common for a complex protocol to be presented in a number of ASN.1 modules (usually within a single physical publication or set of Web pages). This is discussed further later. 这个例子构成了一个所谓的 ASN.1 模块。该模块由六行内容组成（在这个简单的情况下），其中包括一系列类型声明以及“END”语句。这是最基础的 ASN.1 规范单元。许多早期的规范都是采用这种形式的——即一个单独的模块。如今，复杂的协议通常会被分解为多个 ASN.1 模块，这些模块通常集中在一个物理出版物或一组网页中。这一点将在后面进一步讨论。

It is very common in a real publication for the module header to appear at the start of a page, for there then to be up to ten or more pages of type assignments (with the occasional value assignment perhaps), and then the END statement, which terminates the module. Normally there would be a page-break after the END statement in a printed specification, whether followed by another module or not. 在真实的出版物中，模块头出现在页面开头是很常见的现象。之后可能会有多达十页或更多的类型定义内容（偶尔也会出现值定义的段落）。接着是 END 语句，用来终止模块。通常在打印出来的规范文件中，END 语句之后会有一个页面分隔符，无论之后是否还有另一个模块。

But Figure 14 is typical of early ASN.1 specifications, where the total protocol specification was probably only a few pages of ASN.1, and a single self-contained module was used for the entire specification. 不过，图 14 代表了早期 ASN 规范的特点。在那个时代，整个协议规范可能只有几页的 ASN 代码，而且整个规范都是通过一个独立的模块来实现的。

Note that whilst the use of new-lines and indentation at the start of this example is what is commonly used, the normal ASN.1 rule that white-space and new-lines are interchangeable applies here too - the module header could be on a single line. 请注意，虽然在这个示例中通常会使用新行号和缩进格式，但实际上 ASN.1 规范中的规则是：空白字符和新行是可以互换使用的——因此，模块头信息完全可以放在同一行上。

We will look in detail at the different elements of the module header later in this chapter, but first we discuss a little more about publication style. 在本章的后面部分，我们将详细探讨模块头文件中的各个元素。但在那之前，我们先来进一步讨论一下出版风格的相关内容。

## 2 Publication style for ASN.1 specifications 2. ASN.1 规范的公报格式

Over the years, different groups have taken different approaches to the presentation of their ASN.1 specifications in published documents. Problems and variation stem from conflicting desires: 多年来，不同的团队在公开文档中呈现其 ASN.1 规范时采用了不同的方法。这些问题的产生源于各种不同的需求：

a) A wish to introduce the various ASN.1 types that form the total specification gradually (often in a "bottom-up" fashion), within normal human-readable text that explains the semantics of the different types and fields. a) 希望逐步引入各种 ASN.1 类型，并将这些类型完整地描述出来（通常采用“从下到上”的呈现方式），同时将这些描述放在正常的人类可读的文本中，以便人们能够理解不同类型和字段的含义。

b) A wish to have in the specification a complete piece of ASN.1 that conforms to the ASN.1 syntax and is ready to feed into an ASN.1 tool, with the type definitions in either alphabetical order of type-reference-name, or in a "top-down" order. b) 希望在规范中包含一个完整的 ASN.1 代码段，该代码段符合 ASN.1 语法规范，并且可以直接用于 ASN.1 工具中。其中，类型定义可以采用类型名称的字母顺序排列，或者采用“自顶向下”的排序方式。

c) The desire not to repeat text, in order to avoid unintended differences, and questions of which text takes precedence if differences remain in the final product. c) 避免重复文本的愿望，以防止出现意外的差异。同时，还需要确定在最终产品中出现差异时，应以哪种文本为准。

There is no one perfect approach - application designers must make their own decisions in these areas, but the following two sub-sections discuss some common approaches. 并没有一种适用于所有情况的最佳方法——应用程序设计师在这些方面必须自行做出决策。不过，以下两个小节介绍了一些常见的做法。

You may want to consider adding linenumbers to your ASN.1 to help references and cross-references ... but these are not part of the language! 您可以考虑在 ASN.1 中添加 linenumbers 元素，以便实现引用和交叉引用功能……不过，这些并不是语言本身的一部分哦！

## 2.1 Use of line-numbers. 2.1 行数的使用方式。

One approach is to give line numbers sequentially to the entire ASN.1 specification, as partly shown in figure 15 (again, lines of four dots are used to indicate pieces of the specification that have been left out). 一种方法是在整个 ASN.1 规范中依次给出行号，如图 15 所示（同样，每四行点表示一个被省略的规范部分）。

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/a0059080-59e4-4cd9-913b-34e7587e39f7/3ff709074aaf3ad62fc8b7b5f2031ce23327b8c0a325639ab62328cdacf00d5f.jpg)

It is important to note that if this specification is fed into an ASN.1 tool, the line numbers have to be removed - they are not part of the ASN.1 syntax, and the writer knows of no tool that provides a directive to ignore them! 需要注意的是，如果将这些规范输入到 ASN.1 工具中，那么行号必须被删除——因为它们不属于 ASN.1 语法的一部分。而且，作者也不知道有任何工具提供了忽略这些行号的指令！

If you have tools to assist in producing it (and they exist), this line-numbered approach also makes it possible to provide a cross-reference at the end of the specification which gives, for each typereference-name, the line number of the type assignment where it is given a type, followed by all the line numbers where that reference is used. For a large specification, this approach is VERY useful to readers. If you don't do this, then you may wish to re-order your definitions into alphabetical order. 如果你有工具可以帮助生成这种格式的内容（而且这样的工具确实存在），那么这种按行号排序的方法还可以让你在规范文件的末尾提供一个交叉引用。通过这个交叉引用，你可以找到每个类型引用对应的行号，以及该引用被使用的所有行号。对于大型规范文件来说，这种做法对读者非常有帮助。如果你没有采用这种方法，那么你可能需要考虑重新排序你的定义，使其按照字母顺序排列。

Once you decide to use line numbers, there are two main possibilities. You can: 一旦你决定使用行号功能，就有两个主要的选择。你可以：

Only put the ASN.1 in one place, as a complete specification (usually at the end), and use the line-numbers to reference the ASN.1 text from within the normal human-readable text that specifies the semantics. 只需将 ASN.1 的规范内容放在一个单独的位置作为完整的规范文档（通常放在文档的末尾），然后通过行号来引用其中的 ASN.1 文本，这样就能在那些易于理解的普通文本中引用到 ASN.1 的语义描述。

• Break the line-numbered ASN.1 into a series of "figures" and embed them in the appropriate place in the human-readable text, again using the line-numbers for more specific references. • 将编号顺序的 ASN1 元素分解为一系列“数字”，并将这些数字嵌入到人类可读的文本中适当的位置。同时，仍使用行号来进行更精确的引用。

The latter approach only works well if the order you have the type definitions in (in the total specification) is the same as the order in which you wish to introduce and discuss them in the main text. 后一种方法只有在你放置类型定义的顺序与在正文部分引入和讨论这些定义的顺序相同时才有效。

## 2.2 Duplicating the ASN.1 text 2.2 复制 ASN1 文本

A number of specifications have chosen to duplicate the ASN.1 text (usually but not necessarily without using line numbers). In this case the types are introduced with fragments of ASN.1 embedded in the human-readable text, and the full module specification with the module header and the "END" are presented as either the last clause of the document, or in an Appendix. 许多规范都选择复制 ASN.1 的文本格式（通常还会保留原有的行号）。在这种情况下，各种类型是通过在人类可读的文本中嵌入 ASN.1 的代码片段来引入的。而完整的模块规范则包括模块头信息以及“END”标记，这些内容要么作为文档的最后一节单独呈现，要么作为附录单独列出。

You may choose to repeat your ASN.1 text, fragmented in the body of your specification and complete in an annex - but be careful the texts are the same! 你可以选择重复列出你的 ASN.1 文本。如果文本在规范的主体部分被分割开来，那么可以在附录中提供完整的文本。不过请注意，文本内容必须完全一致！

Note that where ASN.1 text is embedded in normal human-readable text, it is highly desirable for it to be given a distinctive font. This is particularly important where the individual names of ASN.1 types or sequence (or set) elements or choice alternatives are embedded in a sentence. Where a distinctive font is not possible, then use of italics or of quotation marks is common for such cases. (Quotation marks are generally used in this text.) 需要注意的是，当 ASN.1 文本被嵌入到普通的人类可读文本中时，建议使用独特的字体来表示这些文本。这一点在 ASN.1 类型、序列元素或选择方案的名称被嵌入到句子中时尤为关键。如果无法使用独特的字体，那么通常会使用斜体或引号来表示这些文本。（在本文中，通常会使用引号来表示文本。）

If ASN.1 text appears in more than one place, then it used to be common to say that the collected text in the Appendix "took precedence if there were differences". Today it is more common to say that "if differences are found in the two texts, this is a bug in the specification and should be reported as such". 如果 ASN.1 文本出现在多个地方，过去常这样表述：如果在两份文本中存在差异，那么附录中的文本具有优先适用性。如今，更常见的说法是：“如果两份文本存在差异，那么这就是规范中的缺陷，应该予以报告。”

## 2.3 Providing machine-readable copy 2.3 提供机器可读取的副本

An annex collecting together the entire ASN.1 is clearly better than having it totally fragmented within many pages of printed text, no matter how implementation is to be tackled. 将整个 ASN.1 规范集中在一起作为一个附录，显然比将其分散在众多页面中的印刷文本中要好得多。无论如何实施该规范，采用这种方式都能带来更好的效果。

If your implementors use tools, they will want machine-readable copy: consider how to provide this, and to tell them where it is! 如果您的实施者使用了某些工具，他们自然会希望获得机器可读取的文档。请考虑如何提供这样的文档，并告诉他们文档所在的位置！

Prior to the existence of ASN.1 tools, the ASN.1 specification was there to tell an implementor what to code up, and would rarely need to be fed into a computer, so printed text sufficed. With the coming of ASN.1 compilers, which enable a major part of the implementation to be automatically generated directly from a machine-readable version of the ASN.1 specification, some attention is needed to the provision of such material. 在 ASN.1 工具出现之前，ASN.1 规范只是用来指导实现者如何编写代码，通常不需要直接输入到计算机中，因此打印出来的文本就足够了。随着 ASN.1 编译器的出现，现在可以直接从机器可阅读的 ASN.1 规范中自动生成大部分实现代码，因此现在需要更加重视这类文档的提供工作。

Even if the "published" specification is in electronic form, it may not be easy for a user to extract the formal ASN.1 definition because of the format used for publication, or because of the need to remove the line-numbers discussed above, or to extract the material from "figures". 即使“已发布”的规范文档是以电子形式存在的，但用户仍然可能难以从中提取出正式的 ASN1 定义。这是因为采用了某种特定的发布格式，或者因为需要去除上面提到的行数标记，又或者因为要从“图表”中提取相关信息而变得困难。

Wherever possible, the "published" specification should identify an authoritative source of machine-readable text for the complete specification. This should currently (1998) be ASCII encoded, with only spaces and new-lines as formatting characters, and using character names (see Section II Chapter 2) for any non-ASCII characters in value notations. It is, however, likely that the so-called UTF8 encodings (again see Section II Chapter 2), allowing direct representation of any character, will become increasingly acceptable, indeed, preferable. 在可能的情况下，所发布的规范应明确提供一份可供机器阅读的权威文本来源。目前（1998 年），规范文本通常采用 ASCII 编码格式，仅使用空格和换行符作为格式化字符；对于非 ASCII 字符，则使用字符名称来表示（详见第二章第二节）。不过，允许直接表示任何字符的 UTF8 编码方式（同样参见第二章第二节）可能会越来越被接受，甚至成为首选方式。

It is unfortunate that many early ASN.1 specifications were published by ISO and ITU-T, who had a history of making money from sales of hard-copy specifications and did not in the early days provide machine-readable material. However, a number of Editors of the corresponding Standards and Recommendations did obtain permission to circulate (usually without charge) a machinereadable copy of the ASN.1 (usually as ASCII text), but the availability of such material was not always widely publicised. 不幸的是，许多早期的 ASN.1 规范是由 ISO 和 ITU-T 发布的。这两家机构有从纸质规范销售中获利的历史，因此在早期并没有提供机器可读取的文档。不过，一些相关标准和建议的编辑确实获得了许可，可以免费分发 ASN.1 的机器可读取版本（通常是以 ASCII 文本格式）。不过，这类资源的可用性并没有得到广泛的宣传。

```txt
001 Wineco-ordering-protocol
002 {joint-iso-itu-t internationalRA(23) set(42) set-vendors(9)
003 wineco(43) modules(2) ordering(1)}
004 DEFINITIONS
005 AUTOMATIC TAGS ::=
006 BEGIN
007
008 Order-for-stock ::= SEQUENCE
009 {order-no INTEGER,
010 name-address BranchIdentification,
.....
Figure 16: The module header 
```

It is unfortunate that many ASN.1 specifications have had to be re-keyed from printed copies for use in tools, with all the errors that can cause. The better tool vendors have built-up over time a stock of machine-readable specifications (either obtained from Editors or by re-keying themselves) for the most common protocols, and will supply these to their customers on request. (The URL in Appendix 5 provides a link to a list of many ASN.1-based specifications, and in some cases to sources of machine-readable specifications where these are known to exist.) 不幸的是，许多 ASN.1 规范都需要从打印版重新进行密钥生成，以便用于各种工具中，而这可能会导致各种错误。那些较为优秀的工具供应商随着时间的推移，已经积累了大量适用于机器阅读的规范文档（这些文档可能是从其他来源获得的，也可能是他们自己重新生成的）。这些供应商会根据客户需求向客户提供这些规范文档。（附录 5 中的链接提供了一个包含许多基于 ASN.1 的规范文档的列表，在某些情况下，还提供了已知存在此类机器可读规范的来源。）

## 3 Returning to the module header! 3. 回到模块头部部分！

## 3.1 Syntactic discussion 3.1 句法讨论

Figure 16 repeats the module header lines (with line numbers). 图 16 重复了模块头部信息的行内容（并标注了行号）。

Let us take the items in turn. The first line contains the module name, and is any ASN.1 name beginning with a capital letter. It is intended to identify the module and its contents for human-beings, and would normally be distinct from any other module name in the same application specification. This is not, however, a requirement, as ASN.1 has no actual concept of a complete application specification (only of a complete and legal module)! We return later to the question of a "complete specification". 让我们依次来看这些项。第一行包含了模块的名称，这个名称可以是任何以大写字母开头的 ASN.1 名称。它的作用是为了让人类能够识别该模块及其内容，通常会与同一应用程序规范中的其他模块名称区分开来。不过，这并不是必需的，因为 ASN.1 实际上并不存在一个完整的应用程序规范的概念（它只涉及一个完整且合法的模块而已）。我们稍后会再次讨论“完整规范”的问题。

<table><tbody><tr><td data-imt-p="1">The module header provides 模块头部信息已经提供完毕。</td></tr><tr><td data-imt-p="1">A module name 模块名称</td></tr><tr><td data-imt-p="1">A unique module identification 独特的模块识别</td></tr><tr><td data-imt-p="1">Definition of the tagging environment 标签环境的定义</td></tr><tr><td data-imt-p="1">Definition of the extensibility environment 可扩展环境的定义</td></tr></tbody></table>

The second/third line is called the module identifier, and is another case of an object identifier value. This name-form is required to be distinct from that of any other module - not just from those in the same application specification, but from any ASN.1 module ever-written or ever to-bewritten, world-wide! (Including - tho' some might say Figure 999 applies – any later version of this module.) 第二行或第三行被称为模块标识符，这也是一种对象标识符的表示方式。这种名称格式需要与任何其他模块的标识符区分开来——不仅需要与同一应用程序规范中的模块标识符区分，还需要与任何已编写或未来可能编写的 ASN.1 模块标识符区分。当然，虽然有些人可能会认为“图 999”这个名称仍然适用，但无论如何，这个模块标识符需要与其他所有模块标识符区分开来。

Strictly speaking, you don't need to include this second/third line. It was introduced into ASN.1 in about 1988, and was left optional partly for reasons of backwards compatibility and partly to take account of those who had difficulty in getting (or were too lazy to try to get!) a bit of the object identifier name space. 严格来说，并不需要包含这第二行或第三行内容。这一行内容大约在 1988 年被引入到 ASN.1 标准中，之所以成为可选内容，部分原因是出于与旧版本的兼容性考虑，部分则是为了照顾那些难以获取该对象标识符空间的人，或者干脆不想尝试去获取该空间的人。

It is today relatively easy to get some object identifier name-space to enable you to give worldwide unambiguous names to any modules that you write, but we defer a discussion of how to go about this (and of the detailed form of an object identifier value) to Section II. Suffice it to say that the object identifier values used in this book are "legitimate", and are distinct from others (legally!) used to name any other ASN.1 module in the world. If name-space can be obtained for this relatively unimportant book ....! 现在，要为所编写的任意模块分配全球范围内唯一且明确的名称，已经相对容易了。不过，关于如何实现这一点（以及对象标识符值的详细形式），我们会在第二部分进行讨论。值得一提的是，本书中使用的对象标识符值是“合法”的，并且与其他任何用于命名其他 ASN.1 模块的名称都不同。如果能够为这本相对不重要的书籍分配一个命名空间的话……

The fourth line and the sixth line are "boiler-plate". They say nothing, but they have to be there! No alternative syntax is possible. (The same applies to the "END" statement at the end of the module.) 第四行和第六行都是些千篇一律的、毫无意义的代码。它们什么都没有说，但必须存在才行！没有其他可行的语法可以替代它们。（同样的情况也适用于模块末尾的“END”语句。）

The fifth line is one of several possibilities, and determines the "environment" of the module that affects the detailed interpretation of the type-notation (but not of type-reference-names) textually appearing within the body of the module. 第五行是几种可能性中的一种，它决定了模块的“环境”，这会影响对模块内部出现的类型注释文本的详细解释（但不影响类型引用名称的解释）。

Designers please note: Not only is it illegal ASN.1 to write a specification without a module header and an "END" statement, it can also be very ambiguous because the "environment" of the type-notation has not been determined. 设计师们请注意：如果不包含模块头注释和“END”声明，就编写规范是完全非法的。此外，由于类型表示的“环境”尚未确定，这样的规范可能会非常模糊不清。

So ... what aspects of the "environment" can be specified, and what syntax is possible in this fifth line? 那么……在“环境”这个方面，可以指定哪些元素呢？在这第五行中，可以使用什么样的语法呢？

There are two aspects to the "environment", called (in this book) "the tagging environment" and "the extensibility environment". The reader will note that these both contain terms that we have briefly mentioned before, but have never properly explained! Please don't be disappointed, but the explanation here is again going to be partial - for a full discussion of these concepts you need to go to Section II. “环境”这个概念包含两个方面，在本书中分别被称为“标记环境”和“可扩展环境”。读者可能会注意到，这两个概念中有些术语之前已经简要提到过，但并未进行充分的解释。不过请不要失望，这里的解释仍然只是部分性的——要深入了解这些概念，请参考第二部分的内容。

The tagging environment (with the string used in line 4 to specify it given in parenthesis) is one of the following: 标记环境（第 4 行中用括号括起来的字符串表示）包括以下几种情况：

• An environment of explicit tagging (EXPLICIT TAGS). • 一个具有明确标签标识的环境（明确的标签标签）。

• An environment of implicit tagging (IMPLICIT TAGS). • 一种隐性标签化的环境（隐性标签）。

• An environment of automatic tagging (AUTOMATIC TAGS). • 自动标签化环境（自动标签）。

Omission of all of these implies an environment of explicit tagging. (This is for historical reasons, as an environment of explicit tagging was the only available tagging environment up to the 1988 specification). 忽略所有这些选项意味着需要采用显式标记的方式来处理数据。（这是出于历史原因，因为在 1988 年的规范制定之前，显式标记是唯一可用的标记方式。）

The extensibility environment (with the string used in line 4 to specify it given in parenthesis) is one of the following: 可扩展环境（第 4 行中使用的字符串用于指定该环境，括号内即为具体说明）包括以下几种情况：

• An environment requiring explicit extensibility markers (no mention of extensibility in line 4). • 需要一个明确的可扩展性标识的环境（第 4 行中没有提到可扩展性的概念）。

• An environment of implied extensibility markers (EXTENSIBILITY IMPLIED). • 一种包含隐含可扩展性的标记环境（可扩展性已隐含）。

We discuss these environments below. If both a tagging and an extensibility environment are being specified, the text for either one can come first. 我们在下文中会讨论这些环境。如果同时指定了标签化环境和可扩展性环境，那么可以先介绍其中任何一个环境的相关内容。

## 3.2 The tagging environment 3.2 标签标注环境

The treatment here leans heavily on the effect of tagging in a TLV-style encoding, and on BER in particular. It was to assist in such an encoding scheme that tagging was introduced into ASN.1. A more abstract treatment of tagging applicable to any encoding rules is given in Section II. 这里的处理方法主要依赖于在 TLV 风格的编码中对标签的使用，尤其是针对错误率问题。为了支持这种编码方式，才在 ASN.1 中引入了标签机制。关于适用于任何编码规则的更抽象化的标签处理方式，可以在第二部分中找到。

To look more closely at the effects of tagging, let us review a section from figure 13, repeated in figure 17. 为了更仔细地了解标记效果，让我们看一下图 13 中的一部分内容，这部分内容在图 17 中有所重复。

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/a0059080-59e4-4cd9-913b-34e7587e39f7/f92632cdb905fcb92ee7ccd610a45468e680a87601a75ce4342a4b3b49627228.jpg)

We have already noted that in BER a SEQUENCE is encoded as a TLV, with the "V" part being a series of TLVs, one for each element of the sequence. Thus the "overseas" element is a TLV, with the "V" part consisting of three TLVs, one for each of the three elements. We have also stated that the tag "\[1\]" over-rides the tag value in the outermost "T" for the "overseas" sequence. 我们已经注意到，在 BER 中，一个序列被编码为一个 TLV，而“V”部分则由一系列 TLV 组成，每个 TLV 对应序列中的一个元素。因此，“overseas”元素也是一个 TLV，其“V”部分由三个 TLV 组成，每个 TLV 对应序列中的三个元素。此外，我们还提到，标签“\[1\]”会覆盖最外层“T”中的标签值，从而影响“overseas”序列的内容。

Similarly, we have noted that the tag \[0\] and the tag \[1\] on the NULLs overrides the default tag on the TLV for each NULL. In this case, the encoding no longer contains the default tag for NULL, and the fact that this TLV does actually represent a NULL (or in other cases an INTEGER or a BOOLEAN etc) is now only implied by the tag in the "T" part - you need to know the type definition to recognise that \[0\] is in this case referring to a NULL. We say that we have "implicitly tagged the NULL". Similarly, the "overseas" "SEQUENCE" was implicitly tagged with tag "\[1\]". 同样，我们注意到，对于空值，标签\[0\]和标签\[1\]会覆盖 TLV 中的默认标签。在这种情况下，编码中不再包含空值的默认标签；而该 TLV 实际上代表一个空值（在其他情况下，也可能代表整数、布尔值等），这一点仅通过“T”部分中的标签来暗示——你需要了解类型定义，才能识别出\[0\]在这里指的是空值。我们可以说，我们“隐式地标记了空值”。同样地，所谓的“overseas”序列也被隐式地标记为标签"\[1\]"。

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/a0059080-59e4-4cd9-913b-34e7587e39f7/5d0af9e3e9438d9529ad3c2bb40b3caa41372d35d10e406a50ca190fd1e01a44.jpg)

But what about the tag we have placed on the "warehouse" "CHOICE"? There is a superficial similarity between "CHOICE" and "SEQUENCE" (they have almost the same following syntax), but in fact they are very different in their BER encoding. With "SEQUENCE", following elements are wrapped up in an outer-level TLV wrapper as described earlier, but with "CHOICE", we merely take any one of the TLV encodings for one of the alternatives of the "CHOICE", and we use that as the entire encoding (the TLV) for the "CHOICE" itself. 但是，我们给“warehouse”这个标签加上了“CHOICE”这个后缀，那该怎么办呢？虽然“CHOICE”和“SEQUENCE”在表面上有一些相似之处（它们的后续语法几乎相同），但实际上它们在 BER 编码上却有很大的差异。对于“SEQUENCE”来说，后续元素会被包裹在一个外部的 TLV 包装器中，就像之前描述的那样。而“CHOICE”则只是选择其中一个 TLV 编码作为“CHOICE”的整个编码方式，即直接使用那个编码来表示“CHOICE”本身。

Where does that leave the tagging of "warehouse"? Well, at first sight, it will over-ride the tag of the TLV for the "CHOICE" (which is either "\[0\]" or "\[1\]" depending on which alternative was selected) with the tag "\[2\]". Think for a bit, and then recognise that this would be a BUST specification! The alternatives were specifically given (by tagging the NULLs) distinct tags precisely so as to be able to know which was being sent down the line in an instance of communication, but now we are over-riding both with a common value ("\[2\]")! This cannot be allowed! 那么，“仓库”这个标签该放在哪里呢？乍一看，似乎应该用“\[2\]”来覆盖“CHOICE”这个标签的值——因为“CHOICE”的值取决于所选的替代方案，要么是“\[0\]”，要么是“\[1\]”。但仔细想想就会发现，这样做会导致规范失效！原本是通过为空值分配不同的标签来明确区分各种替代方案的，这样就能在通信过程中确定发送的是哪个选项。但现在，我们却用一个通用的值“\[2\]”来覆盖所有这些标签！这是不允许的！

To cut a long story short - two forms of tagging are available in ASN.1: 长话短说，在 ASN 中有两种标签格式可供使用：

implicit tagging: (this is what has been described so far), where the new tag over-rides the old tag and type information which was carried by the old tag is now only implicit in the encoding; this cannot be allowed for a "CHOICE" type; and 隐式标签标注：（这是目前所描述的机制）。在这种机制中，新的标签会覆盖旧的标签；而旧标签所携带的类型信息则仅以隐式方式存在于编码中；这种机制不适用于“CHOICE”类型的数据。

• explicit tagging: we add a new TLV wrapper specifically to carry the new tag in the "T" part of this wrapper, and carry the entire original TLV (with the old tag) in the "V" part of this wrapper; clearly this is OK for "CHOICE". • 明确的标签标注：我们新增了一个 TLV 包装器，用于在“T”部分携带新的标签；而原始的 TLV 信息则保留在“V”部分。显然，这种结构适用于“CHOICE”类型的数据。

Whilst implicit tagging is forbidden for "CHOICE" types (it is an illegal ASN.1 specification to ask for it), both implicit and explicit tagging can be applied to any other type. However, whilst explicit tagging retains maximum type information, and might help a dumb line-monitor to produce a sensible display, it is clearly more verbose than implicit tagging. 虽然对“CHOICE”类型的数据进行隐式标记是被禁止的（因为要求使用这种标记属于非法的 ASN 规范），但其他类型的数据则可以同时使用隐式标记和显式标记。不过，虽然显式标记能够保留最多的类型信息，并且可能有助于那些不熟练的用户也能理解地查看数据，但相比隐式标记，显式标记显然更加冗长。

<table><tbody><tr><td data-imt-p="1">implicit tagging - overrides the "T" part 隐式标签标注——会覆盖“T”这部分内容</td></tr><tr><td data-imt-p="1">explicit tagging - adds an extra TLV wrapper 明确标注——增加了一个额外的 TLV 封装层</td></tr></tbody></table>

Now, what do the different tagging environments mean? 那么，不同的标签环境究竟意味着什么呢？

## 3.2.1 An environment of explicit tagging 3.2.1 一个带有明确标签标识的环境

With an environment of explicit tagging, all tags produce explicit tagging unless the tag (number in square brackets) is immediately followed by the keyword "IMPLICIT". 在明确标记的环境中，所有的标签都会产生明确的标记效果，除非该标签（位于方括号中）后面直接跟着关键字“IMPLICIT”。

An environment of explicit tagging was the only one available in the early ASN.1 specifications, so it was common to see the word "IMPLICIT" almost everywhere, reducing readability. Of course, it was - and is - illegal to put "IMPLICIT" on a tag that is applied to a "CHOICE" type-notation, or to a type-reference-name for such notation. 在早期的 ASN.1 规范中，唯一可用的标签标注方式就是明确的标签标注。因此，几乎到处都可以看到“IMPLICIT”这个词，这降低了代码的可读性。当然，将“IMPLICIT”标注在适用于“CHOICE”类型标记的标签上，或者用于此类标记的类型名称上，是非法的行为——至今仍然如此。

## 3.2.2 An environment of implicit tagging 3.2.2 一种隐性标签化的环境

With an environment of implicit tagging, all tags are applied as implicit tagging unless one (or both) of the following apply: 在隐式标签的环境中，所有的标签都会被当作隐式标签来使用，除非满足以下情形之一：

• The tag is being applied to a "CHOICE" type-notation or to a type-reference-name for such notation; or • 该标签被应用于“CHOICE”类型的表示法，或者用于此类表示法的类型引用名称；或者

• The keyword "EXPLICIT" follows the tag notation. • 关键词“EXPLICIT”位于标签符号之后。

In the above cases, tagging is still explicit tagging. In practice most specifications written between about 1986 and 1995 specified an environment of implicit tagging in their module headers, and it was unusual to see either the keyword "IMPLICIT" or the keyword "EXPLICIT" after a tag. Occasionally, EXPLICIT was used for reinforcement, and occasionally (mainly in the security world to guarantee an extra TLV wrapper) on specific types within an environment of implicit taggin 在上述情况下，标签的标注仍然是明确的。实际上，大约在 1986 年到 1995 年期间编写的大部分规范都要求在模块头文件中使用隐式标签的标注方式。在标签后面出现“IMPLICIT”或“EXPLICIT”这样的关键词是比较罕见的。偶尔，EXPLICIT 一词会被用来作为补充说明；而在某些特定情况下（主要出现在安全领域，为了增加额外的 TLV 封装层），EXPLICIT 也会被使用。

<table><tbody><tr><td data-imt-p="1">An environment of implicit tagging only produces implicit tagging where it is legal - there is no need to say "EXPLICIT" on a "CHOICE". 仅限隐式标签化的环境会在符合法律要求的情况下实现隐式标签化——在“选择”选项中无需明确标注“显式”标签。</td></tr></tbody></table>

## 3.2.3 An environment of automatic tagging 3.2.3 自动标签化的环境

The rules about explicit and implicit tagging add to what is already a complicated set of rules on when tagging is needed, and in the 1994 specification, partly to simplify things for the application designer, and partly because the new Packed Encoding Rules (PER) were not TLV-based and made little use of tags, the ability to specify an environment of automatic 关于显性和隐性标签的规则，进一步增加了原本就复杂的标签使用规则体系。在 1994 年的规范中，制定这些规则的部分目的是为了简化应用程序设计者的操作，而另一原因是新的“打包编码规则”（PER）并非基于临时标签表设计的，因此很少使用标签。现在，人们可以指定一个自动处理的标签环境。

<table><tbody><tr><td data-imt-p="1">Automatic tagging 自动标记功能</td></tr><tr><td data-imt-p="1">Set up this environment and forget about tags! 创建这个环境后，就可以不再使用标签了！</td></tr></tbody></table>

tagging was added. 已经添加了标签功能。

In this case, tags are automatically added to all elements of each sequence (or set) and to each alternative of a choice, sequentially from "\[0\]" onwards (separately for each “SEQUENCE”, “SET”, or “CHOICE” construction). They are added in an environment of implicit tagging EXCEPT that if tag-notation is present on any one of the elements of a particular “SEQUENCE” (or “SET”) element or “CHOICE” alternative, then it is assumed that the designer has taken control, and there will be NO automatic application of tags. (The tag-notation that is present is interpreted in an environment of implicit tagging in this case.) 在这种情况下，标签会自动添加到每个序列（或集合）中的所有元素中，以及选择的每个选项上。这些标签是依次从“\[0\]”开始添加的，每个“序列”、“集合”或“选择”结构都是独立添加的。除了那些位于特定“序列”或“集合”中的元素或选项上的标签外，其余元素都处于隐式标签设置的状态。也就是说，如果某个元素或选项上有标签标记，那么设计师有权决定如何处理这些标签，因此不会自动应用标签。（此时，存在的标签标记会被视为处于隐式标签设置的状态而被处理。）

It is generally recommended today that "AUTOMATIC TAGS" be placed in the module header, and the designer can then forget about tags altogether! However (refer back to figure 999 please!), there is a counter-argument that "AUTOMATIC TAGS" can be more verbose than necessary in BER, and can give more scope for errors of implementation if ASN.1 tools are not used. You take your choice! But I know what mine would be! 目前普遍的建议是在模块头文件中添加“自动标签”，这样设计者就可以完全不再使用标签了！不过（请参考图 999！），也有相反的看法认为，在 BER 格式中，自动标签可能会过于冗长，而且如果未使用 ASN.1 工具的话，还可能导致实现上的错误。最终的选择还是取决于个人！不过，我知道我的选择会是什么！

## 3.3 The extensibility environment 3.3 可扩展性环境

We have already discussed the power of a TLVstyle of encoding to allow additions of elements in version 2, with version 1 specifications able to skip and to ignore such additional elements. (This extensibility concept actually generalises to things other than sequences and sets, but these are sufficient for now.) 我们已经讨论了 TLV 风格的编码方式在版本 2 中引入新元素时的优势。在版本 1 的规范中，可以跳过这些额外元素，或者忽略它们。这种可扩展性概念实际上可以应用于除序列和集合之外的其他对象，不过目前来说，这种扩展已经足够了。

## The extensibility marker 可扩展性标记

An ellipsis (or a pair) which identifies an insertion point where version 2 material can be added without affecting a version 1 system's ability to decode version 2 encodings. 省略号（或一对省略号）用于标识一个插入点，在该点上可以添加第二版本的内容，而不会影响第一版本的系统解码第二版本编码的能力。

If we are to retain some extensibility capability in ASN.1 and we are to introduce encoding rules that are less verbose than the TLV of BER (such as the new PER), then a designer's requirements for extensibility in his application specification have to be made explicit. 如果我们想要在 ASN.1 中保留一定的扩展性，并且希望引入一些比 BER 的 TLV 更简洁的编码规则（比如新的 PER），那么设计人员必须在他们的应用规范中明确说明对扩展性的需求。

We also need to make sure not only that encoding rules will allow a version 1 system to find the end of (and perhaps ignore) added version 2 material, but also that the application designer clearly specifies the actions expected of a version 1 system if it receives such material. 我们还必须确保，编码规则不仅能够让版本 1 的系统找到添加的版本 2 内容，并可能忽略这些内容；同时，应用程序的设计者也需要明确说明，当版本 1 的系统接收到此类内容时，应该执行哪些操作。

To make this possible, the 1994 specification introduced an extensibility marker into the ASN.1 notation. In the simplest use of this, 为了实现这一点，1994 年的规范在 ASN.1 表示法中引入了一个可扩展性标记。在最简单的应用中，这个标记的作用就是……

the type-notation "Order-for-stock" could be written as in figure 18. 这种类型符号“Order-for-stock”可以像图 18 中所展示的那样书写。

Here we are identifying that we require encoding rules to permit the later addition of outer-level elements between "urgency" and "authenticator", and additional enumerations, in version 2, without ill-effect if they get sent to version 1 systems. (Full details are in Section II.) (Should we have been happy to add the version 2 elements at the end after "authenticator", then a single ellipsis would have sufficed.) 我们认识到，需要一些编码规则来允许在“紧急程度”和“认证器”之间添加外部元素，以及在版本 2 中添加更多的枚举项。如果这些元素被发送到版本 1 的系统中，而不产生任何负面影响的话。（详细内容请参阅第二部分。）（如果在“认证器”之后直接添加版本 2 的元素，那么使用一个省略号就足够了。）

```txt
Order-for-stock ::= SEQUENCE
{order-no INTEGER,
name-address BranchIdentification,
details SEQUENCE OF
SEQUENCE
{item OBJECT IDENTIFIER,
cases INTEGER},
urgency ENUMERATED
{tomorrow(0),
three-day(1),
week(2), ... } DEFAULT week,
...
...
authenticator Security-Type}
Figure 18: Order-for-stock with extensibility markers 
```

The place where the ellipses are placed, and where new version 2 material can be safely inserted without upsetting deployed version 1 systems is called (surprise, surprise!) the insertion point. You are only allowed to have one insertion point in any given sequence, set, choice, etc. 那些放置省略号的位置，以及可以安全地插入新版本 2 内容而不影响已部署的版本 1 系统的位置，被称为“插入点”。在任何给定的序列、设置、选择等中，只允许有一个插入点。

The alert reader (you should be getting used to that phrase by now, but it is probably still annoying 这位警觉的读者（你应该已经习惯了这个称呼了，不过它仍然有点令人烦恼吧）

*   sorry!) will recognise that in addition to warning encoding rules to make provision, it is also necessary to tell the version 1 systems what to do with added material. In the case of new outerlevel elements, it may appear "obvious" that the required action would be to silently ignore the added elements. But what should a version 1 system do if it receives an "urgency" value that it 抱歉!)会认识到，除了遵循警告编码规则之外，还需要告诉版本 1 的系统如何处理新增的素材。对于新的外层元素来说，可能看起来“显而易见”的是，所需的操作就是忽略这些新增元素。但是，如果版本 1 的系统接收到“紧急”值，它应该怎么做呢？

Exception specification Specification of the behaviour of a version 1 system in the presence of added version 2 elements or values. 异常规范：描述在存在新增的版本 2 元素或值时，版本 1 系统行为的规范。

does not know about? There is a further piece of notation (section II again, I am afraid, if you want details!) called the exception specification which can be added immediately after the extensibility ellipsis. (The exception specification starts with an exclamation mark, so you will know it when you see it!). 不知道什么是？还有另一种标注方式（如果希望了解更多细节，可以再查看第二部分的内容！），叫做“异常说明”。这种说明可以紧接着可扩展性标记之后添加。（异常说明以感叹号开头，所以你看到它时就能认出它来！）

Application designers are encouraged to provide exception specifications when they use extensibility markers, although this has not been made mandatory. 虽然并没有强制要求，但应用程序设计者在使用可扩展标记时，被鼓励提供例外规格说明。

In an environment requiring explicit extensibility markers, the ellipsis, and any implications on encoding rules and version 1 behaviour which stem from the presence of an ellipsis, only occurs if the ellipsis is textually present in the specification wherever it is required. 在需要明确标注可扩展性的环境中，省略符号的使用，以及由于省略符号的存在而引发的编码规则与版本 1 行为的调整，都只有在规范文件中实际出现省略符号时才会发生。

In an environment of implied extensibility markers, all type-notations in that environment which do not already contain an extensibility marker in constructions where such markers are permitted automatically have one added at the end of the construction. 在存在隐含可扩展性的标记的环境中，所有不在允许使用此类标记的构造中包含可扩展性的标记的类型标记，都会自动在相应构造的末尾添加该标记。

So if the type-notation of figure 18 was in an environment of implied extensibility, an additional extension marker would be automatically inserted at the end of the "SEQUENCE{....}" construction in the "details" "SEQUENCE OF". 因此，如果图 18 的类型表示法处于一种隐式可扩展性的环境中，那么会在“details”部分“SEQUENCE{....}”结构末尾自动插入一个额外的扩展标记。

At the time of writing this text, extension markers are being extensively used, but few designers have chosen to specify an environment of implied extensibility markers, even tho' the cost of having additional, perhaps unnecessary, insertion points for the insertion of version 2 material is low in terms of bits on the line. 在撰写本文时，扩展标记已经被广泛使用了，但很少有设计师选择使用带有隐含可扩展性的标记环境。不过，在代码行数方面，为插入第二版本的内容而添加一些可能并不必要的额外标记点，其成本其实并不高。

Environment of implied extensibility markers: an environment where any construction without an extensibility marker (and which is allowed one) has one added (at its end). 隐含可扩展标记的环境：在这种环境中，任何不使用可扩展标记的构造（只要这种构造是允许存在的）都会在其末尾添加一个额外的标记。

The problem probably stems from three problems with using this environment: 这个问题可能源于使用这种环境时存在的三个问题：

• The insertion point is always at the end - you have no control over its position. • 插入点的位置总是位于文本的末尾——你无法控制它的位置。

• When producing the version 2 specification, you have to actually insert the ellipses explicitly before your added elements - and you might forget! • 在编写版本 2 的规范时，必须在添加元素之前明确插入省略号；不过，也有可能忘记这一点哦！

There is no provision (when this environment is used) for the presence of an exception specification with the extension marker, so all rules for the required behaviour of version 1 systems in the presence of version 2 elements or values have to be generic to the entire specification. 在这种环境下，没有相关条款规定可以使用异常指定符与扩展标记一起使用。因此，关于在版本 2 的元素或值存在时，版本 1 系统应具备的特性的所有规则，都必须适用于整个规范。

Concluding advice: Think carefully about where you want extension markers and about the handling you want version 1 systems to give to version 2 elements and values (using exception specifications to localise and make explicit those decisions), but do not attempt a blanket solution using an environment of implied extensibility. 最后的建议：请仔细考虑希望将扩展标记放置在哪里，以及希望第 1 版系统对第 2 版元素和值如何处理（通过异常规范来明确这些决策，以实现本地化处理）。但不要试图通过一种隐含的可扩展性的环境来解决问题。

## 4 Exports/imports statements 4 条进出口申报单

It has taken a lot of text to describe the effects of a six-line header! There is much less text in the ASN.1 Standard/Recommendation! But we are not yet done! 要描述六行标题的效果，需要大量的文字描述！而在 ASN.1 标准/建议书中，相关的文字内容要少得多。不过，我们的工作还远未结束！

Following the sixth line ("BEGIN") and (only) before any type or value assignment statements, we can include an exports statement (first) and/or an imports statement. These are usually regarded as part of the module header. 在进行任何类型或值的赋值操作之前，可以位于第六行（“BEGIN”行）之前，然后可以添加 exports 语句和/或 imports 语句。这些语句通常被视为模块头文件的一部分。

## Exports/Imports statements 进出口报表

A pair of optional statements at the head of a module that specify the use of types defined in other modules (import), or that make available to other modules types defined in this module (export). 在模块的开头有一对可选的语句，用于指定如何使用其他模块中定义的类型（导入），或者将本模块中定义的类型暴露给其他模块使用（导出）。

At this point it is important to highlight what has been only hinted at earlier: there is more in the ASN.1 repertoire of things that have reference names than just types and values, although these are by far the most important (or at least, the most prolific!) in most specifications. 此时，有必要强调一点：在 ASN.1 的规范中，其实还有更多具有参考名称的元素，而这些元素不仅仅是类型和值而已。不过，在大多数规范中，类型和值无疑是最重要的元素（或者至少是最常用的元素）。

Pre-1994 (only) we add macro names, and post-1994 we add names of information object classes, information objects, and information object sets. These can all appear in an export or an import statement, but for now we concentrate only on type-reference-names and value-reference-names. 在 1994 年之前，我们只添加宏名称；而在 1994 年之后，我们开始添加信息对象类、信息对象以及信息对象集合的名称。这些名称可以出现在导出或导入语句中，但目前我们只关注类型引用名称和值引用名称。

An exports statement is relatively simple, and is illustrated in figure 19, where we have taken our type definitions for "OutletType" and "Address", put them into a module of commonly used types, and exported them, that is to say, made them available for use in another module. 导出声明相对简单，如图 19 所示。我们在其中将“OutletType”和“Address”这两个类型定义放入一个通用类型模块中，从而将其导出，即让其他模块可以访问这些类型。

```txt
Wineco-common-types
{ joint-iso-itu-t internationalRA(23) set(42) set-vendors(9)
wineco(43) modules(2) common(3)}
DEFINITIONS
AUTOMATIC TAGS ::=
BEGIN

EXPORTS OutletType, Address;

OutletType ::= SEQUENCE
{ ....
.....
.... }
Address ::= SEQUENCE
{ ....
.....
.... }
......
END

Figure 19: The common types module (first attempt) 
```

In reality there would be more supporting types in "Wineco-common-types" which we are choosing not to export - they are not available for use in other modules. There would probably also be rather more types exported. 实际上，在“Wineco-常见类型”中还会有更多辅助类型，而我们选择不将这些类型进行输出；因为它们无法被其他模块所使用。很可能还会有更多类型的物品被输出。

Note the presence of the semi-colon as a statement terminator for the "EXPORTS" statement. We will see this being used to terminate the “IMPORTS” statement also. These are the only two cases where ASN.1 has a statement terminator. 请注意，在“EXPORTS”语句的末尾使用了分号作为语句的终止符。我们还会看到分号也被用来终止“IMPORTS”语句。这两种情况就是 ASN.1 中唯一使用语句终止符的地方。

Note also that for historical reasons (“EXPORTS” was only added in 1988) the omission of an “EXPORTS” statement has the semantics "everything is available for import by another module", whilst: 请注意，由于历史原因（“EXPORTS”这一选项直到 1988 年才被添加），省略“EXPORTS”声明时的含义是“所有内容均可被其他模块导入”。

Absence of an EXPORTS statements means "exports EVERYTHING". The statement "EXPORTS ;" means "exports NOTHING". 如果不存在“EXPORTS”报表，那就意味着“出口了所有东西”。而“EXPORTS;”这一表述则意味着“没有出口任何东西”。

## EXPORTS ; 出口；

has the semantics "nothing is available for import by another module". 它的语义是“没有其他模块可以导入该模块所依赖的变量或数据”。

Next we are going to assume that the "Security-Type" which we first used in Figure 13 is being imported from the Secure Electronic Transactions (SET) specification (a totally separate publication), and will be used in our "Wineco-common-types" module but also in our other modules. We import this for use in the "Wineco-common-types" module, but also export it again to make the imports clauses of our other modules simpler (they merely need to import from "Wineco-common-types"). This "relaying" of type definitions is legal. 接下来，我们将假设在图 13 中首次使用的“Security-Type”类型是从安全电子交易（SET）规范中导入的（这是一个完全独立的规范）。该类型将被用于我们的“Wineco-common-types”模块，同时也会应用于其他模块。我们导入这个类型是为了在“Wineco-common-types”模块中使用，但也会再次导出它，以便其他模块在导入时只需从“Wineco-common-types”模块中导入该类型即可。这种类型定义的“传递”方式是完全合法的。

```txt
Wineco-common-types
{ joint-iso-itu-t internationalRA(23) set(42) set-vendors(9)
    wineco(43) modules(2) common(3)}
DEFINITIONS
AUTOMATIC TAGS ::=
BEGIN

EXPORTS OutletType, Address, Security-Type;

IMPORTS Security-Type FROM
SET-module
{joint-iso-itu-t internationalRA(23) set(42) module(6) 0};

OutletType ::= SEQUENCE
{ ....
.....
.... }
Address ::= SEQUENCE
{ ....
.....
.... }
......

END

Figure 20: The common types module (enhanced) 
```

This changes figure 19 to figure 20. 这样就把图 19 改成了图 20。

As with EXPORTS, the text between "IMPORTS" and "FROM" is a comma separated list of reference names. We will see how to import from more than one other module in the next figure. 与 EXPORTS 的情况类似，IMPORTS 和 FROM 之间的文本也是一个用逗号分隔的引用名称列表。在下一个图中，我们将看到如何从多个其他模块中导入内容。

Note at this point that if a type is imported from a module with a particular tagging or extensibility environment into a module with a different tagging or extensibility environment, the type-notation for that imported type continues to be interpreted with the environment of the module in which it was originally defined. This may seem obvious from the way in which the environment concept was presented, but it is worth reinforcing the point - what is being imported is in some sense the "abstract type" that the type-notation defines, not the text of the type-notation. 需要注意的是，如果一个类型从一个具有特定标签或可扩展性的模块中被导入到另一个具有不同标签或可扩展性的模块中，那么该导入类型的类型表示方式仍然遵循该类型最初被定义的模块的环境。从描述环境概念的方式来看，这一点似乎显而易见，但仍有必要强调这一点——实际上被导入的其实是一个“抽象类型”，即类型表示方式所定义的抽象概念，而不是类型表示方式本身的文本。

## 5 Refining our structure 5. 优化我们的结构

## The final example 最后一个例子

We now use several modules, we have a CHOICE as our top-level type and we clearly identify it as our top-level type, We use an object identifier value-reference-name, we use APPLICATION class tags, we handle invalid encodings, we have extensibility at the toplevel with exception handling. We are getting quite sophisticated in our use of ASN.1! 我们现在使用了多个模块。我们将 CHOICE 作为我们的顶层类型，并明确将其标识为顶层类型。我们使用对象标识符值-引用-名称，使用 APPLICATION 类标签。我们能够处理无效的编码问题。在顶层结构方面，我们实现了可扩展性，同时加入了异常处理机制。我们在使用 ASN.1 方面越来越熟练了！

Now we are going to make quite a few changes! We will add a second top-level message (and make provision for more) called "Return-of-sales" defined in another module, and we will now include the “ABSTRACT-SYNTAX” statement (mentioned in Chapter 2) to define our new toplevel type in yet another module, that we will put first. 现在，我们将进行几项修改！我们会添加第二个顶层消息类型，名为“销售退回”，该类型定义在其他模块中。同时，我们还会在另一个模块中加入“抽象语法”声明（如第 2 章所述），以便在新模块中定义我们的新顶层类型。

We will do a few more cosmetic changes to this top-level module, to illustrate some slightly more advanced features. We will: 我们将对这个高层模块进行一些进一步的修改，以展示一些较为高级的功能。具体步骤如下：

use "APPLICATION" class tags for our top-level messages. This is not necessary, but is often done (see later discussion of tag classes) 我们使用“APPLICATION”类标签来标识顶层消息。虽然这不是必须的，但通常会这样做（关于标签类的更多讨论请参见后面的内容）。

• assign the first part of our long object identifiers to the value-reference-name "wineco-OID" and use that as the start of our object identifiers, a commonly used feature of ASN.1. • 我们将这些长对象标识符的第一部分命名为“wineco-OID”，并将其作为我们对象标识符的起始值。这是 ASN 中常见的做法。

add text to "ABSTRACT-SYNTAX" to make clear that if the decoder detects an invalid encoding of incoming material our text will specify exactly how the system is to behave. 在“摘要语法”部分添加文本，以明确说明：如果解码器检测到传入的编码数据存在错误，我们的文本将详细说明系统应有的行为方式。

The final result is shown in Figure 21, which is assumed to be followed by the text of Figure 20. Have a good look at Figure 21, and then read the following text that "talks you through it". 最终的结果如图 21 所示。预计图 21 之后会跟着图 20 的文字内容。请仔细查看图 21，然后阅读接下来的文字内容，它们会为您详细解释整个情况。

Lines 001 to 006 are nothing new. Note that in lines 10 and 13 we will use "wineco-OID" (defined in lines 015 and 016) to shorten our object identifier value, but we are not allowed to use this in the module header, as it is not yet within scope, and the object identifier value must be written out in full. 第 001 至第 006 行并不属于新的内容。请注意，在第 10 行和第 13 行中，我们将使用“wineco-OID”作为对象标识符的缩写形式（该标识符的定义位于第 015 行和第 016 行）。不过，我们不允许在模块头文件中使用这种缩写形式，因为目前它尚未被纳入支持范围，因此对象标识符的值必须完整书写。

Line 007 simply says that nothing is available for reference from other modules. 007 线路仅表示没有其他模块中有可供参考的内容。

```tcl
001 Wineco-common-top-level
002 { joint-iso-itu-t internationalRA(23) set(42) set-vendors(9)
003 wineco(43) modules(2) top(0)}
004 DEFINITIONS
005 AUTOMATIC TAGS ::= 
006 BEGIN
007 EXPORTS ;
008 IMPORTS Order-for-stock FROM
009 Wineco-ordering-protocol
010 {wineco-OID modules(2) ordering(1)}
011 Return-of-sales FROM
012 Wineco-returns-protocol
013 {wineco-OID modules(2) returns(2)};
014
015 wineco-OID OBJECT IDENTIFIER ::= 
016 { joint-iso-itu-t internationalRA(23)
017 set(42) set-vendors(9) wineco(43)}
018 wineco-abstract-syntax ABSTRACT-SYNTAX ::= 
019 {Wineco-Protocol IDENTIFIED BY
020 {wineco-OID abstract-syntax(1)}
021 HAS PROPERTY
022 {handles-invalid-encodings}
023 --See clause 45.6 --
}
024
025 Wineco-Protocol ::= CHOICE
026 {ordering [APPLICATION 1] Order-for-stock,
027 sales [APPLICATION 2] Return-of-sales,
028 ... ! PrintableString : "See clause 45.7"
029 }
030
031 END
--New page in published spec.
032 Wineco-ordering-protocol
033 { joint-iso-itu-t internationalRA(23) set(42) set-vendors(9)
034 wineco(43) modules(2) ordering(1)}
035 DEFINITIONS
036 AUTOMATIC TAGS ::= 
037 BEGIN
038 EXPORTS Order-for-stock;
039 IMPORTS OutletType, Address, Security-Type FROM
040 Wineco-common-types
041 {wineco-OID modules(2) common (3)};
042
043 wineco-OID OBJECT IDENTIFIER ::= 
044 { joint-iso-itu-t internationalRA(23)
045 set(42) set-vendors(9) wineco(43)}
046
047 Order-for-stock ::= SEQUENCE
048 { ....
.... } ....
.... BranchIdentification ::= SET
070 { ....
.... .... }
.... .... .... .... .... .... .... .... .... .... .... .... .... .... .... .... .... .... .... .... .... .... .... .... .... .... .... .... .... .... .... .... .... .... .... .... .... .... .... .... .... .... .... .... .... .... .... .... .... .... .... .... .... .... .... .... .... .... .... .... .... .... .... .... .... .... .... .... .... .... .... .... .... .... .... .... .... .... .... .... .... .. 
```

Lines 008 to 013 are the imports we were expecting from our other two modules. Note the syntax here: if we had more types being imported from the same module, there would be a comma separated list as in line 039, but when we import from two different modules lines 011 to 013 just run on from lines 008 and 010 with no separator. 第 008 行到第 013 行是来自其他两个模块的导入语句。注意这里的语法：如果我们从同一个模块中导入多个类型，就会像第 039 行那样使用逗号分隔的列表。但是，当从两个不同的模块导入时，第 011 行到第 013 行只是简单地在第 008 行和第 010 行之后继续运行，不需要使用分隔符。

Lines 015 and 017 provide our object identifier value-reference-name with a value assignment. It is a (very useful!) curiosity of the value notation for object identifiers that it can begin with an object identifier value-reference-name which "expands" into the initial part of a full object identifier value, and is then added to, as we see in lines 010, 013, and 020. If you want to jump ahead, and are interested, the OID tree is more fully described in Chapter 1 of Section II. 第 015 行和第 017 行为我们的对象标识符 value-reference-name 赋予了具体的数值赋值。对象标识符的表示方式有一个非常有趣的特点：它可以以对象标识符 value-reference-name 开头，这个开头部分会扩展为完整对象标识符值的初始部分，然后才会被添加到实际的值中，如第 010 行、013 行和 020 行所示。如果你想要深入了解，可以参阅第二部分第 1 章中对 OID 树的更详细描述。

Lines 018 to 023 are the "piece of magic" syntax that defines the top-level type, names the abstract syntax, and assigns an object identifier value to it - something which in older specifications would be done in human-readable text. In fact, this syntax is not "ad hoc" it is an example of an information object assignment statement which will be discussed in Section II. 018 到 023 行是“魔法条款”语法，用于定义顶层类型、指定抽象语法结构，并为其分配一个对象标识符值。在早期的规范中，这类定义通常是用人类可读的文本来描述的。实际上，这种语法并非“临时性的”，而是一种信息对象赋值语句的例子，相关内容将在第二部分中进行讨论。

The "HAS PROPERTY" and lines 22 to 23 is the only "property" that can be specified at present. The inclusion of this syntax is partly to counter an old OSI view-point that decoding was a separate layer from the application, and that if decoding failed to produce a recognised abstract value, all you could do was abort the connection! (Do check Figure 999 again!) Stupid idea! But including lines 20 to 23 reassures the reader that the specification does indeed contain (in clause 45.6) text to cover what to do in this case. “具有属性”以及第 22 到 23 行是目前唯一可以指定的“属性”字段。引入这一语法部分是为了反驳旧的 OSI 观点，即解码是一个独立于应用程序的层；如果解码未能产生可识别的抽象值，那么就只能终止连接了！（请再次参考图 999！）这种想法太愚蠢了！不过，第 20 到 23 行的内容确实让读者放心，因为规范中确实包含了第 45.6 条，规定了在这种情况下应采取的措施。

Lines 025 to 029 define the single-ASN.1-type that we need for our top-level messages to ensure that each encoding (of either or our main message types) is unambiguous. If we simply applied BER to the two types "Order-for-stock" and "Return-of-sales-data", we could (and probably would) get a bit-pattern used for a value of one type also being used as an encoding for a value of the other type. By forming a new CHOICE type, the rules for tag uniqueness of a CHOICE type solve this problem. Notice that we have used "AUTOMATIC TAGS" in line 005, so there was no need to add any tags in lines 026 and 027, but as a matter of personal preference and style, we chose to take complete control of the "T" value in the outermost TLV of our messages and make one an encoding of "\[APPLICATION 0\]" and the other of "\[APPLICATION 1\]", no matter what the original tags were. Some designers argue that this is helpful for hand-encoders - it is certainly irrelevant to those using a tool. Notice that the presence of tags in lines 026 and 027 disables automatic tagging for the CHOICE in line 025, temporarily replacing the tagging environment with an environment of implicit tagging. 第 025 行到第 029 行定义了我们需要使用的单类型 ASN.1 标签。通过这种方式，我们可以确保每种编码方式（无论是主要消息类型还是其他类型）都具有唯一性。如果我们简单地将 BER 算法应用于“Order-for-stock”和“Return-of-sales-data”这两种类型，那么很可能会得到一种模式，这种模式可以用于一种类型的值，同时又能作为另一种类型值的编码。通过创建一个新的 CHOICE 类型，我们可以解决标签唯一性的问题。注意，我们在第 005 行使用了“AUTOMATIC TAGS”这一标签，因此在第 026 行和第 027 行无需添加任何标签。不过，出于个人风格考虑，我们选择完全控制消息最外层 TLV 中的“T”值，使得一个标签被编码为“\[APPLICATION 0\]”，另一个标签被编码为“\[APPLICATION 1\]”，而不管原始标签是什么。一些设计师认为，这种方式对手动编码器来说是有帮助的——不过对于使用工具的人来说，这种机制显然并不重要。请注意，在 026 行和 027 行中，标签的存在使得 025 行中的 CHOICE 选项无法自动进行标记，从而暂时将标记环境转变为隐式标记环境。

Line 028 tells us that in version 2 we suspect we may need more outer-level messages, and that encoding rules must ensure that adding such messages does not prevent version 1 systems from correctly receiving messages that were in version 1. The exclamation mark and following material (the exception specification - described in detail in Section II) in line 028 tells us that clause 45.7 details the actions that a version 1 system should take if it receives messages added in version 2 (or later). 第 028 行告诉我们，在版本 2 中，我们怀疑可能需要更多外部级别的消息。同时，编码规则必须确保添加这些消息后，版本 1 的系统仍然能够正确地接收版本 1 中的消息。第 028 行中的感叹号以及随后的内容（即例外情况的详细说明——详见第二部分）表明，第 45.7 条详细规定了当版本 1 的系统接收到版本 2（或更高版本）中添加的消息时，它应该采取的行动。

Lines 032 to 101 are our second module (the development of the original Figure 13), and contain nothing new. Note, however, that lines 043 and 045 are a repetition of 015 to 017, and this might seem undesirable. It would have been possible to define "wineco-OID" in yet another module (with lots of other value-reference-names we might need), and to import that name from that module. However, we would not (for obvious "infinite recursion") reasons be allowed to use "wineco-OID" in the "FROM" for that import, so we would end up writing out as much text (and repeating it in each module where we wish to do the import) as we have written in lines 015 to 017 and 043 to 045. What we have is about as minimal as we can get. 第 032 行到第 101 行是我们的第二个模块（即原始 Figure 13 的扩展部分），其中并没有包含任何新的内容。不过需要注意的是，第 043 行和第 045 行实际上是第 015 行到第 017 行的重复，这种情况可能并不理想。其实可以将“wineco-OID”定义在另一个模块中（我们可以在这个模块中定义许多其他的值引用名称），然后从该模块导入这个名称。然而，由于“无限递归”的问题，我们不得不在导入时使用“FROM”语句来引用该模块中的“wineco-OID”定义。因此，我们最终需要写出与第 015 行到第 017 行以及第 043 行到第 045 行相同数量的文本。我们所做的这个设计已经尽可能简洁了。

Lines 102 to 139 are our third module, structurally the same as 032 to 101, and introducing nothing new. The whole specification then concludes with the text of Figure 20, giving our "common-type" module, which we have already discussed. 第 102 条到第 139 条是我们的第三个模块，其结构与第 032 条到第 101 条相同，没有引入任何新的内容。整个规范最后以图 20 的文字作为结尾，这便是我们已经讨论过的“通用类型”模块。

```txt
--New page in published spec.
102 Wineco-returns-protocol
103 { joint-iso-itu-t internationalRA(23) set(42)
104 set-vendors(9) wineco(43) modules(2) returns(2)}
105 DEFINITIONS
106 AUTOMATIC TAGS ::= 
107 BEGIN
108 EXPORTS Return-of-sales;
109 IMPORTS OutletType, Address, Security-Type FROM
110 Wineco-common-types
111 {wineco-OID modules(2) common (3)};
112
113 wineco-OID OBJECT IDENTIFIER ::= 
114 {iso identified-organization icd-wineco(10)}
115
116 Return-of-sales ::= SEQUENCE
117 { ....
.... .... }
.... ....
.... ....
.... ....
139 END
Figure 21 (last part):Last figure for this chapter! 
```

## 6 Complete specifications 6 份完整的规格说明

As was stated earlier, there is no concept in ASN.1 of a "complete specification", only of correct (complete) modules, some of which may include an "ABSTRACT-SYNTAX" statement to identify a top-level type (or which may contain a top-level type identified in human-readable text). 如前所述，在 ASN.1 标准中并不存在“完整规范”的概念。而是存在一系列正确的模块组合，其中一些模块可能包含“抽象语法”声明，用于标识顶级类型（或者包含以人类可读文本形式表示的顶级类型）。

In many cases if a module imports a type from some other module, the two modules will be in the same publication (loosely, part of the same specification), but this is not a requirement. Types can be imported from any module anywhere. 在许多情况下，当一个模块从另一个模块中导入某个类型时，这两个模块会属于同一个发布体系（广义上，就是同一个规范的一部分）。不过，这并不是必须的。类型可以从任何模块中导入。

Suppose we take a top-level type in some module, and follow the chain of all the type-referencenames it uses (directly or indirectly) within its own module, and through import and export links (again chained to any depth) to types in other modules. This will give us the complete set of types that form the "complete specification" for the application for which this is the top-level type, and the specifications of all these types have (of course) to be available to any implementor of that application and to any ASN.1 compiler tool assisting in the implementation. Purely for the purposes of the final part of this chapter of this book, this tree of type definitions will be called the application-required types. 假设我们取某个模块中的顶级类型，然后沿着该类型所使用的所有类型名称链进行遍历——这些名称链可以是在该模块内部直接或间接产生的，也可以通过导入和导出链接进一步延伸，直到其他模块中的类型。这样就能得到构成该顶级类型的完整类型集合。当然，所有这些类型的规范都必须能够被该应用的任何实现者以及任何用于辅助实现的 ASN.1 编译器工具所使用。为了本书本章的最后一部分的讨论目的，我们将把这种类型定义树称为“应用所需的类型”。

It is important advice to any application designer to make it very clear early in the text of any application specification precisely which additional (physical) documents are required to obtain the definitions of all the application-required types. 对于任何应用程序设计师来说，一个重要的建议是在应用程序规范的开头就明确说明，为了获得所有所需应用程序类型的定义，还需要哪些额外的（物理）文档。

But suppose we now consider the set of modules in which these application-required types were defined. (Again, purely for the next few paragraphs, we will call these the application-required modules). 但是，假设我们现在考虑一下那些定义了这些应用程序所需类型的模块集合。（同样，在接下来的几段中，我们仍将把这些模块称为“应用程序所需模块”。）

In general, the module textually containing the top-level type probably does not contain any types other than those which are application-required types (although there is no requirement that this be so). But as soon as we start importing, particularly from modules in other publications which were perhaps produced to satisfy more general requirements, then there are likely to be some types defined in application-required modules that are not application-required types! 一般来说，包含顶级类型的模块在文本描述中似乎只会包含那些属于应用所需类型的类型而已（尽管并没有强制要求必须如此）。不过，当我们开始从其他出版物中的模块导入内容时，那些属于应用所需类型的模块中可能会有一些并非应用所需类型的类型被定义进来！

As we shall see later, tools vary in their intelligence. There are some tools that require you to physically extract referenced types and put everything into the same module with the top-level type first! This is at the extreme bad end, and can give real problems if the tagging or extensibility environments of the different modules are different. 正如我们稍后会看到的，各种工具在智能方面存在差异。有些工具需要用户手动提取指定的类型，并将这些类型按照层级顺序放置在同一模块中！这种情况非常糟糕，如果不同模块的标签机制或可扩展性存在差异，就会引发实际问题。

The best tools will allow you to present them with machine-readable text (perhaps in several files) that contains all the application-required modules (and a directive identifying the top-level type), and will extract from those modules only the application-required types, mapping only those to data structures in your chosen programming language. (This keeps the memory requirement for the implementation to a minimum). 最好的工具能够让你使用机器可阅读的文本来呈现这些数据（可以分多个文件进行存储），其中包含了所有应用程序所需的模块，以及用于标识最高级别类型的指令。这些工具只会从这些模块中提取出真正需要的类型，并将这些类型映射到你选择的编程语言中的数据结构上。（这样就能将实现所需的内存占用降到最低。）

Remember the discussion you had with yourself earlier (as a potential application designer) about the pros and cons of referencing (importing) or textually copying types from other modules? You may re-open that discussion! 还记得你之前作为潜在的应用设计者，与自己进行的关于从其他模块引用或复制文本内容的利弊的讨论吗？你可以重新开启那次讨论吧！

## 7 Conclusion 7 结论

We have come a long way from our simple type assignments in Figure 13! 我们已经取得了巨大的进步，从图 13 中简单的类型分配方式已经发展到了今天！

The high-level structure of an ASN.1-based application specification has been described and explored, and most of the important concepts have now been introduced. 基于 ASN.1 的应用程序规范的高层次结构已经得到描述与探讨，现在大多数重要的概念也已经介绍完毕。

But a word of caution: the simple protocol we have used here for illustration would probably be better structured as the single-ASN.1-module outlined in Figure 14. The additional power (but complexity) of multiple modules with export/import is important for large specifications, but should not be used unnecessarily - keep it as simple as possible! If the Figure 14 structure will do, stay with Figure 14! 不过，有一点需要提醒：我们在这里用于示例的简单协议，其实可以整理成如图 14 所示的单个 ASN.1 模块。虽然多个模块结合导出/导入功能能带来更大的灵活性，但这种做法可能会增加复杂性。因此，除非绝对有必要，否则不要过度使用这种结构——尽量保持协议的简单性吧！如果图 14 的结构就足够了，那就继续使用图 14 的结构吧！

It now remains to complete the discussion of the ASN.1 type and value notations for the simple built-in types and the construction mechanisms (this is done in the next chapter), and (in Section II – with an introduction in the Chapter 5 of this section) to give a fuller treatment of the more advanced concepts we have mentioned, and to discuss more of the features added in 1994. 现在剩下的工作就是完成对 ASN.1 类型和数据表示方式的讨论。对于简单的内置类型以及相关的构造机制，我们将在下一章中进行详细讨论。（在第二部分——以及第 5 章的引言部分，我们将对更先进的概念进行更全面的处理。）此外，我们还将讨论 1994 年新增的一些功能。

The reader should, however, now be able to read and to understand the bulk of most real ASN.1 specifications produced before 1994, and to recognise the use of some features introduced in the 1994 ASN.1. Read on! 不过，现在读者应该能够阅读并理解 1994 年之前发布的大多数真实 ASN1 规范的内容，并且能够识别 1994 年引入的一些新功能。继续阅读吧！

# Chapter 4 The basic data types and construction mechanisms - closure 第四章 基本数据类型与构造机制——闭包

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

```txt
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

```txt
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

```txt
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

# Chapter 6 Using an ASN.1 compiler 第六章 使用 ASN 编译器

## (Or: What it is all about - producing the bits on the line!) （或者：到底是怎么回事——就是在生产线上下制造这些零件而已！）

## Summary: 总结：

This chapter: 这一章：

• describes approaches to implementation of ASN.1-defined protocols, • 描述了实现 ASN 定义的协议的方法。

• briefly describes what needs to be done if an ASN.1 compiler is not available, • 简要说明如果无法使用 ASN 编译器时，需要采取的措施。

• describes in detail the concept and operation of an ASN.1 compiler, • 详细描述了 ASN.1 编译器的概念和运作方式。

illustrates the implementation process (when using an ASN.1 compiler), with examples of programming language structures produced by the "OSS ASN.1 Tools" product, 介绍了实施流程（在使用 ASN.1 编译器时），并通过“OSS ASN.1 工具”产品生成的编程语言结构示例来加以说明。

• discusses what to look for when seeking a "best buy" in an ASN.1 compiler. • 讨论了在寻找合适的 ASN 编译器时应该注意哪些因素，以选出最优质的产品。

This chapter talks about implementation architectures, strategy, and so on. It is therefore inevitably incomplete and partial. The issues it discusses are not standardised, and different implementors will produce different approaches. It is also the case that what is "best" on one platform may well not be "best" on a different platform. 这一章讨论了实现架构、策略等方面的问题。因此，它不可避免地会存在不完整和片面之处。文中提到的这些问题并未得到标准化处理，不同的实现者可能会采用不同的方法。同样，某个平台上认为“最佳”的方案，在另一个平台上可能并不适用。

This chapter gives an insight into the implementation of protocols specified using ASN.1, but much of the detail depends on knowledge of programming languages such as C and Java, and knowledge of BER encodings that are covered in Section III. Nonetheless, those without such knowledge can still gain useful information from this chapter. But if you are not a programmer, read the next clause then skip the rest completely! 这一章介绍了如何使用 ASN.1 规范来实现各种协议的方法。不过，其中的许多细节需要了解 C 语言和 Java 等编程语言，以及第三章中提到的 BER 编码知识。不过，即使没有这些知识的人也能从这一章中获得一些有用的信息。如果你不是程序员，那么可以直接跳过这一章的内容吧！

## 1 The route to an implementation 1 实现该方案的路径

We discussed in Chapter 1 clause 5.6 (and illustrated Its all so simple with a compiler! it in figure 12) the implementation process using an ASN.1 compiler. Before reading this chapter, you 在第一章的 5.6 节中，我们讨论了使用 ASN 编译器进行实现的过程。如图 12 所示，整个过程其实非常简单。在阅读这一章之前，你们已经了解相关的基础知识了。

may wish to review that material. You simply "compile" your ASN.1 into a programming language of your choice, include the compiler output with application code that deals with the semantics of the application, (really) compile and link. Your own code reads/writes language datastructures, and you call ENCODE/DECODE run-time routines provided by the ASN.1 compiler vendor when necessary (and provide an interface to your lower layer APIs.) 你可能希望复习那些材料。你只需将 ASN.1 代码“编译”成你喜欢的编程语言，将编译输出结果与处理应用程序语义的应用程序代码结合在一起，然后进行真正的编译和链接过程。你的代码负责读写数据结构，而在必要时，你可以调用 ASN.1 编译器供应商提供的 ENCODE/DECODE 运行时例程（同时提供接口以与底层 API 进行交互）。

## 2 What is an ASN.1 compiler? 2. 什么是 ASN.1 编译器？

We all know what "a compiler" normally means - a programme that reads in the text of a programme written in a high-level language and turns it into instructions that can be loaded into computer memory and obeyed by some particular computer hard-ware, usually involving a further linkingloader stage to incorporate run-time libraries. 我们都知道“编译器”通常指的是什么——它是一种能够读取用高级语言编写的程序文本，并将其转化为计算机内存中的指令的程序。这些指令随后会被特定的计算机硬件执行。通常在这个过程中还需要经过进一步的链接和加载阶段，才能将运行时所需的库文件整合到程序中。

<table><tbody><tr><td data-imt-p="1">What does it mean to "compile" a datastructure definition? 所谓“编译”数据结构定义，究竟是什么意思呢？</td></tr></tbody></table>

But ASN.1 is not a programming language. It is a language for defining data structures, so how can you "compile" ASN.1? 但是，ASN.1 并不是一种编程语言。它是一种用于定义数据结构的语言，那么，如何“编译”ASN.1 代码呢？

The term compiler is a little bit of a misnomer, but was first used to distinguish very advanced tools supporting the implementation of ASN.1-defined protocols from early tools that provided little more than a syntax-checking and pretty-print capability. In the rest of this chapter, we will use the term "ASN.1-compiler-tool", rather than "compiler". “编译器”这个术语有点用词不当，它最初是用来区分那些能够实现 ASN.1 定义协议的非常高级的工具与那些仅具备语法检查和点状显示功能的早期工具。在本章的其余部分，我们将使用“ASN.1 编译器工具”这一术语，而不是“编译器”。

There are several ways of implementing a protocol defined using ASN.1. The three main options are discussed below. 实现使用 ASN.1 定义的协议有多种方法。下面将讨论三种主要的方式。

Write all necessary code to encode and decode values in an ad hoc way. This is only suitable for the very simplest ASN.1 specifications, and leaves you with the full responsibility for debugging your encoding code, and for ensuring that you have the ability to handle all options on decoding. (The same statement would apply to character-based protocols defined using BNF, where there are some tools to help you, but they do not provide anything like as much support as an ASN.1-compiler-tool with an ASN.1-based specification). We will not discuss this option further. 请编写所有必要的代码，以实现对值的编码和解码操作，且这种编码方式需要以自底优先的方式进行处理。这种方法仅适用于最简单的 ASN.1 规范。接下来，你需要自行负责调试编码代码，并确保能够处理解码过程中可能出现的所有情况。（对于使用 BNF 定义的基于字符的协议来说，虽然也有一些工具可以提供帮助，但它们所提供的支持远远不及基于 ASN.1 的规范所使用的编码工具。不过，我们不会进一步讨论这个选项。）

• Use a pre-built and pre-tested set of general-purpose library routines with invocations such as: • 使用一套预先构建并经过测试的通用库程序集，这些程序包括各种调用功能，例如：

 

$$
\text { encode\_untagged\_int (int\_val, output\_buffer) };
$$

However, the above is just about the simplest invocation you will get. In most cases you will also want to provide an implicit or explicit tag (of one of three possible classes), and for constructed types such as SEQUENCE, support in this way can become quite complex. This approach also only really works well with BER, where constraints are irrelevant and there is a relatively rigid encoding of tags and lengths. This approach pre-dated the development of ASN.1-compiler-tools, and is discussed a little further later. 不过，上述描述仅涉及了最简单的情形。在大多数情况下，你还需要在标签中明确或隐含地指定某个类别的标签。但对于像 SEQUENCE 这样的构造类型来说，这种处理方式可能会变得相当复杂。这种方法主要适用于 BER 类型，因为在这种类型中，约束条件并不重要，而且标签和长度的定义也相对固定。这种处理方式是在 ASN.1 编译器工具出现之前就已经被使用的了，后面会进一步讨论这一点。

Use an ASN.1-compiler-tool that lets you put values into a programming language datastructure corresponding to your ASN.1 type (and generated by the ASN.1-compiler-tool automatically from your ASN.1 type) and then make a single invocation of "encode" when you have all your values in place, to produce a complete encoding of the value of that type. This provides the simplest implementation, with the least constraints on the structure of the application code, and is the approach discussed most in this chapter. It works equally well for PER, DER and CER as it does for BER, and makes maximum use of tested and debugged code for all aspects of encoding. 使用一种 ASN.1 编译器工具，可以将数值存入与 ASN.1 类型相对应的编程语言数据结构中等价。这些数值是由 ASN.1 编译器工具根据 ASN.1 类型自动生成的。当所有数值都准备就绪后，只需调用一次“编码”函数，就能生成该类型数值的完整编码结果。这种实现方式最为简单，对应用程序代码的结构要求也最低，也是本章中经常讨论的方法。这种方法适用于 PER、DER 和 CER 等多种编码格式，并且能够充分利用经过测试和调试过的代码来进行编码处理。

However, remember that we usually have to decode as well as to encode. In the case of the third option (use of an ASN.1-compiler-tool), decoding is no more difficult than encoding. Run-time routines provided by the ASN.1-compiler-tool will take an encoding of the value of an ASN.1 type and set all the fields of the programming language data-structure corresponding to that type. 不过，请记住，我们通常需要进行解码和编码的操作。在第三个选项的情况下（使用 ASN.1 编译器工具），解码的过程并不比编码更困难。ASN.1 编译器工具所提供的运行时程序会处理 ASN.1 类型值的编码形式，并相应地设置该类型对应的编程语言数据结构中的所有字段。

With the middle option, encoding is basically a series of invocations of appropriate library routines, but for decoding there is the further problem of parsing the received bit-string into a treestructure of primitive values, and then tree-walking this parse tree to find the primitive values. Again, this is more easily possible with BER than with PER, because with BER the parse tree can be constructed without knowledge of the type of the value being decoded. 在中间选项中，编码本质上就是一系列对相应库函数的调用。而解码则涉及到将接收到的位串解析成一种树形结构，然后遍历这个树形结构来找到各个基本值。同样，使用 BER 这种方式比使用 PER 更容易实现这一点，因为在使用 BER 时，可以在不知道要解码的值的类型的情况下构建出解析树。

The use of a library of encode routines and of a parse tree are discussed further below (briefly), but the chapter concentrates mainly on the use of an ASN.1-compiler-tool, as this provides a simple approach to implementation of ASN.1-based specifications, with effectively a 100% guarantee (assuming the ASN.1-compiler-tool is bug-free!) that: 下面会简要讨论如何使用编码例程库和解析树。不过，本章主要关注的是使用 ASN.1 编译器工具来实现基于 ASN.1 的规范。因为该工具提供了一种简单的实现方式，而且几乎可以百分之百地保证实现的正确性（前提是 ASN.1 编译器工具没有漏洞！）

• Only correct encodings of values will be produced. • 只会生成正确的值编码形式。

• No correct encoding will "blow" the decoder, values being correctly extracted from all possible correct encodings. • 没有任何一种正确的编码方式会导致解码器出现错误，所有正确编码后的数据都能被正确提取出来。

As an illustration of what ASN.1-compiler-tools produce, we will use a part of our wineco specification, that for "Return-of-sales", which references "Report-item". These were first shown in Figure 22 (part 2) in Chapter 4 of this section, and are repeated here without the comments. The C and Java structures and classes produced by the "OSS ASN.1 Tools" product (a good example of an ASN.1-compiler-tool product) are given in Appendices 3 and 4, and those familiar with C and Java may wish to compare these structures and classes with figure 28. (The "OSS ASN.1 Tools" product also provides mappings to C++, but we do not illustrate that in this book – it is too big already!) 作为展示 ASN.1 编译器工具所生成的结果的一个例子，我们将使用 wineco 规范中的一部分内容。这部分内容涉及到“销售退回”功能，而“销售退回”功能又依赖于“报告项目”。这些结构在本书第 4 章的第 2 部分中有描述，这里直接呈现出来，没有添加注释。由“OSS ASN.1 工具”生成的 C 语言和 Java 语言的结构与类在附录 3 和附录 4 中有详细说明。对于熟悉 C 语言和 Java 编程的人来说，或许可以将这些结构与图 28 进行比较。（“OSS ASN.1 工具”还提供了与 C++语言的映射关系，但本书并未对此进行展示——因为内容太多，无法一一介绍。）

```txt
Return-of-sales ::= SEQUENCE
{version BIT STRING
{version1 (0), version2 (1)} DEFAULT {version1},
no-of-days-reported-on INTEGER
{week(7), month (28), maximum (56)} (1..56)
DEFAULT week,
time-and-date-of-report CHOICE
{two-digit-year UTCTime,
four-digit-year GeneralizedTime},
reason-for-delay ENUMERATED
{computer-failure, network-failure, other} OPTIONAL,
additional-information
SEQUENCE OF PrintableString OPTIONAL,
sales-data SET OF Report-item,
... ! PrintableString : "See wineco manual chapter 15" }
Report-item ::= SEQUENCE
{item OBJECT IDENTIFIER,
item-description ObjectDescriptor OPTIONAL,
bar-code-data OCTET STRING,
ran-out-of-stock BOOLEAN DEFAULT FALSE,
min-stock-level REAL,
max-stock-level REAL,
average-stock-level REAL}
Figure 28 - An example to be implemented 
```

## 3 The overall features of an ASN.1-compiler-tool 3. ASN.1 编译工具的整体特性

An ASN.1-compiler-tool is composed of a "compiler", application-independent programming language text to be included with your implementation (for C, this is .H and .C files), and libraries to be linked into your final executable. For some platforms, the compiler may also emit text which has to be compiled to produce a DLL which will be used at run-time. 一个 ASN.1 编译器工具由三部分组成：编译器、与应用程序无关的编程语言代码（这些代码需要被包含在你的实现中，对于 C 语言来说，就是.H 和.C 文件），以及需要链接到最终可执行文件中的库。在某些平台上，编译器还会生成一些文本文件，这些文本文件需要在运行时被编译成 DLL 文件来使用。

<table><tbody><tr><td data-imt-p="1">This does it all. Take your ASN.1 type. "Compile" it into a language data-structure. Populate it with values. Call ENCODE. Done! Decoding is just as easy. 这就完成了整个过程。将你的 ASN.1 类型数据“编译”成一种语言的数据结构，然后填充一些值进去。最后调用 ENCODE 函数即可！解码过程同样简单。</td></tr></tbody></table>

The overall pattern is that the "compiler" phase takes in ASN.1 modules, and produces two main outputs. These are: 整体来看，所谓的“编译器”阶段会接收 ASN.1 模块作为输入，并生成两个主要输出。这两个输出分别是：

Data-structure definitions (for the language you have chosen) that correspond to the ASN.1 type. 与 ASN 类型相对应的数据结构定义（针对您所选的语言）。

Source text (for the language you have chosen) which will eventually produce either tables or code which the run-time routines in the supplied libraries can use to perform encode/decode operations, given only pointers to this information and to the in-core representation of the values to be encoded (and a handle for the buffer to encode into). This text includes all details of tagging in your ASN.1 types, so you never need to worry about tags in your implementation code. 您所选语言的源文本最终会生成表格或代码，这些代码可以由提供中的库中的运行时程序使用，以执行编码/解码操作。只需提供对这些信息的指针，以及待编码值的内部表示形式，以及用于编码的缓冲区句柄即可。该文本包含了关于 ASN.1 类型中标签的所有细节，因此您在实现代码中无需担心标签方面的问题。

For some platforms, the situation can be just a bit more complex. The compiler may output text which you must compile to produce a DLL for use by your application. 对于某些平台来说，情况可能会稍微复杂一些。编译器可能会输出一些文本，这些文本需要经过编译后才能生成可用于应用程序的 DLL 文件。

The next section looks at the use of a simple library of encode/decode routines, and then we look at the output from the "compiler" part of the "OSS ASN.1 Tools" compiler and the use of that tool. 下一节将介绍如何使用一个简单的编码/解码程序库，然后我们会探讨“OSS ASN.1 工具”编译器的输出结果，以及如何使用该工具。

## 4 Use of a simple library of encode/decode routines 4. 使用一个简单的编码/解码程序库

The earliest support for ASN.1 implementations (after simple syntax checkers and "pretty print" programs had been produced) was a library of routines that helped in the generation of BER tag (identifier) fields, BER length fields, and the encoding of BER primitive types. 最早对 ASN.1 实现的支持，是在简单的语法检查器和“漂亮打印”程序之后出现的。这些支持包括一系列帮助生成 BER 标签（标识符）字段、BER 长度字段，以及 BER 基本类型编码的库函数。

A library of encode/decode routines (one for each ASN.1 type) is better than nothing. But complications arise in the handling of nested SEQUENCE types etc, particularly in relation to length fields. 虽然拥有一系列编码/解码例程（每种 ASN.1 类型对应一个例程）总归是好的做法，但在处理嵌套的序列类型时就会遇到一些复杂的问题，尤其是在与长度字段相关的处理上。

Some implementations today still use this approach. It is better than doing everything from scratch! 目前仍有一些实现方式采用这种策略。相比从头开始构建一切来说，这种方式确实更优！

The approach is described in terms of a BER encoding. For a PER encoding it tends to work rather less well, and the ASN.1-compiler-tool approach would be more appropriate here. 这种方法的实现是通过 BER 编码来实现的。而对于 PER 编码来说，其效果则相对较差一些。因此，在这里更适合使用 ASN.1 编译器工具来实现相应的功能。

## 4.1 Encoding 4.1 编码

Encoding of untagged primitive items is trivial - but add tagging and add constructed types with nesting of SEQUENCE OF within SEQUENCE within another SEQUENCE OF (etc), and .... well, life is not quite so simple if all you have available is a library that just does identifier and length encodings for you (and encodings of primitive values). 对于未标记的原始数据项的编码其实很简单——但是，当引入标记机制后，就需要创建复杂的类型结构，比如将多个元素按顺序排列在一个序列中，而每个序列又可以包含另一个序列等等。不过，如果可用的工具只有那些只能进行标识符和长度编码的库，那么事情就变得复杂多了（因为它们也无法处理原始值的编码问题）。

Encoding using a library of routines can get messy, because you often need to know the length of an encoding before you encode it! 使用库中的例程进行编码可能会变得复杂，因为通常你需要在编码之前就知道编码的长度！

Before the emergence of ASN.1-compiler-tools, a common approach to encoding a sequence such as "Report-item" (see Figure 28) would be to have code looking something like Figure 29 (using pseudo-code). 在 ASN.1 编译器工具出现之前，对诸如“报告项”这样的序列进行编码的常见方法，就是使用类似图 29 所示的伪代码来进行编码。

```txt
Get value for "item" into x1
encode-oid (x1, buffer_x[1])
Get value for "item-description" into x2
encode_obje_desc (x2, buffer_x[2])
Get "bar-code-data" into x3
encode_octet_str (x3, buffer_x[3])
Get "ran-out-stock" value into x4
IF x4 is true THEN
    encode_boolean (true, buffer_x[4])
ELSE
    Set buffer_x[4] to an empty string
END IF
...
etc, encoding the last item into buffer_x[7] say.
...
encode-sequence (buffer_x, 1, 7, buffer_y)
-- This encodes the contents of buffer_x from 1 to 7
-- into buffer_y with a "SEQUENCE" wrapper.
-- Note that in practice the SEQUENCE may be tagged
-- resulting in a more complicated calling sequence
Pass buffer_y to lower layers for transmission.
Clear buffer_x, buffer_y

Figure 29 - Pseucode to encode "Report-item" 
```

Here we assume we have routines available in a library we have purchased that will take a value of any given ASN.1 primitive type (using some datatype in the language capable of supporting that primitive type) and returning an encoding in a buffer. Finally, we call another library routine that will put all the buffers together (note the copying that is involved here) and will generate the "T" and the "L" for a SEQUENCE (assuming we are using BER), returning the final coding in buffer\_y. 在这里，我们假设有一个我们购买的库中的函数可用，该函数能够接受任何给定的 ASN.1 基本类型的值（使用语言中能够支持该基本类型的数据类型），并返回一个编码结果到缓冲区中。最后，我们调用另一个库函数，它将把所有缓冲区中的编码结果合并起来（注意这里涉及到数据的复制操作），并生成 SEQUENCE 的“T”和“L”部分（假设我们使用的是 BER 编码方式），最终将完整的编码结果返回到 buffer\_y 中。

Clearly, if we have more complex nested structures in our ASN.1, this can become quite messy unless we are using a programming language that allows full recursion. We have effectively hardwired the ASN.1 structure into the structure of our code, making possible changes to version 2 of the protocol more difficult. 显然，如果我们使用的 ASN.1 结构包含更复杂的嵌套结构，那么情况就会变得非常混乱，除非我们使用的是支持完全递归的编程语言。实际上，ASN.1 结构已经硬编码在了我们的代码中，这就使得对协议版本 2 的修改变得更加困难。

There are some things that can be done to eliminate some of the copying. Part of the problem is that we cannot generate the BER octets for the length octets of a SEQUENCE until we have encoded all the elements of that sequence and counted the length of that encoding. 有一些方法可以消除一些复制现象。问题的部分原因在于，在编码完序列中的所有元素并计算出编码的长度之后，我们才能生成与序列长度相关的 BER 字节。

For encoding a SEQUENCE there are (at least!) four ways to reduce/eliminate this problem of having to copy encodings from one buffer to another. These are: 对于序列的编码，至少有四种方法可以解决需要不断复制编码数据的问题。这些方法包括：

Do a "trial encoding" which just does enough to determine the length of each element of the sequence (this really needs to be a recursive call if our structure involves many levels of SEQUENCE or SEQUENCE OF), then generate the SEQUENCE header into the final buffer, then encode each of the SEQUENCE elements into that buffer. 进行“试验性编码”，仅对序列中的每个元素的长度进行适当确定（如果我们的结构包含多个层次的序列，那么这种操作需要递归调用）。然后将序列头信息写入最终缓冲区，接着将每个序列元素编码到该缓冲区中。

• Use the indefinite length form, in which case we can generate the sequence header into our final buffer and then encode into that buffer each of the elements of the sequence, with a pair of zeros at the end. • 使用不定长度的形式来表示数据。这样，我们可以将序列头部分放入最终缓冲区中，然后将该缓冲区中的各个元素进行编码，最后在每個元素的末尾加上两个零。

• Use the "trick" of allocating space for a long-form length encoding which is a length of length equal to 2, followed by two blank octets that we will fill in later once the length is known, and then encode each element into the same final buffer. • 采用“技巧”，为长格式编码分配空间：首先是一个长度为 2 的字节，接着是两个空白八位元，这些空白八位元在知道总长度之后再进行填充。然后，将每个元素编码到同一个最终缓冲区中。

• Use (assuming it is available!) a "gather" capability in the interface to lower layer software which enables you to pass a chain of buffers to that software, rather than a single contiguous piece of memory. • 使用接口中的“收集”功能（假设该功能可用！），将一系列缓冲区传递给下层软件。这样就能让软件处理多个缓冲区，而不是只处理一块连续的内存区域。

These approaches have been shown to work well for BER, but for CER/DER/PER, they can be either not possible (CER/DER demands minimum octets for length encoding) or more difficult/complex. 这些方法在处理 BER 问题时效果不错，但在处理 CER/DER/PER 问题时，要么无法实施（因为 CER/DER 需要至少一定数量的八位元来进行长度编码），要么实施起来更加困难且复杂。

## 4.2 Decoding 4.2 解码

Decoding using library routines is not quite so easy. You need a general-purpose parser - relatively easy for BER (less easy for PER), tree-walking code, and then the basic decode routines for primitive types. This rather parallels what you have to do with character-based encodings - but with character-based encodings you need a quite sophisticated tool to split the incoming character string (based on input of the 使用库中的例程进行解码并不容易。你需要一个通用的解析器来处理 BER 编码（对于 PER 编码则难度更大），还需要能够执行树遍历操作的代码，以及用于处理基本类型的数据的基本解码例程。这与基于字符的编码方式类似——不过在基于字符的编码中，你需要一个相当复杂的工具来拆分输入的字符字符串（这需要基于一定的输入条件）。

For decoding you need a generalpurpose parser, then you tree-walk. The library approach is easier with BER than with PER as the TLV structure is independent of the datatype. 进行解码时，你需要一个通用类型的解析器，然后按照树形结构进行遍历。与 PER 相比，使用 BER 进行库级处理更为简单，因为 TLV 结构与数据类型无关。

BNF) into a tree-structure of "leaf" components for processing. Producing a parse tree of BER is rather easier. 将 BNF 数据转换为“叶节点”构成的树形结构，以便进行处理。而生成 BER 的解析树则相对容易一些。

In general, use of a simple library of encode-decode routines with ASN.1 is neither complex nor more simple than use of parsers for character-based protocols defined using BNF, although it is arguable that the original ASN.1 definition is more readable to a "layman" than a BNF description of a character-based protocol. 总体而言，使用基于 ASN.1 的简单编码解码库并不复杂，其使用方式也不比使用基于 BNF 定义的字符协议解析器更为简单。不过，可以说，与基于 BNF 描述的字符协议相比，原始 ASN.1 定义对于普通用户来说更易于理解。

It is also the case that parsing an incoming BER encoding into a tree-structure (where each leaf is a primitive type) is a great deal easier than producing a syntax tree from a character-based encoding defined using BNF. 此外，将输入的 BER 编码解析成树形结构（其中每个叶子节点代表一种基本类型）要比从基于 BNF 定义的字符编码中生成语法树要简单得多。

Decode implementations for BER can take advantage of the use of bit 6 of the identifier octets to identify whether the following "V" part is constructed, enabling application-independent code to produce a tree-structure with primitive types at the leaves. That tree-structure is then "walked" by the application-specific code to determine the values that have been received. 在 BER 解码实现中，可以利用标识符字节的第 6 位来标识后续的“V”部分是否由某种结构构成。这样，与应用无关的代码就能生成具有树状结构的代码，其中基本类型位于树的叶子位置。然后，应用程序特定的代码可以遍历这个树状结构，以确定已经接收到的数值。

This "library of useful routines" approach is certainly better than doing everything from scratch! But things are so much simpler with an ASN.1-compiler-tool as described below. 这种“实用程序库”式的解决方案，显然比从头开始构建一切要更优！而使用下面描述的 ASN.1 编译器工具的话，事情就会简单得多。

## 5 Using an ASN.1-compiler-tool 5. 使用 ASN.1 编译器工具

## 5.1 Basic considerations 5.1 基本考虑因素

An ASN.1-compiler-tool makes everything much more of a one-step process (for the user of the tool). All the decisions on how to encode (copying buffers, doing trial encodings, using indefinite length, using long-form definite length with a length of two) are buried in the run-time support of the ASN.1-compiler-tool, as are the mechanisms for parsing an incoming encoding into components that can then be placed into memory in a 一个 ASN.1 编译工具让整个过程变得更加简单，用户只需一步操作即可完成。关于如何编码的所有决策（如复制缓冲区、尝试不同编码方式、使用不定长度或固定长度但长度为 2 等），都隐藏在 ASN.1 编译工具的运行时支持中。而解析输入编码并将其分解为可存储于内存中的各个组件的过程，也由该工具负责处理。

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/a0059080-59e4-4cd9-913b-34e7587e39f7/9618460df4096b78044f561048c2fe35916b905f1069a78938e5986454bc2a57.jpg)

form which matches a programming-language data-structure. 一种与编程语言中的数据结构相匹配的格式。

ASN.1-compiler-tools are specific to a given platform (meaning hardware, operating system, programming language, and perhaps even development environment) and you will need to find one that is available for the platform that you are using. If you are using C, C++, or Java, on commonly used hardware and operating systems you will have no problem, but if you are locked into some rather archaic language (sorry if I sound rude!), life may be more difficult. ASN.1 编译器工具通常是针对特定平台设计的（即针对特定的硬件、操作系统、编程语言，甚至开发环境）。因此，你需要找到适用于你所使用平台的编译器工具。如果你使用的是 C、C++或 Java 语言，并且在常见的硬件和操作系统上运行，那么选择相应的编译器工具应该不会有问题。不过，如果你使用的是一些较为古老的编程语言，情况可能会比较棘手（如果我的话听起来有些无礼的话，请见谅！）。

A particular product may support several of these languages in one software package, using "compiler directives", or you may have to pay for several versions of a product if you want support for multiple platforms (C and Java, say). In some cases "cross-compilation" (which some ASN.1-compiler-tools support) can provide implementation support on older platforms. Basically, you need to "filter" available tools according to whether they can support directly or through crosscompilation the platform you want/need to use, then choose the "best" (see later section in this chapter). 某种特定产品可以通过“编译指令”在同一个软件包中支持多种语言。或者，如果你希望支持多个平台（比如 C 语言和 Java），那么可能需要购买该产品的多个版本。在某些情况下，交叉编译技术（一些 ASN.1 编译器工具支持这一功能）可以确保在旧平台上也能使用该产品的功能。基本上，你需要根据工具是否能够直接支持目标平台，还是需要通过交叉编译来支持目标平台，来筛选出最合适的工具。关于这一点，请参考本章后面的章节。

"Want/need" is important here. Sometimes the implementation platform is fixed and almost impossible to change for either historical reasons or for reasons of company policy, but more often, there are costs associated with the use of different platforms (procurement of hardware which is not "in-company", training costs of programmers, etc etc) which must be balanced against the "quality" (and cost) of available tools for these platforms. “想要/需要”在这里非常重要。有时候，由于历史原因或公司政策的原因，某些实施平台是固定不变的，很难进行更改。但更常见的情况是，使用不同平台会带来一些成本开销（比如需要采购非公司自有的硬件设备，程序员培训费用等），这些成本必须与这些平台所提供的工具“质量”和“成本”相权衡。

## 5.2 What do tool designers have to decide? 5.2 工具设计师需要做出哪些决策呢？

There are three very critical decisions in the design of a good ASN.1-compiler-tool - how to map ASN.1 data-structures to programming-language datastructures, how to make CPU/memory trade-offs in the overall run-time support, and how to handle memory allocation and buffer management during encode/decode operations. But other important 在设计一个优秀的 ASN1 编译器工具时，有三个非常关键的决策需要考虑：如何将 ASN1 数据结构映射到编程语言中的数据结构；如何在整体运行时间范围内进行 CPU 和内存资源的优化分配；以及在编码/解码操作过程中如何处理内存分配和缓冲区管理问题。不过，还有其他一些重要的因素也需要考虑。

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/a0059080-59e4-4cd9-913b-34e7587e39f7/f19f6c3bf8d6ef1b46d1d516810ba7b70471713b61e2fb652cc75c5960f52347.jpg)

decisions are how much user control, options, and flexibility to provide in these areas. All of these factors contribute to the "quality" of any particular tool. 决策决定了在这些领域用户可以拥有多大的控制权、选择余地以及灵活性。所有这些因素共同影响着某个工具的“质量”。

The designers of the ASN.1-compiler-tool will have made some important decisions. We will see later that the quality of these decisions very much affects the quality of the ASN.1-compiler-tool (and the ease and flexibility with which you can use it to help you to produce protocol implementations). ASN.1 编译器工具的设计者们已经做出了一些重要的决策。我们稍后会看到，这些决策的质量直接影响到 ASN.1 编译器工具的整体性能（以及用户使用它来编写协议实现时的便捷性和灵活性）。

The most important areas they have had to address (and which affect the quality of the resulting ASN.1-compiler-tool) are: 他们必须解决的最重要的几个问题（这些问题会影响最终生成的 ASN.1 编译器工具的质量）包括：

• How to map ASN.1 into programming-language data-structures? • 如何将 ASN.1 格式的数据映射到编程语言的数据结构之中呢？

• What are the right trade-offs between run-time encoding/decoding speed and memory requirements? • 在运行时编码/解码速度与内存需求之间，应该如何进行合理的权衡呢？

• How to handle memory allocation when performing encode and decode operations? • 在执行编码和解码操作时，如何处理内存分配问题？

• How much user control should be provided (and how - global directives or local control) on the behaviour of the tool for mappings and for run-time operation? • 应该提供多少用户控制权限？是通过全局指令还是局部控制来实现呢？关于映射功能的工具行为以及运行时的操作，又该如何进行控制呢？

None of these decisions are easy, but the best tools will provide some degree of user control in all these areas, through the use of "compiler directives", ideally both in terms of global default settings as well as specific local over-rides. (For example, for two-octet, four-octet, or truly indefinite-length integers). 这些决策都不容易做出，但最好的工具能够为用户在这些领域提供一定程度的控制权，这可以通过使用“编译指令”来实现。理想情况下，这些指令既包括全局默认设置，也包括具体的局部调整选项。（例如，对于两位数、四位数或真正长度不固定的整数来说，都可以使用相应的指令进行设置。）

## 5.3 The mapping to a programming-language data structure 5.3 映射到一种编程语言的数据结构

The designers of the ASN.1-compiler-tool will have determined a mapping from any arbitrarily complicated set of ASN.1 types into a related (and similarly complicated) set of datatypes in your chosen language. And they will have written a program (this is the bit that is usually called the "compiler") which will take in the text of an ASN.1 module (or several modules linked by EXPORTS and IMPORTS) and will process the module(s) to generate as output the mapping of the types in those modules into the chosen target language. ASN.1 编译器工具的设计者已经成功地将任意复杂的 ASN.1 类型集映射到了所选语言中的相关数据类型集。同时，他们还编写了相应的程序（这通常被称为“编译器”）。该程序能够接收 ASN.1 模块的文本（或由 EXPORTS 和 IMPORTS 连接的多个模块），然后对这些模块进行处理，最终将模块中各类别的映射结果输出到所选的目标语言中。

This is perhaps the most important design decision. It is often called "defining the API for ASN.1", and in the case of C++ there is an X-Open standard for this. Get that wrong, and there will be some abstract values of the ASN.1 type that cannot be represented by values of the programminglanguage data-structure. Or perhaps the programming-language data-structure generated will just produce programminglanguage-compiler error messages when you try to use it! 这或许是最重要的一项设计决策。它通常被称为“为 ASN.1 定义 API”。在 C++的情况下，有一个名为 X-Open 的标准规范用于这一目的。如果处理出错，那么一些 ASN.1 类型的数据将无法用编程语言的数据结构来表示。或者，当尝试使用所生成的数据结构时，可能会遇到编程语言的编译错误！

How does that help you? Well, your pseudo-code for encoding "Report- item" now looks more like figure 30. 那对你有什么帮助呢？嗯，你现在用于编码“报告-项目”的伪代码看起来更像是图 30 的样子了。

```txt
Get value for "item" into Report-item.item
Get value for "item-description" into
Report-item.item-description
Get "bar-code-data" into Report-item.bar-code-data
Get "ran-out-of-stock" value into
Report-item.ran-out-of-stock
...
etc, setting all the fields of Report-item
...
Call Encode (CompilerInfo, Report-item, Buffer)
Pass Buffer to lower layers for transmission
Clear Buffer 
```

Figue 30 - Pseudo-code to encode using an ASN.1-compiler-tool 图 30 – 使用 ASN.1 编译器工具进行编码的伪代码

Note that however complicated a nested structure of types or repetitions of SEQUENCE OF there are, there is just one call of "Encode" at the end to encode your complete message from the values you have set in your programming language data-structure. 请注意，无论类型嵌套结构或序列重复多么复杂，最终只需要调用一次“编码”操作，就可以从您在编程语言数据结构中设置的数值中编码出整个消息。

For incoming messages, the process is reversed. Your own code does no parsing, and no treewalking. It merely accesses the fields of the programming-language data-structure that the "compiler" part of the tool generated for you. 对于传入的消息，处理过程则相反。你的代码不需要进行解析，也不需要进行任何树遍历操作。只需要访问工具中的“编译器”部分所生成的编程语言数据结构的各个字段即可。

"CompilerInfo" in the call of "Encode" is information passed from the "compiler" part of the tool to the run-time routines. This passes (inter alia) the tagging to be applied for BER. Although largely invisible to you (you do not need to understand the form of this information), it is absolutely essential to enable the run-time routines to provide their encode/decode functions. 在“Encode”函数的调用中，“CompilerInfo”所包含的信息是从工具的“编译器”部分传递到运行时 routines 的。这些信息中包含了用于错误检测（BER）的标签信息。虽然这些信息对您来说可能不太明显（您无需理解这些信息的格式），但这些信息对于让运行时 routines 能够执行编码/解码功能来说至关重要。

## 5.4 Memory and CPU trade-offs at run-time 5.4 运行时的内存和 CPU 资源权衡问题

What is this parameter "CompilerInfo"? This is a vital magic ingredient! This is produced by the compiler, and contains the "recipe" for taking the contents of memory pointed to by "Return-of-sales" (for example), finding from that memory the actual values for the ASN.1 type, and encoding those 这个参数“CompilerInfo”是什么？它其实是一个非常重要的魔法元素！这个参数是由编译器生成的，它包含了获取由“Return-of-sales”指针所指向的内存中的内容，然后从该内存中提取 ASN.1 类型的实际值，并对这些值进行编码的“配方”。

Interpretation of tables is a pretty compact way of performing a task, but open code is faster! With the best tools you choose. 表格的解析是一种较为简洁的完成任务的方式，但使用开放式的代码则能更快完成工作！选择合适的工具，让你能够事半功倍。

values with correct tags, correct use of DEFAULT, etc. It essentially contains the entire information present in the ASN.1 type definition. 带有正确标签的变量，正确的 DEFAULT 使用方式等。实际上，它包含了 ASN.1 类型定义中的所有信息。

There are (at least!) two forms this "CompilerInfo" can take: 这种“CompilerInfo”类型至少有两种形式：

• It can be a very compact set of tables which are used in an interpretive fashion by "Encode" to determine how to encode the contents of the memory containing a value of (eg) "Return-of-sales" (and similarly for "decode"). • 它其实可以是一组非常简洁的表格结构。通过“编码”操作，可以以解释性的方式使用这些表格来确定如何对包含“退货率”等值的内存内容进行编码；而“解码”操作则用于相反的目的。

It can be (rather more verbose, but faster) actual code to pick up the value of each field in turn to do the encoding of that field (and to merge the pieces together into larger SEQUENCE, SEQUENCE OF, etc structures). In general, open code is probably more appropriate for PER than for BER, as tags and lengths are often omitted in PER, whereas a table-driven approach, defining the tags to be encoded and letting the interpreter generate the lengths, may be more appropriate for BER. It is horses for courses! 可以使用一些实际代码来依次获取每个字段的值，然后对这些字段进行编码，并将这些编码结果合并成更大的序列、数组等结构。一般来说，对于 PER 来说，开放式的编码方式可能更为合适，因为 PER 中常常省略了标签和长度信息。而对于 BER 来说，采用以表格驱动的方式，明确需要编码的标签，并让解释器自动生成长度信息，则更为合适。总之，具体情况需要具体分析！

Just as there are many different implementation architectures for hand-encoding, so there are many different possible architectures for the design of tools. With implementation architectures, all that matters is that the bits-on-the-line are correct. And similarly with an ASN.1-compiler-tool, all that really matters is that it produces a programming-language data-structure that can represent all abstract values of the ASN.1 type, and that it efficiently produces correct encodings for values placed in that data-structure. (With similar remarks concerning decoding.) I don't know exactly how the "OSS ASN.1 Tools" product goes about producing an encoding (or decodes), but it does produce the right results! 在手工编码方面，存在许多不同的实现架构；而在工具设计方面，也有许多不同的架构可供选择。在实现架构方面，重要的是线上的数据要准确无误。同样，对于 ASN.1 编译器工具来说，重要的是它能够生成一种编程语言的数据结构，能够表示 ASN.1 类型中的所有抽象值，并且能够高效地生成适用于该数据结构的正确编码（关于解码方面也有类似的说明）。我不知道“OSS ASN.1 工具”是如何生成编码（或解码）结果的，但它确实能够产生正确的结果！

## 5.5 Control of a tool 5.5 工具的控制

There are a host of options that can be incorporated into an ASN.1-compiler-tool (and/or the run-time libraries that support it). For example: 在 ASN.1 编译器工具中，可以整合许多不同的选项（以及支持这些选项的运行时库）。例如：

Inevitably there are options you want to leave to the user. How best to do that? 不可避免地，有一些选项是需要留给用户自行决定的。那么，应该如何最好地实现这一点呢？

• The language or platform to "compile" for. • 用于“编译”的语言或平台。

• How to represent ASN.1 INTEGER types in the programming-language data-structures. • 如何在编程语言的数据结构中表示 ASN.1 的 INTEGER 类型。

• Whether to use arrays or linked-list structures in the mapping from ASN.1 to your programming-language (for example, for "SEQUENCE OF"). • 在从 ASN.1 格式转换为你的编程语言时，是应该使用数组结构还是链表结构来表示“序列”这样的数据结构。

• Which encoding rules to use for encoding (and to assume for decoding). • 应该使用哪种编码规则来进行编码（以及用于解码的规则）。

(Slightly more subtle) Which encoding rules can be selected at run-time - all or only a subset? (This affects the library routines that are included, and hence the size of the executable.) （稍微复杂一点）可以在运行时选择哪些编码规则？全部选择，还是只选择一部分？这会影响所包含的库函数，从而影响到可执行文件的大小。

• Which encodings to use in the non-canonical encoding rules. • 在非标准编码规则中应使用哪些编码方式。

• Whether the user prefers the fastest possible encode/decode or the smallest executable. • 用户是更倾向于最快速的编码/解码过程，还是更倾向于最小的可执行文件大小？

• (Fairly unimportant) The names of the directories and files that will be used at both compile-time and run-time. • （不太重要）在编译和运行时都会使用的目录和文件名称。

• And many others. • 还有很多其他的事情。

The control by the user can be expressed by a global configuration file, by command-line directives, by an "options" button in a Windows-based product, by "compiler directives" embedded in the ASN.1 source, or by run-time call parameters, or by several of these, with one providing a global default and another overriding that default locally. With the "OSS ASN.1 Tools" product, compiler directives are included after a type definition (where a subtype specification might go) as a specialised form of comment. For example: 用户的控制可以通过全局配置文件、命令行指令、基于 Windows 的产品的“选项”按钮、嵌入在 ASN.1 源代码中的“编译指令”，或者运行时的调用参数来实现。其中一些方式会提供全局默认值，而另一些则可以在本地覆盖该默认值。使用“OSS ASN.1 工具”产品时，编译指令被包含在类型定义之后（比如子类型声明的位置），作为一种特殊的注释形式。例如：

 

$$
\text { SET } - - < \text { LINKED } > - - \text { OF INTEGER }
$$

 

## 6 Use of the "OSS ASN.1 Tools" product 6. 使用“OSS ASN.1 工具”产品

Here we describe how to encode values with one particular tool. The process with other ASN.1- compiler-tools is similar. 在这里，我们描述了如何使用一种特定的工具来编码值。其他 ASN.1 编译器工具的过程也是类似的。

<table><tbody><tr><td data-imt-p="1">Put your values in the language data-structure and call ENCODE. That is all there is to it! More-or-less! 将你的数值值放入语言、数据结构和调用 ENCODE 函数中。就这么简单而已！差不多就是这样吧！</td></tr></tbody></table>

When you use the "OSS ASN.1 Tools" product to support an application written using the C programming language, you input an ASN.1 specification (and identify the top-level type that forms the abstract syntax, or PDU, to the compiler via a compiler directive). This can be defined using a single module or several modules. There are four outputs (but only the last two are important for correct ASN.1 input): 当您使用“OSS ASN.1 工具”来支持用 C 语言编写的应用程序时，您需要输入一个 ASN.1 规范（同时指明顶级类型，该类型通过编译器指令传递给编译器，以形成抽象语法或 PDU）。这个规范可以通过一个模块或多个模块来定义。总共有四个输出结果（但只有最后两个对于生成正确的 ASN.1 输入非常重要）：

• A "pretty-print" listing (not really very important). • 一个用于“美化输出格式”的列表项（其实并不是非常重要）。

• Error and warning messages if your ASN.1 is a bit "funny". • 如果您的 ASN.1 格式有些特殊或复杂，可能会出现错误和警告信息。

• A ".h" header file that contains the mapping of your ASN.1 types into C language datastructures. • 一个“.h”头文件，其中包含了将您的 ASN.1 类型映射到 C 语言数据结构之间的映射信息。

• A ".c" control file that conveys information from the compiler to the run-time routines that you will invoke to encode and decode. • 一个“.c”控制文件，它负责将编译器的信息传递给运行时程序，以便这些程序能够执行编码和解码操作。

The latter is pretty incomprehensible (but vitally important), and you ignore it, other than to compile it with your C compiler and link in the resulting object file as part of your application. 后者其实相当难以理解（但非常重要），你只需忽略它，无需对其进行任何处理，只需将其与你的 C 语言编译器一起编译，然后将生成的对象文件作为应用程序的一部分进行链接即可。

The ".h" file is included with your own code, and compiled to form the main part of your application, which will include calls to "encode" and "decode". You also link in a run-time library. At this stage you may wish to look at Appendices 3 and 4, which have not been included in ths chapter due to their bulk. 那个“.h”文件是随你的代码一起编译进应用程序中的，它构成了应用程序的主要组成部分。在这个文件中，你会看到对“encode”和“decode”函数的调用。此外，你还需要在运行时链接一个库文件。在这个阶段，你可以参考附录 3 和附录 4 的内容，但由于篇幅原因，这些内容并未被包含在这章中。

Appendix 3 gives most of the ".h" file for "Return-of-sales" and "Report-item" for the C language implementation (and some parts of relevant "include" files). Appendix 4 gives the equivalent for a Java implementation. 附录 3 列出了 C 语言实现中“销售回款”和“报告项目”相关的“.h”文件内容（以及相关“包含文件”中的部分代码）。附录 4 则提供了 Java 实现中的对应代码。

I offer no explanation or discussion of these appendices - if you are a C or Java programmer, the text (and its relation to the ASN.1 definitions) will be quite understandable. If you are not, just ignore them! 我不会对这些附录进行任何解释或讨论——如果你是一名 C 语言或 Java 语言的程序员，那么这些文本以及它们与 ASN.1 定义之间的关系对你来说应该很容易理解。如果你不是这样的程序员，那就直接忽略它们吧！

And there you have it! Of course, the original application standard could have been published in "pseudo-C" or in Java instead of using ASN.1, but would that really have been a good idea? For once I will express an opinion - NO. Ask the same question in 1982/4 and it would have been COBOL or Pascal (or perhaps Modula) that we would have been talking about. And even if you define your structures in "pseudo-C", you still have to make statements about the encoding of those structures, the most important being about the order of the bytes in an integer when transmitted down the line, about the flattening of any tree structures you create, about the size of integers and of pointers, and so on. It really is rather simpler with ASN.1 - let the ASN.1-compiler-tool take the strain! 就是这样！当然，原本的应用程序标准可以用“伪 C”语言或 Java 来编写，而不是使用 ASN.1 标准。但那样真的好吗？至少我可以表达一下我的意见——不行。如果在 1982 年或 1984 年提出同样的问题，我们讨论的可能会是 COBOL 语言、Pascal 语言（或者 Modula 语言）。即使你用“伪 C”语言定义你的数据结构，仍然需要处理关于这些数据结构编码的问题，比如整数在传输过程中字节的顺序、你创建的任何树形结构如何被处理、整数和指针的大小等等。使用 ASN.1 确实要简单得多——让 ASN.1 编译器来处理这些事情吧！

The appendices are not of course the entire compiler output. There is also the control information used by the run-time routines to perform the encode/decode, but the implementor need never look at that, and it is not shown here. 当然，附录并不是编译输出的全部内容。此外，还有运行时程序用来进行编码/解码的控制信息，但实现者无需查看这些信息，因此这里并未展示。

## 7 What makes one ASN.1-comiler-tool better than another? 7. 究竟是什么让一种 ASN.1 编译器工具比其他工具更优秀呢？

There are many dimensions on which the quality of a tool can be judged. The major areas to be looked at are: 判断一个工具的优劣可以从许多方面入手。主要需要关注的领域包括：

• The extent of support for the full ASN.1 notation. • 对完整 ASN1 表示法的支持程度。

<table><tbody><tr><td data-imt-p="1">OK. So you want to buy an ASN.1-compiler-tool? What to look for in a best-buy? It is not as easy as buying a washing-machine! Here are some things you might want to look for or beware of. 好的。那么，您想要购买一款 ASN.1 编译器工具吗？在挑选合适的产品时，应该注意哪些因素呢？这可不像购买洗衣机那么简单！以下是一些您可能需要考虑或警惕的事情。</td></tr></tbody></table>

• The mappings to programming-language data-structures. • 这些映射与编程语言中的数据结构相对应。

• Run-time memory/CPU trade-offs. • 运行时的内存/CPU 资源权衡问题。

• Memory allocation mechanisms. • 内存分配机制。

• The degree of user control over options. • 用户对各项选项的控制程度。

We have already had some discussion of most of these areas when we discussed the sorts of decisions a tool vendor needs to take. Here we highlight a few points of detail. It is, however, important to recognise that with the best tools, absolutely none of the problems listed below will arise. Indeed, many of the problems occurred only in early tools before they were fullydeveloped. 在讨论工具供应商需要做出哪些决策时，我们已经对大部分相关领域进行了讨论。在这里，我们重点强调一些细节。不过，重要的是要认识到，使用最优秀的工具的话，上述所有问题都不会出现。实际上，许多问题只出现在那些尚未完全开发的早期工具中。

Some early tools provided no support for ASN.1 value notation, so you needed to remove all value assignments from your module and replace "DEFAULT" by "OPTIONAL", handling the default value in your application code. 一些早期的工具并不支持 ASN.1 值表示法，因此你需要从模块中移除所有值赋值操作，并将“DEFAULT”替换为“OPTIONAL”，并在应用程序代码中处理默认值。

Other early tools could only handle a single module (no support for IMPORTS and EXPORTS), so you had to physically copy text to produce a single module. The better tools today will handle multiple modules, and (once you have identified your top-level message to them) will extract from those modules precisely and only those types that are needed to support your top-level message. 早期的工具只能处理单个模块，不支持导入和导出功能，因此必须手动复制文本以生成单个模块。而如今更好的工具能够处理多个模块，并且一旦确定了向它们传递的顶层信息，就能精确地提取出那些对支持该顶层信息至关重要的数据类型。

Another issue is whether you can use the ASN.1 definition as published, or whether you have to help the parser in the tool by adding a semi-colon to the end of each of the assignment statements in your module. 另一个问题是，是否可以使用发布的 ASN.1 定义；还是需要在你的模块中，在每个赋值语句的末尾添加分号，以辅助工具中的解析器工作。

There are other tools that are designed simply to support one particular protocol, and will recognise only the types that appear in that protocol. If that protocol is extended in version 2 to use more types, you may have to wait for an upgrade to your tool before you can implement version 2! 还有其他一些工具，它们专门设计用于支持某种特定的协议，并且只能识别该协议中出现的类型。如果某个协议在版本 2 中增加了更多的类型，那么你可能需要等待工具的升级，才能实现版本 2 的功能！

There is also the issue of the 1994 extensions to ASN.1 - Information Object Classes etc, described in Section II. This is probably the area where you are most likely to still find lack of support in some tools. 此外，还有 1994 年对 ASN.1 标准的扩展——即信息对象类等相关内容。这些扩展在第二部分中有详细描述。很可能在这个领域，某些工具仍然不支持这些扩展。

The mapping to the programming-language data-structure is a very critical area. If this is got wrong you may not be able to set all the values you should be able to! 将数据结构映射到编程语言中的操作是一个非常关键的领域。如果这一步骤出错，那么你可能就无法设置所有应有的数值了！

Note also that ASN.1 allows arbitrary length names for identifiers (with all characters significant), and is case sensitive. In some programming languages, characters after (e.g.) the 31st are simply discarded. Does the tool ensure that long names (which are quite common in ASN.1) are mapped into distinct programming language names in an ergonomic way that you can understand? 请注意，ASN.1 允许标识符具有任意长度（包含所有字符），并且区分大小写。在某些编程语言中，第 31 个字符之后的字符会被直接忽略。该工具是否能够确保较长的标识符能够以易于理解的方式被转换为相应的编程语言名称呢？

What about INTEGER types? A good tool will give you control (usually through either global directives or directives you embed into the ASN.1 text against a particular type) over the mapping of INTEGER types, for example into a short, normal, long, or huge (represented as a string) integer. 那么 INTEGER 类型呢？一个好的工具可以让你对 INTEGER 类型的映射进行控制——通常可以通过全局指令或嵌入到 ASN.1 配置文件中的特定类型指令来实现这一点。例如，你可以控制 INTEGER 类型如何被转换为短整数、普通整数、长整数，或者以字符串形式表示的巨大整数。

There are also efficiency considerations in the mappings. On some platforms there is the concept of "native" integer types. Mapping directly into these can be much more efficient than proceeding in a more generic (platform-independent) manner. 在映射过程中，效率也是一个需要考虑的因素。在某些平台上，存在“原生”整数类型的概念。直接将这些类型映射到相应的位置，会比采用更通用（与平台无关）的方法更高效。

It is important here to remember that the mappings from ASN.1 to a programming language (usually called an "ASN.1 Application Programme Interface (API)" are in general not standardised, so each tool vendor does their own thing. (Work was done within X-Open on standardisation of the mapping to C++ - called the ASN.1/C++ API - but I am not sure whether the document was finally ratified. If you want to use C++ as your implementation language, you may want to ask your tool vendor about whether they use that mapping or not.) 在这里，重要的是要记住，从 ASN.1 到某种编程语言的映射关系通常并不标准化，因此每个工具供应商都有自己的实现方式。不过，有一些标准化努力在 X-Open 项目中进行了尝试，比如将 ASN.1 映射到 C++的语言接口——即 ASN.1/C++ API。不过我不确定该文档是否最终得到了批准。如果你想要使用 C++作为实现语言，可能需要咨询你的工具供应商，了解他们是否采用了这种映射方式。

We discussed earlier the option of a largely interpretative table-driven approach (using little memory) versus an approach based on generated code (taking more memory but faster) to run-time encoding and decoding. This is one area where you will probably be looking for options in the use of the tool that will enable you to choose for each application or platform which approach you want taken. 我们之前讨论过两种方法的优劣：一种是基于表格驱动的解释性方法（占用较少内存），另一种则是基于生成代码的编码方法（虽然需要更多内存，但执行速度更快）。在这一点上，您可以在工具的使用选项中找到适合每种应用或平台的编码方式。

And finally, we discussed earlier the means of providing user control over tool options and the range of such options that can be controlled. 最后，我们之前讨论过如何让用户能够控制工具选项的设置，以及可以控制的选项范围。

All these factors contribute to the "quality" of a tool, but you will certainly want to look at the cost as well! Most tool vendors charge a licence fee that gets you just one copy of the ASN.1-compilertool, but unlimited copies of the run-time support (which you clearly need if you are to distribute your resulting application!). 所有这些因素都影响着工具的“质量”，但您肯定也会关心其成本！大多数工具供应商都会收取一次性许可费，这样您就可以拥有一份 ASN 编译工具的安装版。不过，对于运行时的支持部分，您可以免费获取无限份副本——如果您要分发自己的应用程序的话，这一点非常重要。

## 8 Conclusion 8. 结论

This chapter has discussed how to build an actual implementation for a protocol that has been defined using ASN.1. It is followed by some discussion of management and design issues for consideration by managers, specifiers, and implementors, to complete Section I of this book. 本章讨论了如何构建基于 ASN.1 定义的协议的实际实现。接下来，我们将讨论一些管理和设计方面的问题，以便管理者、规范制定者以及实施者能够充分考虑这些问题，从而完成本书的第一部分的内容。

# Chapter 7 Management and design issues for ASN.1 specification and implementation 第七章 ASN.1 规范与实现的管理与设计问题

# (Or: Things you need to think about!) （或者：你需要思考的一些事情！）

Summary: 总结：

This chapter: 这一章：

• collects together many of the issues and "style" decisions mentioned elsewhere in the text; • 汇集了文本其他部分中提到的许多相关问题和风格决策；

• identifies some global issues for management decisions; • 识别了一些需要管理层决策的全球性问题；

• identifies matters that specifiers need to consider; • 确定了那些需要由指定方考虑的因素；

• identifies matters that implementors need to consider. • 指出了实施者需要考虑的事项。

The section on management decisions should be understandable to anyone who has read Section I. The remaining sections will require a knowledge of material covered in Section II, assume a quite detailed knowledge of ASN.1, and cover some fairly abstruse areas. 关于管理决策的部分，任何读过第一部分内容的人都应该能够理解。其余的部分则需要具备第二部分中涉及的知识，同时还需要对 ASN.1 有相当深入的了解。其中一些内容则相当复杂，需要较高的专业水平才能理解。

A word of caution: I am not a believer in management gurus and elaborate "methodologies". Most of the headings below have the word "issues" in them. The following text is designed to give the reader some idea of the options, and things they should consider. At the end of the day you make the decisions, not me! I try as much as possible to suggest areas you should think about, rather than to tell you what I think you should do. If occasionally I move towards the latter, I apologise and please feel free to ignore my advice! 请注意：我不相信那些管理大师所提出的复杂“方法论”。下面列出的大多数标题中都包含了“问题”这个词。这段文字旨在让读者对各种选择有所了解，并知道他们需要考虑哪些因素。最终的决定还是由你来做，而不是由我来决定！我尽可能多地提出一些值得思考的要点，而不是告诉您我认为您应该做什么。如果偶尔我倾向于使用后者，请原谅我，如果您愿意，也可以忽略我的建议！

Much of what is being said in this chapter is opinion (Figure 999 again!), not fact, and there are others who may well have different and perhaps opposite views to some of the suggestions made here. 这一章中大部分内容都是观点表达（再次提到图 999 了！），而非事实。当然，也可能有人持有与这里提出的建议不同的、甚至是相反的观点。

# 1 Global issues for management decisions 1. 管理决策中的全球性问题

## 1.1 Specification 1.1 规格说明

## 1.1.1 To use ASN.1 or not! 1.1.1 是否使用 ASN.1 格式！

This has been well-discussed in Chapter 1, when a variety of techniques for defining protocols were described. This of course is the number 1 decision, but may be more conditioned by the culture within which the protocol specification is being made, or on the specification notation that has been used for other related protocols. 在第一章中已经充分讨论过这个问题，当时提到了多种定义协议的技术。当然，这是首要的决策，但实际上这一决策还可能受到制定协议规范时所处的文化环境的影响，或者取决于用于其他相关协议的规范语言选择。

If you have read this far, and you are able to influence the specification language used for a protocol, then I am sure you will ensure that ASN.1 is seriously considered. Go on to the next clause! 如果您已经读到了这里，并且能够影响协议所使用的规范语言，那么我相信您一定会确保 ASN.1 被认真考虑。请继续阅读下一节吧！

By now, you should have a clear view of the ease of producing a specification using ASN.1, and of the ease of implementing such a protocol provided an ASN.1 tool is available. 到现在为止，你应该已经清楚地了解到使用 ASN1 来编写规范是多么简单了。而且，如果有相应的 ASN1 工具可用，那么实现这样的协议也将会非常容易。

The counter-argument is that, simply because of its ease of use, ASN.1 does not force you to keep your specification simple (but of course does not prevent you from doing so!), and the more complex the protocol becomes the more your implementors will need tool support, and tools do cost money! 另一种观点是，由于 ASN.1 的易用性，它并不强制要求规范设计必须简单明了（当然，这也不是说开发者不能设计复杂的规范！）。而且，随着协议复杂性的增加，开发者需要更多工具的支持，而这些工具的成本也是相当高的！

However, if you are expecting your protocol to be implemented by commercial firms, with perhaps ten to twenty man-years of effort going into the implementation, the cost of purchasing a tool becomes totally insignificant. Paying money for a professionally-developed, supported, and robust tool is often more effective in the long run than use of a "freebie". (The main counter-argument to this is probably the Apache Web server - probably the most popular Web server in use today, and it is free! But there is an English saying "the exception proves the rule".) 不过，如果你期望由商业公司来实施你的协议，那么可能需要投入十到二十个人年的时间来完成实施工作。在这种情况下，购买这样的工具所付出的成本就变得微不足道了。从长远来看，使用一款专业开发、有支持且功能强大的工具，往往比使用“免费工具”更为划算。（反对这一观点的主要理由是：Apache Web 服务器——目前最流行的 Web 服务器，而且它是免费的！不过，有句英语谚语说：“例外证明规则。”）

## 1.1.2 To copy or not? 1.1.2 是否要复制？

If you need an ASN.1 type defined in (and exported by) another standard, there is a clear argument for importing that type into your own module(s). This is commonly done for ROSE datatypes and object classes, and 如果您需要一个在另一标准中定义且被该标准使用的 ASN.1 类型，那么将这种类型导入到您自己的模块中是非常合理的做法。这种情况常见于 ROSE 数据类型和对象类的情况。

Copying is wrong, yes? You may be able to get permission, and it may be the better solution. Look at the issues below. 复制的做法确实不对吧？也许你可以获得许可，那样或许才是更好的解决方案。请参考下面的问题。

for X.500 Directory Names and for X.509 certificates. In this case you would, of course, also include a clear reference to the source that your were importing from. 适用于 X.500 目录名称以及 X.509 证书。在这种情况下，当然还需要明确注明您所导入资源的来源。

There is, however, another option that has been taken by some specifiers, and that is to simply copy a type definition into your own specification (of course also giving the semantics related to the fields). This is arguably in violation of the copyright laws, or at least of intellectual property rights, unless your specification is to be published by the same standards body as the one you are copying from, but it has ocurred in a number of specifications, even when the above caveat does not apply! 不过，还有一些规范制定者采用了另一种方法，那就是直接复制某个类型定义到自己的规范中（当然，同时还需要提供与这些字段相关的语义说明）。这种做法显然违反了版权法律，或者至少侵犯了知识产权。不过，这种情况在一些规范中确实存在，即使在上述警告条件不适用的情况下也是如此！

There are three main reasons for copying (embedding) rather than importing and referencing: 采用复制（嵌入）而非导入和引用主要有三个原因：

• It gives you control over the material, preventing problems and confusion if the referenced material is changed in a later version in a way that is not compatible with your own specification. • 这让你能够控制所使用的材料，从而避免因为参考材料在后续版本中发生与你的规范不兼容的变更而带来的问题和混乱。

• It means that your implementors only need to obtain your documents - your specification is complete and self-contained. 这意味着，您的实施者只需获取您的文档即可——您的规范已经完整且独立了。

• You want only a simplified version of the copied material (this is often the reason why you find copies of the ROSE material in other specifications, rather than direct use of IMPORT). • 您只希望获得复制材料的简化版本（这通常就是为什么会在其他规范中看到 ROSE 材料的副本，而不是直接使用 IMPORT 的原因）。

Decisions on this issue are not easy, and should be taken consciously after appropriate discussion. 关于这个问题，做出决策并不容易，应该在充分讨论之后才进行。

There are no other real management issues related to specification (but many more details for specifiers are discussed below), so we now turn to issues related to implementation. 与规范相关的实际管理问题并不多见（不过下面会讨论一些更详细的细节）。现在，我们转向与实施相关的问题。

## 1.2 Implementation - setting the budget 1.2 实施阶段——制定预算

Any commercial project needs detailed costings, but it can be easy to overlook some of the hidden costs (or opportunities to spend money wisely!) when undertaking an implementation of an ASN.1-based specification. Some of these are mentioned below. 任何商业项目都需要详细的成本预算，但在实施基于 ASN.1 的规范时，很容易忽略一些隐藏的成本或合理利用资金的机会。以下列出了一些这些成本/机会。

Just a few things you should not forget about when doing your costings ... 在进行成本计算时，有一些事情是绝对不能忘记的……

## 1.2.1 Getting the specs 1.2.1 获取规格信息

There are two sets of specifications that you need - those for the protocol you are implementing and those for ASN.1 itself. 你需要准备两套规范文件：一套是关于你所实现的协议的规范，另一套则是关于 ASN.1 本身的规范。

Of course you need the specification for your protocol. But also for ASN.1, and possibly for anything either of these reference. 当然，你需要你的协议的相关规范。不过，对于 ASN.1 来说也是必需的。此外，可能还需要这些规范的任何相关文档。

In most cases you will want to use the latest versions of both the protocol specification and the ASN.1 specifications, but occasionally there may be some industry or community of interest agreement on use of older versions. (The ASN.1 1990 issue is discussed in Chapter 1 of Section IV). Be careful, too, to look out for corrigenda and addenda to the specifications. The place you obtained your specifications from should be able to alert you to this. In some cases there may be draft corrigenda or addenda in circulation. In this latter case, you may need to investigate further and perhaps try to contact the chairman or rapporteur or editor of the standards to discover the stability of these documents. Draft corrigenda and draft addenda do not always become approved corrigenda or addenda (at least not without sometimes substantial change). 在大多数情况下，你都应该使用最新版本的协议规范和 ASN 规范。不过，偶尔也会有一些行业或社区之间的共识，允许使用较旧的版本。（关于 ASN 1990 版本的讨论可以在第四部分的第一章中找到）。同时，也要注意查看规范的补遗和附加内容。你获取规范来源的地方应该会提醒你这一点。在某些情况下，可能会有一些草案补遗或附加内容在流传中。在这种情况下，你可能需要进一步调查，并试图联系标准的负责人、报告员或编辑，以了解这些文件的稳定性。草案补遗和附加内容并不一定会成为正式批准的规范或附加内容（至少通常会有很大的改动）。

Note that ITU-T now have a Web-site from which (provided you have set up an account) you can purchase all ITU-T specifications and down-load copies over the Web. ETSI (European Telecommunications Standards Institute) have a similar site, but ETSI standards are free! Many of these use ASN.1 as their specification language. Links to these sites can be obtained via Appendix 5. 请注意，ITU-T 现在有一个官方网站，只要注册了账户，就可以从该网站购买所有 ITU-T 标准，并通过网络下载相关文档。ETSI（欧洲电信标准协会）也有类似的网站，不过 ETSII 的标准是可以免费获取的！许多 ITU-T 标准都采用 ASN.1 作为其规范语言。这些网站的链接可以在附录 5 中找到。

In the case of your protocol specifications (but not the ASN.1 specifications themselves) it will be important to try to get hold of an electronic copy of the ASN.1 parts of the specification if you are going to use a tool, otherwise you will have the tedious and error-prone task of keying in that text. 在您编写协议规范时（不过 ASN.1 规范本身并不需要翻译），如果打算使用某些工具的话，那么获取规范中 ASN.1 部分的电子版本是非常重要的。否则，您就不得不进行繁琐且容易出错的文本输入工作。

The vendor of your tool is likely to be able to help you here, and electronic copies of ASN.1 specifications usually circulate without charge and are sometimes on the Web. Another source of an electronic copy is the Editor of the protocol specification, who will usually be happy to provide one provided there are no commercial vendors of electronic versions and provided he knows you have bought the printed version of the specifications. 您所购买工具的供应商很可能能够为您提供帮助。而 ASN.1 规范的数字版本通常可以免费获取，有时甚至可以在互联网上找到。另一个获取数字版本的途径是该协议规范的编辑人员，只要他们没有商业化的电子版本销售渠道，并且他们知道您已经购买了纸质版本的规范，那么他们通常很乐意为您提供数字版本。

You will need to get these specifications in a timely manner for your project, and in both cases (ASN.1 specs and your protocol specs) you will probably find you need some supporting specifications as well, and these need to be identified early in the project. 你需要及时获取这些规格信息，以便用于你的项目。在 ASN.1 规范和你的协议规范这两方面，你可能会发现还需要一些相关的支持性规范，这些规范需要在项目初期就加以考虑和规划。

In the case of the ASN.1 specifications, full details of the encoding of REAL, of GeneralizedTime and of most of the character set types require reference to additional separate specifications, so if these types are used in your protocol specification, you will need to obtain these other specifications as well. 在 ASN.1 规范中，对于 REAL、GeneralizedTime 以及大多数字符集类型的编码细节，需要参考其他单独的规范。因此，如果您的协议规范使用了这些类型，那么您也需要获取这些相关规范。

It is ISO advice that when one Standard references another, you should always use the latest version of the referenced Standard. This can, however, sometimes be dangerous, and it is always well to check publication dates to see which version of a referenced Standard was current at the time of publication of the referencing Standard, and see what impact the changes made might have on your protocol. 根据 ISO 的建议，当一个标准引用了另一个标准时，应该始终使用引用标准的最新版本。不过，这种情况有时可能会带来风险，因此始终有必要检查引用标准的发布日期，以确定在引用标准发布时该标准的具体版本是什么，以及这些变更可能对你的协议设计产生什么影响。

## 1.2.2 Training courses, tutorials, and consultants 1.2.2 培训课程、辅导以及顾问服务

Another cost that is easily over-looked (and time for it not included in the project plan) is training time and the cost of courses for your implementation team. 另一个容易被忽视的成本（而且这个成本也没有包含在项目计划中）就是培训时间和相关课程的费用。这些费用需要由实施团队自行承担。

Commercial courses are commercial! (But your tool vendor may have a bundle that includes some courses and tutorial material for you). 商业课程当然是商业性质的！（不过，您的工具供应商或许提供了一套包含若干商业课程和教程材料的套餐供您使用。）

A "theory only" course on ASN.1 (covering more or less the same technical material as this book, but without the sorts of discussions that are appearing in this chapter and in a few other places) will take about two days. A course with some hands-on work writing ASN.1 specifications and using a tool could be as long as four days. 关于 ASN.1 的“仅理论讲解”课程大约需要两天时间。而包含实际编写 ASN.1 规范以及使用相关工具的实践的课程则可能需要长达四天的时间。

You may also want to supplement such courses with purchases of this book! (Or of the companion volume by Olivier Dubuisson - available in both French and English. See Appendix 5 for a link.) 您或许还可以通过购买这本书来补充所学的知识哦！（或者购买奥利维尔·杜布伊松的配套书籍——该书籍有法语和英语版本。详情请参阅附录 5 中的链接。）

Similarly, there are commercial courses available giving a good introduction to many of the protocols that are specified using ASN.1, and if these are available for the protocol you are implementing, you will probably want to use them. Frequently the speaker/trainer/presenter will be active in standardization of that protocol, and can alert you to the state of any addenda and corrigenda that may be circulating. 同样地，也有商业课程可以很好地介绍使用 ASN.1 规范定义的许多协议。如果你正在开发的协议有这些课程，那么你很可能会选择使用它们。通常，这些课程的讲师或培训师会在该协议的标准化过程中发挥重要作用，他们可以提醒你关于任何相关补充规范或修正内容的动态变化。

Finally, there are a (small) number of people that advertise themselves as "ASN.1 consultants". They will give implementation advice, or will take an outline of a protocol you want written and produce the ASN.1 for you. But you pay consultancy prices! 最后，还有一小部分人自称是“ASN.1 顾问”。他们会提供实现方面的建议，或者根据你提供的协议大纲来编写相应的 ASN.1 文件。不过，他们收取的是高昂的咨询费用！

## 1.3 Implementation platform and tools 1.3 实施平台与工具

You may have no choice on the implementation platform (hardware, operating system, programming language), due to the need to extend an existing system, or to your firms global policies, or simply due to the operating system and programming language experience of your existing employees. 在选择实施平台时，你可能没有太多选择——因为需要扩展现有的系统，或者因为公司的全球政策要求如此，又或者仅仅是因为现有员工的操作系统和编程语言经验有限。

There are many factors involved in taking decisions on implementation platforms, but there can be interactions between tool choice and platform choice. 在决定采用何种实施平台时，涉及的因素有很多，而工具选择与平台选择之间也可能存在相互作用。

But if you do have a choice, a decision on the platform should be taken along with the decision on whether to use a tool, and if so which one. (Aspects of the "quality" of a tool were discussed in the previous chapter, and should be considered here.) 不过，如果你确实有选择的话，那么关于该使用哪种工具的决定，应该与是否使用该工具的决定一起做出。至于工具的“质量”方面，已经在上一章中讨论过，这里也需要加以考虑。

At least one tool vendor will provide their tool for any platform, provided a C-compiler or a Ccross-compiler exists for that platform. Tools supporting programming in C, C++, and Java are all available. 至少会有一种工具供应商提供适用于任何平台的工具，只要该平台拥有 C 语言编译器或 Ccross 编译器。此外，还有支持 C、C++和 Java 语言的工具可供选择。

## 2 Issues for specifiers 2 个需要关注的问题，供规格制定者参考

This clause discusses a number of points that those involved in protocol specification using ASN.1 should consider. 这一条款涉及了若干要点，那些负责编写使用 ASN 协议的协议规范的人士应当予以注意。

## 2.1 Guiding principles 2.1 指导原则

There are four main principles to keep in mind (some apply to all protocol design, whether using ASN.1 or not). These principles may sound very obvious, but they are often overlooked: 有四个主要原则需要牢记（无论是否使用 ASN.1 标准，这些原则都适用于所有协议设计）。这些原则看起来很直观，但实际上常常被忽视。

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/a0059080-59e4-4cd9-913b-34e7587e39f7/b5a17021ebf675f51bc5b4d6fc04ac4a8f5984366727c2bf6464de7684b9487e.jpg)

• Simplicity: Keep it as simple as possible, whilst being as general and flexible as necessary. • 简洁性：尽可能保持简洁明了，同时确保在必要的情况下具有通用性和灵活性。

Unambiguous and complete: Make absolutely sure you have left no ambiguities in your specification, and no implementation dependence in your specification unless you consciously decide to do so. In the latter case, make sure that such dependencies are clearly stated, not just implied or hidden, and that you consider the full interworking problems of such dependencies. 清晰且完整：务必确保您的规范中没有任何模糊之处，同时确保在实施过程中不存在依赖关系。如果确实存在依赖关系，那么必须明确说明这些关系，而不是隐含或隐藏起来。此外，还需要考虑这些依赖关系所带来的整体协作问题。

Avoid options: Try to avoid encoder options unless there is a very good reason for them, as this reduces decoder implementation costs and testing costs. Allowing options on what parts of the total specification need be implemented is also dangerous, and unless done carefully can seriously limit interworking (but is often done!). A detailed application of this principle says "Don't use SET or SET OF, always use SEQUENCE or SEQUENCE OF instead". 避免使用选项：尽量避免使用编码器的相关选项，除非有非常充分的理由需要使用这些选项。因为这样做可以降低解码器的实现成本以及测试成本。允许在规格说明的某些部分使用选项也是危险的，如果不谨慎处理，可能会严重限制不同系统之间的互操作性（不过这种情况通常也会发生）。这一原则的具体应用说明是：“不要使用 SET 或 SET OF，而始终使用 SEQUENCE 或 SEQUENCE OF。”

• Think about the next version: There always will be a next version if your protocol takes off. How might it differ? How do you want added material to be handled by version 1 systems? • 思考一下下一个版本：如果您的协议能够取得成功，那么必然会有下一个版本出现。这个版本会有哪些不同之处呢？您希望在第一个版本中如何处理那些需要添加的功能呢？

Most of these principles map into some specific ASN.1 features and their use that are described further below. 这些原则大多可以归类到某些特定的 ASN 特性及其使用方式上，这些特性将在下文中进一步描述。

## 2.2 Decisions on style 2.2 风格选择的决定

The best advice is for you to look at as many different specifications as you can and make a conscious decision on the various style issues. 最好的建议是，你应该尽可能了解各种不同的规格参数，然后基于这些信息来做出关于各种风格选择的明智决定。

Some simple things to consider are: 一些需要考虑的简单事项包括：

<table><tbody><tr><td data-imt-p="1">A good style makes the specification easy to read and follow, a bad one makes it hard. The actual bits on the line may be just the same! 好的风格能让规范内容易于阅读和理解，而糟糕的风格则会让内容难以遵循。实际上，那些具体的条款可能根本没什么不同！</td></tr></tbody></table>

• Fonts: Use of different fonts to distinguish formal material from English text. • 字体：使用不同的字体来区分正式文档和英文文本。

• Order of definitions: Top-down listing of type definitions or alphabetical listing? • 定义顺序：是从上到下列出各种类型定义，还是按字母顺序排列？

• Module structure: Grouping of related definitions into modules and the order and overall structure of modules. • 模块结构：将相关定义归类到各个模块中，并确定模块之间的顺序及整体结构。

• Line numbers and indexes: Possible use of line numbering and provision of an index (showing where defined and where used for each reference name) for the specification. • 行号和索引：可以设置行号，并提供索引功能，以便明确标注每个引用名称在规范中的使用位置。

• Lengths of reference names: Long names can be clearer, but can clutter-up a specification. Don't rely on the name alone to define (imply) the associated semantics. • 参考名称的长度：较长的名称可能更清晰，但也可能使规范文件变得混乱。不要仅依赖名称来定义相关的语义。

• Duplicated text: Try not to duplicate text where several messages have common elements, but where this is clearer than (for example) using parameterization, do not be afraid of it if it makes the specification simpler. • 重复的文字：尽量避免在多个消息中存在相同的内容，但如果这样做能让规范更清晰明了，那么就不要害怕使用重复的文字。例如，可以使用参数化来避免重复，但如果这样做能简化规范的话，那就毫无问题。

• Number of parameters: If you have a lot of parameters in a reference name definition, consider defining an Information Object Class to bundle them into a single parameter, as described in Section II Chapter 7. • 参数数量：如果参考名称定义中包含大量参数，可以考虑定义一个信息对象类，将这些参数整合到一个单独的参数中，具体方法请参考第二章第 7 节的描述。

Web publication: There are a lot of standards that now have their ASN.1 (or even the complete specification) on the Web. An approach some take is to provide hyper-text links from every use of a reference name to the definition of that name, but of course you need an ASN.1 tool to generate the HTML for you in this case, or it would be too tedious and error prone to produce. You also still need to provide the "ASCII" txt of your specification for input input an ASN.1 compiler-tool. 网络出版物：现在有许多标准的 ASN.1 格式文档，甚至还有完整的规范文档可以在网络上找到。有些人采用的方法是为每个引用名称提供超链接，指向该名称的定义页面。不过，在这种情况下，你需要使用 ASN.1 工具来生成相应的 HTML 文件，因为否则的话，生成过程会非常繁琐且容易出错。此外，你还需要提供规范的“ASCII”文本版本，以便将其输入到 ASN.1 编译器工具中进行处理。

Other issues are a little more than "style", or warrant a longer discussion than can be provided in a bullet. These are discussed below. 其他问题则不仅仅是“风格”的问题，它们需要更长时间的讨论，而无法在短短几句话中充分阐述。这些问题将在下文中讨论。

## 2.3 Your top-level type 2.3 你的顶级类型

You need to very clearly specify what is the top-level type that defines your messages. This should be a single type, and will almost always be an extensible CHOICE type. Include in this CHOICE all and only those types that define one of your complete outer- 你需要明确指定用于定义你消息的顶层类型。这个类型应该是一个单一的类型，而且几乎总是会是一个可扩展的 CHOICE 类型。在这个 CHOICE 类型中，只包含那些能够定义你所有外部类型的类型。

<table><tbody><tr><td data-imt-p="1">This is your set of messages. Give it the importance and prominence it deserves. All other types are simply there to support this type. 这是您的消息集合。请给予它应有的重视和突出地位。其他类型的消息只是用来辅助这一类型的消息而已。</td></tr></tbody></table>

level messages, not types that might be used in constraints on open types, for example. 比如，应该使用级别消息，而不是那些可能在开放类型约束中使用的类型。

You may use the ABSTRACT-SYNTAX notation to identify this top-level type, or you can just make it very clear by English text and by placing it in a conspicuous position - perhaps in a module of its own. 你可以使用 ABSTRACT-SYNTAX 标记来标识这种顶层类型；或者也可以通过英文文字来明确说明，并将其放在显眼的位置——比如某个模块中。

ABSTRACT-SYNTAX is not often used in current specifications, partly because it was added to ASN.1 at a relatively late date, and partly because the associated object identifier value is needed in communications only if the full OSI stack is being used, but it provides a very clear way of identifying your top-level types. 摘要语法在当前的规范中并不常用，部分原因是它是在相对较晚的时候才被添加到 ASN.1 标准中的；另一部分原因是，只有当使用完整的 OSI 层时，才需要在通信过程中提供相关的对象标识符值。不过，这种语法确实为识别顶级类型提供了一种非常清晰的方式。

As with all cases where you use the extensibility marker, you should think about, and specify clearly, what you want version 1 systems to do if they receive messages that have been added in version 2. If you leave this undefined (implementation-dependent), you have violated one of the four principles above, and it will probably end up biting you! 就像使用扩展性标记的所有情况下一样，你需要明确指定：当系统接收到在版本 2 中新增的消息时，它们应该执行哪些功能。如果你不对此进行明确的规定（依赖具体实现），那么你就违反了上述四个原则中的一条，而这种情况很可能会给你带来麻烦！

## 2.4 Integer sizes and bounds 2.4 整数的大小与界限

This is a detailed issue, and relates not just to the size of integers but also to the length of strings and to iterations of SEQUENCE OF and SET OF. 这是一个比较复杂的问题，它不仅涉及到整数的大小，还与字符串的长度以及\`SEQUENCE OF\`和\`SET OF\`的迭代方式有关。

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/a0059080-59e4-4cd9-913b-34e7587e39f7/f3f65777b38dcaae9c113508504d1c56820c7ae559d8d46672d169574ed44f43.jpg)

If you are using PER, then it is very important that bounds be formally expressed using the subtype notation, as tools will perform encodings according to the bounds. If you are using BER, then the issue is not one of encoding, but concerns: 如果你使用的是 PER 协议，那么非常重要的是，各种边界应该用子类型标记法来明确表述。因为工具会根据这些边界来进行编码处理。而如果你使用的是 BER 协议，那么问题就不在于编码了，而在于其他方面的问题。

• What size integer should be used in the internal processing of these fields? (How should they be mapped into your chosen programming language?) • 在对这些字段进行内部处理时，应该使用什么大小的整数？（它们应该如何转换为你选择的编程语言中的数据类型呢？）

If you fail to give any specification, one implementation may map to (and encode and transmit) 4-octet integers, and another may only support 2-octet integers. Still others may increase implementation costs significantly by making strenuous but unnecessary efforts to handle arbitrarily large integers or arbitrarily long strings. 如果您不提供任何规格要求，那么不同的实现方式可能会有所不同：有的实现能够处理 4 个八位数的整数，并进行编码和传输；而有的实现则只能处理 2 个八位数的整数。还有一些实现方式则会增加显著的实施成本，因为它们需要花费大量不必要的资源来处理任意大的整数或任意长的字符串。

These are, of course, issues with PER as well, but if you have placed bounds on INTEGER types, the implementor can deduce the appropriate size of integer to use internally. 当然，这些问题也涉及到 PER 方面。不过，如果你已经为 INTEGER 类型设定了上限，那么实现者就可以推断出在内部使用适当大小的整数字段。

If a specification is littered with bounds, particularly if these are set in a single module and imported, or passed as parameters, it can make the specification (whilst totally clear to a computer!) less readable by a human being. An alternative can be to define your own type INTEGER4, but then this has to be exported and imported to wherever you want to use it. 如果某个规范中充满了各种限制条件，尤其是当这些限制条件被定义在某个模块中并作为参数传递时，那么对于人类读者来说，该规范就难以理解了（尽管计算机来说这些限制条件显然很清晰）。另一种方法是定义自己的类型 INTEGER4，但这样一来，这个类型就需要被导入导出，才能被实际使用到。

ASN.1 tools generally permit global statements on the size of programming language integers that the ASN.1 INTEGER type is to be mapped into, so that a clear statement in ordinary English that unless otherwise stated, INTEGER fields are expected to be implemented as 4 octet integers can suffice. ASN.1 规范通常允许使用全局声明来指定 ASN.1 的 INTEGER 类型应映射到哪种编程语言整数类型。因此，用简单的英语描述即可满足需求：除非另有说明，否则 INTEGER 字段应被实现为 4 个八位元整数。这样的声明就足够了。

Notice that there is a certain tension here between specification of bounds to ensure the smallest possible number of bits on the line when using PER encodings, versus guidance on what to use for mapping to programming language integers and internal processing. 请注意，这里存在一个矛盾点：一方面需要规定一些限制条件，以确保在使用 PER 编码时线路上的位数尽可能少；另一方面，又需要指导如何将这些编码结果映射到编程语言的整数形式以及内部处理过程中。

What is absolutely vital, however, is to make it clear when very large integers (such as those that appear in signatures in X.509 certificates) have to be supported for the ASN.1 INTEGER type. 然而，最为重要的是要明确指出，在 ASN.1 的 INTEGER 类型中，何时需要支持非常大的整数值（比如那些出现在 X.509 证书签名中的数值）。

We have mainly concentrated on INTEGER in the above, but remember that there are bounds issues related to all of: 在上面的讨论中，我们主要关注的是 INTEGER 类型。不过需要注意的是，所有类型都存在一些相关的限制问题。

• INTEGER values. • 整数值。

• Lengths of BIT STRING, OCTET STRING, character string types, and GeneralizedTime. • BIT 字符串、OCTET 字符串、字符字符串类型以及 GeneralizedTime 类型的长度。

• Number of iterations of each SEQUENCE OF and SET OF. • 每个序列和集合的迭代次数。

And in each case, you have the two main issues raised above: ensuring optimum PER encodings, and ensuring interworking. The latter is arguably the more important. 在每种情况下，都会遇到上述两个主要问题：如何确保最佳的性能参数编码，以及如何确保不同系统之间的互联互通。其中，后者显然更为重要。

As ia pointed out in Section II Chapter 7, if you really do decide to leave some bounds (or anything else) as implementation-dependent, then inclusion of a parameter of the abstract syntax clearly flags this, and you can then include an exception marker on the bound to specify what a receiver should do if the two implementation choices are not the same. If you do take this route, it would be as well to clearly explain in English text what you intend, your reasons for leaving implementation-dependence, and when you expect it (or do not expect it) to cause interworking problems. 正如我在第 7 章第 II 节中指出的，如果你真的决定让某些约束条件取决于具体实现，那么将抽象语法中的参数包含进来显然有助于说明这一点。此外，你还可以在这些约束条件上添加异常标记，以明确当两种实现方式不一致时接收器应该执行什么操作。如果你选择采用这种方法，那么最好用英语清楚地解释你的意图，说明你为何允许实现上的依赖，以及你预计这种情况何时会引发互操作问题。

## 2.5 Extensibility issues 2.5 扩展性问题

We have already mentioned the importance of considering what extensions you are likely to require in version 2, and the importance of inclusion of an ellipsis at appropriate points. 我们已经提到了在版本 2 中考虑可能需要哪些扩展功能的重要性，以及在不适当的位置添加省略号的重要性。

Extensibility is important and will work for you - but only if you obey the rules when you write version 2! 可扩展性非常重要，它会为你带来好处——但前提是你在编写版本 2 时遵守相关规则！

Most people do not use EXTENSIBILITY IMPLIED in the module header, preferring to explicitly include the ellipsis wherever necessary rather than have over-kill. This is probably clearer, and does allow separate exception handling in each case if this is desired (see below). 大多数人都不在模块头中使用“可扩展性”这一选项，而是选择在必要时直接添加省略号，而不是使用复杂的注释来表述。这样的做法可能更清晰明了，而且如果确实需要的话，还可以针对每种情况分别进行异常处理（详见下文）。

It is important to recognise what changes you can and cannot make in your version 2 specification if you want interworking with deployed version 1 systems to be possible without some separate version negotiation or requiring version 2 implementors to support "dual stacks". 重要的是要认识到，在版本 2 的规范中，你可以做出哪些改变，而哪些改变是不可实现的。这样就能实现与已部署的版本 1 系统的互操作，而无需进行额外的版本协商，也无需要求版本 2 的实施者支持“双堆栈”架构。

You can only add material where you have put your ellipses in version 1. Unless you originally wrote "EXTENSIBILITY IMPLIED", you cannot add new ellipses in version 2 (except in new types you add as extensions, of course), nor can you remove ellipses. And you cannot change existing types, for example from: 你只能在已经添加了省略号的版本中添加新的省略号。除非你最初写作的是“可扩展性已隐含在……中”，否则在版本 2 中你不能添加新的省略号（当然，可以在作为扩展类型中添加新的类型）。同时，你也无法删除现有的省略号。此外，你也不能修改现有的类型，例如从这样的类型开始：

## INTEGER 整数

to 到……去

## CHOICE { INTEGER , OBJECT IDENTIFIER } CHOICE { 整数, 对象标识符 }

A last addition to "what you can't do" (but of course this list is not exhaustive!) is optionality: You cannot add or remove OPTIONAL or DEFAULT from existing elements (although you can, if you wish, add another mandatory element at your ellipsis with the same type as an earlier OPTIONAL element). 最后一个属于“无法实现的功能”范畴的选项就是可选性：你不能对现有元素添加或删除“可选”或“默认”选项：不过，如果你愿意，也可以在原有的省略号位置再添加一个与之前的可选元素类型相同的必选元素。

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/a0059080-59e4-4cd9-913b-34e7587e39f7/34e48647b11bb6207d907c99875b0320f0d1689793bdf82d105251ae972b52a7.jpg)

## 2.6 Exception handling 2.6 异常处理

## 2.6.1 The requirement 2.6.1 要求内容

It is absolutely vital that when you use ellipsis you give a clear statement of what behaviour you expect: 当您使用省略号时，非常重要的是要明确说明您期望看到的行为：

<table><tbody><tr><td data-imt-p="1">Version 1 must be told what to do when hit by version 2 - and you must remember what you told it to do when you write version 2! 在版本 2 的攻击下，必须告诉版本 1 该做什么——而在编写版本 2 时，也必须记住之前告诉版本 1 要做什么！</td></tr></tbody></table>

• From version 1 systems if they receive added material. • 从版本 1 开始，当系统接收到新的素材时，就会执行相应的操作。

• How version 2 systems where mandatory fields have been added are to handle messages from version 1 systems. • 版本 2 的系统增加了一些必填字段，以此来处理来自版本 1 系统的消息。

The former is the more common case, as version 2 additions tend usually to be marked OPTIONAL. 前者更为常见，因为版本 2 中的新增功能通常会被标记为“可选”。

## 2.6.2 Common forms of exception handling 2.6.2 常见的异常处理形式

## 2.6.2.1 SEQUENCE and SET 2.6.2.1 序列与集合

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/a0059080-59e4-4cd9-913b-34e7587e39f7/5210ea855fc4aa07e32f679c37d63e5c84e8731e28a3b0956066ed2c98aff195.jpg)

Consider first added elements in a SEQUENCE or 首先考虑在一个序列中新增的元素。

SET. It is extremely common here to specify that these are to be silently ignored by version 1 systems (you then need to consider the implications of this in your version 2 protocol). SET。在这里，通常会有这样的规定：版本 1 的系统可以忽略这些参数（因此，在版本 2 的协议中需要考虑到这一点所带来的影响）。

The simplest cases first - silently ignore. 先处理最简单的情况——直接忽略它们。

ASN.1 tools are likely to support the removal of such material within the decode routines, so that the application code is never even aware that it has been hit by a version 2 message, unless action is taken to specifically indicate to the tool that such material has to be passed up (for example, for relaying). ASN.1 工具很可能会支持在解码过程中移除这类内容，因此应用程序甚至不会意识到自己受到了版本 2 消息的影响，除非有特定的措施来指示工具必须保留这些内容（例如，用于转发目的）。

## 2.6.2.2 CHOICE 2.6.2.2 选择

In the case of CHOICE, the situation is more difficult, and will depend on the precise interactions that occur within your protocol. 在 CHOICE 的情况下，情况更为复杂，这取决于你在协议中发生的各种具体互动。

The simplest case is your top-level CHOICE, where there is probably some defined responses to top-level messages from an initiator of an exchange, and you can make provision in those responses for some form of "Sorry, I have not implemented that, I am just a version 1 system" indication. (Such provision needs to be made in the version 1 response messages, of course.) 最简单的情况就是你的顶级选择功能。在这种情况下，对于发起交换的方的顶级消息，通常会有一些明确的响应方式。你可以在这些响应中加入类似“对不起，我还没有实现这个功能，我只是一个 1 版系统”这样的提示。（当然，这种提示需要在 1 版的消息响应中予以体现。）

Consider now the case where an extensible CHOICE is embedded in a sequence, and perhaps is an extensible choice of some character string types which in version 2 has new types added. 现在考虑这样一种情况：一个可扩展的选择列表被嵌入在一个序列中，而且这个可扩展的选择列表可能包含一些字符字符串类型的数据。在版本 2 中，这些类型被增加了新的属性。

It would be possible for a version 1 system receiving a version 2 value of such a type to treat that value as an empty string - effectively to ignore it, and to say in subsequent processing "No value available for this field". Of course, many other actions are possible, depending on your detailed protocol and the importance of the CHOICE field. Only you can decide what would be appropriate. 在版本 1 的系统中，如果接收到版本 2 中这样的值，那么可以将该值视为空字符串——实际上就是忽略它。在后续的处理中，就可以声明“该字段没有可用的值”。当然，根据具体的协议细节以及 CHOICE 字段的重要性，还可以采取许多其他的操作。最终由你来决定什么才是合适的方法。

## 2.6.2.3 INTEGER and ENUMERATED 2.6.2.3 整数类型和枚举类型

For extensible ranges on INTEGER, or for extensible ENUMERATIONS, the situation is not clear-cut. One option can be to define (in version 1) a mapping of any new version 2 value into a specific version 1 value, and specify the processing of that value as version 1 behaviour. 对于整数类型的可扩展范围，或者可扩展的枚举类型，情况并不明确。一种方案是在版本 1 中定义一种将任何新的版本 2 值映射到特定版本 1 值的方法，并指定该值作为版本 1 的行为来处理。

Another difficult one. Is there a version 1 value that all version 2 values can be mapped to without causing too many problems? Otherwise you need to look at just how the integer or enumeration is going to affect subsequent processing. 又是一个难题。是否存在一个“版本 1 的值”，所有“版本 2 的值”都可以映射到该值上，而不会造成太多问题？否则，你就需要仔细考虑一下整数或枚举值会对后续处理产生什么影响。

You need to try to think (when writing version 1) why you might be making the extension in version 2, and whether this behaviour would work out OK. You need to re-visit that discussion when you do eventually make version 2 additions! 在编写版本 1 的时候，你需要思考一下为什么要添加版本 2 中的功能，以及这样的设计是否真的可行。在最终完成版本 2 的添加内容时，你需要再次讨论这个问题！

Mapping to a version 1 value will not always be right, and the presence of a version 2 value may need to be carried as an "unknown value" through several stages of further processing (perhaps even into a database), and its effect on later code which is processing that value should be fully determined in version 1. 将数值映射到版本 1 的对应值并不总是正确的。而版本 2 的数值则可能需要作为“未知值”保留下来，在后续的多个处理阶段（甚至可能被存储到数据库中）。至于该数值对后续处理代码的影響，则需要在版本 1 阶段就完全确定下来。

## 2.6.2.4 Extensible strings 2.6.2.4 可扩展的字符串

The next case we need to consider are strings that had a limited (but extensible) maximum size in version 1, and the size in version 2 was increased. 下一个需要考虑的案例是那些在版本 1 时具有有限（但可扩展）的最大长度的字符串，而在版本 2 中，该长度得到了增加。

Two main options, both obvious: Require version 1 to support at the processing level longer strings, or truncate. 有两个主要的选项，而且都很明显：要么要求版本 1 在处理层面能够支持更长的字符串，要么就直接截断这些字符串。

Here again we see a conflict between the need to use constraints to get a tight PER encoding, and what we really want implementors to support in subsequent processing. 再次，我们看到了一种矛盾：一方面需要利用约束条件来实现更紧凑的 PER 编码；另一方面，我们又希望实现者在后续处理过程中能够支持更多的功能。

It would be possible in this case to say (in version 1) that the constraint determines the maximum for version 1 senders (it is all that is considered necessary at present), but that version 1 receivers should be capable of handling in their implementation sizes up to (say) twice the version 1 limit - and perhaps truncate after that. 在这种情况下，可以在版本 1 中这样描述：该限制条件决定了版本 1 发送者所能处理的最大数据量（目前来说，这是最必要的限制）。而版本 1 的接收者则应该能够在实现中处理高达版本 1 限制两倍的数据量——或许超过这个限制后数据就会被截断。

But again, depending on the subsequent use and processing of the string field, options such as treating a version 2 value as "unknown value" can also be appropriate. 不过，再次强调，根据字符串字段的后续使用和处理方式，将版本 2 的值视为“未知值”也是合适的选择。

## 2.6.2.5 Extensible bounds on SET OF and SEQUENCE OF 2.6.2.5 可扩展的 SET 和 SEQUENCE 集合的边界

This situation is very similar to the situation with bounds on strings. 这种情况与字符串长度限制的问题非常相似。

Very similar to strings, as you would expect. 正如预期的那样，它们与字符串非常相似。

It is clearly possible to require version 1 systems to support greater iterations on receipt. It is also possible to specify that they process the iterated material up to some limit of iterations, and then ignore the rest of the material (equivalent to truncating a string), possibly with some form of error return. 显然，可以要求版本 1 的系统在接收后能够支持更多的迭代操作。同时，也可以规定这些系统只能处理有限次数的迭代操作，之后可以忽略剩余的物料处理（相当于截断字符串），并且可能需要某种形式的错误返回机制。

Bounds on SET OF and SEQUENCE OF iterations are, however, relatively uncommon (with or without extension markers), so this case does not often arise. But the reader will be aware from earlier text that this means potential interworking problems or expensive implementations: few implementations will truly support an unlimited number of iterations unless told that they are required to do so. 不过，对“迭代次数”的限制其实并不常见（无论是否包含扩展标记），因此这种情况并不经常出现。不过，读者可以从前面的文本中了解到，这意味着可能存在兼容性问题或复杂的实现方式：除非明确说明需要支持无限次的迭代，否则很少有实现能够真正支持无限次的迭代操作。

The problem, however, is that real implementation limits are more likely to be on the total size of the iterated material when mapped into an implementation programming language data structure, rather than on the number of iterations per se. This perhaps explains why bounds on iteration counts are often left unspecified. 不过，问题在于，实际的实现限制更可能体现在将迭代结果映射至实现编程语言数据结构时的总大小上，而不是在迭代次数本身上。这或许可以解释为什么对迭代次数的限制通常并不明确说明。

## 2.6.2.6 Use of extensible object sets in constraints 2.6.2.6 在约束条件中使用可扩展对象集

Finally, we consider the case where an extensible Information Object Set is used as a table or relational constraint, as in ROSE. Here it would be common to have some form of error response such as the ROSE REJECT message if a version 2 object is received. 最后，我们考虑使用可扩展的信息对象集作为表格或关系约束的情况，就像在 ROSE 中那样。如果接收到的是版本 2 的对象，通常会有一个错误响应，比如 ROSE 中的 REJECT 消息。

<table><tbody><tr><td data-imt-p="1">Our last example, both the most complex and the simplest! 我们的最后一个例子，既是最复杂的例子，也是最简单的例子！</td></tr></tbody></table>

But in other cases the option of silently ignoring (perhaps linked to an additional "criticality" field) the version 2 object, or to treat it as a version 1 object, can also be possibilities. 但在其他情况下，也可以选择忽略这个版本 2 的对象（这可能与另一个“临界性”字段有关），或者将其视为版本 1 的对象。这两种情况都是可行的选择。

## 2.6.2.7 Summary 2.6.2.7 总结

In the above we have used six main mechanisms: 在上面的内容中，我们提到了六种主要的机制：

• Silently ignore. • 选择忽略。

• Give some form of error response. • 需要提供某种形式的错误响应。

<table><tbody><tr><td data-imt-p="1">Six mechanisms were described earlier - someone please find another one and we will have the magic seven! 之前已经描述了六种机制——请再找一个人来补充其中一种机制吧，这样我们就拥有完整的七种机制了！</td></tr></tbody></table>

• Map to a version 1 value or object. • 将某个版本 1 的值或对象映射到其他对象。

• Include a special "unknown value" in version 1 and specify its processing. • 在版本 1 中添加一个特殊的“未知值”字段，并说明对其的处理方式。

• Take the added material or unknown choice or value and relay it on unchanged. • 接受那些额外的材料或未知的选择或价值，并保持不变地传递它们。

• Process as much as possible then truncate (silently or with some form of error response). • 尽可能多地处理数据，然后将其截断（可以无声无息地完成，或者附带一些错误提示）。

Depending on the actual extensible construct, where that construct is used, the semantics associated with it, and how it affects later (perhaps much later) processing, we can choose one of these behaviours - or perhaps determine that another application-specific handling is more appropriate. 根据实际的可扩展结构、该结构在何种场景中的使用方式、与之相关的语义，以及它对未来（可能是很久以后）的处理有何影响，我们可以选择其中一种行为方式——或者决定采用另一种特定于应用的处理方式更为合适。

## 2.6.3 ASN.1-specified default exception handling 2.6.3 ASN.1 标准规定的默认异常处理机制

ASN.1 has been criticised for not specifying default exception handling behaviour, but I hope the above discussion of options makes it clear that good and appropriate exception handling must be related to the needs of a specific protocol, and will frequently differ in different places in the protocol. ASN.1 标准受到了批评，因为它没有明确规定默认的异常处理行为。不过，根据上述讨论，我们可以明确一点：有效的、恰当的异常处理方式必须符合特定协议的需求，并且在不同协议的不同部分中可能会有所不同。

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/a0059080-59e4-4cd9-913b-34e7587e39f7/d1a7e2b74d870eba93cb1d91e50273e262fe0be6d1c5d54b6115e7ee2e9c045d.jpg)

It would be positively dangerous to allow specifiers to put in ellipses without thinking through the implications of different sorts of version 1 exception handling behaviour. Ellipsis is not an easy option. It was introduced originally to ensure that the efficient PER encodings were such that some interworking would still be possible between version 1 and version 2 systems, but even with BER, if version 2 additions are made without a clear (earlier) specification of version 1 behaviour, serious problems result. 如果允许指定器在不充分考虑各种版本 1 异常处理行为影响的情况下使用省略号，那将是非常危险的。省略号并不是一个合适的选择。它最初被引入是为了确保高效的 PER 编码方式能够使得版本 1 和版本 2 的系统之间仍然可以进行一定程度的互操作。但是，即使使用 BER 编码，如果版本 2 的新增功能是在没有对版本 1 的行为进行明确规范的情况下进行的，那么就会引发严重的问题。

It may be difficult, it may be a chore, but giving serious consideration to extensibility issues and the associated exception handling is part of the job of a protocol specifier - the job is more than just defining a few data structures! 这可能很困难，也可能是一项繁琐的工作。但是，认真考虑可扩展性问题以及相关的异常处理措施，确实是一个协议规范者的重要职责——这不仅仅是定义一些数据结构那么简单的事情！

Unfortunately, if a bad job is done on exception handling in version 1, it is quite possibly a wholly new (and innocent!) group of specifiers producing version 2 that will suffer from the bad version 1 design. But I am afraid that is life! 不幸的是，如果版本 1 在异常处理方面做得不够好，那么版本 2 中出现的那些新的（且看似无害的）规范条款，很可能会受到版本 1 糟糕设计的负面影响。不过，唉，现实就是这样！

## 2.6.4 Use of the formal exception specification notation 2.6.4 使用正式的异常说明规范

Before leaving this discussion of extensibility, we must make some mention of the use of the formal exception specification notation (the notation that starts with "!"). 在结束关于可扩展性的讨论之前，我们必须提到一种正式的异常规范表示法（以“!”开头的表示法）。

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/a0059080-59e4-4cd9-913b-34e7587e39f7/50b606681376e7defe01a60290b42527658cd4dee413e781786c97c43a8ce49f.jpg)

The important thing (emphasised in the previous clause) is that exception handling should be very clearly stated, and the places in the protocol that particular handling is to be used are clearly identified. If there are relatively few uses of ellipsis, and particularly if the required exception handling is the same for all of them, then there is no real gain in including the formal exception specification notation, and English language text can suffice. (This might be the case if the only ellipses are at the end of SEQUENCE constructs, and the required behaviour in all cases is to silently ignore added material). 重要的是（如前文所述），异常处理部分应该表述得非常清楚，并且协议中明确指出应该使用哪种异常处理方式。如果省略的使用情况相对较少，尤其是当所有情况下所需的异常处理方式都相同时，那么使用正式的异常处理规范其实并没有太大意义，使用英文描述就足够了。（当然，这种情况可能发生在省略出现在“序列”结构末尾的情况下，因为在这种情况下，无论哪种情况，系统都只需忽略新增的内容即可。）

(Actually, that is not quite true - inclusion of the formal notation tells a reader that exception handling has been thought about, and that there is somewhere in the text details of required behaviour, and it is my own personal view that there should be formal exception specification notation wherever extensibility occurs, but I know that there are others that disagree with me!) （实际上，这种说法并不完全正确——使用正式的符号来表示异常处理机制，是为了让读者明白已经考虑到了异常处理的问题，并且文本中也会详细说明所需的行为。我个人认为，在具备可扩展性的地方，就应该使用正式的异常处理规范符号来表示。不过我知道有些人并不认同我的观点。）

In a protocol with perhaps four or five different exception handling procedures specified (to be used with different instances of ellipsis, each behaviour applying to several instances of ellipsis), then use of the formal notation (perhaps simply using "!1", "!2, etc) on each ellipsis can be a simple and convenient way of identifying clearly which behaviour applies to which. Something similar to this is done very effectively in the ROSE protocol (using value reference names for "1", "2", etc), as described in Section II Chapter 6. 在协议中，可能会规定四到五种不同的异常处理机制（这些机制适用于不同的省略号实例，每种机制又可应用于多个省略号实例）。此时，可以在每个省略号上使用正式的符号表示法（比如简单地使用“!1”、“!2”等），这样就能清晰地识别出哪种机制适用于哪个实例。类似的做法在 ROSE 协议中得到了非常有效的实现（使用“1”、“2”等值的引用名称来表示），具体细节请参考第 6 章第二节的内容。

## 2.7 Parameterization issues 2.7 参数化问题

Parameterization is powerful and can be the only way of achieving certain "re-usability" goals, particularly where one group provides a carrier protocol and several other groups fill in the holes in different ways to produce a complete specification. 参数化设计是一种非常强大的方法，它可能是实现特定“可重用性”目标的唯一途径。特别是当某个团队负责提供基础协议，而其他团队则以不同的方式填补其中的空白，从而形成一个完整的规范时。

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/a0059080-59e4-4cd9-913b-34e7587e39f7/9610e63a25ddb6f3a979eaea379f33382be7b35ad2610de3ead33363fc7323a4.jpg)

But if a parameterized type is instantiated only a limited number of times within a single specification, then it may be that parameterization is unnecessary, and that the same effect can be achieved more clearly by using different (but similar) type or value definitions. 但是，如果某种参数化类型在单个规范中只会被实例化有限次，那么可能就不需要进行参数化了。通过使用不同但类似的类型或值定义，同样可以达到相同的效果。

Object Set parameters of the abstract syntax are a very good way of providing precise specifications of "must implement all, but can add" versus "can implement a subset, but can't add" versus "this is a guide, add or subtract", but are currently unfamiliar to many readers of ASN.1, and should be accompanied by explanatory text. 在抽象语法中设置参数是一种很好的方式，它可以清晰地区分“必须实现所有功能，但可以添加某些内容”与“可以实现部分功能，但不能添加某些内容”的情况，以及“这是一个指导性规范，可以增减内容”的情况。不过，目前很多使用 ASN1 的读者并不了解这种表达方式，因此应该附带相应的解释文本。

Integer parameters of the abstract syntax (used in bounds) are also a very good way of clearly indicating that (for whatever reason), you have chosen to leave implementation-dependent features in your specification. 在抽象语法中，整数参数也是一种很好的方式，可以清楚地表明：出于某种原因，您选择将依赖于实现的特性留在了规范中。

But in both these cases, it is essential that exception handling procedures be fully specified, as discussed earlier. 但在这两种情况下，正如之前所讨论的那样，必须完全明确异常处理流程。

The use of the {...} notation is a form of parameterization, declaring that the object set to be used is implementation dependent, and is generally a less clear and precise notation than parameterization (but there are those that would disagree!). 使用{...}这种表示法是一种参数化方式。它表明所指定的对象取决于具体的实现情况，这种表示法通常不如参数化方式那么清晰和精确（不过，也有人不认同这种观点！）。

It is important if this notation is used, that text clearly specifies how it is intended (by whom and where) for the specification to be completed, and what implications there are on interworking, and what exception handling is to be applied. If that is done, this notation can produce a less cluttered specification than a lot of different parameters (object sets of various classes) being passed from the top-level type all the way down to where they are being used as a constraint. 如果采用这种表示方式，那么文本中明确说明该规范是由谁在何处制定的非常重要。同时，还需要明确关于相互协作的注意事项，以及需要如何处理异常情况。只要做到这一点，这种表示方式就能比使用许多不同参数（各种类别的对象集合）来传递信息的方式，使规范更加简洁明了。

Finally, remember (Section II, Chapter 7) that if you have a lot of parameters of a parameterised type (or other form of reference name), you can reduce them to a single object set parameter by defining a suitable Information Object Class whose objects carry the complete set of information for each parameter. This can be a very useful simplification and reduction of verbosity in your text. 最后，请记住（第 7 章第 II 节）：如果你有很多参数化类型的参数（或其他形式的引用名称），你可以将这些参数简化为单个对象集参数。通过定义一个合适的信息对象类，使得每个对象的参数都包含完整的相关信息，这样就能大大简化文本中的冗余信息。这确实是一种非常有用的简化方式，能减少文本的复杂性。

## 2.8 Unconstrained open types 2.8 无约束开放类型

Unconstrained open types - elements of sequences looking like, for example: 无约束的开放类型——序列中的元素，比如：

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/a0059080-59e4-4cd9-913b-34e7587e39f7/65769f7f387f58331163e4ce633614f1208502e7cb56dee68533e01a3ae0c029.jpg)

## OPERATION.&Type 操作与类型

are syntactically allowed in ASN.1 as part of the Seoul (see Section IV Chapter 1) introduction of the Information Object Class concept, but that was largely in response to a perceived need to provide syntax that was semantically equivalent to the old "raw ANY", and I hope the reader (at least those that have read Section II) by now appreciates that a "raw ANY" (and hence an unconstrained open type) is a BAD THING. 在 ASN.1 中，这些语法结构是被允许的。这是作为“信息对象类”概念引入的一部分（详见第 1 章的第四部分）。不过，这些规定的实施主要是出于一种需求——即需要提供一种在语义上与旧的“原始 ANY”结构等效的语法规则。希望读者们（至少那些阅读了第二部分内容的人）能够理解，所谓的“原始 ANY”结构（以及由此产生的无约束开放类型）其实是一种糟糕的设计。

All that a tool can deliver for this construct is an octet string. And even the implementor of the application has no clear indication of where to look to find out the possible types that can occur in this element, the semantics associated with those types, and which type has actually appeared in a given instance of communication, that is, how to decode and interpret the octet string. 该工具为这种结构所能提供的内容仅是一个八位元字符串而已。甚至应用程序的实现者也无法明确知道应该去哪里查找有关该元素可能存在的各种类型的信息、与这些类型相关的语义信息，以及在实际的通信实例中究竟出现了哪种类型的信息。也就是说，人们无法解码和解释这个八位元字符串所包含的内容。

As a specifier in the years 2000 onwards, please don't use this form, even 'tho' you are allowed to! Look at the ROSE chapter (Section II Chapter 6) to see how to give a more precise and implementable specification of these sorts of constructs. I suspect that if ASN.1 is still going strong in 2010, forbidding this unconstrained construct may become possible (I am likely to campaign for it!), provided nobody shouts "1990, 1990!" (again, see Section IV Chapter 1!). 在 2000 年代及之后，作为规范说明者，请不要使用这种形式来表达描述，尽管你是可以这么做的！请参阅 ROSE 规范中的相关章节（第二部分，第六章），了解如何给出更精确且易于实施的这类结构的描述。我认为，如果 ASN.1 在 2010 年仍然保持强大的发展势头，那么禁止这种无约束的结构可能就会成为现实（我可能会积极倡导这一点！），只要没有人喊出“1990 年，1990 年！”这样的口号即可（同样，请参阅第四部分，第一章）。

## 2.9 Tagging issues 2.9 标签相关问题

If you are writing a new specification, you should use AUTOMATIC TAGS (and - as an aside - not specify enumeration values for enumerations). But if you are adding to an existing specification, life can be more complicated. 如果你正在编写新的规范文档，那么应该使用 AUTOMATIC TAGS 功能（另外，不要为枚举类型指定枚举值）。但如果你是在对已有的规范进行补充修改，情况可能会更复杂一些。

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/a0059080-59e4-4cd9-913b-34e7587e39f7/18c78ca07d19ca8aaf0bd550daa7242373d939bb01e7572bee9cb7da46211385.jpg)

Remember that a textually present tag construct automatically disables automatic tagging in a CHOICE, SEQUENCE, or SET - you are back in control (with IMPLICIT tagging). 请记住，文本中出现的标签结构会自动使系统不再进行自动标签添加操作——此时您可以重新控制这一过程（使用隐式标签添加功能）。

If you have good reasons not to use AUTOMATIC TAGS, then you need to have a much greater understanding of tagging, but should then always use IMPLICIT TAGS in your module header. Using an explicit tagging environment in modern specifications would be confusing, and you would either have a very verbose protocol (with BER), or a specification that was littered with the word IMPLICIT. 如果你有充分的理由不使用自动标签，那么你需要对标签的使用有更深入的理解。不过，无论如何，你都应该在模块头文件中使用显式标签。在现代规范中，使用显式标签环境会导致混乱，要么会使协议文本变得冗长，要么会让规范中充斥着“显式”这个词。

If you choose, to specify that certain tags are EXPLICIT, the reasons for this will be obscure to most readers, and you should indicate in your text why this was done. 如果你选择明确说明某些标签是可选的，那么对于大多数读者来说，这些标签被明确指定的原因将会很模糊不清。因此，你应该在文本中明确说明这样做的原因。

There are usually two possible reasons: in an implicit tagging environment, tags on a choice type do in fact become explicit tags. It can help people implementing without a tool if this is made clear in the specification by writing in the word EXPLICIT (it is redundant to a computer, but may help a human being). 通常有两种可能的原因：一种是处于隐式标签的环境中，此时选择项上的标签实际上变成了显式的标签。如果规格说明中明确注明这一点，并写上“EXPLICIT”这个词，那么对于不使用工具的人来说会有所帮助。虽然对于计算机来说这有些多余，但对于人类来说或许还是有帮助的。

The other reason is some desire to essentially associate some semantics or categorization with particular tag values, and to ensure that (in BER) there is a length wrapper round the actual type being identified. A similar motivation comes from use of a type constraint on an open-type when PER is used. Both of these (rather obscure) devices appear in some security specifications. 另一个原因是，人们希望为某些标签值赋予一定的语义或分类功能，同时确保在 BER 中，实际被识别的类型周围有一个长度限制。这种动机也出现在使用 PER 时对开放类型进行类型约束的情况中。这两种相当复杂的机制在某些安全规范中都有体现。

Of course, all the above discussion of tagging assumes you have written your type definitions within the defined ASN.1 module framework, not just written it stand-alone! I am sure that readers of this book would never do that! 当然，上述关于标签的讨论都假设了您已经将类型定义写在规定的 ASN.1 模块框架内，而不是单独书写的！我相信本书的读者绝不会这样做！

## 2.10 Keeping it simple 2.10 保持简单

ASN.1 has a number of powerful mechanisms for providing clear specifications, but you will often find people recommending that some of them not be used in the interests of a simpler specification. ASN.1 提供了许多强大的机制来制定清晰的规范，但人们通常会建议为了使规范更加简洁，有些机制可以不用。

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/a0059080-59e4-4cd9-913b-34e7587e39f7/421b6f0fae836f035fed97e6cd76635ed5f08fad7ba68e69f0833455177ab221.jpg)

There can sometimes be justification in this, but what appears simple tends very much to depend on what has been frequently encountered in the past, and new notational constructs may take a little time to gain a ready acceptance and recognition. Once understood and recognised, they can provide a clearer (and hence simpler) specification than the alternative of English text. 有时候，这种表达方式确实有其合理性，但看似简单的表达方式实际上往往取决于人们过去是否经常使用某种特定的表达方式。新的符号系统可能需要一些时间才能被广泛接受和认可。一旦人们理解了这些符号系统，它们就能比使用英语文本提供更清晰、更简单的表达方式。

There is a second reason sometimes put forward for not using certain constructs, which is that some current-day tools will accept those constructs, but make no use of them, instead relying on so-called "compiler directives" (usually a specialised form of ASN.1 comment) that provide the same effect (and which in some cases pre-date the introduction of the notation into ASN.1). 有时候，人们会提出第二个理由来解释为何不使用某些构造方式。那就是，虽然一些现代工具能够接受这些构造方式，但它们并不会实际使用它们。相反，这些工具会依赖所谓的“编译器指令”来实现相同的效果（在某些情况下，这些指令甚至早于 ASN.1 表示法的出现）。

Notations that fall into this category for either or both reasons are (in no particular order): 出于任一或两种原因，属于这一类别的注释包括（顺序不固定）：

• Use of ABSTRACT-SYNTAX. • 抽象句法的使用。

• Use of parameters of the abstract syntax (variable constraints). • 使用抽象语法中的参数（变量约束）。

• Use of a type constraint on an Open Type. • 对开放类型使用类型约束。

• Use of the {...} notation. • 使用 {...} 这种表示方式。

• Use of the ! exception specification notation. • 使用!表示法来指定异常情况。

I would not recommend avoidance of any of these, but I would caution that where these constructs (or of any other construct that is not - yet - widely used) are used, it can be sensible to include an ASN.1 comment, or introductory text in the main body of the specification, saying how and why the constructs are being used and their precise meaning for this protocol. That way, such constructs will become familiar to all, and become "simple"! 我并不建议避免使用这些结构。不过，我提醒的是，在使用这些结构时（或者任何尚未被广泛使用的结构时），在规范的主体部分添加一些说明是明智的做法。这些说明可以解释这些结构为何被使用，以及它们在这个协议中的具体含义。这样，所有相关人员都能理解这些结构，从而使其变得“简单”易懂。

## 3 Issues for implementors 实施者面临的 3 个问题

This section is slightly shorter than the "issues for specifiers", but quite a few of the earlier topics recur here. The difference is that you (the implementor) are on the receiving end, and if the specifiers have produced ambiguities or left implementation dependencies, you have to sort them out! (Implementors would also be well-advised to read carefully the two earlier parts of this chapter, as well, of course, as the whole of Section II.) 这一部分的内容比“规范说明者需要解决的问题”要简短一些，但仍有不少之前讨论过的话题在这里再次出现。不同的是，现在你作为实施者处于被动地位，如果规范说明产生了歧义或留下了实施上的依赖问题，你就必须自行解决这些问题！当然，实施者也建议仔细阅读本章的前两部分内容，以及第二部分的所有内容。

## 3.1 Guiding principles 3.1 指导原则

Principles for Internet implementors are often stated as: 互联网实施者应遵循的原则通常如下：

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/a0059080-59e4-4cd9-913b-34e7587e39f7/38782f259da13cc9987f15f5edd681a6a28f17bf413d7b98c5fd5abd2158e7e5.jpg)

• Strictly confirm to the specification in what you send. • 请严格遵循所发送产品的规格要求。

• Be forgiving in what you receive. • 在接受事物时，要心怀宽容之心。

That sounds like good advice, and it is often possible to write code that understands and processes things that are strictly invalid. 这听起来像是很好的建议。通常，我们可以编写能够理解并处理那些完全无效情况的代码。

This situation arises more often in Internet protocols than in ASN.1-based protocols, because the use of a text-based format often introduces more redundancy, and hence scope for "understanding" formally incorrect encodings, and because most Internet protocols rely on this principle to provide for interworking between version 1 and version 2 of a specification. The situation will rarely arise with PER, which has almost no redundancy, and an explicit extensions bit! 这种情况在基于互联网的协议中出现得更为频繁，因为在 ASN.1 基础的协议中，文本格式的使用往往会导致更多的冗余，从而增加了理解那些形式上错误的编码的可能性。而大多数互联网协议都采用这种机制来实现规范版本 1 和版本 2 之间的互操作。不过，在 PER 协议中，这种情况很少发生，因为 PER 几乎没有冗余，而且还有明确的扩展位可以用来指示某些特性。

With BER you could decide to be forgiving if you got a universal class 16 tag (SEQUENCE) with the primitive/constructor bit set to "primitive". Or you could be accidentally forbidding by just not bothering to write the code to check that bit once you had detected universal class 16! 使用 BER 机制，你可以选择在检测到通用类 16 标签时予以原谅（如果该标签的“primitive/constructor”位被设置为“primitive”的话）。或者，你也可以选择不编写相应的代码来检查该位，从而避免意外地禁止某些情况的发生。

But if you are forgiving of errors (a primitive sequence, or integers exceeding stated bounds say), you should consider carefully the effect of being forgiving. This issue is very strongly related to extensibility - what you have got is implied extensibility (that you yourself have decided to introduce), and you are on your own to define the best exception handling procedures. 不过，如果你能够原谅这些错误（比如一些原始的错误代码，或者整数超出了规定的范围），那么你就需要仔细考虑这种宽容行为所带来的影响。这个问题与可扩展性密切相关——你所拥有的功能意味着存在可扩展性（即你自己决定引入的这种特性），而如何设计最佳的异常处理机制则完全取决于你自己的判断。

I would recommend that in the case of ASN.1-based protocols it is rarely a good idea to silently ignore and process incorrect encodings which you are able to give meaning to (your own extensions). You may well choose to go on processing, but the error (with details of the sender) should at least be logged somewhere, and if the protocol permits it, sent back to the sender in some form of error message. 我建议，在基于 ASN.1 的协议中，很少有必要对那些可以被解析为有意义的数据进行默默忽略处理。虽然可以选择继续处理这些数据，但错误信息（包括发送者的详细信息）至少应该被记录下来，如果协议允许的话，还应该以某种错误消息的形式返回给发送者。

## 3.2 Know your tool 3.2 了解你的工具

In any development environment there are an immense number of features in the chose tool that can make an implementors life easier. It is important to become familiar with those features/options/parameters of the tool. 在任何开发环境中，都有许多功能可以帮助开发者更轻松地完成工作。因此，熟悉这些工具的功能、选项和参数是非常重要的。

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/a0059080-59e4-4cd9-913b-34e7587e39f7/47e2542608eb01b87aa4c7bb97e0c40fd51e517ba3df6c356279ebe3ad19fd3f.jpg)

Part of the "quality" aspects of a tool are the ease with which you can acquire an understanding of the functions it provides, and the detailed syntax needed to obtain those functions. Of course, you may regard the actual functions it does provide as more important, but functions that are not obvious in associated documentation or help files or are not easy to invoke are almost as bad as missing functions. 一个工具的“质量”体现在多个方面，其中之一就是用户能够轻松理解该工具提供的功能，以及获取这些功能所需的详细语法说明。当然，有些人可能认为工具本身的功能更为重要，但是那些在相关文档或帮助文件中并不明显，或者难以调用的功能，其实和没有这些功能一样糟糕。

## 3.3 Sizes of integers 3.3 整数的大小

This issue has been heavily discussed in the section for specifiers (which is relevant to implementors too). Tools will often give you control over the length of integer they map to, on a global basis (usually by command-line parameters), but will also give an over-ride for individual fields, usually by "compiler directives" - special forms of ASN.1 comment. 这个问题在针对实现者的部分中有过充分的讨论。工具通常能够让你全局性地控制整数类型的长度（通常是通过命令行参数来实现），同时也会为单个字段提供额外的配置选项，这通常是通过“编译器指令”来实现的——这是一种特殊的 ASN.1 注释形式。

You need to know exactly what was intended. With luck, the specification will tell you. Otherwise a good guess is four octets! But if you guess, cover your back - raise it as an issue in your implementatin team. 你需要确切知道具体的设计意图。幸运的话，规格说明会告诉你答案。否则，一个合理的猜测是 4 个八位组！不过，如果你只是猜测的话，最好把这个问题提给你的实施团队去处理。

The better tools will also allow you to specify that certain integer fields are to be treated as strings to allow them to be arbitrarily large (using dynamic memory allocation) subject to available memory. 更先进的工具还允许你指定某些整数字段应被视为字符串类型，这样它们就可以拥有任意大的长度（通过动态内存分配来实现），只要内存足够即可。

You have two problems: 你面临两个问题：

• Interpreting the intent of the specifier of the protocol. • 理解协议中指定条款的意图。

• Getting your tool to do what you want, if what you want is not part of the formal specification or contradicts it! • 让你的工具能够完成你想要的任务——当然，前提是你所期望的功能不属于正式规范的内容，或者不会与规范相矛盾！

The latter depends on the quality of the tool. So if your protocol specification says that a field is "INTEGER (0..7)", but you want it (for ease of programming and/or writing to a database) to be mapped to a four-octet integer, rather than a two or one-octet integer in the programming language of your choice, are you able to do it? 后一种情况取决于工具的质量。例如，如果您的协议规范规定一个字段应该是“INTEGER(0..7)”，但您希望为了编程的方便以及/或写入数据库的需要，将该字段映射为四个八位整数，而不是您所选编程语言中的两个或一个八位整数，那么您是否能够实现这一点呢？

The former can be the more difficult problem! If specifiers have obeyed the guidelines/exhortions in this area given earlier in this chapter, you should have no problem, but otherwise you may need to try to guess (from knowledge of the application and from other parts of the specification, or by enquiry from others (see below)), just what the intention was, or how others are interpreting it. 前者可能是一个比较困难的问题！如果规范制定者遵循了本章前面提到的相关指南/建议，那么应该不会有问题。但否则的话，你可能需要尝试根据应用程序的实际情况以及规范的其它部分来推测其意图，或者向他人咨询以获取更多信息（见下文）。

## 3.4 Ambiguities and implementation-dependencies in specifications 3.4 规范中的歧义与实施依赖项

Don't believe the box! It is hard to write a specification that is completely clean (particularly in the first published specification), and has totally specified the bits on the line that the implementation is required to produce under all circumstances. (I hate to say it, but if done well, the specifier’s job is harder than the implementor’s, but in the specifier's case it is a lot easier to do the job badly and not be found out! 不要轻信那些文档！要编写一个完全清晰的规范文件是非常困难的（尤其是在第一个发布的规范文件中），而且必须明确说明在实现过程中各种情况下的具体细节。不得不说，如果做得好，编写规范文档的工作比实现代码要困难得多；但如果是编写规范文档的话，即使做得不好，也更容易蒙混过关而不会被发现。

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/a0059080-59e4-4cd9-913b-34e7587e39f7/61b5f4ed177844599f539088a7b49bbe1c9e4c13fee4f7a088ef4490c560a32e.jpg)

The most important advice to implementors - and this is very important - is that if you find things that are not said, raise them as an issue, at least within your team, but preferably with the specifiers themselves through some appropriate mailing list or group. 对实施者来说，最重要的建议就是——这一点非常关键——如果你发现了一些未被提及的问题，一定要把它们提出来讨论，至少是在你的团队内部进行讨论，但如果可能的话，还可以通过适当的邮件列表或小组来与相关的指定人员进行沟通。

Some of you will have heard of the Alternating Bit Protocol. A very similar protocol was specified for use over a particular LAN (no names, no pack drill!) in the late 1970s, but the specification did not say what the behaviour was to be when an ACK with the wrong number was received. The implementors decided that the "right" action was to immediately retransmit the last message (with the same sequence number), trusting the receiver to discard duplicates. Result: parasitic transmissions. Throughput dropped to half until the load backed off, with every packet being transmitted twice! 你们当中有些人可能已经听说过交替位协议。在 20 世纪 70 年代末，有一种类似的协议被提出用于特定局域网中的通信（不会透露具体名称，也不会故意制造困惑！）。不过，该协议并没有明确说明在接收到错误编号的确认消息时该如何处理。实现者们认为，正确的做法应该是立即重新传输最后一条消息（使用相同的序列号），并相信接收方会丢弃重复的数据包。结果就是出现了寄生传输现象。吞吐量下降了一半，直到负载逐渐减轻为止，而每包数据都被重复传输了两次！

If there is one clear duty on implementors, it is not to take their own decisions when specifications are unclear! 如果给实施者设定了一项明确的职责，那就是在规格不明确的情况下不要自行做出决策！

## 3.5 Corrigenda 3.5 修正说明

Implementors need to be as much aware as those in a more managerial capacity of what corrigenda are around, their status, and how they might impact the implementation in the future. 实施人员需要像那些具有管理职责的人一样，了解相关规范的内容、它们的状态，以及这些规范未来可能对实施过程产生的影响。

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/a0059080-59e4-4cd9-913b-34e7587e39f7/ccbc1c2063210d090c3fd5f1ba3200742630e878510afb05b89eb3ad3b7c898d.jpg)

If you know something is coming, its arrival can be a lot less painful if it has been planned for! 如果你知道某件事情即将发生，那么如果提前做好了准备，它的到来就不会那么令人痛苦了！

## 3.6 Extensibility and exception handling 3.6 可扩展性和异常处理

This text is getting repetitive! If you are told clearly what the bits on the wire should be (and what you do in response to them), and how you are to handle unknown stuff coming in, and if your decoding tool is sufficiently good and flexible, then there are no problems. 这段文字看起来有些重复了！如果能够清楚地知道线路上的各个位应该是什么值（以及面对这些值时该如何处理），同时又能妥善处理可能出现的未知情况，而且你的解码工具足够强大且灵活，那么就不会有问题了。

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/a0059080-59e4-4cd9-913b-34e7587e39f7/b85b814eaa3fb617220c04cf12290d6ad88a2e1912bda46e90c75a1992f9bf74.jpg)

Otherwise worry! 否则就担心吧！

## 3.7 Care with hand encodings 3.7 对手工编码的注意事项

If, for whatever reason, you do not even have access to a well-debugged library of routines to encode simple types like INTEGER, etc, let alone access to a fully-fledged ASN.1 compiler, then you deserve sympathy! 如果由于某种原因，你甚至无法使用那些已经经过充分调试的库函数来编码简单的类型，比如 INTEGER 等，更不用说使用功能齐全的 ASN.1 编译器了，那么你确实值得同情！

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/a0059080-59e4-4cd9-913b-34e7587e39f7/d04a2e8fbf3c22707876f683ecf925cc65c62a1ecaacc651326b88b517dbd67e.jpg)

Producing ASN.1 encodings from scratch, by hand, is not impossible, and in one sense, not even difficult. (But it is probably easier to get it right first time with BER than with PER, unfortunately, due to the large number of optimisations in PER.) It is just time-consuming and error prone. 从头开始手动生成 ASN.1 编码并非不可能，某种程度上来说也不算困难。不过，遗憾的是，使用 BER 方法首次就正确地生成编码要比使用 PER 方法容易得多，因为 PER 方法包含了大量的优化措施。不过，这样做会耗费大量时间，并且容易出错。

First of all, you need to read Section III rather more carefully than you otherwise would! Then you need to spend a lot of time with the actual ASN.1 encoding specification that you are going to be using. 首先，你必须比平时更仔细地阅读第三部分的内容！此外，你还需要花费大量时间研究实际的 ASN.1 编码规范，因为这些规范正是你将要使用的标准。

Second, you will need some sort of ad hoc "line monitor" tool to display what you are producing in a format that will make it easy for you to check that you are producing what you intended. 其次，你需要一种临时的“生产线监控”工具，能够以易于查看的格式显示你的生产成果，这样就能轻松确认你是否按照预期进行了生产。

And lastly, you really need an ASN.1 tool! Not one that necessarily runs on your platform (lack of that is presumably why you are not using a tool), but one that can run on some other communicating platform, take your output, and display the values it thinks you are transmitting. 最后，你真的需要一款 ASN.1 工具！这个工具不一定必须运行在你的平台上（可能正是因为缺乏这样的条件，你才没有使用工具），但它应该能够在其他通信平台上运行。该工具可以接收你的输出结果，然后显示它认为你正在传输的值。

Well, that was almost last! There is nothing like final inter-operability testing with a totally different complete implementation, particularly if it (and you!) have good error logging of things you think are erroneous about what you are receiving. 嗯，差不多就到最后阶段了！现在需要进行最终的互操作性测试，会使用完全不同的实现方式来进行测试。当然，前提是你们能够很好地记录那些看似错误的操作，以及系统所遇到的各种错误。

## 3.8 Mailing lists 3.8 邮件列表

There is a mailing list you can use for general ASN.1 enquiries (see Appendix 5 for a link to this), and many protocol specifications today are supported by mailing lists, news groups, Web pages, etc. 有一个邮件列表可用于处理一般的 ASN 相关查询（链接见附录 5）。如今，许多协议规范都是通过邮件列表、新闻组、网页等方式来进行维护和交流的。

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/a0059080-59e4-4cd9-913b-34e7587e39f7/f48a711f97177a04632989edc9980b8ab779bc9146c7e29b659967ec2af87b1c.jpg)

These resources can be very valuable to you. (As can people that give ASN.1 and specificprotocol courses, who are usually willing to leave their e-mail addresses with you and to answer queries subsequent to their courses. 这些资源对您来说可能非常有价值。（同样，那些提供 ASN.1 和特定协议课程的人也很有帮助，他们通常愿意留下自己的电子邮件地址，并在课程结束后回答您的疑问。）

## 3.9 Good engineering - version 2 **will** come! 3.9 工程性能良好——版本 2 即将推出！

Any protocol you implement will have a version 2 specification that you or your descendants (team-wise) will have to implement. 你所实现的任何协议都會有一份版本 2 的规范，你或你的后代们（以团队形式）都必须遵守这份规范。

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/a0059080-59e4-4cd9-913b-34e7587e39f7/b03d49b904cc5b522714645b625d32c1603ab7a04e562804a6fbeef0322bd28d.jpg)

All the usual good engineering principles apply to make sure that your code and documentation enables others to modify your implementation to support the version 2 specification as and when this is produced. 所有常见的优秀工程原则都适用于确保你的代码和文档能够让人们随时修改你的实现，以符合 2 版规范的要求。随着 2 版规范的发布，这些修改将变得十分容易。

You will get some hints in the extensibility provisions of version 1 of what areas the specifiers expect to change. This can help you to engineer the structure of your implementation to be easily able to accommodate those changes when they arrive. 在版本 1 的可扩展性条款中，你会找到一些提示，说明这些规范定义者希望改变哪些部分。这些提示可以帮助你设计实现结构，以便能够在这些变更发生时轻松应对。

Just as getting exception handling as right as possible is a challenge for specifiers, getting an implementation architecture that enables extensions to be easily handled (and providing correct exception handling in version 1 when there are as yet no version 2 systems around to test against) is the challenge for the implementor. As for specifiers - this is part of your job, get it right! 对于规范编写者来说，尽可能实现完善的异常处理机制确实是一个挑战；而对于实现者而言，则面临着如何构建一种能够轻松处理扩展功能的实现架构的挑战（同时，在还没有版本 2 的系统可供测试的情况下，还需要在版本 1 中提供正确的异常处理机制）。至于规范编写者——这确实是你们的工作职责之一，一定要把事情做好！

## 4 Conclusion 4. 结论

And that completes this first Section of the book. Many of you will be leaving us at this point (although you may find some parts of Section IV interesting). I hope you have found it useful. The more technically-minded will no doubt be proceeding to Sections II and III – read on! 至此，本书的第一部分内容已经讲完了。你们中的许多人现在会离开这里（不过，第四部分的某些内容或许还是值得你们继续阅读的）。希望这些内容对你们有所帮助。那些对技术方面比较感兴趣的人，想必会继续阅读第二部分和第三部分的内容吧——请继续阅读下去吧！

## SECTION II 第二部分

## Further Details 更多详细信息

# Chapter 1 The object identifier type 第一章 对象标识符类型

(Or: What's in a name?) （或者：名字有什么意义呢？）

Summary: The object identifier type, and its associated hierarchical name-space is heavily used by protocol specifiers that use ASN.1. It provides a world-wide unambiguous naming scheme that anyone can use, and has been used to name a very wide range of "things". 摘要：对象标识符类型及其相关的分层命名空间被许多使用 ASN.1 协议的规范定义所广泛应用。它提供了一种全球范围内统一的命名方案，任何人都可以使用这种方案。实际上，这种命名方式已经被用于为各种各样的“对象”命名。

Object identifiers are used to identify: 对象标识符用于识别：

a) ASN.1 modules a) ASN.1 模块

b) Abstract and transfer syntaxes b) 抽象语法和转换语法

c) Managed objects and their attributes c) 被管理的对象及其属性

d) Components of Directory (X.500) names d) 目录名称的组成部分（X.500）

e) Headers of MHS messages (X.400) and MHS Body Types e) MHS 消息的头部信息（X.400 协议）以及 MHS 消息的主体内容

f) Banks and Merchants in Secure Electronic Transactions f) 银行在安全电子交易中的作用与职责

g) Character Repertoires and their encodings g) 字符集及其编码方式

h) Parcels being tracked by courier firms h) 由快递公司负责追踪的包裹

i) And many other "things" or "information objects". i) 还有许多其他的“事物”或“信息对象”。

## 1 Introduction 1 引言

Final discussion of the object identifier type has been deferred to this "Further Details" Section, but as a type notation it is as simple as BOOLEAN. You just write: 关于对象标识符类型的最后讨论被推迟到“更多细节”部分进行。不过，作为一种类型标记，它其实非常简单，就像 BOOLEAN 那样。你只需要这样写：

Object identifiers were introduced into ASN.1 in 1986 to meet a growing need for a name-space with globally unique short identifiers which permitted easy acquisition of name-space by anybody. 在 1986 年，为了满足对具有全球唯一性且简短的标识符的需求，对象标识符被引入到 ASN.1 标准中。这一标准旨在让任何人都能轻松获取命名空间。

OBJECT IDENTIFIER 对象标识符

all upper case. The complexity arises with the set of values of this type, and with the value notation. 全部使用大写字母。这种类型的数值集合以及数值表示方式所带来的复杂性是显而易见的。

First, we should note that the set of values is dynamically changing on a daily basis, and that no one computer system (or human-being) is expected to know what all the legal values are. The value notation has a structure, and each object identifier value can be mapped onto a sequence of simple integer values, but these structures do not matter. Treated as an atomic entity, an object identifier value (and its associated semantics) is either known to an implementation, or not known. This is all that matters. 首先，我们需要注意到，这些值的集合是每天都在动态变化的，而且预计没有任何一个计算机系统或人类能够知晓所有合法值的具体内容。值表示法具有某种结构，每个对象标识符都可以映射到一个由简单整数值组成的序列上，但这些结构其实并不重要。将对象标识符视为一个原子实体，那么要么实现方知道该标识符及其相关的语义，要么就完全不知道它。这才是最重要的。

When this type is used in a computer protocol, it is almost always used in circumstances where there is (or should be!) a clear specification of the exception handling that is required if a received object identifier value does not match a known value. 当这种类型在计算机协议中被使用时，通常都是出现在这样一种情况下：即需要明确指定当接收到的对象标识符值与已知值不匹配时该如何处理这种情况。

Note that all current ASN.1 encoding rules provide a canonical encoding of object identifier values (no encoder options) which is the same for all encoding rules and is also an integral multiple of eight bits (an octetstring). So storing those object identifier values for which the semantics is known as simple octet strings containing the ASN.1 encoding, and comparing incoming encodings with these, is a viable implementation option. 请注意，当前所有的 ASN.1 编码规则都提供了一种标准的对象标识符值编码方式（没有可选的编码选项）。这种编码方式适用于所有编码规则，并且是 8 位比特的整数倍——即一个字节字符串。因此，将那些具有已知语义的对象标识符值存储为简单的字节字符串，并将传入的编码方式与这些字节字符串进行比较，是一种可行的实现方案。

We have met values of the type already as a way of identifying modules, and have seen some of the value notation. We must now discuss the model underlying such values and the allocation of 我们已经使用了某种类型的值来标识模块，并且已经了解了一些关于值表示法的内容。现在我们需要讨论这些值的底层模型以及它们的分配方式。

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/a0059080-59e4-4cd9-913b-34e7587e39f7/e2f8246a4fcb3140a547a0fc892decbf48a560bee214c1f877f68db98d0122f2.jpg)

© OSS,31 May 1999 © OSS，1999 年 5 月 31 日

object identifier name space. 对象标识符名称空间。

## 2 The object identifier tree 2. 对象标识符树

The underlying concept for object identifiers is a tree-structure, usually drawn as in figure II-1. Each object identifier value corresponds to precisely one path from the root down to a leaf (or possibly an internal node), with each component of the value notation identifying one of the arcs traversed on this path. 对象标识符的基本结构是一种树形结构，通常如图 II-1 所示。每个对象标识符值对应一条从根节点到叶子节点（或内部节点）的路径。该值表示中的每个组成部分都对应着这条路径上所经过的一个节点。

The tree has a single root (usually drawn at the top as is the usual way with trees in computing!), and a number of arcs to the next level (all arcs go just to the next level), providing nodes at that level. Each node at the next level has arcs down to nodes at the next level below, and so on. Both the depth of the tree and the number of arcs from each node are unlimited. Some branches of the tree will be thickly populated with sub-arcs, others sparsely. Some branches will end early, others will go very deep. 这棵树有一个根节点（通常在图中位于顶部，这是计算机中表示树结构的标准做法！），以及若干通往上一层节点的分支节点。每个上一层节点都有分支连接到更下方的节点。树的深度以及每个节点所连接的分支数量都是无限的。树的一些分支会包含大量子分支，而另一些则相对较少。有些分支会很快终止，而有些则会深入延伸。

Every node is administered by some authority. That authority allocates arcs beneath that node, leading to a subordinate node, and determining: 每个节点都由某个权威机构管理。该机构在该节点下方分配出相应的路径，从而指向一个下属节点，并决定：

• The authority to which delegated responsibility for further allocation (beneath the subordinate node) has been passed, or an information object which is associated with that (leaf) node. (The "information object" concept is discussed further below.) • 负责进一步分配资源的权限已下达到相应的机构，或者与那个叶节点相关联的信息对象。 (关于“信息对象”的概念，将在下文中进一步讨论。)

• A number (unambiguous within all arcs from the current node) to identify the subordinate node from the current node (zero upwards, not necessarily consecutive). • 一个数字（在从当前节点出发的所有路径中都是唯一标识的），用于指定从当前节点开始时的子节点位置（从 0 开始计数，不必连续）。

Optionally a name to be associated with the arc for use by human beings, and again providing identification within the arcs from the current node. 可选地，可以提供一个名称，用于与弧关联，以便人类能够使用这个名称。同时，该名称还可以在当前节点所属的弧中起到标识作用。

The name in the third bullet is required to conform to the ASN.1 rules for a value-reference-name - that is, it must begin with a lower-case letter, and continue with letters (of any case) and digits and hyphens (but with no two consecutive hyphens). 在第三个项目中，名称需要遵循 ASN.1 规范中的规则，即名称必须以小写字母开头，之后可以包含任意大小写的字母、数字以及连字符，但连续使用连字符是不允许的。

When "ccitt" became "itu-t", the ASN.1 standardisers tacitly accepted synonyms for names on arcs. 当“ccitt”被改为“itu-t”时，ASN.1 标准制定者默认接受了用于表示弧的命名方式中的同义词。

Perhaps because of this, many users of ASN.1 now feel that arc names are relatively unimportant (certainly they don't affect the bits-on-the-line), and that once you have obtained a (numerical) object identifier allocation, you can use value notation for that object identifier with any names you choose when you wish to identify yourself, or to publish allocations beneath your node. Some would even assert the right to vary the names used in higher-level nodes. 或许正因为如此，现在许多使用 ASN.1 的用户都认为，弧符号在命名中并不重要（显然它们不会影响在线上的比特数）。一旦获得了数值化的对象标识符分配，就可以使用该标识符，并随意选择任何名称来标识自己，或者在自己的节点下发布相关的分配信息。有些人甚至声称有权更改高级节点中使用的名称。

As at mid-1999, this area is in a state of flux. Earlier views would have said that names were allocated by the superior of an arc, and were immutable, otherwise there is much scope for human confusion. However, the text in the Specification does not entirely support this view, although I know it was the original intent! 到 1999 年中期为止，这一地区的情况处于不断变化之中。按照以往的观点，名字是由某个区域的管理者分配的，而且是不可改变的。否则的话，就会出现很多人为的混乱情况。不过，《规范》中的文字并不完全支持这一观点，虽然我知道这原本就是原意！

The contrary view (that in published OIDs any name can be used) is supported on two grounds: 相反的观点认为（在已发布的 OIDs 中，可以使用任何名称），这一观点的支持基于两个理由：

• There are issues of copyright or trademark of names, which superior nodes are often unwilling to get involved in, so they make no name allocation to their subordinate arcs, only a number. • 有一些版权或商标问题，这些问题通常上级节点不愿意去处理，因此他们不会为下属的弧线分配名称，而只是赋予它们一个数字。

Lower arcs can sometimes be sensitive about appearing to be subordinate to (or part of) organizations whose names identify arcs between themselves and the root. In many cases such an association is at best a loose one, and some organizations will give out object identifier space to anyone who asks for it. 较低的层级组织有时可能会刻意表现得要服从于那些与根组织有联系的组织。在很多情况下，这种关联最多只能算是一种松散的关系；有些组织甚至会主动将对象标识符提供給任何提出请求的人。

It is likely that the standard will be clarified to assert not only that names are optional in the value notation for an object identifier, but also that all such names are arbitrarily chosen by those that include object identifier values in publications. However, it would be irresponsible to use misleading names on arcs, and it is probably best to either omit the name or to use the generally recognised one from any arcs above that which points to your node. 很可能，这个标准会被进一步明确，不仅指出在对象标识符的值表示法中，名称是可选的，而且所有这样的名称都由在出版物中使用对象标识符值的人随意选定。不过，使用误导性的名称来描述弧线显然是不负责任的做法。因此，最好要么不使用名称，要么使用那些被广泛认可的、指向你的节点的名称。

## 3 Information objects 3 个信息对象

NOTE –The term "information object" was used in OBJECT IDENTIFIER text long before the introduction of the "Informaton Object Class" concepts and (perhaps confusingly) refers to a more general concept than the same words used in connection with Information Object Classes. 注意——“信息对象”这一术语在“信息对象类”概念被提出之前就已经被使用了。实际上，“信息对象”这个术语指的是一个更为通用的概念，而非仅用于描述与信息对象类相关的对象。

The term information object used in this context emphasises the fact that object identifiers are usually used to identify relatively abstract objects, such as ASN.1 modules, the definition of some operation that a computer can perform, attributes of some system that can be manipulated by a management protocol, and so on. In other words, they usually identify some piece of specification (not necessarily written using ASN.1). In fact, an organization can be seen as just another type of information object, and in general a node can both be associated with an information object (of any sort) and also have further subordinate nodes. 在这里，“信息对象”这一术语强调的是，对象标识符通常用于标识一些相对抽象的对象，比如 ASN.1 模块、某种计算机可以执行的操作的定义、可以通过管理协议进行操作的系统属性等等。换句话说，它们通常用来标识某种规范或定义（不一定是用 ASN.1 格式编写的）。实际上，一个组织也可以被视为另一种类型的信息对象；一般来说，一个节点既可以属于某个信息对象，也可以包含其他子节点。

If an organization has been allocated a node, we say they have been "hung" from the tree. It is also possible to "hang" inanimate objects (like ASN.1 modules) from the tree, once you are the proud owner of a node! 如果一个组织被分配了一个节点，我们就说该组织已经从树结构中“挂起”了。当然，一旦你成为了某个节点的拥有者，那么无生命的物体（比如 ASN.1 模块）也可以被“挂”在树结构中哦！

Distributed registration authorities provide space enough for all. Have you got hung on the Object Identifier tree yet? Get a piece of the action! 分布式注册机构为每个人提供了足够的注册空间。你是否已经理解了对象标识符的层级结构了呢？那就一起来参与吧！

It is very easy to learn the top bits of the tree, and then to "cheat". To "steal" an arc from some node, publishing allocations beneath that. Don't do it!. It is not hard to get "legal" object identifier name space. But .... see figure 999 .... there are those that advocate a top-level arc where arcs below that are only unambiguous within a very closed community - anyone can use any number, and caveat emptor! What this is really saying is that there is a suggestion that some Object Identifier values should be context-specific, all such values being identified by a special top-level arc. However, this proposal is merely that - a proposal. Such a top-level arc does not yet (mid 1999) exist, although the RELATIVE OID type discussed in Section IV perofrms a similar role. 学习树的顶部节点是非常简单的，然后就可以进行“作弊”了——从某个节点“窃取”弧段，并在其下方发布分配信息。但不要这么做！获得“合法”的对象标识符命名空间并不难。但是……请看图 999……有些人主张使用一个顶级弧段，而低于该弧段的弧段则只在一个非常封闭的社区内具有明确的含义——任何人都可以使用任意编号，让使用者自己决定吧！这实际上意味着，有些对象标识符的值应该具有上下文特异性，所有这些值都由一个特殊的顶级弧段来标识。不过，这个提议仅仅只是一个提议而已。目前还没有这样的顶级弧段存在（截至 1999 年中期），尽管在第四部分讨论的 RELATIVE OID 类型实现了类似的功能。

To identify an organization or object, we use an object identifier value. At the abstract level, this is simply a path from the root to the organization or object being identified. This path can be specified by giving the number of each arc in turn, together with the names (which may be empty/non-existent) associated with each of these arcs. The encoding rules use only the numbers of the arcs, so non-existent names are not a problem. The value notation has various forms (see below) that allow both the names and numbers to be specified. Figure II-1 shows one small part of the tree, with two branches taken to a depth of 4 and 5 arcs. 为了识别一个组织或对象，我们需要使用一个对象标识符值。在抽象层面上，这仅仅是一个从根节点到该组织或对象的路径。这个路径可以通过依次指定每条路径中的节点编号来构建，同时还可以为这些节点指定名称（这些名称可能是空的或不存在的）。编码规则仅使用节点编号，因此不存在的名称并不构成问题。值表示法有多种形式（详见下文），可以同时使用名称和编号来指定路径。图 II-1 展示了一棵树的一部分，其中有两个分支，分别深入到 4 层和 5 层的节点。

## 4 Value notation 4 数值表示法

Note that in all the examples that follow, it would be legal to replace any number by a valuereference name of type INTEGER. If this value reference name had been assigned the value given in the examples below, then the resulting object identifier value is unchanged. It is, however, not common practice to do this. 请注意，在以下所有示例中，用类型为 INTEGER 的值引用名称来替代任何数字都是合法的。如果这种值引用名称被赋予了下文中给出的数值，那么生成的对象标识符值仍然不会发生变化。不过，这种做法并不常见。

The value notation consists of a series of components, one for each arc leading to an identified object. In figure II-1 we can identify the objects at the bottom of the figure by: 数值表示由一系列组件构成，每个组件对应一个通往特定对象的路径。在图 II-1 中，我们可以通过以下方式识别图中底部的对象：

```txt
{iso standard 8571 abstract-syntax (2)}
and
{iso identified-organization dod (6) internet (1)}
and
{joint-iso-itu-t internationalRA (23) set (42) set-vendors (9) oss (12)} 
```

or equivalently, but less readably, by: 或者，等价地表达，但更不容易被阅读的是：

```txt
{1 0 8571 2}
{1 3 6 1}
{2 23 42 9 12} 
```

The first value names an information object in the ISO Standard 8571, the second gives object identifier space to the IETF, and sub-arcs of this are heavily populated in the Internet specification for SNMP (Simple Network Management Protocol). The third value gives object identifier name space to Open Systems Solutions, a vendor associated with the Secure Electronic Transactions (SET) consortium. 第一个值是在 ISO 标准 8571 中用于标识信息对象的名称；第二个值则由 IETF 提供，用于标识对象标识符。而该标准的子领域在 SNMP（简单网络管理协议）的互联网规范中得到了广泛应用。第三个值则由 Open Systems Solutions 公司提供，该公司隶属于 Secure Electronic Transactions (SET)联盟。

It is always permissible to use only numbers (but not common). In one case "8571" an arc has a number but no name, so the number appears alone, not in brackets. In most other cases, the name is given followed by the number in brackets. (The number is required to be in brackets if both are given). It is only for the top arcs (iso, standard, joint-iso-itu-t) that the numbers can be omitted, as these are "well-known" arcs, with their numerical values listed in the ASN.1 specification pre-1988 (they are now listed in X.660/ISO 9834-1). Whilst seeing specifications with these top-level numbers omitted is quite common, it is becoming increasingly the practice, particularly as ASN.1 is now being used by organizations only loosely associated with ITU-T or ISO (or not associated at all), to list the numbers in parenthesis for all arcs. 通常可以使用仅包含数字的编号（但不得使用常见的名称）。在某些情况下，如“8571”这种弧线，只有编号而没有名称，因此编号会单独出现，不会用括号括起来。在大多数情况下，名称会先给出，然后括号中附上编号。（如果同时提供了名称和编号，那么编号必须放在括号中。）只有对于最高级别的弧线（如 iso、standard、joint-iso-itu-t），才能省略编号，因为这些弧线是“众所周知的”弧线，其数值已在 1988 年之前的 ASN.1 规范中列出（现在则见于 X.660/ISO 9834-1 标准）。虽然过去常常看到某些规范中省略这些最高级别弧线的编号，但现在这种情况越来越常见了，尤其是当 ASN.1 被那些与 ITU-T 或 ISO 关联不大的组织使用时，他们通常会将所有弧线的编号都用括号括起来来表示。

Notice that this value notation does not contain commas between components. This is unusual for ASN.1 value notation, and was done to promote easy human readability, particularly of the early components with the numbers omitted. 请注意，这种值表示法中的各个组成部分之间不使用逗号分隔。这对于 ASN.1 值表示法来说比较少见，这样做是为了便于人类阅读，尤其是对于那些省略了数字的早期组成部分而言。

There is one other facility available when specifying object identifier values. We have already met it in figure 21, where we chose to define an object identifier value "wineco-OID" with five components, and then use that name immediately after the curly bracket in our IMPORTS statement. (It is only allowed immediately after the curly bracket). This is something that is quite commonly done, but note that it is not allowed for the module identifier, as the scope of reference names in the module has not yet been entered. Some specifications will define a large number of object identifier values, particularly in association with the definition of information objects, and a very common style is to assign these values in a single module to a series of value-referencenames, exporting those names. They will then be imported and used as necessary in other modules. 在指定对象标识符值时，还有另一种可用的方式。我们在图 21 中已经处理过这种情况，当时我们选择了一个包含五个组件的对象标识符“wineco-OID”，然后立即在 IMPORTS 语句中的大括号之后使用这个名称。（这种用法是严格允许的，但需要注意，这种用法不适用于模块标识符，因为此时模块的引用名称范围尚未确定。有些规范要求定义大量的对象标识符值，尤其是在与信息对象相关的定义中。一种常见的做法是在单个模块中将这些值分配给一系列值引用名称，然后将这些名称导入到其他模块中，并在需要的时候进行使用。）

## 5 Uses of the object identifier type 对象标识符类型的 5 种使用场景

It is a common occurrence for a protocol to be written where there is a need to carry identification of "things". These "things" may be: 在编写协议时，通常需要包含对“对象”的标识信息。这些“对象”可以是：

• what it is: • 它到底是什么：

− operating on; – 在……上进行操作；

− ordering; − 订购；

− reporting on; − 进行报告；

• information that it is carrying; • 它正在传输的信息内容；

• identification of specific actions to be undertaken on receipt of a message; • 在收到消息后，需要执行的具体操作；

• components of some more complex structure, such as Directory (X.500) names; • 一些更复杂结构的组成部分，例如目录名称（X.500 协议中的命名方式）；

• etc, etc. • 等等，等等。

Some existing uses are listed in the "Summary" at the start of this chapter. 本章开头的“概述”部分列出了一些现有的应用案例。

We use the term "information objects" for "things", because at the end of the day a physical "thing" is identified by some piece of text or specification - a piece of information, and sometimes the "thing" is not a physical object but is a rather abstract "thing" such a an organization, but the "thing" is still identified by some specification - a piece of information. What is really being identified by an object identifier value is that more elaborate and precise specification of the thing - an "information object", rather than the "thing" itself, but the two are in 1-1 correspondence, so there is really no distinction. 我们使用“信息对象”这个术语来指代“事物”，因为归根结底，一个物理上的“事物”是通过某些文本或规范来识别的——也就是一些信息。有时候，这个“事物”并非实际存在的物体，而是指一个较为抽象的概念，比如一个组织。不过，这个“事物”仍然是通过某种规范来识别的——也就是一些信息。实际上，被对象标识符所标识的，是那个事物的更详细、更精确的描述——即一个“信息对象”，而不是那个“事物”本身。不过，这两者之间是一一对应的关系，所以实际上并没有什么区别。

Where there is a need for the identification of an information object: 在需要识别某个信息对象的情况下：

• which must be world-wide unambiguous; and • 这一要求必须是全球范围内明确无误的；并且

where allocations of identification to such information objects needs to be widely available to almost anybody; then 当需要将身份分配信息分配给这些信息对象时，希望几乎任何人都能轻松获取这些信息；那么……

use of ASN.1 object identifier values is a good way to go. 使用 ASN.1 对象标识符值是一种很好的方法。

In general, almost all users of ASN.1 have found the need for a naming scheme to identify information objects relevant to their application, and have chosen to use object identifier values for this purpose, and to include in their protocol fields that are OBJECT IDENTIFIER types to carry such values. The OBJECT IDENTIFIER type, and its associated naming structure is important and heavily used. 一般来说，几乎所有使用 ASN.1 的用户都意识到需要一种命名机制来标识与他们的应用相关的信息对象。因此，他们选择使用对象标识符值来进行标识，并将这些值存储在协议字段中的 OBJECT IDENTIFIER 类型中。OBJECT IDENTIFIER 类型及其相关的命名结构非常重要，并且被广泛地使用。

# Chapter 2 The character string types 第二章 字符串类型

## (Or: Overcoming Genesis Chapter 11!) （或者：克服创世记第 11 章的困难！）

Summary: This chapter discusses the complete set of character string types: 摘要：本章讨论了所有字符串类型的完整集合：

• NumericString • 数字字符串

• PrintableString • 可打印的字符串

• VisibleString (ISO646String)

• IA5String

• TeletexString (T61String)

• VideotexString • 视文本字符串

• GraphicString

• GeneralString

• UniversalString

• BMPString

• UTF8String • UTF8 字符串

It describes their value notations, and gives recommendations on their use. 它描述了这些数值的表示方式，并给出了关于如何使用的建议。

Discussion of the character string "hole" type - CHARACTER STRING - is deferred until Chapter 7 of this section. 关于字符串“hole”类型的讨论——即字符字符串的相关内容——将推迟到本部分的第七章再进行讨论。

## 1 Introduction 1 引言

Here we will describe all the available (up to 1988) character string types apart from "CHARACTER STRING", which is described later under "Hole Types". For a full understanding of these types, the reader must be aware of the various approaches that have been taken to character encoding schemes for computers generally over the years. A full discussion of this, and of the historical development of support for character string types in ASN.1, is 在这里，我们将介绍所有可用的字符串类型（截至 1988 年），除了“CHARACTER STRING”类型，后者将在后面的“漏洞类型”中进行讨论。要全面理解这些类型，读者需要了解多年来人们在计算机字符编码方面所采取的各种方法。关于这一点，以及 ASN.1 中字符串类型支持的历史发展，我们将在后续的内容中进行详细讨论。

And God was displeased with the people of Babel for building their tower unto heaven, and sent a thunderbolt and scattered the peoples to the corners of the world giving them different languages. 而上帝对巴比伦人的行为感到不满，因为他们建造了高达天空的塔楼。于是，上帝降下雷霆，将那些人驱散到世界各个角落，让他们拥有了不同的语言。

given in Section IV. Sufficient information is given here for the writing and understanding of ASN.1 specifications. If you want to skip some of this material, just go down to the section "Recommended character string types" (clause 13), and look at the paragraphs about the ones mentioned there. That is probably all you need! 在第四部分中已经提供了足够的信息，足以用于编写和理解 ASN.1 规范。如果您想跳过某些内容，只需前往“推荐的字符串类型”部分（第 13 条），然后查看那里提到的相关段落即可。这些内容应该就足够了！

Character string types are considered by some to be unnecessary (won't a good old OCTET STRING do the job?). (See figure 999!). Yes, an OCTET STRING could be used. But you would then need to spell out clearly the precise encoding to be used, and to make clear to implementors the range of characters that were to be supported. Moreover, that specification would be in normal human-readable text or in ASN.1 comment, could not be understood by any tool assisting an implementation, and (as it is new text) would be a potential source of ambiguity and interworking problems. 有些人认为字符串类型其实是不必要的（使用传统的 OCTET STRING 语法不就足够了？）。（参见图 999！）当然，也可以使用 OCTET STRING 语法。但此时就需要明确说明具体的编码方式，并且要让实现者清楚所支持字符集的范围。此外，这种规范通常是以人类可读的文本形式或 ASN.1 注释的形式出现的，因此不会被任何用于实现的工具理解。而且，由于这是一种新的规范，可能会带来一些歧义和问题。

The types provided in ASN.1 cover the spectrum from the simplest requirements to the most ambitious. In general, if your character set requirements for a particular string are restricted, use the more restricted character set types to make this clear, even if the encoding is the same as for a type with a wider character repertoire. 在 ASN.1 中提供的类型涵盖了从最基础的需求到最复杂的需求的各种情况。一般来说，如果某个字符串所需的字符集限制较多，那么应该使用更受限的字符集类型来表示这一点。即便编码方式与适用于更宽字符集的类型相同，也应使用更受限的类型。

Note also that some of the latest character string types can only easily be supported by a programming language (such as Java) that uses 16 bits per character, supporting the Unicode encoding scheme. (This scheme is fully described in Section IV). Increasingly, however, (late 1990s) programming languages and operating systems and browsers and word processors and .... are all providing Unicode support, either for the 16-bits-per-character repertoire, or in some cases for a 32-bits-per-character repertoire. 另外，一些最新的字符字符串类型只能由那些采用 16 位字符编码方式的编程语言来支持（例如 Java），这些编程语言支持 Unicode 编码方案。这一方案在第四部分中有详细的描述。不过，从 20 世纪 90 年代末开始，越来越多的编程语言、操作系统、浏览器、文字处理软件等也开始提供 Unicode 支持，无论是针对 16 位字符编码，还是在某些情况下针对 32 位字符编码。

This does not mean that if the application designer has specified a field as (for example) UTF8String or UniversalString, you cannot implement that protocol in a language (or operating system) that does not have Unicode support, it just means that it may be harder work! 这并不意味着，如果应用程序设计者将某个字段指定为 UTF8String 或 UniversalString 等类型，那么你就无法在不支持 Unicode 的语言或操作系统上实现该协议。不过，这样做可能会更麻烦一些而已！

## 2 NumericString 2 数字字符串

Values of the type are strings of characters containing the digits zero to 9 and space. The BER encoding is ASCII (8 bits per character), and the PER encoding is 4 bits per character unless the character repertoire has been further restricted by a "permitted alphabet constraint" (see Chapter 3 following), when it could be less. 这类值的类型是由字符组成的字符串，其中包含 0 到 9 的数字以及空格。BER 编码采用 ASCII 格式，即每个字符占用 8 位比特；而 PER 编码则每个字符仅占用 4 位比特。不过，如果由于“允许的字母表限制”而进一步限制了字符集的范围（详见第 3 章），那么 PER 编码所需的位数可能会更少。

## 3 PrintableString 3 可打印的字符串

Values of the type are strings of characters containing an ad hoc list of characters defined in a table in the ASN.1 specification, and copied here as Figure II-2. 这类值的本质是一类字符字符串，这些字符来自 ASN1 规范中定义的特定字符列表，如图 II-2 所示，这些字符被复制到这里。

This is basically the old telex character set, plus the lower case letters. You would probably tend not to use it today unless you had an application likely to be associated with devices with limited character input or display capabilities. 这基本上就是旧的电报字符集，再加上了小写字母。如今，除非有需要处理那些字符输入或显示能力有限的设备的应用程序，否则人们通常不会使用这个字符集了。

<table><tbody><tr><td data-imt-p="1">Name 名称</td><td data-imt-p="1">Graphic 图形/图像</td></tr><tr><td data-imt-p="1">Capital letters 大写字母</td><td data-imt-p="1">A, B, ... Z A、B、… Z</td></tr><tr><td data-imt-p="1">Small letters 小写字母</td><td data-imt-p="1">a, b, ... z a, b, … z</td></tr><tr><td data-imt-p="1">Digits 数字</td><td>0, 1, ... 9</td></tr><tr><td data-imt-p="1">Space 空间</td><td data-imt-p="1">(space) （空格）</td></tr><tr><td data-imt-p="1">Apostrophe 省略号</td><td>'</td></tr><tr><td data-imt-p="1">Left Parenthesis 左括号</td><td>(</td></tr><tr><td data-imt-p="1">Right Parenthesis 正确的括号使用</td><td>)</td></tr><tr><td data-imt-p="1">Plus sign 加号</td><td>+</td></tr><tr><td data-imt-p="1">Comma 逗号</td><td>,</td></tr><tr><td data-imt-p="1">Hyphen 连字符</td><td>-</td></tr><tr><td data-imt-p="1">Full stop 句号</td><td>.</td></tr><tr><td data-imt-p="1" data-imt_insert_failed_reason="same_text">Solidus</td><td>/</td></tr><tr><td data-imt-p="1">Colon 结肠</td><td>:</td></tr><tr><td data-imt-p="1">Equal sign 等号</td><td>=</td></tr><tr><td data-imt-p="1">Question mark 问号</td><td>?</td></tr></tbody></table>

## 4 VisibleString (ISO646String) 4 可见字符串（ISO646 字符串）

The name "ISO646String" is a deprecated synonym for VisibleString (deprecated because the name contains a Standard number which is not in fact used in its definition, post 1986!), but you may encounter it. The character repertoire is described in the very old ISO Standard ISO 646, which laid the foundation for the better-known ASCII. Whilst this character repertoire was originally strictly not ASCII, but rather "the International Reference Version of ISO 646", it was widely interpreted by all ASN.1 users and implementors as simple plain ASCII, but printing characters plus space only. The original definition was by reference to the ISO 646 Standard, but post-1986 the definition was formally "Register Entry 2 (plus space) of the International Register of Coded Character Sets to be used with Escape Sequences". (See Section IV for more detail). This was changed in 1994 to reference "Register Entry 6", which is strict ASCII, recognising the normal interpretation by ASN.1 users. The coding in BER is 8 bits per character, and it is the same in PER if there is no subtyping applied to the type to restrict the range of characters (if there is, it could be less). “ISO646String”这个名称是“VisibleString”的过时替代名称（之所以使用这个名称，是因为标准中使用了“Standard”这个词汇，但实际上在 1986 年之后就再也没有被使用了！）。不过，你仍有可能遇到这个名称。关于字符集的详细描述可以在非常古老的 ISO 标准 ISO 646 中找到，该标准为后来更为人熟知的 ASCII 标准奠定了基础。虽然最初这些字符并不属于 ASCII 范畴，而是属于“ISO 646 的国际参考版本”，但所有 ASN.1 的用户和实现者都将其简单地视为普通的 ASCII 字符集，即只包含字符和空格。最初的定义是基于 ISO 646 标准，但在 1986 年之后，定义被正式改为“国际编码字符集注册表中的第 6 个注册项（加上空格）”，用于与转义序列一起使用。（更多细节请参见第四部分）。这一定义在 1994 年进行了修改，改为以“第 6 个注册项”作为标准 ASCII 字符集，从而明确了其定义。由 ASN 的用户进行正常的解释。在 BER 中，每个字符的编码长度为 8 位；在 PER 中也是如此。如果不对类型进行子类型划分来限制字符范围，那么每个字符的编码长度就是 8 位（如果进行了子类型划分，则编码长度可能会减少）。

## 5 IA5String

"International Alphabet 5" is specified in a very old ITU-T Recommendation, which again was the original reference for this type. Again, this was close to ASCII (ASCII was a "national variant" of International Alphabet 5, but the type is widely assumed to mean simply "the whole of ASCII, including control characters, space, and del". The precise reference today is "Register Entries 1 and 6 (plus space and delete) of the International Register of Coded Character Sets to be used with Escape Sequences", which is strict ASCII. The encoding is again 8 bits per character (possibly less in PER). “国际字母表 5”是在一份非常古老的 ITU-T 建议书中规定的。实际上，这一标准最初就是以该文件为基准制定的。该标准与 ASCII 标准较为接近（ASCII 实际上是国际字母表 5 的“国家版本”），不过通常认为“国际字母表 5” simply 指的是“包括控制字符、空格以及删除符在内的完整 ASCII 标准”。目前，这一标准的确切依据是“国际编码字符集注册表中的第 1 条和第 6 条条目，再加上空格和删除符”，这完全符合严格的 ASCII 标准。该编码方式仍然是每个字符 8 位（在 PER 模式下可能会更少）。

## 6 TeletexString (T61String) 6 电信科技字符串（T61 字符串）

Again, the synonym is deprecated. Originally CCITT Recommendation T.61 specified the character repertoire for Teletex, and was referenced by the ASN.1 specification. (Today the corresponding specifications are in the ITU-T T.50 series.) The precise definition of this type has changed over time to reflect the increasing range of languages supported by the ITU-T teletex Recommendations. Today it includes Urdu, Korean, Greek, .... . Formally, it is Register Entries 6, 87, 102, 103, 106, 107, 126, 144, 150, 153, 156, 164, 165, 168, plus SPACE and DELETE! The encoding of each register entry is 8 bits per character, but there are defined escape codes (the ASCII "ESC" encoding followed by some defined octet values) to switch between the different register entries. It is quite hard to implement full support for this character string type, but it is extensively used in the X.400 and X.500 work. The character repertoires referenced have increased with each new version of ASN.1, and may continue to do so, under pressure to maintain alignment with the ITU-T Teletex Recommendations, which themselves are under pressure to support more and more of the world's character sets. This makes this type effectively an openended set of character repertoires, and would make any claims of "conformance" hard to define or sustain. Today, it is best avoided, but it was popular in the mid-1980s, and you will often encounter it. 同样，这个同义词就是“deprecated”。最初，CCITT 建议书 T.61 规定了 Teletex 使用的字符集，这一规定在 ASN.1 规范中也有提及。（如今，相应的规范属于 ITU-T T.50 系列。）随着时间的推移，这种类型的定义已经发生了变化，以反映 ITU-T Teletex 建议所支持的语言种类越来越多。如今，它包括了 Urdu、韩语、希腊语等语言。从正式定义来看，这些字符属于寄存器 6、87、102、103、106、107、126、144、150、153、156、164、165、168 这些寄存器，此外还有 SPACE 和 DELETE 字符。每个寄存器的编码都是 8 位一个字符，但还定义了一些转义码（如 ASCII 中的“ESC”编码，后面跟着一些特定的八位数值），用于在不同寄存器之间切换。要完全支持这种字符类型相当困难，不过它在 X.400 和 X.500 协议中得到了广泛的应用。随着每个新版本的 ASN 出现，所涉及的字符集范围都在不断扩大。由于需要保持与 ITU-T Teletex 推荐标准的兼容性，这些字符集继续会有所扩展。而 ITU-T Teletex 推荐标准本身也面临着支持更多全球字符集的压力。因此，这类字符集实际上是一个开放式的字符集，任何关于“符合标准”的声明都难以界定或维持。目前，最好避免使用这种字符集，但在 1980 年代中期，它却很流行，因此你经常会遇到它。

## 7 VideotexString 7 视频电话字符串

A little-used character string type that gives access to the "characters" used to build crude pictures on videotext systems. Typically a "character" is a 3x2 array, with each cell containing either a foreground colour or a background colour (determined by transmission of one of about five control characters), giving 64 different printing "characters" that can be used to build the picture. 这是一种使用频率较低的字符字符串类型，它提供了对用于构建 Videotext 系统中图像元素的“字符”的访问权限。通常，一个“字符”是一个 3x2 的数组，每个单元格中要么包含前景颜色，要么包含背景颜色（背景颜色由其中一个约五种控制字符的传输状态决定）。这样，就可以使用 64 种不同的“字符”来构建图像。

Formally, it is again a list of 17 register entries, partially overlapping those specified for TeletexString. 从形式上看，这仍然是一组包含 17 个寄存器条目的列表，其中部分条目与为 TeletexString 指定的条目有重叠。

## 8 GraphicString 8 图形字符串

This was a popular string type in the main OSI (Open Systems Interconnection) standards produced during the 1980s, and allowed any of the Register Entries in the International Register for printing characters (but not the control character entries). In its hey-day the International Register had a new entry added about every month or so, and eventually covered most of the languages of the world. If this text is used in an academic course, an interesting student exercise would be to discuss the implementation implications of using such a wide (and ever-expanding!) type definition. Since the development of ISO 10646/Unicode, additions to the International Register have become much less common, and coding schemes based on this Register can be regarded as obsolescent. 在 20 世纪 80 年代制定的 OSI 标准体系中，这种字符串类型非常流行。它允许使用国际字符注册表中的任何注册项（但不包括控制字符项）。在鼎盛时期，国际字符注册表大约每月会新增一项注册项，最终涵盖了世界上大多数语言。如果在学术课程中使用这种文本，一个有趣的课堂练习就是讨论使用如此广泛且不断扩展的定义所带来的实现问题。自从 ISO 10646/Unicode 问世以来，国际字符注册表的更新频率已经大大降低，基于该注册表的编码方案也被视为过时的技术了。

## 9 GeneralString 9 通用字符串

This is similar to GraphicString, except that the register entries for control characters (of which there are many) can also be used. 这与 GraphicString 类似，不过它还可以使用控制字符的寄存器条目（这些控制字符有很多）。

## 10 UniversalString 10 通用字符串

This is a string type that was introduced into ASN.1 in 1994, following the completion of the ISO Standard 10646 and the publication of the Unicode specification (see Section IV for more information on ISO 10646 and Unicode). The ISO 10646 standard (and the ASN.1 encoding in BER) envisages a 32-bits 这是一种在 1994 年引入 ASN.1 中的字符串类型。这一标准的制定是在 ISO 标准 10646 发布之后，同时也在 Unicode 规范发布之后进行的（有关 ISO 10646 和 Unicode 的更多信息，请参见第四部分）。ISO 10646 标准（以及 ASN.1 编码格式）规定使用 32 位来表示字符串。

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/a0059080-59e4-4cd9-913b-34e7587e39f7/0d12bb2cfa55905678efc224e2f4e6e43fb29fe192667be25f398dd9a9e5d60e.jpg)

per character encoding scheme, sufficient to cover all the languages of the world without using "combining characters", with a fair bit left over for the languages of Mars and most of the rest of the undiscovered Universe! It is only this type and UTF8String (see below) that can cover all the characters for which computer encodings have been defined (not quite true - there are some weird glyphs in the International Register that have not yet been put into ISO 10646). This type has not, however, proved popular among ASN.1 users. 按照这种字符编码方案，足以涵盖世界上所有语言的需求，而无需使用“组合字符”的方式。此外，还留有足够的空间来容纳火星上以及宇宙中尚未被发现的许多语言的字符！只有这种编码方式以及 UTF8String（见下文）能够涵盖所有已定义的计算机编码字符（不过并非完全如此——国际注册表中有一些奇怪的字符尚未被纳入 ISO 10646 标准）。不过，这种编码方式在 ASN.1 用户中并不受欢迎。

## 11 BMPString 11 BMP 字符串

The name comes from the "Basic Multilingual Plane" (BMP) of ISO 10646, which contains all characters with any commercial importance (all living languages), and can be encoded (and is in BER) with a fixed 16-bits per character. Whilst the formal ASN.1 definition references ISO 10646, the character set is the same as that defined in and more commonly known as the Unicode Standard produced by the Unicode Consortium. (Search the Web if you want to know more about 这个名称来源于 ISO 10646 标准中的“基本多语言平面”（Basic Multilingual Plane, BMP）。该标准包含了所有具有商业意义的字符，也就是所有活着的语言所使用的字符。这些字符可以通过固定的 16 位编码来表示，这种编码方式已经被广泛采用。虽然正式的 ASN.1 定义引用了 ISO 10646 标准，但实际上所使用的字符集与 Unicode 联盟制定的 Unicode 标准中的字符集是相同的。如果你想了解更多关于 Unicode 标准的信息，可以搜索一下吧。

Unicode, oar see Section IV). The fixed-size representation of 16-bits per character, holding Unicode characters, is becoming common in revisions of programming languages and operating systems, and is rapidly replacing ASCII as the default encoding for manipulating character data. This ASN.1 type was widely used during the mid-1990s by those application specifications upgrading to the 1994 ASN.1 specification. (It was not present in ASN.1 pre-1994). Unicode，请参见第四部分）。每个字符使用 16 位固定长度的编码方式来表示 Unicode 字符，这种编码方式在编程语言和操作系统的更新中越来越常见，并且正迅速取代 ASCII 成为处理字符数据时的默认编码方式。这种 ASN.1 类型在 20 世纪 90 年代中期被广泛使用，当时许多应用程序的规范都采用了这种编码方式，以符合 1994 年发布的 ASN.1 规范。在 1994 年之前的 ASN.1 规范中并未出现这种编码方式。

## 12 UTF8String

UTF8String is the recommended character string type for full internationalization without unnecessary verbosity. UTF8String 是被推荐用于完全国际化的字符字符串类型，它避免了不必要的复杂性。

This encoding scheme was developed in the mid-1990s and the type was added to ASN.1 in 1998. The acronym stands for "Universal Transformation Format, 8 bit", but that does not matter much. Formally, the character repertoire is exactly the same as UniversalString - all defined characters can be represented. 这种编码方案是在 1990 年代中期开发的，而该类型在 1998 年被添加到 ASN.1 标准中。其缩写意为“通用转换格式，8 位长度”，不过这个缩写其实并不重要。从形式上讲，这种编码方式与 UniversalString 完全相同——所有定义的字符类型都可以被用来表示。

UTF8 is, however, a variable length encoding for each character, with the rather interesting property that (7-bit) ASCII characters encode as ASCII - in a single octet with the top bit set to zero, and none of the octets in the representation of a non-ASCII character have the top bit set to zero. ASCII is paramount! Most European language characters (like c-cedilla or u-umlaut) will encode in two octets, and the whole of the Basic Multi-lingual Plane, together with all characters identified so far, encode in at most three octets per character. If we ever do populate the whole of the ISO 10646 32-bit space, then UTF8 would use a maximum of six octets per character. 不过，UTF8 是一种可变长度的字符编码方式。其独特之处在于：7 位的 ASCII 字符仍然以 ASCII 格式进行编码——即占用一个八位元，其中最高位为 0。而非 ASCII 字符在编码时，其最高位不会为 0。ASCII 编码非常重要！大多数欧洲语言中的字符（如 c-cedilla 或 u-umlaut）需要两个八位元来编码。而整个基本多语言平面中的字符，最多只需要三个八位元就能表示。如果我们真的要填满整个 ISO 10646 32 位空间，那么 UTF8 每个字符最多就需要六个八位元来编码。

Whilst use of a fixed 16-bits per character is becoming the norm for operating system interfaces and programming languages, use of UTF8 for storage and transmission of character data is the way everybody is going (as at mid-1999). As an implementor of an ASN.1-based application, you can expect that if you use an ASN.1 tool with a language that supports Unicode, the UTF8 transformations will be applied by the tool, invisibly to you, as part of the ASN.1 encode/decode process, giving you a simple 16-bits (or 32-bits) per character to work with in memory, but with an efficient transfer syntax. 虽然以固定 16 位来表示每个字符已成为操作系统接口和编程语言的标准做法，但在字符数据的存储和传输方面，使用 UTF8 格式才是未来的发展方向（至少在 1999 年中期是这样）。作为基于 ASN.1 的应用程序实现者，您可以放心，如果您使用支持 Unicode 的 ASN.1 工具，那么 UTF8 格式的转换将会在工具进行 ASN.1 编码/解码过程中自动完成，而您无需察觉。这样，您在内存中就可以使用简单的 16 位（或 32 位）字符表示方式，同时还能实现高效的传输效率。

## 13 Recommended character string types 推荐使用的 13 种字符串类型

So having read right to the end, you can now make an informed judgment on which character string types to use! Here it is assumed you are writing a new specification and will conform to the post-1994 ASN.1, and hence can use all the facilities in the latest ASN.1. (A fuller discussion of the pre-1994/post-1994 issues appears in Section IV). 因此，只要一直阅读到结尾，你现在就可以对应该使用哪种字符字符串类型做出明智的判断了！这里假设你正在编写新的规范，并且会遵循 1994 年之后的 ASN.1 标准，所以你可以使用最新版本的 ASN.1 中的所有功能。（关于 1994 年之前和之后标准的详细讨论请参见第四部分。）

If, for the expected implementation of your application, the input/output devices involved are likely to be able to handle the full Unicode 如果您的应用程序按计划实施，那么相关的输入/输出设备应该能够处理完整的 Unicode 字符集。

For full internationalization, use UTF8String. Otherwise use the most restrictive character string type available for your needs. If input/output devices restrict your application, consider NumericString or PrintableString or VisibleString or IA5String. 如果需要完全实现国际化功能，建议使用 UTF8String 类型。否则，可以根据实际需求选择最严格的字符字符串类型。如果输入/输出设备对应用程序的使用有限制，可以考虑使用 NumericString、PrintableString、VisibleString 或 IA5String 类型。

character set, and you want to be as general as possible, then UTF8String is for you! The earlier UniversalString and BMPString offer few if any advantages, and should be ignored. If, however, input or output is likely to be done on more limited devices, then you may wish to consider a more restricted character string type. 如果你希望实现尽可能通用的字符集处理，那么 UTF8String 就是理想的选择！之前的 UniversalString 和 BMPString 这两种字符集类型几乎没有优势，因此可以忽略它们。不过，如果输入或输出的操作可能是在较为有限的设备上进行的，那么你可以考虑使用一些功能较为有限的字符集类型。

GeneralString and GraphicString, based on the International Register are obsolete, and there is no case for using them in new specifications, although they were important in the 1980's. 基于国际注册标准的 GeneralString 和 GraphicString 已经过时了，在新规范中不再推荐使用它们。不过，在 1980 年代时，这些标准确实发挥了重要作用。

The same remark applies to TeletexString (T61String) and VideotexString: you are unlikely to want to use these unless you have strong links to the associated ITU-T Recommendations. 同样的道理也适用于 TeletexString (T61String)和 VideotexString：除非您与相关的 ITU-T 建议有紧密的联系，否则您不太可能会使用这些字符串。

If your application does require use of input/output devices that may only be able to support a limited range of characters, then you must seriously consider using only NumericString, PrintableString, VisibleString (ISO646String), or IA5String. NumericString is very limited, and is not fully international, but is better from the internationalization point of view than the other three (arabic numbers are accepted over more of the world than the full range of ASCII characters). PrintableString has the slight merit that it is hard-wired into ASN.1, so there can be no misunderstandings about what characters are included, but it is essentially a cut-down ASCII with few advantages over ASCII. If you want full ASCII, then you need VisibleString (no control characters) or IA5String (includes control characters). This will be fine for English-speaking communities, and is livable-with for a number of other European languages, but is generally deprecated in any sort of international specification. 如果您的应用程序确实需要使用输入/输出设备，而这些设备可能只能支持有限的字符集，那么您应该考虑仅使用 NumericString、PrintableString、VisibleString（ISO646String）或 IA5String。NumericString 的局限性很大，且并非完全符合国际化标准；但从国际化的角度来看，它比其他三种方式要好一些（因为除了全部 ASCII 字符外，它还支持阿拉伯数字）。PrintableString 的优点在于它已硬编码到 ASN.1 中，因此不会出现关于所包含字符的误解；但实际上它不过是经过精简的 ASCII 版本，与其他 ASCII 格式相比并没有什么优势。如果您需要完整的 ASCII 字符集，那么您需要使用 VisibleString（因为它不包含控制字符），或者 IA5String（因为它包含了控制字符）。这种方式适用于英语为母语的社区，对于其他一些欧洲语言来说也是可行的，但在任何国际规格标准中通常都被不推荐使用。

Ultimately, the choice has to be yours as the application designer - ASN.1 merely provides the notational tools, but you probably want to restrict your choice to NumericString, PrintableString, VisibleString, IA5String, and UTF8String. You should use UTF8String if input\\output devices are not likely to play a strong determining role in implementations of your application (for example, if all associated input\\output will be using general-purpose computer software for keyboard input and display). 最终，这个选择还是由应用程序设计者您来决定。 ASN.1 只是提供了相关的符号表示方式，但您或许希望将选择范围限制在 NumericString、PrintableString、VisibleString、IA5String 和 UTF8String 这几种类型上。如果输入输出设备不太可能在应用程序的实现中起到重要作用（例如，如果所有相关的输入输出都通过通用计算机软件进行键盘输入和显示），那么建议使用 UTF8String 类型。

## 14 Value notation for character string types 14. 字符串类型的数值表示方式

This book gives full coverage of the ASN.1 notation, but there are a number of parts of that notation that you will rarely need or encounter. Value notation for character strings is in that category, and value notation for control characters or characters appearing in several languages is even less commonly needed. Skip-read this section and return to it later if you find you need it! 这本书全面介绍了 ASN.1 表示法。不过，该表示法中有一些部分很少被使用或遇到。字符字符串的值表示法就属于这类情况；而用于控制字符或来自多种语言的字符的值表示法则更是不常被需要的。如果你之后觉得需要这部分内容，可以跳过它，之后再回来学习吧！

Names exist for all UNICODE characters, and can be used in ASN.1 to give precision to the specification of character string values without concern about ambiguity of glyphs or the character set available on your publication medium. Cell references can also be used. 对于所有 UNICODE 字符，都有相应的名称可用。在 ASN1 中可以使用这些名称来精确指定字符串值，而无需担心字形表示上的歧义或出版物介质上可用的字符集问题。此外，还可以使用单元格引用来进行引用。

The only value notation for character string types pre-1994 was to list the characters in quotation marks. This was fine for simple repertoires like PrintableString, but did not enable control characters to be specified for a type such as IA5String, and gives ambiguity problems in printed specifications with strings such as 在 1994 年之前，用于字符字符串类型的唯一值表示方法是用引号来列出字符。这种方法适用于像 PrintableString 这样的简单类型，但无法为像 IA5String 这样的类型指定控制字符。此外，这种表示方式在打印规格说明中也会造成歧义问题。

## "HOPE" “希望”

if the repertoire includes Cyrillic and Greek as well as ASCII! (Each of these four glyphs appears as a character in more than one of these alphabets). There are also potential problems in printed specifications in determining what white space in character string values is intended to represent (how many spaces, "thin" spaces, etc). 如果词汇表不仅包括西里尔字母和希腊字母，还包括 ASCII 字符的话，那么情况就会更复杂了！因为这四种字符在多种字母表中都作为独立的字符出现。此外，在打印规格中确定字符串值中的空白字符代表什么含义时，也可能出现一些问题——比如需要几个空格、什么样的“瘦型”空格等。

Post 1994, two additional mechanisms are available for defining a character string precisely, both of them based on listing the characters individually. 自 1994 年之后，又有两种方法来精确定义字符串，这两种方法都是基于逐个列出字符的方式来进行的。

The notation is illustrated by the following: 这种表示方式可以用以下例子来说明：

```txt
my-string1 UTF8String ::= {cyrillicCapitalLetterEn,
    greekCapitalLetterOmicron,
    latinCapitalLetterP,
    cyrillicCapitalLetterIe} 
```

```autohotkey
my-string4 IA5String ::= { {0, 0}, {0, 1}, {0, 3}, "ABC", {7, 15} } 
```

As you will guess, my-string3 is the same as my-string1 (and could be printed as "HOPE"!), and my-string4 is the same as my-string2. The last two notations reference the cells (giving group, plane, row, cell) of ISO 10646 or of ASCII (formally, of Register Entry 6 of the International Register) (giving table column as 0 to 7 and table row as 0 to 15). 如你所料，my-string3 与 my-string1 相同（可以打印为“HOPE”！），而 my-string4 则与 my-string2 相同。后两个表示方式分别指向了 ISO 10646 标准中的单元格（包括组、平面、行、单元格信息），或者 ASCII 标准中的单元格信息（具体位置为国际注册表中的第 6 个寄存器）。其中，表格的列编号为 0 到 7，行的编号为 0 到 15。

The last two notations can be used freely, but the character names used in the first two notations are only available if they have been imported into your module from a module which is defined (algorithmically) in the ASN.1 specification by reference to character names assigned in ISO 10646 (and Unicode). 最后两种表示方式可以随意使用，但前两种表示方式中使用的字符名称只有在从符合 ASN.1 规范的模块中导入时才能使用，而该模块必须通过引用 ISO 10646 标准（以及 Unicode）中定义的字符名称来定义。

To make the above value notations valid, you need the following IMPORTS statement in your module: 为了使上述数值表示法有效，你需要在你的模块中添加以下导入语句：

```txt
IMPORTS cyrillicCapitalLetterEn, greekCapitalLetterOmicron,
latinCapitalLetterP, cyrillicCapitalLetterIe,
nul, soh, etx, del FROM
ASN1-CHARACTER-MODULE
{joint-iso-itu-t asn1(1) specification(0) modules(0) iso10646(0)}; 
```

You will also note that you can mix the different notations - character names, quoted strings, cell references - within a single value definition. 您还会注意到，可以在一个值定义中混合使用不同的表示方式——比如字符名称、带引号的字符串，以及单元格引用等。

The above works, but if your "HOPE" was actually intended to be the ASCII characters, there is a less verbose method available post-1998. You can simply write: 上述方法可以起作用，但如果你希望“HOPE”实际上代表的是 ASCII 字符，那么自 1998 年之后有一种更简洁的方法可用。你可以简单地这样写：

```txt
my-string5 UTF8String(BasicLatin)::= "HOPE" 
```

where "BasicLatin" is imported from the ASN.1 module. You can then, in a SEQUENCE say, have an element: 在“BasicLatin”从 ASN.1 模块导入之后，你可以像在序列中那样定义一个元素：

```txt
string-element UTF8String DEFAULT my-string5 
```

What we are doing here is fairly obvious - we are "qualifying" the UTF8String type to say that we are only using the BasicLatin (ASCII) part, so the "HOPE" is now unambiguously the ASCII characters. Note that in the SEQUENCE, we use the full UTF8String type. This rather simple notation rests on two powerful and general concepts, those of subtyping and of value mappings. Subtyping is the definition of a new type which contains only a subset of the values of the socalled parent type. In this case the parent type is "UTF8String", and we are using a subtype of that (defined in the ASN.1 module) called "BasicLatin" to subtype it here. The above example could actually have been written: 我们在这里所做的操作相当直观——我们正在对 UTF8String 类型进行“限定”，即只使用 BasicLatin（ASCII）部分的数据。这样一来，“HOPE”就明确地指代了 ASCII 字符。需要注意的是，在 SEQUENCE 中，我们使用了完整的 UTF8String 类型。这种简单的表示方式基于两个强大的概念：子类型定义和价值映射。子类型定义是指创建一种新类型，该类型仅包含父类型部分值的子集。在这个例子中，父类型是“UTF8String”，而我们使用的子类型则是定义在 ASN.1 模块中的“BasicLatin”。实际上，上述示例也可以这样表述：

## my-string5 BasicLatin ::= "HOPE" my-string5 基本拉丁文 ::= "HOPE"

which perhaps makes it clearer that "my-string5" is latin characters, but makes it less clear that it can be used as a DEFAULT value for UTF8String (although it still can). Subtyping is discussed in more detail in the next chapter. Whichever way "my-string5" is defined, its use as a default value for UTF8String is dependent on a general concept in ASN.1 that if something is a valuereference-name of a subtype of some type, it can also be used as a value-reference-name for a value of the parent type, and in some cases of other "similar" types. This is the value mapping concept in the ASN.1 semantic model (introduced briefly in Section I and discussed more fully in Section IV), and in this case allows "my-string5" to be used not just as a value for UTF8String, but also, should you wish it, as a value for PrintableString and VisibleString. 这可能使得“my-string5”被明确视为拉丁字符，但就不太可能被当作 UTF8String 的默认值了（尽管它仍然可以充当这一角色）。关于类型继承的问题，将在下一章中详细讨论。无论“my-string5”是如何定义的，它作为 UTF8String 的默认值，都基于 ASN.1 中的一个通用概念：如果某个值是某个子类型的价值引用名，那么它也可以作为父类型的值使用，在某些情况下，甚至可以用于其他“类似”的类型。这就是 ASN.1 语义模型中的值映射概念（在第一节中简要介绍，在第四节中进行了更深入的讨论）。在这种情况下， “my-string5”不仅可以作为 UTF8String 的值使用，如果愿意的话，也可以作为 PrintableString 和 VisibleString 的值使用。

## 15 The ASN.1-CHARACTER-MODULE 15 ASN.1-CHARACTER-MODULE

This module has been mentioned above. It provides value-reference-names for all the ASCII control characters (explicitly listed), and for all the characters in Unicode/ISO 10646. The character names listed in the ISO 10646 Standard (and Unicode) are given in all upper case with spaces between words. To convert to an ASN.1 name you keep the upper case letter for the first letter of every word except for the first name, change all other letters to lower-case, then remove the spaces! This produces the names we used above, and also the rather long name: 这个模块已经在上面被提及过了。它为所有 ASCII 控制字符（明确列出的字符）以及 Unicode/ISO 10646 中的字符提供了名称。ISO 10646 标准中列出的字符名称（以及 Unicode 中的字符名称）都是用全大写字母表示的，单词之间用空格分隔。要将其转换为 ASN.1 格式的名称，可以将每个单词的第一个字母保持为大写，其余字母都转换为小写，然后去掉空格。这样就能得到我们上面使用的那些名称，还包括那个相当长的名称。

## cjkUnifiedIdeograph-4e2a cjk 统一字素-4e2a

for the Chinese/Japanese/Korean (CJK) character which looks (to a Western eye!) like a vertical bar with a caret over it, and is named in ISO 10646 as "CJK Unified Ideograph-4e2a".. 对于中文/日语/韩语字符来说，这个字符在西方人的眼中看起来就像一个带有冒号的垂直条状符号。在 ISO 10646 标准中，这个字符被命名为“CJK 统一表意文字-4e2a”。

ISO 10646 also defines 84 collections - useful sets of characters. These names are mapped into ASN.1 names for subtypes of UTF8String by the same algorithm, except that as they are types (sets of string values, not single character values), they keep their initial upper-case letter. Here are a few examples of the names that are available for import: ISO 10646 还定义了 84 种字符集——这些都是有用的字符集合。这些名称通过相同的算法被映射到 UTF8String 子类型的 ASN.1 名称中。不过，由于这些名称属于类型（即字符值集合，而非单个字符值），因此它们保留了初始的大写字母形式。以下是一些可用于导入的名称示例：

```txt
BasicLatin
Latin-1Supplement
LatinExtended-A
IpaExtensions
BasicGreek
SuperscriptsAndSubscripts
MathematicalOperators
BoxDrawing
etc 
```

## 16 Conclusion 16 结论

The ASN.1 character string types have evolved over time as the character set standards themselves have changed, and as input/output devices and packages have become more capable of handling a wider and wider range of characters. ASN.1 字符字符串类型随着时间的推移而不断发展演变。随着字符集标准本身的变化，以及输入/输出设备和软件包能力的提升，它们能够处理的范围也越来越广。

Partly to provide a mechanism that would accommodate any character repertoire and encoding scheme, the CHARACTER STRING hole type was introduced. This is described in a later chapter. 为了容纳各种字符集和编码方式，引入了“字符字符串”这一数据类型。关于这一点，将在后面的章节中进行详细说明。

Mechanisms were also added over time to provide for a more precise tailoring of character repertoires to user's needs, and to provide a precise and unambiguous value notation for character strings which does not depend on (the perhaps restricted set of) glyphs available for any printed ASN.1 specification, or on the character repertoire (such as perhaps only ASCII) available for any machine-readable ASN.1 specification. 随着时间的推移，还增加了一些机制，以便能够根据用户的需求更精确地调整字符集的构成。此外，还为字符字符串提供了一种精确且明确的价值表示方式，这种表示方式不依赖于任何印刷形式的 ASN1 规范中可用的字符集，也不依赖于任何机器可读取的 ASN1 规范中提供的字符集（例如，可能只有 ASCII 字符集）。

The end result is a perhaps confusing, but wide-ranging and up-to-date set of types for character string fields. 最终得到的是一套或许有些复杂，但覆盖范围广且最新的字符字符串字段类型定义。

# Chapter 3 Subtyping 第三章 亚型分类

# (Or: Tighten up your data types!) （或者：请仔细考虑一下你的数据类型吧！）

Summary: This chapter describes the ASN.1 subtype notation that allows the precise definition of the set (subset) of values that you wish to allow for a type. You can, for example, specify: 摘要：本章介绍了 ASN.1 子类型表示法，它使得我们可以精确地定义某个类型所允许的值集（或子集）。例如，我们可以这样进行定义：

• the range of an integer; • 整数的范围；

• minimum and/or maximum length of a string; • 字符串的最小和/或最大长度；

• the precise characters wanted from a character set; • 需要从字符集中选取的特定字符；

• minimum and/or maximum number of iterations in a SEQUENCE OF or SET OF. • 在序列或集合中，最小和/或最大迭代次数。

The full notation has considerable power and flexibility, but the above examples are the ones most commonly met. 这种完整的表示方式具有相当强的表达力与灵活性，但上述例子正是最为常见的应用实例。

## 1 Introduction 1 引言

The ASN.1 "subtype notation" is very powerful, and it would be nice to say that it is one of the things that makes ASN.1 great! However, whilst the simpler instances of its use (length limits on strings, limits on iterations of sequence-of, ranges on integers) are common, and it is important that you use them where you can, some of the other features of this notation are seen less often, and are perhaps less important. ASN.1 中的“类型标记”机制非常强大，可以说它是使 ASN.1 如此出色的关键因素之一。不过，虽然这种标记在一些简单的应用场景中得到了广泛应用，比如对字符串长度的限制、序列迭代次数的限制，以及整数的范围限制等，但其他一些特性则较少被使用，或许也显得不那么重要了。

Customise your types to just the precise values you need - it can often reduce the number of bits-on-the-line by more than a factor of two (if PER is in use), and gives clear guidance to implementors for memory allocation decisions, such as the size of integer to use. 您可以自定义类型，只选择所需的特定数值。这样做通常可以将线上使用的位数减少一半以上（如果使用了 PER 功能的话）。此外，这种方式还为实现者提供了明确的指导，帮助他们决定使用什么大小的整型数据。

Note also (before reading on - or skipping!) that flexibility in subtype notation was considerably enhanced in 1994, so some of the examples given below would not be legal pre-1994. Check the actual ASN.1 specification! 另外，请注意（在继续阅读或跳过这部分内容之前）：1994 年之后，子类型表示的灵活性得到了显著提升。因此，下面给出的一些示例在 1994 年之前可能是不合法的。请参考实际的 ASN.1 规范文档以获取更多信息！

We have very briefly met subtyping in figure 13, where (omitting the distinguished values) we had a sequence element of: 我们在图 13 中简要介绍了子类型概念。在这里，我们省略了那些特殊的数值，只关注以下内容：

 

$$
\text { no - of - days - reported - on } \quad \text { INTEGER (1..56) }
$$

 

restricting the range of the integer field to the values 1 to 56. 将整数字段的范围限制在 1 到 56 之间。

In the pre-1994 ASN.1, this notation in round brackets was regarded as producing a new type consisting of a subset (hence subtyping) of the values in the original or parent type. Post-1994, the view-point tends to be more that we are constraining the integer to be in the range 1 to 56. Why the difference? Well, post-1994 a number of other constraint mechanisms were introduced (also within a pair of round-brackets following the type being constrained), but more importantly, focussing on the notation as a constraint raises the question "And what if I get incoming material that violates the constraint?". The general issue of constraints (and associated exception handling) is left to Chapter 7 of this section, but here we will fully discuss the simple subtype notation, first introduced into ASN.1 in 1986. 在 1994 年之前，ASN.1 中，这种圆括号中的表示方式被视作一种新类型的定义方式，它实际上是对原始类型或父类型中值的子集进行归类处理。而自 1994 年之后，人们的观点更倾向于认为，我们只是限制了整数的取值范围，使其只能处于 1 到 56 之间。为什么会有所区别呢？因为在 1994 年之后，又引入了许多其他约束机制（这些机制也是通过圆括号来表示的，位于被约束类型的后面）。但更重要的是，将这种表示方式视为一种约束机制，就会引发一个问题：如果收到不符合该约束条件的输入数据该怎么办？关于约束机制的一般问题（以及相关的异常处理），我们将在本章的第七章中进行讨论。不过在这里，我们会详细探讨一下这种简单的子类型表示方式，它最早是在 1986 年被引入 ASN.1 中的。

When subtyping was introduced into ASN.1, the Basic Encoding Rules were not changed. They were TLV-based, and using subtype information to, for example, eliminate the "L" part, would have destroyed the structure of the encoding. So up to 1994, application of subtyping merely helped the writer of application-code - it did not affect encoding, or the number of bits-on-the-line. With the introduction of the Packed Encoding Rules (PER), the encoding is affected by subtyping (particularly of integers). To gain maximum benefit from PER, application designers should include range information (and length constraints on strings, and iteration constraints on set-of and sequence-of) whenever they reasonably can. 在 ASN.1 中引入子类型机制时，基本编码规则并未发生变化。这些规则仍然基于 TPV（技术参数值）结构，而使用子类型信息来消除“L”部分等处理方式，实际上会破坏编码的结构。因此，直到 1994 年，子类型机制的应用仅仅有助于应用程序编写者更方便地组织代码——它并没有影响编码方式，也不会改变每行代码的位数。随着打包编码规则（PER）的引入，子类型机制开始对编码产生影响，尤其是对于整数类型的编码。为了最大限度地利用 PER 的功能，应用程序设计者在合理的情况下，应该尽可能包含范围信息（以及字符串的长度限制，以及集合和序列的迭代限制）。

In PER there is the concept of "PER-visible constraints" - things that affect the encoding. Not all subtyping constructs are PER-visible (and in particular inner subtyping - see below - is never PER-visible for good reasons). It is tempting to suggest (see figure 999 again!) that you can ignore - don't learn about, don't use - any subtyping notation that is not PER-visible, but this would be bad advice, as a new super-PER could at some stage be defined that would take account of the more complex constraints. The right advice is: "If you intend your applications to use only a subset of the values of some type, then try to express that formally using the ASN.1 subtype notation, not just as comment." 在 PER 中，存在“PER 可见约束”这一概念——指的是那些影响编码的因素。并非所有的类型标注都是 PER 可见的（尤其是内部类型标注——详见下文——由于某些原因，它们永远都不是 PER 可见的）。人们可能会想建议说（再次参考图 999！），可以忽略那些非 PER 可见的类型标注，不要去了解或使用它们。但这样的建议并不明智，因为将来可能会定义出一种新的超级 PER，能够考虑到更为复杂的约束条件。正确的做法应该是：“如果你打算让应用程序只使用某个类型的部分取值，那么请尝试使用 ASN.1 类型标注来正式表达这一点，而不是仅仅在注释中提及。”

## 2 Basic concepts and set arithmetic 2. 基本概念与集合算术

Before looking at the different forms of subtype notation, it is important to recognise that subtype notation (like tagging - see the next chapter) is formally producing a new type. So wherever ASN.1 requires/allows type-notation, you can instead write: 在了解不同形式的子类型表示法之前，重要的是要认识到，子类型表示法（类似于标签标注——请参见下一章）实际上是在创建一个新的类型。因此，在 ASN.1 中，只要需要/允许使用类型表示法的地方，就可以这样书写：

The subtype notation is applied to a type (the parent type) and produces a new type that contains a subset of the set of abstract values in the parent type. 这种子类型标记被应用于某个类型（即父类型），从而生成一个新的类型。这个新类型包含了父类型中抽象值的子集。

## type-notation subtype-notation 类型表示法 子类型表示法

although the "subtype-notation" has to be one of the allowed notations for the parent type given by "type-notation". "subtype-notation" always begins and ends with round brackets. 虽然“亚型表示法”必须是根据“类型表示法”所给出的父类型的允许表示法之一。这种表示法总是以圆括号开头和结尾。

This idea can be recursively applied. So you can, for example, write: 这个想法可以递归地应用。例如，你可以这样写：

My-string1 ::= PrintableString (SIZE (1..10)) (FROM ("A" .. "Z")) 我的字符串 1 ::= 可打印字符串（大小 1 到 10）（来自“A”到“Z”字母）

This first defines a type which is PrintableString restricted to strings between and 1 and 10 characters, then further restricts this to strings that contain only the characters "A" to "Z". 首先，定义了一个类型为 PrintableString 的类型，该类型只包含长度在 1 到 10 个字符之间的字符串，并且这些字符串只能包含字母“A”到“Z”。

There is another subtype notation that can do the same job in one go using set arithmetic. We can write: 还有一种子类型表示法，它能够通过集合运算一次性完成相应的操作。我们可以这样书写：

```sql
INTEGER ( A EXCEPT ( B EXCEPT C ) ) 
```

 

$$
\text { My - string2 }:: := \text { PrintableString } (\text SIZE(1..10)INTERSECTIONFROM("A" .. "Z"))
$$

In this notation, the "SIZE (1..10)" selects the set of all values of PrintableString that have lengths between 1 and 10 inclusive. The "FROM ("A" .. "Z")" selects all values of PrintableString which contain only the characters "A" to "Z". The mathematical intersection of these sets gives exactly the same set of PrintableString values as was specified by My-String1 above. 在这种表示方式下，"SIZE(1..10)"表示选取所有长度在 1 到 10 之间的 PrintableString 值。"FROM("A" .. "Z")"则选取所有只包含字符"A"到"Z"的 PrintableString 值。这两个集合的交集，就得到了与上面定义的 My-String1 相同的 PrintableString 值集合。

In general, the construction in round-brackets contains a number of terms separated by the words "INTERSECTION", "UNION", "EXCEPT", with the "normal" precedence (INTERSECTION binds tightest, EXCEPT binds least tightly). Each term formally identifies a set of values of the parent type (PrintableString in the case above), and normal set arithmetic is applied to determine which values are in the resulting new type. 通常，在圆括号中的构造包含多个项，这些项被“INTERSECTION”、“UNION”、“EXCEPT”这些词分隔。按照“正常”的优先级顺序，这些词的作用如下：INTERSECTION 的优先级最高，而 EXCEPT 的优先级最低。每个项都代表父类型的一个值集合（在上面的例子中就是 PrintableString），然后应用常规的集合运算来确定新类型中哪些值属于该类型。

(As an aside, it is illegal ASN.1 if the set-arithmetic results in a type being defined that has no values!). （顺便说一下，如果集合运算的结果导致定义了一个没有任何值的类型，那么这种做法就是非法的 ASN.1 规范。）

Note also that, to avoid confusion for the reader on precedence 另外，为了避免让读者产生混淆，需要注意优先级的问题。

## INTEGER ( A EXCEPT B EXCEPT C ) 整数（不包括 A、B 和 C）

is disallowed, and has to be written as: 这种表达方式是不被允许的，必须写成：

```txt
INTEGER ( ( A EXCEPT B ) EXCEPT C ) 
```

whichever was intended. There is no equivalent restriction for UNION and INTERSECTION, because if both the "EXCEPT"s above are replaced by "UNION" (or by "INTERSECTION"), the two different bracket patterns produce identical resulting sets. 无论哪种情况都是如此。对于 UNION 和 INTERSECTION 操作，并没有相应的限制条件，因为当上述“EXCEPT”操作被“UNION”或“INTERSECTION”替代时，这两种不同的括号使用方式会得到相同的结果集。

It is also possible to write 也可以这样书写：

## INTEGER ( ALL EXCEPT (1..20) ) 整数类型（所有整数，除了 1 到 20）

with the obvious meaning. ("ALL" can only be followed by "EXCEPT"). 具有显而易见的含义。（“ALL”后面只能接“EXCEPT”）。

A more complex example (exercise for the reader - find a real-world example where this sort of construction would be useful!) would be: 一个更复杂的例子（供读者练习——请找到一个现实世界中的例子，来说明这种结构在实际情况中的实用性！）如下：

```txt
My-string3 ::= PrintableString
( SIZE (1..10) INTERSECTION FROM ("A" .. "Z")
UNION
("yes" UNION "no" UNION maybe)
EXCEPT
"A" UNION B) 
```

I think you can work out what that means, but if not, come back to it when you have read what follows! Note that the absence of quotation marks around "maybe" and "B" above was not a typo! "maybe" is assumed to be a value-reference-name for a value of type PrintableString (assigned elsewhere in this module), and B is assumed to be a type-reference-name for a subtype of PrintableString (also assigned elsewhere in this module)! Remember that wherever explicit valuenotation for a value is allowed, a value-reference-name is also allowed (provided it refers to a value of the parent type), and (less obviously perhaps) wherever a subset is needed for set arithmetic, a type-reference-name can be used (provided it refers to a subtype of the parent type). 我想你可以自己推断出那是什么意思。不过，如果你还是不明白，那就继续阅读接下来的内容吧！注意，上面“maybe”和“B”之间没有引号，这不是拼写错误！这里的“maybe”被当作一个值引用名，指的是类型为 PrintableString 的值（该值在其他地方也有定义）。而“B”则被当作一个类型引用名，指的是 PrintableString 的子类（同样在其他地方也有定义）。记住，在允许使用值明确标注的情况下，也可以使用值引用名（只要它指的是父类型的某个值）。另外，在需要进行集合运算时，也可以使用类型引用名（只要它指的是父类型的子类）。

The alert-alert-reader (!) may be beginning to ask what the exact rules are about the way a valuereference-name or type-reference-name has to be defined in order to be legal in some set-arithmetic with a particular governor (parent type). This is covered in the description of the ASN.1 Semantic Model in Sectin IV, but it is sufficient to note for now that if it would make sense to a human reader it is almost certainly legal! 该警报器可能已经开始询问关于“值引用名”或“类型引用名”的定义规则究竟是什么，以便其在某个特定的语法规则下在某种算术运算中能够合法使用。这一点在 ASN 的语义模型描述中有所涉及，不过目前可以认为，对于人类读者来说，这样的定义几乎肯定是合法的！

Note that value-notation for a type defined using subtype-notation is not affected by that notation - it remains the normal value notation for the parent type. 需要注意的是，使用子类型表示法定义的类型的值表示方式并不会受到该表示法的影響——它仍然采用父类型通常使用的正常值表示方式。

One final global comment: the word "INTERSECTION" can be replaced by the "caret" symbol: "^", and the word "UNION" by the "vertical-bar" symbol: "|", but you are recommended not to mix and match in any one application specification! For me, ASN.1 specifications tend to be quite verbose anyway - longish names are common - so I prefer the words! 最后一点关于全局性的说明：单词“INTERSECTION”可以用“caret”符号“^”替代；而单词“UNION”则可以用“vertical-bar”符号“|”替代。不过，建议不要在任何一个应用规范中混合使用这些符号。对我来说，ASN.1 规范通常比较冗长——经常看到较长的名称——所以我还是更喜欢使用文字来表示这些符号。

What then are the basic terms that we can use - either as stand-alone subtype constraints in round brackets, or as part of a possibly complex set-arithmetic expression, and what set of values do they identify? 那么，我们可以使用的基本术语有哪些呢？这些术语可以单独用作圆括号中的子类型约束，也可以作为更复杂的集合运算表达式的一部分来使用。它们所代表的数值范围又是什么呢？

We treat each possibility below. Note that in some cases the clause has "subtyping" or "subtype" in its heading, and in other cases the word "constraint" is used. This reflects the terms used in the ASN.1 specification itself, and reinforces the point that for most purposes the two words are interchangeable. 我们逐一考虑以下每种可能性。请注意，在某些情况下，条款的标题中会使用“子类型”或“亚型”这样的术语；而在其他情况下，则使用“约束”这个词。这反映了 ASN.1 规范中使用的术语，同时也强调了对于大多数情况来说，这两个词是可以互换使用的。

## 3 Single value subtyping 3 单值子类型划分

This can be applied to any parent type. (Remember that there is value notation for any type we can define in ASN.1). We just list the permitted value! Normally this would be accompanied by use of vertical bar or UNION. So: 这适用于任何父类型。记住，在 ASN 中，我们可以为任何类型定义值表示法。我们只需要列出允许的值即可！通常，这会伴随着垂直杠号或 UNION 的使用。所以，表达方式就是这样的：

and 以及

```haskell
Yes ::= PrintableString ("Yes")
Yes-No ::= PrintableString ("Yes" | "No") 
```

are examples that use single value subtyping. The set of values identified by each use of single value subtyping is just that single value identified by the value notation. 这些都是使用单值类型化的例子。每次使用单值类型化时所确定的值集，实际上就是数值表示法所标识的那个单一值。

## 4 Value range subtyping 4. 数值范围子类型划分

This can only be applied directly to integer and real types, but the same construction following the word "FROM" is used to restrict the set of characters that are permitted in some character string types (see "permitted alphabet" below). 这种规则只能直接应用于整数和实数类型。不过，通过“FROM”关键字所描述的相同操作，可以限制某些字符字符串类型中允许的字符集（详见下文的“允许的字符集”部分）。

<table><tbody><tr><td data-imt-p="1">Value range subtyping is frequently applied to specify the range of integer values. 数值范围子类型划分常被用于指定整数值的范围。</td></tr></tbody></table>

The end-points of a range of values are given, and the set of values identified by the notation is precisely those from one end-point to the other (including the end-points). This is the notation we encountered earlier, and which is often seen to constrain integer values: 该数值范围的终点已经给出，而用这种符号表示的一组数值，实际上就是从一个终点到另一个终点的所有数值，包括这两个终点本身。这就是我们之前遇到的那种符号表示方式，它通常用于限定整数的取值范围。

As usual, intersections and unions of these constraints are possible, but are rarely seen. 像往常一样，这些约束条件也可以进行交集和并集的操作，不过这种情况很少出现。

## 5 Permitted alphabet constraints 5. 允许的字母表约束条件

This is a constraint which can only be applied to the character string types (not including the type "CHARACTER STRING"). 这是一个只能应用于字符串类型的数据类型限制（不包括“CHARACTER STRING”类型）。

In its simplest form this constraint is the word "FROM" followed by a character string containing a set of permitted characters. Thus: 在最简单的形式下，这个约束条件由单词“FROM”加上一个包含若干允许字符的字符串组成。因此可以表示为：FROM 一个包含允许字符的字符串。

Some encoding rules (unaligned PER) will use the minimum number of bits per character, depending on how many different characters you allow in a string, so imposing alphabet constraints can save bits on the line. 某些编码规则（如非对齐 PER 编码）会采用每个字符所需的最少位数，这一位数目取决于字符串中允许使用的不同字符数量。因此，施加字母表约束可以节省行级代码量。

or 或

```txt
String-of-vowels1 ::= PrintableString (FROM ("AEIOU"))
String-of-vowels2 ::= PrintableString (FROM ("AEIOU")
UNION
FROM ("aeiou")) 
```

would be possible examples. The opening bracket following "FROM" may appear unnecessary and looks cumbersome, but the syntax definition allows a fully general constraint following FROM, so 以下是一些可能的例子。在“FROM”之后加上括号可能看起来有些多余且不美观，但按照语法定义，可以在“FROM”之后直接添加完全通用的约束条件。因此，这样的结构是完全可行的。

```lisp
String-of-vowels3 ::= PrintableString (FROM ("AEIOU" UNION "aeiou")) 
```

is also permitted. 也是被允许的。

The constraint following "FROM" is required to be one that could be directly applied to the parent type to produce a set of string values (call this the defining set of string values (a term used only in this book). The effect of "FROM" is to allow (in the subset of string values selected by "FROM") all strings of the parent type which contain (only) any of the characters in any of the string values in the defining set. “FROM”后面的约束条件必须能够直接应用于父类型，从而生成一组字符串值（我们将这称为“定义字符串值集”——这一术语仅出现在本书中）。“FROM”的功能是：在由“FROM”选定的字符串值集中，允许父类型中的所有字符串包含定义集中的任何一个字符串值所包含的字符。

An exercise: read this definition carefully, then answer the question "Are String-of-vowels2 and String-of-vowels3 equivalent definitions?". Read on when you have your answer! 练习：请仔细阅读这个定义，然后回答这个问题：“String-of-vowels2 和 String-of-vowels3 是等效的定义吗？”等你找到答案后，继续阅读吧！

We reason it through. With "String-of-Vowels2", we first define two sets of PrintableString values. One is all strings made up of upper case vowels only and the other is all strings made up of lower case vowels only, and we take the union of these two sets. Thus the end result allows strings containing only vowels, but each string must be entirely upper case or entirely lower case. With "String-of-Vowels3", we first produce a set with just two string values, each of five characters: "AEIOU" and "aeiou". We then apply "FROM" to this set, allowing as the end result strings made up of arbitrary combinations of upper and lower case vowels, so "String-of-Vowels2" and "String-of-Vowels3" are not the same. 我们通过推理来得出这个结论。对于“String-of-Vowels2”来说，我们首先定义了两组可打印字符串的集合。第一组包含仅由大写元音字母组成的字符串，第二组包含仅由小写元音字母组成的字符串。然后，我们将这两组集合进行合并，从而得到一组包含仅由元音字母组成的字符串，但每个字符串必须完全由大写字母或完全由小写字母组成。而对于“String-of-Vowels3”来说，我们首先得到了一个只包含两个字符串集合，每个字符串由五个字符组成，分别是“AEIOU”和“aeiou”。接着，我们对这个集合应用“FROM”操作，最终得到一组包含由大写和小写元音字母任意组合而成的字符串。因此，“String-of-Vowels2”和“String-of-Vowels3”并不相同。

The above used only single value subtype notation in the constraint following FROM, but any subtype notation that can be applied to the parent type can be used. In particular, value range subtyping is explicitly permitted for application to certain character string types when it is used in the constraint following FROM, and is restricted to strings containing only a single character. 在 FROM 后面的约束条件中，仅使用了单一值子类型表示法。不过，任何可以应用于父类型的子类型表示法都可以被使用。具体来说，当在 FROM 后面的约束条件中使用时，允许对某些字符串类型进行值范围子类型标注，且这种标注仅限于包含单个字符的字符串。

Thus we can write: 因此，我们可以写成：

```lisp
Hex-digit-String ::= PrintableString (FROM ("0"..."9" UNION "A"..."Z" UNION "a"..."z")) 
```

which first forms the set of all single character strings using digits and letters (62 string values), and then applies FROM to this set to generate the set of all PrintableString values containing only these 62 characters. 首先，会生成包含所有单个字符的字符串集合，这些字符串由数字和字母组成（共 62 个字符）。然后，对这堆字符串应用“FROM”操作，从而生成所有只包含这 62 个字符的可打印字符串集合。

The value range constraint can be used in this way for those character string types for which an ordering of the characters is well-defined (BMPString, IA5String, NumericString, PrintableString, VisibleString, UniversalString, UTF8String), but not for character string types based on the International Register of Coded Character Sets (GeneralString, GraphicString, TeletexString, or ViedotexString), where ordering is not easy to define. 这种价值范围限制适用于那些字符顺序具有明确定义的字符串类型，例如 BMPString、IA5String、NumericString、PrintableString、VisibleString、UniversalString 和 UTF8String。而对于那些基于国际编码字符集的字符串类型，比如 GeneralString、GraphicString、TeletexString 或 ViedotexString，则不适合使用这种限制，因为这些类型的字符顺序并不容易定义。

## 6 Size constraints 6. 尺寸限制

A size constraint has a similar structure to a permitted alphabet constraint. It consists of the word "SIZE" followed by any constraint specification (in parentheses) that can be applied to a non-negative integer. It can (only) be applied to a bit-string, an octet-string, a “大小限制”这一约束条件的结构与“允许的字母表约束”类似。它由一个单词“SIZE”加上任何可以应用于非负整数的约束条件组成（条件说明位于括号内）。该约束条件只能应用于位串、八位串或……

Size constraints use value ranges to specify the permitted lengths of strings and iteration counts. Their use can again save bits on the line. 尺寸限制通过使用数值范围来指定字符串的允许长度以及迭代次数。这种用法同样可以节省代码行数。

character string (including the type "CHARACTER STRING" introduced in a later chapter) or to a "SEQUENCE OF" or "SET OF" construction. Its effect is to select those values of the parent type that contain a number of characters or iterations equal to one of the integer values in the set selected (from non-negative integers) by the constraint following the word "SIZE". 字符串（包括在后续章节中介绍的“字符字符串”类型），或者可以指“一系列”或“一组”构造。它的作用是从父类型中选择那些包含与由“SIZE”一词所指定的集合中的某个非负整数值相等的字符数或迭代次数的值。

In the case of "SEQUENCE OF Xyz" and "SET OF Xyz", the constraint can appear after the type definition, or immediately before the "OF". This is necessary to allow constraints to be applied to both the iteration counts and to the type being iterated, in cases such as 在“Xyz 序列”和“Xyz 集合”的情况下，该约束可以出现在类型定义之后，也可以出现在“OF”字样的短语之前。这样做是为了让约束能够同时应用于迭代次数以及被迭代的类型，比如在以下这种情况下：

## SEQUENCE OF SEQUENCE OF PrintableString (SIZE (10)) 可打印字符串序列（长度范围为 10）

This syntax would restrict the PrintableString to exactly ten characters, and cannot be used to constrain the iteration counts. To constrain these, you would use 这种语法会将 PrintableString 限制为恰好十个字符，因此无法用来限制迭代次数。若要限制迭代次数，应该使用其他方法。

SEQUENCE (SIZE (10)) OF SEQUENCE OF PrintableString 可打印字符串序列（长度：10）

or 或

SEQUENCE OF SEQUENCE (SIZE (10)) OF PrintableString 可打印字符串的序列（大小：10）

Once again, ASN.1 is fully general in this area - the constraint notation appearing before the OF is a general constraint that can contain unions and intersections etc, although the pre-1994 specifications were more restrictive. 再次强调，ASN.1 在这一领域具有完全的通用性——在 OF 之前出现的约束符号是一种通用的约束条件，可以包含联合、交集等运算。不过，1994 年之前的规范则更为严格。

In practice, the constraint following the word "SIZE" is almost always a single value constraint or a value range constraint, such as: 在实践中，与“SIZE”相关的约束几乎总是一种单一值约束或值范围约束，例如：

$$
\begin{array}{c} \text {SEQUENCE (SIZE (1..100)) OF SEQUENCE (SIZE (20)) OF} \\ \text {PrintableString (SIZE (0..15))} \end{array}
$$

```txt
PrintableString ( SIZE (1..10) INTERSECTION FROM ("A"."Z")) 
```

which could represent a table of one to one-hundred rows with twenty columns, each cell containing a PrintableString which is either empty or up to 15 characters long. 这可能代表一个包含 100 行、20 列的表格，每个单元格中包含一个 PrintableString 对象，该对象可以是空的，或者包含最多 15 个字符。

Going back to our Wineco-protocol, and referring to figure 22 in Section I Chapter 4, we originally defined "sales-data" as an unlimited number of "Report-item". It is generally quite hard for an implementor to support unlimited numbers of things, although with increasing memory sizes now easily available and large capacity disks, implementation of "effectively unlimited" (which is what we mean here) is possible. Both the BER and PER encodings will support the transfer of effectively unlimited numbers (and sizes) of things, but with PER the encoding will be more efficient if it is possible to limit counts and integer values, for example to values which can be held in two or four octets. 回到我们的 Wineco 协议，参考第 4 章第 1 节的图 22，我们最初将“销售数据”定义为无限数量的“报告项”。对于实施者来说，支持无限数量的项通常是非常困难的，不过随着现在可使用的内存容量越来越大，以及大容量磁盘的出现，实现“实际上无限”的数量（这正是我们在这里所指的是）已经变得可能了。无论是 BER 编码还是 PER 编码，都能支持传输实际上无限数量的项目（以及无限大的数据量）。不过，如果能够将计数和整数值限制在一定范围内，比如只占用两个或四个八位元的数值，那么使用 PER 编码会更为高效。

It would be common practice to replace the "sales-data" line with: 通常会将“销售数据”这一行替换为以下内容：

 

$$
\text { sales - data } \quad \text { SEQUENCE (SIZE (1..sales - ub)) OF Report - Item }
$$

 

The value reference "sales-ub" is required to be an integer value reference, and might be assigned in a module which collects together all such bounds, using EXPORTS/IMPORTS to make it available in the context of figure 22. A typical assignment might be: 数值参考“sales-ub”必须是一个整数类型的值，它可以被存储在某个模块中，通过 EXPORTS/IMPORTS 功能将该模块的内容在图 22 的上下文中呈现出来。一个典型的赋值方式可能是：

```txt
sales-ub INTEGER ::= 10000 
```

Consider a final example using both FROM and SIZE: 最后，让我们来看一个同时使用 FROM 和 SIZE 的示例：

Take a moment to work out what this means before reading on. 在继续阅读之前，请花一点时间来理解这句话的含义。

We first select the (finite) set of all strings with one to ten characters in them, and we intersect that with the (infinite set) of all strings made up solely of the characters "A" to "Z". The end result is the set of strings of one to ten characters which contain only the letters "A" to "Z". Note that exactly the same result is obtained by any of: 我们首先选取所有由 1 到 10 个字符组成的字符串的（有限）集合，然后把这个集合与由字母“A”到“Z”组成的无限集合相交。最终得到的就是由 1 到 10 个字符组成的、且只包含字母“A”到“Z”的字符串的集合。注意，通过任何一种方法都可以得到完全相同的结果。

```txt
PrintableString (SIZE (1..10)) (FROM ("A".."Z")) 
```

```txt
PrintableString (First) (Second) 
```

where 在何处

```autohotkey
Second ::= PrintableString (FROM ("A" .. "Z")) 
```

## 7 Contained sub-type constraints 7 包含子类型约束条件

We have met this notation informally on a couple of occasions above. This form of constraint is where we provide a type reference name (for a subtype of the parent type) to identify the set of values to be included. This would not normally be useful unless it was within a more complex constraint using intersections, or with repeated application of constraints, as in the cases 我们在上面已经几次非正式地提到过这种表示方式。这种约束形式指的是我们提供一个类型引用名称（用于指代父类型的子类型），以标识需要包含的值集。不过，这种情况通常并不适用，除非是在使用更复杂的交集约束，或者是在多次应用约束的情况下才需要这样做。

PrintableString ( First INTERSECTION Second ) 可打印字符串（第一个点，第二个点）

and 以及

PrintableString (First) (Second) 可打印字符串（第一个） （第二个）

above. 以上。

Note that pre-1994, use of a type reference name in this way in a constraint required the name to be preceded by the word "INCLUDES", and it is still permissible to write (for example): 请注意，在 1994 年之前，在约束条件中使用类型引用名称时，必须在名称前加上“INCLUDES”这个词。不过，现在仍然可以这样书写（例如）：

PrintableString (INCLUDES First INTERSECTION INCLUDES Second) 可打印的字符串（包含“第一个包含部分”和“第二个包含部分”）

or 或

PrintableString (INCLUDES First EXCEPT INCLUDES Second) 可打印的字符串（包含“第一”以及“第二”两个元素）

but these do not read very well, and it is best to omit the word "INCLUDES". 不过，这些文字读起来并不舒服，所以最好把“INCLUDES”这个词省略不写。

## 8 Inner Subtyping 8 内部亚型分类

## 8.1 Introduction 8.1 引言

Inner subtyping is an important and under-used tool. It is often the case that application designers have invented a new meta-notation of their own (not supported by ASN.1 tools) to produce specifications which could more sensibly have been written using inner subtyping (which is supported by the OSS tool). Not only does this 内部类型标注是一种非常重要但被低估的工具。通常情况下，应用程序设计者会发明出自己的新元符号来表示类型，而这些元符号并不被 ASN.1 工具所支持。因此，他们编写的规范可能无法用内部类型标注来更清晰地表达出来（而内部类型标注是开源工具所支持的）。这不仅……

Inner subtyping is an important mechanism that can help to give precision to the specification of subsets or conformance classes of a protocol. 内部类型划分是一种重要的机制，它能够帮助提高协议子集合或一致性类别的规范精度。

require the reader to get used to the ad hoc notation, but it can also make the implementor's work unnecessarily hard, with some sort of ad hoc pre-processing of the specification needed before use of ASN.1 tools. 这可能需要读者逐渐适应这种特殊的标记方式。不过，这样做也会让实现者的工作变得复杂化，因为在使用 ASN.1 工具之前，通常需要对规范进行某种形式的预处理工作。

It is likely, perhaps probable, that this occurs through ignorance. Inner subtyping has an overall importance which is not brought out by its positioning as "just another subtyping notation" in the ASN.1 specification. 很可能，甚至可以说是必然，这种情况是由于无知所导致的。内部类型划分其实具有非常重要的意义，这一意义并非因为其在 ASN.1 规范中被简单地归类为“另一种类型表示方式”而就被忽视了。

The subtype notations described so far provide a very powerful tool for application designers to clearly specify the range of permitted values in their protocols for the basic types, but there is another requirement: some designers have a requirement to define a number of different subsets of a protocol to suit different purposes, different so-called "conformance classes". 到目前为止所描述的子类型标记，为应用程序设计者提供了非常强大的工具，使他们能够清晰地指定基本类型在协议中允许的值范围。不过，还有另一个需求：一些设计者希望定义多个不同的协议子集，以适应不同的用途，也就是所谓的“符合等级”。

In the simplest case, we have a "Full Class" protocol in which each message is some defined ASN.1 type such as the "Wineco-Protocol" in figure 21 of Section 1 Chapter 3, but we also wish to define a "Basic Class" protocol in which some of the optional elements of sequences are required to be omitted, others are required to be always included, some of the choices are restricted, and some of the iterations and/or integer values have restricted values. 在最简单的情况下，我们采用“完整类”协议，在这种协议中，每条消息都属于某种定义好的 ASN 类型。例如，第 3 章第 1 节的图 21 中的“Wineco-Protocol”协议就属于这种类型。不过，我们还希望定义一种“基础类”协议，在这种协议中，某些可选元素必须被省略，而另一些则必须始终包含在内。此外，某些选择项会受到限制，还有一些迭代操作和/或整数值也有特定的取值范围。

If you consider the set of abstract values of the "Wineco-Protocol" type, you will recognise that all the restrictions described above (including requiring some optional elements to be present and others to be absent) are simply the selection of a particular subset of the "Wineco-Protocol" values - in other words, subtyping! 如果你考虑一下“Wineco-协议”类型的抽象价值集合，你会意识到上述所有限制条件（包括要求某些可选元素必须存在，而另一些则必须不存在）实际上都是对“Wineco-协议”值的一个特定子集的选择——换句话说，就是对其进行子类型划分而已！

There are, however, two additional requirements: 不过，还有两个额外的要求需要满足：

• First, it needs to be possible to define both of the conformance classes without duplication of text (and hence scope for error). • 首先，必须能够同时定义这两个符合标准的内容，而不会造成文本重复的情况（从而避免出错的可能性）。

Secondly (for some but not all applications) the encoding of those values that are present in both the "Basic Class" protocol and the "Full Class" protocol should be the same in both protocols. 其次（对于某些应用来说），那些同时出现在“基础类”协议和“完整类”协议中的值，在这两个协议中应该采用相同的编码方式。

The latter requirement is so as to enable easy interworking between "Full class" and "Basic Class" implementations. 后一个要求是为了实现“完全类”和“基础类”实现之间的轻松互操作。

There is a relationship between this area and the "extensibility" issues described later, but there are differences. "Extensibility" refers to differences in specifications over time (different versions) where the maximal functionality is not known when the first systems are deployed, whereas here we are concerned with differences in implementations where maximal functionality is known from the start, permitting a somewhat simpler approach. 这个领域与后面提到的“可扩展性”问题之间存在一定的关联，但两者也有差异。“可扩展性”指的是随着时间推移而产生的规格差异（即不同版本之间的差异），在首次部署系统时，其最大功能是不确定的。而在这里，我们关注的是实现上的差异，这些实现从一开始就能知道其最大功能，因此可以采用较为简单的解决方案。

In order to define all conformance classes without duplication of text, it is necessary to: 为了明确所有符合要求的类别，同时避免文本重复，有必要做到以下几点：

• (first) define the "Wineco-Protocol" type with maximal functionality, providing it with a type reference name; then • 首先定义具有最大功能的“Wineco-Protocol”类型，并为该类型指定一个类型引用名称；然后……

to use this type reference name and apply to it the constraints which generate the "Basic-Ordering-Class" and "Basic-Sales-Data-Class" (or other conformance classes). The latter is achieved by placing subtype constraint notation, in parentheses, following the type reference name. So we have: 使用这种类型的参考名称，并为其应用那些能够生成“Basic-Ordering-Class”和“Basic-Sales-Data-Class”（或其他相关一致性类）的约束条件。后者是通过在类型参考名称后面加上括号中的子类型约束表示法来实现的。因此，我们的表达应该是这样的：

 

$$
\text { Basic - Ordering - Class }: := \text { Wineco - Protocol } (\dots \dots)
$$

The (.......) is the inner subtyping constraint, where we constrain the inner components of "Wineco-Protocol". (.......)指的是内部子类型约束，我们在这里对“Wineco-Protocol”的内部组件进行约束。

It is important to note that in both BER and PER, the application of these constraints does not affect the encoding of the values that are in the selected subset - they are encoded exactly as in the "Full-Class" protocol. By contrast, if constraints (such as removal of some choices, or making optional fields mandatorily present or absent) were specified by an ad hoc meta-language that modified the ASN.1 text (or by explicitly writing out the Basic Class protocols), the encoding of values in the Basic Class would be different from that of the corresponding values in the Full Class, and care would also need to be taken that rules on unambiguous tags (see below) were not violated with any of the variants that were produced. 需要注意的是，在 BER 和 PER 中，这些约束条件的应用并不会影响所选子集中值的编码方式——这些值的编码方式与“完整类”协议中的编码方式完全相同。相比之下，如果通过某种特定的元语言来指定约束条件（例如删除某些选项，或者强制某些字段必须存在或不存在），从而修改 ASN.1 文本，或者直接按照基本类协议进行编码，那么基本类中的值编码方式就会与完整类中的值编码方式有所不同。此外，还需要注意，在任何这些变体中，都不能违反关于唯一标签的规定（详见下文）。

This is another reason why use of inner subtyping should be preferred to an ad hoc "pre-processor" notation - it ensures that encodings and taggings are the same in all classes. 这也是为什么应该优先使用内部类型划分，而不是采用特定的“预处理器”表示方式的原因之一——因为这种方式可以确保所有类中的编码和标签都是一致的。

## 8.2 Subsetting Wineco-Protocol 8.2 对 Wineco 协议进行子集化处理

Once again, let us proceed with an illustration first. Consider figure II-3. This repeats the toplevel definition of figure 21, but now we have moved to version 2 (produced in AD 2002), and have an additional top-level choice available to enable us to up-load the contents of the electronic cash in our till. (The fact that this follows an extension marker makes no difference to the inner subtyping notation, and for the moment the presence of the extension marker line should be completely ignored.) Refer also to Appendix 2 that contains the full definition of Wineco-Protocol. 再次，让我们先通过一个示例来说明这个问题。请看图 II-3。这个图重复了图 21 中的顶层定义，但现在我们处于版本 2 的状态（该版本是在公元 2002 年生成的），并且我们有了一个额外的顶层选项，可以用来上传电子现金账户中的内容。（尽管存在扩展标记，但这对内部类型注释并没有任何影响；目前，可以忽略这个扩展标记线。）此外，请参阅附录 2，其中包含了 Wineco 协议的全部定义。

```txt
Wineco-Protocol ::= CHOICE
{ordering [APPLICATION 1] Order-for-Stock,
sales [APPLICATION 2] Return-of-sales-data,
... ! PrintableString : "See clause 45.7",
e-cash-return -- Added in version 2 --
[APPLICATION 3] Cash-upload}

Basic-Ordering-Class ::= Wineco-Protocol
(WITH COMPONENTS
{ordering (Basic-Order) PRESENT,
sales ABSENT } )

Basic-Sales-Class ::= Wineco-Protocol
(WITH COMPONENTS
{ordering ABSENT,
sales (Basic-Return) PRESENT } )

Figure II-3: Constraining in version 2 
```

Here we have restricted the outer-level choice by making precisely one of the version 1 alternatives always present and the other always absent. We are further applying included subtype constraints (see above) "Basic-Order" and "Basic-Return" to the alternative that is present, restricting it further. We will shortly define the types "Basic-Order" and "Basic-Return". 我们通过对高层选项进行限制，使得版本 1 中的两个选项中只能有一个始终存在，另一个则始终不存在。此外，我们还对存在的那个选项应用了包含的子类型约束（参见上文）“基本顺序”和“基本返回”，从而进一步限制其限制范围。接下来我们将简要定义“基本顺序”和“基本返回”这两个类型。

Notice that here we have listed every alternative present in version 1, giving PRESENT or ABSENT. This is called a "full specification". Despite being called a "full specification", it is not actually necessary to list every alternative. ABSENT is implied for any not listed, so the definition of "Basic-Sales-Class" is equivalent to: 请注意，在这里我们列出了版本 1 中所有的选项，并标明这些选项是存在还是不存在。这被称为“完整规格说明”。虽然被称为“完整规格说明”，但实际上并不需要将所有的选项都列出。如果某个选项没有列出，那么默认就是不存在的；因此，“基础销售等级”的定义可以等同于以下内容：

and to 以及到……为止

```txt
Basic-Sales-Class ::= Wineco-Protocol
(WITH COMPONENTS
{ordering ABSENT,
sales (Basic-Return) PRESENT,
e-cash-return ABSENT}
Basic-Sales-Class ::= Wineco-Protocol
(WITH COMPONENTS
{sales (Basic-Return) PRESENT} ) 
```

(Note that there must be at least one alternative listed, and that there must be exactly one listed as PRESENT in the "full specification".) （请注意，必须至少列出一种替代方案，并且在“完整规格说明”中，只有一种方案被标记为当前可行的选项。）

There is also a "partial specification" notation in which the constraint starts with "... ,". This is shown in figure II-4, where we wish the Basic-Sales-Class2 protocol to include both "sales" and "e-cash-return" messages. "Partial specification" differs from the "full specification" only in that any alternatives not listed remain as possible unconstrained choices, and any listed are neither required to be ABSENT nor PRESENT if neither of these words are present (but may be constrained in other ways). Thus in figure II-4, either the "sales" (constrained by "Basic-Return") or the "e-cash-return" messages (unconstrained) are available and have to be implemented, but the "ordering" messages should never be sent or received and need not be implemented. 还有一种“部分规范”的表示方式，在这种表示方式中，约束条件以“…,”开头。如图 II-4 所示，我们希望 Basic-Sales-Class2 协议能够包含“sales”和“e-cash-return”这两种消息。所谓“部分规范”，与“完整规范”的区别仅在于：那些未列出的选项仍然可以作为非约束性的选择；而那些已列出的选项，在不存在“Basic-Return”或“e-cash-return”这两种情况时，既不必被排除，也不必被实现。因此，在图 II-4 中，要么实现“sales”消息（受“Basic-Return”约束），要么实现“e-cash-return”消息（无约束）。而“ordering”消息则永远不应被发送或接收，因此也不需要进行实现。

```txt
Basic-Sales-Class2 ::= Wineco-Protocol
( WITH COMPONENTS
{...,
ordering ABSENT,
sales (Basic-Return) } )
Figure II-4: Constraining only the sales alternative 
```

Let us go on to specify what is a "Basic-Return". This is shown in figure II-5 as a constrained "Return-of-sales". Note that as usual in ASN.1, we could have put the constraint "in-line" in figure II-5 and made no use of the type reference name "Basic-Report-Item". This is just a matter of style. Figure II-6 shows the same definition but with the constraint "in-line" (we have not repeated the comments in figure II-6). Whilst more compact, it is arguable that the lack of a name to associate with the inner constraint on "Report-item" in figure II-6 makes that style less readable than the slightly more verbose style of figure II-5. Both notations do, however, express exactly the same semantics. 让我们来具体说明一下什么是“Basic-Return”。在图 II-5 中，它被呈现为一个带有约束条件的“Return-of-sales”形式。注意，像在 ASN.1 中常见的那样，我们也可以在图 II-5 中直接添加该约束条件，而无需使用“Basic-Report-Item”这个类型引用名称。这仅仅是一种风格上的选择而已。图 II-6 展示了相同的定义，只不过这次约束条件是“in-line”形式（我们没有重复图 II-6 中的注释）。虽然这种形式更为简洁，但可以说，由于缺乏与图 II-6 中“Report-item”内部约束条件相关联的名称，这种形式的可读性不如图 II-5 那种稍微冗长的形式。不过，这两种表示方式实际上都表达了相同的语义。

```txt
Basic-Return ::= Return-of-sales
( WITH COMPONENTS
    {...,
    no-of-days-reported-on (7)
    -- reports must be weekly --,
    reason-for-delay ABSENT,
    additional-information ABSENT,
    sales-data (SIZE (1..basic-sales-ub)
    INTERSECTION
    (WITH COMPONENT
    (Basic-report-item) }) 
Basic-report-item ::= Report-item
( WITH COMPONENTS
    {...,
    item-description ABSENT
    -- Version 2 of Report-item allows omission
    -- of item-description even for newly-stocked
    -- items --} )
Figure II-5: Constraining "Return-of-Sales" 
```

Figures II-5 needs a little explanation of "sales-data". Here we are further constraining the number of "Report-item"s, and also restricting each "Report-item" to the subset "Basic-report-item". Notice that when we apply inner subtyping to a SEQUENCE or SET, we start the constraint with "WITH COMPONENTS", and then have paired curly brackets with the constraints (if any) on each component listed within the brackets following the name of the component. (You can see this with the constraint on "Report-item" (which is a SEQUENCE) in Figure II-5). Now suppose that one of the components of the outer SEQUENCE is a SEQUENCE 在图 II-5 中，“销售数据”这一项需要一些说明。我们进一步限制了“报告项”的数量，并且每个“报告项”都只能属于“基础报告项”这一子集。请注意，当我们对 SEQUENCE 或 SET 应用内部子类型时，我们会从“WITH COMPONENTS”开始定义约束条件，然后用大括号将每个组件上的约束条件括起来（如果有的话）。例如，在图 II-5 中，“报告项”这一项就是一个 SEQUENCE。现在假设外部 SEQUENCE 中的一个组件本身也是一个 SEQUENCE。

```txt
Basic-Return ::= Return-of-sales
( WITH COMPONENTS
    {...,
    no-of-days-reported-on (7),
    reason-for-delay ABSENT,
    additional-information ABSENT,
    sales-data (SIZE (1..basic-sales-ub)
    INTERSECTION
    (WITH COMPONENT
    ( WITH COMPONENTS
    {...,
    item-description ABSENT }) )
    }
)

Figure II-6: Applying the constraint "in-line" 
```

OF or SET OF, then we can apply a constraint to the number of iterations of the SEQUENCE OF or SET OF by directly listing it following the component name, but if we wish to constrain the type being iterated, we have to apply a further inner subtyping constraint, but this time beginning with the words "WITH COMPONENT" (instead of "WITH COMPONENTS"), followed directly by the constraint to be applied to the type being iterated. 如果是“OF”或“SET OF”，那么我们可以通过在组件名称之后直接列出迭代次数来限制序列或集合的迭代次数。但如果我们希望进一步限制迭代的类型，就需要使用一种更精细的子类约束机制。此时，我们需要从“WITH COMPONENTS”开始，紧接着就是需要应用于迭代类型的约束条件。

## 8.3 Inner subtyping of an array 8.3 数组的内部类型划分

As a final example, let us return to our two-dimensional array of PrintableString introduced earlier. We will first define: 作为最后一个例子，让我们回到之前提到的二维数组 PrintableString。首先，我们定义如下：

## Generic-array ::= SEQUENCE OF SEQUENCE OF PrintableString 通用数组 ::= 一系列可打印字符串的序列

and we will then produce a "Special-array" by inner subtyping that will be (almost - see below) equivalent to our original definition of 然后，我们通过内部子类型化操作来生成一个“特殊数组”。这个特殊数组几乎与我们对“数组”的原始定义是一致的——详见下文。

```txt
SEQUENCE (SIZE(1..100)) OF SEQUENCE (SIZE(20)) OF PrintableString (SIZE(0..15)) 
```

This is what we need: 这正是我们所需要的：

```lisp
Special-array ::= Generic-array
(SIZE (1..100) INTERSECTION
WITH COMPONENT
(SIZE (20) INTERSECTION
WITH COMPONENT (SIZE (0..15))
)
) 
```

Why only almost equivalent? It is important to remember that a PER encoding of a Generic-array with inner subtyping is always the general encoding (inner subtype constraints are not PER visible), so an implementation of Special-array with the above constraints will produce bits on the line identical with the corresponding values of "Generic-array", whilst putting in the constraints explicitly will produce a different (more compact) encoding. Where the constraints apply to all classes of implementation, or where interworking between different classes is not required, it is clearly better to embed the constraints explicitly. Where, however, interworking is required between a full implementation and a constrained implementation, it is generally better to use inner subtyping to express the constraint. 为什么只实现几乎相同的编码方式呢？重要的是要记住，对于具有内部子类型的通用数组来说，PER 编码始终是一种通用的编码方式（因为子类型的约束并不体现在 PER 编码中）。因此，当使用上述约束条件来实现特殊数组时，所生成的二进制表示会与“通用数组”的对应值相同。而如果明确指定这些约束条件，那么生成的编码方式将会更加紧凑。当这些约束条件适用于所有类型的实现，或者不需要不同类型之间的相互协作时，明确指定这些约束条件显然更为合适。然而，当需要在完整实现和受约束实现之间进行相互协作时，通常建议使用内部子类型来表达这些约束条件。

## 9 Conclusion 9. 结论

"Simple subtyping" can indeed be simple - as when a range is specified for an INTEGER type, but requires care in writing (and a good understanding of the syntax when reading) if the very powerful set arithmetic and inner subtyping features are used. “简单的类型划分”确实可以很简单——比如当为 INTEGER 类型指定一个范围时。不过，在使用那些功能强大的集合运算和内层类型划分特性时，就需要注意书写方式，并且要很好地理解相关语法。

The simplest forms of range and size constraint are very simple to apply, and should be used whenever possible. The more complex forms using set arithmetic or inner subtyping are very powerful, but are for more specialised use. 最简单的范围和大小约束形式非常易于应用，只要有可能就应该使用它们。而使用集合运算或内部类型划分的更复杂形式则更为强大，但只适用于更特殊的场景。

Because in the old Basic Encoding Rules (BER), subtyping never affected the bits on 因为在旧的基本编码规则中，对类型进行划分从来都不会影响那些比特位的值。

the line, there was a tendency for writers of ASN.1 protocols not to bother to think about subtyping, and there are many specifications which, if taken at face value, would require implementations to support indefinite length integers, even 'tho' everybody knows that was never the intention. 在 ASN.1 协议的相关规范中，有些编写者倾向于避免考虑类型划分的问题。有许多规范的规定，如果仅按照字面意思来理解，那么这些规范要求实现能够支持无限长整数的处理，不过众所周知，这从来都不是这些规范的初衷。

Both to give precision to the requirements on implementation, and also because the more recent Packed Encoding Rules will reduce the bits on the line if subtyping is applied, it is now strongly recommended that in producing new or revised protocols, subtyping is applied wherever possible and sensible. This is particularly important for ranges of integers and iterations of SEQUENCE OFs or SET OFs. 为了更准确地满足实施要求，同时因为较新的打包编码规则在应用类型区分后会减少每行中的位数，因此现在强烈建议在处理新的或修订的协议时，尽可能合理地应用类型区分。这一点对于整数范围以及 SEQUENCE OFs 或 SET OFs 的迭代情况尤为重要。

# Chapter 4 Tagging 第四章 标签标注

# (Or: Control it or forget it!) （或者：控制它，或者就放弃吧！）

Summary: Tagging was an important (and difficult!) part of the ASN.1 notation pre-1994. Its importance (and the need to understand it) is much less now, due to three factors: 总结：在 1994 年之前，标签标注是 ASN.1 表示法中的一个重要环节（而且相当复杂）。不过，由于三个原因，现在这一环节的重要性已经大大降低，人们不需要再深入了解它了。

the ability to set an AUTOMATIC TAGS environment in the module header as described in Section I Chapter 3; 能够像第 3 章第一节所描述的那样，在模块头文件中设置自动标签环境；

• the provision for extensibility without relying on tags to achieve this; • 提供了无需依赖标签即可实现扩展性的功能；

• the introduction of PER which does not encode tags. • 引入了不编码标签的 PER 技术。

There are four tag classes: 共有四个标签类别：

• UNIVERSAL • 普适性

• APPLICATION • 应用

• PRIVATE • 私人定制

• context-specific • 特定上下文的

and a tag value is a class and a number (zero upwards, unbounded). 一个标签值由一个类和一个数字组成（数字范围是从 0 开始的，且无上限）。

This chapter describes the requirements on use of tags in a legal piece of ASN.1, and gives stylistic advice on the choice of tag class. 本章阐述了在合法的 ASN1 代码中使用标签的要求，同时提供了关于选择标签类的风格建议。

## 1 Review of earlier discussions 1. 对之前讨论内容的回顾

We have already discussed the idea of including tags, and have introduced the concepts of implicit tagging and explicit tagging, describing these in terms of their effect on a BER encoding: changing the "T" in the TLV for the type (implicit tagging), or adding a new TLV wrapper (explicit tagging). 我们已经讨论过添加标签的想法，并且介绍了隐式标签和显式标签的概念。具体来说，这两种标签方式对 BER 编码的影响如下：改变类型字段中的“T”值（隐式标签方式），或者添加一个新的 TLV 包装器（显式标签方式）。

This is clearly not an academically 这显然并非一种学术上的表达方式。

Tags were originally closely related to the "T" in the "TLV" of the Basic Encoding Rules (BER), and gave users control over the "T" values used for different elements and choices. This was important if interworking between version 1 and version 2 was to be easy in a BER environment with no explicit extensibility marker. 这些标签最初与“基本编码规则”中的“T”字符密切相关。在版本 1 与版本 2 之间实现无缝协作时，这些标签能够让用户灵活地控制用于不同元素和选择的“T”值。这一点在缺乏明确的可扩展性标记的情况下显得尤为重要。

satisfactory way of discussing tagging (but might satisfy many readers!), given that the notation is supposed to be independent of the encoding rules, and that there are now other ASN.1 encoding rules that do not use the "TLV" concept. We will therefore introduce below an encoding-ruleindependent, and slightly more abstract (sorry!), description of tags. 这是一种不错的标签讨论方式（而且应该能吸引许多读者的兴趣！），因为这种表示方式应该是独立于编码规则的。此外，现在还有其他 ASN.1 编码规则，它们并不使用“TLV”这一概念。因此，我们在下面会介绍一种独立于编码规则的描述方式，这种描述方式稍微抽象一些（抱歉！）。

In earlier text we have implied (wrongly!) - but never stated! - that the name-space for tag values is a simple integer. Indeed, we did use a tag "\[APPLICATION 1\]" in figure 21, which might imply a more complex name-space. We describe below the complete set of available values for tags, and the way these are normally used. 在之前的文本中，我们错误地推测——但实际上并没有明确说明——标签值的命名空间实际上只是一个简单的整数。的确，在图 21 中，我们确实使用了标签“\[APPLICATION 1\]”，这可能意味着其命名空间更为复杂。下面我们将详细介绍标签的所有可用值以及这些值的正常使用方式。

Finally, we have already briefly mentioned that there are rules about when tags are required to be distinct (broadly, wherever the "T" of a TLV needs to be distinct from that of some other TLV to ensure unambiguity in BER encodings). We give below the actual rules. 最后，我们已经简要提到了关于何时需要使标签具有区分性的规则（一般来说，当某个 TLV 的“T”需要与其他 TLV 的“T”区分开来，以确保 BER 编码的清晰性时，就需要确保标签是独特的）。下面我们将给出具体的规则。

But as a last important reminder: post-1994 you can establish an automatic tagging environment in which you need know nothing about tags, and need never include them in your type definitions. This is the recommended style to adopt for new specifications, and is absolutely the right approach for anybody who gets confused with the text below! 但最后要提醒一下：自 1994 年之后，你可以创建一个自动标记的环境，在这种环境中，你无需了解任何与标签相关的内容，也无需在类型定义中包含这些标签。这是为新的规范推荐采用的风格，对于任何容易混淆文本内容的人来说，这绝对是正确的做法！

Let us look at the global level for a moment. Wherever ASN.1 requires or allows type-notation, it is permissible to write: 让我们来看看全球范围内的情况。在那些要求或允许使用类型表示法的环境中，我们可以这样书写：

tag-notation type-notation 标签标记 类型标记

In other words, tagging is formally defining a new type from an old type, and tag notation can be repeatedly applied to the same type notation. So the following is legal: 换句话说，标签化实际上是从一个旧的类型中定义一个新的类型，而标签表示法可以反复应用于同一个类型。因此，以下这种用法是合法的：

My-type ::= \[APPLICATION 1\] \[3\] INTEGER 我的类型 ::= \[应用 1\] \[3\] 整数

but would be rather pointless in an environment of implicit tagging, as the "\[3\]" is immediately over-ridden! You will rarely see this sort of construction - tag-notation is normally applied to a type-reference or to untagged type-notation. 但在隐式标签化的环境中，这种表达方式其实没什么意义，因为“\[3\]”这样的标签很快就会被覆盖掉！这种构造方式很少被使用——通常，标签标记是用于类型引用或未标记的类型表示上的。

Finally, if a type is defined using tag-notation, the tag-notation is ignored for the purposes of value-notation. Value notation for My-type above is still simply "6" (for example). 最后，如果某个类型是通过标签符号来定义的，那么在这种情况下，标签符号将被忽略，采用数值表示方式来表示该类型。上面提到的 My-type 类型，其数值表示方式仍然只是简单地写作“6”而已。

## 2 The tag namespace 2 标签命名空间

Staying with BER encodings for the moment: a tag encodes in 7 bits of the "T" part of a BER TLV. 目前，我们仍继续使用 BER 编码方式。在这种编码中，一个标签会用 7 位来表示 BER TLV 中“T”部分的内容。

The remaining bit is nothing to do with tagging, and is set to one if the "V" part is itself a series of TLVs (a constructed encoding such as that used for "SEQUENCE" or "SET"), and 剩下的部分与标签无关，如果“V”部分本身是由一系列 TLV 构成的（这是一种自定义的编码方式，例如用于表示“序列”或“集合”），那么就会设置为 1。

## Tags 标签

• \[UNIVERSAL 29\]: do not use UNIVERSAL class tags. • \[通用类 29\]: 不要使用通用类标签。

• \[APPLICATION 10\]: use for commonly used types or top-level messages. Do not re-use. • \[应用 10\]: 用于常见的类型或顶级消息。请勿重复使用。

\[PRIVATE 0\]: Rarely seen. Use to extend a standard with private additions (if you really must!). \[私有模式 0\]: 较为罕见的使用方式。通常用于对标准模式进行扩展，以加入一些私有的调整（当然，只有在绝对需要的情况下才使用！）

• \[3\]: Use and re-use in a different context. The most common form of tagging. • \[3\]：在不同情境下使用与重用。这是最常见的标签形式。

to zero if the "V" part is not composed of further TLVs (a primitive encoding such as that used for "INTEGER" or "BOOLEAN" or "NULL"). 如果“V”部分并不由更多的 TLV 组成（即是一种简单的编码方式，比如用于“INTEGER”、“BOOLEAN”或“NULL”的编码方式），那么此时该字段的值就为零。

A tag is specified by giving a class and a tag-value (the latter is indeed a simple positive integer - zero upwards, unbounded). But the class is one of four possibilities: 一个标签是通过提供一个类和一个标签值来指定的（后者实际上只是一个简单的正整数——可以为零或更高）。而该类则有四种可能性：

UNIVERSAL class APPLICATION class PRIVATE class context-specific class 通用类 应用程序类 私有类 特定上下文类

<table><tbody><tr><td data-imt-p="1">UNIVERSAL 0 通用 0</td><td data-imt-p="1">Reserved for use by the encoding rules 预留用于编码规则的使用</td></tr><tr><td data-imt-p="1">UNIVERSAL 1 宇宙 1</td><td data-imt-p="1">Boolean type 布尔类型</td></tr><tr><td data-imt-p="1">UNIVERSAL 2 《宇宙 2》</td><td data-imt-p="1">Integer type 整数类型</td></tr><tr><td data-imt-p="1">UNIVERSAL 3 《宇宙 3》</td><td data-imt-p="1">Bitstring type 位串类型</td></tr><tr><td data-imt-p="1">UNIVERSAL 4 通用 4</td><td data-imt-p="1">Octetstring type 八进制字符串类型</td></tr><tr><td data-imt-p="1">UNIVERSAL 5 宇宙之音 5</td><td data-imt-p="1">Null type 空类型</td></tr><tr><td data-imt-p="1">UNIVERSAL 6 通用 6</td><td data-imt-p="1">Object identifier type 对象标识符类型</td></tr><tr><td data-imt-p="1">UNIVERSAL 7 宇宙 7</td><td data-imt-p="1">Object descriptor type 对象描述符类型</td></tr><tr><td data-imt-p="1">UNIVERSAL 8 宇宙 8</td><td data-imt-p="1">External type and Instance-of type 外部类型与实例类型</td></tr><tr><td data-imt-p="1">UNIVERSAL 9 通用 9</td><td data-imt-p="1">Real type 真正的类型</td></tr><tr><td data-imt-p="1">UNIVERSAL 10 通用 10</td><td data-imt-p="1">Enumerated type 枚举类型</td></tr><tr><td data-imt-p="1">UNIVERSAL 11 通用 11</td><td data-imt-p="1">Embedded-pdv type 嵌入式 PDV 型</td></tr><tr><td data-imt-p="1">UNIVERSAL 12 通用 12</td><td data-imt-p="1">UTF8String type UTF8String 类型</td></tr><tr><td data-imt-p="1">UNIVERSAL 13 - 15 宇宙系列 13 - 15</td><td data-imt-p="1">Reserved for future editions of this Recommendation | International Standard 预留用于本建议书的未来版本 | 国际标准</td></tr><tr><td data-imt-p="1">UNIVERSAL 16 通用 16</td><td data-imt-p="1">Sequence and Sequence-of types 序列与类型序列</td></tr><tr><td data-imt-p="1">UNIVERSAL 17 宇宙 17</td><td data-imt-p="1">Set and Set-of types 集合类型与集合类型集合</td></tr><tr><td data-imt-p="1">UNIVERSAL 18-22 通用版 18-22</td><td data-imt-p="1">Character string types 字符字符串类型</td></tr><tr><td data-imt-p="1">UNIVERSAL 23-24 普世性 23-24</td><td data-imt-p="1">Time types 时间类型</td></tr><tr><td data-imt-p="1">UNIVERSAL 35-30 通用版 35-30</td><td data-imt-p="1">More character string types 更多的字符字符串类型</td></tr><tr><td data-imt-p="1">UNIVERSAL 31-... 通用 31-…</td><td data-imt-p="1">Reserved for addenda to this Recommendation | International Standard 预留用于本建议书的补充内容｜国际标准</td></tr></tbody></table>

Figure II-7: Assignment of UNIVERSAL class tags 图 II-7：通用类标签的分配情况

In the tag notation, a number alone in square brackets denotes the tag-value of a context-specific class tag. For the other classes, the name (all upper-case) of the class appears after the opening square bracket. 在标签表示法中，仅一个数字放在方括号中就能表示某个上下文特定的类标签及其值。对于其他类，类的名称（全部大写）则出现在第一个方括号之后。

For example: 例如：

```txt
[UNIVERSAL 29] tag-value 29, "universal" class
[APPLICATION 10] tag-value 10, "application" class
[PRIVATE 0] tag-value 0, "private" class
[3] tag-value 3, "context-specific" class 
```

I like to think of the four classes of tag as just different "colours" of tag (red, green, blue, yellow). The actual names do not matter. For most purposes, the "colour" of the tag does not matter either! All that matters is that tags be distinct where so required, and they can differ either in their "colour" (class) or in their tag-value. The colour you choose to use is mainly a matter of style. 我喜欢将这四种标签类别视为不同的“颜色”——红色、绿色、蓝色、黄色。这些名称本身并不重要。在大多数情况下，标签的“颜色”也并不重要！重要的是，标签要具有区分性，并且它们可以在“颜色”或标签值上进行区分。你选择使用的颜色主要是出于风格考虑而已。

There is only one hard prohibition: users are not allowed to tag types with a UNIVERSAL class tag. This class is (always) used for the "default tag" on a type, and values of such tags can only be assigned within the ASN.1 specification itself. 只有一条严格禁止的规定：用户不得使用“UNIVERSAL”类标签来标记类型。这个类始终用于标记类型的“默认标签”，而此类标签的值只能定义在 ASN.1 规范本身中。

Figure II-7 is a copy of a table from X.680/ISO 8824-1 (including all amendments up to September 1998), and gives the UNIVERSAL class tag assigned as the default tag (used unless overridden by implicit tagging) for each of the type notations and constructor mechanisms defined in ASN.1. 图 II-7 是 X.680/ISO 8824-1 标准的表格副本（包含截至 1998 年 9 月的所有修订内容）。该图表列出了在 ASN 中定义的每种类型标记和构造机制所默认的通用类标签。除非有明确的标签规定，否则将使用这些默认的标签。

The main reason for forbidding use of UNIVERSAL class tags by users is to avoid problems when future extensions to ASN.1 occur. It is, however, important to note that this is no real hardship, as every tag has equal status with every other tag, no matter what its "colour" (class). 禁止用户使用通用类标签的主要原因是避免在未来对 ASN 进行扩展时产生问题。不过，需要注意的是，这实际上并不算什么大问题，因为无论某个标签的“类别”如何，它与其他标签一样，都具有同等的重要性。

There have been specifications that conformed to pre-1994 ASN.1, but wanted to use UTF8String (added 1998), and decided to copy the text of the post-1994 definition into their own application specification. This is probably harmless, but is strictly in violation of the specification. As well as being illegal, it is also unnecessary to copy the text and to assign a UNIVERSAL class tag in the copied text - an APPLICATION class tag can be used in the definition of the type, and provided the type is implicitly tagged wherever it is used, the end-result is indistinguishable from an initial assignment with a UNIVERSAL class tag, as later implicit tagging will override either. 有一些规范遵循了 1994 年之前的 ASN1 标准。不过，他们希望使用 UTF8String 这个类型（该类型是在 1998 年添加的），因此决定将 1994 年之后的定义内容复制到他们自己的应用规范中。这或许并无大碍，但实际上这违反了规范的规定。此外，复制定义内容并为其分配一个“通用类标签”也是不必要的——在类型定义中可以使用“应用类标签”。只要类型在使用的任何地方都自动带有标签，那么最终的结果与最初使用“通用类标签”进行标记并无区别，因为后续的隐式标记会覆盖掉“通用类标签”的标记。

So what about the other three classes of tag? Which one should be used when? To repeat: they are all equivalent. Use PRIVATE class tags absolutely everywhere if you wish! But as a matter of style, most people use context-specific class tags most of the time (they are the easiest to write - just a number in square brackets!). The name "context-specific" implies that they are only unambiguous within some specific context (typically within a single SEQUENCE, SET, or CHOICE), and it is normal to use (and to re-use) these tags (from zero upwards) whenever you need to tag the alternatives of a CHOICE or the elements of a SEQUENCE or SET to conform to the rules requiring distinct tags in particular places (see below). 那么，其他三种类别的标签又该如何使用呢？在什么时候应该使用哪一种标签呢？再次强调：这三种标签都是等效的。如果你愿意，完全可以随时随地使用“私有”类别标签！不过从风格上来说，大多数人通常都会使用与上下文相关的标签（因为这样更容易编写——只需在方括号中填入一个数字即可）。所谓“与上下文相关的标签”，意味着这些标签只在特定上下文内具有明确的含义（通常是在某个序列、集合或选择项中）。因此，当你需要为选择项的选项或序列、集合中的元素添加标签时，通常会使用这些标签（可以反复使用），以符合某些地方对特定标签的严格要求（详见下文）。

It is also common practice (but by no means universal nor required) to use APPLICATION class tags in the following way: 通常的做法是（不过这并非普遍现象，也不一定是必需的）以以下方式使用 APPLICATION 类标签：

• An application class tag is only used once in the entire application specification, it is never applied twice. • 在整个应用程序规范中，应用类标签只会被使用一次，绝不会重复使用。

If the outer-most type for the application is a CHOICE (it usually is), then each of the alternatives of that choice are tagged (implicitly if possible) with APPLICATION class tags (usually \[APPLICATION 0\], \[APPLICATION 1\], \[APPLICATION 2\], etc). We saw this approach in Figure 21 of Section I Chapter 3. 如果应用程序的最外层类型是一个 CHOICE 类型（通常都是这样），那么该选择中的每个选项都会被附加上 APPLICATION 类标签（如果可能的话，这些标签会自动添加，通常是\[APPLICATION 0\]、\[APPLICATION 1\]、\[APPLICATION 2\]等）。我们在第 3 章第 1 节的图 21 中看到了这种处理方式。

If there are some complex types that are defined once and then used in many parts of the application specification, then when they are defined they are given an application class tag (and this tag is never given to anything else), so they can be safely used in a choice (for example) with no danger of a violation of any rules requiring distinct tags (unless the identical type appears again in the CHOICE - presumably with different semantic). 如果有一些复杂的类型，它们只被定义一次，但在整个应用程序的多个地方被使用，那么在这些类型被定义时，会赋予它们一个“应用程序类标签”。而这个标签永远不会被用于其他任何对象。因此，可以放心地在选择结构中使用这些类型，而不必担心违反那些要求使用不同标签的规则——除非在选择结构中再次出现同一个类型，而且这次的语义与之前不同。

An example of this might be the types "OutletType" and "Address" in Figures 13 and 14 of Section I Chapters 3 and 4. So in Figure 14 we might write instead: 例如，在第三章和第四章的第一部分的图 13 和图 14 中出现的“OutletType”和“Address”这类字段。因此，在图 14 中，我们可以这样书写：

$$
\begin{array}{l} \text {OutletType}: := [ \text {APPLICATION 10} ] \text {SEQUENCE} \\ \{\dots . \\ \dots . \\ \dots . \} \\ \text {Address}: := [ \text {APPLICATION 11} ] \text {SEQUENCE} \\ \{\dots . \\ \dots . \\ \dots . \} \end{array}
$$

taking the decision to use application class tags 0 to 9 for top-level messages, and 10 onwards for commonly-used types. 决定对顶级消息使用应用类标签 0 到 9，而对于常用类型则使用 10 作为起始值。

There is no limit to the magnitude of a tag-value, but when we examine BER in Section III, we will see that a "T" will encode in a single octet provided the tag-value to be encoded is less than or equal to 30, so most application designers usually try to use tag-values below 31 for all their tags. (But there are specifications with tag values in the low hundreds) 标签值的长度没有限制，但在第 III 部分中我们会看到，如果待编码的标签值小于或等于 30，那么用一个“T”字符就可以表示它。因此，大多数应用程序设计者通常会尽量使用不超过 31 的标签值来标识各种标签。（不过，也有一些规范要求使用低至几百的标签值）

PRIVATE class tags are never used in standardised specifications. They have been used by some multi-nationals that have extended an international standard by adding extra elements at the end of some sequences or sets. The assumption here (as with most jiggery-pokery with tags) is that BER is being used, and the (reasonable) hope is that by adding new elements with PRIVATE class tags, these will not clash with any extension of the base standard in the future. 在标准化的规范中，从不使用“私有类标签”。不过，一些跨国公司采用了这种标签方式，他们在某些序列或集合的末尾添加了额外的元素，从而扩展了国际标准。这里的假设是正在使用 BER 标准；而希望是，通过添加带有“私有类标签”的新元素，这些元素在未来不会与基础标准的任何扩展部分产生冲突。

## 3 An abstract model of tagging 3. 标签的抽象模型

Note: This material is not present in the ASN.1 specification. It is considered by this author to be a useful model to provide an encoding-ruleindependent description of the meaning of tagging at the notational level, and a means of specifying the behaviour of encoding rules. Most ASN.1 "experts" would probably accept the model, but might argue that it is not needed, and is only one 注意：这一内容并未出现在 ASN.1 规范中。作者认为，这一模型有助于提供一种与编码规则无关的标记含义描述方式，同时也能帮助指定编码规则的行为。大多数 ASN.1“专家”可能会接受这一模型，但也可能认为它并非绝对必要，它只是一种……

We can model tagging as affecting a tag-list associated with every ASN.1 abstract value. Some encoding rules use some or all of the tags in the tag-list as part of the encoding. 我们可以将标签的添加建模为影响每个 ASN.1 抽象值所对应的标签列表。某些编码规则会使用标签列表中的部分或所有标签作为编码的一部分。

of several possible ways of modelling what the ASN.1 notation is specifying, in order to link it cleanly to encoding rules. (See Figure 999 again!). 有几种不同的方式可以建模 ASN.1 符号所指定的内容，以便将其清晰地与编码规则联系起来。（请再次参考图 999！）

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/a0059080-59e4-4cd9-913b-34e7587e39f7/8e5aa554d9f8bbc0a5500031f64ed60a8508594e0621251e2fd952320dbfd62a.jpg)

In order to provide a means of describing the effects of tagging we introduce a model of ASN.1 abstract values (the "things" that are in ASN.1 types) which involves some structure to these values. This is shown in figure II-8. 为了描述标记效果的描述方式，我们引入了一个关于 ASN.1 抽象值的模型。这些抽象值代表了 ASN.1 类型中的对象。这种结构在图 II-8 中有所展示。

In figure II-8 we see that each ASN.1 abstract value is made up of a basic-value (like "integer 1", "boolean true", etc), together with an ordered tag-list consisting of one or more tags (an innermost, closest to the basic-value, and an outermost, furthest away). Each tag consists of, as described earlier, a class and a tag-value. 在图 II-8 中，我们可以看到每个 ASN.1 抽象值都由一个基本值（如“整数 1”、“布尔值 true”等）以及一个有序的标签列表组成。这个标签列表包含一个或多个标签，这些标签按照从内到外、从基本值向外的顺序排列。如前所述，每个标签由一个类和一个标签值组成。

When a type is defined using ASN.1 type-notation such as "BOOLEAN" or "INTEGER", or as the result of using notation such as SEQUENCE or SET, all its values are given the same tag-list - a single tag (which is both innermost and outermost) of the UNIVERSAL class. The tag-value for each type notation is specified in the ASN.1 specification, and repeated in figure II-7 above. (We have referred to this as the "default tag" for the type in earlier text). 当使用 ASN.1 类型表示法来定义一个类型时，例如“BOOLEAN”或“INTEGER”，或者通过 SEQUENCE 或 SET 等表示法定义时，该类型的所有值都会具有相同的标签列表——即 UNIVERSAL 类中的单个标签。每个类型表示的标签值在 ASN.1 规范中有明确的规定，并在上面的图 II-7 中重复列出。（在之前的文本中，我们将其称为该类型的“默认标签”。）

There are only two operations that are possible on a tag-list. If a type is implicitly tagged, then the outer-most tag is replaced by the new tag specified in the tagging construction. If a type is explicitly tagged, then a new outer-most tag is added to the tag list. Note that all ASN.1 abstract values always have at least one tag. They acquire additional tags by explicit tagging, and can never have the number of tags reduced. 在标签列表中，只有两种操作是可行的。如果某个类型被隐式标记了，那么最外层的标签会被替换为在标记构造中指定的新标签。如果某个类型被显式标记了，那么会在标签列表中添加一个新的最外层标签。注意，所有 ASN.1 抽象值至少都有一个标签。通过显式标记，这些抽象值还可以获得额外的标签，而且它们的标签数量永远无法减少。

With this model of tagging, we can now define our Basic Encoding Rules as encoding a "TLV" for each tag in the tag-list, from the outermost to the innermost tag, where the tag forms the "T", the "L" identifies the length of the remainder of the encoding of the ASN.1 abstract value, and each "V" apart from the last contains (only) the next TLV. The last "V" contains an encoding identifying the basic value. 通过这种标签编码方式，我们现在可以定义基本编码规则：对于标签列表中的每个标签，从最外层的标签开始，依次进行编码。其中，标签部分构成“T”字形结构；“L”表示 ASN.1 抽象值的剩余部分需要编码的长度；除了最后一个“V”之外，每个“V”仅包含下一个 TLV 的编码信息。最后一个“V”则包含用于标识基本值的编码。

The reader will recognise that this gives exactly the same encoding as was obtained when we described explicit tagging as "adding an extra layer of TLV", but the use of the abstract model makes it unnecessary to describe the meaning of the notation in encoding rule terms. We use the concept of a tag-list as a sort of indirection between the notation and the encoding rules. It represents information which an ASN.1 tool will normally need to retain between syntax analysis and other functions. 读者会注意到，这种编码方式与我们之前将显式标签描述为“增加一层 TLV”时所使用的编码方式是完全相同的。不过，由于使用了抽象模型，因此无需用编码规则来详细说明这种符号的含义。我们将标签列表的概念视为一种间接表达方式，它代表了那些在语法分析和其他功能之间需要被保留的信息。

Finally, but very importantly, note that for most types, all the values in the type have exactly the same tag-list. If we apply further tagging to the type, we will change the tag-list (add a new tag or replace the outer-level tag) for each and every value in that type. 最后，但同样重要的是，需要注意的是，对于大多数类型来说，该类型中的所有值都具有完全相同的标签列表。如果我们对类型进行进一步的标签标注，那么就会改变该类型中每个值的标签列表——要么添加新的标签，要么修改外部级别的标签。

Moreover, for many purposes (in particular what tag values are permitted) all that matters is the outer-most tag. It is thus meaningful to talk about "the tag of the type", because every abstract value of that type has the same tag-list (and hence the same outer-level tag). There is, however, one exception to this simple situation. 此外，对于许多情况来说（尤其是关于允许使用哪些标签值的问题），真正重要的只是最外层的标签。因此，谈论“类型的标签”是有意义的，因为该类型中的每一个抽象值都具有相同的标签列表，从而也具有相同的外层标签。不过，这种情况也有一个例外。

The CHOICE constructor is modelled as forming a new type whose values are the union of the set of values in each of the alternatives, with each value retaining its original tag-list. Thus for the choice types, it is not meaningful to talk about "the tag of the type", as different abstract values in the type have different tag-lists. (It is important to remember this if you see text in canonical encoding rules saying "the elements are sorted into tag-order" - look for some qualifying text to cover the case of a choice type!) CHOICE 构造体被建模为一种新型类型，其取值是各个选项所提供的值的集合。每个值都保留其原始的标签列表。因此，对于选择类型来说，谈论“类型的标签”是没有意义的，因为类型中的不同抽象值拥有不同的标签列表。（如果你在规范编码规则中看到类似“元素按标签顺序排序”这样的描述，请记住这一点——需要找到相关的说明来涵盖选择类型的情况！）

Suppose, however, that a choice type is explicitly tagged (the only form of tagging allowed for choice types). Then whilst the tag-list on different abstract values may (will) still differ, the outermost tag is the same for all abstract values in the type, and the explicitly tagged choice is just like any ordinary type - every abstract value has the same outer-level tag and we can talk about this as "the tag of the type". 不过，假设某个选择类型被明确标记了（这是允许对选择类型进行标记的唯一方式）。那么，虽然不同抽象值的标签可能有所不同，但所有抽象类型的最外层标签都是相同的。而被明确标记的选择类型，其实与普通类型并无区别——每个抽象值都具有相同的外层标签，我们可以将其称为“类型的标签”。

So we can now recognise that most types have a single associated tag (the common outer-level tag for all abstract values of that type), that we can call "the tag of the type", but that an untagged choice type has many tags associated with it (all the outer-level tags of any of its values). If none of the alternatives of this choice are themselves choices, then the number of outer-level tags (all distinct) associated with this choice type will be equal to the number of its alternatives. If, however, some alternatives are themselves choice types, they will each bring to the table multiple (distinct) outer-level tags, and the outer-level choice type will have more (distinct) tags associated with it than it has alternatives. 现在我们可以认识到，大多数类型都只有一个关联的标签（这个标签是所有该类型抽象值的共同外层标签），我们可以称之为“该类型的标签”。但是，如果一个无标签的选择类型有多个关联标签，那么它与之相关的外层标签数量就会等于该选择类型所拥有的替代选项的数量。不过，如果某些替代选项本身也是选择类型，那么这些选项就会各自带来多个不同的外层标签。这样一来，这个外层选择类型所关联的标签数量就会超过其替代选项的数量。

For example, if: 例如，如果：

$$
\begin{array}{l} \text {My - choice}:: := \text {CHOICE} \\ \left\{\text {alt1} \quad \text {CHOICE} \right. \\ \left. \begin{array}{l} \left\{\text {alt1 - 1} [ 0 ] \text {INTEGER}, \right. \\ \text {alt1 - 2} [ 1 ] \text {INTEGER} \}, \\ \text {alt2} [ 2 ] \text {EXPLICIT My - choice2} \end{array} \right\} \end{array}
$$

then the tags associated with "My-choice" are context-specific zero, one, and two. Any tags in "My-choice2" are hidden by the explicit tagging. 那么，与“My-choice”相关的标签就是那些具有上下文特定性的零、一和二。而“My-choice2”中的任何标签则会被显式标记隐藏起来。

With this concept of "the tag of the type", or rather "the tags associated with the type" (which are always distinct), we can go on to discuss the rules for when distinct tags are required. 通过“该类型的标签”这一概念，或者更确切地说“与该类型相关的标签”（这些标签总是相互独立的），我们可以继续讨论何时需要使用不同的标签的规则。

# 4 The rules for when tags are required to be distinct 4. 确定何时需要使标签区分开来的规则

The rule is that distinct tags are required: 规则是必须使用不同的标签：

When do we need distinct tags? 我们什么时候需要使用不同的标签呢？

• for the alternatives of a CHOICE; • 对于“选择”这一选项的不同可能性；

• for the elements of a SET; and • 对于集合中的元素；以及

• for consecutive DEFAULT or OPTIONAL elements and any following mandatory element in a SEQUENCE. • 适用于连续出现的“默认”或“可选”元素，以及随后出现的任何强制性元素，这些元素必须按顺序排列。

There - its simple really, isn't it? (Skip the rest!) 很简单，对吧？（剩下的部分就不用多说了！）

The rules given below (and in the ASN.1 specification) are expressed in terms of tag uniqueness, but are most easily remembered if you know that they are the minimum necessary rules to enable a TLV-style of encoding to be unambiguous! Alternatively, just remember the rules and forget the rationale! 以下列出的规则（在 ASN.1 规范中也有描述）都是基于标签唯一性的原则来制定的。不过，如果你知道这些规则是使 TLV 式编码具有明确性的最低要求，那么这些规则就很容易记住了！或者，你也可以只记住这些规则，而忽略其背后的原理吧！

Within a CHOICE constructor, the collection of tags brought to the table by each alternative have all to be distinct. (Remember, each alternative brings just one tag to the table - the common outerlevel tag of the tag-list of its abstract values, unless it is an untagged choice type, when it brings to the table at least one tag for each alternative of the choice type, but these are all distinct.) 在 CHOICE 构造体中，每个选项所携带的标签都必须是不同的。（记住，每个选项只携带一个标签——即其抽象值的标签列表的通用外层标签。除非是未标记的选项类型，在这种情况下，每个选项至少会携带一个标签，但这些标签都是不同的。）

Similarly, within a SET constructor, the tags of all the elements have to be distinct, with any elements that are choice types again potentially contributing several distinct tags to the matching process. 同样，在 SET 构造器中，所有元素的标签也必须各不相同。而那些属于可选类型的元素，同样可能会在匹配过程中产生多个不同的标签。

Within a SEQUENCE constructor, the rules are a little more complicated. In the absence of DEFAULT or OPTIONAL, there are no requirements for distinct tags on the elements of a sequence type. However, in the presence of DEFAULT or OPTIONAL, the situation changes slightly: for any block of successive elements marked DEFAULT or OPTIONAL, together with the next mandatory element, if any, the tags of all elements in that block are required to be distinct. 在 SEQUENCE 构造器中，规则会稍微复杂一些。在没有 DEFAULT 或 OPTIONAL 的情况下，序列类型中的元素不需要使用不同的标签。然而，在存在 DEFAULT 或 OPTIONAL 的情况下，情况会略有变化：对于任何被标记为 DEFAULT 或 OPTIONAL 的连续元素组，加上下一个必填元素（如果有的话），那么该组中所有元素的标签都必须是不同的。

You will want to think about that for a moment. Clearly the block of DEFAULT or OPTIONAL elements must all have distinct tags, or (in BER) the receiver won't know which are present and which missing, but equally, if one of those tags matched the next mandatory element there could again be confusion. By requiring that the following mandatory element has a tag distinct from any element of the preceding block, then the appearance of that tag in an encoding gives complete knowledge that the block of OPTIONAL or DEFAULT elements is complete, and processing of the remainder of the sequence elements can proceed in a normal manner. 你可能需要花一点时间思考这个问题。显然，所有属于“默认”或“可选”元素的块都必须具有独特的标签。否则，接收方将无法判断哪些元素存在，哪些不存在。同样地，如果某个标签与下一个必填元素匹配，同样会导致混淆。因此，要求下一个必填元素具有与前一个块中任何元素都不同的标签，这样在编码中该标签的出现就能确保“可选”或“默认”元素的完整性，而其余元素的处理就可以正常进行了。

There is only one small additional complication if you are trying to control your tags without using automatic tagging. That is an interaction between the extensibility marker and the rules for distinct tags, in circumstances where there are multiple extension markers within a sequence (for example, one on a choice element in the sequence and one at the end of the sequence). The purpose of the rules here is to ensure that if a version 2 specification adds elements, a version 1 system receiving those elements will be in no doubt (with BER – there is never a problem with PER!) about whether the version 2 specification (of which, of course, it has no knowledge!) had extended the choice element or added further elements to the sequence. (This can matter if different exception handling had been specified in version 1 in the two cases.) For details of these additional requirements see the discussion in the next chapter on Extensibility. 如果你试图在不使用自动标记功能的情况下控制标签，那么就会有一个小问题需要解决。这个问题源于可扩展标记器和不同标签的规则之间的相互作用，尤其是在序列中同时存在多个可扩展标记器的情况下（例如，序列中的一个选择元素上有一个可扩展标记器，而序列的末尾还有一个可扩展标记器）。这些规则的目的是确保，当版本 2 的规范添加了新元素时，接收这些元素的版本 1 系统能够明确判断出，版本 2 的规范是否扩展了选择元素，或者向序列中添加了其他元素。这一点非常重要，因为如果在版本 1 中规定了两种不同的异常处理方式，那么这种情况就尤为重要。有关这些额外要求的详细信息，请参见下一章关于可扩展性的讨论。

For those of a philosophical bent, you may wish to ponder how much simpler these rules could have been if (in BER, which really dictated the rules) all CHOICE constructions had automatically produced a TLV wrapper with a default tag (say UNIVERSAL 15), in the same way as SEQUENCE! Anybody using this book as an academic text might want to set that question as an exercise for the better students! Please note that whilst PER does not have a TLV philosophy, it does none-the-less have explicit encoding associated with CHOICE, which BER does not. One day some-one will invent the perfect encoding rule philosophy! 对于喜欢哲学思考的人来说，你们可能会想：如果这些规则在 BER 中就能得到制定，那么情况会简单得多。因为在 BER 中，所有的 CHOICE 构造都会自动生成一个 TLV 包装器，并且默认使用某个标签（比如 UNIVERSAL 15）。这种方式与 SEQUENCE 的方式类似。任何将这本书作为学术教材的人，都可以把这个问题作为一道练习题来教给优秀的学生！请注意，虽然 PER 并没有像 TLV 那样明确的编码规则，但它对 CHOICE 确实有明确的编码规范，而 BER 则没有这样的规范。总有一天，会有人发明出完美的编码规则哲学吧！

## 5 Automatic tagging 5. 自动标签功能

## This clause is solely for implementors! 这一条款完全是为实施者设计的！

What tags are applied in an "automatic tagging" environment? First, if anyh piece of SET, SEQUENCE or CHOICE notation contains a textually present tag on any of its outer-level elements or alternatives, automatic tagging is disabled for the outer-level of that notation. Otherwise, tags \[0\], \[1\], \[2\], etc. are successively applied to each element or alternative in an environment of implicit tagging. (So elements/alternatives that are CHOICE types get explicitly tagged and all other elements get implicitly tagged.) 在“自动标记”环境中，会应用哪些标签呢？首先，如果某个 SET、SEQUENCE 或 CHOICE 类型的声明在其任何外层元素或选项中包含有文本形式的标签，那么该声明的外层部分就不会被进行自动标记。否则，标签\[0\]\[1\]\[2\]等会依次应用于环境中的所有元素或选项。（也就是说，属于 CHOICE 类型的元素会被明确标记，而其余元素则会被隐式标记。）

## 6 Conclusion 6 结论

Tagging appears complex, but once understood is a relatively simple matter. In early specifications it became common, as a matter of style, to simply tag all elements of SEQUENCEs and SETs and alternatives of CHOICEs with context-specific (implicit) tags from zero upwards (avoiding the word "IMPLICIT" if the type being tagged was itself a CHOICE). 虽然标签的使用看起来比较复杂，但一旦理解了其原理，其实就变得相当简单了。在早期的规定中，出于风格考虑，通常会对所有序列、集合以及选择项的各个元素加上与上下文相关的（隐式的）标签。如果被标记的元素本身也是一个选择项，那么就会避免使用“隐式”这个词。

With the introduction of an "implicit tagging" environment, this became somewhat easier, but if this is desired, it is essentially what automatic tagging provides. 随着“隐性标签标注”环境的引入，这种情况变得稍微容易了一些。不过，如果确实需要这种功能，那么自动标签标注恰恰能够满足这一需求。

There are few specifications where the minimum necessary tagging is used. Writers of ASN.1 protocols tend to be more "symmetric" (or lazy?) than a minimalist approach would require. 在少数几个规范中，只使用了最基本的标签标注。ASN.1 协议的编写者往往更倾向于采用“对称”的思维方式（或者说比较懒散的方法），而不是遵循极简主义的设计原则。

It is the firm recommendation of this author that all new modules be produced with automatic tagging, and for tags to be forgotten about! 这位作者强烈建议，所有新的模块都应配备自动标签功能，而且这些标签应该被彻底遗忘！

# Chapter 5 Extensibility, Exceptions, and Version Brackets 第五章 扩展性、异常处理以及版本标签

# (Or: There is always more to learn!) （或者可以说：总是有更多的东西可以学习！）

## Summary: This chapter: 摘要：这一章的内容是：

describes the "extensibility" concept of interworking between version 1 systems and later version 2 systems; 描述了版本 1 系统与后续版本 2 系统之间互操作的“扩展性”概念；

explains the need for an "extension marker" to indicate where version 2 additions might occur; 解释了需要一种“扩展标记”来指示版本 2 的新增内容可能出现的位置；

• describes all the places where an extension marker is permitted; • 描述了所有允许设置扩展标志的位置；

• explains the need for defined exception handling when an extension marker is used; • 说明了在使用扩展标记时，需要明确指定异常处理方式的必要性；

• describes the notation for "version brackets" to group together elements added in later versions; and • 描述了用于将后续版本中添加的元素组合在一起的“版本括号”标记方式；以及

• describes the interaction between extensibility and the requirements for distinct tags. • 描述了可扩展性与不同标签需求之间的相互作用关系。

Presence in appropriate places of the extension marker is key to use of the Packed Encoding Rules (PER) which generate encodings approximately 50% the size of those produced by the Basic Encoding Rules (BER). 在适当的位置放置扩展标记是使用“打包编码规则”的关键。与“基本编码规则”所生成的编码相比，打包编码规则生成的编码大小大约小了 50%。

Writers of ASN.1-based protocols are very strongly encouraged to include extension markers (with defined exception handling) in their version 1 specifications in order to minimise problems in the future. 强烈建议基于 ASN.1 协议的编写者在他们的版本 1 规范中引入扩展标记（同时需对异常情况做好处理措施），以尽量减少未来可能出现的问题。

## 1 The extensibility concept 1 可扩展性概念

NOTE — In this chapter, the acronyms BER (Basic Encoding Rules) and PER (Packed Encoding Rules) are used without further explanation. 注意：在本章中，缩写术语 BER（基本编码规则）和 PER（打包编码规则）无需进一步解释即可使用。

What is "extensibility"? "Extensibility" refers to a combination of notational support, constraints on encoding rules, and 什么是“可扩展性”？“可扩展性”指的是一种符号支持体系、对编码规则的限制以及其他相关方面的组合。

You wrote your specification three years ago, there are many fielded implementations - success! But you want to make additions. How do you migrate? What will version 1 systems do with your additions? ASN.1 extensibility gives you control. 您在三年前就已经编写了规范文档，目前已经有许多实现方案被采用——这很成功！不过，您希望进行一些补充。该如何进行迁移呢？版本 1 的系统在引入这些补充功能后会有什么变化呢？ASN.1 的可扩展特性让您可以掌控整个流程。

implementation rules. This support enables a protocol specified (and implemented) as version 1 to be upgraded some years later to version 2 in specifically permitted ways. Provided the version 2 extensions are within the permitted set of extensions (and provided the version 1 protocol was marked as "extensible"), then there will be a good interworking capability between the new version 2 systems and the already-deployed and unmodified version 1 systems. 实施规则。这种支持使得按照版本 1 的规定制定并实施的协议，可以在特定许可的情况下，在几年后升级为版本 2。只要版本 2 的扩展功能属于允许的扩展功能范围（并且版本 1 的协议被标记为“可扩展”），那么新的版本 2 系统与已部署且未修改的版本 1 系统之间将具备良好的互操作性。

The keys to extensibility are: 可扩展性的关键在于：

To ensure that version 2 additions or extensions are "wrapped up" with length counts in encodings, and can be clearly identified by version 1 systems as "foreign material". 为了确保版本 2 的添加或扩展内容能够在编码中通过长度统计信息进行标识，并且能够被版本 1 的系统明确识别为“外来内容”，这一点非常重要。

• To provide a clear specification that version 1 systems should process the parts of the encoding that are not "foreign material" in the normal version 1 way, and should take defined and predictable actions with the "foreign material". • 需要提供一个明确的规范，规定版本 1 的系统应以常规版本 1 的方式处理不属于“外来物质”的编码部分，并且对于“外来物质”部分应采取明确且可预测的处理方式。

• To avoid unnecessary (and verbose) wrappers and identifications in encodings by using notational "flags" on where version 2 additions or extensions may need to be made. • 通过使用表示“标志”来标记需要添加或扩展功能的区域，可以避免在编码中出现不必要的、冗长的封装和标识操作。

For the extensibility concept to be successful, all three of these components must be present. 要使可扩展性的概念能够成功实施，这三个要素都必须同时存在。

A detailed discussion of possible exception handling actions is given in Section I Chapter 7. 关于可能的异常处理措施的详细讨论，请参见第 7 章的第 1 节。

With the BER encoding rules, all fields have a tag and a length associated with them, covering the first point above, but producing the verbosity we want to avoid in the third point. BER itself says nothing about point 2. Some forward-thinking application designers did include text such as: "Within a SEQUENCE or SET, implementations should ignore any TLV which has a tag that is not what is expected in their version", but this was by no means universal, and it was in general not possible to specify different action on "foreign material" in different parts of the protocol. With the PER encoding rules, length wrappers are often missing, and tags are always missing. PER has to be told where to insert length wrappers and to encode presence or absence of version 2 material if extensibility is to be achieved without undue cost. This is the primary purpose of the "extension marker". 根据 BER 编码规则，所有字段都带有标签和长度信息，这满足了上述第一个要求。不过，这样的描述过于冗长，这正是我们想要避免的情况。BER 本身并没有对第二点做出任何规定。一些具有前瞻性的应用设计者确实加入了类似这样的说明：“在序列或集合中，实现方应忽略那些标签不符合他们版本要求的元素”。不过，这种做法并非普遍适用，而且通常无法在协议中为不同的“外部元素”指定不同的处理方式。而根据 PER 编码规则，往往不需要使用长度标签，同时也不需要明确标注是否包含第二版本的要素。为了实现可扩展性，同时又不造成不必要的成本负担，就必须明确如何插入长度标签，以及如何表示是否包含第二版本的要素。这就是“扩展标记”的主要作用。

## 2 The extension marker 2. 扩展标记器

What does the extension marker look like? We have already encountered it in Figure 21 and Figure 22 of Section I Chapters 3 and 4. It is the ellipsis (three dots) following the "sales" alternative in line 26 of Figure 21, and following the "sales-data" element in Figure 22. 那个扩展标记是什么样子的呢？我们已经在第一节第 3 章和第 4 章的图 21 和图 22 中遇到过它。图 21 第 26 行中“sales”选项后面的三个点符号，以及图 22 中“sales-data”元素后面的部分，都是这种扩展标记的表现形式。

Look out for the three little dots. Put them in as often as you like, they cost you little on the line. (Zero in BER, one bit in PER). 注意那三个小点。你可以根据需要随时将它们放置进去，它们带来的收益非常有限。（在 BER 中占 0 点，在 PER 中占 1 点）

If the reader now refers to Figure II-3 in Chapter 3, we see another element being added after the extension marker in the "Wineco-protocol" CHOICE of Figure 21. This is our version 2 addition. 如果读者现在参考第 3 章中的图 II-3，会看到在图 21 中“Wineco 协议”选项中的扩展标记之后，又增加了一个元素。这就是我们的版本 2 的新增内容。

(Note that an ellipsis is also used following "WITH COMPONENTS {". This is a separate use of three dots, pre-dating the extensibility work, and should not be confused with extensibility.) （请注意，在“WITH COMPONENTS {”之后也使用了省略号。这其实是另一种用法，与可扩展性功能不同，不应将其与可扩展性功能混淆。）

## 3 The exception specification 3 例外情况的规定

It is strongly recommended that all uses of extensibility be accompanied by an exception specification, unless the same exception handling is specified for the entire application. 强烈建议在所有使用扩展性的情况下都附带一个异常规范，除非整个应用程序都采用了相同的异常处理机制。

The exception specification makes clear what implementors of version 1 systems are supposed to 该例外规定明确指出了第 1 版系统的实现者应当遵循的行为规范。

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/a0059080-59e4-4cd9-913b-34e7587e39f7/3ba760c910562416911ec4e92ce2432e69323649a5a24d10df630d536d241448.jpg)

do with "foreign material" in this position in the message (as in Figures 21 and 22), but this recommendation is not universally followed at this time. 在消息中，这个位置使用了“外国材料”这个词（如图 21 和 22 所示），不过目前这一建议并没有被普遍遵循。

The syntax of the exception specification (which can appear immediately after any ellipsis which indicates extensibility) is either an integer value, or the name of any ASN.1 type followed by a colon followed by a value of that type. Typical examples would be: 异常指定的语法格式（可以出现在表示可扩展性的任何省略号之后）要么是一个整数值，要么是一个 ASN.1 类型的名称，后面跟着一个冒号，再后面跟着该类型的一个值。典型的例子如：

The first two might be used where there are a list of numbered exception handling procedures, and would identify which to apply in each position of added material. The third might be used where exceptions always give error reports, and the value is just the text for the error report. The final example might be used where "My-Type" has been defined as a SEQUENCE with the first element an enumeration of possible actions (for example, "abort", "returnError", "ignore", "treatAsMaximum" and the second (optional) element as a character string qualifying those actions. Note that "treatAsMaximum" might be an appropriate exception handling procedure for an ellipsis that was within a constraint, whilst "Ignore" is clearly only applicable to added material in a SEQUENCE or SET. For an unexpected CHOICE alternative, "returnError" might be desired. ASN.1 provides the notational tools, but only the application designer can decide how to use them appropriately. (For more discussion, see Section I Chapter 7.) 前两个选项适用于那些包含一系列编号的异常处理程序的场景，它们可以明确指出在添加何种内容时应该应用相应的处理程序。第三个选项适用于那些总是会生成错误报告的异常情况，此时所提供的值只是错误报告的文本。最后一个选项适用于“My-Type”被定义为一个序列的情况，该序列的第一个元素为可能的操作枚举（例如“abort”、“returnError”、“ignore”、“treatAsMaximum”），第二个元素则是一个字符串，用于描述这些操作的具体细节。需要注意的是，“treatAsMaximum”可能是适用于符合特定约束条件的省略情况的异常处理程序，而“Ignore”则显然只适用于出现在序列或集合中的添加内容。对于意外的情况，可能需要使用“returnError”来处理。1 提供了符号工具，但如何正确使用这些工具则取决于应用程序的设计者。（更多讨论请参见第 I 部分第 7 节。）

## 4 Where can the ellipsis be placed? 4. 省略号应该放在哪里呢？

In the first ASN.1 extensibility specification, ellipses could be placed (and extensions added serially after them) as follows (illustrations in Figure II-9 give the version 1 text followed by the version 2 text): 在第一个 ASN.1 扩展性规范中，可以放置省略号（并且可以在这些省略号之后连续添加更多的扩展项）。如图 II-9 所示，版本 1 的文本之后就是版本 2 的文本：

• At the end of any SEQUENCE or SET or CHOICE (see figures 21 and II-3). • 在任何序列、集合或选择题中，在每一部分的末尾处（参见图 21 和图 II-3）。

• Wherever there is a constraint (see figure II-9). • 在任何存在限制条件的地方（参见图 II-9）。

• At the end of the list of enumerations in an ENUMERATED type (see figure II-9). • 在 ENUMERATED 类型的枚举列表中末尾（参见图 II-9）。

```txt
INTEGER (0..255, ... ) or INTEGER (0..255, ... !1)
INTEGER (0..255, ..., 0..65535) INTEGER (0..255, ... !1, 0..65535)
ENUMERATED {red, blue, green, ... }
ENUMERATED {red, blue, green, ..., purple}
Figure II-9: Illustrations of extensibility marker use 
```

An early addendum to the ASN.1 extensibility specification allowed the insertion point for new material in a SEQUENCE, SET or CHOICE (but nowhere else) to be not just at the end, but in the middle. This was flagged by the use of two ellipsis elements as shown in Figure II-10. Again we have included the exception specification to remind implementors that the handling of foreign material at this position is specified in clause 50 of the application specification. 在 ASN.1 可扩展性规范的早期修订中，允许在 SEQUENCE、SET 或 CHOICE 结构中，新元素的插入点不再仅限于末尾位置，也可以位于中间。这一修改是通过使用两个省略号来表示的，如图 II-10 所示。此外，我们还添加了例外说明，以提醒实现者：此类情况下对外部元素的处理方式应在应用规范的第 50 条中进行规定。

```txt
SEQUENCE
{field1 TypeA,
    field2 TypeB,
    ... ! PrintableString : "See clause 50",
    -- Version 2 material goes here.
    ...
    field3 TypeC}
Figure II-10: An insertion point between elements 2 and 3 
```

## 5 Version brackets 5. 版本区间

The same addendum introduced version brackets, with an opening bracket of a pair of "\[\[" and a closing bracket of "\]\]". These were introduced to reduce the number of length wrappers needed at any given insertion point to the minimum necessary - one wrapper for each new version, 同样的附加规则引入了版本括号的表示方式，即开始使用一个“\[”字符作为开始括号，结尾使用“\]”字符作为结束括号。这样设计是为了将每个新版本所需的包装次数减少到最低限度——每个新版本只需要一个包装。

Version brackets not only save bits on the line but provide a historical record of the additions that have been made to the protocol. 版本标签不仅节省了行数，还记录了协议中发生的所有修改历史。

and also because application designers felt they would like to be able to identify for historical purposes what was in version 1, version 2, version 3, etc. With extensions for versions 2 and 3, the above sequence could look like figure II-11. 此外，应用程序设计师们也希望能够记录下各个版本的具体内容，以便将来进行历史参考。对于版本 2 和版本 3 来说，这样的序列可以像图 II-11 所示。

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
    ... ,
    -- The following is version 1 material.
    field3 TypeC}
Figure II-11: An insertion point with two version additions 
```

It should be noted that extensibility can be identified independently for each SEQUENCE, SET and CHOICE, even if these constructs are nested within other extensible constructs. However, within any one such construct there can be at most one insertion point at the outer level of that construct, with material being successively added at the insertion point after any already inserted material. 需要注意的是，可扩展性可以独立地为每个序列、集合和选择结构进行定义，即使这些结构嵌套在其他可扩展结构中。然而，在任何一个这样的结构中，外部层面最多只能有一个插入点，而数据则会在该插入点之后依次被添加进去。

Version brackets should normally be employed even if there is only one element added, to provide a clear documentation of the revision history. 即使只添加了一个元素，也应该使用版本标签来清晰地记录修改的历史。

Note also that version brackets can only be inserted in SEQUENCE, SET, and CHOICE constructs, not in ENUMERATED or constraints. 请注意，版本区间只能用于 SEQUENCE、SET 和 CHOICE 类型的数据结构，而不适用于 ENUMERATED 类型或约束条件。

At the time of writing this book (mid-1999), there are a number of published specifications that have inserted extension markers, and some that contain added material and version brackets. 在撰写这本书时（1999 年中期），已经有一些公开的规范文件中包含了扩展标记，还有一些文件则增加了额外的内容和版本说明。

## 6 The {...} notation 6 这种 {...} 表示法

You will encounter what appears to be an extensible empty "table constraint" (see later) in a number of specifications. This relates to the use of Information Object Classes, and discussion of it is deferred until Chapter 7 of this Section. 在许多规范中，你会遇到一种看似可扩展的“表约束”机制（详见后文）。这一机制与信息对象类的使用有关，其相关讨论将推迟到本部分的第 7 章进行。

## 7 Interaction between extensibility and tagging 7. 可扩展性与标签化之间的相互作用

When tagging was discussed in the previous chapter, it was noted that extensibility gave rise to some further requirements on the distinctness of tags. 在上一章中讨论标签时，人们指出可扩展性带来了一些关于标签唯一性的额外要求。

These requirements arise because if there are several extension markers in an ASN.1 type, they may have different exception specifications associated with them, and it is therefore important for version 1 systems to be able to unambiguously associate "foreign" material with a specific insertion point and hence exception specification. 这些要求的存在是因为，在 ASN.1 类型中，如果存在多个扩展标记，那么它们可能具有不同的异常规范。因此，对于版本 1 的系统来说，能够明确地将“外部”元素与特定的插入点以及相应的异常规范关联起来是非常重要的。

NOTE — Explanations given in this text may be hard to understand without a clear understanding of the BER encoding rules. Readers that are progressing sequentially through this book should either just accept that there are further rules on tagging that are "ad hoc" and curious, or else read the text on BER and return to this section. Sorry! I can do no better! 注意：如果不清楚 BER 编码规则的话，那么本文中的解释可能会难以理解。那些按照顺序阅读本书的读者，要么接受存在一些“临时性”且令人困惑的标签规则，要么阅读有关 BER 的章节后再回到这一部分。抱歉！我无法给出更好的解释了！

It is fortunate (as PER does not encode tags) that there are no problems in this area with a PER encoding. However, with BER, constructions like the following give real problems: 幸运的是（因为 PER 并不对标签进行编码），在 PER 编码方式下不会出现相关问题。不过，对于 BER 编码方式来说，以下几种构造方式确实会带来实际问题：

$$
\begin{array}{l} \text {Example1}: := \text {SEQUENCE} \\ \quad \{\text {field1 CHOICE} \\ \quad \{\text {alt1 INTEGER,} \\ \quad \dots ! 1 \} \text {OPTIONAL,} \\ \quad \dots ! 2 \} \end{array}
$$

or 或

Example2 ::= CHOICE {alt2 CHOICE {alt3 INTEGER, ...!3 }, ...!4} 示例 2：= 选择列表 {alt2 选择列表 {alt3 整数，...!3}，...!4}

Now suppose that in version 2 additions are made at the insertion points with exception handling !1 or !2. If "field1" had not been optional it would have been easy - presence of foreign material before the presence of "alt1" is clearly a !1 case, and after it a !2 case. But with field1 being optional, there is no way for version1 systems to determine whether we have new material at !1, or !1 being missing and new material at !2. A similar problem arises with new material at !3 or !4. 现在假设在版本 2 中，插入点处进行了添加操作，同时包含了异常处理机制！1 或！2。如果“field1”不是可选的，那么情况就很简单了——在“alt1”出现之前出现外来物质，显然属于！1 的情况；而在“alt1”出现之后出现外来物质，则属于！2 的情况。但是，由于 field1 是可选的，因此版本 1 的系统无法判断是在！1 位置有新的物质，还是在！2 位置有新的物质。类似的问题也出现在！3 或！4 位置有新的物质的情况。

Note that the problem is not with the tag on any added material, the problem is fundamental to the use of extensibility in these constructs. 需要注意的是，问题并不在于任何附加材料上的标签，而在于这种结构在利用扩展性功能时的根本性问题。

Unless BER were to be changed (shrieks of horror - BER long precedes extensibility!) it is necessary to make the two above (and other similar) constructs illegal. How to do that? 除非改变 BER 的设定（惊恐的尖叫——BER 的存在早已决定了其不可扩展的特性！），否则就必须禁止上述这两种以及类似的结构。那么，该如何实现这一点呢？

The ASN.1 Specification adopts a slightly curious approach. It says that wherever there is an extension marker, you should add (at the end of any existing extensions) a "conceptual element" whose tag matches that of no other element except other "conceptual element"s. Then you apply rules about when distinct tags are required, and if they are satisfied, you are legal (and there will be no problems for a version 1 system to unambiguously assign foreign material to a single insertion point). ASN.1 规范采用了一种略显奇特的命名方式。该规范规定，每当出现扩展标记时，都需要在现有扩展的末尾添加一个“概念元素”标签，且该元素的标签必须是独一无二的，没有其他“概念元素”与之重复。接着，会制定关于何时需要使用不同标签的规则；如果这些规则得到满足，那么这种命名方式就是合法的（对于版本 1 的系统来说，将外部材料分配到单个插入点并不会产生任何问题）。

In the first of the above cases, addition of the conceptual element in the !1 position means that "field1" brings to the table both the INTEGER tag and the tag of the conceptual element. The latter clashes with the tag of the following (mandatory) conceptual element in the !2 position, so the construction is illegal. 在上述第一种情况中，将概念元素添加到!1 位置意味着“field1”同时包含了 INTEGER 标签和该概念元素的标签。而后者会与下一个（强制性的）概念元素的标签产生冲突，因此这种构造方式是无效的。

In the second of the above cases, "alt2" brings to the table the tag of the conceptual element (as well as the INTEGER tag), which again clashes with the tag of the conceptual element in the extension !4. So again we have illegality. 在上述第二个案例中，“alt2”标签包含了概念元素的标签（以及 INTEGER 标签），这再次与扩展版本！4 中的概念元素标签产生了冲突。因此，这里同样存在合法性问题。

(Please refer to Figure 999 again!) It is important to note here that this is a distinct complexity with extensibility. Having given earlier advice that you should use AUTOMATIC TAGS, and then forget about tagging, I am now saying (and the ASN.1 Specification is saying) that in order to determine whether some extensibility constructions are legal or not requires that you have a fairly sophisticated understanding of tagging. Of course, if you use a tool such as that provided by OSS to check your ASN.1, it will instantly tell you that you have broken the rules, although whether you will understand the error message in these cases is more questionable! （请再次参考图 999！）需要注意的是，这里所讨论的复杂性具有可扩展性。之前我们建议大家使用自动标签机制，但之后又建议放弃使用标签。现在我要说（根据 ASN.1 规范），要判断某些可扩展构造是否合法，就需要对标签机制有相当深入的理解。当然，如果你使用 OSS 提供的工具来检查你的 ASN.1 文件，它会立即提示你违反了规则。不过，在这种情况下，你是否能够理解错误提示的内容则值得怀疑！

## So .... we need some simple advice: 那么……我们需要一些简单的建议：

• If a CHOICE is OPTIONAL in some SEQUENCE, make sure it is not the last element before an extension marker, or make sure it is not itself extensible. (And don't follow it by another extensible CHOICE!) • 如果某个选项在某个序列中是可选的，请确保它不是扩展标记之前的最后一个元素，或者确保它本身并非可扩展的选项。（并且，不要在其之后再出现另一个可扩展的选项！）

• If a CHOICE is in a SET, make sure that only one of the CHOICE and the SET are extensible. • 如果某个选项属于某个集合，请确保该选项本身以及该集合都是可扩展的。

• Never put an extensible CHOICE in another extensible CHOICE. • 永远不要将一个可扩展的选择置于另一个可扩展的选择之中。

In summary, treat extensible CHOICEs like radio-active material - keep them well apart, and clearly separated from other extension markers! If you do that, there will never be any problems. 总结来说，对待可扩展的 CHOICE 元素就像对待放射性物质一样——把它们分开放置，并且与其他扩展标记明确区分开来！只要做到这一点，就不会有任何问题了。

These rules really are ad hoc, but they are simple to apply, and will eliminate the problems described above. 这些规则确实是临时制定的，但它们很容易实施，并且能够解决上述提到的问题。

Of course, if you break these rules, you are writing de jure illegal ASN.1, and a good tool will tell you so, and probably refuse to encode it! But if you encode it yourself .... well, problems only arise in practice if you have different exception handling on the various extensions. Just keep the above points in mind, and you should be OK. 当然，如果你违反这些规则，那么你编写的就是法律上讲是非法使用的 ASN1 代码。一个好的工具会提示你这一点，并且可能会拒绝进行编码！但如果你自己进行编码的话……那么只有在处理不同扩展时采用不同的异常处理方式时，才会出现问题。只要记住上述要点，应该就不会有麻烦了。

## 8 Concluding remarks 8. 总结性发言

We have described the extension marker and its association with the exception specification, and the complications arising from BER, which give rise to the need to produce some complex rules on when apparently innocuous extension markers are illegal. 我们已经描述了扩展标记及其与异常规范的关联，以及由 BER 引起的各种复杂情况。这些情况使得有必要制定一些复杂的规则，以确定那些看似无害的扩展标记何时会变得非法。

Finally, it is important to note that the interworking that extensibility provides between version 1 and version 2 systems is dependent on the extension marker being present in version 1, and in changes being made to the protocol only as permitted by the extensibility provisions (addition of elements, alternatives, enumerations, at the insertion point, and relaxation of constraints). 最后，需要指出的是，版本 1 和版本 2 系统之间所提供的是扩展性带来的互操作能力，这一能力取决于版本 1 中是否存在扩展标记。而协议上的修改则只能在扩展性规定的范围内进行——比如在插入点添加元素、引入替代方案、增加枚举项，或者放宽某些约束条件。

If changes are made to a specification that are not covered by the extensibility provisions (such as random insertion of new elements), then the encodings of that new version are likely to produce unpredictable effects if sent to a version 1 system. Similarly, insertion of an extensibility marker in version 2 which was not present in version 1 means that encodings of the version 2 material will produce unpredictable effects if sent to version 1 systems. 如果某个规范发生了超出可扩展性的修改（比如随机插入新的元素），那么当将这些新版本的编码发送给版本 1 的系统时，很可能会产生不可预测的效果。同样，如果在版本 2 中加入了原本不存在的可扩展性标记，那么当将这些版本 2 的编码发送给版本 1 的系统时，同样会产生不可预测的效果。

The unpredictability described above may be simply between "Will they abort in some way or will they ignore the apparent error?", but could be "With encodings of some version 2 values version 1 systems will think they are correct encodings of totally unrelated version 1 values" and will act accordingly, which could be very dangerous. So it is generally important to prevent encodings of version 2 types that do not obey the extensibility rules from being sent to version 1 systems. This can, of course, be done in many ways, the most common being some form of version negotiation when a connection is first established. 上述不可预测性可能仅仅表现为“系统会以某种方式放弃处理，还是会忽略这个明显的错误？”这样的问题。但实际上，它可能是“在某些版本 2 的编码下，版本 1 的系统会误以为这些编码是正确的，从而采取相应的行动，这可能会非常危险”。因此，通常重要的是要防止那些不遵守可扩展性的版本 2 编码被发送到版本 1 的系统中。当然，这可以通过多种方式来实现，最常见的方法就是在连接建立时进行某种形式的版本协商。

Extensibility and exception handling are powerful tools, and enable highly optimised encoding rules to be used. They are safe if the rules governing their use are obeyed. 可扩展性和异常处理是非常强大的工具，它们使得能够使用高度优化的编码规则。只要遵守相关的使用规则，这些工具就是安全的。

It is, however, very important to insert extension markers fairly liberally into version 1 specifications (or to use the EXTENSIBILITY IMPLIED notation). 不过，非常重要的是要在版本 1 的规范中大量使用扩展标记（或者使用“可扩展性隐含标记”）。

# Chapter 6 Information Object Classes, Constraints, and Parameterization 第六章 信息对象类、约束条件与参数化

## (Or: Completing the incomplete - with precision) （或者：完成那些不完整的事物——以精确的方式）

## Summary: 总结：

This chapter: 这一章：

• provides a brief description of the concept of "holes" in protocols; • 简要描述了协议中“漏洞”这一概念的含义；

describes briefly the ROSE (Remote Operations Service Element) protocol in order to provide a specific example of the need to define types with "holes" in them, and the need for notation to support clear specifications in the presence of "holes"; 简要介绍了 ROSE（远程操作服务元素）协议。通过这一例子，说明了在存在“空洞”的情况下，定义带有“空洞”的类型是多么重要，以及使用特定符号来明确说明这些空洞的需求。

provides a clear statement of the Information Object, Information Object Class, and Information Object Set concepts, and the use of those Object Sets to complete a partial protocol specification by constraining "holes" (and the consistency relationships for filling in multiple holes) left in a carrier protocol. 该文档清晰地阐述了信息对象、信息对象类别以及信息对象集的概念。同时，还介绍了如何利用这些对象集来完善部分协议规范，从而填补在载体协议中存在的“漏洞”——以及用于填充这些漏洞的一致性关系。

It goes on to describe: 文中继续描述如下：

the syntax for defining an Information Object Class, Information Objects, and Information Object Sets, using a development of the wineco protocol as examples; 以 wineco 协议的发展为例，介绍了用于定义信息对象类、信息对象以及信息对象集的语法规则；

the means by which defined Information Object Sets can be related to the "holes" that they are intended to constrain, using a simplified version of the ROSE protocol as an example; 以一种简化的 ROSE 协议为例，介绍了如何将特定的信息对象集与它们旨在解决的“漏洞”联系起来。

• describes the need for parameterization, and the parameterization syntax of ASN.1 specifications. • 描述了参数化的需求，以及 ASN.1 规范中参数化的语法规则。

It is supposed to be bad practice to tell a student that "what I am about to say is difficult"! But the information object concepts are among the more conceptually difficult parts of ASN.1, and we will introduce these concepts gently in this chapter and fill in final details in the next chapter. Just skip-read this chapter if it is all too easy! 告诉学生“我接下来要说的内容比较难理解”是一种不好的做法！不过，在 ASN.1 中，信息对象概念属于较为抽象的部分。我们在本章会循序渐进地介绍这些概念，而最后的细节则会在下一章中详细说明。如果觉得本章的内容太简单了，可以直接跳过吧！

# 1 The need for "holes" and notational support for them 1. 需要为这些“洞”提供相应的标注和支持。

## 1.1 OSI Layering 1.1 OSI 模型层次结构

This is probably the first time in this book that Open Systems Interconnection (OSI) has been seriously discussed, although it was within the OSI stable that ASN.1 was first standardised. 这可能是本书中首次正式讨论开放系统互连标准（OSI）。不过，ASN.1 标准其实是在 OSI 标准体系内首次被标准化的。

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/a0059080-59e4-4cd9-913b-34e7587e39f7/ab65f9c3f11e42a7381c3436c02843a72d5e56689fa6c25ea3cb99bd66840a69.jpg)

OSI was perhaps the first protocol suite specification to take seriously the question of documenting its architecture, with the production of the OSI 7-layer model. Many vendor-specific protocols had some concept of layering, and the TCP/IP work had split off IP from TCP in the late 1970s, but the OSI model was the most complete attempt at describing the concept of layering. OSI 可能是第一个真正重视架构文档化的协议标准，它提出了 OSI 七层模型。虽然许多特定于供应商的协议也包含了分层的概念，而在 20 世纪 70 年代末，TCP/IP 协议将 IP 从 TCP 中分离出来。但 OSI 模型才是描述分层概念最完整的尝试。

The 7-layer model was (in 1984) just the latest attempt to try to produce a simplification of the (quite difficult) task of specifying how computers would communicate, by dividing the task into a number of separate pieces of specification with well-defined links between those pieces of specification. 这个七层模型是在 1984 年提出的，它试图将原本复杂且难以处理的计算机通信规范工作简化为一系列独立的规范，这些规范之间有着明确的联系。不过，这一尝试仍然只是当前最先进的解决方案而已。

Although this "architecture" was primarily aimed at making it possible for several groups to work on different parts of the specification simultaneously, an important off-shoot was to provide reusability of pieces of specification. This included re-usability of network specifications to carry many different applications over the same network, or re-usability of application specifications to run over many different network technologies, some of which may not have been invented when the application specification was first written. 虽然这种“架构”的主要目的是为了让多个团队能够同时处理规范的各个部分，但另一个重要的成果是实现了规范的复用性。这意味着网络规范可以被重复使用，以便在同一个网络上承载多种不同的应用；同时，应用规范也可以被复用，从而在多种不同的网络技术环境下运行，其中一些技术可能在编写应用规范时尚未被发明出来。

The reader should contrast this with the early so-called "link" protocols (mainly deployed in the military arena, but also in telephony), where a single monolithic specification (document) completely and absolutely defined everything from application semantics to electrical signalling. 读者可以将这种情况与早期的所谓“连接协议”进行对比。这些协议主要应用于军事领域，但也用于电话通信领域。在那种情况下，整个规范（文档）都试图对从应用程序语义到电气信号传输等所有方面进行完全的定义。

In the International Standards Organization (ISO) 7- layer model, each layer provided a partial specification of messages that were being transmitted, each message having a "hole" in it (called user-data) that carried the bit-patterns of the messages defined by the next higher layer. However, there was a "fan-out" and "fan-in" situation: many possible lower layers (for example, transport or network protocols) could be used to carry any given higher-layer messages, and any given transport (or network) could carry many different higherlayer messages. It was a very flexible many-to-many situation. 在国际标准化组织（ISO）的七层模型体系中，每一层都对传输的消息进行了部分规范描述。每一条消息中都包含一个“空洞”，其中包含了由上一层定义的消息的位模式。不过，存在“发向下层”和“接收来自上层”的情况：许多可能的下层协议（例如传输层或网络协议）都可以用来承载某一特定高层消息；而任何一个传输层或网络层也可以承载多种不同高层消息。这是一种非常灵活的多对多关系。

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/a0059080-59e4-4cd9-913b-34e7587e39f7/b4138b9fe609cd5a9def681198432579878f7d5284286a6a59dcbe62f098cc36.jpg)

But the basic concept in the original ISO OSI model was that every application layer specification would fill in the final hole - each application layer standard would produce a complete specification for some application. 但在原始的 ISO OSI 模型中，基本的概念是：每个应用层规范都会填补最终的空白——每个应用层标准都会为某种应用提供完整的规范。

It was the CCITT 7-layer model (eventually adopted by ISO) that brought to the table the concept of partial specifications of "useful tools" in the application layer, recognising a potentially infinite set of layers, each filling in a "hole" in the layer beneath, but itself leaving "holes" for other groups to fill in due course. 正是 CCITT 的七层模型（后来被 ISO 采纳）提出了“有用工具”在应用层中的部分规范这一概念。该模型认识到，可能存在无限多的层次结构，每个层次都填补了下层层次中的空白，而同时这些层次本身也会留下空白，以便其他组在后续阶段来填充这些空白。

As ASN.1 increasingly became the notation of choice for defining application specifications, there clearly became a need for support in ASN.1 for "holes". 随着 ASN.1 逐渐成为定义应用规范的首选标记语言，显然需要为 ASN.1 中的“空洞”情况提供相应的支持。

## 1.2 Hole support in ASN.1 1.2 ASN.1 中的孔支撑结构

Forget about theoretical models for now. It rapidly became clear that people writing application specifications using ASN.1 in 1984 wanted to be able to write a "generic" or "carrier" specification, with "holes" left in their datatypes, with other groups (multiple, independent, groups) providing specifications for what filled the holes. 现在先不要考虑理论模型了。很快便明白，1984 年那些使用 ASN.1 编写应用规范的人，其实想要编写一个“通用”或“载体”规范——这种规范会在数据类型中留下一些空白，然后由其他小组（多个、独立的小组）来负责填补这些空白。

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/a0059080-59e4-4cd9-913b-34e7587e39f7/3d1443e66bcc5b68e9aea1b13de248457a68e9633c2cec888ef90a8d5502dee6.jpg)

At this point it is important to recognise that "leaving some things left undefined, for others to define", can (most obviously) be an undefined part of the format of messages (the user-data in OSI layering), or one of the elements in an ASN.1 sequence, but can also be an undefined part of the procedures for conducting a computer exchange. Both types of "holes" have occurred in real specifications, and notation is needed to identify clearly the presence and nature of any "holes" in a specification, together with notation for "user" specifiers to fill in the "holes". 在这一点上，重要的是要认识到：“让一些内容保持不明确状态，由其他用户来定义”，这可以是消息格式中的一个不明确部分（在 OSI 层次结构中指的是用户数据），也可以是 ASN.1 序列中的一个元素。不过，这也可能属于进行计算机交换过程中的一些不明确步骤。实际上，这两种“漏洞”都曾出现在真实的规范中，因此需要一种标记方式来明确标识规范中存在的“漏洞”及其性质，同时还需要一种标记方式来指导“用户”如何填充这些“漏洞”。

There is one other important point: if several different (user) groups provide specifications for applications which fit in the holes of some carrier or generic protocol, it often happens that implementations wish to support several of these user specifications, and need to be able to determine at communication-time precisely which specification has been used to fill in the hole in a given instance of communication. This is rather like the "protocol id" concept in a layered architecture. We recognise the need for holes to carry not just some encoding of information for the user specification, but also an identification of that specification. 还有一个重要的问题：如果多个不同的用户群体为适合某些载体或通用协议的应用程序提供了规范，那么通常会出现这样一种情况，即各种实现都希望支持这些用户规范，并且需要在通信过程中准确确定在特定的通信实例中使用了哪种规范来填补其中的空白。这有点类似于分层架构中的“协议标识”概念。我们认为，这些“空白”不仅需要包含用户规范的信息编码，还需要包含该规范的标识信息。

The earliest ASN.1 support for "holes" was with the notation "ANY", which (subject to a lot of controversy!) was withdrawn in 1994, along with the "macro notation" which was an early and largely unsuccessful attempt to relate material defining the contents of a hole (for a particular application) to a specific hole occurrence (in a carrier specification). 最早对“空洞”进行 ASN.1 编码的规范是“ANY”这种表示法。不过，这种表示法在 1994 年被取消了，因为它引发了不少争议。此外，还有“宏表示法”这一尝试，它试图将定义某个空洞内容的材料与特定空洞的出现情况联系起来，但这一尝试最终并未取得成功。

In 1994, the ASN.1 "Information Object Class" and related concepts matured, as the preferred way of handling "holes". In this chapter we next introduce the concepts of ROSE (Remote Operations Service Element), showing how ROSE had the need for notation to let its users complete the holes left in the ROSE protocol. We then briefly describe the nature of the information that has to be supplied when a user of the ROSE specification produces a complete application specification. We then proceed to the concepts associated with ASN.1 "Information Object Classes". 在 1994 年，ASN.1 的“信息对象类”及相关概念逐渐成熟，这成为了处理“空缺”问题的首选方式。在本章中，我们将介绍 ROSE（远程操作服务元素）的概念，说明 ROSE 需要使用特定的表示方式来填补协议中存在的空白。接着，我们简要描述了当用户使用 ROSE 规范编写完整的应用程序规范时，需要提供的信息内容。最后，我们将讨论与 ASN.1“信息对象类”相关的概念。

## 2 The ROSE invocation model 2 玫瑰式调用模型

## 2.1 Introduction 2.1 引言

One of the earliest users of the ASN.1 notation was the ROSE (Remote Operations Service Element) specification - originally 最早使用 ASN.1 标记语言的技术之一，是 ROSE（远程操作服务元素）规范——最初是由……提出的。

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/a0059080-59e4-4cd9-913b-34e7587e39f7/884bc2966c5486dd2e3e45021bf79a680dfc07546052a06d8237ee959f1f6473.jpg)

just called ROS (Remote Operations Service). This still provides one of the easiest to understand examples of the use of the Information Object Class concept, and a little time is taken here to introduce ROSE. 其实，这个系统被称为 ROS（远程操作服务）。这仍然是一个比较容易理解的、关于信息对象类概念应用的例子。这里花一点时间来介绍 ROSE 系统。

The reader should, however, note that this treatment of ROSE is NOT complete, and that when tables of information are introduced, the latest version of ROSE has many more columns than are described below. There have been a number of specifications that have written their own version of ROSE, with some simplifications and/or with some extensions, so if you see text using "OPERATION" or "ERROR", check where these names are being imported from. They may be imported from the actual ROSE specification, or they may be a ROSE "look-alike". The definitions in this text are a ROSE "look-alike" - they are a simplification of the actual ROSE definitions. 不过，读者需要注意的是，对 ROSE 的处理并不完整。当引入表格信息时，最新版本的 ROSE 包含的比下面的描述要多得多列。有一些规范编写了自己的 ROSE 版本，其中包含了一些简化或扩展的内容。因此，如果看到使用“操作”或“错误”的术语，请检查这些名称是从哪里引入的。它们可能是直接来自 ROSE 规范，也可能是类似 ROSE 的替代定义。本文中的定义就是这种类似 ROSE 的替代定义——它们实际上是 ROSE 定义的一种简化版本。

A common approach to the specification of protocols by a number of standardization groups (of which the latest is CORBA) is to introduce the concept of one system invoking an operation (or method, or activating an interface) on a remote system. This requires some form of message (defined in ASN.1 in the case of ROSE) to carry details for the operation being invoked, the three most important elements being: 许多标准化组织在协议规范制定时采用的一种常见方法（最新的例子是 CORBA）是引入“一个系统调用远程系统的操作”这一概念。这需要使用某种消息来传递调用的详细信息，其中三个最重要的元素包括：

• some identification of this invocation, so that any returned results or errors can be associated with the invocation; and • 需要对该调用进行一定的标识，这样就能将任何返回的结果或错误与特定的调用关联起来；此外……

• some identification of the operation to be performed; and • 需要明确要执行的操作的具体内容；此外……

• the value of some ASN.1 type (specific to that operation) which will carry all the arguments or input parameters for the operation. • 某些 ASN 类型的值（特定于该操作）。这些值将包含该操作所需的所有参数或输入参数。

This is called the ROSE INVOKE message (defined as an ASN.1 type called "Invoke"). ROSE introduced the concept of the "invocation identification" because it recognised that multiple instances of (perhaps the same) operation might be launched before the results of earlier ones had come back, and indeed that results might not come back in the same order as the order operations where launched in. 这种消息被称为 ROSE 调用消息（定义为一种 ASN.1 类型，名为“Invoke”）。ROSE 引入了“调用标识”的概念，因为它认识到，在之前的操作结果返回之前，可能会启动多个相同的操作实例。实际上，这些操作的结果可能不会按照启动操作的顺序来返回。

It is important here to note that the ROSE specification will define the concepts, and the form of the invocation message, but that lots of other groups will independently assign values to identify operations, define the ASN.1 type to carry the arguments or input parameters, and specify the associated semantics. They need a notation to do this, and to be able to link such definitions clearly to the holes left in the ASN.1 definition of the ROSE INVOKE message. 这里需要指出的是，ROSE 规范会定义相关的概念以及调用消息的格式。不过，许多其他团队会自行为各种操作分配数值，定义用于承载参数或输入参数的 ASN.1 类型，并指定相关的语义。他们需要一种 notations 来表述这些细节，同时还能将这些定义清晰地与 ROSE INVOKE 消息在 ASN.1 定义中留下的空白处联系起来。

Used in this context, ASN.1 is being used as what is sometimes called an "Interface Definition Language" (IDL), but it is important to remember that ASN.1 is not restricted to such use and can be applied to protocol definition where there is no concept of remote invocations and return of results. 在这一上下文中，ASN.1 被用作一种所谓的“接口定义语言”。不过需要注意的是，ASN.1 并不局限于这种用途，它也可以用于定义那些没有远程调用和结果返回概念的协议。

The INVOKE message itself is not a complete ASN.1 type definition. It has a "hole" which can carry whatever ASN.1 type is eventually used to carry values of the arguments of an operation. This "hole", and the value of the operation code field in the INVOKE message, clearly have to be filled-in in a consistent manner - that is, the op-code and the type must match. INVOKE 消息本身并不是一个完整的 ASN.1 类型定义。它有一个“空位”，这个空位可以容纳任何将来用于存储操作参数值的 ASN.1 类型。这个“空位”，以及 INVOKE 消息中操作码字段的值，都必须以一致的方式被填充——也就是说，操作码的类型必须与所存储的值的类型相匹配。

## 2.2 Responding to the INVOKE message 2.2 回应 INVOKE 消息

The ROSE concept says that an INVOKE message may be responded to by a REJECT message, carrying operation-independent error indications, such as "operation not implemented" (strictly, "invokeunrecognisedOperation"), "system busy" (strictly, ROSE 概念指出，一个 INVOKE 消息可能会收到一个 REJECT 响应，该响应会携带与操作无关的错误信息，例如“操作未执行”（严格来说是“invokeunrecognisedOperation”）、“系统繁忙”等。

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/a0059080-59e4-4cd9-913b-34e7587e39f7/7839cf5734f932a021f0b37d2108707a703c4ccd8f7d09586cffaad530086ebb.jpg)

"resourceLimitation"), etc). ROSE has about 40 different error or problem cases that can be notified with a REJECT message. （例如“资源限制”等情况）。ROSE 系统大约有 40 种不同的错误或问题情况，这些情况可以通过发送 REJECT 消息来通知用户。

If, however, there is no such message, then the operation is successfully invoked and will result in an "intended result" (the RESULT message) or an operation-dependent "error response" (the ERROR message). 不过，如果不存在这样的消息，那么操作就会成功执行，并会产生一个“预期结果”（即 RESULT 消息），或者一个与操作相关的“错误响应”（即 ERROR 消息）。

ROSE invocation is illustrated in figure II-12. 在图 II-12 中展示了 ROSE 的调用过程。

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/a0059080-59e4-4cd9-913b-34e7587e39f7/0e2a77f5ec84bbf97569e41efa219f4798c9d8c3111a743af53b96308225da4a.jpg)

This separation of "intended result" and "error response" is not strictly necessary, but simplifies the ASN.1 definition. The assumption here is that any one group will be defining a number of closely-related operations, each of which will have an identification and precisely one ASN.1 type to carry the input arguments in the INVOKE message hole, and precisely one ASN.1 type to carry the output arguments in the RESULT message hole. However, for this complete set of operations, there are likely to be a set of possible error returns, such that any given operation can give rise to a specified subset of these errors. For each error we need an error code, and an ASN.1 type to carry additional information (which ROSE calls parameters) about the error, and of course we need to be able to specify which errors can arise from which operations. 将“预期结果”与“错误响应”分开并不是绝对必要的，但这有助于简化 ASN.1 的定义。这里的假设是，每个组都会定义一系列密切相关的操作，每个操作都有一个标识符，并且有一个特定的 ASN.1 类型用于携带 INVOKE 消息中的输入参数，同时还有一个特定的 ASN.1 类型用于携带 RESULT 消息中的输出参数。不过，对于这一系列操作来说，可能会存在多种可能的错误返回情况，因此任何操作都可能引发某些特定的错误。对于每种错误，我们需要一个错误代码，以及一个 ASN.1 类型来携带关于该错误的额外信息（ROSE 称之为参数）。当然，我们还需要能够指定哪些操作可能会引发哪些错误。

## 3 The use of tables to complete the user specification 3. 使用表格来整理用户需求说明

We return here to our wineco protocol, and will first use an informal tabular format to show how we use the ROSE (incomplete) protocol to support our wineco exchanges. We have already specified two main messages using ASN.1, namely 我们接下来将继续讨论我们的葡萄酒交易协议。首先，我们会使用一种非正式的表格形式来展示如何运用 ROSE 协议来支持我们的葡萄酒交易交换。我们已经使用 ASN.1 规范定义了两个主要消息类型。

<table><tbody><tr><td data-imt-p="1">Expressing wineco exchanges as a set of remote operations - you don't have to, but it might be simple and convenient. 将 Wineco 的交换操作表示为一组远程操作——虽然不必这样做，但这样可能会更简洁方便一些。</td></tr></tbody></table>

```txt
Order-for-stock and Return-of-sales 
```

We will add, without defining the ASN.1 types themselves, two further wineco messages we might wish to pass with a ROSE INVOKE, namely 我们将在不定义 ASN 类型本身的情况下，再添加两种希望通过 ROSE 调用传递的 wineco 消息，即

```txt
Query-availability and Request-order-state 
```

The first of these messages queries the availability of items for immediate delivery, and the second asks for an update on the state of an earlier order. 第一条消息询问了那些可以立即交付的商品的可用性，第二条消息则是对之前一个订单的进展情况进行更新。

We will make all four of these messages a ROSE operation, which will either produce a response or an error return. The response to an "Order-for-stock" will be an "Order-confirmed" message. Successful processing of a "Return-of-sales" will result in an ASN.1 NULL being returned. The response to "Query-availability" will be an "Availability-response" and the response to a "Requestorder-state" will be an "Order-status" response. 我们将把这四条消息都设计为 ROS 操作，这样要么会返回响应，要么会返回错误。对于“库存订单”请求，响应将是一个“订单已确认”的消息。而“销售退货”请求的成功处理将会返回一个 ASN.1 NULL 响应。对于“可用性查询”请求，响应将是一个“可用性响应”消息；而对于“订单状态查询”请求，则返回一个“订单状态”响应。

We envisage that some or all of these requests (operations) can produce the following errors (in each case with some additional data giving more details of the failure): 我们认为，这些请求或操作中有一些可能会导致以下错误（在每种情况下，还会伴随一些额外的数据，以便更详细地描述故障情况）：

• Security check failure. • 安全检查失败。

• Unknown branch. • 未知的分支。

• Order number unknown. • 订单编号未知。

• Items unavailable. • 这些物品无法获得。

Note that there are other operation-independent errors carried in the ROSE Reject message that are provided for us by ROSE, but we do not need to consider those. Here we are only interested in errors specific to our own operations. 请注意，ROSE 拒绝消息中还包含了一些与操作无关的错误信息，这些信息是由 ROSE 系统提供的，但我们不需要考虑这些错误。在这里，我们只关心那些与我们的操作相关的错误。

We need to say all this rather more formally, but we start by doing it in an informal tabular form shown in figures II-13 and II-14. 我们需要以更正式的方式来表达这些内容，但首先，我们可以用图 II-13 和图 II-14 中所展示的非正式表格形式来呈现它们。

In the figures, names such as "asn-val-....." are ASN.1 value reference names of a type defined by ROSE (actually, a CHOICE of INTEGER or OBJECT IDENTIFIER) used to identify operations or errors, and names such as "ASN-type-...." are ASN.1 types that carry more details about each of our possible errors. Note that in the case of the error "Order number unknown", we decide to return no further information, and we have left the corresponding cell of the table empty. We could have decided to return the ASN.1 type NULL in this case, but the element in the ROSE "ReturnError" SEQUENCE type that carries the parameter is OPTIONAL, and by leaving the cell of our table blank, we indicate that that element of the "ReturnError" SEQUENCE is to be omitted in this case. We will see later how we know whether we are allowed to leave a cell of the table empty or not. 在这些图中，诸如“asn-val-…”这样的名称属于 ASN.1 中的值引用名称，这些名称由 ROSE 定义的类型来表示特定操作或错误。而诸如“ASN-type-…”这样的名称则代表 ASN.1 类型，它们包含了关于各种可能错误的详细信息。需要注意的是，在错误“订单编号未知”的情况下，我们决定不返回任何信息，因此将表格中的相应单元格留空。虽然我们可以在这种情况下使用 ASN.1 类型 NULL，但 ROSE 中的“ReturnError”序列类型中的该元素却是可选择的。通过将表格中的对应单元格留空，我们表明在这种情况下可以省略“ReturnError”序列中的该元素。之后我们会进一步了解如何判断是否允许将表格中的某个单元格留空。

Figure II-13: The wineco ERROR table 图 II-13：葡萄酒误差表

The figure II-13 table has one row for each possible error, and has just two columns: 在 II-13 表格中，每一可能错误都对应一行记录，并且只有两列：

• the error codes assigned (as values of the type determined in the ROSE specification); and • 所分配的错误代码（这些代码是根据 ROSE 规范中确定的类型来定义的）；以及

• the corresponding ASN.1 type (defined in our module) to carry parameters of the error. • 与之对应的 ASN.1 类型（在我们模块中有定义），用于携带错误相关的参数。

We might normally expect a small number of rows for this table for any given application that uses ROSE to define its protocol (in our case we have four rows), and it may be that for some errors there is no additional parameter information to return, and hence no ASN.1 type needed for parameters of that error, as in the case of "asn-val-unknown-order". 对于使用 ROSE 来定义协议的任何应用程序来说，这个表的行数通常都会比较少（在我们的案例中，有四行）。在某些情况下，某些错误可能没有任何额外的参数信息可供返回，因此也就不需要为这些错误指定 ASN.1 类型了，比如在“asn-val-unknown-order”这种错误的情况下。

The table in figure II-14 is the other information needed to complete the ROSE protocol for our wineco application. It lists an operation code, which is again a value of the type - as specified by ROSE: 图 II-14 中的表格包含了完成 ROSE 协议所需的其他信息。该表格列出了操作代码，这些代码属于 ROSE 所定义的类型——即数值类型。

$$
\begin{array}{l} \text {CHOICE} \left\{\text {local INTEGER}, \right. \\ \text {global OBJECT IDENTIFIER} \end{array}
$$

together with the ASN.1 type that carries the input arguments for the operation, together with the ASN.1 type that carries the result values, together with a list of the errors that the operation can generate. 包括用于该操作的输入参数的 ASN.1 类型，以及包含结果值的 ASN.1 类型。此外，还包括该操作可能产生的错误列表。

<table><tbody><tr><td data-imt-p="1">Op Code 操作代码</td><td data-imt-p="1">Argument Type 论点类型</td><td data-imt-p="1">Result Type 结果类型</td><td data-imt-p="1">Errors 错误</td></tr><tr><td data-imt-p="1">ash-val-order 灰烬秩序</td><td data-imt-p="1">Order-for-stock 按股票数量订购</td><td data-imt-p="1">Order-confirmed 已确认订单</td><td data-imt-p="1">security-failure unknown-branch 安全故障，原因不明——分支部分</td></tr><tr><td data-imt-p="1" data-imt_insert_failed_reason="same_text">asn-val-sales</td><td data-imt-p="1">Return-of-sales 销售回售</td><td>NULL</td><td data-imt-p="1">security-failure unknown-branch 安全故障，原因不明——分支部分</td></tr><tr><td data-imt-p="1" data-imt_insert_failed_reason="same_text">asn-val-query</td><td data-imt-p="1">Query-availability 查询可用性</td><td data-imt-p="1">Availability-Response 可访问性-响应</td><td data-imt-p="1">security-failure unknown-branch unavailable 安全机制故障，未知分支不可用</td></tr><tr><td data-imt-p="1">asn-val-state ASN-值状态</td><td data-imt-p="1">Request-order-state 请求-订单-状态</td><td data-imt-p="1">Order-status 订单状态</td><td data-imt-p="1">security-failure unknown-branch unknown-order 安全故障，未知分支，未知顺序</td></tr></tbody></table>

In the real ROSE specification, there are additional columns to assign a priority value for operations and for error returns, to identify so-called "linked operations", and to determine whether results are always returned, values of error parameters needed, and so on. Discussion of these details of ROSE would go beyond the scope or the needs of this text, and we have not included these features in the illustration. 在真实的 ROSE 规范中，还有额外的列用于为操作分配优先级，以及处理错误返回情况；这些列还可以用来识别所谓的“关联操作”；此外，这些列还用于确定是否总是返回结果、所需的错误参数值等。关于 ROSE 这些细节的讨论超出了本文的范围，因此我们并没有在图示中包含这些功能。

Given then the ROSE concept of messages (ASN.1 datatypes) with "holes" in them, we see 鉴于消息采用 ROSE 规范格式（ASN.1 数据类型），这些格式中存在“空洞”情况，因此我们会看到这样的结果。

• The need for a syntax for ROSE to specify the information its users need to supply to complete the ROSE datatypes by the specification of a number of operations and errors (definition of the number and form of the above tables). • 需要一种语法规则，用于 ROSE 语言，以明确用户需要提供的信息。同时，还需要规定一些操作规则和错误类型（例如，上述表格的数量和形式）。

• The need for a strict ASN.1 syntax (machine-readable) for ROSE users to specify the information shown informally in figures II-13 and II-14. • 对于 ROSE 用户来说，需要一种严格的 ASN.1 语法（便于机器读取的语法），以便他们能够清晰地指定图 II-13 和图 II-14 中非正式展示的信息。

• The need for notation in ASN.1 to identify "holes" in ASN.1 types, and to link the information shown in figures II-13 and II-14 clearly with the "hole" it is intended to complete. 在 ASN.1 中，需要使用注释来标识 ASN.1 类型中的“空洞”，并且需要将图 II-13 和图 II-14 中显示的信息与那些需要填充的“空洞”清晰地联系起来。

## 3.1 From specific to general 3.1 从具体到 général

In the general case, there may be many different tables needed to complete any given "generic" protocol, and each table will have a number of columns determined by that "generic" protocol. The nature of the information needed for each column of the table (and the column headings to provide a "handle" for each piece of information) will all vary depending on the "generic" protocol in question. 在一般情况下，为了完成任何给定的“通用”协议，可能需要使用许多不同的表格。每个表格中的列数由该“通用”协议决定。表格中每一列所需的信息内容，以及列标题的作用，都会根据具体的“通用”协议而有所不同。

ROSE is just one example of incomplete (generic) protocols. There are many other examples where specifiers leave it to others to complete the specification, and need to be able to (formally) say what additional information is needed. This is an Information Object Class specification. ROSE 只是不完整（通用）协议的一个例子。还有很多其他的情况，其中规范制定者将规范的交付权委托给他人来完成，而他们自己则需要能够（正式地）说明还需要哪些额外的信息。这就是信息对象类规范的一个例子。

Thus the specifier of a "generic" protocol needs a notation which will provide a clear statement of the form of the tables (the information needed to complete the "generic" protocol). We call the specification of this the specification of Information Object Classes. When a user of the "generic" protocol provides information for a row of a table we say that they are specifying an Information Object of the class associated with that table. The total set of rows of a given table defined to support any one user specification is called an Information Object Set. 因此，“通用”协议的规范需要一种能够明确说明表格格式的符号系统（即完成“通用”协议所需的信息）。我们将这种规范称为信息对象类的规范。当使用“通用”协议的用户为表格中的某一行提供信息时，他们实际上是在指定与该表格相关联的信息对象。而一个给定表格所包含的所有行，如果用于满足任何用户的需求，那么这些行就构成了一个信息对象集。

Notation is thus needed in ASN.1 for: 因此，在 ASN.1 中需要采用特定的标记方式来表示这些元素。

• The definition of a named Information Object Class (the form of a table). • 命名的信息对象类的定义（即表格的形式）。

• The definition of named Information Objects of a given class (completing the information for one row of the table). • 给定类别的命名信息对象的定义（包含了表格中某一行数据的完整信息）。

• Collecting together all the Information Objects (of any given class) defined in a specification into a named Information Object Set (a completed table). • 将所有在规范中定义的信息对象（无论属于什么类别）收集起来，形成一个名为“信息对象集”的完整表格。

Linking a named information object set to the "holes" in the carrier protocol that it is designed to complete. 将一组具有名称的信息对象与载体协议中需要被填充的“空缺”联系起来，从而完成该协议的功能。

## 4 From tables to Information Object Classes 4. 从表格到信息对象类

The table metaphor is a very useful one in introducing the Information Object Class concepts, but the term "table" is not used in the ASN.1 Standard itself (except in the term "table constraint", discussed later). 在介绍信息对象类概念时，使用表格作为比喻非常有用。不过，在 ASN.1 标准中本身并没有使用“表格”这个术语（除了后面提到的“表格约束”这一表述）。

<table><tbody><tr><td data-imt-p="1">Tables are fine for human-to-human communication. For computer processing we use ASN.1 notation to define the form of tables and the contents of those tables. 在人与人之间的通信中，使用表格是可行的。而在计算机处理方面，我们则使用 ASN.1 标记语言来定义表格的结构以及其中的内容。</td></tr></tbody></table>

We say that each Information Object has a series of fields, each with a field name. Defining an Information Object Class involves listing all the fields for objects of that class, giving the fieldname for each field, and some properties of that field. The most important property is the nature of the information needed when defining that field. This is most commonly the specification of some ASN.1 type (with the semantics associated with that type), or the specification of an ASN.1 value of some fixed ASN.1 type. We will, however, see later that there are a number of other sorts of fields that can be defined. 我们说过，每个信息对象都包含一系列字段，每个字段都有一个对应的字段名。定义某个信息对象类时，需要列出该类所有对象的字段，为每个字段指定字段名，以及该字段的一些属性。其中最重要的属性是定义该字段时所需要的信息类型。通常，这指的是某种 ASN.1 类型的规范（以及与该类型相关的语义），或者某种固定 ASN.1 类型的 ASN.1 值。不过，稍后我们会了解到，还可以定义其他类型的字段。

In the case of ROSE, we have two Information Object Classes defined by ROSE, the OPERATION class and the ERROR class. (Names of Information Object Classes are required to be all upper-case). 在 ROSE 的情况下，我们定义了两种由 ROSE 自身定义的信息对象类：操作类与错误类。（信息对象类的名称必须全部用大写字母表示。）

All objects of class OPERATION will have four fields containing: 所有属于 OPERATION 类的对象都将拥有四个字段，具体内容如下：

• A value of type • 一个类型为的值

$$
\begin{array}{l} \text {CHOICE} \left\{ \begin{array}{l l} \text {local} & \text {INTEGER}, \\ & \text {global} \end{array} \right. \text {OBJECT IDENTIFIER} \end{array}
$$

to identify the operation. 为了识别该操作。

• An ASN.1 type capable of carrying input values for the operation. • 一种符合 ASN.1 标准的类型，能够承载用于该操作的输入值。

• An ASN.1 type capable of carrying the result values on successful completion of the operation. • 一种 ASN.1 类型，能够存储操作成功完成后的结果值。

• A list of information objects of class ERROR, each of which is an error that this particular operation can produce. • 这是一个包含错误信息的列表，每个对象都代表该操作可能产生的一种错误。

All objects of class ERROR will have two fields containing: 所有属于 ERROR 类的对象都将拥有两个字段，其内容如下：

• A value of type • 类型为 的值

CHOICE {local INTEGER, global OBJECT IDENTIFIER} 选择 {局部整数，全局对象标识符}

to identify the error. 找出错误所在。

• An ASN.1 type capable of carrying the values of the parameters of the error. • 一种 ASN.1 类型，能够存储与错误相关参数的值。

To summarise: An Information Object Class definition defines the amount and form of information that is needed to specify an object of that class. An Information Object definition provides that information. The nature of the information needed can be very varied, and we talk about the form of the fields of the Information Object Class according to the information needed for that field when defining an Information Object. 总结一下：信息对象类的定义规定了指定该类对象所需的信息的数量和形式。而信息对象的定义则具体描述了这些信息的内容。所需信息的种类可能非常多样，因此在定义信息对象时，我们会根据每个字段所需的信息来规定该字段的形式。

In the above discussion, we have introduced: 在上面的讨论中，我们已经介绍了：

• type fields: Fields that need an ASN.1 type definition to complete them. • 类型字段：需要 ASN.1 类型定义来完成的字段。

• fixed type value fields: Fields that need the value of a single (specified) ASN.1 type to complete them. • 固定类型值字段：这类字段需要一个特定的 ASN.1 类型的值来填充它们。

object set fields: Fields that need a set of information objects of a single (specified) Information Object Class (in this case the ERROR class) to complete them. 对象集合字段：这些字段需要一组属于某个特定信息对象类的信息对象来填充它们（在本例中，该类为 ERROR 类）。

There are a number of other forms of field that can be specified when defining an Information Object Class, and we shall see more of these later. 在定义信息对象类时，还可以指定多种其他形式的字段。之后我们会进一步了解这些形式。

If you see names in all upper case, you can be reasonably sure that you are dealing with Information Object Classes, but another certain way to tell is the presence of names beginning with the & (ampersand) character. In order to avoid confusion with other pieces of ASN.1 notation, the names of fields of Information Object Classes are required to begin with an &. Thus the field of the OPERATION class that contains the object identifier value for some particular operation is called: 如果你看到所有名称都采用全大写字母表示，那么可以合理地判断你面对的是信息对象类。另一种确定方法就是看名称是否以&符号开头。为了避免与其他 ASN.1 表示法产生混淆，信息对象类的字段名称必须以&符号开头。因此，属于 OPERATION 类且包含某个特定操作的对象标识符值的字段，就被称作：

## OPERATION.&operationCode 操作 & 操作代码

The field that has to be supplied with a type definition for the arguments of the INVOKE message is called: 需要为 INVOKE 消息的参数提供类型定义的字段被称为：

## OPERATION.&ArgumentType 操作。&参数类型

Note that the &operationCode field contains a single ASN.1 value, and after the & we have a lower-case letter (this is a requirement), whilst the &ArgumentType field contains an ASN.1 type, and after the & we have an upper-case letter (again a requirement). Where a field contains a single value (usually - but not always - of some fixed type) or a single information object (of some fixed class) the field-name after the & starts with a lower-case letter. Where a field contains multiple values or multiple information objects (as with the list of errors for an operation), the field-name after the & starts with an upper-case letter. It is important to remember these rules when trying to interpret the meaning of an ASN.1 Information Object Class definition. 请注意，&operationCode 字段包含一个 ASN.1 值，且位于&之后的是一个小写字母；而&ArgumentType 字段包含一个 ASN.1 类型，位于&之后的是一个大写字母。当某个字段包含单个值（通常是某种固定类型的数值）或单个信息对象时，该字段的名称以小写字母开头。当字段包含多个值或多个信息对象时（例如操作错误列表），字段名称则以大写字母开头。在解读 ASN.1 信息对象类的定义时，记住这些规则非常重要。

We have already seen that names of Information Object Classes are required to be all upper case. Names given to individual Information Objects are required to start with a lower case letter (similar to value references), and names given to Information Object Sets (collections of Information Objects of a given class) are required to start with an upper case letter. 我们已经了解到，信息对象类的名称必须全部采用大写字母。而分配给单个信息对象的名称则必须从一个小写字母开始（类似于值引用方式）。至于信息对象集的名称（即某一类信息对象的集合），则必须从一个大写字母开始。

There is in general a strong similarity between the concepts of types, values, and sets of values (subtypes), and the concepts of Information Object Classes, Information Objects, and Information Object Sets, and naming conventions in relation to the initial letter of names follow the same rules. 一般来说，类型、值和值集（子类型）的概念与信息对象类、信息对象和信息对象集的概念有着明显的相似性。此外，名称的命名规则也遵循相同的规则，即名称的首字母具有特定的含义。

There is, however, an important difference between types and information object classes. All ASN.1 types start life populated with a set of values, and new types can be produceced as subsets of these values. Information Object Classes have no predefined objects, they merely determine the notation for defining objects of that class, which can later be collected together into information object sets, which are really the equivalent of types. 不过，类型和信息对象类之间确实存在重要的区别。所有的 ASN.1 类型在创建时都包含了一组值，而新的类型则可以作为这些值的子集被创建出来。信息对象类并没有预定义的对象，它们只是定义了用于描述该类对象的表示方式，这些表示方式之后可以被收集起来，形成信息对象集，而这些信息对象集实际上就相当于类型了。

When you define a class you provide it with a reference name, and similarly for Information Objects and Information Object Sets. These reference names can then be used in other parts of the ASN.1 notation to reference those classes, objects, and sets, just like type reference and value reference names are assigned to type and value definitions and then used elsewhere. Reference names for classes, objects, and object sets are imported and exported between modules in the IMPORTS and EXPORTS statements just like type and value reference names. 当定义一个类时，需要为其提供一个引用名称；对于信息对象和信息对象集合也是如此。这些引用名称可以在 ASN.1 表示法的其他部分中被用来引用这些类、对象和集合。就像类型引用和值引用名称被分配给类型和解码定义，并在其他地方被使用一样，类、对象和集合的引用名称也可以在 IMPORTS 和 EXPORTS 语句之间在模块之间导入和导出。类型值引用名称的运作方式，类、对象和对象集合的引用名称同样如此。

## 5 The ROSE OPERATION and ERROR Object Class definitions 5. 玫瑰行动与错误对象类的定义

Figure II-15 shows a simplified form of the definition of the OPERATION and ERROR classes of ROSE, and is the first introduction of the actual ASN.1 syntax for defining Information Object Classes. 图 II-15 展示了 ROSE 中“操作”类与“错误”类定义的简化形式。这也是首次引入用于定义信息对象类的实际 ASN 语法。

Remember, this syntax is essentially defining the table headings and the information content of the informal tables shown in II-13 and II-14, but it is doing it with a 请记住，这种语法实际上是在定义表格的标题以及 II-13 和 II-14 中展示的表格中的信息内容。不过，这种定义方式是采用一种特定的方式来实现的。

At last! We get to see an example of a real Information Object Class definition. Two in fact! The OPERATION class and the ERROR class from ROSE. 终于！我们看到了一个真实的“信息对象类”定义的例子。实际上有两个这样的类：来自 ROSE 的 OPERATION 类和 ERROR 类。

syntax that is similar to ASN.1 type and value definition syntax, and which is fully machineprocessable. 这种语法与 ASN.1 中的类型和值定义语法类似，而且完全可以被机器处理。

```txt
OPERATION ::= CLASS
    {&operationCode CHOICE {local INTEGER,
    global OBJECT IDENTIFIER}
    UNIQUE,
    &ArgumentType,
    &ResultType,
    &Errors ERROR OPTIONAL }

ERROR ::= CLASS
    {&errorCode CHOICE {local INTEGER,
    global OBJECT IDENTIFIER}
    UNIQUE,
    &ParameterType OPTIONAL }

Figure II-15: The OPERATION and ERROR class definitions 
```

In figure II-15, we see the definition of four fields for OPERATION and two for ERROR, as expected. Compare that figure with the table headings of figures II-13 and II-14, and let us go through the fields in detail. (Remember, each class definition corresponds to the definition of the form of a table, and each field corresponds to the definition of the form of a column of that table.) 在图 II-15 中，我们看到了“操作”字段的四种定义，而“错误”字段则有两种定义，这与预期一致。将这一图表与图 II-13 和图 II-14 中的表格标题进行比较，然后我们可以详细了解这些字段的含义。（记住，每个类别的定义都对应着表格中某个字段的形式，而每个字段则对应着该表格中某个列的格式。）

For the OPERATION class, we have the "&operationCode" field, which is required to be completed with a value of the specified type. (It is called a fixed type value field). This field is also flagged as "UNIQUE". When defining an object of this class, any value (of the specified type) can be inserted in this field, but if a set of such objects are placed together to form an Information Object Set (using notation we will see later), there is a requirement (because of the "UNIQUE") that all values in this field are different for each object in the set. If you regard the object set as representing a completely filled in table, then in database terminology, fields marked "UNIQUE" provide a key or index into the table. More than one field can be marked "UNIQUE" (but this is uncommon), but there is no mechanism in the notation to require that the combination of two fields has to be unique within an information object set. If you needed to specify that, you would have to use comment within the class definition. 在 OPERATION 类中，有一个名为“&operationCode”的字段，该字段必须包含指定类型的值。（它被称为固定类型值字段）。该字段也被标记为“UNIQUE”。在定义此类对象时，可以在该字段中插入任何指定类型的值。但是，如果将这些对象组合成一个信息对象集（稍后会在规范中介绍），那么由于“UNIQUE”的特性，该字段中的每个值都必须是不同的。如果将信息对象集视为一个完全填充的表格，那么在数据库术语中，标记为“UNIQUE”的字段就相当于表格中的键或索引。可以有多个字段被标记为“UNIQUE”（但这并不常见），不过在规范中并没有规定两个字段的组合在信息对象集中必须是唯一的。如果你确实需要指定这一点，那么你就需要在类定义中使用注释来说明。

The next two fields, "&ArgumentType" and "&ResultType" have names which begin with a capital letter, and no type definition after them. This means that they have to be completed by the specification of an ASN.1 type (usually, but not necessarily, by giving a type reference rather than an explicit definition of a type). 接下来的两个字段，“&ArgumentType”和“&ResultType”的命名方式都是以大写字母开头的，之后则不再有类型定义。这意味着这些字段需要通过指定一个 ASN 类型来填充（通常做法是提供类型引用，而不是明确的定义）。

The fourth and last field is more interesting. "&Errors" begins with a capital letter, so you complete it with a set of things. But the name following is not an ASN.1 type reference, it is a class reference. So this field requires to be completed with a set of Information Objects of that (the ERROR) class, defined next. This field is also flagged as "OPTIONAL". This means that in the definition of objects of this class, it is not a requirement to define information for this field - it can be left blank. This would imply that the corresponding operation never produced a "ReturnError" response. 第四个也是最后一个字段比较有趣。&Errors 这个字段以大写字母开头，因此你需要用一组对象来填充它。不过，后面的名称并不是对 ASN.1 类型的引用，而是指向某个类。所以，这个字段需要用该类中定义的某个信息对象来填充。这个字段也被标记为“可选项”。这意味着，在定义该类的对象时，不必为这个字段定义任何信息——可以留空。这意味着相应的操作可能不会产生“ReturnError”响应。

It is left to the reader to examine the definition of the error class, which should now be understandable. 现在，读者可以自行研究错误类别的定义了，相信这一定义应该已经足够清晰明了了。

## 6 Defining the Information Objects 6. 定义信息对象

Let us now use the notation for defining objects of a defined class (in this case OPERATION and ERROR). We take the informal definition of operations and errors given in figures II-13 and II-14 and express them in the ASN.1 notation for defining objects. This is shown in figure II-16 (the ERROR objects) and II-17 (the OPERATION objects). 现在，让我们使用特定的符号来表示各种对象（在本例中为 OPERATION 和 ERROR）。我们参考了图 II-13 和图 II-14 中给出的操作和错误的非正式定义，并将其用 ASN.1 符号来表示。如图 II-16 所示（为 ERROR 对象），如图 II-17 所示（为 OPERATION 对象）。

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/a0059080-59e4-4cd9-913b-34e7587e39f7/88a3e713d917f81425c00f6df90cef5afbec52d269ccac2ceedfef6245ca2170.jpg)

```lisp
sec-fail ERROR ::=
{&errorCode asn-val-security-failure,
    &ParameterType ASN-type-sec-failure-details}
unknown-branch ERROR ::=
{&errorCode asn-val-unknown-branch,
    &ParameterType ASN-type-branch-fail-details}
unknown-order ERROR ::=
{&errorCode asn-val-unknown-order}
unavailable ERROR ::=
{&errorCode asn-val-unavailable,
    &ParameterType ASN-type-unavailable-details} 
```

Figure II-16: Definition of the wineco ERROR Information Objects 图 II-16：葡萄酒错误信息的对象定义

These figures should be fairly understandable, and a line-by-line commentary will not be given, but there are some points to which the reader's attention is drawn. 这些数字应该比较容易理解，不会进行逐行注释。不过，有一些要点需要读者注意。

Note that the left of the "::=" looks rather like the definition of a value reference - compare: 请注意，“::=”左边的部分看起来很像是值引用的定义——请参考相关说明：

which is read as "my-int-val of type INTEGER has the value 3". In a similar way, we read figures II-16 and II-17 as (for example) "sec-fail of class ERROR has the fields ...". Following the "::=" we list (in curly brackets) each of the fields in the class definition, in order, and separated by commas, giving in each case the name of the field and the definition of that field for this particular object. 翻译结果为：“我的-int-val 类型为整数类型，其值为 3”。同样地，我们理解图 II-16 和 II-17 的含义为：“ERROR 类中的 sec-fail 具有以下字段……”在“::=”之后，我们用大括号列出了类定义中每个字段的名称，这些字段按顺序排列，并用逗号分隔。每一条记录都包含了该字段的名称以及该字段在特定的对象中的定义。

Note also that the "unknown-order" ERROR object has no definition for the &ParameterType field - this is permissible only because that field was marked OPTIONAL in the class definition of figure II-15. 需要注意的是，名为“未知顺序”的 ERROR 对象没有对&ParameterType 字段的定义——这种情况是被允许的，因为在该图 II-15 的类定义中，该字段被标记为可选项。

Turning to the "&Errors" field, note that when we want to define a set of errors, we use a list of reference names separated by a vertical bar and enclosed in curly brackets. This may seem less intuitive than if a comma had been used as the list separator, but is in fact a special case of a much more powerful mechanism for grouping objects into sets using set arithmetic (see below). The vertical bar is used for set UNION, so we are producing a set for the "&Error" field of "order" which is the union of "security-failure" and "unknown-branch". 接下来是“&错误”这个字段。当我们想要定义一组错误时，会使用一个由竖线分隔、位于大括号中的引用名称列表来表示。这种方法可能不如使用逗号作为列表分隔符那样直观，但实际上这是一种更强大的机制——它可以通过集合运算将对象组合成特定的集合（详见下文）。竖线用于实现集合的并集操作，因此“order”字段中的“&错误”实际上是由“security-failure”和“unknown-branch”这两个集合合并而成的。

Finally, note that the names used in the definition of the "&Error" fields are themselves defined as errors in figure II-16. Those definitions would be in the same module as the figure II-17 definitions, or would be imported into that module. 最后，需要注意到在定义“&Error”字段时所使用的名称，其实都是如图 II-16 中所列出的错误名称。这些定义会与图 II-17 中的定义位于同一个模块中，或者可以被导入到该模块中。

```txt
order OPERATION ::=
    {&operationCode asn-val-order,
    &ArgumentType Order-for-stock,
    &ResultType Order-confirmed,
    &Errors {security-failure |
    unknown-branch}}
sales OPERATION ::=
    {&operationCode asn-val-sales,
    &ArgumentType Return-of-sales,
    &ResultType NULL,
    &Errors {security-failure |
    unknown-branch}}
query OPERATION ::=
    {&operationCode asn-val-query,
    &ArgumentType Query-availability,
    &ResultType Availability-Response,
    &Errors {security-failure |
    unknown-branch |
    unavailable}}
status OPERATION ::=
    {&operationCode asn-val-state,
    &ArgumentType Request-order-state,
    &ResultType Order-status,
    &Errors {security-failure |
    unknown-branch |
    unknown-order}}
Figure II-17: Definition of the wineco OPERATION Information Objects 
```