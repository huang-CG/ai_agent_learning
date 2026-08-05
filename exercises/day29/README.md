# Day 29 · LangChain Agent（组装闭环）

## 这题要你做什么？（一句话）

> 把 D28 的 Tools **接进** `create_agent`，跑通「选工具 → 执行 → Observation → 最终回答」，并加上基础错误处理。

---

## 和 D27 / D28 的关系

| 天 | 停在哪 |
|----|--------|
| D27 | 天气 Agent 已跑通过（里程碑），但当时重点是「能用」 |
| D28 | `bind_tools` 只看到 **tool_calls 提议**，不执行工具 |
| **D29** | 用 D28 同类工具，把 **闭环** 写清楚：执行 + 回灌 + 最终答；并练错误处理 |

计划里写的 `create_react_agent` / `AgentExecutor` 是旧 API；你环境里用的是 **`create_agent`**（D27 已用），今天继续这条线。

---

## 验收

1. `agent_lab.py` 可运行  
2. 至少 **2 个** `@tool`（可复用 D28 思路，允许精简重写）  
3. `create_agent(model + tools + system_prompt)` 组装成功  
4. 问「现在几点了？」能调工具并给出含真实时间的回答（不是只打印 tool_calls）  
5. 再问一句会触发**另一个**工具的问题（如温度换算 / 字数统计）也能答对  
6. `ask` 外层有 `try/except`：工具失败或 API 异常时不崩掉，打印可读错误  
7. 能口述：今天的链路比 D28 多了哪几步  

拓展（时间够）：用 `stream_mode="updates"` 打印中间节点，对照 D22 的 Thought/Action/Observation。

---

## 运行

```powershell
cd E:\AI_agent_Quick
.\venv\Scripts\activate
.\venv\Scripts\python.exe exercises\day29\agent_lab.py
```

---

## 今日时间盒（约 3h）

| 段 | 时长 | 内容 |
|----|------|------|
| A | ~20min | 口述：D28 vs D29 差在哪；system_prompt 与工具要对齐 |
| B | ~90min | 写工具 + `build_agent` + `ask`（invoke，打印 messages 轨迹） |
| C | ~30min | 错误处理 + 双工具验收 |
| D | ~25min | 力扣 1 题 + 收工 |
| 拓展 | 剩余 | stream updates |
