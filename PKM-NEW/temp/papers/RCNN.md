
# RCNN

![[assets/rcnn.png]]

* 将 AlexNet 与选择性搜索算法相结合，成功将 CNN 用在目标检测领域，提出了 RCNN算法。
* 生成 patch
  *   首先采用选择性搜索算法提取 2000 个候选区域。

      其他的算法：“objectness \[1],  **本文选择 selective search** \[39], category-independent object proposals \[14], constrained parametric min-cuts (CPMC) \[5], multi-scale combinatorial grouping \[3], and Cires ̧an et al. \[6]”&#x20;


  *   然后对每个候选区域进行归一化，后续逐个输入 CNN中提取特征。

      * (A) the original object proposal at its actual scale relative to the transformed CNN inputs;&#x20;
      * (B) tightest square with context;&#x20;
      * (C) tightest square without context;&#x20;
      * **本文选择(D)** warp. Within each column and example proposal, the top row corresponds to p = 0 pixels of context padding while the bottom row has p = 16 pixels of context padding.

      ![[assets/rcnn-transformations.png]]

      *   跟据 IoU≥0.5，判断是否为正样本。

          ![[assets/rcnn-ss.png]]
* 训练
  * 训练一个图片分类器（Supervised pre-training），比如 Alexnet on ILSVRC2012 classification.
  * 对分类器进行微调（Domain-specific fine-tuning），比如在 ILSVRC2013 中 N = 200，在 VOC 中 N = 20。这里加入一个背景类，所以输出为 21 类，在选择性搜索处理后的图像块组成的新数据加上做微调。lr=0.001，优化器为 SGD，每个类有32个正窗口和96个背景窗口，batch=128.
  * 为每一个类训练 SVM 二分类器（Object category classifiers），用来判断输入的 patch 是背景还是图像。如果 IoU≥0.3,就是正样本。这个参数作者调整过，已经是最佳。
  * （为何微调 AlexNet 时 IoU 阈值为 0.5，训练 SVM 时 IoU 阈值是 0.3？因为微调 AlexNet 时需要大量的正样本，所以放宽了要求。）
  * （为何要训练 SVM 二分类器而不是直接用微调的 AlexNet？因为 AlexNet是放宽了要求的，他预测出来就也不会很准确。作者认为后续可以不训练 SVM，通过更好的 Finetune 模型得到分类结果。）
  * 训练边界框微调模块（Bounding-box regression），对 SVM 预测出来的边界进行进一步调整。
* 推理
  * 某张图片生成 n 个 patch，输入到微调后的模型，得到特征（而不是分类结果）。
  * n 个 patch 输入到微调模型后得到 n 个特征，n 个特征输入到 m 个 SVM 中，得到 nxm 个得分，对 nxm 个得分进行 NMS（非极大值抑制）
  * NMS具体做法为，假设有 A、B、C、D、E、F是排号顺序的得分，A 最大，保留。然后查看 B，如果 IoU(A,B)≥阈值，就删除 B，假设 B，C 都被删除。现在到了 E，保留下来，再去判断 F。如果 F 被删除，那最后就有两个区域，A，E 是识别到的两个框。
  * 边界框微调（Bounding-box regression），对 SVM 预测出来的边界进行进一步调整。
* 优点：RCNN 算法在 PASCAL VOC 2007 数据集上的检测精度达到了 58.5%（2007年VOC的mAP为30.5%）。
* 改进空间
  * 对于单张图像提取的 2000个候选区域需要逐个输 入 CNN 中, 导致计算开销十分巨大。
  * 候选区域输入 CNN 前, 必须剪裁或缩放至固定大小, 这会使候选区域发生形变且丢失较多的信息, 导 致网络检测精度下降。
* 文中细节
  * “性能最好的方法是复杂的集成系统，通常将多个低级图像特征与高级上下文相结合。”所以 RCNN 用了很多模块来组成检测的任务。
  * 区域提案阶段有很大的改进空间。
