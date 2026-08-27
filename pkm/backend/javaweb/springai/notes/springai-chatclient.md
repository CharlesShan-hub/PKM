# ChatClient 与 Prompt 工程

## 一、ChatClient — Spring AI 的心脏

ChatClient 是 Spring AI 的高层 Fluent API，封装了底层 ChatModel，提供链式调用的编程体验。

### 类比理解

> ChatClient 之于 AI = JdbcTemplate 之于数据库
> 都封装了底层细节，提供了简洁的 Fluent API

### 基本用法

```java
@RestController
public class ChatController {

    private final ChatClient chatClient;

    public ChatController(ChatClient.Builder builder) {
        this.chatClient = builder.build();
    }

    // 最简单的调用
    @GetMapping("/ai/simple")
    String simpleChat(@RequestParam String message) {
        return chatClient.prompt()
                .user(message)
                .call()
                .content();
    }

    // 带 SystemMessage 的调用
    @GetMapping("/ai/expert")
    String expertChat(@RequestParam String question) {
        return chatClient.prompt()
                .system("你是一个资深的 Java 架构师，回答要专业、简洁、有代码示例")
                .user(question)
                .call()
                .content();
    }

    // 流式响应（打字机效果）
    @GetMapping("/ai/stream")
    Flux<String> streamChat(@RequestParam String message) {
        return chatClient.prompt()
                .user(message)
                .stream()
                .content();  // 返回 Flux<String>，前端 SSE 接收
    }
}
```

### ChatClient 的完整调用链

```
chatClient
    .prompt()                    // 创建 Prompt 构建器
    .system("...")               // 设置系统消息
    .user("...")                 // 设置用户消息
    .messages(list)              // 设置多轮对话历史
    .options(callOptions)        // 设置模型参数（temperature 等）
    .advisors(advisors)          // 添加 Advisors 链
    .call()                      // 同步调用
    .content();                  // 获取文本响应
// 或
    .stream()                    // 流式调用
    .content();                  // 获取 Flux<String>
// 或
    .entity(MyClass.class);      // 获取结构化输出（模块 3 讲）
```

## 二、Prompt 的三层消息结构

| 消息类型 | 角色 | 作用 | 示例 |
|:---|:---|:---|:---|
| SystemMessage | 系统 | 设定 AI 的角色和行为规则 | "你是一个专业的 Java 技术顾问" |
| UserMessage | 用户 | 用户的输入/问题 | "Spring AI 和 LangChain 有什么区别？" |
| AssistantMessage | 助手 | AI 的回复（多轮对话上下文） | "Spring AI 是 Spring 官方..." |

### 关键洞察

**SystemMessage 是最容易被忽视但最重要的！** 好的 SystemMessage 能让 AI 输出质量提升 10 倍。

```java
// ❌ 弱 SystemMessage
chatClient.prompt()
    .system("你是一个助手")
    .user("请解释 Spring AI 的架构")
    .call()
    .content();

// ✅ 强 SystemMessage
chatClient.prompt()
    .system("""
        你是一个资深的 Java 企业级架构师，专精于 Spring 生态。
        回答要求：
        1. 先给出核心概念的一句话总结
        2. 然后用代码示例说明
        3. 最后指出常见误区
        4. 如果涉及版本差异，请说明
        """)
    .user("请解释 Spring AI 的架构")
    .call()
    .content();
```

## 三、Prompt Template（模板化 Prompt）

### 为什么需要模板

- 避免字符串拼接导致的 Prompt Injection 风险
- 提高可复用性
- 易于维护和版本管理

### 基本用法

```java
// 定义模板
String template = """
    请用 {language} 回答以下问题：
    {question}
    
    要求：
    - 用 {style} 的风格回答
    - 控制在 {maxLength} 字以内
    """;

// 创建模板并填充参数
PromptTemplate promptTemplate = new PromptTemplate(template);
Message message = promptTemplate.createMessage(Map.of(
    "language", "中文",
    "question", "什么是依赖注入？",
    "style", "通俗易懂",
    "maxLength", "200"
));

// 使用
String answer = chatClient.prompt()
    .user(message)
    .call()
    .content();
```

