# AI Agent 学习上下文（Agent 用）

> 极简进度文档，供每日对话快速恢复上下文  
> 最后更新：2026-08-25 | 状态：**D42 ✅ → 下次 D43（文档助手 CLI 完善）**

---

## 学员 profile

| 键 | 值 |
|---|---|
| 目标 | **AI Agent / AI 应用岗**（求职向） |
| 城市 | **广州**（可投深圳 remote/hybrid） |
| 学习模式 | **非全职**（日均 2–4h） |
| 岗位范围 | 纯 Agent 岗 + **AI 应用 / Python+LLM 岗均可** |
| 基础 | 零基础 |
| 计划周期 | 90 天为**节奏锚点**（可按实际进度拉长；D1=2026-07-01） |
| 技术栈 | Python + LangChain/LangGraph |
| API | **DeepSeek** ✅ |
| VIP | ✅（Phase 6 → yu-ai-agent） |
| 环境 | Python 3.14.6 / Git 2.54 / venv ✅ |
| 执行力 | 高 |

---

## 当前状态

```
Day:    42 / 90 ✅
Phase:  3（进行中）
Next:   D43（智能文档助手 · CLI 完善）
```

### 复盘日程（Agent 维护 · 2026-08-25）

| 类型 | 周期 | 时长 | 期间 | 封顶 | 下次触发 | 状态 |
|------|------|------|------|------|----------|------|
| **周复盘** | 每 **7 个学习日** | 固定 2 天 | 暂停每日新课 | 最多 2 天 | D42 起计 **1/7** | ✅ 第 2 次完成（D35–D41） |
| **阶段复盘** | 每 **Phase 通关** | 固定 3 天（含 Day1 摸底） | 暂停每日新课 | 最多 3 天 | Phase 3 通关后 | ✅ Phase 2 已完成 |

> Agent 在新窗口读 CONTEXT 时须先看上表：到期则提醒进入复盘，不默认开新课。

---

## 阶段 checkpoint

| Ph | 范围 | 状态 | 通关标准 |
|---|---|---|---|
| 0 | D1–7 | ✅ 7/7 | Python + 首次 API 调用 |
| 1 | D8–17 | ✅ 10/10 | Prompt 实验 + Function Calling |
| 2 | D18–27 | ✅ 10/10 | 手写 ReAct + LangChain 重写 |
| 3 | D28–47 | 🔄 15/20 | RAG Agent + Web UI |
| 4 | D48–57 | ⬜ | LangGraph 多 Agent |
| 5 | D58–67 | ⬜ | FastAPI 部署 + Docker |
| 6 | D68–82 | ⬜ | 毕业综合项目 |
| 7 | D83–90 | ⬜ | 简历 + 面试 ready |

---

## 每日 log（倒序，最新在上）

