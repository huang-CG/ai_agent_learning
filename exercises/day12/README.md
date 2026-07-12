# Day 12 · 多轮对话

## 这题要你做什么？（一句话）

> 让 AI **记得上一轮说了什么**：用 `messages` 列表攒历史，实现带记忆的 CLI 聊天。

D7 每次只发一条 `user`；今天改成**整段对话历史**一起发。

---

## 核心概念

### D7 单轮 vs D12 多轮

```python
# D7 单轮：只有当前问题
messages = [{"role": "user", "content": "你好"}]

# D12 多轮：历史 + 新问题
messages = [
    {"role": "user", "content": "我叫小明"},
    {"role": "assistant", "content": "你好小明！"},
    {"role": "user", "content": "我叫什么？"},   # ← 模型能看到上面历史
]
```

### 每轮流程

```
1. 用户输入 → append {"role":"user", "content": ...}
2. 把 messages 整个发给 API
3. 拿到回答 → append {"role":"assistant", "content": ...}
4. 下一轮重复
```

### 为什么要限制历史长度？

对话越长，`messages` 越大 → **Token 越多** → 越慢、越贵，还可能超出**上下文窗口**（D8 学过）。

做法：只保留最近 N 轮（或最近 N 条），旧的丢掉。

---

## 文件

| 文件 | 用途 |
|------|------|
| `history_chat.py` | 带历史的多轮 CLI |

---

## 建议学习顺序

1. 读 `history_chat.py`，找到 `messages = []` 和两次 `append`
2. 运行后先试：「我叫小明」→「我叫什么？」看是否记得
3. 再试：「用一句话介绍梅州」→「刚才那座城市的特产是什么？」
4. 理解 `trim_history` 怎么砍掉太旧的消息
5. 笔记里写一句：多轮和单轮 body 差在哪？

---

## 运行

```powershell
cd e:\AI_agent_Quick
.\venv\Scripts\Activate.ps1
python exercises/day12/history_chat.py
```

---

## 验收自检

- [ ] 连续两轮，AI 能引用上一轮内容
- [ ] 能说出 user / assistant 在 messages 里怎么交替
- [ ] 知道为什么要 `trim_history`
- [ ] 对比 D7：单轮 messages 长度永远是 1（或 2 含 system）
