# 编写猜数字游戏

https://rustwiki.org/zh-CN/book/ch02-00-guessing-game-tutorial.html

我们会实现一个经典的新手编程问题：猜数字游戏。这是它的工作原理：程序会随机生成一个 1 到 100 之间的整数。接着它会提示玩家猜一个数并输入，然后指出猜测是大了还是小了。如果猜对了，它会打印祝贺信息并退出。

<pre class="language-toml" data-title="Cargo.toml"><code class="lang-toml">[package]
name = "guessing_game"
version = "0.1.0"
edition = "2021"

# See more keys and their definitions at https://doc.rust-lang.org/cargo/reference/manifest.html

[dependencies]
<strong>rand = "0.8.3"
</strong></code></pre>

{% code title="main.rs" %}
```rust
use rand::Rng;
use std::cmp::Ordering;
use std::io;

fn main() {
    println!("Guess the number!");

    let secret_number = rand::thread_rng().gen_range(1..101);

    loop {
        println!("Please input your guess.");

        let mut guess = String::new();

        io::stdin()
            .read_line(&mut guess)
            .expect("Failed to read line");

        let guess: u32 = match guess.trim().parse() {
            Ok(num) => num,
            Err(_) => continue,
        };

        println!("You guessed: {}", guess);

        match guess.cmp(&secret_number) {
            Ordering::Less => println!("Too small!"),
            Ordering::Greater => println!("Too big!"),
            Ordering::Equal => {
                println!("You win!");
                break;
            }
        }
    }
}
```
{% endcode %}

***

语法比较，引入包/命名空间：

* rust：`use rand::Rng;`
* C++：`#inlude <stdlib>`，又有点像命名空间`using namespace std;`
* python：`from math import radians`

语法比较，io 后的 expect

{% code title="Rust" %}
```rust
io::stdin()
  .read_line(&mut guess)
  .expect("Failed to read line");
```
{% endcode %}

{% code title="Swift" %}
```swift
guard let guess = readLine() else {
    print("Failed to read line")
    return ""
}
```
{% endcode %}

语法比较，引用

{% code title="Rust" %}
```rust
io::stdin()
  .read_line(&mut guess)
  .expect("Failed to read line");
```
{% endcode %}

<pre class="language-cpp" data-title="C++"><code class="lang-cpp">#include &#x3C;iostream>

<strong>void modifyValue(int &#x26;value)
</strong>{
    // 通过指针修改原始变量的值
    value = 24; // 修改传入的变量值
}

int main()
{
    int number = 42;
    std::cout &#x3C;&#x3C; "原始值: " &#x3C;&#x3C; number &#x3C;&#x3C; std::endl; // 原始值: 42

<strong>    modifyValue(number);
</strong>
    std::cout &#x3C;&#x3C; "修改后的值: " &#x3C;&#x3C; number &#x3C;&#x3C; std::endl; // 修改后的值: 24

    return 0;
}
</code></pre>

语法比较，result 和 error

{% code title="Rust" %}
```rust
let guess: u32 = match guess.trim().parse() {
    Ok(num) => num,
    Err(_) => continue,
};
```
{% endcode %}

{% code title="JavaScript" %}
```javascript
contract.methods.addEventApprove(index,approve,identity).send({from:account})
.then(function(res){
    console.log("To do list reply Request Send",res);
}, function(error){
    console.log("To do list reply Failed!",error);
});
```
{% endcode %}



