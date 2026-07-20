# Day 19 · ReAct 架构

## 这题要你做什么？（一句话）

> 搞懂 **ReAct = Reason + Act**：用固定格式循环 **Thought → Action → Observation**，直到给出 Final Answer。今天**纸笔手写 1 个完整例子**（不写真实 Agent 代码；D21–22 再写）。

验收：完整写出至少 1 个含多轮 Thought/Action/Observation 的示例。

---

## 先抓住这一句

昨天的 Agent 四步，用 ReAct 的「台词」写出来就是：

| Agent 四步 | ReAct 台词 |
|------------|------------|
| 推理 | **Thought**（我想…） |
| 决策 + 点工具 | **Action**（我要调某某工具，参数是…） |
| 感知工具结果 | **Observation**（工具返回了…） |
| 循环 / 交卷 | 再 Thought… 或 **Final Answer** |

**ReAct** 论文核心：把「思考」和「行动」交错写出来，而不是闷头只生成最终答案——这样更稳、更好查错。

---

## 标准格式（今天就按这个写）

```text
Question: ……用户问题……

Thought 1: ……我在想什么、缺什么信息……
Action 1: 工具名[参数]
Observation 1: ……工具返回的结果……

Thought 2: ……根据结果继续想……
Action 2: ……
Observation 2: ……

Thought 3: ……已经够了……
Final Answer: ……给用户的最终回答……
```

**规则速记**

- Thought：只写推理，不假装已经拿到工具结果  
- Action：写清调哪个工具、什么参数（像 FC 的 name + arguments）  
- Observation：**假装**工具已经执行完（今天纸笔可自己编合理结果；D22 才接真 API）  
- 信息不够就再来一轮；够了就 Final Answer  

---

## 和 Function Calling 的关系

| | Function Calling（D14–15） | ReAct（今天） |
|--|---------------------------|--------------|
| 形式 | JSON `tool_calls` | 文本 Thought/Action/Observation |
| 谁执行 | 你的 Python | 一样是程序（今天纸笔模拟） |
| 本质 | 都是「想 → 调工具 → 看结果 → 再想」 | 同构，写法不同 |

以后 LangChain/LangGraph 里两种都会见到。

---

## 今日作业：手写 1 个完整例子

任选一题（推荐题 A）：

**题 A（推荐）**  
用户：`广州现在气温多少？出门要不要带伞？`  
可用工具（纸笔假装）：

- `get_weather[city]` → 返回天气摘要（你自己编合理内容，如 `阴，28℃，降水概率 70%`）  
- `calculator[expression]` → 返回计算结果（若需要）

要求：至少 **2 轮** Thought/Action/Observation，最后有 Final Answer。

**题 B**  
用户：`帮我算 (3+5)*2，再用一句话解释结果。`  
工具：`calculator[expression]`

把写好的全文贴给我验收（手机拍照纸笔 或 直接打字）。

---

## 对照图

`notes/diagrams/day19-react-loop.md`（先自己写例子，再对照）。

---

## 建议 3h 节奏

| 时段 | 内容 | 产出 |
|------|------|------|
| 0:00–0:40 | 读 README，搞清三台词 | 能口述 Thought/Action/Observation |
| 0:40–1:40 | 纸笔手写题 A（或 B）完整循环 | 验收用文本 |
| 1:40–2:20 | 笔记：三台词 + 与 FC/Agent 四步对照 | 笔记 |
| 2:20–2:50 | 力扣 1 道 | 贴代码 |
| 2:50–3:00 | 「今日完成」 | 更新文档 |

---

## 验收标准

1. 能口述：ReAct 三步各干什么  
2. 交出 **1 份完整示例**（含 ≥2 轮 T/A/O + Final Answer）  
3. 能说清：ReAct 和 Function Calling 本质一样、格式不同  

---

## 力扣（课后）

推荐：[217. 存在重复元素](https://leetcode.cn/problems/contains-duplicate/) 复习，或  
[349. 两个数组的交集](https://leetcode.cn/problems/intersection-of-two-arrays/)（练 set）。