| Day | 日期 | 时长 | 完成摘要 | 问题 | 自评 | Agent |
|-----|------|------|----------|------|------|-------|
| D42 | 2026-08-25 | 约3h | 三工具文档助手✅；吉祥物/新闻/memo轨迹含tool✅；算术不调工具✅；167双指针✅ | 口述曾把读文件说成SQL；IndentationError；web_search超时有降级 | 4 | 4 |
| D41 | 2026-08-21 | 约3h | Pydantic+with_structured_output✅；两问TicketReport✅；ValidationError✅；392双指针✅；理论C/B | Literal未导入；v4-flash思考模式拒tool_choice；对象/继承需讲 | 3 | 3 |
| D40 | 2026-08-20 | 约3h | MCP概念+FC对比表✅；Host/Client/Server✅；口头三问✅；344 reverse✅；理论B/A | 对比表曾写「MCP包含FC」；344 print(reverse)得None | 4 | 4 |
| D39 | 2026-08-18 | 约3h | LangSmith注册US+tracing✅；成功四层trace✅；失败停工具层ValueError✅；70滚动AC；理论A/B | 失败初判成参数错；key_ok未定义；build_agent缩进返回None；三ask同try跳过第三问；Docker镜像/容器说反 | 4 | 4 |
| D38 | 2026-08-17 | 约3h | 弱/强system prompt+JSON Few-shot✅；强版label/reason稳定✅；14两种写法已记；理论D/B | Few-shot曾把用户句塞进JSON；ask又用[]; 14提早return/or顺序/for-elif | 3 | 3 |
| D37 | 2026-08-16 | 约3h | 文件沙箱三工具✅；resolve+relative_to拒逃出✅；Agent总结note.txt✅；58从右扫✅；理论C/A | list_dir须return勿只print；路径esercises笔误；力扣s[-1]需i>0放and最前 | 4 | 4 |
| D36 | 2026-08-15 | 约3h | SQLite建库+SELECT冒烟✅；run_sql只读+create_agent Text-to-SQL✅；人数4/广州2✅；125回文✅；理论B/B | execute_select误用path（应DB_PATH）；125跳过字符时越界后改先过滤 | 4 | 4 |
| D35 | 2026-08-13 | 2.5h | ddgs裸搜冒烟✅；web_search@tool+create_agent按需联网✅；新闻调tool/1+1不调✅；69二分✅；理论B/B | ask混用dict/对象（.content vs []）；二分曾l+=1后改l=mid+1、return r | 4 | 4 |
| D34 | 2026-08-10 | 约3h | RAG做成@tool+create_agent按需查库✅；吉祥物调tool/1+1不调✅；66加一✅；理论题已出 | 骨架注释误导用message[]；raise写成OpenAIEmbeddings；tool预览截断易误解 | 4 | 4 |
| D33 | 2026-08-09 | 约3h | RAG引用+拒编✅ metadata过滤✅ Hybrid口述✅；35搜索插入✅；理论题已出 | format_sources漏parts=[]；拒答仍标出处后改prompt；裸写README路径再踩坑；35初稿误用in | 4 | 4 |
| D32 | 2026-08-08 | 约3h | 完整RAG六步✅ PDF问答✅ 无答案拒编✅ chunk 200vs80对比✅；704二分✅；理论题已出 | 未保存导致跑旧文件；run_rag漏build_llm；二分初稿未缩区间 | 4 | 4 |
| D31 | 2026-08-07 | 约3h | Embed(硅基bge-m3)+向量检索top-3✅；Chroma崩改InMemoryVectorStore✅；509✅；理论B/B | Py3.14下Chroma写入崩溃；番茄炒蛋检索偏；出题未先读规则已立硬性检查 | 4 | 4 |
| D30 | 2026-08-06 | 约3h | Load+Split✅ RecursiveCharacterTextSplitter✅ 200/40→8块 vs 100/20→19块对比✅；485✅；理论题已出 | 缺文件判断写成if not text（应exists）；理论题待报 | 4 | 4 |
| D29 | 2026-08-05 | 约3h | create_agent闭环✅ messages轨迹见tool Observation✅ try/except✅；448 set查缺✅ | 体感与D27高度重合（API相同）；计划旧API名已澄清用create_agent | 4 | 4 |
| D28 | 2026-08-02 | 约3h | Phase3开篇：3×@tool✅ Schema打印✅ 直调✅ bind_tools选型✅；977双指针✅；力扣已做清单✅ | 开场口述主信号偏；docstring与签名曾不一致（已修）；误出136已建防重 | 4 | 4 |
| D27 | 2026-07-28 | 约3h | LangChain 天气 Agent✅（天气/计算验收）README✅；进入 Phase 2 复盘 Day1✅ | 框架细节与安全点记忆断点；阶段口述偏弱 | 3 | 3 |
| D26 | 2026-07-27 | 2.5h | LangChain Hello✅ 对比表✅ 414第三大数✅ 少脚手架实践✅ | 理论题0/2；概念映射先懵后通 | 4 | 4 |
| D25 | 2026-07-26 | 2h | 结构化日志✅ 评测10/10✅ 口述调试✅ 268 set/求和/异或✅ 协作改少脚手架✅ | deepseek-chat失效改v4-flash；脚手架过重独立实现弱 | 4 | 3 |
| D24 | 2026-07-25 | 2.5h | 三架构概念✅ 对比表自写验收✅ 169 Counter✅ 理论题1/2 | dict键不可list；P&E并行/实时调整表述需微调 | 4 | 4 |
| D23 | 2026-07-24 | 2.5h | 短期记忆ReAct✅ 记名字验收✅ 三层记忆口述✅ 387 Counter/dict/enumerate✅ 解析容错**Final Answer**✅ | 模型Markdown粗体导致解析失败（已修） | 5 | 4 |
| D22 | 2026-07-23 | 2.5h | 真天气ReAct✅ 北京天气验收✅ Observation口述✅ 383 Counter✅ 理论题归档补解析✅ | Counter<=版本差异；力扣耗时波动 | 4 | 4 |
| D21 | 2026-07-22 | 2h | ReAct主循环✅ 正则解析✅ max_steps实测✅ 口述循环✅ 242 Counter/sorted✅ | parse_action嵌套括号截断需修；Counter误用.sort | 4 | 4 |
| D20 | 2026-07-21 | 2.5h | 工具Schema三字段✅ GOOD/BAD对照✅ 口头4题3对✅ 350 Counter✅ 理论题归档✅ | 传参格式归属需点拨；开场自拟题已纠正+立红线 | 4 | 4 |
| D19 | 2026-07-20 | 3h | ReAct三台词✅ 手写2轮示例✅ 对齐FC✅ 349双set✅ | 349先list查找需点拨；AC等术语初学 | 4 | 4 |
| D18 | 2026-07-19 | 3h | Agent定义✅ 四步循环✅ vs Chatbot表✅ 136五种解法笔记✅ | O(n)/O(1)题意需讲；异或待消化 | 4 | 4 |
| D17 | 2026-07-18 | 3h | 拼Prompt QA✅ 对比RAG✅ Phase1复盘✅ 26双指针✅ | 先问del/remove再写双指针 | 5 | 4 |
| D16 | 2026-07-17 | 3h | RAG概念✅ Dify零代码✅ 开/关知识库对比✅ 验收口述✅ | Dify配置乱；缺Embedding；模板OpenAI；力扣26顺延 | 4 | 4 |
| D15 | 2026-07-16 | 3h | FC实战tool_chat✅ 时间+计算器✅ 多轮循环修复✅ 27移除✅ | 单轮bug需排查；模型偶编时间；终端重绘 | 4 | 4 |
| D14 | 2026-07-14 | 3h | FC原理✅ 流程图✅ Schema三角✅ 88合并✅ | 88下标/m·n/越界需讲；文档示例易混 | 4 | 4 |
| D13 | 2026-07-13 | 3h | 4原则✅ A/B/C对比✅ 选B✅ 改C✅ 283双指针✅ | range/len混淆；283需提示 | 3 | 4 |
| D12 | 2026-07-12 | 3h | 多轮✅ history_chat✅ trim✅ 121股票✅ 流程图✅ | 代码靠注释；min/max初学 | 4 | 4 |
| D11 | 2026-07-11 | 3h | 流式✅ 四参数✅ max_tokens实验✅ 217 set✅ | 代码初读吃力；list超时 | 4 | 4 |
| D10 | 2026-07-10 | 3h | CoT对比✅ cot_lab✅ 鸡兔同笼✅ 有效括号✅ | 括号题循环内过早return；False大小写 | 4 | 4 |
| D9 | 2026-07-09 | 2h | 5种Prompt✅ system/user✅ prompt_lab✅ 两数之和暴力✅ | range/!语法；示例3用i!=j；Few-shot延后 | 4 | 4 |
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

