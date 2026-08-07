# Part 1：快速上手

> 目标：5 分钟跑通 Gson 基本流程，知道怎么用，不深入原理。
> 
> 🏰 背景故事：下面所有例子都发生在 **"查尔斯动物园"** 里：
>
> - **动物（Animal）**：动物园的居民 —— 后续所有例子都会用到它
> - **动物园（Zoo）**：管理动物的场所 —— 演示 `List`、`Map` 的集合场景
> - **员工（Employee）**：动物园的员工 —— 演示字段重命名
> - **经理（Manager）**：动物园的管理层 —— 演示 `transient`
> - **老板（Boss）**：动物园的老板和会计 —— 演示 `Expose`
> - **游客（Tourist）**：来参观动物园的人 —— 演示日期格式化
>
> 每个例子之间有关联，建议按顺序阅读。

---

## 引入依赖

**Maven**：

```xml
<dependency>
    <groupId>com.google.code.gson</groupId>
    <artifactId>gson</artifactId>
    <version>2.10.1</version>
</dependency>
```

**Gradle**：

```groovy
implementation 'com.google.code.gson:gson:2.10.1'
```

---

## 场景：对象

> 🐯 **背景**：1938年的一个春日，查尔斯动物园迎来了一位新居民 —— 一只名叫**汤姆**的猫。兽医打开登记簿，准备给它建档。此时档案还很简单，只有两个字段：名字和出生年份。

💡 Gson 不强制要求 getter/setter，直接通过反射读取字段值。但**必须有默认构造器**（无参构造），否则反序列化会失败。

```java
package top.charles;  
  
import lombok.AllArgsConstructor;  
import lombok.NoArgsConstructor;  
import lombok.ToString;  
  
// @Data // getter/setter 可省略，Gson 通过反射直接访问字段  
@AllArgsConstructor  
@NoArgsConstructor // 必须有默认构造器（无参构造）  
@ToString  
public class Animal {  
    private String name;  
    private int birthYear;  
}
```

```java
package top.charles;  
  
import com.google.gson.Gson;  
import org.junit.Test;  
  
public class AnimalTest {  
    Gson gson = new Gson();  
    @Test  
    public void test(){  
        // 对象 → JSON        
        Animal a1 = new Animal("Tom", 1938);  
        String json = gson.toJson(a1);  
        System.out.println(json); 
        // {"name":"Tom","birthYear":1938}
  
        // JSON → 对象  
        Animal a2 = gson.fromJson(json, Animal.class);  
        System.out.println(a2); 
        // Animal(name=Tom, birthYear=1938)
    }  
}
```

## 场景：美观的输出

> 🖨️ **背景**：兽医想打印一份漂亮的动物清单贴在墙上。但 Gson 默认输出的 JSON 是一整行，密密麻麻看不清。这时候就需要漂亮的格式化输出。
> 📌 **说明**：为了让笔记里的输出示例更清晰，**本文档后续统一用 `prettyGson` 进行序列化演示**（即 `GsonBuilder().setPrettyPrinting().create()`）。但实际开发中，默认用 `Gson gson = new Gson()` 即可——需要格式化输出时再临时用 `prettyGson`。

💡 Gson 默认输出是紧凑的（一行），用 `GsonBuilder().setPrettyPrinting()` 可以让输出有缩进、换行，可读性大大提升。
💡 注意：`setPrettyPrinting()` 只影响**序列化**（`toJson`）的输出格式，不影响**反序列化**（`fromJson`）的行为。`fromJson` 无论 JSON 是紧凑还是美观的，都能正常解析。

