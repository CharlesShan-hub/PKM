# 枚举处理器

---

## 使用枚举增强可读性

假设汽车有一个状态属性，状态包括：在售(1)、已售(2)、维修中(3)、报废(4)，在数据库表中对应的字段为`status`，数据库中字段的类型为`int`，如下：

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1744439091743-ff706e19-8360-4a35-849b-8d7000ee6454.png" width="493" title="" crop="0,0,1,1" id="ud3624dde" class="ne-image" style="font-size: 16px">

这时候，在po上也应该添加一个新的属性，如下：

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1744439193534-8417f125-a0b0-4ff1-8b6c-a49bcf4cc037.png" width="495" title="" crop="0,0,1,1" id="u3a8ebd8d" class="ne-image" style="font-size: 16px">

`status`定义为Integer类型不是特别好的设计，因为这样出现在程序中的是数字`1,2,3,4`，**可读性较差**。

有的时候**对于po的属性**来说定义为枚举类型比数字类型来说可读性更好一些，例如定义这样一个枚举类型来表示汽车状态：

```java

package com.jkweilai.carmgtsys.enums;

import lombok.Getter;

@Getter
public enum CarStatus {
    
    FOR_SALE(1, "在售"),
    SOLD(2, "已售"),
    IN_MAIN(3, "维修中"),
    SCRAP(4, "报废");
    
    private int value;
    private String desc;

    CarStatus(int value, String desc) {
        this.value = value;
        this.desc = desc;
    }
}

```

po中的属性使用枚举类型：

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1744439732134-c6e12dac-1274-4027-b48c-243b7a65708c.png" width="538" title="" crop="0,0,1,1" id="uc25e002e" class="ne-image" style="font-size: 16px">

这样的话，我们在编写java程序时，可读性会很好。但是新的问题出现了：数据库中存储的是`1,2,3,4`这样的数字，Java程序中是枚举类型的值，它们之间怎么进行映射转换呢？

不用担心，MyBatis-Plus已经帮我们解决了，它提供了这样一个类：`MybatisEnumTypeHandler`，这个类可以帮助我们完成`Java枚举类型的值`与`数据库中的int值`之间的转换，我们只需要在程序中做以下两步：

第一步：使用`@EnumValue`标注在Java枚举类型中哪个属性的值存储到数据库中。

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1744440422424-e65aa05d-5b93-4f99-8c0f-5ea821995b38.png" width="408" title="" crop="0,0,1,1" id="ud99faf99" class="ne-image" style="font-size: 16px">

第二步：在`application.yml`文件中指定我们使用的是哪个转换器，我们使用MP提供的`MybatisEnumTypeHandler`即可。

```yaml

mybatis-plus:
  configuration:
    default-enum-type-handler: com.baomidou.mybatisplus.core.handlers.MybatisEnumTypeHandler

```

---

## 测试保存功能

`CarDTO`代码添加属性，如下：

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1744441847827-44668c5a-d5cd-4738-96f8-67fea673ac2d.png" width="673" title="" crop="0,0,1,1" id="u7c2541e3" class="ne-image" style="font-size: 16px">

其他位置不需要修改，直接测试我们之前编写的保存接口：

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1744442036230-36af4263-bbdb-48b1-8922-daf7c4fa9784.png" width="446" title="" crop="0,0,1,1" id="ud5cd8407" class="ne-image" style="font-size: 16px">

我们来看一下数据库表中插入的状态值是不是`2`：

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1744442152960-767bb71f-0497-45db-8ba3-b705a298e57d.png" width="735" title="" crop="0,0,1,1" id="ubfe9e741" class="ne-image" style="font-size: 16px">

---

## 测试查询功能

需求：查询所有 **在售 **的车辆信息。

第一步：CarVO中添加属性

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1744442862124-6a655706-6b27-491d-a2fc-9037a77fb8c2.png" width="585" title="" crop="0,0,1,1" id="u0d57bea8" class="ne-image" style="font-size: 16px">

第二步：在CarController中添加方法

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1744442894426-b0d92395-50ca-49f3-953e-259bc5eaf78c.png" width="721" title="" crop="0,0,1,1" id="ub462265f" class="ne-image" style="font-size: 16px">

第三步：编写CarServiceImpl类中的query

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1744442949283-577f344c-faac-4f5c-8da9-7207bef3dfe2.png" width="810" title="" crop="0,0,1,1" id="u71dc1077" class="ne-image" style="font-size: 16px">

测试结果：

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1744443075911-9a80edfd-bc54-42ef-8000-2a3c055118b9.png" width="466" title="" crop="0,0,1,1" id="u840d2062" class="ne-image" style="font-size: 16px">

如果展示的时候，希望展示结果是`在售`，而不是`FOR_SALE`，可以使用`@JsonValue`注解标注枚举类型中`desc`属性：

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1744443210615-9a3ec3cf-754e-4d93-be07-6e91c045ba23.png" width="500" title="" crop="0,0,1,1" id="u5098a384" class="ne-image" style="font-size: 16px">

这个注解不是mp的。属于`Jackson库`的注解。

再来看结果：

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1744443329927-170a622c-392f-4bf7-b012-7b670a481277.png" width="414" title="" crop="0,0,1,1" id="uc24bfb0b" class="ne-image" style="font-size: 16px">
