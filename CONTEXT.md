# AI Agent 学习上下文（Agent 用）

> 极简进度文档，供每日对话快速恢复上下文  
> 最后更新：2026-07-08 | 状态：**D8 ✅ 完成 · Phase 1 进行中**

---

## 学员 profile

| 键 | 值 |
|---|---|
| 目标 | **AI Agent / AI 应用岗**（求职向） |
| 城市 | **广州**（可投深圳 remote/hybrid） |
| 学习模式 | **非全职**（日均 2–4h） |
| 岗位范围 | 纯 Agent 岗 + **AI 应用 / Python+LLM 岗均可** |
| 基础 | 零基础 |
| 计划周期 | 90 天（D1=2026-07-01） |
| 技术栈 | Python + LangChain/LangGraph |
| API | **DeepSeek** ✅ |
| VIP | ✅（Phase 6 → yu-ai-agent） |
| 环境 | Python 3.14.6 / Git 2.54 / venv ✅ |
| 执行力 | 高 |

---

## 当前状态

```
Day:    8 / 90 ✅
Phase:  1 (D8/17 进行中)
Next:   D9 Prompt 基础 · 5 种 Prompt 练习
```

---

## 阶段 checkpoint

| Ph | 范围 | 状态 | 通关标准 |
|---|---|---|---|
| 0 | D1–7 | ✅ 7/7 | Python + 首次 API 调用 |
| 1 | D8–17 | 🔄 1/10 | Prompt 实验 + Function Calling |
| 2 | D18–27 | ⬜ | 手写 ReAct + LangChain 重写 |
| 3 | D28–47 | ⬜ | RAG Agent + Web UI |
| 4 | D48–57 | ⬜ | LangGraph 多 Agent |
| 5 | D58–67 | ⬜ | FastAPI 部署 + Docker |
| 6 | D68–82 | ⬜ | 毕业综合项目 |
| 7 | D83–90 | ⬜ | 简历 + 面试 ready |

---

## 每日 log（倒序，最新在上）

| Day | 日期 | 时长 | 完成摘要 | 问题 | 自评 | Agent |
|-----|------|------|----------|------|------|-------|
| D8 | 2026-07-08 | 3h | LLM概念✅ temperature实验✅ try/except✅ FizzBuzz✅ | 廖雪峰旧链接404 | 4 | 4 |
| D7 | 2026-07-07 | 2h | DeepSeek CLI问答✅ ask_ai+main✅ POST/JSON解析✅ Phase0复盘✅ | 全角括号、URL/role拼写；文档模型名差异 | 4 | 4 |
| D6 | 2026-07-06 | 3h | OOP通讯录✅ Contact对象✅ JSON持久化✅ D7预习✅ | 未保存代码、dict/Contact混用、list_all误写 | 4 | 4 |
| D5 | 2026-07-05 | 4h | Git教程✅ GitHub push✅ README✅ OOP预习✅ D3→D6映射✅ | D2–4 commit 非亲手；命令误敲 | 5 | 4 |
| D4 | 2026-07-04 | 3h | 模块/pip✅ requests✅ 天气API✅ 中文格式化✅ | 理论散、语法/结构弱 | 3 | 4 |
| D3 | 2026-07-03 | 3h | 函数✅ 通讯录✅ JSON持久化✅ 全功能通过 | load vs list、break误用 | 4 | 4 |
| D2 | 2026-07-02 | 3h | 速通Py 1–2章✅ 计算器✅ 交互模式✅ | 题意理解难、缩进错误 | 2 | 3 |
| D1 | 2026-07-01 | 3h | env✅ AI指南3章✅ Agent路线✅ Git commit | copy命令 typo | 5 | 5 |

### Agent 评分标准（1–5）

| 分 | 含义 |
|----|------|
| 5 | 验收全过，基本独立，理解到位 |
| 4 | 验收全过，有小 bug/需少量指导，最终理解好 |
| 3 | 验收通过，但独立度一般或需较多提示 |
| 2 | 部分完成或核心理解明显不足 |
| 1 | 几乎未完成 |

依据：★ 任务完成情况、代码独立度、调试过程、概念理解（对话中体现）。

---

## 已掌握（累计）

**D1**：Agent 概念；venv + `.env`

**D2**：`if/for/while`；`>>>` vs `python xxx.py`

**D3**：列表+字典；`json.load/dump`；多函数 + 菜单循环

**D4**：`pip`/`import` 第三方库；`requests.get` + `.json()`；URL `?` 参数；`dict.get`

**D5**：`git add/commit/push/pull`；GitHub 远程仓库；文件状态（Untracked→Staged→Committed）；OOP 预习（class/`__init__`/self）

