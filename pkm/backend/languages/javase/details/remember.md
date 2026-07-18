# 反思总结

## 反思
* 学习的思路
    * 明确目标：为了找工作？跳槽？爱好？
    * 现有技能：现在的技术能不能解决？
    * 学新技能：引出新的技能
    * 快速入门：不要追求细节！先搭房子再装修！
    * 细节优化：追求细节，使用规范，优化，从此有无止境
* 编程思想
    * 化繁为简：将复杂的需求拆分成多条简单的需求
    * 先死后活：先考虑固定的值，然后转为变量
* OOP
    * 多组合少继承
        * 继承适合描述“is-a”的关系，但继承容易导致类之间的强耦合，⼀旦⽗类发⽣改变，⼦类也要随之改变，违背了开闭原则（尽量不修改现有代码，⽽是添加新的代码来实现）。
        * 组合适合描述“has-a”或“can-do”的关系，通过在类中组合其他类，能够更灵活地扩展功能。组合避免了复杂的类继承体系，同时遵循了开闭原则和松耦合的设计原则。
* SOLID
    * 单⼀职责原则（Single Responsibility Principle, SRP）[参考视频](https://www.bilibili.com/video/BV1jT411P7Ei/)：⼀个类应该只有⼀个引起它变化的原因，即⼀个类只负责⼀项职责。这样做的⽬的是使类更加清晰，更容易理解和维护。
    * 开闭原则（Open-Closed Principle, OCP）：指软件实体应该**对扩展开放，对修改关闭**。这意味着⼀个类应该通过扩展来实现新的功能，⽽不是通过修改已有的代码来实现。
    * 李⽒替换原则（Liskov Substitution Principle, LSP)
        * 任何⽗类可以出现的地⽅，⼦类也⼀定可以出现。LSP 是继承复⽤的基⽯，只有当⼦类可以替换掉⽗类，并且单位功能不受到影响时，⽗类才能真正被复⽤，⽽⼦类也能够在⽗类的基础上增加新的⾏为。
        * 这意味着⼦类在扩展⽗类时，不应改变⽗类原有的⾏为。例如，如果有⼀个⽅法接受⼀个⽗类对象作为参数，那么传⼊该⽅法的任何⼦类对象也应该能正常⼯作。
        * 比如，鸵鸟继承鸟，这就违反了李⽒替换原则，因为鸵鸟不能飞。
* 接⼝隔离原则（Interface Segregation Principle, ISP）指客户端不应该依赖它不需要的接⼝。这意味着设计接⼝时应该尽量精简，不应该设计臃肿庞⼤的接⼝。
* 依赖倒置原则（Dependency Inversion Principle, DIP）
    * 指⾼层模块不应该依赖低层模块，⼆者都应该依赖其抽象；抽象不应该依赖细节，细节应该依赖抽象。这意味着设计时应该尽量依赖接⼝或抽象类，⽽不是实现类。

## 代码规范

## 代码规范

