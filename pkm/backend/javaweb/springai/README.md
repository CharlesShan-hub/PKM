# spring-ai

> Spring AI 是 Spring 生态中专为 AI 工程设计的应用框架，让 Java 开发者用 Spring 方式集成 AI 能力

## 实战项目

项目路径：`D:\project\work\learn-springai`

### 项目结构

```
learn-springai/
├── pom.xml                              # Spring Boot 3.3 + Spring AI 1.1.3
├── start.bat                            # 一键启动脚本
├── src/main/java/com/learn/springai/
│   ├── LearnSpringAiApplication.java    # 启动类
│   ├── config/
│   │   └── ChatClientConfig.java        # ChatClient 单例配置
│   ├── controller/
│   │   ├── ChatController.java          # 模块2: 基础 ChatClient 用法
│   │   ├── PromptTemplateController.java # 模块2: Prompt 模板化
│   │   ├── StructuredOutputController.java # 模块3: 结构化输出
│   │   ├── ToolController.java          # 模块4: 函数调用 @Tool
│   │   ├── MemoryController.java        # 模块5: 对话记忆 Advisors
│   │   └── RagController.java           # 模块6: 检索增强生成 RAG
│   ├── model/
│   │   ├── CodeReviewRequest.java       # 代码审查请求体
│   │   ├── CodeReviewResult.java        # 结构化审查结果
│   │   ├── MovieRecommendation.java     # 电影推荐结构化输出
│   │   └── MeetingMinutes.java          # 会议纪要结构化输出
│   └── service/
│       └── ToolService.java             # @Tool 工具定义
└── src/main/resources/
    ├── application.yml                  # 配置（DeepSeek API）
    └── prompts/
        ├── translate.st                 # 翻译模板
        └── sql-generator.st             # SQL 生成模板
```

### 接口一览

| 模块 | 接口 | 说明 |
|:---|:---|:---|
| 基础 | `GET /ai/chat?message=你好` | 最简单的对话 |
| 基础 | `GET /ai/expert?question=...` | 带角色的专家问答 |
| 基础 | `GET /ai/stream?message=...` | 流式打字机效果 |
| 基础 | `POST /ai/code-review` | 代码审查助手 |
| 模板 | `GET /ai/template/translate` | 翻译助手（代码内模板） |
| 模板 | `GET /ai/template/translate-file` | 翻译助手（外部文件模板） |
| 模板 | `GET /ai/template/sql` | SQL 生成器 |
| 结构化 | `POST /ai/structured/code-review` | 审查结果返回 POJO |
| 结构化 | `GET /ai/structured/movies` | 电影推荐返回 POJO |
| 结构化 | `POST /ai/structured/meeting-minutes` | 会议纪要提取 |
| 函数调用 | `GET /ai/tool/chat?message=现在几点` | 带工具调用的对话 |
| 函数调用 | `GET /ai/tool/weather?city=北京` | 天气查询 |
| 函数调用 | `GET /ai/tool/calculate?expression=计算1+2` | 数学计算 |
| 对话记忆 | `GET /ai/memory/chat?sessionId=xx&message=...` | 多轮对话 |
| 对话记忆 | `GET /ai/memory/clear?sessionId=xx` | 清除记忆 |
| RAG | `GET /ai/rag/ask?question=年假几天` | 知识库问答 |

* [springai-overview.md](notes/springai-overview.md)
* [springai-chatclient.md](notes/springai-chatclient.md)
* [springai-structured-output.md](notes/springai-structured-output.md)
* [springai-tool-calling.md](notes/springai-tool-calling.md)
* [springai-advisors.md](notes/springai-advisors.md)
* [springai-rag.md](notes/springai-rag.md)
* [springai-vector-store.md](notes/springai-vector-store.md)
* [springai-mcp-agent.md](notes/springai-mcp-agent.md)
* [springai-production.md](notes/springai-production.md)