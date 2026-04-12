
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
