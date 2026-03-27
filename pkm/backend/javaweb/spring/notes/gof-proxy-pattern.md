# GoF之代理模式

---

## 对代理模式的理解

**生活场景1**：牛村的牛二看上了隔壁村小花，牛二不好意思直接找小花，于是牛二找来了媒婆王妈妈。这里面就有一个非常典型的代理模式。牛二不能和小花直接对接，只能找一个中间人。其中王妈妈是代理类，牛二是目标类。王妈妈代替牛二和小花先见个面。（现实生活中的婚介所）【在程序中，对象A和对象B无法直接交互时。】

**生活场景2**：你刚到北京，要租房子，可以自己找，也可以找链家帮你找。其中链家是代理类，你是目标类。你们两个都有共同的行为：找房子。不过链家除了满足你找房子，另外会收取一些费用的。(现实生活中的房产中介)【在程序中，功能需要增强时。】

**西游记场景**：八戒和高小姐的故事。八戒要强抢民女高翠兰。悟空得知此事之后怎么做的？悟空幻化成高小姐的模样。代替高小姐与八戒会面。其中八戒是客户端程序。悟空是代理类。高小姐是目标类。那天夜里，在八戒眼里，眼前的就是高小姐，对于八戒来说，他是不知道眼前的高小姐是悟空幻化的，在他内心里这就是高小姐。所以悟空代替高小姐和八戒亲了嘴儿。这是非常典型的代理模式实现的保护机制。****代理模式中有一个非常重要的特点：对于客户端程序来说，使用代理对象时就像在使用目标对象一样。******【在程序中，目标需要被保护时】**

**业务场景**：系统中有A、B、C三个模块，使用这些模块的前提是需要用户登录，也就是说在A模块中要编写判断登录的代码，B模块中也要编写，C模块中还要编写，这些判断登录的代码反复出现，显然代码没有得到复用，可以为A、B、C三个模块提供一个代理，在代理当中写一次登录判断即可。代理的逻辑是：请求来了之后，判断用户是否登录了，如果已经登录了，则执行对应的目标，如果没有登录则跳转到登录页面。【在程序中，目标不但受到保护，并且代码也得到了复用。】

代理模式是GoF23种设计模式之一。属于结构型设计模式。

代理模式的作用是：为其他对象提供一种代理以控制对这个对象的访问。在某些情况下，一个客户不想或者不能直接引用一个对象，此时可以通过一个称之为“代理”的第三者来实现间接引用。代理对象可以在客户端和目标对象之间起到中介的作用，并且可以通过代理对象去掉客户不应该看到的内容和服务或者添加客户需要的额外服务。 通过引入一个新的对象来实现对真实对象的操作或者将新的对象作为真实对象的一个替身，这种实现机制即为代理模式，通过引入代理对象来间接访问一个对象，这就是代理模式的模式动机。

代理模式中的角色：

+ 代理类（代理主题）
+ 目标类（真实主题）
+ 代理类和目标类的公共接口（抽象主题）：客户端在使用代理类时就像在使用目标类，不被客户端所察觉，所以代理类和目标类要有共同的行为，也就是实现共同的接口。

代理模式的类图：

