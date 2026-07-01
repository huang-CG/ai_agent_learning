# AI Agent 工程师 · 90 天日计划

> 基于 [鱼皮 AI Agent 学习路线](https://www.codefather.cn/post/2029156872593256451) 压缩编排  
> 适用：零基础 · 日均 2–4h · 高执行力  
> 技术栈：**Python + LangChain/LangGraph**（AI Agent 主流栈，上手最快）  
> 项目收官：自建 Agent 项目 + 鱼皮教程对照（有 VIP 可跟 `yu-ai-agent` 或 AI 零代码平台）

---

## 使用说明

1. **每天开始前**：告诉我「今天有 X 小时」，我会从当日任务中裁剪或补充
2. **每天结束后**：说「今日学习完成」，我会更新 `notes/学习笔记.md` 和 `CONTEXT.md`
3. **标准时长**：每任务标注 `⏱` 为 3h 基准；2h 做 ★ 任务，4h 加「拓展」
4. **资源入口**：
   - [编程导航](https://www.codefather.cn/) · [AI 导航](https://ai.codefather.cn/)
   - [AI Agent 路线](https://www.codefather.cn/post/2029156872593256451)
   - [AI 大模型路线](https://www.codefather.cn/download/agentroad)
   - [LangChain 教程](https://www.codefather.cn/)（站内搜索）
   - 开源参考：[yu-ai-agent](https://github.com/liyupi/yu-ai-agent) · [ai-guide](https://github.com/liyupi/ai-guide)

---

## 阶段总览

| 阶段 | 天数 | 主题 | 通关标志 |
|------|------|------|----------|
| 0 | D1–7 | 环境与 Python 基础 | 能写脚本调 API |
| 1 | D8–17 | LLM + Prompt + API | 完成 Prompt 实验 + API 小项目 |
| 2 | D18–27 | Agent 概念 + ReAct | 手写 ReAct 天气 Agent |
| 3 | D28–47 | LangChain / RAG / Tools | 带 RAG 的工具 Agent |
| 4 | D48–57 | LangGraph + 多 Agent | 多角色协作 Demo |
| 5 | D58–67 | 优化 + 部署 + MCP | 可访问的 API 服务 |
| 6 | D68–82 | 综合项目实战 | 完整 Agent 作品 + README |
| 7 | D83–90 | 求职备战 | 简历 + 20 道面试题 |

---

## Phase 0：环境与 Python 基础（D1–7）

### D1 · 启动日 ⏱3h（2026-07-01）
**目标**：环境验证 + AI 认知建立 + DeepSeek 就绪

| 优先级 | 任务 | 资源 |
|--------|------|------|
| ★ | 验证：`python --version`、`git --version` | 终端 |
| ★ | 创建 venv + `pip install requests`；Key 写入 `.env` | 本地（Key 预习已完成） |
| ★ | 观看鱼皮《AI 指南》前 3 章 | 编程导航 VIP |
| ★ | 浏览 AI Agent 路线，列出 5 个不懂的术语 | 路线链接 |
| 拓展 | 创建 GitHub 仓库 `ai-agent-learning` 并首次 commit | Git |

**验收**：venv 可用；DeepSeek Key 已保存；5 个术语写入笔记；能口述 Agent 是什么

---

### D2 · Python 语法（一）⏱3h
**目标**：变量、类型、条件、循环

| ★ | 学习鱼皮「十分钟速通 Python」第 1–2 章 | 编程导航 |
| ★ | 练习：计算器程序（加减乘除 + 循环菜单） | 自建 |
| 拓展 | 完成 10 道基础语法题 | 牛客 / LeetCode Easy |

**验收**：独立写出含 `if/for` 的计算器脚本

---

### D3 · Python 语法（二）⏱3h
**目标**：函数、列表、字典

| ★ | 速通 Python 第 3–4 章 | 编程导航 |
| ★ | 练习：通讯录 CLI（增删查联系人） | 自建 |
| 拓展 | 读「从 0 到 1 学 Python」函数章节 | 编程导航 |

**验收**：通讯录能持久化到 JSON 文件

---

### D4 · Python 进阶 ⏱3h
**目标**：模块、文件、异常、pip

| ★ | 学习 `requests` 库，发 GET 请求 | 文档 |
| ★ | 练习：调用免费天气 API 打印结果 | 自建 |
| 拓展 | 了解 venv 虚拟环境 | — |

**验收**：脚本成功打印天气 JSON

---

### D5 · Git 与项目结构 ⏱3h
**目标**：版本管理 + 工程习惯

| ★ | 鱼皮 Git 教程前 4 章 | 编程导航 |
| ★ | 创建 GitHub 仓库 `ai-agent-learning` | github.com |
| ★ | 提交 D2–D4 代码 | — |

**验收**：远程仓库有至少 3 次 commit

---

### D6 · 面向对象 + JSON ⏱3h
**目标**：能读懂框架代码

| ★ | Python class 基础（`__init__`、方法） | 速通 Python |
| ★ | 重构通讯录为 OOP 版本 | 自建 |
| 拓展 | 阅读 LangChain 官方 Quickstart 代码（只读） | langchain.com |

**验收**：OOP 版通讯录可运行

---

### D7 · Phase 0 总结 ⏱3h
**目标**：整合，第一次调 LLM API

| ★ | 用 Python 调用大模型 API（chat/completions） | API 文档 |
| ★ | 实现：命令行 AI 问答（单轮） | 自建 |
| ★ | 写 Phase 0 复盘（200 字） | 笔记 |

**验收**：终端输入问题 → 打印 AI 回答

---

## Phase 1：LLM + Prompt + API（D8–17）

### D8 · LLM 基础概念 ⏱3h
| ★ | AI 指南：LLM、Transformer、Token、上下文窗口 | 编程导航 |
| ★ | 实验：同一问题不同 temperature 对比 | 网页/API |
| 拓展 | 鱼皮「AI 为什么会胡说八道」文章 | codefather |

**验收**：用自己的话解释 Token 和幻觉

---

### D9 · Prompt 基础 ⏱3h
| ★ | Prompt Engineering 路线：基础 + Few-shot | 编程导航 |
| ★ | 练习 5 种 Prompt（翻译/摘要/分类/提取/生成） | ChatGPT |
| ★ | 记录哪种 Prompt 效果最好 | 笔记 |

**验收**：5 个 Prompt 模板存入笔记

---

### D10 · 思维链 CoT ⏱3h
| ★ | 学习 Chain-of-Thought、角色扮演 | Prompt 路线 |
| ★ | 对比：普通 Prompt vs CoT 解数学题 | API |
| ★ | 实现：API 版「逐步推理」问答 | 自建 |

**验收**：CoT 正确率明显高于普通 Prompt

---

### D11 · API 深入 ⏱3h
| ★ | 参数：temperature、top_p、max_tokens、stop | OpenAI/百炼文档 |
| ★ | 实现：流式输出（streaming）CLI | 自建 |
| 拓展 | 错误重试 + 超时处理 | — |

**验收**：流式打印 AI 回复

---

### D12 · 多轮对话 ⏱3h
| ★ | 理解 messages 数组与对话历史 | 文档 |
| ★ | 实现：带历史的 CLI 聊天机器人 | 自建 |
| ★ | 限制历史长度（防 Token 爆炸） | — |

**验收**：能连续对话且记得上一轮内容

---

### D13 · Prompt 优化实战 ⏱3h
| ★ | System Prompt 设计原则 | AI 指南 |
| ★ | 为聊天机器人写 3 版 System Prompt 对比 | 自建 |
| 拓展 | 输出格式控制（JSON mode / 结构化） | — |

**验收**：选定最优 System Prompt 并说明理由

---

### D14 · Function Calling 原理 ⏱3h
| ★ | 学习 Function Calling 概念与 JSON Schema | 官方文档 |
| ★ | 阅读：模型如何决定调用哪个工具 | 文章 |
| ★ | 画流程图：用户 → LLM → 工具 → LLM → 用户 | 笔记 |

**验收**：手绘/文字版 Function Calling 流程

---

### D15 · Function Calling 实战 ⏱3h
| ★ | 实现：LLM 调用「获取当前时间」函数 | 自建 |
| ★ | 实现：LLM 调用「计算器」函数 | 自建 |
| 拓展 | 多函数场景：模型自动选择 | — |

**验收**：模型能正确选择并调用函数

---

### D16 · RAG 概念预习 ⏱3h
| ★ | 学习：Embedding、向量、相似度、RAG 流程 | AI 大模型路线 |
| ★ | 使用 Dify / 百炼知识库体验 RAG（零代码） | Dify |
| 拓展 | 了解 Chroma / FAISS | — |

**验收**：解释 RAG 解决什么问题

---

### D17 · Phase 1 小项目 ⏱3h
**项目**：「个人知识库问答 Bot（API 版，无向量库）」

| ★ | 把文档拼进 Prompt 做简易 QA | 自建 |
| ★ | 对比 RAG 与直接拼 Prompt 的局限 | 笔记 |
| ★ | 提交 Git + Phase 1 复盘 | — |

**验收**：能对自己写的 markdown 文档问答

---

## Phase 2：Agent 概念 + ReAct（D18–27）

### D18 · Agent 是什么 ⏱3h
| ★ | AI Agent 路线 Phase 2：核心概念 | 路线 |
| ★ | 理解：感知-推理-决策-执行 | 笔记 |
| ★ | 对比 Agent vs 普通 Chatbot（表格） | 笔记 |

**验收**：1 分钟口述 Agent 定义

---

### D19 · ReAct 架构 ⏱3h
| ★ | 精读 ReAct 思想：Thought → Action → Observation 循环 | 论文/文章 |
| ★ | 手工模拟 1 个 ReAct 推理过程（纸笔） | — |
| 拓展 | 鱼皮 AI 超级智能体项目介绍视频（了解即可） | VIP/简介 |

**验收**：完整写出 1 个 ReAct 循环示例

---

### D20 · 工具定义与描述 ⏱3h
| ★ | 工具 Schema 设计：name、description、parameters | 文档 |
| ★ | 编写 3 个工具定义（天气/搜索/计算） | 自建 |
| ★ | 理解：description 质量影响调用准确率 | — |

**验收**：3 个工具 JSON Schema 完成

---

### D21 · 手写 ReAct Agent（一）⏱3h
| ★ | 实现 ReAct 主循环（不含真实工具） | 自建 |
| ★ | 解析 LLM 输出的 Thought/Action | — |
| 拓展 | 正则 vs JSON 解析对比 | — |

**验收**：循环能跑 3 轮后停止

---

### D22 · 手写 ReAct Agent（二）⏱3h
| ★ | 接入真实工具：天气 API | 自建 |
| ★ | 实现 Observation 回传 | — |
| ★ | 加 max_steps 防死循环 | — |

**验收**：问「北京天气」能正确调用并回答

---

### D23 · Agent 记忆系统 ⏱3h
| ★ | 短期记忆：对话历史管理 | 路线 |
| ★ | 长期记忆：向量库概念 | 路线 |
| ★ | 给 ReAct Agent 加对话历史 | 自建 |

**验收**：Agent 记住用户名字

---

### D24 · Plan-and-Execute 与 Reflection ⏱3h
| ★ | 了解 Plan-and-Execute、Reflection 模式 | 路线 |
| ★ | 对比 ReAct vs Plan-and-Execute 适用场景 | 笔记 |
| 拓展 | 看 LangGraph 官方 Plan-and-Execute 示例 | 文档 |

**验收**：笔记中 3 种架构对比表

---

### D25 · Agent 调试 ⏱3h
| ★ | 加日志：每步 Thought/Action/Observation | 自建 |
| ★ | 排查：工具未被调用 / 参数错误 | — |
| ★ | 优化 System Prompt 提升工具选择准确率 | — |

**验收**：日志清晰，准确率 > 80%（10 题测试）

---

### D26 · LangChain 入门 ⏱3h
| ★ | 安装 langchain、langchain-openai（或兼容包） | pip |
| ★ | 跑通 LangChain 官方 Quickstart | 文档 |
| ★ | 对比：手写 Agent vs LangChain Agent | 笔记 |

**验收**：LangChain 版 Hello Agent 跑通

---

### D27 · Phase 2 总结 ⏱3h
| ★ | 用 LangChain 重写 ReAct 天气 Agent | 自建 |
| ★ | 写 README：架构说明 + 运行方式 | Git |
| ★ | Phase 2 复盘 | 笔记 |

**验收**：Git 仓库 Phase 2 里程碑 tag

---

## Phase 3：LangChain / RAG / Tools（D28–47）

### D28 · LangChain Tools ⏱3h
| ★ | `@tool` 装饰器、Tool 绑定 | 文档 |
| ★ | 创建自定义工具集 | 自建 |
| 拓展 | StructuredTool | — |

**验收**：3 个 LangChain Tool 可用

---

### D29 · LangChain Agent ⏱3h
| ★ | create_react_agent / AgentExecutor | 文档 |
| ★ | 组装：LLM + Tools + Agent | 自建 |
| ★ | 处理 parsing error | — |

**验收**：LangChain ReAct Agent 跑通

---

### D30 · 文档加载与分割 ⏱3h
| ★ | Document Loader、Text Splitter | 文档 |
| ★ | 加载本地 PDF/Markdown 并切块 | 自建 |
| 拓展 | chunk_size / overlap 实验 | — |

**验收**：文档切分为 chunks 并打印统计

---

### D31 · Embedding 与向量库 ⏱3h
| ★ | Embedding 模型调用 | API |
| ★ | Chroma 本地向量库 | pip install chromadb |
| ★ | 写入 + 相似度检索 | 自建 |

**验收**：query 返回 top-3 相关片段

---

### D32 · RAG 管道 ⏱3h
| ★ | 完整 RAG：Load → Split → Embed → Store → Retrieve → Generate | 自建 |
| ★ | 对比不同 chunk_size 效果 | — |
| 拓展 | 鱼皮 RAG 相关教程章节 | VIP |

**验收**：对 PDF 文档准确问答

---

### D33 · RAG 优化 ⏱3h
| ★ | 优化：Hybrid Search 概念、metadata 过滤 | 文章 |
| ★ | 加 source 引用（回答标注出处） | 自建 |
| ★ | 处理「文档中没有」的情况 | — |

**验收**：回答带来源；无答案时不编造

---

### D34 · RAG + Agent 结合 ⏱3h
| ★ | 把 RAG 检索做成 Agent 工具 | 自建 |
| ★ | Agent 决定何时查知识库 vs 直接回答 | — |
| 拓展 | Self-RAG 概念 | — |

**验收**：Agent 能按需检索知识库

---

### D35 · 搜索工具集成 ⏱3h
| ★ | 接入 Tavily / DuckDuckGo 搜索 API | 免费 API |
| ★ | Agent 工具：web_search | 自建 |
| ★ | 测试：需要实时信息的问题 | — |

**验收**：能回答今日新闻类问题

---

### D36 · SQL Agent 概念 ⏱3h
| ★ | Text-to-SQL 原理 | 教程 |
| ★ | 创建 SQLite 示例库 + 自然语言查数 | 自建 |
| 拓展 | LangChain SQL Agent 官方示例 | — |

**验收**：「有多少用户？」类问题正确

---

### D37 · 文件操作工具 ⏱3h
| ★ | 工具：读文件、写文件、列目录 | 自建 |
| ★ | 安全：限制可访问目录 | — |
| ★ | Agent 能总结指定文件内容 | — |

**验收**：安全沙箱内文件操作正常

---

### D38 · Prompt 工程进阶 ⏱3h
| ★ | Agent System Prompt 最佳实践 | 鱼皮教程 |
| ★ | Few-shot 示例嵌入 Agent | 自建 |
| ★ | 输出格式约束（JSON/结构化） | — |

**验收**：Agent 输出格式稳定

---

### D39 · LangSmith 调试 ⏱3h
| ★ | 注册 LangSmith，接入 tracing | langsmith.com |
| ★ | 查看 Agent 每步 trace | — |
| ★ | 分析 1 次失败调用原因 | 笔记 |

**验收**：LangSmith 能看到完整 trace

---

### D40 · MCP 协议入门 ⏱3h
| ★ | 学习 MCP（Model Context Protocol）概念 | ai.codefather.cn |
| ★ | 了解 MCP vs Function Calling | 笔记 |
| 拓展 | 跑通一个 MCP Server 示例 | GitHub |

**验收**：解释 MCP 解决什么问题

---

### D41 · 结构化输出 ⏱3h
| ★ | Pydantic + LangChain structured output | 文档 |
| ★ | Agent 输出结构化报告（JSON） | 自建 |
| 拓展 | Instructor 库 | — |

**验收**：输出通过 Pydantic 校验

---

### D42–D43 · 中型项目（一）（2 天）⏱3h/天
**项目**：「智能文档助手 Agent」

| ★ | 功能：RAG 问答 + 网络搜索 + 文件摘要 | 自建 |
| ★ | 技术：LangChain + Chroma + 3 Tools | — |
| ★ | 每日 commit + 进度笔记 | Git |

**验收 D43 末**：CLI 版功能完整

---

### D44–D47 · 中型项目（二）完善（4 天）⏱3h/天
| ★ | 加 Streamlit/Gradio Web UI | 自建 |
| ★ | 错误处理 + 加载态 + 会话历史 | — |
| ★ | 写测试用例 10 条 + 通过率 | — |
| ★ | README + 架构图 | Git |

**验收**：Web 版可演示；测试 ≥ 80% 通过

---

## Phase 4：LangGraph + 多 Agent（D48–57）

### D48 · LangGraph 基础 ⏱3h
| ★ | 图、节点、边、State 概念 | 文档 |
| ★ | 跑通官方 Hello Graph | — |
| ★ | 对比 LangChain Agent vs LangGraph | 笔记 |

**验收**：最简单的 2 节点 Graph 跑通

---

### D49 · State 与条件分支 ⏱3h
| ★ | TypedDict State 设计 | 文档 |
| ★ | 条件边：根据 LLM 输出路由 | 自建 |
| 拓展 | 人工介入（interrupt）概念 | — |

**验收**：Agent 能走不同分支

---

### D50 · 循环与终止 ⏱3h
| ★ | ReAct 用 LangGraph 重写 | 自建 |
| ★ | 终止条件：max_iterations / 用户满意 | — |
| ★ | 对比手写版与 Graph 版 | 笔记 |

**验收**：LangGraph ReAct 与 D27 功能等价

---

### D51 · 多 Agent 概念 ⏱3h
| ★ | 路线 Phase 4：协作模式、角色设计 | 路线 |
| ★ | 了解 AutoGen / MetaGPT 架构 | GitHub |
| ★ | 设计：Researcher + Writer 双 Agent 方案 | 笔记 |

**验收**：双 Agent 协作流程图

---

### D52 · 多 Agent 实现（一）⏱3h
| ★ | LangGraph 多节点：Research → Write | 自建 |
| ★ | 节点间 State 传递 | — |
| 拓展 | Supervisor 模式概念 | — |

**验收**：输入主题 → 输出文章

---

### D53 · 多 Agent 实现（二）⏱3h
| ★ | 加 Reviewer Agent 审核修改 | 自建 |
| ★ | 加 max_rounds 防无限循环 | — |
| ★ | 日志可视化每 Agent 输出 | — |

**验收**：3 Agent 协作生成高质量回答

---

### D54 · Supervisor 模式 ⏱3h
| ★ | 实现 Supervisor 分发任务 | 教程 |
| ★ | 子 Agent：搜索 / 代码 / 写作 | 自建 |
| 拓展 | 鱼皮 AI 零代码平台工作流章节 | VIP |

**验收**：Supervisor 正确路由到子 Agent

---

### D55 · 工作流编排实战 ⏱3h
| ★ | 复杂流程：条件 + 并行 + 重试 | 自建 |
| ★ | 错误节点与 fallback | — |
| 拓展 | LangGraph Studio 可视化 | — |

**验收**：含错误处理的 workflow 跑通

---

### D56 · Human-in-the-loop ⏱3h
| ★ | 关键步骤人工确认 | 文档 |
| ★ | 实现：删除文件前需用户批准 | 自建 |
| ★ | 安全与权限意识总结 | 笔记 |

**验收**：危险操作被拦截

---

### D57 · Phase 4 总结 ⏱3h
| ★ | 整合多 Agent 项目代码 | Git |
| ★ | 录制 2 分钟演示视频 | 本地 |
| ★ | Phase 4 复盘 | 笔记 |

**验收**：可演示的多 Agent Demo

---

## Phase 5：优化 + 部署 + 生产化（D58–67）

### D58 · 性能优化 ⏱3h
| ★ | Prompt 压缩、缓存常见问答 | 路线 Phase 5 |
| ★ | 并行工具调用 | — |
| ★ | Token 用量统计 | 自建 |

**验收**：同任务 Token 消耗下降 20%+

---

### D59 · 成本与安全 ⏱3h
| ★ | 输入过滤、输出审查 | 路线 |
| ★ | API Key 环境变量管理 | — |
| ★ | 工具权限白名单 | 自建 |

**验收**：无明文 Key；危险输入被拦截

---

### D60 · FastAPI 封装 ⏱3h
| ★ | 学习 FastAPI 基础（Quickstart） | 官方文档 |
| ★ | 把 Agent 封装为 `/chat` API | 自建 |
| ★ | 本地 Postman/curl 测试 | — |

**验收**：HTTP 调用 Agent 成功

---

### D61 · 流式 API + SSE ⏱3h
| ★ | FastAPI StreamingResponse / SSE | 文档 |
| ★ | Agent 流式返回 | 自建 |
| 拓展 | 鱼皮 SSE 相关教程 | VIP |

**验收**：客户端看到逐字输出

---

### D62 · Docker 部署 ⏱3h
| ★ | 编写 Dockerfile + docker-compose | 自建 |
| ★ | 本地 Docker 跑通 | — |
| 拓展 | 云服务器部署（阿里云/腾讯云） | — |

**验收**：`docker compose up` 后 API 可访问

---

### D63 · 监控与日志 ⏱3h
| ★ | 结构化日志 | 自建 |
| ★ | LangSmith 生产 tracing | — |
| ★ | 简单健康检查 `/health` | — |

**验收**：出错时可追溯完整链路

---

### D64 · MCP 实战 ⏱3h
| ★ | 创建简单 MCP Server | 文档 |
| ★ | Agent 通过 MCP 调用工具 | — |
| 拓展 | 对接 Cursor MCP | — |

**验收**：MCP 工具被 Agent 成功调用

---

### D65 · 评估 Agent 质量 ⏱3h
| ★ | 设计 20 条 eval 测试集 | 自建 |
| ★ | 指标：准确率、延迟、Token 成本 | — |
| ★ | 跑 benchmark 记录 baseline | 笔记 |

**验收**：eval 报告完成

---

### D66 · A/B Prompt 测试 ⏱3h
| ★ | 两个 System Prompt 版本对比 | 自建 |
| ★ | 记录 eval 结果差异 | — |
| ★ | 选定生产版 Prompt | — |

**验收**：数据驱动的 Prompt 选型

---

### D67 · Phase 5 总结 ⏱3h
| ★ | 部署版 Agent 上线（本地或云） | — |
| ★ | 写运维文档 | Git |
| ★ | Phase 5 复盘 | 笔记 |

**验收**：他人可通过 URL 使用你的 Agent

---

## Phase 6：综合项目实战（D68–82）

> **推荐项目**（三选一，默认 A）  
> A. **职场效率 Agent**：邮件/日程/文档处理多工具 Agent（Python）  
> B. **智能客服 Agent**：RAG + 工单 + 人工转接（Python）  
> C. **跟鱼皮 VIP 项目**：yu-ai-agent 或 AI 零代码平台（Java，需补 Java 基础）

### D68 · 选题 + 需求 ⏱3h
| ★ | 确定项目方向与 MVP 功能列表 | — |
| ★ | 画架构图、数据流 | 笔记 |
| ★ | 创建项目仓库 | Git |

---

### D69–D71 · 核心开发（3 天）⏱3h/天
| ★ | LLM 接入 + Agent 核心循环 | 自建 |
| ★ | 至少 3 个 Tool + RAG | — |
| ★ | 多轮对话 + 记忆 | — |

---

### D72–D74 · 高级特性（3 天）⏱3h/天
| ★ | LangGraph 工作流 | 自建 |
| ★ | 流式 Web UI | — |
| ★ | 错误处理 + 日志 | — |

---

### D75–D77 · 打磨（3 天）⏱3h/天
| ★ | eval 测试 + 修复 | — |
| ★ | Prompt 优化 | — |
| ★ | UI/UX 改进 | — |

---

### D78–D80 · 部署 + 文档（3 天）⏱3h/天
| ★ | Docker 部署 | — |
| ★ | README：功能、架构、运行、截图 | Git |
| ★ | 2 分钟演示视频 | — |

---

### D81 · 开源与博客 ⏱3h
| ★ | 整理代码、加 LICENSE | Git |
| ★ | 写技术博客 1 篇（开发心得） | 编程导航/community |
| 拓展 | 参考鱼皮项目简历写法 | VIP |

---

### D82 · Phase 6 验收 ⏱3h
| ★ | 完整演示走查 | — |
| ★ | 对照 Agent 路线 Phase 6 checklist | — |
| ★ | 项目复盘 | 笔记 |

**通关标志**：可在线访问的 Agent 项目 + 完整文档

---

## Phase 7：求职备战（D83–90）

### D83 · 简历 ⏱3h
| ★ | 鱼皮写简历指南 | 编程导航 |
| ★ | 写 AI Agent 工程师简历初稿 | — |
| ★ | 项目经历 STAR 描述 | — |

---

### D84 · 面试题（基础）⏱3h
| ★ | 面试鸭：AI Agent 专题 10 题 | 面试鸭 |
| ★ | 整理标准答案 | 笔记 |

---

### D85 · 面试题（架构）⏱3h
| ★ | ReAct / RAG / 多 Agent / MCP 各 5 题 | 笔记 |
| ★ | 结合自己项目回答 | — |

---

### D86 · 面试题（实战）⏱3h
| ★ | 项目深挖：难点、优化、评估 | — |
| ★ | 模拟：介绍项目 3 分钟 | 录音 |

---

### D87 · LangChain 源码/原理 ⏱3h
| ★ | 了解 AgentExecutor 执行流程 | 源码 |
| ★ | 了解 Embedding 与向量检索原理 | — |
| 拓展 | 读 1 篇 Agent 相关论文摘要 | — |

---

### D88 · 行业动态 ⏱3h
| ★ | 浏览 AI 导航最新资讯 | ai.codefather.cn |
| ★ | 了解 OpenAI Agents SDK / Claude Tool Use 动态 | — |
| ★ | 笔记：3 个行业趋势 | — |

---

### D89 · 模拟面试 ⏱3h
| ★ | 编程导航 1 对 1 模拟面试（或自问自答） | VIP/自建 |
| ★ | 复盘薄弱点 | 笔记 |

---

### D90 · 毕业日 ⏱3h
| ★ | 90 天总复盘 | 笔记 |
| ★ | 更新 GitHub Profile + 项目 pin | — |
| ★ | 制定后续 30 天计划（进阶/投递） | — |

**通关标志**：简历 ready + 20+ 面试题答案 + 1 个可演示项目

---

## 每日时间裁剪指南

| 可用时间 | 策略 |
|----------|------|
| 2h | 仅做 ★ 任务的第一项 + 最小验收 |
| 3h | 标准计划 |
| 4h | 标准 + 「拓展」 |
| 5h+ | 标准 + 拓展 + 提前预习次日内容 |
| 不足 2h | 复习前日笔记 + 1 个小练习，不算完成当日，顺延 |

---

## 补充资源（非鱼皮）

| 资源 | 用途 |
|------|------|
| [LangChain 官方文档](https://python.langchain.com/) | 框架权威参考 |
| [LangGraph 文档](https://langchain-ai.github.io/langgraph/) | 工作流编排 |
| [DeepLearning.AI Agent 短课](https://www.deeplearning.ai/) | 免费视频补充 |
| [Anthropic Prompt 指南](https://docs.anthropic.com/) | Prompt 工程 |
| [Tavily Search API](https://tavily.com/) | Agent 搜索工具 |

---

## 学员配置（已确认 2026-06-30）

- [x] VIP → Phase 6 跟 **yu-ai-agent**
- [x] API → **DeepSeek**（`base_url=https://api.deepseek.com`）
- [x] D1 → **2026-07-01**
- [x] 求职 → **AI Agent 岗位**
- [x] 环境已装 → D1 跳过安装步骤
