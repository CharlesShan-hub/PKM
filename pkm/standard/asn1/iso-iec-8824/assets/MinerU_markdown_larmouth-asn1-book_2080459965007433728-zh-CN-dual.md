The figure II-16 and II-17 definitions may appear more verbose (they are!) than the informal tabular notation used in figures II-13 and II-14, however, they are very explicit, but more importantly they are machine-readable, and ASN.1 tools can process them and use these definitions in checking and decoding the content of "holes" in incoming messages. 在图 II-16 和 II-17 中给出的定义可能看起来比图 II-13 和 II-14 中使用的非正式表格形式更为冗长（不过，它们确实如此！）。然而，这些定义非常明确且易于理解。更重要的是，这些定义可以被机器读取。因此，使用 ASN.1 工具可以处理这些定义，并在检查和解码传入消息中的“漏洞”时利用这些定义来进行处理。

## 7 Defining an Information Object Set 7. 定义信息对象集

Why do we need to combine the definition of individual Information Objects into an Information Object Set? Well, we saw a use of this in defining the "&Errors" field of the OPERATION class above, but there is a more important reason. The whole purpose of defining Information Object Classes and Information Objects is to provide an ASN.1 definition of the complete (informal) table we saw earlier that determines what can fill in the holes in a carrier or generic protocol, and to link that ASN.1 definition to the "holes" in the generic or carrier protocol. 为什么我们需要将各个信息对象的定义合并到一个信息对象集中呢？其实，我们在定义 OPERATION 类的“&Errors”字段时就已经使用了这种合并方式。不过，还有一个更重要的原因。定义信息对象类和信息对象的整个目的，就是提供一个 ASN.1 定义，从而补全我们之前提到的那个不完整表格的内容，进而填补通用协议或载体协议中存在的空白。而将这些 ASN.1 定义与通用协议或载体协议中的“空白”部分联系起来，正是实现这一目的的关键。

<table><tbody><tr><td data-imt-p="1">The next step on the way. Someone has defined some Information Object Classes. We define some Information Objects. Now we pull them together into a named Information Object Set. 这是接下来的步骤。已经有人定义了一些信息对象类。我们现在也定义了一些信息对象。接下来，我们将这些信息对象组合成一个有名称的信息对象集。</td></tr></tbody></table>

So we need a notation to allow us to define Information Object Sets (collections of Information Objects of a given class), with a name assigned to that set which can be used elsewhere in our specification. 因此，我们需要一种标记方式，以便能够定义信息对象集（即属于某一类别的信息对象集合）。同时，这些集合应该有一个唯一的名称，这样在规范的其它部分就可以使用这个名称来进行引用。

Information Object Sets are collections of Information Objects, much as types can be seen as collections or sets of values. So it is not surprising that the names for Information Object Sets are required to start with an upper-case letter. If we want a name for the collection of operations we have defined in Figure II-17, we can write: 信息对象集指的是一系列信息对象的集合。就像类型可以被视为值的集合一样，信息对象集的名称也应当以大写字母开头。如果我们想要为图 II-17 中定义的操作集合命名，我们可以这样写：

$$
\begin{array}{c} \text {My - ops OPERATION : : = \{order |} \\ \text {sales |} \\ \text {query |} \\ \text {status \}} \end{array}
$$

Read this as "My-ops of class OPERATION is the set consisting of the union of the objects order, sales, query, and status". 可以理解为：“操作类对象集合指的是由订单、销售、查询以及状态这些对象所构成的联合。”

This is the most common form, but general set arithmetic is available if needed. Suppose that A1, A2, A3, and A4 have been defined as Information Object Sets of class OPERATION. We can write expressions such as: 这是最常见的一种形式，但如果需要的话，也可以使用一般的集合运算。假设 A1、A2、A3 和 A4 已经被定义为属于 OPERATION 类的信息对象集。我们可以编写如下表达式：

 

$$
\text { New - Set OPERATION }:: := \left\{ \begin{array}{l} (\text { A1 INTERSECTION A2 }) \\ \text { UNION (A3 EXCEPT A4) } \end{array} \right\}
$$

but as a colleague of mine frequently says: "No-one ever does!" 不过，正如我的一个同事经常说的那样：“从来没有人做到过！”

If you leave the brackets out, the most binding is EXCEPT, the next INTERSECTION, and the weakest UNION. So all the round brackets above could be omitted without change of meaning, but it is usually best to include them to avoid confusing a reader. (Some people seem to find it intuitive that "EXCEPT" should be the least binding, so clarifying brackets when "EXCEPT" is used are always a good idea.) 如果你不使用括号，那么最有权威性的连词是“EXCEPT”，其次是“INTERSECTION”，而“UNION”则是最弱的连词。因此，上述所有圆括号都可以省略，而不影响句子的意思。不过，通常还是应该保留这些括号，以避免让读者产生混淆。（有些人似乎认为“EXCEPT”应该是最弱的连词，所以在使用“EXCEPT”时加上括号来明确其含义是个好主意。）

I won't bore you with a long-winded example of the result for various sets A1 to A4 - invent your own and work it out - or ask your teenage daughter to help you! 我不会用冗长的例子来演示各种集合 A1 到 A4 的结果——请自己创造一些例子并自行计算吧！或者，也可以请你的女儿帮忙哦！

The caret character "^" is a synonym for "INTERSECTION", and the vertical bar character "|" is a synonym for "UNION". There is no single character that is a synonym for EXCEPT - you must write that out in full. 字符“^”是“INTERSECTION”的别名，而字符“|”则是“UNION”的别名。没有哪个字符可以作为“EXCEPT”的别名——你必须完整地将其书写出来。

We have already noted the similarity between Information Objects and values, and Information Object Sets and types or subtypes (collections of values). Where do classes fit into this pattern? This is less clear cut. Information Object Classes are in some ways like types, but unlike types, they start off with no Information Objects in them, merely with a mechanism for the ASN.1 user to define objects of that class. By contrast, built-in types come with a ready-made collection of values and value notation, from which you can produce subsets using constraints. 我们已经注意到，信息对象与值之间存在相似性，而信息对象集则与类型或子类型（值的集合）有相似之处。那么，类在这种模式中处于什么位置呢？这一点并不那么明确。信息对象类在某种程度上类似于类型，但与类型不同的是，类一开始并没有任何信息对象，而是提供了一个机制，让 ASN.1 用户能够定义该类的对象。相比之下，内置类型则已经包含了预先定义好的值集合以及值表示方式，用户可以通过约束条件来生成子集。

Nonetheless, because of the similarity of objects and values, when ASN.1 was extended to introduce the information-object-related concepts, it was decided to allow the same syntax as was introduced for defining sets of objects to be used for defining sets of values (subsets of some type). Because of this, the so-called value set assignment was introduced into the ASN.1 syntax. This allows you to write (should you so wish!): 不过，由于对象和值的相似性，当 ASN.1 被扩展以引入与对象相关的概念时，决定采用与定义对象集相同的语法来定义值集（某种类型的子集）。因此，在 ASN.1 语法中引入了一种所谓的值集分配机制。这样，你就可以这样编写（如果你愿意的话）：

$$
\begin{array}{l} \text {First - set INTEGER}: := \{0.. 5 \} \\ \text {Second - set INTEGER}: := \{1 0.. 1 5 \text {UNION} 2 0 \} \\ \text {Third - set INTEGER}: := \\ \quad \{\text {First - set UNION Second - set EXCEPT} 1 3 \} \\ \text {Fourth - set INTEGER}: := \{0.. 5 | 1 0.. 1 2 | 1 4 | 1 5 | 2 0 \} \end{array}
$$

"Fourth-set" is, of course, exactly the same subset of INTEGER as is "Third-set". “第四盘”当然与“第三盘”属于同一组整数集合。

It is testing time! Or put it another way, time for some fun! With the above definitions, can I write 现在是测试时间啦！或者可以说，是享受乐趣的时候了！根据以上的定义，我就可以开始编写了。

## selected-int Fourth-set ::= 14 选定的 int 第四组 ::= 14

and as an element of a SEQUENCE 作为序列中的一个元素

## Third-set DEFAULT selected-int 第三盘默认选入

Yes you can! This question of *exactly* what is legal ASN.1 in such cases has vexed the Standards group for several years, but is now largely resolved. It is, however, best to rely on a good tool to give you the answer, rather than to pore over the Standard text itself! Or maybe better still to keep your ASN.1 simple and straightforward! 是的，你可以这样做！关于在这种情况下什么是合法的 ASN.1 格式的问题，已经困扰了标准制定团队多年，但现在这个问题基本上已经解决了。不过，最好使用合适的工具来获取答案，而不是仔细阅读标准文本本身！或者，或许更理想的做法是保持 ASN.1 格式的简单明了。

Before we leave this sub-clause, let us look at "My-ops" again. It is likely that in a future version of the wineco protocol, we will want to add some additional operations, and hence to extend "Myops". This has implications for version 1 systems, which will need to have some defined errorhandling if they are requested to perform an operation that they know nothing about. We will see in a moment the way the error handling is specified, but first we need to indicate that "My-ops" may be extended in the future. We do this by re-writing it as: 在离开这个子条款之前，让我们再看看“My-ops”这个定义。在未来版本的 wineco 协议中，我们可能会需要添加一些额外的操作，因此也需要对“My-ops”进行扩展。这对于版本 1 的系统来说意味着，如果它们被要求执行一些它们并不了解的操作，那么就需要有一些明确的错误处理机制。接下来我们会介绍错误处理的具体实现方式，但现在需要先表明“My-ops”在未来是有可能被扩展的。我们通过将其重新表述为如下形式来实现这一点：

 

$$
\text { My - ops OPERATION }: := \left\{ \begin{array}{l} \text { order } \\ \text { sales } \\ \text { query } \\ \text { status }, \dots \end{array} \right\}
$$

with a possible version 2, with an added operation "payment", being written: 有一个可能的版本 2，其中增加了“支付”这一操作，具体实现如下：

## 8 Using the information to complete the ROSE protocol 8. 利用这些信息来完成 ROSE 协议的操作。

Lets get back to our main theme. Designers of "generic" protocols want to have elements of SEQUENCES and SETS that they do not define. They want other groups to define the types to fill these positions. Frequently the other groups will want to carry many different types in these elements at different times. The Information Object concepts enable the definition of the types 让我们回到主题上来。那些设计“通用”协议的开发者希望拥有一些既不是序列也不是集合的元素，他们不希望自己来定义这些元素。他们希望其他团队来负责定义用于填充这些位置的类型。通常，其他团队会在不同时间需要管理多种不同类型的元素。而信息对象的概念则使得定义这些类型变得更加容易。

No point in defining classes, objects, and object sets unless they are going somewhere. After-all, you can't encode them and send them down the line. So what good are they? Answer: to fill in holes. 如果没有明确说明类、对象以及对象集合的作用，那么定义它们就没有任何意义。毕竟，你无法将这些概念编码后传递给后续的处理流程。那么，它们究竟有什么用呢？答案是：用来填补其中的空白。

that will fill these elements. But how are these "holes" identified in an ASN.1 type definition? And how are the Information Object (Set) definitions linked to the "holes"? 这些元素将被填充进去。但是，在 ASN.1 类型定义中，如何识别这些“空缺”呢？此外，信息对象（集合）的定义又是如何与这些“空缺”相联系的呢？

Largely for historical reasons, ASN.1 takes a three-stage approach to this problem. The first step is to allow reference to a field of an Information Object Class to be used wherever an ASN.1 type (or in some cases an ASN.1 value) is required. The second stage is to allow an Information Object Set to be used as a constraint on such types, requiring that that element be a type (or a value) from the corresponding field of that Information Object Set. This is called a table constraint. The third step is to allow (additionally) two or more elements of a SET or SEQUENCE (that are defined as fields of the same Information Object Class) to be linked using a pointer between them (the "@" symbol is used to provide the link). Use of this linking mechanism says that the linked fields have to be filled consistently in accordance with some Information Object of the constraining Information Object Set. In other words, that the linked fields have to correspond to cells from a single row of the defining table. Constraints expressing a linkage between elements are called relational constraints. 由于历史原因，ASN.1 采用了三阶段的方法来解决这一问题。第一步是允许在需要 ASN.1 类型（或某些情况下需要 ASN.1 值）的地方引用某个信息对象类的字段。第二步是将信息对象集作为对这些类型的约束条件，即要求该元素必须是该信息对象集对应字段中的类型（或值）。这被称为表级约束。第三步是允许将集合或序列中的两个或多个元素通过指针连接起来（使用“@”符号来表示连接）。这种连接机制意味着，被连接的字段必须遵循某个信息对象集中的信息对象规范进行填充。换句话说，这些关联字段必须对应到定义表中的同一行中的单元格。表示元素之间关联关系的约束被称为关系约束。

Figure II-18 shows a (simplified) ROSE "Invoke" datatype, illustrating these features. It uses the Information Object Set "My-ops" (of class OPERATION), defined above, in the table and relational constraints on the elements of "Invoke". 图 II-18 展示了一个（简化的）ROSE“Invoke”数据类型，该图表展示了该数据类型的各项特性。该数据类型使用了上述定义的“My-ops”信息对象集（属于 OPERATION 类），并且在“Invoke”元素的表格和关系约束中得到了体现。

```txt
Invoke ::= SEQUENCE
{ invokeId INTEGER,
    opcode OPERATION.&operationCode
    ({My-ops} ! invoke-unrecognisedOperation),
    argument OPERATION.&ArgumentType
    ({My-ops}
    {@opcode} ! invoke-mistypedArgument) OPTIONAL }
Figure II-18: The ROSE Invoke datatype 
```

Figure 18 is quite complex! Take it a step at a time. The "opcode" element of the sequence says that it is a value from the "&operationCode" field of the class "OPERATION". In itself, this is just a synonym for 图 18 相当复杂！让我们一步一步来解析它。该序列中的“opcode”元素表明，它来自类“OPERATION”的“&operationCode”字段的值。实际上，这只是一个同义词而已。

because this is a fixed-type value field of this type. Or to put it another way, all values of this field are of this type. 因为这是一个固定类型的数值字段。或者换句话说，这个字段的所有值都属于这种类型。

However, by referencing the type through the field of the Information Object Class, we are then allowed to constrain it with an Information Object Set ("My-ops") of that class. (Such a constraint would not be allowed if we had simply written the element as "CHOICE ... etc".) 不过，通过引用信息对象类的字段类型，我们可以使用该类的信息对象集来对其进行约束。如果我们只是简单地将元素写成“CHOICE … etc”的形式，那么就无法实现这样的约束了。

The curly brackets round "My-ops" are a stupidity (sorry - there are a few!) in the ASN.1 syntax. The requirement here is for the syntactic construct "ObjectSet". A reference name for an object set (which is what "My-ops" would be) is not allowed. However, we can generate an "ObjectSet" from "My-ops" by importing "My-ops" into an object set definition, that is to say, by enclosing it in curly brackets. 在 ASN1 的语法中，圆括号“My-ops”其实是一种愚蠢的写法（抱歉，确实有一些这样的错误）。这里的要求是使用“ObjectSet”这个语法结构来表示对象集。不过，允许将“My-ops”作为一个独立的对象集来使用，也就是将其包裹在圆括号中。

Put simply, there is no good reason for it, but you have to put the curly brackets in! 简单来说，没有正当理由需要这样做，但你必须把圆括号放在正确的位置！

The effect of the "My-ops" constraint is to say that the only values permitted for this element are those assigned to the "&operationCode" field one of the Information Objects of "My-ops". In other words, the field must contain an op-code for one of the four (in version 1) operations defined for wineco. This is all fully machine-readable, and encoders/decoders can use this specification to help with error checking. “My-ops”约束的含义是：该元素所允许的值仅限于那些被分配给“My-ops”中信息对象之一的“&operationCode”字段所包含的值。换句话说，该字段必须包含 wineco 定义的四种操作中的一种操作码。所有这些信息都完全可以被机器读取，而编码器/解码器可以利用这一规范来帮助进行错误检查。

The "!" introduces an exception specification, and says that if this constraint is not satisfied (a different op-code value appears), the error handling is to return a REJECT with the integer value "invoke-unrecognisedOperation". The designers of the wineco protocol need not concern themselves with specifying such error handling. This is all done within the ROSE specification. Note that this is precisely the error situation that will arise if a version 1 implementation is hit with a request to perform the "payment" operation. “!”符号用于表示异常情况的处理。如果满足不了这一条件（即出现的操作码值与预期不符），那么错误处理机制会返回 REJECT 结果，同时附带一个整数值“invoke-unrecognisedOperation”。Wineco 协议的设计者无需专门处理这类错误情况，因为这些工作都在 ROSE 规范中已经解决了。需要注意的是，当版本 1 的实现遇到需要执行“支付”操作的请求时，就会出现这种错误情况。

Now we move onto the "argument" element. This is the true "hole". In its unconstrained form, it simply says that this element can be "any ASN.1 type" (because any ASN.1 type can be used for this field of an Information Object of the OPERATION class). Such notation is described in ASN.1 as "Open Type" notation, and is handled rather specially by encoding rules. 现在我们来讨论“参数”元素。这其实是个真正的问题所在。在不加限制的情况下，这个元素可以被定义为“任何 ASN.1 类型”。因为任何 ASN.1 类型都可以用于 OPERATION 类的信息对象这个字段。这种表示方式在 ASN.1 中被称为“开放类型”表示法，并且需要特别处理，因为它涉及到编码规则的问题。

In particular, it is important that encodings enable a decoder to find the end of an open type encoding before they know in detail what type is encoded within it (the "opcode" element of the SEQUENCE could have been written after the "argument" element - there is no restriction). 特别地，重要的是，这些编码方式能够使得解码器在不知道具体编码了哪种类型的数据之前，就能识别出开放类型编码的结尾。在“ARGUMENT”元素之后，还可以写入“OPCODE”元素——实际上并没有这种限制。

In BER, there is no problem - the end of an encoding can always be determined using the "L" field of the "TLV", for all ASN.1 BER encodings of types. In PER, however, this is not the case. Unless a decoder knows what the type being encoded is, it cannot find the end of the encoding of a value of the type. So in PER, an extra "length" wrapper is always added to an open type. 在 BER 编码中，不存在这个问题——对于所有 ASN.1 编码类型，编码的结束位置可以通过“TLV”中的“L”字段来确定。然而，在 PER 编码中情况则不同。除非解码器知道所编码数据的类型，否则它无法找到该类型数据的编码结束位置。因此，在 PER 编码中，总是会在开放类型前面添加一个额外的“长度”字段来指示其长度。

As an aside, you will sometimes find people deliberately defining an element as an open type (typically using a class with just one field, a type field), and then constraining that element to be a single fully-defined ASN.1 type. The sole purpose of this is to produce the additional length wrapper, and relates to implementation architecture. Such constructs are used to encapsulate security-related data, where the implementation architecture is likely to be to pass an encapsulated set of octets to a security kernel, with the insecure part of the application having no detailed knowledge of the security-related data. (Government Health Warning - Figure 999 - again - you must judge for yourself whether such provision is sensible or not. It happens. At worst it just means an unnecessary length field!) 顺便提一下，有时你会看到有人故意将一个元素定义为开放类型（通常是一个只有一个字段的类），然后限制该元素只属于一个完全定义的 ASN.1 类型。这样做的唯一目的就是为数据添加额外的长度字段，这与实现架构有关。这种结构用于封装与安全性相关的数据，在这种情况下，实现架构通常是将封装后的八位元数据传递给安全内核，而应用程序的不安全部分则无需了解与安全性相关的数据细节。（政府健康警告——图 999——再次提醒，你必须自行判断这种做法是否合理。这种情况确实会发生。最坏的情况下，它只不过是一个不必要的长度字段而已！）

Finally, we address the "@" part of "argument". This turns the constraint into a relational constraint, linking the "argument" and "opcode" fields, and requiring them to be consistent with some row of the constraining table. (Whoops! To be consistent with some object in the constraining Information Object Set - let's use the correct terminology!). 最后，我们处理“argument”中的“@”部分。这部分将约束条件转化为一种关系约束，从而将“argument”和“opcode”字段联系起来，并要求它们与约束表中的某一行数据保持一致。（哎呀！更准确地说，应该是与约束信息对象集中的某个对象保持一致——让我们使用正确的术语吧！）

The "@" construction could equally well, and with the same effect, have been placed on the "opcode" field (as well, or instead of). All that is being formally said is that the two (and there could be more) linked fields have to be consistent with an object in the set. We know, of course, that "OPERATION.&operationCode" was defined as "UNIQUE" in the class definition, so there will be at most one object in the Information Object Set that matches a value in the "opcode" field of the "Invoke" message. In the general case, this is not necessarily true, and the only requirement is that the values and/or types of linked fields are consistent with at least one of the information objects in the constraining object set (consistent with at least one row of the constraining table). “@”符号的构造同样可以放在“操作码”字段上，且效果相同。实际上，需要保证两个（甚至更多个）关联字段的值与集合中的某个对象保持一致。当然，我们知道在类定义中，“OPERATION&operationCode”被定义为“唯一”，因此，在“Invoke”消息的“操作码”字段中，最多只能有一个值与集合中的某个对象匹配。但在一般情况下，这种情况并不必然成立。唯一的要求是，关联字段的值和/或类型与约束对象集中的至少一个信息对象保持一致（即与约束表的至少一行数据一致）。

Finally, note the "invoke-mistypedArgument" error return. In BER, there is a lot of redundancy in an encoding, and it can usually be easily detected if an encoding does not represent a value of the type we think it should (or might) be. In PER, this is not so often the case, as there is much less redundant encoding. In PER, the main detection of "invoke-mistypedArgument" will be if the encoding of the open type (as determined by the added length field) does not have the right length for some value of the type we are trying to match it with (the one identified by the "opcode" value). 最后，需要注意“invoke-mistypedArgument”错误返回的情况。在 BER 编码中，由于存在大量的冗余信息，因此如果某种编码所表示的类型与我们预期的类型不符，通常可以很容易地检测到这个问题。而在 PER 编码中，这种情况并不常见，因为冗余编码的数量要少得多。在 PER 中，检测“invoke-mistypedArgument”错误的主要依据是，根据附加的长度字段确定的开放类型编码，其长度并不适合我们试图匹配的那个类型（即由“opcode”值所标识的类型）。

There is always an argument among protocol designers on the extent to which one should specify the actions of an implementation on receipt of erroneous material (presumably from a bust sending implementation, or due to the very very rare occurrence of undetected errors in lower layers), or whether such actions should be left as implementation-dependent. ASN.1 provides notation to go in either direction. ROSE chose to be very prescriptive on error handling, and made full use of ASN.1 exception handling to specify the required behaviour on receipt of "bad" material. If you are a protocol designer, this is a decision for you to take. ASN.1 gives you the tools to be prescriptive, but there is no requirement to use those tools, and many specifiers choose not to. 在协议设计者之间，总是存在关于是否应该明确指定在收到错误数据时的处理方式的争论（这些数据可能来自发送失败的情况，或者由于底层代码中极罕见的未检测到的错误而引发）。或者，是否应该将这种处理方式留给实现方自行决定。ASN.1 提供了两种可能的表达方式。ROSE 在错误处理方面采取了非常严格的规定方式，充分利用 ASN.1 的异常处理机制来指定在收到“错误数据”时的行为。如果你是一名协议设计者，这就是你需要做出的决定。ASN.1 提供了实现严格规定的工具，但实际上并没有强制要求使用这些工具，许多规范制定者选择不采用这种方式。

Note that there is a certain difference between the "!" on the opcode element and that on the "argument" element. In the first case we know it can get activated if a version 2 system tries to invoke "payment" on a version 1 system. In the second case it should never get activated if systems are conforming and lower layer communications are reliable. 需要注意的是，操作元素上的“!”与“参数”元素上的“!”之间存在一定的差异。在第一种情况下，我们知道如果版本 2 的系统试图对版本 1 的系统调用“payment”函数，那么这个操作符可能会被激活。而在第二种情况下，只要系统遵循了相关规范，并且下层通信是可靠的，那么这个操作符就绝不会被激活。

## 9 The need for parameterization 9. 参数化的需求

I wonder how many readers noticed that the above, whilst looking attractively precise and implementable, recognised the major problem with it? 我想知道，有多少读者注意到，虽然上述描述看起来非常精确且易于实施，但实际上它存在着一个主要问题。

But unfortunately it just doesn't work! Lot's of people are defining their own "My-op" object sets, but there is just one ROSE specification of "Invoke"! 不过，不幸的是这种方法并不奏效！很多人都在定义自己的“我的操作”对象集，但实际上“Invoke”这个动作只有一种规范定义而已！

If we were to re-write the whole of ROSE in 如果我们能够重新编写整个《ROSE》的故事的话……

our wineco specification, the above would work fine. We might have a series of modules defining our main types, as illustrated in earlier chapters (call these MAIN modules) and another module defining the OPERATION and ERROR classes, and the "Invoke", "Reject", "ReturnResult", and "ReturnError" (call this the ROSE module). Then we have a final module (call this the INFORMATION OBJECTS module) that defines our information objects and the "My-op" set. 在我们的 Wineco 规范中，上述描述应该能够正常工作。我们可能会有一系列模块来定义各种主要类型，就像在前面的章节中所描述的那样（将这些模块称为 MAIN 模块）。此外，还有另一个模块用于定义 OPERATION 和 ERROR 类，以及“Invoke”、“Reject”、“ReturnResult”和“ReturnError”这些函数（将这一模块称为 ROSE 模块）。最后，还有一个模块（称为 INFORMATION OBJECTS 模块），用于定义我们的信息对象以及“My-op”集合。

From MAIN we export all our top-level wineco types. From the ROSE module we export our Information Object Class definitions. In the INFORMATION OBJECTS module we import the Information Object Class definitions, and export "My-op". Finally, in the ROSE module, as well as exporting the class definitions, we import "My-op" for use in the "Invoke" etc messages as described above, and define our top-level PDU that now defines our wineco abstract syntax as: 我们从 MAIN 模块出口所有高级别的葡萄酒类型。在 ROSE 模块中，我们出口了信息对象类的定义。在 INFORMATION OBJECTS 模块中，我们导入这些信息对象类的定义，并出口“My-op”定义。最后，在 ROSE 模块中，除了导出类定义之外，我们还导入“My-op”，以便在“Invoke”等消息中使用，同时定义了我们的最高级别的 PDU。现在，这个 PDU 定义了我们的葡萄酒抽象语法。

```txt
wineco-PDU ::= CHOICE
{invoke Invoke,
reject Reject,
result ResultResult,
error ReturnError } 
```

We have a complete and working protocol. 我们有一套完整且可行的操作方案。

But this approach does not work if we want the ROSE specifications to be published totally separately from the wineco specification, with lot's of different applications (of which wineco would be just one) wanting to produce a ROSE-based specification. Copying the ROSE text for each application would not be a good idea! (That said, there are specifications about that define their own ROSE-equivalent classes and PDUs, usually in a simplified form, simply because they wish to be complete in their own right and to have control so that the ROSE part cannot change under their feet. This "copying with simplification" occurs with other popular specifications, not just with ROSE.) 但是，如果我们希望 ROSE 规范能够与 wineco 规范完全独立地发布，那么这种做法就不适用了。因为有很多不同的应用场景需要使用基于 ROSE 的规范，而 wineco 规范只是其中之一。为每个应用场景复制 ROSE 规范显然不是一个好主意！不过，也有一些规范采用了类似的做法，它们自己定义了 ROSE 等效的等级和 PDU，通常是以简化形式呈现的。这些规范希望保持自身的完整性，并能够控制 ROSE 部分的变更。这种“简化后复制”的做法在其他流行的规范中也很常见，而不仅仅是 ROSE 规范。

If the ROSE specification is to be independent of the wineco application, then clearly it cannot import the "My-op" type. How then can it supply a constraint to say how the hole is to be filled in? 如果 ROSE 规范要与 Wineco 应用程序独立运行，那么显然它就无法导入“我的操作”类型的数据。那么，它该如何设定约束条件来决定如何填充这个漏洞呢？

## Here we introduce a new and very powerful ASN.1 concept, that of parameterization. 在这里，我们引入了一个新且非常强大的 ASN.1 概念，即参数化机制。

All programmers are fully familiar with the concept of functions or subroutines or methods having a set of dummy parameters which are referred to in the body of the function or subroutine or method specification. When those functions or subroutines are called, the calling code supplies a set of actual parameters that are used instead of the dummy parameters for that call. 所有程序员都熟悉函数的概念，也就是在函数的主体中定义的一组虚拟参数。当这些函数或子程序被调用时，调用代码会提供一组实际的参数，这些实际参数会替代那些虚拟参数在调用过程中被使用。

ASN.1 has a very similar concept. When we define a type, such as the ROSE "Invoke" type, we can list after the type name a dummy parameter list. These dummy parameters can then be used on the right-hand side of the type definition as if they were normal reference names. We call such a type a parameterised type, and we can export parameterised types (for example from the generic ROSE specification, with import into one or more application specifications like wineco). In the importing specification (or anywhere else the parameterised type is used) we supply an actual parameter specific to that use. Figure II-19 shows the ROSE module, and Figure II-20 the wineco module. Note that now all exporting is from ROSE - ROSE does no imports at all. ASN.1 的概念与之非常相似。当我们定义一种类型时，比如 ROSE 中的“Invoke”类型，我们可以在类型名称之后列出一个虚拟参数列表。这些虚拟参数可以在类型定义的后半部分像普通引用名称一样被使用。我们称这种类型为参数化类型，并且可以导出参数化类型（例如从通用的 ROSE 规范中导出，然后将其导入到一个或多个应用规范中，比如 wineco）。在导入的规范中（或者参数化类型被使用的任何其他地方），我们需要提供特定于该使用的实际参数。图 II-19 展示了 ROSE 模块，而图 II-20 则展示了 wineco 模块。请注意，现在所有的导出操作都是从 ROSE 规范进行的——ROSE 根本不进行导入操作。

```txt
ROSE-module
{joint-iso-itu-t remote-operations(4) generic-ROS-PDUs(6)}
DEFINITIONS
AUTOMATIC TAGS
BEGIN
EXPORTS OPERATION, ERROR, Rose-PDU{};

Rose-PDU {OPERATION:User-ops} ::=
    CHOICE
{invoke    Invoke {User-ops},
reject    Reject,
result    ReturnResult {User-ops},
error    ReturnError {User-ops} }

Invoke {OPERATION:User-ops} ::= SEQUENCE
{ invokeId    INTEGER,
opcode    OPERATION.&operationCode
({User-ops} ! invoke-unrecognisedOperation),
argument    OPERATION.&ArgumentType
({User-ops}
{@opcode} ! invoke-mistypedArgument) OPTIONAL }

Reject ::= etc
ReturnResult {OPERATION:User-ops} ::= etc
ReturnError {OPERATION:User-ops} ::= etc
END

Figure II-19: Defining and exporting a parameterised type 
```

There are a few points to notice in figure II-19. We could have exported separately the Invoke, Reject, ReturnResult, and ReturnError messages, but we chose to bundle these together as a "Rose-PDU" CHOICE type and to export that. This meant that "Rose-PDU" had to be parameterised with the "User-ops" dummy parameter, with that dummy parameter supplied as the actual parameter to the use of Invoke and ReturnResult and ReturnError within that CHOICE. Invoke, ReturnResult and ReturnError slightly confusingly use the same name for their dummy parameter, which is then used for the table and relational constraint. This situation of having a dummy parameter being passed down through a chain of nested type definitions is quite common, and it is also quite common for the same name to be used each time, but please note that formally these are distinct names - as you would expect, the scope of a dummy parameter name is limited to the right-hand side of the parameterised type. 在图 II-19 中有一些需要注意的地方。我们可以分别输出 Invoke、Reject、ReturnResult 和 ReturnError 这些消息，但我们选择将它们合并在一起，作为“Rose-PDU”选项的一部分进行输出。这意味着“Rose-PDU”需要使用“User-ops”这个虚拟参数进行参数化，而这个虚拟参数实际上被用作 Invoke 和 ReturnResult 以及 ReturnError 在选项中的实际参数。Invoke、ReturnResult 和 ReturnError 这几个名称有些令人困惑，因为它们都使用了相同的名称作为虚拟参数，而这个参数也被用于表格和关系约束中。这种通过嵌套类型定义传递虚拟参数的做法很常见，而且每次都使用相同的名称也是常见的做法。不过请注意，从形式上讲，这些名称其实是不同的——正如你所预期的那样。虚拟参数的名称范围仅限于参数化类型的右侧部分。

Note also the occurrence of "{}" after Rose-PDU in the EXPORTS list (and later in the IMPORTS list of Figure II-20). This is not a requirement, but helps to clarify for a human reader that this is a parameterised type. 请注意，在 EXPORTS 列表中，Rose-PDU 后面出现了“{}”符号（在图 II-20 的 IMPORTS 列表中也有出现）。这并不是必需的，但有助于让阅读者明白这是一个被参数化的类型。

The dummy parameter list in this case has just one dummy parameter (if there were more it would be a comma-separated list), and here we see the syntax for a dummy parameter that is an Information Object Set. It is the class name ("OPERATION"), a ":" (colon), then the dummy parameter name which must start with a capital letter because it is an Information Object Set. We will in the next chapter that dummy parameters can be many other things as well, and that things other than types can be parameterised, but this will suffice for now. 在这种情况下，虚拟参数列表只有一个虚拟参数（如果有很多个的话，那就会是一个以逗号分隔的列表）。这里我们看到的是以信息对象集形式表示的虚拟参数的语法结构。首先是类名称（“OPERATION”），然后是冒号“:”，接着是虚拟参数的名称，由于这是一个信息对象集，所以名称必须以大写字母开头。在下一章中我们会了解到，虚拟参数可以包含许多其他类型的内容，而且除了类型之外，还有其他元素可以被参数化。不过目前来说，这种描述已经足够了。

Figure II-20 shows the import into Wineco-main, and the definition of the new ROSE-based abstract syntax with the supply of the wineco-specific "My-ops" as the actual parameter to the Rose-PDU parameterized type. 图 II-20 展示了数据导入 Wineco 主数据库的过程，以及新的基于 ROSE 的抽象语法定义。其中，Wineco 特有的“My-ops”参数被用作 ROSE 参数化类型的实际参数。

```txt
Wineco-main
{ joint-iso-itu-t internationalRA(23) set(42)
    set-vendors(9) wineco(43) modules(2) main(5)}
DEFINITIONS
AUTOMATIC TAGS
BEGIN
IMPORTS
Rose-PDU{} FROM Rose-module
{joint-iso-itu-t remote-operations(4) generic-ROS-PDUs(6)}
My-Ops FROM Wineco-operations
{ joint-iso-itu-t internationalRA(23) set(42)
    set-vendors(9) wineco(43) modules(2) ops(4)};
wineco-abstract-syntax ABSTRACT-SYNTAX ::=
{ Rose-PDU{My-ops} IDENTIFIED BY
{ joint-iso-itu-t internationalRA(23) set(42)
    set-vendors(9) wineco(43) abstract-syntax(2)}
HAS PROPERTY
{handles-invalid-encodings}
-- See the Rose specification -- }
END

Figure II-20: Using the ROSE-PDU to define the Wineco abstract syntax 
```

## 10 What has not been said yet? 10 还有哪些事情还没有被提及呢？

This chapter has hopefully given the reader a good understanding of the concepts related to Information Objects, and the principle of parameterization of ASN.1 constructs, but it has not told the full story. 本章希望能让读者对与信息对象相关的概念以及 ASN 结构参数化原理有更深入的理解。不过，这并没有涵盖所有的细节。

## Why is there always more to say? 为什么总有更多的事情需要说呢？

In the next chapter, we will complete some more detail on the full possibilities for the sorts of fields you can define when you specify an Information Object Class. 在下一章中，我们将详细探讨在指定信息对象类时，可以定义的各种字段类型的具体可能性。

There is also an important facility called variable syntax which enables a more user-friendly (and sometimes less verbose) notation to be used for defining objects of a given class (replacing the notation of Figure II-17). 此外，还有一个重要的功能叫做“可变语法”，它使得定义某个类中的对象时可以使用更易于使用的表达方式（有时甚至可以减少不必要的冗余表述）。这种表达方式可以替代图 II-17 中的 notation。

On the question of constraints, we saw in earlier chapters the simple subtype constraints, and in this chapter table and relational constraints have been introduced. The next chapter will explore some further examples of constraints, and will also introduce the remaining type of constraint, the so-called user-defined constraint. 在约束方面，在前面的章节中已经介绍了简单的子类型约束。而在本章中，则引入了表和关系约束。下一章将进一步探讨一些其他的约束类型，并且会介绍另一种重要的约束类型——用户自定义约束。

On parameterization, there is a little more discussion to be had, including mention of so-called parameters of the abstract syntax and the extensible empty set. 在参数化方面，还有更多需要讨论的内容，其中包括对所谓抽象语法结构的参数以及可扩展空集参数的讨论。

Finally, we will mention the remaining ASN.1 constructs that provide alternative means of leaving holes in specifications. Readers will be pleased to know that at the end of that chapter, they can be certified as "ASN.1 Complete" as far as the notation is concerned, and if that is their only interest in reading this book, they can stop there! 最后，我们还将介绍其余的 ASN.1 构造方式，这些构造方式为填补规范中的空白提供了替代方案。读者们会很高兴地得知，在那一章的末尾，他们可以确信自己的文档在语法方面是符合 ASN.1 规范的，而如果阅读这本书只是出于对这一点的兴趣，那么他们也可以就此停止阅读了！

# Chapter 7 More on classes, constraints, and parameterization 第七章 关于类、约束条件以及参数化的更多内容

# (Or: More than you ever wanted to know!) （或者：比你想知道的一切还要多！）

Summary: 总结：

This chapter: 这一章：

• describes all the different sorts of Information Object Class Field that are available for use in a class definition; • 描述了在类定义中可以使用的各种信息对象类字段的类型；

describes the "variable syntax" for defining Information Objects (this is arguably the most important area covered in this chapter - read that material if you read nothing else); 文中描述了定义信息对象的“可变语法”。这可以说是本章中最重要的内容之一——如果你没有其他选择，那就务必阅读这部分内容。

• completes the discussion of constraints and of parameterization; • 完成了关于约束条件和参数化的讨论；

• describes the TYPE-IDENTIFIER built-in class; • 描述了内置类 TYPE-IDENTIFIER；

• completes the discussion of ASN.1 notational support for "holes". • 完成了关于 ASN.1 表示法对“空洞”处理的相关讨论。

## 1 Information Object Class Fields 1. 信息对象类别字段

There are many different sorts of information that generic protocol specifiers have found they wanted to collect from their users to complete their protocol, and ASN.1 allows the specification of a variety of different sorts of Information Object Class Field. Here we briefly look at each in turn. Figure II-21 gives an artificial example of an Information Object Class in which all the different sorts of field appear. 通用协议规范器们发现，他们需要从用户那里收集各种类型的信息来完善他们的协议。ASN.1 则允许定义多种不同类型的信息对象字段。下面我们将逐一介绍这些字段。图 II-21 展示了一个信息对象类的示例，其中包含了所有不同类型的字段。

There are many sorts of fields for Information Object Classes. Some are frequently used, some are rarely encountered. This clause lists them all! 信息对象类有多种不同的应用场景。有些应用非常常见，有些则比较少见。这一条列出了所有这些情况！

There are examples of all these different sorts of fields in current protocol specifications, but some are much more common than others. 在当前的协议规范中，有各种不同领域的例子，但其中有些领域比其他领域更为常见。

```txt
ILLUSTRATION ::= CLASS
    {&Type-field,
    &fixed-type-value-field INTEGER,
    &variable-type-value-field &Type-field,
    &Fixed-type-value-set-field My-enumeration,
    &Variable-type-value-set-field &Type-field,
    &object-field OPERATION,
    &Object-set-field ERROR }
Figure II-21: An illustration of the different sorts of field 
```

References to these fields such as 关于这些领域的参考，例如：

ILLUSTRATION.&fixed-type-value-field 插图与固定类型值字段

are possible in ASN.1 notation (constrained by an actual object set or unconstrained). Use of this notation is called information from object class. 这些定义在 ASN.1 表示法中是可以实现的（要么受限于某个实际的对象集，要么完全不受限制）。这种表示法被称为来自对象类的信息。

It is also in general possible to have references to fields of defined Information Objects and defined Information Object Sets using notation such as 通常也可以使用诸如“字段”之类的表达方式来指代定义好的信息对象或信息对象集。

illustration-object.&Type-field 插图对象。&类型字段

Illustration-object-set.&fixed-type-value-field 插图-对象集。&固定类型值字段

Use of this notation is called information from object and information from object set. 这种表示方式被称为“来自单个对象的信息”和“来自对象集的信息”。

In some cases, such notation is forbidden (see the Standard for a simple table of what is legal and what is not, and following text for a general description). A good guide, however, is if it makes some sort of sense, then it is legal. We discuss below the meaning and usefulness of these notations for each sort of field, and the circumstances in which you might want to use them. 在某些情况下，这种表示方式是被禁止的（请参阅标准文档，其中列出了哪些情况是合法的，哪些是不合法的）。不过，一个基本的判断标准是：如果这种表示方式有一定的意义，那么它就是合法的。我们在下文中会讨论这些表示方式对于每种字段的意义和实用性，以及在什么情况下应该使用它们。

## 1.1 Type fields 1.1 类型字段

The type field we have already encountered. The field-name has to start with a capital letter, and may be followed immediately by a comma, or we can write, for example: 我们已经遇到过“类型”这个字段了。字段名必须以大写字母开始，之后可以立即加上逗号，或者也可以这样写：

Type fields are common and important. They fill in the holes in protocols, and the need for them drove the development of the Information Object Class concept. 类型字段非常常见且重要。它们填补了协议中存在的空白，而对这些字段的需求促成了信息对象类概念的产生。

## &Type-field-optional OPTIONAL, &Type-field-defaulted DEFAULT NULL, &类型字段可选，&类型字段默认值为 NULL。

In the case of OPTIONAL, then that field may be left undefined when an Information Object of that class is defined. That field is then empty, and "empty" is distinct from any value that could be put into the field. The rules for applying an Information Object Set as a constraint say that a match occurs with an empty field only if the corresponding element in the SEQUENCE is missing. Thus it only makes sense to write OPTIONAL in the class definition if OPTIONAL also appears on the corresponding element (the "hole") in the type definition of the protocol. By contrast, DEFAULT places no requirements on the protocol, it merely provides the type to be used if none is specified in the definition of a particular information object. In the illustration above we have specified NULL. It could, of course, be any ASN.1 type, built-in or user-defined, but use of NULL with DEFAULT is the most common. 在 OPTIONAL 的情况下，当定义了此类信息对象时，该字段可以被定义为未定义状态。此时该字段为空，而“空”这个状态与可以赋予该字段的任何值都是不同的。关于如何将信息对象集作为约束条件的规则指出，只有当序列中的相应元素不存在时，才会发生与空字段的匹配。因此，只有在协议类型定义中对应的元素也出现 OPTIONAL 时，才在类定义中使用 OPTIONAL 是有意义的。相比之下，DEFAULT 并不对协议提出任何要求，它只是提供了一种在特定信息对象的定义中未指定其他类型时可以使用的类型。在上面的示例中，我们指定了 NULL。当然，它可以是任何 ASN.1 类型，无论是内置类型还是用户定义类型。不过，结合 DEFAULT 使用 NULL 是最常见的做法。

If we use the "information from object class" notation unconstrained, we have what is called an "open type". This really means an incomplete specification with no indication of who will provide, and where, the completion of the specification. Such use is not forbidden, but it should have been! Don't do it! Use with a simple table constraint is not much better, as the decoder has no way of knowing which of a set of types have been encoded, and without such knowledge encodings can be ambiguous. There is a special constraint that can be supplied to an "open type" called a type constraint. This was mentioned briefly in clause 8 of the last chapter. Here we might write 如果我们不使用任何约束条件，而是完全采用“对象类信息”的表示方式，那么就会得到一种被称为“开放类型”的规范。这实际上意味着一种不完整的规范，没有任何指示表明由谁来负责完成该规范。虽然这种使用方式并非被严格禁止，但实际上应该避免这样做！如果仅使用简单的表格约束来定义“开放类型”，情况也不会好到哪去，因为解码器无法知道哪些类型被编码了，而如果没有这样的信息，编码结果就会变得模糊不清。对于“开放类型”，还有一种特殊的约束条件可以施加，即类型约束。这一点在上一章的第 8 节中有简要提及。在这里，我们可以这样表述：

 

$$
\text { ILLUSTRATION. } \& \text { Type - field (My - type) }
$$

 

In terms of the semantics it carries, it is exactly equivalent to writing just "My-type", but it gets an extra length wrapper in PER, and is generally handled by tools as a pointer to a separate piece of memory rather than being embedded in the containing data-structure. It is useful if there are a number of places in the protocol that have some meta-semantics associated with them (such as types carrying security data), so that by writing as an element of a SEQUENCE or SET 从语义上讲，它等同于直接编写“My-type”。不过，它会在 PER 中额外加上一个长度描述符。通常，这种结构会被工具当作指向单独一块内存的指针来处理，而不是嵌入到包含它的数据结构中。如果协议中有多个地方包含某种元语义（例如，类型携带安全数据），那么这种写法就非常有用，因为可以将它作为序列或集合中的一个元素来使用。

 

$$
\text { SECURITY - DATA. \& Type - field (Data - type - 1) }
$$

 

you identify the element as the ASN.1 type "Data-type-1", but clearly flag it as a "SECURITY-DATA" type. 你将该元素识别为 ASN.1 类型“Data-type-1”，但实际上将其标记为“SECURITY-DATA”类型。

Use of "information from object set" for a type field is illegal. This would in general produce a set of ASN.1 types (one from each of the objects in the object set), and there is nowhere in ASN.1 where you can use a set of types. 在类型字段中使用“来自对象集的信息”这一表述是不合法的。通常来说，这会产生一组 ASN.1 类型（每个对象类型对应一个类型），而在 ASN.1 标准中，并没有规定可以使用这样的类型集合。

Use of "information from object" for a type field produces a single type, and an alternative to the previous SEQUENCE or SET element using "Data-type-1" could in suitable circumstances be 在类型字段中使用“来自对象的信息”可以生成一种单一的类型。在适当的情况下，这种类型可以替代之前使用的“序列”或“集合”元素，采用“数据类型 1”来表示。

 

$$
\text { object1. } \& \text { Type - field }
$$

 

with 随着

$$
\begin{array}{l} \text {object1} \quad \text {SECURITY - DATA}:: = \\ \{\& \text {Type - field} \quad \text {Data - type - 1}, \\ \text {etc} \} \end{array}
$$

Note that this latter construction flags Data-type-1 as a SECURITY-DATA type, but it does not produce the encapsulation that the earlier construct produced. Use of "object1.&Type-field" produces exactly the same encoding as use of "Data-type-1" would produce. 需要注意的是，后一种构造方式将“Data-type-1”标记为安全性数据类型，但它并不能产生与之前构造方式相同的封装效果。使用“object1.&Type-field”所产生的编码结果，实际上与使用“Data-type-1”所产生的编码结果是完全相同的。

## 1.2 Fixed type value fields 1.2 固定类型值字段已修复

The names of these fields are required to begin with a lower-case letter, and the name is required to be followed by an ASN.1 type which specifies the type of the value that has to be supplied for that field. It is again permissible to include OPTIONAL and DEFAULT in this specification, and also UNIQUE (as described in the last chapter). 这些字段的名称必须以小写字母开头，名称之后需要加上 ASN.1 类型，该类型用于指定该字段所包含的值的类型。在这个规范中，也可以包含 OPTIONAL 和 DEFAULT 属性，此外还有 UNIQUE 属性（如最后一章中所描述的那样）。

Closely linked to type fields, these are again frequently encountered. 这些内容与类型字段密切相关，因此也经常会被遇到。

The most common types for these fields are INTEGER or OBJECT IDENTIFIER or a choice of the two, but BOOLEAN or an ENUMERATED type are also quite common. The latter two are used when the information being collected is not designed to be carried in a protocol message, but rather completes a "hole" in the procedures. 这些字段最常见的类型包括 INTEGER、OBJECT IDENTIFIER，或者其中的一种组合。不过，BOOLEAN 或 ENUMERATED 类型也很常见。当收集的信息不适合通过协议消息传递时，就会使用后两种类型。在这种情况下，这些类型可以填补程序中的空白。

For example, to take our ROSE example again, suppose that we allow the possibility that for some operations "ReturnResult" carries no information. This could be handled by putting OPTIONAL in the class definition of OPERATION.&ResultType, and also on the "hole" element of the "ReturnResult" SEQUENCE. However, we may want to go further than that. In cases where there is no result type, we may want to specify that, for some non-critical operations, the "ReturnResult" is never sent (a "Reject" or "ReturnError" will indicate failure), for others it must always be sent as a confirmation of completion of the operation, and for still others it is an option of the remote system to send it or not. In this case the fixed type value field might read: 例如，再次以 ROSE 为例。假设某些操作情况下“ReturnResult”并不包含任何信息。这可以通过在 OPERATION 类的定义中使用 OPTIONAL 属性来实现，同时也可以在“ReturnResult”序列的“hole”元素上设置此属性。然而，我们可能希望更进一步考虑这种情况。在某些没有结果类型的情况下，我们可能需要规定：对于某些非关键性的操作，“ReturnResult”根本不会被发送（此时会返回“Reject”或“ReturnError”来表示失败）；而对于其他操作，则必须始终发送“ReturnResult”作为操作完成的确认；还有一些情况，远程系统可以选择是否发送“ReturnResult”。在这种情况下，“ReturnResult”的固定类型值字段可能如下所示：

## &returnResult ENUMERATED {always, never, optional} DEFAULT always, &返回结果可以是以下枚举值：always、never、optional。默认值为 always。

and the ROSE user would specify a value of "never" or "optional" for operations where this was the required behaviour. 对于需要这种行为的操作，ROSE 用户可以指定“从不”或“可选”的值。

The use of the "information from object class" construct in this case produces simply the type of the fixed type value field. So use of 在这种情况下，使用“来自对象类的信息”结构只会返回固定类型的值字段的类型。因此，只需使用该结构即可。

 

$$
\text { ILLUSTRATION. } \& \text { fixed - type - value - field }
$$

 

is (almost) exactly equivalent to writing 几乎相当于直接书写出来

## INTEGER 整数

The difference is that you cannot apply a table constraint with an object set of class ILLUSTRATION to the type INTEGER. You can apply it (and frequently do) to the "information from object class" construct. 区别在于，你无法将表约束应用于\`ILLUSTRATION\`类对象类型的\`INTEGER\`类型。不过，你可以将表约束应用于“来自对象类的信息”结构，而且通常也是这么做的。

Both "information from object" producing (in this illustration) a single integer value and "information from object set" producing a set of integer values (a subset of type integer) are allowed in this case. Thus with an object set "Illustration-object-set" of class ILLUSTRATION, we could write 在这种情况下，允许使用一种方式是从单个对象中获取信息，这种方式会返回一个整数值；另一种方式则是从一组对象中获取信息，这组对象会返回一组整数值（属于整数类型的子集）。因此，以“Illustration-object-set”这类对象作为示例，我们可以写成这样的表达式：

 

$$
\text { Illustration - object - set. } \& \text { fixed - type - value - field }
$$

 

instead of 而不是

## ILLUSTRATION.&fixed-type-value-field (Illustration-object) 插图与固定类型值字段（插图对象）

What is the difference? Not a lot! In the latter case, you could use "@" with a relational constraint (on a type field of class ILLUSTRATION) to point to this element. In the former case you could not. The latter is what you will normally see. 有什么区别呢？其实并没有太大的差异！在后一种情况下，你可以使用“@”符号，并结合关系约束（针对 ILLUSTRATION 类的类型字段），来指向这个元素。而在前一种情况下，则无法使用这种符号。通常，我们会看到后一种情况的应用。

## 1.3 Variable type value fields 1.3 变量类型的值字段

This is probably the second least common sort of field. Its main use is to provide a default value for a type that is provided in a type field. 这大概是第二种较为少见的字段类型了。它的主要用途是为某个类型字段提供一个默认值。

<table><tbody><tr><td data-imt-p="1">Much less common. An interesting example of a theoretically useful concept! 比较少见。不过，这确实是一个在理论上很有用的有趣例子！</td></tr></tbody></table>

The field name is followed by the name of some type field (&T-F say) defined in this class definition. The value supplied for the variable type value field in the definition of an information object of this class is required to be a value of the type that was supplied for the &T-F field. 该字段名称之后是该类定义中定义的某种类型字段的名称（例如&T-F）。在定义该类的信息对象时，为变量类型字段提供的值必须属于与&T-F 字段相同类型。

This field can be marked OPTIONAL or DEFAULT, but there are then rules that link the use of OPTIONAL and DEFAULT between this field and the field &T-F. Roughly, if it makes sense it is allowed, if it doesn't it is not! Check the Standard (or use a tool to check your ASN.1) if you are unsure what is allowed and what is not. Roughly, both this field and &T-F must have, or not have, the same use of OPTIONAL or DEFAULT, and in the latter case, the default value for this field must be a value of the default type for the &T-F field. 这个字段可以标记为 OPTIONAL 或 DEFAULT，但有一些规则规定了如何结合使用 OPTIONAL 和 DEFAULT 属性。大致来说，如果某个值合理，就可以使用该属性；如果不合理，则不能使用。如果你不确定哪些值是允许的、哪些是不允许的，可以参考标准规范（或者使用工具来检查你的 ASN.1 描述）。此外，这个字段和&T-F 字段都必须使用相同的 OPTIONAL 或 DEFAULT 属性，如果使用了后者，那么这个字段的默认值就必须是&T-F 字段的默认类型值。

As you would expect for a field which holds a single value, the field-name has a lower-case letter following the "&". 正如你所预期的那样，对于一个只包含一个值的字段来说，字段名称应该以小写字母开头，后面跟着“&”符号。

The use of "Illustration-object-set.&variable-type-value-field" is forbidden (not legal ASN.1). The use of "illustration-object.&variable-type-field" produces the value assigned to that field. 禁止使用“Illustration-object-set.&variable-type-value-field”这种表达方式（不符合合法的 ASN1 规范）。如果使用“illustration-object.&variable-type-field”，则只会得到该字段所赋的值。

## 1.4 Fixed type value set fields 1.4 已修复固定类型的值设置字段问题

These are fields that hold a set of values of a fixed type, and hence the field-name starts with an upper-case letter after the ampersand. 这些字段存储的是固定类型的值集合，因此这些字段的名称在通配符之后以大写字母开头。

Quite frequently used, mainly where we need to fill in holes in the procedures of a protocol, and have a list (an enumeration) of possible actions, some of which need to be selected and others forbidden. 这种方法被广泛使用，主要用于填补协议流程中的空白之处。需要列出所有可能的操作选项，其中一些是可选的，而另一些则被禁止。

The information required here is a set of values of the type following the field-name (the governor type), or in other words, a subset of that type. These values can be supplied either by a typereference to a type which is the governor type with a simple subtype constraint applied it, or can be supplied using the value-set notation described in the last chapter. 这里需要的信息是一组符合字段名称后边的类型定义的值，换句话说，就是该类型的一个子集。这些值可以通过对作为父类型的类型进行类型引用来提供，同时还需要施加简单的子类型约束；或者，也可以使用在上一章中描述的数值集表示法来提供这些值。

The most common occurrence of this field is where there are a number of possibilities, and the definer of an Information Object is required to select those that are to be allowed for this Information Object. 这个领域最常见的情形是，存在多种可能性，此时需要确定该信息对象的定义者来选择那些被允许使用的可能性。

Thus, in a class definition: 因此，在一个类定义中：

```txt
&Fixed-type-value-set-field
ENUMERATED {confirm-by-post, confirm-by-fax,
    confirm-registered, confirm-by-e-mail
    confirm-by-phone}, 
```

might be used to let the user specify that, for some particular information object, some subset of the enumeration possibilities can be used. It is left to the reader's imagination to flesh out the above definition into a real fictitious scenario! 这个特性可以用来让用户指定：对于某些特定的信息对象，可以使用其中的一部分枚举选项。至于如何将上述定义具体化为一个真实的虚构场景，则取决于读者的想象力了！

Extraction of information from both objects and object sets using this field both produce a (sub)set of values of the type used in the class definition, containing just those values that appear in any of the objects concerned. 通过此字段从对象及其集合中提取信息，可以得到一个包含与类定义中使用的类型相匹配的值的（子）集合。这个集合中只包含那些出现在相关对象中的值。

## 1.5 Variable type value set fields 1.5 变量类型值用于设置字段

I (the author of this text!) am not at all sure that this sort of field does actually occur in practice. It was added largely because it seemed to be needed to "complete the set" of available sorts of field! Find a good use for it! 我（这篇文的作者）并不确定这种字段在实际情况中是否真的存在。之所以添加这种字段，主要是因为觉得有必要“完善”现有的字段种类吧！希望能找到它的合理用途。

In this box I can say "this has never been used!". In the body of the text I am more cautious! 在这个框里，我可以填写“这个从未被使用过！”。而在文本主体部分，我则会更加谨慎一些！

It begins with an upper-case letter, and the field-name is followed by the name of some type field (&T-F) in the same class definition. The field is completed by giving a set of values (a subset) of the type that is put into &T-F. 这个字段以一个大写字母开头，之后是字段名称，接着是同一类定义中某种类型字段的名称。该字段通过给出该类型的一组值来完整描述，这些值属于该类型的一个子集。

Extraction of information from an object gives the value assigned to that field, but notation to extract information from an object set is illegal for this field type. 从某个对象中提取信息会为该字段赋予相应的价值，但针对这种字段类型，从对象集合中提取信息的表示方法是不合法的。

## 1.6 Object fields 1.6 对象字段

Perhaps surprisingly, this is less common than the object set field described below, but it is used. 或许令人惊讶的是，这种用法比下面提到的“对象集字段”要少见一些，但依然被使用。

The object field carries the identification (an information object reference name) of some object of the class that follows the field name. 该对象字段携带了与字段名称对应的类中的某个对象的标识（即信息对象引用名称）。

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/54379e17-c034-430b-894c-f77661f731e5/82be3e32aad5fc93c00ad9efa888e80cb54f2c3cdc9d2b59bfb0cf2fbe169555.jpg)

This is the object-and-class equivalent of the fixed type value field. 这是对象与类级别的固定类型值字段的等价物。

Its main use is to help in the structuring of information object definitions. If every object of one class (MAIN-CLASS say) is going to require certain additional information to be specified which would add a number of fields to MAIN-CLASS (and if the same additional information is likely to be specified frequently for different objects of MAIN-CLASS) then it makes sense to define a separate class (ADDITIONAL-INFO-CLASS say). Objects of ADDITIONAL-INFO-CLASS carry just the additional information, and references to them are included in an object field of MAIN-CLASS. 它的主要用途是帮助构建信息对象的定义。如果某个类（比如 MAIN-CLASS）中的每个对象都需要指定某些额外的信息，那么这就会为 MAIN-CLASS 增加一些字段。而且，如果同样的额外信息需要为 MAIN-CLASS 中的不同对象反复指定，那么定义一个单独的类（比如 ADDITIONAL-INFO-CLASS）就很有意义了。ADDITIONAL-INFO-CLASS 中的对象只包含额外的信息，而对这些信息的引用则会被包含在 MAIN-CLASS 的某个对象字段中。

Information from an object and from an object set produces a single object or a set of objects respectively. Use of these constructions is mainly useful if we have two classes defined that are closely related (the Directory OPERATION-X and CHAINED-OPERATION-X are examples), with one having the fields of the other as a subset of its fields. In this case it can avoid "fingertrouble" in the definition (and provide a clearer specification) if objects defined for CHAINED-OPERATION-X have the fields that correspond to OPERATION-X defined by extracting information from the corresponding OPERATION-X object, rather than repeating the definition over again. (This point actually applies to the use of information from object for all the different sorts of field.) 从一个对象中获取的信息会对应生成一个独立的对象；而从一组对象中获取的信息则对应生成一组对象。这种构造方式在以下情况下非常有用：当我们有两个紧密相关的类时（例如 Directory OPERATION-X 和 CHAINED-OPERATION-X），其中一个类的字段是另一个类的字段的子集。这样一来，就可以避免定义时的重复劳动（通过从相应的 OPERATION-X 对象中提取字段信息来定义 CHAINED-OPERATION-X 中的对象），从而提供更清晰的规范。实际上，这一点适用于所有需要使用对象信息的情况。

## 1.7 Object set fields 1.7 对象设置字段

We have already seen this in use to list the errors associated with an operation. As expected for something that is a set of objects, the & is followed by an upper-case letter. 我们已经看到这种用法，它用于列出与某个操作相关的错误。正如预期的那样，对于一组对象来说，&后面会跟着一个大写字母。

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/54379e17-c034-430b-894c-f77661f731e5/1ccdf5e6f929fbb27707a243fef4077073b18378fe72a03ccde7f772a1651715.jpg)

Information from object and from object set is again permitted, with the obvious results. 再次允许获取单个对象的信息以及对象集合的信息，所带来的效果非常明显。

## 1.8 Extended field names 1.8 扩展的字段名称

When you are referencing fields of a class, object, or object set, you may end up with something that is itself a CLASS or object or object set (for example, OPERATION.&Errors delivers the ERROR class). When this happens, you are able to add a further "." (dot) followed by a field-name of the class you obtained. 当您引用某个类、对象或对象集的字段时，最终可能会得到另一个类或对象（例如，OPERATION.&Errors 会返回 ERROR 类）。在这种情况下，您可以再添加一个点 "."，然后跟上该类的字段名称。

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/54379e17-c034-430b-894c-f77661f731e5/11978dc52e3176e9c15a1df4f9325167713b6f19473e0396bc50b272e70e663c.jpg)

Thus 因此，就是如此。

OPERATION.&Errors.&ParameterType 操作、错误与参数类型

and 以及

OPERATION.&Errors.&errorCode 操作、错误及错误代码

are valid notations, and are equivalent to: 这些都是有效的表示方式，且等价于以下内容：

and 以及

ERROR.&ParameterType 错误。&参数类型

ERROR.&errorCode 错误。&errorCode

Similar constructions using an information object set of class OPERATION are more interesting. 使用 OPERATION 类的信息对象集进行类似构建的方式更为有趣。

Here 这里

My-ops.&Errors.&errorCode 我的操作。&错误。&错误代码

delivers the set of values that are error codes for any of the operations in "My-ops", and 在“我的操作”中，会传递出所有操作的错误代码所对应的数值集，以及……

my-look-up-operation.&Errors.&errorCode 我的查询操作。&错误。&错误代码

delivers that set of values that identify the possible errors of "my-look-up-operation". 传递了那组价值观，这些价值观定义了“我的查询操作”可能产生的错误。

Of course, this can proceed to any length, so if we have an object set field of class OPERATION that is itself a set of objects of class OPERATION (this does actually occur in ROSE - the field is called "&Linked" and records so-called "linked operations"), we can write things like: 当然，这种情况可以持续下去。因此，如果我们有一个属于 OPERATION 类的对象集合，而这个集合本身又是由 OPERATION 类的对象构成的集合（实际上在 ROSE 中确实存在这种情况——这个集合被称为“&Linked”，它记录了所谓的“链接操作”）。那么我们可以写出类似这样的代码：

my-op.&Linked.&Linked.&Linked.&Linked.&Errors.&errorCode 我的操作出现了错误。错误代码：errorCode

This stuff is utterly fascinating - yes? But the reader is challenged to find a real use for it! (To be fair to ASN.1, these sorts of notation come out naturally if one wants consistency and generality in the notation, and cost little to provide. It is better that they are allowed than that what are fairly obvious notations be disallowed.) 这东西真是太有趣了，对吧？不过，读者需要自己找出它的实际用途呢！（公平地说， ASN.1 的规范之所以采用这种表示方式，是因为希望在整个规范中保持一致性和通用性，而且这种表示方式在实现起来也相当简单。与其禁止使用那些显而易见的表示方式，不如允许使用这种方式更为明智。）

## 2 Variable syntax for Information Object definition 2 种用于定义信息对象的变量语法结构

Historically, before the concept of Information Object Classes was fully-developed, an earlier feature of ASN.1 (now withdrawn), the so-called macro notation, was used by ROSE (and others) to provide users with a notation for defining the 从历史来看，在“信息对象类”这一概念完全成熟之前，ASN.1 协议中有一个更早的功能（现已不再使用），即所谓的宏注释方式。当时，ROSE 等工具使用这种注释方式来为用户定义各种对象。

A few techies define information object classes, but a lot of users define objects of those classes, and even more (non-techie) people read those definitions. We need a human-friendly notation to define objects of a given class. "Variable syntax" is important and much used. 有一些技术专家负责定义信息对象类，但有很多用户自己来定义这些类的对象。还有更多的人（非技术人士）阅读这些定义。我们需要一种易于理解的符号来表示某个类中的对象。“可变语法”非常重要，而且被广泛使用。

information needed to fill in the holes in their protocols. The notation that ROSE (and others) provided was quite human-friendly. It certainly did not contain the "&" character, and often did not contain any commas! It frequently read like an English sentence, with conjunctions such as "WITH" being included in the notation, or as a series of keyword-value pairs. 这些信息对于填补协议中的空白是必要的。ROSE（以及其他系统）所使用的表示方式非常易于理解。这种表示方式确实没有使用“&”符号，而且通常也不使用逗号。这种表示方式常常看起来像一句英文句子，其中包含了诸如“与”这样的连词，或者由一系列关键词-值对组成。

For example, to define a ROSE operation, you would write: 例如，要定义一种 ROSE 操作，你可以这样编写：

```txt
my-op OPERATION
    ARGUMENT Type-for-my-op-arg
    RESULT Type-for-my-op-result
    ERRORS {error1, error4}
::= local 1 
```

(In the following text, we call this the ad-hoc-notation.) （在接下来的文本中，我们将其称为“临时标记法”。）

This was ad-hoc-notation defined by ROSE. (Other groups would define similar but unrelated syntax - in particular, some used comma to separate lists of things, others used vertical bar). 这是一种由 ROSE 定义的临时标记方式。（其他团队也会使用类似的但不同的语法结构——例如，有些团队用逗号来分隔列表项，而另一些团队则使用竖线来表示分隔。）

It is important to note here that when this syntax was provided (in advance of the Information Object Class concept) there was little semantics associated with it. The above notation formally (to an ASN.1 tool) was nothing more than a convoluted syntax for saying: 需要注意的是，在“信息对象类”概念出现之前，当这种语法被提出时，其实并没有相关的语义说明。上述表示法对 ASN.1 工具来说，只不过是一种复杂的语法结构，用来表达某种含义而已。

```txt
my-op CHOICE {local INTEGER, global OBJECT IDENTIFIER} ::= local:1 
```

and typically the value reference "my-ops" was never used anywhere. A lot of information was apparently being collected, but was then "thrown on the ground" (in terms of any formal model of what the text meant). 通常，那个所谓的“my-ops”这个值根本没有被任何地方使用过。显然，有很多信息被收集起来，但这些信息随后就被“扔掉了”（也就是说，那些信息并没有被纳入到任何关于这些文本意义的正式模型中）。

(As an aside, the inclusion of the ":" (colon) above after "local" is not fundamental to this discussion - it resulted from the fact that a choice value was expressed in early work as (eg) "local 1" and post-1994 as "local:1"). （顺便说一下，在“local”之后加上“:”符号并不是这一讨论的核心内容——实际上，之所以要加上这个符号，是因为在早期的工作中，选项的值被表示为“local 1”，而自 1994 年之后则改为“local:1”。）

The above notation was, however, designed really to serve the same purpose that you would get today with the object definition: 不过，上述符号表示方式其实也是为了达到与今天通过对象定义所实现的功能相同的目的：

```txt
my-op OPERATION ::=
    {&operationCode local:1,
    &ArgumentType Type-for-my-op-arg,
    &ResultType Type-for-my-op-result,
    &Errors {error1 | error4} } 
```

(We call this below the object-definition-notation.) （我们在对象定义与符号之下进行这样的处理。）

We can observe a number of things. First, the ad-hoc-notation is probably easier for a human to read than the object-definition-notation, although the lack of a clear semantic under-pinning would confuse more intelligent readers! Second, because the notation was ad hoc, it was very difficult to produce any tool support for it. Third, because the notation was ad hoc, a tool had no means of knowing when this ad hoc notation terminated and we returned to normal ASN.1 (there were no brackets around the ad-hoc-notation). Finally, there was no formal link (such as we get by using an Information Object Set as a constraint) between use of this notation and holes in the ROSE protocol. 我们可以观察到一些特点。首先，这种临时性的标记方式可能比对象定义式标记更容易被人理解；不过，由于缺乏明确的语义基础，这会让更聪明的读者感到困惑。其次，由于这种标记方式是临时性的，因此很难为此开发相应的工具来支持其使用。第三，由于这种标记方式是临时性的，因此没有工具能够判断这种临时标记何时结束，从而回到正常的 ASN.1 标准（在临时标记周围没有括号）。最后，这种标记方式与 ROSE 协议中的漏洞之间没有任何形式的关联（比如通过以信息对象集作为约束条件来实现关联）。

Nonetheless, when the Information Object Class material was introduced into ASN.1 (and the use of macro notation withdrawn) in 1994, it was felt important to allow a more human-friendly (but still fully machine-friendly, and with full semantics) notation for the definition of objects of a given class. 不过，当在 1994 年将“信息对象类”相关的规范引入到 ASN.1 中时（同时不再使用宏表示法），人们认为有必要提供一种更易于人类理解的表示方式来表示特定类别的对象。当然，这种表示方式仍然完全符合机器处理的要求，并且具有完整的语义表达能力。

The aim was to allow definers of a class to be able to specify the notation for defining objects of that class which would let them get as close as possible (without sacrificing machineprocessability) to the notation that had hitherto been provided as ad-hoc notation. The "variable syntax" of ASN.1 supports (fulfills) this aim. 我们的目标是让一个类的定义者能够指定该类对象的表示方式，这样就能在不过度牺牲机器处理能力的前提下，尽可能接近以往所使用的临时表示方法。ASN.1 中的“变量语法”正是为了实现这一目标的工具。

Variable syntax requires that a class definition is immediately followed by the key words "WITH SYNTAX" followed by a definition of the syntax for defining objects of that class. If those keywords are not present following the class definition, then the only available syntax for defining objects is the object-definition-notation. (The latter can still be used by users defining objects even if there is a "WITH SYNTAX" clause.) 可变语法要求，在类定义之后必须紧接着出现“WITH SYNTAX”这个关键词，然后才是对该类对象进行定义的语法说明。如果类定义之后没有出现这些关键词，那么唯一可用的对象定义语法就是对象定义符号法。（即使存在“WITH SYNTAX”条款，用户仍然可以使用对象定义符号法来定义对象。）

Figure II-22 adds WITH SYNTAX to the OPERATION class definition. (Again we must emphasise that the real ROSE specification is a little more complex than this - we are not producing a full tutorial on ROSE!) 图 II-22 将“WITH SYNTAX”这一语法添加到“OPERATION”类的定义中。同样需要强调的是，真正的 ROSE 规范其实比这要复杂得多——我们并不打算编写关于 ROSE 的完整教程！

```txt
OPERATION ::= CLASS
    { &operationCode CHOICE {local INTEGER,
    global OBJECT IDENTIFIER}
    UNIQUE,
    &ArgumentType,
    &ResultType,
    &Errors ERROR OPTIONAL }
WITH SYNTAX
    { ARGUMENT &ArgumentType
    RESULT &ResultType
    [ERRORS &Errors]
    CODE &operationCode } 
```

What is this saying/doing? It allows an object of class operation to be defined with the syntax: 这到底是什么意思/做什么呢？它允许使用以下语法来定义一个操作类的对象：

```txt
my-op OPERATION ::=
{ ARGUMENT Type-for-my-op-arg
RESULT Type-for-my-op-result
ERRORS {error1 | error4}
CODE local:1 } 
```

The reader will notice the disappearance of the unsightly "&", the strong similarity between this and the ad-hoc-notation, but also the presence of curly brackets around the definition, needed to maintain machine-processability. 读者会注意到，那些难看的“&”符号已经消失了。这种表示方式与特定场合使用的符号非常相似。此外，定义部分还使用了花括号来表示，这样做是为了保持机器可处理性。

What can you write following "WITH SYNTAX"? Roughly you have the power normally used in defining command-line syntax - a series of words, interspersed with references to fields of the class. In defining an object, the definer must repeat these words, in order, and give the necessary syntax to define any field that is referenced. Where a sequence of words and/or field references are enclosed in square brackets (as with "\[ERRORS &Errors\]" above), then that part of the syntax can be omitted. (Of course, the inclusion of the square brackets was only legal in the definition of the "WITH SYNTAX" clause because "&Errors" was flagged as "OPTIONAL" in the main class definition.) 在“WITH SYNTAX”之后，可以编写以下内容。大致上，你可以使用通常用于定义命令行语法的方式——即一系列单词，同时包含对类中各个字段的引用。在定义对象时，定义者必须按顺序重复这些单词，并提供必要的语法来定义任何被引用的字段。当一系列单词和/或字段引用被放在方括号中时（如上面的“\[ERRORS &errors\]”），那么这部分语法可以省略。（当然，只有在“WITH SYNTAX”子句的定义中，才允许使用方括号，因为“&errors”在类定义中被标记为“可选项”。）

A "word" for the purpose of the WITH SYNTAX clause is defined as a sequence of upper-case (not lower-case) letters (no digits allowed), possibly with (single) hyphens in the middle. 在 WITH 语法中，所谓的“词”被定义为由大写字母组成的序列（不允许使用小写字母），中间可以包含一个或多个连字符。

It is also possible to include a comma (but no other punctuation) in the WITH SYNTAX clause, in which case the comma has to appear at the corresponding point in the definition of an object of that class. 在“WITH SYNTAX”子句中，也可以包含一个逗号（但不需要其他标点符号）。在这种情况下，这个逗号必须出现在该类对象的定义中的相应位置。

Square brackets can be nested to produce optional sections within optional sections. However, there are some quite severe restrictions on the use of "WITH SYNTAX" which are designed both to prevent the apparent acquisition of information with no effect on the actual object definition, and also to ensure easy machine-processability. Writers of a WITH SYNTAX clause should read the Standard carefully. Figure II-23 would, for example, be illegal. 方括号可以嵌套使用，从而在更细小的部分中设置可选内容。不过，对于“WITH SYNTAX”这种语法结构的使用有一些相当严格的规定。这些规定的目的是防止随意获取信息而不会影响实体的实际定义，同时也确保了语句能够被机器轻松处理。编写“WITH SYNTAX”子句的开发者应当仔细阅读相关标准。例如，像图 II-23 这样的结构就是不合法的。

```txt
OPERATION ::= CLASS
    { &operationCode CHOICE {local INTEGER,
    global OBJECT IDENTIFER}
    UNIQUE,
    &ArgumentType,
    &ResultType,
    &Errors ERROR OPTIONAL }
WITH SYNTAX
    { ARGUMENT &ArgumentType
    RESULT &ResultType [REQUIRED]
    [ERRORS &Errors]
    CODE &operationCode }

Figure II-23: Illegal specification of WITH SYNTAX 
```

```txt
OPERATION ::= CLASS
    { &operationCode CHOICE {local INTEGER,
    global OBJECT IDENTIFIER}
    UNIQUE,
    &ArgumentType,
    &ResultType,
    &ReturnsResult ENUMERATED
    {does, does-not},
    &Errors ERROR OPTIONAL }
WITH SYNTAX
    { ARGUMENT &ArgumentType
    RESULT &ResultType
    &ReturnsResult RETURN-RESULT
    [ERRORS &Errors]
    CODE &operationCode } 
```

This is because it allows the definer of an object to provide information by inclusion or not of the word "REQUIRED" which is nowhere recorded in a field of the object. If it is desired to let the definer of an object specify whether the return of a result is required or not, the definition of figure II-24 could be used, allowing: 这是因为，通过这种方式，对象的定义者可以通过是否包含“REQUIRED”这个词来提供相关信息，而这个词在对象的任何字段中都没有被记录。如果希望让对象的定义者能够指定是否需要返回某个结果，那么可以使用图 II-24 的定义方式来实现这一点。

```makefile
my-op OPERATION ::=
{ ARGUMENT Type-for-my-op-arg
RESULT Type-for-my-op-result
does-not RETURN-RESULT
ERRORS {error1 | error4}
CODE local:1 } 
```

Finally, we try to provide a tabular notation for the compact definition of a an object of class OPERATION similar to the table defined originally in Figure II-14. This is shown in figure II-25. 最后，我们试图为 OPERATION 类对象的简洁定义提供一种表格形式的表现方式，类似于图 II-14 中最初定义的表格。该表格形式如图 II-25 所示。

```txt
OPERATION ::= CLASS
    { &operationCode CHOICE {local INTEGER,
    global OBJECT IDENTIFER}
    UNIQUE,
    &ArgumentType,
    &ResultType,
    &Errors ERROR OPTIONAL }
WITH SYNTAX
    { &operationCode
    &ArgumentType
    &ResultType
    [&Errors]
    } 
```

With the definition in figure II-24 we would be allowed to write (compare figures II-14 and II-17): 根据图 II-24 中的定义，我们可以这样书写（参见图 II-14 和图 II-17）：

```txt
My-ops OPERATION ::=
{ {asn-val-order Order-for-stock Order-confirmed
    {security-failure
    | unknown-branch} }
| {asn-val-sales Return-of-sales NULL {security-failure
    | unknown-branch} }
| {asn-val-query Query-availability Availability-response
    {security-failure
    | unknown-branch
    | unavailable } }
| {asn-val-state Request-order-state Order-state {security-failure
    | unknown-branch
    | unknown-order } } 
```

So we have now come full circle! The informal tabular presentation we used in figure II-14 was replaced with the formal but more verbose definition of figure II-17, which (using WITH SYNTAX) can be replaced with syntax very like that of figure II-14. 现在，我们终于回到了原点！在图 II-14 中使用的非正式表格形式，已经被图 II-17 中更为正式且详细的定义所取代。而图 II-17 中的定义，通过采用类似图 II-14 的语法结构，也可以被重新用图 II-14 的语法形式来表示。

It should by now be clear to the reader that WITH SYNTAX clauses should be carefully considered. Not only must the rules of what is legal be understood, but what is a good compromise between verbosity and intelligibility in the final notation has to be determined. As with all human interface matters, there is no one right decision, but a little thought will avoid bad decisions! 现在读者应该已经明白，对于语法规则必须予以高度重视。不仅要了解各种规则的规定，还要确定在保持简洁性的同时，如何达到最佳的可读性。就像所有与人类界面相关的问题一样，并没有一种绝对正确的解决方案，但稍加思考就能避免错误的决策！

## 3 Constraints re-visited - the user-defined constraint 重新审视了 3 个约束条件——即用户自定义的约束条件。

There is not a lot to add on constraints. We have covered earlier all the simple sub-type constraints, and in the last chapter the table and relational constraints. There is just one other form of constraint to discuss, the so-called user-defined constraint. 关于约束条件，其实没有太多需要补充的内容。之前我们已经讨论了所有简单的子类型约束条件，而在最后一章中则探讨了表和关系约束条件。现在还有一种约束条件需要讨论，那就是所谓用户定义的约束条件。

```txt
User-defined constraints - little more than a comment! Why bother? 
```

We discussed above the earlier availability of a notation (the macro notation) that allowed people to define new ad-hoc-notation (with no real semantics) for inclusion in an ASN.1 module. When this "facility" was removed in 1994, it turned out that the Information Object concept did not quite cover all the requirements that had been met by use of this macro notation, and the user-defined constraint concept was introduced to meet the remaining requirements. This form of constraint would probably not have been introduced otherwise, as it is little more than a comment, and tools can make little use of it. It is almost always used in connection with a parameterised type, introduced in clause 9 of II-6. 我们在上面讨论了之前存在的某种标记方式（即宏标记），这种标记方式允许人们定义新的临时标记，这些标记在 ASN.1 模块中可以被使用，但并没有实际的语义含义。当这种“功能”在 1994 年被移除时，我们发现信息对象的概念并不能完全满足使用宏标记时所需要满足的所有要求。因此，人们引入了用户定义的约束概念来满足剩余的需求。不过，这种约束形式可能原本并不会被引入，因为它只不过是一种注释而已，而且各种工具也很少会使用它。这种约束方式几乎总是与参数化类型一起使用，具体信息可以在 II-6 的第 9 条中找到。

One piece of ad-hoc-notation that was defined using the macro notation was the ability to write: 一种使用宏注释定义的特殊注释方式就是能够这样书写：

 

$$
\text { ENCRYPTED My - type }
$$

 

as an element of a SET or SEQUENCE. 作为集合或序列中的一个元素。

Although not implied by the ASN.1 formal text, this actually meant that the element was a BITSTRING, whose contents were an encryption (according to an encryption algorithm specified in English text) of the encoding of the type My-type. 虽然 ASN.1 官方文档中没有明确说明这一点，但实际上这意味着该元素是一个比特串，其内容是根据某种加密算法对类型为“My-type”的编码进行加密后的结果。

We can get slightly more clarity if we define a parameterised type "ENCRYPTED" as : 如果我们把一种参数化类型“ENCRYPTED”定义为如下形式，那么就能更清楚地理解其含义了：

and then use 然后使用它

```txt
ENCRYPTED {My-type} 
```

as the SEQUENCE or SET element. 作为序列或集合中的元素。

(Note that we violate convention, but not the rules of ASN.1 by using all capitals for the ENCRYPTED type. This is for reasons of historical compatibility with the original ad-hocnotation "ENCRYPTED My-type". Note also that the new formal notation includes a new pair of curly brackets, as we saw - for a slightly different reason - with the move from ad-hoc-notation to object-definition-notation.) （请注意，虽然我们违反了常规做法，但并未违反 ASN1 的规范。我们使用全部大写字母来表示“ENCRYPTED”类型，这一做法是为了与原始的非正式标记“ENCRYPTED My-type”保持历史上的兼容性。另外，新的正式标记格式中使用了新的花括号配对方式——这与从非正式标记转换为对象定义标记时采用的方式略有不同。）

The above avoided the use of an ad-hoc-notation, but it is curious for the dummy parameter of "ENCRYPTED" not to be used at all on the right-hand side of the assignment. It is clear that the actual value of the BITSTRING will depend on the "Type-to-be-encrypted" type (and also on the encryption algorithm and keys, which we cannot define using ASN.1). 上述描述中避免了使用特定于情况的注释。不过，有趣的是，在赋值语句的右侧，竟然完全没有使用“ENCRYPTED”这个伪参数。显然，BITSTRING 的实际值取决于“待加密类型”这一参数（同时也取决于加密算法和密钥，而这些内容是无法通过 ASN.1 格式来定义的）。

So we introduce the user-defined constraint. In its basic form, we would write: 因此，我们介绍用户自定义约束条件。在其基本形式下，我们可以这样表述：

```txt
ENCRYPTED {Type-to-be-encrypted} ::= BITSTRING
(CONSTRAINED BY {Type-to-be-encrypted}) 
```

which shows that the dummy parameter is used to constrain the value of BITSTRING. (If there were multiple parameters used in the constraint, these would be in a comma-separated list within the curly braces after CONSTRAINED BY.) 这表明，这个虚拟参数被用来限制 BITSTRING 的值。如果约束条件中使用了多个参数，这些参数将会以逗号分隔的形式列在“CONSTRAINED BY”之后的花括号内。

The constraint is called a "user-defined" constraint because the precise nature of the constraint is not specified with formal ASN.1 notation. This construction almost invariably contains comment that details the precise nature of the constraint. So the above would more commonly be written as: 这种约束被称为“用户定义的”约束，因为其具体性质并未在正式的 ASN.1 标记法中明确说明。这种约束几乎总是会包含一些注释，用来详细说明该约束的具体性质。因此，上述描述通常会这样书写：

```txt
ENCRYPTED {Type-to-be-encrypted} ::= BITSTRING
(CONSTRAINED BY {Type-to-be-encrypted}
-- The BITSTRING is the results of
-- encrypting Type-to-be-encrypted
-- using the algorithm specified
-- in the field security-algorithm,
-- and with the encryption parameters
-- specified in Security-data -- ) 
```

The reader should know enough by now (assuming earlier text has been read and not skipped!) to realise that "security-algorithm" will turn out to be a (UNIQUE) fixed type value field (probably of type object identifier) of some SECURITY-INFORMATION class, with "Security-data" being a corresponding type field of this class that, for any given object of SECURITY-INFORMATION is defined with an ASN.1 type that can carry all necessary parameters for the algorithm that is being defined by that object. There might be other fields of SECURITY-INFORMATION that statically define choices of procedures in the application of the algorithm, filling in procedural "holes" in this process. 读者现在应该已经了解得足够多了（假设之前已经阅读了相关内容且没有跳过任何部分！）。“安全算法”实际上是一个唯一的固定类型值字段，该字段属于某个 SECURITY-INFORMATION 类。而“安全数据”则是该类的对应类型字段。对于任何一个 SECURITY-INFORMATION 对象来说，其安全数据字段都包含一种 ASN 类型，该类型可以携带该算法所需的所有参数。此外，SECURITY-INFORMATION 类还可能包含其他字段，这些字段可以静态地定义算法应用过程中所需的各种参数，从而填补这一过程中的各种“空白”。

<table><tbody><tr><td data-imt-p="1">It is obvious, powerful, and simple! How unusual for ASN.1! 它非常直观、强大且简单！这对 ASN 来说真是罕见啊！</td></tr></tbody></table>

## 4 The full story on parameterization 4. 关于参数化的完整信息

There is not a lot more to add on parameterization, and it is all pretty obvious stuff. But here it is. © OS, 31 May 1999 22 关于参数化的设置，其实并没有太多需要补充的内容，所有操作都相当直观明了。不过，还是在这里说明一下吧。© OS，1999 年 5 月 31 日 22

## 4.1 What can be parameterized and be a parameter? 4.1 哪些事物可以被参数化，并且可以作为参数使用呢？

The box says it all. Any form of reference name - a type reference, a value reference, a class reference, Answer: Anything and everything! an object reference, an object set reference can be parameterised by adding a dummy parameter list after the reference name and before the "::=" when the "thing" the name references is being defined. 这个框里的内容已经说明了一切。任何形式的引用名称都可以使用：类型引用、值引用、类引用、对象引用，甚至是对象集合引用。可以通过在引用名称之后、赋值运算符“::=”之前添加一个虚拟参数列表来为这些引用添加参数。当定义该名称所引用的对象时，就可以使用这些参数了。

Here is an example of a reference name with a complete range of parameters: 以下是一个包含完整参数范围的参考名称示例：

```autohotkey
Example-reference {INTEGER:intval,
My-type,
THIS-CLASS,
OPERATION:My-ops,
ILLUSTRATION:illustration-object} ::= 
```

As we would expect, the initial letter of dummy parameters is upper-case for types, classes, and object sets, and lower case for objects and values. Note that for values, object sets, and objects, the dummy parameter list includes the type or class of these parameters followed by a ":" (colon). (The only one of the above examples that I have not seen in an actual specification is a dummy parameter which is a class (THIS-CLASS above). 正如我们所预期的那样，虚拟参数的首字母对于类型、类以及对象集来说都是大写的，而对于对象和值则使用小写字母。需要注意的是，对于值、对象集以及对象而言，虚拟参数列表中会先列出这些参数的类型或类，然后加上冒号：“”。在上述示例中，唯一一个我没有在实际规范中看到的是作为类的虚拟参数（比如上述示例中的 THIS-CLASS）。

Normally, the dummy parameter is used somewhere on the right-hand side of the assignment, but it can also be used within the parameter list itself (before or after its own appearance). So we could, for example, write: 通常，dummy 参数会被放在赋值语句的右侧某个位置，但它也可以直接出现在参数列表中（在其被声明之前或之后）。例如，我们可以这样写：

 

$$
\text { Example1 } \left\{\text { My - type:default - value, My - type } \right\}:: =
$$

This notation is extremely general and powerful, and has many applications. We have seen the ROSE examples where an Information Object Set is declared as a dummy parameter. This is probably the most common thing that is used as a dummy parameter, but next to that is a value of type INTEGER that is used on the right-hand side as the upper-bound of INTEGER values, or as an upper-bound on the length of strings. 这种表示方式非常通用且强大，有着广泛的应用。我们已经看到了在 ROSE 示例中，信息对象集被声明为虚拟参数的情况。这可能是最常用的虚拟参数用法。除此之外，还有一种情况是使用 INTEGER 类型的值作为右侧参数的上限，或者作为字符串长度的上限。

There is also an important use in the Manufacturing Messaging Formats (MMF) specification. Here the bulk of the protocol specification occurs in a "generic" module, and is common to all cells on a production line. However, specific cells on the production line require some additional information to be passed to them. In the generic module we use a dummy parameter (a type) and include it in our protocol specification as an element of our SEQUENCE and export this parameterised type. Modules for specific cells define a type containing the additional information for that cell, import the generic type, and declare the protocol to be used for that type of cell as the generic type, supplied with the type containing the additional information as the actual parameter. This is similar to the ROSE example, but using a type rather than an information object set. 在制造消息格式规范中，这种用法也非常重要。该规范的大部分内容都体现在一个“通用”模块中，这个模块是生产线上的所有单元都共有的。不过，生产线上的特定单元需要一些额外的信息传递给它们。在通用模块中，我们使用了一个虚拟参数（类型），并将其作为协议规范的一部分包含进来，同时导出这个带有参数化的类型。针对特定单元的模块会定义包含该单元所需额外信息的类型，然后导入通用类型，并声明该类型所使用的协议为通用类型，而包含额外信息的类型则作为实际参数被传递。这与 ROSE 示例类似，但使用的是类型而不是信息对象集。

Let us explore the question of bounds a little further. Few protocols "hard-wire" upper bounds into the specification, but it is always a good idea to specify such bounds, as designers rarely intend to require implementors to handle arbitrarily large integers, iterations of sequences, or arbitrarily long strings. Where such bounds are fixed for the entire protocol, then it is common practice to assign the various bounds that are needed to an integer reference name in some module, then to use EXPORTS and IMPORTS to get those names into the modules where they are used as bounds. 让我们进一步探讨一下关于上限的问题。很少有协议会在规范中明确指定上限值，但无论如何，指定这些上限值还是个好主意，因为设计者通常并不希望要求实现者能够处理任意大的整数、序列的重复项，或者任意长的字符串。当这些上限值在整个协议中都是固定的时候，通常会将各种所需的上限值分配给某个模块中的整数引用名称，然后通过 EXPORTS 和 IMPORTS 将这些名称导入到需要使用这些名称作为上限值的模块中。

Where, however, there are generic types (such as a CHOICE of a number of different character string types) that are used in many places but with different bounds for each use, then using an INTEGER dummy parameter for the bounds is a very effective and common practice. 不过，当存在一些通用类型时（例如，一系列不同字符串类型的选择），这些类型会在许多地方被使用，但每个使用的场景都有其特定的限制条件。在这种情况下，使用一个 INTEGER 虚拟参数来表示这些限制条件是一种非常有效且常见的做法。

It is actually quite rare to see long dummy parameter lists. This is because any collection of information (apart from a class) can easily be turned into a Information Object Set. So with the earlier example (taking MY-CLASS out) of: 实际上，看到较长的参数列表是很罕见的。因为除了类之外，任何信息集合都很容易被转化为信息对象集。所以，以之前的例子为例（去掉 MY-CLASS 这个元素）：

```txt
Example-reference {INTEGER:intval,
My-type,
OPERATION:My-ops,
ILLUSTRATION:illustration-object} ::= 
```

We could instead define: 我们可以这样定义：

```txt
PARAMETERS-CLASS ::= CLASS
    {&intval INTEGER,
    &My-type,
    &My-ops OPERATION,
    &illustration-object ILLUSTRATION} 
```

and then our parameter list just becomes: 然后，我们的参数列表就变成了：

```txt
Example-reference {PARAMETERS-CLASS:parameters} ::= 
```

and on the right-hand side we use (for example) "parameters.&My-type" instead of "My-type". This may seem more cumbersome than using several dummy parameters, but if the same parameter list is appearing in several places, particularly if dummy parameters are being passed down as actual parameters through several levels of type definition, it can be useful to bundle up the dummy parameters in this way. 在右侧，我们通常使用“parameters.&My-type”而不是“My-type”。虽然这种方式看起来比使用多个虚拟参数更繁琐，但如果同一个参数列表出现在多个地方，尤其是当虚拟参数作为实际参数被传递到多个类型定义层次时，将虚拟参数合并起来使用就非常有用。

A particular case of this would be where a protocol designer has identified twelve situations (iterations of sequences, lengths of strings, sizes of integers) where bounds are appropriate, with potentially twelve different integer values for each of these situations, probably with each of the twelve values being used in several places in the protocol. This is again a good case for "bundling". We can define a class: 一个具体的例子是，当协议设计者确定了十二种情况（如序列的迭代、字符串的长度、整数的大小等），在这些情况下需要使用边界值。每种情况可能对应十二个不同的整数值，而这些值可能在协议的多个地方被使用。这再次体现了“捆绑”策略的适用性。我们可以定义一个类来描述这种情况。

```txt
BOUNDS ::= CLASS
    { &short-strings INTEGER,
    &long-strings INTEGER,
    &normal-ints INTEGER,
    &very-long-ints INTEGER,
    &number-of-orders INTEGER}
WITH SYNTAX
{STRG &short-strings, LONG-STRG &long-strings,
    INT &normal-ints, LONG-INT &very-long-ints,
    ORDERS &number-of-orders} 
```

and routinely and simply make an object set of this class a dummy parameter of every type that we define, passing it down as an actual parameter of any types in SEQUENCE, SET, or CHOICE constructions. We can then use whichever of the fields we need in the various places in our protocol. In some type definitions, we might use none of them, and the dummy parameter for that type would be redundant (but still legal), or we might use one or two of the fields, or (probably rarely) all of them. 我们通常只需将这种类型的对象作为所有定义类型的实际参数之一来使用。然后，我们可以在协议中的各个位置使用所需的字段。在某些类型定义中，我们可能不使用任何字段，此时该类型的虚拟参数就是多余的（但仍然是合法的）；或者，我们可能会使用一两个字段，或者（极少数情况下）使用所有字段。

At the point where we define our top-level type (usually a CHOICE type, as we discussed in the early parts of this book), we can set our bounds and supply them as an actual parameter. So if "Wineco-protocol" is our top-level type, we could have: 在我们定义最高级别类型的时候（通常是一个 CHOICE 类型，正如我们在本书的早些章节中提到的），我们可以为这个类型设定边界，并将这些边界作为实际参数来传递。因此，如果“Wineco-protocol”是我们的最高级别类型，那么我们可以这样定义：

```txt
bounds BOUNDS ::= {STRG 32, LONG-STRG 128,
    etc }
Wineco-protocol {BOUNDS:bounds} ::= CHOICE
{ordering [APPLICATION 1] Order-for-stock
{BOUNDS: bounds},
sales [APPLICATION 2] Return-of-sales
{BOUNDS: bounds}
etc. } 
```

No doubt there are some readers that will be saying "What is the point of passing this stuff down as parameters, when (provided "bounds" is exported and imported everywhere), it can be directly used?" The answer in this case is "Not much!". If, for any given type, any set of bounds is always going to be fixed, then there is no point in making it a parameter, a global reference name can be used instead, with a simpler and more obvious specification. But read on to the next section! 无疑，会有一些读者会问：“既然在到处都可以导入和导出‘边界值’的情况下，把这些参数传递下去有什么意义呢？直接使用时不是更方便吗？”这个问题的答案就是：“没什么意义！”。如果对于任何一种类型来说，边界值都是固定不变的，那么将其作为参数传递就没有意义了。相反，可以使用一个全局的引用名称来代替，这样就能实现更简洁、更直观的规范了。不过，请继续阅读下一节吧！

## 4.2 Parameters of the abstract syntax 4.2 抽象语法的参数

Protocol designers are often hesitant about fixing bounds in the body of a protocol definition, even if they are defined in just one place and passed around either by simple import/export or by additionally using dummy parameters. The reason for the hesitation is that bounds can very much "date" a protocol for two reasons: First, what seems adequate initially (for example, for the number of iterations of the "details" SEQUENCE in our "Order-for-stock" type in 协议设计者通常对修改协议定义中的约束条件持犹豫态度，即使这些约束条件只在一个地方被定义，并且可以通过简单的导入/导出方式传递，或者通过使用虚拟参数来传递。之所以会犹豫，是因为约束条件可能会让协议变得过时。原因有两个：首先，最初认为的约束条件可能并不合适（例如，在我们“库存订单”类型中，关于“细节序列”的迭代次数这样的约束条件，可能后来被证明并不必要）。

So you want to leave some things implementation-dependent? Coward! But at least make it explicit (and define exceptionhandling to help interworking between different implementations) Parameters of the abstract syntax let you do that, but they are a rarely-used feature. 所以你想让一些事情的实现方式具有灵活性？真胆小啊！但至少应该明确说明这一点（并定义异常处理机制，以帮助不同实现之间的互操作）。抽象语法中的参数可以让你做到这一点，不过这只是一个很少被使用的功能而已。

Figure 13 of Section I) can well prove inadequate ten years later when the business has expanded and mergers have occurred! Second, bounds are usually applied to ease the implementation effort when implementing on machines with limited memory capacity, or without support for calculations with very long integer values. Such technological limitations do, however, have a habit of disappearing over time. So whilst fifteen years ago, many designers felt that it was unreasonable to have messages that exceeded 64K octets, today implementors on most machines would have no problem handling messages that are a megabyte long. (An exception here would be specifications of data formats for smart cards, where memory is still very limited. This is an area where ASN.1 has been used.) 第 I 部分的图 13 在十年后显然已经不够用了——因为当业务规模扩大且发生了合并之后，这种限制就变得不再适用了。其次，这些限制通常是为了简化在内存容量有限或不支持对非常长整数值进行计算的机器上的实现工作而设定的。不过，这类技术限制随着时间的推移会逐渐消失。因此，十五年前，许多设计师认为超过 64K 字节的消息是不合理的，而如今，大多数机器的实现者都能轻松处理长达一兆字节的消息。（不过，对于智能卡的数据格式规范来说，情况就有所不同，因为此时内存仍然非常有限。在这方面，ASN.1 标准确实发挥了重要作用。）

So ..., if we don't want to put our bounds into the main specification, what to do? Just leave them out? This will undoubtedly cause interworking problems, with some systems not being able to handle things of the size that some other systems generate, and we are not even flagging this up as a potential problem in our ASN.1 specification. 那么……如果我们不想将这些限制因素纳入主要规范中，该怎么办呢？难道就直接把它们省略掉吗？这样做无疑会导致兼容性问题，因为有些系统可能无法处理某些大型数据，而我们在 ASN1 规范中甚至没有将这个问题列为潜在问题。

Providing a "bounds" parameter, but never setting values for it, can help with this problem. We have already seen in figure 21 in Section I Chapter 3 that we can specify our top-level type using the "ABSTRACT- SYNTAX" notation. Let us repeat that now with our parameterised Winecoprotocol developed above: 提供一个“bounds”参数，但不要为其设置具体值，这有助于解决这个问题。在第三章第一节的图 21 中，我们已经看到可以使用“抽象语法” notation 来指定顶层类型。现在，让我们用上面提到的带有参数的 Winecopyrotocol 来再次说明这一点：

$$
\begin{array}{l} \text {wineco - abstract - syntax \{BOUNDS:bounds\} ABSTRACT - SYNTAX :: =} \\ \quad \{\text {Wineco - protocol \{BOUNDS: bounds\} IDENTIFIED BY etc} \} \end{array}
$$

We are now defining our abstract syntax with a parameter list. We have parameters of the abstract syntax. ASN.1 permits this, provided such parameters are used only in constraints. These constraints are then called variable constraints, because the actual bound is implementationdependent. The important gain that we have now got, however, is that this implementationdependence has been made very clear and specific. Where we have a variable constraint, we would normally provide an exception marker to indicate the intended error handling if material is received that exceeds the local bounds. 我们现在使用参数列表来定义我们的抽象语法。我们有一些抽象语法的参数。ASN.1 允许这样做，但前提是这些参数只能用于约束条件中。这些约束被称为可变约束，因为实际的约束条件取决于具体的实现方式。不过，我们现在获得的一个重要好处是，这种实现依赖的特性得到了非常清晰和具体的描述。当存在可变约束时，我们通常会提供一个异常标记，以指示如果接收到超出本地范围的消息时应该如何处理。

In the OSI work, there is the concept of International Standardized Profiles (ISPs) and of Protocol Implementation Conformance Statements (PICS). The purpose of ISPs is to provide a profile of options and parameter values to tailor a protocol to the needs of specific communities, or to define different classes (small, medium, large say) of implementation. The purpose of the PICS is to provide a format for implementors to specify the choices they have made in implementationdependent parts of the protocol. Clearly, the use of parameters of the abstract syntax aids in both these tasks, with values for those parameters either being specified in some profile (which an implementation would then claim conformance to) or directly in the PICS for an implementation. 在 OSI 标准中，存在国际标准化配置文件和协议实施一致性声明的概念。标准化配置文件的目的是提供各种选项和参数值，以便根据特定社区的需求来定制协议，或者定义不同级别的实施方式（例如小型、中型、大型等）。而协议实施一致性声明的目的是为实施者提供一种格式，使他们能够明确在协议依赖部分所做出的选择。显然，使用抽象语法中的参数有助于完成这两项任务——这些参数的取值要么在某个配置文件中被指定，要么直接体现在协议实施一致性声明中。

Parameters of the abstract syntax (with exception markers on all variable parameters) provide a very powerful tool for identifying areas of potential interworking problems, but it is (for this author at least) sad that to-date these features are not yet widely used. 抽象语法中的参数设置（除了所有可变参数的例外情况）是一种非常有效的工具，可以用来识别可能存在互操作问题的区域。不过，令人遗憾的是，目前这些功能还没有得到广泛的应用。至少对我来说，这种情况确实令人遗憾。

## 4.3 Making your requirements explicit 4.3 明确表述你的需求

## 4.3.1 The TYPE-IDENTIFIER class 4.3.1 TYPE-IDENTIFIER 类

A very common Information Object Class is one which has just two fields, one holding an object identifier to identify an object of the class, and the other holding a type associated with that object. This class is in fact pre-defined (built-in) in ASN.1 as the TYPE-IDENTIFIER class. It is defined as: 一种非常常见的信息对象类只有两个字段：一个用于存储该类的对象标识符，另一个用于存储与该对象相关的类型信息。实际上，这种类在 ASN.1 中已经被预定义了，被称为 TYPE-IDENTIFIER 类。其定义如下：

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/54379e17-c034-430b-894c-f77661f731e5/f12ec0bf62d08541f83d1c50d88a4bca70976606f7b72a692028c5c688f51b70.jpg)

One of only two built-in classes (the other is ABSTRACT-SYNTAX) in ASN.1, and quite well-used. 它是 ASN 中仅有的两个内置类之一（另一个为 ABSTRACT-SYNTAX），并且被广泛使用。

TYPE-IDENTIFIER ::= CLASS {&id OBJECT IDENTIFIER UNIQUE, &Type } WITH SYNTAX {&Type IDENTIFIED BY &id} 类型标识符 ::= 类别 {&类型 对象标识符 唯一, &类型} 语法 {&类型 由 &id 标识}

There are many protocols that make use of this class. It is the foundation stone for a very flexible approach to extensibility of protocols. 有许多协议都使用了这一类接口。它是实现协议可扩展性的一种非常灵活的方法的基础。

## 4.3.2 An example - X.400 headers 4.3.2 一个例子——X.400 头部结构

(As with ROSE, the following is not an exact copy of X.400). （与 ROSE 类似，以下内容并非 X.400 系统的完全复制。）

In X.400 (an e-mail standard), there is the concept of "headers" for a message. A wide range of headers are defined. In the earliest version of X.400, these were hard-wired as types within a SEQUENCE, but it rapidly became clear that new headers would be added in subsequent versions. Of course, the SEQUENCE could just have had the extensibility ellipsis added, with defined exception handling on the ellipsis, ensuring interworking between versions 1 and 2, but an alternative approach is to define the headers as: 在 X.400 标准（一种电子邮件协议）中，存在对消息进行标识的“头部”概念。该标准中定义了多种类型的头部。在 X.400 的早期版本中，这些头部是作为序列中的固定元素来定义的；不过很快便意识到在后续版本中还会添加新的头部。当然，也可以让序列具有可扩展性，为这些扩展元素定义相应的异常处理机制，从而确保版本 1 和版本 2 之间的互操作性。不过，另一种方法是将这些头部定义为：

 

$$
\text { HEADER - CLASS }:: := \text { TYPE - IDENTIFIER }
$$

 

and the actual headers as: 实际的头部信息如下：

```autohotkey
Headers-type {HEADER-CLASS:Supported-headers} ::=
SEQUENCE OF SEQUENCE
{id HEADER-CLASS.&id ( {Supported-headers} !100),
info HEADER-CLASS.&Type ( {Supported-headers}{@id}!101) } 
```

Exception handling 100 and 101 will be specified in the text of the protocol definition. Handling of 100 is likely to be "silently ignore" and of 101 (a bad type) "send an error return and otherwise ignore". 在协议定义文本中，会明确说明对错误代码 100 和 101 的处理方式。对于错误代码 100，可能会选择“忽略处理”；而对于错误代码 101（表示类型错误的情况），则会选择“返回错误信息并忽略其他处理”。

The question is, when we eventually supply an actual parameter for Header-type, what do we provide? Let us examine some options. 问题是，当我们最终为“Header-type”类型提供一个具体的参数时，我们应该提供什么内容呢？让我们来看看一些可行的选项吧。

There will certainly be some headers defined in this version of the protocol, and we will undoubtedly expect to add more in subsequent versions, so we would first define an extensible information object set something like: 在这个版本的协议中，肯定会有一些可扩展的头部信息。在后续的版本中，我们无疑还会继续添加更多的可扩展元素。因此，我们首先定义一组可扩展的信息对象，其结构大致如下：

$$
\begin{array}{l} \text {Defined - Headers HEADER - CLASS : : =} \\ \{\text {header1 | header2 | header3 , ..., header4} \} \end{array}
$$

where header4 was added in version 2. 在版本 2 中，添加了 header4。

But what do we supply as the actual parameter for our protocol? Let us take the most general case first. We consider providing two parameters of the abstract syntax, both object sets of class HEADER-CLASS. One is called "Not-implemented" and the other "Additional-headers". We might want to provide one or both of these or neither, depending on the decisions below. I think you are probably getting the idea! 但是，我们的协议到底会提供哪些具体参数呢？我们先来看最一般的情况。我们考虑提供两个抽象语法的参数，这两个参数都是关于 HEADER-CLASS 类的对象集。其中一个参数被称为“未实现”，另一个则被称为“附加头部”。根据下面的决定，我们可能会选择使用其中一个或两者，或者根本不使用这些参数。我想你们应该已经明白了吧！

Let us now look at various possible views we might take on the requirements of implementations to support headers. 现在让我们来看看关于支持头部字段的各种可能实现方式。

## 4.3.3 Use of a simple SEQUENCE 4.3.3 使用简单的序列

We decide we want to define a fixed set of headers, all to be implemented, no additions, and we will never make later changes. Some headers will be required, others optional. 我们决定要定义一组固定的头部信息，这些信息都需要被实现，不允许添加任何内容，而且之后也不会进行任何修改。有些头部是必需的，而另一些则是可选的。

We got it right first time! 我们第一次就做对了！

This case is easy, and we don't need Information Object Sets, we simply use: 这个案例很简单，我们不需要使用信息对象集，我们只需要这样做就行了：

```txt
Headers ::= SEQUENCE
{header1 Header1-type --must be included--, header2 Header2-type OPTIONAL, etc } 
```

This is simple and straight-forward, but very inflexible. Where the decisions on what headers to provide (as in the case of e-mail headers) is rather ad hoc and likely to need to be changed in the future, this is NOT a good way to go! 这种方案很简单直接，但缺乏灵活性。例如，关于是否提供邮件头信息的问题，其决定往往是随机的，而且未来可能会发生变化。因此，这种方案并不适合长期使用！

Note that in this case the identification of what header is being encoded in a group of OPTIONAL headers is essentially done (in BER) using the tag value. (In PER it is slightly different - a bitmap identifies which header has been encoded in a particular position). 需要注意的是，在这种情况下，确定一组可选头部中究竟包含了哪个头部的数据，实际上是通过标签值来完成的（在 BER 协议中）。而在 PER 协议中则有所不同——此时使用的是位图来标识在特定位置中编码了哪个头部的数据。

## 4.3.4 Use of an extensible SEQUENCE 4.3.4 使用可扩展的 SEQUENCE

In the case of e-mail headers, it is highly likely that we will want to add more types of header later, so making the SEQUENCE extensible would be a better approach. And we should specify exception handling so that we know how 在电子邮件头部信息方面，很可能会在未来需要添加更多类型的头部信息。因此，让序列结构具有可扩展性会是一个更好的解决方案。此外，我们还应该指定异常处理机制，以便我们能够应对各种情况。

We are in control. You do what we say. We won't remove anything, but we might add more later. 我们掌控着局面。你们必须按照我们的指示行事。我们不会移除任何东西，不过之后可能会添加一些内容。

version 1 systems will behave when they are sent headers from a version 2 system (and how version 2 systems should behave if headers that are mandatory in version 2 are missing because it is a version 1 system that is generating the headers). 版本 1 的系统在接收到来自版本 2 系统的头部信息时会采取何种行为？而如果版本 2 中要求必须包含的头部信息因该系统为版本 1 而缺失，那么版本 2 的系统又会如何表现呢？

## 4.3.5 Moving to an information object set definition 4.3.5 转向信息对象集的定义

Now we make a quite big jump in apparent complexity, and use the "Headers" type we introduced above, namely: 现在，我们的复杂度有了显著的增加。我们将使用上文提到的“头部”类型，也就是：

Giving ourselves more options, but still keeping control. 让我们拥有更多的选择，同时仍然保持控制权。

```autohotkey
Headers-type {HEADER-CLASS:Headers} ::= SEQUENCE OF SEQUENCE
{identifier HEADER-CLASS.&id({Headers} !100),
data HEADER-CLASS.&Type({Headers}{@identifier} !101)} 
```

We have now moved to use of an object identifier to identify the type of any particular header, and potentially we now allow any given header type to be supplied multiple times with different values. But we have lost the ability to say whether a header is optional or not, and we have no easy way of saying which headers can appear multiple times. 我们现在改用对象标识符来标识特定头文件的类型。此外，现在允许某种头文件类型可以多次出现，并且每次出现时可以携带不同的值。不过，我们不再能够判断某个头文件是否是可选的，也没有简便的方法来确定哪些头文件可以多次出现。

We can address these problems by adding fields to our HEADER-CLASS. So instead of defining it as TYPE-IDENTIFIER, we can define it as: 我们可以通过在 HEADER-CLASS 中添加字段来解决这些问题。因此，我们可以不再使用 TYPE-IDENTIFIER 来定义它，而是采用以下方式进行定义：

```sql
HEADER-CLASS ::= CLASS
    {&id OBJECT IDENTIFIER UNIQUE,
    &Type,
    &Required BOOLEAN DEFAULT TRUE,
    &Multiples BOOLEAN DEFAULT TRUE}
WITH SYNTAX {&Type IDENTIFIED BY &id,
    [REQUIRED IS &Required],
    [MULTIPLES ALLOWED IS &Multiples]} 
```

We can now specify (when each header object is defined) whether it is optional or not, and whether multiple occurrences of it are permitted or not. Of course, when we used a SEQUENCE, we could flag optionality, and we could have indicated that multiples were allowed by putting SEQUENCE OF around certain elements. But the approach using information objects is probably simpler if we want all of that, and paves the way for more options. 我们现在可以指定每个头部对象是否是可选的，以及是否允许出现多次。当然，当使用 SEQUENCE 时，我们可以标记出选项性，并且可以通过在某些元素前加上 SEQUENCE OF 来表明允许多次出现。不过，如果我们想要实现所有这些功能，使用信息对象的方法可能更简单，而且也为未来提供更多可能性铺平了道路。

Of course, when we define the information object set "Defined-Headers", we will make it extensible, indicating the possibility of additions in version 2, and will put an exception specification on the ellipsis to tell version 1 systems what to do if they get headers they don't understand. 当然，当我们定义“已定义头文件”这一信息对象集时，我们会使其具有可扩展性，从而在版本 2 中允许添加新的头文件。同时，我们会在省略号上添加例外说明，以便让版本 1 的系统知道如何处理那些它们无法理解的头文件。

We could actually go further than this, as X.500 does in a similar circumstance: we could put another field into HEADER-CLASS defining the "criticality" of a header, and we could provide a field in "Headers-type" to carry that value. Our exception specification could then define different exception handling for unknown headers, depending on the value of the "criticality" field associated with it in the message. 实际上，我们可以更进一步的做法是，就像 X.500 在类似的情况中所做的那样：我们可以在 HEADER-CLASS 字段中再添加一个字段，用来表示头部的“重要性”。同时，我们可以在“Headers-type”字段中提供一个字段，用来存储这个数值。然后，我们的异常处理规范可以根据消息中“重要性”字段的值，来制定相应的异常处理方案。

We have advanced some way from the rather restricted functionality we had with SEQUENCE. 我们已经取得了一些进展，相比使用 SEQUENCE 时的功能限制，现在的情况要好多了。

## 4.3.6 The object set "Headers" 4.3.6 对象集“Headers”

An extensible "Defined-Headers" merely gives us control over what version 1 does when we add new material in version 2. It in no way says that implementations (probably on some user-group or vendor-specific basis) can agree and add new headers. It also says that to conform to version x, you must support all the headers listed in the "Defined- Headers" for version x. 一种可扩展的“定义头文件”机制，实际上只是让我们能够控制在版本 2 中添加新内容时，版本 1 会执行哪些操作。但这并不表示不同的实现（可能是基于特定用户组或供应商的实现）可以达成一致并添加新的头文件。同时，这也意味着要符合版本 x 的要求，就必须支持版本 x 中“定义头文件”中列出的所有头文件。

Now we give flexibility to the implementors. We use the parameters of the abstract syntax. 现在，我们为实施者提供了灵活性。我们可以灵活运用抽象语法的各种参数。

But, suppose we define: 但是，假设我们这样定义：

```txt
Supported-Headers
{HEADER-CLASS:Additional-Headers,
HEADER-CLASS:Excluded-Headers} HEADER-CLASS::=
{ (Defined-Headers | Additional-Headers)
EXCEPT Excluded-Headers) } 
```

where "Additional-Headers" and "Excluded-Headers" are parameters of the abstract syntax as described above, and where "Supported-Headers" is supplied as the actual parameter for our dummy parameter "Headers" in an instantiation of "Header-type".when we define our top-level PDU (and then passed down for eventual use in the constraints on "Header-type"). 在上述抽象语法中，“Additional-Headers”和“Excluded-Headers”都是参数。而“Supported-Headers”则作为实际参数，被提供给“Header-type”实例中的“Headers”参数。当我们定义顶层 PDU 时，这个参数会被传递下去，最终用于“Header-type”的约束条件中。

As usual, we could, if we wish, bundle the two object sets together as an object set of a new object class, making just one parameter of the abstract syntax covering both specifications. 像往常一样，如果我们愿意的话，可以将这两个对象集合合并为一个新的对象类，从而将抽象语法中的参数统一为仅一个参数，同时涵盖两种规范的内容。

With the above definition, we are clearly saying that we have some defined headers, implementors may support others, and indeed may choose not to support some of the defined headers. Total freedom! Possibly total anarchy! But most implementations will probably choose to implement most of the defined headers, and the exception handling should cope with interworking problems with those that miss a few out (for whatever reason). 根据上述定义，我们显然可以认为有一些被定义的头文件。实现者可以选择支持这些头文件，或者干脆选择不支持某些头文件。完全的自由！甚至可以说是完全的“无秩序”。不过，大多数实现方式通常会选择实现大部分被定义的头文件，而异常处理机制则能够解决那些因为某种原因而缺少某些头文件的兼容问题。

It is left as a (simple!) exercise for the reader to write an appropriate definition of Supported-Headers where we 这里把这部分内容留作一个简单的练习，让读者自行定义“支持头部”这个概念。

a) decide to allow additional headers, but require support for all defined headers; or a) 决定允许添加更多的头部信息，但要求所有定义的头部信息都必须得到支持；或者

b) decide to allow some defined headers not to be supported, but disallow implementation-dependent or vendor-specific additions. b) 决定允许某些特定的头部不被支持，同时禁止进行依赖于实现或特定供应商的扩展。

Of course, at the end of the day, you can never ENFORCE a requirement to implement everything, nor can you prevent people from extending a standardised protocol. But you CAN make it very clear that they are then not conforming to the Standard. ASN.1 provides the tools for doing this. 当然，归根结底，你无法强制要求所有人都遵守某些规定，也无法阻止人们对标准协议进行扩展。但是，你可以明确表示，那些不遵守标准的人实际上是不符合标准的。ASN.1 提供了实现这一目标的工具。

## 4.4 The (empty) extensible information object set 4.4 空的、可扩展的信息对象集

It makes little sense in most protocols to have an information object set with no members, even if it is extensible: 在大多数协议中，拥有一个没有成员的信息对象集是没有意义的，即使这个集合是可以扩展的。

$$
\{\dots \}
$$

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/54379e17-c034-430b-894c-f77661f731e5/9a6f23c88de756158da2a8b4e74094a2e289c7bac746578c35355370af1cf5e5.jpg)

It has become a fairly common practice (now supported by text in the Standard) to use this notation as a short-hand for "a parameter of the abstract syntax". When this is used as a constraint, it quite simply says that the specification is incomplete, and that you must look elsewhere for the specification of what is or is not supported. 使用这种表示法作为“抽象语法的参数”的简写形式，已经成为了一种相当常见的做法（现在标准文档中也对此进行了支持）。当这种表示法被用作约束条件时，就意味着该规范是不完整的，因此必须去其他地方查找关于哪些内容是被支持的、哪些内容是不被支持的详细说明。

This is called a "dynamically extensible object set", the idea being that implementations will determine in an instance of communication what objects they deem it to contain, and may indeed (depending on whether it is raining or not!) accept or reject some objects at different times. 这被称为“动态可扩展对象集”。其原理是，各个实现模块会在通信实例中决定它们认为该实例应该包含哪些对象；实际上，根据是否下雨的情况，这些实现模块可能会在不同的时间选择接受或拒绝某些对象。

If you get the impression that this author disapproves of the use of this construct, you will not be very wrong! 如果你觉得这位作者不赞成使用这种结构，那你的理解是正确的！

It provides no functionality beyond that provided (far more clearly) by parameters of the abstract syntax. It does, however, have one advantage. Parameters of the abstract syntax appear at the top-level, and need to be passed down as parameters to succeeding nested types until they reach the point at which they are to be used. This adds to the size of a specification, and can sometimes make it less easily readable. (Work was once proposed to add the concept of "global parameters" to ASN.1. This would effectively have enabled a top-level parameter to become a normal reference name, usable anywhere, without being passed from type to type as a sequence of actualdummy parameters. This work was, however, never progressed). 它除了能实现抽象语法中的参数功能之外，并没有其他功能。不过，它确实有一个优点：抽象语法中的参数出现在最顶层，并且需要作为参数传递给后续的嵌套类型，直到最终被使用。这会增加规范的复杂性，有时也会使得规范变得难以理解。（曾经有人提议在 ASN.1 中添加“全局参数”的概念。这样一来，最顶层的参数就可以成为一个普通的引用名称，可以在任何地方使用，而无需通过一系列实际存在的参数来传递。不过，这个提议最终没有得到实现。）

The use of the "{...}" notation in a constraint provides a direct statement at the bottom level that this constraint is implementation-dependent. But on the opposite side again - you cannot tell by looking at the top-level definition that there are (effectively) parameters of the abstract syntax, that is, that the specification is incomplete. You have to look through perhaps a hundred pages of ASN.1 definitions trying to spot occurrences of "{...}. 在约束条件中使用“{...}”这种表示法，实际上是一种在底层直接声明该约束条件是依赖于具体实现的手段。但是另一方面，从顶层定义来看，却无法判断出抽象语法规范中实际上存在参数这样的元素，也就是说，该规范并不完整。你必须仔细阅读可能长达一百页的 ASN.1 定义，才能找到“{...}”的身影。

The advice of this author is DON'T USE THIS CONSTRUCT. But you do need to know what it is supposed to mean if you encounter it, and there are many specifications that use it (more than use parameters of the abstract syntax). 这位作者的建议是：不要使用这个构造符。不过，如果你遇到它，还是有必要了解它到底代表什么意思。实际上，有很多规范都使用了这个构造符（而且不止是在抽象语法中用到它）。

There is an informative annex (not part of the Standard) in X.681 that says that ANY object set that is made extensible implies that random additions and removals of objects can be made when considering constraints imposed by that object set. It is not often that this author criticises the ASN.1 Standards - I wrote a lot of the text in them! But this annex gives bad advice, and is not really supported by normative text in the body of the Standard. 在 X.681 标准中有一个补充说明部分，其中指出：任何可以被扩展的对象集，都意味着在考虑该对象集所施加的约束条件时，可以对其进行随机添加或删除操作。不过，这位作者很少批评 ASN.1 标准——我自己就编写了其中许多内容！但这个补充信息给出了错误的建议，而且实际上并没有得到标准正文中的任何规范文本的支持。

So ... how do you decide what a particular specification means when it uses an extensible nonempty set? Read the specification carefully, and it will usually be clear. If it uses {...} it is probably saying that all extensible object sets can have implementation-dependent additions or exceptions (but then has no way of countering that in specific cases except by comment). If (like X.400), it has explicit parameters of the abstract syntax, it surely will NOT be implying that, and you should use the interpretation given in the previous clause for "Headers". 那么……当某个规范使用可扩展的非空集合时，该如何确定其具体含义呢？仔细阅读该规范的话，通常就能明白其意思了。如果规范中使用了 {...}，那意味着所有可扩展的对象集合都可以包含依赖于实现的额外规定或例外情况（不过在具体情况下，除了通过注释说明之外，没有其他办法来应对这种情况）。如果规范像 X.400 那样有明确的抽象语法参数，那它肯定不会意味着这样的含义，你应该按照前一段中对“头部信息”的解释来理解该规范。

<table><tbody><tr><td data-imt-p="1">You and me both - we must be getting tired! There is not much more to say, but there is still some. We'll try to keep it brief. This is not difficult stuff, but it IS used, and IS important. 你我都是如此——我们肯定已经很累了！其实没什么好说的了，但还是有一些事情需要提及。我们会尽量简短地表达。这并不是什么难事，但实际上这种技能是非常有用的，而且非常重要。</td></tr></tbody></table>

## 5 Other provision for "holes" 5. 其他关于“漏洞”的处理方式

There are some other mechanisms, mainly pre-dating the information object concept, that support holes in ASN.1 specifications. We need to have a brief discussion of these. 还有一些其他机制，它们出现在信息对象概念出现之前，这些机制有助于解释 ASN.1 规范中的漏洞。我们需要简要讨论一下这些机制。

## 5.1 ANY 5.1 任何

This has two important claims to fame. First, it was the only support for black-holes in the original 1984 ASN.1 Specifications! And second, it was withdrawn in 1994, causing a fairly major uproar among some ASN.1 users. 这个版本有两个重要的特点。首先，它是 1984 年原始 ASN1 规范中唯一支持黑洞处理的实现方式。其次，该版本在 1994 年被撤销，这引发了一些 ASN1 用户的强烈不满。

A (bad?) first attempt? 'Twas the best we could do in 1984. Holes were not really understood then. 那是一个（或许不太好的）初次尝试吧？不过，那已经是 1984 年时我们能做到的最好的水平了。那时候，人们还并不真正了解黑洞的本质。

If you wrote type "ANY" in a SEQUENCE or SET, it literally meant that any ASN.1 type could be slotted in there to replace the ANY. It was frequently accompanied in early CCITT specifications with the comment: 如果你在序列或集合中写入“ANY”这个词，那实际上意味着任何类型的 ASN.1 对象都可以被放入其中来替代“ANY”这个关键字。在早期的国际电信标准组织中，这种用法通常会伴随着这样的注释：

$$
- - \text { For further study } - -
$$

This comment clearly indicated that it was merely a place-holder in an incomplete specification. Usually in such cases, the SEQUENCE element read: 这条评论清楚地表明，它只是一个不完整的规范中的占位符而已。通常在这种情况下，会看到类似“序列元素”这样的描述。

## ANY OPTIONAL 任何可选的内容

so you basically knew that that element was not implementable - YET! 所以，你实际上已经知道那个元素是无法被实现的——不过还是这么做了！

Used in this way, it did no harm, but was probably not really useful. It provided part of the functionality we get today by using the extensibility ellipsis. It said "there is more to come in a later version, but we don't really know what yet". 以这种方式使用它并没有造成任何危害，但可能也并不真正具有实用性。它实现了我们现在通过扩展功能来实现的部分功能。它表示：“在后续版本中会有更多内容加入，不过目前我们还不清楚具体是什么。”

There were, however, other uses. One was in X.500 until recent times, where an element of a SEQUENCE read: 不过，它还有其他用途。在 X.500 协议中，直到最近为止，它都被用于某种序列的读取操作中。

## bi-lateral-information ANY OPTIONAL 双边信息，任选一项

The intent here was to allow implementation-dependent additional information to be passed, where the ASN.1 type for this information would be determined elsewhere (community of interest, or vendor-specific). If several vendors or communities produced different specifications for the type to fill this field, then you would typically look at the calling address to determine what the field was saying. (Yet another - non-standard - way of providing an identifier for the content of a hole!) 这里的目的是允许传递依赖于实现的附加信息，而这类信息的 ASN.1 类型则会在其他地方进行定义（例如由相关社区或特定供应商确定）。如果多个供应商或社区为该字段制定了不同的规范，那么通常可以通过查看调用地址来确定该字段的具体含义。（这又是一种非标准的手段，用于为空洞的内容提供标识符！）

In practice, this field was never implemented by X.500 implementors. 实际上，X.500 标准的实施者从未真正应用过这一技术。

Another option for determining the type (and its semantics) that filled the field would be to see if it was raining or not, but I don't think anyone ever used this particular mechanism for "holeidentification"! 确定填充该字段的类型（及其语义）的另一种方法是查看当时是否在下雨。不过，我认为应该没有人使用这种方法来“识别空洞”吧！

## 5.2 ANY DEFINED BY 5.2 任何由…定义的事物

This was an attempt in 1986/88 to shore up the ANY. There was by now a recognition that a black-hole absolutely had to have somewhere close to it in the protocol some value that would point to the definition of the actual type (and - more importantly - the semantics associated with that type) that was filling the hole. Suddenly the hole became a bit less black! 这是 1986/88 年的一次尝试，旨在加强 ANY 的定义。当时人们已经认识到，黑洞在协议中必须有一个与之相关的数值，这个数值能够指向填充该黑洞的实际类型的定义——更重要的是，还能指向与该类型相关的语义。突然间，这个“黑洞”变得不那么“黑色”了！

Dawn breaks (but just a bit!). It was recognised that any hole really MUST have associated with it a mechanism for determining what (and with what semantics) fills the hole. 黎明即将到来（虽然只是微弱的曙光而已！）。人们认识到，任何“空洞”都存在一种机制，可以用来决定是什么内容会以何种语义填充这个“空洞”。

(The light in the coal-cellar really got switched on when information objects appeared in the 1994 specification. I am grateful to Bancroft Scott for the analogy between the introduction of the information object concepts and switching on a light in a coal-cellar. When he first made the remark, someone - forgotten who - replied "That sounds rather dramatic. Things that dramatic can cause tidal waves." The reply was a good one! Information objects did not replace ANY and ANY DEFINED BY easily. Eventually they did, but it took close to seven years before the waves subsided!) （当在 1994 年的规范中引入信息对象这个概念时，煤仓里的灯光才真正被点亮了。我很感激 Bancroft Scott 能够举出这样一个类比：信息对象概念的引入就像煤仓里灯光的点亮。当他第一次提出这个观点时，有个人——我记不清是谁了——回答说：“那听起来太夸张了。这么夸张的事情可能会引发海啸。”这个回答真是绝妙！信息对象并没有完全取代那些由简单元素构成的系统。最终它们确实被取代了，但这一过程花了将近七年的时间，那些“海浪”才逐渐平息下来。）

With ANY DEFINED BY a typical SEQUENCE might now contain: 通过典型的序列来定义的任何对象，现在可能包含以下内容：

$$
\begin{array}{l l} \text {identifier} & \text {OBJECT IDENTIFIER,} \\ \text {hole} & \text {ANY DEFINED BY identifier} \end{array}
$$

The reader will recognise that this provides the same sort of link between the two fields that is now provided by use of a relational constraint (the @ notation) between "information from object class" constructs, but that it lacks any information object set reference to define the precise linkage, the types that can fill the "ANY" field, and the semantics associated with those types.. 读者会注意到，这种连接方式其实与通过关系约束（@符号）来连接“对象类信息”结构的方式相同。不过，这种连接方式缺乏用于定义精确关联的信息对象集引用、可以填充“ANY”字段的类型，以及与这些类型相关的语义描述。

There were also (too severe) restrictions on the linkages that could be specified using the ANY DEFINED BY notation which made it impossible for some existing specifications to move from ANY to ANY DEFINED BY, even 'tho' they DID have a field (somewhere) in their protocol that defined the content of the ANY hole. 此外，还有一些对使用“ANY DEFINED BY”标记来指定链接方式的限制过于严格了。这使得一些现有的规范无法从“ANY”模式转换为“ANY DEFINED BY”模式。尽管这些规范在协议中确实有一个字段用于定义“ANY”模式所包含的内容，但这种情况仍然无法解决上述问题。

## 5.3 EXTERNAL 5.3 外部因素

EXTERNAL was introduced in 1986/88, and is still with us. The name is in recognition of the fact that people want to embed material that is external to ASN.1, that is, material that is not defined using ASN.1 (for example, a GIF image). It was, however, also intended as a better version of ANY and ANY DEFINED BY, because it encapsulated identification of what was in the hole with the hole itself. EXTERNAL 这一术语是在 1986/88 年引入的，至今仍然被使用。这个名字的选用是为了体现人们希望嵌入那些不属于 ASN 定义的外部资源的需求——也就是说，那些不是通过 ASN 来定义的资源，比如 GIF 图像。不过，EXTERNAL 也代表着比 ANY 和 ANY DEFINED BY 更完善的解决方案，因为它能够明确说明其中包含了哪些具体的资源。

But you want to include material that is not defined using ASN.1. And you want to identify the type of material and the encoding of it. Roll your own using OCTET STRING or BIT STRING and a separate identifier field. That would work. But EXTERNAL tried to provide a ready-made solution. 但是，您希望包含那些没有使用 ASN 定义的数据类型。同时，您还需要明确数据的类型以及其编码方式。可以使用 OCTET STRING 或 BIT STRING 来定义这些数据类型，并设置一个独立的标识符字段。这样的方式应该是可行的。不过，EXTERNAL 试图提供一种现成的解决方案。

EXTERNAL was defined when ASN.1 was very much part of the OSI family, and recognised (amongst other possibilities) identification of the hole contents using a "presentation context" “EXTERNAL”这个定义是在 ASN.1 还是属于 OSI 家族的时候提出的。当时，人们认为可以通过“表示层上下文”来识别数据的内容。

negotiated using the Presentation Layer facilities of OSI. This mechanism was probably never used by any actual implementation. 通过 OSI 的表示层功能进行协商。不过，实际上可能没有任何实现会使用这种机制。

EXTERNAL can also make a claim to fame: its definition is almost certainly the only place in any ASN.1 specification where the type "ObjectDescriptor" is used! (But it is OPTIONAL - and I will wager that no implementation has ever transmitted an "ObjectDescriptor" value within an EXTERNAL.) EXTERNAL 这个类型还有一个独特的优点：在所有的 ASN.1 规范中，几乎可以肯定只有在这个类型的定义中才会使用“ObjectDescriptor”这个类型！（不过这是可选的——我敢打赌，没有任何实现会在 EXTERNAL 类型中传递“ObjectDescriptor”值。）

Finally, EXTERNAL was borne in the early days of understanding about abstract and transfer syntaxes, and (if you exclude the option of using the OSI Presentation Layer) used only a single object identifier value to identify the combination of abstract and transfer syntax for the material that filled the hole. Today, we generally believe that it is appropriate to identify the set of abstract values in the hole (for example, that it is a still picture) with one object identifier, and the encoding of those values (the encoding of the picture) with a separate object identifier. So whilst EXTERNAL remains (unchanged from its original introduction in 1986/88) in the 1988 specification, it has serious flaws, and new specifications should instead use "EMBEDDED PDV" (described below) if they wish to carry non-ASN.1-defined material. 最终，EXTERNAL 这一规范在人们开始理解抽象语法和传输语法的时候被提出。如果排除使用 OSI 表示层的选项，那么这个规范只使用一个对象标识符来标识填充空缺的数据所需的抽象语法和传输语法的组合。如今，我们通常认为将空缺处的抽象值（例如，一张静态图片）用一个对象标识符来表示是合适的，而将这些值的编码则用另一个对象标识符来表示。因此，虽然 EXTERNAL 这一规范在 1988 年的规范中仍然保持不变，但它存在严重的缺陷。如果希望包含非 ASN.1 定义的数据，那么应该使用“EMBEDDED PDV”这一规范来代替。

## 5.4 EMBEDDED PDV 5.4 嵌入式 PDV

EMBEDDED PDV was introduced in 1994. It was, quite simply, an attempt to "improve" EXTERNAL. It has all the functionality of EXTERNAL that anyone cares about. It got rid of the Object Descriptor that no-one ever used, and it allowed (but did not require) separate object identifiers for the identification of the abstract syntax and the transfer syntax (encoding) of the material that filled the hole. 嵌入式 PDV 在 1994 年被引入。简单来说，它就是一种试图“改进”外部系统的尝试。它具备了所有人们所期望的外部系统的功能。它摒弃了那些从未被使用的对象描述符，并允许使用独立的对象标识符来标识抽象语法和传输语法（即数据的编码方式），从而填补了原有系统的空白。

Why is it so difficult to get it right first time? EMBEDDED PDV is really just mending the deficiencies of EXTERNAL. EXTERNAL looked pretty good in 1986/88, but by 1994, it needed a re-fit. 为什么第一次就做对如此困难呢？嵌入式 PDV 其实只是在弥补外部方式的缺陷而已。外部方式在 1986/88 年时看起来相当不错，但到了 1994 年，就需要进行改造了。

Perhaps more importantly, it included the ability for a protocol designer to specify (statically) either or both of the abstract and transfer syntaxes for the "hole" (using constraint notation). 或许更重要的是，该规范还包含了让协议设计者能够（静态地）指定“空洞”部分的抽象语法和传输语法中的任意一种或两种的能力（使用约束表达式进行描述）。

One important use for this is in security work, where EMBEDDED PDV is used to carry the encryption of a type, the type (abstract syntax of hole contents) being statically specified, and the encryption mechanism (transfer syntax) being transferred at communication time. 这种技术的一个重要应用是在安全领域。在这里，嵌入式 PDV 被用来实现加密功能。其中，类型的定义是在静态阶段就确定的，而加密机制则会在通信过程中动态传输。

In appropriate circumstances, a designer can specify statically both the abstract (type of material) and transfer syntax (encoding) of what fills the hole. If this is done, then EMBEDDED PDV produces no overheads other than a length wrapper around the embedded material. 在适当的情境下，设计师可以静态地指定填充该空洞的材料的类型以及编码方式。如果做到这一点，那么 EMBEDDED PDV 就不会产生任何额外开销，只需要对嵌入的材料加上一个长度包装器即可。

A brief word about the name. (Figure 999 again). It is certainly a bad name for the type. "EMBEDDED" is fine. It represents a hole that can take embedded material. But "PDV"? Most readers will never have met the term "PDV". It actually standard for "Presentation Data Value", and is the term used by the OSI Presentation Layer Standard to describe the unit of information passed between the Application Layer and the Presentation Layer, or (in terms more related to the description given here of ASN.1) an abstract value from some abstract syntax (not necessarily defined using ASN.1). 关于这个名称，有一点需要说明。（再次看到图 999）。对于这种类型来说，这个名称显然不合适。“EMBEDDED”这个名称倒是还可以，它表示一个可以容纳嵌入数据的孔。不过“PDV”呢？大多数读者可能从未听说过“PDV”这个术语。实际上，它指的是“呈现数据价值”，是 OSI 表示层标准中的一个术语，用于描述在应用层与表示层之间传递的信息单位。或者，用与这里描述的 ASN.1 规范更相关的说法，它指的是某种抽象语法中的抽象价值（不一定是用 ASN.1 定义的）。

So don't worry about the name! For embedded material which is defined as an ASN.1 type you probably want to use the information object-related concepts to handle your holes. But if the material you want to embed is not defined using ASN.1, use EMBEDDED PDV. 所以不必担心名称的问题！对于被定义为 ASN 类型的嵌入材料，你可以使用与信息对象相关的概念来处理这些材料。但如果你要嵌入的材料并未使用 ASN 进行定义，那么应该使用 EMBEDDED PDV 方法来处理它。

## 5.5 CHARACTER STRING 5.5 字符字符串

CHARACTER STRING is actually just a special case of EMBEDDED PDV, and there is a lot of shared text in the specification of these types in the ASN.1 Standard. 字符字符串实际上只是嵌入式 PDV 的一种特例。在 ASN.1 标准中，这两种类型的规范中有很多内容是共通的。

CHARACTER STRING was an (unsuccessful!) attempt to produce a character string type that would satisfy all possible needs FOREVER. It was intended to make it possible for the maintainers of the ASN.1 Standard to say (as new character sets and encodings emerged in the world), "We don't need to change ASN.1, use CHARACTER STRING". “字符字符串”是一种试图创造一种能够满足所有潜在需求的字符字符串类型的尝试（但并未成功）。其初衷是让 ASN 标准的管理人员能够在新的字符集和编码出现时，能够轻松地说：“我们无需修改 ASN 标准，直接使用字符字符串即可。”

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/54379e17-c034-430b-894c-f77661f731e5/8a87220a7125939494262707937b0ea4f8a29ba294678aca25ab014e6e91e448.jpg)

The CHARACTER STRING type extends the concept of abstract and transfer syntax. It introduces the term "character abstract syntax" (an abstract syntax all of whose values are strings of characters from some defined character set), and "character transfer syntax" (a transfer syntax that provides encodings for all possible strings in a given character abstract syntax). CHARACTER STRING 类型扩展了抽象语法和传输语法的概念。它引入了“字符抽象语法”这一概念（一种抽象语法，其所有值都来自某个定义的字符集），以及“字符传输语法”这一概念（一种传输语法，能够为给定字符抽象语法中的所有可能字符串提供编码方式）。

Put in slightly less technical terms, a character abstract syntax object identifier identifies a character repertoire, and a character transfer syntax OBJECT IDENTIFIER identifies an encoding for strings of those characters. 用稍微不那么专业的术语来说，字符抽象语法对象标识符用于标识一组字符，而字符传输语法对象标识符则用于标识这些字符的字符串的编码方式。

Unconstrained, an encoding of the CHARACTER STRING type includes the two object identifiers that identify its character abstract syntax (repertoire) and its character transfer syntax (encoding) with each string that is transmitted. This is an unfortunate(!) overhead, as constructs like 无约束的字符字符串编码方式包含了两个对象标识符：一个用于标识其字符抽象语法结构，另一个用于标识其字符传输方式。不过，这种额外的信息确实有些多余了……因为像这样的结构其实并不需要包含这些信息。

## SEQUENCE OF CHARACTER STRING 字符字符串序列

(where the repertoire and encoding are the same for each element of the SEQUENCE OF) are quite common. As with EMBEDDED PDV, however, it is possible to statically constrain the CHARACTER STRING type so that only the actual encodings of characters are transmitted. 在“序列”的每个元素中，如果其编码方式相同的话，这种情况相当常见。不过，与嵌入式 PDV 类似，我们可以静态地限制字符字符串的类型，从而只传输字符的实际编码方式。

Object identifier values have been assigned for many character repertoires and sub-repertoires, and for many encoding schemes, but unfortunately not for all. UTF8String was added to ASN.1 after CHARACTER STRING. It could have been defined as a constrained CHARACTER STRING, but in fact it was "hard-wired" into ASN.1 as a new type defined using English text, just like PrintableString and IA5String etc! That is why "unsuccessful!" appeared in the second paragraph of this clause. 许多字符集、子字符集以及多种编码方式都已分配了对象标识符值。不过遗憾的是，并非所有情况都如此。UTF8String 在 CHARACTER STRING 之后被添加到 ASN.1 中。它本可以被定义为一种受限的 CHARACTER STRING 类型，但实际上它作为一种新的类型被直接纳入 ASN.1 规范，就像 PrintableString、IA5String 等类型一样！这就是为什么在这个条款的第二段中出现了“未成功”的提示。

## 5.6 OCTET STRING and BIT STRING 5.6 八元串和二元串

Of course, the ultimate blackest of black holes is to use OCTET STRING or BIT STRING to carry embedded material. It happens. You are really "rolling your own". ASN.1 will provide the delimitation (the length wrapper), but you must sort out the problems of identifying to a receiver the semantics of what fills the octet string or bit string hole. 当然，最复杂的黑洞实现方式就是使用 OCTET STRING 或 BIT STRING 来携带嵌入的物料。这种情况确实会发生。你实际上是在“自己动手”来实现这个功能。ASN.1 会提供相关的定义规则，但你需要解决如何将 OCTET STRING 或 BIT STRING 中的内容与具体的语义关联起来的问题。

Those who believe in using a very cut-down ASN.1 use these types for their holes. I guess you can't complain. They make it work. But there are more powerful specification tools available in the ASN.1 armoury, and I hope that anyone that has read this far in this text will not be tempted into use of OCTET STRING or BIT STRING when they need to introduce a hole! 那些相信使用非常精简的 ASN 标准的人，会采用这类机制来定义他们的“空洞”。我想你也没什么好抱怨的——他们确实让这个机制发挥了作用。不过，ASN 标准库中还有更强大的规范工具可用。希望读到这里的读者们，在需要定义“空洞”时，不会倾向于使用 OCTET STRING 或 BIT STRING 这种机制吧！

## 6 Remarks to conclude Section II 第六，作为第二部分的结束语

I wonder if there is a single reader (even my reviewers!) that can say they read from the start through to here? E-mail me at [j.larmouth@iti.salford.ac.uk](mailto:j.larmouth@iti.salford.ac.uk) if you did. (But don't bother if you just jumped around and got here from the index!) 我想知道，是否有一个读者能够从头到尾读完这本书呢？如果是的话，请发送邮件至 j.larmouth@iti.salford.ac.uk 与我联系。（如果你只是随意地跳着读这本书，那么就不用麻烦了！）

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/54379e17-c034-430b-894c-f77661f731e5/9d6105f53a7fde328b216adbe3f363451dff946a34c6181a4a2c296b0fec3032.jpg)

This text has tried to cover the whole of the ASN.1 concepts, mechanisms, notation. It is believed to be complete ("ASN.1 Complete" is the title!). There are further sections concerned with encoding rules and history and applications, but the description of the notation itself is now complete. 本文试图全面介绍 ASN.1 的概念、机制以及表示法。相信这些内容已经足够完整了（“ASN.1 Complete”就是这个标题的由来！）。此外，文章还涉及了编码规则、历史以及应用等方面的内容，不过对表示法的描述已经相当完整了。

Well ... it is complete as of 1999! If you are reading this book in 2010, there might be a later version available which you should get, 'cos there is probably a lot missing in this text! But I can't give you a reference to a later version - try a Web search, and in particular try the URL given in Appendix 5 (which might or might not still work in 2010!). 嗯……截至 1999 年，这个版本就已经完全成熟了！如果你在 2010 年阅读这本书，那么可能会有一些更新的版本可供选择，建议你去获取那些更新版本的内容，因为现在的文本中很可能缺少很多信息。不过，我无法提供关于后续版本的参考链接——你可以尝试在网上搜索，特别是查看附录 5 中给出的 URL 链接，也许在那个网址还能找到一些有用的信息。

At the time of writing, there are quite a lot of suggestions bubbling up in the ASN.1 standardization group that could give rise to additions to the ASN.1 notation. Recent (post-1994) history, however, has been of only introducing changes that clarify existing text or add very minor (from a technical view-point) and simple new functionality (such as UTF8String), not of earthshaking additions. Indeed, possibly earth-shaking additions that have been proposed in the last decade have a history of being abandoned - examples include light-weight encoding rules, global parameters, and dynamic constraints. 在撰写本文时，ASN 标准委员会中涌现出了许多建议，这些建议可能会为 ASN 标记语言带来新的扩展。不过，自 1994 年以来的历史中，标准委员会通常只进行那些旨在澄清现有规范或添加一些非常小的、技术性较强的新功能的修改（比如 UTF8String 这样的功能）。实际上，过去十年中提出的一些看似具有革命性的新功能，最终都被放弃了——比如轻量级编码规则、全局参数以及动态约束等。

Good luck in reading, writing, or implementing ASN.1 specifications! 祝你在阅读、编写或实施 ASN1 规范时一切顺利！

## THE END. 结束。

Well ... of this section! 嗯……关于这一节的内容！

SECTION III 第三部分

Encodings 编码方式

# Chapter 1 Introduction to encoding rules 第一章 编码规则介绍

## (Or: What no-one needs to know!) （或者：那些没人需要知道的事情！）

Summary: This first chapter of Section 3: 摘要：这是第 3 部分的第一个章节。

• Discusses the concept of encoding rules. • 讨论了编码规则的概念。

• Describes the TLV principle underlying the Basic Encoding Rules (BER). • 描述了基本编码规则（BER）所依据的 TLV 原则。

• Discusses the question of "extensibility", or "future proofing". • 讨论了“可扩展性”这个问题，也就是如何确保系统在未来能够持续运行的问题。

• Describes the principles underlying the more recent Packed Encoding Rules (PER). • 描述了最新的“打包编码规则”所依据的准则。

• Discusses the need for "canonical" encoding rules. • 讨论了采用“规范”编码规则的必要性。

• Briefly mentions the existence of other encoding rules. • 简要提及了其他编码规则的存在。

There has already been some discussion of encoding rules in earlier chapters which can provide a useful introduction to this concept, but this section has been designed to be complete and to be readable without reference to other sections. 在之前的一些章节中已经讨论过编码规则的相关内容，这些讨论可以为理解这一概念提供有益的入门信息。不过，本节的内容旨在做到完整且易于理解，无需参考其他章节的内容即可理解。

The next two chapters of Section III describe in detail the Basic Encoding Rules and the Packed Encoding Rules, but assume an understanding of the principles and concepts given here. 第三部分的接下来的两章详细描述了基本编码规则与打包编码规则。不过，读者需要已经了解这里所提到的相关原则和概念，才能理解这些描述。

## 1 What are encoding rules, and why the chapter sub-title? 1. 什么是编码规则？为什么这一章会有副标题呢？

"What no-one needs to know!". At the end-of-the-day, computer communication is all about "bits-on-the-line" - what has in the past been called "concrete transfer syntax", but today is just called "transfer syntax". (But if you think about it, a "bit" or "binary digit" is itself a pretty abstract concept - what is "concrete" is the electrical or optical signals used to represent the bits.) “没人需要知道的事情！”归根结底，计算机通信本质上就是关于“位级传输”的——过去这种传输方式被称为“具体传输语法”，如今则简称为“传输语法”。不过，仔细想想，“位”或“二进制位”本身就是一个相当抽象的概念——真正具有“具体性”的是用来表示这些位的电信号或光信号。

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/54379e17-c034-430b-894c-f77661f731e5/9844feb9c199bf490625271c9c90f0d00b42d468148271ca9de317c5eacadc87.jpg)

ASN.1 has taken on-board some concepts which originated with the so-called "Presentation Layer" of the ISO/ITU-T specifications for Open Systems Interconnection (OSI). (Note that the term "Presentation Layer" is a bad and misleading one - "Representation Layer" might be better). ASN.1 包含了一些源自 ISO/ITU-T 开放系统互连规范中的“表示层”的概念。（注意，“表示层”这个术语并不准确且具有误导性——使用“表示层”可能更为合适。）

The concepts are of a set of "abstract values" that are sent over a communications line, and which have associated with them bit patterns that represent these abstract values in an instance of communication. 这些概念指的是一组“抽象价值”，这些价值通过通信线路进行传输。同时，这些价值还伴随着特定的比特模式，这些比特模式用于在具体的通信场景中表示这些抽象价值。

The set of abstract values to be used, and their associated semantics, is at the heart of any application specification. The "encoding rules" are concerns of the (Re)Presentation Layer, and define the bit patterns used to represent the abstract values. The rules are a complete specification in their own right (actually, there are a number of variants of two main sets of rules - these are described later). The encoding rules say how to represent with a bit-pattern the abstract values in each basic ASN.1 type, and those in any possible constructed type that can be defined using the ASN.1 notation. 所有抽象值的集合以及与之相关的语义，是任何应用规范的核心内容。而“编码规则”则属于（重新）表示层的范畴，它们定义了用于表示抽象值的比特模式。这些规则本身就是一个完整的规范（实际上，主要有两套规则的不同变体——这些将在后面详细说明）。编码规则规定了如何将这些抽象值表示为每种基本 ASN.1 类型中的比特模式，以及使用 ASN.1 语法定义的所有可能构造类型中的比特模式。

ASN.1 provides its users with notation for defining the "abstract values" which carry user semantics and which are to be conveyed over a communications line. (This was fully described in Sections I and II). Just as a user does not care (and frequently does not know) what electrical or optical signal is used to represent zero and one bits, so in ASN.1, the user should not care (or bother to learn about) what bit patterns are used to represent his abstract values. ASN.1 为用户提供了一种表示“抽象值”的语法，这些抽象值具有用户语义，并且可以通过通信线路进行传输。（这一机制在第一节和第二节中有详细说明）。就像用户并不关心（实际上也通常不知道）用什么电信号或光信号来表示零和一比特一样，在 ASN.1 中，用户也不应该关心（或者不必去了解）用什么比特模式来表示他们的抽象值。

So details of the ASN.1 "encoding rules", which define the precise bit-patterns to be used to represent ASN.1 values, while frightfully important, are "What no-one needs to know". 因此，关于 ASN.1“编码规则”的详细信息其实非常重要，这些规则定义了用于表示 ASN.1 值的精确位模式。不过，这些细节其实属于“没人需要知道的事情”。

It is the case today that there are good ASN.1 tools (called "ASN.1 compilers") available that will map an ASN.1 type definition into a type definition in (for example), the C, C++, or Java programming languages (see Section I Chapter 6), and will provide run-time support to encode values of these data structures in accordance with the ASN.1 Encoding Rules. Similarly, an incoming bit-stream is decoded by these tools into values of the programming language datastructure. This means that application programmers using such tools need have no knowledge of, or even interest in, the encoded bit-patterns. All that they need to worry about is providing the right application semantics for values of the programming language data structures. The reader will find some further discussion of these issues in the Introduction to this book, and in Chapter 1 of Section 1. A detailed discussion of ASN.1 compilers is provided in Chapter 6 of Section 1. 目前，已经有很好的 ASN.1 工具可供使用（这些工具被称为“ASN.1 编译器”）。这些工具能够将 ASN.1 类型定义转换为 C、C++或 Java 等编程语言中的类型定义（详见第 6 章第一节）。同时，这些工具还能在运行时支持根据 ASN.1 编码规则对这些数据结构的数值进行编码。同样地，传入的位流也会通过这些工具被解码为编程语言中的数据结构对应的数值。这意味着使用这些工具的应用程序开发者无需了解或关心编码后的位模式，他们只需要为编程语言中的数据结构的值提供正确的应用语义即可。关于这些问题的更多讨论，可以在本书的引言部分以及第一节的第一章中找到。关于 ASN.1 编译器的详细讨论则位于第一节的第六章中。

There are, however, a few groups of people that will want to know all about the ASN.1 Encoding Rules. These are: 不过，还是有一些人想要了解关于 ASN.1 编码规则的所有细节。这些人群包括：

• The intellectually curious! • 那些充满求知欲的人！

• Students being examined on them! • 学生们正在接受考核！

• Standards writers who wish to be reassured about the quality of the ASN.1 Encoding Rules. • 那些希望确保 ASN.1 编码规则质量可靠的规范编写者们。

Implementors who, for whatever reason, are unable to use an ASN.1 compiler (perhaps they are working with an obscure programming language or hardware platform, or perhaps they have no funding to purchase tools), and have to "hand-code" values for transmission and "hand-decode" incoming bit-patterns. 那些由于某种原因无法使用 ASN 编译器实现的开发者们（也许他们使用的是一种不太流行的编程语言或硬件平台，或者他们没有足够的资金购买相关工具）。因此，他们不得不手动编写用于传输的值，并手动解码接收到的比特模式。

Testers and trouble-shooters that need to determine whether the actual bit-patterns being transmitted by some implementation are in accordance with the ASN.1 Encoding Rules specification. 那些需要确定某种实现方式所传输的实际位模式是否符合 ASN.1 编码规则规范的测试人员和问题排查人员。

If you fall into any of these categories, read on! Otherwise this section of the book is not for you! 如果你属于上述任何一种情况，请继续阅读吧！否则，这本书的这一部分就不适合你阅读了。

## 2 What are the advantages of the encoding rules approach? 2. 编码规则方法的优势是什么？

Section 1 Chapter 1 discussed a number of approaches to specifying protocols. The ASN.1 approach (borrowed from the Presentation Layer of OSI) of completely separating off and "hiding" the details of the bit-patterns used to represent values has a number of advantages which are discussed in the next few paragraphs. 第 1 章第 1 节讨论了多种指定协议的方法。ASN.1 方法（源自 OSI 的表示层）通过将用于表示值的位模式的细节完全分离并“隐藏”起来，这种方法具有许多优点，这些优点将在接下来的几段中详细讨论。

The first point to note is that a clear separation of the concept of transmitting abstract values from the bitpatterns representing those values enables a variety of different encodings to be used to suit the needs of particular environments. One often-quoted example (but I am not sure you will find it in the real-world!) is of a communication over a high-bandwidth leased line with hardware encryption devices at each end. The main concern here is to have representations of values that impose the least CPU-cycle cost at the two ends. But a 首先需要注意的是，将传输抽象价值的概念与表示这些价值的位模式分开考虑，这样可以实现多种不同的编码方式，从而满足不同环境的需求。一个常见的例子是：在一条高带宽的租用线路上进行通信时，两端都配备了硬件加密设备。此时的主要问题是，找到一种能够在两端都产生最小 CPU 运算成本的数值表示方式。不过，这个例子可能并不适用于现实世界的情况……

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/54379e17-c034-430b-894c-f77661f731e5/0a7afe179e34eeae083d3f3e300250e54851a7856095e5d3f8ae3d4379b9ca3c.jpg)

bull-dozer goes through the leased line! And the back-up provision is a modem on a telephone line with no security device. The concern is now with maximum compression, and some selective field encryption. The same abstract values have to be communicated, but what is the "best" representation of these values has now changed. 那台推土机正在穿越租赁线路！而备用方案则是通过没有安全装置的电话线路来传输数据。目前的问题在于如何实现数据的最大压缩效果，同时还需要对某些字段进行选择性加密处理。那些相同的抽象数值仍然需要被传输出去，但是这些数值的“最佳”表示方式已经发生了变化。

The second example is similar. There are some protocols where a large bulk of information has to be transferred from the disk of one computer system to the disk of another computer system. If those systems are different, then some work will be needed by one or both systems to map the local representations of the information into an agreed (standard) representation for transfer of the values over a communication line. But if, in some instance of communication, the two systems are the same type of system, CPU-cycles can probably be saved by using a representation that is close to that used for their common local representation of the information. 第二个例子类似。在某些协议中，需要把大量信息从一台计算机的磁盘传输到另一台计算机的磁盘上。如果这两台计算机的类型不同，那么其中一台或两台计算机都需要进行一些工作，以将信息的本地表示形式转换为一种标准格式，从而能够通过通信线路进行数据传输。不过，在某些通信场景中，如果这两台计算机属于同一类型，那么就可以使用与它们本地表示形式相近的表示方式，从而节省 CPU 周期。

Both the above examples are used to justify the OSI concept of negotiating in an instance of communication the representation (encoding) to be used, from a set of possible representations. However, today, ASN.1 is more commonly used in non-OSI applications, where the encoding is fixed in advance, and is not negotiable at communications-time (there is no OSI Presentation Layer present). 上述两个例子都用于说明 OSI 框架中关于通信过程中所使用的表示方式（编码方式）的协商机制。不过，如今 ASN.1 更常被用于非 OSI 框架的应用场景中，在这些场景中，编码方式是预先确定的，不会在通信过程中进行协商（因为不存在 OSI 的表示层）。

There are, however, a few other advantages of this clear separation of encodings from abstract values that are important in the real-world of today for the users of ASN.1. 不过，将编码与抽象值彻底分离这一做法在现实世界中也有一些重要的优势，这些优势对于使用 ASN1 的用户来说非常关键。

We have seen over the last twenty years considerable progress in human knowledge about how to produce "good" encodings for abstract values. This is reflected in the difference between the ASN.1 Basic Encoding Rules developed in the early 1980s and the Packed Encoding Rules developed in the early 1990s. But application specifications defined using ASN.1 in the 1980s require little or no change to the specification to take advantage of the new encoding rules - the application specification is unaffected, and will continue to be unaffected if even better encoding rules are devised in the next century. 在过去的二十年里，我们在了解如何为抽象值生成“良好”的编码方式这一方面取得了显著的进展。这一点可以从 1980 年代初制定的 ASN.1 基本编码规则与 1990 年代初推出的打包编码规则之间的差异中看出。不过，使用 ASN.1 在 1980 年代定义的应用规范，在采用新的编码规则时几乎不需要进行任何修改——应用规范本身不会受到影响，即使在未来一个世纪里再设计出更优秀的编码规则，应用规范依然会保持原样。

There is a similar but perhaps more far-reaching issue concerned with tools. The separation of encoding issues from the application specification of abstract values and semantics is fundamental to the ability to provide ASN.1 compilers, relieving application implementors from the task of writing (and more importantly, debugging) code to map between the values of their programming language data-structures and "bits-on-the-line". Moreover, where such tools are in use, changing to a new set of encoding rules, such as PER, requires nothing more than the installation of a new version of the ASN.1 compiler, and perhaps the changing of a flag in a run-time call to invoke the code for the new encoding rules rather than the old. 还有一个类似但可能更为重要的问题，与工具相关。将编码问题与抽象值及语义的应用规范分离，是提供 ASN.1 编译器的基础性要求。这一做法能够减轻应用程序开发者的负担，让他们无需再编写代码来实现编程语言数据结构与“线上比特”之间的映射，更无需进行调试工作。此外，在使用了这类工具的情况下，如果要更换为新的编码规则（如 PER），只需要安装新版本的 ASN.1 编译器即可，或许还需要在运行时调整某个标志，以启用新编码规则的代码，而不是旧的代码。

## 3 Defining encodings - the TLV approach 3. 定义编码方式——采用 TLV 方法

Chapter 1 of Section 1 discussed briefly the approach of using character strings to represent values, giving rise to a variety of mechanisms to precisely specify the strings to be used, and to "parsing" tools to recognise the patterns in incoming strings of characters. These approaches tend to produce quite verbose protocols, and generally do not give rise to as complete tool support as is possible with ASN.1. They are not discussed further, and we here concentrate on approaches which more directly specify the bit-patterns to be employed in communication. 第 1 部分的第 1 章简要讨论了使用字符字符串来表示值的方法。此外，还提出了多种机制来精确指定所使用的字符串，以及用于识别输入字符模式中模式的“解析”工具。这些方法往往会导致相当冗长的协议描述，而且通常无法像 ASN.1 那样提供如此完善的工具支持。因此，这里不再赘述这些方法，而是重点讨论那些能够更直接地指定通信中使用的位模式的方法。

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/54379e17-c034-430b-894c-f77661f731e5/021e9a1cb30d6908ea4269ddc56c14d7b8d6f427d60c3e657d1cf303b40d0dff.jpg)

As the complexity of application specifications developed over the years, one important and early technique to introduce some "order" to the task of defining representations was the so-called "TLV" approach. 随着多年来应用程序规范复杂性的不断增加，为了在一定程度上规范表示方式的定义过程，人们提出了一种早期的重要技术，即所谓的“TLV”方法。

With this approach, information to be sent in a message was regarded as a set of "parameter values". Each parameter value was encoded with a parameter identification (usually of fixed length, commonly a single octet, but perhaps overflowing to further octets), followed by some encoding that gave the length (octet count) of the parameter value (again as a single octet with occasionally the need for two or more octets of length encoding), and then an encoding for the value itself as a sequence of octets. 采用这种方式时，需要传输的信息被看作是一组“参数值”。每个参数值都会通过一个参数标识符来编码（通常这个标识符的长度是固定的，通常只是一个八位元，但有时可能需要使用更多的八位元来表示），接着是参数值的长度编码（同样以八位元表示，有时需要两个或更多的八位元来表示长度信息），最后才是参数值本身的编码，即一系列八位元的序列。

The parameter id was often said to identify the type of the parameter, so we have a Type field, a Length field, and a Value field, or a TLV encoding. 参数 id 通常被用来标识参数的类型。因此，我们设有 Type 字段、Length 字段以及 Value 字段，或者采用 TLV 编码方式来表示参数信息。

In these approaches, all fields were an integral number of octets, with all length counts counting octets, although some of the earliest approaches (not followed by ASN.1) had sixteen bit words as the fundamental unit, not octets. 在这些方法中，所有字段都被视为一个完整的八位元单元。所有的长度计数都是以八位元为单位进行的。不过，在一些早期的方法中（ASN.1 并不采用这些方法），十六位元的字元被作为基本单位，而不是八位元。

Once the way of encoding types and lengths is determined, the rest of the specification merely needs to determine what parameters are to appear on each message, what their exact id is, and how the values are to be encoded. 一旦确定了编码类型和长度的方法之后，剩下的工作就只是确定每条消息中应该包含哪些参数，这些参数的具体编号是什么，以及这些值应该如何进行编码。

This structure has a number of important advantages: 这种结构具有许多重要的优势：

• It makes it possible to give freedom to a sender to transmit the parameters in any order, perhaps making for simpler (sender) implementation. (Note that this is today seen as actually a bad thing to allow, not a good one!) • 这允许发送者以任意顺序传输参数，从而可能使实现更加简单。（不过，如今人们认为这种做法其实并不合适，不是一种好的做法。）

• It makes it possible to declare that some parameters are optional - to be included only when needed in a message. • 这使得可以声明某些参数为可选择的——只有在这些参数在消息中真正需要时才会被包含进来。

• It handles items of variable length. • 它可以处理长度不同的项目。

• It enables a basic "parsing" into a set of parameter values without needing any knowledge about the actual parameters themselves. • 它实现了基本的“解析”操作，将输入数据转换为一组参数值，而无需了解这些参数的具体含义。

And importantly - it enables a version 1 system to identify, to find the end of, and to ignore (if that is the desired behaviour), or perhaps to relay onwards, parameters that were added in a version 2 of the protocol. 重要的是，这种方式使得版本 1 的系统能够识别某些参数，找到这些参数的位置，并可以选择忽略它们（如果这是预期的行为）。或者，也可以将这些参数传递给后续版本。

The reader should recognise the relationship of these features to ASN.1 - the existence of "SET" (elements transmitted in any order), the "OPTIONAL" notation which can be applied to elements of a SET or SEQUENCE, and the variable length nature of many ASN.1 basic types. The version 1/version 2 issue is what is usually called "extensibility" in ASN.1. 读者应该能够识别出这些特性与 ASN.1 规范之间的关系。例如，“SET”概念指的是以任意顺序传输的元素；“OPTIONAL”标记可以用于描述集合或序列中的某些元素；而许多 ASN.1 基本类型的长度则是可变的。在 ASN.1 中，所谓“扩展性”指的是对版本 1 或版本 2 规范的处理能力。

The major extension beyond this "parameter" concept developed in the late 1970s with the idea of "parameter groups", used to keep close together related parameters. Here we encode a "group identifier", a group length encoding, then a series of TLV encodings for the parameters within the group. As before, the groups can appear in any order, and a complete group may be optional or mandatory, with parameters within that group in any order and either optional or mandatory for that group. Thus we have effectively two levels of TLV - the group level and the parameter level. 在 20 世纪 70 年代末，随着“参数组”概念的提出，这一体系得到了进一步的发展。所谓“参数组”，指的是将相关参数紧密地组合在一起的方式。在这里，我们首先为参数组编码一个“组标识符”，然后是对该组内各个参数的 TLV 编码。与之前一样，这些参数组可以以任意顺序出现；一个完整的参数组可能是可选的，也可能是必填的。而该组内的各个参数则可以是任意顺序的，且可以是可选的，也可以是必填的。因此，我们实际上有了两个层次的 TLV 结构——组级别和参数级别。

It is a natural extension to allow arbitrarily many levels of TLV, with the V part of all except the innermost TLVs being a series of embedded TLVs. This clearly maps well to the ASN.1 concept of being able to define a new type as a SEQUENCE or SET of basic types, then to use that new type as if it were a basic type in further SEQUENCEs or SETs, and so on to any depth. 这是一种自然的扩展，可以允许任意多的 TLV 层级。除了最内层的 TLV 之外，所有其他 TLV 的 V 部分都实际上是由一些嵌入式的 TLV 构成的序列。这显然符合 ASN.1 的概念：即可以将一种新类型定义为基本类型的序列或集合，然后像使用基本类型一样在后续的序列或集合中继续使用这种新类型，如此循环下去，直到无限深度。

Thus this nested TLV approach emerged as the natural one to take for the ASN.1 Basic Encoding Rules, and reigned supreme for over a decade. 因此，这种嵌套的 TLV 表示方法成为了处理 ASN.1 基本编码规则的自然选择，并且持续了十多年时间，成为最流行的做法。

To completely understand the Basic Encoding Rules we need: 要完全理解基本编码规则，我们需要：

• To understand the encoding of the "T" part, and how the identifier in the "T" part is allocated. • 需要了解“T”部分的编码方式，以及“T”部分中的标识符是如何被分配的。

• To understand the encoding of the "L" part, for both short "V" parts and for long "V" parts. • 为了理解“L”部分的编码方式，需要了解短“V”部分和长“V”部分的编码差异。

• For each basic type such as INTEGER, BOOLEAN, BIT STRING, how the "V" is encoded to represent the abstract values of that type. • 对于每种基本类型，例如 INTEGER、BOOLEAN、BIT STRING 等，都会说明如何编码“V”来表示该类型的抽象值。

• For each construction mechanism such as SEQUENCE or SET, how the encodings of types defined with that mechanism map to nested TLV structures. • 对于诸如 SEQUENCE 或 SET 之类的构建机制，由该机制定义的类型编码如何映射到嵌套的 TLV 结构中。

This is the agenda for the next chapter. 这是下一章的议程。

## 4 Extensibility or "future proofing" 4. 可扩展性或“面向未来的设计”

The TLV approach is very powerful at enabling the specification of a version 1 system to require specified action on TLV elements where the "T" part is not recognised. This allows new elements (with a distinct "T" part) to be added in version 2 of a specification, with a known pattern of behaviour from version 1 systems that receive such material. TLV 方法在定义版本 1 的系统时非常有效，它要求对 TLV 元素进行特定的处理，而此时“T”部分并不被识别。这样，在规范的版本 2 中就可以添加新的元素（这些元素具有独特的“T”部分），而来自版本 1 的系统的已知行为模式也可以被保留下来。

This interworking between version 1 and version 2 systems without the need for version 2 implementations to implement both the version 1 and the version 2 protocol is a powerful and important feature of ASN.1. 在版本 1 和版本 2 的系统之间实现互操作功能，而无需版本 2 的实现来同时支持版本 1 和版本 2 的协议，这是 ASN.1 的一个强大且重要的特性。

It is a natural outcome of the TLV approach to encoding in the Basic Encoding Rules, but if one seeks encodings where there is a minimal transfer of information down the line, it is important to investigate how to get some degree of "future-proofing" to allow interworking of version 1 and version 2 systems without the verbosity of the TLV approach. 这是 TLV 编码方法在基本编码规则中的自然结果。不过，如果希望实现一种能够最大程度减少信息传输量的编码方式，那么研究如何做到一定程度的“未来兼容”就变得非常重要了。这样就能实现版本 1 和版本 2 的系统之间的相互协作，而无需使用 TLV 方法的那种复杂编码方式。

Early discussions in this area seemed to indicate that future-proofing was only possible if a TLV style of encoding was used, but later work showed that provided the places in the protocol where version 2 additions might be needed were identified by a new notational construct (the ASN.1 "extensibility" ellipsis - three dots), then future-proofing becomes possible with very little overhead even in an encoding structure that is not in any way a TLV type of structure. 在这一领域的初步讨论表明，只有使用与 TLV 格式类似的编码方式，才能实现面向未来的设计。但后续的研究表明，只要通过一种新的表示方式来标识协议中可能需要添加功能的地方（即 ASN.1 中的“扩展性”省略号——三个点），那么即使在不采用 TLV 格式的结构中，也能以很少的额外开销实现面向未来的设计。

It was this recognition that enabled the so-called Packed Encoding Rules (PER) to be developed. 正是这种认识促成了所谓“打包编码规则”（PER）的提出。

## 5 First attempts at PER - start with BER and remove redundant octets 5. 首次尝试计算 PER 值——从 BER 值开始，然后去除多余的八位组。

This was a blind-alley! 这真是个疯狂的地方啊！

NOTE — Those with no knowledge of BER may wish to at lest skim the next chapter before returning to the following text, as some examples show BER encodings. 注意：对于那些不了解 BER 的人来说，建议在返回后续内容之前至少先阅读下一章的内容，因为其中有一些示例展示了 BER 编码的方式。

The first approach to producing more compact (packed) encodings for ASN.1 was based on a BER TLV-style encoding, but with recognition that in a BER encoding there were frequently octets sent down the line where this was the only possible octet value allowed in this position (at least in this version of the specification). This 第一种用于生成更紧凑的 ASN.1 编码的方法是基于 BER TLV 风格的编码。不过，这种编码方式存在一个问题：在 BER 编码中，经常会发送一些八位字节，而在这个位置，这些八位字节是唯一允许的值（至少在这个版本的规范中是如此）。

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/54379e17-c034-430b-894c-f77661f731e5/938407f05197da57daa2b8225483ecf566abb7269a6f32912231a7f5f63bf182.jpg)

applied particularly to the "T" values, but also frequently to the length field if the value part of the item (such as a BOOLEAN value) was fixed length. 这一用法主要适用于“T”值，但如果项目中的数值部分（例如布尔值）是固定长度的，那么也常常用于长度字段。

By allowing the Packed Encoding Rules to take account of constraints (on, for example, the length of strings or the sizes of INTEGERs), we can find many more cases where explicit transmission of length fields is not needed, because both ends know the value of the "L" field. 通过让打包编码规则考虑各种约束条件（例如字符串的长度或 INTEGER 类型的数据大小），我们可以找到更多的情况，在这种情况下不需要显式传输长度字段的值，因为双方都知道“L”字段的值。

A final "improvement" is to consider the "L" field for a SEQUENCE type. Here each element of the SEQUENCE is encoded as a TLV, and there is an outer level "TL" "wrapper" for the SEQUENCE as a whole. If we modify BER so that the "L" part of this wrapper is a count not of octets, but of the number of TLVs in the value part of the SEQUENCE, this count is again fixed (unless the SEQUENCE has OPTIONAL elements), and therefore often need not be transmitted, even if there are inner elements whose length might vary. 最后一个“改进”是考虑使用“L”字段来表示序列类型。在这里，序列中的每个元素都被编码为一个 TLV，而整个序列则有一个外部的“TL”级包装器。如果我们修改 BER 编码方式，使得这个包装器的“L”字段不是以八位元为单位来计数，而是以序列中 TLV 的数量来计算，那么这个计数就可以被固定下来（除非序列包含可选元素）。因此，通常不需要传输这个计数，即使某些内部元素的长度可能会有所不同。

Consider the ASN.1 type shown in figure III-1. The BER encoding (modified to count TLVs rather than octets for non-inner length fields) is shown in figure III-2. 请参考图 III-1 中所示的 ASN.1 类型。BER 编码的编码方式（修改为仅对 TLV 进行计数，而不是对八位元字段进行计数）如图 III-2 所示。

```txt
Example ::= SEQUENCE
{first INTEGER (0..127),
second SEQUENCE
{string OCTET STRING (SIZE(2)),
name PrintableString (SIZE(1..8)) },
third BIT STRING (SIZE (8)) }

Figure III-1: An example for encoding 
```

You will see from Figure III-2 that there are a total of 23 octets sent down the line, but a receiver can predict in advance the value of all but 11 of them - those marked as {????} (and knows precisely where these 11 occur). Thus we need not transmit the remaining 12 octets, giving a 50% reduction in communications traffic. Attractive! 从图 III-2 中可以看出，总共有 23 个八位组被发送出去。不过，接收器可以提前预测出其中除了 11 个之外的所有八位组的值——那些被标记为{????}的八位组——并且能够准确知道这 11 个八位组出现在哪几个位置。因此，我们无需发送剩下的 12 个八位组，这样一来，通信流量就减少了 50%。真是个不错的改进啊！

The approach, then, was to take a BER encoding as the starting point, determine rules for what 因此，我们的方法是以 BER 编码作为起点，然后确定相关的规则。

```txt
{U 16} -- Universal class 16 ("T" value for SEQUENCE)
{3} -- 3 items ("L" value for SEQUENCE)
{U 2} -- Universal class 2 ("T" value for "first")
{1} -- 1 octet ("L" value for "first")
{?????} -- Value of "first"
{U 16} -- Universal class 16 ("T" value for "second")
{2} -- 2 items ("L" value for "second")
{U 3} -- Universal class 3 ("T" value for "string")
{2} -- 2 octets ("L" value for "string")
{?????}{?????} -- Value of "string"
{U 24} -- Universal class 24 ("T" value for "name")
{?????} -- 1 to 8 ("L" value for "name" - 5 say)
{?????}{?????}{?????}{?????}{?????} -- Value of "name"
{U 4} -- Universal class 4 "T" value for "third"
{3} -- 3 octets ("L" value for "third")
{0} -- 0 unused bits in last octet of "third" "V"
{?????}{?????} -- Value of "third"

Figure III-2: Modified BER encoding of figure III-1 
```

octets need not be transmitted, and to delete those octets from the BER encoding before transmission, re-inserting them (from knowledge of the type definition) on reception before performing a standard BER decode. 这些八位组不必被传输出去；在传输之前，可以从 BER 编码中删除这些八位组。而在接收后执行标准的 BER 解码之前，可以根据类型定义的知识将这些八位组重新插入到编码中。

Work was done on this approach over a period of some three years, but it fell apart. A document was produced, getting gradually more and more complex as additional (pretty ad hoc) rules were added on what could and could not be deleted from a BER encoding, and went for international ballot. An editing meeting was convened just outside New York (around 1990), and the comments from National Bodies were only faxed to participants at the start of the meeting. 这种方法的实施过程持续了大约三年时间，但最终失败了。最终形成了一份文件，其中包含了越来越复杂的规则，这些规则是根据各种具体情况来确定的，关于哪些内容可以被删除，哪些内容则必须保留。这份文件随后进行了国际层面的审议。大约在 1990 年，在纽约附近召开了一次编辑会议，各国机构的意见只是以传真方式发送给与会者。

Imagine the consternation when the dozen or so participants realised that EVERY National Body had voted "NO", and, moreover, with NO constructive comments! The approach was seen as too complex, too ad hoc, and (because it still left everything requiring an integral number of octets) insufficient to produce efficient encodings of things like "SEQUENCE OF BOOLEAN". It was quite clearly dead in the water. 当那十几名参与者意识到每一个国家机构都投了“反对”票时，他们会感到多么的困惑啊！而且，这些反对意见还毫无建设性可言！这种处理方式被认为过于复杂、过于臃肿，而且（因为它仍然需要大量的八位二进制数来表示各种信息），因此无法有效地处理像“布尔序列”这样的数据。显然，这种方案已经彻底失败了。

Many people had pre-booked flights which could not be changed without considerable expense, but it was clear that what had been planned as a week-long meeting was over. The meeting broke early at about 11am for lunch (and eventually reconvened late at about 4pm). Over the lunch-break much beer was consumed, and the proverbial back-of-a-cigarette-packet recorded the discussions (actually, I think it was a paper napkin – long since lost!). PER as we know it today was born! The rest of the week put some flesh on the bones, and the next two years produced the final text for what was eventually accepted as the PER specification. Implementations of tools supporting it came a year or so later. 许多人已经预订了航班，这些预订如果不花费大量费用是无法更改的。显然，原本计划为期一周的会议已经结束了。会议在上午 11 点左右提前结束，大家去吃了午饭（最终在下午 4 点左右再次聚在一起）。在午休期间，大家喝了很多啤酒。所谓的“会议记录”其实是一张香烟包装纸上的笔记——不过那张纸已经丢失了！就这样，PER 规范诞生了！在接下来的几周里，相关的工作得到了进一步的发展，而在接下来的两年里，最终形成了被大家认可的 PER 规范的最终版本。支持该规范的工具也在一年后开始被实际应用起来。

## 6 Some of the principles of PER 6. PER 的一些原则

## 6.1 Breaking out of the BER straight-jacket 6.1 摆脱这种思维定势的束缚

Probably the most important decisions in that initial lunch-time design of PER were: 在 PER 的初始设计阶段， probably 最重要的几个决定包括：

To start with a clean piece of paper (or rather napkin!) and ignore BER and any concept of TLV. This was quite radical at the time, and the beer probably helped people to think the unthinkable! 首先，先在一张干净的纸上开始吧（或者更确切地说，是一张餐巾纸！），然后忽略“BER”这个概念，也别考虑“TLV”这个术语了。当时这个想法相当激进，而啤酒或许帮助人们实现了那些原本无法想象的想法！

## Initial "principles" 最初的“原则”

• Forget about TLV. • 别再考虑 TLV 了。

• Forget about octets - use bits. • 忘掉字节的概念吧——使用比特 instead。

• Recognise constraints (subtypes). • 识别各种约束条件（类型）。

• Produce "intelligent" encodings. • 生成“智能”的编码方式。

• Forget "extensibility" (initially). • 忘掉“可扩展性”这个概念吧（最初是这样说的）。

• Not to be constrained to using an integral number of octets - another quite radical idea. • 不必局限于使用固定数量的数据位；这其实是一个相当激进的想法。

To take as full account of constraints (subtyping) in the type definition as could sensibly be done. (BER ignored constraints, perhaps largely because it was produced before the constraint/subtype notation was introduced into ASN.1, and was not modified when that notation came in around 1986). 在类型定义中，应尽可能全面地考虑各种限制条件（子类型定义）。不过，BER 并没有考虑这些限制条件，可能是因为它在 1986 年左右引入 ASN 规范之前就已经被开发出来了，而且当这种表示法被引入后也没有进行任何修改。

• To produce the sort of encoding that a (by now slightly drunk!) intelligent human being would produce - this was quite a challenge! • 要创造出那种（现在已经有点醉了！）聪明的人类才会使用的编码方式——这真是个相当大的挑战啊！

• Not to consider "extensibility" issues. This was a pragmatic decision that made the whole thing possible over a (long) lunch-time discussion, but of course provision for "futureproofing" had to be (and was) added later. • 没有考虑“可扩展性”问题。这是一个务实的决定，通过一次漫长的午餐时间讨论就决定了整个系统的实现方式。不过，当然之后还是增加了一些“面向未来”的考虑因素。

So how would you the reader encode things? Whatever you think is the obvious way is probably what PER does! In all the following cases, the "obvious" solution is what PER does. 那么，作为读者的你，会如何对信息进行编码呢？你认为最显而易见的方法，很可能就是 PER 所采用的方法吧！在所有这些情况下，所谓的“显而易见”的解决方案，其实就是 PER 所采取的方案。

What about the encoding of BOOLEAN? Clearly a single bit set to zero or one is the "obvious" solution. 那么，BOOLEAN 的编码方式是什么呢？显然，将一个比特位设置为 0 或 1 就是“显而易见”的解决方案。

What about 那怎么样呢？

INTEGER (0..7) 整数类型 (0..7)

and 以及

INTEGER (8..11) 整数类型（范围：8 到 11）

Clearly a three-bit encoding is appropriate for the former and a two-bit encoding for the latter. 显然，对于前者来说，使用三位编码是合适的；而对于后者，则应该使用两位编码。

© OS, 31 May 1999 © OS，1999 年 5 月 31 日

An INTEGER value restricted to a 16-bit range could go into two octets with no length field. 一个限制在 16 位范围内的整数值，可以通过两个八位元来表示，而无需使用长度字段。

But what about an unconstrained INTEGER? (Meaning, in theory, integer values up to infinity, and with BER capable of encoding integer values that take millions of years to transmit (even over super- fast lines)? Clearly an "L" will be needed here to encode the length of the integer value (and here you probably want to go for a length count in octets). 但是，有没有一种不受限制的整数表示方式呢？理论上来说，可以表示无限大的整数值，而且 BER 能够编码那些需要数百万年才能传输完毕的整数值（即使是在超高速的传输线路上）。显然，这里需要使用一个“L”来表示整数的长度（你可能希望用八位二进制数来表示这个长度）。

If you have read about the details of BER encodings of "L", you will know that for length counts up to 127 octets, "L" is encoded in a single octet, but that BER requires three octets for "L" once the count is more than 255. In PER, the count is a count of bits, items, or octets, but only goes beyond two octets for counts of 64K or more - a fifty per cent reduction on the size of "L" in many cases compared with BER. 如果你了解过“L”的 BER 编码细节，就会知道：当长度不超过 127 个八位元时，单个八位元就可以表示“L”的值；而当长度超过 255 个八位元时，就需要三个八位元来表示“L”。在 PER 编码中，计数单位是位、项或八位元，但只有当计数达到 64K 或更高时才会超过两个八位元——与 BER 编码相比，PER 编码所占用的大小通常只会增加 50%。

For virtually all values of an unconstrained INTEGER, we will get a one octet "L" field, followed by the minimum number of octets needed to hold the actual value being sent. This is the same as BER. 对于几乎所有不受限制的整数值，我们都会得到一个八位元的“L”字段，随后是表示所发送数值所需的最小八位元数量。这与 BER 的情况相同。

## 6.2 How to cope with other problems that a "T" solves? 6.2 如何应对“T”型人格所引发的其他问题呢？

So far, no mention has been made of a "T" field for PER. Do we ever need one? There are three main areas in BER where the "T" field is rather important. These are: 到目前为止，关于 PER 的“T”字段还没有被提及。我们真的需要这个字段吗？在 BER 的三个主要区域中，“T”字段确实非常重要。这些区域包括：

```txt
- Use a "choice-index".
- SET in a fixed order.
- Bit-map for OPTIONAL elements. 
```

• To identify which actual alternative has been encoded as the value of a CHOICE type (remember that all alternatives of a CHOICE are required to have distinct tags, and hence have distinct "T" values). • 目的是确定哪个实际选项被编码为“CHOICE”类型的值（记住，所有“CHOICE”选项的标签都必须各不相同，因此它们的“T”值也必然不同）。

• To identify the presence or absence of OPTIONAL elements in a SEQUENCE (or SET). • 用于识别在序列（或集合）中是否存在可选元素。

• To identify which element of a SET has been encoded where (remember that elements of a SET can be encoded and sent in any order chosen by the sender). • 目的是确定某个集合中的元素已被编码到了哪个位置（记住，集合中的元素可以以发送者选择的任何顺序进行编码和传输）。

How to do these things without a "T" encoding for each element? 如何在不为每个元素都进行“T”编码的情况下完成这些操作呢？

To cope with alternatives in a CHOICE, PER encodes a "choice-index" in the minimum bits necessary: up to two alternatives, one bit; three or four alternatives, two bits; five to seven alternatives, three bits; etc. 为了在处理多个选项时保持简洁，PER 编码方式会以一种最少的位数来表示“选项索引”：最多两个选项时使用 1 位；三个或四个选项时使用 2 位；五到七个选项时使用 3 位；以此类推。

At this point we can observe one important discipline in the design of PER. The fieldwidth (in bits) for any particular part of the encoding (in this case the field-width of the choice-index) does not (must not) depend on the abstract value being 在这一点上，我们可以观察到 PER 设计中一个重要的规则。对于任何特定的编码部分，其字段宽度（以位为单位）不得依赖于该抽象值的实际数值。

The important field-length principle or rule: Encode into fields of an arbitrary number of bits, but the length of fields must be statically determinable from the type definition, for all values. 重要的字段长度原则或规则是：数据应被编码到任意位数的字段中，但所有值的字段长度必须能够从类型定义中静态确定。

transmitted, but can be statically determined by examining the type definition. Hence it is known unambiguously by both ends of the communication - assuming they are using the same type definition. But there is the rub! If one is using a version 1 type definition and the other a version 2 type definition .... but we agreed not to consider this just yet! 虽然可以传输，但可以通过检查类型定义来静态地确定其状态。因此，只要双方使用相同的类型定义，那么通信的双方就能明确无误地理解对方的含义。不过，这里有一个问题！如果一方使用的是版本 1 的类型定义，而另一方则使用版本 2 的类型定义……不过我们暂时先不讨论这个问题吧！

What about OPTIONAL elements in a SET or SEQUENCE? Again, the idea is pretty obvious. We use one bit to identify whether an OPTIONAL element is present or absent in the value of the 那么，在集合或序列中出现的可选元素该怎么办呢？这个思路其实相当简单。我们使用一个比特位来表示某个可选元素是否存在于该值中。

SET or SEQUENCE. In fact, these bits are all collected together and encoded at the start of the SET or SEQUENCE encoding rather than in the position of the optional element, for reasons to do with "alignment" discussed below. SET 或 SEQUENCE。实际上，这些位都是集中在一起在 SET 或 SEQUENCE 的编码开始时就被编码的，而不是在可选元素的位置上进行编码。这一做法与下面提到的“对齐”问题有关。

And so to the third item that might require a "T". What about the encoding of SET - surely we need the "T" encodings here? Start of big debate about the importance of SET (where elements are transmitted in an order determined by the sender) over SEQUENCE (where the order of encodings is the order of elements in the type definition), and of the problems that SET causes. In addition to the verbosity of introducing some form of "T" encoding, we can also observe that: 那么，第三个需要“T”编码的项目是什么呢？关于 SET 的编码方式——显然在这里我们需要使用“T”编码。关于 SET 与 SEQUENCE 的重要性之争开始了：在 SET 中，元素的顺序是由发送方决定的；而在 SEQUENCE 中，编码的顺序则遵循类型定义中的元素顺序。此外，SET 还会带来一些问题。除了引入某种“T”编码方式所带来的复杂性之外，我们还可以注意到：

Allowing sender's options produces a combinatoric explosion in any form of exhaustive test sequence (and hence in the cost of conformance checking) to check that (receiving) implementations behave correctly in all cases. 允许使用发送方的选项会在任何形式的穷举测试序列中引发巨大的组合可能性（因此也会增加一致性检查的成本），以确保在所有情况下，（接收方的）实现都能正确运行。

The existence of multiple ways of sending the same information produces what in the security world is called a "side-channel" - a means of transmitting additional information from a trojan horse by systematically varying the senders options. For example, if there are eight elements in a SET, then 256 bits of additional information can be transmitted with each value of that SET by systematically varying the order of elements. 存在多种可以传递相同信息的方式，这在安全领域被称为“侧信道”攻击——即通过系统地改变传输过程中的选项，从木马程序中获取额外的信息。例如，如果有一个集合中有八个元素，那么通过系统地改变元素的排列顺序，每个元素都可以携带 256 位的额外信息。

This discussion led to the development of a further principle for PER: there shall be NO sender's options in the encoding unless there was an excellent reason 这次讨论促成了 PER 的又一原则的形成：除非有充分的理由，否则在编码过程中不应存在发送者可选择的选项。

The sender's options principle/rule: Don't have any! 发送者的选择原则/规则：不要有任何选择！

for introducing them. PER effectively has no sender's options. A canonical order is needed for transmitting elements of a SET, and after much discussion, this was taken to be the tag order of the elements (see the next chapter for more detail), rather than the textually printed order. (In allocating choice-index values to alternatives of a choice, the same tag-order, rather than textual order is also used, for consistency). 用于引入这些元素。实际上，PER 并没有“发送者选项”这一功能。在传输 SET 中的元素时，需要一种规范的排序方式。经过多次讨论后，人们决定采用元素的标签顺序作为排序依据（更多细节请参见下一章），而不是文本中打印出的顺序。（在为选择项分配选择索引值时，同样也采用标签顺序而非文本顺序，以保持一致性。）

It should, however, be noted that the term "PER" strictly refers to a family of four closely related encoding rules. The most important is "BASIC-PER" (with an ALIGNED and an UNALIGNED variant discussed later). Although BASIC-PER has no senders options, it is not regarded as truly a canonical encoding rule because values of the elements of a SET OF are not required to be sorted into a fixed order, and no restrictions are placed on the way escape sequences are used in encodings of GeneralString. (If neither of these two types are used in an application specification, then BASIC-PER is almost canonical (there are some other unimportant complex cases that never arise in practice where it is not fully canonical. There is a separate CANONICAL-PER (also with an ALIGNED and an UNALIGNED version) that is truly canonical even when these types are present. 不过，需要指出的是，"PER"这个术语实际上指的是一组密切相关的编码规则。其中最重要的是"BASIC-PER"（后面还会介绍它的变体——ALIGNED 和 UALIGNED）。虽然 BASIC-PER 没有关于发送者的选项，但它并不被视为真正的规范编码规则，因为 SET\_OF 元素的取值不需要按照固定顺序进行排序，而且在对 GeneralString 进行编码时，对转义序列的使用也没有任何限制。（如果应用程序规范中既不使用这两种类型，那么 BASIC-PER 几乎可以算作规范编码了。不过，在实际使用中，偶尔会出现一些不太重要的复杂情况，这些情况并不会导致 BASIC-PER 完全不符合规范。另外还有一种名为 CANONICAL-PER 的编码规则，它同样包含 ALIGNED 和 UALIGNED 两种变体，即使存在这两种类型，CANONICAL-PER 仍然可以算作真正的规范编码。）

## 6.3 Do we still need T and L for SEQUENCE and SET headers? 6.3 对于 SEQUENCE 和 SET 的头部，我们还需要 T 和 L 这些字段吗？

Clearly we do not! We need no header encodings for these types, provided we can identify the presence or absence of optional elements (which is done by the bit-map described earlier). 显然，我们并不需要这种编码方式！对于这些类型的数据，我们不需要任何头部编码，只要我们能够识别出可选元素的存在或缺失即可（这可以通过之前提到的位图方法来实现）。

"Wrappers" are no longer needed. Well ... that is sort of true - but see the discussion of extensibility below, that re-introduces wrappers for elements added in version 2! “包装层”已不再必要了。嗯……某种程度上来说确实是这样——不过请参考下面关于可扩展性的讨论吧，因为在版本 2 中新增的元素需要重新使用包装层！

## 6.4 Aligned and Unaligned PER 6.4 对齐后的与非对齐后的 PER 值

But here we look at another feature of PER. Basically, PER produces encodings into fields that are a certain number of bits long and which are simply concatenated end-to-end for transmission. But there was recognition from the start that for some ASN.1 types (for example, a sequence of two-byte integers), it is silly to start every component value at, say, bit 6. Insertion of two padding bits at the start of the sequence-of value 不过，这里我们关注 PER 的另一个特性。实际上，PER 会将数据编码成若干位长的字段，这些字段会依次连接在一起进行传输。但从一开始我们就意识到，对于某些 ASN 类型的数据（例如，由两个字节整数组成的数据序列），如果每个组件值都从第 6 位开始，那显然是不合理的做法。因此，在数值序列的开头添加两个填充位才是合适的做法。

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/54379e17-c034-430b-894c-f77661f731e5/99cf5af4eaf50b4889c4973c4c6732e5f3d368823905c2a328c76facc36f0a78.jpg)

would probably be a good compromise between CPU costs and line costs. 这或许可以算是 CPU 成本与线路成本之间的一个不错的折中方案吧。

This led to the concept of encoding items into bit-fields (which were simply added to the end of the bits in earlier parts of the encoding) or into octet-aligned-bit-fields where padding bits were introduced to ensure that the octet-aligned-bit-fields started on an octet boundary. 这就引出了将各项数据编码到位字段中的概念（这些位字段简单地被添加到编码过程中的各个位之后）。或者，也可以将它们编码到以八位为单位的位字段中，同时引入填充位来确保这些位字段能够从八位边界处开始。

The intelligent reader (aren't you all?) will note that whilst the length of fields is (has to be) statically determined from the type, the number of padding bits to be inserted before an octetaligned-bit-field is not fixed. The number of bits in the earlier part of the encoding can depend on whether optional elements of SET and SEQUENCE are present or not, and on the actual alternative chosen in a CHOICE. But of course, the encoding always contains information about this, and hence a receiving implementation can always determine the number of padding bits that are present and that have to be ignored. Notice that whether a field is a bit-field or an octetaligned-bit-field again has to be (and is) statically determined from the type definition - it must not depend on the actul value being transmitted, or PER would be bust! 聪明的读者应该会注意到，虽然字段的长度是由类型定义静态确定的，但在一个八位元字段之前需要插入的填充位数却不是固定的。编码中前面部分的位数取决于是否包含了 SET 和 SEQUENCE 中的可选元素，以及 CHOICE 中实际选择的选项。不过，当然，编码中总是包含有关这些信息的说明，因此接收方可以实现程序来确定存在的填充位数以及哪些位需要被忽略。另外，一个字段是单字节字段还是八位元字段，同样是由类型定义静态确定的——它不得依赖于传输中的实际值，否则 PER 机制就会失效！

The concept of "octet-aligned-bit-fields" and "padding bits" was in the original design, but later people in air traffic control wanted the padding bits removed, and we now have two variants of PER. Both formally encode into a sequence of "bit-fields" and "octet-aligned-bit-fields", depending on the type definition, but for "unaligned PER", there is no difference in the two - padding bits are never inserted at the start of "octet-aligned-bit-fields". With aligned PER, they are. 在最初的设计中，确实采用了“按八位组对齐的位字段”和“填充位”这一概念。不过后来，空中交通管制部门希望去掉这些填充位。因此，我们现在有了两种形式的 PER 编码方式。这两种方式都通过一系列“位字段”和“按八位组对齐的位字段”来编码数据，具体取决于所定义的数据类型。不过，对于“非对齐 PER”来说，这两种方式并没有区别——在“按八位组对齐的位字段”中，根本不会插入填充位。而对于“对齐 PER”来说，则会在这些位字段中插入填充位。

There are actually a couple of other differences between aligned and unaligned PER, but these are left to the later chapter on PER for details. 实际上，对齐的 PER 与非对齐的 PER 之间还有几处差异，但这些细节可以在后面关于 PER 的章节中了解到。

As a final comment - if you want to try to keep octet alignment for as long as possible after insertion of padding bits, then using a single bit to denote the presence or absence of an OPTIONAL element in a SEQUENCE or SET is probably not a good idea - better to collect all such bits together as a "bit-map" at the start of the encoding of the SEQUENCE or SET. This was part of the original back-of-cigarette-packet design and was briefly referred to earlier. That feature is present in PER. 最后一点说明——如果你希望在整个编码过程中尽可能保持八位组的对齐，那么使用单个位来表示序列或集合中是否存在某个可选元素可能并不是一个好主意。更好的做法是在编码开始时，将所有这样的位合并成一个“位图”形式。这一设计最初出现在“香烟包装背面”方案中，之前也简要提到过。现在这一功能已经在“PER”中实现了。

## 7 Extensibility - you have to have it! 7 可扩展性——你必须拥有它！

## Third attempt! 第三次尝试！

One bit says it all - it is a version 1 value, or it contains wrapped-up version 2 material. 只要有一点信息就足够了——要么是版本 1 的内容，要么包含了版本 2 的整合信息。

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/54379e17-c034-430b-894c-f77661f731e5/3d6b16fc2ed327099aecaadc051730f4a50279d15e1f88e463f5b2c8a1dbef26.jpg)

When the second approach to better encodings (described above) was balloted internationally, it almost failed again. 当上述第二种改进编码的方法在国际上被提出时，它同样几乎再次失败了。

It is clear from the above discussion that unless both ends have exactly the same type definition for their implementation, all hell will break loose - pardon the term. They will have different views on the fields and the field lengths that are present, and will produce almost random abstract values from the encodings. 从上述讨论中可以清楚地看出，除非两个端点的实现方式完全相同，否则将会出现严重的问题。它们对存在的字段以及字段长度会有不同的理解，从而导致从编码中产生的数值几乎都是随机的。

But do we really want to throw in the towel and admit that a very verbose TLV style of encoding is all that is possible if we are to be "future-proof"? NO! 但是，我们真的想放弃努力，承认如果我们要确保代码的“未来可扩展性”，那么唯一可行的编码方式就是那种非常冗长的 TLV 格式吗？不！我们绝对不想这样做。

How to allow version 2 to add things? How about notation to indicate the end of the "root" (version 1) specification, and the start of added version 2 (or 3 etc) material? Will this help? 如何允许版本 2 添加一些内容呢？有没有什么方式可以表示“根”版本（版本 1）的结束，以及新增的版本 2（或 3 等）内容的开始呢？这样做会有帮助吗？

The most common case for requiring "extensibility" is the ability to add elements to the end of SETs and SEQUENCEs in version 2. 需要“可扩展性”的最常见情况是在版本 2 中，能够向 SET 和-sequence 的末尾添加元素。

Later, people argued - successfully - for the need to add elements in the middle of SETs and SEQUENCEs, and we got the "insertion point" concept described in an earlier Section. 后来，人们成功地提出了在 SET 和 SEQUENCE 的中间添加元素的必要性，于是我们就有了前面章节中提到的“插入点”概念。

But let's stick to adding at the end for now. Suppose we have added elements (most of which are probably going to be OPTIONAL) at the end of a SEQUENCE, or added alternatives in a CHOICE, or added enumerations in an ENUMERATED, or relaxed constraints on an INTEGER (that list will do for now!). 不过，目前我们先暂且保持原样吧。假设我们在序列的末尾添加了元素（其中大部分可能是可选的），或者在选择项中增加了备选方案，在枚举项中添加了枚举值，又或者在整数约束上放宽了一些限制（目前列出这些元素就可以了！）。

How to handle that? We first require that a type be marked "extensible" if we want "futureproofing" (this is the ellipsis that can appear in many ASN.1 types). This warns the version 1 implementation that it may be hit with abstract values going beyond the version 1 type, but more importantly, it introduces one "extended" bit at the head of the version 1 encodings of all values of that type. 该如何处理这个问题呢？首先，如果我们希望实现“面向未来”的功能，那么该类型必须被标记为“可扩展”类型（这种省略号常见于许多 ASN.1 类型中）。这样就能提醒版本 1 的实现，该类型可能会包含超出版本 1 类型的抽象值。更重要的是，这种方式会在该类型所有值的版本 1 编码中添加一个“扩展”位。

The concept is that any of these "extensible" types has a "root" set of abstract values - version 1 abstract values. If the abstract value being sent (by a version 1, version 2, or version 3, etc implementation) is within the root, the "extended" bit is set to zero, and the encoding is purely the encoding of the version 1 type. But if it is set to 1, then abstract values introduced in version 2 or later are present, and version 1 systems have a number of options, but importantly, extra length (and sometimes identification) fields are included to "wrap-up" parts or all of these new abstract values to enable good interworking with version 1 systems. The "exception marker" enables specifiers to say how early version systems are to deal with material that was added in later versions, and (in the views of this author) should always be included if the extensibility marker is introduced. 这个概念指的是，这些“可扩展”的类型都有一组“根”抽象值——即版本 1 的抽象值。如果所传递的抽象值属于根集合，那么“可扩展”位会被设置为 0，此时编码仅针对版本 1 的类型进行。但如果该位被设置为 1，那么版本 2 或更高版本的抽象值就会被包含进来。对于版本 1 的系统来说，虽然有一些选项，但重要的是，会包含额外的长度（有时还包括标识）字段，以便将这些新的抽象值“整合”进来，从而实现与版本 1 系统的良好互操作性。而“扩展标记”则允许指定器指定早期版本的系统如何处理在后续版本中添加的内容。笔者认为，如果引入了可扩展性标记，那么“扩展标记”应该始终被包含进来。

The exact form of encodings for "extensible" types is discussed in more detail in the PER chapter following. later in this section. 关于“可扩展”类型的具体编码形式，将在下一节的 PER 章节中详细讨论。

## 8 What more do you need to know about PER? 关于 PER，你还想知道哪些信息呢？

It is interesting to note that whilst PER is now defined without any reference to BER (except for encoding the value part of things like object identifiers and generalizedtime and real types), a PER encoding of a value of the type shown in Figure III-1 actually produces exactly the same 11 octets (shown in Figure III-2) that would have been produced in the earlier (abandonned) approach! 有趣的是，虽然 PER 的定义现在不再涉及 BER，除了对对象标识符以及通用时间类型和实数类型等值的编码之外，但图 III-1 中所示类型的值的 PER 编码实际上会产生与早期方法（已被弃用）相同的 11 个八位组（如图 III-2 所示）。

This chapter has introduced most of the concepts of PER, but there are rather more things to learn about PER than about BER. These are all covered in the next chapter-but-one. 这一章已经介绍了 PER 的大部分概念，不过关于 PER 的知识比关于 BER 的知识要多得多。所有这些内容都将在下一章中详细讨论。

You need to know (well, you probably don't, unless you are writing an ASN.1 compiler tool! See the first part of this chapter!): 你需要知道这一点（不过，实际上你可能并不需要知道它，除非你正在编写某种 ASN 编译器工具！请参阅本章的第一部分！）：

• What constraints (subtyping) affect the PER encoding of various types (these are called "PER-visible constraints"). • 有哪些限制因素（类型划分）会影响各种类型的数据的 PER 编码方式（这些被称为“PER 可见限制”）。

• What is the general structure of the encoding ("bit-fields" and "octet-aligned-bit-fields", and how is a "complete encoding" produced. • 编码的一般结构是什么？比如“位字段”和“按字节排列的位字段”，以及如何生成“完整编码”。

• When are length fields included, and when are "lengths of lengths" needed, and how are they encoded. • 长度字段通常在什么情况下会被包含进来？什么时候需要显示“长度字段的详细内容”？它们是如何进行编码的？

• How PER encodes SEQUENCEs, SETs, and CHOICEs. (You already have a good idea from the above text). • PER 如何编码序列、集合和选择项。（从上文来看，你已经对这一点有了一定的了解了。）

• How PER encodes all the other ASN.1 types. (Actually, it references the BER "V" part encoding a lot of the time.) • PER 如何编码所有其他 ASN.1 类型的数据。（实际上，它经常引用 BER 的“V”部分来进行编码。）

• How does the presence of the "extensibility marker" affect PER encodings. (Again, the above has given some outline of the effect - a one-bit overhead if the abstract value is in the root, and generally an additional length field if it is not. • “可扩展标记”的存在如何影响 PER 编码方式？（再次强调，上述内容已经简要介绍了这一效果——如果抽象值位于根节点，则会增加一个比特位的开销；如果不在根节点上，通常会需要一个额外的长度字段来表示数据长度。）

These are all issues that have been touched on above, but which are treated more fully later. 这些都是上面已经提到过的问题，不过后面会进一步详细讨论。

## 9 Experience with PER 9 在 PER 方面的经验

There is now a lot of experience with PER applied to existing protocol specifications, and there is a growing willingness among specifiers to produce PER-friendly specifications (that is, specifications where constraints are consistently applied to integer fields and lengths of strings where appropriate). 现在，在将 PER 技术应用于现有协议规范方面已经积累了丰富的经验。而且，越来越多的规范制定者愿意编写符合 PER 规范的规范——也就是说，这些规范能够确保约束条件始终适用于整数字段以及字符串的长度限制。

Bandwidth reductions (even with added general-purpose compression - surprise?). CPU-cycle reductions (real surprise). Complexity - only at analysis time! Relation to use of tools - increases the advantages of tools. 带宽的减少（即使加上了通用压缩技术，还是会有惊喜吧？）。CPU 周期的减少（真是令人惊讶）。复杂性——只在分析阶段出现！与工具使用的关系——提升了工具的优势。

There were some surprises when PER implementations started to become available. 当那些基于 PER 的实现方式开始被广泛应用时，确实出现了一些意外情况。

First of all, it became possible to apply general-purpose compression algorithms to both the BER and the PER encodings of existing protocols, and it turned out that such compression algorithms produced about a 50% reduction in BER encodings (known for a long-time), but also produced a 50% reduction in PER encodings, which (uncompressed) turned out to be about a 50% reduction of the uncompressed BER encodings. Interesting! 首先，现在可以将通用的压缩算法应用于现有协议的 BER 编码和 PER 编码。结果表明，这种压缩算法能够将 BER 编码的复杂度降低约 50%（这一特性早已被认识到）。同样，PER 编码的复杂度也降低了 50%。而未经压缩的 BER 编码复杂度则降低了约 50%。真是有趣！

If you apply Shannon's information theory, it is perhaps not quite so surprising. A BER encoding more or less transmits complete details of the ASN.1 type as well as the value of that type. PER transmits information about only the value, assuming that full details of the type are already known at both ends. So an uncompressed PER encoding carries less information, and can be expected to be smaller than, an uncompressed BER encoding, but the same statement applies to compressed versions of these encodings. This is borne out in practice. 如果应用香农信息理论来解释这种情况，那么其实并不那么令人惊讶。BER 编码或多或少会传输 ASN.1 类型的完整信息以及该类型的值。而 PER 编码则只传输值的信息，前提是双方都已经知道了该类型的完整细节。因此，未压缩的 PER 编码所携带的信息量较少，预计其大小也会小于未压缩的 BER 编码。同样的情况也适用于这些编码的压缩版本。实际上，这一点在实践中也得到了验证。

<table><tbody><tr><td colspan="2">SEQUENCE</td></tr><tr><td data-imt-p="1">{ firstfield { 第一个字段 }</td><td data-imt-p="1">INTEGER (0..7), 整数类型（0~7），</td></tr><tr><td data-imt-p="1">secondfield 第二个领域</td><td data-imt-p="1">BOOLEAN, 布尔类型，</td></tr><tr><td data-imt-p="1">thirdfield 第三领域</td><td data-imt-p="1">INTEGER (8..11), 整数类型（8..11），</td></tr><tr><td data-imt-p="1">fourthfield 第四领域</td><td>SEQUENCE</td></tr><tr><td data-imt-p="1">{fourA {四 A</td><td data-imt-p="1">BOOLEAN, 布尔类型，</td></tr><tr><td data-imt-p="1">fourB 四 B</td><td data-imt-p="1">BOOLEAN} 布尔类型}</td></tr></tbody></table>

Secondly - and this WAS a surprise to most ASN.1 workers - the number of CPU cycles needed to produce an ASN.1 PER encoding proved to be a lot LESS than those required to produce an ASN.1 BER encoding (and similarly for encoding). Why? Surely PER is more complex? 其次——这一点让大多数 ASN 从业者都感到意外——用于生成 ASN.1 PER 编码所需的 CPU 周期数量，实际上比生成 ASN.1 BER 编码所需的周期数量要少得多。为什么呢？显然，PER 编码的复杂度应该更高吧？

It is true that to determine the encoding to produce (what constraints apply, the field-widths to use, whether a length field is needed or not) is much more complex for PER than for BER. But that determination is static. It is part of generating (by hand or by an ASN.1 "compiler") the code to do an encoding. 确实，对于 PER 来说，确定适用的编码方式（包括哪些约束条件、需要使用哪些字段宽度、是否需要长度字段等）要比对于 BER 复杂得多。不过，这种确定编码方式属于静态操作。它实际上是生成编码代码的步骤的一部分——无论是手动进行还是通过 ASN.1“编译器”来生成代码。

At encode time, it is far less orders to take an integer from memory, mask off the bottom three bits, and add them to the encoding buffer (that is what PER needs to do to encode a value of "INTEGER (0..7)") than to generate (and add to the encoding buffer) a BER "T" value, a BER "L" value (which for most old BER implementations means testing the actual size of the integer value, as most old BER implementations ignored constraints), and then an octet or two of actual value encoding. Similarly for decoding. 在编码过程中，从内存中取出一个整数、屏蔽掉最下面的三个位，然后将其添加到编码缓冲区中的操作，比生成并添加到编码缓冲区中的一个 BER“T”值、一个 BER“L”值要简单得多。对于 BER 来说，生成 BER“L”值意味着需要测试整数值的实际大小，因为大多数旧的 BER 实现都忽略了这种约束。此外，还需要对实际数值进行一到两个字节的编码。解码过程也是如此。

There is a further CPU-cycle gain in the code handling the lower layers of the protocol stack, simply from the reduced volume of the material to be handled when PER is in use. 在处理协议栈较低层的部分代码中，还会进一步获得 CPU 处理时间的提升，这主要是因为使用 PER 模式时，需要处理的数据量减少了。

So PER seems to produce good gains in both bandwidth and CPU cycles, even for "old" protocols. Where a specification tries to introduce bounds on integers and lengths, where they are sensible for the application, the gains can be much greater. Also protocols that have a lot of boolean "flags" benefit heavily. Figure III-3 shows a (slightly artificial!) SEQUENCE type for which the BER encoding is 19 octets and the PER encoding a single octet! 因此，PER 在带宽和 CPU 周期方面都能带来显著的改善，即使对于“老旧”的协议来说也是如此。当规范对整数和长度施加了限制时，这种改善会更加明显。那些包含大量布尔“标志”的协议也能从中受益。图 III-3 展示了一个（稍微有些人为设计的！）序列类型，其 BER 编码需要 19 个八位元，而 PER 编码则只需要一个八位元即可完成编码任务。

There is a view in the implementor community that use of PER requires the use of a tool to analyze the type definition, determine what constraints affect the encoding (and follow possibly long chains of parameterization of these constraints if necessary), in order to generate correct code for use in an instance of communication to encode\\decode values. 在实现社区中，有一种观点认为，使用 PER 需要借助某种工具来分析类型定义，确定哪些约束会影响编码过程（必要时还需要遵循这些约束所涉及的复杂参数化过程），这样才能生成适用于通信实例的正确编码/解码代码。

There is no doubt that it is easier to make mistakes in PER encoding/decoding by hand than with BER. The PER specification is more complex, and is probably less easy to understand. (If you want my honest opinion, it is actually less well-written than the BER specification! Mea Culpa!) 毫无疑问，手动进行 PER 编码/解码时出错的可能性要比使用 BER 方法时要小得多。PER 规范更为复杂，而且可能也更难理解。（说实话，我的看法是，PER 规范的编写质量实际上比 BER 规范还要差！真是我的过错啊！）

All these points increase the importance of using a well-debugged tool to generate encodings rather than trying to do it by hand. But hand-encodings of PER do exist, and are perfectly possible - but be prepared to put a wet-towel over your head and drink lot's of coffee! And importantly to test against encodings/decodings produced using a tool. These points also apply to hand-encoding of BER, but to a much lesser extent. 所有这些因素都凸显了使用经过充分调试的工具来生成编码的重要性，而不是试图手动完成这项工作。不过，手动生成 PER 的编码是完全可行的——不过请做好心理准备，可能需要花费大量时间和精力来完成这项工作。此外，在测试时，还需要与工具生成的编码/解码结果进行比对。这些原则同样适用于 BER 的手动编码，不过适用范围要小一些。

## 10 Distinguished and Canonical Encoding Rules 10 条著名的规范编码规则

We have observed earlier that encoding rules in which there are no options for the encoder are a good thing. 我们之前已经注意到，对于那些没有编码选项的情况，采用特定的编码规则是一种很好的做法。

Encodings produced by such encoding rules are usually called "distinguished" or "canonical" encodings. At this level (no capitals!) the two terms are synonymous! 由这些编码规则产生的编码通常被称为“标准”或“规范”编码。在这个层次上（不使用大写字母！），这两个术语是同义的！

<table><tbody><tr><td data-imt-p="1">Your job is to produce Standards. If you can't agree, make it optional, or better still another Standard. After all, if one Standard is good, many Standards must be better! 你的任务就是制定标准。如果无法达成一致意见，那就将其设为可选项吧，或者干脆再制定一个标准。毕竟，如果一个标准足够好，那么更多的标准自然也会更好！</td></tr></tbody></table>

However, if options are introduced (such as the indefinite and definite length encodings in BER - see the next chapter) because you cannot agree, how do you agree on encoding rules with all options removed? The answer is two Standards! The Basic Encoding Rules come in three variants: 不过，如果因为某些原因而不愿意采用某些选项（比如 BER 中的不定长和定长编码方式——请参见下一章），那么在没有这些选项的情况下，该如何就编码规则达成一致呢？答案是制定两个标准！基本编码规则有三种变体：

• BER - which allows options for the encoder. • BER——它为编码器提供了多种选择。

• DER (Distinguished Encoding Rules) - which resolves all options in a particular direction. • DER（杰出编码规则）——能够解决某一方向上的所有选项问题。

• CER (Canonical Encoding Rules) - which resolves all options in the other direction! • CER（规范编码规则）——它通过另一种方式解决了所有问题！

It is arguably the case that CER is technically superior, but there is no doubt that DER has become the de facto distinguished/canonical encoding for BER. 可以说，从技术角度来看，CER 确实更优越一些。不过，毫无疑问，DER 已经成为了 BER 标准编码方式中的主流选择。

When we come to PER, the term "distinguished" is not used, but there is defined a BASIC-PER and a CANONICAL-PER with both aligned and unaligned versions as described ealier. 在 PER 这个术语中，并没有使用“杰出”这样的形容词。不过，定义了两种类型：BASIC-PER 和 CANONICAL-PER，并且这两种类型都有对齐版本和未对齐版本，如前面所述。

We mentioned earlier the problem with encodings of the "SET OF xyz" type. (There are also problems with the encoding of GraphicString and GeneralString that are discussed in the later chapters). In a formal sense, the order of the series of "xyz" encodings that are being sent has no significance at the abstract level (it is a SET, not a SEQUENCE), so the order of encodings is clearly a senders option. To determine a single "canonical" encoding for the values of this type requires that the series of "xyz" encodings be SORTED (based on the binary value of each of these encodings) into some defined order. This can put a very significant load on CPU cycles, and also on "disk-churning", and is not something to be lightly entered into! 我们之前提到了“xyz 的集合”这种类型的编码存在的问题。（在后面的章节中，还会讨论 GraphicString 和 GeneralString 的编码问题。）从形式上讲，所发送的“xyz”编码序列的顺序在抽象层面上并没有意义（它只是一个集合，而不是一个序列）。因此，编码的顺序显然是由发送方决定的。为了为这种类型的值确定一个“标准”编码，就需要根据每个编码的二进制值对这些“xyz”编码序列进行排序。这会给 CPU 的运算时间带来很大的负担，也会增加磁盘操作的负担。因此，这不是一个可以轻易处理的问题！

So "normal PER" is not strictly-speaking canonical if a specification contains uses of "SET OF" (although there are those that would argue that we get into "how many angels can sit on the end of a pin" issues here). 所以，严格来说，如果规范中使用了“SET OF”这个术语，那么“正常的 PER”就不算是标准的表达方式了（不过也有人认为，在这种情况下，我们其实是在讨论“有多少天使能够坐在针尖上”这样的问题）。

"Canonical PER" specifies sorting of the "xyz" encodings to produce a truly one-to-one mapping of an (unordered) set of values into bitstrings, each bitstring representing one possible set of (unordered) values of the type "xyz". “规范 PER”用于排序“xyz”编码，以实现一种真正的单对一映射关系。即把一组无序的值集转化为位串，每个位串代表一种可能的“xyz”类型的值集。

Author's opinion: I know of no applications where this degree of formality or precision matters. CANONICAL-PER is basically not a good idea, but neither is the use of "SET OF" in specifications! Try to avoid both. (Others may not agree!) 作者的观点：据我所知，没有哪种应用场景需要如此程度的正式性或精确性。使用“CANONICAL-PER”基本上不是一个好的做法，而使用“SET OF”来描述规格也是如此！尽量避免这两种用法。（不过，其他人可能不同意这种观点！）

## 11 Conclusion 11 结论

This chapter has provided an introduction to the ASN.1 Basic Encoding Rules and the ASN.1 Packed Encoding Rules, showing their approach to encodings and their relative advantages and disadvantages. 这一章节介绍了 ASN.1 基本编码规则与打包编码规则，阐述了这两种编码方式各自的优缺点。

It has also discussed issues of extensibility or "future-proofing", and mentioned canonical/distinguished encoding rules. 会议还讨论了可扩展性问题或“未来兼容性”问题，并提到了规范化/专门的编码规则。

The chapter has formed a basic introduction to the detailed, factual (and dry!) description of BER and of PER in the next two chapters. 这一章节对下一两章中将要详细描述的 BER 和 PER 的基本情况进行了简要介绍。不过，这些描述都是基于事实的、较为枯燥的内容。

Readers may also have heard of ASN.1 Encoding Rules with names like "Minimum Bit Encoding Rules" (MBER), "Lightweight Encoding Rules" (LWER), "Clear text encoding rules", "BACNet Encoding Rules", "Session Layer Encoding Rules" and perhaps others. These represented attempts (sometimes outside the standards community, sometimes within it) to develop other Encoding Rules for ASN.1 that might be superior to both BER and PER in some circumstances (or which were partial early attempts to move towards PER). None of these is regarded as important today for general use with ASN.1, but these are discussed a little further in the fourth (short) chapter of this section. 读者们或许也听说过诸如“最小位编码规则”（MBER）、“轻量级编码规则”（LWER）、“明文编码规则”、“BACNet 编码规则”、“会话层编码规则”等名称的 ASN 编码规则。这些规则试图开发出一些优于 BER 和 PER 的 ASN 编码规则（或者至少是向 PER 方向发展的初步尝试）。不过，如今这些规则已不再被视作为用于 ASN1 编码的重要规则了。不过，在本节的第四章中，我们将进一步探讨这些规则。

# Chapter 2 The Basic Encoding Rules 第二章 基本编码规则

## (Or: Encodings for the 80s - simple, robust, but inefficient!) （或者：80 年代的编码方式——简单、可靠，但效率较低！）

Summary: This chapter provides details of the Basic Encoding Rules. It describes: 摘要：本章详细介绍了基本编码规则的相关内容。具体内容包括：

• The form of the T part of a TLV encoding (the identifier octets), including the primitive/constructed bit. • TLV 编码中 T 部分的格式（标识符的八位组），包括原始/构造位。

The short, definite, and indefinite forms of encoding for the L part of the TLV (the length octets). 用于 TLV 中 L 部分的编码，包括简短的、明确的以及不明确的编码形式（即长度对应的八位组）。

• The V part of the TLV encoding (the contents octets) for each of the primitive types, taken roughly in order of increasing complexity. • TLV 编码中的 V 部分，即每种基本类型的内容字节数，按照复杂度递增的顺序排列。

• The encoding of the constructed types (such as SET and SEQUENCE) • 那些被构建出来的类型（如 SET 和 SEQUENCE 等）的编码方式

The encoding of remaining types, such as the character string and time types and types that represent "holes" of various sorts. 其余类型的编码，比如字符串类型、时间类型，以及表示各种“空洞”的类型。

## 1 Introduction 1 引言

The TLV principles underlying BER encodings have been extensively introduced in earlier chapters, and the reader should have little difficulty in going to the actual Standard/Recommendation for authoritative details. 在之前的章节中已经详细介绍了 BER 编码所基于的 TLV 原则。读者们应该能够轻松找到相关标准/建议的权威资料，以获取更多详细信息。

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/54379e17-c034-430b-894c-f77661f731e5/e0dd100192e597fa60c073bdfbd69bc36fac8b1bc5977b80a130cadf056e40ef.jpg)

For completeness, however, this chapter provides examples of all the encodings, and gives some further explanation in a few cases. 不过，为了完整性，这一章节还是提供了所有编码方式的示例，并在一些情况下给出了进一步的说明。

## 2 General issues 2. 一般问题

## 2.1 Notation for bit numbers and diagrams 2.1 位数的表示方式及图表形式

One of the problems with encoding specifications in the late 1970s was that the bits of an octet were sometimes numbered from left to right in diagrams, sometimes the other way, and sometimes the most significant bit was shown at the right, and sometimes at the left. The order of octet transmission from diagrams could also be right to left in some specifications and left to right in others. Naturally there was often confusion! 在 1970 年代末，编码规范存在的问题之一是：在图表中，一个八位组的各个位有时被从左到右编号，有时则相反；有时最重要的位被标在右边，有时则在左边。在某些规范中，八位组数据的传输顺序可能是从右到左，而在另一些规范中则可能是从左到右。显然，这种情况常常会导致混淆！

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/54379e17-c034-430b-894c-f77661f731e5/24a1406f6817a65a44e83d3c35a86e4935de902fbbb344ed82659f4e63a90d7b.jpg)

In the case of ASN.1 (and this book), we show the first transmitted octet to the left (or above) later transmitted octets, and we show each octet with the most significant bit on the left, with bit numbers running from 8 (most significant) to 1 (least significant) as shown in Figure III-4. 在 ASN.1 的情况下（以及本书中），我们会将第一个传输的八位组显示在最左侧（或上方），然后依次显示后续每个八位组。每个八位组的显示方式是将最高有效位放在最左侧，八位组的编号从 8（最高有效位）开始，到 1（最低有效位）结束，如图 III-4 所示。

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/54379e17-c034-430b-894c-f77661f731e5/fa9d6e223841698f52d2ead9321da83934a74e341bf821744cb77903a064555a.jpg)

Whether within an octet the most or least significant bit is transmitted first (or the bits are transmitted in parallel) is not prescribed in ASN.1. This is determined by the carrier protocols. On a serial line, most significant first is the most common. It is the terms "most significant bit" and "least significant bit" that link the ASN.1 specifications to the lower layer carrier specifications for the determination of the order of bits on the line. 在 ASN.1 标准中并没有规定在八个字节中，哪个位应该先传输，或者各个位是否应并行传输。这一决定由上层协议来决定。在串行线路中，通常是以最高有效位为优先传输的。正是“最高有效位”和“最低有效位”这两个术语，使得 ASN.1 规范与下层载波规范能够相互衔接，从而确定线路上各位的传输顺序。

The order of octets on the line is entirely determined by ASN.1. When encoding a multi-octet integer value, ASN.1 specifies that the most significant octet of the value is transmitted first, and hence is shown in diagrams in the standard (and in this book) as the left-most octet of the value (see the encoding of the integer type later in this chapter). 行中八位组的顺序完全由 ASN.1 协议决定。在编码多八位组整数值时，ASN.1 规定首先传输该数值的最高位八位组，因此在标准规范中（以及本书中），这个八位组被标记为数值的最左侧位组（请参考本章后面的整数类型编码部分）。

## 2.2 The identifier octets 2.2 标识符的八位组

Every ASN.1 type has a tag of one of four classes, with a number for the tag, as discussed earlier. In the simplest case these values are encoded in a single octet as shown in Figure III-5. 每个 ASN.1 类型都有一个属于四个类别之一的标签，该标签由一个数字组成，如前所述。在最简单的情况下，这些数值被编码为一个八位元，如图 III-5 所示。

<table><tbody><tr><td data-imt-p="1">First the T part, encoding the tag value. 首先是对 T 部分的处理，即对标签值的编码。</td></tr></tbody></table>

We see that the first two bits encode the class as follows: 我们看到，前两个位元分别用于编码类别信息，具体编码方式如下：

<table><tbody><tr><td data-imt-p="1">Class 班级</td><td data-imt-p="1">Bit 8 第 8 位</td><td data-imt-p="1">Bit 7 第 7 位</td></tr><tr><td data-imt-p="1">Universal 通用性</td><td>0</td><td>0</td></tr><tr><td data-imt-p="1">Application 应用程序</td><td>0</td><td>1</td></tr><tr><td data-imt-p="1">Context-specific 特定情境下的</td><td>1</td><td>0</td></tr><tr><td data-imt-p="1">Private 私人</td><td>1</td><td>1</td></tr></tbody></table>

<table><tbody><tr><td data-imt-p="1">Class 班级</td><td data-imt-p="1" data-imt_insert_failed_reason="same_text">P/C</td><td data-imt-p="1">Number 数字</td></tr></tbody></table>

Figure III-5: Encoding of the identifier octet (number less than 31) 图 III-5：标识符八位组的编码（数值小于 31）

The next bit (bit six) is called the primitive/constructed (P/C) bit, and we will return to that in a moment. 下一个位（第六位）被称为原始/构造位（P/C 位），我们稍后会再次讨论这个问题。

The last five bits (bits 5 to 1) encode the number of the tag. Clearly this will only cope with numbers that are less than 32. In fact, the value 31 is used as an escape marker, so only tag numbers up to 30 encode in a single octet. 最后五位二进制位（从位 5 到位 1）用于编码标签的编号。显然，这一编码方式只能表示小于 32 的数字。实际上，数值 31 被用作一个转义标记，因此只有直到 30 的标签编号才能用单个八位元来表示。

For larger tag values, the first octet has all ones in bits 5 to 1, and the tag value is then encoded in as many following octets as are needed, using only the least significant seven bits of each octet, and using the minimum number of octets for the encoding. The most significant bit (the "more" bit) is set to 1 in the first following octet, and to zero in the last. This is illustrated in Figure III-6. 对于较大的标签值，第一个八位组中的第 5 位到第 1 位都是 1。之后，需要多少位就可以用多少位来编码标签值，只需使用每个八位组的最低 7 位，并尽量使用最少的位数进行编码。在接下来的第一个八位组中，最高位（“更多”位）被设置为 1，而在最后一个八位组中则设置为 0。如图 III-6 所示。

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/54379e17-c034-430b-894c-f77661f731e5/b3106c91de051193a4a462381e280177a69b450a48f03688488bfd7a910b644f.jpg)

Figure III-6: Encoding of the identifier octets (numbers greater than 30) 图 III-6：标识符八位组（数值大于 30 的位）的编码方式

Thus tag numbers between 31 and 127 (inclusive) will produce two identifier octets, tag numbers between 128 and 16383 will produce three identifier octets. (Most ASN.1 specifications keep tag numbers below 128, so either 1 identifier octet - most common - or two identifier octets is what you will normally see, but I have seen a tag number of 999!. 因此，标签编号在 31 到 127 之间（包括两端）会生成两个标识符位元组；而标签编号在 128 到 16383 之间则会生成三个标识符位元组。大多数 ASN.1 规范将标签编号限制在 128 以下，所以通常情况下你会看到的是一个标识符位元组——也就是最常见的做法。不过，我也见过一些标签编号高达 999 的案例。

What about the primitive/constructed bit? This is required to be set to 1 (constructed) if the V part of the encoding is itself a series of TLV encodings, and is required to be set to 0 (primitive) otherwise. Thus for the encoding of an integer type or boolean type (provided any tagging was implicit), it is always set to 0. For the encoding of a SET or SET-OF etc, it is always set to 1. In these cases it is clearly redundant, provided the decoder has the type definition available. 那么“原始”与“构造”这部分呢？如果编码中的 V 部分本身是由多个 TLV 编码构成的序列，那么这部分应该被设置为 1（构造的）；否则，应该设置为 0（原始的）。因此，对于整数类型或布尔类型的数据编码（只要标签是隐式的），这部分总是被设置为 0。而对于 SET 或 SET-OF 等类型的编码，这部分则总是被设置为 1。在这些情况下，只要解码器能够获取类型定义，那么设置这部分为 0 显然是没有必要的。

But having this bit present permits a style of decoding architecture in which the incoming octetstream is first parsed into a tree-structure of TLV encodings (with no knowledge of the type definition), so that the leaves of the tree are all primitive encodings. The tree is then passed to code that does know about the type definition, for further processing. 不过，如果具备这一特性，就可以采用一种解码架构。在这种架构中，传入的八位元数据流首先会被解析成一种树形结构，其中各个节点都代表某种基本编码格式。然后，这个树形结构会被传递给那些了解类型定义的处理器，以便进行进一步的处理。

There is, however, a rather more important role for this bit. As we will see later, when transmitting a very long octet string value (and the same applies to bit string and character string values), ASN.1 permits the encoder to either transmit as the entire V part the octets of the octet string value (preceded by a length count), or to fragment the octet string into a series of fragments which are each turned into TLV encodings which then go into the V part of the main outer-level encoding of the octet string value. Clearly a decoder needs to know which option was taken, and the primitive/constructed bit tells it precisely that. 不过，这一位确实扮演着更为重要的角色。正如我们稍后会看到的，在传输非常长的八位组字符串值时（对于位字符串和字符字符串值也是如此），ASN.1 允许编码器将八位组字符串值的各个八位组作为一个完整的 V 部分进行传输（并附带长度信息），或者将八位组字符串拆分成多个片段，每个片段都进行 TLV 编码后作为 V 部分的一部分被包含在主外部编码中。显然，解码器需要知道采用了哪种方式，而原始/构造位就能准确传达这一信息。

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/54379e17-c034-430b-894c-f77661f731e5/2fc52f8237440683c5c30a222660246fefcc0e3e6d23dc6f3176e708bf9b65aa.jpg)

Why is fragmentation in this way useful? This will become clearer in the next Clause, when we consider the form of the "L" encoding, but the problem is roughly as follows. 为什么这种碎片化结构是有用的呢？这一点在下一节中将会更清楚地体现出来，当我们讨论“L”形编码的形式时就会明白。不过，问题的核心大致可以概括为以下几点。

If our V part is primitive, clearly all possible octet values can appear within it, and the only mechanism that ASN.1 provides for determining its length is to have an explicit count of octets in the "L" part. For extremely long octet values, this could mean a lot of disk churning to determine the exact length (and transmit it) before any of the actual octets can be sent. If however, the V part is made up of a series of TLVs, we can find ways of terminating that series of TLVs without an up-front count, so we can transmit octets from the value as they become available, without having to count them all first. 如果 V 部分是一个原始的数据结构，那么显然所有可能的八位元数值都可能出现在其中。而 ASN.1 提供的唯一确定其长度的方法，就是明确指定“L”部分中的八位元数量。对于非常长的八位元数值来说，这意味着需要花费大量时间来计算确切的长度（并在发送实际八位元数值之前先发送出该长度）。不过，如果 V 部分由一系列 TLV 组成，那么我们可以找到方法在不进行预先计数的情况下终止这一系列 TLV 的传输，这样就能在八位元数值逐个可用时将其发送出去，而无需先计算出总数。

## 2.3 The length octets 2.3 长度字节位

There are three forms of length encoding used in BER, called the short form, the long form, and the indefinite form. It is not always possible to use all three forms, but where it is, it is an encoder's option which to use. This is one of the main sources of optionality in BER, and the main area that canonical/distinguished encoding rules have to address. 在 BER 中，有三种长度编码方式：短形式、长形式和不定形式。虽然并不总是能够同时使用这三种方式，但在必要时，编码器可以选择使用其中一种。这是 BER 中可变性的主要来源之一，也是规范/特殊编码规则需要处理的主要领域。

## 2.3.1 The short form 2.3.1 缩写形式

Now the L part - three forms are available in general, sometimes only two, and occasionally only one. The encoder chooses the one to use. 现在，L 部分有三种形式可供选择：通常情况下会有三种形式，有时只有两种，偶尔甚至只有一种。编码器会自行决定使用哪种形式。

This is illustrated in Figure III-7. 如图 III-7 所示。

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/54379e17-c034-430b-894c-f77661f731e5/f4cfb5d8662b3b5660db71ab31e0bc2c4a9f7521a32cf836a3aead5529acb77c.jpg)

The short form can be used if the number of octets in the V part is less than or equal to 127, and can be used whether the V part is primitive or constructed. This form is identified by encoding bit 8 as zero, with the length count in bits 7 to 1 (as usual, with bit 7 the most significant bit of the length). 如果 V 部分的八位组数量小于或等于 127，就可以使用这种简式表示法。无论 V 部分是原始格式还是组合格式，都可以使用这种形式。这种形式的识别方式是将第 8 位编码为 0，而长度信息则存储在第 7 位到第 1 位上（按照常规，第 7 位代表长度的最高位）。

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/54379e17-c034-430b-894c-f77661f731e5/f0602d0c4f4636f3b6c16069c1444375f65a49db4cd78553bf4256c6c4cd1e32.jpg)

## 2.3.2 The long form 2.3.2 长形式

If bit 8 of the first length octet is set to 1, then we have the long form of length. This form can be used for all types of V part, no matter how long or short, no matter whether primitive or constructed. In this long form, the first octet encodes in its remaining seven bits a value N which is the length of a series of octets that themselves encode the length of the V part. This is shown in Figure III-8. 如果第一个长度字节的第 8 位被设置为 1，那么我们就得到了完整的长度表示形式。这种表示形式适用于所有类型的 V 部分，无论其长度长短，也不管是原始类型还是复合类型。在这种完整的形式中，第一个字节的其余 7 位则用于表示一个数值 N，这个数值代表了由多个字节组成的序列的长度。如图 III-8 所示。

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/54379e17-c034-430b-894c-f77661f731e5/4eee760be8638cdd607c45a3190970899dae892c9d90c2ff59c79c1b3b417064.jpg)

There is no requirement that the minimum number of octets be used to encode the actual length, so all the length encodings shown in Figure III-9 are permitted if the actual length of the V part is 5. 并没有要求必须使用最小数量的八位元来编码实际长度。因此，如果 V 部分的实际长度为 5，那么图 III-9 中所示的所有长度编码都是可行的。

This was actually introduced into ASN.1 in the early 1980s just before the first specification was finalised (early drafts required length encodings to be as small as possible). It was introduced because there were a number of implementors that wanted N to have a fixed value (typically 2), then the N (2) octets that would hold the actual length value, then the V part. There are probably still BER implementations around today that always have three length octets (using the long form encoding), even where one octet (using the short form encoding) would do. 这一规范实际上是在 20 世纪 80 年代初被引入到 ASN.1 标准中的。当时，第一个规范草案尚未最终确定（早期的草案要求长度编码的位数要尽可能少）。之所以引入这一规范，是因为有一些实现方希望 N 具有固定的值（通常设为 2），然后由 N（2 个八位组）来表示实际的长度值，再接着是 V 部分。今天，可能仍然有一些 BER 实现始终使用三个八位组来表示长度，即使使用一个八位组就能满足需求的情况也是如此。

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/54379e17-c034-430b-894c-f77661f731e5/40c7ac8b33e789580fc9c48d0e8b14b6097b22af0b42ee979144020c7895fec9.jpg)

Figure III-9: Options for encoding a length of 5 图 III-9：编码长度为 5 的数据的各种方法

There is a restriction on the first length octet in the long form. N is not allowed to have the value 127. This is "reserved for future extensions", but such extensions are now highly unlikely. If you consider how long the V part can be when N has the maximum value of 126, and how large an integer value such a V part can hold, you will find that the number is greater than the number of stars in our galaxy. It was also calculated that if you transmit down a line running at one tera-bit per second the longest possible V part, it would take one hundred million years to transmit all the octets! So there is no practical limit imposed by BER on the size of the V part, or on the value of integers. 在长形式中，第一个长度八位组有一个限制条件：N 的值不得为 127。这个限制“为未来的扩展预留了空间”，但实际上这样的扩展现在几乎不太可能出现。如果考虑到当 N 的值为 126 时，V 部分可以包含多少数据，以及这样的 V 部分所能容纳的整数值有多大，你会发现这个数字远远超过我们银河系中恒星的数量。此外，据计算，如果以每秒一太字节的速度传输数据，要传输完所有八位组的话，需要一亿年时间！因此，BER 对 V 部分的大小或整数的取值并没有实际的限制。

## 2.3.3 The indefinite form 2.3.3 不定形式

The indefinite form of length can only be used (but does not have to be) if the V part is constructed, that is to say, consists of a series of TLVs. (The length octets of each of these TLVs in this contained series can independently be chosen as short, definite, or indefinite where such choices are available - the form used at the outer level does not affect the inner encoding.) “不定长度”形式只能用于那些由多个传输层标签（TLV）构成的条目中。（这些 TLV 中的长度八位组可以独立地选择为固定、明确或不确定的形式——在外部层次中使用的格式并不影响内部的编码方式。）

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/54379e17-c034-430b-894c-f77661f731e5/e2ad1a0b0bca9d08fbbe1d79711756dec8077610f64880925012a2aef3875d0a.jpg)

In the indefinite form of length the first bit of the first octet is set to 1, as for the long form, but the value N is set to zero. Clearly a value of zero for N would not be useful in the long form, so this serves as a flag that the indefinite form is in use. Following this single octet, we get the series of TLVs forming the V part, followed by a special delimiter that is a pair of zero octets. 在无限长度的形式中，第一个八位组的第一个位被设置为 1；而在长格式中，这个位则被设置为 0。显然，在长格式中，N 的值为 0 是没有意义的，因此这个位起到了标识当前使用无限长度格式的作用。在第一个八位组之后，是构成 V 部分的多个 TLV 字段，接着是一个特殊的分隔符，即一对零八位组。

This is shown in Figure III-10. 如图 III-10 所示。

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/54379e17-c034-430b-894c-f77661f731e5/7bab9cc570e56ea51cfb1a7cebca15785b4396923be116508d4ad85a877712ef.jpg)

Figure III-10: An indefinite length encoding 图 III-10：不定长度编码

How does this work? The most important thing to note is that a decoder is processing the series of TLVs, and when it hits the pair of zero octets it will interpret them as the start of another TLV. So let us do just that. The zero T looks like a primitive encoding (bit six is zero) with a tag of UNIVERSAL class ZERO, and a definite form length encoding of zero length (zero octets in the V part). 这是如何工作的呢？最重要的是，解码器正在处理一系列 TLV 数据。当遇到一对零八位组时，它会将其视为另一个 TLV 数据的开始。那么，我们就按照这种方式来处理吧。这个零八位组看起来像是一种原始编码（第六位为 0），其标签为“UNIVERSAL 类零”，而定义形式长度则被设置为零长度（V 部分包含零个八位组）。

If you now refer back to the assignment of UNIVERSAL class tags given in Figure II-7, you will see that UNIVERSAL class zero is "Reserved for use by Encoding Rules" (and remember that users are not allowed to assign UNIVERSAL class tags). So a pair of zero octets can never appear as a TLV in any real encoding, and this "special" TLV can safely be defined by BER as the delimiter for the series of TLVs in the V part of an indefinite form encoding. 如果你现在回想一下图 II-7 中给出的通用类标签的分配情况，你会发现通用类零号是“预留用于编码规则使用的”（记住，用户不允许分配通用类标签）。因此，一对零八位组永远不可能出现在任何实际编码中作为 TLV 元素。而这一“特殊”的 TLV 可以被 BER 安全地定义为不定形式编码中 V 部分内一系列 TLV 元素的分隔符。

We have said earlier that, within an indefinite form TLV we may have inner TLVs that themselves are constructed and have an indefinite form of length. There is no confusion: a pair of zero octets (when a TLV is expected) terminates the innermost "open" indefinite form. 我们已经提到过，在一个不定长的 TLV 中，可能还存在一些内部 TLV。这些内部 TLV 也是由多个元素构成的，并且它们的长度也是不定长的。需要注意的是：当遇到 TLV 时，一对零八位组会作为最内层的“开放”不定长形式的终结。

## 2.3.4 Discussion of length variants 2.3.4 长度变体的讨论

Why do we need so many different variants of length? Clearly they all have some advantages and disadvantages. The short form is the briefest when it can be used, the long form is the only one that can handle very large primitive encodings, and seems to many to be intuitively simpler than the indefinite form. The indefinite is the only one which allows very large OCTET STRING values or SEQUENCE OF values to be transmitted without counting the number of octets in the value before starting. 为什么我们需要这么多不同形式的长度表示方式呢？显然，每种形式都有其优缺点。最短的形式在需要使用时最为简洁；而长形式则能够处理非常庞大的原始编码，而且似乎比不定形式更直观易懂。不定形式是唯一一种可以传输非常大的 OCTET STRING 值或 SEQUENCE OF 值的形式，无需在开始传输之前计算这些值的字节数。

The disadvantage of having three options is the extra implementation complexity in decoders, and the presence of encoding options creating side-channels and extra debugging effort. If we want to remove these options, then we have to either say "use indefinite length form whenever possible" (and make statements about the size of fragment to use when fragmenting an octet string), or to say "use short form where possible, otherwise use long form with the minimum value of N needed for the count". Both of these approaches are standardised! The distinguished/canonical encoding rules that take the former approach are called the Canonical Encoding Rules (CER), and those that take the latter approach are called the Distinguished Encoding Rules (DER). Applications with requirements for canonical/distinguished encoding rules will mandate use of one of these in the application specification. 采用三种编码方式的缺点在于，解码过程会更加复杂；此外，多种编码方式还会产生额外的侧流，从而增加调试工作的复杂性。如果我们想要取消这些选项，那么我们就必须选择一种方式：要么“尽可能使用不定长度的形式”，同时还需要说明在分割八位组时应该使用的片段大小；要么“尽可能使用短形式，否则就使用长形式，但需确保使用的 N 值尽可能小”。这两种方法都是标准化的！采用第一种方法的规范编码规则被称为“标准编码规则”（CER），而采用第二种方法的则被称为“特色编码规则”（DER）。那些需要采用标准或特色编码规则的应用程序，会在应用规范中明确要求使用其中一种编码方式。

## 3 Encodings of the V part of the main types 主类型中 V 部分的 3 种编码方式

In the examples for this clause we use the ASN.1 value notation to specify a value of a type, and then show the complete encoding of that value using hexadecimal notation for the value of each octet. 在本节的示例中，我们使用 ASN.1 值表示法来指定某种类型的值。同时，我们会以十六进制表示法来展示每个八位组值的完整编码形式。

The primary focus here is to illustrate the encoding of the V part for each type, but it must be remembered that there will be other permissible length encodings in addition to the one illustrated (as discussed earlier), and that if implicit tagging were to be applied, the T part would differ. 这里的主要目的是为了说明每种类型中 V 部分的编码方式。不过，需要注意的是，除了所展示的编码方式之外，还可能存在其他允许的长度编码方式（如前所述）。如果采用隐式标签标记方式，那么 T 部分的编码方式也会有所不同。

<table><tbody><tr><td data-imt-p="1">Encoding the V part is specific to each type. In many cases it is obvious, but the majority of types throw up problems which produce a little complexity in the encoding. 对 V 部分的编码是特定于每种类型的。在许多情况下，这种编码是显而易见的，但大多数类型都会带来一些复杂性的问题，从而增加了编码的难度。</td></tr></tbody></table>

The encoding of each of the following types is always primitive unless stated otherwise. The types are taken roughly in ascending order of complexity! 以下每种类型的编码方式通常都是原始的，除非另有说明。这些类型大致按照复杂度的递增顺序排列！

## 3.1 Encoding a NULL value 3.1 对空值进行编码

Utterly simple! 非常简单！

The value of 数值为

 

$$
\text { null NULL }: := \text { NULL }
$$

 

(the only value of the NULL type) is encoded as （NULL 类型的唯一值）被编码为

<table><tbody><tr><td></td><td>T</td><td>L</td><td>V</td></tr><tr><td data-imt-p="1">null: 无：</td><td>05</td><td>00</td><td data-imt-p="1">empty 空的</td></tr></tbody></table>

Note that whilst we have described our structure as TLV, it is (as in this case) possible for there to be zero octets in the V part if the length is zero. This can arise in cases other than NULL. So for example, a SEQUENCE OF value with an iteration count of zero would encode with an L of zero. Similarly a SEQUENCE, all of whose elements were optional, and which in an instance of communication were all missing, would again encode with an L of zero. 请注意，虽然我们将我们的结构描述为 TLV 格式，但实际上如果 V 部分的长度为 0，那么可能不会有任何八位元被使用。这种情况可能出现在其他情况下，而不仅仅是 NULL 情况下。例如，一个迭代次数为零的 SEQUENCE-of-value 序列，其编码方式就是使用一个零值的 L。同样，如果一个 SEQUENCE 中的所有元素都是可选的，并且在通信过程中这些元素实际上并未被使用，那么这个 SEQUENCE 的编码方式同样也会是零值的 L。

## 3.2 Encoding a BOOLEAN value 3.2 对布尔值进行编码

The values of 这些数值/内容

<table><tbody><tr><td data-imt-p="1">boolean1 布尔值 1</td><td data-imt-p="1" data-imt_insert_failed_reason="same_text">BOOLEAN ::= TRUE</td></tr><tr><td data-imt-p="1">boolean2 布尔值 2</td><td data-imt-p="1" data-imt_insert_failed_reason="same_text">BOOLEAN ::= FALSE</td></tr></tbody></table>

<table><tbody><tr><td data-imt-p="1">Still pretty obvious, but we now have encoders options! 虽然很明显，但现在我们有了编码器选项了！</td></tr></tbody></table>

are encoded as 被编码为

<table><tbody><tr><td></td><td>T</td><td>L</td><td>V</td></tr><tr><td data-imt-p="1">boolean1: 布尔值 1：</td><td>01</td><td>01</td><td>FF</td></tr><tr><td data-imt-p="1">boolean2: 布尔值 2：</td><td>01</td><td>01</td><td>00</td></tr></tbody></table>

For the value TRUE, an encoding of hex FF is shown. This is the only permissible encoding in DER and CER, but in BER any non-zero value for the V part is permitted. 当值为 TRUE 时，会显示十六进制编码 FF。这是 DER 和 CER 中唯一允许的编码方式；而在 BER 中，V 部分的任何非零值都是被允许的。

## 3.3 Encoding an INTEGER value 3.3 对整数值进行编码

A two's complement encoding of the integer values into the smallest possible V part is specified. When two's complement is used "smallest possible" means that the first (most significant) nine bits of the V part cannot be all zeros or all ones, but there will be values that will encode with the first eight bits all zeros or ones. 该整数值采用了二进制补码编码方式来表示，以使得 V 部分的位数尽可能少。当使用二进制补码编码时，“尽可能少”的含义是，V 部分的前九个二进制位不能全部为 0 或全部为 1，而是会有一些数值使得前八个二进制位全部为 0 或全部为 1。

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/54379e17-c034-430b-894c-f77661f731e5/33b375164fb43da3eec7e3613c8bdf06e9cb0c08d5a209618aac4a49444a43e1.jpg)

Note that it would in theory have been possible to use an L value of zero and no V part to represent the integer value zero, but this is expressly forbidden by BER - there is always at least one octet in the V part. 需要注意的是，理论上可以使用零的 L 值和不存在的 V 部分来表示整数零值。但实际上，BER 明确禁止了这种用法——V 部分中总是至少有一个八位组。

Thus the values of 因此，这些数值为

<table><tbody><tr><td data-imt-p="1">integer1 整数 1</td><td data-imt-p="1">INTEGER ::= 72 整数 ::= 72</td></tr><tr><td data-imt-p="1">integer2 整数 2</td><td data-imt-p="1">INTEGER ::= 127 整数 ::= 127</td></tr><tr><td data-imt-p="1">integer3 整数 3</td><td data-imt-p="1">INTEGER ::= -128 整数 ::= -128</td></tr><tr><td data-imt-p="1">integer4 整数 4</td><td data-imt-p="1">INTEGER ::= 128 整数类型 ::= 128</td></tr></tbody></table>

are encoded as 被编码为

<table><tbody><tr><td></td><td>T</td><td>L</td><td>V</td></tr><tr><td data-imt-p="1">integer1 整数 1</td><td>02</td><td>01</td><td>48</td></tr><tr><td data-imt-p="1">integer2 整数 2</td><td>02</td><td>01</td><td>7F</td></tr><tr><td data-imt-p="1">integer3 整数 3</td><td>02</td><td>01</td><td>80</td></tr><tr><td data-imt-p="1">integer4 整数 4</td><td>02</td><td>02</td><td>0080</td></tr></tbody></table>

If the integer type was defined with a distinguished value list, this does not in any way affect the encoding. 如果整数类型被定义为具有特定的值列表，那么这并不会对编码过程产生任何影响。

## 3.4 Encoding an ENUMERATED value 3.4 对枚举值进行编码

The definition of an enumerated type may include integer values to be used to represent each enumeration during transfer, or (post 1994) may allow those values to be automatically assigned in order from zero. In the latter case all such values will be positive, but in the general case a user is allowed to assign negative values for 枚举类型的定义可能包括用于在传输过程中表示每个枚举值的整数值。或者，自 1994 年后，这些值可以自动从零开始分配。在后一种情况下，所有值都将为正数；但在一般情况下，用户也可以为这些值分配负数值。

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/54379e17-c034-430b-894c-f77661f731e5/d3083e03bbd7a1e050a8ab11ad71d9c94ab0ed6920359aa8aa65fa2b7b781a1e.jpg)

enumerations (nobody ever does). BER takes no account of the (common) case where all associated values are positive: the encoding of an enumerated value is exactly the same as the (two's complement) encoding of the associated integer value (except that the tag value is different of course). 枚举类型（从来没有人会处理这种情况）。BER 算法并没有考虑到一种常见的情况：即所有相关的数值都是正数。在这种情况下，对枚举值的编码方式与对相关整数的二进制补码编码方式完全相同（当然，标签值需要有所不同）。

In practice, this only makes an efficiency difference if there are more than 127 enumerations, which is rare. 实际上，这种情况只有在枚举次数超过 127 次时才会产生效率上的差异，而这种情况非常罕见。

## 3.5 Encoding a REAL value 3.5 对实数进行编码

The encoding of a real value is quite complex. First of all, recall that the type is formally defined as the set of all values that can be expressed base 10, together with the set of all possible values that can be expressed base 2, even if these are the same numerical value. This means that different 对实数进行编码是非常复杂的操作。首先，需要记住的是，类型被正式定义为所有可以用十进制表示的值的集合，以及所有可以用二进制表示的值的集合——即使这些二进制表示的值与十进制表示的值相同。这意味着不同的实数在编码时会有不同的处理方式。

Forget about floating point format standards. What matters is how easily you can encode/decode with real hardware. 先不要考虑浮点数的格式标准了。真正重要的是，你是否能够轻松地使用实际的硬件进行编码和解码操作。

encodings are applied to these two sets of values, and the application may apply different semantics. (There is one exception to this - the value zero has just one encoding, zero octets in the V part.) For base 10 values, the encoding is character-based, for base 2 values, it is binary floating point. 这两种数值集都经过了编码处理，而且应用程序可能会采用不同的编码方式。（不过有一个例外——数值零只有一种编码方式，即 V 部分使用零个八位元。）对于基于 10 的数值，编码方式是字符编码；而对于基于 2 的数值，则采用二进制浮点数的编码方式。

There are also two further values of type REAL - PLUS-INFINITY and MINUS-INFINITY, with their own special encodings. 此外，还有两个更高级别的 REAL 类型的值：PLUS-INFINITY 和 MINUS-INFINITY，它们各自具有独特的编码方式。

Note that it is possible to subtype type REAL to contain only base 10 or base 2 values, effectively giving the application designer control over whether the character-based encoding or the binarybased encoding of values of the type are to be used. 需要注意的是，可以将类型“REAL”进一步细分，以仅包含基于 10 进制或 2 进制的数值。这样实际上就给了应用程序设计者选择权，让他们决定是使用基于字符的编码方式，还是基于二进制的编码方式来表示该类型的数值。

## 3.5.1 Encoding base 10 values 3.5.1 将基于 10 的数值进行编码

If the (non-zero) value is base 10, then the contents octets (the V part) start with one octet whose first two bits are 00 (other values are used for the base 2 values and the special values PLUS-INFINITY and MINUS-INFINITY). Octets after this initial octet are a series of ASCII characters (8 bits 如果这个（非零）数值是以 10 为基数，那么这些八位元的内容（即 V 部分）会以一个八位元开头，该八位元的前两位为 00（对于以 2 为基数的数值，以及其他特殊数值如 PLUS-INFINITY 和 MINUS-INFINITY，则使用其他值）。在第一个八位元之后，接下来的八位元则是由一系列 ASCII 字符组成的（共 8 位）。

A character encoding base 10 is available. (But not much used!) 该字符编码基于十进制系统。（不过其实很少被使用！）

per character) representing digits 0 to 9, space, plus sign, minus sign, comma or full-stop (for "decimal mark"), and capital E and small e (for exponents), in a format defined in the ISO Standard 6093. This standard has a lot of options, and in particular defines "Numerical Representation 1" (NR1), NR2, and NR3. Which of these is used is coded as values 1, 2, or 3 respectively into the bottom six bits of the first contents octet. Even within these representations, there are many options. In particular, arbitrary many leading spaces can be included, plus signs are optional, and so on. 每个字符代表一个数字，这些数字可以是 0 到 9 之间的整数，空格、加号、减号、逗号或句号（用于表示小数点），以及大写的 E 和小写的 e（用于表示指数）。这些字符的表示方式遵循 ISO 标准 6093 的规定。该标准提供了许多选项，特别是定义了“数值表示 1”（NR1）、NR2 和 NR3 三种表示方法。究竟使用哪种表示方法，可以通过第一个内容字节的后六位来指定相应的值，分别表示为 1、2 或 3。即使在这三种表示方法中，也有许多可选的设置。例如，可以包含任意多的前导空格；加号是可选的，等等。

When used with DER and CER (and all versions of PER), options are restricted to NR3, spaces and leading zeros are in general forbidden, the full-stop has to be used for any "decimal mark", and the plus sign is required for positive values. The mantissa is required to be normalised so that there are no digits after the "decimal mark". In each case below, the second column shows the way the same real value would be encoded in DER/CER/PER. 当与 DER 和 CER（以及所有版本的 PER）结合使用时，选项的限制如下：只能使用 NR3 表示法；通常禁止使用空格和前导零；任何“小数点”都需要用全停号表示；对于正数，必须使用加号来表示。尾数必须进行标准化处理，以确保“小数点”之后没有其他数字。在下面的每个例子中，第二列展示了相同实数值在 DER/CER/PER 编码中的表示方式。

We will not attempt here a detailed description of ISO 6093, but give below some examples of the resulting strings. Note that whilst there may be leading spaces, there are never trailing spaces. There may also be leading zeros and trailing zeros. 我们不会在这里对 ISO 6093 标准进行详细的说明，而是提供一些具体的例子。需要注意的是，虽然字符串开头可能会有空格，但结尾永远不会有空格。此外，字符串开头和结尾也可能出现零位。

NR1 encodes only simple whole numbers (no decimal point, no exponent). Here are some examples of NR1 encodings, where # is used to denote the space character: NR1 仅编码简单的整数（没有小数点，也没有指数）。以下是一些 NR1 编码的示例，其中#用来表示空格字符：

<table><tbody><tr><td>4902</td><td data-imt-p="1">4902.E+0 4902. E^0</td></tr><tr><td>#4902</td><td data-imt-p="1">4902.E+0 4902. E^0</td></tr><tr><td>###0004902</td><td data-imt-p="1">4902.E+0 4902. E^0</td></tr><tr><td data-imt-p="1" data-imt_insert_failed_reason="same_text">###+4902</td><td data-imt-p="1">4902.E+0 4902.E^0</td></tr><tr><td>-004902</td><td data-imt-p="1" data-imt_insert_failed_reason="same_text">-4902.E+0</td></tr></tbody></table>

NR2 requires the presence of a "decimal mark" (full-stop or comma as an encoders option). Here are some examples of NR2 encodings: NR2 要求必须有一个“小数点”符号（编码器可以选择使用句号或逗号作为分隔符）。以下是一些 NR2 编码的示例：

<table><tbody><tr><td>4902.00</td><td data-imt-p="1">4902.E+0 4902. E^0</td></tr><tr><td>###4902,00</td><td data-imt-p="1">4902.E+0 4902. E^0</td></tr><tr><td>000.4</td><td>4.E-1</td></tr><tr><td>#.4</td><td>4.E-1</td></tr><tr><td>4.</td><td data-imt-p="1" data-imt_insert_failed_reason="same_text">4.E+0</td></tr></tbody></table>

NR3 extends NR2 by the use of a base 10 exponent represented by a capital E or lower case e. Examples of NR3 are: NR3 通过使用以大写字母 E 或小写字母 e 表示的 10 进制指数来表示 NR2。NR3 的例子包括：

## 3.5.2 Encoding base 2 values 3.5.2 将二进制值进行编码

NOTE — For a full understanding of this material the reader will need some familiarity with the form of computer floating point units - something assembler language programmers of the 1960s were very familiar with, but something today's programmers can usually forget about! You may want to skim this material very quickly, or even totally ignore it. 注意：要完全理解这部分内容，读者需要一些关于计算机浮点运算单位形式的知识——这种知识在 1960 年代的汇编语言程序员中非常常见，但现在的程序员往往已经忘记了！你可以快速浏览这部分内容，或者完全忽略它吧。

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/54379e17-c034-430b-894c-f77661f731e5/c9a47fe5fef77e24f4015a1ed604bd5ff04bc09295cfa833e3811bff3d1ff07a.jpg)

Base 2 values are encoded in a form that is similar to the floating point formats used when a computer system dumps the contents of a floating point unit into main memory. We talk about the mantissa (M), the base (B) and the exponent (E) of the number. 基数 2 的值是以一种类似于计算机系统中将浮点数值输出到主内存时使用的浮点格式来编码的。我们所说的数字中的尾数（M）、基数（B）和指数（E）。

However, in real floating point units, the base may be either 2, 8 or 16 (but is fixed for that hardware). In an ASN.1 encoding, the value of B has to be sent. This is done in the first contents octet. We then need the value of the exponent for this numerical value, and of the mantissa. 不过，在实际的浮点数表示中，基数可以是 2、8 或 16（但这是针对特定硬件而言的）。在 ASN.1 编码中，必须发送 B 的值。这一数值是通过第一个内容字节来表示的。接下来，我们需要该数值的指数部分的值，以及 Mantissa 部分的值。

Let us look at the first contents octet in the case of base 2 values (recall that the first contents octet for base 10 values started 00 and then encoded NR1, NR2, or NR3). This first content octet is illustrated in Figure III-11. 让我们来看看二进制数值的第一个内容八位组。回想一下，十进制数值的第一个内容八位组以 00 开始，之后分别编码为 NR1、NR2 或 NR3。这个第一个内容八位组如图 III-11 所示。

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/54379e17-c034-430b-894c-f77661f731e5/ec66448663891fc77681e68455b96759a571162d7820aea3779c56cd5e78851a.jpg)

Figure III-11: Encoding of the first contents octet of a base 2 real value 图 III-11：二进制实数第一个字节内容的编码方式

The first bit (bit 8, most significant) is set to 1 to identify this as a base 2 value. The next bit (S) is the sign of the number, with the mantissa represented (later) as a positive integer value. The next two bits (B) encode the base (2, 8, or 16, with the fourth value reserved for future use). The next two bits encode a "scaling factor" value called F, restricted to values 0 to 3, and the final two bits encode the length (LE) of the exponent encoding (the exponent is encoded as a two's complement integer value immediately following this initial octet). The four values of LE allow for a one octet, two octet, or three octet exponent, with the fourth value indicating that the exponent field starts with a one octet length field, then the exponent value. Following the encoding of the exponent field we get the mantissa (M) as a positive integer encoding, terminated by the end of the contents octets (V part) in the usual way. 第一个位（第 8 位，最高有效位）被设置为 1，以表明这是一个二进制数值。接下来的位表示数的符号，而数值部分则被表示为一个正整数。接下来的两个位用于指定进制类型（2、8 或 16，第四个位保留供将来使用）。再接下来的两个位则编码一个称为 F 的“缩放因子”值，该值的范围限制在 0 到 3 之间。最后两个位则编码指数字段的长度（LE），指数字段是一个二进制补码整数，紧接在初始的 8 位字节之后。LE 的四个值可以对应 1 位、2 位或 3 位指数字段；第四个位表示指数字段以 1 位的长度字段开始，然后才是指数值。在指数字段编码之后，数值部分作为一个正整数进行编码，并以通常的方式结束，即位于内容字节部分的末尾。

The actual value of the real number encoded in this way is: 以这种方式编码的实数的实际值为：

$$
\texttt {S x M x (2 * *} \texttt {F) x (B * *} \texttt {E)}
$$

where \*\* above denotes exponentiation and x denotes multiplication. 其中，\*\*表示幂运算，而 x 表示乘法。

This is a fairly familiar way to represent floating point numbers, apart from the presence of F. We also need to discuss a little more the use of sign and magnitude instead of a 2's complement (or even 1's complement) mantissa. 这种表示浮点数的方法相当常见，不过其中使用了“F”这个符号。我们还需要进一步讨论使用符号和幅度来表示数值，而不是使用二进制补数或二进制补码来表示尾数。

In the early 1980s, there was very considerable variation in the form of floating point units, even within a single computer manufacturer, and although there are now de jure standards for floating point representation, there is in practice still a wide de facto variation. 在 20 世纪 80 年代初，即使是同一家计算机制造商生产的设备，其浮点运算单元的形式也存在很大的差异。虽然现在法律上有了关于浮点表示的标准，但实际上各种实现方式仍然存在很大的差异。

What has to be achieved (and was achieved) in the ASN.1 encoding of real is a representation that makes it (fairly) easy and quick for any floating point architecture to encode or decode values. 在 ASN.1 编码中，需要实现的目标就是创建一个能够让任何浮点运算架构都易于快速进行数值编码和解码的表达式。

Consider the choice between sign and magnitude or two's complement for the mantissa. If your actual hardware is two's complement, you can easily test the number and set the S bit, then negate the number, and you have a sign and magnitude format. If, however, your hardware was sign and magnitude and you are asked to generate a two's complement representation for transfer, the task is much more difficult. It is clear then that sign and magnitude is right for transfer, no matter which type of machine is most common. 在保留数的表示方式上，可以考虑使用符号表示法和绝对值表示法，或者二进制补码表示法。如果你的硬件使用的是二进制补码表示法，那么你可以很容易地测试数字，并设置 S 位，然后取数字的反转形式，这样就能得到符号表示法的数字了。然而，如果你使用的硬件是符号表示法，而你需要生成二进制补码表示法以供传输使用，那么任务就会变得复杂得多。显然，无论哪种类型的机器更为常见，符号表示法都是适合传输数据的表示方式。

The scaling factor F is included for a similar reason. All mantissa's have an implied decimal point position when the floating point value is dumped into main memory, but this is frequently not at the end of the mantissa field, that is, the mantissa is not naturally considered as an integer value. However, it is an integer value we wish to transfer in the ASN.1 encoding, and rather than try to encode the position of the implied decimal point, instead we recognise that the implied point can be moved one place to the right if we subtract one off the exponent value (for base 2). If the base is 8, one off the exponent value moves the implied decimal point three places right, and base 16 four places. Thus with a fixed (for this hardware) decrement to the exponent, we can get the implied decimal point close to the end of the mantissa. In particular, to within three positions of the end for a base 16 machine. By encoding an F value (which again is fixed for any given hardware), we can move the implied decimal point the remaining zero to three bits to get it exactly at the end. Of course a decoder has to multiply the resulting number by 2 to the power F, but this is quick and easy to do in a floating point unit. 之所以要包含缩放因子 F，也是出于同样的原因。当浮点数值被存入主内存时，所有的小数部分都带有隐含的小数点位置，但这一位置通常并不位于小数部分的末尾，也就是说，小数部分并不天然被视为一个整数值。然而，在 ASN.1 编码中，我们希望将其表示为一个整数值。因此，我们不会试图编码隐含的小数点位置，而是认识到，如果从指数值中减去 1（对于二进制基数而言），那么隐含的小数点就可以向右移动一位。如果基数为 8，那么指数值减 1 会使隐含的小数点向右移动三位；而对于基数为 16 的系统，则向右移动四位。因此，通过给指数值加上一个固定的值，我们可以使隐含的小数点靠近小数部分的末尾。特别是对于基于 16 的机器来说，误差可以控制在距离末尾三位以内。通过编码一个 F 值（该值……对于任何给定的硬件来说，“再次”这个操作都是可以实现的。我们可以将隐含的小数点移动到后面的零位上三个位置，这样就能使其正好位于末尾了。当然，解码器需要将得到的数字乘以 2 的 F 次方，不过这一步骤在浮点运算单元中操作起来非常快速且简单。

When this encoding was developed in the mid-1980s, there was a lot of discussion of these issues, and there was agreement over a range of vendors that the format provided a very good "neutral" format that they could all encode into and decode out of from a range of actual floating point hardware. Recommendation X.690/ISO 8825 Part 1 has a substantial tutorial annex about both the rationale for including F and also describing in some detail the algorithm needed to statically determine the encodings for a given floating point unit, and for encoding and decoding values. The interested reader is referred to this tutorial for further detail. 当这种编码方式在 20 世纪 80 年代中期被开发出来时，关于这些问题有很多讨论。许多供应商都认为，这种格式提供了一种非常优秀的“中立”格式，他们可以使用这种格式对实际使用的浮点硬件进行编码和解码。ISO 8825 标准中的 X.690 建议书第 1 部分中包含了关于为何要包含浮点运算的详细说明，同时还详细描述了用于确定特定浮点运算单元所需的编码方式，以及编码和解码过程的算法。有兴趣的读者可以参考该教程以获取更多详细信息。

Once again, in producing a canonical/distinguished encoding, we have to look at what options are being permitted, and eliminate them. We also have to concern ourselves with "normalization" of the representation. (This was illustrated in the character case above, where we required 4.E-1 rather than 0.4. A similar concern arises with the binary encoding.) For DER/CER/PER (all forms) we require that B be 2, that the mantissa be odd, that F be zero, and that the exponent and mantissa be encoded in the minimum number of octets possible. This is sufficient to remove all options. 在生成标准的/独特的编码方式时，我们必须考虑有哪些可行的选项，并排除那些不合适的选项。我们还必须关注表示的“规范化”问题。（正如上面的字符示例所示，我们需要使用 4.E-1 而不是 0.4。在二进制编码中也有类似的问题。）对于 DER/CER/PER（所有形式）来说，我们要求 B 为 2，尾数必须为奇数，F 为零，并且指数和尾数用最少的八位二进制数来表示。这样的要求足以排除所有不合适的选项。

## 3.5.3 Encoding the special real values 3.5.3 对特殊实数值的编码

There were early discussions about allowing special encodings for real values of the form "underflow" and "overflow", and for pi and other "interesting" values, but the only special values standardised so far (and there are unlikely to be any others now) are PLUS-INFINITY and MINUS-INFINITY. 最初有过关于为“下溢”和“溢出”这样的特殊数值，以及π和其他“有趣”的数值设置特殊编码的讨论。不过，目前唯一被标准化的特殊数值就是“正无穷”和“负无穷”。很可能不会再有其他特殊数值被标准化了。

And finally there are "special" real values that cannot easily be represented by normal character or floating point formats. 最后，还有一些“特殊”的实数，它们很难用常规的文字或浮点数格式来表示。

Recall that for a base 2 encoding the first (most significant) bit of the first contents octet is 1, and that for a base 10 encoding, the first two bits are zero. A special value encoding has the first two bits set to zero and one, with the remaining six bits of the first (and only) content octet identifying the value (two encodings only used). 需要注意的是，在二进制编码中，第一个内容八位组的第 1 位为 1；而在十进制编码中，前两位为 0。特殊值编码中，前两位分别设为 0 和 1，而第一个内容八位组剩下的 6 位则用于标识该值（仅使用两种编码方式）。

## 3.6 Encoding an OCTET STRING value 3.6 对 OCTET STRING 值进行编码

As was pointed out earlier, there are two ways of encoding an octet string - either as a primitive encoding, or as a series of TLV encodings, which we illustrate using the indefinite form for the outer-level TLV. 正如之前所指出的，对八位元字符串进行编码有两种方式：一种是使用原始编码方式，另一种则是使用 TLV 编码方式。我们以外层级 TLV 的无限形式为例来说明这两种编码方式。

Thus: 因此：

<table><tbody><tr><td data-imt-p="1">Pretty simple again - except that if you have a very long octet string you may want to fragment it to avoid counting it before transmission. Again, an encoder's option. 其实很简单——只不过，如果字符串的长度非常长，你可能需要将其分割开来，以避免在传输之前重复计算。这同样也是编码器可以选择的选项。</td></tr></tbody></table>

## octetstring OCTET STRING ::= '00112233445566778899AABBCCDDEEFF'H 八位组字符串 OCTET STRING ::= '00112233445566778899AABBCCDDEEFF'H

encodes as either 编码为以下任一方式：

<table><tbody><tr><td></td><td>T</td><td>L</td><td>V</td><td></td><td></td></tr><tr><td data-imt-p="1">octetstring: 八位组字符串：</td><td>04</td><td>10</td><td colspan="3">00112233445566778899AABBCCDDEEFF</td></tr><tr><td data-imt-p="1">or as octetstring: 或者作为八位元字符串：</td><td>24</td><td>80</td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td>T</td><td>L</td><td>V</td></tr><tr><td></td><td></td><td></td><td>04</td><td>08</td><td>0011223344556677</td></tr><tr><td></td><td></td><td></td><td>04</td><td>08</td><td>8899AABBCCDDEEFF</td></tr><tr><td></td><td></td><td>0000</td><td></td><td></td><td></td></tr></tbody></table>

There are a number of points to note here. Of course fragmentation makes little sense for such a short string, but it illustrates the form. We chose here to fragment into two equal halves, but in general we can fragment at any point. We chose not to fragment our fragments, but we are actually permitted to do so! In DER fragmentation is forbidden. In CER the fragment size is fixed at 1000 octets (no fragmentation if 1000 octets or under), and additional fragmentation of fragments is forbidden. 这里有几个需要注意的点。当然，对于如此短的一段数据来说，进行分割是没有意义的，但这说明了这种形式的特点。我们在这里选择将数据分割成两个相等的部分，不过一般来说，可以在任何点进行分割。我们选择不分割分割后的片段，但实际上是可以这样做的！在 DER 协议中，禁止进行分割操作。而在 CER 协议中，片段的大小被固定为 1000 个八位组（如果大小达到或低于 1000 个八位组，则不需要进行分割），并且还禁止对片段进行进一步的分割。

Finally, note that if the OCTET STRING had been implicitly tagged, the outer most T value (24 - universal class 4, constructed), would reflect the replacement tag, but the tag on each fragment would remain 04 (universal class 4, primitive). 最后，需要注意的是，如果 OCTET STRING 被隐式标记了，那么最外层的 T 值（24 - 通用类 4，构造型）将会反映替换标签的信息，而每个片段上的标签则仍然保持为 04（通用类 4，原始类型）。

## 3.7 Encoding a BIT STRING value 3.7 对位串值进行编码

For a BIT STRING value, we talk about the leading bit of the bitstring and the trailing bit, with the leading bit numbered as bit zero if we list named bits. The leading bit goes into the most significant bit of the first octet of the contents octets. Thus using the diagram conventions detailed earlier, the bits are transmitted with the left-most on the paper as the leading bit, proceeding to the right-most. When specifying a BIT STRING value, the value 对于 BIT 串值，我们讨论的是 BIT 串的首位和尾位。如果以命名方式来表示这些位，那么首位被编号为 0 位。首位位于内容八位组的第一个八位组的最高位。根据之前描述的图表规范，这些位按照从纸面的左端到右端的顺序进行传输。在指定 BIT 串值时，数值为……

<table><tbody><tr><td data-imt-p="1">BER length counts are always in octets. So how to determine the exact length of a bit string encoding? And what bit-value to pad with to reach an octet boundary? (Answer to the latter - encoder's option!) BER 长度总是以八位元为单位进行表示的。那么，如何确定用于编码的位串的确切长度呢？又该如何填充适当的位值以达到八位元的边界呢？（关于后一个问题的答案——由编码器自行决定！）</td></tr></tbody></table>

notation declares the left-most bit in the notation as the leading bit, so there is general consistency, except that the numbering of bits in a BIT STRING type goes in the opposite direction to the numbering of bits in an octet. 这种表示方式将表示法中最左侧的位指定为首位位。因此，这种表示方式具有一致性，只不过 BIT 串中位的编号方向与八位字节中位的编号方向相反。

As with an OCTET STRING value, BIT STRING value encodings can be primitive or broken into fragments. There is only one additional complication - the length count in BER is always a count of octets, so we need some way of determining how many unused bits there are in the last octet. This is handled by adding an extra contents octet at the start of the contents octets saying how many unused bits there are in the last octet. (In CER/DER these unused bits are required to be set to zero. BER has their values as a sender's option.) 与 OCTET STRING 值类似，BIT STRING 值的编码也可以采用原始形式，或者拆分为多个片段。不过还有一个额外的问题：在 BER 编码中，长度计数总是以八位组为单位进行统计的，因此我们需要一种方法来确定最后一个八位组中还有多少位未被使用。解决这个问题的方法是在描述内容部分的八位组开头添加一个额外的八位组，用来说明最后一个八位组中有多少位未被使用。（在 CER/DER 编码中，这些未被使用的位必须被设置为零。而在 BER 编码中，这些位的值则由发送方自行决定。）

If fragmentation of the bitstring into separate TLVs is performed, the fragments are required to be on an octet boundary, and the extra octet described above is placed (only) at the start of the last fragment in the fragmented encoding. 如果将对位串的分割成一个个独立的 TLV 结构，那么这些片段必须位于八位组的边界上。上述提到的额外八位组则只会被放置在分段编码中最后一个片段的起始位置。

Thus: 因此：

## bitstring BIT STRING ::= '1111000011110000111101'B 位串 BIT STRING ::= '1111000011110000111101'B

encodes as either 编码为以下任一方式：

<table><tbody><tr><td></td><td>T</td><td>L</td><td>V</td><td></td><td></td></tr><tr><td data-imt-p="1">bitstring: 比特串：</td><td>03</td><td>0F</td><td>02F0F0F4</td><td></td><td></td></tr><tr><td data-imt-p="1">or as bitstring: 或者像 bitstring 那样：</td><td>23</td><td>80</td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td>T</td><td>L</td><td>V</td></tr><tr><td></td><td></td><td></td><td>03</td><td>02</td><td>F0F0</td></tr><tr><td></td><td></td><td></td><td>03</td><td>02</td><td>02F4</td></tr><tr><td></td><td></td><td>0000</td><td></td><td></td><td></td></tr></tbody></table>

Again, fragmentation makes little sense for such a short string, and again in DER fragmentation is forbidden. In CER the fragment size is again fixed at 1000 octets (no fragmentation if 1000 octets or under), and additional fragmentation of fragments is forbidden. 同样，对于如此短的字符串来说，分片处理毫无意义。在 DER 协议中，分片处理是被禁止的。而在 CER 协议中，分片的大小被固定为 1000 个八位组（如果长度在 1000 个八位组或以下，则不需要分片处理），并且不允许对分片进行进一步的分片处理。

Apart from the extra octet detailing the number of unused bits, the situation is in all respects the same as for OCTET STRING. 除了额外增加了用于表示未使用位数的八个字节之外，其他方面的情况都与 OCTET STRING 的情况相同。

## 3.8 Encoding values of tagged types 3.8 对标记类型的值进行编码处理

If an implicit tag is applied (either by use of the word IMPLICIT, or because we are in an environment of automatic or implicit tagging), then as described in Section II, the class and number of the new tag replaces that of the old tag in all the above encodings. 如果使用了隐式标签（无论是通过“IMPLICIT”一词，还是因为处于自动或隐式标签使用的环境中），那么正如第二节所描述的，新标签的类别和编号将会取代旧标签在所有上述编码中的身份。

<table><tbody><tr><td data-imt-p="1">The final discussion of tagging!If its not clear by the end of thisclause, throw the book in theriver! 关于标签使用的最后讨论！如果到本节结束时仍然不清楚，那就把书扔到河里吧！</td></tr></tbody></table>

If however, an explicit tag is applied, we get the original encoding with the old tag, placed as a (single) TLV as the contents octets of a constructed encoding whose T part encodes the new (explicit) tag. 不过，如果使用了明确的标签，那么就会得到原始编码格式。在这种格式中，旧的标签被作为单独的 TLV 元素来放置，而构建出的编码内容则包含新的（明确的）标签的八位元数据。

For example: 例如：

integer1 INTEGER ::= 72 integer1 整数 ::= 72

integer2 \[1\] IMPLICIT INTEGER ::= 72 整数 2 \[1\] 定义为整数类型：72

integer3 \[APPLICATION 27\] EXPLICIT INTEGER ::= 72 整数 3 \[应用 27\] 显式整数 ::= 72

are encoded as 被编码为

<table><tbody><tr><td></td><td>T</td><td>L</td><td>V</td><td></td><td></td></tr><tr><td data-imt-p="1">integer1 整数 1</td><td>02</td><td>01</td><td>48</td><td></td><td></td></tr><tr><td data-imt-p="1">integer2 整数 2</td><td>C1</td><td>01</td><td>48</td><td></td><td></td></tr><tr><td data-imt-p="1">integer3 整数 3</td><td>7B</td><td>03</td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td>T</td><td>L</td><td>V</td></tr><tr><td></td><td></td><td></td><td>02</td><td>01</td><td>48</td></tr></tbody></table>

where the 7B is made up, in binary, as follows: 其中，7B 由以下二进制数字组成：

<table><tbody><tr><td data-imt-p="1">Class 班级</td><td data-imt-p="1" data-imt_insert_failed_reason="same_text">P/C</td><td data-imt-p="1">Number 数字</td></tr><tr><td>APPLICATION</td><td data-imt-p="1">Constructed 建造完成</td><td>27</td></tr><tr><td>01</td><td>1</td><td data-imt-p="1" data-imt_insert_failed_reason="same_text">11011 = 01111011 = 7B</td></tr></tbody></table>

## 3.9 Encoding values of CHOICE types 3.9 对 CHOICE 类型的数据进行编码处理

In all variants of BER, there are no additional TL wrappers for choices. The encoding is just that of the chosen item. The decoder knows which was encoded, because the tags of all alternatives in a choice are required to be distinct. 在所有的 BER 变体中，都不会为选项提供额外的标签封装。编码仅针对所选选项进行。解码器能够识别出哪个选项被选中了，因为每个选项的标签都必须各不相同。

<table><tbody><tr><td data-imt-p="1">This is either obvious or curious! There is no TLV associated with the CHOICE construct itself - you just encode the TLV for a value of the chosen alternative. 这要么很明显，要么就令人好奇！这个 CHOICE 结构本身并没有相关的 TLV 值——你只需要为所选选项编码一个 TLV 值即可。</td></tr></tbody></table>

So (compare with the encodings for the INTEGER and BOOLEAN types given above) 因此（与上面给出的 INTEGER 和 BOOLEAN 类型的编码进行比较）

and 以及

```txt
value1 CHOICE
{ flag BOOLEAN,
    value INTEGER} ::= flag:TRUE
value2 CHOICE
{flag BOOLEAN,
    value INTEGER} ::= value:72 
```

we get the encodings: 我们得到了这些编码：

<table><tbody><tr><td></td><td>T</td><td>L</td><td>V</td></tr><tr><td data-imt-p="1">value1 价值 1</td><td>01</td><td>01</td><td>FF</td></tr><tr><td data-imt-p="1">value2 价值 2</td><td>02</td><td>01</td><td>48</td></tr></tbody></table>

## 3.10 Encoding SEQUENCE OF values 3.10 值编码序列

This is quite straight-forward - an outer (constructed) TL as the wrapper, with a TLV for each element (if any) in the SEQUENCE OF value. 这非常直观——一个外部（构建的）主题列表作为包装层，而在值序列中，每个元素（如果有的话）都有一个主题标签。

So 那么，就这样吧。

<table><tbody><tr><td data-imt-p="1">You should know this already from the general discussion of the TLV approach. Nothing new here. 从对 TLV 方法的讨论中，你应该已经知道这一点了。这里并没有什么新内容。</td></tr></tbody></table>

 

$$
\begin{array}{r l} \text { temperature - each - day SEQUENCE(7)OF INTEGER } \\ & : := \{2 1, 1 5, 5, - 2, 5, 1 0, 5 \} \end{array}
$$

could be encoded as: 可以编码为：

<table><tbody><tr><td rowspan="2" data-imt-p="1">temperature-each-day: 每日温度：</td><td>T</td><td>L</td><td>V</td><td></td><td></td></tr><tr><td>30</td><td>80</td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td>T</td><td>L</td><td>V</td></tr><tr><td></td><td></td><td></td><td>02</td><td>01</td><td>15</td></tr><tr><td></td><td></td><td></td><td>02</td><td>01</td><td>0F</td></tr><tr><td></td><td></td><td></td><td>02</td><td>01</td><td>05</td></tr><tr><td></td><td></td><td></td><td>02</td><td>01</td><td>FE</td></tr><tr><td></td><td></td><td></td><td>02</td><td>01</td><td>05</td></tr><tr><td></td><td></td><td></td><td>02</td><td>01</td><td>10</td></tr><tr><td></td><td></td><td></td><td>02</td><td>01</td><td>05</td></tr><tr><td></td><td></td><td>0000</td><td></td><td></td><td></td></tr></tbody></table>

Of course, we could have employed definite length encoding at the outer level, which in this case would have saved two octets if the short form had been employed. 当然，我们可以在外部层次使用确定性长度编码方式。如果采用短格式，那么就可以节省两个八位元的空间。

## 3.11 Encoding SET OF values 3.11 编码 值集合

What are the actual set of abstract values? Is {3, 2} the same value as {2, 3}? It should be! So we must have just one encoding in distinguished/canonical encoding rules for this single value. This produces a significant cost at encode time. Best not to use set-of if you want to have distinguished/canonical encodings. 那么，这些抽象值到底是什么呢？{3, 2}和{2, 3}到底代表相同的数值吗？应该是这样的吧！因此，对于这个单一值，我们只需要使用一种编码方式即可。不过，这种编码方式在编码时会产生相当大的成本。所以，如果想要使用区分化/规范化的编码方式，就最好不要使用集合形式的编码方式。

The encoding of set-of is just the same as for sequence-of except that the outer T field is 31. If, however, this were a CER or DER encoding then the seven TLVs would be sorted into ascending order and we would get: 这种编码方式与“序列”类型的编码相同，只不过外部的 T 字段值为 31。不过，如果这是 CER 或 DER 编码，那么这七个 TLV 字段会被按照升序排序，最终会得到如下结果：

$$
\begin{array}{c c c c c} \text {unordered - weeks - temps SET (7) OF INTEGER} \\ : := \{2 1, 1 5, 5, - 2, 5, 1 0, 5 \} \\ \text {weekstemperatures:} & T & L & V \\ & 3 1 & 8 0 \\ & & & T & L & V \\ & & & 0 2 & 0 1 & F E \\ & & & 0 2 & 0 1 & 1 5 \\ & & & 0 2 & 0 1 & 1 0 \\ & & & 0 2 & 0 1 & O F \\ & & & 0 2 & 0 1 & 0 5 \\ & & & 0 2 & 0 1 & 0 5 \\ & & & 0 2 & 0 1 & 0 5 \\ & & & 0 0 0 0 \end{array}
$$

Notice that the sort is on the final encodings of each element, so the temperature -2 sorts ahead of the temperature 21. 注意，排序是按照每个元素的末尾编码来进行的，因此温度-2 比温度 21 更优先排序。

## 3.12 Encoding SEQUENCE and SET values 3.12 对序列和集合值进行编码

These are exactly similar, except that now the inner TLVs (one for each element of the sequence or set) will be of varying size and have varying tags. In some cases these elements may themselves be sequences or sets, so we may get deeper nesting of TLVs (to any depth). 这些其实都是类似的，只不过现在每个序列或集合中的元素内部的 TLV 大小各不相同，而且每个 TLV 都有不同的标签。在某些情况下，这些元素本身也可能是其他序列或集合，因此 TLV 的嵌套层次可能会更加深。

<table><tbody><tr><td data-imt-p="1">Back to simplicity again. Nested TLVs, to any depth. 再次回归简单性。嵌套的 TLV 可以嵌套到任意深度。</td></tr></tbody></table>

If there are optional elements, and the abstract value of the sequence or set does not contain a value for these elements, then the corresponding TLV is simply omitted. 如果存在一些可选元素，而序列或集合的抽象值并不包含这些元素的对应值，那么相应的 TLV 就会被省略。

In the case of SET, BER allows the nested TLVs to be appear in any order chosen by the encoder. In DER, the elements are sorted by the tag of each element (which again are required to be distinct). However, if we have 在 SET 的情况下，BER 允许嵌套的 TLV 以编码器选择的任意顺序出现。而在 DER 中，元素则是按照每个元素的标签进行排序的（当然，这些标签必须是唯一的）。不过，如果我们拥有多个……

```txt
My-type ::= SET OF
{ field1 INTEGER,
    field2 CHOICE
    { flag BOOLEAN,
    dummy NULL } } 
```

then each set-of value contains an integer value plus either a boolean or a null value. But in the sort into ascending order of tag, a boolean value would come before an integer value but a null value after it. Thus depending on which value of field2 is chosen, it may appear before or after the value of field1! In CER, a slightly more complicated algorithm applies which says that the maximum tag that appears in any value of field2 is the NULL tag, and that that determines the position of field 2 no matter what value is actually being sent. This is marginally more difficult to explain and perhaps understand, but avoids having to do a sort at encode time. 每组值都包含一个整数值，外加一个布尔值或空值。但在按标签升序排序时，布尔值会出现在整数值之前，而空值则会出现在整数值之后。因此，根据 field2 中选择的数值，它可能会出现在 field1 的值之前或之后！在 CER 中，采用了一种稍微复杂的算法：在任何 field2 的值中，出现次数最多的标签是 NULL 标签。这一规则决定了 field2 的位置，而不管实际发送的是哪种值。这种方法虽然解释起来稍微复杂一些，但可以避免在编码过程中进行排序操作。

## 3.13 Handling of OPTIONAL and DEFAULT elements in sequence and set 3.13 如何处理序列和集合中可选的以及默认的元素

There are no problems caused by OPTIONAL (the use of tags makes it unambiguous what has been included and what has not). However, in the case of DEFAULT, BER leaves it as a sender's option whether to omit 使用可选标签可以确保明确区分哪些内容已被包含，哪些没有包含。不过，在默认情况下，BER 允许发送方自行决定是否忽略某些内容。

a default value (implying possibly complex checking that it is the default value), or whether to encode it anyway! 是否使用默认值（这意味着可能需要进行复杂的检查来确保确实是默认值），还是无论如何都要将其编码处理！

Again, this gives DER and CER problems to remove this encoder's option. In this case they both require that an element whose value equals the default value be omitted, no matter how complicated the check might be. (However, in practice, DEFAULT is normally applied only to elements that are very simple types, rarely to elements that are complex structured sequences and sets). 同样，这也会带来 DER 和 CER 方面的问题，需要去除这个编码器的选项。在这种情况下，无论检查过程多么复杂，都要求将那些值等于默认值的元素进行省略。（不过，实际上，DEFAULT 选项通常只适用于非常简单的元素，很少应用于结构复杂的序列和集合。）

When we discuss PER more fully in the next chapter, however, we find that PER specifies mandatory omission for "simple types" (which it lists) and a sender's option otherwise, avoiding verbosity in and options incommon cases, but avoiding implementation complexity in the other cases. 在下一章中，当我们更详细地讨论 PER 时，会发现 PER 规定了对“简单类型”的强制省略规则，而在其他情况下则允许选择省略，这样可以在常见情况下避免不必要的复杂性，同时也能降低实现上的复杂度。

## 3.14 Encoding OBJECT IDENTIFIER values 3.14 编码对象标识符值

The value is basically a sequence of integers, but we need a more compact encoding than using "SEQUENCE OF INTEGER". The "more bit" concept comes in again here, but with a curious (and nasty) optimization for the top two arcs. 这个值本质上是一个整数序列，不过我们需要一种比“整数序列”更简洁的编码方式。这里又出现了“更节省比特数”的概念，不过对于前两个弧线来说，这种优化方式有些奇怪且不太理想。

Figure III-12 is a repeat of Figure II-1, and shows a part of the object identifier tree. 图 III-12 是图 II-1 的重复显示，它展示了对象标识符树的一部分结构。

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/54379e17-c034-430b-894c-f77661f731e5/8eb5b15270b1140cff5eb2b8d49c06d17c780b047474c4aebd4678532c875505.jpg)

Object identifier values are paths down this tree from the root to a leaf, and one such path is defined by 对象标识符的值就是沿着这棵树从根到叶子的路径。而这样的路径之一就是由…所定义的。

$$
\{\text { iso(1) standard(0) 8571 abstract - syntax(2) } \}
$$

but the only information that is encoded is a value of 但是，唯一被编码的信息只是一个数值而已。

$$
\left\{ \begin{array}{c c c c} 1 & 0 & 8 5 7 1 & 2 \end{array} \right\}
$$

This could in theory be carried by an encoding of "SEQUENCE OF INTEGER", but the presence of T and L fields for each integer value makes this rather verbose, and a different (ad hoc) encoding is specified. 理论上，这可以通过编码“整数序列”来实现。不过，对于每个整数值，都需要使用 T 和 L 字段进行表示，这使得编码方式相当冗长。因此，采用了一种不同的、更为灵活的编码方式。

The "more bit" concept (also used in the encoding of tags – see Figure III-6 in 2.2) is used. For each object identifier component (the values 1, 0, 8571 and 2 above), we encode it as a positive integer value into the minimum necessary number of bits (the standard requires that the minimum multiple of seven bits is used), then place those bits into octets using only the least significant seven bits of each octet (most significant octet first). Bit 8 (most significant) of the last octet is set to 0, earlier bit 8 values (the "more" bit) are set to 1. 采用了“更多位”这一概念（该概念也用于标签的编码中——参见 2.2 节中的图 III-6）。对于每一个对象标识符组件（上述提到的 1、0、8571 和 2 这些值），我们将其编码为尽可能少位的整数值（标准要求使用至少 7 位的倍数）。然后，将这些位转换为八位二进制数，只使用每个八位中最低的 7 位（最高位的 8 位优先处理）。最后一个八位的最高位被设置为 0，而之前的最高位则被设置为 1，即所谓的“更多位”。

The result of encoding 编码的结果

 

$$
\text { ftam - oid OBJECT IDENTIFER }: := \{1 0 8 5 7 1 2 \}
$$

would be (in hex): 在十六进制中表示的话是：

<table><tbody><tr><td></td><td>T</td><td>L</td><td>V</td><td></td><td></td><td></td></tr><tr><td data-imt-p="1">ftam-oid: 类似 ftam 的：</td><td>06</td><td>05</td><td>01</td><td>00</td><td>C27B</td><td>02</td></tr></tbody></table>

However, the actual encoding of this object identifier value is 不过，这个对象标识符值的实际编码方式是……

<table><tbody><tr><td>T</td><td>L</td><td>V</td></tr><tr><td>06</td><td>04</td><td data-imt-p="1" data-imt_insert_failed_reason="same_text">28 C27B 02</td></tr></tbody></table>

How come? 怎么会这样呢？

A dirty trick was played! (And like most dirty tricks, it caused problems later). 一个卑鄙的伎俩被利用了！（就像大多数卑鄙的伎俩一样，这个伎俩后来引发了问题。）

The octets encoding the first two arcs were (in 1986) thought to be unlikely to ever have large values, and that using two octets for these two arcs was "a bad thing". So an "optimization" (mandatory) was introduced. 在 1986 年时，人们认为用于编码前两个弧线的八位组的值不太可能达到较大的数值，因此使用两个八位组来表示这两个弧线被认为是“不妥的”。于是，人们引入了一种“优化”方案（这是必须的）。

We can take the top two arcs of Figure III-12 and "overlay" them with the dotted arcs shown in Figure III-13, producing a single (pseudo) arc from the root to each second level node. How to number these pseudo-arcs? 我们可以选取图 III-12 中前两个弧线，并将其与图 III-13 中显示的虚线弧线进行“叠加”。这样，就能得到一条从根节点到每个第二级节点的伪弧线。那么，该如何为这些伪弧线编号呢？

Well, there are three top-level arcs, and we can accommodate encodings for up to 128 arcs (0 to 127) in a single octet with the "more bit" concept described above. 128 divided by 3 is about 40! Let's assume the first two top-level arcs will never have more than 40 sub-arcs, and allocate the first 40 pseudo-arcs to top-level arc 0, the next 40 to top-level arc 1, and the remainder to top-level arc 2. 嗯，总共有三个顶层弧点。通过上述的“更多位”概念，我们可以在一个八位元中容纳最多 128 个弧点的编码信息（0 到 127）。128 除以 3 约等于 40！假设前两个顶层弧点最多只有 40 个子弧点，那么可以将前 40 个子弧点分配给顶层弧点 0，接下来的 40 个分配给顶层弧点 1，剩下的部分则分配给顶层弧点 2。

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/54379e17-c034-430b-894c-f77661f731e5/2aea3e26801372abe6a42602994299592adf6633fb77063f15b1d3d7c0f3e6b3.jpg)

Figure III-13: Making the top two arcs into a single arc 图 III-13：将两条最上面的弧线合并为一条弧线

So for any second level arc beneath top-level arc 0, we use the second level arc number as the number for the pseudo-arc. For any second-level arc beneath top-level arc 1, we use the second level arc number plus 40 as the number for the pseudo-arc, and for any second-level arc beneath top-level arc 2, we use the second level arc number plus 80 as the number for the pseudo-arc. 因此，对于位于最高级别弧线 0 下方的任何二级弧线，我们使用该二级弧线的编号作为伪弧线的编号。对于位于最高级别弧线 1 下方的任何二级弧线，我们使用该二级弧线的编号加上 40 作为伪弧线的编号；而对于位于最高级别弧线 2 下方的任何二级弧线，我们使用该二级弧线的编号加上 80 作为伪弧线的编号。

We then get the encoding of {1 0 8571 2} as 然后，我们将{1 0 8571 2}编码为

$$
\begin{array}{c c c c c} \mathbf {T} & \mathbf {L} & \mathbf {V} \\ 0 6 & 0 4 & 2 8 \text {C27B} 0 2 \end{array}
$$

as described earlier. 如之前所述。

As was pointed out earlier, where you are "hung" on the object identifier tree is unimportant, except that your object identifiers will be longer the lower down you are. In mid-1995 this surfaced as an issue, with other major international players wanting top-level arcs. The above "fudge" with the top two arcs makes it difficult (not impossible, but difficult) to add new top-level arcs, and to alleviate this problem the RELATIVE OID constructor was proposed for addition to ASN.1. 正如之前所指出的，你在对象标识符树中处于什么位置并不重要，只是越往下层次，对象标识符就会越长一些。到了 1995 年中期，这个问题变得明显起来，因为其他主要的国际机构希望拥有最高级别的弧段。对前两个弧段进行这种“调整”使得添加新的最高级别弧段变得困难（虽然并非完全不可能，但确实比较困难）。为了解决这个问题，人们提出了在 ASN.1 中添加“相对 OID 构造器”的方法。

If an organization has the need to allocate object identifiers beneath a root such as: 如果一个组织需要在根节点下分配对象标识符，例如：

$$
\left\{\text { joint - iso - itu - t(2) } \quad \text { internationalRA(2)set(42) } \right\}
$$

and has a protocol that is specifically designed to carry (always or commonly) object identifier values beneath this root, then it can define 并且有一个专门设计的协议，用于承载位于此根下的对象标识符值（总是或通常会如此）。那么，就可以定义这样的结构了。

$$
\begin{array}{r l} \text {SET - OIDs} & : := \text {RELATIVE OID} \\ & \quad \text {- - Relative to\{2 2 42\}} \end{array}
$$

and use that type in its protocol, either alone or as a CHOICE of that and a normal OBJECT IDENTIFIER. 在协议中可以使用这种类型，可以单独使用，也可以作为普通对象标识符的选择之一来使用。

A relative object identifier type is only capable of carrying object identifier values that hang below a known node (in this case {2 2 42}), but the encoding of the value encodes only the object identifier components after {2 2 42}, saving in this case two octets. 相对对象标识符类型只能携带那些位于已知节点下方的对象标识符值（在本例中为{2 2 42}）。该标识符的编码方式仅包含了对象标识符组件的信息，而{2 2 42}之后则不需要再编码额外的八位元数据，从而节省了两个八位元。

The saving can be more significant in PER, where encodings are generally smaller anyway. In the case of Secure Electronic Transactions (SET), getting ASN.1 encodings of certificates down to a size that will fit easily on a smart card posed some challenges, and the use of PER and the relative object identifier technique was important. 在 PER 方面，这种优化可以带来更大的节省效果，因为无论如何，编码的尺寸通常都较小。在安全电子交易（SET）场景中，将证书对应的 ASN.1 编码压缩到适合智能卡存储的大小是一个挑战，而使用 PER 技术和相对对象标识符技术则显得非常重要。

At the time of going to press, the RELATIVE OID work was not finalised, so do check details with the latest standard! (And/or look for errata sheets for this book on the Web site in Appendix 5). 在出版之前，RELATIVE OID 项目的文档尚未完成最终定稿，因此请务必与最新标准进行核对！（或者可以在附录 5 中的网站上下载该书的勘误表。）

## 3.15 Encoding character string values 3.15 编码字符串值

The character string types (as with the time types described below) are encoded by reference to other standards. A more detailed description of these character set standards is included in Section IV, but the basic characteristics of each encoding is described here. 字符字符串类型（就像下面提到的时间类型一样）是通过引用其他标准来编码的。这些字符集标准的详细描述可以在第四部分中找到，但这里会简要介绍每种编码方式的基本特性。

<table><tbody><tr><td data-imt-p="1">Here's where you have to go out and buy additional specifications - almost all the character string encodings are by reference to other specifications. 在这里，你需要去购买额外的功能规格——几乎所有的字符编码都是基于其他规格来定义的。</td></tr></tbody></table>

There is probably more text in this book than in the ASN.1 Standard itself! 这本书中的内容可能比 ASN.1 标准本身还要多！

Starting with the simplest character string types - NumericString, PrintableString, VisibleString, and GraphicString - the contents octets of these are just the ASCII encoding of the characters. 从最简单的字符字符串类型开始——NumericString、PrintableString、VisibleString 和 GraphicString。这些类型的内部字节序列实际上都是对应字符的 ASCII 编码形式。

The next group is TeletexString, VideotexString, GraphicString and GeneralString. These have encodings whose structure is specified in ISO 2022, using "escape sequences" specified for each Register Entry in the International Register to "designate and invoke" that register entry. After the appropriate escape sequence, subsequent eight bit encodings reference characters from that register entry until the next escape sequence occurs. It is important to note that there are many characters that appear in multiple register entries, so there are frequently many encodings for a given character string. It is also theoretically possible to have a succession of escape sequences each one over-riding the last, with no intervening character encoding. In the distinguished/canonical encoding rules, all these options are eliminated. 下一个编码组是 TeletexString、VideotexString、GraphicString 和 GeneralString。这些编码的结构遵循 ISO 2022 标准，使用“转义序列”来“指定和调用”每个寄存器条目。在适当的转义序列之后，接下来的八位编码会引用该寄存器条目中的字符，直到下一个转义序列出现。需要注意的是，有许多字符出现在多个寄存器条目中，因此对于一个给定的字符字符串，通常会有多种编码方式。理论上，也可以连续使用多个转义序列，而中间没有任何字符编码。但在标准的编码规则中，这些选项都被排除了。

The next two character set types to consider are UniversalString and BMPString. UniversalString supports all the characters of ISO 10646 (the most recent character code standard, using 32 bits per character in the encoding. BMPString supports only those characters in the "Basic Multilingual Plane" (sufficient for all normal earthly activity!) which also corresponds to the "Unicode" character set, using 16 bits per character. 接下来需要考虑的两种字符集类型分别是 UniversalString 和 BMPString。UniversalString 支持 ISO 10646 标准中的所有字符（这是最新的字符编码标准，每个字符使用 32 位来表示）。而 BMPString 则仅支持“基本多文种平面”中的字符，这些字符足以满足所有日常使用的需求！此外，BMPString 还使用 16 位来表示每个字符，这也与“Unicode”字符集相对应。

Finally, UTF8String uses a variable number of octets per character (from one for the ASCII characters to a maximum of six octets). None of the octets in a UTF8String encoding have the top bit set to zero unless they are the (single octet) encoding of an ASCII character. The encoding of octets that form a single character always start with "10" unless they are the first octet of the encoding of a character, so even if you start at a random point in the middle of an encoding, you can easily identify the start of the next character encoding. 最后，UTF8String 每个字符使用的八位元数量是可以变化的（从单个八位元用于 ASCII 字符，最多可达六个八位元）。在 UTF8String 编码中，除非某个八位元代表一个 ASCII 字符，否则其最高位永远不会被设置为零。而构成单个字符的八位元编码总是以“10”开始，除非它们是某个字符的第一个八位元。因此，即使你从编码中间的随机位置开始阅读，也很容易就能识别出下一个字符的起始位置。

A UTF8 encoding of a character has an "initial octet" that either starts with a "0" bit (in which case we have a single octet ASCII encoding), or starts with two to six one bits followed by a zero bit. Remaining bits in this first octet are available to identify the character. The number of one bits gives the number of octets being used to encode the character. Each subsequent octet has the top two bits set to "10", and the remaining six bits are available to identify the character. The character is identified by its number in the ISO 10646 32-bit coding scheme, which is encoded into the available bits (right justified), using the minimum number of octets necessary. Thus characters with values less than two to the power 11 (which is all "European" characters) will encode into two octets, and characters with values less than two to the power 16 will encode into three characters, and so on. UTF8 编码中，一个字符的“首个八位组”要么以“0”位开始（这种情况下，只是一个八位组的 ASCII 编码），要么以两个到六个 1 位 followed by 一个 0 位开始。这个首个八位组中的其余位可以用来标识该字符。1 位的数量决定了用于编码该字符的八位组的数量。每个后续的八位组中，最高两位被设置为“10”，其余六位则可用于标识该字符。该字符通过 ISO 10646 32 位编码方案中的数值来标识，该方案将数值编码到可用的位中（右对齐），同时使用最少的八位组数量。因此，值小于 2 的 11 次方（即所有“欧洲字符”）的字符将被编码为两个八位组，而值小于 2 的 16 次方以上的字符则会被编码为三个八位组，依此类推。

Some examples of UTF8 encodings of characters are given in Figure III-14 as hex representations. 在图 III-14 中，给出了一些 UTF8 编码字符的十六进制表示示例。

<table><tbody><tr><td data-imt-p="1">Name of character 角色名称</td><td data-imt-p="1">Unicode/10646 number Unicode 编码/10646 号数字</td><td data-imt-p="1">Encoding in binary 二进制编码</td></tr><tr><td data-imt-p="1">LATIN CAPITAL LETTER H 拉丁字母 H</td><td>72</td><td>01001000</td></tr><tr><td data-imt-p="1">LATIN DIGIT ZERO 拉丁数字零</td><td>48</td><td>00110000</td></tr><tr><td data-imt-p="1">LATIN CAPITAL LETTER C WITH CEDILLA 带有连音符号的拉丁文大写字母 C</td><td>199</td><td>11000011 10000111</td></tr><tr><td data-imt-p="1">GREEK CAPITAL LETTER BETA 希腊大写字母 BETA</td><td>914</td><td>11001110 10010010</td></tr><tr><td data-imt-p="1">CYRILLIC CAPITAL LETTER EN 西里尔字母表中的大写字母 E</td><td>1053</td><td>11010000 10011101</td></tr><tr><td data-imt-p="1">ARABIC LETTER BEHEH 阿拉伯字母“BEHEH”</td><td>1664</td><td>11011010 10000000</td></tr><tr><td data-imt-p="1">KATAKANA LETTER KA 片假字“KA”</td><td>12459</td><td>11100001 10100001 10101011</td></tr></tbody></table>

Figure III-14: Some examples of UTF8 Encodings 图 III-14：一些 UTF8 编码的示例

## 3.16 Encoding values of the time types 3.16 对时间类型的值进行编码处理

The time types are specified as strings of characters, and their encoding is simply the ASCII encoding of those characters. 时间类型被表示为字符字符串，其编码方式就是这些字符的 ASCII 编码。

There were problems with the precision of GeneralizedTime. The actual referenced standard is GeneralizedTime 的精度存在一些问题。实际上，所参考的标准并不符合要求。

Simply an ASCII encoding of the characters. But watch out for issues of precision in the distinguished/canonical rules. 这只是字符的 ASCII 编码而已。不过需要注意在区分大小写/规范规则方面所存在的精度问题。

ISO 3307, which from its first edition in 1975 permitted seconds to have any number of decimal places. But somehow some parts of the ASN.1 implementor community had got the impression that the precision was limited to milliseconds, and would not accept values to a greater precision. ISO 3307 在 1975 年首次发布时，允许秒数可以有任意多的小数位。不过，似乎有些 ASN.1 实施者认为该数值的精度仅限于毫秒级别，不会接受更高精度的数值。

There are also issues with what is the precise set of abstract values. The ASN.1 specification states that GeneralizedTime allows the representation of times to a variety of precisions. So, for example, is a time of: 此外，关于究竟哪些抽象值才是有效的设定也存在一些问题。ASN.1 规范中提到，GeneralizedTime 允许以多种精度来表示时间。例如，时间可以表示为：

## "199205201221.00Z" “199205201221.00Z”

the same abstract value as 与……具有相同的抽象价值

## "199205201221.0Z" “199205201221.0Z”

If so, then the canonical and distinguished encoding rules should forbid one or the other encoding (or even both!). But if it is regarded that different precisions are different abstract values (and may carry different semantics), then all such encodings need to be allowed in the canonical and distinguished encoding rules. 如果是这样的话，那么标准的、权威的编码规则应该禁止其中一种或两种编码方式的使用！不过，如果认为不同的精度代表着不同的抽象值（并且可能具有不同的语义），那么所有这些编码方式都应该在标准的、权威的编码规则中被允许。

The eventual ruling was that the implied precision by the inclusion of trailing zeros was not a primary part of the abstract value, and that in the distinguished and canonical encoding rules trailing zeros should be forbidden - a time to an implied precision of one hundredth of a second is the same time (abstract value) as one to an implied precision of one tenth of a second, and should not carry different semantics, and should have the same encoding in the distinguished and canonical encoding rules. 最终的裁决是，通过添加尾随零来体现的精确性并非该抽象值的核心要素。在规范的编码规则中，应该禁止这种尾随零的使用——因为将一百分之一秒的精度与一十分之一秒的精度视为相同的抽象值，两者不应具有不同的语义含义，并且在规范和标准的编码规则中都应该采用相同的编码方式。

## 4 Encodings for more complex constructions 4 种编码方式，适用于更复杂的构造情况

## 4.1 Open types 4.1 开放类型

ASN.1 has had the concept of "holes" from its inception, originally described as a type called "ANY", and later as a so-called "open type" specified with syntax looking like: 从一开始，ASN.1 就包含了“空洞”这一概念。最初，这种空洞被描述为一种名为“ANY”的类型；后来则被定义为一种所谓的“开放类型”，其语法规范如下所示：

Most of the more complex types are defined as ASN.1 SEQUENCE types, and their values encode by encoding values of those sequence types. 大多数较为复杂的类型都被定义为 ASN.1 序列类型。这些类型的值就是对这些序列类型的值进行编码后得到的。

## OPERATOR.&Type 操作员。&类型

stating that the type that will fill this field is the value of some ASN.1 type that is assigned to the &Type field of an information object of the OPERATOR class (see Section II Chapter 6). 声明将填充此字段的类型，是某种被分配给操作对象的信息对象中的&Type 字段的 ASN.1 类型的值（详见第 6 章第二节）。

BER handles open types very simply: What eventually fills this field has to be an ASN.1 type, and the encoding of the field is simply the encoding of a value of that type. BER 对开放类型的数据处理非常简单：填充此字段的数据必须是一个 ASN.1 类型，而该字段的编码方式则简单地对应于该类型值的编码方式。

Remember that in BER there is a strict TLV structure, so it is always possible to find the end of a BER TLV encoding without any knowledge of the actual type being encoded. In the case of an open type, the identification of that type may appear later in the encoding than the occurrence of the encoding of a value of the type. That gives no problem in BER, because the TLV structure is independent of the type. 请记住，在 BER 编码中，存在一个严格的 TLV 结构。因此，即使不了解实际要编码的类型，也总能找到 BER TLV 编码的结尾。对于开放类型来说，该类型的标识可能在编码中出现的位置之后才被定义。但在 BER 编码中这并不构成问题，因为 TLV 结构与类型本身是独立的。

## 4.2 The embedded pdv type and the external type 4.2 嵌入式 PVD 类型与外部类型

As described in Section II, these are slightly obscure names for ASN.1 types, but the "embedded" means that here we have foreign (non-ASN.1-defined) material embedded in an ASN.1 type, and the "external" means more or less the same thing - material external to ASN.1 is being embedded. 如第二节所述，这些名称对于 ASN.1 类型来说有些晦涩难懂。不过，“嵌入式”意味着这些内容是嵌入到 ASN.1 类型中的外部数据；“外部的”则指的是那些位于 ASN.1 类型之外的数据。

Historically, EXTERNAL came first, and EMBEDDED PDV was added in 1994 with slightly greater functionality (new specifications should always use EMBEDDED PDV, not EXTERNAL). 从历史上看，最初使用的是“EXTERNAL”模式。而“ EMBEDDED PDV”模式则是在 1994 年才被引入的，其功能稍显完善一些（新的规范建议始终采用“ EMBEDDED PDV”模式，而不是“EXTERNAL”模式）。

Both these types have "associated types" which are sequence types, and which have fields capable of carrying all the semantics of the type. Broadly, this is the encoding of some material (carried as a bitstring in the most general case) and identification (using one object identifier in the case of EXTERNAL and zero to two in the case of EMBEDDED PDV) of the abstract and transfer syntax for the encoding in the bitstring. (There is some slight additional complexity by the inclusion of options that apply when the encodings are transferred over an OSI Presentation Layer protocol, but this does not affect the encoding in the non-OSI case.) The BER encoding is simply defined as the encoding of these "associated types". 这两种类型都包含“相关类型”，即序列类型，这些类型具有能够承载该类型所有语义的字段。总体而言，这种编码方式是将某种数据编码为位串（在最一般的情况下），同时还会为这种编码方式提供唯一标识（对于 EXTERNAL 类型，使用一个对象标识符；对于 EMBEDDED PDV 类型，则使用零到两个对象标识符）。此外，当这些编码信息通过 OSI 表示层协议传输时，还会有一些额外的复杂性，但这些复杂性并不影响非 OSI 情况下的编码过程。BER 编码则简单地被定义为对这些“相关类型”的编码方式。

## 4.3 The INSTANCE OF type 4.3 类型“INSTANCE”的实例

The INSTANCE OF type provides a very simplified version of EXTERNAL or EMBEDDED PDV, designed specifically for the case where what we want to put into our "hole" is a (single) object identifier to identify the (ASN.1) type whose value is encoded into the "hole", followed by a value of that ASN.1 type. This type relates to the built-in very simple information object class TYPE-IDENTIFIER described in section II. 这种类型的定义提供了一种非常简化的版本，用于替代 EXTERNAL 或 EMBEDDED PDV 方式。这种方式的目的是将某个对象标识符放入“孔洞”中，该标识符标识着一种 ASN.1 类型，而其具体值则会被编码到“孔洞”中。这种类型与第二节中提到的内置简单信息对象类 TYPE-IDENTIFIER 相关。

It is encoded as a SEQUENCE type with just two fields - an object identifier and the value of an ASN.1 type (as an open type). 该类型被编码为一种序列类型，仅包含两个字段：一个对象标识符，以及一个 ASN.1 类型的值（作为一种开放类型）。

## 4.4 The CHARACTER STRING type 4.4 字符字符串类型

The CHARACTER STRING type was introduced in 1994, and is almost identical to EMBEDDED PDV in its encoding. The idea here is that we have the value of a character string (from some repertoire identified by a character abstract syntax object identifier) is encoded according to a character transfer syntax object identifier. Thus we have essentially an encoding of a sequence comprising zero to two object identifiers (as with EMBEDDED PDV, there are options where either or both object identifiers take fixed values determined by the protocol specification and which therefore do not need to be encoded), followed by the encoding of the actual characters in the string. CHARACTER STRING 类型是在 1994 年引入的，其编码方式与 EMBEDDED PDV 几乎完全相同。这里的原理是：将字符字符串的值按照字符传输语法对象的标识符进行编码。因此，实际上我们是对一系列对象标识符的编码——这些对象标识符的数量可以是零个，也可以是两个。与 EMBEDDED PDV 一样，有些情况下，某个或两个对象标识符会固定取值，这些固定值由协议规范决定，因此无需进行编码。之后，就是对字符串中实际字符的编码。

## 5 Conclusion 5 结论

The ASN.1 specification of BER is just 17 pages long - less than this chapter! (Ignoring the Annexes and details of DER and CER). The interested reader should now have no problems in understanding that specification. Go away and read it! BER 的 ASN.1 规范仅有 17 页——比这一章的内容还要少！（不包括附录以及 DER 和 CER 的相关细节）。有兴趣的读者应该能够轻松理解这一规范。那就去阅读它吧！

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/54379e17-c034-430b-894c-f77661f731e5/87b5c16d558dec77afcdc069928e79327f29dcf35af1f1c014bb30d70e002b13.jpg)

# Chapter 3 The Packed Encoding Rules 第三章 打包编码规则

(Or: Encodings for the next millennium - as good as you'll get – for now!) （或者：为下一个千年准备的编码方案——目前来看，这已经算是相当不错的了……）

Summary: This chapter provides details of the Packed Encoding Rules. It has broadly two main parts. In the first part further details are given of some of the global features of PER and the terminology employed in the actual specification. In this first part we cover: 摘要：本章详细介绍了打包编码规则的相关内容。全书大致分为两部分。第一部分详细阐述了 PER 的一些全局特性以及规范中使用的术语。在这一部分中，我们涵盖了以下内容：

• The overall structure of a PER encoding and the terminology used (preamble, length determinant, contents), with discussion of the four variants of PER. • PER 编码的整体结构以及所使用的术语（前导码、长度确定器、内容等），同时讨论了 PER 的四种不同变体。

• The general nature of encodings for extensible types. • 可扩展类型的编码通用特性。

• PER-visible constraints. • 可见性限制。

• Effective size and alphabet constraints. • 有效的尺寸和字母表限制。

• Canonical order of tags, and the use of this ordering. • 标签的规范排序方式，以及这种排序方式的应用情况。

• The form of a general length field, when needed. • 在需要的时候，可以使用通用长度字段的形式来表示数据。

• The OPTIONAL bit-map and the CHOICE index (for extensible and non-extensible choices) • 可选的位图格式，以及用于表示可扩展与不可扩展选项的选择索引

The second part gives details of the encodings of each ASN.1 type in much the same way as was done for BER in the previous chapter. The order is again chosen in a way that moves from the simpler to the slightly more complex encodings. We cover the encodings of: 第二部分详细介绍了每种 ASN.1 类型的编码方式，其描述方式与上一章中对 BER 编码的描述方式类似。这些编码的顺序也是按照从简单到稍复杂的顺序来安排的。我们涵盖了以下编码方式：

• NULL and BOOLEAN values. • 空值以及布尔值。

• INTEGER values. • 整数值。

• ENUMERATED values. • 枚举值。

• Length determinants of strings. • 字符串长度的决定因素。

• Character string values. • 字符字符串值。

• Encoding of SEQUENCE and SET. • SEQUENCE 和 SET 的编码处理。

• Encoding of SEQUENCE OF and SET OF. • “SEQUENCE OF”和“SET OF”的编码方式。

• Encoding of REAL and OBJECT IDENTIFIER. • 对 REAL 和 OBJECT IDENTIFIER 进行编码处理。

• Encoding of the remaining types (GeneralizedTime, UTCTime, ObjectDescriptor, and types defined using the "ValueSet" notation). • 对其余类型进行编码（包括 GeneralizedTime、UTCTime、ObjectDescriptor，以及使用“ValueSet”表示法定义的类型）。

Most of these later topics are covered by simply giving examples, as they follow the general approaches that are fully covered in the first part of this chapter. 这些后续主题大多通过举例来讲解，因为它们遵循的是本章第一部分中已经介绍过的总体方法。

## 1 Introduction 1 引言

The principles underlying PER encodings (no encoding of tags, use of a bit-map for OPTIONAL, use of a CHOICE index, and the sorting of SET elements and CHOICE alternatives into tag order have already been introduced in Chapter 1 of this section. In this chapter we complete the detail. 在 PER 编码中遵循的一些原则已经在本章节的第 1 章中介绍过了：不对标签进行编码；可以使用位图来表示可选项；使用 CHOICE 索引；还将 SET 元素和 CHOICE 选项按照标签顺序进行排序。在本章中，我们将对这些原则进行更详细的说明。

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/54379e17-c034-430b-894c-f77661f731e5/ee8b1a4d5529c0803c7975913faf64f1722b11c5d0fe8fc5deb12bc40b98ca01.jpg)

The latter part of this chapter provides examples of all the encodings, and gives some further explanation where needed. 这一章的后面部分提供了所有编码方式的示例，并在需要的地方提供了进一步的说明。

This chapter is not totally free-standing. It is assumed that the reader will have read the relevant parts of Section III, Chapter 1 before starting on this chapter, but there are also a number of cases where PER codings are the same as BER (or more usually CER/DER) encodings, and in such cases reference is made to Section III, Chapter 2. 这一章节并不是完全独立存在的。假设读者在开始阅读这一章节之前已经阅读了第三章第一节的相关内容。不过，也有一些情况中，PER 编码与 BER 编码（或更常见的 CER/DER 编码）是相同的。在这种情况下，会引用第三章第二节的内容作为参考。

The bit-numbering and diagram convention (first octet of the encoding shown on the left, bits numbered with 8 as the most significant and shown on the left) that was used for BER is used here also. 在 BER 编码中使用的位编号和图表格式（左侧显示的编码中，最高位的 8 位被标记为最重要的位，并且按照从左到右的顺序进行编号）在这里也被采用。

However, with PER there are sometimes padding bits inserted to produce octet alignment at the start of some field. Where padding bits may have to be inserted (depending on the current bit position within an octet, there may be anything from zero to seven padding bits), a capital "P" is used at the start of the field in the examples given in this chapter. 不过，在使用 PER 的情况下，有时会插入一些填充位来确保某些字段在开头时具有相同的八位长度。根据八位中当前位的不同情况，可能需要插入 0 到 7 个填充位。在本章给出的示例中，这些字段的开头都使用了大写的“P”来表示填充位。

## 2 Structure of a PER encoding 2. PER 编码的结构

## 2.1 General form 2.1 一般形式

You will already know that PER does not necessarily encode into fields that are a multiple of eight bits, but the BER concept of encodings of (for example) SEQUENCE, being some up-front header followed by the complete encodings of each element also applies to PER. 你们已经知道，PER 并不一定需要编码为 8 位的倍数。不过，对于 SEQUENCE 这种编码方式来说，BER 概念仍然适用——即先是一个头部信息，然后是每个元素的完整编码。这一规则同样适用于 PER。

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/54379e17-c034-430b-894c-f77661f731e5/ae9d36befc90d603329da1ffa43632eaeb47e8ce401d24640dff5510e7738552.jpg)

In the case of PER, the "header" is called the preamble, but is present for SEQUENCE only if there are optional elements, otherwise it is null and we have simply the encoding of each element. 在 PER 的情况下，所谓的“头部”被称为前导段。不过，只有当存在可选元素时，该头部才会出现在 SEQUENCE 中；否则，该头部就为空，我们看到的就只是每个元素的编码而已。

There is also a difference in the "L" part of an encoding from BER. Once again, it can frequently be missing (whenever the length is known in advance in fact), but also the terminology changes to "length determinant". This change was made because whilst the length octets of BER are always a count of octets (apart from the indefinite form), in PER the length determinant encodes a value that may be: 在编码的“L”部分方面，BER 与 PER 也有差异。同样，这个部分往往会被省略（实际上，当长度可以预先知道时，这个部分通常是存在的）。此外，术语也发生了改变，变成了“长度决定器”。这种改变是因为，在 BER 中，长度以八位元计数来表示；而在 PER 中，长度决定器则编码一个数值，该数值可以是：

• a count of octets (as in BER); or • 以八位组为单位进行计数（如 BER 格式）；或者

• a count of bits (used for the length of an unconstrained BIT STRING value); or • 位数的统计（用于确定无约束的 BIT 字符串的值的长度）；或者

• a count of iterations (used to determine the length of a SEQUENCE OF or SET OF value). • 迭代次数（用于确定“序列”或“集合”的长度）。

It is also the case that in PER the length determinant is not necessarily an integral multiple of eight bits. 此外，在 PER 中，长度的决定因素并不一定是 8 位整数的倍数。

The precise form and encoding of a length determinant is described later. 长度决定因子的具体形式与编码方式将在后面详细描述。

Each of the three pieces of encoding encode into what is called a bit-field. The length of this bitfield is either statically determinable from the type definition, or that part of the encoding will be preceded by a length determinant encoding. The term "bit-field" is used to imply that the field is not necessarily an integral multiple of eight bits, nor in general is the field required to start on an octet boundary. 这三部分编码中的每一部分都被编码成一种称为“位字段”的结构。这种位字段的长度要么可以从类型定义中直接确定，要么会在编码过程中有一个用于确定长度的部分。所谓“位字段”，意味着该字段不一定是 8 位的整数倍，而且通常也不要求该字段必须以 8 位字节的边界开始。

As we proceed through the encoding of a value of a large and complex structured type, we generate a succession of bit-fields. At the end of the encoding, these are simply placed end-to-end (in order), ignoring octet boundaries, to produce the complete encoding of the value. 在对大型且结构复杂的数值进行编码的过程中，我们会生成一系列位字段。在编码完成后，这些位字段会被按顺序连接在一起，忽略字节边界，从而得出该数值的完整编码结果。

## 2.2 Partial octet alignment and PER variants 2.2 部分八位组对齐方式及 PER 的多种变体

There are a couple of further wrinkles on the overall structure, of which this is the first! 在整个结构中还有几处需要进一步解决的问题，而这只是其中的第一个问题而已！

There are some fields where the designers of PER felt that it would be more sensible to ensure that the field started on an octet boundary (for simplicity of implementation and minimisation of CPU cycles). Fields to which this applies can be identified from the type definition (and do not depend on the particular value being transmitted). Such cases are said to encode into octet-aligned bitfields. In the final concatenation of bit-fields, padding bits are inserted as necessary before any octet-aligned bit-fields to ensure that they start at a multiple of eight bits from the start of the entire encoding of the outer-level type - the message, or "protocol data unit" (PDU). 在一些字段中，PER 的设计者认为，为了简化实现过程并减少 CPU 占用时间，让字段从八位字的边界开始是一个更合理的做法。这些字段可以通过类型定义来识别（它们并不依赖于实际传输的具体值）。这种编码方式可以被看作是将字段编码为按八位字排列的位字段。在最终合并位字段时，会在每个按八位字排列的位字段之前插入填充位，以确保这些字段从整个外层类型编码的起始位置开始，其长度都是 8 的倍数——也就是消息或“协议数据单元”。

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/54379e17-c034-430b-894c-f77661f731e5/465ebab73fa8046aab0ecbfbb8c52cf01a4dada2ea08b796f58258ee32df4109.jpg)

There are some applications (air traffic control is one), where the padding bits are not wanted - minimising bandwidth is considered the primary need. There are therefore formally two variants of PER: 有一些应用场景中并不需要使用填充位——例如空中交通管制领域，此时最小化带宽需求才是首要考虑的问题。因此，PER 有两种正式的实现方式：

• the ALIGNED variant (with padding bits); and • 对齐版本（包含填充位）；以及

• the UNALIGNED variant (with no padding bits, and with some other bandwidth reduction features that will be described later). • 非平行排列的版本（没有填充位，同时还有一些其他的数据带宽降低功能，这些功能将在后面详细说明）。

## 2.3 Canonical encodings 2.3 标准编码方式

BASIC-PER is largely canonical, but there are some types (SET OF, some character string types, time types, and some occurrences of DEFAULT) where being 100% canonical is "expensive". So BASIC-PER (being pragmatic!) has non-canonical encodings for these types. CANONICAL-PER is fully canonical. BASIC-PER 基本上属于标准编码方式，不过有一些类型（如 SET OF、某些字符字符串类型、时间类型，以及 DEFAULT 的一些用法）并非完全符合标准编码规则。因此，BASIC-PER 为了实用起见，为这些类型提供了非标准的编码方式。而 CANONICAL-PER 则完全遵循标准编码规则。

This is another area that gives rise to further encoding rules within the general PER family. 这是另一个会催生更多编码规则的领域，属于通用的 PER 家族的一部分。

Notice that whilst BER has many encoder's options, leading to the production of specifications for CER and DER, PER avoids options in the basic encoding, and looks at first sight to be canonical. (It is certainly far more canonical than BER!) 需要注意的是，虽然 BER 提供了许多编码选项，从而产生了 CER 和 DER 的规范，但 PER 却避开了这些复杂的编码选项，看起来更像是一种规范化的编码方式。（实际上，PER 确实比 BER 更规范化！）

However, to produce truly canonical encodings (as with BER) requires a sort of SET OF elements, and adds complexity to encoding character string types like GeneralString and GraphicString. Socalled BASIC-PER (with both ALIGNED and UNALIGNED variants) does not do this, and produces canonical encodings ONLY if these types are not involved. CANONICAL-PER (with an ALIGNED and an UNALIGNED variant) is fully canonical, and introduces sorting of SET-OF and special rules for GeneralString etc. The actual rules are exactly the same (and are specified by reference) as those used to turn BER into CER. 不过，要生成真正符合规范的编码方式（就像 BER 那样），就需要一组特定的元素，这会增加对像 GeneralString 和 GraphicString 这样的字符字符串类型进行编码的复杂性。所谓的 BASIC-PER 编码方式（包括 ALIGNED 和 UNALIGNED 两种变体）并不具备这种特性，它只能在这些类型不出现的情况下生成规范化的编码。而 CANONICAL-PER 编码方式（也有 ALIGNED 和 UNALIGNED 两种变体）则完全符合规范，它还会对 SET-OF 类型进行排序，并对 GeneralString 等类型引入特殊的规则。实际上，其规则与用于将 BER 转换为 CER 所使用的规则完全相同（并且是通过引用来指定的）。

## 2.4 The outer level complete encoding 2.4 外部层的完整编码

Another slight complication arises at the outer level of a complete encoding (the total message being sent down the line). (This is a pretty detailed point, and unless you are heavily involved in producing encodings you can skip to the next clause). 在完整编码的外层阶段，还会出现另一个小问题（即整个消息是如何被传输出去的）。这一点相当重要，不过如果你并不太熟悉编码的生成过程，那么可以直接跳到下一节内容。

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/54379e17-c034-430b-894c-f77661f731e5/80ea7e64fd8f84c231ad6676c8730af3ec302d2b010e60a8924338f316fe5b65.jpg)

There are a few theoretical cases where a message may encode into zero bits with PER. This would occur, for example, with an outer-level type of NULL, or of a SET OF constrained to have zero iterations (both are highly unlikely to occur in practice, but ...!). 在某些理论情况下，一个消息可以编码为零比特，这种情况会在某些特定情况下发生。例如，当使用外部级别的 NULL 类型时，或者当某个集合被限制为只有零次迭代时，就有可能出现这种情况（不过，实际上这种情况很少发生……）。

The problem here is that if the way a carrier protocol is used allows multiple values of that type to be placed into the carrier, a multiple of zero bits is still zero bits, and the receiver would not know how many values had been sent, even with complete knowledge of the type definition! 这里的问题在于，如果载体协议的使用方式允许将多个该类型的数值存入载体中，那么多个零位仍然会被表示为零位。这样一来，即使接收方完全了解类型的定义，也无法知道究竟发送了几个数值。

So PER requires that if the complete encoding of the outer-level type is zero bits (which would mean that the outer-level type contains only one abstract value), then a single one-bit is used for that encoding instead. 因此，PER 规定，如果外层类型的完整编码为 0 位（这意味着外层类型只包含一个抽象值），那么就可以使用 1 位来编码该类型。

And finally, recognising that carrier protocols often provide "buckets" that are only able to contain multiples of eight bits, PER specifies that the complete encoding should always be padded at the end with zero bits to produce an integral multiple of eight bits. (Again, this is to ensure that there is no doubt at the decoding end about the number of values that have been encoded into the octet bucket that the carrier uses to convey the PER encoding from encoder to decoder). 最后，由于载波协议通常只提供能够存储 8 位倍数的比特数，因此 PER 规定在编码过程中，末尾必须填充零位比特，以确保解码端能够明确知道每个八位字节中编码了哪些值。这一点非常重要，因为它可以避免解码过程中出现任何误解。

So the minimum size of a complete outer-level PER encoding is one octet, and it is always a multiple of eight bits, but individual component parts are generally not a multiple of eight bits, and may be zero bits. 因此，完整的外部级别 PER 编码的最小尺寸为一个八位元，并且总是以八位元为倍数进行表示。不过，各个组成部分通常并不以八位元为倍数，有些组件甚至可以为零位元。

## 3 Encoding values of extensible types 3. 可扩展类型的编码值

PER has a uniform approach to extensibility. Refer in what follows to Figure III-15 for an illustration of the encoding of extensible INTEGER and string values, to Figure III-16 for an illustration of the encoding of extensible SET and SEQUENCE values, to Figure III-17 for an illustration of the encoding of extensible CHOICE values, and to Figure III-18 for an illustration of the encoding of extensible ENUMERATED values. PER 对可扩展性的处理采用了统一的方法。关于可扩展整数和字符串值的编码方式，请参考图 III-15；关于可扩展集合和序列值的编码方式，请参考图 III-16；关于可扩展选择值的编码方式，请参考图 III-17；关于可扩展枚举值的编码方式，请参考图 III-18。

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/54379e17-c034-430b-894c-f77661f731e5/cd0337690a49f4bd1cc6dc2c001de1c24ad78970da5c07aa313a6d5c76a7ef88.jpg)

```txt
Either:
0
followed by:
An encoding of a value of the type, which is the same as that for the type without an extensibility marker or extensions.
Or:
1
followed by:
An encoding for a value of the extensible type which is outside the root, which is the same as that for values of the unconstrained type.
Figure III-15: Extensible constrained INTEGER or string encodings 
```

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/54379e17-c034-430b-894c-f77661f731e5/9a8cb650bed81ccd615c7b70264aad07b83d7c97eb33a161a62e722483fe18d9.jpg)

Any type (a constrained INTEGER, a constrained string, a SEQUENCE, a SET, a CHOICE, or an ENUMERATED) that has an extensibility marker (the ellipsis) in its type definition or in a PERvisible constraint has a value of that type encoded as follows: 任何具有可扩展性的类型（包括受限整数、受限字符串、序列、集合、选择或枚举类型），在其类型定义或 PER 可见约束中带有省略号表示的可扩展性标记时，其类型值将按照以下方式进行编码：

```txt
Either:
0
followed by:
An encoding of the choice index (identifying an alternative which is present in the root), which is the same as that for the type without an extensibility marker.
followed by:
The encoding of a value of the chosen alternative within the root.
Or:
1
followed by:
A different encoding for the choice index, (identifying an alternative outside the root).
followed by:
The encoding of a value of the chosen alternative that is outside the root.
Figure III-17: Extensible CHOICE encodings 
```

• There is a one-bit-long bit-field encoded up-front - the extensions bit. • 有一个长度为 1 位的数据字段被预先编码好了——那就是扩展位。

The extensions bit is set to zero if the value being encoded is in the root (one of the original INTEGER or ENUMERATED values, or a SET or SEQUENCE value in which all extension additions - if any - are absent). 如果所编码的值属于根节点（即原始的 INTEGER 或 ENUMERATED 类型之一，或者是一个 SET 或 SEQUENCE 类型，且其中没有包含任何扩展属性），那么这些扩展属性对应的字段值将被设置为零。

• The extensions bit is set to one otherwise (values outside the root). • 如果其他值不在根节点范围内，则“扩展”选项会被设置为 1。

NOTE — Only implementations of versions greater than 1 will set the bit to one, but all implementations may encode a root value, and hence set the extensions bit to zero. 注意：只有那些支持版本高于 1 的实现才会将该位设置为 1。不过，所有实现都可能会编码一个根值，因此会将扩展位设置为 0。

```txt
Either:
0
followed by:
An encoding of a value of the type, which is the same as that for the type without an extensibility marker or extensions.
Or:
1
followed by:
An encoding for a value of the extensible type which is outside the root.
Figure III-18: Extensible ENUMERATED type encodings 
```

• If the "extensions bit" is set to zero, what follows is exactly the same encoding (for all types that can be marked extensible) as if the extension marker (and all extensions) was absent. • 如果“扩展标志”被设置为零，那么对于所有可以被标记为可扩展的类型来说，后续的编码方式将完全与没有使用扩展标志的情况相同。

If the "extensions bit" is set to one, the following encoding is sometimes the same as for the unconstrained type, but sometimes different, as follows: 如果“扩展位”被设置为 1，那么接下来的编码方式有时会与无约束类型相同，但有时也会有所不同，具体如下：

If the "extensions bit" is set to one when encoding an extensible INTEGER or extensible string, what follows is an encoding which is the same as for a value of the unconstrained type. 如果在对可扩展的整数字段或可扩展字符串进行编码时，将“扩展位”设置为 1，那么后续的编码方式就与对无约束类型的值进行编码时相同。

If the "extensions bit" is set to one when encoding a SEQUENCE or SET value, what follows is the encoding of the elements that are in the root, with a special encoding (see 15.2) inserted at the insertion point to carry the values of elements outside the root (and to identify their presence). 如果在编码一个序列或集合值时将“扩展位”设置为 1，那么接下来就是对根节点中各个元素的编码。在插入点处会插入一种特殊的编码方式（参见 15.2 节），用来标记根节点之外的一些元素的值，并表明这些元素的存在。

If the "extensions bit" is set to one when encoding a CHOICE value, what follows is a special encoding of the choice index (recognising that although theoretically unbounded, the value will usually be small), followed by an encoding of the chosen alternative. (See 8.2 for the encoding of a "normally small whole number"). 在编码 CHOICE 值时，如果“扩展位”被设置为 1，那么接下来就是对选择指数的特殊编码（需要注意的是，虽然理论上这个值可以是无限的，但实际上通常都会很小）。之后才是所选选项的编码。（有关“通常较小的整数”的编码方式，请参见 8.2 节。）

• If the "extensions bit" is set to one when encoding an ENUMERATED value, the same encoding is used as for the choice index, for again the value is theoretically unbounded, but in practice will usually be small. • 当对枚举值进行编码时，如果“扩展位”被设置为 1，那么使用的编码方式与选择索引时相同。这样一来，该值理论上可以是无限大的，但实际上通常都会比较小。

It will be seen from the above that the only cost in version 1 of including an extensibility marker is 1 bit (possibly causing the insertion of up to seven padding bits after it). We will see later that if the type actually has extensions, and values outside the root are encoded, we generally get an additional overhead of a length field for such values. 从上述内容可以看出，在版本 1 中，引入可扩展标记的唯一成本就是 1 比特的开销（这可能会导致在标记之后额外添加多达 7 个填充比特）。稍后我们会了解到，如果类型实际上包含扩展功能，并且需要编码那些位于根结构之外的值，那么通常会额外需要一个用于这些值的长度字段。

The encoding for values of extensible types that lie outside the root is described below after the description of the encoding for types that were not defined to be extensible (and for values of extensible types that are within the root). 对于那些不属于根类型的可扩展类型的值的编码方式，将在下文中进行描述。而对于那些被定义为不可扩展类型的类型的值以及属于根范围内的可扩展类型的值的编码方式，则已在前面进行了说明。

It will be clear from the above description that encoders and decoders must agree on whether a type is extensible or not, and if so on precisely which abstract values are in the root. Where a type has an ellipsis as a direct part of the type definition - SET, SEQUENCE, CHOICE, ENUMERATED, there is little problem. But where a type such as integer or a character string is constrained with a constraint that contains an ellipsis, the situation is (perhaps surprisingly!) not so clear cut, and the type may well be declared to be not extensible for PER-encodings, despite the clear presence of an ellipsis! This area is discussed at the end of the discussion on PER-visible constraints. 从上述描述中可以清楚地看出，编码器和解码器必须就某个类型是否可扩展达成一致。如果类型具有省略号作为类型定义的一部分——比如 SET、SEQUENCE、CHOICE、ENUMERATED 等类型，那么问题并不复杂。但是，当像整数或字符字符串这样的类型被某种包含省略号的约束条件所限制时，情况就变得相当复杂了。在这种情况下，尽管类型定义中明确包含了省略号，但该类型仍可能被声明为不可扩展，以适应 PER 编码方式。这一领域在关于 PER 可见约束的讨论的最后部分进行了详细的探讨。

## 4 PER-visible constraints 4 个可见的约束条件

## 4.1 The concept 4.1 概念

Crucial to understanding PER encodings is the concept of PER-visible constraints. These are (subtype) constraints which, if present, affect the encoding of the parent type. 理解 PER 编码的关键在于 PER 可见约束的概念。这些属于子类型约束，如果存在这些约束，就会影响到父类型的编码方式。

The most important PER-visible constraints are those placed on the INTEGER type and on the lengths of strings (or on iteration counts for SET OF and SEQUENCE OF). There are also constraints on the alphabet of some character string types that are PERvisible (see Clause 6), and can reduce the number of bits per character for these character strings. 对 PER 可见性有约束的最重要条件，是那些对 INTEGER 类型以及字符串长度（或 SET OF 和 SEQUENCE OF 结构中的迭代次数）所施加的约束。此外，某些字符字符串类型的字母表也存在 PER 可见性的约束（详见第 6 条），这些约束会减少这些字符字符串每个字符所需的位数。

Constraints that are PER-visible in the above cases are quite widely-defined. They may be applied "a bit at a time", through repeated use of type references, or they may be 在上述情况下，那些在页面上可见的约束条件有着非常广泛的定义。这些约束条件可以逐步被应用，通过反复使用类型引用来实现，或者也可以一次性应用。

PER-visible constraints are constraints that PER uses to produce less verbose encodings - for example - INTEGER (0..7) encodes into just three bits because the (0..7) constraint is PER-visible. BER ignores all constraints, and hence always needs a length field. PER takes a pragmatic view and uses constraints that are "easily" used and produce important bandwidth gains, but ignores other more complex constraints. PER 可见约束是指 PER 用来生成更简洁编码方式的约束条件。例如，INTEGER(0..7)这种编码方式仅用三个比特就能表示，因为(0..7)这个约束是 PER 可见的。而 BER 则完全忽略所有约束条件，因此总是需要长度字段来表示数据长度。PER 采取务实的态度，只使用那些“易于使用”且能带来显著带宽节省的约束条件，而忽略那些更复杂的约束条件。

applied through the use of parameterisation. Or they may be extremely complicated subtype specifications involving included subtype constraints, intersections and unions. 它们是通过参数化来应用的。或者，这些规范可能是非常复杂的子类型定义，包含有子类型的约束条件、交集和并集等元素。

There are two comments to make on this: first, most specifications are pretty simple, so handcoders don't have to do too much work to calculate the actual constraint in the real world; second, an ASN.1 compiler has no problems in resolving such expressions of arbitrary generality down to a precise record of the permitted values for the integer type, the length of the string, etc. 关于这一点，有两点需要指出：首先，大多数规范都相当简单，因此手工编码者不需要花费太多精力来计算现实世界中的实际约束条件；其次，ASN.1 编译器在解析这种具有任意通用性的表达式时毫无问题，因为它能够精确地确定整数类型、字符串长度等允许的值范围。

## 4.2 The effect of variable parameters 4.2 可变参数的影响

One major exception to PER-visibility is if, in trying to determine the actual constraint, a variable parameter (a parameter that still does not have a value when the abstract syntax is defined) is textually referenced in the resolution of the actual constraint, then the constraint ceases to be PER- PER-可见性的一个主要例外情况是：在确定实际约束条件时，如果某个变量参数（即在抽象语法定义时尚未有值的参数）在具体的约束条件描述中被明确提及，那么这种约束条件就不再属于 PER-可见性范畴了。

Presence of a variable parameter in a constraint means that PER totally ignores that entire constraint. 在约束条件中存在一个可变参数意味着 PER 完全忽略了整个约束条件。

visible, and would encode as if that constraint were not present. 可见的，并且会像没有这个限制一样进行编码。

This is the first of several cases where a type which is formally extensible encodes as if it was not extensible. In this case, it contains an ellipsis in a constraint that is not PER-visible, so (assuming no other constraints have been applied) it will encode as not extensible and not constrained. 这是多个类似案例中的第一个例子：一种被定义为可以扩展的类型，实际上却表现得并不具备扩展性。在这个案例中，该类型在一个约束条件中使用了省略号，而这样的省略是肉眼无法辨认的。因此（假设没有其他约束条件被应用），该类型会被编码为不具备扩展性和约束性。

Variable parameters are still not heavily used, so this is not too big an issue, but the term textually above refers to the possibility of constructing union and intersection expressions which appear to use the value of such a parameter, but where the actual result of the expression evaluation proves to be the same no matter what value the variable parameter might have. Even if the parameter does not affect the result, its textual presence kicks the constraint out of court. This was done to ease implementation efforts for compilers, and to avoid possible errors in hand-encoding. 可变参数目前仍未被广泛使用，因此这并不算什么问题。不过，上述术语实际上指的是那种可以构建 union 和 intersection 表达式的情况，这些表达式似乎会利用某个参数的值，但实际上无论该参数取何值，表达式的计算结果都是相同的。即使该参数本身并不影响计算结果，其存在的概念性描述也足以使这种约束失效。这样做是为了简化编译器的实现工作，同时避免在进行手工编码时可能出现的错误。

## 4.3 Character strings with variable length encodings 4.3 具有可变长度编码的字符字符串

Another major exception to PER-visibility that should be noted is that a constraint on the length of a character string applies to the number of (abstract) characters that can appear in the string. If the encoding is something like UTF8 (or GeneralString), where the number of octets needed to encode each character is different for different characters (and in the case of GeneralString can depend on encoder options), the length constraint is not much help at the encoding level - a length field is still needed in order to find the end of the encoding. 另一个需要注意的 PER 可见性方面的例外是：字符字符串的长度存在一个限制，即字符串中出现的（抽象）字符的数量受到了限制。如果编码方式类似于 UTF8（或 GeneralString），那么每个字符所需的八位元数量会有所不同（而在 GeneralString 的情况下，这一数值还可能取决于编码器的设置）。在这种情况下，长度限制在编码层面并没有太大帮助——仍然需要一个长度字段来标识字符编码的结束位置。

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/54379e17-c034-430b-894c-f77661f731e5/72b9cab3815afca5bb11939fe92c371169ee0d4493e7365806e6d11ff9daf052.jpg)

(The above statement is not strictly true. If the itty-gritty details of an encoding scheme such as UTF8 are fully understood then knowledge of the number of abstract characters being encoded is in fact sufficient to find the end of the encoding, but PER wants a decoder to be able to find the end of the encoding without resorting to such detailed analysis.) （上述陈述并不完全正确。虽然如果完全理解诸如 UTF8 这样的编码方案的细节，那么仅仅知道被编码的抽象字符的数量就足以确定编码的结束位置。不过，PER 希望解码器能够在不进行如此详细分析的情况下找到编码的结束点。）

So character set types that have a fixed number of octets for each abstract character are called known multiplier types, and length constraints on such types are PER-visible (and will give rise to reduced or eliminated length encodings), but for character string types that are not "known multiplier types", the constraints are not PER-visible (do not affect the encoding of values of the type), and any extension markers in these constraints are ignored for the purpose of PER encodings. 那些每个抽象字符都有固定数量八位元的字符集类型被称为“已知乘数类型”。对于这类类型，长度限制是严格可见的（这通常会导致编码长度减少或消除）。然而，对于那些不属于“已知乘数类型”的字符串类型来说，这些限制就不具有可见性了（它们不会影响该类型值的编码）。在 PER 编码过程中，这些限制中的任何扩展标记都会被忽略。

## 4.4 Now let's get complicated! 4.4 现在让我们来复杂一些吧！

This book is called "ASN.1 Complete", so we had better explore a bit more about PER-visibility and about extensibility. 这本书的标题是《ASN.1 完整指南》，因此我们有必要进一步了解 PER 可见性以及可扩展性相关的内容。

First, we note that there are a number of different sorts of subtype constraint which may be used alone, but which in the general case combine together using EXCEPT, INTERSECTION, and UNION. We call the basic building blocks component constraints, and the complete constraint the outer-level constraint. Both component constraints and outer-level constraints may contain an ellipsis! 首先，我们注意到存在多种不同类型的子类型约束，这些约束可以单独使用，但在一般情况下，它们会通过 EXCEPT、INTERSECTION 和 UNION 等操作符进行组合使用。我们将构成这些约束的基本单元称为“组件约束”，而完整的约束则被称为“外层约束”。无论是组件约束还是外层约束，都可以包含省略号来表示某些信息。

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/54379e17-c034-430b-894c-f77661f731e5/d191c2a7a95bb9b5db1d8cfcc4a9f3e733384b51e2ce1534244569a68f6d671a.jpg)

Whether a component constraint is PER-visible will depend in general on the sort of component constraint it is, and on the type being constrained. Figure III-19 gives a list. 一个组件约束是否可见，通常取决于该约束本身的类型以及被约束的具体内容。图 III-19 提供了一个列表，其中列出了各种组件约束的可见性情况。

<table><tbody><tr><td data-imt-p="1">Variable constraint 变量约束</td><td data-imt-p="1">Never visible 永远不可见</td></tr><tr><td data-imt-p="1">Single value constraint 单一值约束</td><td data-imt-p="1">Visible for INTEGER only 仅适用于整数类型的数据可见</td></tr><tr><td data-imt-p="1">Contained subtype constraint 包含的子类型约束</td><td data-imt-p="1">Always visible 始终可见</td></tr><tr><td data-imt-p="1">Value range 价值范围</td><td data-imt-p="1">Visible for INTEGER only and in an alphabet constraint on a known-multiplier character string type 仅对 INTEGER 类型可见，且必须位于一个以字母为字符集的约束条件所限定的已知乘数字符串类型中。</td></tr><tr><td data-imt-p="1">Size constraint 尺寸限制</td><td data-imt-p="1">Visible for OCTET STRING, SET and SEQUENCE OF, and known-multiplier character string types 适用于 OCTET STRING、SET 和 SEQUENCE OF 类型，以及已知乘性字符字符串类型</td></tr><tr><td data-imt-p="1">Permitted alphabet 允许使用的字母表</td><td data-imt-p="1">Visible for known-multiplier character string types 适用于已知乘数字符字符串类型</td></tr><tr><td data-imt-p="1">Inner subtyping 内部类型划分</td><td data-imt-p="1">Never visible 永远不可见</td></tr><tr><td colspan="2" data-imt-p="1">Figure III-19: PER-visibility of constraints 图 III-19：可感知性的约束条件</td></tr></tbody></table>

Two important points to note from Figure III-19 are that a single value constraint is only visible if applied to INTEGER, and a contained subtype constraint is always visible. This can give rise to some distinctly non-obvious effects in relation to known-multiplier character string types such as IA5String! Suppose we have: 从图 III-19 中可以注意到两个重要点：首先，只有当某个值约束应用于 INTEGER 类型时，它才会显示出来；其次，包含的子类型约束总是会显示出来。这一点可能会带来一些不太明显的影响，尤其是在处理像 IA5String!这样的已知乘数字符串类型时。假设我们有如下情况：

Subtype ::= IA5String ("abcd" UNION "abc" UNION SIZE(2)) MyString ::= IA5String (Subtype INTERSECTION SIZE(3)) 类型 ::= IA5String("abcd" UNION "abc" UNION SIZE(2)) 变量名 ::= IA5String(类型 INTERSECTION SIZE(3))

In Mystring, all the component constraints are PER-visible, and we expect to be able to work out the outer-level constraint. In Subtype, the first two component constraints are not PER-visible but the third is. What is the effect on Subtype and on MyString? This question, and a number of related ones, produced some lengthy discussion within the ASN.1 group with "keep it simple" colliding to some extent with "keep it general and intuitive". 在 MyString 中，所有组件的约束都是“PER 可见”的，我们预计能够计算出外部级别的约束。而在 Subtype 中，前两个组件的约束并非“PER 可见”，但第三个约束却是如此。这对 Subtype 和 MyString 有什么影响呢？这个问题以及一些相关的问题在 ASN1 小组中引发了一些长时间的讨论。在讨论过程中，“保持简单性”与“保持通用性和直观性”这两个原则在一定程度上发生了冲突。

The first important rule is that if any component constraint is not PER-visible, then the entire outerlevel constraint is declared to be not PER-visible, and will not affect the encoding. Notice here that if there is an ellipsis in either a component or in the outerlevel constraint, because we are ignoring the entire constraint, the type is NOT encoded as an extensible type. So Subtype above is treated by PER as unconstrained, and contributes all abstract values of an unconstrained IA5String in the set arithmetic for MyString. 第一个重要的规则是，如果任何组件约束都不是“PER-可见”的，那么整个外部级别约束也会被声明为“非 PER-可见”，从而不会影响编码过程。注意，如果组件或外部级别约束中出现省略号，因为整个约束被忽略了，所以该类型的类型就不会被编码为可扩展类型。因此，上述子类型被视為无约束的，其在 MyString 的集合运算中贡献的所有抽象值都属于无约束的 IA5String 类型。

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/54379e17-c034-430b-894c-f77661f731e5/31aca601be57ebe68e52a4e7a124cac876173f9170d5a73a93a51a0f2e9bad36.jpg)

For MyString, all component constraints are PER-visible, so the SIZE(3) applies, and values of the string encode as if it contained all possible abstract values of length 3. 对于 MyString 来说，所有组件的约束都是“完全可见”的，因此 SIZE(3)这个参数仍然适用。字符串的值会被编码为包含长度为 3 的所有可能抽象值。

There is one additional rule, related to the use of the ellipsis. When performing set arithmetic to determine whether a PER-encoding is extensible and what values are in the root, all ellipsis marks (and any actual additions) in a component constraint (or any of the component constraints of that component - such as Subtype above) are ignored. A constrained type is extensible for PERencodings if and only if an ellipsis appears at the outer-level of a constraint, all of whose © OS, 31 May 1999 287 component constraints are PER-visible. This is simple, but perhaps not quite what you might have expected. 还有一条与省略号使用相关的规则。在执行集合运算以确定某个 PER 编码是否可扩展时，该编码中出现的所有省略号标记（以及任何实际添加的内容）都会被忽略。一个受约束的类型只有在其所有约束条件的外层级别出现省略号时，才被认为是可扩展的。© OS，1999 年 5 月 31 日，第 287 页。这个规则很简单，但可能并不像你预期的那样。

Now consider a Version 2 specification, where the constraint in Version 1 was PER-visible, but in Version 2 things (such as a single value constraint) are added that would normally wreck PER-visibility. This does not (and cannot be allowed to) affect PERvisibility of the original Version 1 constraint, otherwise interworking would be prejudiced. So it is only those parts of a constraint that appear in the root that affect PER-visibility (and that affect the way a value is encoded). 现在考虑一下版本 2 的规范。在版本 1 中，约束条件是“可看见”，但在版本 2 中，出现了一些额外的约束条件（比如某个值约束），这些约束条件通常会破坏“可看见”的特性。不过，这些新增的约束条件并不应该影响版本 1 中原有约束条件的“可看见”特性，否则就会导致规范之间的互操作性问题。因此，只有那些出现在根节点中的约束条件部分才会影响“可看见”的特性，以及值编码方式。

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/54379e17-c034-430b-894c-f77661f731e5/94f939b2285d22840eaefb6990ace134cbd1150f942eb68da2bc2929108ff02c.jpg)

But as someone once said "Such contorted constraint specifications only ever appear in discussions within the ASN.1 group, never in real user specifications." And they are right! 但正如有人曾经说的：“这种扭曲的约束规范只出现在 ASN 社区的讨论中，在真正的用户规范中根本不存在。”他们是对的！

## 5 Encoding INTEGERs - preparatory discussion 5. 整数编码——预备性讨论

What matters for a PER-encoding of the INTEGER type (and of the lengths of known-multiplier 在 INTEGER 类型的编码中，以及对于已知乘数长度的计算来说，真正重要的因素是……

character strings) is not the actual values, but the range of values permitted by PER-visible constraints. It is the largest and smallest value that matter. An integer constrained to have only the two values 0 and 7 will still encode in three bits, not two. What matters is the range, not the number of values. 字符字符串中的值并不是实际的值，而是指由 PER 可见约束所允许的值范围。真正重要的其实是这个范围的最大值和最小值。一个被限制只能取 0 和 7 这两个值的整数，仍然可以用 3 位来表示，而不是 2 位。重要的是这个范围，而不是值的个数。

<table><tbody><tr><td data-imt-p="1">It's the largest and smallest values that matter. Gaps in between do not affect the encoding. 重要的是最大值和最小值之间的差异。中间的差值并不会影响编码结果。</td></tr></tbody></table>

Figure III-20 illustrates some simple constraints that are PER-visible, and the values that PER assumes need encoding. 图 III-20 展示了一些简单的约束条件，这些约束是 PER 可见的；而 PER 所采用的值则需要经过编码处理。

For any integer that has a lower bound (and similarly for the lengths of strings), what is encoded in the PER encoding is the offset from the lower bound. So the encoding of values of SET3 in Figure III-20 would use just 2 bits. 对于任何具有下限的整数（字符串的长度也是如此），PER 编码方式所表示的是与下限之间的差值。因此，在图 III-20 中，SET3 值的编码仅需要使用 2 位二进制数即可。

<table><tbody><tr><td data-imt-p="1">Type definition 类型定义</td><td data-imt-p="1">Values assumed to need encoding 那些被认为需要编码的价值观</td></tr><tr><td data-imt-p="1">INTEGER (0..7) 整数类型（0~7）</td><td data-imt-p="1">0 to 7 0 到 7</td></tr><tr><td data-imt-p="1">INTEGER (0 UNION 7) 整数类型 (0 联合 7)</td><td data-imt-p="1">0 to 7 0 到 7</td></tr><tr><td data-imt-p="1">SET1 ::= INTEGER (15..31) SET1 ::= 整数 (15..31)</td><td data-imt-p="1">15 to 31 15 到 31</td></tr><tr><td data-imt-p="1">SET2 ::= INTEGER (0..18) SET2 ::= 整数(0..18)</td><td data-imt-p="1">0 to 18 0 到 18</td></tr><tr><td data-imt-p="1">SET3 ::= INTEGER (SET1 INTERSECTION SET2) SET3 ::= 整数集合 (SET1 与 SET2 的交集)</td><td data-imt-p="1">15 to 18 15 到 18 岁</td></tr><tr><td data-imt-p="1">SET (SIZE (0..3)) OF INTEGER 整数类型，其大小可以是 0 到 3 中的一个数值。</td><td data-imt-p="1">Iteration count: 0 to 3 迭代次数：0 到 3 次</td></tr><tr><td data-imt-p="1">INTEGER (1 UNION 3 UNION 5 UNION 7) 整数类型（1、3、5、7）</td><td data-imt-p="1">1 to 7 1 到 7</td></tr><tr><td colspan="2" data-imt-p="1">Figure III-20: Values assumed to need encoding 图 III-20：被认为需要编码的数据值</td></tr></tbody></table>

When we look at the encoding of integers (and of the lengths of strings) we will see that there are three distinct cases: 当我们考虑整数的编码方式时（以及字符串长度的编码方式），会发现有三种不同的情况：

• We have a finite upper and lower bound (called a constrained value); • 我们拥有一个有限的上限和下限（这被称为“受限值”）；

• We have a finite lower bound, but no upper bound (called a semi-constrained value); • 我们有一个有限的下界，但并没有上界（这种情况被称为“半约束值”）；

• We do not have a lower bound (this cannot occur for the length of strings, as zero is always a lower bound); this is called an unconstrained value; (even if there is a defined upper bound! - the upper bound gets ignored in this case). • 我们并没有给出下限值（对于字符串长度来说，这种情况是不存在的，因为零始终是一个下限）；这种值被称为无约束值。（即使存在明确的上限的话——在这种情况下，上限会被忽略。）

We describe below the encoding of constrained, semi-constrained, and unconstrained integers, and of constrained and semi-constrained lengths of strings in subsequent text, also addressing any special encodings that arise in the case of an extensible type. In the case of a constrained integer (or length), there are several different encodings depending on the range permitted by the constraint. (Remember that the absolute values permitted do not matter). 我们在下文中描述了受限整数、半受限整数以及无限制整数的编码方式，同时还介绍了字符串长度在受限和半受限情况下的编码方法。此外，我们还讨论了在可扩展类型中出现的一些特殊编码问题。对于受限整数或字符串长度来说，根据约束条件所允许的范围不同，会有多种不同的编码方式。（需要注意的是，所允许的数值范围并不重要。）

The reader may wonder whether it is worth bothering with using "range" (and offset from the lower bound), rather than just determining the coding based on whether negative values are allowed or not, and then using enough bits to handle the largest value permitted by the constraint. Certainly INTEGER (10..13) and INTEGER (-3..0) are not likely to occur in the real world! But INTEGER (1..4) may be more common, and will use just two bits with the "offset from lower bound" rule, rather than three if we encoded the actual values. 读者可能会想，是否值得特意使用“范围”这个概念（并考虑从下限开始进行偏移处理），而不是仅仅根据是否允许使用负值来决定编码方式，然后再用足够的位数来处理由约束条件所允许的最大值。当然，在现实世界中，INTEGER(10..13)和 INTEGER(-3..0)这样的数值不太可能出现！不过，INTEGER(1..4)可能更为常见。使用“从下限开始偏移”的规则，只需要两个位数就能表示这些数值，而不是像编码实际数值那样使用三个位数。

Working with "offset from lower bound" may appear to be an additional complexity, but is actually simpler than a specification saying "First see if all allowed values are positive or not, then etc etc", and amounts to just a couple of orders in a couple of places in actual implementations. 使用“从下限开始偏移”的方法看起来可能更复杂一些，但实际上比那种要求“先判断所有允许的值是否为正数，然后再进行后续操作”的规范要简单得多。在实际实现中，这种方法的复杂度通常只有几个数量级而已。

## 6 Effective size and alphabet constraints. 6. 有效的尺寸和字母表限制。

## 6.1 Statement of the problem 6.1 问题的陈述

We mentioned above (but did not emphasise) that constraints such as: 我们之前已经提到过（不过并没有特别强调）诸如以下这些限制条件：

```autohotkey
MyString ::= PrintableString (FROM (("0" .."9")  
UNION ("#")  
UNION ("*")) 
```

are PER-visible, and would result in just four bits per character for the encoding of values of "MyString" (which consists of all strings that contain only zero to nine and hash and star - twelve characters). 这些编码方式是可见的，因此“MyString”字符串的编码方式下，每个字符只需要 4 位比特位即可表示（“MyString”由所有只包含 0 到 9 以及哈希和星号这 12 个字符组成的字符串构成）。

This is described more fully in the discussion of the encoding of character string values in clause 14, but note here that for alphabet constraints, what matters is the actual number of characters permitted, not the range of characters. This is different from the treatment of constrained integers, as the need to define a character string type with an almost random selection of characters being permitted is far more likely to arise than the need to define an integer type with a random selection of integer values. 在第 14 节中关于字符串值编码的讨论中有更详细的说明。不过这里需要注意的是，对于字母约束来说，重要的是允许使用的字符数量，而不是字符的范围。这与受限整数的处理方式不同，因为定义字符串类型时，通常需要允许使用几乎随机选择的字符，这种情况比定义整数类型时需要允许使用随机整数值的情况要更常见。

There is, however, a slightly difficult interaction between alphabet constraints such as that above and length (size) constraints which can also be applied. 不过，上述字母顺序约束与长度（大小）约束之间存在着一些较为复杂的相互作用，这种相互作用也是需要考虑的。

For example, consider 例如，考虑以下情况：

```txt
MyString1 ::= IA5String (FROM ("01") INTERSECTION SIZE (4))
MyString2 ::= IA5String (FROM ("TF") INTERSECTION SIZE (6))
MyString3 ::= IA5String (Mystring1 UNION Mystring2) 
```

All constraints are PER-visible, and it is clear that MyString 1 has a fixed length of 4 characters so should encode without a length field, and contains only two characters "0" and "1", and should encode with just one bit per character. Similarly MyString2 has an alphabet constraint restricting its character set to "T" and "F" (again giving one bit per character), and a size constraint of 6. 所有约束条件都是显而易见的。显然，MyString1 的固定长度为 4 个字符，因此不需要使用长度字段进行编码；它只包含两个字符“0”和“1”，每个字符只需要用一个比特位来表示。同样，MyString2 有一个字符集限制，即只能使用“T”和“F”两个字符，这也意味着每个字符只需要用一个比特位来表示。此外，MyString2 还有 6 个字符的长度限制。

But what is the alphabet and size constraint on MyString3? Does it have them? This is where the concept of an effective size constraint and an effective alphabet constraint comes in. 但是，MyString3 中的字母表规则和大小限制是什么呢？它真的有这些限制吗？这里就涉及到“有效大小限制”和“有效字母表限制”的概念了。

## 6.2 Effective size constraint 6.2 有效尺寸限制

An "effective size constraint" is defined to be a single size constraint such that a length is permitted by that size constraint if and only if there is at least one abstract value in the constrained type that has that length. “有效大小限制”指的是这样一种大小限制：只有当受限类型中至少有一个抽象值的长度满足该限制时，该长度才被允许使用。

So in the earlier example, MyString3 has abstract values of length 4 and 6 only. But what matters is the range of a size constraint, which is 4 to 6. This is equivalent to 0 to 2 when we remove the lower bound, so the length field of MyString3 would encode with 2 bits. 在前面的例子中，MyString3 只有长度为 4 和 6 的抽象值。但重要的是大小范围的限制，即 4 到 6 之间。如果去掉下限，这就相当于 0 到 2 之间了，所以 MyString3 的长度字段可以用 2 位来表示。

## 6.3 Effective alphabet constraint 6.3 有效的字母顺序限制

In an exactly equivalent fashion, an "effective alphabet constraint" is defined to be a single permitted alphabet constraint such that a character is permitted by that alphabet constraint if and only if there is at least one abstract value in the constrained type that contains somewhere within it that character. 以一种完全类似的方式，所谓的“有效字母表约束”可以被定义为一种单一的允许字母表约束。也就是说，一个字符只有在其所属于的约束类型中至少存在一个抽象值包含该字符时，才被允许使用该字母表约束来表示。

So in the earlier example, all the characters "0", "1", "T" and "F" are used by at least one abstract value, and the effective alphabet constraint allows these (and only these) characters, so two bits will be used per character. 所以在前面的例子中，所有的字符“0”、“1”、“T”和“F”都被至少一个抽象值所使用。而有效的字母表限制要求只能使用这些字符，因此每个字符需要两个比特来表示。

It is normally a simple matter for both a human and a computer to work out the effective alphabet and effective size constraints in every case, provided the rules on what is PER-visible are understood and applied. 对于人类和计算机来说，只要理解并应用了关于什么是“可见”的规则，那么确定每种情况下的有效字母表以及有效的大小限制通常都是一件简单的事情。

This is particularly true for a human because constraints are in practice quite simple. For a computer (which in an ASN.1 tool needs to be programmed to handle all possible constraints, no matter how complex or way-out), a program can be written which can take any arbitrarily complex set arithmetic expression (using only size and alphabet constraints) and resolve it down to an effective alphabet and an effective size constraint. It does this using equalities like: 对于人类来说，这种情况尤为明显，因为约束实际上非常简单。而对于计算机而言（在 ASN.1 工具中，计算机需要被编程来处理所有可能的约束，无论这些约束多么复杂或难以处理），可以编写出一个程序，该程序能够接受任何任意复杂的集合算术表达式（仅使用大小和字母表的约束），并将其解析为有效的字母表和有效的大小约束。这一过程是通过使用诸如“相等”这样的逻辑运算符来实现的。

```txt
A EXCEPT B equals A INTERSECTION (NOT B)
and
NOT (A UNION B) equals (NOT A) INTERSECTION (NOT B)
etc 
```

If single value constraints had been allowed on character string types, this would have been a much more difficult task. 如果字符字符串类型允许使用单一值约束条件的话，那么这件事就会变得困难得多。

## 7 Canonical order of tags 7. 标签的规范顺序

The reader will recall that PER requires a choice index, which means numbering the alternatives in a CHOICE in some order. Similarly, it avoids the need to encode a tag with elements of a SET by determining a fixed order for transmission of values of those elements. 读者应该记得，PER 要求使用一个选择索引，这意味着需要按照某种顺序对 CHOICE 中的选项进行编号。同样，它避免了需要为 SET 中的元素编码标签的情况，而是为这些元素的取值确定了固定的传输顺序。

It would have been possible to have used the textual order of the alternatives and elements for this purpose, but this was felt to be inappropriate, as any change in the textual order (perhaps in going from version 1 to version 2, for purely editorial reasons) would change the encoding on the line. Essentially, such a change of order would have to be forbidden, which was felt to be counter-intuitive. 虽然可以使用备选方案和元素的文本顺序来达到这个目的，但这样做被认为是不合适的。因为无论何时改变文本顺序（比如从版本 1 切换到版本 2，纯粹出于编辑上的考虑），都会改变该行的编码方式。实际上，这样的顺序调整应该被禁止，因为这样做会违反直觉。

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/54379e17-c034-430b-894c-f77661f731e5/8322cef91d76bce238aa89f366f59fa39d31d1bcb5c7cc2f46f70aa78b05cf52.jpg)

As all alternatives in a CHOICE and all elements in a SET are already required to have distinct (outer-level) tags, there is an obvious alternative available to that of using textual order: define an order for tag values, and then effectively re-order CHOICE and SET into tag order before determining the choice index or the order of transmission for SET elements. This is what is done. 在 CHOICE 结构中，所有的替代选项以及 SET 中的各个元素都明确要求具有独立的（外部级别的）标签。因此，除了使用文本顺序之外，还有一个明显的替代方案：为标签值定义一种排序方式，然后按照该排序方式重新整理 CHOICE 结构和 SET 中的元素，从而在确定选择索引或 SET 元素传输顺序时更加合理。实际上，这就是我们所采取的方法。

The so-called canonical tag order is defined to be: 所谓的规范标签顺序定义为：

```txt
Universal Class (first)
Application Class
Context-specific Class
Private Class (last) 
```

with lower tag numbers coming before higher ones within each class. 在每个类别中，较低的分类号会出现在较高的分类号之前。

There is just one small complication - there always is! Recall that most types have the same outerlevel tag for all their abstract values, and we can validly talk about the "tag of the type". The only case where this is not true is for an untagged choice type. In this case different abstractvalues may have different outer level tags, and we cannot talk about "the tag of the type" so easily. (But remember that all these tags are required to be distinct from any of the tags of any other type in a SET or CHOICE). PER defines the tag of an untagged choice type as the smallest tag of any of its values, for the purpose of putting types into a canonical order, and the problem is solved. 不过有一个小问题需要解决——不过这种情况总是存在的！记住，大多数类型的所有抽象值都拥有相同的外部标签，因此我们可以合理地谈论“类型的标签”。唯一例外的是未标记的选择类型。在这种情况下，不同的抽象值可能拥有不同的外部标签，因此我们无法如此简单地谈论“类型的标签”。（但请记住，所有这些标签都必须与任何其他类型的标签区分开来。）PER 将未标记选择类型的标签定义为其所有值中最小的标签，这样就能将类型按规范顺序进行排序，问题也就解决了。

## 8 Encoding an unbounded count 8. 对无限数量的数据进行编码

If constraints are placed on lengths, iteration counts, or sizes of integers, PER will often omit the length field completely, or will use a highly optimised encoding for the length (described later), otherwise it will use length encodings similar to (but different from) those of BER. It is these encodings that are described in this clause. 如果對整数长度、迭代次数或大小施加了限制，PER 通常会完全省略长度字段，或者会使用一种高度优化的长度编码方式（详见后文）。否则，它会使用与 BER 类似的编码方式，但有所不同。正是这些编码方式在本文中得到了描述。

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/54379e17-c034-430b-894c-f77661f731e5/c1ffc65dfd2059ca2438fe3377006a891e2fa8818e6c503fc6dd4e7de209f78f.jpg)

## 8.1 The three forms of length encoding 8.1 三种长度编码方式

PER has an equivalent of the BER short and long definite length and indefinite length forms, but there are a number of important differences, and apart from the short definite form the encodings are not the same as BER. PER 的编码方式与 BER 的短型、长型以及不定型编码方式类似，但两者之间也存在一些重要的差异。除了短型编码方式外，其他类型的编码方式与 BER 并不相同。

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/54379e17-c034-430b-894c-f77661f731e5/eaf0388646b3398d97e51f3c3c53c8d0aad70523ef1eaf976ccf85dc5f488d8c.jpg)

This clause describes the form used for length determinants in cases where a count is needed which is potentially unbounded. This is generally the case only when there are no PER-visible constraints on the length of strings, iteration counts of SEQUENCE OF and SET OF, or on the size of integers. 这一条款规定了在需要计算可能无限长的数值时，所使用的长度表示形式。通常，这种情况只发生在没有对字符串长度、SEQUENCE OF 和 SET OF 的迭代次数，以及整数大小施加任何可见性限制的情况下才会发生。

Where there are such constraints, PER will have a much more optimised length field (described later), or no length field at all. 在存在此类限制的情况下，PER 将会有一个经过优化过的长度字段（稍后会详细说明），或者根本就没有长度字段。

The first important difference from BER is in what PER counts. (BER always counts the number of octets in the contents). PER counts the number of bits in a BIT STRING value, abstract characters in a known-multiplier character string values, the iteration count in a SEQUENCE OF or SET OF, and octets in all other cases. We talk about the count in the length determinant. 与 BER 相比，第一个重要的区别在于 PER 的计算方式不同。（BER 总是计算内容中的八位组数量）。而 PER 则计算 BIT 字符串中的位数、已知乘数字符字符串中的抽象字符、SEQ 或 SET 中的迭代次数，以及其他情况下所有八位组的数量。我们所说的“计数”指的是在长度指标上的计数结果。

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/54379e17-c034-430b-894c-f77661f731e5/d9de893ca7ab05ab0de1992ed9ac17249880e49b35a59c179402922e2206cfb1.jpg)

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/54379e17-c034-430b-894c-f77661f731e5/80e26e68cb788a2b90e5dbf1678b2981ab36f014f83b3a9e582eb0a98d65fe67.jpg)

Figure III-21 to III-23 illustrate the three forms of encoding for the length determinant. 图 III-21 至 III-23 展示了长度决定因素三种编码方式的情况。

In the first form (corresponding to the BER short form, although PER does not use this term), we have the same encoding as BER, with the encoding placed in an octet-aligned-bit-field (in other words, there will be padding bits in the ALIGNED variants). The top bit of the octet is set to zero, and the remainder of the octet encodes count values from zero to 127. 在第一种形式中（对应 BER 简式格式，尽管 PER 并不使用这一术语），我们的编码方式与 BER 相同。编码信息被放在一个八位元字段中（也就是说，在 ALIGNED 版本中会有填充位）。八位元的最高位被设置为 0，其余位则用于编码 0 到 127 之间的数值。

In the second form (corresponding roughly to the BER long definite form), there are always exactly two octets of length determinant. The first octet has the first bit set to 1 and the second bit set to zero, and the remaining 14 bits of those two octets encode count values from 128 to 16K-1. 在第二种形式中（大致相当于 BER 长定义形式），总是恰好有两个八位组。第一个八位组的第一位被设置为 1，第二位为 0；这两个八位组中的其余 14 位则用于编码从 128 到 16K-1 的计数值。

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/54379e17-c034-430b-894c-f77661f731e5/12e29a53499794351d8d4b4ca6b068cfddc4b09d09282222c6c00d58d89c5740.jpg)

Figure III-23: The encoding for large counts 图 III-23：大数量数据的编码方式

The third form (corresponding roughly to the BER indefinite form, but with a very different mechanism) has an initial octet with both the top two bits set to 1. The remaining six bits encode (right justified) the values 1 to 4 - call this value "m". This octet says two things: 第三种形式（大致相当于 BER 的不确定形式，但机制有所不同）的第一个八位组中，前两个位被设置为 1。剩余的六个位则用来以右对齐的方式存储 1 到 4 的数值——将这個数值称为“m”。这个八位组包含了两方面的信息：

• It says that "m" times 16K bits, iterations, abstract characters, or octets of the contents follow. • 文中提到：“m”乘以 16K 比特、迭代次数、抽象字符或八位元的内容数量如下。

• It says that after this fragment of the contents, there will be a further length field (of either of the three forms) for the rest of the contents, or for another fragment. • 根据说明，在这一段内容之后，还会有一个长度字段，该字段可以采用三种格式中的任何一种来表示后续内容的长度，或者用于指代另一个片段的内容。

PER requires that each fragment should be as large as possible, so there are no encoder's options in the choice of "m". Notice that in principle the largest permitted "m" could have been made much greater (there are six bits available to encode it), but the designers of PER chose to enforce fragmentation into fragments of at most 64K (4 times 16K) items for long octet strings etc. PER 要求每个片段尽可能大，因此在选择“m”时没有编码器的选项。不过，原则上最大的“m”值可以更大（有六个比特位可以用来编码），但 PER 的设计者选择将片段大小限制在最多 64K（即 4 个 16K）项以内，适用于较长的八位元字符串等场景。

Figure III-24 illustrates the encoding (in binary) for count values (for example for a SEQUENCE OF) of 5, 130, 16000, 32768, and 99000. The insertion of one or more padding bits is shown with a "P", the length determinant is prefixed with "L:", and fragments of content with "C:" (a convention used throughout this chapter). 图 III-24 展示了各计数值的二进制编码形式，这些计数值包括 5、130、16000、32768 和 99000。其中一个或多个填充位的插入用“P”表示；而内容片段则用“C”来表示（这一符号格式在整篇文档中都是统一使用的）。

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/54379e17-c034-430b-894c-f77661f731e5/87c7471fc5b9e533b0986329d5fa1eb711840acf77737b2d350ed898d6df6bde.jpg)

Note that where we get fragmentation in Figure III-24, although the fragments will be encoding multiples of 16K values of the same type, the encodings for each value are not necessarily the same length if the type being iterated has extensions, so padding bits may again be required before the length determinant after a fragment, as all these length determinants are specified as octetaligned. 请注意，在图 III-24 中出现的碎片化现象意味着，虽然各个片段会编码相同类型的 16K 数值的多个副本，但如果所迭代的类型具有扩展部分，那么每个数值的编码长度并不一定是固定的。因此，在分割后的片段中，可能需要再次使用填充位来确定长度，因为所有长度参数都被指定为采用八位对齐格式。

## 8.2 Encoding "normally small" values 8.2 对“通常较小的”数值进行编码处理

PER has one further encoding for counts that are potentially unbounded. This encoding is used in cases where, although there is no upper-bound on the values which may need to be encoded, the values are expected to be "normally small" (and are all zero or positive), so this is described as "encoding a normally small non-negative whole number". PER 还有一种用于处理可能无限大的数值的编码方式。这种编码方式适用于那些虽然不存在数值的上限限制，但预计这些数值会“通常很小”的情况（也就是说，这些数值要么全部为零，要么全部为正）。因此，这种编码方式可以被描述为“对通常很小的非负整数进行编码”。

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/54379e17-c034-430b-894c-f77661f731e5/f77abbe65e10ff278b1be3a5160b584bebed527835d206e0174060e8662297d0.jpg)

This case is applied to encode a choice index for a choice alternative that is not in the root - there could be millions of additional choices in Version 2, and a Version 1 system has no idea how many, but actually, there are unlikely to be more than a few. 这个案例用于对那些不在根节点中的选择选项进行编码。在版本 2 中，可能会存在数百万个额外的选择选项，而版本 1 的系统根本无法知道到底有多少种选择选项。但实际上，这样的选择选项数量应该不会超过几个而已。

A second application is to encode values of an enumerated type that are outside the root, where again the possible values are unbounded but are usually going to be small. 第二个应用场景是对那些位于根类型之外枚举类型的值进行编码。在这种情况下，可能的取值是没有上限的，但通常这些取值都会比较小。

In both these cases, encoding the value as an unbounded integer value (which would require an octet-aligned length field - usually set to 1 - as above and an integer encoding of one octet) is not optimal. The specified encoding in this case is instead to use just seven bits (not octet-aligned), with the top bit set to zero and the other six encoding values up to 63. Thus we avoid the octet alignment, and use only seven bits, not sixteen. Why use seven bits and not eight? Remember that this encoding will frequently appear following an extensions bit, so the two together give us exactly eight bits and if we had alignment at the start, we still have it. 在这两种情况下，将值编码为无界整数值都不是最优的选择。无界整数值的编码需要一个八位对齐的字段——通常该字段会被设置为 1——而仅用一个八位整数进行编码则更为简单。在这种情况下，我们采用仅使用七位进行编码，其中最高位设为 0，其余六位可以表示 0 到 63 之间的数值。这样我们就避免了八位对齐的问题，只使用了七位而不是十六位。为什么使用七位而不是八位呢？记住，这种编码方式通常出现在扩展位之后，因此两者加起来正好等于八位。而且，如果一开始就有对齐方式的话，我们仍然可以保持这种对齐状态。

Of course, there is a penalty in optimising for small values! If the normally small non-negative whole number actually turns out to be more than 63, then we add a one-bit bit-field set to one, followed by a positive integer encoding into minimum octets preceded by a general length field as described above. 当然，在针对较小值进行优化时也会存在惩罚机制！如果原本为非负整数的小数值实际上超过了 63，那么我们会添加一个 1 位长的位字段，并将其值设置为 1；然后会使用一个正整数进行编码，该编码结果会被存储到最小 8 位字长的数据中，同时还会包含一个通用长度字段，就像上面所描述的那样。

Figure III-25 illustrates the encoding of a count as a normally small non-negative whole number for values of 5, 60, 254, and 99000. (There is no way the latter will occur in any real specification, and a tool that failed to provide code for this case - simply saying "not supported" - would be very unlikely to be caught out! The specification is, however, complete, and will encode any value no matter how large.) Note the absence of padding bits in the first two cases. 图 III-25 展示了如何将计数编码为一个通常较小的非负整数。对于 5、60、254 和 99000 这些数值，都会采用这种编码方式。（实际上，99000 这样的数值在真实的应用中是不可能出现的，因此如果一个工具无法为这种情况提供编码支持，只是简单地表示“不支持”，那么这种情况很可能会被忽略。不过，该规范是完整的，无论数值有多大，都能得到正确的编码。）注意，在前两种情况下，没有使用填充位。

```txt
5 L:0000101 C:(5 items of content)
60 L:0111100 C:(60 items of content)
254 L:1 P00000001 11111110 C:(254 items of content)
99000: L:1 P11000100
C:(64K items of content)
L:P11000010
C:(32K items of content)
L:P10000010 10111000
C:(696 items of content)

Figure III-25: Encoding normally-small non-negative whole numbers 
```

## 8.3 Comments on encodings of unbounded counts 8.3 关于无限计数编码的评论

The fragmentation mechanism in PER is not reliant on nested TLV structures, and can be applied to any contents encoding, and in particular to encodings of unbounded integers. Because the number of 64K fragments is unlimited, PER can truly encode indefinitely large integers, but we have already seen that the actual limit BER imposes is for all practical purposes irrelevant. The fragmentation mechanism of PER, particularly the lack of encoder's options, is, irrelevant. The fragmentation mechanism of PER, particularly however, probably simpler than that of BER. however, probably simpler than that of BER. PER 中的碎片化机制并不依赖于嵌套的 TLV 结构，因此可以应用于任何内容编码，尤其是无界整数的编码。由于 64K 片段的数量是无限的，PER 能够真正编码无限大的整数。不过，我们已经看到，实际上 BER 所设定的限制在实际使用中并不重要。PER 的碎片化机制，尤其是缺乏编码器的选项这一特点，实际上并不重要。而且，PER 的碎片化机制可能比 BER 的更为简单。

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/54379e17-c034-430b-894c-f77661f731e5/517e198ab3afac50846ed1673f29daae7d95504139d64e3c5d7c2a2b98016cc7.jpg)

The main advantage of the PER encoding over BER is that length fields will generally be two octets, and counts of less than 128 are required to be done using the short form. With BER, length fields of three octets (long definite form) are permitted (and some implementations use them always), even for a contents length of - say - five octets. This is a big verbosity overhead for such implementations. PER 编码相比 BER 编码的主要优势在于：长度字段通常只有两个八位元；而使用短形式时，需要记录的数量不得超过 128 个。而在 BER 编码中，即使内容长度为五个八位元，也允许使用三个八位元的长度字段（某些实现方式总是采用这种形式）。但对于这类实现方式来说，这种额外的信息量确实会带来很大的负担。

The main advantage of the encoding of normally small non-negative whole numbers is that they (usually) encode into a bit-field without padding bits. If the value gets too big (unlikely to occur in practice), there is still only an additional penalty of one bit over a general length encoding. 通常较小的非负整数的编码方式的主要优势在于：它们可以直接用一位字段来表示数值，而无需进行填充操作。如果数值变得过大（但在实际使用中这种情况很少发生），那么与常规长度编码相比，只会增加一个比特的额外开销而已。

## 9 Encoding the OPTIONAL bit-map and the CHOICE index. 9. 对可选的位图和选择索引进行编码。

## 9.1 The OPTIONAL bit-map 9.1 可选位图

We already know that when encoding a sequence or set value, PER encodes a preamble into a bit-field, with one bit for each OPTIONAL or DEFAULT element (zero bits if there are no OPTIONAL or DEFAULT elements). The bit is set to one if a value of the element is present in the encoding, set to zero otherwise. The encoding of each element then follows. 我们已经知道，在对序列或集合值进行编码时，PER 会将前置码编码到位字段中，每个可选的或默认的元素对应一个位位。如果某个元素在编码中出现，则该位会被设置为 1；否则，该位会被设置为 0。之后，就会对每个元素进行编码处理。

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/54379e17-c034-430b-894c-f77661f731e5/45bc52391de8e6dc935ece9e45267ceb3853afc5012be11a715e7c6ae46ddf39.jpg)

This applies to elements in the root. A similar bit-map is used at the insertion point for elements which are extension additions, but this is described later. 这适用于根节点中的元素。在插入点处，对于通过扩展方式添加的元素，也会使用类似的位图表示方式，不过这一点将在后面详细说明。

Under normal circumstances, there is no length determinant for this bit-map (as both sender and receiver know its length from the type definition), but if (and it will never occur, so a "not supported" response from a tool would be OK!) the length of the bit-map (the number of optional or default elements) exceeds 64K, then a length determinant is included and the bit-map fragments into 64K fragments. 在正常情况下，这个位图并没有明确的长度限制（因为发送方和接收方都可以通过类型定义来知道其长度）。但是，如果位图的长度超过 64K（这种情况几乎不会发生，所以工具可以返回“不支持”的响应即可！），那么就会有一个长度限制机制，位图会被分割成 64K 的片段。

## 9.2 The CHOICE index 9.2 选择指数

For a CHOICE value, there is again a preamble. If the type is not extensible, or the value is in the root, we have an upper bound on this choice index (and a lower bound of zero - the choice index starts at zero with the alternative that has the lowest tag value, as described earlier). This value is encoded as a constrained integer value - one that has both an upper and a lower bound. We will see below that integer values that are constrained to a range of, say, 0 to 15 (up to 16 alternatives in the CHOICE type) encode into a bit-field of four bits. 对于 CHOICE 类型，同样存在一个上限限制。如果该类型不可扩展，或者该值位于根级别，那么这种选择索引就有一个上限；而下限则是零——因为选择索引从具有最低标签值的选项开始，这一点之前已经描述过。这个值被编码为一个有上下限的受限整数值。如下所示，那些被限制在 0 到 15 这个范围内的整数值（在 CHOICE 类型中最多可容纳 16 个选项）会被编码为四个比特位的字段。

If the chosen alternative is outside of the root, then we get our "extensions bit" set to one in a bitfield (as described earlier), followed by (usually) seven bits in a bit-field encoding the normally small non-negative whole number which is the index of the alternative within the extension additions (taking the first addition alternative as value zero). Note that whilst version brackets are allowed in a CHOICE, their presence makes no difference to the encoding, it is only for SEQUENCE and SET that the encoding is affected. 如果所选的替代方案位于根之外，那么我们的“扩展位”就会被设置为 1（如前面所述）。之后，通常还会有一个由 7 位组成的位字段，用来表示那个较小的非负整数值，这个数值就是该替代方案在扩展中的索引值（将第一个替代方案视为值零）。需要注意的是，虽然 CHOICE 类型允许使用版本标记，但这一特性对编码并无影响；只有 SEQUENCE 和 SET 类型时，编码才会受到影响。

Notice that if we started on an octet boundary, we have added exactly eight bits and will remain on an octet boundary, and we have not forced any octet alignment in these encodings. Illustrations of these encodings are given in Clause 16 describing the complete encoding of choice values. 请注意，如果我们从八位组的边界开始，那么我们就增加了整整八位，并且仍然会保持八位组的边界不变。在这些编码中，我们没有强制任何八位组之间的对齐。这些编码的示例可以在第 16 条中找到，该条款描述了选择值的完整编码方式。

## 10 Encoding NULL and BOOLEAN values. 10. 对 NULL 值和 BOOLEAN 值进行编码处理。

These are easy. No PER-visible constraints can apply, and optionality is sorted by the bit-map. 这些都很简单。没有任何 PER 可见性的限制条件适用，而且选项性也是通过位图来处理的。

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/54379e17-c034-430b-894c-f77661f731e5/5f4e17134524597f8b7980c89af41ef4e23a48209041f3c7be5d933119743a5e.jpg)

Zero bits for NULL. That's all you need. One bit for BOOLEAN - set to 1 for TRUE and set to zero for FALSE. And of course there are no padding bits in the ALIGNED version. 对于 NULL 字段，只需要 0 位。对于 BOOLEAN 类型的数据，只需要 1 位——当值为 TRUE 时设置这 1 位为 1，当值为 FALSE 时则设置这 1 位为 0。当然，在 ALIGNED 版本中并没有使用任何填充位。

## 11 Encoding INTEGER values. 11. 对整数值进行编码。

Remember - when we talk about constraints below, we are only concerned with PER-visible constraints as discussed earlier. 请记住——当我们讨论以下约束条件时，我们仅关注前面提到的那些对 PER 可见的约束。

The only interesting parts of this discussion are to do with encoding constrained integers, when "minimum bits" tend to be used. For unconstrained integers, we get the standard length determinant and an encoding in the mum octets. There are, however, differences between the ALIGNED and UNALIGNED variants (apart from adding or not adding padding bits). 这次讨论中唯一有趣的内容是关于受限整数的编码问题，因为通常会涉及到“最小位数”的设定。对于无限制的整数，我们得到的是标准的长度表示方式，以及用 mum 八位字节进行编码的方法。不过，ALIGNED 和 UNALIGNED 这两种编码方式之间还是存在差异的（除了是否添加填充位这一点之外）。

## 11.1 Unconstrained integer types 11.1 无约束的整数类型

The most important thing with the encoding of INTEGER types is whether a lower bound on the value exists or not. If it doesn't, we encode into the minimum octets as a signed number, with a general length determinant (as described earlier) containing a count of the number of octets. So: 在整数类型编码中，最重要的是是否存在值的下限。如果不存在下限，我们就将其编码为带有符号的数字，其一般长度由某个确定因素决定（如前所述），该因素包含八位小数的数量。因此，编码方式如下：

If there is no lower bound, we get a 2's-complement encoding into minimum octets with a general length determinant (all variants). 如果没有下限限制，那么就可以采用 2 的补码编码方式，将数据编码成最小数量的八位二进制数，而这一编码方式具有通用的长度确定因素（所有变体都适用）。

```txt
integer1 INTEGER ::= 4096
integer2 INTEGER (MIN .. 65535) ::= 127
integer3 INTEGER (MIN .. 65535) ::= -128
integer4 INTEGER (MIN .. 65535) ::= 128 
```

are all described as "unconstrained" and encode as (with "L:" preceding the length determinant - if any - and "C:" preceding the contents encoding - if any): 所有这些都被描述为“无约束的”，并且其编码方式如下（其中“L：”位于长度决定器的前面——如果有的话；“C：”位于内容编码的前面——如果有的话）：

```yaml
integer1: L:P00000010 C:00010000 00000000
integer2: L:P00000001 C:01111111
integer3: L:P00000001 C:10000000
integer4: L:P00000010 C:00000000 10000000 
```

This is the same as BER (for values up to 127 octets), but without the identifier octets. Remember that in the UNALIGNED variant P bits are never inserted. 这与 BER 类似（适用于最多 127 个八位元的值），但缺少了标识符相关的八位元。请注意，在 UNALIGNED 变体中，从不插入 P 位。

## 11.2 Semi-constrained integer types 11.2 半约束整数类型

Once we have a lower bound (which will typically be zero or one, but could be anything) then we only need to encode a positive value, using the offset from the base as the value to be encoded. 一旦我们得到了一个下限值（通常为零或一，但实际上可以是任何数值），那么我们就只需要编码一个正数即可，将基准值作为需要编码的数值来进行处理。

Encode the (positive) offset from the lower bound. 对从下限开始的正数偏移量进行编码。

As for unconstrained integer types, the encoding is into the minimum necessary multiple of eight bits preceded by a length determinant counting the number of octets. So: 对于无约束的整数类型，其编码方式是将数据编码为至少 8 位的最小倍数，并且会在编码前加上一个表示字节数的长度指示符。因此，编码后的数据总位数由该长度指示符决定。

```txt
integer5 INTEGER (-1.. MAX) ::= 4096
integer6 INTEGER (1 .. MAX) ::= 127
integer7 INTEGER (0 .. MAX) ::= 128 
```

encode as: 编码为：

```yaml
Integer5: L:P00000010 C:00010000 00000001
Integer6: L:P00000001 C:01111110
Integer7: L:P00000001 C:10000000 
```

(Compare the encoding of integer7 with that of integer4.) （将 integer7 的编码与 integer4 的编码进行比较。）

## 11.3 Constrained integer types 11.3 受限整数类型

It is in the encoding of integers with both a lower and an upper bound that PER tries hardest to "do the sensible thing". However, "the sensible thing" as determined by the proponents of the UNALIGNED variant turned out to be different from "the sensible thing" as determined by the proponents of the ALIGNED version, so the approaches are not quite the same. Which is the most sensible, you must judge! 在整数的编码过程中，PER 试图做到“最合理的选择”。不过，由“UNALIGNED”方案的支持者所定义的“最合理的方式”，与由“ALIGNED”方案的支持者所定义的“最合理的方式”并不相同。因此，这两种方法并不完全相同。到底哪种方式更合理呢？这必须由用户自己来判断了！

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/54379e17-c034-430b-894c-f77661f731e5/8005424648fbe349266b1ecd5c6751a3825a98954104fa3279482655a97f55eb.jpg)

The standard talks about the "range" of the values, defining the "range" as the upper-bound minus the lower-bound plus 1. So a constraint of (0..3) has a "range" of four. Thus "range" is essentially defined as the total number of values between (and including) the upper and lower bounds. 标准中提到了“范围”的概念，将“范围”定义为上限减去下限再加上 1。因此，约束条件(0..3)对应的“范围”为 4。所以，“范围”本质上就是介于上下限之间的值的总数，包括上下限本身。

If the "range" is one, then only one value is possible. This is not likely to occur in practice, but the encoding follows naturally from the treatment of larger ranges and is similar to the handling of NULL: there are no bits in the encoding! 如果“范围”只有一个值，那么只有一种可能性。这种情况在实践中不太可能出现，但编码方式实际上是从处理更大的范围时自然得出的，这与处理 NULL 值的方式类似：在编码过程中并没有使用任何比特位！

We first describe all the cases that can arise, then we give examples. 我们首先描述了所有可能出现的情形，然后给出了具体的例子。

For larger ranges, the UNALIGNED case is the easiest to describe. It encodes the offset from the lower bound into the minimum number of bits needed to support all values in the range. So a constraint of (1..3) - or (6..8) or (11..13) or (-2..0) - has a range of three, and values will encode into a bit-field of 2 bits (as would a range of 4). A constraint of (0..65535) will produce encodings of all values into exactly 16 bits, and so on. Remember that with the UNALIGNED variants, there are never any padding bits, so in this last case successive integers in the encoding of SEQUENCE OF INTEGER (0..65535) will all be 16 bits long, but may all be starting at bit 3 (say) of an octet. 对于更大的范围，UNALIGNED 这种编码方式最为简单。它将下限的偏移量编码为最少数量的位，从而能够支持该范围内的所有值。例如，对于(1..3) - 或 (6..8) - 或 (11..13) - 或 (-2..0) - 这样的约束条件，其范围就是 3 个值；而(0..65535)这样的约束条件则会将所有值编码为 16 位。记住，在 UNALIGNED 编码方式中，永远不会出现填充位，因此在这种情况下，SEQUENCE OF INTEGER (0..65535) 编码中的连续整数都将占用 16 位，但这些整数可能都从八位字的第 3 位开始。

## The ALIGNED case is a bit more varied! “ALIGNED”案例的情况要复杂一些！

If the range is less than or equal to 255 (note: 255, not 256), then the encoding is into a bit-field which is the minimum necessary to encode the range, and there will be no padding bits. If, however, the range is 256 - for example, the constraint might be (0..255) or (1..256) - then the value encodes into eight bits, but they go into an octet-aligned field - we get padding bits if necessary. 如果范围小于或等于 255（注意：是 255，不是 256），那么编码会使用最少的位数来表示这个范围，此时不需要填充位。然而，如果范围大于 256，例如约束条件可能是(0..255)或(1..256)，那么这个值就需要用 8 位来表示，但这些位会被安排到一个八位字段中；如果需要，还会添加填充位。

If the range is greater than 256 but no greater than 64K, we get two octets (octet-aligned). 如果该范围大于 256 但不超过 64K，那么我们得到的是两个八位元数据（即按八位元对齐的方式存储）。

If we need to go over two octets (the range is more than 64K), we encode each value (as a positive integer offset from the lower bound) into the minimum number of octets necessary (except that zero always encodes into an octet of all zeros, not into zero bits, so we always have a minimum of one octet), and prefix a length determinant giving the number of octets used. In this case, however, the general length determinant described earlier is not used! Instead, we look at the range of values that this octet count can take (lower bound one, remember, because zero encodes into one octet), and encode the value of the length in the minimum number of bits needed to encode a positive number with that range, offset from one. 如果我们需要表示的数值超过两个八位元的范围（实际范围超过 64K），我们会将每个数值编码为最少数量的八位元（作为比下限高的一个正整数偏移量）。不过，零总是被编码为一个全零的八位元，因此至少会占用一个八位元。此外，还会添加一个长度指示符来表明所使用的八位元数量。不过，在这种情况下来，我们并不使用之前描述的一般长度指示符。相反，我们会考虑这个八位元计数所能表示的值范围（记住，下限是 1，因为零会被编码为一个八位元）。然后，我们会用最少的比特数来表示这个长度值，从而确保能够表示出该范围内的所有正数。

Let's have some examples. What follows is not correct value notation - for compactness of the examples, we give a value, then a comma, then another value, etc, and use commas to separate the encodings in the same way. 让我们来看一些例子。下面这个写法并不正确——为了简洁起见，我们通常会先给出一个数值，然后加上逗号，再给出另一个数值，以此类推，并用逗号来分隔不同的编码方式。

```txt
integer8 INTEGER (3..6) ::= 3, 4, 5, 6
integer9 INTEGER (4000..4254) ::= 4002, 4006
integer10 INTEGER (4000..4255) ::= 4002, 4006
integer11 INTEGER (0..32000) ::= 0, 31000
integer12 INTEGER (1..65538) ::= 1, 257, 65538 
```

will encode as follows: 将会按照以下方式进行编码：

```txt
integer8 C:00, C:01, C:10, C:11
integer9 C:00000010, C:00000110
integer10 C:P00000010, C:P00000110
integer11 C:P00000000 00000000, C:P01111001 00011000
integer12 (UNALIGNED) C:0 00000000 00000000,
    C:0 00000001 00000000,
    C:1 00000000 00000001
(ALIGNED) L:00 C:P00000000,
    L:01 C:P00000001 00000000,
    L:10 C:P00000001 00000000 00000001 
```

You will see that where there is no length determinant, the field is the same size for all values of the type, and can be deduced from the type notation. (If this were not true, PER would be a bust specification!) Where the field size varies, a length determinant is encoded so that the decoder knows the size of the field, with the length of the length determinant the same for all values, and again derivable from the type definition. As stated earlier, these are necessary conditions for an encoder and decoder to be able to interwork. Study these examples! 你会看到，在不存在长度确定因素的情况下，该字段的大小对于类型中的所有值都是相同的，并且可以从类型表示法中推导出来。（如果情况并非如此，那么 PER 就不是一个有效的规范了！）当字段大小有所变化时，就会引入长度确定因素，这样解码器就能知道字段的大小。而长度确定因素的长度对于所有值都是相同的，同样也可以从类型定义中推导出来。正如之前所说，这些是编码器和解码器能够相互协作的必要条件。请仔细研究这些例子吧！

There is one further (and final) case for encoding the ALIGNED variant of a constrained integer: If the number of octets needed to encode the range of the integer value exceeds 64K ..... Need I go on? This will never ever arise in practice! But if it did, then a general length encoding is used, and the fragmentation procedures discussed earlier come into place. 还有另一种情况需要编码受限整数的对齐版本：如果编码该整数值所需的八位元数量超过 64K……我还需要继续列举下去吗？但实际上这种情况绝不会出现！但如果真出现了，那么就需要使用通用的长度编码方式，然后采用之前讨论过的碎片化处理方案。

## 11.4 And if the constraint on the integer is extensible? 11.4 那么，如果对整数的限制是可以扩展的呢？

There is nothing new or unexpected here. The principles of encoding extensible types have been discussed already. 这里没有任何新内容或意外之处。关于编码可扩展类型的原理，已经有过讨论过了。

But let's have some examples: 不过，让我们来看一些例子吧：

It's just the usual one bit up-front, a constrained encoding if in the root, and an unconstrained encoding otherwise. 这只是通常情况下的预付费用而已：在根节点时采用有限制的编码方式，而在其他情况下则采用无限制的编码方式。

```txt
integer13 INTEGER (MIN .. 65535, ..., 65536 .. 4294967296) ::= 127, 65536
integer14 INTEGER (-1..MAX, ..., -20..0) ::= 4096, -8
integer15 INTEGER (3..6, ..., 7, 8) ::= 3, 4, 5, 6, 7, 8
integer16 INTEGER (1..65538, ..., 65539) ::= 1, 257, 65538, 65539 
```

will encode as (the "extensions bit" has "E:" placed before it for clarity): 将会被编码为（为了清晰起见，将“扩展位”前面的位置放置了“E：”）：

```txt
integer13: E:0 L:P00000001 C:0111111,
E:1 L:P00000011 C:00000001 00000000 00000000
integer14: E:0 L:P00000010 C:00010000 00000001,
E:1 L:P00000001 C:11111000
integer15: E:0 C:00, E:0 C:01, E:0 C:10, E:0 C:11,
E:1 L:P00000001 C:00000101,
E:1 L:P00000001 C:00001000
integer16: (UNALIGNED) E:0 0 00000000 00000000,
E:0 0 00000001 00000001,
E:0 1 00000000 00000001,
E:1 L:00000011 C:00000001 00000000 0000010
(ALIGNED) E:0 L:00 C:P0000000,
E:0 L:01 C:P0000001 0000000,
E:1 L:12 C:P2P2P2P2P2P2P2P2P2P2P2P2P2P2P2P2P2P2P2P2P2P2P2P2P2P2P2P2P2P2P2P2P2P2P2P2P2P2P2P2P2P2P2P2P2P2P2 
```

OK - Now you know it all! It is not difficult, but there are a lot of cases to remember. Come back BER! All the other types are much more straightforward! No doubt you will want to write notes on this lot, and hope that your examination is an Open Book examination! But by now (if you got this far!) you should certainly have a very good understanding of the principles involved in the PER encodings. 好了——现在你们已经了解了一切！这并不难，不过有很多情况需要记住。回头再讨论吧！其他类型的问题则简单得多！毫无疑问，你们会想要记录下这些内容的要点，并希望考试能采用开卷方式！不过到现在为止（如果你已经读到了这里），你应该已经对 PER 编码所涉及的原则有了很好的理解了。

## 12 Encoding ENUMERATED values. 12. 对枚举值进行编码处理。

First we consider the encoding of an enumerated type that is not marked extensible (and remember, the encoding of an extensible type for a value that is in the root is just the same except that it is preceded by an extensions bit set to zero). Encoding of enumerations outside of the root are covered later. 首先，我们考虑那些未被标记为可扩展的枚举类型的编码问题。记住，对于根节点中的可扩展类型来说，其编码方式与普通类型相同，只不过在编码之前会有一个被设置为零的“可扩展”标志。关于根节点之外类型的编码问题，我们将在后面讨论。

The numerical value associated with an enumeration is always bounded above and below. Moreover, it is possible to order the enumerations into ascending order (even if some have negative associated values), and then to re-number each enumeration from zero upwards. 与某个枚举值相关的数值总是存在上下限的约束。此外，还可以按照升序对这些枚举值进行排序（即使某些枚举值的数值为负），然后重新为每个枚举值分配一个从零开始的新编号。

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/54379e17-c034-430b-894c-f77661f731e5/0162e80d544493a88338e4c69663891f03283a7cc5d2fbaab118b4ede1015f52.jpg)

This gives us a compact set of integer values (called the enumeration index) with a lower and an upper bound. Any value of the enumerated type now encodes like the corresponding constrained integer. 这为我们提供了一组有限的整数值（称为枚举索引），该索引有下限和上限。现在，任何枚举类型的值都像对应的受限整数一样被编码了。

In principle, all possible constrained integer encodings are possible, but in practice, definitions of enumerated types never have more than a few tens of enumerations - usually much less, so we are essentially encoding the enumeration index into a bit-field of size equal to the minimum necessary to cope with the range of the index. 原则上，所有可能的受限整数编码都是可能的。但实际上，枚举类型的定义通常只有几十种枚举值而已——通常数量要少得多。因此，我们实际上是将枚举索引编码到一个固定大小的位字段中，这个字段的大小至少要能够满足枚举值的取值范围需求。

If the enumeration is extensible, then enumerations outside the root are again sorted by their associated numerical value, and are given their own enumeration index starting at zero again. (Remember, the extensions bit identifies whether an encoded value is a root one or not, so there is no ambiguity, and starting again at zero keeps the index values as small as possible). For a value outside the root, the encoding is the encoding of the enumeration index as a "normally small nonnegative whole number" described earlier. 如果枚举是可扩展的，那么根之外的元素将按照其对应的数值进行排序，并且会赋予它们各自的枚举索引，该索引从零开始。记住，扩展位用于标识一个编码值是否为根值，因此不会存在歧义；从零开始设置索引值可以确保索引值尽可能小。对于根之外的元素，编码方式就是之前描述的那种将枚举索引编码为“通常较小的非负整数”的方式。

No doubt you want some examples! Here goes (with a way-out example first!) - and again we use commas to separate lists of values and of encodings, for brevity: 毫无疑问，您想要一些例子吧！那么，让我们开始吧（先举一个例子！）——同样，为了简洁起见，我们使用逗号来分隔各种值和编码方式列表：

```txt
enum1 ENUMERATED {red(-6), blue(20), green(-8)}
    ::= red, blue, green
enum2 ENUMERATED {red, blue, green, ..., yellow, purple}
    ::= red, yellow, purple

These encode as:

enum1: C:01, C:10, C:00
enum2: E:0 C:00,
E:1 C:0000000, (These are the "normally small"
E:1 C:0000001 encodings of zero and one.
Note the absence of a "P")

If we had more than 63 extension additions .... No! I am not going to give an example for that. It won't happen! Produce your own example! (You have been told enough to be able do it). 
```

## 13 Encoding length determinants of strings etc 13. 字符串编码长度的确定因素等

The "etc" in the heading of this clause refers to iteration counts in SEQUENCE OF and SET OF. 本条款标题中的“等”指的是在“序列”和“集合”中的迭代次数。

Remember that for iteration counts, the length determinant encodes the number of iterations, for the length of bitstrings it encodes the number of bits, for the length of knownmultiplier character strings it encodes the number of abstract characters, and for everything else it encodes the number of octets. 记住，对于迭代次数的编码，长度确定器会表示迭代的次数；对于位字符串的长度，该确定器则表示位的数量；对于已知乘数字符字符串的长度，该确定器则表示抽象字符的数量；而对于其他所有情况，该确定器则表示八位元的数量。

<table><tbody><tr><td data-imt-p="1">A length determinant which is constrained by an effective size constraint encodes in exactly the same way that an integer with an equivalent constraint would encode (well, almost - read the details below if you wish!). 一种受有效尺寸限制的长度确定器，其编码方式与受类似限制的整数相同（不过，如果你愿意，可以仔细阅读下面的详细说明哦！）。</td></tr></tbody></table>

A length determinant can, however, have values which are constrained by an effective size constraint, and in many ways we can view this as similar to the situation when an integer value (a count) is constrained by a direct constraint on the integer. 然而，长度参数的值可能受到有效大小限制的影响。从许多角度来看，这种情况类似于整数值（即计数）受到整数本身直接限制的情况。

Note that we are here talking only about lengths of strings or iteration counts - the form of the length determinant for integer values has been fully dealt with (and illustrated) earlier. We have also discussed earlier the general case of a length determinant where there are no PER-visible size constraints. So in this clause we are talking only about the case where there is an effective size constraint, and as in earlier clauses, we consider first the case of a constraint without an extension marker (which also applies to encoding counts within the root if there is an extension marker). 请注意，我们在这里讨论的只是字符串的长度或迭代次数而已。对于整数值的长度判定形式，我们已经在之前进行了全面讨论和说明。此外，我们之前也探讨了在没有 PER 可见大小限制的情况下使用长度判定的一般情况。因此，在本段内容中，我们仅讨论存在有效大小限制的情况。就像之前一样，我们首先考虑的是没有扩展标记的情况（如果存在扩展标记，这种情况也适用于根节点内的编码次数）。

The discussion of length encodings for strings etc has been deliberately delayed until after the description of integer encodings was given, and the reader may like to review that description before reading on. 关于字符串等内容的长度编码的讨论，我们特意推迟到先介绍整数编码的相关内容之后再进行讨论。读者在阅读后续内容之前，或许可以先回顾一下关于整数编码的描述部分。

A length or iteration count is basically an integer value, except that it is always bounded below (by zero if no other lower bound is specified), so if we need to encode the lengths of strings, we can draw on the concepts (and the text!) used to describe the encoding of values of the integer type. For a semi-constrained count (no upper bound), it would be pointless to encode a semi-constrained integer value (with its "length of length" encoding), and instead a general length determinant as described in Clause 8 is encoded. 长度或迭代次数本质上是一个整数值，只不过这个值的下限总是有规定的（如果没有指定其他下限的话，那么下限就是 0）。因此，当我们需要编码字符串的长度时，就可以借鉴那些用于描述整数类型值编码的概念和文本。对于具有半限制性限制的情况（即没有上限），那么对具有“长度”特性的半限制性整数值进行编码是没有意义的，相反，应该像第 8 条所描述的那样，使用通用的长度表示方式来编码。

For a constrained count, where the count is restricted to a single value (a fixed length string, for example, or a fixed number of iterations in a sequence-of), then there is no length determinant - we simply encode the contents. Otherwise, we need a length determinant. 当计数受到限制时，即计数被限定在单一数值上（例如，一个固定长度的字符串，或者在一个序列中固定次数的迭代），那么就没有必要设定长度了——我们只需编码内容本身即可。否则，我们就需要一个用于确定长度的因素。

For a constrained count, the count is encoded (in both the ALIGNED and UNALIGNED versions) exactly like the encoding of a corresponding constrained integer, except where the maximum allowed count exceeds 64K. In this latter case the constraint is ignored for purposes of encoding, and a general length determinant is used, with fragmentation into 64K hunks (as described in Clause 8) if the actual value has more than 64K bits, octets, iterations, or abstract characters. 在有限制的计数情况下，计数信息会被编码处理（包括 ALIGNED 和 UNALIGNED 两种版本），其编码方式与相应的有限制整数类型的编码方式完全相同。不过，当允许的最大计数超过 64K 时，这种限制会被忽略，此时会采用通用的长度确定方法来进行编码。如果实际值的位数超过 64K 比特、八位元、迭代次数或抽象字符数，那么就会将数值分割成 64K 的片段进行编码，具体方法请参考第 8 条说明。

Finally, we need to consider an extensible constraint. If the effective size constraint makes the type extensible, then the general provisions for encoding extensible types discussed earlier apply to the type as a whole - we don't encode an extensible integer for the length determinant. So we get the extensions bit up-front saying whether the count (and any other aspect of the value, such as the alphabet used) is in the root, and if so we encode the count according to the size constraint on the root. If not, then the extensions bit is set to one and a general length determinant is used. 最后，我们需要考虑一种可扩展的约束条件。如果有效大小约束使得类型具有可扩展性，那么之前讨论过的关于编码可扩展类型的一般规定也适用于整个类型——我们不会为长度决定因素编码一个可扩展的整数。因此，我们会提前设置一个扩展位，用来表明数值的计数方式（以及该数值的其他特性，如使用的字母表）是否属于可扩展类型。如果是这种情况，我们就根据根类型的尺寸约束来编码计数信息。如果不是这种情况，那么就会设置扩展位为 1，并使用一般的长度决定因素来表示数值。

So to summarise: 总结一下：

• With no PER-visible size constraint, or a constraint that allows counts in excess of 64K, we encode a general length determinant. • 由于没有 PER 可见性的尺寸限制，也没有允许计数超过 64K 的约束条件，因此我们引入了一个通用长度决定因素来进行编码。

• For abstract values outside the root, a general length determinant is again used. • 对于根之外的抽象值，仍然使用了一个通用的长度确定因素。

With a size constraint that gives a fixed value for the count, there is no length determinant encoding. 由于尺寸限制，计数值是一个固定的数值，因此不存在用于编码长度的因素。

• Otherwise, we encode the count exactly like an integer with the equivalent constraint. • 否则，我们就会像处理整数一样来编码这个计数，同时遵循类似的约束条件。

We illustrate this with some IA5String examples, but remember that the same length determinant encodings also apply to iteration counts etc. In the examples you will see "P" for padding bits in the contents. These are a consequence of the main type being IA5String with more than two characters, and would not be present if we had used BIT STRING for the examples (or if we had an IA5String whose length was restricted to at most two characters - see later). Where padding bits are shown in the length determinant, these would be present for all types. We give the E: and L: fields in binary, but the C: fields in hexadecimal, for brevity. 我们通过一些 IA5String 示例来说明这一点。不过请注意，相同长度的确定编码也适用于迭代次数等数值。在示例中，你会看到内容中有“P”表示填充位。这是当主类型是一个包含超过两个字符的 IA5String 时的必然结果；如果我们使用 BIT STRING 来表示示例，或者如果 IA5String 的长度被限制为最多两个字符，那么就不会出现这种情况——稍后会有相关说明。在确定长度时，如果显示了填充位，那么所有类型都会包含这些位。我们以二进制形式表示 E:和 L:字段，而 C:字段则使用十六进制表示，以简化表达。

If the reader wants some exercise, then try writing down the encodings of each value before reading the answers that follow! (For very long strings, we indicate the contents with the count in characters in brackets, and do the same when giving the encoding). 如果读者想要练习一下，那么可以在阅读后续答案之前，先写下每个值的编码方式！对于非常长的字符串，我们会用字符数来表示长度，在给出编码时也会采用同样的表示方法。

With the following value definitions: 根据以下数值定义：

```txt
string1 IA5String (SIZE (6)) ::= "012345"
string2 IA5String (SIZE (5..20)) ::= "0123456"
string3 IA5String (SIZE (MIN..7)) ::= "abc"
string4 IA5String ::= "ABCDEFGH"
string5 IA5String (SIZE (0..7, ..., 8)) ::= "abc", "abcdefgh"
string6 IA5String (SIZE (65534..65535)) ::= "(65534 chars)"
string7 IA5String (SIZE (65537)) ::= "(65537 chars)" 
```

we get the following encodings (using hex or binary as appropriate): 我们得到以下编码方式（使用十六进制或二进制表示，根据具体情况选择）：

```yaml
string1: C:P303132333435
string2: L:0001 C:P30313233343536
string3: L:011 C:P616263
string4: L:P00001000 C:4142434445464748
string5: L:011 C:P616263,
    L:P00001000 C:6162636465666768
string6: L:0 C:(65534 octets)
string7: L:P11000100 C:(65536 octets) L:P00000001 C:(1 octet) 
```

## 14 Encoding character string values. 14. 编码字符串值。

## 14.1 Bits per character 14.1 每个字符的位数

We have discussed above the encoding of the lengths of strings. To recap, the length determinant gives the count of the number of abstract characters for the "known multiplier" character string types, and of octets for the other character string types. 我们在上文已经讨论了字符串长度的编码问题。总结一下，长度确定器能够计算出“已知乘数”类型的字符字符串所对应的抽象字符的数量，以及其他类型的字符字符串所对应的八位元数量。

In the case of the known multiplier character string types, the number of bits used in the encoding of the UNALIGNED variants of PER is the minimum needed to represent each character unambiguously. For the ALIGNED versions, the number of bits for each character is rounded up to a power of two (one, two, four, eight, sixteen, etc), to ensure that octet alignment is not lost between characters. 对于已知的乘法器字符字符串类型，PER 的未对齐版本在编码过程中所使用的位数，是能够唯一表示每个字符所需的最少位数。而对于对齐版本，每个字符所需的位数会被向上取整，成为 2 的幂次形式（1、2、4、8、16 等），这样可以确保在不同字符之间不会出现八位组对齐的问题。

<table><tbody><tr><td data-imt-p="1">Encoding of known multiplier character strings uses the minimum number of bits for each character, except that in the ALIGNED variants this number is rounded up to a power of two, to avoid losing alignment. 对于已知的乘法因子字符串，编码时会使用每个字符所需的最少位数。不过，在 ALIGNED 版本中，这个数值会被向上取整到 2 的幂次，以避免影响数据的对齐效果。</td></tr></tbody></table>

The known multiplier types, with the number of characters that the unconstrained type is defined to contain (and the number you need to exclude to improve the encoding in the UNALIGNED variants) are: 已知的乘数类型包括：无约束类型所定义的字符数量（以及为了改善 UNALIGNED 变体的编码而需要排除的字符数量）。

<table><tbody><tr><td data-imt-p="1">Type name 输入名称</td><td data-imt-p="1">Number of chars 字符数量</td><td data-imt-p="1">Number of reductions needed for better encoding 为了实现更好的编码效果，需要进行的压缩次数。</td></tr><tr><td data-imt-p="1" data-imt_insert_failed_reason="same_text">IA5String</td><td data-imt-p="1">128 characters 128 个字符</td><td>64</td></tr><tr><td data-imt-p="1">PrintableString 可打印的字符串</td><td data-imt-p="1">74 characters 74 个字符</td><td>10</td></tr><tr><td data-imt-p="1">VisibleString 可见字符串</td><td data-imt-p="1">95 characters 95 个字符</td><td>31</td></tr><tr><td data-imt-p="1">NumericString 数字字符串</td><td data-imt-p="1">11 characters 11 个角色</td><td>3</td></tr><tr><td data-imt-p="1">UniversalString 通用字符串</td><td data-imt-p="1">2**32 characters 2**32 个字符</td><td>2**31</td></tr><tr><td data-imt-p="1">BMPString BMP 字符串</td><td data-imt-p="1">2**16 characters 2**16 个字符</td><td>2**15</td></tr></tbody></table>

For all other character string types, the length determinant gives the count in octets, because the number of octets used to represent each character can vary for different characters. In this latter case, constraints are not PER-visible, and the encoding of each character is that specified by the base specification, is outside the scope of this chapter, and is the same as for BER. 对于其他所有字符串类型，长度确定器以八位元数来表示长度，因为表示每个字符所需的八位元数可能会因字符类型而异。在这种情况下，这些限制并非与可读性相关，每个字符的编码方式遵循基础规范的规定，这超出了本章的讨论范围，与 BER 编码方式相同。

All that remains is to discuss the encoding of each character in the known multiplier character string types, as the encoding of these characters is affected by the effective alphabet constraint (see Clause 6), and to see when octet-aligned fields are or are not used for character string encodings. Again we see differences between the ALIGNED and the UNALIGNED variants, but the encodings are what you would probably expect, or have invented yourself! 现在剩下的工作就是讨论已知的多重字符字符串类型中每个字符的编码方式。这些字符的编码方式会受到有效字母表限制的影响（详见第 6 条）。此外，还需要确定在字符字符串编码时是否使用了按八位对齐的字段。我们再次看到了“按八位对齐”与“不按八位对齐”这两种编码方式之间的区别。不过，这些编码方式其实都是人们预期中的结果，或者可以说是人们自己发明出来的结果吧！

Each of the known multiplier characters string types has a canonical order defined for the characters, based on the numerical value in the BER encoding (the ASCII value for IA5String, 所有已知的乘法字符字符串类型都有相应的规范顺序，这一顺序是基于 BER 编码中的数值信息来确定的（对于 IA5String 字符，其 ASCII 值即为该顺序）。

PrintableString, VisibleString, and NumericString, the UNICODE value for BMPString, and the ISO 10646 32-bit value for characters outside the Basic Multi-lingual Plane for UniversalString). These values are used to provide a canonical order of characters. The values used to encode each character are determined by assigning the value zero to the first abstract character permitted by the effective alphabet constraint, one to the second, etc. The last value used is n-1 if there are n abstract characters permitted for the type (using only PER-visible constraints in this determination). There are a minimum number of bits needed to encode the value n-1 as a positive integer, and in the UNALIGNED variants, this is exactly the number of bits used to encode each character. For example: 可打印字符串、可见字符串以及数字字符串。对于 BMP 字符串，使用 UNICODE 编码；而对于通用字符串中不属于基本多语言平面的字符，则使用 ISO 10646 标准的 32 位编码。这些编码方式用于规定字符的规范顺序。每个字符的编码值是通过将有效字母表约束所允许的第一个抽象字符的值设为 0，第二个抽象字符的值设为 1，依此类推来确定的。如果该类型允许使用 n 个抽象字符，那么最后一个使用的编码值就是 n-1。将 n-1 作为正整数进行编码所需的最小位数为固定不变的，而在 UNALIGNED 变体中，这正好就是每个字符的编码所需使用的位数。例如：

$$
\begin{array}{l l} \text {Type definition} & \text {No of bits per char} \\ \text {My - chars1}: := \text {IA5String (FROM ("T"))} & \text {Zero} \\ \text {My - chars2}: := \text {IA5String (FROM ("TF"))} & \text {One} \\ \text {My - chars2}: := \text {UniversalString (FROM ("01"))} & \text {One} \\ \text {My - chars2}: := \text {NumericString (FROM ("01234567")} & \text {Three} \end{array}
$$

Note that in the above, the actual base type being constrained could be any of the known-multiplier character string types, and the result would actually be just the same encoding! You effectively design your own character set, and PER then assigns an efficient encoding for each character. 请注意，在上述示例中，实际被限制的基础类型可以是任何已知的乘数字符串类型。而结果实际上都只是相同的编码方式而已！你实际上是在自己设计一种字符集，然后 PER 为每个字符分配一个高效的编码方式。

For the ALIGNED variants, the number of bits used is always rounded up to a power of two - zero, one, two, four, eight, sixteen, thirty-two, to ensure that octet alignment is not lost within the string. 对于对齐版本，所使用的位数总是向上取整到 2 的幂次——即 0、1、2、4、8、16、32 等，以确保字符串内的八位组能够保持对齐状态。

There is one small exception to this mapping of values to new values for encoding. The original set of characters have associated values with some "holes" in the middle (in general). If remapping the original values to a compact range from zero to n-1 does not produce a reduction in the number of bits per character in the PER encoding (for whichever variant is in use), then the remapping is not done, and the original associated value is used in the encoding. In practice, this means that remapping is more likely for UNALIGNED PER than for ALIGNED PER (where the number of bits per character is always a power of two), except in the case of NumericString, where the presence of "space" means that for both variants (even with no constraints), remapping takes place, reducing the encoding to a maximum of four bits per character. 在将值映射到新值进行编码的过程中，有一个小小的例外情况。原始字符集中存在一些“空位”，这些空位在中间位置。如果重新映射原始值到一个更紧凑的区间，即从零到 n-1，并不会导致 PER 编码中每个字符所需的位数减少，那么就不进行重新映射，而是继续使用原始对应的值进行编码。实际上，对于 UNALIGNED PER 来说，重新映射的可能性更大，因为对于 ALIGNED PER 来说，每个字符所需的位数总是 2 的幂次。不过，在 NumericString 的情况下，由于存在“空格”字符，无论是否受到任何限制，都会进行重新映射，从而将每个字符的编码位数限制在最多 4 位以内。

So with: 所以，使用以下方法：

 

$$
\text { My - Boolean }:: := \text { IA5STRING (FROM ("TF"))(SIZE(1))}
$$

The encoding would be a single bit in a bit-field (with no length encoding) - in other words, it would be identical to the encoding of a BOOLEAN! 这种编码方式相当于在一个位字段中存储单个比特位（无需进行长度编码），换句话说，它和 BOOLEAN 类型的数据的编码方式是完全相同的！

## 14.2 Padding bits 14.2 填充位

When do we get padding bits in the ALIGNED case? Here we need to look at the combination of the effective size constraint (which restricts the number of abstract characters in every value) and the effective alphabet constraint (which determines the number of bits used to encode each character). If the combination of these is 在 ALIGNED 情况下，我们什么时候能得到填充位呢？这里我们需要考虑有效大小限制（这决定了每个值中抽象字符的数量）和有效字母表限制（这决定了编码每个字符所使用的位数）。如果这两种限制的组合满足……

<table><tbody><tr><td data-imt-p="1">No padding if the size is constrained so that an encoded string value never exceeds 16 bits. 如果尺寸有限，那么就不会使用填充字符；这样编码后的字符串长度就不会超过 16 位。</td></tr></tbody></table>

such that the total encoding size for a value of this constrained type can never exceed sixteen bits, then there are no padding bits. The character string value is encoded into a bit-field. If, however, there are some values which might require more than 16 bits, then the encoding is into an octetaligned bit-field, and no character will cross an octet boundary (in the ALIGNED case). 这样，对于这种受限类型的值，总的编码大小永远不会超过十六位比特。因此，不需要使用填充位。字符字符串的值会被编码到一个位字段中。然而，如果有些值需要超过 16 位比特来编码，那么编码方式就会改为使用八位对齐的位字段，这样就不会有字符跨越八位边界了（在对齐的情况下）。

Some examples of character strings whose encodings do not produce padding bits: 以下是一些字符串示例，它们的编码方式不会产生填充位：

```autohotkey
String1 ::= NumericString (SIZE (0..4))
String2 ::= IA5String (FROM ("TF")) (SIZE (0..16))
String3 ::= IA5String (SIZE (0..2))
String4 ::= BMPString (SIZE (0..1)) 
```

Again, this rule of "16 bits" maximum is another example of PER being pragmatic. The limit could just as well have been set at 32, or 64 bits. The philosophy is that for short strings we do not want to force alignment, but that for long strings doing alignment at the start of the string (and then maintaining it) is on balance the best decision. 再次，这种“最多 16 位”的规定也是 PER 务实决策的一个例子。这个限制完全可以设定为 32 位或 64 位。我们的理念是，对于较短的字符串，我们不希望强制进行对齐；而对于较长的字符串，在字符串开头进行对齐，并且之后保持这种对齐方式，总体来看是更好的选择。

## 14.3 Extensible character string types 14.3 可扩展的字符字符串类型

The encoding of an extensible (by PER-visible constraints) known-multiplier character string type follows the normal pattern - an extensions bit set to zero if in the root, one otherwise, then the optimised encoding described above for root values, and an encoding of the unconstrained type (with a general length determinant) if we are not in the root. (Note, however, That mapping of associated values to produce a 4-bit encoding still occurs for an unconstrained NumericString). 这种可扩展的已知乘数字符字符串类型的编码遵循常规模式——如果处于根节点，则扩展位被设置为零；否则，采用上述针对根节点优化的编码方式。如果我们不在根节点上，则采用无约束类型的编码方式（具有通用的长度确定因素）。不过，需要注意的是，对于无约束的 NumericString 类型，仍然会进行相关值的映射，以生成 4 位的编码。

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/54379e17-c034-430b-894c-f77661f731e5/036face1d9860911dd5c4c8ac01b23548d783d02d4c9e661e274195a7cdc4441.jpg)

All the above applies only to the known-multiplier types. For the other character string types, there is never an extensions bit, the general encoding always applies for all values. 以上所述仅适用于已知乘数类型。对于其他字符串类型，根本不存在扩展位的概念，因为对于所有值来说，都适用同样的编码方式。

Finally, note that there is no concern in determining encodings of whether a known-multiplier type is extensible for alphabet or for size constraints. All that matters is whether or not PER-visible constraints make it extensible, and what the effective alphabet and effective size constraints for the root then are. The encoding is totally determined by that. 最后，需要指出的是，在确定已知乘数类型是否可扩展时，并不需要考虑字母表的大小限制。真正重要的是：PER 可见性约束是否使得该类型具有可扩展性，以及根节点的有效字母表大小限制是多少。编码方式完全取决于这些因素。

## 15 Encoding SEQUENCE and SET values. 15. 对序列和集合值进行编码。

For a SEQUENCE without an extension marker, earlier text (Clause 9) has described the encoding. There is up-front a preamble (encoded as a bit-field, not octet-aligned), with one bit for each element that is OPTIONAL or DEFAULT, set to one if there is an encoding present for a value of that element, to zero otherwise. Then there is simply the encoding for each element. 对于没有扩展标记的序列，之前的文本已经描述了编码方式。首先有一个前置部分（以位字段的形式编码，而不是按八位对齐），其中每个可选或默认的元素都有一个对应的位，如果该元素有编码存在，则该位设为 1；否则设为 0。之后就是每个元素的编码部分了。

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/54379e17-c034-430b-894c-f77661f731e5/5b1a4731eebf31875fcd51aada444fd1533380bd73bfc414709aba0e882c8a80.jpg)

We have also discussed earlier the use of tags to provide a canonical order for the elements of a SET, which then encodes in exactly the same way as a SEQUENCE. 我们之前还讨论过使用标签来为集合中的元素提供规范的排序方式，这种排序方式与序列的编码方式是完全相同的。

We are left in this clause to discuss when/whether values equal to a DEFAULT value are required to be present, or required to be absent, or whether we have an encoder's option. We also need to discuss the way extension additions are encoded. 在这一条款中，我们需要讨论的是：是否要求某些值必须存在，或者必须不存在；以及是否允许编码器自行选择这些值的存在或不存在。我们还需要讨论扩展信息的编码方式。

But first, let's have an example of encoding a value of a simple sequence type. The example is shown in Figure III-26 and the encoding in Figure III-27. The OPTIONAL/DEFAULT bit-map is preceded by "B:", contents by "C:", length determinant by "L:", and one or more padding bits by "P", as in earlier examples. 不过，首先让我们来看一个对简单序列类型的值进行编码的示例。该示例如图 III-26 所示，而编码过程则如图 III-27 所示。像之前的例子一样，OPTIONAL/DEFAULT 位图之前有一个“B:”，内容部分用“C:”表示，长度确定用“L:”来标识，此外还有一个或多个填充位，用“P”来表示。

```txt
my-sequence-val
SEQUENCE
{item-code INTEGER (0..254),
item-name IA5String (SIZE (3..10))OPTIONAL,
urgency ENUMERATED
{normal, high} DEFAULT normal }
::= {item-code 29, item-name "SHERRY"} 
```

```txt
B:10 (item-name present, urgency missing)
C:00011011 (value of item-code)
L:011 C:P534845525259 (length and value of item-name)

Figure III-27 Encoding of the sequence value 
```

It is worth noting that the total length of this PER encoding is seven octets. In BER (assuming the encoder takes the option of encoding default values and always using a 3-octet definite length field, both on the grounds of simplicity), we get a total of 24 octets. If the encoder is more bandwidth conscious and omits the encoding of the default value and uses short definite lengths (which suffice in this case), BER will produce 13 octets. 值得注意的是，这种 PER 编码的总长度共有七个八位组。而在 BER 编码中（假设编码器选择默认值的编码方式，并且始终使用三个八位组来表示固定长度字段，这样更简洁），总长度为 24 个八位组。如果编码器更加注重带宽效率，省略了默认值的编码处理，而采用较短的固定长度字段表示数据，那么 BER 编码将只需要 13 个八位组即可。

## 15.1 Encoding DEFAULT values 15.1 编码 默认值

Here we find some differences between CANONICAL-PER (which is fully canonical), and BASIC-PER (which has encoder's options in complex cases that rarely arise). 在这里，我们发现了两种方式之间的某些差异：一种是“标准模式”（完全符合规范），另一种则是“基础模式”（在极少数情况下允许使用编码器提供的选项）。

For both encoding rules, if the actual value to be encoded equals the default value for "simple types" (defined as anything that is not a SET, SEQUENCE, SET OF, SEQUENCE OF, CHOICE, EMBEDDED PDV, EXTERNAL or unrestricted character string type, then the encoder is required to omit the encoding in both CANONICAL-PER and in BASIC-PER (both are canonical). 对于这两种编码规则，如果待编码的实际值等于“简单类型”的默认值（即那些不属于 SET、SEQUENCE、SET OF、SEQUENCE OF、CHOICE、EMBEDDED PDV、EXTERNAL 或不受限制字符字符串类型的类型），那么编码器需要在 CANONICAL-P 和 BASIC-PER 两种规范中都不进行编码操作（这两种规范都是标准的规范）。

However, for the types listed above, CANONICAL-PER again requires omission if the value equals the default value, but BASIC-PER leave it as an encoder's option, making it unnecessary to do a possibly complex run-time check for equality of a value with the DEFAULT value. 不过，对于上述列出的类型，如果值等于默认值，那么再次需要忽略该值。但是，对于 BASIC-PER 类型，可以将此选项作为编码器的选项来处理，这样就无需进行可能复杂的运行时检查来判断值是否与默认值相等了。

## 15.2 Encoding extension additions 15.2 编码扩展添加

The general principles of encoding extensible types applies: we have an extensions bit up front (before the bit-map of OPTIONAL or DEFAULT elements) which is set to zero if the abstract value is in the root, one otherwise. 扩展类型的编码基本原则同样适用：我们预先定义了一个扩展位（位于 OPTIONAL 或 DEFAULT 元素的位图之前），如果抽象值在根节点中，则该位设为 0；否则就设为 1。

Extension additions tend in practice to be marked OPTIONAL (or DEFAULT), but this is not a requirement. If in Version 2, one addition was not so marked, then Version 2 systems would always have to encode additions, and would always have the extensions bit set to one. Only version 1 systems would set it to zero. 在实际使用中，这些扩展项通常被标记为“可选”或“默认选项”。不过，这并不是强制要求。如果在版本 2 中某个扩展项没有被标记为可选，那么版本 2 的系统必须始终对该扩展项进行编码处理，并且扩展标志始终会被设置为 1。只有版本 1 的系统才会将其设置为 0。

Values for extension additions are always encoded at the position of the insertion point, and a decoder expects such encodings if the extensions bit is set to 1, not otherwise. 扩展添加的值总是被编码在插入点的位置。如果扩展位被设置为 1，那么解码器就会期望看到这种编码方式；否则就不会如此了。

First, we must recap about extension additions in a SEQUENCE. These may be either a single element (called an extension addition type), or a group of elements contained in version brackets (called an extension addition group). 首先，我们需要回顾一下在序列中如何进行扩展添加操作。这些扩展添加可以是单个元素（称为扩展添加类型），也可以是一组包含在版本括号中的元素（称为扩展添加组）。

The easiest way to describe the handling of an extensions addition group (and the way it is described in the specification), is for the reader to mentally replace the entire group of elements and the version brackets with a single OPTIONAL SEQUENCE, whose elements are the elements of the addition group. There is just one rider: if all elements of the group are to be omitted in the encoding (they are all marked OPTIONAL or DEFAULT), then there is no encoding for the entire SEQUENCE, and the outer-most OPTIONAL bit-map would record its absence. (An example of this is given later). 描述扩展加法群的处理方式（以及规范中对该方式的描述）最简单的方法，是让读者在脑海中将整个元素集和那些版本括号替换为单一的“可选序列”。这个序列的元素就是加法群中的元素。不过有一个例外：如果编码过程中需要省略该群的所有元素（因为它们都被标记为“可选”或“默认”），那么整个序列就不会被编码，而最外层的“可选”标志则用于表示这一情况。（稍后会给出一个示例。）

We have now reduced the problem to a simple list of extension addition types, some or all of which may be marked OPTIONAL, and hence may be missing in an encoding. As with elements in the root, a decoder needs to know which elements are present in the encoding, and which are not, and once again a bit-map is used. The problem in this case, however, is that Version 1 systems will not know how many extension addition types there are in the specification, and hence will not know the length of the bit-map. Moreover, such systems will not know whether an extension addition type was marked optional or not. This produces two differences from the bit-map used for the root elements: 我们现在将问题简化为一组简单的扩展加法类型列表。其中一些类型可能被标记为“可选项”，因此可能在编码过程中缺失。就像在根元素中一样，解码器需要知道编码中哪些元素存在，哪些不存在。同样，这里也会使用位图来表示这些信息。不过，问题在于，第 1 版系统并不清楚规范中到底包含了多少种扩展加法类型，因此也无法确定位图的长度。此外，这些系统也无法判断某个扩展加法类型是被标记为“可选项”还是其他情况。这就使得与根元素相关的位图存在两个方面的差异：

• The bit-map contains one bit for every extension addition type, whether it is marked optional or not, recording its presence or absence in the encoding. • 该位图结构中，每种扩展添加类型都对应一个位位。这些位可以标记为可选，也可以不标记，以此来表明该扩展类型在编码中的存在与否。

• The bit-map is preceded by a count giving the number of bits in the bit-map. • 位图之前有一个数字，表示位图中的位数。

The count for the bit-map length is encoded as a normally small whole number. 位图长度的计算结果被编码成一个较小的整数。

The effect of encoding the count as a normally small whole number is that there is again provision for fragmenting the extension additions bit-map into 64K fragments if the number of extension additions exceeds 64K. With the presence of version brackets, where additions are unlikely to occur at less than about one year intervals, a "not supported" response from a tool would be wholly appropriate! 将计数编码为较小的整数，这样做的好处是，如果扩展附加的位数超过了 64K，那么就可以将这部分数据分割成 64K 的片段。考虑到版本间隔通常约为一年，因此当工具返回“不支持”的响应时，这种处理方式是完全合理的。

Following the bit-map, we encode the value of the extension addition types, but in this case a Version 1 system does not know the actual types involved, and would not be able to find the end of the encoding of an extension addition, so each of the extension addition types is "wrapped up" with a preceding length determinant. The situation is slightly worse than this, however. What should the length determinant count, given that the decoder does not know the type that is wrapped up? Clearly the only possibility is bits or octets, and octets was chosen. 在处理位图之后，我们会对扩展加法类型的值进行编码。不过，在版本 1 的系统中，系统并不知晓实际涉及的类型，因此无法确定扩展加法编码的结束位置。因此，每种扩展加法类型都被一个长度指示符“包裹”了起来。不过，情况其实比这更糟糕一些。考虑到解码器并不知晓被“包裹”的类型，那么长度指示符的数量应该是多少呢？显然，唯一的可能性就是比特或八位字节，而这里选择了八位字节作为长度指示符。

So each extension addition type is treated as if it were an outer- level type being encoded. If it is present, but has zero bits (not likely to arise - a NULL, for example), then it encodes to a one-bit. It then has zero padding bits added at the end to make it up to an integral number of octets and is then added to the encoding preceded by a general length determinant (which, remember, is octet aligned). 因此，每种扩展加法类型都被视为一种被编码的外层类型。如果某个类型存在，但其中的位数为零（这种情况不太可能发生，例如 NULL 的情况），那么这种类型就会被编码为一个一位的二进制值。之后，会在该类型末尾添加零个填充位，以使其总位数达到一个完整的八位组，然后再将其添加到编码中，同时还会包含一个通用长度指示符（记住，这个指示符是以八位组为单位对齐的）。

This "wrapping up" then can be quite expensive on bandwidth, and it was for this reason (mainly) that "version brackets" were introduced. Because all the elements in a version bracket encode (optimally) as the elements of an OPTIONAL SEQUENCE which is treated as a single extension addition, we get only one "wrapper" instead of one for each element. 这种“封装”过程可能会消耗大量的带宽资源，因此才主要引入了“版本括号”机制。因为在一个版本括号中，所有元素都被优化地编码为可选序列的元素，而这些可选序列则被视作单一的扩展项。这样一来，我们只需一个“封装器”来处理所有元素，而不是对每个元素都分别进行封装。

```txt
my-sequence-val
SEQUENCE
{item-code INTEGER (0..254),
item-name IA5String (SIZE (3..10))OPTIONAL,
... !1 -- see para 14.6 for exception handling --,
urgency ENUMERATED {normal, high} DEFAULT normal,
[[ alternate-item-code INTEGER (0..254),
alternate-item-name IA5String (SIZE (3..10))OPTIONAL ]] }
::= {item-code 29, item-name "SHERRY",
urgency high, alternate-item-code 45,
alternate-item-name "PORT" }
Figure III:28: An extended sequence value for encoding 
```

The "wrapping up" also has a significant implementation cost, in that it requires the complete encoding (or at least the first 64K octets thereof) of the extension addition to be produced and any necessary padding bits inserted, before the length wrapper count is known and can be encoded. (This is similar to the problem of the use of the long definite form in BER to encode the length of a SEQUENCE, rather than the indefinite form). There is, however, no alternative to this wrapping up if we want interworking between Version 2 and Version 1 systems (unless we go back to a TLV approach for everything). 这种“封装”过程还伴随着较高的实施成本，因为需要完整地编码扩展项（或者至少是前 64K 个八位组），并插入必要的填充位，只有这样，才能确定长度并对其进行编码。（这类似于在 BER 中使用长定义形式来编码 SEQUENCE 的长度的问题，而不是使用不定形式。）不过，如果我们希望版本 2 和版本 1 的系统能够相互协作，那么除了采用 TLV 方法处理所有情况之外，没有其他可行的办法。

```txt
E:1 (extensions bit SET)
B:1 (item-name present)
C:00011011 (value of item-code)
L:011 C:P534845525259 (length and value of item-name)
L:000010 B:11 (length - normally small whole number and value of extensions bit-map)
L:P0000001 C:10000000 (general length and padded value of urgency)
L:P00000011 (general length of version bracket addition)
C:00101101 (alternate-item-code)
L:001 C:P504F5254 (length and value of alternate-item-name) 
```

Figure III-29: The encoding of the extended sequence value 图 III-29：扩展序列值的编码方式

Now for an example of encoding an extensible SEQUENCE with one extension addition type and one extension addition group added. (We base this on the earlier sequence type example.) Figure III-28 shows the value to be encoded, and Figure III-29 shows the encoding (the notation used is the same as in earlier examples of encodings). 现在我们来举个例子，说明如何对一个可扩展的 SEQUENCE 进行编码。在这个例子中，我们只增加了一个扩展类型和一个扩展组。（我们的做法基于之前提到的序列类型示例。）图 III-28 展示了需要编码的数据内容，而图 III-29 则展示了编码方式（所使用的符号与之前示例中的相同）。

This gives a total of 18 octets. Again, if we take the worst case BER encoding as described earlier, this gives 37 octets, and the best case gives 25. 总共需要 18 个八位元。再次强调，如果采用之前描述的最差情况 BER 编码方式，那么所需的数据量将达到 37 个八位元；而使用最佳编码方式的话，所需数据量则降至 25 个八位元。

## 16 Encoding CHOICE values. 16. 编码 CHOICE 值。

The encoding of choice indexes for both root alternatives and for those outside the root has been fully described earlier. The only remaining point to note is that here, as for sequence, if the chosen alternative is outside the root a Version 1 system will not be able to find the end of it, so we again have a "wrapper", encoded in exactly the same way as extension additions in a SEQUENCE or SET. 关于根选项以及那些位于根选项之外的选项的编码方式，之前已经详细描述了。现在需要注意的一点是：在这里，就像在序列中一样，如果选择的选项位于根选项之外，那么版本 1 的系统将无法找到该选项的末端。因此，我们再次需要一个“包装器”来对其进行编码，这种编码方式与在序列或集合中对扩展项的编码方式完全相同。

Here we give one example of each of these cases. 在这里，我们为每个案例提供了一个示例。

Note that version brackets are permitted in choice type extensions, but they do not affect the encoding, and serve purely as a documentation aid for humans. What matters is simply the list of added alternatives, each of which must have distinct outer-level tags, even if they are in different version brackets. 请注意，在选项扩展中允许使用版本括号，但它们不会影响编码方式，仅仅是为了方便人类理解而设计的文档辅助工具。重要的是要列出所有不同的选项，每个选项都必须拥有独特的外部标签，即使它们属于不同的版本括号。

The values to be encoded are shown in Figure III-30 (assume an environment of automatic tags) and the encodings are shown in Figure III-31, where "I:" is used to introduce the choice index encoding. 需要编码的值如图 III-30 所示（假设处于自动标签环境），而编码方式则如图 III-31 所示。在图 III-31 中，“I：”用于引入选择索引编码方式。

```txt
Choice-example ::= CHOICE
{normal NULL,
high NULL,
... !2 -- see para 14.6 for exception handling --
medium NULL }

first-choice Choice-example ::= normal:NULL
second-choice Choice-example ::= medium:NULL

Figure III-30: Two choice values for encoding 
```

```txt
first-choice: E:0 I:0 C: (a total of two bits)
second-choice: E:1 (extensions bit set)
C:000000 (index as a normally small
whole number)
L:P00000001 (general length "wrapper")
C:00000000 (padded encoding of NULL)

Figure III-31: The encodings of the choice values 
```

In this example, worst case BER encodes with four octets in both cases, and best-case BER with two octets. PER took three octets in the second. This is just one of a small number of cases where PER can actually produce worse encodings than BER, but this is not often the case! 在这个示例中，最坏情况下的 BER 编码需要四个八位元来表示数据，而最佳情况下的 BER 编码则只需要两个八位元。在第二种情况下，PER 则使用了三个八位元来表示数据。这种情况只是少数几个当中，PER 所生成的编码可能比 BER 更差的情况之一；不过这种情况并不常见！

## 17 Encoding SEQUENCE OF and SET OF values. 17. 编码序列与数值集合。

There is nothing more to add here. There is a length determinant upfront giving the iteration count. The form of this (depending on any SIZE constraint on the SEQUENCE OF or SET OF) has been fully discussed earlier. 这里没有更多需要补充的内容了。前面有一个明确标注的变量，用于指示迭代次数。关于这种形式的讨论已经在前文中充分阐述过了，具体形式取决于对“序列”或“集合”的 SIZE 约束条件。

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/54379e17-c034-430b-894c-f77661f731e5/a49acbd3f7ab7df30215c675dfe690ed1ecdec71d1809905760ab0a825962d83.jpg)

Note that these types may have a SIZE constraint in which there is an extension marker. As usual, values outside the root encode as if there were no size constraint. 请注意，这些类型可能存在一个“大小限制”，即存在扩展标记的情况。和往常一样，超出根节点范围的值会被编码为没有大小限制的情况。

Two examples are shown in Figures III-32 and III-33. The numbers have been kept deliberately small for ease of illustration. Note that in the example both the iteration count and the type being iterated are extensible. For a value of the SEQUENCE OF to be in its root only requires the iteration count to be within the root. The fact that the integer value 4 is outside the root of the INTEGER in the third iteration is flagged in the encoding of the INTEGER, and does not affect the extensions bit for the SEQUENCE OF. 在图 III-32 和图 III-33 中展示了两个示例。这些数字被刻意设计得较小，以便于图示说明。请注意，在这两个示例中，迭代次数和迭代的类型都是可扩展的。对于“SEQUENCE OF”的值来说，只需确保迭代次数在根值范围内即可。在第三次迭代时，整数值 4 超出了“INTEGER”的根值范围，这一点在“INTEGER”的编码中得到了标记，但这并不影响“SEQUENCE OF”的扩展功能。

My-sequence-of SEQUENCE (SIZE(1..4), ..., 4) OF INTEGER (0..3, ..., 4) 我的序列序列（长度由 1 到 4 个整数决定，范围为 0 到 3，共 4 个整数）

My-value-1 My-sequence-of ::= {1, 3, 4} 我的值 1，我的序列为：{1, 3, 4}

My-value-2 My-sequence-of ::= {1, 2, 3, 4} 我的值 2 我的序列为：{1, 2, 3, 4}

Figure III-32: Two SEQUENCE OF values for encoding 图 III-32：用于编码的两种数值序列

```lisp
My-value-1:
E:0 (extensions bit)
L:10 (iteration count of 3)
E:0 C:01 (value 1)
E:0 C:11 (value 3)
E:1 L:P0000001 C:00000100 (value 4)
My-value-2:
E:1 (extensions bit)
L:P00000011 (iteration count of 4)
E:0 C:01 (value 1)
E:0 C:10 (value 2)
E:0 C:11 (value 3)
E:1 L:P00000001 C:00000100 (value 4) 
```

Figure III-33: The encodings of the two SEQUENCE OF values 图 III-33：两个值序列的编码方式

## 18 Encoding REAL and OBJECT IDENTIFIER values. 18. 对 REAL 类型和 OBJECT IDENTIFIER 类型的值进行编码处理。

The box says it all! We have a general length determinant giving a count in octets, then for REAL (for both BASIC-PER and CANONICAL-PER) the contents octets of the CER/DER encoding of REAL (they are the same). For OBJECT IDENTIFIER encodings, the specification actually references the BER encoding, but the CER/DER encodings are exactly the same. 这个盒子已经说明了一切！它提供了一个通用长度确定器，以八位元为单位表示长度。而对于真正的（无论是基本长度还是标准长度）情况，REAL 类型的 CER/DER 编码中的内容八位元数值也是相同的。对于 OBJECT IDENTIFIER 编码，规范实际上引用了 BER 编码，但 CER/DER 编码与 BER 编码是完全一致的。

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/54379e17-c034-430b-894c-f77661f731e5/da5ed63c22643aebe78dba69c293ba1f5b0703e97187376d539cf0313eb768d6.jpg)

## 19 Encoding an Open Type 19. 对开放类型进行编码

We have discussed the form of an outer-level encoding, and of a general length determinant to provide a "wrapper" for extensions in sequence and set and choice types. Exactly the same mechanism is used to wrap up an Open Type (a "hole" that can contain any ASN.1 type). In general, the field of the protocol which tells a decoder what type has been encoded 我们已经讨论了外部级编码的形式，以及用于描述序列、集合和选择类型中扩展信息的通用长度指示符。同样的机制也被用来对开放类型进行封装——即一个可以容纳任何 ASN.1 类型的“容器”。一般来说，协议中负责告知解码器所编码类型信息的字段就是这种封装机制的一部分。

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/54379e17-c034-430b-894c-f77661f731e5/7972b18a98ccce91d4c3806b63e47767d268e588eddd3cd41930d4303ed457fb.jpg)

into the "hole" - into the Open Type field, may appear later in the encoding than that field, but with PER a decoder will be unable to find the end of the encoding in the "hole" without knowing the type. (Contrast BER, where there is a standard TLV wrapper at the outer level of all types, and where no additional wrapper is needed nor used). So in PER the wrapper is essential in the general case, and is always encoded. 进入“hole”这个字段后，该字段可能会在编码中出现，但使用 PER 编码方式时，解码器将无法在“hole”中找到编码的结尾，除非知道该字段的类型。与 BER 不同，在 BER 中，所有类型都有一个标准的 TLV 封装层，因此不需要或不会使用额外的封装层。所以，在 PER 编码方式中，封装层是必不可少的，并且总是会被编码进去的。

The inclusion of a wrapper in PER Open Types has been exploited by some applications to "wrap-up" parts of an encoding, even tho' it is not strictly necessary to do so. 在 PER Open Types 中加入了包装器功能后，一些应用程序利用这一特性来“封装”编码的某些部分。不过，虽然这样做并非绝对必要，但确实有一些应用采用了这种做法。

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/54379e17-c034-430b-894c-f77661f731e5/f85c1dc0b626565b62d37b4ad8ae076378de45b34c32a256462e15bb304f4ad4.jpg)

Consider an element of a large SEQUENCE consisting of: 考虑一个由多个元素构成的巨大序列：

## security-data SECURITY-TYPES.&Type (Type1) 安全数据 安全类型。类型 1

This is an example of a "type constraint" on an Open Type, and the reader was referred to this clause for an explanation of its usefulness. 这是一个关于“类型约束”的例子，其中提到了这个条款，以说明其重要性。读者可以参考该条款来了解其具体含义。

From the point of view of abstract values, this is exactly equivalent to: 从抽象价值的角度来看，这完全等同于：

## security-data Type1 安全数据 类型 1

The PER encoding, however, will have a wrapper round Type1 in the first case, not in the second (type constraints are not PER-visible). 不过，在第一种情况下，PER 编码会包含一个 Type1 的包装轮次；而在第二种情况下则不会（因为类型约束并不适用于 PER）。

This can be useful in an implementation, because it enables the main body of the protocol to be dealt with in an application-specific way, leaving the security data unwrapped and unprocessed, passing it as a complete package to some common "security kernel" in the implementation. 这在实现中非常有用，因为它使得协议的核心部分能够以特定于应用程序的方式进行处理，而安全相关数据则保持原样，未经处理，作为一个完整的包被传递给实现中的某个通用“安全核心”模块。

It is generally only in the security field that specifiers use these sorts of construct. 通常，只有在安全领域才会使用这种表述方式。

## 20 Encoding of the remaining types 20. 其余类型的编码处理

GeneralizedTime, UTCTime, ObjectDescriptor, all encode with a general length determinant giving an octet count, and contents the same as BER or CER (for BASIC-PER and CANONICAL-PER respectively). Notice that this is the fourth occurrence where BASIC-PER is not canonical, in the interests of simplicity - the other three are: GeneralizedTime、UTCTime、ObjectDescriptor 这些类型都使用一种通用的长度确定方法来编码，该方法会返回一个八位元的数值。这些类型的内容与 BER 或 CER 相同（分别用于 BASIC-PER 和 CANONICAL-PER）。需要注意的是，这是第四次出现 BASIC-PER 不是规范化的情况了。出于简洁性的考虑，其他三次情况都是如此。

```txt
At last! The final clause describing PER encodings. I wish this book was a Web site, so that I could see how many people had read all the way to here! Well done those of you that made it! 
```

• Encoding values of a set-of type. • 对某一类型集合中的值进行编码。

• Encoding GeneralString and related character string types. • 对 GeneralString 及相关字符字符串类型进行编码处理。

• Encoding a DEFAULT element (which is not a simple type) in a sequence or set type. • 在序列或集合类型中编码一个“DEFAULT”元素（该元素并非简单的类型）。

Canonical PER is, of course, always canonical. 当然，典型的 PER 始终都是具有规范性的。

That just leaves types which are defined using the "ValueSetTypeAssignment" notation, that is, notation such as: 这样就只剩下那些使用“ValueSetTypeAssignment”表示法来定义的类型了，比如这样的表示法：

```txt
MyInt1 INTEGER ::= { 3 | 4 | 7}
MyReal1 REAL ::= {0 | PLUS-INFINITY | MINUS-INFINITY} 
```

These are equivalent to: 这些相当于：

```txt
MyInt2 ::= INTEGER (3 | 4 | 7)
MyReal2 ::= REAL (0 | PLUS-INFINITY | MINUS-INFINITY) 
```

Initially the PER standard overlooked the specification of these types, but a Corrigendum was issued saying that they encode using this transformation. 最初，PER 标准没有考虑到这些类型的规范问题。不过后来发布了一个修正说明，指出这些类型确实使用了这种变换来进行编码。

## 21 Conclusion 21 结论

In a chapter like this, it seems important to emphasise that neither the author nor any of those involved in publishing this material can in any way be held liable for errors within the text. 在这样一个章节中，重要的是要强调：无论是作者还是参与出版此材料的任何人，都不应对文本中的错误负责。

Caveat Emptor! 小心，买家啊！

The only authoritative definition of PER encodings is that specified in the Standards/Recommendations themselves, and anyone undertaking implementations should base their work on those primary documents, not on this tutorial text. 关于 PER 编码的唯一定义，就是标准/建议文件中所规定的内容。任何负责实现该编码的人都应该以这些主要文件为参考，而不是依赖本教程中的内容。

Nonetheless, it is hoped that this text will have been useful, and will help implementors to more readily read and to understand the actual specifications. 不过，希望这篇文本能够起到作用，帮助实施者更轻松地阅读和理解具体的技术要求。

The reader should now have a good grasp of the principles used in PER to provide optimum encodings, but tempered by pragmatic decisions to avoid unnecessary implementation complexity. 现在，读者应该已经很好地理解了在 PER 中用于实现最佳编码的原理了。不过，这些原理的实现过程中也考虑到了实际可行性，以避免不必要的实现复杂性。

Some things may appear to be unnecessarily complex, such as fragmenting bit-maps if they are more than 64K, or encoding zero bits if an INTEGER is restricted to a single value, as such things will never occur in the real world. These specifications, however, result from applying a general principle (and general code in an implementation) to a wider range of circumstances, and are not extra implementation complexity. 有些情况看起来可能过于复杂了，比如当位图的大小超过 64K 时，就需要将其分割开来；或者当某个整数值只能取单一值时，就需要对零位进行编码。不过，这些情况其实并不存在于现实世界中。这些规范之所以存在，是因为我们将一个通用原则（以及在实现过程中使用的通用代码）应用到更广泛的情况中，而这些规范本身并不构成额外的实现复杂性。

We have also seen in the examples how PER encodings achieve significant gains over BER in verbosity, and even greater gains if sensible use of constraints has been made in the base specification. 在示例中，我们看到了 PER 编码在信息量方面比 BER 有显著的优势，而如果在基础规范中合理地使用约束条件，那么这种优势会更加明显。

There is just one more chapter to come in this section (very much shorter than this one!). That discusses some other encoding rules that never quite made it (or have not yet made it!) to becoming International standards, and the advantages and (mainly) disadvantages of "rolling your own" encoding rules. 这一节还有一章内容即将介绍（不过这一章要短得多！）。那一章会讨论一些其他编码规则，这些规则至今未能成为国际标准，同时也会探讨“自行制定编码规则”的优势以及主要缺点。

# Chapter 4 Other ASN.1-related encoding rules 第四章 其他与 ASN.1 相关的编码规则

(Or: So you have special requirements?) （或者：那么您有一些特殊的要求吗？）

## Summary: 总结：

This chapter briefly describes other proposals for ASN.1 encoding rules that have been made from time to time. None of these are currently on a path for International Standardization as part of the ASN.1 specifications, and this chapter can safely be omitted by all but the intellectually curious. It is of no interest to most readers concerned with "What is ASN.1, how do I write it, and how do I implement protocols defined using it." But it does give an (incomplete) picture of other attempts to enhance the ASN.1 notation with different encoding rules. 本章简要介绍了一些关于 ASN.1 编码规则的提议。不过，这些提议目前都未能成为 ASN.1 规范中的国际标准，因此除了那些感兴趣的人之外，其他人可以不必关注这些内容。对于那些只关心“什么是 ASN.1、如何编写 ASN.1 代码以及如何使用它来构建协议”的读者来说，这些内容并不重要。不过，这些章节确实提供了一些关于如何改进 ASN.1 表示法的其他尝试的概述（尽管并不完整）。

The order of coverage is not time order (saying when the germ of an idea first appeared within a sometimes closed community is not easy), but is basically random! The following are briefly mentioned: 这些内容的排序并非按照时间顺序进行的（也就是说，某个想法何时首次出现在一个有时较为封闭的社会群体中并不容易确定）。实际上，这些内容的排序基本上是随机的！以下简要提及一下：

• LWER - Light-Weight Encoding Rules • LWER – 轻量级编码规则

• MBER - Minimum Bit Encoding Rules • MBER – 最小位编码规则

• OER - Octet Encoding Rules • OER——八位组编码规则

• XER - XML (Extended Mark-up Language) Encoding Rules • XER - XML（扩展标记语言）编码规则

• BACnetER - BAC (Building Automation Committee) net Encoding Rules • BACnetER – BAC（楼宇自动化委员会）的编码规则

• Encoding Control Specifications (ECS) • 编码控制规范（ECS）

No doubt there are others lurking out there! 毫无疑问，还有其他人潜伏在那些地方！

## 1 Why do people suggest new encoding rules? 1. 为什么人们会提出新的编码规则呢？

As a basic work-horse, it is doubtful if BER can be bettered. It is simple, straight-forward, and robust. If you keep its basic "TLV" approach, there are few improvements that can be made. 作为一款基础型的工作用计算机，似乎已经没有什么改进的空间了。它的设计简单、直接且稳定。如果你保持其基本的“TLV”架构，那么基本上就不需要再进行任何改进了。

But it was clear in 1984 that it should be possible to encode more efficiently 不过，在 1984 年时已经明确，应该有可能更高效地进行编码了。

In the beginning there was chaos. And the greater Gods descended and each begat a new Standard, and the people worshipped the Standards and said "Give us more, give us more!" So the greater Gods begat more Standards and more and more, and lo, there was chaos once more! 起初，一切都是混乱的。然后，伟大的神祇们降临了，他们各自创造了新的标准。人们崇拜这些标准，不断祈求更多的标准。于是，伟大的神祇们又创造了更多的标准……然而，混乱再次降临了！

than BER, and several attempts were made prior to or around the time of the introduction of PER to produce essentially PER-like encodings. To avoid a proliferation of encoding rules, PER should have been developed and standardised in the late 1980s, not the early 1990s, but it wasn't! So several "industry-specific" encoding rules emerged to fill the vacuum. 在引入 PER 之前，以及在其推出前后，人们尝试了多次方法来创建类似 PER 的编码方式。为了避免编码规则的混乱，PER 本应在 20 世纪 80 年代末而不是 90 年代初被开发并标准化。但实际上并没有这样做！于是，各种针对特定行业的编码规则应运而生，以填补这一空白。

Currently, major tool vendors support only BER and PER. Support for other encoding rules for particular industry-specific protocols (supporting only the types used in those protocols, rather than all ASN.1 types) by a library of routines to perform specific parts of the encoding (not by an ASN.1 compiler, as defined and described in Section I Chapter 6) does however exist. 目前，大多数工具供应商仅支持 BER 和 PER 编码方式。不过，确实存在一些库程序，能够支持特定行业协议所需的其他编码规则（即仅处理这些协议中使用的类型，而不是所有 ASN.1 类型）。这些库程序通过执行特定的编码操作来实现对其他编码方式的支持，而不是像 ASN.1 编译器那样进行全面的编码处理，这一点在第六章第一节中有详细说明。

Producers of new encoding rules often claim either less verbosity on the line than BER, or greater simplicity than PER (or both!). 新编码规则的制定者通常声称，与 BER 相比，新规则在行数上要少得多；而与 PER 相比，新规则则更为简洁明了（或者两者兼具！）。

But to-date, the standardizers of ASN.1 have not considered any of the alternative encoding rule drafts that have been submitted to have sufficient merit to progress them as standards within the ASN.1 suite. 但迄今为止，ASN.1 的标准制定者们并未考虑那些被提交来的替代编码规则草案中有哪些具有足够的合理性，足以被采纳为 ASN.1 标准。

That is not to say that they are (for example), necessarily on balance inferior to PER - everyone accepts that if you started again with what you know now, PER could be improved - but providing another standard for encoding rules that was very similar to PER and only a marginal improvement on it would not make any sort of sense. Tool vendors would not want to support it, and of course existing implementations of protocols would have to be considered. The ASN.1 encoding rules have a high degree of inertia (the notation can be changed much more easily) because of the "bitson-the-line" that are flowing around the world every minute of every day. 这并不是说，它们必然不如 PER。毕竟，如果重新从现有的知识出发来开始工作，那么 PER 是可以得到改进的。但是，如果有一个与 PER 非常相似的编码规则标准，而且只是对 PER 有轻微的提升，那也是没有意义的。工具供应商不会愿意支持这样的标准，当然，也需要考虑现有的协议实现方式。ASN.1 的编码规则具有很高的惯性特性（因为这种规范可以很容易地被修改），因为每天每分钟都有大量的数据在全世界范围内传输。

Nonetheless, there continue to be attempts to provide slightly different encoding rules to support a particular protocol for a particular industry, usually proposed by some consultancy or software house associated with that industry, in the hope that those encoding rules will become the de facto standard for that industry. Such encoding rules rarely, however, achieve the market demand that leads to their incorporation in the main ASN.1 compiler tools, or ratification as international standards for ASN.1 encoding rules for use across all industries. 不过，仍然有一些人试图提出一些略有不同的编码规则，以支持特定行业中的特定协议。这些建议通常由与该行业相关的咨询公司或软件公司提出，希望这些编码规则能成为该行业的事实标准。然而，这样的编码规则很少能够满足市场需求，从而被纳入主要的 ASN 编译工具中，或者被批准为国际标准，以便在所有行业中使用。

It is, perhaps, a sign of the success of the ASN.1 notation that many industries new to protocol design are choosing to use ASN.1 to define their messages, but perhaps it is the NIH (Not Invented Here) factor that so often leads to desires to cut down the notation, or to produce different encodings for it. Who knows? 这或许正是 ASN.1 标记语言成功的一个标志——许多从事协议设计的行业都选择使用 ASN.1 来定义他们的消息格式。不过，也可能是因为“并非本土发明”的因素，人们往往希望简化这种标记语言，或者为其设计不同的编码方式。谁知道呢？

## 2 LWER - Light-Weight Encoding Rules 2 轻量级编码规则 – 低重编码规范

Light-Weight Encoding Rules were first proposed in the late 1980s when ASN.1 compilers started to emerge, and were from the beginning the subject of much controversy, with the Deutsches Institut für Normung (DIN) strenuously opposing their development as international standards. 轻量级编码规则最初是在 20 世纪 80 年代末提出的，当时 ASN.1 编译器开始出现。从一开始，这一规则就引发了诸多争议，德国标准协会（DIN）强烈反对将其发展为国际标准。

Standards work was approved, but was eventually abandoned - too many problems! 这些标准工作已经得到了批准，但最终还是被放弃了——存在的问题太多了！

Suggestions for LWER pre-dated work on PER, and the concern was not with the verbosity of BER, but with the number of CPU cycles required to do a BER encoding. They were approved as a Work Item within ISO, and were being progressed up to the mid-1990s, when they were abandoned (for reasons, see below). 这些关于 LWER 的建议早于对 PER 的研究，其重点并非 BER 的冗长性，而是进行 BER 编码所需的 CPU 周期数量。这些建议被作为工作项在 ISO 内部得到了批准，并一直推进到 20 世纪 90 年代中期，之后由于某些原因而被放弃了（具体原因见下文）。

## 2.1 The LWER approach 2.1 LWER 方法

The basic idea was simple, and was based on the observation that: 这个基本的想法很简单，其基于这样的观察：

An ASN.1 compiler generates the pattern for an in-core data structure to hold values of an ASN.1 type (it is usually a whole series of linked lists and pointers to similar structures), defining that in-core data structure using a high-level programming language. ASN 编译器会生成一种内部数据结构的数据模型，该模型用于存储 ASN 类型的值。通常，这种内部数据结构由一系列链接列表以及指向类似结构的指针组成。该数据模型是使用高级编程语言来定义的。

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/54379e17-c034-430b-894c-f77661f731e5/3d216ed7905ffd119dc76585153bb9a4701d2de3042028c52d724198d9f7865f.jpg)

• Run-time support tree-walks that structure to generate encodings (at some cost in CPU cycles) that are then transmitted down the line. • 在运行时支持树形结构，以生成编码结果（这需要一定的 CPU 周期开销），然后将这些编码结果沿着线路传输下去。

• A decoder reproduces a (very similar) in-core structure at the other end of the line. • 解码器能够在线路的另一端再现一个与原始结构非常相似的信号结构。

Why not simply ship the contents of the in-core data structure directly? That was in essence the LWER proposal. 为什么不直接将核心数据结构中包含的内容发送出去呢？这实际上就是 LWER 提案中的方案。

## 2.2 The way to proceed was agreed 2.2 后续的行动方案已经达成一致。

Early work agreed several key points: 早期的工作达成了几个关键共识：

<table><tbody><tr><td data-imt-p="1">Agree a standard in-core representation of ASN.1 values, and agree how to ship it to another machine. Easy. 同意采用标准化的内嵌方式来表示 ASN.1 值。同时也商量一下如何将其传输到另一台机器上。很简单而已。</td></tr></tbody></table>

• The first step was to agree a model of computer memory on which to base the definition of in-core data structures. • 第一步是就计算机内存的模型达成一致，这一模型将作为定义核心数据结构的依据。

• The second step was to standardise a memory-based in-core structure for holding the values of any ASN.1 type. • 第二步是标准化一种基于内存的核心结构，用于存储任何 ASN.1 类型的数值。

• The third step was to standardise how such a structure was to be transmitted to a remote system. • 第三步是标准化如何将这种结构传输到远程系统。

## 2.3 Problems, problems, problems 2.3 问题、问题、问题……太多了

Serious problems were encountered related to all these areas. 在所有这些领域都遇到了严重的问题。

As far as a model of computer memory was concerned, at assembler language level (which noone uses today anyway), memory is made up of addressable units capable of containing integers or pointers to other addressable units or strings of characters (a simplification, but it will do). But the size of those addressable units - bytes, 16-bit words, 32-bit words - hard-ware varies very much. 就计算机内存的模型而言，在汇编语言级别（如今已经很少有人使用这种语言了），内存是由一些可寻址的单元组成的，这些单元可以存储整数数据，或者指向其他可寻址单元或字符字符串的指针（这是一种简化的表示方式，但足够用了）。不过，这些可寻址单元的大小有所不同——可能是字节、16 位字、32 位字等。硬件层面上，这些单位的大小差异很大。

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/54379e17-c034-430b-894c-f77661f731e5/8755fa79eaa19aea40f0b25f400376ff62a0642cf0425aa66898979974fa414b.jpg)

And if a structure is defined using such a model, how easy will it be to replicate that structure using the features available in particular high level languages such as Java? 如果某个结构是通过这样的模型来定义的，那么使用像 Java 这样的高级编程语言所提供的功能来复制该结构将会多么容易呢？

More significant was the little-endian/big-endian problem. (Named after the characters in Jonathon Swift's Gulliver's travels who fought a war over whether eggs should be broken at their "little-end" or their "big-end"). But in computer parlance, you look at basic hardware architecture and proceed as follows: 更为重要的是“小端序/大端序”问题。这个问题得名于乔纳森·斯威夫特的《 Gulliver's Travels》中的角色们，他们为了争论鸡蛋应该以“小端”还是“大端”方式打开而发生了战争。但在计算机领域，我们通常会考虑硬件架构的基本规则，并按照以下方式来处理这个问题：

• Assume byte addressing, and draw a picture of your memory with two-byte integers in it. • 假设采用字节寻址方式，然后绘制出包含两个字节整数数据的内存结构图。

• Put an arrow on your picture from low addresses to high addresses. (Some people will have drawn the picture so that the arrow goes left-to right, others the reverse. This is not important, that only affects the depiction on paper.) • 在图片上画一个箭头，箭头应从较低的地址指向较高的地址方向。（有些人会画成箭头从左到右的方向，有些人则相反。这并不重要，因为只会影响图片在纸上的呈现效果。）

Now write down whether, for each integer, the first byte that you encounter in the direction of the arrow is the least significant octet of the integer (a little-endian machine) or the most significant octet of the integer (a big-endian machine). 现在请写下：对于每一个整数来说，在箭头所指的方向上，首先遇到的第一个字节是該整数的最低有效八位组（对于小端字节序的机器），还是最高有效八位组（对于大端字节序的机器）。

Little-endians will probably have drawn the arrow going left-to-right, and big-endians will probably have drawn it going right-to-left, but as said above, that is not important (both could have drawn a mirror image of their picture). What matters is whether the high-order octet of an integer is at a higher or lower address position than the low-order octet. And remember, what applies to integers also (invariably) applies to fields holding addresses (pointers). 那些持小端观点的人可能会将箭头画成从左到右的方向，而持大端观点的人则可能将其画成从右到左的方向。不过，如上所述，这并不重要（两种观点的人都可以画出自己图像的镜像版本）。真正重要的是，一个整数的最高八位字节是位于比最低八位字节更靠上的位置，还是更靠下的位置。记住，这一规则同样适用于存储地址的字段（即指针）。

Unfortunately, both big-endian and little-endian machines exist in the world! 不幸的是，世界上存在两种不同版本的机器：一种是大端序的，另一种是小端序的！

And if you have an in-core data structure representing an ASN.1 value on a little-endian machine, and you copy that to a big-endian machine, decoding it into a usable from will certainly not be light-weight! 如果你在一个小端序的机器上有一个表示 ASN.1 值的内部数据结构，然后将其复制到大端序的机器上，那么将其解码为可用的格式后，结果肯定不会是简洁的！

So we need a big-endian and a little-endian variant of LWER, and you will only be able to use LWER if you are transferring between similar (endian-wise) machines, otherwise you go back to BER or PER. 因此，我们需要两种版本的 LWER：一种采用大端序，另一种采用小端序。只有在使用具有相似端序的机器进行数据传输时，才能使用 LWER；否则，就只能回到使用 BER 或 PER 的方式了。

But that was all assuming machines with byte addressing, and 16-bit integers and pointers. Now consider the possible permutations of 32-bit integers, or machines that can only (easily) address (point to) 16-bit or 32-bit words ..... 不过，这一切都是建立在机器能够使用字节地址体系、处理 16 位整数以及指针的基础上。现在，让我们考虑一下 32 位整数的情况，或者那些只能轻松处理 16 位或 32 位字长的机器的情形吧……

Suddenly we seem to need rather a lot of variants of LWER! 似乎我们现在需要很多不同版本的 LWER 了！

This was the basic reason for the DIN opposition to the work - even if standards were produced, they would be useful only for transfers between very restricted families of machine architecture. And add the problems of mirroring those low-level memory-based architectures in high-level languages. Throw in the fact that tool-vendors can, if they wish, define an LWER (separate ones for each machine range that they support) to be used when their own tool is communicating with itself on the same machine range, and what do you get? Probably as much interworking as you would get with LWER! 这就是 DIN 反对这种工作的基本原因——即便能够制定出相关标准，这些标准也只适用于非常有限范围内的机器架构之间的数据传输。此外，将那些基于内存的低级架构移植到高级语言中还会带来许多问题。再加上，工具供应商可以在需要时定义自己的 LWER（针对他们支持的各个机器架构分别定义），以便在自己的工具在同一机器架构上相互通信时使用。那么，结果会是什么呢？很可能带来的互操作性还不如使用 LWER 时那么好吧！

What LWER demonstrated was the importance of defining encoding rules (be they character-based or binary-based) that were independent of any given machine architecture - the idea of having something like BER or PER was vindicated. (And of course character-based encodings are also architecture independent.) LWER 所证明的是：定义编码规则的重要性——无论是基于字符还是基于二进制的方式，这些规则都无需依赖于任何特定的机器架构。因此，像 BER 或 PER 这样的概念确实具有实用性。（当然，基于字符的编码方式同样也是与架构无关的。）

## 2.4 The demise of LWER 2.4 LWER 的终结

Even if the above problems were sorted, there were still issues about what to ship down the line. If the total memory the linked list structures occupied was shipped, empty memory within that total hunk would need to be zeroed 即使上述问题得到了解决，仍然存在关于如何分配内存分配的问题。如果链表结构所占用的总内存被全部发送出去，那么这部分空内存就需要被清零。

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/54379e17-c034-430b-894c-f77661f731e5/1b549f2399019d16c7d94ef47979b5ac3a79794f5db9fa58e8c22caf0b1096e8.jpg)

to prevent security leaks. If empty memory was not shipped, then some form of garbage collection or of tree-walking for transmission would be needed, none of which seemed very light-weight. 为了防止安全漏洞的出现，如果不存在空闲内存的话，那么就需要某种形式的垃圾收集机制或树遍历方式来传输数据。不过，这些方案似乎都并不灵活。

But what eventually killed the LWER work is something that nobody had expected. Implementations of PER began to emerge. Whilst it was expected that PER would produce about a factor of two reduction in the length of an encoding (it did), it was wholly unexpected that it would encode and decode twice as fast! It did the job that LWER was trying to do! 但最终导致 LWER 项目失败的是一件出乎意料的事情。PER 的实现开始出现。虽然人们预计 PER 会使编码长度减少大约两倍（实际上确实如此），但完全出乎意料的是，PER 的编码和解码速度竟然是原来的两倍！它确实完成了 LWER 试图实现的目标。

Once you know, it seems obvious. All the complexity and CPU cycles in PER relates to analyzing the type definition and deciding what the encoding should be. This is either a hand-implementors brain-cycles, or is the compiler phase of a tool. It does not affect run-time CPU cycles. 一旦你知道了，一切似乎都变得显而易见。PER 中所有的复杂性和 CPU 消耗都集中在分析类型定义以及决定采用的编码方式上。这要么是手工实现的开发者所经历的流程，要么就是某种编译器的处理过程。不过，这些都不会影响程序的运行时的 CPU 消耗时间。

At run-time, it is a lot quicker (assuming code has been generated) to pick-up an integer value from a known location, and add the bottom three bits (say) of that integer value to a bit-position in a buffer than it is to generate the T and the L and the V for BER (probably using subroutine calls). 在运行时，从已知位置获取一个整数值，然后将该整数的最后三位附加到缓冲区的某个位位置上，这种方式要快得多（前提是代码已经生成完毕）。相比之下，为了生成 BER 所需的 T、L 和 V 等参数，就需要调用多个子程序，这显然效率较低。

There were also gains because if you reduce the size of the encoding you reduce the CPU cycles spent in the code of the lower layers of the protocol stack. 此外，还有其他方面的好处：通过减小编码的规模，就可以减少协议栈底层代码中所需的 CPU 周期数。

And finally, LWER was conceived in the mid to late 1980s, but machines got faster year-by-year. Gradually the CPU cycles spent in encoding/decoding became insignificant and irrelevant (the application processing for actual protocols also became more complex and time-consuming by comparison). 最后，LWER 这一概念是在 20 世纪 80 年代中期到后期提出的。不过，随着时间的推移，计算机的性能越来越快。因此，用于编码/解码的 CPU 周期变得越来越不重要了（实际上，处理各种协议的应用程序也变得更加复杂，所需的时间也更多了）。

LWER was dead. Too many problems with developing it, and what it was trying to achieve seemed no longer necessary. It was finally abandoned in 1997. LWER 已经失效了。开发它存在太多问题，而且它原本想要实现的目标也变得不再重要了。最终，它在 1997 年被放弃了。

## 3 MBER - Minimum Bit Encoding Rules 3 月 1 日 - 最小位编码规则

MBER was proposed in about the mid-1980s, but was never approved for the Standards path. Many of its principles were, however, adopted when PER was produced. MBER 这一概念大约在 1980 年代中期被提出，但从未被批准用于标准规范中。不过，在 PER 标准制定时，其许多原则确实被采纳了。

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/54379e17-c034-430b-894c-f77661f731e5/2a5107d07616545bdc566a1bc43650a6eafa94ac014936e9d7d1adc51bfc9af5.jpg)

The idea behind MBER was to make full use of bounds information, and to produce encodings that were "what you would expect". MBER 背后的理念是充分利用边界信息，从而生成出“符合预期”的编码方式。

So a BOOLEAN would encode into one bit, and the type INTEGER (0..7) would encode into three bits. 因此，布尔类型会被编码为一位，而整数类型（0~7）则会被编码为三位比特。

MBER never addressed the encoding of all possible ASN.1 types (and in particular did not address the problems solved in PER by a choice index and a bit-map for OPTIONAL elements). MBER 从未处理过所有可能的 ASN.1 类型的编码问题（特别是没有解决在 PER 中通过选择索引和位图来处理 OPTIONAL 元素所遇到的那些问题）。

The main thrust of the MBER work was to make it possible to produce an ASN.1 definition of a type which, if MBER was applied to values of that type, would produce exactly and precisely the same bits on the line as some existing hand-crafted protocol was producing. MBER 工作的核心目标是实现一种 ASN.1 类型的定义。如果将该定义应用于该类型的各个值，那么生成的二进制位将会与某些现有的手工编写协议生成的二进制位完全一致且精确无误。

Typically, the aim was to move from protocol definitions using the techniques described in Section I Chapter 1 Clause 5.1 (pictures of octets) to ASN.1 specifications with no change to the bits on the line. 通常，我们的目标是从第 1 章第 5.1 节中描述的协议定义转向 ASN.1 规范，同时不会改变线路上的各个比特位。

(The reader may well ask "Why?", but this was a rather flattering recognition that use of the ASN.1 notation was quite a good (clear) way to describe the fields in a protocol message.) （读者可能会问：“为什么？”不过，这其实是一种相当赞赏的评价，表明使用 ASN.1 标记法来描述协议消息中的字段是一种非常有效且清晰的方法。）

MBER was never progressed internationally, but (as stated above), the idea of "minimum bit encodings" had a long-term influence and was included in PER. MBER 从未在国际上得到发展，但正如上文所述，“最小位编码”的概念产生了长期影响，并被纳入了 PER 中。

## 4 OER - Octet Encoding Rules 4. 八位组编码规则 – Octet Encoding Rules

At the time of writing this text, the future of OER is unclear, nor is its final form fully-determined. This text merely gives an outline of what this specification appears to the author to look like in the (very) late 1990s. 在撰写本文时，开放教育资源的发展前景尚不明朗，其最终形态也尚未确定。本文仅概述了作者认为这种规范在 20 世纪 90 年代末的样子。

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/54379e17-c034-430b-894c-f77661f731e5/009bacf74b54cd89910bb4abb2349eaabfac19d9fe95274d4f8cb8263f196efd.jpg)

It has been proposed as the encoding rules for a particular industry sector in the USA, and perhaps for international standardization for use with protocols in that sector. The industry sector is concerned with "intelligent highways". The sector is using ASN.1 to define protocols for communication between devices on the road-side and between them and control centres. In some cases the devices are large general-purpose computers (where BER or PER could certainly be easily handled). Some devices, however, will be more limited, and may not be able to handle the (alleged) complexity of PER, but where much of the efficiency of PER is required. 这一编码规则被提出用于美国某个特定行业领域，或许也可以用于国际标准化，以便与该领域的协议相结合。该行业领域关注的是“智能高速公路”系统。该领域使用 ASN.1 标准来定义道路两侧设备之间以及设备与控制中心之间通信的协议。在某些情况下，这些设备是大型通用计算机（在这种情况下，错误率或性能指标的问题可以轻松解决）。不过，也有一些设备的性能限制较多，可能无法处理性能指标所要求的复杂情况，但在需要大量提升性能的情况下，这种编码规则仍然非常有用。

(In relation to “alleged”, remember that all the complexity in PER is in the compile phase to analyze what the encoding should be. Once that is done, the actual encoding in PER is less code and simpler than in BER. Given a good cross-compiler system, even the simplest devices should be able to handle PER.) 关于“所谓的复杂性”，需要注意的是，PER 中的所有复杂性都存在于编译阶段，这一阶段负责分析编码方式。一旦编译完成，PER 中的实际编码方式就会比 BER 更简单、更简洁。只要拥有良好的跨编译器系统，即使是最简单的设备也能处理 PER 格式的数据。

OER was originally developed around the same time as PER, but in ignorance of the PER work (which was later folded into it). At the time of writing, it is a mix of BER (using BER length encodings) and PER. OER 最初的开发时间与 PER 几乎同时开始，但当时人们并未了解 PER 的相关研究成果（后来这些研究成果被整合到了 OER 中）。在撰写本文时，OER 实际上是由 BER 和 PER 混合而成的系统。

The name Octet-aligned Encoding Rules stems from the fact that all elements of an OER encoding have padding bits that make them an integral of eight bits. So INTEGER (0..7) will encode into eight bits (no tag, no length field), and BOOLEAN will encode into eight bits (no tag, no length field). “Octet-aligned Encoding Rules”这个名称的由来是因为 OER 编码中的所有元素都包含填充位，这些填充位使得每个元素都可以被表示为 8 位整数。因此，INTEGER 类型（0..7）会被编码为 8 位（没有标签，也没有长度字段）；而 BOOLEAN 类型则也会被编码为 8 位（同样没有标签，也没有长度字段）。

Apart from the use of BER-style length encodings, OER is very much like PER, but omits some of the optimisations of PER, producing a specification that is (arguably) simpler. 除了采用了 BER 风格的长度编码方式之外，OER 与 PER 非常相似，但省略了 PER 中的一些优化措施。因此，OER 的规范可以说更加简洁明了。

These encoding rules were considered by a joint meeting of the ISO/IEC and ITU-T ASN.1 groups in 1999, and the idea of providing a "FULLY-ALIGNED" version of PER received some support. This would in some ways complete the PER family, going along-side the existing UNALIGNED (no padding bits) and ALIGNED (padding bits where sensible) variants. 这些编码规则在 1999 年由 ISO/IEC 和 ITU-T ASN.1 小组的联合会议进行了讨论。提供“完全对齐”版本的 PER 得到了一些支持。这种方式可以在某种程度上完善 PER 系列标准，与现有的非对齐版本（没有填充位）和带有合理填充位的对齐版本相配合。

In discussion, it was felt that there was as yet insufficient customer demand to justify a "FULLY-ALIGNED" version of PER, and that in any case such a version of PER would not in fact be OER-compatible because of the multitude of differences (less optimization and use of BER features) between OER and PER. 在讨论中，人们认为目前客户的需求还不足以支持推出“完全兼容”版本的 PER。此外，由于 OER 和 PER 之间存在诸多差异（例如优化程度较低，且未充分利用 BER 功能），因此这样的 PER 版本实际上并不具备与 OER 兼容的能力。

At the time of writing, international standardization of OER is not being progressed within ASN.1 standardization. 在撰写本文时，OER 的国际标准化工作并未在 ASN.1 标准制定过程中得到推进。

## 5 XER - XML (Extended Mark-up Language) Encoding Rules 5 条 XER-XML（扩展标记语言）编码规则

XER is a relative new-comer (in 1999) to ASN.1 standardization. Work on it is proceeding with great rapidity through electronic mailing groups, and serious consideration of it will occur within ISO/IEC and ITU-T about a month after the text of this book is put to bed! The outcome of that discussion cannot be predicted with any accuracy, but I XER 是 1999 年才加入 ASN.1 标准规范的相对较新的标准。关于 XER 的工作正在通过电子邮件群组迅速进行着。而在 ISO/IEC 和 ITU-T 组织中，对 XER 的正式审议预计会在本书出版后大约一个月内进行。不过，这次讨论的结果目前还无法准确预测。

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/54379e17-c034-430b-894c-f77661f731e5/703e3c4eee00be3486a1405795b282c6066f10fa2418e70ec7689b102ae9c210.jpg)

have a sneaming feeling that any second edition of this book may contain a substantial section on XER! 感觉这本书的任何修订版都可能包含关于 XER 的详细内容呢！

Many readers will be aware that XML has a strong head of steam, and a lot of supporting tools. A marriage of XML with ASN.1 will undoubtedly be a good thing for both. But XER is VERY verbose! 许多读者都知道，XML 已经拥有了强大的发展势头，同时也有许多相关的工具来支持其应用。将 XML 与 ASN.1 结合起来使用，无疑会对双方都有好处。不过，XER 的语法实在过于冗长了！

XER is character-based, and carries XML start and end mark-up (tags which are usually the names of the elements of ASN.1 SEQUENCES or SETS or CHOICES, which are frequently very long) around ASN.1 items. XER 是一种基于字符的编码方式，它在 ASN 元素周围添加了 XML 格式的起始和结束标记（这些标签通常代表 ASN 序列或集合或选择项的名称，这些标签往往非常长）。

XER appears to hold out the promise of being able to send an XER encoding to a data-base system that has only been configured with a schema corresponding to the fields of an ASN.1 SEQUENCE, and to use code which is independent of the actual ASN.1 SEQUENCE definition (and which is part of the database vendor's software) to automatically insert the received values into the database. This may prove to be worth the price of the verbosity of XER (perhaps!). XER 似乎具有这样的潜力：它能够将 XER 编码发送到那些仅配置了与 ASN.1 序列中的字段相对应的模式的数据库系统。同时，XER 还能使用一种与 ASN.1 序列定义无关的编码方式，将接收到的数据自动插入到数据库中。也许，XER 的复杂性所带来的好处确实值得付出相应的代价吧！

## 6 BACnetER - BAC (Building Automation Committee) net Encoding Rules 6 BACnetER – BAC（楼宇自动化委员会）的编码规则

These encoding rules are quite old, and were a very honest attempt to produce PER before PER ever existed! They were never submitted to the ASN.1 group for international standardization, and have largely been over-taken by PER (but are still in use). 这些编码规则非常古老，它们是在“PER”出现之前所制定的，旨在尽可能准确地实现数据交换。这些规则从未提交给 ASN.1 标准组织进行国际标准化，现在大部分已经被“PER”标准所取代（不过这些规则仍然在继续使用）。

Perhaps one of the first industry sectors to decide to use ASN.1, but to also decide to "roll their own" encoding rules. 或许，第一个决定使用 ASN.1 标准的行业领域就是这个领域。不过，该领域还自行制定了自己的编码规则。

They are again an industry sector de facto standard in the USA for messages used in "intelligent buildings" (compare the discussion of "intelligent highways" above). 这在美国再次成为了“智能建筑”中使用的消息传递方式的行业标准（可以参考上文关于“智能高速公路”的讨论）。

BACnet encodings are used to control elevators, lights, central heating systems, and so on. BACnet 编码被用于控制电梯、照明系统、中央供暖系统等设备。

From a technical point of view, there are some ASN.1 constructs for which BACnetER does not provide unambiguous encodings, and they have no real advantage over the now standard PER, so it is unlikely (in the opinion of this author) that they will have further impact on the international scene. 从技术角度来看，有一些 ASN.1 结构在 BACnetER 中并没有得到明确的编码方式，而这些结构相对于现在标准的 PER 来说并没有真正的优势。因此，作者认为这些结构在国际领域中的影响可能性不大。

## 7 Encoding Control Specifications 7.编码控制规范

A very recent (1999) development in the work on ASN.1, largely resulting from consideration of requirements for variations of encoding rules such as OER, was the production of text for extensions to the ASN.1 notation called "Encoding Control Specifications". 在 ASN.1 领域，一项非常新的发展出现在 1999 年。这一发展的主要原因在于人们开始考虑各种编码规则的变化需求，比如输出规则。于是，人们开始编写关于 ASN.1 表示法扩展的文本，这些文本被称为“编码控制规范”。

<table><tbody><tr><td data-imt-p="1">If everyone is changing BER and PER, let's have a meta-language to formally specify the changes they want. Good idea? 如果大家都想要修改 BER 和 PER 的值，那么我们应该有一个统一的语言来正式指定他们想要进行的这些修改。这个想法不错吧？</td></tr></tbody></table>

The idea is that the definition of an Encoding Control Specification (using a notation very distinct from ASN.1) could be associated with an ASN.1 module in much the same way as a style-sheet can be associated with a page of HTML or XML. The Encoding Control Specification could vary the way certain types were encoded, selecting (for specified types or all types) PER or BER styles of length, including or omitting tags and/or padding bits, etc, etc. 这个概念的核心理念是：可以将编码控制规范的定义与一个 ASN.1 模块关联起来，就像将样式表与 HTML 或 XML 页面关联一样。编码控制规范可以改变某些类型的编码方式，例如选择适用于特定类型或所有类型的 PER 或 BER 编码方式，包括或排除标签和/或填充位等元素。

This work (1999) is very much in its infancy. Could the result be a meta-language (that a tool can be built to use) which is powerful enough that a suitable Encoding Control Specification could be applied to an ASN.1 module with the effect that types in that module are encoded with BACnetER or OER (or perhaps even XER) encodings? 这项研究工作（1999 年完成）仍处于初级阶段。有没有可能开发出一种强大的元语言，从而可以构建出实用的工具来使用它？这样一来，就可以将合适的编码控制规范应用于 ASN.1 模块中，使得该模块中的数据类型能够使用 BACnetER 或 OER 编码方式来表示，甚至可以使用 XER 编码方式也是如此。

This is broadly the aim of the work. But five years from now you may never have heard of it, and it may be as dead as LWER, or it may be supported by lots of tools and give important added flexibility to ASN.1. Don’t know! Get the second edition (if there is one!) of this book! (But it is not yet even a formally approved Work Item in ISO, so this stuff is just glints in the eye at present.) 这大致就是这项工作的目标。不过，五年之后，你可能再也不会听到关于它的消息了。也许它现在已经像 LWER 一样被遗忘，或者它可能会得到许多工具的支持，从而为 ASN.1 带来重要的灵活性提升。谁知道呢？那就去获取这本书的第二版吧（如果真的有第二版的话！）不过，目前这还不是一个正式被 ISO 认可的 Work Item，所以这些想法目前还只是些幻想而已。

## SECTION IV 第四部分

## History and Applications 历史与应用

# Chapter 1 The development of ASN.1 第 1 章 ASN.1 的发展

# (Or: The ramblings of an old man!) （或者：一个老人的絮絮叨叨！）

## Summary: 总结：

This chapter is somewhat different in style from the rest of the book. (This summary is not a list of bullets, for a start!) Whilst it does contain some facts, it is not so much a formal record of the stages and dates in the development of ASN.1 (Olivier Dubuisson's book is better for that – see the link via Appendix 5) as my own personal recollections of the various events that occurred along the way. 这一章的风格与其他章节有所不同。（这个总结并不是简单的要点列表！）虽然其中包含了一些事实，但它并不像奥利维尔·杜布伊松的书中那样，严格记录着 ASN.1 发展的各个阶段和日期——对于这方面内容，建议参考附录 5 中的链接。这一章更多的是我对过程中各种事件的个人回忆。

Unusually for an academic text, in this chapter I blatantly use the "I" personal pronoun in several sections. It seemed appropriate. 与学术文本通常使用的第三人称单数形式不同，在这一章中，我在多个段落中直接使用了“我”这个代词。这似乎是个合适的选择。

I was involved in ASN.1 almost from its earliest days (I think that only Jim White – I talk about Jim in the first clause of this chapter - can claim to have seen it through from its start, but he "retired" from Standards work in the late-1980s) through to the present day. I have been active in a number of areas of Standardization within ISO, but ASN.1 has probably taken up the largest part of my time because of its time-span (at the time of writing this text) of close on 20 years. 我参与 ASN.1 项目的时间几乎从它成立之初就开始了（不过，我觉得只有 Jim White——他在本章的第一段中提到了他——能够声称亲眼见证了 ASN.1 项目的成长过程。不过，Jim 在 1980 年代末从标准制定工作中退休了）。在 ISO 组织的多个标准化领域，我一直都很活跃，但 ASN.1 项目无疑占了我大量时间的重点。因为从撰写本文到现在，ASN.1 项目已经接近 20 年了。

There were many other people who gave a great deal of their time to the development of ASN.1, and if you list of some of them, you are in very great danger of being unfair to (and offending) those who just drop off the end of the list, but who nevertheless made important contributions to the work. There is no easy criterion on who to mention, and there are some of my past fellowworkers whose names I can no longer spell with accuracy, and have lost the attendance records! 还有许多其他人也投入了大量时间来推动 ASN1 项目的开发。如果你列出他们中的一些人的名字，那么就有可能对那些虽然排在名单末尾，但实际上对这项工作做出了重要贡献的人不公平。不过，要确定该提到谁并没有简单的标准。有些人的名字我已经记不清了，而且连他们的出勤记录也丢失了！

And, of course, there are the current participants in the ASN.1 work that seem larger than life simply because they are the current drivers. But I am ignoring most of them! I hope nobody takes offence at being left out. 当然，还有那些参与 ASN 工作的当前参与者们。他们看起来就像真实存在的人物一样重要，因为他们正是当前工作的推动者。不过，我其实并没有关注他们中的大多数人！希望没有人会因为被排除在外而感到不满吧。

The structure of this chapter is not a simple time-line. Rather, certain themes have been selected for the major sub-headings, but within those sub-headings the material is largely presented on a time-line basis. I hope that this will ensure rather more continuity in the text and easier reading than a pure time-line treatment, but the reader is advised that the major sub-headings are largely self-contained, and can be read (or skipped, or omitted) in a more or less random order depending on your interests. 这一章的结构并非简单的时间线排列。相反，我们选择了一些主题作为主要的子标题，而在这些子标题内部，内容基本上是按照时间顺序展开的。希望这样的安排能够确保文本的连贯性，并使其比单纯的时间线排列方式更易于阅读。不过，需要提醒读者的是，这些主要的子标题本身都是相对独立的，因此可以根据兴趣以任意顺序来阅读、跳过或忽略它们。

One major part of this chapter contains the history of the development of character encodings, that was promised in Section II Chapter 2. 这一章的一个重要部分讲述了字符编码发展的历史，这一内容曾在第二章第二节中有所提及。

## 1 People 1 个人

Jim White played an active part (perhaps a leading part - I am not sure) in the development of the Xerox Courier specification, on which ASN.1 was eventually based. 吉姆·怀特在 Xerox Courier 规范的开发过程中发挥了重要作用（或许还是主导者——我不确定）。而 ASN.1 规范正是基于 Xerox Courier 规范发展而来的。

## Let's get this one out of the way first! 我们先把这件事解决掉吧！

Courier was part of the "XNS" protocol stack. It represented, I think, the first recognition in protocol architecture of the value of providing a notation for the definition of protocol messages that was supported by well-defined encoding rules and tools within high-level language systems to enable users (not just computer vendors) to define their own protocols and to have an easy implementation path for those protocols. Courier 是“XNS”协议栈的一部分。我认为，这是协议架构中首次认识到提供一种用于定义协议消息的表示法的价值——这种表示法需要由定义明确的编码规则来支持，并且能够在高级语言系统中实现。这样一来，用户（而不仅仅是计算机供应商）就可以自行定义自己的协议，并且能够轻松实现这些协议。

Jim (as Rapporteur in CCITT responsible for developing notational support for the X.400 work) was largely responsible for bringing the Courier principles into international standardization and in due course for the production of X.409. 吉姆作为 CCITT 的报告员，负责为 X.400 标准开发相关的符号支持系统。他在这方面做出了重大贡献，使得 Courier 协议的原则得以纳入国际标准化体系。最终，X.409 标准也由此诞生了。

Doug Steedman was also very active within both CCITT and ISO in these early days, and was (I think) the first person to author a full-length tutorial text on ASN.1. This is still read today, but unfortunately was never updated to cover the work beyond 1990, as Doug also "retired" from Standards work in the late 1980s. 道格·斯蒂德曼在早期的 CCITT 和 ISO 组织中也非常活跃。他被认为是第一个编写关于 ASN.1 的完整教程的人。这部教程至今仍然被阅读，不过遗憾的是，由于道格在 1980 年代末从标准制定工作中退休，因此该教程并未再更新，以涵盖 1990 年之后的发展情况。

I was ISO Editor for the early ISO texts (and after X.409, CCITT texts were copies of the ISO texts). Bancroft Scott came onto the seen in the late 1980s, when (due to other "retirements"), I became Rapporteur for the ASN.1 work in ISO, and Bancroft, having volunteered to be Editor for one part of ASN.1, found himself Editor for all the different parts (now six parts in ISO and six corresponding ITU-T Recommendations), a role that he continues to occupy at the date of publication of this text (1999). 我曾是早期 ISO 标准的编辑人员（在 X.409 标准之后，CCITT 的标准实际上都是 ISO 标准的副本）。Bancroft Scott 在 20 世纪 80 年代末加入这个团队，那时由于其他人退休，我成为了 ISO 标准中 ASN.1 工作的负责人。Bancroft 自愿担任 ASN.1 中某一部分的编辑工作，之后他成为了所有相关部分的编辑——在 ISO 标准中共有六部分，而在 ITU-T 标准中也有六部分相应的建议。直到本文出版时（1999 年），他仍然担任这一职务。

In more recent years, Olivier Dubuisson has played a very active role in the development of ASN.1, and is the author of the second/third/fourth major book on ASN.1. (He can claim prior publication to this text with a French version of his book - making his the second text, but at the time of typing this I hope his English version will be later than this publication, making him also the fourth - but he could make third as well! Friendly rivalry!) 在近年来，奥利维尔·杜布伊松在 ASN.1 标准的开发过程中发挥了非常重要的作用。他也是关于 ASN.1 的第二、第三或第四本重要著作的作者。（他可以声称自己的这本书有法语版本，因此这本著作应该是他的第二本著作——不过在本文撰写时，希望他的英文版本能比这本出版物更早出版，这样他就可以成为第四位作者了！不过，他也可以成为第三位作者哦！真是充满友情的竞争啊！）

There are many, many, others that I could and perhaps should list, particularly colleagues in BSI that have provided much support for ASN.1 over the years, but then I should also mention colleagues operating within AFNOR and from Sweden, and colleagues in the USA that produced course material for ASN.1 that is still used throughout the world today, and ... 还有很多很多其他的人我可以而且或许应该列出他们的名字。特别是那些在 BSI 工作的同事，他们在多年来为 ASN.1 项目提供了大量支持。此外，我还想提到那些在 AFNOR 工作、来自瑞典的同事，以及在美国的同事们——他们制作的 ASN.1 相关课程资料至今仍被全球广泛使用。

Stop! Enough of this clause! 停止！已经够了，不再需要这个条款了！

## 2 Going round in circles? 2 在循环中兜圈吗？

There are so many areas of notational and encoding support for computer communications where understanding has emerged only slowly. (Support for "holes", described earlier, is one of these, as are mechanisms to ensure interworking between implementations of "version 1" and "version 2" of protocol specifications). Sometimes developments are clear steps forward (as was the case when ASN.1 was introduced in the early 1980s), sometimes we make backward steps in some areas to make progress in others. 在计算机通信的表示和编码方面，有很多领域的发展进展十分缓慢。例如，对“空洞”这种表示方式的支持，以及确保“版本 1”和“版本 2”协议规范之间相互兼容的机制，都是需要逐步完善的领域。有时候，发展会呈现出明显的进步（比如，在 20 世纪 80 年代初引入 ASN.1 标准时的情况），而有时候，我们则需要在某些领域做出退步，才能在其他领域取得进展。

We see through a glass darkly. What is the "right" notational support for people trying to define messages for computer communication? ASN.1 has a lot to offer, and has recognised many of the problems (and provided some good solutions) but the world has a way to go yet. 我们仿佛透过玻璃看透了黑暗。对于那些试图为计算机通信定义消息的人来说，究竟应该采用哪种“正确的”表示方式呢？ASN.1 提供了很多解决方案，并且已经识别了许多问题（并提出了一些不错的解决方案），不过这个世界还有很长的路要走。

When ASN.1 was born in the early 1980s, Open System's Interconnection (OSI) Standards were "the best thing since sliced bread", and meetings to develop these Standards within ISO and CCITT often involved several hundred people. But in all the ISO groups defining OSI Standards for applications, there was at that time a doubt, a debate, about what notation to use to clearly specify the messages (including their semantics, and their bit-patterns) to be used to support the application. Every group was doing its own thing, with different approaches and different notations. 在 20 世纪 80 年代初，ASN.1 这一标准诞生时，开放系统互连标准被视作“自切片面包以来最优秀的解决方案”。在 ISO 和 CCITT 组织的各种标准化会议上，经常会有数百人参与这些标准的制定工作。不过，在那些负责定义应用层 OSI 标准的各个小组中，人们对于应该使用哪种表示方式来清晰指定消息的内容（包括它们的语义和位模式）存在争议。每个小组都采用自己的方法，使用不同的表示方式。

Use of a BNF (Bacchus-Naur Form) style of specification was common in most early OSI drafts, often with an encoding based on strings of characters (much as many Internet protocols are today). 在早期的 OSI 协议中，广泛使用 BNF（Bacchus-Naur Form）风格的规范格式。这种规范通常基于字符字符串进行编码（就像许多现代互联网协议一样）。

When the first ASN.1 text (and it was not called ASN.1 in those days - that is another story - see below) was sent as a liaison from CCITT to ISO, it was almost immediately welcomed by every single application layer standardization group in ISO as: 当第一个 ASN.1 文本（在那个时候它并不被称为 ASN.1——这是另一个故事了——详见下文）作为通信内容从 CCITT 发送给 ISO 时，它几乎立刻就受到了 ISO 中每一个应用层标准化组织的欢迎。

• Great to have a common and standard notation for all to use in specifying protocols. • 拥有一种通用的标准符号系统真是太好了，这样大家都能使用同一种方式来指定协议。

• Great to get away from verbose text-based exchanges. • 能够远离那些冗长且基于文本的交流方式，真是太好了。

(Note the latter point. Despite later strong criticism of the verbosity of BER, and the eventual emergence of PER, both are far less verbose than text-based encodings.) （注意后一点。尽管后来有人对 BER 的冗长性提出了强烈批评，并且后来出现了 PER 这种替代方案，但 PER 的冗长程度还是远远低于基于文本的编码方式。）

ASN.1 became the notation of choice (and BER the encoding) for all the application layer OSI Standards (and for the Presentation Layer as well). ASN.1 已成为所有 OSI 层协议的首选表示方式（BER 则被用作编码方式），同样，在表示层中也如此。

But it was in the mid-1980s when ASN.1 started to become widely used outside of the OSI stack. There was even some take-up (usually in a cut-down - some would say bastardised! - form) within the Internet community, but the real expansion of ASN.1 was amongst the telecommunications standards specifiers. 不过，直到 20 世纪 80 年代中期，ASN.1 才开始在 OSI 模型之外得到广泛应用。虽然它在互联网社区中也存在一些应用实例（通常都是经过简化版的形式——可以说是一种修改过的版本），但 ASN.1 真正的大规模应用还是出现在电信标准规范领域。

It is the case today that a great many telecommunications standards (for mobile phones, for intelligent networks, for signalling systems, for control of electric power distribution, for air traffic control) use ASN.1. (See the next chapter.) 目前，许多电信标准（包括移动电话、智能网络、信号系统、电力分配控制以及空中交通管制等领域的标准）都采用了 ASN.1 标准。（详见下一章。）

But today we still see a battle between those who prefer text-based protocols and the supporters of ASN.1. The emergence of XER (Extended Mark-up Language - XML - Encoding Rules) for ASN.1 has in some ways married the two camps. XER is based on ASN.1 notation for defining types, but is totally character-based (and verbose!) for the transfer of values of those types. However, you will hear people today (with some justification) saying: 不过，如今我们仍然可以看到那些偏好文本协议的人与支持 ASN1 的人之间的争论。XER（扩展标记语言——XML 编码规则）的出现在一定程度上弥合了这两派之间的分歧。XER 基于 ASN1 的语法定义类型，但在处理这些类型的值时却完全采用字符编码方式（而且非常冗长）。不过，现在人们也会说一些话——虽然有些理由可以支持这种说法：

HTML (with Netscape and Microsoft) made provision for write-it-once, read-it-anywhere Web pages. HTML（结合 Netscape 和 Microsoft 的技术）提供了可以一次性编写、任意位置阅读的网页功能。

• JAVA made provision for write-it-once, run-it-anywhere programs. • JAVA 语言提供了能够编写一次代码、在任意地方运行的程序的支持。

• XML makes provision for write-it-once, process-it-anywhere data. • XML 提供了可一次性编写、任意位置处理的数据支持。

And, of course, there is still CORBA (with its IDL notation and IOP protocol as an encoding) as a communications-specification-language contender! 当然，还有 CORBA 作为一种通信规范语言候选方案存在！它采用 IDL 表示法和 IOP 协议作为编码标准。

And we still have a lot of Internet Engineering Task Force (IETF) specifications choosing to use BNF and character-based exchanges as the preferred definition mechanism for messages. 目前，仍有许多互联网工程任务组（IETF）的规范选择将 BNF 和基于字符的交换方式作为消息传输的首选机制。

It may be some time yet before the world homes-in-on, understands, or recognises the "right" way to define and to encode computer communications (and that may or may not be ASN.1 in the form we know it today). We have progressed a lot (in terms of understanding the issues and problems to be solved) from the early 1980s, but we have progressed rather less far in political (lower-case "p") agreements, with a still (alarmingly large) number of contenders for notation to be used in defining protocols. And still people continue to suggest more! (I guess it is no worse than the programming language scene.) 或许还需要一段时间，世界才能确定、理解或认可“正确”的方式来定义和编码计算机通信（也许这种方式就是我们现在所熟知的 ASN.1 标准）。从 20 世纪 80 年代初到现在，我们在理解相关问题和需要解决的技术难题方面已经取得了很大的进展。然而，在关于协议符号选择的政治性协议中，我们取得的进展却相对较少。目前，仍然有大量的竞争者试图主导协议的符号选择。而且，人们不断提出更多新的建议！（我想这种情况并不比编程语言领域的状况更糟糕吧。）

So ... I look forward to the next decade with interest! What notation will we be using in 2020 to specify protocol standards? I regret that I may not be around to find out! Some readers will! 所以……我非常期待下一个十年的到来！2020 年我们会使用什么符号来表示协议标准呢？可惜我可能活不到那个时候了……不过，肯定会有其他人能发现答案的！

## 3 Who produces Standards? 3. 谁负责制定这些标准？

There have over the years and into today been five main sets of actors in the production of Standards related to computer communication, and in the adoption of various forms of notation to support those Standards. 多年来，在计算机通信相关标准的制定过程中，以及在各种符号的采用上，一直存在五组主要的参与者。

Who are the five? 那五个人都是谁啊？

I would suggest: 我建议：

There has always been a difficulty over de jure and de facto standards for computer communication around the world. National Standards Institutes often think/hope they wield the power. But the real power over deciding how the world's computers communicate is largely not in their hands, but has shifted over time between many actors. 在全球范围内，关于计算机通信的法律标准与事实标准一直存在争议。各国的标准机构往往认为自己拥有决定这些标准的权力，但实际上，决定全球计算机如何通信的真正权力并不掌握在它们手中，而是随着时间推移，逐渐转移到了许多其他参与者手中。

• Main-frame computer vendors in the 1970s, but largely now unimportant. • 在 20 世纪 70 年代，这些公司是大型机计算机的供应商，但现在它们已经不再重要了。

• CCITT (renamed ITU-T at the start of the 1990s) in the 1980s and 1990s, and still the dominant force in the specification of telecommunications standards today. • 在 20 世纪 80 年代和 90 年代，CCITT（在 20 世纪 90 年代初更名为 ITU-T）一直主导着电信标准的制定工作，至今仍是在这一领域中最具有影响力的组织。

• ISO, working largely in collaboration with CCITT/ITU-T, but with its major influence limited to the OSI developments of the 1980s, and perhaps not being a dominant force today except in isolated areas. • ISO 主要在与 CCITT/ITU-T 的合作下进行工作，但其主要影响范围仅限于 20 世纪 80 年代的 OSI 标准制定工作。如今，ISO 虽然在某些领域仍具有影响力，但总体上已不再是一个主导性的组织。

The IETF, its task forces and working groups, now responsible for the development of Internet standards, which have (for many applications) become the de facto standards for computer communication between telecommunications users (whilst ITU-T remains dominant for standardising the protocols that make telecommunications possible). IETF 及其各个工作组现在负责制定互联网标准。这些标准已经成为了许多应用中计算机通信的默认标准（而 ITU-T 则仍然在标准化使电信通信成为可能的协议方面占据主导地位）。

• And with increasing influence today, various consortia of manufacturers and other groups, including the SET consortium and the World-Wide Web Consortium (W3C), and the CORBA grouping. • 如今，各种制造商联盟以及其他组织的影响力日益增强，其中包括 SET 联盟、全球网络联盟（W3C）以及 CORBA 组织等。

The importance of computer vendors in protocol definition had largely declined before ASN.1 entered the scene, with the notable exception of XEROX which (as stated earlier) gave birth to the original ASN.1 concepts. 在 ASN.1 出现之前，计算机供应商在协议定义方面的重要性已经大大降低了。不过，XEROX 是一个显著的例外——正如之前提到的，XEROX 孕育了 ASN.1 的最初概念。

ASN.1 as an international specification started life within CCITT as X.409, entitled "Presentation Transfer Syntax and Notation". (Note that the "transfer syntax" was placed first in the - English - title, not the "notation"! Today we would probably see the notation as the more important part of ASN.1). The work leading to ASN.1 was originally intended only to provide notational support for the definition of the X.400-series e-mail protocols. However, it very rapidly moved into ISO, and during the early 1980s, although the work was collaborative, it was largely ISO National Bodies (they were then called "Member Bodies") through which most of the input was provided. ASN.1 作为一种国际规范，最初由 CCITT 在 X.409 标准下提出，该标准名为“Presentation Transfer Syntax and Notation”。需要注意的是，在英文标题中，“Transfer Syntax”被排在了首位，而不是“Notation”！如今，我们可能会认为“Notation”是 ASN.1 中更为重要的部分。最初制定 ASN.1 的工作只是为了为 X.400 系列电子邮件协议的定义提供相应的符号支持。然而，这项工作在很短的时间内就进入了 ISO 的管辖范围。在 20 世纪 80 年代初，尽管这项工作是由多个机构共同完成的，但实际上大部分内容都是由 ISO 各国家机构提供的。

In the late 1990s the pendulum swung back (partly due to the decline of OSI, and partly due to reorganizations within ISO), with what had by then become ITU-T making most of the running in progressing new work on ASN.1. 在 20 世纪 90 年代末，这一趋势又发生了逆转（部分原因是 OSI 的衰落，部分原因是 ISO 内部的重组）。此时，ITU-T 继续在 ASN.1 领域推进新的研究工作。

Within IETF, take-up of ASN.1 was always very patchy. This was probably at least in part due to the fact that most of the movers in IETF wanted a specification language that had support from publicly available (for-free) tools. BNF-based text-encodings satisfied this requirement. ASN.1 did not, and does not to this day (1999). So most use of ASN.1 in the IETF world was (and is) using a cut-down version of ASN.1 that was (is) easily capable of being encoded without the use of any tools. 在 IETF 内部，ASN.1 的采用情况一直很不平衡。这至少部分是因为 IETF 中的许多活跃人士希望有一种能够得到公开可用工具支持的规范语言。基于 BNF 的文本编码方式满足了这一需求。而 ASN.1 则没有做到这一点，直到今天（1999 年）仍然如此。因此，在 IETF 领域，大多数对 ASN.1 的使用都是采用一种简化版的 ASN.1 进行编码的，而这种简化版 ASN.1 完全可以通过无需任何工具就能被编码出来。

By contrast, ITU-T telecommunications specifications use the full power of ASN.1, and the telecomms and switch vendors implementing those specifications make full use of available tool products for easy, rapid, and (largely) bug-free implementation of protocols that are highly efficient in terms of band-width requirements. 相比之下，ITU-T 的电信规范充分利用了 ASN.1 框架的优势。那些实施这些规范的电信设备和交换机供应商，会充分利用现有的工具产品，从而实现协议的快速、高效的实施——而且几乎不会遇到任何问题。

## 4 The numbers game 4. 数字游戏

The ASN.1 specifications have gone through a variety of designations. ASN.1 规范经历了多种名称的变迁。

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/54379e17-c034-430b-894c-f77661f731e5/66ae97c8ce9eb8cc27aacb3c6d659957c50aa0f7b4b9da910555e37b438dcede.jpg)

The first published specification was X.409 (1984). X.409 pre-dated the use of the term "Abstract Syntax Notation One (ASN.1)", and was part of the X.400 series. It was seen, quite simply, as a notation (and encoding rules) to aid the specification of protocols in the X.400 (OSI e-mail) suite. 第一个公开的规范是 X.409（1984 年发布）。X.409 的出现早于“抽象语法符号表示法之一（ASN.1）”这一术语的使用，它是 X.400 系列的一部分。简单来说，X.409 是一种用于辅助 X.400 协议（如 OSI 电子邮件协议）规范描述的符号和编码规则。

Later it was completely re-written (with no technical changes - see later!) and published (with some additions) by ISO as ISO 8824 and ISO 8825 in 1986, and the same text (again with some additions) was then published by CCITT as X.208 and X.209 in 1988. There was a later version of this text (with minor corrections) published jointly by ISO and IEC in 1990 as ISO/IEC 8824 and ISO/IEC 8825. This became known as the infamous "1990 version of ASN.1". 后来，该标准被完全重新编写（实际上没有进行任何技术上的修改——详见后文！），并由 ISO 在 1986 年以 ISO 8824 和 ISO 8825 的标准发布。同年，同样的内容又被 CCITT 作为 X.208 和 X.209 标准发布。此后，ISO 和 IEC 在 1990 年联合发布了修订了部分内容的版本，即 ISO/IEC 8824 和 ISO/IEC 8825。这一版本被称为“著名的 1990 版 ASN.1 标准”。

The "1994 version of ASN.1" (with very major extensions to the 1990 version) was jointly published by ISO/IEC and CCITT as a whole raft of new documents, with identical text shown in parallel columns below: “1994 版的 ASN.1”版本（在 1990 版的基础上进行了重大扩展）是由 ISO/IEC 和 CCITT 联合发布的一系列新文件。这些文件的文本内容在下面以平行方式呈现：

ITU-T X.680 ISO/IEC 8824-1 ITU-T X.681 ISO/IEC 8824-2 ITU-T X.682 ISO/IEC 8824-3 ITU-T X.683 ISO/IEC 8824-4 ITU-T X.690 ISO/IEC 8825-1 ITU-T X.691 ISO/IEC 8825-2 ITU-T X.680 ISO/IEC 8824-1；ITU-T X.681 ISO/IEC 8824-2；ITU-T X.682 ISO/IEC 8824-3；ITU-T X.683 ISO/IEC 8824-4；ITU-T X.690 ISO/IEC 8825-1；ITU-T X.691 ISO/IEC 8825-2

Still later, there was a joint ISO/IEC and ITU-T "1997 version" (with only relatively minor changes and additions to the 1994 version). However, whilst the "final" text was approved in 1997, neither ITU-T nor ISO have yet produced a published copy that people can purchase (current date early 1999)! But watch this space, it is imminent! (Later correctoin – you can now buy it from ITU-T!) 后来，又出现了一种由 ISO/IEC 和 ITU-T 联合制定的“1997 版本”标准（与 1994 年的版本相比，只有一些微小的修改和补充）。不过，虽然该“最终版”标准在 1997 年得到了批准，但无论是 ITU-T 还是 ISO 都尚未发布可供人们购买的正式版本（当前版本为 1999 年初发布的）。不过请继续关注进展情况，很快就能买到该标准了！（稍后补充：现在可以从 ITU-T 那里购买到该标准了！）

Readers should note that in 1994 (and in 1997) X.680 was roughly the old X.208 with some extensions, mainly in the character set area. X.681 was the extensions related to the Information Object concept. X.682 was the table and relational and user-defined constraints, and X.683 was parameterization. X.690 was the old X.209 with CER and DER added, and X.691 was the PER specification. 读者需要注意，在 1994 年以及 1997 年时，X.680 基本上就是旧的 X.208 标准，只是增加了一些扩展功能，主要集中在字符集方面。X.681 则包含了与信息对象概念相关的扩展功能。X.682 涉及表格处理、关系型数据以及用户自定义约束条件。而 X.683 则涉及到参数化功能。X.690 则是旧的 X.209 标准，增加了 CER 和 DER 功能。最后，X.691 则包含了 PER 规范的相关内容。

Phew! I hate numbers! 'Nuff said. 呼！我讨厌数字！说多了反而让人厌烦。

## 5 The early years - X.409 and all that 5. 早期岁月——X.409 以及相关的一切

## 5.1 Drafts are exchanged and the name ASN.1 is assigned 5.1 双方交换了草稿文件，并指定了 ASN.1 作为标识符。

The first drafts of X.409 were produced in CCITT. In those days both ISO and CCITT had a "7-layer model" for OSI, and they were totally different texts (technically very similar, but largely developed independently). The era of strong collaboration between the two groups was yet to come, and most communication was by written "liaison statements", usually accompanied by a draft of some specification. X.409 标准的初稿是在国际电信联盟 ITU 的会议上制定的。当时，ISO 和 ITU 都采用了类似的“七层模型”来描述 OSI 协议，不过它们所依据的文本是完全不同的——从技术层面来看，两者非常相似，但主要是在不同的时间、由不同的团队独立开发的。直到后来，这两个组织才开始加强合作，而当时的通信方式大多还是通过书面“联络声明”来进行，通常会附上一些规范草案作为支持。

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/54379e17-c034-430b-894c-f77661f731e5/1db2f4bdecc5b6922d8d1b92ab569a1975467d821c42658fa2bcc704a112600f.jpg)

This is how (during 1982) X.409 first reached ISO TC97 SC16 (Technical Committee 97 - responsible for the whole of computer-related standards, Sub-Committee 16 - responsible for the OSI model and for all work on OSI standards above the Network Layer). At first, it was unclear how these X.409 concepts fitted into the OSI model, and an ad hoc group (chaired, I think, by Lloyd Hollis) was set up to consider the draft. It rapidly became apparent that this work should be slotted into the Presentation Layer of OSI, and a liaison statement was despatched welcoming the work. 这就是 X.409 标准在 1982 年时首次被提交给 ISO TC97 SC16 技术委员会的过程。TC97 是负责所有与计算机相关的标准的专业委员会，而 SC16 则负责 OSI 模型以及网络层以上的所有 OSI 标准相关工作。起初，人们并不清楚 X.409 的概念如何融入 OSI 模型中。于是，一个临时小组被成立来审议这份草案。很快便明确，这项工作应该被纳入 OSI 模型的表示层。随后，一份合作声明被发送出来，以表示对这项工作的欢迎。

This X.409 draft came into an ISO vacuum - or perhaps I mean a primeval plasma! There was anarchy, with all the various application layer standards wondering what notational mechanisms to use to define their protocols, and all having different approaches. The new notation was extremely rapidly accepted by every single Application Layer standards group as the means to define their protocols. 这份 X.409 草案在 ISO 的空白环境中诞生了——或者可以说，它诞生于原始的“等离子体”状态之中。当时处于一片混乱的状态，各个应用层的标准们都在思考应该使用哪种表示机制来定义他们的协议，而且各种标准之间存在着不同的方法。不过，这种新的表示方式很快就被每一个应用层标准组织所接受，成为了定义他们协议的标准手段。

It was at this time that a name was considered for the notation, and the ISO group suggested Abstract Syntax Notation One, or "ASN1". The CCITT group replied "OK, but never talk to us about ASN2". ASN2 was never proposed, although there are those that have argued that ASN.1 (1994) should have been named ASN.2 (see later text). 就在那时，有人提议为这种标记方式起一个名字。ISO 小组建议将其命名为抽象语法标记语言一（Abstract Syntax Notation One），简称“ASN1”。而 CCITT 小组则回应说：“好吧，但请不要再跟我們提起 ASN2 这个名称。”实际上，ASN2 从未被正式提出过。不过，有些人认为，ASN.1（1994 年版本）应该被命名为 ASN.2（详见后文）。

Notice that in the last paragraph there was no dot after "ASN". This was not a typo! The original proposed name was indeed "ASN1". However, within six months it became apparent that people were frequently mistyping it as "ANS1", and/or misreading it as "ANSI" - the American National Standards Institute. Considerable confusion was being caused! I remember the day when the head of the USA delegation (also Chairman of SC16!) came to the ASN.1 group and said "Look, I know it isn't "ANSI", but it is so close that it is causing problems, can't you change the name?". Uproar! Explosion! But when the dust settled, the "dot" had been inserted and we had "ASN.1". Thereafter no-one ever mistyped it or confused it with ANSI! 请注意，在最后一段中，“ASN”后面并没有点号。这并非拼写错误！最初提议的命名确实是“ASN1”。然而，在六个月的时间里，人们经常将其误拼成“ANS1”，或者误将其理解为“ANSI”——即美国国家标准协会。这导致了相当大的混乱！我记得有一天下午，美国代表团的负责人（同时也是 SC16 会议的主席）来到 ASN.1 小组，说道：“听着，我知道它并不等于 ANSI，但这个名字太接近了，会造成问题，你们能改改这个名字吗？”顿时引起了轩然大波！不过，等一切平静下来后，人们发现“点号”被正确地加在了后面，于是“ASN.1”这个名称就定型了。从那以后，就再也没有人把它误拼或误认为是 ANSI 了！

The "dot" is not without precedent - all CCITT Recommendations are written with a dot - X.400, X.25, V.24, so ASN.1 was readily accepted. 这种用点号连接的名称并不陌生——所有国际电信联盟的建议书都是这样命名的，比如 X.400、X.25、V.24 等。因此，ASN.1 这种命名方式也很容易被接受。

It was at this time that the term "BER" (Basic Encoding Rules) was coined, but in this case there was recognition in both ISO and CCITT that other and perhaps better encoding rules could be produced, but it took ten years before PER (Packed Encoding Rules) eventually emerged. 就在那时，术语“BER”（基本编码规则）被提出。不过，当时无论是 ISO 还是 CCITT 都认识到，可以制定出更优秀的编码规则。但直到十年后，PER（打包编码规则）才最终被提出来。

## 5.2 Splitting BER from the notation 5.2 从符号表示法中解析误码率

There were some difficult moments in these early years. It was ISO and not CCITT that had a very strong view on the importance of separating abstract specification (Application Layer) from encoding issues (the first published X.400 specifications were a monolithic protocol directly on the Session Layer, with no Presentation Layer). The X.409 draft (and the eventually published X.409 (1984)) contained, interleaved paragraph by paragraph, a description of a piece of ASN.1 notation and the specification of the corresponding BER encoding. 在那些早期阶段，确实遇到了一些困难。当时是 ISO 而不是 CCITT 在强调将抽象规范（应用层）与编码问题分离的重要性。最初的 X.400 规范文档中，所有内容都是混杂在一起的；比如 X.409 草案（最终于 1984 年正式发布）中，每一段都详细描述了某种 ASN.1 表示法，并规定了相应的 BER 编码方式。

ISO was serious about the Presentation Layer. Encoding details should be kept clearly separate (in separate documents) from application semantics. A great idea, but CCITT were not quite as evangelical about it. But without ASN.1 the concept would probably never have reached reality. ISO 在表示层方面非常重视细节。编码相关的内容应该与应用程序的语义分开处理，分别放在不同的文档中。这是一个很好的想法，不过 CCITT 在这方面并没有那么积极。不过，如果没有 ASN.1 标准，这个概念可能永远无法付诸实践。

The first thing that ISO decided to do was to rip these pieces apart, and completely re-write them (in theory with no technical change) as two separate documents, one describing the notation (this eventually became ISO 8824) and one describing BER (this eventually became ISO 8825). ISO 首先采取的措施是将这些文档拆分开来，然后分别重新编写成两份独立的文件（理论上不进行任何技术上的修改）。其中一份文件用于描述符号规范（该规范最终被命名为 ISO 8824），另一份文件则用于描述 BER 标准（该标准最终被命名为 ISO 8825）。

As closer and closer collaboration occurred between ISO and CCITT in the following years (and on the ASN.1 work in particular), the question of course arose - would CCITT adopt the ISO text for ASN.1 and drop X.409? After some agonising, it did, and in 1988 X.409 was withdrawn and there were two new CCITT recommendations in the X.200 series, X.208 and X.209. Recommendation X.200 itself was (and is) the CCITT/ITU-T publication of the OSI Reference Model - eventually aligned with that of ISO but leaning technically far more towards the original CCITT draft than to the OSI one - but that is a separate story! (See my book "Understanding OSI", available on the Web.) Putting the ASN.1 specifications into the X.200 series was a recognition that ASN.1 had become a general tool for the whole of OSI, having outgrown X.400. I like to think that its move to the X.680 and the X.690 range in 1994 represented its outgrowing of OSI, but I think it was more due to the fact that it now needed six Recommendations, and there was no suitable space left in the X.200 range! (ISO does not have similar problems - a single part Standard like ISO 8824 can grow into ISO 8824 Part 1 (ISO 8824-1), Part 2, etc, without changing its number.) 在接下来的几年里，ISO 与 CCITT 之间的合作越来越紧密（尤其是在 ASN.1 领域）。自然而然地，一个问题出现了：CCITT 是否会采用 ISO 的规范来制定 ASN.1 标准，并放弃 X.409 标准？经过一番讨论后，他们决定采用 ISO 的规范，于是 X.409 标准被撤销，取而代之的是 X.200 系列中的两个新标准：X.208 和 X.209。X.200 标准本身实际上是 CCITT/ITU-T 对 OSI 参考模型的规范——最终与 ISO 的规范保持一致，但在技术层面上，X.200 更接近于原始的 CCITT 草案，而非 OSI 的规范。不过，这又是另一个故事了！（可以参考我的书籍《理解 OSI》，该书可以在网上找到。）将 ASN.1 规范纳入 X.200 系列，意味着 ASN.1 已经成为了涵盖整个 OSI 模型的通用工具，因为它已经不再适合仅用于 X.400 标准了。我喜欢认为，ASN.1 之所以被纳入 X.680 和 X.200 系列，正是因为它已经成为了整个 OSI 模型的核心规范。在 1994 年，690 系列标准代表了其超越 OSI 标准的发展态势。不过我认为，这主要是因为现在需要包含六条建议内容，而 X.200 系列标准中已经没有足够的空间来容纳这些内容了。（ISO 标准并没有类似的问题——比如 ISO 8824 这样的单一部分标准，可以逐渐发展成 ISO 8824-1 第 1 部分、第 2 部分等，而无需改变其编号。）

X.409 was written in a fairly informal style, but when it was re-written within the ISO community, the rather stilted "standardese" language required for ISO Standards was used. For example, "must" must never be used - use "shall" instead (this was due to claimed translation difficulties into French), don't give examples or reasons, just state clearly and exactly what the requirements are - you are writing a specification of what people must do to conform to the Standard, not a piece of descriptive text. X.409 的编写风格相当非正式，但在 ISO 社区内部重新编写时，采用了更为正式的标准化语言。例如，“必须”这个词绝对不能使用，应该使用“应当”来代替。此外，不要提供例子或理由，只需明确准确地说明要求是什么——你是在编写一份关于人们必须做什么才能符合标准的规范说明，而不是一篇描述性文本。

I often advise those who want a gentle introduction to ASN.1 to try to find an old copy of X.409 (1984) and read that - it is written in more informal language, and because the encodings are specified along-side the notation, I believe that it is easier for a beginner to grasp. But I was interested to see that in Olivier's book he claimed that 8824/8825 were more readable and better specifications than X.409! I guess we all have our own views on what makes a good specification! 我经常建议那些想要了解 ASN.1 的人，尝试找到一份旧的 X.409 标准（版本 1984 年）的副本进行阅读。该标准使用的语言更为简洁明了，而且由于编码规范与符号说明一起给出，因此初学者更容易理解。不过，我很惊讶地发现，在奥利维耶的书中，他声称 8824/8825 标准比 X.409 标准更易于理解，且规范更完善！我想，对于什么是好的规范标准，每个人都有自己的看法吧！

## 5.3 When are changes technical changes? 5.3 什么时候会进行技术上的变更呢？

Genuinely, ISO attempted to re-write X.409 without making technical changes, but two crept in. The first was to do with the type "GeneralizedTime". These were in the days when people had human secretaries to do their 实际上，ISO 试图在不进行任何技术修改的情况下重新编写 X.409 标准。不过，有两个修改被悄悄加进了标准中。第一个修改与“广义时间”这一类型有关。在那个时代，人们还依赖人工秘书来处理这些事务……

Correct a spelling, remove an example, trivial things. No problem. Don't you believe it! 纠正一个拼写错误，删除一个例子，处理一些琐碎的问题。没什么大不了的。你相信吧！

typing and not word processors. X.409 had been authored in the USA. The ISO text for 8824/8825 had a UK Editor (mea culpa), and the secretary (another name - Barbara Cheadle!), unknown to the Editor, corrected the spelling to "GeneralisedTime". This went unnoticed through all the formal balloting, but was eventually corrected before 8824 was actually published! Irrespective about arguments over what is "correct" English, the term "GeneralizedTime" had to stand, because this was a formal part of the notation, and any change to its spelling represented a technical change! 使用的是打字方式，而非文字处理软件来编辑文档。X.409 标准是在美国制定的。ISO 关于 8824/8825 标准的文本中，有一位英国编辑参与了编辑工作（这是我的过错），而另一位秘书（名叫芭芭拉·切德勒！）在编辑者不知情的情况下，将拼写改为“GeneralisedTime”。这一修改在所有的正式审议过程中都没有被注意到，但最终在 8824 标准正式发布之前得到了修正！无论哪种英语拼写方式才是正确的，因为“GeneralisedTime”这个术语已经是该标准的一部分了，对其拼写进行任何修改都意味着技术上的变更！

The second change was only noticed in the early 1990s! Far too late to do anything about it! There was a point of detail about the character string type TeletexString that was only indicated in X.409 in an example. The example was lost in 8824, and the point of detail lost with it - I am afraid I have forgotten the precise details of the point of detail! 第二个问题直到 20 世纪 90 年代初才被注意到！现在想要解决已经为时已晚了！在 X.409 规范中，有一个关于字符串类型 TeletexString 的细节说明，但那个例子在 8824 版本中丢失了。因此，那个细节也一并消失了——恐怕我已经记不清那个细节的详细内容了！

## 5.4 The near-demise of ASN.1 - OPERATION and ERROR 5.4 ASN.1 的即将失效——操作与错误

The final incident I want to describe, in this clause about the early days, is one which almost completely de-railed ASN.1. 在关于那段早期经历的部分，我想要描述的最后一个事件，是那个几乎完全破坏了 ASN1 运作的事件。

At that time, CCITT was locked into a fouryear time-frame called a Study Period where at the start of the four years "Questions" 当时，国际电信联盟被限制在一个为期四年的时间范围内，这个时间段被称为“研究期”。在四年期的开始之际，各种“问题”尚未得到解决。

Easy wars are based on misunderstanding or lack of understanding (difficult ones are base on real clashes of self-interest). This was an easy war, but the short time-scales for achieving peace amplified the conflict. 简单的战争是基于误解或缺乏理解而发生的（复杂的战争则是基于实际的利益冲突）。这是一场简单的战争，但由于实现和平所需的时间很短，反而加剧了冲突。

(capital Q!) were formulated. (Each Question generally gave rise to a new Recommendation or to an update of an existing one.) At the end of the Study Period, a complete new set of CCITT Recommendations were published (with a different colour cover in each period). In 1980 the colour was Yellow, Red in 1984, and Blue in 1988. （资本 Q！）这些建议被正式制定出来。每个问题通常都会产生一个新的建议，或者是对现有建议的更新。在研究期结束时，发布了一整套全新的 CCITT 建议书（每个时期的建议书都有不同的颜色封面）。1980 年，封面颜色为黄色；1984 年为红色；1988 年则变为蓝色。

(1988 was the last year this complete re-publication occurred, so if you have a set of the Bluebooks in mint condition, keep them - they will be valuable fifty years from now!) 1988 年是这次完整重新出版的最后一年。所以，如果你拥有一套保存状况良好的《蓝色之书》系列书籍，请好好保存它们——五十年后，这些书籍将会变得非常有价值！

It took time for the administration to prepare these new texts for publication, and in those days CCITT went into a "big sleep" about twelve months before the end of the Study Period, with the new or amended Recommendations finalised, and with only "rubber-stamping" meetings during the following year. It was in mid-1993, with the "big sleep" about to start - we were at five minutes to midnight - when the CCITT ASN.1 group sent their latest draft of X.409 to the ISO group. 行政机构需要一些时间来准备这些新的标准文本以供发布。在那个时期，国际电信联盟在研究期结束前大约十二个月进入了“大休整期”，新的或修改后的建议最终确定下来，而在接下来的这一年里，相关的会议也只进行了很少的次数。大约在 1993 年中期，当“大休整期”即将开始时——当时时间距离午夜还有五分钟——国际电信联盟 ASN.1 小组将他们最新的 X.409 草案提交给了 ISO 小组。

Mostly it was only minor tidies, but a whole new section had been added that "hard-wired" into the ASN.1 syntax the ability to write constructions such as: 大多数情况下，这些只是一些简单的修改而已。不过，新增了一整段内容，这些内容被“硬编码”在了 ASN.1 语法中，使得用户可以编写如下这样的结构：

and 以及

```txt
lookup OPERATION
    ARGUMENTS name Some-type
    RESULT name Result-type
    ERRORS {invalidName, nameNotFound}
::= 1

nameNotFound ERROR ::= 1

invalidName ERROR
    PARAMETER reason BITSTRING
    {nameTooLong(1),
    illegalCharacter(2),
    unspecified(3)}
::= 2 
```

Well ... if the reader has read the earlier parts of this book, and in particular Section II Chapters 6 and 7, that syntax will look rather familiar, and the meaning will be perhaps fairly obvious. But to those in the ISO group faced with a simple liaison statement defining the revised ASN.1 (and with absolutely no understanding or knowledge about even the existence of the ROSE work), there was utter incomprehension. 嗯……如果读者已经阅读了这本书的前面部分，尤其是第二部分的第六章和第七章，那么这些语法结构会显得相当熟悉，其含义也可能相当明显。不过，对于那些身处 ISO 小组的人来说，他们面对的是一条简单的关联语句，用来定义修改后的 ASN.1 标准。而他们对于 ROSE 工作甚至其存在都一无所知。因此，他们对这些内容完全无法理解。

What had this to do with defining datatypes for an abstract syntax (and corresponding encoding rules)? How were ERROR and OPERATION encoded (there was no specification of any encoding in the draft)? What on earth was an "operation" or an "error"? Rip it all out! Had there been more time .... But the ISO group decided that no-way was this stuff going into the ISO Standards that were planned. Agonies within CCITT. Keep it in and risk different Recommendations and Standards for ASN.1? 这与为抽象语法定义数据类型有什么关系呢？而“ERROR”和“OPERATION”又是如何被编码的呢？在草案中并没有对编码方式做任何规定。那么，“operation”和“error”到底指的是什么呢？算了，还是把这一切都抛到一边吧！如果还有更多的时间的话……但是 ISO 小组决定，这些内容绝对不会被纳入原本计划中的 ISO 标准中。CCITT 内部也发生了一些争执。那么，是否应该将相关内容保留下来，以便为 ASN.1 标准制定不同的建议和规则呢？

It was one minute to midnight when the next draft of X.409 reached ISO. The offending OPERATION and ERROR syntax had been removed - deep sigh of relief - but a new Annex had been added defining a "macro notation". This Annex was very, very obscure! But many programming languages had a "macro notation" to support the language. (These usually took the form of some template text with dummy parameters that could be instantiated in various places with actual parameters - what was eventually introduced with the parameterization features of ASN.1). And it was one minute to midnight. And the CCITT group had agreed to withdraw the OPERATION and ERROR syntax, and deserved a favour in return. The ISO group agreed to accept the macro notation Annex. Peace had been achieved and ASN.1 had been saved! 当 X.409 的下一版草案到达 ISO 时，已经是午夜零点刚过的一分钟。那些引起争议的 OPERATION 和 ERROR 语法已经被删除了——真是松了一口气！不过，新的附录中增加了一项关于“宏表示法”的规定。这项附录非常晦涩难懂！不过，许多编程语言都有类似的“宏表示法”来支持他们的语言设计。（通常这种表示法以某种模板文本的形式出现，其中包含可以随实际参数进行替换的虚拟参数——这种机制后来被引入到 ASN.1 的参数化功能中）。现在已经是午夜零点，而 CCITT 委员会也同意撤销 OPERATION 和 ERROR 语法，因此 ISO 委员会也愿意接受这项宏表示法附录。于是，和平达成了，ASN.1 也得救了！

In retrospect, this whole incident was probably a good thing, although it had reverberations into the late-1990s. If OPERATION and ERROR had remained hard-wired, and there had been no macro-notation, it would have been very much harder for ASN.1 to develop the concepts related to Information Objects (and it was quite hard anyway!). More on this subject below. 回顾起来，这一整件事情或许其实是一件好事，尽管它带来的影响一直持续到 20 世纪 90 年代末。如果“OPERATION”和“ERROR”这两个概念是固定不变的，而且没有使用宏注释来表述，那么 ASN.1 就难以开发出与信息对象相关的概念了（而无论如何，开发这些概念本身就已经很困难了！）。关于这个话题，下面会进一步讨论。

## 6 Organization and re-organization! 6. 组织与重组！

When the idea of Open Systems Interconnection was first considered in ISO, it came from the work in TC97 SC6 on HDLC (High Level Data Link Control) from the question "Who is going to define - and how - the formats of what fills the HDLC frames?" At a meeting in Sydney of TC97 it was decided to create a new sub-committee, SC16, to be charged with the task of developing a model for OSI, and at its first meeting about six different proposed models were submitted from each of the major countries, but the 当开放系统互连的概念首次在 ISO 中被提出时，它源自于 TC97 SC6 工作组在 HDLC（高级数据链路控制）领域的工作。当时的问题是：“谁来定义——以及如何定义——填充 HDLC 帧的数据格式？”在悉尼召开的 TC97 会议上，决定成立一个新的小组委员会 SC16，负责开发 OSI 模型的规范。在第一次会议上，来自各个主要国家的代表团分别提出了大约六种不同的模型方案。

Organizational structures matter a bit, but the technical work can often go on despite re-organization above. But sometimes too much turbulence can make it difficult to progress the work formally (and hence to reach publication status). Fortunately, with a joint project between ITU-T/CCITT and ISO/IEC, if you can't progress it in one forum, you can probably progress it in the other! 组织结构固然重要，但即便存在重组情况，技术工作仍然可以继续进行。不过，有时候过度的混乱可能会阻碍工作的正式推进（从而无法完成出版工作）。幸运的是，通过 ITU-T/CCITT 与 ISO/IEC 之间的合作项目，如果你在一个平台上无法推进工作，那么可能在另一个平台上也能顺利推进！

submission that most nearly resembled the eventual shape of OSI was that from the European Computer Manufacturers Association (ECMA). The USA voted against the establishment of a new sub-committee, but by some rather interesting political manoeuvres (again beyond the scope of this text!) became the Secretariat and provided the Chair for SC16. 与 OSI 最终确定的方案最为接近的提案，来自欧洲计算机制造商协会（ECMA）。美国投票反对成立一个新的小组委员会，但通过一些相当有趣的政治手段（同样超出了本文的讨论范围），他们最终成为了该小组的秘书处，并担任了 SC16 会议的主席。

SC16 became one of the largest sub-committees in the whole of ISO, and in its hey-day could only meet by taking over a complete large University campus. ASN.1 became a relatively selfcontained group within the Presentation Layer Rapporteur Group of SC16. SC16 成为了整个 ISO 中规模较大的子委员会之一。在其鼎盛时期，它甚至需要占据整个大型大学校园才能举行会议。而 ASN 则成为了 SC16 报告委员会中一个相对独立的团体。

On the CCITT front, ASN.1 became a part of Study Group VII, and has had a relatively calm (organizationally) life. When CCITT changed its name to ITU-T, it had little organizational impact at the bottom levels, the main change being that SG VII became SG 7! This is the home of ASN.1 to this day (within Working Party 5 of SG 7). 在 CCITT 的框架下，ASN.1 成为了第七研究组的一部分，其发展过程相对平稳。当 CCITT 更名为 ITU-T 时，其在基层组织层面几乎没有产生实质性影响，主要的改变仅仅是第七研究组更名为第七研究组而已！直到今天，ASN.1 仍然属于第七研究组的第五工作组负责处理相关事务。

On the ISO front, there was a top-level re-organization when ISO agreed that standardization of computer matters was a joint responsibility with the International Electro-Technical Commission (IEC), and formed, with the IEC, a new "Joint Technical Committee 1" to replace TC97. (There has never been, and probably never will be, a JTC2). This had zero impact on the ASN.1 work, save that the cover-page of the Standards now included the IEC logo alongside that of ISO, and the formal number became ISO/IEC 8824 instead of ISO 8824. JTC1 inherited exactly the same SC structure and the same officers and members as were originally in TC97. It was at this time that the name of contributors to the ISO work changed from "Member Body" to "National Body", but they were still the same organizations - BSI, ANSI, AFNOR, DIN, JISC, to name just a few. 在 ISO 方面，进行了一次高层级的重组。ISO 决定，计算机相关标准的制定工作应由国际电工委员会（IEC）与 ISO 共同负责。于是，ISO 与 IEC 联合成立了新的“联合技术委员会 1”，以取代原来的 TC97。实际上，从未存在过名为 JTC2 的委员会。这一重组对 ASN.1 的工作几乎没有影响，只是标准的封面现在同时印有 IEC 和 ISO 的徽标，而标准的正式编号也从 ISO 8824 改为 ISO/IEC 8824。JTC1 继承了与 TC97 相同的委员会结构和相同的委员们。此时，参与 ISO 工作的各组织名称从“会员机构”改为“国家机构”，但参与的组织仍然相同，比如 BSI、ANSI、AFNOR、DIN、JISC 等。

A slightly more disruptive reorganization was when SC5 (programming languages and databases) and SC16 (OSI) were re-shaped into a new SC21 and SC22, but the transition was smooth and the ASN.1 work was not really affected. 一次较为彻底的重组发生在 SC5（编程语言和数据库领域）以及 SC16（OSI 标准）被合并为新的 SC21 和 SC22 时。不过这一过渡过程非常顺利，ASN.1 的相关工作也没有受到太大影响。

In the late 1990s, however, the Secretariat of SC21 decided it could no longer resource the subcommittee, and it was split into an SC32 and SC33. ASN.1 was placed in SC33 as a fully-fledged Working Group (it had had the lower-status of a Rapporteur Group within a Working Group for all its previous history), but it never met under this group as there was no National Body prepared to provide the Secretariat for it, and SC33 was disbanded almost before it ever existed. ASN.1 (together with other remnants of the original OSI work, including the continuing X.400 standardization) was assigned to SC6 (a very old sub-committee, responsible for the lower layer protocol standards, and with a very long history of a close working relationship with CCITT/ITU-T SG VII/SG 7). This is likely to prove a good home for ASN.1 within ISO. 然而，在 20 世纪 90 年代末，SC21 秘书处决定不再为该小组委员会提供资金支持，于是该小组委员会被拆分为两个独立的委员会：SC32 和 SC33。ASN.1 被纳入 SC33 作为一个正式的工作组（在之前的历史中，它一直是一个较低级别的报告小组），但实际上它从未在这个小组委员会下召开过会议，因为没有任何国家机构愿意为其提供秘书处支持。SC33 在成立之前就已经解散了。ASN.1（连同原始 OSI 工作的一些残余部分，包括持续进行的 X.400 标准化工作）被分配到 SC6 这个非常古老的子委员会中。SC6 负责下层协议标准的研究，并且与 CCITT/ITU-T SG VII/SG 7 有着长期紧密的工作关系。这或许会成为 ASN.1 在 ISO 内部的一个良好发展平台。

This last transition was less smooth than earlier re-organizations, and the formal progression of ASN.1 work within ISO was disrupted, but at the technical level the work non-the-less continued, and formal progression of documents was undertaken within the ITU-T structures. 这次的过渡过程并不像之前的几次重组那样顺利。ISO 内部关于 ASN.1 标准的工作进展受到了阻碍，但在技术层面上，相关工作仍然持续进行着。相关文件的管理工作则是在 ITU-T 的架构下进行进行的。

## 7 The tool vendors 7. 工具供应商

Of course, when ASN.1 was "invented" in the 1980 to 1984 CCITT Study Period, there were no tools to support the notation. Whilst it drew on Xerox Courier for many of its concepts, it was sufficiently different that none of the Xerox tools were remotely useful for ASN.1. 当然，当 ASN.1 在 1980 至 1984 年的 CCITT 研究期间被“发明”出来时，还没有工具可以用来支持这种表示方式。虽然 ASN.1 在很多概念上借鉴了 Xerox Courier，但两者之间的差异太大，以至于 Xerox 的任何工具都无法适用于 ASN.1。

The tool vendors. The Traders of ASIMOV's "Foundation". A law unto themselves, but vital to the success of the enterprise and contributing immensely to its development in the middle years. 这些工具供应商们。他们是 ASIMOV 的“基金会”的经营者们。他们自成一派，但对企业的发展至关重要，并且在企业成长过程中发挥了极其重要的作用。

It was the mid-1980s before tools began to appear, and these were generally just syntax-checkers and pretty-print programs. It was in the late 1980s that tools as we now know them started to emerge, and the ASN.1 tool vendor industry was borne. (See Chapter 6 in Section I for more about ASN.1 tools). 在 20 世纪 80 年代中期，还没有出现专门用于特定任务的工具。那时出现的工具基本上只是一些语法检查器和格式输出程序而已。到了 20 世纪 80 年代末，我们现在所熟知的那些工具才开始出现，而 ASN.1 工具供应商行业也由此诞生了。（更多关于 ASN.1 工具的信息，请参见第一部分中的第六章。）

Of course, in the early days, all those working on ASN.1 were essentially "users" - employees of computer manufacturers or telecommunications companies, (sometimes Universities), and usually with strong interests in some protocol that was using ASN.1 as its notation for protocol definition. But at the last meeting (1999) of the ASN.1 group, the majority of those around the table had strong links one way or another with the vendor of some ASN.1 tool - ASN.1 had come of age! 当然，在初期阶段，所有从事 ASN 相关工作的人基本上都是“使用者”——他们是计算机制造商或电信公司的员工（有时也是大学的研究人员）。他们通常都非常关注那些使用 ASN 作为协议定义符号的协议。但在最后一次 ASN 小组会议（1999 年）上，与会者中大多数人与某些 ASN 工具的供应商都有直接或间接的联系——于是，ASN 终于迎来了它的“成熟时期”！

There was an interesting transition point in the late 1980s when tool vendors were beginning to appear at Standards meetings, and were complaining that there were some features of the ASN.1 syntax that made it hard for computers to read (the main problem was the lack of a semi-colon as a separator between assignment statements - eventually resolved by introducing a colon into the value notation for CHOICE and ANY values). At that time, there were strong arguments that ASN.1 was not, and was never intended to be, a computer-processable language. Rather it was a medium for communication between one set of humans (those writing protocol standards) and another set of humans (those producing implementations of those protocols). That view was rapidly demolished, and today ASN.1 is seen as very much a computer language, and many of the changes made in the early 1990s were driven by the need to make it fully computer-friendly. 在 20 世纪 80 年代末，有一个有趣的转折点。当时，一些工具供应商开始出现在标准会议上，他们抱怨 ASN.1 语法中有一些特性使得计算机难以读取。主要问题在于，赋值语句之间的分隔符缺乏分号——这个问题后来通过为 CHOICE 和 ANY 类型的值标记添加冒号得到了解决。当时，有人强烈主张认为 ASN.1 并非一种适合计算机处理的语言，它本质上是一种用于人类之间沟通的工具，即编写协议标准的人与实现这些协议的人之间的沟通手段。然而，这一观点很快被推翻了。如今，ASN.1 被视为一种非常适合计算机的语言，而 20 世纪 90 年代初所做的许多改进，都是为了使其更加适合计算机处理。

## 8 Object identifiers 8. 对象标识符

## 8.1 Long or short, human or computer friendly, that is the question 8.1 是长格式还是短格式？是适合人类还是计算机？这就是问题所在。

Object identifiers (I'll use the informal abbreviation OID below) pre-dated the "Information Object" concept by at least five years, although today they are closely associated with that concept. 对象标识符（在下文中我将使用非正式的缩写 OID 来表示）的出现时间，至少早于“信息对象”这一概念五年以上。不过，如今它们与“信息对象”这一概念已经紧密关联在一起了。

Again, what's in a name? Well the length might matter if you are carrying it in your protocol! 再次强调，名字究竟意味着什么呢？如果你在协议中使用了这个名称的话，那么它的长度或许还真有讲究哦！

It was in the mid-1980s that it became apparent that many different groups within OSI had a requirement for unambiguous names to identify things that their protocol was dealing with, and which could be assigned in a distributed fashion by many groups around the world. 在 20 世纪 80 年代中期，人们意识到 OSI 内部有许多不同的组需要一些明确的名称来标识它们所处理的对象，而且这些名称应该可以由世界各地的多个组共同分配。

A similar problem had been tackled a few years earlier in SC6, but with the narrower focus of providing a name-space for so-called "Network Service Access Point Addresses" - NSAP addresses, the OSI equivalent of IP addresses on the Internet. If the reader studies the NSAP addressing scheme, some similarities will be seen to the Object Identifier system, but with the very important difference that the length of NSAP addresses had always to be kept relatively short, whilst for application layer protocols long(ish) object identifiers were considered OK. 在几年前，SC6 中也解决了类似的问题。不过，当时关注的是为所谓的“网络服务接入点地址”提供一个命名空间——即 NSAP 地址。NSAP 地址相当于互联网上的 IP 地址。如果读者仔细研究 NSAP 地址的寻址方案，会发现它与对象标识符系统有一些相似之处。但两者有一个重要的区别：NSAP 地址的长度必须保持较短，而对于应用层协议来说，较长的对象标识符则是可以接受的。

In around 1986 a lot of blood was spilt over the OBJECT IDENTIFIER type, and it could easily have gone in a totally opposite direction (but I think the right decision was eventually taken). This was not a CCITT v ISO fight - by this time the two groups were meeting jointly, and divisions between them were rarely apparent. (That situation continues to this day, where at any given meeting, the various attendees can often claim representation of both camps, but where if they are delegates from one camp or the other, discussion almost never polarises around the two camps.) 大约在 1986 年，关于 OBJECT IDENTIFIER 类型的问题引发了大量的争论。其实，情况很可能会朝着完全相反的方向发展（不过我认为最终还是做出了正确的决定）。这并非是 CCITT 与 ISO 之间的对立关系——当时这两个组织实际上是联合在一起工作的，它们之间的分歧已经很少见了。（这种情况一直持续到现在：在任何一次会议上，与会者往往都能声称代表两个阵营的观点；但如果他们是来自某一阵营的代表，那么讨论几乎不会因为两个阵营的存在而变得两极分化。）

To return to OIDs! The argument was over whether an OID should be as short as possible, using only numbers, or whether it should be much more human-friendly and be character-based, with encouragement to use quite long names as components within it. 现在回到 OID 的问题吧！争论的焦点在于：OID 应该尽可能简短，只使用数字来表示，还是应该采用更人性化的方式，使用字符来表示，并且鼓励使用相当长的名称作为 OID 的组成部分。

The eventual compromise was what we have today - an object identifier tree with unique numbers on each arc, but with a rather loose provision for providing names as well on each arc. In the value notation for object identifiers, the numbers always appear (apart from the top-level arcs, where the names are essentially well-known synonyms for the numbers), but the names can be added as well to aid human-beings. In encodings, however, only the numbers are conveyed. 最终的妥协方案就是我们现在所使用的结构——一个对象标识符树，每个弧上都有一个唯一的数字标识。不过，这种结构也允许为每条弧提供名称。在对象标识符的表示方式中，数字总是会出现在前面（除了最高层的弧线，因为那些弧线的名称实际上是数字的名称），而名称则可以用来帮助人类更好地理解这些标识符。不过，在编码方面，只有数字被用来表示这些标识符。

A further part of the compromise was the introduction of the "ObjectDescriptor" type to carry long human-friendly text, but text that was not guaranteed to be world-wide unambiguous, and hence which was not much use to computers. As stated earlier, the "ObjectDescriptor" type was the biggest damp squib in the whole of the ASN.1 armoury! 另一个妥协措施是引入了“对象描述符”类型，用来存储较长的、易于人类理解的文本。不过，这些文本并不保证在全球范围内具有一致性，因此对于计算机来说并没有太大用处。正如之前提到的， “对象描述符”类型是整个 ASN.1 框架中最大的缺陷之一！

A very similar battle raged - but with pretty-well the opposite outcome - within the X.500 group a year or so later. X.500 names (called "Distinguished Names") are an ASN.1 data type that is (simplifying slightly again) essentially: 大约一年后，X.500 小组内部也发生了一场非常类似的争论——不过结果却截然相反。X.500 中的“知名人士”名称是一种 ASN.1 数据类型。简单来说，这些名称本质上就是：

$$
\begin{array}{l} \text {SEQUENCE OF} \\ \text {SEQUENCE} \\ \left\{\text {attribute - id} \quad \text {TYPE - IDENTIFIER.} \& \text {id}, \right. \\ \left. \text {attribute - value TYPE - IDENTIFIER.} \& \text {Type} \right\} \end{array}
$$

Remember that "TYPE-IDENTIFIER.&id" is essentially a synonym for "OBJECT IDENTIFIER", so it is clear that X.500 names are very much longer than ASN.1 names. 请记住，"TYPE-IDENTIFIER.&id"实际上与"OBJECT IDENTIFIER"是同义词。因此很明显，X.500 格式的名称要比 ASN.1 格式的名称要长得多。

There was pressure in the late 1980s (from groups outside of X.500) for X.500 to support use of a simple single OBJECT IDENTIFER (a so-called "short-form" name) along-side its Distinguished Names (so-called "long-form" names), and I believe it was formally agreed within SC21 that this should happen, but I think it never did happen! 在 20 世纪 80 年代末，有一些来自 X.500 之外团体的压力，要求 X.500 能够同时支持使用简单的单个对象标识符（所谓的“短格式”名称），以及其具有辨识性的名称（所谓的“长格式”名称）。我认为，在 SC21 会议上，大家已经正式同意了这一点，但实际上这一要求从未真正实现！

## 8.2 Where should the object identifier tree be defined? 8.2 那么，对象标识符树应该定义在何处呢？

Another problem with the definition of the OBJECT IDENTIFIER type is that it is not just defining a data type, it is implicitly establishing a whole registration authority structure. “OBJECT IDENTIFIER”类型的定义还存在另一个问题：它不仅定义了一个数据类型，还隐含地建立了一个完整的注册机构结构。

Demarcation disputes. Ugh! 边界划分争议。呃！

This went beyond the remit of the ASN.1 group (a separate group in OSI was charged with sorting out registration authority issues, and produced its own standard). This was a source of continuing wrangling over almost a decade. Initially (mid-1980), it was within ISO that people were saying "The description of the object identifier tree should be moved from ASN.1 to the Registration Authority Standard", but the CCITT people were saying "No-way - ASN.1 users want to be able to read that text as part of the ASN.1 Standard, and control of it should remain with the ASN.1 group." 这一问题超出了 ASN 小组的权限范围。在 OSI 中，有一个独立的团体负责处理注册机构的相关问题，并且他们制定了自己的标准。这一问题在将近十年的时间里一直引发争议。最初（在 1980 年代中期），人们提议将对象标识符树的描述从 ASN.1 标准中分离出来，放到注册机构标准中。但国际电信联盟的标准化人员则坚持认为：“不行——ASN.1 的用户希望将这部分内容作为 ASN.1 标准的一部分来阅读，因此这部分内容应该由 ASN.1 小组来负责。”

It stayed in the ASN.1 Standard until (and including) the 1990 publication. But in the early 1990s, the roles were reversed, and there was pressure from ITU-T (largely from outside the ASN.1 work) to move the text from X.680 (ISO/IEC 8824-1) to X.660 (ISO/IEC 9834-1). There was some opposition within the ASN.1 group itself, but the move happened, and relevant text was deleted from X.680/8824 and replaced by a reference to X.660/9834. Ever since then, there have been various liaisons between the keepers of the respective standards to try to ensure continued consistency! Fortunately, however, the work on the object identifier tree itself was completed long ago and is very stable. (But see the next clause!) 该标准一直遵循 ASN.1 标准规范，直到 1990 年发布的相关文档为止。不过在 1990 年代初，情况发生了转变：ITU-T 方面施加了压力，希望将相关文本从 X.680 标准（ISO/IEC 8824-1）迁移到 X.660 标准（ISO/IEC 9834-1）。尽管 ASN.1 标准委员会内部也出现了一些反对意见，但这一变更最终还是实现了。相关文本从 X.680/8824 标准中删除，并替换为对 X.660/9834 标准的引用。从那时起，各标准维护者之间不断进行沟通，以确保标准的持续一致性。幸运的是，关于对象标识符树的结构的规范早已完成，目前该标准非常稳定。（不过，请继续关注下一节内容！）

## 8.3 The battle for top-level arcs and the introduction of RELATIVE OIDs 8.3 对顶级弧线的争夺以及相对 OID 的引入

The change of name from CCITT to ITU-T was a simple top-level name change, yes? But remember that two of the top arcs of the object identifier tree were "ccitt" and "joint-iso-ccitt". 名称从 CCITT 改为 ITU-T 只是一个简单的顶级名称变更而已，对吧？不过需要注意的是，对象标识符树中最重要的两个分支仍然是“ccitt”和“joint-iso-ccitt”。

Everyone wants to be at the top of the tree, but in this case for good reasons - it reduces the verbosity of their protocols. 每个人都想处于顶尖的位置，但这种情况是有正当理由的——这样做可以减少他们的协议中的冗余内容。

ITU-T proposed two new arcs (with new numbers) for "itu-t" and "joint-iso-itu-t". Those who have read the text associated with figure III-13 will realise that whilst it was not wholly impossible to accede to this request, it would be very difficult! Eventually, the new names were accepted as synonyms for the existing arcs (keeping the same numbers). ITU-T 提出了两个新的名称，分别用于“itu-t”和“joint-iso-itu-t”。那些阅读过与图 III-13 相关的文本的人会明白，虽然完全拒绝这一提议并非完全不可能，但实际上是非常困难的。最终，这些新名称被接受为现有名称的替代方案（同时保留原有的编号）。

It was shortly after this that there became an increased demand by international organizations for object identifier name space using a top arc. Organizations realised that object identifier values they allocated (and used in their protocols) would be shorter if they could get "hung" nearer the top of the tree. ITU-R, the International Postal Union, and the IETF were among organizations expressing (with various degrees of strength) the wish to wrest some top-level arcs from ISO and ITU-T (who were surely never going to use all the ones allocated to them). 就在那时，各国际组织对使用顶级弧号作为对象标识符空间的需求逐渐增加。各组织意识到，如果能够将对象标识符的值放在树的较高层次，那么所分配的值就会更短一些。国际邮政联盟 ITU-R、IETF 等组织都表达了希望从 ISO 和 ITU-T 手中夺取一些顶级弧号的使用权的愿望，不过这些组织的力量程度各不相同。显然，ISO 和 ITU-T 根本不会使用所有分配给它们的弧号。

This issue looks today (1999) as if it is being defused by the addition of a new type called RELATIVE OID. (Yes, at the time of writing it is OID, not OBJECT IDENTIFIER.) A RELATIVE OID value identifies parts of the object identifier tree that sits below some (statically determined) root node, and the encodings of these values only contain the numbers of the nodes beneath that root node, omitting the common prefix. 从 1999 年今天的角度来看，这个问题似乎可以通过引入一种名为“相对 OID”的新类型来解决。在编写本文时，这个术语被称为 OID，而不是 OBJECT IDENTIFIER。相对 OID 的值用于标识对象标识符树中位于某个固定根节点下方的部分节点，这些值的编码仅包含该根节点下方的节点编号，而省略了常见的前缀部分。

This rather simple proposal was a very much cut-down version of an earlier proposal that would have allowed the common prefix to be transmitted in an instance of communication, and then be automatically associated with particular relative oid values that were transmitted later in that instance of communication. 这个相当简单的方案，其实是对之前那个方案的简化版本。在之前的方案中，会允许在通信过程中使用通用前缀，然后该前缀会自动与在通信过程中随后传输的特定相对值相关联。

(It is always very difficult when writing books to avoid them becoming rapidly out of date - you either don't talk about things like RELATIVE OID, or you do, with the danger that a few weeks after publication you find it has either been withdrawn or has been dramatically changed. But in this case, I am fairly confident that it will be added to ASN.1 much as described above.) 在撰写书籍时，避免内容迅速过时总是非常困难——要么就不谈论像相对 OID 这类概念，要么就不得不提及它们，但这样做就有风险：在出版几周后，这些概念可能会被撤销或修改。不过，在这种情况下，我相当有信心，这些概念仍会被添加到 ASN.1 中，就像上面所描述的那样。

## 9 The REAL type 9 真正的类型

The REAL type might seem innocuous enough, but was also the source of controversy around 1986. 真正的类型看起来可能相当无害，但实际上却是 1986 年争议的根源。

Probably just an academic exercise - nobody uses REAL in actual protocols! But it produced its own heated moments. 这可能只是一种学术上的练习而已——在实际的协议中根本没有人使用“REAL”这个术语！不过，这项研究还是引发了一些激烈的讨论。

Everyone agreed we had to have it, but how 大家都认为我们必须拥有它，但是具体该如何做呢？

to encode it? (The actual encoding eventually agreed is fully described in Section II Chapter 2 clause 3.5, and the interested reader should refer to that.) 如何对其进行编码呢？（具体的编码方式在第二章第二节的 3.5 条款中有详细说明，有兴趣的读者可以参考该部分内容。）

There were several issues, of which binary versus character encodings was one. As usual, the easy compromise was to allow both, but that produced problems later when canonical encodings were needed, and the rather dirty fudge had to be taken of saying that base 2 and base 10 values that are mathematically equal are regarded as distinct abstract values, and hence encode differently, even in the canonical encoding rules. 存在几个问题，其中之一就是二进制与字符编码的问题。像往常一样，最简单的解决方案是允许同时使用这两种编码方式。但是，当需要使用规范化的编码方式时，这个问题就出现了。于是，人们不得不采取一种较为复杂的解决方案：规定那些在数学上相等的二进制和十进制数值，实际上被视为不同的抽象数值，因此在使用规范化编码规则时，它们的编码方式也会有所不同。

But the main problem was with the binary encoding format. There was a (fairly new) standard at that time for floating point formats for computer systems, and it was generally used by people handling floating point in software, but not by existing hardware (later it got implemented in chips). Naturally, there were those that advocated use of this format for ASN.1 encodings. 不过，主要问题在于二进制编码格式的问题。当时有一种新的浮点数编码标准被广泛应用，这种标准被软件系统用来处理浮点数运算，但现有的硬件却并不支持这种格式（后来这种标准才被应用到芯片中）。当然，也有一些人主张将这种格式用于 ASN.1 编码。

The counter-argument, however, eventually prevailed (and again I think this was the right decision). The counter-argument was that we were some time away from a de facto standard for floating point formats, and that what mattered was to find a format that could be easily encoded and decoded with whatever floating point unit your hardware possessed. 不过，反对意见最终还是占了上风（我认为这确实是一个正确的决定）。反对者认为，我们距离实现一种公认的浮点运算格式还有一段时间，重要的是要找到一种能够轻松地被各种硬件设备支持的浮点运算格式。

This principle dictated, for example, the use of a "sign and magnitude" (rather than "two's complement" or "one's complement") mantissa, because "sign and magnitude" can be easily generated or processed by hardware of the other two forms, but the converse is not true. It was also this principle that gave rise to the rather curious format (not present in any real floating point hardware or package) involving the "F" scaling factor described in 3.5.2. 这一原则规定，例如，应该使用“符号与数值”这种形式来表示小数部分，而不是使用“二进制补数”或“原码补数”。因为另一种形式的补数很容易由硬件生成或处理，但反之则不成立。正是这一原则催生了第 3.5.2 节中提到的“F”缩放因子这种奇特的形式。不过，这种形式并不存在于任何真正的浮点运算硬件或封装中。

Finally, there was a lot of pressure at the time to support specific encodings that would identify "common and important" numbers that otherwise would have no finite representation, such as "3.14159..." and "2.7183...", and also values such as "overflow", and "not-a-number", but in the end all that was added was encodings to identify PLUS-INFINITY and MINUS-INFINITY, with plenty of encoding space for identification of other things related to type REAL later. The pressure to provide these additional encodings evaporated, and no extensions have been made, nor do any seem likely now. 最终，当时确实存在很大的压力，需要支持一些特定的编码方式，以便能够表示那些“常见且重要”的数字，比如“3.14159…”和“2.7183…”。此外，还需要处理诸如“溢出”和“非数字”等数值的编码问题。不过，最终只增加了用于表示 PLUS-INFINITY 和 MINUS-INFINITY 的编码方式，而用于表示与 REAL 类型相关的其他数值的编码空间则被留给了以后使用。对于提供这些额外编码方式的压力已经消失了，因此再也没有进行任何扩展，现在看来也不太可能再有所发展了。

## 10 Character string types - let's try to keep it short! 10 种字符串类型——我们尽量简短地介绍一下吧！

The history of the development of encodings for "characters" (and discussion on just what a "character" is) is much broader than ASN.1. ASN.1 has not really contributed to this work, but rather has done its best to enable ASN.1 users to have available notation that can let them reference “字符”编码的发展历史，以及关于“字符”究竟是什么的讨论，其范围远比 ASN.1 要广泛得多。ASN.1 实际上并没有对这一领域做出太多贡献，而是尽力为 ASN.1 用户提供一种易于使用的表示方式，使他们能够方便地引用相关的内容。

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/54379e17-c034-430b-894c-f77661f731e5/43ed84c2bbf11bb1e2e3922d86dee2afa43772df2c5c809e2364a29fac7c9cd2.jpg)

in their protocols, clearly and simply, these various character encoding standards. 在他们的协议中，这些不同的字符编码标准都被表述得清晰明了。

The result, however, has been a steady growth in the number of character types in ASN.1 over the years, with a lot of fairly obsolete baggage being carried around now. 然而，多年来，ASN1 中字符类型的数量却持续增加。现在，有很多已经相当过时的字符类型仍然被使用着。

Section II Chapter 2 promised that we would here provide a description of the history of the development of character encoding schemes, and the impact this had on ASN.1 over the years. What follows is the main parts of that history (but detail is sometimes lacking, and it is not a complete history - that is left to other texts), with the impact on ASN.1. 第二部分第二章承诺会介绍字符编码方案的发展历史，以及这一历史对 ASN.1 影响的相关内容。以下便是该历史的主要部分描述（不过有时缺乏细节，且这并不是完整的历史记载——完整的历史内容可参考其他资料）。同时也会说明这些历史对 ASN.1 的影响。

## 10.1 From the beginning to ASCII 10.1 从最初到 ASCII 编码的演变过程

The earliest character coding standards were used for the telegraph system, and on punched paper tape and cards. The earliest formats used 5 bits to represent each character (32 possible encodings), with an encoding for "alpha-shift" and "numeric-shift" to allow upper-case letters, digits, and a few additional characters. 最早的字符编码标准被用于电报系统，以及穿孔磁带和卡片上的数据传输。最早的编码格式使用 5 位来表示每个字符（共有 32 种可能的编码方式），同时引入了“字母移位”和“数字移位”的编码方式，以便表示大写字母、数字以及一些额外的字符。

Five-bit codes, seven-bit codes. And to come later, 16 bit codes and 32 bit codes! I doubt anyone will EVER suggest 64 bit codes ... but on second thoughts, how many bits does Microsoft Word take to indicate fonts etc? (OK, that is usually per paragraph not per character, but in the future ... ?) 五位代码、七位代码……将来还会有十六位代码和三十二位代码！我怀疑是否真的会有人建议使用六十四位代码……不过再想想，微软的 Word 软件究竟需要多少位来表示字体等信息呢？（好吧，通常这是按段落来计算的，而不是按字符来计算的，不过将来会不会有所不同呢？）

Later the use of 7 bits with an eighth parity bit 后来，人们开始使用 7 位数据位，再加上一个第八位用于指示奇偶校验状态。

became the de facto standard, and this eventually became enshrined in the 8-bit bytes of current computers. The ASCII code-set is the best-known 7-bit encoding, with essentially 32 so-called "control characters" (many of whose functions related to the framing of early protocol packets) and 94 so-called "graphics characters" (printing characters), plus SPACE and DEL (delete). (DEL, of course, is in the all-ones position - 127 decimal - because on punched paper tape the only thing you could do if you had made a mistake was to punch out all the rest of the holes - you could not remove a hole!). 它成为了事实上的标准，最终被固化在了当前计算机的 8 位字节中。ASCII 编码系统是最为著名的 7 位编码方式，它包含 32 个所谓的“控制字符”（许多控制字符的功能与早期协议数据包的构造有关），以及 94 个所谓的“图形字符”（用于打印的字符）。此外，还有空格键和删除键。当然，删除键处于全 1 的状态——十进制为 127——因为在穿孔纸带中，如果你犯了错误，你只能将所有其他孔都打掉，而无法移除某个孔。

ASCII has formed the basis of our character coding schemes for close on forty years, and is only now being replaced. ASCII is in fact the American variant of the international standard ISO 646, which defines a number of "national options" in certain character positions, and many other countries defined similar (but different) national variants. The UK variant was often called (incorrectly!) "UK ASCII". ASCII 标准已经成为了我们字符编码体系的基础，已经使用了近四十年之久，而现在才刚刚开始被取代。实际上，ASCII 只是国际标准 ISO 646 的美国版本而已。ISO 646 标准在某些字符位置定义了多种“国家选项”，许多其他国家也定义了类似但不同的国家版本。英国的版本常被误称为“UK ASCII”。

## 10.2 The emergence of the international register of character sets 10.2 国际字符集注册表的出现

Early computer protocols used 7 bit encodings, and retained the use of the eighth bit as a parity bit. That is why we find today that if you wish to send arbitrary binary over e-mail, it gets converted into a seven-bit format, and more or 早期的计算机协议使用 7 位编码，并保留了第 8 位作为奇偶校验位。因此，如今当我们希望通过电子邮件发送任意二进制数据时，这些数据都会被转换为 7 位格式。

Providing encodings for all the characters in the world - first attempt, and not a bad one. 为世界上所有的字符提供编码方案——这是第一次尝试，而且成果并不差。

less doubles in size! More modern protocols (such as those used to access Web pages) provide what is called "full eight-bit transparency" and the eighth bit is a perfectly ordinary bit which can carry user information. 大小增加了两倍！更现代的协议（比如用于访问网页的那些协议）提供了所谓的“全八位元透明性”功能，而第八位则是一个普通的位，可以用来存储用户信息。

As protocols developed, the use of a parity bit was very quickly dropped in favour of a Cyclic Redundancy Code (CRC) as an error detecting code on a complete packet of information, and character coding schemes were free to move to an 8-bit encoding capable of representing 256 characters. 随着协议的不断发展，使用奇偶校验位的做法很快就被放弃了，取而代之的是使用循环冗余码（CRC）作为完整信息包的错误检测机制。同时，字符编码方式也转向了 8 位编码，从而能够表示 256 种字符。

There were two developments related to this: The first of these was developed as early as 1973. This was ISO 2022, which established a framework (based on ISO 646) for the representation of all the characters in the world. (I am afraid the following description is of necessity somewhat simplified - the so-called multiple-byte formats and the dynamically redefinable character sets of 2022 are not mentioned in what follows.) 与此相关的有两项发展：第一项是在 1973 年提出的。这就是 ISO 2022 标准，它基于 ISO 646 标准，建立了一个框架，用于表示世界上所有的字符。（不过，以下描述不得不有所简化——所谓的多字节格式以及 ISO 2022 中可动态重新定义的字符集在描述中并未提及。）

The way ISO 2022 worked was to identify the first two columns (32 cells holding control characters) of the ASCII structure as cells that could contain (represent, define) any so-called Cset of characters, and the remaining 94 positions (keeping the SPACE and DEL positions fixed as SPACE and DEL) as cells that could contain (represent, define) any so-called G-set. Moreover, within the C-set positions, the ASCII ESC character would always be kept at that precise position, so a C-set of characters was in fact only allowed to be 31 control functions. ISO 2022 标准的工作原理是：将 ASCII 结构中的前两列（共 32 个单元格，用于存放控制字符）视为可以存储任意字符集的单元格；剩余的 94 个位置则用于存储任意 G 集。此外，在字符集内部，ASCII 中的 ESC 字符始终被固定位于那个位置。因此，字符集实际上最多只能包含 31 个控制功能。

The old parity bit could be used to identify one of two meanings (one of two character sets) for encodings of C-sets, called the C0 and the C1 set. If one of the C-sets in use included control characters for "shift-outer" and "shift-inner" (which affected the interpretation of G-set but not Cset codes), then the combination of using these together with the old parity bit enabled reference to (encodings of) up to four G-sets, called G0, G1, G2, and G3. 旧的奇偶位可以用来区分 C 集编码中的两种含义（即两种字符集），分别称为 C0 和 C1 集。如果使用的 C 集中包含用于“shift-outer”和“shift-inner”的控制字符（这些字符会影响 G 集的解析，但不会影响 C 集编码），那么结合使用这些字符与旧的奇偶位，就可以实现对多达四种 G 集的编码的引用，这四种 G 集分别称为 G0、G1、G2 和 G3。

Finally, there was the concept of a register of C-sets and G-sets that, for each register entry, would assign characters to each position in the ASCII structure. At any point in time, up to two C-sets and up to four G-sets could be "designated and invoked" into the C0, C1, G0, G1, G2, and G3 positions. The ESC character (required to be present in the same position in all C-sets, remember) was given a special meaning. Each register entry contained the specification of binary codes that could follow the ESC character to "designate and invoke" any register entry into either a C0 or C1 position (for C entries) or into one of the G0 to G3 positions (for G-entries). 最后，还有 C 集和 G 集的注册表这一概念。对于每个注册表条目，都可以为 ASCII 结构中的每个位置分配相应的字符。在任何时刻，最多可以有两个 C 集和四个 G 集被“指定并调用”到 C0、C1、G0、G1、G2 和 G3 这些位置中。ESC 字符（需要出现在所有 C 集的相同位置）具有特殊的含义。每个注册表条目都包含了二进制代码的规范，这些代码可以跟随 ESC 字符，以“指定并调用”某个注册表条目进入 C0 或 C1 位置（对于 C 集而言），或者进入 G0 到 G3 中的任何一个位置（对于 G 集而言）。

All that remained was to produce the register entries! This became the "International Register of Coded Character Sets to be used with Escape Sequences", commonly referred to as "the international register of character sets". 剩下的工作就是制作相应的登记条目了！这个登记条目被称之为“用于与转义序列一起使用的编码字符集国际登记册”，通常简称为“国际字符集登记册”。

The register was originally maintained by the European Computer Manufacturer's Association (ECMA), and grew to well over 200 entries covering virtually the entire world's character sets. Today it is maintained by the Japanese Industrial Standards Committee (JISC), the Japanese equivalent of BSI and ANSI and AFNOR and DIN. Both ECMA and JISC provide free copies and free up-dates to interested parties, but JISC now maintains a web-site with every register entry on it. (See Appendix 5 if you want to access this site). 该注册表最初由欧洲计算机制造商协会（ECMA）负责维护，后来其收录的条目数量增长到了 200 多个，几乎涵盖了全球所有的字符集。如今，该注册表由日本工业标准委员会（JISC）负责维护，JISC 相当于英国的 BSI、美国的 ANSI 以及法国的 AFNOR 和德国的 DIN。ECMA 和 JISC 都为感兴趣的人士提供免费的注册表副本以及定期更新服务。不过，JISC 现在有一个网站，上面包含了所有的注册表条目。（如需访问该网站，请参见附录 5。）

ASN.1 provides full support for ISO 2022, with GraphicString and GeneralString, and relies on the International Register for the definition of many of its other character string types. ASN.1 完全支持 ISO 2022 标准，其中包括 GraphicString 和 GeneralString 类型。此外，许多其他字符串类型的定义也依赖于国际注册标准。

## 10.3 The development if ISO 8859 10.3 ISO 8859 标准的发展历程

ISO 8859 came much later (in 1987), and came in a number of "parts". ISO 8859 标准出现得较晚，大约在 1987 年才被提出。该标准包含多个版本。

The problem with the 2022 scheme was that because of the inclusion of ESC sequences to make new designations and invocations, encodings for characters were not fixed length. 2022 年的方案存在的问题是，由于需要包含用于创建新标识和调用的 ESC 序列，因此字符的编码长度并不固定。

Giving European languages full coverage with an efficient encoding - a standard ignored by ASN.1! Who cares about Europe in International Standardization? (President of the European Commission, please do not read this!) 为欧洲语言提供全面的覆盖，采用高效的编码方式——这种标准被 ASN.1 所忽视！在国际标准化中，谁会在乎欧洲呢？（欧洲委员会主席，请不要阅读此内容！）

ISO 8859 was designed to meet the needs of European languages with a fixed (eight bits per character) encoding. Each part of 8859 specified ASCII as its so-called "left half" - the encoding you got with the old parity bit set to zero, and a further 94 printing characters in its "right-half" designed to meet the needs of various European languages. So 8859-1 is called "Latin alphabet No.1", and in addition to ASCII provides characters with grave, circumflex, acute accents, cedillas, tildas and umlauts, together with a number of other characters. 8859-6 is called "Latin/Arabic", and contains arabic characters in its right-half. ISO 8859 标准是为了满足使用固定字符编码方式的欧洲语言而设计的。8859 标准中的每一部分都包含了 ASCII 字符集作为“左半部分”——即那些在旧奇偶位被设置为 0 时生成的编码方式。而“右半部分”则包含了额外的 94 个用于欧洲语言的特殊字符。因此，8859-1 被称为“拉丁字母第 1 版”，除了 ASCII 字符外，它还提供了带着重号、尖号、连音符号、连字符以及 umlaut 符号的字符。8859-6 则被称为“拉丁/阿拉伯语版”，其右半部分包含了阿拉伯语字符。

ASN.1 never provided any direct support for 8859, although 8859 encodings were quite often used in computer systems in Europe. ASN.1 从未为 8859 编码提供过直接的支持，不过在欧洲的计算机系统中，8859 编码经常被使用。

## 10.4 The emergence of ISO 10646 and Unicode 10.4 ISO 10646 标准和 Unicode 标准的出现

## 10.4.1 The four-dimensional architecture 10.4.1 四维架构

A very major development in the early 1990s (still, almost a decade later, to work its way completely into computer systems and protocols) was the development of a completely new frame-work for encoding characters, wholly unrelated to the ASCII structure. (But of course capable of encoding ASCII characters!) 在 20 世纪 90 年代初，有一个非常重要的发展（尽管至今仍有一半的时间过去了，这一技术才完全融入了计算机系统和协议中）。那就是出现了一种全新的字符编码框架，这种框架与 ASCII 结构完全无关。（不过，它当然能够编码 ASCII 字符！）

Probably the most important development in character set encoding work EVER. It is hard to see a likely change from this architecture at any time in the future. Wow! At ANY time in the future? Yup. 这或许是有史以来在字符集编码领域最重要的进展。很难想象未来任何时候都会出现与当前架构不同的变化。哇！真的在任何时候都可能发生这样的变化吗？没错。

Here you must look at figure IV-1 (yes, the first figure in this chapter - you must be feeling deprived!). This shows a four-dimensional structure (compared with the ASCII 2-dimensional code table). 请查看图 IV-1（没错，这是本章的第一张图——你一定觉得很有趣吧！）该图展示了一个四维结构（与 ASCII 二维代码表相比）。

Figure IV-1 shows a street of 256 houses. Each house has 256 "planes" in it (positioned vertically, and running left to right within the house on the street). Each plane has 256 rows in it (running top to bottom within each plane of each house). And each row has 256 cells in it (running from left to right within each row). Each cell can contain (define, represent) a different character. (Actually, the correct technical term for a house is a "group" - "house" is not used, but I prefer to call them houses!) 图 IV-1 展示了一条由 256 栋房屋构成的街道。每栋房屋内部包含 256 个“平面”，这些平面垂直排列，在街道上从左到右延伸。每个平面内有 256 行，每行包含 256 个单元格。每个单元格可以容纳不同的字符。（实际上，对一栋房屋来说，更合适的术语是“组”——实际上并没有使用“房屋”这个术语，但我更愿意将其称为“房屋”）

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/54379e17-c034-430b-894c-f77661f731e5/96ab0308e7b2832f374d449e732f3769ad597255c57b28efc18901d9d39e21f0.jpg)

Figure IV-1: 256 houses each with 256 planes each with 256 rows each with 256 cells 图 IV-1：共有 256 栋房屋，每栋房屋中有 256 个平面；每个平面包含 256 行，每行中有 256 个单元格。

The very first plane (number zero) of the first house (number zero) is called the Basic Multilingual Plane or "BMP". The first row of that plane contains Latin Alphabet No 1 (8859-1), and hence contains ASCII in its left half. 第一个房子中的第一个平面，被称为基础多语言平面或“BMP”。该平面的第一行包含拉丁字母第 1 种形式（8859-1），因此其左侧半部分包含了 ASCII 字符。

(In the early drafts of ISO 10646, the other parts of 8859 occupied successive rows, and hence ASCII appeared multiple times, but this was removed in the "fight" with Unicode (see below), and the other parts of 8859 only have their right-hand halves present.) 在 ISO 10646 标准的早期版本中，8859 字符集的其他部分占据了连续的行位置，因此 ASCII 字符出现了多次。不过，在与 Unicode 的“竞争”过程中，这一情况被解决了（详见下文）。现在，8859 字符集的其他部分只显示其右侧的部分内容而已。

Notice that any cell of any row of any plane of any house can be identified by four values of 0 to 255, that is to say, by 32 bits. So in its basic form ISO 10646 is a 32-bits per character encoding scheme. 注意，任何房屋中任何一行中的任何单元格都可以用 4 个 0 到 255 之间的数值来表示，也就是说，用 32 位来表示。因此，在基本形式下，ISO 10646 是一种每字符 32 位的编码方案。

Notice also that the numerical value of these 32 bits for ASCII characters is just the numerical value of those characters in 7-bit ASCII - the top 25 bits are all zero! 请注意，这 32 位数值实际上代表了 7 位 ASCII 字符的字符数值——前 25 位都是 0！

Now, it is a sad fact of life that if 现在，这是一个令人遗憾的事实：如果……

• You take all the characters there are in the world (defining things like "a-grave" and "acircumflex" and even more complicated combinations of scribbles used in the Thai language as separate and distinct characters requiring a fixed length encoding); and • 你需要处理世界上所有存在的字符（比如“a-grave”、“acircumflex”，以及泰语中那些更复杂的组合字符；这些字符都是作为独立的字符来定义的，需要采用固定长度的编码方式来表示）；

You admit that glyphs (scribbles) in the Chinese and Japanese and Korean scripts that look to a Western eye to be extremely similar are actually distinct characters that need separate encodings; and 你承认，那些在中文、日文和韩文书写系统中出现的符号，从西方人的视角来看似乎非常相似，但实际上它们是不同的字符，因此需要不同的编码方式。

You include all the scribbles carved into Egyptian tomb-stones and on bark long-preserved in deepest Africa; and 你包含了所有刻在埃及墓碑上、以及保存在非洲最偏远地区的树皮上的文字痕迹；

• You include ASCII multiple times by putting the whole of each part of 8859 into successive rows of the BMP; then • 你通过将 8859 字符集的每一部分都单独放在 BMP 的连续行中，从而实现了对 ASCII 字符的多次包含；然后……

you find that there are nowhere near 2 to the power 32 "characters" you would want to encode, but that there are very significantly more than 2 to the power 16. 你会发现，实际上需要编码的字符数量远远超过了 2 的 16 次方个。而 2 的 32 次方个字符则远远不足以满足需求。

The ISO 10646 structure permits all such characters to be represented with a fixed 32 bits per character, but is this over-kill? Can we manage with just 16 bits per character if we do some judicious pruning? ISO 10646 标准允许用固定的 32 位空间来表示所有字符。不过，这种规定是否过于繁琐了呢？如果我们进行一些合理的优化，使用 16 位空间来表示字符是否就足够了呢？

## 10.4.2 Enter Unicode 10.4.2 输入 Unicode 编码

(For a pointer to Unicode material on the Web, see Appendix 5). （如需了解网络上关于 Unicode 的相关资料，请参阅附录 5。）

Whilst the ISO group JTC1 SC2 was beavering away trying to develop ISO 10646, computer manufacturers were independently getting together to recognise 虽然 ISO 的 JTC1 SC2 工作组一直在努力制定 ISO 10646 标准，但各计算机制造商则各自为政，试图确定自己的标准。

The manufacturers flex their muscle. 32 bits per character is not necessary or sensible for commercially important character sets! 16 bits can be made to work. 这些制造商正在展示他们的实力。对于具有商业价值的字符集来说，每个字符使用 32 位并不是必要或合理的做法！使用 16 位就能满足需求了。

that neither the ISO 2022 nor the ISO 8859 schemes were adequate for the increasingly global communications infrastructure and text processing requirements of the world, but they jibbed at going to a full 32 bits per character. Can't we make 16 bits suffice? 无论是 ISO 2022 还是 ISO 8859 标准，都不足以满足日益全球化的通信基础设施以及文本处理需求。而且，这两种标准都只支持 32 位字符的表示方式，这显然不够。难道 16 位就能满足需求吗？

Well, we can reverse some of the decisions taken above. Let's ignore Egyptian hierogplyphs and anything of interest only to librarians. Let's also introduce the concept of combining characters with which we can build scribbles like a-grave etc (this does not save much for European languages, but saves a lot for Eastern languages such as Thai). Of course, from one point of view, use of combining characters means we no longer have a fixed length encoding for each character, but that depends on your definition of what is a character! 嗯，我们可以撤销上面做出的一些决定。让我们忽略埃及象形文字以及其他只有图书馆员才感兴趣的内容吧。同时，我们还可以引入字符组合的概念，这样就能构建出像“a-grave”这样的符号了（这种方法对欧洲语言影响不大，但对像泰语这样的东方语言却有很大帮助）。当然，从某种角度来看，字符组合的使用意味着我们不再需要为每个字符设定固定的长度编码，因为这取决于你对“字符”的定义！

Finally, let us perform "Han unification" or "CJK Unification" to produce a "unified code" or "Unicode". CJK Unification means that we look at the scribbles in the Chinese (C), Japanese (J), and Korean (K) scripts with a western eye, and decide that they are sufficiently similar that we can assign all three similar scribbles to a single cell in our street of houses. 最后，让我们执行“汉文统一”或“CJK 统一”操作，以创造出一种“统一编码”或“Unicode”。CJK 统一指的是用西方的眼光来审视中文、日文和韩文中的各种字符，并认为这些字符之间具有足够的相似性，因此我们可以将这三种相似的字符都归到同一个“单元格”中。

Now we have cracked it! There are less than two to the power sixteen (important) characters in the world, and we can fit them all into the Basic Multi-lingual Plane and use just 16 bits per character to represent them. 现在我们成功解决了这个问题！这个世界中的角色数量少于 2 的 16 次方个（数量相当有限），因此我们可以将所有角色都容纳到基础多语言层面中，并且每个角色只需要使用 16 位来存储信息即可。

Of course, when the final balloting to approve the ISO 10646 draft ocurred, there were massive "NO" votes, saying "replace it with Unicode"! 当然，当进行最终投票以通过 ISO 10646 标准草案时，有大量的“反对”投票，人们主张用 Unicode 来替代该标准！

## 10.4.3 The final compromise 10.4.3 最终的妥协方案

ISO 10646 was published as an International Standard in 1993 (about 750 pages long!), and the Unicode specification was published in 1992 by Addison Wesley on behalf of the Unicode Consortium, with Version 2 appearing in 1996. ISO 10646 标准于 1993 年被发布为国际标准（共约 750 页！）。而 Unicode 规范则由 Addison Wesley 在 1992 年代表 Unicode 联盟发布，其第二版则于 1996 年推出。

And the amazing thing about international standardization is that compromises ARE often reached, and standards agreed. 而国际标准化令人惊叹的地方在于，往往能够达成妥协，并共同制定标准。

Unicode and ISO 10646 were aligned: the CJK unification and the inclusion of combining characters was agreed, and the Basic Multi-lingual Plane of ISO 10646 was populated with exactly the same characters as appeared in the Unicode specification, and close collaboration has continued since. Unicode 和 ISO 10646 实现了对齐：中日文字的统一以及组合字符的纳入得到了认可。ISO 10646 的基本多语言平面中使用的字符与 Unicode 规范中的字符完全一致。自那以后，双方一直保持着密切的合作关系。

However, important differences remained in the two texts. The ISO text describes three "levels of implementation" of ISO 10646. In level 1, combining characters are forbidden. Everything is encoded with the same number of bits, 32 (UCS-4) bits if you want the whole street, or 16 (UCS-2) bits if you just want the characters in the Basic Multi-lingual Plane. In level 2, you can use combining characters, but only if the character you want is not present in a populated cell (this forbids the use of "a" with the combining character "grave" to get "a-grave"). In level 3, anything goes. Unicode does not describe these levels, but it is in the spirit of Unicode to use combining characters wherever possible. 不过，这两份文本仍然存在一些重要的差异。ISO 标准文本规定了 ISO 10646 的三种“实施级别”。在一级实施中，禁止使用字符组合。所有字符都用相同的位数进行编码：如果需要完整街道信息，则使用 32 位（UCS-4 格式）；如果只需要基本多语言平面中的字符，则使用 16 位（UCS-2 格式）。在二级实施中，可以使用字符组合，但前提是目标字符不存在于某个已填充的单元格中（这样就能避免像“a”与组合字符“grave”组合成“a-grave”这种情况）。在三级实施中，则完全允许使用字符组合。Unicode 标准并没有明确描述这些级别，但实际上，只要可能，就应该尽可能使用字符组合。

There are also other differences between the texts that do not relate to character encoding (and hence are irrelevant to ASN.1): the Unicode specification contains some excellent classificatory material that says what characters should be regarded as numbers, upper/lower-case mappings, and so on; such text is missing from ISO 10646. 这些文本之间还存在其他一些差异，这些差异与字符编码无关，因此与 ASN.1 无关。例如，Unicode 规范中包含了一些非常有用的分类指南，这些指南规定了哪些字符应该被视为数字，以及大小写字母的映射等细节；而 ISO 10646 标准中并没有这些内容。

After the initial publication of Version 1 of Unicode and of ISO 10646, work continued. There are now characters in cells outside of the BMP, but both groups have agreed a mechanism for referencing them within a 16-bit encoding scheme (called UTF-16 - Universal Transformation Function 16) by using reserved characters in the BMP as escape characters to effectively designate and invoke other planes into the BMP position (although that is not the terminology used). 在 Unicode 版本 1 和 ISO 10646 发布之后，相关工作继续展开。现在，在 BMP 之外的单元格中也可以使用字符了。不过，双方都同意在 16 位编码方案中引用这些字符的一种机制——即使用 BMP 中的保留字符作为转义字符，来指代 BMP 中的其他字符层。虽然这种机制并不是官方使用的术语。

Another extremely important development was the definition of UTF-8, briefly described in clause 12 of Section II Chapter 2. This provides a variable number of octets per character, but with all ASCII characters represented with just one octet, with their normal ASCII encoding (with the top bit - the old parity bit - set to zero). 另一个非常重要的进展是 UTF-8 编码标准的定义，这一标准在第二章第二节的第 12 条中有简要描述。该编码方式允许每个字符使用不同数量的八位元来表示，但所有 ASCII 字符都只需用一个八位元就能表示出来，其编码方式与普通 ASCII 编码相同（即最高位——也就是原来的奇偶校验位——被设置为 0）。

For in-core handling of characters in programming languages (and operating system interfaces), computer vendors are supporting 16 bits (usually) or 32 bits (some) or both representations of characters. But for storage on disk or for transfer, UTF-8 is proving a very popular format. 在编程语言（以及操作系统接口）中处理字符时，各计算机供应商通常支持 16 位、32 位或同时支持这两种字符表示方式。不过，在磁盘存储或传输过程中，UTF-8 格式却成为了非常流行的格式。

## 10.5 And the impact of all this on ASN.1? 10.5 那么，这一切对 ASN.1 有什么影响呢？

Current ASN.1 support for character sets has been described in Section II, and it should now be possible for the reader to relate that text to the development of character set standards. The history of character set work in ASN.1 关于 ASN.1 中字符集支持的现行规范，已在第二部分中进行了描述。现在，读者应该能够将这些内容与字符集标准的发展联系起来理解了。ASN.1 中字符集相关规范的历史发展情况也已在相关章节中有所介绍。

On the character set front, ASN.1 has just rolled with the punches. It has not seriously contributed to either repertoire definitions or to encodings. What it HAS tried to do is to provide simple notational support for referencing character set standards. 在字符集方面，ASN.1 确实做出了不少努力。不过，它并没有真正对字符集的定义或编码方式产生实质性影响。它所尝试的是提供一种简单的符号体系，以便引用字符集标准。

has, however, been a long up-hill struggle to try to meet the demands of its users. It has not always succeeded in keeping everybody happy! 不过，为了满足用户的需求，公司一直都在经历着艰难的努力。虽然它并不总是能够让每个人都满意！

X.409 made no use of any of the ISO character set standards apart from ISO 646 (equal to CCITT International Alphabet #5), which it used in the definition of ISO646String (no control characters) and IA5String (control characters included). "ISO646String" is still a permitted type, but the synonym "VisibleString" is preferred. NumericString and PrintableString were also present in X.409, but with the character repertoires and the encodings hard-wired into ASN.1 (as they still are today). X.409 标准并未使用任何 ISO 字符集标准，只采用了 ISO 646 标准（等同于 CCITT 国际字母表第 5 号）。在定义 ISO646String 类型时，它使用了 ISO 646 标准；而在定义 IA5String 类型时，则包含了控制字符。不过，ISO646String 类型仍然是允许使用的类型，但更推荐使用 VisibleString 这个同义词。在 X.409 标准中，还定义了 NumericString 和 PrintableString 类型，但这些类型的字符集和编码方式都是硬编码在 ASN.1 中的，这一点与现在的情况相同。

The only other two character string types in X.409 were T61String (with the preferred synonym today of TeletexString) and VideotexString, which were defined by reference to what was then Recommendation T.61 and T.100 and T.101. 在 X.409 标准中，另外两种字符串类型分别是 T61String（如今更常用的别名为 TeletexString）和 VideotexString。这两种类型的定义参考了当时相关的建议标准 T.61、T.100 和 T.101。

In the early 1980s, writers of ISO standards had to get special permission to reference any specification that was not an ISO standard, so TeletexString and VideotexString posed some problems. The decision was taken (when the re-write that produced ISO 8824 and ISO 8825 was done) to re-cast the definitions (with no technical change!) in terms of references to the international register of character sets described earlier, and this was successfully accomplished (by adding some new register entries!). 在 20 世纪 80 年代初，制定 ISO 标准的人员需要获得特别许可，才能引用那些并非 ISO 标准的规范。因此，TeletexString 和 VideotexString 这类规范确实带来了一些问题。不过，在重新编写导致 ISO 8824 和 ISO 8825 标准诞生的过程中，人们决定重新定义这些规范（而不进行任何技术上的修改），并将这些定义与之前提到的国际字符集注册表进行关联。这一做法取得了成功，同时还增加了一些新的注册项。

At the same time, GraphicString and GeneralString were added to provide full support for the International Register. 同时，还增加了 GraphicString 和 GeneralString 功能，以全面支持国际注册体系。

There were two problems with this: first, new entries were being continually made to the register, so it was very unclear what implementation of GraphicString and GeneralString really meant - these were open-ended specifications. Second, and perhaps more importantly, recasting TeletexString as a reference to particular register entries effectively "froze" it at the 1984 T.61 definition, but many countries made (successful) attempts to get their scripts added to the teletex Recommendations and were (perhaps not surprisingly!) annoyed that they were still not part of the formal definition of TeletexString in ASN.1! 这个问题主要有两点：首先，注册表中不断有新的条目被添加进来，因此很难明确 GraphicString 和 GeneralString 到底意味着什么——这些都属于不明确的规定。其次，或许更为重要的是，将 TeletexString 重新定义为对特定注册表的引用实际上使得它在 1984 年的 T.61 标准中就固定了下来。不过，许多国家都试图将自己的脚本纳入 Teletex 推荐标准之中，但他们却很失望地发现，这些脚本仍然不在 ASN.1 中 TeletexString 的正式定义范围内！

Eventually the political pressure to change TeletexString in ASN.1 became just too great, and in 1994 a whole raft of new register entries was added as permissible entries to designate and invoke within a TeletexString encoding. What about existing implementations of existing protocols? Political pressure is no respecter of minor technical matters like that! The formal definition of TeletexString changed! 最终，要求改变 TeletexString 在 ASN.1 中的使用的政治压力变得难以承受。于是，在 1994 年，大量新的注册项被添加到 TeletexString 编码中，以作为可使用的标识符。那么，现有的协议实现怎么办呢？对于这种次要的技术问题，政治压力是不考虑任何因素的！因此，TeletexString 的正式定义发生了改变。

There was another change that also caused some upsets. Formally, VisibleString and IA5String referred to register entry #2, which was the so-called "International Reference Version" of ISO 646 (but virtually everyone - incorrectly - interpreted that as "ASCII"). But ISO 646 was changed in the late 1980s to introduce the "dollar" character - present in ASCII, but not in the International Reference Version of ISO 646. So ASN.1 changed the reference to register entry #6 (ASCII). At the same time it changed the default G0 set at the start of all GraphicString and GeneralString encodings from #2 to #6. This caused great anger from the X.400 group, who now recommend that in these encodings the G-sets should be specifically designated and invoked by escape sequences, and a default should not be assumed. 还有另一个改动也引发了一些不满。原本，VisibleString 和 IA5String 指的是寄存器条目#2，这个条目代表了 ISO 646 的“国际参考版本”（但实际上，大多数人都错误地将其理解为“ASCII”）。不过，在 1980 年代末，ISO 646 被修改，加入了“美元”字符——这个字符存在于 ASCII 中，但在 ISO 646 的国际参考版本中并不存在。因此，ASN.1 将参考值改为寄存器条目#6（ASCII）。同时，它还将所有 GraphicString 和 GeneralString 编码在开始的 G 集的默认值从#2 改为#6。这一改动让 X.400 团体非常不满，他们现在建议在这些编码中，G 集应该通过转义序列来明确指定，而不应默认使用默认值。

Then ISO 10646 came along, and the ASN.1 group watched the discussions between the ISO workers and the Unicode workers with interest, but from the side-lines. When a compromise was reached and ISO 10646 was published, it looked easy: ASN.1 provided two new types, UniversalString (UCS-4 32-bit encoding), and BMPString (UCS-2 16-bit encoding) for characters in the multi-lingual plane. UCS-2 and UCS-4 provided escapes into encodings using the International Register - effectively the ability to embed GeneralString encodings in UniversalString or BMPString. In the interests of simplicity ASN.1 locked these escape mechanisms out in ASN.1 encodings, again giving some complaints today from sophisticated users! 后来，ISO 10646 标准应运而生。ASN.1 工作组则在一旁关注着 ISO 标准制定者与 Unicode 开发者之间的讨论。当最终达成一项妥协并发布了 ISO 10646 标准后，看起来问题似乎已经解决了：ASN.1 新增了两种类型——UniversalString（UCS-4 32 位编码）和 BMPString（UCS-2 16 位编码），用于处理多语言环境中的字符。UCS-2 和 UCS-4 则提供了将通用编码嵌入到 UniversalString 或 BMPString 中的机制。为了追求简洁性，ASN.1 干脆将这种嵌入式编码机制排除在标准之外，这自然引发了一些高级用户的抱怨！

A more serious problem was that just after the ink was dry on the 1994 ASN.1 publication, UTF-8 (and UTF-16), described earlier, arrived as amendments to ISO 10646 and to Unicode. UTF8String was added to ASN.1 in the 1997 version, but at the time of writing there is no support for UTF-16 - but some pressure to provide it! 一个更严重的问题是，在 1994 年 ASN.1 标准发布后不久，之前提到的 UTF-8（以及 UTF-16）作为修正案被纳入了 ISO 10646 标准和 Unicode 标准中。在 1997 版的 ASN.1 标准中，UTF-8 被添加进来；但在撰写本文时，还没有对 UTF-16 的支持——不过，有压力要求必须提供对 UTF-16 的支持！

In an attempt to "get out from under" in this character set and encoding debate, ASN.1 introduced "CHARACTER STRING" in 1994, supported by JTC1 SC2, who included an annex (but only an informative one!) in ISO 10646 that specified object identifier values to be used to identify character repertoires (including restrictions to level 1 or level 2 described above) and encoding schemes (UCS-2 and UCS-4). 为了摆脱这一关于字符集和编码争议的困境，ASN.1 在 1994 年引入了“字符字符串”这一概念。这一提议得到了 JTC1 SC2 的支持。JTC1 SC2 在 ISO 10646 标准中增加了一个附录，该附录仅用于提供信息而已！该附录规定了用于识别字符集的对象标识符值（包括上述提到的级别 1 或级别 2 的限制），以及编码方案（UCS-2 和 UCS-4）。

The type "CHARACTER STRING" was originally intended to be very efficient, with the object identifiers used to identify the character abstract and transfer syntaxes of character strings within a "SEQUENCE OF CHARACTER STRING" being transmitted only once. Unfortunately, the mechanism used to provide this turned out to have some fatal bugs in it, and was with-drawn. A later mechanism of "dynamic constraints", or "run-time parameters" attempted to provide equivalent support, but foundered because the power to complexity ratio was found to be too low. (This is discussed further in the final clause of this chapter.) “CHARACTER STRING”类型原本被设计成非常高效的机制。其中，对象标识符用于标识字符抽象，而“序列中的字符字符串”的传输语法则只需传输一次。然而，实现这一功能的机制存在一些致命缺陷，因此不得不放弃该机制。后来，人们尝试使用“动态约束”或“运行时参数”机制来提供类似的支持，但这一方案也失败了，因为其复杂性与简单性的比例过低。（这一点的详细讨论请参考本章的最后一部分。）

ASN.1 also provided mappings from the names of "collections" of characters in ISO 10646 into ASN.1 (sub)type names, and provided (sub)type names corresponding to the different "levels of implementation" of ISO 10646, and value references for each of the characters in 10646. (See Section II Chapter 2.). ASN.1 还提供了从 ISO 10646 中定义的字符集合名称到 ASN.1（(子)类型名称的映射关系。同时，它也为 ISO 10646 的不同“实现层次”提供了相应的(子)类型名称，并且为 10646 中的每个字符都定义了值引用方式。（详见第二章第二节。）

That is the history to-date, but watch this space! I think the saga of character sets and encodings is probably not yet over! 这就是迄今为止的历史了，不过请继续关注后续发展吧！我觉得关于字符集和编码的争论可能还远未结束呢！

## 11 ANY, macros, and Information Objects - hard to keep that short (even the heading has gone to two lines)! 11. 任意对象、宏以及信息对象——真难做到如此简洁啊（就连标题都长到两行了）！

Well, maybe we can keep it short - the information object concept has been well and fully discussed earlier, and ANY and macros were withdrawn from ASN.1 in 1994, so perhaps there is not really much more to say! 嗯，或许我们可以简短地总结一下——关于信息对象的概念已经得到了充分讨论，而所有宏指令在 1994 年就从 ASN.1 标准中删除了。所以，或许真的没有太多需要补充的内容了！

<table><tbody><tr><td data-imt-p="1">Much of this (if you are reading from front to back!) you already know. Let's pull the historical threads together. 这些内容中的大部分，如果你从头到尾仔细阅读的话，其实你已经了解了。让我们把这些历史线索串联起来吧。</td></tr></tbody></table>

The story starts with the attempted introduction of the OPERATION and ERROR syntax into ASN.1 in 1982/83 as described above. 这个故事始于 1982 或 1983 年，当时有人试图将 OPERATION 和 ERROR 语法引入 ASN.1 标准。如上所述，这一尝试最终成功了。

This attempt failed, and macros were introduced. It turned out that what the macro notation really provided (forget about what it appeared to provide!) was the ability to define arbitrary syntactic extensions (but with no semantics to relate those extensions to other ASN.1 constructs) to ASN.1. Until 1986, there were only two macros defined. These were defined in ROSE, and (surprise, surprise!) were called OPERATION and ERROR, and provided for any ASN.1 module that imported these macros to write precisely the OPERATION and ERROR syntax described earlier. 这次尝试失败了，于是人们引入了宏定义。实际上，宏定义真正提供的是一种定义任意语法扩展的能力（不过这些扩展与 ASN.1 的其他结构之间并没有任何语义关联）。直到 1986 年，只有两个宏被定义出来。这两个宏在 ROSE 规范中被定义，名字分别是 OPERATION 和 ERROR。任何使用这些宏的 ASN.1 模块都可以按照之前描述的 OPERATION 和 ERROR 语法来编写代码。

Of course, what was really happening (but this was only realised about five years later) was that the syntax was being provided to give ROSE users a reasonably friendly syntax with which to provide the information needed to complete the ROSE protocol - ASN.1 types and values associated with the definition of operations and errors which would be carried in ROSE messages. Information objects, in other words. But whilst the macro notation gave ROSE the ability to define the syntax it wanted, the underlying information object concepts were missing, and the use of that syntax (to define information associated with an operation or error) had no formal link with the ROSE messages. 当然，实际上发生的情况是，这种语法结构被设计出来，目的是为 ROSE 用户提供一种较为友好的语法方式，以便他们能够使用这种语法来提供完成 ROSE 协议所需的信息。这些信息包括与 ROSE 消息中的操作和错误相关的 ASN.1 类型和数据值。换句话说，就是各种信息对象。不过，虽然宏注释使得 ROSE 能够定义自己想要的语法结构，但那些底层的信息对象概念却缺失了，而且这种语法结构在定义与操作或错误相关的信息时，并没有与 ROSE 消息建立任何正式的关联。

Around 1986 there was a sudden explosion in the writing of new macros. It seemed that almost every group using ASN.1 found the need to add new syntax to the ASN.1 notation. What were they all doing? 大约在 1986 年，新的宏定义编写方式出现了突然的爆发式增长。似乎几乎所有使用 ASN.1 标准的团队都觉得有必要为 ASN.1 规范添加新的语法规则。他们到底在做什么呢？

Well ... nobody really knew, in terms of a global picture. The uses of that new syntax were many and varied, and had nothing to do with operations or errors. Moreover, tool providers were beginning to complain about the macro notation. 嗯……从全球的角度来看，其实并没有人真正了解这种新语法的具体用途。这种新语法有着多种多样的应用，而且与运算或错误处理毫无关系。此外，一些工具提供商也开始对宏注释方式表示不满了。

It became clear that (at least formally) it was possible to write new notation which claimed to define an ASN.1 type, but which totally failed to define the type unless accompanied by value notation (such as value notation in a value reference assignment, or use of DEFAULT in an element of a SET or SEQUENCE). 显然，（至少在形式上）是可以创建一种新的表示法来定义一种 ASN 类型。不过，这种表示法完全无法真正定义该类型，除非伴随有数值表示法的使用，比如在值引用赋值中使用数值表示法，或者在 SET 或 SEQUENCE 的元素中使用 DEFAULT 关键字。

There were two other major problems. 还有另外两个主要问题。

The first was that ASN.1 users were given (via the macro notation) the power to define arbitrarily complex syntactic extensions to ASN.1 using the Bacchus-Naur Form (BNF) notation. BNF is an extremely powerful notation that is often used to define the syntax of programming languages (and is indeed used to formally define the syntax of the ASN.1 notation itself). However, it is well known to definers of programming languages and other users of BNF that if the resulting syntax is to be computer-friendly (easily parsed by computers), then some moderately sophisticated and complex restrictions have to be adhered to in the BNF definition. No such restrictions were applied to its use in ASN.1. 首先，ASN.1 的用户可以通过宏定义方式，使用 BNF 语法来定义极其复杂的语法扩展。BNF 是一种非常强大的语法表示方式，常被用来定义编程语言的语法结构（实际上，BNF 也被用来正式定义 ASN.1 语法的结构）。不过，众所周知，对于编程语言的设计者以及其他使用 BNF 的用户来说，如果生成的语法结构要便于计算机处理（即能够被计算机轻松解析），那么在对 BNF 进行定义时就必须遵守一些相当复杂的规则。但在 ASN.1 中，并没有对这些规则进行应用。

The second problem was that it was generally not possible to find the end of a new piece of syntax introduced by a macro without knowing the details of that macro. But the definition of the macro could well follow the first use of the macro name and hence of the new syntax. 第二个问题是，通常很难在不了解该宏的具体细节的情况下找到新语法规则的结尾。不过，宏的定义很可能会在宏名称首次被使用时就已经确定下来，从而也确定了新的语法规则。

Whoops! Tool vendors did not like it! Some of the better tools hard-wired into their tool knowledge of the syntax defined by macros in most known international standards, and then simply ignored the actual syntax definition (macro definition) supplied to the tool. It worked, but .... 哎呀！工具供应商并不满意！一些较好的工具其实已经内置在了它们的工具知识中，这些知识是基于大多数已知国际标准中宏定义的语法结构。而工具则直接忽略了提供给工具的那些具体语法定义（宏定义）。虽然这样还能使用，但……

Around 1988, the USA campaigned strongly within SC21 for an embargo on the writing of new macros, and succeeded in getting a resolution passed forbidding such new macros until "either the macro notation was replaced, or the problems with it were resolved". It took around five years for this demand to be satisfied, with, in fact, replacement. 大约在 1988 年，美国在 SC21 组织中强烈呼吁禁止新宏变量的编写。他们成功促使会议通过了一项决议，规定在“要么宏变量表示方式被取代，要么其存在的问题得到解决”之前，不得创建新的宏变量。这一要求实际上花了大约五年的时间才得以实现，期间确实出现了一些替代方案。

Most of that time was spent trying to determine just exactly what the different groups were using macros for, and eventually light dawned, and it became apparent that in almost all cases the definition of extensions to the ASN.1 syntax was (as with ROSE) in order to provide users of a protocol full of holes with a human-friendly but formal notation to specify the contents of those holes. Use of the macro notation was (almost) always associated with use of "ANY" (and later "ANY DEFINED BY") in ASN.1-defined messages. (There were important exceptions, such as the ENCRYPTED macro in X.500, where the new syntax was being used to provide a real extension to ASN.1 which was later satisfied using the user-defined constraint and parameterization, described earlier in this text.) 大部分时间都用于研究各个小组究竟是将宏用于什么目的。最终发现，在几乎所有情况下，对 ASN.1 语法的扩展定义都是为了给那些使用这种复杂协议的用户提供一种易于理解但形式化的表示方式，以便他们能够明确了解这些“空洞”的内容。宏表示法的使用几乎总是与在 ASN.1 定义的消息中使用“ANY”或“ANY DEFINED BY”关键字联系在一起。（当然也有一些重要的例外，比如 X.500 中的 ENCRYPTED 宏，在这里，新的语法被用作对 ASN.1 的实质性扩展，而这一扩展后来通过用户自定义的约束条件和参数化机制得到了实现，这些内容在本文的 earlier 部分已经有过介绍。）

Around this time (late 1980s early 1900s) the problems with "ANY" became more widely recognised (although they had been flagged as early as 1985, with attempts to shore up "ANY" with "ANY DEFINED BY".) 在那个时候（20 世纪 80 年代末到 90 年代初），“ANY”这个表达存在的问题得到了更广泛的认可（尽管早在 1985 年就已经有人指出这个问题，当时人们试图通过添加“由某些定义来限定”这样的措辞来改进“ANY”的表达）。

The attempt to understand what macros were being used for and to define an appropriate replacement for macros and ANY went through many iterations and false starts over several years. "Non-encodable types" and "table types" were terms that were invented and discarded. 试图理解这些宏变量是用来做什么的，以及找到一种合适的替代品来替代宏变量……这个过程经历了许多迭代和尝试，耗时数年才最终确定下来。所谓“无法编码的类型”和“表类型”等概念也是先被提出然后又被放弃的。

Eventually something was almost ready, but it was complicated, and the terminology was not clear. There was a critical meeting (I think in Seoul, Korea, and I am pretty sure it was Bancroft Scott's first international ASN.1 meeting) in which it looked as tho' we could not find a replacement for macros - the earlier work was just too complex. But after a night of no sleep, solutions began to appear. The next day we started to discuss the Information Object Class concept, and to keep things simple, we agreed to allow just (eg): 最终，某个方案几乎准备好了，不过实施起来相当复杂，而且相关术语也不太清晰。有一次重要的会议中，我们似乎找不到合适的替代方案来取代宏函数——之前的工作实在太过复杂了。但在经过一整夜的思索之后，一些解决方案开始出现。第二天，我们开始讨论“信息对象类”这个概念，为了简化问题，我们决定只允许使用一些简单的描述方式，比如：

## OPERATION.&Type 操作与类型

without any constraint applied to it. (Something I still regret!) 没有任何限制条件施加在它身上。（这是我一直感到遗憾的地方！）

But the Seoul meeting was a good one. What looked (at the start) like the abandoning of several years of work, ended with the Information Object Class terminology and associated concepts pretty-well as we know them today. 不过，首尔的会议确实很成功。虽然一开始看起来似乎要放弃多年来的研究成果，但最终还是确定了“信息对象类”这一术语以及相关概念，而这些概念如今已经广为人知了。

Slightly later, another crucial meeting (at which probably nobody really understood the magnitude of the decision taken) occurred around 1991 - Washington I think (I remember the room, but can't remember the location!). This meeting decided to withdraw from ASN.1: 稍晚一些的时候，又有一场重要的会议召开（当时可能没人真正了解所做出的决定的重要性）。我记得是在 1991 年左右，地点在华盛顿州。我记得那个会议室的位置，但记不清具体的地点了。这次会议决定退出 ASN.1 组织。

• The entire macro notation. • 整个宏定义格式。

• The ANY and ANY DEFINED BY syntax. • 使用 ANY 和 ANY DEFINED BY 语法。

These were to be replaced by the notation for defining information object classes, objects, and sets, and the associated "information from object class" notation and the application of table and relational constraints. 这些概念将被用于定义信息对象类、对象和集合的表示法所取代。同时，还会引入“来自对象类的信息”这一表示法，以及表格和关系约束的应用。

There was around this time a popular UK television series about UK Government in which a civil servant would often say to a Cabinet Minister, "Minister, that is very brave of you." The Minister would wince, and almost instantly attempt to withdraw what he had been proposing. 大约在那个时候，英国有一档很受欢迎的电视系列节目，专门报道英国政府的运作情况。在节目中，经常会有公务员对内阁部长说：“部长，您真是太勇敢了。”听到这话，部长通常会感到有些尴尬，几乎会立刻收回自己提出的建议。

Nobody told the ASN.1 group that they were being "very brave" in withdrawing the macro and ANY and ANY DEFINED BY notation, but somebody should have! I don't know whether they (we) would have backed-off even if told, but I am sure that the extent of the adverse reaction was not anticipated. 没有人告诉 ASN.1 小组，他们撤销了那些宏指令以及所有基于定义符号的规范是“非常勇敢”的行为。不过，应该有人会告诉他们的！我不知道即使知道了这一点，他们是否还会坚持这么做。但我确信，这种负面反应的程度是出乎他们预期的。

This was the first (and only) non-backwards-compatible change to ASN.1 in its twenty year (todate) history, and gave rise to the "ASN.1 1990 problem" - see below - which lingered on for almost a decade. 这是 ASN.1 在过去二十年历史中首次（也是唯一一次）发生的与向后兼容无关的变化。这一变化引发了所谓的“ASN.1 1990 问题”——详见下文——该问题持续了近十年时间。

## 12 The ASN.1(1990) controversy 12. ASN.1(1990)争议

When the 1994 version of ASN.1 was published, there was an accompanying campaign to get people to change their specifications from use of ANY and ANY DEFINED BY and macros to use of the information object concepts. I think the ASN.1 group felt that as this would not 在 1994 年发布 ASN.1 的版本时，组织了一场宣传活动，旨在促使人们改变规范的使用方式，从使用“ANY”和“ANY DEFINED BY”宏，转变为使用信息对象概念。我认为，ASN.1 工作组认为，这样做是因为这样能够……

Never, never, never produce a specification that makes illegal what was previously legal. If you do, you will regret it! But maybe sometimes it is the only way to get rid of a bad feature? 千万不要制定这样的规范，让原本合法的功能变得非法。如果你这么做，你会后悔的！不过，也许有时候这是消除不良功能的唯一办法吧？

change any "bits on the line", it was not a big deal! But of course any change to a specification (even to add a single comma) that is "stable" and not immediately about to be re-issued in a new version is actually a costly exercise. The gains must be apparent. 只要修改那些“在行间的字符”即可，这并不算什么大问题！不过，当然，任何对规范的修改（哪怕只是添加一个逗号）都必须是“稳定的”，并且不会很快被重新发布到新的版本中。这样的修改确实需要花费不少精力。而且，这些修改带来的好处必须非常明显才行。

The ASN.1 group had no doubt: there were so many flaws with the macro notation and the use of ANY, and the information object concepts and associated notation were so much better. Everyone should make the transition. A transition plan was agreed. A lot of the use of macro notation was in the original ROSE OPERATION and ERROR macros. So it was agreed that ROSE would change in 1994 (it did - keeping the old macro definition as an informative annex) and that users of ROSE would change no later than 1998. ASN.1 工作组毫不怀疑：宏定义方式以及使用 ANY 这种语法存在许多缺陷，而信息对象概念及相关表示法则要好得多。所有人都应该进行迁移。已经制定了迁移计划。宏定义方式的大量应用存在于原始的 ROSE 操作与错误宏中。因此，大家一致认为 ROSE 会在 1994 年进行更新（实际上确实如此——旧的宏定义被保留下来作为补充说明）。而使用 ROSE 的用户则需要在 1998 年之前完成迁移。

New specifications (like SET - Secure Electronic Transactions) did, of course, like the readers of this book(!), have no problems in adopting the new concepts - they gave important clarity in the specification of protocols with holes in them. 新的规范（如 SET 安全电子交易等）当然没有遇到任何问题，就像本书的读者们一样，能够顺利地采纳这些新概念。这些新规范为协议的描述提供了重要的清晰度，使得那些存在漏洞的协议得到了有效的改进。

Specifications such as X.400 and X.500, which defined their own macros and were still in the process of being extended also bettered the agreed time-frame. They recognised the greater clarity of the new notation, and switched to it early in the 1990s. 像 X.400 和 X.500 这样的规范，它们定义了自己的宏命令，并且仍在不断扩展中。这些规范也改善了约定的实施时间框架。人们认识到新的表示方式更加清晰明了，因此从 20 世纪 90 年代初就开始采用这种新的规范了。

However, there were some groups that found the change more difficult, and resisted it for longer. Interestingly, the embargo that the USA placed on writing new macros lead one group whose protocol was almost 50% "ANY" (of course I exaggerate!) to define (in English) their own notation for specifying the information objects (as we now call them) that would complete their protocol. This notation is called "Generic Definition of Managed Objects" (GDMO), and is today supported by its own set of tools specific to that application and that notation. This group had the least incentive, and took longest, to make the transition to the 1994 version of ASN.1. (Removal of uses of "ANY" from their protocol.) 不过，有一些小组觉得这种改变更加困难，因此抵制了这种变化的时间更长。有趣的是，美国对编写新的宏指令的禁令使得其中一个小组的协议中有近 50%的语句使用了“ANY”作为标记（当然，我是在夸张啦！）。他们自己定义了用于指定信息对象的符号系统，这些符号系统我们现在称之为“管理对象通用定义”。这个符号系统如今得到了专门的工具支持，这些工具专门针对该应用领域而设计。这个小组是最不愿意接受 1994 年版本的 ASN.1 的，他们抵制这种改变的时间也最长。（他们从自己的协议中删除了对“ANY”的使用。）

It is normal in ISO for a revised Standard to automatically replace an earlier version. It replaces it in the sense that the older version can no longer be purchased, and is no longer recorded in the catalogue of available ISO Standards, and new Standards are not allowed to refer to the old version. 在 ISO 标准中，修订后的标准通常会自动取代旧版本的标准。这意味着旧版本的标准无法再被购买，也不会被收录在可用的 ISO 标准目录中。新的标准也不允许引用旧版本的标准。

Because the definition of the ASN.1 notation in ASN.1 (1994) was not fully backwards compatible with the ASN.1 (1990) definition (and because everyone knew that time was needed for standards referencing ASN.1 to up-date their specifications to conform to the 1994 versions), there was strong pressure to "retain" ASN.1 (1990). ISO Central Secretariat agreed to this, provided a resolution to that effect was passed by SC21 at each of its annual plenary meetings. 由于 ASN.1 规范在 1994 年提出的定义与 1990 年版本的定义并不完全向后兼容（而且众所周知，标准规范需要时间来更新其规范，以符合 1994 年的版本），因此存在强烈的压力要求保留 1990 年的 ASN.1 规范。ISO 中央秘书处同意了这一要求，前提是 SC21 在每年的全体会议上能够就相关决议达成一致。

Of course, these resolutions became the focus of a battle-ground, with each year the ASN.1 group increasingly strongly proposing withdrawal of ASN.1 1990, and each year some group or other saying "we are not ready yet". It was actually 1999 before ASN.1 (1990) was finally laid to rest! 当然，这些决议成为了争论的焦点。每年，ASN.1 小组都不断强烈建议撤销 ASN.1 1990 版本的规定。而每年都有不同团体表示“我们还没有准备好”。实际上，直到 1999 年，ASN.1 1990 版本才最终被放弃！

This has been a salutary lesson, and if in an ASN.1 meeting anyone dares to propose a change that would make illegal anything that could reasonably be interpreted as legal under the current wording, there are howls of "1990, 1990", and the proposal fails! Even if changes do not affect the bits on the line, the notation is now sacrosanct - too many people use it, and existing specifications can not be made retrospectively illegal. 这真是一堂有益的教训。如果在 ASN 的会议上有人敢提出任何会改变现有条款的提议，使得那些在现行条款下可以被合理解释为合法的内容变得非法，那么就会有人大声喊出“1990 年，1990 年”来反对这个提议，而该提议最终会失败！即使这些修改并不影响那些具体的条款内容，但现在的规范已经变得不可更改了——有太多人在使用这种规范，而现有的规范也无法被追溯性地变为非法。

## 13 The emergence of PER 13. PER 的出现

## 13.1 The first attempt - PER-2 13.1 第一次尝试——PER-2

Pronounce that "PER minus 2"! 请说出“PER 减去 2”这个数值！

It took three attempts to get PER to where it is today - PER-2, PER-1, and finally real-PER. 要让 PER 达到现在的水平，我们经历了三次尝试——分别是 PER-2、PER-1，最后才得到了真正的 PER。

Work on producing better encoding rules started at about the same time as work on understanding how macros were being used, and on mending or replacing macros, and was for a long time overshadowed by that work, with only a small number of people really contributing to work on new encoding rules. 在制定更完善的编码规则方面的工作，大约在同一时期开始进行。与此同时，人们也在研究如何有效使用宏指令，以及如何修复或替换那些不再适用的宏指令。不过，这些工作在很长一段时间内都被那些关于宏指令的研究所掩盖，真正在编码规则制定方面做出实质性贡献的人其实并不多。

The original work (let me call this "PER-2", pronounced "PER minus 2"!) was based on using BER and "improving" it. The recognition was that BER often transmitted octets down the line that a decoder (provided they had knowledge of the identical type definition to that being used by an encoder) could totally predict. This was what had to be sent at that point. Therefore it did not need to be sent. 最初的方案（让我将其命名为“PER-2”，发音为“PER 减去 2”）是基于使用 BER 并对其进行“改进”的构想。人们意识到，BER 通常会连续传输某些八位组的数据，而解码器（只要它们了解与编码器所使用的相同类型的定义）完全可以预测这些数据的内容。这些数据就是当时应该被传输的内容。因此，其实并不需要再传输这些数据了。

```txt
Example-for-encoding ::= SEQUENCE
{first-element INTEGER (0..127),
second-element SEQUENCE
{string OCTET STRING (SIZE (2)),
name PrintableString (SIZE (1..8)) }
third-element BIT STRING (SIZE (8)) }

Figure IV-2: An example sequence to be encoded 
```

It was also recognised that if the length field of a constructed encoding was changed to provide a count of the number of TLVs in the encoding of the contents rather than a count of the octets in the contents, then further octets could be removed. And finally, it was recognised that if there were constraints on the length of a character string field or on the size of an integer, then length fields could be omitted. 此外，还认识到：如果修改构造的编码中的长度字段，使其用来显示内容中 TLV 的数量，而不是显示内容中八位元的数量，那么就可以进一步减少所需的八位元数量。最后，还认识到，如果字符字符串字段的长度或整数的大小存在限制，那么可以省略长度字段。

Accept these changes to BER, and examine figure IV-2, a (slightly contrived) example of a type to be encoded, and figure IV-3, the BER encoding of that type. 请接受这些对 BER 的修改。接下来请查看图 IV-2，这是一个用于编码的类型的示例（虽然有些人为地构造了这个例子）；再看看图 IV-3，那是该类型的 BER 编码方式。

```ini
1 T=[Universal 16]
2 L=3 (TLV count)
3 T=[Universal 2]
4 L=1
5 V=what-ever
6 T=[Universal 16]
7 L=2 (TLV count)
8 T=[Universal 4]
9 L=2
10-11 V=what-ever
12 T=[Universal 19]
13 L=5 (say)
14-18 V=what-ever
19 T=[Universal 3]
20 L=2
21 V1=0 (no unused bits in last octet)
22 V2=what-ever

Figure IV-3: The 22 octet BER encoding of figure IV-2 
```

Looking at figure IV-3, we have 22 octets in the BER encoding. But all except octets 5, 10-11, 13-18, and 22 (a total of 10 octets) are completely known by a decoder, and need never be transmitted! PER-2 said "delete them!". 从图 IV-3 可以看出，BER 编码中共有 22 个八位组。不过，除了第 5、10-11、13-18 以及 22 个八位组之外，其余的八位组都完全被解码器知晓，因此无需进行传输！PER-2 命令“删除这些八位组”。

(Interestingly, whilst the final real-PER specification was totally different from this early approach, it is just these 10 octets that the current real-PER will transmit!) 有趣的是，虽然最终的真实 PER 规格与这种早期方法有很大不同，但当前的真实 PER 仍然只是传输了这 10 个八位组的数据而已！

The PER-2 draft said essentially: PER-2 草案的内容大致如下：

• Do a standard BER encoding (slightly modified to provide counts of TLVs rather than octets for constructed encodings). • 进行标准的 BER 编码处理（稍作修改，以使用 TLV 标签来表示计数，而不是用八位元来表示编码数据）。

• Apply the following rules to delete octets from the encoding. • 请遵循以下规则来删除编码中的八位组。

• At the receiving end, apply the rules in reverse to reconstruct the original BER encoding. • 在接收端，反向应用这些规则来重建原始的 BER 编码方式。

• Do a standard BER decoding (again modified to use TLV counts). • 进行标准的 BER 解码操作（再次对算法进行修改，以使用 TLV 计数方式）。

Some of the rules for when you could delete octets were obvious and straight-forward, some got quite complicated. The reader might like to try to formulate precisely the rules that enabled us to delete (not transmit) 12 of the 22 octets in the encoding of figure IV-3. 关于何时可以删除某些八位组的规定，有些相当简单明了，而有些则相当复杂。读者或许可以试着明确那些让我们能够删除图 IV-3 中编码中的 22 个八位组中的 12 个的规则。

PER-2 was really a sort of "expert system" approach to encoding. There were a whole raft of rules to be applied to determine when you could or could not delete octets (with re-insertion on receipt), and these were very ad hoc and some-how looked as if they were not complete and not founded on any good general principles. (They were ad hoc, and were not founded on any general principles!) PER-2 实际上是一种“专家系统”式的编码方法。需要遵循一系列规则来决定何时可以或不能删除某些八位组（并且这些八位组在重新插入后会重新生效）。不过，这些规则都是非常灵活的，看起来并没有任何明确的、普遍适用的原则来支撑它们。（这些规则都是非常灵活的，而且根本没有任何普遍适用的原则来支撑它们！）

But the text was eventually deemed complete, and sent for ballot. The editing meeting to consider ballot comments was in New Jersey, and was scheduled to last for one week (this being the only business under consideration). Something went wrong with the administration, and the copies of the formal National Body responses to the ballot only became available by fax at 9am on the first day of the meeting. 不过，这份文本最终被认定为完整无误，于是被送交投票环节。负责审议投票意见的编辑会议在纽杰利州举行，预计会持续一周时间（这确实是唯一需要讨论的事项）。然而，由于管理方面的原因，正式的国家机构对投票结果的回复文件直到会议第一天上午 9 点才通过传真方式送达。

Faces dropped. Everyone knew their own country's response, but until then they did not know what others had said. Every, yes every, National Body had voted "DISAPPROVE". And none of the comments were in any way helpful for further progress. They more or less all said "This is just too complicated, too ad hoc, it will never work". None of them suggested anything that could be done to change the PER-2 draft to make it acceptable. 大家都沉默了。每个人都知道自己的国家会做出什么反应，但在此之前，他们并不清楚其他国家会怎么说。每个国家机构都投票支持了“反对”这一选项。而所有的评论都毫无助于事情的进展。他们几乎都表示：“这太复杂了，太临时了，根本不可能成功。”没有人提出任何能够改变 PER-2 草案、使其变得可接受的方案。

The meeting broke up for lunch that day at about 11am, with many delegates (there were about a dozen present representing five or six countries) ringing their air-lines to find out how much more it would cost to fly back that day rather than on their scheduled flight at the end of the week. Other delegates (myself included) retired to the bar to drown their sorrows. 当天的会议在上午 11 点左右中断，以便进行午餐休息。许多代表（大约有十几位，他们来自五到六个国家）纷纷打电话询问，当天飞行返回的费用是否比本周末的预定航班更高。其他代表们则回到酒吧里，试图排解心中的烦恼。包括我在内的几位代表也不例外。

After enough beer had been consumed, people started to think the unthinkable. Why don't we just abandon the TLV principle and start from scratch? Forget interworking between different versions of a standard (PER-2 didn't really provide that anyway) - how would we encode stuff, using maximum human intelligence, to produce minimum octets on the line? The "back of a cigarette packet" (actually, it was a paper table napkin) design started to take shape. (I wish now that I had kept the napkin, but I think it was consigned to the WPB. So much for important historical documents!) Come 2pm, the chairman (Bancroft, the Editor, I think) said, "Shall we convene and get this meeting wrapped up?". "No," was the response from the then mildly intoxicated bar group (drunk - never!), "we might be getting somewhere." I think the meeting eventually resumed that day at around 4pm. PER-1 (PER minus 1), almost PER as we now know it (but not quite) had been borne. 当人们喝够了啤酒之后，他们开始思考一些不可思议的事情。为什么我们不放弃 TLV 原则，从头开始呢？先不说不同版本标准之间的互操作性问题（反正 PER-2 标准本身也不具备这种功能），我们如何利用人类最聪明的思维方式，以最少的数据传输量来编码信息呢？“香烟包装纸”设计就这样诞生了。（真希望我当时能保留那张包装纸，不过看来它已经被送到了 WPB 了……那些重要的历史文件啊！）到了下午 2 点左右，主席（我记得是 Bancroft，编辑部的人）问道：“我们是不是应该结束这次会议了？”“不，”当时还略微喝醉的酒吧成员们回答道，“我们或许还能取得一些进展。”我想，那次会议最终在下午 4 点左右才结束。PER-1（即 PER 减去 1），实际上就是我们现在所熟知的 PER 数值。不过，它并不完全等同于 PER。

The principles were in place: 原则已经确立：

Forget about tags - abandon them! (You had to be pretty drunk to make that statement - TLV was a sort of mind-set it was hard to break out of.) 别再考虑那些标签了——干脆把它们抛到一边去吧！（要说出这种话，得喝得相当醉才行……TLV 这种心态确实很难改变。）

Make full use of knowledge about constraints on integers and on lengths to remove length fields whenever possible. 充分利用关于整数限制和长度限制的知识，在可能的情况下删除那些不需要的长度字段。

How to solve the problem of SET elements being in a random order? Fix the order! (You had to be a little drunk to say that too!) 如何解决 SET 元素顺序随机的问题呢？只要固定顺序就好了！（说这话的时候你肯定有点醉了吧！）

• How to identify a chosen element of a CHOICE? Encode a choice index. • 如何识别一个选择中的元素？可以通过创建一个选择索引来实现。

• How to identify missing OPTIONAL elements in a SEQUENCE or SET? Use a bit-map at the head of the SEQUENCE or SET. • 如何识别序列或集合中缺失的可选元素？可以在序列或集合的开头部分使用一个位图来表示这些可选元素。

• How to encode a BOOLEAN - well of course, use just one bit! • 如何对布尔值进行编码——嗯，当然，只需要使用一个比特位就可以了！

But .... octet-alignment? Recognise it is good to have padding bits at times so that later material which is a sequence of elements that are an integral number of octets will lie on an octet boundary, but use the minimum number of bits without worrying about octet alignment where that looks sensible. 但是……八位数的对齐问题呢？其实，有时候使用一些填充位还是不错的。这样，那些由多个元素组成的、总位数恰好是整个数的八位数的数据，就可以整齐地排列在八位数的边界上。不过，我们还是应该尽量使用最少的位数，而不必过于担心八位数对齐的问题，只要确保数据的排列符合逻辑即可。

There were still some elements of the "expert system" approach to this design (as there are with current PER). It is a fairly ad hoc decision on which fields should encode into bit-fields (no padding bits) and which into octet-aligned-bit-fields (with padding bits). 在这种设计中，仍然采用了“专家系统”方法的某些元素（就像当前的 PER 系统一样）。关于哪些字段应该编码为位字段（无需填充位），哪些字段应该编码为八位字节对齐的字段（需要填充位），这些决策都是相当即兴的。

A lot of details remained to be solved, but the meeting continued for the rest of the week, drafts were produced and considered, and PER-1 became a reality, with later editorial work being done to produce good text over the next few months. 还有很多细节需要解决，但会议在接下来的一周里持续进行着。相关草案已经出炉并得到了审议，PER-1 终于成为了现实。在接下来的几个月里，还会进行进一步的编辑工作，以完成最终的文本编写工作。

## 13.2 The second attempt - PER-1 13.2 第二次尝试——PER-1

When PER-1 was balloted, it got a much more favorable response than PER-2, but there was still a very strong "DISAPPROVE" vote from the USA which said "Regrettably, after much discussion, we have to disapprove of PER-1. With PER-1 there is no way a version 1 system can interwork with a version 2 system (you can't even find the end of an encoding unless you are both working with an identical type definition). This stuff just isn't going to work for International Standards. Kill it." 在 PER-1 的投票中，得到了比 PER-2 更为积极的反馈。不过，来自美国的投票中还是有一票表示“不赞成”。投票者写道：“很遗憾，经过多次讨论后，我们不得不对 PER-1 表示反对。使用 PER-1 的系统无法与版本 2 的系统协同工作（甚至无法找到编码的结尾部分，除非双方使用的类型定义完全相同）。这种方案根本无法成为国际标准。应该取消它。”

Nope - you must go back to TLV. Only TLV can provide interworking between version 1 and version 2 systems. It is a tried and true technique. Well, the last sentence is true, but is the second? We know now that it is not. In 1992 we were less sure! 不行——你必须回到 TLV 那里。只有 TLV 能够实现版本 1 和版本 2 系统之间的互操作。这是经过验证的有效方法。不过，最后一句话是正确的，但第二句话呢？我们现在知道这是不正确的。在 1992 年时，我们对此还不太确定呢！

This meeting was less traumatic than the last, but this "interworking" (or "extensibility" problem as it became known) delayed the production of the final real-PER for just over twelve months. 这次会议的创伤比上次要小一些，不过这个“互操作性问题”还是导致了最终的实际 PER 的发布被推迟了大约十二个月。

## 13.3 And eventually we get real-PER 13.3 最终，我们得到了真正的 PER 值。

A lot of trees were cut down to provide paper for people to describe what sorts of additions or changes they would want to make between version 1 and version 2 of a protocol. The consensus that emerged was essentially "We only need to add things at the end." 为了编写描述人们希望在协议版本 1 和版本 2 之间进行哪些改进或变更的文字，很多人砍掉了许多树木来获取纸张。最终达成的共识是：“我们只需要在协议的末尾添加一些内容就可以了。”

The ellipsis goes into the notation (and the exception marker with it), and the extension bit goes into PER. We have got there! 省略号被放入了符号中（同时附上了例外标记），而扩展位则被放入了 PER 中。我们终于完成了！

The ellipsis was provided for people to indicate this, and the extension bit in PER provided the encoding support. 省略号是为了让人们能够表示这一点而添加的，而 PER 中的扩展位则提供了编码支持。

The real-PER approach is to say essentially: 真正的 PER 计算方法本质上可以表述为：

• If parts of the specification are not flagged as extensible, then encode them in an efficient manner. • 如果规范的某些部分没有被标记为可扩展的，那么应当以高效的方式对这些部分进行编码。

• If parts are marked extensible, but the values are values of the version 1 specification (in the root), provide one bit to say so, but still encode them efficiently. • 如果某些部分被标记为可扩展的，但其值仍遵循版本 1 规范的规定（位于根节点中），那么可以预留一个比特位来表示这一点，同时仍需要高效地编码这些值。

• If extensible parts have values outside of the root (version 2 additions), set the extensions bit to one, and provide a length wrapper. • 如果可扩展部分的值位于根部分之外（这是版本 2 新增的功能），请将扩展标志设置为 1，并提供一个长度封装器。

It is unlikely that this approach would have been developed if we had not been starting from a design (PER-1) that did efficient encodings, with no concern for interworking. The various traumas on the path to PER were probably necessary to break the in-built tradition of TLV encodings as the only way to provide version 1 to version 2 interworking. 如果我们不是从一个能够实现高效编码且不考虑互操作性的设计出发，那么这种方法的开发可能性就很小了。在通往 PER 过程中的各种挑战或许是必要的，因为它们有助于打破 TLV 编码作为唯一实现版本 1 与版本 2 之间互操作的方式的固有传统。

This is not quite the end of the story! Later, there was strong pressure to be able to add things in the middle of sequences and sets, and version brackets were added. 但这并不是故事的终点！后来，人们强烈要求能够在序列和集合的中间添加元素，于是版本括号就被引入了。

There was also pressure from the air traffic control people to get rid of the padding bits and to forget about octet alignment, which produced the UNALIGNED version of PER. 此外，空中交通管制部门也施加了压力，要求去掉那些填充部分，并忽略八位字节的对齐问题。因此，就产生了未经对齐的 PER 版本。

But these were minor problems. The path from PER-1 to the final PER has left us with text which is not always as precise as it should be, and in particular the integration of the extensibility and extensions bit concept into the PER-1 text still poses some problems today (1999), with arguments (and probably eventually corrigenda) related to obscure uses of the extensibility notation (which fortunately no-one has yet written, and perhaps never will!). Many of these problems were uncovered by Olivier and myself when we started writing our books! Fortunately, we both agreed on what the answer should be, and I think our books both tell the same story! 不过，这些问题都是次要的。从 PER-1 到最终版本的 PER 的过程中，我们得到了一些文本，这些文本并不总是十分精确。特别是，将可扩展性和扩展概念整合到 PER-1 文本中仍然存在一些问题（1999 年），其中一些问题与可扩展性符号的模糊使用有关（幸运的是，至今还没有人提出过相关的解决方案，也许永远也不会有人这样做！）。这些问题中很多都是 Olivier 和我在我们开始编写书籍时发现的！幸运的是，我们两人对问题的解决方案达成了共识，我认为我们的书籍都讲述了同样的故事！

## 14 DER and CER 14 个 DER 和 CER

(Sounds familiar? Yup, I've used that box before - sorry!) （听起来很耳熟吧？没错，我之前用过那个盒子——抱歉！）

The major "option" in a BER encoding is the use of definite or indefinite lengths for constructed encodings. There was never agreement on which was best, and both are allowed in the BER specification. There have been all sorts of rows over the years when some profiling groups attempted to mandate one form or the other. 在 BER 编码中，主要的“选项”是采用固定长度或可变长度来构建编码。关于哪种方式更优一直没有达成一致意见，因此在 BER 规范中同时允许这两种方式。多年来，每当有一些分析团队试图强制使用某种特定方式时，就会引发各种争议。

Engraven on the hearts of standardizers: Your job is to produce Standards. If you can't agree, make it optional, or better still, another Standard. After all, if one Standard is good, many standards must be better! 这些标准被刻在那些制定标准的人心中：你的任务就是制定标准。如果你无法达成一致意见，那就让这项标准成为可选择的选项吧；或者，更好的办法是再制定一个标准。毕竟，如果一个标准已经足够好了，那么更多的标准当然会更优秀！

Roughly speaking, for short messages, the definite length form is probably the most sensible, but for long ones the indefinite form is to be preferred. Leaving the option to an implementor seems like a good idea, but of course it means that decoders have to handle both forms. 一般来说，对于简短的消息来说，使用固定长度的形式可能是最合理的选择；而对于较长的消息则应该采用不固定长度的形式。将这种选择留给实现者来处理似乎是个不错的主意，不过当然，这意味着解码器需要能够处理这两种形式的数据。

If, however, you want encoding rules with no options for the encoder (to minimise the testing problem and to help with security-related problems, as discussed in clause 10 of Section III Chapter 1) then you have to bite the bullet! 不过，如果你希望编解码器没有任何选项可供选择（这是为了减少测试难度，同时解决与安全性相关的问题，详见第 1 章第 III 节第 10 条），那么你就不得不接受现实了！

X.500 first produced (as about a twenty-line specification) the rules for producing a canonical encoding of BER, and they called it a "distinguished" encoding. It did enough of the job to cover the types that they wanted to apply it to, but was not complete. It also (arguably) did not make some choices in an optimal manner. X.500 规范最初提出了一套用于生成 BER 规范编码的规则（该规范描述大约包含二十行内容），并将其称为“高级”编码方式。这套规范确实足以涵盖他们想要应用的各种类型，但还不够完善。此外，可以说，它在某些方面并没有做出最优的选择。

The ASN.1 group decided to produce a standard for a canonical version of BER which it decided to call "Distinguished Encoding Rules", taking the name from X.500. ASN.1 工作组决定为 BER 的规范版本制定一个标准，并将其命名为“Distinguished Encoding Rules”，这一名称来源于 X.500 标准。

The major difference between the ASN.1 specification and the X.500 specification was that X.500 mandated use of definite length encodings, and the ASN.1 group went for indefinite length wherever they were possible! ASN.1 规范与 X.500 规范之间的主要区别在于：X.500 要求使用固定长度的编码方式，而 ASN.1 规范则尽可能采用不定长度的编码方式！

Major liaison statements, etc etc. Meanwhile, workers on another standard - ODA (Office Document Architecture) - who had very large messages to ship but who also needed canonical encodings, liked the ASN.1 groups draft! 此外，那些使用另一种标准——ODA（办公文档架构）的工程师们，他们有大量的消息需要发送，但同时也需要使用特定的编码规则。对他们来说，ASN.1 的组结构是一个很好的选择！

So the eventual up-shot was effectively two separate standards, one for DER (totally aligned with the early X.500 text, and using definite length encodings), and one for CER ("improving" on the © OS, 31 May 1999 353 original X.500 work, and using indefinite length encodings whenever possible). Both "standards" are, of course, published alongside BER in X.690 (ISO/IEC 8825-1). 因此，最终的成果实际上是两种不同的标准：一种适用于 DER 标准（完全符合早期的 X.500 规范，采用固定的长度编码方式）；另一种则适用于 CER 标准（在 1999 年 5 月 31 日发布的原始 X.500 规范基础上进行“改进”，尽可能使用不固定的长度编码方式）。这两种“标准”都随 X.690 标准（ISO/IEC 8825-1）一起发布。

The X.500 use of DER is mainly for certificates, becoming now heavily used in the development of e-commerce. (Most e-commerce activity is based on X.509 certificates, which use DER encoding.) By contrast, the ODA work has not been widely implemented. So whatever their relative technical merits, DER has become the de facto standard for canonical encodings of BER, and CER is probably dead! X.500 规范中 DER 编码的主要应用场景是证书传输。如今，DER 编码在电子商务领域的开发中得到了广泛应用（大多数电子商务活动都是基于 X.509 证书进行的，而这些证书就使用了 DER 编码）。相比之下，ODA 编码则几乎没有得到广泛应用。因此，无论 DER 编码在技术上有哪些优势，它都已经成为了 BER 和 CER 编码的默认标准，而 ODA 编码可能已经逐渐被淘汰了！

## 15 Semantic models and all that - ASN.1 in the late 1990s 15 种语义模型等等——在 20 世纪 90 年代末的 ASN 标准中出现的概念

There have always been questions about the legality of certain ASN.1 constructs where things were syntactically permissible, but might or might not really be something you should allow. The main area of these problems is in "type matching" rules between a value reference and its governor. For example, with: 一直以来，人们对于某些 ASN.1 构造的合法性一直存在疑问。这些构造在语法上可能是可行的，但实际上是否真的属于应该允许的范围，这一点并不明确。这些问题主要出现在值和其描述符之间的“类型匹配”规则上。例如：

Humans only write simple and obvious ASN.1. But stupid dumb computers want to know about the legality of the most abstruse expressions that the syntax allows. And the computers have an important voice in the tool vendors! They have to be listened to! 人类只会编写简单明了的 ASN.1 代码。但是那些愚蠢的计算机却想要了解语法所能表达的最复杂的概念的含义。而在工具供应商的决策过程中，计算机发挥着重要作用！他们的意见必须得到重视！

## intval INTEGER ::= 7 intval 整数类型 ::= 7

You might ask whether you can legally write as an element of a sequence: 你可能会想问，作为序列的一部分来编写内容，在法律上是否可行呢？

## \[27\] INTEGER DEFAULT intval \[27\] 整数类型 默认值为 intval

or 或

## INTEGER (0..127) DEFAULT intval 整数类型（0~127）默认值为 intval

Of course you would expect these to be legal, yes? But "\[27\] INTEGER" and "INTEGER (0..27)" are certainly not exactly the same type as "INTEGER". All three types do not contain exactly the same values, and the encoding of their common values differs in either or both of BER and PER. 当然，你可能会认为这些类型应该是合法的，对吧？不过，“\[27\] INTEGER”和“INTEGER(0..27)”显然与“INTEGER”不是完全相同的类型。这三种类型所包含的值并不完全相同，而且它们在 BER 和 PER 中的编码方式也有所不同。

Again, if a value reference is defined using a certain (fairly complex) type definition, and that value reference is then used when governed by an identical (but textually distinct) type reference, is that legal? And if the second textual occurrence is not quite identical to the first, by how much can it deviate before the text becomes illegal ASN.1? 再次，如果某个值引用是通过某种相当复杂的类型定义来定义的，而该值引用在受到另一个相同（但在文本上有所不同）的类型引用时也被使用，那么这是否合法呢？如果第二个文本出现的情况与第一个不完全相同，那么文本在变得不符合 ASN.1 标准之前，可以相差多少才会导致其变得非法呢？

Add to these examples use of the extension marker .... 在这些例子中，还包含了对扩展标记器的使用说明……

These are the problems that are being grappled with in the late 1990s, and which will probably lead to the inclusion in the standard of models (pictures) of types as buckets containing values, and of "value mappings" between types which are defined by textually separate pieces of notation. Similar models/pictures are needed to cover types that have an ellipsis, and/or extensions. 这些问题是在 20 世纪 90 年代末被研究的课题，它们可能会导致标准中引入一些模型（例如图表），这些模型用于描述不同类型的数据如何包含值，以及不同类型之间如何通过文本形式的规范来定义“值映射”。为了涵盖那些带有省略号的类型，以及相关的扩展情况，就需要使用类似的模型/图表来描述。

The guiding principle in all this work is to make things legal if they make any sort of sense (rather than a tight specification that makes only the most obviously correct things legal), but to end up with a very complete specification of what is legal ASN.1. 所有工作的指导原则都是：如果某件事有道理，那就将其合法化（而不是仅仅满足于严格的规范，只让那些显然正确的事情变得合法）。但最终，我们会得到一个非常完整的关于什么是合法的 ASN.1 规范。

Of course, the reader will guess that the pressure for this work comes from tool vendors. They have to write code which is required to make judgments on the legality or otherwise of stuff that no protocol specifier in their right mind would ever write! 当然，读者可以猜测，这项工作的压力主要来自工具供应商。他们必须编写一些代码，这些代码用于判断某些内容的合法性与否，而实际上，任何理智的协议规范制定者都不会编写这样的代码！

## 16 What got away? 16 什么被遗漏了？

There have been a few features of ASN.1 development that have not made it into the current standard. They may get resurrected, but probably won't! 在 ASN.1 的开发中，有一些特性并未被纳入当前的标准中。这些特性有可能会被重新引入，但可能性不大吧！

<table><tbody><tr><td data-imt-p="1">Could ASN.1 be even better? There are certainly further improvements that have been discussed. But is the added complexity worth the gains? The consensus is "NO". ASN.1 是否还能改进得更好呢？当然，肯定还有更多的改进空间。但是，这些额外的复杂性是否值得这样的提升呢？大家的共识是：“不值得”。</td></tr></tbody></table>

The Light Weight Encoding Rules (LWER) were fully discussed in Section III Chapter 4, and will not be referred to again here. 轻量级编码规则（LWER）已在第 4 章的第 III 节中详细讨论过，因此在此不再赘述。

Probably the major loss was in not providing an efficient encoding for SEQUENCE OF CHARACTER STRING, and for the encoding of a table where each column can be the choice of a number of possible types. 可能最大的损失在于未能为“字符字符串序列”类型提供一个高效的编码方式，同时也无法对包含多个可能类型的列的表格进行正确的编码处理。

In the case of CHARACTER STRING (which, if you remember, carries two object identifier values with each encoding of this type), the original concept was to permit chains of encodings of type CHARACTER STRING, where each encoding in any given chain had the same object identifier values. These values would be transmitted at the start of each chain, and then, rather like virtual circuits in network protocol, there would be an abbreviated identification to link each encoding into its chain. Unfortunately, serious bugs were found in this chaining concept (because of interaction with extensions), and it was very rapidly withdrawn within days of its initial publication. 在“字符字符串”这种编码类型的情况下（如果你还记得的话，每种编码类型都包含两个对象标识符值），最初的设想是允许一系列字符字符串的编码方式，其中每个编码在链条中都具有相同的对象标识符值。这些标识符值会在每个链条开始时被传输，然后，类似于网络协议中的虚拟电路机制，会有一个简化的标识符来将每个编码链接到相应的链条中。不过，由于与扩展功能的交互问题，这种链式编码方式出现了严重的漏洞，因此该编码方式在发布后的几天内就被迅速弃用了。

At the time, it was felt that another feature "run-time parameters" (also called "dynamic constraints", because the run-time parameters could only be used in constraints) could support the same efficiency requirement, but run-time parameters (dynamic constraints) were eventually abandoned. 当时认为，另一种名为“运行时参数”的功能（也被称为“动态约束”，因为运行时参数只能在约束条件下使用）也能满足相同的效率要求。不过，最终决定放弃使用运行时参数（动态约束）。

The approach was abandoned not because of any inherent problems, but simply that the marketplace (ASN.1 users) did not really seem to be demanding it, and adding a further fairly complex feature to ASN.1 did not seem worthwhile. 这种方法的采用并非因为存在任何固有的问题，而是因为市场（ASN.1 用户）似乎并不迫切需要这种功能。此外，在 ASN.1 中添加一项相当复杂的特性似乎也并不值得。

What were these run-time parameters? The idea was that a type could be a parameterised type, but the actual parameters would be transmitted in an instance of communication rather than being specified when the type was referenced. This would enable any information that was common to a SEQUENCE OF (for example the object identifiers of SEQUENCE OF CHARACTER STRING, or the identification of the types for each column of a table) to be transmitted just once, rather than with each element of the SEQUENCE OF. 这些运行时参数到底是什么？其概念是，一种类型可以作为一个可参数化的类型，但实际上这些参数是通过通信实例来传递的，而不是在引用该类型时直接指定。这样就能实现一种优化，即那些在“序列”中常见的信息（例如，序列中所有字符字符串对象的标识符，或者表中每一列类型的标识）只需传输一次，而无需为序列中的每个元素都单独传输这些信息。

Another abandoned feature was "global parameters". If you have a parameterised type, it is quite common for parameters to be passed down from the abstract syntax definition through many levels of type definition to the point where they are eventually used. 另一个被废弃的功能是“全局参数”。如果你有一个参数化的类型，那么参数通常会从抽象语法定义开始，经过多个级别的类型定义，最终被使用到具体的代码中。

The global parameters work was intended to improve clarity and reduce the verbosity of specifications by providing essentially a direct path from a parameter of the abstract syntax to the point where it would be used. 这些全局参数的设计旨在提高文档的清晰度，并减少规范的冗余程度。它们提供了一种直接的路径，从抽象语法中的某个参数直接指向该参数实际会被使用的位置。

If you rather like some of these ideas, get into the standardization game and see if you can bring them back! If you don't want to get into the standardization game, then just agree that ASN.1 is great as it is, and we can end this chapter! 如果你觉得其中一些想法还不错，那么不妨尝试进行标准化工作，看看能否将它们重新引入到讨论中！如果你不想参与标准化工作，那只需同意现状，即 ASN.1 已经很不错了，我们可以就此结束这一章的讨论吧！

END OF CHAPTER. 本章结束。

# Chapter 2 Applications of ASN.1 第 2 章 ASN.1 的应用

## (Or: Are you using software that does ASN.1 encodings?) （或者：您使用的是可以进行 ASN.1 编码处理的软件吗？）

## Summary: 总结：

This chapter: 这一章：

• Tries to provide an indication of the application areas in which ASN.1 has been used. • 试图指出那些已经应用了 ASN.1 的领域。

• Tries to identify some of the organizations that have used ASN.1 as their chosen specification-language. • 试图找出那些将 ASN.1 作为指定语言的组织。

• Uses a partial historical framework for the discussion of applications and organizations. • 在讨论相关应用和组织时，采用了部分历史背景作为参考框架。

## 1 Introduction 1 引言

This brief chapter outlines some of the areas in which ASN.1 has been applied. It in no way claims to be exhaustive, and if some groups feel offended that they have not been mentioned, I apologise! 这一小节简要介绍了 ASN.1 所应用于的一些领域。当然，这份列表并非详尽无遗；如果有些团队因为未被提及而感到不满，请谅解！

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/54379e17-c034-430b-894c-f77661f731e5/6bf2cdb75daf70c884363fbabdd16c90ab1a02e5d71e7727d09b2686eb66c423.jpg)

Equally, I have seen Web pages that say they will include their ASN.1 definitions, only to be assured by people I trust that use of ASN.1 for that particular application was abandoned! I hope there are not too many errors in what follows, but I am sure there are serious omissions. 同样，我也见过一些网页声称会包含他们的 ASN.1 定义。不过，后来我了解到，那些信任的人已经放弃了在那种特定应用中使用 ASN.1 的做法。希望以下内容中没有太大的错误，但我确信肯定有一些重要的信息被遗漏了。

Whilst the emphasis is on different applications, the treatment is partly historical, showing the gradual extension of the use of ASN.1 from a single application (X.400) to a wide range of applications today. 虽然重点在于不同的应用场景，但这部分内容也带有一定的历史性质，展示了 ASN.1 技术从最初仅应用于 X.400 系统，逐渐扩展到如今广泛应用于各种场景的过程。

Thus this chapter complements the previous historical chapter. 因此，这一章是对之前历史章节的补充。

The chapter does not contain a detailed list of ISO Standard numbers and ITU-T Recommendations and Internet RFCs, but rather gives a broad outline of application areas with the occasional mention of an actual specification as an illustration. 这一章节并未列出详细的 ISO 标准编号、ITU-T 推荐标准以及互联网 RFC 文件列表，而是简要介绍了这些标准的应用领域，偶尔会提及一些具体的规范作为示例。

For anyone interested, a more complete set of detailed references to specifications using ASN.1 can be found via the URL in Appendix 5, or in the companion text by Olivier Dubuisson (also referenced via Appendix 5). 对于感兴趣的人士来说，如果想要更完整的关于 ASN.1 规范的详细参考信息，可以通过附录 5 中的链接获取，或者参考 Olivier Dubuisson 撰写的配套文档（该文档也在附录 5 中有提及）。

Most of the acronyms in this chapter can be used as input to Web search engines, and will usually result in hits on home-pages for the relevant organizations or specifications. This is the best way to obtain more information if Appendix 5 does not work for you! (Web URLs have a habit of changing!) 本章中的大多数缩写都可以作为搜索关键词输入到网络搜索引擎中，通常能够找到相关组织或规格的详细信息。如果附录 5 无法提供所需信息，这种方法就是获取更多资料的最佳途径！（不过，网络链接的内容可能会随时发生变化。）

There are also Web sites (access via Appendix 5 or a search) for ITU-T and ETSI and ECMA that will give you much more information about their specifications, and in the case of ITU-T a list of the Recommendations that use ASN.1. (If you get interested in any of the ITU-T Recommendations, beware - they can all be purchased and delivered on-line, but it will cost you serious money!) 此外，还有一些网站可以提供 ITU-T、ETSI 和 ECMA 的相关信息（可通过附录 5 或在线搜索获取）。这些网站能为您提供大量关于其规范的信息。对于 ITU-T 的规范，这些网站还会提供使用 ASN.1 的推荐方案列表。不过，如果您对 ITU-T 的某些推荐方案感兴趣，请注意——这些资料都可以在线购买，但价格相当昂贵！

This chapter inevitably contains a lot of acronyms - every protocol and every organization has its own acronym. I try to spell out the acronym if it has not been used in earlier text, but sometimes it it seems hardly worth the effort, because the acronym is often far better known than the full title! 这一章中不可避免地会包含很多缩写词——每种协议和每个组织都有各自的缩写名称。如果之前的相关文字中已经使用过某个缩写词，我会尽量将其完整拼写出来；但有时候，似乎并没有必要这么做，因为很多缩写词本身就比完整的名称更容易被人记住！

In many cases you will find that a document you locate via a search uses the acronym without giving the full name. Many, many people know these acronyms, but would have to think hard to give you the full name, and would probably then get it wrong! (In some cases, different Web and other documents give different full names for the same acronyms - but clearly intend to identify the same thing!) 在许多情况下，你会发现通过搜索找到的文档中，缩写词被使用而没有提供完整的名称。很多人都知道这些缩写词，但要想提供完整的名称就需要花费较多精力，而且很可能还会出错！（在某些情况下，不同的网页和其他文档可能会给出相同缩写词的不同完整名称——但显然它们指的是同一件事！）

So, we do our best. But if you want a challenge, see what you can find out about the following acronyms (in the ASN.1 context). They are given in no particular order. Some are mentioned in this chapter, most are not. It is believed that they all relate to protocols or organizations that are using ASN.1 as a specification language. Test yourself on the following: 所以，我们会尽力而为。不过，如果你想要挑战一下，可以试着了解以下这些缩写的含义（在 ASN.1 领域里）。这些缩写并没有特定的排序。有些在本章已经提到过，而大多数则没有。相信这些缩写都与那些使用 ASN.1 作为规范语言的协议或组织有关。你可以自己来测试一下：

SET, SNMP, TCAP, CMIP, PKCS, MHS, ACSE, CSTA, NSDP, DPA, TDP, ETSI, DMH, ICAO, IMTC, DAVIC, DSS1, PKIX, IIF, LSM, MHEG, NSP, ROS(E), FTAM, JTMP, VT, RPI, RR, SCAI, TME, WMtp, GDMO, SMTP. SET、SNMP、TCAP、CMIP、PKCS、MHS、ACSE、CSTA、NSDP、DPA、TDP、ETSI、DMH、ICAO、IMTC、DAVIC、DSS1、PKIX、IIF、LSM、MHEG、NSP、ROS(E)、FTAM、JTMP、VT、RPI、RR、SCAI、TME、WMtp、GDMO、SMTP。

If you don't get 100% (although some could of course be mistyping!), you are not a network guru, and can't charge $££££$ per hour for your advice on network matters! 如果你无法达到 100%的正确率（当然，也有可能存在一些错误！），那么你就不算是个网络专家了。因此，你无法以每小时 $££££$ 的价格来收取关于网络问题的建议费用！

If you commute between Europe and the US and are active in both communities, you stand a better chance of meeting the challenge than those operating on only one side of the Atlantic pond. Of course, ASN.1 tool providers CERTAINLY know what all these acronyms mean, 'cos they are selling their tools to support them. But will they tell? 如果你在欧洲和美国之间往返通勤，并且同时活跃于这两个社区，那么你就有更大的机会应对这一挑战。当然，那些提供 ASN.1 工具的公司肯定明白这些缩写的含义——因为它们正是通过这些工具来提供支持的。不过，他们会主动说明吗？

Well, I honestly admit that after a fair bit of research I can cover about 95% of the above list (I have described a lot less than 95% in this chapter), but certainly not all! 嗯，老实说，经过一番研究后，我承认自己能够涵盖上述列表中的大约 95%内容（在本章中，我描述的内容还不到 95%）。当然，并不是所有的内容都能被涵盖啦！

If any reader can cover the lot (and preferably give a URL for further info) then an e-mail to the my address via the link in Appendix 5 would be welcomed - but too late for this book, maybe the second edition? 如果有任何读者能够提供相关的信息（最好是附上网址以便进一步了解），那么可以通过附录 5 中的链接发送电子邮件至我的地址。不过，对于这本书来说，现在可能已经太晚了，也许可以在第二版中补上这些信息吧？

## 2 The origins in X.400 2 其起源可以追溯到 X.400 系统。

X.400 was originally a related set of CCITT Recommendations covering (with gaps) X.400 to X.430. The X.400 specifications were intended to become the (OSI) de facto e-mail system for the world. X.400 最初是一组与 CCITT 建议书相关的标准，涵盖了从 X.400 到 X.430 的内容。X.400 规范旨在成为全球范围内事实上的电子邮件系统。

Everything has a beginning! 一切都有个开始！

X.400 started off with many advantages over the Internet mail protocol (at that time it was Simple Mail Transfer Protocol (SMTP), with no frills - frills like Multipurpose Internet Mail Extensions (MIME) were added later). X.400 相比当时的互联网邮件协议有着许多优势（当时的协议只是简单的邮件传输协议，没有附加功能；直到后来才出现了像多用途互联网邮件扩展标准这样的附加功能）。

X.400 from the start supported a variety of different types of "body part", permitting multi-media attachments to mail, and in its 1998 version incorporated virtually all the security features of the Military Message Handling Systems (MMHS) specifications (security features in SMTP are still very much poorer). X.400 从一开始就支持多种不同类型的“主体部分”，允许在邮件中附加多媒体内容。在 1998 年版本中，它几乎包含了军事消息处理系统规范中的所有安全功能（而 SMTP 的安全性功能仍然相对较弱）。

SMTP was, however, enhanced with the MIME extensions to provide for the transfer of arbitrary attachments (albeit at about twice the band-width of X.400) and Internet mail implementations today generally do not accept mail from outside their own domain, reducing (but not eliminating) the risks of masquerade. (None of this work is ASN.1-based.) But whatever the technical merits or otherwise, we all know that SMTP-based e-mail is now the world's de facto standard, although X.400 still plays a roll in gateways between different mail systems, and in military communications, and has other minority followings. 不过，SMTP 通过 MIME 扩展得到了改进，从而能够传输任意类型的附件（不过其传输带宽大约是 X.400 的两倍）。如今，大多数互联网邮件系统都不接受来自自身域之外的邮件，这在一定程度上降低了伪装攻击的风险。不过，这些技术改进并非基于 ASN.1 标准。但无论从技术角度来看如何，我们都明白，基于 SMTP 的电子邮件现在已成为全球的事实标准。虽然 X.400 仍在不同邮件系统之间的网关通信以及军事通信中发挥着作用，而且还有一些小范围的追随者。

ASN.1 was originally produced to support just this one X.400 specification, and is, of course, still used in all the ongoing X.400 work. ASN.1 最初就是为了支持 X.400 规范而设计的，目前仍然被广泛应用于所有的 X.400 相关工作中。

Another important specification which was originally produced to support just X.400 was the Remote Operations Service Element (ROSE) specification - originally just called "ROS". Like ASN.1, this became recognised as of more general utility, and moved into the X.200 series of Recommendations. (ROSE is discussed further in Section II Chapter 6). ROSE was (and is) totally ASN.1-based and is the foundation of many many applications in the telecommunications area. Its requirements were very influential in the development of the Information Object concept and in the recognition of the need to handle "holes". (See the previous chapter on the history of ASN.1.) 另一个重要的规范是远程操作服务元素（Remote Operations Service Element，简称 ROSE）规范——最初仅被称为“ROS”规范。与 ASN.1 类似，该规范也逐渐被认可，并纳入了 X.200 系列建议中。关于 ROSE 的详细信息请参见第二章第 6 节。ROSE 完全基于 ASN.1 规范，是电信领域许多应用的基础。其规范在信息对象概念的发展以及解决“漏洞”问题的需求方面发挥了重要作用。（有关 ASN.1 历史的更多信息，请参考前一章。）

## 3 The move into Open Systems Interconnection (OSI) and ISO 3. 转向开放系统互连以及 ISO 标准

In the early 1980s, papers at conferences would have titles like "OSI versus SNA" (SNA was IBM's "Systems Network Architecture"), with most people believing that the OSI work would eventually become the de facto standard for world-wide networking, but would have a battle 在 20 世纪 80 年代初，会议上的论文标题常常类似“OSI 与 SNA 的比较”（SNA 是 IBM 提出的“系统网络架构”），大多数人认为 OSI 标准最终会成为全球网络的标准。不过，两者之间确实存在竞争关系。

Rapid expansion to take over the world through OSI - supposedly! But also take-up by several other ISO Technical Committees. 通过 OSI 技术实现迅速扩张，以征服世界——至少是这样吧！而且，还有其他几个 ISO 技术委员会也加入了这一计划。

to unseat SNA. Again, historically, OSI as a whole never really made it, but it was the introduction of ASN.1 into main-stream OSI that moved ASN.1 from being a single-application language into a tool used by many protocol specifiers. 为了推翻 SNA 的统治地位。从历史上看，OSI 作为一个整体其实一直并不成功，但正是 ASN.1 被引入到 OSI 标准中，使得 ASN.1 从一种单一应用语言转变为一种被许多协议规范者使用的工具。

Very soon after it was introduced from CCITT (as it then was) into ISO, ASN.1 was adopted as the specification language of choice by every single group producing specifications for the Application Layer of OSI and for many other OSI-related standards. Implementations of most of these standards are still in use today, but it is fair to say that in most cases they are in a minority use. 自从它被从 CCITT（当时的名称）引入到 ISO 之后，ASN.1 很快就被成为所有负责制定 OSI 应用层规范以及许多其他与 OSI 相关的标准的团体所选择的规范语言。目前，这些标准中的大多数仍然在应用之中，但可以说，在大多数情况下，ASN.1 只是少数被使用的规范语言而已。

Most of the OSI applications of ASN.1 were for standards in the so-called "Application Layer" of OSI, developed by ISO/JTC1/SC16, and then (following a reorganization) by ISO/JTC1/SC21. These covered, inter alia, standards for remote database access, for transaction processing, for file transfer, for virtual terminals, and so on. ASN.1 的 OSI 层应用大多属于 ISO/JTC1/SC16 工作组所制定的所谓“应用层”标准。这些标准包括远程数据库访问、事务处理、文件传输、虚拟终端等方面的规范。这些标准在后来经过一些调整之后，由 ISO/JTC1/SC21 工作组继续负责维护。

The ASN.1 concepts of a separation of abstract and transfer syntax fitted very well with the socalled "Presentation Layer" of OSI for protocols running over the OSI stack and using the Presentation Layer to negotiate the transfer syntax to be used for any given abstract syntax. ASN 的抽象与传输语法分离的概念，非常适用于 OSI 层次结构中所谓的“表示层”。对于那些在 OSI 层次上运行的协议来说，使用表示层来协商用于特定抽象语法的传输语法，是一种非常有效的做法。

Interestingly, however, ASN.1 was also used to define the Presentation Layer protocol itself - probably the first use of ASN.1 for a protocol which did not run over the OSI Presentation Layer (many others were to follow). 不过，有趣的是，ASN.1 也被用来定义呈现层协议本身——这可能是 ASN.1 首次被用于描述一种并非基于 OSI 呈现层运行的协议。此后还有许多其他例子也使用了 ASN.1 来描述类似的协议。

There was even a draft circulated showing how the OSI Session Layer (the layer below the Presentation Layer) could be defined (more clearly, and in a machine-readable format) using ASN.1. This was accompanied by a draft of a "Session-Layer-BER" which was a minor change to BER and which if applied to the ASN.1 definition would produce exactly the bits on the line that the Session Protocol Standard currently specified. But the Session Layer specifications were complete and stable by then, so the draft was never progressed. 甚至还有一份草案，其中详细描述了如何使用 ASN1 来明确定义会话层（位于表示层之下的一层）。该草案还包含了一份名为“会话层 BER”的修改方案，其实就是对 BER 进行的轻微调整。如果将该方案应用到 ASN1 的定义中，就能得到与会话协议标准当前规定的二进制位完全一致的结果。不过，当时会话层的规范已经相当完善且稳定了，因此这份草案最终并没有得到进一步的发展。

A similar situation arose with the Generic Definition of Managed Objects (GDMO) - see Clause 8 below, where an equivalent notation using Information Object Classes and "WITH SYNTAX" was identified in a circulated draft - from Japan - but was never progressed because the GDMO work was by then stable and quite mature. 关于“受管理的对象通用定义”（GDMO）这一方面也出现了类似的情况——请参考下面的第 8 条。在一份来自日本的草案中，提到了一种使用“信息对象类”和“具有语法”的等效表示方式。不过，由于 GDMO 的相关工作当时已经相当成熟且稳定，因此这一提议并未得到进一步推进。

ASN.1 has been used in many other ISO Technical Committees, in areas such as banking, security, protocols for control of automated production lines, and most recently in the development of protocols in the transportation domain for "intelligent highways". These protocols are often (usually) not carried over the OSI stack, and have served to show the independence of ASN.1 from OSI, despite its early roots in the OSI work. ASN.1 已被许多其他 ISO 技术委员会所采用，这些领域包括银行业、安全性、自动化生产线控制协议，最近则用于“智能高速公路”领域的协议开发。这些协议通常无法在 OSI 层结构中延续使用，这充分体现了 ASN.1 与 OSI 的独立性，尽管 ASN.1 的起源可以追溯到 OSI 工作。

A recent example of such use is for the definition (by ISO/TC68) of messages passing between an Integrated Circuit credit card and the card accepting device. 最近的一个应用实例是，根据 ISO/TC68 的标准，这种机制被用于定义集成电路信用卡与受理该信用卡的终端设备之间的通信方式。

## 4 Use within the protocol testing community 4. 在协议测试领域中使用

As well as protocol specifications, the OSI world started the idea of standardized tests of protocol implementations. These test sequences are, of course, protocols in their own right, where a testing system sends messages to an implementation under test, and assesses the responses it gets. The Tree and Tabular Combined Notation (TTCN) is the most commonly used notation for this purpose, and ASN.1 is embedded within this notation for the definition of data structures. 除了协议规范之外，OSI 领域还提出了对协议实现进行标准化测试的理念。这些测试序列本身也是一种协议，其中测试系统会向被测试的实现发送消息，并评估该实现所返回的响应。树状与表格结合表示法（TTCN）是最常用的这种测试表示方法，而 ASN.1 则用于定义数据结构。

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/54379e17-c034-430b-894c-f77661f731e5/999d030e1a163a1e941ec951ff0c23ea0a605752ea724d6bee1fa3a1b1acb219.jpg)

Closely related to the TTCN application is the use of ASN.1 within another ITU-T formal description technique, System Description Language (SDL). 与 TTCN 应用密切相关的是在 ITU-T 另一种正式描述技术——系统描述语言（SDL）中运用 ASN.1 标准的情况。

The European Telecommunications Standards Institute (ETSI) has been a major actor in the development of testing specifications using these notations. 欧洲电信标准协会（ETSI）在采用这些标记方式来制定测试规范方面发挥了重要作用。

## 5 Use within the Integrated Services Digital Network (ISDN) 5. 在综合业务数字网络（ISDN）中的应用

In the 80's, Integrated Services Digital Network (ISDN) was the great talking point. It grew out of the digitisation of the telephone network. 在 80 年代，综合业务数字网络（ISDN）成为了当时的热门话题。这一技术起源于电话网络的数字化改造。

<table><tbody><tr><td data-imt-p="1">Probably the first application of ASN.1 outside of the main OSI work. 这可能是 ASN.1 在 OSI 模型之外领域的首次应用。</td></tr></tbody></table>

The telephone network in most advanced countries is now entirely digital apart from the so-called "local loop" between homes and the local telephone exchange, which in the majority of cases remains analogue. 在大多数发达国家，电话网络已经完全实现了数字化，不过在家庭与当地电话交换站之间的连接仍然采用模拟方式。

ISDN provided, using the existing local loops between homes and a local telephone exchange, two so-called "B-channels" each capable of carrying a telephone call or a 64 Kbps data connection, and a "D-channel" (used for signalling between the subscriber and the exchange). ISDN became widely available to telephone subscribers, but its main application was (and still is today - 1999) the use of the two B-channels together to provide a 128 Kbps data channel for video-conferencing over the telephone network. ISDN 通过利用家庭与当地电话交换局之间的现有局部回路，提供了两种所谓的“B 通道”。每种通道都能支持一个电话通话或 64 Kbps 的数据传输。此外，还有一条“D 通道”，用于实现用户与交换局之间的信号传输。ISDN 逐渐被电话用户所接受，但其主要应用方式仍然是将这两种 B 通道结合起来，从而通过电话网络实现 128 Kbps 级别的数据传输，用于视频会议等应用。这一技术至今仍被广泛应用。

Within ISDN, many so-called "supplementary services" (for example, Call Back to Busy Subscriber) were implemented using the D-channel, and ASN.1 (with BER encodings) was chosen to define the protocol for these services. 在 ISDN 标准中，许多所谓的“附加服务”都是通过 D 通道来实现的（例如，回拨到繁忙用户的功能）。这些服务的协议定义采用了 ASN.1 格式，并使用了 BER 编码方式。

## 6 Use in ITU-T and multimedia standards 6. 适用于 ITU-T 标准和多媒体标准

ASN.1 was, of course, first introduced to ITU-T through X.400 and OSI, but was rapidly taken up by many other standardization groups within ITU-T (then CCITT). ASN.1 最初是通过 X.400 和 OSI 标准被引入 ITU-T 的，但很快就被 ITU-T 内部的其他许多标准化组织所采用（当时称为 CCITT）。

<table><tbody><tr><td data-imt-p="1">Widespread use of ASN.1 throughout many parts of ITU-T continues to this day. ASN.1 在 ITU-T 的许多领域中被广泛使用，这一现象一直持续到了今天。</td></tr></tbody></table>

Uses of ASN.1 within ITU-T can be found in: ITU-T 标准框架中，ASN.1 的应用可以在以下文档中找到：

• The G-series recommendations for speech encoding and silence compression. • G 系列产品对语音编码和静音压缩方面的建议。

• The H-series for multimedia (audio-visual) communications, including moving video coding for low bit rate communication, and specifications being implemented by the Interactive Multimedia Teleconferencing Consortium (IMTC). • H 系列用于多媒体通信（音视频通信），包括适用于低比特率通信的动态视频编码技术。这些规范由互动多媒体电话会议联盟（IMTC）负责实施。

• The M-series for test management in ATM. • 适用于 ATM 测试管理的 M 系列产品。

• The Q-series for a host of specifications related to ISDN and Intelligent Networks (IN). • Q 系列产品涵盖了与 ISDN 和智能网络相关的各种规格。

• The T-series for group 3 facsimile and for MHEG communications. • T 系列适用于第三组的仿真功能，以及 MHEG 通信需求。

• The V-series for audio-visual terminal communication. • 适用于视听终端通信的 V 系列产品。

• The Z-series for use within SDL (described above) and within GDMO (described in Clause 8 below). • Z 系列设备适用于 SDL 系统（如上所述），也适用于 GDMO 系统（详见下文的第 8 条）。

• And of course, in the X-series for Recommendations that originated in the OSI work. • 当然，在 X 系列的相关功能中，这些功能都是基于 OSI 规范中提出的建议而设计的。

Regarding the H-series, the most important of these Recommendations is perhaps the H.323 series for audio, video, and data communication across the Internet (including video-conferencing, interactive shopping, network gaming, and many other multi-media applications - check out the H.323 Web site for further details). Other specifications in the H.320 series address multimedia communication over both narrow-band and broad-band (ATM) ISDN and PSTN communications. These Recommendations seem set to become de facto standards for multi-media communication that will operate over a wide range of network infrastructures. 关于 H 系列协议，其中最重要的规范可能是 H.323 协议。该协议适用于通过互联网进行的音频、视频和数据通信（包括视频会议、互动购物、网络游戏等多种多媒体应用——更多详情请参考 H.323 协议网站）。而 H.320 系列规范则涵盖了通过窄带和宽带（ATM）ISDN 以及 PSTN 通信进行的多媒体通信。这些规范似乎将成为在各种网络基础设施上运行的多媒体通信的行业标准。

It is these Recommendations that cause many familiar products to have ASN.1 (PER in this case) encoders embedded wtihin them, so if you use any of these products, you are using ASN.1 (encodings)! Examples of such products are Microsoft NetMeeting, Intel VideoPhone, PictureTel software, and so on and so on. 正是这些建议使得许多常见的产品都内置了 ASN.1 编码方式。因此，如果你使用了这些产品，那就意味着你正在使用 ASN.1 编码方式！这类产品的例子包括 Microsoft NetMeeting、Intel VideoPhone、PictureTel 软件等等。

## 7 Use in European and American standardization groups 7. 适用于欧洲和美国的标准化团体

There are three European standardization groups worth mentioning where ASN.1 has been quite heavily used (no doubt there are others). The first two carry the name "European" in their title, but they all contribute standards to the world-wide community. These are the European Computer Manufacturers Association (ECMA), the 有三个欧洲标准化组织值得一提，在这些组织中，ASN.1 被广泛应用（当然，还有其他组织也使用它）。前两个组织的名称中带有“欧洲”字样，但它们都为全球社区制定标准。这两个组织分别是欧洲计算机制造商协会（ECMA）和——

Many sub-international (to coin a phrase) groups that are really international actors have used ASN.1. 许多属于国际性组织的子组织也使用了 ASN.1 标准。

European Telecommunications Standards Institute (ETSI), and the rather more recent Digital Audio Visual Council (DAVIC). (DAVIC is Europe-based, but would justifiably claim to be a world-wide consortium.) 欧洲电信标准协会（ETSI），以及相对较新的数字音频视觉委员会（DAVIC）。虽然 DAVIC 总部位于欧洲，但它确实可以被视为一个全球性的组织。

ECMA has long worked on OSI-related standards for input into OSI (but also in broader areas - for example, it had significant input into the initial IEEE 802 Standard). It has also produced the ASN.1-based Computer Supported Telecommunications Applications (CSTA) specification for communication between telephone switches and end-user computers. Initial deployment of CSTA has been in support of large Call Centres - an important development in communications in the late 1990s. As is normal with ECMA specifications, the work has been input to ISO for international standardization. ECMA 长期以来一直致力于 OSI 相关标准的研发，这些标准被广泛应用于 OSI 领域（同时也涉及更广泛的领域——例如，ECMA 对最初的 IEEE 802 标准也提出了重要的贡献）。此外，ECMA 还制定了基于 ASN.1 的计算机支持电信应用规范，用于实现电话交换机与终端用户计算机之间的通信。CSTA 规范最初应用于大型客服中心，这无疑是 1990 年代末通信领域的重要进展。像 ECMA 的规范一样，这些成果已经提交给 ISO 进行国际标准化工作。

ETSI is primarily concerned with European variants of ITU-T Recommendations and with the development of telecommunications specifications for input into ITU-T. It has also been active in the development of specifications based on TTCN (which has ASN.1 embedded within it). There is close liaison between ECMA and ETSI on telecommunications standards, and with ITU-T. ETSI 主要关注欧洲地区的 ITU-T 建议的变体，以及为 ITU-T 提供规范的开发工作。该组织还积极参与基于 TTCN 的规范制定工作（TTCN 标准中包含了 ASN.1 标准）。ECMA 与 ETSI 在电信标准方面有着紧密的合作关系，同时也与 ITU-T 保持密切沟通。

DAVIC is a consortium of 157 companies and government agencies from 25 countries promoting video-conferencing. Its specifications are input to ISO for international standardization. DAVIC 是由来自 25 个国家的 157 家企业和政府机构组成的联盟，致力于推动视频会议技术的发展。该联盟的规范被提交给 ISO 进行国际标准化工作。

There are also a number of standards groups and consortia in the USA that have used ASN.1 in their specifications. Frequently, but not always, such work feeds into international standardization. 在美国，还有许多标准组织和联盟在其规范中使用了 ASN.1 标准。通常，这类工作会推动国际标准的制定。不过，并非总是如此。

Worth mentioning (but this list is very incomplete and a bit random - it is the ones I have heard about) are: 值得一提的是（不过这个列表非常不完整，而且内容有些随机——这些只是我听过的例子）：

The ANSI X9 committees concerned with Financial Industry Standardization (Funds Transfer and EDI, for example), feeding into ISO/TC68. 负责金融行业标准标准化的 ANSI X9 委员会（例如，资金转移和 EDI 领域的工作）正在为 ISO/TC68 委员会提供建议。

The American Chemical Society for the exchange of chemical information and DNA sequences (for the Web site, see links via Appendix 5 to the National Centre for Biological Information (NCBI)). 美国化学学会致力于化学信息及 DNA 序列的交换工作（有关网站信息，请参见附录 5 中的链接，该链接指向国家生物信息中心网站）。

Many Federal Information Processing Standards (FIPS) concerned with security matters, for example, FIPS PUB 188 on Standard Security Labels for Information Transfer - the Standard Security Label is defined as an ASN.1 type: "SET OF NamedTagSet" where "NamedTagSet" is .... etc. 许多与安全性相关的联邦信息处理标准（FIPS）规范中，例如 FIPS PUB 188《信息传输的标准安全标签》就定义了标准安全标签。该标准安全标签被定义为一个 ASN.1 类型：“SET OF NamedTagSet”，其中“NamedTagSet”的具体含义则不明确……

• The SET consortium (see Clause 9 below). • SET 联盟（详见下文第 9 条）。

## 8 Use for managing computer-controlled systems 8. 用于管理计算机控制系统

Another major "invention" from the OSI work was the concept of "managed objects" (devices that are interrogated, tested, configured, reset, etc by remote communications). This came out of the work on Common Management Information Services/Protocol (CMIS/CMIP), which produced a model of such objects (identified by ASN.1 object identifiers) having attributes (which were ASN.1 types identified by further ASN.1 object identifiers). "Management" was essentially performed by reading from or writing to these "attributes" (using CMIP) which were, as it were, on the surface of the managed objects, and provided external visibility and contro of the object. OSI 团队的另一项重要“发明”是“管理对象”的概念（即那些可以通过远程通信进行查询、测试、配置、重置等操作的设备）。这一概念源自于通用管理信息服务/协议的研究，该研究提出了一个管理对象的模型（这些对象由 ASN.1 对象标识符标识），并且这些对象具有属性（这些属性又是 ASN.1 类型，进一步由 ASN.1 对象标识符进行标识）。所谓“管理”操作，实际上是通过读取或写入这些“属性”来实现的（使用 CMIP 协议），而这些属性就存在于被管理对象的表面，从而提供了对对象的外部可见性和控制能力。

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/54379e17-c034-430b-894c-f77661f731e5/8162efd0291dcaa79bfae15064b24fc2495ad12a9afae0bf4613f0ee5b6e04ee.jpg)

When the CMIP standard was first published, it was a protocol full of "holes" - not a single managed object and its attributes had been defined at that stage! A notation was clearly needed to allow people to define (preferably in a machine-readable way) managed objects. An ASN.1 macro might well have been used to define that notation, but by then there was an embargo on writing new macros, and the replacement Information Object Class work was still in its infancy. So Generic Definition of Managed Objects (GDMO) was defined (in English) as a notation for specifying the necessary details about managed objects, with ASN.1 as an embedded notation within GDMO. 当 CMIP 标准首次发布时，它存在一个严重的问题：几乎没有管理对象的定义，而且管理对象的属性也尚未明确指定。因此，需要一种能够让人们以机器可读取的方式定义管理对象的符号系统。当时可能会使用 ASN.1 宏来定义这种符号系统，但那时已经禁止了新宏的编写，而替代性的信息对象类规范工作也还处于初期阶段。于是，最终提出了“管理对象通用定义”（GDMO）这一方案——它是一种用于指定管理对象所需细节的符号系统，而 ASN.1 则作为 GDMO 内的嵌入式符号系统被使用。

In the Internet world, the concepts of CMIS/CMIP were adopted, and while work was still continuing on the development of CMIS/CMIP, an RFC was produced for Simple Network Management Protocol (SNMP). Initially, this was stated to be a temporary solution until CMIS/CMIP matured, but like most temporary solutions, it became rather permanent, and has today a greater market share of management of remote devices than does CMIS/CMIP. 在互联网领域，CMIS/CMIP 的概念被采纳了。虽然 CMIS/CMIP 的开发工作仍在进行中，但当时已经发布了关于简单网络管理协议（SNMP）的 RFC 文档。最初，这种解决方案被视作一种临时解决方案，直到 CMIS/CMIP 成熟之后才会被采用。不过，就像大多数临时解决方案一样，简单网络管理协议也逐渐变成了永久性的解决方案。如今，它在远程设备管理领域的市场份额甚至超过了 CMIS/CMIP。

Like CMIS/CMIP, SNMP also uses ASN.1, but in a very cut-down form, and with considerable restrictions on the form of ASN.1 types that can be used to define the values to be set or read on managed objects. This did, however, represent the first real penetration of ASN.1 into the Internet standardization community. 与 CMIS/CMIP 类似，SNMP 也使用了 ASN.1 标准。不过，SNMP 的实现方式要简单得多，而且对于用于定义需要设置或读取的数据类型的 ASN.1 类型也有相当多的限制。尽管如此，这仍然标志着 ASN.1 标准首次真正被纳入了互联网标准化领域。

CMIS/CMIP was originally designed to control implementations of the OSI stack in network switches and remote hosts, but (like SNMP) it is increasingly used today to manage remotely anything that is computer controlled. So applications of management protocols can include the steering of telescopes or radar dishes, or even the switching on and off of washing machines or ovens! (But I am not sure the latter are yet a reality.) CMIS/CMIP 最初是为了在网络交换机和远程主机上实现 OSI 协议的运行而设计的，不过如今它也被越来越多地用于管理任何由计算机控制的设备。因此，管理协议的应用范围可以扩展到控制望远镜或雷达天线的转向，甚至包括控制洗衣机或烤箱的开关操作！不过，我不确定后者是否已经实现啦。

## 9 Use in PKCS and PKIX and SET and other security-related protocols 9. 适用于 PKCS、PKIX、SET 以及其他与安全相关的协议。

Let's just get the acronyms in the title out of the way! PKCS is Public Key Cryptographic Standards, PKIX is Public Key Infrastructure (X.509), and SET is Secure Electronic Transactions (a little more detail on these follows below). 让我们先把标题中的缩写部分处理一下吧！PKCS 指的是公共密钥加密标准，PKIX 指的是公共密钥基础设施（X.509 领域的术语），而 SET 则指的是安全电子交易技术。关于这些术语的详细解释，后面会有所说明。

The wide-spread adoption of X.509 (ASN.1-based) certificates has made ASN.1 the dominant specification technique in security work. X.509 证书标准的广泛采用（基于 ASN.1 标准）使得 ASN.1 成为了安全领域中的主要规范技术。

X.500 is one of the OSI Standards that still has significant support, and its use of ASN.1 in the OSI work has led to adoption of ASN.1 in almost all security-related protocols. X.500 是 OSI 标准之一，至今仍得到广泛支持。它在 OSI 框架中采用 ASN.1 编码的方式，这使得 ASN.1 编码几乎被应用于所有与安全相关的协议中。

X.500 was (and is) an ISO and ITU-T Standard and Recommendation, but the Light-Weight Directory Access Protocol (LDAP), which is a functional subset of X.500 is an Internet RFC, and is rapidly becoming the de facto standard for access to Directory services, leaving X.500 proper for use "behind the scenes" to link local LDAP servers to provide a world-wide Directory service. LDAP uses the ASN.1 notation to define its messages, but specifies a text encoding for values of the (limited) subset of ASN.1 that it uses (see later discussion in Clause 10 on preferences for textbased protocols among Internet specifiers). X.500 曾经是（现在仍然）一项由 ISO 和 ITU-T 制定的标准和建议规范。而轻量级目录访问协议（LDAP）则是 X.500 的一个功能子集，它属于互联网 RFC 标准，正迅速成为访问目录服务的默认标准。真正的 X.500 则用于“幕后操作”，用于将本地 LDAP 服务器连接起来，从而提供全球范围的目录服务。LDAP 使用 ASN.1 表示法来定义其通信消息，但它为 ASN.1 子集中的值指定了文本编码方式（关于互联网规范中基于文本的协议的选择偏好，请参见第 10 条的描述）。

Whilst X.500 was primarily designed to provide a world-wide Directory service, allowing look-up of a very wide variety of information with a world-wide search, it also provided the first standard (X.509) for certificates (which were - and are, of course, an ASN.1 type). 虽然 X.500 最初旨在提供一种全球范围的目录服务，能够查询各种类型的信息，但它同时也提出了第一个证书标准（X.509）——而证书本身其实就是 ASN.1 类型的数据。

The basic certificate concept is that a Certification Authority (CA) will provide a public and private key pair (usually for some commercial fee) to an applicant, and will also provide an electronic bit-pattern (a certificate) that is encrypted using the public key of the CA. The certificate is an ASN.1 type that provides an association between the public key issued to the applicant and some property of the applicant (name, company registration number, etc). Certificates cannot be forged provided the CA keeps its own private key secure. However, anyone knowing (for absolutely sure) the public key of the CA, can decrypt the certificates it issues and hence "believe" the public key of the organization or person that the certificate contains - and hence apply some degree of "trust" to that organization or person (and to messages or signatures that decrypt to produce valid hash values using that public key). Of course, the public key of the CA is usually obtained from another certificate issued by a "higher" CA, whose public key is obtained from another certificate issued by .... and so on, until, .... well, .... the Netscape public key is usually built into your Web browser software! (Which of course you obtained from a trustworthy source!). 基本证书的概念是，认证机构会向申请人提供一把公共密钥和私有密钥对（通常需要支付一定的费用），同时还会提供一份用认证机构的公共密钥加密后的电子证书。该证书属于 ASN.1 类型，它能够实现向申请人颁发的公共密钥与申请人的某些信息（如姓名、公司注册号等）之间的关联。只要认证机构能够保护好自己的私有密钥，那么证书就无法被伪造。不过，只要有人确切知道认证机构的公共密钥，就可以解密该机构颁发的证书，从而相信证书中所包含的组织或个人的公共密钥。这样一来，人们就可以对该组织或个人以及使用该公共密钥解密后得到有效哈希值的信息或签名产生一定程度的“信任”。当然，认证机构的公共密钥本身也是需要被保护的。CA 证书通常是从另一个由“更高权威”的 CA 机构颁发的证书中获得的。该 CA 机构的公钥又来自另一个由……机构颁发的证书……以此类推。最终，……嗯，……Netscape 的公钥通常会被内置在你的网络浏览器软件中！（当然，这些证书都是来自可信来源的）。

This process of obtaining a public key from one certificate to unlock another certificate to get a public key which unlocks another certificate etc is called certificate chaining, and originally people expected just one or two top-level CAs in the entire world, with their public keys really public - perhaps advertised daily in the newspapers! 这种从某个证书中获取公钥以解锁另一个证书的过程，被称为证书链验证。最初，人们认为全世界只有一两个顶级证书颁发机构，它们的公钥应该是完全公开的——或许可以像报纸上那样每天进行公告！

But then just about every national government decided it wanted one of its agencies to be a toplevel CA, and many companies also decided to be their own CA for internal use. And suddenly the problem of distribution of public keys and of degrees of trust got a lot more complicated. 不过，几乎每个国家政府都决定让其中一个机构成为顶级证书颁发机构。许多公司也决定为自己内部使用而设立自己的证书颁发机构。于是，公钥的分发问题以及信任程度的问题就变得复杂多了。

PKIX stands for Public Key Infrastructure (X.509), and is a set of Internet RFCs and Draft RFCs which specify how CAs should operate. For example, PKIX 4 specifies the form of a Certification Policy Statement (CPS) which all conforming CAs should make available to the public. The CPS says, for example, that (before issuing a certificate) the CA should verify individual names by requiring a photo-copy of a passport, or an actual passport, or a birth certificate, or (for a company in the UK) has checked that the Registered Office exists, as registered with Companies House, or ... You get the idea. The certificate they issue asserts that there is some association between the public key it contains and some further information about an individual or company. How much trust can you place in that assertion? The CPS helps you to determine that. PKIX 代表的是公共密钥基础设施（X.509 协议）。它包含一系列互联网 RFC 文档和草案文档，这些文档规定了证书颁发机构应该如何运作。例如，PKIX 4 规范了证书政策声明的形式，所有符合该规范的证书颁发机构都应向公众提供这种声明。该声明规定，在颁发证书之前，证书颁发机构必须验证个人的身份，这可能要求用户提供护照的复印件、真实的护照、出生证明，或者对于在英国注册的公司，还需要确认其注册地址确实存在于公司注册处所记录的地址中……以此类推。他们颁发的证书表明，其中包含的公共密钥与有关个人或公司的其他信息之间存在关联。那么，我们究竟能信任这种声明呢？证书政策声明可以帮助我们判断出这种信任的程度。

Several parts of PKIX use ASN.1, fully and straight-forwardly. 在 PKIX 的多个部分中，完全采用了 ASN.1 标准。

PKCS stands for Public-Key Cryptographic Standards. These are standards produced by a consortium of RSA Data Security and its major licensees, including Microsoft, Apple, Lotus, Sun, Novell, and MIT. PKCS uses ASN.1 as its notation for defining data-structures and their encoding. PKCS 指的是公共密钥加密标准。这些标准是由 RSA 数据安全公司及其主要授权方组成的联盟所制定的，这些授权方包括微软、苹果、Lotus、Sun、Novell 和 MIT 等公司。PKCS 使用 ASN.1 作为定义数据结构及其编码的语法标准。

Another important security-related protocol is Secure Electronic Transactions (SET), produced by a consortium of MasterCard, Visa, and other parts of the computer and banking industries. SET is designed to support electronic commerce in a fully secure manner, and hence uses X.509 certificates, and is itself about 60 pages of ASN.1 (with many more pages of supporting text). 另一个重要的安全相关协议是安全电子交易协议（SET），该协议由万事达卡、维萨卡以及计算机和银行行业的相关机构联合推出。SET 旨在以完全安全的方式支持电子商业交易，因此采用了 X.509 证书体系。该协议文件大约有 60 页，其中还包含大量关于 ASN.1 编码的详细说明。

When SET certificates are stored on smart-cards (because of the limited memory available on smart-cards) PER encoding is likely to be used with an ASN.1 datatype called a compressed certificate. 当 SET 证书存储在智能卡上时（由于智能卡上内存有限），通常会使用 PER 编码方式对 ASN.1 类型的数据进行编码，这种编码方式被称为“压缩证书”。

In general, the use of ASN.1 in X.509 has led most security-related protocols to use ASN.1. 总体而言，X.509 标准中采用 ASN.1 标准的方式，使得大多数与安全性相关的协议也采用了 ASN.1 标准。

## 10 Use in other Internet specifications 10. 在其他互联网规范中的应用

We have already discussed PKCS and PKIX and SNMP. ASN.1 (with PER) was considered for use in the latest version of HTTP, but instead an ASN.1-like notation called "pseudo-C was invented. 我们已经讨论过 PKCS、PKIX 以及 SNMP 了。在最新版本的 HTTP 协议中，考虑过使用 ASN.1 标准（结合 PER 特性）。不过，后来人们发明了另一种类似 ASN.1 的表示方式，称为“伪-C”。

Yes, even here we see some use of ASN.1! 是的，在这里我们也看到了一些使用 ASN1 的情况！

In general, Internet specifiers try to keep protocol specifications as simple as possible and to make it easy for implementors to operate without specialised tools, or using only tools that are in the public domain. 一般来说，互联网规范的设计者们力求使协议规范尽可能简单明了，同时让实施者能够在不使用特殊工具的情况下进行操作，或者仅使用那些属于公共领域的工具。

This tends to lead to protocols that in the end are simply lines of ASCII text (usually defined using BNF), or, if ASN.1 is used, to use of a subset of the ASN.1 notation. 这通常会导致一些协议规范，这些规范最终都只是简单的 ASCII 文本字符串（通常采用 BNF 格式定义），或者，如果使用了 ASN.1 标准，那么就会采用 ASN.1 表示法的某个子集来进行描述。

The Web is very much part of the Internet, but the World-Wide Web Consortium (W3C) now has very much a life of its own. 互联网中的网络部分其实也是互联网的重要组成部分，不过现在，万维网联盟（W3C）已经拥有了自己独立的存在。

It is within the W3C forum that work is on-going to marry XML and ASN.1 through the definition of XML Encoding Rules (XER). This work is recent, and was mentioned also in Section III Chapter 3. 在 W3C 的论坛中，人们正在努力通过定义 XML 编码规则来整合 XML 和 ASN.1 标准。这项工作刚刚开始，而且也在第 III 部分的第 3 章中有所提及。

## 11 Use in major corporate enterprises and agencies 11. 适用于大型企业和机构的使用

It is known that a number of house-hold name corporations and national and international agencies have made use of (and are still using) ASN.1 and its encoding rules to support communications activities within their corporations and agencies. 众所周知，许多家庭式企业以及国内外机构都采用了 ASN.1 标准及其编码规则，来支持其内部之间的通信活动。目前，这些机构和组织依然在继续使用这一技术。

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/54379e17-c034-430b-894c-f77661f731e5/1f002efacb6ddc15f55f3985205bae08c87a6a50da6a21ea284a64a0f3b6ccb1.jpg)

However, attempts to obtain more details for publication in this book met with an almost universal rejection, due to concerns about commercial confidentiality of the applications. With regret, therefore, I have decided to make no mention of any specific name of a commercial organization unless the information about their use of ASN.1 appears on the Web. 然而，试图在本书中提供更多详细信息以进行出版，几乎都遭到了拒绝，因为人们担心这些信息的商业机密问题会受到侵犯。因此，很遗憾，我决定不提及任何商业组织的具体名称，除非有关这些组织使用 ASN.1 的信息能够在网上找到。

I will, however, mention one agency, and this is the International Civil Aviation Organization (ICAO). 不过，我还是要提到一个机构，那就是国际民用航空组织（ICAO）。

The ICAO is worth mentioning because it was the first organization to take-up (and to help in the development of) the Packed Encoding Rules. PER encodings were described in ICAO specifications long before the actual ASN.1 specifications were finally ratified, and use of ASN.1 and PER is fundamental to their Aeronautical Telecommunication Network (ATN). ICAO 值得提及，因为它是第一个采用并参与开发封装编码规则的组织。在正式的 ASN 规范最终得到批准之前，ICAO 规范就已经描述了 PER 编码方式。而 ASN.1 和 PER 的应用，正是其航空电信网络的基础。

## 12 Conclusion 12. 结论

ASN.1 has come a long way from the days when it provided support for just one application (X.400). ASN.1 从最初仅支持一种应用（X.400）的发展，已经取得了巨大的进步。

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/54379e17-c034-430b-894c-f77661f731e5/c60ff5478eec3b041ea80a8d0974a652a5a63f7bc8be05be2f87a80ce304f77f.jpg)

It is now used to a significant extent by all the main specifiers of protocols, and in some (but not all) cases is the dominant specification language. Usually use of the notation is associated with use of the ASN.1-defined encodings, with a few exceptions. 现在，这种表示法被所有主要的协议规范机构广泛使用，在某些情况下（但并非所有情况），它甚至是主要的规范语言。不过，这种表示法的使用通常与 ASN.1 定义的编码方式相关联，有一些例外情况除外。

If you were to wave a magic wand and eliminate from the world all messages that are encodings of ASN.1-defined values, disaster would certainly strike on a scale far beyond any that the most pessimistic have described for possible effects of the Y2K (year 2000) computer bugs. (Or any that actually occurred if you are reading this book post-2000!) 如果你挥动一根魔法棒，将所有用 ASN.1 定义的值进行编码的消息从世界上消除掉，那么灾难必将降临——其规模远远超过最悲观的人所描述的 2000 年计算机漏洞可能带来的后果。（或者，如果你在 2000 年后阅读这本书，那么实际上发生的灾难规模会更加巨大！）

Aircraft would collide, mobile phones would cease to work, virtually all telecoms and network switches would be unmanageable and unmaintainable and would gradually die, electric power distribution systems would cease to work, and to look a little further ahead before we wave our magic wand, smart-card-based electronic transactions would fail to complete and your washing machine might fail to work! But worst of all, your NetMeeting with your newly betrothed would suddenly collapse and your life would become a misery! 飞机将会相撞，手机将无法使用，几乎所有的电信系统和网络交换机都会变得无法维护，并逐渐失效。电力分配系统也会停止工作。再往前看一点，我们挥动魔法棒之后，基于智能卡的电子交易也会无法完成，而你的洗衣机也可能无法运转了！但最糟糕的是，你新订婚的伴侣使用的 NetMeeting 软件可能会突然崩溃，而你的生活将会变得极其痛苦！

It is on that happy note that we will conclude this book! 就带着这种愉悦的心情，我们结束这本书的编写吧！

## APPENDICES 附录

# 1 The Wineco protocol scenario 1. Wineco 协议场景

Many of the examples in this book are based on the development of the "Wineco protocol". This is a fictitious protocol, used simply to illustrate various parts of ASN.1. The first parts of it appear in Figure 13 of Section 1 Chapter 2, and a full copy of the final protocol is given in Appendix 2 below. 本书中的许多示例都是基于“Wineco 协议”的开发的。这实际上是一个虚构的协议，用于说明 ASN.1 中的各种组成部分。该协议的初始部分出现在第 2 章第 1 节的图 13 中，而完整的协议文本则可以在下面的附录 2 中找到。

Wineco is a company selling wine from a variety of outlets, and owning two warehouses, one northern and one southern. Initially all outlets were in the UK only (where the name of an outlet could be supported by the ASCII character set), but later Wineco extended to overseas territories, where a larger character set was needed. Wineco 是一家通过多种渠道销售葡萄酒的公司，同时拥有两个仓库，一个位于北部地区，另一个位于南部地区。最初，所有销售点都仅位于英国境内（此时销售点的名称可以使用 ASCII 字符集来表示）。后来，Wineco 扩展到海外地区，因为在这些地区需要使用更大的字符集来表示销售点名称。

In Figure 13 we see one of the messages we use in the protocol, "Order-for-stock", to request a number of cases of particular types of wine with a specified urgency. We also see the form of a "Branch-identification" type. 在图 13 中，我们看到了该协议中使用的一种消息类型——“订单需求”，用于请求特定类型葡萄酒的一定数量，并明确指定了紧急程度。此外，我们还看到了“分支识别”类型的格式。

In Section 1 Chapter 3 we add the necessary module headers, and some extensibility markers with an insertion point not at the end. Later we turn it into a multi-module specification with "common types" in one module, the top-level type in another, and the ordering protocol message "Order-forstock" in a third. We also introduced a second top-level message in Figure 21, "Return-of-sales", which provides for a report on the sales that have been made within the last period. 在第三章的第一节中，我们添加了必要的模块头文件，以及一些扩展性标记，这些标记的位置并不位于代码的末尾。之后，我们将这个规范扩展为多个模块的组合，其中一个模块包含“通用类型”，另一个模块包含顶层类型，而第三个模块则包含用于排序的协议消息“Order-forstock”。此外，我们在图 21 中引入了第二个顶层消息“Return-of-sales”，该消息用于报告过去一段时间内的销售情况。

In Chapter 4 of Section 1 we populated the "Return-of-sales" message in a hopefully plausible way, but really solely in order to illustrate the remaining ASN.1 basic data types! Exception markers and exception handling are introduced in this Chapter. "Return-of-sales" and the "Reportitem" type it uses are used as the main example for illustration of the output from an ASN.1- compiler-tool, given in Appendix 3 for C and in Appendix 4 for Java. 在第一节的第四章中，我们以一种看似合理的方式填充了“销售回款”信息，但实际上这只是为了展示剩余的 ASN.1 基本数据类型而已！本章还介绍了异常标记和异常处理机制。“销售回款”以及它所使用的“Reportitem”类型，被用作示例来说明 ASN.1 编译器工具的输出结果。相关示例可以在附录 3 中针对 C 语言，以及附录 4 中针对 Java 语言找到。

"Return-of-sales" is also used to illustrate the ASN.1 value notation in at the Section I Chapter 4 (Figure 23). “销售回潮”这一术语也被用来描述 ASN 中的数值表示方式。详见第 I 部分第 4 章（图 23）。

The next use of our example is in Chapter 3 of Section II, when we decide to define a "basic class" protocol as a strict subset of our "full class" protocol, both for ordering and for return of sales. Here we have also added a third top-level message as we enter the digital-cash age! We are up-loading the contents of our electronic till using an enhanced protocol. 我们示例的下一个应用出现在第二部分第 3 章中。在那里，我们决定将“基础类”协议定义为“完整类”协议的严格子集，这一定义适用于排序以及销售退货操作。此外，随着数字现金时代的到来，我们还增加了第三种顶层消息类型。我们现在正在使用一种改进的协议来上传电子收银机的内部数据。

The final major extension is when we decide (in Section II Chapter 6 to change over to use of a Remote Operations metaphor, with four defined operations. This leads to two further modules - one to define the Remote Operations PDU (which in the real world would have been imported from the Remote Operations Service (ROSE) Standard, and one to define the Wineco operation Information Objects. 最后一个重要的扩展环节是，我们在第六章的第二部分中决定采用“远程操作”这一隐喻，并定义出四种具体的操作。这一决策还导致了两个新的模块的创建——一个用于定义远程操作的数据单元（在实际应用中，该数据单元通常来自远程操作服务标准），另一个则用于定义 Wineco 操作的信息对象。

# 2 The full protocol for Wineco 2. Wineco 的完整协议说明

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

# 3 Compiler output for C support for the Wineco protocol 3. 编译器输出结果：C 语言支持 Wineco 协议

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

## 5 ASN.1 resources via the Web 通过网络获取 5 个 ASN.1 资源。

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