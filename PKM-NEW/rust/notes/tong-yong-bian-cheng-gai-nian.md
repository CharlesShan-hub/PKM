# 通用编程概念

https://rustwiki.org/zh-CN/book/ch03-00-common-programming-concepts.html

## [**3.1.** 变量和可变性](https://rustwiki.org/zh-CN/book/ch03-01-variables-and-mutability.html)

### 可变性

rust 特点：“变量不可变”。如何记住呢，可以这样理解，生成一个变量用的是`let`，本来也没说可以变。可以想象一个稳定的真理世界，里边都是不变的永恒的东西，这样就觉得很安全吧。如果要定义一个东西确实可以变，那就再加上 mut。

不可变变量

```rust
let x = 5;
```

可变变量

```rust
let mut x = 5;
```

常量：常量只能设置为常量表达式，而不能是函数调用的结果或是只能在运行时计算得到的值。

```rust
const THREE_HOURS_IN_SECONDS: u32 = 60 * 60 * 3;
```

### 遮蔽

{% hint style="info" %}
rust 特点：“变量重复声明”。如何记住呢（我的理解）：

* 对于 c，一个作用域中我们不能两次声明变量 x。我们的内存空间就很稳定，但是程序写的不方便，没用的东西没办法及时丢掉。
* 对于 python，可以重复的创建同样变量名的 x，每次后边就会取代前边。这样程序很好写，但是由于 python 是解释型语言，性能就会很差。（可以发现变量每变一次地址都不一样）。而且 Python 由于他的“逐行解释”，不能支持遮蔽了。

```python
s = "Hello"
print(id(s)) # 4534146672
s = s+" World"
print(id(s)) # 4534146544

x = 1
print(id(x)) # 4531576152
x = x+1
print(id(x)) # 4531576184

y = 1
print(id(y)) # 4531576152
y += 1
print(id(y)) # 4531576184
```

* 对于 rust，我们可以重复声明变量x，让程序好写。然后通过编译环节来提高性能，这样就能精准的控制每个变量的作用域了。

```rust
fn main() {
    let a = "String";
    println!("{a}"); // String
    let a = a.len();
    println!("{a}"); // 6
}
```
{% endhint %}

遮蔽就是内部的作用域的变量传不出去，但可以访问外部的作用域的变量。很多语言都可以做到：

{% code title="C（可以遮蔽）" %}
```c
#include <stdio.h>

int main()
{
    int i = 1;
    {
        int j = i;
        int i = j + 1;
        printf("%d\n", i); // 2
    }
    printf("%d\n", i); // 1
    return 0;
}
```
{% endcode %}

{% code title="Python（不能遮蔽）" %}
```python
x = 1
def f():
    x = x+1 # UnboundLocalError: cannot access local variable 'x' where it is not associated with a value
    print(x+1)
f()
print(x)
```
{% endcode %}

{% code title="Rust（可以遮蔽）" %}
```rust
fn main() {
    let a = "String";
    {
        let a = a.len();
        println!("{a}"); // 6let a = a.len();
    }
    println!("{a}"); // String
}
```
{% endcode %}

总得来讲，Rust 既可以像 C 一样遮蔽，又可以像 Python 一样好用。

***

## [**3.2.** 数据类型](https://rustwiki.org/zh-CN/book/ch03-02-data-types.html)

### 标量类型

> 整型、浮点型、布尔型和字符

#### 整型类型

| 长度    | 有符号类型   | 无符号类型   |
| ----- | ------- | ------- |
| 8 位   | `i8`    | `u8`    |
| 16 位  | `i16`   | `u16`   |
| 32 位  | `i32`   | `u32`   |
| 64 位  | `i64`   | `u64`   |
| 128 位 | `i128`  | `u128`  |
| arch  | `isize` | `usize` |

`isize` 和 `usize` 类型取决于程序运行的计算机体系结构，在表中表示为“arch”：若使用 64 位架构系统则为 64 位，若使用 32 位架构系统则为 32 位。

#### 整形字面量

| 数字字面量         | 示例            |
| ------------- | ------------- |
| 十进制           | `98_222`      |
| 十六进制          | `0xff`        |
| 八进制           | `0o77`        |
| 二进制           | `0b1111_0000` |
| 字节 (仅限于 `u8`) | `b'A'`        |

