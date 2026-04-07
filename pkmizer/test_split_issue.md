# 测试章节1

这是一个测试章节，包含一些代码。

```java
public void createOrder(Order order) { 
    // 1. 验证订单 
    validateOrder(order); 
    
    // 2. 扣减库存 
    inventoryService.deduct(order); 
    
    // 3. 创建支付记录 
    paymentService.create(order); 
    
    // 4. 发送消息到消息队列 
    rabbitTemplate.convertAndSend( 
        "order.exchange",      // 交换机 
        "order.completed",     // 路由键 
        order                  // 消息内容 
    ); 
    
    // 5. 记录日志 
    logService.log(order); 
} 
```

这是章节1的其余内容。

# 测试章节2

这是第二个章节。

```python
def process_data(data):
    # 处理数据
    result = data * 2
    return result
```

章节2的结束。