```java
package top.charles;  
  
import com.google.gson.Gson;  
import com.google.gson.GsonBuilder;  
import org.junit.Test;  
  
public class AnimalTest {  
    Gson gson = new Gson();  
    Gson prettyGson = new GsonBuilder()  
            .setPrettyPrinting()  // 这里！ 
            .create();  

    @Test  
    public void testPrettyPrint() {  
        Animal a1 = new Animal("Tom", 1938);  
        Animal a2 = new Animal("Jerry", 1940);  
        List<Animal> list = Arrays.asList(a1, a2);  
  
        // 默认：紧凑输出  
        String compactJson = gson.toJson(list);  
        System.out.println(compactJson);  
        // [{"name":"Tom","birthYear":1938},{"name":"Jerry","birthYear":1940}]  
  
        // 美化：格式化输出  
        String prettyJson = prettyGson.toJson(list);  
        System.out.println(prettyJson);  
        // [  
        //   {  
        //     "name": "Tom",  
        //     "birthYear": 1938  
        //   },  
        //   {  
        //     "name": "Jerry",  
        //     "birthYear": 1940  
        //   }  
        // ]  
    }  
}
```

## 场景：集合与列表

> 🐱🐭 **背景**：1940年，汤姆在动物园里认识了新朋友 —— 一只叫**杰瑞**的小老鼠。两年过去了，动物园的居民越来越多，兽医不能再一个个手动建档了，得用**列表**和**字典**来批量管理这些动物档案。

💡 Gson 反序列化需要指定泛型，否则会退回到 `LinkedTreeMap`。这里记住：**凡是泛型类型（List、Map、自定义泛型类），必须用 `TypeToken` 包装**。

 `List`类如何进行转换：
 
```java
@Test  
public void testList(){  
    // List -> JSON  
    List<Animal> list = Arrays.asList(  
            new Animal("Tom",1938),  
            new Animal("Jerry", 1940)  
    );    
    String json = prettyGson.toJson(list);  
    System.out.println(json);  
    // [  
    //   {  
    //     "name": "Tom",  
    //     "birthYear": 1938  
    //   },  
    //   {  
    //     "name": "Jerry",  
    //     "birthYear": 1940  
    //   }  
    // ]  
  
    // JSON -> List    
    List<Animal> list2 = gson.fromJson(json,  
        new TypeToken<List<Animal>>(){}.getType()  
    );    
    System.out.println(list2);  
    // [Animal(name=Tom, birthYear=1938), Animal(name=Jerry, birthYear=1940)]  
}
```

`Map`类如何进行转换：

```java
@Test  
public void testMap(){  
    // Map -> JSON  
    Map<String, Animal> zoo = new HashMap<>();  
    zoo.put("cat", new Animal("Tom", 1938));  
    zoo.put("mouse", new Animal("Jerry", 1940));  
    String json = prettyGson.toJson(zoo);  
    System.out.println(json);  
    // {  
    //   "mouse": {  
    //     "name": "Jerry",  
    //     "birthYear": 1940  
    //   },  
    //   "cat": {  
    //     "name": "Tom",  
    //     "birthYear": 1938  
    //   }  
    // }  
  
    // JSON -> Map    
    Map<String, Animal> zoo2 = gson.fromJson(json,   
        new TypeToken<Map<String, Animal>>(){}.getType()  
    );  
    System.out.println(zoo2);  
    // {mouse=Animal(name=Jerry, birthYear=1940), cat=Animal(name=Tom, birthYear=1938)}  
}
```

类型擦除错误示例：

```java
@Test  
public void testListError() {
    String json = "[\n" +  
            "  {\n" +  
            "    \"name\": \"Tom\",\n" +  
            "    \"birthYear\": 1938\n" +  
            "  },\n" +  
            "  {\n" +  
            "    \"name\": \"Jerry\",\n" +  
            "    \"birthYear\": 1940\n" +  
            "  }\n" +  
            "]";  
  
    // ❌ 错误写法：直接传 List.class  
    // List<Animal> list = gson.fromJson(json, List.class);  
    List list = gson.fromJson(json, List.class);  
  
    System.out.println(list.getClass());  
    // class java.util.ArrayList  
  
    System.out.println(list.get(0).getClass());  
    // class com.google.gson.internal.LinkedTreeMap  
    // ↑ 每个元素都是 LinkedTreeMap，不是 Animal！  
  
    // 如果尝试强转或当 Animal 用：  
    // Animal a1 = list.get(0);  // ❌ ClassCastException
    // a1.getName();             // ❌ 编译不报错，运行时报  
}
```

