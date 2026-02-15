# 包、carte、模块

https://rustwiki.org/zh-CN/book/ch07-00-managing-growing-projects-with-packages-crates-and-modules.html

> * **包**（_Packages_）： Cargo 的一个功能，它允许你构建、测试和分享 crate。
> * **Crates** ：一个模块的树形结构，它形成了库或二进制项目。
> * **模块**（_Modules_）和 **use**： 允许你控制作用域和路径的私有性。
> * **路径**（_path_）：一个命名例如结构体、函数或模块等项的方式

## [**7.1.** 包和 crate](https://rustwiki.org/zh-CN/book/ch07-01-packages-and-crates.html)

1. `crate`是库
2. `crate root`是库的源文件，编译的起点
3. `binary crate`是库的二进制项
4. `packet` 是包，一个包里边有一个或多个库，一个包有一个 `Cargo.toml`
5. `cargo new`之后会生成一个包，rust 会默认创建一个叫做`src/main.rs`的crate root，这个是约定俗成。

***

## [**7.2.** 定义模块来控制作用域与私有性](https://rustwiki.org/zh-CN/book/ch07-02-defining-modules-to-control-scope-and-privacy.html)

我们用`cargo new --lib restaurant`来创建一个模块

然后修改其中的的`src/lib.rs`

```rust
mod front_of_house {
    mod hosting {
        fn add_to_waitlist() {}

        fn seat_at_table() {}
    }

    mod serving {
        fn take_order() {}

        fn serve_order() {}

        fn take_payment() {}
    }
}
```

它的模块树就是

```
crate
 └── front_of_house
     ├── hosting
     │   ├── add_to_waitlist
     │   └── seat_at_table
     └── serving
         ├── take_order
         ├── serve_order
         └── take_payment
```

***

## [**7.3.** 路径用于引用模块树中的项](https://rustwiki.org/zh-CN/book/ch07-03-paths-for-referring-to-an-item-in-the-module-tree.html)

接下来如果我们要引用包里边的成员，有两种方式：

* <mark style="color:red;">**绝对路径**</mark>（_absolute path_）从 crate 根部开始，以 crate 名或者字面量 <mark style="color:red;">`crate`</mark> 开头。
* <mark style="color:red;">**相对路径**</mark>（_relative path_）从当前模块开始，以 <mark style="color:red;">`self`</mark>、<mark style="color:red;">`super`</mark> 或<mark style="color:red;">当前模块的标识符</mark>开头。

另外，如果一个变量要暴露到他外边，需要用到<mark style="color:red;">**pub**</mark>

<pre class="language-rust"><code class="lang-rust">mod front_of_house {
<strong>    pub mod hosting {
</strong><strong>        pub fn add_to_waitlist() {}
</strong>    }
}

pub fn eat_at_restaurant() {
    // 绝对路径
<strong>    crate::front_of_house::hosting::add_to_waitlist();
</strong>
    // 相对路径
<strong>    front_of_house::hosting::add_to_waitlist();
</strong>}
</code></pre>

如果某一层要引用它上层的内容，就需要 <mark style="color:red;">**super**</mark>

<pre class="language-rust"><code class="lang-rust">fn serve_order() {}

mod back_of_house {
    fn fix_incorrect_order() {
        cook_order();
<strong>        super::serve_order();
</strong>    }

    fn cook_order() {}
}

</code></pre>

我们还可以更精细化的指定 struct 和 enum 内部的成员是否是 pub

<pre class="language-rust"><code class="lang-rust">mod back_of_house {
<strong>    pub struct Breakfast { // 这里的 struct 没有 pub
</strong><strong>        pub toast: String, // 可以指定内部的 toast 是 pub
</strong><strong>        seasonal_fruit: String, // 不指定就是私有的
</strong><strong>    }
</strong>
    impl Breakfast {
        pub fn summer(toast: &#x26;str) -> Breakfast {
            Breakfast {
                toast: String::from(toast),
                seasonal_fruit: String::from("peaches"),
            }
        }
    }
}

