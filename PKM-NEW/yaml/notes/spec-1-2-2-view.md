# 模型

> 本文按照YAML官方文档1.2.2版本翻译总结而成
>
> https://yaml.org/spec/1.2.2/#chapter-3-processes-and-models

YAML is both a text format and a method for [presenting](https://yaml.org/spec/1.2.2/#presenting-the-serialization-tree) any [native data structure](https://yaml.org/spec/1.2.2/#representing-native-data-structures) in this format. Therefore, this specification defines two concepts: a class of data objects called YAML [representations](https://yaml.org/spec/1.2.2/#representation-graph) and a syntax for [presenting](https://yaml.org/spec/1.2.2/#presenting-the-serialization-tree) YAML [representations](https://yaml.org/spec/1.2.2/#representation-graph) as a series of characters, called a YAML [stream](https://yaml.org/spec/1.2.2/#streams).

YAML 既是一种文本格式，也是一种以这种格式呈现任何本机数据结构的方法。因此，本规范定义了两个概念
* YAML 表示的数据对象。
* YAML 流：将 YAML 表示呈现为一系列字符的语法。

A YAML *processor* is a tool for converting information between these complementary views. It is assumed that a YAML processor does its work on behalf of another module, called an *application*. This chapter describes the information structures a YAML processor must provide to or obtain from the application.

YAML 处理器是一种在这些互补视图之间转换信息的工具。假设 YAML 处理器代表另一个模块（称为应用程序）工作。本章介绍 YAML 处理器必须向应用程序提供或从应用程序获取的信息结构。

YAML information is used in two ways: for machine processing and for human consumption. The challenge of reconciling these two perspectives is best done in three distinct translation stages: [representation](https://yaml.org/spec/1.2.2/#representation-graph), [serialization](https://yaml.org/spec/1.2.2/#serialization-tree) and [presentation](https://yaml.org/spec/1.2.2/#presentation-stream). [Representation](https://yaml.org/spec/1.2.2/#representation-graph) addresses how YAML views [native data structures](https://yaml.org/spec/1.2.2/#representing-native-data-structures) to achieve portability between programming environments. [Serialization](https://yaml.org/spec/1.2.2/#serialization-tree) concerns itself with turning a YAML [representation](https://yaml.org/spec/1.2.2/#representation-graph) into a serial form, that is, a form with sequential access constraints. [Presentation](https://yaml.org/spec/1.2.2/#presentation-stream) deals with the formatting of a YAML [serialization](https://yaml.org/spec/1.2.2/#serialization-tree) as a series of characters in a human-friendly manner.

YAML 信息有两种用途：用于机器处理和供人类使用。协调这两个观点的挑战最好在三个不同的转换阶段完成：表示、序列化和表示。
* Representation：YAML 如何查看本机数据结构以实现编程环境之间的可移植性。
* Serialization：涉及将 YAML 表示转换为串行形式，即具有顺序访问约束的形式。
* Presentation：涉及以人性化的方式将 YAML 序列化格式化为一系列字符。

## 3.1. Processes

Translating between [native data structures](https://yaml.org/spec/1.2.2/#representing-native-data-structures) and a character [stream](https://yaml.org/spec/1.2.2/#streams) is done in several logically distinct stages, each with a well defined input and output data model, as shown in the following diagram:

[原生数据结构](https://yaml.org/spec/1.2.2/#representing-native-data-structures)和字符[流](https://yaml.org/spec/1.2.2/#streams)之间的转换在几个逻辑上不同的阶段中完成，每个阶段都有定义明确的输入和输出数据模型


**Figure 3.1. Processing Overview**

![Processing Overview](https://yaml.org/spec/1.2.2/img/overview2.svg)

A YAML processor need not expose the [serialization](https://yaml.org/spec/1.2.2/#serialization-tree) or [representation](https://yaml.org/spec/1.2.2/#representation-graph) stages. It may translate directly between [native data structures](https://yaml.org/spec/1.2.2/#representing-native-data-structures) and a character [stream](https://yaml.org/spec/1.2.2/#streams) ([dump](https://yaml.org/spec/1.2.2/#dump) and [load](https://yaml.org/spec/1.2.2/#load) in the diagram above). However, such a direct translation should take place so that the [native data structures](https://yaml.org/spec/1.2.2/#representing-native-data-structures) are [constructed](https://yaml.org/spec/1.2.2/#constructing-native-data-structures) only from information available in the [representation](https://yaml.org/spec/1.2.2/#representation-graph). In particular, [mapping key order](https://yaml.org/spec/1.2.2/#mapping), [comments](https://yaml.org/spec/1.2.2/#comments) and [tag handles](https://yaml.org/spec/1.2.2/#tag-handles) should not be referenced during [construction](https://yaml.org/spec/1.2.2/#constructing-native-data-structures).

YAML处理器无需展示序列化或表示阶段的过程。它可以直接在本地数据结构与字符流之间进行转换（如图中的dump和load过程）。这种转换应确保本地数据结构仅根据表示中提供的信息来构建。特别是，在构建过程中不应考虑映射键的顺序、注释以及标签处理程序等因素。

### 3.1.1. Dump

*Dumping* native data structures to a character [stream](https://yaml.org/spec/1.2.2/#streams) is done using the following three stages:

将本机数据结构转储到字符流使用以下三个阶段完成：

- Representing Native Data Structures

  YAML *represents* any *native data structure* using three [node kinds](https://yaml.org/spec/1.2.2/#nodes): [sequence](https://yaml.org/spec/1.2.2/#sequence) - an ordered series of entries; [mapping](https://yaml.org/spec/1.2.2/#mapping) - an unordered association of [unique](https://yaml.org/spec/1.2.2/#node-comparison) [keys](https://yaml.org/spec/1.2.2/#nodes) to [values](https://yaml.org/spec/1.2.2/#nodes); and [scalar](https://yaml.org/spec/1.2.2/#scalar) - any datum with opaque structure presentable as a series of Unicode characters.
  
  YAML 使用三种[节点类型](https://yaml.org/spec/1.2.2/#nodes)表示任何本机数据结构： 
  * [sequence](https://yaml.org/spec/1.2.2/#sequence) - 一系列有序的条目;
		```yaml
		product:
	   - sku         : BL394D
	     quantity    : 4
	     description : Football
	     price       : 450.00
	   - sku         : BL4438H
	     quantity    : 1
	     description : Super Hoop
	     price       : 2392.00
		```
  * [mapping](https://yaml.org/spec/1.2.2/#mapping) - [唯一](https://yaml.org/spec/1.2.2/#node-comparison)[键](https://yaml.org/spec/1.2.2/#nodes)与[值](https://yaml.org/spec/1.2.2/#nodes)的无序关联;
		```yaml
		batchLimit: 1000
		threadCountLimit: 2
		key: value
		keyMapping: <What goes here?>
		```
  * [scalar](https://yaml.org/spec/1.2.2/#scalar) - 任何具有不透明结构的数据，可表示为一系列 Unicode 字符。

  Combined, these primitives generate directed graph structures. These primitives were chosen because they are both powerful and familiar: the [sequence](https://yaml.org/spec/1.2.2/#sequence) corresponds to a Perl array and a Python list, the [mapping](https://yaml.org/spec/1.2.2/#mapping) corresponds to a Perl hash table and a Python dictionary. The [scalar](https://yaml.org/spec/1.2.2/#scalar) represents strings, integers, dates and other atomic data types.
  
  这些基元组合在一起，生成有向图形结构。 选择这些原语是因为它们既强大又熟悉： [sequence](https://yaml.org/spec/1.2.2/#sequence) 对应一个 Perl 数组和一个 Python 列表，[mapping](https://yaml.org/spec/1.2.2/#mapping) 对应一个 Perl 哈希表和一个 Python 字典。 [scalar](https://yaml.org/spec/1.2.2/#scalar)表示字符串、整数、日期和其他原子数据类型。

  ```yaml
	# 这是一个使用全局标签的整数标量，它告诉 YAML 解析器 `42` 是一个整数。
	number: !!int 42
	
	# `!invoice` 和 `!item` 是局部标签，它们用于定义一个特定于应用程序的数据结构。在这个例子中，`!invoice` 表示一个发票对象，而 `!item` 表示发票中的一个项目。
	!invoice
	  id: 12345
	  date: 2023-04-01
	  items:
	    - !item
	      product: "Widget"
	      quantity: 1
	      price: !!float 19.99
	
	```

	Each YAML [node](https://yaml.org/spec/1.2.2/#nodes) requires, in addition to its [kind](https://yaml.org/spec/1.2.2/#nodes) and [content](https://yaml.org/spec/1.2.2/#nodes), a [tag](https://yaml.org/spec/1.2.2/#tags) specifying its data type. Type specifiers are either [global](https://yaml.org/spec/1.2.2/#tags) URIs or are [local](https://yaml.org/spec/1.2.2/#tags) in scope to a single [application](https://yaml.org/spec/1.2.2/#processes-and-models). For example, an integer is represented in YAML with a [scalar](https://yaml.org/spec/1.2.2/#scalar) plus the [global tag](https://yaml.org/spec/1.2.2/#tags) “`tag:yaml.org,2002:int`”. Similarly, an invoice object, particular to a given organization, could be represented as a [mapping](https://yaml.org/spec/1.2.2/#mapping) together with the [local tag](https://yaml.org/spec/1.2.2/#tags) “`!invoice`”. This simple model can represent any data structure independent of programming language.
	
	每个YAML节点除了需要知道其类型和内容外，还需要一个标签来指明其数据类型。这些类型标签要么是全局统一资源标识符（URI），要么是仅限于特定应用程序的本地标签。例如，在YAML中，整数是通过一个标量值加上全局标签“tag:yaml.org,2002:int”来表示的。同样，特定于某个组织的发票对象可以表示为一个映射，并加上本地标签“!invoice”。这种简单的模型能够描述任何与编程语言无关的数据结构。
	
- Serializing the Representation Graph

  For sequential access mediums, such as an event callback API, a YAML [representation](https://yaml.org/spec/1.2.2/#representation-graph) must be *serialized* to an ordered tree. Since in a YAML [representation](https://yaml.org/spec/1.2.2/#representation-graph), [mapping keys](https://yaml.org/spec/1.2.2/#nodes) are unordered and [nodes](https://yaml.org/spec/1.2.2/#nodes) may be referenced more than once (have more than one incoming “arrow”), the serialization process is required to impose an [ordering](https://yaml.org/spec/1.2.2/#mapping-key-order) on the [mapping keys](https://yaml.org/spec/1.2.2/#nodes) and to replace the second and subsequent references to a given [node](https://yaml.org/spec/1.2.2/#nodes) with place holders called [aliases](https://yaml.org/spec/1.2.2/#anchors-and-aliases). YAML does not specify how these *serialization details* are chosen. It is up to the YAML [processor](https://yaml.org/spec/1.2.2/#processes-and-models) to come up with human-friendly [key order](https://yaml.org/spec/1.2.2/#mapping-key-order) and [anchor](https://yaml.org/spec/1.2.2/#anchors-and-aliases) names, possibly with the help of the [application](https://yaml.org/spec/1.2.2/#processes-and-models). The result of this process, a YAML [serialization tree](https://yaml.org/spec/1.2.2/#serialization-tree), can then be traversed to produce a series of event calls for one-pass processing of YAML data.
  
  在顺序访问的介质中，例如事件回调API，需要将YAML的数据表示转换为一个有序的树结构。由于在YAML的数据表示中，映射的键是无序的，且节点可能被多次引用，因此在序列化过程中需要确定映射键的顺序，并将对同一节点的多次引用转换为称为别名的占位符。YAML标准并没有规定如何选择这些序列化细节，这取决于YAML处理器来决定一个直观的键顺序和锚点名称，可能还需要应用程序的协助。这个过程的结果是一个YAML序列化树，它可以通过遍历产生一系列事件调用，从而实现一次性处理YAML数据。

- Presenting the Serialization Tree

  The final output process is *presenting* the YAML [serializations](https://yaml.org/spec/1.2.2/#serialization-tree) as a character [stream](https://yaml.org/spec/1.2.2/#streams) in a human-friendly manner. To maximize human readability, YAML offers a rich set of stylistic options which go far beyond the minimal functional needs of simple data storage. Therefore the YAML [processor](https://yaml.org/spec/1.2.2/#processes-and-models) is required to introduce various *presentation details* when creating the [stream](https://yaml.org/spec/1.2.2/#streams), such as the choice of [node styles](https://yaml.org/spec/1.2.2/#node-styles), how to [format scalar content](https://yaml.org/spec/1.2.2/#scalar-formats), the amount of [indentation](https://yaml.org/spec/1.2.2/#indentation-spaces), which [tag handles](https://yaml.org/spec/1.2.2/#tag-handles) to use, the [node tags](https://yaml.org/spec/1.2.2/#node-tags) to leave [unspecified](https://yaml.org/spec/1.2.2/#resolved-tags), the set of [directives](https://yaml.org/spec/1.2.2/#directives) to provide and possibly even what [comments](https://yaml.org/spec/1.2.2/#comments) to add. While some of this can be done with the help of the [application](https://yaml.org/spec/1.2.2/#processes-and-models), in general this process should be guided by the preferences of the user.
  
  YAML的最终输出过程是将YAML的序列化数据以人类友好的方式转换为字符流输出。为了提高可读性，YAML提供了多种样式选择，这些选择不仅满足了简单数据存储的基本功能，还提供了更多的灵活性。因此，在创建字符流时，YAML处理器需要考虑各种输出细节，如选择节点样式、标量内容的格式化方式、缩进大小、使用的标签句柄、保留未指定的节点标签、提供的指令，甚至包括添加的注释。虽然一些细节可以通过应用程序来辅助完成，但总体上，这个过程应该根据用户的需求和喜好来调整。

### 3.1.2. Load

*Loading* [native data structures](https://yaml.org/spec/1.2.2/#representing-native-data-structures) from a character [stream](https://yaml.org/spec/1.2.2/#streams) is done using the following three stages:

- Parsing the Presentation Stream

  *Parsing* is the inverse process of [presentation](https://yaml.org/spec/1.2.2/#presentation-stream), it takes a [stream](https://yaml.org/spec/1.2.2/#streams) of characters and produces a [serialization tree](https://yaml.org/spec/1.2.2/#serialization-tree). Parsing discards all the [details](https://yaml.org/spec/1.2.2/#presenting-the-serialization-tree) introduced in the [presentation](https://yaml.org/spec/1.2.2/#presentation-stream) process, reporting only the [serialization tree](https://yaml.org/spec/1.2.2/#serialization-tree). Parsing can fail due to [ill-formed](https://yaml.org/spec/1.2.2/#well-formed-streams-and-identified-aliases) input.
  
  解析是呈现过程的逆过程，它将字符流转换为序列化树。在解析过程中，会忽略呈现时添加的所有格式细节，只保留序列化树的结构。如果输入的字符流格式不正确，解析过程可能会失败。

- Composing the Representation Graph

  *Composing* takes a [serialization tree](https://yaml.org/spec/1.2.2/#serialization-tree) and produces a [representation graph](https://yaml.org/spec/1.2.2/#representation-graph). Composing discards all the [details](https://yaml.org/spec/1.2.2/#presenting-the-serialization-tree) introduced in the [serialization](https://yaml.org/spec/1.2.2/#serialization-tree) process, producing only the [representation graph](https://yaml.org/spec/1.2.2/#representation-graph). Composing can fail due to any of several reasons, detailed [below](https://yaml.org/spec/1.2.2/#loading-failure-points).
  
  组合过程是将序列化树转换成代表图。在这个过程中，会忽略序列化时添加的所有格式细节，只保留代表图的结构。组合可能会因为多种原因失败，具体原因将在下面详细讨论。

- Constructing Native Data Structures

  The final input process is *constructing* [native data structures](https://yaml.org/spec/1.2.2/#representing-native-data-structures) from the YAML [representation](https://yaml.org/spec/1.2.2/#representation-graph). Construction must be based only on the information available in the [representation](https://yaml.org/spec/1.2.2/#representation-graph) and not on additional [serialization](https://yaml.org/spec/1.2.2/#serialization-tree) or [presentation details](https://yaml.org/spec/1.2.2/#presenting-the-serialization-tree) such as [comments](https://yaml.org/spec/1.2.2/#comments), [directives](https://yaml.org/spec/1.2.2/#directives), [mapping key order](https://yaml.org/spec/1.2.2/#mapping), [node styles](https://yaml.org/spec/1.2.2/#node-styles), [scalar content format](https://yaml.org/spec/1.2.2/#scalar-formats), [indentation](https://yaml.org/spec/1.2.2/#indentation-spaces) levels etc. Construction can fail due to the [unavailability](https://yaml.org/spec/1.2.2/#available-tags) of the required [native data types](https://yaml.org/spec/1.2.2/#representing-native-data-structures).
  
  最后的输入过程是从YAML的表示中创建本地数据结构。这一过程应仅依赖于表示中的信息，而不应考虑序列化或呈现时的额外信息，如注释、指令、映射键的排序、节点样式、标量内容的格式、缩进层次等。如果所需的本地数据类型不可用，构建过程可能会失败。

## 3.2. Information Models

This section specifies the formal details of the results of the above processes. To maximize data portability between programming languages and implementations, users of YAML should be mindful of the distinction between [serialization](https://yaml.org/spec/1.2.2/#serialization-tree) or [presentation](https://yaml.org/spec/1.2.2/#presentation-stream) properties and those which are part of the YAML [representation](https://yaml.org/spec/1.2.2/#representation-graph). Thus, while imposing a [order](https://yaml.org/spec/1.2.2/#mapping-key-order) on [mapping keys](https://yaml.org/spec/1.2.2/#nodes) is necessary for flattening YAML [representations](https://yaml.org/spec/1.2.2/#representation-graph) to a sequential access medium, this [serialization detail](https://yaml.org/spec/1.2.2/#serializing-the-representation-graph) must not be used to convey [application](https://yaml.org/spec/1.2.2/#processes-and-models) level information. In a similar manner, while [indentation](https://yaml.org/spec/1.2.2/#indentation-spaces) technique and a choice of a [node style](https://yaml.org/spec/1.2.2/#node-styles) are needed for the human readability, these [presentation details](https://yaml.org/spec/1.2.2/#presenting-the-serialization-tree) are neither part of the YAML [serialization](https://yaml.org/spec/1.2.2/#serialization-tree) nor the YAML [representation](https://yaml.org/spec/1.2.2/#representation-graph). By carefully separating properties needed for [serialization](https://yaml.org/spec/1.2.2/#serialization-tree) and [presentation](https://yaml.org/spec/1.2.2/#presentation-stream), YAML [representations](https://yaml.org/spec/1.2.2/#representation-graph) of [application](https://yaml.org/spec/1.2.2/#processes-and-models) information will be consistent and portable between various programming environments.

本节详细规定了上述流程的结果。为了提高YAML在不同编程语言和环境间的数据可移植性，用户应区分开序列化和展示属性与YAML表示本身的部分。例如，在将YAML表示转换为顺序访问格式时，虽然需要确定映射键的顺序，但这部分序列化细节不应用于传递应用级别的信息。同样，虽然为了易读性需要选择缩进方式和节点样式，但这些展示细节并不属于YAML的序列化或表示。通过清晰地区分序列化和展示所需的属性，YAML表示的应用信息能在不同的编程环境中保持一致和可移植。

The following diagram summarizes the three *information models*. Full arrows denote composition, hollow arrows denote inheritance, “`1`” and “`*`” denote “one” and “many” relationships. A single “`+`” denotes [serialization](https://yaml.org/spec/1.2.2/#serialization-tree) details, a double “`++`” denotes [presentation](https://yaml.org/spec/1.2.2/#presentation-stream) details.

在下图中，三个信息模型被总结。实箭头表示组合关系，空心箭头表示继承关系，`1`和`*`分别代表“一个”和“多个”的关系。单个`+`表示序列化细节，而双`++`表示展示细节。

**Figure 3.2. Information Models**

![Information Models](https://yaml.org/spec/1.2.2/img/model2.svg)

### 3.2.1. Representation Graph

YAML’s *representation* of [native data structure](https://yaml.org/spec/1.2.2/#representing-native-data-structures) is a rooted, connected, directed graph of [tagged](https://yaml.org/spec/1.2.2/#tags) [nodes](https://yaml.org/spec/1.2.2/#nodes). By “directed graph” we mean a set of [nodes](https://yaml.org/spec/1.2.2/#nodes) and directed edges (“arrows”), where each edge connects one [node](https://yaml.org/spec/1.2.2/#nodes) to another (see a formal directed graph definition[13](https://yaml.org/spec/1.2.2/#fn:digraph)). All the [nodes](https://yaml.org/spec/1.2.2/#nodes) must be reachable from the *root node* via such edges. Note that the YAML graph may include cycles and a [node](https://yaml.org/spec/1.2.2/#nodes) may have more than one incoming edge.

[Nodes](https://yaml.org/spec/1.2.2/#nodes) that are defined in terms of other [nodes](https://yaml.org/spec/1.2.2/#nodes) are [collections](https://yaml.org/spec/1.2.2/#collections); [nodes](https://yaml.org/spec/1.2.2/#nodes) that are independent of any other [nodes](https://yaml.org/spec/1.2.2/#nodes) are [scalars](https://yaml.org/spec/1.2.2/#scalars). YAML supports two [kinds](https://yaml.org/spec/1.2.2/#nodes) of [collection nodes](https://yaml.org/spec/1.2.2/#mapping): [sequences](https://yaml.org/spec/1.2.2/#sequence) and [mappings](https://yaml.org/spec/1.2.2/#mapping). [Mapping nodes](https://yaml.org/spec/1.2.2/#mapping) are somewhat tricky because their [keys](https://yaml.org/spec/1.2.2/#nodes) are unordered and must be [unique](https://yaml.org/spec/1.2.2/#node-comparison).

**Figure 3.3. Representation Model**

![Representation Model](https://yaml.org/spec/1.2.2/img/represent2.svg)

#### 3.2.1.1. Nodes

A YAML *node* [represents](https://yaml.org/spec/1.2.2/#representation-graph) a single [native data structure](https://yaml.org/spec/1.2.2/#representing-native-data-structures). Such nodes have *content* of one of three *kinds*: scalar, sequence or mapping. In addition, each node has a [tag](https://yaml.org/spec/1.2.2/#tags) which serves to restrict the set of possible values the content can have.

- Scalar

  The content of a *scalar* node is an opaque datum that can be [presented](https://yaml.org/spec/1.2.2/#presenting-the-serialization-tree) as a series of zero or more Unicode characters.

- Sequence

  The content of a *sequence* node is an ordered series of zero or more nodes. In particular, a sequence may contain the same node more than once. It could even contain itself.

- Mapping

  The content of a *mapping* node is an unordered set of *key/value* node *pairs*, with the restriction that each of the keys is [unique](https://yaml.org/spec/1.2.2/#node-comparison). YAML places no further restrictions on the nodes. In particular, keys may be arbitrary nodes, the same node may be used as the value of several key/value pairs and a mapping could even contain itself as a key or a value.

#### 3.2.1.2. Tags

YAML [represents](https://yaml.org/spec/1.2.2/#representation-graph) type information of [native data structures](https://yaml.org/spec/1.2.2/#representing-native-data-structures) with a simple identifier, called a *tag*. *Global tags* are URIs and hence globally unique across all [applications](https://yaml.org/spec/1.2.2/#processes-and-models). The “`tag:`” URI scheme[14](https://yaml.org/spec/1.2.2/#fn:tag-uri) is recommended for all global YAML tags. In contrast, *local tags* are specific to a single [application](https://yaml.org/spec/1.2.2/#processes-and-models). Local tags start with “`!`”, are not URIs and are not expected to be globally unique. YAML provides a “`TAG`” directive to make tag notation less verbose; it also offers easy migration from local to global tags. To ensure this, local tags are restricted to the URI character set and use URI character [escaping](https://yaml.org/spec/1.2.2/#escaped-characters).

YAML does not mandate any special relationship between different tags that begin with the same substring. Tags ending with URI fragments (containing “`#`”) are no exception; tags that share the same base URI but differ in their fragment part are considered to be different, independent tags. By convention, fragments are used to identify different “variants” of a tag, while “`/`” is used to define nested tag “namespace” hierarchies. However, this is merely a convention and each tag may employ its own rules. For example, Perl tags may use “`::`” to express namespace hierarchies, Java tags may use “`.`”, etc.

YAML tags are used to associate meta information with each [node](https://yaml.org/spec/1.2.2/#nodes). In particular, each tag must specify the expected [node kind](https://yaml.org/spec/1.2.2/#nodes) ([scalar](https://yaml.org/spec/1.2.2/#scalar), [sequence](https://yaml.org/spec/1.2.2/#sequence) or [mapping](https://yaml.org/spec/1.2.2/#mapping)). [Scalar](https://yaml.org/spec/1.2.2/#scalar) tags must also provide a mechanism for converting [formatted content](https://yaml.org/spec/1.2.2/#scalar-formats) to a [canonical form](https://yaml.org/spec/1.2.2/#canonical-form) for supporting [equality](https://yaml.org/spec/1.2.2/#equality) testing. Furthermore, a tag may provide additional information such as the set of allowed [content](https://yaml.org/spec/1.2.2/#nodes) values for validation, a mechanism for [tag resolution](https://yaml.org/spec/1.2.2/#tag-resolution) or any other data that is applicable to all of the tag’s [nodes](https://yaml.org/spec/1.2.2/#nodes).

#### 3.2.1.3. Node Comparison

Since YAML [mappings](https://yaml.org/spec/1.2.2/#mapping) require [key](https://yaml.org/spec/1.2.2/#nodes) uniqueness, [representations](https://yaml.org/spec/1.2.2/#representation-graph) must include a mechanism for testing the equality of [nodes](https://yaml.org/spec/1.2.2/#nodes). This is non-trivial since YAML allows various ways to [format scalar content](https://yaml.org/spec/1.2.2/#scalar-formats). For example, the integer eleven can be written as “`0o13`” (octal) or “`0xB`” (hexadecimal). If both notations are used as [keys](https://yaml.org/spec/1.2.2/#nodes) in the same [mapping](https://yaml.org/spec/1.2.2/#mapping), only a YAML [processor](https://yaml.org/spec/1.2.2/#processes-and-models) which recognizes integer [formats](https://yaml.org/spec/1.2.2/#scalar-formats) would correctly flag the duplicate [key](https://yaml.org/spec/1.2.2/#nodes) as an error.

- Canonical Form

  YAML supports the need for [scalar](https://yaml.org/spec/1.2.2/#scalar) equality by requiring that every [scalar](https://yaml.org/spec/1.2.2/#scalar) [tag](https://yaml.org/spec/1.2.2/#tags) must specify a mechanism for producing the *canonical form* of any [formatted content](https://yaml.org/spec/1.2.2/#scalar-formats). This form is a Unicode character string which also [presents](https://yaml.org/spec/1.2.2/#presenting-the-serialization-tree) the same [content](https://yaml.org/spec/1.2.2/#nodes) and can be used for equality testing.

- Equality

  Two [nodes](https://yaml.org/spec/1.2.2/#nodes) must have the same [tag](https://yaml.org/spec/1.2.2/#tags) and [content](https://yaml.org/spec/1.2.2/#nodes) to be *equal*. Since each [tag](https://yaml.org/spec/1.2.2/#tags) applies to exactly one [kind](https://yaml.org/spec/1.2.2/#nodes), this implies that the two [nodes](https://yaml.org/spec/1.2.2/#nodes) must have the same [kind](https://yaml.org/spec/1.2.2/#nodes) to be equal.

  Two [scalars](https://yaml.org/spec/1.2.2/#scalars) are equal only when their [tags](https://yaml.org/spec/1.2.2/#tags) and canonical forms are equal character-by-character. Equality of [collections](https://yaml.org/spec/1.2.2/#collections) is defined recursively.

  Two [sequences](https://yaml.org/spec/1.2.2/#sequence) are equal only when they have the same [tag](https://yaml.org/spec/1.2.2/#tags) and length and each [node](https://yaml.org/spec/1.2.2/#nodes) in one [sequence](https://yaml.org/spec/1.2.2/#sequence) is equal to the corresponding [node](https://yaml.org/spec/1.2.2/#nodes) in the other [sequence](https://yaml.org/spec/1.2.2/#sequence).

  Two [mappings](https://yaml.org/spec/1.2.2/#mapping) are equal only when they have the same [tag](https://yaml.org/spec/1.2.2/#tags) and an equal set of [keys](https://yaml.org/spec/1.2.2/#nodes) and each [key](https://yaml.org/spec/1.2.2/#nodes) in this set is associated with equal [values](https://yaml.org/spec/1.2.2/#nodes) in both [mappings](https://yaml.org/spec/1.2.2/#mapping).

  Different URI schemes may define different rules for testing the equality of URIs. Since a YAML [processor](https://yaml.org/spec/1.2.2/#processes-and-models) cannot be reasonably expected to be aware of them all, it must resort to a simple character-by-character comparison of [tags](https://yaml.org/spec/1.2.2/#tags) to ensure consistency. This also happens to be the comparison method defined by the “`tag:`” URI scheme. [Tags](https://yaml.org/spec/1.2.2/#tags) in a YAML stream must therefore be [presented](https://yaml.org/spec/1.2.2/#presenting-the-serialization-tree) in a canonical way so that such comparison would yield the correct results.

  If a node has itself as a descendant (via an alias), then determining the equality of that node is implementation-defined.

  A YAML [processor](https://yaml.org/spec/1.2.2/#processes-and-models) may treat equal [scalars](https://yaml.org/spec/1.2.2/#scalars) as if they were identical.

- Uniqueness

  A [mapping’s](https://yaml.org/spec/1.2.2/#mapping) [keys](https://yaml.org/spec/1.2.2/#nodes) are *unique* if no two keys are equal to each other. Obviously, identical nodes are always considered equal.

### 3.2.2. Serialization Tree

To express a YAML [representation](https://yaml.org/spec/1.2.2/#representation-graph) using a serial API, it is necessary to impose an [order](https://yaml.org/spec/1.2.2/#mapping-key-order) on [mapping keys](https://yaml.org/spec/1.2.2/#nodes) and employ [alias nodes](https://yaml.org/spec/1.2.2/#alias-nodes) to indicate a subsequent occurrence of a previously encountered [node](https://yaml.org/spec/1.2.2/#nodes). The result of this process is a *serialization tree*, where each [node](https://yaml.org/spec/1.2.2/#nodes) has an ordered set of children. This tree can be traversed for a serial event-based API. [Construction](https://yaml.org/spec/1.2.2/#constructing-native-data-structures) of [native data structures](https://yaml.org/spec/1.2.2/#representing-native-data-structures) from the serial interface should not use [key order](https://yaml.org/spec/1.2.2/#mapping-key-order) or [anchor names](https://yaml.org/spec/1.2.2/#anchors-and-aliases) for the preservation of [application](https://yaml.org/spec/1.2.2/#processes-and-models) data.

**Figure 3.4. Serialization Model**

![Serialization Model](https://yaml.org/spec/1.2.2/img/serialize2.svg)

#### 3.2.2.1. Mapping Key Order

In the [representation](https://yaml.org/spec/1.2.2/#representation-graph) model, [mapping keys](https://yaml.org/spec/1.2.2/#nodes) do not have an order. To [serialize](https://yaml.org/spec/1.2.2/#serializing-the-representation-graph) a [mapping](https://yaml.org/spec/1.2.2/#mapping), it is necessary to impose an *ordering* on its [keys](https://yaml.org/spec/1.2.2/#nodes). This order is a [serialization detail](https://yaml.org/spec/1.2.2/#serializing-the-representation-graph) and should not be used when [composing](https://yaml.org/spec/1.2.2/#composing-the-representation-graph) the [representation graph](https://yaml.org/spec/1.2.2/#representation-graph) (and hence for the preservation of [application](https://yaml.org/spec/1.2.2/#processes-and-models) data). In every case where [node](https://yaml.org/spec/1.2.2/#nodes) order is significant, a [sequence](https://yaml.org/spec/1.2.2/#sequence) must be used. For example, an ordered [mapping](https://yaml.org/spec/1.2.2/#mapping) can be [represented](https://yaml.org/spec/1.2.2/#representation-graph) as a [sequence](https://yaml.org/spec/1.2.2/#sequence) of [mappings](https://yaml.org/spec/1.2.2/#mapping), where each [mapping](https://yaml.org/spec/1.2.2/#mapping) is a single [key/value pair](https://yaml.org/spec/1.2.2/#mapping). YAML provides convenient [compact notation](https://yaml.org/spec/1.2.2/#example-flow-mapping-adjacent-values) for this case.

#### 3.2.2.2. Anchors and Aliases

In the [representation graph](https://yaml.org/spec/1.2.2/#representation-graph), a [node](https://yaml.org/spec/1.2.2/#nodes) may appear in more than one [collection](https://yaml.org/spec/1.2.2/#collections). When [serializing](https://yaml.org/spec/1.2.2/#serializing-the-representation-graph) such data, the first occurrence of the [node](https://yaml.org/spec/1.2.2/#nodes) is *identified* by an *anchor*. Each subsequent occurrence is [serialized](https://yaml.org/spec/1.2.2/#serializing-the-representation-graph) as an [alias node](https://yaml.org/spec/1.2.2/#alias-nodes) which refers back to this anchor. Otherwise, anchor names are a [serialization detail](https://yaml.org/spec/1.2.2/#serializing-the-representation-graph) and are discarded once [composing](https://yaml.org/spec/1.2.2/#composing-the-representation-graph) is completed. When [composing](https://yaml.org/spec/1.2.2/#composing-the-representation-graph) a [representation graph](https://yaml.org/spec/1.2.2/#representation-graph) from [serialized](https://yaml.org/spec/1.2.2/#serializing-the-representation-graph) events, an alias event refers to the most recent event in the [serialization](https://yaml.org/spec/1.2.2/#serialization-tree) having the specified anchor. Therefore, anchors need not be unique within a [serialization](https://yaml.org/spec/1.2.2/#serialization-tree). In addition, an anchor need not have an alias node referring to it.

### 3.2.3. Presentation Stream

A YAML *presentation* is a [stream](https://yaml.org/spec/1.2.2/#streams) of Unicode characters making use of [styles](https://yaml.org/spec/1.2.2/#node-styles), [scalar content formats](https://yaml.org/spec/1.2.2/#scalar-formats), [comments](https://yaml.org/spec/1.2.2/#comments), [directives](https://yaml.org/spec/1.2.2/#directives) and other [presentation details](https://yaml.org/spec/1.2.2/#presenting-the-serialization-tree) to [present](https://yaml.org/spec/1.2.2/#presenting-the-serialization-tree) a YAML [serialization](https://yaml.org/spec/1.2.2/#serialization-tree) in a human readable way. YAML allows several [serialization trees](https://yaml.org/spec/1.2.2/#serialization-tree) to be contained in the same YAML presentation stream, as a series of [documents](https://yaml.org/spec/1.2.2/#documents) separated by [markers](https://yaml.org/spec/1.2.2/#document-markers).

**Figure 3.5. Presentation Model**

![Presentation Model](https://yaml.org/spec/1.2.2/img/present2.svg)

#### 3.2.3.1. Node Styles

Each [node](https://yaml.org/spec/1.2.2/#nodes) is presented in some *style*, depending on its [kind](https://yaml.org/spec/1.2.2/#nodes). The node style is a [presentation detail](https://yaml.org/spec/1.2.2/#presenting-the-serialization-tree) and is not reflected in the [serialization tree](https://yaml.org/spec/1.2.2/#serialization-tree) or [representation graph](https://yaml.org/spec/1.2.2/#representation-graph). There are two groups of styles. [Block styles](https://yaml.org/spec/1.2.2/#block-style-productions) use [indentation](https://yaml.org/spec/1.2.2/#indentation-spaces) to denote structure. In contrast, [flow styles](https://yaml.org/spec/1.2.2/#flow-style-productions) rely on explicit [indicators](https://yaml.org/spec/1.2.2/#indicator-characters).

YAML provides a rich set of *scalar styles*. [Block scalar](https://yaml.org/spec/1.2.2/#block-scalar-styles) styles include the [literal style](https://yaml.org/spec/1.2.2/#literal-style) and the [folded style](https://yaml.org/spec/1.2.2/#folded-style). [Flow scalar](https://yaml.org/spec/1.2.2/#flow-scalar-styles) styles include the [plain style](https://yaml.org/spec/1.2.2/#plain-style) and two quoted styles, the [single-quoted style](https://yaml.org/spec/1.2.2/#single-quoted-style) and the [double-quoted style](https://yaml.org/spec/1.2.2/#double-quoted-style). These styles offer a range of trade-offs between expressive power and readability.

Normally, [block sequences](https://yaml.org/spec/1.2.2/#block-sequences) and [mappings](https://yaml.org/spec/1.2.2/#mapping) begin on the next line. In some cases, YAML also allows nested [block](https://yaml.org/spec/1.2.2/#scalars) [collections](https://yaml.org/spec/1.2.2/#collections) to start in-line for a more [compact notation](https://yaml.org/spec/1.2.2/#example-flow-mapping-adjacent-values). In addition, YAML provides a [compact notation](https://yaml.org/spec/1.2.2/#example-flow-mapping-adjacent-values) for [flow mappings](https://yaml.org/spec/1.2.2/#flow-mappings) with a single [key/value pair](https://yaml.org/spec/1.2.2/#mapping), nested inside a [flow sequence](https://yaml.org/spec/1.2.2/#flow-sequences). These allow for a natural “ordered mapping” notation.

**Figure 3.6. Kind/Style Combinations**

![Kind/Style Combinations](https://yaml.org/spec/1.2.2/img/styles2.svg)

#### 3.2.3.2. Scalar Formats

YAML allows [scalars](https://yaml.org/spec/1.2.2/#scalars) to be [presented](https://yaml.org/spec/1.2.2/#presenting-the-serialization-tree) in several *formats*. For example, the integer “`11`” might also be written as “`0xB`”. [Tags](https://yaml.org/spec/1.2.2/#tags) must specify a mechanism for converting the formatted content to a [canonical form](https://yaml.org/spec/1.2.2/#canonical-form) for use in [equality](https://yaml.org/spec/1.2.2/#equality) testing. Like [node style](https://yaml.org/spec/1.2.2/#node-styles), the format is a [presentation detail](https://yaml.org/spec/1.2.2/#presenting-the-serialization-tree) and is not reflected in the [serialization tree](https://yaml.org/spec/1.2.2/#serialization-tree) and [representation graph](https://yaml.org/spec/1.2.2/#representation-graph).

#### 3.2.3.3. Comments

[Comments](https://yaml.org/spec/1.2.2/#comments) are a [presentation detail](https://yaml.org/spec/1.2.2/#presenting-the-serialization-tree) and must not have any effect on the [serialization tree](https://yaml.org/spec/1.2.2/#serialization-tree) or [representation graph](https://yaml.org/spec/1.2.2/#representation-graph). In particular, comments are not associated with a particular [node](https://yaml.org/spec/1.2.2/#nodes). The usual purpose of a comment is to communicate between the human maintainers of a file. A typical example is comments in a configuration file. Comments must not appear inside [scalars](https://yaml.org/spec/1.2.2/#scalars), but may be interleaved with such [scalars](https://yaml.org/spec/1.2.2/#scalars) inside [collections](https://yaml.org/spec/1.2.2/#collections).

#### 3.2.3.4. Directives

Each [document](https://yaml.org/spec/1.2.2/#documents) may be associated with a set of [directives](https://yaml.org/spec/1.2.2/#directives). A directive has a name and an optional sequence of parameters. Directives are instructions to the YAML [processor](https://yaml.org/spec/1.2.2/#processes-and-models) and like all other [presentation details](https://yaml.org/spec/1.2.2/#presenting-the-serialization-tree) are not reflected in the YAML [serialization tree](https://yaml.org/spec/1.2.2/#serialization-tree) or [representation graph](https://yaml.org/spec/1.2.2/#representation-graph). This version of YAML defines two directives, “`YAML`” and “`TAG`”. All other directives are [reserved](https://yaml.org/spec/1.2.2/#directives) for future versions of YAML.

## 3.3. Loading Failure Points

The process of [loading](https://yaml.org/spec/1.2.2/#load) [native data structures](https://yaml.org/spec/1.2.2/#representing-native-data-structures) from a YAML [stream](https://yaml.org/spec/1.2.2/#streams) has several potential *failure points*. The character [stream](https://yaml.org/spec/1.2.2/#streams) may be [ill-formed](https://yaml.org/spec/1.2.2/#well-formed-streams-and-identified-aliases), [aliases](https://yaml.org/spec/1.2.2/#anchors-and-aliases) may be [unidentified](https://yaml.org/spec/1.2.2/#well-formed-streams-and-identified-aliases), [unspecified tags](https://yaml.org/spec/1.2.2/#resolved-tags) may be [unresolvable](https://yaml.org/spec/1.2.2/#resolved-tags), [tags](https://yaml.org/spec/1.2.2/#tags) may be [unrecognized](https://yaml.org/spec/1.2.2/#recognized-and-valid-tags), the [content](https://yaml.org/spec/1.2.2/#nodes) may be [invalid](https://yaml.org/spec/1.2.2/#recognized-and-valid-tags), [mapping](https://yaml.org/spec/1.2.2/#mapping) [keys](https://yaml.org/spec/1.2.2/#nodes) may not be [unique](https://yaml.org/spec/1.2.2/#node-comparison) and a native type may be [unavailable](https://yaml.org/spec/1.2.2/#available-tags). Each of these failures results with an incomplete loading.

A *partial representation* need not [resolve](https://yaml.org/spec/1.2.2/#resolved-tags) the [tag](https://yaml.org/spec/1.2.2/#tags) of each [node](https://yaml.org/spec/1.2.2/#nodes) and the [canonical form](https://yaml.org/spec/1.2.2/#canonical-form) of [formatted scalar content](https://yaml.org/spec/1.2.2/#scalar-formats) need not be available. This weaker representation is useful for cases of incomplete knowledge of the types used in the [document](https://yaml.org/spec/1.2.2/#documents).

In contrast, a *complete representation* specifies the [tag](https://yaml.org/spec/1.2.2/#tags) of each [node](https://yaml.org/spec/1.2.2/#nodes) and provides the [canonical form](https://yaml.org/spec/1.2.2/#canonical-form) of [formatted scalar content](https://yaml.org/spec/1.2.2/#scalar-formats), allowing for [equality](https://yaml.org/spec/1.2.2/#equality) testing. A complete representation is required in order to [construct](https://yaml.org/spec/1.2.2/#constructing-native-data-structures) [native data structures](https://yaml.org/spec/1.2.2/#representing-native-data-structures).

**Figure 3.7. Loading Failure Points**

![Loading Failure Points](https://yaml.org/spec/1.2.2/img/validity2.svg)

### 3.3.1. Well-Formed Streams and Identified Aliases

A [well-formed](https://yaml.org/spec/1.2.2/#example-stream) character [stream](https://yaml.org/spec/1.2.2/#streams) must match the BNF productions specified in the following chapters. Successful loading also requires that each [alias](https://yaml.org/spec/1.2.2/#anchors-and-aliases) shall refer to a previous [node](https://yaml.org/spec/1.2.2/#nodes) [identified](https://yaml.org/spec/1.2.2/#anchors-and-aliases) by the [anchor](https://yaml.org/spec/1.2.2/#anchors-and-aliases). A YAML [processor](https://yaml.org/spec/1.2.2/#processes-and-models) should reject *ill-formed streams* and *unidentified aliases*. A YAML [processor](https://yaml.org/spec/1.2.2/#processes-and-models) may recover from syntax errors, possibly by ignoring certain parts of the input, but it must provide a mechanism for reporting such errors.

### 3.3.2. Resolved Tags

Typically, most [tags](https://yaml.org/spec/1.2.2/#tags) are not explicitly specified in the character [stream](https://yaml.org/spec/1.2.2/#streams). During [parsing](https://yaml.org/spec/1.2.2/#parsing-the-presentation-stream), [nodes](https://yaml.org/spec/1.2.2/#nodes) lacking an explicit [tag](https://yaml.org/spec/1.2.2/#tags) are given a *non-specific tag*: “`!`” for non-[plain scalars](https://yaml.org/spec/1.2.2/#plain-style) and “`?`” for all other [nodes](https://yaml.org/spec/1.2.2/#nodes). [Composing](https://yaml.org/spec/1.2.2/#composing-the-representation-graph) a [complete representation](https://yaml.org/spec/1.2.2/#loading-failure-points) requires each such non-specific tag to be *resolved* to a *specific tag*, be it a [global tag](https://yaml.org/spec/1.2.2/#tags) or a [local tag](https://yaml.org/spec/1.2.2/#tags).

Resolving the [tag](https://yaml.org/spec/1.2.2/#tags) of a [node](https://yaml.org/spec/1.2.2/#nodes) must only depend on the following three parameters: (1) the non-specific tag of the [node](https://yaml.org/spec/1.2.2/#nodes), (2) the path leading from the [root](https://yaml.org/spec/1.2.2/#representation-graph) to the [node](https://yaml.org/spec/1.2.2/#nodes) and (3) the [content](https://yaml.org/spec/1.2.2/#nodes) (and hence the [kind](https://yaml.org/spec/1.2.2/#nodes)) of the [node](https://yaml.org/spec/1.2.2/#nodes). When a [node](https://yaml.org/spec/1.2.2/#nodes) has more than one occurrence (using [aliases](https://yaml.org/spec/1.2.2/#anchors-and-aliases)), tag resolution must depend only on the path to the first ([anchored](https://yaml.org/spec/1.2.2/#anchors-and-aliases)) occurrence of the [node](https://yaml.org/spec/1.2.2/#nodes).

Note that resolution must not consider [presentation details](https://yaml.org/spec/1.2.2/#presenting-the-serialization-tree) such as [comments](https://yaml.org/spec/1.2.2/#comments), [indentation](https://yaml.org/spec/1.2.2/#indentation-spaces) and [node style](https://yaml.org/spec/1.2.2/#node-styles). Also, resolution must not consider the [content](https://yaml.org/spec/1.2.2/#nodes) of any other [node](https://yaml.org/spec/1.2.2/#nodes), except for the [content](https://yaml.org/spec/1.2.2/#nodes) of the [key nodes](https://yaml.org/spec/1.2.2/#mapping) directly along the path leading from the [root](https://yaml.org/spec/1.2.2/#representation-graph) to the resolved [node](https://yaml.org/spec/1.2.2/#nodes). Finally, resolution must not consider the [content](https://yaml.org/spec/1.2.2/#nodes) of a sibling [node](https://yaml.org/spec/1.2.2/#nodes) in a [collection](https://yaml.org/spec/1.2.2/#collections) or the [content](https://yaml.org/spec/1.2.2/#nodes) of the [value node](https://yaml.org/spec/1.2.2/#nodes) associated with a [key node](https://yaml.org/spec/1.2.2/#mapping) being resolved.

These rules ensure that tag resolution can be performed as soon as a [node](https://yaml.org/spec/1.2.2/#nodes) is first encountered in the [stream](https://yaml.org/spec/1.2.2/#streams), typically before its [content](https://yaml.org/spec/1.2.2/#nodes) is [parsed](https://yaml.org/spec/1.2.2/#parsing-the-presentation-stream). Also, tag resolution only requires referring to a relatively small number of previously parsed [nodes](https://yaml.org/spec/1.2.2/#nodes). Thus, in most cases, tag resolution in one-pass [processors](https://yaml.org/spec/1.2.2/#processes-and-models) is both possible and practical.

YAML [processors](https://yaml.org/spec/1.2.2/#processes-and-models) should resolve [nodes](https://yaml.org/spec/1.2.2/#nodes) having the “`!`” non-specific tag as “`tag:yaml.org,2002:seq`”, “`tag:yaml.org,2002:map`” or “`tag:yaml.org,2002:str`” depending on their [kind](https://yaml.org/spec/1.2.2/#nodes). This *tag resolution convention* allows the author of a YAML character [stream](https://yaml.org/spec/1.2.2/#streams) to effectively “disable” the tag resolution process. By explicitly specifying a “`!`” non-specific [tag property](https://yaml.org/spec/1.2.2/#node-tags), the [node](https://yaml.org/spec/1.2.2/#nodes) would then be resolved to a “vanilla” [sequence](https://yaml.org/spec/1.2.2/#sequence), [mapping](https://yaml.org/spec/1.2.2/#mapping) or string, according to its [kind](https://yaml.org/spec/1.2.2/#nodes).

[Application](https://yaml.org/spec/1.2.2/#processes-and-models) specific tag resolution rules should be restricted to resolving the “`?`” non-specific tag, most commonly to resolving [plain scalars](https://yaml.org/spec/1.2.2/#plain-style). These may be matched against a set of regular expressions to provide automatic resolution of integers, floats, timestamps and similar types. An [application](https://yaml.org/spec/1.2.2/#processes-and-models) may also match the [content](https://yaml.org/spec/1.2.2/#nodes) of [mapping nodes](https://yaml.org/spec/1.2.2/#mapping) against sets of expected [keys](https://yaml.org/spec/1.2.2/#nodes) to automatically resolve points, complex numbers and similar types. Resolved [sequence node](https://yaml.org/spec/1.2.2/#sequence) types such as the “ordered mapping” are also possible.

That said, tag resolution is specific to the [application](https://yaml.org/spec/1.2.2/#processes-and-models). YAML [processors](https://yaml.org/spec/1.2.2/#processes-and-models) should therefore provide a mechanism allowing the [application](https://yaml.org/spec/1.2.2/#processes-and-models) to override and expand these default tag resolution rules.

If a [document](https://yaml.org/spec/1.2.2/#documents) contains *unresolved tags*, the YAML [processor](https://yaml.org/spec/1.2.2/#processes-and-models) is unable to [compose](https://yaml.org/spec/1.2.2/#composing-the-representation-graph) a [complete representation](https://yaml.org/spec/1.2.2/#loading-failure-points) graph. In such a case, the YAML [processor](https://yaml.org/spec/1.2.2/#processes-and-models) may [compose](https://yaml.org/spec/1.2.2/#composing-the-representation-graph) a [partial representation](https://yaml.org/spec/1.2.2/#loading-failure-points), based on each [node’s kind](https://yaml.org/spec/1.2.2/#nodes) and allowing for non-specific tags.

### 3.3.3. Recognized and Valid Tags

To be *valid*, a [node](https://yaml.org/spec/1.2.2/#nodes) must have a [tag](https://yaml.org/spec/1.2.2/#tags) which is *recognized* by the YAML [processor](https://yaml.org/spec/1.2.2/#processes-and-models) and its [content](https://yaml.org/spec/1.2.2/#nodes) must satisfy the constraints imposed by this [tag](https://yaml.org/spec/1.2.2/#tags). If a [document](https://yaml.org/spec/1.2.2/#documents) contains a [scalar node](https://yaml.org/spec/1.2.2/#nodes) with an *unrecognized tag* or *invalid content*, only a [partial representation](https://yaml.org/spec/1.2.2/#loading-failure-points) may be [composed](https://yaml.org/spec/1.2.2/#composing-the-representation-graph). In contrast, a YAML [processor](https://yaml.org/spec/1.2.2/#processes-and-models) can always [compose](https://yaml.org/spec/1.2.2/#composing-the-representation-graph) a [complete representation](https://yaml.org/spec/1.2.2/#loading-failure-points) for an unrecognized or an invalid [collection](https://yaml.org/spec/1.2.2/#collections), since [collection](https://yaml.org/spec/1.2.2/#collections) [equality](https://yaml.org/spec/1.2.2/#equality) does not depend upon knowledge of the [collection’s](https://yaml.org/spec/1.2.2/#mapping) data type. However, such a [complete representation](https://yaml.org/spec/1.2.2/#loading-failure-points) cannot be used to [construct](https://yaml.org/spec/1.2.2/#constructing-native-data-structures) a [native data structure](https://yaml.org/spec/1.2.2/#representing-native-data-structures).

### 3.3.4. Available Tags

In a given processing environment, there need not be an *available* native type corresponding to a given [tag](https://yaml.org/spec/1.2.2/#tags). If a [node’s tag](https://yaml.org/spec/1.2.2/#tags) is *unavailable*, a YAML [processor](https://yaml.org/spec/1.2.2/#processes-and-models) will not be able to [construct](https://yaml.org/spec/1.2.2/#constructing-native-data-structures) a [native data structure](https://yaml.org/spec/1.2.2/#representing-native-data-structures) for it. In this case, a [complete representation](https://yaml.org/spec/1.2.2/#loading-failure-points) may still be [composed](https://yaml.org/spec/1.2.2/#composing-the-representation-graph) and an [application](https://yaml.org/spec/1.2.2/#processes-and-models) may wish to use this [representation](https://yaml.org/spec/1.2.2/#representation-graph) directly.