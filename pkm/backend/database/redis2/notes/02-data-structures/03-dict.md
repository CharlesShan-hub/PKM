# 字典（Dict）

**来源**：《Redis设计与实现》第 4 章

---

## 概述

Redis 的数据库就是使用字典作为底层实现的，对数据库的增删查改操作都是构建在字典之上。此外，哈希键的底层实现之一也是字典。

## 实现

Redis 字典使用 **哈希表** 作为底层实现。

### 哈希表

```c
typedef struct dictht {
    dictEntry **table;      // 哈希表数组
    unsigned long size;     // 哈希表大小
    unsigned long sizemask; // 大小掩码，用于计算索引值，总是等于 size-1
    unsigned long used;     // 已有节点数量
} dictht;
```

### 哈希表节点

```c
typedef struct dictEntry {
    void *key;                  // 键
    union {
        void *val;
        uint64_t u64;
        int64_t s64;
    } v;                        // 值
    struct dictEntry *next;     // 指向下个节点，形成链表（解决冲突）
} dictEntry;
```

### 字典

```c
typedef struct dict {
    dictType *type;     // 类型特定函数
    void *privdata;     // 私有数据
    dictht ht[2];       // 两个哈希表，ht[1] 仅在 rehash 时使用
    int rehashidx;      // rehash 进度，-1 表示未进行 rehash
} dict;
```

## 哈希算法

Redis 使用 **MurmurHash2** 算法计算键的哈希值：

```
hash = dict->type->hashFunction(key);
index = hash & dict->ht[x].sizemask;
```

## 解决键冲突

使用 **链地址法**：多个哈希值相同的节点通过 next 指针构成单向链表。新节点总是添加到链表表头（O(1) 复杂度）。

## rehash（重新散列）

为了保持合理的负载因子，哈希表会进行扩展或收缩。

### rehash 步骤

1. 为 ht[1] 分配空间：
   - **扩展**：第一个大于等于 `ht[0].used * 2` 的 2^n
   - **收缩**：第一个大于等于 `ht[0].used` 的 2^n
2. 将 ht[0] 中的所有键值对 rehash 到 ht[1]
3. 释放 ht[0]，将 ht[1] 设为 ht[0]，在 ht[1] 创建空白哈希表

### 触发条件

- 负载因子 = `ht[0].used / ht[0].size`
- **扩展**：未执行 BGSAVE/BGREWRITEAOF 时负载因子 >= 1；执行时 >= 5
- **收缩**：负载因子 < 0.1

### 渐进式 rehash

为了避免大量计算阻塞服务，rehash 是分多次、渐进式完成的：

1. 为 ht[1] 分配空间，rehashidx 设为 0
2. 每次对字典执行增删改查操作时，顺带将 ht[0] 在 rehashidx 索引上的所有键值对迁移到 ht[1]
3. rehashidx 递增
4. 全部迁移完成后，rehashidx 重新设为 -1

**渐进式 rehash 期间的规则**：
- 删/改/查在两个哈希表上进行
- **新添加的键值对一律保存到 ht[1]**，ht[0] 只减不增