#### 浮点类型

默认为`f64`，也可以声明成`f32`

#### 数字运算

&#x20;Rust 除法整形不取小数，和 C 一样。（Python 除法整形会自动转换成小数）

#### 布尔类型

true，false。和 C 一样。

#### 字符类型

大小为 3 字节。C 是一字节。Python 不一定。

{% tabs %}
{% tab title="Rust" %}
统一采用Unicode

```rust
fn main() {
    let c1 = 'a';
    println!(
        "The size of the char 'a' is {} bytes",
        std::mem::size_of_val(&c1)
    );
    let c2 = 'π';
    println!(
        "The size of the char 'π' is {} bytes",
        std::mem::size_of_val(&c2)
    );
    let c3 = '中';
    println!(
        "The size of the char '中' is {} bytes",
        std::mem::size_of_val(&c3)
    );
    let c4 = '😻';
    println!(
        "The size of the char '😻' is {} bytes",
        std::mem::size_of_val(&c4)
    );
    let c5 = "🀄️";
    println!(
        "The size of the string '🀄️' is {} bytes",
        std::mem::size_of_val(&c5)
    );
}

// The size of the char 'a' is 4 bytes
// The size of the char 'π' is 4 bytes
// The size of the char '中' is 4 bytes
// The size of the char '😻' is 4 bytes
// The size of the string '🀄️' is 16 bytes

// note: this `🀄` is followed by the combining mark `\u{fe0f}`
//   --> src/main.rs:17:15
//    |
// 17 |     let c4 = '🀄️';
//    |               ^^
// help: if you meant to write a string literal, use double quotes
//    |
// 17 |     let c4 = "🀄️";
//    |              ~  ~

```
{% endtab %}

{% tab title="Python" %}
一个字符不一定多大

```python
def get_byte_size(char):
    # 尝试将字符编码为UTF-8
    try:
        utf8_bytes = char.encode('utf-8')
        # 返回字符编码后的字节大小
        return len(utf8_bytes)
    except UnicodeEncodeError:
        # 如果字符不能被编码为UTF-8，返回一个错误消息或默认值
        return "字符不能被编码为UTF-8"

print(f"字符 'a' 的字节大小是：{get_byte_size('a')}")
print(f"字符 'π' 的字节大小是：{get_byte_size('π')}")
print(f"字符 '中' 的字节大小是：{get_byte_size('中')}")
print(f"字符 '😻' 的字节大小是：{get_byte_size('😻')}")
print(f"字符 '🀄️' 的字节大小是：{get_byte_size('🀄️')}")
# 字符 'a' 的字节大小是：1
# 字符 'π' 的字节大小是：2
# 字符 '中' 的字节大小是：3
# 字符 '😻' 的字节大小是：4
# 字符 '🀄️' 的字节大小是：7
```
{% endtab %}
{% endtabs %}

### 复合类型

> **复合类型**（_compound type_）可以将多个值组合成一个类型。Rust 有两种基本的复合类型：元组（tuple）和数组（array）。

#### 元组

```rust
fn main() {
    let t: (i32, f64, u8) = (500, 6.4, 1);
    let (x, y, z) = t;  // 解构

    let five_hundred = t.0; // 从 0 开始索引

    let six_point_four = t.1;

    let one = t.2;
}
```

#### 数组

```rust
fn main() {
    let a = [1, 2, 3, 4, 5]; // 1,2,3,4,5
    println!("{} {} {} {} {}", a[0], a[1], a[2], a[3], a[4]);
    let a: [i32; 5] = [1, 2, 3, 4, 5]; // 1,2,3,4,5
    println!("{} {} {} {} {}", a[0], a[1], a[2], a[3], a[4]);
    let a = [3; 5]; // 3,3,3,3,3
    println!("{} {} {} {} {}", a[0], a[1], a[2], a[3], a[4]);
}
```

***

## [**3.3.** 函数](https://rustwiki.org/zh-CN/book/ch03-03-how-functions-work.html)

#### 函数定义

用小驼峰命名法

#### 参数

