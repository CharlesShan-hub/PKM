# 文档流

> 本文按照YAML官方文档1.2.2版本翻译总结而成
>
> https://yaml.org/spec/1.2.2/#chapter-9-document-stream-productions

## 9.1. Documents

A YAML character [stream](https://yaml.org/spec/1.2.2/#streams) may contain several *documents*. Each document is completely independent from the rest.

### 9.1.1. Document Prefix

A document may be preceded by a *prefix* specifying the [character encoding](https://yaml.org/spec/1.2.2/#character-encodings) and optional [comment](https://yaml.org/spec/1.2.2/#comments) lines. Note that all [documents](https://yaml.org/spec/1.2.2/#documents) in a stream must use the same [character encoding](https://yaml.org/spec/1.2.2/#character-encodings). However it is valid to re-specify the [encoding](https://yaml.org/spec/1.2.2/#character-encodings) using a [byte order mark](https://yaml.org/spec/1.2.2/#character-encodings) for each [document](https://yaml.org/spec/1.2.2/#documents) in the stream.

The existence of the optional prefix does not necessarily indicate the existence of an actual [document](https://yaml.org/spec/1.2.2/#documents).

```
[202] l-document-prefix ::=
  c-byte-order-mark?
  l-comment*
```

**Example 9.1 Document Prefix**

| `⇔# Comment # lines Document ` | `"Document" ` |
| ------------------------------ | ------------- |
|                                |               |

Legend:

- `l-document-prefix`

### 9.1.2. Document Markers

Using [directives](https://yaml.org/spec/1.2.2/#directives) creates a potential ambiguity. It is valid to have a “`%`” character at the start of a line (e.g. as the first character of the second line of a [plain scalar](https://yaml.org/spec/1.2.2/#plain-style)). How, then, to distinguish between an actual [directive](https://yaml.org/spec/1.2.2/#directives) and a [content](https://yaml.org/spec/1.2.2/#nodes) line that happens to start with a “`%`” character?

The solution is the use of two special *marker* lines to control the processing of [directives](https://yaml.org/spec/1.2.2/#directives), one at the start of a [document](https://yaml.org/spec/1.2.2/#documents) and one at the end.

At the start of a [document](https://yaml.org/spec/1.2.2/#documents), lines beginning with a “`%`” character are assumed to be [directives](https://yaml.org/spec/1.2.2/#directives). The (possibly empty) list of [directives](https://yaml.org/spec/1.2.2/#directives) is terminated by a *directives end marker* line. Lines following this marker can safely use “`%`” as the first character.

At the end of a [document](https://yaml.org/spec/1.2.2/#documents), a *document end marker* line is used to signal the [parser](https://yaml.org/spec/1.2.2/#parsing-the-presentation-stream) to begin scanning for [directives](https://yaml.org/spec/1.2.2/#directives) again.

The existence of this optional *document suffix* does not necessarily indicate the existence of an actual following [document](https://yaml.org/spec/1.2.2/#documents).

Obviously, the actual [content](https://yaml.org/spec/1.2.2/#nodes) lines are therefore forbidden to begin with either of these markers.

```
[203] c-directives-end ::= "---"
[204] c-document-end ::=
  "..."    # (not followed by non-ws char)
[205] l-document-suffix ::=
  c-document-end
  s-l-comments
[206] c-forbidden ::=
  <start-of-line>
  (
      c-directives-end
    | c-document-end
  )
  (
      b-char
    | s-white
    | <end-of-input>
  )
```

**Example 9.2 Document Markers**

| `%YAML 1.2 --- Document ... # Suffix ` | `"Document" ` |
| -------------------------------------- | ------------- |
|                                        |               |

Legend:

- `c-directives-end`
-  

- `l-document-suffix`
-  

- `c-document-end`

### 9.1.3. Bare Documents

A *bare document* does not begin with any [directives](https://yaml.org/spec/1.2.2/#directives) or [marker](https://yaml.org/spec/1.2.2/#document-markers) lines. Such documents are very “clean” as they contain nothing other than the [content](https://yaml.org/spec/1.2.2/#nodes). In this case, the first non-comment line may not start with a “`%`” first character.

Document [nodes](https://yaml.org/spec/1.2.2/#nodes) are [indented](https://yaml.org/spec/1.2.2/#indentation-spaces) as if they have a parent [indented](https://yaml.org/spec/1.2.2/#indentation-spaces) at -1 [spaces](https://yaml.org/spec/1.2.2/#white-space-characters). Since a [node](https://yaml.org/spec/1.2.2/#nodes) must be more [indented](https://yaml.org/spec/1.2.2/#indentation-spaces) than its parent [node](https://yaml.org/spec/1.2.2/#nodes), this allows the document’s [node](https://yaml.org/spec/1.2.2/#nodes) to be [indented](https://yaml.org/spec/1.2.2/#indentation-spaces) at zero or more [spaces](https://yaml.org/spec/1.2.2/#white-space-characters).

```
[207] l-bare-document ::=
  s-l+block-node(-1,BLOCK-IN)
  /* Excluding c-forbidden content */
```

**Example 9.3 Bare Documents**

| `Bare document ... # No document ... | %!PS-Adobe-2.0 # Not the first line ` | `"Bare document" --- "%!PS-Adobe-2.0\n" ` |
| ------------------------------------------------------------ | ----------------------------------------- |
|                                                              |                                           |

Legend:

- `l-bare-document`

### 9.1.4. Explicit Documents

An *explicit document* begins with an explicit [directives end marker](https://yaml.org/spec/1.2.2/#document-markers) line but no [directives](https://yaml.org/spec/1.2.2/#directives). Since the existence of the [document](https://yaml.org/spec/1.2.2/#documents) is indicated by this [marker](https://yaml.org/spec/1.2.2/#document-markers), the [document](https://yaml.org/spec/1.2.2/#documents) itself may be [completely empty](https://yaml.org/spec/1.2.2/#example-empty-content).

```
[208] l-explicit-document ::=
  c-directives-end
  (
      l-bare-document
    | (
        e-node    # ""
        s-l-comments
      )
  )
```

**Example 9.4 Explicit Documents**

| `--- { matches % : 20 } ... --- # Empty ... ` | `{ "matches %": 20 } --- null ` |
| --------------------------------------------- | ------------------------------- |
|                                               |                                 |

Legend:

- `l-explicit-document`

### 9.1.5. Directives Documents

A *directives document* begins with some [directives](https://yaml.org/spec/1.2.2/#directives) followed by an explicit [directives end marker](https://yaml.org/spec/1.2.2/#document-markers) line.

```
[209] l-directive-document ::=
  l-directive+
  l-explicit-document
```

**Example 9.5 Directives Documents**

| `%YAML 1.2 --- | %!PS-Adobe-2.0 ... %YAML 1.2 --- # Empty ... ` | `"%!PS-Adobe-2.0\n" --- null ` |
| ------------------------------------------------------------ | ------------------------------ |
|                                                              |                                |

Legend:

- `l-explicit-document`

## 9.2. Streams

A YAML *stream* consists of zero or more [documents](https://yaml.org/spec/1.2.2/#documents). Subsequent [documents](https://yaml.org/spec/1.2.2/#documents) require some sort of separation [marker](https://yaml.org/spec/1.2.2/#document-markers) line. If a [document](https://yaml.org/spec/1.2.2/#documents) is not terminated by a [document end marker](https://yaml.org/spec/1.2.2/#document-markers) line, then the following [document](https://yaml.org/spec/1.2.2/#documents) must begin with a [directives end marker](https://yaml.org/spec/1.2.2/#document-markers) line.

```
[210] l-any-document ::=
    l-directive-document
  | l-explicit-document
  | l-bare-document
[211] l-yaml-stream ::=
  l-document-prefix*
  l-any-document?
  (
      (
        l-document-suffix+
        l-document-prefix*
        l-any-document?
      )
    | c-byte-order-mark
    | l-comment
    | l-explicit-document
  )*
```

**Example 9.6 Stream**

| `Document --- # Empty ... %YAML 1.2 --- matches %: 20 ` | `"Document" --- null --- { "matches %": 20 } ` |
| ------------------------------------------------------- | ---------------------------------------------- |
|                                                         |                                                |

Legend:

- `l-any-document`
-  

- `l-document-suffix`
-  

- `l-explicit-document`

A sequence of bytes is a *well-formed stream* if, taken as a whole, it complies with the above `l-yaml-stream` production.

# Chapter 10. Recommended Schemas

A YAML *schema* is a combination of a set of [tags](https://yaml.org/spec/1.2.2/#tags) and a mechanism for [resolving](https://yaml.org/spec/1.2.2/#resolved-tags) [non-specific tags](https://yaml.org/spec/1.2.2/#resolved-tags).

## 10.1. Failsafe Schema

The *failsafe schema* is guaranteed to work with any YAML [document](https://yaml.org/spec/1.2.2/#documents). It is therefore the recommended [schema](https://yaml.org/spec/1.2.2/#recommended-schemas) for generic YAML tools. A YAML [processor](https://yaml.org/spec/1.2.2/#processes-and-models) should therefore support this [schema](https://yaml.org/spec/1.2.2/#recommended-schemas), at least as an option.

### 10.1.1. Tags

#### 10.1.1.1. Generic Mapping

- URI

  `tag:yaml.org,2002:map`

- Kind

  [Mapping](https://yaml.org/spec/1.2.2/#mapping).

- Definition

  [Represents](https://yaml.org/spec/1.2.2/#representation-graph) an associative container, where each [key](https://yaml.org/spec/1.2.2/#nodes) is unique in the association and mapped to exactly one [value](https://yaml.org/spec/1.2.2/#nodes). YAML places no restrictions on the type of [keys](https://yaml.org/spec/1.2.2/#nodes); in particular, they are not restricted to being [scalars](https://yaml.org/spec/1.2.2/#scalars). Example [bindings](https://yaml.org/spec/1.2.2/#constructing-native-data-structures) to [native](https://yaml.org/spec/1.2.2/#representing-native-data-structures) types include Perl’s hash, Python’s dictionary and Java’s Hashtable.

**Example 10.1 `!!map` Examples**

```yaml
Block style: !!map
  Clark : Evans
  Ingy  : döt Net
  Oren  : Ben-Kiki

Flow style: !!map { Clark: Evans, Ingy: döt Net, Oren: Ben-Kiki }
```

