# Day 40 · MCP 协议入门

## 这题要你做什么？（一句话）

> 搞清 **MCP（Model Context Protocol）解决什么问题**，以及它和你已会的 **Function Calling / `@tool`** 是什么关系——今天以**概念 + 笔记对比表**为主，不强制写新 Agent。

```
D14–D15：Function Calling（模型怎么「提议」调工具）
D28–D39：@tool + create_agent（工具写在「这一个」Python 程序里）
D40：   MCP（工具按统一协议「插」进多种 AI 应用，可复用）
D64：   再实战搭一个简单 MCP Server
```

路径：`exercises/day40/README.md`

---

## 先抓住这一句

**MCP 不替代 Function Calling。**

| 层 | 解决什么 | 你已见过的 |
|----|----------|------------|
| **Function Calling** | 模型用结构化方式说：我要调某某工具、参数是什么 | D14 `tool_calls`；LangChain `@tool` |
| **MCP** | 工具怎么**发现、连接、复用**：写一次 Server，Cursor / Claude Desktop / 你的 App 都能接 | 今天新概念 |

类比（帮助记，不必抠死）：

- FC ≈ 你跟服务员说「我要一份炒饭」（点菜格式）  
- MCP ≈ 餐厅菜单、传菜窗口的**统一标准**——换一家店（换 Host）也能用同一套菜单协议  

MCP 要解决的痛点：每个 AI 应用都自己抄一遍 GitHub/文件系统/数据库工具 → **N 个工具 × M 个应用 = 重复胶水**。有了 MCP，工具方做 **Server**，应用方做 **Host/Client**，按协议对话即可。

---

## 三个角色（名字认得即可）

| 角色 | 干什么 | 例子 |
|------|--------|------|
| **Host** | 跑 AI 的应用外壳 | Cursor、Claude Desktop、你的 Agent 程序 |
| **Client** | Host 里负责连 MCP 的那一层 | 读工具列表、转发调用 |
| **Server** | 真正提供工具/资源的一端 | 「读本地文件」Server、「查库」Server |

常见能力类型（面试听到这些词别慌）：

- **Tools**：可调用的函数（最接近你的 `@tool`）  
- **Resources**：可读的数据/文件（像给模型塞上下文）  
- **Prompts**：服务端提供的提示模板（今天知道有即可）

---

## 对比表（验收用 · 自己填进笔记）

在 `notes/学习笔记.md` 的 Day 40 节写一张表（可改表述，意思要对）：

| 维度 | Function Calling / `@tool` | MCP |
|------|----------------------------|-----|
| 主要解决 | 怎么准确调用工具 | 怎么发现、连接和复用工具 |
| 工具写在哪 | python运行文件里 | Server |
| 换一个 AI 应用（如 Cursor→自写 App） | 重新写一套 | 连接Server找到对应得工具使用即可 |
| 和对方的关系 | 是MCP的底层运行机制 | MCP包含FC |
| 你已做过的例子 | D15 / D28–D39 | （今天概念；实战 D64） |

口头验收三问（收工前能答即可）：

1. MCP 全称是什么？它主要解决什么重复劳动？  
2. 为什么说「MCP 不替代 FC」？  
3. 若只要在一个自写 Python Agent 里算温度换算，优先 FC 本地 `@tool` 还是先上 MCP？为什么？

---

## 今日时间盒（约 3h）

| 段 | 时长 | 内容 |
|----|------|------|
| A | ~25min | 口述：FC 回顾 + MCP 要解决的问题（先别查文档） |
| B | ~50min | 读本 README + 官方/鱼皮入门（链接见下），记三个角色 |
| C | ~50min | 自写对比表进笔记；答口头三问 |
| D | ~25min | 力扣 + 收工 |
| 拓展 | 剩余 | 浏览一个 MCP Server 仓库 README（不必跑通）；或 Cursor 里看已接的 MCP 设置页 |

时间不够：**不砍**「对比表 + 口头三问」；砍拓展跑 Server。

---

## 推荐阅读（选 1～2 篇即可，别全啃）

- 官方介绍：[Model Context Protocol](https://modelcontextprotocol.io/)（英文，看 Overview 即可）  
- 计划里的鱼皮站：`ai.codefather.cn` 搜 MCP（有中文入门则优先）  
- 你已会的对照：D14/D15 Function Calling、D28 `@tool`

拓展（有余力）：GitHub 搜 `mcp-server` 示例，只读 README 里的「提供了哪些 tools」，对照今天的「Server 暴露工具」一句话。

---

## 和前后天的关系

| 天 | 停在哪 |
|----|--------|
| D39 | LangSmith：看本机 Agent 每一步 |
| **D40** | **协议层概念**：工具如何标准化接入 |
| D41 | 结构化输出（Pydantic） |
| D64 | MCP 实战：自己搭 Server |

今天过关标准只有一句：**能解释 MCP 解决什么问题，以及它和 FC 不是二选一。**
