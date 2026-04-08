# 消息超时机制
消息在消息队列里放的时间太长，会导致消息队列内存耗尽，消息超时机制就是来解决这个问题的。

消息超时会被自动删除。



**可以从两个层面设置消息的超时机制：**

1. （类似于全局设置）设置消息队列的超时时间，这种方式将作用于消息队列当中的所有消息。（不是队列的超时时间，是队列中**所有消息**的超时时间。）
2. （类似于局部设置）通过代码设置某个消息的超时时间。

如果同时设置，以时间短的为准。

## 设置队列的超时时间
在 web 界面操作：

1. 创建交换机：`exchange.timeout`

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1763896968333-b865fd9d-d7aa-4426-a557-0ba25cef4aa1.png" width="506.4" title="" crop="0,0,1,1" id="u722f0079" class="ne-image">

2. 创建队列：`queue.timeout`

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1763897083238-885377f0-be73-47c7-ab23-72609e03639d.png" width="723.2" title="" crop="0,0,1,1" id="uf5e569bc" class="ne-image">

3. 配置路由键，绑定交换机和队列：`routing.key.timeout`

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1763897154516-58ab64b5-6e6c-40f3-87d4-7167889c25da.png" width="824.8" title="" crop="0,0,1,1" id="u9a85fcca" class="ne-image">



**在 **`**producer_confirm**`**项目中编写测试代码，生产端发送 100 条消息到队列，看看超时之后，消息是否全部删除：**

```java
public static final String EXCHANGE_TIMEOUT = "exchange.timeout";
public static final String ROUTING_KEY_TIMEOUT = "routing.key.timeout";
@Test
void test02() {
    for (int i = 0; i < 100; i++) {
        rabbitTemplate.convertAndSend(EXCHANGE_TIMEOUT, ROUTING_KEY_TIMEOUT, "hello rabbit " + i);
    }
}
```

运行测试程序，观察 web 管理界面：

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1763897508094-4be978e4-dbe3-4837-8be9-056f1caf4061.png" width="197.6" title="" crop="0,0,1,1" id="u8bf86499" class="ne-image">

10 秒超时后：

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1763897515548-9783d76a-c5f4-4734-a70a-5319e7a482cc.png" width="171.2" title="" crop="0,0,1,1" id="ue16e320e" class="ne-image">

## 通过代码设置某条消息的超时时间
**在 **`**producer_confirm**`**项目中编写测试代码，生产端发送 1 条****<font style="color:#DF2A3F;">设置了超时时间</font>****的消息到队列，看看超时之后，消息是否全部删除：**

```java
@Test
void test03() {
    // 创建消息后处理器，这也是一个回调
    MessagePostProcessor messagePostProcessor = message -> {
        // 设置当前消息的超时时间为7秒
        message.getMessageProperties().setExpiration("7000");
        return message;
    };
    // 发送消息（记得将上面的消息后处理对象传到下面方法的末尾参数位置上）
    rabbitTemplate.convertAndSend(EXCHANGE_TIMEOUT, ROUTING_KEY_TIMEOUT, "hello rabbit", messagePostProcessor);
}
```

运行测试，看看 7 秒后该消息是否自动删除。

