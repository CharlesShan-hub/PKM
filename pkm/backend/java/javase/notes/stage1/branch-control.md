# Java控制结构

![java-basic-branchs.excalidraw|1000](../../assets/java-basic-branchs.excalidraw.md)

---

## 顺序控制

程序从上到下逐行执行，是最基本的控制结构。

---

## 分支结构

### 1. 单分支 if
```java
if (condition) {
    // 代码块
}
```

**注意**：如果只有一行代码，可以不写大括号（但不推荐）。

### 2. 双分支 if-else
```java
if (condition) {
    // 代码块1
} else {
    // 代码块2
}
```

**示例：判断闰年**
```java
int year = 2024;
if ((year % 4 == 0 && year % 100 != 0) || year % 400 == 0) {
    System.out.println("闰年");
} else {
    System.out.println("平年");
}
```

### 3. 多分支 if-else if
```java
if (condition1) {
    // 代码块1
} else if (condition2) {
    // 代码块2
} else if (condition_n) {
    // 代码块n
} else {
    // 默认代码块
}
```

### 4. 嵌套分支
if语句可以嵌套使用，但建议不要超过三层嵌套。

**减少嵌套的方法**：
```java
while (condition) {
    if (flag) continue;  // 跳过当前迭代
    // 其他代码
}
```

### 5. switch语句
```java
switch (表达式) {
    case 常量1:
        语句块1;
        break;
    case 常量2:
        语句块2;
        break;
    // ...
    case 常量n:
        语句块n;
        break;
    default:
        默认语句块;
        break;
}
```

#### switch注意事项：
1. **break作用**：只退出switch，不退出外层循环
2. **穿透现象**：如果case后没有break，会继续执行下一个case
3. **表达式类型限制**（重要‼️）：
   - 整型：**byte、short、int、long**
   - 枚举类型（**enum**）
   - 字符串（**Java 7+**）
   - **不支持**：浮点型、布尔型

```java
// 错误示例：不支持double
double num = 1.1;
switch (num) {  // 编译错误
    case 1.1:
        // ...
}

// 正确示例：char可以，但要注意类型匹配
char c = 'a';
switch (c) {
    case "a":  // 错误：字符串不能匹配char
    case 20:   // 正确：char可以匹配整型常量
}
```

4. **case值限制**：必须是常量或常量表达式，不能是变量
```java
int j = 2;
switch (n) {
    case j:      // 错误：不能是变量
    case 1 + 1:  // 正确：常量表达式
}
```

### 6. switch vs if 选择建议
- **使用switch**：判断的具体数值不多，且符合**byte、short、int、char、enum、String**六种类型
	- 最原始：byte，short，int，char，以及对应的包装类。
	- java5：enum
	- java7：String
- **使用if**：区间判断、结果为boolean类型、复杂条件判断

### 7. Java 12+ 新特性
#### 箭头语法（->）
```java
int month = 4;
String season = switch (month) {
    case 12, 1, 2 -> "冬季";
    case 3, 4, 5 -> "春季";
    case 6, 7, 8 -> "夏季";
    case 9, 10, 11 -> "秋季";
    default -> "无效月份";
};
```

#### 作为表达式返回值
```java
int dayNumber = switch (day) {
    case "MON" -> 1;
    case "TUE" -> 2;
    case "WED" -> 3;
    case "THU" -> 4;
    case "FRI" -> 5;
    case "SAT" -> 6;
    case "SUN" -> 7;
    default -> 0;
};
```

#### 使用yield返回值（Java 13+）
```java
String day = "MON";
String dayDescription = switch (day) {
    case "MON" -> {
        System.out.println("一周的开始");
        yield "星期一";
    }
    case "TUE" -> "星期二";
    // ... 其他cases
    default -> "未知";
};
```

---

## 循环结构

### 1. for循环
```java
for (循环变量初始化; 循环条件; 循环变量迭代) {
    语句块;
}
```

**特点**：
- 初始化和变量迭代可以用逗号分隔多个表达式
- `for (;;)` 表示死循环（两个分号不能省略）

### 2. while循环
```java
while (循环条件) {
    循环体;
    循环变量迭代;
}
```

### 3. do-while循环
```java
do {
    循环体;
    循环变量迭代;
} while (循环条件);
```

**示例：统计1-200之间能被5整除但不能被3整除的数**
```java
public class Demo {
    public static void main(String[] args) {
        int i = 1;
        int count = 0;
        do {
            if (i % 5 == 0 && i % 3 != 0) {
                System.out.println(i);
                count++;
            }
            i++;
        } while (i <= 200);
        System.out.println("count = " + count);
    }
}
```

### 4. 多重循环
建议不要超过三层嵌套。

**示例1：九九乘法表**
```java
public class Demo {
    public static void main(String[] args) {
        for (int i = 1; i < 10; i++) {
            for (int j = 1; j <= i; j++) {
                System.out.print(i + " * " + j + " = " + (i * j) + "\t");
            }
            System.out.println();
        }
    }
}
```

**示例2：空心金字塔**
```java
public class Demo {
    public static void main(String[] args) {
        int height = 5;
        
        // 上半部分（三角形）
        for (int i = 1; i <= height - 1; i++) {
            // 左边空格
            for (int j = 0; j < height - i; j++) {
                System.out.print(" ");
            }
            
            // 左边星号
            System.out.print("*");
            
            // 中间空格
            for (int k = 1; k < 2 * (i - 1); k++) {
                System.out.print(" ");
            }
            
            // 右边星号（第一行除外）
            if (i != 1) {
                System.out.print("*");
            }
            
            // 右边空格
            for (int j = 0; j < height - i; j++) {
                System.out.print(" ");
            }
            
            System.out.println();
        }
        
        // 底部（最后一行）
        for (int i = 0; i < 2 * height - 1; i++) {
            System.out.print("*");
        }
    }
}
```

---

## 循环控制语句

### 1. break
用于跳出当前循环或switch语句。

**带标签的break**：
```java
label1:
for (int j = 0; j < 4; j++) {
    label2:
    for (int i = 0; i < 10; i++) {
        if (i == 2) break label1;  // 跳出外层循环
        System.out.println("i=" + i + " j=" + j);
    }
}
// 输出：
// i=0 j=0
// i=1 j=0
```

### 2. continue
跳过当前循环的剩余部分，继续下一次迭代。

**带标签的continue**：
```java
label1:
for (int j = 0; j < 4; j++) {
    label2:
    for (int i = 0; i < 10; i++) {
        if (i == 2) continue label1;  // 跳过外层循环的当前迭代
        System.out.println("i=" + i + " j=" + j);
    }
}
// 输出：
// i=0 j=0
// i=1 j=0
// i=0 j=1
// i=1 j=1
// i=0 j=2
// i=1 j=2
// i=0 j=3
// i=1 j=3
```

### 3. return
跳出所在方法，结束方法的执行。

---

## 总结

### 控制结构选择指南
1. **顺序结构**：默认执行方式
2. **分支结构**：
   - 简单条件：if-else
   - 多值匹配：switch
   - 复杂条件：if-else if
3. **循环结构**：
   - 已知循环次数：for
   - 未知循环次数：while
   - 至少执行一次：do-while

### 最佳实践
1. 避免过深的嵌套（建议不超过3层）
2. switch语句记得加break防止穿透
3. 循环中合理使用break和continue控制流程
4. 多重循环使用标签提高可读性