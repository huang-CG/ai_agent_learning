# Day 41 · 结构化输出

## 这题要你做什么？（一句话）

> 用 **Pydantic 模型** 定义「报告长什么样」，再用 LangChain 的 `with_structured_output`，让模型输出**直接变成可校验的对象**（不是先 `json.loads` 再手搓）。

```
D38：靠 Prompt + Few-shot 逼 JSON，再用 json.loads（可能键名飘、类型错）
D41：先定义 Schema（Pydantic）→ 框架按 Schema 要结构化结果 → 校验失败会报错
```

路径：

- 今日说明：`exercises/day41/README.md`
- 代码骨架：`exercises/day41/structured_lab.py`

---

## 和前后天的关系

| 天 | 停在哪 |
|----|--------|
| D38 | Prompt 约束 JSON + 手写解析 |
| D40 | MCP 概念（协议层） |
| **D41** | **Schema 驱动**：输出必须过 Pydantic |
| D42–D43 | 中型项目（文档助手）会用到「稳定结构」 |

不必挂工具。DeepSeek 照旧。环境里一般已有 `pydantic`；若缺：`pip install pydantic`。

---

## 验收

1. 定义至少一个 `BaseModel`（如客服报告：`label` / `reason` / `priority`）  
2. `llm.with_structured_output(YourModel, method="function_calling")`（DeepSeek 兼容优先用 **function_calling**）  
3. 对 ≥2 句用户话 `invoke`，得到的是 **Pydantic 实例**（能 `.label` / `model_dump()`），不是裸字符串  
4. 故意造一个**校验失败**的例子（如 `priority` 必须是 1–3，却传非法值），能口述 / 打印 `ValidationError`  
5. 能口述：D38 的 `json.loads` 和今天差在哪  

时间不够：砍「失败例子手写」；**不砍**「structured 成功拿到 Pydantic 对象」。

建议字段（可改，但要写清约束）：

| 字段 | 类型 | 约束 |
|------|------|------|
| `label` | `str` | 只能是 `闲聊` / `投诉` / `咨询` |
| `reason` | `str` | 一句理由 |
| `priority` | `int` | 1～3（1 低，3 高） |

---

## 跑法

```powershell
.\venv\Scripts\python.exe exercises\day41\structured_lab.py
```

若 `json_schema` 报不支持，改回骨架里的 `method="function_calling"`。

---

## 今日时间盒（约 3h）

| 段 | 时长 | 内容 |
|----|------|------|
| A | ~20min | 口述：D38 vs D41；Pydantic 是什么 |
| B | ~90min | 填骨架：模型 + structured + 两问验收 |
| C | ~25min | ValidationError 小实验 / 口述 |
| D | ~25min | 力扣 + 收工 |

实践日：先自己填；卡住约 15～20 分钟再要最小提示。
