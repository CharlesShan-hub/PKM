# Spring AI 概览与 Hello World

## 一、什么是 Spring AI

Spring AI 是 **Spring 官方**推出的 AI 工程应用框架，于 2024 年正式推出，2025 年 5 月发布 1.0 GA，2026 年 6 月发布 2.0 GA。

### 核心定位

> Spring AI = Spring 生态的"AI 集成抽象层"
> 就像 JDBC 统一了数据库访问、Spring Data 统一了数据存储一样，Spring AI 统一了 AI 模型的接入方式

### 关键认知

- ✅ 它是**按 Spring 设计理念**从零构建的（可移植性、模块化、POJO 驱动）
- ❌ 它不是 "Java 版的 LangChain"（不是 Python 移植）

### 解决的核心问题

**连接企业数据与 API 到 AI 模型**。在 Spring AI 之前，每个 AI 提供商都有自己的 SDK，切换模型意味着重写代码。

## 二、核心特性

| 特性                    | 说明                         |
| :-------------------- | :------------------------- |
| Chat Completion       | 同步/流式对话，支持主流 AI 提供商        |
| Embedding             | 文本向量化                      |
| Text to Image         | 文生图（DALL-E、Stability AI 等） |
| Audio Transcription   | 语音转文字                      |
| Text to Speech        | 文字转语音                      |
| Structured Output     | AI 输出映射为 Java POJO         |
| Vector Store          | 支持 20+ 向量数据库               |
| Tool/Function Calling | 工具调用，连接外部系统                |
| Advisors 链            | 类似 Servlet Filter 的横切关注点机制 |
| MCP 协议                | 标准化跨进程工具调用（v2.0）           |

## 三、支持的主流 AI 提供商

- OpenAI（GPT-4o、GPT-4 等）
- Anthropic（Claude 系列）
- Google（Gemini）
- Microsoft（Azure OpenAI）
- Amazon（Bedrock）
- Ollama（本地模型，免费）
- DeepSeek
- 百度文心一言
- 阿里通义千问
- 等等 20+ 家

## 四、架构概览

```
用户输入
    ↓
Spring Boot Controller
    ↓
ChatClient（高层 Fluent API）
    ↓
Advisors 链（记忆、RAG、安全过滤…）
    ↓
ChatModel（底层抽象接口）
    ↓
AI 提供商适配器（OpenAI / Anthropic / Ollama…）
    ↓
AI 模型
```

## 五、Hello World 示例

### 环境要求

- JDK 17+
- Spring Boot 3.2+
- Maven 或 Gradle

### Maven 依赖

```xml
<dependency>
    <groupId>org.springframework.ai</groupId>
    <artifactId>spring-ai-openai-spring-boot-starter</artifactId>
    <version>1.1.0</version>
</dependency>
```

### 配置（application.yml）

```yaml
spring:
  ai:
    openai:
      api-key: ${OPENAI_API_KEY}
      chat:
        options:
          model: gpt-4o
```

### 代码

```java
@RestController
public class ChatController {

    private final ChatClient chatClient;

    public ChatController(ChatClient.Builder builder) {
        this.chatClient = builder.build();
    }

    @GetMapping("/ai")
    String chat(@RequestParam String message) {
        return chatClient.prompt()
                .user(message)
                .call()
                .content();
    }
}
```

### 效果

访问 `GET /ai?message=你好，请介绍一下自己` → 返回 AI 的自我介绍

## 六、ChatModel vs ChatClient

| 对比维度 | ChatModel（底层） | ChatClient（高层） |
|:---|:---|:---|
| 抽象级别 | 底层接口，直接调用 AI 模型 | 高层 Fluent API，封装了 ChatModel |
| 使用场景 | 需要精细控制或自定义集成 | **90% 的场景用这个** |
| 流式支持 | 手动处理 | 内置 `.stream()` |
| Advisors 链 | 不支持 | 原生支持 |
| 结构化输出 | 手动解析 | 内置 `.entity()` |
| 建议 | 少用 | **首选** |

## 七、多模型切换

Spring AI 最大的优势之一：**切换模型只需改依赖和配置，代码不变**

```yaml
# 从 OpenAI 切到 Ollama（本地模型）
spring:
  ai:
    ollama:
      chat:
        options:
          model: llama3
```

代码完全不用改，因为都是面向 `ChatClient` 编程。

## 八、学习路径

按顺序学习：
1. ✅ 本模块：概览与 Hello World
2. ChatClient 与 Prompt 工程
3. 结构化输出
4. 函数调用（@Tool）
5. 记忆与对话管理（Advisors 链）
6. RAG 检索增强生成
7. 向量数据库集成
8. MCP 协议与 Agent 开发
9. 生产化部署与最佳实践