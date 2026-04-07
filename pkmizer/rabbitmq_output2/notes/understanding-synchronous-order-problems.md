# 以下单功能为例理解同步模式下的问题
## 用户等待时间长【同步】
<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1763726658488-9d52329b-675f-40c4-9b6e-a14705d0e670.png" width="902.4000244140625" title="" crop="0,0,1,1" id="u89d79c43" class="ne-image">

**<font style="color:rgb(15, 17, 21);">用户等待时间长体现在：</font>**

1. **<font style="color:rgb(15, 17, 21);">串行阻塞</font>**<font style="color:rgb(15, 17, 21);">：每个步骤必须等待前一个步骤完成才能开始</font>
2. **<font style="color:rgb(15, 17, 21);">累积延迟</font>**<font style="color:rgb(15, 17, 21);">：总时间 = 订单服务 + 库存服务 + 支付服务 + 物流服务 的耗时总和</font>
3. **<font style="color:rgb(15, 17, 21);">网络IO等待</font>**<font style="color:rgb(15, 17, 21);">：每个服务间的网络通信都有延迟</font>
4. **<font style="color:rgb(15, 17, 21);">下游依赖</font>**<font style="color:rgb(15, 17, 21);">：任何一个下游服务响应慢，都会直接影响用户等待时间</font>

**<font style="color:rgb(15, 17, 21);">举例说明：</font>**

+ <font style="color:rgb(15, 17, 21);">订单服务：100ms</font>
+ <font style="color:rgb(15, 17, 21);">库存服务：200ms</font>
+ <font style="color:rgb(15, 17, 21);">支付服务：300ms</font>
+ <font style="color:rgb(15, 17, 21);">物流服务：150ms</font>
+ **<font style="color:rgb(15, 17, 21);">用户总等待时间 ≈ 750ms</font>**

<font style="color:rgb(15, 17, 21);">在同步模式下，用户必须等待所有这些操作</font>**<font style="color:rgb(15, 17, 21);">全部完成</font>**<font style="color:rgb(15, 17, 21);">才能得到响应，即使有些操作（如通知物流）并不需要立即完成。</font>

## <font style="color:rgb(15, 17, 21);">用户等待时间短（异步）</font>
<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1763726710111-1df4d3d2-e0c0-4b2e-8e9c-7abe21fc9689.png" width="816.4000244140625" title="" crop="0,0,1,1" id="ucb51bb32" class="ne-image">

**<font style="color:rgb(15, 17, 21);">用户等待时间短体现在：</font>**

1. **<font style="color:rgb(15, 17, 21);">只等待核心</font>**<font style="color:rgb(15, 17, 21);">：总时间 = 订单服务 + 消息发送确认，不包含业务处理时间（不影响</font>**<font style="color:rgb(15, 17, 21);">给用户响应的动作</font>**<font style="color:rgb(15, 17, 21);">可以放到后台慢慢做。）</font>
2. **<font style="color:rgb(15, 17, 21);">并行触发</font>**<font style="color:rgb(15, 17, 21);">：所有下游服务通过消息队列并行触发，无需串行等待（用了消息队列多个服务可以并行执行了）</font>

**<font style="color:rgb(15, 17, 21);">举例说明：</font>**

+ <font style="color:rgb(15, 17, 21);">订单服务：100ms</font>
+ <font style="color:rgb(15, 17, 21);">消息发送确认：50ms（3个消息并行发送）</font>
+ <font style="color:rgb(15, 17, 21);">~~</font><font style="color:rgb(15, 17, 21);">库存服务：200ms</font><font style="color:rgb(15, 17, 21);">~~</font><font style="color:rgb(15, 17, 21);">（异步处理）</font>
+ <font style="color:rgb(15, 17, 21);">~~</font><font style="color:rgb(15, 17, 21);">支付服务：300ms</font><font style="color:rgb(15, 17, 21);">~~</font><font style="color:rgb(15, 17, 21);">（异步处理）</font>
+ <font style="color:rgb(15, 17, 21);">~~</font><font style="color:rgb(15, 17, 21);">物流服务：150ms</font><font style="color:rgb(15, 17, 21);">~~</font><font style="color:rgb(15, 17, 21);">（异步处理）</font>
+ **<font style="color:rgb(15, 17, 21);">用户总等待时间 ≈ 150ms</font>**

## <font style="color:rgb(15, 17, 21);">功能耦合度高【同步】</font>
**同步等于是一个串联电路，一个环节出问题，全部失败。**

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1763727530205-2bde3e5f-ed9e-461b-bb87-ac978d0df7bb.png" width="2672" title="" crop="0,0,1,1" id="u09026b91" class="ne-image">

**故障传播路径：**

**支付服务故障 → 通知服务不被调用 → 订单服务收到错误 → 客户端收到失败响应**

## 功能解耦【异步】
**异步等于是一个并联电路，一个环节出问题，其他服务不受影响。**

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1763727740610-7e2d9d66-d7cc-4c0b-b192-b12cdbc7c882.png" width="641.4000244140625" title="" crop="0,0,1,1" id="ua0cf5420" class="ne-image">

**支付服务失败了，没有关系，其他功能不受影响，并且支付服务可以采用失败重试机制，如果重试不行，可以选择人工干预。**

## 并发时压力向后传递【同步】
并发时假设 1000QPS，那么服务链上的每个节点都要具备 1000QPS 的处理能力。假设其中库存服务的只能承受住 500QPS，那么系统的整体性能会受限于最慢的这个服务，最终导致请求堆积、响应超时、连接耗尽、服务雪崩。

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1763728274079-1fb6a937-7d72-4d6f-b051-28ffe5564628.png" width="412.4000244140625" title="" crop="0,0,1,1" id="u629aaef3" class="ne-image">

## 并发时压力吸收，形成削峰填谷【异步】
高并发时，只是将大量的消息**积压在消息队列**中，消息队列来承受压力，等于消息队列是一个缓冲区。它可以保护后面的服务，因为这些服务慢慢处理也是可以的，没必要立即处理完。

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1763728553131-414568ca-8161-4238-bac7-dcb27c9673ec.png" width="666.4000244140625" title="" crop="0,0,1,1" id="uae9fa983" class="ne-image">



**怎么理解削峰填谷：**

同步模式下：高峰期来了，超过硬件承受能力，容易造成服务器宕机。低谷期来了，服务器资源大量闲置，造成浪费。

异步模式下：引入消息队列之后，将高峰期的并发积压到消息队列中，消息队列慢慢消费，这样服务器的资源在低谷期也不会闲置。

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1763729202513-aa03270a-4aae-4cb7-989e-5c3cf3af8a0c.png" width="650.4000244140625" title="" crop="0,0,1,1" id="ue94dc298" class="ne-image">

## 同步模式扩展性差，异步模式扩展性强
**假设我要在同步的模式下，扩展一个发短信的功能：**

```java
class OrderService {
    
    public void processOrder(Order order) {
        // 1. 验证订单
        validateOrder(order);
        
        // 2. 扣减库存
        inventoryService.deduct(order);
        
        // 3. 创建支付记录
        paymentService.create(order);
        
        // 4. ~~~~以同步的方式新增一个发送短信的功能~~~~
        smsService.sendOrderSMS(order);
        
        // 5. 记录日志
        logService.log(order);
    }
}
```

**缺点：**

1. 如果新增的发短信的业务挂了，会影响到主业务。
2. OrderService 需要全景回归测试。



**在异步的模式下，扩展一个发短信的功能：原始代码如下**

```java
// 原始代码如下：
class OrderService {
    
    public void processOr