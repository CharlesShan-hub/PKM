# contourpy

`contourpy` 是一个 Python 库，用于生成高质量的等高线图。它提供了多种等高线生成算法，包括快速等高线生成（Fast Marching Method）、区域生长法（Region Growing）和最小二乘等高线拟合（Least Squares Contouring）。`contourpy` 支持多种输入格式，如 NumPy 数组、Python 列表和 Pandas DataFrame。 以下是 `contourpy` 的关键特点和用法：

#### 关键特点

1. **高质量等高线生成**：提供多种等高线生成算法，以生成高质量的等高线图。
2. **支持多种输入格式**：支持 NumPy 数组、Python 列表和 Pandas DataFrame 等多种输入格式。
3. **灵活的参数设置**：允许你自定义等高线生成算法和参数，以满足特定需求。
4. **可定制性**：允许你自定义等高线图的样式，包括颜色、线型、标记等。

#### 安装

可以通过pip安装`contourpy`：

```bash
pip install contourpy
```

#### 基本用法

以下是一些使用 `contourpy` 的基本示例：

**生成等高线图**

```python
import numpy as np
import contourpy as cp
# 创建一个高度场数据
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
z = np.sin(x**2 + y**2)
# 使用 contourpy 生成等高线图
contours = cp.generate_contours(z, 10)
# 绘制等高线图
cp.plot_contours(contours)
```

在这个例子中，我们创建了一个高度场数据，并使用 `contourpy.generate_contours` 函数来生成等高线图。然后，我们使用 `contourpy.plot_contours` 函数来绘制等高线图。

#### 使用场景

* **科学可视化**：在科学可视化中，使用 `contourpy` 来生成高质量的等高线图。
* **地理信息系统**：在地理信息系统中，使用 `contourpy` 来生成地形等高线图。
* **数据可视化**：在数据可视化中，使用 `contourpy` 来生成等高线图，以展示数据的分布和趋势。 `contourpy` 是一个非常有用的库，它可以帮助 Python 开发者生成高质量的等高线图。由于其灵活性和可定制性，`contourpy` 在科学可视化和地理信息系统等领域非常有用。