![](https://cdn.nlark.com/yuque/0/2022/png/21376908/1665651817094-af9ecbad-24ae-4c11-9fa2-efe46653df25.png)

代理模式在代码实现上，包括两种形式：

+ 静态代理
+ 动态代理

---

## 静态代理

现在有这样一个接口和实现类：

```java
package com.jkweilai.mall.service;

/**
 * 订单接口
 */
public interface OrderService {
    /**
     * 生成订单
     */
    void generate();

    /**
     * 查看订单详情
     */
    void detail();

    /**
     * 修改订单
     */
    void modify();
}

```

```java
package com.jkweilai.mall.service.impl;

import com.jkweilai.mall.service.OrderService;

public class OrderServiceImpl implements OrderService {
    @Override
    public void generate() {
        try {
            Thread.sleep(1234);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
        System.out.println("订单已生成");
    }

    @Override
    public void detail() {
        try {
            Thread.sleep(2541);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
        System.out.println("订单信息如下：******");
    }

    @Override
    public void modify() {
        try {
            Thread.sleep(1010);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
        System.out.println("订单已修改");
    }
}

```

其中Thread.sleep()方法的调用是为了模拟操作耗时。

项目已上线，并且运行正常，只是客户反馈系统有一些地方运行较慢，要求项目组对系统进行优化。于是项目负责人就下达了这个需求。首先需要搞清楚是哪些业务方法耗时较长，于是让我们统计每个业务方法所耗费的时长。如果是你，你该怎么做呢？

第一种方案：直接修改Java源代码，在每个业务方法中添加统计逻辑，如下：

```java
package com.jkweilai.mall.service.impl;

import com.jkweilai.mall.service.OrderService;

public class OrderServiceImpl implements OrderService {
    @Override
    public void generate() {
        long begin = System.currentTimeMillis();
        try {
            Thread.sleep(1234);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
        System.out.println("订单已生成");
        long end = System.currentTimeMillis();
        System.out.println("耗费时长"+(end - begin)+"毫秒");
    }

    @Override
    public void detail() {
        long begin = System.currentTimeMillis();
        try {
            Thread.sleep(2541);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
        System.out.println("订单信息如下：******");
        long end = System.currentTimeMillis();
        System.out.println("耗费时长"+(end - begin)+"毫秒");
    }

    @Override
    public void modify() {
        long begin = System.currentTimeMillis();
        try {
            Thread.sleep(1010);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
        System.out.println("订单已修改");
        long end = System.currentTimeMillis();
        System.out.println("耗费时长"+(end - begin)+"毫秒");
    }
}
```

需求可以满足，但显然是违背了OCP开闭原则。这种方案不可取。

第二种方案：编写一个子类继承OrderServiceImpl，在子类中重写每个方法，代码如下：

```java
package com.jkweilai.mall.service.impl;

public class OrderServiceImplSub extends OrderServiceImpl{
    @Override
    public void generate() {
        long begin = System.currentTimeMillis();
        super.generate();
        long end = System.currentTimeMillis();
        System.out.println("耗时"+(end - begin)+"毫秒");
    }

    @Override
    public void detail() {
        long begin = System.currentTimeMillis();
        super.detail();
        long end = System.currentTimeMillis();
        System.out.println("耗时"+(end - begin)+"毫秒");
    }

    @Override
    public void modify() {
        long begin = System.currentTimeMillis();
        super.modify();
        long end = System.currentTimeMillis();
        System.out.println("耗时"+(end - begin)+"毫秒");
    }
}
```

这种方式可以解决，但是存在两个问题：

+ 第一个问题：假设系统中有100个这样的业务类，需要提供100个子类，并且之前写好的创建Service对象的代码，都要修改为创建子类对象。
+ 第二个问题：由于采用了继承的方式，导致代码之间的耦合度较高。

这种方案也不可取。

第三种方案：使用代理模式（这里采用静态代理）

可以为OrderService接口提供一个代理类。

```java
package com.jkweilai.mall.service;

public class OrderServiceProxy implements OrderService{ // 代理对象

    // 目标对象
    private OrderService orderService;

    // 通过构造方法将目标对象传递给代理对象
    public OrderServiceProxy(OrderService orderService) {
        this.orderService = orderService;
    }

    @Override
    public void generate() {
        long begin = System.currentTimeMillis();
        // 执行目标对象的目标方法
        orderService.generate();
        long end = System.currentTimeMillis();
        System.out.println("耗时"+(end - begin)+"毫秒");
    }

    @Override
    public void detail() {
        long begin = System.currentTimeMillis();
        // 执行目标对象的目标方法
        orderService.detail();
        long end = System.currentTimeMillis();
        System.out.println("耗时"+(end - begin)+"毫秒");
    }

    @Override
    public void modify() {
        long begin = System.currentTimeMillis();
        // 执行目标对象的目标方法
        orderService.modify();
        long end = System.currentTimeMillis();
        System.out.println("耗时"+(end - begin)+"毫秒");
    }
}

```

这种方式的优点：符合OCP开闭原则，同时采用的是关联关系，所以程序的耦合度较低。所以这种方案是被推荐的。

编写客户端程序：

```java
package com.jkweilai.mall;

import com.jkweilai.mall.service.OrderService;
import com.jkweilai.mall.service.OrderServiceProxy;
import com.jkweilai.mall.service.impl.OrderServiceImpl;

public class Client {
    public static void main(String[] args) {
        // 创建目标对象
        OrderService target = new OrderServiceImpl();
        // 创建代理对象
        OrderService proxy = new OrderServiceProxy(target);
        // 调用代理对象的代理方法
        proxy.generate();
        proxy.modify();
        proxy.detail();
    }
}

```

运行结果：

![](https://cdn.nlark.com/yuque/0/2025/png/21376908/1763899986560-1ffb9314-4127-4514-9e6e-b8427fc725b5.png)

以上就是代理模式中的静态代理，其中OrderService接口是代理类和目标类的共同接口。OrderServiceImpl是目标类。OrderServiceProxy是代理类。

大家思考一下：如果系统中业务接口很多，一个接口对应一个代理类，显然也是不合理的，会导致类爆炸。怎么解决这个问题？动态代理可以解决。因为在动态代理中可以在内存中动态的为我们生成代理类的字节码。代理类不需要我们写了。类爆炸解决了，而且代码只需要写一次，代码也会得到复用。

---

## 动态代理

在程序运行阶段，在内存中动态生成代理类，被称为动态代理，目的是为了减少代理类的数量。解决代码复用的问题。

在内存当中动态生成类的技术常见的包括：

+ JDK动态代理技术：只能代理接口。
+ CGLIB动态代理技术：CGLIB(Code Generation Library)是一个开源项目。是一个强大的，高性能，高质量的Code生成类库，它可以在运行期扩展Java类与实现Java接口。它既可以代理接口，又可以代理类，****底层是通过继承的方式实现的****。性能比JDK动态代理要好。****（底层有一个小而快的字节码处理框架ASM。）****
+ Javassist动态代理技术：Javassist是一个开源的分析、编辑和创建Java字节码的类库。是由东京工业大学的数学和计算机科学系的 Shigeru Chiba （千叶 滋）所创建的。它已加入了开放源代码JBoss 应用服务器项目，通过使用Javassist对字节码操作为JBoss实现动态"AOP"框架。

### JDK动态代理

我们还是使用静态代理中的例子：一个接口和一个实现类。

```java
package com.jkweilai.mall.service;

public interface OrderService {
    /**
     * 生成订单
     */
    void generate();

    /**
     * 查看订单详情
     */
    void detail();

    /**
     * 修改订单
     */
    void modify();
}

```

```java
package com.jkweilai.mall.service.impl;

import com.jkweilai.mall.service.OrderService;

public class OrderServiceImpl implements OrderService {
    @Override
    public void generate() {
        try {
            Thread.sleep(1234);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
        System.out.println("订单已生成");
    }

    @Override
    public void detail() {
        try {
            Thread.sleep(2541);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
        System.out.println("订单信息如下：******");
    }

    @Override
    public void modify() {
        try {
            Thread.sleep(1010);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
        System.out.println("订单已修改");
    }
}

```

我们在静态代理的时候，除了以上一个接口和一个实现类之外，是不是要写一个代理类UserServiceProxy呀！在动态代理中UserServiceProxy代理类是可以动态生成的。这个类不需要写。我们直接写客户端程序即可：

```java
package com.jkweilai.mall;

import com.jkweilai.mall.service.OrderService;
import com.jkweilai.mall.service.impl.OrderServiceImpl;

import java.lang.reflect.Proxy;

public class Client {
    public static void main(String[] args) {
        // 第一步：创建目标对象
        OrderService target = new OrderServiceImpl();
        // 第二步：创建代理对象
        OrderService orderServiceProxy = Proxy.newProxyInstance(target.getClass().getClassLoader(), target.getClass().getInterfaces(), 调用处理器对象);
        // 第三步：调用代理对象的代理方法
        orderServiceProxy.detail();
        orderServiceProxy.modify();
        orderServiceProxy.generate();
    }
}
```

以上第二步创建代理对象是需要大家理解的：

OrderService orderServiceProxy = Proxy.newProxyInstance(target.getClass().getClassLoader(), target.getClass().getInterfaces(), 调用处理器对象);

这行代码做了两件事：

+ 第一件事：在内存中生成了代理类的字节码
+ 第二件事：创建代理对象

Proxy类全名：java.lang.reflect.Proxy。这是JDK提供的一个类（所以称为JDK动态代理）。主要是通过这个类在内存中生成代理类的字节码。

其中newProxyInstance()方法有三个参数：

+ 第一个参数：类加载器。在内存中生成了字节码，要想执行这个字节码，也是需要先把这个字节码加载到内存当中的。所以要指定使用哪个类加载器加载。
+ 第二个参数：接口类型。代理类和目标类实现相同的接口，所以要通过这个参数告诉JDK动态代理生成的类要实现哪些接口。
+ 第三个参数：调用处理器。这是一个JDK动态代理规定的接口，接口全名：java.lang.reflect.InvocationHandler。显然这是一个回调接口，也就是说调用这个接口中方法的程序已经写好了，就差这个接口的实现类了。

所以接下来我们要写一下java.lang.reflect.InvocationHandler接口的实现类，并且实现接口中的方法，代码如下：

```java
package com.jkweilai.mall.service;

import java.lang.reflect.InvocationHandler;
import java.lang.reflect.Method;

public class TimerInvocationHandler implements InvocationHandler {
    @Override
    public Object invoke(Object proxy, Method method, Object[] args) throws Throwable {
        return null;
    }
}
```

InvocationHandler接口中有一个方法invoke，这个invoke方法上有三个参数：

+ 第一个参数：Object proxy。代理对象。设计这个参数只是为了后期的方便，如果想在invoke方法中使用代理对象的话，尽管通过这个参数来使用。
+ 第二个参数：Method method。目标方法。
+ 第三个参数：Object[] args。目标方法调用时要传的参数。

我们将来肯定是要调用“目标方法”的，但要调用目标方法的话，需要“目标对象”的存在，“目标对象”从哪儿来呢？我们可以给TimerInvocationHandler提供一个构造方法，可以通过这个构造方法传过来“目标对象”，代码如下：

```java
package com.jkweilai.mall.service;

import java.lang.reflect.InvocationHandler;
import java.lang.reflect.Method;

public class TimerInvocationHandler implements InvocationHandler {
    // 目标对象
    private Object target;

    // 通过构造方法来传目标对象
    public TimerInvocationHandler(Object target) {
        this.target = target;
    }

    @Override
    public Object invoke(Object proxy, Method method, Object[] args) throws Throwable {
        return null;
    }
}

```

有了目标对象我们就可以在invoke()方法中调用目标方法了。代码如下：

```java
package com.jkweilai.mall.service;

import java.lang.reflect.InvocationHandler;
import java.lang.reflect.Method;

public class TimerInvocationHandler implements InvocationHandler {
    // 目标对象
    private Object target;

    // 通过构造方法来传目标对象
    public TimerInvocationHandler(Object target) {
        this.target = target;
    }

    @Override
    public Object invoke(Object proxy, Method method, Object[] args) throws Throwable {
        // 目标执行之前增强。
        long begin = System.currentTimeMillis();
        // 调用目标对象的目标方法
        Object retValue = method.invoke(target, args);
        // 目标执行之后增强。
        long end = System.currentTimeMillis();
        System.out.println("耗时"+(end - begin)+"毫秒");
        // 一定要记得返回哦。
        return retValue;
    }
}

```

到此为止，调用处理器就完成了。接下来，应该继续完善Client程序：

```java
package com.jkweilai.mall;

import com.jkweilai.mall.service.OrderService;
import com.jkweilai.mall.service.TimerInvocationHandler;
import com.jkweilai.mall.service.impl.OrderServiceImpl;

import java.lang.reflect.Proxy;

public class Client {
    public static void main(String[] args) {
        // 创建目标对象
        OrderService target = new OrderServiceImpl();
        // 创建代理对象
        OrderService orderServiceProxy = (OrderService) Proxy.newProxyInstance(target.getClass().getClassLoader(),
                                                                                target.getClass().getInterfaces(),
                                                                                new TimerInvocationHandler(target));
        // 调用代理对象的代理方法
        orderServiceProxy.detail();
        orderServiceProxy.modify();
        orderServiceProxy.generate();
    }
}

```

大家可能会比较好奇：那个InvocationHandler接口中的invoke()方法没看见在哪里调用呀？

注意：当你调用代理对象的代理方法的时候，注册在InvocationHandler接口中的invoke()方法会被调用。也就是上面代码第24 25 26行，这三行代码中任意一行代码执行，注册在InvocationHandler接口中的invoke()方法都会被调用。

执行结果：

![](https://cdn.nlark.com/yuque/0/2025/png/21376908/1763900041906-2f1f20aa-9f0a-4a22-8fb8-8c92a5cb4063.png)

学到这里可能会感觉有点懵，折腾半天，到最后这不是还得写一个接口的实现类吗？没省劲儿呀？

你要这样想就错了!!!!

我们可以看到，不管你有多少个Service接口，多少个业务类，这个TimerInvocationHandler接口是不是只需要写一次就行了，代码是不是得到复用了！！！！

而且最重要的是，以后程序员只需要关注核心业务的编写了，像这种统计时间的代码根本不需要关注。因为这种统计时间的代码只需要在调用处理器中编写一次即可。

到这里，JDK动态代理的原理就结束了。

不过我们看以下这个代码确实有点繁琐，对于客户端来说，用起来不方便：

![](https://cdn.nlark.com/yuque/0/2022/png/21376908/1665716434406-4e092df4-b1a7-4d16-bbc1-1f134b8f51f7.png)

我们可以提供一个工具类：ProxyUtil，封装一个方法：

```java
package com.jkweilai.mall.util;

import com.jkweilai.mall.service.TimerInvocationHandler;

import java.lang.reflect.Proxy;

public class ProxyUtil {
    public static Object newProxyInstance(Object target) {
        return Proxy.newProxyInstance(target.getClass().getClassLoader(), 
                target.getClass().getInterfaces(), 
                new TimerInvocationHandler(target));
    }
}
```

这样客户端代码就不需要写那么繁琐了：

```java
package com.jkweilai.mall;

import com.jkweilai.mall.service.OrderService;
import com.jkweilai.mall.service.TimerInvocationHandler;
import com.jkweilai.mall.service.impl.OrderServiceImpl;
import com.jkweilai.mall.util.ProxyUtil;

import java.lang.reflect.Proxy;

public class Client {
    public static void main(String[] args) {
        // 创建目标对象
        OrderService target = new OrderServiceImpl();
        // 创建代理对象
        OrderService orderServiceProxy = (OrderService) ProxyUtil.newProxyInstance(target);
        // 调用代理对象的代理方法
        orderServiceProxy.detail();
        orderServiceProxy.modify();
        orderServiceProxy.generate();
    }
}

```

执行结果：

![](https://cdn.nlark.com/yuque/0/2025/png/21376908/1763900073143-1738ce13-7f3d-4452-92bb-1d89797c4637.png)

### CGLIB动态代理

CGLIB既可以代理接口，又可以代理类。底层采用继承的方式实现。所以被代理的目标类不能使用final修饰。

使用CGLIB，需要引入它的依赖：

```xml
<dependency>
  <groupId>cglib</groupId>
  <artifactId>cglib</artifactId>
  <version>3.3.0</version>
</dependency>
```

我们准备一个没有实现接口的类，如下：

```java
package com.jkweilai.mall.service;

public class UserService {

    public void login(){
        System.out.println("用户正在登录系统....");
    }

    public void logout(){
        System.out.println("用户正在退出系统....");
    }
}
```

使用CGLIB在内存中为UserService类生成代理类，并创建对象：

```java
package com.jkweilai.mall;

import com.jkweilai.mall.service.UserService;
import net.sf.cglib.proxy.Enhancer;

public class Client {
    public static void main(String[] args) {
        // 创建字节码增强器
        Enhancer enhancer = new Enhancer();
        
        // 告诉cglib要继承哪个类
        enhancer.setSuperclass(UserService.class);
        
        // 告诉cglib要代理哪个接口（如果要使用cglib进行接口的代码，这样写。）
        //enhancer.setInterfaces(UserServiceImpl.class.getInterfaces());
        
        // 设置回调接口
        enhancer.setCallback(方法拦截器对象);
        // 生成源码，编译class，加载到JVM，并创建代理对象
        UserService userServiceProxy = (UserService)enhancer.create();

        userServiceProxy.login();
        userServiceProxy.logout();

    }
}
```

和JDK动态代理原理差不多，在CGLIB中需要提供的不是InvocationHandler，而是：net.sf.cglib.proxy.MethodInterceptor

编写MethodInterceptor接口实现类：

```java
package com.jkweilai.mall.service;

import net.sf.cglib.proxy.MethodInterceptor;
import net.sf.cglib.proxy.MethodProxy;

import java.lang.reflect.Method;

public class TimerMethodInterceptor implements MethodInterceptor {
    @Override
    public Object intercept(Object proxy, Method method, Object[] objects, MethodProxy methodProxy) throws Throwable {
        return null;
    }
}
```

MethodInterceptor接口中有一个方法intercept()，该方法有4个参数：

**第一个参数**：代理对象

**第二个参数**：目标方法

**第三个参数**：目标方法调用时的实参

**第四个参数**：**用于调用目标方法或其超类方法的代理工具，性能更优。（******直接字节码调用，性能更高******：避免了反射开销）**

在MethodInterceptor的intercept()方法中调用目标以及添加增强：

```java
package com.jkweilai.mall.service;

import net.sf.cglib.proxy.MethodInterceptor;
import net.sf.cglib.proxy.MethodProxy;

import java.lang.reflect.Method;

public class TimerMethodInterceptor implements MethodInterceptor {
    @Override
    public Object intercept(Object proxy, Method method, Object[] objects, MethodProxy methodProxy) throws Throwable {
        // 前增强
        long begin = System.currentTimeMillis();
        
        // 调用目标（更高效的调用方式）
        Object retValue = methodProxy.invokeSuper(proxy, objects);
        
        // 如果不使用以上的方式调用，使用原始的反射机制调用，代码需要这样写。
        // Object retValue = method.invoke(从外部将目标对象传过来, objects);
        
        // 后增强
        long end = System.currentTimeMillis();
        System.out.println("耗时" + (end - begin) + "毫秒");
        
        // 一定要返回
        return retValue;
    }
}

```

回调已经写完了，可以修改客户端程序了：

```java
package com.jkweilai.mall;

import com.jkweilai.mall.service.TimerMethodInterceptor;
import com.jkweilai.mall.service.UserService;
import net.sf.cglib.proxy.Enhancer;

public class Client {
    public static void main(String[] args) {
        // 创建字节码增强器
        Enhancer enhancer = new Enhancer();
        // 告诉cglib要继承哪个类
        enhancer.setSuperclass(UserService.class);
        // 设置回调接口
        enhancer.setCallback(new TimerMethodInterceptor());
        // 生成源码，编译class，加载到JVM，并创建代理对象
        UserService userServiceProxy = (UserService)enhancer.create();

        userServiceProxy.login();
        userServiceProxy.logout();

    }
}
```

对于高版本的JDK，如果使用CGLIB，需要在启动项中添加两个启动参数：****（下图第一个红色框需要点击 Modify options来 Add vm options才能显示）****

![](https://cdn.nlark.com/yuque/0/2025/png/21376908/1764241276991-95dffe8b-56b2-49e6-85c3-4a0568d4016a.png)

+ `--add-opens java.base/java.lang=ALL-UNNAMED`
+ `--add-opens java.base/sun.net.util=ALL-UNNAMED`

**执行结果：**

![](https://cdn.nlark.com/yuque/0/2025/png/21376908/1763900217070-16caaae5-163f-49f4-97dc-74b9f02338cf.png)
