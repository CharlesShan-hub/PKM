# 引导滤波
---
## 资料

* 官网：https://kaiminghe.github.io/eccv10/index.html
* 论文翻译：https://blog.csdn.net/studyeboy/article/details/121137028
* wiki：https://en.wikipedia.org/wiki/Guided_filter
* 大佬笔记：https://www.zhihu.com/question/26949096/answer/2910776043
* 推荐阅读：[引导滤波原理](https://blog.csdn.net/magic_shuang/article/details/123729987)

---
## 原理

引导滤波（Guided Filter）的核心思想是**利用一张引导图（Guidance Image）来指导对输入图像的滤波过程**。它假设输出图像在局部窗口内是引导图的线性变换，从而在平滑噪声的同时，能更好地保持引导图所提供的边缘结构。

**核心公式**（对于像素点 *i*）：
$$q_i = a_k I_i + b_k, \quad \forall i \in \omega_k$$
其中：
- $q_i$ 是输出图像在像素 *i* 的值。
- $I_i$ 是引导图像在像素 *i* 的值。
- $a_k$ 和 $b_k$ 是在以像素 *k* 为中心的局部窗口 $\omega_k$ 内计算出的线性系数。

**系数求解**：
通过最小化窗口内的代价函数（输出与输入的差异，并加入对系数 $a_k$ 的正则化）来求解 $a_k$ 和 $b_k$：
$$E(a_k, b_k) = \sum_{i \in \omega_k} \left( (a_k I_i + b_k - p_i)^2 + \epsilon a_k^2 \right)$$
其中 $p_i$ 是输入图像，$\epsilon$ 是防止 $a_k$ 过大的正则化参数。

**实际计算步骤**（简化）：
1.  计算窗口内 $I$ 和 $p$ 的均值、方差、协方差。
2.  根据公式求出每个窗口的 $a_k$ 和 $b_k$。
3.  由于像素 *i* 会被多个窗口覆盖，最终取其对应所有窗口系数的均值作为该像素的 $a_i$ 和 $b_i$。
4.  最终输出 $q_i = a_i I_i + b_i$。

**关键特性**：
- **边缘保持**：在边缘处，$I$ 变化大，$a_k$ 较大，$b_k$ 较小，输出 $q$ 会跟随引导图 $I$ 的变化，从而保留边缘。
- **平滑区域**：在平坦区域，$I$ 变化小，$a_k$ 趋近于0，$b_k$ 趋近于 $\bar{p}$，输出近似为输入的平均值，起到平滑作用。
- **非迭代、速度快**：只需几次均值滤波（盒滤波）即可实现，计算效率高。

---
## 效果展示

- 第一列：理想引导 (Original Guidance / Ideal Case)
	- 机制 ：使用 无噪声的原始可见光图像 作为引导。
	- 分析 ：这是去噪性能的 理论上限 。由于引导图完美包含了所有真实的边缘和纹理信息，滤波器能精准地区分噪声与细节。
	- 结果 ：第三行的误差图几乎全黑，表明去噪最彻底，且边缘细节保留最完美，无结构丢失。
- 第二列：跨模态引导 (IR Guidance / Cross-modal Case)
	- 机制 ：使用同一场景的**红外图像（Infrared）**作为引导。
	- 分析 ：模拟多模态图像处理场景。红外图像提供了互补的结构信息（如热源目标的轮廓），但也缺失了可见光特有的纹理细节。
	- 结果 ：去噪效果较好，但出现了独特的**结构迁移（Structure Transfer）**现象。仔细观察误差图，可见部分红外图像特有的边缘被“强行”保留到了结果中，而可见光独有的纹理因红外引导图的平坦而被抹平。
- 第三列：双边滤波引导 (Bilateral Guidance / Realistic Case)
	- 机制 ：先对噪声图进行**双边滤波（Bilateral Filter）**预处理，将其输出作为引导图。
	- 分析 ：这是一种实用的单幅图像增强策略。相比直接使用噪声图，双边滤波预先去除了大部分高频噪声并保留了主要边缘，从而提供了更可靠的结构指引。
	- 结果 ：误差显著低于自引导（第四列），在去噪能力和细节保持之间取得了良好的平衡。
- 第四列：自引导 (Self-Guidance / Baseline Case)
	- 机制 ：直接使用 含噪输入图像本身 作为引导图。
	- 分析 ：这是引导滤波的最基础用法。由于引导图本身含有噪声，计算出的线性系数会受到干扰，难以在平滑区域和边缘之间做出完美划分。
	- 结果 ：误差图最亮，表明残留噪声最多，且在边缘附近容易产生模糊或光晕（Halo）效应。
![guided](../assets/guided.png)

```python
import matplotlib.pyplot as plt
from skimage import data, img_as_float
from skimage.util import random_noise
from skimage.restoration import denoise_bilateral
from scipy.ndimage import uniform_filter
import numpy as np
from cslib.metrics.fusion import ir,vis
from cslib.utils import to_numpy

ir = to_numpy(ir)
vis = to_numpy(vis)

def guided_filter(I, p, r, eps):
	"""
	引导滤波器 (Guided Filter) 实现
	参数:
	I: 引导图像 (Guidance Image) - 应该是归一化到 [0, 1] 的浮点数图像
	p: 输入图像 (Input Image) - 应该是归一化到 [0, 1] 的浮点数图像
	r: 滤波半径 (Radius)
	eps: 正则化参数 (Regularization parameter)
	返回:
	q: 滤波后的输出图像
	"""
	
	# 均值滤波函数 (使用 scipy.ndimage.uniform_filter)
	# uniform_filter 的 size 参数如果是标量，则各个维度都一样，即 size=2*r+1
	w_size = 2 * r + 1
	
	# 计算均值
	mean_I = uniform_filter(I, size=w_size)
	mean_p = uniform_filter(p, size=w_size)
	mean_Ip = uniform_filter(I * p, size=w_size)
	
	# 协方差 cov(I, p) = E(Ip) - E(I)E(p)
	cov_Ip = mean_Ip - mean_I * mean_p
	mean_II = uniform_filter(I * I, size=w_size)
	var_I = mean_II - mean_I * mean_I
	
	# 线性系数 a 和 b
	a = cov_Ip / (var_I + eps)
	b = mean_p - a * mean_I
	
	# 计算均值 a 和 b
	mean_a = uniform_filter(a, size=w_size)
	mean_b = uniform_filter(b, size=w_size)
	q = mean_a * I + mean_b
	return q

# 1. 加载图像并转换为浮点数 [0, 1]
# original_img = img_as_float(data.camera())
original_img = vis # 使用 vis 作为原图

# 2. 添加噪声
noisy_img = random_noise(original_img, mode='gaussian', var=0.002)

# 3. 准备引导图
# 引导图1：原始无噪声图 (Ideal case)
guidance_1 = original_img

# 引导图2：红外图像 (Cross-modal case)
guidance_2 = ir

# 引导图3：双边滤波后的图 (More realistic case)
# sigma_color: 值域标准差, sigma_spatial: 空间标准差
# 噪声方差 var=0.01，即标准差 sigma=0.1。
# 应该设置 sigma_color >= 噪声标准差，这里设为 0.15 左右效果会好很多。
guidance_3 = denoise_bilateral(noisy_img, sigma_color=0.12, sigma_spatial=20, channel_axis=None)

# 引导图4：噪声图本身 (Self-guided, most common/simple case)
guidance_4 = noisy_img

# 4. 引导滤波
radius = 4
epsilon = 1e-2 ** 2 # (0.01)^2

# 使用原图作为引导
filtered_1 = guided_filter(guidance_1, noisy_img, radius, epsilon)

# 使用红外图作为引导
filtered_2 = guided_filter(guidance_2, noisy_img, radius, epsilon)

# 使用双边滤波图作为引导
filtered_3 = guided_filter(guidance_3, noisy_img, radius, epsilon)

# 使用噪声图本身作为引导
filtered_4 = guided_filter(guidance_4, noisy_img, radius, epsilon)

# 5. 可视化结果对比
fig, axes = plt.subplots(3, 4, figsize=(20, 15))

# 第一行：引导图
ax_row1 = axes[0]
ax_row1[0].imshow(guidance_1, cmap='gray')
ax_row1[0].set_title('Guidance 1: Original (Vis)\n(Ideal Reference)')
ax_row1[0].axis('off')
ax_row1[1].imshow(guidance_2, cmap='gray')
ax_row1[1].set_title('Guidance 2: Infrared (IR)\n(Cross-modal)')
ax_row1[1].axis('off')
ax_row1[2].imshow(guidance_3, cmap='gray')
ax_row1[2].set_title(f'Guidance 3: Bilateral Filtered\n($\sigma_s$=20, $\sigma_c$=0.12)')
ax_row1[2].axis('off')
ax_row1[3].imshow(guidance_4, cmap='gray')
ax_row1[3].set_title('Guidance 4: Noisy Image\n(Self-guided)')
ax_row1[3].axis('off')

# 第二行：滤波结果
ax_row2 = axes[1]

# 显示原图引导的结果
ax_row2[0].imshow(filtered_1, cmap='gray')
ax_row2[0].set_title(f'Result with Original Guidance\n(r={radius}, $\epsilon$={epsilon:.0e})')
ax_row2[0].axis('off')

# 显示红外图引导的结果
ax_row2[1].imshow(filtered_2, cmap='gray')
ax_row2[1].set_title(f'Result with IR Guidance\n(r={radius}, $\epsilon$={epsilon:.0e})')
ax_row2[1].axis('off')

# 显示双边滤波引导的结果
ax_row2[2].imshow(filtered_3, cmap='gray')
ax_row2[2].set_title(f'Result with Bilateral Guidance\n(r={radius}, $\epsilon$={epsilon:.0e})')
ax_row2[2].axis('off')

# 显示噪声图引导的结果
ax_row2[3].imshow(filtered_4, cmap='gray')
ax_row2[3].set_title(f'Result with Self-Guidance\n(r={radius}, $\epsilon$={epsilon:.0e})')
ax_row2[3].axis('off')

# 第三行：与原图的差异（残差/误差）
ax_row3 = axes[2]

# 结果1与原图差异
diff1 = np.abs(filtered_1 - original_img)
im_diff1 = ax_row3[0].imshow(diff1, cmap='inferno', vmin=0, vmax=0.2)
ax_row3[0].set_title('Error: Result 1 vs Original\n(Ideal Guidance)')
ax_row3[0].axis('off')
plt.colorbar(im_diff1, ax=ax_row3[0], fraction=0.046, pad=0.04)

# 结果2与原图差异
diff2 = np.abs(filtered_2 - original_img)
im_diff2 = ax_row3[1].imshow(diff2, cmap='inferno', vmin=0, vmax=0.2)
ax_row3[1].set_title('Error: Result 2 vs Original\n(IR Guidance)')
ax_row3[1].axis('off')
plt.colorbar(im_diff2, ax=ax_row3[1], fraction=0.046, pad=0.04)

# 结果3与原图差异
diff3 = np.abs(filtered_3 - original_img)
im_diff3 = ax_row3[2].imshow(diff3, cmap='inferno', vmin=0, vmax=0.2)
ax_row3[2].set_title('Error: Result 3 vs Original\n(Bilateral Guidance)')
ax_row3[2].axis('off')
plt.colorbar(im_diff3, ax=ax_row3[2], fraction=0.046, pad=0.04)

# 结果4与原图差异
diff4 = np.abs(filtered_4 - original_img)
im_diff4 = ax_row3[3].imshow(diff4, cmap='inferno', vmin=0, vmax=0.2)
ax_row3[3].set_title('Error: Result 4 vs Original\n(Self-Guidance)')
ax_row3[3].axis('off')
plt.colorbar(im_diff4, ax=ax_row3[3], fraction=0.046, pad=0.04)
plt.suptitle('Guided Filter Comparison: Impact of Guidance Image Quality', fontsize=16)
plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.show()
```