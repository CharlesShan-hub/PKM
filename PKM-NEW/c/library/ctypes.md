
# ctypes.h

## Overview

![[../assets/ctypes-drawing|1000]]

***

## Functions

### Check

<table><thead><tr><th width="80">序号</th><th>函数 &#x26; 描述</th></tr></thead><tbody><tr><td>1</td><td><a href="https://www.runoob.com/cprogramming/c-function-isalnum.html">int isalnum(int c)</a><br>该函数检查所传的字符是否是字母和数字。</td></tr><tr><td>2</td><td><a href="https://www.runoob.com/cprogramming/c-function-isalpha.html">int isalpha(int c)</a><br>该函数检查所传的字符是否是字母。</td></tr><tr><td>3</td><td><a href="https://www.runoob.com/cprogramming/c-function-iscntrl.html">int iscntrl(int c)</a><br>该函数检查所传的字符是否是控制字符。</td></tr><tr><td>4</td><td><a href="https://www.runoob.com/cprogramming/c-function-isdigit.html">int isdigit(int c)</a><br>该函数检查所传的字符是否是十进制数字。</td></tr><tr><td>5</td><td><a href="https://www.runoob.com/cprogramming/c-function-isgraph.html">int isgraph(int c)</a><br>该函数检查所传的字符是否有图形表示法。</td></tr><tr><td>6</td><td><a href="https://www.runoob.com/cprogramming/c-function-islower.html">int islower(int c)</a><br>该函数检查所传的字符是否是小写字母。</td></tr><tr><td>7</td><td><a href="https://www.runoob.com/cprogramming/c-function-isprint.html">int isprint(int c)</a><br>该函数检查所传的字符是否是可打印的。</td></tr><tr><td>8</td><td><a href="https://www.runoob.com/cprogramming/c-function-ispunct.html">int ispunct(int c)</a><br>该函数检查所传的字符是否是标点符号字符。</td></tr><tr><td>9</td><td><a href="https://www.runoob.com/cprogramming/c-function-isspace.html">int isspace(int c)</a><br>该函数检查所传的字符是否是空白字符。</td></tr><tr><td>10</td><td><a href="https://www.runoob.com/cprogramming/c-function-isupper.html">int isupper(int c)</a><br>该函数检查所传的字符是否是大写字母。</td></tr><tr><td>11</td><td><a href="https://www.runoob.com/cprogramming/c-function-isxdigit.html">int isxdigit(int c)</a><br>该函数检查所传的字符是否是十六进制数字。</td></tr></tbody></table>

### Change

<table data-header-hidden><thead><tr><th width="81"></th><th></th></tr></thead><tbody><tr><td>1</td><td><a href="https://www.runoob.com/cprogramming/c-function-tolower.html">int tolower(int c)</a><br>该函数把大写字母转换为小写字母。</td></tr><tr><td>2</td><td><a href="https://www.runoob.com/cprogramming/c-function-toupper.html">int toupper(int c)</a><br>该函数把小写字母转换为大写字母。</td></tr></tbody></table>

### Class

<table><thead><tr><th width="164">类别</th><th>介绍</th></tr></thead><tbody><tr><td>数字</td><td>{ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 }</td></tr><tr><td>十六进制数字</td><td>{ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C, D, E, F, a, b, c, d, e, f }</td></tr><tr><td>小写字母</td><td>{ a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z }</td></tr><tr><td>大写字母</td><td>{ A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z }</td></tr><tr><td>字母</td><td>小写字母和大写字母的集合</td></tr><tr><td>字母数字字符</td><td>数字、小写字母和大写字母的集合</td></tr><tr><td>标点符号字符</td><td>{ !, ", #, $, %, &#x26;, ', (, ), *, +, ,, -, ., /, :, ;, &#x3C;, =, >, ?, @, [, , ], ^, _, `, {, |, }, ~ }</td></tr><tr><td>图形字符</td><td>字母数字字符和标点符号字符的集合</td></tr><tr><td>空格字符</td><td>制表符、换行符、垂直制表符、换页符、回车符、空格符的集合</td></tr><tr><td>可打印字符</td><td>字母数字字符、标点符号字符和空格字符的集合</td></tr><tr><td>控制字符</td><td>在 ASCII 编码中，八进制代码从 000 到 037，以及 177（DEL）</td></tr><tr><td>空白字符</td><td>包括空格符和制表符</td></tr><tr><td>字母字符</td><td>小写字母和大写字母的集合</td></tr></tbody></table>

***

## Reference

\[1] [https://www.runoob.com/cprogramming/c-standard-library-ctype-h.html](https://www.runoob.com/cprogramming/c-standard-library-ctype-h.html)
