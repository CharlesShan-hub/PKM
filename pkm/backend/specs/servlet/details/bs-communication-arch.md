
# BS 结构通信流程

> 这个过程需要背下来。

以下是基于 B/S（Browser/Server）结构的系统通信流程，从用户输入 URL 开始的简化步骤：

## 用户输入 URL

- 用户在浏览器地址栏输入 URL（如 `https://www.example.com`）。

## DNS 解析

- 浏览器检查本地缓存（如 Hosts 文件、浏览器 DNS 缓存）是否有域名对应的 IP 地址。
- 若未找到，向**本地 DNS 服务器**发起递归查询，最终通过 DNS 层级解析获取 IP（如 `93.184.216.34`）。

## 建立 TCP 连接

- 浏览器通过 IP 地址和默认端口（HTTP:80 / HTTPS:443）向服务器发起**TCP 三次握手**，建立连接。
- 若为 HTTPS，会额外进行 TLS 握手（交换证书、协商加密密钥等）。

## 发送 HTTP 请求

- 浏览器构造**HTTP 请求报文**（如 `GET /index.html HTTP/1.1`），包含请求头（User-Agent、Cookie 等）和请求体（如 POST 数据）。
- 示例请求方法：`GET`、`POST`等。

## 服务器处理请求

- 服务器（如 Tomcat）接收请求，根据路径转发到后端应用（如 Java Servlet）。
- 后端程序处理业务逻辑（查询数据库、调用 API 等），生成响应数据（如 HTML/JSON）。

## 服务器返回 HTTP 响应

- 服务器返回**HTTP 响应报文**，包含状态码（如 `200 OK`）、响应头（Content-Type 等）和响应体（如 HTML 内容）。

## 浏览器解析渲染

- 浏览器解析 HTML，逐行构建 DOM 树。渲染页面。

## 断开连接

- 完成传输后，若 HTTP 头 `Connection: close`或协议为 HTTP/1.0，则通过**TCP 四次挥手**断开连接；HTTP/1.1 默认保持长连接复用。
