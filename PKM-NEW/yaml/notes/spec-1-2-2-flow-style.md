# 流风格

> 本文按照YAML官方文档1.2.2版本翻译总结而成
>
> https://yaml.org/spec/1.2.2/#chapter-7-flow-style-productions

YAML’s *flow styles* can be thought of as the natural extension of JSON to cover [folding](https://yaml.org/spec/1.2.2/#line-folding) long content lines for readability, [tagging](https://yaml.org/spec/1.2.2/#tags) nodes to control [construction](https://yaml.org/spec/1.2.2/#constructing-native-data-structures) of [native data structures](https://yaml.org/spec/1.2.2/#representing-native-data-structures) and using [anchors](https://yaml.org/spec/1.2.2/#anchors-and-aliases) and [aliases](https://yaml.org/spec/1.2.2/#anchors-and-aliases) to reuse [constructed](https://yaml.org/spec/1.2.2/#constructing-native-data-structures) object instances.

## 7.1. Alias Nodes

Subsequent occurrences of a previously [serialized](https://yaml.org/spec/1.2.2/#serializing-the-representation-graph) node are [presented](https://yaml.org/spec/1.2.2/#presenting-the-serialization-tree) as *alias nodes*. The first occurrence of the [node](https://yaml.org/spec/1.2.2/#nodes) must be marked by an [anchor](https://yaml.org/spec/1.2.2/#anchors-and-aliases) to allow subsequent occurrences to be [presented](https://yaml.org/spec/1.2.2/#presenting-the-serialization-tree) as alias nodes.

An alias node is denoted by the “`*`” indicator. The alias refers to the most recent preceding [node](https://yaml.org/spec/1.2.2/#nodes) having the same [anchor](https://yaml.org/spec/1.2.2/#anchors-and-aliases). It is an error for an alias node to use an [anchor](https://yaml.org/spec/1.2.2/#anchors-and-aliases) that does not previously occur in the [document](https://yaml.org/spec/1.2.2/#documents). It is not an error to specify an [anchor](https://yaml.org/spec/1.2.2/#anchors-and-aliases) that is not used by any alias node.

Note that an alias node must not specify any [properties](https://yaml.org/spec/1.2.2/#node-properties) or [content](https://yaml.org/spec/1.2.2/#nodes), as these were already specified at the first occurrence of the [node](https://yaml.org/spec/1.2.2/#nodes).

```
[104] c-ns-alias-node ::=
  c-alias           # '*'
  ns-anchor-name
```

**Example 7.1 Alias Nodes**

| `First occurrence: &anchor Foo Second occurrence: *anchor Override anchor: &anchor Bar Reuse anchor: *anchor ` | `{ "First occurrence": &A "Foo",  "Override anchor": &B "Bar",  "Second occurrence": *A,  "Reuse anchor": *B } ` |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
|                                                              |                                                              |

Legend:

- `c-ns-alias-node`
-  

- `ns-anchor-name`

## 7.2. Empty Nodes

YAML allows the [node content](https://yaml.org/spec/1.2.2/#nodes) to be omitted in many cases. [Nodes](https://yaml.org/spec/1.2.2/#nodes) with empty [content](https://yaml.org/spec/1.2.2/#nodes) are interpreted as if they were [plain scalars](https://yaml.org/spec/1.2.2/#plain-style) with an empty value. Such [nodes](https://yaml.org/spec/1.2.2/#nodes) are commonly resolved to a “`null`” value.

```
[105] e-scalar ::= ""
```

In the examples, empty [scalars](https://yaml.org/spec/1.2.2/#scalars) are sometimes displayed as the glyph “`°`” for clarity. Note that this glyph corresponds to a position in the characters [stream](https://yaml.org/spec/1.2.2/#streams) rather than to an actual character.

**Example 7.2 Empty Content**

| `{  foo : !!str°,  !!str° : bar, } ` | `{ "foo": "",  "": "bar" } ` |
| ------------------------------------ | ---------------------------- |
|                                      |                              |

Legend:

- `e-scalar`

Both the [node’s properties](https://yaml.org/spec/1.2.2/#node-properties) and [node content](https://yaml.org/spec/1.2.2/#nodes) are optional. This allows for a *completely empty node*. Completely empty nodes are only valid when following some explicit indication for their existence.

```
[106] e-node ::=
  e-scalar    # ""
```

**Example 7.3 Completely Empty Flow Nodes**

| `{  ? foo :°,  °: bar, } ` | `{ "foo": null,  null : "bar" } ` |
| -------------------------- | --------------------------------- |
|                            |                                   |

Legend:

- `e-node`

## 7.3. Flow Scalar Styles

YAML provides three *flow scalar styles*: [double-quoted](https://yaml.org/spec/1.2.2/#double-quoted-style), [single-quoted](https://yaml.org/spec/1.2.2/#single-quoted-style) and [plain](https://yaml.org/spec/1.2.2/#plain-style) (unquoted). Each provides a different trade-off between readability and expressive power.

The [scalar style](https://yaml.org/spec/1.2.2/#node-styles) is a [presentation detail](https://yaml.org/spec/1.2.2/#presenting-the-serialization-tree) and must not be used to convey [content](https://yaml.org/spec/1.2.2/#nodes) information, with the exception that [plain scalars](https://yaml.org/spec/1.2.2/#plain-style) are distinguished for the purpose of [tag resolution](https://yaml.org/spec/1.2.2/#tag-resolution).

### 7.3.1. Double-Quoted Style

The *double-quoted style* is specified by surrounding “`"`” indicators. This is the only [style](https://yaml.org/spec/1.2.2/#node-styles) capable of expressing arbitrary strings, by using “`\`” [escape sequences](https://yaml.org/spec/1.2.2/#escaped-characters). This comes at the cost of having to escape the “`\`” and “`"`” characters.

```
[107] nb-double-char ::=
    c-ns-esc-char
  | (
        nb-json
      - c-escape          # '\'
      - c-double-quote    # '"'
    )
[108] ns-double-char ::=
  nb-double-char - s-white
```

Double-quoted scalars are restricted to a single line when contained inside an [implicit key](https://yaml.org/spec/1.2.2/#example-single-pair-explicit-entry).

```
[109] c-double-quoted(n,c) ::=
  c-double-quote         # '"'
  nb-double-text(n,c)
  c-double-quote         # '"'
[110]
nb-double-text(n,FLOW-OUT)  ::= nb-double-multi-line(n)
nb-double-text(n,FLOW-IN)   ::= nb-double-multi-line(n)
nb-double-text(n,BLOCK-KEY) ::= nb-double-one-line
nb-double-text(n,FLOW-KEY)  ::= nb-double-one-line
[111] nb-double-one-line ::=
  nb-double-char*
```

**Example 7.4 Double Quoted Implicit Keys**

| `"implicit block key" : [  "implicit flow key" : value, ] ` | `{ "implicit block key":  [ { "implicit flow key": "value" } ] } ` |
| ----------------------------------------------------------- | ------------------------------------------------------------ |
|                                                             |                                                              |

Legend:

- `nb-double-one-line`
-  

- `c-double-quoted(n,c)`

In a multi-line double-quoted scalar, [line breaks](https://yaml.org/spec/1.2.2/#line-break-characters) are subject to [flow line folding](https://yaml.org/spec/1.2.2/#flow-folding), which discards any trailing [white space](https://yaml.org/spec/1.2.2/#white-space-characters) characters. It is also possible to *escape* the [line break](https://yaml.org/spec/1.2.2/#line-break-characters) character. In this case, the escaped [line break](https://yaml.org/spec/1.2.2/#line-break-characters) is excluded from the [content](https://yaml.org/spec/1.2.2/#nodes) and any trailing [white space](https://yaml.org/spec/1.2.2/#white-space-characters) characters that precede the escaped line break are preserved. Combined with the ability to [escape](https://yaml.org/spec/1.2.2/#escaped-characters) [white space](https://yaml.org/spec/1.2.2/#white-space-characters) characters, this allows double-quoted lines to be broken at arbitrary positions.

```
[112] s-double-escaped(n) ::=
  s-white*
  c-escape         # '\'
  b-non-content
  l-empty(n,FLOW-IN)*
  s-flow-line-prefix(n)
[113] s-double-break(n) ::=
    s-double-escaped(n)
  | s-flow-folded(n)
```

**Example 7.5 Double Quoted Line Breaks**

| `"folded·↓ to a space,→↓ ·↓ to a line feed, or·→\↓ ·\·→non-content" ` | `"folded to a space,\nto a line feed, or \t \tnon-content" ` |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
|                                                              |                                                              |

Legend:

- `s-flow-folded(n)`
-  

- `s-double-escaped(n)`

All leading and trailing [white space](https://yaml.org/spec/1.2.2/#white-space-characters) characters on each line are excluded from the [content](https://yaml.org/spec/1.2.2/#nodes). Each continuation line must therefore contain at least one non-[space](https://yaml.org/spec/1.2.2/#white-space-characters) character. Empty lines, if any, are consumed as part of the [line folding](https://yaml.org/spec/1.2.2/#line-folding).

```
[114] nb-ns-double-in-line ::=
  (
    s-white*
    ns-double-char
  )*
[115] s-double-next-line(n) ::=
  s-double-break(n)
  (
    ns-double-char nb-ns-double-in-line
    (
        s-double-next-line(n)
      | s-white*
    )
  )?
[116] nb-double-multi-line(n) ::=
  nb-ns-double-in-line
  (
      s-double-next-line(n)
    | s-white*
  )
```

**Example 7.6 Double Quoted Lines**

| `"·1st non-empty↓ ↓ ·2nd non-empty· →3rd non-empty·" ` | `" 1st non-empty\n2nd non-empty 3rd non-empty " ` |
| ------------------------------------------------------ | ------------------------------------------------- |
|                                                        |                                                   |

Legend:

- `nb-ns-double-in-line`
-  

- `s-double-next-line(n)`

### 7.3.2. Single-Quoted Style

The *single-quoted style* is specified by surrounding “`'`” indicators. Therefore, within a single-quoted scalar, such characters need to be repeated. This is the only form of *escaping* performed in single-quoted scalars. In particular, the “`\`” and “`"`” characters may be freely used. This restricts single-quoted scalars to [printable](https://yaml.org/spec/1.2.2/#character-set) characters. In addition, it is only possible to break a long single-quoted line where a [space](https://yaml.org/spec/1.2.2/#white-space-characters) character is surrounded by non-[spaces](https://yaml.org/spec/1.2.2/#white-space-characters).

```
[117] c-quoted-quote ::= "''"
[118] nb-single-char ::=
    c-quoted-quote
  | (
        nb-json
      - c-single-quote    # "'"
    )
[119] ns-single-char ::=
  nb-single-char - s-white
```

**Example 7.7 Single Quoted Characters**

| `'here''s to "quotes"' ` | `"here's to \"quotes\"" ` |
| ------------------------ | ------------------------- |
|                          |                           |

Legend:

- `c-quoted-quote`

Single-quoted scalars are restricted to a single line when contained inside a [implicit key](https://yaml.org/spec/1.2.2/#example-single-pair-explicit-entry).

```
[120] c-single-quoted(n,c) ::=
  c-single-quote    # "'"
  nb-single-text(n,c)
  c-single-quote    # "'"
[121]
nb-single-text(FLOW-OUT)  ::= nb-single-multi-line(n)
nb-single-text(FLOW-IN)   ::= nb-single-multi-line(n)
nb-single-text(BLOCK-KEY) ::= nb-single-one-line
nb-single-text(FLOW-KEY)  ::= nb-single-one-line
[122] nb-single-one-line ::=
  nb-single-char*
```

**Example 7.8 Single Quoted Implicit Keys**

| `'implicit block key' : [  'implicit flow key' : value, ] ` | `{ "implicit block key":  [ { "implicit flow key": "value" } ] } ` |
| ----------------------------------------------------------- | ------------------------------------------------------------ |
|                                                             |                                                              |

Legend:

- `nb-single-one-line`
-  

- `c-single-quoted(n,c)`

All leading and trailing [white space](https://yaml.org/spec/1.2.2/#white-space-characters) characters are excluded from the [content](https://yaml.org/spec/1.2.2/#nodes). Each continuation line must therefore contain at least one non-[space](https://yaml.org/spec/1.2.2/#white-space-characters) character. Empty lines, if any, are consumed as part of the [line folding](https://yaml.org/spec/1.2.2/#line-folding).

```
[123] nb-ns-single-in-line ::=
  (
    s-white*
    ns-single-char
  )*
[124] s-single-next-line(n) ::=
  s-flow-folded(n)
  (
    ns-single-char
    nb-ns-single-in-line
    (
        s-single-next-line(n)
      | s-white*
    )
  )?
[125] nb-single-multi-line(n) ::=
  nb-ns-single-in-line
  (
      s-single-next-line(n)
    | s-white*
  )
```

**Example 7.9 Single Quoted Lines**

| `'·1st non-empty↓ ↓ ·2nd non-empty· →3rd non-empty·' ` | `" 1st non-empty\n2nd non-empty 3rd non-empty " ` |
| ------------------------------------------------------ | ------------------------------------------------- |
|                                                        |                                                   |

Legend:

- `nb-ns-single-in-line(n)`
-  

- `s-single-next-line(n)`

### 7.3.3. Plain Style

The *plain* (unquoted) style has no identifying [indicators](https://yaml.org/spec/1.2.2/#indicator-characters) and provides no form of escaping. It is therefore the most readable, most limited and most [context](https://yaml.org/spec/1.2.2/#context-c) sensitive [style](https://yaml.org/spec/1.2.2/#node-styles). In addition to a restricted character set, a plain scalar must not be empty or contain leading or trailing [white space](https://yaml.org/spec/1.2.2/#white-space-characters) characters. It is only possible to break a long plain line where a [space](https://yaml.org/spec/1.2.2/#white-space-characters) character is surrounded by non-[spaces](https://yaml.org/spec/1.2.2/#white-space-characters).

Plain scalars must not begin with most [indicators](https://yaml.org/spec/1.2.2/#indicator-characters), as this would cause ambiguity with other YAML constructs. However, the “`:`”, “`?`” and “`-`” [indicators](https://yaml.org/spec/1.2.2/#indicator-characters) may be used as the first character if followed by a non-[space](https://yaml.org/spec/1.2.2/#white-space-characters) “safe” character, as this causes no ambiguity.

```
[126] ns-plain-first(c) ::=
    (
        ns-char
      - c-indicator
    )
  | (
      (
          c-mapping-key       # '?'
        | c-mapping-value     # ':'
        | c-sequence-entry    # '-'
      )
      [ lookahead = ns-plain-safe(c) ]
    )
```

Plain scalars must never contain the “`: `” and “` #`” character combinations. Such combinations would cause ambiguity with [mapping](https://yaml.org/spec/1.2.2/#mapping) [key/value pairs](https://yaml.org/spec/1.2.2/#mapping) and [comments](https://yaml.org/spec/1.2.2/#comments). In addition, inside [flow collections](https://yaml.org/spec/1.2.2/#flow-collection-styles), or when used as [implicit keys](https://yaml.org/spec/1.2.2/#example-single-pair-explicit-entry), plain scalars must not contain the “`[`”, “`]`”, “`{`”, “`}`” and “`,`” characters. These characters would cause ambiguity with [flow collection](https://yaml.org/spec/1.2.2/#flow-collection-styles) structures.

```
[127]
ns-plain-safe(FLOW-OUT)  ::= ns-plain-safe-out
ns-plain-safe(FLOW-IN)   ::= ns-plain-safe-in
ns-plain-safe(BLOCK-KEY) ::= ns-plain-safe-out
ns-plain-safe(FLOW-KEY)  ::= ns-plain-safe-in
[128] ns-plain-safe-out ::=
  ns-char
[129] ns-plain-safe-in ::=
  ns-char - c-flow-indicator
[130] ns-plain-char(c) ::=
    (
        ns-plain-safe(c)
      - c-mapping-value    # ':'
      - c-comment          # '#'
    )
  | (
      [ lookbehind = ns-char ]
      c-comment          # '#'
    )
  | (
      c-mapping-value    # ':'
      [ lookahead = ns-plain-safe(c) ]
    )
```

**Example 7.10 Plain Characters**

| `# Outside flow collection: - ::vector - ": - ()" - Up, up, and away! - -123 - https://example.com/foo#bar # Inside flow collection: - [ ::vector,  ": - ()",  "Up, up and away!",  -123,  https://example.com/foo#bar ] ` | `[ "::vector",  ": - ()",  "Up, up, and away!",  -123,  "http://example.com/foo#bar",  [ "::vector",    ": - ()",    "Up, up, and away!",    -123,    "http://example.com/foo#bar" ] ] ` |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
|                                                              |                                                              |

Legend:

- `ns-plain-first(c)`
-  

- `ns-plain-char(c)`
-  

- `Not ns-plain-first(c)`
-  

- `Not ns-plain-char(c)`

Plain scalars are further restricted to a single line when contained inside an [implicit key](https://yaml.org/spec/1.2.2/#example-single-pair-explicit-entry).

```
[131]
ns-plain(n,FLOW-OUT)  ::= ns-plain-multi-line(n,FLOW-OUT)
ns-plain(n,FLOW-IN)   ::= ns-plain-multi-line(n,FLOW-IN)
ns-plain(n,BLOCK-KEY) ::= ns-plain-one-line(BLOCK-KEY)
ns-plain(n,FLOW-KEY)  ::= ns-plain-one-line(FLOW-KEY)
[132] nb-ns-plain-in-line(c) ::=
  (
    s-white*
    ns-plain-char(c)
  )*
[133] ns-plain-one-line(c) ::=
  ns-plain-first(c)
  nb-ns-plain-in-line(c)
```

**Example 7.11 Plain Implicit Keys**

| `implicit block key : [  implicit flow key : value, ] ` | `{ "implicit block key":  [ { "implicit flow key": "value" } ] } ` |
| ------------------------------------------------------- | ------------------------------------------------------------ |
|                                                         |                                                              |

Legend:

- `ns-plain-one-line(c)`

All leading and trailing [white space](https://yaml.org/spec/1.2.2/#white-space-characters) characters are excluded from the [content](https://yaml.org/spec/1.2.2/#nodes). Each continuation line must therefore contain at least one non-[space](https://yaml.org/spec/1.2.2/#white-space-characters) character. Empty lines, if any, are consumed as part of the [line folding](https://yaml.org/spec/1.2.2/#line-folding).

```
[134] s-ns-plain-next-line(n,c) ::=
  s-flow-folded(n)
  ns-plain-char(c)
  nb-ns-plain-in-line(c)
[135] ns-plain-multi-line(n,c) ::=
  ns-plain-one-line(c)
  s-ns-plain-next-line(n,c)*
```

**Example 7.12 Plain Lines**

| `1st non-empty↓ ↓ ·2nd non-empty· →3rd non-empty ` | `"1st non-empty\n2nd non-empty 3rd non-empty" ` |
| -------------------------------------------------- | ----------------------------------------------- |
|                                                    |                                                 |

Legend:

- `nb-ns-plain-in-line(c)`
-  

- `s-ns-plain-next-line(n,c)`

## 7.4. Flow Collection Styles

A *flow collection* may be nested within a [block collection](https://yaml.org/spec/1.2.2/#block-collection-styles) ([`FLOW-OUT` context]), nested within another flow collection ([`FLOW-IN` context]) or be a part of an [implicit key](https://yaml.org/spec/1.2.2/#example-single-pair-explicit-entry) ([`FLOW-KEY` context] or [`BLOCK-KEY` context]). Flow collection entries are terminated by the “`,`” indicator. The final “`,`” may be omitted. This does not cause ambiguity because flow collection entries can never be [completely empty](https://yaml.org/spec/1.2.2/#example-empty-content).

```
[136]
in-flow(n,FLOW-OUT)  ::= ns-s-flow-seq-entries(n,FLOW-IN)
in-flow(n,FLOW-IN)   ::= ns-s-flow-seq-entries(n,FLOW-IN)
in-flow(n,BLOCK-KEY) ::= ns-s-flow-seq-entries(n,FLOW-KEY)
in-flow(n,FLOW-KEY)  ::= ns-s-flow-seq-entries(n,FLOW-KEY)
```

### 7.4.1. Flow Sequences

*Flow sequence content* is denoted by surrounding “`[`” and “`]`” characters.

```
[137] c-flow-sequence(n,c) ::=
  c-sequence-start    # '['
  s-separate(n,c)?
  in-flow(n,c)?
  c-sequence-end      # ']'
```

Sequence entries are separated by a “`,`” character.

```
[138] ns-s-flow-seq-entries(n,c) ::=
  ns-flow-seq-entry(n,c)
  s-separate(n,c)?
  (
    c-collect-entry     # ','
    s-separate(n,c)?
    ns-s-flow-seq-entries(n,c)?
  )?
```

**Example 7.13 Flow Sequence**

| `- [ one, two, ] - [three ,four] ` | `[ [ "one",    "two" ],  [ "three",    "four" ] ] ` |
| ---------------------------------- | --------------------------------------------------- |
|                                    |                                                     |

Legend:

- `c-sequence-start c-sequence-end`
-  

- `ns-flow-seq-entry(n,c)`

Any [flow node](https://yaml.org/spec/1.2.2/#flow-nodes) may be used as a flow sequence entry. In addition, YAML provides a [compact notation](https://yaml.org/spec/1.2.2/#example-flow-mapping-adjacent-values) for the case where a flow sequence entry is a [mapping](https://yaml.org/spec/1.2.2/#mapping) with a [single key/value pair](https://yaml.org/spec/1.2.2/#mapping).

```
[139] ns-flow-seq-entry(n,c) ::=
  ns-flow-pair(n,c) | ns-flow-node(n,c)
```

**Example 7.14 Flow Sequence Entries**

| `[ "double quoted", 'single           quoted', plain text, [ nested ], single: pair, ] ` | `[ "double quoted",  "single quoted",  "plain text",  [ "nested" ],  { "single": "pair" } ] ` |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
|                                                              |                                                              |

Legend:

- `ns-flow-node(n,c)`
-  

- `ns-flow-pair(n,c)`

### 7.4.2. Flow Mappings

*Flow mappings* are denoted by surrounding “`{`” and “`}`” characters.

```
[140] c-flow-mapping(n,c) ::=
  c-mapping-start       # '{'
  s-separate(n,c)?
  ns-s-flow-map-entries(n,in-flow(c))?
  c-mapping-end         # '}'
```

Mapping entries are separated by a “`,`” character.

```
[141] ns-s-flow-map-entries(n,c) ::=
  ns-flow-map-entry(n,c)
  s-separate(n,c)?
  (
    c-collect-entry     # ','
    s-separate(n,c)?
    ns-s-flow-map-entries(n,c)?
  )?
```

**Example 7.15 Flow Mappings**

| `- { one : two , three: four , } - {five: six,seven : eight} ` | `[ { "one": "two",    "three": "four" },  { "five": "six",    "seven": "eight" } ] ` |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
|                                                              |                                                              |

Legend:

- `c-mapping-start c-mapping-end`
-  

- `ns-flow-map-entry(n,c)`

If the optional “`?`” mapping key indicator is specified, the rest of the entry may be [completely empty](https://yaml.org/spec/1.2.2/#example-empty-content).

```
[142] ns-flow-map-entry(n,c) ::=
    (
      c-mapping-key    # '?' (not followed by non-ws char)
      s-separate(n,c)
      ns-flow-map-explicit-entry(n,c)
    )
  | ns-flow-map-implicit-entry(n,c)
[143] ns-flow-map-explicit-entry(n,c) ::=
    ns-flow-map-implicit-entry(n,c)
  | (
      e-node    # ""
      e-node    # ""
    )
```

**Example 7.16 Flow Mapping Entries**

| `{ ? explicit: entry, implicit: entry, ?°° } ` | `{ "explicit": "entry",  "implicit": "entry",  null: null } ` |
| ---------------------------------------------- | ------------------------------------------------------------ |
|                                                |                                                              |

Legend:

- `ns-flow-map-explicit-entry(n,c)`
-  

- `ns-flow-map-implicit-entry(n,c)`
-  

- `e-node`

Normally, YAML insists the “`:`” mapping value indicator be [separated](https://yaml.org/spec/1.2.2/#separation-spaces) from the [value](https://yaml.org/spec/1.2.2/#nodes) by [white space](https://yaml.org/spec/1.2.2/#white-space-characters). A benefit of this restriction is that the “`:`” character can be used inside [plain scalars](https://yaml.org/spec/1.2.2/#plain-style), as long as it is not followed by [white space](https://yaml.org/spec/1.2.2/#white-space-characters). This allows for unquoted URLs and timestamps. It is also a potential source for confusion as “`a:1`” is a [plain scalar](https://yaml.org/spec/1.2.2/#plain-style) and not a [key/value pair](https://yaml.org/spec/1.2.2/#mapping).

Note that the [value](https://yaml.org/spec/1.2.2/#nodes) may be [completely empty](https://yaml.org/spec/1.2.2/#example-empty-content) since its existence is indicated by the “`:`”.

```
[144] ns-flow-map-implicit-entry(n,c) ::=
    ns-flow-map-yaml-key-entry(n,c)
  | c-ns-flow-map-empty-key-entry(n,c)
  | c-ns-flow-map-json-key-entry(n,c)
[145] ns-flow-map-yaml-key-entry(n,c) ::=
  ns-flow-yaml-node(n,c)
  (
      (
        s-separate(n,c)?
        c-ns-flow-map-separate-value(n,c)
      )
    | e-node    # ""
  )
[146] c-ns-flow-map-empty-key-entry(n,c) ::=
  e-node    # ""
  c-ns-flow-map-separate-value(n,c)
[147] c-ns-flow-map-separate-value(n,c) ::=
  c-mapping-value    # ':'
  [ lookahead ≠ ns-plain-safe(c) ]
  (
      (
        s-separate(n,c)
        ns-flow-node(n,c)
      )
    | e-node    # ""
  )
```

**Example 7.17 Flow Mapping Separate Values**

| `{ unquoted·:·"separate", https://foo.com, omitted value:°, °:·omitted key, } ` | `{ "unquoted": "separate",  "http://foo.com": null,  "omitted value": null,  null: "omitted key" } ` |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
|                                                              |                                                              |

Legend:

- `ns-flow-yaml-node(n,c)`
-  

- `e-node`
-  

- `c-ns-flow-map-separate-value(n,c)`

To ensure [JSON compatibility](https://yaml.org/spec/1.2.2/#yaml-directives), if a [key](https://yaml.org/spec/1.2.2/#nodes) inside a flow mapping is [JSON-like](https://yaml.org/spec/1.2.2/#flow-nodes), YAML allows the following [value](https://yaml.org/spec/1.2.2/#nodes) to be specified adjacent to the “`:`”. This causes no ambiguity, as all [JSON-like](https://yaml.org/spec/1.2.2/#flow-nodes) [keys](https://yaml.org/spec/1.2.2/#nodes) are surrounded by [indicators](https://yaml.org/spec/1.2.2/#indicator-characters). However, as this greatly reduces readability, YAML [processors](https://yaml.org/spec/1.2.2/#processes-and-models) should [separate](https://yaml.org/spec/1.2.2/#separation-spaces) the [value](https://yaml.org/spec/1.2.2/#nodes) from the “`:`” on output, even in this case.

```
[148] c-ns-flow-map-json-key-entry(n,c) ::=
  c-flow-json-node(n,c)
  (
      (
        s-separate(n,c)?
        c-ns-flow-map-adjacent-value(n,c)
      )
    | e-node    # ""
  )
[149] c-ns-flow-map-adjacent-value(n,c) ::=
  c-mapping-value          # ':'
  (
      (
        s-separate(n,c)?
        ns-flow-node(n,c)
      )
    | e-node    # ""
  )
```

**Example 7.18 Flow Mapping Adjacent Values**

| `{ "adjacent":value, "readable":·value, "empty":° } ` | `{ "adjacent": "value",  "readable": "value",  "empty": null } ` |
| ----------------------------------------------------- | ------------------------------------------------------------ |
|                                                       |                                                              |

Legend:

- `c-flow-json-node(n,c)`
-  

- `e-node`
-  

- `c-ns-flow-map-adjacent-value(n,c)`

A more compact notation is usable inside [flow sequences](https://yaml.org/spec/1.2.2/#flow-sequences), if the [mapping](https://yaml.org/spec/1.2.2/#mapping) contains a *single key/value pair*. This notation does not require the surrounding “`{`” and “`}`” characters. Note that it is not possible to specify any [node properties](https://yaml.org/spec/1.2.2/#node-properties) for the [mapping](https://yaml.org/spec/1.2.2/#mapping) in this case.

**Example 7.19 Single Pair Flow Mappings**

| `[ foo: bar ] ` | `[ { "foo": "bar" } ] ` |
| --------------- | ----------------------- |
|                 |                         |

Legend:

- `ns-flow-pair(n,c)`

If the “`?`” indicator is explicitly specified, [parsing](https://yaml.org/spec/1.2.2/#parsing-the-presentation-stream) is unambiguous and the syntax is identical to the general case.

```
[150] ns-flow-pair(n,c) ::=
    (
      c-mapping-key     # '?' (not followed by non-ws char)
      s-separate(n,c)
      ns-flow-map-explicit-entry(n,c)
    )
  | ns-flow-pair-entry(n,c)
```

**Example 7.20 Single Pair Explicit Entry**

| `[ ? foo bar : baz ] ` | `[ { "foo bar": "baz" } ] ` |
| ---------------------- | --------------------------- |
|                        |                             |

Legend:

- `ns-flow-map-explicit-entry(n,c)`

If the “`?`” indicator is omitted, [parsing](https://yaml.org/spec/1.2.2/#parsing-the-presentation-stream) needs to see past the *implicit key* to recognize it as such. To limit the amount of lookahead required, the “`:`” indicator must appear at most 1024 Unicode characters beyond the start of the [key](https://yaml.org/spec/1.2.2/#nodes). In addition, the [key](https://yaml.org/spec/1.2.2/#nodes) is restricted to a single line.

Note that YAML allows arbitrary [nodes](https://yaml.org/spec/1.2.2/#nodes) to be used as [keys](https://yaml.org/spec/1.2.2/#nodes). In particular, a [key](https://yaml.org/spec/1.2.2/#nodes) may be a [sequence](https://yaml.org/spec/1.2.2/#sequence) or a [mapping](https://yaml.org/spec/1.2.2/#mapping). Thus, without the above restrictions, practical one-pass [parsing](https://yaml.org/spec/1.2.2/#parsing-the-presentation-stream) would have been impossible to implement.

```
[151] ns-flow-pair-entry(n,c) ::=
    ns-flow-pair-yaml-key-entry(n,c)
  | c-ns-flow-map-empty-key-entry(n,c)
  | c-ns-flow-pair-json-key-entry(n,c)
[152] ns-flow-pair-yaml-key-entry(n,c) ::=
  ns-s-implicit-yaml-key(FLOW-KEY)
  c-ns-flow-map-separate-value(n,c)
[153] c-ns-flow-pair-json-key-entry(n,c) ::=
  c-s-implicit-json-key(FLOW-KEY)
  c-ns-flow-map-adjacent-value(n,c)
[154] ns-s-implicit-yaml-key(c) ::=
  ns-flow-yaml-node(0,c)
  s-separate-in-line?
  /* At most 1024 characters altogether */
[155] c-s-implicit-json-key(c) ::=
  c-flow-json-node(0,c)
  s-separate-in-line?
  /* At most 1024 characters altogether */
```

**Example 7.21 Single Pair Implicit Entries**

| `- [ YAML·: separate ] - [ °: empty key entry ] - [ {JSON: like}:adjacent ] ` | `[ [ { "YAML": "separate" } ],  [ { null: "empty key entry" } ],  [ { { "JSON": "like" }: "adjacent" } ] ] ` |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
|                                                              |                                                              |

Legend:

- `ns-s-implicit-yaml-key`
-  

- `e-node`
-  

- `c-s-implicit-json-key`
-  

- `Value`

**Example 7.22 Invalid Implicit Keys**

| `[ foo bar: invalid, "foo_...>1K characters..._bar": invalid ] ` | `ERROR: - The foo bar key spans multiple lines - The foo...bar key is too long ` |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
|                                                              |                                                              |

## 7.5. Flow Nodes

*JSON-like* [flow styles](https://yaml.org/spec/1.2.2/#flow-style-productions) all have explicit start and end [indicators](https://yaml.org/spec/1.2.2/#indicator-characters). The only [flow style](https://yaml.org/spec/1.2.2/#flow-style-productions) that does not have this property is the [plain scalar](https://yaml.org/spec/1.2.2/#plain-style). Note that none of the “JSON-like” styles is actually acceptable by JSON. Even the [double-quoted style](https://yaml.org/spec/1.2.2/#double-quoted-style) is a superset of the JSON string format.

```
[156] ns-flow-yaml-content(n,c) ::=
  ns-plain(n,c)
[157] c-flow-json-content(n,c) ::=
    c-flow-sequence(n,c)
  | c-flow-mapping(n,c)
  | c-single-quoted(n,c)
  | c-double-quoted(n,c)
[158] ns-flow-content(n,c) ::=
    ns-flow-yaml-content(n,c)
  | c-flow-json-content(n,c)
```

**Example 7.23 Flow Content**

| `- [ a, b ] - { a: b } - "a" - 'b' - c ` | `[ [ "a", "b" ],  { "a": "b" },  "a",  "b",  "c" ] ` |
| ---------------------------------------- | ---------------------------------------------------- |
|                                          |                                                      |

Legend:

- `c-flow-json-content(n,c)`
-  

- `ns-flow-yaml-content(n,c)`

A complete [flow](https://yaml.org/spec/1.2.2/#flow-style-productions) [node](https://yaml.org/spec/1.2.2/#nodes) also has optional [node properties](https://yaml.org/spec/1.2.2/#node-properties), except for [alias nodes](https://yaml.org/spec/1.2.2/#alias-nodes) which refer to the [anchored](https://yaml.org/spec/1.2.2/#anchors-and-aliases) [node properties](https://yaml.org/spec/1.2.2/#node-properties).

```
[159] ns-flow-yaml-node(n,c) ::=
    c-ns-alias-node
  | ns-flow-yaml-content(n,c)
  | (
      c-ns-properties(n,c)
      (
          (
            s-separate(n,c)
            ns-flow-yaml-content(n,c)
          )
        | e-scalar
      )
    )
[160] c-flow-json-node(n,c) ::=
  (
    c-ns-properties(n,c)
    s-separate(n,c)
  )?
  c-flow-json-content(n,c)
[161] ns-flow-node(n,c) ::=
    c-ns-alias-node
  | ns-flow-content(n,c)
  | (
      c-ns-properties(n,c)
      (
        (
          s-separate(n,c)
          ns-flow-content(n,c)
        )
        | e-scalar
      )
    )
```

**Example 7.24 Flow Nodes**

| `- !!str "a" - 'b' - &anchor "c" - *anchor - !!str° ` | `[ "a",  "b",  "c",  "c",  "" ] ` |
| ----------------------------------------------------- | --------------------------------- |
|                                                       |                                   |

Legend:

- `c-flow-json-node(n,c)`
- `ns-flow-yaml-node(n,c)`