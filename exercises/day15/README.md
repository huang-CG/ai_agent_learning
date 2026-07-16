# Day 15 · Function Calling 实战

## 这题要你做什么？（一句话）

> 用 DeepSeek **真的**走完：问时间 / 算算术 → 模型返回 `tool_calls` → **你的 Python 执行** → `role: tool` 回传 → 模型说人话。

D14 学的是流程图；今天把 `get_current_time` 和 `calculator` 接进真实 API。

---

## 和 D14 / 官方文档的对应

| D14 / 官方 | 今天代码里 |
|------------|------------|
| `send_messages(messages)` | `chat(messages)`（用你熟悉的 `requests`） |
| `tools` 说明书 | `TOOLS`（两个函数） |
| 假结果 `"24℃"` | **真执行** `get_current_time()` / `calculator()` |
| 第二次请求 | 拼好 tool 结果后再 `chat` 一次 |

---

## 文件

| 文件 | 用途 |
|------|------|
| `tool_chat.py` | 完整 CLI：多工具自动选择 |

---

## 建议学习顺序

1. 读 `tool_chat.py`：先找两个真函数 `get_current_time` / `calculator`
2. 再找 `TOOLS`（说明书）和 `run_tool`（按名字调用）
3. 读 `chat_with_tools`：第一轮 → 有无 `tool_calls` → 执行 → 第二轮
4. 运行后依次试：
   - `现在几点了？`
   - `帮我算 (3+5)*2`
   - `你好`（应直接答，不调工具）
5. 笔记写一句：模型选错工具时，多半是 `description` 写得不清

---

## 运行

```powershell
cd e:\AI_agent_Quick
.\venv\Scripts\Activate.ps1
python exercises/day15/tool_chat.py
```

---

## 验收自检

- [ ] 问时间：能调 `get_current_time`，回答里有真实时间
- [ ] 问计算：能调 `calculator`，结果正确
- [ ] 闲聊：不调工具，直接回答
- [ ] 能指出代码里「第一轮 / 执行 / 第二轮」三处
- [ ] 力扣 1 道（今日结束后）

**明日 D16**：RAG 概念预习（Embedding / 向量 / 相似度）
