# 面向切面编程AOP

IoC使软件组件松耦合。AOP让你能够捕捉系统中经常使用的功能，把它转化成组件。

AOP（Aspect Oriented Programming）：面向切面编程，面向方面编程。（AOP是一种编程技术）

AOP是对OOP的补充延伸。

AOP底层使用的就是动态代理来实现的。

Spring的AOP使用的动态代理是：JDK动态代理 + CGLIB动态代理技术。Spring在这两种动态代理中灵活切换，如果是代理接口，会默认使用JDK动态代理，如果要代理某个类，这个类没有实现接口，就会切换使用CGLIB。当然，你也可以强制通过一些配置让Spring只使用CGLIB。

---

## AOP介绍

一般一个系统当中都会有一些系统服务，例如：日志、事务管理、安全等。这些系统服务被称为：****交叉业务****

这些****交叉业务****几乎是通用的，不管你是做银行账户转账，还是删除用户数据。日志、事务管理、安全，这些都是需要做的。

如果在每一个业务处理过程当中，都掺杂这些交叉业务代码进去的话，存在两方面问题：

+ 第一：交叉业务代码在多个业务流程中反复出现，显然这个交叉业务代码没有得到复用。并且修改这些交叉业务代码的话，需要修改多处。
+ 第二：程序员无法专注核心业务代码的编写，在编写核心业务代码的同时还需要处理这些交叉业务。

使用AOP可以很轻松的解决以上问题。

请看下图，可以帮助你快速理解AOP的思想：

