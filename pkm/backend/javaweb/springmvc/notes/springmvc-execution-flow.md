# SpringMVC 执行流程

---

## SpringMVC 九大核心角色

****前端控制器（DispatcherServlet）****

+ ****角色******：中央调度器、总指挥**
+ ****职责******：接收所有请求，统一分发和协调**

****处理器映射器（HandlerMapping）****

+ ****角色******：路由导航员**
+ ****职责******：根据请求URL找到对应的处理器（建立URL→处理器的映射）**

****处理器执行链（HandlerExecutionChain）****

+ ****角色******：执行任务包**
+ ****职责******：封装******处理器方法**********+**********拦截器集合******，形成完整的执行单元**

****处理器（Handler）****

+ ****角色******：业务执行者（通常是Controller）**
+ ****职责******：执行业务逻辑，处理具体请求**

****处理器适配器（HandlerAdapter）****

+ ****角色******：万能转换器**
+ ****职责******：适配不同处理器类型，让DispatcherServlet能用统一方式调用它们**

****拦截器（Interceptor）****

+ ****角色******：AOP切面卫士**
+ ****职责******：在处理器前后插入通用逻辑（权限、日志等）**

****ModelAndView****

+ ****角色******：数据视图封装器**
+ ****职责******：携带业务数据（Model）+ 视图信息（View）**

****视图解析器（ViewResolver）****

+ ****角色******：视图定位器**
+ ****职责******：将逻辑视图名（如"home"）解析为具体视图对象（如home.jsp）**

****视图（View）****

+ ****角色******：页面渲染器**
+ ****职责******：最终渲染HTML/JSON等响应内容**

---

## 从源码角度看执行流程

以下是核心代码：

```java

public class DispatcherServlet extends FrameworkServlet {
    protected void doDispatch(HttpServletRequest request, HttpServletResponse response) throws Exception {
        // 根据请求对象获取处理器执行链
        // 处理器执行链中封装了：处理器方法 和 拦截器集合
        HandlerExecutionChain mappedHandler = getHandler(processedRequest); // 该方法底层调用了处理器映射器（根据请求路径找到对应处理器方法）

        // 通过处理器执行链获取处理器
        // 根据处理器获取适合的处理器适配器
        // 为什么需要一个处理器适配器？
        // 因为处理器类型多样（Controller、HttpRequestHandler等），适配器模式让DispatcherServlet能用统一方式调用它们。
        HandlerAdapter ha = getHandlerAdapter(mappedHandler.getHandler());

        // 顺序执行所有拦截器中的 preHandle 方法
        if (!mappedHandler.applyPreHandle(processedRequest, response)) {
            return;
        }

        // 通过处理器适配器调用处理器方法
        // 在调用处理器方法之前会进行数据绑定，将表单提交的数据绑定到处理器方法上。（底层是通过WebDataBinder完成的）
        // 如果有@RequestBody注解，则数据绑定的过程中会使用到消息转换器：HttpMessageConverter
        // 结束后返回ModelAndView对象
        mv = ha.handle(processedRequest, response, mappedHandler.getHandler());

        //  逆序执行所有拦截器中的 postHandle 方法
        mappedHandler.applyPostHandle(processedRequest, response, mv);

        // 处理分发结果（在这个方法中完成了响应）
        processDispatchResult(processedRequest, response, mappedHandler, mv, dispatchException);
    }

    // 根据每一次的请求对象来获取处理器执行链对象
    // 底层就是通过处理器映射器找到处理器方法，并将处理器方法（HandlerMethod）和拦截器集合封装为处理器执行链对象。
    protected HandlerExecutionChain getHandler(HttpServletRequest request) throws Exception {
        if (this.handlerMappings != null) {
            for (HandlerMapping mapping : this.handlerMappings) {
                HandlerExecutionChain handler = mapping.getHandler(request);
                if (handler != null) {
                    return handler;
                }
            }
        }
        return null;
    }

    private void processDispatchResult(HttpServletRequest request, HttpServletResponse response,
            @Nullable HandlerExecutionChain mappedHandler, @Nullable ModelAndView mv,
            @Nullable Exception exception) throws Exception {
        // 渲染
        render(mv, request, response);
        // 渲染完毕后，调用该请求对应的所有拦截器的 afterCompletion方法。
        mappedHandler.triggerAfterCompletion(request, response, null);
    }

    protected void render(ModelAndView mv, HttpServletRequest request, HttpServletResponse response) throws Exception {
        // 通过视图解析器返回视图对象
        view = resolveViewName(viewName, mv.getModelInternal(), locale, request);
        // 真正的渲染视图
        view.render(mv.getModelInternal(), request, response);
    }

    protected View resolveViewName(String viewName, @Nullable Map<String, Object> model,
            Locale locale, HttpServletRequest request) throws Exception {
        // 通过视图解析器返回视图对象
        View view = viewResolver.resolveViewName(viewName, locale);
    }
}

```

```java

public interface ViewResolver {
    View resolveViewName(String viewName, Locale locale) throws Exception;
}

```

```java

public interface View {
    void render(@Nullable Map<String, ?> model, HttpServletRequest request, HttpServletResponse response)
            throws Exception;
}

```

---

## 从画图角度看执行流程

<img src="https://cdn.nlark.com/yuque/0/2024/png/21376908/1711943505835-476f954e-ba6c-4a78-b16b-683524e25520.png" width="1508" title="" crop="0,0,1,1" id="u96674032" class="ne-image" style="font-size: 16px">

**SpringMVC 执行流程文字性的描述：**