**D9**：`system`/`user` Prompt；5 种任务模板；格式约束 vs `temperature`；`prompt_lab.py`

**D10**：CoT 逐步推理；普通 vs CoT 对比；CoT + 格式约束；栈（有效括号）；`enumerate`；dict 一遍解（两数之和）

**D11**：API 参数 top_p/max_tokens/stop；流式 SSE/`[DONE]`/`delta.content`；`stream_chat.py`；set vs list（217）；O(n) vs O(n²)

**D12**：messages 多轮历史；`append` user/assistant；`trim_history`；`history_chat.py`；121 一次遍历

**D13**：System Prompt 四原则（角色/边界/格式/拒绝）；A/B/C 对比选优；`system_prompt_lab.py`；283 双指针挤非 0

**D14**：Function Calling 流程；tools/parameters(JSON Schema)/arguments；`role:tool`；`finish_reason` stop vs tool_calls；88 从后往前合并

**D15**：Function Calling 实战 `tool_chat.py`；多工具自动选择；`json.loads(arguments)`+`run_tool`；多轮 tool_calls 循环；列表引用原地改（27）

**D16**：RAG 概念（Embedding/向量/余弦/top-k）；Dify 知识库+Chatflow 零代码；开/关知识库对比降幻觉；硅基流动 Embedding

**D17**：拼 Prompt 知识库 QA（`kb_qa.py`）；拼 Prompt vs RAG 对比；Phase 1 复盘；力扣 26 双指针

**D18**：Agent 定义（感知-推理-决策-执行循环）；Agent vs Chatbot；力扣 136（字典/Counter/set/异或）

**D19**：ReAct 三台词（Thought/Action/Observation→Final Answer）；手写 2 轮示例；与 FC 同构；力扣 349 双 set 交集

**D20**：工具 Schema 三字段（`name`/`description`/`parameters`）；描述质量决定调用准确率（何时调→function.description，怎么传→参数 description）；GOOD vs BAD 对照；力扣 350 交集 II（Counter 取 min / 排序双指针 / 手动字典）；理论题归档到 `notes/理论题归档.md`

