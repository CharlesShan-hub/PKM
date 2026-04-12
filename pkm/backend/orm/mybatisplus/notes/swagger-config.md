# Swagger配置

  mvc:
    pathmatch:
      matching-strategy: ant_path_matcher  # Spring Boot 3集成swagger必须的配置
knife4j:
  enable: true
  openapi:
    title: 汽车信息管理接口文档
    description: 汽车信息管理接口文档
    contact:
      name: 老杜
      email: dujubin@126.com
      url: http://localhost:8080
    version: 1.0.0
  group:
    default:
      group-name: default
      api-rule: package
      api-rule-resources:
        - com.jkweilai.carmgtsys.controller

```

### MyBatis-Plus相关代码

编写po：Car类

```java

package com.jkweilai.carmgtsys.model.po;

import com.baomidou.mybatisplus.annotation.IdType;
import com.baomidou.mybatisplus.annotation.TableId;
import com.baomidou.mybatisplus.annotation.TableName;
import lombok.Data;

@Data
@TableName("t_car")
public class Car {
    @TableId(value = "id", type = IdType.AUTO)
    private Long id;
    private String carNum;
    private String brand;
    private Double guidePrice;
    private String produceTime;
    private String carType;
}

```

mapper的编写：CarMapper接口

```java

package com.jkweilai.carmgtsys.mapper;

import com.baomidou.mybatisplus.core.mapper.BaseMapper;
import com.jkweilai.carmgtsys.po.Car;

public interface CarMapper extends BaseMapper<Car> {
}

```

****在SpringBoot入口程序上添加****`****@MapperScan****`****扫描****

****@MapperScan(basePackages = "com.jkweilai.carmgtsys.mapper")****

service接口的编写：CarService

```java

package com.jkweilai.carmgtsys.service;

import com.baomidou.mybatisplus.extension.service.IService;
import com.jkweilai.carmgtsys.po.Car;

public interface CarService extends IService<Car> {
}

```

service实现类的编写：CarServiceImpl

```java

package com.jkweilai.carmgtsys.service.impl;

import com.baomidou.mybatisplus.extension.service.impl.ServiceImpl;
import com.jkweilai.carmgtsys.mapper.CarMapper;
import com.jkweilai.carmgtsys.po.Car;
import com.jkweilai.carmgtsys.service.CarService;
import org.springframework.stereotype.Service;

@Service
public class CarServiceImpl extends ServiceImpl<CarMapper, Car> implements CarService {
}

```

### 编写dto

```java

package com.jkweilai.carmgtsys.model.dto;

import io.swagger.v3.oas.annotations.media.Schema;
import lombok.Data;

@Data
@Schema(name = "CarDTO", description = "车辆信息传输对象")
public class CarDTO {
    @Schema(description = "车辆唯一ID", example = "1", requiredMode = Schema.RequiredMode.REQUIRED)
    private Long id;

    @Schema(description = "车牌号", example = "京A12345", maxLength = 20)
    private String carNum;

    @Schema(description = "品牌", example = "宝马", maxLength = 50)
    private String brand;

    @Schema(description = "指导价格（万元）", example = "42.5")
    private Double guidePrice;

    @Schema(description = "生产日期（yyyy-MM-dd）", example = "2023-08-01")
    private String produceTime;

    @Schema(description = "车辆类型", example = "SUV", allowableValues = {"SUV", "轿车", "跑车", "MPV"})
    private String carType;
}

```

### 编写vo

```java

package com.jkweilai.carmgtsys.model.vo;

import io.swagger.v3.oas.annotations.media.Schema;
import lombok.Data;

@Data
@Schema(name = "CarVO", description = "车辆信息视图对象")
public class CarVO {
    @Schema(description = "车辆唯一ID", example = "1")
    private Long id;

    @Schema(description = "车牌号码", example = "粤B12345", maxLength = 20)
    private String carNum;

    @Schema(description = "车辆品牌", example = "特斯拉", maxLength = 50)
    private String brand;

