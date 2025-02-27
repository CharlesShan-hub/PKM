# 简介

> 本文按照YAML官方文档1.2.2版本翻译总结而成
>
> https://yaml.org/spec/1.2.2/#chapter-1-introduction-to-yaml

*YAML (a recursive acronym for “YAML Ain’t Markup Language”) is a data serialization language designed to be human-friendly and work well with modern programming languages for common everyday tasks. This specification is both an introduction to the YAML language and the concepts supporting it. It is also a complete specification of the information needed to develop [applications](https://yaml.org/spec/1.2.2/#processes-and-models) for processing YAML.*

* YAML缩写自YAML Ain’t Markup Language，是一种数据序列化语言。

* 它被设计成对人类友好的，并且可以与现代编程语言很好地处理常见的日常任务。

*Open, interoperable and readily understandable tools have advanced computing immensely. YAML was designed from the start to be useful and friendly to people working with data. It uses Unicode [printable](https://yaml.org/spec/1.2.2/#character-set) characters, [some](https://yaml.org/spec/1.2.2/#indicator-characters) of which provide structural information and the rest containing the data itself. YAML achieves a unique cleanness by minimizing the amount of structural characters and allowing the data to show itself in a natural and meaningful way. For example, [indentation](https://yaml.org/spec/1.2.2/#indentation-spaces) may be used for structure, [colons](https://yaml.org/spec/1.2.2/#flow-mappings) separate [key/value pairs](https://yaml.org/spec/1.2.2/#mapping) and [dashes](https://yaml.org/spec/1.2.2/#block-sequences) are used to create “bulleted” [lists](https://yaml.org/spec/1.2.2/#sequence).*

* YAML使用Unicode中的[可打印字符](https://yaml.org/spec/1.2.2/#character-set)，其中[一部分](https://yaml.org/spec/1.2.2/#indicator-characters)提供结构信息，其余包含数据本身。
* YAML通过最小化结构字符的数量，从而实现整洁性与自然性。例如，[缩紧](https://yaml.org/spec/1.2.2/#indentation-spaces)可以用于结构，[冒号](https://yaml.org/spec/1.2.2/#flow-mappings)分隔[键/值对](https://yaml.org/spec/1.2.2/#mapping)和[破折号](https://yaml.org/spec/1.2.2/#block-sequences)用于创建"项目符号"[列表](https://yaml.org/spec/1.2.2/#sequence)。

*There are many kinds of [data structures](https://yaml.org/spec/1.2.2/#dump), but they can all be adequately [represented](https://yaml.org/spec/1.2.2/#representation-graph) with three basic primitives: [mappings](https://yaml.org/spec/1.2.2/#mapping) (hashes/dictionaries), [sequences](https://yaml.org/spec/1.2.2/#sequence) (arrays/lists) and [scalars](https://yaml.org/spec/1.2.2/#scalars) (strings/numbers). YAML leverages these primitives and adds a simple typing system and [aliasing](https://yaml.org/spec/1.2.2/#anchors-and-aliases) mechanism to form a complete language for [serializing](https://yaml.org/spec/1.2.2/#serializing-the-representation-graph) any [native data structure](https://yaml.org/spec/1.2.2/#representing-native-data-structures). While most programming languages can use YAML for data serialization, YAML excels in working with those languages that are fundamentally built around the three basic primitives. These include common dynamic languages such as JavaScript, Perl, PHP, Python and Ruby.*

*There are hundreds of different languages for programming, but only a handful of languages for storing and transferring data. Even though its potential is virtually boundless, YAML was specifically created to work well for common use cases such as: configuration files, log files, interprocess messaging, cross-language data sharing, object persistence and debugging of complex data structures. When data is easy to view and understand, programming becomes a simpler task.*

* 可通过三种基本的原语，[mappings](https://yaml.org/spec/1.2.2/#mapping)(哈希值/字典)，[sequence](https://yaml.org/spec/1.2.2/#sequence)(数组/列表)和[scalars](https://yaml.org/spec/1.2.2/#scalars)(字符串/数字)，[表示](https://yaml.org/spec/1.2.2/#representation-graph)许多种[数据结构](https://yaml.org/spec/1.2.2/#dump)。
* YAML利用了这些原语，并添加了一个简单的类型系统和[别名](https://yaml.org/spec/1.2.2/#anchors-and-aliases)机制，以形成一个完整的语言，用于[序列化](https://yaml.org/spec/1.2.2/#serializing-the-representation-graph)任何[原生数据结构](https://yaml.org/spec/1.2.2/#representing-native-data-structures)。
* 虽然大多数编程语言都可以使用YAML进行数据序列化，但YAML擅长处理那些基本上围绕三个基本原语构建的语言。这些语言包括常见的动态语言，如JavaScript、Perl、PHP、Python和Ruby。
* YAML常见功能举例：配置文件、日志文件、进程间消息传递、跨语言数据共享、对象持久性和复杂数据结构的调试。

## 1.1. Goals

*The design goals for YAML are, in decreasing priority:*

1. 易读性。*YAML should be easily readable by humans.*
2. 可移植性。*YAML data should be portable between programming languages.*
3. 可匹配动态语言的[原生数据结构](https://yaml.org/spec/1.2.2/#representing-native-data-structures)。*YAML should match the [native data structures](https://yaml.org/spec/1.2.2/#representing-native-data-structures) of dynamic languages.*
4. 通用工具。*YAML should have a consistent model to support generic tools.*
5. 一次处理。*YAML should support one-pass processing.*
6. 可扩展性。*YAML should be expressive and extensible.*
7. 实用性。*YAML should be easy to implement and use.*

## 1.2. YAML History

*The YAML 1.0 specification was published in early 2004 by by Clark Evans, Oren Ben-Kiki, and Ingy döt Net after 3 years of collaborative design work through the yaml-core mailing list[5](https://yaml.org/spec/1.2.2/#fn:yaml-core). The project was initially rooted in Clark and Oren’s work on the SML-DEV[6](https://yaml.org/spec/1.2.2/#fn:sml-dev) mailing list (for simplifying XML) and Ingy’s plain text serialization module[7](https://yaml.org/spec/1.2.2/#fn:denter) for Perl. The language took a lot of inspiration from many other technologies and formats that preceded it.*

YAML 1.0 规范由 Clark Evans、Oren Ben-Kiki 和 Ingy döt Net 于 2004 年初通过 yaml-core 邮件列表[5](https://yaml.org/spec/1.2.2/#fn:yaml-core) 进行了 3 年的协作设计工作后发布。该项目最初植根于 Clark 和 Oren 在 SML-DEV[6](https://yaml.org/spec/1.2.2/#fn:sml-dev) 邮件列表（用于简化 XML）和 Ingy 的 Perl 纯文本序列化模块[7](https://yaml.org/spec/1.2.2/#fn:denter) 上的工作。该语言从之前的许多其他技术和格式中汲取了很多灵感。

*The first YAML framework was written in Perl in 2001 and Ruby was the first language to ship a YAML framework as part of its core language distribution in 2003.*

第一个 YAML 框架是在 2001 年用 Perl 编写的，Ruby 是第一个在 2003 年将 YAML 框架作为其核心语言发行版的一部分发布的语言。

*The YAML 1.1[8](https://yaml.org/spec/1.2.2/#fn:1-1-spec) specification was published in 2005. Around this time, the developers became aware of JSON[9](https://yaml.org/spec/1.2.2/#fn:json). By sheer coincidence, JSON was almost a complete subset of YAML (both syntactically and semantically).*

YAML 1.1[8](https://yaml.org/spec/1.2.2/#fn:1-1-spec) 规范于 2005 年发布。大约在这个时候，开发人员开始注意到 JSON[9](https://yaml.org/spec/1.2.2/#fn:json)。纯属巧合，JSON 几乎是 YAML 的一个完整子集（在语法和语义上）。

*In 2006, Kyrylo Simonov produced PyYAML[10](https://yaml.org/spec/1.2.2/#fn:pyyaml) and LibYAML[11](https://yaml.org/spec/1.2.2/#fn:libyaml). A lot of the YAML frameworks in various programming languages are built over LibYAML and many others have looked to PyYAML as a solid reference for their implementations.*

2006 年，Kyrylo Simonov 开发了 PyYAML[10](https://yaml.org/spec/1.2.2/#fn:pyyaml) 和 LibYAML[11](https://yaml.org/spec/1.2.2/#fn:libyaml)。各种编程语言中的许多 YAML 框架都是基于 LibYAML 构建的，许多其他框架将 PyYAML 视为其实现的可靠参考。

*The YAML 1.2[3](https://yaml.org/spec/1.2.2/#fn:1-2-spec) specification was published in 2009. Its primary focus was making YAML a strict superset of JSON. It also removed many of the problematic implicit typing recommendations.*

YAML 1.2[3](https://yaml.org/spec/1.2.2/#fn:1-2-spec) 规范于 2009 年发布。它的主要重点是使 YAML 成为 JSON 的严格超集。它还删除了许多有问题的隐式类型化建议。

*Since the release of the 1.2 specification, YAML adoption has continued to grow, and many large-scale projects use it as their primary interface language. In 2020, the new [YAML language design team](https://yaml.org/spec/1.2.2/ext/team) began meeting regularly to discuss improvements to the YAML language and specification; to better meet the needs and expectations of its users and use cases.*

自 1.2 规范发布以来，YAML 的采用率持续增长，许多大型项目将其用作主要接口语言。2020 年，新的 [YAML 语言设计团队](https://yaml.org/spec/1.2.2/ext/team)开始定期开会，讨论对 YAML 语言和规范的改进;以更好地满足其用户和使用案例的需求和期望。

*This YAML 1.2.2 specification, published in October 2021, is the first step in YAML’s rejuvenated development journey. YAML is now more popular than it has ever been, but there is a long list of things that need to be addressed for it to reach its full potential. The YAML design team is focused on making YAML as good as possible.*

此 YAML 1.2.2 规范于 2021 年 10 月发布，是 YAML 焕然一新的开发之旅的第一步。YAML 现在比以往任何时候都更受欢迎，但要充分发挥其潜力，需要解决的问题有很多问题需要解决。YAML 设计团队专注于使 YAML 尽可能好。

## 1.3. Terminology

*The key words “MUST”, “MUST NOT”, “REQUIRED”, “SHALL”, “SHALL NOT”, “SHOULD”, “SHOULD NOT”, “RECOMMENDED”, “MAY”, and “OPTIONAL” in this document are to be interpreted as described in RFC 2119[12](https://yaml.org/spec/1.2.2/#fn:rfc-2119).*

本文档中的关键词“必须”、“不得”、“必需”、“应”、“不应”、“应该”、“不应”、“推荐”、“可以”和“可选”应按照 RFC 2119[12](https://yaml.org/spec/1.2.2/#fn:rfc-2119) 中的描述进行解释。

*The rest of this document is arranged as follows. Chapter [2](https://yaml.org/spec/1.2.2/#language-overview) provides a short preview of the main YAML features. Chapter [3](https://yaml.org/spec/1.2.2/#processes-and-models) describes the YAML information model and the processes for converting from and to this model and the YAML text format. The bulk of the document, chapters [4](https://yaml.org/spec/1.2.2/#syntax-conventions), [5](https://yaml.org/spec/1.2.2/#character-productions), [6](https://yaml.org/spec/1.2.2/#structural-productions), [7](https://yaml.org/spec/1.2.2/#flow-style-productions), [8](https://yaml.org/spec/1.2.2/#block-style-productions) and [9](https://yaml.org/spec/1.2.2/#document-stream-productions), formally define this text format. Finally, chapter [10](https://yaml.org/spec/1.2.2/#recommended-schemas) recommends basic YAML schemas.*

* 本文档的其余部分安排如下。
  * 第[2](https://yaml.org/spec/1.2.2/#language-overview)章提供了YAML主要特性的简短预览。
  * 第[3](https://yaml.org/spec/1.2.2/#processes-and-models)章描述了YAML信息模型以及从该模型和YAML文本格式转换到该模型的过程。
  * 文档的大部分章节[4](https://yaml.org/spec/1.2.2/#syntax-conventions)、[5](https://yaml.org/spec/1.2.2/#character-productions)、[6](https://yaml.org/spec/1.2.2/#structural-productions)、[7](https://yaml.org/spec/1.2.2/#flow-style-productions)、[8](https://yaml.org/spec/1.2.2/#block-style-productions)和[9](https://yaml.org/spec/1.2.2/#document-stream-productions)正式定义了这种文本格式。
  * 第[10](https://yaml.org/spec/1.2.2/#recommended-schemas)章推荐了基本的YAML模式。