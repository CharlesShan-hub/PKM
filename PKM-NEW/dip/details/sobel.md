![image](../assets/image%20(53).png)

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