    @Schema(description = "官方指导价(单位：万元)", example = "29.99")
    private Double guidePrice;

    @Schema(description = "生产日期(yyyy-MM-dd格式)", example = "2023-05-15")
    private String produceTime;

    @Schema(description = "车辆类型", example = "新能源轿车",
            allowableValues = {"燃油车", "新能源轿车", "SUV", "MPV", "跑车"})
    private String carType;
}

```

### 实现简单的业务接口

编写`CarController`

```java

package com.jkweilai.carmgtsys.controller;

import cn.hutool.core.bean.BeanUtil;
import com.jkweilai.carmgtsys.model.dto.CarDTO;
import com.jkweilai.carmgtsys.model.po.Car;
import com.jkweilai.carmgtsys.model.vo.CarVO;
import com.jkweilai.carmgtsys.service.CarService;
import io.swagger.v3.oas.annotations.Operation;
import io.swagger.v3.oas.annotations.Parameter;
import io.swagger.v3.oas.annotations.tags.Tag;
import lombok.RequiredArgsConstructor;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@Tag(name = "汽车信息管理接口") // swagger注解
@RequestMapping("/cars")
@RestController
@RequiredArgsConstructor // lombok注解，提供必须的构造方法
public class CarController {

    // 该属性会对应一个构造方法，构造方法帮助注入。
    private final CarService carService;

    @Operation(summary = "保存汽车信息") // swagger注解
    @PostMapping
    public void save(@RequestBody CarDTO carDTO) {
        // 1. 将DTO转换为PO
        Car car = BeanUtil.copyProperties(carDTO, Car.class);
        // 2. 保存
        carService.save(car);
    }

    @Operation(summary = "删除汽车信息", description = "根据id删除汽车信息", parameters = {@Parameter(name = "id", description = "车辆id")})
    @DeleteMapping("{id}")
    public void removeById(@PathVariable("id") Long id) {
        carService.removeById(id);
    }

    @Operation(summary = "查询汽车信息", description = "根据id查询汽车信息", parameters = {@Parameter(name = "id", description = "车辆id")})
    @GetMapping("{id}")
    public CarVO getById(@PathVariable("id") Long id) {
        // 1. 根据id查询汽车信息，返回po对象
        Car car = carService.getById(id);
        // 2. 将po对象转换成vo对象返回
        return BeanUtil.copyProperties(car, CarVO.class);
    }

    @Operation(summary = "批量查询汽车信息", description = "根据id批量查询汽车信息", parameters = @Parameter(name = "ids", example="1,2,3" description = "批量的车辆id"))
    @GetMapping
    public List<CarVO> getByIds(@RequestParam("ids") List<Long> ids){
        // 1.根据id批量查询，返回po集合
        List<Car> cars = carService.listByIds(ids);
        // 2.将po集合转换成vo集合
        return BeanUtil.copyToList(cars, CarVO.class);
    }
}

```

### 实现复杂的业务接口

在controller中添加方法：

```java

@Operation(summary = "降低官方指导价", description = "降低给定车辆id的官方指导价",
        parameters = {@Parameter(name = "id", description = "车辆id"),@Parameter(name="price", description = "降价额度")})
@PutMapping("{id}/reduction/{price}")
public void reduction(@PathVariable("id") Long id, @PathVariable("price") Double price){
    carService.reduction(id, price);
}

```

CarService接口添加方法：

```java

public interface CarService extends IService<Car> {
    void reduction(Long id, Double price);
}

```

CarServiceImpl实现方法：

```java

@Service
public class CarServiceImpl extends ServiceImpl<CarMapper, Car> implements CarService {
    @Override
    public void reduction(Long id, Double price) {
        // 1.查询汽车
        Car car = getById(id);
        // 2.判断汽车是否存在
        if(car == null){
            throw new RuntimeException("汽车信息异常！");
        }
        // 3.校验官方指导价
        if(car.getGuidePrice() < price){
            throw new RuntimeException("官方指导价不能小于0！");
        }
        // 4.降价
        baseMapper.reduction(id, price);
    }
}

