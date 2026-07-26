# Day 25 · Agent 调试

## 这题要你做什么？（一句话）

> 给 ReAct 加上**清晰的分步日志**，用 **10 道题**测工具是否选对，目标 **准确率 > 80%**；不对就查日志、改 System Prompt。

今天 2h：以「跑评测 + 看日志 + 必要时改 Prompt」为主。

---

## 调试三问（先记住）

| 现象 | 先看日志哪一行 | 常见原因 |
|------|----------------|----------|
| 该调工具却没调 | 有没有 `Action:`？直接 Final 了？ | Prompt 没强调「必须调」；问法太模糊 |
| 调错工具 | `Action:` 是 weather 还是 calculator？ | 两个工具 description/规则边界不清 |
| 参数错 | `Action: get_weather[...]` 里城市对不对？ | 例子不够；城市被吃掉/乱填 |

口诀：**先看日志，再猜模型；先改 Prompt，再改代码。**

---

## 文件

| 文件 | 用途 |
|------|------|
| `react_debug_agent.py` | 带结构化日志的 ReAct（基于 D22） |
| `run_eval.py` | 跑 10 题，统计工具选择准确率 |
| `test_cases.py` | 10 道评测题 + 期望工具 |

```powershell
cd E:\AI_agent_Quick

# 交互调试（单题细看日志）
.\venv\Scripts\python.exe exercises\day25\react_debug_agent.py

# 验收：10 题批量评测
.\venv\Scripts\python.exe exercises\day25\run_eval.py
```

---

## 建议 2h 节奏

| 时段 | 内容 |
|------|------|
| **0:00–0:25** | 读本 README；跑 1～2 道交互，认清 `[LOG]` 字段 |
| **0:25–1:20** | 跑 `run_eval.py`；准确率 < 80% 则对照失败题改 `REACT_SYSTEM` |
| **1:20–1:45** | 口述：工具未调用 / 参数错误分别怎么查 |
| **1:45–2:00** | 力扣 1 道（短题）或「今日完成」 |

---

## 验收标准

1. 日志每步能看到：**Thought / Action / Observation**（或 Final Answer）  
2. `run_eval.py` 报告准确率 **> 80%**（10 题里 ≥ 9 题；≥ 8 题也算过线，争取 9+）  
3. 能说清：失败时优先看什么、Prompt 改了哪句  

---

## 和前后天的关系

| 天 | 关系 |
|----|------|
| D22–23 | 已有 Agent；今天加「可观测 + 可评测」 |
| D26 | 上 LangChain；调试思路通用 |
| 面试 | 「Agent 不调工具你怎么查？」→ 日志 + 用例集 |
