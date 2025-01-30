# 结构

> 本文按照YAML官方文档1.2.2版本翻译总结而成
>
> https://yaml.org/spec/1.2.2/#chapter-6-structural-productions

## 6.1. Indentation Spaces

In YAML [block styles](https://yaml.org/spec/1.2.2/#block-style-productions), structure is determined by *indentation*. In general, indentation is defined as a zero or more [space](https://yaml.org/spec/1.2.2/#white-space-characters) characters at the start of a line.

To maintain portability, [tab](https://yaml.org/spec/1.2.2/#white-space-characters) characters must not be used in indentation, since different systems treat [tabs](https://yaml.org/spec/1.2.2/#white-space-characters) differently. Note that most modern editors may be configured so that pressing the [tab](https://yaml.org/spec/1.2.2/#white-space-characters) key results in the insertion of an appropriate number of [spaces](https://yaml.org/spec/1.2.2/#white-space-characters).

The amount of indentation is a [presentation detail](https://yaml.org/spec/1.2.2/#presenting-the-serialization-tree) and must not be used to convey [content](https://yaml.org/spec/1.2.2/#nodes) information.

```
[63]
s-indent(0) ::=
  <empty>

# When n≥0
s-indent(n+1) ::=
  s-space s-indent(n)
```

A [block style](https://yaml.org/spec/1.2.2/#block-style-productions) construct is terminated when encountering a line which is less indented than the construct. The productions use the notation “`s-indent-less-than(n)`” and “`s-indent-less-or-equal(n)`” to express this.

```
[64]
s-indent-less-than(1) ::=
  <empty>

# When n≥1
s-indent-less-than(n+1) ::=
  s-space s-indent-less-than(n)
  | <empty>
[65]
s-indent-less-or-equal(0) ::=
  <empty>

# When n≥0
s-indent-less-or-equal(n+1) ::=
  s-space s-indent-less-or-equal(n)
  | <empty>
```

Each [node](https://yaml.org/spec/1.2.2/#nodes) must be indented further than its parent [node](https://yaml.org/spec/1.2.2/#nodes). All sibling [nodes](https://yaml.org/spec/1.2.2/#nodes) must use the exact same indentation level. However the [content](https://yaml.org/spec/1.2.2/#nodes) of each sibling [node](https://yaml.org/spec/1.2.2/#nodes) may be further indented independently.

**Example 6.1 Indentation Spaces**

| `··# Leading comment line spaces are ···# neither content nor indentation. ···· Not indented: ·By one space: | ····By four ······spaces ·Flow style: [    # Leading spaces ···By two,        # in flow style ··Also by two,    # are neither ··→Still by two   # content nor ····]             # indentation. ` | `{ "Not indented": {    "By one space": "By four\n  spaces\n",    "Flow style": [      "By two",      "Also by two",      "Still by two" ] } } ` |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
|                                                              |                                                              |

Legend:

- `s-indent(n)`
-  

- `Content`
-  

- `Neither content nor indentation`

The “`-`”, “`?`” and “`:`” characters used to denote [block collection](https://yaml.org/spec/1.2.2/#block-collection-styles) entries are perceived by people to be part of the indentation. This is handled on a case-by-case basis by the relevant productions.

**Example 6.2 Indentation Indicators**

| `?·a :·-→b ··-··-→c ·····-·d ` | `{ "a":  [ "b",    [ "c",      "d" ] ] } ` |
| ------------------------------ | ------------------------------------------ |
|                                |                                            |

Legend:

- `Total Indentation`
-  

- `s-indent(n)`
-  

- `Indicator as indentation`

## 6.2. Separation Spaces

Outside [indentation](https://yaml.org/spec/1.2.2/#indentation-spaces) and [scalar content](https://yaml.org/spec/1.2.2/#scalar), YAML uses [white space](https://yaml.org/spec/1.2.2/#white-space-characters) characters for *separation* between tokens within a line. Note that such [white space](https://yaml.org/spec/1.2.2/#white-space-characters) may safely include [tab](https://yaml.org/spec/1.2.2/#white-space-characters) characters.

Separation spaces are a [presentation detail](https://yaml.org/spec/1.2.2/#presenting-the-serialization-tree) and must not be used to convey [content](https://yaml.org/spec/1.2.2/#nodes) information.

```
[66] s-separate-in-line ::=
    s-white+
  | <start-of-line>
```

**Example 6.3 Separation Spaces**

| `-·foo:→·bar - -·baz  -→baz ` | `[ { "foo": "bar" },  [ "baz",    "baz" ] ] ` |
| ----------------------------- | --------------------------------------------- |
|                               |                                               |

Legend:

- `s-separate-in-line`

## 6.3. Line Prefixes

Inside [scalar content](https://yaml.org/spec/1.2.2/#scalar), each line begins with a non-[content](https://yaml.org/spec/1.2.2/#nodes) *line prefix*. This prefix always includes the [indentation](https://yaml.org/spec/1.2.2/#indentation-spaces). For [flow scalar styles](https://yaml.org/spec/1.2.2/#flow-scalar-styles) it additionally includes all leading [white space](https://yaml.org/spec/1.2.2/#white-space-characters), which may contain [tab](https://yaml.org/spec/1.2.2/#white-space-characters) characters.

Line prefixes are a [presentation detail](https://yaml.org/spec/1.2.2/#presenting-the-serialization-tree) and must not be used to convey [content](https://yaml.org/spec/1.2.2/#nodes) information.

```
[67]
s-line-prefix(n,BLOCK-OUT) ::= s-block-line-prefix(n)
s-line-prefix(n,BLOCK-IN)  ::= s-block-line-prefix(n)
s-line-prefix(n,FLOW-OUT)  ::= s-flow-line-prefix(n)
s-line-prefix(n,FLOW-IN)   ::= s-flow-line-prefix(n)
[68] s-block-line-prefix(n) ::=
  s-indent(n)
[69] s-flow-line-prefix(n) ::=
  s-indent(n)
  s-separate-in-line?
```

**Example 6.4 Line Prefixes**

| `plain: text ··lines quoted: "text ··→lines" block: | ··text ···→lines ` | `{ "plain": "text lines",  "quoted": "text lines",  "block": "text\n \tlines\n" } ` |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
|                                                              |                                                              |

Legend:

- `s-flow-line-prefix(n)`
-  

- `s-block-line-prefix(n)`
-  

- `s-indent(n)`

## 6.4. Empty Lines

An *empty line* line consists of the non-[content](https://yaml.org/spec/1.2.2/#nodes) [prefix](https://yaml.org/spec/1.2.2/#tag-prefixes) followed by a [line break](https://yaml.org/spec/1.2.2/#line-break-characters).

```
[70] l-empty(n,c) ::=
  (
      s-line-prefix(n,c)
    | s-indent-less-than(n)
  )
  b-as-line-feed
```

The semantics of empty lines depend on the [scalar style](https://yaml.org/spec/1.2.2/#node-styles) they appear in. This is handled on a case-by-case basis by the relevant productions.

**Example 6.5 Empty Lines**

| `Folding:  "Empty line ···→  as a line feed" Chomping: |  Clipped empty lines · ` | `{ "Folding": "Empty line\nas a line feed",  "Chomping": "Clipped empty lines\n" } ` |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
|                                                              |                                                              |

Legend:

- `l-empty(n,c)`

## 6.5. Line Folding

*Line folding* allows long lines to be broken for readability, while retaining the semantics of the original long line. If a [line break](https://yaml.org/spec/1.2.2/#line-break-characters) is followed by an [empty line](https://yaml.org/spec/1.2.2/#empty-lines), it is *trimmed*; the first [line break](https://yaml.org/spec/1.2.2/#line-break-characters) is discarded and the rest are retained as [content](https://yaml.org/spec/1.2.2/#nodes).

```
[71] b-l-trimmed(n,c) ::=
  b-non-content
  l-empty(n,c)+
```

Otherwise (the following line is not [empty](https://yaml.org/spec/1.2.2/#empty-lines)), the [line break](https://yaml.org/spec/1.2.2/#line-break-characters) is converted to a single [space](https://yaml.org/spec/1.2.2/#white-space-characters) (`x20`).

```
[72] b-as-space ::=
  b-break
```

A folded non-[empty line](https://yaml.org/spec/1.2.2/#empty-lines) may end with either of the above [line breaks](https://yaml.org/spec/1.2.2/#line-break-characters).

```
[73] b-l-folded(n,c) ::=
  b-l-trimmed(n,c) | b-as-space
```

**Example 6.6 Line Folding**

| `>-  trimmed↓ ··↓ ·↓ ↓  as↓  space ` | `"trimmed\n\n\nas space" ` |
| ------------------------------------ | -------------------------- |
|                                      |                            |

Legend:

- `b-l-trimmed(n,c)`
-  

- `b-as-space`

The above rules are common to both the [folded block style](https://yaml.org/spec/1.2.2/#block-folding) and the [scalar flow styles](https://yaml.org/spec/1.2.2/#flow-scalar-styles). Folding does distinguish between these cases in the following way:

- Block Folding

  In the [folded block style](https://yaml.org/spec/1.2.2/#block-folding), the final [line break](https://yaml.org/spec/1.2.2/#line-break-characters) and trailing [empty lines](https://yaml.org/spec/1.2.2/#empty-lines) are subject to [chomping](https://yaml.org/spec/1.2.2/#block-chomping-indicator) and are never folded. In addition, folding does not apply to [line breaks](https://yaml.org/spec/1.2.2/#line-break-characters) surrounding text lines that contain leading [white space](https://yaml.org/spec/1.2.2/#white-space-characters). Note that such a [more-indented](https://yaml.org/spec/1.2.2/#example-more-indented-lines) line may consist only of such leading [white space](https://yaml.org/spec/1.2.2/#white-space-characters).

  The combined effect of the *block line folding* rules is that each “paragraph” is interpreted as a line, [empty lines](https://yaml.org/spec/1.2.2/#empty-lines) are interpreted as a line feed and the formatting of [more-indented](https://yaml.org/spec/1.2.2/#example-more-indented-lines) lines is preserved.

**Example 6.7 Block Folding**

| `> ··foo·↓ ·↓ ··→·bar↓ ↓ ··baz↓ ` | `"foo \n\n\t bar\n\nbaz\n" ` |
| --------------------------------- | ---------------------------- |
|                                   |                              |

Legend:

- `b-l-folded(n,c)`
-  

- `Non-content spaces`
-  

- `Content spaces`

- Flow Folding

  Folding in [flow styles](https://yaml.org/spec/1.2.2/#flow-style-productions) provides more relaxed semantics. [Flow styles](https://yaml.org/spec/1.2.2/#flow-style-productions) typically depend on explicit [indicators](https://yaml.org/spec/1.2.2/#indicator-characters) rather than [indentation](https://yaml.org/spec/1.2.2/#indentation-spaces) to convey structure. Hence spaces preceding or following the text in a line are a [presentation detail](https://yaml.org/spec/1.2.2/#presenting-the-serialization-tree) and must not be used to convey [content](https://yaml.org/spec/1.2.2/#nodes) information. Once all such spaces have been discarded, all [line breaks](https://yaml.org/spec/1.2.2/#line-break-characters) are folded without exception.

  The combined effect of the *flow line folding* rules is that each “paragraph” is interpreted as a line, [empty lines](https://yaml.org/spec/1.2.2/#empty-lines) are interpreted as line feeds and text can be freely [more-indented](https://yaml.org/spec/1.2.2/#example-more-indented-lines) without affecting the [content](https://yaml.org/spec/1.2.2/#nodes) information.

```
[74] s-flow-folded(n) ::=
  s-separate-in-line?
  b-l-folded(n,FLOW-IN)
  s-flow-line-prefix(n)
```

**Example 6.8 Flow Folding**

| `"↓ ··foo·↓ ·↓ ··→·bar↓ ↓ ··baz↓ " ` | `" foo\nbar\nbaz " ` |
| ------------------------------------ | -------------------- |
|                                      |                      |

Legend:

- `s-flow-folded(n)`
-  

- `Non-content spaces`

## 6.6. Comments

An explicit *comment* is marked by a “`#`” indicator. Comments are a [presentation detail](https://yaml.org/spec/1.2.2/#presenting-the-serialization-tree) and must not be used to convey [content](https://yaml.org/spec/1.2.2/#nodes) information.

Comments must be [separated](https://yaml.org/spec/1.2.2/#separation-spaces) from other tokens by [white space](https://yaml.org/spec/1.2.2/#white-space-characters) characters.

> Note: To ensure [JSON compatibility](https://yaml.org/spec/1.2.2/#yaml-directives), YAML [processors](https://yaml.org/spec/1.2.2/#processes-and-models) must allow for the omission of the final comment [line break](https://yaml.org/spec/1.2.2/#line-break-characters) of the input [stream](https://yaml.org/spec/1.2.2/#streams). However, as this confuses many tools, YAML [processors](https://yaml.org/spec/1.2.2/#processes-and-models) should terminate the [stream](https://yaml.org/spec/1.2.2/#streams) with an explicit [line break](https://yaml.org/spec/1.2.2/#line-break-characters) on output.

```
[75] c-nb-comment-text ::=
  c-comment    # '#'
  nb-char*
[76] b-comment ::=
    b-non-content
  | <end-of-input>
[77] s-b-comment ::=
  (
    s-separate-in-line
    c-nb-comment-text?
  )?
  b-comment
```

**Example 6.9 Separated Comment**

| `key:····# Comment↓  value*eof* ` | `{ "key": "value" } ` |
| --------------------------------- | --------------------- |
|                                   |                       |

Legend:

- `c-nb-comment-text`
-  

- `b-comment`
-  

- `s-b-comment`

Outside [scalar content](https://yaml.org/spec/1.2.2/#scalar), comments may appear on a line of their own, independent of the [indentation](https://yaml.org/spec/1.2.2/#indentation-spaces) level. Note that outside [scalar content](https://yaml.org/spec/1.2.2/#scalar), a line containing only [white space](https://yaml.org/spec/1.2.2/#white-space-characters) characters is taken to be a comment line.

```
[78] l-comment ::=
  s-separate-in-line
  c-nb-comment-text?
  b-comment
```

**Example 6.10 Comment Lines**

| `··# Comment↓ ···↓ ↓ ` | `# This stream contains no # documents, only comments. ` |
| ---------------------- | -------------------------------------------------------- |
|                        |                                                          |

Legend:

- `s-b-comment`
-  

- `l-comment`

In most cases, when a line may end with a comment, YAML allows it to be followed by additional comment lines. The only exception is a comment ending a [block scalar header](https://yaml.org/spec/1.2.2/#block-scalar-headers).

```
[79] s-l-comments ::=
  (
      s-b-comment
    | <start-of-line>
  )
  l-comment*
```

**Example 6.11 Multi-Line Comments**

| `key:····# Comment↓ ········# lines↓  value↓ ↓ ` | `{ "key": "value" } ` |
| ------------------------------------------------ | --------------------- |
|                                                  |                       |

Legend:

- `s-b-comment`
-  

- `l-comment`
-  

- `s-l-comments`

## 6.7. Separation Lines

[Implicit keys](https://yaml.org/spec/1.2.2/#example-single-pair-explicit-entry) are restricted to a single line. In all other cases, YAML allows tokens to be separated by multi-line (possibly empty) [comments](https://yaml.org/spec/1.2.2/#comments).

Note that structures following multi-line comment separation must be properly [indented](https://yaml.org/spec/1.2.2/#indentation-spaces), even though there is no such restriction on the separation [comment](https://yaml.org/spec/1.2.2/#comments) lines themselves.

```
[80]
s-separate(n,BLOCK-OUT) ::= s-separate-lines(n)
s-separate(n,BLOCK-IN)  ::= s-separate-lines(n)
s-separate(n,FLOW-OUT)  ::= s-separate-lines(n)
s-separate(n,FLOW-IN)   ::= s-separate-lines(n)
s-separate(n,BLOCK-KEY) ::= s-separate-in-line
s-separate(n,FLOW-KEY)  ::= s-separate-in-line
[81] s-separate-lines(n) ::=
    (
      s-l-comments
      s-flow-line-prefix(n)
    )
  | s-separate-in-line
```

**Example 6.12 Separation Spaces**

| `{·first:·Sammy,·last:·Sosa·}:↓ # Statistics: ··hr:··# Home runs ·····65 ··avg:·# Average ···0.278 ` | `{ { "first": "Sammy",    "last": "Sosa" }: {    "hr": 65,    "avg": 0.278 } } ` |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
|                                                              |                                                              |

Legend:

- `s-separate-in-line`
-  

- `s-separate-lines(n)`
-  

- `s-indent(n)`

## 6.8. Directives

*Directives* are instructions to the YAML [processor](https://yaml.org/spec/1.2.2/#processes-and-models). This specification defines two directives, “`YAML`” and “`TAG`”, and *reserves* all other directives for future use. There is no way to define private directives. This is intentional.

Directives are a [presentation detail](https://yaml.org/spec/1.2.2/#presenting-the-serialization-tree) and must not be used to convey [content](https://yaml.org/spec/1.2.2/#nodes) information.

```
[82] l-directive ::=
  c-directive            # '%'
  (
      ns-yaml-directive
    | ns-tag-directive
    | ns-reserved-directive
  )
  s-l-comments
```

Each directive is specified on a separate non-[indented](https://yaml.org/spec/1.2.2/#indentation-spaces) line starting with the “`%`” indicator, followed by the directive name and a list of parameters. The semantics of these parameters depends on the specific directive. A YAML [processor](https://yaml.org/spec/1.2.2/#processes-and-models) should ignore unknown directives with an appropriate warning.

```
[83] ns-reserved-directive ::=
  ns-directive-name
  (
    s-separate-in-line
    ns-directive-parameter
  )*
[84] ns-directive-name ::=
  ns-char+
[85] ns-directive-parameter ::=
  ns-char+
```

**Example 6.13 Reserved Directives**

| `%FOO  bar baz # Should be ignored               # with a warning. --- "foo" ` | `"foo" ` |
| ------------------------------------------------------------ | -------- |
|                                                              |          |

Legend:

- `ns-reserved-directive`
-  

- `ns-directive-name`
-  

- `ns-directive-parameter`

### 6.8.1. “`YAML`” Directives

The “`YAML`” directive specifies the version of YAML the [document](https://yaml.org/spec/1.2.2/#documents) conforms to. This specification defines version “`1.2`”, including recommendations for *YAML 1.1 processing*.

A version 1.2 YAML [processor](https://yaml.org/spec/1.2.2/#processes-and-models) must accept [documents](https://yaml.org/spec/1.2.2/#documents) with an explicit “`%YAML 1.2`” directive, as well as [documents](https://yaml.org/spec/1.2.2/#documents) lacking a “`YAML`” directive. Such [documents](https://yaml.org/spec/1.2.2/#documents) are assumed to conform to the 1.2 version specification. [Documents](https://yaml.org/spec/1.2.2/#documents) with a “`YAML`” directive specifying a higher minor version (e.g. “`%YAML 1.3`”) should be processed with an appropriate warning. [Documents](https://yaml.org/spec/1.2.2/#documents) with a “`YAML`” directive specifying a higher major version (e.g. “`%YAML 2.0`”) should be rejected with an appropriate error message.

A version 1.2 YAML [processor](https://yaml.org/spec/1.2.2/#processes-and-models) must also accept [documents](https://yaml.org/spec/1.2.2/#documents) with an explicit “`%YAML 1.1`” directive. Note that version 1.2 is mostly a superset of version 1.1, defined for the purpose of ensuring *JSON compatibility*. Hence a version 1.2 [processor](https://yaml.org/spec/1.2.2/#processes-and-models) should process version 1.1 [documents](https://yaml.org/spec/1.2.2/#documents) as if they were version 1.2, giving a warning on points of incompatibility (handling of [non-ASCII line breaks](https://yaml.org/spec/1.2.2/#line-break-characters), as described [above](https://yaml.org/spec/1.2.2/#line-break-characters)).

```
[86] ns-yaml-directive ::=
  "YAML"
  s-separate-in-line
  ns-yaml-version
[87] ns-yaml-version ::=
  ns-dec-digit+
  '.'
  ns-dec-digit+
```

**Example 6.14 “`YAML`” directive**

| `%YAML 1.3 # Attempt parsing           # with a warning --- "foo" ` | `"foo" ` |
| ------------------------------------------------------------ | -------- |
|                                                              |          |

Legend:

- `ns-yaml-directive`
-  

- `ns-yaml-version`

It is an error to specify more than one “`YAML`” directive for the same document, even if both occurrences give the same version number.

**Example 6.15 Invalid Repeated YAML directive**

| `%YAML 1.2 %YAML 1.1 foo ` | `ERROR: The YAML directive must only be given at most once per document. ` |
| -------------------------- | ------------------------------------------------------------ |
|                            |                                                              |

### 6.8.2. “`TAG`” Directives

The “`TAG`” directive establishes a [tag shorthand](https://yaml.org/spec/1.2.2/#tag-shorthands) notation for specifying [node tags](https://yaml.org/spec/1.2.2/#node-tags). Each “`TAG`” directive associates a [handle](https://yaml.org/spec/1.2.2/#tag-handles) with a [prefix](https://yaml.org/spec/1.2.2/#tag-prefixes). This allows for compact and readable [tag](https://yaml.org/spec/1.2.2/#tags) notation.

```
[88] ns-tag-directive ::=
  "TAG"
  s-separate-in-line
  c-tag-handle
  s-separate-in-line
  ns-tag-prefix
```

**Example 6.16 “`TAG`” directive**

| `%TAG !yaml! tag:yaml.org,2002: --- !yaml!str "foo" ` | `"foo" ` |
| ----------------------------------------------------- | -------- |
|                                                       |          |

Legend:

- `ns-tag-directive`
-  

- `c-tag-handle`
-  

- `ns-tag-prefix`

It is an error to specify more than one “`TAG`” directive for the same [handle](https://yaml.org/spec/1.2.2/#tag-handles) in the same document, even if both occurrences give the same [prefix](https://yaml.org/spec/1.2.2/#tag-prefixes).

**Example 6.17 Invalid Repeated TAG directive**

| `%TAG ! !foo %TAG ! !foo bar ` | `ERROR: The TAG directive must only be given at most once per handle in the same document. ` |
| ------------------------------ | ------------------------------------------------------------ |
|                                |                                                              |

#### 6.8.2.1. Tag Handles

The *tag handle* exactly matches the prefix of the affected [tag shorthand](https://yaml.org/spec/1.2.2/#tag-shorthands). There are three tag handle variants:

```
[89] c-tag-handle ::=
    c-named-tag-handle
  | c-secondary-tag-handle
  | c-primary-tag-handle
```

- Primary Handle

  The *primary tag handle* is a single “`!`” character. This allows using the most compact possible notation for a single “primary” name space. By default, the prefix associated with this handle is “`!`”. Thus, by default, [shorthands](https://yaml.org/spec/1.2.2/#tag-shorthands) using this handle are interpreted as [local tags](https://yaml.org/spec/1.2.2/#tags).

  It is possible to override the default behavior by providing an explicit “`TAG`” directive, associating a different prefix for this handle. This provides smooth migration from using [local tags](https://yaml.org/spec/1.2.2/#tags) to using [global tags](https://yaml.org/spec/1.2.2/#tags) by the simple addition of a single “`TAG`” directive.

```
[90] c-primary-tag-handle ::= '!'
```

**Example 6.18 Primary Tag Handle**

| `# Private !foo "bar" ... # Global %TAG ! tag:example.com,2000:app/ --- !foo "bar" ` | `!<!foo> "bar" --- !<tag:example.com,2000:app/foo> "bar" ` |
| ------------------------------------------------------------ | ---------------------------------------------------------- |
|                                                              |                                                            |

Legend:

- `c-primary-tag-handle`

- Secondary Handle

  The *secondary tag handle* is written as “`!!`”. This allows using a compact notation for a single “secondary” name space. By default, the prefix associated with this handle is “`tag:yaml.org,2002:`”.

  It is possible to override this default behavior by providing an explicit “`TAG`” directive associating a different prefix for this handle.

```
[91] c-secondary-tag-handle ::= "!!"
```

**Example 6.19 Secondary Tag Handle**

| `%TAG !! tag:example.com,2000:app/ --- !!int 1 - 3 # Interval, not integer ` | `!<tag:example.com,2000:app/int> "1 - 3" ` |
| ------------------------------------------------------------ | ------------------------------------------ |
|                                                              |                                            |

Legend:

- `c-secondary-tag-handle`

- Named Handles

  A *named tag handle* surrounds a non-empty name with “`!`” characters. A handle name must not be used in a [tag shorthand](https://yaml.org/spec/1.2.2/#tag-shorthands) unless an explicit “`TAG`” directive has associated some prefix with it.

  The name of the handle is a [presentation detail](https://yaml.org/spec/1.2.2/#presenting-the-serialization-tree) and must not be used to convey [content](https://yaml.org/spec/1.2.2/#nodes) information. In particular, the YAML [processor](https://yaml.org/spec/1.2.2/#processes-and-models) need not preserve the handle name once [parsing](https://yaml.org/spec/1.2.2/#parsing-the-presentation-stream) is completed.

```
[92] c-named-tag-handle ::=
  c-tag            # '!'
  ns-word-char+
  c-tag            # '!'
```

**Example 6.20 Tag Handles**

| `%TAG !e! tag:example.com,2000:app/ --- !e!foo "bar" ` | `!<tag:example.com,2000:app/foo> "bar" ` |
| ------------------------------------------------------ | ---------------------------------------- |
|                                                        |                                          |

Legend:

- `c-named-tag-handle`

#### 6.8.2.2. Tag Prefixes

There are two *tag prefix* variants:

```
[93] ns-tag-prefix ::=
  c-ns-local-tag-prefix | ns-global-tag-prefix
```

- Local Tag Prefix

  If the prefix begins with a “`!`” character, [shorthands](https://yaml.org/spec/1.2.2/#tag-shorthands) using the [handle](https://yaml.org/spec/1.2.2/#tag-handles) are expanded to a [local tag](https://yaml.org/spec/1.2.2/#tags). Note that such a [tag](https://yaml.org/spec/1.2.2/#tags) is intentionally not a valid URI and its semantics are specific to the [application](https://yaml.org/spec/1.2.2/#processes-and-models). In particular, two [documents](https://yaml.org/spec/1.2.2/#documents) in the same [stream](https://yaml.org/spec/1.2.2/#streams) may assign different semantics to the same [local tag](https://yaml.org/spec/1.2.2/#tags).

```
[94] c-ns-local-tag-prefix ::=
  c-tag           # '!'
  ns-uri-char*
```

**Example 6.21 Local Tag Prefix**

| `%TAG !m! !my- --- # Bulb here !m!light fluorescent ... %TAG !m! !my- --- # Color here !m!light green ` | `!<!my-light> "fluorescent" --- !<!my-light> "green" ` |
| ------------------------------------------------------------ | ------------------------------------------------------ |
|                                                              |                                                        |

Legend:

- `c-ns-local-tag-prefix`

- Global Tag Prefix

  If the prefix begins with a character other than “`!`”, it must be a valid URI prefix, and should contain at least the scheme. [Shorthands](https://yaml.org/spec/1.2.2/#tag-shorthands) using the associated [handle](https://yaml.org/spec/1.2.2/#tag-handles) are expanded to globally unique URI tags and their semantics is consistent across [applications](https://yaml.org/spec/1.2.2/#processes-and-models). In particular, every [document](https://yaml.org/spec/1.2.2/#documents) in every [stream](https://yaml.org/spec/1.2.2/#streams) must assign the same semantics to the same [global tag](https://yaml.org/spec/1.2.2/#tags).

```
[95] ns-global-tag-prefix ::=
  ns-tag-char
  ns-uri-char*
```

**Example 6.22 Global Tag Prefix**

| `%TAG !e! tag:example.com,2000:app/ --- - !e!foo "bar" ` | `- !<tag:example.com,2000:app/foo> "bar" ` |
| -------------------------------------------------------- | ------------------------------------------ |
|                                                          |                                            |

Legend:

- `ns-global-tag-prefix`

## 6.9. Node Properties

Each [node](https://yaml.org/spec/1.2.2/#nodes) may have two optional *properties*, [anchor](https://yaml.org/spec/1.2.2/#anchors-and-aliases) and [tag](https://yaml.org/spec/1.2.2/#tags), in addition to its [content](https://yaml.org/spec/1.2.2/#nodes). Node properties may be specified in any order before the [node’s content](https://yaml.org/spec/1.2.2/#nodes). Either or both may be omitted.

```
[96] c-ns-properties(n,c) ::=
    (
      c-ns-tag-property
      (
        s-separate(n,c)
        c-ns-anchor-property
      )?
    )
  | (
      c-ns-anchor-property
      (
        s-separate(n,c)
        c-ns-tag-property
      )?
    )
```

**Example 6.23 Node Properties**

| `!!str &a1 "foo":  !!str bar &a2 baz : *a1 ` | `{ &B1 "foo": "bar",  "baz": *B1 } ` |
| -------------------------------------------- | ------------------------------------ |
|                                              |                                      |

Legend:

- `c-ns-properties(n,c)`
-  

- `c-ns-anchor-property`
-  

- `c-ns-tag-property`

### 6.9.1. Node Tags

The *tag property* identifies the type of the [native data structure](https://yaml.org/spec/1.2.2/#representing-native-data-structures) [presented](https://yaml.org/spec/1.2.2/#presenting-the-serialization-tree) by the [node](https://yaml.org/spec/1.2.2/#nodes). A tag is denoted by the “`!`” indicator.

```
[97] c-ns-tag-property ::=
    c-verbatim-tag
  | c-ns-shorthand-tag
  | c-non-specific-tag
```

- Verbatim Tags

  A tag may be written *verbatim* by surrounding it with the “`<`” and “`>`” characters. In this case, the YAML [processor](https://yaml.org/spec/1.2.2/#processes-and-models) must deliver the verbatim tag as-is to the [application](https://yaml.org/spec/1.2.2/#processes-and-models). In particular, verbatim tags are not subject to [tag resolution](https://yaml.org/spec/1.2.2/#tag-resolution). A verbatim tag must either begin with a “`!`” (a [local tag](https://yaml.org/spec/1.2.2/#tags)) or be a valid URI (a [global tag](https://yaml.org/spec/1.2.2/#tags)).

```
[98] c-verbatim-tag ::=
  "!<"
  ns-uri-char+
  '>'
```

**Example 6.24 Verbatim Tags**

| `!<tag:yaml.org,2002:str> foo :  !<!bar> baz ` | `{ "foo": !<!bar> "baz" } ` |
| ---------------------------------------------- | --------------------------- |
|                                                |                             |

Legend:

- `c-verbatim-tag`

**Example 6.25 Invalid Verbatim Tags**

| `- !<!> foo - !<$:?> bar ` | `ERROR: - Verbatim tags aren't resolved,  so ! is invalid. - The $:? tag is neither a global  URI tag nor a local tag starting  with '!'. ` |
| -------------------------- | ------------------------------------------------------------ |
|                            |                                                              |

- Tag Shorthands

  A *tag shorthand* consists of a valid [tag handle](https://yaml.org/spec/1.2.2/#tag-handles) followed by a non-empty suffix. The [tag handle](https://yaml.org/spec/1.2.2/#tag-handles) must be associated with a [prefix](https://yaml.org/spec/1.2.2/#tag-prefixes), either by default or by using a “`TAG`” directive. The resulting [parsed](https://yaml.org/spec/1.2.2/#parsing-the-presentation-stream) [tag](https://yaml.org/spec/1.2.2/#tags) is the concatenation of the [prefix](https://yaml.org/spec/1.2.2/#tag-prefixes) and the suffix and must either begin with “`!`” (a [local tag](https://yaml.org/spec/1.2.2/#tags)) or be a valid URI (a [global tag](https://yaml.org/spec/1.2.2/#tags)).

  The choice of [tag handle](https://yaml.org/spec/1.2.2/#tag-handles) is a [presentation detail](https://yaml.org/spec/1.2.2/#presenting-the-serialization-tree) and must not be used to convey [content](https://yaml.org/spec/1.2.2/#nodes) information. In particular, the [tag handle](https://yaml.org/spec/1.2.2/#tag-handles) may be discarded once [parsing](https://yaml.org/spec/1.2.2/#parsing-the-presentation-stream) is completed.

  The suffix must not contain any “`!`” character. This would cause the tag shorthand to be interpreted as having a [named tag handle](https://yaml.org/spec/1.2.2/#tag-handles). In addition, the suffix must not contain the “`[`”, “`]`”, “`{`”, “`}`” and “`,`” characters. These characters would cause ambiguity with [flow collection](https://yaml.org/spec/1.2.2/#flow-collection-styles) structures. If the suffix needs to specify any of the above restricted characters, they must be [escaped](https://yaml.org/spec/1.2.2/#escaped-characters) using the “`%`” character. This behavior is consistent with the URI character escaping rules (specifically, section 2.3 of URI RFC).

```
[99] c-ns-shorthand-tag ::=
  c-tag-handle
  ns-tag-char+
```

**Example 6.26 Tag Shorthands**

| `%TAG !e! tag:example.com,2000:app/ --- - !local foo - !!str bar - !e!tag%21 baz ` | `[ !<!local> "foo",  !<tag:yaml.org,2002:str> "bar",  !<tag:example.com,2000:app/tag!> "baz" ] ` |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
|                                                              |                                                              |

Legend:

- `c-ns-shorthand-tag`

**Example 6.27 Invalid Tag Shorthands**

| `%TAG !e! tag:example,2000:app/ --- - !e! foo - !h!bar baz ` | `ERROR: - The !e! handle has no suffix. - The !h! handle wasn't declared. ` |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
|                                                              |                                                              |

- Non-Specific Tags

  If a [node](https://yaml.org/spec/1.2.2/#nodes) has no tag property, it is assigned a [non-specific tag](https://yaml.org/spec/1.2.2/#resolved-tags) that needs to be [resolved](https://yaml.org/spec/1.2.2/#resolved-tags) to a [specific](https://yaml.org/spec/1.2.2/#resolved-tags) one. This [non-specific tag](https://yaml.org/spec/1.2.2/#resolved-tags) is “`!`” for non-[plain scalars](https://yaml.org/spec/1.2.2/#plain-style) and “`?`” for all other [nodes](https://yaml.org/spec/1.2.2/#nodes). This is the only case where the [node style](https://yaml.org/spec/1.2.2/#node-styles) has any effect on the [content](https://yaml.org/spec/1.2.2/#nodes) information.

  It is possible for the tag property to be explicitly set to the “`!`” non-specific tag. By [convention](https://yaml.org/spec/1.2.2/#resolved-tags), this “disables” [tag resolution](https://yaml.org/spec/1.2.2/#tag-resolution), forcing the [node](https://yaml.org/spec/1.2.2/#nodes) to be interpreted as “`tag:yaml.org,2002:seq`”, “`tag:yaml.org,2002:map`” or “`tag:yaml.org,2002:str`”, according to its [kind](https://yaml.org/spec/1.2.2/#nodes).

  There is no way to explicitly specify the “`?`” non-specific tag. This is intentional.

```
[100] c-non-specific-tag ::= '!'
```

**Example 6.28 Non-Specific Tags**

| `# Assuming conventional resolution: - "12" - 12 - ! 12 ` | `[ "12",  12,  "12" ] ` |
| --------------------------------------------------------- | ----------------------- |
|                                                           |                         |

Legend:

- `c-non-specific-tag`

### 6.9.2. Node Anchors

An anchor is denoted by the “`&`” indicator. It marks a [node](https://yaml.org/spec/1.2.2/#nodes) for future reference. An [alias node](https://yaml.org/spec/1.2.2/#alias-nodes) can then be used to indicate additional inclusions of the anchored [node](https://yaml.org/spec/1.2.2/#nodes). An anchored [node](https://yaml.org/spec/1.2.2/#nodes) need not be referenced by any [alias nodes](https://yaml.org/spec/1.2.2/#alias-nodes); in particular, it is valid for all [nodes](https://yaml.org/spec/1.2.2/#nodes) to be anchored.

```
[101] c-ns-anchor-property ::=
  c-anchor          # '&'
  ns-anchor-name
```

Note that as a [serialization detail](https://yaml.org/spec/1.2.2/#serializing-the-representation-graph), the anchor name is preserved in the [serialization tree](https://yaml.org/spec/1.2.2/#serialization-tree). However, it is not reflected in the [representation](https://yaml.org/spec/1.2.2/#representation-graph) graph and must not be used to convey [content](https://yaml.org/spec/1.2.2/#nodes) information. In particular, the YAML [processor](https://yaml.org/spec/1.2.2/#processes-and-models) need not preserve the anchor name once the [representation](https://yaml.org/spec/1.2.2/#representation-graph) is [composed](https://yaml.org/spec/1.2.2/#composing-the-representation-graph).

Anchor names must not contain the “`[`”, “`]`”, “`{`”, “`}`” and “`,`” characters. These characters would cause ambiguity with [flow collection](https://yaml.org/spec/1.2.2/#flow-collection-styles) structures.

```
[102] ns-anchor-char ::=
    ns-char - c-flow-indicator
[103] ns-anchor-name ::=
  ns-anchor-char+
```

**Example 6.29 Node Anchors**

| `First occurrence: &anchor Value Second occurrence: *anchor ` | `{ "First occurrence": &A "Value",  "Second occurrence": *A } ` |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
|                                                              |                                                              |

Legend:

- `c-ns-anchor-property`
- `ns-anchor-name`