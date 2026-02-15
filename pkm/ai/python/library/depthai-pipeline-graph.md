# depthai-pipeline-graph

`depthai-pipeline-graph` 是一个 Python 库，用于构建和运行深度学习加速器（如 NVIDIA Jetson TX2 上的 NVIDIA TX2）的深度学习流水线。这个库提供了一种图形化的方式来定义和运行深度学习流水线，包括图像预处理、深度学习推理和后处理等步骤。 以下是 `depthai-pipeline-graph` 的关键特点和用法：

#### 关键特点

1. **图形化流水线定义**：允许你使用图形化的方式来定义深度学习流水线。
2. **实时处理**：支持实时视频处理和深度学习推理。
3. **丰富的功能**：提供多种深度学习模型和算法，如目标检测、图像识别、分割等。
4. **易用性**：提供简单的 API，易于集成到现有代码中。
5. **跨平台**：支持多种操作系统，包括 Linux 和 Windows。

#### 安装

可以通过pip安装`depthai-pipeline-graph`：

```bash
pip install depthai-pipeline-graph
```

#### 基本用法

以下是一些使用 `depthai-pipeline-graph` 的基本示例：

**初始化设备**

```python
import depthai as dai
# 创建一个深度学习加速器实例
device = dai.Device()
```

在这个例子中，我们创建了一个 `dai.Device` 实例，用于与深度学习加速器进行交互。

**创建流水线图**

```python
from depthai_pipeline_graph import PipelineGraph
# 创建一个流水线图实例
graph = PipelineGraph()
# 添加一个摄像头节点
graph.addNode('camera', 'RGB Camera', 'RGB')
# 添加一个神经网络节点
graph.addNode('nn', 'Neural Network', 'NN')
# 添加一个显示节点
graph.addNode('display', 'Display', 'Display')
```

在这个例子中，我们创建了一个 `depthai_pipeline_graph.PipelineGraph` 实例，并使用 `addNode` 方法来添加摄像头、神经网络和显示节点。

**连接节点**

```python
graph.connect('camera', 'nn')
graph.connect('nn', 'display')
```

在这个例子中，我们使用 `connect` 方法来连接摄像头节点和神经网络节点，以及神经网络节点和显示节点。

**运行流水线**

```python
graph.run()
```

在这个例子中，我们使用 `run` 方法来运行深度学习流水线。

#### 使用场景

* **机器人视觉**：在机器人视觉应用中，使用 `depthai-pipeline-graph` 来构建和运行深度学习流水线。
* **自动驾驶汽车**：在自动驾驶汽车中，使用 `depthai-pipeline-graph` 来处理和分析摄像头数据。
* **工业自动化**：在工业自动化中，使用 `depthai-pipeline-graph` 来识别和分类物体。 `depthai-pipeline-graph` 是一个非常实用的库，它可以帮助 Python 开发者高效地构建和运行深度学习流水线。由于其易用性和强大的功能，`depthai-pipeline-graph` 在需要实时深度学习推理的场景中非常有用。
