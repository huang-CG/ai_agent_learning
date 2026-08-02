# Day 28 · LangChain Tools（Phase 3 开篇）

## 这题要你做什么？（一句话）

> 用 `@tool` 自建 **3 个**自定义工具，打印它们的 Schema，并验证「直接调用」与「模型绑定后能选对工具」。

---

## 和 D27 的关系

| D27 | D28 |
|-----|-----|
| 为了跑通 Agent，顺便写了 `@tool` | **专门练 Tool**：Schema、docstring、绑定 |
| 天气 + 计算器（可复用思路） | **新建 3 个工具**（不要照搬 D27 那套名字） |
| `create_agent` 整条链路 | 今天可只做到 `bind_tools` + 看 `tool_calls`；完整 Agent 留给 D29 |

对应旧知识：D20 的 `name` / `description` / `parameters` —— `@tool` 就是从函数签名 + docstring 自动生成这三字段。

---

## 验收

1. `tools_lab.py` 可运行  
2. 有 **3 个** `@tool` 函数，docstring 写清「何时用 / 参数含义 / 不要用于」  
3. 打印每个工具的 `name`、`description`、`args`（或等价 Schema 字段）  
4. 能 **直接** `tool.invoke(...)` 跑通至少 1 个工具  
5. 用 `llm.bind_tools(tools)` 问一句，模型能选出正确工具（打印 `tool_calls` 即可，**不必**今天就接完整 Agent 循环）

拓展（时间够再做）：用 `StructuredTool.from_function` 再做一个工具，对比与 `@tool` 的写法差异。

---

## 建议的 3 个工具（可自定，但需互不重叠）

1. **时间类**：如 `get_current_time`（返回本地当前时间字符串）  
2. **文本类**：如 `count_words`（统计中英文字数/词数）  
3. **换算类**：如 `celsius_to_fahrenheit`（摄氏 → 华氏）

要求：三个工具的能力边界写清楚，避免模型乱选。

---

## 运行

```powershell
cd E:\AI_agent_Quick
.\venv\Scripts\activate
.\venv\Scripts\python.exe exercises\day28\tools_lab.py
```

---

## 今日时间盒（约 3h）

| 段 | 时长 | 内容 |
|----|------|------|
| A | ~25min | 概念：`@tool` ↔ Schema 三字段；看一眼 Tool 对象有哪些属性 |
| B | ~90min | 自己写 3 个工具 + 打印 Schema + `invoke` 直调 |
| C | ~35min | `bind_tools` 验收：模型选对工具 |
| D | ~25min | 力扣 1 题 + 收工笔记 |
| 拓展 | 剩余 | StructuredTool |
