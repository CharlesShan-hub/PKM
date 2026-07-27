# 第三章总结：构建 ASN.1 规范的结构

**核心内容**：模块结构、模块头、导出/导入、标签环境、可扩展性环境

---

### 1. 模块基本结构
```
ModuleName {OID} DEFINITIONS [TAGS] ::= BEGIN
    EXPORTS ...;
    IMPORTS ... FROM ModuleName {OID};
    -- 类型/值定义 --
END
```
- 模块头必需，`END` 必需
- `OID`（模块标识符）可选但推荐，需全球唯一

### 2. 模块头要素
| 要素 | 说明 |
|------|------|
| 模块名称 | 大写开头，标识模块 |
| 模块标识符 | OID，全局唯一 |
| 标签环境 | `EXPLICIT TAGS` / `IMPLICIT TAGS` / `AUTOMATIC TAGS` |
| 可扩展性环境 | 默认需显式标记，`EXTENSIBILITY IMPLIED` 自动添加 |

### 3. 标签环境
- **显式标签（EXPLICIT）**：添加外层 TLV 包装，保留原类型信息，适合 CHOICE，但更冗长
- **隐式标签（IMPLICIT）**：替换原 T 值，更紧凑，但 CHOICE 类型禁用
- **自动标签（AUTOMATIC TAGS）**：自动从 `[0]` 开始对所有元素/选项编号，推荐使用，可避免手动标签冲突

### 4. 可扩展性标记
- **省略号 `...`** 标记插入点，允许 v2 添加元素
- **异常规范**（以 `!` 开头）：定义 v1 系统收到 v2 新元素时的行为
- **EXTENSIBILITY IMPLIED**：所有允许扩展的结构自动在末尾加 `...`，但插入点固定在最末

### 5. EXPORTS / IMPORTS
- **EXPORTS**：输出类型给其他模块；省略则默认输出所有；`EXPORTS ;` 禁止任何输出
- **IMPORTS**：从其他模块引用类型
- 可中继导入（A 导入 B，再导出 B 给 C）
- 导入的类型保留原模块的标签/可扩展性环境

### 6. 发布格式建议
- ASN.1 应集中于附录，而非散落在正文各处
- 提供机器可读的 ASCII 或 UTF-8 副本
- 避免重复文本导致不一致
- 可加行号便于交叉引用，但工具使用前需删除

### 7. 完整规范的构建
- 顶层类型 + 递归引用链 + 导入导出链 = 完整规范
- 多个模块可共用同一 OID 前缀（自动编号）
- **`ABSTRACT-SYNTAX`** 语句标识顶层类型，可附加 `has-property` 说明（如 `handles-invalid-encodings`）