# GLUE模式运行

1. 简单来说，就是使用GLUE模式创建任务。
2. 在自己的项目中的方法不需要`@XxlJob`了。
3. 在调度中心，需要去这个任务的在线ide中编写java函数，去调用到自己项目中的方法。

---

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

重启服务器，让以上添加的代码生效。这一点岂不是和我们上面所描述的“不需要重启服务器”不一致了？这其实说的并不是一码事！！！！！服务器端的代码添加了/修改了，是一定要重启服务器的，不重新编译、发布，代码怎么可能生效呢。我们上面所说的“不需要重启服务器”指的是，在调度中心修改具体的任务的代码是不需要重启服务器的！！！

在`调度中心`中在线编写代码，动态添加任务，并且不需要重启服务器：

**新增任务：**

![1744729565767-7c98d568-9dd9-4af0-a1fc-ac91aa229fe9.png](../assets/1744729565767-7c98d568-9dd9-4af0-a1fc-ac91aa229fe9.png)

**运行模式选择：GLUE(Java)**

![1744729616572-eb356940-6e02-43cb-b76b-847afcaaab17.png](../assets/1744729616572-eb356940-6e02-43cb-b76b-847afcaaab17.png)

**使用GLUE IDE编写Java代码：**

![1744729639721-d173b91a-13aa-46e6-88c9-439897e4c680.png](../assets/1744729639721-d173b91a-13aa-46e6-88c9-439897e4c680.png)

编写代码，导入`Autowired`和`HelloService`

```java
package com.xxl.job.service.handler;

import com.xxl.job.core.context.XxlJobHelper;
import com.xxl.job.core.handler.IJobHandler;
import org.springframework.beans.factory.annotation.Autowired;
import com.example.demo.job.HelloService;

public class DemoGlueJobHandler extends IJobHandler {
  
    @Autowired
    private HelloService helloService;
    
    @Override
    public void execute() throws Exception {
        helloService.doSome();
    }
}
```

**保存/发布：**

![1744729785421-60542a97-b959-4c93-84f2-d172b717a7cc.png](../assets/1744729785421-60542a97-b959-4c93-84f2-d172b717a7cc.png)

**开启任务：**

![1744766838592-6f2f84d4-187d-4c3c-bb1e-fdd94ddb8ba8.png](../assets/1744766838592-6f2f84d4-187d-4c3c-bb1e-fdd94ddb8ba8.png)

![1744766810943-7dfaca57-4fe9-46ca-bc36-686175dfb1d2.png](../assets/1744766810943-7dfaca57-4fe9-46ca-bc36-686175dfb1d2.png)

再次修改代码，不需要停止任务，不需要重启服务器：

![1744766889696-f419ee24-383b-41c9-addc-56cf2ca70dd2.png](../assets/1744766889696-f419ee24-383b-41c9-addc-56cf2ca70dd2.png)

```java
package com.xxl.job.service.handler;

import com.xxl.job.core.context.XxlJobHelper;
import com.xxl.job.core.handler.IJobHandler;
import org.springframework.beans.factory.annotation.Autowired;
import com.example.demo.job.HelloService;

public class DemoGlueJobHandler extends IJobHandler {
  
    @Autowired
    private HelloService helloService;
    
    @Override
    public void execute() throws Exception {
        helloService.doOther();
    }
}
```

**保存/发布，查看控制台：**

![1744766974576-6bd9012b-9885-459c-9364-229ac4d166ec.png](../assets/1744766974576-6bd9012b-9885-459c-9364-229ac4d166ec.png)

通过以上的测试可以看出，当我们使用`XXL-JOB`的时候，任务修改不需要重启服务器。

