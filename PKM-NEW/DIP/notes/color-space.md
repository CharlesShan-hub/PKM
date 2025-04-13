
# Color Space

---
## Overview

![[../assets/color-space-drawing|1000]]
***

## Theory

### Tristimulus Values

光是电磁波，按照频率可以绘制出光谱。人眼的三种视锥细胞分别可以吸收三种频率的光。自然界各种频率的光，对于人眼而言，只要转换成三种细胞的吸收情况就可以了。

詹姆斯·克拉克·麦克斯韦（James Clerk Maxwell）**（1861年）** 首次通过红、绿、蓝滤光片分别拍摄黑白照片，再叠加投影，验证了RGB合成彩色的可行性。这被视为RGB技术的雏形。

---
## Color Space

### RGB

* 提出：在 20 世纪 20 年代，W. David Wright 与 10 名观察者进行了两项独立的人类颜色感知实验，John Guild 与 7 名观察者进行了实验。本节描述了他们的结果如何为 CIE 1931 色空间奠定了基础。
* 细节：👉 [[../details/RGB|RGB]]

### LMS

* 提出：2000年，Stockman和Sharpe根据人眼视锥细胞的规律，提出了一套基于生理学的LMS功能，在 2006 年 CIE 的技术报告 （CIE 170） 中发布。
* 细节：[[../details/LMS|👉 LMS]]

### XYZ

* 提出：1931 年 XYZ 颜色匹配函数是 1931 年 RGB 颜色匹配函数的线性变换，以便赋予它们一些数学上的便利性质。事实上，我们一直在讨论的 RGB CMFs 在实用色度学中大部分未被使用。现代色域是用 XYZ 来定义的。
* 细节：👉 [[../details/XYZ|XYZ]]

### HSV

* 提出：RGB 虽然从颜色组成原理上有很好的解释，但我们调整颜色时想进行某个维度的掉整比如提升亮度，改变色调，RGB 三维度的“缠绕”关系让人很难理解，这就促成了从人类感官视角HSV。
* 细节：👉 [[../details/HSV|HSV]]

### HSL

* 提出：HSL 和 HSV 非常类似。我们想象把下图右上角HSL的白点“拍”平，就得到了 HSV。
* 细节：👉 [[../details/HSL|HSL]]

### Lab

* 提出：Lab 通过非线性的变换，提升人们对色彩和谐的感知。很多可视化网站，将颜色从 RGB 换成了 Lab，大幅提升了颜色效果。
* 细节：👉 [[../details/Lab|Lab]]

### YIQ

* 提出：YIQ 的时代背景是黑白电视变成彩色电视。它是一个电视系统标准。Y 就是亮度，也就是原来的黑白电视。黑白想加入色彩，按照 RGB 的思想，就要把一维空间升成三维。所以 YIQ 引入了另外两个维度用来表示颜色。
* 细节：👉 [[../details/YIQ|YIQ]]

### YCbCr / YUV

* 提出：YIQ，YCbCr 和 YUV 彼此十分类似，都是亮度加两个色彩通道。只是YIQ适用于NTSC彩色电视制式，YUV适用于PAL和SECAM彩色电视制式，而YCrCb适用于计算机用的显示器。
* 细节：👉 [[../details/YCbCr|YCbCr]]
### CMY / CMYK

* 提出：以上的内容不管是RGB 还是 SUV 等等都是“加法思维”，但对于印刷来说，要转换成“减法思维”。
* 细节：👉 [[../details/CMY|CMY]]

***

## Resources and Reference

https://www.bilibili.com/video/BV1U34y1G7wa

https://www.youtube.com/watch?v=nJlZT5AE9zY

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
> 
> [19] https://github.com/mittimithai/colorspacegraphs
