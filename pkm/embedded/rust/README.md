# Rust

按照邓老师 B 站以及那个网站来总结，因为是第一次学，所以就写成代码集锦吧。

* 邓老师 rust 合集：[https://space.bilibili.com/504069720/channel/collectiondetail?sid=3642485](https://space.bilibili.com/504069720/channel/collectiondetail?sid=3642485)
* google rust 培训：[https://google.github.io/comprehensive-rust/](https://google.github.io/comprehensive-rust/)
* gitbook
  * 官网翻译：[https://rustwiki.org/zh-CN/book/title-page.html](https://rustwiki.org/zh-CN/book/title-page.html)
  * 布朗大学改进：[https://rust-book.cs.brown.edu/](https://rust-book.cs.brown.edu/)
* Rust Language Cheat Sheet：[https://cheats.rs/](https://cheats.rs/)

* [入门指南](notes/ru-men-zhi-nan.md)：认识rust和cargo
* [猜数字案例](notes/bian-xie-cai-shu-zi-you-xi.md)：进阶版hello world



第 2 章是 Rust 语⾔的实战介绍。我们会站在较⾼的层次介绍⼀些概念，⽽将详细的介绍放在稍后的章节中。如果你希望⽴刻就动⼿实践⼀下，第 2 章正好适合你。开始阅读时，你甚⾄可能希望略过第 3 章，它介绍了 Rust 中类似其他编程语⾔中的功能，并直接阅读第 4 章学习Rust 的所有权系统。然⽽，如果你是特别重视细节的学习者，并倾向于在继续之前学习每⼀个细节，你可能希望略过第 2 章并直接阅读第 3 章，并在想要构建项⽬来实践这些细节时再回来阅读第 2 章。

第 5 章讨论结构体和⽅法，第 6 章介绍枚举、 match 表达式和 if let 控制流结构。在 Rust中，你将使⽤结构体和枚举创建⾃定义类型。

第 7 章你会学习 Rust 的模块系统和私有性规则来组织代码和公有应⽤程序接⼝（Application Programming Interface, API）。第 8 章讨论了⼀些标准库提供的常⻅集合数据结构，⽐如可变⻓数组（vector）、字符串和哈希 map。第 9 章探索了 Rust 的错误处理哲学和技术。

第 10 章深⼊介绍泛型、trait 和⽣命周期，他们提供了定义出适⽤于多种类型的代码的能⼒。

第11 章全部关于测试，即使 Rust 有安全保证，也需要测试确保程序逻辑正确。

第 12 章，我们构建了属于⾃⼰的在⽂件中搜索⽂本的命令⾏⼯具 grep 的⼦集功能实现。为此会利⽤之前章节讨论的很多概念。

第 13 章探索了闭包和迭代器：Rust 中来⾃函数式编程语⾔的功能。

第 14 章会更深层次的理解 Cargo 并讨论向他⼈分享库的最佳实践。

第 15 章讨论标准库提供的智能指针以及启⽤这些功能的 trait。

第 16 章会学习不同的并发编程模型，并讨论 Rust 如何助你⽆畏的编写多线程程序。

第 17 章着眼于⽐较 Rust ⻛格与你可能熟悉的⾯向对象编程原则。

第 18 章是关于模式和模式匹配的参考章节，它是在 Rust 程序中表达思想的有效⽅式。

第 19 章是⼀个⾼级主题⼤杂烩，包括 unsafe Rust、宏和更多关于⽣命周期、 trait、类型、函数和闭包的内容。

第 20 章将会完成⼀个项⽬，我们会实现⼀个底层的、多线程的 web server！

最后是⼀些附录，包含了⼀些关于语⾔的参考⻛格格式的实⽤信息。附录 A 介绍了 Rust 的关键字。附录 B 介绍 Rust 的运算符和符号。附录 C 介绍标准库提供的派⽣ trait。附录 D 涉及了⼀些有⽤的开发⼯具，附录 E 介绍了 Rust 的不同版本。