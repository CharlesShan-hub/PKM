# 概述

> 本文按照YAML官方文档1.2.2版本翻译总结而成
>
> https://yaml.org/spec/1.2.2/#chapter-2-language-overview

*This section provides a quick glimpse into the expressive power of YAML. It is not expected that the first-time reader grok all of the examples. Rather, these selections are used as motivation for the remainder of the specification.*

本节简要介绍YAML的表达能力。第一次阅读的读者不可能熟读所有的例子。相反，这些选择被用作规范其余部分的动机。

## 2.1. Collections

*YAML’s [block collections](https://yaml.org/spec/1.2.2/#block-collection-styles) use [indentation](https://yaml.org/spec/1.2.2/#indentation-spaces) for scope and begin each entry on its own line. [Block sequences](https://yaml.org/spec/1.2.2/#block-sequences) indicate each entry with a dash and space (“`- `”). [Mappings](https://yaml.org/spec/1.2.2/#mapping) use a colon and space (“`: `”) to mark each [key/value pair](https://yaml.org/spec/1.2.2/#mapping). [Comments](https://yaml.org/spec/1.2.2/#comments) begin with an octothorpe (also called a “hash”, “sharp”, “pound” or “number sign” - “`#`”).*

* YAML的使用[缩进](https://yaml.org/spec/1.2.2/#indentation-spaces)作为[块集合](https://yaml.org/spec/1.2.2/#block-collection-styles)的范围，并在自己的行上开始每个条目。
* [块序列](https://yaml.org/spec/1.2.2/#block-sequences)用破折号和空格(“`- `”)表示每个条目。
* [映射](https://yaml.org/spec/1.2.2/#mapping)使用冒号和空格(“`: `”)来标记每个[键/值对](https://yaml.org/spec/1.2.2/#mapping)。
* [语句](https://yaml.org/spec/1.2.2/#comments)以八通码(也称为“hash”、“sharp”、“pound” 或 “number sign” - “`# `”)开始。

**Example 2.1 Sequence of Scalars (ball players)** **标量序列（球手）**

```yaml
- Mark McGwire
- Sammy Sosa
- Ken Griffey
```

**Example 2.2 Mapping Scalars to Scalars (player statistics)** **将标量映射到标量（玩家统计信息）**

```yaml
hr:  65    # Home runs
avg: 0.278 # Batting average
rbi: 147   # Runs Batted In
```

**Example 2.3 Mapping Scalars to Sequences (ball clubs in each league)** **将标量映射到序列（每个联赛中的球杆）**

```yaml
american:
- Boston Red Sox
- Detroit Tigers
- New York Yankees
national:
- New York Mets
- Chicago Cubs
- Atlanta Braves
```

**Example 2.4 Sequence of Mappings (players’ statistics)** **映射序列（玩家的统计数据）**

```yaml
-
  name: Mark McGwire
  hr:   65
  avg:  0.278
-
  name: Sammy Sosa
  hr:   63
  avg:  0.288
```

*YAML also has [flow styles](https://yaml.org/spec/1.2.2/#flow-style-productions), using explicit [indicators](https://yaml.org/spec/1.2.2/#indicator-characters) rather than [indentation](https://yaml.org/spec/1.2.2/#indentation-spaces) to denote scope. The [flow sequence](https://yaml.org/spec/1.2.2/#flow-sequences) is written as a [comma](https://yaml.org/spec/1.2.2/#flow-collection-styles) separated list within [square](https://yaml.org/spec/1.2.2/#flow-sequences) [brackets](https://yaml.org/spec/1.2.2/#flow-sequences). In a similar manner, the [flow mapping](https://yaml.org/spec/1.2.2/#flow-mappings) uses [curly](https://yaml.org/spec/1.2.2/#flow-mappings) [braces](https://yaml.org/spec/1.2.2/#flow-mappings).*

* YAML还有[流样式](https://yaml.org/spec/1.2.2/#flow-style-productions)，使用显式的[指示器](https://yaml.org/spec/1.2.2/#indicator-characters)而不是[缩进](https://yaml.org/spec/1.2.2/#indentation-spaces)来表示作用域。
* [流序列](https://yaml.org/spec/1.2.2/#flow-sequences)被写成[逗号](https://yaml.org/spec/1.2.2/#flow-collection-styles)分隔在[方框](https://yaml.org/spec/1.2.2/#flow-sequences)[方括号](https://yaml.org/spec/1.2.2/#flow-sequences)中的列表。以类似的方式，[流映射](https://yaml.org/spec/1.2.2/#flow-mappings)使用[大括号](https://yaml.org/spec/1.2.2/#flow-mappings)[大括号](https://yaml.org/spec/1.2.2/#flow-mappings)。

**Example 2.5 Sequence of Sequences**

```yaml
- [name        , hr, avg  ]
- [Mark McGwire, 65, 0.278]
- [Sammy Sosa  , 63, 0.288]
```

**Example 2.6 Mapping of Mappings**

```yaml
Mark McGwire: {hr: 65, avg: 0.278}
Sammy Sosa: {
    hr: 63,
    avg: 0.288,
 }
```

## 2.2. Structures

*YAML uses three dashes (“`---`”) to separate [directives](https://yaml.org/spec/1.2.2/#directives) from [document](https://yaml.org/spec/1.2.2/#documents) [content](https://yaml.org/spec/1.2.2/#nodes). This also serves to signal the start of a document if no [directives](https://yaml.org/spec/1.2.2/#directives) are present. Three dots ( “`...`”) indicate the end of a document without starting a new one, for use in communication channels.*

* YAML使用三个破折号(" '---' ")来分隔[指令](https://yaml.org/spec/1.2.2/#directives)和[文档](https://yaml.org/spec/1.2.2/#documents)[内容](https://yaml.org/spec/1.2.2/#nodes)。如果没有[指令](https://yaml.org/spec/1.2.2/#directives)，这也用来表示文档的开始。
* 三个点(“……”)表示一个文档的结束，而不是开始一个新的文档，用于通信通道。

**Example 2.7 Two Documents in a Stream (each with a leading comment)**

```yaml
# Ranking of 1998 home runs
---
- Mark McGwire
- Sammy Sosa
- Ken Griffey

# Team ranking
---
- Chicago Cubs
- St Louis Cardinals
```

**Example 2.8 Play by Play Feed from a Game**

```yaml
---
time: 20:03:20
player: Sammy Sosa
action: strike (miss)
...
---
time: 20:03:47
player: Sammy Sosa
action: grand slam
...
```

*Repeated [nodes](https://yaml.org/spec/1.2.2/#nodes) (objects) are first [identified](https://yaml.org/spec/1.2.2/#anchors-and-aliases) by an [anchor](https://yaml.org/spec/1.2.2/#anchors-and-aliases) (marked with the ampersand - “`&`”) and are then [aliased](https://yaml.org/spec/1.2.2/#anchors-and-aliases) (referenced with an asterisk - “`*`”) thereafter.*

重复的[节点](https://yaml.org/spec/1.2.2/#nodes)（对象）首先由[锚点](https://yaml.org/spec/1.2.2/#anchors-and-aliases)（标有 & 符号 - “`&`”）[标识](https://yaml.org/spec/1.2.2/#anchors-and-aliases)，然后[是别名](https://yaml.org/spec/1.2.2/#anchors-and-aliases)（用星号 - “`*`”引用”）。

**Example 2.9 Single Document with Two Comments**

`Sammy Sosa`的节点在本文档中出现了两次

```yaml
---
hr: # 1998 hr ranking
- Mark McGwire
- Sammy Sosa
# 1998 rbi ranking
rbi:
- Sammy Sosa
- Ken Griffey
```

**Example 2.10 Node for “`Sammy Sosa`” appears twice in this document**

上例中第二个`Sammy Sosa`和第一个合并

```yaml
---
hr:
- Mark McGwire
# Following node labeled SS
- &SS Sammy Sosa
rbi:
- *SS # Subsequent occurrence
- Ken Griffey
```

*A question mark and space (“`? `”) indicate a complex [mapping](https://yaml.org/spec/1.2.2/#mapping) [key](https://yaml.org/spec/1.2.2/#nodes). Within a [block collection](https://yaml.org/spec/1.2.2/#block-collection-styles), [key/value pairs](https://yaml.org/spec/1.2.2/#mapping) can start immediately following the [dash](https://yaml.org/spec/1.2.2/#block-sequences), [colon](https://yaml.org/spec/1.2.2/#flow-mappings) or [question mark](https://yaml.org/spec/1.2.2/#flow-mappings).*

一个问号和一个空格(" `?` ")表示复杂的[映射](https://yaml.org/spec/1.2.2/#mapping) [key](https://yaml.org/spec/1.2.2/#nodes)。在[块集合](https://yaml.org/spec/1.2.2/#block-collection-styles)中，[键/值对](https://yaml.org/spec/1.2.2/#mapping)可以紧跟着[破折号](https://yaml.org/spec/1.2.2/#block-sequences)，[冒号](https://yaml.org/spec/1.2.2/#flow-mappings)或[问号](https://yaml.org/spec/1.2.2/#flow-mappings)。

**Example 2.11 Mapping between Sequences**

```yaml
? - Detroit Tigers
  - Chicago cubs
: - 2001-07-23

? [ New York Yankees,
    Atlanta Braves ]
: [ 2001-07-02, 2001-08-12,
    2001-08-14 ]
    
# "? "问号+空格表示复杂的键, 再如RGB与颜色对应
? [blue, red, green]: Color
# 等价于下面
? - blue
  - red
  - green
: Color
```

**Example 2.12 Compact Nested Mapping**

```yaml
---
# Products purchased
- item    : Super Hoop
  quantity: 1
- item    : Basketball
  quantity: 4
- item    : Big Shoes
  quantity: 1
```

## 2.3. Scalars

*[Scalar content](https://yaml.org/spec/1.2.2/#scalar) can be written in [block](https://yaml.org/spec/1.2.2/#scalars) notation, using a [literal style](https://yaml.org/spec/1.2.2/#literal-style) (indicated by “`|`”) where all [line breaks](https://yaml.org/spec/1.2.2/#line-break-characters) are significant. Alternatively, they can be written with the [folded style](https://yaml.org/spec/1.2.2/#folded-style) (denoted by “`>`”) where each [line break](https://yaml.org/spec/1.2.2/#line-break-characters) is [folded](https://yaml.org/spec/1.2.2/#line-folding) to a [space](https://yaml.org/spec/1.2.2/#white-space-characters) unless it ends an [empty](https://yaml.org/spec/1.2.2/#empty-lines) or a [more-indented](https://yaml.org/spec/1.2.2/#example-more-indented-lines) line.*

* 使用`|`可以保留多行字符串的换行符
* 使用`>`可以将多行字符串的换行符转换为一个空格

**Example 2.13 In literals, newlines are preserved**

在字面值中，保留换行符

```yaml
# ASCII Art
--- |
  \//||\/||
  // ||  ||__
```

**Example 2.14 In the folded scalars, newlines become spaces**

在折叠的标量中，换行成为空格

```yaml
--- >
  Mark McGwire's
  year was crippled
  by a knee injury.
```

**Example 2.15 Folded newlines are preserved for “more indented” and blank lines**

为“更缩进”和空白行保留折叠换行

```yaml
--- >
 Sammy Sosa completed another
 fine season with great stats.

   63 Home Runs
   0.288 Batting Average

 What a year!
```

下面是python-IDE中的案例

```python
Python 3.7.6 (default, Jan  8 2020, 13:42:34) 
[Clang 4.0.1 (tags/RELEASE_401/final)] :: Anaconda, Inc. on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import yaml
>>> a = '''>
...  Sammy Sosa completed another
...  fine season with great stats.
... 
...    63 Home Runs
...    0.288 Batting Average
... 
...  What a year!'''
>>> print(yaml.load(a))
Sammy Sosa completed another fine season with great stats.

  63 Home Runs
  0.288 Batting Average

What a year!
>>> 
```

**Example 2.16 Indentation determines scope**

```yaml
name: Mark McGwire
accomplishment: >
  Mark set a major league
  home run record in 1998.
stats: |
  65 Home Runs
  0.278 Batting Average
```

*YAML’s [flow scalars](https://yaml.org/spec/1.2.2/#flow-scalar-styles) include the [plain style](https://yaml.org/spec/1.2.2/#plain-style) (most examples thus far) and two quoted styles. The [double-quoted style](https://yaml.org/spec/1.2.2/#double-quoted-style) provides [escape sequences](https://yaml.org/spec/1.2.2/#escaped-characters). The [single-quoted style](https://yaml.org/spec/1.2.2/#single-quoted-style) is useful when [escaping](https://yaml.org/spec/1.2.2/#escaped-characters) is not needed. All [flow scalars](https://yaml.org/spec/1.2.2/#flow-scalar-styles) can span multiple lines; [line breaks](https://yaml.org/spec/1.2.2/#line-break-characters) are always [folded](https://yaml.org/spec/1.2.2/#line-folding).*

YAML的[流标量](https://yaml.org/spec/1.2.2/#flow-scalar-styles)包括[普通样式](https://yaml.org/spec/1.2.2/#plain-style)(到目前为止的大多数示例)和两个引用的样式。[双引号样式](https://yaml.org/spec/1.2.2/#double-quoted-style)提供[转义序列](https://yaml.org/spec/1.2.2/#escaped-characters)。当不需要[转义](https://yaml.org/spec/1.2.2/#escaped-characters)时，[单引号样式](https://yaml.org/spec/1.2.2/#single-quoted-style)很有用。所有[流量标量](https://yaml.org/spec/1.2.2/#flow-scalar-styles)可以跨越多行;[换行符](https://yaml.org/spec/1.2.2/#line-break-characters)总是[折叠](https://yaml.org/spec/1.2.2/#line-folding)。

**Example 2.17 Quoted Scalars**

```yaml
unicode: "Sosa did fine.\u263A"
control: "\b1998\t1999\t2000\n"
hex esc: "\x0d\x0a is \r\n"

single: '"Howdy!" he cried.'
quoted: ' # Not a ''comment''.'
tie-fighter: '|\-*-/|'
```

**Example 2.18 Multi-line Flow Scalars**

```yaml
plain:
  This unquoted scalar
  spans many lines.

quoted: "So does this
  quoted scalar.\n"
```

## 2.4. Tags

*In YAML, [untagged nodes](https://yaml.org/spec/1.2.2/#resolved-tags) are given a type depending on the [application](https://yaml.org/spec/1.2.2/#processes-and-models). The examples in this specification generally use the `seq`, `map` and `str` types from the [fail safe schema](https://yaml.org/spec/1.2.2/#failsafe-schema). A few examples also use the `int`, `float` and `null` types from the [JSON schema](https://yaml.org/spec/1.2.2/#json-schema).*

在YAML中，[无标记节点](https://yaml.org/spec/1.2.2/#resolved-tags)根据[应用场景](https://yaml.org/spec/1.2.2/#processes-and-models)给出了一种类型。本规范中的示例通常使用[fail safe schema](https://yaml.org/spec/1.2.2/#failsafe-schema)中的`seq`、`map`和`str`类型。一些例子也使用了[JSON模式](https://yaml.org/spec/1.2.2/#json-schema)中的`int`， `float`和`null`类型。

**Example 2.19 Integers**

```yaml
canonical: 12345
decimal: +12345
octal: 0o14
hexadecimal: 0xC
```

**Example 2.20 Floating Point**

```yaml
canonical: 1.23015e+3
exponential: 12.3015e+02
fixed: 1230.15
negative infinity: -.inf
not a number: .nan
```

**Example 2.21 Miscellaneous**

```yaml
null:
booleans: [ true, false ]
string: '012345'
```

**Example 2.22 Timestamps**

```yaml
canonical: 2001-12-15T02:59:43.1Z
iso8601: 2001-12-14t21:59:43.10-05:00
spaced: 2001-12-14 21:59:43.10 -5
date: 2002-12-14
```

*Explicit typing is denoted with a [tag](https://yaml.org/spec/1.2.2/#tags) using the exclamation point (“`!`”) symbol. [Global tags](https://yaml.org/spec/1.2.2/#tags) are URIs and may be specified in a [tag shorthand](https://yaml.org/spec/1.2.2/#tag-shorthands) notation using a [handle](https://yaml.org/spec/1.2.2/#tag-handles). [Application](https://yaml.org/spec/1.2.2/#processes-and-models)-specific [local tags](https://yaml.org/spec/1.2.2/#tags) may also be used.*

显式输入用[标记](https://yaml.org/spec/1.2.2/#tags)表示，并使用感叹号("`!`")符号。[Global tags](https://yaml.org/spec/1.2.2/#tags)是URIs，可以使用[handle](https://yaml.org/spec/1.2.2/#tag-handles)在[tag简写](https://yaml.org/spec/1.2.2/#tag-shorthands)表示法中指定。[Application](https://yaml.org/spec/1.2.2/#processes-and-models)-specific [local tags](https://yaml.org/spec/1.2.2/#tags)也可以使用。

**Example 2.23 Various Explicit Tags**

```yaml
---
not-date: !!str 2002-04-28

picture: !!binary |
 R0lGODlhDAAMAIQAAP//9/X
 17unp5WZmZgAAAOfn515eXv
 Pz7Y6OjuDg4J+fn5OTk6enp
 56enmleECcgggoBADs=

application specific tag: !something |
 The semantics of the tag
 above may be different for
 different documents.
```

**Example 2.24 Global Tags**

```yaml
%TAG ! tag:clarkevans.com,2002:
--- !shape
  # Use the ! handle for presenting
  # tag:clarkevans.com,2002:circle
- !circle
  center: &ORIGIN {x: 73, y: 129}
  radius: 7
- !line
  start: *ORIGIN
  finish: { x: 89, y: 102 }
- !label
  start: *ORIGIN
  color: 0xFFEEBB
  text: Pretty vector drawing.
```

**Example 2.25 Unordered Sets**

```yaml
# Sets are represented as a
# Mapping where each key is
# associated with a null value
--- !!set
? Mark McGwire
? Sammy Sosa
? Ken Griffey
```

**Example 2.26 Ordered Mappings**

```yaml
# Ordered maps are represented as
# A sequence of mappings, with
# each mapping having one key
--- !!omap
- Mark McGwire: 65
- Sammy Sosa: 63
- Ken Griffey: 58
```

## 2.5. Full Length Example

*Below are two full-length examples of YAML. The first is a sample invoice; the second is a sample log file.*

下面是两个完整的YAML示例。第一个是发票样本;第二个是示例日志文件。

**Example 2.27 Invoice**

```yaml
--- !<tag:clarkevans.com,2002:invoice>
invoice: 34843
date   : 2001-01-23
bill-to: &id001
  given  : Chris
  family : Dumars
  address:
    lines: |
      458 Walkman Dr.
      Suite #292
    city    : Royal Oak
    state   : MI
    postal  : 48046
ship-to: *id001
product:
- sku         : BL394D
  quantity    : 4
  description : Basketball
  price       : 450.00
- sku         : BL4438H
  quantity    : 1
  description : Super Hoop
  price       : 2392.00
tax  : 251.42
total: 4443.52
comments:
  Late afternoon is best.
  Backup contact is Nancy
  Billsmer @ 338-4338.
```

**Example 2.28 Log File**

```yaml
---
Time: 2001-11-23 15:01:42 -5
User: ed
Warning:
  This is an error message
  for the log file
---
Time: 2001-11-23 15:02:31 -5
User: ed
Warning:
  A slightly different error
  message.
---
Date: 2001-11-23 15:03:17 -5
User: ed
Fatal:
  Unknown variable "bar"
Stack:
- file: TopClass.py
  line: 23
  code: |
    x = MoreObject("345\n")
- file: MoreClass.py
  line: 58
  code: |-
    foo = bar
```

