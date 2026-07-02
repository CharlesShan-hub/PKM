# Lua 脚本

**来源**：《Redis设计与实现》第 20 章

---

## 概述

Redis 从 2.6 版本开始支持通过 `EVAL` 和 `EVALSHA` 命令执行 Lua 脚本，使得多个命令可以在服务器端原子性地执行。

## 创建并修改 Lua 环境

Redis 在服务器初始化时创建一个专用的 Lua 环境，并对其进行修改：

1. **加载函数库**：如 `cjson`、`cmsgpack` 等
2. **创建全局表**：`redis` 全局表，提供 `redis.call()`、`redis.pcall()` 等方法
3. **替换随机函数**：确保脚本的确定性（如用自定义随机函数替代 math.random）
4. **创建排序辅助函数**：保证在不同系统中排序结果一致

## Lua 环境协作组件

- **伪客户端**：专门用于执行 Lua 脚本中的 Redis 命令
- **lua_scripts 字典**：记录所有已执行过的脚本的 SHA1 校验和与脚本体的映射

## EVAL 命令的实现

```
EVAL "return redis.call('SET', KEYS[1], ARGV[1])" 1 key value
```

执行步骤：
1. 在 Lua 环境中定义脚本函数（函数名为 `f_{SHA1}`）
2. 将脚本保存到 lua_scripts 字典
3. 执行脚本函数

## EVALSHA 命令的实现

```
EVALSHA "SHA1_sum" 1 key value
```

- 根据 SHA1 校验和从 lua_scripts 字典中查找脚本
- 找到则执行，未找到则返回错误（此时需用 EVAL 重试）

## 脚本复制

复制模式下，主服务器将脚本传播到从服务器：

- **EVAL 命令**：直接传播 EVAL
- **EVALSHA 命令**：
  1. 首先尝试传播 EVALSHA
  2. 若从服务器没有该脚本（返回 NOSCRIPT），则回退为传播 EVAL
- **写命令**：使用 `redis.replicate_commands()` 可将写命令逐个传播
