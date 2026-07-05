# AI Agent Learning

90 天 AI Agent 工程师学习仓库 · [GitHub](https://github.com/huang-CG/ai_agent_learning)

Python + LangChain/LangGraph · 目标岗位：AI Agent / AI 应用开发

---

## 环境

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
copy .env.example .env   # 填入 DeepSeek API Key
```

---

## 项目结构

```
AI_agent_Quick/
├── exercises/          # 每日练习（按 dayXX 分目录）
├── notes/              # 学习笔记
├── scripts/            # 工具脚本
├── CONTEXT.md          # 学习进度快照（Agent 上下文）
├── LEARNING_PLAN.md    # 90 天日计划
├── requirements.txt
├── .env.example        # API Key 模板（可提交）
└── .gitignore          # 忽略 venv、.env、密钥等
```

> `.env` 含 API Key，**切勿提交**；已在 `.gitignore` 中排除。

---

## 练习运行

激活 venv 后，在项目根目录执行：

| Day | 练习 | 命令 |
|-----|------|------|
| 2 | 命令行计算器 | `python exercises/day02/calculator.py` |
| 3 | 通讯录（JSON 持久化） | `python exercises/day03/address_book.py` |
| 4 | 天气 API | `python exercises/day04/weather.py` |

---

## 进度

| Day | 日期 | 主题 | 状态 |
|-----|------|------|------|
| 1 | 2026-07-01 | 环境 + AI 认知 + Git 首次 commit | ✅ |
| 2 | 2026-07-02 | Python 语法（一）· 计算器 | ✅ |
| 3 | 2026-07-03 | Python 语法（二）· 通讯录 | ✅ |
| 4 | 2026-07-04 | Python 进阶 · 天气 API | ✅ |
| 5 | 2026-07-05 | Git 与项目结构 · 推送 GitHub | ✅ |
| 6 | — | 面向对象 · OOP 通讯录 | ⬜ |

**当前阶段**：Phase 0（D5/7）· 下一步：D6 面向对象
