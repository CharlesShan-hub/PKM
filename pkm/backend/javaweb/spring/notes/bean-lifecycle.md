# Bean的生命周期

---

## 什么是Bean的生命周期

Spring其实就是一个管理Bean对象的工厂。它负责对象的创建，对象的销毁等。

所谓的生命周期就是：对象从创建开始到最终销毁的整个过程。

什么时候创建Bean对象？

创建Bean对象的前后会调用什么方法？

Bean对象什么时候销毁？

Bean对象的销毁前后调用什么方法？

---

## 为什么要知道Bean的生命周期

其实生命周期的本质是：在哪个时间节点上调用了哪个类的哪个方法。

我们需要充分的了解在这个生命线上，都有哪些特殊的时间节点。

只有我们知道了特殊的时间节点都在哪，到时我们才可以确定代码写到哪。

我们可能需要在某个特殊的时间点上执行一段特定的代码，这段代码就可以放到这个节点上。当生命线走到这里的时候，自然会被调用。

任何一个生命周期都是基于回调机制的。（提前写好回调函数，到了这个时刻就会调用对应的回调函数。）

---

## Bean的生命周期之5步

Bean生命周期的管理，可以参考Spring的源码：****AbstractAutowireCapableBeanFactory类的doCreateBean()方法******。**

Bean生命周期可以粗略的划分为五大步：

+ 第一步：实例化Bean
+ 第二步：Bean属性赋值
+ 第三步：初始化Bean
+ 第四步：使用Bean
+ 第五步：销毁Bean

