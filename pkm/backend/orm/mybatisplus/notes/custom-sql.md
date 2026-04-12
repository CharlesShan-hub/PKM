# 自定义SQL

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1744292844260-8f50ee88-77dc-48e5-a8a0-80f21c72074d.png" width="646" title="" crop="0,0,1,1" id="ue31c2549" class="ne-image" style="font-size: 16px">

在Java程序中直接编写SQL这是不建议的，怎么解决这个问题？自定义SQL可以解决。

什么是自定义SQL？在Java程序中继续使用`Wrapper`进行条件的封装，将SQL语句编写到`Mapper xml`文件中，将`Wrapper`传递给`Mapper xml`，然后进行SQL语句的拼装。

第一步：在java程序中只进行`Wrapper`条件的构造

```java

@Test
void testCustomSql(){
    // 创建条件构造器
    UpdateWrapper<Car> wrapper = new UpdateWrapper<>();
    // 设置set语句并链式追加条件
    wrapper.eq("brand", "宝马535");
    // 更新
    carMapper.updateByCustomSql(wrapper, 5.0);
}

```

第二步：在Mapper接口中自定义方法

```java

public interface CarMapper extends BaseMapper<Car> {
    void updateByCustomSql(@Param("ew") UpdateWrapper<Car> wrapper, @Param("amount") Double amount);
}

```

注意：`@Param("ew")`中的`ew`是固定写法。当然也可以采用mp内置的常量来代替`"ew"`：**Constants.WRAPPER**

第三步：编写`Mapper xml`的配置

```xml

<mapper namespace="com.jkweilai.mp.mapper.CarMapper">
    <update id="updateByCustomSql">
        update t_car set guide_price = guide_price + #{amount} ${ew.customSqlSegment}
    </update>
</mapper>

```

注意：`${ew.customSqlSegment}`是固定写法。
