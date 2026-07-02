# 链表

**来源**：《Redis设计与实现》第 3 章

---

## 概述

Redis 的列表键底层实现之一就是链表（另一个是压缩列表）。当一个列表键包含较多元素或较长字符串时，Redis 会使用链表作为底层实现。

链表还被用于：发布与订阅、慢查询、监视器、保存多个客户端状态信息、构建客户端输出缓冲区。

## 实现

### 链表节点

```c
typedef struct listNode {
    struct listNode *prev;  // 前置节点
    struct listNode *next;  // 后置节点
    void *value;            // 节点的值
} listNode;
```

### 链表结构

```c
typedef struct list {
    listNode *head;                             // 表头节点
    listNode *tail;                             // 表尾节点
    unsigned long len;                          // 节点数量
    void *(*dup)(void *ptr);                    // 节点值复制函数
    void (*free)(void *ptr);                    // 节点值释放函数
    int (*match)(void *ptr, void *key);         // 节点值对比函数
} list;
```

## 特性

| 特性 | 说明 |
|------|------|
| **双端** | 有 prev 和 next 指针，获取前后节点复杂度 O(1) |
| **无环** | 头节点 prev 和尾节点 next 都指向 NULL |
| **带表头/表尾指针** | 通过 head/tail 指针，O(1) 获取首尾节点 |
| **带长度计数器** | 通过 len 属性 O(1) 获取节点数量 |
| **多态** | 节点值用 void* 保存，通过 dup/free/match 函数实现多态 |
