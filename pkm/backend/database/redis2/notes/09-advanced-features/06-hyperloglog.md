# HyperLogLog

> 完整原理讲解参见：`d:\project\PKM\pkm\backend\database\redis\notes\other.md`

## 概述

HyperLogLog 用极小空间（约 12KB）估算海量数据中不重复元素的个数，接受微小误差（约 1%）。

## 核心命令

| 命令 | 说明 |
|------|------|
| `PFADD key element [element ...]` | 添加元素 |
| `PFCOUNT key [key ...]` | 返回基数估算值 |
| `PFMERGE destkey source [source ...]` | 合并多个 HyperLogLog |

## 应用场景

UV 统计（独立访客数），只需约 12KB 即可统计上亿级别的 UV。