![](https://cdn.nlark.com/yuque/0/2022/png/21376908/1665388735200-444405f6-283d-4b3a-8cdf-8c3e01743618.png)

编写测试程序：

定义一个Bean

```java
public class User {
    private String name;

    public User() {
        System.out.println("1.实例化Bean");
    }

    public void setName(String name) {
        this.name = name;
        System.out.println("2.Bean属性赋值");
    }

    public void initBean(){
        System.out.println("3.初始化Bean");
    }

    public void destroyBean(){
        System.out.println("5.销毁Bean");
    }

}

```

```xml
<!--
  init-method属性指定初始化方法。
  destroy-method属性指定销毁方法。
-->
<bean id="userBean" class="com.jkweilai.spring.bean.User" init-method="initBean" destroy-method="destroyBean">
    <property name="name" value="zhangsan"/>
</bean>
```

```java
public class BeanLifecycleTest {
    @Test
    public void testLifecycle(){
        ApplicationContext applicationContext = new ClassPathXmlApplicationContext("spring.xml");
        User userBean = applicationContext.getBean("userBean", User.class);
        System.out.println("4.使用Bean");
        // 只有正常关闭spring容器才会执行销毁方法
        ClassPathXmlApplicationContext context = (ClassPathXmlApplicationContext) applicationContext;
        context.close();
    }
}

```

执行结果：

![](https://cdn.nlark.com/yuque/0/2025/png/21376908/1763779901212-2d884ee4-3595-431e-9069-52bd00213814.png)

需要注意的：

+ 第一：只有正常关闭spring容器，bean的销毁方法才会被调用。
+ 第二：ClassPathXmlApplicationContext类才有close()方法。
+ 第三：配置文件中的init-method指定初始化方法。destroy-method指定销毁方法。

---

## Bean生命周期之7步

在以上的5步中，第3步是初始化Bean，如果你还想在初始化前和初始化后添加代码，可以加入“Bean后处理器”。

编写一个类实现BeanPostProcessor类，并且重写before和after方法：

```java
public class LogBeanPostProcessor implements BeanPostProcessor {
    @Override
    public Object postProcessBeforeInitialization(Object bean, String beanName) throws BeansException {
        System.out.println("Bean后处理器的before方法执行，即将开始初始化");
        return bean;
    }

    @Override
    public Object postProcessAfterInitialization(Object bean, String beanName) throws BeansException {
        System.out.println("Bean后处理器的after方法执行，已完成初始化");
        return bean;
    }
}

```

在spring.xml文件中配置“Bean后处理器”：

```xml
<!--配置Bean后处理器。这个后处理器将作用于当前配置文件中所有的bean。-->
<bean class="com.jkweilai.spring.bean.LogBeanPostProcessor"/>
```

****一定要注意：在spring.xml文件中配置的Bean后处理器将作用于当前配置文件中所有的Bean。****

执行测试程序：

![](https://cdn.nlark.com/yuque/0/2025/png/21376908/1763780009201-436ef7c3-8bc0-44ad-a368-fcfe4de77b54.png)

如果加上Bean后处理器的话，Bean的生命周期就是7步了：

![](https://cdn.nlark.com/yuque/0/2022/png/21376908/1665393936765-0ea5dcdd-859a-4ac5-9407-f06022c498b9.png)

---

## Bean生命周期之10步

如果根据源码跟踪，可以划分更细粒度的步骤，10步：

![](https://cdn.nlark.com/yuque/0/2022/png/21376908/1665394697870-15de433a-8d50-4b31-9b75-b2ca7090c1c6.png)

上图中检查Bean是否实现了Aware的相关接口是什么意思？

Aware相关的接口包括：BeanNameAware、BeanClassLoaderAware、BeanFactoryAware

+ 当Bean实现了BeanNameAware，Spring会将Bean的名字传递给Bean。
+ 当Bean实现了BeanClassLoaderAware，Spring会将加载该Bean的类加载器传递给Bean。
+ 当Bean实现了BeanFactoryAware，Spring会将Bean工厂对象传递给Bean。

测试以上10步，可以让User类实现5个接口，并实现所有方法：

+ BeanNameAware
+ BeanClassLoaderAware
+ BeanFactoryAware
+ InitializingBean
+ DisposableBean

代码如下：

```java
public class User implements BeanNameAware, BeanClassLoaderAware, BeanFactoryAware, InitializingBean, DisposableBean {
    private String name;

    public User() {
        System.out.println("1.实例化Bean");
    }

    public void setName(String name) {
        this.name = name;
        System.out.println("2.Bean属性赋值");
    }

    public void initBean(){
        System.out.println("6.初始化Bean");
    }

    public void destroyBean(){
        System.out.println("10.销毁Bean");
    }

    @Override
    public void setBeanClassLoader(ClassLoader classLoader) {
        System.out.println("3.类加载器：" + classLoader);
    }

    @Override
    public void setBeanFactory(BeanFactory beanFactory) throws BeansException {
        System.out.println("3.Bean工厂：" + beanFactory);
    }

    @Override
    public void setBeanName(String name) {
        System.out.println("3.bean名字：" + name);
    }

    @Override
    public void destroy() throws Exception {
        System.out.println("9.DisposableBean destroy");
    }

    @Override
    public void afterPropertiesSet() throws Exception {
        System.out.println("5.afterPropertiesSet执行");
    }
}

```

```java
public class LogBeanPostProcessor implements BeanPostProcessor {
    @Override
    public Object postProcessBeforeInitialization(Object bean, String beanName) throws BeansException {
        System.out.println("4.Bean后处理器的before方法执行，即将开始初始化");
        return bean;
    }

    @Override
    public Object postProcessAfterInitialization(Object bean, String beanName) throws BeansException {
        System.out.println("7.Bean后处理器的after方法执行，已完成初始化");
        return bean;
    }
}

```

执行结果：

![](https://cdn.nlark.com/yuque/0/2025/png/21376908/1763780194137-98ac319c-369a-4fa1-a83f-4789887ccb22.png)

****通过测试可以看出来：****

+ ****InitializingBean的方法早于init-method的执行。****
+ ****DisposableBean的方法早于destroy-method的执行。****

**对于SpringBean的生命周期，掌握之前的7步即可。够用。**

****相关源码：****

```java
protected Object doCreateBean(String beanName, RootBeanDefinition mbd, @Nullable Object[] args)
        throws BeanCreationException {

    // 第1步：Bean实例化 - 创建Bean的原始对象
    BeanWrapper instanceWrapper = null;
    if (mbd.isSingleton()) {
        instanceWrapper = this.factoryBeanInstanceCache.remove(beanName);
    }
    if (instanceWrapper == null) {
        // 真正的实例化逻辑：通过构造函数、工厂方法等创建Bean实例
        instanceWrapper = createBeanInstance(beanName, mbd, args);
    }
    Object bean = instanceWrapper.getWrappedInstance();
    Class<?> beanType = instanceWrapper.getWrappedClass();
    if (beanType != NullBean.class) {
        mbd.resolvedTargetType = beanType;
    }

    synchronized (mbd.postProcessingLock) {
        if (!mbd.postProcessed) {
            try {
                applyMergedBeanDefinitionPostProcessors(mbd, beanType, beanName);
            }
            catch (Throwable ex) {
                throw new BeanCreationException(mbd.getResourceDescription(), beanName,
                        "Post-processing of merged bean definition failed", ex);
            }
            mbd.markAsPostProcessed();
        }
    }

    // 提前暴露单例Bean的引用，用于解决循环依赖问题
    boolean earlySingletonExposure = (mbd.isSingleton() && this.allowCircularReferences &&
            isSingletonCurrentlyInCreation(beanName));
    if (earlySingletonExposure) {
        if (logger.isTraceEnabled()) {
            logger.trace("Eagerly caching bean '" + beanName +
                    "' to allow for resolving potential circular references");
        }
        // 将Bean的早期引用（可能被代理包装）添加到单例工厂中（三级缓存）
        addSingletonFactory(beanName, () -> getEarlyBeanReference(beanName, mbd, bean));
    }

    // 这是Bean生命周期的核心部分
    Object exposedObject = bean; // 最终暴露给外部的Bean（可能是原始Bean也可能是代理后的Bean）
    try {
        // 第2步：属性赋值 - 依赖注入发生在这里
        // 包括@Autowired、@Value、@Resource等注解的注入
        populateBean(beanName, mbd, instanceWrapper);
        
        // 第3步：初始化Bean - 包含Aware接口、BeanPostProcessor、初始化方法等
        exposedObject = initializeBean(beanName, exposedObject, mbd);
    }
    catch (Throwable ex) {
        if (ex instanceof BeanCreationException bce && beanName.equals(bce.getBeanName())) {
            throw bce;
        }
        else {
            throw new BeanCreationException(mbd.getResourceDescription(), beanName, ex.getMessage(), ex);
        }
    }

    // 处理循环依赖的最终检查
    if (earlySingletonExposure) {
        Object earlySingletonReference = getSingleton(beanName, false);
        if (earlySingletonReference != null) {
            if (exposedObject == bean) {
                exposedObject = earlySingletonReference;
            }
            else if (!this.allowRawInjectionDespiteWrapping && hasDependentBean(beanName)) {
                String[] dependentBeans = getDependentBeans(beanName);
                Set<String> actualDependentBeans = CollectionUtils.newLinkedHashSet(dependentBeans.length);
                for (String dependentBean : dependentBeans) {
                    if (!removeSingletonIfCreatedForTypeCheckOnly(dependentBean)) {
                        actualDependentBeans.add(dependentBean);
                    }
                }
                if (!actualDependentBeans.isEmpty()) {
                    throw new BeanCurrentlyInCreationException(beanName,
                            "Bean with name '" + beanName + "' has been injected into other beans [" +
                            StringUtils.collectionToCommaDelimitedString(actualDependentBeans) +
                            "] in its raw version as part of a circular reference, but has eventually been " +
                            "wrapped. This means that said other beans do not use the final version of the " +
                            "bean. This is often the result of over-eager type matching - consider using " +
                            "'getBeanNamesForType' with the 'allowEagerInit' flag turned off, for example.");
                }
            }
        }
    }

    // 第5步：注册可销毁的Bean - 为Bean的销毁阶段做准备
    try {
        // 注册实现了DisposableBean接口或配置了destroy-method的Bean
        registerDisposableBeanIfNecessary(beanName, bean, mbd);
    }
    catch (BeanDefinitionValidationException ex) {
        throw new BeanCreationException(
                mbd.getResourceDescription(), beanName, "Invalid destruction signature", ex);
    }

    // 返回最终处理完成的Bean（可能是原始对象，也可能是代理对象）
    return exposedObject;
}
```

---

## Bean的作用域不同，管理方式不同

Spring 根据Bean的作用域来选择管理方式。

+ 对于singleton作用域的Bean，Spring 能够精确地知道该Bean何时被创建，何时初始化完成，以及何时被销毁；
+ 而对于 prototype 作用域的 Bean，Spring 只负责创建，当容器创建了 Bean 的实例后，Bean 的实例就交给客户端代码管理，Spring 容器将不再跟踪其生命周期。

我们把之前User类的spring.xml文件中的配置scope设置为prototype：

```xml
<!--
  init-method属性指定初始化方法。
  destroy-method属性指定销毁方法。
-->
<bean id="userBean" class="com.jkweilai.spring.bean.User" init-method="initBean" destroy-method="destroyBean" scope="prototype">
    <property name="name" value="zhangsan"/>
</bean>

<!--配置Bean后处理器。这个后处理器将作用于当前配置文件中所有的bean。-->
<bean class="com.jkweilai.spring.bean.LogBeanPostProcessor"/>
```

执行测试程序：

![](https://cdn.nlark.com/yuque/0/2025/png/21376908/1763780370388-000f1c5f-eb90-4d6c-be76-ac5e39231729.png)

通过测试一目了然。只执行了前8步，第9和10都没有执行。

---

## 自己new的对象如何让Spring管理

有些时候可能会遇到这样的需求，某个java对象是我们自己new的，然后我们希望这个对象被Spring容器管理，怎么实现？

```java
public class User {
}

```

```java
public class RegisterBeanTest {

    @Test
    public void testBeanRegister(){
        // 自己new的对象
        User user = new User();
        System.out.println(user);

        // 创建 默认可列表BeanFactory 对象
        DefaultListableBeanFactory factory = new DefaultListableBeanFactory();
        // 注册Bean
        factory.registerSingleton("userBean", user);
        // 从spring容器中获取bean
        User userBean = factory.getBean("userBean", User.class);
        System.out.println(userBean);
    }
}

```

执行结果：

![](https://cdn.nlark.com/yuque/0/2025/png/21376908/1763780413264-6a23ba14-d5ea-493f-a3da-1c458c62ecbb.png)
