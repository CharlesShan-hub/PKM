# async-lru

`async-lru` 是一个专为 `asyncio` 设计的轻量级 LRU（Least Recently Used，最近最少使用）缓存实现。它解决了在异步环境中有效管理内存和重复计算的问题。这个库是基于 Python 内置的 `functools.lru_cache` 函数，但针对异步行为进行了优化。它确保多个并发调用只会导致对包装函数的一次调用，当该调用完成后，所有等待的请求都会收到该调用的结果。 `async-lru` 的主要特点包括：

1. **异步优化**：它特别优化了异步环境下的缓存操作，提高了在异步程序中的效率。
2. **内存管理**：通过使用 LRU 缓存机制，它可以有效管理内存，减少不必要的重复计算。
3. **兼容性**：与 Python 的 `functools.lru_cache` 功能兼容，但提供了异步的支持。 要使用 `async-lru`，你可以通过 pip 进行安装：

```bash
pip install async-lru
```

更多信息和文档可以在 `async-lru` 的官方 PyPI 页面、CSDN 博客以及 Anaconda.org 页面中找到。
