# 访问修饰符（权限修饰符）

> [Java访问控制修饰符详解（public、 private、protected 和 friendly）](http://c.biancheng.net/view/965.html)

---
## 精华总结

|   访问修饰符   |   描述    | 当前类 | 同包  | 子类  | 其他包 |
| :-------: | :-----: | :-: | :-: | :-: | :-: |
|  public   |  全部公开   |  ✅  |  ✅  |  ✅  |  ✅  |
| protected | 不同包不能用  |  ✅  |  ✅  |  ✅  |  ❌  |
|    默认     | 默认子类不能用 |  ✅  |  ✅  |  ❌  |  ❌  |
|  private  |   私有    |  ✅  |  ❌  |  ❌  |  ❌  |

|   访问修饰符   | 类（外部类） | 接口  | 变量  | 方法  |
| :-------: | :----: | :-: | :-: | :-: |
|  public   |   ✅    |  ✅  |  ✅  |  ✅  |
| protected |   ❌    |  ❌  |  ✅  |  ✅  |
|    默认     |   ✅    |  ✅  |  ✅  |  ✅  |
|  private  |   ❌    |  ❌  |  ✅  |  ✅  |

---
## 场景

java既然最常用public和private为什么要有protected和默认呢，这些常用的场景是什么呢？

当需要提供一个流程，一些方法需要让子类去重写，但不要子类直接访问，可以使用`protected`

```java
// 基类设计为可扩展
public abstract class AbstractController {
    // 子类可以重写，但外部不能直接调用
    protected void validateParameters(Map<String, Object> params) {
        // 参数验证逻辑
    }
    
    // 模板方法模式
    public final void process() {
        validateParameters(getParams());
        doBusiness();
    }
    
    protected abstract void doBusiness();
    protected abstract Map<String, Object> getParams();
}

// 子类使用
public class UserController extends AbstractController {
    @Override
    protected void validateParameters(Map<String, Object> params) {
        // 可以重写父类的保护方法
        super.validateParameters(params);
        // 添加额外的验证
    }
    
    @Override
    protected void doBusiness() {
        // 业务实现
    }
}
```

如果写一个工具类，比如字符串处理，只想要在包内使用，就可以用默认

```java
// 字符串处理工具，只在当前包内使用
class StringUtils {
    static String normalize(String input) {
        // 内部工具方法
    }
}

public class TextProcessor {
    public String process(String text) {
        // 使用包内工具类
        return StringUtils.normalize(text);
    }
}
```

---
## 测试案例（可跳过）

* 文件结构

  ```
  - com.charles.modifiermodifier1
  | - Main
  | - A
  | - SamePacket
  - com.charles.modifiermodifier2
  | - SubA
  - com.charles.modifiermodifier3
  | - AnotherPacket
  ```

* Main

  ```java
  package com.charles.modifier;
  import com.charles.modifier2.SubA;
  import com.charles.modifier3.AnotherPacket;
  
  public class Main{
      public static void main(String[] args){
          A a = new A();
          a.test();
          SamePacket b = new SamePacket();
          b.test();
          SubA sa = new SubA();
          sa.test();
          AnotherPacket ap = new AnotherPacket();
          ap.test();
      }
  }
  /*
  同类
  public 100
  protected 200
  default 300
  private 400
  同包不同类(同一个文件夹的不同类)
  public 100
  protected 200
  default 300
  子类
  public 100
  protected 200
  不同包
  public 100
  */
  ```

* A

  ```java
  package com.charles.modifier;
  public class A{
      public int n1 = 100;
      protected int n2 = 200;
      int n3 = 300;
      private int n4 = 400;
      public void test(){
          System.out.println("同类");
          System.out.println("public "+n1);
          System.out.println("protected "+n2);
          System.out.println("default "+n3);
          System.out.println("private "+n4);
      }
  }
  ```

* SamePacket

  ```java
  package com.charles.modifier;
  import com .charles.modifier.A;
  
  public class SamePacket {
      public void test(){
          A a = new A();
          System.out.println("同包不同类");
          System.out.println("public "+a.n1);
          System.out.println("protected "+a.n2);
          System.out.println("default "+a.n3);
          //System.out.println("private "+a.n4);
      }
  }
  ```

* SubA

  ```java
  package com.charles.modifier2;
  import com.charles.modifier.A;
  
  public class SubA extends A {
      public void test(){
          A a = new A();
          System.out.println("子类");
          System.out.println("public "+n1);
          System.out.println("protected "+n2);
          //System.out.println("default "+n3);
          //System.out.println("private "+a.n4);
      }
  }
  ```

* AnotherPacket

  ```java
  package com.charles.modifier3;
  import com.charles.modifier.A;
  
  public class AnotherPacket {
      public void test(){
          A a = new A();
          System.out.println("不同包");
          System.out.println("public "+a.n1);
          //System.out.println("protected "+a.n2);
          //System.out.println("default "+a.n3);
          //System.out.println("private "+A.n4);
      }
  }
  ```