对象中的字段包装好`List`或者`Map`可以简化反序列化的复杂度：

```java
package top.charles;  
  
import lombok.AllArgsConstructor;  
import lombok.NoArgsConstructor;  
import lombok.ToString;  
  
import java.util.List;  
  
public class Zoo {  
    private List<Animal> animals;  
}
```

```java
package top.charles;  
  
import com.google.gson.Gson;  
import com.google.gson.GsonBuilder;  
import org.junit.Test;  
  
import java.util.Arrays;  
  
public class ZooTest {  
    Gson gson = new Gson();  
    Gson prettyGson = new GsonBuilder()  
            .setPrettyPrinting()  
            .create();  
  
    @Test  
    public void test() {  
        // 对象 → JSON  
        Zoo z1 = new Zoo(Arrays.asList(  
            new Animal("Tom", 1940),  
            new Animal("Jerry", 1940))  
        );  
        String json = prettyGson.toJson(z1);  
        System.out.println(json);  
        // {  
        //   "animals": [  
        //     {  
        //       "name": "Tom",  
        //       "birthYear": 1940  
        //     },  
        //     {  
        //       "name": "Jerry",  
        //       "birthYear": 1940  
        //     }  
        //   ]  
        // }  
  
        // JSON → 对象  
        Zoo z2 = gson.fromJson(json, Zoo.class);  
        System.out.println(z2);  
        // Zoo(animals=[Animal(name=Tom, birthYear=1940), Animal(name=Jerry, birthYear=1940)])  
    }  
}
```

## 场景：null字段

> 🐯 **背景**：动物园录入动物信息时，有些动物没有名字（比如刚出生的），`name` 可能是 `null`。我们需要决定：`null` 要不要写进 JSON？

💡 Gson 序列化某字段为`null`，不会加入到json中，反序列化遇到json没有的字段默认填充`null`；如果json需要指定`null`，需要用`serializeNulls()`。

```java
Gson gson = new Gson();
Gson gsonWithNull = new GsonBuilder()
        .serializeNulls()   // 多了这一行
        .setPrettyPrinting()
        .create();

@Test
public void testNull(){
    Animal a1 = new Animal(null, 1940);

    // 默认：null 字段不输出
    String json1 = gson.toJson(a1);
    System.out.println(json1);
    // {"birthYear":1940}
    // ↑ name 字段消失了

    // 开启 serializeNulls：null 字段保留
    String json2 = gsonWithNull.toJson(a1);
    System.out.println(json2);
    // {
    //   "name": null,
    //   "birthYear": 1940
    // }
    // ↑ null 字段保留了

    // 反序列化：无论哪种 JSON，都能正确填充 null
    Animal a2 = gson.fromJson(json1, Animal.class);
    System.out.println(a2); // Animal(name=null, birthYear=1940)

    Animal a3 = gson.fromJson(json2, Animal.class);
    System.out.println(a3); // Animal(name=null, birthYear=1940)
}
```

## 场景：日期格式

> 🧑 **背景**：1942年，查尔斯动物园名声渐起，不少游客慕名而来。售票处需要登记每位游客的姓名和**生日** —— 生日是完整的日期时间。

💡 Gson 默认日期格式是 `"Jun 8, 2021, 10:00:00 AM"`，不是我们常用的 `yyyy-MM-dd HH:mm:ss`。需要手动指定。

```java
package top.charles;  
  
import lombok.AllArgsConstructor;  
import lombok.NoArgsConstructor;  
import lombok.ToString;  
  
import java.util.Date;  
  
@AllArgsConstructor  
@NoArgsConstructor  
@ToString  
public class Tourist {  
    private String name;  
    private Date birthday;  
}
```

