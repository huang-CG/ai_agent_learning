# Day 38 · Prompt 工程进阶

## 这题要你做什么？（一句话）

> 给 Agent 写一版 **带 Few-shot + JSON 格式** 的 system prompt，让同一类问题输出能稳定被 `json.loads`。

```
D13：三版 system prompt 对比（角色/边界/格式）
D38：把这件事用在 Agent 上 + 加 Few-shot + 强制 JSON
```

路径请用全路径：

- 今日说明：`exercises/day38/README.md`
- 代码骨架：`exercises/day38/prompt_agent_lab.py`

---

## 和前后天的关系

| 天 | 停在哪 |
|----|--------|
| D9–D13 | Prompt / 格式约束 / 四原则 |
| D29–D37 | 工具 + `create_agent` |
| **D38** | **Agent 的说明书**（system prompt）写稳 |
| D39 | LangSmith 看每步 |

不必新装包。DeepSeek 照旧。今天可以不挂工具（只练输出格式）；要挂也只许挂辅助、别抢戏。

---

## 验收

1. 写两版 `system_prompt`：弱版（只说「用 JSON」）vs 强版（角色 + 边界 + **JSON 字段说明** + **至少 2 条 Few-shot**）  
2. 同一组（≥2 句）分类题，两版都跑  
3. 强版输出能被 `json.loads` 解析，且含约定字段（如 `label` / `reason`）  
4. 能口述：Few-shot 是什么；为什么 JSON 任务宜低 temperature  

时间不够：砍弱版对比；**不砍** 强版 + `json.loads` 验收。

约定分类标签（强版必须只输出这些）：`闲聊` / `投诉` / `咨询`（三选一即可）。

---

## 环境

```powershell
.\venv\Scripts\python.exe exercises\day38\prompt_agent_lab.py
```

JSON 小抄：模型常会包 \`\`\`json ... \`\`\`，解析前可先去掉围栏，再 `json.loads`。

---

## 今日时间盒（约 3h）

| 段 | 时长 | 内容 |
|----|------|------|
| A | ~15min | 口述：四原则落到 Agent；Few-shot；温度 |
| B | ~90min | 写两版 prompt + 跑题 + 解析 JSON |
| C | ~20min | 对比弱版 vs 强版（哪边更稳） |
| D | ~25min | 力扣 + 收工 |

实践日：先自己填骨架；卡住约 15～20 分钟再要最小提示。
