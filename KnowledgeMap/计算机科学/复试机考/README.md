# WDAlgorithmsNote

 王道考研机试指南第2版——题目链接、代码
 > 题解（书籍作者炉灰）：[例题代码](https://github.com/BenedictYoung/Lecture)   [习题代码](https://github.com/BenedictYoung/Practice)

# 题目及链接

## 第2章 暴力求解

### [2.1 枚举](./notes/第2章/枚举.md)

> 1. 暴力求解要擅长设置大小为N的数组，每个元素对应一个信息：
>
>    1. 手机键盘不同数字权重不同，求一串文本的权重。可以设置`下标:权重`数组（http://t.cn/E9ulclc）
>
>    2. 一段路上种N+1棵树(0到N)，每次移走一个区间，最后剩几棵树。可以设置`下标:是否有树`数组(http://t.cn/E9ufYo5)
>
> 2. 循环输入
>
>    ```C
>    while(scanf("%d",&n)!=EOF)
>    ```
>
> 3. 反序数
>
>    ```C
>    int Reverse(int num){
>      int count = 0;
>      for(int n=num; n>0; n/=10)
>        count=n%10+count*10;
>      return count;
>    }
>    ```
>

|         | 题目                                     | 地址                |
| ------- | ---------------------------------------- | ------------------- |
| 例题2.1 | abc（清华大学复试上机题）                | http://t.cn/E9WMRTE |
| 例题2.2 | 反序数（清华大学复试上机题）             | http://t.cn/E9WBrut |
| 例题2.3 | 对称平方数1（清华大学复试上机题）        | http://t.cn/E9lUYRn |
| 习题2.1 | 与7无关的数（北京大学复试上机题）        | http://t.cn/E9lOOZQ |
| 习题2.2 | 百鸡问题（北京哈尔滨工业大学复试上机题） | http://t.cn/E9ldhru |
| 习题2.3 | old bill（上海交通大学复试上机题）       | http://t.cn/E9jqijR |

### 2.2 模拟

> 1. 判断闰年
>
>    ```C
>    bool is_leap(int year){
>      if(year%100==0) return year%400==0;
>      else return year%4==0;
>    }
>    ```
>
> 2. 每月日期
>
>    ```C
>    int day[2][12] = {
>      {31,28,31,30,31,30,31,31,30,31,30,31},
>      {31,29,31,30,31,30,31,31,30,31,30,31},
>    }
>    day[is_leap(year)][month];//某一个月的天数
>    ```

#### 1. 图形排版

|         | 题目                                    | 地址                                           |
| ------- | --------------------------------------- | ---------------------------------------------- |
| 例题2.4 | 输出梯形（清华大学复试上机题）          |                                                |
| 例题2.5 | 叠筐                                    | http://acm.hdu.edu.cn/showproblem.php?pid=2074 |
| 习题2.4 | Repeater（北京大学复试上机题）          | http://t.cn/E9jcaVb                            |
| 习题2.5 | Hello World for U（浙江大学复试上机题） | http://t.cn/E9jizni                            |

#### 2. 日期问题

|         | 题目                                 | 地址                |
| ------- | ------------------------------------ | ------------------- |
| 例题2.6 | 今年的第几天？（清华大学复试上机题） | http://t.cn/E9jXK5A |
| 例题2.7 | 打印日期（华中科技大学复试上机题）   | http://t.cn/E9YP2a8 |
| 例题2.8 | 日期累加（北京理工大学复试上机题）   | http://t.cn/E9Yw0Cr |
| 习题2.6 | 日期差值（上海交通大学复试上机题）   | http://t.cn/E9Yz0LE |
| 习题2.7 | Day of Week（清华大学复试上机题）    | http://t.cn/E9YZLbi |
| 习题2.8 | 日期类（北京理工大学复试上机题）     | http://t.cn/E9RJUp4 |

#### 3. 其他模拟

|          | 题目                               | 地址                |
| -------- | ---------------------------------- | ------------------- |
| 例题2.9  | 剩下的树（清华大学复试上机题）     | http://t.cn/E9ufYo5 |
| 例题2.10 | 手机键盘（清华大学复试上机题）     | http://t.cn/E9ulcIc |
| 例题2.11 | XXX定律（浙江大学复试上机题）      | http://t.cn/E937wDs |
| 习题2.9  | Grading（浙江大学复试上机题）      | http://t.cn/E9rDPSq |
| 习题2.10 | 路径打印（上海交通大学复试上机题） | http://t.cn/E9dvHs4 |
| 习题2.11 | 坠落的蚂蚁（北京大学复试上机题）   | http://t.cn/E9dhoRA |

## 第3章 排序与查找

### 3.1 排序

> 1. 冒泡排序
>
>    ```C
>    int num[n] = {...};
>    for(int i=0;i<n-1;i++)
>      for(int j=0;j<n-1-i;j++)
>        if(valid(num[j])) operate();
>    ```
>
> 2. 冒泡排序是稳定的算法，所以在“相同条件再排序问题”很好用！

|         | 题目                               | 地址                |
| ------- | ---------------------------------- | ------------------- |
| 例题3.1 | 排序（清华大学复试上机题）         | http://t.cn/E9dLx5K |
| 例题3.2 | 成绩排序（清华大学复试上机题）     | http://t.cn/E9d3ysv |
| 例题3.3 | 成绩排序2（清华大学复试上机题）    | http://t.cn/E9gyHM1 |
| 习题3.1 | 特殊排序（华中科技大学复试上机题） | http://t.cn/E9gio39 |
| 习题3.2 | 整数奇偶排序（北京大学复试上机题） | http://t.cn/E9glPvp |
| 习题3.3 | 小白鼠排队（北京大学复试上机题）   | http://t.cn/E9gXh9Z |
| 习题3.4 | 奥运排序问题（浙江大学复试上机题） | http://t.cn/E9gYpyl |

### 3.2 查找

> 1. 在查找前可以先进行冒泡排序🫧
>
> 2. 更快的可以进行二分查找
>
>    ```C
>    bool binary(int *num, int len, int target){
>      int start = 0;
>      int end = len-1;
>      int mid;
>      while(start<=end){
>        mid = (start+end)/2;
>        if(num[target]<num[mid]) end = mid-1;
>        else if(num[target]>num[mid]) start = mid+1;
>        else return true;
>      }
>      return false;
>    }
>    ```
>
> 3. 字符串查重复字符次数：每个字符出现的次数是n，可以用字符对应的多整数作为int数组下标
>
>    ```C
>    int count[100];
>    char str[100];
>    for(int i=0;i<strlen(str);i++)
>    	num[str[i]]++;
>    ```

|         | 题目                                 | 地址                |
| ------- | ------------------------------------ | ------------------- |
| 例题3.4 | 找x（哈尔滨工业大学复试上机题）      | http://t.cn/E9gHFnS |
| 例题3.5 | 查找（北京邮电大学复试上机题）       | http://t.cn/E9g8aaR |
| 习题3.5 | 找最小数（北京邮电大学复试上机题）   | http://t.cn/E9gekWa |
| 习题3.6 | 打印极值点下标（北京大学复试上机题） | http://t.cn/E9ehDw4 |
| 习题3.7 | 找位置（华中科技大学复试上机题）     | http://t.cn/E9eh4jY |

## 第4章 字符串

### 4.1 字符串

> 1. 善用string.h
>
>    ```C
>    /** 字符串比较
>     * -1: str1<str2
>     * 1:  str1>str2
>     * 0:  str1=str2
>     */
>    int strcmp(const char *str1, const char *str2);
>    
>    // 字符串长度
>    size_t strlen(const char *str);
>    
>    // 字符串复制（从src到dest）
>    char *strcpy(char *dest, const char *src)
>      
>    // 字符串拼接（第一个变成1+2）
>    char *strcat(char *dest, const char *src)
>      
>    // 字符串第一次出现某个字符
>    char *strchr(const char *str, int c)
>    ```
>
> 2. 要擅长使用C++
>
>    ```C++
>    #include <iostream>
>    #include <cstdio>
>    #include <string>
>    using namespace std;
>    int main(){
>      string str;
>      while(getline(cin,str)){}
>    }
>    ```
>
>    

### 4.2 字符串处理

|         | 题目                                     | 地址                 |
| ------- | ---------------------------------------- | -------------------- |
| 例题4.1 | 特殊乘法（清华大学复试上机题）           | http://t.cn/Ai8by9vW |
| 例题4.2 | 密码翻译（北京大学复试上机题）           | http://t.cn/Ai8bGaIx |
| 例题4.3 | 简单密码（北京大学复试上机题）           | http://t.cn/Ai8bih2z |
| 例题4.4 | 统计字符（浙江大学复试上机题）           | http://t.cn/Ai8fvq4I |
| 例题4.5 | 字母统计（上海交通大学复试上机题）       | http://t.cn/Ai8VB72e |
| 习题4.1 | skew数（北京大学复试上机题）             | http://t.cn/Ai8IALKI |
| 习题4.2 | 单词替换（北京大学复试上机题）           | http://t.cn/Ai8Iycp6 |
| 习题4.3 | 首字母大写（北京大学复试上机题）         | http://t.cn/Ai8I2hco |
| 习题4.4 | 浮点数加法（北京大学复试上机题）         | http://t.cn/Ai8I4v0j |
| 习题4.5 | 后缀字符串排序（上海交通大学复试上机题） | http://1t.click/VGP  |

### 4.3 字符串匹配

|         | 题目                                      | 地址                                           |
| ------- | ----------------------------------------- | ---------------------------------------------- |
| 例题4.6 | Number Sequence                           | http://acm.hdu.edu.cn/showproblem.php?pid=1711 |
| 例题4.7 | Oulipo                                    | http://poj.org/problem?id=3461                 |
| 习题4.6 | 字符串匹配（北京航空航天大学复试上机题）  | http://1t.click/VGG                            |
| 习题4.7 | String Matching（上海交通大学复试上机题） | http://1t.click/VGH                            |

## 第5章 数据结构一

### 5.1 向量


|         | 题目                                     | 地址                 |
| ------- | ---------------------------------------- | -------------------- |
| 例题5.1 | 完数与盈数（清华大学复试上机题）           | http://t.cn/AiKEyQWW |

### 5.2 队列

> 1. 构造辅助队列
>
>    ```C
>    typedef struct{
>      int data[300];
>      int start;
>      int end;
>      int len;
>    }Queue;
>    
>    void InitQueue(Queue &Q){
>      for(int i=0;i<=300;i++) Q.data[i] = 0;
>      Q.start = 0;
>      Q.end = 0;
>      Q.len = 0;
>    }
>    
>    bool IsEmpty(Queue Q){
>      return Q.start == Q.end;
>    }
>    
>    bool InQueue(Queue &Q,int n){
>      Q.data[Q.end]=n;       // 1. 入队
>      Q.end = (Q.end+1)%300; // 2. 指针
>      Q.len++;               // 3. 长度
>      return true;
>    }
>    
>    int DeQueue(Queue &Q){
>      if(IsEmpty(Q)) return -1;
>      int temp=Q.data[Q.start]; // 1. 入队
>      Q.start = (Q.start+1)%300;// 2. 指针
>      Q.len--;                  // 3. 长度
>      return temp;
>    }
>    ```
>
> 

|         | 题目           | 地址                                      |
| ------- | -------------- | ----------------------------------------- |
| 例题5.2 | 约瑟夫问题NO.2 | http://bailian.openjudge.cn/practice/3254 |
| 例题5.3 | 猫狗收容所     |                                           |

### 5.3 栈

> 1. 构造栈
>
>    ```C
>    typedef struct{
>    	int num[300];
>      int top;
>    }Stack;
>    
>    bool IsEmpty(Stact S){
>      return S.top == 0;
>    }
>    
>    bool InStack(Stack &S, int n){
>      num[S.top++]=n;
>      return true;
>    }
>    
>    int DeStack(Stack &S){
>      return num[S.top--];
>    }
>    ```
>
>    

|         | 题目                                                    | 地址                                    |
| ------- | ------------------------------------------------------- | --------------------------------------- |
| 例题5.4 | Zero-complexity Transposition（上海交通大学复试上机题） | http://t.cn/AiKa20bt                    |
| 例题5.5 | 括号匹配问题                                            | http://ccnu.openjudge.cn/practice/1978/ |
| 例题5.6 | 简单计算器（浙江大学复试上机题）                        | http://t.cn/AiKoGS94                    |
| 习题5.1 | 堆栈的使用（吉林大学复试上机题）                        | http://t.cn/AiKKM6F6                    |
| 习题5.2 | 计算表达式（上海交通大学复试上机题）                    | http://t.cn/AiKKJjJ5                    |

## 第6章 数学问题

### 6.1 进制转换

> 1. 十转二
>
>    ```C
>    #include<stdio.h>
>    
>    void d_to_b(int d){
>      int i;
>      int b[32];
>      for(i=0;d>1;i++){
>        b[32-i]= d%2;
>        d/=2;
>      }
>      b[32-i]=d;
>      for(int j=32-i;j<=32;j++)
>        printf("%d",b[j]);
>      printf("\n");
>    }
>    
>    int main(){
>      d_to_b(1);
>      d_to_b(2);
>      d_to_b(4);
>      d_to_b(8);
>      d_to_b(16);
>      d_to_b(32);
>      return 0;
>    }
>    
>    1
>    10
>    100
>    1000
>    10000
>    100000
>    [Finished in 618ms]
>    ```
>
>    

|         | 题目                                     | 地址                 |
| ------- | ---------------------------------------- | -------------------- |
| 例题6.1 | 二进制数（北京邮电大学复试上机题）           | http://t.cn/AiCuKTOv |
| 例题6.2 | 进制转换（清华大学复试上机题）           | http://t.cn/AiCuoPRO |
| 例题6.3 | 十进制与二进制（清华大学复试上机题）           | http://t.cn/AiCuoHKg |
| 例题6.4 | 进制转换2（清华大学复试上机题）           | http://t.cn/AiCuKG7E |
| 习题6.1 | 八进制（华中科技大学复试上机题）             | http://t.cn/AiCu0lHe |
| 习题6.2 | 又一版A+B（浙江大学复试上机题）           | http://t.cn/AiCuOSWv |
| 习题6.3 | 进制转换（北京大学复试上机题）         | http://t.cn/AiCuig9B |
| 习题6.4 | 数制转换（北京大学复试上机题）         | http://t.cn/AiCu6ne4 |

### 6.2 最大公约数与最小公倍数

> 1. 最大公约数
>
>    ```C
>    int GCD(int a,int b){
>      if(b==0) return a;
>      else return GCD(b,a%b);
>    }
>    ```
>
> 2. 质数：小于n的质数，只需要对比到sqrt(n)的数就好了
>
> 3. math
>
>    ```C
>    #include <math.h>
>    int main(){
>      sqrt(n); // 开方
>      power(x,y);// x的y次方
>      return 0;
>    }
>    ```
>
>    

|         | 题目                                     | 地址                 |
| ------- | ---------------------------------------- | -------------------- |
| 例题6.5 | 最大公约数（哈尔滨工业大学复试上机题）           | http://t.cn/AiCuWLTS |
| 例题6.6 | 最小公倍数                              | http://acm.hdu.edu.cn/showproblem.php?pid=1108 |
| 习题6.5 | 最简真分数（北京大学复试上机题）         | http://t.cn/AiCua2g8 |

### 6.3 质数

|         | 题目                                     | 地址                 |
| ------- | ---------------------------------------- | -------------------- |
| 例题6.7 | 素数判定（哈尔滨工业大学复试上机题）           | http://t.cn/AiCuWE0Q |
| 例题6.8 | 素数                              | http://t.cn/AiCulqtW |
| 习题6.6 | Prime Number（上海交通大学复试上机题）         | http://t.cn/AiCulrSh |

### 6.4 分解质因数

|         | 题目                                     | 地址                 |
| ------- | ---------------------------------------- | -------------------- |
| 例题6.9 | 质因数的个数（清华大学复试上机题）           | http://t.cn/Aip7J0Oo |
| 习题6.7 | 约数的个数（清华大学复试上机题）                              | http://t.cn/Aip7dTUp |
| 习题6.8 | 整除问题（上海交通大学复试上机题）         | http://t.cn/Aip7eHBD |


### 6.5 快速幂

|         | 题目                                     | 地址                 |
| ------- | ---------------------------------------- | -------------------- |
| 例题6.10 | 人见人爱A^B           | http://acm.hdu.edu.cn/showproblem.php?pid=2035 |
| 习题6.9 | 求root(N,K)（清华大学复试上机题）         | http://t.cn/AipAw4B1 |

### 6.6 矩阵与矩阵快速幂

|         | 题目                                     | 地址                 |
| ------- | ---------------------------------------- | -------------------- |
| 例题6.11 | 计算两个矩阵的乘积（哈尔滨工业大学复试上机题）           | http://t.cn/Aip450PJ |
| 例题6.12 | 矩阵幂（北京邮电大学复试上机题）           | http://t.cn/Aip4T3HX |
| 习题6.10 | A+B for Matrices（浙江大学复试上机题）         | http://t.cn/Aipb7GBG |
| 习题6.11 | 递推数列（清华大学复试上机题）         | http://t.cn/AipbZ2sS |

### 6.7 高精度整数

|         | 题目                                     | 地址                 |
| ------- | ---------------------------------------- | -------------------- |
| 例题6.13 | a+b（华中科技大学复试上机题）           | http://t.cn/AipaWiSG |
| 例题6.14 | N的阶乘（清华大学复试上机题）           | http://t.cn/AipaBKQJ |
| 习题6.12 | 数字阶梯求和（哈尔滨工业大学复试上机题）         | http://t.cn/Aipak8BQ |
| 习题6.13 | 大整数的因子（北京大学复试上机题）         | http://t.cn/AipaFCJE |

## 第7章 贪心策略

### 7.1 简单贪心

|         | 题目                             | 地址                                           |
| ------- | -------------------------------- | ---------------------------------------------- |
| 例题7.1 | 鸡兔同笼（北京大学复试上机题）   | http://t.cn/E9ewERU                            |
| 例题7.2 | FatMouse' Trade                  | http://acm.hdu.edu.cn/showproblem.php?pid=1009 |
| 例题7.3 | Senior's Gun                     | http://acm.hdu.edu.cn/showproblem.php?pid=5281 |
| 习题7.1 | 代理服务器（清华大学复试上机题） | http://t.cn/E9emuS9                            |

### 7.2 区间贪心

|         | 题目                                         | 地址                                           |
| ------- | -------------------------------------------- | ---------------------------------------------- |
| 例题7.4 | 今年暑假不AC                                 | http://acm.hdu.edu.cn/showproblem.php?pid=2037 |
| 例题7.5 | Case of Fugitive                             | http://codeforces.com/problemset/problem/555/B |
| 习题7.2 | To Fill or Not to Fill（清华大学复试上机题） | http://dwz.date/b2tj                           |

## 第8章 递归与分治

### 8.1 递归策略

|         | 题目                                 | 地址                                           |
| ------- | ------------------------------------ | ---------------------------------------------- |
| 例题8.1 | n的阶乘（清华大学复试上机题）        | http://t.cn/Ai0ocOUY                           |
| 例题8.2 | 汉诺塔Ⅲ                              | http://acm.hdu.edu.cn/showproblem.php?pid=2064 |
| 习题8.1 | 杨辉三角形（西北工业大学复试上机题） | http://t.cn/Ai0KcLRI                           |
| 习题8.2 | 全排列（北京大学复试上机题）         | http://t.cn/Ai0K0hXZ                           |

### 8.2 分治法

|         | 题目                                | 地址                 |
| ------- | ----------------------------------- | -------------------- |
| 例题8.3 | Fibonacci（上海交通大学复试上机题） | http://t.cn/Ai0K3tU5 |
| 例题8.4 | 二叉树（北京大学复试上机题）        | http://t.cn/Ai0Ke6I0 |
| 习题8.3 | 2的幂次方（上海交通大学复试上机题） | http://suo.im/5D5hnX |


## 第9章 搜索

### 9.1 宽度优先搜索

|         | 题目                             | 地址                |
| ------- | -------------------------------- | ------------------- |
| 例题9.1 | Catch That Cow   | http://poj.org/problem?id=3278 |
| 例题9.2 | Find The Multiple  | http://poj.org/problem?id=1426 |
| 习题9.1 | 玛雅人的密码 | http://t.cn/Ai0lUhJj |

### 9.2 深度优先搜索

|         | 题目                                         | 地址     |
| ------- | -------------------------------------------- | -------- |
| 例题9.3 | A Knights's Journey           | http://poj.org/problem?id=2488 |
| 例题9.4 | Square                     | http://poj.org/problem?id=2362 |
| 习题9.1 | 神奇的口袋（北京大学复试上机题） |http://t.cn/Ai0u0GUz |
| 习题9.2 | 八皇后（北京大学复试上机题） |http://t.cn/Ai0uOazs |

## 第10章 数据结构二

### 10.1 二叉树

|          | 题目                                 | 地址                 |
| -------- | ------------------------------------ | -------------------- |
| 例题10.1 | 二叉树遍历（清华大学复试上机题）     | http://t.cn/AiKuUTlX |
| 例题10.2 | 二叉树遍历（华中科技大学复试上机题） | http://t.cn/AiKgDfLU |

### 10.2 二叉排序树

|          | 题目                                 | 地址                 |
| -------- | ------------------------------------ | -------------------- |
| 例题10.3 | 二叉排序树（华中科技大学复试上机题   | http://t.cn/Ai9PAkkv |
| 例题10.4 | 二叉排序树（华中科技大学复试上机题） | http://t.cn/AiKD0L5V |
| 习题10.1 | 二叉搜索树（浙江大学复试上机题）     | http://t.cn/Ai9PUJtK |

### 10.3 优先队列

|          | 题目                                    | 地址                 |
| -------- | --------------------------------------- | -------------------- |
| 例题10.5 | 复数集合（北京邮电大学复试上机题）      | http://t.cn/Ai98yYlt |
| 例题10.6 | 哈夫曼树（北京邮电大学复试上机题）      | http://t.cn/AiCuGMki |
| 习题10.2 | 查找第K小的数（北京邮电大学复试上机题） | http://t.cn/AiCu5hcK |
| 习题10.3 | 搬水果（吉林大学复试上机题）            | http://t.cn/AiCu5nsQ |

```C
#include <stdio.h>
//http://t.cn/AiCuGMki
void swap(int &a,int &b){
    int p = a;
    a = b;
    b = p;
}

int main() {
    int n,num[1000];
    int count=0;
    while (scanf("%d", &n) != EOF) {
        for(int i=0;i<n;i++)
            scanf("%d",&num[i]);
        for(int i=0;i<n-1;i++)
            for(int j=0;j<n-i-1;j++)
                if(num[j]>num[j+1]) swap(num[j],num[j+1]);
        for(int i=0;i<n-1;i++){
            for(int j=i;j<n-1;j++)
                if(num[j]>num[j+1]) swap(num[j],num[j+1]);
            count += num[i]+num[i+1];
            num[i+1] += num[i];
        }
        printf("%d\n",count);
    }
    return 0;
}
```



### 10.4 散列表

|          | 题目                                     | 地址                 |
| -------- | ---------------------------------------- | -------------------- |
| 例题10.7 | 查找学生信息（清华大学复试上机题）       | http://t.cn/AiCuVIuY |
| 例题10.8 | 魔咒词典（浙江大学复试上机题）           | http://t.cn/AiCufczt |
| 例题10.9 | 字串计算（北京大学复试上机题）           | http://t.cn/AiCuJtI5 |
| 习题10.4 | 统计同成绩学生人数（浙江大学复试上机题） | http://t.cn/Ai0u0GUz |
| 习题10.5 | 开门人和关门人(浙江大学复试上机题)       | http://t.cn/AiCuM09f |
| 习题10.6 | 谁是你的潜在朋友（北京大学复试上机题）   | http://t.cn/AiCux4f7 |

## 第11章 图论

### 11.1 概述

### 11.2 并查集

|          | 题目                                 | 地址                 |
| -------- | ------------------------------------ | -------------------- |
| 例题11.1 | 畅通工程（浙江大学复试上机题）       | http://t.cn/AiOvBHj9 |
| 例题11.2 | 连通图（吉林大学复试上机题）         | http://t.cn/AiO77VoA  |
| 例题11.3 | Is It A Tree?（北京大学复试上机题）  | http://t.cn/AiO7FyDO |
| 习题11.1 | 找出直系亲属（浙江大学复试上机题）   | http://t.cn/AiOzTX5c |
| 习题11.2 | 第一题（上海交通大学复试上机题）     | http://t.cn/AiOhkgMJ |
| 习题11.3 | Head of a Gang（浙江大学复试上机题） | http://t.cn/AiOzQMBH |

### 11.3 最小生成树

|          | 题目                               | 地址                 |
| -------- | ---------------------------------- | -------------------- |
| 例题11.4 | 还是畅通工程（浙江大学复试上机题） | http://t.cn/AiWud0C6 |
| 例题11.5 | 继续畅通工程（浙江大学复试上机题） | http://t.cn/AiW3fcfp |
| 习题11.4 | Freckles（北京大学复试上机题）     | http://t.cn/AiW3Hbqr |
| 习题11.5 | Jungle Roads（北京大学复试上机题） | http://t.cn/AiW33P91 |

### 11.4 最短路径

|          | 题目                               | 地址                                           |
| -------- | ---------------------------------- | ---------------------------------------------- |
| 例题11.6 | 畅通工程续（浙江大学复试上机题）   | http://acm.hdu.edu.cn/showproblem.php?pid=1874 |
| 例题11.7 | 最短路径问题（浙江大学复试上机题） | http://t.cn/AilPbME2                           |
| 习题11.6 | 最短路径（上海交通大学复试上机题） | http://t.cn/AilPCAuL                           |

### 11.5 拓扑排序

|          | 题目         | 地址                                           |
| -------- | ------------ | ---------------------------------------------- |
| 例题11.8 | Legal or Not | http://acm.hdu.edu.cn/showproblem.php?pid=3342 |
| 例题11.9 | 确定比赛名次 | http://acm.hdu.edu.cn/showproblem.php?pid=1285 |

### 11.6 关键路径

|           | 题目                     | 地址                                           |
| --------- | ------------------------ | ---------------------------------------------- |
| 例题11.10 | Instructions Arrangement | http://acm.hdu.edu.cn/showproblem.php?pid=4109 |
| 例题11.11 | p3（清华大学复试上机题） |                                                |

## 第12章 动态规划

### 12.1 递归求解

|          | 题目                                      | 地址                 |
| -------- | ----------------------------------------- | -------------------- |
| 例题12.1 | N阶楼梯上楼问题（华中科技大学复试上机题） | http://t.cn/Aij9Fr3V |
| 习题12.1 | 吃糖果（北京大学复试上机题）              | http://t.cn/AiQsVyKz |

### 12.2 最大连续子序列和

|          | 题目                                 | 地址                 |
| -------- | ------------------------------------ | -------------------- |
| 例题12.2 | 最大序列和（清华大学复试上机题）     | http://t.cn/AiYSlQMU |
| 例题12.3 | 最大子矩阵（北京大学复试上机题）     | http://t.cn/AiYSemJz |
| 习题12.2 | 最大连续子序列（浙江大学复试上机题） | http://t.cn/AiYoUkjP |

### 12.3 最长递增子序列

|          | 题目                                   | 地址                 |
| -------- | -------------------------------------- | -------------------- |
| 例题12.4 | 拦截导弹（北京大学复试上机题）         | http://t.cn/AiYCeV3m |
| 例题12.5 | 最长上升子序列和（北京大学复试上机题） | http://t.cn/AiYNAGD3 |
| 习题12.3 | 合唱队形（北京大学复试上机题）         | http://t.cn/AiYNyHPe |

### 12.4 最长公共子序列

|          | 题目                                  | 地址                                           |
| -------- | ------------------------------------- | ---------------------------------------------- |
| 例题12.6 | Common Subsequence                    | http://acm.hdu.edu.cn/showproblem.php?pid=1159 |
| 习题12.4 | Coincidence（上海交通大学复试上机题） | http://t.cn/AiY03RO5                           |

### 12.5 背包问题

#### 1.  0-1背包

|          | 题目                             | 地址                 |
| -------- | -------------------------------- | -------------------- |
| 例题12.7 | 点菜问题（北京大学复试上机题）   | http://t.cn/AiYOrkXr |
| 习题12.5 | 采药（北京大学复试上机题）       | 地址错               |
| 习题12.6 | 最小邮票数（清华大学复试上机题） | http://t.cn/AiYlwchD |

#### 2. 完全背包

|          | 题目       | 地址                                           |
| -------- | ---------- | ---------------------------------------------- |
| 例题12.8 | Piggy-Bank | http://acm.hdu.edu.cn/showproblem.php?pid=1114 |

#### 3. 多重背包

|          | 题目               | 地址                                           |
| -------- | ------------------ | ---------------------------------------------- |
| 例题12.9 | 珍惜现在，感恩生活 | http://acm.hdu.edu.cn/showproblem.php?pid=2191 |

### 12.6 其他问题

|           | 题目                           | 地址                                                   |
| --------- | ------------------------------ | ------------------------------------------------------ |
| 例题12.10 | The Triangle                   | http://poj.org/problem?id=1163                         |
| 例题12.11 | Monkey Banana Problem          | http://lightoj.com/volume_showproblem.php?problem=1004 |
| 习题12.7  | 放苹果（北京大学复试上机题）   | http://t.cn/AiQsyOnq                                   |
| 习题12.8  | 整数拆分（清华大学复试上机题） | http://t.cn/AiQsUM0Q                                   |