```java
package top.charles;  
  
import com.google.gson.Gson;  
import com.google.gson.GsonBuilder;  
import org.junit.Test;  
  
import java.util.Date;  
  
public class TouristTest {  
  
    @Test  
    public void testDefault() {  
        Gson prettyGson = new GsonBuilder()  
                .setPrettyPrinting()  
                .create();  
    
        Tourist user = new Tourist("Dimo", new Date());  
        String json = prettyGson.toJson(user);  
    
        System.out.println(json);  
        // {  
        //   "name": "Dimo",  
        //   "birthday": "Aug 6, 2026, 2:03:41 PM"  
        // }  
        // 默认格式，不是我们常用的  
    }
  
    @Test  
    public void testCustomFormat() {  
        Gson prettyGson = new GsonBuilder()  
                .setDateFormat("yyyy-MM-dd HH:mm:ss")  
                .setPrettyPrinting()  
                .create();  
    
        Tourist user = new Tourist("Guardian Dog", new Date());  
        String json = prettyGson.toJson(user);  
    
        System.out.println(json);  
        // {  
        //   "name": "Guardian Dog",  
        //   "birthday": "2026-08-06 14:03:41"  
        // }  
    }  
    
    @Test  
    public void testDeserialize() {  
        Gson gson = new GsonBuilder()  
                .setDateFormat("yyyy-MM-dd HH:mm:ss")  
                .create();  
    
        String json = "{\"name\":\"Elsa\",\"age\":30,\"birthday\":\"2025-03-21 14:30:00\"}";  
    
        Tourist user = gson.fromJson(json, Tourist.class);  
        System.out.println(user);  
        // Tourist(name=Elsa, birthday=Fri Mar 21 14:30:00 CST 2025)  
    }
}
```

## 场景：字段重命名

> 🏢 **背景**：1943年，动物园规模扩大，查尔斯先生招了一批新员工。人事系统是外国的，字段名都要求用英文缩写 —— "员工姓名"叫 `ename`，"工资"叫 `sal`。但 Java 代码里我们希望用可读性好的 `name` 和 `salary`，这就需要 Gson 的 `@SerializedName` 来做个**翻译**。

💡 `@SerializedName` 指定 JSON 里的字段名。
💡 `alternate` 只在**反序列化**时生效，序列化时始终用 `value` 指定的名字。

```java
package top.charles;  
  
import com.google.gson.annotations.SerializedName;  
import lombok.AllArgsConstructor;  
import lombok.NoArgsConstructor;  
import lombok.ToString;  
  
@AllArgsConstructor  
@NoArgsConstructor  
@ToString  
public class Employee {  
    @SerializedName(
        value = "ename", 
        alternate = {"employee_name"}
    )  
    private String name;  
    
    @SerializedName("sal")
    private double salary;
}
```

```java
package top.charles;  
  
import com.google.gson.Gson;  
import com.google.gson.GsonBuilder;  
import org.junit.Test;  
  
public class EmployeeTest {  
  
    Gson gson = new Gson();  
    Gson prettyGson = new GsonBuilder()  
            .setPrettyPrinting()  
            .create();  
  
    @Test  
    public void testSerialize() {  
        Employee employee = new Employee("Jack", 10000.5);  
        String json = prettyGson.toJson(employee);  
  
        System.out.println(json);  
        // {  
        //   "ename": "Jack",  
        //   "sal": 10000.5  
        // }  
        // ↑ name 变成 ename，salary 变成 sal    
    }  
  
    @Test  
    public void testDeserializeWithAlternate() {  
        String json = "{\"employee_name\":\"Tom\",\"sal\":8000.5}";  
  
        Employee employee = gson.fromJson(json, Employee.class);  
        System.out.println(employee);  
        // Employee(name=Tom, salary=8000.5)  
    }  
}
```

## 场景：字段过滤

