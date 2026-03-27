# MP 分页插件的使用

**MyBatis-Plus的分页插件能自动将Page对象参数转换为数据库分页SQL，无需手写LIMIT语句。**

---

## **第一步：引入额外的依赖**

使用分页插件需要引入以下的依赖。

```xml

<dependency>
  <groupId>com.baomidou</groupId>
  <artifactId>mybatis-plus-jsqlparser</artifactId>
  <version>3.5.11</version>
</dependency>

```

---

## 第二步：通过配置类添加插件

要使用 MP 提供的分页插件，第一步先配置插件，编写以下的配置类：

```java

package com.jkweilai.mp.config;

import com.baomidou.mybatisplus.annotation.DbType;
import com.baomidou.mybatisplus.extension.plugins.MybatisPlusInterceptor;
import com.baomidou.mybatisplus.extension.plugins.inner.PaginationInnerInterceptor;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

@Configuration
public class MyBatisConfig {
    
    // MyBatis-Plus 的插件机制底层基于 MyBatis 的拦截器（Interceptor） 实现
    @Bean
    public MybatisPlusInterceptor mybatisPlusInterceptor() {
        // 创建 MybatisPlusInterceptor 拦截器链，用于集中管理 Mybatis-Plus 的各种功能拦截器
        MybatisPlusInterceptor interceptor = new MybatisPlusInterceptor();

        // 创建分页拦截器实例，指定数据库类型为 MySQL
        // DbType.MYSQL 会自动生成适合 MySQL 的分页 SQL（使用 LIMIT 语句）
        PaginationInnerInterceptor pageInterceptor = new PaginationInnerInterceptor(DbType.MYSQL);

        // 设置单次分页查询的最大记录数限制，防止恶意大数量查询（如 pageSize=10000）
        // 当 pageSize 参数值超过 500 时，会自动调整为 500
        // 这可以有效防止内存溢出和数据库性能问题
        pageInterceptor.setMaxLimit(500L);

        // 将分页拦截器添加到拦截器链中
        // 拦截器会按照添加顺序执行，分页拦截器通常放在最后
        interceptor.addInnerInterceptor(pageInterceptor);

        // 返回配置好的拦截器实例，Spring 会将其注册到 Mybatis 的插件链中
        return interceptor;
    }
}

```

---

## 编写分页查询的代码

```java

@Test
void testPage(){
    // 创建分页对象（指定pageNo和pageSize）
    int pageNo = 1;
    int pageSize = 2;
    Page<Car> page = Page.of(pageNo, pageSize);
    // 指定排序规则，以下表示：先按照guide_price升序，如果guide_price相同则按照id降序
    page.addOrder(OrderItem.asc("guide_price"));
    page.addOrder(OrderItem.desc("id"));
    // 指定查询条件，执行查询
    //QueryWrapper<Car> queryWrapper = new QueryWrapper<>();
    //carService.page(page, queryWrapper);
    carService.page(page);
    // 获取总记录条数
    long total = page.getTotal();
    System.out.println("总记录条数：" + total);
    // 获取总页数
    long pages = page.getPages();
    System.out.println("总页数：" + pages);
    // 获取数据
    List<Car> records = page.getRecords();
    records.forEach(System.out::println);
}

```

到此：MP 的基础使用就结束了。