### 阿里巴巴Java开发手册
- **链接**：[https://pdai.tech/md/dev-spec/code-style/code-style-alibaba.html](https://pdai.tech/md/dev-spec/code-style/code-style-alibaba.html)

### 基本规范建议
1. **命名规范**
   - 类名使用大驼峰：`HelloWorld`
   - 方法名使用小驼峰：`getUserName()`
   - 常量全大写：`MAX_VALUE`

2. **代码格式**
   - 使用4个空格缩进（不要用Tab）
   - 大括号换行风格一致
   - 适当的空行分隔逻辑块

3. **注释规范**
   - 公共API必须使用文档注释
   - 复杂逻辑添加行内注释
   - 及时更新过时的注释


## 资料
* [01-JavaSE《第01章》](https://www.yuque.com/dujubin/java/na23g2vnz7cgzzdi?singleDoc#)
* [《第02章 Java基础语法》](https://www.yuque.com/dujubin/java/rw03xkpkadgaw7u7?singleDoc#)
* [《第03章 IntelliJ IDEA的使用》](https://www.yuque.com/dujubin/java/gqhbqtrtg7ruutad?singleDoc#)
* [《第04章 面向对象》](https://www.yuque.com/dujubin/java/ohod7qvxq1z36ocz?singleDoc#)
* [《第05章 数组》](https://www.yuque.com/dujubin/java/qhagel2niihaqfl0?singleDoc#)
* [《第06章 异常处理》](https://www.yuque.com/dujubin/java/osb8y2l2q8urmtn9?singleDoc#)
* [《第07章 常用类》](https://www.yuque.com/dujubin/java/hmquiuye1fg6irwy?singleDoc#)
* [《第08章 泛型和比较器》](https://www.yuque.com/dujubin/java/tpq5h36k7huw6lmg?singleDoc#)
* [《第09章 数据结构和集合》](https://www.yuque.com/dujubin/java/mqhcc1lh1m94713v?singleDoc#)
* [《第10章 Java I/O》](https://www.yuque.com/dujubin/java/cagtgrmuzx9ig14e?singleDoc#)
* [《第11章 多线程》](https://www.yuque.com/dujubin/java/rgb5uru34dzbwpse?singleDoc#)
* [《第12章 反射机制》](https://www.yuque.com/dujubin/java/txtiia405xiq5g3k?singleDoc#)
* [《第13章 注解》](https://www.yuque.com/dujubin/java/sl7071kp08h6zlwq?singleDoc#)
* [《第14章 网络编程》](https://www.yuque.com/dujubin/java/qnodco6rtzwg62sg?singleDoc#)
* [《第15章 Lambda表达式》](https://www.yuque.com/dujubin/java/oh8efg7v4gfcuvbx?singleDoc#)
* [《第16章 Stream API》](https://www.yuque.com/dujubin/java/piphoczi1zmhhduz?singleDoc#)
* [《第17章 Java新特性》](https://www.yuque.com/dujubin/java/cxnnnxpt8ubmiqle?singleDoc#)
* [02-MySQL](https://www.yuque.com/dujubin/java/uzw5g4gtnuew49yp?singleDoc#)
* [03-JDBC](https://www.yuque.com/dujubin/java/cy7vu9zsa0gmpprp?singleDoc#)
* [04-Web前端](https://www.yuque.com/dujubin/java/gr1diu?singleDoc#)
* [《CSS3》](https://www.yuque.com/dujubin/java/uqkric?singleDoc#)
* [《JavaScript（ES6）》](https://www.yuque.com/dujubin/java/lk3u4vr4uc1ekxbk?singleDoc#)
* [05-XML&JSON](https://www.yuque.com/dujubin/java/anghr4?singleDoc#)
* [06-JavaWeb](https://www.yuque.com/dujubin/java/rd3n67sf9bnakih9?singleDoc#)
* [07-Ajax&axios](https://www.yuque.com/dujubin/java/szlh0l?singleDoc#)
* [08-Maven](https://www.yuque.com/dujubin/java/hp5bllxqf7g9gmn5?singleDoc#)
* [09-MyBatis](https://www.yuque.com/dujubin/java/udots9ngcd97pyui?singleDoc#)
* [10-Spring](https://www.yuque.com/dujubin/java/lyvg9x9hf3u22s7e?singleDoc#)
* [11-SpringMVC](https://www.yuque.com/dujubin/java/myxi54xu063hgsl4?singleDoc#)
* [12-SpringBoot](https://www.yuque.com/dujubin/java/uwxe0halgc03tm93?singleDoc#)
* [13-MyBatis-Plus](https://www.yuque.com/dujubin/java/qgp36l3entp30hp2?singleDoc#)
* [14-TypeScript](https://www.yuque.com/dujubin/java/mt5sq6akfcx5fr5g?singleDoc#)
* [15-Vue3](https://www.yuque.com/dujubin/java/vu082c?singleDoc#)
* [16-ElementPlus](https://www.yuque.com/dujubin/java/yw2xscrz4thagw34?singleDoc#)
* [17-Linux](https://www.yuque.com/dujubin/java/nurwunyse629kzwy?singleDoc#)
