# Bean的循环依赖问题

---

## 什么是Bean的循环依赖

A对象中有B属性。B对象中有A属性。这就是循环依赖。我依赖你，你也依赖我。

比如：丈夫类Husband，妻子类Wife。Husband中有Wife的引用。Wife中有Husband的引用。

![](https://cdn.nlark.com/yuque/0/2022/png/21376908/1665452274046-82594b87-2974-4e08-a6ab-2218d001d14f.png)

```java
public class Husband {
    private String name;
    private Wife wife;
}

```

```java
public class Wife {
    private String name;
    private Husband husband;
}

```

---

## singleton下的set注入产生的循环依赖

我们来编写程序，测试一下在singleton+setter的模式下产生的循环依赖，Spring是否能够解决？

```java
public class Husband {
    private String name;
    private Wife wife;

    public void setName(String name) {
        this.name = name;
    }

    public String getName() {
        return name;
    }

    public void setWife(Wife wife) {
        this.wife = wife;
    }

    // toString()方法重写时需要注意：不能直接输出wife，输出wife.getName()。要不然会出现递归导致的栈内存溢出错误。
    @Override
    public String toString() {
        return "Husband{" +
                "name='" + name + '\'' +
                ", wife=" + wife.getName() +
                '}';
    }
}

```

```java
public class Wife {
    private String name;
    private Husband husband;

    public void setName(String name) {
        this.name = name;
    }

    public String getName() {
        return name;
    }

    public void setHusband(Husband husband) {
        this.husband = husband;
    }

    // toString()方法重写时需要注意：不能直接输出husband，输出husband.getName()。要不然会出现递归导致的栈内存溢出错误。
    @Override
    public String toString() {
        return "Wife{" +
                "name='" + name + '\'' +
                ", husband=" + husband.getName() +
                '}';
    }
}

```

```xml
<bean id="husbandBean" class="com.jkweilai.spring.bean.Husband" scope="singleton">
    <property name="name" value="张三"/>
    <property name="wife" ref="wifeBean"/>
</bean>
<bean id="wifeBean" class="com.jkweilai.spring.bean.Wife" scope="singleton">
    <property name="name" value="小花"/>
    <property name="husband" ref="husbandBean"/>
</bean>
```

```java
public class CircularDependencyTest {

    @Test
    public void testSingletonAndSet(){
        ApplicationContext applicationContext = new ClassPathXmlApplicationContext("spring.xml");
        Husband husbandBean = applicationContext.getBean("husbandBean", Husband.class);
        Wife wifeBean = applicationContext.getBean("wifeBean", Wife.class);
        System.out.println(husbandBean);
        System.out.println(wifeBean);
    }
}

```

执行结果：

![](https://cdn.nlark.com/yuque/0/2025/png/21376908/1763786197531-47f4054d-19e8-4364-93e8-f7d366cdd880.png)

****通过测试得知：在singleton + set注入的情况下，循环依赖是没有问题的。Spring可以解决这个问题。****

****

---

## prototype下的set注入产生的循环依赖

我们再来测试一下：prototype+set注入的方式下，循环依赖会不会出现问题？

```xml
<bean id="husbandBean" class="com.jkweilai.spring.bean.Husband" scope="prototype">
    <property name="name" value="张三"/>
    <property name="wife" ref="wifeBean"/>
</bean>
<bean id="wifeBean" class="com.jkweilai.spring.bean.Wife" scope="prototype">
    <property name="name" value="小花"/>
    <property name="husband" ref="husbandBean"/>
</bean>
```

执行测试程序：发生了异常，异常信息如下：

Caused by: org.springframework.beans.factory.****BeanCurrentlyInCreationException****: Error creating bean with name 'husbandBean': Requested bean is currently in creation: Is there an unresolvable circular reference?

    at org.springframework.beans.factory.support.AbstractBeanFactory.doGetBean(AbstractBeanFactory.java:265)

    at org.springframework.beans.factory.support.AbstractBeanFactory.getBean(AbstractBeanFactory.java:199)

    at org.springframework.beans.factory.support.BeanDefinitionValueResolver.resolveReference(BeanDefinitionValueResolver.java:325)

    ... 44 more

翻译为：创建名为“husbandBean”的bean时出错：请求的bean当前正在创建中：是否存在无法解析的循环引用？

通过测试得知，当循环依赖的****所有Bean****的scope="prototype"的时候，产生的循环依赖，Spring是无法解决的，会出现****BeanCurrentlyInCreationException****异常。

大家可以测试一下，以上两个Bean，如果其中一个是singleton，另一个是prototype，是没有问题的。

为什么两个Bean都是prototype时会出错呢？由于是 prototype，因此会注入一个新的对象，新对象注入时又需要关联注入一个新对象。

---

## singleton下的构造注入产生的循环依赖

我们再来测试一下singleton + 构造注入的方式下，spring是否能够解决这种循环依赖。

```java
public class Husband {
    private String name;
    private Wife wife;

    public Husband(String name, Wife wife) {
        this.name = name;
        this.wife = wife;
    }

    // -----------------------分割线--------------------------------
    public String getName() {
        return name;
    }

    @Override
    public String toString() {
        return "Husband{" +
                "name='" + name + '\'' +
                ", wife=" + wife +
                '}';
    }
}

```

```java
public class Wife {
    private String name;
    private Husband husband;

    public Wife(String name, Husband husband) {
        this.name = name;
        this.husband = husband;
    }

    // -------------------------分割线--------------------------------
    public String getName() {
        return name;
    }

    @Override
    public String toString() {
        return "Wife{" +
                "name='" + name + '\'' +
                ", husband=" + husband +
                '}';
    }
}

```

```xml
<bean id="hBean" class="com.jkweilai.spring.bean2.Husband" scope="singleton">
    <constructor-arg name="name" value="张三"/>
    <constructor-arg name="wife" ref="wBean"/>
</bean>

<bean id="wBean" class="com.jkweilai.spring.bean2.Wife" scope="singleton">
    <constructor-arg name="name" value="小花"/>
    <constructor-arg name="husband" ref="hBean"/>
</bean>
```

```java
@Test
public void testSingletonAndConstructor(){
    ApplicationContext applicationContext = new ClassPathXmlApplicationContext("spring2.xml");
    Husband hBean = applicationContext.getBean("hBean", Husband.class);
    Wife wBean = applicationContext.getBean("wBean", Wife.class);
    System.out.println(hBean);
    System.out.println(wBean);
}
```

执行结果：发生了异常，信息如下：

Caused by: org.springframework.beans.factory.****BeanCurrentlyInCreationException****: Error creating bean with name 'hBean': Requested bean is currently in creation: Is there an unresolvable circular reference?

    at org.springframework.beans.factory.support.DefaultSingletonBeanRegistry.beforeSingletonCreation(DefaultSingletonBeanRegistry.java:355)

    at org.springframework.beans.factory.support.DefaultSingletonBeanRegistry.getSingleton(DefaultSingletonBeanRegistry.java:227)

    at org.springframework.beans.factory.support.AbstractBeanFactory.doGetBean(AbstractBeanFactory.java:324)

    at org.springframework.beans.factory.support.AbstractBeanFactory.getBean(AbstractBeanFactory.java:199)

    at org.springframework.beans.factory.support.BeanDefinitionValueResolver.resolveReference(BeanDefinitionValueResolver.java:325)

    ... 56 more

和上一个测试结果相同，都是提示产生了循环依赖，并且Spring是无法解决这种循环依赖的。

为什么呢？

****主要原因是因为通过构造方法注入导致的：因为构造方法注入会导致********实例化对象的过程********和********对象属性赋值的过程********没有分离开，必须在一起完成导致的。****

****

---

## Spring解决循环依赖的机理

**Spring通过三级缓存机制，在Bean的生命周期中巧妙地设置了一个“提前曝光”的节点，允许半成品的Bean被引用，从而打破了循环依赖的死锁。这套设计是Spring容器生命周期管理中非常精妙的一部分。**

### 三个缓存

![](https://cdn.nlark.com/yuque/0/2022/png/21376908/1665456331018-18c45ae3-fa4c-4cd8-aabf-d9bace567693.png)

| ****缓存级别**** | ****名称**** | ****存储内容**** | ****作用**** | ****类比**** |
| --- | --- | --- | --- | --- |
| ****第一级**** | `**singletonObjects**` | **完整的、成熟的Bean** | **对外提供最终可用的Bean** | ****成品仓库**** |
| ****第二级**** | `**earlySingletonObjects**` | **早期的Bean引用** | **避免重复创建早期引用** | ****半成品暂存区**** |
| ****第三级**** | `**singletonFactories**` | `**ObjectFactory**` | ****核心：解决循环依赖，并处理AOP代理**** | ****生产线**** |

### 源码分析

在该类中有这样一个方法addSingletonFactory()，这个方法的作用是：将创建Bean对象的ObjectFactory对象提前曝光。

![](https://cdn.nlark.com/yuque/0/2022/png/21376908/1665460724682-2222366d-cc07-43db-a8d0-fb27712b20a4.png)

再分析下面的源码：

![](https://cdn.nlark.com/yuque/0/2022/png/21376908/1665460240687-3d0794c4-e6ed-4653-9463-767a7f943ff9.png)

从源码中可以看到，spring会先从一级缓存中获取Bean，如果获取不到，则从二级缓存中获取Bean，如果二级缓存还是获取不到，则从三级缓存中获取之前曝光的ObjectFactory对象，通过ObjectFactory对象获取Bean实例。

### 总结描述

**让我们结合Spring的******三级缓存******来描述这个流程：**

1. ****开始创建ClassA******：**
    - `**getBean("classA")**`**->**`**doCreateBean("classA")**`
    - ****步骤1：实例化******。通过反射调用构造函数，创建一个“原始”的ClassA对象（此时它的属性**`**classB**`**还是**`**null**`**）。**
    - ****步骤2：提前曝光******。Spring意识到ClassA还在创建中，于是将一个能生产ClassA的******ObjectFactory******（对象工厂）放入******第三级缓存****`**singletonFactories**`**中。**
2. ****填充ClassA的属性（解析依赖）******：**
    - **Spring发现ClassA有一个**`**@Autowired**`**的属性**`**classB**`**。**
    - **于是执行**`**getBean("classB")**`**去获取ClassB的实例。**
3. ****开始创建ClassB******：**
    - `**getBean("classB")**`**->**`**doCreateBean("classB")**`
    - ****步骤1：实例化******。创建一个“原始”的ClassB对象。**
    - ****步骤2：提前曝光******。同样，将ClassB的ObjectFactory放入******第三级缓存******。**
4. ****填充ClassB的属性（解析依赖）******：**
    - **Spring发现ClassB有一个**`**@Autowired**`**的属性**`**classA**`**。**
    - **于是执行**`**getBean("classA")**`**去获取ClassA的实例。**
5. ****关键时刻：解决循环依赖******：**
    - **这次调用**`**getBean("classA")**`**不会从头开始创建，因为Spring发现：**
        * **在******第一级缓存****`**singletonObjects**`**中找不到ClassA。**
        * **在******第二级缓存****`**earlySingletonObjects**`**中也找不到ClassA。**
        * ****但在第三级缓存********`****singletonFactories****`********中找到了ClassA的对象工厂******。**
    - **Spring******执行这个对象工厂的****`****getObject()****`****方法******。这个方法可能会返回ClassA的原始对象，也可能返回一个被AOP增强的代理对象（如果ClassA需要被代理的话）。**
    - **然后，将这个（可能是早期的代理）对象放入******第二级缓存******，并从第三级缓存中移除。**
    - **最后，将这个ClassA的早期引用注入给ClassB的**`**classA**`**属性。**
6. ****完成创建流程******：**
    - **ClassB的属性填充完成，完成后续的初始化（如**`**InitializingBean**`**,**`**init-method**`**），然后ClassB这个完整的Bean被放入******第一级缓存******。**
    - **此时，ClassA的**`**getBean("classB")**`**调用返回，将创建好的ClassB实例注入到ClassA的**`**classB**`**属性中。**
    - **ClassA完成属性填充和后续初始化，最终也被放入******第一级缓存******。**

![](https://cdn.nlark.com/yuque/0/2025/png/21376908/1763803781026-9807d217-2e77-4023-b378-fabc277c811f.png)

### **面试题：为什么需要三级，两级不行吗？**

****一句话概括：******三级缓存的核心目的是为了******在解决循环依赖的同时，能够无缝地兼容Spring AOP的代理机制******。如果只用两级缓存，无法处理代理Bean的循环依赖。**

****详细阐述（请按这个逻辑顺序说）：****

1. ****首先，明确三级缓存各自的作用：****
    - ****一级缓存********`****singletonObjects****`**：存放完全创建好的成品Bean。**
    - ****二级缓存********`****earlySingletonObjects****`**：存放提前暴露的、早期的Bean对象（半成品）。**
    - ****三级缓存********`****singletonFactories****`**：存放的不是Bean对象，而是能生产Bean的**`**ObjectFactory**`**（对象工厂）。**
2. ****提出关键问题：如果没有三级缓存，只用一级和二级会怎样？******假设我们去掉第三级，只保留第一级（成品）和第二级（早期引用）。那么流程会是这样：**
    - **实例化Bean A之后，我们会直接把******原始对象A******放入第二级缓存。**
    - **当Bean B依赖A时，从第二级缓存中拿到这个******原始对象A******，并注入给B。**
    - **B创建完成后，A继续完成属性填充和初始化。**
    - ****致命问题来了******：如果Bean A需要被AOP代理，那么最终放入一级缓存的应该是它的******代理对象********`****$ProxyA****`**。这就导致了一个严重的不一致：**
        * ****Bean B里面持有的是原始对象A。****
        * ****而Spring容器里最终管理的是代理对象********`****$ProxyA****`****。****
    - **后果：通过B调用A的方法时，******完全不会经过AOP代理的增强逻辑******（例如事务、日志等全部失效），因为B调用的是一个“假的”、未被代理的对象。这是绝对不允许的。**
3. ****引出第三级缓存的解决方案：******第三级缓存**`**singletonFactories**`**存储的**`**ObjectFactory**`**就是一个******智能的决策器******。它的核心价值在于******“延迟决策”******和******“动态生成”******。**
    - **当发生循环依赖，需要获取A的早期引用时，Spring不会直接返回一个固定的对象，而是******调用三级缓存里的********`****ObjectFactory.getObject()****`********方法******。**
    - **这个方法会进行判断：**
        * **如果这个Bean******不需要被代理******，它就返回原始的Bean对象。**
        * **如果这个Bean******需要被代理******，它就有机会******立即生成并返回一个代理对象******。**
    - **这样，Bean B在创建时，注入到它里面的就是A的******代理对象****`****$ProxyA****`**。这个代理对象与最终放入一级缓存的Bean是******同一个对象******，从而保证了依赖的一致性，AOP功能也能正常生效。**

### **面试题：Spring 是如何解决循环依赖问题的**

**Spring框架通过一个精妙的“三级缓存”机制，默认******解决了单例Bean之间通过Setter方法或字段注入（即非构造器注入）造成的循环依赖问题******。**

****核心回答（分步阐述）：****

****1. 核心机制：三级缓存****

**Spring在**`**DefaultSingletonBeanRegistry**`**类中维护了三个Map，也就是我们常说的“三级缓存”，这是解决循环依赖的基石：**

+ ****第一级缓存********`****singletonObjects****`**：存放******已经完全创建好******的、成熟的单例Bean。这是我们日常从Spring容器中获取到的最终产品。**
+ ****第二级缓存********`****earlySingletonObjects****`**：存放******提前暴露的、早期的Bean引用******。这些Bean已经实例化，但还未进行属性填充和初始化，是一个“半成品”。**
+ ****第三级缓存********`****singletonFactories****`**：存放用于创建Bean的**`****ObjectFactory****`****（对象工厂）******。这是整个机制中最关键的部分。**

****2. 解决流程（结合经典案例 ClassA********↔********ClassB）****

**让我们以ClassA依赖ClassB，ClassB又依赖ClassA为例：**

+ ****第一步：开始创建ClassA****
    1. **Spring调用**`**getBean("classA")**`**，发现A不在任何缓存中，开始创建。**
    2. ****实例化******：通过构造函数**`**new ClassA()**`**，在堆内存中分配空间，创建一个******原始对象******（此时它的**`**classB**`**属性为**`**null**`**）。**
    3. ****提前曝光******：Spring将这个原始A对象包装成一个**`**ObjectFactory**`**，并放入******第三级缓存******。******（至此，A已经可以被其他Bean“发现”了。）****
+ ****第二步：填充ClassA的属性（发现循环依赖）****
    1. **Spring开始为A进行属性填充**`**populateBean()**`**，发现它依赖**`**classB**`**。**
    2. **于是调用**`**getBean("classB")**`**去获取B。**
+ ****第三步：开始创建ClassB****
    1. **流程与创建A类似：实例化B，创建一个原始对象。**
    2. **将B的**`**ObjectFactory**`**放入******第三级缓存******。**
+ ****第四步：填充ClassB的属性（解决循环依赖的关键时刻）****
    1. **Spring开始为B填充属性，发现它依赖**`**classA**`**。**
    2. **于是再次调用**`**getBean("classA")**`**。**
    3. **这次调用，Spring的查找顺序是：**
        * **一级缓存（成品）？******没有******。**
        * **二级缓存（半成品）？******没有******。**
        * ****三级缓存（对象工厂）？找到了！****
    4. **Spring立即调用这个**`**ObjectFactory**`**的**`**getObject()**`**方法。这个方法会进行一个关键判断：**
        * **如果ClassA******不需要******被AOP代理，则直接返回原始A对象。**
        * **如果ClassA******需要******被AOP代理，则会******智能地提前返回一个A的代理对象******。**
    5. **无论返回的是原始对象还是代理对象，Spring都会将其放入******第二级缓存******，并******从第三级缓存中移除******对应的**`**ObjectFactory**`**。**
    6. **最终，这个（可能是早期的代理）对象被成功注入到ClassB的**`**classA**`**属性中。******至此，循环依赖的“环”被打破了。****
+ ****第五步：完成创建流程****
    1. **ClassB注入A成功后，继续完成后续的初始化，然后成为一个完整的Bean，被放入******第一级缓存******。**
    2. **此时，最初创建A的流程（**`**getBean("classB")**`**）成功返回B实例，并将其注入到A的**`**classB**`**属性中。**
    3. **ClassA也继续完成自己的初始化，最终被放入******第一级缓存******。整个应用程序上下文启动成功。**

### **面试题： Spring 不能解决的循环依赖场景有哪些？**

1. ****构造器注入******：因为构造器注入要求在实例化之时就必须提供完整的依赖对象，而那时Bean本身都还未创建，更无法提前曝光，所以无法解决。**
2. ****原型Bean（Prototype）******：Spring不缓存原型Bean，每次都会重新创建，因此无法利用三级缓存机制。**
