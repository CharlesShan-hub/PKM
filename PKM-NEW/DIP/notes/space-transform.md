
# Space Transform

---
## Overview

![[../assets/space-transform-drawing|1000]]

***

## 卷积

一维卷积：反转，相乘相加。假设有两个一维连续信号进行卷积，公式如下。

$$
(g * f)(t) = \int_{-\infty}^{\infty} f(\tau) h(t - \tau) \, d\tau
$$

二维卷积其实是“相关”，因为缺少了反转的这一步骤，但是由于卷积核大部分都是对称的，所以可以忽略这一条件。所以图像卷积就是对应位置相乘相加！图片的卷积公式如下。

$$
T(x, y) = \sum_{i=-a}^{b} \sum_{j=-a}^{b} I(x + i, y + j) k(i, j)
$$

## 降噪/平滑

### Box

均值滤波器（盒式滤波器），就是某个“方块”内的像素求均值。

$$
k = \frac{1}{mn}\begin{bmatrix} 1&1&...&1\\1&1&...&1\\...&...&...&...\\1&1&...&1\end{bmatrix}_{mn}
$$

![[../assets/image (49).png]]
<figure><img src="../../.gitbook/assets/image (49).png" alt=""><figcaption></figcaption></figure>

<details>

<summary>Code</summary>

```python
from matplotlib import pyplot as plt
from scipy.ndimage import convolve
import skimage.data as data
import numpy as np

image = data.camera().astype(np.float32)

convolved_image1 = convolve(image, np.ones((3,3))/9.0, mode='reflect')
convolved_image2 = convolve(image, np.ones((5,5))/25.0, mode='reflect')

plt.figure(figsize=(10, 5))
plt.subplot(1, 3, 1)
plt.imshow(image, cmap='gray')
plt.title('Original Image')
plt.axis('off')

plt.subplot(1, 3, 2)
plt.imshow(np.abs(convolved_image1), cmap='gray')
plt.title('Convolved by Box(3,3)')
plt.axis('off')

plt.subplot(1, 3, 3)
plt.imshow(np.abs(convolved_image2), cmap='gray')
plt.title('Convolved by Box(5,5)')
plt.axis('off')

plt.tight_layout()
plt.show()
```

</details>

### Gaussian

Box 太平均了，边缘损失严重，为了提升“保边”效果，进行高斯加权平均。

$$
G(x,y)=\frac{1}{2\pi\sigma^2}e^{-\frac{x^2+y^2}{2\sigma^2}}
$$

$$
W(i,j) = \frac{G(i,j)}{\sum_{i=-a}^{a}\sum_{i=-b}^{b}G(i,j)}
$$

![[../assets/image (50).png]]
<figure><img src="../../.gitbook/assets/image (50).png" alt=""><figcaption></figcaption></figure>

<details>

<summary>Code</summary>

```python
from matplotlib import pyplot as plt
from scipy.ndimage import convolve
import skimage.data as data
import numpy as np

image = data.camera().astype(np.float32)

k1 = np.array([[1,2,1],[2,4,2],[1,2,1]])
k2 = np.array([[1, 4, 7, 4,1],
               [4,16,26,16,4],
               [7,26,41,26,7],
               [4,16,26,16,4],
               [1, 4, 7, 4,1]])

convolved_image1 = convolve(image, k1, mode='reflect')
convolved_image2 = convolve(image, k2, mode='reflect')

plt.figure(figsize=(10, 5))
plt.subplot(1, 3, 1)
plt.imshow(image, cmap='gray')
plt.title('Original Image')
plt.axis('off')

plt.subplot(1, 3, 2)
plt.imshow(np.abs(convolved_image1), cmap='gray')
plt.title('Convolved by Gaussian(3,3)')
plt.axis('off')

plt.subplot(1, 3, 3)
plt.imshow(np.abs(convolved_image2), cmap='gray')
plt.title('Convolved by Gaussian(5,5)')
plt.axis('off')

plt.tight_layout()
plt.show()
```

</details>

### Mean

以上滤波器均为线性滤波，而中值滤波是一种基于统计的非线性滤波，它是椒盐噪声的“特效药”。
![[../assets/image (51).png]]
<figure><img src="../../.gitbook/assets/image (51).png" alt=""><figcaption></figcaption></figure>

<details>

<summary>Code</summary>

```python
from matplotlib import pyplot as plt
from skimage import data, util, filters
import numpy as np

image = data.camera()

noisy_image = util.random_noise(image, mode='s&p',rng=None,clip= True)

filtered_image = filters.median(noisy_image)

plt.figure(figsize=(10, 5))
plt.subplot(1, 3, 1)
plt.imshow(image, cmap='gray')
plt.title('Original Image')
plt.axis('off')

plt.subplot(1, 3, 2)
plt.imshow(np.abs(noisy_image), cmap='gray')
plt.title('Noisy Image')
plt.axis('off')

plt.subplot(1, 3, 3)
plt.imshow(filtered_image, cmap='gray')
plt.title('Filtered Image')
plt.axis('off')

plt.tight_layout()
plt.show()
```

