# 块风格

> 本文按照YAML官方文档1.2.2版本翻译总结而成
>
> https://yaml.org/spec/1.2.2/#chapter-8-block-style-productions

YAML’s *block styles* employ [indentation](https://yaml.org/spec/1.2.2/#indentation-spaces) rather than [indicators](https://yaml.org/spec/1.2.2/#indicator-characters) to denote structure. This results in a more human readable (though less compact) notation.

## 8.1. Block Scalar Styles

YAML provides two *block scalar styles*, [literal](https://yaml.org/spec/1.2.2/#literal-style) and [folded](https://yaml.org/spec/1.2.2/#line-folding). Each provides a different trade-off between readability and expressive power.

### 8.1.1. Block Scalar Headers

[Block scalars](https://yaml.org/spec/1.2.2/#block-scalar-styles) are controlled by a few [indicators](https://yaml.org/spec/1.2.2/#indicator-characters) given in a *header* preceding the [content](https://yaml.org/spec/1.2.2/#nodes) itself. This header is followed by a non-content [line break](https://yaml.org/spec/1.2.2/#line-break-characters) with an optional [comment](https://yaml.org/spec/1.2.2/#comments). This is the only case where a [comment](https://yaml.org/spec/1.2.2/#comments) must not be followed by additional [comment](https://yaml.org/spec/1.2.2/#comments) lines.

> Note: See [Production Parameters](https://yaml.org/spec/1.2.2/#production-parameters) for the definition of the `t` variable.

```
[162] c-b-block-header(t) ::=
  (
      (
        c-indentation-indicator
        c-chomping-indicator(t)
      )
    | (
        c-chomping-indicator(t)
        c-indentation-indicator
      )
  )
  s-b-comment
```

**Example 8.1 Block Scalar Header**

| `- | # Empty header↓ literal - >1 # Indentation indicator↓ ·folded - |+ # Chomping indicator↓ keep - >1- # Both indicators↓ ·strip ` | `[ "literal\n",  " folded\n",  "keep\n\n",  " strip" ] ` |
| ------------------------------------------------------------ | -------------------------------------------------------- |
|                                                              |                                                          |

Legend:

- `c-b-block-header(t)`

#### 8.1.1.1. Block Indentation Indicator

Every block scalar has a *content indentation level*. The content of the block scalar excludes a number of leading [spaces](https://yaml.org/spec/1.2.2/#white-space-characters) on each line up to the content indentation level.

If a block scalar has an *indentation indicator*, then the content indentation level of the block scalar is equal to the indentation level of the block scalar plus the integer value of the indentation indicator character.

If no indentation indicator is given, then the content indentation level is equal to the number of leading [spaces](https://yaml.org/spec/1.2.2/#white-space-characters) on the first non-[empty line](https://yaml.org/spec/1.2.2/#empty-lines) of the contents. If there is no non-[empty line](https://yaml.org/spec/1.2.2/#empty-lines) then the content indentation level is equal to the number of spaces on the longest line.

It is an error if any non-[empty line](https://yaml.org/spec/1.2.2/#empty-lines) does not begin with a number of spaces greater than or equal to the content indentation level.

It is an error for any of the leading [empty lines](https://yaml.org/spec/1.2.2/#empty-lines) to contain more [spaces](https://yaml.org/spec/1.2.2/#white-space-characters) than the first non-[empty line](https://yaml.org/spec/1.2.2/#empty-lines).

A YAML [processor](https://yaml.org/spec/1.2.2/#processes-and-models) should only emit an explicit indentation indicator for cases where detection will fail.

```
[163] c-indentation-indicator ::=
  [x31-x39]    # 1-9
```

**Example 8.2 Block Indentation Indicator**

| `- |° ·detected - >° · ·· ··# detected - |1 ··explicit - >° ·→ ·detected ` | `[ "detected\n",  "\n\n# detected\n",  " explicit\n",  "\t\ndetected\n" ] ` |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
|                                                              |                                                              |

Legend:

- `c-indentation-indicator`
-  

- `s-indent(n)`

**Example 8.3 Invalid Block Scalar Indentation Indicators**

| `- | ·· ·text - > ··text ·text - |2 ·text ` | `ERROR: - A leading all-space line must  not have too many spaces. - A following text line must  not be less indented. - The text is less indented  than the indicated level. ` |
| ------------------------------------------- | ------------------------------------------------------------ |
|                                             |                                                              |

#### 8.1.1.2. Block Chomping Indicator

*Chomping* controls how final [line breaks](https://yaml.org/spec/1.2.2/#line-break-characters) and trailing [empty lines](https://yaml.org/spec/1.2.2/#empty-lines) are interpreted. YAML provides three chomping methods:

- Strip

  *Stripping* is specified by the “`-`” chomping indicator. In this case, the final [line break](https://yaml.org/spec/1.2.2/#line-break-characters) and any trailing [empty lines](https://yaml.org/spec/1.2.2/#empty-lines) are excluded from the [scalar’s content](https://yaml.org/spec/1.2.2/#scalar).

- Clip

  *Clipping* is the default behavior used if no explicit chomping indicator is specified. In this case, the final [line break](https://yaml.org/spec/1.2.2/#line-break-characters) character is preserved in the [scalar’s content](https://yaml.org/spec/1.2.2/#scalar). However, any trailing [empty lines](https://yaml.org/spec/1.2.2/#empty-lines) are excluded from the [scalar’s content](https://yaml.org/spec/1.2.2/#scalar).

- Keep

  *Keeping* is specified by the “`+`” chomping indicator. In this case, the final [line break](https://yaml.org/spec/1.2.2/#line-break-characters) and any trailing [empty lines](https://yaml.org/spec/1.2.2/#empty-lines) are considered to be part of the [scalar’s content](https://yaml.org/spec/1.2.2/#scalar). These additional lines are not subject to [folding](https://yaml.org/spec/1.2.2/#line-folding).

The chomping method used is a [presentation detail](https://yaml.org/spec/1.2.2/#presenting-the-serialization-tree) and must not be used to convey [content](https://yaml.org/spec/1.2.2/#nodes) information.

```
[164]
c-chomping-indicator(STRIP) ::= '-'
c-chomping-indicator(KEEP)  ::= '+'
c-chomping-indicator(CLIP)  ::= ""
```

The interpretation of the final [line break](https://yaml.org/spec/1.2.2/#line-break-characters) of a [block scalar](https://yaml.org/spec/1.2.2/#block-scalar-styles) is controlled by the chomping indicator specified in the [block scalar header](https://yaml.org/spec/1.2.2/#block-scalar-headers).

```
[165]
b-chomped-last(STRIP) ::= b-non-content  | <end-of-input>
b-chomped-last(CLIP)  ::= b-as-line-feed | <end-of-input>
b-chomped-last(KEEP)  ::= b-as-line-feed | <end-of-input>
```

**Example 8.4 Chomping Final Line Break**

| `strip: | -  text↓ clip: | text↓ keep: | +  text↓ ` | `{ "strip": "text",  "clip": "text\n",  "keep": "text\n" } ` |
| ------- | -------------- | ----------- | ---------- | ------------------------------------------------------------ |
|         |                |             |            |                                                              |

Legend:

- `b-non-content`
-  

- `b-as-line-feed`

The interpretation of the trailing [empty lines](https://yaml.org/spec/1.2.2/#empty-lines) following a [block scalar](https://yaml.org/spec/1.2.2/#block-scalar-styles) is also controlled by the chomping indicator specified in the [block scalar header](https://yaml.org/spec/1.2.2/#block-scalar-headers).

```
[166]
l-chomped-empty(n,STRIP) ::= l-strip-empty(n)
l-chomped-empty(n,CLIP)  ::= l-strip-empty(n)
l-chomped-empty(n,KEEP)  ::= l-keep-empty(n)
[167] l-strip-empty(n) ::=
  (
    s-indent-less-or-equal(n)
    b-non-content
  )*
  l-trail-comments(n)?
[168] l-keep-empty(n) ::=
  l-empty(n,BLOCK-IN)*
  l-trail-comments(n)?
```

Explicit [comment](https://yaml.org/spec/1.2.2/#comments) lines may follow the trailing [empty lines](https://yaml.org/spec/1.2.2/#empty-lines). To prevent ambiguity, the first such [comment](https://yaml.org/spec/1.2.2/#comments) line must be less [indented](https://yaml.org/spec/1.2.2/#indentation-spaces) than the [block scalar content](https://yaml.org/spec/1.2.2/#block-scalar-styles). Additional [comment](https://yaml.org/spec/1.2.2/#comments) lines, if any, are not so restricted. This is the only case where the [indentation](https://yaml.org/spec/1.2.2/#indentation-spaces) of [comment](https://yaml.org/spec/1.2.2/#comments) lines is constrained.

```
[169] l-trail-comments(n) ::=
  s-indent-less-than(n)
  c-nb-comment-text
  b-comment
  l-comment*
```

**Example 8.5 Chomping Trailing Lines**

| `# Strip  # Comments: strip: |-  # text↓ ··⇓ ·# Clip ··# comments: ↓ clip: |  # text↓ ·↓ ·# Keep ··# comments: ↓ keep: |+  # text↓ ↓ ·# Trail ··# comments. ` | `{ "strip": "# text",  "clip": "# text\n",  "keep": "# text\n\n" } ` |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
|                                                              |                                                              |

Legend:

- `l-strip-empty(n)`
-  

- `l-keep-empty(n)`
-  

- `l-trail-comments(n)`

If a [block scalar](https://yaml.org/spec/1.2.2/#block-scalar-styles) consists only of [empty lines](https://yaml.org/spec/1.2.2/#empty-lines), then these lines are considered as trailing lines and hence are affected by chomping.

**Example 8.6 Empty Scalar Chomping**

| `strip: >- ↓ clip: > ↓ keep: |+ ↓ ` | `{ "strip": "",  "clip": "",  "keep": "\n" } ` |
| ----------------------------------- | ---------------------------------------------- |
|                                     |                                                |

Legend:

- `l-strip-empty(n)`
-  

- `l-keep-empty(n)`

### 8.1.2. Literal Style

The *literal style* is denoted by the “`|`” indicator. It is the simplest, most restricted and most readable [scalar style](https://yaml.org/spec/1.2.2/#node-styles).

```
[170] c-l+literal(n) ::=
  c-literal                # '|'
  c-b-block-header(t)
  l-literal-content(n+m,t)
```

**Example 8.7 Literal Scalar**

| `|↓ ·literal↓ ·→text↓ ↓ ` | `"literal\n\ttext\n" ` |
| ------------------------- | ---------------------- |
|                           |                        |

Legend:

- `c-l+literal(n)`

Inside literal scalars, all ([indented](https://yaml.org/spec/1.2.2/#indentation-spaces)) characters are considered to be [content](https://yaml.org/spec/1.2.2/#nodes), including [white space](https://yaml.org/spec/1.2.2/#white-space-characters) characters. Note that all [line break](https://yaml.org/spec/1.2.2/#line-break-characters) characters are [normalized](https://yaml.org/spec/1.2.2/#line-break-characters). In addition, [empty lines](https://yaml.org/spec/1.2.2/#empty-lines) are not [folded](https://yaml.org/spec/1.2.2/#line-folding), though final [line breaks](https://yaml.org/spec/1.2.2/#line-break-characters) and trailing [empty lines](https://yaml.org/spec/1.2.2/#empty-lines) are [chomped](https://yaml.org/spec/1.2.2/#block-chomping-indicator).

There is no way to escape characters inside literal scalars. This restricts them to [printable](https://yaml.org/spec/1.2.2/#character-set) characters. In addition, there is no way to break a long literal line.

```
[171] l-nb-literal-text(n) ::=
  l-empty(n,BLOCK-IN)*
  s-indent(n) nb-char+
[172] b-nb-literal-next(n) ::=
  b-as-line-feed
  l-nb-literal-text(n)
[173] l-literal-content(n,t) ::=
  (
    l-nb-literal-text(n)
    b-nb-literal-next(n)*
    b-chomped-last(t)
  )?
  l-chomped-empty(n,t)
```

**Example 8.8 Literal Content**

| `| · ·· ··literal↓ ···↓ ·· ··text↓ ↓ ·# Comment ` | `"\n\nliteral\n·\n\ntext\n" ` |
| ------------------------------------------------- | ----------------------------- |
|                                                   |                               |

Legend:

- `l-nb-literal-text(n)`
-  

- `b-nb-literal-next(n)`
-  

- `b-chomped-last(t)`
-  

- `l-chomped-empty(n,t)`

### 8.1.3. Folded Style

The *folded style* is denoted by the “`>`” indicator. It is similar to the [literal style](https://yaml.org/spec/1.2.2/#literal-style); however, folded scalars are subject to [line folding](https://yaml.org/spec/1.2.2/#line-folding).

```
[174] c-l+folded(n) ::=
  c-folded                 # '>'
  c-b-block-header(t)
  l-folded-content(n+m,t)
```

**Example 8.9 Folded Scalar**

| `>↓ ·folded↓ ·text↓ ↓ ` | `"folded text\n" ` |
| ----------------------- | ------------------ |
|                         |                    |

Legend:

- `c-l+folded(n)`

[Folding](https://yaml.org/spec/1.2.2/#line-folding) allows long lines to be broken anywhere a single [space](https://yaml.org/spec/1.2.2/#white-space-characters) character separates two non-[space](https://yaml.org/spec/1.2.2/#white-space-characters) characters.

```
[175] s-nb-folded-text(n) ::=
  s-indent(n)
  ns-char
  nb-char*
[176] l-nb-folded-lines(n) ::=
  s-nb-folded-text(n)
  (
    b-l-folded(n,BLOCK-IN)
    s-nb-folded-text(n)
  )*
```

**Example 8.10 Folded Lines**

| `> ·folded↓ ·line↓ ↓ ·next ·line↓   * bullet    * list   * lines ·last↓ ·line↓ # Comment ` | `"\nfolded line\nnext line\n  \ * bullet\n \n  * list\n  \ * lines\n\nlast line\n" ` |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
|                                                              |                                                              |

Legend:

- `l-nb-folded-lines(n)`
-  

- `s-nb-folded-text(n)`

(The following three examples duplicate this example, each highlighting different productions.)

Lines starting with [white space](https://yaml.org/spec/1.2.2/#white-space-characters) characters (*more-indented* lines) are not [folded](https://yaml.org/spec/1.2.2/#line-folding).

```
[177] s-nb-spaced-text(n) ::=
  s-indent(n)
  s-white
  nb-char*
[178] b-l-spaced(n) ::=
  b-as-line-feed
  l-empty(n,BLOCK-IN)*
[179] l-nb-spaced-lines(n) ::=
  s-nb-spaced-text(n)
  (
    b-l-spaced(n)
    s-nb-spaced-text(n)
  )*
```

**Example 8.11 More Indented Lines**

| `>  folded line  next line ···* bullet↓ ↓ ···* list↓ ···* lines↓  last line # Comment ` | `"\nfolded line\nnext line\n  \ * bullet\n \n  * list\n  \ * lines\n\nlast line\n" ` |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
|                                                              |                                                              |

Legend:

- `l-nb-spaced-lines(n)`
-  

- `s-nb-spaced-text(n)`

[Line breaks](https://yaml.org/spec/1.2.2/#line-break-characters) and [empty lines](https://yaml.org/spec/1.2.2/#empty-lines) separating folded and more-indented lines are also not [folded](https://yaml.org/spec/1.2.2/#line-folding).

```
[180] l-nb-same-lines(n) ::=
  l-empty(n,BLOCK-IN)*
  (
      l-nb-folded-lines(n)
    | l-nb-spaced-lines(n)
  )
[181] l-nb-diff-lines(n) ::=
  l-nb-same-lines(n)
  (
    b-as-line-feed
    l-nb-same-lines(n)
  )*
```

**Example 8.12 Empty Separation Lines**

| `> ↓ folded line↓ ↓ next line↓   * bullet    * list   * lines↓ ↓ last line # Comment ` | `"\nfolded line\nnext line\n  \ * bullet\n \n  * list\n  \ * lines\n\nlast line\n" ` |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
|                                                              |                                                              |

Legend:

- `b-as-line-feed`
-  

- `(separation) l-empty(n,c)`

The final [line break](https://yaml.org/spec/1.2.2/#line-break-characters) and trailing [empty lines](https://yaml.org/spec/1.2.2/#empty-lines) if any, are subject to [chomping](https://yaml.org/spec/1.2.2/#block-chomping-indicator) and are never [folded](https://yaml.org/spec/1.2.2/#line-folding).

```
[182] l-folded-content(n,t) ::=
  (
    l-nb-diff-lines(n)
    b-chomped-last(t)
  )?
  l-chomped-empty(n,t)
```

**Example 8.13 Final Empty Lines**

| `>  folded line  next line   * bullet    * list   * lines  last line↓ ↓ # Comment ` | `"\nfolded line\nnext line\n  \ * bullet\n \n  * list\n  \ * lines\n\nlast line\n" ` |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
|                                                              |                                                              |

Legend:

- `b-chomped-last(t)`
-  

- `l-chomped-empty(n,t)`

## 8.2. Block Collection Styles

For readability, *block collections styles* are not denoted by any [indicator](https://yaml.org/spec/1.2.2/#indicator-characters). Instead, YAML uses a lookahead method, where a block collection is distinguished from a [plain scalar](https://yaml.org/spec/1.2.2/#plain-style) only when a [key/value pair](https://yaml.org/spec/1.2.2/#mapping) or a [sequence entry](https://yaml.org/spec/1.2.2/#block-sequences) is seen.

### 8.2.1. Block Sequences

A *block sequence* is simply a series of [nodes](https://yaml.org/spec/1.2.2/#nodes), each denoted by a leading “`-`” indicator. The “`-`” indicator must be [separated](https://yaml.org/spec/1.2.2/#separation-spaces) from the [node](https://yaml.org/spec/1.2.2/#nodes) by [white space](https://yaml.org/spec/1.2.2/#white-space-characters). This allows “`-`” to be used as the first character in a [plain scalar](https://yaml.org/spec/1.2.2/#plain-style) if followed by a non-space character (e.g. “`-42`”).

```
[183] l+block-sequence(n) ::=
  (
    s-indent(n+1+m)
    c-l-block-seq-entry(n+1+m)
  )+
[184] c-l-block-seq-entry(n) ::=
  c-sequence-entry    # '-'
  [ lookahead ≠ ns-char ]
  s-l+block-indented(n,BLOCK-IN)
```

**Example 8.14 Block Sequence**

| `block sequence: ··- one↓  - two : three↓ ` | `{ "block sequence": [    "one",    { "two": "three" } ] } ` |
| ------------------------------------------- | ------------------------------------------------------------ |
|                                             |                                                              |

Legend:

- `c-l-block-seq-entry(n)`
-  

- `auto-detected s-indent(n)`

The entry [node](https://yaml.org/spec/1.2.2/#nodes) may be either [completely empty](https://yaml.org/spec/1.2.2/#example-empty-content), be a nested [block node](https://yaml.org/spec/1.2.2/#block-nodes) or use a *compact in-line notation*. The compact notation may be used when the entry is itself a nested [block collection](https://yaml.org/spec/1.2.2/#block-collection-styles). In this case, both the “`-`” indicator and the following [spaces](https://yaml.org/spec/1.2.2/#white-space-characters) are considered to be part of the [indentation](https://yaml.org/spec/1.2.2/#indentation-spaces) of the nested [collection](https://yaml.org/spec/1.2.2/#collections). Note that it is not possible to specify [node properties](https://yaml.org/spec/1.2.2/#node-properties) for such a [collection](https://yaml.org/spec/1.2.2/#collections).

```
[185] s-l+block-indented(n,c) ::=
    (
      s-indent(m)
      (
          ns-l-compact-sequence(n+1+m)
        | ns-l-compact-mapping(n+1+m)
      )
    )
  | s-l+block-node(n,c)
  | (
      e-node    # ""
      s-l-comments
    )
[186] ns-l-compact-sequence(n) ::=
  c-l-block-seq-entry(n)
  (
    s-indent(n)
    c-l-block-seq-entry(n)
  )*
```

**Example 8.15 Block Sequence Entry Types**

| `-° # Empty - | block node -·- one # Compact ··- two # sequence - one: two # Compact mapping ` | `[ null,  "block node\n",  [ "one", "two" ],  { "one": "two" } ] ` |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
|                                                              |                                                              |

Legend:

- `Empty`
-  

- `s-l+block-node(n,c)`
-  

- `ns-l-compact-sequence(n)`
-  

- `ns-l-compact-mapping(n)`

### 8.2.2. Block Mappings

A *Block mapping* is a series of entries, each [presenting](https://yaml.org/spec/1.2.2/#presenting-the-serialization-tree) a [key/value pair](https://yaml.org/spec/1.2.2/#mapping).

```
[187] l+block-mapping(n) ::=
  (
    s-indent(n+1+m)
    ns-l-block-map-entry(n+1+m)
  )+
```

**Example 8.16 Block Mappings**

| `block mapping: ·key: value↓ ` | `{ "block mapping": {    "key": "value" } } ` |
| ------------------------------ | --------------------------------------------- |
|                                |                                               |

Legend:

- `ns-l-block-map-entry(n)`
-  

- `auto-detected s-indent(n)`

If the “`?`” indicator is specified, the optional value node must be specified on a separate line, denoted by the “`:`” indicator. Note that YAML allows here the same [compact in-line notation](https://yaml.org/spec/1.2.2/#example-block-sequence) described above for [block sequence](https://yaml.org/spec/1.2.2/#block-sequences) entries.

```
[188] ns-l-block-map-entry(n) ::=
    c-l-block-map-explicit-entry(n)
  | ns-l-block-map-implicit-entry(n)
[189] c-l-block-map-explicit-entry(n) ::=
  c-l-block-map-explicit-key(n)
  (
      l-block-map-explicit-value(n)
    | e-node                        # ""
  )
[190] c-l-block-map-explicit-key(n) ::=
  c-mapping-key                     # '?' (not followed by non-ws char)
  s-l+block-indented(n,BLOCK-OUT)
[191] l-block-map-explicit-value(n) ::=
  s-indent(n)
  c-mapping-value                   # ':' (not followed by non-ws char)
  s-l+block-indented(n,BLOCK-OUT)
```

**Example 8.17 Explicit Block Mapping Entries**

| `? explicit key # Empty value↓° ? |  block key↓ :·- one # Explicit compact ··- two # block value↓ ` | `{ "explicit key": null,  "block key\n": [    "one",    "two" ] } ` |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
|                                                              |                                                              |

Legend:

- `c-l-block-map-explicit-key(n)`
-  

- `l-block-map-explicit-value(n)`
-  

- `e-node`

If the “`?`” indicator is omitted, [parsing](https://yaml.org/spec/1.2.2/#parsing-the-presentation-stream) needs to see past the [implicit key](https://yaml.org/spec/1.2.2/#example-single-pair-explicit-entry), in the same way as in the [single key/value pair](https://yaml.org/spec/1.2.2/#mapping) [flow mapping](https://yaml.org/spec/1.2.2/#flow-mappings). Hence, such [keys](https://yaml.org/spec/1.2.2/#nodes) are subject to the same restrictions; they are limited to a single line and must not span more than 1024 Unicode characters.

```
[192] ns-l-block-map-implicit-entry(n) ::=
  (
      ns-s-block-map-implicit-key
    | e-node    # ""
  )
  c-l-block-map-implicit-value(n)
[193] ns-s-block-map-implicit-key ::=
    c-s-implicit-json-key(BLOCK-KEY)
  | ns-s-implicit-yaml-key(BLOCK-KEY)
```

In this case, the [value](https://yaml.org/spec/1.2.2/#nodes) may be specified on the same line as the [implicit key](https://yaml.org/spec/1.2.2/#example-single-pair-explicit-entry). Note however that in block mappings the [value](https://yaml.org/spec/1.2.2/#nodes) must never be adjacent to the “`:`”, as this greatly reduces readability and is not required for [JSON compatibility](https://yaml.org/spec/1.2.2/#yaml-directives) (unlike the case in [flow mappings](https://yaml.org/spec/1.2.2/#flow-mappings)).

There is no compact notation for in-line [values](https://yaml.org/spec/1.2.2/#nodes). Also, while both the [implicit key](https://yaml.org/spec/1.2.2/#example-single-pair-explicit-entry) and the [value](https://yaml.org/spec/1.2.2/#nodes) following it may be empty, the “`:`” indicator is mandatory. This prevents a potential ambiguity with multi-line [plain scalars](https://yaml.org/spec/1.2.2/#plain-style).

```
[194] c-l-block-map-implicit-value(n) ::=
  c-mapping-value           # ':' (not followed by non-ws char)
  (
      s-l+block-node(n,BLOCK-OUT)
    | (
        e-node    # ""
        s-l-comments
      )
  )
```

**Example 8.18 Implicit Block Mapping Entries**

| `plain key: in-line value °:° # Both empty "quoted key": - entry ` | `{ "plain key": "in-line value",  null: null,  "quoted key": [ "entry" ] } ` |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
|                                                              |                                                              |

Legend:

- `ns-s-block-map-implicit-key`
-  

- `c-l-block-map-implicit-value(n)`

A [compact in-line notation](https://yaml.org/spec/1.2.2/#example-block-sequence) is also available. This compact notation may be nested inside [block sequences](https://yaml.org/spec/1.2.2/#block-sequences) and explicit block mapping entries. Note that it is not possible to specify [node properties](https://yaml.org/spec/1.2.2/#node-properties) for such a nested mapping.

```
[195] ns-l-compact-mapping(n) ::=
  ns-l-block-map-entry(n)
  (
    s-indent(n)
    ns-l-block-map-entry(n)
  )*
```

**Example 8.19 Compact Block Mappings**

| `- sun: yellow↓ - ? earth: blue↓  : moon: white↓ ` | `[ { "sun": "yellow" },  { { "earth": "blue" }:      { "moon": "white" } } ] ` |
| -------------------------------------------------- | ------------------------------------------------------------ |
|                                                    |                                                              |

Legend:

- `ns-l-compact-mapping(n)`

### 8.2.3. Block Nodes

YAML allows [flow nodes](https://yaml.org/spec/1.2.2/#flow-nodes) to be embedded inside [block collections](https://yaml.org/spec/1.2.2/#block-collection-styles) (but not vice-versa). [Flow nodes](https://yaml.org/spec/1.2.2/#flow-nodes) must be [indented](https://yaml.org/spec/1.2.2/#indentation-spaces) by at least one more [space](https://yaml.org/spec/1.2.2/#white-space-characters) than the parent [block collection](https://yaml.org/spec/1.2.2/#block-collection-styles). Note that [flow nodes](https://yaml.org/spec/1.2.2/#flow-nodes) may begin on a following line.

It is at this point that [parsing](https://yaml.org/spec/1.2.2/#parsing-the-presentation-stream) needs to distinguish between a [plain scalar](https://yaml.org/spec/1.2.2/#plain-style) and an [implicit key](https://yaml.org/spec/1.2.2/#example-single-pair-explicit-entry) starting a nested [block mapping](https://yaml.org/spec/1.2.2/#block-mappings).

```
[196] s-l+block-node(n,c) ::=
    s-l+block-in-block(n,c)
  | s-l+flow-in-block(n)
[197] s-l+flow-in-block(n) ::=
  s-separate(n+1,FLOW-OUT)
  ns-flow-node(n+1,FLOW-OUT)
  s-l-comments
```

**Example 8.20 Block Node Types**

| `-↓ ··"flow in block"↓ -·> Block scalar↓ -·!!map # Block collection  foo : bar↓ ` | `[ "flow in block",  "Block scalar\n",  { "foo": "bar" } ] ` |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
|                                                              |                                                              |

Legend:

- `s-l+flow-in-block(n)`
-  

- `s-l+block-in-block(n,c)`

The block [node’s properties](https://yaml.org/spec/1.2.2/#node-properties) may span across several lines. In this case, they must be [indented](https://yaml.org/spec/1.2.2/#indentation-spaces) by at least one more [space](https://yaml.org/spec/1.2.2/#white-space-characters) than the [block collection](https://yaml.org/spec/1.2.2/#block-collection-styles), regardless of the [indentation](https://yaml.org/spec/1.2.2/#indentation-spaces) of the [block collection](https://yaml.org/spec/1.2.2/#block-collection-styles) entries.

```
[198] s-l+block-in-block(n,c) ::=
    s-l+block-scalar(n,c)
  | s-l+block-collection(n,c)
[199] s-l+block-scalar(n,c) ::=
  s-separate(n+1,c)
  (
    c-ns-properties(n+1,c)
    s-separate(n+1,c)
  )?
  (
      c-l+literal(n)
    | c-l+folded(n)
  )
```

**Example 8.21 Block Scalar Nodes**

| `literal: |2 ··value folded:↓ ···!foo ··>1 ·value ` | `{ "literal": "value",  "folded": !<!foo> "value" } ` |
| --------------------------------------------------- | ----------------------------------------------------- |
|                                                     |                                                       |

Legend:

- `c-l+literal(n)`
-  

- `c-l+folded(n)`

Since people perceive the “`-`” indicator as [indentation](https://yaml.org/spec/1.2.2/#indentation-spaces), nested [block sequences](https://yaml.org/spec/1.2.2/#block-sequences) may be [indented](https://yaml.org/spec/1.2.2/#indentation-spaces) by one less [space](https://yaml.org/spec/1.2.2/#white-space-characters) to compensate, except, of course, if nested inside another [block sequence](https://yaml.org/spec/1.2.2/#block-sequences) ([`BLOCK-OUT` context] versus [`BLOCK-IN` context]).

```
[200] s-l+block-collection(n,c) ::=
  (
    s-separate(n+1,c)
    c-ns-properties(n+1,c)
  )?
  s-l-comments
  (
      seq-space(n,c)
    | l+block-mapping(n)
  )
[201] seq-space(n,BLOCK-OUT) ::= l+block-sequence(n-1)
    seq-space(n,BLOCK-IN)  ::= l+block-sequence(n)
```

**Example 8.22 Block Collection Nodes**

| `sequence: !!seq - entry - !!seq - nested mapping: !!map foo: bar ` | `{ "sequence": [    "entry",    [ "nested" ] ],  "mapping": { "foo": "bar" } } ` |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
|                                                              |                                                              |

Legend:

- `s-l+block-collection(n,c)`
-  

- `l+block-sequence(n)`
-  

- `l+block-mapping(n)`