# Day 13 · System Prompt 设计 · 3 版对比

## 这题要你做什么？（一句话）

> 为同一个「Python 学习助手」写 **3 版不同的 system prompt**，用**相同测试问题**对比效果，选出最优并说明理由。

D9 学过 system/user 分工；D12 在 `history_chat.py` 里用过一句 system。今天要**认真设计** system，而不是随便写一句。

---

## System Prompt 设计原则（速记）

| 原则 | 说明 | 反例 |
|------|------|------|
| **角色清晰** | 你是谁、为谁服务 | 「你是助手」太泛 |
| **边界明确** | 能做什么、不能做什么 | 没写 → 可能瞎编、跑题 |
| **格式约束** | 回答长度、结构、语言 | 「简洁」vs「分点+示例」差很多 |
| **拒绝策略** | 超范围怎么答 | 否则可能硬答医学/法律题 |
| **稳定可测** | 同一问题多次结果接近 | temperature 太高会飘 |

记忆口诀：**角色 + 边界 + 格式 + 拒绝**

---

## 三版 Prompt 思路（你要对比的）

| 版本 | 风格 | 特点 |
|------|------|------|
| **A 极简** | 1～2 句 | 看缺什么会出问题 |
| **B 详细** | 分条写角色/范围/格式 | 日常最常用 |
| **C 结构化** | 强制输出模板（如：概念→示例→练习） | 适合教学类 Bot |

---

## 文件

| 文件 | 用途 |
|------|------|
| `system_prompt_lab.py` | 3 版 system + 4 道固定测试题，自动对比输出 |

---

## 建议学习顺序

1. 读 `system_prompt_lab.py` 里 `PROMPT_A/B/C` 三版，理解差异
2. 运行 `python exercises/day13/system_prompt_lab.py`，看 4 道题 × 3 版的输出
3. 自己改一版 Prompt（例如加强「拒绝非 Python 问题」），再跑对比
4. 笔记里写：**你选哪版？为什么？** 至少 3 条理由
5. 可选：把最优 system 贴进 `history_chat.py` 试多轮聊天

---

## 固定测试题（脚本内置）

1. `什么是列表推导式？` — 测**概念解释**是否清晰
2. `帮我写一段读取 JSON 文件的代码` — 测**代码生成**质量
3. `Python 和 Java 哪个更好？` — 测**边界/客观性**（不应站队）
4. `帮我看看这段代码有没有 bug：for i in range(10) print(i)` — 测**纠错**能力

---

## 运行

```powershell
cd e:\AI_agent_Quick
.\venv\Scripts\Activate.ps1
python exercises/day13/system_prompt_lab.py
```

只跑某一版：`python exercises/day13/system_prompt_lab.py --version B`

---

## 验收自检

- [ ] 能说出 system prompt 的 4 条设计原则
- [ ] 3 版 prompt 都跑过，看过对比输出
- [ ] 笔记里选定最优版 + **至少 3 条理由**
- [ ] 知道 system 和 user 的分工（D9 复习）
- [ ] 力扣 1 道（今日结束后）
