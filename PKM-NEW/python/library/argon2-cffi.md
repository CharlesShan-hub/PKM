# argon2-cffi

`argon2-cffi` 是一个用于 Python 的库，它提供了对 Argon2 密码散列算法的支持。Argon2 是一种安全的密码散列算法，它被设计为具有可配置的运行时间和内存消耗。这意味着你可以决定散列密码所需的时间和所需的内存量。Argon2 有三种变体：Argon2d、Argon2i 和 Argon2id。其中，Argon2d 的优势在于抵抗时间内存交易，而 Argon2i 的重点在于抵抗侧信道攻击。因此，Argon2i 最初被认为是密码散列和密码管理的首选。

`argon2-cffi` 是使用 Argon2 算法在 Python 中进行密码散列的最简单方法。它通过 CFFI（Python 的 C 扩展构建框架）提供对 Argon2 算法的低级绑定。这使得在 Python 应用程序中使用 Argon2 变得高效且易于集成。

要使用 `argon2-cffi`，你可以从 PyPI 安装它，并通过以下代码示例开始使用：

```python
from argon2 import PasswordHasher
ph = PasswordHasher()
hash = ph.hash("correct horse battery staple")
print(hash)
```

这段代码将散列提供的密码，并打印出散列后的值。`argon2-cffi` 还提供了其他功能，如验证散列密码、检查是否需要重新散列等。

`argon2-cffi` 的最新版本是 23.1.0，发布于 2023 年 8 月 15 日。它由 Hynek Schlawack 维护，并获得了 Variomedia AG、Tidelift 订阅者以及个人捐赠者的支持。更多关于 `argon2-cffi` 的信息，包括其文档、源代码和贡献者信息，可以在其官方 GitHub 页面中找到。
