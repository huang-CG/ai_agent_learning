# Day 14 · Function Calling 原理

## 这题要你做什么？（一句话）

> 搞懂：**模型自己不能查天气/算数/读数据库**；它只能**提出要调哪个函数、传什么参数**；**你的代码执行后把结果塞回 messages**，模型再据此回答用户。

D15 才动手写「时间 + 计算器」实战。今天只学**概念 + JSON Schema + 流程图**。

文档：[DeepSeek Tool Calls](https://api-docs.deepseek.com/guides/tool_calls)

---

## 核心一句话

| 谁 | 干什么 |
|----|--------|
| **LLM** | 看 `tools` 列表 → 决定是否调用 → 输出 `tool_calls`（函数名 + JSON 参数） |
| **你的程序** | 真正 `def get_weather(...)` 执行，得到结果 |
| **再请求一次 API** | 把结果以 `role: "tool"` 放进 messages → LLM 用自然语言回答用户 |

**模型不会执行函数**；Function Calling = **结构化「我想调用某某函数」的约定**。

---

## 五步流程（必须能默画）

```
① 用户提问
    ↓
② 你发请求：messages + tools（函数说明书列表）
    ↓
③ LLM 二选一：
   · 直接回答（finish_reason: stop）
   · 或返回 tool_calls（finish_reason: tool_calls）
    ↓
④ 你的代码：解析 arguments → 执行 Python 函数 → 得到结果
    ↓
⑤ 把 assistant 的 tool_calls 消息 + role:tool 结果 再发给 LLM
    → LLM 结合结果，用自然语言回用户
```

详细 Mermaid：见 `notes/diagrams/day14-function-calling-flow.md`（你可先手绘，再对照）。

---

## JSON Schema 是什么？

给模型看的「函数参数说明书」，告诉它：参数名、类型、是否必填、含义。

```json
{
  "type": "function",
  "function": {
    "name": "get_weather",
    "description": "查询某城市当前天气。用户问天气时使用。",
    "parameters": {
      "type": "object",
      "properties": {
        "city": {
          "type": "string",
          "description": "城市名，如 广州"
        }
      },
      "required": ["city"]
    }
  }
}
```

| 字段 | 作用 |
|------|------|
| `name` | 函数名（模型返回时带这个名字） |
| `description` | **最重要**：模型靠它决定「要不要调、何时调」 |
| `parameters` | JSON Schema：参数长什么样 |
| `required` | 必填参数列表 |

模型选工具靠：**用户问题 + 各函数 description**，不是靠猜函数体代码。

---

## messages 里多出来的两种角色

D12 只有 `system` / `user` / `assistant`。Function Calling 再加：

| role | 谁发 | 内容 |
|------|------|------|
| `assistant`（含 `tool_calls`） | 模型 | 「我要调 get_weather，参数 {city:广州}」 |
| `tool` | 你的程序 | 函数真实返回值，如 `"晴，28℃"` |

顺序必须对：先有带 `tool_calls` 的 assistant，再有对应 `tool` 结果，再请求第三轮让模型说话。

---

## 文件

| 文件 | 用途 |
|------|------|
| `tools_schema_demo.py` | 打印示例 tools / 模拟一轮 tool_calls 消息长什么样（**不调真实工具 API**） |
| `notes/diagrams/day14-function-calling-flow.md` | 流程图（对照用） |

---

## 建议学习顺序

1. 读上面「五步流程」+ Schema 示例，用自己的话复述一遍
2. 运行 `python exercises/day14/tools_schema_demo.py`，看打印出来的 JSON
3. **手绘**流程图：用户 → LLM → 工具 → LLM → 用户（纸上或笔记）
4. 对照 `notes/diagrams/day14-function-calling-flow.md`
5. 笔记写 3 句：**模型做什么 / 程序做什么 / 为什么要 JSON Schema**

---

## 运行

```powershell
cd e:\AI_agent_Quick
.\venv\Scripts\Activate.ps1
python exercises/day14/tools_schema_demo.py
```

---

## 验收自检

- [ ] 能口述：模型**不执行**函数，只输出调用意图
- [ ] 能画出五步流程（或文字版等价）
- [ ] 能解释 `name` / `description` / `parameters` 各自干什么
- [ ] 知道 `role: tool` 是谁写的
- [ ] 力扣 1 道（今日结束后）

**Tomorrow D15**：真正调 DeepSeek，接「当前时间」+「计算器」。
