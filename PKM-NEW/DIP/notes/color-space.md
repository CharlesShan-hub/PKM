
# Color Space

---
## Overview

![[../assets/color-space-drawing|1000]]
***

## Color Space

### LMS

光是电磁波，按照频率可以绘制出光谱。人眼的三种视锥细胞分别可以吸收三种频率的光。自然界各种频率的光，对于人眼而言，只要转换成三种细胞的吸收情况就可以了。

![[../assets/retina.png]]
LMS Response over the light wavelength (from Wikipedia). L is roughly centered on red, M on green and S on blue. Note that the responses overlap significantly, especially for the L and M cones.[1]
<!--https://upload.wikimedia.org/wikipedia/commons/d/d1/Cone_spectral_sensitivities.png-->

人眼的三种视锥细胞对光的响应值的公式如下\[3]，视锥响应函数![{\displaystyle {\bar {l\}}(\lambda ),{\bar {m\}}(\lambda ),{\bar {s\}}(\lambda )}](https://wikimedia.org/api/rest\_v1/media/math/render/svg/1b09aeb060e8ce50c6fcaa63ca4e6ee62ed0f10a) 是LMS颜色空间的颜色匹配函数：

<figure><img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/a0f66c09f32a2db12739fe49d7ce13f13c36b031" alt=""><figcaption></figcaption></figure>

<figure><img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/8bf4b90785233c594e12ac69e4aad251fb41abfd" alt=""><figcaption></figcaption></figure>

<figure><img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/0a45c5b2f886a77529cd13f9bff0c8104e1c7a8a" alt=""><figcaption></figcaption></figure>

LMS代表Long（长波长，对应红色）、Medium（中波长，对应绿色）和Short（短波长，对应蓝色）。建立一个坐标系，坐标轴是三种细胞对某种光刺激的响应值。然后扫描光谱，把不同频率的光对应的响应值绘制在坐标系中。

<figure><img src="../../.gitbook/assets/image (57).png" alt="https://commons.wikimedia.org/wiki/File:3D_Graph_of_LMS_Color_Space.png"><figcaption><p><a href="https://commons.wikimedia.org/wiki/File:3D_Graph_of_LMS_Color_Space.png">https://commons.wikimedia.org/wiki/File:3D_Graph_of_LMS_Color_Space.png</a> [2]</p></figcaption></figure>

上图的边缘就代表了所有的纯色。利用这些纯色相互组合，就可以构造出所有的人可以看到的颜色。提现在图中，就是上图中的任意两点，连成一条线，这条线就是可以被这两个纯色插值出来的所有颜色。

<figure><img src="../../.gitbook/assets/image (59).png" alt="" width="375"><figcaption><p>https://www.bilibili.com/video/BV1U34y1G7wa/?t=1673</p></figcaption></figure>

以上我们就得到了所有的人眼可见的颜色。但是注意，还有好多人眼不可见的区域也在这个正方体中。比如“超绿色”，这是人们不能看到的，因为人的视锥细胞对某个频率会两种细胞都刺激到而并不会只刺激到一种。比如频率为 550Hz 的光，红色和绿色的视锥细胞都会有反应值。

<figure><img src="../../.gitbook/assets/image (60).png" alt="【C02.02 Imaging - Colorspace】 【精准空降到 30:51】 https://www.bilibili.com/video/BV1U34y1G7wa/?share_source=copy_web&#x26;vd_source=0470ad56f59229195a0a7f79ab37cb27&#x26;t=1851" width="400"><figcaption><p>https://www.bilibili.com/video/BV1U34y1G7wa/?t=1851</p></figcaption></figure>

### XYZ

LMS 中，人眼的三种视锥细胞的响应值是归一化过的。三种视锥细胞的真实的响应函数是这样的。

<figure><img src="../../.gitbook/assets/image (44).png" alt=""><figcaption><p>XYZ color matching functions, CIE 1931 and Stockman &#x26; Sharpe 2006.[4]</p></figcaption></figure>

可以看到，上图中的蓝色响应函数的最大值很大，如果它被标准化到 1，相比红色和绿色而言会有很多的颜色被压缩。所以 XYZ 把 LMS 的蓝色维度保持不变，保持了三种响应函数彼此的一个比例关系，从而让色彩空间看起来更加“舒展”，这样如果后续需要进行抽样，可以更均衡的表示各种颜色。

<figure><img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/4a15573a77cd48decc68aada921e4ff01a6d24e2" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
其实 XYZ 的提出要早于 LMS！上面的内容其实是从实用主义的角度往回推导。从另一个角度想，其实 XYZ 也给 LMS 提供了科学依据，因为 LMS 从细胞的角度进行了精确的测量。
{% endhint %}

下面我们还是回到 LMS，想象由坐标轴三个顶点进行连线，将颜色空间切开。这个切面的三个点就是三个最极限的纯色，三角形内部的点就是三个顶点插值的结果。另外，三角形上任意一点与原点相连，可以提现亮度的变化（原点是黑色，三角形上一点是某一颜色的最亮）

<figure><img src="../../.gitbook/assets/image (45).png" alt="" width="249"><figcaption><p>https://www.bilibili.com/video/BV1U34y1G7wa/?t=1973</p></figcaption></figure>

XYZ 其实就是 LMS 的线性变换，XYZ 保持了LMS 的很多性质，比如颜色由三色光组成。但是这个变换让上边的那个三角形扭曲了，得到了 XYZ 里边的三角形，但其原理不变：三维空间某个纯颜色在三角形上投影，这个投影的颜色绘制为这个纯颜色在二维上的表示。

<figure><img src="../../.gitbook/assets/image (68).png" alt=""><figcaption></figcaption></figure>

得到了我们熟悉的 CIE颜色图（CIE chromaticity diagram）。

<figure><img src="../../.gitbook/assets/image (47).png" alt=""><figcaption><p>The Chromaticity Diagram[5]</p></figcaption></figure>

CIE颜色图中上半边曲线是所有频率颜色，也就是前边说的纯颜色，红橙黄绿青蓝紫。图中的下半边直线以及区域内部的点均是插值得到的结果！

{% hint style="info" %}
当然，这个切面肯定不是单纯把 LMS 的切面线性变换了一下这么简单。毕竟 LMS 是后来的理论，XYZ切的角度会不一样。
{% endhint %}

### RGB

上边的理论需要现代生物知识才能做到，RGB 模型诞生于二十世纪，那时的人们怎么确定的人眼对三原色的响应值呢。

<figure><img src="../../.gitbook/assets/image (70).png" alt=""><figcaption><p>A Beginner’s Guide to (CIE) Colorimetry[7]</p></figcaption></figure>

人们用三原色的光照射到某一个点（上图左侧）上，然后与待观测的颜色（上图右侧）进行对比，调节三原色光的强度直到两点颜色相同。

<figure><img src="../../.gitbook/assets/image (71).png" alt="https://medium.com/hipster-color-science/a-beginners-guide-to-colorimetry-401f1830b65a"><figcaption></figcaption></figure>

您可能已经注意到，在颜色匹配函数中，有时他们需要负光量来实现匹配，例如520 nm。实验者发现就算把一个颜色的光降成 0 颜色仍然不匹配。这时，他们就把这个颜色的光从强度 0 开始打在右边，从而得到左边强度为负的等价效果。

由于负值，我们可以表达更广泛的空间，下面是 CIE-RGB。（注意下图中的 r 坐标轴有负数）

<figure><img src="../../.gitbook/assets/image (74).png" alt=""><figcaption><p>1931 Color Matching Functions[8]</p></figcaption></figure>

RGB 的负值让我们表示颜色很麻烦，如果能把 RGB 线性变换一下就好了。选取三个颜色空间外的点，这样三角形就可以把整个 RGB 色彩空间保住，然后进行变换，把三个点变换到坐标轴上去。

<figure><img src="../../.gitbook/assets/image (75).png" alt=""><figcaption><p>[7]</p></figcaption></figure>

以 sRGB 举例，RGB 转换到 XYZ 的公式如下。

$$
\begin{bmatrix} X \\ Y \\ Z \end{bmatrix} = M = \begin{bmatrix} 0.4124564 & 0.3575761 & 0.1804375 \\ 0.2126729 & 0.7151522 & 0.0721750 \\ 0.0193339 & 0.1191920 & 0.9503041 \end{bmatrix} \begin{bmatrix} R \\ G \\ B \end{bmatrix}_{sRGB}
$$

当然，RGB 也有好多种，更详细的表格请看：[http://www.brucelindbloom.com/index.html?Eqn\_RGB\_XYZ\_Matrix.html](http://www.brucelindbloom.com/index.html?Eqn\_RGB\_XYZ\_Matrix.html)

线性变换后，响应函数也变成了正数。

<figure><img src="../../.gitbook/assets/image (76).png" alt="" width="375"><figcaption></figcaption></figure>

在CIE-RGB 的基础上，人们通过改变三个原色的极点，制定了越来越多的变种。比如 sRGB，AdobeRGB 等等。

<figure><img src="../../.gitbook/assets/image (80).png" alt=""><figcaption><p>[9]</p></figcaption></figure>

另外，由于人眼在暗色时对亮度变换更敏感，所以 sRGB 加入了 gamma 矫正，从而在暗色引入更多颜色，减少了人眼看起来变换不大的亮色颜色。但这有带来了新的问题，sRGB 不是线性的了！

<figure><img src="../../.gitbook/assets/image (81).png" alt="" width="375"><figcaption><p>[9]</p></figcaption></figure>

### HSV

RGB 虽然从颜色组成原理上有很好的解释，但我们调整颜色时想进行某个维度的掉整比如提升亮度，改变色调，RGB 三维度的“缠绕”关系让人很难理解，这就促成了从人类感官视角HSV。\[10]

* H（Hue）：色相。比如：红黄蓝。
* S（Saturation）：饱和度。比如，低饱和度的莫兰迪色系，就是往纯色里边掺“灰”。
* V（Value， Lightness， Brightness）：明度。顾名思义，就是亮度。

HSV 色彩空间的 Hue 可以理解成 RGB 中间的白色向四周画一个圆。

<figure><img src="../../.gitbook/assets/image (82).png" alt="" width="329"><figcaption><p>The Amazing Math behind Colors! [11]</p></figcaption></figure>

RGB 到 HSV 是非线性的变换

$$
\begin{aligned} \min &= \min(R,G,B)\\V&=max=\max(R,G,B)\\S&=(\max-\min)/\max\\H&=60\cdot \begin{cases}0+(G-B)/(\max-\min),if \max=R\\2+(B-R)/(\max-\min),if \max=G\\4+(R-G)/(\max-\min),if \max=B\\\end{cases}\\H&=H+360, if H<0 \end{aligned}
$$

至此，我们的到了 HSV。

<figure><img src="../../.gitbook/assets/image (84).png" alt="" width="375"><figcaption><p>[13]</p></figcaption></figure>

### HSL

HSL 和 HSV 非常类似。我们想象把下图右上角HSL的白点“拍”平，就得到了 HSV。

<figure><img src="../../.gitbook/assets/image (83).png" alt=""><figcaption><p>[12]</p></figcaption></figure>

另外，通过下张图，可以感受从 RGB 变换到 HSV 和 HSL 的过程。

<figure><img src="../../.gitbook/assets/image (85).png" alt=""><figcaption><p>[14]</p></figcaption></figure>

### Lab

Lab 通过非线性的变换，提升人们对色彩和谐的感知。很多可视化网站，将颜色从 RGB 换成了 Lab，大幅提升了颜色效果。

<figure><img src="../../.gitbook/assets/image (86).png" alt=""><figcaption><p>[15]</p></figcaption></figure>

### YIQ

YIQ 的时代背景是黑白电视变成彩色电视。它是一个电视系统标准。Y 就是亮度，也就是原来的黑白电视。黑白想加入色彩，按照 RGB 的思想，就要把一维空间升成三维。所以 YIQ 引入了另外两个维度用来表示颜色。

<figure><img src="../../.gitbook/assets/image (87).png" alt="" width="375"><figcaption><p>[16]</p></figcaption></figure>

YIQ 的优势是，相对于 HSV，YIQ和RGB 仍然是一个线性变换，计算复杂度低。另外它的亮度通道被提取出来了，可操纵性强。

<figure><img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/fcdfdebe09590e617de9e523514a79f506086a74" alt=""><figcaption></figcaption></figure>

### YCbCr / YUV

YIQ，YCbCr 和 YUV 彼此十分类似，都是亮度加两个色彩通道。只是YIQ适用于NTSC彩色电视制式，YUV适用于PAL和SECAM彩色电视制式，而YCrCb适用于计算机用的显示器。\[17] 下图左侧是 YIQ 的色域，右侧是 YUV 的，可见只是反转加旋转就可等价。

<figure><img src="../../.gitbook/assets/image (88).png" alt=""><figcaption></figcaption></figure>

人们发现，人眼对 Y 通道的变化很敏感，而对后两个颜色通道的变化不敏感，所以可以采用去除颜色通道高频成分的方式来压缩图片。

<figure><img src="../../.gitbook/assets/image (89).png" alt=""><figcaption><p>[18]</p></figcaption></figure>

### CMY / CMYK

以上的内容不管是RGB 还是 SUV 等等都是“加法思维”，但对于印刷来说，要转换成“减法思维”。

<figure><img src="../../.gitbook/assets/image (43).png" alt=""><figcaption></figcaption></figure>

***

## Resources and Reference

{% embed url="https://www.bilibili.com/video/BV1U34y1G7wa" %}

{% embed url="https://www.youtube.com/watch?v=nJlZT5AE9zY" %}

> \[1] [https://daltonlens.org/opensource-cvd-simulation/](https://daltonlens.org/opensource-cvd-simulation/)
>
> \[2] [https://upload.wikimedia.org/wikipedia/commons/5/5d/3D\_Graph\_of\_LMS\_Color\_Space.png](https://upload.wikimedia.org/wikipedia/commons/5/5d/3D\_Graph\_of\_LMS\_Color\_Space.png)
>
> \[3] [https://en.wikipedia.org/wiki/LMS\_color\_space](https://en.wikipedia.org/wiki/LMS\_color\_space)
>
> \[4] [https://en.wikipedia.org/wiki/CIE\_1931\_color\_space](https://en.wikipedia.org/wiki/CIE\_1931\_color\_space)
>
> \[5] [https://www.youtube.com/watch?v=O0nYJ0Mjx10](https://www.youtube.com/watch?v=O0nYJ0Mjx10)
>
> \[6] [https://www.youtube.com/watch?v=AS1OHMW873s](https://www.youtube.com/watch?v=AS1OHMW873s)
>
> \[7] [https://medium.com/hipster-color-science/a-beginners-guide-to-colorimetry-401f1830b65a](https://medium.com/hipster-color-science/a-beginners-guide-to-colorimetry-401f1830b65a)
>
> \[8] [https://clarkvision.com/imagedetail/color-cie-chromaticity-and-perception/](https://clarkvision.com/imagedetail/color-cie-chromaticity-and-perception/)
>
> \[9] [https://en.wikipedia.org/wiki/SRGB](https://en.wikipedia.org/wiki/SRGB)
>
> \[10] [https://en.wikipedia.org/wiki/HSL\_and\_HSV#Motivation](https://en.wikipedia.org/wiki/HSL\_and\_HSV#Motivation)
>
> \[11] [https://www.youtube.com/watch?v=gnUYoQ1pwes](https://www.youtube.com/watch?v=gnUYoQ1pwes)
>
> \[12] [https://en.m.wikipedia.org/wiki/File:Color\_solid\_comparison\_hsl\_hsv\_rgb\_cone\_sphere\_cube\_cylinder.png](https://en.m.wikipedia.org/wiki/File:Color\_solid\_comparison\_hsl\_hsv\_rgb\_cone\_sphere\_cube\_cylinder.png)
>
> \[13] [https://hyperskill.org/learn/step/13179](https://hyperskill.org/learn/step/13179)
>
> \[14] [https://en.wikipedia.org/wiki/HSL\_and\_HSV](https://en.wikipedia.org/wiki/HSL\_and\_HSV)
>
> \[15] [https://www.youtube.com/watch?v=AS1OHMW873s](https://www.youtube.com/watch?v=AS1OHMW873s)
>
> \[16] [https://en.wikipedia.org/wiki/YIQ](https://en.wikipedia.org/wiki/YIQ)
>
> \[17] [https://blog.csdn.net/machh/article/details/51799403](https://blog.csdn.net/machh/article/details/51799403)
>
> \[18] [https://www.youtube.com/watch?v=P3F3EwvU0m4](https://www.youtube.com/watch?v=P3F3EwvU0m4)
