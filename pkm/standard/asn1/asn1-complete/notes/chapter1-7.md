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

![b5a17021ebf675f51bc5b4d6fc04ac4a8f5984366727c2bf6464de7684b9487e.jpg](../assets/b5a17021ebf675f51bc5b4d6fc04ac4a8f5984366727c2bf6464de7684b9487e.jpg)

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

![f3f65777b38dcaae9c113508504d1c56820c7ae559d8d46672d169574ed44f43.jpg](../assets/f3f65777b38dcaae9c113508504d1c56820c7ae559d8d46672d169574ed44f43.jpg)

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

![34e48647b11bb6207d907c99875b0320f0d1689793bdf82d105251ae972b52a7.jpg](../assets/34e48647b11bb6207d907c99875b0320f0d1689793bdf82d105251ae972b52a7.jpg)

## 2.6 Exception handling 2.6 异常处理

## 2.6.1 The requirement 2.6.1 要求内容

It is absolutely vital that when you use ellipsis you give a clear statement of what behaviour you expect: 当您使用省略号时，非常重要的是要明确说明您期望看到的行为：

<table><tbody><tr><td data-imt-p="1">Version 1 must be told what to do when hit by version 2 - and you must remember what you told it to do when you write version 2! 在版本 2 的攻击下，必须告诉版本 1 该做什么——而在编写版本 2 时，也必须记住之前告诉版本 1 要做什么！</td></tr></tbody></table>

• From version 1 systems if they receive added material. • 从版本 1 开始，当系统接收到新的素材时，就会执行相应的操作。

• How version 2 systems where mandatory fields have been added are to handle messages from version 1 systems. • 版本 2 的系统增加了一些必填字段，以此来处理来自版本 1 系统的消息。

The former is the more common case, as version 2 additions tend usually to be marked OPTIONAL. 前者更为常见，因为版本 2 中的新增功能通常会被标记为“可选”。

## 2.6.2 Common forms of exception handling 2.6.2 常见的异常处理形式

## 2.6.2.1 SEQUENCE and SET 2.6.2.1 序列与集合

![5210ea855fc4aa07e32f679c37d63e5c84e8731e28a3b0956066ed2c98aff195.jpg](../assets/5210ea855fc4aa07e32f679c37d63e5c84e8731e28a3b0956066ed2c98aff195.jpg)

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

![d1a7e2b74d870eba93cb1d91e50273e262fe0be6d1c5d54b6115e7ee2e9c045d.jpg](../assets/d1a7e2b74d870eba93cb1d91e50273e262fe0be6d1c5d54b6115e7ee2e9c045d.jpg)

It would be positively dangerous to allow specifiers to put in ellipses without thinking through the implications of different sorts of version 1 exception handling behaviour. Ellipsis is not an easy option. It was introduced originally to ensure that the efficient PER encodings were such that some interworking would still be possible between version 1 and version 2 systems, but even with BER, if version 2 additions are made without a clear (earlier) specification of version 1 behaviour, serious problems result. 如果允许指定器在不充分考虑各种版本 1 异常处理行为影响的情况下使用省略号，那将是非常危险的。省略号并不是一个合适的选择。它最初被引入是为了确保高效的 PER 编码方式能够使得版本 1 和版本 2 的系统之间仍然可以进行一定程度的互操作。但是，即使使用 BER 编码，如果版本 2 的新增功能是在没有对版本 1 的行为进行明确规范的情况下进行的，那么就会引发严重的问题。

It may be difficult, it may be a chore, but giving serious consideration to extensibility issues and the associated exception handling is part of the job of a protocol specifier - the job is more than just defining a few data structures! 这可能很困难，也可能是一项繁琐的工作。但是，认真考虑可扩展性问题以及相关的异常处理措施，确实是一个协议规范者的重要职责——这不仅仅是定义一些数据结构那么简单的事情！