**D21**：手写 ReAct 主循环（`run_react` + scratchpad）；正则解析 Thought/Action/Final Answer；`simulate_tool` 假 Observation；`max_steps` 防死循环；力扣 242（Counter / sorted）

**D22**：真天气 ReAct（`run_tool` + wttr.in）；Observation 来自 JSON；关键路径 D22 打通；力扣 383 赎金信（Counter）

**D23**：Agent 短期记忆（对话历史 + trim）；scratchpad vs 历史 vs 向量库概念；ReAct 记住用户名字；解析容忍 Markdown；力扣 387（Counter / dict / enumerate）

**D24**：ReAct / Plan-and-Execute / Reflection 三种架构；自写对比表验收；力扣 169（Counter 多数元素）

**D25**：Agent 调试日志 + 10 题评测（100%）；DeepSeek 模型名切 v4-flash；力扣 268；确认少脚手架/顺延债务/90天弹性

**D26**：LangChain 入门（ChatOpenAI + invoke）跑通 DeepSeek；手写 ReAct vs LangChain 对比；力扣 414

**D27**：LangChain `create_agent` 重写天气 Agent；`@tool` + 流式；Phase 2 通关

**D28**：LangChain Tools 专题；`@tool`→Schema→`invoke`→`bind_tools`/`tool_calls`；厘清与 `create_agent` 差在「谁执行 Observation」；力扣 977；新建 `notes/力扣已做.md`

**D29**：`create_agent` 组装闭环（时间+温度工具）；`messages` 轨迹见 `tool` Observation；try/except；力扣 448；学员反馈与 D27 API 重合（计划旧名已澄清）

**D30**：文档 Load + Split；`RecursiveCharacterTextSplitter`；chunk_size/overlap 对比实验；力扣 485

**D31**：硅基流动 Embedding（`OpenAIEmbeddings` 兼容接口）+ `InMemoryVectorStore` 检索 top-3；Chroma 在 Py3.14/Win 崩溃已绕过；力扣 509

**D32**：完整 RAG（PDF Load→…→Generate）；与 D17 差别在 Retrieve；chunk_size 影响检索粒度；力扣 704 二分 / O(log n)

**D33**：RAG 引用（source/chunk_id）+ 拒编；metadata 过滤；Hybrid Search 概念；力扣 35 插入位置

**D34**：RAG 检索做成 `@tool` + `create_agent` 按需调用；力扣 66 加一 / 从右往左进位

**D35**：`ddgs` 真搜索 + `@tool web_search` + `create_agent` 按需联网；RAG vs 搜索选型；力扣 69 二分求平方根 / 退出返回 `r`

**D36**：SQLite + Text-to-SQL（`run_sql` 只允许 SELECT）+ `SCHEMA_HINT`；RAG/搜索/SQL 选型；力扣 125 回文 / 先滤再双指针

**D37**：文件工具沙箱（`safe_path` + list/read/write）；`Path /` 拼接与 `resolve`；力扣 58 从右扫最后一个单词 / `i>0` 防 `s[-1]`

**D38**：Agent system prompt + Few-shot + JSON 字段约束；弱版能 loads 但键名不稳；力扣 14 边扫边缩短前缀

**D39**：LangSmith tracing（`LANGSMITH_*` env，选 US）；成功 Trace 四层；失败=工具 raise 不是参数错；力扣 70 爬楼梯 / 与 509 同递推

**D40**：MCP = Model Context Protocol；与 FC 不同层不替代；Host/Client/Server；单 App 优先 `@tool`；力扣 344 `reverse` 返回 None

**D41**：Pydantic `BaseModel` + `with_structured_output`；继承≠传业务参；思考模式慎用 tool_choice；力扣 392 子序列双指针

**D42**：智能文档助手 CLI 雏形；RAG + web_search + 沙箱读文件三工具同一 Agent；InMemory 替代 Chroma；力扣 167 有序双指针

