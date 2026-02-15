# Markdown Syntax

## Syntax

![[../assets/markdown-syntex-drawing|1000]]

允许我擅自把 markdown 的语法按照一个文档从无到有，从有到好的构建需求分成了四类：

1. **Plain Text**：构建基础框架。包含段落，换行，简单的加粗，斜体等内容。
2. **Logic**：构建具有逻辑的文档。包含表和和列表。
3. **Function**：为文档构建具体功能。包含代码块，公式块，超链接等内容。
4. **Beautify**：为文档增加可读性。包含分隔符等内容。

### ✏️Plain Text

让文档"写"出来

#### Title (标题)

标题除了`#`的写法，也可以用横线，但是不推荐使用。

```markdown
Heading level 1
===============
Heading level 2
---------------
```

#### Break Line (换行)

换行的三种方式：

* `<br>`
* 直接回车
* 行末两个空格：不推荐

#### &#x20;Emphasis (强调)

* 加粗或斜体：推荐用下划线而不是星号
  * `Love__is__bold`：不起作用！
  * `Love**is**bold`：这样才行！
* 下划线：`<u>下划线文本</u>`
* 删除：`~~世界是平坦的。~~`

#### Escape (转义)

```
如果要显示*，需要
\* 
其他的需要转义的符号：\`*_{}[]<>()#*+-/!|
```



### 📖Logic

让文档"有逻辑"

#### List (列表)

有序列表，序号可以不真的按序号，只要是数字就行

```
列表可以不真正的排序
1. First item
1. Second item
1. Third item
1. Fourth item

甚至可以是错的
1. First item
8. Second item
3. Third item
5. Fourth item
```

无需列表可以用`+`，`-`，`*`

```markdown
可以用-
- First item
- Second item
- Third item

也可以用*
* First item
* Second item
* Third item

或者*
+ First item
+ Second item
+ Third item
```

#### Definition List (定义列表)

这样就是First Term和Second Term分成两大块，内部没有空行的

```markdown
First Term
: This is the definition of the first term.

Second Term
: This is one definition of the second term.
: This is another definition of the second term.
```

#### Task List (代办清单)

```markdown
- [x] Write the press release
- [ ] Update the website
- [ ] Contact the media
```

#### Table (表格)

```markdown
表格
| Syntax      | Description |
| ----------- | ----------- |
| Header      | Title       |
| Paragraph   | Text        |

表格可以不用这么工整
| Syntax      | Description |
| --- | --------- |
| Header | Title |
| Paragraph | Text  |

表格对齐
| Syntax      | Description | Test Text     |
| :---        |    :----:   |          ---: |
| Header      | Title       | Here's this   |
| Paragraph   | Text        | And more      |

表格中显示|，需要用&#124;
```



### ⚙️Function

让文档"跑"起来

#### Code (代码)

除了三个撇号（围栏式），也可以用缩进来表示一个

```markdown
    <html>
      <head>
      </head>
    </html>
```

#### Links (各种链接, 图片其实也是链接)

* 图片：`![图片显示名](超链接地址 "超链接title")`

```markdown
图片(普通)
![Tux, the Linux mascot](/assets/images/tux.png)

图片(带鼠标悬停显示)
![The San Juan Mountains are beautiful!](/assets/images/san-juan-mountains.jpg "San Juan Mountains")
```

* 链接：`![链接显示名](超链接地址 "超链接title")`

```markdown
链接(普通)
My favorite search engine is [Google](https://www.google.com/).

链接(带鼠标悬停显示)
My favorite search engine is [Google](https://www.google.com/，"Goto google").

带有链接的图片(就是在图片上边套上链接)
[![An old rock in the desert](/assets/images/shiprock.jpg "Shiprock, New Mexico by Beau Rogers")](https://www.flickr.com/photos/beaurogers/31833779864/in/photolist-Qv3rFw-34mt9F-a9Cmfy-5Ha3Zi-9msKdv-o3hgjr-hWpUte-4WMsJ1-KUQ8N-deshUb-vssBD-6CQci6-8AFCiD-zsJWT-nNfsgB-dPDwZJ-bn9JGn-5HtSXY-6CUhAL-a4UTXB-ugPum-KUPSo-fBLNm-6CUmpy-4WMsc9-8a7D3T-83KJev-6CQ2bK-nNusHJ-a78rQH-nw3NvT-7aq2qf-8wwBso-3nNceh-ugSKP-4mh4kh-bbeeqH-a7biME-q3PtTf-brFpgb-cg38zw-bXMZc-nJPELD-f58Lmo-bXMYG-bz8AAi-bxNtNT-bXMYi-bXMY6-bXMYv)
```

* 简写：直接用尖括号括起来

```markdown
URL
<https://www.markdownguide.org>

邮箱
<fake@example.com>
```

* 引用类型链接：分成两部分，第一部分是链接名部分，第二部分是链接地址部分，用一个标签来连接

```
第一部分（两种同效果）
[hobbit-hole][1]
[hobbit-hole] [1]

第二部分（七种同效果）
[1]: https://en.wikipedia.org/wiki/Hobbit#Lifestyle
[1]: https://en.wikipedia.org/wiki/Hobbit#Lifestyle "Hobbit lifestyles"
[1]: https://en.wikipedia.org/wiki/Hobbit#Lifestyle 'Hobbit lifestyles'
[1]: https://en.wikipedia.org/wiki/Hobbit#Lifestyle (Hobbit lifestyles)
[1]: <https://en.wikipedia.org/wiki/Hobbit#Lifestyle> "Hobbit lifestyles"
[1]: <https://en.wikipedia.org/wiki/Hobbit#Lifestyle> 'Hobbit lifestyles'
[1]: <https://en.wikipedia.org/wiki/Hobbit#Lifestyle> (Hobbit lifestyles)
```

* Header ID (内部跳转)

```markdown
首先要在内部生成 ID

### My Great Heading {#custom-id}

然后链接链到 ID

[Heading IDs](#heading-ids)
```

* Automatic URL Linking (自动 URL) 会直接带上超链接

```markdown
http://www.example.com
```

* Disabling Automatic URL Linking (禁止自动 URL)

```
`http://www.example.com`
```

#### Footnote (脚注)

就是论文中的\[1]\[2]

```
Here's a simple footnote,[^1] and here's a longer one.[^bignote]

[^1]: This is the first footnote.

[^bignote]: Here's one with multiple paragraphs and code.

    Indent paragraphs to include them in the footnote.

    `{ my code }`

    Add as many paragraphs as you like.
```



### 🌟Beautify

让文档"美"起来

#### Seperator (分割线)

分割横线（注意前后要有空行）

```markdown

***

---

_________________

```

#### emoji (表情)

```markdown
Gone camping! :tent: Be back soon.

That is so funny! :joy:
```

Gone camping! ⛺ Be back soon.

That is so funny! 😂

#### Subscript (下标) <a href="#subscript" id="subscript"></a>

```
H~2~O
```

$$
H_2O
$$

like this： H\<sub>2\</sub>O

#### Superscript (上标) <a href="#superscript" id="superscript"></a>

```
X^2^
```

$$
x^2
$$

like this：X\<sup>2\</sup>

***

## Reference

\[1] [https://www.markdownguide.org/basic-syntax/](https://www.markdownguide.org/basic-syntax/)

\[2] [https://www.markdownguide.org/extended-syntax/](https://www.markdownguide.org/extended-syntax/)
