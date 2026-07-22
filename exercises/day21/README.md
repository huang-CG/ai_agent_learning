# Day 21 · 手写 ReAct Agent（一）

## 这题要你做什么？（一句话）

> 把 D19 纸笔的 **Thought → Action → Observation** 写成**能跑的 Python 循环**：调 LLM → 解析输出 → **模拟**工具结果 → 再喂回去，直到 `Final Answer`。

验收：循环能跑 **≥3 轮**（或模型提前 Final Answer），有 `max_steps` 上限。

**今天不接真 API / 真工具**（D22 再接天气）。

---

## 先抓住这一句

```text
用户问题
  → LLM 输出 Thought + Action（或 Final Answer）
  → 若是 Action：程序 simulate_tool → 得到 Observation
  → 把 Observation 拼回上下文 → 再请求 LLM
  → 重复，直到 Final Answer 或 max_steps
```

| D19 纸笔 | D21 代码 |
|----------|----------|
| 你手写 Observation | `simulate_tool()` 返回假数据 |
| Action: `get_weather[广州]` | `parse_action()` 用正则拆工具名+参数 |
| 循环在纸上 | `for step in range(max_steps)` |

---

## 文件

| 文件 | 用途 |
|------|------|
| `react_agent.py` | 主循环 + 解析 + 模拟工具 |

运行（外部 PowerShell）：

```powershell
cd E:\AI_agent_Quick
.\venv\Scripts\python.exe exercises\day21\react_agent.py
```

试：`广州现在气温多少？` / `帮我算 (3+5)*2`

---

## 核心函数（今天要读懂）

| 函数 | 干什么 |
|------|--------|
| `parse_react(text)` | 从 LLM 文本里拆 `thought` / `action` / `final_answer` |
| `parse_action(action)` | `get_weather[广州]` → `("get_weather", "广州")` |
| `simulate_tool(name, arg)` | 假工具，返回 Observation 字符串 |
| `run_react(question)` | 主循环：`max_steps` + scratchpad 累加 |

---

## 建议 2h 节奏（你今天 2h）

| 时段 | 内容 |
|------|------|
| **0:00–0:25** | 读 README + 跑 `react_agent.py` 两次 |
| **0:25–1:10** | 逐函数读代码；口述「一轮循环发生了什么」 |
| **1:10–1:40** | 改一处：例如给 `simulate_tool` 加一条假数据，或调 `max_steps=3` 看停止 |
| **1:40–2:00** | 验收口述 + 「今日完成」 |

力扣今天**可选**（时间紧可跳过，D22 补）。

---

## 验收标准

1. 能口述：scratchpad 是什么、Observation 谁产生  
2. 终端跑通，能看到多轮 Thought/Action/Observation 日志  
3. 能说清 `max_steps` 干什么  
4. 知道 D22 要换什么：`simulate_tool` → 真函数

---

## 拓展（有余力）

- 对比：正则解析 vs 让模型输出 JSON（D21 计划里的拓展）  
- `parse_action` 若模型写成 `Action: get_weather(广州)` 怎么兼容？
