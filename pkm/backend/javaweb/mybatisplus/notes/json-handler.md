# json 处理器

---

## 为什么需要 json 处理器

假设汽车表中有一个字段是 json 类型，存储了车主的信息。如下：

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1765424229312-d7cd17b2-8134-45b7-b2f7-70109e129a9b.png" width="945.6" title="" crop="0,0,1,1" id="u77a0f9a7" class="ne-image">

```json

{"id": "909890989898767676", "name": "张三"}
{"id": "909890989898767677", "name": "李四"}
{"id": "909890989898767678", "name": "王五"}

```

**在实体类中应该定义为什么类型的属性来接收这个 json 数据呢？**

1. 定义为 String 直接接收 json 格式的字符串。
2. 定义一个 json 字符串对应的实体类。

显然第二种方式会比较好。因为在 java 程序中操作对象比操作 json 字符串更方便。但默认情况下，数据库表中 json 格式的字符串是不会自动转换成 java 对象的。这个时候就需要 MP 为我们提供的 json 处理器了。

---

## MP 提供的 json 处理器

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1765424546642-67352e0f-e202-454e-aa56-20e3d46d29b0.png" width="479.2" title="" crop="0,0,1,1" id="u7949dbe4" class="ne-image">

MP 给我们提供了很多 json 处理器，springboot 默认集成的是 jackson，因此我们这里选择 `JacksonTypeHandler`会比较方便，不需要引入额外的 json 处理库。

---

## 使用 json 处理器

### 第一步：编写 json 对应的实体

```java

package com.jkweilai.mp.entity;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

@Data
@NoArgsConstructor
// 生成静态方法of，便于对象的创建。
@AllArgsConstructor(staticName = "of")
public class Owner {
    private String id;
    private String name;
}

```

### 第二步：在字段上使用 `@TableField`注解

在 Car 实体类上添加字段，并使用 `@TableField`注解进行标注，****指定 json 类型处理器****，另外在实体类上****开启自动结果映射****：

```java

@Data
// 需要开启自动结果映射
@TableName(value = "t_car", autoResultMap = true)
public class Car {
    @TableId(value = "id", type = IdType.AUTO)
    private Long id;
    private String carNum;
    private String brand;
    private BigDecimal guidePrice;
    private String produceTime;
    private String carType;
    private CarStatus status;
    // 添加json类型处理器
    @TableField(typeHandler = JacksonTypeHandler.class)
    private Owner owner;
}

```

记得 VO 类也要修改一下：`CarVO`类上添加一个字段

```java

@Schema(description = "车主信息")
private Owner owner;

```

### 第三步：测试查询

直接通过 Swagger UI 测试之前的接口：通过 id 查询汽车信息的接口。

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1765425952884-d4409c4b-a80c-429b-bcdf-93fe25f00764.png" width="338.4" title="" crop="0,0,1,1" id="u90f78992" class="ne-image">

### 第四步：测试插入

编写单元测试，插入数据，看看能不能正常插入 json 字符串：

```java

@Resource
private CarService carService;

@Test
public void testSave(){
    Car car = new Car();
    car.setCarNum("津A90909");
    car.setCarType("新能源");
    car.setBrand("BYD666");
    car.setProduceTime("2025-10-11");
    car.setStatus(CarStatus.FOR_SALE);
    car.setGuidePrice(BigDecimal.valueOf(20));
    // 车辆关联车主
    car.setOwner(Owner.of("890989098989876787", "达摩"));
    carService.save(car);
}

```

测试结果：

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1765426213984-aa09478f-f210-49fe-b757-c01f65d932b9.png" width="948" title="" crop="0,0,1,1" id="u53ee3ce8" class="ne-image">
