![image](../assets/laplacian.png)

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