Unfortunately, if a bad job is done on exception handling in version 1, it is quite possibly a wholly new (and innocent!) group of specifiers producing version 2 that will suffer from the bad version 1 design. But I am afraid that is life! 不幸的是，如果版本 1 在异常处理方面做得不够好，那么版本 2 中出现的那些新的（且看似无害的）规范条款，很可能会受到版本 1 糟糕设计的负面影响。不过，唉，现实就是这样！

## 2.6.4 Use of the formal exception specification notation 2.6.4 使用正式的异常说明规范

Before leaving this discussion of extensibility, we must make some mention of the use of the formal exception specification notation (the notation that starts with "!"). 在结束关于可扩展性的讨论之前，我们必须提到一种正式的异常规范表示法（以“!”开头的表示法）。

![50b606681376e7defe01a60290b42527658cd4dee413e781786c97c43a8ce49f.jpg](../assets/50b606681376e7defe01a60290b42527658cd4dee413e781786c97c43a8ce49f.jpg)

The important thing (emphasised in the previous clause) is that exception handling should be very clearly stated, and the places in the protocol that particular handling is to be used are clearly identified. If there are relatively few uses of ellipsis, and particularly if the required exception handling is the same for all of them, then there is no real gain in including the formal exception specification notation, and English language text can suffice. (This might be the case if the only ellipses are at the end of SEQUENCE constructs, and the required behaviour in all cases is to silently ignore added material). 重要的是（如前文所述），异常处理部分应该表述得非常清楚，并且协议中明确指出应该使用哪种异常处理方式。如果省略的使用情况相对较少，尤其是当所有情况下所需的异常处理方式都相同时，那么使用正式的异常处理规范其实并没有太大意义，使用英文描述就足够了。（当然，这种情况可能发生在省略出现在“序列”结构末尾的情况下，因为在这种情况下，无论哪种情况，系统都只需忽略新增的内容即可。）

(Actually, that is not quite true - inclusion of the formal notation tells a reader that exception handling has been thought about, and that there is somewhere in the text details of required behaviour, and it is my own personal view that there should be formal exception specification notation wherever extensibility occurs, but I know that there are others that disagree with me!) （实际上，这种说法并不完全正确——使用正式的符号来表示异常处理机制，是为了让读者明白已经考虑到了异常处理的问题，并且文本中也会详细说明所需的行为。我个人认为，在具备可扩展性的地方，就应该使用正式的异常处理规范符号来表示。不过我知道有些人并不认同我的观点。）