![](https://cdn.nlark.com/yuque/0/2022/png/21376908/1665732609757-d8ae52ba-915e-49cf-9ef4-c7bcada0d601.png)

****用一句话总结AOP：将与核心业务无关的代码独立的抽取出来，形成一个独立的组件，然后以横向交叉的方式应用到业务流程当中的过程被称为AOP。****

****AOP的优点：****

+ ****第一：代码复用性增强。****
+ ****第二：代码易维护。****
+ ****第三：使开发者更关注业务逻辑。****

****

---

## AOP的七大术语

```java
public class UserService{
    public void do1(){
        System.out.println("do 1");
    }
    public void do2(){
        System.out.println("do 2");
    }
    public void do3(){
        System.out.println("do 3");
    }
    public void do4(){
        System.out.println("do 4");
    }
    public void do5(){
        System.out.println("do 5");
    }
    // 核心业务方法
    public void service(){
        do1();
        do2();
        do3();
        do5();
    }
}
```

+ ****连接点 Joinpoint******：程序执行过程中可以插入切面的具体位置（如方法执行前、方法正常返回后、方法抛出异常时、方法最终结束时等）**
+ ****切点 Pointcut******：******切点本质上就是一个"位置表达式"******，用来精确指定在哪些连接点织入切面**
+ ****通知 Advice******：在切点处执行的增强逻辑代码**
+ ****切面 Aspect******：切点 + 通知**
+ ****织入 Weaving******：将切面应用到目标对象的过程**
+ ****代理对象 Proxy******：被增强后产生的对象**
+ ****目标对象 Target******：原始的需要被增强的对象**

---

## 切点表达式

切点表达式用来定义通知（Advice）往哪些方法上切入。

切入点表达式语法格式：

```plain
execution([访问控制权限修饰符] 返回值类型 [全限定类名]方法名(形式参数列表) [异常])
```

**访问控制权限修饰符：**

+ 可选项。
+ **没写时会匹配******所有访问权限******的方法**。
+ 写public就表示只包括公开的方法。

**返回值类型：**

+ 必填项。
+ `*` 表示返回值类型任意。

**全限定类名：**

+ 可选项。
+ **在类路径中，**`**..**`**表示******当前包及其所有子包****
+ 省略时表示所有的类。

**方法名：**

+ 必填项。
+ `*` 表示所有方法。
+ `set*` 表示所有的set方法。

**形式参数列表：**

+ 必填项
+ `**()**`**- 无参数方法**
+ `**(..)**`**- 任意参数（0个或多个）**
+ `**(*)**`**- 恰好一个参数，类型任意**
+ `**(String)**`**- 恰好一个String类型参数**
+ `**(String, *)**`**- 恰好两个参数，第一个是String，第二个任意**
+ `**(*, String)**`**- 恰好两个参数，第二个是String，第一个任意**

**异常：**

+ 可选项。
+ 省略时表示任意异常类型。

**理解以下的切点表达式：**

```java
execution(public * com.jkweilai.mall.service.*.delete*(..))
```

+ `****public****`**：只匹配public方法**
+ `*********`**：返回值类型任意**
+ `****com.jkweilai.mall.service.*****`**：**`**com.jkweilai.mall.service**`**包下的******直接子类******（不包含子包）**
+ `****delete*****`**：方法名以**`**delete**`**开头**
+ `****(..)****`**：参数任意（0个或多个）**

```java
execution(* com.jkweilai.mall..*(..))
```

+ `*********`**：返回值类型任意**
+ `****com.jkweilai.mall..*****`**：**`**com.jkweilai.mall**`**包及其******所有子包******下的所有类**
+ `*********`**：所有方法**
+ `****(..)****`**：参数任意（0个或多个）**

```java
execution(* *(..))
```

+ `*********`**：返回值类型任意**
+ `****`**：所有类**
+ `*********`**：所有方法**
+ `****(..)****`**：参数任意（0个或多个）**

---

## 使用Spring的AOP

Spring对AOP的实现包括以下3种方式：

+ ****第一种方式：Spring框架结合AspectJ框架实现的AOP，基于注解方式。（只需要掌握这种）****
+ 第二种方式：Spring框架结合AspectJ框架实现的AOP，基于XML方式。
+ 第三种方式：Spring框架自己实现的AOP，基于XML配置方式。

实际开发中，都是Spring+AspectJ来实现AOP。所以我们重点学习第一种和第二种方式。

什么是AspectJ？（Eclipse组织的一个支持AOP的框架。AspectJ框架是独立于Spring框架之外的一个框架，Spring框架用了AspectJ） 

AspectJ项目起源于帕洛阿尔托（Palo Alto）研究中心（缩写为PARC）。该中心由Xerox集团资助，Gregor Kiczales领导，从1997年开始致力于AspectJ的开发，1998年第一次发布给外部用户，2001年发布1.0 release。为了推动AspectJ技术和社团的发展，PARC在2003年3月正式将AspectJ项目移交给了Eclipse组织，因为AspectJ的发展和受关注程度大大超出了PARC的预期，他们已经无力继续维持它的发展。

### 准备工作

使用Spring+AspectJ的AOP需要引入的依赖如下：

```xml
<dependency>
    <groupId>org.springframework</groupId>
    <artifactId>spring-context</artifactId>
    <version>6.2.13</version>
</dependency>
<!--spring aspects-->
<dependency>
    <groupId>org.springframework</groupId>
    <artifactId>spring-aspects</artifactId>
    <version>6.2.13</version>
</dependency>
```

Spring配置文件中添加context命名空间和aop命名空间

```xml
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
       xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
       xmlns:context="http://www.springframework.org/schema/context"
       xmlns:aop="http://www.springframework.org/schema/aop"
       xsi:schemaLocation="http://www.springframework.org/schema/beans http://www.springframework.org/schema/beans/spring-beans.xsd
                           http://www.springframework.org/schema/context http://www.springframework.org/schema/context/spring-context.xsd
                           http://www.springframework.org/schema/aop http://www.springframework.org/schema/aop/spring-aop.xsd">

</beans>
```

### 基于AspectJ的AOP注解式开发

**第一步：**定义目标类以及目标方法

```java
package com.jkweilai.spring.service;

// 目标类
public class OrderService {
    // 目标方法
    public void generate(){
        System.out.println("订单已生成！");
    }
}
```

**第二步：**定义切面类

```java
package com.jkweilai.spring.service;

import org.aspectj.lang.annotation.Aspect;

// 切面类
@Aspect
public class MyAspect {
}
```

**第三步：**目标类和切面类都纳入spring bean管理

在目标类OrderService上添加****@Component****注解。

在切面类MyAspect类上添加****@Component****注解。

**第四步：**在spring配置文件中添加组建扫描

```xml
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
       xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
       xmlns:context="http://www.springframework.org/schema/context"
       xmlns:aop="http://www.springframework.org/schema/aop"
       xsi:schemaLocation="http://www.springframework.org/schema/beans http://www.springframework.org/schema/beans/spring-beans.xsd
                           http://www.springframework.org/schema/context http://www.springframework.org/schema/context/spring-context.xsd
                           http://www.springframework.org/schema/aop http://www.springframework.org/schema/aop/spring-aop.xsd">
    <!--开启组件扫描-->
    <context:component-scan base-package="com.jkweilai.spring.service"/>
</beans>
```

**第五步：**在切面类中添加通知

```java
package com.jkweilai.spring.service;

import org.springframework.stereotype.Component;
import org.aspectj.lang.annotation.Aspect;

// 切面类
@Aspect
@Component
public class MyAspect {
    // 这就是需要增强的代码（通知）
    public void advice(){
        System.out.println("我是一个通知");
    }
}

```

**第六步：**在通知上添加切点表达式

```java
package com.jkweilai.spring.service;

import org.aspectj.lang.annotation.Before;
import org.springframework.stereotype.Component;
import org.aspectj.lang.annotation.Aspect;

// 切面类
@Aspect
@Component
public class MyAspect {
    
    // 切点表达式
    @Before("execution(* com.jkweilai.spring.service.OrderService.*(..))")
    // 这就是需要增强的代码（通知）
    public void advice(){
        System.out.println("我是一个通知");
    }
}
```

****注解@Before表示前置通知。****

**第七步：**在spring配置文件中启用自动代理

```xml
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
       xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
       xmlns:context="http://www.springframework.org/schema/context"
       xmlns:aop="http://www.springframework.org/schema/aop"
       xsi:schemaLocation="http://www.springframework.org/schema/beans http://www.springframework.org/schema/beans/spring-beans.xsd
                           http://www.springframework.org/schema/context http://www.springframework.org/schema/context/spring-context.xsd
                           http://www.springframework.org/schema/aop http://www.springframework.org/schema/aop/spring-aop.xsd">
    <!--开启组件扫描-->
    <context:component-scan base-package="com.jkweilai.spring.service"/>
    <!--开启自动代理-->
    <aop:aspectj-autoproxy proxy-target-class="true"/>
</beans>
```

`****<aop:aspectj-autoproxy proxy-target-class="true"/>****`****开启自动代理之后，凡事带有@Aspect注解的bean都会生成代理对象。****

`****proxy-target-class="true"****`****表示采用cglib动态代理。****

`****proxy-target-class="false"****`****表示采用jdk动态代理。默认值是false。即使写成false，当没有接口的时候，也会自动选择cglib生成代理类。****

测试程序：

```java
package com.jkweilai.spring.test;

import com.jkweilai.spring.service.OrderService;
import org.junit.Test;
import org.springframework.context.ApplicationContext;
import org.springframework.context.support.ClassPathXmlApplicationContext;

public class AOPTest {
    @Test
    public void testAOP(){
        ApplicationContext applicationContext = new ClassPathXmlApplicationContext("spring-aspectj-aop-annotation.xml");
        OrderService orderService = applicationContext.getBean("orderService", OrderService.class);
        orderService.generate();
    }
}

```

运行结果：

![](https://cdn.nlark.com/yuque/0/2022/png/21376908/1665843923087-e1116f09-2470-46cb-b21a-1526f62cab50.png)

### 全注解式开发AOP

就是编写一个类，在这个类上面使用大量注解来代替spring的配置文件，spring配置文件消失了，如下：

```java
package com.jkweilai.spring.service;

import org.springframework.context.annotation.ComponentScan;
import org.springframework.context.annotation.Configuration;
import org.springframework.context.annotation.EnableAspectJAutoProxy;

@Configuration
@ComponentScan("com.jkweilai.spring.service")
@EnableAspectJAutoProxy(proxyTargetClass = true)
public class SpringConfiguration {
}
```

测试程序也变化了：

```java
@Test
public void testAOPWithAllAnnotation(){
    ApplicationContext applicationContext = new AnnotationConfigApplicationContext(SpringConfiguration.class);
    OrderService orderService = applicationContext.getBean("orderService", OrderService.class);
    orderService.generate();
}
```

### 通知类型

通知类型包括：

+ ****前置通知：@Before******目标方法执行之前的通知**
+ ****后置通知：@After******目标方法不管是否成功结束，后置通知都会执行（即时有未捕获的异常）**
+ ****返回通知：@AfterReturning******目标方法成功执行返回后执行的通知（目标方法出现未捕获的异常时，不会执行）**
+ ****异常通知：@AfterThrowing******目标方法发生异常后执行的通知**
+ ****环绕通知：@Around******目标方法执行之前和之后都可添加通知，******可以控制目标方法是否执行****

**执行顺序：**

+ ****正常执行：******@Around前半 → @Before → 目标方法 → @AfterReturning → @After → @Around后半**
+ ****异常执行：******@Around前半 → @Before → 目标方法 → @AfterThrowing → @After → @Around后半**
+ ****注意：******目标方法出现异常，并且最终异常没有捕获的话，@Around后半  不会执行。**

接下来，编写程序来测试这几个通知的执行顺序：

```java
package com.jkweilai.spring.service;

import org.aspectj.lang.ProceedingJoinPoint;
import org.aspectj.lang.annotation.*;
import org.springframework.stereotype.Component;

// 切面类
@Component
@Aspect
public class MyAspect {

    @Around("execution(* com.jkweilai.spring.service.OrderService.*(..))")
    public Object aroundAdvice(ProceedingJoinPoint proceedingJoinPoint) throws Throwable {
        System.out.println("环绕通知开始");
        // 执行目标方法。
        Object retValue = proceedingJoinPoint.proceed();
        System.out.println("环绕通知结束");
        return retValue;
    }

    @Before("execution(* com.jkweilai.spring.service.OrderService.*(..))")
    public void beforeAdvice(){
        System.out.println("前置通知");
    }

    @AfterReturning("execution(* com.jkweilai.spring.service.OrderService.*(..))")
    public void afterReturningAdvice(){
        System.out.println("返回通知");
    }

    @AfterThrowing("execution(* com.jkweilai.spring.service.OrderService.*(..))")
    public void afterThrowingAdvice(){
        System.out.println("异常通知");
    }

    @After("execution(* com.jkweilai.spring.service.OrderService.*(..))")
    public void afterAdvice(){
        System.out.println("后置通知");
    }

}
```

```java
package com.jkweilai.spring.service;

import org.springframework.stereotype.Component;

// 目标类
@Component
public class OrderService {
    // 目标方法
    public void generate(){
        System.out.println("订单已生成！");
    }
}

```

```java
package com.jkweilai.spring.test;

import com.jkweilai.spring.service.OrderService;
import org.junit.Test;
import org.springframework.context.ApplicationContext;
import org.springframework.context.support.ClassPathXmlApplicationContext;

public class AOPTest {
    @Test
    public void testAOP(){
        ApplicationContext applicationContext = new ClassPathXmlApplicationContext("spring-aspectj-aop-annotation.xml");
        OrderService orderService = applicationContext.getBean("orderService", OrderService.class);
        orderService.generate();
    }
}
```

执行结果：

![](https://cdn.nlark.com/yuque/0/2024/png/21376908/1727354763970-e62d8306-982e-4d23-881d-802a4213f2d3.png)

通过上面的执行结果就可以判断他们的执行顺序了，这里不再赘述。

结果中没有异常通知，这是因为目标程序执行过程中没有发生异常。我们尝试让目标方法发生异常：

```java
package com.jkweilai.spring.service;

import org.springframework.stereotype.Component;

// 目标类
@Component
public class OrderService {
    // 目标方法
    public void generate(){
        System.out.println("订单已生成！");
        if (1 == 1) {
            throw new RuntimeException("模拟异常发生");
        }
    }
}
```

再次执行测试程序，结果如下：

![](https://cdn.nlark.com/yuque/0/2024/png/21376908/1727354892988-43f912b5-9d3d-4ae4-b5ee-640a69d7359c.png)

通过测试得知，当发生异常之后，后置通知也会执行。

出现异常之后，如果**未捕获该异常**，****返回通知****和****环绕通知的结束部分****不会执行。

出现异常之后，如果**捕获了该异常**，****返回通知****不会执行，但****环绕通知的结束部分****会执行。（可以自行测试一下）

### 切面的先后顺序

我们知道，业务流程当中不一定只有一个切面，可能有的切面控制事务，有的记录日志，有的进行安全控制，如果多个切面的话，顺序如何控制：****可以使用@Order注解来标识切面类，为@Order注解的value指定一个整数型的数字，数字越小，优先级越高****。

再定义一个切面类，如下：

```java
package com.jkweilai.spring.service;

import org.aspectj.lang.ProceedingJoinPoint;
import org.aspectj.lang.annotation.*;
import org.springframework.core.annotation.Order;
import org.springframework.stereotype.Component;

@Aspect
@Component
@Order(1) //设置优先级
public class YourAspect {

    @Around("execution(* com.jkweilai.spring.service.OrderService.*(..))")
    public Object aroundAdvice(ProceedingJoinPoint proceedingJoinPoint) throws Throwable {
        System.out.println("YourAspect环绕通知开始");
        // 执行目标方法。
        Object retValue = proceedingJoinPoint.proceed();
        System.out.println("YourAspect环绕通知结束");
        return retValue;
    }

    @Before("execution(* com.jkweilai.spring.service.OrderService.*(..))")
    public void beforeAdvice(){
        System.out.println("YourAspect前置通知");
    }

    @AfterReturning("execution(* com.jkweilai.spring.service.OrderService.*(..))")
    public void afterReturningAdvice(){
        System.out.println("YourAspect返回通知");
    }

    @AfterThrowing("execution(* com.jkweilai.spring.service.OrderService.*(..))")
    public void afterThrowingAdvice(){
        System.out.println("YourAspect异常通知");
    }

    @After("execution(* com.jkweilai.spring.service.OrderService.*(..))")
    public void afterAdvice(){
        System.out.println("YourAspect后置通知");
    }
}

```

```java
package com.jkweilai.spring.service;

import org.aspectj.lang.ProceedingJoinPoint;
import org.aspectj.lang.annotation.*;
import org.springframework.core.annotation.Order;
import org.springframework.stereotype.Component;

// 切面类
@Component
@Aspect
@Order(2) //设置优先级
public class MyAspect {

    @Around("execution(* com.jkweilai.spring.service.OrderService.*(..))")
    public Object aroundAdvice(ProceedingJoinPoint proceedingJoinPoint) throws Throwable {
        System.out.println("环绕通知开始");
        // 执行目标方法。
        Object retValue = proceedingJoinPoint.proceed();
        System.out.println("环绕通知结束");
        return retValue;
    }

    @Before("execution(* com.jkweilai.spring.service.OrderService.*(..))")
    public void beforeAdvice(){
        System.out.println("前置通知");
    }

    @AfterReturning("execution(* com.jkweilai.spring.service.OrderService.*(..))")
    public void afterReturningAdvice(){
        System.out.println("返回通知");
    }

    @AfterThrowing("execution(* com.jkweilai.spring.service.OrderService.*(..))")
    public void afterThrowingAdvice(){
        System.out.println("异常通知");
    }

    @After("execution(* com.jkweilai.spring.service.OrderService.*(..))")
    public void afterAdvice(){
        System.out.println("后置通知");
    }

}
```

执行测试程序：

![](https://cdn.nlark.com/yuque/0/2024/png/21376908/1727355165649-0a4443b6-5ac5-4f38-a23f-756af6585dbc.png)

通过修改@Order注解的整数值来切换顺序，执行测试程序：

![](https://cdn.nlark.com/yuque/0/2024/png/21376908/1727355225994-ecb4fbe1-2611-477b-a319-d64a5a897153.png)

### 优化使用切点表达式

观看以下代码中的切点表达式：

```java
package com.jkweilai.spring.service;

import org.aspectj.lang.ProceedingJoinPoint;
import org.aspectj.lang.annotation.*;
import org.springframework.core.annotation.Order;
import org.springframework.stereotype.Component;

// 切面类
@Component
@Aspect
@Order(2)
public class MyAspect {

    @Around("execution(* com.jkweilai.spring.service.OrderService.*(..))")
    public Object aroundAdvice(ProceedingJoinPoint proceedingJoinPoint) throws Throwable {
        System.out.println("环绕通知开始");
        // 执行目标方法。
        Object retValue = proceedingJoinPoint.proceed();
        System.out.println("环绕通知结束");
        return retValue;
    }

    @Before("execution(* com.jkweilai.spring.service.OrderService.*(..))")
    public void beforeAdvice(){
        System.out.println("前置通知");
    }

    @AfterReturning("execution(* com.jkweilai.spring.service.OrderService.*(..))")
    public void afterReturningAdvice(){
        System.out.println("返回通知");
    }

    @AfterThrowing("execution(* com.jkweilai.spring.service.OrderService.*(..))")
    public void afterThrowingAdvice(){
        System.out.println("异常通知");
    }

    @After("execution(* com.jkweilai.spring.service.OrderService.*(..))")
    public void afterAdvice(){
        System.out.println("后置通知");
    }

}

```

缺点是：

+ 第一：切点表达式重复写了多次，没有得到复用。
+ 第二：如果要修改切点表达式，需要修改多处，难维护。

可以这样做：将切点表达式单独的定义出来，在需要的位置引入即可。如下：

```java
package com.jkweilai.spring.service;

import org.aspectj.lang.ProceedingJoinPoint;
import org.aspectj.lang.annotation.*;
import org.springframework.core.annotation.Order;
import org.springframework.stereotype.Component;

// 切面类
@Component
@Aspect
@Order(2)
public class MyAspect {
    
    @Pointcut("execution(* com.jkweilai.spring.service.OrderService.*(..))")
    public void pointcut(){}

    @Around("pointcut()")
    public Object aroundAdvice(ProceedingJoinPoint proceedingJoinPoint) throws Throwable {
        System.out.println("环绕通知开始");
        // 执行目标方法。
        Object retValue = proceedingJoinPoint.proceed();
        System.out.println("环绕通知结束");
        return retValue;
    }

    @Before("pointcut()")
    public void beforeAdvice(){
        System.out.println("前置通知");
    }

    @AfterReturning("pointcut()")
    public void afterReturningAdvice(){
        System.out.println("返回通知");
    }

    @AfterThrowing("pointcut()")
    public void afterThrowingAdvice(){
        System.out.println("异常通知");
    }

    @After("pointcut()")
    public void afterAdvice(){
        System.out.println("后置通知");
    }

}

```

使用@Pointcut注解来定义独立的切点表达式。

注意这个@Pointcut注解标注的方法随意，只是起到一个能够让@Pointcut注解编写的位置。

---

## AOP的实际案例：事务处理

项目中的事务控制是在所难免的。在一个业务流程当中，可能需要多条DML语句共同完成，为了保证数据的安全，这多条DML语句要么同时成功，要么同时失败。这就需要添加事务控制的代码。例如以下伪代码：

```java
class 业务类1{
    public void 业务方法1(){
        try{
            // 开启事务
            startTransaction();
            
            // 执行核心业务逻辑
            step1();
            step2();
            step3();
            ....
            
            // 提交事务
            commitTransaction();
        }catch(Exception e){
            // 回滚事务
            rollbackTransaction();
        }
    }
    public void 业务方法2(){
        try{
            // 开启事务
            startTransaction();
            
            // 执行核心业务逻辑
            step1();
            step2();
            step3();
            ....
            
            // 提交事务
            commitTransaction();
        }catch(Exception e){
            // 回滚事务
            rollbackTransaction();
        }
    }
    public void 业务方法3(){
        try{
            // 开启事务
            startTransaction();
            
            // 执行核心业务逻辑
            step1();
            step2();
            step3();
            ....
            
            // 提交事务
            commitTransaction();
        }catch(Exception e){
            // 回滚事务
            rollbackTransaction();
        }
    }
}

class 业务类2{
    public void 业务方法1(){
        try{
            // 开启事务
            startTransaction();
            
            // 执行核心业务逻辑
            step1();
            step2();
            step3();
            ....
            
            // 提交事务
            commitTransaction();
        }catch(Exception e){
            // 回滚事务
            rollbackTransaction();
        }
    }
    public void 业务方法2(){
        try{
            // 开启事务
            startTransaction();
            
            // 执行核心业务逻辑
            step1();
            step2();
            step3();
            ....
            
            // 提交事务
            commitTransaction();
        }catch(Exception e){
            // 回滚事务
            rollbackTransaction();
        }
    }
    public void 业务方法3(){
        try{
            // 开启事务
            startTransaction();
            
            // 执行核心业务逻辑
            step1();
            step2();
            step3();
            ....
            
            // 提交事务
            commitTransaction();
        }catch(Exception e){
            // 回滚事务
            rollbackTransaction();
        }
    }
}
//......
```

可以看到，这些业务类中的每一个业务方法都是需要控制事务的，而控制事务的代码又是固定的格式，都是：

```java
try{
    // 开启事务
    startTransaction();

    // 执行核心业务逻辑
    //......

    // 提交事务
    commitTransaction();
}catch(Exception e){
    // 回滚事务
    rollbackTransaction();
}
```

这个控制事务的代码就是和业务逻辑没有关系的“****交叉业务****”。以上伪代码当中可以看到这些交叉业务的代码没有得到复用，并且如果这些交叉业务代码需要修改，那必然需要修改多处，难维护，怎么解决？可以采用AOP思想解决。可以把以上控制事务的代码作为环绕通知，切入到目标类的方法当中。接下来我们做一下这件事，有两个业务类，如下：

```java
package com.jkweilai.spring.biz;

import org.springframework.stereotype.Component;

@Component
// 业务类
public class AccountService {
    // 转账业务方法
    public void transfer(){
        System.out.println("正在进行银行账户转账");
    }
    // 取款业务方法
    public void withdraw(){
        System.out.println("正在进行取款操作");
    }
}

```

```java
package com.jkweilai.spring.biz;

import org.springframework.stereotype.Component;

@Component
// 业务类
public class OrderService {
    // 生成订单
    public void generate(){
        System.out.println("正在生成订单");
    }
    // 取消订单
    public void cancel(){
        System.out.println("正在取消订单");
    }
}
```

注意，以上两个业务类已经纳入spring bean的管理，因为都添加了@Component注解。

接下来我们给以上两个业务类的4个方法添加事务控制代码，使用AOP来完成：

```java
package com.jkweilai.spring.biz;

import org.aspectj.lang.ProceedingJoinPoint;
import org.aspectj.lang.annotation.Around;
import org.aspectj.lang.annotation.Aspect;
import org.springframework.stereotype.Component;

@Aspect
@Component
// 事务切面类
public class TransactionAspect {
    
    @Around("execution(* com.jkweilai.spring.biz..*(..))")
    public Object aroundAdvice(ProceedingJoinPoint proceedingJoinPoint){
        Object retValue = null;
        try {
            System.out.println("开启事务");
            // 执行目标
            retValue = proceedingJoinPoint.proceed();
            System.out.println("提交事务");
        } catch (Throwable e) {
            System.out.println("回滚事务");
        }
        return retValue;
    }
}

```

你看，这个事务控制代码是不是只需要写一次就行了，并且修改起来也没有成本。编写测试程序：

```java
package com.jkweilai.spring.test;

import com.jkweilai.spring.biz.AccountService;
import com.jkweilai.spring.biz.OrderService;
import com.jkweilai.spring.service.SpringConfiguration;
import org.junit.Test;
import org.springframework.context.ApplicationContext;
import org.springframework.context.annotation.AnnotationConfigApplicationContext;

public class AOPTest2 {
    @Test
    public void testTransaction(){
        ApplicationContext applicationContext = new AnnotationConfigApplicationContext(SpringConfiguration.class);
        OrderService orderService = applicationContext.getBean("orderService", OrderService.class);
        AccountService accountService = applicationContext.getBean("accountService", AccountService.class);
        // 生成订单
        orderService.generate();
        // 取消订单
        orderService.cancel();
        // 转账
        accountService.transfer();
        // 取款
        accountService.withdraw();
    }
}
```

执行结果：

![](https://cdn.nlark.com/yuque/0/2025/png/21376908/1763900978755-59d9c5ec-850c-40b3-8d90-98163a7d2429.png)

通过测试可以看到，所有的业务方法都添加了事务控制的代码。

---

## AOP的实际案例：安全日志

需求是这样的：项目开发结束了，已经上线了。运行正常。客户提出了新的需求：凡是在系统中进行修改操作的，删除操作的，新增操作的，都要把这个人记录下来。因为这几个操作是属于危险行为。例如有业务类和业务方法：

```java
package com.jkweilai.spring.biz;

import org.springframework.stereotype.Component;

@Component
//用户业务
public class UserService {
    public void getUser(){
        System.out.println("获取用户信息");
    }
    public void saveUser(){
        System.out.println("保存用户");
    }
    public void deleteUser(){
        System.out.println("删除用户");
    }
    public void modifyUser(){
        System.out.println("修改用户");
    }
}
```

```java
package com.jkweilai.spring.biz;

import org.springframework.stereotype.Component;

// 商品业务类
@Component
public class ProductService {
    public void getProduct(){
        System.out.println("获取商品信息");
    }
    public void saveProduct(){
        System.out.println("保存商品");
    }
    public void deleteProduct(){
        System.out.println("删除商品");
    }
    public void modifyProduct(){
        System.out.println("修改商品");
    }
}

```

注意：已经添加了@Component注解。

接下来我们使用aop来解决上面的需求：编写一个负责安全的切面类

```java
package com.jkweilai.spring.biz;

import org.aspectj.lang.JoinPoint;
import org.aspectj.lang.annotation.Aspect;
import org.aspectj.lang.annotation.Before;
import org.aspectj.lang.annotation.Pointcut;
import org.springframework.stereotype.Component;

@Component
@Aspect
public class SecurityAspect {

    @Pointcut("execution(* com.jkweilai.spring.biz..save*(..))")
    public void savePointcut(){}

    @Pointcut("execution(* com.jkweilai.spring.biz..delete*(..))")
    public void deletePointcut(){}

    @Pointcut("execution(* com.jkweilai.spring.biz..modify*(..))")
    public void modifyPointcut(){}

    @Before("savePointcut() || deletePointcut() || modifyPointcut()")
    public void beforeAdivce(JoinPoint joinpoint){
        System.out.println("XXX操作员正在操作"+joinpoint.getSignature().getName()+"方法");
    }
}

```

```java
@Test
public void testSecurity(){
    ApplicationContext applicationContext = new AnnotationConfigApplicationContext(SpringConfiguration.class);
    UserService userService = applicationContext.getBean("userService", UserService.class);
    ProductService productService = applicationContext.getBean("productService", ProductService.class);
    userService.getUser();
    userService.saveUser();
    userService.deleteUser();
    userService.modifyUser();
    productService.getProduct();
    productService.saveProduct();
    productService.deleteProduct();
    productService.modifyProduct();
}
```

执行结果：

![](https://cdn.nlark.com/yuque/0/2025/png/21376908/1763901002972-6212a72e-2316-44ba-80a2-9c2817a277df.png)
