# Day 16 · RAG 流程图

> 建议：先自己在纸上画五步，再对照本图。

```mermaid
flowchart TD
  subgraph prep [离线准备 · 建库]
    A[原始文档] --> B[切块 chunk]
    B --> C[Embedding 模型]
    C --> D[向量]
    D --> E[(向量库<br/>Chroma / FAISS 等)]
  end

  subgraph online [在线问答 · 检索增强]
    F[用户问题] --> G[问题 Embedding]
    G --> H[向量相似度检索 top-k]
    E --> H
    H --> I[相关文档片段]
    I --> J[拼进 Prompt<br/>片段 + 问题]
    J --> K[LLM 生成回答]
    K --> L[用户看到答案]
  end
```

## 对照记忆

| 步 | 发生什么 | 谁在干活 |
|----|----------|----------|
| 1 | 文档切块 | 你的程序 / 平台 |
| 2 | 块 → 向量并入库 | Embedding 模型 + 向量库 |
| 3 | 问题 → 向量 | Embedding 模型 |
| 4 | 找最像的几块 | 向量库（相似度） |
| 5 | 片段 + 问题 → 回答 | LLM |

**和 Function Calling 的对比（帮助串联）：**

- FC：模型缺**能力**（算数、查时间）→ 调工具
- RAG：模型缺**知识**（你的文档）→ 先检索再答
