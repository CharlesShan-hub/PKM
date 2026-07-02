# 事件的调度与执行

**来源**：《Redis设计与实现》第 12 章

---

## 调度函数 aeProcessEvents

服务器通过 `aeProcessEvents` 函数对文件事件和时间事件进行统一调度：

```
def aeProcessEvents():
    # 1. 查找最近要到达的时间事件
    time_event = aeSearchNearestTimer()
    
    # 2. 计算距离到达还有多少毫秒
    remaind_ms = time_event.when - unix_ts_now()
    if remaind_ms < 0:
        remaind_ms = 0
    
    # 3. 根据 remaind_ms 创建 timeval 结构
    timeval = create_timeval_with_ms(remaind_ms)
    
    # 4. 阻塞等待文件事件（最多等待 remaind_ms 毫秒）
    aeApiPoll(timeval)
    
    # 5. 处理所有已产生的文件事件
    processFileEvents()
    
    # 6. 处理所有已到达的时间事件
    processTimeEvents()
```

## 服务器主循环

```
def main():
    init_server()
    while server_is_not_shutdown():
        aeProcessEvents()
    clean_server()
```

## 调度规则

| 规则 | 说明 |
|------|------|
| **1. 阻塞时间由最近时间事件决定** | aeApiPoll 的最大阻塞时间由最近的时间事件决定，避免忙等待又不会阻塞过久 |
| **2. 文件事件优先处理** | 处理完文件事件后若时间事件仍未到达，继续等待和处理文件事件 |
| **3. 同步有序执行** | 文件事件和时间事件都是同步、有序、原子地执行，不抢占 |
| **4. 时间事件可能延迟** | 时间事件总是在文件事件之后执行，实际处理时间可能比预定时间稍晚 |
