# 专题：变量与数据类型

* 基础
    * 👉 [keywords](details/keywords.md): 关键字(官方预留的)
    * 👉 [identifier](details/identifier.md): 标识符(用户可写的)
    * 👉 [literal](details/literal.md): 字面量
    * 👉 [variable](details/variable.md): 变量
* 类型
    * 👉 [var-type](details/var-type.md): 数据类型概述
    * 👉 [intenger](details/intenger.md): 整型
    * 👉 [float](details/float.md): 浮点型
    * 👉 [char](details/char.md): 字符型
    * 👉 [boolean](details/boolean.md): 布尔型
* 运算符
    * 👉 [operator](operator.md)：运算符概述
    * 👉 [operator-basic](details/operator-basic.md)：基础运算符
    * 👉 [operator-compare](details/operator-compare.md)：比较运算符
    * 👉 [operator-logic](details/operator-logic.md)：逻辑运算符
    * 👉 [operator-assign](details/operator-assign.md)：赋值运算符、三目运算符
* 后续扩展
    * 👉 [WrapperClass](../04-utils/WrapperClass.md)

---


## 进制
| 进制   | 前缀        | 举例      |
| ---- | --------- | ------- |
| 二进制  | `0b`，`0B` | `0b111` |
| 十进制  | 没有前缀      | `7`     |
| 八进制  | `0`       | `07`    |
| 十六进制 | `0x`，`0X` | `0x7`   |

```java
public class Hello{
  public static void main(String[] args){
    int num1 = 0b111;
    int num2 = 111;
    int num3 = 0111;
    int num4 = 0x111;
    System.out.println("num1:"+num1);//num1:7
    System.out.println("num2:"+num2);//num2:111
    System.out.println("num3:"+num3);//num3:73
    System.out.println("num4:"+num4);//num4:273
  }
}
```

* 进制转换工具
  * [在线转换工具](https://www.sojson.com/hexconvert.html)
  * [二、八、十、十六进制之间的转换](http://t.csdn.cn/8WKlz)

---


## 类型转换

### 自动类型转换

#### 转换方向（从小到大）
```txt
byte 
⬇️
short 
⬇️
int ➡️ long ➡️ float ➡️ double
⬆️
char
```


#### 转换规则
1. **默认转成最宽泛的类型；用常量赋值float需要指定f**

    ```java
    int a = 1;
    // 错误：1.1默认为double
    float n1 = a + 1.1;

    // 正确：明确指定float
    float n2 = a + 1.1F;

    // 正确：使用double接收
    double n3 = a + 1.1;

    // 正确：float+float没有自动变double
    float f1 = 10.0f;
    float f2 = 20.0f;
    float f3 = f1 + f2;
    ```

2. **byte/short**

    ```java
    // 语法糖：-128到127的int可以直接赋值给byte
    // 正确：常量在范围内可自动转换
    byte a = 127;
    // 错误：超出范围
    // byte b = 128;
    // 正确：强制转换
    byte c = (byte) 127;
    // 正确：强制转换
    byte c = (byte) 128;// 变成了-128了

    System.out.println(Integer.toBinaryString(128));  
    // 10000000
    System.out.println(Integer.toBinaryString((byte)128));
    // 11111111111111111111111110000000
    // 因为byte强制转型，然后128本来的符号为0没了，数字位1变成了byte的符号了。

    // 错误：变量无法判断范围
    int temp = 97;
    // byte d = temp;

    // 正确：强制转换
    byte e = (byte) temp;
    ```

3. **char与byte/short的特殊关系**

    ```java
    // 正确：char可以直接保存整数常量
    char f = 97;

    // 错误：byte不能自动转成char
    // char g = a;

    // 正确：强制转换
    char h = (char) a;
    ```

4. **byte/short运算会自动提升精度**

    ```java
    byte age = 20;
    byte age2 = 30;
    // age + age2 的结果是int类型
    int sum = age + age2;
    ```

5. **boolean不参与转换**

    ```java
    boolean flag = true;
    // 错误：boolean不能转换为其他类型
    // int num = flag;
    ```


### 强制类型转换
通过类型转换运算符 `(类型)`：

```java
double d = 3.14;
int i = (int) d;  // i = 3（截断小数部分）
```


### 基本类型与String的转换

#### 基本类型 → String
```java
int num = 123;
String s = num + "";  // "123"
```


#### String → 基本类型
使用[WrapperClass](../04-utils/WrapperClass.md)的解析方法：

```java
String s = "123";

int n1 = Integer.parseInt(s);
double n2 = Double.parseDouble(s);
float n3 = Float.parseFloat(s);
long n4 = Long.parseLong(s);
byte n5 = Byte.parseByte(s);
boolean n6 = Boolean.parseBoolean("true");
short n7 = Short.parseShort(s);
```


#### char → 基本类型
使用`Character`类（也是包装类）的方法：

```java
int a = Character.getNumericValue('1');
int b = Character.digit('1', 10);
```


#### 字符串操作
```java
// 提取字符串中的字符
String s = "123";
char c = s.charAt(0);  // '1'

// 字符串相等比较（推荐方式）
String name = "林黛玉";
System.out.println("林黛玉".equals(name));  // 更好：避免空指针
System.out.println(name.equals("林黛玉"));   // 可能引发空指针异常
```

---


## 总结要点
1. **变量命名**：作用域内不能重名，Java不支持变量遮蔽
2. **类型选择**：
   * 整数默认用 `int`，大数用 `long`
   * 浮点数默认用 `double`，`float` 必须加 `F` 后缀
3. **类型转换**：
   * 小范围类型可自动转大范围类型
   * 大范围转小范围需要强制转换
   * `boolean` 不参与类型转换
4. **浮点数陷阱**：避免直接比较，使用容差法
5. **字符串操作**：使用 `equals()` 比较字符串，注意空指针问题
6. **字符特性**：`char` 可参与数值运算，本质是Unicode编码
