# 开启mapper接口的日志

logging:
  level:
    com.jkweilai.demo.mapper: DEBUG

```

第四步：编写Mapper接口直接继承`BaseMapper`

```java

package com.jkweilai.mp.mapper;

import com.baomidou.mybatisplus.core.mapper.BaseMapper;
import com.jkweilai.mp.model.Car;

public interface CarMapper extends BaseMapper<Car> {
}

```

`****BaseMapper****`****已经将CRUD相关的方法全部实现了，该类中有大量的 insert、delete、update、select 等方法。****

第五步：Spring Boot主入口程序添加 Mapper扫描

```java

package com.jkweilai.mp;

import org.mybatis.spring.annotation.MapperScan;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@MapperScan(basePackages = {"com.jkweilai.mp.mapper"})
@SpringBootApplication
public class Mp01Application {

    public static void main(String[] args) {
        SpringApplication.run(Mp01Application.class, args);
    }

}

```

第六步：编写测试程序

```java

package com.jkweilai.mp;

import com.jkweilai.mp.mapper.CarMapper;
import com.jkweilai.mp.model.Car;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;

import java.util.List;

@SpringBootTest
class Mp01ApplicationTests {

    @Autowired
    private CarMapper carMapper;

    @Test
    void testInsert(){
        Car car = new Car();
        car.setCarNum("999");
        car.setBrand("小米su7");
        car.setGuidePrice(30.00);
        car.setProduceTime("2025-10-11");
        car.setCarType("电车");
        int count = carMapper.insert(car);
        System.out.println("插入" + count + "条记录");
    }

    @Test
    void testDeleteById(){
        int count = carMapper.deleteById(7L);
        System.out.println("删除了" + count + "条记录");
    }

    @Test
    void testUpdateById(){
        Car car = new Car();
        car.setId(8L);
        car.setBrand("小米utl");
        int count = carMapper.updateById(car);
        System.out.println("更新了" + count + "条记录");
    }

    @Test
    void testSelectById(){
        Car car = carMapper.selectById(8L);
        System.out.println(car);
    }

    @Test
    void testSelectAll(){
        List<Car> cars = carMapper.selectList(null);
        cars.forEach(System.out::println);
    }

}

```
