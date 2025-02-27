# 字符

> 本文按照YAML官方文档1.2.2版本翻译总结而成
>
> https://yaml.org/spec/1.2.2/#chapter-5-character-productions

## 5.1. Character Set

To ensure readability, YAML [streams](https://yaml.org/spec/1.2.2/#streams) use only the *printable* subset of the Unicode character set. The allowed character range explicitly excludes the C0 control block[15](https://yaml.org/spec/1.2.2/#fn:c0-block) `x00-x1F` (except for TAB `x09`, LF `x0A` and CR `x0D` which are allowed), DEL `x7F`, the C1 control block `x80-x9F` (except for NEL `x85` which is allowed), the surrogate block[16](https://yaml.org/spec/1.2.2/#fn:surrogates) `xD800-xDFFF`, `xFFFE` and `xFFFF`.

On input, a YAML [processor](https://yaml.org/spec/1.2.2/#processes-and-models) must accept all characters in this printable subset.

On output, a YAML [processor](https://yaml.org/spec/1.2.2/#processes-and-models) must only produce only characters in this printable subset. Characters outside this set must be [presented](https://yaml.org/spec/1.2.2/#presenting-the-serialization-tree) using [escape](https://yaml.org/spec/1.2.2/#escaped-characters) sequences. In addition, any allowed characters known to be non-printable should also be [escaped](https://yaml.org/spec/1.2.2/#escaped-characters).

> Note: This isn’t mandatory since a full implementation would require extensive character property tables.

```
[1] c-printable ::=
                         # 8 bit
    x09                  # Tab (\t)
  | x0A                  # Line feed (LF \n)
  | x0D                  # Carriage Return (CR \r)
  | [x20-x7E]            # Printable ASCII
                         # 16 bit
  | x85                  # Next Line (NEL)
  | [xA0-xD7FF]          # Basic Multilingual Plane (BMP)
  | [xE000-xFFFD]        # Additional Unicode Areas
  | [x010000-x10FFFF]    # 32 bit
```

To ensure [JSON compatibility](https://yaml.org/spec/1.2.2/#yaml-directives), YAML [processors](https://yaml.org/spec/1.2.2/#processes-and-models) must allow all non-C0 characters inside [quoted scalars](https://yaml.org/spec/1.2.2/#double-quoted-style). To ensure readability, non-printable characters should be [escaped](https://yaml.org/spec/1.2.2/#escaped-characters) on output, even inside such [scalars](https://yaml.org/spec/1.2.2/#scalars).

> Note: JSON [quoted scalars](https://yaml.org/spec/1.2.2/#double-quoted-style) cannot span multiple lines or contain [tabs](https://yaml.org/spec/1.2.2/#white-space-characters), but YAML [quoted scalars](https://yaml.org/spec/1.2.2/#double-quoted-style) can.

```
[2] nb-json ::=
    x09              # Tab character
  | [x20-x10FFFF]    # Non-C0-control characters
```

> Note: The production name `nb-json` means “non-break JSON compatible” here.

## 5.2. Character Encodings

All characters mentioned in this specification are Unicode code points. Each such code point is written as one or more bytes depending on the *character encoding* used. Note that in UTF-16, characters above `xFFFF` are written as four bytes, using a surrogate pair.

The character encoding is a [presentation detail](https://yaml.org/spec/1.2.2/#presenting-the-serialization-tree) and must not be used to convey [content](https://yaml.org/spec/1.2.2/#nodes) information.

On input, a YAML [processor](https://yaml.org/spec/1.2.2/#processes-and-models) must support the UTF-8 and UTF-16 character encodings. For [JSON compatibility](https://yaml.org/spec/1.2.2/#yaml-directives), the UTF-32 encodings must also be supported.

If a character [stream](https://yaml.org/spec/1.2.2/#streams) begins with a *byte order mark*, the character encoding will be taken to be as indicated by the byte order mark. Otherwise, the [stream](https://yaml.org/spec/1.2.2/#streams) must begin with an ASCII character. This allows the encoding to be deduced by the pattern of null (`x00`) characters.

Byte order marks may appear at the start of any [document](https://yaml.org/spec/1.2.2/#documents), however all [documents](https://yaml.org/spec/1.2.2/#documents) in the same [stream](https://yaml.org/spec/1.2.2/#streams) must use the same character encoding.

To allow for [JSON compatibility](https://yaml.org/spec/1.2.2/#yaml-directives), byte order marks are also allowed inside [quoted scalars](https://yaml.org/spec/1.2.2/#double-quoted-style). For readability, such [content](https://yaml.org/spec/1.2.2/#nodes) byte order marks should be [escaped](https://yaml.org/spec/1.2.2/#escaped-characters) on output.

The encoding can therefore be deduced by matching the first few bytes of the [stream](https://yaml.org/spec/1.2.2/#streams) with the following table rows (in order):

|                       | Byte0 | Byte1 | Byte2 | Byte3 | Encoding |
| --------------------- | ----- | ----- | ----- | ----- | -------- |
| Explicit BOM          | x00   | x00   | xFE   | xFF   | UTF-32BE |
| ASCII first character | x00   | x00   | x00   | any   | UTF-32BE |
| Explicit BOM          | xFF   | xFE   | x00   | x00   | UTF-32LE |
| ASCII first character | any   | x00   | x00   | x00   | UTF-32LE |
| Explicit BOM          | xFE   | xFF   |       |       | UTF-16BE |
| ASCII first character | x00   | any   |       |       | UTF-16BE |
| Explicit BOM          | xFF   | xFE   |       |       | UTF-16LE |
| ASCII first character | any   | x00   |       |       | UTF-16LE |
| Explicit BOM          | xEF   | xBB   | xBF   |       | UTF-8    |
| Default               |       |       |       |       | UTF-8    |

The recommended output encoding is UTF-8. If another encoding is used, it is recommended that an explicit byte order mark be used, even if the first [stream](https://yaml.org/spec/1.2.2/#streams) character is ASCII.

For more information about the byte order mark and the Unicode character encoding schemes see the Unicode FAQ[17](https://yaml.org/spec/1.2.2/#fn:uni-faq).

```
[3] c-byte-order-mark ::= xFEFF
```

In the examples, byte order mark characters are displayed as “`⇔`”.

**Example 5.1 Byte Order Mark**

| `⇔# Comment only. ` | `# This stream contains no # documents, only comments. ` |
| ------------------- | -------------------------------------------------------- |
|                     |                                                          |

Legend:

- `c-byte-order-mark`

**Example 5.2 Invalid Byte Order Mark**

| `- Invalid use of BOM ⇔ - Inside a document. ` | `ERROR: A BOM must not appear inside a document. ` |
| ---------------------------------------------- | -------------------------------------------------- |
|                                                |                                                    |

## 5.3. Indicator Characters

*Indicators* are characters that have special semantics.

”`-`” (`x2D`, hyphen) denotes a [block sequence](https://yaml.org/spec/1.2.2/#block-sequences) entry.

```
[4] c-sequence-entry ::= '-'
```

”`?`” (`x3F`, question mark) denotes a [mapping key](https://yaml.org/spec/1.2.2/#nodes).

```
[5] c-mapping-key ::= '?'
```

”`:`” (`x3A`, colon) denotes a [mapping value](https://yaml.org/spec/1.2.2/#mapping).

```
[6] c-mapping-value ::= ':'
```

**Example 5.3 Block Structure Indicators**

| `sequence: - one - two mapping:  ? sky  : blue  sea : green ` | `{ "sequence": [    "one",    "two" ],  "mapping": {    "sky": "blue",    "sea": "green" } } ` |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
|                                                              |                                                              |

Legend:

- `c-sequence-entry`
-  

- `c-mapping-key`
-  

- `c-mapping-value`

”`,`” (`x2C`, comma) ends a [flow collection](https://yaml.org/spec/1.2.2/#flow-collection-styles) entry.

```
[7] c-collect-entry ::= ','
```

”`[`” (`x5B`, left bracket) starts a [flow sequence](https://yaml.org/spec/1.2.2/#flow-sequences).

```
[8] c-sequence-start ::= '['
```

”`]`” (`x5D`, right bracket) ends a [flow sequence](https://yaml.org/spec/1.2.2/#flow-sequences).

```
[9] c-sequence-end ::= ']'
```

”`{`” (`x7B`, left brace) starts a [flow mapping](https://yaml.org/spec/1.2.2/#flow-mappings).

```
[10] c-mapping-start ::= '{'
```

”`}`” (`x7D`, right brace) ends a [flow mapping](https://yaml.org/spec/1.2.2/#flow-mappings).

```
[11] c-mapping-end ::= '}'
```

**Example 5.4 Flow Collection Indicators**

| `sequence: [ one, two, ] mapping: { sky: blue, sea: green } ` | `{ "sequence": [ "one", "two" ],  "mapping":    { "sky": "blue", "sea": "green" } } ` |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
|                                                              |                                                              |

Legend:

- `c-sequence-start c-sequence-end`
-  

- `c-mapping-start c-mapping-end`
-  

- `c-collect-entry`

”`#`” (`x23`, octothorpe, hash, sharp, pound, number sign) denotes a [comment](https://yaml.org/spec/1.2.2/#comments).

```
[12] c-comment ::= '#'
```

**Example 5.5 Comment Indicator**

| `# Comment only. ` | `# This stream contains no # documents, only comments. ` |
| ------------------ | -------------------------------------------------------- |
|                    |                                                          |

Legend:

- `c-comment`

”`&`” (`x26`, ampersand) denotes a [node’s anchor property](https://yaml.org/spec/1.2.2/#anchors-and-aliases).

```
[13] c-anchor ::= '&'
```

”`*`” (`x2A`, asterisk) denotes an [alias node](https://yaml.org/spec/1.2.2/#alias-nodes).

```
[14] c-alias ::= '*'
```

The “`!`” (`x21`, exclamation) is used for specifying [node tags](https://yaml.org/spec/1.2.2/#node-tags). It is used to denote [tag handles](https://yaml.org/spec/1.2.2/#tag-handles) used in [tag directives](https://yaml.org/spec/1.2.2/#tag-directives) and [tag properties](https://yaml.org/spec/1.2.2/#node-tags); to denote [local tags](https://yaml.org/spec/1.2.2/#tags); and as the [non-specific tag](https://yaml.org/spec/1.2.2/#resolved-tags) for non-[plain scalars](https://yaml.org/spec/1.2.2/#plain-style).

```
[15] c-tag ::= '!'
```

**Example 5.6 Node Property Indicators**

| `anchored: !local &anchor value alias: *anchor ` | `{ "anchored": !local &A1 "value",  "alias": *A1 } ` |
| ------------------------------------------------ | ---------------------------------------------------- |
|                                                  |                                                      |

Legend:

- `c-tag`
-  

- `c-anchor`
-  

- `c-alias`

”`|`” (`7C`, vertical bar) denotes a [literal block scalar](https://yaml.org/spec/1.2.2/#literal-style).

```
[16] c-literal ::= '|'
```

”`>`” (`x3E`, greater than) denotes a [folded block scalar](https://yaml.org/spec/1.2.2/#block-folding).

```
[17] c-folded ::= '>'
```

**Example 5.7 Block Scalar Indicators**

| `literal: |  some  text folded: >  some  text ` | `{ "literal": "some\ntext\n",  "folded": "some text\n" } ` |
| ----------------------------------------------- | ---------------------------------------------------------- |
|                                                 |                                                            |

Legend:

- `c-literal`
-  

- `c-folded`

”`'`” (`x27`, apostrophe, single quote) surrounds a [single-quoted flow scalar](https://yaml.org/spec/1.2.2/#single-quoted-style).

```
[18] c-single-quote ::= "'"
```

”`"`” (`x22`, double quote) surrounds a [double-quoted flow scalar](https://yaml.org/spec/1.2.2/#double-quoted-style).

```
[19] c-double-quote ::= '"'
```

**Example 5.8 Quoted Scalar Indicators**

| `single: 'text' double: "text" ` | `{ "single": "text",  "double": "text" } ` |
| -------------------------------- | ------------------------------------------ |
|                                  |                                            |

Legend:

- `c-single-quote`
-  

- `c-double-quote`

”`%`” (`x25`, percent) denotes a [directive](https://yaml.org/spec/1.2.2/#directives) line.

```
[20] c-directive ::= '%'
```

**Example 5.9 Directive Indicator**

| `%YAML 1.2 --- text ` | `"text" ` |
| --------------------- | --------- |
|                       |           |

Legend:

- `c-directive`

The “`@`” (`x40`, at) and “```” (`x60`, grave accent) are *reserved* for future use.

```
[21] c-reserved ::=
    '@' | '`'
```

**Example 5.10 Invalid use of Reserved Indicators**

| `commercial-at: @text grave-accent: `text ` | `ERROR: Reserved indicators can't start a plain scalar. ` |
| ------------------------------------------- | --------------------------------------------------------- |
|                                             |                                                           |

Any indicator character:

```
[22] c-indicator ::=
    c-sequence-entry    # '-'
  | c-mapping-key       # '?'
  | c-mapping-value     # ':'
  | c-collect-entry     # ','
  | c-sequence-start    # '['
  | c-sequence-end      # ']'
  | c-mapping-start     # '{'
  | c-mapping-end       # '}'
  | c-comment           # '#'
  | c-anchor            # '&'
  | c-alias             # '*'
  | c-tag               # '!'
  | c-literal           # '|'
  | c-folded            # '>'
  | c-single-quote      # "'"
  | c-double-quote      # '"'
  | c-directive         # '%'
  | c-reserved          # '@' '`'
```

The “`[`”, “`]`”, “`{`”, “`}`” and “`,`” indicators denote structure in [flow collections](https://yaml.org/spec/1.2.2/#flow-collection-styles). They are therefore forbidden in some cases, to avoid ambiguity in several constructs. This is handled on a case-by-case basis by the relevant productions.

```
[23] c-flow-indicator ::=
    c-collect-entry     # ','
  | c-sequence-start    # '['
  | c-sequence-end      # ']'
  | c-mapping-start     # '{'
  | c-mapping-end       # '}'
```

## 5.4. Line Break Characters

YAML recognizes the following ASCII *line break* characters.

```
[24] b-line-feed ::= x0A
[25] b-carriage-return ::= x0D
[26] b-char ::=
    b-line-feed          # x0A
  | b-carriage-return    # X0D
```

All other characters, including the form feed (`x0C`), are considered to be non-break characters. Note that these include the *non-ASCII line breaks*: next line (`x85`), line separator (`x2028`) and paragraph separator (`x2029`).

[YAML version 1.1](https://yaml.org/spec/1.2.2/#yaml-directives) did support the above non-ASCII line break characters; however, JSON does not. Hence, to ensure [JSON compatibility](https://yaml.org/spec/1.2.2/#yaml-directives), YAML treats them as non-break characters as of version 1.2. YAML 1.2 [processors](https://yaml.org/spec/1.2.2/#processes-and-models) [parsing](https://yaml.org/spec/1.2.2/#parsing-the-presentation-stream) a [version 1.1](https://yaml.org/spec/1.2.2/#yaml-directives) [document](https://yaml.org/spec/1.2.2/#documents) should therefore treat these line breaks as non-break characters, with an appropriate warning.

```
[27] nb-char ::=
  c-printable - b-char - c-byte-order-mark
```

Line breaks are interpreted differently by different systems and have multiple widely used formats.

```
[28] b-break ::=
    (
      b-carriage-return  # x0A
      b-line-feed
    )                    # x0D
  | b-carriage-return
  | b-line-feed
```

Line breaks inside [scalar content](https://yaml.org/spec/1.2.2/#scalar) must be *normalized* by the YAML [processor](https://yaml.org/spec/1.2.2/#processes-and-models). Each such line break must be [parsed](https://yaml.org/spec/1.2.2/#parsing-the-presentation-stream) into a single line feed character. The original line break format is a [presentation detail](https://yaml.org/spec/1.2.2/#presenting-the-serialization-tree) and must not be used to convey [content](https://yaml.org/spec/1.2.2/#nodes) information.

```
[29] b-as-line-feed ::=
  b-break
```

Outside [scalar content](https://yaml.org/spec/1.2.2/#scalar), YAML allows any line break to be used to terminate lines.

```
[30] b-non-content ::=
  b-break
```

On output, a YAML [processor](https://yaml.org/spec/1.2.2/#processes-and-models) is free to emit line breaks using whatever convention is most appropriate.

In the examples, line breaks are sometimes displayed using the “`↓`” glyph for clarity.

**Example 5.11 Line Break Characters**

| `|  Line break (no glyph)  Line break (glyphed)↓ ` | `"Line break (no glyph)\nLine break (glyphed)\n" ` |
| -------------------------------------------------- | -------------------------------------------------- |
|                                                    |                                                    |

Legend:

- `b-break`

## 5.5. White Space Characters

YAML recognizes two *white space* characters: *space* and *tab*.

```
[31] s-space ::= x20
[32] s-tab ::= x09
[33] s-white ::=
  s-space | s-tab
```

The rest of the ([printable](https://yaml.org/spec/1.2.2/#character-set)) non-[break](https://yaml.org/spec/1.2.2/#line-break-characters) characters are considered to be non-space characters.

```
[34] ns-char ::=
  nb-char - s-white
```

In the examples, tab characters are displayed as the glyph “`→`”. Space characters are sometimes displayed as the glyph “`·`” for clarity.

**Example 5.12 Tabs and Spaces**

| `# Tabs and spaces quoted:·"Quoted →" block:→| ··void main() { ··→printf("Hello, world!\n"); ··} ` | `{ "quoted": "Quoted \t",  "block": "void main()    {\n\tprintf(\"Hello, world!\\n\");\n}\n" } ` |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
|                                                              |                                                              |

Legend:

- `s-space`
-  

- `s-tab`

## 5.6. Miscellaneous Characters

The YAML syntax productions make use of the following additional character classes:

A decimal digit for numbers:

```
[35] ns-dec-digit ::=
  [x30-x39]             # 0-9
```

A hexadecimal digit for [escape sequences](https://yaml.org/spec/1.2.2/#escaped-characters):

```
[36] ns-hex-digit ::=
    ns-dec-digit        # 0-9
  | [x41-x46]           # A-F
  | [x61-x66]           # a-f
```

ASCII letter (alphabetic) characters:

```
[37] ns-ascii-letter ::=
    [x41-x5A]           # A-Z
  | [x61-x7A]           # a-z
```

Word (alphanumeric) characters for identifiers:

```
[38] ns-word-char ::=
    ns-dec-digit        # 0-9
  | ns-ascii-letter     # A-Z a-z
  | '-'                 # '-'
```

URI characters for [tags](https://yaml.org/spec/1.2.2/#tags), as defined in the URI specification[18](https://yaml.org/spec/1.2.2/#fn:uri).

By convention, any URI characters other than the allowed printable ASCII characters are first *encoded* in UTF-8 and then each byte is *escaped* using the “`%`” character. The YAML [processor](https://yaml.org/spec/1.2.2/#processes-and-models) must not expand such escaped characters. [Tag](https://yaml.org/spec/1.2.2/#tags) characters must be preserved and compared exactly as [presented](https://yaml.org/spec/1.2.2/#presenting-the-serialization-tree) in the YAML [stream](https://yaml.org/spec/1.2.2/#streams), without any processing.

```
[39] ns-uri-char ::=
    (
      '%'
      ns-hex-digit{2}
    )
  | ns-word-char
  | '#'
  | ';'
  | '/'
  | '?'
  | ':'
  | '@'
  | '&'
  | '='
  | '+'
  | '$'
  | ','
  | '_'
  | '.'
  | '!'
  | '~'
  | '*'
  | "'"
  | '('
  | ')'
  | '['
  | ']'
```

The “`!`” character is used to indicate the end of a [named tag handle](https://yaml.org/spec/1.2.2/#tag-handles); hence its use in [tag shorthands](https://yaml.org/spec/1.2.2/#tag-shorthands) is restricted. In addition, such [shorthands](https://yaml.org/spec/1.2.2/#tag-shorthands) must not contain the “`[`”, “`]`”, “`{`”, “`}`” and “`,`” characters. These characters would cause ambiguity with [flow collection](https://yaml.org/spec/1.2.2/#flow-collection-styles) structures.

```
[40] ns-tag-char ::=
    ns-uri-char
  - c-tag               # '!'
  - c-flow-indicator
```

## 5.7. Escaped Characters

All non-[printable](https://yaml.org/spec/1.2.2/#character-set) characters must be *escaped*. YAML escape sequences use the “`\`” notation common to most modern computer languages. Each escape sequence must be [parsed](https://yaml.org/spec/1.2.2/#parsing-the-presentation-stream) into the appropriate Unicode character. The original escape sequence is a [presentation detail](https://yaml.org/spec/1.2.2/#presenting-the-serialization-tree) and must not be used to convey [content](https://yaml.org/spec/1.2.2/#nodes) information.

Note that escape sequences are only interpreted in [double-quoted scalars](https://yaml.org/spec/1.2.2/#double-quoted-style). In all other [scalar styles](https://yaml.org/spec/1.2.2/#node-styles), the “`\`” character has no special meaning and non-[printable](https://yaml.org/spec/1.2.2/#character-set) characters are not available.

```
[41] c-escape ::= '\'
```

YAML escape sequences are a superset of C’s escape sequences:

Escaped ASCII null (`x00`) character.

```
[42] ns-esc-null ::= '0'
```

Escaped ASCII bell (`x07`) character.

```
[43] ns-esc-bell ::= 'a'
```

Escaped ASCII backspace (`x08`) character.

```
[44] ns-esc-backspace ::= 'b'
```

Escaped ASCII horizontal tab (`x09`) character. This is useful at the start or the end of a line to force a leading or trailing tab to become part of the [content](https://yaml.org/spec/1.2.2/#nodes).

```
[45] ns-esc-horizontal-tab ::=
  't' | x09
```

Escaped ASCII line feed (`x0A`) character.

```
[46] ns-esc-line-feed ::= 'n'
```

Escaped ASCII vertical tab (`x0B`) character.

```
[47] ns-esc-vertical-tab ::= 'v'
```

Escaped ASCII form feed (`x0C`) character.

```
[48] ns-esc-form-feed ::= 'f'
```

Escaped ASCII carriage return (`x0D`) character.

```
[49] ns-esc-carriage-return ::= 'r'
```

Escaped ASCII escape (`x1B`) character.

```
[50] ns-esc-escape ::= 'e'
```

Escaped ASCII space (`x20`) character. This is useful at the start or the end of a line to force a leading or trailing space to become part of the [content](https://yaml.org/spec/1.2.2/#nodes).

```
[51] ns-esc-space ::= x20
```

Escaped ASCII double quote (`x22`).

```
[52] ns-esc-double-quote ::= '"'
```

Escaped ASCII slash (`x2F`), for [JSON compatibility](https://yaml.org/spec/1.2.2/#yaml-directives).

```
[53] ns-esc-slash ::= '/'
```

Escaped ASCII back slash (`x5C`).

```
[54] ns-esc-backslash ::= '\'
```

Escaped Unicode next line (`x85`) character.

```
[55] ns-esc-next-line ::= 'N'
```

Escaped Unicode non-breaking space (`xA0`) character.

```
[56] ns-esc-non-breaking-space ::= '_'
```

Escaped Unicode line separator (`x2028`) character.

```
[57] ns-esc-line-separator ::= 'L'
```

Escaped Unicode paragraph separator (`x2029`) character.

```
[58] ns-esc-paragraph-separator ::= 'P'
```

Escaped 8-bit Unicode character.

```
[59] ns-esc-8-bit ::=
  'x'
  ns-hex-digit{2}
```

Escaped 16-bit Unicode character.

```
[60] ns-esc-16-bit ::=
  'u'
  ns-hex-digit{4}
```

Escaped 32-bit Unicode character.

```
[61] ns-esc-32-bit ::=
  'U'
  ns-hex-digit{8}
```

Any escaped character:

```
[62] c-ns-esc-char ::=
  c-escape         # '\'
  (
      ns-esc-null
    | ns-esc-bell
    | ns-esc-backspace
    | ns-esc-horizontal-tab
    | ns-esc-line-feed
    | ns-esc-vertical-tab
    | ns-esc-form-feed
    | ns-esc-carriage-return
    | ns-esc-escape
    | ns-esc-space
    | ns-esc-double-quote
    | ns-esc-slash
    | ns-esc-backslash
    | ns-esc-next-line
    | ns-esc-non-breaking-space
    | ns-esc-line-separator
    | ns-esc-paragraph-separator
    | ns-esc-8-bit
    | ns-esc-16-bit
    | ns-esc-32-bit
  )
```

**Example 5.13 Escaped Characters**

| `- "Fun with \\" - "\" \a \b \e \f" - "\n \r \t \v \0" - "\  \_ \N \L \P \  \x41 \u0041 \U00000041" ` | `[ "Fun with \\",  "\" \u0007 \b \u001b \f",  "\n \r \t \u000b \u0000",  "\u0020 \u00a0 \u0085 \u2028 \u2029 A A A" ] ` |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
|                                                              |                                                              |

Legend:

- `c-ns-esc-char`

**Example 5.14 Invalid Escaped Characters**

| `Bad escapes:  "\c  \xq-" ` | `ERROR: - c is an invalid escaped character. - q and - are invalid hex digits. ` |
| --------------------------- | ------------------------------------------------------------ |
|                             |                                                              |