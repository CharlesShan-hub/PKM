# 基础专题

## 基础定义

* 什么是机器学习
  * 李宏毅：很多应用场景都是根据给定输入进行处理后进行输出，其过程可以抽象成一个函数，机器学习就是通过给定大量数据，学习到这样的一个函数。
* 机器学习的种类
  * 回归（regression）：函数的输出是一个标量（scaler）。比如，预测明天温度。
  * 分类（classification）：函数输出的是类别（class）。比如，判断邮件是否为垃圾邮件，AlphaGo下围棋（判断 19x19 的个位置要取哪一个）。
  * 结构化学习（structured learning）：（参考：[大佬笔记](https://www.cnblogs.com/wry789/p/13215042.html)）函数输出是一个结构化的数据，比如图片，语句等等。比如，语音识别、机器翻译、句法解析、目标检测
* 如何找到这个函数

<img src="../../.gitbook/assets/ml-workflow.excalidraw.svg" alt="" class="gitbook-drawing">

1. 我们的主要目标是根据特定的数据学到一个模型。假设任务是预测天气。
2. 首先定义一个模型，比如最简单的线性模型，明天天气是今天天气的 k 倍+ b。
3. 通过模型得到的结果和真实结果的误差可以进一步计算的到 MAE 或 MSE。
   1. $$MAE = \frac{1}{n}\sum_{i=1}^{n}|y_i - \hat{y}_i|$$
   2. $$MSE = \frac{1}{n}\sum_{i=1}^{n}(y_i - \hat{y}_i)^2$$
4. 误差表面(error surface)：根据不同的超参数，绘制误差。
5. 优化：通过梯度下降等方法找到误差最小的地方。

## 经验误差

前提：$$m$$个样本中$$\alpha$$个样本分类错误

* 错误率：$$E=\alpha / m$$
* 精度：$$1-E = (1-\alpha/m)\times 100\%$$
* 误差（error）：实际输出与真实输出的差异
  * 训练集上的误差：训练误差（training error）或经验误差（empirical error）
  * 新样本上的误差：泛化误差（generalization error）
* 过拟合（over fitting）：训练样本自身特点当成泛化规律，模型变得教条
* 欠拟合（under fitting）：未能掌握足够的泛化规律

## 评估方法

### 留出法（hold-out）

1. 主要思路：将数据集分成两个部分，一个较大的训练集（用于训练模型）和一个较小的测试集（用于评估模型性能）。
2. 划分比例：训练集（2/3～4/5），测试集（1/3～1/5）
3. 各种样本按照类别采用分层采样，比如正例和反例需要分别分成两部分然后再组成训练集和测试集
4. 单次使用留出法会使结果不稳定（被分到测试集的数据永远不会提供经验），一般会多次使用留出法，每次都进行随机划分。

### k 折交叉验证（ k-fold cross validation）

1. 主要思路：将整个数据集随机分成k个大小大致相等的子集。每个子集都将成为一次测试集。
2. k 通常取 10，也可以取 5 或 20
3. p 次 k 折交叉验证：k 折交叉验证做 p 次求平均。比如 10 次 10 折交叉验证，做了 100 次训练。
4. 留一法（Leave-One-Out，LOO）：一种特殊的交叉验证方法，其中k的值等于数据集中的样本数量。

### 自助法（bootstrapping）

1. 主要思路：在 m 个原始数据中每次挑一个，一共挑 m 次，有放回，每次挑出来都复制一份到训练集中一次，这样训练集中也有 m 个数据。
2. 没被取到的概率：$$\lim_{m\to\infty}(1-\frac{1}{m})^m ≈ 0.368$$，这一部分就作为验证集。
3. 好处：交叉验证会让训练集变小。自助法不会让训练集变小，适合数据很少的情况。
4. 坏处：训练集的数据分布不同了，因为有重复数据。

## 性能度量

### 错误率与精度

可以从离散的数数，和概率角度，两个方向去统计错误率和精读（正确率）

### 混淆矩阵、查准率、全检率、F1

* 混淆矩阵（**Confusion Matrix**）

> [\[机器学习笔记\] 混淆矩阵（Confusion Matrix）](https://blog.csdn.net/seagal890/article/details/105059498)

|      | 预测正例    | 预测反例    |
| ---- | ------- | ------- |
| 真实正例 | TP（真正例） | FN（假反例） |
| 真实反例 | FP（假正例） | TN（真反例） |

* 精确率

$$
Accuracy = \frac{TP+TN}{TP+FN+FP+TN}
$$

* 查准率，正确率：预测为正确的，有多少真正确

$$
Precision = \frac{TP}{TP+FP}
$$



* 全检率，召回率：正例中，多少被预测到了

查准率和查全率是一对矛盾的指标。一般来说，查准率高时，查全率往往偏低；二查全率高时，查准率往往偏低。

$$
Recall = Sensitivity(True Positive Rate，TPR) = \frac{TP}{TP+FN}
$$

* 负正确率：预测为正确的，但其实是错误的，占所有错误的比率，越低越好

$$
False Positive Rate, FPR = \frac{FP}{TN+FP}
$$

* 特异性：识别为负类的样本的数量，占总的负类样本数量的比值

$$
Specificity = 1-FPR
$$

* Fβ\_Score：正确率和召回率的一种加权平均，召回率的权重是正确率的β倍

$$
F\beta = \beta \cdot Recall + Precision
$$

* F1\_Score：正确率和召回率的调和平均数

$$
F1 = Recall + Precision
$$





## Reference

\[1] [【機器學習2021】預測本頻道觀看人數 (上) - 機器學習基本概念簡介](https://www.youtube.com/watch?v=Ye018rCVvOo\&list=PLJV\_el3uVTsMhtt7\_Y6sgTHGHp1Vb2P2J)

\[2] 大佬笔记：[西瓜书学习笔记(1)--绪论](https://www.heywhale.com/mw/project/5e4f83590e2b66002c1f574b)

\[3] 大佬笔记：[西瓜书学习笔记(2)--模型的评估与选择](https://www.heywhale.com/mw/project/5e4f89fb0e2b66002c1f6468)

