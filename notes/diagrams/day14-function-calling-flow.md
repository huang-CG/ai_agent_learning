# Day 14 · Function Calling 流程图

> 先**自己手绘**再对照本页。D14 验收：能讲清每一步「谁在干活」。

---

## 总览（五步）

```mermaid
sequenceDiagram
    participant U as 用户
    participant App as 你的程序
    participant LLM as LLM API
    participant F as Python 函数

    U->>App: ①「广州天气怎么样？」
    App->>LLM: ② messages + tools 说明书
    LLM-->>App: ③ tool_calls<br/>get_weather(city=广州)
    App->>F: ④ 执行 get_weather
    F-->>App: 「晴，28℃」
    App->>LLM: ⑤ messages 追加<br/>assistant(tool_calls) + tool(结果)
    LLM-->>App: 自然语言回答
    App->>U: 「广州今天晴，28℃」
```

---

## 和「普通聊天」对比

```mermaid
flowchart LR
    subgraph 普通 D7/D12
        A1[user] --> A2[LLM] --> A3[assistant 直接答]
    end

    subgraph Function Calling
        B1[user] --> B2[LLM 看 tools]
        B2 -->|需要工具| B3[assistant tool_calls]
        B3 --> B4[程序执行函数]
        B4 --> B5[role tool 结果]
        B5 --> B6[LLM 再答]
        B2 -->|不需要| B6
    end
```

---

## messages 增长示意

```
第 1 次请求：
  [ system?, user: 广州天气怎么样？ ]  + tools=[...]

第 1 次响应：
  assistant: tool_calls=[get_weather({city:广州})]

第 2 次请求：
  [ ...上面历史...,
    assistant(tool_calls),
    tool: "晴，28℃" ]

第 2 次响应：
  assistant: "广州今天晴，气温 28℃。"  ← 给用户看的
```

---

## 记忆口诀

**说明书给模型 → 模型点菜（tool_calls）→ 厨房是你（执行）→ 上菜回模型 → 模型对人说话**
