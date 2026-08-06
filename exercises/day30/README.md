# Day 30 · 文档加载与分割（RAG 前置）

## 这题要你做什么？（一句话）

> 加载本地 Markdown，用 Text Splitter 切成 chunks，打印块数与每块长度统计。

---

## 在 RAG 流水线里的位置

```
Load → Split → Embed → Store → Retrieve → Generate
 ▲       ▲
 今天只做这两步（D31 起才接向量库）
```

对应 D16/D17 概念：拼 Prompt 塞整篇；RAG 要先能切出可检索的块。

---

## 验收

1. 已安装 `langchain-text-splitters`  
2. `split_lab.py` 可运行  
3. 成功加载 `sample_doc.md`（或你指定的 md）  
4. 用 `RecursiveCharacterTextSplitter` 切块  
5. 打印：总块数、每块字符数、前 2～3 块预览（截断即可）  
6. （建议）再跑一组不同的 `chunk_size` / `chunk_overlap`，口述差在哪  

拓展：试 `CharacterTextSplitter`，或加载第二份 md 对比。PDF 今天可不做（依赖更多）。

---

## 环境

```powershell
cd E:\AI_agent_Quick
.\venv\Scripts\activate
pip install langchain-text-splitters
.\venv\Scripts\python.exe exercises\day30\split_lab.py
```

---

## 今日时间盒（约 3h）

| 段 | 时长 | 内容 |
|----|------|------|
| A | ~20min | 口述：为何切块；size / overlap 各自管什么 |
| B | ~20min | `pip install` + 读骨架 |
| C | ~90min | 填 TODO：加载 → 切块 → 打印统计 |
| D | ~25min | 力扣 1 题 + 理论题 + 收工 |
