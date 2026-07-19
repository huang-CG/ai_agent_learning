# Day 18 · Agent 循环图

> 建议：先自己在纸上画「感知 → 推理 → 决策 → 执行 → 再感知」，再对照。

```mermaid
flowchart TD
  A[感知 Perceive<br/>用户输入 / 工具结果 / 文档…] --> B[推理 Reason<br/>CoT：现在怎样？缺什么？]
  B --> C{决策 Decide}
  C -->|可以直接答| D[生成最终回答]
  C -->|需要外部能力| E[执行 Act<br/>Function Calling / API / 检索…]
  E --> F[观察 Observation<br/>工具返回结果]
  F --> A
  D --> G[交给用户]
```

## 和你已学内容的挂钩

| 步骤 | 你学过的 |
|------|----------|
| 感知 | messages 里的 user；`role:tool` 结果；RAG 检索片段 |
| 推理 | CoT、System Prompt |
| 决策 | 模型选「直接 stop」还是 `tool_calls` |
| 执行 | 你的 Python `run_tool`；将来天气 API 等 |

**一句话**：Chatbot 常常只走到「推理→回答」；Agent 会在「决策→执行→再感知」上多转几圈。
