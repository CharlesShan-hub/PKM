
# Frequceial Transform

## Transform

### FFT

通过`np.fft.fft2`可以进行图片的傅里叶变换。

![[../assets/image (91).png]]
<figure><img src="../../.gitbook/assets/image (91).png" alt=""><figcaption></figcaption></figure>

<details>

<summary>Code</summary>

```python
import numpy as np
import matplotlib.pyplot as plt
from skimage import data, color

# 使用skimage的案例图片：camera
image = np.clip(color.rgb2gray(data.coffee())*255.0,0,255).astype(np.uint8)

# 图像尺寸
rows, cols = image.shape

# 变换结果
f = np.fft.fft2(image)
fshift = np.fft.fftshift(f)

# 显示原始图像和变换后的图像
fig, axs = plt.subplots(2, 3, figsize=(20, 10))

# 原始图像
axs[0][0].imshow(image, cmap='gray')
axs[0][0].set_title('Original Image')

# 变换后的图像
axs[1][0].imshow(np.log(np.abs(fshift)), cmap='gray')
axs[1][0].set_title('Fourier Transformed Image')

def function_im(m, n):
    N = 256
    x, y = np.meshgrid(np.arange(N), np.arange(N))
    im = np.exp(-2j * np.pi * (m * x / N + n * y / N)).real
    if m == 0 and n == 0:
        im = np.round(im)
    return im

axs[0][1].imshow(function_im(0,1),cmap='gray')
axs[0][1].set_title("(0,1)")
axs[1][1].imshow(function_im(1,0),cmap='gray')
axs[1][1].set_title("(1,0)")
axs[0][2].imshow(function_im(1,1),cmap='gray')
axs[0][2].set_title("(1,1)")
axs[1][2].imshow(function_im(2,3),cmap='gray')
axs[1][2].set_title("(2,3)")

plt.show()

```

</details>

## Filtering

### Ideal Filter

简单的把频域切成高通与低通，会产生“振铃”效应。

![[../assets/image (90).png]]
<figure><img src="../../.gitbook/assets/image (90).png" alt=""><figcaption></figcaption></figure>

<details>

<summary>Code</summary>

```python
from skimage import data
import numpy as np
import matplotlib.pyplot as plt

def freq_trans(image,func=None):
    # Convert the image to the frequency domain
    f = np.fft.fft2(image)
    fshift = np.fft.fftshift(f)
    if func == None: return fshift, image

    # Apply the filter function to the frequency domain
    fshift_filtered = func(fshift)

    # Convert back to the spatial domain
    f_inv = np.fft.ifftshift(fshift_filtered)
    image_filtered = np.fft.ifft2(f_inv)
    return fshift_filtered, image_filtered

def cal_dis(image_shape):
    """Create a high-pass mask."""
    center_width = image_shape[0] // 2
    center_height = image_shape[1] // 2
    x = np.arange(image_shape[0])
    y = np.arange(image_shape[1])
    X, Y = np.meshgrid(x, y)
    distances = np.sqrt((X - center_width)**2 + (Y - center_height)**2)
    return distances

def ideal_high_pass_filter(fshift):
    """High pass filter function."""
    return np.where(cal_dis(fshift.shape)>40, fshift, 0)

def ideal_low_pass_filter(fshift):
    """Low pass filter function."""
    return np.where(cal_dis(fshift.shape)<=40, fshift, 0)

img = data.camera()
f1,m1 = freq_trans(img)
f2,m2 = freq_trans(img, ideal_high_pass_filter)
f3,m3 = freq_trans(img, ideal_low_pass_filter)

plt.subplot(2,3,1)
plt.imshow(m1,cmap='gray')
plt.title("Original Image")
plt.axis('off')
plt.subplot(2,3,2)
plt.imshow(np.real(m2),cmap='gray')
plt.title("High Pass Image")
plt.axis('off')
plt.subplot(2,3,3)
plt.imshow(np.real(m3),cmap='gray')
plt.title("Low Pass Image")
plt.axis('off')
plt.subplot(2,3,4)
plt.imshow(np.log(np.abs(f1)),cmap='gray')
plt.axis('off')
plt.subplot(2,3,5)
plt.imshow(np.log(np.abs(f2)),cmap='gray')
plt.axis('off')
plt.subplot(2,3,6)
plt.imshow(np.log(np.abs(f3)),cmap='gray')
plt.axis('off')
plt.show()
```

</details>

### Butterworth Filter

![[../assets/image (92).png]]
<figure><img src="../../.gitbook/assets/image (92).png" alt=""><figcaption></figcaption></figure>

<details>

<summary>Code</summary>

```python
from skimage import data, filters
import numpy as np
import matplotlib.pyplot as plt

def fft(img):
    f = np.fft.fft2(img)
    return np.fft.fftshift(f)

m1 = data.camera()
f1 = fft(m1)
m2 = filters.butterworth(m1,high_pass=True,cutoff_frequency_ratio=0.04)
f2 = fft(m2)
m3 = filters.butterworth(m1,high_pass=False,cutoff_frequency_ratio=0.04)
f3 = fft(m3)

plt.subplot(2,3,1)
plt.imshow(m1,cmap='gray',vmax=255,vmin=0)
plt.title("Original Image")
plt.axis('off')
plt.subplot(2,3,2)
plt.imshow(m2,cmap='gray',vmax=255,vmin=0) # type: ignore
plt.title("High Pass Image")
plt.axis('off')
plt.subplot(2,3,3)
plt.imshow(m3,cmap='gray') # type: ignore
plt.title("Low Pass Image")
plt.axis('off')
plt.subplot(2,3,4)
plt.imshow(np.log(np.abs(f1)),cmap='gray')
plt.axis('off')
plt.subplot(2,3,5)
plt.imshow(np.log(np.abs(f2)),cmap='gray')
plt.axis('off')
plt.subplot(2,3,6)
plt.imshow(np.log(np.abs(f3)),cmap='gray')
plt.axis('off')
plt.tight_layout()
plt.show()
```

</details>

## Wavelet

Haar 小波基函数，(a) 为缩放因子，(b) 为平移因子

$$
\psi_{a,b}(x)=|a|^{-1/2}\psi\left(\frac{x-b}{a}\right)
$$

对于离散小波：i为缩放因子，j为平移因子

$$
a=2^j, b=ia
$$

$$
\phi_j^{i}(x)=2^{j/2}\phi(2^j x-i)
$$

![[../assets/image (111).png]]
<figure><img src="../../.gitbook/assets/image (111).png" alt=""><figcaption><p>[1]</p></figcaption></figure>

## Reference

\[1] [https://mathworld.wolfram.com/HaarFunction.html](https://mathworld.wolfram.com/HaarFunction.html)
