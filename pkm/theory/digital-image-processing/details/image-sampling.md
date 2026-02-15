
# Image Sampling

下面的案例是模拟“图片采样”的过程，生成了四个不同尺寸的灰度图像，每个图像都是通过余弦函数计算得到的黑白图案，并且将这些图案排列展示出来，来展示不同“分辨率”的图片的采样过程的影响。

![[../assets/sampling.png]]

```python
import numpy as np
import matplotlib.pyplot as plt

def generate_image(width, height):
    I = np.zeros((width, height))
    for x in range(width):
        for y in range(height):
            I[x, y] = np.cos(x/width*2*np.pi) * np.cos(y/height*2*np.pi) * 255
    return I

def plot(index,n):
    plt.subplot(1,4,index+1)
    plt.imshow(generate_image(n, n), cmap='gray')
    plt.title(f"{n}x{n}")
    plt.axis('off')
for i,n in enumerate([5,15,50,1000]):
    plot(i,n)
plt.show()
```