# 内容协商时，优先考虑请求参数format方式。

spring.mvc.contentnegotiation.favor-parameter=true

```

测试：

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1765110575841-9db9f89d-a913-4802-963c-244df980dd33.png" width="597.6" title="" crop="0,0,1,1" id="u32889b33" class="ne-image">

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1765110605566-dd3c535b-61b5-4006-b875-0cadaae5a06e.png" width="597.6" title="" crop="0,0,1,1" id="uad2f6564" class="ne-image">

可以看到，现在SpringBoot已经优先考虑使用`请求参数format`方式了。

当然，请求参数的名字可以不使用`format`吗？支持定制化吗？答案是支持的，例如你希望请求参数的名字为`type`，可以做如下配置：

```properties
