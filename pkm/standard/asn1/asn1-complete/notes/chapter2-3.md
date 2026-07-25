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