In a protocol with perhaps four or five different exception handling procedures specified (to be used with different instances of ellipsis, each behaviour applying to several instances of ellipsis), then use of the formal notation (perhaps simply using "!1", "!2, etc) on each ellipsis can be a simple and convenient way of identifying clearly which behaviour applies to which. Something similar to this is done very effectively in the ROSE protocol (using value reference names for "1", "2", etc), as described in Section II Chapter 6. 在协议中，可能会规定四到五种不同的异常处理机制（这些机制适用于不同的省略号实例，每种机制又可应用于多个省略号实例）。此时，可以在每个省略号上使用正式的符号表示法（比如简单地使用“!1”、“!2”等），这样就能清晰地识别出哪种机制适用于哪个实例。类似的做法在 ROSE 协议中得到了非常有效的实现（使用“1”、“2”等值的引用名称来表示），具体细节请参考第 6 章第二节的内容。

## 2.7 Parameterization issues 2.7 参数化问题

Parameterization is powerful and can be the only way of achieving certain "re-usability" goals, particularly where one group provides a carrier protocol and several other groups fill in the holes in different ways to produce a complete specification. 参数化设计是一种非常强大的方法，它可能是实现特定“可重用性”目标的唯一途径。特别是当某个团队负责提供基础协议，而其他团队则以不同的方式填补其中的空白，从而形成一个完整的规范时。

![9610e63a25ddb6f3a979eaea379f33382be7b35ad2610de3ead33363fc7323a4.jpg](../assets/9610e63a25ddb6f3a979eaea379f33382be7b35ad2610de3ead33363fc7323a4.jpg)

But if a parameterized type is instantiated only a limited number of times within a single specification, then it may be that parameterization is unnecessary, and that the same effect can be achieved more clearly by using different (but similar) type or value definitions. 但是，如果某种参数化类型在单个规范中只会被实例化有限次，那么可能就不需要进行参数化了。通过使用不同但类似的类型或值定义，同样可以达到相同的效果。

Object Set parameters of the abstract syntax are a very good way of providing precise specifications of "must implement all, but can add" versus "can implement a subset, but can't add" versus "this is a guide, add or subtract", but are currently unfamiliar to many readers of ASN.1, and should be accompanied by explanatory text. 在抽象语法中设置参数是一种很好的方式，它可以清晰地区分“必须实现所有功能，但可以添加某些内容”与“可以实现部分功能，但不能添加某些内容”的情况，以及“这是一个指导性规范，可以增减内容”的情况。不过，目前很多使用 ASN1 的读者并不了解这种表达方式，因此应该附带相应的解释文本。

Integer parameters of the abstract syntax (used in bounds) are also a very good way of clearly indicating that (for whatever reason), you have chosen to leave implementation-dependent features in your specification. 在抽象语法中，整数参数也是一种很好的方式，可以清楚地表明：出于某种原因，您选择将依赖于实现的特性留在了规范中。

But in both these cases, it is essential that exception handling procedures be fully specified, as discussed earlier. 但在这两种情况下，正如之前所讨论的那样，必须完全明确异常处理流程。

The use of the {...} notation is a form of parameterization, declaring that the object set to be used is implementation dependent, and is generally a less clear and precise notation than parameterization (but there are those that would disagree!). 使用{...}这种表示法是一种参数化方式。它表明所指定的对象取决于具体的实现情况，这种表示法通常不如参数化方式那么清晰和精确（不过，也有人不认同这种观点！）。

It is important if this notation is used, that text clearly specifies how it is intended (by whom and where) for the specification to be completed, and what implications there are on interworking, and what exception handling is to be applied. If that is done, this notation can produce a less cluttered specification than a lot of different parameters (object sets of various classes) being passed from the top-level type all the way down to where they are being used as a constraint. 如果采用这种表示方式，那么文本中明确说明该规范是由谁在何处制定的非常重要。同时，还需要明确关于相互协作的注意事项，以及需要如何处理异常情况。只要做到这一点，这种表示方式就能比使用许多不同参数（各种类别的对象集合）来传递信息的方式，使规范更加简洁明了。

Finally, remember (Section II, Chapter 7) that if you have a lot of parameters of a parameterised type (or other form of reference name), you can reduce them to a single object set parameter by defining a suitable Information Object Class whose objects carry the complete set of information for each parameter. This can be a very useful simplification and reduction of verbosity in your text. 最后，请记住（第 7 章第 II 节）：如果你有很多参数化类型的参数（或其他形式的引用名称），你可以将这些参数简化为单个对象集参数。通过定义一个合适的信息对象类，使得每个对象的参数都包含完整的相关信息，这样就能大大简化文本中的冗余信息。这确实是一种非常有用的简化方式，能减少文本的复杂性。

## 2.8 Unconstrained open types 2.8 无约束开放类型

Unconstrained open types - elements of sequences looking like, for example: 无约束的开放类型——序列中的元素，比如：

![65769f7f387f58331163e4ce633614f1208502e7cb56dee68533e01a3ae0c029.jpg](../assets/65769f7f387f58331163e4ce633614f1208502e7cb56dee68533e01a3ae0c029.jpg)

## OPERATION.&Type 操作与类型

are syntactically allowed in ASN.1 as part of the Seoul (see Section IV Chapter 1) introduction of the Information Object Class concept, but that was largely in response to a perceived need to provide syntax that was semantically equivalent to the old "raw ANY", and I hope the reader (at least those that have read Section II) by now appreciates that a "raw ANY" (and hence an unconstrained open type) is a BAD THING. 在 ASN.1 中，这些语法结构是被允许的。这是作为“信息对象类”概念引入的一部分（详见第 1 章的第四部分）。不过，这些规定的实施主要是出于一种需求——即需要提供一种在语义上与旧的“原始 ANY”结构等效的语法规则。希望读者们（至少那些阅读了第二部分内容的人）能够理解，所谓的“原始 ANY”结构（以及由此产生的无约束开放类型）其实是一种糟糕的设计。

All that a tool can deliver for this construct is an octet string. And even the implementor of the application has no clear indication of where to look to find out the possible types that can occur in this element, the semantics associated with those types, and which type has actually appeared in a given instance of communication, that is, how to decode and interpret the octet string. 该工具为这种结构所能提供的内容仅是一个八位元字符串而已。甚至应用程序的实现者也无法明确知道应该去哪里查找有关该元素可能存在的各种类型的信息、与这些类型相关的语义信息，以及在实际的通信实例中究竟出现了哪种类型的信息。也就是说，人们无法解码和解释这个八位元字符串所包含的内容。

As a specifier in the years 2000 onwards, please don't use this form, even 'tho' you are allowed to! Look at the ROSE chapter (Section II Chapter 6) to see how to give a more precise and implementable specification of these sorts of constructs. I suspect that if ASN.1 is still going strong in 2010, forbidding this unconstrained construct may become possible (I am likely to campaign for it!), provided nobody shouts "1990, 1990!" (again, see Section IV Chapter 1!). 在 2000 年代及之后，作为规范说明者，请不要使用这种形式来表达描述，尽管你是可以这么做的！请参阅 ROSE 规范中的相关章节（第二部分，第六章），了解如何给出更精确且易于实施的这类结构的描述。我认为，如果 ASN.1 在 2010 年仍然保持强大的发展势头，那么禁止这种无约束的结构可能就会成为现实（我可能会积极倡导这一点！），只要没有人喊出“1990 年，1990 年！”这样的口号即可（同样，请参阅第四部分，第一章）。

## 2.9 Tagging issues 2.9 标签相关问题

If you are writing a new specification, you should use AUTOMATIC TAGS (and - as an aside - not specify enumeration values for enumerations). But if you are adding to an existing specification, life can be more complicated. 如果你正在编写新的规范文档，那么应该使用 AUTOMATIC TAGS 功能（另外，不要为枚举类型指定枚举值）。但如果你是在对已有的规范进行补充修改，情况可能会更复杂一些。

![18c78ca07d19ca8aaf0bd550daa7242373d939bb01e7572bee9cb7da46211385.jpg](../assets/18c78ca07d19ca8aaf0bd550daa7242373d939bb01e7572bee9cb7da46211385.jpg)

Remember that a textually present tag construct automatically disables automatic tagging in a CHOICE, SEQUENCE, or SET - you are back in control (with IMPLICIT tagging). 请记住，文本中出现的标签结构会自动使系统不再进行自动标签添加操作——此时您可以重新控制这一过程（使用隐式标签添加功能）。

If you have good reasons not to use AUTOMATIC TAGS, then you need to have a much greater understanding of tagging, but should then always use IMPLICIT TAGS in your module header. Using an explicit tagging environment in modern specifications would be confusing, and you would either have a very verbose protocol (with BER), or a specification that was littered with the word IMPLICIT. 如果你有充分的理由不使用自动标签，那么你需要对标签的使用有更深入的理解。不过，无论如何，你都应该在模块头文件中使用显式标签。在现代规范中，使用显式标签环境会导致混乱，要么会使协议文本变得冗长，要么会让规范中充斥着“显式”这个词。

If you choose, to specify that certain tags are EXPLICIT, the reasons for this will be obscure to most readers, and you should indicate in your text why this was done. 如果你选择明确说明某些标签是可选的，那么对于大多数读者来说，这些标签被明确指定的原因将会很模糊不清。因此，你应该在文本中明确说明这样做的原因。

There are usually two possible reasons: in an implicit tagging environment, tags on a choice type do in fact become explicit tags. It can help people implementing without a tool if this is made clear in the specification by writing in the word EXPLICIT (it is redundant to a computer, but may help a human being). 通常有两种可能的原因：一种是处于隐式标签的环境中，此时选择项上的标签实际上变成了显式的标签。如果规格说明中明确注明这一点，并写上“EXPLICIT”这个词，那么对于不使用工具的人来说会有所帮助。虽然对于计算机来说这有些多余，但对于人类来说或许还是有帮助的。

The other reason is some desire to essentially associate some semantics or categorization with particular tag values, and to ensure that (in BER) there is a length wrapper round the actual type being identified. A similar motivation comes from use of a type constraint on an open-type when PER is used. Both of these (rather obscure) devices appear in some security specifications. 另一个原因是，人们希望为某些标签值赋予一定的语义或分类功能，同时确保在 BER 中，实际被识别的类型周围有一个长度限制。这种动机也出现在使用 PER 时对开放类型进行类型约束的情况中。这两种相当复杂的机制在某些安全规范中都有体现。

Of course, all the above discussion of tagging assumes you have written your type definitions within the defined ASN.1 module framework, not just written it stand-alone! I am sure that readers of this book would never do that! 当然，上述关于标签的讨论都假设了您已经将类型定义写在规定的 ASN.1 模块框架内，而不是单独书写的！我相信本书的读者绝不会这样做！

## 2.10 Keeping it simple 2.10 保持简单

ASN.1 has a number of powerful mechanisms for providing clear specifications, but you will often find people recommending that some of them not be used in the interests of a simpler specification. ASN.1 提供了许多强大的机制来制定清晰的规范，但人们通常会建议为了使规范更加简洁，有些机制可以不用。

![421b6f0fae836f035fed97e6cd76635ed5f08fad7ba68e69f0833455177ab221.jpg](../assets/421b6f0fae836f035fed97e6cd76635ed5f08fad7ba68e69f0833455177ab221.jpg)

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

![38782f259da13cc9987f15f5edd681a6a28f17bf413d7b98c5fd5abd2158e7e5.jpg](../assets/38782f259da13cc9987f15f5edd681a6a28f17bf413d7b98c5fd5abd2158e7e5.jpg)

• Strictly confirm to the specification in what you send. • 请严格遵循所发送产品的规格要求。

• Be forgiving in what you receive. • 在接受事物时，要心怀宽容之心。

That sounds like good advice, and it is often possible to write code that understands and processes things that are strictly invalid. 这听起来像是很好的建议。通常，我们可以编写能够理解并处理那些完全无效情况的代码。

This situation arises more often in Internet protocols than in ASN.1-based protocols, because the use of a text-based format often introduces more redundancy, and hence scope for "understanding" formally incorrect encodings, and because most Internet protocols rely on this principle to provide for interworking between version 1 and version 2 of a specification. The situation will rarely arise with PER, which has almost no redundancy, and an explicit extensions bit! 这种情况在基于互联网的协议中出现得更为频繁，因为在 ASN.1 基础的协议中，文本格式的使用往往会导致更多的冗余，从而增加了理解那些形式上错误的编码的可能性。而大多数互联网协议都采用这种机制来实现规范版本 1 和版本 2 之间的互操作。不过，在 PER 协议中，这种情况很少发生，因为 PER 几乎没有冗余，而且还有明确的扩展位可以用来指示某些特性。

With BER you could decide to be forgiving if you got a universal class 16 tag (SEQUENCE) with the primitive/constructor bit set to "primitive". Or you could be accidentally forbidding by just not bothering to write the code to check that bit once you had detected universal class 16! 使用 BER 机制，你可以选择在检测到通用类 16 标签时予以原谅（如果该标签的“primitive/constructor”位被设置为“primitive”的话）。或者，你也可以选择不编写相应的代码来检查该位，从而避免意外地禁止某些情况的发生。

But if you are forgiving of errors (a primitive sequence, or integers exceeding stated bounds say), you should consider carefully the effect of being forgiving. This issue is very strongly related to extensibility - what you have got is implied extensibility (that you yourself have decided to introduce), and you are on your own to define the best exception handling procedures. 不过，如果你能够原谅这些错误（比如一些原始的错误代码，或者整数超出了规定的范围），那么你就需要仔细考虑这种宽容行为所带来的影响。这个问题与可扩展性密切相关——你所拥有的功能意味着存在可扩展性（即你自己决定引入的这种特性），而如何设计最佳的异常处理机制则完全取决于你自己的判断。

I would recommend that in the case of ASN.1-based protocols it is rarely a good idea to silently ignore and process incorrect encodings which you are able to give meaning to (your own extensions). You may well choose to go on processing, but the error (with details of the sender) should at least be logged somewhere, and if the protocol permits it, sent back to the sender in some form of error message. 我建议，在基于 ASN.1 的协议中，很少有必要对那些可以被解析为有意义的数据进行默默忽略处理。虽然可以选择继续处理这些数据，但错误信息（包括发送者的详细信息）至少应该被记录下来，如果协议允许的话，还应该以某种错误消息的形式返回给发送者。

## 3.2 Know your tool 3.2 了解你的工具

In any development environment there are an immense number of features in the chose tool that can make an implementors life easier. It is important to become familiar with those features/options/parameters of the tool. 在任何开发环境中，都有许多功能可以帮助开发者更轻松地完成工作。因此，熟悉这些工具的功能、选项和参数是非常重要的。

![47e2542608eb01b87aa4c7bb97e0c40fd51e517ba3df6c356279ebe3ad19fd3f.jpg](../assets/47e2542608eb01b87aa4c7bb97e0c40fd51e517ba3df6c356279ebe3ad19fd3f.jpg)

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

![61b5f4ed177844599f539088a7b49bbe1c9e4c13fee4f7a088ef4490c560a32e.jpg](../assets/61b5f4ed177844599f539088a7b49bbe1c9e4c13fee4f7a088ef4490c560a32e.jpg)

The most important advice to implementors - and this is very important - is that if you find things that are not said, raise them as an issue, at least within your team, but preferably with the specifiers themselves through some appropriate mailing list or group. 对实施者来说，最重要的建议就是——这一点非常关键——如果你发现了一些未被提及的问题，一定要把它们提出来讨论，至少是在你的团队内部进行讨论，但如果可能的话，还可以通过适当的邮件列表或小组来与相关的指定人员进行沟通。

Some of you will have heard of the Alternating Bit Protocol. A very similar protocol was specified for use over a particular LAN (no names, no pack drill!) in the late 1970s, but the specification did not say what the behaviour was to be when an ACK with the wrong number was received. The implementors decided that the "right" action was to immediately retransmit the last message (with the same sequence number), trusting the receiver to discard duplicates. Result: parasitic transmissions. Throughput dropped to half until the load backed off, with every packet being transmitted twice! 你们当中有些人可能已经听说过交替位协议。在 20 世纪 70 年代末，有一种类似的协议被提出用于特定局域网中的通信（不会透露具体名称，也不会故意制造困惑！）。不过，该协议并没有明确说明在接收到错误编号的确认消息时该如何处理。实现者们认为，正确的做法应该是立即重新传输最后一条消息（使用相同的序列号），并相信接收方会丢弃重复的数据包。结果就是出现了寄生传输现象。吞吐量下降了一半，直到负载逐渐减轻为止，而每包数据都被重复传输了两次！

If there is one clear duty on implementors, it is not to take their own decisions when specifications are unclear! 如果给实施者设定了一项明确的职责，那就是在规格不明确的情况下不要自行做出决策！

## 3.5 Corrigenda 3.5 修正说明

Implementors need to be as much aware as those in a more managerial capacity of what corrigenda are around, their status, and how they might impact the implementation in the future. 实施人员需要像那些具有管理职责的人一样，了解相关规范的内容、它们的状态，以及这些规范未来可能对实施过程产生的影响。

![ccbc1c2063210d090c3fd5f1ba3200742630e878510afb05b89eb3ad3b7c898d.jpg](../assets/ccbc1c2063210d090c3fd5f1ba3200742630e878510afb05b89eb3ad3b7c898d.jpg)

If you know something is coming, its arrival can be a lot less painful if it has been planned for! 如果你知道某件事情即将发生，那么如果提前做好了准备，它的到来就不会那么令人痛苦了！

## 3.6 Extensibility and exception handling 3.6 可扩展性和异常处理

This text is getting repetitive! If you are told clearly what the bits on the wire should be (and what you do in response to them), and how you are to handle unknown stuff coming in, and if your decoding tool is sufficiently good and flexible, then there are no problems. 这段文字看起来有些重复了！如果能够清楚地知道线路上的各个位应该是什么值（以及面对这些值时该如何处理），同时又能妥善处理可能出现的未知情况，而且你的解码工具足够强大且灵活，那么就不会有问题了。

![b85b814eaa3fb617220c04cf12290d6ad88a2e1912bda46e90c75a1992f9bf74.jpg](../assets/b85b814eaa3fb617220c04cf12290d6ad88a2e1912bda46e90c75a1992f9bf74.jpg)

Otherwise worry! 否则就担心吧！

## 3.7 Care with hand encodings 3.7 对手工编码的注意事项

If, for whatever reason, you do not even have access to a well-debugged library of routines to encode simple types like INTEGER, etc, let alone access to a fully-fledged ASN.1 compiler, then you deserve sympathy! 如果由于某种原因，你甚至无法使用那些已经经过充分调试的库函数来编码简单的类型，比如 INTEGER 等，更不用说使用功能齐全的 ASN.1 编译器了，那么你确实值得同情！

![d04a2e8fbf3c22707876f683ecf925cc65c62a1ecaacc651326b88b517dbd67e.jpg](../assets/d04a2e8fbf3c22707876f683ecf925cc65c62a1ecaacc651326b88b517dbd67e.jpg)

Producing ASN.1 encodings from scratch, by hand, is not impossible, and in one sense, not even difficult. (But it is probably easier to get it right first time with BER than with PER, unfortunately, due to the large number of optimisations in PER.) It is just time-consuming and error prone. 从头开始手动生成 ASN.1 编码并非不可能，某种程度上来说也不算困难。不过，遗憾的是，使用 BER 方法首次就正确地生成编码要比使用 PER 方法容易得多，因为 PER 方法包含了大量的优化措施。不过，这样做会耗费大量时间，并且容易出错。

First of all, you need to read Section III rather more carefully than you otherwise would! Then you need to spend a lot of time with the actual ASN.1 encoding specification that you are going to be using. 首先，你必须比平时更仔细地阅读第三部分的内容！此外，你还需要花费大量时间研究实际的 ASN.1 编码规范，因为这些规范正是你将要使用的标准。

Second, you will need some sort of ad hoc "line monitor" tool to display what you are producing in a format that will make it easy for you to check that you are producing what you intended. 其次，你需要一种临时的“生产线监控”工具，能够以易于查看的格式显示你的生产成果，这样就能轻松确认你是否按照预期进行了生产。

And lastly, you really need an ASN.1 tool! Not one that necessarily runs on your platform (lack of that is presumably why you are not using a tool), but one that can run on some other communicating platform, take your output, and display the values it thinks you are transmitting. 最后，你真的需要一款 ASN.1 工具！这个工具不一定必须运行在你的平台上（可能正是因为缺乏这样的条件，你才没有使用工具），但它应该能够在其他通信平台上运行。该工具可以接收你的输出结果，然后显示它认为你正在传输的值。

Well, that was almost last! There is nothing like final inter-operability testing with a totally different complete implementation, particularly if it (and you!) have good error logging of things you think are erroneous about what you are receiving. 嗯，差不多就到最后阶段了！现在需要进行最终的互操作性测试，会使用完全不同的实现方式来进行测试。当然，前提是你们能够很好地记录那些看似错误的操作，以及系统所遇到的各种错误。

## 3.8 Mailing lists 3.8 邮件列表

There is a mailing list you can use for general ASN.1 enquiries (see Appendix 5 for a link to this), and many protocol specifications today are supported by mailing lists, news groups, Web pages, etc. 有一个邮件列表可用于处理一般的 ASN 相关查询（链接见附录 5）。如今，许多协议规范都是通过邮件列表、新闻组、网页等方式来进行维护和交流的。

![f48a711f97177a04632989edc9980b8ab779bc9146c7e29b659967ec2af87b1c.jpg](../assets/f48a711f97177a04632989edc9980b8ab779bc9146c7e29b659967ec2af87b1c.jpg)

These resources can be very valuable to you. (As can people that give ASN.1 and specificprotocol courses, who are usually willing to leave their e-mail addresses with you and to answer queries subsequent to their courses. 这些资源对您来说可能非常有价值。（同样，那些提供 ASN.1 和特定协议课程的人也很有帮助，他们通常愿意留下自己的电子邮件地址，并在课程结束后回答您的疑问。）

## 3.9 Good engineering - version 2 **will** come! 3.9 工程性能良好——版本 2 即将推出！

Any protocol you implement will have a version 2 specification that you or your descendants (team-wise) will have to implement. 你所实现的任何协议都會有一份版本 2 的规范，你或你的后代们（以团队形式）都必须遵守这份规范。

![b03d49b904cc5b522714645b625d32c1603ab7a04e562804a6fbeef0322bd28d.jpg](../assets/b03d49b904cc5b522714645b625d32c1603ab7a04e562804a6fbeef0322bd28d.jpg)

All the usual good engineering principles apply to make sure that your code and documentation enables others to modify your implementation to support the version 2 specification as and when this is produced. 所有常见的优秀工程原则都适用于确保你的代码和文档能够让人们随时修改你的实现，以符合 2 版规范的要求。随着 2 版规范的发布，这些修改将变得十分容易。

You will get some hints in the extensibility provisions of version 1 of what areas the specifiers expect to change. This can help you to engineer the structure of your implementation to be easily able to accommodate those changes when they arrive. 在版本 1 的可扩展性条款中，你会找到一些提示，说明这些规范定义者希望改变哪些部分。这些提示可以帮助你设计实现结构，以便能够在这些变更发生时轻松应对。

Just as getting exception handling as right as possible is a challenge for specifiers, getting an implementation architecture that enables extensions to be easily handled (and providing correct exception handling in version 1 when there are as yet no version 2 systems around to test against) is the challenge for the implementor. As for specifiers - this is part of your job, get it right! 对于规范编写者来说，尽可能实现完善的异常处理机制确实是一个挑战；而对于实现者而言，则面临着如何构建一种能够轻松处理扩展功能的实现架构的挑战（同时，在还没有版本 2 的系统可供测试的情况下，还需要在版本 1 中提供正确的异常处理机制）。至于规范编写者——这确实是你们的工作职责之一，一定要把事情做好！

## 4 Conclusion 4. 结论

And that completes this first Section of the book. Many of you will be leaving us at this point (although you may find some parts of Section IV interesting). I hope you have found it useful. The more technically-minded will no doubt be proceeding to Sections II and III – read on! 至此，本书的第一部分内容已经讲完了。你们中的许多人现在会离开这里（不过，第四部分的某些内容或许还是值得你们继续阅读的）。希望这些内容对你们有所帮助。那些对技术方面比较感兴趣的人，想必会继续阅读第二部分和第三部分的内容吧——请继续阅读下去吧！