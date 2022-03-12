# 普通语法

2022.3.11

[TOC]

> 本文按照[菜鸟教程](https://www.runoob.com/markdown/md-tutorial.html)编写

## 标题

方案一：

```markdown
我展示的是一级标题
=================

我展示的是二级标题
-----------------
```

方法二：

```markdown
# 一级标题
## 二级标题
### 三级标题
#### 四级标题
##### 五级标题
###### 六级标题
```

## 字体

```markdown
*斜体文本*
_斜体文本_
**粗体文本**
__粗体文本__
***粗斜体文本***
___粗斜体文本___
```

## 段落

两个空格或者一个空行代表换行

## 分隔线

```markdown
***

* * *

*****

- - -

----------
```

## 删除线

```markdown
RUNOOB.COM
GOOGLE.COM
~~BAIDU.COM~~
```

## 下划线

```markdown
<u>带下划线文本</u>
```

## 脚注

```markdown
创建脚注格式类似这样 [^RUNOOB]。

[^RUNOOB]: 菜鸟教程 -- 学的不仅是技术，更是梦想！！！
```

![案例](https://www.runoob.com/wp-content/uploads/2019/03/md5.gif)

## 无序列表

```markdown
* 第一项
* 第二项
* 第三项

+ 第一项
+ 第二项
+ 第三项


- 第一项
- 第二项
- 第三项
```

## 有序列表

```markdown
1. 第一项
2. 第二项
3. 第三项
```

## 区块

### 区块

```markdown
> 区块引用
> 菜鸟教程
> 学的不仅是技术更是梦想
```

> 区块引用
> 菜鸟教程
> 学的不仅是技术更是梦想

### 区块嵌套

```markdown
> 最外层
> > 第一层嵌套
> > > 第二层嵌套
```

> 最外层
> > 第一层嵌套
> >
> > > 第二层嵌套

### 区块中使用列表

```
> 区块中使用列表
>
> 1. 第一项
> 2. 第二项
>
> + 第一项
> + 第二项
> + 第三项
```

> 区块中使用列表
>
> 1. 第一项
> 2. 第二项
>
> + 第一项
> + 第二项
> + 第三项

### 列表中使用区块

```
* 第一项

  > 菜鸟教程
  > 学的不仅是技术更是梦想

* 第二项
```

* 第一项

  > 菜鸟教程
  > 学的不仅是技术更是梦想

* 第二项

## 代码

### 行内代码

```markdown
`printf()` 函数
```

`printf()` 函数

### 代码区块

~~~markdown
```javascript
$(document).ready(function () {
    alert('RUNOOB');
});
```
~~~

## 链接

### 普通链接

```markdown
这是一个链接 [菜鸟教程](https://www.runoob.com)
<https://www.runoob.com>
```

### 高级链接

```markdown
这个链接用 1 作为网址变量 [Google][1]
这个链接用 runoob 作为网址变量 [Runoob][runoob]
然后在文档的结尾为变量赋值（网址）

  [1]: http://www.google.com/
  [runoob]: http://www.runoob.com/
```

![案例](https://www.runoob.com/wp-content/uploads/2019/03/EC3ED5D2-4F0D-492A-81B3-D485623D1A9E.jpg)

### 图片链接

```markdown
![alt 属性文本](图片地址)

![alt 属性文本](图片地址 "可选标题")
```

```markdown
![RUNOOB 图标](http://static.runoob.com/images/runoob-logo.png)

![RUNOOB 图标](http://static.runoob.com/images/runoob-logo.png "RUNOOB")
```

```markdown
这个链接用 1 作为网址变量 [RUNOOB][1].
然后在文档的结尾为变量赋值（网址）

[1]: http://static.runoob.com/images/runoob-logo.png
```

```markdown
<img src="http://static.runoob.com/images/runoob-logo.png" width="50%">
```

## 表格

```markdown
|  表头   | 表头  |
|  ----  | ----  |
| 单元格  | 单元格 |
| 单元格  | 单元格 |
```

| 表头   | 表头   |
| ------ | ------ |
| 单元格 | 单元格 |
| 单元格 | 单元格 |

- **-:** 设置内容和标题栏居右对齐。
- **:-** 设置内容和标题栏居左对齐。
- **:-:** 设置内容和标题栏居中对齐。

```markdown
| 左对齐 | 右对齐 | 居中对齐 |
| :-----| ----: | :----: |
| 单元格 | 单元格 | 单元格 |
| 单元格 | 单元格 | 单元格 |
```

## HTML元素

不在 Markdown 涵盖范围之内的标签，都可以直接在文档里面用 HTML 撰写。

目前支持的 HTML 元素有：`<kbd> <b> <i> <em> <sup> <sub> <br>`等 ，如

```markdown
使用 <kbd>Ctrl</kbd>+<kbd>Alt</kbd>+<kbd>Del</kbd> 重启电脑
```

使用 <kbd>Ctrl</kbd>+<kbd>Alt</kbd>+<kbd>Del</kbd> 重启电脑

## 转义

```markdown
**文本加粗** 
\*\* 正常显示星号 \*\*
```

**文本加粗** 
\*\* 正常显示星号 \*\*

```
\   反斜线
`   反引号
*   星号
_   下划线
{}  花括号
[]  方括号
()  小括号
#   井字号
+   加号
-   减号
.   英文句点
!   感叹号
```