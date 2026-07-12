# Day 12 · messages 多轮对话流程图

> 学完 Day 12 后，将下方 Mermaid 图复制到 `学习笔记.md` 对应章节即可。  
> VS Code / GitHub / 多数 Markdown 预览支持 Mermaid 渲染。

---

## 总览：D7 单轮 vs D12 多轮

```mermaid
flowchart TB
    subgraph D7["D7 单轮 · 每次失忆"]
        direction TB
        D7A["post 发送"] --> D7B["messages = [<br/>  user: 当前问题<br/>]"]
        D7B --> D7C["response 回答"]
        D7C --> D7D["❌ 不保存历史<br/>下一轮又是全新 messages"]
    end

    subgraph D12["D12 多轮 · 带会话笔记本"]
        direction TB
        D12A["messages 列表持续累积"] --> D12B["每轮 post 发送<strong>整包</strong> messages"]
        D12B --> D12C["response 后 append assistant"]
        D12C --> D12D["✅ 下一轮仍带上之前所有对话"]
    end

    style D7 fill:#fff5f5,stroke:#e57373
    style D12 fill:#f1f8e9,stroke:#81c784
```

---

## 多轮对话详细流程（两轮示例）

```mermaid
sequenceDiagram
    autonumber
    participant 用户
    participant messages as messages 列表
    participant API as DeepSeek API

    Note over messages: 启动时<br/>[system: 你是友好助手]

    rect rgb(232, 245, 253)
        Note right of 用户: 第一轮
        用户->>messages: 我叫小明
        Note over messages: append user<br/>[system, user:我叫小明]
        messages->>API: post（整包 messages）
        API-->>messages: 你好，小明！
        Note over messages: append assistant<br/>[system, user, assistant]
    end

    rect rgb(255, 243, 224)
        Note right of 用户: 第二轮
        用户->>messages: 我叫什么？
        Note over messages: append user<br/>[system, user, assistant, user:我叫什么？]
        messages->>API: post（含完整历史）
        API-->>messages: 你叫小明。
        Note over messages: append assistant<br/>历史继续变长…
    end
```

---

## messages 列表变化（表格版）

### 第一轮：「我叫小明」

| 步骤 | 操作 | messages 内容 |
|------|------|----------------|
| 0 | 程序启动 | `[system]` |
| 1 | `append` user | `[system, user: 我叫小明]` |
| 2 | **post → API** | ↑ 发送这一包 |
| 3 | 收到回答 | assistant: `你好，小明！` |
| 4 | `append` assistant | `[system, user, assistant]` |

### 第二轮：「我叫什么？」

| 步骤 | 操作 | messages 内容 |
|------|------|----------------|
| 5 | `append` user | `[system, user, assistant, user: 我叫什么？]` |
| 6 | **post → API** | ↑ 模型能看到第一轮 → 能答「小明」 |
| 7 | 收到回答 | assistant: `你叫小明。` |
| 8 | `append` assistant | 历史继续累积… |

---

## 核心代码对应

```python
# 会话笔记本（程序启动时创建，整个聊天期间一直存在）
messages = [
    {"role": "system", "content": "你是友好的助手。"},
]

# 每一轮循环里：
messages.append({"role": "user", "content": question})   # ① 用户话入本
answer = ask_ai(messages)                                 # ② 整本 post 给 API
messages.append({"role": "assistant", "content": answer}) # ③ AI 话也入本
```

---

## 三个 role

```mermaid
flowchart LR
    S["system<br/>定规矩"] --> U["user<br/>用户说的"]
    U --> A["assistant<br/>AI 说的"]
    A --> U2["user<br/>下一轮…"]
    U2 --> A2["assistant<br/>…"]

    style S fill:#e3f2fd,stroke:#1976d2
    style U fill:#fff9c4,stroke:#f9a825
    style U2 fill:#fff9c4,stroke:#f9a825
    style A fill:#e8f5e9,stroke:#388e3c
    style A2 fill:#e8f5e9,stroke:#388e3c
```

---

## 为什么要 trim_history？（Day 12 ② 预习）

```mermaid
flowchart TB
    A["聊得越久<br/>messages 越长"] --> B["Token 越多"]
    B --> C["更慢 · 更贵"]
    B --> D["可能超出上下文窗口"]
    E["trim_history<br/>只留最近 N 轮"] --> F["system 永远保留<br/>旧对话丢掉"]
    F --> G["✅ 控制成本与长度"]

    style A fill:#ffebee
    style E fill:#e8f5e9
```

---

## 粘贴到笔记时可用的一句话

> **多轮对话**：用 `messages` 列表累积 `user` / `assistant` 交替记录；每轮把**整包**发给 API，模型并无记忆，是靠历史消息才「记得」上文。
