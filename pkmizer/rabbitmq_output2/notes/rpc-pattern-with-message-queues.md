, 21);">RPC 模式</font>
<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1763812799030-a3ba00c8-1256-4d51-b4dc-900d55874864.png" width="333.6" title="" crop="0,0,1,1" id="uc75dbda8" class="ne-image">

**<font style="color:rgb(15, 17, 21);">通过消息队列实现远程过程调用，生产者发送请求消息并</font>****<font style="color:#DF2A3F;">同步等待</font>****<font style="color:rgb(15, 17, 21);">消费者返回响应结果。</font>**

<font style="color:rgb(15, 17, 21);">这是一种利用消息队列 </font>**<font style="color:rgb(15, 17, 21);">“笨拙地”实现同步调用</font>**<font style="color:rgb(15, 17, 21);"> 的方式，让发送请求的程序像调用本地函数一样，停下来等待远方的处理结果。</font>

<font style="color:rgb(15, 17, 21);">很少用：因为它本质上是在用一个为 </font>**<font style="color:rgb(15, 17, 21);">“异步通信”</font>**<font style="color:rgb(15, 17, 21);"> 设计的工具（消息队列）去实现 </font>**<font style="color:rgb(15, 17, 21);">“同步通信”</font>**<font style="color:rgb(15, 17, 21);"> 的功能，显得很别扭。现在我们有更专业、更高效的替代方案：</font>**<font style="color:rgb(15, 17, 21);">gRPC 、Dubbo、Spring Cloud OpenFeign 等。</font>**

**<font style="color:rgb(15, 17, 21);"></font>**

## <font style="color:rgb(15, 17, 21);">Publisher Confirms（发布者确认机制）</font>
**这个是可靠性机制，不是工作模式。**

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1763812807667-ece845ec-e010-4efd-