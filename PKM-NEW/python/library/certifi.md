# certifi

`certifi` 是一个 Python 库，它提供了一组可信的 SSL/TLS 证书。这些证书是从 Mozilla 维护的 CA 证书列表中提取的，以确保在 HTTPS 连接时使用的是可信的证书颁发机构（CA）。`certifi` 是 Python 的 `requests` 库和 `urllib3` 库的官方依赖项，用于处理网络请求。 以下是 `certifi` 的关键特点和用法：

#### 关键特点

1. **安全性**：确保 HTTPS 连接使用的是可信的 CA 证书，从而提高网络安全性。
2. **兼容性**：与 Python 的其他 SSL/TLS 库兼容，如 `requests` 和 `urllib3`。
3. **易用性**：安装后，`certifi` 会自动被 Python 的 SSL 库使用，无需手动配置。

#### 安装

可以通过pip安装`certifi`：

```bash
pip install certifi
```

#### 基本用法

由于 `certifi` 是一个库，它不需要直接调用。当你使用 `requests` 或 `urllib3` 进行 HTTPS 请求时，`certifi` 中的证书会被自动使用。 以下是一个使用 `requests` 库进行 HTTPS 请求的例子：

```python
import requests
# 发送 HTTPS 请求
response = requests.get('https://example.com')
# 打印响应内容
print(response.text)
```

在这个例子中，`requests.get` 函数用于发送一个 HTTPS 请求到 `example.com`。由于 `certifi` 已经安装，`requests` 库会自动使用 `certifi` 中的证书来验证 SSL/TLS 连接。

#### 使用场景

* **网络编程**：在需要通过 HTTPS 连接外部服务时使用 `certifi`。
* **Web 应用程序**：在需要安全地与外部服务交互的 Web 应用程序中使用 `certifi`。
* **开发工具**：在需要进行网络请求的开发工具中使用 `certifi`。 `certifi` 是一个非常实用的库，它可以帮助 Python 开发者确保他们的应用程序在安全的 SSL/TLS 环境中运行。由于它是 Python 的标准库的一部分，因此大多数 Python 环境都已经包含了这个库。
