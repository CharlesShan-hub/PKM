# 静态工具类Db

静态工具类`Db`的功能和`IService接口`功能一样。

---

## Db中的方法

1. 增

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1744379838552-3d1b6a62-78f0-4e95-9ced-153ac50927dd.png" width="398" title="" crop="0,0,1,1" id="ua4c3cca3" class="ne-image" style="font-size: 16px">

2. 删

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1744379879613-a97aaa06-9577-4605-9531-d9f95324f0df.png" width="508" title="" crop="0,0,1,1" id="u22982222" class="ne-image" style="font-size: 16px">

3. 改

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1744379969894-38d8d299-c939-4217-a70f-301e22528f36.png" width="333" title="" crop="0,0,1,1" id="u91a7bb7c" class="ne-image" style="font-size: 16px">

4. 查

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1744380054930-af582d90-e0d4-488d-823d-05dbc74807bd.png" width="332" title="" crop="0,0,1,1" id="u91c6fd64" class="ne-image" style="font-size: 16px">

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1744380130810-be45dac1-a3b0-4034-9dd9-0ae0f7c2b68a.png" width="413" title="" crop="0,0,1,1" id="ub550de5a" class="ne-image" style="font-size: 16px">

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1744380155936-0916ecd0-e116-40fe-9a19-c3a00d70599d.png" width="370" title="" crop="0,0,1,1" id="u6499aaac" class="ne-image" style="font-size: 16px">

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1744380170477-43b7351a-a986-447a-bc8f-c2e726a8aebd.png" width="219" title="" crop="0,0,1,1" id="uf75204bd" class="ne-image" style="font-size: 16px">

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1744380221861-049ba810-073c-4b2c-895d-837b79fca7e3.png" width="420" title="" crop="0,0,1,1" id="ubad46c88" class="ne-image" style="font-size: 16px">

可以看到以上的方法基本上都是`IService`接口中的方法。

****静态工具类 Db 中的方法一般比 IService 接口中的方法多一个****`****Class****`****参数。这是因为 IService 接口可以通过泛型来指定类型，而静态工具类 Db 是无法指定泛型的。****

---

## 什么情况下需要Db

既然方法一样，为什么还要再提供一个静态工具类Db呢？

现在我们已经有一张表`t_car`，假设我们还有一张表来保存汽车的维修记录`t_wx`，这两张表的结构分别如下：

汽车表：

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1744418354574-6d424729-fe5c-4064-86f9-623c3360c7d7.png" width="314" title="" crop="0,0,1,1" id="uc53f7cdb" class="ne-image" style="font-size: 16px">

维修记录表：

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1744418614986-6917d5d1-fee4-4597-b3b5-53a5251a4c56.png" width="374" title="" crop="0,0,1,1" id="u7666c744" class="ne-image" style="font-size: 16px">

```sql

drop table if exists t_wx;
create table t_wx(
  id bigint primary key auto_increment,
  `time` char(10),
  cost decimal,
  description varchar(255),
  car_id bigint
);
insert into t_wx(`time`,cost,description,car_id) values('2025-10-11',300,'更换火花塞',1);
insert into t_wx(`time`,cost,description,car_id) values('2025-10-12',400,'小保养',1);
insert into t_wx(`time`,cost,description,car_id) values('2025-10-13',500,'大保养',1);
select * from t_wx;

```

可以看到汽车和维修记录的关系是：**一对多**。一个汽车有多条维修记录。

假设我们现在有这样一个需求：给定汽车的id，查询汽车的同时，再将汽车关联的维修记录也查出来。

我们有两张表，那应该是两个Service，分别是：CarService、WeiXiuService，要实现上面的需求，代码应该会是这样的结构：

```java

public class CarServiceImpl extends ServiceImpl<CarMapper, Car> implements CarService{
    @Autowire
    private WeiXiuService weiXiuService;

    // 根据汽车id查询汽车信息，并且携带汽车关联的维修记录
    public Car queryCarAndWeiXiuById(Long id){
        // 这里需要调用 CarService 的方法，也需要调用 WeiXiuService 的方法
    }
}

```

假设我们还有另一个需求：给定维修的id，查询维修记录的同时，再将关联的汽车信息查出来。代码应该是这样的结构：

