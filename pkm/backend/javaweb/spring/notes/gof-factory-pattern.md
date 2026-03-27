# GoF之工厂模式

+ 设计模式：一种可以被重复利用的解决方案。
+ GoF（Gang of Four），中文名——四人组。
+ 《Design Patterns: Elements of Reusable Object-Oriented Software》（即《设计模式》一书），1995年由 Erich Gamma、Richard Helm、Ralph Johnson 和 John Vlissides 合著。这几位作者常被称为"四人组（Gang of Four）"。
+ 该书中描述了23种设计模式。我们平常所说的设计模式就是指这23种设计模式。
+ 不过除了GoF23种设计模式之外，还有其它的设计模式，比如：JavaEE的设计模式（DAO模式、MVC模式等）。
+ GoF23种设计模式可分为三大类：
    - ****创建型****（5个）：解决对象创建问题。
        * 单例模式
        * 工厂方法模式
        * 抽象工厂模式
        * 建造者模式
        * 原型模式
    - ****结构型****（7个）：一些类或对象组合在一起的经典结构。
        * 代理模式
        * 装饰模式
        * 适配器模式
        * 组合模式
        * 享元模式
        * 外观模式
        * 桥接模式
    - ****行为型****（11个）：解决类或对象之间的交互问题。
        * 策略模式
        * 模板方法模式
        * 责任链模式
        * 观察者模式
        * 迭代子模式
        * 命令模式
        * 备忘录模式
        * 状态模式
        * 访问者模式
        * 中介者模式
        * 解释器模式
+ 工厂模式是解决对象创建问题的，所以工厂模式属于创建型设计模式。这里为什么学习工厂模式呢？这是因为Spring框架底层使用了大量的工厂模式。

---

## 工厂模式的三种形态

工厂模式通常有三种形态：

+ 第一种：****简单工厂模式（Simple Factory）：不属于23种设计模式之一。简单工厂模式又叫做：静态 工厂方法模式。简单工厂模式是工厂方法模式的一种特殊实现。****
+ 第二种：工厂方法模式（Factory Method）：是23种设计模式之一。
+ 第三种：抽象工厂模式（Abstract Factory）：是23种设计模式之一。

---

## 简单工厂模式

简单工厂模式的角色包括三个：

+ 抽象产品 角色
+ 具体产品 角色
+ 工厂类 角色

简单工厂模式的代码如下：

抽象产品角色：

```java
public abstract class Weapon {
    /**
     * 所有的武器都有攻击行为
     */
    public abstract void attack();
}
```

具体产品角色：

```java
// 坦克
public class Tank extends Weapon{
    @Override
    public void attack() {
        System.out.println("坦克开炮！");
    }
}

```

```java
// 战斗机
public class Fighter extends Weapon{
    @Override
    public void attack() {
        System.out.println("战斗机投下原子弹！");
    }
}

```

```java
// 匕首
public class Dagger extends Weapon{
    @Override
    public void attack() {
        System.out.println("砍他丫的！");
    }
}

```

工厂类角色：

```java
public class WeaponFactory {
    /**
     * 根据不同的武器类型生产武器
     * @param weaponType 武器类型
     * @return 武器对象
     */
    public static Weapon get(String weaponType){
        if (weaponType == null || weaponType.trim().length() == 0) {
            return null;
        }
        Weapon weapon = null;
        if ("TANK".equals(weaponType)) {
            weapon = new Tank();
        } else if ("FIGHTER".equals(weaponType)) {
            weapon = new Fighter();
        } else if ("DAGGER".equals(weaponType)) {
            weapon = new Dagger();
        } else {
            throw new RuntimeException("不支持该武器！");
        }
        return weapon;
    }
}

```

测试程序（客户端程序）：

```java
public class Client {
    public static void main(String[] args) {
        Weapon weapon1 = WeaponFactory.get("TANK");
        weapon1.attack();

        Weapon weapon2 = WeaponFactory.get("FIGHTER");
        weapon2.attack();

        Weapon weapon3 = WeaponFactory.get("DAGGER");
        weapon3.attack();
    }
}

```

执行结果：

