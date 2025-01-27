
# Pixel Transform

> 点运算又可以分为线性点运算和非线性点运算。线性点运算的原值和目标值通过线性方程完成转换，典型的如对比度灰度调整、图像反色都属于线性点运算。非线性点运算对应非线性映射函数，典型的映射包括平方函数、对数函数、截取（窗口函数）​、阈值函数、多值量化函数等。灰度幂次变换、灰度对数变换、阈值化处理、直方图均衡化是较常见的非线性点运算方法。
>
> 1. Gamma Transfrom：Gamma 变换
> 2. 直方图均衡化

***

## Gamma Transform

Gamma变换（幂次变换）：用于改变亮度。

![[../assets/image (66).png]]
<figure><img src="../../.gitbook/assets/image (66).png" alt=""><figcaption></figcaption></figure>

<details>

<summary>Code</summary>

```python
from skimage import data,io,exposure
from matplotlib import pyplot as plt

image=data.coffee()

for i,gamma in enumerate([1,0.2,0.67,25]):
    plt.subplot(1,4,i+1)
    plt.title(f'gamma={gamma}')
    plt.axis('off')
    io.imshow(exposure.adjust_gamma(image,gamma))
plt.show()
```

</details>

***

## Histograms and Histograms Equization

直方图就是图片中不同颜色的占比，是一个统计量。

直方图均衡化的步骤：

1. 求 pdf，也就是直方图。
2. 求 cdf。类似从概率密度函数求概率分布函数。$$cdf[t] = \sum_0^tp[t]$$。
3. 累计概率的 0 到 1，就是颜色的 0 到 1。

![[../assets/image (67).png]]
<figure><img src="../../.gitbook/assets/image (67).png" alt=""><figcaption></figcaption></figure>

<details>

<summary>Code</summary>

```python
import numpy as np
import matplotlib.pyplot as plt
from skimage import data, color

def calculate_histogram(image):
    """计算图像的直方图"""
    # 确定可能的灰度级别
    levels = np.arange(0, 257)
    # 计算并返回直方图
    histogram, _ = np.histogram(image, bins=levels, density=False)
    return histogram

def calculate_cdf(histogram):
    """计算累积分布函数（CDF）"""
    cdf = histogram.cumsum()
    # 归一化CDF
    cdf_normalized = cdf / float(cdf[-1])
    return cdf_normalized

def equalize_histogram(image):
    """均衡化直方图"""
    # 计算原始图像的直方图
    histogram = calculate_histogram(image)
    # 计算CDF
    cdf = calculate_cdf(histogram)
    # 映射原始图像的像素值
    image_equalized = np.interp(image, np.arange(0, 256), cdf * 255)
    return image_equalized.astype('uint8')

# 使用skimage的案例图片：camera
image_camera = np.clip(color.rgb2gray(data.coffee())*255.0,0,255).astype(np.uint8)

# 均衡化图像
image_equalized = equalize_histogram(image_camera)

# 可视化
fig, ax = plt.subplots(2, 3, figsize=(12, 12))

# 原始图像
ax[0, 0].imshow(image_camera, cmap='gray')
ax[0, 0].set_title('Original Image (Camera)')
ax[0, 0].axis('off')

# 原始直方图
ax[0, 1].bar(np.arange(0, 256), calculate_histogram(image_camera))
ax[0, 1].set_title('Histogram of Original Image')
ax[0, 1].set_xlabel('Pixel Value')
ax[0, 1].set_ylabel('Frequency')

# 均衡化后的CDF
ax[0, 2].plot(np.arange(0, 256), calculate_cdf(calculate_histogram(image_camera)))
ax[0, 2].set_title('CDF of Original Image')
ax[0, 2].set_xlabel('Pixel Value')
ax[0, 2].set_ylabel('Cumulative Probability')

# 均衡化后的图像
ax[1, 0].imshow(image_equalized, cmap='gray')
ax[1, 0].set_title('Equalized Image (Camera)')
ax[1, 0].axis('off')

# 均衡化后直方图
ax[1, 1].bar(np.arange(0, 256), calculate_histogram(image_equalized))
ax[1, 1].set_title('Histogram of Equalized Image')
ax[1, 1].set_xlabel('Pixel Value')
ax[1, 1].set_ylabel('Frequency')

# 均衡化后的CDF
ax[1, 2].plot(np.arange(0, 256), calculate_cdf(calculate_histogram(image_equalized)))
ax[1, 2].set_title('CDF of Equalized Image')
ax[1, 2].set_xlabel('Pixel Value')
ax[1, 2].set_ylabel('Cumulative Probability')

plt.tight_layout()
plt.show()

```

</details>