```

CarMapper添加方法：

```java

public interface CarMapper extends BaseMapper<Car> {

    @Update("UPDATE t_car SET guide_price = guide_price - #{price} WHERE id = #{id}")
    void reduction(@Param("id") Long id, @Param("price") Double price);
}

```

**最后**，启动项目，打开浏览器，输入`Swagger`地址：http://localhost:8080/doc.html 来进行接口的测试：

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1744360643972-df1da6d7-871a-40e3-9930-23d9327ecb78.png" width="1717" title="" crop="0,0,1,1" id="ud4efd0e8" class="ne-image" style="font-size: 16px">

### IService的lambdaQuery()方法

适合复杂查询。

实现一个功能：实现多条件查询。查询条件包括：

+ 可以根据汽车品牌模糊查询
+ 可以根据价格区间查询
+ 可以根据汽车类型查询

实际查询时，不知道用户提供了哪些条件。如果使用原生的`mybatis`实现的话`SQL`应该是这样写：

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1744362927181-94c01deb-74e3-4cda-8688-95cc0cf44182.png" width="593" title="" crop="0,0,1,1" id="u44451229" class="ne-image" style="font-size: 16px">

在mp中应该怎么做呢？可以使用我们之前学过的`Wrapper`，也可以使用`IService`中提供的`lambdaQuery()`方法。下面演示`lambdaQuery()`的用法：

提供`CarQuery`对象来封装查询条件：

```java

package com.jkweilai.carmgtsys.model.query;

import io.swagger.v3.oas.annotations.media.Schema;
import lombok.Data;

@Schema(name = "CarQuery", description = "对汽车进行查询时的多条件封装")
@Data
public class CarQuery {
    @Schema(description = "汽车品牌，支持模糊查询")
    private String brand;

    @Schema(description = "汽车类型，例如：燃油车，电车，氢能源，新能源")
    private String carType;

    @Schema(description = "最低价格")
    private Double minPrice;

    @Schema(description = "最高价格")
    private Double maxPrice;
}

```

在`CarController`中提供`queryByMultiCondition`方法：

****查询操作如果参数不多，RESTful 接口应设计为 get 请求，请求在请求行上提交，以下代码中****`****@ParameterObject****`****是 swagger 的注解，和 SpringMVC 无关。使用这个注解，swagger 在生成文档的时候，会将****`****CarQuery****`****对象的属性拆开在文档中显示。****

```java

@Operation(summary = "多条件查询汽车信息", description = "多条件查询汽车信息")
@GetMapping("/query")
public List<CarVO> queryByMultiCondition(@ParameterObject CarQuery carQuery){
    List<Car> cars = carService.queryByMultiCondition(
            carQuery.getBrand(), carQuery.getCarType(), carQuery.getMinPrice(), carQuery.getMaxPrice());
    return BeanUtil.copyToList(cars, CarVO.class);
}

```

在`CarServiceImpl`中实现`queryByMultiCondition`方法：使用`lambdaQuery()`方法

```java

@Override
public List<Car> queryByMultiCondition(String brand, String carType, Double minPrice, Double maxPrice) {
    // 这里没有再调用 lambdaQuery().select()这样的方法，如果不调用就是将实体类中的@TableField标注的字段都返回。
    // 如果你要返回指定字段，那么就需要手动调用select()方法。
    return lambdaQuery()
            .like(brand != null && !brand.trim().isEmpty(), Car::getBrand, brand)
            .eq(carType != null && !carType.trim().isEmpty(), Car::getCarType, carType)
            .ge(minPrice != null, Car::getGuidePrice, minPrice)
            .le(maxPrice != null, Car::getGuidePrice, maxPrice)
            .list();
}

