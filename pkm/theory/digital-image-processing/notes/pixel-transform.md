# Pixel Transform

> 点运算又可以分为线性点运算和非线性点运算。线性点运算的原值和目标值通过线性方程完成转换，典型的如对比度灰度调整、图像反色都属于线性点运算。非线性点运算对应非线性映射函数，典型的映射包括平方函数、对数函数、截取（窗口函数）​、阈值函数、多值量化函数等。灰度幂次变换、灰度对数变换、阈值化处理、直方图均衡化是较常见的非线性点运算方法。
>
> 1. Gamma Transfrom：Gamma 变换
> 2. 直方图均衡化

***
## Gamma Transform

Gamma变换（幂次变换）：用于改变亮度。👉 [代码](../details/gamma-transform.md)

![image](../assets/gamma-transform.png)

***
## Histograms and Histograms Equization

直方图就是图片中不同颜色的占比，是一个统计量。

直方图均衡化的步骤：

1. 求**概率密度函数**（Probability Density Function, PDF），也就是直方图。
2. 求**累积分布函数**（Cumulative Distribution Function, CDF）。类似从概率密度函数求概率分布函数。$$cdf[t] = \sum_0^tp[t]$$
3. 累计概率的 0 到 1，就是颜色的 0 到 1。

![histograms-equization](../assets/histograms-equization.png) 👉 [代码](../details/histograms-equization.md)