**薄弱点（持续）**：语法结构；力扣多指针下标；读官方示例易和第三方混淆；交互脚本建议外部 PowerShell 跑（Cursor 终端重绘 bug）；低代码平台（Dify）首次配置易绕；异或等位运算需再练；**OOP 继承 / 对象 vs 类** 需多对照例子；走读时易把**注释当实现**（如 SQL `startswith` 大小写）；工具选型口述偶混（读文件≠SQL）

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
| 2026-07-09 | **D9 完成**，自评 4 / Agent 4；Prompt 5 模板 + 两数之和 |
| 2026-07-10 | **D10 完成**，自评 4 / Agent 4；CoT + 有效括号；笔记流程：写前向学员要感悟 |
| 2026-07-11 | **D11 完成**，自评 4 / Agent 4；流式 + set；练习代码加中文注释 |
| 2026-07-12 | **D12 完成**，自评 4 / Agent 4；多轮 messages + 121；流程图 `notes/diagrams/` |
| 2026-07-12 | 理论题规则：Agent **随机出**，学过/未学均可；零碎自测，非必修 |
| 2026-07-13 | **D13 完成**，自评 3 / Agent 4；System Prompt A/B/C 选 B + 283 移动零 |
| 2026-07-14 | **D14 完成**，自评 4 / Agent 4；FC 原理+流程图+88；结束补理论题 |
| 2026-07-16 | Cursor 终端拖动重绘 bug：外部 PS 正常；设置 `windowsUseConptyDll: true`；`gpuAcceleration: auto`（off 会卡） |
| 2026-07-16 | **D15 完成**，自评 4 / Agent 4；FC 实战 tool_chat（时间+计算器）+ 27 移除元素 |
| 2026-07-17 | **D16 完成**，自评 4 / Agent 4；RAG 概念 + Dify 零代码；力扣 26 顺延 D17 |
| 2026-07-18 | **D17 完成**，自评 5 / Agent 4；拼 Prompt QA + Phase 1 通关；力扣 26 |
| 2026-07-19 | **D18 完成**，自评 4 / Agent 4；Agent 定义 + vs Chatbot；力扣 136 |
| 2026-07-20 | **D19 完成**，自评 4 / Agent 4；ReAct 手写示例 + 力扣 349 |
| 2026-07-21 | **D20 完成**，自评 4 / Agent 4；工具 Schema 三字段 + 力扣 350；新建 `notes/理论题归档.md` + 立「禁止自拟题」红线 |
| 2026-07-22 | **D21 完成**，自评 4 / Agent 4；手写 ReAct 主循环 + max_steps 实测；力扣 242 |
| 2026-07-23 | **D22 完成**，自评 4 / Agent 4；真天气 ReAct + 力扣 383；理论题归档补全逐选项解析 |
| 2026-07-24 | **D23 完成**，自评 5 / Agent 4；短期记忆 ReAct + 记名字；力扣 387；解析容错 Markdown |
| 2026-07-25 | **D24 完成**，自评 4 / Agent 4；三架构对比表自写；力扣 169 |
| 2026-07-26 | **D25 完成**，自评 4 / Agent 3；调试评测 10/10；模型名迁移；确认少脚手架等协作规则 |
| 2026-07-27 | **D26 完成**，自评 4 / Agent 4；LangChain Hello 跑通；414 与对比表完成 |
| 2026-07-28 | **D27 完成**，自评 3 / Agent 3；LangChain 重写天气 Agent 跑通；确认进入 Phase 2 复盘 |
| 2026-07-29 | **复盘规则定稿**：周复盘固定 2 天（Day1 摸底+计划，Day2 执行）；阶段复盘固定 3 天（Day1 摸底+计划，Day2/Day3 执行）；按每日可用时长动态裁剪 |
| 2026-08-02 | **D28 完成**，自评 4 / Agent 4；Phase 3 开篇；新建 `notes/力扣已做.md`（出题前必查） |
| 2026-08-05 | **D29 完成**，自评 4 / Agent 4；create_agent 闭环 + messages 轨迹；力扣 448 |
| 2026-08-06 | **D30 完成**，自评 4 / Agent 4；文档切块统计与参数对比；力扣 485 |
| 2026-08-07 | **D31 完成**，自评 4 / Agent 4；Embedding + 向量检索；Chroma 环境崩改内存库；力扣 509 |
| 2026-08-15 | **D36 完成**，自评 4 / Agent 4；SQL Agent Text-to-SQL；力扣 125；周复盘计数 **2/7** |
| 2026-08-13 | **D35 完成**，自评 4 / Agent 4；ddgs + web_search Agent；力扣 69；周复盘计数 **1/7** |
| 2026-08-12 | **第 1 次周复盘完成**（D28–D34）：知识清单+错题表+小改造；归档 `notes/复盘归档.md` |
| 2026-08-10 | **D34 完成**，自评 4 / Agent 4；RAG+Agent 按需检索；力扣 66；**周复盘触发（7/7）** |
| 2026-08-09 | **D33 完成**，自评 4 / Agent 4；RAG 引用/拒编/metadata；力扣 35 |
| 2026-08-25 | **D42 完成**，自评 4 / Agent 4；三工具文档助手 CLI 雏形；力扣 167；周复盘计数 **1/7** |
| 2026-08-24 | **第 2 次周复盘完成**（D35–D41）：知识清单+错题表+小改造（day38 键名检查）；归档 `notes/复盘归档.md`；下次新课 **D42** |
| 2026-08-22 | **周复盘第 2 次 Day1**（D35–D41）：12 问摸底 + 知识清单草稿；小改造顺延 Day2 |
| 2026-08-21 | **D41 完成**，自评 3 / Agent 3；Pydantic structured output；力扣 392；**周复盘计数 7/7 → 下次进周复盘** |
| 2026-08-20 | **D40 完成**，自评 4 / Agent 4；MCP vs FC 对比表；力扣 344；周复盘计数 **6/7** |
| 2026-08-18 | **D39 完成**，自评 4 / Agent 4；LangSmith 完整 trace + 失败层分析；力扣 70；周复盘计数 **5/7** |
| 2026-08-17 | **D38 完成**，自评 3 / Agent 3；JSON Few-shot 格式稳定；力扣 14 耗时长；周复盘计数 **4/7** |
| 2026-08-16 | **D37 完成**，自评 4 / Agent 4；文件沙箱工具；力扣 58；周复盘计数 **3/7** |
| 2026-08-16 | 理论题正确项打散：禁止习惯性 B/B，同日两题不要同一字母 |
| 2026-08-09 | 理论题出题后**不要**再提示「答完报 B / B 这种格式」 |
| 2026-08-08 | 出题纪律再强调：每次出理论题/力扣前必须先读 CONTEXT「每日刷题」+ 理论题「协作约定」；禁止不读规则就出题、禁止理论题默认绑当天课 |
| 2026-08-02 | 新建 `notes/力扣已做.md`；约定出题前必查，禁止重复已做题号 |
| 2026-07-29 | **Phase 2 复盘 Day1 完成**：60 分钟口述摸底 + 复盘计划落地到 `notes/复盘归档.md` |
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
| `notes/理论题归档.md` | 历日理论题全文（题干/选项/答案） |
| `notes/力扣已做.md` | 力扣已做题号清单（**出题前必查，防重复**） |
| `notes/复盘归档.md` | 周复盘 / 阶段复盘过程归档（摸底·执行·踩坑·结论） |
| `CONTEXT.md` | 本文件 |
| `exercises/day02/calculator.py` | D2 计算器 |
| `exercises/day03/address_book.py` | D3 通讯录 |
| `exercises/day04/weather.py` | D4 天气 API |
| `exercises/day06/address_book_oop.py` | D6 OOP 通讯录 |
| `exercises/day07/chat.py` | D7 命令行 AI 问答 |
| `exercises/day09/prompt_lab.py` | D9 Prompt 实验 |
| `exercises/day10/cot_lab.py` | D10 CoT 对比实验 |
| `exercises/day11/stream_chat.py` | D11 流式 CLI |
| `exercises/day12/history_chat.py` | D12 多轮对话 |
| `exercises/day13/system_prompt_lab.py` | D13 System Prompt 三版对比 |
| `exercises/day14/tools_schema_demo.py` | D14 FC 结构演示 |
| `exercises/day15/tool_chat.py` | D15 FC 实战（时间+计算器） |
| `exercises/day16/README.md` | D16 RAG 概念 + Dify 步骤 |
| `exercises/day20/tool_schemas.py` | D20 工具 Schema（GOOD/BAD 对照） |
| `exercises/day21/react_agent.py` | D21 手写 ReAct 主循环（模拟工具） |
| `exercises/day22/react_weather_agent.py` | D22 真天气 ReAct Agent |
| `exercises/day23/react_memory_agent.py` | D23 带短期记忆的 ReAct Agent |
| `exercises/day24/README.md` | D24 三架构概念 + 验收说明 |
| `exercises/day25/react_debug_agent.py` | D25 结构化日志 ReAct |
| `exercises/day25/run_eval.py` | D25 10 题工具选择评测 |
| `exercises/day28/tools_lab.py` | D28 LangChain Tools 实验 |
| `exercises/day28/README.md` | D28 验收与时间盒 |
| `exercises/day29/agent_lab.py` | D29 LangChain Agent 组装 |
| `exercises/day29/README.md` | D29 验收与时间盒 |
| `exercises/day30/split_lab.py` | D30 文档加载与切块 |
| `exercises/day30/sample_doc.md` | D30 切块样例文档 |
| `exercises/day30/README.md` | D30 验收与时间盒 |
| `exercises/day31/vector_lab.py` | D31 Embedding + 向量检索（InMemory） |
| `exercises/day31/README.md` | D31 验收与环境说明 |
| `exercises/day32/rag_lab.py` | D32 完整 RAG 管道（关键路径） |
| `exercises/day32/sample_kb.pdf` | D32 样例 PDF 知识库 |
| `exercises/day32/README.md` | D32 验收与时间盒 |
| `exercises/day33/rag_cite_lab.py` | D33 RAG 引用 / 拒编 / metadata 过滤 |
| `exercises/day33/README.md` | D33 验收与时间盒 |
| `exercises/day34/rag_agent_lab.py` | D34 RAG 检索做成 Agent 工具 |
| `exercises/day34/README.md` | D34 验收与时间盒 |
| `exercises/day35/search_agent_lab.py` | D35 web_search Agent（ddgs） |
| `exercises/day35/README.md` | D35 验收与时间盒 |
| `exercises/day36/sql_agent_lab.py` | D36 SQL Agent（Text-to-SQL） |
| `exercises/day36/README.md` | D36 验收与时间盒 |
| `exercises/day37/file_agent_lab.py` | D37 文件工具（沙箱） |
| `exercises/day37/README.md` | D37 验收与时间盒 |
| `exercises/day38/prompt_agent_lab.py` | D38 Prompt + JSON Few-shot Agent |
| `exercises/day38/README.md` | D38 验收与时间盒 |
| `exercises/day39/tracing_lab.py` | D39 LangSmith tracing Agent |
| `exercises/day39/README.md` | D39 验收与时间盒 |
| `exercises/day40/README.md` | D40 MCP 概念与 FC 对比 |
| `exercises/day41/structured_lab.py` | D41 Pydantic structured output |
| `exercises/day41/README.md` | D41 验收与时间盒 |
| `exercises/day42/doc_assistant.py` | D42 智能文档助手（三工具 CLI 雏形） |
| `exercises/day42/README.md` | D42 验收与时间盒 |
| `exercises/day42/sandbox/memo.txt` | D42 沙箱样例备忘 |
| `notes/diagrams/day24-agent-architectures.md` | D24 三架构流程图 |
| `exercises/day16/sample_kb.md` | D16 知识库样例 |
| `exercises/day17/kb_qa.py` | D17 拼 Prompt 知识库 QA |
| `exercises/day17/knowledge.md` | D17 知识库文档 |
| `exercises/day18/README.md` | D18 Agent 概念 |
| `exercises/day19/README.md` | D19 ReAct 格式 + 作业 |
| `notes/diagrams/day12-messages-flow.md` | D12 messages 流程图 |
| `notes/diagrams/day14-function-calling-flow.md` | D14 Function Calling 流程图 |
| `notes/diagrams/day16-rag-flow.md` | D16 RAG 流程图 |
| `notes/diagrams/day18-agent-loop.md` | D18 Agent 循环图 |
| `notes/diagrams/day19-react-loop.md` | D19 ReAct 循环图 |
| GitHub `huang-CG/ai_agent_learning` | D5 远程仓库 |

