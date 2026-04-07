// 声明队列（为什么要在消费端声明队列？因为消费端要从这个队列进行消费，如果启动消费端的时候生产者端一次也没有运行过，需要写下面这一行代码）
        channel.queueDeclare("work_queues",true, false, false, null);
        channel.basicQos(1);
        // 注册回调函数，开始消费
        channel.basicConsume("work_queues", false, consumer);
    }
}
```

### 测试
先启动两个消费者端，然后再启动生产者端。

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1763817465954-f140df76-5724-4ea8-9265-3dd915436dee.png" width="280" title="" crop="0,0,1,1" id="u78f5b26c" class="ne-image">

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1763817483560-05530e6a-dfad-45cf-90ff-ec6326cb6d7e.png" width="267.2" title="" crop="0,0,1,1" id="u32598a13" class="ne-image">

通过测试，可以看到，消费者确实是竞争的关系。

查看 web 管理界面，也可以看到所有消息已经全部消费了：

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1763817557160-4df2520a-938e-4285-a382-51a511013524.png" width="1160.8" title="" crop="0,0,1,1" id="u99efb5e4" class="ne-image">

## <font style="color:rgb(15, 17, 21);">Publish/Subscribe（发布与订阅模式）</font>
### 模式的理解
<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1763812763977-8b21dbf4-5a5b-4fa0-ac0c-54e3491d3d9f.png" width="331.2" title="" crop="0,0,1,1" id="u48fb8197" class="ne-image">

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1763813424160-d1688434-0dd2-4503-9edf-9e7ec0fbc727.png" width="587" title="" crop="0,0,1,1" id="u62d10bd2" class="ne-image">

+ <font style="color:rgb(15, 17, 21);">一个生产者，</font>**<font style="color:rgb(15, 17, 21);">多个队列</font>**<font style="color:rgb(15, 17, 21);">，多个消费者</font>
+ **<font style="color:rgb(15, 17, 21);">一条消息被所有消费者处理</font>**<font style="color:rgb(15, 17, 21);">（每个队列都收到消息的副本）</font>
+ <font style="color:rgb(15, 17, 21);">用于</font>**<font style="color:rgb(15, 17, 21);">广播，</font>**<font style="color:rgb(15, 17, 21);">让</font>*