```

### IService的lambdaUpdate()方法

适合复杂更新语句。

需求：针对提供id的车辆进行降价操作，如果降价后的价格低于10万，则将汽车类型修改为低端车。

直接在`CarServiceImpl`**的**`**reduction()**`**方法基础上做修改：**

```java

@Override
@Transactional
public void reduction(Long id, Double price) {
    // 1.查询汽车
    Car car = getById(id);
    // 2.判断汽车是否存在
    if (car == null) {
        throw new RuntimeException("汽车信息异常！");
    }
    // 3.校验官方指导价
    if (car.getGuidePrice() < price) {
        throw new RuntimeException("官方指导价不能小于0！");
    }
    // 4.降价
    //baseMapper.reduction(id, price);
    Double guidePriceNow = car.getGuidePrice() - price;
    lambdaUpdate()
            .set(Car::getGuidePrice, guidePriceNow)
            .set(guidePriceNow < 10, Car::getCarType, "低端车")
            .eq(Car::getId, id)
            .eq(Car::getGuidePrice, car.getGuidePrice()) // 事务 + 乐观锁 保证原子化操作！
            .update();
}

```

****注意：事务 + 乐观锁 来保证原子化操作！！！****

### IService的批量新增

向`t_car`表中插入1万条车辆信息

1. 第一种方式：不使用批处理操作并记录耗时

```java

@Test
void testSave() {
    long begin = System.currentTimeMillis();
    for (long i = 1; i <= 10000; i++) {
        // 每循环一次创建一个Car对象
        Car car = new Car();
        car.setId(i);
        car.setCarNum("CarNum" + i);
        car.setBrand("宝马" + i);
        car.setGuidePrice(30.0);
        car.setProduceTime("2000-10-11");
        car.setCarType("燃油车");
        // 保存Car
        carService.save(car);
    }
    long end = System.currentTimeMillis();
    System.out.println("耗时" + (end - begin) / 1000 + "秒");
}

```

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1744372402863-22556ef5-fc53-4a2c-9643-ab3f0815c489.png" width="163" title="" crop="0,0,1,1" id="udbcf2268" class="ne-image" style="font-size: 16px">

2. 第二种方式：使用批处理操作并记录耗时

```java

@Test
void testSaveBatch() {
    long begin = System.currentTimeMillis();
    List<Car> cars = new ArrayList<>();
    for (long i = 1; i <= 10000; i++) {
        // 每循环一次创建一个Car对象
        Car car = new Car();
        car.setId(i);
        car.setCarNum("CarNum" + i);
        car.setBrand("宝马" + i);
        car.setGuidePrice(30.0);
        car.setProduceTime("2000-10-11");
        car.setCarType("燃油车");
        cars.add(car);
        // 每100个保存一次
        if(i % 100 == 0){
            carService.saveBatch(cars);
            cars.clear();
        }
    }
    long end = System.currentTimeMillis();
    System.out.println("耗时" + (end - begin) / 1000 + "秒");
}

```

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1744372598941-ca856d4c-382d-43b3-a80b-260b97e93c49.png" width="135" title="" crop="0,0,1,1" id="uc6370e5e" class="ne-image" style="font-size: 16px">

效率得到提升，原理是：每100条`insert`语句打包一次批量发给数据。

3. 在`application.yml`中的`url`后面添加`rewriteBatchedStatements=true`并记录耗时

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1744373051588-13dd3192-2f5a-4d43-8068-8354900bb890.png" width="161" title="" crop="0,0,1,1" id="ubfb75374" class="ne-image" style="font-size: 16px">

它的作用是将这种写法

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1744372873640-bc99c91c-2142-4809-8936-a9ebb3d0c8ca.png" width="325" title="" crop="0,0,1,1" id="uad8149b3" class="ne-image" style="font-size: 16px">

转换成这种写法

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1744372883742-2335e86b-2836-4905-8ac2-83c5f3259683.png" width="434" title="" crop="0,0,1,1" id="ub923bf3e" class="ne-image" style="font-size: 16px">

这是mysql驱动实现的，不是mp的功能。
