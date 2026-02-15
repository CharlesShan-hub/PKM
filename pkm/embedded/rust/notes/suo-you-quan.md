# 所有权

https://rustwiki.org/zh-CN/book/ch04-00-understanding-ownership.html

> 所有权（系统）是 Rust 最为与众不同的特性，它让 Rust 无需垃圾回收器（garbage collector）即可保证内存安全。因此，理解 Rust 中所有权的运作方式非常重要。在本章中，我们将讨论所有权以及相关功能：借用、slice 以及 Rust 如何在内存中存放数据。

## [**4.1.** 什么是所有权？](https://rustwiki.org/zh-CN/book/ch04-01-what-is-ownership.html)

### 内存管理

* C，快：开发者必须**亲自分配和释放**内存
* Python，Java，好：语言中具有**垃圾回收机制**，在程序运行时不断地寻找不再使用的内存
* Rust，又好又快：通过**所有权**系统管理内存，编译器在编译时会根据一系列的规则进行检查。在运行时，所有权系统的任何功能都不会减慢程序。

### 栈和堆

* 栈中的所有数据都必须占用已知且固定的大小。在编译时大小未知或大小可能变化的数据，要改为存储在堆上。
* 访问堆上的数据比访问栈上的数据慢，因为必须通过指针来访问。

### 所有权的规则

* Rust 中的每一个值都有一个被称为其 **所有者**（_owner_）的变量。
* 值在任一时刻**有且只有一个**所有者。
* 当所有者（变量）离开作用域，这个值将被丢弃。

### String

（第八章再深入，这里引入一下）

```rust
fn main() {
    let mut s = String::from("hello");

    s.push_str(", world!"); // push_str() 在字符串后追加字面值

    println!("{}", s); // 将打印 `hello, world!`
}
```

* "hello"不能变，它是字面量，存在堆上，存的是数据本身
* s 可变，s 是字符串变量，存在栈上，存的是对数据的引用

### “深拷贝”，克隆

```rust
fn main() {
    let s1 = String::from("hello");
    let s2 = s1.clone();

    println!("s1 = {}, s2 = {}", s1, s2);
}
```

### “浅拷贝”，移动

下面代码。s1 和 s2分别指向同一个内存，这样释放的时候可能会释放两次，导致“二次释放”。所以 rust 为了防止这种隐患，当 s2 = s1 时，认为 s1 不再有效。

```rust
fn main() {
    let s1 = String::from("hello");
    let s2 = s1;

    println!("{}, world!", s1);// Wrong, you can't use s1!
}
```

<details>

<summary> 小实验：就算是进到子作用域，作用域结束后，外边的被移除的所有权也不会被归还</summary>

```rust
fn main() {
    let s1 = String::from("Hello");
    {
        let s1 = s2;
        println!("{s2}");
    }
    println!("{s1}"); // Wrong, you can't use s1!

```

</details>

### trait

你可能想，整数才没这么麻烦，直接 b=a，两个也互不影响。如果你要想像赋值整数一样，那你就要把数据本身存到栈上，而不是堆上，这就要用到 trait。

如果一个类型实现了 `Copy` trait，那么一个旧的变量在将其赋值给其他变量后仍然可用。Rust 不允许自身或其任何部分实现了 `Drop` trait 的类型使用 `Copy` trait。

### 所有权与函数

移动除了可以移动到另一个变量，也可以移动到函数里去。

```rust
fn main() {
  let s = String::from("hello");  // s 进入作用域

  takes_ownership(s);             // s 的值移动到函数里 ...
                                  // ... 所以到这里不再有效

  let x = 5;                      // x 进入作用域

  makes_copy(x);                  // x 应该移动函数里，
                                  // 但 i32 是 Copy 的，所以在后面可继续使用 x

} // 这里, x 先移出了作用域，然后是 s。但因为 s 的值已被移走，
  // 所以不会有特殊操作

fn takes_ownership(some_string: String) { // some_string 进入作用域
  println!("{}", some_string);
} // 这里，some_string 移出作用域并调用 `drop` 方法。占用的内存被释放

fn makes_copy(some_integer: i32) { // some_integer 进入作用域
  println!("{}", some_integer);
} // 这里，some_integer 移出作用域。不会有特殊操作
```

{% hint style="success" %}
有趣，一个变量被调用一下，后边就用不了了？？幸好，我们可以用返回值归还所有权。
{% endhint %}

```rust
fn main() {
  let s1 = gives_ownership();         // gives_ownership 将返回值
                                      // 移给 s1

  let s2 = String::from("hello");     // s2 进入作用域

  let s3 = takes_and_gives_back(s2);  // s2 被移动到
                                      // takes_and_gives_back 中,
                                      // 它也将返回值移给 s3
} // 这里, s3 移出作用域并被丢弃。s2 也移出作用域，但已被移走，
  // 所以什么也不会发生。s1 移出作用域并被丢弃

fn gives_ownership() -> String {           // gives_ownership 将返回值移动给
                                           // 调用它的函数

  let some_string = String::from("yours"); // some_string 进入作用域

  some_string                              // 返回 some_string 并移出给调用的函数
}

// takes_and_gives_back 将传入字符串并返回该值
fn takes_and_gives_back(a_string: String) -> String { // a_string 进入作用域

  a_string  // 返回 a_string 并移出给调用的函数
}
```