</details>

## 边缘

### Roberts

2x2大小的求边缘。

$$
G_x = \begin{bmatrix} -1 & 0 \\ 0 & 1 \end{bmatrix}
$$

$$
G_y = \begin{bmatrix} 0 & -1 \\ 1 & 0 \end{bmatrix}
$$

![[../assets/image (52).png]]
<figure><img src="../../.gitbook/assets/image (52).png" alt=""><figcaption></figcaption></figure>

<details>

<summary>Code</summary>

```python
from skimage import data, filters
from matplotlib import pyplot as plt
import numpy as np

img = data.camera()

img_robert_pos = filters.roberts_pos_diag(img)
img_robert_neg = filters.roberts_neg_diag(img)
# ROBERTS_PD_WEIGHTS = np.array([[1, 0],
#                                [0, -1]], dtype=np.float64)
# ROBERTS_ND_WEIGHTS = np.array([[0, 1],
#                                [-1, 0]], dtype=np.float64)
img_robert = filters.roberts(img)
# out = np.sqrt(roberts_pos_diag(image, mask) ** 2 +
#                 roberts_neg_diag(image, mask) ** 2)
# out /= np.sqrt(2)

def plot(n,i,title,img):
    plt.subplot(1, n, i+1)
    plt.imshow(np.abs(img), cmap='gray')
    plt.title(title)
    plt.axis('off')

for i,(title,im) in enumerate(zip(
    ['Original Image','Roberts pos','Roberts neg','Roberts'],
    [img,img_robert_pos,img_robert_neg,img_robert])):
    plot(4,i,title,im)

plt.tight_layout()
plt.show()
```

</details>

### Sobel

3x3 大小的边缘

$$
G_x = \begin{bmatrix} -1 & -2 & -1 \\ 0 & 0 & 0 \\ 1 & 2 & 1 \end{bmatrix}
$$

$$
G_y = \begin{bmatrix} -1 & 0 & 1 \\ -2 & 0 & 2 \\ -1 & 0 & 1 \end{bmatrix}
$$

![[../assets/image (53).png]]
<figure><img src="../../.gitbook/assets/image (53).png" alt=""><figcaption></figcaption></figure>

<details>

<summary>Code</summary>

```python
from skimage import data, filters
from matplotlib import pyplot as plt
import numpy as np

img = data.camera()

img_sobel_h = filters.sobel_h(img)
img_sobel_v = filters.sobel_v(img)
# SOBEL_EDGE = np.array([1, 0, -1])
# SOBEL_SMOOTH = np.array([1, 2, 1]) / 4
# HSOBEL_WEIGHTS = SOBEL_EDGE.reshape((3, 1)) * SOBEL_SMOOTH.reshape((1, 3))
# VSOBEL_WEIGHTS = HSOBEL_WEIGHTS.T
img_sobel = filters.sobel(img)

def plot(n,i,title,img):
    plt.subplot(1, n, i+1)
    plt.imshow(np.abs(img), cmap='gray')
    plt.title(title)
    plt.axis('off')

for i,(title,im) in enumerate(zip(
    ['Original Image','Sobel H','Sobel V','Sobel'],
    [img,img_sobel_h,img_sobel_v,img_sobel])):
    plot(4,i,title,im)

plt.tight_layout()
plt.show()
```

</details>

### Laplacian

Sobel 和 Robert 把 3x3 或者 2x2 的区域当成一个大像素，算这个像素内部的梯度。Laplacian 换了一个角度，找一个 3x3 的区域，算这个区域中心往外的梯度。另外，实践中，尝尝采用中心权重为正的形式，虽然按照梯度公式中心应该是负。

$$
G = \begin{bmatrix} 0 & -1 & 0 \\ -1 & 4 & -1 \\ 0 & -1 & 0 \end{bmatrix}
$$

或者加上四个对角线方向

$$
G = \begin{bmatrix} -1 & -1 & -1 \\ -1 & 8 & -1 \\ -1 & -1 & -1 \end{bmatrix}
$$

另外，可以把边缘加到原图上得到锐化图像。

![[../assets/image (56).png]]
<figure><img src="../../.gitbook/assets/image (56).png" alt=""><figcaption></figcaption></figure>

<details>

<summary>Code</summary>

{% code fullWidth="false" %}
```python
from skimage import data, filters
from matplotlib import pyplot as plt
import numpy as np

img = data.camera()
lap_img = filters.laplace(img)*255

def plot(n,i,title,img):
    plt.subplot(1, n, i+1)
    plt.imshow(np.abs(img), cmap='gray',vmin=0,vmax=255)
    plt.title(title)
    plt.axis('off')

for i,(title,im) in enumerate(zip(
    ['Original Image','Laplace Edge','Origin+Edge','Origin+2Edge'],
    [img,lap_img,lap_img+img,2*lap_img+img])):
    plot(4,i,title,im)

plt.tight_layout()
plt.show()
```
{% endcode %}

</details>
