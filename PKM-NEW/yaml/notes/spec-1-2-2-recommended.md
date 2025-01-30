# 建议

> 本文按照YAML官方文档1.2.2版本翻译总结而成
>
> https://yaml.org/spec/1.2.2/#chapter-10-recommended-schemas

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

```
Block style: !!map
  Clark : Evans
  Ingy  : döt Net
  Oren  : Ben-Kiki

Flow style: !!map { Clark: Evans, Ingy: döt Net, Oren: Ben-Kiki }
```

#### 10.1.1.2. Generic Sequence

- URI

  `tag:yaml.org,2002:seq`

- Kind

  [Sequence](https://yaml.org/spec/1.2.2/#sequence).

- Definition

  [Represents](https://yaml.org/spec/1.2.2/#representation-graph) a collection indexed by sequential integers starting with zero. Example [bindings](https://yaml.org/spec/1.2.2/#constructing-native-data-structures) to [native](https://yaml.org/spec/1.2.2/#representing-native-data-structures) types include Perl’s array, Python’s list or tuple and Java’s array or Vector.

**Example 10.2 `!!seq` Examples**

```
Block style: !!seq
- Clark Evans
- Ingy döt Net
- Oren Ben-Kiki

Flow style: !!seq [ Clark Evans, Ingy döt Net, Oren Ben-Kiki ]
```

#### 10.1.1.3. Generic String

- URI

  `tag:yaml.org,2002:str`

- Kind

  [Scalar](https://yaml.org/spec/1.2.2/#scalar).

- Definition

  [Represents](https://yaml.org/spec/1.2.2/#representation-graph) a Unicode string, a sequence of zero or more Unicode characters. This type is usually [bound](https://yaml.org/spec/1.2.2/#representing-native-data-structures) to the [native](https://yaml.org/spec/1.2.2/#representing-native-data-structures) language’s string type or, for languages lacking one (such as C), to a character array.

- Canonical Form:

  The obvious.

**Example 10.3 `!!str` Examples**

```
Block style: !!str |-
  String: just a theory.

Flow style: !!str "String: just a theory."
```

### 10.1.2. Tag Resolution

All [nodes](https://yaml.org/spec/1.2.2/#nodes) with the “`!`” non-specific tag are [resolved](https://yaml.org/spec/1.2.2/#resolved-tags), by the standard [convention](https://yaml.org/spec/1.2.2/#resolved-tags), to “`tag:yaml.org,2002:seq`”, “`tag:yaml.org,2002:map`” or “`tag:yaml.org,2002:str`”, according to their [kind](https://yaml.org/spec/1.2.2/#nodes).

All [nodes](https://yaml.org/spec/1.2.2/#nodes) with the “`?`” non-specific tag are left [unresolved](https://yaml.org/spec/1.2.2/#resolved-tags). This constrains the [application](https://yaml.org/spec/1.2.2/#processes-and-models) to deal with a [partial representation](https://yaml.org/spec/1.2.2/#loading-failure-points).

## 10.2. JSON Schema

The *JSON schema* is the lowest common denominator of most modern computer languages and allows [parsing](https://yaml.org/spec/1.2.2/#parsing-the-presentation-stream) JSON files. A YAML [processor](https://yaml.org/spec/1.2.2/#processes-and-models) should therefore support this [schema](https://yaml.org/spec/1.2.2/#recommended-schemas), at least as an option. It is also strongly recommended that other [schemas](https://yaml.org/spec/1.2.2/#recommended-schemas) should be based on it.

### 10.2.1. Tags

The JSON [schema](https://yaml.org/spec/1.2.2/#recommended-schemas) uses the following [tags](https://yaml.org/spec/1.2.2/#tags) in addition to those defined by the [failsafe](https://yaml.org/spec/1.2.2/#failsafe-schema) schema:

#### 10.2.1.1. Null

- URI

  `tag:yaml.org,2002:null`

- Kind

  [Scalar](https://yaml.org/spec/1.2.2/#scalar).

- Definition

  [Represents](https://yaml.org/spec/1.2.2/#representation-graph) the lack of a value. This is typically [bound](https://yaml.org/spec/1.2.2/#representing-native-data-structures) to a [native](https://yaml.org/spec/1.2.2/#representing-native-data-structures) null-like value (e.g., `undef` in Perl, `None` in Python). Note that a null is different from an empty string. Also, a [mapping](https://yaml.org/spec/1.2.2/#mapping) entry with some [key](https://yaml.org/spec/1.2.2/#nodes) and a null [value](https://yaml.org/spec/1.2.2/#nodes) is valid and different from not having that [key](https://yaml.org/spec/1.2.2/#nodes) in the [mapping](https://yaml.org/spec/1.2.2/#mapping).

- Canonical Form

  `null`.

**Example 10.4 `!!null` Examples**

```
!!null null: value for null key
key with null value: !!null null
```

#### 10.2.1.2. Boolean

- URI

  `tag:yaml.org,2002:bool`

- Kind

  [Scalar](https://yaml.org/spec/1.2.2/#scalar).

- Definition

  [Represents](https://yaml.org/spec/1.2.2/#representation-graph) a true/false value. In languages without a [native](https://yaml.org/spec/1.2.2/#representing-native-data-structures) Boolean type (such as C), they are usually [bound](https://yaml.org/spec/1.2.2/#representing-native-data-structures) to a native integer type, using one for true and zero for false.

- Canonical Form

  Either `true` or `false`.

**Example 10.5 `!!bool` Examples**

```
YAML is a superset of JSON: !!bool true
Pluto is a planet: !!bool false
```

#### 10.2.1.3. Integer

- URI

  `tag:yaml.org,2002:int`

- Kind

  [Scalar](https://yaml.org/spec/1.2.2/#scalar).

- Definition

  [Represents](https://yaml.org/spec/1.2.2/#representation-graph) arbitrary sized finite mathematical integers. Scalars of this type should be [bound](https://yaml.org/spec/1.2.2/#representing-native-data-structures) to a [native](https://yaml.org/spec/1.2.2/#representing-native-data-structures) integer data type, if possible.

  Some languages (such as Perl) provide only a “number” type that allows for both integer and floating-point values. A YAML [processor](https://yaml.org/spec/1.2.2/#processes-and-models) may use such a type for integers as long as they round-trip properly.

  In some languages (such as C), an integer may overflow the [native](https://yaml.org/spec/1.2.2/#representing-native-data-structures) type’s storage capability. A YAML [processor](https://yaml.org/spec/1.2.2/#processes-and-models) may reject such a value as an error, truncate it with a warning or find some other manner to round-trip it. In general, integers representable using 32 binary digits should safely round-trip through most systems.

- Canonical Form

  Decimal integer notation, with a leading “`-`” character for negative values, matching the regular expression `0 | -? [1-9] [0-9]*`

**Example 10.6 `!!int` Examples**

```
negative: !!int -12
zero: !!int 0
positive: !!int 34
```

#### 10.2.1.4. Floating Point

- URI

  `tag:yaml.org,2002:float`

- Kind

  [Scalar](https://yaml.org/spec/1.2.2/#scalar).

- Definition

  [Represents](https://yaml.org/spec/1.2.2/#representation-graph) an approximation to real numbers, including three special values (positive and negative infinity and “not a number”).

  Some languages (such as Perl) provide only a “number” type that allows for both integer and floating-point values. A YAML [processor](https://yaml.org/spec/1.2.2/#processes-and-models) may use such a type for floating-point numbers, as long as they round-trip properly.

  Not all floating-point values can be stored exactly in any given [native](https://yaml.org/spec/1.2.2/#representing-native-data-structures) type. Hence a float value may change by “a small amount” when round-tripped. The supported range and accuracy depends on the implementation, though 32 bit IEEE floats should be safe. Since YAML does not specify a particular accuracy, using floating-point [mapping keys](https://yaml.org/spec/1.2.2/#nodes) requires great care and is not recommended.

- Canonical Form

  Either `0`, `.inf`, `-.inf`, `.nan` or scientific notation matching the regular expression `-? [1-9] ( \. [0-9]* [1-9] )? ( e [-+] [1-9] [0-9]* )?`.

**Example 10.7 `!!float` Examples**

```
negative: !!float -1
zero: !!float 0
positive: !!float 2.3e4
infinity: !!float .inf
not a number: !!float .nan
```

### 10.2.2. Tag Resolution

The [JSON schema](https://yaml.org/spec/1.2.2/#json-schema) [tag resolution](https://yaml.org/spec/1.2.2/#tag-resolution) is an extension of the [failsafe schema](https://yaml.org/spec/1.2.2/#failsafe-schema) [tag resolution](https://yaml.org/spec/1.2.2/#tag-resolution).

All [nodes](https://yaml.org/spec/1.2.2/#nodes) with the “`!`” non-specific tag are [resolved](https://yaml.org/spec/1.2.2/#resolved-tags), by the standard [convention](https://yaml.org/spec/1.2.2/#resolved-tags), to “`tag:yaml.org,2002:seq`”, “`tag:yaml.org,2002:map`” or “`tag:yaml.org,2002:str`”, according to their [kind](https://yaml.org/spec/1.2.2/#nodes).

[Collections](https://yaml.org/spec/1.2.2/#collections) with the “`?`” non-specific tag (that is, [untagged](https://yaml.org/spec/1.2.2/#resolved-tags) [collections](https://yaml.org/spec/1.2.2/#collections)) are [resolved](https://yaml.org/spec/1.2.2/#resolved-tags) to “`tag:yaml.org,2002:seq`” or “`tag:yaml.org,2002:map`” according to their [kind](https://yaml.org/spec/1.2.2/#nodes).

[Scalars](https://yaml.org/spec/1.2.2/#scalars) with the “`?`” non-specific tag (that is, [plain scalars](https://yaml.org/spec/1.2.2/#plain-style)) are matched with a list of regular expressions (first match wins, e.g. `0` is resolved as `!!int`). In principle, JSON files should not contain any [scalars](https://yaml.org/spec/1.2.2/#scalars) that do not match at least one of these. Hence the YAML [processor](https://yaml.org/spec/1.2.2/#processes-and-models) should consider them to be an error.

| Regular expression                                           | Resolved to tag         |
| ------------------------------------------------------------ | ----------------------- |
| `null`                                                       | tag:yaml.org,2002:null  |
| `true | false`                                               | tag:yaml.org,2002:bool  |
| `-? ( 0 | [1-9] [0-9]* )`                                    | tag:yaml.org,2002:int   |
| `-? ( 0 | [1-9] [0-9]* ) ( \. [0-9]* )? ( [eE] [-+]? [0-9]+ )?` | tag:yaml.org,2002:float |
| `*`                                                          | Error                   |

> Note: The regular expression for `float` does not exactly match the one in the JSON specification, where at least one digit is required after the dot: `( \. [0-9]+ )`. The YAML 1.2 specification intended to match JSON behavior, but this cannot be addressed in the 1.2.2 specification.

**Example 10.8 JSON Tag Resolution**

| `A null: null Booleans: [ true, false ] Integers: [ 0, -0, 3, -19 ] Floats: [ 0., -0.0, 12e03, -2E+05 ] Invalid: [ True, Null,  0o7, 0x3A, +12.3 ] ` | `{ "A null": null,  "Booleans": [ true, false ],  "Integers": [ 0, 0, 3, -19 ],  "Floats": [ 0.0, -0.0, 12000, -200000 ],  "Invalid": [ "True", "Null",    "0o7", "0x3A", "+12.3" ] } ` |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
|                                                              |                                                              |

## 10.3. Core Schema

The *Core schema* is an extension of the [JSON schema](https://yaml.org/spec/1.2.2/#json-schema), allowing for more human-readable [presentation](https://yaml.org/spec/1.2.2/#presentation-stream) of the same types. This is the recommended default [schema](https://yaml.org/spec/1.2.2/#recommended-schemas) that YAML [processor](https://yaml.org/spec/1.2.2/#processes-and-models) should use unless instructed otherwise. It is also strongly recommended that other [schemas](https://yaml.org/spec/1.2.2/#recommended-schemas) should be based on it.

### 10.3.1. Tags

The core [schema](https://yaml.org/spec/1.2.2/#recommended-schemas) uses the same [tags](https://yaml.org/spec/1.2.2/#tags) as the [JSON schema](https://yaml.org/spec/1.2.2/#json-schema).

### 10.3.2. Tag Resolution

The [core schema](https://yaml.org/spec/1.2.2/#core-schema) [tag resolution](https://yaml.org/spec/1.2.2/#tag-resolution) is an extension of the [JSON schema](https://yaml.org/spec/1.2.2/#json-schema) [tag resolution](https://yaml.org/spec/1.2.2/#tag-resolution).

All [nodes](https://yaml.org/spec/1.2.2/#nodes) with the “`!`” non-specific tag are [resolved](https://yaml.org/spec/1.2.2/#resolved-tags), by the standard [convention](https://yaml.org/spec/1.2.2/#resolved-tags), to “`tag:yaml.org,2002:seq`”, “`tag:yaml.org,2002:map`” or “`tag:yaml.org,2002:str`”, according to their [kind](https://yaml.org/spec/1.2.2/#nodes).

[Collections](https://yaml.org/spec/1.2.2/#collections) with the “`?`” non-specific tag (that is, [untagged](https://yaml.org/spec/1.2.2/#resolved-tags) [collections](https://yaml.org/spec/1.2.2/#collections)) are [resolved](https://yaml.org/spec/1.2.2/#resolved-tags) to “`tag:yaml.org,2002:seq`” or “`tag:yaml.org,2002:map`” according to their [kind](https://yaml.org/spec/1.2.2/#nodes).

[Scalars](https://yaml.org/spec/1.2.2/#scalars) with the “`?`” non-specific tag (that is, [plain scalars](https://yaml.org/spec/1.2.2/#plain-style)) are matched with an extended list of regular expressions. However, in this case, if none of the regular expressions matches, the [scalar](https://yaml.org/spec/1.2.2/#scalar) is [resolved](https://yaml.org/spec/1.2.2/#resolved-tags) to `tag:yaml.org,2002:str` (that is, considered to be a string).

| Regular expression                                           | Resolved to tag                        |
| ------------------------------------------------------------ | -------------------------------------- |
| `null | Null | NULL | ~`                                     | tag:yaml.org,2002:null                 |
| `/* Empty */`                                                | tag:yaml.org,2002:null                 |
| `true | True | TRUE | false | False | FALSE`                 | tag:yaml.org,2002:bool                 |
| `[-+]? [0-9]+`                                               | tag:yaml.org,2002:int (Base 10)        |
| `0o [0-7]+`                                                  | tag:yaml.org,2002:int (Base 8)         |
| `0x [0-9a-fA-F]+`                                            | tag:yaml.org,2002:int (Base 16)        |
| `[-+]? ( \. [0-9]+ | [0-9]+ ( \. [0-9]* )? ) ( [eE] [-+]? [0-9]+ )?` | tag:yaml.org,2002:float (Number)       |
| `[-+]? ( \.inf | \.Inf | \.INF )`                            | tag:yaml.org,2002:float (Infinity)     |
| `\.nan | \.NaN | \.NAN`                                      | tag:yaml.org,2002:float (Not a number) |
| `*`                                                          | tag:yaml.org,2002:str (Default)        |

**Example 10.9 Core Tag Resolution**

| `A null: null Also a null: # Empty Not a null: "" Booleans: [ true, True, false, FALSE ] Integers: [ 0, 0o7, 0x3A, -19 ] Floats: [  0., -0.0, .5, +12e03, -2E+05 ] Also floats: [  .inf, -.Inf, +.INF, .NAN ] ` | `{ "A null": null,  "Also a null": null,  "Not a null": "",  "Booleans": [ true, true, false, false ],  "Integers": [ 0, 7, 58, -19 ],  "Floats": [    0.0, -0.0, 0.5, 12000, -200000 ],  "Also floats": [    Infinity, -Infinity, Infinity, NaN ] } ` |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
|                                                              |                                                              |

## 10.4. Other Schemas

None of the above recommended [schemas](https://yaml.org/spec/1.2.2/#recommended-schemas) preclude the use of arbitrary explicit [tags](https://yaml.org/spec/1.2.2/#tags). Hence YAML [processors](https://yaml.org/spec/1.2.2/#processes-and-models) for a particular programming language typically provide some form of [local tags](https://yaml.org/spec/1.2.2/#tags) that map directly to the language’s [native data structures](https://yaml.org/spec/1.2.2/#representing-native-data-structures) (e.g., `!ruby/object:Set`).

While such [local tags](https://yaml.org/spec/1.2.2/#tags) are useful for ad hoc [applications](https://yaml.org/spec/1.2.2/#processes-and-models), they do not suffice for stable, interoperable cross-[application](https://yaml.org/spec/1.2.2/#processes-and-models) or cross-platform data exchange.

Interoperable [schemas](https://yaml.org/spec/1.2.2/#recommended-schemas) make use of [global tags](https://yaml.org/spec/1.2.2/#tags) (URIs) that [represent](https://yaml.org/spec/1.2.2/#representation-graph) the same data across different programming languages. In addition, an interoperable [schema](https://yaml.org/spec/1.2.2/#recommended-schemas) may provide additional [tag resolution](https://yaml.org/spec/1.2.2/#tag-resolution) rules. Such rules may provide additional regular expressions, as well as consider the path to the [node](https://yaml.org/spec/1.2.2/#nodes). This allows interoperable [schemas](https://yaml.org/spec/1.2.2/#recommended-schemas) to use [untagged](https://yaml.org/spec/1.2.2/#resolved-tags) [nodes](https://yaml.org/spec/1.2.2/#nodes).

It is strongly recommended that such [schemas](https://yaml.org/spec/1.2.2/#recommended-schemas) be based on the [core schema](https://yaml.org/spec/1.2.2/#core-schema) defined above.