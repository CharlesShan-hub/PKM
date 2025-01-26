# 入门指南

https://rustwiki.org/zh-CN/book/ch01-00-getting-started.html

在 Linux、macOS 和 Windows 上安装 Rust。（`rustup`是下载 rust 的工具，`rustc` 是编译的工具，`cargo` 是集成的工具）

* 更新：`rustup update`
* 版本：`rustc --version`

编写一个打印 `Hello, world!` 的程序

{% code title="main.rs" %}
```rust
fn main() {
    println!("Hello, world!");
}
```
{% endcode %}

<pre class="language-bash"><code class="lang-bash">(base) kimshan@MacBook-Pro use_rustc % ls
main.rs
<strong>(base) kimshan@MacBook-Pro use_rustc % rustc main.rs
</strong><strong>(base) kimshan@MacBook-Pro use_rustc % ./main
</strong>Hello World!
</code></pre>

使用 `cargo`，这是 Rust 的包管理器和构建系统

* 版本：`cargo --version`
* build（编译，产生可执行文件）：`cargo build`
* build+run（编译+运行）：`cargo run`
* check（编译不产生可执行文件）：`cargo check`

<pre class="language-bash"><code class="lang-bash"><strong>(base) kimshan@MacBook-Pro LearnRust % cargo new hello_world
</strong>     Created binary (application) `hello_world` package
error: could not find `Cargo.toml` in `/Users/kimshan/workplace/LearnRust` or any parent directory
(base) kimshan@MacBook-Pro LearnRust % cd hello_world 
<strong>(base) kimshan@MacBook-Pro hello_world % cargo run            
</strong>   Compiling hello_world v0.1.0 (/Users/kimshan/workplace/LearnRust/hello_world)
    Finished dev [unoptimized + debuginfo] target(s) in 1.04s
     Running `target/debug/hello_world`
Hello, world!
</code></pre>
