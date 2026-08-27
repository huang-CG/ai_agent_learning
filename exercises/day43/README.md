# Day 43 · 智能文档助手（中型项目 · 第 2 天 · CLI 完善）

## 这题要你做什么？（一句话）

> 在 D42 三工具 Agent 上补上 **多轮交互 CLI**：能连续提问、可退出、报错不崩、system_prompt 写清楚。

```
D42：三工具 + 写死几问验收
D43：input 循环 + 多轮历史 + 错误提示 → CLI 功能完整
D44 起：Web UI（另一段）
```

路径请用全路径：

- 今日说明：`exercises/day43/README.md`
- 代码骨架：`exercises/day43/doc_assistant_cli.py`
- 沙箱文件：复用 `exercises/day42/sandbox/memo.txt`（也可在 day43/sandbox 自备）
- 知识库：仍用 `exercises/day32/sample_kb.pdf`

---

## 今日时间盒（约 2.5h）

| 段 | 大约 | 内容 |
|----|------|------|
| 口述 | 5–10 min | CLI vs 写死验收差在哪 |
| 编码 | ~1.5–2h | 填骨架：收紧 prompt + ask 返回值 + 交互循环 |
| 力扣 | ~25 min | 1 道 |
| 收口 | ~10 min | 理论题 + 笔记 |

时间不够：砍「美化打印」，**不砍** `input` 循环与退出。

---

## 验收（D43 末 · CLI 完整）

1. 启动后进入循环：终端提示输入 → Agent 回答 → 再问下一句  
2. 输入 `quit` / `exit` / `q`（大小写不敏感）→ 礼貌退出，不报错  
3. 空回车 → 提示「请输入问题」，不调 API  
4. 单轮异常（网络等）→ 打印错误，**循环继续**，不整程序崩  
5. **多轮**：第二问能用到第一问上下文（例如先说「我叫小明」，再问「我叫什么」）  
6. system_prompt：读文件写成「sandbox 内任意文本」，不要写死只认 memo.txt  
7. 口述：为什么交互版要把 `result["messages"]` 留下来给下一轮

可选：`--demo` 跑三问自动验收（不挡主验收）。

---

## 环境

```powershell
.\venv\Scripts\python.exe exercises\day43\doc_assistant_cli.py
```

工具实现可从 `exercises/day42/doc_assistant.py` **对照抄思路**，不要整文件无脑粘贴后只改 main。

---

## 和前后天

| 天 | 停在哪 |
|----|--------|
| D12 | 手写 messages 历史 + trim |
| D42 | 三工具装好，固定问句 |
| **D43** | CLI 多轮 + 容错 |
| D44 | Web UI |
