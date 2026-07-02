# Bitmaps（位图）

> 完整内容参见：`d:\project\PKM\pkm\backend\database\redis\notes\other.md`

## 概述

Bitmaps 是 String 的一种特殊用法——每个字节的 8 个位分别用作布尔标记。

## 相关命令

| 命令 | 说明 |
|------|------|
| `SETBIT key offset value` | 设置指定偏移量的位值（0 或 1） |
| `GETBIT key offset` | 获取指定偏移量的位值 |
| `BITCOUNT key [start end]` | 统计位值为 1 的数量 |
| `BITOP op destkey key [key ...]` | 对多个位图执行 AND/OR/NOT/XOR |

## 底层实现

Redis 使用 SDS 作为位数组的底层表示，通过 `SETBIT`、`GETBIT`、`BITCOUNT`、`BITOP` 四个核心命令实现位操作。

### BITCOUNT 算法

BITCOUNT 使用了查表法 + 变量循环的优化策略：

1. 按 128 位为一批处理
2. 每批使用查表法计算 32 位的汉明重量
3. 最后处理剩余位数
