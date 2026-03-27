# GLUE模式运行

GLUE模式可以达到的效果是：采用在线编写代码的方式，在不需要重启服务器的前提下，动态添加/变更执行的任务。

在`执行器项目`中添加如下类和方法：

```java
@Service
public class HelloService {
    public void doSome(){
        System.out.println("do some!");
    }
    public void doOther(){
        System.out.println("do other!");
    }
}
```

**重启服务器，让以上添加的代码生效。这一点岂不是和我们上面所描述的“不需要重启服务器”不一致了？这其实说的并不是一码事！！！！！服务器端的代码添加了/修改了，是一定要重启服务器的，不重新编译、发布，代码怎么可能生效呢。我们上面所说的“不需要重启服务器”指的是，在调度中心修改具体的任务的代码是不需要重启服务器的！！！**

在`调度中心`中在线编写代码，动态添加任务，并且不需要重启服务器：

**新增任务：**

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1744729565767-7c98d568-9dd9-4af0-a1fc-ac91aa229fe9.png" width="1910" title="" crop="0,0,1,1" id="ubba6bd74" class="ne-image" style="font-size: 16px">

**运行模式选择：GLUE(Java)**

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1744729616572-eb356940-6e02-43cb-b76b-847afcaaab17.png" width="891" title="" crop="0,0,1,1" id="u961ba838" class="ne-image" style="font-size: 16px">

**使用GLUE IDE编写Java代码：**

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1744729639721-d173b91a-13aa-46e6-88c9-439897e4c680.png" width="192" title="" crop="0,0,1,1" id="u54f94a46" class="ne-image" style="font-size: 16px">

**编写代码，导入**`**Autowired**`**和**`**HelloService**`

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1744730138254-3582dbd3-7c14-4ced-a23c-ae8370168b26.png" width="531" title="" crop="0,0,1,1" id="ub6831f8e" class="ne-image" style="font-size: 16px">

**保存/发布：**

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1744729785421-60542a97-b959-4c93-84f2-d172b717a7cc.png" width="582" title="" crop="0,0,1,1" id="u1c776695" class="ne-image" style="font-size: 16px">

**开启任务：**

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1744766838592-6f2f84d4-187d-4c3c-bb1e-fdd94ddb8ba8.png" width="194" title="" crop="0,0,1,1" id="u18a89219" class="ne-image" style="font-size: 16px">

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1744766810943-7dfaca57-4fe9-46ca-bc36-686175dfb1d2.png" width="311" title="" crop="0,0,1,1" id="uc0575d62" class="ne-image" style="font-size: 16px">

再次修改代码，不需要停止任务，不需要重启服务器：

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1744766889696-f419ee24-383b-41c9-addc-56cf2ca70dd2.png" width="192" title="" crop="0,0,1,1" id="u0e2a6e20" class="ne-image" style="font-size: 16px">

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1744766927081-743d5813-d4b7-4422-a9f1-52f0e4c07cd5.png" width="520" title="" crop="0,0,1,1" id="uc12e3b1b" class="ne-image" style="font-size: 16px">

**保存/发布，查看控制台：**

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1744766974576-6bd9012b-9885-459c-9364-229ac4d166ec.png" width="261" title="" crop="0,0,1,1" id="ub2c644ca" class="ne-image" style="font-size: 16px">

通过以上的测试可以看出，当我们使用`XXL-JOB`的时候，任务修改不需要重启服务器。

