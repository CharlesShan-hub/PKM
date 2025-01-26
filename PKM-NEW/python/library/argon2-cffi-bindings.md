# argon2-cffi-bindings

`argon2-cffi-bindings` 是一个用于 Python 的库，它提供了对 Argon2 密码散列算法的低级 CFFI 绑定。Argon2 是一种安全的密码散列算法，被设计为具有可配置的运行时间和内存消耗，以抵御不同的攻击类型。`argon2-cffi-bindings` 通过 CFFI 提供了对 Argon2 算法的低级绑定，使得在 Python 应用程序中使用 Argon2 变得高效且易于集成。 这个库的目的是为其他需要使用 Argon2 库的 Python 包提供底层支持，而不需要处理与 C 相关的复杂性。它包含了对 Argon2 算法的官方实现版本，并且可以被其他包所使用。不过，需要注意的是，如果您的目的是在应用程序中散列密码，那么这个包可能不适合您的需求。在这种情况下，您应该考虑使用 `argon2-cffi`，它提供了更高层次的抽象和更易于使用的接口。 要使用 `argon2-cffi-bindings`，您可以从 PyPI 安装它，并通过相应的 Python 代码进行使用。不过，由于这个库提供了低级绑定，它的使用可能需要一定的技术背景和理解。 更多信息和文档可以在 `argon2-cffi-bindings` 的官方 PyPI 页面、Libraries.io 页面以及相关文档页面中找到。