![](https://cdn.nlark.com/yuque/0/2025/png/21376908/1763719728644-ec17cbc9-9c3b-4b51-9e33-8b80cdf138fd.png)

**简单工厂模式的优点：**

+ 客户端程序不需要关心对象的创建细节，需要哪个对象时，只需要向工厂索要即可，初步实现了责任的分离。客户端只负责“消费”，工厂负责“生产”。生产和消费分离。

**简单工厂模式的缺点：**

+ 缺点1：工厂类集中了所有产品的创造逻辑，形成一个无所不知的全能类，有人把它叫做上帝类。显然工厂类非常关键，不能出问题，一旦出问题，整个系统瘫痪。
+ 缺点2：不符合OCP开闭原则，在进行系统扩展时，需要修改工厂类。

****

****Spring中的BeanFactory 是简单工厂模式吗？****

****从最表层的“根据名字拿对象”的功能来看，BeanFactory 的 getBean(String name) 方法扮演了类似简单工厂的角色。但从本质和实现上来看，BeanFactory 是一个功能极其丰富的 IoC容器，它包含并远远超越了简单工厂的功能。****

****

---

## 工厂方法模式

工厂方法模式既保留了简单工厂模式的优点，同时又解决了简单工厂模式的缺点。

工厂方法模式的角色包括：

+ ****抽象工厂角色****
+ ****具体工厂角色****
+ 抽象产品角色
+ 具体产品角色

代码如下：

```java
public abstract class Weapon {
    /**
     * 所有武器都有攻击行为
     */
    public abstract void attack();
}

```

```java
public class Gun extends Weapon{
    @Override
    public void attack() {
        System.out.println("开枪射击！");
    }
}

```

```java
public class Fighter extends Weapon{
    @Override
    public void attack() {
        System.out.println("战斗机发射核弹！");
    }
}

```

```java
public interface WeaponFactory {
    Weapon get();
}

```

```java
public class GunFactory implements WeaponFactory{
    @Override
    public Weapon get() {
        return new Gun();
    }
}

```

```java
public class FighterFactory implements WeaponFactory{
    @Override
    public Weapon get() {
        return new Fighter();
    }
}

```

客户端程序：

```java
public class Client {
    public static void main(String[] args) {
        WeaponFactory factory = new GunFactory();
        Weapon weapon = factory.get();
        weapon.attack();

        WeaponFactory factory1 = new FighterFactory();
        Weapon weapon1 = factory1.get();
        weapon1.attack();
    }
}

```

执行客户端程序：

![](https://cdn.nlark.com/yuque/0/2025/png/21376908/1763720058823-fc661399-c5fb-4d44-acb3-5f6102989891.png)

如果想扩展一个新的产品，只要新增一个产品类，再新增一个该产品对应的工厂即可，例如新增：匕首

```java
public class Dagger extends Weapon{
    @Override
    public void attack() {
        System.out.println("砍丫的！");
    }
}

```

```java
public class DaggerFactory implements WeaponFactory{
    @Override
    public Weapon get() {
        return new Dagger();
    }
}

```

客户端程序：

```java
public class Client {
    public static void main(String[] args) {
        WeaponFactory factory = new GunFactory();
        Weapon weapon = factory.get();
        weapon.attack();

        WeaponFactory factory1 = new FighterFactory();
        Weapon weapon1 = factory1.get();
        weapon1.attack();

        WeaponFactory factory2 = new DaggerFactory();
        Weapon weapon2 = factory2.get();
        weapon2.attack();
    }
}

```

执行结果如下：

![](https://cdn.nlark.com/yuque/0/2025/png/21376908/1763720094112-317c5f56-b197-4ea4-8138-e4a4af4e661a.png)

我们可以看到在进行功能扩展的时候，不需要修改之前的源代码，显然工厂方法模式符合OCP原则。

**工厂方法模式的优点：**

+ 扩展性高，如果想增加一个产品，只要扩展一个工厂类就可以。
+ 屏蔽产品的具体实现，调用者只关心产品的接口。

**工厂方法模式的缺点：**

+ 每次增加一个产品时，都需要增加一个具体类和对象实现工厂，使得系统中类的个数成倍增加，在一定程度上增加了系统的复杂度。

---

## 抽象工厂模式（了解）

抽象工厂模式相对于工厂方法模式来说，就是工厂方法模式是针对一个产品系列的，而抽象工厂模式是针对多个产品系列的，即工厂方法模式是一个产品系列一个工厂类，而抽象工厂模式是多个产品系列一个工厂类。

抽象工厂模式特点：抽象工厂模式是所有形态的工厂模式中最为抽象和最具一般性的一种形态。抽象工厂模式是指当有多个抽象角色时，使用的一种工厂模式。抽象工厂模式可以向客户端提供一个接口，使客户端在不必指定产品的具体的情况下，创建多个产品族中的产品对象。它有多个抽象产品类，每个抽象产品类可以派生出多个具体产品类，一个抽象工厂类，可以派生出多个具体工厂类，每个具体工厂类可以创建多个具体产品类的实例。每一个模式都是针对一定问题的解决方案，工厂方法模式针对的是一个产品等级结构；而抽象工厂模式针对的是多个产品等级结构。

抽象工厂中包含4个角色：

+ 抽象工厂角色
+ 具体工厂角色
+ 抽象产品角色
+ 具体产品角色

抽象工厂模式的类图如下：

![](https://cdn.nlark.com/yuque/0/2022/png/21376908/1665370116084-46b714b8-95d2-45c5-89b6-564057c45694.png)

抽象工厂模式代码如下：

第一部分：武器产品族

```java
package com.jkweilai.product;

/**
 * 武器产品族
 */
public abstract class Weapon {
    public abstract void attack();
}

```

```java
package com.jkweilai.product;

/**
 * 武器产品族中的产品等级1
 */
public class Gun extends Weapon{
    @Override
    public void attack() {
        System.out.println("开枪射击！");
    }
}

```

```java
package com.jkweilai.product;

/**
 * 武器产品族中的产品等级2
 */
public class Dagger extends Weapon{
    @Override
    public void attack() {
        System.out.println("砍丫的！");
    }
}

```

第二部分：水果产品族

```java
package com.jkweilai.product;

/**
 * 水果产品族
 */
public abstract class Fruit {
    /**
     * 所有果实都有一个成熟周期。
     */
    public abstract void ripeCycle();
}

```

```java
package com.jkweilai.product;

/**
 * 水果产品族中的产品等级1
 */
public class Orange extends Fruit{
    @Override
    public void ripeCycle() {
        System.out.println("橘子的成熟周期是10个月");
    }
}

```

```java
package com.jkweilai.product;

/**
 * 水果产品族中的产品等级2
 */
public class Apple extends Fruit{
    @Override
    public void ripeCycle() {
        System.out.println("苹果的成熟周期是8个月");
    }
}

```

第三部分：抽象工厂类

```java
package com.jkweilai.factory;

import com.jkweilai.product.Fruit;
import com.jkweilai.product.Weapon;

/**
 * 抽象工厂
 */
public abstract class AbstractFactory {
    public abstract Weapon getWeapon(String type);
    public abstract Fruit getFruit(String type);
}

```

第四部分：具体工厂类

```java
package com.jkweilai.factory;

import com.jkweilai.product.Dagger;
import com.jkweilai.product.Fruit;
import com.jkweilai.product.Gun;
import com.jkweilai.product.Weapon;

/**
 * 武器族工厂
 */
public class WeaponFactory extends AbstractFactory{

    public Weapon getWeapon(String type){
        if (type == null || type.trim().length() == 0) {
            return null;
        }
        if ("Gun".equals(type)) {
            return new Gun();
        } else if ("Dagger".equals(type)) {
            return new Dagger();
        } else {
            throw new RuntimeException("无法生产该武器");
        }
    }

    @Override
    public Fruit getFruit(String type) {
        return null;
    }
}

```

```java
package com.jkweilai.factory;

import com.jkweilai.product.*;

/**
 * 水果族工厂
 */
public class FruitFactory extends AbstractFactory{
    @Override
    public Weapon getWeapon(String type) {
        return null;
    }

    public Fruit getFruit(String type){
        if (type == null || type.trim().length() == 0) {
            return null;
        }
        if ("Orange".equals(type)) {
            return new Orange();
        } else if ("Apple".equals(type)) {
            return new Apple();
        } else {
            throw new RuntimeException("我家果园不产这种水果");
        }
    }
}

```

第五部分：客户端程序

```java
package com.jkweilai.client;

import com.jkweilai.factory.AbstractFactory;
import com.jkweilai.factory.FruitFactory;
import com.jkweilai.factory.WeaponFactory;
import com.jkweilai.product.Fruit;
import com.jkweilai.product.Weapon;

public class Client {
    public static void main(String[] args) {
        // 客户端调用方法时只面向AbstractFactory调用方法。
        AbstractFactory factory = new WeaponFactory(); // 注意：这里的new WeaponFactory()可以采用 简单工厂模式 进行隐藏。
        Weapon gun = factory.getWeapon("Gun");
        Weapon dagger = factory.getWeapon("Dagger");

        gun.attack();
        dagger.attack();

        AbstractFactory factory1 = new FruitFactory(); // 注意：这里的new FruitFactory()可以采用 简单工厂模式 进行隐藏。
        Fruit orange = factory1.getFruit("Orange");
        Fruit apple = factory1.getFruit("Apple");

        orange.ripeCycle();
        apple.ripeCycle();
    }
}

```

执行结果：

![](https://cdn.nlark.com/yuque/0/2025/png/21376908/1763720813526-b7cea529-1376-41f5-b157-55ba11b05d1c.png)

抽象工厂模式的优缺点：

+ 优点：当一个产品族中的多个对象被设计成一起工作时，它能保证客户端始终只使用同一个产品族中的对象。
+ 缺点：产品族扩展非常困难，要增加一个系列的某一产品，既要在AbstractFactory里加代码，又要在具体的里面加代码。