---

## 每日协作流程

```
早上：报「今天 X 小时，Day N 开始」
晚上：报「今日学习完成」+ 自评 → Agent 向学员要感悟 → 更新两文档 + Agent 客观评分
      → 提醒 git 提交（需学员明确说「提交/commit」才执行；需 push 再说「push」）
```

### 实践日交付模式（D26 起默认 · 2026-07-26 学员确认）

为提高独立实现能力，实践日默认：

1. **步骤清单 + 最小骨架**（函数签名/TODO），不默认给完整可跑实现  
2. **学员先写**；卡住约 **15～20 分钟**再要最小提示  
3. **验收**除跑通外，看「学员改过/写过哪些」  
4. **时间不够：砍范围，不砍动手**（少题量/少花活，保留自写段）  
5. 学员某天特别赶，可临时说「今天可以多给脚手架」

概念日（对比表/口述）仍可少代码；关键路径日可在骨架上略厚，但仍避免「一次交全套终稿」。

### 当天完不成 / 顺延（防债务堆积 · 2026-07-26）

1. **先保关键路径最小验收**；其余显式标「未完成/顺延」，不假装 ✅  
2. **债务最多约 1 天**：再欠则停开新 Day，先补关键缺口（先补后进）  
3. **非关键可丢不进债**：拓展、选读、第二道力扣等  
4. 太难则 **拆成两天**（同主题 Dxxa/Dxxb），不堆一长串半截任务  
5. 卡住 >20 分钟可要最小提示；收工写清卡点与明日先补什么  

