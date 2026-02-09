# Image Basic

---
## Overview

![PKM-NEW/dip/assets/dip-image-drawing|1000](PKM-NEW/dip/assets/dip-image-drawing.md)

***
## Basic Concepts
### Image

* 图像就是数组，每个像素点的颜色是响应值。
* skimage 库中的data模块有很多预设的图片：👉 [data](../../python/library/skimage/data.md)

### Sampling

* 采样：从连续信号到离散信号。
* 通过不同尺寸的灰度图像，展示不同采样对图片的影响：👉 [image-sampling](PKM-NEW/dip/details/image-sampling.md)
	![PKM-NEW/dip/assets/sampling.png](PKM-NEW/dip/assets/sampling.png)

### Quantization

* 量化：用多少比特代表每个像素的颜色。
* 不同量化级别对图片颜色的影响：👉 [image-quantization](PKM-NEW/dip/details/image-quantization.md)
	![PKM-NEW/dip/assets/quantization.png](PKM-NEW/dip/assets/quantization.png)

### Neighbor

* 4 邻域(上下左右)
* D 邻域(四个角)
* 8 邻域(4+D)

### Distance

$(x,y)$与$(s,t)$的距离：

*  欧氏距离：$$D_e = \sqrt{(x-s)^2+(x-t)^2}$$
* $D_4$距离：$$D_4 = |x-s|+|y-t|$$
* $D_8$距离：$$D_8 = \max(|x-s|+|y-t|)$$