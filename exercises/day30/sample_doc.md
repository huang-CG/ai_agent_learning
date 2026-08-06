# Day 30 样例文档 · RAG 切块用

> 本文件供 D30 加载与分割实验。故意写得稍长，方便观察 chunk_size / overlap 效果。

## 什么是 RAG

RAG（Retrieval-Augmented Generation，检索增强生成）的核心思路是：
不要把整本知识库一次性塞进 Prompt，而是先按问题去检索最相关的若干片段，
再把这些片段作为上下文交给大模型生成答案。这样可以降低幻觉，也更能撑住长文档。

RAG 常见流水线：

1. Load：加载本地 Markdown / PDF 等文档
2. Split：把长文切成 chunks（块）
3. Embed：把每个 chunk 变成向量
4. Store：写入向量库
5. Retrieve：按问题相似度取出 top-k 片段
6. Generate：把片段 + 问题交给 LLM 生成回答

今天 D30 只做前两步：Load + Split。Embedding 与向量库留给 D31，完整管道在 D32（关键路径）。

## 为什么要切块

大模型有上下文窗口上限。一份很长的手册如果整份塞进去：

- Token 很容易超限或很贵
- 模型注意力被大量无关段落稀释，答偏
- 后续检索也无法精确定位「哪一段」相关

切块后，检索只返回少数相关 chunk，生成时更聚焦。

## chunk_size 与 chunk_overlap

- chunk_size：每块大约多少字符（具体单位取决于 splitter 实现）
- chunk_overlap：相邻两块重叠多少，避免一句话被从中间切断后语义丢失

经验上：过小会碎、丢上下文；过大又接近「整段塞」。需要按文档类型试验。

## 与拼 Prompt 的对比（复习 D17）

| 方式 | 做法 | 适合 |
|------|------|------|
| 拼 Prompt | 整份文档进 messages | 短文档、原型快 |
| RAG | 检索片段再生成 | 长文档、私有知识库 |

## 本仓库学习节奏摘要

- Phase 0：Python 与环境
- Phase 1：Prompt / Function Calling / RAG 概念
- Phase 2：手写 ReAct + LangChain 重写
- Phase 3：Tools / Agent / RAG 工程化（当前）
- 之后：LangGraph、部署、毕业项目

## 小测验段落（方便看切块边界）

苹果派的做法：先准备面粉、黄油和冰水做酥皮，再把苹果片与糖、肉桂拌匀。烤箱预热到 190 摄氏度，烤约 45 分钟直到金黄冒泡。出炉后静置 10 分钟再切，否则馅料容易塌。

番茄炒蛋：蛋液加少许盐打散，热锅凉油滑蛋盛出；再下番茄翻炒出汁，回锅鸡蛋轻轻翻匀，出锅前可加葱花。火候关键是番茄出汁后再合蛋，否则会水汪汪。
