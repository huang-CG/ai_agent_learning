# Day 22 · 手写 ReAct Agent（二）· 真天气

## 这题要你做什么？（一句话）

> 把 D21 的 `simulate_tool` 换成**真实工具**：天气用 wttr.in（同 D4），计算器真算；Observation 来自程序执行结果；保留 `max_steps`。

验收：问 **「北京天气」** 能调 `get_weather`、拿到真实 Observation、给出 Final Answer。

---

## D21 → D22 改了什么

| D21 | D22 |
|-----|-----|
| `simulate_tool` + 假字典 | `run_tool` → 真 `get_weather` / `calculator` |
| Observation 是编的 | Observation = HTTP / 计算的真实结果 |
| `[模拟]` 日志 | `[工具]` 日志 |
| max_steps 已有 | **继续保留**（真工具更要防死循环） |

循环骨架不变：Thought → Action → Observation → scratchpad → … → Final Answer。

---

## 文件

| 文件 | 用途 |
|------|------|
| `react_weather_agent.py` | 真天气 ReAct Agent |

```powershell
cd E:\AI_agent_Quick
.\venv\Scripts\python.exe exercises\day22\react_weather_agent.py
```

必测：`北京天气` / `广州现在气温多少？`  
可选：`帮我算 (3+5)*2`

---

## 建议 2.5h 节奏

| 时段 | 内容 |
|------|------|
| **0:00–0:20** | 对照 D21，读 `run_tool` / `get_weather` |
| **0:20–1:20** | 跑通「北京天气」验收 |
| **1:20–1:50** | 口述：真 Observation 从哪来；对比 D21 |
| **1:50–2:20** | 力扣 1 道（推荐 383 赎金信，Counter） |
| **2:20–2:30** | 「今日完成」 |

---

## 验收标准

1. 问「北京天气」→ 日志出现 `Action: get_weather[北京]` + 真实 Observation  
2. 最终有自然语言 Final Answer（含气温/天气概况）  
3. 能说清：`max_steps` 为何仍要保留  
4. 力扣 1 道（可选但建议做）

---

## 关键路径

今天是路线里的 **D22 手写 ReAct Agent**——接真工具后，你就有了「能查天气的 Agent」。
