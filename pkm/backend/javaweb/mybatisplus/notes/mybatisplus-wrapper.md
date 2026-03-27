# MyBatis-Plus条件构造器

---

## 初识条件构造器

mp默认生成的CRUD的SQL语句，都是基于主键id的，例如：deleteById、updateById、selectById等。

在实际的开发中 SQL 的 where 条件应该是多样化的，如何构造一个复杂条件的 SQL 呢？mp 提供了条件构造器`Wrapper`来解决这个问题。

来自官方的一段描述：

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1744286634938-7d863454-cc00-4452-80ab-fa2320e779bf.png" width="924" title="" crop="0,0,1,1" id="u825e8b6e" class="ne-image" style="font-size: 16px">

以下是条件构造器`Wrapper`的继承结构图：

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1744287684456-1fc1448b-0e13-46f7-b4a4-0789213abc40.png" width="863" title="" crop="0,0,1,1" id="u13d61d24" class="ne-image" style="font-size: 16px">

---

## QueryWrapper的使用

****注意：MP 中提供的****`****QueryWrapper****`****与****`****LambdaQueryWrapper****`****适合于单表查询，如果多表连接查询建议大家使用 MyBatis 原生配置文件。****

### 案例1

查询出汽车品牌中带有 '宝' 的，厂商指导价大于20万的，要求查询 id、car_num、brand、guide_price 字段。

如果写SQL语句应该这样写：

```sql

select id,car_num,brand,guide_price from t_car where brand like '%宝%' and guide_price > 20;

```

如果用条件构造器的话，Java代码应该怎么写呢？

```java

@Test
void testQueryWrapper(){
    // 1. 创建条件构造器
    QueryWrapper<Car> wrapper = new QueryWrapper<>();
    // 2. 链式追加条件
    wrapper.select("id","car_num","brand","guide_price")
            .like("brand", "宝")
            .gt("guide_price", 20.0);
    // 3. 查询
    List<Car> cars = carMapper.selectList(wrapper);
    cars.forEach(System.out::println);
}

```

另外，以上编写的代码中 `"id","car_num","brand","guide_price"` 等都属于硬编码，如果表的列名修改了，Java代码也是需要修改的。另外双引号里的字符串即使写错了，编译器也不会报错，因此mp给出了`Lambda`方式来解决这个问题，例如`LambdaQueryWrapper`，代码如下：

```java

@Test
void testLambdaQueryWrapper(){
    // 1.创建条件构造器
    LambdaQueryWrapper<Car> wrapper = new LambdaQueryWrapper<>();
    // 2.链式追加条件
    wrapper.select(Car::getId,Car::getCarNum,Car::getBrand,Car::getGuidePrice)
            .like(Car::getBrand, "宝")
            .gt(Car::getGuidePrice, 20.0);
    // 3.查询
    List<Car> cars = carMapper.selectList(wrapper);
    cars.forEach(System.out::println);
}

```

`**Car::getId**`**是如何转换成 **`**"id"**`**的呢？感兴趣的同学可以研究一下以下代码：**

```java

import java.lang.invoke.SerializedLambda;
import java.lang.reflect.Method;

// 普通类
class User {
    private Long id;

    public Long getId() {
        return id;
    }
}

// 函数式接口
interface MyFunc extends java.io.Serializable {
    Object apply(User user);
}

// 测试程序（以下代码是Lambda表达式相关的反射机制代码）
public class Test {
    public static void main(String[] args) throws Exception {
        // 方法引用
        MyFunc func = User::getId;
        // 获取SerializedLambda
        Method m = func.getClass().getDeclaredMethod("writeReplace");
        m.setAccessible(true);
        SerializedLambda lambda = (SerializedLambda) m.invoke(func);
        // 提取字段名
        String methodName = lambda.getImplMethodName(); // "getId"
        String fieldName = methodName.substring(3, 4).toLowerCase() + methodName.substring(4); // "id"
        System.out.println("字段名: " + fieldName);
    }
}

```

### 案例2

将`宝马535`的厂商指导价修改为`10.0`万。

对应的SQL语句写法：

```sql

update t_car set guide_price = 10.0 where brand = '宝马535';

```

如果用条件构造器的话Java代码该怎么写呢？

```java

@Test
void testQueryWrapper2(){
    // 1.准备数据
    Car car = new Car();
    car.setGuidePrice(10.0);
    // 2.创建条件构造器，并链式追加条件
    QueryWrapper<Car> wrapper = new QueryWrapper<Car>()
            .eq("brand", "宝马535");
    // 3.更新
    carMapper.update(car, wrapper);
}

```

使用`LambdaQueryWrapper`改造：

```java

@Test
void testLambdaQueryWrapper2(){
    // 1.准备数据
    Car car = new Car();
    car.setGuidePrice(10.0);
    // 2.创建条件构造器，并链式追加条件
    LambdaQueryWrapper<Car> wrapper = new LambdaQueryWrapper<Car>()
            .eq(Car::getBrand, "宝马535");
    // 3.更新
    carMapper.update(car, wrapper);
}

```

---

## UpdateWrapper的使用

当`update`语句中`set`后面的语句比较特殊的话，就需要使用`UpdateWrapper`了。

例如：要求所有的`宝马535`涨价`5`万。

SQL语句应该这样写：

```sql

update t_car set guide_price = guide_price + 5 where brand = '宝马535';

```

这个时候就需要使用`UpdateWrapper`了，Java代码如下：

```java

@Test
void testUpdateWrapper(){
    // 创建条件构造器
    UpdateWrapper<Car> wrapper = new UpdateWrapper<>();
    // 设置set语句并链式追加条件
    wrapper.setSql("guide_price = guide_price + 5")
            .eq("brand", "宝马535");
    // 更新
    carMapper.update(wrapper);
}

```

如果使用`LambdaUpdateWrapper`，代码应该这样写：

```java

@Test
void testLambdaUpdateWrapper(){
    // 创建条件构造器
    LambdaUpdateWrapper<Car> wrapper = new LambdaUpdateWrapper<>();
    // 设置set语句并链式追加条件
    wrapper.setSql("guide_price = guide_price + 5")
            .eq(Car::getBrand, "宝马535");
    // 更新
    carMapper.update(wrapper);
}

```

---

## 条件构造器用法总结

条件构造器用法：

1. `QueryWrapper`和`LambdaQueryWrapper`用来构建`select`、`delete`、`update`的`where`条件。
2. `UpdateWrapper`和`LambdaUpdateWrapper`一般只有在`set语句`比较特殊的情况下才会使用。
3. 尽量使用`LambdaQueryWrapper`和`LambdaUpdateWrapper`，避免硬编码。