1. **用户发送请求到******前端控制器（DispatcherServlet）****
2. **控制器调用**********doDispatch()**********方法进行统一分发**
3. **通过******处理器映射器（HandlerMapping）**********查找对应的******处理器执行链（HandlerExecutionChain）****
4. **执行链包含：******处理器方法（HandlerMethod）**********+**********拦截器列表（Interceptors）****
5. **根据******处理器类型******获取对应的******处理器适配器（HandlerAdapter）****
6. ****顺序执行******所有拦截器的**********preHandle()**********方法**
7. **适配器调用处理器的目标方法执行业务逻辑**
8. **处理器返回******逻辑视图名******给适配器**
9. **适配器封装成**********ModelAndView**********返回给前端控制器**
10. ****逆序执行******拦截器的**********postHandle()**********方法**
11. **前端控制器调用******视图解析器（ViewResolver）******解析视图（View）**
12. **视图(View)进行渲染并返回响应**
13. ****逆序执行******拦截器的******afterCompletion()******方法（无论成功失败都会执行）**

---

## 处理器映射器和处理器适配器的创建时机

先搞明白核心类的继承关系：

**DispatcherServlet** extends **FrameworkServlet** extends **HttpServletBean** extends **HttpServlet** extends **GenericServlet** implements **Servlet**

服务器启动阶段完成了：

1. 初始化Spring上下文，也就是创建所有的bean，让IoC容器将其管理起来。
2. 初始化SpringMVC相关的对象：处理器映射器，处理器适配器等。。。

<img src="https://cdn.nlark.com/yuque/0/2024/png/21376908/1711945073073-1466293a-37a5-4e04-a628-00225ec9ad8f.png" width="1035" title="" crop="0,0,1,1" id="u358e4869" class="ne-image" style="font-size: 16px">

<img src="https://cdn.nlark.com/yuque/0/2024/png/21376908/1711945189838-6546c84c-23c9-479d-b2df-893851fdb912.png" width="842" title="" crop="0,0,1,1" id="u1c451def" class="ne-image" style="font-size: 16px">

<img src="https://cdn.nlark.com/yuque/0/2024/png/21376908/1711945264590-8b563ba5-bf2a-4e27-8695-9a0ee2577f2a.png" width="1280" title="" crop="0,0,1,1" id="udcc03fa7" class="ne-image" style="font-size: 16px">

<img src="https://cdn.nlark.com/yuque/0/2024/png/21376908/1711945298853-016466d1-3882-461f-8ac5-296983a67d24.png" width="1348" title="" crop="0,0,1,1" id="ufef5ee9d" class="ne-image" style="font-size: 16px">

<img src="https://cdn.nlark.com/yuque/0/2024/png/21376908/1711945338150-b4f14a20-cc75-4915-9651-51acbffcd872.png" width="805" title="" crop="0,0,1,1" id="u3f47fae4" class="ne-image" style="font-size: 16px">

<img src="https://cdn.nlark.com/yuque/0/2024/png/21376908/1711945352375-01882059-ab91-4668-a595-eb83ca01344c.png" width="815" title="" crop="0,0,1,1" id="u935e0db6" class="ne-image" style="font-size: 16px">

<img src="https://cdn.nlark.com/yuque/0/2024/png/21376908/1711945371377-87ac618e-495f-4fe9-92c4-50a1f2c199d8.png" width="757" title="" crop="0,0,1,1" id="u63c8bc73" class="ne-image" style="font-size: 16px">

<img src="https://cdn.nlark.com/yuque/0/2024/png/21376908/1711945408231-6e96abeb-ceff-480e-9f2c-72bfa2a5d419.png" width="748" title="" crop="0,0,1,1" id="u9d958078" class="ne-image" style="font-size: 16px">

---

## 常见面试题

****Q：处理器映射器和适配器什么时候创建？****

**在Spring容器启动时，DispatcherServlet初始化阶段创建的。具体是在**`**initStrategies()**`**方法中，通过**`**initHandlerMappings()**`**和**`**initHandlerAdapters()**`**方法从Spring容器中获取所有相关Bean，并按优先级排序后缓存在DispatcherServlet中。这样请求到来时就能直接使用，不需要每次请求都重新创建。**

****

****Q：请你描述一下 SpringMVC 的执行流程？****

1. **用户发送请求到******前端控制器（DispatcherServlet）****
2. **控制器调用**********doDispatch()**********方法进行统一分发**
3. **通过******处理器映射器（HandlerMapping）**********查找对应的******处理器执行链（HandlerExecutionChain）****
4. **执行链包含：******处理器方法（HandlerMethod）**********+**********拦截器列表（Interceptors）****
5. **根据处理器类型获取对应的******处理器适配器（HandlerAdapter）****
6. ****顺序执行******所有拦截器的**********preHandle()**********方法**
7. **适配器调用处理器的目标方法执行业务逻辑**
8. **处理器返回******逻辑视图名******给适配器**
9. **适配器封装成**********ModelAndView**********返回给前端控制器**
10. ****逆序执行******拦截器的**********postHandle()**********方法**
11. **前端控制器调用******视图解析器（ViewResolver）**********解析视图**
12. **视图进行渲染并返回响应**
13. ****逆序执行******拦截器的******afterCompletion()******方法（抛异常了也会执行）**

****

****Q：DispatcherServlet的作用？**********它是Spring MVC的总指挥，负责请求分发、协调各组件工作。**

****

****Q：为什么需要HandlerAdapter？**********因为处理器类型多样（Controller、HttpRequestHandler等），适配器模式让DispatcherServlet能用统一方式调用它们。**

****

****Q：拦截器三个方法的执行时机？**********preHandle在处理器前，postHandle在处理器后但视图渲染前，afterCompletion在视图渲染后。**

****

****Q：过滤器和拦截器在流程中的位置？**********过滤器在最外层（Tomcat层面），然后才进入Spring MVC的DispatcherServlet → 拦截器 → 处理器。**

****