pub fn eat_at_restaurant() {
    // 在夏天点一份黑麦面包作为早餐
    let mut meal = back_of_house::Breakfast::summer("Rye");
    // 更改我们想要的面包
    meal.toast = String::from("Wheat");
    println!("I'd like {} toast please", meal.toast);

    // 如果取消下一行的注释，将会导致编译失败；我们不被允许
    // 看到或更改随餐搭配的季节水果
    // meal.seasonal_fruit = String::from("blueberries");
}

</code></pre>

```rust
mod back_of_house {
    pub enum Appetizer { // 直接把 enum 指定为 pub，内部的 Soup 和 Salad都是 pub
        Soup,
        Salad,
    }
}

pub fn eat_at_restaurant() {
    let order1 = back_of_house::Appetizer::Soup;
    let order2 = back_of_house::Appetizer::Salad;
}
```

***

## [**7.4.** 使用 use 关键字将名称引入作用域](https://rustwiki.org/zh-CN/book/ch07-04-bringing-paths-into-scope-with-the-use-keyword.html)

> use
>
> use as&#x20;
>
> pub use
>
> Cargo中假如 dependencies
>
> 嵌套 use

每次引用都需要假如一长串的后缀太麻烦了。所以感觉直接 use

注意我们习惯引入到模块，而不是引用到函数。所以下面例子是`use crate::front_of_house::hosting;`而不是`use crate::front_of_house::hosting::add_to_waitlist;`

<pre class="language-rust"><code class="lang-rust">mod front_of_house {
    pub mod hosting {
        pub fn add_to_waitlist() {}
    }
}

<strong>use crate::front_of_house::hosting; // 绝对路径
</strong><strong>use front_of_house::hosting; // 相对路径
</strong>
pub fn eat_at_restaurant() {
    hosting::add_to_waitlist();
}
fn main() {}

</code></pre>

类似 python的 import as，rust 是 use as

<pre class="language-rust"><code class="lang-rust"><strong>use std::fmt::Result;
</strong><strong>use std::io::Result as IoResult;
</strong>
fn function1() -> Result {
    // --snip--
    Ok(())
}

fn function2() -> IoResult&#x3C;()> {
    // --snip--
    Ok(())
}
</code></pre>

重导出：pub use

让调用你编写的代码的代码能够像在自己的作用域内引用这些类型，可以结合 `pub` 和 `use`。这个技术被称为 “_重导出_（_re-exporting_）”，因为这样做将项引入作用域并同时使其可供其他代码引入自己的作用域。

```rust
mod front_of_house {
    pub mod hosting {
        pub fn add_to_waitlist() {}
    }
}

pub use crate::front_of_house::hosting;

pub fn eat_at_restaurant() {
    hosting::add_to_waitlist();
}

```

Cargo.toml 中假如某个包然后才能 use

<pre class="language-toml"><code class="lang-toml"><strong>[dependencies]
</strong><strong>rand = "0.8.3"
</strong></code></pre>

<pre class="language-rust"><code class="lang-rust"><strong>use rand::Rng;
</strong>
fn main() {
    let secret_number = rand::thread_rng().gen_range(1..101);
}
</code></pre>

嵌套 use，如果我们需要从一个包里边 use 很多东西。类似 python 的 from .. import 一大堆

```rust
// use std::cmp::Ordering;
// use std::io;
use std::{cmp::Ordering, io};

// use std::io;
// use std::io::Write;
use std::io::{self, Write};

// 引入所有内容
use std::collections::*;
```

***

## [**7.5.** 将模块分割进不同文件](https://rustwiki.org/zh-CN/book/ch07-05-separating-modules-into-different-files.html)

例如我们想把上边的 add\_to\_waitlist放在自己的文件里边

{% code title="src/front_of_house.rs" %}
```rust
pub mod hosting {
    pub fn add_to_waitlist() {}
}
```
{% endcode %}

{% code title="src/lib.rs" %}
```rust
mod front_of_house;

pub use crate::front_of_house::hosting;

pub fn eat_at_restaurant() {
    hosting::add_to_waitlist();
}
```
{% endcode %}

可以进一步修改，（如果想扩充 host），src/lib.rs中的引用不会改变：

{% code title=" src/front_of_house/hosting.rs" %}
```rust
pub fn add_to_waitlist() {}
```
{% endcode %}

{% code title="src/front_of_house.rs" %}
```rust
pub mod hosting;
```
{% endcode %}