### 计划弹性（2026-07-26 确认）

- **90 天是节奏锚点，不是死线**；按实际消化速度规划，可整体后移  
- **不可跳过的是关键路径**（见下节），不是日历上的 Day 编号  
- 求职预期仍参考：能投递 ≠ 当天 offer；offer 更现实约 2026 年底～2027 年初（非全职）

### 周复盘 / 阶段复盘（2026-07-29 规则升级）

**触发**

- **周复盘**：每完成 **7 个学习日** 进行 1 次（见上表「复盘日程」）
- **阶段复盘**：每个 **Phase 通关** 进行 1 次（D7/D17/D27/D47…）

**时长与暂停（默认模板）**

- 周复盘：**固定 2 天**（特殊情况可临时调整），期间**暂停每日新课**
  - Day 1：Agent 提问摸底 + 制定复盘计划
  - Day 2：按计划复盘
- 阶段复盘：**固定 3 天（含 Day 1 摸底）**（特殊情况可临时调整），期间**暂停每日新课**
  - Day 1：Agent 提问摸底 + 制定复盘计划
  - Day 2：按计划复盘
  - Day 3：按计划复盘
- 每天开场由学员先报可用时长；Agent 结合当日时长动态调整任务颗粒度

**流程（Agent 主导）**

1. **复盘 Day 1 摸底**（按时间，不按题数；**简答/口述**，不用选择题）
   - 周复盘：**30 分钟**
   - 阶段复盘：**60 分钟**（可分两段各 30 分钟）
   - Agent 通过提问摸清掌握情况；学员**不必先自评**薄弱点