***

## [**4.2.** 引用与借用](https://rustwiki.org/zh-CN/book/ch04-02-references-and-borrowing.html)

### 借用

> 1. 引用 -> 借用
> 2. 可变借用与不可边借用
> 3. 避免数据竞争

书接上回，如果我们写一个统计某个字符串有多长的函数，那就要这么写，s1 传进去，保存成 s2

<pre class="language-rust"><code class="lang-rust">fn main() {
    let s1 = String::from("hello");

<strong>    let (s2, len) = calculate_length(s1);
</strong>
    println!("The length of '{}' is {}.", s2, len);
}

<strong>fn calculate_length(s: String) -> (String, usize) {
</strong>    let length = s.len(); // len() 返回字符串的长度

    (s, length)
}
</code></pre>

&#x20;太窒息了，形式主义，不过这种“有借有还”的形式，能不能放到编译器里边去呢。这就是**借用**。

<pre class="language-rust"><code class="lang-rust">fn main() {
    let s1 = String::from("hello");

<strong>    let len = calculate_length(&#x26;s1);
</strong>
    println!("The length of '{}' is {}.", s1, len);
}

<strong>fn calculate_length(s: &#x26;String) -> usize {
</strong>    s.len()
}
</code></pre>

**这里的 main 里边的 s1 和 calculate\_length 中的 s 并不是都指向了同一个字符串！他组成了链表，s1 指向 s 指向内存！**换言之，s 没有得到所有权！

上边的是不可变的借用，下边是**可变的借用**。（借的时候说好会改）

<pre class="language-rust"><code class="lang-rust">fn main() {
    let mut s = String::from("hello");

<strong>    change(&#x26;mut s);
</strong>}

<strong>fn change(some_string: &#x26;mut String) {
</strong>    some_string.push_str(", world");
}
</code></pre>

这种可变的借用要注意，不能两个人一起借用一起改，下边的这个会报错。如果通过会导致“数据竞争”。

<pre class="language-rust"><code class="lang-rust">fn main() {
    let mut s = String::from("hello");

<strong>    let r1 = &#x26;mut s;
</strong><strong>    let r2 = &#x26;mut s;
</strong>
    println!("{}, {}", r1, r2);
}
</code></pre>

另外，可变借用也不能搭配不可变借用。因为一个不可变借用不希望自己在读一个不稳定的东西。

<pre class="language-rust"><code class="lang-rust">fn main() {
    let mut s = String::from("hello");

    let r1 = &#x26;s; // 没问题
    let r2 = &#x26;s; // 没问题
    let r3 = &#x26;mut s; // 大问题

<strong>    println!("{}, {}, and {}", r1, r2, r3); // 编译不能通过
</strong>}
</code></pre>

但如果我们可以保证s1，s2不会在 s3 出现后再被调用，那就可以编译通过

<pre class="language-rust"><code class="lang-rust">fn main() {
    let mut s = String::from("hello");

    let r1 = &#x26;s; // 没问题
    let r2 = &#x26;s; // 没问题
    let r3 = &#x26;mut s; // 大问题

<strong>    println!("{}", r3); // 编译可以通过
</strong>}
</code></pre>

### 避免悬垂引用

在具有指针的语言中，很容易通过释放内存时保留指向它的指针而错误地生成一个 **悬垂指针**（_dangling pointer_），所谓悬垂指针是其指向的内存可能已经被分配给其它持有者。相比之下，在 Rust 中编译器确保引用永远也不会变成悬垂状态：当你拥有一些数据的引用，编译器确保数据不会在其引用之前离开作用域。

让我们尝试创建一个悬垂引用，Rust 会通过一个编译时错误来避免：

<pre class="language-rust"><code class="lang-rust">fn main() {
    let reference_to_nothing = dangle();
}

<strong>fn dangle() -> &#x26;String {
</strong>    let s = String::from("hello");

    &#x26;s // 返回字符串 s 的引用
}// 这里 s 离开作用域并被丢弃。其内存被释放。
</code></pre>

***

## [**4.3.** 切片 slice](https://rustwiki.org/zh-CN/book/ch04-03-slices.html)

上边说借用没有所有权，**切片，也没有所有权**。切片是对几个钟一段连续元素序列的引用。

就像指向一片内存空间的指针只能有一个（所有权），字符串和字符串中的位置也存在绑定关系。所以 slice 是很有必要的。

基本语法如下：

```rust
fn main() {
    let s = String::from("hello");
    
    let slice = &s[0..2]; // 左闭右开
    let slice = &s[..2];  // 从0 开始，可以省略
    
    let slice = &s[3..len];
    let slice = &s[3..];  // 包含尾部也可以省略，这个和 python 一样
}
```

字符串是`String`，字符串的切片是`&str`

