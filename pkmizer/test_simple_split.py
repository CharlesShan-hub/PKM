import sys
sys.path.append('.')
from scripts.markdown_splitter import split_markdown_by_headings

# 测试简单的分割逻辑
test_content = """# 测试章节1

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

章节2的结束。"""

# 先写入测试文件
with open('test_simple.md', 'w', encoding='utf-8') as f:
    f.write(test_content)

# 测试分割
print("测试简单分割逻辑...")
sections = split_markdown_by_headings('test_simple.md')

print(f"找到 {len(sections)} 个章节")
for i, (heading, content) in enumerate(sections):
    print(f"\n章节 {i+1}: {heading}")
    print(f"内容长度: {len(content)} 字符")
    
    # 检查内容是否完整
    if 'createOrder' in content:
        if 'public void createOrder' in content and 'logService.log(order);' in content:
            print("包含完整的 createOrder 方法")
        else:
            print("createOrder 方法不完整")
            # 显示开头和结尾
            print(f"开头100字符: {content[:100]}")
            print(f"结尾100字符: {content[-100:]}")
    
    # 检查代码块
    code_blocks = content.count('```')
    print(f"包含 {code_blocks//2} 个完整代码块")