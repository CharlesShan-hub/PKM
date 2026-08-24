# 入门指南

> https://rustwiki.org/zh-CN/book/ch01-00-getting-started.html
> 第 1 章介绍如何安装 Rust，如何编写 “Hello, world!” 程序，以及如何使⽤ Rust 的包管理器和构建⼯具 Cargo。

## rustc

在 Linux、macOS 和 Windows 上安装 Rust。（`rustup`是下载 rust 的工具，`rustc` 是编译的工具，`cargo` 是集成的工具）

* 更新：`rustup update`
* 版本：`rustc --version`

编写一个打印 `Hello, world!` 的程序

```rust
// main.rs
fn main() {
    println!("Hello, world!");
}
```

```bash
(base) kimshan@MacBook-Pro use_rustc % ls
main.rs
(base) kimshan@MacBook-Pro use_rustc % rustc main.rs
(base) kimshan@MacBook-Pro use_rustc % ./main
Hello World!
```

## cargo

使用 `cargo`，这是 Rust 的包管理器和构建系统

* 版本：`cargo --version`
* build（编译，产生可执行文件）：`cargo build`
* build+run（编译+运行）：`cargo run`
* check（编译不产生可执行文件）：`cargo check`

```bash
(base) kimshan@MacBook-Pro LearnRust % cargo new hello_world  # 创建
     Created binary (application) `hello_world` package
(base) kimshan@MacBook-Pro LearnRust % cd hello_world         # 进入目录 
(base) kimshan@MacBook-Pro hello_world % cargo run            # 编译运行   
   Compiling hello_world v0.1.0 (/Users/kimshan/workplace/LearnRust/hello_world)
    Finished dev [unoptimized + debuginfo] target(s) in 1.04s
     Running `target/debug/hello_world`
Hello, world!
```

更多介绍：

1. `Cargo.toml`：包含两部分，`package`是自己的内容，`dependence`是依赖的别人的内容

```toml
[package]
name = "hello_world"
version = "0.1.0"# 这个是自己写的包本身的版本
edition = "2024" # 这个是rust的大版本

[dependencies]
```

2. `cargo build`也有多个模式

|命令|对应的 Profile|用途|
|---|---|---|
|`cargo build`|**`dev`**|**开发模式**（默认）。编译极快，但运行慢、体积大，包含完整调试信息，适合日常写代码调试。|
|`cargo build --release`|**`release`**|**发布模式**。运行极快，体积小，但编译慢，适合最终交付给用户。|
|`cargo test`|**`test`**|运行测试时使用，会做一些优化，同时支持断言和调试。|
|`cargo bench`|**`bench`**|性能基准测试时使用，会进行极致优化，以获得最准确的跑分。|
