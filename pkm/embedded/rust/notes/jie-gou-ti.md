# 结构体

https://rustwiki.org/zh-CN/book/ch05-00-structs.html

## [**5.1.** 定义和举例说明结构体](https://rustwiki.org/zh-CN/book/ch05-01-defining-structs.html)

<details>

<summary>基础的定义与赋值</summary>

```rust
// 定义结构体
struct User {
    active: bool,
    username: String,
    email: String,
    sign_in_count: u64,
}

fn main() {
    // 生成结构体
    // 注意整个实例必须是可变的；Rust 并不允许只将某个字段标记为可变
    let mut user1 = User {
        email: String::from("someone@example.com"),
        username: String::from("someusername123"),
        active: true,
        sign_in_count: 1,
    };

    // 改变结构体中的值
    user1.email = String::from("anotheremail@example.com");
}
```

</details>

<details>

<summary>基础的定义与赋值 之 结构体应拥有数据的所有权</summary>

<pre class="language-rust"><code class="lang-rust">struct User {
    active: bool,
<strong>    username: &#x26;str, // wrong! use String!
</strong><strong>    email: &#x26;str, // wrong! use String!
</strong>    sign_in_count: u64,
}

fn main() {
    let user1 = User {
        email: "someone@example.com",
        username: "someusername123",
        active: true,
        sign_in_count: 1,
    };
}

</code></pre>

</details>

<details>

<summary>语法糖：变量与字段同名</summary>

<pre class="language-rust"><code class="lang-rust">struct User {
    active: bool,
    username: String,
    email: String,
    sign_in_count: u64,
}

fn build_user(email: String, username: String) -> User {
    User {
<strong>        email,    // email:email,
</strong><strong>        username, // username:username,
</strong>        active: true,
        sign_in_count: 1,
    }
}

fn main() {
    let user1 = build_user(
        String::from("someone@example.com"),
        String::from("someusername123"),
    );
}

</code></pre>

</details>

<details>

<summary>语法糖：从别的结构体为模板创建新结构体</summary>

<pre class="language-rust"><code class="lang-rust">struct User {
    active: bool,
    username: String,
    email: String,
    sign_in_count: u64,
}

fn main() {
    let user1 = User {
        email: String::from("someone@example.com"),
        username: String::from("someusername123"),
        active: true,
        sign_in_count: 1,
    };

    // let user2 = User {
    //     active: user1.active,
    //     username: user1.username,
    //     email: String::from("another@example.com"),
    //     sign_in_count: user1.sign_in_count,
    // };

    let user2 = User {
        email: String::from("another@example.com"),
<strong>        ..user1
</strong>    };
}
</code></pre>

</details>

<details>

<summary>元组结构体</summary>

```rust
struct Color(i32, i32, i32);
struct Point(i32, i32, i32);

fn main() {
    let black = Color(0, 0, 0);
    let origin = Point(0, 0, 0);
}
```

</details>

<details>

<summary>没有任何字段的类单元结构体</summary>

```rust
struct AlwaysEqual;

fn main() {
    let subject = AlwaysEqual;
}
```

</details>

***

## [**5.2.** 使用结构体的代码例子](https://rustwiki.org/zh-CN/book/ch05-02-example-structs.html)

需求 1：我们打算做的是，打印矩形面积。

<details>

<summary>分别定义长度与宽度</summary>

```rust
fn main() {
    let width1 = 30;
    let height1 = 50;

    println!(
        "The area of the rectangle is {} square pixels.",
        area(width1, height1)
    );
    // The area of the rectangle is 1500 square pixels.
}

fn area(width: u32, height: u32) -> u32 {
    width * height
}
```

</details>

<details>

<summary>采用元组定义矩形</summary>

```rust
fn main() {
    let rect1 = (30, 50);

    println!(
        "The area of the rectangle is {} square pixels.",
        area(rect1)
    );
    // The area of the rectangle is 1500 square pixels.
}

fn area(dimensions: (u32, u32)) -> u32 {
    dimensions.0 * dimensions.1
}
```

</details>

<details>

<summary>采用结构体定义矩形</summary>

```rust
struct Rectangle {
    width: u32,
    height: u32,
}

fn main() {
    let rect1 = Rectangle {
        width: 30,
        height: 50,
    };

    println!(
        "The area of the rectangle is {} square pixels.",
        area(&rect1)
    );
    // The area of the rectangle is 1500 square pixels.
}

fn area(rectangle: &Rectangle) -> u32 {
    rectangle.width * rectangle.height
}
```

</details>

需求 2：直接打印数据集结构的内容

<details>