### 进阶：从文件加载模板

```yaml
# resources/prompts/tech-consultant.st
你是一个 {role} 专家。
请用 {language} 回答以下问题：
{question}

风格要求：{style}
```

```java
@Value("classpath:prompts/tech-consultant.st")
private Resource promptResource;

public String consult(String question) {
    PromptTemplate template = new PromptTemplate(promptResource);
    Message message = template.createMessage(Map.of(
        "role", "Java 架构师",
        "language", "中文",
        "question", question,
        "style", "专业简洁"
    ));
    return chatClient.prompt().user(message).call().content();
}
```

## 四、流式响应（Streaming）

### 同步 vs 流式

| 对比 | 同步 (call) | 流式 (stream) |
|:---|:---|:---|
| 返回类型 | String | Flux<String> |
| 用户体验 | 等待全部生成后一次性显示 | 打字机效果，逐字显示 |
| 适用场景 | 简单问答、后台处理 | 聊天界面、实时交互 |
| 实现复杂度 | 低 | 中（前端需要 SSE 支持） |

### 流式代码示例

```java
@GetMapping(value = "/ai/stream", produces = MediaType.TEXT_EVENT_STREAM_VALUE)
Flux<String> stream(@RequestParam String message) {
    return chatClient.prompt()
            .user(message)
            .stream()
            .content();
}
```

前端用 EventSource 或 fetch + ReadableStream 接收。

## 五、模型参数控制（CallOptions）

```java
chatClient.prompt()
    .user("讲个笑话")
    .options(ChatOptionsBuilder.builder()
        .withTemperature(0.8f)      // 创造性：0=保守，1=创意
        .withMaxTokens(500)          // 最大输出长度
        .withTopP(0.9f)              // 核采样
        .build())
    .call()
    .content();
```

### 常用参数说明

| 参数 | 作用 | 建议值 |
|:---|:---|:---|
| temperature | 控制输出的创造性/随机性 | 0.3（事实类）/ 0.8（创意类） |
| maxTokens | 限制输出最大 Token 数 | 根据需求设定 |
| topP | 核采样，控制词汇选择的多样性 | 0.9 |
| frequencyPenalty | 降低重复内容 | 0.0-1.0 |

## 六、反模式

### ❌ 反模式 1：每次请求都创建新的 ChatClient

```java
// ❌ ChatClient 是重量级对象，应该复用
public String chat(String msg) {
    ChatClient client = ChatClient.builder(chatModel).build();  // 每次 new！
    return client.prompt().user(msg).call().content();
}
```

```java
// ✅ 注入单例
@Service
public class ChatService {
    private final ChatClient chatClient;
    
    public ChatService(ChatClient.Builder builder) {
        this.chatClient = builder.build();  // 只创建一次
    }
}
```

### ❌ 反模式 2：用字符串拼接构造 Prompt

```java
// ❌ 危险！容易受到 Prompt Injection
String prompt = "请用" + language + "回答：" + userInput;

// ✅ 使用 PromptTemplate
PromptTemplate template = new PromptTemplate("请用 {language} 回答：{question}");
```

### ❌ 反模式 3：忽略 SystemMessage

```java
// ❌ 没有 SystemMessage，AI 不知道自己的角色
chatClient.prompt().user("...").call().content();

// ✅ 设置 SystemMessage 让 AI 行为可控
chatClient.prompt()
    .system("你是一个专业的 Java 技术顾问，回答要准确、简洁")
    .user("...")
    .call()
    .content();
```

## 七、最佳实践总结

1. **ChatClient 作为单例注入**，不要每次创建
2. **总是设置 SystemMessage**，明确 AI 的角色
3. **用 PromptTemplate 代替字符串拼接**
4. **交互式场景用 stream()**，后台处理用 call()
5. **根据任务类型调整 temperature**：事实类用低值，创意类用高值
6. **Prompt 模板从外部文件加载**，方便管理和版本控制