> 🏢 **背景**：1943年，动物园规模扩大，查尔斯先生雇了一位**经理**来管理员工。经理要算手下所有员工的工资开销，但这个"总开销"是内部数据，不想让外部系统看到。

使用了`transient`的字段，不参加序列化：

```java
package top.charles;  
  
import lombok.AllArgsConstructor;  
import lombok.NoArgsConstructor;  
import lombok.ToString;  
  
import java.util.List;  
  
@AllArgsConstructor  
@NoArgsConstructor  
@ToString  
public class Manager extends Employee {  
  
    private List<Employee> employees;  
  
    // transient：部门总开销，内部计算，不序列化  
    private transient double totalExpense;  
  
    public Manager(String name, double salary, List<Employee> employees) {  
        super(name, salary);  
        this.employees = employees;  
        this.totalExpense = initTotalExpense();  
    }  
    private double initTotalExpense() {  
        double sum = salary;  
        for (Employee employee : employees) {  
            sum += employee.salary;  
        }        
        return sum;  
    }  
    public double getTotalExpense() {  
        totalExpense = initTotalExpense();  
        return totalExpense;  
    }
}
```

```java
package top.charles;  
  
import com.google.gson.Gson;  
import com.google.gson.GsonBuilder;  
import org.junit.Test;  
  
import java.util.Arrays;  
  
public class ManagerTest {  
  
    Gson gson = new Gson();  
    Gson prettyGson = new GsonBuilder()  
            .setPrettyPrinting()  
            .create();  
  
    @Test  
    public void testManager() {  
        // 创建经理：自己工资 10000，手下 张三 5000、李四 6000   
        Manager manager = new Manager("张经理", 10000.0, Arrays.asList(  
                new Employee("张三", 5000.0),  
                new Employee("李四", 6000.0)  
        ));        
        System.out.println("构造时 totalExpense 自动计算: "+manager);  
        // Manager(employees=[Employee(name=张三, salary=5000.0), Employee(name=李四, salary=6000.0)], totalExpense=21000.0)  
        // 可以看到已经有了totalExpense
  
        // 序列化：totalExpense 不输出（transient）  
        String json = prettyGson.toJson(manager);  
        System.out.println("序列化: " + json);  
        // {  
        //   "employees": [  
        //     {  
        //       "ename": "张三",  
        //       "sal": 5000.0  
        //     },  
        //     {  
        //       "ename": "李四",  
        //       "sal": 6000.0  
        //     }  
        //   ],  
        //   "ename": "张经理",  
        //   "sal": 10000.0  
        // }  
        // ↑ totalExpense 不输出，因为它是 transient
  
        // 反序列化：totalExpense 恢复默认 0.0        
        Manager manager2 = gson.fromJson(json, Manager.class);  
        System.out.println("反序列化后 totalExpense: " + manager2);  
        // 反序列化后 totalExpense: Manager(employees=[Employee(name=张三, salary=5000.0), Employee(name=李四, salary=6000.0)], totalExpense=21000.0)  
        // ↑ 走的是 getter，重新算了  
    }  
}
```

> 🏢 **背景**：1943年，动物园生意越来越火，查尔斯先生（老板）请了一位**会计**来帮忙算账。老板要把自己的账本发给会计，会计填好花费后再发回来，老板自己算利润 —— 因为只有老板才知道自己到底有多少钱。
>
> 这中间就涉及到**双向控制**：
>
> - **总额（total）**：老板发给会计，会计也知道总数，双方都参与
> - **花费（cost）**：会计填写的，从 JSON 读进来；老板不会把自己的花费发给别人看，所以不序列化出去
> - **利润（profit）**：老板自己算的（总额 - 花费），只有老板知道；会计不需要知道，所以不从 JSON 读
>
> 流程：
> 1. 老板序列化 `{total}` 发给会计（cost 不输出，profit 也没有）
> 2. 会计填好花费发回 `{total, cost}`
> 3. 老板反序列化后自己算出 `profit`

使用`Expose`精准控制序列化与反序列化的作用范围：

