
# 模板模式

---
## 简介

模板模式（Template Pattern）是一种行为设计模式，用于定义一个操作中的算法骨架，而将一些**步骤延迟到子类中实现**。

下面是一个实际的例子：模拟不同类型的咖啡制作过程。

```java
// 抽象模板类 - 饮料制作
abstract class BeverageMaker {
    // 模板方法，定义了制作饮料的骨架
    public final void prepareBeverage() {
        boilWater();
        brew();
        pourInCup();
        addCondiments();
    }
    
    // 公共步骤 - 煮水
    private void boilWater() {
        System.out.println("煮沸水");
    }
    
    // 公共步骤 - 倒入杯子
    private void pourInCup() {
        System.out.println("将饮料倒入杯子");
    }
    
    // 抽象方法 - 冲泡（子类必须实现）
    protected abstract void brew();
    
    // 抽象方法 - 添加调料（子类必须实现）
    protected abstract void addCondiments();
}

// 具体子类 - 咖啡
class CoffeeMaker extends BeverageMaker {
    @Override
    protected void brew() {
        System.out.println("用沸水冲泡咖啡");
    }
    
    @Override
    protected void addCondiments() {
        System.out.println("添加糖和牛奶");
    }
}

// 具体子类 - 茶
class TeaMaker extends BeverageMaker {
    @Override
    protected void brew() {
        System.out.println("用沸水浸泡茶叶");
    }
    
    @Override
    protected void addCondiments() {
        System.out.println("添加柠檬");
    }
}

// 测试类
public class TemplatePatternDemo {
    public static void main(String[] args) {
        System.out.println("准备咖啡:");
        BeverageMaker coffee = new CoffeeMaker();
        coffee.prepareBeverage();
        
        System.out.println("\n准备茶:");
        BeverageMaker tea = new TeaMaker();
        tea.prepareBeverage();
    }
}
```

运行结果会是：
```
准备咖啡:
煮沸水
用沸水冲泡咖啡
将饮料倒入杯子
添加糖和牛奶

准备茶:
煮沸水
用沸水浸泡茶叶
将饮料倒入杯子
添加柠檬
```

这个例子展示了模板模式的关键点：

1. `BeverageMaker` 是抽象模板类，定义了制作饮料的固定流程（`prepareBeverage()`）
2. 使用 `final` 关键字确保算法骨架不可被子类修改
3. 公共步骤（`boilWater()` 和 `pourInCup()`）在父类中实现
4. 可变步骤（`brew()` 和 `addCondiments()`）声明为抽象方法，由子类实现
5. 具体类（`CoffeeMaker` 和 `TeaMaker`）实现了不同的冲泡和调料添加方式

模板模式的优点：
- 代码复用：公共步骤在父类中实现，避免重复
- 扩展性好：新增饮料类型只需创建新子类
- 行为控制：父类控制整体流程，子类只实现特定步骤

这个模式在实际开发中非常常见，比如：
- 数据访问的模板（JDBC操作流程）
- Servlet的service方法
- 框架中的回调方法等

---

## 模板方法设计模式（老杜的课的笔记）

模板方法模式（Template Method Pattern）是GoF 23种设计模式中的一种**行为型**设计模式，它定义了一个操作中的算法骨架，而将一些步骤延迟到子类中实现。

### 核心概念

模板方法模式的主要思想是：

+ **定义一个算法的骨架**，将不变的部分（通用步骤）放在父类中实现
+ **可变的部分**（具体实现）通过抽象方法或钩子方法留给子类实现
+ 通过这种方式，可以在不改变算法结构的情况下，重新定义算法中的某些步骤

### 结构组成

模板方法模式通常包含以下几个角色：

1. **抽象类（AbstractClass）**：
    - 定义了一个或多个抽象操作，这些操作由子类实现
    - 实现了一个模板方法，定义了算法的骨架
2. **具体子类（ConcreteClass）**：
    - 实现抽象类中定义的抽象操作
    - 可以有多个具体子类，每个子类提供不同的实现

### 代码示例

```java
// 抽象类
// 游戏模板
abstract class Game {
    
    // 玩游戏的标准流程（模板方法）
    public final void play() {
        start();
        playing();
        if (needSound()) {
            playSound();
        }
    }
    
    // 开始游戏：每种游戏开始方式不同
    protected abstract void start();
    
    // 游戏进行中：每种游戏玩法不同
    protected abstract void playing();
    
    // 播放音效：具体方法，已经有默认实现
    private void playSound() {
        System.out.println("播放游戏音效...");
    }

    // 注意：模板方法设计模式中，不一定要有钩子。不过一般都是有钩子的。因为钩子可以让子类有决定权，子类可以决定步骤中的某个环节是否执行。
    // 是否需要音效：钩子方法，默认需要音效
    protected boolean needSound() {
        return true;
    }
}

// 具体子类
// 象棋游戏
class ChessGame extends Game {
    @Override
    protected void start() {
        System.out.println("摆好棋盘，红方先走");
    }
    
    @Override
    protected void playing() {
        System.out.println("车马炮相士帅，轮流走子");
    }
    
    @Override
    protected boolean needSound() {
        return false; // 象棋不需要音效
    }
}

// 具体子类
// 赛车游戏
class RacingGame extends Game {
    @Override
    protected void start() {
        System.out.println("3、2、1，踩油门出发！");
    }
    
    @Override
    protected void playing() {
        System.out.println("控制方向盘，躲避障碍物");
    }
    // 使用默认的needSound()方法，赛车游戏需要音效
}

// 测试
public class Test {
    public static void main(String[] args) {
        System.out.println("玩象棋：");
        Game chess = new ChessGame();
        chess.play();
        
        System.out.println("\n玩赛车游戏：");
        Game racing = new RacingGame();
        racing.play();
    }
}
```

**注意：模板方法设计模式中，不一定要有钩子。不过一般都是有钩子的。因为钩子可以让子类有决定权，子类可以决定步骤中的某个环节是否执行。**

### 应用场景

模板方法模式适用于以下情况：

1. 一次性实现一个算法的不变部分，将可变部分留给子类实现
2. 各子类中公共的行为应被提取到父类中，避免代码重复

实际应用示例：

1. **Servlet中的doGet/doPost方法**：HttpServlet类提供了service()方法作为模板方法
2. **Spring框架**：JdbcTemplate等模板类大量使用模板方法模式

### 注意事项

1. **模板方法通常被声明为final**，以防止子类重写算法结构
2. 尽量减少模板方法中需要子类实现的方法数量

模板方法模式通过封装算法骨架，实现了代码复用和扩展性的平衡，是面向对象设计中非常实用的一种模式。
