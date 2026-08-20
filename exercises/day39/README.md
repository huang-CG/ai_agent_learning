# Day 39 · LangSmith 调试

## 这题要你做什么？（一句话）

> 给已有的 `create_agent` **接上 LangSmith tracing**，在网页里看见完整一步步调用，并对照一次**失败调用**写出原因。

```
D25：终端 print 日志（本机看得见）
D39：同一类信息上报到 LangSmith（网页里看得见、可点开）
```

路径请用全路径：

- 今日说明：`exercises/day39/README.md`
- 代码骨架：`exercises/day39/tracing_lab.py`

---

## 和前后天的关系

| 天 | 停在哪 |
|----|--------|
| D25 | 手写 ReAct + `[LOG]` 结构化日志 |
| D29–D38 | `create_agent` 已会跑，但调试主要靠 `print(messages)` |
| **D39** | **云端 Trace**：LLM / tool / 报错 分层可点 |
| D40 | MCP（另一条线，不挡今天） |

口诀：**先看 Trace，再猜模型；先改 Prompt/工具，再改框架代码。**

---

## 验收

1. 已注册 [LangSmith](https://smith.langchain.com)，`.env` 里有 `LANGSMITH_TRACING=true` 和 `LANGSMITH_API_KEY`（**不要把 Key 贴到聊天/Git**）
2. `tracing_lab.py` 可运行；启动时能打印 tracing 是否开启（只打「有/无」，不要打印完整 Key）
3. 至少 **2 个** `@tool`（一个会成功，一个能故意失败）
4. **成功问** 在 LangSmith 里能点开完整 trace：用户句 → 模型 → 工具 → 最终答
5. **失败问**（除数为 0）在 Trace 里能看到工具报错；你能口述失败发生在哪一层
6. 笔记里写清：**这一次失败的原因**（不是空话「模型不行」）

时间不够：砍「给 trace 加 tags」；**不砍**「网页能看到完整 trace + 分析 1 次失败」。

---

## 注册与环境（先做这件事）

1. 打开 [smith.langchain.com](https://smith.langchain.com) 注册（GitHub / Google / 邮箱均可）  
   - 广州访问若打不开：先告诉我，不要空转等；可能需要能访问外网  
2. 设置里创建 **API Key**（常见前缀 `lsv2_`）  
3. 复制到项目根目录 `.env`（对照 `.env.example`），例如：

```
LANGSMITH_TRACING=true
LANGSMITH_API_KEY=lsv2_你的key
LANGSMITH_PROJECT=ai-agent-quick-d39
```

旧文档里的 `LANGCHAIN_TRACING_V2` / `LANGCHAIN_API_KEY` 是旧名字；**今天用 `LANGSMITH_*`**。

缺包时：

```powershell
.\venv\Scripts\python.exe -m pip install langsmith
```

跑法：

```powershell
.\venv\Scripts\python.exe exercises\day39\tracing_lab.py
```

网页：LangSmith → 选项目 `ai-agent-quick-d39`（或你设的名字）→ **Traces**。跑完脚本后刷新。

---

## Trace 里你该认出什么

一次 Agent 调用 ≈ **一条 Trace**（最外层），里面套若干 **Run**：

| 你在网页里看到的 | 对应课堂上的 |
|------------------|--------------|
| 最外层 Agent / graph | 整轮 `invoke` |
| `ChatOpenAI` / model | 模型推理（Thought + 是否调工具） |
| tool 名字（如 `divide_numbers`） | Action + Observation |
| 红色 / Error | 工具抛错或模型调用失败 |

失败可能在四层，不要混为一谈：

1. **没调工具**（该算的却直接口算）  
2. **调错工具**（时间题去调除法）  
3. **参数错**（`b` 填成别的数）  
4. **工具自己报错**（今天的 0 作除数）

---

## 今日时间盒（约 3h）

| 段 | 时长 | 内容 |
|----|------|------|
| A | ~20min | 口述：D25 vs D39；Trace 四层失败 |
| B | ~40min | 注册 + `.env` + 打印 tracing 状态 |
| C | ~80min | 填骨架：双工具 Agent；成功问 + 失败问；网页对照 |
| D | ~25min | 力扣 + 收工 |

实践日：先自己填骨架；卡住约 15～20 分钟再要最小提示。