```java
package top.charles;  
  
import com.google.gson.annotations.Expose;  
import lombok.AllArgsConstructor;  
import lombok.NoArgsConstructor;  
import lombok.ToString;  
  
@AllArgsConstructor  
@NoArgsConstructor  
@ToString  
public class Boss {  
  
    // 总额：常量，序列化/反序列化都参与  
    @Expose  
    private double total;  
  
    // 花费：会计告诉的，从 JSON 读，不序列化出去  
    @Expose(serialize = false, deserialize = true)  
    private double cost;  
  
    // 利润：自己算的，序列化给外面看，不从 JSON 读  
    @Expose(serialize = true, deserialize = false)  
    private double profit;  
  
    public Boss(double total, double cost) {  
        this.total = total;  
        this.cost = cost;  
        this.profit = total - cost;  
    }  
    // 这个一定要写
    public double getProfit() {  
        this.profit = total - cost;  
        return profit;  
    }
}
```

```java
package top.charles;  
  
import com.google.gson.Gson;  
import com.google.gson.GsonBuilder;  
import org.junit.Test;  
  
public class BossTest {  
  
    Gson gson = new GsonBuilder()  
            .excludeFieldsWithoutExposeAnnotation()  
            .create();  
  
    @Test  
    public void testBoss() {  
        // 序列化：cost 不输出，profit 输出  
        Boss boss = new Boss(100000.0, 40000.0);  
        String json = gson.toJson(boss);  
        System.out.println(json);  
        // {"total":100000.0,"profit":60000.0}  
  
        // 会计传来花费  
        String fromAccountant = "{\"total\":100000.0,\"cost\":80000.0,\"profit\":99999.0}";  
  
        Boss boss2 = gson.fromJson(fromAccountant, Boss.class);  
        System.out.println(boss2);  
        // Boss(total=100000.0, cost=80000.0, profit=20000.0)  
    }  
}
```

## 场景：循环引用

> 🏢 **背景**：1944年，动物园规模扩大，查尔斯先生按**条块划分**管理 —— 张经理负责"动物管理"业务线，同时兼任"员工培训"的讲师；小李经理负责"员工培训"业务线，同时在"动物管理"担任顾问。**从行政级别讲，张经理是领导；但从业务线讲，小李是培训这块的负责人** —— 两人互相挂职，档案里互相包含对方 —— 形成**循环引用**。直接序列化会**栈溢出**！

```java
// 张经理：动物管理线负责人，兼任培训讲师
Manager zhang = new Manager("张经理", 10000.0, Arrays.asList(
    new Employee("张三", 5000.0),
    new Employee("李四", 6000.0)
));

// 小李经理：培训线负责人，兼任动物管理顾问
Manager li = new Manager("小李经理", 8000.0, Arrays.asList(
    new Employee("王五", 4000.0)
));

// 条块划分：互相挂职，往对方的员工列表里加
zhang.getEmployees().add(li);   // 张经理手下有小李（培训线）
li.getEmployees().add(zhang);   // 小李手下有张经理（动物管理线）

// ❌ 直接序列化
String json = gson.toJson(zhang);
// StackOverflowError：张经理 -> 小李 -> 张经理 -> 小李 ... 无限递归
```

这个问题其实没有满分的解决答案，下面是一些常见的思路

**1. @Expose 注解 + 排除未标记字段**
- 做法：在需要序列化的字段上加 `@Expose`，反向引用字段不加。构建 Gson 时调用 `excludeFieldsWithoutExposeAnnotation()`
- 本质：白名单机制，只序列化明确标记的字段
- 适用：能修改实体类，且希望明确控制哪些字段参与序列化

**2. transient 关键字**
- 做法：在反向引用字段上加 `transient`，如 `private transient Manager manager;`
- 本质：Java 原生机制，序列化时直接跳过该字段
- 局限：字段会完全从 JSON 中消失，反序列化时该字段为 null，且对子类、集合内元素中的同名字段也生效，粒度较粗

