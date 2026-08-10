# Day 34 · RAG + Agent（检索做成工具）

## 这题要你做什么？（一句话）

> 把知识库检索做成 `@tool`，用 `create_agent` 让模型 **自己决定**：何时查库、何时直接答。

```
D32/D33：你写死「先检索再生成」
D34：Agent 按需调用 search_knowledge 工具
```

路径请用全路径，避免点到仓库根目录 `README.md`：

- 今日说明：`exercises/day34/README.md`
- 代码骨架：`exercises/day34/rag_agent_lab.py`

---

## 和前后天的关系

| 天 | 停在哪 |
|----|--------|
| D29 | `create_agent` + 普通工具闭环 |
| D32–33 | RAG 管道 + 引用/过滤 |
| **D34** | RAG **变成工具**；Agent 选不选它 |
| D35 | 再加联网搜索工具 |

拓展（口头即可）：Self-RAG ≈ 模型自己判断「要不要检索 / 检索结果够不够」。

---

## 验收

1. 有工具 `search_knowledge(query: str) -> str`（内部：向量检索 top-k，返回拼接片段）  
2. `create_agent` 组装成功（至少再带 1 个非 RAG 工具，如当前时间）  
3. 问知识库内问题（吉祥物）→ messages 里出现 **tool** 调用，答案正确  
4. 问与库无关的常识/闲聊（如「1+1 等于几」或「用一句话打个招呼」）→ **不必**调知识库也能答  
5. 能口述：和 D32「每次必检索」差在哪  

时间不够：砍 Self-RAG 拓展阅读，**不砍**「按需调用」。

---

## 环境

```powershell
.\venv\Scripts\python.exe exercises\day34\rag_agent_lab.py
```

复用：`exercises/day32/sample_kb.pdf` + 硅基 Embedding + DeepSeek。

---

## 今日时间盒（约 3h）

| 段 | 时长 | 内容 |
|----|------|------|
| A | ~15min | 口述：按需检索 vs 每次必检索 |
| B | ~100min | 写工具 + create_agent + 两问验收 |
| C | ~20min | 看 messages 轨迹（tool / 最终答） |
| D | ~25min | 力扣 + 收工 |

实践日：先自己填；卡住 15～20 分钟再要最小提示。

> 提醒：今天学完后，本周学习日将满 **7/7**，下次开课优先进入 **周复盘**（暂停新课）。
