# 跳跃表（Skiplist）

**来源**：《Redis设计与实现》第 5 章

---

## 概述

跳跃表是一种有序数据结构，通过在每个节点中维持多个指向其他节点的指针，实现快速访问。支持平均 O(log N)、最坏 O(N) 的节点查找。

Redis 使用跳跃表实现：
1. **有序集合键（ZSet）**的底层实现之一
2. **集群节点**中的内部数据结构

## 实现

### 跳跃表节点

```c
typedef struct zskiplistNode {
    struct zskiplistLevel {
        struct zskiplistNode *forward;  // 前进指针
        unsigned int span;              // 跨度（用于计算排位）
    } level[];                          // 层数组
    struct zskiplistNode *backward;     // 后退指针
    double score;                       // 分值
    robj *obj;                          // 成员对象
} zskiplistNode;
```

### 跳跃表

```c
typedef struct zskiplist {
    struct zskiplistNode *header, *tail;  // 表头、表尾节点
    unsigned long length;                 // 节点数量
    int level;                            // 最大层数（表头不计）
} zskiplist;
```

## 关键特性

### 层（Level）

- 每次创建新节点时，根据 **幂次定律** 随机生成 1~32 之间的层高
- 层数越多，访问其他节点的速度越快

### 前进指针与跨度

- **前进指针**：用于从表头向表尾遍历
- **跨度**：记录两个节点之间的距离，用于计算排位（rank）

### 后退指针

- 每个节点只有一个后退指针，从表尾向表头遍历时使用
- 每次只能后退至前一个节点

### 分值和成员

- 节点按分值从小到大排序
- 分值可以相同，相同的按成员对象字典序排序
- 成员对象必须唯一

## 节点排位计算

查找节点时，将沿途访问过的所有层跨度累计，即得到目标节点的排位。

例如查找分值为 3.0、成员为 o3 的节点，如果沿途只有一个层且跨度为 3，则该节点排位为 3。
