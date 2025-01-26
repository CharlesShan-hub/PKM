
# Markdown

## Overview

John Gruber于2004年创建了一种轻量级标记语言 Markdown，用于使用纯文本编辑器创建格式化文本。主要设计目标是**可读性**，即语言可以按原样阅读，而不会看起来像是用标签或格式化指令标记的，不像用“更重”的标记语言格式化的文本，例如RTF，HTML。Gruber避免在Markdown中使用花括号，以非正式地将它们保留给特定于实现的扩展。\[1]

![[assets/markdown-syntex-drawing|1000]]

下面是 markdown 冷门语法汇总：

* [[notes/markdown-syntex|markdown-syntex]]

markdown 语言的目标是使人们能够“使用易于阅读和编写的纯文本格式进行编写，并选择将其转换为结构有效的XHTML（或HTML）。从2012年开始，包括Jeff Atwood和John MacFarlane在内的一群人发起了Atwood所说的标准化工作。下图[2]是markdown渲染过程。

![[assets/render-workflow-drawing|1000]]

人们总结了 markdown 转其他标记语言的工具列表\[3]。其中 commonmark\[4] 是一个持续更新的很好的转换的实现标准。

另外，为了扩展功能，不同的平台也推出了自己的 markdown 变体：

* [CommonMark](https://commonmark.org/)：markdown 作者并没有推出详细的规则(Spec)，commonMark 制定了一套规则
* [GitHub Flavored Markdown (GFM)](https://github.github.com/gfm/)：
  * 修复了commonMark很多歧义的情况，更细致的 Spec
  * commonMark 的超集：添加了折叠，引用问题和拉取请求，警报等功能
  * [https://www.freecodecamp.org/news/github-flavored-markdown-syntax-examples/](https://www.freecodecamp.org/news/github-flavored-markdown-syntax-examples/)\[8]
* [Markdown Extra](https://michelf.ca/projects/php-markdown/extra/)：markdown++
  1. **内联HTML**：放宽了Markdown对块级HTML元素的限制，允许更灵活地使用HTML。
  2. **Markdown Inside HTML Blocks**：允许在HTML块级元素中使用Markdown格式。
  3. **特殊属性**：可以给标题、围栏代码块、链接和图片添加id和class属性。
  4. **围栏代码块**：引入了无需缩进的代码块表示法。
  5. **表格**：支持简单的表格创建。
  6. **定义列表**：实现了定义列表的语法。
  7. **脚注**：允许在文档中添加脚注。
  8. **缩写**：支持缩写词的定义和使用。
  9. **有序列表**：允许有序列表从非数字1开始。
  10. **强调**：修改了强调的规则，使下划线在单词中间时不触发强调。
* [MultiMarkdown](https://fletcherpenney.net/multimarkdown/)
  * commonMark 的超集：添加了bibtex，latex等功能
  * 即是 spec 也是工具，可以转换成 html 以外的更多的文件格式
* [R Markdown](https://rmarkdown.rstudio.com/)
  * 更强调了代码运行能力，有点像 python 的 jupyter notebook
  * 也可以转换成 html 以外的更多的文件格式，《R for data science》就是它生成的。

## Resources

* awesome-markdown\[5]：markdown的库，服务，编辑器，工具，备忘录等
* 闯关式教程\[6]
* markdown 中文官网语法介绍\[7]

## Reference

1. [Wiki of Markdown](https://en.wikipedia.org/wiki/Markdown)
2. [快速入门](https://www.markdownguide.org/getting-started/)
3. [markdown render 整理](https://github.com/markdown/markdown.github.com/wiki/Implementations)
4. [commonmark](https://commonmark.org/)
5. [awesome-markdown](https://github.com/mundimark/awesome-markdown)
6. [闯关式教程](https://www.markdowntutorial.com/)
7. [markdown 中文官网](https://markdown.com.cn/)
8. [freecodecamp 上的 github markdown 优秀帖子](https://www.freecodecamp.org/news/github-flavored-markdown-syntax-examples/)

