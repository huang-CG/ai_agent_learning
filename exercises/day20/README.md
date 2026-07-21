# Day 20 · 工具定义与描述

## 这题要你做什么？（一句话）

> 为 **天气 / 搜索 / 计算** 三个工具写出完整的 Function Calling **JSON Schema**（`name` + `description` + `parameters`），并理解：**description 写得好不好，直接决定模型会不会调对工具、传对参数**。

验收：3 个工具 Schema 完成（见 `tool_schemas.py`）。

---

## 先抓住这一句

D14 学过 FC 三角：`tools`（说明书）→ `tool_calls`（模型点菜）→ `role:tool`（厨房上菜）。

**今天只练「说明书」怎么写**——还不接真 API、不写 ReAct 循环（D21–22 再做）。

| 字段 | 写给谁 | 作用 |
|------|--------|------|
| `name` | 模型 + 你的代码 | 唯一标识；`run_tool` 靠它路由 |
| `description` | **主要是模型** | 何时该调、何时不该调 |
| `parameters` | 模型 | 传什么 JSON；`properties` 里每个字段也有 `description` |

---

## JSON Schema 最小模板

```python
{
    "type": "function",
    "function": {
        "name": "工具名_英文蛇形",
        "description": "何时调用 + 何时不调用 + 边界说明",
        "parameters": {
            "type": "object",
            "properties": {
                "字段名": {
                    "type": "string",  # string / integer / number / boolean / array
                    "description": "这个参数是什么意思、举例",
                }
            },
            "required": ["必填字段"],
        },
    },
}
```

---

## 今日三个工具

| 工具 | name 建议 | 核心参数 |
|------|-----------|----------|
| 天气 | `get_weather` | `city`（必填） |
| 搜索 | `web_search` | `query`（必填）；`max_results`（可选） |
| 计算 | `calculator` | `expression`（必填） |

文件：`tool_schemas.py` 里已有 **好版** 和 **差版** 对比，跑一遍：

```powershell
cd E:\AI_agent_Quick
.\venv\Scripts\python.exe exercises\day20\tool_schemas.py
```

---

## description 质量 · 自测 4 题

读 `tool_schemas.py` 里 `BAD_*` vs `GOOD_*`，口头回答：

1. 差版 `get_weather` 的 description 缺了什么？（提示：用户问「深圳热不热」会不会调？）
2. `web_search` 为什么要写「不要用于数学计算」？
3. `calculator` 的 `expression` 字段 description 为什么要给例子？
4. 若模型把「广州天气」传成 `city: "广州市天河区"`，你会改 Schema 还是改 Prompt？

---

## 和 D14 / D15 / D19 的关系

| 天 | 你学了什么 | 今天补什么 |
|----|-----------|-----------|
| D14 | FC 结构演示 | 自己设计完整 Schema |
| D15 | 时间 + 计算器真调 | 计算器 description 可对照升级 |
| D19 | ReAct 文本 Action | Action 里的工具名 = 今天写的 `name` |

---

## 建议 2.5h 节奏

| 时段 | 内容 | 产出 |
|------|------|------|
| 0:00–0:25 | 复习 D14 + 读 README + 跑 `tool_schemas.py` | 能口述三字段 |
| 0:25–1:15 | 精读三个 GOOD schema；对比 BAD | 笔记 3 条 |
| 1:15–1:45 | 口头设计：若加 `get_air_quality` 怎么写 description | 口述 |
| 1:45–2:20 | 力扣 350 | 贴代码 |
| 2:20–2:30 | 「今日完成」+ 自评 | 更新文档 |

---

## 验收标准

1. 能口述：`name` / `description` / `parameters` 各干什么  
2. `tool_schemas.py` 三个 GOOD schema 能 `json.dumps` 打印  
3. 能举 1 个「差 description 导致调错工具」的例子  
4. 力扣 1 道（推荐 350）

---

## 力扣（课后）

推荐：[350. 两个数组的交集 II](https://leetcode.cn/problems/intersection-of-two-arrays-ii/)（349 进阶， multiset / Counter）
