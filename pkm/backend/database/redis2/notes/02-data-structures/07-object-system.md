# 对象系统

**来源**：《Redis设计与实现》第 8 章

---

## 概述

Redis 没有直接使用 SDS、链表、字典等数据结构实现键值对数据库，而是基于这些数据结构创建了一个 **对象系统**，包含 5 种类型的对象：

1. 字符串对象
2. 列表对象
3. 哈希对象
4. 集合对象
5. 有序集合对象

## 对象的类型与编码

```c
typedef struct redisObject {
    unsigned type:4;       // 类型
    unsigned encoding:4;   // 编码
    void *ptr;             // 指向底层实现数据结构的指针
    // ...
} robj;
```

### 类型（type）

| 类型常量 | 对象名称 | TYPE 命令输出 |
|----------|----------|--------------|
| REDIS_STRING | 字符串对象 | "string" |
| REDIS_LIST | 列表对象 | "list" |
| REDIS_HASH | 哈希对象 | "hash" |
| REDIS_SET | 集合对象 | "set" |
| REDIS_ZSET | 有序集合对象 | "zset" |

> 键总是一个字符串对象，值可以是上述 5 种之一。

### 编码（encoding）与底层实现

| 编码常量 | 底层数据结构 | 对应对象 |
|----------|-------------|----------|
| REDIS_ENCODING_INT | long 类型整数 | 字符串对象 |
| REDIS_ENCODING_EMBSTR | embstr 编码的 SDS | 字符串对象 |
| REDIS_ENCODING_RAW | SDS | 字符串对象 |
| REDIS_ENCODING_HT | 字典 | 哈希/集合对象 |
| REDIS_ENCODING_LINKEDLIST | 双端链表 | 列表对象（旧版） |
| REDIS_ENCODING_ZIPLIST | 压缩列表 | 列表/哈希/有序集合对象 |
| REDIS_ENCODING_INTSET | 整数集合 | 集合对象 |
| REDIS_ENCODING_SKIPLIST | 跳跃表 + 字典 | 有序集合对象 |

## 类型检查与命令多态

- **类型检查**：执行命令前检查对象的 type 属性，不匹配则返回类型错误
- **命令多态**：同一个命令在不同编码上采用不同的实现方式（如 LLEN 对 ziplist 和 linkedlist 两种编码有不同的处理）

## 内存回收

Redis 的对象系统基于 **引用计数** 技术实现内存回收：

- 创建对象时引用计数初始化为 1
- 被新程序使用时引用计数 +1
- 不再被使用时引用计数 -1
- 引用计数变为 0 时释放对象内存

## 对象共享

- 引用计数还用于对象共享机制
- Redis 会预先创建一些整数值对象（0~9999），多个键可以共享这些对象，节约内存

## 对象的空转时长

- redisObject 中的 lru 属性记录了对象最后一次被访问的时间
- `OBJECT IDLETIME key` 可以查看对象的空转时长
- 在 `maxmemory` 功能启用时，空转时长较大的键可能优先被删除（volatile-lru / allkeys-lru 策略）

## 编码转换条件

| 对象 | 编码方式 | 转换条件（转为其他编码） |
|------|----------|------------------------|
| 列表对象 | ziplist → linkedlist | 元素数量 > 512 或元素长度 > 64 字节 |
| 哈希对象 | ziplist → hashtable | 键值对数量 > 512 或键/值长度 > 64 字节 |
| 集合对象 | intset → hashtable | 元素包含非整数或元素数量 > 512 |
| 有序集合对象 | ziplist → skiplist | 元素数量 > 128 或成员长度 > 64 字节 |
| 字符串对象 | int → embstr → raw | 数字保存为 int；短字符串为 embstr；长字符串为 raw |

## 重点回顾

1. Redis 对象系统基于引用计数实现内存回收
2. 0~9999 的整数值会被共享
3. 每种类型对象都至少使用了两种编码（根据具体场景优化）
4. 编码转换是单向的（从小内存向大内存转换）
