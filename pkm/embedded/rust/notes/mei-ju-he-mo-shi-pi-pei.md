# 枚举和模式匹配

https://rustwiki.org/zh-CN/book/ch06-00-enums.html

## [**6.1.** 定义枚举](https://rustwiki.org/zh-CN/book/ch06-01-defining-an-enum.html)

### 枚举基础

枚举和结构类似，都有自己的变量和方法，不过枚举更倾向于列举出所有的可能性。

<details>

<summary>枚举可以作为数据类型</summary>

自己定义枚举 IP = {v4, v6}

```rust
fn main() {
    // 定义枚举
    #[derive(PartialEq)] // to use "=="
    enum IpAddrKind {
        V4,
        V6,
    }

    // 访问枚举
    let four = IpAddrKind::V4;
    let six = IpAddrKind::V6;

    // 作为函数参数类型
    fn route(ip_type: IpAddrKind) {
        if ip_type == IpAddrKind::V4 {
            println!("Type of route is V4");
        } else {
            println!("Type of route is V6");
        }
    }
    route(four); // Type of route is V4
    route(six); // Type of route is V6
}

```

</details>

<details>

<summary>枚举可以包含数据，关联方法（有点像结构体了）</summary>

```rust
fn main() {
    // 枚举可以包含数据
    #[derive(PartialEq)]
    enum IpAddr {
        V4(u8, u8, u8, u8),
        V6(String),
    }

    impl IpAddr {
        fn test(&self) {
            println!("我也不知道干点啥\n");
        }
    }

    let home = IpAddr::V4(127, 0, 0, 1);
    let loopback = IpAddr::V6(String::from("::1"));
    home.test();
}
```

</details>

<details>

<summary> 更好的方案，enum 里边套结构体</summary>

这个是rust 标准库里边对 IP 类型枚举的实现方案

```rust
#![allow(unused)]
fn main() {
    struct Ipv4Addr {
        // --snip--
    }

    struct Ipv6Addr {
        // --snip--
    }

    enum IpAddr {
        V4(Ipv4Addr),
        V6(Ipv6Addr),
    }
}

```

</details>

### Option 枚举和其相对于空值的优势

空值容易引发错误的原因是，人们按照非空的方式去调用空。

rust如何解决的：空与非空也是一种枚举，他就是 Option！

```rust
// rust 中对 Option 的定义
enum Option<T> {
    Some(T),
    None,
}
```

如果我们写了下面的函数，并尝试运行

```rust
let x: i8 = 5;
let y: Option<i8> = Some(5);

let sum = x + y;
```

这不会通过！因为 rust 不会把i8和 Option\<i8>加在一起。我们需要手动把Option\<i8>转换成i8，这样就可以保证，所有可以编译通过的代码不会把空加进去了。

***

## [**6.2.** match 控制流运算符](https://rustwiki.org/zh-CN/book/ch06-02-match.html)

上边我还在想，定义了枚举类型，怎么进行类型判断，这不就来了

<details>

<summary>Match Demo（ 匹配纯类型的 enum）</summary>

<pre class="language-rust"><code class="lang-rust">enum Coin {
    Penny,
    Nickel,
    Dime,
    Quarter,
}

<strong>fn value_in_cents(coin: Coin) -> u8 {
</strong><strong>    match coin {
</strong><strong>        Coin::Penny => 1,
</strong><strong>        Coin::Nickel => 5,
</strong><strong>        Coin::Dime => 10,
</strong><strong>        Coin::Quarter => 25,
</strong><strong>    }
</strong><strong>}
</strong>
fn main() {
    println!("{}", value_in_cents(Coin::Penny));
    println!("{}", value_in_cents(Coin::Nickel));
    println!("{}", value_in_cents(Coin::Dime));
}
</code></pre>

</details>

<details>

<summary>Match Demo（ 匹配有数据的 enum）</summary>

<pre class="language-rust"><code class="lang-rust"><strong>#[derive(Debug)]
</strong>enum UsState {
    Alabama,
    Alaska,
    // ....
}