**D6**：OOP 通讯录；`Contact` / `AddressBook`；`self.contacts`；JSON dict ↔ Contact 转换；`with open(..., "w")`

**D7**：DeepSeek Chat Completions；`requests.post` + `json=body`；`choices[0].message.content`；`os.getenv` + `.env`；`raise_for_status`

**D8**：LLM/Token/上下文窗口/幻觉；`temperature` 参数实验；`try/except`（ValueError/ZeroDivisionError）

**薄弱点（持续）**：语法结构（if/elif、缩进、函数层级、拼写）；理论吸收偏散

**学习调整（D4 起）**：Python 理论主线改跟 **廖雪峰教程一条线**；语法题零碎时间补

**Java**：想学，但 **90 天主线完成后再学**（Phase 6 或之后）；当前不并行

---

## 求职预期（2026-07-04 确认）

| 项 | 内容 |
|----|------|
| 现实时间线 | 90 天 ≈ 能投递；offer 更现实 **2026 年底 ~ 2027 年初**（非全职） |
| 广州 JD 关键词 | Python 大模型 / LLM 应用 / AI 应用开发 / RAG |
| 简历核心 | D68–82 毕业项目 + GitHub 仓库 |
| 评分 | 每日自评 + **Agent 客观评分**（见 daily log） |

---

## 调整记录

| 日期 | 调整 |
|---|---|
| 2026-06-30 | 创建 90 天计划 |
| 2026-07-01 | **D1 完成**，自评 5 / Agent 5 |
| 2026-07-02 | **D2 完成**，自评 2 / Agent 3 |
| 2026-07-03 | **D3 完成**，自评 4 / Agent 4 |
| 2026-07-04 | **D4 完成**，自评 3 / Agent 4；理论改单线+语法加强 |
| 2026-07-04 | 求职画像：广州/非全职/AI应用岗可；Java 主线后再学 |
| 2026-07-05 | **D5 完成**，自评 5 / Agent 4；GitHub [ai_agent_learning](https://github.com/huang-CG/ai_agent_learning) |
| 2026-07-06 | **D6 完成**，自评 4 / Agent 4；OOP 通讯录 + D7 DeepSeek API 预习 |
| 2026-07-07 | **D7 完成**，自评 4 / Agent 4；首次 LLM API + **Phase 0 通关** |
| 2026-07-08 | **D8 完成**，自评 4 / Agent 4；LLM 概念 + temperature；每日刷题规则确认 |

---

## 关键路径（不可跳过）

1. D7  首次 LLM API 调用
2. D15 Function Calling 实战
3. D22 手写 ReAct Agent
4. D32 完整 RAG 管道
5. D50 LangGraph ReAct
6. D60 FastAPI 封装
7. D68–82 毕业项目

---

## 文件索引

| 文件 | 用途 |
|------|------|
| `LEARNING_PLAN.md` | 完整 90 天日计划 |
| `notes/学习笔记.md` | 学员笔记 |
| `CONTEXT.md` | 本文件 |
| `exercises/day02/calculator.py` | D2 计算器 |
| `exercises/day03/address_book.py` | D3 通讯录 |
| `exercises/day04/weather.py` | D4 天气 API |
| `exercises/day06/address_book_oop.py` | D6 OOP 通讯录 |
| `exercises/day07/chat.py` | D7 命令行 AI 问答 |
| GitHub `huang-CG/ai_agent_learning` | D5 远程仓库 |

---

## 每日协作流程

```
早上：报「今天 X 小时，Day N 开始」
晚上：报「今日学习完成」+ 自评 → 更新两文档 + Agent 客观评分
```

### 每日刷题（D7 起，学员确认 2026-07-08）

| 类型 | 数量 | 时机 | 规则 |
|------|------|------|------|
| **力扣编程题** | 1～2 道/天 | 当日课程结束后**当场做**，贴代码给 Agent 检查 | 从「简单」起步，根据完成情况**循序渐进**加难度 |
| **理论选择题** | 1～2 道/天 | **零碎时间**自己做，像八股/概念自测 | 附参考答案与「为什么」；根据掌握情况逐步加难 |

- 编程题主战场：**力扣中国站**（简单 → 简单+ → 中等）
- 理论题：Agent **自拟**或从**牛客选择题**挑选；**不必绑当天课程**，可混入未学概念（当预习/八股）；附参考答案与「为什么」
- 牛客：仅作概念选择题补充，不作为编程题主来源

## 换新窗口时

新对话第一句可写：**「继续 AI Agent 学习，请先读 CONTEXT.md」**  
Agent 靠 `CONTEXT.md`（进度/画像）+ `notes/学习笔记.md`（每日细节）恢复上下文。