<summary>使用trait Debug，并通过 println! 宏打印</summary>

<pre class="language-rust"><code class="lang-rust"><strong>#[derive(Debug)]
</strong>struct Rectangle {
    width: u32,
    height: u32,
}

fn main() {
    let rect1 = Rectangle {
        width: 30,
        height: 50,
    };

<strong>    println!("rect1 is {:?}", rect1);
</strong>    // rect1 is Rectangle { width: 30, height: 50 }，
<strong>    println!("rect1 is {:#?}", rect1);
</strong>    // rect1 is Rectangle {
    //     width: 30,
    //     height: 50,
    // }
}
</code></pre>

</details>

<details>

<summary>使用trait Debug，并通过 dbg! 宏打印</summary>

```rust
#[derive(Debug)]
struct Rectangle {
    width: u32,
    height: u32,
}

fn main() {
    let scale = 2;
    let rect1 = Rectangle {
        width: dbg!(30 * scale),
        height: 50,
    };

    dbg!(&rect1); // 我们不希望 dbg! 拥有 rect1 的所有权，所以我们在下一次调用 dbg! 时传入一个引用
}
// [src/main.rs:10:16] 30 * scale = 60
// [src/main.rs:14:5] &rect1 = Rectangle {
//     width: 60,
//     height: 50,
// }

```

</details>

***

## [**5.3.** 方法语法](https://rustwiki.org/zh-CN/book/ch05-03-method-syntax.html)

<details>

<summary>方法</summary>

<pre class="language-rust"><code class="lang-rust">#[derive(Debug)]
struct Rectangle {
    width: u32,
    height: u32,
}

<strong>impl Rectangle {
</strong><strong>    fn area(&#x26;self) -> u32 { // 注意要有 self
</strong><strong>        self.width * self.height
</strong><strong>    }
</strong><strong>}
</strong>
fn main() {
    let rect1 = Rectangle {
        width: 30,
        height: 50,
    };

    println!(
        "The area of the rectangle is {} square pixels.",
<strong>        rect1.area()
</strong>    );
}

</code></pre>

</details>

<details>

<summary>带返回值的方法</summary>

<pre class="language-rust"><code class="lang-rust">#[derive(Debug)]
struct Rectangle {
    width: u32,
    height: u32,
}

<strong>impl Rectangle {
</strong><strong>    fn width(&#x26;self) -> bool {
</strong><strong>        self.width > 0
</strong><strong>    }
</strong><strong>}
</strong>
fn main() {
    let rect1 = Rectangle {
        width: 30,
        height: 50,
    };

<strong>    if rect1.width() {
</strong>        println!("The rectangle has a nonzero width; it is {}", rect1.width);
    }
}
</code></pre>

</details>

<details>

<summary>带传入参数的方法</summary>

<pre class="language-rust"><code class="lang-rust">#[derive(Debug)]
struct Rectangle {
    width: u32,
    height: u32,
}

impl Rectangle {
    fn area(&#x26;self) -> u32 {
        self.width * self.height
    }

<strong>    fn can_hold(&#x26;self, other: &#x26;Rectangle) -> bool {
</strong><strong>        self.width > other.width &#x26;&#x26; self.height > other.height
</strong><strong>    }
</strong>}

fn main() {
    let rect1 = Rectangle {
        width: 30,
        height: 50,
    };
    let rect2 = Rectangle {
        width: 10,
        height: 40,
    };
    let rect3 = Rectangle {
        width: 60,
        height: 45,
    };

<strong>    println!("Can rect1 hold rect2? {}", rect1.can_hold(&#x26;rect2));
</strong><strong>    println!("Can rect1 hold rect3? {}", rect1.can_hold(&#x26;rect3));
</strong>}
</code></pre>

</details>

<details>

<summary>可以为一个 struct 创建 多个impl</summary>

```rust
#[derive(Debug)]
struct Rectangle {
    width: u32,
    height: u32,
}

impl Rectangle {
    fn area(&self) -> u32 {
        self.width * self.height
    }
}

impl Rectangle {
    fn can_hold(&self, other: &Rectangle) -> bool {
        self.width > other.width && self.height > other.height
    }
}

fn main() {
    let rect1 = Rectangle {
        width: 30,
        height: 50,
    };
    let rect2 = Rectangle {
        width: 10,
        height: 40,
    };
    let rect3 = Rectangle {
        width: 60,
        height: 45,
    };

    println!("Can rect1 hold rect2? {}", rect1.can_hold(&rect2));
    println!("Can rect1 hold rect3? {}", rect1.can_hold(&rect3));
}
```

</details>



