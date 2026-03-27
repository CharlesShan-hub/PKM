# 集群环境下任务不会重复执行

---

## 创建应用副本

创建应用副本是为了搭建一个集群的环境：

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1744767917646-1b82ac34-6ce3-40a1-a774-f63cd0fbd69b.png" width="295" title="" crop="0,0,1,1" id="udf8a5e9f" class="ne-image" style="font-size: 16px">

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1744768029242-be52bf95-ceb5-433e-9d3a-dd292c58c05e.png" width="300" title="" crop="0,0,1,1" id="u62e02d99" class="ne-image" style="font-size: 16px">

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1744768042052-96d3d584-2886-4b67-ab53-e6061b58f67f.png" width="285" title="" crop="0,0,1,1" id="u770a03fe" class="ne-image" style="font-size: 16px">

---

## 不同应用配置不同端口

配置第一个应用的服务器端口8088和执行器端口9998：

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1744768252306-db15d7f6-e0eb-464e-88dd-2f721c7a47a2.png" width="760" title="" crop="0,0,1,1" id="EILdM" class="ne-image" style="font-size: 16px">

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1744768319572-7ea1aa91-5439-44bb-b01c-ec3dd26f5084.png" width="633" title="" crop="0,0,1,1" id="lAmsf" class="ne-image" style="font-size: 16px">

`**-Dserver.port=8088 -Dxxl.job.executor.port=9998**`

配置第二个应用的服务器端口8089和执行器端口9999：

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1744768409646-fb923c0f-7c7a-40b8-9ef1-6f957f1e55f2.png" width="628" title="" crop="0,0,1,1" id="Qkclh" class="ne-image" style="font-size: 16px">

`**-Dserver.port=8089 -Dxxl.job.executor.port=9999**`

启动两个应用：

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1744768513115-e4fd700e-d4e0-474f-8c78-c5e4ee219ef9.png" width="684" title="" crop="0,0,1,1" id="uef073188" class="ne-image" style="font-size: 16px">

---

## 测试集群环境下是否会重复执行任务

在`调度中心`启动任务，查看这两个应用有没有重复执行任务。

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1744768620531-95959730-cdb1-4828-8393-58f4018b51e9.png" width="538" title="" crop="0,0,1,1" id="u84c22888" class="ne-image" style="font-size: 16px">

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1744768634657-6df7ae5c-7b80-4a9c-8597-3e67aec9f73e.png" width="613" title="" crop="0,0,1,1" id="u377b3026" class="ne-image" style="font-size: 16px">

可以看到，任务只在第一个应用中执行，并不会重复执行任务。

---

## 路由策略

**为什么只会在第一个应用中执行呢？**

这是由`路由策略`所决定的。如下图，在调度中心的任务编辑页面可以看到路由策略的选择，默认选择的是`第一个`:

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1744768739485-ab084ee7-091b-4ea4-a59f-3db8f5df428d.png" width="886" title="" crop="0,0,1,1" id="u69160d40" class="ne-image" style="font-size: 16px">

**所有的路由策略包括：**

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1744768767551-414eff64-15c4-40b4-bfac-b51a4529bd79.png" width="394" title="" crop="0,0,1,1" id="udc4f4f1d" class="ne-image" style="font-size: 16px">

**每个路由策略什么含义？**

1. 第一个：直接选任务列表里的第一个机器干活。  
2. 最后一个：直接选任务列表里的最后一个机器干活。  
3. 轮询：轮流让每台机器干活，大家排队，一人一次。  
4. 随机：随便抽一台机器干活，全凭运气。  
5. 一致性HASH：同样的任务永远找同一台机器干，避免换来换去。  
6. 最不经常使用：挑平时干活最少的机器去干，雨露均沾。  
7. 最近最久未使用：挑最闲的机器（好久没干活的）去干。  
8. 故障转移：如果一台机器挂了，自动换另一台好的继续干。  
9. 忙碌转移：如果一台机器正忙着，就找其他闲着的机器干。  
10. 分片广播：让所有机器一起干同一个活，各自分一小块任务。

尝试将路由策略修改为轮询，看看是否两个应用交替执行任务：

停止任务：

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1744769080198-25a8f8bf-46df-4efd-8daa-6576e8f2a7ab.png" width="173" title="" crop="0,0,1,1" id="u258812e4" class="ne-image" style="font-size: 16px">

编辑任务：

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1744769094127-8cdab30c-ea4f-4ba3-a0fd-ada8f00d28ae.png" width="185" title="" crop="0,0,1,1" id="u36c08441" class="ne-image" style="font-size: 16px">

路由策略选择轮询：

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1744769106866-f4719771-25a1-42ed-a511-7b8bb22732fd.png" width="388" title="" crop="0,0,1,1" id="u0ae54bde" class="ne-image" style="font-size: 16px">

启动任务：

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1744769120771-a485ce76-41c3-4ab0-b62f-039d9745c049.png" width="181" title="" crop="0,0,1,1" id="u83783891" class="ne-image" style="font-size: 16px">

查看控制台：

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1744769221653-e1cef3d8-5e85-4241-a44f-766233f5fe60.png" width="621" title="" crop="0,0,1,1" id="u52ebb776" class="ne-image" style="font-size: 16px">

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1744769233742-9fc95a07-88a9-4473-a22e-f3b2a1d7fafe.png" width="644" title="" crop="0,0,1,1" id="ufa7aa6c5" class="ne-image" style="font-size: 16px">

可以看到，确实采用轮询的方式交替执行任务。

