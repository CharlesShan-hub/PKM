![image](../assets/gaussian.png)

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
