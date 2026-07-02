# ACL 与 TLS/SSL

> 详细用法参考：`d:\project\PKM\pkm\backend\database\redis\notes\usage.md`

## ACL（Access Control List）

Redis 6.0 引入的访问控制系统，提供细粒度的权限控制。

### 核心概念

- 定义多个用户，每个用户有独立的密码
- 为每个用户分配特定的命令权限和键模式访问权限
- `ACL SETUSER username on >password +@all ~*`

### 常用 ACL 命令

```
ACL LIST                          # 查看所有用户
ACL SETUSER user on >pass +@read  # 创建只读用户
ACL SETUSER user ~cache:*         # 限制只能访问 cache: 前缀的键
ACL SAVE                          # 保存到配置文件
ACL DELUSER user                  # 删除用户
```

## TLS/SSL

Redis 7.0+ 支持 TLS/SSL 加密传输。

### 配置要点

1. 编译时需 `BUILD_TLS=yes`
2. Redis 配置中指定证书文件
3. Java 客户端将 Redis 证书导入 JDK 信任库
4. 连接时使用 `rediss://` 协议或 `ssl(true)` 配置

### 证书生成

使用 Redis 源码 `utils/gen-test-certs.sh` 生成自签名证书（适用于开发/局域网环境）。

生产环境一般连接云服务商的 Redis（已配置好 CA 证书）。
