# pickle

以下内容由deepseek生成：

**`pickle`** 是 Python 的一个**内置库**，用于**对象的序列化和反序列化**（即：将 Python 对象转换为字节流，或从字节流还原对象）。它可以将内存中的对象保存到文件或通过网络传输，之后再恢复成原始对象。

---

## **1. 核心功能**
• **序列化（Pickling）**：将对象 → 字节流  
  ```python
  import pickle

  data = {"name": "Alice", "age": 30}
  serialized = pickle.dumps(data)  # 对象 → 字节流
  ```
• **反序列化（Unpickling）**：字节流 → 对象  
  ```python
  restored_data = pickle.loads(serialized)  # 字节流 → 对象
  print(restored_data)  # 输出: {'name': 'Alice', 'age': 30}
  ```

---

## **2. 常用场景**
### **(1) 保存/加载对象到文件**
```python
# 保存到文件
with open("data.pkl", "wb") as f:
    pickle.dump(data, f)

# 从文件加载
with open("data.pkl", "rb") as f:
    loaded_data = pickle.load(f)
```

### **(2) 跨进程或网络传输**
• 将对象序列化后发送，接收方反序列化还原（需注意安全性风险）。

---

## **3. 支持的 Python 对象类型**
`pickle` 可以处理绝大多数 Python 对象，包括：
• 基础类型：`int`, `str`, `list`, `dict`, `set` 等  
• 自定义类实例（需类定义在反序列化时可访问）  
• 函数、类（需模块可导入）  
• 嵌套对象  

---

## **4. 结合 `dataclass` 和 `Enum` 的示例**
如果之前的 `dataclass` + `Enum` 对象需要序列化：
```python
from dataclasses import dataclass
from enum import Enum
import pickle

@dataclass
class RoleAttributes:
    health: int
    attack: int

class CharacterType(RoleAttributes, Enum):
    WARRIOR = 100, 10
    ARCHER = 70, 15

# 序列化
serialized = pickle.dumps(CharacterType.WARRIOR)

# 反序列化
restored = pickle.loads(serialized)
print(restored == CharacterType.WARRIOR)  # True
```

---

## **5. 注意事项**
### **(1) 安全性风险**
• **不要反序列化不受信任的数据**！`pickle` 可能执行任意代码（类似 `eval`）。  
• 安全替代方案：用 `json` 或 `marshal` 处理简单数据。

### **(2) 兼容性**
• Python 版本间可能不兼容（如 Py3.8 的 `pickle` 文件可能无法在 Py3.7 加载）。  
• 跨语言不支持（仅限 Python）。

### **(3) 自定义类的限制**
• 类定义必须在反序列化时可用（否则会报 `AttributeError`）。  
• 可通过定义 `__reduce__` 方法控制序列化行为。

---

## **6. 替代方案**
| 库          | 特点                               | 适用场景               |
|-------------|-----------------------------------|-----------------------|
| `json`      | 文本格式，跨语言，仅支持基础类型     | Web API、配置文件      |
| `marshal`   | Python 专用，比 `pickle` 更轻量    | 内部 Python 对象交换   |
| `shelve`    | 基于 `pickle` 的键值存储           | 本地持久化小型数据库   |

---

## **总结**
• **`pickle`** 是 Python 对象序列化的标准工具，适合保存复杂对象或临时状态。  
• **风险**：仅用于可信数据，避免安全漏洞。  
• **结合 `dataclass`/`Enum`**：可无缝序列化自定义类型，但需确保类定义可访问。  

如果需要跨语言或安全敏感场景，优先选择 `json` 或 Protobuf 等方案。