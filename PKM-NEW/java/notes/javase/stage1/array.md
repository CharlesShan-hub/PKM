# Java数组

数组专题推荐浏览顺序：本文 👉 [Arrays](../stage2/Arrays.md)

---

## 数组基础

### 数组初始化方式

1. **方式1**：直接初始化
   ```java
   double[] hens = {3, 5, 1, 3.4, 2, 50};
   ```

2. **方式2**：C风格声明
   ```java
   double hens[] = {3, 5, 1, 3.4, 2, 50};
   ```

3. **方式3**：使用new关键字
   ```java
   double[] hens = new double[]{3, 5, 1, 3.4, 2, 50};
   ```

4. **方式4**：先声明后分配空间
   ```java
   double[] hens;           // 声明
   hens = new double[6];    // 分配空间
   // hens[0] = 1;          // 赋值
   ```

5. **错误方式**：不能同时指定大小和元素
   
   ```java
   double hens[] = new double[6]{3, 5, 1, 3.4, 2, 50};// 错误写法
   ```

**注意**：方式1、2、3是等价的。

### 数组入门案例：找最大值
```java
double[] num = {1.0, 20.4, 11.4, 13};
double max = num[0];
for (int i = 0; i < num.length; i++) {
    if (num[i] > max) {
        max = num[i];
    }
}
System.out.println("max = " + max);
```

---

## 数组特性

### 数组默认值
- **整型、浮点型**：`0`
- **char类型**：`\u0000`
- **boolean类型**：`false`
- **String类型**：`null`

### 数组赋值机制
数组在默认情况下是**引用传递**，赋值的是地址。

```java
int[] arr1 = {1, 2, 3};
int[] arr2 = arr1;          // arr2指向arr1的地址
arr2[0] = 4;                // 修改arr2会影响arr1
System.out.println(arr1[0]); // 输出：4
```

### JVM内存模型
- **栈**：保存变量（包括引用类型的地址）
- **堆**：保存数组的具体内容
- **方法区**：保存类信息、常量等

数组变量在栈中保存的是堆中数组内容的地址。

---

## 数组操作

### 数组拷贝
需要创建独立的数据空间：

#### 方法1：手动拷贝
```java
int[] arr1 = {1, 2, 3};
int[] arr2 = new int[arr1.length];
for (int i = 0; i < arr1.length; i++) {
    arr2[i] = arr1[i];
}
```

#### 方法2：使用System.arraycopy()
```java
int[] arr1 = {1, 2, 3};
int[] arr2 = new int[arr1.length * 2];
System.arraycopy(arr1, 0, arr2, 0, arr1.length);
```

### 数组逆序
```java
int[] arr1 = {1, 2, 3, 4, 5, 6};
int[] arr2 = new int[arr1.length];
for (int i = 0; i < arr1.length; i++) {
    arr2[arr1.length - 1 - i] = arr1[i];
}
arr1 = arr2; // 原arr1指向的内存会被垃圾回收
```

### 数组添加元素
需要创建新数组：

```java
// 案例：在数组{1, 2, 3}后添加元素4
int[] arr = {1, 2, 3};
int[] temp = new int[arr.length + 1];
for (int i = 0; i < arr.length; i++) {
    temp[i] = arr[i];
}
temp[temp.length - 1] = 4;
arr = temp;
```

---

## 多维数组

### 声明方式
```java
int a[][];
int[][] a;
int[] a[];
```

### 二维数组初始化

#### 静态初始化
```java
int[][] arr = {
    {1, 2, 3, 4},
    {10, 20, 30, 40},
    {100, 200, 300, 400}
};

// 等价写法
int[][] arr = new int[][]{
    {1, 2, 3, 4},
    {10, 20, 30, 40},
    {100, 200, 300, 400}
};

System.out.println(arr.length); // 输出：3（行数）
```

#### 动态初始化
```java
int[][] narr = new int[3][4];
for (int i = 0; i < 3; i++) {
    for (int j = 0; j < 4; j++) {
        narr[i][j] = arr[i][j];
    }
}
```

### 不规则二维数组
每行元素个数可以不同：

```java
// 创建如下结构的二维数组：
// 1
// 1 2
// 1 2 3
int[][] arr = new int[3][];
for (int i = 1; i < 4; i++) {
    arr[i - 1] = new int[i];
    for (int j = 0; j < i; j++) {
        arr[i - 1][j] = j + 1;
    }
}
```

### 案例：杨辉三角
```java
public class YangHuiTriangle {
    public static void main(String[] args) {
        int[][] n = new int[10][];
        
        for (int i = 0; i < n.length; i++) {
            n[i] = new int[i + 1];
            
            if (i == 0) {
                n[0][0] = 1;
                continue;
            }
            
            n[i][0] = 1;
            for (int j = 1; j < i; j++) {
                n[i][j] = n[i - 1][j] + n[i - 1][j - 1];
            }
            n[i][i] = 1;
        }
        
        // 打印杨辉三角
        for (int i = 0; i < n.length; i++) {
            for (int j = 0; j <= i; j++) {
                System.out.print(n[i][j] + "\t");
            }
            System.out.println();
        }
    }
}
```

---

## 总结要点

### 数组核心概念
1. **引用类型**：数组是引用类型，赋值传递的是地址
2. **固定长度**：数组一旦创建，长度不可变
3. **索引从0开始**：有效索引范围是0到length-1

### 操作注意事项
1. **拷贝数组**：需要创建新数组并复制元素
2. **添加元素**：需要创建更大的新数组
3. **多维数组**：可以创建不规则数组（每行长度不同）

### 内存管理
- 数组变量在栈中，数组内容在堆中
- 引用赋值不会创建新数组，只是复制地址
- 没有引用的数组会被垃圾回收器回收