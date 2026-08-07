# Day 31 · Embedding 与向量库

## 这题要你做什么？（一句话）

> 把 D30 切好的 chunks **向量化并写入 Chroma**，再用问题检索 **top-3** 相关片段。

---

## 在 RAG 流水线里的位置

```
Load → Split → Embed → Store → Retrieve → Generate
              ▲       ▲         ▲
              今天做这三步（还不接 LLM 生成；生成是 D32）
```

提醒：DeepSeek **没有** Embedding API（D16 已踩过）。今天用 **硅基流动** 的 `BAAI/bge-m3`（OpenAI 兼容接口）。

---

## 验收

1. `.env` 配好 `SILICONFLOW_API_KEY`  
2. `vector_lab.py` 可运行  
3. 成功：加载 → 切块 → Embed → 写入向量库 → `similarity_search(k=3)`  
4. 打印 top-3 的内容预览  
5. 能口述：Embedding / 向量库 / top-k 各干什么  

> **环境说明（2026-08-07）**：本机 Python 3.14 下 `chromadb` / `langchain-chroma` 写入时可能崩溃（Windows 访问冲突）。  
> **改用** `langchain_core.vectorstores.InMemoryVectorStore`（概念相同：向量化 + 相似度检索；不落盘）。Chroma 以后换稳定环境再试即可。  

---

## 环境

### 1) 依赖

已有 `langchain-openai` / `langchain-text-splitters` 即可；**不必再装 chromadb**（见上方环境说明）。

### 2) `.env` 增加（没有就去 [硅基流动](https://siliconflow.cn) 开免费 Key）

```env
SILICONFLOW_API_KEY=你的key
SILICONFLOW_BASE_URL=https://api.siliconflow.cn/v1
SILICONFLOW_EMBEDDING_MODEL=BAAI/bge-m3
```

DeepSeek 的 Key **不能**用来做 Embedding。

### 3) 运行

```powershell
.\venv\Scripts\python.exe exercises\day31\vector_lab.py
```

---

## 今日时间盒（约 3h）

| 段 | 时长 | 内容 |
|----|------|------|
| A | ~20min | 口述：Embedding / 向量库 / top-k；为何不用 DeepSeek |
| B | ~25min | pip + 配 Key |
| C | ~90min | 填 TODO：切块 → Embed → Chroma → 检索 |
| D | ~25min | 力扣 + 理论题 + 收工 |
