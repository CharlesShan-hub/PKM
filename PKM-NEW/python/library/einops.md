# einops

> 通过不停的对 GPT 提问，结合源码，可以达到怎样的学习体验呢？

---
## Overview
### einops概况

> 直观的有个印象，einops在做什么
1. einops 是一个在处理多维数组（例如在深度学习中常用的张量）时非常有用的 Python 库。它提供了一种简洁且统一的表达方式来重排、拆分和合并张量的维度。使用 einops 可以让代码更加易于理解和维护。
2. 安装 einops：`pip install einops`
3. 链接
	1. 官网：[https://einops.rocks/](https://einops.rocks/)
	2. [medium：Einops in 30 seconds](https://medium.com/@kyeg/einops-in-30-seconds-377a5f4d641a)
	3. [https://blog.csdn.net/angel_hben/article/details/129079635](https://blog.csdn.net/angel_hben/article/details/129079635)
4. 应用场景
	1. 维度重排：在卷积神经网络（CNN）、循环神经网络（RNN）和变压器（Transformer）模型中，经常需要重新排列张量的维度以匹配层之间的输入和输出要求。【**这个是我用到的，把一个图片分成小块放到Transformer里边**】
	2. 维度缩减：在池化层或全局平均池化中，减少张量的维度，例如从 (batch_size, height, width, channels) 到 (batch_size, channels)。
	3. 维度扩展：在数据增强或某些层中，可能需要增加额外的维度，例如将 (batch_size, channels) 扩展为 (batch_size, 1, 1, channels)。【这么看确实比使用 pytorch 更直观】
	4. ... and so on
### einops内容

> 直击源码，打通所有的代码框架
1. 所有内容都有什么
	```bash
	(Pytorch2) kimshan@MacBook-Pro einops % ls
	__init__.py             experimental
	__pycache__             layers
	_backends.py            packing.py
	_torch_specific.py      parsing.py
	array_api.py            py.typed
	einops.py
	```
2. 直接使用的API：`__init__.py`
	1. `einops.py`：（核心）张量的高级操作
		1. **rearrange**: 用于重新排列和重塑张量的维度，以匹配所需的格式。
		2. **reduce**: 通过指定的操作（如求和、平均等）减少张量的维度。
		3. **repeat**: 在指定的维度上复制张量，以增加其大小。
		4. **einsum**: 提供了一种简洁的方式来执行张量之间的逐元素乘法和累加操作。
		5. **parse_shape**: 解析和计算张量的形状，特别是在形状包含表达式或未知维度时。
		6. **asnumpy**: 将张量转换为 NumPy 数组，以便使用 NumPy 提供的功能。
		7. **EinopsError**: 在执行 einops 操作时抛出的异常，用于指示发生了错误。
	2. `packing.py`：用于处理张量的打包和解包
		8. **pack**: 将多个张量打包成一个更大的张量，通常用于批处理操作。
		9. **unpack**: 将一个打包的张量解包回多个单独的张量。 
  3. 为各种框架提供实现：`layers`文件夹
  	4. `__init__.py`：提供了底层的 class RearrangeMixin，class ReduceMixin
  	5. `_einmix.py`：提供了一个混合器类，用于在深度学习框架中实现 **EinMix** 层，该层可以简化多维张量的混合操作，并自动处理权重和偏差张量的初始化和管理。这个类需要在特定的深度学习框架中进一步实现。
  	6. `flax.py`：为 flax 框架提供了三个自定义层：Rearrange、Reduce 和 EinMix
  	7. `oneflow.py`：为 oneflow 框架提供了三个自定义层
  	8. `tensorflow.py`：为 tensorflow 框架提供了三个自定义层
  	9. `chainer.py`：为 chainer 框架提供了三个自定义层
  	10. `keras.py`：为 keras 框架提供了三个自定义层
  	11. `paddle.py`：为 paddle 框架提供了三个自定义层
  	12. `torch.py`：为 pytorch 框架提供了三个自定义层
  413. 持作用的底层操作
  	14. `parsing.py`：这些类和方法是 einops 库内部用于解析和处理张量操作表达式的工具。它们使得用户能够使用简洁的字符串表达式来指定复杂的张量操作，例如重新排列、重塑和组合轴。
  	15. `array_api.py`：一个说明文件，和`einops.py`很多代码相同。
  	16. `_torch_specific.py`：支持与 PyTorch 的 JIT 编译兼容。
  	17. `_backends.py`：各种实现的后端。【我感觉这个才是这个库的精髓，他把不同的框架的 tensor 都抽象起来了，在实现具体功能的时候各种逻辑只需要写一遍】
 5.18. 再加入的功能：`experimental`文件夹

---
## APIs

> 经过以上分析，这个库实现了对多个框架的，函数或者模块化的高级张量操作。
> 下面我把源码中的文档字符串粘贴进来，然后如果有不容易懂得再展开说。
### reduce
    """
    einops.reduce provides combination of reordering and reduction using reader-friendly notation.

    Examples for reduce operation:

    ```python
    >>> x = np.random.randn(100, 32, 64)

    # perform max-reduction on the first axis
    >>> y = reduce(x, 't b c -> b c', 'max')

    # same as previous, but with clearer axes meaning
    >>> y = reduce(x, 'time batch channel -> batch channel', 'max')

    >>> x = np.random.randn(10, 20, 30, 40)

    # 2d max-pooling with kernel size = 2 * 2 for image processing
    >>> y1 = reduce(x, 'b c (h1 h2) (w1 w2) -> b c h1 w1', 'max', h2=2, w2=2)

    # if one wants to go back to the original height and width, depth-to-space trick can be applied
    >>> y2 = rearrange(y1, 'b (c h2 w2) h1 w1 -> b c (h1 h2) (w1 w2)', h2=2, w2=2)
    >>> assert parse_shape(x, 'b _ h w') == parse_shape(y2, 'b _ h w')

    # Adaptive 2d max-pooling to 3 * 4 grid
    >>> reduce(x, 'b c (h1 h2) (w1 w2) -> b c h1 w1', 'max', h1=3, w1=4).shape
    (10, 20, 3, 4)

    # Global average pooling
    >>> reduce(x, 'b c h w -> b c', 'mean').shape
    (10, 20)

    # Subtracting mean over batch for each channel
    >>> y = x - reduce(x, 'b c h w -> () c () ()', 'mean')

    # Subtracting per-image mean for each channel
    >>> y = x - reduce(x, 'b c h w -> b c () ()', 'mean')

    ```

    Parameters:
        tensor: tensor: tensor of any supported library (e.g. numpy.ndarray, tensorflow, pytorch).
            list of tensors is also accepted, those should be of the same type and shape
        pattern: string, reduction pattern
        reduction: one of available reductions ('min', 'max', 'sum', 'mean', 'prod'), case-sensitive
            alternatively, a callable f(tensor, reduced_axes) -> tensor can be provided.
            This allows using various reductions, examples: np.max, tf.reduce_logsumexp, torch.var, etc.
        axes_lengths: any additional specifications for dimensions

    Returns:
        tensor of the same type as input
    """
1. 一个 **Demo**：求最大值
```python
>>> x = np.random.randn(5,3)
>>> y = reduce(x, 't a -> a', 'max')
>>> x
array([[-0.09399422,  0.98488931, -0.83173863],
       [-0.0140485 ,  0.55658672, -0.11621765],
       [-1.73142355,  0.49761059,  0.31423137],
       [ 0.48302816, -0.68043368,  1.39221535],
       [-0.33247845, -0.58816318, -0.01502158]])
>>> y
array([0.48302816, 0.98488931, 1.39221535])
```
2. 上边的例子中，t、a 都是我们取的名字，我们可以自己取更明确的**代称**
```python
>>> x = np.random.randn(100, 32, 64)
>>> y = reduce(x, 'time batch channel -> batch channel', 'max')
>>> x.shape
(100, 32, 64)
>>> y.shape
(32, 64)
```
3. 另一个 Demo，2d max-pooling with kernel size = 2 * 2，用到了**倍数缩减**某个维度大小
```python
>>> x = np.random.randn(1, 3, 256, 256)
>>> y = reduce(x, 'b c (h1 h2) (w1 w2) -> b c h1 w1', 'max', h2=2, w2=2)
>>> y.shape
(1, 3, 128, 128)
```
4. 除了缩减一个维度，我们可以使用（）来**保留维度**
```python
>>> x = np.random.randn(2,3,4)
>>> y = x - reduce(x, 'c w h -> c () ()', 'mean')
>>> reduce(x, 'c w h -> c () ()', 'mean')
array([[[-0.13433713]],

       [[-0.07317865]]])
>>> reduce(x, 'c w h -> c () ()', 'mean').shape
(2, 1, 1)
```
最后我们进行维度缩减时进行的操作有：**'min', 'max', 'sum', 'mean', 'prod'**
### rearrange
    """
    einops.rearrange is a reader-friendly smart element reordering for multidimensional tensors.
    This operation includes functionality of transpose (axes permutation), reshape (view), squeeze, unsqueeze,
    stack, concatenate and other operations.

    Examples for rearrange operation:

    ```python
    # suppose we have a set of 32 images in "h w c" format (height-width-channel)
    >>> images = [np.random.randn(30, 40, 3) for _ in range(32)]

    # stack along first (batch) axis, output is a single array
    >>> rearrange(images, 'b h w c -> b h w c').shape
    (32, 30, 40, 3)

    # concatenate images along height (vertical axis), 960 = 32 * 30
    >>> rearrange(images, 'b h w c -> (b h) w c').shape
    (960, 40, 3)

    # concatenated images along horizontal axis, 1280 = 32 * 40
    >>> rearrange(images, 'b h w c -> h (b w) c').shape
    (30, 1280, 3)

    # reordered axes to "b c h w" format for deep learning
    >>> rearrange(images, 'b h w c -> b c h w').shape
    (32, 3, 30, 40)

    # flattened each image into a vector, 3600 = 30 * 40 * 3
    >>> rearrange(images, 'b h w c -> b (c h w)').shape
    (32, 3600)

    # split each image into 4 smaller (top-left, top-right, bottom-left, bottom-right), 128 = 32 * 2 * 2
    >>> rearrange(images, 'b (h1 h) (w1 w) c -> (b h1 w1) h w c', h1=2, w1=2).shape
    (128, 15, 20, 3)

    # space-to-depth operation
    >>> rearrange(images, 'b (h h1) (w w1) c -> b h w (c h1 w1)', h1=2, w1=2).shape
    (32, 15, 20, 12)

    ```

    When composing axes, C-order enumeration used (consecutive elements have different last axis)
    Find more examples in einops tutorial.

    Parameters:
        tensor: tensor of any supported library (e.g. numpy.ndarray, tensorflow, pytorch).
                list of tensors is also accepted, those should be of the same type and shape
        pattern: string, rearrangement pattern
        axes_lengths: any additional specifications for dimensions

    Returns:
        tensor of the same type as input. If possible, a view to the original tensor is returned.

    """
1. 通过列表得到的维度可以被合并进去
```python
>>> images = [np.random.randn(30, 40, 3) for _ in range(32)]
>>> rearrange(images, 'b h w c -> b h w c').shape
(32, 30, 40, 3)
```
2. 可以进行指定维度的转置
```python
>>> images = [np.random.randn(30, 40, 3) for _ in range(32)]
>>> rearrange(images, 'b h w c -> b c h w').shape
(32, 3, 30, 40)
```
3. 可以进行指定维度的合并（这里的图片是一个 batch 为 1 的，2x3 大小的灰度图，255 单独算一个颜色）
```python
>>> images = np.array([[[[255, 200, 150],[200, 40, 130]]]])
>>> # 拿到图片 tensor
>>> rearrange(images, 'b c h w -> b c h w').shape
(1, 1, 2, 3)
>>> rearrange(images, 'b c h w -> b c h w')
array([[[[255, 200, 150],
         [200,  40, 130]]]])
>>> # 合并
>>> rearrange(images, 'b c h w -> (b c) h w').shape
(1, 2, 3)
>>> rearrange(images, 'b c h w -> (b c) h w')
array([[[255, 200, 150],
        [200,  40, 130]]])
>>> # 交换顺序结果不一定一样
>>> rearrange(images, 'b c h w -> b c (h w)').shape
(1, 1, 6)
>>> rearrange(images, 'b c h w -> b c (w h)').shape
(1, 1, 6)
>>> rearrange(images, 'b c h w -> b c (h w)') # h 拼在 w 后边，保留 w 完整性
array([[[255, 200, 150, 200,  40, 130]]])
>>> rearrange(images, 'b c h w -> b c (w h)') # w 拼在 h 后边，保留 h 完整性
array([[[255, 200, 200,  40, 150, 130]]])
```
4. 图片的flatten，这里就要注意顺序了（这里改成了 bhwc 了，[255, 200, 150]算一个 RGB 颜色）
```python
>>> images = np.array([[[[255, 200, 150],[200, 40, 130]]]])
>>> rearrange(images, 'b h w c -> b (c h w)').shape
(1, 6)
>>> rearrange(images, 'b h w c -> b (c h w)')
array([[255, 200, 200,  40, 150, 130]])
```
5. 图片的分块：下边的例子就是根据图片的宽和高，各分两份，然后叠加在 batch 上边。
```python
>>> images = np.array([[[[255, 200, 150, 100],[200, 40, 130, 200]]]])
>>> rearrange(images, 'b c h w -> b c h w')
array([[[[255, 200, 150, 100],
         [200,  40, 130, 200]]]])
>>> rearrange(images, 'b c (h1 h) (w1 w) -> (b h1 w1) c h w', h1=2, w1=2).shape
(4, 1, 1, 2)
>>> rearrange(images, 'b c (h1 h) (w1 w) -> (b h1 w1) c h w', h1=2, w1=2)
array([[[[255, 200]]],
       [[[150, 100]]],
       [[[200,  40]]],
       [[[130, 200]]]])
```
6. space-to-depth operation，但我觉得像下采样，然后遍历一下
```python
>>> images = np.array([[[[255, 200, 150, 100, 1, 2],[200, 40, 130, 200, 3, 4],[255, 224, 253, 252, 5, 6], [10, 20, 30, 40, 7, 8]]]])
>>> rearrange(images, 'b c h w -> b c h w')
array([[[[255, 200, 150, 100,   1,   2],
         [200,  40, 130, 200,   3,   4],
         [255, 224, 253, 252,   5,   6],
         [ 10,  20,  30,  40,   7,   8]]]])
>>> rearrange(images, 'b c (h h1) (w w1) -> b (c h1 w1) h w', h1=2, w1=2).shape
(1, 4, 2, 3)
>>> rearrange(images, 'b c (h h1) (w w1) -> b (c h1 w1) h w', h1=2, w1=2)
array([[[[255, 150,   1],
         [255, 253,   5]],

        [[200, 100,   2],
         [224, 252,   6]],

        [[200, 130,   3],
         [ 10,  30,   7]],

        [[ 40, 200,   4],
         [ 20,  40,   8]]]])
```
### repeat
    """
    einops.repeat allows reordering elements and repeating them in arbitrary combinations.
    This operation includes functionality of repeat, tile, broadcast functions.

    Examples for repeat operation:

    ```python
    # a grayscale image (of shape height x width)
    >>> image = np.random.randn(30, 40)

    # change it to RGB format by repeating in each channel
    >>> repeat(image, 'h w -> h w c', c=3).shape
    (30, 40, 3)

    # repeat image 2 times along height (vertical axis)
    >>> repeat(image, 'h w -> (repeat h) w', repeat=2).shape
    (60, 40)

    # repeat image 2 time along height and 3 times along width
    >>> repeat(image, 'h w -> (h2 h) (w3 w)', h2=2, w3=3).shape
    (60, 120)

    # convert each pixel to a small square 2x2. Upsample image by 2x
    >>> repeat(image, 'h w -> (h h2) (w w2)', h2=2, w2=2).shape
    (60, 80)

    # pixelate image first by downsampling by 2x, then upsampling
    >>> downsampled = reduce(image, '(h h2) (w w2) -> h w', 'mean', h2=2, w2=2)
    >>> repeat(downsampled, 'h w -> (h h2) (w w2)', h2=2, w2=2).shape
    (30, 40)

    ```

    When composing axes, C-order enumeration used (consecutive elements have different last axis)
    Find more examples in einops tutorial.

    Parameters:
        tensor: tensor of any supported library (e.g. numpy.ndarray, tensorflow, pytorch).
            list of tensors is also accepted, those should be of the same type and shape
        pattern: string, rearrangement pattern
        axes_lengths: any additional specifications for dimensions

    Returns:
        Tensor of the same type as input. If possible, a view to the original tensor is returned.

    """
1. repeat 就是重复，比如把灰度图通过简单的通道堆叠变成 RGB
```python
>>> image = np.random.randn(30, 40)
>>> repeat(image, 'h w -> h w c', c=3).shape
(30, 40, 3)
```
2. 更复杂一点，可以实现金字塔算发里边的上采样操作（下采样去用reduce做）
```python
>>> image = np.array([[10,20],[30,40]])
>>> rearrange(image, 'h w -> h w')
array([[10, 20],
       [30, 40]])
>>> repeat(image, 'h w -> (h h2) (w w2)', h2=2, w2=2).shape
(4, 4)
>>> repeat(image, 'h w -> (h h2) (w w2)', h2=2, w2=2)
array([[10, 10, 20, 20],
       [10, 10, 20, 20],
       [30, 30, 40, 40],
       [30, 30, 40, 40]])
```
### parse_shape
    """
    Parse a tensor shape to dictionary mapping axes names to their lengths.

    ```python
    # Use underscore to skip the dimension in parsing.
    >>> x = np.zeros([2, 3, 5, 7])
    >>> parse_shape(x, 'batch _ h w')
    {'batch': 2, 'h': 5, 'w': 7}

    # `parse_shape` output can be used to specify axes_lengths for other operations:
    >>> y = np.zeros([700])
    >>> rearrange(y, '(b c h w) -> b c h w', **parse_shape(x, 'b _ h w')).shape
    (2, 10, 5, 7)

    ```

    For symbolic frameworks may return symbols, not integers.

    Parameters:
        x: tensor of any supported framework
        pattern: str, space separated names for axes, underscore means skip axis

    Returns:
        dict, maps axes names to their lengths
    """
用来获取 tensor 形状
```python
>>> x = np.zeros([2, 3, 5, 7])
>>> parse_shape(x, 'batch _ h w')
{'batch': 2, 'h': 5, 'w': 7}
```
### asnumpy
    """
    Convert a tensor of an imperative framework (i.e. numpy/cupy/torch/jax/etc.) to `numpy.ndarray`

    Parameters:
        tensor: tensor of any known imperative framework

    Returns:
        `numpy.ndarray`, converted to numpy
    """
 源码中就是`return get_backend(tensor).to_numpy(tensor)`，调用各个框架的 to_numpy

### einsum
einops.einsum 提供了一种使用爱因斯坦求和约定来表示和执行张量操作的方法，但它专为处理深度学习框架中的张量（如 PyTorch、TensorFlow、JAX 等）而设计。

	"""
    einops.einsum calls einsum operations with einops-style named
    axes indexing, computing tensor products with an arbitrary
    number of tensors. Unlike typical einsum syntax, here you must
    pass tensors first, and then the pattern.

    Also, note that rearrange operations such as `"(batch chan) out"`,
    or singleton axes `()`, are not currently supported.

    Examples:

    For a given pattern such as:
    ```python
    >>> x, y, z = np.random.randn(3, 20, 20, 20)
    >>> output = einsum(x, y, z, "a b c, c b d, a g k -> a b k")

    ```
    the following formula is computed:
    ```tex
    output[a, b, k] =
        \sum_{c, d, g} x[a, b, c] * y[c, b, d] * z[a, g, k]
    ```
    where the summation over `c`, `d`, and `g` is performed
    because those axes names do not appear on the right-hand side.

    Let's see some additional examples:
    ```python
    # Filter a set of images:
    >>> batched_images = np.random.randn(128, 16, 16)
    >>> filters = np.random.randn(16, 16, 30)
    >>> result = einsum(batched_images, filters,
    ...                 "batch h w, h w channel -> batch channel")
    >>> result.shape
    (128, 30)

    # Matrix multiplication, with an unknown input shape:
    >>> batch_shape = (50, 30)
    >>> data = np.random.randn(*batch_shape, 20)
    >>> weights = np.random.randn(10, 20)
    >>> result = einsum(weights, data,
    ...                 "out_dim in_dim, ... in_dim -> ... out_dim")
    >>> result.shape
    (50, 30, 10)

    # Matrix trace on a single tensor:
    >>> matrix = np.random.randn(10, 10)
    >>> result = einsum(matrix, "i i ->")
    >>> result.shape
    ()

    ```

    Parameters:
        tensors_and_pattern:
            tensors: tensors of any supported library (numpy, tensorflow, pytorch, jax).
            pattern: string, einsum pattern, with commas
                separating specifications for each tensor.
                pattern should be provided after all tensors.

    Returns:
        Tensor of the same type as input, after processing with einsum.

    """
1. 官网的案例：不同张量的合并
```python
>>> x, y, z = np.random.randn(3, 1, 2, 3)
>>> x
array([[[ 0.16705873,  2.51210949,  0.52959118],
        [ 0.58353769, -0.6779666 , -0.13415447]]])
>>> y
array([[[-0.47765094,  0.00385458, -0.14655275],
        [-1.05469934, -0.15484965, -0.15026622]]])
>>> z
array([[[-0.47858963, -0.12515551, -0.18813591],
        [ 1.30117152,  0.02993121,  0.47870161]]])
>>> output = einsum(x, y, z, "a b c, c b d, a g k -> a b k")
>>> output
array([[[-1.63739124,  0.18954883, -0.57838586],
        [ 0.25568409, -0.02959868,  0.09031688]]])
```
$$output[a, b, k] =
        \sum_{c, d, g} x[a, b, c] * y[c, b, d] * z[a, g, k]$$
2. 官网的案例并没有看懂，我们进行一个小实验**（如果你知道 einsum 是什么就可以跳过这一部分）**
* 首先准备一些数据：
```python
>>> from einops import einsum
>>> import numpy as np
>>> x = np.array([[1,0,0],[0,0,1],[0,1,0]])
>>> y = np.array([[3,4,5],[6,7,8],[3,2,1]])
>>> x
array([[1, 0, 0],
       [0, 0, 1],
       [0, 1, 0]])
>>> y
array([[3, 4, 5],
       [6, 7, 8],
       [3, 2, 1]])
```
*  einsum 是不是矩阵乘积呢？我们试一下
```python
>>> x@y
array([[3, 4, 5],
       [3, 2, 1],
       [6, 7, 8]])
>>> einsum(x,y,'a b, c d -> a d')
array([[12, 13, 14],
       [12, 13, 14],
       [12, 13, 14]])
```
* 发现并不一样！所以 einsum 不是矩阵乘积。再观察，[12 13 14] 分别排列了三行，看起来很有规律。但我们一时想不出 12 13 14 这三个数是怎么来的。继续实验。如果不是'a d'而是'a b'它会输出 x 本身吗？
```python
>>> einsum(x,y,'a b, c d -> a b')
array([[39,  0,  0],
       [ 0,  0, 39],
       [ 0, 39,  0]])
```
* 并不会，但是这个 array 看起来也很有规律。三个 39 的位置表现了 x 的信息，那么 39 这个数字本身一定来自于第二个数组 y。
```python
>>> y.sum()
39
```
* 原来是把第二个数组 sum 了一下，乘到第一个数组上了。我们分别实验'a b'和'c d'可以发现同样的结论
```python
>>> x
array([[1, 0, 0],
       [0, 0, 1],
       [0, 1, 0]])
>>> einsum(x,y,'a b, c d -> a b')
array([[39,  0,  0],
       [ 0,  0, 39],
       [ 0, 39,  0]])
>>> y.sum()
39
>>> y
array([[3, 4, 5],
       [6, 7, 8],
       [3, 2, 1]])
>>> einsum(x,y,'a b, c d -> c d')
array([[ 9, 12, 15],
       [18, 21, 24],
       [ 9,  6,  3]])
>>> x.sum()
3
```
* 再推广一下，可能是我们输入了'a b c d'四个维度，然后把要输出的'a b'（或者'c d'）保留，剩下的'c d'（或者'a b'）进行求和。那么如果是'a d'或者'c d'呢。
```python
>>> einsum(x,y,'a b, c d -> a d')
array([[12, 13, 14],
       [12, 13, 14],
       [12, 13, 14]])
>>> x.sum(axis=1)
array([1, 1, 1])
>>> y.sum(axis=0)
array([12, 13, 14])

>>> einsum(x,y,'a b, c d -> b c')
array([[12, 21,  6],
       [12, 21,  6],
       [12, 21,  6]])
>>> x.sum(axis=0)
array([1, 1, 1])
>>> y.sum(axis=1)
array([12, 21,  6])
```
* 这样就解开了上边 [12 13 14] 数字得出的谜团。因为 x 不管沿axis 0 还是 axis 1 求和都是 [1 1 1] 所以比较容易观察规律。就是**把输出的维度保留，剩下的维度求和**。
* 再看一下顺序对输出的影响，可以发现会有一个转置的效果。
```python
>>> einsum(x,y,'a b, c d -> a d')
ab,cd->ad
array([[12, 13, 14],
       [12, 13, 14],
       [12, 13, 14]])
>>> einsum(x,y,'a b, c d -> d a')
ab,cd->da
array([[12, 12, 12],
       [13, 13, 13],
       [14, 14, 14]])
```
* 最后我们就可以解释下面的例子了
```python
>>> x, y, z = np.random.randn(3, 1, 2, 3)
>>> x
array([[[ 0.51613364, -1.64413418,  0.02056939],
        [-0.38257828,  1.15543751, -0.10533596]]])
>>> y
array([[[-0.15940847,  0.00430798,  0.19768969],
        [-0.2401132 ,  1.64144003, -1.79326939]]])
>>> z
array([[[ 0.23757063, -0.64599319, -1.03294572],
        [-0.21582711,  1.29888799, -1.75626082]]])
>>> x_s = x.sum(axis=(1,2),keepdims=True)
>>> y_s = y.sum(axis=(0,2),keepdims=True)
>>> z_s = z.sum(axis=(0,1),keepdims=True)
>>> x_s
array([[[-0.43990787]]])
>>> y_s
array([[[ 0.04258921],
        [-0.39194256]]])
>>> z_s
array([[[ 0.02174352,  0.65289481, -2.78920655]]])
>>> x_s * y_s * z_s
array([[[-4.07371907e-04, -1.22321979e-02,  5.22566975e-02],
        [ 3.74898712e-03,  1.12571219e-01, -4.80911134e-01]]])
>>> einsum(x, y, z, "a b c, d e f, g h i -> a e i")
array([[[-4.07371907e-04, -1.22321979e-02,  5.22566975e-02],
        [ 3.74898712e-03,  1.12571219e-01, -4.80911134e-01]]])
```
* 这样的应用案例就是（也是官网的）
```python
>>> batched_images = np.random.randn(128, 16, 16)
>>> filters = np.random.randn(16, 16, 30)
>>> result = einsum(batched_images, filters,
...                 "batch h w, h w channel -> batch channel")
>>> result.shape
(128, 30)
```

### pack
    """
    Packs several tensors into one.
    See einops tutorial for introduction into packing (and how it replaces stack and concatenation).

    Parameters:
        tensors: tensors to be packed, can be of different dimensionality
        pattern: pattern that is shared for all inputs and output, e.g. "i j * k" or "batch seq *"

    Returns:
        (packed_tensor, packed_shapes aka PS)

    Example:
    ```python
    >>> from numpy import zeros as Z
    >>> inputs = [Z([2, 3, 5]), Z([2, 3, 7, 5]), Z([2, 3, 7, 9, 5])]
    >>> packed, ps = pack(inputs, 'i j * k')
    >>> packed.shape, ps
    ((2, 3, 71, 5), [(), (7,), (7, 9)])
    ```

    In this example, axes were matched to: i=2, j=3, k=5 based on order (first, second, and last).
    All other axes were 'packed' and concatenated.
    PS (packed shapes) contains information about axes that were matched to '*' in every input.
    Resulting tensor has as many elements as all inputs in total.

    Packing can be reversed with unpack, which additionally needs PS (packed shapes) to reconstruct order.

    ```python
    >>> inputs_unpacked = unpack(packed, ps, 'i j * k')
    >>> [x.shape for x in inputs_unpacked]
    [(2, 3, 5), (2, 3, 7, 5), (2, 3, 7, 9, 5)]
    ```

    Read the tutorial for introduction and application scenarios.
    """
1. 应用，channel 上的堆叠
```python
from einops import pack, unpack

h, w = 100, 200
# image_rgb is 3-dimensional (h, w, 3) and depth is 2-dimensional (h, w)
image_rgb = np.random.random([h, w, 3])
image_depth = np.random.random([h, w])
# but we can stack them
image_rgbd, ps = pack([image_rgb, image_depth], 'h w *')
```
2.下面这个例子就是，[i, j , \*, k]，对于第一个 Z([2,3,5])，[2,3,5]就是[i,j,k]。然后
*代表其他的张量多的维度往这里边插。71 = 1 + 7 + 7\*9
```python
>>> from numpy import zeros as Z
>>> inputs = [Z([2, 3, 5]), Z([2, 3, 7, 5]), Z([2, 3, 7, 9, 5])]
>>> packed, ps = pack(inputs, 'i j * k')
>>> packed.shape, ps
((2, 3, 71, 5), [(), (7,), (7, 9)])
   ```
### unpack
    """
    Unpacks a single tensor into several by splitting over a selected axes.
    See einops tutorial for introduction into packing (and how it replaces stack and concatenation).

    Parameters:
        tensor: tensor to be unpacked
        packed_shapes: packed_shapes (aka PS) is a list of shapes that take place of '*' in each output.
            output will contain a single tensor for every provided shape
        pattern: pattern that is shared for input and all outputs, e.g. "i j * k" or "batch seq *",
            where * designates an axis to be unpacked

    Returns:
        list of tensors

    If framework supports views, results are views to the original tensor.

    Example:
    ```python
    >>> from numpy import zeros as Z
    >>> inputs = [Z([2, 3, 5]), Z([2, 3, 7, 5]), Z([2, 3, 7, 9, 5])]
    >>> packed, ps = pack(inputs, 'i j * k')
    >>> packed.shape, ps
    ((2, 3, 71, 5), [(), (7,), (7, 9)])
    ```

    In this example, axes were matched to: i=2, j=3, k=5 based on order (first, second, and last).
    All other axes were 'packed' and concatenated.
    PS (packed shapes) contains information about axes that were matched to '*' in every input.
    Resulting tensor has as many elements as all inputs in total.

    Packing can be reversed with unpack, which additionally needs PS (packed shapes) to reconstruct order.

    ```python
    >>> inputs_unpacked = unpack(packed, ps, 'i j * k')
    >>> [x.shape for x in inputs_unpacked]
    [(2, 3, 5), (2, 3, 7, 5), (2, 3, 7, 9, 5)]
    ```

    Read the tutorial for introduction and application scenarios.
    """
pack 是堆叠，unpack 就是分开。还是刚才的例子，我们把一个彩色图片和黑白图片堆叠在一起了。现在要分开。
```python
from einops import pack, unpack

h, w = 100, 200
# image_rgb is 3-dimensional (h, w, 3) and depth is 2-dimensional (h, w)
image_rgb = np.random.random([h, w, 3])
image_depth = np.random.random([h, w])
# but we can stack them
image_rgbd, ps = pack([image_rgb, image_depth], 'h w *')
# then split
unpacked_rgb, unpacked_depth = unpack(image_rgbd, ps, 'h w *')
```