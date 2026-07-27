# Day 26 · LangChain 入门（少脚手架）

## 这题要你做什么？（一句话）

> 自己安装 LangChain 相关包，填完骨架，用 **DeepSeek** 跑通一次「Hello」调用；并在笔记写 **手写 Agent vs LangChain** 对比（至少 3 行）。

今天 **不** 默认给完整可跑终稿。卡住约 15～20 分钟再问我最小提示。

---

## 验收

1. `hello_langchain.py` 能打印模型回复（非空）  
2. 笔记有「手写 vs LangChain」对比表（≥3 维度）  
3. 力扣 1 道（建议做）

---

## 步骤清单（按顺序做）

### 1. 安装（在 venv 里）

```powershell
cd E:\AI_agent_Quick
.\venv\Scripts\activate
pip install langchain langchain-openai python-dotenv
```

说明：DeepSeek 兼容 OpenAI 接口，用 `langchain-openai` 的 `ChatOpenAI` + 改 `base_url` 即可（不必强求 `langchain-deepseek`）。

模型名用现网可用的：`deepseek-v4-flash`（或你在 `.env` 里配的 `DEEPSEEK_MODEL`）。

### 2. 填骨架

打开 `exercises/day26/hello_langchain.py`，按 `# TODO` 补全：

- 从环境变量读 `DEEPSEEK_API_KEY`、`DEEPSEEK_BASE_URL`  
- 创建 `ChatOpenAI(...)`  
- 调用一次（`invoke`），打印 `content`

跑：

```powershell
.\venv\Scripts\python.exe exercises\day26\hello_langchain.py
```

### 3. 对比表（写进笔记）

至少填这些维度（可增删表述）：

| 维度 | 手写 ReAct（D21–25） | LangChain |
|------|----------------------|-----------|
| 谁写循环 | ？ | ？ |
| 调模型方式 | ？ | ？ |
| 工具/Agent | ？ | ？（今天可写「以后用框架封装」） |
| 优点 | ？ | ？ |
| 缺点 | ？ | ？ |

### 4. 力扣

见对话里给的链接。

---

## 建议 2.5h 节奏

| 时段 | 内容 |
|------|------|
| 0:00–0:20 | 读本 README；安装包 |
| 0:20–1:20 | 填骨架、跑通 Hello |
| 1:20–2:00 | 写对比表 |
| 2:00–2:25 | 力扣 |
| 2:25–2:30 | 「今日完成」 |

---

## 和前后天

| 天 | 关系 |
|----|------|
| D21–25 | 手写 ReAct，你知道轮子长什么样 |
| **D26** | 换框架调通 LLM（Hello） |
| D27 | 用 LangChain **重写**天气 Agent（明天再做） |

---

## 提示边界（我默认不越界）

- ❌ 不直接贴完整无 TODO 的终稿  
- ✅ 可问：报错全文、某个 TODO 该用哪个参数名、对比表某一格怎么写  
- 卡 >15～20 分钟：说「要最小提示」
