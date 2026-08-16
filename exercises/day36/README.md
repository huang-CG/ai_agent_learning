# Day 36 · SQL Agent 概念

## 这题要你做什么？（一句话）

> 建一个小 SQLite 库，把 **跑 SQL** 做成 `@tool`，让 Agent 把「有多少用户？」翻译成 SQL 再查。

```
D34：本地非结构化文档 → RAG
D35：公开网上最新事实 → web_search
D36：本地结构化表格     → SQL
```

路径请用全路径：

- 今日说明：`exercises/day36/README.md`
- 代码骨架：`exercises/day36/sql_agent_lab.py`

---

## 和前后天的关系

| 天 | 数据从哪来 |
|----|------------|
| D32–34 | 文档切块 + 向量检索 |
| D35 | 外网搜索 |
| **D36** | **表结构 + SELECT** |
| D37 | 本地文件读写（沙箱） |

**Text-to-SQL**（今天核心词）：用户说中文 → 模型写出 SQL → 工具执行 → 用查询结果回答。

不要直接抄 LangChain 现成 `SQLDatabaseToolkit` 完事——今天继续 **自己包工具**。官方 SQL Agent 标拓展，时间不够就砍。

---

## 验收

1. 本地有 SQLite 示例库（至少 `users` 表，若干行）  
2. 工具 `run_sql(sql: str) -> str`：执行查询，返回可读文本  
3. **只允许 SELECT**（拒绝 DROP / DELETE / INSERT 等）  
4. `create_agent` 问「有多少用户？」→ messages 里出现 **tool**，人数正确  
5. 再问一句表内事实（如「广州有几个用户」）也能答对  
6. 能口述：Text-to-SQL 三步；SQL 工具 vs RAG vs 搜索各适合什么  

时间不够：砍第二张表、砍官方 SQL Agent；**不砍**「建库 + SELECT 工具 + 有多少用户」。

---

## 环境

SQLite 是 Python 标准库，一般不用再装包。

```powershell
.\venv\Scripts\python.exe exercises\day36\sql_agent_lab.py
```

复用 DeepSeek（`.env`）。库文件会写在 `exercises/day36/demo.db`（可重复重建）。

SQL 小抄（今天够用）：

```sql
SELECT COUNT(*) FROM users;
SELECT * FROM users WHERE city = '广州';
```

---

## 今日时间盒（约 3h）

| 段 | 时长 | 内容 |
|----|------|------|
| A | ~15min | 口述：Text-to-SQL；SQL vs RAG vs 搜索 |
| B | ~40min | 建库 + 裸 SQL 冒烟（不经 Agent） |
| C | ~90min | `run_sql` 工具 + `create_agent` + 两问验收 |
| D | ~25min | 力扣 + 收工 |

实践日：先自己填骨架；卡住约 15～20 分钟再要最小提示。
