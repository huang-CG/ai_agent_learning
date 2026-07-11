# Day 11 · API 深入 + 流式输出

## 这题要你做什么？（一句话）

> 理解 Chat Completions 常用参数，把 D7 `chat.py` 改成 **流式打印**（字一个个蹦出来）。

D8 学过 `temperature`；今天补 **top_p / max_tokens / stop**，并实现 **streaming**。

---

## 四个参数（必记）

| 参数 | 作用 | 典型值 |
|------|------|--------|
| **temperature** | 随机性；低=稳，高=发散 | 0～0.7（任务用 0.3）；创意写作用 0.8+ |
| **top_p** | 核采样；只从累计概率前 p 的 token 里选 | 0.9～1.0；与 temperature **二选一调**即可 |
| **max_tokens** | 限制**生成**的最大 token 数（不含输入） | 512、1024；防回答过长/费钱 |
| **stop** | 遇到这些字符串就**停止生成** | `["\n\n", "用户："]` 或 `None` |

**工程习惯**：格式/推理靠 Prompt；参数做「长度、停止、采样」微调。

---

## 流式 vs 非流式

| | 非流式（D7） | 流式（D11） |
|---|---|---|
| body | 默认 `stream: false` | `"stream": true` |
| 请求 | `requests.post(...)` | `requests.post(..., stream=True)` |
| 响应 | 一次拿完整 JSON | SSE 一行行 `data: {...}` |
| 体验 | 等很久，突然整段出现 | **边生成边打印**，像 ChatGPT 打字 |

---

## 文件

| 文件 | 用途 |
|------|------|
| `stream_chat.py` | 流式 CLI 问答 |

---

## 建议学习顺序

1. 读 `stream_chat.py`，对照 D7 `chat.py` 看改了什么
2. 运行 `python exercises/day11/stream_chat.py`，观察打字效果
3. 试改 `max_tokens=50`，看回答是否被截断
4. 试加 `stop=["。"]`，看是否在第一个句号停（实验用）
5. 笔记里写一句：流式对用户体验为什么重要？

---

## 运行

```powershell
cd e:\AI_agent_Quick
.\venv\Scripts\Activate.ps1
python exercises/day11/stream_chat.py
```

---

## 验收自检

- [ ] 能口述四个参数各管什么
- [ ] 流式 CLI 能边生成边打印
- [ ] 知道 `stream=True` 时解析的是 SSE，不是完整 JSON
- [ ] 对比过流式 vs 非流式的等待感受

---

## 拓展（有余力）

- `timeout=30` + `try/except` 重试 1 次（D8 已学异常处理）
- 对比 `temperature=0` vs `0.7` 流式输出的差异
