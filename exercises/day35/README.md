# Day 35 · 搜索工具集成（web_search）

## 这题要你做什么？（一句话）

> 把 **联网搜索** 做成 `@tool`，用 `create_agent` 回答「需要实时信息」的问题。

```
D32–34：本地知识库（RAG）
D35：   外网实时信息（web_search）
以后：  两者可同时挂在同一 Agent 上
```

路径请用全路径：

- 今日说明：`exercises/day35/README.md`
- 代码骨架：`exercises/day35/search_agent_lab.py`

---

## 和前后天的关系

| 天 | 停在哪 |
|----|--------|
| D22 | 手写 ReAct 里假的 `web_search` |
| D34 | RAG 检索做成工具（本地库） |
| **D35** | **真搜索**做成工具（外网） |
| D36 | SQL 工具（结构化数据） |

选型（今天默认）：

| 方案 | 要不要 Key | 说明 |
|------|------------|------|
| **ddgs（DuckDuckGo）** | ❌ 推荐今天用 | `pip install ddgs`，自己 `@tool` 包一层 |
| Tavily | ✅ 要注册 | 质量往往更好；时间紧可下周再试 |

不要直接抄 LangChain 现成 `DuckDuckGoSearchRun` 完事——今天重点是 **自己包工具**（和 D28/D34 同一技能）。

---

## 验收

1. 有工具 `web_search(query: str) -> str`（内部调 `ddgs`，返回若干条标题+摘要+链接的拼接文本）  
2. `create_agent` 至少再带 1 个非搜索工具（如 `get_current_time`）  
3. 问「需要联网才知道」的题（如「今天/最近某某新闻或比赛结果」）→ messages 里出现 **tool**，答案基于搜索结果  
4. 问「1+1 等于几」→ **不必**调搜索也能答  
5. 能口述：RAG 工具 vs `web_search` 各解决什么问题  

时间不够：砍 Tavily；**不砍**「真搜索 + 按需调用」。

---

## 环境

先装依赖（venv 内）：

```powershell
.\venv\Scripts\pip.exe install ddgs
```

再跑：

```powershell
.\venv\Scripts\python.exe exercises\day35\search_agent_lab.py
```

复用：DeepSeek（`.env` 里已有即可）。搜索不走 Embedding。

若 `ddgs` 报限流/网络错误：换关键词重试、稍等再跑；仍不行再考虑 Tavily（需 Key）。

---

## 今日时间盒（约 2.5h）

| 段 | 时长 | 内容 |
|----|------|------|
| A | ~10min | 口述：为何要搜索工具；RAG vs 搜索 |
| B | ~15min | 安装 `ddgs` + 裸调用冒烟（不经 Agent） |
| C | ~90min | 写 `@tool` + `create_agent` + 两问验收 |
| D | ~25min | 力扣 + 收工 |

实践日：先自己填骨架；卡住约 15～20 分钟再要最小提示。
