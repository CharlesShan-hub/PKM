# SORT 命令的实现

**来源**：《Redis设计与实现》第 21 章

---

## 概述

`SORT` 命令可以对列表、集合、有序集合进行排序，并支持多种选项：

```
SORT key [BY pattern] [LIMIT offset count] [GET pattern [GET pattern ...]]
      [ASC|DESC] [ALPHA] [STORE destination]
```

## SORT 命令的基本实现

```
def SORT(key):
    # 1. 取出待排序数据
    elements = LOAD(key)
    
    # 2. 根据 ALPHA/ASC/DESC 排序
    if ALPHA:
        SORT_ALPHA(elements)
    else:
        SORT_NUMERIC(elements)
    if DESC:
        REVERSE(elements)
    
    # 3. 应用 LIMIT
    result = elements[offset: offset + count]
    
    # 4. 应用 GET 选项（若有）
    if GET:
        result = GET_PATTERNS(result)
    
    # 5. 返回结果（或 STORE 保存）
    return result
```

## 各选项的实现

### ALPHA 选项

使用字符串排序（按字典序）；默认按数字排序：

```
SORT key ALPHA
```

### ASC / DESC 选项

- ASC（默认）：从小到大
- DESC：从大到小

### BY 选项

指定排序所依据的键模式：

```
SORT fruits BY *-price
```
将 fruits 列表中的每个元素作为 `*` 的替代值去查找对应键的值，按该值排序。

### LIMIT 选项

`LIMIT offset count` — 返回排序结果的 offset 到 offset+count 区间。

### GET 选项

获取排序结果中每个元素对应的其他键的值：

```
SORT fruits GET *-price GET *-stock
```

### STORE 选项

将排序结果保存到指定键，而不是返回给客户端：

```
SORT fruits STORE sorted-fruits
```

## 多个选项的执行顺序

```
SORT key [BY] [LIMIT] [GET] [ASC|DESC] [ALPHA] [STORE destination]
```

执行顺序：
1. **排序**：BY → ALPHA/ASC/DESC → 排序
2. **截取**：LIMIT
3. **获取**：GET
4. **保存**：STORE
5. **返回**
