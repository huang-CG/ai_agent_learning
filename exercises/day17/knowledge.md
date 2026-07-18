# AI Agent 90 天学习计划 · 摘要

> Day 17 个人知识库样例。可自行增删改，再问 Bot。

## 基本信息

- 计划名称：AI Agent 工程师 90 天学习
- 开始日期：2026-07-01
- 技术栈：Python + LangChain / LangGraph
- 大模型 API：DeepSeek
- 城市方向：广州（可投深圳 remote / hybrid）

## 阶段划分

| Phase | 天数 | 主题 |
|-------|------|------|
| 0 | D1–7 | 环境与 Python 基础 |
| 1 | D8–17 | LLM + Prompt + API |
| 2 | D18–27 | Agent 概念 + ReAct |
| 3 | D28–47 | LangChain / RAG / Tools |
| 4 | D48–57 | LangGraph + 多 Agent |
| 5 | D58–67 | 优化 + 部署 + MCP |
| 6 | D68–82 | 综合项目实战 |
| 7 | D83–90 | 简历 + 面试 |

## Phase 1 重点（D8–17）

- Prompt 实验（system / user、CoT、格式约束）
- Function Calling（模型点菜，程序执行）
- RAG 概念预习（Embedding、向量、相似度）
- 小项目：个人知识库问答 Bot（API 版，无向量库）= 今天这个

## 关键路径（不可跳过）

1. D7 首次 LLM API 调用
2. D15 Function Calling 实战
3. D22 手写 ReAct Agent
4. D32 完整 RAG 管道
5. D50 LangGraph ReAct
6. D60 FastAPI 封装
7. D68–82 毕业项目

## 拼 Prompt vs RAG（Day17 笔记用）

- 拼 Prompt：整份文档塞进 messages，实现简单，适合短文档
- RAG：先检索相关片段再塞进 Prompt，适合长文档 / 私有知识库