enum Coin {
    Penny,
    Nickel,
    Dime,
<strong>    Quarter(UsState),
</strong>}

fn value_in_cents(coin: Coin) -> u8 {
    match coin {
        Coin::Penny => 1,
        Coin::Nickel => 5,
        Coin::Dime => 10,
<strong>        Coin::Quarter(state) => {
</strong><strong>            println!("State quarter from {:?}!", state);
</strong>            25
        }
    }
}

fn main() {
    println!("{}", value_in_cents(Coin::Penny));
    println!("{}", value_in_cents(Coin::Nickel));
<strong>    println!("{}", value_in_cents(Coin::Quarter(UsState::Alabama)));
</strong>}

</code></pre>

</details>

<details>

<summary>匹配 Option&#x3C;T></summary>

之前说的 Option 还没说处理方案：比如可能是空的数要加一，方法为，空还是空，数+1

```rust
fn main() {
    fn plus_one(x: Option<i32>) -> Option<i32> {
        match x {
            None => None,
            Some(i) => Some(i + 1),
        }
    }

    // 这个会报错，因为没写 None，对 enum 的匹配需要是穷尽的
    // fn plus_one(x: Option<i32>) -> Option<i32> {
    //     match x {
    //         Some(i) => Some(i + 1),
    //     }
    // }

    let five = Some(5);
    let six = plus_one(five);
    let none = plus_one(None);
}
```

</details>

<details>

<summary>通配模式和 _ 占位符</summary>

&#x20;如果不是对 enum 的匹配，比如输入一个数，根据大小进行后续判断。就要用到“other”。

<pre class="language-rust"><code class="lang-rust">fn main() {
    let dice_roll = 9;
    match dice_roll {
        3 => add_fancy_hat(),
        7 => remove_fancy_hat(),
<strong>        other => move_player(other),
</strong>    }

    fn add_fancy_hat() {}
    fn remove_fancy_hat() {}
    fn move_player(num_spaces: u8) {}
}
</code></pre>

&#x20;如果不需要获取 other 的值，也可以用通配符"\_"

<pre class="language-rust"><code class="lang-rust">fn main() {
    let dice_roll = 9;
    match dice_roll {
        3 => add_fancy_hat(),
        7 => remove_fancy_hat(),
<strong>        _ => reroll(),
</strong><strong>        // _ => (), // 可以用空的()，代表“无事发生”
</strong>    }

    fn add_fancy_hat() {}
    fn remove_fancy_hat() {}
    fn reroll() {}
}
</code></pre>

</details>

***

## [**6.3.** if let 简单控制流](https://rustwiki.org/zh-CN/book/ch06-03-if-let.html)

if let 可以简化代码。可以认为 `if let` 是 `match` 的一个语法糖，它当值匹配某一模式时执行代码而忽略所有其他值。

<details>

<summary>  if let</summary>

复杂的案例

<pre class="language-rust"><code class="lang-rust">#![allow(unused)]
fn main() {
    let some_u8_value = Some(0u8);
    match some_u8_value {
<strong>        Some(3) => println!("three"),
</strong><strong>        _ => (), // 我们只考虑 3 的情况，但是我们需要写通配符，很麻烦
</strong>    }
}

</code></pre>

使用 if let 进行简化

<pre class="language-rust"><code class="lang-rust">#![allow(unused)]
fn main() {
    let some_u8_value = Some(0u8);
<strong>    if let Some(3) = some_u8_value {
</strong>        println!("three");
    }
}

</code></pre>

</details>

<details>

<summary> if let else</summary>

复杂的情况

```rust
let mut count = 0;
match coin {
    Coin::Quarter(state) => println!("State quarter from {:?}!", state),
    _ => count += 1,
}
```

简单的情况

```rust
let mut count = 0;
if let Coin::Quarter(state) = coin {
    println!("State quarter from {:?}!", state);
} else {
    count += 1;
}
```

</details>