```java

public class WeiXiuServiceImpl extends ServiceImpl<WeiXiuMapper, WeiXiu> implements WeiXiuService{
    @Autowire
    private CarService carService;

    // 根据维修id查询维修记录，并且携带关联的汽车信息。
    public WeiXiu queryWeiXiuAndCarById(Long id){
        // 这里需要调用 WeiXiuService 的方法，也需要调用 CarService 的方法
    }
}

```

如果代码这样写的话，很容易形成循环依赖。因为CarService中需要注入WeiXiuService，而WeiXiuService中需要注入CarService。怎么避免循环依赖呢？****可以使用Db静态工具类。****这样的话 CarService 中就不需要注入 WeiXiuService，而WeiXiuService中也不再注入CarService。

---

## Db的使用

接下来我们就使用Db来实现这样的需求：给定汽车的id，查询汽车的同时，再将汽车关联的维修记录也查出来。

### 编写`WeiXiu`这个po

```java

package com.jkweilai.carmgtsys.model.po;

import com.baomidou.mybatisplus.annotation.IdType;
import com.baomidou.mybatisplus.annotation.TableField;
import com.baomidou.mybatisplus.annotation.TableId;
import com.baomidou.mybatisplus.annotation.TableName;
import lombok.Data;

@Data
@TableName("t_wx")
public class WeiXiu {
    @TableId(value = "id", type = IdType.AUTO)
    private Long id;
    @TableField("`time`")
    private String time;
    private Double cost;
    private String description;
    private Long carId;
}

```

### 编写`WeiXiuMapper`

```java

package com.jkweilai.carmgtsys.mapper;

import com.baomidou.mybatisplus.core.mapper.BaseMapper;
import com.jkweilai.carmgtsys.model.po.WeiXiu;

public interface WeiXiuMapper extends BaseMapper<WeiXiu> {
}

```

### 编写`WeiXiuVO`

```java

package com.jkweilai.carmgtsys.model.vo;

import io.swagger.v3.oas.annotations.media.Schema;
import lombok.Data;

@Data
@Schema(name = "WeiXiuVO", description = "维修记录的视图对象")
public class WeiXiuVO {
    @Schema(description = "维修记录id")
    private Long id;
    @Schema(description = "维修时间")
    private String time;
    @Schema(description = "维修费用")
    private Double cost;
    @Schema(description = "问题描述")
    private String description;
}

```

### `CarVO`中添加`List<WeiXiuVO>`

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1744427707462-cc4ff4a5-17ba-4ff9-8f03-7e0aa1106ed5.png" width="771" title="" crop="0,0,1,1" id="u11a873e0" class="ne-image" style="font-size: 16px">

### `CarController`中添加业务接口

```java

@Operation(summary = "查询车辆信息以及该车辆的维修记录",
        description = "根据车辆id查询汽车信息，并且将该车辆的维修记录全部查询出来",
        parameters = @Parameter(name = "id", description = "车辆id"))
@GetMapping("queryById/{id}")
public CarVO queryCarAndWeiXiuById(@PathVariable("id") Long id){
    return carService.queryCarAndWeiXiuById(id);
}

```

### `CarServiceImpl`编写业务方法

```java

@Override
public CarVO queryCarAndWeiXiuById(Long id) {
    // 1. 根据id查找车辆信息
    Car car = getById(id);
    // 2. 校验车辆信息是否存在
    if(car == null){
        throw new RuntimeException("车辆信息异常！");
    }
    // 3. 车辆信息存在的情况下继续查询维修记录
    List<WeiXiu> weiXiuList = Db.lambdaQuery(WeiXiu.class)
            .eq(WeiXiu::getCarId, car.getId())
            .list();
    // 4. Car转CarVO
    CarVO carVO = BeanUtil.copyProperties(car, CarVO.class);
    carVO.setWeiXiuList(BeanUtil.copyToList(weiXiuList, WeiXiuVO.class));
    return carVO;
}

```

测试：

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1744427830630-96ed7d4d-6954-4c84-a339-1d8088034bea.png" width="571" title="" crop="0,0,1,1" id="uada41765" class="ne-image" style="font-size: 16px">

****课后练习：给定多个车辆的id，查询这些车辆的信息以及每个车辆关联的维修记录信息。****
