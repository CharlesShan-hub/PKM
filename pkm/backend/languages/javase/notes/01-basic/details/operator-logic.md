
# 逻辑运算符

## 逻辑运算符分类
> `&&`和`||`和C语言一样，就会短路。`$`和`|`就不会短路。

- **逻辑与** `&`：非短路，两边都计算
- **逻辑或** `|`：非短路，两边都计算  
- **逻辑异或** `^`：相同为false，不同为true
- **逻辑非** `!`：取反
- **短路与** `&&`：左边为false则短路
- **短路或** `||`：左边为true则短路


## 短路 vs 非短路
```java
public class LogicDemo {
    public static boolean condition1() {
        System.out.println("condition1执行");
        return true;
    }
    
    public static boolean condition2() {
        System.out.println("condition2执行");
        return false;
    }
    
    public static void main(String[] args) {
        System.out.println("=== 非短路与 & ===");
        if (condition1() & condition2()) {
            // 两个条件都会执行
        }
        
        System.out.println("\n=== 短路与 && ===");
        if (condition1() && condition2()) {
            // condition2可能不会执行
        }
    }
}
```


## 逻辑运算练习
```java
// 练习1：非短路与
int x = 5, y = 5;
if (x++ == 6 & ++y == 6) {  // x=5(比较),x=6; y=6(比较)
    x = 11;
}
System.out.println("x=" + x + ", y=" + y);  // x=6, y=6

// 练习2：短路与
int x = 5, y = 5;
if (x++ == 6 && ++y == 6) {  // x=5(比较),x=6; y不变（短路）
    x = 11;
}
System.out.println("x=" + x + ", y=" + y);  // x=6, y=5

// 练习3：非短路或
int x = 5, y = 5;
if (x++ == 5 | ++y == 5) {  // x=5(比较),x=6; y=6(比较)
    x = 11;
}
System.out.println("x=" + x + ", y=" + y);  // x=11, y=6

// 练习4：短路或
int x = 5, y = 5;
if (x++ == 5 || ++y == 5) {  // x=5(比较),x=6; y不变（短路）
    x = 11;
}
System.out.println("x=" + x + ", y=" + y);  // x=11, y=5

// 练习5：综合练习
boolean x = true;
boolean y = false;
short z = 46;
if ((z++ == 46) && (y = true)) z++;  // z=47, y=true, z=48
if ((x = false) || (++z == 49)) z++;  // x=false, z=49, z=50
System.out.println("z=" + z);  // z=50
```


## 异或运算
```java
// 异或：相同为false，不同为true
System.out.println(true ^ true);    // false
System.out.println(true ^ false);   // true
System.out.println(false ^ true);   // true
System.out.println(false ^ false);  // false
```