```rust
fn main() {
    print_labeled_measurement(5, 'h');
}

fn print_labeled_measurement(value: i32, unit_label: char) {
    println!("The measurement is: {}{}", value, unit_label);
}
```

#### 语句

{% hint style="success" %}
这是 Rust 的精髓之一！一切皆表达式！函数，if，{}都是
{% endhint %}

```rust
fn main() {
    let y = { // {...}就是表达式了，有返回值
        let x = 3;
        x + 1 // 没有分号就自动当成 return
    }; // 注意，let 没有返回值

    println!("The value of y is: {}", y);
}
// The value of y is: 4
```

函数的 return 可以用这种语法糖来完成

<pre class="language-rust"><code class="lang-rust">fn main() {
    let x = plus_one(5);

    println!("The value of x is: {}", x);
}

fn plus_one(x: i32) -> i32 {
<strong>    x + 1
</strong>}
</code></pre>

***

## [**3.4.** 控制流](https://rustwiki.org/zh-CN/book/ch03-05-control-flow.html)

### if 表达式

<details>

<summary>最基础的 if</summary>

```rust
fn main() {
    let number = 6;

    if number % 4 == 0 {
        println!("number is divisible by 4");
    } else if number % 3 == 0 {
        println!("number is divisible by 3");
    } else if number % 2 == 0 {
        println!("number is divisible by 2");
    } else {
        println!("number is not divisible by 4, 3, or 2");
    }
}
```

</details>

<details>

<summary>if 的条件必须是 bool，rust 不会自动把 int 转成 bool</summary>

```rust
fn main() {
    let number = 3;

    if number { // Wrong!
    if number != 0 { // You can do this!
        println!("number was three");
    }
}
```

</details>

<details>

<summary>let + if</summary>

<pre class="language-rust"><code class="lang-rust">fn main() {
    let condition = true;
<strong>    let number = if condition { 5 } else { 6 };
</strong>
    println!("The value of number is: {}", number); // 5
}
</code></pre>

</details>

<details>

<summary>let + if 也要注意相同的返回类型</summary>

```rust
fn main() {
    let condition = true;

    let number = if condition { 5 } else { "six" }; // Wrong!

    println!("The value of number is: {}", number);
}
```

</details>

### 循环

<details>

<summary>loop</summary>

<pre class="language-rust"><code class="lang-rust">fn main() {
    let mut count = 0;
<strong>    loop {
</strong>        if count == 10 {
            break;
        }
        count += 1;
    }
}
</code></pre>

</details>

<details>

<summary>break 可以指定跳到外边的某一层</summary>

<pre class="language-rust"><code class="lang-rust">fn main() {
    let mut count = 0;
<strong>    'counting_up: loop {
</strong>        println!("count = {}", count);
        let mut remaining = 10;

        loop {
            println!("remaining = {}", remaining);
            if remaining == 9 {
<strong>                break; // break本层
</strong>            }
            if count == 2 {
<strong>                break 'counting_up; // break指定层
</strong>            }
            remaining -= 1;
        }

        count += 1;
    }
    println!("End count = {}", count);
}
//count = 0
//remaining = 10
//remaining = 9
//count = 1
//remaining = 10
//remaining = 9
//count = 2
//remaining = 10
//End count = 2
</code></pre>

</details>

<details>

<summary>循环 + 表达式，用 break 作为 return</summary>

```rust
fn main() {
    let mut counter = 0;

    let result = loop {
        counter += 1;

        if counter == 10 {
            break counter * 2;
        }
    };

    println!("The result is {}", result); // 20
}
```

</details>

<details>

<summary>while</summary>

```rust
fn main() {
    let mut number = 3;

    while number != 0 {
        println!("{}!", number);

        number -= 1;
    }

    println!("LIFTOFF!!!");
}
```

</details>

<details>

<summary>for</summary>

```rust
fn main() {
    let a = [10, 20, 30, 40, 50];

    for element in a {
        println!("the value is: {}", element);
    }
}
```

</details>

<details>

<summary>for + 倒序</summary>

```rust
fn main() {
    for number in (1..4).rev() { // 左闭右开
        println!("{}!", number);
    }
    println!("LIFTOFF!!!");
}
//3!
//2!
//1!
//LIFTOFF!!!
```

</details>