2. Agent 根据摸底结果**制定当次复盘计划**（按当天可用时长拆任务）
3. 复盘 Day 2/Day 3 按计划带练（概念追问 / 代码走读 / 小实战改造）
   - 说明：总天数是「Day1 摸底 + Day2/Day3 执行」，不是 Day1 后再额外加 3 天
4. 结束后给出复盘结论 + 更新本文件「复盘日程」表；**过程写入 `notes/复盘归档.md`**（分「周复盘记录」「阶段复盘记录」两栏追加，含摸底要点、执行过程、踩坑、交付物）

**交付物（必须有，防空转）**

| 类型 | 必交付 |
|------|--------|
| 周复盘 | 当周知识清单 + 错题清单 + **1 个小改造**（改旧代码，不新开大题） |
| 阶段复盘 | 阶段能力清单 + 项目口述稿 + **1 个综合小练习** |

**复盘天规则**：每天至少有一段动手代码，不能只看笔记。  
**复盘不评分**（2026-08-01 确认）：复盘日不做学员自评 / Agent 评分；收工只更新复盘归档与进度即可。

---

### 每日刷题（D7 起，学员确认 2026-07-08）

> **Agent 硬性检查（2026-08-08 学员再次强调）**  
> 每次出**理论题**或**力扣**之前，必须先完整读完本小节规则 + `notes/理论题归档.md`「协作约定」（力扣另查 `notes/力扣已做.md`），**读完再出题**。  
> 禁止不读规则就出题；禁止默认绑死当天课程（理论题须随机，可学过/未学）。多次违规已提醒，不得再犯。

| 类型 | 数量 | 时机 | 规则 |
|------|------|------|------|
| **力扣编程题** | 1～2 道/天 | 当日课程结束后**当场做**，贴代码给 Agent 检查 | 从「简单」起步，根据完成情况**循序渐进**加难度 |
| **理论选择题** | 1～2 道/天 | **零碎时间**自己做，像八股/概念自测 | Agent **随机出**；学过的/没学过的均可；附参考答案与「为什么」 |

- 编程题主战场：**力扣中国站**（简单 → 简单+ → 中等）
- **力扣出题前必查** `notes/力扣已做.md`，**禁止重复已做题号**；收工同步追加新题
- 理论题：Agent **随机自拟**（或牛客挑选）；**不必绑当天课程**；**学过的 + 未学的**都可出（复习/八股/预习）；附参考答案与「为什么」；**参考答案须写清为何选该项、为何不选其他选项**；**不做不算当天未完成**
- **正确项打散（2026-08-16）**：同一天两题不要都是同一字母（禁止习惯性 B/B）；先定知识点再排选项
- **出题前必读**：本段 + `notes/理论题归档.md`「协作约定」；对话中须贴完整题干+选项
- 牛客：仅作概念选择题补充，不作为编程题主来源
- **理论题批改红线（2026-07-21）**：学员只报「选 C/B」而本对话无题面时 → 先查 `notes/理论题归档.md` / 历史 transcript；**禁止另编一套题假装批改**；找不到就明说并请贴题/截图。出题后须同步写入归档。

## 换新窗口时

新对话第一句可写：**「继续 AI Agent 学习，请先读 CONTEXT.md」**  
Agent 靠 `CONTEXT.md`（进度/画像）恢复；笔记/理论题归档/复盘归档**按需再读**，不必整本塞进上下文。
