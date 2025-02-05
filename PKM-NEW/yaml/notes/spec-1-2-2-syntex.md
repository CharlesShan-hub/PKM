# 语法

> 本文按照YAML官方文档1.2.2版本翻译总结而成
>
> https://yaml.org/spec/1.2.2/#chapter-4-syntax-conventions

The following chapters formally define the syntax of YAML character [streams](https://yaml.org/spec/1.2.2/#streams), using parameterized BNF productions. Each BNF production is both named and numbered for easy reference. Whenever possible, basic structures are specified before the more complex structures using them in a “bottom up” fashion.

以下章节明确规定了YAML字符流的语法，采用了参数化的巴科斯范式产生式。每个产生式都进行了命名和编号，以便于查阅。在描述时，首先规定了基本结构，然后逐步引入使用这些基本结构的更复杂结构，采用自底向上的方式。

The productions are accompanied by examples which are presented in a two-pane side-by-side format. The left-hand side is the YAML example and the right-hand side is an alternate YAML view of the example. The right-hand view uses JSON when possible. Otherwise it uses a YAML form that is as close to JSON as possible.

这些产生式附带了一些示例，示例以双窗格并排方式呈现。左侧是YAML格式的示例，而右侧则提供了该示例的另一种YAML格式视图。右侧视图尽可能使用JSON格式，如果无法使用JSON，则使用尽可能接近JSON的YAML格式。

## 4.1. Production Syntax

Productions are defined using the syntax `production-name ::= term`, where a term is either 产生式通过语法 `production-name ::= term` 来定义，其中术语（term）可以是：

- An atomic term（原子项）

  A quoted string (`"abc"`), which matches that concatenation of characters. A single character is usually written with single quotes (`'a'`).A hexadecimal number (`x0A`), which matches the character at that Unicode code point.A range of hexadecimal numbers (`[x20-x7E]`), which matches any character whose Unicode code point is within that range.The name of a production (`c-printable`), which matches that production.
  
  一个引用字符串（如 `"abc"`），它与这些字符的连续序列匹配。单个字符通常用单引号表示（如 `'a'`）。一个十六进制数（如 `x0A`），它对应于该Unicode码点上的字符。一系列十六进制数（如 `[x20-x7E]`），它匹配任何Unicode码点在该区间内的字符。产生式的名称（如 `c-printable`），它对应于该产生式。

- A lookaround（环视）

  `[ lookahead = term ]`, which matches the empty string if `term` would match.`[ lookahead ≠ term ]`, which matches the empty string if `term` would not match.`[ lookbehind = term ]`, which matches the empty string if `term` would match beginning at any prior point on the line and ending at the current position.
  
  `[ lookahead = term ]`，如果 `term` 将匹配，则匹配空字符串。`[ lookahead ≠ term ]`，如果` term `不匹配，则匹配空字符串。`[ lookbehind = term ]`，如果 `term` 从该行之前的任何点开始并在当前位置结束匹配，则匹配空字符串。

- A special production（特殊产生式）

  `<start-of-line>`, which matches the empty string at the beginning of a line.`<end-of-input>`, matches the empty string at the end of the input.`<empty>`, which (always) matches the empty string.
  
  `<start-of-line>`，在行首匹配空字符串。`<end-of-input>`，在输入末尾匹配空字符串。`<empty>`，始终匹配空字符串。
  
- A parenthesized term

  Matches its contents.

- A concatenation

  Is `term-one term-two`, which matches `term-one` followed by `term-two`.

- A alternation

  Is `term-one | term-two`, which matches the `term-one` if possible, or `term-two` otherwise.

- A quantified term:

  `term?`, which matches `(term | <empty>)`.`term*`, which matches `(term term* | <empty>)`.`term+`, which matches `(term term*)`.

> Note: Quantified terms are always greedy.

The order of precedence is parenthesization, then quantification, then concatenation, then alternation.

Some lines in a production definition might have a comment like:

```
production-a ::=
  production-b      # clarifying comment
```

These comments are meant to be informative only. For instance a comment that says `# not followed by non-ws char` just means that you should be aware that actual production rules will behave as described even though it might not be obvious from the content of that particular production alone.

## 4.2. Production Parameters

Some productions have parameters in parentheses after the name, such as [`s-line-prefix(n,c)`](https://yaml.org/spec/1.2.2/#rule-s-line-prefix). A parameterized production is shorthand for a (infinite) series of productions, each with a fixed value for each parameter.

For instance, this production:

```
production-a(n) ::= production-b(n)
```

Is shorthand for:

```
production-a(0) ::= production-b(0)
production-a(1) ::= production-b(1)
…
```

And this production:

```
production-a(n) ::=
  ( production-b(n+m) production-c(n+m) )+
```

Is shorthand for:

```
production-a(0) ::=
    ( production-b(0) production-c(0) )+
  | ( production-b(1) production-c(1) )+
  | …
production-a(1) ::=
    ( production-b(1) production-c(1) )+
  | ( production-b(2) production-c(2) )+
  | …
…
```

The parameters are as follows:

- Indentation: `n` or `m`

  May be any natural number, including zero. `n` may also be -1.

- Context: `c`

  This parameter allows productions to tweak their behavior according to their surrounding. YAML supports two groups of *contexts*, distinguishing between [block styles](https://yaml.org/spec/1.2.2/#block-style-productions) and [flow styles](https://yaml.org/spec/1.2.2/#flow-style-productions).

  May be any of the following values:

  `BLOCK-IN` – inside block context`BLOCK-OUT` – outside block context`BLOCK-KEY` – inside block key context`FLOW-IN` – inside flow context`FLOW-OUT` – outside flow context`FLOW-KEY` – inside flow key context

- (Block) Chomping: `t`

  The [line break](https://yaml.org/spec/1.2.2/#line-break-characters) chomping behavior for flow scalars. May be any of the following values:

- `STRIP` – remove all trailing newlines
- `CLIP` – remove all trailing newlines except the first
- `KEEP` – retain all trailing newlines

## 4.3. Production Naming Conventions

To make it easier to follow production combinations, production names use a prefix-style naming convention. Each production is given a prefix based on the type of characters it begins and ends with.

- `e-`

  A production matching no characters.

- `c-`

  A production starting and ending with a special character.

- `b-`

  A production matching a single [line break](https://yaml.org/spec/1.2.2/#line-break-characters).

- `nb-`

  A production starting and ending with a non-[break](https://yaml.org/spec/1.2.2/#line-break-characters) character.

- `s-`

  A production starting and ending with a [white space](https://yaml.org/spec/1.2.2/#white-space-characters) character.

- `ns-`

  A production starting and ending with a non-[space](https://yaml.org/spec/1.2.2/#white-space-characters) character.

- `l-`

  A production matching complete line(s).

- `X-Y-`

  A production starting with an `X-` character and ending with a `Y-` character, where `X-` and `Y-` are any of the above prefixes.

- `X+`, `X-Y+`

  A production as above, with the additional property that the matched content [indentation](https://yaml.org/spec/1.2.2/#indentation-spaces) level is greater than the specified `n` parameter.