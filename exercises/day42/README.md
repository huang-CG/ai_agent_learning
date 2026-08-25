# Day 42 · 智能文档助手 Agent（中型项目 · 第 1 天）

## 这题要你做什么？（一句话）

> 把 **RAG 检索 + 联网搜索 + 沙箱读文件** 三个工具装进同一个 `create_agent`，让模型按题选型。

```
D34：只有 RAG 工具
D35：只有搜索
D37：只有文件沙箱
D42：三件套装一起 → CLI 助手雏形
D43：补交互循环，打磨到「CLI 功能完整」
```

路径请用全路径：

- 今日说明：`exercises/day42/README.md`
- 代码骨架：`exercises/day42/doc_assistant.py`
- 知识库 PDF：复用 `exercises/day32/sample_kb.pdf`
- 待摘要文件：`exercises/day42/sandbox/memo.txt`

---

## 为什么不用 Chroma？

计划写的是 Chroma，但本机 **Python 3.14 + Windows** 下 Chroma 曾写入崩溃（D31）。  
今天继续用 **`InMemoryVectorStore`**，能力等价于「向量库」，不挡验收。

---

## 今日时间盒（约 3h）

| 段 | 大约 | 内容 |
|----|------|------|
| 口述 | 10 min | 三工具何时用 |
| 编码 | ~2h | 填骨架：建库 + 三工具 + Agent + 三问验收 |
| 力扣 | ~30 min | 1 道简单/简单+ |
| 收口 | ~15 min | 理论题 + 笔记 |

时间不够：砍花活，**不砍**「三工具都能被按需调用」。交互 CLI（`input` 循环）留给 **D43**。

---

## 验收（D42）

1. 三个 `@tool`：`search_knowledge` / `web_search` / `read_workspace_file`  
2. 启动时建好向量库（PDF → 切块 → Embed → InMemory）  
3. 三问验收 + 打印 `messages` 的 `.type`：  
   - 知识库内（如吉祥物）→ 应出现 **tool**（检索）  
   - 需要最新/外网事实 → 应调 **web_search**  
   - 「总结 sandbox 里的 memo.txt」→ 应调 **read_workspace_file**  
4. 口述：和「每天只做一个工具」差在哪（选型靠 system_prompt + docstring）

---

## 环境

```powershell
.\venv\Scripts\python.exe exercises\day42\doc_assistant.py
```

依赖：已有 DeepSeek / 硅基 Embedding / `ddgs` / `pypdf`（与 D32–D35 相同）。

---

## D43 预告

交互式 CLI（多轮输入）、错误提示、system_prompt 再收紧；D43 末「CLI 版功能完整」。
