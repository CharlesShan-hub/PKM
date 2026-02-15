# Image Quantization

通过调整量化级别，展示了不同量化程度对图像的影响，反映了量化过程中图像细节的损失。

![[../assets/quantization.png]]

```python
import numpy as np
import matplotlib.pyplot as plt

def generate_image(level):
    I = np.zeros((16,256))
    for x in range(256):
        n = 2**level         # 一共多少个格子
        length = int(256/n)  # 每个格子有多大
        I[:, x] = int(x/length) / n
    return I/np.max(I)

def plot(index,level):
    plt.subplot(4,1,index+1)
    plt.imshow(generate_image(level), cmap='gray', vmax=1, vmin=0)
    plt.title(f"level = {level}")
    plt.axis('off')
for index,level in enumerate([1,2,4,8]):
    plot(index,level)
plt.show()
```