# Day 27 · LangChain 重写天气 Agent（Phase 2 收官）

## 这题要你做什么？（一句话）

> 用 LangChain 的 `create_agent` 重写 D22 的天气 Agent，完成工具调用、交互运行和架构说明，作为 Phase 2 里程碑。

---

## 验收

1. `langchain_weather_agent.py` 可运行，支持连续对话  
2. 问「广州天气怎么样」能调用 `get_weather` 并给出天气回答  
3. 问「(3+5)*2 等于几」可返回正确结果（16）  
4. 能口述手写版（D22）与 LangChain 版的核心差异  

---

## 架构说明（D22 手写版 vs D27 LangChain 版）

| 维度 | D22 手写 ReAct | D27 LangChain |
|------|----------------|---------------|
| 主循环 | 自己写 `run_react` + `max_steps` | `create_agent` 内部处理循环 |
| 解析动作 | 自己写正则 `parse_react` / `parse_action` | 框架负责消息与工具调用编排 |
| 工具注册 | 手动 `run_tool` 分发 | `@tool` 装饰函数后交给 agent |
| 何时调用工具 | 主要靠长提示词约束 | 主要靠 `@tool` docstring + system prompt |
| 调试视角 | 打印 Thought/Action/Observation | 看 `result["messages"]` 中 `human/ai/tool/ai` |

一句话总结：**手写版练底层机制，LangChain 版练工程封装与可复用。**

---

## 运行方式

### 1) 环境准备（venv）

```powershell
cd E:\AI_agent_Quick
.\venv\Scripts\activate
```

确保已安装：

```powershell
pip install langchain langchain-openai python-dotenv requests
```

### 2) `.env` 最低要求

```env
DEEPSEEK_API_KEY=你的key
DEEPSEEK_BASE_URL=https://api.deepseek.com
DEEPSEEK_MODEL=deepseek-v4-flash
```

### 3) 启动

```powershell
.\venv\Scripts\python.exe exercises\day27\langchain_weather_agent.py
```

---

## 建议测试用例

1. `广州天气怎么样？`（应触发 `get_weather`）  
2. `北京现在下雨吗？`（应触发 `get_weather`）  
3. `(3+5)*2 等于几？`（可直接回答 16，或触发 `calculator` 后回答）  
4. `2**10`（受白名单控制，检查 calculator 行为）  

---

## 常见问题

1. **看起来不是流式输出？**  
   现在用的是 `agent.invoke(...)`，这是一次性返回；若要流式需改为 `agent.stream(...)`。

2. **工具不调用/调用错？**  
   先检查 `@tool` 的 docstring 是否清楚写了「何时使用、参数含义、不适用场景」。

3. **消息打印报属性错误？**  
   LangChain 消息对象通常用 `message.type`，不是 `message.role`。

---

## 与后续衔接

- D27 完成后，Phase 2（D18–27）核心能力打通：  
  **手写 Agent 机制理解 + LangChain 工程化重写**
- 进入 Phase 3 时，会继续扩展到 RAG、检索、工具组合与更强的工程结构。

