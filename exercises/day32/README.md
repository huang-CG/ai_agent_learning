# Day 32 · 完整 RAG 管道（关键路径）

## 这题要你做什么？（一句话）

> 打通 **Load → Split → Embed → Store → Retrieve → Generate**，对 **PDF** 做准确问答。

```
Load → Split → Embed → Store → Retrieve → Generate
  ▲      ▲       ▲       ▲        ▲          ▲
 D30    D30     D31     D31      D31        ★今天
```

---

## 与 D17 的差别（必懂）

| | D17 拼 Prompt | D32 RAG |
|--|---------------|---------|
| 上下文 | 整份文档塞进 messages | 只塞检索到的 top-k 片段 |
| 适合 | 短文档 | 长文档 / 可扩展知识库 |
| 今天文件 | `sample_kb.pdf` | 用向量检索再生成 |

---

## 验收（关键路径 · 先保这些）

1. `rag_lab.py` 能跑通完整六步  
2. 问「吉祥物叫什么」→ 答出 **小向量**（及「只吃向量」）  
3. 问「毕业项目代号」→ 答出 **青云助手** + RAG/Agent 要求  
4. 问文档没有的信息（如月费）→ **明确说没有**，不编造  
5. 至少对比 **两种 chunk_size**（如 200 vs 80），口述差异  
6. 能口述：六步各自干什么；Generate 吃的是「检索片段」，不是整本 PDF  

时间不够：砍第二种 chunk 的多题，**不砍** Generate；至少一种参数下 q1+q3 过关。

---

## 环境

```powershell
.\venv\Scripts\pip.exe install pypdf
# Embedding：SILICONFLOW_*（同 D31）
# 生成：DEEPSEEK_API_KEY（同 D26）
.\venv\Scripts\python.exe exercises\day32\rag_lab.py
```

样例 PDF：`exercises/day32/sample_kb.pdf`（虚构「广州 AI Agent 学习站」，方便验幻觉）。  
若 PDF 损坏，可跑：`python exercises/day32/_make_sample_pdf.py` 重新生成。

> 向量库继续用 **InMemoryVectorStore**（D31 已避开 Chroma 崩溃）。

---

## 今日时间盒（约 3h）

| 段 | 时长 | 内容 |
|----|------|------|
| A | ~15min | 口述六步；对照 D17 |
| B | ~90min | 填 TODO：PDF→检索→Generate |
| C | ~25min | chunk_size 对比 + 无答案题 |
| D | ~30min | 力扣 1 道 + 收工 |

实践日规则：先自己填；卡住 15～20 分钟再要最小提示。
