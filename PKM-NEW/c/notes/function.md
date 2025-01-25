# Function

## 函数基本组成结构

<details>

<summary>Demo</summary>

<pre class="language-c"><code class="lang-c">/* proto.c -- uses a function prototype */
#include &#x3C;stdio.h>
<strong>int imax(int, int);        /* prototype */
</strong>int main(void)
{
    printf("The maximum of %d and %d is %d.\n",
           3, 5, imax(3, 5)); 
    printf("The maximum of %d and %d is %d.\n",
           3, 5, imax(3.0, 5.0));
    return 0;
}

<strong>int imax(int n, int m)
</strong>{
    return (n > m ? n : m);
}
</code></pre>

</details>

* 函数原型（为了可以不用把 main 放在最底下，在最前边定义函数原型）
  * 如果没有传入参数，要写 void：`void test(void);`
* 使用函数
  * 会自动转换成目标类型（如 demo），可能会损失精度，会弹出警告
* 定义函数
* 参数
  * 形参
  * 实参
  * 形参不固定的情况：stdarg.h

{% content-ref url="../library/stdarg.h.md" %}
[stdarg.h.md](../library/stdarg.h.md)
{% endcontent-ref %}

## 递归

* 尾递归：把递归调用至于函数末尾
* main 函数也可以被调用！（但是很少这么做）

## 编译多源代码文件

