# Solution Number

## RoadMap

![[../assets/solution-number-drawing|1000]]

继续进行“换句话说”。从单纯的解方程角度，变换到“独立性”和“秩”

1. dependence（独立性）
   1. dependent（独立的）：
      1. $a_1v_1+a_2v_2+⋯+a_nv_n=0$，只有全 0 解（所有 a 都是 0）
      2. $v_i$ 可以被 $\{ v_1, v_2, \ldots, v_{i-1}, v_{i+1}, \ldots, v_n \}$线性表示
   2. independent（不独立）
      1. $a_1v_1+a_2v_2+⋯+a_nv_n=0$，不只有全 0 解
      2. 任何 $v_i$ 都不能被 $\{ v_1, v_2, \ldots, v_{i-1}, v_{i+1}, \ldots, v_n \}$线性表示
      3. $v_i$ 是 0 向量，$n≥1$ （是的，就算只有一个0 向量，也不独立）
   3. 解的数量与独立性
      1. A的列空间独立，则只有唯一解
      2. A的列空间不独立，则有无穷解
      3. 证明“A的列空间不独立，则有无穷解”：
         1. $Ax = b\to A(u+v)=0+b\to Au=0,Av=b$
         2. u来保证齐次，因为A不独立，所以 u 存在，且有无穷个
         3. 前提是有解，所以 v 存在
2. rank（秩）and nullity（核）
   1. rank = 最大的线性相关列的数量
   2. 对于一个 m×n 矩阵 A：$\text{rank}(A)+\text{null}(A)=n$
   3. 满秩 + 有解 = 唯一解



## Reference

\[1] [Linear Algebra Lecture 7: How many solutions?](https://www.youtube.com/watch?v=34HlThINCsc\&list=PLJV\_el3uVTsNmr39gwbyV-0KjULUsN7fW\&index=7)