**3. ExclusionStrategy 动态排除**
- 做法：实现 `ExclusionStrategy` 接口，在 `shouldSkipField()` 中按字段名、字段类型、甚至注解动态判断是否跳过
- 本质：运行时策略模式，比 `transient` 灵活，比 `@Expose` 更动态（可根据上下文决定）
- 适用：不想改实体类，或排除规则需要动态变化

**4. 自定义 TypeAdapter / JsonSerializer**
- 做法：接管序列化全过程，用 `IdentityHashMap` 记录已访问对象，遇到重复引用时输出 `null`、ID 或自定义标记
- 本质：完全控制序列化逻辑，理论上可以实现"遇到已访问节点就停"
- 局限：实现复杂，反序列化更难，且输出非标准 JSON；Gson 本身并未内置此功能，需手写大量代码

**5. 换用支持循环引用的库**
- 做法：使用 FastJson（默认输出 `$ref`）或 Jackson（`@JsonIdentityInfo`）
- 本质：这些库内置了循环引用检测机制，通过引用 ID 或特殊标记保留对象关系
- 代价：输出的 JSON 不标准，跨语言/跨系统消费可能不兼容

6. **遇到已访问节点就中断**
* 这是最自然的想法，但 Gson 没这么做的原因：一旦中断，要么输出 `null`（数据丢失），要么输出特殊引用标记（JSON 不标准），两种结果都不符合 Gson 追求"标准 JSON 且完整表达数据"的设计目标。所以 Gson 的选择是：**不自动处理，由开发者按业务需要显式切断引用链**。

💡 精髓：JSON 是树，Java 是图。循环引用超出了 JSON 的表达范围，Gson 不提供魔法解法 —— 它引导开发者**主动设计序列化边界**：什么字段该出现、什么关系该切断。`transient`、`@Expose`、自定义序列化器，都是你在告诉 Gson"你的 JSON 长什么样"。

## 场景：大整数精度

> 💰 **背景**：1945年，动物园开放了募捐，一位富豪捐了一笔巨款。财务要用 `long` 来记录这笔捐款，但 Gson 序列化时默认把数字变成 `double`，**精度丢失**！

Gson 默认行为：

```java
@Test
public void testBigNumber() {
    long donation = 9007199254740993L;  // 超过 2^53
    String json = gson.toJson(donation);
    System.out.println(json);
    // 9007199254740992  ← 精度丢了！最后一位 3 变成了 2
}
```

为什么？因为 Gson 内部默认把数字当作 `double` 处理，而 `double` 只能精确表示 2^53 以内的整数。

**解决办法**：注册自定义 `TypeAdapter`：

```java
Gson gson = new GsonBuilder()
    .registerTypeAdapter(Long.class, new JsonSerializer<Long>() {
        @Override
        public JsonElement serialize(Long value, Type type, JsonSerializationContext context) {
            return new JsonPrimitive(value.toString());  // 转成字符串
        }
    })
    .create();
```

或者更简单：如果字段类型是 `long`/`Long`，Gson 其实会正确序列化。问题主要出在**反序列化时**：

```java
String json = "{\"donation\":9007199254740993}";
// 如果字段是 long，Gson 能正确处理
```

## 本章总结

> Gson 的设计哲学：**忠实还原 JSON，不做多余的事**。它不试图帮你抹平 Java 与 JSON 的差异，而是把差异**暴露**给你，让你自己决定怎么处理。
>
> 好在 Gson 提供了两把手术刀：
>
> - **建造者模式（`GsonBuilder`）**：格式化输出、日期格式、`serializeNulls`、自定义 `TypeAdapter` 等 —— 从**全局**定制行为
> - **注解（`@SerializedName`、`@Expose`、`transient`）**：字段重命名、双向过滤、循环引用切断 —— 从**局部**精细控制
>
> 所以，**Java 和 JSON 的鸿沟，Gson 不会替你填，但给你填的工具。**